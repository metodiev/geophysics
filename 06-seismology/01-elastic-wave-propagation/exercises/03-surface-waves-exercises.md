# Exercises — 06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity

Attempt these before reading the
[solutions](./03-surface-waves-solutions.md). The lesson is
[03 Surface Waves](../03-surface-waves.md); every number needed is printed by
[`../code/surface_waves_demo.py`](../code/surface_waves_demo.py). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For the demonstration's Love-wave model ($\beta_1 = 3.500$,
$\rho_1 = 2700\ \mathrm{kg\,m^{-3}}$, $H = 30\ \mathrm{km}$,
$\beta_2 = 4.500\ \mathrm{km\,s^{-1}}$, $\rho_2 = 3300\ \mathrm{kg\,m^{-3}}$),
state the interval of phase velocities that can be trapped, and compute
$q = \sqrt{\beta_1^{-2} - \beta_2^{-2}}$ with its unit.

**★2.** Using the mode-count formula $1 + \lfloor\omega H q/\pi\rfloor$, compute
the number of Love modes at $T = 10\ \mathrm{s}$ and $T = 5\ \mathrm{s}$ and
check against the demonstration's table (2 and 3 modes).

**★3.** State, with the reason, whether $c(T)$ for the fundamental Love mode
increases or decreases as the period shortens, and verify your answer using the
demonstration's values at $T = 200\ \mathrm{s}$ and $T = 2\ \mathrm{s}$.

## ★★ Applied

**★★4.** The demonstration gives $c(40\ \mathrm{s}) = 4.2519$ and
$c(30\ \mathrm{s})$ can be interpolated between its printed rows $40$ and $20$ s
($c(20\ \mathrm{s}) = 3.8666$). Estimate $U$ at $T = 40\ \mathrm{s}$ with a
one-sided finite difference and compare with the demonstration's value
$U = 3.8496\ \mathrm{km\,s^{-1}}$ at that period. State the sign of $c - U$ and
what it says about the medium.

**★★5.** The demonstration reports the largest $|c - U| = 0.4023\
\mathrm{km\,s^{-1}}$ at $T = 40\ \mathrm{s}$. Express that as a percentage of
$c$ and explain, in terms of where the energy samples the medium, why the
difference is largest at intermediate periods rather than at the extremes.

**★★6.** For a Poisson solid ($\lambda = \mu$, $v_p/v_s = \sqrt{3}$) the
demonstration obtains $\zeta = 0.84529946$ and
$c_R = 0.91940169\,\beta$. Compute the Rayleigh speed for $\beta = 3.5\
\mathrm{km\,s^{-1}}$ and state how it compares with the Love fundamental at
$T = 5\ \mathrm{s}$ ($3.5327\ \mathrm{km\,s^{-1}}$). What does the comparison
require you to hold fixed?

## ★★★ Research-oriented

**★★★7.** The demonstration tests waveguide existence by counting how many of
200 trial velocities fall inside the trapping interval, obtaining 10 when the
layer is slower and 0 when it is faster. Design a test that finds the *minimum*
velocity contrast at which a fundamental Love mode is still trapped for
$H = 30\ \mathrm{km}$ at $T = 20\ \mathrm{s}$, state the numerical tolerance you
would accept, and predict whether the threshold is sharp or smooth in the
contrast.

**★★★8.** Derive the two group-velocity expressions
$U = c + k\,\mathrm{d}c/\mathrm{d}k$ and
$U = c\left[1 - (\omega/c)\mathrm{d}c/\mathrm{d}\omega\right]^{-1}$ from
$U = \mathrm{d}\omega/\mathrm{d}k$ and show that they are the same statement.
Then explain why their agreement to $1.52\times10^{-9}$ in the demonstration is a
check on the arithmetic and not on the physics.

**★★★9.** A thin low-velocity layer is invisible to long-period surface waves
because the mode samples mostly the half space. Using the demonstration's mode
count and the fundamental's limits $c(T\to0) = \beta_1$ and
$c(T\to\infty) = \beta_2$, state at what period the fundamental first carries
more than half of its displacement energy inside the layer, and say what
additional measurement would make the answer quantitative rather than
qualitative.
