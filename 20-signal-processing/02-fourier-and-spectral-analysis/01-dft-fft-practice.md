---
id: 20-02-01
title: "Practical DFT/FFT: Normalisation, Units and Pitfalls"
level: intermediate
prereqs: ["20-01-05", "01-10-04", "03-02-04"]
tags: [signal-processing, dft, fft, normalisation, parseval, spectra]
---

# Practical DFT/FFT: Normalisation, Units and Pitfalls

The discrete Fourier transform is exact, and almost every error made with it is a
convention error: the factor of $N$, the factor of 2 for a one-sided spectrum,
the factor $\Delta f$, the sign of the exponent, or the ordering of the output
bins. This lesson fixes the conventions, verifies each of them numerically
against an independent calculation, and then derives the two effects that a
correct implementation still produces — leakage from truncation and the
$\approx 36\%$ scalloping loss of a tone that falls between bins.

**All models and data in this module are SYNTHETIC.** Every comparison below is
against an exact algebraic identity, so the printed differences are rounding
residuals, not estimates.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the DFT convention used by `numpy.fft` and **verify** it against a
   transform computed from the definition.
2. **Convert** between raw DFT output and amplitude spectra, power spectra and
   power spectral densities, and **give the units** of each.
3. **Check** a spectrum with Parseval's theorem in all three forms, and use the
   check to catch normalisation errors.
4. **Handle** the bin ordering of `fft`, `rfft`, `fftfreq`, `rfftfreq` and
   `fftshift`, including the DC and Nyquist bins that must not be doubled.
5. **Derive** the DFT of a rectangular pulse as the Dirichlet kernel and
   **explain** its exact zeros.
6. **Quantify** the scalloping loss of an off-bin tone, including the exact
   half-bin value $2/\pi$.
7. **Distinguish** leakage (a property of truncation, curable by windowing) from
   a numerical error (which it is not).

## Prerequisites

- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md) —
  how the samples were obtained and what the sample rate means.
- [01-10-04 Discrete Fourier Transform and the FFT](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md) —
  the transform's definition and properties.
- [03-02-04 ufuncs and Reductions in NumPy](../../03-scientific-computing/02-numpy/04-ufuncs-reductions.md) —
  the array operations used in the demonstration.

## 1. Intuition: the transform is exact; your bookkeeping is not

The DFT knows nothing about time or frequency units. It takes $N$ numbers and
returns $N$ numbers. Everything physical — a frequency in hertz, an amplitude in
$\mathrm{m\,s^{-1}}$, a density in $(\mathrm{m\,s^{-1}})^{2}\,\mathrm{Hz^{-1}}$ —
is added by you, in the form of $\Delta t$, $f_s$ and a normalisation factor. If
the result looks wrong, the transform is almost never at fault; one of those
three is.

The practical consequences are worth stating up front, because they are what the
demonstration measures:

- A **tone standing between two bins** is under-reported by up to $3.92\
\mathrm{dB}$ ($36\%$ in amplitude) — not an error, but the shape of the kernel.
- A **record that is not an integer number of periods** spreads its energy across
  every bin; that is leakage, and windowing is the cure
  ([20-02-03](03-windowing-advanced.md)).
- **DC and Nyquist are special**: they occur once, not twice, so the factor 2 of a
  one-sided spectrum must not be applied to them.

## 2. The convention, stated and verified

`numpy.fft.fft` computes

$$X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-2\pi i kn/N},
\qquad k = 0,\dots,N-1,$$

and `numpy.fft.ifft` computes

$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]\,e^{+2\pi i kn/N}.$$

Four things to notice, each of which is a different convention in some other
library or textbook: the exponent is **negative** in the forward transform; the
forward transform carries **no** $1/N$ (the inverse does); the sum runs over
$n = 0,\dots,N-1$ so no time origin is assumed; and $X$ is indexed from 0 to
$N-1$ with the negative frequencies stored at the **end**, not discarded.

*Numerical check (SYNTHETIC, $N = 64$, Gaussian noise).* Computing the transform
from the double sum above and comparing with the library:

| comparison | maximum absolute difference |
|---|---|
| `dft_by_definition` vs `numpy.fft.fft` | $1.76\times10^{-13}$ |
| `idft_by_definition` vs `numpy.fft.ifft` | $2.68\times10^{-14}$ |
| `ifft(fft(x))` vs `x` | $5.57\times10^{-16}$ |

The first two residuals are larger than the third because the explicit
matrix–vector product accumulates rounding differently from the FFT's butterfly
structure; all three are at the level of double precision and none of them is a
convention disagreement.

## 3. Exact identities, useful as unit tests

Three transforms can be written down exactly, and any implementation must
reproduce them:

| input | DFT | demonstration |
|---|---|---|
| $x[n] = 1$ | $X[0] = N$, $X[k] = 0$ otherwise | $16.000000$, others exactly $0$ |
| $x[n] = e^{+2\pi ik_0n/N}$ | $X[k_0] = N$, $0$ otherwise | $\lvert X[9]\rvert = 64.000000$, others $\le 3.1\times10^{-14}$ |
| $x[n] = (-1)^{n}$ | $X[N/2] = N$, $0$ otherwise | $\lvert X[32]\rvert = 64.000000$, others exactly $0$ |

The first and third are exact in floating point (they are integer sums); the
second is exact up to rounding because it evaluates complex exponentials. Writing
these three as a test of your own FFT wrapper costs five lines and catches every
normalisation and index error.

## 4. The DFT of a rectangular pulse: the Dirichlet kernel

For $x[n] = 1$ on $0 \le n \le L-1$ and $0$ elsewhere in a record of length
$N$,

$$X[k] = \sum_{n=0}^{L-1}e^{-2\pi ikn/N}
= e^{-i\pi k(L-1)/N}\,
\frac{\sin(\pi kL/N)}{\sin(\pi k/N)}
= e^{-i\pi k(L-1)/N}\,D\!\left(\frac{2\pi k}{N},L\right),$$

where $D(\omega,L) = \sin(L\omega/2)/\sin(\omega/2)$ is the **Dirichlet kernel**.
Two consequences that matter in practice:

- $X[0] = L$ exactly (the sum of the pulse), and the transform has **exact
  zeros** wherever $kL/N$ is a non-zero integer, i.e. at $k = mN/L$ for
  $m = 1,2,\dots$ Hence a pulse of length $L$ in a record of length $N$ is
  invisible to every bin numbered in multiples of $N/L$.
- The sidelobe structure is the same Dirichlet kernel that appears as the
  rectangular window's spectral leakage; its asymptotic first sidelobe is
  $-13.26\ \mathrm{dB}$ relative to the main lobe
  (measured for short windows in
  [20-01-03 §5.1](../01-signals-and-systems/03-convolution-and-filters.md)).

*Numerical check* ($N = 256$, $L = 32$): the library DFT matches
$D(2\pi k/N,32)e^{-i\pi k\cdot31/256}$ to a maximum difference of
$1.64\times10^{-13}$, $X[0] = 32.0$ exactly, and the bins $k = 8, 16, 24, 32$
are exactly zero — the predicted multiples of $N/L = 8$.

## 5. The normalisation ladder

Let $x$ be a real record of $N$ samples with interval $\Delta t$ and rate
$f_s = 1/\Delta t$; let $\Delta f = f_s/N = 1/(N\Delta t)$ be the bin spacing.
For a sinusoid of amplitude $A$ at a frequency that is exactly on bin $k_0$, the
raw transform is $X[k_0] = AN/2$ (and $\lvert X\rvert$ has a mirror image at
$N-k_0$). The table gives the ladder from that raw number to interpretable
quantities, with the measured values for $A = 3$, $N = 1000$, $f_s = 100\
\mathrm{Hz}$, $f_0 = 10\ \mathrm{Hz}$ (exactly bin 100):

| quantity | formula | measured | exact | unit |
|---|---|---|---|---|
| raw bin | $\lvert X[k_0]\rvert$ | $1500.000$ | $AN/2 = 1500$ | signal × samples |
| raw power | $\lvert X[k_0]\rvert^{2}$ | $2.25\times10^{6}$ | $(AN/2)^{2}$ | (signal × samples)² |
| **amplitude spectrum** | $2\lvert X\rvert/N$ | $3.000000$ | $A = 3$ | signal units (m/s) |
| **one-sided PSD** | $2\lvert X\rvert^{2}/(N^{2}\Delta f)$ | $45.000$ | $A^{2}/(2\Delta f)$ | signal² per Hz |

The amplitude-spectrum factor is $2/N$ — the 2 to fold the mirror image onto the
positive axis, the $1/N$ for the forward transform's missing normalisation.
The PSD factor additionally divides by $\Delta f$ so that integrating over
frequency returns power. Two rules follow:

- **Do not double DC or Nyquist.** They have no mirror image. With `rfft` on an
  even-length record the correct amplitude spectrum is
  $2\lvert X\rvert/N$ for bins $1..N/2-1$ and $\lvert X\rvert/N$ for bins $0$ and
  $N/2$.
- **State the scaling.** `scipy.signal.periodogram(x, fs, scaling='spectrum')`
  returns amplitude-squared per bin, `scaling='density'` returns per-hertz
  density; the two differ by a factor $\Delta f$ and their numbers therefore
  differ by the record length. Neither is more correct; only the stated one is.

## 6. Parseval, in three forms

$$\sum_{n=0}^{N-1}\lvert x[n]\rvert^{2}
= \frac{1}{N}\sum_{k=0}^{N-1}\lvert X[k]\rvert^{2}
= \frac{1}{N}\left(\lvert X[0]\rvert^{2} + \lvert X[N/2]\rvert^{2}
+ 2\sum_{k=1}^{N/2-1}\lvert X[k]\rvert^{2}\right),$$

the last form being the one-sided version for even $N$ and real $x$. It is the
quickest global check on a transform and on a scaling convention.

*Numerical check* (SYNTHETIC, $N = 512$, $f_s = 200\ \mathrm{Hz}$, Gaussian noise
of $\sigma = 2$):

| check | value | difference |
|---|---|---|
| $\sum x^{2}$ | $2093.545032$ | — |
| $\frac1N\sum\lvert X\rvert^{2}$ | $2093.545032$ | $4.5\times10^{-13}$ |
| one-sided sum | $2093.545032$ | $0.0$ |
| mean square vs $\sum_k P[k]\Delta f$ | $4.088955$ | $0.0$ |

With the PSD defined as in Section 5 the last check is exact to the last printed
digit, which is what makes it a usable test rather than an approximation.

## 7. Bin ordering: `fftfreq`, `rfftfreq` and `fftshift`

For $N = 8$ and $f_s = 8\ \mathrm{Hz}$ the demonstration prints

$$\texttt{fftfreq} = [0, 1, 2, 3, -4, -3, -2, -1], \qquad
\texttt{fftshift(fftfreq)} = [-4, -3, -2, -1, 0, 1, 2, 3],$$

$$\texttt{rfftfreq} = [0, 1, 2, 3, 4] \quad (N/2+1 = 5\ \text{bins}),$$

and for odd $N = 9$, $\texttt{rfftfreq} = [0, 0.8889, 1.7778, 2.6667, 3.5556]$.
Three traps follow directly:

1. **The Nyquist bin exists only for even $N$.** For odd $N$ there is no bin at
   $f_s/2$, so "double everything except DC" is the correct rule and there is no
   exception to remember.
2. **`fftshift` must be applied before any one-sided reduction, not after.**
   Applying it to `rfft` output — half a spectrum, ordered from DC upward —
   produces a meaningless array whose first entry is the Nyquist bin.
3. **The imaginary parts of the DC and Nyquist bins are exactly zero** for a real
   input, and the measurement returns $0.0$ for both. Their real parts are the
   record's sum and alternating sum, and they are the only two bins that carry no
   phase information. The full conjugate symmetry
   $X[k] = \overline{X[N-k]}$ holds for $k = 1,\dots,N-1$ and is verified to
   $0.0$.

## 8. Two effects a correct implementation still has

### 8.1 Scalloping loss

If the tone is not exactly on a bin, its amplitude is under-reported by the
Dirichlet factor

$$\frac{\lvert X_{\text{peak}}\rvert}{AN/2}
= \left\lvert\frac{\sin(\pi\delta)}{N\sin(\pi\delta/N)}\right\rvert,
\qquad \delta = \text{offset in bins}.$$

Measured for $N = 1000$, $f_s = 100\ \mathrm{Hz}$ ($\Delta f = 0.1\
\mathrm{Hz}$), amplitude 1:

| offset (bins) | 0 | 0.25 | 0.50 | 0.75 |
|---|---|---|---|---|
| recovered amplitude | 1.000000 | 0.899609 | 0.636942 | 0.899610 |
| exact factor | 1.000000 | 0.900316 | 0.636620 | 0.900316 |
| loss (dB) | $-0.000$ | $-0.919$ | $-3.918$ | $-0.919$ |

The worst case is exactly $\delta = 1/2$, where
$\lvert\sin(\pi\delta)\rvert = 1$ and $N\sin(\pi/2N)\to\pi/2$, giving

$$\frac{1}{\pi/2} = \frac{2}{\pi} = 0.636620,\qquad
20\log_{10}\frac{2}{\pi} = -3.9224\ \mathrm{dB}.$$

The residual $0.08\%$ between the measured and exact columns at $\delta = 0.25$
and $0.75$ is the negative-frequency term of the real sine, which the Dirichlet
factor for a complex exponential does not include — a reminder that the
"one-sided amplitude spectrum" is an addition, not part of the transform.

**Practical status.** Scalloping loss is a systematic amplitude error of up to
$3.9\ \mathrm{dB}$, not random noise, and it survives averaging. It is removed by
estimating the peak's true frequency and interpolating (three-point parabolic
interpolation reduces the error to a few hundredths of a dB), by zero-padding to
interpolate the spectrum on a finer grid (which does **not** increase
resolution — it interpolates the kernel you already have), or by choosing a
window with a flatter top (the flat-top windows of
[20-02-03](03-windowing-advanced.md), at the cost of ENBW).

### 8.2 Leakage from truncation

A finite record is a longer signal multiplied by a rectangular window. In the
frequency domain that is a convolution with the window's kernel, so a pure tone
becomes the Dirichlet kernel centred on its frequency. Measured on a
1000-sample, $100\ \mathrm{Hz}$ record:

| tone | fraction of spectral energy within $\pm3$ bins of the peak |
|---|---|
| exactly 100 periods (on bin) | $1.000000$ |
| not a whole number of periods (off bin) | $0.941606$ |

So $5.8\%$ of the energy has moved more than three bins from the tone's true
frequency — in a record of 1000 samples, where "three bins" is $0.3\
\mathrm{Hz}$. Nothing is lost (Parseval is exact) and nothing is wrong with the
transform: the record simply is not periodic in its own length, and the transform
of a finite record is the transform of that finite object. This is why windowing
tapers the ends: it changes the kernel from the slowly-decaying Dirichlet to a
kernel with low sidelobes.

## 9. Units and dimensional analysis

| quantity | unit (for $x$ in m/s, $t$ in s) | check |
|---|---|---|
| $X[k]$ | $\mathrm{m\,s^{-1}}$ × (dimensionless count) | sum of $N$ samples, so $N$ appears |
| $2\lvert X\rvert/N$ | $\mathrm{m\,s^{-1}}$ | amplitude |
| $\lvert X\rvert^{2}/N^{2}$ | $(\mathrm{m\,s^{-1}})^{2}$ | power, per sample-squared |
| $P[k] = 2\lvert X\rvert^{2}/(N^{2}\Delta f)$ | $(\mathrm{m\,s^{-1}})^{2}\,\mathrm{Hz^{-1}}$ | density |
| $\sum_k P[k]\Delta f$ | $(\mathrm{m\,s^{-1}})^{2}$ | power, as required |
| $\sum_n x^{2}\Delta t$ | $(\mathrm{m\,s^{-1}})^{2}\,\mathrm{s}$ | energy-like |

If a "PSD" does not integrate to a power with the units of the signal squared,
the $\Delta f$ or the $N^{2}$ is wrong. If an "amplitude" carries a factor of
$N$, you forgot to divide.

## 10. Worked examples

### Example 1 — reading a spectrum correctly

A synthetic 1024-sample record at $f_s = 128\ \mathrm{Hz}$ contains a
$16\ \mathrm{Hz}$ sine of amplitude $0.5\ \mathrm{m\,s^{-1}}$. Then
$\Delta f = 0.125\ \mathrm{Hz}$ and $16\ \mathrm{Hz}$ is exactly bin $128$. The
raw peak is $\lvert X\rvert = AN/2 = 0.5\times512 = 256$, the amplitude spectrum
gives $2\times256/1024 = 0.5$, and the one-sided PSD gives
$2(256)^{2}/(1024^{2}\times0.125) = 1.0\ (\mathrm{m\,s^{-1}})^{2}\,\mathrm{Hz^{-1}}$,
which integrates over one bin to $0.125\ (\mathrm{m\,s^{-1}})^{2}$ — a quarter of
the true power $A^{2}/2 = 0.125$. ✔ (The check is exact because the sine has two
half-amplitude exponentials, one of which is folded into the one-sided bin.)

### Example 2 — why the pulse's zeros matter

A synthetic reflection pulse of 32 samples in a 256-sample record: bin $k$
carries zero energy exactly when $k$ is a multiple of $8$. If a source repeats at
$f_s/8$, its fundamental and all harmonics land on those zeros and the pulse is
*invisible*. Choosing a shot rate near, but not at, a submultiple of the record
length is a cheap way to avoid systematically nulling a periodic source; choosing
it exactly is a way to make a real signal disappear.

### Example 3 — verifying someone else's spectrum

A colleague reports a noise PSD of $2.0\times10^{-12}\ (\mathrm{m\,s^{-1}})^{2}\,\mathrm{Hz^{-1}}$
from a 10-second, $100\ \mathrm{Hz}$ record of a channel whose time-domain rms is
$4.5\times10^{-5}\ \mathrm{m\,s^{-1}}$. Check:

$$\text{rms}^{2} = (4.5\times10^{-5})^{2} = 2.025\times10^{-9}\
(\mathrm{m\,s^{-1}})^{2},
\qquad
\text{bandwidth} = f_s/2 = 50\ \mathrm{Hz},$$

so a flat PSD should be $2.025\times10^{-9}/50 = 4.05\times10^{-11}$, five times
the reported value. The discrepancy factor of five is not a coincidence: it is a
one-sided/two-sided or amplitude/power error. Parseval is the diagnostic — always
run it before believing a PSD.

## 11. Python demonstration

`code/dft_fft_practice_demo.py` is print-only, single-process, uses `numpy` only,
and runs in about a second. It:

1. compares the DFT from its definition with `numpy.fft`, forward and inverse;
2. checks the three exact identities of Section 3;
3. compares the boxcar's DFT with the analytic Dirichlet kernel;
4. walks the normalisation ladder for an on-bin sine;
5. checks Parseval in three forms including the PSD integral;
6. prints the bin orderings and the conjugate-symmetry residual;
7. measures scalloping loss at offsets of 0, 0.25, 0.5 and 0.75 bins;
8. compares the energy concentration of an on-bin and an off-bin record.

```bash
cd 20-signal-processing/02-fourier-and-spectral-analysis/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dft_fft_practice_demo.py
```

## 12. Assumptions and regime of validity

1. **The record is treated as one period of a periodic signal.** That is what the
   DFT computes. If the record is not periodic in its own length, leakage is the
   honest consequence (Section 8.2), not an artefact to be blamed on the FFT.
2. **$\Delta f = f_s/N$ is the resolution, not $f_s/N_{\text{padded}}$.** Zero
   padding interpolates the existing kernel; it does not resolve frequencies
   closer together. Only a longer observation does that
   ([20-02-03](03-windowing-advanced.md)).
3. **Real input is assumed in the one-sided formulas.** For a complex or analytic
   signal there is no conjugate symmetry and no factor of 2; doubling would
   double-count.
4. **The amplitude spectrum is only meaningful for a deterministic, stationary
   sinusoid.** For noise the amplitude carries no information — the phase is
   random — and only the PSD or a power spectrum is interpretable.
   ([20-02-02](02-spectral-estimation.md) makes this precise.)
5. **`np.fft` results are not bit-reproducible across libraries.** FFT
   implementations differ in rounding by $\sim10^{-15}$ relative; a test that
   demands equality rather than agreement to a tolerance will fail on a different
   machine.
6. **The Dirichlet formulas assume a rectangular taper.** Any other window
   replaces $D$ by the window's kernel, and the exact zeros disappear.
7. **Undersampling is undetectable in a spectrum.** Everything here describes the
   sampled record; whether it faithfully represents the continuous signal is
   [20-01-05](../01-signals-and-systems/05-sampling-theory.md)'s question, and
   nothing in the spectrum can answer it.

## 13. Exercises

- [`exercises/01-dft-fft-practice-exercises.md`](./exercises/01-dft-fft-practice-exercises.md)
- [`exercises/01-dft-fft-practice-solutions.md`](./exercises/01-dft-fft-practice-solutions.md)

## 14. Common pitfalls

1. **Forgetting the $1/N$.** `fft` does not scale; `ifft` does. A spectrum that
   grows with record length is missing a division.
2. **Doubling DC or Nyquist.** They have no mirror image; doubling them inflates
   the mean and the Nyquist power by a factor 2.
3. **Applying `fftshift` after `rfft`.** Meaningless, as Section 7 shows.
4. **Reporting $\Delta f = f_s/N_{\text{padded}}$ as resolution.** Padding
   interpolates; only observation time resolves.
5. **Reading an amplitude spectrum of noise.** The bin amplitudes are random with
   a $100\%$ standard deviation; average PSDs instead.
6. **Quoting a peak amplitude without checking its bin offset.** The scalloping
   loss is up to $3.92\ \mathrm{dB}$ and is systematic.
7. **Blaming leakage on the FFT.** Compare $X$ with the analytic Dirichlet kernel
   of Section 4 and the leakage is reproduced exactly.

## 15. Mastery checkpoint

Without notes:

**(a)** Write the DFT and inverse DFT as `numpy.fft` defines them, including every
normalisation factor and the sign of the exponent.
**(b)** A 2048-sample record at $f_s = 512\ \mathrm{Hz}$ contains a full-scale
$1\ \mathrm{V}$ sine at $64\ \mathrm{Hz}$ (on bin). Give $\Delta f$, the raw peak
bin value, the amplitude spectrum value, and the one-sided PSD value, with units.
**(c)** The same tone sits at $64.1\ \mathrm{Hz}$. Estimate the amplitude
spectrum's peak value and convert the shortfall to dB.
**(d)** State Parseval in the form that uses `rfft` output, and say which two bins
are not doubled.
**(e)** A 40-sample pulse is embedded in a 1000-sample record. List five bin
indices at which its transform is exactly zero.
**(f)** A PSD is reported as $10^{-9}$ in units of "power"; the signal rms is
$10^{-4}$. Is that consistent for a flat spectrum over a $100\ \mathrm{Hz}$ band?

Answers for (b), (c) and (e) are in the
[solutions](./exercises/01-dft-fft-practice-solutions.md).

## 16. Related modules

- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md) —
  what the samples represent, and the folds the spectrum cannot show.
- [20-02-02 Spectral Estimation](02-spectral-estimation.md) — what to do when the
  signal is noise rather than a tone.
- [20-02-03 Window Functions and Spectral Leakage Control](03-windowing-advanced.md) —
  the cure for leakage, and the cost in resolution.
- [20-02-04 Cross-Spectra, Coherence and Phase Estimation](04-cross-spectra-coherence.md) —
  two-channel versions of the same conventions.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the mathematical treatment of the same transform.
- [03-02 NumPy for Scientific Computing](../../03-scientific-computing/02-numpy/README.md) —
  the array library whose conventions are fixed here.
