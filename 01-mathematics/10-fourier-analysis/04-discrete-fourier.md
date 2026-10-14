---
id: 01-10-04
title: "Discrete Fourier Transform and the FFT"
level: advanced
prereqs: ["01-10-02", "01-10-03"]
estimated_minutes: 90
tags: [dft, fft, normalisation, numerical-algorithms, spectral-estimation]
---

# Discrete Fourier Transform and the FFT

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the DFT and its inverse from the definition, with an explicit,
   consistent normalisation and sign convention.
2. **Compute** a small DFT by hand and verify a round trip numerically.
3. **Explain** why the transform is reversible, and what the $1/N$ in the inverse
   is doing there rather than in the forward transform.
4. **Distinguish** the bin spacing $df = 1/(N\,dt)$ from the resolution $1/T$, and
   demonstrate numerically that zero padding interpolates but does not resolve.
5. **Recover** the amplitude of a real sinusoid from a spectrum correctly,
   including the factor 2 for a one-sided spectrum and the treatment of the DC
   and Nyquist bins.
6. **State** the cost of the direct DFT ($N^{2}$ complex operations) and of the
   radix-2 FFT ($(N/2)\log_2N$ butterflies), and verify the cost models by
   measurement.

## Prerequisites

[01-10-02 The Fourier Transform and Its Properties](./02-fourier-transform.md) —
the continuous transform, its normalisation and the bridge to the sampled case;
[01-10-03 Convolution, Filtering and the Convolution Theorem](./03-convolution.md) —
because the FFT's commercial importance is largely convolution, and because
circular wrap-around is the same phenomenon as un-padded convolution.

## 1. Intuition: the continuous transform cannot be computed

The Fourier transform of a record is an integral over an infinite domain. Three
things must happen before a computer can evaluate it:

1. the signal must be **sampled**, replacing $t$ by $n\,dt$;
2. the record must be **finite**, replacing the infinite integral by a sum over
   $N$ samples;
3. the frequency variable must be **discretised**, because a sum over $N$ samples
   can only determine $N$ independent numbers.

Steps 1 and 2 are approximations that introduce aliasing and leakage
([01-10-05](./05-windowing-aliasing.md)). Step 3 is *not* an approximation: the
$N$ values $X[k]$ determine the $N$ samples $x[n]$ exactly, and vice versa. The
DFT is a change of basis, and it is lossless. This is worth dwelling on, because
it is the reason processing in either domain is legitimate: you are not
approximating, you are looking at the same object in two coordinate systems.

## 2. Definitions, exactly

### 2.1 The transform pair

$$\boxed{\;X[k] = \sum_{n=0}^{N-1}x[n]\,e^{-2\pi i kn/N},
\qquad
x[n] = \frac{1}{N}\sum_{k=0}^{N-1}X[k]\,e^{+2\pi i kn/N}.\;}$$

Every symbol matters:

- The **forward** transform uses the negative exponent and carries **no**
  scaling. This matches the continuous convention of
  [01-10-02](./02-fourier-transform.md), so the property table there applies
  unchanged.
- The **inverse** carries the $1/N$. Putting it there (rather than splitting it
  as $1/\sqrt{N}$ between the two) makes the forward transform equal to a sum, so
  $X[0] = \sum_n x[n]$ — the sum of the samples, *not* their mean. Every
  "factor of $N$" error in practice is a confusion between the sum and the mean.
- The **bin frequencies** are $f_k = k/(N\,dt)$ for $k = 0,\ldots,N-1$; the
  spacing is $df = 1/(N\,dt) = 1/T$ where $T$ is the record length.

### 2.2 What the bins mean

For $N$ even (the usual case for the radix-2 FFT), bins
$k = 1,\ldots,N/2-1$ are the **positive** frequencies, bin $k = N/2$ is the
**Nyquist** frequency $1/(2\,dt)$, and bins $k > N/2$ are the **negative**
frequencies $f_{k-N}$ (equivalently, $\mathrm{fftshift}$ moves zero to the
middle). The demo's sign-convention test on a 64-sample record with $dt = 0.125$ s
shows this directly:

| input | $\lvert X[8]\rvert$ | $\lvert X[56]\rvert$ |
|---|---|---|
| $e^{+2\pi i\cdot1\cdot t}$ (all energy at $+1$ Hz) | 64.000 | 0.000 |
| $\cos(2\pi\cdot1\cdot t)$ (energy at both $\pm1$ Hz) | 32.000 | 32.000 |

with $k_0 = 8$ corresponding to $f = 1$ Hz. Using the opposite kernel
$e^{+2\pi ikn/N}$ mirrors the answer — $\lvert X[8]\rvert = 0$ and
$\lvert X[56]\rvert = 64$ — with a maximum difference of $6.4\times10^{1}$ from
the standard result, i.e. everything swapped.

### 2.3 A worked transform

For $x = [1,2,3,4,4,3,2,1]$ ($N = 8$):

| $k$ | $X[k]$ |
|---|---|
| 0 | $20.000000 + 0.000000i$ |
| 1 | $-5.828427 - 2.414214i$ |
| 2 | $0.000000 - 0.000000i$ |
| 3 | $-0.171573 - 0.414214i$ |
| 4 | $0.000000 - 0.000000i$ |
| 5 | $-0.171573 + 0.414214i$ |
| 6 | $0.000000 - 0.000000i$ |
| 7 | $-5.828427 + 2.414214i$ |

Three things to read off it.

1. $X[0] = 20$ equals the sum of the samples, and $X[7] = \overline{X[1]}$,
   $X[6] = \overline{X[2]}$, $X[5] = \overline{X[3]}$: the sequence is real, so
   the spectrum is Hermitian.
2. Three bins ($k = 2, 4, 6$) are zero. This sequence is palindromic about the
   half-integer index $n = 3.5$, and the even components of the DFT basis are
   orthogonal to it.
3. The phase is an exact linear ramp: for $k = 1, 3, 5, 7$ the demo prints
   $-157.5000^\circ$, $-112.5000^\circ$, $112.5000^\circ$ and $157.5000^\circ$,
   matching $-2\pi k(3.5)/8$ at every one of those bins. That ramp *is* the shift
   property: a sequence symmetric about $n = 3.5$ is a zero-centred symmetric
   sequence shifted by 3.5 samples.

The round trip $x \to X \to x$ reproduces the input with a maximum error of
$4.4\times10^{-16}$.

## 3. Why it is reversible, and what $1/N$ is doing

The inverse formula is not magic. Substitute the forward definition into it:

$$\frac{1}{N}\sum_{k=0}^{N-1}\left(\sum_{m=0}^{N-1}x[m]e^{-2\pi ikm/N}\right)e^{+2\pi ikn/N}
= \sum_{m=0}^{N-1}x[m]\underbrace{\left(\frac{1}{N}\sum_{k=0}^{N-1}
e^{2\pi ik(n-m)/N}\right)}_{\delta_{nm}} .$$

The inner sum is a geometric series: it equals 1 when $n = m$ and
$\frac{1}{N}\cdot\frac{1-e^{2\pi i(n-m)}}{1-e^{2\pi i(n-m)/N}} = 0$ otherwise,
because the numerator vanishes for every integer $n-m$ other than a multiple of
$N$. So the bracket is the Kronecker delta and the sum collapses to $x[n]$.

**This is where the $1/N$ comes from.** The basis vectors
$\{e^{2\pi ikn/N}\}_k$ are orthogonal but not orthonormal: their squared norms
are $N$, so a projection has to be divided by $N$ to reconstruct. The forward
transform is the projection; the inverse is the reconstruction. Either choice of
where to put the $1/N$ is possible, and the "symmetric" choice of $1/\sqrt N$ on
both sides makes the operator unitary, which is elegant but inconvenient for
spectral estimation because then neither bin is a plain sum.

## 4. Cost: $O(N^{2})$ against $O(N\log N)$

The definition requires, for each of $N$ outputs, a sum over $N$ terms: $N^{2}$
complex multiply-adds. The demo times both algorithms on the same machine:

| $N$ | direct DFT (s) | FFT (s) | speed-up | operation ratio $N^{2}/((N/2)\log_2N)$ |
|---|---|---|---|---|
| 128 | 0.001435 | 0.000113 | 12.7 | 18.3 |
| 256 | 0.006577 | 0.000242 | 27.2 | 32.0 |
| 512 | 0.024792 | 0.000553 | 44.9 | 56.9 |
| 1024 | 0.097654 | 0.001252 | 78.0 | 102.4 |
| 2048 | 0.368482 | 0.002309 | 159.6 | 186.2 |
| 4096 | (not timed) | 0.004991 | — | 341.3 |
| 16384 | (not timed) | 0.024806 | — | 1208.0 |
| 65536 | (not timed) | 0.128661 | — | 4369.1 |

These are wall-clock measurements on a shared machine, and they move by tens of
per cent between runs: the speed-up column and the fitted exponents below should
be read as orders of magnitude and trends, not as calibration. The script takes
the minimum of three runs for each case to reduce the noise, and the
**operation counts in the last column are exact and reproducible** — they are
the statement worth quoting.

Fitting a power law $\text{time} \propto N^{p}$ by least squares gives
$p = 2.02$ for the direct DFT and $p = 1.12$ for the FFT in the run tabulated
above; repeated runs give 2.01–2.08 and 1.10–1.14. The DFT's exponent is $2$ to
within the noise of the timing measurement; the FFT's is for ever slightly above
1 because $(N/2)\log_2N$ is not a pure power law (it grows as $N\log N$, so its
local exponent increases slowly) and because memory hierarchy effects change at
the larger sizes. Dividing by the cost model instead of fitting largely removes
the ambiguity: the DFT's time divided by $N^{2}$ is
$8.8$–$10.0\times10^{-8}$ s over the tested range, and the FFT's time divided by
$N\log_2N$ is $1.18$–$1.26\times10^{-7}$ s — each constant to within about 15%
across a factor of sixteen in $N$. The *operation counts* are exact: at $N = 1024$ the direct DFT
performs 1 048 576 complex multiply-adds and the radix-2 FFT performs 5120
butterflies, a ratio of 205.

**The practical consequence is not that the FFT is faster, but that it changed
what is computable.** A DFT of $10^{6}$ samples by direct summation is
$10^{12}$ operations — hours — while an FFT is about $10^{7}$ butterflies, a
fraction of a second. Convolution, migration, correlation and matched filtering
all rest on that change.

The algorithm, in two sentences: a radix-2 FFT splits the sum into even and odd
indices, $X[k] = E[k] + e^{-2\pi ik/N}O[k]$, repeats the split recursively until
the sub-problems have length 1, and combines pairs of results with
$(u+v, u-v)$ butterflies. The demo implements it iteratively with an initial
bit-reversal permutation, and the more important point for a user is that its
output is *numerically identical* to the direct sum: on a 1024-sample
three-sinusoid signal the maximum difference between the two implementations is
$9.8\times10^{-11}$ absolute, $2.1\times10^{-13}$ relative — accumulated
round-off, larger for the direct sum because its twiddle factors are built by
repeated multiplication. A relative difference above $10^{-12}$ indicates a bug,
not a property of the FFT.

## 5. Normalisation: the three readings of one number

The demo transforms $x[n] = 3\cos(2\pi\cdot20\cdot n\,dt)$ with $N = 1000$ and
$dt = 0.01$ s, so the record is exactly 10.00 s long, $df = 0.1000$ Hz, and
20 Hz falls exactly on bin $k_0 = 200$. The result:

| quantity | value |
|---|---|
| $X[k_0]$ | $1500.0000 - 0.0000i$ |
| $N/2 \times A$ (prediction) | $1500.0000$ |
| amplitude recovered as $2\lvert X[k_0]\rvert/N$ | $3.0000000000$ (true 3.0) |
| amplitude recovered as $\lvert X[k_0]\rvert/N$ | $1.5000000000$ — **wrong by exactly 2** |
| amplitude recovered as $2\lvert X[k_0]\rvert/N^{2}$ | $0.0030000000$ — **wrong by a further $N$** |
| $\lvert X[N-k_0]\rvert$ | $1500.0000$ (equal, as Hermitian symmetry requires) |

**Why the factor 2.** A real cosine is two complex exponentials of half the
weight, and the transform puts them at $+k_0$ and $-k_0$. Each carries
$A\,N/2$, so a one-sided spectrum — which throws the negative frequencies away —
must double every retained bin to preserve amplitude. The exceptions are the DC
bin ($k=0$), where a real signal's energy is not split, and the Nyquist bin
($k = N/2$, $N$ even), where a real sample sequence cannot distinguish $+f_N$
from $-f_N$.

**Parseval's check** on the same signal:

| quantity | value |
|---|---|
| $\sum\lvert x[n]\rvert^{2}$ | 4500.000000 |
| $(1/N)\sum\lvert X[k]\rvert^{2}$ | 4500.000000 (relative difference $2.4\times10^{-15}$) |
| $\sum\lvert X[k]\rvert^{2}$ (no $1/N$) | 4 500 000.000000 — too large by exactly $N = 1000$ |
| mean square $\sum\lvert x\rvert^{2}/N$ | 4.5000, against the theoretical $A^{2}/2 = 4.5000$ |

So the discrete Parseval relation is
$\sum_n\lvert x[n]\rvert^{2} = \frac{1}{N}\sum_k\lvert X[k]\rvert^{2}$,
and the mean square of a sinusoid of amplitude $A$ is $A^{2}/2$ as it must be.

## 6. Zero padding: interpolation, not resolution

This is the most commonly mis-stated fact in applied Fourier analysis, so the
demo measures it. Take a 64-sample record at $dt = 1$ s, so $T = 64$ s and
$df = 1/T = 0.015625$ Hz, containing two equal tones. Because each tone is
tapered with a Hann window, leakage is out of the way. For each separation, the
spectrum is zero-padded to lengths 64, 256, 1024 and 16384, and the demo records
the number of local maxima in the neighbourhood of the two tones and the depth of
the valley between them:

| separation | pad | maxima | valley (dB) |
|---|---|---|---|
| $0.50\times df$ | 64 | 1 | 0.0 |
| $0.50\times df$ | 256 | 1 | 0.3 |
| $0.50\times df$ | 1024 | 1 | 0.1 |
| $0.50\times df$ | 16384 | 1 | 0.0 |
| $2.00\times df$ | 64 | 1 | 0.1 |
| $2.00\times df$ | 256 | 2 | 0.1 |
| $2.00\times df$ | 1024 | 2 | 0.1 |
| $2.00\times df$ | 16384 | 2 | 0.0 |
| $3.00\times df$ | 64 | 2 | $-5.9$ |
| $3.00\times df$ | 256 | 2 | $-31.5$ |
| $3.00\times df$ | 1024 | 2 | $-31.5$ |
| $3.00\times df$ | 16384 | 2 | $-31.5$ |

Three honest conclusions.

1. **The truly unresolved pair (0.50 df) is a single lobe at every padding.**
   Padding never invents a split that the record does not contain.
2. **The marginal pair (2.00 df) shows one maximum on the coarse grid and two on
   the fine ones**, purely because the coarse grid lands between the peaks. Its
   valley is $+0.1$ dB at *every* padding: the two bumps are not separated by a
   dip at all. Counting maxima is therefore a poor test of resolution.
3. **The resolved pair (3.00 df) has a real valley at every padding.** The coarse
   grid merely under-reports its depth ($-5.9$ dB instead of $-31.5$ dB) because
   it missed the bottom; the three fine grids agree with one another exactly.

So padding buys **precision in reading a spectrum that already exists** and
nothing else. The bin spacing is $df = 1/(N_{\text{pad}}\,dt)$ and can be made
arbitrarily small; the **resolution** is set by $T$ and cannot. Whether two tones
count as resolved remains a judgement about how deep a valley you are willing to
call a split, which is the subject of
[01-10-05](./05-windowing-aliasing.md).

## 7. Python demonstration

[`code/dft_fft_demo.py`](./code/dft_fft_demo.py) implements the direct DFT, the
iterative radix-2 FFT, the timing study, the normalisation ladder and the
zero-padding experiment. It runs in under a second:

```text
python3 code/dft_fft_demo.py
```

Two notes on the implementation.

1. **The direct DFT precomputes its twiddle factors.** The comparison should be
   between two reasonable implementations, not between a good FFT and a careless
   sum; even with precomputation, the sum remains $N^{2}$ operations.
2. **$N = 1000$ is used for the normalisation test**, which is not a power of
   two, so the direct DFT computes it. Choosing a signal whose frequency lands
   exactly on a bin matters more for that test than using the fast algorithm —
   and both facts are stated in the script rather than hidden.

## 8. Common mistakes

1. **Confusing the sum with the mean.** $X[0]$ is the sum. The mean is
   $X[0]/N$; the integral is $dt\,X[0]$. The demo's three-way ladder in
   [01-10-02](./02-fourier-transform.md) Section 6 shows the two factors
   ($1/N$ and $1/dt$) that separate them.
2. **Forgetting the factor 2 in a one-sided amplitude spectrum.** Every bin
   except DC and Nyquist needs it, because the negative-frequency twin has been
   discarded.
3. **Believing zero padding improves resolution.** It improves the *sampling* of
   the spectrum. Resolution is $1/T$.
4. **Padding without noting the change in $df$.** After padding to
   $N_{\text{pad}}$, the bin spacing is $1/(N_{\text{pad}}dt)$, not $1/T$, and
   reading a peak's frequency off the padded axis requires the padded spacing.
5. **Assuming the FFT requires a power of two.** Radix-2 requires it; mixed-radix
   and chirp-$z$ algorithms handle any $N$ in $O(N\log N)$. The constraint is a
   property of one algorithm, not of the transform.
6. **Comparing a DFT's output with a continuous transform without the $dt$ and
   time-origin factors.** See [01-10-02](./02-fourier-transform.md) Section 7 for
   the exact relation.
7. **Treating the output of a real-signal FFT as if the upper half were
   independent.** It is the conjugate mirror; plotting it as data doubles the
   apparent information content.

## 9. Real-world applications

- **Seismic trace processing.** Every filter, deconvolution, correlation and
  spectral-whitening step runs on an FFT. Trace lengths are chosen to be
  convenient for the transform, and padding decisions are made explicitly because
  of Section 4's wrap-around.
- **Gravity and magnetic map processing.** Grid sizes are powers of two or are
  padded to such, and the wavelength content of a map is read from a padded
  spectrum — hence the importance of stating whether a displayed peak is
  interpolated or resolved.
- **Matched filtering and correlation.** Cross-correlation through the FFT
  ($O(N\log N)$ instead of $O(N^{2})$) is what makes template matching over long
  continuous records practical, and is the core of matched-filter detection of
  small seismic events.
- **Spectra of continuous data streams.** Long records are broken into segments,
  each transformed, and the results averaged — the Welch method, whose statistics
  are quantified in [01-10-08](./08-spatial-spectra.md).
- **Tidal and climate harmonic analysis.** The fit of
  [01-10-01](./01-fourier-series.md) is routinely accelerated by FFT-based
  projection when the frequencies are chosen to be exactly on bins.
- **Accelerating optimal estimation.** Any operator that can be applied as a
  convolution can be applied in $O(N\log N)$ — the basis of every modern
  iterative geophysical inversion that uses FFTs in its forward operator.

## 10. Further reading

- **Cooley, J. W. & Tukey, J. W. (1965). An algorithm for the machine
  calculation of complex Fourier series. *Mathematics of Computation*, 19(90),
  297–301.** Level: advanced. The paper that made the FFT widely known; the
  essential idea (the even/odd split with a small-$N$ closed form) is readable in
  an afternoon.
- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapters 10–12. Level: intermediate. The DFT as the
  sampled transform, with a careful treatment of the factors.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T. & Flannery, B. P. (2007).
  *Numerical Recipes* (3rd ed.). Cambridge University Press.** Chapter 12.
  Level: intermediate. Implementation details, real-versus-complex transforms,
  and the padding discussion.
- **Harris, F. J. (1978). On the use of windows for harmonic analysis with the
  discrete Fourier transform. *Proceedings of the IEEE*, 66(1), 51–83.**
  Level: advanced. The reference for window definitions and their measured
  sidelobe behaviour, and the source of the coherent-gain table used in
  [01-10-05](./05-windowing-aliasing.md).
- **Oppenheim, A. V. & Schafer, R. W. (2010). *Discrete-Time Signal Processing*
  (3rd ed.). Pearson.** Chapters 8–9. Level: advanced. The rigorous development
  of the DFT as a sampling of the DTFT, and the definitive treatment of the
  circular-versus-linear convolution distinction.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 11. Related lessons

- [02 The Fourier Transform and Its Properties](./02-fourier-transform.md) — the
  continuous transform this discretises.
- [03 Convolution, Filtering and the Convolution Theorem](./03-convolution.md) —
  why circular wrap-around is a padding problem.
- [05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
  the two approximations (sampling and truncation) that Section 6 defers.
- [06 Hilbert Transform, Analytic Signal and Instantaneous Phase](./06-hilbert-transform.md) —
  a spectral construction that depends on the bin layout of Section 2.2.
- [07 Two-Dimensional Fourier Analysis and Wavenumber Filtering](./07-2d-fourier.md) —
  the separable extension to two dimensions.
- [08 Power Spectra, Admittance and Coherence of Geophysical Fields](./08-spatial-spectra.md) —
  what to do with the numbers once you have them.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — where
  transform-based operators sit in large-scale modelling and inversion.

## 12. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/04-discrete-fourier-exercises.md`](./exercises/04-discrete-fourier-exercises.md).
Solutions: [`exercises/04-discrete-fourier-solutions.md`](./exercises/04-discrete-fourier-solutions.md).

## Self-assessment checklist

- [ ] I can write the DFT pair with the normalisation and sign convention stated.
- [ ] I can derive the inverse formula by substituting the forward one and
      showing the inner sum is a Kronecker delta.
- [ ] I can compute the DFT of a small real sequence by hand and check Hermitian
      symmetry.
- [ ] I can state which bins are positive, Nyquist and negative frequencies.
- [ ] I can recover an amplitude from a spectrum with the right factor of 2 and
      the right treatment of DC and Nyquist.
- [ ] I can verify Parseval numerically and state the factor introduced by
      dropping $1/N$.
- [ ] I can explain why zero padding interpolates but does not resolve, and
      support the claim with the three-row table of Section 6.
- [ ] I can state the FFT's operation count and why it changed what is
      computable.
