---
layout: post
title: "Survey Bias"
comments: true
date: "Thursday, May 12, 2016"
tags:
- Physics
excerpt: Overview of two of the main biases seen in astronomical surveys
---

> *A quick overview of two of the main biases seen in astronomical surveys*

**Eddington Bias** is introduced by measurement error. If you measure a collection of different sources that all have the same intrinsic luminosity, your observations will show a scatter introduced by the measurement errors. This isn't too much of an issue on its own, but when combined with another collection of objects at a similar but distinct luminosity, the distributions of measurements might overlap. This presents a problem when the sizes of each collection are different. If the first collection has more objects than the second, many of your observations of the first will scatter in to the second, but not as many will scatter from the second in to the first. You'll then end up underestimating the number of sources in your first collection, and overestimating the number in your second.

A further complication is introduced if your survey has a detection threshold. Imagine that the intrinsic luminosity of a collection of objects is close to the threshold, and the scatter due to measurement error actually exceeds this threshold. You'll only see those objects that appear above the threshold. The luminosity derived from these sources will be higher than the one you'd get if you had access to all of the sources. So, you overestimate the luminosity of the collection.

**Malmquist Bias** is a selection bias, due to the fact that at greater distances you can only see the brightest sources. This is mostly an issue if your survey is flux limited, where sources below a certain flux are undetectable, rather than volume limited, where objects within a given volume are identified. In the flux limited case the brightest objects will be more numerous than the faint, as they are being sampled from a larger volume.
