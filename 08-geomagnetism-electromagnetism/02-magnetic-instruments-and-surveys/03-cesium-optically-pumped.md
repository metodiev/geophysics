---
id: 08-02-03
title: "Optically Pumped Cesium and Potassium Magnetometers"
level: graduate
prereqs: ["08-02-02", "02-09-01", "02-07-07"]
tags: [geomagnetism, instruments, optically-pumped, cesium, potassium, zeeman, breit-rabi, heading-error]
---

# Optically Pumped Cesium and Potassium Magnetometers

Optically pumped alkali magnetometers reach the highest resolution of any field
instrument, and they do it by measuring a frequency roughly a hundred times
higher than a proton sensor's. That choice of species is not arbitrary: it is
fixed by the quantum numbers of the atom through the Landé factor and the
hyperfine structure. This lesson derives the frequency from the quantum numbers
using only standard constants, shows why the **stretched** state is exactly linear
in the field, quantifies the quadratic Zeeman shift of the field-independent
transition, and then treats the two error mechanisms that dominate field use:
heading error and dead zones.

**All models and data in this module are SYNTHETIC.** Cell design, pumping
geometry, light shift, noise floors and sensitivities are chosen teaching values.
The standard constants used are the electron spin $g$-factor, the Bohr magneton,
the Planck constant, the electron/proton mass ratio and the caesium hyperfine
frequency that defines the SI second. No instrument or published specification is
described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the Landé factor $g_F$ of a hyperfine level from $I$, $J$ and $F$,
   including the order of magnitude of the nuclear term that is usually neglected.
2. **Compute** the Larmor frequency and the sensitivity in $\mathrm{Hz\,nT^{-1}}$
   for a given alkali species.
3. **Show** that the Breit–Rabi radical is a perfect square for the stretched
   state, so that state is exactly linear in $B$ at all fields.
4. **Compute** the quadratic Zeeman shift of the $m_F = 0$ transition and find
   the field at which it reaches a stated size.
5. **Distinguish** a second-order heading error from the first-order cross-axis
   error of a fluxgate, and compute both.
6. **Explain** dead zones and their operational consequences.
7. **Budget** the resolution of an alkali sensor, including the terms that
   dominate outside the laboratory.

## Prerequisites

- [08-02-02 Proton Precession and Overhauser Magnetometers](02-proton-overhauser.md) —
  the scalar-sensor idea and the Larmor relation.
- [02-09-01 Atomic Structure and Energy Levels](../../02-physics/09-radiation-and-atomic-physics/01-atomic-structure.md)
  — hyperfine structure and the quantum numbers used here.
- [02-07-07 Magnetisation, Susceptibility and Magnetic Materials](../../02-physics/07-electromagnetism/07-magnetisation-materials.md)
  — magnetic moments, and the Bohr magneton.

## 1. The frequency comes from quantum numbers

The alkali ground state has $J = 1/2$ (one valence electron) and nuclear spin
$I$ (caesium: $I = 7/2$; potassium and rubidium: $I = 3/2$). Hyperfine coupling
gives levels $F = I \pm 1/2$, each split by the magnetic field into $2F+1$
Zeeman sublevels. For weak fields the splitting is linear, and the level's
effective $g$-factor is the **Landé factor**

$$g_F = g_J\frac{F(F+1)+J(J+1)-I(I+1)}{2F(F+1)}
+ g_I\frac{m_e}{m_p}\frac{F(F+1)+I(I+1)-J(J+1)}{2F(F+1)},$$

with $g_J \approx g_s = 2.00231930436256$ for a $^2S_{1/2}$ state. The transitions
used observe $\Delta m_F = \pm1$, at the frequency

$$f = g_F\,\frac{\mu_B}{h}\,B, \qquad
\frac{\mu_B}{h} = \frac{9.2740100783\times10^{-24}}{6.62607015\times10^{-34}}
= 1.399624\times10^{10}\ \mathrm{Hz\,T^{-1}}.$$

### 1.1 Computing $g_F$

For caesium, $I = 7/2$, $J = 1/2$, $F = 4$:
$F(F+1) = 20$, $J(J+1) = 0.75$, $I(I+1) = 15.75$, so

$$g_F = g_J\frac{20+0.75-15.75}{40} = g_J\times0.125
= 0.125\times2.002319 = +0.250290.$$

For potassium, $I = 3/2$, $J = 1/2$, $F = 2$:
$F(F+1) = 6$, $I(I+1) = 3.75$, so

$$g_F = g_J\frac{6+0.75-3.75}{12} = g_J\times0.25 = +0.500580.$$

The demonstration prints, for each species, $g_F$ and the sensitivity
$|g_F|\mu_B/h$ in $\mathrm{Hz\,nT^{-1}}$:

| species | $I$ | $J$ | $F$ | $g_F$ | sensitivity (Hz/nT) |
|---|---|---|---|---|---|
| Cs-133 | 3.5 | 0.5 | 4.0 | +0.25029 | 3.50312 |
| Cs-133 | 3.5 | 0.5 | 3.0 | −0.25029 | 3.50312 |
| K-39 | 1.5 | 0.5 | 2.0 | +0.50058 | 7.00624 |
| K-39 | 1.5 | 0.5 | 1.0 | −0.50058 | 7.00624 |
| Rb-87 | 1.5 | 0.5 | 2.0 | +0.50058 | 7.00624 |

so a caesium sensor counts at $3.50312\ \mathrm{Hz\,nT^{-1}}$ and a potassium
sensor at $7.00624\ \mathrm{Hz\,nT^{-1}}$: **82 times higher than the proton's
$0.0426\ \mathrm{Hz\,nT^{-1}}$**. Larmor frequencies follow:

| $B$ (nT) | $f_{\text{Cs}}$ (Hz) | $f_{\text{K}}$ (Hz) |
|---|---|---|
| 10000 | 35031.19 | 70062.38 |
| 25000 | 87577.97 | 175155.95 |
| 50000 | 175155.95 | 350311.89 |
| 100000 | 350311.89 | 700623.79 |

For comparison, the proton frequency at a $50000\ \mathrm{nT}$ field is
$2128.87\ \mathrm{Hz}$ (lesson 02). Counting 175 kHz rather than 2.1 kHz is
easier by the same factor, and that factor is the origin of the alkali sensor's
resolution advantage.

### 1.2 The nuclear term that this model neglects

The second term of $g_F$ is the nuclear contribution. Its magnitude is at most

$$|g_I|\frac{m_e}{m_p}\times\frac{7}{8}
\le 1\times5.446170\times10^{-4}\times0.875 = 4.77\times10^{-4},$$

which is up to **0.19%** of $g_F$ for caesium. That is *not* negligible at the
0.1% level. The consequence is a statement about practice: a real instrument's
constant is fixed by **spectroscopy**, not computed from $g_s$ alone, and this
lesson's derived numbers are a model of the right order, not a calibration.

## 2. Breit–Rabi: when the linear relation fails

For $J = 1/2$ the level energies are given exactly by the **Breit–Rabi** formula

$$E = -\frac{h f_{\text{hfs}}}{2(2I+1)}
+ \frac{\mu_B}{h}g_I\frac{m_e}{m_p}m_FB
\;\pm\;\frac{h f_{\text{hfs}}}{2}
\sqrt{1+\frac{4m_Fx}{2I+1}+x^{2}},$$

with $x = (g_J-g_I)\mu_BB/(h f_{\text{hfs}})$ and the sign following
$F = I \pm 1/2$. For caesium the hyperfine splitting is
$f_{\text{hfs}} = 9192631770\ \mathrm{Hz}$, a value fixed by the definition of the
SI second rather than measured.

### 2.1 The stretched state is exactly linear

Take the stretched state $m_F = F = I + 1/2$. Then

$$\frac{4m_F}{2I+1} = \frac{4(I+\tfrac12)}{2I+1} = 2,
\qquad\text{so}\qquad
1+2x+x^{2} = (1+x)^{2}, \qquad \sqrt{\cdot} = 1+x \ \text{exactly}.$$

The radical is a perfect square, so the energy is a **strictly linear** function
of $B$ at every field. The demonstration verifies it numerically:

| $B$ (nT) | $m_F = 4$ shift (Hz) | deviation from linear | $m_F = 1$ deviation |
|---|---|---|---|
| 50000 | 700623.7856 | $-7.3\times10^{-13}$ | $+2.9\times10^{-4}$ |
| 100000 | 1401247.5712 | $-5.0\times10^{-14}$ | $+5.7\times10^{-4}$ |
| $10^{6}$ | 14012475.7120 | $+1.8\times10^{-14}$ | $+5.7\times10^{-3}$ |
| $10^{7}$ | 140124757.1204 | $-2.1\times10^{-15}$ | $+5.7\times10^{-2}$ |

The residual for $m_F = 4$ is floating-point round-off; for $m_F = 1$ the
deviation is real (about $5.7\times10^{-4}$ relative at $10^{6}\ \mathrm{nT}$)
and grows quadratically. **This is why alkali magnetometers use stretched
states**: linearity over a range far wider than the Earth's field, with no
need for a field-dependent calibration.

### 2.2 The quadratic Zeeman shift of $m_F = 0$

The transition $(F=3, m_F=0)\to(F=4, m_F=0)$ has no linear shift, so its field
dependence is pure quadratic. The demonstration computes from Breit–Rabi:

| $B$ (nT) | shift (Hz) | shift/$B^2$ (Hz nT⁻²) |
|---|---|---|
| 10000 | 4.2719 | $4.2719\times10^{-8}$ |
| 25000 | 26.6993 | $4.2719\times10^{-8}$ |
| 50000 | 106.7972 | $4.2719\times10^{-8}$ |
| 100000 | 427.1888 | $4.2719\times10^{-8}$ |
| 150000 | 961.1748 | $4.2719\times10^{-8}$ |

The constant ratio is the definition of a quadratic shift, and the demonstration
finds that it reaches **1 kHz at $B = 153000\ \mathrm{nT}$**
($153.0\ \mu\mathrm{T}$). Note what that means in both directions:

- A **clock** wants the smallest possible field, because any field contaminates
  the frequency: this is why primary frequency standards shield their C-field
  region to nanotesla levels.
- A **magnetometer** wants the opposite — a large, linear response — and
  therefore uses the stretched state, not the clock transition. The same physics
  that makes the transition good for timekeeping makes it bad for field
  measurement, and vice versa.

## 3. Heading error: second order, and why that matters

An alkali sensor is pumped and probed along an optical axis $\hat{\mathbf{o}}$.
The measured frequency depends on the angle $\theta$ between $\hat{\mathbf{o}}$
and $\mathbf{B}$ only through a term that is second order in the transverse
field,

$$\frac{\delta f}{f} = c\sin^{2}\theta \quad (c \ll 1),$$

because the leading first-order effect is a line-shape asymmetry (the
"heading error") that is arranged to cancel at the operating point. With a
SYNTHETIC coefficient $c = 5.0\times10^{-4}$:

| $\theta$ (°) | $\sin^2\theta$ | relative error | error at 50000 nT |
|---|---|---|---|
| 0.5 | $7.6\times10^{-5}$ | $3.8\times10^{-8}$ | 0.0019 nT |
| 1.0 | $3.1\times10^{-4}$ | $1.5\times10^{-7}$ | 0.0076 nT |
| 2.0 | $1.2\times10^{-3}$ | $6.1\times10^{-7}$ | 0.0304 nT |
| 5.0 | $7.6\times10^{-3}$ | $3.8\times10^{-6}$ | 0.1899 nT |
| 10.0 | $3.0\times10^{-2}$ | $1.5\times10^{-5}$ | 0.7538 nT |

Even at a $10^{\circ}$ misalignment the error is under a nanotesla. Contrast the
fluxgate ([08-02-01](01-fluxgate-magnetometers.md) §4), whose cross-axis leak is
$B_\perp\sin\alpha$ — **first order**, giving 873 nT for a $1^{\circ}$ error in a
50000 nT field. Three orders of magnitude more sensitive to orientation, for the
same nominal field.

The practical consequence is decisive: an alkali sensor can be flown on a
light aircraft or carried by hand without a levelling gimbal, whereas a
three-axis fluxgate cannot. In exchange, the alkali sensor gives only
$|\mathbf{B}|$.

## 4. Dead zones

The pumping and probe beams define the optical axis, and the signal amplitude
falls as $\sin\theta$: along $\hat{\mathbf{o}}$ the sample is pumped into a state
that the probe cannot read as a field-dependent signal. With a SYNTHETIC noise
floor at $5.0\times10^{-3}$ of the full signal amplitude:

| $\theta$ (°) | signal (fraction of full) | usable? |
|---|---|---|
| 0.05 | 0.000873 | no — dead zone |
| 0.2 | 0.003491 | no — dead zone |
| 0.5 | 0.008727 | yes |
| 1.0 | 0.017452 | yes |
| 45.0 | 0.707107 | yes |
| 90.0 | 1.000000 | yes |

So the dead zone is a cone of roughly $\pm0.3^{\circ}$ about the field direction
for this design. Two operational notes:

- **A moving platform sweeps through it.** An aircraft or a vehicle changes its
  attitude relative to the field continuously, so the dead-zone cone is crossed;
  a single-sensor scalar instrument therefore needs either a gimbal that keeps
  the axis well away from the field direction, or a second sensor on an
  orthogonal axis, or a component instrument for those intervals.
- **Design choices change the cone.** Multi-beam and self-oscillating designs
  reduce the dead zone at the cost of complexity, which is why the shape of the
  sensor head, not its quantum physics, is often the interesting engineering.

## 5. The resolution budget

The intrinsic floor of the demonstration's model is $1.0\ \mathrm{pT/\sqrt{Hz}}$,
which over a stated bandwidth gives

| bandwidth (Hz) | noise (nT rms) |
|---|---|
| 10.0 | 0.00316 |
| 1.0 | 0.00100 |
| 0.1 | 0.00032 |

These are *nanotesla-class or better* figures, and they are not what limits a
field survey. The real budget adds:

1. **Heading error** (§3): $0.75\ \mathrm{nT}$ at $10^{\circ}$ of misalignment —
   two orders of magnitude above the floor.
2. **Orientation knowledge of the platform**: for an airborne survey, attitude is
   known to a fraction of a degree at best, so the heading term is irreducible at
   the 0.01–0.1 nT level.
3. **Calibration of the sensor constant**: a 0.1% error in the constant is a
   50 nT error in a 50000 nT field, which is why absolute accuracy depends on
   spectroscopy and on a comparison with an absolute standard, not on the
   sensor's resolution.
4. **The main field's temporal variation**: a diurnal change of tens of nT is
   thousands of times the resolution, and it is removed by a base station, not by
   the sensor.

**The lesson of the budget is that resolution and accuracy are different
promises.** An alkali magnetometer offers exquisite resolution — the ability to
see a small *change* — and its *accuracy* is limited by the same
orientation, calibration and reference-field problems as any other instrument.

## 6. Assumptions and regime of validity

1. **Weak-field Zeeman limit for the linear relation.** Section 2 quantifies the
   departure; the Earth's field is three orders of magnitude below the hyperfine
   splitting, so the linear form is excellent — for the stretched state, exact.
2. **The nuclear moment is neglected in §1.** Its effect is up to 0.19% on $g_F$;
   real constants are spectroscopic.
3. **A single, well-defined optical axis.** Multi-beam and anti-relaxation-coated
   cells complicate the geometry but not the quantum numbers.
4. **Light shift and buffer-gas effects are absent.** Both scale with the pumping
   intensity and can be stabilised, but they are calibration terms in a real
   instrument.
5. **A uniform field over the cell.** A gradient broadens the resonance and
   degrades resolution exactly as it does for protons.
6. **Synthetic coefficients.** $c$, the dead-zone noise fraction and the noise
   floor are teaching values.

## 7. Python demonstration

`code/cesium_optically_pumped_demo.py` prints, with units:

1. $g_F$ and the sensitivity in $\mathrm{Hz\,nT^{-1}}$ for caesium, potassium and
   rubidium, with the neglected nuclear term bounded;
2. the Larmor frequency at four fields for caesium and potassium;
3. the Breit–Rabi shift of the stretched state compared with the linear model,
   and of $m_F = 1$, showing the perfect-square result and the first real
   nonlinearity;
4. the quadratic Zeeman shift of the $m_F = 0$ transition and the field at which
   it reaches 1 kHz;
5. heading error versus misalignment;
6. the dead-zone cone and the signal-loss table;
7. the noise floor versus bandwidth.

Exercises and solutions:
[`exercises/03-cesium-optically-pumped-exercises.md`](./exercises/03-cesium-optically-pumped-exercises.md),
[`exercises/03-cesium-optically-pumped-solutions.md`](./exercises/03-cesium-optically-pumped-solutions.md).

## Mastery checkpoint

1. Compute $g_F$ for $I = 3/2$, $J = 1/2$, $F = 2$ and hence the sensitivity in
   Hz/nT.
2. Compute the precession frequency of a potassium sensor in a
   $48000\ \mathrm{nT}$ field.
3. Show algebraically that the Breit–Rabi radical is a perfect square for the
   stretched state.
4. Compute the quadratic Zeeman shift of the $m_F = 0$ transition at
   $75000\ \mathrm{nT}$ using the constant $4.2719\times10^{-8}\
   \mathrm{Hz\,nT^{-2}}$.
5. Compute the heading error at $8^{\circ}$ with $c = 5\times10^{-4}$ in a
   50000 nT field, and compare with a fluxgate's $1^{\circ}$ cross-axis error.
6. Name the four terms of the resolution budget that dominate the intrinsic
   noise floor.

## Common pitfalls

1. **Quoting resolution as accuracy.** Section 5 is the distinction.
2. **Using the $m_F = 0$ transition as a magnetometer.** It is field-independent
   to second order: good for clocks, poor for fields.
3. **Assuming the computed constant is the instrument's constant.** The nuclear
   term is up to 0.19%.
4. **Forgetting the dead zone.** It is a cone, and a moving platform crosses it.
5. **Comparing the heading error with a fluxgate's without checking the order.**
   Second order versus first order is the whole story.
6. **Confusing an Overhauser sensor with an optically pumped one.** One polarises
   protons at 0.0426 Hz/nT; the other polarises electrons in an alkali vapour at
   3.5 or 7.0 Hz/nT.

## Related modules

- [08-02-02 Proton Precession and Overhauser Magnetometers](02-proton-overhauser.md) —
  the slower but simpler scalar alternative.
- [08-02-05 Airborne Magnetic Surveys and Compensation](05-airborne-magnetic-surveys.md) —
  where heading error and dead zones become survey design.
- [02-09 Radiation, Atomic Physics and Radioactivity](../../02-physics/09-radiation-and-atomic-physics/README.md) —
  hyperfine structure and spectroscopy.
- [08-01-01 Describing the Main Field: Declination, Inclination, Intensity](../01-earth-magnetic-field/01-main-field-description.md) —
  the quantities a scalar instrument can and cannot deliver.

## Self-assessment checklist

- [ ] I can compute $g_F$ and the sensitivity from $I$, $J$, $F$.
- [ ] I can state why the stretched state is exactly linear.
- [ ] I can compute a quadratic Zeeman shift.
- [ ] I can compare first-order and second-order heading errors with numbers.
- [ ] I can explain a dead zone and its operational consequence.
- [ ] I can separate resolution from accuracy in a budget.
