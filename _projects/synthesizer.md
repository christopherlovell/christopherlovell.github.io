---
layout: page
title: Synthesizer & Forward Modelling
description: Software for generating synthetic astronomical observables
img: assets/img/synthesizer_logo.png
importance: 1
category: Projects
related_publications: true
---

In order to compare simulations and observations we traditionally perform inverse modelling, or SED fitting, and compare in some physical property space.
An alternative approach is to forward model numerical simulations directly to the observational space.
This avoids many of the uncertainties and biases inherent to inverse modelling, and provides a new space to compare and understand our models.
I have written codes and performed analysis of forward modelled simulations in a wide range of projects.
Most of my time now is spent developing and working with Synthesizer.

<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/motivation_synthesizer.png" title="sims scheme" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Figure showing the various points at which models and observations can be compared, and inverse (green) and forward (blue) modelling approaches.
</div>

Synthesizer is a python package for generating synthetic astrophysical observables. It is designed to be modular, extensible, flexible and fast.
The code is hosted on [GitHub](https://github.com/synthesizer-project/synthesizer), and comprehensive documentation is provided [here](https://flaresimulations.github.io/synthesizer/).

<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/synthesizer-flowchart.png" title="sims scheme" class="img-fluid rounded z-depth-1" width="550px" %}
    </div>
</div>
<div class="caption">
    Flowchart showing some of the main modules and functionality in Synthesizer.
</div>

Some papers that have used Synthesizer include {% cite lovell_learning_2024 %} and {% cite newman_cloudy-maraston_2025 %}. Synthesizer is based on codes developed for a number of previous papers, including {% cite wilkins_nebular_2020 %} and {% cite vijayan_first_2021 %}.
It is also meant to complement full dust radiative transfer approaches, in codes such as Powderday {% cite narayanan_powderday_2021 %}.
