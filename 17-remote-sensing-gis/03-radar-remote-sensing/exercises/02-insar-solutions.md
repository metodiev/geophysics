# Solutions — 17-03-02 InSAR: Interferometric Phase and Deformation Measurement

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [02 InSAR](../02-insar.md).

---

## ★1 — Phase, fringes, wrap

$$\Delta\phi = \frac{4\pi}{\lambda}\Delta r
= 222.16\ \mathrm{rad\,m^{-1}} \times 0.0170\ \mathrm{m}
= 3.7767\ \mathrm{rad}.$$

Fringes:
$$\frac{3.7767}{2\pi} = 0.6011\ \text{fringes}.$$

Wrapped value: $3.7767 > \pi = 3.1416$, so subtract $2\pi$:
$$\mathcal{W}(\phi) = 3.7767 - 6.2832 = -2.5065\ \mathrm{rad}.$$

The unwrapped and wrapped values differ by exactly $2\pi$, and only the second
is measurable.

---

## ★2 — Four displacements with one wrapped phase

$\mathcal{W}(\phi) = -1.40$ rad means $\phi = -1.40 + 2\pi k$, and
$d = \phi\lambda/(4\pi) = \phi/222.16\ \mathrm{m}$:

| $k$ | $\phi$ (rad) | $d$ (cm) | wrapped (rad) |
|---|---|---|---|
| $-1$ | $-7.6832$ | $-3.458$ | $-1.40$ |
| $0$ | $-1.4000$ | $-0.630$ | $-1.40$ |
| $+1$ | $+4.8832$ | $+2.198$ | $-1.40$ |
| $+2$ | $+11.1664$ | $+5.026$ | $-1.40$ |

The candidates are separated by exactly
$$\frac{\lambda}{2} = \frac{5.6565}{2} = 2.8282\ \mathrm{cm},$$
so a single wrapped phase admits an arithmetic progression of displacements
extending to $\pm\infty$, with a sign ambiguity as well.

---

## ★3 — Ambiguity height versus baseline

$$h_a = \frac{\lambda R}{2B_{\perp}\sin\theta}
= \frac{0.056565 \times 8.0\times10^{5}}{2B_{\perp} \times 0.5736}
= \frac{3.9447\times10^{4}}{B_{\perp}}\ \mathrm{m}.$$

For $B_{\perp} = 50\ \mathrm{m}$:
$$h_a = \frac{3.9447\times10^{4}}{50} = 789.0\ \mathrm{m}.$$

For $B_{\perp} = 150\ \mathrm{m}$:
$$h_a = \frac{3.9447\times10^{4}}{150} = 263.0\ \mathrm{m}.$$

**Effect of a growing baseline:** $h_a$ falls as $1/B_{\perp}$, so a three-fold
baseline increase triples the fringe density over a fixed relief. That is the
central trade of topographic InSAR: a long baseline is sensitive (good for
height resolution) but decorrelates (Section 3.8 of the lesson) and produces
fringes so dense that unwrapping fails. Short baselines are robust and blunt.

---

## ★4 — Why the perpendicular convention differs by $1/\sin^{2}\theta$

A displacement $\mathrm{d}s$ along $\hat{n} = (\cos\theta, \sin\theta)$ — the
direction perpendicular to the line of sight $\hat{u} = (\sin\theta,
-\cos\theta)$ — has a vertical component

$$\mathrm{d}h = \hat{n}\cdot(0,1)\,\mathrm{d}s = \sin\theta\,\mathrm{d}s.$$

The phase change is proportional to $\mathrm{d}s$ through
$\mathrm{d}\phi = (4\pi/\lambda)(B_{\perp}/R)\mathrm{d}s$, so per unit *vertical*
change

$$\frac{\mathrm{d}\phi}{\mathrm{d}h}
= \frac{4\pi}{\lambda}\frac{B_{\perp}}{R}\frac{1}{\sin\theta},$$

against the true vertical sensitivity $(4\pi/\lambda)B_{\perp}\sin\theta/R$. The
ratio is

$$\frac{1}{\sin^{2}\theta} = \frac{1}{0.5736^{2}} = 3.039
\quad \text{at } 35^\circ.$$

**Trigonometric reason:** the perpendicular direction is tilted from the
horizontal by $\theta$ toward the vertical, so its vertical component is
$\sin\theta$. At shallow incidence ($\theta$ large, $\sin\theta \to 1$) the two
conventions coincide; as the look approaches nadir ($\theta \to 0$) the
perpendicular motion becomes purely horizontal, its vertical component vanishes,
and the ratio $1/\sin^{2}\theta$ diverges. A vertical displacement at nadir
produces no phase at all, which is the physically correct limit — and it is why
the perpendicular form must never be used for relief.

---

## ★5 — A coherence threshold cannot ignore the look count

From the lesson's bias table, for a true coherence of 0.20:

| looks | expected $\hat{\gamma}$ | passes $\hat{\gamma} > 0.30$? |
|---|---|---|
| 4 | 0.4810 | yes |
| 64 | 0.2203 | no |

So **the same threshold selects different pixels** at different look counts. At
$L = 4$ essentially all of this low-coherence terrain survives the mask; at
$L = 64$ the terrain is rejected although its true coherence is identical. At
$L = 1$ everything passes, because the estimator is identically 1.

**Practical consequence:** a mask "$\hat{\gamma} > 0.30$" means different things
in different products. Either fix the look count and quote it with the
threshold, or compare against the look-dependent expectation
$\mathbb{E}[\hat{\gamma}\,|\,\gamma,L]$ and threshold the *true* coherence
inferred from it. Reporting the threshold alone is not a reproducible
criterion.

---

## ★6 — Aliasing threshold for a subsidence gradient

Unambiguous unwrapping requires the phase difference between adjacent pixels to
stay below $\pi$:

$$|\Delta\phi| = \frac{4\pi}{\lambda}\,\delta d < \pi
\;\Longrightarrow\;
\delta d < \frac{\lambda}{4} = \frac{5.6565}{4} = 1.4141\ \mathrm{cm}$$

per pixel of LOS change. Over a $20\ \mathrm{m}$ pixel the gradient limit is

$$\frac{0.014141\ \mathrm{m}}{20\ \mathrm{m}} = 7.07\times10^{-4}
= 0.707\ \mathrm{mm\,m^{-1}}.$$

**The bowl:** $6\ \mathrm{cm}$ over $400\ \mathrm{m}$ is an average gradient of
$6\times10^{-2}/400 = 1.5\times10^{-4} = 0.15\ \mathrm{mm\,m^{-1}}$; if the
profile is parabolic the maximum gradient is twice the average,
$0.30\ \mathrm{mm\,m^{-1}}$. Both are below $0.707\ \mathrm{mm\,m^{-1}}$, so the
bowl unwraps — with a margin of about a factor of two at the steepest point.
The margin is what matters, not the average: a bowl twice as steep would alias
at its rim, and the residual would be a closed loop of residues around the
subsidence centre.

---

## ★7 — Deformation, atmosphere or orbit (specification)

**Additional data.** (i) A time series of many acquisitions over the same area,
not one pair. (ii) An independent deformation measurement where available — a
continuous GNSS station inside the scene. (iii) A numerical weather model field
and/or a global atmospheric reanalysis for the acquisition times. (iv) The
precise orbit determination solution and its formal uncertainty.

**Diagnostics and signatures.**

| hypothesis | diagnostic | signature |
|---|---|---|
| deformation | temporal evolution in the stack | rate is steady or physically smooth (elastic decay, seasonal cycle); a GNSS station at the location agrees in trend |
| stratified atmosphere | correlation of phase with topography | phase is a smooth function of elevation, and repeats between independent dates with the same weather; does not accumulate linearly in time |
| turbulent atmosphere | spatial structure function of the phase | power-law structure function with no topographic correlation, decorrelating over a few kilometres; appears as a screen redrawn each date |
| orbit error | phase gradient across the whole scene | a linear (or low-order polynomial) ramp in range and azimuth, present in every pair sharing the same orbit solution, with an amplitude that produces no discontinuity at the scene edge but a step at the edge of the *sub*-swath |

**Reported uncertainty.** After correction, quote: the residual standard
deviation of the model fit to the screen, the uncertainty of the fitted ramp
coefficients, and the propagation of both into the velocity estimate. For a
single pair, state the conservative bound as the RMS of the uncorrected
stratified term, and mark the result as unverified until a stack exists.

---

## ★8 — Where the asymptotic phase-precision formula errs

**Prediction.** At $\gamma = 0.3$, $L = 1$:
$$\sigma_\phi = \sqrt{\frac{1-0.09}{2\times1\times0.09}} = \sqrt{5.0556}
= 2.2485\ \mathrm{rad}.$$

**Measurement.** 1.5665 rad (lesson table), i.e. *smaller*, not larger.

**Mechanism.** The wrapped phase is confined to $(-\pi,\pi]$; a phase that
carries no information is uniform there, with
$\sigma_\phi = \pi/\sqrt{3} = 1.8138\ \mathrm{rad}$. The asymptotic formula is
derived from a small-perturbation (Gaussian) model of the phase around its mean
value, which requires the phase distribution to be narrow compared with the
wrap interval. When $2L\gamma^{2} \ll 1$ the distribution is broad and wraps,
the Gaussian model is invalid, and the formula returns values larger than any
wrapped phase can achieve — 2.2485 rad > 1.8138 rad is the visible symptom.

**Criterion for use.** Require *both*:
1. the formula's prediction to be well below the uniform limit, say
   $\sigma_\phi < 0.5\ \mathrm{rad}$, which for this relation means
   $2L\gamma^{2} > (1-\gamma^{2})/0.25 \approx 4$;
2. an independent check on a control region — simulate or measure the phase
   spread for the actual $L$ and a coherence matched to the data, and confirm
   the formula reproduces it.

When these fail, report the coherence and the look count and state that the
phase is not quantifiable from that stack, rather than quoting an error bar the
distribution cannot support.
