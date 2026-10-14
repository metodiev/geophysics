# Solutions — 20-07-03 Sparse Representations for Seismic Data

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output.

Lesson: [03 Sparse Representations for Seismic Data](../03-sparsity-seismic.md).

---

## ★1 — Representation versus inversion

A **sparse representation** claim says the signal is well approximated by $k$
atoms of a dictionary; it is a statement about the dictionary and the signal,
and it can be tested on complete data. A **sparse inversion** claim says those
coefficients can be recovered from the data actually acquired; it is a statement
about the dictionary, the signal *and* the sensing operator, and the governing
quantity is the coherence. A dictionary can satisfy the first and fail the
second (the Gabor dictionary here: error 0.000 at $k = 16$, coherence 0.9610).

---

## ★2 — Redundancy and orthogonality

Redundancy $= p/n = 1130/256 = 4.41$.

In $\mathbb{R}^{n}$ at most $n$ vectors can be mutually orthogonal and nonzero.
With $p > n$ atoms, the Gram matrix $D^{T}D$ is $p \times p$ with rank at most
$n$, so it has at least $p - n = 874$ zero eigenvalues; at least one pair of
atoms must therefore have a nonzero inner product, i.e. $\mu > 0$. Redundancy
and coherence are the same statement seen from two sides.

---

## ★3 — Which dictionary for which purpose

**Recovery from 50 % of samples: Haar (or Fourier)**, i.e. an orthonormal basis.
The reason is coherence, not approximation: with $\mu \approx 9\times10^{-17}$ the
sensing matrix is well conditioned on any support, whereas $\mu = 0.9610$ means
overlapping shifted wavelets are nearly indistinguishable from a limited sample
set, and recovery would need far more measurements than the sparsity alone
suggests.

**Denoising a complete trace: Gabor.** With all samples present there is no
conditioning penalty, and the measured output SNR was 29.02 dB against 19.78 dB
(Fourier) and 19.23 dB (Haar) — the approximation power is what counts.

The two answers differ, which is the lesson: the criterion for a representation
is error, the criterion for an inversion is coherence, and a single dictionary
rarely optimises both.

---

## ★4 — Halving the error by doubling $k$

| dictionary | $E_{16}$ | $E_{32}$ | ratio $E_{32}/E_{16}$ |
|---|---|---|---|
| Fourier | 0.5436 | 0.3750 | 0.690 |
| Haar | 0.5865 | 0.3990 | 0.680 |
| Gabor | 0.0000 | 0.0000 | undefined |
| random | 0.8095 | 0.6769 | 0.836 |

The orthonormal bases and the random dictionary all reduce their error by about
30 % for a factor 2 in coefficients — a slow, roughly power-law decay, as
expected for a non-sparse signal in a fixed basis. The Gabor ratio is undefined
because both errors are at machine precision: the trace is *exactly* 14 atoms in
that dictionary. The comparison measures the difference between a signal that is
sparse in the dictionary and one that is merely compressible in it.

---

## ★5 — The hidden budget failure

A fixed-$k$ rule would apply the same 64-atom budget to both dictionaries, and
the outputs would be recorded as "Gabor: 29.02 dB; random: 6.78 dB" — a quality
difference. It would not reveal that the two runs stopped for different reasons:
the Gabor run stopped because further atoms would fit noise, and the random run
went to the budget limit without ever reaching the noise floor. The number of
iterations is the same and the meaning is opposite.

Diagnostics to report: the **residual trajectory** (relative residual versus
iteration, or the iteration at which the residual first fell below the measured
noise level, and whether it did); the **noise level** used; and explicitly
whether the stopping criterion fired. A run in which the criterion never fires
should be flagged as incomplete, not reported as a result.

---

## ★6 — The winning mechanism, and when it fails

Mechanism: a 15 Hz Ricker is a smooth, narrowband-in-time wavelet, and the
dictionary contains 10 Hz and 20 Hz atoms at every sample position. Overlapping
a 10 Hz atom with a 20 Hz atom of the right relative amplitude and sign
reproduces a 15 Hz Ricker closely, so the Gabor dictionary remains a good
approximation even though the exact atom is absent. The exactness is gone (0.000
becomes 0.057 at $k = 32$), but the family advantage survives.

A generator for which Gabor would lose: any signal whose atoms are *outside the
family's shapes* — the demonstration's own examples are the tone (error 0.000
with 2 Fourier coefficients, against Gabor 0.797 at $k = 8$) and the step (8
Haar coefficients, error $1.1\times10^{-15}$, against Gabor 0.958 at $k = 8$).
A dispersive or phase-rotated wavelet would be a realistic seismic example of
the same failure.

---

## ★7 — Held-out evaluation: specification

**Generators.** (i) spikes convolved with a 30 Hz Ricker (matching the
dictionary), (ii) spikes convolved with a 15 Hz Ricker (near-match), (iii)
spikes convolved with a 70 Hz Ricker (outside the dictionary band).

**Split.** For each generator, 200 traces of 256 samples. Draw 100 for
*dictionary fitting* (for a fixed dictionary this stage is a no-op and is
included to make the protocol honest) and 100 for *scoring*, with disjoint
random seeds.

**Metric.** Best $k$-term relative error at $k \in \{4, 8, 16, 32, 64\}$,
averaged over the 100 scoring traces, reported as a median with the interquartile
range. Also report the coherence of each dictionary.

**Trials.** 100 scoring traces per generator; the spread across traces is
reported, not hidden by the mean.

**Ambiguity.** If two dictionaries are within the interquartile range of each
other at every $k$, report the pair and the metric value rather than declaring a
winner; a difference smaller than the spread is not a difference.

**What changes.** The demonstration's §2 table used the trace the dictionary was
built from, giving error 0.0000 at $k = 16$. Held out, the same generator would
give a small nonzero median (0.00–0.02 depending on the draw), and the
**spread** would become visible where the in-sample table showed a bare zero.
That is the whole reason for the protocol.

---

## ★8 — How far exactness survives a wrong generator

**Design.** Fix the dictionary (atoms at 10, 20, 30, 40, 50 Hz). Vary the
generator's Ricker frequency from 30 Hz in 1 Hz steps down to 5 Hz and up to
55 Hz. For each, generate 50 traces (fixed spike positions across the sweep, so
that only the wavelet changes) and record the median $k = 16$ approximation
error from OMP.

**Predicted shape.** A flat minimum of 0.000 over a plateau of roughly
$\pm\frac{1}{2}$ the atom spacing ($\pm 5$ Hz, i.e. $\pm 2$ steps), a steep rise
where the generator frequency falls midway between two atoms (at 15 and 25 Hz
the error rises to the 0.05–0.1 range observed in the table), and a slow decay
back towards the Fourier/Haar level beyond the dictionary band (above 55 Hz,
below 10 Hz), where the dictionary contributes nothing and the error approaches
0.6–0.9 at $k = 16$.

**Width-setting parameter.** The ratio of the atom frequency spacing (10 Hz) to
the Ricker bandwidth. A Ricker of frequency $f$ has a spectrum peaking at $f$
with a width of order $f/\sqrt{2}$, so the plateau is wide when the spacing is
small compared with the bandwidth and collapses to nothing when the spacing
exceeds it. Equivalently: the plateau width is set by the **coherence** between
neighbouring-frequency atoms — high coherence means each atom can substitute for
its neighbour, which is exactly the property that made Gabor both a good
approximator and a poor recovery dictionary.
