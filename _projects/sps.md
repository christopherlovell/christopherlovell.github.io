---
layout: page
title: Stellar Population Synthesis
description: Modelling stellar populations, for observational and theoretical applications
img: assets/img/sps.png
importance: 8
category: Projects
related_publications: true
---

Stellar Population Synthesis (SPS) is a key ingredient in forward models for galaxy emission (see [Conroy 2013](https://ui.adsabs.harvard.edu/abs/2013ARA%26A..51..393C/abstract)).

I have used SPS models in a wide range of projects. Most recently, [Sophie Newman](https://sophie-newman.github.io/), a student at the ICG, used the CLOUDY photoionization code to explore the line and continuum emission properties of young star forming regions {% cite newman_cloudy-maraston_2025 %}, utilising our [Synthesizer code](/projects/synthesizer).

<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/sps-long.png" title="sims scheme" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Stellar, nebular line and continuum emission components from the M24 Maraston models {% cite newman_cloudy-maraston_2025 %}.
</div>

I have also developed an online tool, [Sengi](https://www.christopherlovell.co.uk/sengi/), for exploring SPS models in an interactive way. Details on the implementation are published in {% cite lovell_sengi_2021 %}.

