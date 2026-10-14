# Exercises — 19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy

Attempt these before reading the
[solutions](./04-numerical-dispersion-diffusion-solutions.md). The lesson is
[04 Numerical Dispersion and Dissipation](../04-numerical-dispersion-diffusion.md).
All models are **SYNTHETIC**. Numbers printed by
`../code/numerical_dispersion_diffusion_demo.py` may be quoted directly.

## ★ Foundational

**★1.** Write the discrete dispersion relation of the CTCS scheme and evaluate
$v_{\text{num}}/v$ at $C = 0.5$ for $\mathrm{PPW} = 4$ and $10$.

**★2.** For $u_t + au_x = 0$ discretised with upwind differencing, write
$|G|^{2}$ and state the equivalent diffusivity $D_{\text{num}}$.

**★3.** State what "no numerical dissipation" means for a scheme, in terms of
$|G|$, and name one scheme that has this property.

## ★★ Applied

**★★4.** A pulse travels 5000 m at $C = 0.5$ in a medium with
$a = 2000\ \mathrm{m\,s^{-1}}$ and a carrier wavelength of eight cells. Predict
its arrival lag in seconds and in per cent.

**★★5.** A monochromatic wave at $\mathrm{PPW} = 12$, $C = 0.75$ propagates
for 20 wavelengths in an upwind scheme with $h = 10$ m, $a = 1500\
\mathrm{m\,s^{-1}}$. Compute the amplitude remaining and the equivalent
diffusivity, then state which of the two numbers describes the physics and which
is purely numerical.

**★★6.** Using the anisotropy table for the five-point and nine-point
Laplacians, state the reduction in angular error achieved by the nine-point
operator at PPW $= 8$ and $16$, and the cost in matrix non-zeros per row.

## ★★★ Research-oriented

**★★★7.** A policy is proposed: "use $\mathrm{PPW} = 6$ and accept the
dispersion error, because the error is second order and will fall quickly when
the grid is refined." Evaluate the policy numerically for a target phase error of
$0.5\,\%$ at $C = 0.5$, state the PPW actually required, and identify the
assumption in the policy that is wrong.

**★★★8.** Design an experiment that separates numerical dissipation from
physical attenuation in a run whose medium has a known $Q$. State the observable,
the prediction for each effect, the resolution at which they can be
distinguished, and the control that rules out the alternative explanation.
