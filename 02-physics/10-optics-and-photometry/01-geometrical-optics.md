---
id: 02-10-01
title: "Geometrical Optics, Refraction and Lenses"
level: intermediate
prereqs: ["02-03-08", "01-05-02", "02-01-01"]
estimated_minutes: 90
tags: [optics, refraction, snell, total-internal-reflection, lenses, fibre]
---

# Geometrical Optics, Refraction and Lenses

Every optical instrument in geophysics — a satellite radiometer, a borehole
camera, a laser strainmeter, a distributed acoustic sensing (DAS) interrogator —
is built out of interfaces and lenses. Geometrical optics is the bookkeeping for
those two elements: what happens to a ray at an interface, and what happens to a
set of rays at a lens. It is the only branch of optics that is *entirely*
geometry, and it is valid whenever the wavelength is small compared with every
aperture and every feature the light meets.

The three results this lesson computes, and their geophysical identities:

| Result | Statement | Where it is the whole story |
|---|---|---|
| Snell's law | $n_1\sin\theta_1 = n_2\sin\theta_2$ | Where a ray goes at water, rock, glass or cladding |
| Total internal reflection | Beyond $\theta_c=\arcsin(n_2/n_1)$, nothing transmits | **Optical fibre guidance** — the basis of DAS |
| Thin-lens equation | $1/f = 1/s + 1/s'$ | Every camera, telescope and spectrometer design |

The second row is the one this module keeps returning to. A step-index optical
fibre has an index step of 0.4 per cent and *no mirror anywhere*: light is
confined by the geometry of total internal reflection alone. Every distributed
acoustic sensing measurement in geophysics — a fibre in a borehole, a fibre
cemented behind casing, a submarine telecom cable repurposed as a seismic array —
is a consequence of the critical angle.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** Snell's law from Fermat's principle of least time, and state
   precisely what the refractive index is a property of.
2. **Compute** the refracted angle, the critical angle and the Fresnel
   reflectance for an interface, and explain the Brewster angle.
3. **Derive** the numerical aperture and acceptance angle of a step-index
   fibre, and compute the V number, the mode count and the single-mode cutoff
   wavelength.
4. **Apply** the thin-lens equation to a camera, a telescope and a spectrometer,
   and compute the focus travel and the image scale.
5. **Compute** apparent depth, the lateral displacement of a ray through a
   window, and the angular compression of a hemisphere entering water.
6. **State** the validity condition of geometrical optics, $\lambda/a \ll 1$,
   and quantify where it fails for a fibre core.
7. **Explain** why the ray picture gives the correct acceptance cone of a fibre
   but cannot predict how many modes it supports.

## Prerequisites

- [02-03-08 Reflection, Refraction and Snell's Law for Waves](../03-oscillations-and-waves/08-reflection-refraction.md)
  — Snell's law for elastic and electromagnetic waves, from which the optical
  case follows with $v = c/n$.
- [01-05-02 Derivatives and Rates of Change](../../01-mathematics/05-single-variable-calculus/02-derivatives.md)
  — the differentiation used to derive Fermat's principle into Snell's law.
- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../01-measurement-and-physical-reasoning/01-physical-quantities.md)
  — the unit discipline; angles in radians throughout.

## 1. The refractive index, and what it is not

The refractive index of a medium is defined by the ratio

$$n \equiv \frac{c}{v} , \tag{1}$$

with $c = 299\,792\,458$ m s⁻¹ exactly (a defined constant) and $v$ the *phase
velocity* of a monochromatic wave in the medium. Three things follow immediately
and are worth stating because each is routinely got wrong:

- **$n$ is not the speed of the photons.** It is the ratio of the vacuum phase
  velocity to the phase velocity of the wave in the medium. Inside a dielectric
  the field is the superposition of the incident wave and the coherent forward
  radiation of the induced dipoles; the *net* wave is delayed, and no single
  photon is slowed.
- **$n$ depends on wavelength.** This is dispersion, and it is why a prism works
  and why an image has chromatic aberration. Any value of $n$ is stated at a
  wavelength; §3 shows a computed case.
- **$n$ depends on the medium's state.** Temperature, pressure, composition and,
  for rock, porosity and saturation all change it. Air at 15 °C and 101.325 kPa
  has $n = 1.000293$ (nominal, visible); the same air at 0 °C has a value larger
  in the fourth decimal. That small difference is astronomical refraction.

| Medium | $n$ (nominal) | Wavelength | Note |
|---|---|---|---|
| Vacuum | 1 | by definition | $c$ is defined here |
| Air, 15 °C, 101.325 kPa | 1.000293 | visible | sets astronomical refraction |
| Water | 1.333 | ~589 nm, 20 °C | ~4/3, the classical value |
| Soda-lime glass | ~1.52 | ~589 nm | windows, lenses |
| Fused silica | 1.4447 | 1550 nm | fibre cladding |
| GeO₂-doped silica | 1.4504 | 1550 nm | fibre core |

Nominal values for the stated wavelength and conditions: an index without its
wavelength is not a number, it is a rumour.

## 2. Snell's law from Fermat's principle

### 2.1 The derivation

Fermat's principle: a ray travelling between two points follows the path of
stationary optical path length

$$S = \int n\, \mathrm{d}l . \tag{2}$$

Take two media meeting at a plane $z = 0$, with a point $A$ at height $h_1$ in
medium 1 and a point $B$ at depth $h_2$ in medium 2, separated horizontally by
$L$. Let the ray cross the interface at horizontal coordinate $x$. Then

$$S(x) = n_1\sqrt{h_1^2 + x^2} + n_2\sqrt{h_2^2 + (L-x)^2} . \tag{3}$$

Stationarity, $\mathrm{d}S/\mathrm{d}x = 0$, gives

$$\frac{n_1 x}{\sqrt{h_1^2+x^2}} = \frac{n_2 (L-x)}{\sqrt{h_2^2+(L-x)^2}} , \tag{4}$$

and the two fractions are exactly $\sin\theta_1$ and $\sin\theta_2$, with the
angles measured from the interface normal. Hence

$$\boxed{\ n_1\sin\theta_1 = n_2\sin\theta_2\ } \tag{5}$$

**Snell's law is not an independent law of nature.** It is the
stationarity condition of the optical path, which in turn is the short-wavelength
limit of the wave equation — the same limit that gives seismic ray theory in
[02-03-08](../03-oscillations-and-waves/08-reflection-refraction.md). Snell's law
for light, for P waves and for radar is one equation; only the expression for $n$
differs.

### 2.2 What the geometry does

Because $n$ is fixed by the medium, (5) is a statement about angles. The table
below is the actual output of
[`code/geometrical_optics_demo.py`](./code/geometrical_optics_demo.py) section 1,
for an air-to-water interface with $n_{\text{air}} = 1.000293$ and
$n_{\text{water}} = 1.333$:

```text
 theta_1 (deg) theta_2 (deg)       R_s       R_p   R_unpol  transmitted
          0.00      0.000000   0.02033   0.02033   0.02033      0.97967
         15.00     11.199145   0.02254   0.01823   0.02039      0.97961
         30.00     22.036902   0.03088   0.01191   0.02139      0.97861
         45.00     32.047229   0.05290   0.00280   0.02785      0.97215
         60.00     40.531939   0.11492   0.00432   0.05962      0.94038
         75.00     46.455360   0.31378   0.11073   0.21225      0.78775
         85.00     48.378752   0.67358   0.49326   0.58342      0.41658
         89.00     48.615770   0.92381   0.86868   0.89625      0.10375
```

Three consequences, each of which matters downstream:

- **The compression is non-linear.** 60° of incidence becomes 40.53° in the
  water; 85° becomes 48.38°. The whole incident hemisphere is squeezed into a
  cone of half-angle 48.6257° inside the water. A diver looking up sees the
  entire sky in a cone of $2\times48.6257 = 97.25°$: the *Snell window*. The same
  geometry governs what a satellite sees through a water surface and why
  measuring water-leaving radiance requires viewing away from the glint.
- **Reflectance rises steeply near grazing incidence.** At normal incidence only
  2.03 per cent of the light is reflected; at 85° it is 58.3 per cent. Surface
  glint is a grazing-incidence phenomenon.
- **Polarisation splits.** $R_s$ and $R_p$ (the Fresnel coefficients for the two
  polarisations) diverge with angle, and $R_p$ passes through zero at the
  **Brewster angle** $\theta_B = \arctan(n_2/n_1)$, computed by the demo as
  53.115° for air into water, where $R_s = 0.0781$ and $R_p = 0$ (numerically
  $4.8\times10^{-33}$). Reflected light at that angle is fully s-polarised, which
  is why a polarising filter suppresses water glint: the glint has a
  polarisation the transmitted signal does not.

### 2.3 Fresnel reflectance at normal incidence

At normal incidence the intensity reflectance of a single interface is

$$R = \left(\frac{n_1-n_2}{n_1+n_2}\right)^2 . \tag{6}$$

For air into water the demo computes $R = 0.02033$; for air into glass with
$n = 1.52$, $R = 0.0426$. That 4.26 per cent matters twice per surface, which is
why an uncoated lens of six elements loses about 40 per cent of the light to
reflections, and why the antireflection coating of lesson
[02-10-02](./02-interference-diffraction-optics.md) exists. Equation (6) is the
normal-incidence limit of the Fresnel equations, which are derived in any optics
text; the full angular forms are what the demo tabulates.

## 3. Total internal reflection and the critical angle

### 3.1 The critical angle

Snell's law (5) can be solved for $\theta_2$:

$$\sin\theta_2 = \frac{n_1}{n_2}\sin\theta_1 . \tag{7}$$

If $n_1 > n_2$ the right-hand side reaches 1 at

$$\boxed{\ \theta_c = \arcsin\!\left(\frac{n_2}{n_1}\right)\ } \tag{8}$$

and for $\theta_1 > \theta_c$ no real $\theta_2$ exists: all the light is
reflected. Because the evanescent field still penetrates a fraction of a
wavelength into the second medium, total internal reflection is not
"instantaneous" reflection at a mathematical plane, but for every purpose in this
module it is.

```text
interface                         n1      n2   theta_c (deg)
water -> air                  1.3330  1.0003        48.62568
glass -> air                  1.5200  1.0003        41.15418
silica fibre core -> clad     1.4504  1.4447        84.91872
```

Read the third row. The fibre's critical angle is 84.92° *from the normal to the
core-cladding interface*, which corresponds to a ray at **5.0813° to the fibre
axis**. Any ray steeper than that leaks out. A 0.4 per cent index step confines
light within a 5° cone, and that is the entire mechanism of light guidance in an
optical fibre.

### 3.2 The step-index fibre: numerical aperture and V number

A step-index fibre has a core of index $n_1$ and radius $a$ inside a cladding of
index $n_2$. The largest ray angle to the axis that is guided follows from the
critical angle:

$$\cos\theta_{\max} = \frac{n_2}{n_1}
\quad\Longrightarrow\quad
\sin\theta_{\max} = \frac{\sqrt{n_1^2-n_2^2}}{n_1} . \tag{9}$$

The **numerical aperture** is defined as

$$\mathrm{NA} \equiv n_1\sin\theta_{\max} = \sqrt{n_1^2 - n_2^2} , \tag{10}$$

and, by Snell's law at the input face, $\mathrm{NA}$ is also the sine of the
largest *external* incidence angle that is accepted:

$$\sin\theta_{\text{accept}} = \mathrm{NA} . \tag{11}$$

The demo computes, for $n_1 = 1.4504$, $n_2 = 1.4447$:

```text
  numerical aperture NA = sqrt(n1^2 - n2^2) = 0.128460
  acceptance half-angle in air = asin(NA)   = 7.3806 deg
  maximum ray angle to the axis in the core = 5.0813 deg

  V = 2*pi*a*NA/lambda                      = 2.1350
  number of guided modes M ~ V^2/2          = 2.279
  single-mode cutoff lambda_c = 2*pi*a*NA/2.4048 = 1376.1 nm
```

The **V number** is the normalised frequency of the waveguide,

$$V = \frac{2\pi a}{\lambda}\,\mathrm{NA} , \tag{12}$$

and it is the single dimensionless number that classifies a step-index fibre. A
step-index fibre supports one spatial mode when $V < 2.405$ (the first zero of
$J_0$, the same constant that appeared in the Bessel treatment of
[02-03-09](../03-oscillations-and-waves/09-diffraction.md)), and approximately
$M \approx V^2/2$ modes when $V$ is large. At $\lambda = 1550$ nm the fibre
computed here has $V = 2.135$, so it is single-mode, with a cutoff at 1376.1 nm.
Double the core radius and $V$ doubles, the fibre becomes multimode, and the
single well-defined output phase that every interferometric fibre sensor needs
disappears into modal speckle.

**This is the central design fact of fibre sensing.** Single mode is not a
preference; it is what makes the measured quantity a phase.

### 3.3 Where the ray picture is not enough

For the fibre core, $\lambda/a = 1550\ \mathrm{nm}/8.2\ \mu\mathrm{m} = 0.189$
rad $= 10.83°$ — comparable with the 5.08° guiding angle itself. Geometrical
optics therefore gives the right *acceptance cone* (a boundary-condition
property, correctly captured by Snell) but cannot say how many modes the core
supports or how the field is distributed across it; that needs the waveguide
eigenvalue problem, which is the subject of
[02-10-05](./05-fiber-optics-sensing.md). The full computed comparison:

```text
             a    lambda    lambda/a (deg)   comment
   2.000e-03      550nm            0.0158   eye pupil: ray optics ok
   1.500e-01      550nm            0.0002   camera lens: ray optics ok
   8.200e-06     1550nm           10.8303   fibre core: not ray optics
   1.000e-06      633nm           36.2682   grating period: diffraction
   1.000e-08      500nm         2864.7890   protein: no ray picture
```

## 4. Lenses and the thin-lens equation

### 4.1 Derivation

A lens is two refracting surfaces. Applying (5) twice, once per surface, and
using the small-angle approximation $\sin\theta\approx\theta$ for paraxial rays,
gives the **thin-lens equation**

$$\boxed{\ \frac{1}{f} = \frac{1}{s} + \frac{1}{s'}\ } \qquad
m = -\frac{s'}{s} , \tag{13}$$

with $s$ the object distance, $s'$ the image distance and $m$ the transverse
magnification. The focal length of a thin lens of index $n$ with radii of
curvature $R_1$ and $R_2$ is the lensmaker's equation

$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right) . \tag{14}$$

Both (13) and (14) are *paraxial*: they assume rays near the axis, and they
therefore say nothing about resolution. Aperture sets resolution (lesson
[02-10-02](./02-interference-diffraction-optics.md)); focal length sets scale.
Confusing the two is the commonest error in instrument design.

### 4.2 Computed cases

```text
system                       f (mm)       s (m)   image s (mm)           m
camera, focused at 3 m         50.0           3        50.8475 -1.6949e-02
camera, focused at 30 m        50.0          30        50.0835 -1.6694e-03
camera, focused at inf         50.0       1e+09        50.0000 -5.0000e-11
telescope objective          1200.0       1e+09      1200.0000 -1.2000e-09
```

With $f = 50$ mm focused on an object at 3 m, the image forms 50.847 mm behind
the lens and a 1 m object images to 16.949 mm. The **focus travel** from infinity
to 3 m is $50.8475 - 50.0000 = 0.847$ mm. That sub-millimetre number is what a
camera's focusing mechanism has to deliver, and it is why macro photography needs
a different lens rather than a longer thread: at 1:1 magnification the image
distance is $2f$ and the travel is a full focal length.

A telescope objective of $f = 1.2$ m forms the image of a distant object exactly
one focal length behind it, at 1200 mm. The angular scale of the focal plane is
then set by the focal length alone: 1 mm on the detector corresponds to
$1/1200$ rad $= 172″$ on the sky. This is the single number that connects a
telescope's optics to its detector's plate scale.

### 4.3 A window is not transparent

A plane-parallel window displaces a ray laterally by

$$d = t\,\frac{\sin(\theta_1-\theta_2)}{\cos\theta_2} , \tag{15}$$

where $t$ is the thickness. The demo computes, for 10 mm of glass in air:

```text
 theta_1 (deg) theta_2 (deg)   displacement (mm)
          0.00        0.0000            0.000000
         15.00        9.8067            0.918575
         30.00       19.2107            1.982359
         45.00       27.7321            3.353618
         60.00       34.7447            5.192318
         75.00       39.4692            7.528052
```

Zero on axis, 3.35 mm at 45°, 7.53 mm at 75°. Any instrument with a window in
front of its detector — a pressure housing for a borehole camera, a sapphire
port on a spectrometer, an underwater housing — carries this distortion, and it
must be either designed out (window at the pupil) or calibrated.

## 5. Physical interpretation

**Refraction is a phase-matching condition, not a force.** At an interface the
component of the wavevector parallel to the surface must be continuous;
$n\sin\theta$ is that component in units of $\omega/c$. Nothing pushes the ray.
Once this is seen, Snell's law stops being a rule about light and becomes the same
statement as Snell's law for seismic waves, where the conserved quantity is
$\sin\theta/v$ — identical to (5) with $n = c/v$.

**Total internal reflection is a failure to phase-match.** Beyond the critical
angle there is no real transmitted wavevector satisfying continuity, so all the
energy returns. The field that leaks into the second medium is evanescent — it
decays exponentially, carries no net energy away, and is the same mathematical
object as the evanescent wave in anomalous seismic refraction and in the
magnetotelluric problem of
[02-07-06](../07-electromagnetism/06-em-in-conductors.md).

**A fibre is a waveguide with no mirror.** Every guided ray inside the core
bounces at an angle shallower than 5.08° to the axis, which is *steeper* than
84.92° to the interface normal, which is beyond the critical angle. The
tolerance is tight: a 0.4 per cent index step and a 5° cone. Bend the fibre and
the local geometry changes, some rays exceed the critical angle, and power leaks
out — the physical origin of bend loss and the reason a fibre installation has a
minimum bend radius.

**Lenses trade angle for position.** The thin-lens equation is a
position-space statement; the equivalent statement in angle space is that a lens
converts an angular field into a spatial position on the focal plane, by the
factor $f$. That is why a spectrometer disperses at the focal plane and why a
telescope's field of view is detector size over focal length.

## 6. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Geometrical optics | $\lambda \to 0$; rays exist | Apertures comparable with $\lambda$: diffraction sets both the beam width and the resolution |
| Snell's law | Phase matching at a plane interface | Curved or rough interfaces; a region graded over a wavelength |
| Isotropic, linear medium | $n$ a scalar constant | Birefringent crystals, anisotropic rock, intensity-dependent index |
| Non-dispersive | $n$ independent of $\lambda$ | Chromatic aberration; a fibre's modal and material dispersion |
| Paraxial rays | $\sin\theta\approx\theta$ | Wide-angle lenses; spherical aberration; the $85°$ rows of §2.2 |
| Thin lens | Lens thickness $\ll s, s'$ | Thick lenses and multi-element systems: use ray transfer matrices |
| TIR at a perfect interface | No transmission beyond $\theta_c$ | Attenuated total internal reflection: the evanescent wave couples to any absorber within a wavelength |
| Lossless | No absorption | Any real glass and especially fibre: $0.2$ dB km⁻¹ in a typical single-mode fibre at 1550 nm |
| Nominal indices | $n$ from a table | Actual fibre, water and rock: use a datasheet at the operating wavelength and temperature |

## 7. Units and dimensional analysis

- $n$ is dimensionless: $c/v$ is a ratio of two speeds. Its only scale is 1, and
  the geophysically interesting part is the *fourth* decimal in air.
- $\sin\theta$ is dimensionless because an angle in radians is a ratio of lengths.
  Using degrees inside a formula that assumes radians is the commonest unit
  error in this lesson; (7) and (8) are radian statements.
- $R$ and $T$: from (6), $R$ is a ratio of two squared index differences, hence
  dimensionless, and $R + T = 1$ for a lossless interface — a useful check that
  a computed row of §2.2 should satisfy.
- $\mathrm{NA}$: $\sqrt{n_1^2-n_2^2}$ is dimensionless, so $\mathrm{NA}$ is the
  sine of an angle, as (11) requires. A numerical aperture of 0.128 means an
  acceptance half-angle of $7.38°$, not 0.128 degrees.
- $V$: $(2\pi a/\lambda)\times\mathrm{NA}$ is
  $(\mathrm{m}/\mathrm{m})\times1$, dimensionless ✓. It must be compared with a
  pure number (2.405), never with a length.
- $d$ in (15) is a length: $t\,(\text{dimensionless})$. Check with the demo:
  10 mm of glass at 45° gives 3.354 mm, i.e. 0.34 of the thickness. A
  displacement larger than the thickness is impossible for $n_2 > n_1$; if your
  computed value exceeds it, you have mixed units.
- **Useful anchors:** $n_{\text{water}} = 1.333$; $\theta_c$ at a water-air
  surface 48.6°; glass-air 41.2°; a telecom fibre's index step 0.4 per cent;
  $\mathrm{NA} \approx 0.13$ and acceptance 7.4°; single-mode requires
  $V<2.405$; a 50 mm lens focused at 3 m has under 1 mm of travel from infinity.

## 8. Python demonstration

[`code/geometrical_optics_demo.py`](./code/geometrical_optics_demo.py) computes
Snell's law and the Fresnel reflectance, critical angles, the fibre's numerical
aperture, V number and mode count, the thin-lens solution, apparent depth, the
slab displacement and the $\lambda/a$ validity table. It uses the standard
library only. The output quoted in §§2–4 is its actual output; two further
sections are worth reading in full:

```text
  apparent depth of water = real depth / n = 0.7502 x real depth
  A 2 m deep pool looks 1.5 m deep.  Snell's law with n = 4/3 is why
  spear fishing is done with the correction applied.
```

```text
  At a = 8.2 um and lambda = 1550 nm, lambda/a =
  0.1890 rad = 10.83 deg, comparable with the
  guiding angle of 5.08 deg.  The ray picture therefore gives the
  right acceptance cone — NA is defined by the indices, and the cone
  is a property of the boundary condition — but it cannot say how
  many modes the core supports or how the field is distributed
  across it.  That requires the waveguide eigenvalue problem of
  lesson 02-10-05, which is where V, the mode count and the
  single-mode cutoff of section 3 actually come from.
```

### What to observe

| Observation | Consequence |
|---|---|
| $R = 0.02033$ at normal incidence on water, 0.583 at 85° | Glint is a grazing-angle problem, not a flat 2 per cent |
| $R_p = 0$ at 53.115°, $R_s = 0.0781$ there | Polarisation removes glint; Brewster's angle is a filter design tool |
| $\theta_c = 84.9187°$ at the core-cladding interface | The 0.4 per cent index step is the whole of fibre guidance |
| $\mathrm{NA} = 0.1285$, acceptance 7.3806° | Coupling light into a single-mode fibre is an angular alignment problem to a few degrees |
| $V = 2.135 < 2.405$ | This fibre is single-mode at 1550 nm; its phase is a single number |
| Cutoff at 1376.1 nm | Shorten the wavelength below that and the fibre becomes multimode |
| Focus travel 0.847 mm for a 50 mm lens at 3 m | Precision positioning, not precision optics, is the engineering challenge |
| 10 mm window displaces a 45° ray by 3.354 mm | Windows are refractive elements and must be placed at a pupil |
| $\lambda/a = 10.83°$ for the fibre core | Ray optics is quantitatively wrong for a single-mode fibre |

> **Breaking exercise.** Before running anything, predict what happens to the
> acceptance angle if the core index is raised from 1.4504 to 1.4600 with the
> cladding fixed at 1.4447, and to the V number and the cutoff wavelength. Then
> change the numbers in the demo and explain the direction of each change in
> terms of (10) and (12).

## 9. Common mistakes

1. **Quoting an index without its wavelength.** 1.52 is meaningless until you
   say "at 589 nm"; fused silica is 1.458 at 589 nm and 1.4447 at 1550 nm.
2. **Using degrees in Snell's law.** $\sin\theta$ requires radians in any
   subsequent differentiation or small-angle step.
3. **Believing the refractive index slows photons.** It is a phase-velocity
   ratio; the microscopic statement is coherent forward scattering.
4. **Confusing the critical angle with the acceptance angle.** The critical angle
   is measured at the core-cladding interface, from that interface's normal
   (84.92° here). The acceptance angle is measured outside the fibre, from the
   fibre axis (7.38°). They differ by two Snell refractions.
5. **Treating a numerical aperture as an angle.** $\mathrm{NA}=0.128$ is
   $\sin 7.38°$; it is a sine, not an angle, and it is dimensionless.
6. **Using the thin-lens equation for a wide-angle system.** Paraxial means
   small angles; a 24 mm lens on a full-frame sensor is not paraxial, and its
   design is not (13).
7. **Assuming a window is optically neutral.** It displaces and distorts; §4.3
   quantifies it.
8. **Ignoring bend loss in a fibre installation.** Bending changes the local
   incidence angle at the interface; exceed the critical angle anywhere and
   light leaves.
9. **Believing that total internal reflection happens at a sharp plane.** The
   evanescent field penetrates a fraction of a wavelength; polished fibre ends
   and fibre connectors live or die on this.
10. **Applying ray optics at the scale of the waveguide.** At $\lambda/a \sim
    0.19$ the ray picture gives the cone and nothing else; mode count needs the
    wave treatment.

## 10. Real-world applications

- **Distributed acoustic sensing.** Total internal reflection in a single-mode
  fibre is the physical basis of DAS: the fibre is the sensor, the cable is the
  array and the measurement is optical phase
  ([02-10-05](./05-fiber-optics-sensing.md)). A DAS installation is a
  geometry problem before it is a signal-processing problem — bend radius,
  splices, connectors.
- **Optical instruments.** Cameras, telescopes, spectrometers and lidar
  receivers are lens systems designed with (13) and (14); the focal length sets
  the plate scale and hence the ground sample distance of an airborne or
  spaceborne imager ([17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)).
- **Water-leaving radiance.** The air-water interface transmits with the
  reflectance of §2.2, compresses the hemisphere into the Snell window of 97.25°
  and produces glint at grazing angles; every ocean-colour measurement is
  corrected for all three.
- **Atmospheric refraction.** The same law with a vertically graded index bends
  starlight by an amount that grows toward the horizon — of order half a degree
  there, commonly quoted as about 34 arcmin under standard conditions, and
  strongly dependent on the temperature and pressure profile rather than being a
  material constant. That is why refraction corrections in astrometry and precise
  levelling are computed from an atmospheric model, not from a table.
- **Borehole and downhole optics.** Cameras, video logging tools and fibre
  strainmeters operate through windows and sapphire ports, with the displacement
  of (15) and the Fresnel losses of (6) designed in.
- **Seismic ray theory.** The same Snell's law, with $n$ replaced by $1/v$,
  governs the refraction of P and S waves and the head waves used in refraction
  surveying ([02-03-08](../03-oscillations-and-waves/08-reflection-refraction.md)).
- **Fibre-optic strainmeters and geodetic instruments.** Laser interferometer
  arms, fibre feed-throughs and vacuum windows all obey §2–§4; the sensitivity
  of a strainmeter is set by how well these refractive elements are
  mechanically decoupled from the strain it measures.

## 11. Further reading

- **Hecht, E. *Optics* (5th ed., Pearson).** The standard undergraduate
  treatment of geometrical optics, Fermat's principle, the Fresnel equations and
  the thin-lens equation. Level: intermediate.
- **Born, M., & Wolf, E. *Principles of Optics* (7th ed., Cambridge University
  Press).** The rigorous electromagnetic treatment of refraction at a boundary,
  including the derivation of the Fresnel coefficients and the evanescent wave.
  Level: advanced.
- **Snyder, A. W., & Love, J. D. *Optical Waveguide Theory* (Chapman & Hall).**
  The step-index fibre as an eigenvalue problem: V number, mode count, cutoff,
  bend loss. Level: graduate.
- **Mitschke, F. *Fiber Optics: Physics and Technology* (2nd ed., Springer).**
  A practically oriented treatment of fibre parameters, attenuation and the
  measurement techniques that accompany them. Level: advanced.
- **Hartmann, J., & Kenny, S. *Distributed Acoustic Sensing: Principles and
  Applications* (and the review literature on DAS in geophysics).** Where fibre
  guidance becomes a seismic instrument. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [02-03-08 Reflection, Refraction and Snell's Law for Waves](../03-oscillations-and-waves/08-reflection-refraction.md)
  — the same law for seismic and electromagnetic waves.
- [02-03-09 Diffraction, Scattering and Resolution Limits](../03-oscillations-and-waves/09-diffraction.md)
  — where the ray approximation ends and resolution limits begin.
- [02-10-02 Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md)
  — the aperture that sets resolution, and the coatings that (6) makes necessary.
- [02-10-05 Fibre-Optic Sensing and Distributed Acoustic Sensing](./05-fiber-optics-sensing.md)
  — TIR turned into an instrument.
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../07-electromagnetism/06-em-in-conductors.md)
  — the evanescent wave, seen from the electromagnetic side.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)
  — where these optics become an observing system.

Exercises:
[`exercises/01-geometrical-optics-exercises.md`](./exercises/01-geometrical-optics-exercises.md)
and
[`exercises/01-geometrical-optics-solutions.md`](./exercises/01-geometrical-optics-solutions.md).

## Self-assessment checklist

- [ ] I can derive $n_1\sin\theta_1 = n_2\sin\theta_2$ from Fermat's principle
      and state what is being extremised. (§2.1)
- [ ] I can compute a refracted angle, a critical angle and a Fresnel
      reflectance, and check that $R+T=1$. (§2.2, §2.3)
- [ ] I can explain the Brewster angle and why it removes glint. (§2.2)
- [ ] I can compute the numerical aperture, acceptance angle, V number, mode
      count and cutoff wavelength of a step-index fibre. (§3.2)
- [ ] I can solve the thin-lens equation and compute the focus travel and the
      plate scale of an instrument. (§4.2)
- [ ] I can compute the lateral displacement produced by a window and say where
      in an optical train it must be placed. (§4.3)
- [ ] I can state the validity condition of geometrical optics and give a
      numerical example of its failure. (§3.3, §6)
- [ ] I can explain why the ray picture gets the acceptance cone right and the
      mode count wrong. (§3.3)
