---
id: 10-03-04
title: "GPR for Pavements, Concrete and Infrastructure Inspection"
level: advanced
prereqs: ["10-01-01", "10-01-02", "10-01-05", "10-03-03"]
tags: [gpr, near-surface, geotechnical, pavement, concrete, infrastructure, thin-layer, rebar]
---

# GPR for Pavements, Concrete and Infrastructure Inspection

**All models and data in this module are SYNTHETIC.** The layer thicknesses,
permittivities, cover depths, bar spacings and pick errors are chosen teaching
values. No road, bridge deck, runway or building is described here. Physical
constants and standard material permittivities are labelled as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the layer thickness relation $h = vt/2$ and its exact sensitivity
   $\mathrm{d}h/h = -\mathrm{d}\varepsilon_r/(2\varepsilon_r)$, and **compute**
   the thickness error contributed by an assumed permittivity.
2. **Derive** the metal plate (or metal plate equivalent) calibration
   $\varepsilon_r = ((1-R)/(1+R))^2$ from the surface reflection, and **propagate**
   an amplitude error into a thickness error.
3. **Derive** the exact three-layer reflection response of a slab, **verify** it
   against the half-space limit, and **explain** the non-monotonic
   amplitude–thickness relation of a layer thinner than $\lambda/4$.
4. **Demonstrate** that one amplitude can belong to several thicknesses, and
   **state** what additional information breaks the ambiguity.
5. **Compute** rebar cover depth and spacing from diffraction apexes, and
   **distinguish** the part of the answer that needs a velocity from the part that
   does not.
6. **Compute** where a layer multiple lands and **explain** how it differs from a
   real deeper interface.
7. **Assemble** an infrastructure thickness budget with the permittivity term
   dominant, and **decide** whether the result meets a stated paving tolerance.

## Prerequisites

- [10-01-01 GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](../01-gpr-principles/01-gpr-physics.md)
  — permittivity, the reflection coefficient and the source pulse.
- [10-01-02 Velocity Estimation and Depth Conversion](../01-gpr-principles/02-gpr-velocity-and-depth.md)
  — the two-way time and the depth conversion.
- [10-01-05 Vertical and Horizontal Resolution Limits](../01-gpr-principles/05-gpr-resolution.md)
  — the $\lambda/4$ limit and the Fresnel zone.
- [10-03-03 GPR in Archaeology, Forensics and Buried Utilities](03-gpr-archaeology-forensics.md)
  — hyperbola geometry and the aperture result reused for rebar.

## 1. Intuition: a calibration problem with a built-in answer

Pavement and concrete inspection is the most quantitative routine application of
GPR, for one reason: **the geometry is right**. The layers are flat, horizontal
and thin; the antenna is moved on the surface; and the material permittivities sit
in a narrow range. Under those conditions a two-way time converts to a thickness
with one arithmetic step, and the method is used to control construction rather
than to explore.

The uncertainty is entirely in the permittivity, and it has a standard remedy. A
metal plate laid on the surface reflects almost all the energy with a known
coefficient ($R \to -1$), so the *ratio* of the surface reflection to the plate
reflection gives the surface permittivity algebraically, on site, per layer. That
single trick converts an assumed permittivity into a measured one, and it is the
difference between a survey that can certify a $100\ \mathrm{mm}$ layer to a few
millimetres and one that cannot.

This lesson also contains the cleanest example in the folder of an **ill-posed
amplitude problem**. A layer thinner than a quarter wavelength does not produce
two echoes. It produces one composite wavelet whose amplitude depends on the
thickness, on the permittivity, on the contrast with the layer below and on the
shape of the source pulse. The demonstration shows the same amplitude arising at
$12.0$, $30.0$, $50.0$ and $51.0\ \mathrm{mm}$. An amplitude is not a thickness.

## 2. Precise definitions

| Quantity | Symbol | Meaning | Unit |
|---|---|---|---|
| layer thickness | $h$ | the target | m |
| two-way time | $t$ | picked from the section | ns |
| permittivity | $\varepsilon_r$ | of the layer | dimensionless |
| surface reflection | $R_s$ | air-to-layer amplitude ratio | dimensionless |
| plate reference | $R_{\mathrm{plate}}$ | $\approx -1$ | dimensionless |
| tuning thickness | $h_t$ | where the slab response is extremal | m |
| cover depth | $c$ | concrete above a bar | m |
| layer multiple | $\tau_m$ | $2\times$ the primary time | ns |

**Metal plate calibration.** A metal plate at the surface returns $R = -1$ with
the same antenna and geometry, so it calibrates the system response; the surface
reflection measured against it is $R_s$, and $R_s$ inverts to $\varepsilon_r$.

**Tuning thickness.** The thickness at which the two interface reflections of a
slab interfere most strongly at the dominant frequency. It is of order
$\lambda/4$, but its exact value depends on the sign and size of both interface
coefficients and on the source spectrum — as the demonstration shows, it is
$20\ \mathrm{mm}$ for both the wet and the dry base used here, while $\lambda/4$
is $23.6\ \mathrm{mm}$.

## 3. Derivations

### 3.1 Thickness and its permittivity sensitivity

$$h = \frac{vt}{2}, \qquad v = \frac{c}{\sqrt{\varepsilon_r}}
\;\Rightarrow\; h = \frac{c\,t}{2\sqrt{\varepsilon_r}}.$$

$$\frac{\mathrm{d}h}{h} = -\frac{1}{2}\frac{\mathrm{d}\varepsilon_r}{\varepsilon_r}
\qquad \mathrm{(at\ fixed\ }t\mathrm{)}.$$

*Numerical check.* A $+5\%$ permittivity error gives
$1/\sqrt{1.05}-1 = -2.41\%$. The demonstration's table, one measured time of
$1.00\ \mathrm{ns}$ and four assumed permittivities:

| assumed $\varepsilon_r$ | $h$ (mm) | error against $\varepsilon_r = 4.5$ (mm) |
|---|---|---|
| $4.0$ | $74.9$ | $+4.3$ |
| $4.5$ | $70.7$ | $0.0$ |
| $5.0$ | $67.0$ | $-3.6$ |
| $5.5$ | $63.9$ | $-6.7$ |

**A $37\%$ spread of permittivity — the full plausible range for a compacted
asphalt — spans $11\ \mathrm{mm}$ of a $70\ \mathrm{mm}$ layer, i.e. $16\%$.** No
picking accuracy recovers that; only a measurement of $\varepsilon_r$ does.

### 3.2 The metal plate calibration, derived and inverted

With medium 1 = air ($\varepsilon_r = 1$) and medium 2 = the layer,

$$R_s = \frac{\sqrt{1}-\sqrt{\varepsilon_r}}{\sqrt{1}+\sqrt{\varepsilon_r}}
= \frac{1-n}{1+n}, \qquad n = \sqrt{\varepsilon_r}.$$

Solve for $n$:

$$n = \frac{1-R_s}{1+R_s}
\;\Rightarrow\;
\varepsilon_r = \left(\frac{1-R_s}{1+R_s}\right)^{2}.$$

*Worked values.* For $\varepsilon_r = 4.0$, $4.5$, $5.5$, $9.0$ the coefficients
are $-0.3333$, $-0.3592$, $-0.4021$, $-0.5000$, and the inversion returns the
input exactly in every case (the demonstration checks the round trip
algebraically: `True` for all four).

**Error propagation.** Differentiate the inversion:

$$\frac{\mathrm{d}\varepsilon_r}{\varepsilon_r} = \frac{4\,\mathrm{d}R_s}{1-R_s^{2}}.$$

For $R_s = -0.3592$, $1-R_s^2 = 0.8710$:

| amplitude error in $R_s$ | $\mathrm{d}\varepsilon_r/\varepsilon_r$ | thickness error |
|---|---|---|
| $0.01$ | $4.59\%$ | $2.30\%$ |
| $0.02$ | $9.19\%$ | $4.59\%$ |
| $0.05$ | $22.96\%$ | $11.48\%$ |

The amplification factor $4/(1-R_s^2)$ is between $4$ and $4.6$ in the range of
road materials, so **an amplitude error in the calibration costs about four times
as much in permittivity and twice as much in thickness**. The method is only as
good as the amplitude calibration — which is why the metal plate is used on the
surface at each layer, not once at the start of the day.

### 3.3 The exact slab response, and the thin-layer ambiguity

Consider a slab of thickness $h$ and velocity $v$ between an upper medium and a
lower medium. At normal incidence the total reflection coefficient is the sum of
all multiple reflections:

$$r = r_{01} + t_{01}t_{10}r_{12}e^{-i\phi} + t_{01}t_{10}r_{12}^2 r_{10}e^{-2i\phi} + \cdots,$$

with $\phi = 2\omega h/v$ the two-way phase across the slab. Summing the geometric
series and using $t_{01}t_{10} = 1-r_{01}^2$:

$$r(\omega) = \frac{r_{01} + r_{12}e^{-i\phi}}{1 + r_{01}r_{12}e^{-i\phi}}.$$

**Check on the limit $h \to 0$** ($\phi \to 0$): $r \to (r_{01}+r_{12})/(1+r_{01}r_{12})$,
which is algebraically identical to the direct half-space coefficient $r_{02}$.
Numerically, the demonstration's air/asphalt/wet-base case ($r_{01} = -0.3592$,
$r_{12} = -0.1716$) returns $0.5000$ against the exact
$|r_{02}| = |(1-\sqrt{9})/(1+\sqrt{9})| = 0.5000$. **That is an exact check on the
whole implementation.**

**Measured thickness dependence** (asphalt $\varepsilon_r = 4.5$,
$f_0 = 1.5\ \mathrm{GHz}$, so $\lambda = 94.2\ \mathrm{mm}$ and
$\lambda/4 = 23.6\ \mathrm{mm}$):

| $h$ (mm) | two-way time (ns) | p2p, wet base | p2p, dry base |
|---|---|---|---|
| $5$ | $0.071$ | $0.4730$ | $0.3104$ |
| $10$ | $0.142$ | $0.4015$ | $0.3871$ |
| $15$ | $0.212$ | $0.3314$ | $0.4362$ |
| $20$ | $0.283$ | $0.3165$ | $0.4441$ |
| $24$ | $0.340$ | $0.3278$ | $0.4236$ |
| $30$ | $0.425$ | $0.3691$ | $0.3714$ |
| $40$ | $0.566$ | $0.4001$ | $0.3599$ |
| $90$ | $1.274$ | $0.3592$ | $0.3592$ |

(p2p is normalised to the response of a perfect reflector, so it is an
amplitude ratio, dimensionless.)

Three readings:

- **Near $\lambda/4$ the interference is strongest, and its direction is set by
  the sign of the base contrast.** The wet base (base reflection of the same sign
  as the surface reflection) gives a *minimum* of $0.3165$ at $20\ \mathrm{mm}$,
  $12\%$ below the asymptote; the dry base gives a *maximum* of $0.4441$, $24\%$
  above it. Whether a quarter-wave layer looks bright or dim depends on material
  you cannot see.
- **For $h$ well above $\lambda/4$ the two echoes separate in time** and the
  composite amplitude converges on the surface coefficient alone, $0.3592$ at
  $60$–$90\ \mathrm{mm}$. That is a second, independent check on the
  implementation.
- **Below $\lambda/4$ the amplitude is not a thickness measurement.** The
  demonstration searches the amplitude–thickness curve for every thickness
  returning the same p2p ($0.3691 \pm 0.002$) and finds
  **$12.0$, $30.0$, $50.0$ and $51.0\ \mathrm{mm}$** — a factor of $4$ in
  thickness and, at $50\ \mathrm{mm}$, three times the true two-way time. Nothing
  in the amplitude separates them without an independent constraint.

### 3.4 Rebar: what the geometry gives for free

Rebar in concrete reflects as a diffraction hyperbola of the same form as any
point scatterer, so

$$t^2 = \frac{4}{v^2}x^2 + \frac{4c^2}{v^2}, \qquad c\ \mathrm{the\ cover\ depth}.$$

- The **spacing** of the bars is the distance between apexes. It is a property of
  the trace positions, so it needs no velocity at all and is limited only by the
  pick of each apex.
- The **cover depth** is $v t_0/2$, which needs the velocity; the velocity comes
  from the hyperbola curvature, and its uncertainty is the aperture-limited one
  from the previous lesson.

The demonstration's SYNTHETIC deck: $\varepsilon_r = 6.0$, so
$v = 0.1224\ \mathrm{m\,ns^{-1}}$; cover $60\ \mathrm{mm}$; spacing
$150\ \mathrm{mm}$:

| offset (m) | two-way time (ns) | depth if $v$ is right (mm) |
|---|---|---|
| $0.00$ | $0.98$ | $60.0$ |
| $0.05$ | $1.28$ | $78.1$ |
| $0.10$ | $1.91$ | $116.6$ |
| $0.15$ | $2.64$ | $161.6$ |
| $0.20$ | $3.41$ | $208.8$ |
| $0.30$ | $5.00$ | $305.9$ |

Fitting $t^2$ against $x^2$ over a $\pm0.30\ \mathrm{m}$ aperture with a
$0.02\ \mathrm{ns}$ picking error gives, by Monte Carlo of $4000$ realisations,

$$v = 0.1224 \pm 0.0011\ \mathrm{m\,ns^{-1}}\ (0.9\%), \qquad
c = 60.0 \pm 1.5\ \mathrm{mm}\ (2.6\%).$$

Note that the depth column of the table is the *hyperbola*, not a bar at that
depth: at $0.15\ \mathrm{m}$ offset the event appears at an equivalent depth of
$161.6\ \mathrm{mm}$, which is the classic misreading of a rebar map. The
horizontal position of a bar is its apex, never the wide part of its hyperbola.

### 3.5 Multiples: where they land

The layer multiple has traced the slab twice, so its two-way time is twice the
primary time, $\tau_m = 2\tau$. Converting it as if it were a primary gives an
apparent depth of $2h$:

| slab (mm) | primary (ns) | multiple (ns) | apparent depth of the multiple as a primary (mm) |
|---|---|---|---|
| $30$ | $0.425$ | $0.849$ | $60.0$ |
| $60$ | $0.849$ | $1.698$ | $120.0$ |
| $90$ | $1.274$ | $2.547$ | $180.0$ |
| $140$ | $1.981$ | $3.963$ | $280.0$ |

Nothing about a multiple's travel time distinguishes it from a primary; the
separation is kinematic and diagnostic: a multiple of a shallow layer inherits the
moveout of that layer (larger, because it has travelled further in the slow upper
medium) and it disappears if the upper interface is removed. On a road section,
where the layers below are often at comparable times, this is the single most
common mis-pick.

## 4. Physical interpretation

- **A thickness is a time divided by a velocity**, and the velocity comes from the
  permittivity, which is measured on site. Everything else in this lesson is
  error propagation.
- **Thin layers are an inverse problem, not a measurement.** The amplitude carries
  the product of thickness and contrast, and its non-monotonic dependence means one
  amplitude maps to several thicknesses.
- **Rebar gives a free geometric measurement (spacing) and a velocity-limited one
  (cover).** Reporting the spacing as if it had the same status as the cover depth
  overstates the survey.
- **Multiples are not noise.** They are the strongest events on a thin-layer
  section, and they are recognised by their moveout and their dependence on the
  layer above, not by their time.
- **The inverse-scattering view.** The exact slab response of Section 3.3 is the
  forward operator of a one-dimensional inverse problem; reading the thickness out
  of a composite wavelet is deconvolution, and the ambiguity measured there is the
  null space of that operator for thin layers.

## 5. Worked examples

### Example 1 — metal plate calibration end to end

A $1.5\ \mathrm{GHz}$ antenna on a new asphalt layer. The plate response has p2p
amplitude $1.00$ (by definition); the surface reflection has p2p $0.36$, negative
polarity.

1. $R_s = -0.36$.
2. $\varepsilon_r = ((1-(-0.36))/(1+(-0.36)))^2 = (1.36/0.64)^2 = 2.125^2 = 4.516$.
3. $v = 0.299792458/\sqrt{4.516} = 0.14107\ \mathrm{m\,ns^{-1}}$.
4. The base reflection is picked at $t = 1.40\ \mathrm{ns}$, so
   $h = 0.14107(1.40)/2 = 0.09875\ \mathrm{m} = 98.8\ \mathrm{mm}$.
5. Suppose the amplitude had been read as $0.38$ instead of $0.36$: then
   $\varepsilon_r = (1.38/0.62)^2 = 4.954$, $v = 0.13469\ \mathrm{m\,ns^{-1}}$ and
   $h = 94.3\ \mathrm{mm}$ — a $4.5\ \mathrm{mm}$ change in the reported thickness
   from a $0.02$ amplitude error, consistent with the $4.59\%$ rule of Section 3.2.

### Example 2 — a thin overlay, honestly reported

A $20\ \mathrm{mm}$ overlay on a wet base is surveyed with the same antenna. The
event is a single composite wavelet of p2p $0.3165$ (from Section 3.3), i.e.
$12\%$ below the value $0.3592$ that a thick asphalt would give.

1. If the analyst assumes the layer is thick and reads the amplitude as a
   permittivity, the calibration returns
   $\varepsilon_r = ((1+0.3165)/(1-0.3165))^2 = (1.3165/0.6835)^2 = 3.709$, against
   a plate-measured $4.5$ — a $18\%$ discrepancy that is the *warning sign*.
2. With the plate calibration fixed at $4.5$, the amplitude is not a thickness, as
   Section 3.3 shows.
3. The honest report: "two-way time $0.28\ \mathrm{ns}$; the event is a composite
   wavelet; a slab model with the plate-calibrated permittivity and a base
   contrast of $0.17$ gives $h = 20 \pm 6\ \mathrm{mm}$, where the interval is the
   model's admitted range, not a picking error."

The important habit is in step 1: **the plate calibration and the layer
amplitude must agree**. When they do not, the layer is thin, or the base contrast
is not what was assumed, or the surface is rough — and all three are information.

### Example 3 — a rebar survey error budget

A deck with $\varepsilon_r = 6.0$, bars at $150\ \mathrm{mm}$ spacing, and a
$0.02\ \mathrm{ns}$ picking error.

1. **Spacing.** The apexes are $150\ \mathrm{mm}$ apart, and the measurement
   error is the pick error in horizontal position, i.e. bounded by the trace
   spacing (say $25\ \mathrm{mm}$). Velocity does not enter: $150 \pm 25\ \mathrm{mm}$
   is an honest statement.
2. **Cover depth.** From the fit, $c = 60.0 \pm 1.5\ \mathrm{mm}$ at $1\sigma$. The
   two contributions are $v\sigma_t/2 = 0.1224(0.02)/2 = 1.22\ \mathrm{mm}$ from
   picking and $c\,\sigma_v/v = 60.0(0.009) = 0.54\ \mathrm{mm}$ from the velocity.
   Their quadrature sum is $1.33\ \mathrm{mm}$, so the Monte Carlo's
   $1.5\ \mathrm{mm}$ is larger than the sum of the terms — the excess is the
   correlation between the fitted velocity and depth (the previous lesson's
   $+0.999$), which makes the pair's errors add rather than cancel.
3. **What would break it.** A wet patch changes $\varepsilon_r$ locally from
   $6.0$ to, say, $8.0$, which changes the apex time for the same cover by
   $\sqrt{6/8} = 0.866$, i.e. $-13\%$ in time and $+15\%$ in inferred cover if the
   permittivity is not updated. Local moisture is the dominant practical error in
   cover-depth surveys, and it is larger than either of the two terms above.

## 6. Assumptions and regime of validity

1. **Plane, parallel, horizontal layers.** Any of the three violations mixes the
   neighbouring reflections into the pick and invalidates the one-dimensional
   response of Section 3.3.
2. **Normal incidence and a known, stable antenna response.** The metal plate
   calibration is valid only if the antenna coupling is unchanged between the
   plate measurement and the survey; a change of surface (from asphalt to
   concrete) requires a new plate measurement.
3. **Low loss.** $\tan\delta \ll 1$; wet chloride-contaminated concrete violates
   it, and the effect is both a slower speed and a lower amplitude — the two are
   not separable from a single trace.
4. **A slab model for thin layers.** The exact response assumes sharp interfaces
   and a homogeneous slab. A graded overlay (a chip seal, a tack coat) is a
   continuous permittivity profile, whose response is the integral of Section 3.3
   and is *even more* ambiguous.
5. **A point scatterer for the rebar hyperbola.** Adjacent bars interact when the
   spacing approaches the cover depth, and the individual hyperbolas merge.
6. **No dispersion.** The permittivity of a wet material is frequency-dependent;
   the single-permittivity calibration is an average over the antenna band.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| thickness | $h$ | mm | $vt/2$ with $v$ in m/ns, $t$ in ns |
| two-way time | $t$ | ns | — |
| permittivity | $\varepsilon_r$ | dimensionless | $((1-R)/(1+R))^2$ |
| reflection coefficient | $R$ | dimensionless | ratio of amplitudes |
| two-way phase | $\phi$ | rad | $2\omega h/v$, dimensionless argument |
| frequency | $f_0$ | GHz | $1\ \mathrm{GHz} = 1\ \mathrm{ns^{-1}}$ |

The last row is the reason infrastructure GPR uses GHz: a $1.5\ \mathrm{GHz}$
antenna has a period of $0.67\ \mathrm{ns}$, so a $100\ \mathrm{mm}$ layer at
$0.14\ \mathrm{m\,ns^{-1}}$ produces a $1.4\ \mathrm{ns}$ two-way time — two
cycles, comfortably resolvable. At $250\ \mathrm{MHz}$ the same layer is a third
of a cycle and the measurement becomes the inverse problem of Section 3.3.

## 8. Python demonstration

[`code/gpr_roads_concrete_demo.py`](code/gpr_roads_concrete_demo.py) prints every
number quoted above:

1. the thickness table and the $-2.41\%$ sensitivity for a $+5\%$ permittivity
   error;
2. the metal plate inversion with an exact round-trip check for four
   permittivities, and the $4/(1-R^2)$ amplification of an amplitude error;
3. the exact three-layer slab response: the $h \to 0$ limit against the
   half-space coefficient ($0.5000$ against $0.5000$), the thickness table for a
   wet and a dry base, the $\lambda/4$ comparison, and the four thicknesses that
   return one amplitude;
4. a rebar hyperbola table with a Monte Carlo fit giving
   $v = 0.1224 \pm 0.0011\ \mathrm{m\,ns^{-1}}$ and
   $c = 60.0 \pm 1.5\ \mathrm{mm}$;
5. the multiple times and their apparent depths;
6. a Monte Carlo thickness budget ($99.0 \pm 1.8\ \mathrm{mm}$ from a
   $3\%$ permittivity and a $1\%$ time error).

The demo is print-only, uses the fixed seed `20261014`, needs no network, and
exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-gpr-roads-concrete-exercises.md`](exercises/04-gpr-roads-concrete-exercises.md)
and
[`exercises/04-gpr-roads-concrete-solutions.md`](exercises/04-gpr-roads-concrete-solutions.md).

- **★** A surface reflection is measured at $R_s = -0.42$ against a metal plate.
  Compute $\varepsilon_r$, the speed and the thickness for a $1.20\ \mathrm{ns}$
  two-way time.
- **★★** For asphalt of $\varepsilon_r = 4.5$ at $1.5\ \mathrm{GHz}$, compute
  $\lambda$, $\lambda/4$, and decide whether a $15\ \mathrm{mm}$ layer can be
  measured as two echoes. Justify with the demonstration's table.
- **★★★** Design a quality-control procedure that certifies a $50\ \mathrm{mm}$
  asphalt layer to $\pm 3\ \mathrm{mm}$, stating the frequency, the calibration,
  and which error term limits the result.

## 10. Further reading

- **Saarenketo, T., & Scullion, T. (2000). Road evaluation with ground
  penetrating radar. *Journal of Applied Geophysics*, 43.** Level: research. The
  standard review of pavement applications, written from the practice side.
- **Al-Qadi, I. L., & Lahouar, S. (2005). Measuring layer thicknesses with GPR:
  theory to practice. *Construction and Building Materials*, 19.** Level:
  research. The calibration and accuracy question that Section 3.2 derives.
- **Lai, W. W.-L., Dérobert, X., & Annan, A. P. (2018). A review of Ground
  Penetrating Radar application in civil engineering. *NDT & E International*,
  96.** Level: research. A recent survey of the whole field, including bridge
  decks and the limits of amplitude methods.
- **Daniels, D. J. (ed.) (2004). *Ground Penetrating Radar* (2nd ed.).
  Institution of Engineering and Technology.** Level: reference. System and
  antenna behaviour behind the calibration.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A $1.5\ \mathrm{GHz}$ survey of a pavement gives a plate-referenced surface
> reflection of $R_s = -0.36$ and a base reflection at $1.40\ \mathrm{ns}$; the
> asphalt is $\varepsilon_r = 4.5$ and a further interface is picked at
> $2.80\ \mathrm{ns}$. **(a)** Compute the permittivity from $R_s$ and the
> thickness of the asphalt. **(b)** State the two candidate explanations of the
> $2.80\ \mathrm{ns}$ event and how you would separate them. **(c)** An overlay
> $15\ \mathrm{mm}$ thick is placed on top. Using the demonstration's table,
> state whether its two-way time is resolvable, and what the amplitude does near
> $\lambda/4$ for a wet base and for a dry base. **(d)** The surface amplitude is
> re-read as $0.34$. Compute the thickness change this causes and compare with
> the Section 3.2 rule. **(e)** State the one sentence a report must contain
> about the permittivity for the thickness to be defensible.

Worked versions of (a), (c) and (d) are in the
[solutions](exercises/04-gpr-roads-concrete-solutions.md).

## Common pitfalls

1. **Assuming the permittivity.** The full plausible range for asphalt costs
   $16\%$ of a $70\ \mathrm{mm}$ layer; the plate calibration is not optional.
2. **Using one calibration for a change of surface.** The plate reference is a
   coupling measurement, and coupling changes with the surface.
3. **Reading an amplitude as a thickness below $\lambda/4$.** One amplitude
   belongs to $12$, $30$, $50$ and $51\ \mathrm{mm}$ in the demonstration.
4. **Assuming a quarter-wave layer is bright.** The sign of the base contrast
   decides: the wet base gave a minimum, the dry base a maximum.
5. **Mis-picking a multiple as a deeper layer.** The layer multiple sits at twice
   the primary time and appears to be a reflector at twice the layer thickness.
6. **Reading the wide part of a rebar hyperbola as the bar's position.** The bar
   is at the apex; the flanks are geometry.

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — permittivity, the
  resolution limits and the source pulse.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md)
  — antenna choice, gain, deconvolution and migration for layered media.
- [10-03 GPR Applications](./README.md) — hydrogeology, glaciology,
  archaeology and planetary sounding with the same instrument.
- [11-06 Geotechnical and Engineering Exploration](../../11-exploration-geophysics/06-geotechnical-and-engineering/README.md)
  — the same measurements at larger scale, for tunnels, dams and foundations.
- [23-04 Electrical and EM Fieldwork](../../23-field-methods-instruments/04-electrical-em-fieldwork/README.md)
  — acquisition practice, including the metal plate and calibration workflow.

## Code and exercises

| Path | Contents |
|---|---|
| [`code/gpr_roads_concrete_demo.py`](code/gpr_roads_concrete_demo.py) | The six computations of Section 8 |
| [`exercises/04-gpr-roads-concrete-exercises.md`](exercises/04-gpr-roads-concrete-exercises.md) | Graded problems |
| [`exercises/04-gpr-roads-concrete-solutions.md`](exercises/04-gpr-roads-concrete-solutions.md) | Worked solutions |

```bash
cd 10-gpr-near-surface/03-gpr-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_roads_concrete_demo.py
```
