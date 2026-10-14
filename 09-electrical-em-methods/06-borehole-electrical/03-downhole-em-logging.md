---
id: 09-06-03
title: "Downhole EM Logging and Induction Tools"
level: graduate
prereqs: ["09-01-01", "09-05-02", "05-08-03"]
tags: [electrical-methods, borehole, induction-logging, skin-depth, resolution]
---

# Downhole EM Logging and Induction Tools

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the skin depth $\delta=\sqrt{2/(\omega\mu\sigma)}$ from the
   diffusive wave equation and **compute** it, and the induction number
   $p=L/\delta$, for a given tool spacing, frequency and formation resistivity.
2. **Derive** the exact homogeneous-medium mutual coupling of a coaxial
   two-coil system, $Z/Z_0 = (1+\mathrm{i}kL)\mathrm{e}^{-\mathrm{i}kL}$, and
   **obtain** its small-$p$ expansion.
3. **Distinguish** the in-phase and quadrature channels, **explain** why
   apparent conductivity is calibrated on the quadrature, and **quantify** the
   skin-effect bias of that calibration.
4. **Derive** Doll's geometric factor from the ring-flux identity and **compute**
   the vertical response of a two-coil sonde, including its flat top and its
   $1/z^{2}$ tails.
5. **Measure** the shoulder effect for a thin bed and **state** the vertical
   resolution of a sonde in terms of its spacing.
6. **Explain** why a conductivity log is not a lithology log, and **give** the
   several independent rock properties that conductivity mixes together.
7. **State** the assumptions — whole space, no borehole, no skin effect for the
   geometric-factor model, small induction number for the linear calibration —
   and the regime in which each fails.

## Prerequisites

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  what conductivity means for a rock, and its range in nature.
- [09-05-02 FEM Conductivity Mapping and Apparent Conductivity](../05-em-methods-applications/02-fem-conductivity-mapping.md) —
  apparent conductivity, and the induction-number language.
- [05-08-03 Resistivity Logging](../../05-core-geophysics/08-geophysical-logging/03-resistivity-logging.md) —
  the borehole measurement this lesson quantifies.

## 1. Intuition: what an induction tool measures

An induction tool is a set of coils on a sonde. A transmitter coil carries an
alternating current at a few tens of kilohertz; it does not need to touch the
formation. The alternating magnetic field induces **eddy currents** in the
conducting rock around the sonde, and those currents radiate a secondary field
that a receiver coil, some tens of centimetres to a metre away, measures as a
voltage.

Two facts follow from that description and they organise the whole lesson.

- The tool measures **conductivity**, not resistivity directly and not
  lithology. Its output is an apparent conductivity $\sigma_a$ — a weighted
  average, over a volume set by the coil spacing, of whatever conducts in the
  formation.
- The measurement is **resistive to the borehole** (no galvanic contact) but not
  immune to it: the borehole fluid, the invaded zone and the formation all
  conduct, and the tool averages them.

All models and data in this module are **SYNTHETIC**. Spacings, frequencies and
conductivities used below are chosen teaching values; no instrument model,
specification sheet or field log is referenced.

## 2. Skin depth and the induction number

### 2.1 The diffusion equation and the skin depth

At the frequencies of induction logging the displacement current is negligible
(we verify this in §2.3), so Ampère's law reads
$\nabla\times\mathbf{H} = \sigma\mathbf{E}$, and Faraday's law
$\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ gives, for time
dependence $\mathrm{e}^{\mathrm{i}\omega t}$,

$$\nabla^{2}\mathbf{E} = \mathrm{i}\omega\mu\sigma\,\mathbf{E}
\qquad\Longrightarrow\qquad k = \frac{1+\mathrm{i}}{\delta},
\qquad
\boxed{\;\delta = \sqrt{\frac{2}{\omega\mu\sigma}} = \sqrt{\frac{2\rho}{\omega\mu}}\;}
\quad[\mathrm{m}],$$

with $\rho = 1/\sigma$ in $\Omega\,\mathrm{m}$ and $\omega = 2\pi f$. Substituting
$\mu_0 = 1.2566370614\times10^{-6}\ \mathrm{H\,m^{-1}}$ gives the form used in
practice:

$$\delta = 503.2921\,\sqrt{\frac{\rho}{f}}\ \mathrm{m},
\qquad \rho\ \text{in}\ \Omega\,\mathrm{m},\ f\ \text{in Hz}.$$

*Numerical check.* The demonstration prints the factor
$\sqrt{2/(2\pi\mu_0)} = 503.2921$. For a 20 kHz tool in a
$10\ \Omega\,\mathrm{m}$ formation: $\delta = 503.2921\sqrt{10/20000} = 11.254\
\mathrm{m}$, and with a 1 m spacing the induction number is $p = L/\delta
= 0.0889$.

### 2.2 The induction number

$$p \equiv \frac{L}{\delta} = L\sqrt{\frac{\omega\mu_0\sigma}{2}} .$$

$p\ll1$ is the **induction** regime: the field varies slowly across the tool and
the response is close to linear in $\sigma$. $p\gtrsim1$ is the **wave** regime:
the field rotates appreciably across the tool, the response becomes
phase-shifted and non-linear, and the same reading can be produced by a
conductive thick body or a less conductive thin one. The demonstration's table
shows how quickly $p$ moves:

| $f$ | $\rho = 1\ \Omega\,$m | $\rho = 10$ | $\rho = 100$ |
|---|---|---|---|
| 1 kHz | $\delta = 15.92$ m, $p = 0.063$ | 50.33 m, 0.020 | 159.15 m, 0.006 |
| 10 kHz | 5.033 m, 0.199 | 15.92 m, 0.063 | 50.33 m, 0.020 |
| 20 kHz | 3.559 m, 0.281 | 11.25 m, 0.089 | 35.59 m, 0.028 |
| 100 kHz | 1.592 m, 0.628 | 5.033 m, 0.199 | 15.92 m, 0.063 |

### 2.3 Checking the neglect of displacement current

The ratio of conduction to displacement current is
$\sigma/(\omega\varepsilon) = 1/(\rho\,\omega\varepsilon)$. For
$\rho = 1\ \Omega\,\mathrm{m}$, $f = 20$ kHz and
$\varepsilon\approx10\varepsilon_0$:
$\omega\varepsilon = 1.2566\times10^{5}\times8.854\times10^{-11} = 1.11\times10^{-5}\
\mathrm{S\,m^{-1}}$ against $\sigma = 1\ \mathrm{S\,m^{-1}}$: a ratio of
$9\times10^{4}$. Displacement current is negligible for every formation of
interest, which is exactly why the induction problem is diffusive.

## 3. The exact homogeneous response of a coaxial coil pair

### 3.1 Derivation

For a magnetic dipole of moment $m$ along $z$ in a homogeneous medium of
wavenumber $k$, the Hertz-vector solution for the azimuthal electric field is

$$E_\varphi(r,\theta) = -\mathrm{i}\omega\mu\,\frac{m}{4\pi}\,
\sin\theta\,\frac{(1+\mathrm{i}kr)\,\mathrm{e}^{-\mathrm{i}kr}}{r^{2}} ,$$

which reduces to the magnetostatic dipole field as $k\to0$. A coaxial receiver
coil at axial distance $L$ (so $\theta = 90^\circ$, $\sin\theta = 1$) therefore
measures a voltage proportional to

$$\frac{Z}{Z_0} = (1+\mathrm{i}kL)\,\mathrm{e}^{-\mathrm{i}kL},$$

where $Z_0$ is the free-space coupling (the value the same pair would have in
vacuum). With $k = (1+\mathrm{i})/\delta$ and $p = L/\delta$,

$$kL = (1+\mathrm{i})p,\qquad
\boxed{\;\frac{Z}{Z_0} = (1-p+\mathrm{i}p)\,\mathrm{e}^{\,p-\mathrm{i}p}\;}$$

*Verification.* The demonstration confirms that the radial function
$(1+\mathrm{i}kr)\mathrm{e}^{-\mathrm{i}kr}/r^{2}$ satisfies the spherical radial
wave equation
$g'' + (2/r)g' + (k^{2}-2/r^{2})g = 0$ to finite-difference truncation
($3.5\times10^{-7}$ relative residual at $p = 1$), so the closed form is
verified independently of the algebra that produced it. The sign of
$\mathrm{Im}(Z/Z_0)$ first changes at $p = 2.043$ (computed from the closed
form); that sign change is a phase rotation, not a new conduction mechanism, and
it is one reason the quadrature channel is a measurement only in the induction
regime.

### 3.2 Small-$p$ expansion, and the two channels

Expanding the closed form for small $p$:

$$\frac{Z}{Z_0} = 1 + \mathrm{i}p^{2} + \tfrac{2}{3}(1+\mathrm{i})p^{3}
+ O(p^{4}).$$

The demonstration checks the coefficients numerically:

| $p$ | exact $\mathrm{Im}(Z/Z_0)$ | $p^{2}$ | ratio | exact $\mathrm{Re}(Z/Z_0)-1$ | $\tfrac23p^{3}$ | ratio |
|---|---|---|---|---|---|---|
| $10^{-3}$ | $1.000667\times10^{-6}$ | $1.0\times10^{-6}$ | 1.000667 | $6.6717\times10^{-10}$ | $6.6667\times10^{-10}$ | 1.000750 |
| $10^{-2}$ | $1.006667\times10^{-4}$ | $1.0\times10^{-4}$ | 1.006667 | $6.7168\times10^{-7}$ | $6.6667\times10^{-7}$ | 1.007520 |
| $10^{-1}$ | $1.066528\times10^{-2}$ | $1.0\times10^{-2}$ | 1.066528 | $7.17999\times10^{-4}$ | $6.6667\times10^{-4}$ | 1.076999 |

So, in the induction regime:

- the **quadrature** (out-of-phase) response is proportional to $\sigma$ at
  leading order — a linear measure of conduction;
- the **in-phase** (real) deviation is $O(\sigma^{3/2})$ — a much weaker
  signal, which is why the in-phase channel is used as the skin-effect
  indicator rather than as the primary measurement.

### 3.3 Apparent conductivity and the skin-effect bias

Calibrate the tool so that the quadrature reading gives conductivity:

$$\frac{\sigma_a}{\sigma} \equiv \frac{\mathrm{Im}(Z/Z_0)}{p^{2}}
\;\xrightarrow[p\to0]{}\; 1 .$$

The demonstration tabulates the exact value:

| $p$ | in-phase | quadrature | $\sigma_a/\sigma$ |
|---|---|---|---|
| 0.05 | 1.00009 | 0.00258 | 1.0333 |
| 0.10 | 1.00072 | 0.01067 | 1.0665 |
| 0.20 | 1.00618 | 0.04529 | 1.1322 |
| 0.50 | 1.11866 | 0.32822 | 1.3129 |
| 1.00 | 2.28736 | 1.46869 | 1.4687 |
| 1.57 | 7.54425 | 2.74580 | 1.1140 |
| 2.00 | 16.51263 | 0.56899 | 0.1423 |
| 3.00 | 48.27248 | $-53.98465$ | $-5.9983$ |

The measured bias is well described by the leading correction derived from the
series, $\sigma_a/\sigma - 1 \approx \tfrac{2}{3}p$:

| $p$ | measured bias | $\tfrac23 p$ |
|---|---|---|
| 0.1 | +6.653% | +6.667% |
| 0.2 | +13.217% | +13.333% |
| 0.3 | +19.592% | +20.000% |

The calibration is within $1\%$ for $p\le0.015$ and within $5\%$ for
$p\le0.075$. **This is the single most useful number in the lesson**: the
induction number, not the tool's own accuracy, usually sets the systematic error
of an apparent-conductivity log. Because $p\propto\sqrt{\sigma}$, the bias grows
as the square root of conductivity, so it is invisible in a resistive formation
and dominant in a conductive one.

*Numerical example.* The synthetic sonde has $L = 1.00\ \mathrm{m}$ and operates
at 20 kHz. In a $1\ \Omega\,\mathrm{m}$ formation, $\delta = 3.559\ \mathrm{m}$,
$p = 0.2810$, and the skin-effect bias is $+18.40\%$. To keep the bias under
$5\%$ at this frequency and spacing you need $p\le0.075$, hence
$\delta\ge L/0.075 = 13.33\ \mathrm{m}$, hence
$\rho\ge f(\delta/503.2921)^{2} = 20000\times(13.33/503.2921)^{2}
= 14.0\ \Omega\,\mathrm{m}$. Below about $14\ \Omega\,\mathrm{m}$ this
calibration is not a $5\%$ measurement.

## 4. Doll's geometric factor and vertical resolution

### 4.1 The ring-flux identity

Doll's approach fixes a thin coaxial ring of radius $\rho$ at axial offset $z$
from the sonde centre and computes what it contributes. The first ingredient is
the flux through the ring from a magnetic dipole on the axis. With the axial
field $B_z = (\mu_0 m/4\pi)(2z^{2}-\rho'^{2})/(\rho'^{2}+z^{2})^{5/2}$,

$$\Phi(\rho,z) = \int_0^{\rho} 2\pi\rho'\,B_z(\rho',z)\,\mathrm{d}\rho'
= \frac{\mu_0 m}{2}\frac{\rho^{2}}{r^{3}},
\qquad r = \sqrt{\rho^{2}+z^{2}} .$$

The demonstration verifies this by quadrature to six decimals at five
$(\rho,z)$ pairs. The case $z = 0$ is excluded and the exclusion is physics, not
numerics: a ring lying in the dipole's equatorial plane has a logarithmically
divergent flux linkage in the point-dipole model, and a real coil's finite radius
is what makes the real flux finite.

### 4.2 Assembling the geometric factor

The ring carries a current $I_{\text{ring}} = \omega\Phi_T\,\sigma\,\mathrm{d}\rho\,
\mathrm{d}z/(2\pi\rho)$ (driven by $\omega\Phi_T$, limited by the ring resistance
$2\pi\rho/\sigma\,\mathrm{d}\rho\,\mathrm{d}z$), and the receiver coil sees the
flux $(\mu_0/2)\rho^{2}/r_R^{3}$ per unit ring current. Collecting the factors,
the contribution of a volume element is proportional to

$$\rho^{2}\big/\big(r_T^{3}\,r_R^{3}\big),
\qquad r_T^{2} = \rho^{2} + (z-\tfrac{L}{2})^{2},
\qquad r_R^{2} = \rho^{2} + (z+\tfrac{L}{2})^{2}.$$

The **geometric factor** $g$ is this expression normalised so that
$\int g\,\mathrm{d}V = 1$ over all space; that normalisation is what makes
$\sigma_a = \sigma$ exact for a homogeneous medium. The demonstration computes the
normalising integral ($12.48080\ \mathrm{m^{3}}$ for $L = 1$ m) and verifies
$\int g_v(z)\,\mathrm{d}z = 1.00000000$.

### 4.3 The vertical response

Integrating $g$ over $\rho$ gives the vertical response $g_v(z)$, which can be
checked analytically. For $|z|\le L/2$ the angular factor becomes trivial and

$$g_v(z) = \frac{2\pi}{L^{2}}\ \text{(unnormalised)}
\qquad\Longrightarrow\qquad g_v(0) = g_v(L/2),$$

an exactly **flat top**; and for large $|z|$,

$$g_v(z)\,z^{2} \to \frac{\pi}{2}\ \text{(unnormalised)},$$

so the tails fall off only as $1/z^{2}$ and never quite vanish. The demonstration
confirms both: the numeric value at $z = 0,\,L/2$ is $0.503358$ against the
analytic $0.503428$ (ratio $0.999861$, the residual being the truncation of the
$z$ integral), and $g_v z^{2}/\text{(total)}$ reaches 1.5673, 1.5630, 1.5492 and
1.5164 at $z = 2, 3, 5, 8$ m against $\pi/2 = 1.5708$.

Fractions of the vertical response, measured:

| window | fraction of $g_v$ |
|---|---|
| $|z|\le L/2$ | 0.5034 |
| $|z|\le L$ | 0.7579 |
| $|z|\le 2L$ | 0.8840 |

**Half the measurement comes from within half a spacing of the coil midpoint, and
the remaining sixth lives beyond two spacings.** That is the vertical resolution
of the tool, and it is not improved by logging more densely.

## 5. The shoulder effect, measured

Convolve a layered conductivity profile with $g_v$ (the Doll model) and the same
1 m bed of $1.00\ \mathrm{S\,m^{-1}}$ in a $0.10\ \mathrm{S\,m^{-1}}$ background
reads:

| sonde spacing $L$ | peak apparent conductivity | as a fraction of the bed |
|---|---|---|
| 1.00 m | 0.7922 S/m | 79.2% |
| 0.50 m | 0.8956 S/m | 89.6% |
| 0.25 m | 0.9484 S/m | 94.8% |

The reading never reaches the bed value: the sonde averages the shoulders into
the answer. Two consequences deserve to be said plainly.

- **A thin resistive bed is invisible and a thin conductive bed is under-read.**
  Neither is a logging error; both are the definition of the measurement.
- **Shorter spacing is better resolution and shallower investigation.** The same
  physics that narrows the vertical window reduces the volume you sample, and
  (through $p = L/\delta$) changes the skin-effect bias. Resolution,
  depth-of-investigation and calibration bias move together, and no sonde
  design escapes that.

## 6. Conductivity is not lithology

The Doll model shows that $\sigma_a$ is a weighted average of the formation
conductivity over a known volume. What the *conductivity* means is a separate
question, and the answer is not unique. Conductivity in a rock is dominated by

- the connected pore fluid (its salinity and saturation),
- the clay content and its cation-exchange capacity (surface conduction),
- the pore geometry and connectivity (the cementation exponent of Archie's law),
- metallic minerals, if present, which conduct electronically,
- and temperature, which raises fluid conductivity by about $2\%$ per degree
  Celsius near room temperature.

Two rocks with the same $\sigma_a$ can differ in saturation, clay content or
salinity, and no single-frequency induction measurement separates them. The
lesson of module 09-01 applies here in its most practical form: a conductivity
log is a *petrophysical average*, and interpreting it requires independent
information (a porosity log, a gamma-ray log for clay, a salinity, or
multi-frequency data that adds the spectral dimension). This is the same
non-uniqueness that module 09-03 quantifies for the frequency-dependent
(polarisation) part of the response.

## 7. Assumptions and regime of validity

1. **No borehole.** The geometric-factor model assumes a homogeneous medium
   everywhere. A real hole is filled with fluid of a different conductivity, and
   the invaded zone has a third. The measured value is a weighted average of all
   three; the borehole correction is largest exactly when the contrast is
   interesting.
2. **Doll's model has no skin effect.** It is exact for a homogeneous medium and
   a low induction number, and it systematically misses the quadrature-phase
   distortion described in §3.3.
3. **Point (small) coils.** The geometric factor above is the point-dipole
   limit; a real coil has a finite radius and the correction scales as
   $(a/L)^{2}$.
4. **Isotropic formation.** Thinly bedded sand-shale sequences are anisotropic
   at the tool scale, and the anisotropy appears as a spacing-dependent
   apparent conductivity.
5. **Whole space.** No surface and no bed boundary outside the sampled volume.
6. **Linearity.** The quadrature calibration assumes $p\le0.075$ for 5%
   accuracy; beyond that, compute the exact response rather than quoting a linear
   one.

## 8. Worked examples

### Example 1 — skin depth and a go/no-go decision

A 20 kHz sonde with $L = 1.00\ \mathrm{m}$ is run in a formation whose
conductivity is expected to be $1\ \mathrm{S\,m^{-1}}$. From the table,
$\delta = 3.559\ \mathrm{m}$ and $p = 1.00/3.559 = 0.2810$. The quadrature-based
apparent conductivity will read $+18.4\%$ high before any borehole correction. If
the target is a $10\%$ conductivity change, the tool cannot resolve it: the
systematic bias is twice the signal. The remedies, in order of preference, are a
lower frequency (halving $f$ reduces $p$ by $\sqrt{2}$), a shorter spacing, or an
explicit skin-effect inversion of the complex response.

### Example 2 — the flat top, by hand

With $L = 1$ m, over $|z|\le0.5$ m the vertical response is
$g_v = 2\pi/L^{2} = 6.2832\ \mathrm{m^{-1}}$ before normalisation. The measured
normalising volume is $12.4808\ \mathrm{m^{3}}$, so the normalised value is
$6.2832/12.4808 = 0.50343\ \mathrm{m^{-1}}$ — which is what the demonstration
prints at $z = 0$, $0.25$ and $0.5$ m (0.503358, the difference being the
truncation of the numerical $z$ integral). Because the response is *flat* over
that window, shifting the sonde within it does not change the reading; the
reading changes only when a boundary enters within $\sim L/2$ of the coils.

### Example 3 — how much of the reading is from the bed?

For the 1 m bed with $L=1$ m, the Doll model gives 0.7922 S/m instead of
1.00 S/m, so $20.8\%$ of the true bed conductivity is missing from the peak
reading and has been replaced by the background. If the analyst converts the
reading to a water saturation with Archie's law and no shoulder correction, the
error is entirely in the saturation: $\sigma \propto S_w^{n}$ with $n\approx2$,
so a $20.8\%$ conductivity deficit is a $10\%$ saturation deficit before any
other error.

## 9. Python demonstration

[`code/downhole_em_logging_demo.py`](./code/downhole_em_logging_demo.py) prints,
with units:

1. the skin depth and induction number over a grid of frequency and resistivity,
   together with the exact constant 503.2921;
2. the ring-flux identity, verified by quadrature against the closed form;
3. Doll's geometric factor: the normalising integral, the check that
   $\int g_v\,\mathrm{d}z = 1$, the flat top, the $1/z^{2}$ tail, and the
   fractions of the response inside $|z|\le L/2$, $L$ and $2L$;
4. the shoulder effect for sonde spacings 1.0, 0.5 and 0.25 m;
5. the exact homogeneous response, its small-$p$ series, the quadrature
   calibration, the measured skin-effect bias against $\tfrac23p$, and the
   independent solution check of the closed form.

```bash
cd 09-electrical-em-methods/06-borehole-electrical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python downhole_em_logging_demo.py
```

It takes under a second, requires no network, uses a fixed seed and exits 0.

## 10. Exercises

See
[`exercises/03-downhole-em-logging-exercises.md`](./exercises/03-downhole-em-logging-exercises.md)
and
[`exercises/03-downhole-em-logging-solutions.md`](./exercises/03-downhole-em-logging-solutions.md).

- **★** Compute $\delta$ and $p$ for three tool spacings at 20 kHz in
  $20\ \Omega\,\mathrm{m}$ rock, and state which regime each is in.
- **★★** Derive $\sigma_a/\sigma - 1 \approx \tfrac23p$ from the series and use
  it to find the resistivity at which the bias reaches 10% for the synthetic
  sonde.
- **★★** From the measured fractions of $g_v$, estimate how thick a bed must be
  before the peak reading is within 5% of the true bed conductivity, and check
  your estimate against the shoulder-effect table.
- **★★★** Design a two-spacing, two-frequency induction experiment that
  separates a salinity change from a clay-content change, and state the
  degeneracy that remains even then.

## 11. Common mistakes

1. **Reading a conductivity log as a lithology log.** It is a weighted average
   of fluid, clay, geometry and metallic content.
2. **Ignoring the induction number.** $p$ sets the systematic error, and it is
   usually larger than the tool's stated accuracy.
3. **Quoting the bed value from a thin-bed reading.** The shoulder effect is
   $10$–$20\%$ on a 1 m bed and larger on thinner ones.
4. **Using a shorter sonde for "better resolution" without re-checking the
   calibration.** Both the vertical window and the skin-effect bias change.
5. **Treating the Doll model as the instrument response.** It has no borehole,
   no skin effect and no finite coil radius.

## Mastery checkpoint

Complete this without notes.

> A two-coil induction sonde has $L = 0.80\ \mathrm{m}$ and operates at 25 kHz.
> **(a)** Compute the skin depth and the induction number in formations of 1, 10
> and $100\ \Omega\,\mathrm{m}$. **(b)** Estimate the skin-effect bias of a
> quadrature-calibrated apparent conductivity in each case using
> $\tfrac23p$, and check the sign and rough size against the exact table in §3.3.
> **(c)** Compute the unnormalised vertical response over $|z|\le L/2$ and state
> the vertical window that carries half the measurement. **(d)** A 0.6 m bed of
> $0.5\ \mathrm{S\,m^{-1}}$ sits in a $0.05\ \mathrm{S\,m^{-1}}$ formation. State
> whether the peak reading will be closer to, or further from, the true bed
> conductivity than the 1 m bed of the demonstration, and why. **(e)** Name three
> rock properties that could produce the same reading, and one independent
> measurement for each that would break the ambiguity.

A worked version of (a)–(c) appears in the lesson-03
[solutions](./exercises/03-downhole-em-logging-solutions.md).

## Common pitfalls

1. **Confusing $\delta$ with a depth of investigation.** $\delta$ is the
   amplitude decay length; the *geometric* depth of investigation is set by $L$
   and by the 1/z² tails, and they are different questions.
2. **Assuming the in-phase channel is the measurement.** It is the skin-effect
   channel; the conductivity comes from the quadrature in the induction regime.
3. **Extrapolating a linear calibration into the wave regime.** At $p=1$ the
   quadrature reads $46.9\%$ high (measured), the maximum of the calibrated
   ratio within $p\le4$ is $1.4687$ at $p=1.000$, and the sign of the quadrature
   changes at $p=2.043$.
4. **Forgetting temperature.** Fluid conductivity rises about $2\%$ per degree
   Celsius near room temperature; a $20\ ^\circ$C logging temperature change is a
   $40\%$ conductivity change that has nothing to do with geology.
5. **Reporting a bed boundary to a precision finer than $L/2$.** The tool cannot
   see it.

## Related modules

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  Archie's law, clay conduction and the temperature dependence that this lesson
  leaves as an input.
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) — the
  frequency-dependent part of the same response, and membrane polarisation in
  clays.
- [09-06-01 Cross-Hole and Borehole-to-Surface Tomography](01-cross-hole-tomography.md) —
  what several holes can do that one cannot.
- [05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md) —
  the multi-log interpretation context, including the gamma-ray log that
  resolves the clay ambiguity.
