---
id: 06-07-04
title: "Autocorrelation and Body-Wave Microseismics"
level: doctoral
prereqs: ["06-07-02", "06-01-04"]
tags: [seismology, ambient-noise, autocorrelation, reflectivity, microseism]
---

# Autocorrelation and Body-Wave Microseismics

**All models and data in this module are SYNTHETIC.** The layered model, the
passband and the noise realisations are chosen teaching values, and every number
below is printed by [`code/autocorrelation_demo.py`](code/autocorrelation_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the normal-incidence reflection coefficient $R=(Z_2-Z_1)/(Z_2+Z_1)$
   from continuity of pressure and particle velocity, and **state** the
   transmission coefficient $T = 1+R$.
2. **Compute** two-way travel times and impedances for a layered model with
   units, and **convert** a two-way time to a depth given a velocity.
3. **Derive** why the autocorrelation of the vertical record of a surface
   source gives the zero-offset reflection response, including the
   **unit-amplitude direct arrival** at zero lag.
4. **Explain** why peak amplitudes give only *ratios* of reflection
   coefficients, and **quantify** the contamination by internal multiples in
   the demonstration's own numbers.
5. **Measure** the resolution limit of the method from the source
   autocorrelation, and **compute** the tuning curve of a thin bed.
6. **State** what the single-station method assumes, and which of those
   assumptions a three-component recording can and cannot relax.

## Prerequisites

- [06-07-02 Retrieving the Green's Function by Cross-Correlation](02-cross-correlation-green.md) —
  the correlation identity and the emergence with stacking.
- [06-01-04 Reflected, Refracted and Converted Body Waves](../01-elastic-wave-propagation/04-body-wave-arrivals.md) —
  reflection and transmission at an interface.

---

## 1. The idea, and the fact that makes it work

A single station records vertical ground motion. If the noise field contains
body waves that travel **downward** from the surface, reflect from interfaces
beneath the station, and return, then the record contains a superposition of
the source wavelet at zero lag and its reflections at the two-way times
$t_i = 2\sum h/v$. Correlating the record with itself compares every arrival
with every other arrival, so the reflector times appear as **lag differences**.

The whole method rests on one bookkeeping point: to obtain *absolute* two-way
times, the record must contain an arrival at zero lag that can serve as the
reference. Physically that arrival is the free-surface reflection of the
down-going wavefield: a source at (or very near) the surface produces both a
down-going pulse and its immediate up-going counterpart, which the sensor
records as a single arrival at $t\approx 0$. The demonstration implements
exactly this: its reflectivity series carries a unit amplitude at $t=0$.

## 2. Normal-incidence reflection: derivation

Let a plane wave travel vertically in a medium of impedance $Z_1=\rho_1v_1$ and
meet a medium of impedance $Z_2=\rho_2v_2$. Write the pressure amplitudes as
incident $A_i$, reflected $A_r$ and transmitted $A_t$. Two conditions hold at
the interface, and they are enough to solve the problem.

- **Pressure continuity:** $A_i + A_r = A_t$.
- **Particle-velocity continuity:** with $v = A/Z$ for a travelling wave,
  $\dfrac{A_i - A_r}{Z_1} = \dfrac{A_t}{Z_2}$ (the reflected wave travels the
  opposite way, hence the minus sign).

Substituting the first into the second:

$$\frac{A_i - A_r}{Z_1} = \frac{A_i + A_r}{Z_2}
\;\Longrightarrow\;
A_i\left(\frac{1}{Z_1}-\frac{1}{Z_2}\right)
= A_r\left(\frac{1}{Z_1}+\frac{1}{Z_2}\right),$$

$$\boxed{\;R \equiv \frac{A_r}{A_i} = \frac{Z_2 - Z_1}{Z_2 + Z_1},
\qquad T \equiv \frac{A_t}{A_i} = 1 + R = \frac{2Z_2}{Z_1+Z_2}.\;}$$

Three properties matter for interpretation.

1. $R$ is **dimensionless** and depends only on the ratio of impedances.
2. $R = 0$ requires $Z_2 = Z_1$: a contrast in velocity *or* density, not
   velocity alone.
3. $R>0$ for a harder medium below (a "hard" reflection) and $R<0$ for a
   softer one. At normal incidence the sign is a robust, first-order observable;
   the *magnitude* is not.

The demonstration's teaching model is a four-layer stack. It computes

$$Z = \rho v_p,$$

and prints, with $Z$ in rayl ($\mathrm{kg\,m^{-2}\,s^{-1}}$):

| interface | $Z$ above (rayl) | $Z$ below (rayl) | $R$ | $T = 1+R$ |
|---|---|---|---|---|
| 1 | $1.508\times10^{7}$ | $1.732\times10^{7}$ | $+0.06928$ | 1.06928 |
| 2 | $1.732\times10^{7}$ | $2.094\times10^{7}$ | $+0.09459$ | 1.09459 |
| 3 | $2.094\times10^{7}$ | $2.560\times10^{7}$ | $+0.10001$ | 1.10001 |

**Worked numeric example (interface 1).** With
$\rho_1 = 2.60\ \mathrm{g\,cm^{-3}} = 2600\ \mathrm{kg\,m^{-3}}$,
$v_{p1} = 5.80\ \mathrm{km\,s^{-1}} = 5800\ \mathrm{m\,s^{-1}}$,
$\rho_2 = 2.75\ \mathrm{g\,cm^{-3}}$, $v_{p2} = 6.30\ \mathrm{km\,s^{-1}}$:

$$Z_1 = 2600 \times 5800 = 1.508\times10^{7}\ \mathrm{rayl},$$
$$Z_2 = 2750 \times 6300 = 1.7325\times10^{7}\ \mathrm{rayl},$$
$$R = \frac{1.7325-1.508}{1.7325+1.508} = \frac{0.2245}{3.2405} = +0.06928.$$

The printed values are $1.508\times10^{7}$, $1.732\times10^{7}$ and
$+0.06928$: agreement to the printed precision.

## 3. From impedances to a reflectivity series in time

The same model converted to two-way times:

| interface | depth (km) | two-way time (s) |
|---|---|---|
| surface | 0.0 | 0.0000 |
| 1 | 5.0 | 1.7241 |
| 2 | 9.0 | 2.9940 |
| 3 | 15.0 | 4.6841 |

**Worked numeric example.** The first layer is $5.0\ \mathrm{km}$ thick with
$v_p = 5.80\ \mathrm{km\,s^{-1}}$, so

$$t_1 = \frac{2 \times 5.0}{5.80} = 1.7241\ \mathrm{s},$$

and the second interface adds $\frac{2\times 4.0}{6.30} = 1.2698\ \mathrm{s}$,
giving $t_2 = 2.9939\ \mathrm{s}$; the third adds
$\frac{2\times6.0}{7.10}=1.6901\ \mathrm{s}$, giving $t_3 = 4.6840\ \mathrm{s}$.
The printed values are 1.7241, 2.9940 and 4.6841 s.

The **non-uniqueness is visible in this arithmetic**: the conversion from time
to depth used $v_p$ at every step. A measured set of two-way times determines
depths only through an assumed velocity model, exactly as receiver-function
delays do (module 08). The time section is the measurement; the depth section is
an interpretation.

## 4. Why the autocorrelation gives the reflection response

Write the recorded vertical noise as the convolution of a source wavelet $w(t)$
with the reflectivity series of the medium seen from the surface:

$$x(t) = w(t) * r(t), \qquad
r(t) = \delta(t) + \sum_i R_i\,\delta(t - t_i),$$

where the $\delta(t)$ term is the unit surface arrival discussed in §1. The
autocorrelation of $x$ is

$$c(\tau) = \int x(t)x(t+\tau)\,dt
= \big(R_{ww} * (r \star r)\big)(\tau), \qquad
R_{ww}(\tau) = \int w(t)w(t+\tau)\,dt,$$

and expanding $r\star r$ pair by pair with $R_0 \equiv 1$, $t_0\equiv 0$:

$$(r\star r)(\tau) = \sum_i\sum_j R_iR_j\,\delta\!\big(\tau - (t_j-t_i)\big).$$

Two families of peaks result.

- **Direct-to-reflector pairs** $(0,i)$ and $(i,0)$: peaks at $\tau = \pm t_i$
  with amplitude $R_i R_{ww}(0)$. These are the **absolute** two-way times, and
  they exist *because* of the $\delta(t)$ term.
- **Reflector-to-reflector pairs** $(i,j)$, $i,j\ne0$: peaks at
  $\tau = t_j - t_i$, the **differences** of reflector times. These are the
  internal multiples of the stack, and they are not wanted.

The demonstration measures the peaks with a three-point parabolic refinement
around each maximum, over 64 windows of 60 s at 40 Hz sampling:

| interface | $t$ model (s) | $t$ measured (s) | error (ms) |
|---|---|---|---|
| 1 | 1.7241 | 1.7174 | $-6.73$ |
| 2 | 2.9940 | 3.0008 | $+6.86$ |
| 3 | 4.6841 | 4.6746 | $-9.49$ |

Errors are below $10\ \mathrm{ms}$ on a sampling interval of $25\ \mathrm{ms}$
(40 Hz): the retrieval is sub-sample accurate, because the peak of a band-limited
wavelet is located by interpolation and because 64 independent windows average
the noise down ($\sqrt{64} = 8$).

## 5. Amplitudes: ratios only, and the multiple contamination

Because every peak is scaled by the same $R_{ww}(0)$, the amplitudes give only
**ratios** of reflection coefficients. The demonstration verifies the
proportionality with a calibration experiment — a model with a single reflector:

| quantity | value |
|---|---|
| $R$ of the single reflector | $+0.06928$ |
| measured $A_{\text{peak}}/A(0)$ | $0.077497$ |

The excess of $12\%$ over $R$ is the tail of the zero-lag term reaching the
reflector's lag, not a failure of the proportionality: the relation
$A_{\text{peak}} = R_i R_{ww}(0)$ holds for the *peak of the wavelet*, whereas
$A(0)$ contains the zero-lag value of the whole stacked autocorrelation.

With three reflectors the amplitudes are further contaminated:

| interface | $R$ model | $A_{\text{peak}}$ | $A/A(0)$ | ratio $A_i/A_1$ |
|---|---|---|---|---|
| 1 | $+0.06928$ | 0.01472 | 0.079637 | 1.0000 |
| 2 | $+0.09459$ | 0.01731 | 0.093613 | 1.1755 |
| 3 | $+0.10001$ | 0.01569 | 0.084877 | 1.0658 |

against model ratios $R_2/R_1 = 1.3654$ and $R_3/R_1 = 1.4436$. The measured
ratios are $-13.9\%$ and $-26.2\%$ away from the model, and the explanation is
arithmetic, not mysterious:

$$t_2 - t_1 = 1.270\ \mathrm{s}, \qquad t_3 - t_2 = 1.690\ \mathrm{s},$$

both of which fall *within one wavelet width* of the primary peaks at
$t_1 = 1.7241\ \mathrm{s}$ and $t_2 = 2.9940\ \mathrm{s}$ (the passband is
$1$-$5\ \mathrm{Hz}$, so the wavelet is about $0.2$-$1\ \mathrm{s}$ long). The
difference peaks therefore add to or subtract from the primary peaks. In field
language: the internal multiples have not been removed, and amplitude
interpretation from an autocorrelation requires either a multiple model or a
weak-reflectivity assumption.

## 6. Resolution: the source autocorrelation is the limit

Two measurements define the resolution, and the demonstration makes both:

- The **half-width at half-maximum** of the source autocorrelation,
  $0.100\ \mathrm{s}$ for the $1$-$5\ \mathrm{Hz}$ passband. This is the
  coarsest scale on which two arrivals can be separated.
- The **tuning curve**: put two reflectors of opposite polarity at 2.5 s and
  $2.5+\Delta$ and measure the peak amplitude relative to a single reflector:

| separation $\Delta$ (s) | $A(\Delta)/A_{\text{single}}$ | lag of maximum (s) |
|---|---|---|
| 0.05 | 0.769 | 2.450 |
| 0.15 | 1.533 | 2.500 |
| 0.30 | 1.065 | 2.500 |
| 0.60 | 1.033 | 3.100 |

and, from the analytic response with no noise at all, the extremes of the tuning
curve are

$$\text{minimum ratio } 0.182 \text{ at } \Delta = 0.020\ \mathrm{s},\qquad
\text{maximum ratio } 2.856 \text{ at } \Delta = 0.317\ \mathrm{s}.$$

The construction is the classic **wedge problem**. Below the HWHM the pair is
*not* two reflections: the amplitude is not the sum of the two coefficients
(it can be anything from $0.18$ to $2.86$ times a single reflector), and the
measured lag is not the time of either reflector. The tuning curve is the only
observable there — and it is not invertible for $\Delta$, because a thin bed and
a thick bed with weaker coefficients produce the same amplitude at different
lags.

## 7. Convergence with the available data

The estimate is a stack of incoherent contributions, so its random error should
fall as $1/\sqrt{N}$. Measured against a 256-window reference (4.3 h of
synthetic noise), over the 5-20 s lag window:

| windows $N$ | rms error |
|---|---|
| 1 | $7.456\times10^{-3}$ |
| 2 | $5.721\times10^{-3}$ |
| 4 | $3.275\times10^{-3}$ |
| 8 | $2.750\times10^{-3}$ |
| 16 | $2.068\times10^{-3}$ |
| 32 | $1.481\times10^{-3}$ |
| 64 | $1.135\times10^{-3}$ |

A straight-line fit gives

$$\frac{d\log_{10}(\text{error})}{d\log_{10}N} = -0.454$$

against the $-0.500$ of the $\sqrt{N}$ law, with the same small shortfall seen in
lesson 02's noise floor: the windows are not perfectly independent, because the
source wavelet is shared.

## 8. Assumptions and regime of validity

1. **The noise field must contain down-going body waves from a surface source.**
   Microseisms supply them; a pure surface-wave field does not. *Diagnostic:*
   the retrieval must contain energy whose lag is stable and whose
   depth-converted geometry agrees with independent constraints.
2. **Equipartition, so that the correlation is the Green's function.** This is
   the same assumption as in lesson 02 and the same weakness: a one-sided
   up-going field retrieves nothing.
3. **A reference arrival at zero lag.** Without it the autocorrelation gives
   differences of arrival times, which is a different (and less useful) data
   set. In practice the free-surface reflection supplies it; a sensor in a
   borehole does not have it in the same form.
4. **Zero-offset geometry only.** The autocorrelation of a single station
   measures the reflection response at normal incidence, so it constrains a
   1-D structure beneath the station. There is no lateral information, and
   dipping interfaces appear smeared.
5. **Weak reflectivity for amplitude work.** §5 quantifies the failure: with
   $|R|\sim0.07$-$0.10$ the internal multiples bias the amplitude ratios by
   $14\%$-$26\%$.
6. **No attenuation, or known attenuation.** Attenuation removes high
   frequencies preferentially, which broadens the source autocorrelation and
   therefore worsens the resolution in §6 — a depth-dependent loss of
   resolution that mimics a change in structure.

A final, structural honesty point: the method **cannot** separate structure
above the station from structure below it in the same measurement, because both
are encoded in the same lag. It also cannot, from the vertical component alone,
distinguish a P reflection response from an S response converted at depth. The
three-component version of the experiment (P from the vertical, S from the
horizontal, converted phases in the mixed components) is what partially lifts
these degeneracies — and that is exactly the receiver-function experiment of
[module 08](../08-receiver-functions-and-crustal-structure/README.md), seen from
the other direction.

## Mastery checkpoint

> **(a)** Derive $R = (Z_2-Z_1)/(Z_2+Z_1)$ from pressure and velocity continuity
> and evaluate it for $v_1 = 5.80\ \mathrm{km\,s^{-1}}$,
> $\rho_1 = 2.60\ \mathrm{g\,cm^{-3}}$,
> $v_2 = 6.30\ \mathrm{km\,s^{-1}}$, $\rho_2 = 2.75\ \mathrm{g\,cm^{-3}}$,
> with $Z$ in rayl. **(b)** The same interface is at $5.0\ \mathrm{km}$ depth;
> compute its two-way time. **(c)** State in one sentence why the reflectivity
> series used in the retrieval contains a unit amplitude at $t=0$.
> **(d)** Two reflectors sit at 2.5 s and 2.55 s with equal and opposite
> coefficients. Using the tuning curve numbers, state what the autocorrelation
> will show and why the separation cannot be recovered from it.
> **(e)** The measured amplitude ratio $A_2/A_1 = 1.1755$ against a model
> $1.3654$: give the mechanism and one way to reduce the discrepancy.

## Common pitfalls

1. **Forgetting the zero-lag reference.** Without it, only *differences* of
   two-way times are retrieved.
2. **Reading absolute amplitudes.** Only ratios survive; the scaling is the
   source's autocorrelation, which is unknown.
3. **Ignoring internal multiples.** They land within a wavelet of the primaries
   and bias amplitudes by tens of per cent.
4. **Quoting a depth from the time section.** Depths need velocities; the trade
   is the same as in module 08.
5. **Assuming a horizontal 1-D medium.** The method is inherently zero-offset,
   so dip and lateral variation appear as inconsistent timing between stations,
   not as a measurable offset dependence.

## Related modules

- [06-07-02 Retrieving the Green's Function by Cross-Correlation](02-cross-correlation-green.md).
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  the same layering measured with converted phases.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the
  same reflection coefficients measured with a controlled source and offsets.
- [06-01-04 Reflected, Refracted and Converted Body Waves](../01-elastic-wave-propagation/04-body-wave-arrivals.md).

## Code and exercises

- Demonstration:
  [`code/autocorrelation_demo.py`](code/autocorrelation_demo.py).
- Exercises:
  [`exercises/04-autocorrelation-exercises.md`](exercises/04-autocorrelation-exercises.md)
  with worked [solutions](exercises/04-autocorrelation-solutions.md).
