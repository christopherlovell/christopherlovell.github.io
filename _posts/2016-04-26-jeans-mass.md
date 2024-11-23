---
layout: post
title: "Deriving the Jean's Mass"
comments: true
date: "Tuesday, April 26, 2016"
tags:
- Physics
cover: /images/small_magellanic_cloud.jpg
excerpt: Two approaches to deriving the mass scale for gravitational collapse
---

The early universe was a pretty uninteresting place, an expanse of neutral hydrogen with a few marginally heavier elements scattered around. It wasn't until overdense regions of gas started to collapse and condense that stars and galaxies formed. But this collapse only occurs under the right conditions; the gravitational collapse must first overcome the internal pressure of the cloud of gas. There is therefore a balancing act between internal pressure and gravitational contraction.


When the cloud is stable it is in what's known as hydrostatic equilbrium, which for a spherical cloud is given by

$$\frac{dp}{dr}=-\frac{G\rho(r) M(r)}{r^2}$$

Here, $r$ is the radius, $M(r)$ is the mass enclosed at radius $r$, $p$ is the pressure, $\rho(r)$ is the density at $r$, and $G$ is the gravitational constant. The pressure is temperature dependent, so, for a given temperature, if the mass exceeds a threshold value the cloud will collapse.  

This mass is known as the Jean's Mass, after the British physicist Sir James Jeans who first derived it. There are two ways of deriving it, one from energy considerations using the virial mass, and another by looking at the sound crossing speed and gravitational free fall time. We'll look at both, and see that dimensionally they both give the same result, give or take a small constant.

In a future post we'll look at the conditions in the early universe, and scaling with the expansion factor, to find the approximate sizes of the first collapsed objects that led to the first stars and galaxies.

## Ratio of Timescales
In this derivation, we imagine a spherical gas cloud that has just started to collapse gravitationally. The characteristic time over which this collapse would take is known as the **free fall time**. Once the collapse starts, pressure is exerted on the cloud, which sends out sound waves through the cloud. These take time to travel through the cloud and back to re-establish pressure balance This is known as the **sound crossing time**.

If the *sound crossing time* is shorter than the *free fall time* then the cloud will remain in equilibirum; the pressure will counteract the gravitational collapse. If the *free fall time* is shorter than the *sound crossing time* then the gravitational collapse continues unabated, and the cloud collapses.

The free fall time can be derived by looking at a particle on the edge of the cloud (at radius $R$). It feels an acceleration from the rest of the cloud $g = -\frac{GM}{R^{2}}$, where $M$ is the total mass of the cloud (equal to the volume of the cloud at the start of collapse times the average density, $M = \frac{4\pi }{3}R_{0}^{3} \rho_{0}$); this makes use of the divergence theorem from electrostatics, whereby the point mass only feels the gravitational force from the mass interior to its radius

Using Newton's second law we can write the equation of motion of the cloud,

$$\frac{d^{2}R}{dt^{2}} = \left(\frac{-G}{R^{2}}\right) \left( \frac{4\pi R_{0}^{3}\rho}{3}\right)$$

Can rewrite the left hand side with the chain rule

$$\frac{d^{2}R}{dt^{2}}=\frac{d}{dt}v=\frac{dR}{dt}\frac{d}{dR}v=v\frac{dv}{dR}$$

$$v \, \frac{dv}{dR}=-\frac{4\pi \, G R_{0}^{3}\rho}{3 \, R^{2}}$$

Can now integrate this differential equation

$$\int v \, dv = - \frac{4\pi G R_{0}^{3}\rho_{0}}{3} \int \frac{dR}{R^2} $$

$$\frac{1}{2}\,v^{2}=\frac{4\pi G R_{0}^{3}\rho_{0}}{3R} + C$$

When $R = R_{0}$, i.e. when the particle is at it's start position, we assume it is at rest, $v = 0$. Substituting, we can find $C$,

$$C=-\frac{4\pi G R_{0}^{2}\rho_{0}}{3}$$

$$\frac{1}{2}\,v^{2}=\frac{4\pi G R_{0}^{3}\rho_{0}}{3R} -\frac{4\pi G R_{0}^{2}\rho_{0}}{3}$$

$$\frac{1}{2}\,v^{2}=\frac{4\pi G R_{0}^{2}\rho_{0}}{3}  \left( \frac{R_{0}}{R} - 1 \right)$$

$$|v| = \sqrt{\frac{8 \pi G \rho R_{0}^{2}}{3} \left( \frac{R_{0}}{R} - 1 \right)} $$

The total collapse time can be found by intergating over the whole radius

$$t_{c}=\int dt=\int \frac{dt}{dr}\,dt = \int \frac{dr}{v}$$

$$t_{c}=\sqrt{\frac{3}{8 \pi G \rho R_{0}^2}} \;\int_{0}^{R_{0}} \frac{1}{\sqrt{\left( \frac{R_{0}}{R} - 1 \right)}}$$

The integral is a bit tricky, it ends up giving you $\frac{\pi R_{0}^{2}}{2}$, so we have

$$t_{c} = \sqrt{\frac{3}{8 \pi G \rho}} \frac{\pi}{2} = \sqrt{\frac{3 \pi}{32 G \rho}}$$

This is our timescale for gravitational collapse. To find the sound crossing time we first need to know the sound speed in the medium, which, for an ideal gas, is given by

$$c_{s}=\sqrt{\frac{\gamma k_{B} T}{m}}$$

where $k_{B}$ is the Boltzmann constant, $\gamma$ is the adiabatic index, $T$ is the temperature of the gas, and $m$ is the particle mass.

The sound crossing time is then given by

$$t_{s} = \frac{R}{c_{s}} = \sqrt{\frac{m}{\gamma k_{B} T}} \; R$$

For collapse to occur, $t_{s} > t_{c}$. At the turnover point, they are equal, so $t_{s}/t_{c} = 1$. The radius at this turnover point is the **Jean's Length**, $R_{J}$.

$$\frac{t_{s}}{t_{c}} = \left(\frac{m}{\gamma k_{B} T}\right)^{1/2} \; R \left(\frac{32 G \rho}{3 \pi}\right)^{1/2}$$

$$ R_{J} = \sqrt{\frac{3 \pi \gamma k T}{32 G \rho m}}  = c_{s} \sqrt{\frac{3 \pi}{32} \frac{1}{G \rho}}$$

The **Jean's Mass** is just the volume of the sphere with radius the Jean's legnth times the average density

$$M_{J} = \frac{4\,\pi}{3} R_{J}^{3} \rho_{0}$$


## Virial Theorem
We can derive this result using the *Virial Theorem*, which states that the total kinetic energy in a system is equal to half the potential energy,

$$\langle T \rangle = -\frac{1}{2} \langle{U}\rangle$$

The gravitational potential energy of a cloud of point masses is given by

$$U = -\frac{3}{5} \frac{GM^2}{R}$$

And the total kinetic energy of the particles is

$$T = \frac{3}{2} \, N \,k_{b}\, t$$

where $m$ is the average particle mass, and $N$ is the total number of particles, $N = M/m$.

For collapse to occur, the gravitational potential energy must be greater than the thermal kinetic energy of the cloud. So, substituting in to the Virial Theorem, the inequality becomes

$$3 \, N \,k_{b}\, t < \frac{3}{5} \frac{GM^2}{R}$$

$$\frac{k_{b}\, t}{m} < \frac{1}{5} \frac{GM}{R}$$

The Jean's Mass / Length is at the boundary of this inequality. First we'll find the Jean's Length by substituting for $M$, assuming a constant density cloud,

$$\frac{\,k_{b}\, t}{m} < \frac{1}{5} \frac{G}{R} \frac{4 \pi R^{3}}{3} \rho$$

$$R_{J}^{2} = \frac{15 \,k_{b}\, t}{G\,m}  \frac{1}{4 \pi \rho} $$

Substitute for the sound speed, $c_{s}$, we found in the previous derivation,

$$ R_{J} = c_{s} \sqrt{\frac{9}{4 \pi} \frac{1}{G \rho}}$$

Note that the constant in the front of this equation is slightly different than that derived above using the timescale method.

For the Jean's Mass, substitute for $R$ with the same constant density assumption,

$$R = \left( \frac{3M}{4 \pi \rho} \right)^{1/3}$$

$$3 \, \frac{M \,k_{b}\, t}{m}  < \frac{3}{5} GM^2 \left( \frac{4 \pi \rho}{3M} \right)^{1/3}$$

$$3 \, \frac{k_{b}\, t}{m}  < \frac{3G}{5} \left( \frac{4 \pi \rho}{3} \right)^{1/3} M^{2/3}$$

$$M^{2/3} > \left(\frac{k_{b}\, t}{m}\right) \left(\frac{5}{G}\right) \left( \frac{3}{4 \pi \rho} \right)^{1/3}$$

$$M > \left(\frac{5 \, k_{b}\, t}{G\,m}\right)^{3/2} \left( \frac{3}{4 \pi \rho} \right)^{1/2}$$

$$\boxed{M_{J} = \left(\frac{-5 \, k_{b}\, t}{G\,m}\right)^{3/2} \left( \frac{3}{4 \pi \rho} \right)^{1/2}}$$
