---
id: 23-04-04
title: "GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration"
level: graduate
prereqs: ["10-01-04", "23-04-01"]
estimated_minutes: 100
tags: [gpr, ground-penetrating-radar, fieldwork, antennas, resolution, calibration]
---

# GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the propagation velocity, wavelength and vertical resolution for a
   stated permittivity and antenna frequency.
2. **Compute** the velocity and depth of a target from its diffraction hyperbola.
3. **Compute** the trace spacing a migration requires, and **state** what happens
   when it is not met.
4. **Compute** the maximum depth of an attenuation budget from the material's
   loss and the system's dynamic range.
5. **Size** a survey grid and its data volume and acquisition time.
6. **Calibrate** the velocity against a known target and **compute** the depth
   error of a wrong permittivity.

All permittivities, frequencies, attenuation rates, grid geometries and measured
times in this lesson are **SYNTHETIC** teaching values, combined with the standard
relations quoted in the text. No field dataset, antenna specification or commercial
system is used or reproduced.

## Prerequisites

- [01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](01-ert-fieldwork.md) —
  the galvanic method used at the same sites.
- [10-01-04 Antennas: Frequency, Shielding, Polarisation and Offsets](../../10-gpr-near-surface/01-gpr-principles/04-gpr-antennas.md) —
  the antenna properties this lesson deploys.

## 1. Intuition: GPR trades penetration for resolution, explicitly

Ground-penetrating radar radiates a short electromagnetic pulse into the ground and
listens for reflections. Its two performance limits are stated in the same units as
the target:

- **Resolution**, set by the wavelength: the vertical resolution is conventionally a
  quarter of the wavelength, so higher frequency means finer resolution.
- **Penetration**, set by attenuation: higher frequency is attenuated faster, so
  higher frequency means less depth.

Everything else in the field method — the antenna choice, the grid spacing, the
velocity calibration, the coupling — follows from those two limits and from the
ground's permittivity, which the survey must measure rather than assume.

## 2. Velocity, wavelength and resolution

In a low-loss dielectric the propagation velocity is

$$v = \frac{c}{\sqrt{\varepsilon_r}}, \qquad c = 0.299792458\ \mathrm{m/ns},$$

and the wavelength at frequency $f$ is $\lambda = v/f$, with the vertical
resolution conventionally taken as $\lambda/4$. The demonstration's table:

| $\varepsilon_r$ | $v$ (m/ns) | 100 MHz: $\lambda$ / $\lambda/4$ | 250 MHz | 500 MHz | 900 MHz |
|---|---|---|---|---|---|
| 4 | 0.14990 | 1.4990 / 0.3747 | 0.5996 / 0.1499 | 0.2998 / 0.0749 | 0.1666 / 0.0416 |
| 9 | 0.09993 | 0.9993 / 0.2498 | 0.3997 / 0.0999 | 0.1999 / 0.0500 | 0.1110 / 0.0278 |
| 16 | 0.07495 | 0.7495 / 0.1874 | 0.2998 / 0.0749 | 0.1499 / 0.0375 | 0.0833 / 0.0208 |

Read the table as three coupled decisions. The **frequency** sets the resolution;
the **material** sets the velocity, and therefore how much resolution a given
frequency delivers (a wet material with $\varepsilon_r = 16$ has two thirds of the
wavelength of dry material at the same frequency, so its resolution is two thirds
as fine and its attenuation much higher); and the **resolution requirement** decides
which frequencies are worth carrying on the survey. A 250 MHz antenna in
$\varepsilon_r = 9$ material resolves 0.10 m, which is the right scale for
archaeological stratigraphy or utility detection; a 900 MHz antenna in the same
material resolves 0.028 m, for concrete inspection, at a fraction of the depth.

## 3. Velocity from a diffraction hyperbola

A point target produces a hyperbolic diffraction whose apex is at the two-way
travel time $t_0 = 2d/v$ above the target, with the time at horizontal offset $x$
given by $t(x)^{2} = t_0^{2} + (2x/v)^{2}$. Inverting:

$$v = \frac{2x}{\sqrt{t(x)^{2} - t_0^{2}}} , \qquad d = \frac{v\,t_0}{2} .$$

With $t_0 = 10.0$ ns, $x = 1.0$ m and $t = 12.8$ ns the demonstration reports

$$v = \frac{2.0}{\sqrt{12.8^{2} - 10.0^{2}}} = \frac{2.0}{7.9900}
= 0.25031\ \mathrm{m/ns}, \qquad
\varepsilon_r = \left(\frac{c}{v}\right)^{2} = 1.4344, \qquad
d = 1.2516\ \mathrm{m}.$$

This is the standard field calibration: **one isolated, identifiable target with a
known position gives both the velocity and the depth scale for the whole survey.**
Two practical requirements: the horizontal offset must be measured on the ground
(not read from a file whose trace spacing is itself uncertain), and the hyperbola
must be from a compact target rather than a linear reflector, because a planar
reflector produces a different moveout.

## 4. Trace spacing and migration

Migration collapses diffractions back to their apex and needs the wavefield sampled
in space at a quarter of the wavelength or finer:

| $\varepsilon_r$ | 100 MHz | 250 MHz | 500 MHz |
|---|---|---|---|
| 9 | 0.2498 m | 0.0999 m | 0.0500 m |
| 16 | 0.1874 m | 0.0749 m | 0.0375 m |

A 250 MHz survey in $\varepsilon_r = 9$ material therefore needs a trace every
**0.10 m**. That is a demanding field rate: 10 traces per metre, or 1000 traces per
100 m line, and the grid of Section 5 shows what that costs in time. The temptation
to pace at 0.5 m must be resisted or the diffractions will be aliased into
artefacts that migration will strengthen rather than remove — the spatial equivalent
of the temporal aliasing of
[20-01-05 Sampling, Nyquist and Reconstruction](../../20-signal-processing/01-signals-and-systems/05-sampling-theory.md).

## 5. The attenuation budget

The depth range is a budget: the two-way loss at depth $d$ is $2\alpha d$ with
$\alpha$ the one-way attenuation, and the surveying stops where the loss exhausts
the system's dynamic range. With $\alpha = 1$ dB/m and a 100 dB range:

| Depth (m) | Two-way loss (dB) | Within range? |
|---|---|---|
| 2 | 4.0 | yes |
| 5 | 10.0 | yes |
| 10 | 20.0 | yes |
| 20 | 40.0 | yes |
| 50 | 100.0 | yes |
| 100 | 200.0 | no |

so the maximum depth at this attenuation and range is

$$d_{\max} = \frac{\text{range}}{2\alpha} = \frac{100}{2} = 50\ \mathrm{m}.$$

Two cautions. First, **attenuation is a property of the ground, not of the
antenna**: it rises steeply with water content and with clay, so the same antenna
that reaches 50 m in dry sand reaches 2 m in wet clay. Second, **the range is not
all signal**: the useful signal-to-noise at the bottom of the budget is close to
the noise, so the *interpretable* depth is smaller than $d_{\max}$, and the honest
field practice is to test the depth range on site (by observing a known target at
depth) rather than to compute it from a specification.

## 6. The grid, its data volume and its time

For a 20 m × 20 m grid at 0.25 m spacing in both directions, the demonstration
reports

| Quantity | Value |
|---|---|
| traces | $81 \times 81 = 6561$ |
| data volume at 512 samples, 4 bytes | 13.4 MB |
| acquisition time at 5 s per trace | 9.11 h of continuous work |

The data volume is modest; the **time** is not. Nine hours of continuous walking for
a single grid — before setup, marking, the inevitable re-walks and the second
antenna frequency that most surveys also want — is more than a field day, which is
why GPR grids are planned at the largest trace spacing the science allows, and why
the trace spacing decision of Section 4 is the decision that sets the survey's cost.

Practical notes on the grid and the field procedure:

1. **Lay out a square grid with marked stations** and record the line azimuth and
   the station spacing, so that the data can be gridded and migrated with the
   correct geometry.
2. **Walk the same direction on every line** where the antenna polarisation matters
   (a dipole antenna radiates differently along and across the line).
3. **Two orthogonal line sets** for a 3-D survey or for utility mapping, with the
   crossing points used as a quality check (the same target should appear at the
   same position in both directions).
4. **Record the surface conditions**: wet or dry, paved or vegetated, and any
   metallic objects. Coupling to the ground changes the antenna's effective
   frequency and the reflection strength, and it is the most common explanation for
   a survey that works on one side of a fence and not on the other.

## 7. Calibration against a known target

Calibration means measuring the velocity of *this* ground at *this* site. The
demonstration's example: a target at a known 1.50 m depth measured at 31.5 ns
two-way time.

$$v_{\text{true}} = \frac{2d}{t} = \frac{3.00}{31.5} = 0.09524\ \mathrm{m/ns},
\qquad
\varepsilon_r = \left(\frac{0.299792458}{0.09524}\right)^{2} = 9.909 .$$

If the assumed permittivity was 9.0 (velocity 0.09993 m/ns), the depth reported for
that same measurement is

$$d = \frac{v\,t}{2} = \frac{0.09993 \times 31.5}{2} = 1.5739\ \mathrm{m},
\qquad \text{error} = +4.93\ \%.$$

A 10 % error in permittivity becomes a 5 % error in depth — a factor of two
reduction because $v \propto 1/\sqrt{\varepsilon_r}$ — but 5 % of 1.5 m is 7.5 cm,
which matters when the question is whether a pipe is 1.5 m or 1.6 m deep. The
calibration methods, in order of reliability:

1. **A target of known depth** (a plate buried by the survey team, a known pipe or
   foundation, a borehole with a logged interface). This is the gold standard.
2. **A diffraction hyperbola** (Section 3), which needs only an isolated target and
   a measured offset.
3. **Common-midpoint or wide-angle reflection sounding**, which recovers the
   velocity from the moveout of a reflector across offsets — more field time, and
   the most reliable where a suitable reflector exists.
4. **A time-domain reflectometry probe or a sample measurement** of the material's
   permittivity, which is indirect but useful for planning.

## 8. Assumptions and regime of validity

1. **A low-loss dielectric.** $v = c/\sqrt{\varepsilon_r}$ ignores conduction
   losses; in wet clay or saline ground the velocity is dispersive and the simple
   relation is inadequate — which is also where GPR fails entirely.
2. **A known permittivity.** The depth scale is only as good as $\varepsilon_r$, and
   it varies laterally and with depth; a single value is an average.
3. **$\lambda/4$ as the resolution.** It is a convention (the Rayleigh criterion
   equivalent for a thin bed); the practical resolution also depends on the
   signal-to-noise and the migration.
4. **A compact target for the hyperbola method.** A planar reflector, a dipping
   interface or two interfering targets give the wrong velocity.
5. **A constant attenuation.** Real ground has a layered, moisture-dependent
   attenuation; the budget of Section 5 is a planning estimate.
6. **Coupling is invariant.** It is not: antenna height, ground roughness, surface
   water and the operator's own body all change the radiated pulse, which is why
   the field notes must record surface conditions along each line.

## 9. The honest summary

- $v = c/\sqrt{\varepsilon_r}$; a 250 MHz antenna in $\varepsilon_r = 9$ resolves
  0.10 m and reaches metres.
- A diffraction hyperbola gives velocity and depth from one target.
- Migration needs a trace every $\lambda/4$: 0.10 m at 250 MHz in
  $\varepsilon_r = 9$.
- The depth range is a budget: 50 m at 1 dB/m one-way with a 100 dB range, and far
  less in wet clay.
- A 20 m × 20 m grid at 0.25 m spacing is 6561 traces and 9.1 h.
- A 10 % permittivity error is a 5 % depth error: calibrate on site.

## 10. Python demonstration

[`code/gpr_fieldwork_demo.py`](./code/gpr_fieldwork_demo.py) prints every number
quoted above. It:

1. tabulates velocity, wavelength and $\lambda/4$ resolution for three
   permittivities and four frequencies;
2. computes the velocity, permittivity and depth from a diffraction hyperbola;
3. tabulates the trace spacing required for migration;
4. computes the two-way loss and the maximum depth of an attenuation budget;
5. computes the trace count, data volume and acquisition time of a grid;
6. calibrates the velocity against a known target and reports the depth error of a
   wrong permittivity.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/04-electrical-em-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_fieldwork_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/04-gpr-fieldwork-exercises.md`](./exercises/04-gpr-fieldwork-exercises.md)
and
[`exercises/04-gpr-fieldwork-solutions.md`](./exercises/04-gpr-fieldwork-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. Compute the velocity, wavelength and $\lambda/4$ resolution for
   $\varepsilon_r = 6$ at 400 MHz.
2. A hyperbola has an apex at 8.0 ns and a time of 11.3 ns at an offset of 0.75 m.
   Compute the velocity, the permittivity and the depth.
3. Compute the trace spacing required for migration at that wavelength, and the
   number of traces on a 30 m line at that spacing.
4. A material has 2.5 dB/m one-way attenuation and the system's range is 90 dB.
   Compute the maximum depth.
5. A target at 2.0 m is measured at 26.0 ns. Compute the true velocity and the
   depth that would be reported using $\varepsilon_r = 9$.

## 13. Common pitfalls

1. **Assuming a permittivity instead of measuring one.** A 10 % error is a 5 %
   depth error.
2. **Pacing traces too coarsely for migration.** The diffractions alias into
   artefacts.
3. **Confusing resolution with penetration.** Higher frequency buys the first and
   costs the second.
4. **Using the depth-range specification as a promise.** Attenuation is a property
   of the ground.
5. **Reading the hyperbola offset from a file.** The trace spacing may itself be
   wrong.
6. **Ignoring coupling changes along a line.** They change the effective frequency
   and the amplitudes.
7. **Walking alternate lines in opposite directions.** The radiation pattern is
   not symmetric.

## 14. Where this is used

- Utility and infrastructure detection, where the depth accuracy is the deliverable.
- Archaeology and forensics, where the resolution and the grid are the survey.
- Glaciology and hydrology, where the permittivity contrast is large and the depth
  range long — see
  [10-03-02 GPR for Glacier Thickness and Internal Stratigraphy](../../10-gpr-near-surface/03-gpr-applications/02-gpr-glaciology.md).
- Concrete and pavement inspection, where high frequencies and fine trace spacing
  are both used.
- Any 4-D or monitoring survey, where the repeatability of the coupling and the
  antenna position becomes the limiting factor.

## 15. Related lessons

- [01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](01-ert-fieldwork.md) —
  the complementary galvanic method.
- [02 EM Fieldwork: Loop, Coil and Grounded-Source Configurations](02-em-fieldwork.md) —
  the same electromagnetic spectrum at lower frequencies.
- [05 Borehole Logging Operations and Tool Calibration](05-borehole-fieldwork.md) —
  where log depth control and GPR depth conversion meet.
- [10-01-02 Velocity Estimation and Depth Conversion in GPR](../../10-gpr-near-surface/01-gpr-principles/02-gpr-velocity-and-depth.md) —
  the velocity analysis in more depth.
- [10-02-01 Survey Design: Profile, Grid, CMP and Transillumination](../../10-gpr-near-surface/02-gpr-acquisition-and-processing/01-gpr-survey-design.md) —
  the design methods this lesson sizes.

## 16. Self-assessment checklist

- [ ] I can compute velocity, wavelength and resolution from permittivity.
- [ ] I can compute velocity and depth from a hyperbola.
- [ ] I can compute a migration trace spacing.
- [ ] I can size an attenuation budget.
- [ ] I can size a grid's traces, volume and time.
- [ ] I can calibrate a velocity and compute a depth error.
