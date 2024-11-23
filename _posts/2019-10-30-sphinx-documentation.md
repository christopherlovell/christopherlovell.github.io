---
title:  "An introduction to creating Python documentation using Sphinx"
layout: post
comments: true
tags:
- Technology
date: "Wednesday, October 30, 2019"
excerpt: An introduction to creating Python documentation using Sphinx
---

Documentation: a god-send when it exists, but always bottom of the priority list when creating your own projects. Fortunately, Sphinx is here to make it (a bit) easier to document Python projects. Here's a quick, bare-bones run down of how to do it, and host it on [readthedocs](https://readthedocs.org/).

## Installation
I think the easiest way is to just use pip

    pip install -U sphinx

This way it's packaged with your environment, and you can easily update or remove it as needed. The downside is you will have a separate install for each environment, so if disk space is a concern this isn't the best approach, and you might want to choose another option [here](http://www.sphinx-doc.org/en/master/usage/installation.html).

## Quickstart
Navigate to your project directory, and create a `docs` folder.

    mkdir docs
    cd docs

Then you can run `sphinx-quickstart` in this directory.

    sphinx-quickstart

This will ask you a few questions, which you can answer yes to the defaults to in most cases. I like to separate the source and build directories to make managing the documentation with git easier.

## Build the docs
It's as simple as running `make` with the format desired in the `docs` directory. For example, for html:

    make html


## Push to github
Your project is all up to date in source control, right? Good. (If not, go sort that out now).

Commit and push your new docs. You can ignore the `build` folder and just add the make files and contents of the `source` folder.


## Deploy to Read the docs
If you upload your code as-is to _readthedocs_ your build will initially fail. This is because _readthedocs_ by default assumes that the default master document is `conf.rst`, not `index.rst`. To fix it, just add this line anywhere within `source/conf.py` (I stuck mine at the bottom with a 'custom features' comment).

    master_doc = 'index'

Then go to [readthedocs.org](https://readthedocs.org), sign up, and search for your repository. You should then be able to just follow the instricutions and build your beautiful documentation.

