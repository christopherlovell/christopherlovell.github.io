#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "publications.tex"
OUT = ROOT / "_includes" / "publications_generated.html"


def load_items():
    text = SRC.read_text(encoding="utf-8")
    sections = {}
    stats = {}
    current = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("% ADS_STATS"):
            for key, value in re.findall(r"(\w+)=([0-9]+)", line):
                stats[key] = int(value)
            continue
        if line.startswith(r"\subsubsection*"):
            name = re.search(r"\{(.+?)\}", line).group(1)
            current = name
            sections[current] = []
        elif line.startswith(r"\item") and current:
            item = line[len(r"\item") :].strip()
            sections[current].append(item)
    return sections, stats


def latex_to_html(s: str) -> str:
    s = s.replace(r"\&", "&")
    s = s.replace(r"\$", "$")
    s = s.replace(r"$\geq$", "≥").replace(r"$\leq$", "≤")
    s = s.replace(r"$\Lambda$", "Λ").replace(r"$\Omega_{m}$", "Ωₘ")
    s = s.replace(r"$<$", "&lt;").replace(r"$>$", "&gt;")
    s = s.replace(r"---", "—").replace(r"--", "–")
    s = re.sub(r"\\textbf\{(.+?)\}", r"<strong>\1</strong>", s)
    s = re.sub(r"\\textit\{(.+?)\}", r"<em>\1</em>", s)
    s = re.sub(r"\\href\{(.+?)\}\{(.+?)\}", r'<a href="\1" target="_blank" rel="noreferrer">\2</a>', s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def render_list(title, items):
    lis = "\n".join(f"      <li>{latex_to_html(i)}</li>" for i in items)
    return f"""  <section class=\"pub-block\">\n    <h2>{title}</h2>\n    <ul>\n{lis}\n    </ul>\n  </section>"""


def render_stats(stats, first_items, second_items, co_items):
    first_count = stats.get("first_author_count", len(first_items))
    total_count = stats.get("total_count", len(first_items) + len(second_items) + len(co_items))
    h_index = stats.get("h_index")
    h_value = str(h_index) if h_index is not None else "N/A"

    return f"""<section class=\"publications-stats\" aria-label=\"ADS library metrics\">
  <article class=\"publications-stat-card\">
    <p class=\"publications-stat-label\">First-author papers</p>
    <p class=\"publications-stat-value\">{first_count}</p>
  </article>
  <article class=\"publications-stat-card\">
    <p class=\"publications-stat-label\">Total papers</p>
    <p class=\"publications-stat-value\">{total_count}</p>
  </article>
  <article class=\"publications-stat-card\">
    <p class=\"publications-stat-label\">h-index (library)</p>
    <p class=\"publications-stat-value\">{h_value}</p>
  </article>
</section>
"""


def is_second_author_item(item: str) -> bool:
    me_name_pattern = r"(?:Christopher C\.|C\.\s*C\.)\s+Lovell|Lovell,\s*(?:Christopher C\.|C\.\s*C\.)"
    # Exclude truncated entries where the explicit order is unknown.
    if re.search(
        rf"others including\s+(?:\\textbf\{{)?(?:{me_name_pattern})",
        item,
    ):
        return False
    # Match either old style "Last, First" or new style "First Last".
    return bool(
        re.search(
            rf"\\textit\{{[^}}]*,\s*\\textbf\{{(?:{me_name_pattern})",
            item,
        )
    )


def build_fragment(sections, stats):
    first_items = list(sections.get("First-Author", []))
    second_items = list(sections.get("Second-Author", []))
    co_items = list(sections.get("Co-Authored", []))

    # Backward compatibility: older publications.tex has no dedicated second-author section.
    if not second_items and co_items:
        inferred_second = [item for item in co_items if is_second_author_item(item)]
        if inferred_second:
            second_items = inferred_second
            co_items = [item for item in co_items if item not in inferred_second]

    top_blocks = []
    if first_items:
        top_blocks.append(render_list("First-Author", first_items))
    if second_items:
        top_blocks.append(render_list("Second-Author", second_items))

    full_width_blocks = []
    if co_items:
        full_width_blocks.append(render_list("Co-Authored", co_items))

    # Preserve any additional sections if present.
    for name, items in sections.items():
        if name not in {"First-Author", "Second-Author", "Co-Authored"}:
            full_width_blocks.append(render_list(name, items))

    top_html = ""
    if top_blocks:
        top_html = "<div class=\"publications-top-grid\">\n" + "\n".join(top_blocks) + "\n</div>\n"
    full_html = ""
    if full_width_blocks:
        full_html = "<div class=\"publications-bottom-stack\">\n" + "\n".join(full_width_blocks) + "\n</div>\n"

    stats_html = render_stats(stats, first_items, second_items, co_items)
    html = f"""{stats_html}<div class=\"publications-layout\">\n{top_html}{full_html}</div>\n"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")


def main():
    sections, stats = load_items()
    build_fragment(sections, stats)


if __name__ == "__main__":
    main()
