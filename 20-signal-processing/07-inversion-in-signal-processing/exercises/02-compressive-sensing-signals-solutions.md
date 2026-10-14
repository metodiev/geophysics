# Solutions — 20-07-02 Compressive Sensing and Data Reconstruction

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output.

Lesson: [02 Compressive Sensing and Data Reconstruction](../02-compressive-sensing-signals.md).

---

## ★1 — Coherence of a two-column matrix

$\lVert a_1\rVert = 1$. For $\varepsilon = 0.5$:
$\lVert a_2\rVert = \sqrt{1 + 0.25} = 1.1180$, $a_1^{T}a_2 = 1$, so
$\mu = 1/1.1180 = \mathbf{0.8944}$.

For $\varepsilon = 0$: $a_2 = a_1$, $\lVert a_2\rVert = 1$, $a_1^{T}a_2 = 1$, so
$\mu = \mathbf{1.000}$ — the two columns are identical. The data cannot
distinguish them at any noise level, and no sparsity prior helps: the two
hypotheses are the same hypothesis. This is what the stride-4 mask does to the
Fourier dictionary (measured coherence 1.000 in the lesson).

---

## ★2 — Why stride-4 sampling aliases exactly

With $n = 128$ and $m = 32$, the sampling interval is 4 samples, so the
subsampled Nyquist frequency is $1/(2\times4) = 0.125$ cycles/sample and the
sampled band contains only $m/2 = 16$ positive frequencies. Sampled at $t = 4j$,

$$
\cos\!\left(2\pi \frac{k \cdot 4j}{128}\right)
= \cos\!\left(2\pi \frac{(k \bmod 32) j}{32}\right),
$$

so two frequencies $k$ and $k'$ produce identical sampled columns whenever
$k \equiv k' \pmod{32}$. The stride-4 sampling folds the 128-point grid onto a
32-point grid, and $\mu = 1$ follows immediately. Random sampling does not
possess such congruences, and the measured coherence falls to 0.528.

---

## ★3 — Smallest $m$ for exact recovery

| $k$ | smallest $m$ (3/3) | $m/k$ |
|---|---|---|
| 4 | 24 | 6.0 |
| 8 | 40 | 5.0 |

The $m/k$ ratio falls with $k$, which is the observable signature of
$m \propto k\log(n/k)$: $k\log(n/k)$ is 13.9 at $k = 4$ and 22.2 at $k = 8$,
a rise by a factor 1.6, while $m$ rises by a factor 40/24 = 1.67. Both
quantities track each other; neither establishes the constant.

---

## ★4 — Verifying the alias pair

The true tone is at $f = 40/128 = 0.3125$ cycles/sample. Under stride-4
sampling the sampled column of bin $k$ is determined by $k \bmod 32$:

- bin 40: $40 \bmod 32 = 8$; frequency $8/128 = 0.0625$ cycles/sample.
- bin 24: $24 \bmod 32 = 24$; frequency 0.1875.
- bin 8: $8 \bmod 32 = 8$; same sampled column as bin 40.
- bin 56: $56 \bmod 32 = 24$; same sampled column as bin 24.

So the four bins fall into two alias classes, $\{8, 40\}$ and $\{24, 56\}$, both
present in the measured set, and all four fit the 32 samples with residual
$< 10^{-8}$. The reported L1 amplitudes (0.691 at bin 40, 0.404 at bin 8,
$-0.199$ at bin 56) are one arbitrary split within the classes.

---

## ★5 — Shape of the error surface

Grid: $k \in \{1,\dots,6\}$, $m \in \{16,24,32,40,48,64,80\}$, 42 cells.

Counting cells whose median is exactly 0.000: $k = 1,2,3$ contribute 7 each
(21), $k = 4$ contributes 6 (the cell at $m = 16$ is 0.913), $k = 5$ contributes
6 (0.625 at 16), $k = 6$ contributes 6 (1.091 at 16). Total $21 + 6 + 6 + 6 = 39$
of 42, i.e. **92.9 %**.

The flat zero is not a small error; it is exact recovery to machine precision
after the debiasing step, because once the support is identified correctly the
problem is a square or overdetermined least-squares system on $k$ unknowns,
which is solved exactly. The surface therefore has two plateaux and a cliff, and
the "median error" summary hides that the only interesting quantity is where the
cliff is.

---

## ★6 — Can $m = 12$ identify $k = 2$?

Measured restricted eigenvalues at $k = 2$, $m = 12$: minimum 0.0760, maximum
0.1246. Both are positive, so the restricted Gram is invertible and the two
coefficients are identifiable from those 12 samples — and the phase-transition
table agrees: $k = 2$ succeeds in 3/3 trials at $m = 16$ (the smallest grid
value) and thus certainly could at 12.

Caveat: the eigenvalues are far below 1. Normalising the dictionary in the full
space means restricting to $m$ of $n$ rows scales the Gram by about $m/n = 12/128
= 0.094$, close to the observed 0.0760–0.1246. The property that matters for
recovery is that the *ratio* of largest to smallest restricted eigenvalue stays
bounded, not that either equals 1; a value of 0 would mean failure, and a value
far from 1 is not evidence of failure.

---

## ★7 — Noise-dependent transition: specification

**Noise level.** Gaussian, added to the samples (not to the coefficients), at
0 %, 5 %, 10 % and 20 % of the sample rms, in four separate sweeps.

**Success criterion.** Relative coefficient error $< 0.15$ after debiasing —
looser than the noiseless threshold of $10^{-6}$, because with noise an exact
recovery is impossible and a threshold below the noise-induced floor would
report success rates of zero everywhere.

**Grid.** $k \in \{1,\dots,8\}$ in steps of 1, $m \in \{8, 12, 16, 24, 32, 40,
48, 64, 80, 96, 112\}$, 15 trials per cell (the criterion is noisy, and 15
trials give a standard error of about 0.13 on a proportion near 0.5).

**Prediction.** The transition band moves to larger $m$ and becomes wider as the
noise rises; the location of the 50 % contour moves up roughly linearly in $k$
along $m = C(k\log(n/k) + \text{const}\cdot\text{SNR}^{-1})$. The **width** of
the band grows more than its location moves, because noise randomises which
supports are recoverable, so cells become partly successful rather than all-or-
nothing.

**More sensitive quantity.** The bandwidth, not the position. The position is a
resampling-noise-limited estimate; the width reflects the mechanism (the
distribution of restricted eigenvalues across supports) and is where a model of
the failure will show first.

---

## ★8 — Without the debiasing step

Soft thresholding leaves every surviving coefficient shrunk by
$\lambda/L$, and the gradient of the shrinkage depends on the local amplitude.
Without debiasing the error would be a smooth, monotone function of $(k, m)$:
different supports would still give different errors, and the "all-or-nothing"
signature would be replaced by a gradient from about $10^{-1}$ (support wrong)
through $10^{-2}$ (support right, amplitudes shrunk). The transition would be a
blur because the two effects — wrong support, shrunken amplitude — overlap in
magnitude and cannot be separated from the error alone.

What debiasing costs with noise: it removes the shrinkage bias (good) and
amplifies whatever noise lies along the identified support (bad). On a wrong
support it is much worse than the L1 solution, because unpenalised least squares
will fit the noise at the wrong atoms with large coefficients. The standard
compromise is a partially debiased or nonconvex step, at the price of
reintroducing a nonconvex problem.
