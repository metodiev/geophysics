---
id: 17-03-07
title: "Radar Altimetry and Sea/Ice Surface Height"
level: doctoral
prereqs: ["17-03-01", "07-04-02", "12-06-02"]
tags: [remote-sensing, radar, altimetry, sea-surface-height, sea-ice, geostrophy, aliasing]
---

# Radar Altimetry and Sea/Ice Surface Height

> All models and data in this module are **SYNTHETIC**. The orbit height, pulse
> length, wave heights, sea surface profiles, repeat cycles, freeboards and
> densities in this lesson are teaching values computed by the demonstration. No
> real mission, product or measured sea surface is used. The M2 tidal period
> $12.4206012\ \mathrm{h}$ is the standard astronomical value; $c$, $g$ and
> $\Omega$ are stated standard constants.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a round-trip time into a range, and **state** the timing precision
   required for a centimetre-level height.
2. **Derive** the pulse-limited footprint $\rho = \sqrt{c\tau h}$ and **explain**
   why the altimeter's resolution is set by the pulse rather than the antenna.
3. **Derive** the relation between the leading-edge width and significant wave
   height, and **verify** the conversion factor by synthesising waveforms.
4. **Quantify** the speckle-averaging gain and **identify** the resolution cost
   that buys it.
5. **Derive** the geostrophic balance used to turn a sea surface slope into a
   current, and **state** why the measurement is a difference of large numbers.
6. **Compute** the aliased period of a tidal constituent for a stated repeat
   cycle, and **explain** why aliasing is a design constraint.
7. **Convert** an ice freeboard into a thickness and **quantify** the sensitivity
   to the assumed densities and to the snow layer.

## Prerequisites

- [17-03-01 SAR Principles: Geometry, Polarisation, Backscatter](01-sar-principles.md) —
  the range–time relation and pulse compression.
- [07-04-02 Height Systems and the Geoid](../../07-gravity-geodesy/04-geodesy-reference-frames/02-height-systems.md) —
  ellipsoidal, orthometric and mean-sea-surface heights.
- [12-06-02 Tidal Love Numbers](../../12-global-geophysics-interior/06-geodesy-constraints-interior/02-tidal-love-numbers.md) —
  why the solid Earth also moves under the tide.

## 1. Intuition: the one geometry where the pulse sets the resolution

An altimeter looks straight down. There is no synthetic aperture to exploit, so
resolution must come from somewhere else, and it comes from the *pulse*: the
shortest pulse gives the smallest area of surface that can contribute to a single
range gate. Everything about altimeter design follows from that one inversion of
the SAR logic.

The deliverables are deceptively simple — a height above a reference surface, and
a wave height from the shape of the return. The difficulty is entirely in the
reference and in the assumptions: the range is measured to centimetres, but the
height requires the orbit, the geoid, the tide and the atmospheric delay to
almost the same accuracy, and the geophysical signal is obtained by differencing
numbers of order a thousand kilometres.

## 2. Definitions

| Symbol | Meaning | Unit |
|---|---|---|
| $\tau$ | pulse duration | s |
| $h$ | altitude above the surface | m |
| $\rho$ | pulse-limited footprint radius | m |
| $SWH$ | significant wave height | m |
| $\sigma_z$ | standard deviation of surface height, $SWH/4$ | m |
| $SSH$ | sea surface height above a reference surface | m |

Two conventions must be stated whenever they are used:

- $SWH = 4\sigma_z$ **by definition** (four times the standard deviation of the
  surface elevation), which is why the leading-edge width converts with the
  factor derived in Section 3.3.
- The *retracking* step — fitting a model waveform to the measured one to obtain
  the epoch (range) and the leading-edge slope — is where the height and the wave
  height are actually extracted. Different retrackers give different numbers, and
  the choice belongs in the metadata.

## 3. Derivations

### 3.1 Round trip and the timing requirement

$$r = \frac{c\,t}{2}.$$

| timing precision | range precision |
|---|---|
| 10 ns | 149.90 cm |
| 1 ns | 14.99 cm |
| 0.1 ns | 1.50 cm |
| 0.01 ns | 0.15 cm |

A centimetre of height needs a tenth of a nanosecond of *effective* timing, far
better than any single pulse. The gain comes from averaging (Section 3.4) and
from the fact that a systematic timing bias cancels in the *difference* between
the sea surface and a reference surface measured by the same instrument. That
cancellation is the reason the geoid and the orbit must be modelled rather than
the instrument refined without limit.

### 3.2 The pulse-limited footprint

The leading edge of the return comes from the annulus whose range exceeds the
nadir range by less than half the pulse length. For a radius $\rho$ on a sphere
of radius $h$ (the altitude),

$$\Delta r \approx \frac{\rho^{2}}{2h} < \frac{c\tau}{2}
\qquad\Longrightarrow\qquad
\boxed{\;\rho = \sqrt{c\,\tau\,h}.\;}$$

*Numerical check (SYNTHETIC),* from the demonstration:

| pulse | altitude | footprint radius | footprint area |
|---|---|---|---|
| 1 ns | 500 km | 387.2 m | 0.4709 km² |
| 1 ns | 800 km | 489.7 m | 0.7535 km² |
| 3 ns | 800 km | 848.2 m | 2.2604 km² |
| 3 ns | 1300 km | 1081.3 m | 3.6731 km² |

The footprint grows as $\sqrt{\tau h}$: a shorter pulse and a lower orbit both
shrink it. This is the opposite of the SAR logic of
[lesson 01](01-sar-principles.md), where a *smaller* antenna gave a finer
resolution. Here the antenna is deliberately made wide enough to illuminate the
whole range window, and the resolution is bought with bandwidth.

### 3.3 The leading edge and the wave height

The returned waveform is the flat-surface response convolved with the
distribution of surface heights. Taking the heights to be Gaussian with standard
deviation $\sigma_z$, the leading edge becomes an error-function ramp whose
10–90% width is

$$w = 2\times1.2816\,\sigma_z = 2.5632\,\sigma_z .$$

Since $SWH = 4\sigma_z$ by definition,

$$SWH = \frac{4}{2.5632}\,w = 1.5605\,w
\qquad\Longleftrightarrow\qquad
\frac{w}{SWH} = 0.6407 .$$

The demonstration synthesises waveforms (step $\otimes$ pulse box $\otimes$
Gaussian pdf) and measures the ratio rather than assuming it:

| $SWH$ | $\sigma_z$ | measured width | width $/SWH$ |
|---|---|---|---|
| 1.0 m | 0.250 m | 0.6550 m | 0.6550 |
| 2.0 m | 0.500 m | 1.2850 m | 0.6425 |
| 4.0 m | 1.000 m | 2.5650 m | 0.6412 |
| 8.0 m | 2.000 m | 5.1250 m | 0.6406 |

The ratio converges to $0.6407$ as the sea grows, and is $0.6550$ at $1\ \mathrm{m}$
because the flat-pulse rise itself contributes $c\tau/2 = 0.1499\ \mathrm{m}$ at
$\tau = 1\ \mathrm{ns}$. That systematic, plus the beam-weighting and the
non-Gaussianity of a real sea, is why the extraction is done by *retracking* a
model waveform: the correction terms are large enough to matter at the
centimetre level.

### 3.4 Speckle averaging and its cost

Each pulse illuminates a different set of scatterers, so successive range
estimates are independent and $N$ pulses reduce the height error as
$\sigma_1/\sqrt{N}$:

| $N$ pulses | relative precision | height error for $\sigma_1 = 45$ cm |
|---|---|---|
| 1 | 1.0000 | 45.00 cm |
| 10 | 0.3162 | 14.23 cm |
| 100 | 0.1000 | 4.50 cm |
| 1000 | 0.0316 | 1.42 cm |
| 10000 | 0.0100 | 0.45 cm |

The price is spatial resolution: the $N$ pulses are gathered along the ground
track, so the effective footprint becomes a strip whose length grows with $N$.
(The $\sigma_1 = 45\ \mathrm{cm}$ figure is a teaching value: the *scaling* is
what the demonstration establishes, not the constant.)

### 3.5 Sea surface height and geostrophic velocity

Geostrophic balance for a surface current perpendicular to the pressure gradient
reads, with $f = 2\Omega\sin\phi$,

$$f\,u = -g\,\frac{\partial h}{\partial y}
\qquad\Longrightarrow\qquad
u = -\frac{g}{f}\frac{\partial h}{\partial y}.$$

*Numerical check.* At $\phi = 45^\circ$, $f = 2(7.292\,115\times10^{-5})\sin45^\circ
= 1.031261\times10^{-4}\ \mathrm{s^{-1}}$. A slope of $1\ \mathrm{cm}$ per
$10\ \mathrm{km}$ is $1\times10^{-6}$, giving

$$u = \frac{9.80665}{1.031261\times10^{-4}}\times10^{-6} = 0.0951\ \mathrm{m\,s^{-1}}
\approx 10\ \mathrm{cm\,s^{-1}}.$$

That single number explains why satellite altimetry is a successful oceanographic
instrument and why it is hard: a $10\ \mathrm{cm\,s^{-1}}$ current is a
$1\ \mathrm{cm}$ height difference over $10\ \mathrm{km}$, measured from
$800\ \mathrm{km}$ away, on top of a geoid undulation of tens of metres. The
demonstration's synthetic eddy (an $11\ \mathrm{cm}$ anomaly of $60\ \mathrm{km}$
Gaussian radius) gives a maximum slope of $1.044\times10^{-6}$ and a peak speed of
$0.099\ \mathrm{m\,s^{-1}}$, exactly as the rule predicts.

Two consequences worth stating:

1. **The signal is a difference.** SSH $= (\text{orbit altitude}) - (\text{range}) -
   (\text{corrections})$, all referred to an ellipsoid and then to a geoid or a
   mean sea surface. The *absolute* height is dominated by the geoid; ocean
   dynamics lives in the *residual* after removing it. Getting the geoid wrong by
   metres is invisible in the gradient if the error is smooth, and fatal if it is
   not — which is exactly the motivation for the dedicated gravity missions of
   [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md).
2. **Everything must be modelled in the same frame.** Solid Earth tides, ocean
   loading, the inverse barometer and the wet tropospheric delay are all of
   comparable size to the signal. Their treatment is the same non-uniqueness
   problem as the geodetic reference-frame issues of
   [07-04-01 Geodetic Datums](../../07-gravity-geodesy/04-geodesy-reference-frames/01-geodetic-datums.md).

### 3.6 Tidal aliasing: the repeat cycle as a filter

A satellite in a repeating orbit samples a given location once every repeat
cycle $T_r$, so any tidal constituent with frequency $f$ appears at the aliased
frequency

$$f_{\text{alias}} = \left|\,f - n\,f_s\,\right|, \qquad f_s = \frac{1}{T_r},
\qquad n = \operatorname{round}\!\left(\frac{f}{f_s}\right).$$

*Numerical check,* with the standard M2 period $12.4206012\ \mathrm{h}$:

| repeat cycle | alias period (days) |
|---|---|
| 5.0 d | 14.77 |
| 10.0 d | 30.99 |
| 20.0 d | 56.41 |
| 35.0 d | 94.49 |

A $12.42\ \mathrm{h}$ tide sampled every 10 days appears as a $31$-day
variation. It is fully coherent with the sampling, so it does not average away
with more data: it must be *modelled* with the same sampling geometry, or the
repeat cycle must be chosen so that the aliases of the constituents of interest
fall where they can be separated. **The repeat cycle is therefore a design
choice about which frequencies are observable**, not a processing detail — the
same statement, in the time domain, as the PRF window of
[lesson 01](01-sar-principles.md).

### 3.7 Freeboard to ice thickness

For a slab in hydrostatic equilibrium with ice density $\rho_i$ and water density
$\rho_w$, the thickness $T$ follows from the freeboard $F$:

$$\rho_i T = \rho_w (T - F)
\qquad\Longrightarrow\qquad
T = F\,\frac{\rho_w}{\rho_w-\rho_i}.$$

*Numerical check (SYNTHETIC densities).* With $\rho_i = 0.917$ and
$\rho_w = 1.028\ \mathrm{g\,cm^{-3}}$, the ratio is
$1.028/0.111 = 9.2613$:

| freeboard | thickness |
|---|---|
| 0.10 m | 0.9261 m |
| 0.25 m | 2.3153 m |
| 0.50 m | 4.6306 m |
| 1.00 m | 9.2613 m |

The densities matter, and the derivative says how much: at $F = 0.5\ \mathrm{m}$,

$$\frac{\partial T}{\partial\rho_i} = \frac{F\rho_w}{(\rho_w-\rho_i)^{2}}
= \frac{0.5\times1.028}{0.111^{2}} = 41.72\ \mathrm{m\ per\ g\,cm^{-3}},$$

so a density error of $0.001\ \mathrm{g\,cm^{-3}}$ moves the thickness by
$4.17\ \mathrm{cm}$, i.e. $0.90\%$ of the $4.6306\ \mathrm{m}$ answer. Three
further assumptions are as important as the densities: that the freeboard is
measured above the *local* sea surface (a range difference between two surfaces,
each with its own error), that the radar reflects from the snow–ice interface or
the air–snow interface depending on penetration, and that the ice is in
hydrostatic equilibrium at all (thin, ridged or deformed ice is not).

## 4. Worked example — from a waveform to a current

*All values SYNTHETIC.* An altimeter at $h = 800\ \mathrm{km}$ with
$\tau = 1\ \mathrm{ns}$ returns a waveform whose leading edge rises from 10% to
90% in $3.20\ \mathrm{ns}$ of two-way time, at a gate whose two-way time is
$5.3347\ \mathrm{ms}$.

1. **Range.** $r = ct/2 = 299\,792\,458 \times 5.3347\times10^{-3}/2
   = 799\,650\ \mathrm{m}$ (to five figures). The height above the surface is
   $800\,000 - 799\,650 = 350\ \mathrm{m}$ — the reason the orbit must be known
   to centimetres.
2. **Wave height.** The rise time in range is
   $c\,\Delta t/2 = 299\,792\,458\times3.20\times10^{-9}/2 = 0.4797\ \mathrm{m}$.
   With the measured ratio $0.6407$: $SWH = 0.4797/0.6407 = 0.7487\ \mathrm{m}$.
   (From Section 3.3, at this small wave height the flat-pulse correction of
   $0.1499\ \mathrm{m}$ is not negligible, and a real retracker would include
   it.)
3. **Footprint.** $\rho = \sqrt{c\tau h} = \sqrt{299\,792\,458\times10^{-9}\times8
   \times10^{5}} = 489.7\ \mathrm{m}$ radius, area $0.7535\ \mathrm{km^{2}}$.
4. **Averaging.** If the single-pulse height precision is $45\ \mathrm{cm}$ and
   400 pulses are averaged, the precision is $45/\sqrt{400} = 2.25\ \mathrm{cm}$.
5. **Current.** With a neighbouring track 10 km away reading $1.5\ \mathrm{cm}$
   higher, the slope is $1.5\times10^{-3}/10^{4} = 1.5\times10^{-6}$ and at
   $45^\circ$ N the geostrophic speed is
   $u = (g/f)\times1.5\times10^{-6} = 0.1427\ \mathrm{m\,s^{-1}}$.
6. **Interpretation and honesty.** The $1.5\ \mathrm{cm}$ difference is smaller
   than an uncorrected wet-tropospheric delay, comparable to the solid-Earth tide,
   and meaningless if the two tracks use different orbit solutions. The number is
   only as good as the list of corrections, which is why processing documentation
   is part of the measurement.

## 5. Assumptions and regime of validity

1. **Nadir geometry.** Off-nadir returns (from rough terrain or from an
   off-pointing platform) bias the range; the altimeter is designed to reject
   them, not to invert them.
2. **A Gaussian surface height distribution.** Real seas have skewness; the
   leading-edge slope is then a function of the higher moments, and retracking
   models must include them.
3. **Specular reflection from water/ice surfaces** in the altimeter's band; the
   echo from a smooth surface is stronger and easier to track, which is why open
   water is the easiest target and leads are the hardest.
4. **Independent speckle between pulses.** True for a moving platform over a
   random sea; questionable for a fixed, specular target.
5. **Geostrophic balance.** Valid for large-scale, low-frequency motions away
   from the equator ($f \to 0$ there) and away from strong friction or
   inertial motion.
6. **Known densities and hydrostatic equilibrium** for the ice conversion
   (Section 3.7).
7. **A stated frame.** All heights are meaningless without the ellipsoid, the
   geoid model, the tide model and the mean sea surface used to define them.
8. **Teaching values throughout.** The $\sigma_1 = 45\ \mathrm{cm}$, the
   synthetic eddy, the repeat cycles and the densities are chosen for arithmetic
   clarity.

## 6. Python demonstration

`code/radar_altimetry_demo.py` prints seven sections: the timing-to-range table;
the pulse-limited footprint; the synthesised leading edge and its measured ratio
to $SWH$; the speckle-averaging table; the geostrophic conversion with the
$1\ \mathrm{cm}$ per $10\ \mathrm{km}$ rule; the tidal aliasing table; and the
freeboard-to-thickness conversion with its density sensitivity.

```bash
cd 17-remote-sensing-gis/03-radar-remote-sensing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radar_altimetry_demo.py
```

## 7. Exercises

See
[`exercises/07-radar-altimetry-exercises.md`](./exercises/07-radar-altimetry-exercises.md)
and
[`exercises/07-radar-altimetry-solutions.md`](./exercises/07-radar-altimetry-solutions.md).

## Mastery checkpoint

Without notes: **(a)** compute the footprint radius for $\tau = 2\ \mathrm{ns}$ at
$h = 900\ \mathrm{km}$. **(b)** A leading edge rises 10–90% in $0.80\ \mathrm{m}$
of range; give the SWH. **(c)** Compute the geostrophic speed for a
$2\ \mathrm{cm}$ rise over $50\ \mathrm{km}$ at $60^\circ$ N. **(d)** Give the
aliased period of the M2 tide for a $20$-day repeat cycle. **(e)** State two
assumptions in the freeboard-to-thickness conversion that more averaging cannot
fix.

A worked version of (a)–(d) is in the lesson-07
[solutions](./exercises/07-radar-altimetry-solutions.md).

## Common pitfalls

1. **Quoting a height without its reference surface.** Ellipsoid, geoid and mean
   sea surface are different references.
2. **Confusing the footprint area with the resolution of the final product.** The
   along-track averaging that buys precision also buys footprint elongation.
3. **Using $SWH = 4\sigma_z$ and the leading-edge factor interchangeably.** They
   are the definition and its consequence, and both need the pulse correction at
   small wave heights.
4. **Forgetting that the tide is aliased, not averaged.** A coherent alias does
   not shrink with more data.
5. **Treating the geoid as known.** Its errors leak into every absolute height and
   into gradients if they are short-wavelength.
6. **Converting freeboard with unstated densities** and ignoring snow
   penetration.
7. **Comparing two tracks processed with different corrections.** The difference
   is then a processing artefact, not a current.

## Related modules

- [01 SAR Principles: Geometry, Polarisation, Backscatter](01-sar-principles.md) —
  the ranging and pulse logic inverted here.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md) —
  why the geoid is the limiting error term.
- [07-04-02 Height Systems and the Geoid](../../07-gravity-geodesy/04-geodesy-reference-frames/02-height-systems.md) —
  the reference surfaces that make a height a height.
- [15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md) —
  the circulation the geostrophic velocities describe.
- [12-06 Geodesy Constraints on the Interior](../../12-global-geophysics-interior/06-geodesy-constraints-interior/README.md) —
  the tides and their Love numbers, needed for the solid-Earth correction.
- [20 Signal Processing](../../20-signal-processing/README.md) — retracking as a
  model-fitting problem.
