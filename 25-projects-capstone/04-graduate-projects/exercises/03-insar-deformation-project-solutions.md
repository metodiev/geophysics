# Solutions — 25-04-03 Project: InSAR Deformation Time Series Analysis

> Read after attempting. Lesson:
> [03 InSAR Time Series](../03-insar-deformation-project.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/insar_timeseries_demo.py`](../code/insar_timeseries_demo.py).

---

## ★1 — The design matrix

$$d(t) = \underbrace{a}_{\text{offset}} + \underbrace{b\,t}_{\text{rate}}
+ \underbrace{c\cos 2\pi t + e\sin 2\pi t}_{\text{annual season}}
+ \underbrace{f\,H(t-t_s)}_{\text{step}},$$

in matrix form with columns $[\,1,\ t,\ \cos 2\pi t,\ \sin 2\pi t,\ H(t-t_s)\,]$.

- $b$ is the **deformation rate**, in mm yr⁻¹.
- $f$ is the **step**, in mm; its sign is the displacement at $t_s$ relative to the
  pre-step level.
- $a$ is an offset that absorbs the reference point's position; it is not a
  physical quantity.
- $c$ and $e$ are the seasonal amplitudes; their units are mm and their phase is
  $\arctan(e/c)$.

---

## ★2 — The seasonal omission

$$\text{bias} = 10.3834 - 12.0207 = -1.6373\ \mathrm{mm\,yr^{-1}},$$

$$\frac{1.6373}{1.2355} = 1.33
\quad\text{times the correct model's error bar}.$$

The bias is **larger than the uncertainty**, so the rate-only model is not
"consistent with" the correct one: it is wrong by more than its own precision.

**Why the misfit does not diagnose it.** The omitted term is a *smooth* function
over the record, so it is partly absorbed by the rate and the offset; what remains
in the residuals is a gentle annual wiggle of 2–3 mm against a 3 mm noise level,
and the rms only rises from $2.5760$ to $5.9276$ — a factor of 2.3, which a longer
or noisier series would not show at all. A missing term is best detected by
**looking at the residuals as a function of epoch** (a seasonal pattern is
unmistakable there) rather than by comparing a single rms number, and by comparing
candidate models with an information criterion rather than by an rms threshold.

---

## ★3 — The step

$$\frac{10.0 - 7.1133}{4.7237} = 0.61\sigma,$$

so the recovered step is consistent with the truth — but only because the
uncertainty is huge.

**Two reasons the uncertainty is large.**

1. **The step is supported by a short, one-sided baseline.** With $t_s =
   1.95\ \mathrm{yr}$ in a $2.95\ \mathrm{yr}$ record, only the last third of the
   epochs constrain it, and they also constrain the rate and the season, so the step
   trades against them.
2. **The rate and the step are correlated.** A step and a change in trend produce
   similar signatures over a short window; the covariance between $b$ and $f$ is
   strongly negative, which is why the *full* model's rate uncertainty
   ($2.6921$) is larger than the step-omitting model's ($1.6209$) — adding a
   parameter inflates the correlated ones.

A step whose uncertainty is comparable to its size is a step that the record cannot
confirm; the defensible statement is the pair (rate, step) with their covariance,
not a step value.

---

## ★★4 — Comparing the two omissions

$$\text{step omission bias} = 16.7561 - 13.2905 = +3.4656\ \mathrm{mm\,yr^{-1}}
= 28.9\%\ \text{of the true } 12.0\ \mathrm{mm\,yr^{-1}}.$$

$$\text{season omission bias} = -1.6373\ \mathrm{mm\,yr^{-1}}
= 13.6\%\ \text{of the true rate}.$$

**The step omission is the more dangerous**, for two reasons. It is twice as large
in absolute terms, and it is in the *opposite* direction from the season's bias —
so a study that omits both does not have a compensating error. It is also the
omission that is easier to miss: a step in a 3-year record looks like an
acceleration, which is itself a plausible geophysical signal, whereas an annual
cycle in a fixed-phase series at least repeats.

---

## ★★5 — The early-window apparent rate

The signal is $d(t) = 12t - 15e^{-t/0.3}$ mm, so its total change over
$[0, 1]\ \mathrm{yr}$ is

$$d(1) - d(0) = \left(12 - 15e^{-3.333}\right) - \left(0 - 15\right)
= (12 - 0.5353) + 15 = 26.465\ \mathrm{mm},$$

giving a **mean rate over the window of $26.465\ \mathrm{mm\,yr^{-1}}$**.

The fitted value is $23.0487 \pm 7.8911\ \mathrm{mm\,yr^{-1}}$, which is
$0.43\sigma$ from the analytic mean — consistent, and the large uncertainty is
itself the warning: the least-squares rate over that window is the *average slope*,
not the transient's amplitude or its time constant. The window's mean rate is not
the asymptotic rate, and the fit faithfully returns the former.

Note what this means in practice: a study that reports a "deformation rate" from a
window containing a decaying transient reports a number between the transient's
initial rate and the long-term rate, whichever the window happens to weight most.

---

## ★★6 — The colleague's error bar

$$14.2\ \mathrm{mm\,yr^{-1}}\ \text{against a true } 12.0
\qquad\Longrightarrow\qquad \text{bias } +2.2\ \mathrm{mm\,yr^{-1}}.$$

The quoted formal error of $\pm 0.3\ \mathrm{mm\,yr^{-1}}$ is the least-squares
error of the *rate* coefficient, and it is too small for two independent reasons.

1. **The model is wrong.** The window excludes the first $0.25\ \mathrm{yr}$ but
   still contains part of the transient: at $t = 0.25$ the transient is
   $-15e^{-0.833} = -6.5\ \mathrm{mm}$, decaying to $-0.08\ \mathrm{mm}$ by
   $t = 1.5$. Over the window that is a curvature the linear model must absorb into
   its slope, contributing a bias of about $+2.2\ \mathrm{mm\,yr^{-1}}$. The
   formal error describes the noise on a linear model, not the model's
   inadequacy.
2. **The epochs are correlated.** Atmospheric delay and orbit error are
   temporally correlated, so the effective number of independent epochs is smaller
   than the count and the true error is larger than the formal one — the
   demonstration's own least-squares sigma of $1.6\ \mathrm{mm\,yr^{-1}}$ over the
   same window (with a correctly specified model) already exceeds the quoted 0.3.

**The honest uncertainty.** The demonstration's identical fit gives
$14.2215 \pm 1.6153\ \mathrm{mm\,yr^{-1}}$; with correlated errors the uncertainty
is larger still, and with the model misspecification the appropriate statement is a
rate of about $14\ \mathrm{mm\,yr^{-1}}$ with a systematic term of order
$2\ \mathrm{mm\,yr^{-1}}$ — that is, the *bias* dominates the *precision*, and the
reportable uncertainty is of order $2$–$3\ \mathrm{mm\,yr^{-1}}$, not $0.3$.

---

## ★★★7 — A time-series model for a coastal-aquifer subsidence study

**Functional forms.**

| term | form | parameters |
|---|---|---|
| offset | $a$ | 1 |
| linear trend | $b\,t$ | 1 |
| seasonal cycle (groundwater) | $c\cos 2\pi t + e\sin 2\pi t$ (+ optionally one harmonic) | 2–4 |
| coseismic step | $f\,H(t - t_s)$, $t_s$ known from the catalogue | 1 (2 if $t_s$ is fitted) |
| decelerating compaction | $g\left(1 - e^{-t/\tau}\right)$ | 2 ($g$, $\tau$) |

Total: 7–9 parameters; with 60–120 epochs the problem is well over-determined, and
the parameters are the *model*, not a convenience.

**Choosing between forms objectively.**

1. **Residual structure**, not rms: plot residuals against epoch and against the
   fitted seasonal phase; a surviving seasonal pattern or a curvature indicates a
   missing term.
2. **Information criteria** ($\mathrm{AIC}_c$ or BIC) computed on the *same* data
   with the same weight matrix, comparing nested and non-nested candidates; a term
   earns its place only if the criterion improves.
3. **Cross-validation in time**: fit on the first $70\%$ of epochs and predict the
   last $30\%$; a model with a spurious term predicts worse out of sample even
   when it fits better in sample.
4. **Parameter significance with the correlated covariance**, not the formal one: a
   transient whose $\tau$ is uncertain by more than its own value is not
   constrained by the data.

**Observation span needed.** The exponential's time constant $\tau$ is constrained
only by epochs spanning several $\tau$: with a 1-year $\tau$ and a 3-year record,
the amplitude is determined but the decay is not (the exponential is nearly linear
over the record), and the model degenerates into the linear trend. The span should
be **at least 3–5$\tau$** for the transient's shape to be identifiable, which for
slow compaction means a decade of observations.

**The over-parameterisation test.** The decisive test is **out-of-sample
prediction**: withhold the final 20–30% of epochs, fit on the rest, and compare the
predicted and observed displacements over the withheld period. A model that is
over-parameterised fits the training epochs well and predicts the withheld ones
poorly; the ratio of prediction rms to training rms is the diagnostic, and it should
be close to 1 for a correctly specified model with uncorrelated errors. A second,
cheaper check is parameter correlation: if the fitted (rate, transient amplitude,
transient time constant) are correlated above about $0.9$, the data do not
separate them and at most one should be reported.
