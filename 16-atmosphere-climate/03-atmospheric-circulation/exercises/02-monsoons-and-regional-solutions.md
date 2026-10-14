# Solutions — 16-03-02 Monsoons, Regional Circulation and Teleconnections

> **Read after attempting the exercises.** Where a problem has more than one
> defensible answer that is said so. Numbers were computed, not estimated by
> hand.

Lesson: [02 Monsoons, Regional Circulation and Teleconnections](../02-monsoons-and-regional.md).

---

## ★1 — Slab response

$\omega = 2\pi/(365\times86400) = 1.9924\times10^{-7}\ \mathrm{s^{-1}}$.

$$C\omega = 5\times10^7\times1.9924\times10^{-7} = 9.962\
\mathrm{W\,m^{-2}K^{-1}},$$

$$|\hat T| = \frac{40.0}{\sqrt{5.42^2+9.962^2}} = \frac{40.0}{11.34}
= 3.53\ \mathrm{K},$$

$$\varphi = \arctan\frac{9.962}{5.42} = 1.0735\ \mathrm{rad} = 61.5^\circ
= 62.3\ \mathrm{d}.$$

**Sanity check.** $C = 5\times10^7$ lies between the land and ocean values of
the lesson, and so do the answers: 3.53 K between 5.95 and 0.97 K, 62 days
between 36.8 and 83.6 days. A monotone interpolant is the right answer to
expect.

---

## ★2 — Heat low

$$\Delta p_s = -\frac{p_s\Delta T}{T}
= -\frac{1.013\times10^5\times3}{300} = -1013\ \mathrm{Pa} = -10.13\ \mathrm{hPa}.$$

**Why the real value is smaller.** The warming is not uniform through the whole
column, so the depth over which the density reduction is integrated is smaller
than the full atmosphere; and the low-level convergence that the pressure
gradient drives raises the surface pressure, partly cancelling the perturbation.

---

## ★3 — Stationary wavenumber

$$\beta = \frac{2\Omega\cos\phi}{a}
= \frac{2(7.292115\times10^{-5})(0.707107)}{6.371\times10^6}
= 1.619\times10^{-11}\ \mathrm{m^{-1}s^{-1}},$$

$$K_s = \sqrt{\frac{\beta}{U}} = \sqrt{\frac{1.619\times10^{-11}}{15}}
= 1.039\times10^{-6}\ \mathrm{m^{-1}},$$

$$\lambda_s = \frac{2\pi}{K_s} = 6.05\times10^6\ \mathrm{m} = 6048\ \mathrm{km}.$$

**Units.** $\beta$ is $\mathrm{m^{-1}s^{-1}}$, $U$ is
$\mathrm{m\,s^{-1}}$, so $\beta/U$ is $\mathrm{m^{-2}}$ and $K_s$ is
$\mathrm{m^{-1}}$; its reciprocal is a length.

---

## ★4 — Neutral mode of the delayed oscillator

Neutrality means zero growth rate, so $T\sim\mathrm{e}^{\mathrm{i}\omega t}$ with
$\omega$ real. Substituting into
$\mathrm{d}T/\mathrm{d}t = aT(t)-bT(t-\tau)$ gives

$$\mathrm{i}\omega = a - b\mathrm{e}^{-\mathrm{i}\omega\tau}
= a - b\cos\omega\tau + \mathrm{i}\,b\sin\omega\tau .$$

Matching real and imaginary parts: $a = b\cos\omega\tau$ and
$\omega = b\sin\omega\tau$. Squaring and adding,

$$a^2+\omega^2 = b^2 \quad\Longrightarrow\quad \omega = \sqrt{b^2-a^2},$$

and then $\cos\omega\tau = a/b$ gives
$\tau = \arccos(a/b)/\omega$ (taking the principal value, which is the
smallest positive delay).

With $a = 0.004$, $b = 0.02\ \mathrm{d^{-1}}$:

$$\omega = \sqrt{4\times10^{-4}-1.6\times10^{-5}} = \sqrt{3.84\times10^{-4}}
= 0.019596\ \mathrm{d^{-1}},$$

$$P = \frac{2\pi}{\omega} = \frac{6.2832}{0.019596} = 320.6\ \mathrm{d}
= 10.53\ \text{months},$$

$$\tau = \frac{\arccos(0.2)}{0.019596} = \frac{1.36944}{0.019596}
= 69.9\ \mathrm{d} = 2.30\ \text{months}.$$

**Comment.** $a<b$ is required for an oscillatory (rather than purely growing)
mode: if $a\ge b$ the discriminant is negative and there is no oscillation.

---

## ★5 — Thermocline tilt

**(a)** The relation is linear in $\tau$:
$\partial h/\partial x = \tau/(\rho_0g'H)$. A 50% larger stress gives a 50%
larger slope, hence a 50% larger tilt:

$$\text{new tilt} = 243.9\times1.5 = 365.9\ \mathrm{m},$$

an increase of $121.9$ m over the basin.

**(b)** Assumptions: (i) steady state — no acceleration or wave propagation;
(ii) a constant-thickness surface layer with a fixed reduced gravity, so the
pressure gradient is entirely due to the interface slope. If $H$ were 50 m
instead of 150 m, the same stress would give three times the tilt
($\propto 1/H$): $731.7$ m. That sensitivity is why a claimed thermocline
displacement is only as good as the layer depth it assumes.

---

## ★6 — Significance thresholds

**(a)** $2/\sqrt{40} = 2/6.3246 = 0.316$.

**(b)** $r = 0.42 > 0.316$ → **passes** the white-noise test.
$r = 0.42 < 0.432$ → **fails** the AR(1) test at the 5% level.

**(c)** Lag-1 autocorrelation of $0.6$ means consecutive years carry partly the
same information, so 40 annual values contain fewer than 40 independent pieces
of evidence. The Monte Carlo null, built from series with the same persistence,
therefore has a wider distribution than white noise, and its 95th percentile is
larger. Quoting the white-noise threshold on a persistent record overstates
significance.

---

## ★7 — "ENSO must be a delayed oscillator" (counter-argument)

Four points, all from this lesson:

1. **Different oscillators share periods.** Section 6.2 says a period is not an
   identification; a recharge oscillator, a seasonal phase-locking argument or a
   stochastically forced damped mode can all be tuned to four years. Agreement
   of a period is therefore weak evidence.
2. **The model does not predict amplitude**, and it does not predict spatial
   structure, seasonal phase-locking or the asymmetry between warm and cold
   events — all of which are prominent features of the phenomenon it claims to
   explain.
3. **The delay is a predicted quantity.** The model fixes $\tau$ once $a$ and
   $b$ are chosen (Section 6.2). A claim of mechanism must state a delay and
   show that the ocean actually adjusts on that timescale; otherwise the
   agreement is a fit, not a test.
4. **The nonlinear term is a placeholder.** $cT^3$ limits the amplitude without
   any ocean dynamics; the model is silent on what sets $c$.

**Discriminating observation.** A measured lag between the wind-stress
anomaly and the thermocline/SST response that matches the delay the model
requires, with the *sign and meridional structure* of the ocean-wave
propagation (equatorial Kelvin then reflected Rossby waves) resolved by
observations. A period alone cannot do it; a delay plus a propagation pathway
can.

---

## ★8 — Designing the test (specification)

**Indices.** (i) The regional anomaly: a pre-registered, physically motivated
scalar (for example an area-averaged rainfall or low-level wind anomaly), with
the averaging region, the season and the detrending stated *before* the data are
seen. (ii) The remote mode: an index from a defined region, or a principal
component of the remote field, again pre-registered.

**Null model.** AR(1) (or AR(2)) surrogates matched to the *observed*
autocorrelation and variance of each series, with at least $10^4$ realisations;
optionally a phase-randomised surrogate that preserves the power spectrum but
destroys cross-series phase. Report the empirical $p$-value of $\lvert r\rvert$
at each lag, corrected for the number of lags tested (a multiple-comparison
correction is mandatory when you scan lags).

**Lag structure.** State the range of lags tested and why, and whether the
maximum over lags was selected *post hoc* — if it was, the significance must be
assessed against the maximum-lag statistic, not the single-lag $p$-value.

**Degrees of freedom.** Do **not** claim $n-2$; claim an effective sample size
based on the autocorrelation (for AR(1), approximately
$n_\text{eff} = n(1-\phi)/(1+\phi)$) and say so explicitly, or rely on the
Monte Carlo null which handles it automatically.

**Distinguishing teleconnection from common driver.** A common driver predicts a
*simultaneous* relationship with both regions and no lagged asymmetry; a true
teleconnection predicts a specific lag consistent with a wave's group velocity
(the eastward energy propagation of Section 7.3) and a spatial pattern consistent
with the stationary-wave ray path ($K_s^2-k^2>0$ along the route). Evidence
therefore consists of (i) the right lag sign and magnitude, (ii) a spatial
pattern matching the waveguide, and (iii) insensitivity to the removal of the
suspected common driver (for example re-computing with the ENSO signal linearly
removed). A design that omits point (iii) cannot separate the two hypotheses and
is an incomplete answer.
