# Solutions — 16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [04 Natural Variability](../04-natural-variability.md).

---

## ★1 — Decorrelation times and effective sample size

$$\tau = -\frac{1}{\ln\phi},\qquad
n_\text{eff} = n\frac{1-\phi}{1+\phi}.$$

- $\phi = 0.3$: $\tau = -1/\ln 0.3 = 1/1.20397 = 0.831$ yr;
  $n_\text{eff} = 50(0.7)/(1.3) = 26.9$.
- $\phi = 0.7$: $\tau = -1/\ln 0.7 = 1/0.356675 = 2.80$ yr;
  $n_\text{eff} = 50(0.3)/(1.7) = 8.8$.

**The $\phi = 0.3$ record carries more independent information** — about 27
independent samples against about 9 — even though both records are 50 years
long. Record length and information content are different quantities.

---

## ★2 — Attenuation and lag

$$\tau = \frac{C}{|\lambda|} = \frac{2.0423\times10^8}{5.418\times3.156\times10^7}
= 1.195\ \mathrm{yr}.$$

**T = 5 yr:** $\omega = 2\pi/5 = 1.25664\ \mathrm{yr^{-1}}$,
$\omega\tau = 1.5017$;

$$\text{attenuation} = \frac{1}{\sqrt{1+1.5017^2}} = 0.5547,\qquad
\varphi = \frac{\arctan(1.5017)}{1.25664} = \frac{0.98337}{1.25664}
= 0.783\ \mathrm{yr}.$$

**T = 11 yr:** $\omega = 0.57120\ \mathrm{yr^{-1}}$, $\omega\tau = 0.68254$;

$$\text{attenuation} = \frac{1}{\sqrt{1+0.46586}} = 0.8259,\qquad
\varphi = \frac{\arctan(0.68254)}{0.57120} = \frac{0.59864}{0.57120}
= 1.048\ \mathrm{yr}.$$

**The 5-year period is attenuated more** (0.555 against 0.826) because the slab
has 1.195 years of memory: the faster the forcing oscillates relative to $\tau$,
the less the temperature can follow it. Note the asymmetry in the lag: the
11-year forcing is *more* strongly delayed in absolute time even though it is
attenuated less, because the lag approaches a quarter period as $\omega\tau$
falls below 1.

---

## ★3 — The white-noise threshold

$$\sum_{k=0}^{n-1}\left(k-\frac{n-1}{2}\right)^2
= \frac{n(n^2-1)}{12} = \frac{50(2500-1)}{12} = 10412.5 .$$

Threshold: $2/\sqrt{10412.5} = 2/102.04 = 0.0196$ per year for a unit-variance
series.

**Cross-check.** $n(n^2-1)/12$ is the standard sum; for $n = 40$ it gives
$5330$ and a threshold of 0.0274, matching the lesson. ✔

---

## ★4 — An approximate threshold

$$\phi = 0.4,\ n = 60:\quad
n_\text{eff} = 60\frac{0.6}{1.4} = 25.7 .$$

Variance-inflation factor:

$$\sqrt{\frac{1+\phi}{1-\phi}} = \sqrt{\frac{1.4}{0.6}} = 1.528 .$$

White-noise threshold:
$\sum = 60(3600-1)/12 = 17995$, so $2/\sqrt{17995} = 0.0149$. Approximate
threshold: $1.528\times0.0149 = 0.0228$ per year.

**Conservative or anticonservative?** The lesson's worked case ($n=40$,
$\phi = 0.6$) gave an inflation of 2.00 against a Monte Carlo value of 1.74, so
the rule of thumb **overestimates** the threshold — it is conservative, and it
costs detectability. The reason is that the inflation factor $(1+\phi)/(1-\phi)$
is an asymptotic ($n\to\infty$) result, and short records with strong
persistence have a smaller effective inflation.

---

## ★5 — Why a short-memory mode cannot build a trend

**(a)** Forcing duration / mode memory $= 5\ \mathrm{yr}/10\ \mathrm{d}
= 1825/10 = 182.5$ (using 365-day years).

**(b)** Lag-1 daily autocorrelation $= \exp(-1/10) = 0.9048$; at 365 days,
$\exp(-36.5) = 1.4\times10^{-16}$ — numerically zero.

**(c)** The mode's autocorrelation decays to zero within a few weeks, so the
successive anomalies that a multi-year forcing would need to accumulate are
statistically unrelated to each other: **the mode forgets the forcing before the
forcing can accumulate.** Only a mode whose memory is comparable to the forcing
duration — an ocean basin, a delayed feedback — can integrate it.

---

## ★6 — Scaling a pulse response

Linear scaling from $-2.0$ to $-3.0\ \mathrm{W\,m^{-2}}$ gives

$$\text{peak} \approx -0.1511\times\frac{3.0}{2.0} = -0.2267\ \mathrm{K}.$$

**Why it is not exact.** The peak time and the recovery time depend on the
forcing's *decay time*, which has changed from 1.5 yr to 1.0 yr, not just on its
amplitude. The slab's response is a convolution of the forcing with its own
exponential response, so changing the shape of the forcing changes the peak
time and hence the value at the peak. The linear-scaling estimate is exact only
if the forcing's time profile is unchanged — which is the check to state.

---

## ★7 — Multiple testing

**(a)** $12\times8 = 96$ tests; Bonferroni per-test level
$= 0.05/96 = 5.21\times10^{-4}$.

**(b)** If the 96 tests were independent at the nominal 5% level, the
probability of at least one false positive would be

$$1 - 0.95^{96} = 1 - 0.00724 = 0.993,$$

i.e. essentially certain.

**(c)** The tests are not independent for two reasons: (i) nearby lags sample
overlapping data, so their correlations are themselves correlated; and (ii)
neighbouring regions share large-scale variability. Dependence makes the
*effective* number of tests smaller than 96, so (b) is too pessimistic — but it
remains far above 5%, and the correct correction must be computed by a
maximum-statistic Monte Carlo that preserves the observed dependence, not by
Bonferroni. Bonferroni is a valid but conservative bound.

---

## ★8 — Measuring a transfer function (specification)

**Design.** Drive the slab with a sinusoid of fixed amplitude
$F_0 = 0.5\ \mathrm{W\,m^{-2}}$ at a set of periods
$T \in \{1, 2, 5, 11, 30\}$ yr, for each of three capacities
$C\in\{1\times10^8, 2.04\times10^8, 6\times10^8\}$ J m⁻² K⁻¹ (all with the same
$|\lambda|$, so $\tau = C/|\lambda|$ takes three known values). Integrate for at
least 10 periods and fit $a\sin\omega t + b\cos\omega t$ to the final portion.

**Diagnostics and axes.** Plot (i) the response amplitude divided by the
equilibrium response $F_0/|\lambda|$ against the dimensionless product
$\omega\tau$ and (ii) the phase lag divided by the period against $\omega\tau$,
both on logarithmic abscissae. Overlay the analytic curves
$1/\sqrt{1+(\omega\tau)^2}$ and $\arctan(\omega\tau)/(2\pi)$ in units of period.

**Result showing the transfer function depends only on $\omega\tau$.** The
nine points from the three capacities and five periods must **collapse onto a
single curve** when plotted against $\omega\tau$ rather than against $\omega$ or
$\tau$ separately. A collapse is the signature of a one-parameter scaling; if
the points separate by capacity at fixed $\omega\tau$, then the response depends
on $C$ and $|\lambda|$ separately and the simple slab picture is inadequate.
That is the falsifiable content of the design.
