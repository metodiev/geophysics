# Exercises — 06-01-01 From Hooke's Law and Newton to the Elastodynamic Equation

Attempt these before reading the
[solutions](./01-wave-equation-elastic-solutions.md). The lesson is
[01 From Hooke's Law and Newton to the Elastodynamic Equation](../01-wave-equation-elastic.md),
and the numbers you need are printed by
[`../code/wave_equation_demo.py`](../code/wave_equation_demo.py). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A SYNTHETIC rock has $\lambda = 25\ \mathrm{GPa}$,
$\mu = 30\ \mathrm{GPa}$, $\rho = 2700\ \mathrm{kg\,m^{-3}}$. Compute $v_p$ and
$v_s$ and state the unit of each. Then show by dimensional analysis that
$\rho\,\partial^2u/\partial t^2$ and $\mu\nabla^2 u$ have the same dimensions.

**★2.** For the same rock, write the Navier–Cauchy equation in the form
$\rho\ddot{\mathbf u} = (\lambda+\mu)\nabla(\nabla\cdot\mathbf u) +
\mu\nabla^2\mathbf u$ and identify which term vanishes for a P wave and which for
an S wave when the field is built from a scalar potential or a vector potential
respectively.

**★3.** A Poisson solid has $\lambda = \mu$. Show that $v_p/v_s = \sqrt{3}$ and
check this against the demonstration's Poisson-solid row
($v_p = 5883.48$, $v_s = 3396.83\ \mathrm{m\,s^{-1}}$).

## ★★ Applied

**★★4.** The demonstration measures the relative residual of the Navier–Cauchy
equation for a P wave as $2.834\times10^{-2}$ at $n = 48$ and
$6.866\times10^{-3}$ at $n = 96$ grid points. Predict the residual at $n = 192$,
$n = 384$ and $n = 768$, state the convergence order you are assuming, and say
what a measured order of 1 instead of 2 would tell you about the derivative
stencil.

**★★5.** In the finite-difference speed measurement the demonstration reports
measured speed $5402.1965\ \mathrm{m\,s^{-1}}$ at $k_0\Delta x = 0.6280$ and
$5608.5971\ \mathrm{m\,s^{-1}}$ at $k_0\Delta x = 0.0785$, against a derived speed
of $5610.8361\ \mathrm{m\,s^{-1}}$. Compute the percentage error in each case and
verify that the ratio of the two errors is consistent with the fitted exponent
$2.172$ over a factor of 8 in $k_0\Delta x$.

**★★6.** Using the CFL condition $r = c\Delta t/\Delta x = 0.5$ and
$\Delta x = 1000\ \mathrm{m}$ with $c = 5610.8361\ \mathrm{m\,s^{-1}}$, compute
$\Delta t$. Then find the largest $\Delta x$ that keeps at least 10 grid points
per wavelength at $20\ \mathrm{Hz}$ for that speed.

## ★★★ Research-oriented

**★★★7.** Derive the exact discrete dispersion relation for the second-order
scheme, $\omega = (2/\Delta t)\arcsin\!\big(r\sin(k\Delta x/2)\big)$, and from it
the discrete group velocity
$c_g = c\cos(k\Delta x/2)/\sqrt{1 - r^2\sin^2(k\Delta x/2)}$. Then explain why
the measured group velocity is *below* the medium speed rather than above it.

**★★★8.** A medium has depth-dependent $\lambda(z)$ and $\mu(z)$. Carry the
derivatives through the derivation in the lesson without assuming homogeneity and
show that two extra terms appear: $\partial_i\lambda\,\nabla\cdot\mathbf u$ and
$2(\partial_j\mu)\,\varepsilon_{ij}$. Identify the physical process each
describes, and state which one is responsible for P-to-S conversion at a gradient
rather than at a discontinuity.

**★★★9.** The demonstration validates the finite-difference solver against the
analytic speed with no randomness involved, so the fixed seed plays no role in
its result. Design an experiment that *does* need a seed: estimate the
error distribution of the measured speed when the initial packet is a random
superposition of modes, and state how many realisations you need to resolve the
grid-dispersion bias from realisation noise.
