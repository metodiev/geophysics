---
id: 20-03-02
title: "IIR Filter Design: Butterworth, Chebyshev, Elliptic"
level: graduate
prereqs: ["20-03-01", "20-01-04"]
tags: [signal-processing, filtering, iir, butterworth, chebyshev, elliptic, stability, bilinear-transform]
---

# IIR Filter Design: Butterworth, Chebyshev, Elliptic

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the magnitude-squared response of the Butterworth prototype and
   **compute** the order required to meet a specification.
2. **State** the Chebyshev and elliptic magnitude-squared functions, and
   **explain** what each one gives up to gain order.
3. **Map** an analog prototype to a digital filter with the bilinear transform and
   **explain** the frequency warping it introduces.
4. **Measure** the realised ripple and attenuation of a designed filter and
   compare it with the specification.
5. **Verify** stability from the pole locations, not from the impulse response.
6. **Quantify** the phase non-linearity of a causal IIR filter and **explain** why
   it cannot be removed without destroying causality.

## Prerequisites

- [20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares](01-fir-filters.md) —
  the design problem this lesson approaches from the other side.
- [20-01-04 Transfer Functions, Poles and Zeros](../01-signals-and-systems/04-transfer-functions.md) —
  the rational transfer function $H(z) = B(z)/A(z)$ and its pole-zero map.

## 1. Intuition: feedback buys order

An FIR filter of $N$ taps uses $N$ multiplications per output sample. An IIR
filter of order $M$ uses $M$ coefficients in the feedback path and achieves a
much sharper transition for the same $M$, because each stage re-uses the output.
In the demo, a Butterworth IIR needs order 15 to hit a specification that a
47-tap FIR meets — the FIR needs about **9.4 times** as many coefficients.

Nothing is free. The pole that sharpens the amplitude response also bends the
phase response, and a causal IIR filter cannot have exactly linear phase. The
honest way to choose between FIR and IIR is therefore to state which of the two
you need: a prescribed magnitude with unknown phase, or a prescribed magnitude
with *known, zero or constant* phase.

All models and data in this module are SYNTHETIC. The specification below
($f_s = 250$ Hz, $f_p = 40$ Hz, $f_s^{\text{stop}} = 60$ Hz, 1 dB ripple, 60 dB
attenuation) is a chosen teaching specification.

## 2. Definitions

### 2.1 The rational transfer function

An IIR filter is defined by

$$H(z) = \frac{B(z)}{A(z)} = \frac{\sum_{k=0}^{M_b} b_k z^{-k}}
{1 + \sum_{k=1}^{M_a} a_k z^{-k}},$$

giving the recursion $y[n] = \sum_k b_k x[n-k] - \sum_{k\ge 1} a_k y[n-k]$. The
**order** is $\max(M_a, M_b)$.

### 2.2 Stability

$H$ is stable (bounded input, bounded output) if and only if every pole — every
root of $A(z)$ — lies **strictly inside the unit circle**, $|z_k| < 1$. A pole on
the circle gives a marginally stable, undamped resonance; outside it grows
without bound.

### 2.3 Magnitude-squared functions

All three classic prototypes are defined by their magnitude-squared response in
the analog domain, with $\Omega$ the analog angular frequency and $\Omega_c$ the
cutoff:

$$\text{Butterworth:}\quad |H|^2 = \frac{1}{1 + (\Omega/\Omega_c)^{2M}};$$

$$\text{Chebyshev I:}\quad |H|^2 = \frac{1}{1 + \epsilon^2 T_M^2(\Omega/\Omega_c)}
\quad\text{(equiripple passband)};$$

$$\text{Chebyshev II:}\quad |H|^2 = \frac{1}{1 + 1/\big(\epsilon^2
T_M^2(\Omega_s/\Omega)\big)} \quad\text{(equiripple stopband)};$$

$$\text{Elliptic:}\quad |H|^2 = \frac{1}{1 + \epsilon^2 R_M^2(\Omega/\Omega_c)}
\quad\text{(equiripple both)}.$$

$T_M$ is the Chebyshev polynomial and $R_M$ the elliptic rational function. The
design question is: for a given specification, which $M$?

## 3. Derivations

### 3.1 Butterworth order

The Butterworth response is **monotonic** in both bands (no ripple anywhere). Its
order follows from imposing the two edge conditions. At $\Omega_p$ the response
must be $\ge -R_p$ dB, at $\Omega_s$ it must be $\le -R_s$ dB:

$$\left(\frac{\Omega_p}{\Omega_c}\right)^{2M} = 10^{R_p/10}-1, \qquad
\left(\frac{\Omega_s}{\Omega_c}\right)^{2M} = 10^{R_s/10}-1.$$

Dividing eliminates $\Omega_c$:

$$\boxed{\;M \ge
\frac{\log_{10}\!\left(\dfrac{10^{R_s/10}-1}{10^{R_p/10}-1}\right)}
{2\log_{10}\!\left(\dfrac{\Omega_s}{\Omega_p}\right)}.\;}$$

For our specification ($R_p = 1$ dB, $R_s = 60$ dB, $\Omega_s/\Omega_p = 60/40 =
1.5$): numerator $= \log_{10}(10^6-1)/(10^{0.1}-1) = \log_{10}(999999/0.2589)
= \log_{10}(3.862\times10^6) = 6.5868$; denominator $= 2\log_{10}1.5 = 0.35218$;
$M \ge 18.70$. That is the analytic answer, and it assumes the cutoff is chosen
optimally. `buttord` returns **15**, because it chooses $\Omega_c$ inside the
transition band rather than at $\Omega_p$, which is legitimate and buys three
orders. This is worth noticing: the closed-form order is an upper bound for a
pre-specified cutoff, not the minimum order.

### 3.2 The bilinear transform and frequency warping

Digital IIR filters are obtained by mapping the analog prototype through

$$s = \frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}},$$

which maps the left half-plane onto the unit disc (so stability is preserved) and
the imaginary axis onto the unit circle (so the frequency axis maps to itself, but
non-linearly):

$$\Omega = \frac{2}{T}\tan\!\left(\frac{\omega}{2}\right).$$

This **frequency warping** is why the design routines must be given the edges in
digital frequency: `buttord(40, 60, 1, 60, fs=250)` pre-warps internally. If you
design an analog filter at 40/60 Hz and digitise it afterwards, the realised edge
moves. The demo measures the realised attenuation and never assumes the mapping
was exact.

### 3.3 What each prototype gives up

| prototype | passband | stopband | order for our spec |
|---|---|---|---|
| Butterworth | monotonic | monotonic | 15 |
| Chebyshev I | equiripple ($R_p$) | monotonic | 8 |
| Chebyshev II | monotonic | equiripple ($R_s$) | 8 |
| Elliptic | equiripple | equiripple | 5 |

The measured responses confirm the specification is met and show the cost:

| prototype | measured ripple (dB) | measured attenuation (dB) | max pole |
|---|---|---|---|
| Butterworth (15) | 2.997 | 69.80 | 0.915315 |
| Chebyshev I (8) | 1.000 | 66.60 | 0.970827 |
| Chebyshev II (8) | 0.240 | 60.00 | 0.875686 |
| Elliptic (5) | 1.000 | 60.00 | 0.941077 |

Two readings matter. First, the Butterworth *ripple* is measured as 2.997 dB
even though $R_p = 1$ dB was requested: at order 15 the response has fallen only
about 0.1 dB at 40 Hz, so the maximum is at DC and the minimum at the passband
edge, and the "-3 dB" convention of `buttord` places the edge further out. The
number is a measurement of the realised design, not a violation of the
specification, which is about the *filter* rather than about `buttord`'s
convention. Second, all four filters meet the 60 dB requirement, and the order
falls from 15 to 5 as ripples appear.

## 4. Stability, verified

The demo takes `np.roots(a)` for each design and prints the largest pole
magnitude. All four are below 1, so all four are stable. The Chebyshev I filter
has the largest pole (0.970827) because its ripple is concentrated near the
band edge, closest to the unit circle. This is the correct check: a pole at
$|z| = 0.97$ decays as $0.97^n$, which is slow but bounded. Reading stability off
a plotted impulse response is unreliable; reading it off $|z_k|$ is exact.

## 5. Phase: the unavoidable cost

For a causal, stable, rational $H(z)$ with at least one pole away from the origin,
the phase cannot be exactly linear — that is a theorem, not an implementation
detail. The demo measures the peak-to-peak passband group delay:

| prototype | mean group delay (samples) | peak-to-peak variation (samples) |
|---|---|---|
| Butterworth | 11.878 | 15.191 |
| Chebyshev I | 9.822 | 32.916 |
| Chebyshev II | 4.227 | 5.745 |
| Elliptic | 5.324 | 15.517 |

Chebyshev I has the worst dispersion (a 33-sample swing) because its poles sit
closest to the unit circle and its group delay peaks sharply near the passband
edge. Chebyshev II, whose ripple is in the stopband, is the gentlest of the four.
None of them is constant. For a filter on a waveform whose *shape* carries
information — a converted phase, an AVO gradient, a moment-tensor polarity —
that variation is a distortion, and it must be either corrected or avoided
([04](04-phase-and-zero-phase.md)).

## 6. Worked example (SYNTHETIC)

Specification: $f_s = 500$ Hz, passband to 25 Hz with 0.5 dB ripple, stopband from
50 Hz with 55 dB attenuation. Choose a design.

1. Normalised edges: $f_p/f_s = 0.05$, $f_s^{\text{stop}}/f_s = 0.10$; the ratio
   is $2.0$.
2. Chebyshev I order, from the standard closed form
   $M \ge \dfrac{\cosh^{-1}\!\sqrt{(10^{R_s/10}-1)/(10^{R_p/10}-1)}}
   {\cosh^{-1}(\Omega_s/\Omega_p)}$:
   numerator term
   $(10^{5.5}-1)/(10^{0.05}-1) = (316227-1)/(0.1220) = 2.592\times10^6$;
   $\sqrt{\cdot} = 1610$; $\cosh^{-1}(1610) = \ln(1610 + \sqrt{1610^2-1}) = \ln(3220)
   = 8.077$. Denominator: $\cosh^{-1}(2) = \ln(2+\sqrt{3}) = 1.3170$. So
   $M \ge 6.13$, i.e. $M = 7$. `cheb1ord(25, 50, 0.5, 55, fs=500)` confirms 7.
3. An elliptic design needs fewer orders because it ripples *both* bands:
   `ellipord` returns **5** for the same specification. The Chebyshev I formula
   above is not the elliptic degree equation; the elliptic one replaces
   $\cosh^{-1}(\Omega_s/\Omega_p)$ with a ratio of complete elliptic integrals,
   which is why the closed form is rarely written out by hand and the library
   routine is used instead.
4. Stability: the demo's analogous 5th-order design has max pole magnitude
   0.941 — stable.
5. Group delay: expect several samples of delay with a swing of order 10× the
   mean near the edge. If the application needs the waveform undistorted,
   pre-warp or use a zero-phase implementation.

The example shows the two independent facts that decide the design: the **order**
is set by the ratio of the transition width to the band edges and by the required
ripple; the **phase** is set by how close the poles are to the unit circle, which
the order controls.

## 7. Assumptions and regime of validity

1. **The prototype is designed in the analog domain and mapped by the bilinear
   transform.** The mapping is exact for the *specified* edges but warps every
   other frequency; if you care about a frequency in between, measure it.
2. **The design is for a single, fixed specification.** Changing the specification
   changes the order, and sometimes by more than one.
3. **Coefficients are represented exactly.** High-order IIR filters are sensitive
   to coefficient quantisation: a 15th-order Butterworth in direct form II is
   numerically fragile in single precision. Real implementations use cascaded
   second-order sections (`sos`), which the demo does not need at double
   precision.
4. **The filter is causal.** Every phase statement above assumes causality. If
   you filter forward and backward, the effective filter is non-causal and
   zero-phase — see [04](04-phase-and-zero-phase.md).
5. **The input is band-limited below Nyquist.** An IIR lowpass does not undo
   aliasing; if the record is already aliased, no filter helps
   ([03](03-filter-applications.md)).

## 8. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| order | $M$ | dimensionless | number of poles |
| ripple | $R_p$ | dB | $10\log_{10}(1+\epsilon^2)$ |
| attenuation | $R_s$ | dB | $10\log_{10}(1+\cdots)$ |
| normalised frequency | $\omega$ | rad/sample | $2\pi f/f_s$ |
| pole magnitude | $|z_k|$ | dimensionless | $<1$ for stability |
| group delay | $\tau_g$ | samples | $\mathrm{d}\phi/\mathrm{d}\omega$ |

The order is dimensionless and must come out as an integer after rounding up;
a non-integer order means you have not finished the design. A pole magnitude
with units is a dimensional-analysis error.

## 9. Python demonstration

`code/iir_filters_demo.py` designs all four prototypes for one specification and
prints the order each needs, the measured ripple and attenuation, the pole
magnitudes, the group-delay statistics, and the FIR-versus-IIR coefficient count.
It is self-contained, seeded with `np.random.default_rng(20261014)`, and exits 0.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/02-iir-filters-exercises.md`](exercises/02-iir-filters-exercises.md) and
[`exercises/02-iir-filters-solutions.md`](exercises/02-iir-filters-solutions.md).

- **★** Compute the Butterworth order for $f_p = 10$ Hz, $f_s^{\text{stop}} =
  20$ Hz, $R_p = 3$ dB, $R_s = 40$ dB, $f_s = 100$ Hz.
- **★★** Explain why the demo's Butterworth design measures 2.997 dB of ripple
  when 1 dB was requested.
- **★★** Measure the group delay of an elliptic filter of order 3 and of order 9
  and state how the dispersion scales.
- **★★★** Show numerically that breaking the symmetry of a linear-phase FIR
  filter produces a group delay variation of the same order as a causal IIR
  filter of comparable magnitude response.

## Mastery checkpoint

Complete this without notes:

> A 1000 Hz-sampled seismic channel must keep 0–15 Hz with less than 0.5 dB of
> ripple and reject 45 Hz and above by 50 dB. **(a)** Compute the order an
> elliptic design needs, using the closed-form degree equation. **(b)** State the
> order Chebyshev I would need, and why it is higher or lower. **(c)** State
> whether the design is stable and how you verified it. **(d)** Estimate the
> group delay at 14 Hz relative to 1 Hz and explain in one sentence what that
> does to a wavelet. **(e)** State one reason you might still choose an FIR
> design.

A worked version appears in the
[solutions](exercises/02-iir-filters-solutions.md).

## Common pitfalls

1. **Quoting the *requested* ripple rather than the measured one.** Always measure
   $|H|$ from the realised coefficients.
2. **Checking stability by eye.** Compute `np.abs(np.roots(a)).max()` and compare
   with 1.
3. **Using a high-order filter in single precision.** Cascade second-order
   sections (`sos`) instead of one long direct-form filter.
4. **Assuming linear phase.** A causal IIR filter is dispersive; the demo's
   Chebyshev I swings 33 samples across the passband.
5. **Confusing "monotonic" with "no distortion".** A Butterworth response is
   monotonic in *magnitude*; its *phase* is still non-linear.

## Related modules

- [20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares](01-fir-filters.md) —
  the alternative design family.
- [20-01-04 Transfer Functions, Poles and Zeros](../01-signals-and-systems/04-transfer-functions.md) —
  the pole-zero picture used for stability.
- [20-03-04 Phase Response, Zero-Phase Filtering and Distortion](04-phase-and-zero-phase.md) —
  how to remove the phase cost of an IIR design.
- [20-03-03 Filter Selection for Geophysical Data](03-filter-applications.md) —
  choosing an order in practice.
- [01-11-05 The z-Transform and Discrete Linear Systems](../../01-mathematics/11-complex-analysis/05-z-transform.md) —
  the transform that makes stability a statement about pole radii.
- [03-03-05 SciPy for Scientific Computing](../../03-scientific-computing/03-scipy/05-signal.md) —
  `butter`, `cheby1`, `cheby2`, `ellip` and their `ord` companions.
