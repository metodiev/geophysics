---
id: 09-07-01
title: "EM Noise, Coupling and Cultural Effects"
level: graduate
prereqs: ["09-01-01", "09-02-03", "05-06-01"]
tags: [electrical-methods, noise, coupling, stacking, qc]
---

# EM Noise, Coupling and Cultural Effects

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** measurement error into incoherent noise, coherent noise and
   systematic (cultural) error, and **explain** why only the first of the three
   averages down.
2. **Derive** how noise on a measured potential propagates into apparent
   resistivity through the geometric factor $K=2\pi a$, and **predict** the
   spacing dependence of the error.
3. **Measure** the reduction of incoherent noise with the number of repeats,
   **verify** the $1/\sqrt{N}$ law, and **show** that a phase-locked coherent line
   does not reduce at all.
4. **Compare** mean, median and trimmed-mean stacking under a stated spike
   population, and **choose** between them on the basis of a measured rms error
   rather than of principle.
5. **Demonstrate** that a perfectly phase-locked powerline line is exactly
   degenerate with the DC level in a repeat-axis regression, and **state** the
   physical change that removes the degeneracy.
6. **Propagate** a surviving coherent error into an interpreted two-layer model
   and **quantify** the bias it produces in $\rho_2$ and $H$.
7. **State** the assumptions behind a signal-to-noise argument — independence and
   stationarity — and **name** the measurement that tests each.

## Prerequisites

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  what the quantity being measured is, and its range in nature.
- [09-02-03 Apparent Resistivity and Geometric Factors](../02-dc-resistivity/03-apparent-resistivity.md) —
  the geometric factor, which is the amplifier of measurement noise.
- [05-06-01 The Processing Pipeline Concept](../../05-core-geophysics/06-data-processing-principles/01-processing-pipeline-concept.md) —
  stacking, filtering and the distinction between signal and noise.

## 1. Intuition: three different things called noise

"Reduce the noise" is not one instruction but three, and they need different
responses.

- **Incoherent noise** is uncorrelated between repeats: thermal noise in the
  receiver, natural telluric fluctuations, and anything else that differs from
  repeat to repeat. Averaging $N$ repeats reduces its standard deviation by
  $\sqrt{N}$, and only by $\sqrt{N}$; this is the one place where "just stack
  more" is correct.
- **Coherent noise** is the same from repeat to repeat: a powerline line whose
  phase is locked to the acquisition cycle, a transmitter-receiver coupling that
  does not change, a telluric field that varies slowly compared with the
  repeat interval. Averaging does not reduce it, because as far as the stack is
  concerned it is signal.
- **Systematic (cultural) error** is neither: a metal fence in the array, a
  grounded well casing, a pipeline, a buried service. It changes the measured
  value by an amount that is a property of the site and the geometry, not of
  time, and no repetition scheme can see it.

The module's demonstration makes all three measurable on one synthetic sounding
and then follows the survivor into an interpreted model. The result is the
lesson's organising claim: **the error budget is dominated not by the largest
term but by the term that does not average down.**

All models and data in this module are **SYNTHETIC**. The two-layer earth is an
exact teaching model, and every noise amplitude below is a chosen value, not a
measurement from an instrument or a site.

## 2. The forward model used throughout this module

So that noise can be followed all the way into a geological statement, module 09
uses one exact forward model. For a Wenner array of spacing $a$ over a two-layer
earth (resistivity $\rho_1$ to depth $H$, then $\rho_2$), the potential of a point
source at the surface is the image series

$$\phi(r) = \frac{I\rho_1}{2\pi}\left[\frac{1}{r}
+ 2\sum_{n=1}^{\infty}\frac{k^{n}}{\sqrt{r^{2}+(2nH)^{2}}}\right],
\qquad k = \frac{\rho_2-\rho_1}{\rho_2+\rho_1},$$

and, with the geometric factor of the array, this gives

$$\rho_a(a) = \rho_1\left[1 + 4a\sum_{n=1}^{\infty}k^{n}
\left(\frac{1}{\sqrt{a^{2}+(2nH)^{2}}} -
\frac{1}{\sqrt{4a^{2}+(2nH)^{2}}}\right)\right].$$

The demonstration verifies both limits: $a\to0$ gives
$\rho_a = 25.000000\ \Omega\,\mathrm{m} = \rho_1$, and $a\to\infty$ gives
$499.997766\ \Omega\,\mathrm{m} \to \rho_2 = 500\ \Omega\,\mathrm{m}$. Because
the model is exact, any error in the processing or the inversion is *our* error,
not the model's — which is the only way an error budget can be written down
honestly.

The synthetic earth is $\rho_1 = 25\ \Omega\,\mathrm{m}$,
$\rho_2 = 500\ \Omega\,\mathrm{m}$, $H = 8.0$ m, $k = 0.9048$, and the
noise-free sounding on eight logarithmic spacings from 1 to 56 m is

| $a$ (m) | 1.0 | 1.8 | 3.2 | 5.6 | 10.0 | 18.0 | 32.0 | 56.0 |
|---|---|---|---|---|---|---|---|---|
| $\rho_a$ ($\Omega$ m) | 25.038 | 25.217 | 26.120 | 29.843 | 41.972 | 68.511 | 110.897 | 169.494 |

## 3. The noise budget, and why the spacing controls it

### 3.1 Propagation through the geometric factor

A four-electrode measurement returns

$$\rho_a = K\,\frac{\Delta V}{I}, \qquad K = 2\pi a
\quad (\text{Wenner, half-space}),$$

so a constant error $\sigma_V$ on the measured potential becomes an error

$$\sigma_{\rho_a} = K\,\sigma_V = 2\pi a\,\sigma_V .$$

**The error in apparent resistivity grows linearly with spacing**, because the
geometric factor does: a wide array measures a small potential difference and
multiplies it by a large number. Setting $\sigma_V$ so that the smallest spacing
has a $1\%$ error gives

| $a$ (m) | 1.0 | 1.8 | 3.2 | 5.6 | 10.0 | 18.0 | 32.0 | 56.0 |
|---|---|---|---|---|---|---|---|---|
| $\sigma_{\rho_a}$ ($\Omega$ m) | 0.250 | 0.451 | 0.801 | 1.402 | 2.504 | 4.507 | 8.012 | 14.021 |
| relative error | 1.00% | 1.79% | 3.07% | 4.70% | 5.97% | 6.58% | 7.22% | 8.27% |

This is the first place where a noise budget becomes a statement about
*geology*: the largest spacings carry the deepest information and the worst
relative error, so the deep part of an inversion is the noisiest, and the
apparent-resistivity curve is heteroscedastic by construction. Weighted least
squares with $\sigma\propto a$ is not a refinement here; it is the correct
likelihood.

### 3.2 A coherent line

The demonstration injects a powerline line whose amplitude in volts is $2.5\times$
the potential noise, i.e. a constant voltage at every spacing. Because of the
$2\pi a$ factor it appears in apparent resistivity as

| $a$ (m) | 1.0 | 3.2 | 10.0 | 56.0 |
|---|---|---|---|---|
| line amplitude ($\Omega$ m) | 0.626 | 2.003 | 6.260 | 35.054 |
| as a fraction of the datum | 2.50% | 7.67% | 14.91% | 20.68% |

**The coherent line is worst at the largest spacing**, exactly where the
incoherent error is worst: neither can be fixed by improving the *noise* figure,
one is fixed by stacking and the other is not.

## 4. Stacking: what averages down

The demonstration runs 300 independent experiments with $N$ repeats and measures
the rms error of the stacked estimate at the widest spacing:

| $N$ | incoherent (rms, $\Omega$ m) | line phase-locked | line drifting 0.35 rad/repeat | $\sigma/\sqrt{N}$ |
|---|---|---|---|---|
| 1 | 13.2296 | 27.3909 | 13.6476 | 14.0214 |
| 4 | 6.9368 | 23.8548 | 17.5547 | 7.0107 |
| 16 | 3.5119 | 22.8899 | 3.6533 | 3.5053 |
| 64 | 1.7714 | 22.6274 | 3.5790 | 1.7527 |
| 256 | 0.8815 | 22.5303 | 0.8856 | 0.8763 |

Three readings of that table:

1. **Incoherent noise follows $1/\sqrt{N}$ exactly** — the measured column and the
   predicted column agree to two significant figures at every $N$. There is no
   better reduction available: to halve the error again you need four times the
   repeats.
2. **A phase-locked line does not reduce at all.** The error starts at 27.4 and
   ends at 22.5 after 256 stacks. To the stack, the line *is* the signal.
3. **A drifting phase recovers $1/\sqrt{N}$.** The line cancels between repeats
   once the phase advances, and the error returns to the incoherent value. In
   practice this is what happens, because the repeat interval is not an integral
   number of line periods; the physical design choice is to *make sure* it is
   not.

## 5. Robust stacking under spikes

Cultural transients — a passing vehicle, a spike from near-by electrical
equipment — produce occasional samples with values many times the noise. The
demonstration injects spikes into $2\%$ of repeats at $15\sigma$ and compares
three stackers at $N=64$, over 300 experiments (widest spacing):

| estimator | bias ($\Omega$ m) | rms error ($\Omega$ m) |
|---|---|---|
| mean | $-0.205$ | 3.940 |
| median | $-0.193$ | 2.181 |
| 15%-trimmed mean | $-0.108$ | 1.805 |

All three are unbiased; they differ in **efficiency** and in robustness. The
median's rms is $45\%$ lower than the mean's under this spike population — and it
would be *higher* under pure Gaussian noise, because the median throws away
information. The choice is therefore a claim about the noise: **if you use a
median, you have asserted that a fraction of the data are contaminated.** That
claim should be written in the processing log, not implied.

## 6. Coupling: when no estimator can help

A repeat-axis filter that estimates and removes a line at frequency $f$ is a
least-squares fit of $[\cos(2\pi f t_j), \sin(2\pi f t_j), 1]$ to the repeat
sequence $t_j$. Everything depends on whether the phase advances between repeats.
The demonstration measures the design matrix directly:

| case | singular values of $\mathbf{A}$ | condition number | rms error before | after notch |
|---|---|---|---|---|
| phase locked | 11.3137, 0, 0 | $4.0\times10^{31}$ | 22.698 | 73.588 |
| drifting 0.35 rad/repeat | 8.0588, 5.7079, 5.5206 | 1.46 | 5.088 | 4.021 |

With a constant phase the three columns of $\mathbf{A}$ are *the same column*:
the matrix has rank 1 and the line is **exactly degenerate** with the DC level.
The notched estimate is then worse than the plain average (73.6 against 22.7)
because the fit splits a single number among collinear columns and returns it
misattributed. This is not a numerical accident; it is a statement that a
constant-phase line and a DC offset are the same observation, and no arithmetic
separates them.

The remedies are physical:

- **Change the repeat interval** so that the phase advances between repeats
  (demonstrated: condition number 1.46, notch improves the estimate from 5.09 to
  4.02).
- **Place the measurement window away from the line.** A time-domain
  measurement that does not sample the line band cannot be contaminated by it.
- **Measure the line current independently** and use it as a reference.

## 7. What the survivor does to the model

The demonstration stacks 64 repeats containing the phase-locked line and inverts
the resulting sounding for $(\rho_2, H)$ with $\rho_1$ fixed:

| data | $\rho_2$ ($\Omega$ m) | error | $H$ (m) | error |
|---|---|---|---|---|
| noise-free | 500.0 | — | 8.00 | — |
| locked line (3 realisations) | 690, 650, 555 | +38%, +30%, +11% | 7.45, 7.35, 7.30 | $-0.55$, $-0.65$, $-0.70$ m |
| drifting line, same noise | 435, 470, 500 | $-13\%$, $-6\%$, 0% | 7.65, 7.75, 7.75 | $-0.35$, $-0.25$, $-0.25$ m |

The errors from the locked line are *systematic*: they do not shrink with more
repeats, they do not change sign, and they are larger than the scatter of the
drifting case. A formal error bar computed from repeat scatter would report only
the drifting column — which is exactly the failure mode that module
[09-07-03](03-em-uncertainty.md) makes quantitative.

## 8. Assumptions and regime of validity

1. **Repeats are independent for the incoherent component.** If the same
   telluric fluctuation persists across many repeats (which it does, at periods
   of minutes), the effective $N$ is smaller than the nominal $N$ and $1/\sqrt{N}$
   overstates the gain. The test is to compute the autocorrelation of the repeat
   sequence.
2. **Noise is stationary.** The synthetic model has a constant relative error;
   real EM data often have noise proportional to the transmitted current (which
   changes with battery state and coil geometry). Then the correct weights change
   through the survey and must be recorded.
3. **The spike population is as stated.** Robust estimators buy their robustness
   with efficiency at a specified contamination; the fraction must be estimated
   from the data (e.g. by the MAD criterion of module
   [09-07-02](02-em-processing-workflow.md)).
4. **The line is the only coherent component.** In practice a telluric field
   varies slowly and is not a single frequency; removing one line leaves a
   drifting baseline, which is handled by the drift removal of module 09-07-02.
5. **The forward model is exact for the two-layer earth.** It is not the Earth;
   the interpretation error caused by using two layers for a genuinely layered
   ground is *model* error, treated in module
   [09-07-03](03-em-uncertainty.md).
6. **The geometric factor is the half-space Wenner value.** Layering changes
   $K$ slightly; using a constant $K$ is a second-order error compared with the
   ones above, but it is an error.

## 9. Worked examples

### Example 1 — how many repeats for a target error?

The deepest datum has $\sigma_{\rho_a} = 14.02\ \Omega\,\mathrm{m}$ (8.27% of
169.49). Suppose the interpretation needs it at $2\%$, i.e.
$\sigma \le 3.39\ \Omega\,\mathrm{m}$. With incoherent noise only,
$\sigma/\sqrt{N} \le 3.39$ requires $N \ge (14.02/3.39)^{2} = 17.1$, so
$N = 18$ repeats. If a phase-locked line of the amplitude in §3.2 is present, the
error floor is $35.05 \times \sin(0.7) = 22.6\ \Omega\,\mathrm{m}$ and **no** value
of $N$ reaches the target: the requested precision is not achievable at that
spacing with that coupling, and the survey has to be changed.

### Example 2 — the cost of a bad weight

Unweighted least squares on the eight-spacing sounding gives every datum the same
$\sigma$. The two deepest spacings then contribute $(3.39/14.02)^{2} = 0.058$ of
their correct weight, so the deep information is effectively discarded. The
inversion returns a shallower $H$ and a smaller $\rho_2$, and — the important
point — the *residual* is dominated by the shallow data, so the misfit looks
excellent for a model that has thrown the target away. Always plot weighted
residuals, not raw ones.

### Example 3 — why a median is not free

Under pure Gaussian noise, the median of $N$ samples has variance
$\pi/2 \approx 1.571$ times the mean's. In the demonstration's contaminated case
the median's rms error is 2.181 against the mean's 3.940, a factor 0.554. If the
same data had no spikes, the ratio would be approximately
$1/\sqrt{1.571} = 0.798$ in favour of the mean. A processing chain that uses a
median everywhere is therefore paying a $\sim25\%$ efficiency penalty on clean
data to buy robustness on unclean data — a legitimate choice, but one to be made
knowingly and recorded.

## 10. Python demonstration

[`code/em_noise_and_coupling_demo.py`](./code/em_noise_and_coupling_demo.py)
prints, with units:

1. the exact two-layer forward model with both asymptotic limits;
2. the noise budget on the eight spacings, including the coherent line amplitude
   expressed both in volts and in apparent resistivity;
3. the stacking table for incoherent, phase-locked and drifting-line noise
   against the $1/\sqrt{N}$ prediction;
4. the mean/median/trimmed comparison under a $2\%$, $15\sigma$ spike population;
5. the design-matrix singular values in both coupling cases, with the before/after
   notch errors;
6. the inversion of the stacked data, giving the parameter bias caused by the
   phase-locked line.

```bash
cd 09-electrical-em-methods/07-em-data-processing-and-qc/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_noise_and_coupling_demo.py
```

It takes about eleven seconds, needs no network, uses a fixed seed
(`np.random.default_rng(20261014)`) and exits 0.

## 11. Exercises

See
[`exercises/01-em-noise-and-coupling-exercises.md`](./exercises/01-em-noise-and-coupling-exercises.md)
and
[`exercises/01-em-noise-and-coupling-solutions.md`](./exercises/01-em-noise-and-coupling-solutions.md).

- **★** Compute $\sigma_{\rho_a}$ at four spacings for a stated $\sigma_V$ and
  state which spacing limits the sounding.
- **★★** Derive the $1/\sqrt{N}$ law for the mean of independent samples, and
  state the two assumptions it needs; then say which of them the drifting-line
  case violates and how.
- **★★** Given the median/mean efficiency ratio under Gaussian and contaminated
  noise, choose a stacker for a survey with a stated contamination rate and
  defend the choice with the two rms numbers.
- **★★★** Design an acquisition scheme whose repeat interval guarantees a
  specified minimum phase advance of a 50 Hz line between repeats, for a stated
  repeat period and sampling rate.

## 12. Common mistakes

1. **Averaging away a coherent line.** It has a phase; check it before stacking.
2. **Reporting a scatter-based error bar when a coherent term is present.** The
   scatter measures only the incoherent part.
3. **Assuming uniform data errors.** The geometric factor makes $\sigma\propto a$.
4. **Using a notch filter without checking the design matrix.** With a locked
   phase the notch is degenerate and makes things worse.
5. **Choosing a robust estimator by taste.** State the contamination fraction you
   are robust to.

## Mastery checkpoint

Complete this without notes.

> A Wenner sounding uses spacings 1, 2, 4, 8, 16 and 32 m.
> **(a)** With a constant potential noise $\sigma_V$ chosen so the 1 m spacing is
> good to $1\%$, compute the relative error of every spacing.
> **(b)** Sketch (in numbers) the effect on a weighted and an unweighted
> inversion, and say which datapoints each effectively uses.
> **(c)** A 50 Hz line of amplitude $2\sigma_V$ in volts is present and its phase
> is identical in every repeat. Compute its contribution at each spacing in
> $\Omega\,\mathrm{m}$, and state what stacking 100 repeats does to it.
> **(d)** Repeat (c) with a repeat interval that advances the phase by $0.4$ rad
> per repeat, and state the rms error after 100 repeats, assuming the incoherent
> term dominates.
> **(e)** State the one number you must report alongside an inverted $H$ so that a
> reader can tell which of these cases applies.

A worked version of (a) and (c) appears in the lesson-01
[solutions](./exercises/01-em-noise-and-coupling-solutions.md).

## Common pitfalls

1. **Confusing precision with accuracy.** Many repeats give a precise and
   biased answer.
2. **Treating the geometric factor as bookkeeping.** It is the amplifier that
   couples measurement noise to the reported quantity.
3. **Believing a small misfit.** A badly weighted inversion can fit the shallow
   data beautifully while discarding the target.
4. **Forgetting the site.** Buried metal changes the measured value and is
   invisible to every averaging scheme.
5. **Assuming noise scales with the datum.** It scales with the *measurement*,
   and then with the geometric factor.

## Related modules

- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) — the arrays,
  geometric factors and weighting this lesson assumes.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the EM soundings whose late-time windows are the noisiest and most
  contaminated datapoints.
- [09-07-02 EM Processing Workflow and Data Editing](02-em-processing-workflow.md) —
  what to do with the contaminated samples once they are identified.
- [09-07-03 Quantifying Uncertainty in EM Interpretation](03-em-uncertainty.md) —
  how to combine the surviving coherent error with the statistical interval.
