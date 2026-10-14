# Exercises — 14-01-06 The Unsaturated Zone, Infiltration and Soil Moisture

Attempt these before reading the
[solutions](./06-unsaturated-zone-solutions.md). The lesson is
[06 The Unsaturated Zone, Infiltration and Soil Moisture](../06-unsaturated-zone.md).
All soils are **SYNTHETIC**.

Useful relations:
$$\theta(h) = \theta_r + \frac{\theta_s-\theta_r}{[1+(\alpha\lvert h\rvert)^n]^m},
\ m = 1-\tfrac{1}{n};\qquad
K = K_s S_e^{1/2}\left[1-(1-S_e^{1/m})^m\right]^{2};$$
$$f = K_s\left(1+\frac{\psi_f\Delta\theta}{F}\right);\qquad
t_p = \frac{K_s\psi_f\Delta\theta}{r(r-K_s)};$$
$$\sqrt{\varepsilon_{\text{eff}}} = (1-\phi)\sqrt{4.5} + \theta\sqrt{81}
+ (\phi-\theta),\qquad v = c/\sqrt{\varepsilon_{\text{eff}}},$$
with $c = 0.299792458\ \mathrm{m\,ns^{-1}}$.

## ★ Foundational

**★1.** A synthetic soil has $\theta_s = 0.40$, $\theta_r = 0.05$,
$\alpha = 2.0\ \mathrm{m^{-1}}$, $n = 2.0$. Compute $\theta$ at $h = -0.2$ m and
$h = -2.0$ m, and report the effective saturation $S_e$ at each.

**★2.** For the same soil, invert the retention curve: what suction holds a water
content of $\theta = 0.30$?

**★3.** Compute $\theta_{fc}$ at $h = -3.3$ m, $\theta_{wp}$ at $h = -150$ m and
the available water capacity in mm per metre for the soil of ★1.

## ★★ Applied

**★★4.** A synthetic soil has $K_s = 5.0 \times 10^{-7}\ \mathrm{m\,s^{-1}}$,
$\psi_f = 0.15$ m and $\Delta\theta = 0.30$. Compute the cumulative infiltration
$F$, the infiltration rate $f$ in mm h$^{-1}$ and the front depth at $t = 1$ h of
ponded infiltration. Then compute the ponding time for a rainfall rate of
$5\ \mathrm{mm\,h^{-1}}$ and state whether the soil ponds at all at that rate.

**★★5.** Using Mualem–van Genuchten with $K_s = 2.0 \times 10^{-6}$,
$\theta_s = 0.42$, $\theta_r = 0.06$, $n = 1.6$, compute $K$ at $\theta = 0.35$ and
at $\theta = 0.15$, and report the ratio. State in one sentence why a ratio of this
size matters for recharge.

**★★6.** A GPR measurement gives $\varepsilon_{\text{eff}} = 16.0$ for a soil with
assumed $\phi = 0.35$. Invert CRIM for $\theta$, compute the radar velocity, and
the two-way travel time through a 0.4 m layer. Repeat the inversion for an assumed
$\phi = 0.45$ and report the change in $\theta$.

## ★★★ Research-oriented

**★★★7.** Design a soil-moisture monitoring programme that combines GPR velocity
analysis, a point sensor (capacitance or TDR) and a neutron or gravimetric
calibration, to deliver water content to $\pm 0.02$. State the calibration
arithmetic (how many gravimetric samples, over what water-content range), the
error budget in $\varepsilon$ and in $\theta$, the effect of a clay-rich horizon,
and one systematic error that a precision argument alone would miss.

**★★★8.** The lesson's $\mathrm{erfc}$ test verifies the time-stepper against the
solution of a *linear* diffusion equation. State precisely what it verifies and
what it does not. Then design a complete code-verification suite for a Richards
solver: propose (i) a manufactured solution for the linearised equation with the
arithmetic that makes it exact, (ii) a grid-convergence test with the observed order
of accuracy you expect, (iii) two physical limits whose exact values are known, and
(iv) the mass-balance check. Explain what each test would catch that the others
would not.
