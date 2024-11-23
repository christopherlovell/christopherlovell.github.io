---
layout: post
title: "Download D3 vis using SVG crowbar"
comments: true
date: "Wednesday, September 22, 2015"
tags:
- Technology
excerpt: How to extract D3 visualisations through the browser using SVG crowbar
---

You can find D3 almost everywhere on the web now, and often you'll want to grab a visualisation to use elsewhere. In particular, you may want to capture a particular state of an interactive visualisation after playing with some parameters. Since it's not an image *per se*, you can't just right click and download it. You could print the entire page, but then you have to crop it and risk losing the resolution. Fortunately there is a solution, developed by the New York times no less, that grabs the raw SVG and downloads it for you. The bookmark is available [here](http://nytimes.github.io/svg-crowbar/), and you can drag and drop it to your bookmarks bar for ease of use later. Try it on this interactive bilevel partition visualisation [here](http://bl.ocks.org/mbostock/5944371). The image below shows an example output.

<a href="/images/bilevel-partition.svg" data-lightbox="bilevel-partition" data-title="bilevel-partition">
  <img src="/images/bilevel-partition.svg" title="bilevel-partition">
</a>

An SVG is a useful image format; it allows you to do further editing in Photoshop or other image editing software later, such as adding layers or changing colours. If necessary, you can convert this to a jpeg or other static formats.
