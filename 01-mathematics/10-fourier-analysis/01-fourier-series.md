---
id: 01-10-01
title: "Fourier Series and Periodic Decomposition"
level: intermediate
prereqs: ["01-03-05", "01-05-05", "01-05-07"]
estimated_minutes: 90
tags: [fourier-series, tides, harmonic-analysis, periodicity, spectral-analysis]
---

# Fourier Series and Periodic Decomposition

## Learning objectives

By the end of this lesson you will be able to:

1. **Express** any reasonable periodic function as a sum of harmonics, in both
   the trigonometric and the complex-exponential form, and convert between them.
2. **Derive** the Fourier coefficients from orthogonality rather than quote
   them, and state the conditions under which the series converges.
3. **Interpret** an amplitude-and-phase spectrum physically, and explain why the
   amplitude spectrum alone loses information that a tide or seismic analyst
   needs.
4. **Decompose** a periodic geophysical record into tidal constituents, and
   explain why the decomposition requires a record length given by the Rayleigh
   criterion $T > 1/|\Delta f|$.
5. **Quantify** how the uncertainty of each constituent depends on the record
   length, using the normal matrix of the harmonic fit rather than a rule of
   thumb.
6. **Recognise** the Gibbs phenomenon and explain why truncating a series
   overshoots at a jump by a fixed fraction of the jump.

## Prerequisites

[01-03-05 Phase, Harmonics and Superposition of Oscillations](../03-trigonometry/05-phase-and-harmonics.md) —
for the amplitude/phase description of a sinusoid;
[01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md) —
for the integrals that extract the coefficients;
[01-05-07 Sequences, Series and Convergence Tests](../05-single-variable-calculus/07-sequences-and-series.md) —
for what "the series converges" means.

## 1. Intuition: a periodic record is a list of frequencies

A tide gauge at a port records a continuously varying water level. Plot a month
of it and the dominant pattern is obvious: the water rises and falls roughly
twice a day. Plot a year and a second pattern appears on top of the first — the
twice-daily range grows and shrinks over about a fortnight (spring and neap
tides) and again over about a month (perigean and apogean tides).

Nothing about the *physics* of that record is harmonic. The Moon and Sun pull on
a rotating, tilted, ellipsoidal Earth with an ocean of finite depth on a solid
body with its own free oscillations, and the resulting water level is a
horrendously complicated response. Yet the *record* — and this is the empirical
miracle that made tidal prediction possible centuries before tidal theory —
behaves as though it were a sum of a few dozen pure sinusoids with constant
amplitudes and phases.

Fourier's theorem is the statement that this is not a miracle but a
mathematical certainty: any reasonable periodic function, whatever its physical
origin, *is* a sum of harmonics. The tide is the best-documented example in
geophysics, and this lesson uses it throughout, because tidal analysis is where
every concept in the module — orthogonality, amplitude and phase spectra,
truncation, resolution, uncertainty — is forced to be operational rather than
decorative.

## 2. Precise definitions

### 2.1 Periodicity and harmonics

A function $f$ is **periodic with period $T$** if $f(t+T) = f(t)$ for all $t$.
Its **fundamental angular frequency** is $\omega_0 = 2\pi/T$.

The functions $\cos(n\omega_0 t)$ and $\sin(n\omega_0 t)$ for integers
$n = 1, 2, 3, \ldots$ are the **harmonics** of the fundamental: the $n$-th
harmonic completes exactly $n$ cycles in each period.

### 2.2 Orthogonality on a period

The whole method rests on three integrals, valid for integers $m, n$:

$$\int_0^T \cos(n\omega_0 t)\cos(m\omega_0 t)\,dt
= \begin{cases} T/2, & m = n \ge 1,\\ T, & m = n = 0,\\ 0, & m \ne n,\end{cases}$$

$$\int_0^T \sin(n\omega_0 t)\sin(m\omega_0 t)\,dt
= \begin{cases} T/2, & m = n \ge 1,\\ 0, & \text{otherwise},\end{cases}
\qquad
\int_0^T \cos(n\omega_0 t)\sin(m\omega_0 t)\,dt = 0 .$$

The demo evaluates these numerically by the trapezoidal rule on
$[0, 2\pi]$ with 20 000 intervals. For $m = n = 3$ it returns
$3.141593$ for both $\langle\cos,\cos\rangle$ and $\langle\sin,\sin\rangle$,
which is $\pi$ to six figures; for $m = 3$, $n = 5$ it returns
$0.000000$; for $m = n = 0$ it returns $6.283185 = 2\pi$ for
$\langle\cos,\cos\rangle$ and exactly $0$ for $\langle\sin,\sin\rangle$. The
mixed integral $\langle\cos,\sin\rangle$ comes out at the $10^{-16}$ level,
which is round-off.

**Read those numbers as a recipe.** Because distinct harmonics are orthogonal,
multiplying a signal by one harmonic and integrating *projects out* that
harmonic's coefficient and kills every other term in the sum. That is the entire
content of the Fourier coefficient formula, and it is why the "transform" is
really an inner product.

### 2.3 The Fourier series

For a periodic function $f$ with period $T$:

$$\boxed{\;f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\left[
a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)\right]\;}$$

with the **Euler formulas**

$$a_n = \frac{2}{T}\int_0^T f(t)\cos(n\omega_0 t)\,dt, \qquad
b_n = \frac{2}{T}\int_0^T f(t)\sin(n\omega_0 t)\,dt,$$

and $a_0 = \frac{2}{T}\int_0^T f(t)\,dt$, which is twice the mean value. The
$1/2$ on the constant term in the series is what makes $a_0$ the coefficient
formula's natural output rather than a special case.

### 2.4 Amplitude–phase form

A pair of coefficients at one harmonic is a single sinusoid:

$$a_n\cos(n\omega_0 t) + b_n\sin(n\omega_0 t)
= A_n\cos(n\omega_0 t - \phi_n),$$

$$A_n = \sqrt{a_n^2 + b_n^2}, \qquad \phi_n = \arctan_2(b_n, a_n).$$

$A_n$ is the **amplitude** and $\phi_n$ the **phase lag**. Tidal analysis quotes
$A$ and $\phi$ (called $H$ and $g$ in the tidal literature) because they are
what a harbour needs: $A$ sets the range, $g$ sets when high water occurs.

### 2.5 Complex form

Using $\cos\theta = (e^{i\theta} + e^{-i\theta})/2$,

$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{in\omega_0 t}, \qquad
c_n = \frac{1}{T}\int_0^T f(t) e^{-in\omega_0 t}\,dt,$$

with $c_0 = a_0/2$ and, for $n \ge 1$, $c_n = (a_n - i b_n)/2$ and
$c_{-n} = \overline{c_n}$. The complex form is the one that generalises to the
Fourier transform in
[01-10-02](./02-fourier-transform.md), and the factor pattern —
$1/T$ forward, none in the sum — is the same convention used for the DFT in
[01-10-04](./04-discrete-fourier.md).

## 3. Derivation of the coefficient formulas

Take the series, multiply by $\cos(m\omega_0 t)$ and integrate term by term over
one period. Term by term:

- the constant $\frac{a_0}{2}$ gives $\frac{a_0}{2}\int_0^T\cos(m\omega_0 t)dt = 0$
  for $m \ge 1$;
- $\sum_n a_n \cos(n\omega_0 t)\cos(m\omega_0 t)$ leaves only $n = m$, giving
  $a_m T/2$;
- $\sum_n b_n \sin(n\omega_0 t)\cos(m\omega_0 t)$ gives $0$ by the mixed
  orthogonality.

Therefore $\int_0^T f(t)\cos(m\omega_0 t)dt = a_m T/2$, which is the formula for
$a_m$. The same argument with $\sin(m\omega_0 t)$ gives $b_m$. **Nothing else is
required**: the coefficients are what you get when you ask the signal how much of
each harmonic it contains.

Term-by-term integration is legitimate when the series converges uniformly. For
piecewise-smooth $f$ — finitely many jumps and corners per period — the series
converges at every point of continuity, and at a jump it converges to the
*average* of the two one-sided limits. That is the **Dirichlet condition**, and
it is satisfied by every physical record.

## 4. Properties worth knowing before computing

**Linearity.** If $f$ and $g$ have coefficients $(a_n,b_n)$ and $(a'_n,b'_n)$,
then $\alpha f + \beta g$ has $(\alpha a_n + \beta b_n, \alpha a'_n + \beta b'_n)$.
Two signals added means two spectra added: this is why separating overlapping
tidal signals is a *resolution* problem, not a linearity problem.

**Time shift.** If $f(t) \to f(t - t_0)$ then the coefficients become
$a_n\cos(n\omega_0t_0) \mp b_n\sin(n\omega_0 t_0)$ — the amplitude $A_n$ is
unchanged and the phase changes by $n\omega_0 t_0$. A time shift touches phase
only. Tidal phase lags $g$ are quoted relative to a fixed epoch for exactly this
reason; without the epoch, $g$ is meaningless.

**Differentiation.** Term-by-term differentiation multiplies the $n$-th complex
coefficient by $in\omega_0$. In the notation of the next lesson, a derivative in
time multiplies the spectrum by $i\omega$; in space, by $ik$. This single
property turns differential equations into algebra, and it is the reason
spectral methods compete with finite differences at all.

**Parseval.** The mean square of the signal is the sum of the squares of the
coefficients:

$$\frac{1}{T}\int_0^T f(t)^2\,dt = \frac{a_0^2}{4}
+ \frac{1}{2}\sum_{n\ge1}\left(a_n^2 + b_n^2\right)
= \frac{1}{2}\sum_n A_n^2 .$$

So the variance of a record is distributed across its harmonics, and a "variance
spectrum" is a legitimate way to present the decomposition.

**Gibbs phenomenon.** Truncating the series gives the best least-squares
approximation with that many terms, but near a jump the partial sum overshoots
the function by a *fixed fraction of the jump*, no matter how many terms you
keep. The demo computes the partial sums of the square wave
$\mathrm{sign}(\sin t)$ — whose odd-harmonic coefficients are $4/(n\pi)$ — and
measures the maximum:

| odd harmonics kept | maximum of partial sum | overshoot | as a fraction of the jump |
|---|---|---|---|
| 1 | 1.273240 | +0.273240 | 13.662% |
| 3 | 1.200422 | +0.200422 | 10.021% |
| 9 | 1.182328 | +0.182328 | 9.116% |
| 25 | 1.179473 | +0.179473 | 8.974% |
| 99 | 1.179013 | +0.179013 | 8.951% |
| 199 | 1.178988 | +0.178988 | 8.949% |

The jump is $2$, so the limiting overshoot is $0.178988/2 = 8.949\%$ of the
jump. Adding terms does not shrink it: it moves the overshoot closer to the
discontinuity, where it remains. Every sharp-cutoff filter in this module is a
truncated series and carries the same artefact
([01-10-03](./03-convolution.md), Section 7).

## 5. The running example: tidal harmonic analysis

### 5.1 Why tides are a Fourier series

The tide-generating potential has a discrete spectrum, because the Moon's orbit
is periodic (to good approximation) in several independent ways. Each periodic
element produces a line in the spectrum, and each line has a conventional name
and a conventional angular speed in degrees per hour. The demo uses seven of the
largest, and reports the periods implied by those speeds:

| constituent | speed (deg/h) | period (h) | period (d) | frequency (cyc/h) |
|---|---|---|---|---|
| M2 principal lunar semidiurnal | 28.9841042 | 12.42060 | 0.51753 | 0.08051140 |
| S2 principal solar semidiurnal | 30.0000000 | 12.00000 | 0.50000 | 0.08333333 |
| N2 larger lunar elliptic semidiurnal | 28.4397295 | 12.65835 | 0.52743 | 0.07899925 |
| K2 lunisolar semidiurnal | 30.0821373 | 11.96723 | 0.49863 | 0.08356149 |
| K1 lunisolar diurnal | 15.0410686 | 23.93447 | 0.99727 | 0.04178075 |
| O1 principal lunar diurnal | 13.9430356 | 25.81934 | 1.07581 | 0.03873065 |
| P1 principal solar diurnal | 14.9589314 | 24.06589 | 1.00275 | 0.04155259 |

These speeds are the classical Doodson values and are physical constants of the
Sun–Earth–Moon system; the *amplitudes and phases* used in the demo are
**SYNTHETIC** (chosen for readability, not fitted to any station). The two
diurnal speeds differ by only 0.082 deg/h, and the same is true of the pair S2
and K2 — a fact that determines how long a record must be, as Section 5.3 shows.

### 5.2 The Rayleigh criterion

If a record of length $T$ is decomposed into constituents, two constituents whose
frequencies differ by $\Delta f$ can be separated only if the record contains at
least one full beat of their difference:

$$T > \frac{1}{|\Delta f|} \qquad \text{(Rayleigh criterion).}$$

The demo computes the requirement for each pair:

| pair | $\lvert\Delta f\rvert$ (cyc/h) | required record |
|---|---|---|
| M2–S2 | 0.00282193 | 354.37 h = 14.765 d |
| M2–N2 | 0.00151215 | 661.31 h = 27.555 d |
| K1–O1 | 0.00305009 | 327.86 h = 13.661 d |
| M2–K2 | 0.00305009 | 327.86 h = 13.661 d |
| O1–P1 | 0.00282193 | 354.37 h = 14.765 d |

The pairwise requirement is not the whole story: a constituent must be separated
from *all* its neighbours, and the binding constraint is the closest neighbour.
For S2, K2, K1 and P1 that neighbour is 0.082 deg/h away, so 182.6 days is the
threshold — which is why classical tidal analysis uses records of a month to a
year and why the S2/K2 and K1/P1 pairs are routinely estimated as a group rather
than separately.

Note the arithmetic identity: $T > 1/|\Delta f|$ means the frequency separation
must exceed the bin spacing $df = 1/T$. The Rayleigh criterion *is* the
statement that two tones must be more than one transform bin apart. Everything
awkward about short records follows from that, as
[01-10-05](./05-windowing-aliasing.md) develops.

### 5.3 What a short record actually does

The demo synthesises 14-, 30- and 60-day hourly records from the seven
constituents and compares two analyses.

**Bin amplitudes.** Reading the amplitude of each constituent off the nearest
transform bin gives, for a 60-day record:

| | true amplitude (m) | nearest bin offset (cyc/h) | $2\lvert X\rvert/N$ (m) |
|---|---|---|---|
| M2 | 1.20 | 0.00004416 | 1.2199 |
| S2 | 0.40 | 0.00000000 | 0.4753 |
| N2 | 0.24 | 0.00016742 | 0.1823 |
| K2 | 0.11 | 0.00022816 | 0.4753 |
| K1 | 0.30 | 0.00011408 | 0.3592 |
| O1 | 0.18 | 0.00015823 | 0.1675 |
| P1 | 0.10 | 0.00011408 | 0.3592 |

Even a 60-day record cannot put these constituents on bins, so the read-off
amplitudes are wrong: S2 reads 0.475 instead of 0.400, K2 reads the same 0.475
as S2 (they share a bin), and P1 reads 0.359 instead of 0.100 because it shares
a bin with K1. **Reading peaks off a transform is not harmonic analysis.**

**Least squares at the exact frequencies.** Fitting the mean plus a cosine and a
sine at each of the seven known speeds — 15 unknowns, solved by normal equations
— recovers every constituent *exactly* from the noise-free data, even the 14-day
record. That is the lesson most textbooks omit: a short record does not make the
system singular, it makes it **ill-conditioned**. The parameters exist; their
uncertainty is what explodes.

**Noise gain.** The demo computes the formal standard error of each amplitude
from $\sigma^2 (A^{\mathsf T}A)^{-1}$ of the normal matrix, with
$\sigma = 0.0200$ m white noise:

| constituent | Rayleigh (d) | 14 d (mm) | 30 d (mm) | 60 d (mm) | 365 d (mm) |
|---|---|---|---|---|---|
| M2 | 27.6 | 3.43 | 1.09 | 0.75 | 0.30 |
| S2 | 182.6 | 18.99 | 3.70 | 1.34 | 0.30 |
| N2 | 27.6 | 2.91 | 1.07 | 0.75 | 0.30 |
| K2 | 182.6 | 18.66 | 3.74 | 1.35 | 0.30 |
| K1 | 182.6 | 13.55 | 3.71 | 1.35 | 0.30 |
| O1 | 14.8 | 1.85 | 1.08 | 0.75 | 0.30 |
| P1 | 182.6 | 13.59 | 3.69 | 1.35 | 0.30 |

The pattern follows the *nearest-neighbour separation*, not the size of the
constituent: K2, whose amplitude is 0.110 m, carries an 18.66 mm uncertainty on a
14-day record (17% of its own amplitude), because it is nearly degenerate with
S2. Well-separated M2 and O1 are already good at 14 days. As a percentage of
their own amplitudes the 14-day errors are 16.97% for K2, 13.59% for P1, 4.75%
for S2, 4.52% for K1 and under 1.3% for the rest.

A Monte-Carlo check with 24 noise realisations confirms the prediction: the
observed RMS errors are within a factor of about 1.4 of the predicted values,
consistent with the roughly 14% random error of an RMS estimated from 24
samples.

### 5.4 Spring and neap tides are a beat

The spring–neap cycle is nothing more than the beat of M2 against S2. Their
frequency difference is 0.00282193 cyc/h, giving

$$T_{\text{beat}} = \frac{1}{0.00282193} = 354.37\ \text{h} = 14.765\ \text{days}.$$

Taking the analytic envelope
$\lvert A_{M2}e^{i(\omega_{M2}t-\phi_{M2})}
+ A_{S2}e^{i(\omega_{S2}t-\phi_{S2})}\rvert$ of the two constituents
($A_{M2} = 1.20$ m, $A_{S2} = 0.40$ m), the demo finds successive maxima at
$t = 19.5$ h, 374.0 h and 728.5 h — a mean gap of 354.5 h against the
theoretical 14.765 d — with the envelope ranging between $A_{M2}-A_{S2} = 0.800$ m
and $A_{M2}+A_{S2} = 1.600$ m. The full range is reached at springs and equals
the sum of the amplitudes; at neaps it is the difference.

The same arithmetic gives the perigean cycle: the M2/N2 difference of
0.00151215 cyc/h is a 661.31 h = 27.555-day beat, which is close to the
anomalistic month. **Every apparent "cycle" in a tidal record is a beat between
two constituents, and once the constituents are known the modulations are
predictable rather than mysterious.**

## 6. Python demonstration

The companion script is
[`code/fourier_series_demo.py`](./code/fourier_series_demo.py). It requires only
the standard library and runs in about two seconds. Run it with

```text
python3 code/fourier_series_demo.py
```

Sections 1–5 of the script correspond to the tables above. Two implementation
details in it are worth studying.

**The fit is a genuine least-squares inversion.** The basis
$\{1, \cos(\omega_i t), \sin(\omega_i t)\}$ is *not* orthogonal over a finite
record: a 30-day record holds only about two beats of M2 against S2, so the
cosine of one constituent is not exactly orthogonal to the cosine of another.
The code therefore forms the normal equations $A^{\mathsf T}A\,c = A^{\mathsf T}b$
and solves them by Gaussian elimination with partial pivoting. Projecting each
constituent out independently — the tempting shortcut — is wrong whenever the
record is shorter than a few beats.

**The uncertainty comes from the same matrix.** One extra solve per parameter
gives the entries of $(A^{\mathsf T}A)^{-1}$ needed for the standard errors, and
the delta method is used for the amplitude:

$$\operatorname{Var}(A) = \frac{a^2 d_{11} + 2ab\,d_{12} + b^2 d_{22}}{a^2+b^2},
\qquad d_{ij} = \sigma^2\left[(A^{\mathsf T}A)^{-1}\right]_{ij}.$$

The cross term matters: on this synthetic record the cos and sin coefficients of
one constituent are *not* equally well determined, and dropping $d_{12}$ inflated
the predicted errors by 30–45% until the term was restored. The corrected
predictions then matched the Monte-Carlo scatter.

Also worth noting: the demo reports phases on $[0^\circ, 360^\circ)$. A phase of
$-150^\circ$ and one of $210^\circ$ are the same angle, and tidal phases are
conventionally quoted modulo $360^\circ$; printing the principal value of
$\arctan_2$ without wrapping produces a table that looks wrong but is not.

## 7. Common mistakes

1. **Reading amplitudes off transform bins.** As Section 5.3 shows, this
   over-estimates S2 by 19% and P1 by 259% on a 60-day record, and it silently
   merges constituents that share a bin.
2. **Believing a short record makes the parameters undefined.** They are defined
   and computable; what changes is their uncertainty. Report the uncertainty.
3. **Treating the Rayleigh criterion as a cliff.** It is the convention "one full
   beat fits in the record". The quantitative statement is the noise gain from
   $(A^{\mathsf T}A)^{-1}$, which varies smoothly, and a constituent separated by
   less than its neighbour's Rayleigh limit can still be estimated if the noise
   is low enough.
4. **Forgetting that the phase needs an epoch.** $\phi_n$ is meaningless without
   a stated time origin, because a time shift changes every phase and no
   amplitude.
5. **Assuming the coefficients of a physical signal are constants.** They are
   not: the M2 amplitude at a real port varies over decades. A harmonic fit is a
   model of the record, and the statement "the M2 amplitude is 1.20 m" is only
   as good as the assumption that it did not change during the record.
6. **Confusing the two forms' factors.** In the trigonometric form the mean is
   $a_0/2$; in the complex form the $n = 0$ coefficient is the mean. Mixing them
   produces a factor-of-two error in the constant term that is easy to miss
   because the constant term is usually uninteresting.

## 8. Real-world applications

- **Tidal prediction and datum computation.** Harmonic analysis of a port record
  yields amplitudes and phase lags for a set of constituents; summing them
  forward predicts the tide for any future date. National chart datums are
  defined from such analyses, and the required record length is a direct
  consequence of Section 5.3.
- **Loading and Earth tides.** The same decomposition applied to gravity and
  strain records separates the solid-Earth tidal response (M2, O1, ...) from
  ocean loading, and the amplitudes give the Love numbers. The constituent
  speeds are identical to the oceanographic ones.
- **Instrument calibration by injecting a known harmonic.** A long-period
  sinusoidal pressure or acceleration signal is a legitimate way to calibrate a
  broadband sensor, because the response at one frequency can be measured very
  precisely.
- **Seasonal cycles in climate and geodesy.** The annual and semi-annual terms
  of a temperature, sea-level or GRACE mass record are the first two harmonics of
  a 1-year period; the same fit machinery estimates them and their uncertainties.
- **Orbital and rotational signals.** The forced nutation and the small
  periodic terms in Earth rotation are handled as harmonic decompositions with
  empirically refined frequencies — the technique is identical to tidal
  analysis, only the physics of the frequencies differs.

## 9. Further reading

- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapters 1–4. Level: intermediate. The standard
  engineering treatment; its chapter on the Fourier series is the clearest on
  the two forms and their factor conventions.
- **Pugh, D. T. (1987). *Tides, Surges and Mean Sea-Level*. Wiley.** Level:
  intermediate to advanced. The classical account of tidal analysis, including
  the Rayleigh criterion, the synodic and anomalistic beats, and the practical
  tables of constituent speeds.
- **Parker, R. L. (1994). *Geophysical Inverse Theory*. Princeton University
  Press.** Chapter 2. Level: graduate. Where the least-squares fit and the
  $A^{\mathsf T}A$ covariance used in Section 5.3 come from, in exactly the
  notation a geophysicist needs.
- **Courant, R. & Hilbert, D. (1953). *Methods of Mathematical Physics*,
  Vol. I.** Chapter 1. Level: advanced. Convergence, Dirichlet conditions, and
  the rigorous statement of what "the series represents the function" means.
- **Wilbraham, H. (1848) and Gibbs, J. W. (1899).** The original notices of the
  overshoot in Section 4. Historical, but the modern discussion in any analysis
  text is easier to use.
- **Doodson, A. T. (1921). The harmonic development of the tide-generating
  potential.** *Proceedings of the Royal Society A*, 100, 305–329. The origin of
  the constituent speeds tabulated in Section 5.1.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 10. Related lessons

- [02 The Fourier Transform and Its Properties](./02-fourier-transform.md) —
  what happens to the series when the period goes to infinity.
- [04 Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) — the
  finite, sampled version of the same projection, with the conventions that
  Section 2.5 anticipates.
- [05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
  why the nearest-bin amplitudes in Section 5.3 are wrong, quantified.
- [03-trigonometry/05 Phase, Harmonics and Superposition of Oscillations](../03-trigonometry/05-phase-and-harmonics.md) —
  the superposition identity used in Section 2.4.
- [05-single-variable-calculus/07 Sequences, Series and Convergence Tests](../05-single-variable-calculus/07-sequences-and-series.md) —
  the convergence machinery behind Section 3.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — tidal gravity and
  the use of harmonic fits to separate Earth and ocean tides in field data.
- [20-signal-processing](../../20-signal-processing/README.md) — the processing
  context for everything in this module.

## 11. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/01-fourier-series-exercises.md`](./exercises/01-fourier-series-exercises.md).
Solutions: [`exercises/01-fourier-series-solutions.md`](./exercises/01-fourier-series-solutions.md).

## Self-assessment checklist

- [ ] I can write the trigonometric and complex forms of the Fourier series and
      convert between them without a reference.
- [ ] I can derive $a_n$ and $b_n$ from orthogonality, including the $T/2$ factor.
- [ ] I can convert $(a_n,b_n)$ to $(A_n,\phi_n)$ and explain what each means for
      a tide gauge record.
- [ ] I can state the Rayleigh criterion and compute the required record length
      for a given pair of constituents.
- [ ] I can explain why a 14-day record gives large S2 and K2 uncertainty even
      though the fit is formally exact.
- [ ] I can explain the Gibbs overshoot as a fixed fraction of a jump.
- [ ] I can compute the beat period of two constituents and connect it to
      spring–neap modulation.
- [ ] I can state Parseval's relation for a Fourier series and interpret it as a
      variance budget.
