# Solutions — 23-02-04 Active-Source Fieldwork: Sources, Spreads, Shooting Patterns

> Read after attempting. Lesson:
> [04 Active-Source Fieldwork](../04-active-source-fieldwork.md). All values are
> **SYNTHETIC**.

---

## ★1 — Fold of a split spread

$$F = \frac{n\,\Delta x}{2\,\Delta s} .$$

$\Delta s = 25\ \mathrm{m}$:

$$F = \frac{72 \times 12.5}{2 \times 25} = \frac{900}{50} = 18.00 .$$

$\Delta s = 50\ \mathrm{m}$:

$$F = \frac{72 \times 12.5}{100} = \frac{900}{100} = 9.00 .$$

Units: the fold is a *count* — traces per midpoint bin — and is dimensionless.
Doubling the shot interval halves the fold, exactly, at unchanged receiver
geometry. Both values describe the fully covered centre of the line; the ends ramp
down to zero over about half the spread length.

---

## ★2 — Data volume

Traces:

$$N_{\text{traces}} = 500 \text{ shots} \times 144\ \text{traces/shot}
= 72\,000 \text{ traces}.$$

Volume:

$$V = 72\,000 \times 3000\ \text{samples} \times 4\ \mathrm{bytes}
= 8.64\times10^{8}\ \mathrm{B} = 864\ \mathrm{MB}.$$

This is the raw volume with no headers and no redundancy. At 2000 samples
instead of 3000 it would be 576 MB; the recording length is a direct cost and
should be set from the target depth, not by default. For a 20-line survey the raw
volume is about 17 GB, and every processing pass that reads the whole volume costs
that much I/O again — which is why the volume belongs in the plan.

---

## ★★3 — Correlated stacking at $M = 24$, $\rho = 0.02$

$$\operatorname{Var} = \frac{1 + (M-1)\rho}{M} = \frac{1 + 23 \times 0.02}{24}
= \frac{1.46}{24} = 0.060833 .$$

Achieved gain:

$$G = \frac{1}{\sqrt{\operatorname{Var}}} = \frac{1}{0.24665} = 4.054 .$$

Effective stack count:

$$M_{\text{eff}} = \frac{1}{\operatorname{Var}} = \frac{1}{0.060833} = 16.44 .$$

Loss relative to the uncorrelated case ($\sqrt{24} = 4.899$):

$$20\log_{10}\!\left(\frac{4.054}{4.899}\right)
= 20\log_{10}(0.8275) = -1.644\ \mathrm{dB}.$$

**Asymptotic gain.** As $M \to \infty$,
$\operatorname{Var} \to \rho = 0.02$, so
$G_{\infty} = 1/\sqrt{\rho} = 7.071$, i.e. 16.99 dB. At $M = 24$ the achieved
4.054 (12.16 dB) is 4.83 dB below that ceiling — so further stacks would still
buy something at this $\rho$, but the gain would flatten: at $M = 96$,
$\operatorname{Var} = (1+95\times0.02)/96 = 2.90/96 = 0.030208$ and
$G = 5.754$ (15.20 dB), only 3.0 dB more for four times the shots. The practical
rule is that useful stacking stops around $M \approx 1/\rho = 50$.

---

## ★★4 — Two-layer refraction model

**Critical angle:**

$$\theta_c = \arcsin\!\left(\frac{V_1}{V_2}\right) = \arcsin(0.285714)
= 16.6015^\circ .$$

**Intercept time:**

$$t_i = \frac{2h\sqrt{V_2^{2}-V_1^{2}}}{V_1 V_2}
= \frac{30 \times \sqrt{7\,840\,000 - 640\,000}}{800 \times 2800}
= \frac{30 \times 2683.28}{2\,240\,000} = 0.035937\ \mathrm{s} = 35.94\ \mathrm{ms}.$$

**Crossover distance:**

$$x_c = 2h\sqrt{\frac{V_2+V_1}{V_2-V_1}} = 30\sqrt{\frac{3600}{2000}}
= 30 \times 1.34164 = 40.25\ \mathrm{m}.$$

**Depth sensitivity:**

$$\frac{\partial h}{\partial t_i} = \frac{V_1 V_2}{2\sqrt{V_2^{2}-V_1^{2}}}
= \frac{2\,240\,000}{2 \times 2683.28} = 417.40\ \mathrm{m/s},$$

so a 1 ms intercept-time error gives

$$\Delta h = 417.40 \times 10^{-3} = 0.417\ \mathrm{m}.$$

**Check.** Inverting the intercept time for depth:
$h = t_i \times 417.40 = 0.035937 \times 417.40 = 15.00\ \mathrm{m}$ ✔.

---

## ★★★5 — Design for a 30 m target with ±1 m depth accuracy

**Velocity information.** The depth formula is $h = t_i V_1 V_2/(2\sqrt{V_2^2-V_1^2})$,
so $V_1$ and $V_2$ are required, and Section 6 of the lesson showed that at a 4:1
contrast a 5 % $V_1$ error moves the depth by more than a 5 ms picking error.
Obtain them as follows:

1. **$V_1$** from an uphole or downhole measurement at a representative location,
   or from the direct-wave branch of the refraction record itself with a
   linear fit to the near-offset arrivals. Report the fit residual and the number
   of picks; a fitted $V_1$ with a stated uncertainty is the deliverable.
2. **$V_2$** from the reverse (reciprocal) shot at the same spread: shooting from
   both ends identifies the dip and gives a better-constrained refractor velocity
   than a single-ended spread.

**Required offset range.** The refractor must be the first arrival over enough
offsets to be fitted. Take $V_1 = 800\ \mathrm{m/s}$, $V_2 = 2800\ \mathrm{m/s}$
(this exercise's values) and $h = 30\ \mathrm{m}$:

$$t_i = \frac{60 \times 2683.28}{2\,240\,000} = 0.071875\ \mathrm{s},
\qquad
x_c = 60 \times 1.34164 = 80.50\ \mathrm{m}.$$

So no refractor arrival exists closer than about 80 m, and the useful offset range
starts just beyond that. To fit a line to the head-wave branch with a useful lever
arm, use offsets up to at least $3x_c \approx 240\ \mathrm{m}$: the offset range
80–240 m gives a 160 m baseline for the slope fit.

**Receiver spacing and spread.** The receiver interval must be small enough to
pick the refractor's moveout without spatial aliasing: at $V_2$ and a 3 m interval
the aliasing frequency is $2800/(2 \times 3) = 467\ \mathrm{Hz}$, comfortably above
any refraction signal. Practically, 3 m spacing over 240 m requires 81 channels;
10 m spacing would alias above $2800/20 = 140\ \mathrm{Hz}$, still adequate, and
needs 25 channels. Use 10 m spacing and 25 channels with a 250 m spread, and
confirm by inspecting the first-break picks rather than by trusting the arithmetic.

**Shots per kilometre.** Two requirements: a shot at each end of every spread
(reciprocal shooting, to identify dip) and enough intermediate shots to build a
redundant interpretation. With a 250 m spread, a pair of end shots every 250 m is
8 shots/km; add one mid-spread shot per 125 m for redundancy, giving 16 shots/km.
More shots improve the depth estimate only through redundancy in $V_1$ and $t_i$,
not through fold, because refraction interpretation uses first-arrival times rather
than stacked traces.

**Sensitivity.** With $\partial h/\partial t_i = V_1V_2/(2\sqrt{V_2^2-V_1^2})
= 2\,240\,000/(2 \times 2683.28) = 417.40\ \mathrm{m/s}$, a 2 ms pick error gives

$$\Delta h = 417.40 \times 0.002 = 0.835\ \mathrm{m},$$

which already consumes most of the ±1 m budget. The velocity sensitivities are
$\partial h/\partial V_1 = t_i V_2^{3}/(2(V_2^{2}-V_1^{2})^{3/2}) > 0$ and
$\partial h/\partial V_2 = -t_i V_1^{3}/(2(V_2^{2}-V_1^{2})^{3/2}) < 0$; evaluated
directly at perturbed velocities rather than by the derivative, since the signs
are the point:

| Perturbation | depth change (m) |
|---|---|
| $t_i$ +2 ms | +0.835 |
| $V_1$ +5 % | +1.644 |
| $V_2$ +5 % | −0.123 |

So a 5 % error in the near-surface velocity moves the depth by 1.64 m — **more
than the pick error and more than the whole ±1 m budget**.

**Conclusion.** The ±1 m target is not met by a single-ended spread with an
assumed velocity. The design must (i) measure $V_1$ independently, to better than
about 0.6 % (since 1.644 m comes from 5 %, a 1 m budget allows about 3 % — and
only if the pick error is negligible), (ii) shoot reciprocally to constrain $V_2$
and the dip, and (iii) report the depth as a distribution from the measured
uncertainties rather than as a single number. A design that omits (i) cannot claim
±1 m at any fold.

---

## ★★★6 — A repeatability test

**Measurement.** Occupy a fixed pair of source and receiver positions, or a short
line of them, and repeat the *same* shot several times (typically 5–10) within a
short interval, recording to the same spread with identical gain, filters and
geometry. Repeat the whole set a second time after re-occupying the source position
(simulating a re-shoot), and a third time after a day (simulating a re-visit).

**Metric.** The normalised RMS difference between two traces $a$ and $b$,

$$\text{NRMS} = \frac{\mathrm{RMS}(a - b)}
{\tfrac{1}{2}\left[\mathrm{RMS}(a) + \mathrm{RMS}(b)\right]},$$

reported as a percentage, either over the full trace or within a stated time
window around the target reflection. NRMS is dimensionless and is the standard
acquisition repeatability metric because it is insensitive to a common amplitude
scale.

**Acceptance threshold.** State a value before the survey and record it in the
plan. Typical practice for a 4-D survey is a few per cent for the *repeat* shot at
the same position, and a somewhat larger value for a re-occupied position; the
acceptable value depends on the signal-to-noise of the target, and the threshold
should be chosen from the noise level that the 4-D signal of interest must exceed,
not from a rule of thumb. Report the metric per shot pair with its scatter, not as
a single number.

**Causes of failure it detects.** Source position error (a shifted source produces
a moveout difference), source coupling changes (a plate on looser ground),
charge or sweep variation, receiver coupling changes, clock errors between
recordings, and changes in the near-surface where the source is buried.

**What it cannot establish.** (i) Whether the *target* is repeatable: NRMS measures
the whole trace, and a large near-surface change can dominate the metric while the
target is stable, or vice versa — the window matters and must be justified. (ii) The
absolute amplitude calibration: two traces can be highly repeatable in shape while
both carry the same systematic gain error, and the metric is blind to that. A
separate absolute calibration is needed
([23-05-04 Calibration, Testing and Traceability](../../05-instrumentation-and-electronics/04-calibration-and-testing.md)).
