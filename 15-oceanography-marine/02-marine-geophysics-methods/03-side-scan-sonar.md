---
id: 15-02-03
title: "Side-Scan Sonar and Seafloor Imaging"
level: advanced
prereqs: ["15-02-02", "15-01-01", "05-02-02"]
tags: [oceanography, marine-geophysics, side-scan-sonar, backscatter, sonar-equation, grazing-angle, seafloor-imaging]
---

# Side-Scan Sonar and Seafloor Imaging

> **All models and data in this module are SYNTHETIC.** The source level, noise
> level, absorption, backscatter model and geometry are chosen teaching values,
> printed by the demonstration in `code/`. No sonar system, survey, frequency or
> published backscatter curve is reproduced.

Side-scan sonar answers a different question from the multibeam sounder of
[Lesson 02](02-multibeam-bathymetry.md). A multibeam system is a *measurement*
instrument: it returns geometry, and its errors are depth errors. A side-scan is
an *imaging* instrument: it returns the strength of the echo as a function of
time, and what it produces is a picture of the seafloor whose grey levels encode
roughness, hardness and — this is the honest difficulty — **the geometry of the
observation itself**.

Three facts organise the method. The first is the slant-to-ground transformation:
the record's time axis is a *slant* range, and mapping it to a plan position is a
nonlinear stretch that diverges at nadir. The second is the grazing angle: it falls
from tens of degrees near the nadir to a few degrees at the far edge, and the
echo strength changes by tens of decibels across that range. The third is that the
range is limited by absorption, so the survey geometry and the operating frequency
are a single coupled decision.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the slant-to-ground mapping $x = \sqrt{r^{2}-h^{2}}$, **compute** the
   geometric stretch $\mathrm{d}x/\mathrm{d}r$, and **explain** why the nadir part
   of a record is not interpretable.
2. **Compute** the grazing angle for a stated altitude and range, and **state** its
   range span for a typical survey geometry.
3. **Derive** the across-track resolution $c\tau/(2\sin g)$ and the along-track
   resolution $R\,\Delta\phi$, and **state** which degrades faster with range.
4. **Evaluate** an angular backscatter model in decibels, and **explain** why a
   grazing-angle correction is mandatory before any interpretation of intensity.
5. **Assemble** the active sonar equation and **solve** for the maximum detection
   range by bisection.
6. **Measure** the sensitivity of that range to the absorption coefficient and to
   the noise level, and **state** what the comparison shows.
7. **Quantify** the tow-altitude trade between near-field and far-field resolution
   and between ground coverage and absorption.

## Prerequisites

- [15-02-02 Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) —
  the swath geometry and the sound-speed dependence shared with this method.
- [15-01-01 Seawater Properties: Temperature, Salinity, Density](../01-physical-oceanography/01-seawater-properties.md) —
  the sound speed and its variability, which set every range in metres.
- [05-02-02 Field Measurement Units and Instrumentation](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md) —
  the decibel and the logarithmic bookkeeping used throughout.

## 1. What the instrument returns

A side-scan sonar tows two transducers, one on each side, each fanning a thin
beam outward and downward. Per side, the instrument returns **echo intensity
against time**, so

$$r = \frac{c\,t}{2}$$

is a *slant* range to whatever produced the echo. Three consequences follow.

- **The image is not a plan view.** Two features at the same plan distance from the
  track but different altitudes produce echoes at different times; the mapping
  from time to plan position requires the tow height $h$.
- **The echo strength depends on the observation geometry.** A flat, uniform
  seafloor does not produce a uniform image: it produces a bright band near the
  nadir and a dark far field, purely because the grazing angle falls.
- **The instrument images *texture*, not depth.** Its contrast comes from
  centimetre-scale roughness and from impedance — which is why it complements
  rather than duplicates the multibeam.

## 2. Slant range to ground range

For a flat seafloor at height $h$ below the tow-fish (called the altitude) and a
target at horizontal distance $x$ from the nadir:

$$r^{2} = x^{2} + h^{2}
\;\Longrightarrow\;
\boxed{\;x = \sqrt{r^{2} - h^{2}}, \qquad \frac{\mathrm{d}x}{\mathrm{d}r}
= \frac{r}{\sqrt{r^{2}-h^{2}}}.\;}$$

With $h = 20\ \mathrm{m}$:

| slant range $r$ (m) | ground range $x$ (m) | $x/r$ | stretch $\mathrm{d}x/\mathrm{d}r$ |
|---|---|---|---|
| 20.0 | 0.00 | 0.000 | diverges |
| 22.0 | 9.17 | 0.417 | 2.400 |
| 25.0 | 15.00 | 0.600 | 1.667 |
| 30.0 | 22.36 | 0.745 | 1.342 |
| 40.0 | 34.64 | 0.866 | 1.155 |
| 70.0 | 67.08 | 0.958 | 1.044 |
| 120.0 | 118.32 | 0.986 | 1.014 |
| 200.0 | 199.00 | 0.995 | 1.005 |

Three remarks. **The stretch diverges at nadir and tends to 1 at long range**, so
the near-field part of a record is compressed in plan view by an unbounded factor;
that is why the innermost part is usually discarded, and why a "nadir gap"
appears in a mosaic. **The first return is at $r = h$**, giving a blind zone in
ground range from 0 to $\sqrt{r_{\min}^{2}-h^{2}}$ — $9.2\ \mathrm{m}$ for a first
return 2 m beyond the nadir. And **the mapping requires $h$**, so an unknown or
varying altitude makes the geometric correction wrong in a range-dependent way:
a 1 m error in $h$ at $r = 25\ \mathrm{m}$ moves the ground position by
$\Delta x = -(h/x)\Delta h = -1.3\ \mathrm{m}$, which is larger than the
across-track resolution.

## 3. Grazing angle

$$\sin g = \frac{h}{r} .$$

| $r$ (m) | $g$ (deg) |
|---|---|
| 22 | 65.38 |
| 25 | 53.13 |
| 30 | 41.81 |
| 40 | 30.00 |
| 60 | 19.47 |
| 100 | 11.54 |
| 200 | 5.74 |

**The grazing angle spans $65^\circ$ to $5.7^\circ$ in a single side-scan
record.** Everything about the method's interpretation follows from that span,
because the backscatter is a strong function of it (Section 5).

## 4. Resolution

### 4.1 Across-track

The pulse has length $\tau$ in time, so it occupies $c\tau/2$ in range. Projected
onto a seafloor inclined at grazing angle $g$, that length becomes

$$\boxed{\;\ell_{\text{across}} = \frac{c\,\tau}{2\sin g}.\;}$$

### 4.2 Along-track

The azimuthal beam width $\Delta\phi$ subtends a length $R\,\Delta\phi$ at range
$R$:

$$\ell_{\text{along}} = R\,\Delta\phi .$$

With $c = 1500\ \mathrm{m\,s^{-1}}$, $\tau = 0.10\ \mathrm{ms}$
($c\tau/2 = 0.075\ \mathrm{m}$), $\Delta\phi = 0.5^\circ$, $h = 20\ \mathrm{m}$:

| $r$ (m) | $g$ (deg) | across-track (m) | along-track (m) |
|---|---|---|---|
| 22 | 65.38 | 0.0825 | 0.1920 |
| 30 | 41.81 | 0.1125 | 0.2618 |
| 50 | 23.58 | 0.1875 | 0.4363 |
| 100 | 11.54 | 0.3750 | 0.8727 |
| 200 | 5.74 | 0.7500 | 1.7453 |

Both degrade, by a factor 9 over this range, and the across-track term is the
finer of the two throughout. The physical reasons differ, and so do the remedies:

- the **along-track** resolution is proportional to range because the beam
  diverges; nothing in the processing can undo it, and the only remedies are a
  narrower beam (a longer array) or a shorter range;
- the **across-track** resolution is limited by the grazing angle, and since
  $\sin g \approx h/r$ at long range the formula becomes
  $\ell_{\text{across}} \approx c\tau r/(2h)$: **it is restored by towing
  lower.** The pulse length sets the floor, $c\tau/2$, which no geometry beats.

## 5. Backscatter and the angular response

The echo strength from a patch of seafloor depends on the incident angle through
the scattering law. A chosen teaching model is a power law in the sine of the
grazing angle:

$$I(g) = \sin^{n} g, \qquad \mathrm{TS}(g) = 10\log_{10}\!\left(\sin^{2} g\right)
= 20\log_{10}(\sin g)\ \mathrm{dB},$$

where $n = 2$ in the demonstration. (The two forms are the same statement: TS is
defined for *intensity*, so a factor $X$ in pressure is $20\log_{10}X$ dB and a
factor $X^{2}$ in intensity is $10\log_{10}X^{2} = 20\log_{10}X$ dB.)

| grazing (deg) | $\sin g$ | $I = \sin^{2}g$ | TS (dB) |
|---|---|---|---|
| 2.0 | 0.0349 | 0.0012 | $-29.14$ |
| 5.0 | 0.0872 | 0.0076 | $-21.19$ |
| 10.0 | 0.1736 | 0.0302 | $-15.21$ |
| 20.0 | 0.3420 | 0.1170 | $-9.32$ |
| 45.0 | 0.7071 | 0.5000 | $-3.01$ |
| 70.0 | 0.9397 | 0.8830 | $-0.54$ |
| 90.0 | 1.0000 | 1.0000 | 0.00 |

**A change of grazing angle from $45^\circ$ to $5^\circ$ changes the target
strength by 18 dB — a factor of 63 in intensity.** On a uniformly flat, uniformly
rough seafloor, therefore, a side-scan image is bright near the nadir and dark at
the far edge, with no geological cause whatever. Any interpretation of
backscatter *intensity* — as opposed to *texture* — requires a beam-pattern and
grazing-angle correction, and the correction requires the altitude.

The exponent $n$ is a property of the seafloor (rough rock scatters more
isotropically, smooth mud more specularly) and is often *the* quantity of
interest. That is the circularity of backscatter interpretation: the angular
correction needs an angular response, and the angular response is what one is
trying to measure. The resolution of the circle is to fit the angular response
over the full range of grazing angles available in one record — which is exactly
what the wide grazing-angle span of Section 3 provides.

## 6. The sonar equation

The active sonar equation, in decibels:

$$\mathrm{EL} = \mathrm{SL} - 2\,\mathrm{TL} + \mathrm{TS}
- \left(\mathrm{NL} - \mathrm{DI} + \mathrm{DT}\right),$$

with SL the source level, TL the one-way transmission loss, TS the target
strength of the ensonified patch, NL the noise level, DI the receiving directivity
index, DT the detection threshold, and EL the echo level. Transmission loss
combines spherical spreading with absorption:

$$\mathrm{TL} = 20\log_{10} R + \alpha R .$$

With the demonstration's chosen values $\mathrm{SL} = 220\
\mathrm{dB\,re\,1\,\mu Pa\,at\,1\,m}$, $\alpha = 0.10\ \mathrm{dB\,m^{-1}}$,
$\mathrm{NL} = 50\ \mathrm{dB}$, $\mathrm{DI} = 20\ \mathrm{dB}$,
$\mathrm{DT} = 10\ \mathrm{dB}$ (so $\mathrm{NL}-\mathrm{DI}+\mathrm{DT} = 40\
\mathrm{dB}$):

| $R$ (m) | TL (dB) | $2$TL (dB) | $g$ (deg) | TS (dB) | EL (dB) |
|---|---|---|---|---|---|
| 25 | 30.46 | 60.92 | 53.13 | $-1.94$ | 117.14 |
| 50 | 38.98 | 77.96 | 23.58 | $-7.96$ | 94.08 |
| 100 | 50.00 | 100.00 | 11.54 | $-13.98$ | 66.02 |
| 200 | 66.02 | 132.04 | 5.74 | $-20.00$ | 27.96 |
| 250 | 72.96 | 145.92 | 4.59 | $-21.94$ | 12.14 |
| 300 | 79.54 | 159.08 | 3.82 | $-23.52$ | $-2.61$ |
| 400 | 92.04 | 184.08 | 2.87 | $-26.02$ | $-30.10$ |

Solving $\mathrm{EL} = 0$ by bisection, and repeating with one parameter changed:

| change | range at EL $=0$ | factor |
|---|---|---|
| base case | 291.0 m | 1.00 |
| absorption halved ($0.05\ \mathrm{dB\,m^{-1}}$) | 461.6 m | 1.59 |
| noise level halved | 380.9 m | 1.31 |
| absorption doubled ($0.20\ \mathrm{dB\,m^{-1}}$) | 177.6 m | 0.61 |

**The measured sensitivity is smaller than a first guess would suggest, and that
is the useful result.** Halving the absorption multiplies the range by 1.59, not
by 2; halving the noise level multiplies it by 1.31. Neither change doubles the
range, because at the limiting range absorption, spreading *and* the falling
grazing-angle target strength all matter. An argument that "absorption dominates,
so halving it doubles the range" is qualitatively right and quantitatively
wrong — the kind of error that a budget exists to catch.

## 7. Tow altitude: two questions with opposite answers

**(i) At a fixed maximum slant range**, the ground half-width is
$\sqrt{R_{\max}^{2}-h^{2}}$ and the blind zone ends at $\sqrt{r_{\min}^{2}-h^{2}}$:

| altitude (m) | ground half-width (m) | blind zone ends (m) | grazing at 200 m (deg) |
|---|---|---|---|
| 5 | 199.9 | 4.9 | 1.43 |
| 10 | 199.7 | 6.6 | 2.87 |
| 20 | 199.0 | 9.2 | 5.74 |
| 40 | 196.0 | 12.8 | 11.54 |
| 80 | 183.3 | 18.0 | 23.58 |

Flying higher at fixed slant range **raises** the far-edge grazing angle from
$1.43^\circ$ to $23.58^\circ$, improving far-field across-track resolution, at the
cost of a larger blind zone and slightly less ground coverage. Flying lower gives
the opposite. The trade is therefore **near-field resolution against far-field
resolution**, not simply coverage against resolution.

**(ii) At a fixed ground half-width**, the required slant range is
$\sqrt{x^{2}+h^{2}}$, and the extra path costs absorption twice over:

| altitude (m) | required slant range for 200 m ground (m) | extra two-way loss vs 20 m (dB) |
|---|---|---|
| 5 | 200.1 | $-0.19$ |
| 20 | 201.0 | 0.00 |
| 40 | 204.0 | 0.59 |
| 80 | 215.4 | 2.88 |

Here the extra cost is small — $2.88\ \mathrm{dB}$ for a four-fold increase in
altitude — but it scales with $\alpha$, which at high frequency is the binding
constraint. **The two framings give different answers, and a survey must say
which question it was optimised for.** This is the honest form of the statement
"the altitude is a compromise".

## 8. Assumptions and regime of validity

1. **A flat seafloor and constant altitude.** Every formula uses a single $h$. On
   a slope the grazing angle and the ground position both change, and the
   geometric correction is not valid; on a sloping seabed a side-scan record's
   nadir-relative symmetry is broken.
2. **Straight-line rays.** Refraction in a layered ocean bends the path; as in
   multibeam, the effect is second-order in the gradient and first-order in range.
3. **A single scattering law.** The exponent $n$ is assumed constant over the
   record. Real seafloors change sediment type, and with it the angular response,
   *within* one record — which is the signal and the confound at once.
4. **No volume scattering.** Sediment with gas or with a rough sub-surface can
   return echoes from below the interface, which the surface-scattering model
   cannot represent.
5. **No multipath or side-lobe returns.** In shallow water the surface and the
   seafloor form a waveguide; the returns are contaminated, and a side-scan is
   difficult in water shallower than a few times the swath.
6. **Additive, homogeneous noise.** Real noise includes vessel machinery, other
   sonars and biology, none of which averages away.
7. **Intensity is corrected for geometry before interpretation.** The
   demonstration shows the size of the uncorrected effect ($18\ \mathrm{dB}$ over
   the record) so that the necessity is not a matter of taste.

## 9. Worked examples

### Example 1 — the geometry of one record

Altitude $15\ \mathrm{m}$, slant ranges from $17\ \mathrm{m}$ to
$130\ \mathrm{m}$.

- Ground range at the far edge: $\sqrt{130^{2}-15^{2}} = \sqrt{16900-225}
  = 129.13\ \mathrm{m}$.
- Blind zone: from $0$ to $\sqrt{17^{2}-15^{2}} = \sqrt{289-225} = 8.00\
  \mathrm{m}$.
- Grazing angles: at $17\ \mathrm{m}$, $\arcsin(15/17) = 61.93^\circ$; at
  $130\ \mathrm{m}$, $\arcsin(15/130) = 6.63^\circ$.
- Across-track resolution at the far edge with $\tau = 0.1\ \mathrm{ms}$:
  $\dfrac{c\tau/2}{\sin g} = \dfrac{0.075}{\sin 6.63^\circ}
  = \dfrac{0.075}{0.11540} = 0.650\ \mathrm{m}$.

### Example 2 — the grazing correction in decibels

Suppose the correction is *not* applied and a geologist interprets the brightness
as roughness. At the near field ($r = 25\ \mathrm{m}$, $g = 53.13^\circ$) the
model gives $\mathrm{TS} = -1.94\ \mathrm{dB}$; at the far edge
($r = 200\ \mathrm{m}$, $g = 5.74^\circ$) it gives $-20.00\ \mathrm{dB}$. A patch
of seafloor of identical roughness would therefore appear $18.06\ \mathrm{dB}$
darker at the far edge — a factor $10^{18.06/10} = 64$ in intensity.
**Any "roughness" map made from uncorrected amplitude is a map of grazing angle
with a roughness anomaly superimposed.** The correction is
$+20\log_{10}(\sin g)$ to first order, plus a beam-pattern term that depends on
the transducer and must be measured.

### Example 3 — the cost of a longer pulse

Doubling the pulse length to $\tau = 0.2\ \mathrm{ms}$ doubles the floor on the
across-track resolution, from $c\tau/2 = 0.075\ \mathrm{m}$ to
$0.150\ \mathrm{m}$, and it raises the echo level by
$10\log_{10}(2) = 3.01\ \mathrm{dB}$ because twice the energy enters the water.
Solving the same $\mathrm{EL}=0$ bisection with SL raised by $3.01\ \mathrm{dB}$
moves the maximum range from $291.0\ \mathrm{m}$ to $301.4\ \mathrm{m}$ — a
**$3.6\,\%$** gain. So the trade is stark and unfavourable: **doubling the pulse
length costs a factor 2 in across-track resolution and buys 3.6 % in range.** The
reason is that the limiting loss is dominated by $\alpha R$, which is linear in
range, so a fixed decibel gain converts into only a small range gain. A chirp
sweep ([Lesson 04](04-sub-bottom-profiling.md)) is the standard escape: it keeps
the resolution of a short pulse while transmitting the energy of a long one.

## 10. Python demonstration

`code/side_scan_sonar_demo.py` prints everything above with units:

1. the slant-to-ground mapping, the stretch factor and the blind zone;
2. grazing angle against range;
3. across-track and along-track resolution against range;
4. an angular backscatter model in decibels;
5. a sonar-equation budget, plus a **bisection** for the maximum range under four
   parameter changes;
6. the tow-altitude trade under both framings;
7. verification: the exact composition of the slant-to-ground map with its
   inverse ($5.7\times10^{-14}\ \mathrm{m}$), the decibel bookkeeping, and the
   pulse-length floor.

Run it with

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python side_scan_sonar_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/03-side-scan-sonar-exercises.md`](exercises/03-side-scan-sonar-exercises.md)
and
[`exercises/03-side-scan-sonar-solutions.md`](exercises/03-side-scan-sonar-solutions.md).

- ★ Compute the ground range, grazing angle and stretch factor for
  $h = 12\ \mathrm{m}$ at $r = 14$, $25$ and $90\ \mathrm{m}$.
- ★★ Derive $\ell_{\text{across}} = c\tau/(2\sin g)$ and evaluate it at
  $g = 60^\circ$, $20^\circ$ and $5^\circ$ for $\tau = 0.08\ \mathrm{ms}$.
- ★★ Compute the TS change between grazing $40^\circ$ and $8^\circ$ under the
  $\sin^{2}$ model, in dB and as an intensity ratio.
- ★★★ Design a survey and an analysis that would measure the backscatter angular
  exponent $n$ of a seafloor patch, stating how you break the circularity between
  the angular correction and the angular response.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use
$c = 1500\ \mathrm{m\,s^{-1}}$, $\tau = 0.1\ \mathrm{ms}$,
$\Delta\phi = 0.5^\circ$, $h = 25\ \mathrm{m}$, $R_{\max} = 150\ \mathrm{m}$.

> **(a)** Compute the ground range at the far edge, the blind zone for a first
> return 1.5 m beyond the nadir, and the grazing angle at the far edge.
> **(b)** Compute the across-track and along-track resolution at the far edge and
> state which is worse and why.
> **(c)** Compute the target strength at the far edge and at $r = 40\ \mathrm{m}$
> under the $\sin^{2}$ model, and state the difference in dB and as an intensity
> ratio.
> **(d)** The tow is raised to $60\ \mathrm{m}$ keeping $R_{\max} = 150\
> \mathrm{m}$. Compute the new far-edge grazing angle and the new blind zone, and
> state what was gained and what was lost.

A worked version of (a)–(d) is in the lesson-03
[solutions](exercises/03-side-scan-sonar-solutions.md).

## Common pitfalls

1. **Treating a side-scan record as a plan view.** The time axis is slant range,
   and the stretch diverges at nadir.
2. **Interpreting uncorrected amplitude as roughness.** The grazing-angle term is
   worth up to $18\ \mathrm{dB}$ over one record; it must be removed first.
3. **Assuming one resolution.** Both resolutions degrade by about a factor of nine
   across a record, for different reasons and with different remedies.
4. **Believing the range is absorption-limited and so scales as $1/\alpha$.** The
   measured factor is 1.59 for halving $\alpha$, not 2.
5. **Choosing a pulse length for resolution alone.** It trades against energy and
   therefore against range.
6. **Towing high or low without stating the question.** The altitude optimises
   near-field resolution or far-field resolution, not both.
7. **Using an unknown altitude.** The geometric correction depends on $h$, and at
   short range a 1 m altitude error moves the plan position further than the
   resolution.

## Related modules

- [02 Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) —
  the geometry and sound-speed dependence shared with this method, and the depth
  that complements the backscatter.
- [04 Sub-Bottom Profiling and Chirp Systems](04-sub-bottom-profiling.md) —
  the same pulse-length-versus-bandwidth trade, carried to its logical end.
- [Module 15-02 README](README.md) — how the methods in this module fit together.
- [Module 15-04 Seafloor Mapping and Habitat Characterisation](../04-seafloor-mapping-and-habitats/README.md) —
  what a backscatter mosaic is used for, and the classification that consumes it.
- [20-01-04 Transfer Functions and Frequency Response](../../20-signal-processing/01-signals-and-systems/04-transfer-functions.md) —
  the beam pattern and pulse as filters, in the frequency domain.

## Self-assessment checklist

- [ ] I can derive and invert the slant-to-ground mapping.
- [ ] I can compute a grazing angle and say why its span matters.
- [ ] I can derive both resolution terms and say which remedy applies to each.
- [ ] I can convert a backscatter model between intensity and amplitude decibels.
- [ ] I can assemble the sonar equation and solve it by bisection.
- [ ] I can measure the range sensitivity to $\alpha$ and to NL and state the
      result.
- [ ] I can state the two framings of the tow-altitude trade.
