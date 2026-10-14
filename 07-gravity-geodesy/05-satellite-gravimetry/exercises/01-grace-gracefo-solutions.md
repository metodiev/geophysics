# Solutions — 07-05-01 GRACE and GRACE-FO: Mission Concept and Data Products

> **Read after attempting the exercises.** Several problems have more than one
> defensible answer; where that is true it is said so. Numbers were computed,
> not estimated by hand. All values are **SYNTHETIC** teaching values.

Lesson: [01 GRACE and GRACE-FO](../01-grace-gracefo.md).

---

## ★1 — Orbit geometry at $h = 450\ \mathrm{km}$

$$a = R + h = 6371 + 450 = 6821\ \mathrm{km} = 6.821\times10^{6}\ \mathrm{m},$$
$$a^{3} = 3.17354\times10^{20}\ \mathrm{m^{3}},$$
$$T = 2\pi\sqrt{\frac{3.17354\times10^{20}}{3.986004418\times10^{14}}}
= 2\pi\sqrt{7.9617\times10^{5}} = 2\pi(892.29) = 5606.4\ \mathrm{s}
= 93.44\ \mathrm{min},$$
$$v = \sqrt{\frac{3.986004418\times10^{14}}{6.821\times10^{6}}}
= \sqrt{5.8437\times10^{7}} = 7.6444\times10^{3}\ \mathrm{m\,s^{-1}}
= 7.644\ \mathrm{km\,s^{-1}},$$
$$n = \frac{86400}{5606.4} = 15.411\ \mathrm{rev\,day^{-1}},\qquad
d_{\text{track}} = \frac{2\pi(6371)}{15.411} = 2597.5\ \mathrm{km}.$$

**Units:** $T$ in s (or min), $v$ in m/s (or km/s), $n$ in
$\mathrm{rev\,day^{-1}}$ (dimensionless per day), $d_{\text{track}}$ in km.

---

## ★2 — Equivalent water height

$$\frac{R\rho_e}{3\rho_w}\frac{2l+1}{1+k_l}\Delta C_{20}
= \frac{(6.371\times10^{6})(5513.4)}{3(1000)}\cdot\frac{5}{1-0.30}\cdot
3\times10^{-11}$$
$$= (1.17088\times10^{7})(7.14286)(3\times10^{-11})
= 2.5091\times10^{-3}\ \mathrm{m} = 2.509\ \mathrm{mm}.$$

**Why it is not a local water depth:** a single low-degree coefficient describes
a *spherical-harmonic* pattern spanning the globe, not a deposit at a place. The
same coefficient could be produced by a thin global layer or by a much thicker,
smaller patch, and coefficients up to higher degree are needed before a *local*
water thickness is even defined. The 2.5 mm is the amplitude of a global pattern.

---

## ★3 — Amplification at degree 20

$$A(20) = \left(\frac{a}{R}\right)^{21} = 1.07848^{21}
= e^{21(0.0755526)} = e^{1.58660} = 4.887.$$

A coefficient noise of $2\times10^{-12}$ at degree 20 therefore implies a surface
error of

$$2\times10^{-12}\times4.887 = 9.77\times10^{-12},$$

i.e. the noise is nearly five times larger in the surface field than in the
coefficient that was estimated. This is the formal statement of "the resolution
you can guarantee is worse than the resolution you can estimate".

---

## ★4 — The point-mass identity

**Derivation.** With $\mathbf{q}_i = \mathbf{r}_i - \mathbf{r}_m$ and
$\mathbf{q}_2 - \mathbf{q}_1 = \boldsymbol{\rho} = \rho\hat{\boldsymbol{\rho}}$,

$$\delta a_\rho = -Gm\,\hat{\boldsymbol{\rho}}\cdot
\left[\frac{\mathbf{q}_2}{q_2^{3}} - \frac{\mathbf{q}_1}{q_1^{3}}\right].$$

By symmetry about the midpoint of the link, $|\mathbf{q}_1| = |\mathbf{q}_2| = q$
and the radius to the mass at the midpoint is perpendicular to
$\hat{\boldsymbol{\rho}}$, so
$\hat{\boldsymbol{\rho}}\cdot\mathbf{q}_2 = -\hat{\boldsymbol{\rho}}\cdot
\mathbf{q}_1$. Hence

$$\delta a_\rho = -Gm\,\frac{\hat{\boldsymbol{\rho}}\cdot(\mathbf{q}_2 -
\mathbf{q}_1)}{q^{3}} = -\frac{Gm\rho}{q^{3}}. \qquad\blacksquare$$

**Numbers.** $m = \rho_w t\pi r^{2} = 1000(0.05)\pi(2\times10^{5})^{2}
= 6.2832\times10^{12}\ \mathrm{kg}$.

$$\delta a_\rho = -\frac{(6.67430\times10^{-11})(6.2832\times10^{12})
(2.0\times10^{5})}{(5.0\times10^{5})^{3}}
= -\frac{8.387\times10^{7}}{1.25\times10^{17}}
= -6.71\times10^{-10}\ \mathrm{m\,s^{-2}}.$$

Signal-to-noise against $1\times10^{-10}\ \mathrm{m\,s^{-2}}$ is $6.7$: the half-
size anomaly is five times weaker than the lesson's $10\ \mathrm{cm}$ example,
which had $31$. Detection thresholds scale roughly with the *mass*, since
$\delta a_\rho \propto m$ for fixed geometry.

---

## ★5 — A $3\times$ tolerance

$$A(l) = 1.07848^{\,l+1} < 3
\quad\Longrightarrow\quad
l+1 < \frac{\ln 3}{\ln 1.07848} = \frac{1.098612}{0.0755526} = 14.54 .$$

So $l + 1 \le 14$, i.e. $l_{\max} = 13$. Check: $A(13) = 1.07848^{14}
= e^{1.05774} = 2.880 < 3$ ✔ and $A(14) = 1.07848^{15} = e^{1.13329} =
3.106 > 3$ ✘.

Half-wavelength: $\pi R/l = \pi(6371)/13 = 1540\ \mathrm{km}$. The $10\times$
tolerance gave $l = 29$ and $690\ \mathrm{km}$. **Tightening the noise tolerance
by a factor of three costs a factor of two in linear resolution** — the
resolution of a satellite solution degrades only logarithmically with noise, and
that is why mission lifetime matters more than instrument precision for
long-wavelength products.

---

## ★6 — Halving the repeat cycle

Revolutions per cycle: $n \times k = 15.2431 \times 61 = 929.8$ (61 days) and
$15.2431 \times 30 = 457.3$ (30 days).

Track spacing in a repeat cycle of $k$ days is $2\pi R/(nk)$:

| $k$ (days) | revolutions $nk$ | track spacing |
|---|---|---|
| 61 | 929.8 | 43.0 km |
| 30 | 457.3 | 87.5 km |

**Reasons the proposal is not free:**

1. **Sampling gets coarser.** Halving the cycle doubles the equatorial track
   spacing from 43 km to 88 km, so the *spatial* resolution of the resulting
   field drops even though the *temporal* resolution improves.
2. **Noise averaging gets worse.** Each solution averages half as many data, so
   the coefficient error rises (roughly as $1/\sqrt{2}$ for white noise), and the
   usable degree falls because of the amplification table.
3. **A repeat cycle must be commensurate.** A repeat requires $nk$ to be
   (nearly) an integer. With $n = 15.2431$, the demonstration's $k = 61$ gives
   $nk = 929.8$ — not an integer, so it is a chosen teaching value rather than an
   exact repeat. A commensurate alternative is $k = 41$, where
   $nk = 624.97 \approx 625$; that yields a 64.0 km track spacing.

An honest answer names which resource is being traded, and a *design* answer
would also state the target: is the requirement temporal (floods, seasonal
cycles) or spatial (basin boundaries)?

---

## ★7 — Leakage experiment (specification)

A specification that could be executed:

1. **Truth.** Put a uniform $10\ \mathrm{cm}$ water-equivalent disc of radius
   $300\ \mathrm{km}$ at a stated latitude/longitude, and a second, *empty*
   region of the same shape displaced one disc-diameter away.
2. **Forward model.** Expand the disc's surface density into fully normalised
   coefficients $\Delta C_{lm}$ for $0 \le l \le 60$ by numerical integration of
   the layer formula in the lesson's Section 6 (Gauss–Legendre in
   $\cos\theta$ and a trapezoidal sum in $\phi$).
3. **Observation operator.** Truncate at $L = 60$, add white coefficient noise of
   $1\times10^{-12}$ per degree, then continue downward with $(a/R)^{l+1}$ using
   the lesson's $a/R = 1.07848$.
4. **Inversion/analysis.** Reconstruct a mass map at a stated filter radius $r_f$
   (a Gaussian spatial average in the harmonic domain), for
   $r_f \in \{200, 400, 800, 1600\}\ \mathrm{km}$.
5. **Metrics.** (a) peak amplitude recovered inside the disc divided by the truth
   (the *amplitude bias*); (b) mass recovered in the empty region divided by the
   truth mass (the *leakage*); (c) rms noise outside both regions.
6. **Prediction.** As $r_f$ grows, (a) falls and (b) falls: a wider filter
   suppresses noise and spreads the signal, so the recovered peak is *biased low*
   while the empty region receives a *positive* apparent mass from its neighbour.
   The bias–variance trade curve has no minimum that the data can identify for
   you; the choice is set by the science question.

---

## ★8 — Error propagation of a wrong $k_l$

Write $k_l^{\text{used}} = k_l(1+\epsilon)$ with $|\epsilon| = 0.10$. The EWH
factor is $(1+k_l)^{-1}$, so a coefficient's EWH is wrong by the relative factor

$$\left|\frac{\delta \text{EWH}}{\text{EWH}}\right|
= \frac{|k_l|\,\epsilon}{1+k_l}
= \frac{0.30 \times 0.10}{0.70} = 4.3\%
\quad\text{at } l = 2 .$$

**(i) A single coefficient** is therefore biased by $4.3\%$ (per unit
$\epsilon = 0.1$), independent of its magnitude. The sign follows the sign of
$\epsilon$: a $k_2$ that is too *negative* makes $1+k_l$ too small and the mass
too large.

**(ii) A national-scale trend** concentrated in degrees 2–8 is a *sum* of
coefficients $(2l+1)/(1+k_l)\Delta C_{lm}$. Since $k_l$ for load Love numbers
becomes less negative as $l$ grows (the elastic response weakens), the
$4\%$-at-degree-2 error is not uniform across the band: the *spectral shape* of
the reconstructed mass is distorted, not just its amplitude. The reconstructed
pattern changes, so some of the apparent spatial structure is an artefact of the
wrong $k_l$.

**Which is more robust?** The *integrated* mass over a large region is more
robust than any single coefficient, because the region integral is dominated by
the lowest degrees where $|k_l|$ is smallest relative to 1 and where the error
compensates between neighbouring coefficients. The **spatial pattern** is the
fragile part. This is the reason regional mass-budget studies quote a total over
a well-defined basin and report the filter explicitly, rather than drawing a
"mass map".
