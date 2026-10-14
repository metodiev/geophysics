# Solutions — 16-07-01 Extreme Events: Statistics and Physical Drivers

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown. Several problems have more than one defensible
> answer, and where that is true it is stated.

Lesson: [01 Extreme Events](../01-climate-extremes.md).

---


## ★ Foundational

## ★1 — Return levels from GEV parameters

$$z_T = \mu + \frac{\sigma}{\xi}\left[\left(-\ln\left(1-\tfrac{1}{T}\right)\right)^{-\xi}-1\right],
\qquad \frac{\sigma}{\xi} = \frac{15.0}{0.20} = 75.0\ \mathrm{mm\,day^{-1}}.$$

$T=10$: $-\ln(0.9) = 0.105361$; $0.105361^{-0.20} = e^{0.20\times2.25037} = 1.56843$;
$z_{10} = 100.0 + 75.0(0.56843) = \mathbf{142.63\ \mathrm{mm\,day^{-1}}}$.

$T=50$: $-\ln(0.98) = 0.0202027$; $0.0202027^{-0.20} = e^{0.20\times3.90197} = 2.18245$;
$z_{50} = 100.0 + 75.0(1.18245) = \mathbf{188.67\ \mathrm{mm\,day^{-1}}}$.

Units: $\sigma/\xi$ carries mm/day, and the bracket is dimensionless, so $z_T$ is
in mm/day. ✔

---

## ★2 — The Gumbel limit

For $\xi\to0$, $z_T = \mu - \sigma\ln\left(-\ln(1-1/T)\right)$:

$T=10$: $-\ln(0.105361) = 2.25037$, so $z_{10} = 100.0 - 15.0(0.81195) = 133.76$.

$T=50$: $-\ln(0.0202027) = 3.90197$, so $z_{50} = 100.0 - 15.0(1.36143) = 158.53$.

The positive shape **raises** the far-tail level: $142.63$ vs $133.76$ at $T=10$
($+6.6\%$) and $188.67$ vs $158.53$ at $T=50$ ($+19\%$). The effect grows with
$T$, which is exactly why the shape cannot be chosen by convenience.

---

## ★3 — POT return level

$$z_T = u + \frac{\tilde\sigma}{\xi}\left[(\lambda T)^{\xi}-1\right],
\qquad \frac{\tilde\sigma}{\xi} = \frac{16.0}{0.12} = 133.33\ \mathrm{mm\,day^{-1}}.$$

$\lambda T = 2.5\times20 = 50$. $50^{0.12} = e^{0.12\times3.91202} = e^{0.469443} = 1.59908$.

$z_{20} = 90.0 + 133.33(0.59908) = \mathbf{169.88\ \mathrm{mm\,day^{-1}}}$.

---

## ★★ Applied

## ★★4 — The GEV–GPD parameter link

Put the GEV form and the POT form side by side at a common return period:

$$\underbrace{\mu + \frac{\sigma}{\xi}\left[(-\ln(1-\tfrac1T))^{-\xi}-1\right]}_{\text{GEV}}
=\underbrace{u + \frac{\tilde\sigma}{\xi}\left[(\lambda T)^{\xi}-1\right]}_{\text{POT}}.$$

Both describe the same tail if the exceedance rate is the GEV probability of
exceeding the threshold,
$\lambda = \left[1+\xi(u-\mu)/\sigma\right]^{-1/\xi}$, and the scales are related
by

$$\tilde\sigma = \sigma + \xi(u-\mu).$$

Substituting $\tilde\sigma$ and $\lambda$ into the POT form reduces it to the GEV
form, so the identity is exact *when both are taken from the same parent
distribution*.

*Numerical check.* With the demonstration's block-maxima parameters mapped to
$u = 90.21\ \mathrm{mm\,day^{-1}}$:

$$\tilde\sigma = 17.51 + 0.1105\times(90.21-111.67) = 17.51 - 2.372
= 15.14\ \mathrm{mm\,day^{-1}}.$$

The directly fitted GPD scale in the demonstration is
$15.864\ \mathrm{mm\,day^{-1}}$, so the mapping is low by $4.6\%$. That residual
is expected and instructive: the block-maxima GEV is fitted to *annual maxima*,
while the GPD is fitted to *daily exceedances of one threshold*, and the two are
exactly linked only in the limit where the block maximum is drawn for the same
parent. The approximate agreement is evidence that both are describing the same
tail; the residual is the price of extrapolating the asymptotic link to a finite
record.

---

## ★★5 — Sample size and the $1/\sqrt n$ rate

Predicted change in interval width from $n=50$ to $n=1000$ if the width scaled as
$1/\sqrt{n}$:

$$\sqrt{\frac{1000}{50}} = \sqrt{20} = 4.47.$$

Observed change: $106.1 / 19.7 = 5.39$.

The observed width shrinks **faster** than $1/\sqrt{n}$ — by a factor $5.39$ where
$4.47$ was expected, about $20\%$ more. Interpretation: $1/\sqrt n$ is the
*asymptotic* rate. At $n=50$ the estimate is not in its asymptotic regime, so its
spread is inflated above the asymptotic prediction; part of the apparent gain from
a longer record is not the ordinary averaging of $n$ samples but the *arrival of
the regime in which the limit law applies at all*. For a short record the relevant
statement is therefore not a clean sample-size scaling but "not yet asymptotic".

---

## ★★6 — Reporting a 100-year level under a trend

Model answer:

> "The 100-year return level is a property of a *reference climate*, not a fixed
> number. In the climate of 2050 the estimated level is $X$ mm/day (95% interval
> $A$–$B$), where the estimate assumes the fitted linear trend in the location
> parameter continues unchanged and that the shape and scale remain constant. In
> the climate of the record midpoint the same method gives $Y$ mm/day. The
> difference $X-Y$ is attributable to the trend, not to sampling: the trend is
> significant at the 5% level. If the trend were to flatten, the 2050 level would
> fall toward $Y$."

A defensible answer names (i) the reference climate, (ii) the trend-continuation
assumption, (iii) the constancy assumption on scale and shape, and (iv) an
interval. Quoting one number without the reference climate is the error the
exercise is testing for.

---

## ★★★ Research-oriented

## ★★★7 — Mixture experiment (design)

**Setup.** Generate a daily series as a mixture: on each day, draw regime
$r \in \{A,B\}$ with probability $p$ (a two-state synthetic "circulation index"),
then draw rainfall from GEV$_A$ or GEV$_B$ with different locations
($\mu_A = 30$, $\mu_B = 55\ \mathrm{mm\,day^{-1}}$) and a common shape. Block into
annual maxima and fit a single GEV.

**Metric.** Report (i) the fitted shape $\hat\xi$ against the component shapes,
(ii) the 100-year return level against the population level of the mixture (which
you can compute numerically by integrating the mixture), and (iii) a
quantile–quantile comparison against the single-population GEV.

**Prediction to test.** A single GEV fitted to a mixture will absorb the
between-regime spread into the scale and the shape; if the two components have
similar shapes, $\hat\xi$ should be *larger* than either component's shape
(because a mixture of light tails mimics a heavier one), and the 100-year level
should be biased **high**.

**Falsification.** The single-population model is falsified if the QQ plot shows
systematic curvature (a mixture signature) while the fitted shape is close to the
weighted mean of the component shapes — i.e., if the diagnostics reject the single
GEV even though the shape looks plausible.

---

## ★★★8 — Scalings above $7\%/\mathrm{K}$

Three mechanisms that can push a rainfall-extreme scaling above the thermodynamic
moisture scaling, each with a distinguishing observable:

1. **Enhanced moisture convergence (dynamics).** In a warmer atmosphere the
   horizontal convergence of moisture in a storm can increase in proportion to
   the moisture content itself, giving a scaling closer to the *moisture* scaling
   applied twice over the convergence field.
   *Observable:* the vertically integrated moisture-flux convergence during
   extreme events, compared with the thermodynamic contribution alone; if the
   flux convergence increases, the dynamical term is real.

2. **A shift toward longer or larger organised systems.** If events lengthen or
   grow in area, the *accumulated* rainfall over a fixed duration rises faster
   than the rate.
   *Observable:* event duration and spatial extent statistics separately from
   intensity; a duration increase with constant intensity is a different
   mechanism from an intensity increase.

3. **A change in precipitation efficiency or in the fraction of rainfall falling
   in the heaviest hours.** Reorganisation of convection can move water to the
   surface more efficiently, and a redistribution from light to heavy rainfall
   raises the extreme quantile without changing the mean.
   *Observable:* the precipitation efficiency (surface rain divided by
   condensate) and the fraction of total rainfall in the top 1% of hours.

The key point is that none of these is a violation of Clausius–Clapeyron; they are
*additional* terms. The thermodynamic scaling sets the moisture supply, and the
observed scaling is the product of that supply with whatever the dynamics and the
event structure do — which is why a single observed scaling number is not, by
itself, an attribution.
