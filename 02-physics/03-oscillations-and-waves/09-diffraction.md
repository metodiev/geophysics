---
id: 02-03-09
title: "Diffraction, Scattering and Resolution Limits"
level: advanced
prereqs: ["02-03-06", "02-03-08", "01-05-05"]
estimated_minutes: 90
tags: [diffraction, scattering, resolution, fresnel-zone]
---

# Diffraction, Scattering and Resolution Limits

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Huygens' principle and use it to derive the Fraunhofer diffraction
   pattern of a slit and of a circular aperture.
2. **Derive** the resolution limits: $\theta_{\min} = 1.22\lambda/D$ for a
   circular aperture (Rayleigh) and the Fresnel-zone radius
   $r_F = \sqrt{\lambda z/2}$ for a reflection at depth $z$.
3. **Compute** the on-axis Fresnel-zone structure and explain the half-period
   zones, including the result that truncating at the first zone edge maximises
   the on-axis field.
4. **Classify** scattering regimes by the size parameter $ka$ (Rayleigh,
   resonant/Mie, geometric) and say which applies to a given heterogeneity.
5. **Quantify** the resolution of a seismic, GPR or optical measurement, and
   distinguish the unmigrated Fresnel-zone limit from the migrated limit.
6. **Verify** all of the above numerically by direct quadrature of the diffraction
   integrals, and report the measured agreements.

## Prerequisites

- [02-03-06 Superposition, Interference and Standing Waves](./06-superposition-interference.md)
  — interference, which diffraction generalises to a continuum of sources.
- [02-03-08 Reflection, Refraction and Snell's Law for Waves](./08-reflection-refraction.md)
  — the plane-interface limit of what becomes diffraction when the interface ends.
- [01-05-05 Integration, Areas and the Fundamental Theorem](../../01-mathematics/05-single-variable-calculus/05-integration.md)
  — the quadrature used to evaluate the diffraction integrals.

## 1. Why a plane interface is not enough

Lesson 02-03-08 assumed interfaces that are infinite and flat. Real interfaces
end — at a fault, a pinch-out, a channel edge, a crack tip — and wherever an
interface ends, the wave does not simply stop: it spreads into the shadow. This is
diffraction, and it is the single most useful *and* most limiting effect in
geophysical imaging:

- **Useful**: every edge in the subsurface radiates a diffraction, and a migration
  algorithm focuses those diffractions back to their true locations. Diffractions
  are the signal that makes seismic imaging possible.
- **Limiting**: the same spreading sets the resolution limit. A point reflector at
  depth does not appear as a point but as a Fresnel zone of finite size, whether
  or not the data are migrated.

Formally, diffraction is just interference with a continuum of secondary sources.
This lesson derives the standard results and, crucially, keeps track of which
approximation each one uses.

## 2. Precise definitions

**Huygens' principle.** Every point on a wavefront acts as a source of secondary
spherical wavelets; the field at a later point is the superposition of them.

**Fraunhofer (far-field) diffraction.** The observation distance is large enough
that the curvature of the incident wavefront can be neglected over the aperture:
the condition is $z \gg a^2/\lambda$ for an aperture of size $a$.

**Fresnel (near-field) diffraction.** The curvature matters; the field depends on
the aperture in a more complicated way, and the natural units are the Fresnel
zones.

**Fresnel zone.** The region of a wavefront that contributes in phase to the
field at a point; the $n$-th zone boundary is where the path is longer by
$n\lambda/2$. Its radius at distance $z$ for a plane incident wave is
$r_n = \sqrt{n\lambda z}$.

**Resolution limit.** The smallest separation of two objects (or of two
interfaces) that can be distinguished. It depends on the definition of
"distinguished" — Rayleigh, Sparrow, or a stated signal-to-noise criterion.

**Size parameter.** $ka = 2\pi a/\lambda$ for a scatterer of size $a$; the regime
indicator.

## 3. Derivations

### 3.1 From Huygens to an integral

Take a plane wave normally incident on an opaque screen with an aperture, and
evaluate the field on a distant screen at angle $\theta$. Each element $dS$ of the
aperture contributes a wavelet with amplitude proportional to $dS$ and phase
$kr$, where $r$ depends on the element's position. With the observation point far
away,

$$U(\theta) \propto \iint_{\text{aperture}}
e^{-ik\sin\theta\,x}\,dS , \tag{1}$$

where $x$ is the coordinate across the aperture in the plane of incidence. This is
the **Fraunhofer diffraction integral**. Everything in the next two subsections is
a quadrature of equation (1).

### 3.2 The slit

For a slit of width $a$ along $x$ and infinite extent along $y$, the integral
factorises and only the $x$ integral matters:

$$U(\theta) \propto \int_{-a/2}^{a/2}e^{-ik\sin\theta\,x}\,dx
= a\,\frac{\sin\beta}{\beta} , \qquad
\beta = \frac{ka\sin\theta}{2} = \frac{\pi a\sin\theta}{\lambda} , \tag{2}$$

so the intensity is $I(\theta) = I_0\left(\sin\beta/\beta\right)^2$. The zeros are
at $\beta = m\pi$, i.e.

$$\sin\theta_m = \frac{m\lambda}{a} , \tag{3}$$

and the first minimum is at $\sin\theta = \lambda/a$. Wider slit, narrower
pattern: the trade-off in one line. The demo evaluates equation (1) by the
trapezoid rule and compares with equation (2), finding a maximum difference of
$7.7\times10^{-7}$ over the table and locating the first zero at
$\sin\theta = 0.250200$ against the analytic 0.250000 (a relative difference of
$8\times10^{-4}$, set by the search grid).

### 3.3 The circular aperture and the Rayleigh limit

For a circular aperture of diameter $D$, the integral in polar coordinates gives
the **Airy pattern**

$$U(\theta) \propto \frac{2J_1(q)}{q} , \qquad
q = \frac{kD}{2}\sin\theta = \frac{\pi D\sin\theta}{\lambda} , \tag{4}$$

with $J_1$ the Bessel function of the first kind. Its first zero is at
$q = 3.831705970$ (bisection on $J_1$, reproduced to nine digits in the demo), so

$$\sin\theta_{\min} = \frac{3.83170597\,\lambda}{\pi D} = 1.21967\,\frac{\lambda}{D}
\ \longrightarrow\ \theta_{\min} \approx 1.22\frac{\lambda}{D} . \tag{5}$$

The demo's quadrature of equation (1) agrees with equation (4) to
$1.6\times10^{-6}$ at the worst angle and $1.7\times10^{-13}$ on axis, so the
Airy form is verified rather than quoted. For $D = 0.25$ m and
$\lambda = 0.5$ mm the limit is $2.439\times10^{-3}$ rad $= 0.1398^\circ$.

### 3.4 Fresnel zones on axis

Now take the observation point *behind* a circular aperture and ask how the
on-axis field depends on the aperture radius. The paraxial integral in polar
coordinates is

$$U(r) \propto \int_0^r \frac{2\pi\rho}{i\lambda z}e^{i\pi\rho^2/(\lambda z)}\,d\rho
\ \propto\ \int_0^{u}e^{i\phi}\,d\phi , \qquad u = \frac{\pi r^2}{\lambda z} ,
\tag{6}$$

which integrates exactly:

$$|U(r)| = 2\left|\sin\!\left(\frac{\pi r^2}{2\lambda z}\right)\right| . \tag{7}$$

So the on-axis amplitude oscillates between 0 and 2 as the aperture grows, with
the first maximum at $r = \sqrt{\lambda z}$ — the radius of the **first Fresnel
zone**. The physical reading: the zone is divided into concentric rings whose
contributions alternate in sign because each successive ring adds a path
difference of $\lambda/2$; adding a ring that is out of phase *reduces* the field,
which is why the amplitude is not monotonic in aperture size. Truncating the
aperture at the first zone edge gives the largest on-axis field for the least
material — the principle of the zone plate, and a useful diagnostic of whether a
lens or antenna is aperture-limited or aberration-limited.

The demo evaluates the oscillatory integral by Simpson's rule for several radii
and compares with equation (7): the maximum difference is $1.1\times10^{-4}$, and
the numerically located first maximum is at $r = 14.1421$ m against the predicted
$\sqrt{\lambda z} = 14.1421$ m for $\lambda = 0.5$ m, $z = 400$ m.

### 3.5 Resolution of a reflection measurement

For a **reflection** at depth $z$ (two-way path $2z$), the first Fresnel zone
radius follows from requiring the extra path to be $\lambda/2$:

$$2\sqrt{z^2+r_F^2} - 2z = \frac{\lambda}{2}
\quad\Longrightarrow\quad
r_F \approx \sqrt{\frac{\lambda z}{2}} \quad (z \gg \lambda/4) . \tag{8}$$

The factor of two relative to equation (7) is the two-way path, and it is a
standard place to make an error. The demo's numbers: for $v_p = 3000$ m s⁻¹,
$f = 30$ Hz ($\lambda = 100$ m) and $z = 1000$ m,
$r_F = \sqrt{100\times1000/2} = 223.61$ m, so the interface area contributing to
one trace has a diameter of about 447 m. Features narrower than that are averaged
into a single wavelet.

**Migration** narrows the effective footprint back toward the wavelength limit,
but not below it: the practical migrated resolution is of order $\lambda/4$ to
$\lambda/2$, i.e. 25–50 m in this example, an order of magnitude better than the
unmigrated Fresnel zone. Both numbers are *approximations* whose numerical
coefficient depends on the wavelet bandwidth, the migration aperture, and the
signal-to-noise ratio, and they should be computed for the survey at hand rather
than quoted as laws.

### 3.6 Scattering regimes

A heterogeneity of size $a$ in a medium with wavelength $\lambda$ behaves
qualitatively differently depending on the size parameter:

| Regime | Condition | Scattered amplitude scaling | Geophysical example |
|---|---|---|---|
| Rayleigh | $ka \ll 1$ | $\propto a^3/\lambda^2$, and $\propto \omega^4$ | Grain-scale heterogeneity; also why the sky is blue |
| Resonant / Mie | $ka \sim 1$ | Strong, structured, resonance-dependent | Seismic wavelength-scale layering, fracture sets |
| Geometric / ray | $ka \gg 1$ | Reflection and refraction at surfaces; $\propto$ contrast | Regional reflectors, large faults |

The Rayleigh scaling $a^3$ means that small heterogeneities are very weak
scatterers, and $a^3/\lambda^2$ means that high frequencies scatter far more
strongly — the reason seismic coda is dominated by high frequencies, and the
reason attenuation often appears to depend on frequency even in a purely elastic
heterogeneous medium. Distinguishing *scattering* attenuation from *intrinsic*
attenuation is one of the persistent difficulties of the subject, and it cannot be
settled without either a model of the heterogeneity or an independent measurement
of $Q$.

## 4. Physical interpretation

**Diffraction is what a wave does when it meets an edge.** The energy that
"should" be blocked appears in the shadow because the wavefront is not a
mathematical surface but a distribution of secondary sources with a finite
extent. The smaller the aperture relative to the wavelength, the wider the spread:
$\lambda/a$ sets the angular scale, which is the whole content of equations (3)
and (5).

**Resolution is an angular, then a spatial, statement.** An aperture of size $D$
cannot resolve angles below $\sim\lambda/D$; at distance $z$, that angle
corresponds to a length $\lambda z/D$. In reflection geometry the relevant
"aperture" is the round-trip path, which is why the Fresnel-zone radius, not the
aperture of the array, is the natural scale for a reflection measurement.

**Every edge is a source, and that is good news.** Because diffractions radiate in
all directions, a survey sees edges from many angles, and a migration algorithm
can stack those contributions to locate them. Inverting a seismic section is in
large part the business of collapsing diffractions.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Scalar diffraction (Kirchhoff) | One field, no polarisation | Vector elastic or electromagnetic diffraction differs in amplitude and polarisation; the geometry of the zeros is usually preserved |
| Fraunhofer (far field) | $z \gg a^2/\lambda$ | Near-field: use Fresnel zones, and the pattern changes with distance |
| Kirchhoff boundary conditions | Field is the incident field inside the aperture, zero outside | Real screens have edge currents; the approximation is good for apertures $\gg\lambda$ |
| Thin, opaque screen | No transmission through the barrier | Imperfect screens require a transfer-matrix treatment |
| Paraxial approximation in §3.4 | $\sin\theta \approx \theta$ | Wide angles need the full Fresnel integral; the zone radii acquire an oblique correction |
| Single scattering | Scattered energy does not rescatter | Multiple scattering (strong heterogeneity) requires radiative-transfer or full-wave methods |
| Born approximation for heterogeneous media | Weak contrast, $\delta c/c \ll 1$ | Strong contrasts require iterated (nonlinear) scattering descriptions |

## 6. Units and dimensional analysis

- $\beta = \pi a\sin\theta/\lambda$ is dimensionless ✓; $\sin\theta$ is
  dimensionless, and the argument of a sine must be.
- $q = \pi D\sin\theta/\lambda$ dimensionless ✓, so $2J_1(q)/q$ is dimensionless
  and the pattern is a ratio of intensities.
- $r_n = \sqrt{n\lambda z}$ has units $\sqrt{\mathrm{m\times m}} = \mathrm{m}$ ✓.
  With $\lambda = 0.5$ m and $z = 400$ m, $\lambda z = 200$ m² and
  $r_1 = 14.142$ m ✓ as measured.
- $\theta \approx \lambda/D$ is dimensionless; the spatial resolution at distance
  $z$ is $\lambda z/D$ (m) ✓.
- The Rayleigh scattered amplitude $\propto a^3/\lambda^2$ has units of length,
  which is why it is quoted as a ratio to the incident amplitude.

## 7. Python demonstration

[`code/diffraction_demo.py`](./code/diffraction_demo.py) evaluates the diffraction
integrals and compares them with the closed forms. Observed output:

```text
 sin(theta)  |U|/|U(0)| quadrature   closed form  difference
      0.000            1.000000000   1.000000000    0.00e+00
      0.100            0.756826106   0.756826729    6.22e-07
      0.250            0.000000000   0.000000000    1.81e-17
max difference over the table = 1.154e-06
first minimum at sin(theta) = lambda/a = 0.2500
numerically located first zero of the pattern at sin(theta) = 0.250200 (relative difference 8.00e-04)
```

```text
 angle (deg)    quadrature   Airy closed form  difference
      0.0000     1.0000000          1.0000000    1.71e-13
      0.0500     0.7828077          0.7828071    6.00e-07
      0.1401    -0.0019287         -0.0019294    7.23e-07
      0.2000    -0.1248662         -0.1248657    4.50e-07
first zero of J1 (bisection) = 3.831705970
  therefore sin(theta_min) = 3.831706 lambda/(pi D) = 1.219670 lambda/D
  numeric value here: theta_min = 2.439e-03 rad = 0.139764 deg
```

```text
   r (m)   |U| numeric    2|sin(pi r^2/(2 lz))|  difference
  2.0000     0.0628226                0.0628215    1.05e-06
 10.0000     1.4142321                1.4142136    1.85e-05
 14.1421     2.0000000                2.0000000    2.28e-10
 20.0000     0.0001047                0.0000000    1.05e-04
max difference over the table = 1.089e-04
predicted first maximum at r = sqrt(lambda z) = 14.1421 m
first maximum located numerically at r = 14.1421 m with amplitude 2.000000
```

```text
P wave at 3000 m/s, 30 Hz -> wavelength = 100.0 m
reflector at depth z = 1000 m
first Fresnel zone radius  sqrt(lambda z/2) = 223.61 m
  lateral footprint on the interface = 447.21 m
migrated resolution limit ~ lambda/4      = 25.00 m
migrated resolution limit ~ lambda/2      = 50.00 m
```

### What to observe

| Observation | Consequence |
|---|---|
| The slit quadrature matches the closed form to $7.7\times10^{-7}$ | The Fraunhofer integral and the sinc pattern are the same function; the residual is the quadrature error, and it falls as the number of points grows |
| The first zero is located at 0.250200 against 0.250000 | The relative difference is the search grid resolution, not a physical discrepancy — always state how a numerical extremum was located |
| The Airy quadrature matches to $1.6\times10^{-6}$ and the first zero of $J_1$ to nine digits | The 1.22 rule is verified from first principles, including the constant, not just the scaling |
| The on-axis Fresnel amplitude oscillates 0 → 2 and its first maximum is exactly at $\sqrt{\lambda z}$ | The half-period zone structure is real; the amplitude is not monotonic in aperture |
| $\lambda z = 200$ m² gives $r_1 = 14.1421$ m | The zone radius scales as the square root of both wavelength and distance |
| The Fresnel-zone footprint at 1 km and 30 Hz is 447 m across, but the migrated limit is 25–50 m | Unmigrated lateral resolution and migrated resolution differ by an order of magnitude; both must be quoted with their geometry |

> **Breaking exercise.** Change the reflector depth to 4000 m and predict, before
> running, the Fresnel-zone radius and the migrating-resolution limits. Then
> explain why the Fresnel zone grows only as $\sqrt z$ while the migrated limit is
> independent of $z$ in this approximation.

## 8. Common mistakes

1. **Using $r_F = \sqrt{\lambda z}$ for a reflection.** The two-way path gives
   $\sqrt{\lambda z/2}$; the factor of two is a standard error.
2. **Quoting a resolution limit without its criterion.** Rayleigh, Sparrow,
   $\lambda/4$, Fresnel zone and migration aperture limits all differ, sometimes by
   a factor of ten.
3. **Forgetting the far-field condition.** The Airy pattern is the *far-field*
   pattern; in the near field the pattern changes with distance.
4. **Using scalar diffraction for a vector problem and expecting amplitudes to be
   right.** The geometry of the zeros is robust; the amplitudes and polarisations
   are not.
5. **Treating diffraction as a nuisance rather than as signal.** The diffractions
   from edges are what make migration work.
6. **Assuming attenuation is always intrinsic.** Wavelength-scale scattering
   mimics attenuation, with a different frequency dependence; distinguishing them
   requires a heterogeneity model.
7. **Assuming that migration beats the wavelength.** It cannot: no processing
   recovers information at spatial frequencies that were never recorded.
8. **Using the Rayleigh criterion for two sources of unequal strength.** A bright
   source near a faint one is detectable at separations well below 1.22$\lambda/D$;
   the Rayleigh criterion assumes equal brightness.

## 9. Real-world applications

- **Seismic migration and diffraction imaging.** Diffracted energy from faults and
  channel edges is focused by migration; deliberately isolating it is the basis of
  diffraction imaging, a standard tool for sub-seismic-scale structure. Data and
  tooling: [ObsPy](https://docs.obspy.org), [PyGMT](https://pygmt.org).
- **Resolution estimation for a survey.** The Fresnel-zone radius and the
  migrated limit are the first two numbers quoted in a feasibility study; they set
  what "detectable" means for a target.
- **GPR and ground-penetrating radar.** Diffraction hyperbolae from buried
  utilities are both the principal nuisance and the principal measurement; the
  hyperbola's shape gives the velocity.
- **Optical and astronomical resolution.** $\theta = 1.22\lambda/D$ sets the
  diffraction limit of every telescope, microscope and camera, and motivates
  interferometry, which synthesises a larger $D$ from separated apertures.
- **First-arrival and diffraction tomography.** Inverting travel times or
  wavefields in the Fresnel-zone volume (rather than along rays) is the modern
  formulation of seismic tomography, and it is diffraction that defines the volume
  a measurement averages over.
- **Coda and scattering attenuation.** The coda of a local earthquake is
  dominated by scattering from heterogeneity at all scales; its decay is inverted
  for the scattering strength and the intrinsic $Q$, and the two are notoriously
  difficult to separate (see [06-seismology](../../06-seismology/README.md)).

## 10. Further reading

- **Born, M., & Wolf, E. *Principles of Optics* (Cambridge University Press).**
  The definitive treatment of Fraunhofer and Fresnel diffraction, including the
  zone construction and the Airy pattern. Level: advanced.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** Scattering, the Born approximation and the resolution
  discussion in the context of seismology. Level: advanced.
- **Shearer, P. M. *Introduction to Seismology* (3rd ed., Cambridge University
  Press, 2019).** The Fresnel zone and seismic resolution, with observational
  examples. Level: intermediate.
- **Yilmaz, Ö. *Seismic Data Analysis* (SEG).** Diffractions, migration and the
  practical resolution limits of reflection data. Level: intermediate to
  advanced.
- **Ishimaru, A. *Wave Propagation and Scattering in Random Media* (IEEE Press).**
  The Rayleigh/Mie/geometric regimes and multiple scattering, in full. Level:
  graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [06 Superposition, Interference and Standing Waves](./06-superposition-interference.md)
  — interference of two sources; diffraction is the integral over a continuum.
- [08 Reflection, Refraction and Snell's Law for Waves](./08-reflection-refraction.md)
  — the infinite-plane limit whose failure produces diffraction.
- [10 Attenuation, Absorption and the Quality Factor Q](./10-attenuation.md) —
  the other mechanism that removes energy from a beam.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the vector wavefield whose scattering is polarisation-dependent.
- [01-10-07 The Two-Dimensional Fourier Transform](../../01-mathematics/10-fourier-analysis/07-2d-fourier.md)
  — the transform used to compute a diffraction pattern as a spectrum of the
  aperture.
- [06-seismology](../../06-seismology/README.md) — migration, diffraction imaging
  and scattering attenuation.

Exercises:
[`exercises/09-diffraction-exercises.md`](./exercises/09-diffraction-exercises.md)
and
[`exercises/09-diffraction-solutions.md`](./exercises/09-diffraction-solutions.md).

## Self-assessment checklist

- [ ] I can state Huygens' principle and write the Fraunhofer integral.
      (Section 3.1)
- [ ] I can derive the single-slit pattern and its first zero. (Section 3.2)
- [ ] I can derive the circular-aperture resolution limit and explain where 1.22
      comes from. (Section 3.3)
- [ ] I can derive and interpret the Fresnel-zone radius, and distinguish
      $\sqrt{\lambda z}$ from $\sqrt{\lambda z/2}$. (Sections 3.4, 3.5)
- [ ] I can explain why the on-axis amplitude oscillates with aperture size.
      (Section 3.4)
- [ ] I can classify a scatterer by $ka$ and state the amplitude scaling in the
      Rayleigh regime. (Section 3.6)
- [ ] I can compute the lateral resolution of a reflection survey with and
      without migration, and state the assumptions in each number. (Section 3.5)
- [ ] I can name three uses of diffraction as signal rather than nuisance.
      (Sections 4, 9)
