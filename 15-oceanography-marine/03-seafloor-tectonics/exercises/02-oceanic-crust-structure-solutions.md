# Solutions — 15-03-02 Oceanic Crust Structure and Ophiolites

> **Read after attempting the exercises.** Lesson:
> [02 Oceanic Crust Structure and Ophiolites](../02-oceanic-crust-structure.md).
> All numbers are from the lesson's SYNTHETIC model.

## ★ Foundational

## ★1 — Two-layer intercept

$\sin\theta_0 = v_0/v_1 = 2.95/5.10 = 0.57843$ (dimensionless),
$\cos\theta_0=\sqrt{1-0.57843^2}=\sqrt{0.66542}=0.81575$.

$$t_i=\frac{2h_0\cos\theta_0}{v_0}=\frac{2\times0.40\times0.81575}{2.95}
=\frac{0.65260}{2.95}=0.22122\ \mathrm{s}.$$

Travel time at 15 km: $t=15/5.10+0.22122=2.94118+0.22122
=3.16240\ \mathrm{s}$.

Units: $h_0\cos\theta_0$ is km, divided by km/s gives s; $x/v_1$ is km/(km/s) = s.
Both terms are times, as required.

## ★2 — Crossover distance

$$x_c=\frac{t_i^{(2)}-t_i^{(1)}}{1/v_1-1/v_2}
=\frac{0.62-0.30}{1/4.00-1/6.50}=\frac{0.32}{0.25-0.153846}
=\frac{0.32}{0.096154}=3.328\ \mathrm{km}.$$

A spread shorter than 3.33 km never records the deeper refractor as a first
arrival, so the second layer's velocity cannot be measured from it at all — this
is a detection failure, not merely a resolution one.

## ★3 — Layer 2B

Layer 2B is the **sheeted dyke complex**: sub-vertical basaltic dykes that fed the
extrusives. Its velocity is higher than layer 2A's because the dykes are
essentially non-porous — the cracks that formed as the lava quenched are filled or
absent — whereas 2A is a rubble of pillows and flows with several per cent
connected porosity. In this model the contrast is $3.00$ versus
$5.20\ \mathrm{km\,s^{-1}}$, and it is a porosity contrast, not a depth or
pressure effect.

## ★★ Applied

## ★4 — Seeing the mantle branch

$$t(40)=40/8.10+1.2423=4.93827+1.2423=6.1806\ \mathrm{s},$$
$$t(100)=100/8.10+1.2423=12.34568+1.2423=13.5880\ \mathrm{s}.$$

The mantle branch becomes the first arrival beyond the crossover distance
computed in the lesson, $29.677$ km. The smallest useful spread is therefore about
$30$ km for a 5.55 km Moho: a ratio of $5.35$, i.e. a rule of thumb of roughly
five times the target depth. Note that a 40 km spread sees the branch over only
10 km of offsets, which is a narrow basis for a slope.

## ★5 — Trade-off coefficient

$$t_i=2h_0\sqrt{v_0^{-2}-v_1^{-2}}
=2h_0\left(v_0^{-2}-v_1^{-2}\right)^{1/2}.$$

Taking logarithms,
$\ln t_i=\ln 2h_0+\tfrac{1}{2}\ln(v_0^{-2}-v_1^{-2})$, so

$$\frac{\partial\ln t_i}{\partial\ln v_0}
=\frac{1}{2}\cdot\frac{-2v_0^{-3}}{v_0^{-2}-v_1^{-2}}\cdot v_0
=\frac{-v_1^2}{v_1^2-v_0^2},\qquad
\frac{\partial\ln t_i}{\partial\ln h_0}=1 .$$

Holding $t_i$ fixed, $\mathrm{d}\ln h_0 = -\dfrac{\partial\ln t_i/\partial\ln v_0}
{\partial\ln t_i/\partial\ln h_0}\mathrm{d}\ln v_0$, hence
$\dfrac{\mathrm{d}h/h}{\mathrm{d}v/v}=\dfrac{v_1^2}{v_1^2-v_0^2}$. ✔

For $v_0=3.00$, $v_1=6.00$: $36/(36-9)=36/27=1.333$. A 5% velocity error gives a
$1.333\times5\%=6.67\%$ thickness error: $0.50\times0.0667=0.0333$ km, i.e.
$h_0=0.50\pm0.033$ km.

## ★6 — Mixture bounds at 30% serpentine

With $f_{\text{serp}}=0.30$, peridotite $p_a=8.10$, serpentinite $p_b=5.10$:

- Voigt: $0.70\times8.10+0.30\times5.10=5.670+1.530=7.200\ \mathrm{km\,s^{-1}}$
- Reuss: $\left(0.70/8.10+0.30/5.10\right)^{-1}
  =\left(0.086420+0.058824\right)^{-1}=1/0.145243=6.885\ \mathrm{km\,s^{-1}}$
- geometric mean: $\sqrt{7.200\times6.885}=\sqrt{49.57}=7.041\ \mathrm{km\,s^{-1}}$

Densities with $\rho_a=3.30$, $\rho_b=2.55\ \mathrm{g\,cm^{-3}}$: Voigt
$=0.70\times3.30+0.30\times2.55=2.310+0.765=3.075$; Reuss
$=\left(0.70/3.30+0.30/2.55\right)^{-1}=\left(0.212121+0.117647\right)^{-1}
=3.032\ \mathrm{g\,cm^{-3}}$.

**Voigt and Reuss are rigorous bounds** for a two-phase mixture of known volume
fractions, whatever the geometry. The geometric mean is **not** a bound — it is a
middle estimate chosen here as a model, and it would be wrong to call it a bound.
(Cross-check against the demonstration: at $f=0.20$ the same formulae give
Voigt 7.50 and Reuss 7.25, which are the table's values. ✔)

## ★★★ Research-oriented

## ★7 — Specifying the pick accuracy for a 5% thickness

The demonstration's Monte Carlo gives $\sigma_{h_0}=0.048$ km for
$\sigma_t=10$ ms, i.e. 10.7% of the 0.45 km layer. Two routes to 5%:

1. **Better picks.** For a linear least-squares fit, $\sigma_h \propto \sigma_t$
   (the intercept variance scales with the noise variance, with the geometry held
   fixed). To halve the thickness error, halve the pick error: $\sigma_t\approx5$
   ms. This is achievable with modern digitised picks on high-S/N seafloor data,
   but it also halves the *velocity* error, so both improve together.
2. **Longer offsets.** The intercept variance falls as $\sigma_t^2\propto
   1/\sum(x_i-\bar x)^2$: extending the 2B branch from 19 km to, say, 37 km
   roughly doubles the span and quadruples $\sum(x_i-\bar x)^2$, halving the
   intercept error at constant pick quality and cost. **This is the route I would
   choose**, because pick quality is limited by the wavelet and the noise while
   offset range is limited only by the ship's time — and the longer spread also
   improves the deeper layers simultaneously.

**Assumption that makes the scaling valid:** the picks are independent, unbiased
and Gaussian, and the model geometry (flat layers) is correct. If the residuals
are correlated — for example because the seafloor relief is unmodelled — then
extending the offset range adds correlated error faster than it adds information,
and route 2 fails while route 1 still works.

## ★8 — Models for a velocity step at 5.5 km

| model | observable that distinguishes it | precision needed | comment |
|---|---|---|---|
| serpentinised mantle | $v_p/v_s$ high ($\nu\to0.32$) | $v_s$ to $\sim0.1\ \mathrm{km\,s^{-1}}$ | the lesson's Reuss mixing reaches $7.50\ \mathrm{km\,s^{-1}}$ at only 0.14 serpentine |
| thick gabbro-to-peridotite transition | gradational, frequency-dependent velocity step; wide-angle reflectivity weak at high frequency | travel-time residuals at the 10–50 ms level as a function of frequency | can mimic a step at one frequency band |
| underplated body | a positive density anomaly for its velocity; a reflection with reversed polarity | gravity to a few mGal at the right wavelength, plus polarity | density and velocity are not perfectly correlated, so this pair discriminates |
| a real step from gabbro to fresh peridotite | $v_s$ with $\nu\approx0.25$, sharp reflectivity, density jump consistent with $6.8\to8.1$ | as above | the default interpretation |

**What remains untestable from the listed measurements:** the *sharpness* of the
transition at scales finer than the seismic wavelength. A 5 m thick
serpentinised boundary and a sharp contact produce indistinguishable
long-wavelength travel times, so the mechanical and hydrological behaviour of the
boundary — which is what matters for subduction inputs and for the permeability
of the lower crust — is not determined by the seismic data alone. Resolving it
requires drilling or a laboratory analogue.
