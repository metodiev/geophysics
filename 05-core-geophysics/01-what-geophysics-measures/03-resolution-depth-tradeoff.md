---
id: 05-01-03
title: "Resolution, Penetration Depth and the Fundamental Trade-Off"
level: advanced
prereqs: ["05-01-01", "05-01-02"]
tags: [resolution, penetration, trade-off, skin-depth, depth-rule]
---

# Resolution, Penetration Depth and the Fundamental Trade-Off

## Learning objectives

1. **Define** resolution precisely for each method family, and distinguish
   lateral from vertical resolution.
2. **Derive** the linear width–depth law for potential-field anomalies and the
   quarter-wavelength law for wave methods.
3. **Derive** the diffusive skin depth and show why EM penetration is set by
   frequency, not by transmitter power.
4. **Quantify** the information-content penalty of depth with a single exponent.
5. **State** the trade-off as a budget: what must be given up to gain depth.

## Prerequisites

- [05-01-01 The Central Idea](./01-physical-property-contrast.md)
- [05-01-02 Taxonomy of Methods](./02-method-taxonomy.md)
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md)

## 1. Intuition: three different trade-offs wearing one name

"Resolution versus depth" bundles three physically distinct constraints:

1. **Potential fields (gravity, magnetics).** The anomaly width is fixed by
   distance. There is no frequency to trade, so the trade-off is absolute: the
   kernel sets it.
2. **Wave fields (seismic, GPR).** Higher frequency gives finer resolution but
   suffers more attenuation and scattering, so penetration falls. The trade-off
   is a *choice* of band.
3. **Diffusive fields (EM, MT, thermal).** Higher frequency is confined to a
   shallower skin depth. The trade-off is a *law*, and it is the same law for
   magnetotellurics at 100 km and for a metal detector at 10 cm.

Knowing which of the three you are in determines whether a design change can
help.

## 2. Precise definitions

**Vertical resolution** — the smallest separation in depth at which two
interfaces are separately detectable. For a wave method with bandwidth $B$ and
velocity $v$, the Rayleigh limit is

$$\Delta z_\text{res} \approx \frac{v}{4B}.$$

**Lateral resolution** — the smallest horizontal separation resolvable. For
potential fields this is governed by the anomaly half-width; for wave methods by
the first Fresnel zone or by migration aperture.

**Penetration depth** — the depth at which the signal falls to the noise floor.
It is a *system* property: source strength, attenuation and noise together. It
is not an instrument specification.

**Depth rule (potential fields).** The half-width $w_{1/2}$ of an anomaly from
an isolated compact source is proportional to its depth $d$:

$$w_{1/2} = 2\sqrt{2^{2/3}-1}\; d = 1.532842\,d.$$

## 3. Derivations

### 3.1 The potential-field width law

For a point mass at depth $d$, $g_z(x) = Gm\,d/(x^2+d^2)^{3/2}$. Set
$g_z(x) = \tfrac12 g_z(0)$:

$$\frac{d^3}{(x^2+d^2)^{3/2}} = \frac12
\implies \left(\frac{x^2+d^2}{d^2}\right)^{3/2} = 2
\implies x^2 = d^2\left(2^{2/3}-1\right).$$

So $x = d\sqrt{2^{2/3}-1}$ and the full half-width is

$$\boxed{\,w_{1/2} = 2\sqrt{2^{2/3}-1}\;d = 1.532842\,d\,}$$

with $2^{2/3} = 1.587401$. **The width is exactly proportional to depth.** No
instrument, no source, and no processing can change that, because it follows
from the $d^3/(x^2+d^2)^{3/2}$ kernel alone.

### 3.2 The diffusive skin depth

In a good conductor the displacement current is negligible and the magnetic
field obeys a diffusion equation

$$\nabla^2 \mathbf{B} = \mu\sigma\,\frac{\partial\mathbf{B}}{\partial t}.$$

Seek a plane wave $\mathbf{B} = \mathbf{B}_0 e^{i(\omega t - kz)}$. Substituting
gives $-k^2 = i\mu\sigma\omega$, so $k = (1-i)/\delta$ with

$$\boxed{\;\delta = \sqrt{\frac{2}{\mu\sigma\omega}}\;}$$

Dimensional check: $[\mu]=\mathrm{H\,m^{-1}}=\mathrm{kg\,m\,s^{-2}\,A^{-2}}$,
$[\sigma]=\mathrm{S\,m^{-1}}=\mathrm{A^2s^3kg^{-1}m^{-3}}$,
$[\omega]=\mathrm{s^{-1}}$, so $[\mu\sigma\omega]=\mathrm{m^{-2}}$ and
$[\delta]=\mathrm{m}$. The field decays as $e^{-z/\delta}$ and lags in phase by
$z/\delta$ radians.

Because $\delta \propto 1/\sqrt{\omega}$, **penetration is bought with period,
not with power.** Increasing transmitter current raises the signal at all depths
equally and so raises the noise-referenced depth only marginally; increasing the
period raises $\delta$ directly.

### 3.3 The information-content penalty

A compact source at depth $d$ produces an anomaly of peak amplitude
$A \propto d^{-2}$ (point mass) spread over a width $w \propto d$. The number of
independent samples of the anomaly is $N \approx w/\Delta x \propto d$, and the
information about the source therefore scales as

$$I \;\propto\; N\left(\frac{A}{\sigma_n}\right)^{2} \;\propto\; d \cdot d^{-4} = d^{-3}.$$

The exact exponent depends on the source symmetry (a 3-D dipole gives $d^{-5}$
information scaling if $A\propto d^{-3}$), but the qualitative result is robust:
**information about a target falls off far faster than the amplitude**, because
the anomaly both weakens and spreads. This is the single most important
quantitative statement in survey design.

## 4. Units and dimensional analysis

| Symbol | Meaning | SI unit | Notes |
|---|---|---|---|
| $\delta$ | skin depth | m | $\sqrt{2/\mu\sigma\omega}$ |
| $\sigma$ | conductivity | S m⁻¹ | 10⁻⁵ (dry rock) to 10³ (sulphide) |
| $\mu$ | permeability | H m⁻¹ | $4\pi\times10^{-7}$ in practice for non-magnetic rock |
| $f$ | frequency | Hz | period $T = 1/f$ |
| $d$ | depth | m | to source centre |
| $B$ | bandwidth | Hz | not the same as $f$ |

Note $\mu_0 = 1.25663706212\times10^{-6}$ H m⁻¹ (CODATA 2018, NIST); the
often-quoted $4\pi\times10^{-7}$ differs in the ninth significant figure, which
never matters in EM survey work but should be stated when it is used.

## 5. Assumptions

1. **Free space above the Earth; a half-space or layered conductor below.**
   Lateral conductivity contrasts invalidate the simple skin-depth picture.
2. **Low-frequency / quasi-static limit** for the diffusion equation: the
   displacement current is dropped. Invalid above roughly 10⁵ Hz in rock.
3. **A single dominant frequency** when quoting a skin depth. Broadband data
   contain a range of depths simultaneously, which is a feature, not a problem,
   provided the inversion accounts for it.
4. **Rayleigh quarter-wavelength** for seismic resolution assumes a
   zero-phase wavelet and a single interface; it is a rule of thumb, not a
   theorem.
5. **The point-mass/point-dipole kernel** for the width law. Extended or
   tabular bodies give larger apparent widths at the same depth.

## 6. Worked examples

### 6.1 Measured width law

Using `code/resolution_depth_demo.py` with a synthetic point mass of
$10^{10}$ kg:

| depth (m) | half-width (m) | $w/d$ |
|---|---|---|
| 100 | 153.200 | 1.53200 |
| 200 | 306.400 | 1.53200 |
| 800 | 1225.600 | 1.53200 |
| 1600 | 2451.200 | 1.53200 |

The fitted log–log slope is **1.000000**, and the measured ratio 1.532 differs
from the closed form 1.532842 by $5.5\times10^{-4}$ — a purely discretisation
residual from the sampling grid.

### 6.2 Measured minimum resolvable separation

Two equal point masses at depth $d$, separated by $s$, are deemed resolvable
when the midline dips by more than 1% below the peaks. The measurement gives
$s_\text{min}/d = 1.11697$ for every depth tested (100 m to 1600 m), again with
a fitted slope of exactly 1.000000. The *constant* depends on the arbitrary 1%
threshold; the *proportionality* does not.

### 6.3 Skin depth versus period

For a stated synthetic conductivity $\sigma = 1$ S/m and period $T = 100$ s:
$\mu_0\sigma\omega = (1.2566\times10^{-6})(1)(2\pi/100) = 7.896\times10^{-8}$
m⁻², so $\delta = \sqrt{2/7.896\times10^{-8}} = 5032.9$ m. A numerical
finite-difference solution of the diffusion equation, refined over three grids,
measured a decay length of 4830.9 m at $dz/\delta = 0.2$, 4837.3 m at 0.1 and
4841.1 m at 0.05 — an error falling with refinement, i.e. a discretisation
error, not a modelling error. See
[05-02-02](../02-geophysical-fields-and-observables/02-field-measurement-units.md).

### 6.4 Seismic resolution arithmetic

For $v = 2500$ m/s and $B = 50$ Hz: $\Delta z_\text{res} = 2500/(4\cdot50) =
12.5$ m. Doubling the bandwidth to 100 Hz halves it to 6.25 m — but only if the
earth transmits 100 Hz to the target depth. In practice the usable band is set
by attenuation, so bandwidth and penetration are the two ends of one lever
([05-04-06](../04-rock-physics/06-attenuation-dispersion-rock.md)).

## 7. Python demonstration

Run `code/resolution_depth_demo.py`. It prints, for each depth, the measured
half-width, the closed-form prediction, the fitted log–log slope for the width
and for the minimum resolvable separation, and the amplitude-versus-noise table
that shows the $d^{-2}$ amplitude penalty. Predict the slope before running.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/03-resolution-depth-tradeoff-exercises.md`](./exercises/03-resolution-depth-tradeoff-exercises.md).

**Common mistakes.**

1. **Quoting a single "resolution" number.** Lateral, vertical and amplitude
   resolution are different things.
2. **Confusing penetration with depth of investigation.** Penetration is where
   the signal dies; depth of investigation is where the model is constrained.
   They are set by different parts of the system.
3. **Trying to out-engineer the width law.** More power does not narrow an
   anomaly.
4. **Assuming high frequency always resolves better.** Above the usable band it
   only attenuates.
5. **Ignoring the $d^{-3}$ information penalty** when designing a deep survey,
   then blaming the inversion for a smooth answer.

**Real-world applications.**

- **Mineral exploration** targets are shallow, so dense low-frequency EM wins.
- **Crustal and mantle studies** accept kilometre-scale resolution in exchange
  for 100 km penetration (magnetotellurics, receiver functions).
- **Engineering and forensic surveys** trade depth for centimetre resolution.
- **4-D monitoring** needs repeatability, which is an *amplitude* resolution
  problem, not a spatial one.

## 9. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*.** Chapter 6 (anomaly widths and depth rules). Level: advanced.
- **Sheriff & Geldart, *Exploration Seismology*.** Chapter 2 (resolution,
  Fresnel zones). Level: intermediate.
- **Ward, S. H. & Hohmann, G. W. (1988). Electromagnetic theory for
  geophysical applications.** In *Electromagnetic Methods in Applied
  Geophysics*, Vol. 1. Level: graduate. The canonical skin-depth development.

## 10. Related lessons

- [05-01-04 Non-Uniqueness of Geophysical Models](./04-ambiguity-and-nonuniqueness.md)
- [05-02-03 Noise, Drift, Tides and Instrument Bias](../02-geophysical-fields-and-observables/03-noise-and-drift.md)
- [02-07-06 EM Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)

## Self-assessment checklist

- [ ] I can derive $w_{1/2} = 1.532842d$ and verify it numerically.
- [ ] I can derive $\delta=\sqrt{2/\mu\sigma\omega}$ from the diffusion equation
      and check its dimensions.
- [ ] I can explain why EM penetration is bought with period rather than power.
- [ ] I can compute $\Delta z_\text{res}=v/(4B)$ and state its assumptions.
- [ ] I can state the $d^{-3}$ information penalty and its implications.
