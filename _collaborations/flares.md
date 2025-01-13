---
layout: page
title: FLARES
description: The First Light And Reionisation Epoch Simulations
img: assets/img/flares.png
importance: 1
category: Collaborations
related_publications: true
---

Cosmological hydrodynamic simulations have, in recent years, become capable of matching key distribution functions in the local universe, such as those of stellar mass and star formation rate.
However, high resolution, large volume simulations  have rarely been tested in the high redshift (z > 5) regime, particularly in the most overdense environments.
Creating models that fit both high redshift and low redshift observables self consistently is a significant challenge, but key to understanding the properties of galaxies in the first billion years of the universe's history, and how this affects their latter evolution.
Such models are also necessary to make detailed predictions, and plan observations, for upcoming space based instruments, such as JWST, WFIRST and Euclid.


<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/baryonic_volume.png" title="sims scheme" class="img-fluid rounded z-depth-1" width="500px" %}
    </div>
</div>
<div class="caption">
    Figure of merit showing the general anti-correlation between simulation resolution and volume probed. FLARES is able to break this correlation, and explore much larger effective volumes at high fidelity.
</div>

<a href="https://www.flaresimulations.github.io/" target="source">The First Light And Reionisation Epoch Simulations (FLARES)</a> are one approach to these issues.
FLARES consists of a suite of 40 'zoom' simulations using a modified version of the <a href="http://icc.dur.ac.uk/Eagle/" target="blank">EAGLE</a> code.
We selected regions at high redshift, with a range of overdensities, from an enormous periodic dark matter-only volume, and resimulated these with full hydrodynamics at fiducial EAGLE resolution.

I led the first release paper {% cite lovell_first_2021 %} in which we study predictions for the galaxy stellar mass function, star formation rate function and star-forming sequence as a function of environment.
I also led a paper studying passive galaxy populations in the high redshift (z > 5) regime {% cite lovell_first_2023 %}. 
Further work with the FLARES suite is described in {% cite vijayan_first_2021 vijayan_first_2022 roper_first_2022 wilkins_first_2022 dsilva_unveiling_2023 roper_flares_2023 wilkins_first_2023 wilkins_first_2023-1 seeyave_first_2023 thomas_first_2023 vijayan_first_2024 wilkins_first_2023-2 wilkins_first_2024 punyasheel_first_2024 wilkins_first_2024-1 maltz_first_2024 %}
