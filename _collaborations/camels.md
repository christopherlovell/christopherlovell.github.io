---
layout: page
title: CAMELS
description: Cosmology and Astrophysics with MachinE Learning Simulations
img: assets/img/camels.jpg
importance: 1
category: Collaborations
related_publications: true
---

CAMELS is "a project that aims at building bridges between cosmology and astrophysics through numerical simulations and machine learning". You can read more about CAMELS [here](https://www.camel-simulations.org/).

<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/camels_sims_scheme.webp" title="sims scheme" class="img-fluid rounded z-depth-1" width="500px" %}
    </div>
</div>
<div class="caption">
    Schema showing the structure of the CAMELS suite of simulations.
</div>

I have produced synthetic photometric catalogues for CAMELS {% cite lovell_learning_2024 %} using our Synthesizer code; this catalogue of over 200 million individual sources is one of the largest sets of synthetic photometry produced from a hydrodynamic simulation to date.
I have also explored the application of normalising flows for generative modelling of galaxy populations {% cite lovell_hierarchy_2023 %}.

I also ran the Swift-EAGLE model as part of the suite of simulations (Lovell et al. in prep.).
Below is a video of the evolution of one of the Swift-EAGLE runs, with gas density in blue and gas temperature in red.

<div class="row">
    <div class="col-sm mx-auto d-block" style="text-align: center; margin-bottom: 1cm;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/XDpBT6JwRAE?si=9-crxJZT31CEKei_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""></iframe>
    </div>
</div>

I have also been involved in a number of other CAMELS studies, including measurement of the impact of baryons on matter clustering {% cite gebhardt_cosmological_2024 %}, symbolic regression combined with graph neural networks {% cite shao_universal_2023 %} and field level likelihood free inference {% cite de_santi_field-level_2023 de_santi_robust_2023 %}.
