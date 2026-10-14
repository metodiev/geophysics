# Exercises — 16-05-02 GCMs, Resolution and Parameterisation

Attempt these before reading the [solutions](./02-gcms-and-parameterisation-solutions.md).
Lesson: [02 GCMs, Resolution and Parameterisation](../02-gcms-and-parameterisation.md).
All models are **SYNTHETIC**. Standard constants: $g = 9.81\ \mathrm{m\,s^{-2}}$,
$c_p = 1004\ \mathrm{J\,kg^{-1}\,K^{-1}}$.

## ★ Foundational

**★1.** Compute the numerical diffusion coefficient
$K_{\text{num}} = \tfrac12u\,\Delta x(1-C)$ for $u = 10\
\mathrm{m\,s^{-1}}$, $\Delta x = 25\ \mathrm{km}$ and $C = 0.5$. State the unit
of the answer and check it dimensionally.

**★2.** Compute the dry adiabatic lapse rate from $g$ and $c_p$, in
$\mathrm{K\,km^{-1}}$. A model column has $300\ \mathrm{K}$ at the surface and
$250\ \mathrm{K}$ at $5\ \mathrm{km}$. Compute its lapse rate and state whether
it is statically stable.

**★3.** A model has $\Delta x = 12\ \mathrm{km}$. Using the four-grid-spacing
rule, state its effective resolution, and name one process that is still
sub-grid at that scale.

## ★★ Applied

**★★4.** The demonstration measures a tracer variance of $6391.55\
\mathrm{km^{2}}$ at $t=0$ and $8077.64\ \mathrm{km^{2}}$ after 24 h, at
$N = 256$ ($\Delta x = 3.906\ \mathrm{km}$, $K_{\text{analytic}} = 9765.6\
\mathrm{m^{2}\,s^{-1}}$). Verify the variance growth against the analytic
diffusivity and state the agreement as a percentage.

**★★5.** The demonstration's unadjusted column has 21 levels from 0 to 5 km with
$T(z) = 300 - 10.5z$ ($z$ in km). Compute the dry static energy
$s_i = c_pT_i + gz_i$ on each level, its mean, and hence the final surface
temperature after a full convective adjustment in which $s$ becomes uniform.
Compare your answer with the demonstration's $298.20\ \mathrm{K}$.

**★★6.** Two energy-conserving convective closures give surface temperatures
$298.20\ \mathrm{K}$ (full adjustment) and $298.54\ \mathrm{K}$ (half
adjustment). Explain in two or three sentences why both conserve dry static
energy, why they differ, and what kind of uncertainty the difference represents.

## ★★★ Research-oriented

**★★★7.** Design a convergence test for the upwind scheme. State the error
metric, the refinement sequence, the expected slope of the error against
$\Delta x$ on log-log axes, and what a measured slope of 2 would indicate.

**★★★8.** A model is described as "parameterisation-free" because its horizontal
grid spacing is $1\ \mathrm{km}$. Write a short critique using the concept of
effective resolution and the physical scale of convection, clouds,
boundary-layer turbulence and gravity waves.
