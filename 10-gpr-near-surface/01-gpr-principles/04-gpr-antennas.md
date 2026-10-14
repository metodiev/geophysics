---
id: 10-01-04
title: "Antennas: Frequency, Shielding, Polarisation and Offsets"
level: graduate
prereqs: ["10-01-01", "10-01-02", "02-07-05"]
tags: [gpr, near-surface, gpr-principles, antennas, polarisation, ground-coupling, offsets]
---

# Antennas: Frequency, Shielding, Polarisation and Offsets

> **All models and data in this module are SYNTHETIC.** The antenna below is the
> idealised infinitesimal (Hertzian) dipole — the standard far-field model of a
> linearly polarised antenna — and the permittivities are chosen teaching values.
> No instrument model, measured radiation pattern or field site is involved.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the half-wave resonance condition $L = \lambda/2$ and **compute**
   the dipole length in air and in a coupled medium of stated permittivity.
2. **Explain** why a ground-coupled antenna's effective centre frequency depends
   on the medium, and **state** the two idealised limits that bracket a real
   antenna.
3. **Derive** the ideal dipole power pattern $\sin^{2}\theta$ and **compute** the
   fraction of radiated power inside a cone of given half-angle.
4. **Apply** Snell's law at the ground surface to obtain the critical angle
   $\theta_c = \arcsin(1/\sqrt{\varepsilon_r})$ and the footprint radius
   $d/\sqrt{\varepsilon_r-1}$.
5. **Compute** the polarisation coupling $|\cos\psi|$ between a linear dipole and
   a linear target, and **state** what a crossed-polarisation survey can and
   cannot detect.
6. **Derive** the near-surface blind zone $d_{\min} = x/2$ imposed by the
   antenna separation, and **explain** why it is independent of frequency.
7. **Quantify** the travel-time penalty of an offset for a shallow target and the
   depth bias it causes if ignored.

## Prerequisites

- [01 GPR Physics](01-gpr-physics.md) — wavelength, permittivity and speed.
- [02 Velocity Estimation and Depth Conversion in GPR](02-gpr-velocity-and-depth.md) —
  the offset geometry $t = \sqrt{4d^{2}+x^{2}}/v$.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../../02-physics/07-electromagnetism/05-em-waves.md) —
  the radiation field of an oscillating dipole.

## 1. Antenna length and the medium it sits in

A thin linear dipole radiates efficiently near resonance, where its physical
length is close to half the wavelength **in the medium it is coupled to**:

$$L_{1/2} = \frac{\lambda}{2} = \frac{v}{2f} = \frac{c}{2f\sqrt{\varepsilon_r}}.
\tag{1.1}$$

The consequences are large and are often read off the wrong wavelength. In the
demonstration, for a $200\ \mathrm{MHz}$ design:

| $f$ (MHz) | $\lambda_{\mathrm{air}}$ (m) | $L/2$ in air (m) | $L/2$ in $\varepsilon_r=9$ (m) | $L/2$ in $\varepsilon_r=16$ (m) |
|---|---|---|---|---|
| 100 | 2.998 | 1.499 | 0.500 | 0.375 |
| 250 | 1.199 | 0.600 | 0.200 | 0.150 |
| 500 | 0.600 | 0.300 | 0.100 | 0.075 |
| 900 | 0.333 | 0.167 | 0.056 | 0.042 |

Turned around: one and the same $0.150\ \mathrm{m}$ dipole resonates at
$999.3\ \mathrm{MHz}$ in air and at $333.1\ \mathrm{MHz}$, $249.8\ \mathrm{MHz}$
and $199.9\ \mathrm{MHz}$ when coupled to media with $\varepsilon_r$ of $9$,
$16$ and $25$. The "antenna frequency" printed on the box is therefore a
statement about the antenna **and** about the medium — and, for a commercial
ground-coupled antenna, about the loading and shielding that the manufacturer
chose. The two idealised limits (radiating into air; radiating into a medium of
permittivity $\varepsilon_r$) bracket the real behaviour; a real antenna lies
between them, and the only way to know where is to measure its spectrum in place.

This also explains a practical rule that is frequently mis-stated: to move to a
lower frequency you must physically enlarge the antenna, because
$L \propto 1/f$ at fixed medium. Increasing the recorded time window does not
change the radiated band.

## 2. The radiation pattern of a dipole

For an infinitesimal current element the far-field power pattern is

$$P(\theta) \propto \sin^{2}\theta, \tag{2.1}$$

with $\theta$ measured from the dipole axis. Three numbers follow and are
measured in the demonstration:

- the half-power points are where $\sin^{2}\theta = 1/2$, i.e. $\theta = 45^\circ$;
  the 3 dB beam width in the plane of the axis is therefore $90^\circ$;
- the pattern is a **torus**, omnidirectional about the axis — a dipole gives no
  azimuthal discrimination at all;
- the fraction of radiated power inside a cone of half-angle $\theta$ is

$$F(\theta) = \frac{3}{4}\left(\frac{\cos^{3}\theta}{3} - \cos\theta +
\frac{2}{3}\right). \tag{2.2}$$

Equation (2.2) is normalised so that $F(\pi/2) = 1/2$: half the power goes into
each hemisphere. The demonstration verifies the closed form against a fine
numerical quadrature (agreement to $1\times10^{-7}$) and prints:

| $\theta$ (deg) | 15 | 30 | 45 | 60 | 90 |
|---|---|---|---|---|---|
| $F(\theta)$ | 0.00086 | 0.01286 | 0.05806 | 0.15625 | 0.50000 |

Only $5.81\%$ of the power lies inside a $\pm45^\circ$ cone. This is the number to
remember when someone claims an antenna "focuses" energy into the ground: a
dipole does not, and the wide illuminated footprint that follows from it is
treated in Section 3.

## 3. Ground coupling: critical angle and footprint

Snell's law at the ground surface, with air of index $1$ and ground of index
$\sqrt{\varepsilon_r}$, reads

$$\sin\theta_{\mathrm{air}} = \sqrt{\varepsilon_r}\,\sin\theta_{\mathrm{g}},
\tag{3.1}$$

with both angles measured from the vertical. The largest angle a ray can have in
the ground is reached when the air ray is horizontal:

$$\theta_c = \arcsin\!\left(\frac{1}{\sqrt{\varepsilon_r}}\right), \tag{3.2}$$

the **critical angle**. Rays inside the ground steeper than $\theta_c$ cannot
escape through the surface: they are totally internally reflected. That is why a
waveguide-like layer bounds them and why a broad antenna footprint is not
radiated away into the sky.

**Worked example 1.**

| $\varepsilon_r$ | 4 | 9 | 16 | 25 |
|---|---|---|---|---|
| $\theta_c$ (deg) | 30.000 | 19.471 | 14.478 | 11.537 |
| footprint radius at 1 m (m) | 0.577 | 0.354 | 0.258 | 0.204 |
| at 2 m (m) | 1.155 | 0.707 | 0.516 | 0.408 |
| at 3 m (m) | 1.732 | 1.061 | 0.775 | 0.612 |

The footprint radius is $d\tan\theta_c = d/\sqrt{\varepsilon_r-1}$, so at
$\varepsilon_r = 9$ the illuminated radius is $0.354d$: at $2\ \mathrm{m}$ depth
the surface footprint has a radius of $0.707\ \mathrm{m}$. Two facts follow.
First, the illuminated zone is much larger than the antenna, which is why GPR
targets are detected before they are resolved. Second, a single reading of a
buried interface averages over that footprint, so a "point" measurement is
nothing of the kind.

## 4. Polarisation

A linear dipole couples to the component of the target response along its axis,
so the received amplitude carries a factor

$$a(\psi) = |\cos\psi| \quad\Longrightarrow\quad
\text{power} \propto \cos^{2}\psi, \tag{4.1}$$

where $\psi$ is the angle between the dipole axis and the target's polarisation.
The demonstration prints $a = 1.0000$ at $\psi=0^\circ$, $0.9659$ at $15^\circ$,
$0.8660$ at $30^\circ$, $0.7071$ at $45^\circ$ ($-3.01\ \mathrm{dB}$), $0.5000$
at $60^\circ$ ($-6.02\ \mathrm{dB}$), $0.2588$ at $75^\circ$ and a null at
$90^\circ$.

**The sign is not recoverable.** A target at $+45^\circ$ and one at $-45^\circ$
give the same amplitude. Determining a target's strike therefore requires
repeating the line with the antennas rotated (a common practice is to run each
line twice with the dipoles crossed), and even then a linear target at $\psi$ and
one at $180^\circ-\psi$ remain indistinguishable from amplitude alone.

There is a second trap. In the *ideal* isotropic, horizontally layered Earth the
transverse-polarised response is a null, so crossed dipoles should see nothing.
Real records contain transverse energy from buried linear targets, anisotropic
fabrics, dipping interfaces and from the antennas' own imperfections — and
telling these apart from noise needs the multi-offset or multi-azimuth
acquisition of
[02-01 Survey Design](../02-gpr-acquisition-and-processing/01-gpr-survey-design.md).

## 5. Offset, and the near-surface blind zone

With antennas separated by $x$ the first arrival is the air wave, at
$t_{\mathrm{air}} = x/c$; the second is the ground wave, at
$t_{\mathrm{ground}} = x/v_1$. A reflection from depth $d$ at two-way time
$2d/v$ is separable only if it arrives after the ground wave, which for a
ground-coupled antenna ($v_1 = v$) requires

$$\frac{2d}{v} > \frac{x}{v} \qquad\Longrightarrow\qquad
\boxed{\;d_{\min} = \frac{x}{2}\;} \tag{5.1}$$

independent of frequency and of permittivity. The demonstration's table, for
$v_1 = 0.09993\ \mathrm{m\,ns^{-1}}$:

| $x$ (m) | $t_{\mathrm{air}}$ (ns) | $t_{\mathrm{ground}}$ (ns) | $d_{\min}$ (m) |
|---|---|---|---|
| 0.10 | 0.334 | 1.001 | 0.050 |
| 0.20 | 0.667 | 2.001 | 0.100 |
| 0.30 | 1.001 | 3.002 | 0.150 |
| 0.50 | 1.668 | 5.004 | 0.250 |
| 1.00 | 3.336 | 10.007 | 0.500 |

Two consequences, both frequently missed:

- The near surface is recovered by **reducing the separation**, not by raising the
  frequency. A $1\ \mathrm{m}$ separation leaves the top $50\ \mathrm{cm}$
  inseparable, whatever the bandwidth.
- Because the blind zone is set by a *time* comparison, higher-frequency systems
  (shorter pulses) recover less of it than intuition suggests: the ground wave
  arrival time does not change.

### 5.1 Shielding: what it removes and what it cannot

A shielded antenna surrounds the dipole with a conducting enclosure that is open
on the ground side. Its purpose is to suppress the **direct air-path coupling**
between transmitter and receiver — the energy that travels through the air
between the two antennas without ever entering the ground — which otherwise
arrives at $t = x/c$ and rings on for several cycles, masking everything in the
first part of the record.

Three limits follow directly from the geometry above and are worth stating
because they are often assumed away:

- Shielding cannot remove the **air wave** itself. The arrival at $t=x/c$ is the
  wave that travelled through the air *outside* the shields, and the numbers in
  the table above apply whether the antennas are shielded or not. What shielding
  reduces is the direct coupling amplitude, not the arrival time.
- Shielding cannot remove the **ground wave** at $t = x/v_1$, which propagates in
  the medium the survey is trying to measure. The blind zone $d_{\min} = x/2$ is
  a ground-wave constraint, so it is set by the separation and not by the
  shielding.
- Shielding changes the **radiated pattern and the effective bandwidth**. An
  enclosure is a conducting boundary close to the antenna, and it loads the
  antenna electrically; the centre frequency and the band of a shielded antenna
  therefore differ from those of the same dipole unshielded, in a way that depends
  on the enclosure and the ground. That is a measurement to be made in place, not
  a number to be assumed from the model of Section 1.

The practical summary: shielding buys a cleaner **early-time** record (less direct
ringing), and therefore better detection of shallow events that are otherwise
buried in it; it does not change the geometry of the blind zone, and it does not
make the antenna narrower in angle.

## 6. The travel-time penalty of an offset

Offsets are not free even for targets well below the blind zone. From
$t(x) = \sqrt{4d^{2}+x^{2}}/v$ and $t_0 = 2d/v$,

$$\Delta t = t(x) - t_0 \approx \frac{x^{2}}{4\,d\,v}
\quad \text{for } x \ll d, \tag{6.1}$$

so the penalty falls as $1/d$. The demonstration's SYNTHETIC values at
$v = 0.09993\ \mathrm{m\,ns^{-1}}$:

| $d$ (m) | $x$ (m) | $t(x)$ (ns) | $t_0$ (ns) | $\Delta t$ (ns) | depth bias if ignored (cm) |
|---|---|---|---|---|---|
| 0.30 | 0.10 | 6.087 | 6.004 | 0.083 | 0.41 |
| 0.30 | 0.30 | 6.713 | 6.004 | 0.709 | 3.54 |
| 0.50 | 0.30 | 10.448 | 10.007 | 0.441 | 2.20 |
| 1.00 | 0.30 | 20.238 | 20.014 | 0.224 | 1.12 |

At a target depth comparable with the separation, ignoring the offset biases the
depth by centimetres — the same order as the resolution of the survey. The
correction must be applied, not assumed to be negligible.

## 7. Assumptions and regime of validity

1. **Infinitesimal dipole in the far field.** Real GPR antennas are
   finite-length, resistively loaded, shielded and placed on or near the ground.
   The pattern and the resonance are idealisations; the numbers above are
   *predictions of the model*, not specifications of any instrument.
2. **Half-space geometry** for (3.1)–(3.2). A layered medium refracts the
   footprint further and changes $\theta_c$ with depth.
3. **Single, linearly polarised dipole.** Arrays, circular polarisation and
   crossed pairs have different (and generally weaker but azimuth-sensitive)
   responses.
4. **No mutual coupling between transmitting and receiving antennas.** At
   separations of a fraction of a wavelength this is optimistic, and the
   coupling is what shielding is designed to suppress.
5. **Lossless medium** for the pattern. Attenuation makes the effective pattern
   frequency- and depth-dependent.
6. **Straight-ray geometry** for (5.1) and (6.1). The equations are the geometric
   limit; near-field and interface-wave arrivals contaminate the earliest times.

## 8. Python demonstration

`code/gpr_antennas_demo.py` prints everything above:

1. half-wave lengths in air and in two media, plus the resonance frequency of a
   fixed $0.150\ \mathrm{m}$ dipole in five media;
2. the dipole beam width, the power fraction inside a cone (closed form checked
   against numerical quadrature), and the hemisphere normalisation;
3. critical angles and footprint radii;
4. the polarisation coupling and its $3\ \mathrm{dB}$ and null directions;
5. the offset-imposed blind zone $d_{\min} = x/2$;
6. the travel-time penalty and depth bias of a finite offset;
7. a verification section comparing the closed-form power fraction with
   quadrature, point by point.

## Mastery checkpoint

Without notes:

> A survey uses ground-coupled antennas separated by $0.40\ \mathrm{m}$ over
> ground with $\varepsilon_r = 9$ and $v = 0.09993\ \mathrm{m\,ns^{-1}}$.
> **(a)** Compute the half-wave dipole length for $200\ \mathrm{MHz}$ in this
> medium. **(b)** Compute the critical angle and the footprint radius at
> $1.5\ \mathrm{m}$. **(c)** State the shallowest depth that a reflection can be
> separated from the ground wave. **(d)** Compute the two-way time of a reflector
> at $0.60\ \mathrm{m}$ at zero offset and at $x = 0.40\ \mathrm{m}$, and the
> depth error if the offset is ignored. **(e)** A linear target is observed with
> $70\%$ of the amplitude of the same target at $0^\circ$; find the two possible
> angles and state what additional measurement would distinguish them.

Parts (a)–(e) are worked in
[`exercises/04-gpr-antennas-solutions.md`](./exercises/04-gpr-antennas-solutions.md).

## Common pitfalls

1. **Reading the antenna length off the air wavelength** and then burying it in
   wet ground.
2. **Assuming an "antenna frequency" is a bandwidth.** The spectrum, not the
   label, sets both penetration and resolution.
3. **Expecting a dipole to focus energy downward.** Two-thirds of the power goes
   sideways in the axial plane; half goes into the upper hemisphere.
4. **Confusing the critical angle with a limit on the footprint.** The critical
   angle sets the *largest* lateral offset reachable at a depth; the footprint is
   wide, not narrow.
5. **Trying to recover the near surface with a fixed large offset.** Change the
   separation, not the frequency.
6. **Using a $1/(4dv)$ moveout estimate at $x \sim d$.** The approximation, not
   the geometry, is what fails.
7. **Treating crossed-polarisation data as a diagnostic of anisotropy** before
   checking the survey geometry.

## Related modules

- [01 GPR Physics](01-gpr-physics.md).
- [03 Attenuation, Penetration Depth and Frequency Trade-Offs](03-gpr-attenuation-penetration.md) —
  the frequency choice this lesson's medium dependence complicates.
- [05 Vertical and Horizontal Resolution Limits](05-gpr-resolution.md) — what the
  footprint does to resolution.
- [02-01 Survey Design: Profile, Grid, CMP and Transillumination](../02-gpr-acquisition-and-processing/01-gpr-survey-design.md) —
  how separation, frequency and grid are chosen together.
- [23-05 Instrumentation and Electronics for Geophysics](../../23-field-methods-instruments/05-instrumentation-and-electronics/README.md) —
  the hardware that the idealisations here abstract away.

Materials: [`code/gpr_antennas_demo.py`](./code/gpr_antennas_demo.py),
[`exercises/04-gpr-antennas-exercises.md`](./exercises/04-gpr-antennas-exercises.md),
[`exercises/04-gpr-antennas-solutions.md`](./exercises/04-gpr-antennas-solutions.md).
