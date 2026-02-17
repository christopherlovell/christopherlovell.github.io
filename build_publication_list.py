#!/usr/bin/env python3
import os
import re
import sys
import ads  # pip install ads

LIBRARY_ID = "x3_uMCyHTJ2-YisJxQxo_g"  # your ADS library id
ME = "Lovell, Christopher C."          # match your name as in ADS
ME_DISPLAY = "Christopher C. Lovell"

# Replace troublesome unicode with LaTeX-safe equivalents
UNICODE_MAP = {
    "≥": r"$\geq$",
    "≤": r"$\leq$",
    "Λ": r"$\Lambda$",
    "Ω": r"$\Omega$",
    "─": r"$-$",
    "<": r"$<$",
}

HTML_ENTITY_MAP = {
    "&lt;": r"$<$",
    "&gt;": r"$>$",
    "<SUB>": r"_{",
    "</SUB>": r"}",
    # "&": r"\&",
}

# Fields to pull; adjust if you want more
FIELDS = [
    "id", "title", "author", "year", "bibcode",
    "pub", "volume", "page", "doi", "arxiv_eprint", "identifier",
    "comment", "comments", "pubnote", "citation_count"
]

def fetch_library():
    token = os.getenv("ADS_DEV_KEY")
    if not token:
        raise SystemExit("Set ADS_DEV_KEY to your ADS API token.")
    ads.config.token = token

    # ADS limits rows per query; request enough to cover your library
    rows = 200
    papers = list(ads.SearchQuery(
        q=f"docs(library/{LIBRARY_ID})",
        fl=FIELDS,
        rows=rows,
        sort="date desc"
    ))
    return papers

def sanitize(text: str) -> str:
    if not text:
        return ""
    for bad, repl in HTML_ENTITY_MAP.items():
        text = text.replace(bad, repl)
    # Common HTML escaped journal strings
    text = text.replace("A\\&amp;A", "A\\&A")
    text = text.replace("A&amp;A", "A\\&A")
    text = text.replace("M&amp;NRAS", "MNRAS")
    for bad, repl in UNICODE_MAP.items():
        text = text.replace(bad, repl)
    # Guard against double math dollars that can appear if ADS already supplies $<$/$>$
    text = text.replace("$$<$", "$<$").replace("$$>$", "$>$")
    # Collapse any remaining double-$ introduced by mixed sources
    while "$$" in text:
        text = text.replace("$$", "$")
    # Fix cases where math is split, e.g. $\Omega$_{m} -> $\Omega_{m}
    text = text.replace(r"$\Omega$_{", r"$\Omega_{")
    # Handle omega sub m formatting consistently
    text = text.replace(r"$\Omega_{m}", r"$\Omega_{m}$")
    text = text.replace(r"\Omega_{m}", r"$\Omega_{m}$")
    # Handle molecular hydrogen consistently
    text = text.replace(r"$H_{2}", r"$H_{2}$")
    text = text.replace(r"H_{2}", r"$H_{2}$")
    # Collapse double-math for omega if present
    text = text.replace(r"$$\Omega_{m}$$", r"$\Omega_{m}$")
    return text


def normalize_token(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def split_author_name(author: str):
    author = sanitize(author).strip()
    if "," in author:
        last, given = author.split(",", 1)
        return given.strip(), last.strip()
    parts = author.split()
    if len(parts) >= 2:
        return " ".join(parts[:-1]), parts[-1]
    return author, ""


def format_author_name(author: str) -> str:
    given, last = split_author_name(author)
    return f"{given} {last}".strip()


def is_me_author(author: str) -> bool:
    me_given, me_last = split_author_name(ME)
    given, last = split_author_name(author)
    if normalize_token(last) != normalize_token(me_last):
        return False

    me_first = normalize_token(me_given.split()[0]) if me_given else ""
    given_tokens = [normalize_token(tok) for tok in given.split() if normalize_token(tok)]
    if not me_first or not given_tokens:
        return False
    return any(tok == me_first or tok.startswith(me_first[0]) for tok in given_tokens)


def slice_submitted(text: str) -> str:
    """Return substring starting at 'submitted to' if present (case-insensitive)."""
    if not text:
        return ""
    lower = text.lower()
    key = "submitted to"
    idx = lower.find(key)
    return text[idx:].strip() if idx != -1 else text.strip()

def to_latex_item(p):
    year = p.year or "????"
    title = sanitize(p.title[0] if p.title else "Untitled")
    authors_list = [str(a) for a in p.author] if p.author else []
    # Truncate authors: if ME in top three, keep top three; otherwise keep top two, then add suffix.
    suffix = ""
    if authors_list:
        me_in_top3 = any(is_me_author(a) for a in authors_list[:3])
        top_n = 3 if me_in_top3 else 2
        trimmed = []
        for raw_author in authors_list[:top_n]:
            formatted = format_author_name(raw_author)
            if is_me_author(raw_author):
                formatted = f"\\textbf{{{formatted}}}"
            trimmed.append(formatted)
        if len(authors_list) > top_n:
            suffix = " \\& others" if me_in_top3 else f" \\& others including {ME_DISPLAY}"
        authors = ", ".join(trimmed) + suffix
    else:
        authors = ""
    # try to recover an arXiv id
    arxiv_id = None
    if getattr(p, "arxiv_eprint", None):
        arxiv_id = p.arxiv_eprint
    elif getattr(p, "identifier", None):
        for ident in p.identifier:
            if ident.startswith("arXiv:"):
                arxiv_id = ident.split(":", 1)[1]
                break
    arxiv = f"\\href{{https://arxiv.org/abs/{arxiv_id}}}{{arXiv:{arxiv_id}}}" if arxiv_id else ""
    pub_parts = []
    is_arxiv_pub = getattr(p, "pub", None) and "arXiv" in p.pub
    def _as_str(val):
        if isinstance(val, (list, tuple)):
            return " ".join(str(v) for v in val)
        return str(val)

    if getattr(p, "pub", None) and not is_arxiv_pub:
        pub_parts.append(_as_str(p.pub))
    # If this is an arXiv-only entry, try to use the e-print comment (often contains "submitted to ...")
    if is_arxiv_pub:
        comment_text = None
        for attr in ("comment", "comments", "pubnote"):
            val = getattr(p, attr, None)
            if val:
                comment_text = _as_str(val)
                break
        if comment_text:
            comment_text = sanitize(comment_text)
            # Only keep comments that contain a submission/acceptance phrase and an allowed venue
            trigger_map = [
                ("submitted to", "Submitted to"),
                ("accepted for publication in", "Accepted for publication in"),
                ("accepted for publication", "Accepted for publication in"),
                ("accepted in", "Accepted in"),
                ("accepted", "Accepted in"),
                ("published as", "Published as"),
                ("published in", "Published in"),
                ("Paper submitted as part of the", "Paper submitted as part of the")
            ]
            venue_map = {
                "A\\&A Special Issue `Euclid Quick Data Release (Q1)'": "A\\&A Special Issue `Euclid Quick Data Release (Q1)'",
                "encyclopedia of astrophysics": "chapter for the Encyclopedia of Astrophysics",
                "a&a": "A\\&A",
                "a\\&a": "A\\&A",
                "mnras": "MNRAS",
                "apj": "ApJ",
                "apjl": "ApJL",
                "apjs": "ApJS",
                "jcap": "JCAP",
                "physical review letters": "Physical Review Letters",
                "nature": "Nature",
                "science": "Science",
                "a workshop paper at the ML4Astro Workshop at ICML 2025": "a workshop paper at the ML4Astro Workshop at ICML 2025",
                "the Open Journal of Astrophysics": "the Open Journal of Astrophysics",
                
            }
            lower_c = comment_text.lower()
            normalized = lower_c.replace("\\&", "&")
            trigger_found = None
            for key, canon in trigger_map:
                if key.lower() in normalized:
                    trigger_found = canon
                    break
            venue_found = None
            # Special-case: encyclopedia chapter without trigger wording
            if "encyclopedia of astrophysics" in normalized:
                venue_found = "chapter for the Encyclopedia of Astrophysics"
                trigger_found = ""
            for key, canon in venue_map.items():
                if key.lower() in normalized:
                    venue_found = canon
                    break
            if venue_found and trigger_found is not None:
                text_out = f"{trigger_found} {venue_found}".strip()
                pub_parts.append(text_out if text_out else venue_found)
            else:
                sys.stderr.write(f"[WARN] No trigger/venue match for '{title}' with comment '{comment_text}'\n")
    if getattr(p, "volume", None) and not is_arxiv_pub:
        pub_parts.append(_as_str(p.volume))
    if getattr(p, "page", None) and p.page and not is_arxiv_pub:
        pub_parts.append(_as_str(p.page[0]))
    pubinfo = sanitize(" ".join(pub_parts))
    entry = f"\\item \\textbf{{{year}:}} {title}. \\textit{{{authors}}}"
    if pubinfo:
        entry += f", {pubinfo}."
    else:
        entry += "."
    if arxiv:
        # avoid duplicating arXiv if pubinfo already indicates arXiv-only submission
        if not (is_arxiv_pub and "arxiv" in pubinfo.lower()):
            entry += f" {arxiv}"
    return entry

def split_first_author(papers):
    first_author, second_author, coauth = [], [], []
    for p in papers:
        if p.author and is_me_author(p.author[0]):
            first_author.append(p)
        elif p.author and len(p.author) > 1 and is_me_author(p.author[1]):
            second_author.append(p)
        else:
            coauth.append(p)
    return first_author, second_author, coauth


def compute_h_index(papers):
    citation_counts = []
    for p in papers:
        citations = getattr(p, "citation_count", 0) or 0
        try:
            citation_counts.append(int(citations))
        except (TypeError, ValueError):
            citation_counts.append(0)

    citation_counts.sort(reverse=True)
    h_index = 0
    for i, citations in enumerate(citation_counts, start=1):
        if citations >= i:
            h_index = i
        else:
            break
    return h_index


def render_section(title, items):
    out = [f"\\subsubsection*{{{title}}}", "\\begin{itemize}"]
    out.extend(items)
    out.append("\\end{itemize}\n")
    return "\n".join(out)

def main():
    papers = fetch_library()
    fa, sa, co = split_first_author(papers)
    total_count = len(papers)
    first_author_count = len(fa)
    h_index = compute_h_index(papers)

    fa_items = [to_latex_item(p) for p in fa]
    sa_items = [to_latex_item(p) for p in sa]
    co_items = [to_latex_item(p) for p in co]

    parts = [
        # "\\section*{Publications}",
        f"% ADS_STATS first_author_count={first_author_count} total_count={total_count} h_index={h_index}",
        render_section("First-Author", fa_items),
        render_section("Second-Author", sa_items),
        render_section("Co-Authored", co_items),
        "% Generated by build_publication_list.py"
    ]
    print("\n".join(parts))

if __name__ == "__main__":
    main()
