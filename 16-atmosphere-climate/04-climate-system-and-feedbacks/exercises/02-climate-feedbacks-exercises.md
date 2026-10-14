# Exercises — 16-04-02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon

Attempt these before reading the
[solutions](./02-climate-feedbacks-solutions.md). The lesson is
[02 Feedbacks](../02-climate-feedbacks.md). All models are **SYNTHETIC**
teaching values. Use $\sigma = 5.670374419\times10^{-8}\
\mathrm{W\,m^{-2}K^{-4}}$, $L = 2.5\times10^6\ \mathrm{J\,kg^{-1}}$,
$R_v = 461.5\ \mathrm{J\,kg^{-1}K^{-1}}$, $|\lambda_0| = 5.418\
\mathrm{W\,m^{-2}K^{-1}}$ at 288 K, and $F_{2\times} = 3.7\
\mathrm{W\,m^{-2}}$.

## ★ Foundational

**★1.** Compute the Planck feedback parameter $-4\sigma T^3$ at $T = 270$ K and
the Planck-only temperature response to a forcing of $2.0\ \mathrm{W\,m^{-2}}$.

**★2.** Compute $\mathrm{d}\ln e_s/\mathrm{d}T = L/(R_vT^2)$ at 265 K and at
305 K, give both as per cent per kelvin, and state the direction of the change
with temperature.

**★3.** With $\lambda_0 = -5.418$ and feedbacks water vapour $+1.2$, albedo
$+0.35$, cloud $+0.5$ and carbon $+0.2$ (all W m⁻² K⁻¹), compute the total
$\lambda$ and the equilibrium temperature change for $F = 3.7\
\mathrm{W\,m^{-2}}$.

## ★★ Applied

**★★4.** Using the assumed ranges water vapour $[0.9, 1.5]$, cloud
$[-0.3, 1.0]$, albedo $[0.1, 0.4]$, carbon $[0.0, 0.2]$
(W m⁻² K⁻¹), compute the total $\lambda$ and the equilibrium response at the
**midpoints**, then state which range you would narrow first and justify the
choice with a number.

**★★5.** Derive $\lambda_\text{ice} = -(S/4)\,\mathrm{d}\alpha/\mathrm{d}T$ for
a temperature-dependent albedo, and compute the ramp slope
$\mathrm{d}\alpha/\mathrm{d}T$ at which $\lambda_0 + \lambda_\text{ice} = 0$
with $S = 1361\ \mathrm{W\,m^{-2}}$. State what a zero total $\lambda$ implies
for the equilibrium.

**★★6.** The hysteresis loop edges of the zero-dimensional ice-albedo model are

$$S_\text{low} = \frac{4(T_\text{hi}B + A)}{1-\alpha_\text{free}},
\qquad
S_\text{high} = \frac{4(T_\text{lo}B + A)}{1-\alpha_\text{ice}} .$$

**(a)** Verify both for the lesson's parameters ($A = 203.3$, $B = 2.09$,
$T_\text{lo} = -10$, $T_\text{hi} = +10\ ^\circ$C,
$\alpha_\text{ice} = 0.62$, $\alpha_\text{free} = 0.30$).
**(b)** Show how the loop width depends on the ramp half-width $w$ when
$T_\text{lo} = -w$, $T_\text{hi} = +w$, and verify the coefficient against the
lesson's table.

## ★★★ Research-oriented

**★★★7.** Section 5 of the lesson shows a state-dependent feedback making the
linear response wrong by 2.75% at $F = 3.7$ W m⁻². State the maximum value of
the feedback's drift slope you would accept if you required the linear estimate
to be within 5% at $F = 6$ W m⁻², and show the calculation. Then state one
observational constraint that could bound that slope.

**★★★8.** Design a study to bound the cloud feedback parameter from
observations, using only quantities the lesson defines. Specify the diagnostic,
the regression you would run, the confounders you must control, and the reason
the result would be a *bound* rather than a value.
