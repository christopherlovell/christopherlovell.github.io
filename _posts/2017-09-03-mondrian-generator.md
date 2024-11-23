---
title:  "D3 Mondrian Generator"
layout: post
comments: true
tags:
- Technology
date: "Sunday, September 3, 2017"
excerpt: Generating Mondrian-esque art with D3
og_image: /images/Mondrian.png
---

Weekend project: use D3 to generate artwork inspired by [Piet Mondrian](https://en.wikipedia.org/wiki/Piet_Mondrian) (see some examples [here](https://www.google.com/search?q=mondrian&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi_tYHAl4rWAhWs5YMKHbjGAEoQ_AUICigB&biw=1454&bih=733)). A gist of the code is available at the bottom of the page; to run locally, start up a python http server in the script directory:

`python -m SimpleHTTPServer`

Some ideas for future improvements:
- Choose colour scheme from a drop down list
- Choose the recursion level
- Resize the box dynamically
- Animate on refresh
- Sliders for colour ratios

Hit the *update* button to refresh!

<div id="option">
  <input name="updateButton"
         type="button"
         value="Update"
         onclick="update()" />
</div>

<br>

<div id='mondrian' style="display: table; margin: 0 auto">

<script src="https://d3js.org/d3.v4.js" charset="utf-8"></script>
<script>
    var w = 500;
    var h = 500;
    var padding = 30;
    var svg = d3.select("#mondrian")
      .append("svg")
      .attr("width", w)
      .attr("height", h)
      .attr("style", "outline: thick solid black;");
    var colours = ['red', 'blue', 'yellow', 'white', 'black']
    var colour_prob = [0.1, 0.1, 0.1, 0.6, 0.1]  // probability of appearance of each colour
    // cumulative colour probabilities
    var colour_cum_prob = [];
    colour_prob.reduce(function(a,b,i) { return colour_cum_prob[i] = a+b; },0);
    var fractions = [1/5, 2/5, 3/5, 4/5]  // hard coded split fractions
    var tol = 80;  // height/width tolerance on which to split
    var recurs = 7;  // level of recursion
    function update(){
      // initialise array of rectangles with a single, giant rectangle (..square)
      var rectangles = [{"x": 0, "y": 0, "width": w, "height": h}]
      // console.log("rect start", JSON.stringify(rectangles));
      var j = 0;  // recursion counter
      while(j < recurs){
        j++;
        n = rectangles.length;  // number of initial rectangles in this loop
        to_remove = [];  // array of indices of rectangles to remove
        // loop through existing rectangles
        for(var i=0; i<n; i++){
          // test if rectangle already small
          if(rectangles[i]['width'] > tol && rectangles[i]['height'] > tol){
            to_remove.push(i);  // save for removal later
            // calculate split fraction
            var frac = fractions[Math.floor(Math.random() * fractions.length)];
            var x = rectangles[i]['x'];
            var y = rectangles[i]['y'];
            // decide whether to cut vertically or horizontally
            if(Math.random() > 0.5) {
              var width = rectangles[i]['width'] * frac;
              var height = rectangles[i]['height'];
              rectangles.push({"x": x + width, "y": y, "width": rectangles[i]['width'] - width, height});
            }
            else {
              var width = rectangles[i]['width'];
              var height = rectangles[i]['height'] * frac;
              rectangles.push({"x": x, "y": y + height, "width": width, "height": rectangles[i]['height'] - height});
            }
            rectangles.push({"x": x, "y": y, "width": width, "height": height});
          }
        }
        // remove old rectangles (loop in reverse order to avoid messing up indexing)
        for(var i=to_remove.length-1; i>=0; i--){
            rectangles.splice(to_remove[i], 1);
        }
      }
      for(i=0; i < rectangles.length; i++){
        var condition = Math.random()
        colourIndex = colour_cum_prob.findIndex( function(elem) {return elem > condition} );
        svg.append("rect")
           .attr("x", rectangles[i]['x'] )
           .attr("y", rectangles[i]['y'] )
           .attr("width", rectangles[i]['width'] )
           .attr("height", rectangles[i]['height'] )
           .attr("fill", colours[colourIndex])
           .attr("stroke-width", 6)
           .attr("stroke", "black");
      }
    }
    update();

	</script>
</div>

<br>
<script src="https://gist.github.com/christopherlovell/9d532ce94c48c6ff4b9f97ef323e3c6a.js"></script>
