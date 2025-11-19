---
layout: page
permalink: /publications/
title: publications
description: Publications in reverse chronological order. 
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

You can also view my publications on [ADS](https://ui.adsabs.harvard.edu/public-libraries/x3_uMCyHTJ2-YisJxQxo_g) and [Google Scholar](https://scholar.google.com/citations?user=2wlPQ1QAAAAJ&hl=en)[...]

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% comment %}
  Guard the bibliography tag so we don't invoke the bibliography renderer
  when no bibliography is configured. Some bibliography processors expect
  certain fields and can raise errors (e.g. calling numeric? on nil).
{% endcomment %}
{% if site.bibliography %}
  {% bibliography %}
{% else %}
  <p>No bibliography configured. If you expect publications to render here, add a bibliography file and set `bibliography:` in _config.yml (or enable the bibliography plugin).</p>
{% endif %}

</div>
