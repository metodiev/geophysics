---
id: 01-10-02
title: "The Fourier Transform and Its Properties"
level: advanced
prereqs: ["01-10-01", "01-05-06"]
estimated_minutes: 90
tags: [fourier-transform, spectral-methods, differentiation-operator, parseval]
---

# The Fourier Transform and Its Properties

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the Fourier transform pair in a stated sign and normalisation
   convention, and say why the convention must be stated at all.
2. **Derive** the transform of a Gaussian, a boxcar and a complex exponential
   from the integral.
3. **State and use** the property table — linearity, shift, scaling, modulation,
   differentiation, conjugation symmetry — and give the physical meaning of each
   entry.
4. **Explain** why a derivative in space becomes multiplication by $ik$, and
   quantify the difference between that and a finite-difference operator.
5. **Verify** Parseval's relation numerically and diagnose the two classic
   normalisation errors with the factor that each introduces.
6. **Relate** the continuous transform to the DFT, including the factor
   $dt$ and the phase factor from the time origin.

## Prerequisites

[01-10-01 Fourier Series and Periodic Decomposition](./01-fourier-series.md) —
the series, orthogonality, and the amplitude/phase language;
[01-05-06 Improper Integrals, Singularities and Convergence](../05-single-variable-calculus/06-improper-integrals.md) —
because the transform is an integral over an infinite domain and it must be
established that the integral exists.

## 1. Intuition: letting the period go to infinity

A Fourier series represents a signal that repeats. What if it does not? The
honest answer is that a non-repeating signal is the limit of a repeating one
whose period $T \to \infty$, and the discrete set of harmonics $\omega_n = 2\pi n/T$
becomes a continuum.

Read the coefficient formula of
[01-10-01](./01-fourier-series.md) with that in mind:

$$c_n = \frac{1}{T}\int_{-T/2}^{T/2} f(t)e^{-in\omega_0 t}\,dt .$$

As $T$ grows, $c_n$ shrinks (there is a $1/T$ in front) but the *density* of
harmonics $T/2\pi$ grows. The product of the two — the quantity that carries
physical meaning — tends to a finite function of a continuous frequency:

$$F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t}\,dt .$$

Everything about the transform follows from this one step, and one habit should
be adopted at once: **the transform is a density, not an amplitude.** A pure
sinusoid has zero energy at a single frequency and infinite density there; a
broadband signal has energy spread over a range. Amplitudes are recovered by
integrating a density, or by reading a *discrete* transform where the bins have
finite width.

## 2. Definitions and the convention question

### 2.1 The pair

$$F(f) = \int_{-\infty}^{\infty} x(t)e^{-2\pi i f t}\,dt
\qquad\text{(forward / analysis)},$$

$$x(t) = \int_{-\infty}^{\infty} F(f)e^{+2\pi i f t}\,df
\qquad\text{(inverse / synthesis)}.$$

This is the convention used throughout the module, with $F$ a function of
ordinary frequency $f$ in hertz. The equivalent angular-frequency form carries a
$1/(2\pi)$:

$$X(\omega) = \int x(t)e^{-i\omega t}dt, \qquad
x(t) = \frac{1}{2\pi}\int X(\omega)e^{i\omega t}d\omega .$$

### 2.2 Why there are four conventions and three of them are fine

The transform is defined by three independent choices: the sign in the exponent,
which member of the pair carries the $2\pi$, and which carries the $1/2\pi$
(or, in the $f$ convention, the fact that neither does). All consistent choices
describe the same physics. What is *not* fine is mixing them, because the
symptoms of mixing are asymmetric and easily missed:

| mixed choice | what breaks |
|---|---|
| opposite sign in one of the two transforms | the inverse does not invert; the spectrum is mirrored |
| $1/2\pi$ on both or on neither | every amplitude is wrong by $2\pi$ |
| different sign in the forward transform | the derivative operator becomes $-i\omega$ instead of $+i\omega$ |

The demo verifies the sign statement directly. With the kernel
$e^{-2\pi ift}$, the derivative property is $+i\omega$:

| $f$ (Hz) | DFT of $dx/dt$ | $i\,2\pi f\,X(f)$ | difference |
|---|---|---|---|
| 11.72 | $-5.5\times10^{-14} - 5.1921\times10^{2}i$ | $5.0\times10^{-14} - 5.1921\times10^{2}i$ | $2.0\times10^{-16}$ |
| 50.78 | $-1.9\times10^{-13} - 2.0432\times10^{3}i$ | $3.2\times10^{-13} - 2.0432\times10^{3}i$ | $6.1\times10^{-16}$ |
| 101.56 | $4.5\times10^{-13} + 3.0109\times10^{3}i$ | $-1.5\times10^{-12} + 3.0109\times10^{3}i$ | $7.9\times10^{-16}$ |
| 199.22 | $1.2\times10^{-13} - 1.8522\times10^{3}i$ | $3.2\times10^{-12} - 1.8522\times10^{3}i$ | $1.7\times10^{-15}$ |

(the test signal is an analytic Gaussian pulse with $\sigma = 0.002$ s, sampled
at $dt = 0.0005$ s, and the worst relative difference over the four frequencies
is $1.7\times10^{-15}$). Flip the convention and every one of those signs flips
with it — as would the apparent direction of every dip in
[01-10-07](./07-2d-fourier.md).

## 3. Three transforms worked from the integral

### 3.1 The Gaussian is its own transform

For $x(t) = e^{-\pi t^{2}}$,

$$F(f) = \int_{-\infty}^{\infty}e^{-\pi t^2}e^{-2\pi ift}dt
= e^{-\pi f^2}\int_{-\infty}^{\infty}e^{-\pi(t+if)^2}dt = e^{-\pi f^2},$$

the middle step by completing the square and shifting the contour (the integrand
is entire and decays, so the shift is legitimate), and the last step by the
Gaussian integral $\int e^{-\pi u^2}du = 1$.

The demo computes the same transform as a Riemann sum on a grid of 4096 samples
at $dt = 0.02$ s spanning $81.92$ s:

| $f$ | numeric transform | $e^{-\pi f^2}$ | absolute error |
|---|---|---|---|
| 0.00 | 1.0000000000 | 1.0000000000 | $6.7\times10^{-16}$ |
| 0.25 | 0.8217249580 | 0.8217249580 | $6.8\times10^{-14}$ |
| 0.50 | 0.4559381278 | 0.4559381278 | $5.6\times10^{-17}$ |
| 1.00 | 0.0432139183 | 0.0432139183 | $4.0\times10^{-15}$ |
| 1.50 | 0.0008514383 | 0.0008514383 | $3.7\times10^{-16}$ |
| 2.00 | 0.0000034873 | 0.0000034873 | $1.2\times10^{-17}$ |

The imaginary part stays at the $10^{-15}$ level, as it must: the input is real
and even, so the transform is real and even. The self-reciprocal Gaussian is the
reason the Gaussian is the standard test signal in every spectral paper — it has
no sidelobes, no ringing and a known answer.

### 3.2 A boxcar becomes a sinc

For $x(t) = 1$ on $|t| \le T/2$ and zero outside, with $T = 4$ s:

$$F(f) = \int_{-T/2}^{T/2}e^{-2\pi ift}dt
= \frac{\sin(\pi fT)}{\pi f} = T\,\mathrm{sinc}(fT),$$

using $\mathrm{sinc}(x) = \sin(\pi x)/(\pi x)$, so $F(f)$ is real and even with
zeros at $f = n/T$.

The demo builds the sampled boxcar on cell *midpoints* — exactly $M = 200$
samples with $M\,dt = T$ — so that the discrete sum has exactly the same zeros:

| $f$ (Hz) | numeric $\operatorname{Re}X$ | $T\,\mathrm{sinc}(fT)$ | magnitude error |
|---|---|---|---|
| 0.00 | $4.000000\times10^{0}$ | $4.000000\times10^{0}$ | $0$ |
| 0.10 | $3.027327\times10^{0}$ | $3.027307\times10^{0}$ | $2.0\times10^{-5}$ |
| 0.25 | $-2.3\times10^{-16}$ | $1.6\times10^{-16}$ | at a zero |
| 0.30 | $-6.236965\times10^{-1}$ | $-6.236595\times10^{-1}$ | $3.7\times10^{-5}$ |
| 0.50 | $1.5\times10^{-16}$ | $-1.6\times10^{-16}$ | at a zero |
| 0.75 | $-6.4\times10^{-16}$ | $1.6\times10^{-16}$ | at a zero |

Away from the zeros the sampled sum equals the continuous answer multiplied by
the Dirichlet correction $(\pi f dt)/\sin(\pi f dt)$, which the demo reports as
$1.000059$ at $f = 0.30$ Hz and $1.000370$ at $f = 0.75$ Hz — the small
discrepancy between the *sampled* boxcar and the continuous one.

The first sidelobe is found at $f = 0.3575$ Hz $= 1.4300/T$ at a level of
$-13.26$ dB relative to the peak, and the continuous $\mathrm{sinc}$ gives the
same frequency and the same level. **A hard edge in time costs about 13 dB of
sidelobe suppression in frequency.** That number is the reason windows exist, and
[01-10-05](./05-windowing-aliasing.md) is a whole lesson about it.

### 3.3 The complex exponential and the meaning of $\delta$

The transform of $e^{2\pi if_0 t}$ is not a function at all but a distribution:
$\delta(f - f_0)$. The demo's one-sided convention makes this concrete:
transforming $e^{+2\pi if_0 t}$ puts *all* the energy in one bin, while a real
cosine puts half in that bin and half in its mirror at $-f_0$. The measured
values are $|X[k_0]| = 64$ and $|X[N-k_0]| = 0$ for the complex exponential, and
$|X[k_0]| = |X[N-k_0]| = 32$ for the cosine, on a record of 64 samples. The
$\delta$ is a bookkeeping device for "all of it, right here".

## 4. The property table, with physical meaning

Every entry below is verified numerically in the demo; the "difference" column
quotes the largest discrepancy between the two sides.

| property | transform relation | difference | physical meaning |
|---|---|---|---|
| linearity | $\mathcal F\{\alpha x + \beta y\} = \alpha X + \beta Y$ | $2.2\times10^{-15}$ | superposed sources superpose in the spectrum |
| shift | $\mathcal F\{x(t-t_0)\} = X(f)e^{-2\pi if t_0}$ | $2.8\times10^{-16}$ | a time delay is a phase ramp only; $\lvert X\rvert$ untouched |
| scaling | $\mathcal F\{x(at)\} = \frac{1}{\lvert a\rvert}X(f/a)$ | $3.9\times10^{-16}$ | compress in time, expand in frequency, conserving area |
| modulation | $\mathcal F\{x(t)\cos 2\pi f_0t\} = \frac12[X(f-f_0)+X(f+f_0)]$ | $4.5\times10^{-14}$ | a carrier moves the spectrum to $\pm f_0$ |
| differentiation | $\mathcal F\{dx/dt\} = 2\pi i f\,X(f)$ | $3.5\times10^{-15}$ | calculus becomes algebra |
| conjugation | $x$ real $\Rightarrow X(-f) = \overline{X(f)}$ | $0$ | negative frequencies carry no new information |
| Parseval | $\int\lvert x\rvert^2dt = \int\lvert X\rvert^2df$ | $3.5\times10^{-14}$ | energy is the same in either domain |
| convolution | $\mathcal F\{x * h\} = X\cdot H$ | see [01-10-03](./03-convolution.md) | filtering is multiplication |

Three entries deserve emphasis.

**Shift.** A time shift of 5 s leaves the magnitude spectrum identical and
changes only the phase, by exactly $-2\pi f \times 5$. The demo confirms the
magnitudes coincide to all printed figures and the phase prediction is obeyed to
$10^{-16}$. This is why the phase of a seismic wavelet carries the arrival-time
information and the amplitude spectrum does not.

**Scaling.** $x(2t)$ has the transform $\frac{1}{2}X(f/2)$: a pulse twice as
short in time is twice as wide in frequency and half as tall, at every
frequency. The demo checks the value at $f = 0$, 0.5 and 1.0 Hz with differences
below $4\times10^{-14}$. The area under the spectrum is conserved, which is
Parseval read locally.

**Differentiation.** This is the single most useful line in the table and the
reason wave equations are solved in the spectral domain: replace every
$\partial/\partial x$ by $ik$ (or $\partial/\partial t$ by $i\omega$), and a
linear differential equation becomes a polynomial equation in $ik$ and $i\omega$
that can be rearranged. The demo's derivative test agrees to $3.5\times10^{-15}$
relative.

## 5. Differentiation: the ideal operator and the finite-difference operator

The identity converges to a statement with sharp practical consequences: the
*ideal* derivative multiplies the spectrum by $i\omega$, but a finite-difference
operator multiplies it by its own transfer function. For the central difference
with step $h$ that transfer function is

$$\text{central: } i\omega \;\longrightarrow\; \frac{i\sin(\omega h)}{h},
\qquad\text{forward: } i\omega \;\longrightarrow\; \frac{e^{i\omega h}-1}{h}.$$

The demo tabulates both, divided by the ideal $\lvert i\omega\rvert$:

| $f$ (Hz) | $h$ (s) | $\lvert H_{\text{central}}\rvert/\lvert i\omega\rvert$ | phase error (°) | $\lvert H_{\text{forward}}\rvert/\lvert i\omega\rvert$ |
|---|---|---|---|---|
| 0.10 | 0.02 | 0.999974 | 0.000 | 0.999993 |
| 1.00 | 0.02 | 0.997370 | 0.000 | 0.999342 |
| 5.00 | 0.02 | 0.935489 | 0.000 | 0.983632 |
| 10.00 | 0.02 | 0.756827 | 0.000 | 0.935489 |
| 0.10 | 0.10 | 0.999342 | 0.000 | 0.999836 |
| 1.00 | 0.10 | 0.935489 | 0.000 | 0.983632 |
| 5.00 | 0.10 | 0.000000 | 0.000 | 0.636620 |
| 10.00 | 0.10 | 0.000000 | 180.000 | 0.000000 |
| 1.00 | 0.50 | 0.000000 | 0.000 | 0.636620 |
| 5.00 | 0.50 | 0.000000 | 0.000 | 0.127324 |

Read the table as a series of warnings for anyone who differentiates a field by
finite differences and then interprets the result spectrally:

1. The central difference has *exactly* the same $90^\circ$ phase as $i\omega$
   (phase error zero) and its only error is the real amplitude factor
   $\sin(\omega h)/(\omega h)$: a **low-pass filter**, which attenuates precisely
   the high wavenumbers where a rough surface or a thin bed puts its signal.
2. Its response is **exactly zero at $f = 1/(2h)$** — the entry with
   $\lvert H\rvert = 0$ at $f = 5$ Hz, $h = 0.1$ s. The stencil is blind at its
   own Nyquist wavenumber, and flips sign just above it (the $180^\circ$ entry).
3. A forward difference has no blind frequency but a larger amplitude error and a
   first-order phase error, which is why one-sided differences smear dipping
   events.
4. Spectral differentiation with $ik$ has no roll-off at all — but it is global,
   it assumes periodicity, and it amplifies whatever noise sits at the top of the
   band, as [01-10-05](./05-windowing-aliasing.md) and
   [01-10-08](./08-spatial-spectra.md) both show.

## 6. Parseval, and the two normalisation errors everybody makes

For a Gaussian pulse the demo computes both sides of

$$\int_{-\infty}^{\infty}\lvert x(t)\rvert^2dt
= \int_{-\infty}^{\infty}\lvert X(f)\rvert^2df$$

by numerical quadrature on the sampled grid:

| quantity | value |
|---|---|
| $\int \lvert x(t)\rvert^2 dt$ | 0.707106781187 |
| $\int \lvert X(f)\rvert^2 df$ | 0.707106781187 |
| relative difference | $3.5\times10^{-14}$ |

The value is recognisable: for $x = e^{-\pi t^2}$,
$\int e^{-2\pi t^2}dt = 1/\sqrt{2} = 0.70710678\ldots$, so the check has an
exact target, not just self-consistency.

Now the diagnostic ladder. The DFT of the same Gaussian, and its zeroth bin,
read three ways:

| reading | value | what it is |
|---|---|---|
| $X_{\text{DFT}}[0]$ | 50.0000000000 | the *sum* of the samples |
| $X_{\text{DFT}}[0]/N$ | 0.0122070312 | the *mean*, equal to $df\times X(0)$ with $df = 0.012207$ Hz |
| $dt\cdot X_{\text{DFT}}[0]$ | 1.0000000000 | the *integral*, equal to $X(0)$ |

"The FFT is wrong by a factor of $N$" almost always means one of these three was
confused with another. The forward DFT sums; it does not average, and it does not
integrate. The demo makes the cost of confusing them explicit: computing the
Parseval integral while forgetting the $dt$ scaling of $X_{\text{DFT}}$ gives
$1.767767\times10^{3}$ instead of $0.707\times10^{0}$, too large by exactly
$2500 = 1/dt^{2}$; and using $df = 1/N$ instead of $1/(N\,dt)$ gives
$1.414\times10^{-2}$, too small by exactly $50 = 1/dt$ (with $dt = 0.02$ s here).
Both factors are powers of the sampling interval, and both are silent.

## 7. The bridge from the continuous transform to the DFT

For a signal that is negligible outside the window, the DFT and the continuous
transform are related by one sentence:

$$X_{\text{DFT}}[k] \;\approx\; \frac{1}{dt}\,X(f_k)\,
e^{+2\pi i f_k t_0}, \qquad f_k = \frac{k}{N\,dt},$$

where $t_0$ is the time coordinate of sample 0: the DFT is the continuous
transform, *sampled* at the bin frequencies, *multiplied by* $1/dt$, and
*carrying a phase factor* for wherever the time origin sits. The demo verifies
each part on the Gaussian, using a grid whose origin is at $t_0 = -40.96$ s:

| $k$ | $f_k$ (Hz) | $dt\cdot\lvert X_{\text{DFT}}\rvert$ | $e^{-\pi f_k^{2}}$ | magnitude error | phase residual after removing $e^{2\pi if_k t_0}$ |
|---|---|---|---|---|---|
| 0 | 0.00000 | 1.0000000000 | 1.0000000000 | $0$ | $0$ |
| 8 | 0.09766 | 0.9704838065 | 0.9704838065 | $0$ | $9.0\times10^{-16}$ |
| 16 | 0.19531 | 0.8870603603 | 0.8870603603 | $1.1\times10^{-16}$ | $1.5\times10^{-15}$ |
| 24 | 0.29297 | 0.7636504961 | 0.7636504961 | $1.1\times10^{-16}$ | $2.0\times10^{-15}$ |
| 40 | 0.48828 | 0.4728325091 | 0.4728325091 | $5.6\times10^{-16}$ | $2.2\times10^{-15}$ |
| 80 | 0.97656 | 0.0499838050 | 0.0499838050 | $2.2\times10^{-16}$ | $2.4\times10^{-16}$ |

Every normalisation dispute in Fourier practice is a dispute about which of
those three factors ($1/dt$, the bin sampling, or $t_0$) has been dropped. Being
able to write this line from memory is worth more than memorising a table of
transform pairs.

## 8. The uncertainty relation, measured

Define the RMS widths of a signal and its spectrum from their energy densities,

$$\sigma_t^2 = \frac{\int (t-\bar t)^2\lvert x\rvert^2dt}{\int\lvert x\rvert^2dt},
\qquad
\sigma_f^2 = \frac{\int (f-\bar f)^2\lvert X\rvert^2df}{\int\lvert X\rvert^2df}.$$

For $x(t) = e^{-\pi(at)^2}$ the demo computes both numerically for four values
of $a$:

| $a$ | $\sigma_t$ | $\sigma_f$ | product |
|---|---|---|---|
| 0.5 | 0.564190 | 0.141047 | 0.07957747 |
| 1.0 | 0.282095 | 0.282095 | 0.07957747 |
| 2.0 | 0.141047 | 0.564190 | 0.07957747 |
| 4.0 | 0.070524 | 1.128379 | 0.07957747 |

The product is constant at $0.07957747$, and
$1/(4\pi) = 0.07957747$. So
$\sigma_t\sigma_f \ge 1/(4\pi)$ with equality for a Gaussian, in this
convention. The number $1/(4\pi)$ rather than $1/2$ is a direct consequence of
defining the transform in $f$ rather than $\omega$; a paper that quotes
"$\Delta t\Delta f \ge 1/2$" is using the $\omega$ convention and a different
definition of width. **Both statements can be correct at once because the widths
are conventions too — as, of course, is the uncertainty relation's interpretation
as being about measurement rather than about mathematics.**

## 9. Python demonstration

[`code/fourier_transform_demo.py`](./code/fourier_transform_demo.py) implements
every table above and takes under a second to run:

```text
python3 code/fourier_transform_demo.py
```

Two implementation notes.

**The integral is a Riemann sum at arbitrary frequencies.** The function
`numeric_ft` evaluates
$X(f) \approx dt\sum_n x_n e^{-2\pi i f t_n}$ for any list of frequencies, with
the phase of the time origin applied as an explicit exponential. That is why the
transform can be sampled at $f = 0.09766$ Hz without padding the signal.

**The derivative test uses the analytic derivative.** Differentiating
$e^{-((t-t_0)/\sigma)^2}$ by hand avoids confusing the error of a
finite-difference stencil with the error of the transform identity; the
finite-difference roll-off is then measured separately in Section 5, where it
belongs. When you are testing an identity, do not test two approximations at the
same time.

## 10. Common mistakes

1. **Dropping the sign convention.** Write the forward kernel down once per
   project. If a colleague's migration moves energy the wrong way while every
   amplitude looks plausible, this is the first thing to check.
2. **Confusing the transform with the DFT's scaling.** See Section 6: a factor of
   $1/dt$ (usually 10–1000) and a factor of $1/N$ (usually $10^3$–$10^6$) are
   both easy to lose.
3. **Treating the spectrum of a finite record as the spectrum of the signal.**
   The record multiplies the signal by a boxcar, so the measured spectrum is the
   true spectrum convolved with a sinc. This is leakage; it is treated
   quantitatively in [01-10-05](./05-windowing-aliasing.md).
4. **Assuming a real signal's spectrum is symmetric in phase.** Only the
   *magnitude* is even; the phase is odd. Plotting a phase spectrum without
   unwrapping it produces a sawtooth of $2\pi$ jumps that hides the physics.
5. **Using a finite-difference derivative and interpreting it as $i\omega$.**
   Section 5 gives the size of the error, and it is large at the top of the band.
6. **Quoting the time-bandwidth product without its convention.** $1/(4\pi)$,
   $1/2$ and $1$ all appear in the literature; each belongs to a stated
   definition of width and a stated transform convention.

## 11. Real-world applications

- **Upward and downward continuation.** Because the transform of a
  potential-field quantity observed at height $z$ is attenuated by
  $e^{-kz}$ relative to the source plane, moving a field between heights is a
  multiplication by $e^{\pm kz}$ in the wavenumber domain. The exponential
  amplifies high wavenumbers when continuing downward, so the operation is
  stable for only a fraction of the band — the same $1/H$ problem that appears in
  deconvolution in [01-10-03](./03-convolution.md).
- **Thin-slab and flexure response functions.** The elastic plate equation
  becomes a polynomial in $k$ after transformation, so the deflection of the
  lithosphere under a load is obtained as a multiplication — and the resulting
  admittance curve is the observable used in
  [01-10-08](./08-spatial-spectra.md).
- **Wavefield extrapolation.** One-way wave equations are obtained by replacing
  $\partial_z$ with $\pm i k_z$, exactly the differentiation property above; f-k
  migration is the practical realisation of it
  ([01-10-07](./07-2d-fourier.md)).
- **Instrument response.** A sensor's response is a transfer function
  $H(f)$; the recorded signal is the convolution of the ground motion with the
  impulse response, hence a product of transforms. Removing the sensor from a
  record is a division by $H$, with the consequences analysed in
  [01-10-03](./03-convolution.md).
- **Spectroscopic and spectral-element methods.** The same $ik$ substitution is
  what makes spectral methods accurate: derivatives are computed exactly on the
  resolved band rather than approximately.

## 12. Further reading

- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapters 1–6. Level: intermediate. The clearest
  treatment of conventions and of the "which factor goes where" question; its
  table of pairs is the one worth knowing.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T. & Flannery, B. P. (2007).
  *Numerical Recipes* (3rd ed.). Cambridge University Press.** Chapter 13.
  Level: intermediate. Practical, and unusually frank about normalisation
  pitfalls and about differentiating spectral estimates.
- **Bracewell, R. N. (1978). *The Hartley Transform*. Oxford University Press.**
  Level: intermediate. A transform with a symmetric kernel that avoids the
  complex arithmetic — useful to know exists, and a good reminder that the
  Fourier transform is a choice of basis.
- **Stein, E. M. & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*.
  Princeton University Press.** Level: advanced. Where the convergence
  statements and the inversion theorem are proved properly.
- **Gardner, G. H. F., Gardner, L. W. & Gregory, A. R. (1974). Formation
  velocity and density — the diagnostic basics for stratigraphic traps.
  *Geophysics*, 39(6), 770–780.** Level: intermediate. Not about transforms
  directly, but the paper whose convolution model underlies the seismic
  applications above.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 13. Related lessons

- [01 Fourier Series and Periodic Decomposition](./01-fourier-series.md) — the
  discrete-spectrum case this lesson generalises.
- [03 Convolution, Filtering and the Convolution Theorem](./03-convolution.md) —
  the property that makes filtering possible.
- [04 Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) — the
  discrete counterpart, with the $1/dt$ and $t_0$ factors of Section 7 made
  explicit again.
- [05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
  the two ways a finite, sampled record deviates from the ideal transform.
- [06 Hilbert Transform, Analytic Signal and Instantaneous Phase](./06-hilbert-transform.md) —
  a transform defined purely through the conjugation symmetry of Section 4.
- [06-multivariable-calculus/08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md) —
  where $\nabla \to ik$ converts potential theory into algebra.
- [09-partial-differential-equations](../09-partial-differential-equations/README.md) —
  the wave and diffusion equations solved with these operators.

## 14. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/02-fourier-transform-exercises.md`](./exercises/02-fourier-transform-exercises.md).
Solutions: [`exercises/02-fourier-transform-solutions.md`](./exercises/02-fourier-transform-solutions.md).

## Self-assessment checklist

- [ ] I can write the transform pair down with an explicit sign and normalisation
      convention, and say what breaks if the convention is mixed.
- [ ] I can derive the transforms of the Gaussian, the boxcar and a complex
      exponential from the integral.
- [ ] I can state the property table and give the physical meaning of the shift,
      scaling, modulation and differentiation entries.
- [ ] I can explain what a derivative in space becomes in the wavenumber domain,
      and why a finite-difference derivative is not the same operator.
- [ ] I can write the finite-difference transfer function and identify its blind
      frequency.
- [ ] I can verify Parseval numerically and state the two classic factors that
      $1/dt$ and $1/N$ errors introduce.
- [ ] I can relate the DFT of a windowed record to the continuous transform,
      including the $1/dt$ and time-origin phase factors.
- [ ] I can quote the time–bandwidth product for a Gaussian in the stated
      convention and say how it changes with the convention.
