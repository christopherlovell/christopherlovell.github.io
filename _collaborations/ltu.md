---
layout: page
title: Learning the Universe
description: The Learning the Universe Simons Collaboration
img: assets/img/ltu.jpg
importance: 1
category: Collaborations
related_publications: true
---

Learning the Universe (LtU) is a [Simons Collaboration](https://www.simonsfoundation.org/collaborations/) aiming to rapidly forward model the observable Universe in order to perform Bayesian inference with new Simulation Based Inference techniques, and learn both cosmological parameters as well as the initial conditions. You can learn more about the collaboration [here](https://learning-the-universe.org/).

<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/Learning-the-Universe-Summary-Figure.png" title="sims scheme" class="img-fluid rounded z-depth-1" width="500px" %}
    </div>
</div>
<div class="caption">
    The structure of the LtU approach, from initial conditions and cosmological parameters to fully forward modelled synthetic data.
</div>

I was involved in the development and testing of the LtU-ILI pipeline {% cite ho_ltu-ili_2024 %}, a framework for performing Implicit Likelihood Free inference (or Simulation Based Inference) in astrophysical and cosmological settings.
I also led a recent LtU paper applying synthesizer to the CAMELS simulation, using the LtU-ILI framework to perform cosmological and astrophysical parameter inference {% cite lovell_learning_2024 %}.
I have also explored the application of normalising flows for generative modelling of galaxy populations {% cite lovell_hierarchy_2023 %}.