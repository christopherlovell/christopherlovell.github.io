---
layout: page
title: Machine Learning & AI
description: Leveraging the latest AI technologies 
img: assets/img/ml.webp
importance: 4
category: Projects
related_publications: true
---

I have used machine / deep learning methods, and AI approaches more generally, in a number of different projects.
These include direct application to observational data, to increase the accuracy and speed of predictions.

Most of my applications of these methods has, however, been to increase the efficiency and applicability of numerical simulations.
Asd an example, in {% cite lovell_machine_2022 %} we used simple tree based regression methods to learn the galaxy-halo relationship in a series of zoom simulations, and then apply this back to a large parent only volume.
This allowed us to predict clustering statistics over large volumes and dynamic ranges, but using the results of high fidelity hydrodynamic simulations.

<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/ml-haloes.png" title="sims scheme" class="img-fluid rounded z-depth-1" width="500px" %}
    </div>
</div>
<div class="caption">
    Figure showing the frameowrk used in {% cite lovell_machine_2022 %} to learn the galaxy-halo relationship from a series of zooms, and apply to a larent dark-matter only parent simulation.
</div>

In {% cite lovell_hierarchy_2023 %} we extended this framework using the [CAMELS simulations](/collaborations/camels) combined with normalising flows, for probabilistic modelling of the galaxy-halo relationship.
Finally, Maxwell Maltz, a student at the University of Sussex, has explored adding quantitative scatter to tree based predictions, to better recover the covariances in common distribution functions {% cite maltz_first_2024 %}.

I have also explored convolutional neural networks applied to spectra for star formation history recovery {% cite lovell_learning_2019 %}.
With collaborators I have worked on tree models applied to synthetic absorption spectra {% cite appleby_mapping_2023 %}, graph neural networks and symbolic regression for cosmological inference {% cite shao_universal_2023 %}, dimensionality reduction techniques for representing [SPS models](/projects/sps) {% cite lovell_sengi_2021 %}, and explored how to estimate generalization error {% cite acquaviva_debunking_2020 %}.

[Simulation Based Inference](/projects/sbi) approaches can be considered a branch of AI / deep learning, and I have done considerable work applying these methods to numerical simulations {% cite lovell_learning_2024 %}.