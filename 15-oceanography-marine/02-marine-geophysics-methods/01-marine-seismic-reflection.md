---
id: 15-02-01
title: "Marine Seismic Reflection: Airguns, Streamers, Processing"
level: graduate
prereqs: ["06-09-01", "06-01-02", "05-05-02"]
tags: [oceanography, marine-geophysics, seismic-reflection, airgun, streamer, nmo, stacking, resolution]
---

# Marine Seismic Reflection: Airguns, Streamers, Processing

> **All models and data in this module are SYNTHETIC.** The earth model used here
> is a chosen teaching model with invented velocities and densities, printed by
> the demonstration in `code/`. No survey, line, well, vessel or published
> section is reproduced, and no acquisition parameter is quoted from a real
> survey.

Marine reflection seismology is the highest-resolution method available for
imaging below the seafloor, and it is the only one that images *interfaces*
rather than *bodies*. Its physics is the reflection coefficient at a contrast in
acoustic impedance. Its engineering is the separation of the useful reflections
from everything else, and its central limit is a resolution that is proportional
to a wavelength and therefore inversely proportional to the bandwidth the source
and the water will pass.

The lesson is built around two numbers that a reader should be able to produce
from memory. The first is the normal-incidence reflection coefficient
$R = (Z_2-Z_1)/(Z_2+Z_1)$: for water over a soft sediment, $R \approx 0.39$, and
that is the dominant event on nearly every marine record. The second is
$\lambda/4$: at $30\ \mathrm{Hz}$ in water, $12.6\ \mathrm{m}$ — the closest two
reflectors can be and still be separated. Both are exact or nearly exact.
Between them sits the processing chain, and the lesson's honest point is that
**the processing is not a refinement**: a velocity error of only $2\,\%$ halves
the stacked amplitude of the event it was meant to preserve.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the normal-incidence reflection coefficient from continuity of
   pressure and particle velocity at an interface, and **compute** it for a
   stated density and velocity contrast.
2. **Explain** the convolutional model, $d = w * r$, and **state** what the
   source wavelet is and what it is not.
3. **Derive** the hyperbolic moveout $t^{2} = t_0^{2} + x^{2}/v_{\text{rms}}^{2}$
   from the geometry of a single reflector, and **apply** NMO.
4. **Quantify** the residual moveout produced by a wrong NMO velocity, and
   **measure** the corresponding loss of stacked amplitude.
5. **Derive** the $\sqrt{N}$ fold law, and **state** precisely which kind of noise
   it removes and which it does not.
6. **Compute** the $\lambda/4$ resolution limit for a stated velocity and
   frequency, and **explain** why detection and resolution are different
   achievements.
7. **Measure** a tuning curve on a wedge model and **state** where resolution is
   lost.

## Prerequisites

- [06-09-01 The Reflection Principle and Reflection Coefficients](../../06-seismology/09-reflection-seismology/01-reflection-principle.md) —
  the land-based version of the same physics.
- [06-01-02 P and S Waves and Their Velocities](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) —
  the elastic moduli behind every velocity in the model.
- [05-05-02 Geometry, Coverage and Fold](../../05-core-geophysics/05-survey-design-and-acquisition/02-geometry-and-coverage.md) —
  offsets, bins and fold, which the CMP method formalises.

## 1. What the method measures

A source near the surface radiates a pulse. It travels down, reflects at
interfaces where the acoustic impedance $Z = \rho v_p$ changes, and returns to a
receiver towed behind the vessel. The recorded time series, called a trace, is
the Earth's reflectivity convolved with the source wavelet and the receiver
response, plus noise.

Three things follow from that description, and they organise the method.

- **Reflection seismology images contrasts, not materials.** A thick, uniform
  layer produces no reflection at all. What is imaged is the *geometry of
  change*.
- **The observable is a two-way time.** Depth requires a velocity, and the
  velocity is estimated from the same data. Depth and velocity are therefore
  entangled, and the entanglement has a size (Section 5).
- **Everything below the first strong reflector is imaged through it.** In the
  marine case the water bottom is the first strong reflector, and it is stronger
  than most of what lies beneath.

## 2. The reflection coefficient

### 2.1 Derivation

Consider a plane wave at normal incidence on an interface between media with
impedances $Z_1 = \rho_1 v_1$ and $Z_2 = \rho_2 v_2$. Continuity of pressure
across the interface and continuity of normal particle velocity give the two
conditions

$$p_i + p_r = p_t, \qquad \frac{p_i - p_r}{Z_1} = \frac{p_t}{Z_2},$$

where $i$, $r$, $t$ label incident, reflected and transmitted. Eliminating $p_t$:

$$\boxed{\;R \equiv \frac{p_r}{p_i} = \frac{Z_2 - Z_1}{Z_2 + Z_1},
\qquad T \equiv \frac{p_t}{p_i} = 1 + R = \frac{2Z_2}{Z_2+Z_1}.\;}$$

Two consequences worth stating. First, $1 + R = T$ is exact and gives a free
arithmetic check. Second, the coefficient is **symmetric under interchange of the
two media only up to sign**: a hard-to-soft interface gives a negative $R$ of the
same magnitude as the reverse. This is why a tuned interpretation must know
whether impedance is increasing or decreasing with depth, and why polarity
conventions are part of a survey's metadata.

### 2.2 Numerical evaluation — the synthetic model

| layer | thickness (m) | $v_p$ (m s$^{-1}$) | $\rho$ (kg m$^{-3}$) | $Z$ (kg m$^{-2}$ s$^{-1}$) | two-way time to top (s) |
|---|---|---|---|---|---|
| 0 water | 1500 | 1500 | 1025 | $1.5375\times10^{6}$ | 0.0000 |
| 1 sediment | 250 | 1800 | 1950 | $3.5100\times10^{6}$ | 2.0000 |
| 2 sediment | 400 | 2200 | 2150 | $4.7300\times10^{6}$ | 2.2778 |
| 3 indurated | 500 | 3000 | 2450 | $7.3500\times10^{6}$ | 2.6414 |
| 4 half-space | – | 4000 | 2600 | $1.0400\times10^{7}$ | 2.9747 |

| interface | $Z_1$ | $Z_2$ | $R$ |
|---|---|---|---|
| water bottom | $1.5375\times10^{6}$ | $3.5100\times10^{6}$ | $+0.3908$ |
| 1 | $3.5100\times10^{6}$ | $4.7300\times10^{6}$ | $+0.1481$ |
| 2 | $4.7300\times10^{6}$ | $7.3500\times10^{6}$ | $+0.2169$ |
| 3 | $7.3500\times10^{6}$ | $1.0400\times10^{7}$ | $+0.1718$ |

The water bottom gives $R = +0.3908$: **39 % of the incident amplitude is
reflected**, because the impedance of water is $56\,\%$ of the impedance of the
sediment beneath it. Nothing below that interface can be imaged without removing
this event, and its multiples sit in the same time window as the deeper
primaries.

## 3. The convolutional model and the source

### 3.1 The model

$$\mathbf{d} = \mathbf{W}\,\mathbf{r} + \mathbf{n},$$

where $\mathbf{r}$ is the reflectivity series (essentially the $R$ of Section 2
placed at the correct two-way times), $\mathbf{W}$ is the convolution matrix of
the source wavelet, and $\mathbf{n}$ is noise. Almost every processing step in
marine seismics is an attempt to make $\mathbf{W}$ narrow (deconvolution), to
suppress $\mathbf{n}$ (stacking, filtering), or to remove arrivals that are not
in $\mathbf{r}$ (multiples, water-layer reverberation).

**The source is not known.** A marine airgun's signature depends on its volume,
its depth, the firing pressure and the bubble's oscillation. The demonstration
therefore uses a *chosen* synthetic source, $w(t) = e^{-25t}\sin(2\pi f_0 t)$ with
$f_0 = 30\ \mathrm{Hz}$ — a damped oscillation, which is the qualitative shape of
an airgun signature, and nothing more than that. Its spectrum peaks at
$29.75\ \mathrm{Hz}$ with a $-3\ \mathrm{dB}$ band of
$25.5$–$33.5\ \mathrm{Hz}$ (width $8.0\ \mathrm{Hz}$).

### 3.2 Two elements of the real acquisition this model omits

They are omitted because they cannot be invented honestly, and they matter:

- **Bubble oscillation.** A real airgun signature contains a decaying tail from
  the oscillation of the injected gas bubble, at a period that depends on volume,
  depth and pressure. Designed arrays (clusters, tuned volumes) suppress it. This
  tail is the single largest difference between an idealised wavelet and a real
  one.
- **Source directivity and the receiver array.** A towed receiver group is
  spatially extended, so it is a filter as well as a sensor, and it attenuates
  high frequencies at large offsets. The result is a wavelet that varies with
  offset — which is exactly the effect the next section shows to be dangerous.

## 4. Moveout, NMO and the CMP stack

### 4.1 Derivation of hyperbolic moveout

Put a source and a receiver at the surface, separated by offset $x$, over a
horizontal reflector at depth $h$ in a medium of constant velocity $v$. The
reflected path is two legs of length $\sqrt{h^{2} + (x/2)^{2}}$, so the travel
time is

$$t = \frac{2\sqrt{h^{2} + (x/2)^{2}}}{v}
= \sqrt{\left(\frac{2h}{v}\right)^{2} + \left(\frac{x}{v}\right)^{2}}
= \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}},$$

using $t_0 = 2h/v$. This is **hyperbolic moveout**. Two properties of it matter:

- the departure from $t_0$ grows as $x^{2}$ for small offsets, which is why
  moveout analysis is a quadratic-fitting problem;
- the equation is exact only for a single constant-velocity layer. With several
  layers it holds with $v$ replaced by an rms (or, better, a Dix-derived
  interval) velocity, and the approximation degrades at large offsets.

The demonstration's primaries, with offsets out to $1800\ \mathrm{m}$:

| primary | $t_0$ (s) | stacking velocity (m s$^{-1}$) | moveout at 1800 m (s) | $R$ |
|---|---|---|---|---|
| 1 | 2.0000 | 1800 | 0.2361 | $+0.3908$ |
| 2 | 2.2778 | 2200 | 0.1425 | $+0.1481$ |
| 3 | 2.6414 | 3000 | 0.0673 | $+0.2169$ |

**The moveout of the first event is $236\ \mathrm{ms}$ against a wavelet
half-width of $17\ \mathrm{ms}$.** A stack that ignored moveout would sum these
traces almost to zero.

### 4.2 NMO and the stack

NMO correction stretches each trace so that its events sit at their zero-offset
times: $d_{\text{nmo}}(t) = d\!\left(\sqrt{t^{2} + x^{2}/v^{2}}\right)$. The
corrected traces are then summed over the offset range. With $N$ traces:

$$\text{stack}(t) = \frac{1}{N}\sum_{i=1}^{N} d_{\text{nmo},i}(t).$$

In the synthetic model with a correct velocity and $2\,\%$ noise on each trace,
the stacked amplitude of the water-bottom event is $0.3286$. Correcting with a
velocity $10\,\%$ too high, the same sample falls to $0.0707$: **$21.5\,\%$ of
the correct value**. Since NMO stretch is applied to the *same* data, nothing
about this is a modelling artefact — the processing itself has destroyed the
event.

## 5. Velocity error: the sensitivity that governs everything

### 5.1 The residual moveout, derived

Write the trial velocity as $v_{\text{try}} = v(1+e)$ and consider an event at
$t_0$. The difference between the moveout computed with the true and trial
velocities, expanded for small $e$ and small $x/(v t_0)$:

$$\Delta t_{\text{res}} \approx \frac{x^{2}}{2t_0}\left(\frac{1}{v_{\text{try}}^{2}}
- \frac{1}{v^{2}}\right)
= \frac{x^{2}}{2t_0v^{2}}\left(\frac{1}{(1+e)^{2}} - 1\right).$$

With $x = 1800\ \mathrm{m}$, $t_0 = 2.0\ \mathrm{s}$, $v = 1800\
\mathrm{m\,s^{-1}}$, the prefactor $x^{2}/(2t_0v^{2}) = 0.250\ \mathrm{s}$, and

| velocity error | $\Delta t_{\text{res}}$ at 1800 m (ms) | measured stacked amplitude / correct |
|---|---|---|
| 0 % | 0.00 | 0.99 |
| 2 % | $-9.71$ | 0.51 |
| 5 % | $-23.24$ | 0.30 |
| 10 % | $-43.39$ | 0.22 |
| 20 % | $-76.39$ | 0.17 |

**A $2\,\%$ velocity error leaves a 9.7 ms residual — more than half the
wavelet's 17 ms half-width — and halves the stacked amplitude.** A $10\,\%$ error
leaves 43 ms and costs $78\,\%$ of the amplitude.

This is the most important practical number in the lesson, and it has three
consequences:

- **Velocity analysis is not a refinement.** Without it there is no stack.
- **The requirement gets harder with offset and easier with time.** The prefactor
  $x^{2}/(2t_0v^{2})$ grows as the square of the cable length and inversely with
  the two-way time, so shallow, far-offset data demand the most accurate
  velocities — and that is precisely where the hyperbolic approximation is
  weakest.
- **A velocity is a *stacking* parameter, not a rock property**, until it is
  converted through Dix's relation to interval velocities, and that conversion
  amplifies errors.

## 6. Fold and the $\sqrt{N}$ law

For coherent signal and uncorrelated noise, the stack adds signal amplitudes
linearly and noise amplitudes as a random walk:

$$S_{\text{stack}} = N A, \qquad \sigma_{\text{stack}} = \sigma\sqrt{N},
\qquad
\mathrm{SNR}_{\text{stack}} = \frac{NA}{\sigma\sqrt{N}}
= \sqrt{N}\,\mathrm{SNR}_{\text{trace}} .$$

The demonstration measures this directly, placing a spike at the exact NMO time,
adding noise of rms 0.30, and averaging over 40 realisations:

| fold $N$ | measured SNR | ratio to fold 1 | $\sqrt{N}$ | ratio/$\sqrt{N}$ |
|---|---|---|---|---|
| 1 | 4.482 | 1.000 | 1.000 | 1.000 |
| 4 | 8.659 | 1.932 | 2.000 | 0.966 |
| 16 | 16.188 | 3.612 | 4.000 | 0.903 |
| 64 | 31.155 | 6.951 | 8.000 | 0.869 |

The ratio tracks $\sqrt{N}$ to within a few per cent, with a small shortfall at
high fold caused by the interpolated peak picking up noise.

**What fold does not do.** Multiples are *coherent*: they stack as well as
primaries, and their moveout often differs from the primary's only in the fourth
decimal place. Increasing fold therefore improves the ratio of signal to random
noise and does nothing at all to a multiple — which is why multiple suppression
is a separate discipline, treated in
[06-09-06](../../06-seismology/09-reflection-seismology/06-multiple-elimination.md).

## 7. Resolution: $\lambda/4$, and why detection is not resolution

The classical vertical-resolution limit is one quarter of the dominant
wavelength:

$$\Delta z_{\text{res}} \approx \frac{\lambda}{4} = \frac{c}{4f}.$$

At $f = 29.75\ \mathrm{Hz}$ in water ($c = 1500\ \mathrm{m\,s^{-1}}$),
$\lambda = 50.4\ \mathrm{m}$ and $\lambda/4 = 12.61\ \mathrm{m}$.

The demonstration measures the consequence on a wedge: two identical wavelets at
decreasing separation in a medium of $v = 1800\ \mathrm{m\,s^{-1}}$.

| separation (ms) | separation (m) | composite peak / single wavelet peak | peaks above 50 % of max |
|---|---|---|---|
| 2.0 | 1.8 | 1.897 | 1 |
| 4.0 | 3.6 | 1.793 | 1 |
| 6.0 | 5.4 | 1.517 | 1 |
| 8.0 | 7.2 | 1.242 | 1 |
| 11.0 | 9.9 | 0.707 | 1 |
| 16.0 | 14.4 | 0.635 | 2 |
| 25.0 | 22.5 | 0.961 | 2 |

This is the **tuning curve**. At very small separation the two wavelets add
coherently and the composite is *brighter* than either alone ($1.90$ at
$1.8\ \mathrm{m}$), then weakens to a minimum ($0.64$) near $16\ \mathrm{ms}$, and
beyond that the two peaks separate. The transition from one peak to two happens
between $11$ and $16\ \mathrm{ms}$, i.e. at
$\lambda/4 = 16.7\ \mathrm{ms}$ in time or $15.0\ \mathrm{m}$ in depth for
$v = 1800\ \mathrm{m\,s^{-1}}$ — the predicted limit, recovered by measurement.

Two conclusions follow, and they are the point of the section.

- **Detection and resolution are different achievements.** A bed much thinner
  than $\lambda/4$ still changes the composite amplitude measurably — that is the
  whole basis of seismic stratigraphy — but it cannot be split into two events.
- **The tuning curve is *not* monotonic in thickness**, so an isolated amplitude
  bright spot has two possible thicknesses, a thin one and a thick one. Amplitude
  alone is ambiguous; that ambiguity is the reason for the "wedge" calibration in
  the first place.

## 8. Assumptions and regime of validity

1. **One-dimensional, layered, isotropic media** for the reflection coefficient.
   Dipping interfaces, lateral velocity change and anisotropy all modify $R$.
2. **Normal incidence.** The exact oblique-incidence answer is the Zoeppritz
   system; $R = (Z_2-Z_1)/(Z_2+Z_1)$ is its $x=0$ limit, and the angle dependence
   it discards is the *signal* in amplitude-versus-offset analysis.
3. **Hyperbolic moveout with an rms velocity.** Exact for one constant-velocity
   layer. With layering it is a small-offset approximation, and its error grows as
   $x^{4}$.
4. **No attenuation in the model.** Real sediments attenuate high frequencies
   preferentially, so the bandwidth narrows with depth and $\lambda/4$ grows with
   depth — resolution is *depth-dependent*.
5. **No multiples in the synthetic data.** Real marine data are dominated by
   water-layer multiples, which the model omits entirely.
6. **A chosen, offset-independent wavelet.** A real wavelet varies with offset
   (Section 3.2), which biases the NMO amplitude behaviour the lesson measures.
7. **Amplitudes are relative.** The demonstration verifies relative amplitudes and
   explicitly notes that NMO stretch and interference reduce them (Section 9,
   Example 3); absolute amplitudes require a true-amplitude processing chain that
   this model does not attempt.

## 9. Worked examples

### Example 1 — a reflection coefficient and its check

An interface between a shale-like layer ($v = 2500\ \mathrm{m\,s^{-1}}$,
$\rho = 2350\ \mathrm{kg\,m^{-3}}$) and a gas sand ($v = 2100\
\mathrm{m\,s^{-1}}$, $\rho = 2050\ \mathrm{kg\,m^{-3}}$):

$$Z_1 = 2500 \times 2350 = 5.875\times10^{6}, \qquad
Z_2 = 2100 \times 2050 = 4.305\times10^{6},$$

$$R = \frac{4.305 - 5.875}{4.305 + 5.875}\times10^{6}\big/\times10^{6}
= \frac{-1.570}{10.180} = -0.1542,$$

$$T = 1 + R = 0.8458 .$$

The negative sign says the reflector is softer than what is above it — the classic
"bright spot" polarity. **A $15\,\%$ impedance contrast is a strong reflection;
most interfaces in a sedimentary section are below $10\,\%$.**

### Example 2 — the resolution limit with depth

Suppose attenuation reduces the dominant frequency from $30\ \mathrm{Hz}$ at the
seabed to $15\ \mathrm{Hz}$ at $3\ \mathrm{km}$ depth in a medium of
$v = 2500\ \mathrm{m\,s^{-1}}$. Then

$$\Delta z_{\text{res}} = \frac{2500}{4 \times 30} = 20.8\ \mathrm{m}
\quad\text{at 30 Hz}, \qquad
\Delta z_{\text{res}} = \frac{2500}{4 \times 15} = 41.7\ \mathrm{m}
\quad\text{at 15 Hz}.$$

Resolution **doubles** with depth for the same lithology. Quoting a single
resolution for a section is therefore almost always wrong; the resolution is a
function of two-way time.

### Example 3 — relative amplitudes through processing

The demonstration computes the peak of each event divided by its $R$:

| event | $R$ | zero-offset peak / $R$ | after NMO + stack / $R$ | change |
|---|---|---|---|---|
| water bottom | $+0.3908$ | 1.0000 | 0.8859 | $-11.4\,\%$ |
| second | $+0.1481$ | 1.0000 | 0.2175 | $-78.3\,\%$ |
| third | $+0.2169$ | 1.0000 | 0.1583 | $-84.2\,\%$ |

The zero-offset ratios are identical to four figures — the check that the
wavelet's normalisation cancels between events. After NMO and stack the ratios
are not merely scaled but *different for each event*, because NMO stretch
lengthens the wavelet at far offsets (a bigger effect on the shallow event, 0.885,
than on the deep one, 0.158) and because the second and third events interfere at
these separations. **Two real processing effects, both usually corrected for, and
both measurable.** Nothing in the demonstration is a coding error, and the numbers
are what they are.

## 10. Python demonstration

`code/marine_seismic_reflection_demo.py` prints everything above with units:

1. impedances, two-way times and reflection coefficients for the model;
2. the source wavelet's spectrum, $\lambda$ and $\lambda/4$;
3. a 20-trace CMP gather with moveouts, and the stacked amplitude with the
   correct and a $10\,\%$-wrong velocity;
4. the residual-moveout formula against the measured stack loss;
5. the measured fold law against $\sqrt{N}$;
6. a wedge model, with the tuning curve and the one-peak-to-two-peak transition;
7. verification: relative amplitudes on a zero-offset trace and after stacking,
   a unit check, and the analytic exactness of the normal-incidence coefficient.

Run it with

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_seismic_reflection_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/01-marine-seismic-reflection-exercises.md`](exercises/01-marine-seismic-reflection-exercises.md)
and
[`exercises/01-marine-seismic-reflection-solutions.md`](exercises/01-marine-seismic-reflection-solutions.md).

- ★ Compute $R$ and $T$ for an interface with
  $v_1 = 1600$, $\rho_1 = 1900$, $v_2 = 2400$, $\rho_2 = 2200$ (SI units
  throughout) and state the polarity.
- ★★ Derive hyperbolic moveout from the two-leg geometry, and compute the moveout
  at $x = 1200\ \mathrm{m}$ for $t_0 = 1.5\ \mathrm{s}$,
  $v = 2000\ \mathrm{m\,s^{-1}}$.
- ★★ Compute the residual moveout for a $3\,\%$ velocity error at
  $x = 3000\ \mathrm{m}$, $t_0 = 1.0\ \mathrm{s}$, $v = 2000\
  \mathrm{m\,s^{-1}}$, and compare it with the $16.7\ \mathrm{ms}$ half-width of a
  $30\ \mathrm{Hz}$ wavelet.
- ★★★ Design a processing test that would demonstrate whether an observed
  amplitude anomaly is a thin bed or a thick one, and state the ambiguity you must
  resolve.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use
$\rho_{\text{water}} = 1025\ \mathrm{kg\,m^{-3}}$,
$c_{\text{water}} = 1500\ \mathrm{m\,s^{-1}}$, $f = 30\ \mathrm{Hz}$.

> A marine survey traverses water $1200\ \mathrm{m}$ deep, over a $300\ \mathrm{m}$
> thick sediment of $v_p = 1700\ \mathrm{m\,s^{-1}}$ and
> $\rho = 1900\ \mathrm{kg\,m^{-3}}$, then a layer of $v_p = 2400\
> \mathrm{m\,s^{-1}}$ and $\rho = 2250\ \mathrm{kg\,m^{-3}}$.
> **(a)** Compute the two-way time to the water bottom and the two-way time to the
> top of the second layer.
> **(b)** Compute $R$ at both interfaces and state the polarity of each.
> **(c)** Compute $\lambda/4$ in the water and in the first sediment layer at
> $30\ \mathrm{Hz}$, and state which controls the resolution of the water-bottom
> event.
> **(d)** A stacking velocity $4\,\%$ too high is used for the water-bottom
> reflection at $t_0$ from (a), with offsets out to $2400\ \mathrm{m}$. Compute
> the residual moveout at the far offset and state, with a number, whether the
> stack will survive.

A worked version of (a)–(d) is in the lesson-01
[solutions](exercises/01-marine-seismic-reflection-solutions.md).

## Common pitfalls

1. **Quoting a depth from a reflection time without the velocity.** The
   observable is a two-way time; depth is a derived quantity.
2. **Treating the stacking velocity as a rock property.** It is a
   moveout-fitting parameter; converting it to an interval velocity needs Dix's
   relation and amplifies its error.
3. **Assuming a small velocity error is harmless.** Section 5: $2\,\%$ halves the
   stack.
4. **Expecting fold to suppress multiples.** Multiples are coherent and stack as
   well as primaries.
5. **Quoting one resolution for a whole section.** Attenuation narrows the
   bandwidth with depth, so $\lambda/4$ grows with depth.
6. **Reading an amplitude anomaly as a thickness.** The tuning curve is
   non-monotonic: two thicknesses give the same amplitude.
7. **Confusing the model wavelet with an airgun signature.** Bubble oscillation,
   directivity and receiver-array filtering are all omitted here and all matter.

## Related modules

- [02 Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) —
  the same sound-speed sensitivity appearing as a depth error in a swath sounder.
- [04 Sub-Bottom Profiling and Chirp Systems](04-sub-bottom-profiling.md) —
  the same reflection physics with a much higher frequency and much less
  penetration.
- [Module 15-02 README](README.md) — how the methods in this module fit together.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  the land and exploration treatment, including migration and AVO.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  where the impedances in a model come from physically.
- [02-03-10 Attenuation and Quality Factor](../../02-physics/03-oscillations-and-waves/10-attenuation.md) —
  the frequency-dependent loss that makes resolution depth-dependent.

## Self-assessment checklist

- [ ] I can derive and evaluate the normal-incidence reflection coefficient.
- [ ] I can write the convolutional model and say what the source is not.
- [ ] I can derive hyperbolic moveout and apply NMO.
- [ ] I can compute a residual moveout and predict the stack loss from it.
- [ ] I can derive the $\sqrt{N}$ fold law and say what it does not fix.
- [ ] I can compute $\lambda/4$ and explain detection versus resolution.
- [ ] I can read a tuning curve and state the thickness ambiguity it implies.
