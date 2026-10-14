# Solutions — 16-04-02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [02 Feedbacks](../02-climate-feedbacks.md).

---

## ★1 — Planck parameter at 270 K

$$\lambda_0 = -4\sigma T^3 = -4(5.670374419\times10^{-8})(270)^3
= -4.4644\ \mathrm{W\,m^{-2}K^{-1}},$$

$$\Delta T = \frac{2.0}{4.4644} = 0.448\ \mathrm{K}.$$

**Comment.** The magnitude falls with temperature ($T^3$), so a colder planet
has a weaker Planck response and — other things equal — a longer relaxation
time and a larger response to the same forcing. This is the blackbody part of
polar amplification and of the ice-albedo instability.

---

## ★2 — Clausius–Clapeyron rate

$$\frac{\mathrm{d}\ln e_s}{\mathrm{d}T} = \frac{L}{R_vT^2}.$$

- $T = 265$ K: $2.5\times10^6/(461.5\times70225) = 0.07714\ \mathrm{K^{-1}}$
  $= 7.71\%$ per K.
- $T = 305$ K: $2.5\times10^6/(461.5\times93025) = 0.05823\ \mathrm{K^{-1}}$
  $= 5.82\%$ per K.

**Direction.** The rate **decreases** with temperature, because the derivative
carries $1/T^2$. The often-quoted "7% per K" is the mid-tropospheric value near
273 K; it is neither a constant nor a lower bound.

---

## ★3 — Total feedback parameter and response

$$\lambda = \lambda_0 + \sum_i\lambda_i
= -5.418 + 1.2 + 0.35 + 0.5 + 0.2 = -3.168\
\mathrm{W\,m^{-2}K^{-1}},$$

$$\Delta T_\text{eq} = -\frac{F}{\lambda} = \frac{3.7}{3.168}
= 1.168\ \mathrm{K}.$$

**Check on the sign convention.** With $\lambda<0$ the response is positive for
a positive forcing, and the smaller $|\lambda|$ the larger the response. ✔

---

## ★4 — Ranges and where to spend effort

Midpoints: water vapour 1.2, cloud 0.35, albedo 0.25, carbon 0.10, so

$$\lambda = -5.418 + 1.2 + 0.35 + 0.25 + 0.10 = -3.518\
\mathrm{W\,m^{-2}K^{-1}},\qquad
\Delta T = \frac{3.7}{3.518} = 1.052\ \mathrm{K}.$$

**Which range to narrow first.** Compute the response at the ends of each range
with the other feedbacks at their midpoints, and take the span:

| feedback varied | $\Delta T$ at low end (K) | at high end (K) | span (K) |
|---|---|---|---|
| water vapour $[0.9, 1.5]$ | $\lambda = -3.818 \to 0.969$ | $\lambda = -3.218 \to 1.150$ | 0.181 |
| cloud $[-0.3, 1.0]$ | $\lambda = -4.168 \to 0.888$ | $\lambda = -2.868 \to 1.290$ | 0.402 |
| albedo $[0.1, 0.4]$ | $\lambda = -3.668 \to 1.009$ | $\lambda = -3.368 \to 1.099$ | 0.090 |
| carbon $[0.0, 0.2]$ | $\lambda = -3.618 \to 1.023$ | $\lambda = -3.418 \to 1.083$ | 0.060 |

**Narrow the cloud range first**: it contributes a 0.402 K span, more than twice
the next largest. Note that the ranking follows the *width* of the assumed
range, not the size of the mean, exactly as in the lesson's variance
decomposition where cloud supplied 80.7% of the variance.

---

## ★5 — The ice-albedo parameter and the zero-total condition

With $\alpha = \alpha(T)$ and shortwave absorption $(S/4)(1-\alpha)$,

$$\frac{\partial N}{\partial T}\bigg|_{\alpha}
= -\frac{S}{4}\frac{\mathrm{d}\alpha}{\mathrm{d}T}
\;\Longrightarrow\;
\lambda_\text{ice} = -\frac{S}{4}\frac{\mathrm{d}\alpha}{\mathrm{d}T}.$$

Setting $\lambda_0 + \lambda_\text{ice} = 0$:

$$-5.418 - \frac{1361}{4}\frac{\mathrm{d}\alpha}{\mathrm{d}T} = 0
\;\Longrightarrow\;
\frac{\mathrm{d}\alpha}{\mathrm{d}T} = -\frac{5.418}{340.25}
= -0.01592\ \mathrm{K^{-1}}.$$

**What a zero total $\lambda$ means.** $N = F + \lambda\Delta T$ with
$\lambda = 0$ has no solution for $\Delta T$ with $F\ne0$: the system has no
stable equilibrium temperature. It is the marginal case at the edge of
bistability — the point at which the middle, unstable branch of the ice-albedo
model appears (the lesson's ramp slope is $-0.016$, just past this value, which
is why three equilibria exist).

---

## ★6 — Loop edges and their scaling

**(a)** With $A = 203.3$, $B = 2.09$, $T_\text{hi} = 10$,
$T_\text{lo} = -10$, $\alpha_\text{free} = 0.30$, $\alpha_\text{ice} = 0.62$:

$$S_\text{low} = \frac{4(10\times2.09 + 203.3)}{1-0.30}
= \frac{4\times224.2}{0.70} = 1281\ \mathrm{W\,m^{-2}},$$

$$S_\text{high} = \frac{4(-10\times2.09 + 203.3)}{1-0.62}
= \frac{4\times182.4}{0.38} = 1920\ \mathrm{W\,m^{-2}}.$$

Both match the lesson's table (the ice-free branch exists above 1281, the ice
branch below 1920).

**(b)** With $T_\text{lo} = -w$, $T_\text{hi} = +w$:

$$S_\text{high} - S_\text{low}
= 4\left[\frac{A - wB}{1-\alpha_\text{ice}}
- \frac{A + wB}{1-\alpha_\text{free}}\right]
= \underbrace{4A\left[\frac{1}{1-\alpha_\text{ice}}
- \frac{1}{1-\alpha_\text{free}}\right]}_{\text{constant}}
- 4wB\left[\frac{1}{1-\alpha_\text{ice}}
+ \frac{1}{1-\alpha_\text{free}}\right].$$

The width is **linear in the ramp half-width** with coefficient

$$-4(2.09)\left[\frac{1}{0.38} + \frac{1}{0.70}\right]
= -8.36\,(2.6316 + 1.4286) = -33.94\ \mathrm{W\,m^{-2}}\ \text{per }^\circ\text{C}.$$

From the lesson's table: 809 W m⁻² at $w = 5$, 639 at $w = 10$, 299 at
$w = 20$. Differences: $(809-639)/5 = 34.0$ and $(639-299)/10 = 34.0$ ✔ — the
predicted coefficient to three figures. A wider ramp means a weaker
$\mathrm{d}\alpha/\mathrm{d}T$, hence a narrower loop.

---

## ★7 — Tolerable drift slope

The model is $F = (|\lambda_0| - \lambda_{c0} - s\Delta T)\Delta T$ with
$|\lambda_0| - \lambda_{c0} = 4.618$ W m⁻² K⁻¹ and $s>0$ the drift. The linear
estimate is $\Delta T_\text{lin} = F/4.618$; require the exact value to be within
5% of it at $F = 6$ W m⁻².

$$\Delta T_\text{lin} = \frac{6}{4.618} = 1.2993\ \mathrm{K},\qquad
\Delta T_\text{max} = 1.05\times1.2993 = 1.3643\ \mathrm{K}.$$

Substitute $\Delta T_\text{max}$ into the exact relation:

$$s\Delta T_\text{max}^2 - 4.618\,\Delta T_\text{max} + 6 = 0
\;\Longrightarrow\;
1.8612\,s = 6.3003 - 6 = 0.3003
\;\Longrightarrow\;
s = 0.161\ \mathrm{K^{-1}}.$$

So the linear decomposition is acceptable at $F = 6$ W m⁻² as long as the
feedback parameter drifts by less than about $0.16$ W m⁻² K⁻¹ per kelvin. The
lesson's placeholder ($s = 0.15$) is just inside that bound, which is why the
tabulated error is 4.62% rather than 5%.

**An observational constraint that could bound the slope.** The slope is the
derivative of the feedback parameter with respect to global temperature. Two
routes: (i) regress the observed net top-of-atmosphere flux anomaly on the
surface temperature anomaly *within* a single record, and test whether the
regression slope is constant across sub-periods; (ii) estimate the feedback
parameter separately from two climate states that differ substantially in
temperature (for example the seasonal cycle versus the long-term trend) and
compare them. Either route yields a bound, not a value, because the observed
temperature range is small and the flux record is short.

---

## ★8 — Bounding the cloud feedback observationally (specification)

**Diagnostic.** The cloud-radiative contribution to the net top-of-atmosphere
flux: the change in the net flux due to clouds alone, obtained by differencing
all-sky and clear-sky fluxes, split into its shortwave and longwave parts.

**Regression.** Regress the *cloud-induced* net flux anomaly on the surface
temperature anomaly, with the regression coefficient being $\lambda_\text{cloud}$
up to sign. The regression must be run on anomalies (a common climatology
removed), with a lag structure stated in advance, and with the fit reported for
each of the two components separately (shortwave and longwave), because they
have opposite signs and their sum can cancel.

**Confounders to control.** At least four:

1. **Forcing agents that change clouds independently of temperature** —
   aerosols, in particular, which affect cloud droplet number and hence albedo.
2. **Pattern effects** — the same global temperature anomaly produces different
   cloud responses depending on where and when it occurs, so a regression on the
   global mean mixes different regimes.
3. **Autocorrelation and the short record** — both the flux and the temperature
   series are persistent, so the effective sample size is much smaller than the
   number of months (see the AR(1) test in
   [16-03-02](../../03-atmospheric-circulation/02-monsoons-and-regional.md) §8).
4. **Data inhomogeneity** — cloud retrievals change with instrument and
   algorithm, which can produce spurious trends in the differenced quantity.

**Why the result is a bound rather than a value.** The observed global
temperature range is a small fraction of the range over which the feedback
parameter is evaluated, the cloud signal is a residual of two large fluxes, and
the confounders above are not separately observable. A regression therefore
constrains the *sum* of effects in the observed regime; converting it into a
feedback parameter for a doubled-CO₂ climate requires assuming that the
regression transfers to a different pattern of warming. The honest output is a
range, with the dominant systematic stated.
