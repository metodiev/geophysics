# Exercises — 05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off

Difficulty: ★ · ★★ · ★★★. Use $G = 6.67430\times10^{-11}$ SI,
$\mu_0 = 1.25663706212\times10^{-6}$ H/m.

---

## ★ Foundational

**★1.** State the half-width law for a compact gravity source and give the
closed-form constant to six figures.

**★2.** A point mass is at 250 m depth. Predict its anomaly half-width using
the closed form, and state the ratio to depth.

**★3.** Derive $\delta = \sqrt{2/\mu\sigma\omega}$ from the diffusion equation
and check the dimensions of every symbol.

**★4.** A source has usable bandwidth 10–60 Hz; the velocity is 2400 m/s.
Compute $\Delta z_\text{res}$.

---

## ★★ Applied

**★★5.** The half-width law is exact for a point mass. For a horizontal
cylinder (infinite line mass) the kernel is $d/(x^2+d^2)$. Derive its
half-width ratio and compare with 1.532842. Explain the difference.

**★★6.** For a half-space of 0.05 S/m, compute the skin depth at periods of
1 s, 10 s and 100 s. State which period is needed to sense a target at 800 m.

**★★7.** Two equal point masses lie at depth $d$, separated by $s$. Using the
criterion "resolvable if the midline value is more than 1% below the peak",
explain why $s_\text{min}/d$ is independent of $d$ — without computing it.

**★★8.** A survey detects an anomaly of 0.5 mGal at 300 m depth. Estimate,
using the information-content scaling, the anomaly at 1200 m and the relative
information content. State which exponent you used and why.

---

## ★★★ Research-oriented

**★★★9.** Reproduce the width law numerically. Sample a point-mass anomaly on
a grid, measure $w_{1/2}/d$ for at least four depths, fit the log–log slope,
and compare with the closed form. Report the grid size, the fitted slope, and
the measured deviation from 1.532842. Then repeat for a horizontal cylinder and
report whether the slope stays 1. Finally, explain why the *slope* is more
robust than the *constant*.

**★★★10.** Skin-depth measurement. Solve $\partial B/\partial t =
D\,\partial^2B/\partial z^2$ numerically with $B(0,t) = B_0\cos\omega t$ for two
stated conductivities. Fit the amplitude decay length and the phase lag, refine
the grid, and report the measured convergence of the error. State whether the
residual is discretisation or modelling error, and how you know.
