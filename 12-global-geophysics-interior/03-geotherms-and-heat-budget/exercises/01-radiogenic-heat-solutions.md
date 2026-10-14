# Solutions — 12-03-01 Radiogenic Heat Production and Mantle Geotherms

> Read after attempting the [exercises](./01-radiogenic-heat-exercises.md).
> Lesson: [01 Radiogenic Heat Production and Mantle Geotherms](../01-radiogenic-heat.md).
> Numbers were computed, not estimated by hand. All models are **SYNTHETIC**.

---

## ★1 — Specific heat production

$$H = \frac{\ln 2}{T_{1/2}}\,\frac{N_A}{M}\,Q_{\text{tot}}(1-f_\nu).$$

$\lambda = \ln 2/(10.0\times3.1557\times10^{16}\ \mathrm{s})
= 2.197\times10^{-18}\ \mathrm{s^{-1}}$.

$N_A/M = 6.02214076\times10^{23}/0.200\ \mathrm{kg\,mol^{-1}}
= 3.011\times10^{24}\ \mathrm{atoms\,kg^{-1}}$.

$Q_{\text{dep}} = 40\times0.95 = 38.0\ \mathrm{MeV}
= 38.0\times1.602\times10^{-13} = 6.088\times10^{-12}\ \mathrm{J}$.

$$H = 2.197\times10^{-18}\times3.011\times10^{24}\times6.088\times10^{-12}
= 4.03\times10^{-5}\ \mathrm{W\,kg^{-1}} = 40.3\ \mathrm{\mu W\,kg^{-1}}.$$

Units at each step: $\mathrm{s^{-1}}\times\mathrm{kg^{-1}}\times\mathrm{J}
= \mathrm{W\,kg^{-1}}$ ✔.

---

## ★2 — Volumetric production

Per isotope, contribution $= \rho C_{\text{elem}} f_i H_i$
($\mathrm{kg\,m^{-3}}\times\text{dimensionless}\times\mathrm{\mu W\,kg^{-1}}
= \mathrm{\mu W\,m^{-3}}$):

- ²³⁸U: $2800\times1.5\times10^{-6}\times0.9927\times97.56 = 0.4068$
- ²³⁵U: $2800\times1.5\times10^{-6}\times0.0072\times570.07 = 0.0172$
- ²³²Th: $2800\times6.0\times10^{-6}\times1.0\times25.89 = 0.4350$
- ⁴⁰K: $2800\times1.5\times10^{-2}\times1.17\times10^{-4}\times38.97 = 0.1915$

$$A = 1.051\ \mathrm{\mu W\,m^{-3}}.$$

Thorium is again the largest single term, and potassium is not negligible despite
the isotopic abundance of $1.17\times10^{-4}$: the element concentration is
$1.5\ \mathrm{wt\%}$, five orders of magnitude larger than the isotope fraction.

---

## ★3 — The mantle flux and its dominant uncertainty

$q_{\text{mantle}} = q_0 - A_0h = 70 - 12 = 58\ \mathrm{mW\,m^{-2}}$.

For independent errors,
$\delta q_{\text{mantle}} = \sqrt{7^2 + 4^2} = \sqrt{65} = 8.06\
\mathrm{mW\,m^{-2}}$.

$$q_{\text{mantle}} = 58 \pm 8\ \mathrm{mW\,m^{-2}}.$$

Which input dominates? In relative terms the production term is
$4/12 = 33\%$ and the flux is $7/70 = 10\%$, so $A_0h$ dominates; but in
*absolute* terms the flux term contributes 7 of the 8.06. The distinction matters
when quoting the result: the reported uncertainty is set by the flux, while the
*relative* uncertainty is set by the production.

---

## ★★4 — Monotonicity of the radiogenic fraction

With $A_0h = 10$ fixed, $f(q_0) = 10/q_0$, and
$\mathrm{d}f/\mathrm{d}q_0 = -10/q_0^2 < 0$ for all $q_0 > 0$: strictly decreasing.

$f = 0.20 \Rightarrow q_0 = 10/0.20 = 50\ \mathrm{mW\,m^{-2}}$.

The statement fails when $A_0$ varies because the numerator is no longer fixed. In
the demonstration's own provinces $A_0h$ runs from 6.00 to 14.40
$\mathrm{mW\,m^{-2}}$ while $q_0$ runs from 45 to 90, so both numerator and
denominator change together and the fractions come out 0.133, 0.154 and 0.160 —
rising with $q_0$, the opposite of the fixed-numerator case.

---

## ★★5 — The Clapeyron thermometer

$$\Delta z = \frac{m\,\Delta T}{\rho g}, \qquad
\rho g = 3800\times9.81 = 3.728\times10^{4}\ \mathrm{Pa\,m^{-1}}.$$

- $m = +2.5\times10^{6}\ \mathrm{Pa\,K^{-1}}$:
  $\Delta z = 2.5\times10^{6}\times(-150)/3.728\times10^{4}
  = -1.006\times10^{4}\ \mathrm{m} = -10.1\ \mathrm{km}$ (shallower).
- $m = -2.0\times10^{6}$:
  $\Delta z = -2.0\times10^{6}\times(-150)/3.728\times10^{4}
  = +8.05\ \mathrm{km}$ (deeper).

Separation: $|-10.1| + |+8.05| = 18.1\ \mathrm{km}$ **thicker** in the cold
region.

A 20% error in a slope gives a 20% error in that transition's deflection
($\pm2.0\ \mathrm{km}$ and $\pm1.6\ \mathrm{km}$) and therefore a $\pm20\%$ error
in the inferred $\Delta T$ if the depth is assumed exact: $-150 \pm 30\
\mathrm{K}$. The error is systematic in each slope and only partly cancels in the
separation.

---

## ★★6 — Exponential against linear adiabat

$\alpha g/c_p = 3\times10^{-5}\times9.81/1250 = 2.354\times10^{-7}\
\mathrm{K\,m^{-1}} = 0.2354\ \mathrm{K\,km^{-1}}$ (at 1500 K the *linear* value
used below is $0.2354\times1500/1000$… see arithmetic).

Linear approximation at $T_p = 1500\ \mathrm{K}$:
$\mathrm{d}T/\mathrm{d}z = 0.2354\times1500\times10^{-3} = 0.3531\
\mathrm{K\,km^{-1}}$.

- At 660 km: exact $= 1500\,e^{0.2354\times10^{-3}\times660} = 1500\,e^{0.1554}
  = 1752.2\ \mathrm{K}$; linear $= 1500 + 0.35316\times660 = 1733.1\ \mathrm{K}$;
  difference 19.1 K (1.1%).
- At 2891 km: exact $= 1500\,e^{0.6806} = 2962.8\ \mathrm{K}$; linear
  $= 1500 + 0.35316\times2891 = 2521.0\ \mathrm{K}$; difference **441.8 K
  (14.9%)**.

The error grows because the exponent is not small: at 660 km
$\alpha g z/c_p = 0.155$ (1% error), at the CMB it is 0.68 (15% error). The
approximation is safe for a thin layer and unsafe for the whole mantle.

---

## ★★★7 — Depth-dependent gravity

$g(z) = 9.81(1 - z/6371)$:

- 410 km: $g = 9.81\times0.9356 = 9.18\ \mathrm{m\,s^{-2}}$.
- 660 km: $g = 9.81\times0.8964 = 8.79\ \mathrm{m\,s^{-2}}$.

Recompute the 410-type deflection with the transition's own gravity:

$$\Delta z = \frac{2.5\times10^{6}\times(-150)}{3800\times9.18}
= -1.075\times10^{4}\ \mathrm{m} = -10.7\ \mathrm{km},$$

against $-10.1\ \mathrm{km}$ with the surface value: an under-estimate of the
deflection by **0.69 km (6.9%)**, and the same sign for both transitions.

The error is **systematic**, not random: it is a bias in one direction that
survives averaging. Over a survey, more stations do not fix it; only using $g$ at
the right depth does. A useful rule: the relative error in $\Delta z$ from using
$g_s$ equals $z/R$, i.e. 6.4% at 410 km and 10.4% at 660 km.

---

## ★★★8 — Measuring the neutrino fraction

**Observable.** The direction- and energy-resolved flux of geoneutrinos from
²³⁸U and ²³²Th decay chains, in units of
$\mathrm{cm^{-2}\,s^{-1}\,MeV^{-1}}$, detected by inverse beta decay in a
large liquid-scintillator detector. The *shape* of the energy spectrum between
the decay endpoints encodes the fraction of each decay's energy carried by the
neutrino: if $f_\nu$ were 0, the measured antineutrino endpoint energy would
move.

**Scaling.** For a fixed radiogenic heat production $A$, the antineutrino flux at
the detector is proportional to the number of decays per second, hence
$A / [Q_{\text{tot}}(1-f_\nu)] \times (\text{neutrinos per decay})$. A detector
therefore measures a *combination* of the U and Th inventory and $f_\nu$, not
$f_\nu$ alone.

**Bias.** The dominant bias is the assumed Th/U ratio and the crustal
vs mantle partition: the crustal contribution is closer to the detector and is
weighted differently from the mantle's, so an error in the crustal inventory
mimics a change in the energy budget. A second bias is the detector's
energy-scale calibration, which shifts the endpoint and therefore the fitted
$f_\nu$.

---

## What a good answer looks like

Every part carried units, distinguished measured from derived from adopted, and
never reported a difference of two measured quantities as if it were itself a
measurement.
