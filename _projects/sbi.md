---
layout: page
title: Simulation Based Inference
description: The latest techniques for Bayesian Inference
img: assets/img/ltu-ili.png
importance: 6
category: Projects
related_publications: true
---

[Simulation Based Inference](https://simulation-based-inference.org/) (SBI), or Likelihood-free inference, is a state of the art approach to Bayesian inference that leverages the power of modern numerical simulations alongside modern neural density estimation methods. For a review, see [Cranmer, Brehmer & Louppe 2020](https://www.pnas.org/doi/full/10.1073/pnas.1912789117).

I have recently been working on SBI approaches to a range of problems in physics. I was involved in the LtU-ILI suite {% cite ho_ltu-ili_2024 %}, a framework for performing SBI in cosmology and astrophysics. I applied this framework to forward modelled photometry from the CAMELS simulations {% cite lovell_learning_2024 %}, to perform parameter inference.
I've also been involved with a number of other projects utilising SBI approaches, for parameter inference and model comparison {% cite de_santi_robust_2023 de_santi_field-level_2023 %}.

<div class="row">
    <div class="mx-auto d-block" style="text-align: center;">
        {% include figure.liquid loading="eager" path="assets/img/sbi.png" title="sims scheme" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Figure showing the typical components and structure of an SBI methodology (courtesy of <a href="https://transferlab.ai/series/simulation-based-inference/">TransferLab</a>)
</div>

In 2024 we organised the first dedicated meeting on [Simulation Based Inference for Galaxy Evolution](https://sbi-galev.github.io/2024/). The [next installment](https://sbi-galev.github.io/2025/) is scheduled for 27th - 30th May 2025 - come and join us in Bristol!
