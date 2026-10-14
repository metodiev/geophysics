# Exercises — 14-02-02 EM and TDEM for Groundwater Exploration

Attempt these before reading the
[solutions](./02-em-for-hydrology-solutions.md). The lesson is
[02 EM and TDEM for Groundwater Exploration](../02-em-for-hydrology.md). All
targets are **SYNTHETIC**.

Use $\delta = \sqrt{2/(\omega\mu_0\sigma)} = 503/\sqrt{f\sigma}$ m,
$z = \sqrt{2\rho t/\mu_0}$, $t = \mu_0 z^{2}/(2\rho)$,
$\sigma_a = \pi t\,g^{2}/\mu_0$ and $\mu_0 = 4\pi \times 10^{-7}\ \mathrm{H\,m^{-1}}$.

## ★ Foundational

**★1.** Compute the skin depth in a ground of $\sigma = 0.05\
\mathrm{S\,m^{-1}}$ at $f = 50$ Hz, using both the exact expression and the
$503/\sqrt{f\sigma}$ approximation, and report the difference.

**★2.** Compute the diffusion depth at $t = 1$ ms in a $25\ \Omega$ m ground.

**★3.** Compute the time needed for the diffusion to reach 150 m in a
$20\ \Omega$ m ground, in ms.

## ★★ Applied

**★★4.** A receiver records a surface response $g = 0.012$ (normalised) at
$t = 0.3$ ms. Compute the apparent conductivity and the apparent resistivity. Then
compute the fractional error in $\sigma_a$ for a 4% error in $g$, and state the
rule you used.

**★★5.** A 10 m thick aquifer of $5\ \Omega$ m lies at 60 m depth beneath 50 m of
$50\ \Omega$ m cover. Compute the conductance of the aquifer and of the cover, and
the diffusion time to reach the top of the aquifer in the cover's resistivity. State
whether the aquifer's conductance is large enough to be a distinctive anomaly.

**★★6.** For a coal-seam-like target with a fixed conductance of $0.25$ S, list
three $(b, \rho)$ pairs that are indistinguishable to a TDEM sounding, and compute
the layer thickness at which the equivalence should begin to fail if the diffusion
depth at the latest usable time is 150 m.

## ★★★ Research-oriented

**★★★7.** Design a TDEM survey to (i) detect and (ii) resolve a $20\ \Omega$ m
saturated aquifer 15 m thick at 60 m depth beneath $150\ \Omega$ m of dry cover.
Specify the time window, an approximate transmitter moment scaling argument, and the
noise requirement implied by the factor-of-two amplification between amplitude and
apparent conductivity. Then design the inversion-side deliverable: what will you
report about thickness and resistivity, given the conductance equivalence of the
lesson? Support every number with arithmetic.

**★★★8.** Specify a verification *and* validation plan for a 1-D TDEM modelling
code. Include: one analytic check (state the solution and the boundary conditions),
one independent-limit check, one conservation or reciprocity check, one
grid/time-step convergence measurement with the order you expect, and one
**validation** step (against field data) that is genuinely different from
verification. Then explain which failure in the code each test would catch that the
others would not, and identify the one thing none of them can establish.
