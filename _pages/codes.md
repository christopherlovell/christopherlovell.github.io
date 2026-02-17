---
layout: page
permalink: /codes/
title: codes
description: Selected software and repositories with live GitHub stats.
nav: true
nav_order: 5
---

{% if site.data.repositories.github_users and site.data.repositories.github_users.size > 0 %}
  {% assign primary_user = site.data.repositories.github_users.first %}
{% else %}
  {% assign primary_user = site.github_username %}
{% endif %}

<div class="codes-intro">
  <a class="button-link" href="https://github.com/{{ primary_user }}" target="_blank" rel="noreferrer">
    View full GitHub profile
  </a>
</div>

<div class="codes-grid">
  {% for repo in site.data.repositories.github_repos %}
    {% assign repo_parts = repo | split: "/" %}
    {% assign owner = repo_parts[0] %}
    {% assign name = repo_parts[1] %}
    <a class="code-pill" href="https://github.com/{{ repo }}" target="_blank" rel="noreferrer">
      <div class="code-pill-header">
        <span class="code-pill-icon"><i class="fa-brands fa-github"></i></span>
        <span class="code-pill-name">{{ name }}</span>
        <span class="code-pill-owner">{{ owner }}</span>
      </div>
      <p
        class="repo-about"
        data-github-repo="{{ repo }}"
        data-loading-text="Loading repository summary..."
        data-error-text="Repository summary unavailable right now."
        data-empty-text="No GitHub repository description provided."
      >
        Loading repository summary...
      </p>
      <div class="code-pill-stats">
        <img alt="{{ repo }} stars" loading="lazy" src="https://img.shields.io/github/stars/{{ repo }}?style=for-the-badge&label=Stars&labelColor=102a43&color=0f766e">
        <img alt="{{ repo }} forks" loading="lazy" src="https://img.shields.io/github/forks/{{ repo }}?style=for-the-badge&label=Forks&labelColor=102a43&color=0f766e">
        <img alt="{{ repo }} issues" loading="lazy" src="https://img.shields.io/github/issues/{{ repo }}?style=for-the-badge&label=Issues&labelColor=102a43&color=0f766e">
        <img alt="{{ repo }} updated" loading="lazy" src="https://img.shields.io/github/last-commit/{{ repo }}?style=for-the-badge&label=Updated&labelColor=102a43&color=0f766e">
      </div>
    </a>
  {% endfor %}
</div>
