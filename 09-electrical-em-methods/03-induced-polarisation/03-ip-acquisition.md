---
id: 09-03-03
title: "IP Acquisition, Chargeability and Phase Units"
level: graduate
prereqs: ["09-03-01", "09-02-05", "09-02-07", "01-13-09"]
tags: [electrical-methods, induced-polarisation, acquisition, units, noise, uncertainty, survey-design]
---

# IP Acquisition, Chargeability and Phase Units

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** between the three reported IP quantities — window-integral
   chargeability, percent frequency effect and phase — and **state** that the
   conversion factor is a property of a model, not a constant.
2. **Derive** the phase-noise law
   $\sigma_{\varphi} = \sigma_n/\left(A\sqrt{M/2}\right)$ for a least-squares
   phase estimate and **verify** it against a Monte Carlo measurement.
3. **Compute** the number of stacks, and hence the acquisition time, that a
   target phase resolution costs at a stated signal-to-noise ratio.
4. **Quantify** how the charging time, the integration window and a linear drift
   bias a chargeability measurement, and **state** which correction removes each.
5. **Estimate** the error introduced by applying a single conversion factor to a
   set of model responses, using the measured spread of that factor.
6. **Demonstrate** that a fitted $(m, \tau)$ pair depends on the chosen window
   set, and **report** the admissible ranges instead of a single value.
7. **Design** a minimal IP acquisition: window, on-time, stack count and expected
   uncertainty, with each number justified by an arithmetic step.

## Prerequisites

- [09-03-01 IP Principle: Time-Domain and Frequency-Domain Measurement](01-ip-principle.md)
  — the chargeability conventions and the Debye response.
- [09-02-05 ERT Acquisition and Design](../02-dc-resistivity/05-ert-tomography.md)
  — electrode layouts, contact resistance and survey logistics.
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](../02-dc-resistivity/07-resistivity-inversion.md)
  — what a model family does to the answer.
- [01-13-09 Error and Uncertainty Propagation](../../01-mathematics/13-probability-and-statistics-foundations/09-error-propagation.md)
  — how an input uncertainty becomes an output uncertainty.

**All models and data in this module are SYNTHETIC.** Resistivities,
chargeabilities, noise levels and acquisition times are chosen teaching values,
not measurements of any site or instrument.

---

## 1. Intuition: IP is a small-signal measurement with a long integration

A polarised ground produces a secondary voltage that is typically a few per cent
of the primary, and a phase lag in the milliradian range. Both are measured on
top of a primary voltage that is itself contaminated by telluric currents,
electrode drift and cultural noise. The consequence is not a subtle
instrumentation detail; it *is* the survey design problem:

- **The signal is a fraction of the total.** Only a part of what the voltmeter
  reads carries the information, so the effective signal-to-noise ratio is worse
  than the raw numbers suggest.
- **The measurement is an average.** Both domains integrate: the time domain
  integrates the decay over a window, the frequency domain averages many cycles.
  Averaging reduces random noise as $\sqrt{M}$ in the number of samples, so an
  extra decade of precision costs a hundredfold more time.
- **The quantities are defined by convention.** Chargeability, percent frequency
  effect and phase are three functionals of one response, and the conversion
  between them requires a model. This lesson measures how large the resulting
  ambiguity is.

The order of magnitude is worth stating before any formula: reaching a
$1$ mrad phase uncertainty with an amplitude signal-to-noise ratio of $20$ to
$1$ requires of order $10^{4}$ samples (measured below), which at one cycle per
second is hours. That arithmetic, not instrument sensitivity, sets what an IP
survey can afford.

## 2. Precise definitions

### 2.1 The three reported quantities

| Quantity | Definition | Unit | Model dependence |
|---|---|---|---|
| window-integral chargeability | $M_{\text{int}}(T) = \frac{1}{V_p}\int_0^T V_s\,\mathrm{d}t$ | ms (or mV/V per s) | window length $T$; charging time |
| window-average chargeability | $M_{\text{avg}}(T) = M_{\text{int}}/T$ | mV/V | as above |
| percent frequency effect | $\mathrm{PFE} = \frac{\rho_{\text{low}} - \rho_{\text{high}}}{\rho_{\text{high}}}\times100$ | % | the two frequencies chosen |
| phase | $\varphi = \arg\rho$ | mrad, deg | the frequency chosen |

### 2.2 Signal-to-noise, stacking and duty cycle

Let $A$ be the amplitude of the measured voltage at the fundamental frequency
and $\sigma_n$ the rms noise in the same band. A harmonic measurement that
records $M$ samples of the fundamental has a phase uncertainty

$$\sigma_{\varphi} = \frac{\sigma_n}{A\sqrt{M/2}}$$

(Section 3.1), independent of $M$ to the extent that the noise is white and
stationary. A time-domain measurement instead stacks $N$ decays: if each decay
has noise $\sigma_n$, the stacked decay has $\sigma_n/\sqrt{N}$ — the same
square-root law, wearing a different hat.

### 2.3 What "the same ground" means

Two measurements of one ground can disagree and both be right. The window
integral depends on $T$ and on the charging time; the phase depends on the
frequency; and the fitted model parameters depend on the band and the noise. The
only quantity in this list that is a property of the ground alone is the
*response function* $\rho(\omega)$ — and that is what every reported number is a
functional of.

## 3. Derivations

### 3.1 The phase-noise law

Write the sampled record of $M = N_{\text{cyc}}\,n_{\text{pc}}$ points (with
$n_{\text{pc}}$ samples per cycle) as

$$y_k = A\sin\left(\theta_k + \varphi\right) + n_k, \qquad
\theta_k = \frac{2\pi k}{n_{\text{pc}}},$$

with $n_k$ independent samples of zero-mean noise of variance
$\sigma_n^{2}$. Project onto the fundamental:

$$\hat{a} = \frac{2}{M}\sum_k y_k\cos\theta_k, \qquad
\hat{b} = \frac{2}{M}\sum_k y_k\sin\theta_k, \qquad
\hat{\varphi} = \operatorname{atan2}\left(\hat{b}, \hat{a}\right).$$

Because $\cos\theta_k$ and $\sin\theta_k$ are orthogonal over whole cycles,
$X^{\mathsf{T}}X = (M/2)\,I$ for the two-parameter fit, so

$$\operatorname{var}(\hat a) = \operatorname{var}(\hat b) = \frac{2\sigma_n^{2}}{M}.$$

Propagating through $\varphi = \arctan(a/b)$ with $a = A\sin\varphi$,
$b = A\cos\varphi$:

$$\sigma_{\varphi}^{2} = \frac{\cos^{2}\varphi}{A^{2}}\operatorname{var}(\hat a)
+ \frac{\sin^{2}\varphi}{A^{2}}\operatorname{var}(\hat b)
= \frac{2\sigma_n^{2}}{MA^{2}}
\;\Longrightarrow\;
\boxed{\;\sigma_{\varphi} = \frac{\sigma_n}{A\sqrt{M/2}}.\;}$$

The demonstration measures this law directly: over a $256$-fold change in the
number of cycles and a fourfold change in $\sigma_n/A$, the dimensionless
combination $\sigma_{\varphi}A\sqrt{M/2}/\sigma_n$ stays inside
$0.94$ to $1.05$ (ten entries, mean $0.995$), i.e. the law holds to about $5\%$
with $300$ realisations per entry. Measured values include $13.171$ mrad for
$32$ samples at $\sigma_n/A = 1/20$ and $0.7672$ mrad for $8192$ samples at the
same ratio — a factor $17.2$ for a factor $16$ in $\sqrt{M}$, as the law
requires.

### 3.2 Inverting the law: the cost of a resolution

Rearranging,

$$M = 2\left(\frac{\sigma_n}{A\,\sigma_{\varphi}}\right)^{2}
\quad\text{samples}, \qquad
t_{\text{acq}} = \frac{M}{n_{\text{pc}}}\,T_{\text{cycle}}.$$

With $n_{\text{pc}} = 32$ and a $1$ Hz fundamental ($T_{\text{cycle}} = 1$ s):

| $\sigma_n/A$ | target $\sigma_{\varphi}$ | samples $M$ | time at 1 Hz |
|---|---|---|---|
| $1/20$ | 10 mrad | 50 | 1.6 s |
| $1/5$ | 10 mrad | 800 | 25.0 s |
| $1/20$ | 1 mrad | 5000 | 156.2 s |
| $1/5$ | 1 mrad | 80 000 | 2500.0 s |
| $1/5$ | 0.5 mrad | 320 000 | 10 000.0 s |

The last row is nearly three hours for a single measurement. This table is the
quantitative version of the folklore that IP is slow, and it also shows the
leverage available: halving $\sigma_n/A$ (better electrodes, lower contact
resistance, quieter site) buys a factor four in time.

### 3.3 Charging time, window and drift

Three systematic effects act on the time-domain number, and they scale
differently:

1. **Charging.** With the current on for $t_{\text{on}}$, the decay starts from
   $m\left(1 - e^{-t_{\text{on}}/\tau}\right)$ instead of $m$. For
   $\tau = 1.5$ s the measured bias against the fully charged value is
   $-84.65\%$ at $t_{\text{on}} = 0.25$ s, $-51.34\%$ at $1.00$ s, $-26.36\%$ at
   $2.00$ s and $-0.48\%$ at $8.00$ s. The correction is
   $\left(1 - e^{-t_{\text{on}}/\tau}\right)$, so it needs an estimate of
   $\tau$ — which is what the survey is trying to measure. The standard practice
   of fixing $t_{\text{on}}$ therefore *defines* a maximum measurable $\tau$.
2. **Window.** $M_{\text{int}} \propto \left(1 - e^{-T/\tau}\right)$, so a window
   shorter than $\tau$ measures $mT$ and a longer one measures $m\tau$; the
   transition is complete by about $5\tau$.
3. **Drift.** A linear drift $s$ [V/s] across the window adds
   $\frac{1}{2}sT$ to the integral; dividing by $V_p$ and converting to ms gives
   a bias of $500\,sT/V_p$ ms with $s$ in V/s and $T$ in s. The demonstration,
   with $V_p = 10$ V and $T = 1$ s, measures $+0.025$ ms at $s = 0.5$ mV/s,
   $+0.100$ ms at $2.0$ mV/s and $+0.500$ ms at $10.0$ mV/s against a
   $72.987$ ms chargeability. **The drift bias is proportional to $T$**, so it
   cannot be averaged away by a longer window; it must be removed before
   integration (by fitting and subtracting a trend over a pre-switch-off
   baseline).

### 3.4 The conversion factor is a model

The same synthetic response produces a chargeability, a percent frequency effect
and a phase that are numerically unrelated except through a model. For the
Debye model of [09-03-01](01-ip-principle.md) with $m = 0.10$, $\tau = 1.5$ s:

- $\mathrm{PFE} = 4.6600\%$ between $0.125$ Hz and $1$ Hz;
- $\varphi = 52.332$ mrad at $0.125$ Hz and $11.643$ mrad at $1$ Hz;
- $M_{\text{int}}(0\text{–}1\,\mathrm{s}) = 72.987$ ms.

The dimensionless ratios are $\mathrm{PFE}/M = 0.0638$ per ms and
$\varphi(1\,\mathrm{Hz})/M = 0.1595$ mrad per ms. Now vary the model over
eighteen synthetic combinations of $(m, c, \tau)$ spanning $m$ from $0.05$ to
$0.30$, $c$ from $0.3$ to $1.0$ and $\tau$ from $0.3$ to $1.5$ s, and compute
$M/\varphi$ at $1$ Hz for each. The measured range is

$$M/\varphi \in \left[0.540,\ 6.612\right]
\quad\text{(a factor }12.25\text{)}.$$

The widely used working rule "chargeability in ms equals phase in mrad" is the
value $1.0$, which lies inside that range. Applied to the extremes, it misstates
the chargeability by a factor $6.61$ in one direction and a factor $1.85$ in the
other. **A conversion factor is a model statement.** The honest procedure is to
fit the model, convert with the fitted model, and report the residual of the fit
— not to apply a number learned from another survey.

### 3.5 The window decides which answer you get

Section 3.3 showed that the window changes the *number*. This section shows it
also changes the *model*. Take an exact two-relaxation response
($m = 0.12$ split $55/45$ between $\tau = 6.00$ s and $\tau = 0.30$ s), sample
its chargeability at a set of windows with $2\%$ noise, and fit one Debye:

| window set | best $m$ | best $\tau$ (s) | admitted $m$ ($\Delta\chi^{2}\le4$) | admitted $\tau$ (s) |
|---|---|---|---|---|
| 0.25–1 s | 0.111 | 1.266 | $[0.106, 0.116]$ | $[1.051, 1.636]$ |
| 0.25–16 s | 0.090 | 3.960 | $[0.088, 0.091]$ | $[3.795, 4.193]$ |

The same ground, one extra decade of window, a different answer: $m$ moves by
$-18.9\%$ and $\tau$ by a factor $3.13$. Neither reproduces the truth, and the
residual of the long-window fit at *zero* noise runs from $-13.89\%$ to
$+8.97\%$ across the windows, with a sign change — the signature of a model that
cannot represent the data. The admitted ranges are tight in both cases; they are
tight around the wrong model. **A narrow admitted range measures the noise, not
the ground.**

## 4. Physical interpretation

- **Charging and window are filters on $\tau$.** Fixing $t_{\text{on}}$ and $T$
  restricts attention to a band of time constants, exactly as fixing the
  frequencies does in the frequency domain. Reporting the filters is part of
  reporting the measurement.
- **Drift is a first-order error with a signature.** It scales with $T$ and with
  the electrode pair's chemistry, and it is why a pre-switch-off baseline and a
  full-decay fit beat a two-point window difference on marginal ground.
- **Stacking helps only if the noise is white.** Correlated noise (telluric
  fields, powerline harmonics, a moving cultural source) does not average down
  as $\sqrt{N}$, so real surveys plateau; that plateau is a property of the site.
- **Every conversion has a residual.** Converting chargeability to phase through
  a fitted model leaves a misfit, and the misfit is the honest error bar on the
  conversion. Where the misfit is comparable to the effect being interpreted, the
  conversion has decided the answer.

## 5. Assumptions and regime of validity

1. **Linear response.** All three quantities are assumed independent of the
   injected current. Doubling the current must not change $M$ or $\varphi$; if it
   does, the measurement is outside its regime and the numbers are not
   interpretable.
2. **Stationary, white, Gaussian noise** for the phase-noise law of Section 3.1.
   Coloured or correlated noise makes the $\sqrt{M}$ gain optimistic.
3. **Full cycles sampled** so that $\cos\theta$ and $\sin\theta$ are orthogonal;
   partial cycles bias the phase estimate.
4. **$\sigma_n \ll A$, so $\arctan$ linearises.** At a 1:1 signal-to-noise ratio
   the estimator becomes non-linear and biased, and the law above understates the
   error.
5. **No electrode polarisation and no induction coupling** in the modelled data.
   Both act as frequency-dependent systematic errors; the second grows with
   frequency and is treated in
   [09-07-01 EM Noise, Coupling and Cultural Effects](../07-em-data-processing-and-qc/01-em-noise-and-coupling.md).
6. **The window set and the model family are reported.** Section 3.5 is the
   evidence that omitting either changes the answer.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| signal amplitude | $A$ | V | |
| noise | $\sigma_n$ | V | same unit as $A$, so $\sigma_n/A$ is dimensionless |
| sample count | $M$ | — | $\sqrt{M}$ must appear, so $M$ must be a count |
| phase uncertainty | $\sigma_{\varphi}$ | rad | $\mathrm{V}/\left(\mathrm{V}\sqrt{\cdot}\right)$ |
| drift rate | $s$ | V/s | $\frac{1}{2}sT$ has units V, dividing by $V_p$ gives s |
| chargeability | $M_{\text{int}}$ | s (reported ms) | |
| PFE | — | % | two resistivities, same unit |

Check the drift bias against its measured value: $s = 2.0$ mV/s,
$T = 1$ s, $V_p = 10$ V gives $\frac{1}{2}\times 2.0\times10^{-3}\times 1 =
1.0\times10^{-3}$ V·s; divided by $V_p = 10$ V that is
$1.0\times10^{-4}$ s $= 0.100$ ms, which is exactly what the demonstration
prints. A dimensional check of this kind catches the most common error in the
literature: mixing up "mV/V" and "ms" when the window is not one second.

## 7. Worked examples

### Example 1 — how long does a 1 mrad phase take?

Target $\sigma_{\varphi} = 1$ mrad $= 10^{-3}$ rad, with
$\sigma_n/A = 1/5 = 0.2$:

$$M = 2\left(\frac{0.2}{10^{-3}}\right)^{2} = 2 \times 4\times10^{4}
= 8.0\times10^{4}\ \text{samples}.$$

At $32$ samples per cycle and a $1$ Hz fundamental that is
$80000/32 = 2500$ cycles, i.e. $2500.0$ s of continuous stacking — the
demonstration's table entry. Improving the signal-to-noise ratio to $1/20$ cuts
it to $5000$ samples, $156.2$ s. Both numbers are printed by the demonstration.

### Example 2 — the drift bias, checked against its derivation

Measured: $M_{\text{int}}(0\text{–}1\,\mathrm{s}) = 72.987$ ms with no drift and
$73.488$ ms with a $10.0$ mV/s drift. The difference is $0.501$ ms. Predicted
from Section 3.3 with $V_p = 10.0$ V and $T = 1$ s:

$$\Delta M = \frac{\frac{1}{2}sT}{V_p}\times1000\ \mathrm{ms}
= \frac{0.5 \times 10.0\times10^{-3} \times 1.0}{10.0}\times1000
= 0.500\ \mathrm{ms}.$$

The $0.001$ ms excess is the numerical quadrature of the tabulated decay, not
physics. Note the direction: on this synthetic model the drift raises the
apparent chargeability, so an uncorrected survey over-reports polarisation.

### Example 3 — what a conversion factor costs

A survey reports $M_{\text{int}} = 25.0$ ms and, quoting the common rule, also
reports "phase $\approx 25.0$ mrad". From the measured spread of $M/\varphi$
over the eighteen synthetic models ($0.540$ to $6.612$), the same chargeability
is consistent with phases from

$$\varphi_{\min} = \frac{M}{6.612} = \frac{25.0}{6.612} = 3.78\ \mathrm{mrad}
\qquad\text{to}\qquad
\varphi_{\max} = \frac{M}{0.540} = 46.3\ \mathrm{mrad}.$$

So the quoted "$25$ mrad" is inside the range but no better than a factor of
$6.6$ from the extremes. If the interpretation depends on distinguishing a
$10$ mrad response from a $30$ mrad one, the conversion must come from a fitted
model on that survey's own data.

### Example 4 — reading the window sensitivity as a design rule

For $\tau = 1.5$ s the window integral reaches $93.1\%$ of its asymptote at
$T = 4.00$ s and $99.5\%$ at $T = 8.00$ s (measured: $139.577$ and $149.276$ ms
against the asymptote $149.997$ ms). A survey whose window is
$1.00$ s therefore sees $72.987/149.997 = 48.7\%$ of the total chargeability of
this model — half the polarisation of the ground is outside the window. This is a
design decision, not an error: the window is chosen so that the *ratio* remains
sensitive to the target, and it must be quoted with every number.

## 8. Python demonstration

`code/ip_acquisition_demo.py` prints every number in this lesson. It:

1. computes the percent frequency effect, the phase at two frequencies and the
   window chargeability for one model, and the dimensionless ratios between them;
2. measures the phase-noise law over five stack counts and two
   signal-to-noise ratios ($300$ realisations each), reporting the invariant
   $\sigma_{\varphi}A\sqrt{M/2}/\sigma_n$;
3. inverts the law to give the sample count and the time a target phase
   resolution costs;
4. tabulates $M/\varphi$ over eighteen synthetic models and reports the spread;
5. fits one Debye to a two-relaxation truth over two window sets, reporting the
   best fit, the admitted ranges and the zero-noise residuals.

Run it with the project virtual environment:

```bash
cd 09-electrical-em-methods/03-induced-polarisation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_acquisition_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-ip-acquisition-exercises.md`](./exercises/03-ip-acquisition-exercises.md)
and
[`exercises/03-ip-acquisition-solutions.md`](./exercises/03-ip-acquisition-solutions.md).

- **★** A $2$ mrad phase must be resolved with $\sigma_n/A = 1/10$; how many
  samples and how many seconds at $2$ Hz with $16$ samples per cycle?
- **★★** Derive the drift bias $\Delta M_{\text{int}} = \frac{1}{2}sT/V_p$ and
  evaluate it for $s = 5$ mV/s, $T = 2$ s, $V_p = 20$ V, in ms.
- **★★** Using the measured spread of $M/\varphi$, bound the phase that
  corresponds to $M_{\text{int}} = 12$ ms, and state what additional measurement
  would narrow it.
- **★★★** Design an acquisition for a target with $\tau$ between $0.5$ and
  $5$ s and $m$ of order $0.05$, subject to a total time budget of one hour per
  sounding: choose $t_{\text{on}}$, the window set, the stack count and the
  frequencies, and state the expected uncertainty on $m$ and $\tau$.

## 10. Common mistakes

1. **Applying a conversion factor without a model.** The measured spread of
   $M/\varphi$ is a factor $12.25$ across eighteen plausible models.
2. **Assuming $\sqrt{N}$ stacking gain on correlated noise.** Telluric and
   powerline noise are not white; the gain plateaus.
3. **Choosing $t_{\text{on}}$ by habit.** It silently caps the measurable $\tau$;
   $-51.3\%$ of the chargeability was lost at $t_{\text{on}} = 1.00$ s when
   $\tau = 1.5$ s.
4. **Lengthening the window to reduce drift.** The drift bias is proportional to
   $T$; it gets worse.
5. **Quoting one window and calling it "the" chargeability.** Two conventions
   differ by the factor $T$.
6. **Reporting a tight admitted range from one window set.** Section 3.5's tight
   ranges surrounded the wrong model.
7. **Ignoring the sign convention of the phase.** Lag versus lead changes the
   interpretation of the amplitude spectrum.

## 11. Real-world applications

- **Survey planning.** The cost table of Section 3.2 converts a resolution
  target into field hours before mobilisation, which is the most useful single
  calculation in an IP feasibility study.
- **Quality control.** Repeat measurements, drift removal and a stated
  signal-to-noise ratio are the three numbers that make an IP dataset
  interpretable by someone else.
- **Time-lapse and monitoring.** Because ratios are more stable than raw
  voltages, chargeability and phase are the preferred monitoring observables; the
  detectability of a change is then set by the noise law of Section 3.1.
- **Joint inversion with resistivity.** The window and the model family enter the
  inversion as constraints; a poorly stated window becomes a systematic error
  that no amount of regularisation can remove.

## 12. Further reading

- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*
  (2nd ed., Cambridge University Press).** Level: textbook. Field procedures
  and the chargeability conventions.
- **Reynolds, J. M., *An Introduction to Applied and Environmental
  Geophysics* (2nd ed., Wiley-Blackwell).** Level: textbook. Practical
  treatment of noise, stacking and survey design for IP.
- **Sumner, J. S., *Principles of Induced Polarization for Geophysical
  Exploration* (Elsevier).** Level: research monograph. The most thorough
  discussion of the units and the window conventions.
- **Binley, A., & Kemna, A., "DC resistivity and induced polarization methods",
  in *Hydrogeophysics* (Springer).** Level: research review. The link from
  acquisition to the hydrogeophysical interpretation used in
  [04 IP for Sulphides, Clays, Contaminants and Permafrost](04-ip-applications.md).

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Every number in this lesson is
> printed by [`code/ip_acquisition_demo.py`](./code/ip_acquisition_demo.py) or
> is an exact arithmetic consequence of a printed number, shown line by line.

## 13. Related lessons

- [01 IP Principle: Time-Domain and Frequency-Domain Measurement](01-ip-principle.md) —
  the definitions and the Debye response used throughout.
- [02 IP Models: Cole-Cole, Debye, Constant-Phase Element](02-ip-models.md) —
  what the window set and the band do to fitted parameters.
- [04 IP for Sulphides, Clays, Contaminants and Permafrost](04-ip-applications.md) —
  what the numbers mean once they are measured.
- [09-02-05 ERT Acquisition and Design](../02-dc-resistivity/05-ert-tomography.md) —
  the resistivity half of the same field operation.
- [09-07-01 EM Noise, Coupling and Cultural Effects](../07-em-data-processing-and-qc/01-em-noise-and-coupling.md) —
  the systematic effects this lesson assumes away.

## 14. Self-assessment checklist

- [ ] I can derive $\sigma_{\varphi} = \sigma_n/(A\sqrt{M/2})$ from the
      two-parameter fit.
- [ ] I can turn a target phase resolution into a sample count and a time.
- [ ] I can compute the drift bias and the charging-time bias.
- [ ] I can explain why a conversion factor between domains is model-dependent.
- [ ] I can bound the phase range consistent with one chargeability.
- [ ] I can show that a window change moves the fitted $(m, \tau)$.
- [ ] I can write a complete acquisition specification with its uncertainties.
