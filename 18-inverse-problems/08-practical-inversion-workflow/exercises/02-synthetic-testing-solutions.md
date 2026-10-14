# Solutions — 18-08-02 Synthetic Testing, Checkerboards and Recovery Tests

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [02 Synthetic Testing, Checkerboards and Recovery Tests](../02-synthetic-testing.md).

---

## ★1 — Fixed and varied

Fixed: the forward operator $G$ (blur, sampling, wavelet), the noise level
$\sigma$, and the regularisation $P_0$ (weights, prior). Varied: the truth
$\mathbf{m}_{\text{true}}$ over a family of patterns.

The output is a property of (operator, noise, regularisation), never of the
Earth.

---

## ★2 — Reading the table

| period | 2 | 3 | 4 | 6 | 8 | 12 | 16 |
|---|---|---|---|---|---|---|---|
| amplitude | 0.0012 | 0.0045 | 0.5680 | **0.9332** | 0.9875 | 0.9983 | 1.0004 |

Smallest period above 0.9: **6 cells** (0.9332).
Largest period below 0.01: **3 cells** (0.0045).
(Period 2 gives 0.0012, also below 0.01.)

---

## ★3 — Two spikes 2 cells apart

The PSF has half-width 3 cells, so two spikes separated by 2 cells are inside one
PSF width: they merge into a single broad anomaly of amplitude up to about
$2\times0.3222 = 0.6444$ (less if the overlap reduces the sum). The image shows
**one** feature, not two, and reporting "two bodies" from it would be a
resolution failure. The honest report is one body of width ≈ the PSF width.

---

## ★4 — Additional numbers for the 8-cell claim

Required: (i) the **noise level** at which 0.9875 was measured, and (ii) the
**regularisation weight** (or the PSF half-width) that the production inversion
used. Without them the number describes an unspecified experiment.

A reason the conclusion could still be wrong: the pattern may have been
well-aligned at period 8; the alignment sweep for period 4 shows recovery
falling from 0.5683 to 0.0009 with shift, so a single alignment is not evidence
about all patterns. The worst recovery over shifts is the honest number.

---

## ★5 — Worst-to-best ratio for period 4

Best: 0.5691 (shift 2.0). Worst: 0.0009 (shift 1.0).

$$\text{ratio} = \frac{0.5691}{0.0009} = 6.3\times10^{2} .$$

The single number to report is the **worst** recovery, 0.0009, with the
statement that period-4 structure is recoverable only when it is not aligned with
the operator's null direction — i.e. that period-4 recovery is not reliable. A
curve of amplitude versus shift (or a suite of random patterns) is better than
either endpoint.

---

## ★6 — Testing a negative anomaly

Compute the point-spread function for the cell where the negative anomaly
appears, by taking the corresponding row of $R$ (or by passing a unit spike at
that cell through the identical experiment and inversion).

Threshold: the anomaly is an artifact if its amplitude is comparable to or
smaller than the PSF's most negative sidelobe — here $|{-0.0531}|$ times the
amplitude of the adjacent positive feature. Concretely, for a neighbouring peak
of amplitude $A$, a trough shallower than $0.0531A$ is within the PSF's
ringing and must not be reported as structure. A trough substantially deeper
than that requires an independent test (a different regularisation, or a
targeted forward model) before it can be called real.

---

## ★7 — A resolution suite without checkerboards

For a layered target, for example:

- **Patterns:** (i) single thin layers of thickness $h$ at a range of depths;
  (ii) step changes in property at a range of depths; (iii) random layered models
  drawn from a stated distribution; (iv) layer pairs with a gap $g$ between them.
- **Metrics:** recovered thickness/amplitude ratio for (i); recovered step
  position error and edge width for (ii); error versus depth and versus mean
  layer thickness for (iii); minimum separable gap $g_{\min}$ for (iv);
  point-spread half-width as a single summary.
- **Decision rule:** "resolved to within $X$ km" holds if the recovered position
  error is below $X$ for at least 90% of the patterns at the production noise
  level, *and* the recovered amplitude is above 0.5 of the truth. Report the
  fraction of patterns failing, not only the successes.

---

## ★8 — Amplitude above 1

The inversion is linear: $\hat{\mathbf{m}} = M\mathbf{d}$ with
$M = (G^{T}G/\sigma^2 + P_0)^{-1}G^{T}/\sigma^{2}$. A long-wavelength pattern is
dominated by low-order directions where the smoothness prior adds little; the
recovered amplitude of such a pattern can exceed the truth because the operator's
columns overlap, so the inversion can concentrate energy into a pattern that the
prior treats as "free", slightly over-shooting (a Gibbs-like effect amplified by
the prior's relative weakness at low order, plus noise).

Consequence for the metric: amplitude recovery is a *relative* indicator whose
interesting range is where it falls steeply (here between periods 3 and 6). Its
value near 1 at long periods and its small excursions above 1 carry no
information; the resolution length is read where the curve crosses ~0.5, and the
report should state that convention.
