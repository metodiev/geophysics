# Solutions — 13-04-03 Postseismic Relaxation and Viscoelastic Models

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Postseismic Relaxation and Viscoelastic Models](../03-postseismic-viscoelastic.md).

---

## ★1 — Maxwell times

$\mu_e = 3\times10^{10}\ \mathrm{Pa}$; use $1\ \mathrm{yr} =
3.1558\times10^{7}\ \mathrm{s}$.

| $\eta$ (Pa s) | $\tau$ (s) | $\tau$ (yr) |
|---|---|---|
| $3\times10^{19}$ | $1.0\times10^{9}$ | $32.0$ |
| $10^{20}$ | $3.333\times10^{9}$ | $105.6$ |
| $3\times10^{20}$ | $1.0\times10^{10}$ | $316.9$ |

Check: $\eta/\mu_e = 10^{20}/3\times10^{10} = 3.333\times10^{9}$ s, and
$3.333\times10^{9}/3.1558\times10^{7} = 105.6$ yr ✔.

---

## ★2 — Derivation

With $\dot e = 0$:

$$
0 = \frac{\dot\sigma}{2\mu_e} + \frac{\sigma}{2\eta}
\;\;\Longrightarrow\;\;
\dot\sigma = -\frac{\mu_e}{\eta}\sigma
\;\;\Longrightarrow\;\;
\sigma(t) = \sigma_0 e^{-\mu_e t/\eta},
$$

so $\tau = \eta/\mu_e$. Since $\sigma_0$ appears only as a multiplicative
prefactor and has been divided out, the decay constant does not depend on it:
a stress of $1\ \mathrm{MPa}$ and one of $100\ \mathrm{MPa}$ relax with the same
$\tau$. That is the property that makes a relaxation time a material parameter.

---

## ★3 — Three points on the curve

$D(t) = 0.25 - 0.15e^{-t/12}$ m.

- $t = 0$: $D = 0.25-0.15 = 0.10\ \mathrm{m}$ (the immediate coseismic offset);
- $t = 12\ \mathrm{yr}$: $e^{-1} = 0.3679$, $D = 0.25-0.0552 =
  0.1948\ \mathrm{m}$;
- $t = 60\ \mathrm{yr}$: $e^{-5} = 0.00674$, $D = 0.25-0.00101 =
  0.2490\ \mathrm{m}$.

Fraction of the $0.15\ \mathrm{m}$ transient completed:
$0\%$ at $t=0$, $1-0.3679 = 63.2\%$ at $t=\tau$, and
$1-0.00674 = 99.3\%$ at $t = 5\tau$. **A five-$\tau$ window is needed to see the
flattening**, which is why Section 3 of the lesson insists on a few $\tau$.

---

## ★4 — Rates and the half-life

$\dot D = (0.15/12)e^{-t/12} = 0.0125e^{-t/12}\ \mathrm{m\,yr^{-1}}
= 12.5e^{-t/12}\ \mathrm{mm\,yr^{-1}}$.

- $t = 1\ \mathrm{yr}$: $12.5\times0.9200 = 11.50\ \mathrm{mm\,yr^{-1}}$;
- $t = 12\ \mathrm{yr}$: $12.5e^{-1} = 4.60\ \mathrm{mm\,yr^{-1}}$;
- $t = 60\ \mathrm{yr}$: $12.5e^{-5} = 0.084\ \mathrm{mm\,yr^{-1}}$.

Half-life: $t_{1/2} = \tau\ln 2 = 12\times0.6931 = 8.32\ \mathrm{yr}$.
Check: $12.5/2 = 6.25$; from $t=1$ to $t = 1+8.32 = 9.32$:
$12.5e^{-9.32/12} = 12.5\times0.4590 = 5.74$. The ratio is $11.50/5.74 =
2.00$ ✔ — the rate halves, but the halving is measured from wherever you start.

Rate below $0.5\ \mathrm{mm\,yr^{-1}}$:
$12.5e^{-t/12} = 0.5 \Rightarrow e^{-t/12} = 0.04 \Rightarrow
t = 12\ln 25 = 12\times3.219 = 38.6\ \mathrm{yr}$.

---

## ★5 — Window required for $\pm15\%$

The demonstration's short window ($1.5\ \mathrm{yr}$, i.e. $0.14\tau$) gave a
$\Delta\chi^{2}=1$ range of $13.4$–$23.6\ \mathrm{yr}$ around a best fit of
$15.4\ \mathrm{yr}$, while the true $\tau$ was $10.56\ \mathrm{yr}$. Measured
relative to the truth, that range is $+27\%$ to $+124\%$: not merely wider than
the $\pm15\%$ target, but *displaced*, so the target is unattainable at that
window however the data are weighted.

From the full window ($30\ \mathrm{yr} \approx 2.8\tau$) the range was
$10.30$–$10.60\ \mathrm{yr}$, i.e. $\pm1.4\%$. Interpolating, a target of
$\pm15\%$ is reached somewhere between $1.5\tau$ and $2\tau$ of observation,
i.e. a window of roughly $20\ \mathrm{yr}$ for a $\tau$ of about $10\
\mathrm{yr}$.

**The assumption in the extrapolation** is that the noise level and sampling
pattern are unchanged. A different noise level moves the whole curve: the
$\tau$ uncertainty scales roughly as the noise-to-signal ratio, so a campaign
with $1\ \mathrm{mm}$ noise instead of $3\ \mathrm{mm}$ reaches the same
precision in a shorter window. State both numbers or the estimate is not
transferable.

---

## ★6 — Two modes, one fitted decay constant

$D(t) = 0.09(1-e^{-t/10}) + 0.06(1-e^{-t/50})$.

| $t$ (yr) | mode 1 (m) | mode 2 (m) | total (m) |
|---|---|---|---|
| 5 | $0.09(1-0.6065) = 0.0354$ | $0.06(1-0.9048) = 0.0057$ | 0.0411 |
| 20 | $0.09(1-0.1353) = 0.0778$ | $0.06(1-0.6703) = 0.0198$ | 0.0976 |
| 100 | $0.09(1-4.5\times10^{-5}) = 0.0900$ | $0.06(1-0.1353) = 0.0519$ | 0.1419 |

A single exponential fitted over $0$–$100\ \mathrm{yr}$ would see an initial
fast rise dominated by mode 1 (63% of the total amplitude) plus a persistent slow
rise from mode 2. The slow mode contributes only $0.052$ of its $0.060\
\mathrm{m}$ by $100\ \mathrm{yr}$, so the fitted curve must split the difference:
expect $\tau_{\text{fit}}$ between the two, closer to $10\ \mathrm{yr}$ than
$50$ because the fast mode carries more amplitude, but with a substantial
**apparent** asymptote deficit that a single-exponential fit will absorb into
$D_\infty$.

**The lesson's measured case** is the calibration for this argument: two modes
at $10.56$ and $52.81\ \mathrm{yr}$ with weights $0.6/0.4$ returned
$\tau = 13.04\ \mathrm{yr}$ with a $0.28\ \mathrm{mm}$ residual. The fitted value
is $23\%$ above the fast mode and $75\%$ below the slow one — which is exactly
the "in between" answer this estimate predicts.

---

## ★7 — Why the residual does not validate $\eta$

1. **The window is far shorter than $\tau$.** $20\ \mathrm{yr}$ against a claimed
   $\tau = 106\ \mathrm{yr}$ is $0.19\tau$. From Section 3 of the lesson, a
   window of that length cannot determine $\tau$: the accepted range in the
   demonstration's scaled experiment was a factor of $1.8$ wide at $0.14\tau$.
   The reported $\eta$ is therefore a lower bound presented as a measurement.
2. **A two-parameter fit to a nearly linear signal can be excellent and
   meaningless.** With only $0.19\tau$ of the transient observed, $\tau$ and the
   amplitude are almost perfectly anti-correlated; the small residual simply
   confirms that *some* pair of numbers fits, not that the pair is right. The
   demonstration's fixed-$\tau$ table makes this explicit: over the short window,
   $\tau = 3\ \mathrm{yr}$ and $\tau = 40\ \mathrm{yr}$ both give acceptable
   $\chi^{2}$ once the amplitude is re-optimised.

**A measurement that would help:** the *spatial* pattern of the transient. A
viscoelastic relaxation with $\tau = 106\ \mathrm{yr}$ has a nearly
time-independent shape over $20\ \mathrm{yr}$ (it is in the near-linear regime);
if the observed pattern migrates or rotates with time, the relaxation is not the
explanation. Alternatively, an independent constraint on the layer thickness
(e.g. from the depth extent of seismicity or from heat flow) fixes which layer
$\tau$ belongs to, converting an ambiguous $\tau$ into a testable $\eta$.

---

## ★8 — One viscosity or two? (specification)

**Synthetic data generator.** A layered forward model (elastic upper crust over
two viscoelastic layers with viscosities $\eta_1$, $\eta_2$ and thicknesses
$h_1$, $h_2$) driven by a prescribed coseismic slip distribution. Output: surface
displacement time series at $N$ sites over a window of $T$ years. Three cases:
(i) $\eta_2/\eta_1 = 1$ (single layer); (ii) ratio $5$; (iii) ratio $50$.

**Forward models.** Model A: one $\tau$ and one amplitude (two parameters).
Model B: two $\tau$'s and two amplitudes plus a split depth (five parameters).
Both fitted to the same synthetic data.

**Noise model.** $3\ \mathrm{mm}$ per epoch per component, plus $1\ \mathrm{mm}$
of spatially correlated common-mode error, sampled at $20$ epochs with
realistic clustering (dense early, sparse late).

**Model-selection metric.** $\chi^{2}$ per degree of freedom, plus an
information criterion that penalises parameters (BIC is the safer choice here
because the models are not nested in a simple way). Report the layer-ratio at
which the two models' BIC difference falls below $2$ — that is the
indistinguishability threshold.

**Expected threshold.** Based on the lesson, a ratio of $1$ is trivially
indistinguishable and a ratio of $5$ is already only marginally detectable over a
$1$–$2\tau$ window; the threshold should fall near a ratio of $3$–$10$ unless the
window exceeds several $\tau$. **A result that showed detectability down to a
ratio of $1.2$ would falsify the expectation** and would point to the second mode
being constrained by something other than the decay — most likely the spatial
pattern of the displacement, which the specification deliberately includes.

---

## ★9 — Three transient mechanisms

| mechanism | timescale controlled by | expected spatial signature |
|---|---|---|
| poroelastic rebound | hydraulic diffusivity $D$ and the drainage length $L$: $t \sim L^{2}/D$ (days–months) | confined to the near field, lobes reversed relative to the coseismic pattern, no far-field signal |
| afterslip | frictional properties and the stress change on the rupture plane; often logarithmic in time | on and downdip of the rupture plane; pattern geometrically similar to coseismic slip but without the same depth distribution |
| viscoelastic relaxation | $\tau = \eta/\mu_e$ (years–decades) | broad, spreading into the deep crust; the *shape* of the surface pattern evolves with time |

**Why one exponential over a sum of three is misleading.** The three mechanisms
have amplitudes in ratios that depend on the event and the rheology, and four or
more parameters (three amplitudes, one or more timescales) fitted to a single
displacement-time series will always find a combination with a small residual,
because the basis functions are highly correlated over a limited window. The
fitted $\tau$ is then a weighted average of physically unrelated timescales —
one of which is not even a relaxation time (the poroelastic one is diffusive).
The residual is small precisely *because* the fit has enough freedom to absorb
the mixture, so a good fit is evidence of flexibility, not of the mechanism. The
only reliable separation uses the spatial signature, which is where the three
mechanisms genuinely differ.
