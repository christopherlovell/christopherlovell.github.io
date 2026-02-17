(() => {
  const nodes = Array.from(document.querySelectorAll(".repo-about[data-github-repo]"));
  if (!nodes.length) {
    return;
  }

  const CACHE_TTL_MS = 12 * 60 * 60 * 1000;
  const cacheKey = (repo) => `repo-about:${repo}`;

  const readCache = (repo) => {
    try {
      const raw = localStorage.getItem(cacheKey(repo));
      if (!raw) {
        return null;
      }
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") {
        return null;
      }
      if (typeof parsed.ts !== "number" || typeof parsed.description !== "string") {
        return null;
      }
      if (Date.now() - parsed.ts > CACHE_TTL_MS) {
        return null;
      }
      return parsed.description;
    } catch {
      return null;
    }
  };

  const writeCache = (repo, description) => {
    try {
      localStorage.setItem(
        cacheKey(repo),
        JSON.stringify({ ts: Date.now(), description: description || "" }),
      );
    } catch {
      // Ignore storage failures (private mode, quota, etc.).
    }
  };

  const setDescription = (elements, description) => {
    const text = (description || "").trim();
    const state = text ? "ready" : "empty";
    elements.forEach((el) => {
      el.textContent = text;
      el.dataset.state = state;
    });
  };

  const grouped = nodes.reduce((acc, el) => {
    const repo = el.dataset.githubRepo;
    if (!repo) {
      return acc;
    }
    if (!acc[repo]) {
      acc[repo] = [];
    }
    acc[repo].push(el);
    return acc;
  }, {});

  const loadDescription = async (repo, elements) => {
    const cached = readCache(repo);
    if (cached !== null) {
      setDescription(elements, cached);
      return;
    }

    try {
      const response = await fetch(`https://api.github.com/repos/${repo}`, {
        headers: {
          Accept: "application/vnd.github+json",
        },
      });
      if (!response.ok) {
        throw new Error(`GitHub API error: ${response.status}`);
      }
      const payload = await response.json();
      const description =
        payload && typeof payload.description === "string" ? payload.description : "";
      writeCache(repo, description);
      setDescription(elements, description);
    } catch {
      setDescription(elements, "");
    }
  };

  Object.entries(grouped).forEach(([repo, elements]) => {
    loadDescription(repo, elements);
  });
})();
