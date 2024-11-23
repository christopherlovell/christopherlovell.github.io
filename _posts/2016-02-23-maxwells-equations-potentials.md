---
layout: post
title: "Maxwell's equations in terms of potentials"
comments: true
date: "Tuesday, February 23, 2016"
tags:
- Physics
excerpt: Converting Maxwell's 4 equations of electromagnetism in terms of the vector and scalar potential
---

Maxwell's equations are most commonly given in terms of the electric and magnetic fields $\mathbf{E}$ & $\mathbf{B}$. They can also be expressed in terms of the electric potential, $\varphi$, and the magnetic potential, $\mathbf{A}$, which can be physically interpreted as the **potential energy per unit charge**, and the **potential energy per unit of current**, respectively. To convert between the two requires a few identities and a little vector algebra. We start with Maxwell's equations for the electric and magnetic fields,

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_{0}} \tag{1}\label{1}$$

$$\nabla \cdot \mathbf{B} = 0 \tag{2}\label{2}$$

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \tag{3}\label{3}$$

$$\nabla \times \mathbf{B} = \mu_{0} \mathbf{J} + \mu_{0} \epsilon_{0} \frac{\partial \mathbf{E}}{\partial t} \tag{4}\label{4}$$

Since $\nabla \cdot \mathbf{B} = 0$, we can write $\mathbf{B}$ as the curl of a vector field, $\mathbf{A}$,

$$\mathbf{B} = \nabla \times \mathbf{A} = 0  \tag{5}\label{5}$$

This is a result of the identity $\nabla \cdot (\nabla \times \mathbf{A}) = 0$. Here, $\mathbf{A}$ is the *vector potential* of the magnetic field.

Can substitute this into $\eqref{3}$,

$$\nabla \times \mathbf{E} = -\frac{\partial (\nabla \times \mathbf{A})}{\partial t}$$

$$\nabla \times \left( \mathbf{E} + \frac{\partial \mathbf{A}}{\partial t} \right)$$

The left hand side of this equation gives the curl of a vector field that combines the electric field and the time derivative of the magnetic vector potential. Can write this in terms of a scalar field, $\varphi$,

$$\mathbf{E} + \frac{\partial \mathbf{A}}{\partial t} = - \nabla \varphi$$

$$\mathbf{E} = - \nabla \varphi - \frac{\partial \mathbf{A}}{\partial t} \tag{6}\label{6}$$

Can use equations $\eqref{5}$ and $\eqref{6}$ to eliminate $\mathbf{B}$ from $\eqref{4}$.

$$\nabla \times \mathbf{B} = \nabla \times (\nabla \times \mathbf{A}) = \nabla (\nabla \cdot \mathbf{A}) - \nabla^{2} \mathbf{A}$$

$$\begin{align}\nabla (\nabla \cdot \mathbf{A}) - \nabla^{2} \mathbf{A} & = \mu_{0} \mathbf{J} + \mu_{0} \epsilon_{0} \frac{\partial \mathbf{E}}{\partial t} \\
& = \mu_{0} \mathbf{J} + \mu_{0} \epsilon_{0} \nabla \frac{\partial \varphi}{\partial t} - \mu_{0} \epsilon_{0} \frac{\partial^{2} \mathbf{A}}{\partial t^{2}}\end{align}$$

$$\nabla^{2} \mathbf{A} - \mu_{0} \epsilon_{0} \frac{\partial^{2} \mathbf{A}}{\partial t^{2}} = - \mu_{0} \mathbf{J} + \nabla \left( \nabla \cdot \mathbf{A} + \mu_{0} \epsilon_{0} \frac{\partial \varphi}{\partial t} \right) \tag{8}\label{8}$$

and equation $\eqref{6}$ to eliminate $\mathbf{E}$ from $\eqref{1}$,

$$\nabla \cdot \mathbf{E} = - \nabla^{2} \varphi - \frac{\partial}{\partial t} (\nabla \cdot \mathbf{A})$$

$$\nabla^{2} \cdot \varphi + \frac{\partial}{\partial t} (\nabla \cdot \mathbf{A}) = - \frac{\rho}{\epsilon_{0}} \tag{7}\label{7}$$

$\varphi$ and $\mathbf{A}$ make up four functions in total (one for the scalar function, one for each component of $\mathbf{A}$), which can all be solved using equations $\eqref{7}$ and $\eqref{8}$. Their solutions can be used to find $\mathbf{E}$ and $\mathbf{B}$ using $\eqref{5}$ and $\eqref{6}$. This is a simplification over the original equations, which make up 6 functions (3 for each component of $\mathbf{E}$ and $\mathbf{B}$).

We can simplify this further by applying the Lorenz gauge, which is a partial fixing of the gauge. The Lorenz gauge was first introduced by the Irishman George F. FitzGerald, but explicitly published by Ludvig Lorenz, after which it is named. Lorenz is not to be mistaken for Hendrik Lorentz, who discovered the Lorentz invariance condition which the Lorenz gauge satisfies.

The Lorenz gauge is given by,

$$\nabla \cdot \mathbf{A} + \mu_{0} \epsilon_{0} \frac{\partial \varphi}{\partial t} = 0$$

Which we can see easily substitutes in to $\eqref{8}$.
