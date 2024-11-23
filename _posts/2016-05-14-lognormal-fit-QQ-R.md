---
layout: post
title: "Log-normal fitting and Q-Q plots in R"
comments: true
date: "Saturday, May 14, 2016"
tags:
- Data Science
excerpt: Fitting to a log-normal distribution in R, and generating QQ plots for large data sets
---

This week I had the pleasure of fitting a log-normal distribution to some pretty big data. Since I already had code to read in the data in R, that's what I used to do the fit. A bit of googling predictably threw up about twenty different ways of doing it, in an array of different packages, so I tried and tested a few but found that many didn't handle the size of my data very well, and none of them allowed me to generate Q-Q plots, most just hanging and crashing my session.

So, I coded it up by hand. The Gist at the bottom of the page generates some random data, adds a bit of noise, then fits a log-normal using the `fitdistr` function from the `MASS` package. `MASS` has been around for almost 15 years now, from back when R was S, and has a ton of well tested functions that a whole [bunch of other packages](https://cran.r-project.org/web/packages/MASS/index.html) depend on. In other words, it's legit. It then plots a histogram of the data against the fitted log-normal, generates quantiles for the fitted and original data, and plots them against each other in a Q-Q plot.

Here's a histogram of the clean generated data with 50 breaks.

![hist](/images/lognormal/hist.png)

Here's a line plot of the same histogram with a higher number of breaks, alongside the fit.

![hist](/images/lognormal/density_hist.png)

And the Q-Q plot.

![hist](/images/lognormal/QQ.png)

The fit with the noise is visibly off around the peak.

![hist](/images/lognormal/density_hist_noise.png)

The Q-Q plot shows that most of the difference is actually in the high value tail of the distribution.

![hist](/images/lognormal/QQ_noise.png)


{% gist f5370022030f48198ffdd85eab8f1fa2 %}
