# Solutions — 17-03-03 InSAR Time Series: PS-InSAR and SBAS

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [03 InSAR Time Series](../03-insar-time-series.md).

---

## ★1 — Rank and null space of a connected network

$N = 30$ dates, one connected component ($c = 1$):

$$\operatorname{rank}(A) = N - c = 29, \qquad \dim\ker(A) = c = 1.$$

**Physical meaning of the null vector:** it is the constant vector, so the data
determine only *differences* of phase between dates. Adding an arbitrary constant
to every date's phase changes no pair difference, hence no observation. The
absolute phase — equivalently, the absolute displacement of the region — is not
in the data and must come from an external reference (a GNSS station, a
corner reflector, or a stated assumption).

---

## ★2 — A closure phase

Using the signs consistently,
$$d_{12} + d_{23} - d_{13} = 1.80 + (-0.60) - 2.40 = -1.20\ \mathrm{rad}.$$

Now test it against the two candidate explanations:

- an **integer cycle slip** must give a closure that is a multiple of $2\pi$:
  $-1.20/(2\pi) = -0.191$, not an integer, so this is *not* a cycle slip;
- it is also not zero, so something is wrong.

**Verdict:** a gross error (processing, decorrelation-driven phase noise, or an
aliased gradient) in at least one of the three pairs. A $1.20\ \mathrm{rad}$
error is $1.20\lambda/(4\pi) = 1.20\times0.056565/(4\pi) = 5.40\ \mathrm{mm}$ of
LOS displacement — larger than the $2.251\ \mathrm{mm}$ noise per pair quoted in
the lesson, so it is significant and must be located, not absorbed.

---

## ★3 — From phase precision to a rate uncertainty

$$\sigma_{d} = \sigma_\varphi\frac{\lambda}{4\pi}
= 0.50 \times \frac{0.056565}{4\pi} = 2.251\times10^{-3}\ \mathrm{m}
= 2.251\ \mathrm{mm}.$$

For the longest baseline $T = 1.0$ yr, treating a single pair as the rate
measurement,
$$\sigma_v = \frac{\sigma_d}{T} = \frac{2.251\ \mathrm{mm}}{1.0\ \mathrm{yr}}
= 2.25\ \mathrm{mm\,yr^{-1}}.$$

That is a *single-pair* number; the network of Section 3.3 improves it by the
measured factor, which for 339 pairs was $2.25/0.563 \approx 4.0$ in the
demonstration. The point of the exercise is the direction of the reasoning: a
phase precision, a wavelength and a baseline length are all that convert an
interferometric quality metric into a rate uncertainty.

---

## ★4 — A split network

**(a)** $N = 20$, two components ($c = 2$):
$$\operatorname{rank}(A) = 20 - 2 = 18, \qquad \dim\ker(A) = 2.$$

**(b)** Using the kernel argument — a vector in $\ker(A)$ is constant on each
connected component, and nothing else is:

| quantity | determined? | why |
|---|---|---|
| rate within component 1 | **yes** | the component is internally connected, so all differences inside it, and hence its trend, are constrained |
| rate within component 2 | **yes** | same argument, independently |
| offset difference between the components | **no** | adding +const to component 1 and −const to component 2 is a null vector: every pair difference is unchanged |

This is exactly what the lesson measures: with the bridge pairs removed, the
per-component velocities were identical to four decimals, while the offset moved
by $-3.2473$ rad ($-14.617\ \mathrm{mm}$ of LOS). Disconnection costs the
*level*, not the *trend* — and it costs it absolutely, since no amount of
processing recovers an offset that no observation links.

---

## ★5 — Why longer baselines discriminate

**Mechanism.** The velocity error enters each pair's residual multiplied by that
pair's baseline $\Delta t$:
$$r_k = \frac{4\pi \cos\theta}{\lambda}\,\delta v\,\Delta t_k.$$
Temporal coherence is $\left|\frac{1}{M}\sum_k e^{\mathrm{i}r_k}\right|$, which
falls only when the $r_k$ *spread* over pairs. A short-baseline network confines
all $r_k$ to a narrow range, so the phasors stay aligned and $\gamma_t$ stays
near 1; a network reaching 2.43 yr spreads $r_k$ over a range four times wider,
and the sum dephases. That is why network A gave 0.9991 and network B 0.9916 for
the same 10% velocity error.

**Number.** With $\delta v = 0.10\times12 = 1.2\ \mathrm{mm\,yr^{-1}}$,
$\Delta t = 2.0$ yr, $\cos\theta = 0.8192$:
$$\delta d = 1.2 \times 2.0 = 2.4\ \mathrm{mm} = 2.4\times10^{-3}\ \mathrm{m}
\ \text{(vertical)},$$
$$\delta d_{\text{LOS}} = 0.8192 \times 2.4 = 1.966\ \mathrm{mm},$$
$$r = \frac{4\pi}{\lambda}\delta d_{\text{LOS}}
= 222.16 \times 1.966\times10^{-3} = 0.437\ \mathrm{rad}.$$

A $0.44\ \mathrm{rad}$ phase spread is comparable to the $0.50\ \mathrm{rad}$
pair noise, so this baseline length is where the diagnostic starts to work —
and it is two to four times longer than anything in a typical small-baseline
subset.

---

## ★6 — Correcting an omitted seasonal term

The demonstration's measured bias for this configuration is
$+0.464\ \mathrm{mm\,yr^{-1}}$. Subtracting it:
$$\hat{v}_{\text{corrected}} = 11.88 - 0.46 = 11.42\ \mathrm{mm\,yr^{-1}}.$$

**Caveat, and this is the point of the exercise:** the bias is a property of the
*record*, not a universal constant. It depends on the seasonal amplitude, its
phase relative to the record ends, and the record length in cycles. Before using
$11.42\ \mathrm{mm\,yr^{-1}}$, the following must be reported:

1. the span of the record in years and in seasonal cycles;
2. the fitted seasonal amplitude and phase, or a statement that the term was
   omitted and the bias estimated from the data;
3. the network's baseline distribution (Section 3.5);
4. the number of dates and the measured false-positive rate if any $D_A$ screen
   was applied;
5. what fixes the absolute level (reference station or assumption).

The honest reduction is therefore not "11.42" but "11.42 mm/yr assuming the
seasonal term is a pure sinusoid of the fitted amplitude; omitting it moves the
answer by $+0.46\ \mathrm{mm\,yr^{-1}}$."

---

## ★7 — Network design for a 0.5 mm/yr trend in vegetated terrain (specification)

**Target.** $0.5\ \mathrm{mm\,yr^{-1}}$ over 3 yr = $1.5\ \mathrm{mm}$ of
cumulative signal, i.e. $0.27$ of a fringe at $\lambda = 5.6565\ \mathrm{cm}$.
The measurement is therefore not fringe counting; it is a fit to a network.

**Baselines.** Must include a few pairs spanning the full 3 yr, because the
lesson measures that velocity information lives in the long baselines: at
$\Delta t = 2$ yr a $0.5\ \mathrm{mm\,yr^{-1}}$ error produces
$0.18\ \mathrm{rad}$, i.e. one third of the pair noise. The rest of the network
should be short baselines to keep coherence high enough to unwrap. Concretely:
a spanning chain of consecutive dates, plus a handful of 1–3 yr pairs.

**Dates.** The $D_A$ measurement sets the floor: at $N = 8$ dates, 3.3% of pure
speckle pixels pass a 0.25 amplitude-dispersion threshold, and at $N = 4$,
15.6% do. For vegetated terrain — where the target population is scarce — a
false-positive rate above a few per cent contaminates the result, so
$N \ge 16$ is the minimum defensible choice, and $N \ge 40$ if the scatterer
density is low.

**Model.** A rate plus an annual sinusoid plus a semiannual term if the span
exceeds about 2.5 yr; plus a step at any known event. Omitting the sinusoid alone
biased the demonstration's rate by $+0.464\ \mathrm{mm\,yr^{-1}}$ — comparable to
the target trend, which makes the seasonal term mandatory rather than optional
at this accuracy.

**Diagnostics to report.** Residual mean and spread per pair (not $\gamma_t$
alone); the network's baseline histogram; the closure-phase test on all
triangles; the $D_A$ distribution with the number of dates and the measured
false-positive rate; the residual velocity scatter between two disjoint halves of
the network, as an internal consistency check.

**What fails first.** Temporal decorrelation in vegetation: it removes the long
baselines, and the long baselines are exactly where the velocity information
lives (Section 3.5). The second failure is the stratified atmosphere, which
correlates with topography and mimics a steady signal. Design accordingly: keep a
topographically flat control area, and expect the long-baseline subset to be the
binding constraint on the achievable precision.

---

## ★8 — Correlated pair errors and the $\sqrt{M}$ law

**Non-zero off-diagonal terms.** Two pairs sharing an acquisition share that
date's screen: for pairs $(i,j)$ and $(i,k)$ the errors share $s_i$; for
$(i,j)$ and $(j,k)$ they share $s_j$; for $(i,j)$ and $(k,l)$ with no common date
they are independent. So the covariance of the observations has non-zero entries
exactly along the incidence structure of the graph, with each shared date
contributing the *differenced* screen.

**Prediction.** With independent errors the estimator's variance falls as
$\sigma^{2}(A^{\mathsf T}A)^{+}$, i.e. the error falls as $M^{-1/2}$. With a
shared screen the effective number of independent observations is limited by the
number of *dates* (each date's screen is a new independent variable), not by the
number of pairs. As the shared component dominates, the error stops falling with
$M$ at all and instead falls as the number of dates, $N^{-1/2}$: the measured
log-log slope against $M$ would flatten toward $0$ once the extra pairs are
redundant combinations of a limited set of screens.

**Control experiment.** Split the network into two disjoint groups of pairs that
share no dates. Estimate the rate from each. Under independent errors the two
estimates differ by the $\sqrt{M}$-scaled noise, so the scatter should fall as
$M$ grows. Under shared-screen dominance the scatter between the two groups does
not shrink when more pairs are added inside each group — it is set by the number
of dates in each group. Comparing the measured scatter against the two
predictions identifies which regime applies, and it is the check that the
independence assumption cannot perform on itself.
