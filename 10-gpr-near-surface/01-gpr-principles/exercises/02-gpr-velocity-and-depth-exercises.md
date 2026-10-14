# Exercises — 10-01-02 Velocity Estimation and Depth Conversion in GPR

Attempt before the [solutions](./02-gpr-velocity-and-depth-solutions.md). Lesson:
[02 Velocity Estimation and Depth Conversion](../02-gpr-velocity-and-depth.md).
All models **SYNTHETIC**.

## ★ Foundational

**★1.** A hyperbola has apex time $t_0 = 40.000\ \mathrm{ns}$ and a fitted slope
of $278.0\ \mathrm{ns^{2}\,m^{-2}}$ in a plot of $t^{2}$ against $x^{2}$.
Compute $v$ and the depth.

**★2.** With antennas $0.25\ \mathrm{m}$ apart, compute the air-wave and
ground-wave arrival times for $v_1 = 0.075\ \mathrm{m\,ns^{-1}}$, and the implied
$\varepsilon_r$.

**★3.** State the depth bias from a $+1\ \mathrm{ns}$ time-zero error at
$v = 0.075\ \mathrm{m\,ns^{-1}}$.

## ★★ Applied

**★★4.** Derive $d = v t/2$'s error propagation
$\delta d/d = \delta v/v$ and confirm it with $v = 0.09 \pm 0.005\
\mathrm{m\,ns^{-1}}$ and $t = 60\ \mathrm{ns}$.

**★★5.** Two picks give $(t_{0,1}, v_{\mathrm{nmo},1}) = (40.0\ \mathrm{ns},
0.0600\ \mathrm{m\,ns^{-1}})$ and $(t_{0,2}, v_{\mathrm{nmo},2}) = (66.7\
\mathrm{ns}, 0.0740\ \mathrm{m\,ns^{-1}})$. Compute the interval velocity and
state which pick dominates the result.

**★★6.** Using the exact two-layer ray time, compute $t$ at $x = 0$ and
$x = 3.0\ \mathrm{m}$ for $v_1 = 0.060$, $h_1 = 1.2\ \mathrm{m}$, $v_2 = 0.090\
\mathrm{m\,ns^{-1}}$, $d = 2.4\ \mathrm{m}$, and state the sign of the
refraction offset $a$ at the minimum.

## ★★★ Research-oriented

**★★★7.** A diffraction hyperbola is fitted over a $1.0\ \mathrm{m}$ aperture
with $0.2\ \mathrm{ns}$ picking noise. Estimate how much worse the velocity
determination is than for a $4.0\ \mathrm{m}$ aperture, using the fact that the
curvature signal scales as $x^{2}$ while the noise does not.

**★★★8.** Design a two-reflector CMP acquisition for a $2.5\ \mathrm{m}$ deep
target in a medium with $v = 0.08\ \mathrm{m\,ns^{-1}}$ so that the interval
velocity is determined to better than $2\%$. Give the required maximum offset and
justify it with the analytic error propagation.
