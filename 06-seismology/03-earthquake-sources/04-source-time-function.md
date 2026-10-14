---
id: 06-03-04
title: "Source Time Functions, Rupture Kinematics and Directivity"
level: doctoral
prereqs: ["06-03-01", "06-03-02"]
tags: [seismology, source-time-function, directivity, rupture-kinematics, duration]
---

# Source Time Functions, Rupture Kinematics and Directivity

> **All models and data in this module are SYNTHETIC.** Every duration, amplitude
> ratio and azimuth below is produced by
> [`code/source_time_function_demo.py`](code/source_time_function_demo.py) from a
> chosen line-source model ($\beta = 3500\ \mathrm{m\,s^{-1}}$,
> $L = 30\ \mathrm{km}$, $v_r = 0.80\beta$, $\tau_r = 1.00\ \mathrm{s}$,
> 400 elements). No real earthquake or waveform is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the emission-time spread $D(\theta) = L(1/v_r - \cos\theta/\beta)$
   of a unilaterally rupturing line source.
2. **Compute** the apparent source duration $D(\theta)+\tau_r$ and **explain**
   why the true source duration $\tau_r + L/v_r$ is azimuth-independent.
3. **State and test** the quadrature rule
   $\sigma_{\text{total}}^{2} = \sigma_{\text{wavelet}}^{2}
   + \sigma_{\text{delay}}^{2}$, and **explain** why it is an upper bound that
   becomes exact only when the received pulses do not overlap.
4. **Quantify** independent measures of duration — span, rms width, moment-rate
   width — and **show** that they are not the same number.
5. **Derive** the forward/backward directivity contrast in duration and amplitude.
6. **Explain** how directivity propagates into a corner frequency and gives an
   apparent stress drop that depends on azimuth, and **estimate** the error factor.
7. **Show** that a bilateral rupture has no first-order directivity, and state
   what that absence does and does not tell you.

## Prerequisites

- [06-03-01 Faulting, Slip and the Elastic Rebound Cycle](01-faulting-and-slip.md) —
  slip, moment and the moment-rate concept.
- [06-03-02 The Double-Couple Source and Radiation Patterns](02-double-couple.md) —
  the point-source radiation pattern that this lesson makes finite.

## 1. Intuition: the source is not an instant

A point source radiates a pulse whose shape is the source time function. A real
fault cannot do that: it has length, it breaks progressively, and the far-field
signal at a station is the **sum of the pulses emitted by every element of the
rupture, each delayed by its own travel time**. Two effects follow, and they are
the whole of this lesson.

- **Duration.** The rupture takes $L/v_r$ to traverse the fault, and the wave
  takes a different time from each element to reach the station. The received
  pulse is therefore longer than the local slip pulse.
- **Directivity.** The delays are not symmetric. If the rupture runs *towards*
  the station, later elements are closer and their pulses bunch up: a short,
  large pulse. If it runs *away*, the pulses spread out: a long, small pulse.
  This is exactly the Doppler-like effect of a moving source, and it is why the
  same earthquake has a different apparent size at different azimuths.

The lesson derives these two effects from one linear expression, then measures
them, then shows the places where the textbook quadrature rule is *not* exact.

## 2. Precise definitions

| Symbol | Meaning | Unit |
|---|---|---|
| $L$ | rupture length along strike | m |
| $v_r$ | rupture propagation speed, $0<v_r<\beta$ | $\mathrm{m\,s^{-1}}$ |
| $\beta$ | shear-wave speed (the speed of the far-field pulse) | $\mathrm{m\,s^{-1}}$ |
| $\tau_r$ | local rise time at one fault element | s |
| $\xi$ | position along the fault, $0\le\xi\le L$ | m |
| $\theta$ | azimuth of the station, measured **from the direction of rupture propagation** | deg |
| $D(\theta)$ | span of emission times arriving at that azimuth | s |
| $\sigma$ | energy-weighted rms width of a signal | s |
| $\dot M(t)$ | moment-rate (source time) function | $\mathrm{N\,m\,s^{-1}}$ |

The **moment-rate function** (or source time function) is the time derivative of
the moment release, $\dot M(t)$; its integral is $M_0$ and its duration is the
source duration. It is *not* what a single station records: a station records
$\dot M(t)$ convolved with the propagation delays and with the medium response.
Confusing the two is the most common error in this subject, and Section 3.4
measures the difference.

## 3. Derivations

### 3.1 Emission times and the directivity term

Let the station be at distance $r$ in the direction making angle $\theta$ with the
rupture direction. The element at $\xi$ emits at time $\xi/v_r$ (the rupture front
arrives there then), and its pulse reaches the station after an additional travel
time $(r-\xi\cos\theta)/\beta$ in the far field ($r\gg L$). The arrival time is

$$t(\xi) = \frac{\xi}{v_r} + \frac{r-\xi\cos\theta}{\beta}
= \underbrace{\frac{r}{\beta}}_{\text{common}}
+ \xi\left(\frac{1}{v_r} - \frac{\cos\theta}{\beta}\right).$$

The common term shifts the whole signal and is not observable; the **spread** of
arrival times is governed by the coefficient of $\xi$:

$$\boxed{\;\Delta t(\xi) = \xi\left(\frac{1}{v_r}-\frac{\cos\theta}{\beta}\right),
\qquad D(\theta) = L\left(\frac{1}{v_r}-\frac{\cos\theta}{\beta}\right).\;}$$

The extreme cases are the informative ones:

$$D(0^\circ) = L\left(\frac{1}{v_r}-\frac{1}{\beta}\right),\qquad
D(90^\circ) = \frac{L}{v_r},\qquad
D(180^\circ) = L\left(\frac{1}{v_r}+\frac{1}{\beta}\right).$$

*Numerical check (SYNTHETIC).* $L/v_r = 30\,000/2800 = 10.714\ \mathrm{s}$ and
$L/\beta = 30\,000/3500 = 8.571\ \mathrm{s}$, so

$$D(0^\circ) = 10.714-8.571 = 2.143\ \mathrm{s},$$
$$D(90^\circ) = 10.714\ \mathrm{s},\qquad
D(180^\circ) = 10.714+8.571 = 19.286\ \mathrm{s}.$$

The demo prints the pieces: "true duration $\tau_r + L/v_r = 11.714\ \mathrm{s}$"
and "directivity term $L/\beta = 8.571\ \mathrm{s}$". Adding the rise time to the
spans gives the **apparent durations** $3.143$, $11.714$ and
$20.286\ \mathrm{s}$.

### 3.2 The quadrature rule, and why it is only an upper bound

The received signal is the superposition of one wavelet per element:

$$u(t) = \sum_{i} w(t-d_i),$$

where $d_i$ are the emission-time delays of Section 3.1. If the pulses do **not**
overlap, the energy density of the sum is the sum of the energy densities,

$$|u(t)|^{2} = \sum_i |w(t-d_i)|^{2},$$

and the second moment of that energy density is the sum of the second moments of
the wavelet energy and of the delay distribution:

$$\boxed{\;\sigma_{\text{total}}^{2} = \sigma_{\text{wavelet}}^{2}
+ \sigma_{\text{delay}}^{2}.\;}$$

This is the **incoherent** or quadrature rule. When the pulses *do* overlap, the
cross terms $2w(t-d_i)w(t-d_j)$ are present; on average they are negative for
pulses that add with different signs, so the measured width comes out **shorter**
than the rule predicts. The rule is a bound, and the deficit measures the
overlap.

*Numerical check.* The demo computes $\sigma_{\text{delay}} = \mathrm{std}(d_i)$,
$\sigma_{\text{wavelet}}$ from the wavelet alone, predicts
$\sigma = \sqrt{\sigma_{\text{delay}}^{2}+\sigma_{\text{wavelet}}^{2}}$ and
measures the width of the composite signal:

| azimuth $\theta$ | $\sigma_{\text{delay}}$ (s) | $\sigma$ predicted (s) | $\sigma$ measured (s) | difference (s) | peak (normalised) |
|---|---|---|---|---|---|
| $0^\circ$ | 0.6201 | 1.0652 | 0.9747 | $-9.04\times10^{-2}$ | 1.0000 |
| $45^\circ$ | 1.3467 | 1.6011 | 1.4017 | $-1.99\times10^{-1}$ | 0.6561 |
| $90^\circ$ | 3.1007 | 3.2194 | 2.9039 | $-3.15\times10^{-1}$ | 0.3007 |
| $135^\circ$ | 4.8547 | 4.9313 | 4.5735 | $-3.58\times10^{-1}$ | 0.1921 |
| $180^\circ$ | 5.5812 | 5.6480 | 5.2802 | $-3.68\times10^{-1}$ | 0.1671 |

with $\sigma_{\text{wavelet}} = 0.8660\ \mathrm{s}$. The worst absolute
discrepancy is $3.68\times10^{-1}\ \mathrm{s}$, i.e. $11.42\%$ of the predicted
value at $180^\circ$, and every difference is **negative** — the measured signal
is always shorter than the incoherent rule.

The confirmation is the second table: hold the delay distribution fixed at
$180^\circ$ and shrink the wavelet.

| $\tau_r$ (s) | 1.000 | 0.500 | 0.250 | 0.100 | 0.050 | 0.025 |
|---|---|---|---|---|---|---|
| deficit at $180^\circ$ (%) | 6.512 | 3.582 | 1.866 | 0.760 | 0.375 | 0.170 |

The deficit falls monotonically as the pulses separate. **The quadrature rule is
an incoherent energy statement, and it becomes exact in the limit of
non-overlapping pulses.**

A closed form for the delay spread makes the table computable by hand. For $n$
evenly spaced delays spanning $D$, the population standard deviation is
$D/\sqrt{12}$ in the continuum limit, so

$$\sigma_{\text{delay}} \approx \frac{L}{\sqrt{12}}
\left|\frac{1}{v_r} - \frac{\cos\theta}{\beta}\right|.$$

At $\theta=0$: $(30\,000/3.4641)\times(7.1429\times10^{-5}) = 0.6186\ \mathrm{s}$,
against the demo's discrete value $0.6201\ \mathrm{s}$.

### 3.3 The wavelet's own width

The demo's wavelet is $w(t) = (t/\tau_r)e^{-t/\tau_r}$ for $t>0$. Its
energy-weighted width is found from $\int w^{2}\,\mathrm{d}t$:

$$\int_0^\infty \frac{t^{2}}{\tau_r^{2}}e^{-2t/\tau_r}\,\mathrm{d}t
= \frac{\tau_r}{4},$$
$$\langle t\rangle = \frac{\int t\,w^{2}\,\mathrm{d}t}{\int w^{2}\,\mathrm{d}t}
= \frac{3\tau_r}{2}, \qquad
\langle t^{2}\rangle = 3\tau_r^{2},$$
$$\sigma_{\text{wavelet}}^{2} = 3\tau_r^{2} - \left(\tfrac{3\tau_r}{2}\right)^{2}
= \tfrac34\tau_r^{2} \;\Rightarrow\;
\sigma_{\text{wavelet}} = \frac{\sqrt3}{2}\tau_r = 0.8660\,\tau_r,$$

which is the demo's $0.8660\ \mathrm{s}$ for $\tau_r=1.00\ \mathrm{s}$. Note that
the width of a pulse is not its duration: this one has rms width
$0.8660\,\tau_r$ but a long exponential tail.

### 3.4 The moment-rate function is azimuth-independent

Set the receiver term aside and superpose the elements using only their rupture
times $\xi/v_r$:

$$\dot M(t) = \sum_i w\left(t-\frac{\xi_i}{v_r}\right).$$

Its width is **the same at every azimuth**, because no station enters the
definition. The demo measures $\sigma_{\dot M} = 2.9039\ \mathrm{s}$ and reports it
against the apparent widths at $0^\circ$ ($0.9747\ \mathrm{s}$), $90^\circ$
($2.9039\ \mathrm{s}$) and $180^\circ$ ($5.2802\ \mathrm{s}$). A rectangular span
of length $11.714\ \mathrm{s}$ has rms width $11.714/\sqrt{12} = 3.3816\
\mathrm{s}$; the measured $2.9039\ \mathrm{s}$ is smaller because the wavelet has
its own shape and the span is not perfectly rectangular.

**Consequence.** "The source duration" is ambiguous. There is the true
moment-rate duration, which is a property of the source, and the apparent
duration, which is a property of the source *and* the station's azimuth. Any
quoted duration must say which.

### 3.5 Forward and backward: the directivity contrast

From Section 3.1 the spans at the two ends differ by $2L/\beta$, so the
**closed-form span ratio** is

$$\frac{\tau_r + D(180^\circ)}{\tau_r + D(0^\circ)}
= \frac{\tau_r + L/v_r + L/\beta}{\tau_r + L/v_r - L/\beta}
= \frac{11.714+8.571}{11.714-8.571} = \frac{20.286}{3.143} = 6.4545.$$

The demo prints exactly this number. Without the rise time the ratio would be
$19.286/2.143 = 9.0$: **the rise time dilutes directivity**, because a longer
local pulse is a larger constant added to both ends.

The measured **rms** ratio is different: $5.2802/0.9747 = 5.4171$. The rms width
is a second moment, the closed form is a support (span); they are different
duration measures of the same signal. The demo prints both and says so.

Because the *area* of the pulse is fixed by $M_0$, a pulse that is $5.4171$ times
shorter is roughly $5.4171$ times taller. The measured peak ratio is
$0.1671$ between the ends, i.e. a forward/backward contrast of $1/0.1671 = 5.98$
in amplitude, against the inverse-duration ratio $5.4171$; the two agree to about
$9\%$, the residual being the change in pulse *shape* with azimuth.

### 3.6 Bilateral rupture

If the rupture propagates in both directions from the hypocentre, the two halves
contribute delays of opposite sign. In the demo the bilateral delays are
$|\xi|/v_r - \xi\cos\theta/\beta$ with $\xi\in[-L/2,L/2]$. At
$\theta=0^\circ$ the half that approaches and the half that recedes contribute
equal and opposite $-\xi\cos\theta/\beta$ terms, so the first-order directivity
cancels:

| azimuth | bilateral $\sigma$ (s) | unilateral $\sigma$ (s) |
|---|---|---|
| $0^\circ$ | 2.3310 | 0.9747 |
| $90^\circ$ | 1.5548 | 2.9039 |
| $180^\circ$ | 2.3310 | 5.2802 |

Forward and backward are equal ($2.3310$ both) and the widest direction is now
*perpendicular* to the fault. **Absence of directivity is information**: it tells
you the rupture was not strongly unilateral.

### 3.7 Propagation into a corner frequency and a stress drop

If the far-field spectrum scales inversely with duration, then
$f_c\propto1/\sigma$ and the same event has a different corner frequency at every
azimuth. The demo tabulates $f_c/f_c(90^\circ)$:

| azimuth | $0^\circ$ | $45^\circ$ | $90^\circ$ | $135^\circ$ | $180^\circ$ |
|---|---|---|---|---|---|
| $f_c/f_c(90^\circ)$ | 2.9792 | 2.0718 | 1.0000 | 0.6349 | 0.5500 |

i.e. a factor $5.42$ between the two ends. From
[05 Source Spectra](05-source-spectra.md) the stress drop scales as
$M_0f_c^{3}$, so an analyst who ignores directivity inherits that factor
**cubed**: $5.42^{3} \approx 159$. This is why azimuthal coverage, and averaging
over it, is not optional when durations or stress drops are quoted.

## 4. Physical interpretation

**Directivity is a Doppler effect on the *emission* times, not on the wave
speed.** The disturbance still travels at $\beta$; what changes with azimuth is
how the pulses *from different parts of the fault* line up in time. When they
line up, the signal is short and large; when they spread, it is long and small.

**Duration and size are separated.** $M_0$ fixes the area under $\dot M(t)$;
the duration fixes its width. Two events of the same moment release it over
different times, which is exactly the difference between a fast and a slow
source.

**$v_r$ is bounded by $\beta$.** A rupture cannot outrun its own S wave in this
model; $v_r\lesssim0.9\beta$ is typical. As $v_r\to\beta$ (in the limited case
where the relevant speed equals the pulse speed) the directivity term
$L(1/v_r-1/\beta)$ vanishes at $\theta=0$ and the forward pulse becomes a
singular spike — the mathematical origin of "directivity pulses" in strong-motion
records.

**The rise time is a low-pass filter.** Increasing $\tau_r$ lengthens both ends
and reduces the contrast; a long rise time makes the source look like a point
source in duration, even when $L$ is large.

## 5. Assumptions and regime of validity

1. **Line source of finite length, on a single plane.** No width, no branching,
   no segmentation; a two-dimensional rupture has a smaller effective dimension
   and less directivity.
2. **Constant rupture velocity.** Real ruptures accelerate, decelerate and
   occasionally jump. $v_r$ here is an average, and the average is what the
   quadratic emission-time relation propagates.
3. **Identical wavelet at every element.** $\tau_r$ is constant along the fault;
   in reality the local slip history varies, adding a random component to the
   duration.
4. **Far field, $r\gg L$.** Only then is the travel time linear in $\xi$, which is
   what makes the delay distribution rectangular. Near the fault the
   finite-distance and near-field terms matter and the span formula fails.
5. **No attenuation and no scattering.** The medium response is a further
   convolution that broadens the pulse; see
   [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md).
6. **Instantaneous healing.** The elements emit once; no re-rupture or delayed
   slip.
7. **Non-overlapping-pulse limit for the quadrature rule.** Where it is violated
   the rule over-predicts the duration, as measured in Section 3.2.

**Consequence.** Directivity computed from a duration ratio is a *model inference*
about $v_r$ and $L$ jointly. One station gives one number; the azimuthal
variation is what constrains the rupture direction — and with a single station it
cannot be measured at all.

## 6. Units and dimensional analysis

| Quantity | Expression | Unit | Check |
|---|---|---|---|
| delay | $\xi(1/v_r-\cos\theta/\beta)$ | $\mathrm{m}/\mathrm{m\,s^{-1}} = \mathrm{s}$ | ✔ |
| span | $L(1/v_r-\cos\theta/\beta)$ | s | ✔ |
| $\sigma_{\text{wavelet}}$ | $(\sqrt3/2)\tau_r$ | s | dimensionally proportional to a time ✔ |
| $\sigma_{\text{delay}}$ | $L/\sqrt{12}\times\lvert\cdot\rvert$ | s | ✔ |
| $\sigma_{\text{total}}$ | $\sqrt{\sigma_w^2+\sigma_d^2}$ | s | square root of a sum of squared seconds ✔ |
| $f_c$ ratio | $\sigma_2/\sigma_1$ | — | ratio of times ✔ |

The only combinations that can make a time are a length over a speed and a
duration; any expression mixing $\mathrm{m\,s^{-1}}$ into a sum with seconds is
wrong.

## 7. Worked examples

### Example 1 — the three spans and their ratio

From $\tau_r = 1.00\ \mathrm{s}$, $L/v_r = 10.714\ \mathrm{s}$,
$L/\beta = 8.571\ \mathrm{s}$:

$$D(0^\circ) = 2.143\ \mathrm{s},\quad D(90^\circ) = 10.714\ \mathrm{s},\quad
D(180^\circ) = 19.286\ \mathrm{s}.$$

Apparent durations $D+\tau_r$: $3.143$, $11.714$, $20.286\ \mathrm{s}$. Span ratio
$20.286/3.143 = 6.4545$. Without the rise time it would be $9.0$, so a
$1\ \mathrm{s}$ rise time reduces the directivity contrast by $28\%$.

### Example 2 — delay width by hand

$$\sigma_{\text{delay}}(\theta) = \frac{L}{\sqrt{12}}
\left|\frac{1}{v_r} - \frac{\cos\theta}{\beta}\right|.$$

- $\theta=0$: $|1/2800 - 1/3500| = 7.1429\times10^{-5}$,
  $\sigma = 8660.25\times7.1429\times10^{-5} = 0.6186\ \mathrm{s}$.
- $\theta=90$: $|1/2800| = 3.5714\times10^{-4}$,
  $\sigma = 3.0929\ \mathrm{s}$.
- $\theta=180$: $|3.5714\times10^{-4}+2.8571\times10^{-4}| = 6.4286\times10^{-4}$,
  $\sigma = 5.5672\ \mathrm{s}$.

The demo's discrete values are $0.6201$, $3.1007$ and $5.5812\ \mathrm{s}$: the
continuum formula is $0.2$–$0.3\%$ low, as expected for the $1/\sqrt{12}$
approximation to a finite sample.

### Example 3 — predict the incoherent width at $90^\circ$

$$\sigma_{\text{total}} = \sqrt{\sigma_{\text{delay}}^{2}
+ \sigma_{\text{wavelet}}^{2}} = \sqrt{3.1007^{2} + 0.8660^{2}}
= \sqrt{9.6143+0.7500} = \sqrt{10.3643} = 3.2194\ \mathrm{s},$$

which is the demo's predicted value; the measured value is $2.9039\ \mathrm{s}$,
$9.8\%$ shorter, because the pulses overlap.

### Example 4 — azimuth dependence of an inferred stress drop

A worker measures $f_c$ at $0^\circ$ and, assuming a point source, computes a
stress drop from $\Delta\sigma\propto M_0f_c^{3}$. Using the demo's duration
ratios, the $f_c$ at $0^\circ$ is $2.9792$ times the $90^\circ$ value, so the
inferred stress drop is $2.9792^{3} = 26.44$ times too large. A worker at
$180^\circ$ obtains $(0.5500)^{-3} = 6.01$ times too large. **The same event
yields stress drops differing by a factor $26.44/6.01 = 4.4$ between two
azimuths**, purely from unmodelled directivity.

## 8. Python demonstration

[`code/source_time_function_demo.py`](code/source_time_function_demo.py):

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python source_time_function_demo.py
```

Five numbered parts:

1. **The convolution identity.** The table of Section 3.2 (delays, prediction,
   measurement, difference, peak) and the monotone deficit-versus-$\tau_r$ table.
2. **Directivity.** Forward/backward rms ratio $5.4171$, peak ratio $0.1671$,
   inverse-duration ratio $5.4171$, and the closed-form span ratio $6.4545$.
3. **Azimuth independence of the moment-rate duration.**
   $\sigma_{\dot M} = 2.9039\ \mathrm{s}$ at every azimuth against apparent widths
   $0.9747$–$5.2802\ \mathrm{s}$, and the rectangular-span check
   $11.714/\sqrt{12} = 3.3816\ \mathrm{s}$.
4. **Bilateral rupture.** The table of Section 3.6.
5. **Corner frequency and stress drop.** The $f_c/f_c(90^\circ)$ table and the
   factor-$5.42$ range.

## 9. Exercises

- [`exercises/04-source-time-function-exercises.md`](exercises/04-source-time-function-exercises.md)
- [`exercises/04-source-time-function-solutions.md`](exercises/04-source-time-function-solutions.md)

## 10. Real-world applications

- **Source-duration and moment-rate estimates.** Far-field body waves and
  surface waves are routinely deconvolved to recover $\dot M(t)$; its duration is
  a primary observable.
- **Strong-motion forward modelling.** Directivity pulses control the largest
  ground motions, and scenario rupture models must specify $v_r$ and the rupture
  direction.
- **Rapid source inversion for hazard.** The rupture direction inferred from
  directivity is used in near-real-time shaking maps.
- **Discriminating fast and slow sources.** Duration separates ordinary
  earthquakes from slow slip and from some volcanic events at similar moment.
- **Radiated energy.** The duration of $\dot M(t)$ sets the radiated-energy
  estimate, feeding the scaling laws of lesson
  [06](06-rupture-dynamics.md).

## 11. Further reading

- **Haskell, N. A. (1964). Total energy and energy spectral density of elastic
  wave radiation from propagating faults.** *Bulletin of the Seismological
  Society of America*. Level: research. The original kinematic line-source model.
- **Aki, K., & Richards, P. G. (1980). *Quantitative Seismology*.** Level:
  graduate textbook. Chapter 4 for the convolution of source kinematics with
  propagation.
- **Kanamori, H., & Anderson, D. L. (1975). Theoretical basis of some empirical
  relations in seismology.** *Bulletin of the Seismological Society of America*.
  Level: research. Duration, moment and the scaling that ties them together.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC strike-slip rupture has $L = 20\ \mathrm{km}$,
> $v_r = 2.5\ \mathrm{km\,s^{-1}}$, $\beta = 3.5\ \mathrm{km\,s^{-1}}$ and
> $\tau_r = 0.50\ \mathrm{s}$. **(a)** Compute $L/v_r$, $L/\beta$ and
> $D(0^\circ)$, $D(90^\circ)$, $D(180^\circ)$. **(b)** Compute the apparent
> durations at the three azimuths and their span ratio, with and without
> $\tau_r$. **(c)** Compute $\sigma_{\text{wavelet}}$ and
> $\sigma_{\text{delay}}(180^\circ)$ and predict the incoherent
> $\sigma_{\text{total}}$. **(d)** State whether the measured value will be larger
> or smaller than your prediction and why, and name the observation that confirms
> the diagnosis. **(e)** If a corner frequency is measured at $180^\circ$ and a
> point-source stress drop is assumed, compute the error factor relative to the
> $90^\circ$ value. **(f)** State two model assumptions that a single-station
> duration measurement cannot test.

## Common pitfalls

1. **Quoting "the duration" without saying which duration.** Moment-rate
   duration, apparent duration and span are three different numbers.
2. **Assuming the quadrature rule is exact.** It is an upper bound that requires
   non-overlapping pulses.
3. **Reading directivity as a change in wave speed.** The pulse speed is $\beta$
   regardless of azimuth; the *emission-time* distribution changes.
4. **Ignoring the rise time.** It dilutes the directivity contrast and sets a
   floor on the duration.
5. **Computing a stress drop from a single azimuth's $f_c$.** The stress drop
   inherits the duration error *cubed*.
6. **Inferring rupture direction from one station.** Directivity is an azimuthal
   *variation*; one azimuth cannot separate duration, rise time and directivity.
7. **Comparing an rms width with a span.** They are different functionals of the
   same signal, as the demo's $5.4171$ versus $6.4545$ shows.

## Related modules

- [02 The Double-Couple Source and Radiation Patterns](02-double-couple.md) —
  the point-source limit this lesson departs from.
- [03 Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) —
  what a finite source does to the tensor decomposition.
- [05 Source Spectra, Corner Frequency and Stress Drop](05-source-spectra.md) —
  where the durations of this lesson become spectra and stress drops.
- [07 Discriminating Explosions from Earthquakes](07-nuclear-explosion-sources.md) —
  where source *duration* matters for discrimination.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the medium broadening that superposes on source duration.
