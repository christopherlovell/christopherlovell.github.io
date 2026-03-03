---
layout: page
permalink: /tools/
title: tools
description: Interactive tools and web applications.
nav: true
nav_order: 6
---

<div class="summary-panel-grid mt-5">
  <!-- Cosmo Carta Section -->
  <div class="summary-panel">
    <a href="https://www.christopherlovell.co.uk/cosmo-carta/" target="_blank" rel="noopener noreferrer" class="summary-panel-summary" style="text-decoration: none; color: inherit;">
      {% include figure.liquid 
        path="assets/img/cosmo-carta.png" 
        class="summary-panel-image" 
        alt="Cosmo Carta"
      %}
      <div class="summary-panel-content">
        <h2>Cosmo Carta</h2>
        <p>
          An interactive viewer for numerical cosmological simulations on the volume-resolution plane.
        </p>
      </div>
    </a>
  </div>

  <!-- Sengi Section -->
  <div class="summary-panel">
    <a href="https://www.christopherlovell.co.uk/sengi/" target="_blank" rel="noopener noreferrer" class="summary-panel-summary" style="text-decoration: none; color: inherit;">
      {% include figure.liquid 
        path="assets/img/sengi.png" 
        class="summary-panel-image" 
        alt="Sengi"
      %}
      <div class="summary-panel-content">
        <h2>Sengi</h2>
        <p>
          Sengi is a small, fast, interactive viewer for spectral outputs from stellar population synthesis (SPS) models. 
          It uses Non-negative Matrix Factorisation (NMF) and bilinear interpolation to estimate output spectra.
        </p>
      </div>
    </a>
  </div>
</div>
