---
layout: page
title: FLARES
description: The First Light And Reionisation Epoch Simulations
img: assets/img/flares.png
importance: 1
category: Collaborations
related_publications: true
---


<h2><a name="FLARES">First Light And Reionisation Epoch Simulations (FLARES)</a></h2>

Cosmological hydrodynamic simulations have, in recent years, become capable of matching key distribution functions in the local universe, such as those of stellar mass and star formation rate.
However, high resolution, large volume simulations  have rarely been tested in the high redshift ($z > 5$) regime, particularly in the most overdense environments.
Creating models that fit both high redshift and low redshift observables self consistently is a significant challenge, but key to understanding the properties of galaxies in the first billion years of the universe's history, and how this affects their latter evolution.
Such models are also necessary to make detailed predictions, and plan observations, for upcoming space based instruments, such as JWST, WFIRST and Euclid.

<img class="small" src="/images/all_components.png" title="FLARES components">
<p style="text-align:center; font-style:italic">The column density of gas, stars and dark matter in the most overdense region in the FLARES sample.</p>

<a href="https://www.flaresimulations.github.io/" target="source">The First Light And Reionisation Epoch Simulations (FLARES)</a> are one approach to these issues.
FLARES consists of a suite of 40 'zoom' simulations using a modified version of the <a href="http://icc.dur.ac.uk/Eagle/" target="blank">EAGLE</a> code.
We selected regions at high redshift, with a range of overdensities, from an enormous periodic dark matter-only volume, and resimulated these with full hydrodynamics at fiducial EAGLE resolution.
I led the first release paper (<a href="https://arxiv.org/abs/2004.07283">Lovell et al 2021; arXiv:2004.07283</a>) in which we study predictions for the galaxy stellar mass function, star formation rate function and star-forming sequence.
Below is an introductory talk that I gave at the 2020 SAZERAC meeting (with awkward slide transition requests due to a technical error...!).


Every project has a beautiful feature showcase page.
It's easy to include images in a flexible 3-column grid format.
Make your photos 1/3, 2/3, or full width.

To give your project a background in the portfolio page, just add the img tag to the front matter like so:

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images, even citations {% cite einstein1950meaning %}.
Say you wanted to write a bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
