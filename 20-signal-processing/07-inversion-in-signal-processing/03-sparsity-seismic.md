---
id: 20-07-03
title: "Sparse Representations for Seismic Data"
level: research
prereqs: ["20-07-01", "20-07-02", "20-02-06"]
tags: [signal-processing, time-series, sparse-representation, dictionaries, seismic, atoms]
---

# Sparse Representations for Seismic Data

**All models and data in this module are SYNTHETIC.** Every trace below is a
chosen spike train convolved with a chosen wavelet, plus seeded noise. No field
record, survey or published figure is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a *representation* from an *inversion*: choosing a
   transform in which a signal has few coefficients, versus solving for those
   coefficients from incomplete or noisy data.
2. **Compute** the best $k$-term approximation error in an orthonormal basis and
   **measure** it for a redundant dictionary by orthogonal matching pursuit.
3. **Explain** the redundancy–coherence trade-off and **state** why a redundant
   dictionary can approximate better and recover worse at the same time.
4. **Measure** denoising gain in three dictionaries at a fixed noise level and
   **identify** the one that fails, with the reason.
5. **Demonstrate** that the winning dictionary changes with the generator, and
   **state** the circularity of testing a dictionary on data generated from it.
6. **Specify** a defensible dictionary-selection procedure that does not depend
   on knowing the answer.
7. **State** the assumptions under which a sparse representation claim about
   seismic data is meaningful.

## Prerequisites

- [20-07-01 Sparse and L1 Deconvolution](01-sparse-deconvolution.md) — sparsity,
  shrinkage and the optimality conditions.
- [20-07-02 Compressive Sensing and Data Reconstruction](02-compressive-sensing-signals.md)
  — coherence and the sampling conditions that make recovery possible.
- [20-02-06 Wavelet Transforms and Multiresolution Analysis](../02-fourier-and-spectral-analysis/06-wavelet-analysis.md)
  — multiresolution bases and why a narrow basis function localises a
  discontinuity.

The runnable companion is
[`code/sparse_representations_demo.py`](code/sparse_representations_demo.py); the
graded problems are in
[`exercises/03-sparsity-seismic-exercises.md`](exercises/03-sparsity-seismic-exercises.md).

## 1. Representation versus inversion

A **sparse representation** claim is: *the signal is well approximated by $k$
atoms of a dictionary $D$.* An **inversion** claim is: *the coefficients of the
signal in $D$ can be recovered from the data I have.* The two are related but
not the same, and confusing them is the central error this lesson is written to
prevent. Approximation quality is about the dictionary; recovery is about the
dictionary **and** the sensing operator. This lesson measures approximation in
§2–§3 and the practical consequence in §4–§5.

The object of study is a dictionary $D \in \mathbb{R}^{n \times p}$ with
$p \ge n$: redundant, so that atoms outnumber samples. The $k$-term
approximation error is

$$
E_k(s) = \min_{\lVert x \rVert_0 \le k}
\frac{\lVert D x - s \rVert_2}{\lVert s \rVert_2},
$$

and for an orthonormal basis (where $p = n$) the minimiser is simply the $k$
largest coefficients. For a redundant dictionary the problem is combinatorial and
one uses a greedy method; the demonstration uses orthogonal matching pursuit
(OMP), which selects atoms one at a time and refits all selected coefficients by
least squares at each step.

## 2. Four dictionaries on one synthetic trace

The trace is 256 samples at $\Delta t = 4\ \mathrm{ms}$ (1.02 s) made from 14
spikes convolved with a 30 Hz Ricker wavelet, with Gaussian noise at a measured
rms of 0.02189, i.e. an input signal-to-noise ratio of 20.00 dB.

| dictionary | atoms | redundancy | comment |
|---|---|---|---|
| real Fourier basis | 256 | 1.00 | orthonormal |
| Haar wavelet basis | 256 | 1.00 | orthonormal, $\max\lvert HH^{T}-I\rvert = 3.3\times10^{-16}$ |
| Ricker/Gabor | 1130 | 4.41 | 5 frequencies (10–50 Hz) $\times$ 226 positions |
| random Gaussian | 512 | 2.00 | a control, for coherence |

Then the best $k$-term relative error, measured on the **clean** trace:

| $k$ | Fourier | Haar | Ricker/Gabor | random |
|---|---|---|---|---|
| 4 | 0.7869 | 0.7989 | 0.6206 | 0.9419 |
| 8 | 0.6727 | 0.7023 | 0.2652 | 0.8984 |
| 16 | 0.5436 | 0.5865 | **0.0000** | 0.8095 |
| 32 | 0.3750 | 0.3990 | 0.0000 | 0.6769 |
| 64 | 0.1792 | 0.2090 | 0.0000 | 0.4654 |

The Gabor dictionary reaches zero at $k = 16$: 16 atoms represent 14 spikes
exactly, because the spikes really are Ricker wavelets of the frequencies in the
dictionary. The orthonormal bases need 64 coefficients to reach 0.18 — they are
still far from exact at the largest $k$ tested. The random dictionary is worse
than every structured option, as it must be: a random atom has no reason to
resemble a seismic wavelet.

**This table is an advertisement, not evidence.** The dictionary was built from
the wavelet that generated the data, at the generating frequency, on the
generating grid. Understanding what the number means requires the control
experiment of §5.

## 3. Redundancy buys approximation and costs coherence

The measured mutual coherence (the largest normalised inner product between
distinct columns) is:

| dictionary | coherence |
|---|---|
| Fourier basis | $1.7\times10^{-14}$ |
| Haar basis | $9.0\times10^{-17}$ |
| Ricker/Gabor | **0.9610** |
| random | 0.2861 |

The Gabor dictionary is the best approximator **and** by far the most coherent:
two Ricker atoms at the same frequency, four samples apart, overlap almost
completely, and their normalised inner product approaches one. Redundancy and
coherence are two sides of the same coin: to add atoms you must add atoms that
resemble the ones you have.

The consequence is exactly the previous lesson's rule. Approximation is governed
by how well atoms match the signal; recovery is governed by coherence. A
dictionary can win the first and lose the second, and for *sparse recovery* of a
seismic record from incomplete data the Gabor dictionary would be a poor choice
precisely because of its 0.9610. The demonstration's OMP does succeed here
because the data are complete; with 50 % of samples missing, the same dictionary
would need far more measurements than its coherence permits.

Orthonormal bases sit at the other end: coherence is numerically zero, so
recovery from a random subset of samples is well conditioned, but the
representation is never exactly sparse for a wavelet-shaped signal. The
practitioner's choice is between these two failure modes, not above them.

## 4. Denoising by coefficient selection, measured

Take the noisy trace (input SNR 20.00 dB) and select coefficients in each
dictionary, then measure the output SNR against the clean trace:

| dictionary | selection rule | coefficients kept | output SNR |
|---|---|---|---|
| Fourier | hard threshold at $3\sigma$, $\sigma = 0.02189$ | 92 of 256 | 19.78 dB |
| Haar | hard threshold at $3\sigma$ | 106 of 256 | 19.23 dB |
| Ricker/Gabor | OMP stopped when the relative residual reaches the noise | 12 atoms | **29.02 dB** |
| random | OMP stopped when the relative residual reaches the noise | 64 atoms | **6.78 dB** |

Three separate lessons are in this table.

- The matched dictionary improves the signal-to-noise ratio by 9 dB, from 20.00
  to 29.02. The 12 atoms it kept are close to the 14 true spikes, and the count
  is a measurement of the effective sparsity of *this* trace, not a constant of
  the method.
- The orthonormal bases each improve it by a fraction of a decibel. Thresholding
  a global basis removes noise from every coefficient at once, which is a small
  and safe gain.
- The random dictionary makes things **worse**: 6.78 dB against 20.00 dB in.
  With no sparsity to exploit, the greedy procedure spends its 64-atom budget
  fitting noise. A sparse model applied in the wrong domain does not fail
  gracefully; it fails actively.

The stopping rule deserves a comment, because it is where most applied mistakes
live. OMP was stopped when the residual reached the measured noise level, i.e.
when further atoms would be fitting noise. For the random dictionary that
happened *never* in 64 iterations, so the algorithm used its whole budget. A
fixed-$k$ rule would have hidden this: both dictionaries would have been
"used with $k = 64$", and the difference between them would have looked like a
quality difference rather than what it is — a failure of the stopping criterion
to fire.

## 5. The trap: the winner depends on the generator

Four synthetic signals of the same length were approximated in all four
dictionaries. The smallest error at each $k$ is in bold.

| generator | $k$ | Fourier | Haar | Ricker/Gabor | random | winner |
|---|---|---|---|---|---|---|
| 14 spikes $\times$ Ricker 30 Hz | 8 | 0.673 | 0.702 | 0.265 | 0.898 | Gabor |
| | 32 | 0.375 | 0.399 | **0.000** | 0.677 | Gabor |
| 10 spikes $\times$ Ricker 15 Hz (not in dictionary) | 8 | 0.581 | 0.673 | 0.358 | 0.857 | Gabor |
| | 32 | 0.155 | 0.330 | 0.057 | 0.639 | Gabor |
| a single tone, bin 16 | 8 | **0.000** | 0.896 | 0.797 | 0.868 | Fourier |
| | 32 | **0.000** | 0.458 | 0.327 | 0.649 | Fourier |
| a step of 96 samples | 8 | 0.177 | **0.000** | 0.958 | 0.869 | Haar |
| | 32 | 0.089 | **0.000** | 0.837 | 0.651 | Haar |

The winner changes with the generator: Fourier for the tone, Haar for the step,
Gabor for the wavelet trains. Two exactly-sparse facts sit behind the extreme
rows, and both are exact rather than approximate:

- the tone is **2 Fourier coefficients**: error at $k = 2$ is
  $4.0\times10^{-15}$, i.e. machine precision.
- the step is **8 Haar coefficients**: error at $k = 8$ is
  $1.1\times10^{-15}$.

The 15 Hz Ricker train is the informative row. Its wavelet is *not* in the
dictionary, and the Gabor dictionary still wins — because a 15 Hz Ricker is
approximated by overlapping 10 Hz and 20 Hz atoms. But the margin collapses: the
dictionary that was exact (error 0.000) on the in-dictionary case reaches only
0.057 at $k = 32$ when the generator is absent. A dictionary built for one
signal class generalises to neighbouring classes and degrades outside them; the
rate of degradation is a property of the signal class, and can only be measured
against generators the dictionary was not built from.

### 5.1 A selection procedure that is not circular

The trap of §2 is that the dictionary was chosen by someone who knew the
generator. A defensible procedure, in the order the decisions must be made:

1. **Fix the dictionary set before looking at the evaluation data**, and record
   the atoms and their parameters.
2. **Hold out data.** Split records (or gathers) into a part used to fit the
   dictionary and a disjoint part used to score it. The demonstration's §2 is
   the in-sample case; the 15 Hz row is the held-out case.
3. **Score on the held-out part** with a metric fixed in advance (relative
   $k$-term error, or output SNR after a fixed selection rule), and report the
   $k$ at which it is measured.
4. **Report the coherence alongside the error**, because it predicts whether the
   representation will survive incomplete sampling.
5. **Report the number of atoms and the redundancy**, so that a reader can see
   the cost that bought the improvement.

Without steps 2 and 3 the exercise measures the experimenter, not the Earth.

## 6. Assumptions and regime of validity

1. **The atoms are unit-norm and the dictionary is fixed.** A dictionary whose
   normalisation or atom set is tuned per record is a different method, and its
   apparent sparsity is partly fitted.
2. **$p = O(n)$.** At 4.4× redundancy the coherence is already 0.9610; larger
   dictionaries are worse, and the linear-programming recovery guarantee
   degrades accordingly. Redundancy is not free.
3. **The noise is white and its level is known.** Every stopping rule here uses
   the measured $\sigma = 0.02189$; with coloured noise the residual test fires
   at the wrong iteration, and the failure is silent.
4. **The signal is a superposition of atoms from one family.** An Ormsby
   wavelet, a dispersive arrival or a converted phase is outside all four
   dictionaries tested.
5. **OMP is a heuristic for the $\ell_0$ problem.** It is greedy, and it can
   select a correlated atom and never recover; no optimality claim is made for
   its output. The $\ell_1$ route of lesson 01 has a convexity guarantee that
   OMP does not.
6. **Everything is SYNTHETIC and 1-D.** A real seismic section has spatial
   coherence that a per-trace dictionary ignores, and the reductions available
   from 3-D or transform-domain dictionaries are not measurable from this
   experiment.

## Mastery checkpoint

Without notes: **(a)** define $E_k$ for a redundant dictionary and state why OMP
rather than sorting is required; **(b)** from §3, explain in two sentences why
the best-approximating dictionary is the worst for recovery from incomplete
data; **(c)** from §4, state the measured output SNR for each dictionary and
identify which one fails, with the mechanism; **(d)** using §5, state which
dictionary wins for a step and why that is an exact rather than an approximate
result; **(e)** write the five steps of §5.1 from memory and say which one the
§2 table omits.

A worked answer to (a)–(d) appears in the
[solutions](exercises/03-sparsity-seismic-solutions.md).

## Common pitfalls

1. **Scoring in-sample.** The §2 table is the positive control for this
   lesson, not its result.
2. **Reporting approximation error without coherence.** A reader cannot tell
   from $E_k$ alone whether the representation will survive missing traces.
3. **A fixed-$k$ stopping rule that never fires.** §4's random dictionary uses
   its whole budget; the run looks successful and the output is worse than the
   input.
4. **Assuming a bigger dictionary is better.** Redundancy raises coherence and
   hurts recovery; the demonstration measures both sides.
5. **Forgetting that "sparse in the right domain" is a model statement.** The
   same trace is sparse in one dictionary and dense in another, and the data do
   not choose.
6. **Comparing dictionaries of different sizes without saying so.** 1130 atoms
   against 256 is a different budget; report $p$, $n$ and the redundancy.

## Related modules

- [20-07-01 Sparse and L1 Deconvolution](01-sparse-deconvolution.md) — the
  convex route to the same representation problem.
- [20-07-02 Compressive Sensing and Data Reconstruction](02-compressive-sensing-signals.md)
  — coherence as the bridge between representation and recovery.
- [20-02-06 Wavelet Transforms and Multiresolution Analysis](../02-fourier-and-spectral-analysis/06-wavelet-analysis.md)
  — where the Haar basis of this lesson comes from and what its relatives do.
- [20-04-02 Spiking Deconvolution and Wavelet Estimation](../04-deconvolution-and-inverse-filtering/02-spiking-deconvolution.md)
  — the classical route to a spike train, without a dictionary.
