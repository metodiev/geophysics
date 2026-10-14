---
id: 08-01-04
title: "Secular Variation, Jerks and Core Dynamics"
level: doctoral
prereqs: ["08-01-03", "08-01-02", "20-05-01"]
tags: [geomagnetism, secular-variation, jerk, core-flow, frozen-flux, westward-drift]
---

# Secular Variation, Jerks and Core Dynamics

Everything in the previous three lessons described a snapshot. A reference model
that is used in 2030 to remove the main field from a 2015 survey is not a
snapshot: it is a snapshot plus an extrapolation, and the extrapolation is where
the error lives. **Secular variation** (SV) is the rate of change of the field;
it is small — of order $10^{-4}$ of the field per year — and it is the only
observable window onto the fluid motion of the outer core. This lesson develops
its kinematics, measures how much noise each time derivative costs, and is
explicit about which statements about it are data and which are inference.

**All models and data in this module are SYNTHETIC.** The time series,
coefficient rates, drift rate and noise below come from a chosen teaching model
and a seeded generator. No observatory record and no published SV value is used.
Standard values are $a = 6371\ \mathrm{km}$ and $\mu_0 = 4\pi\times10^{-7}\
\mathrm{H\,m^{-1}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** secular variation, acceleration and jerk as the first three time
   derivatives of a field element, with units.
2. **Compute** the characteristic timescale $\tau = |B|/|\partial B/\partial t|$
   and say what it does and does not constrain about the core.
3. **Derive** the frozen-flux induction equation and state the null space of its
   inversion for the core flow.
4. **Measure** westward drift from the phase of a harmonic pattern, and state the
   aliasing limit of the measurement.
5. **Quantify** the noise amplification of the first, second and third
   derivatives from a Monte Carlo experiment.
6. **Estimate** the size of a jerk that can be detected at a given noise level.
7. **Quantify** the error of extrapolating a linear SV model, and explain why it
   grows linearly rather than quadratically.

## Prerequisites

- [08-01-03 Spherical Harmonic Analysis of the Magnetic Field](03-spherical-harmonic-magnetic.md) —
  the coefficients whose time derivatives are the subject here.
- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](02-dipole-and-igrf.md) —
  epochs and the secular-variation term of a model.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md)
  — the noise model used in section 5.

## 1. Definitions, units, and the arithmetic of small numbers

For any field element $E(t)$ — a Gauss coefficient, a component, an element of
the seven of [08-01-01](01-main-field-description.md) — define

$$\text{SV} \equiv \dot{E} = \frac{\mathrm{d}E}{\mathrm{d}t}\
[\mathrm{nT\,yr^{-1}}], \qquad
\text{acceleration} \equiv \ddot{E}\ [\mathrm{nT\,yr^{-2}}], \qquad
\text{jerk} \equiv E^{(3)}\ [\mathrm{nT\,yr^{-3}}].$$

The demonstration's SYNTHETIC $g_1^0(t)$ has a secular variation of
$-12\ \mathrm{nT\,yr^{-1}}$ before 1990 and $-34\ \mathrm{nT\,yr^{-1}}$
afterwards, reached through a $\tanh$ transition of width $1.5\ \mathrm{yr}$:

| year | $g_1^0$ (nT) | SV (nT/yr) | acceleration (nT/yr²) | jerk (nT/yr³) |
|---|---|---|---|---|
| 1960 | −30120.00 | −12.000 | 0.000 | 0.000 |
| 1980 | −30360.00 | −12.000 | −0.000 | −0.000 |
| 1985 | −30420.02 | −12.037 | −0.065 | −0.111 |
| 1990 | −30491.44 | −23.000 | −5.836 | 0.000 |
| 1995 | −30650.02 | −33.963 | −0.065 | +0.111 |
| 2005 | −30990.00 | −34.000 | −0.000 | 0.000 |
| 2018 | −31432.00 | −34.000 | 0.000 | — |

The pattern is the whole of the subject in miniature: the SV changes by a factor
of three, the acceleration is a narrow pulse, and the jerk is a pulse of peak
amplitude $1.895\ \mathrm{nT\,yr^{-3}}$ whose sign is positive on one side of the
transition and negative on the other. **A jerk is a third-derivative phenomenon:
it is invisible in the level of the field and appears only as a change of slope
in SV.** The 1990 row shows why the third derivative column is the informative
one and also the hardest: the finite-difference estimators of §5 are the reason
the jerk column has an intermittent 0.000 at 1990 and $\pm0.111$ at
1985/1995 — the estimator is centred, so the extremum sits at a different node
from the acceleration peak.

### 1.1 The characteristic timescale

Form the ratio of a coefficient to its own rate:

$$\tau = \frac{|g_1^0|}{|\dot{g}_1^0|} = \frac{30000}{12}
= 2500\ \mathrm{yr} \qquad \text{(before 1990)},$$

$$\tau = \frac{30491}{23} = 1326\ \mathrm{yr} \qquad \text{(at the jerk)},$$

$$\tau = \frac{30990}{34} = 912\ \mathrm{yr} \qquad \text{(after 2005)}.$$

A field that changes on a 10²–10³ yr timescale in a core whose resistive
diffusion time is far longer is a field being **advected**, not diffused. That
is the observational argument for a dynamo
([08-01-05](05-dynamo-theory.md)), and the honest statement of it is comparative:
the timescale is short relative to the free-decay time computed in §2 of
[08-01-05](05-dynamo-theory.md).

## 2. Kinematics: frozen flux and what it does not tell you

The magnetic induction equation for a moving conductor is

$$\frac{\partial \mathbf{B}}{\partial t}
= \nabla\times\left(\mathbf{u}\times\mathbf{B}\right)
+ \eta\nabla^2\mathbf{B}, \qquad \eta = \frac{1}{\mu_0\sigma}.$$

When the flow is fast and the conductor good, the advective term dominates and
the field is **frozen into the fluid**: field lines move with the flow. Section 7
of the demonstration shows the two limits side by side using exact spectral
operators:

| operator over one time unit | peak amplitude retained | correlation with the initial field |
|---|---|---|
| pure advection, $u = 0.10$ | 0.999997 | +0.809017 |
| pure diffusion, $D = 0.02$ | 0.454041 | +1.000000 |

with the advected fundamental's phase shifted by exactly $-36.000^{\circ}$
(= $-uT\times360^{\circ}$). Advection moves the pattern and keeps its amplitude;
diffusion keeps its shape and destroys its amplitude. The frozen-flux
approximation is the statement that the first column applies on the timescale of
interest.

### 2.1 The null space of the flow inversion

Take the radial component at the core surface, where $B_r$ is the only component
that matters and $\mathbf{u}$ is tangentially geostrophic by assumption. Setting
the diffusion term to zero,

$$\frac{\partial B_r}{\partial t} = -\nabla_h\cdot\left(\mathbf{u}\,B_r\right),$$

which is one scalar equation for the two components of $\mathbf{u}$. It therefore
determines only the **component of the flow perpendicular to the horizontal
field contours**, and is completely blind to flow along those contours. That
null space is not a technicality: the ambiguity is exact, the same in kind as the
internal/external ambiguity of
[08-01-03](03-spherical-harmonic-magnetic.md) §7.1, and it is why "core flow
models" come as families with stated auxiliary assumptions (tangential
geostrophy, steady flow, no upwelling at the equator) rather than as unique
answers. See
[12-04-01 Observations of the Core Field and Secular Variation](../../12-global-geophysics-interior/04-geomagnetism-and-core/01-core-field-observations.md)
for how the constraints are combined in practice.

### 2.2 Westward drift, measured

The simplest kinematic statement is that the non-dipole pattern drifts westwards
at a roughly constant rate. Measure it from the **phase** of a harmonic of order
$m$: for a pattern $p(\phi) = \cos m(\phi - \Delta)$, the complex Fourier
coefficient $\sum_k p_k e^{-im\phi_k}$ has argument $m\Delta$, so

$$\Delta = \frac{1}{m}\arg\sum_k p_k e^{-im\phi_k}.$$

The demonstration uses a synthetic drift of $0.150\ \mathrm{deg\,yr^{-1}}$,
reuses the pattern after 10 yr, and recovers

$$\text{shift} = -1.5000^{\circ} \quad\Longrightarrow\quad
\text{drift rate} = 0.1500\ \mathrm{deg\,yr^{-1}},$$

exactly, with the negative sign meaning westward. Two numbers make the
measurement quantitative:

- **Aliasing.** A harmonic of order $m$ is periodic in $180^{\circ}/m$ of
  longitude, so the phase estimate is ambiguous beyond a shift of $90^{\circ}$
  for $m = 2$. Over a 10 yr interval this aliases at
  $9.00\ \mathrm{deg\,yr^{-1}}$; higher $m$ aliases sooner. Drift estimates must
  therefore be made over a short enough interval, which conflicts with the noise
  argument of §5.
- **Speed.** One degree of longitude at the equator is
  $2\pi a/360 = 111.195\ \mathrm{km}$ (from $a = 6371\ \mathrm{km}$), so
  $0.150\ \mathrm{deg\,yr^{-1}}$ corresponds to

  $$u = \frac{0.150\times111.195\times10^{3}}{3.1557\times10^{7}}
  = 5.285\times10^{-4}\ \mathrm{m\,s^{-1}},$$

  with $3.1557\times10^{7}\ \mathrm{s\,yr^{-1}}$ ($365.25$ days).

A rate that is a *kinematic* statement is not a proof of rigid westward motion:
differential rotation fits the same data.

## 3. The secular-variation spectrum

Apply the Mauersberger–Lowes construction of
[08-01-03](03-spherical-harmonic-magnetic.md) §4 to the coefficient *rates*:

$$\dot{R}_n = (n+1)\sum_m\left[\left(\dot{g}_n^m\right)^2
+ \left(\dot{h}_n^m\right)^2\right].$$

With the demonstration's synthetic SV coefficients:

| $n$ | $\dot{R}_n$ ((nT/yr)²) | share | $\dot{R}_n/\dot{R}_1$ |
|---|---|---|---|
| 1 | 242.0 | 32.49% | 1.00 |
| 2 | 267.0 | 35.84% | 1.103 |
| 3 | 186.0 | 24.97% | 0.7686 |
| 4 | 49.9 | 6.70% | 0.2062 |

The comparison with the field spectrum of [08-01-03](03-spherical-harmonic-magnetic.md)
§4.2 is the physical point: there the dipole held 98.63% of the power, here it
holds 32.49% and degree 2 holds more. **The SV spectrum is far less red than the
field spectrum.** Short-wavelength structure in the field is *relatively* more
active, which is consistent with advection of a smooth field by a flow whose
characteristic scale is a few thousand kilometres. It is also a warning: a
"dipole-dominant" intuition about the main field does not transfer to its time
derivative.

## 4. Derivatives versus noise

Finite differences are the only way to get time derivatives from a tabulated
series, and they multiply noise. The demonstration runs a Monte Carlo with
$20\,000$ realisations of white noise of rms $1\ \mathrm{nT}$ on annual means and
measures the standard deviation of the centred derivative estimators:

| estimator | measured $\sigma$ | theory | gain |
|---|---|---|---|
| SV, $(E_{i+1}-E_{i-1})/2\Delta t$ | 0.7062 nT/yr | $\sqrt{1/2} = 0.7071$ | 0.71× |
| acceleration, $(E_{i+2}-2E_i+E_{i-2})/4$ | 0.6114 nT/yr² | $\sqrt{6}/4 = 0.6124$ | 0.61× |
| jerk, $(E_{i+3}-3E_{i+1}+3E_{i-1}-E_{i-3})/8$ | 0.5581 nT/yr³ | $\sqrt{20}/8 = 0.5590$ | 0.56× |

The gains are *below* one because a centred difference of a fixed stencil
averages several samples. What matters more than the gain is the **signal**: the
third derivative of a smooth series is the smallest part of it, so the
signal-to-noise ratio falls far faster than the gain rises. And for the red noise
of a real record the third-derivative estimator is dominated by the
low-frequency part of that noise, which is the honest reason why individual
"jerk epochs" are contested in the literature and why their date moves when the
data window moves.

### 4.1 From noise to a detection threshold

Propagating the jerk estimator's gain gives a $1\sigma$ and $3\sigma$ threshold:

| noise $\sigma$ on annual means | $1\sigma$ jerk noise | $3\sigma$ threshold |
|---|---|---|
| 0.5 nT | 0.280 nT/yr³ | 0.839 nT/yr³ |
| 1.0 nT | 0.559 nT/yr³ | 1.677 nT/yr³ |
| 2.0 nT | 1.118 nT/yr³ | 3.354 nT/yr³ |

The synthetic jerk peaks at $1.895\ \mathrm{nT\,yr^{-3}}$, so it is detected with a
comfortable margin even at $2\ \mathrm{nT}$ noise — **provided** the record
contains the quiet intervals on either side that define the baseline. A jerk
detected only from the interval containing it is a curve fit, not a detection.

## 5. Extrapolation: the error a survey actually pays

Suppose a model is fitted in 1985, carries the then-current slope of
$-12\ \mathrm{nT\,yr^{-1}}$, and is used afterwards. The demonstration's true
series changed slope at 1990:

| year | true $g_1^0$ (nT) | model $g_1^0$ (nT) | error (nT) |
|---|---|---|---|
| 1986 | −30432.08 | −30432.02 | +0.06 |
| 1990 | −30491.44 | −30480.02 | +11.42 |
| 1995 | −30650.02 | −30540.02 | +110.00 |
| 2005 | −30990.00 | −30660.02 | +329.98 |
| 2020 | −31500.00 | −30840.02 | +659.98 |

The error is the **integral of the unmodelled slope change**, so it grows
*linearly* in the extrapolation interval, not quadratically: after the first year
the slope error is constant, and each further year adds the same increment. After
35 years the mismodelled part is $660\ \mathrm{nT}$ — larger than most crustal
anomalies of interest. This is the practical rule that a main-field model is
extrapolated with a secular-variation term for a stated validity interval and
then re-fitted, and it is why the epoch of a model is part of its definition
rather than a footnote.

## 6. Assumptions and regime of validity

1. **Sampling.** All derivative estimates above assume annual samples of the
   element. A different sampling changes the noise gains by
   $1/\Delta t^{k}$ for the $k$-th derivative and changes the aliasing behaviour
   of §2.2.
2. **Noise model.** White noise on annual means is the simplest defensible
   model; real records have red noise, which makes the jerk estimator worse than
   the table of §4 suggests.
3. **Frozen flux.** The kinematic statements of §2 assume $\eta\nabla^2\mathbf{B}$
   is negligible. That is an approximation whose validity is scale-dependent, and
   it fails for the smallest scales.
4. **Rigid rotation.** The drift rate is a phase rate; it is not evidence of
   rigid motion.
5. **A single epoch for the flow inversion.** Assuming steady flow is an extra
   assumption, not a consequence of the data.
6. **Synthetic coefficients.** Every magnitude in this lesson is a teaching value
   chosen for its behaviour, not the Earth's behaviour.

## 7. Python demonstration

`code/secular_variation_demo.py` prints, with units:

1. a synthetic $g_1^0(t)$ with a smooth jerk, and its first three derivatives;
2. the secular-variation spectrum by degree with shares;
3. westward drift measured from the phase of an $m = 2$ pattern, with the
   aliasing limit and the implied fluid speed;
4. the Monte Carlo noise gains of the three derivative estimators;
5. the growth of linear-SV extrapolation error after a slope change;
6. jerk detection thresholds for three noise levels;
7. advection versus diffusion of one pattern using exact spectral operators.

Exercises and solutions:
[`exercises/04-secular-variation-exercises.md`](./exercises/04-secular-variation-exercises.md),
[`exercises/04-secular-variation-solutions.md`](./exercises/04-secular-variation-solutions.md).

## Mastery checkpoint

1. Compute $\tau = |g_1^0|/|\dot{g}_1^0|$ from the table of §1 for 1960 and for
   2005, and state in one sentence what the difference implies about the core.
2. Show that the phase of the $m$-th Fourier coefficient of a pattern
   $\cos m(\phi-\Delta)$ equals $m\Delta$, and state the resulting aliasing limit
   for $m = 3$ over a 5-year interval.
3. Convert $0.15\ \mathrm{deg\,yr^{-1}}$ of westward drift into m/s at the
   equator, showing the unit chain.
4. Using the noise gains of §4, compute the $3\sigma$ jerk threshold for
   $1.5\ \mathrm{nT}$ noise.
5. Explain why the extrapolation error of §5 grows linearly and not
   quadratically.
6. State the null space of the frozen-flux flow inversion.

## Common pitfalls

1. **Quoting a jerk without a noise level.** Section 4.1 is the required
   companion.
2. **Computing SV as a secant over unequal intervals.** Use the same interval
   throughout, or fit a local polynomial.
3. **Reading the SV spectrum as the field spectrum.** Section 3 measures the
   difference; they are not the same shape.
4. **Treating a drift rate as a velocity field.** It is a phase rate.
5. **Extrapolating a model outside its stated validity window.** Section 5
   prices it.
6. **Forgetting that the SV term is itself a fitted quantity** with its own
   uncertainty, which is not the same as the field's.

## Related modules

- [08-01-03 Spherical Harmonic Analysis of the Magnetic Field](03-spherical-harmonic-magnetic.md) —
  the static coefficients whose rates these are.
- [08-01-05 The Geodynamo: Mechanism and Evidence](05-dynamo-theory.md) — the
  mechanism the timescale argument points to.
- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](06-palaeomagnetism.md) —
  the same field on geological timescales.
- [20-signal-processing](../../20-signal-processing/README.md) — derivative
  estimators, spectra and noise.
- [12-04-02 Numerical Geodynamo Models](../../12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md) —
  what numerical dynamos say about core flow.

## Self-assessment checklist

- [ ] I can define SV, acceleration and jerk with units.
- [ ] I can compute a characteristic timescale and state its limits.
- [ ] I can write the frozen-flux equation and name its null space.
- [ ] I can measure a drift rate from a harmonic phase and state its aliasing
      limit.
- [ ] I can propagate a noise level to a derivative uncertainty.
- [ ] I can price the error of extrapolating a main-field model.
