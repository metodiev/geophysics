---
id: 17-03-01
title: "SAR Principles: Geometry, Polarisation, Backscatter"
level: graduate
prereqs: ["17-01-01", "17-01-04", "02-07-05"]
tags: [remote-sensing, radar, sar, backscatter, resolution, ambiguity]
---

# SAR Principles: Geometry, Polarisation, Backscatter

> All models and data in this module are **SYNTHETIC**. The carrier
> frequencies, orbit, antenna, noise figures and backscatter coefficients used
> here are teaching values, not the parameters of any real instrument, and no
> measured scene appears in this lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the slant-range resolution $\Delta r = c/(2B)$ and **convert** it
   to ground-range resolution for a stated incidence angle.
2. **Derive** why a synthetic aperture achieves an azimuth resolution
   $L/2$ that is independent of range, and **verify** it by matched-filtering a
   simulated azimuth chirp.
3. **Derive** the pulse-repetition-frequency window from the azimuth Doppler
   bandwidth and the swath-width constraint, and **identify** which ambiguity
   each bound prevents.
4. **Compute** a radar SNR budget from the radar equation, including the range
   and azimuth compression gains, and **state** the units of every factor.
5. **Explain** what $\sigma^{0}$ measures, why it depends on incidence angle and
   surface type, and **distinguish** the three canonical scattering mechanisms.
6. **Predict** the geometric distortions (foreshortening, layover, shadow) for a
   stated slope and incidence angle, and **explain** why layover destroys the
   invertibility of the geometry.

## Prerequisites

- [17-01-01 The Electromagnetic Spectrum and Sensing Windows](../01-remote-sensing-physics/01-em-spectrum-remote-sensing.md) —
  frequencies, wavelengths and atmospheric windows.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../01-remote-sensing-physics/04-resolution-concepts.md) —
  what "resolution" means for a remote sensing system.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../../02-physics/07-electromagnetism/05-em-waves.md) —
  wave propagation, polarisation states and the plane-wave picture.

## 1. What a radar image actually measures

An optical sensor measures reflected sunlight in a band. A radar measures its
own transmitted power returned to it. That difference produces three properties
that matter for every lesson in this module.

First, radar provides **its own illumination**, so it works at night and through
cloud. Second, it measures **range and amplitude**, not brightness: what is
recorded is the two-way travel time and the returned power of each echo. Third,
because the illumination is coherent, the echoes from many scatterers inside one
resolution cell add **as complex numbers**. That is the source of both the
strength of radar (phase is measurable, hence interferometry) and its most
annoying artefact (speckle, a multiplicative noise with no counterpart in
optical imagery).

The word *synthetic* in synthetic aperture radar refers to a single idea: a
small antenna moving along its track can be treated as a very long antenna, if
the echoes are recorded coherently and combined with the correct phase history.
Lesson [02](02-insar.md) exploits the same coherence for deformation
measurement; this lesson establishes the geometry and the budget.

## 2. Definitions and conventions

### 2.1 Geometry

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | slant range, distance from antenna to target | m |
| $\theta$ | local incidence angle, measured from vertical | rad |
| $\eta$ | look angle (from nadir to the slant range vector) | rad |
| $h$ | platform altitude above the reference surface | m |
| $v$ | platform speed along track | m/s |
| $L$ | antenna length in the azimuth (along-track) direction | m |
| $B$ | transmitted bandwidth | Hz |
| $\tau_p$ | transmitted pulse duration | s |

For a flat surface $\eta = \theta$; over topography the local incidence differs
from the look angle, and that difference is what produces the distortions of
Section 6.

### 2.2 Wavelength

The carrier sets everything: $\lambda = c/f$ with $c = 299\,792\,458\ \mathrm{m\,s^{-1}}$
exactly. The band designations in the demonstration are the conventional
letter names with their usual stated ranges; the carriers inside them are
teaching values. Four of them, computed by `code/sar_principles_demo.py`:

| band | stated range | teaching $f$ | $\lambda = c/f$ |
|---|---|---|---|
| P | 0.30–1.00 GHz | 0.50 GHz | 59.958 cm |
| L | 1.00–2.00 GHz | 1.25 GHz | 23.983 cm |
| C | 4.00–8.00 GHz | 5.30 GHz | 5.656 cm |
| X | 8.00–12.00 GHz | 9.60 GHz | 3.123 cm |

Longer wavelengths penetrate vegetation and dry soil further and decorrelate
less between repeat passes; shorter wavelengths give more bandwidth for a given
fractional bandwidth but decorrelate faster. All of that is used in
[06 Polarimetry](06-polarimetry.md) and [07 Altimetry](07-radar-altimetry.md).

### 2.3 Radar cross section and backscatter coefficient

The **radar cross section** $\sigma$ of a target is the equivalent area that
would scatter isotropically to produce the observed echo; it has units of
$\mathrm{m^{2}}$. For a distributed scene one reports the **backscatter
coefficient**

$$\sigma^{0} = \frac{\langle \sigma \rangle}{A_{\text{cell}}}
\qquad (\text{dimensionless, usually in dB}),$$

the cross section per unit illuminated ground area. $\sigma^{0}$ is not a
material constant: it depends on wavelength, incidence angle, polarisation,
surface roughness and the dielectric constant, and it is the quantity that
actually carries the geophysical information.

## 3. Derivations

### 3.1 Range resolution

A pulse of duration $\tau_p$ occupies a length $c\tau_p$ in space. Two targets
at slant ranges separated by $\Delta r$ are resolved when their echoes do not
overlap, i.e. when the round-trip path difference $2\Delta r$ exceeds $c\tau_p$:

$$\Delta r = \frac{c\,\tau_p}{2}.$$

A long pulse delivers more energy but resolves badly. Linear frequency
modulation resolves the contradiction: sweeping the carrier across a bandwidth
$B$ means the matched filter's time resolution is $1/B$ rather than $\tau_p$, so

$$
\boxed{\;\Delta r = \frac{c}{2B}\;}
$$

and the *energy* is still that of the long pulse. This is pulse compression, and
the gain in SNR is the time–bandwidth product $B\tau_p$ (Section 3.4).

The ground-range resolution follows from projecting the slant-range increment
onto the surface. On a locally flat surface, a change $\mathrm{d}r$ of slant
range corresponds to $\mathrm{d}g = \mathrm{d}r/\sin\theta$ of ground range, so

$$\Delta g = \frac{\Delta r}{\sin\theta} = \frac{c}{2B\sin\theta}.$$

*Numerical check (SYNTHETIC).* With $B = 30\ \mathrm{MHz}$,
$\Delta r = 299\,792\,458/(2\times 3\times 10^{7}) = 4.9965\ \mathrm{m}$. At
$\theta = 35^\circ$ this is $\Delta g = 4.9965/\sin 35^\circ = 8.71\ \mathrm{m}$
of ground range. The demonstration tabulates the same calculation for
$B = 10, 30, 100\ \mathrm{MHz}$ and $\theta = 23^\circ, 35^\circ, 45^\circ$;
at $100\ \mathrm{MHz}$ the slant resolution is $1.50\ \mathrm{m}$.

Note the geometry: the same slant-range resolution is *coarser* on the ground at
steep incidence and *finer* at grazing incidence, and it becomes infinite at
$\theta \to 0$. This is why radar resolution is not a single number.

### 3.2 Azimuth resolution: real aperture versus synthetic aperture

A real aperture of length $L$ has a beamwidth $\lambda/L$; at slant range $R$ the
illuminated azimuth patch is $\lambda R/L$, so the *real-aperture* azimuth
resolution is

$$\delta_{\text{real}} = \frac{\lambda R}{L}.$$

It degrades linearly with range — useless from orbit. With
$L = 10\ \mathrm{m}$, $\lambda = 5.656\ \mathrm{cm}$ and $R = 800\ \mathrm{km}$,
the demonstration prints $\delta_{\text{real}} = 4525.17\ \mathrm{m}$: a 4.5 km
azimuth smearing.

Now let the platform fly and record coherently. A point target at broadside is
illuminated for the time its beam covers it,

$$T_s = \frac{\lambda R}{L v},$$

during which the range to it changes quadratically,
$R(t) \approx R_0 + v^{2}t^{2}/(2R_0)$. The recorded phase is
$\phi(t) = -4\pi R(t)/\lambda$, so the signal is a **linear chirp** with rate

$$K_a = \frac{2v^{2}}{\lambda R_0} \qquad (\mathrm{Hz\,s^{-1}})$$

and bandwidth $B_d = K_a T_s = 2v/L$. Matched-filtering this chirp
compresses it to a pulse whose $-3\ \mathrm{dB}$ width in *platform position*
$v\,\delta t$ is

$$\delta_{\text{syn}} = v\,\frac{0.886}{B_d} = \frac{0.886\,v L}{2v}
= 0.443\,L \approx \frac{L}{2}.$$

The range $R$ has cancelled. That cancellation is the whole commercial and
scientific argument for SAR: **resolution is set by the antenna length, not by
the altitude.**

*Verification by measurement.* The demonstration builds the azimuth history
$\exp(-\mathrm{i}4\pi R(t)/\lambda)$ over the dwell, matched-filters it with the
ideal reference, and measures the half-power width:

| $L$ (m) | measured width (m) | $L/2$ (m) | measured $/(L/2)$ |
|---|---|---|---|
| 5.0 | 2.215 | 2.50 | 0.886 |
| 10.0 | 4.430 | 5.00 | 0.886 |
| 20.0 | 8.859 | 10.00 | 0.886 |

The ratio is constant at $0.886$ — the sinc mainlobe factor — and the width
halves when $L$ halves. With $L = 10\ \mathrm{m}$ the synthetic aperture is
$L_s = \lambda R/L = 4525\ \mathrm{m}$, i.e. 4.5 km of *synthetic* aperture.
A shorter antenna gives a *longer* synthetic aperture (a wider beam) and hence a
finer resolution, which is why SAR azimuth antennas are deliberately small.

### 3.3 The PRF window

The pulses must be emitted often enough to sample the azimuth chirp and rarely
enough that the echoes from one pulse have left the scene before the next.

- **Azimuth ambiguity:** sampling at rate $f_{\text{PRF}}$ aliases a Doppler
  bandwidth $B_d$ unless $f_{\text{PRF}} > B_d = 2v/L$. For
  $v = 7455.5\ \mathrm{m\,s^{-1}}$ (circular orbit at 800 km, from
  $v=\sqrt{GM/r}$ with $GM = 3.986\,004\,418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$)
  and $L = 10\ \mathrm{m}$, $B_d = 1491.1\ \mathrm{Hz}$.
- **Range ambiguity:** echoes from the previous pulse arrive superimposed unless
  the unambiguous window $c/(2 f_{\text{PRF}})$ exceeds the swath $W$, i.e.
  $f_{\text{PRF}} < c/(2W)$.

*Numerical check.* The demonstration prints, for each swath width, whether the
window is non-empty:

| swath $W$ | $B_d$ (Hz) | $c/(2W)$ (Hz) | verdict |
|---|---|---|---|
| 20 km | 1491.1 | 7494.8 | OK |
| 50 km | 1491.1 | 2997.9 | OK |
| 100 km | 1491.1 | 1499.0 | OK (margin 8 Hz) |
| 200 km | 1491.1 | 749.5 | CONFLICT |

At $f_{\text{PRF}} = 2000\ \mathrm{Hz}$ the unambiguous one-way range window is
$c/(2f_{\text{PRF}}) = 74.95\ \mathrm{km}$ and the number of pulses in the dwell
is 1214, comfortably above the required $B_d T_s = 905$.

The 100 km row is the honest lesson: the constraint is nearly tight, and a wider
swath at this antenna length is impossible without either multiple azimuth
channels or a different antenna. Every high-resolution wide-swath radar design
is a solution to *this* inequality.

### 3.4 SNR budget

The radar equation gives the peak received power from a target of cross section
$\sigma$:

$$P_r = \frac{P_t G^{2}\lambda^{2}\sigma}{(4\pi)^{3}R^{4}},$$

with $P_t$ the peak transmit power and $G$ the one-way antenna gain (linear).
The noise power in the receiver bandwidth is $N = k_B T_{\text{sys}} F B$, with
$k_B = 1.380\,649\times10^{-23}\ \mathrm{J\,K^{-1}}$ exactly.

*Numerical check (SYNTHETIC),* from the demonstration, with
$P_t = 5.0\ \mathrm{kW}$, $G = 35\ \mathrm{dB}$, $F = 3\ \mathrm{dB}$,
$T_{\text{sys}} = 290\ \mathrm{K}$, $\sigma = 1\ \mathrm{m^{2}}$,
$R = 800\ \mathrm{km}$:

| quantity | value | in dB |
|---|---|---|
| peak received power $P_r$ | $1.968\times10^{-19}\ \mathrm{W}$ | — |
| noise power $N$ | $2.397\times10^{-13}\ \mathrm{W}$ | — |
| single-pulse SNR | $8.212\times10^{-7}$ | $-60.9$ |
| range compression gain $B\tau_p$ | 1200.0 | $+30.8$ |
| azimuth compression gain $B_dT_s$ | 905.0 | $+29.6$ |
| compressed SNR | 0.892 | $-0.5$ |

A single pulse cannot see a $1\ \mathrm{m^{2}}$ target eight hundred kilometres
away; two matched filters, one in range and one in azimuth, bring it to the
detection threshold. Because $P_r \propto R^{-4}$, doubling the range costs
12 dB, and no amount of processing recovers it — the only remedies are more
power, more gain or less range.

### 3.5 What sets $\sigma^{0}$

Three mechanisms dominate, and the rest of this module depends on telling them
apart:

1. **Surface scattering.** Roughness comparable to the wavelength produces
   **Bragg** scattering from the component of the surface spectrum at the
   wavenumber $k_B = 2k\sin\theta = 4\pi\sin\theta/\lambda$. Its strength grows
   with the roughness amplitude and with the dielectric constant.
2. **Double-bounce.** A pair of reflecting facets (a corner, a building on the
   ground, a trunk and the soil) returns a strong echo with a characteristic
   phase relationship between the polarisation channels.
3. **Volume scattering.** Scattering from a random medium such as a canopy or
   dry snow randomises the polarisation and produces a strong cross-polarised
   return.

The polarisation channels HH, VV and HV are the standard notation (transmit,
receive). $HH$ and $VV$ are **co-polarised**; $HV$ is **cross-polarised** and is
a direct measure of depolarisation, hence of volume scattering. Surface
scattering generally gives $\sigma^{0}_{HH} < \sigma^{0}_{VV}$ because the
Fresnel reflection coefficient is larger for V polarisation at oblique
incidence; double bounce reverses the ordering. Turning these inequalities into
quantitative statements is the subject of [06 Polarimetry](06-polarimetry.md).

$\sigma^{0}$ also falls off with incidence angle over bare soil and rock, slowly
over a rough surface, and it can *increase* with incidence over a wet snowpack.
A radar image is therefore never interpretable as "reflectivity" without the
reference to geometry and surface type.

## 4. Worked example — an imaging budget from first principles

*All values SYNTHETIC.* Design a strip-map SAR with $f = 9.6\ \mathrm{GHz}$,
$h = 800\ \mathrm{km}$ (circular orbit), $R = 800\ \mathrm{km}$,
$\theta = 35^\circ$, $L = 10\ \mathrm{m}$, $B = 30\ \mathrm{MHz}$ and
$P_t = 5\ \mathrm{kW}$.

1. **Wavelength.** $\lambda = 2.99792458\times10^{8}/9.6\times10^{9}
   = 3.123\ \mathrm{cm}$.
2. **Slant-range resolution.** $\Delta r = c/(2B) = 299\,792\,458/(6\times10^{7})
   = 4.9965\ \mathrm{m}$.
3. **Ground-range resolution.** $\Delta g = \Delta r/\sin 35^\circ
   = 4.9965/0.5736 = 8.71\ \mathrm{m}$.
4. **Azimuth resolution.** $\delta = L/2 = 5.00\ \mathrm{m}$ (measured $-3$ dB
   width $4.43\ \mathrm{m}$).
5. **Platform speed.** $v = \sqrt{GM/(R_E + h)}$ with
   $R_E = 6371\ \mathrm{km}$: $r = 7171\ \mathrm{km}$,
   $v = \sqrt{3.986\,004\,418\times10^{14}/7.171\times10^{6}}
   = 7455.5\ \mathrm{m\,s^{-1}}$.
6. **Doppler bandwidth and dwell.** $B_d = 2v/L = 1491.1\ \mathrm{Hz}$;
   $T_s = \lambda R/(Lv) = 905.0/1491.1 = 0.6070\ \mathrm{s}$.
7. **PRF choice.** $f_{\text{PRF}} = 2000\ \mathrm{Hz}$ satisfies
   $1491.1 < f_{\text{PRF}} < c/(2W)$ for $W < 74.9\ \mathrm{km}$.
8. **Resolution cell area.** $A = 4.9965 \times 5.00 = 24.98\ \mathrm{m^{2}}$;
   a scene of $\sigma^{0}$ has $\sigma = 24.98\,\sigma^{0}$.

Interpretation: at X band this system images with about $5 \times 8.7\
\mathrm{m}$ pixels from 800 km. Every number above came from the constants of
Section 2 and the equations of Section 3, not from a catalogue.

## 5. Assumptions and regime of validity

1. **Straight-line propagation** at speed $c$ in vacuum; the ionosphere and
   troposphere add small extra delay, treated for the interferometric case in
   [04 Atmospheric and Orbital Error Correction](04-insar-atmospheric-correction.md).
2. **Flat local surface** for the ground-range projection and for $\eta=\theta$.
   Slopes change both, which is Section 6.
3. **Negligible Earth curvature and rotation** within one synthetic aperture.
   Over a 4.5 km aperture the curvature correction is second order; over a very
   long integration it is not.
4. **Additive, white, Gaussian receiver noise** at temperature $T_{\text{sys}}$.
   Speckle is *not* this noise: it is multiplicative, deterministic given the
   scene, and it is treated in the exercises.
5. **Single dominant scattering mechanism per resolution cell** when
   interpreting $\sigma^{0}$. Mixtures are the norm and are handled by
   polarimetric decomposition in [06](06-polarimetry.md).
6. **The radar equation uses the peak power and a rectangular antenna pattern.**
   Real antennas have tapering and sidelobes that trade resolution for
   suppression; the 0.886 factor in Section 3.2 changes accordingly.

## 6. Geometry: foreshortening, layover, shadow

Let a planar facet dip toward the sensor by angle $\alpha$ (a flank rising away
from the radar). Put the radar at $(0,h)$ and the reference ground point at
$x = h\tan\theta$; the facet is $z = s\tan\alpha$ with $s = x - x_{\text{ref}}$.
The slant range is $r = \sqrt{x^{2} + (h-z)^{2}}$, so

$$\frac{\mathrm{d}r}{\mathrm{d}s}
= \frac{x - (h-z)\tan\alpha}{r}.$$

- **Foreshortening** is always present: the ground-to-slant mapping scales with
  $\cos\theta\,(\tan\theta-\tan\alpha)$, so a facing slope is compressed by
  $\sin(\theta-\alpha)/\sin\theta$.
- **Layover** begins when $\mathrm{d}r/\mathrm{d}s$ changes sign, i.e. at
  $\tan\alpha = \tan\theta$, that is $\alpha = \theta$. Equivalently, the local
  incidence $\theta-\alpha$ passes through zero and the facet becomes
  perpendicular to the beam.
- **Shadow** appears on the opposite orientation, where the local incidence is
  $\theta+\alpha$; it requires $\theta+\alpha > 90^\circ$, i.e.
  $\alpha > 90^\circ-\theta$.

The demonstration both *states* these thresholds and *measures* them from the
exact spherical geometry by scanning $\alpha$:

| $\theta$ | layover for $\alpha >$ | measured onset | shadow for $\alpha >$ | measured onset |
|---|---|---|---|---|
| $23^\circ$ | $23^\circ$ | $23.0^\circ$ | $67^\circ$ | $67.0^\circ$ |
| $35^\circ$ | $35^\circ$ | $35.0^\circ$ | $55^\circ$ | $55.0^\circ$ |
| $45^\circ$ | $45^\circ$ | $45.0^\circ$ | $45^\circ$ | $45.0^\circ$ |

The two thresholds are complementary, and they trade against each other:
increasing $\theta$ makes layover *easier* (a shallower facing slope folds) and
shadow *harder*. Between the thresholds the facet is strongly foreshortened but
the mapping is still invertible. Past the layover threshold the far end of the
facet is imaged before the near end, the ground-range-to-slant-range map is no
longer monotonic, and no purely geometric inversion can recover the slope. That
is why steep-terrain InSAR uses ascending and descending geometries and masks
layover rather than attempting to invert it
([05 InSAR Applications](05-insar-applications.md)).

## 7. Python demonstration

`code/sar_principles_demo.py` prints all of the above, in units:

1. $\lambda = c/f$ for six conventional bands with teaching carriers;
2. the slant- and ground-range resolution grid;
3. real versus synthetic aperture, with the $-3$ dB width **measured** by a
   matched-filter sum over the dwell;
4. the PRF window table with the verdict per swath width;
5. the SNR budget with both compression gains;
6. the layover and shadow thresholds.

```bash
cd 17-remote-sensing-gis/03-radar-remote-sensing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sar_principles_demo.py
```

## 8. Exercises

Worked problem sets are in
[`exercises/01-sar-principles-exercises.md`](./exercises/01-sar-principles-exercises.md)
with solutions in
[`exercises/01-sar-principles-solutions.md`](./exercises/01-sar-principles-solutions.md).

## Mastery checkpoint

Without notes: **(a)** a radar at $f = 5.3\ \mathrm{GHz}$ with
$B = 60\ \mathrm{MHz}$ images at $\theta = 30^\circ$; give the slant- and
ground-range resolution. **(b)** With $L = 4\ \mathrm{m}$ and $R = 700\
\mathrm{km}$, compute the real-aperture and synthetic azimuth resolutions and
explain which one depends on range. **(c)** State the two PRF inequalities and
compute the permitted window for $v = 7500\ \mathrm{m\,s^{-1}}$,
$W = 60\ \mathrm{km}$, $L = 4\ \mathrm{m}$. **(d)** A slope facing the radar
dips at $50^\circ$ at $\theta = 35^\circ$: is it foreshortened, in layover, or
in shadow?

A worked version of (a)–(c) is in the lesson-01
[solutions](./exercises/01-sar-principles-solutions.md).

## Common pitfalls

1. **Quoting one resolution number.** Range and azimuth resolutions are set by
   different things (bandwidth and antenna length) and the ground projection
   depends on the incidence angle.
2. **Believing a finer resolution needs a bigger antenna.** Azimuth resolution
   improves as the antenna gets *shorter*, until the PRF window closes.
3. **Confusing speckle with noise.** Speckle is a deterministic consequence of
   coherent summing; averaging it costs resolution, and no filter recovers
   what the geometry never measured.
4. **Treating $\sigma^{0}$ as a material constant.** An unknown incidence angle
   makes a calibrated image uninterpretable.
5. **Ignoring that $P_r \propto R^{-4}$.** The range dependence is not a
   processing problem; it is the budget.
6. **Applying the flat-surface ground-range formula over steep terrain.** That
   is precisely where layover lives.

## Related modules

- [02 InSAR: Interferometric Phase and Deformation Measurement](02-insar.md) —
  what the *phase* of the echo adds.
- [06 SAR Polarimetry and Polarimetric Decomposition](06-polarimetry.md) —
  the three scattering mechanisms as measurable quantities.
- [07 Radar Altimetry and Sea/Ice Surface Height](07-radar-altimetry.md) —
  the nadir-looking limiting case of this geometry.
- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) —
  the radiometric framing shared with optical sensing.
- [17-04 Satellite Geodesy Techniques](../04-satellite-geodesy-techniques/README.md) —
  the measurement geometry from the other side: satellites as the observing
  instrument rather than the observing platform.
- [20 Signal Processing](../../20-signal-processing/README.md) — matched
  filtering, the chirp transform and the sampling theorems used here.
