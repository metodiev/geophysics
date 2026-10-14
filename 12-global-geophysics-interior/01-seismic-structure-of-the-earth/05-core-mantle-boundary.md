---
id: 12-01-05
title: "Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite"
level: research
prereqs: ["12-01-01", "12-01-03", "06-01-02", "02-05-06"]
tags: [global-geophysics, earth-interior, core-mantle-boundary, ulvz, post-perovskite, reflectivity, d-double-prime]
---

# Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite

> **All models and data in this module are SYNTHETIC.** Densities, velocities,
> layer thicknesses, the Clapeyron slope and the reference temperature used here
> are chosen teaching values. No seismogram, station, event or published
> measurement is used. The CMB depth (2891 km) and the base-of-mantle velocities
> are the same chosen values as in lesson 01, and "D''" and "ULVZ" are used as
> labels, not as claims about the real Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** elastic impedance contrasts and reflection coefficients at the
   CMB, and **explain** why S is totally reflected while P is nearly transmitted.
2. **Derive** the postcursor delay of a wave that traverses an ultra-low-velocity
   zone, $\delta t = 2h\left(v_s'^{-1} - v_s^{-1}\right)$, and **construct** the
   $(h,\delta v)$ family that reproduces a measured delay.
3. **Compute** the normal-incidence reflectivity of a layered stack with the
   input-impedance recursion, and **verify** it by energy conservation.
4. **Explain** when a waveform resolves a layer that a travel time cannot: the
   separation $2h/v_s'$ must exceed the period *and* the impedance contrast must be
   large enough to produce visible reverberations.
5. **Derive** the depth of a post-perovskite transition in D'' from a pressure
   difference, and **explain** why the transition switches off above a threshold
   temperature that depends on the Clapeyron slope.
6. **Report** every structure as a time divided by a velocity model, and state the
   resulting ambiguity.
7. **State** which of D'' thickness, ULVZ thickness, ULVZ velocity drop and CMB
   temperature are directly measured and which are inferred.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the base-of-mantle velocities used throughout.
- [12-01-03 Upper-Mantle Discontinuities at 410 and 660 km](03-upper-mantle-discontinuities.md) —
  the same Clapeyron-slope argument and the sharpness-versus-frequency idea.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) —
  why a fluid has no S impedance.
- [02-05-06 Geotherms](../../02-physics/05-thermodynamics/06-geotherms.md) —
  the temperature profile whose crossing with a phase boundary defines D''.

## 1. The CMB is two different boundaries at once

Take the SYNTHETIC base-of-mantle values of
[lesson 01](01-prem-and-reference-models.md) —
$\rho = 5.57\ \mathrm{g\,cm^{-3}}$, $v_p = 13.72$, $v_s = 7.26\
\mathrm{km\,s^{-1}}$ — above an outer core with $\rho = 9.90$, $v_p = 8.06$ and
$v_s = 0$. The normal-incidence reflection coefficient is
$R = (Z_2 - Z_1)/(Z_2 + Z_1)$ with $Z = \rho v$:

| phase | $Z_\text{mantle}$ | $Z_\text{core}$ | $R$ |
|---|---|---|---|
| S (SH) | 40.438 | **0.000** | **−1.0000** |
| P | 76.420 | 79.794 | +0.0216 |

The consequences are the backbone of deep-Earth seismology:

- **A fluid cannot support shear**, so the outer core has zero S impedance and the
  CMB is a *free surface* for shear waves: $R = -1$ exactly, i.e. total reflection
  with polarity reversal. This is why ScS exists, why S does not disappear at the
  CMB the way P does, and why the S shadow zone is not the P shadow zone.
- **The P impedance contrast is 2 %**, so P energy is almost transparent. P
  therefore *enters* the core, which is how the core's own structure is measured at
  all (lesson [06](06-outer-and-inner-core.md)).
- Everything that follows in this lesson is a measurement of a small departure from
  those two clean numbers.

## 2. The ULVZ and the postcursor delay

An **ultra-low-velocity zone** is a layer a few to a few tens of kilometres thick
at the very base of the mantle with strongly reduced velocities. The demonstration
models it with a chosen parametrisation: $v_s$ reduced by a fraction $\delta$,
$v_p$ by $\delta/2$, and density *increased* by $1.30\,\delta$.

Because the layer is slow, an S wave that penetrates it and reflects at the true
CMB arrives later than the reference reflection by the extra time spent inside:

$$\boxed{\;\delta t = 2h\left(\frac{1}{v_s'} - \frac{1}{v_s}\right),\qquad
v_s' = v_s(1-\delta).\;}$$

For the SYNTHETIC model:

| $\delta$ (%) | $v_s'$ (km s$^{-1}$) | $\delta t$, $h = 10$ km | $h = 20$ km | $h = 30$ km |
|---|---|---|---|---|
| 5 | 6.897 | 0.145 | 0.290 | 0.435 |
| 10 | 6.534 | 0.306 | 0.612 | 0.918 |
| 20 | 5.808 | 0.689 | 1.377 | 2.066 |
| 30 | 5.082 | 1.181 | 2.361 | 3.542 |

**A delay is all a travel-time measurement returns.** Everything about the layer
comes from dividing that one number between two unknowns.

### 2.1 The degeneracy, explicitly

Fixing $\delta t = 1.000\ \mathrm{s}$ and solving for $\delta$ at each thickness:

| $h$ (km) | required $\delta$ (%) | $v_s'$ (km s$^{-1}$) |
|---|---|---|
| 5.0 | 42.06 | 4.206 |
| 10.0 | 26.63 | 5.326 |
| 15.0 | 19.49 | 5.845 |
| 20.0 | 15.36 | 6.145 |
| 30.0 | 10.79 | 6.476 |
| 40.0 | 8.32 | 6.656 |

Every row is indistinguishable in the delay. A 5 km layer with a 42 % velocity
reduction and a 40 km layer with an 8 % reduction produce the *same* number, so
neither thickness nor velocity drop is determined by a delay measurement. Note also
how the two ends differ in plausibility: a 42 % velocity reduction is extreme,
while 8 % is modest — the *family* is constrained by mineral physics, not by
seismology.

## 3. The full waveform: what a reflection really returns

The exact normal-incidence response of the stack (mantle | ULVZ | core) is obtained
from the input-impedance recursion, evaluated upward from the core:

$$Z_\text{in}^{(k)} = Z_k\,
\frac{Z_\text{in}^{(k+1)} + iZ_k\tan\left(\omega\tau_k\right)}
{Z_k + iZ_\text{in}^{(k+1)}\tan\left(\omega\tau_k\right)},
\qquad
R = \frac{Z_\text{in}^{(0)} - Z_0}{Z_\text{in}^{(0)} + Z_0},$$

with $\tau_k$ the one-way travel time in layer $k$ and $Z_\text{in}$ for the core
identically zero. Two checks make this trustworthy:

- for a single interface it reduces to $(Z_2-Z_1)/(Z_2+Z_1)$;
- for a *uniform* layer over a free surface it delays the pulse by exactly the
  two-way travel time in the layer — the physical answer, and a sign-convention
  trap that a careless derivation gets backwards.

The demonstration convolves a Ricker wavelet of dominant frequency $f_0$ with
$R(f)$ and reports, for the family of Section 2.1 (all with the same 1.000 s
delay):

| $h$ (km) | $2h/v_s'$ (s) | peak time (s) | pulse width (s) | energy | $r_\text{top}$ |
|---|---|---|---|---|---|
| 5.0 | 2.38 | 2.50 | 9.50 | 1.000 | −0.055 |
| 10.0 | 3.75 | 4.00 | 9.50 | 1.000 | −0.006 |
| 20.0 | 6.51 | 6.50 | 9.00 | 1.000 | +0.008 |
| 40.0 | 12.02 | 12.00 | 9.00 | 1.000 | +0.008 |

$(f_0 = 0.08\ \mathrm{Hz};\ \text{widths at } f_0 = 0.40\ \mathrm{Hz} \text{ are}
1.0\text{–}1.5\ \mathrm{s}.)$

Three quantitative results, and one honest negative:

1. **The peak time tracks $2h/v_s'$** to within 0.25 s in every case (2.50 vs 2.38,
   4.00 vs 3.75, 6.50 vs 6.51, 12.00 vs 12.02). The composite response behaves as a
   single arrival delayed by the two-way time through the layer, so subtracting
   $2h/v_s$ from the peak time recovers the postcursor delay of Section 2 — about
   1.0 s — in every model. The layer acts as a **delay line**.
2. **Energy is conserved to 0.1 %.** With $|R| = 1$ the filter is all-pass, so all
   the incident energy returns. This is a check on the arithmetic, not a physical
   discovery.
3. **The pulse width barely changes**, at either frequency. The reason is in the
   last column: the impedance contrast at the top of the layer, $r_\text{top}$,
   is only **−5.5 % to +0.8 %**, because the density increase ($1.30\,\delta$)
   partly cancels the velocity decrease. Internal reverberations are therefore
   ≤ 5 % of the main arrival and cannot be seen above a 50 % threshold.
4. **The honest negative: in this model the waveform does *not* break the
   degeneracy.** 5 km/42 % and 40 km/8 % give the same delay *and* nearly the same
   pulse. The condition for resolving the layer is twofold — the separation
   $2h/v_s'$ must exceed the dominant period, *and* the reflections from the two
   interfaces must be strong enough to be visible. Here the first condition is met
   at 0.40 Hz for the thicker models and the second is not met for any of them.

Breaking the ambiguity therefore requires one of:

- a **larger impedance contrast**, i.e. a much larger density increase than
  $1.30\,\delta$ (a real mineral-physics question, so a real lever);
- **shorter-period energy** that resolves the top reflection as a separate phase;
- an **independent constraint**, such as a converted or core-reflected phase whose
  path weights the layer differently.

Anyone quoting a ULVZ thickness without one of these is quoting the middle of a
family.

## 4. D'' and post-perovskite: a threshold, not a number

"D''" is the name for the lowermost few hundred kilometres of the mantle, above the
CMB. Its most intriguing property is that it sometimes contains a *discontinuity*
and sometimes does not. The modern reading is that the discontinuity is a
**phase transition** — post-perovskite, Pv → pPv — which exists only if the local
temperature is low enough for the transition pressure to be reached before the
CMB.

Make the physics explicit. A phase boundary obeys
$P_\text{tr}(T) = P_0 + \gamma(T - T_0)$, and the pressure increases downward at
$\mathrm{d}P/\mathrm{d}z = \rho g$. Define $C$ as the amount by which the
transition pressure exceeds the CMB pressure at a reference temperature
$T_\text{ref}$:

$$\Delta P(T) = C - \gamma\left(T_\text{CMB} - T_\text{ref}\right),
\qquad
h_{D''} = \frac{\Delta P}{\rho g}.$$

The layer exists only while $\Delta P > 0$; the transition is therefore **switched
off** above the threshold temperature

$$T_\text{thresh} = T_\text{ref} + \frac{C}{\gamma}.$$

With the demonstration's chosen values $C = 10.0\ \mathrm{GPa}$,
$\rho = 5560\ \mathrm{kg\,m^{-3}}$, $g = 10.68\ \mathrm{m\,s^{-2}}$ and
$T_\text{ref} = 2500\ \mathrm{K}$:

$$\rho g = 59.38\ \mathrm{MPa\,km^{-1}}
\;\Longrightarrow\;
h_{D''}(T_\text{ref}) = \frac{10\,000}{59.38} = 168.4\ \mathrm{km},$$

and the response to temperature is $\mathrm{d}h/\mathrm{d}T = -\gamma/(\rho g)$,
i.e. **−134.7 m K$^{-1}$** for $\gamma = 8\ \mathrm{MPa\,K^{-1}}$. The
transition-zone-style table:

| $T_\text{CMB}$ (K) | $h_{D''}$ (km), $\gamma = 6$ | $\gamma = 8$ | $\gamma = 10$ MPa K$^{-1}$ |
|---|---|---|---|
| 2300 | 188.6 | 195.3 | 202.1 |
| 2500 | 168.4 | 168.4 | 168.4 |
| 2800 | 138.1 | 128.0 | 117.9 |
| 3200 | 97.7 | 74.1 | 50.5 |
| 3500 | 67.4 | 33.7 | **absent** |
| 3800 | 37.0 | **absent** | **absent** |
| 4200 | **absent** | **absent** | **absent** |

The threshold temperatures are

| $\gamma$ (MPa K$^{-1}$) | shut-off at (K) |
|---|---|
| 6 | 4167 |
| 8 | 3750 |
| 10 | 3500 |

This is the geodynamically important structure, and it is worth stating in words:
**a hot CMB thins D'' and eventually removes the discontinuity entirely**, and the
temperature at which that happens is set by a Clapeyron slope that seismology
cannot measure. That is why the presence or absence of a D'' discontinuity is
interpreted as evidence about temperature *only* together with mineral physics
([12-02-02](../02-composition-and-mineral-physics/02-high-pressure-experiments.md),
[12-02-03](../02-composition-and-mineral-physics/03-ab-initio-mineral-physics.md)).

Note also the *threshold* character: the observable is not a smooth function of
temperature at the switch-off, so a small temperature change near the threshold
produces a qualitative change in the seismic signature. Thresholds are where
inversions are most sensitive and least stable.

## 5. Everything here is a time divided by a velocity

A reflection from the top of D'' arrives before the CMB reflection by
$2h/v_s$. With $v_s = 7.26\ \mathrm{km\,s^{-1}}$ the two-way slowness is
$2/v_s = 0.27548\ \mathrm{s\,km^{-1}}$, so:

| measured delay (s) | $h$ for $v_s = 7.26$ (km) | $h$ if $v_s$ is 3 % lower (km) |
|---|---|---|
| 2.0 | 7.3 | 7.0 |
| 5.0 | 18.1 | 17.6 |
| 10.0 | 36.3 | 35.2 |
| 20.0 | 72.6 | 70.4 |

A 3 % velocity error moves the thickness by 3 %. That sounds benign, but the
velocity model between the surface and the CMB is itself uncertain at the 1 %
level *systematically*, and the same 1 % applies to the whole mantle path, not just
to D''. Every thickness in this lesson is a time divided by a velocity, and the
dividing is where the assumptions enter.

## 6. Assumptions and regime of validity

1. **Normal incidence.** The reflection coefficients above are normal-incidence
   values. At the ray parameters actually used in ScS studies (a few degrees from
   vertical at the CMB) the coefficients change, and mode conversions (S-to-P at the
   boundary) appear. These are small corrections to the *polarity* conclusion for
   S, but not to the amplitude of the ULVZ reflections.
2. **One-dimensional, laterally uniform layers.** A ULVZ with lateral extent
   comparable to the Fresnel zone cannot be treated as a plane layer; a
   finite-width body acts partly as a diffractor.
3. **Acoustic (fluid-like) response.** The input-impedance recursion above is for
   an acoustic/SH medium; it ignores conversions and the S-to-P coupling at the
   CMB, which is real and measured.
4. **A layered D''.** A gradational transition (see
   [lesson 03](03-upper-mantle-discontinuities.md)) filters the reflection exactly
   as a transition zone does: a D'' discontinuity wider than a period is invisible
   at that frequency.
5. **Known Clapeyron slope.** The shut-off temperature scales as $C/\gamma$: with
   $\gamma$ uncertain by 30 %, the threshold temperature is uncertain by 30 % —
   hundreds of kelvin at these values.
6. **No chemical boundary.** The D'' discontinuity may be partly compositional, not
   purely a phase transition; the temperature interpretation then inherits a second
   unknown.
7. **Hydrostatic pressure.** Dynamic pressure from mantle flow displaces boundaries
   at these depths by kilometres, the same order as the thermal signal.

## 7. Worked examples

### Example 1 — the delay of a ULVZ and its partner

A ULVZ 15 km thick has $v_s' = 6.20\ \mathrm{km\,s^{-1}}$ where the mantle value is
$7.26$. Then

$$\delta t = 2 \times 15 \times \left(\frac{1}{6.20} - \frac{1}{7.26}\right)
= 30 \times (0.161290 - 0.137741) = 30 \times 0.023549 = 0.706\ \mathrm{s}.$$

The implied $\delta = 1 - 6.20/7.26 = 0.146$, i.e. a 14.6 % reduction. If the layer
were instead 30 km thick, the velocity reduction needed for the *same* 0.706 s is
found by solving $0.706 = 60(1/v_s' - 0.137741)$:

$$1/v_s' = 0.137741 + 0.011767 = 0.149508
\;\Rightarrow\;
v_s' = 6.689\ \mathrm{km\,s^{-1}},$$

a 7.9 % reduction. **Halving the thickness halves the required velocity drop** —
the degeneracy in one line.

### Example 2 — is the reflection actually all-pass?

For a lossless stack with $|R|=1$ at every frequency, Parseval's theorem requires
$\sum |r(t)|^2 = \sum |s(t)|^2$ exactly. The demonstration's energy column is
1.000 for all four models, which confirms two things at once: the input-impedance
recursion has no sign or normalisation error, and the medium modelled has no
attenuation. If a computed energy ratio were 1.3, the bug would be in the
recursion, not in the Earth.

### Example 3 — the shut-off temperature and its sensitivity

With $C = 10.0\ \mathrm{GPa}$ and $\gamma = 8\ \mathrm{MPa\,K^{-1}}$, D'' switches
off at $T_\text{ref} + 1250\ \mathrm{K} = 3750\ \mathrm{K}$. If the true $\gamma$
were 6 instead of 8 (a 25 % change, well inside experimental uncertainty), the
threshold moves to

$$2500 + \frac{10\,000}{6} = 2500 + 1667 = 4167\ \mathrm{K},$$

a change of 417 K. Conversely, with $\gamma = 10$ the threshold drops to 3500 K. So
**the same seismic observation ("no D'' discontinuity here") maps to CMB
temperatures that differ by 700 K depending on a mineral-physics parameter whose
uncertainty is real.** This is the sharpest illustration in the module of why
seismic structure and mineral physics have to be interpreted jointly.

## 8. Python demonstration

`code/core_mantle_boundary_demo.py` computes: the CMB impedance contrasts; the ULVZ
delay and the $(h,\delta)$ family behind one delay; the exact normal-incidence
stack response via the input-impedance recursion, with a synthetic pulse at two
frequencies and the energy-conservation check; the post-perovskite D'' thickness as
a function of CMB temperature for three Clapeyron slopes, including the shut-off;
and the time-to-thickness conversion with its velocity ambiguity. It prints
labelled results with units and runs in about 0.1 s:

```bash
cd 12-global-geophysics-interior/01-seismic-structure-of-the-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_mantle_boundary_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/05-core-mantle-boundary-exercises.md`](exercises/05-core-mantle-boundary-exercises.md)
and
[`exercises/05-core-mantle-boundary-solutions.md`](exercises/05-core-mantle-boundary-solutions.md).

- **★** Compute $R$ at the CMB for a modified outer-core density.
- **★★** Build the $(h,\delta)$ family for a given delay and choose the physically
  admissible part.
- **★★** Compute the D'' thickness for a given CMB temperature and Clapeyron slope.
- **★★★** Design a measurement that would break the ULVZ $(h,\delta)$ degeneracy,
  with a predicted resolution.

## Mastery checkpoint

Without notes:

> A region shows an ScS postcursor delay of $1.8\ \mathrm{s}$ and a D''
> discontinuity at 210 km above the CMB. The reference mantle values are
> $v_s = 7.26$, $\rho = 5.57$; the outer core has $\rho = 9.90$.
> **(a)** Compute the ULVZ thickness for $\delta = 12\ \%$, and the $\delta$
> required if the layer were 25 km thick.
> **(b)** Compute the D'' thickness implied if the CMB temperature were 300 K
> warmer, for $\gamma = 8\ \mathrm{MPa\,K^{-1}}$ and $\rho g = 59.38\
> \mathrm{MPa\,km^{-1}}$.
> **(c)** State two reasons the 210 km value could be an overestimate of the true
> D'' thickness.
> **(d)** Which of the quantities in (a) is directly measured and which is
> inferred?

A worked version appears in the lesson-05
[solutions](exercises/05-core-mantle-boundary-solutions.md).

## Common pitfalls

1. **Quoting a ULVZ thickness without the velocity drop.** They are degenerate by
   construction (Section 2.1).
2. **Assuming the waveform resolves what the delay cannot.** In the demonstration's
   model it does not, because the impedance contrast is only a few per cent.
3. **Forgetting that a fluid has no S impedance.** The $R = -1$ result is exact and
   is the reason the deep S phases exist at all.
4. **Treating D'' as a fixed-thickness layer.** Its thickness is a function of
   temperature, and it can be absent.
5. **Ignoring the Clapeyron-slope uncertainty.** The shut-off temperature scales as
   $1/\gamma$, and a 25 % error in $\gamma$ moves it by more than 400 K.
6. **Reporting a thickness without the dividing velocity.** Section 5: a 3 %
   velocity error is a 3 % thickness error, and reference velocities are uncertain
   at the 1 % level systematically.
7. **Reading a polarity-reversed reflection as a new phase.** Because $R = -1$ at
   the CMB, every core-reflected S arrival is inverted relative to what a
   surface-reflection intuition would predict.

## Related modules

- [01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the reference values at the CMB.
- [03 Upper-Mantle Discontinuities at 410 and 660 km](03-upper-mantle-discontinuities.md) —
  the Clapeyron-slope and sharpness machinery reused here.
- [04 Lower-Mantle Heterogeneity and LLSVPs](04-lower-mantle-heterogeneity.md) —
  the resolution limits that apply to everything above the CMB.
- [06 Outer Core, Inner Core Anisotropy and Rotation](06-outer-and-inner-core.md) —
  the phases that travel through the core this boundary admits.
- [12-02-04 Core Composition, Light Elements and the Geodynamo](../02-composition-and-mineral-physics/04-core-composition.md) —
  what the core side of the boundary is made of.
- [12-03-03 Thermal Evolution of the Earth and Secular Cooling](../03-geotherms-and-heat-budget/03-thermal-evolution.md) —
  what a CMB temperature of 3500–4200 K implies for the Earth's history.

## Self-assessment checklist

- [ ] I can compute impedance contrasts and explain $R = -1$ for S at the CMB.
- [ ] I can derive the postcursor delay and construct the $(h,\delta)$ family.
- [ ] I can implement and validate the input-impedance recursion.
- [ ] I can state the two conditions under which a waveform resolves a layer.
- [ ] I can derive the D'' shut-off temperature from $C$ and $\gamma$.
- [ ] I can convert a delay to a thickness and state the velocity assumption.
- [ ] I can say which of my quoted numbers is measured and which is inferred.
