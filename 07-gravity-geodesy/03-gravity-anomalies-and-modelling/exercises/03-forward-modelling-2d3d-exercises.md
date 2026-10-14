# Exercises — 07-03-03 Forward Modelling in 2-D and 3-D

Attempt these before reading the
[solutions](./03-forward-modelling-2d3d-solutions.md). The lesson is
[03 Forward Modelling](../03-forward-modelling-2d3d.md). Use
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$.

## ★ Foundational

**★1.** State how many terms the rectangular-prism closed form contains per
station, and explain the origin of the alternating sign.

**★2.** Verify by dimensional analysis that each bracket in the prism formula has
dimensions of length, and hence that $G\Delta\rho\times$ (length) is an
acceleration.

**★3.** State the linearity property that makes superposition exact, and give one
example of a model that needs a **negative** density contrast.

## ★★ Applied

**★★4.** A prism occupies $x\in[-500,500]\ \mathrm{m}$, $y\in[-1000,1000]\
\mathrm{m}$, $z\in[200,1500]\ \mathrm{m}$ with
$\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$. Explain why a forward calculation at the
origin is well conditioned, and compute the infinite-slab value for the same
thickness so you can compare.

**★★5.** For the same prism, estimate the error introduced by a 2-D
interpretation using the demonstration's strike-length table, and state the strike
length at which the error would fall below $0.1\%$.

**★★6.** You voxelise a sphere of radius $500\ \mathrm{m}$ at $1200\ \mathrm{m}$
depth with $150\ \mathrm{m}$ cubes and find a $10.22\%$ volume excess. Explain why
the resulting anomaly error is roughly proportional to the volume error, and
compute the density correction that removes it.

## ★★★ Research-oriented

**★★★7.** Design a voxelisation of the same sphere that conserves volume exactly
at $150\ \mathrm{m}$ resolution, and predict the residual rms error as a fraction
of the peak. State how you would verify your prediction.

**★★★8.** A dipping slab is to be modelled with prisms. Propose a discretisation
whose top surface follows a plane dipping $20^{\circ}$, explain how the mass is
conserved, and state the parameter that controls the discretisation error.
