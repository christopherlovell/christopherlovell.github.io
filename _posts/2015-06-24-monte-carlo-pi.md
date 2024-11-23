---
layout: post
title: "Using Monte Carlo methods to estimate pi"
comments: true
date: "Wednesday, June 24, 2015"
tags:
- Data Science
excerpt: A brief post on how to find the value of pi, using the law of large numbers and bit of introductory Julia.
---

You've just bought a brand new computer. You excitedly rip open the packaging, carefully extract it from the box, remove the protective film from the screen (so satisfying) and, after 10 hours of charging, boot it up. It turns on fine, and everything seems to be functioning normally. It's only after a few minutes of use that you discover, to your horror, that the manufacturer has forgotten to store the constant $\pi$ on the operating system. How are you going to play [Kerbal space program](https://kerbalspaceprogram.com/en/) if you can't calculate the equations of motion of your rockets and space probes?!

One way around this is to use Monte Carlo methods, taking advantage of the law of large numbers to gain a reasonable approximation of pi to a few decimal places. In this post I'll demonstrate this using Julia (we'll conveniently ignore the fact that Julia has the number $\pi$ in it), which I've just started learning and having a play with.

Take a square of side $a$, centred on the origin. Now place a circle inside the box with radius $a/2$, also centred on the origin. The area of the rectangle is $a^2$, and the area of the circle is $\pi(a/2)^2$.

{% highlight julia %}
using DataArrays, DataFrames
using Gadfly
using Compose

set_default_plot_size(10cm,10cm)

compose(context(),
  (context(),circle(0.5,.5,0.5),fill("tomato")),
  (context(),rectangle(0.,0.,1,1),fill("black"))
)
{% endhighlight %}

<br>  

<a href="/assets/monte-carlo-pi/output_1_0.svg" data-lightbox="Circle in rectangle" data-title="Circle in rectangle">
  <img class="small" src="/assets/monte-carlo-pi/output_1_0.svg" title="Circle in rectangle">
</a>

<br>

If we take any random point within the rectangle, then the probability that this point lies within the circle, $P(circle)$, is equal to the area of the circle relative to the area of the rectangle. i.e,

$$P(circle)=\frac{A\_{circle}}{A\_{square}}=\frac{\pi (a/2)^2}{a^2}$$


If we take $n$ points, then as $n$ gets very large the fraction of points that lie within the circle will converge to the probability of landing in the circle, $P(circle)$.

Expanding and rearranging our equation above for $\pi$,

$$\pi = 4\times P(circle)$$

Below is a Julia script for doing just this. $n$ samples from a bivariate uniform range $[0,1]$ are taken, and used as coordinates $(x,y)$ centred on the origin. For each coordinate a distance from the origin is calculated; if this exceeds the radius of the circle then it must lie outside, if not the point is within the circle. The sum of points in the circle is divided by the total number of points taken to give the probability of points in the circle. We can then use the equation above to estimate $\pi$.

The plot shows a sample of the coordinates generated, coloured by whether they lie in or out of the circle.

{% highlight julia %}
n = 1000000

df = DataFrame()
df[:x] = 0.5 - rand(n)
df[:y] = 0.5 - rand(n)
df[:c] = Array(String, n)
df[:r] = Array(Float64, n)

for i = 1:n
    df[i,:r] = (df[i,:x]^2 + df[i,:y]^2)^.5
    if df[i,:r] < 0.5
        df[i,:c] = "in"
    else
        df[i,:c] = "out"
    end
end

circle_df = DataFrame()
circle_df[:c] = cos(-pi:0.01:pi)/2
circle_df[:s] = sin(-pi:0.01:pi)/2

set_default_plot_size(15cm,15cm)

plot(df[sample(1:size(df, 1), iceil(0.001 * size(df, 1))), :], x="x", y="y", color="c", Geom.point,Coord.cartesian(fixed=true),
Guide.Annotation(compose(context(),circle(0,0,0.5), fill(nothing), stroke("orange"))))
{% endhighlight %}

<a href="/assets/monte-carlo-pi/output_3_0.svg" data-lightbox="Point distribution" data-title="Point distribution">
  <img class="small" src="/assets/monte-carlo-pi/output_3_0.svg" title="Point distribution">
</a>


{% highlight julia %}
print("pi ~ ",4*sum(df[:c] .== "in")/n)
pi ~ 3.138924
{% endhighlight %}
