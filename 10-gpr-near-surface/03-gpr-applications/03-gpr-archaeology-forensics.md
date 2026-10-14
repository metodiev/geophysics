---
id: 10-03-03
title: "GPR in Archaeology, Forensics and Buried Utilities"
level: advanced
prereqs: ["10-01-01", "10-01-02", "10-01-05", "10-02-02"]
tags: [gpr, near-surface, geotechnical, archaeology, forensics, utilities, migration, resolution]
---

# GPR in Archaeology, Forensics and Buried Utilities

**All models and data in this module are SYNTHETIC.** The targets, depths,
permittivities, target sizes and pick errors are chosen teaching values. No
excavation, forensic case, utility record or site is described here. Physical
constants and standard material permittivities are labelled as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the diffraction hyperbola $t(x) = 2\sqrt{x^2+z^2}/v$ from the
   two-way path, and **show** that a fit to $t^2$ against $x^2$ returns the
   velocity and the depth.
2. **Quantify** how the aperture of the fit controls the correlation between the
   recovered velocity and depth, and **state** the aperture required for a
   velocity of a given accuracy.
3. **Compute** the reflection coefficients of the targets a utility or forensic
   survey looks for, and **explain** why the fill of a pipe matters more than its
   material.
4. **Derive** the Rayleigh-regime amplitude scaling $a^3 f^2$ for targets small
   compared with the wavelength, and **compute** the dynamic range a size change
   demands.
5. **Derive** the first Fresnel zone radius $r_f = \sqrt{\lambda z/2}$ and
   **distinguish** the detection footprint from the two-target resolution limit.
6. **Explain** what Kirchhoff migration does to a hyperbola, and **use** the
   quality of the focus as a velocity diagnostic.
7. **State** the depth error that a wrong overburden velocity produces, and
   **report** a depth with the velocity it came from.

## Prerequisites

- [10-01-01 GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](../01-gpr-principles/01-gpr-physics.md)
  — speed, reflection coefficients, the Ricker pulse.
- [10-01-02 Velocity Estimation and Depth Conversion](../01-gpr-principles/02-gpr-velocity-and-depth.md)
  — velocity from a target of known depth, and depth conversion.
- [10-01-05 Vertical and Horizontal Resolution Limits](../01-gpr-principles/05-gpr-resolution.md)
  — the Fresnel zone and the $\lambda/4$ limit.
- [10-02-02 Processing Steps: Dewow, Gain, Filtering, Migration](../02-gpr-acquisition-and-processing/02-gpr-processing.md)
  — the migration operator used in Section 3.4.

## 1. Intuition: the hyperbola is the one unambiguous object

A GPR section is a picture of two-way time against position. Most of what it
contains is ambiguous: a flat reflection may be an interface, a multiple or a
change of antenna coupling; a weak area may be a small target or a wet patch. The
diffraction **hyperbola** is the exception. It is the signature of a scattering
object small compared with the Fresnel zone, and its shape is fixed by geometry:

- the **apex** gives the object's position along the profile and its two-way
  time;
- the **curvature** gives the velocity of the material above it;
- the **asymptote** slope gives the same velocity again, and the two must agree.

That is why utility mapping, rebar location and archaeological prospection are
all taught as hyperbola-fitting procedures. And it is also why they go wrong in
the same way: the curvature is a *second-order* effect of the aperture, so a
short profile determines the apex well and the velocity badly, and the depth —
which needs both — inherits the velocity error in full.

Two other target classes behave differently and deserve their own statements:

- **Extended buried structures** (walls, floors, voids, pipes seen end-on) give
  flat or mounded reflections whose amplitude is governed by the reflection
  coefficient of Section 3.2, not by curvature.
- **Disturbed ground** — the forensic case of a grave, a pit or a trench —
  usually has a *small* permittivity contrast, and what identifies it is the
  destruction of the natural stratigraphy. The observable is a pattern, not a
  reflector, and the honest detection statement is about pattern disruption.

## 2. Precise definitions

### 2.1 Geometry

| Symbol | Meaning | Unit |
|---|---|---|
| $x$ | antenna offset from the target's surface projection | m |
| $z$ | target depth | m |
| $v$ | speed above the target | $\mathrm{m\,ns^{-1}}$ |
| $t$ | two-way time | ns |
| $t_0$ | two-way time at the apex, $x=0$ | ns |
| $a$ | half-aperture of the fit, $\lvert x\rvert \le a$ | m |
| $r_f$ | first Fresnel zone radius | m |
| $\lambda$ | wavelength in the medium | m |

### 2.2 Rayleigh versus geometric scattering

A target is **small** if its size is much less than the wavelength
($ka \ll 1$ with $k = 2\pi/\lambda$), in which case it scatters as a dipole and
the amplitude scales as $a^3f^2$ (Section 3.3). It is **large** when $ka \gg 1$,
in which case the reflection is geometric and its amplitude is set by the
reflection coefficient of the interface. The demonstration's $500\ \mathrm{MHz}$
centre frequency in a soil with $\varepsilon_r = 9$ gives
$\lambda = 0.200\ \mathrm{m}$, so a $20\ \mathrm{mm}$ target is at
$ka = 0.63$ — Rayleigh, and a $2\ \mathrm{m}$ wall is firmly geometric. The two
regimes are not a continuum to be interpolated; they are different physics.

## 3. Derivations

### 3.1 The hyperbola, and what a fit can and cannot separate

For a transmitter and receiver at the same position $x$, the path to a point
scatterer at depth $z$ is $2\sqrt{x^2+z^2}$, so

$$t(x) = \frac{2\sqrt{x^2+z^2}}{v}.$$

Squaring gives a straight line in $x^2$:

$$t^2 = \frac{4}{v^2}x^2 + \frac{4z^2}{v^2},$$

i.e. $t^2 = m x^2 + c$ with

$$m = \frac{4}{v^2}, \qquad c = \frac{4z^2}{v^2},
\qquad v = \frac{2}{\sqrt m},\qquad z = \frac{\sqrt c}{2}\,v.$$

Two parameters are extracted from the measurements. The intercept $c$ is
determined by the apex time, which is the best-measured feature of the whole
event; the slope $m$ is determined by the *rate of change* of $t^2$ with $x^2$,
which over a small aperture is a small number known only as well as the picks
allow. Since $z = v\sqrt{c}/2$, **every error in $v$ is an error in $z$ of the
same fractional size**, which is why the two estimates come out almost perfectly
correlated.

*Measured result.* The demonstration picks a target at $z = 1.50\ \mathrm{m}$ in
a soil with $\varepsilon_r = 9.0$ ($v = 0.0999\ \mathrm{m\,ns^{-1}}$) with a
$0.20\ \mathrm{ns}$ pick error, $41$ traces, and a Monte Carlo of $4000$
realisations:

| aperture | $\sigma_v$ | $\sigma_z$ | correlation $\rho(v,z)$ |
|---|---|---|---|
| $\pm2.00\ \mathrm{m}$ | $0.0003\ \mathrm{m\,ns^{-1}}$ ($0.3\%$) | $0.0060\ \mathrm{m}$ ($0.4\%$) | $+0.948$ |
| $\pm0.50\ \mathrm{m}$ | $0.0032\ \mathrm{m\,ns^{-1}}$ ($3.2\%$) | $0.0494\ \mathrm{m}$ ($3.3\%$) | $+0.999$ |

Shrinking the aperture by a factor of four costs a factor of ten in velocity
accuracy and drives the correlation to $+0.999$ — the pair becomes, for practical
purposes, one number. The lesson is arithmetic, not opinion: **a velocity picked
from a hyperbola is a statement about the aperture that produced it.**

### 3.2 Reflection coefficients of typical targets

With $R = (\sqrt{\varepsilon_1}-\sqrt{\varepsilon_2})/(\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2})$,
using $\varepsilon_1 = 9.0$ for the host soil:

| target | $\varepsilon_2$ | $R$ | power (dB) |
|---|---|---|---|
| metal | $\to\infty$ (perfect conductor) | $-1.000$ | $0.0$ |
| air-filled void | $1.0$ | $+0.500$ | $-6.0$ |
| water-filled void | $80.1$ | $-0.498$ | $-6.1$ |
| solid plastic pipe | $2.6$ | $+0.301$ | $-10.4$ |
| dry concrete | $6.0$ | $+0.101$ | $-19.9$ |

The metal entry is the limiting case $R \to -1$ of a perfect conductor, where the
field cannot penetrate at all: a metal target is the only reflector that comes
back with the incident amplitude, and it does so with a phase reversal.

The important reading is the comparison between the two voids. **An air-filled
void and a water-filled void have the same amplitude and opposite sign**, because
what matters is the *contrast with the host*: air is a step up in impedance,
water a step down. A pipe is not a material; it is a container, and the echo comes
from its contents — which is why a plastic water main in wet soil can be
invisible while the same pipe, empty in dry sand, is a $+0.5$ reflector.

### 3.3 Small targets: the Rayleigh scaling

For a small homogeneous sphere of radius $a \ll \lambda$, the incident field
induces a dipole moment proportional to its polarizability,
$p \propto \varepsilon_0(\varepsilon_r-1)a^3 E$, and a radiating dipole's field is
proportional to $\omega^2 p$. The scattered amplitude therefore scales as

$$A_{\mathrm{scat}} \propto a^3 \omega^2 \propto a^3 f^2.$$

*Measured consequence.* The demonstration computes the relative amplitude for
radii $0.01$, $0.02$, $0.04$ and $0.08\ \mathrm{m}$ against a $0.04\ \mathrm{m}$
reference:

| radius (m) | relative amplitude | dB |
|---|---|---|
| $0.01$ | $0.0156$ | $-36.1$ |
| $0.02$ | $0.1250$ | $-18.1$ |
| $0.04$ | $1.0000$ | $0.0$ |
| $0.08$ | $8.0000$ | $+18.1$ |

**Halving the radius costs $18\ \mathrm{dB}$** — a factor of $8$ in amplitude and
$64$ in power. A $10\ \mathrm{mm}$ target is $36\ \mathrm{dB}$ weaker than a
$40\ \mathrm{mm}$ one, which is a factor of $4000$ in power. Detection of small
objects is therefore a dynamic-range problem long before it is a resolution
problem, and a report that a target "should be resolvable" at a given frequency
says nothing at all about whether it will be *seen*.

### 3.4 Migration, and the focus as a velocity diagnostic

Kirchhoff migration sums the data along the hyperbola predicted for each output
point:

$$M(x_0,t_0) = \sum_x d\!\left(x,\;\sqrt{t_0^2 + \frac{4(x-x_0)^2}{v_{\mathrm{mig}}^2}}\right).$$

When $v_{\mathrm{mig}}$ equals the true velocity, the hyperbola collapses to a
point at the scatterer's position: the sum is constructive everywhere along the
event. When $v_{\mathrm{mig}}$ is wrong, the data are summed along the wrong
curve, the energy is spread over neighbouring traces and the peak amplitude
falls. The demonstration migrates a synthetic hyperbola over a $1.50\ \mathrm{m}$
target with $121$ traces at $0.05\ \mathrm{m}$:

| $v_{\mathrm{mig}}$ (m/ns) | depth of maximum (m) | peak amplitude | half-width (m) |
|---|---|---|---|
| $0.0800$ | $1.192$ | $0.0809$ | $0.200$ |
| $0.0999$ (true) | $1.499$ | $0.6495$ | $0.000$ |
| $0.1200$ | $1.815$ | $0.1093$ | $0.200$ |

Two independent statements come out of that table, and they are worth keeping
separate:

- the **apex time is set by the data** and cannot be changed by the migration
  velocity, so a wrong velocity moves the depth linearly
  ($v_{\mathrm{mig}}t_0/2$) — $1.192$ and $1.815\ \mathrm{m}$ against a true
  $1.50\ \mathrm{m}$;
- the **focus quality is set by the velocity**, and a $20\%$ error costs a factor
  of $6$ in peak amplitude ($0.6495 \rightarrow 0.0809$). Focus is therefore a
  usable velocity estimator — the basis of velocity analysis in
  [10-02-03](../02-gpr-acquisition-and-processing/03-gpr-velocity-analysis.md) —
  and the same velocity that sharpens the focus also moves the depth.

### 3.5 The Fresnel zone

The first Fresnel zone is the area of a reflector whose contributions arrive
within half a wavelength of the apex contribution. A point at horizontal radius
$r$ on a reflector at depth $z$ has a longer two-way path than the apex by

$$\Delta \ell = 2\left(\sqrt{z^2+r^2}-z\right) \simeq \frac{r^2}{z}
\quad \mathrm{for}\ r \ll z.$$

Setting $\Delta\ell = \lambda/2$:

$$r_f = \sqrt{\frac{\lambda z}{2}}.$$

*Measured values (host $\varepsilon_r = 9$, $v = 0.0999\ \mathrm{m\,ns^{-1}}$):*

| $f$ (MHz) | $\lambda$ (m) | $r_f$ at $0.5\ \mathrm{m}$ | at $1.5\ \mathrm{m}$ | at $3.0\ \mathrm{m}$ |
|---|---|---|---|---|
| $250$ | $0.400$ | $0.316$ | $0.548$ | $0.774$ |
| $500$ | $0.200$ | $0.224$ | $0.387$ | $0.548$ |
| $1000$ | $0.100$ | $0.158$ | $0.274$ | $0.387$ |

$r_f$ is the **detection footprint**: the patch of a reflector that contributes
to one echo, and therefore the smallest object that can return a strong echo on
its own. It is not the two-target resolution limit, which additionally depends on
the contrast and the noise; the two are the same order and are routinely confused
in reports.

### 3.6 Depth from an apex time, and the cost of a wrong velocity

$$z = \frac{v t_0}{2}, \qquad \frac{\delta z}{z} = \frac{\delta v}{v}
\quad \mathrm{exactly, with no second-order term.}$$

The demonstration's table for $t_0 = 30.02\ \mathrm{ns}$ and a true $1.50\
\mathrm{m}$:

| assumed $v$ (m/ns) | reported depth (m) | error (m) | error (%) |
|---|---|---|---|
| $0.070$ | $1.05$ | $-0.45$ | $-30.0$ |
| $0.080$ | $1.20$ | $-0.30$ | $-19.9$ |
| $0.090$ | $1.35$ | $-0.15$ | $-9.9$ |
| $0.100$ | $1.50$ | $+0.00$ | $+0.1$ |
| $0.110$ | $1.65$ | $+0.15$ | $+10.1$ |

A $10\%$ velocity error is a $10\%$ depth error, and nothing in the section
shows it. This is the single most common failure in utility mapping: a strike
that hits a service $0.15\ \mathrm{m}$ from where it was marked.

## 4. Physical interpretation

- The **hyperbola is geometric**: it says nothing about what the target is. Size,
  shape, material and fill must come from the amplitude, from the pattern, or
  from another method.
- **Amplitude is a contrast, never a material.** Air and water voids give the
  same magnitude with opposite sign; plastic is weak; metal is $R = -1$.
- **Small targets are a dynamic-range problem** ($a^3$), **extended targets a
  footprint problem** ($r_f$), and **thin layers a waveform problem** (the next
  lesson). Three different questions, three different equations.
- **The velocity is the deliverable's weak link.** It is invisible on the
  section, it is poorly constrained by a short aperture, and it multiplies every
  depth.
- **Disturbed ground is a pattern target.** A grave or a pit changes
  $\varepsilon_r$ and $\sigma$ by a few per cent and destroys the natural
  stratification; its signature is the *absence* of the expected layering plus a
  diffuse amplitude change, not a hyperbola. Quantitatively, a $5\%$ change in
  $\varepsilon_r$ at a contact gives $R \approx 0.012$, i.e. $-38\ \mathrm{dB}$,
  which is detectable only with a good dynamic range and is indistinguishable from
  a moisture change. Honest reporting of that case names the pattern, not a
  reflector.

## 5. Worked examples

### Example 1 — velocity, depth and the aperture

A hyperbola is picked over $x = \pm1.5\ \mathrm{m}$ at $0.05\ \mathrm{m}$
spacing with a $0.15\ \mathrm{ns}$ pick error, giving
$t_0 = 30.0\ \mathrm{ns}$ and $t(\pm1.5) = 44.7\ \mathrm{ns}$.

1. Fit $t^2$ against $x^2$: $x^2$ values $0 \ldots 2.25\ \mathrm{m^2}$,
   $t^2$ values $900 \ldots 1998\ \mathrm{ns^2}$.
2. Slope $m = (1998-900)/2.25 = 488.0\ \mathrm{ns^2\,m^{-2}}$, so
   $v = 2/\sqrt{488.0} = 0.0905\ \mathrm{m\,ns^{-1}}$.
3. Intercept $c = 900\ \mathrm{ns^2}$, so
   $z = \sqrt{900}(0.0905)/2 = 30.0(0.0905)/2 = 1.358\ \mathrm{m}$.
4. The implied permittivity is $\varepsilon_r = (c/v)^2 = (0.299792458/0.0905)^2
   = 10.97$, against $9.0$ from a common-midpoint sounding farther along the same
   line. The hyperbola velocity is therefore $10\%$ too low, and a trench
   confirms the target is at $z = 1.50\ \mathrm{m}$, so the depth is $10\%$ too
   low as well.

The check that catches this is the **flat reflection from a known layer** or an
independent CMP velocity: if the section also contains a horizontal reflector at a
depth known from a borehole or a trench, its two-way time fixes $v$
independently, and the hyperbola then only has to supply the depth. With the CMP
velocity $v = 0.0999\ \mathrm{m\,ns^{-1}}$, the same apex time gives
$z = 0.0999(30.0)/2 = 1.499\ \mathrm{m}$ — the right answer from the same pick.

### Example 2 — the depth of a utility

A service is struck at $t_0 = 42.0\ \mathrm{ns}$ at an offset of
$0.6\ \mathrm{m}$ from the marked line. Two velocity estimates are available:
from a hyperbola over a $\pm2\ \mathrm{m}$ aperture, $v = 0.085\
\mathrm{m\,ns^{-1}}$ with a $10\%$ uncertainty; from a common-midpoint sounding,
$v = 0.092\ \mathrm{m\,ns^{-1}}$ with a $4\%$ uncertainty.

1. Depth from the hyperbola velocity:
   $z = 0.085(42.0)/2 = 1.785\ \mathrm{m}$, uncertainty $\pm0.179\ \mathrm{m}$.
2. Depth from the CMP velocity:
   $z = 0.092(42.0)/2 = 1.932\ \mathrm{m}$, uncertainty $\pm0.077\ \mathrm{m}$.
3. The two estimates differ by $0.147\ \mathrm{m}$, which is within the combined
   uncertainty of the hyperbola estimate — so the honest report is
   $1.79$–$1.93\ \mathrm{m}$, and a single number would be a false precision.
4. The offset of $0.6\ \mathrm{m}$ matters: it is the *plan position* that is
   $0.6\ \mathrm{m}$ off the mark, and it is measured directly (not through a
   velocity), so it is the more reliable of the two coordinates.

### Example 3 — will a small target be seen?

A survey must detect a $20\ \mathrm{mm}$ feature in a soil with
$\varepsilon_r = 9$ at $500\ \mathrm{MHz}$, with a system whose dynamic range is
$80\ \mathrm{dB}$ and whose noise floor is $60\ \mathrm{dB}$ below the surface
echo.

1. Compare with a $40\ \mathrm{mm}$ reference at the same depth: $
   (0.02/0.04)^3 = 0.125$, i.e. $-18.1\ \mathrm{dB}$.
2. If the $40\ \mathrm{mm}$ feature returns at $-25\ \mathrm{dB}$ relative to the
   surface echo, the $20\ \mathrm{mm}$ one returns at $-43.1\ \mathrm{dB}$, i.e.
   $17\ \mathrm{dB}$ above the noise floor. **Detectable.**
3. Raising the frequency to $1000\ \mathrm{MHz}$ adds $20\log_{10}(2^2) =
   +12.0\ \mathrm{dB}$ from the $f^2$ term — but the absorption in this soil also
   rises, and the penetration falls. The two effects must be computed, not
   assumed to cancel.

The numbers are SYNTHETIC; the structure of the calculation is the point. An
answer of the form "we used $500\ \mathrm{MHz}$, which resolves $0.2\ \mathrm{m}$,
so a $20\ \mathrm{mm}$ target is fine" is wrong twice: it uses the Fresnel zone as
a resolution limit, and it ignores the cubic size dependence.

## 6. Assumptions and regime of validity

1. **A point scatterer for the hyperbola.** A target comparable with the Fresnel
   zone gives a mounded or flat event, not a hyperbola, and fitting a hyperbola to
   it returns a velocity that is too high.
2. **A single, uniform velocity above the target.** A layered or laterally
   varying overburden makes the event non-hyperbolic; the fit then returns an
   effective velocity that depends on the aperture.
3. **Coincident transmitter and receiver (monostatic geometry).** In bistatic
   operation the path is not $2\sqrt{x^2+z^2}$, and the hyperbola is asymmetric;
   the same fitting equation gives a biased velocity.
4. **Rayleigh scattering for small targets.** $ka \ll 1$; the $a^3f^2$ law fails
   as the target approaches the wavelength, and the transition is smooth rather
   than a switch.
5. **A smooth, horizontal reflector for $r_f$.** Roughness and dip both enlarge
   the effective footprint.
6. **Kinematic migration.** The summation in Section 3.4 ignores amplitude,
   transmission loss through the overburden and the antenna pattern, so the
   migrated amplitudes are not reflectivities. The migration velocity is the only
   physical parameter it estimates.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| offset, depth, aperture | $x, z, a$ | m | — |
| speed | $v$ | $\mathrm{m\,ns^{-1}}$ | $2/\sqrt{m}$ with $m$ in $\mathrm{ns^2\,m^{-2}}$ |
| two-way time | $t$ | ns | $2\sqrt{x^2+z^2}/v$ |
| Fresnel radius | $r_f$ | m | $\sqrt{\mathrm{m}\times\mathrm{m}}$ |
| slope of $t^2$ vs $x^2$ | $m$ | $\mathrm{ns^2\,m^{-2}}$ | — |
| reflection coefficient | $R$ | dimensionless | ratio of amplitudes |

The slope has the mildly alarming unit $\mathrm{ns^2\,m^{-2}}$, which is what
makes $v = 2/\sqrt m$ come out in $\mathrm{m\,ns^{-1}}$: the reciprocal of the
square root of time-squared per length-squared is length per time.

## 8. Python demonstration

[`code/gpr_archaeology_forensics_demo.py`](code/gpr_archaeology_forensics_demo.py)
prints every number quoted above:

1. a Monte Carlo hyperbola fit at a long and a short aperture, returning the
   velocity, the depth and their correlation ($+0.948$ and $+0.999$);
2. reflection coefficients for five target types in one host;
3. the Rayleigh $a^3$ amplitude table, $-18.1\ \mathrm{dB}$ per halving of radius;
4. the Fresnel radius at three frequencies and three depths;
5. a Kirchhoff migration of a synthetic hyperbola at the correct velocity and
   $\pm20\%$ from it, measuring the focus (peak $0.6495$ against $0.0809$);
6. the linear $z = vt/2$ depth error versus assumed velocity.

The demo is print-only, uses the fixed seed `20261014`, needs no network, and
exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-gpr-archaeology-forensics-exercises.md`](exercises/03-gpr-archaeology-forensics-exercises.md)
and
[`exercises/03-gpr-archaeology-forensics-solutions.md`](exercises/03-gpr-archaeology-forensics-solutions.md).

- **★** A hyperbola apex is at $t_0 = 24.0\ \mathrm{ns}$ and at
  $x = 1.0\ \mathrm{m}$ the time is $33.6\ \mathrm{ns}$. Compute $v$ and $z$.
- **★★** A $0.5$ m deep air void and a $0.5\ \mathrm{m}$ deep water-filled void
  are in the same soil ($\varepsilon_r = 12$). Compute both reflection
  coefficients and both echo amplitudes in dB, and state how the two are
  distinguished in practice.
- **★★★** Design a utility-mapping procedure that reports a service depth to
  $\pm0.15\ \mathrm{m}$, naming the velocity measurement, the aperture and the
  reason for each choice.

## 10. Further reading

- **Conyers, L. B. (2013). *Ground-Penetrating Radar for Archaeology* (3rd ed.).
  AltaMira Press.** Level: practitioner textbook. The standard treatment of
  survey design, hyperbola analysis and interpretation in archaeology.
- **Daniels, D. J. (ed.) (2004). *Ground Penetrating Radar* (2nd ed.).
  Institution of Engineering and Technology.** Level: reference. System design,
  antenna behaviour and the amplitude calibrations that Section 3.3 assumes.
- **Annan, A. P. (2009). Electromagnetic principles of ground penetrating radar.
  In H. M. Jol (ed.), *Ground Penetrating Radar: Theory and Applications*,
  Elsevier.** Level: research/reference. The clearest short statement of the
  amplitude and coupling systematics behind every "bright" or "weak" claim.
- **Neal, A. (2004). Ground-penetrating radar and its use in sedimentology.
  *Earth-Science Reviews*, 66.** Level: research. Useful for the forensic
  pattern-interpretation problem, where the target is disturbed stratigraphy.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A $250\ \mathrm{MHz}$ survey in a soil of $\varepsilon_r = 9.0$ images a
> hyperbola over $x = \pm0.5\ \mathrm{m}$ with an apex time of
> $30.0\ \mathrm{ns}$. **(a)** Compute the wavelength and the Fresnel radius at
> the target's depth for the true velocity. **(b)** The aperture is increased to
> $\pm2\ \mathrm{m}$; state what improves and what does not, with the numbers from
> the lesson. **(c)** A second, water-filled pipe is recorded at the same two-way
> time; compute the reflection coefficient of each if the first is air-filled,
> and state what else must be measured to tell them apart. **(d)** A
> $15\ \mathrm{mm}$ target is expected at the same depth as a detected
> $30\ \mathrm{mm}$ one. Compute the amplitude ratio in dB and state whether a
> $70\ \mathrm{dB}$ dynamic range is enough if the larger target sits $30\
\mathrm{dB}$ above the noise. **(e)** State the two sentences you would write in
> a report to prevent a reader from treating the depth as exact.

Worked versions of (a)–(c) are in the
[solutions](exercises/03-gpr-archaeology-forensics-solutions.md).

## Common pitfalls

1. **Fitting a hyperbola over a short aperture and quoting a velocity.** The
   correlation with the depth reaches $+0.999$; the pair is one number.
2. **Treating the Fresnel zone as the resolution limit.** $r_f$ is the detection
   footprint; separating two targets depends on the contrast and the noise too.
3. **Reporting a depth without its velocity.** $\delta z/z = \delta v/v$ exactly,
   and the section cannot show it.
4. **Reading the fill as the material.** An air-filled plastic pipe is a strong
   reflector; a water-filled one is weak and opposite in sign.
5. **Using geometric reasoning for small targets.** Below $ka \sim 1$ the
   amplitude falls as $a^3$; halving the radius costs $18\ \mathrm{dB}$.
6. **Claiming a migrated image is a reflectivity section.** Kirchhoff summation
   estimates geometry, not amplitude.

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the speed, resolution
  and amplitude physics.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md)
  — grid design, gain, filtering and the migration used here.
- [10-03 GPR Applications](./README.md) — the other applications of the same
  measurement.
- [11-06 Geotechnical and Engineering Exploration](../../11-exploration-geophysics/06-geotechnical-and-engineering/README.md)
  — buried-object and unexploded-ordnance detection at exploration scale.
- [23-04 Electrical and EM Fieldwork](../../23-field-methods-instruments/04-electrical-em-fieldwork/README.md)
  — the acquisition practicalities of the surveys described here.

## Code and exercises

| Path | Contents |
|---|---|
| [`code/gpr_archaeology_forensics_demo.py`](code/gpr_archaeology_forensics_demo.py) | The six computations of Section 8 |
| [`exercises/03-gpr-archaeology-forensics-exercises.md`](exercises/03-gpr-archaeology-forensics-exercises.md) | Graded problems |
| [`exercises/03-gpr-archaeology-forensics-solutions.md`](exercises/03-gpr-archaeology-forensics-solutions.md) | Worked solutions |

```bash
cd 10-gpr-near-surface/03-gpr-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_archaeology_forensics_demo.py
```
