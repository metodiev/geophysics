---
id: 06-05-01
title: "Measuring Q: Spectral Ratio, Rise Time, Multiple Methods"
level: graduate
prereqs: ["06-01-01", "06-01-02", "06-02-02"]
tags: [seismology, attenuation, quality-factor, spectral-ratio, t-star, anelasticity]
---

# Measuring Q: Spectral Ratio, Rise Time, Multiple Methods

A seismogram carries two kinds of information about the medium it crossed: how
long the wave took, and how much of it was left. The first gives velocity; the
second gives **attenuation**. Attenuation is the only routine seismic observable
that responds directly to temperature, to the presence of fluid, and to the
presence of melt, so it is one of the most useful and one of the most abused
quantities in the subject.

The honest difficulty of this module appears immediately. Everything that
removes energy from a seismic arrival looks the same in an amplitude
measurement: intrinsic absorption converts organised motion into heat, but
*scattering* moves the same energy out of the coherent arrival and into the
coda without heating anything. An amplitude measurement cannot tell them apart.
This lesson builds the measurement of $Q$ carefully, states exactly what a
measured $Q$ is conditional on, and keeps the scattering question visible as the
subject of [lesson 02](02-scattering-vs-intrinsic.md).

All models and data in this module are **SYNTHETIC**. No real station, event or
waveform is used, and no observational $Q$ is quoted as a measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the quality factor $Q$ through the fractional energy lost per
   cycle, and **derive** the amplitude decay law $A(x) = A_0\exp(-\alpha x)$ with
   $\alpha = \pi f/(Q v)$ from it.
2. **Derive** the two-station spectral-ratio estimator and explain why the source
   spectrum, the site response and the geometric spreading all cancel from its
   slope.
3. **Explain** why a measurement over a finite band returns a band-averaged $Q$,
   and **quantify** the resulting bias for a relaxation-peak $1/Q(f)$.
4. **Compute** the standard error of a $Q$ estimate from the fit geometry, and
   **choose** a band that meets a stated precision target.
5. **Derive** the rise-time relation from the causal amplitude spectrum, and
   show that the pulse width grows linearly with travel time.
6. **State** the assumptions under which each method is valid, and identify
   which of them are violated by scattering, directivity or a wrong band.
7. **Explain** the causality constraint that ties attenuation to dispersion, and
   say why the two must be inverted for together.

## Prerequisites

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic Equation](../01-elastic-wave-propagation/01-wave-equation-elastic.md) —
  where the elastic moduli and the propagating speeds come from.
- [06-01-02 P and S Waves](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  P and S speeds, and why an S-wave $Q$ differs from a P-wave $Q$.
- [06-02-02 Snell's Law and Layered Media](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  ray paths, travel time and the geometric terms that a ratio cancels.

## 1. What $Q$ measures

Take a harmonic wave of angular frequency $\omega = 2\pi f$. Its stored elastic
energy is proportional to the square of its amplitude, $E \propto A^2$. The
quality factor is defined by the energy statement

$$Q \equiv \frac{2\pi E}{\Delta E},$$

where $\Delta E$ is the energy converted to heat in **one** cycle and $E$ is the
stored energy. Equivalently $1/Q = \Delta E/(2\pi E)$: the fractional energy
loss per radian. A material with $Q = 1000$ loses about $0.1\%$ of its energy per
radian; a material with $Q = 10$ loses about $10\%$ per radian and is not elastic
in any useful sense. $Q$ is dimensionless, and its reciprocal $Q^{-1}$ is called
the **internal friction**.

Because energy is amplitude squared, a fractional energy loss per cycle of
$2\pi/Q$ is a fractional **amplitude** loss per cycle of half that,
$\pi/Q$. In one cycle the wave advances one wavelength, $\lambda = v/f$, so the
amplitude decay per unit distance is

$$\frac{1}{A}\frac{\mathrm{d}A}{\mathrm{d}x} = -\frac{\pi}{Q\lambda},$$

which integrates to

$$\boxed{\;A(x) = A_0 \exp\left(-\alpha x\right), \qquad
\alpha(f) = \frac{\pi f}{Q v}, \;}$$

the **absorption coefficient** in $\mathrm{m^{-1}}$. This is the *high-$Q$*
(equivalently *nearly-elastic*) form; the exact anelastic form replaces
$Q^{-1}$ by a frequency-dependent loss that the derivations in §3 pin down.

Three consequences of the energy definition deserve to be stated before any
measurement is attempted:

- $\alpha$ is **linear in frequency**. A fixed $Q$ loses the same *fraction*
  per cycle, and a higher frequency fits more cycles into a metre, so the
  fractional loss per metre grows in proportion to $f$. The distance over which
  the amplitude falls by $1/e$ therefore shrinks as frequency rises, and it is
  *not* the wavelength.
- $Q$ is **not a velocity**. It says nothing about how fast the wave travels.
- $Q$ is **band-limited** in practice. §5 shows that any real measurement
  returns an average of $1/Q$ over the band that carried the signal.

## 2. The observable: $t^{*}$

The spectral-amplitude form of the decay law is the workhorse of observational
attenuation. Combining $\alpha = \pi f/(Q v)$ with $x = v t$ gives a decay
controlled by the single combination

$$t^{*} \equiv \int_{\text{path}} \frac{\mathrm{d}t}{Q(t)} \qquad
\text{(s)},$$

so that $\alpha x = \pi f t^{*}$ and

$$A(f) = A_0(f)\, \exp\left(-\pi f t^{*}\right).$$

For a uniform medium $t^{*} = t/Q$, the travel time divided by the quality
factor. $t^{*}$ carries units of **time**, and this is the quantity that a
spectral amplitude measurement actually constrains: the product of a
dimensionless loss and a travel time. To turn $t^{*}$ into a $Q$ you must supply
the travel time, i.e. a velocity model. That single sentence already contains the
first non-uniqueness of the subject: a large $t^{*}$ can mean a low $Q$ over a
short path or a moderate $Q$ over a long one, and amplitude data alone cannot
separate them.

## 3. Attenuation requires dispersion

A medium cannot attenuate without dispersing. To see why, apply the
Kramers-Kronig relation to the transfer function
$H(\omega) = \exp\left(-A(\omega)\right)\exp\left(-\mathrm{i}B(\omega)\right)$
with amplitude $A(\omega) = \pi f t^{*} = a|\omega|$ and $a = t^{*}/2$. The
relation that reconstructs the phase $B$ from the amplitude $A$ is

$$B(\omega) = -\mathcal{H}[A](\omega)
= -\frac{1}{\pi}\,\mathrm{PV}\!\int \frac{A(\omega')}{\omega' - \omega}\,
\mathrm{d}\omega',$$

with the sign fixed by requiring $H$ analytic in the lower half of the complex
$\omega$ plane (that sign is a convention; the demonstration in
[`code/kk_dispersion_causality_demo.py`](code/kk_dispersion_causality_demo.py)
*calibrates* it against a model that is causal by construction rather than
assuming it).

Carrying out the Hilbert transform of $a|\omega|$ gives the logarithmic
dispersion law

$$B(\omega) = -\frac{t^{*}}{\pi}\,\omega \ln\frac{\omega}{\omega_{\text{ref}}}
\;\Longrightarrow\;
v(f) = v_{\text{ref}}\left[1 + \frac{1}{\pi Q}
\ln\frac{f}{f_{\text{ref}}}\right],$$

i.e.

$$\frac{\Delta t}{t} = \frac{1}{\pi Q}\ln\frac{f_2}{f_1}.$$

The demonstration measures this two ways and reports them with units. For an
SYNTHETIC path of $x = 100\ \mathrm{km}$ at $v = 3500\ \mathrm{m\,s^{-1}}$, the
reference travel time is $\tau_r = x/v = 28.571\ \mathrm{s}$. The fitted
dispersion coefficient recovers $c = -2a/\pi = -t^{*}/\pi$ to within $3.4\%$ at
$Q = 20, 50, 100, 200$; the $3.4\%$ is the finite-band truncation of the model
and does not shrink as the numerical grid is refined. The size of the effect is
what matters for measurement design:

| $Q$ | one decade of frequency | delay $\Delta t$ | as a fraction of $\tau_r$ |
|---|---|---|---|
| 20 | $\ln 10$ | $1.047\ \mathrm{s}$ | $3.66\%$ |
| 50 | $\ln 10$ | $0.419\ \mathrm{s}$ | $1.47\%$ |
| 100 | $\ln 10$ | $0.209\ \mathrm{s}$ | $0.73\%$ |
| 500 | $\ln 10$ | $0.042\ \mathrm{s}$ | $0.15\%$ |

The delay is *the same for every decade* because the law depends only on
$\ln(f_2/f_1)$. For $Q = 100$ one decade costs $0.209\ \mathrm{s}$ on a
$28.6\ \mathrm{s}$ path — far larger than the sub-millisecond timing precision of
modern correlation measurements on repeatable paths. Treating a lossy medium as
non-dispersive therefore biases velocity far more than the formal error bar of a
travel-time measurement.

The converse statement is a theorem that constrains every attenuation model:
a non-dispersive constant-$Q$ model is **exactly acausal**. Its transfer
function $\exp(-a|\omega|)$ has the elementary inverse transform

$$h(t) = \frac{a/\pi}{a^{2} + (t - \tau_r)^{2}},$$

a Lorentzian centred on the arrival time that is strictly positive at every
$t$, including $t<0$. The demonstration measures the pre-arrival energy fraction
against the closed form $E(t<0)/E_{\text{total}} = 1/(12\pi Q^{3})$:

| $Q$ | $E(t<0)/E_{\text{tot}}$ measured | $1/(12\pi Q^{3})$ | $h(0)/h_{\text{peak}}$ | $1/(1+4Q^{2})$ |
|---|---|---|---|---|
| 10 | $2.642\times10^{-5}$ | $2.653\times10^{-5}$ | $2.4939\times10^{-3}$ | $2.4938\times10^{-3}$ |
| 20 | $3.310\times10^{-6}$ | $3.316\times10^{-6}$ | $6.2471\times10^{-4}$ | $6.2461\times10^{-4}$ |
| 100 | $2.650\times10^{-8}$ | $2.653\times10^{-8}$ | $2.5090\times10^{-5}$ | $2.4999\times10^{-5}$ |
| 200 | $3.313\times10^{-9}$ | $3.316\times10^{-9}$ | $6.3733\times10^{-6}$ | $6.2500\times10^{-6}$ |

The leak falls as $Q^{-3}$ and is tiny at high $Q$, but "small" is not "causal": a
causal response is **exactly** zero before the first arrival. Restoring causality
(the Hilbert phase of the table above) removes the leak — the demonstration
measures the same amplitude with the causal phase and finds the pre-arrival
energy at or below the numerical floor of $1\times10^{-13}$ established on a
provably causal control model. The physical statement is stronger still: a
medium with frequency-independent $Q$ over *all* frequencies cannot exist,
because the principal-value integral that generates its phase,
$I_L(\omega_0) = 2\omega_0\ln L - 2\omega_0\ln\omega_0 + \mathcal{O}(L^{-2})$,
diverges logarithmically as the band $L$ widens. At $\omega_0 = 2\pi(1\
\mathrm{Hz}) = 6.283\ \mathrm{rad\,s^{-1}}$, each ten-fold widening of the band
adds $2\omega_0\ln 10 = 28.935\ \mathrm{rad}$ to the required phase. **The band
edges of an attenuation model are physical parameters, not numerical
conveniences.**

## 4. Four ways to measure $Q$, and what each one cancels

### 4.1 Two-station (or two-distance) spectral ratio

Record the same source at two distances $x_1 < x_2$ along the same path. Both
records share the source spectrum $S(f)$, the site response and the instrument,
so the ratio cancels them:

$$\frac{A_1(f)}{A_2(f)}
= \frac{S(f)\,G(x_1)\,C_1}{S(f)\,G(x_2)\,C_2}
\exp\!\left[\alpha(f)\,(x_2 - x_1)\right],$$

and with the geometric term $G(x) \propto 1/x$ for 3-D spreading and equal
coupling $C_1 = C_2$,

$$\ln\frac{A_1}{A_2} = \ln\frac{x_2}{x_1} + \alpha(f)\,(x_2-x_1)
= \underbrace{\ln\frac{x_2}{x_1}}_{\text{intercept}} +
\underbrace{\frac{\pi (x_2-x_1)}{Q v}}_{\text{slope } m} f.$$

The geometric term is a **constant offset in $f$**, not a slope, so it cancels
from the fitted slope exactly — the demonstration measures a $+0.00\%$ bias when
the spreading term $\ln(x_2/x_1) = 1.098612$ is omitted, for the ideal case of
two receivers sharing source and coupling. That is a real and useful robustness,
and it is also its own trap: the same cancellation means the method is blind to
any error that *is* frequency-dependent — 2-D versus 3-D spreading over the
band, receiver coupling that varies with frequency, or a source whose corner
frequency shifts.

The estimator is therefore

$$Q = \frac{\pi (x_2 - x_1)}{v\,m}.$$

### 4.2 Single-station spectral decay ($t^{*}$)

With no reference station, expand the observed spectrum as

$$\ln A(f) = \ln S(f) + \ln G(x) + \ln C - \pi f t^{*},$$

and fit a straight line in $f$. Everything not proportional to $f$ lands in the
intercept — *including the source spectrum and the site response*. The method is
only as good as the assumption that the source spectrum is known or negligible
over the band, which is why it is usually applied as a **relative** measurement
(an event-pair ratio, or a comparison against a reference event of known $t^{*}$).
The demonstration used in [lesson 03](03-attenuation-tomography.md),
[`code/tstar_tomography_demo.py`](code/tstar_tomography_demo.py), is built
around exactly this structure: it measures the precision of $t^{*}$ from a
finite band, and then shows what happens when $t^{*}$ and a per-event amplitude
term are inverted for together — an underdetermined joint problem.

### 4.3 Rise time

The decay law is amplitude-only, but §3 showed that no acceptable model is
amplitude-only. There is nevertheless a clean and useful statement about the
*pulse shape* in the amplitude-only limit, because we know its exact impulse
response: the Lorentzian

$$h(t) = \frac{a/\pi}{a^{2} + (t-\tau_r)^{2}}, \qquad
a = \frac{t^{*}}{2} = \frac{\tau_r}{2Q}.$$

A Lorentzian's **full width at half maximum is twice its parameter**: $\mathrm{FWHM} = 2a$. Hence a delta-function source emerges with

$$\mathrm{FWHM} = 2a = t^{*} = \frac{\tau_r}{Q}
\qquad\Longrightarrow\qquad Q = \frac{\tau_r}{\mathrm{FWHM}} .$$

Two exact facts make this more useful than it looks:

- the Fourier transform of $\exp(-a|\omega|)$ is that Lorentzian, so
  $\mathrm{FWHM} = 2a$ is not an approximation;
- the convolution of two Lorentzians with parameters $a_1$ and $a_2$ is a
  Lorentzian with parameter $a_1 + a_2$. **Widths add**, exactly, so an unknown
  source width $\tau_s$ merely shifts the measured width and does not spoil the
  *slope*:

$$\mathrm{FWHM}(\tau_r) = 2\tau_s + \frac{\tau_r}{Q}
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}\,\mathrm{FWHM}}{\mathrm{d}\tau_r} = \frac{1}{Q}.$$

Differential rise time — width plotted against travel time for a set of paths
from one source — therefore measures $1/Q$ with the source width cancelled
exactly, in this model. The assumption being spent is that the pulse is
approximately Lorentzian (or more generally that widths add), which is the
limiting shape of an attenuation-dominated pulse. For a Gaussian source the
widths add in quadrature instead, $w_{\text{obs}}^2 = w_0^2 + w_\alpha^2$, and
the linear-in-travel-time law becomes a square-root law; the rise-time method is
then a *curvature* measurement, which is far noisier. Real pulses sit between the
two, and the honest practice is to state which limiting shape is being assumed.

### 4.4 What the frequency-domain methods cannot do

All three methods above measure a **coherent** amplitude. Every one of them is
therefore sensitive to the same ambiguity: energy removed from the coherent
arrival by scattering produces exactly the decay that intrinsic absorption
produces. §4 of [lesson 02](02-scattering-vs-intrinsic.md) shows the measurement
in which a *purely elastic* random medium returns an apparent
$Q \approx 129$ with no intrinsic loss anywhere. No single-band amplitude
measurement can distinguish the two; the discriminating measurements are listed
there.

## 5. The uncertainty budget: bandwidth is the whole game

Fit $y_i = b + m f_i$ to $N$ log-amplitude ratios with independent errors of
standard deviation $\sigma_y$. The least-squares slope has variance

$$\sigma_m^{2} = \frac{\sigma_y^{2}}{\sum_i (f_i - \bar{f})^{2}},$$

so the fractional error on $Q$ (which is proportional to $1/m$) is

$$\frac{\sigma_Q}{Q} = \frac{\sigma_m}{m}
= \frac{\sigma_y}{m\sqrt{\sum_i (f_i-\bar f)^2}}.$$

For $N$ frequencies uniformly spaced across a band of width $W$,
$\sum_i (f_i-\bar f)^2 = N(N^2-1)/12 \cdot (W/(N-1))^{2} \approx N W^2/12$, so
$\sigma_Q/Q \propto 1/W$: **a narrow band is a short lever arm in the
$f$-direction, and the slope inherits the full noise.** The demonstration
measures this and compares it with the prediction, using $\sigma_y = \sqrt{2}$
(unit noise on each of the two log-amplitudes, so the ratio has variance 2):

| band (Hz) | $W$ (Hz) | $\sigma_m/m$ | predicted | measured |
|---|---|---|---|---|
| $[3, 6]$ | 3.0 | 0.12800 | $12.80\%$ | $13.64\%$ |
| $[1, 6]$ | 5.0 | 0.07680 | $7.68\%$ | $7.80\%$ |
| $[0.5, 10]$ | 9.5 | 0.04042 | $4.04\%$ | $4.03\%$ |
| $[0.2, 20]$ | 19.8 | 0.01939 | $1.94\%$ | $1.93\%$ |

Prediction and measurement agree to a few per cent, so the penalty is a
variance effect and nothing else. The empirical noise sensitivity of the
estimator over 400 noise realisations (band $[0.5,10]\ \mathrm{Hz}$,
$x_1 = 50\ \mathrm{km}$, $x_2 = 150\ \mathrm{km}$, $Q_{\text{true}} = 100$) is:

| SNR ($1/\sigma_{\ln A}$) | mean $Q$ | std $Q$ | bias |
|---|---|---|---|
| 10 | 99.987 | 0.395 | $-0.013\%$ |
| 50 | 100.005 | 0.076 | $+0.005\%$ |
| 200 | 100.000 | 0.019 | $-0.000\%$ |

The estimator is unbiased — the noise is symmetric and the model is exactly
linear in $t^{*}$ — so every improvement in precision must come from bandwidth or
from averaging independent paths.

Bandwidth buys precision but costs **accuracy**, because real $1/Q(f)$ is not
flat. For a single relaxation (one standard linear solid),

$$\frac{1}{Q(f)} = D\,\frac{f/f_0}{1 + (f/f_0)^{2}},$$

which peaks at $f_0$. A straight-line fit over a band returns the band average
$\langle 1/Q \rangle$, so the reported number depends on the band chosen. With
the SYNTHETIC relaxation $f_0 = 1\ \mathrm{Hz}$, $D = 0.020$ (so $Q(f_0) = 100$):

| band (Hz) | $\langle 1/Q\rangle$ | $Q_{\text{band}}$ | $Q(f)$ at band centre |
|---|---|---|---|
| $[0.3, 3]$ | 0.008203 | 121.91 | 200.28 |
| $[0.5, 10]$ | 0.004624 | 216.26 | 268.33 |
| $[1, 30]$ | 0.002115 | 472.79 | 565.98 |
| $[3, 100]$ | 0.000718 | 1392.37 | 1737.82 |

The same synthetic Earth reports $Q = 122$, $216$, $473$ or $1392$ depending
only on the analysis band. **A quoted $Q$ without its band is not a
measurement.** This is the honest reason laboratory and field $Q$ values scatter
so much more than their formal error bars.

## 6. Worked numeric examples

### Example 1 — the spectral ratio from two receivers

SYNTHETIC model: $v = 3500\ \mathrm{m\,s^{-1}}$, $Q = 100$,
$x_1 = 50\ \mathrm{km}$, $x_2 = 150\ \mathrm{km}$, so
$\Delta x = 1.0\times10^{5}\ \mathrm{m}$.

1. $\alpha(1\ \mathrm{Hz}) = \pi f/(Qv) = 3.141593/(100 \times 3500)
   = 8.975979\times10^{-6}\ \mathrm{m^{-1}}$.
2. The expected slope is
   $m = \pi \Delta x/(Q v) = 3.141593\times10^{5}/(100\times3500)
   = 8.975979\times10^{-1}\ \mathrm{Hz^{-1}}$.
3. With the geometric term included, the model predicts
   $\ln(A_1/A_2) = \ln(x_2/x_1) + m f = 1.098612 + 0.897598 = 1.996210$ at
   $f = 1\ \mathrm{Hz}$. The demonstration's noisy realisation prints
   $+1.949606$, which is $0.0466$ — about $1.6$ standard deviations of the
   difference, since each log amplitude carries $\sigma = 1/50 = 0.02$ and the
   difference therefore has $\sigma = 0.02\sqrt{2} = 0.0283$. Individual
   amplitudes are noisy; the *slope* is what is fitted.
4. Inverting a measured slope $m = 0.8970758\ \mathrm{Hz^{-1}}$:
   $Q = \pi \Delta x/(v m) = 3.141593\times10^{5}/(3500\times0.8970758)
   = 100.058$, a $+0.058\%$ error against $Q_{\text{true}} = 100$.

### Example 2 — rise time

The same path has $\tau_r = 28.571\ \mathrm{s}$. For $Q = 50$ the demonstration
uses the amplitude-only parameter $a = \tau_r/(2Q) = 28.571/100
= 0.285714\ \mathrm{s}$. Then

$$\mathrm{FWHM} = 2a = \frac{\tau_r}{Q} = \frac{28.571}{50}
= 0.571429\ \mathrm{s}, \qquad Q = \frac{28.571}{0.5714} = 50.0 .$$

If a source contributes $\tau_s = 0.1\ \mathrm{s}$ of its own (HWHM), the
observed width is $2\tau_s + \tau_r/Q = 0.2 + 0.5714 = 0.7714\ \mathrm{s}$, and
the *slope* against $\tau_r$ is untouched at $1/Q = 0.02$.

### Example 3 — designing the band for a $2\%$ target

Require $\sigma_Q/Q \le 0.02$ with $\sigma_y = \sqrt{2}$ and $Q = 100$ so
$m = 0.897598\ \mathrm{Hz^{-1}}$. Using $N = 200$ uniformly spaced samples,

$$\sqrt{\textstyle\sum_i (f_i-\bar f)^2} = \frac{\sigma_y}{m\,(\sigma_Q/Q)}
= \frac{1.414214}{0.897598 \times 0.02} = 78.78,$$

so $\sum_i (f_i-\bar f)^2 = 6206$ and, from
$\sum \approx N W^2/12$, $W = \sqrt{12 \times 6206/200} = 19.3\ \mathrm{Hz}$.
Exactly the $[0.2, 20]\ \mathrm{Hz}$ band of the table above, whose measured
error is $1.93\%$. **Under $10\ \mathrm{Hz}$ of usable bandwidth, a $2\%$ $Q$ is
not achievable from one path**, no matter how good the signal-to-noise ratio is.

## 7. Assumptions and regime of validity

1. **$Q$ is large enough** that the nearly-elastic form
   $\alpha = \pi f/(Q v)$ applies. The exact anelastic modulus differs at order
   $Q^{-2}$, i.e. a few per cent at $Q = 10$ and below $0.1\%$ for $Q > 50$.
2. **No scattering.** The measured $1/Q$ is an upper bound on the intrinsic
   $1/Q$ ([lesson 02](02-scattering-vs-intrinsic.md)).
3. **One phase in the window.** The fit assumes the arrival is a single
   ray-theoretical phase; a converted arrival or a later branch inside the
   window adds energy that is misinterpreted as a smaller $t^{*}$.
4. **The source spectrum is flat over the band**, or known. In a two-station
   ratio, this is replaced by the weaker requirement that the source is the same
   at both receivers.
5. **The geometric spreading exponent is known.** It affects the intercept, not
   the slope, for a *frequency-independent* exponent; a frequency-dependent
   spreading (2-D to 3-D transition, or guided propagation) contaminates the
   slope directly.
6. **The receiver responses are equal**, or corrected. This is a frequency-domain
   statement and must be checked per band, not just by a calibration pulse.
7. **The band is stated with the answer**, because the answer is a band average
   (§5). Frequency-independent $Q$ over an unbounded band is impossible (§3), so
   every quoted $Q$ is a finite-band approximation whether the author says so or
   not.
8. **Causality holds**, so attenuation and dispersion are two faces of one
   transfer function. Fitting $Q$ and then using a non-dispersive propagator
   produces travel-time errors of the size computed in §3.

## 8. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| quality factor | $Q$ | dimensionless | $2\pi E/\Delta E$ |
| absorption coefficient | $\alpha$ | $\mathrm{m^{-1}}$ | $\mathrm{s^{-1}}/(\mathrm{m\,s^{-1}})$ |
| frequency | $f$ | $\mathrm{Hz} = \mathrm{s^{-1}}$ | |
| speed | $v$ | $\mathrm{m\,s^{-1}}$ | |
| $t^{*}$ | $t^{*}$ | $\mathrm{s}$ | $\mathrm{d}t/Q$ |
| spectral slope | $m$ | dimensionless per Hz | $\pi \Delta x/(Q v)$: $\mathrm{m}/(\mathrm{m\,s^{-1}}) = \mathrm{s}$ |
| width | FWHM | $\mathrm{s}$ | $t^{*}$ |

The combination $\pi f t^{*}$ in the exponent must be dimensionless; if a
computation produces $t^{*}$ in $\mathrm{m\,s^{-1}}$ or $\alpha$ in
$\mathrm{s^{-1}}$, a velocity has been misplaced. Note the pleasing check that
the rose from the rise-time method — a length in metres divided by a velocity in
$\mathrm{m\,s^{-1}}$ — is a time.

## 9. Python demonstrations

Three demonstrations support this lesson and
[lesson 02](02-scattering-vs-intrinsic.md); all print labelled results with
units and use fixed seeds.

- [`code/spectral_ratio_q_demo.py`](code/spectral_ratio_q_demo.py) — the
  amplitude identity, the two-receiver estimator, its bias and standard
  deviation over 400 noise realisations in four bands and three noise levels, the
  geometric-spreading cancellation, the bandwidth penalty, and the band-average
  bias. Run it and read section 3 first, then section 6: the second is the
  reason a quoted $Q$ must carry its band.
- [`code/kk_dispersion_causality_demo.py`](code/kk_dispersion_causality_demo.py) —
  causality, the Lorentzian impulse response, the $Q^{-3}$ pre-arrival leak, the
  logarithmic dispersion law measured from the amplitude, and the divergence that
  makes unbounded constant $Q$ impossible.
- [`code/absorption_band_demo.py`](code/absorption_band_demo.py) — how many
  relaxations are needed before $1/Q$ is flat enough to call "constant $Q$", and
  what that costs.

Full sets with worked solutions are in
[`exercises/01-attenuation-measurement-exercises.md`](exercises/01-attenuation-measurement-exercises.md)
and
[`exercises/01-attenuation-measurement-solutions.md`](exercises/01-attenuation-measurement-solutions.md).

## Mastery checkpoint

Without notes:

> A two-station spectral ratio is measured over $[1, 20]\ \mathrm{Hz}$ with
> unit-variance log-amplitude noise ($\sigma_y = \sqrt{2}$) on 200 samples, for
> receivers at $x_1 = 20\ \mathrm{km}$ and $x_2 = 120\ \mathrm{km}$ in a medium
> with $v = 3600\ \mathrm{m\,s^{-1}}$. The fitted slope is
> $m = 0.087266\ \mathrm{Hz^{-1}}$. **(a)** Compute $\alpha$ at $5\ \mathrm{Hz}$
> for the implied $Q$, with units. **(b)** Compute $t^{*}$ and the pulse FWHM
> expected from the rise-time method. **(c)** Predict $\sigma_Q/Q$ from the fit
> geometry and state whether a $1\%$ answer is possible in this band.
> **(d)** The true $1/Q(f)$ peaks at $2\ \mathrm{Hz}$ with $D = 0.02$; will the
> reported $Q$ be an over- or under-estimate of $Q(2\ \mathrm{Hz})$, and why?

A worked version appears in the
[solutions](exercises/01-attenuation-measurement-solutions.md).

## Common pitfalls

1. **Quoting $Q$ without a band.** §5 makes the band part of the answer.
2. **Quoting $t^{*}$ as $Q$.** They differ by the travel time, which requires a
   velocity model.
3. **Assuming a non-dispersive medium after measuring $Q$.** Check that the
   travel-time correction of §3 is smaller than your timing error; usually it is
   not.
4. **Reading a small $Q$ as heat.** Scattering produces the same decay.
5. **Trusting a narrow-band estimate.** A $3\ \mathrm{Hz}$ band gives a $12.8\%$
   slope error at unit noise, whatever the picks look like.
6. **Fitting amplitudes in a window containing more than one phase.**
7. **Using the intercept.** The intercept contains the source and the geometric
   spreading; only the slope is robust.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the elastic moduli whose imaginary parts $Q$ describes.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the travel times that convert $t^{*}$ into $Q$.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  the same deconvolution and band-limited-image logic applied to conversions.
- [18-inverse-problems](../../18-inverse-problems/README.md) — weighted least
  squares, covariance and regularisation in general form.

## Self-assessment checklist

- [ ] I can derive $\alpha = \pi f/(Q v)$ from the per-cycle energy definition.
- [ ] I can derive the two-station ratio and say exactly what cancels.
- [ ] I can compute the standard error of a fitted slope and design a band.
- [ ] I can derive $\mathrm{FWHM} = t^{*}$ from $\exp(-a|\omega|)$ and explain
      why widths adding linearly rescues the rise-time method.
- [ ] I can state why attenuation forces dispersion and quote the log law.
- [ ] I can list the assumptions that scattering, directivity and a wrong band
      each violate.
