---
id: 15-02-06
title: "Ocean-Bottom Seismology and OBS Networks"
level: doctoral
prereqs: ["15-02-01", "15-01-01", "06-08-01"]
tags: [oceanography, marine-geophysics, obs, ocean-bottom-seismology, compliance-noise, receiver-functions, clock-drift]
---

# Ocean-Bottom Seismology and OBS Networks

> **All models and data in this module are SYNTHETIC.** The water depths,
> velocities, noise levels and instrument errors used here are chosen teaching
> values, printed by the demonstration in `code/`. No OBS network, station, event,
> deployment or published record is reproduced.

An ocean-bottom seismometer puts a three-component sensor and a hydrophone on the
seafloor and leaves it there for months. It is the only way to record seismic
energy that never reaches land: the ocean basins are a seismological blind spot
for every land-based network, and more than two-thirds of the Earth's surface is
behind that blind spot.

The instrument is simple and the errors are not. A free-falling package must land
with a known orientation, keep time for months without a satellite, survive being
insulated from the ocean by a kilometre of water, and record a signal whose
largest noise source — the seafloor's own deformation under infragravity waves —
is coherent with a channel that is cheap to measure and easy to ignore. **This
lesson derives the water-layer multiple, removes compliance noise quantitatively,
and converts the instrument's small flaws into metres and seconds.**

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the water-column multiple period $T_w = 2h/c$ and **compute** the
   comb of notch frequencies it imposes on every ocean-bottom record.
2. **Construct** a synthetic receiver function containing water-layer multiples
   and **state** the water depth at which the multiple spacing becomes shorter
   than a crustal Ps delay, and why that case needs demultiple.
3. **Estimate** the compliance transfer from a co-located pressure channel and
   **measure** the variance reduction it achieves.
4. **Convert** a sensor tilt into a horizontal-to-vertical leakage and **state**
   the tilt at which the leakage is comparable to a real conversion.
5. **Convert** a clock drift into a timing error, a travel-time error and a
   location error, and **state** the drift a modern network can tolerate.
6. **Verify** each calculation against a closed form or an independent route.

## Prerequisites

- [15-02-01 Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) —
  the reflection coefficients and convolution model used throughout.
- [15-01-01 Seawater Properties: Temperature, Salinity, Density](../01-physical-oceanography/01-seawater-properties.md) —
  the sound speed that turns a period into a depth.
- [06-08-01 Receiver Functions: Deconvolution and Ps Conversions](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  the conversion whose delay is measured here, and the non-uniqueness that comes
  with it.

## 1. The water-column multiple

A wave trapped between the sea surface (a pressure release, reflection coefficient
$\approx -1$) and the seafloor (a strong reflector) bounces with a two-way period

$$\boxed{\;T_w = \frac{2h}{c}.\;}$$

| water depth (m) | $T_w$ (s) | $1/T_w$ (Hz) |
|---|---|---|
| 1000 | 1.3333 | 0.7500 |
| 2000 | 2.6667 | 0.3750 |
| 3000 | 4.0000 | 0.2500 |
| 4000 | 5.3333 | 0.1875 |
| 5000 | 6.6667 | 0.1500 |

Three consequences, in increasing order of importance.

- **$T_w$ measures the water depth** to the accuracy of $c$, which is
  $1\,\%$ if a $1500\ \mathrm{m\,s^{-1}}$ reference is used. The seismogram
  therefore carries its own bathymetry.
- **Every arrival below the seabed repeats** at offsets of $T_w$, with amplitudes
  multiplied by the seafloor reflection coefficient once per bounce.
- **The spectrum is notched** at multiples of $1/T_w$, because the multiples sum
  to a comb. Any spectral estimate from an ocean-bottom record must either model
  the comb or avoid it.

**A factor-of-two error in $T_w$ is the commonest mistake in using it**, which is
why the demonstration verifies the round trip explicitly for five depths.

## 2. Water multiples in a receiver function

A synthetic receiver function is built from a direct P at $2.000\ \mathrm{s}$, a
Ps conversion at a sediment–mantle interface, and multiples of each at offsets of
$T_w$, with the seafloor reflection coefficient $-0.4$ applied once per bounce.
For a $2\ \mathrm{km}$ sediment layer with $v_p = 2000\ \mathrm{m\,s^{-1}}$,
$v_s = 1200\ \mathrm{m\,s^{-1}}$ and ray parameter
$p = 0.060\ \mathrm{s\,km^{-1}}$:

$$q_p = \sqrt{1/2.0^{2} - 0.060^{2}} = 0.496387\ \mathrm{s\,km^{-1}}, \qquad
q_s = \sqrt{1/1.2^{2} - 0.060^{2}} = 0.831171\ \mathrm{s\,km^{-1}},$$

$$\Delta t_{Ps} = H(q_s - q_p) = 2.0(0.334784) = 0.6696\ \mathrm{s}.$$

**The Ps delay ($0.67\ \mathrm{s}$) is much shorter than the multiple spacing
($4.00\ \mathrm{s}$) at this water depth**, so the first few arrivals are
separable by eye. That is a property of *this* depth, not of the method:

| water depth (m) | $T_w$ (s) | $\Delta t_{Ps}/T_w$ |
|---|---|---|
| 3000 | 4.000 | 0.167 |
| 600 | 0.800 | 0.837 |
| 200 | 0.267 | **2.512** |

At $200\ \mathrm{m}$ of water the multiple spacing is *shorter* than the Ps delay:
the first multiple of the direct P arrives before the conversion does, and the
record becomes an unresolvable comb. **The shelf case is not merely harder; it
requires the water-layer multiples to be modelled and removed before any
conversion can be identified at all**, whereas deep-water work is comparatively
easy. This is the reason the deep-ocean OBS is the instrument of choice for
mantle-scale receiver-function work.

## 3. Compliance noise and its removal

Infragravity surface waves — long-period ocean waves with periods of tens of
seconds to a few minutes — force the seafloor with a pressure signal that the
seafloor deforms under. The resulting vertical motion is **compliance noise**, and
it is the dominant signal on the vertical channel of a deep OBS at periods of
20–200 s. It is *not* instrument noise, and it *cannot* be removed by averaging,
because it is coherent over the whole array.

It can, however, be removed by measuring it. A co-located pressure sensor records
the forcing directly, and the vertical channel is corrected by

$$V'(f) = V(f) - Z(f)\,P(f), \qquad
Z(f) = \frac{\langle V P^{*}\rangle}{\langle |P|^{2}\rangle},$$

where $Z$ is the compliance transfer function and the angle brackets denote a
spectral average over a band.

The demonstration's synthetic experiment: an infragravity pressure signal, a
compliance transfer that peaks near $0.015\ \mathrm{Hz}$ (a chosen teaching
shape), a vertical channel with compliance amplitude 1.00 and instrument noise
0.0494.

| estimator | variance before | variance after | reduction | residual std | coherence with $P$ |
|---|---|---|---|---|---|
| single scalar over the whole band | 1.0020 | 0.1670 | 6.0 | 0.4086 | – |
| frequency-dependent $Z(f)$ | 1.0020 | 0.0024 | **410** | **0.0494** | $5\times10^{-6}$ |

Two results, both worth carrying forward.

- **The frequency-dependent estimator leaves a residual standard deviation of
  $0.0494$, identical to the instrument noise**, and a squared coherence with
  pressure of $5\times10^{-6}$. The compliance has been removed and the instrument
  noise has not. That is the definition of a correct correction.
- **A single scalar for the whole band leaves a residual eight times larger.** The
  compliance is a function of period, so the estimator must be too. This is the
  kind of error that survives because the corrected record still *looks* right.

**The check that the correction is safe.** Applying the same estimator to an
uncorrelated pressure and vertical pair leaves the variance essentially unchanged
(measured ratio $1.12$, a finite-sample effect of the spectral estimator): a
correct compliance removal takes out the coherent part and nothing else.

## 4. Sensor tilt

A sensor tilted by $\theta$ measures
$a\cos\theta + h\sin\theta$, mixing the true vertical $a$ and horizontal $h$ with
leakage amplitude $\sin\theta$:

| tilt | $\sin\theta$ | leaked fraction of horizontal |
|---|---|---|
| $0.5^\circ$ | 0.008727 | 0.87 % |
| $1.0^\circ$ | 0.017452 | 1.75 % |
| $2.0^\circ$ | 0.034899 | 3.49 % |
| $5.0^\circ$ | 0.087156 | **8.72 %** |
| $10.0^\circ$ | 0.173648 | 17.36 % |

**A $5^\circ$ tilt leaks $8.7\,\%$ of every horizontal arrival onto the vertical
channel** — comparable to the amplitude of a real Ps conversion, which is a few
per cent of the direct P. An uncorrected tilt therefore manufactures conversions.
The tilt must be *measured* — from a compass and accelerometer in the package, or
inferred from the two horizontal channels' long-period coherence — and the three
components rotated before any receiver-function analysis. This is a first-order
correction masquerading as a calibration detail.

## 5. Clock drift

An OBS cannot see a satellite, so its clock free-runs. Converting a drift into the
quantities that matter, with an apparent velocity of $8\ \mathrm{km\,s^{-1}}$:

| drift (s day$^{-1}$) | over 30 days (s) | over 180 days (s) | location error at 180 days (m) |
|---|---|---|---|
| 0.001 | 0.030 | 0.180 | 1440 |
| 0.010 | 0.300 | 1.800 | 14400 |
| 0.100 | 3.000 | 18.000 | 144000 |
| 1.000 | 30.000 | 180.000 | 1440000 |

A $1\ \mathrm{ms\,day^{-1}}$ drift — which sounds negligible — is 18 s over six
months and, through an apparent velocity, **1.4 km of apparent mislocation**. Clock
drift is therefore not a subtlety; it is a first-order error that must be measured.
The standard method does not require an absolute reference: **cross-correlate a
common event between adjacent instruments**, whose relative drift is then known,
and anchor the network to a GNSS-disciplined clock at one site. The residual is
the drift of a single clock over the interval between events, which is minutes
rather than months.

## 6. Assumptions and regime of validity

1. **A flat seafloor and a constant sound speed.** $T_w = 2h/c$ uses one $c$; a
   real sound-speed profile changes the effective $c$ by a per cent or so, which
   is why $T_w$ gives a depth to about $1\,\%$.
2. **A constant seafloor reflection coefficient.** It varies with angle and with
   frequency, so the multiple amplitudes are not simply geometric.
3. **A one-dimensional sediment model** for the Ps delay, with the same
   non-uniqueness documented in
   [06-08-01](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md):
   a delay gives a thickness *conditional on a velocity ratio*.
4. **A linear compliance transfer.** The real seafloor's compliance is
   frequency-dependent and depends on the sediment's shear modulus; a nonlinear or
   a spatially varying transfer leaves a residual.
5. **A rigidly coupled sensor.** A package sitting on soft sediment can resonate;
   the coupling resonance is a separate and often dominant problem.
6. **No tilt variation.** Tilt can change during a deployment as the package
   settles, so a single rotation angle may not be enough.
7. **A single clock model.** Real clocks drift non-linearly, and temperature
   changes the rate.

## 7. Worked examples

### Example 1 — reading the water depth from a record

A record shows repeated arrivals at $4.00$, $8.00$ and $12.00\ \mathrm{s}$:

$$h = \frac{c T_w}{2} = \frac{1500 \times 4.00}{2} = 3000\ \mathrm{m}.$$

If the true sound speed were $1520\ \mathrm{m\,s^{-1}}$ instead of the assumed
$1500$, the inferred depth would be $3040\ \mathrm{m}$ — a $1.3\,\%$ error, which
is the accuracy of the method and the reason it is a cross-check rather than a
survey.

### Example 2 — how much compliance noise is too much?

Suppose a target signal has an rms amplitude of $0.02$ in the same units as the
demonstration's. Before correction the vertical channel's standard deviation is
$1.001$ — a signal-to-noise ratio of $0.02$. After correction it is $0.0494$ — a
ratio of $0.40$. **The correction buys a factor 20 in signal-to-noise**, and it
changes the question from "impossible" to "requiring stacking". A team that
ignores the pressure channel does not merely get noisier data; it gets data whose
noise is coherent across the array and therefore does not average down.

### Example 3 — the tilt budget

Target conversions are a few per cent of the direct P. To keep the leaked
horizontal amplitude below $1\,\%$:

$$\sin\theta \le 0.01 \;\Longrightarrow\; \theta \le 0.57^\circ .$$

**The tilt must be known to better than about half a degree**, which is achievable
with a pendulum-and-compass package but not with a free-fall and a hope.

## 8. Python demonstration

`code/obn_ocean_bottom_seismology_demo.py` prints everything above with units:

1. $T_w$ against water depth and the round-trip verification;
2. a synthetic receiver function with water multiples, and the Ps delay from the
   vertical-slowness algebra;
3. the compliance correction, with a frequency-dependent and a single-scalar
   estimator compared, and the coherence after correction;
4. tilt leakage against tilt angle;
5. clock drift converted to time, distance and location error;
6. verification: the round trip, the unbiased-estimator check, the zero-tilt
   limit, and the reality of the vertical slownesses.

Run it with

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python obn_ocean_bottom_seismology_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/06-obn-ocean-bottom-seismology-exercises.md`](exercises/06-obn-ocean-bottom-seismology-exercises.md)
and
[`exercises/06-obn-ocean-bottom-seismology-solutions.md`](exercises/06-obn-ocean-bottom-seismology-solutions.md).

- ★ Compute $T_w$ and the notch spacing for a $2500\ \mathrm{m}$ water depth, and
  convert $T_w$ back to a depth.
- ★★ Compute the Ps delay for a $3\ \mathrm{km}$ layer with
  $v_p = 2500\ \mathrm{m\,s^{-1}}$, $v_s = 1400\ \mathrm{m\,s^{-1}}$ at
  $p = 0.055\ \mathrm{s\,km^{-1}}$, and state whether the shelf case
  ($h = 150\ \mathrm{m}$) would resolve it.
- ★★ Compute the leaked horizontal amplitude on the vertical channel for tilts of
  $0.3^\circ$, $1^\circ$ and $3^\circ$, and state the tilt required to keep the
  leakage below $0.5\,\%$.
- ★★★ Design an OBS deployment that determines a $1\ \mathrm{mm\,s^{-1}}$ mantle
  velocity anomaly, stating the instrument requirements, the clock strategy, the
  tilt strategy and the noise budget.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use $c = 1500\ \mathrm{m\,s^{-1}}$.

> A free-fall OBS lands in $3500\ \mathrm{m}$ of water and records for 200 days.
> **(a)** Compute $T_w$ and the frequency of the first spectral notch.
> **(b)** A Ps conversion arrives $0.85\ \mathrm{s}$ after the direct P. State how
> far away the nearest water multiple of the P is, and whether identification is
> possible by inspection.
> **(c)** The clock drifts by $0.02\ \mathrm{s\,day^{-1}}$ and the package lands
> tilted by $3^\circ$. Compute the total timing error over the deployment, the
> location error at $8\ \mathrm{km\,s^{-1}}$, and the leaked amplitude fraction.
> **(d)** State which of the two errors (c) can be corrected after the fact and
> which requires a design change, and why.

A worked version of (a)–(d) is in the lesson-06
[solutions](exercises/06-obn-ocean-bottom-seismology-solutions.md).

## Common pitfalls

1. **Forgetting the factor of two in $T_w = 2h/c$.** Verified explicitly in the
   demonstration because it is the commonest error.
2. **Ignoring the pressure channel.** Compliance noise is coherent across an array
   and does not average down.
3. **Using a single scalar compliance.** Section 3: the residual is eight times
   larger.
4. **Neglecting tilt.** A $5^\circ$ tilt manufactures conversions at $8.7\,\%$ of
   the horizontal amplitude.
5. **Trusting the clock.** $1\ \mathrm{ms\,day^{-1}}$ is kilometres over six months.
6. **Treating a Ps delay as a depth.** It is a thickness conditional on a velocity
   ratio, with the trade-off quantified in
   [06-08-01](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md).
7. **Assuming the shelf case is like the deep case.** At $200\ \mathrm{m}$ of water
   the multiple comb is finer than the conversion delay, and demultiple is
   mandatory rather than optional.

## Related modules

- [01 Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) —
  the controlled-source alternative to passive recording.
- [02 Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) —
  the water depth that sets $T_w$, measured independently.
- [07 Marine CSEM and EM for Gas Hydrates](07-marine-csem-em.md) —
  the other seafloor instrument that must survive a free fall and a long deployment.
- [06-08 Receiver Functions and Crustal Structure](../../06-seismology/08-receiver-functions-and-crustal-structure/README.md) —
  what the conversions measured here are inverted for.
- [06-07 Ambient Noise and Interferometry](../../06-seismology/07-ambient-noise-and-interferometry/README.md) —
  the other long-deployment passive method, with the same clock and tilt problems.

## Self-assessment checklist

- [ ] I can derive $T_w$ and convert it to a depth and a notch frequency.
- [ ] I can construct a receiver function with water multiples and identify them.
- [ ] I can state when the multiple comb becomes unresolvable.
- [ ] I can estimate a compliance transfer and measure the variance reduction.
- [ ] I can convert a tilt into a leakage fraction.
- [ ] I can convert a clock drift into seconds, metres and a location error.
- [ ] I can say which of these errors is correctable after the fact.
