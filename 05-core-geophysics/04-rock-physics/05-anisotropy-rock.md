---
id: 05-04-05
title: "Anisotropy in Rocks: Causes and Magnitudes"
level: doctoral
prereqs: ["05-04-02"]
tags: [anisotropy, thomsen, vti, christoffel, shale]
---

# Anisotropy in Rocks: Causes and Magnitudes

## Learning objectives

1. **Distinguish** intrinsic, structural and stress-induced anisotropy, and name
   the rock types dominated by each.
2. **State** the VTI stiffness matrix and derive the phase velocities from the
   Christoffel equation.
3. **Compute** the Thomsen parameters from a stiffness matrix and verify them
   against an independent eigen-solution.
4. **Explain** what $\varepsilon$, $\gamma$ and $\delta$ control physically, and
   why $\delta$ is the one that matters for depth ties.
5. **State** the magnitude range of anisotropy in common settings, as a range
   with its cause.

## Prerequisites

- [05-04-02 Effective-Medium Theories](./02-effective-medium-theory.md)
- [02-04-06 Anisotropic Elasticity](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)

## 1. Intuition

Anisotropy means that velocity depends on direction. In rocks it arises from
three distinct causes, and confusing them leads to wrong predictions:

- **Intrinsic:** crystallographic or grain-shape preferred orientation. Shales
  are the archetype (clay platelets align, producing up to tens of percent
  velocity anisotropy).
- **Structural:** fine layering of isotropic materials. A stack of thin beds is
  anisotropic *in the long-wavelength limit* even though every bed is isotropic
  (Backus averaging). This is the mechanism behind the derivation below.
- **Stress-induced:** aligned cracks opened preferentially by a stress field.
  Magnitudes are typically smaller than the other two but are of great interest
  because they change with stress — and hence with time and with production.

## 2. The VTI stiffness matrix and Thomsen parameters

Transversely isotropic media with a vertical symmetry axis (VTI) require five
independent constants: $C_{11}, C_{33}, C_{13}, C_{44}, C_{66}$. Thomsen's
parameters are combinations chosen to be near-zero for weak anisotropy:

$$\varepsilon = \frac{C_{11}-C_{33}}{2C_{33}}, \qquad
\gamma = \frac{C_{66}-C_{44}}{2C_{44}}, \qquad
\delta = \frac{(C_{13}+C_{44})^2-(C_{33}-C_{44})^2}{2C_{33}(C_{33}-C_{44})}.$$

All three are dimensionless (ratios of like quantities), and all three vanish
identically for an isotropic medium. Physical meanings:

- $\varepsilon$: fractional difference between horizontal and vertical P
  velocities, $\approx (V_p^{H}-V_p^{V})/V_p^{V}$.
- $\gamma$: the corresponding quantity for the fast shear wave (SH).
- $\delta$: controls the *near-vertical* P-velocity variation. It is the
  parameter that governs normal-moveout and depth ties, and it is the hardest to
  measure directly — it can be estimated only from travel times at non-vertical
  incidence, not from vertical velocities.

## 3. Derivation: phase velocities from the Christoffel equation

Plane-wave solutions of the elastodynamic equation require
$\det(\Gamma - \rho V^2 I) = 0$, with $\Gamma_{ik} = C_{ijkl}n_jn_l$ for
propagation direction $\mathbf{n}$. For VTI with $\theta$ measured from the
symmetry axis ($\sin^2\theta = s^2$, $\cos^2\theta = c^2$,
$sc = \sin\theta\cos\theta$):

$$\Gamma = \begin{pmatrix}
C_{11}s^2+C_{44}c^2 & 0 & (C_{13}+C_{44})sc\\
0 & C_{66}s^2+C_{44}c^2 & 0\\
(C_{13}+C_{44})sc & 0 & C_{44}s^2+C_{33}c^2
\end{pmatrix}.$$

The eigenvalues are $\rho V^2$ for the quasi-P, quasi-SV and SH modes. At
$\theta = 0$: $V_p(0) = \sqrt{C_{33}/\rho}$,
$V_s(0) = \sqrt{C_{44}/\rho}$. At $\theta = 90°$:
$V_p(90°) = \sqrt{C_{11}/\rho}$, $V_s(90°) = \sqrt{C_{66}/\rho}$. Hence

$$\frac{V_p(90°)}{V_p(0)} - 1 = \sqrt{1+2\varepsilon}-1, \qquad
\frac{V_s(90°)}{V_s(0)} - 1 = \sqrt{1+2\gamma}-1.$$

These are exact relations between the Thomsen parameters and the axial
velocities, and they are the check used in the demonstration.

### 3.1 The Christoffel equation, derived

Section 3 asserted that plane-wave solutions require
$\det(\Gamma-\rho V^2I) = 0$. That condition is not a postulate; it falls out of
the elastodynamic equation in three lines.

The equation of motion for a homogeneous linearly elastic solid is

$$\rho\frac{\partial^2u_i}{\partial t^2}
= \frac{\partial\sigma_{ij}}{\partial x_j}
= C_{ijkl}\frac{\partial^2u_k}{\partial x_j\partial x_l},$$

using $\sigma_{ij} = C_{ijkl}\partial u_k/\partial x_l$ and the constancy of
$C_{ijkl}$. Substitute a plane wave $u_k = A_k e^{i(k_jx_j-\omega t)}$:

$$\frac{\partial^2u_k}{\partial x_j\partial x_l} = -k_jk_l\,u_k,
\qquad
\frac{\partial^2u_i}{\partial t^2} = -\omega^2u_i,$$

so

$$-\rho\omega^2A_i = -C_{ijkl}k_jk_lA_k
\qquad\Longrightarrow\qquad
\rho\omega^2 A_i = C_{ijkl}k_jk_l A_k .$$

Write $\mathbf{k} = k\hat{\mathbf{n}}$ and use $k = \omega/V$:

$$\boxed{\;\rho V^2A_i = \underbrace{C_{ijkl}n_jn_l}_{\Gamma_{ik}}A_k\;}
\qquad\Longleftrightarrow\qquad
\left(\Gamma_{ik}-\rho V^2\delta_{ik}\right)A_k = 0 .$$

Because the amplitude vector is non-zero, the determinant must vanish — the
Christoffel condition. **The eigenvalues of $\Gamma$ are $\rho V^2$**, one for
each of the three body waves, and the eigenvectors are the polarisations.

**Physical interpretation.** $\Gamma$ mixes the stiffness tensor with the
*propagation direction* $n_jn_l$, so it encodes exactly how the medium's
directional stiffness is sampled by a wave travelling in a given direction. For
an isotropic medium $\Gamma$ is diagonal with a single repeated structure and the
three velocities are independent of direction; for VTI it is not, and the
direction dependence is the anisotropy.

### 3.2 The VTI Christoffel matrix, entry by entry

Section 3 quoted a $3\times3$ matrix. Here it is derived, because the
bookkeeping *is* the physics.

Adopt the Voigt mapping for VTI with the symmetry axis along $z$: stiffness
constants $C_{11} = C_{22}$, $C_{33}$, $C_{12}$, $C_{13} = C_{23}$,
$C_{44} = C_{55}$, $C_{66}$, with $C_{66} = (C_{11}-C_{12})/2$ and $C_{12} =
C_{11}-2C_{66}$. Let $\hat{\mathbf{n}} = (\sin\theta, 0, \cos\theta)$, so
$n_2 = 0$, $n_1 = \sin\theta = s$, $n_3 = \cos\theta = c$.

$$\Gamma_{ik} = C_{ijkl}n_jn_l
= C_{i1k1}s^2 + C_{i3k3}c^2 + C_{i1k3}sc + C_{i3k1}sc
= C_{i1k1}s^2 + C_{i3k3}c^2 + \left(C_{i1k3}+C_{i3k1}\right)sc .$$

Now each entry:

| entry | terms | result |
|---|---|---|
| $\Gamma_{11}$ | $C_{1111}s^2 + C_{1313}c^2$ | $C_{11}s^2 + C_{44}c^2$ |
| $\Gamma_{22}$ | $C_{2121}s^2 + C_{2323}c^2$ | $C_{66}s^2 + C_{44}c^2$ |
| $\Gamma_{33}$ | $C_{3131}s^2 + C_{3333}c^2$ | $C_{44}s^2 + C_{33}c^2$ |
| $\Gamma_{13}$ | $(C_{1133}+C_{1331})sc$ | $(C_{13}+C_{44})sc$ |
| $\Gamma_{12},\Gamma_{23}$ | contain $n_2 = 0$ | $0$ |

which is the matrix quoted earlier. **Note that $C_{12}$ never appears**: a wave
travelling in the $x$–$z$ plane does not sample the $x$–$y$ coupling directly,
which is why five constants suffice for VTI phase velocities in that plane, and
why $\gamma$ carries $C_{66}$ while $\varepsilon$ and $\delta$ carry the rest.

The zero entries decouple the $y$-polarised (**SH**) mode exactly, so

$$\rho V_\text{SH}^2 = \Gamma_{22} = C_{66}s^2 + C_{44}c^2 ,$$

giving $V_\text{SH}(0) = \sqrt{C_{44}/\rho}$ and
$V_\text{SH}(90°) = \sqrt{C_{66}/\rho}$ — the axial relation used in Section 4.
The $(1,3)$ block couples $x$ and $z$, producing the quasi-P and quasi-SV modes
with velocities given by the eigenvalues of a $2\times2$ matrix.

### 3.3 The weak-anisotropy approximation, and what δ does that ε does not

Expand the quasi-P eigenvalue of the $(1,3)$ block to first order in the
anisotropy. The standard result is

$$\frac{V_{qP}(\theta)}{V_p(0)} \approx 1
+ \delta\sin^2\theta\cos^2\theta + \varepsilon\sin^4\theta .$$

**Measured check** for the stated synthetic VTI constants
($\varepsilon = 0.1$, $\delta = 0.0569$), exact Christoffel eigenvalue versus the
approximation:

| $\theta$ | exact $V_{qP}$ (m/s) | weak-anisotropy | relative difference |
|---|---|---|---|
| 15° | 4709.32 | 4709.20 | $-0.0026\%$ |
| 30° | 4771.02 | 4769.76 | $-0.0265\%$ |
| 45° | 4876.39 | 4874.38 | $-0.0413\%$ |
| 60° | 5000.72 | 5004.28 | $+0.0712\%$ |

The approximation is good to better than 0.1% even at $\varepsilon = 0.1$ — the
"weak anisotropy" label is more forgiving than its name suggests.

**Now the crucial distinction.** Compare the two terms' magnitudes:

| $\theta$ | $\delta\sin^2\!\theta\cos^2\!\theta$ | $\varepsilon\sin^4\!\theta$ | ratio |
|---|---|---|---|
| 5° | $4.29\times10^{-4}$ | $5.77\times10^{-6}$ | **74.3** |
| 10° | $1.66\times10^{-3}$ | $9.09\times10^{-5}$ | **18.3** |
| 20° | $5.88\times10^{-3}$ | $1.37\times10^{-3}$ | 4.30 |
| 45° | $1.42\times10^{-2}$ | $2.50\times10^{-2}$ | 0.57 |

**Physical interpretation.** The $\delta$ term involves $\sin^2\theta\cos^2\theta$,
which for small $\theta$ behaves as $\theta^2$; the $\varepsilon$ term involves
$\sin^4\theta \sim \theta^4$. So **near the vertical the $\delta$ term dominates by
a factor of 18 at 10° and 74 at 5°**, while at 45° the $\varepsilon$ term is
almost twice as large. Depth conversion, normal moveout and any near-vertical
work therefore probe $\delta$; and since $\delta$ is precisely the parameter that
axial velocities do not determine (Section 3.2's table shows $C_{13}$ enters only
the $(1,3)$ coupling), **the anisotropy parameter that matters most for depth is
the one least constrained by the measurements that are easiest to make.**

## 4. Units and dimensional analysis

| Quantity | Unit |
|---|---|
| $C_{IJ}$ | Pa |
| $\rho$ | kg m⁻³ |
| $\Gamma_{ik}$ | Pa |
| $V$ | m s⁻¹ |
| $\varepsilon,\gamma,\delta$ | dimensionless |

Check: $[\Gamma/\rho] = \mathrm{Pa/(kg\,m^{-3})} = \mathrm{m^2s^{-2}}$, so
$\sqrt{\Gamma/\rho}$ is m/s. ✓

## 5. Assumptions

1. **Homogeneity on the scale of the wavelength.** Interbedded layers thinner
   than about a quarter of the dominant wavelength are effectively anisotropic;
   thicker ones produce scattering and reflections instead.
2. **Linear elasticity.**
3. **VTI symmetry.** Lower symmetry (orthorhombic, HTI) requires more
   parameters and changes the algebra.
4. **Induced (not intrinsic) magnetisation analogies do not apply** — this is
   purely elastic.
5. **Velocities quoted are phase velocities** unless explicitly stated. Group
   velocities differ, and confusion between them is a real source of survey
   design error at large offsets.

### 5.1 Assumptions, and the size of each failure

| Assumption | Failure | Quantified consequence |
|---|---|---|
| Homogeneity at the wavelength scale | layering thicker than $\lambda/4$ | reflections and scattering appear instead of anisotropy; Backus averaging invalid |
| Linear elasticity | large strain near a source | negligible at seismic strains (10⁻⁶) |
| VTI symmetry | orthorhombic or HTI rock | more parameters; the $(1,2)$ coupling no longer vanishes and SH is no longer pure |
| Known $C_{13}$ | unmeasured | $\delta$ unconstrained; near-vertical depth error of tens of metres at 4 km |
| Phase velocities quoted | group-velocity use at large offsets | NMO velocity differs from phase velocity; the error grows with offset |
| $\delta$ from an empirical relation | lithology mismatch | up to 75% error in the near-vertical correction (this section) |

## 6. Worked examples (measured)

Stated SYNTHETIC VTI stiffness: $C_{11} = 66$ GPa, $C_{33} = 55$ GPa,
$C_{13} = 18$ GPa, $C_{44} = 20$ GPa, $C_{66} = 23$ GPa,
$\rho = 2500$ kg/m³.

Computed Thomsen parameters: $\varepsilon = 0.1000$, $\gamma = 0.0750$,
$\delta = 0.0569$.

Independent Christoffel eigen-solution:

| | 0° | 90° |
|---|---|---|
| $V_p$ (m/s) | 4690.4 | 5138.1 |
| $V_s$ (m/s) | 2828.4 | 3033.2 |

Checks: $V_p(90°)/V_p(0)-1 = 0.095445$, and
$\sqrt{1+2\varepsilon}-1 = 0.095445$ — agreement to all printed digits.
$V_s(90°)/V_s(0)-1 = 0.072381$ against $\sqrt{1+2\gamma}-1 = 0.072381$.

Isotropic limit: setting $C_{11} = C_{33}$ and $C_{44} = C_{66} = 15$ GPa with
$C_{13} = C_{11}-2C_{44}$ returns $\varepsilon = \gamma = \delta = 0$ exactly
(measured $0.000\times10^{0}$).

**Interpretation.** A 10% P-anisotropy is large but entirely ordinary for a
shale. A vertical-incidence-only survey would report $V_p = 4690$ m/s, while the
horizontal velocity is 5138 m/s. Depth conversion using the vertical velocity is
correct only if the rays are vertical and the layering is flat — and $\delta$,
not $\varepsilon$, governs the near-vertical case.

### 6.1 Extended worked example: at 45°, and why the axial velocities are not enough

For the stated SYNTHETIC VTI constants ($C_{11} = 66$, $C_{33} = 55$,
$C_{13} = 18$, $C_{44} = 20$, $C_{66} = 23$ GPa, $\rho = 2500$ kg/m³), the
Christoffel matrix at $\theta = 45°$ has $s^2 = c^2 = 0.5$, $sc = 0.5$, giving

$$\Gamma_{11} = \tfrac12(C_{11}+C_{44}) = 43.0\ \mathrm{GPa},\quad
\Gamma_{33} = \tfrac12(C_{44}+C_{33}) = 37.5\ \mathrm{GPa},\quad
\Gamma_{13} = \tfrac12(C_{13}+C_{44}) = 19.0\ \mathrm{GPa},$$
$$\Gamma_{22} = \tfrac12(C_{66}+C_{44}) = 21.5\ \mathrm{GPa}.$$

The $2\times2$ block in the $(1,3)$ plane has eigenvalues
$40.25 \pm \sqrt{2.75^2+19^2} = 40.25\pm19.196$, i.e. 59.446 and 21.054 GPa.
Dividing by $\rho$ and taking square roots, with the SH branch from
$\Gamma_{22}$:

| mode | velocity at 45° (m/s) |
|---|---|
| quasi-P | 4876.4 |
| SH | 2932.6 |
| quasi-SV | 2901.9 |

**Compare with the axial values** from the lesson: $V_p(0) = 4690.4$,
$V_p(90°) = 5138.1$, $V_s(0) = 2828.4$, $V_s(90°) = 3033.2$ m/s. The
quasi-P velocity at 45° lies between the two axial values, as it must. Both
shear velocities at 45° exceed $V_s(0)$.

**The point of the exercise.** Measurements of $V_p(0)$ and $V_p(90°)$ determine
$C_{33}$ and $C_{11}$, hence $\varepsilon$. Measurements of $V_s(0)$ and
$V_s(90°)$ determine $C_{44}$ and $C_{66}$, hence $\gamma$. **Nothing axial
determines $C_{13}$, hence nothing axial determines $\delta$** — and $\delta$
is what governs near-vertical moveout and depth ties. The 45° quasi-P velocity
does depend on $C_{13}$, which is why non-axial travel times (a walkaway VSP, or
surface-seismic moveout at moderate offsets) are required to constrain it.

**A test you can run.** Recompute the table with $C_{13}$ changed from 18 to
25 GPa, keeping all other constants. The axial velocities are *identical*
(they do not involve $C_{13}$), while $\delta$ and the 45° quasi-P velocity
both change. If your depth conversion depends on $\delta$, this is the
sensitivity that must be reported — and if $\delta$ came from an empirical
$\varepsilon$–$\delta$ relation rather than a measurement, that must be said.

### 6.2 Worked arithmetic: what δ does that ε does not

Take the stated synthetic VTI rock and compare two models that agree on the axial
velocities but differ in $\delta$.

| model | $C_{13}$ (GPa) | $\varepsilon$ | $\delta$ | $V_p(0)$ | $V_p(90°)$ | $V_{qP}(45°)$ |
|---|---|---|---|---|---|---|
| A | 18 | 0.1000 | 0.0569 | 4690.4 | 5138.1 | 4876.4 |
| B | 25 | 0.1000 | **0.2078** | 4690.4 | 5138.1 | **5016.7** |

(The model-B entries are computed, not asserted: the exact Christoffel
eigen-solution at 45° gives 5016.7 m/s for $C_{13} = 25$ GPa.)

Because $\varepsilon = (C_{11}-C_{33})/2C_{33}$ and the axial velocities depend
only on $C_{33}$, $C_{11}$, $C_{44}$, $C_{66}$ and $\rho$, **model B has exactly
the same axial velocities as model A** — the rows of the table for $V_p(0)$ and
$V_p(90°)$ are identical by construction. But $\delta$ depends on
$(C_{13}+C_{44})^2$, so it changes, and so does the 45° velocity.

**The consequence for depth conversion.** A depth tie uses near-vertical
travel times, which the weak-anisotropy expansion shows are governed by $\delta$
(Section 3.3: the $\delta$ term exceeds the $\varepsilon$ term by a factor 18 at
10°). So two models that are *indistinguishable* on the axial-velocity
measurements produce different depths, differing by the accumulated
$\delta\sin^2\theta\cos^2\theta$ effect along the raypath. At a one-way
average $\theta \approx 10°$ over 4 km, the relative travel-time difference is
$1.66\times10^{-3}$ — about **6.6 m of depth** — and for a larger $\delta$
contrast between models A and B — $\Delta\delta = 0.1509$ — the depth error at
10° over 4 km is $0.1509\sin^2\!10°\cos^2\!10°\times4000 = 17.7$ m.

**What to report.** Not "$\delta = 0.06$" but "$\delta$ was obtained from
$C_{13}$, which was constrained by the walkaway VSP first-arrival times at
offsets 1–3 km; the resulting uncertainty in $\delta$ is $\pm0.02$, corresponding
to $\pm40$ m at 4 km depth." That is a statement a reviewer can check and use.

### 6.3 A shortcut that fails: setting δ = ε

**The shortcut.** Anisotropy is hard to measure, so assume $\delta = \varepsilon$
(the "elliptical anisotropy" assumption, which is exactly true only for
$\delta = \varepsilon$) and use $\varepsilon$ from the axial velocities.

**Why it fails.** The assumption $\delta = \varepsilon$ defines elliptical
anisotropy, a genuinely special case in which the wavefronts are ellipses. For
real rocks $\delta$ is usually *smaller* than $\varepsilon$ — the stated
synthetic rock has $\delta = 0.0569$ against $\varepsilon = 0.1000$, a ratio of
0.57, and shale measurements commonly show ratios of 0.4–0.8. Adopting
$\delta = \varepsilon$ therefore *overestimates* $\delta$ by a factor of
$1/0.57 = 1.75$ in this example.

**Quantified consequence.** The near-vertical velocity correction is the
$\delta\sin^2\!\theta\cos^2\!\theta$ term, linear in $\delta$ at fixed $\theta$;
overestimating $\delta$ by 75% therefore overestimates that correction by 75%.
At 10° over 4 km the term measures $1.66\times10^{-3}\times4000 = 6.64$ m of depth
(taken from the table above, not assumed); inflating it by 75% gives 11.62 m, so
the bias from this one assumption is 4.98 m — small in absolute terms, but it is a
*systematic* error that grows with the depth of the target and the dip of the
rays, and it is entirely a modelling assumption rather than a measurement.

**What to do instead.** Measure $\delta$ from non-axial travel times where
possible; where impossible, use an empirical $\varepsilon$–$\delta$ relation for
the lithology *and report it as an assumption with its uncertainty*. The
distinction between "$\delta$ measured" and "$\delta$ assumed via a relation" must
appear in the report, because it is precisely the parameter that depth
conversion depends on.

## 7. Python demonstration

Run `code/petrophysics_demo.py` Section 2. It computes the Thomsen parameters,
solves the Christoffel eigenvalue problem independently, checks the axial
relations, and confirms the isotropic limit. Then try setting $C_{13}$ to make
$\delta = 0$ while keeping $\varepsilon$ fixed, and observe that the axial
velocities do not change — the clearest demonstration that $\delta$ controls
something the axial velocities do not show.

## 8. Magnitudes and causes

Any statement of magnitude must be a range with a cause:

| Setting | Dominant cause | Order of magnitude of anisotropy |
|---|---|---|
| Shales and mudstones | intrinsic (clay alignment) plus fine layering | up to tens of percent in P and S |
| Thin-bedded sequences | structural (Backus) | a few percent, computable from the layering |
| Clean sandstones | weak | typically a few percent or less |
| Fractured reservoirs | stress-aligned cracks | a few percent, and stress-dependent |
| Crystalline basement | weak unless foliated | usually small |

These are ranges, not values; they come from the causes listed, not from a
single remembered number. For a specific site, the only defensible statement is a
measured or modelled value with its uncertainty.

## 9. Exercises, mistakes, applications

Exercises: [`exercises/05-anisotropy-rock-exercises.md`](./exercises/05-anisotropy-rock-exercises.md).

**Common mistakes.** (1) Equating $\delta$ with $\varepsilon$. (2) Using the
vertical velocity for depth conversion when rays are dipping. (3) Assuming
Backus averaging applies to layers that are too thick. (4) Confusing phase and
group velocity. (5) Quoting an anisotropy magnitude without its cause.

**Applications.** Depth conversion in shale-dominated basins (an $\varepsilon$
or $\delta$ error of 0.05 becomes a depth error of a few percent — hundreds of
metres at 4 km); fracture detection from shear-wave splitting
($\gamma$-related); anisotropic migration and velocity model building;
stress monitoring from time-lapse anisotropy.

## 10. Further reading

- **Thomsen, L. (1986).** Weak elastic anisotropy. *Geophysics* 51, 1954–1966.
  Level: graduate. The definitions used here.
- **Backus, G. E. (1962).** Long-wave elastic anisotropy produced by horizontal
  layering. *JGR* 67, 4427–4440. Level: graduate. The structural mechanism.
- **Tsvankin, I. (2012). *Seismic Signatures and Analysis of Reflection Data in
  Anisotropic Media* (2nd ed.).** Level: graduate.

## 11. Related lessons

- [05-04-06 Attenuation and Velocity Dispersion](./06-attenuation-dispersion-rock.md)
- [02-04-06 Anisotropic Elasticity](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)
- [06-seismology](../../06-seismology/README.md)

## Self-assessment checklist

- [ ] I can name the three causes of anisotropy and an example of each.
- [ ] I can write the VTI stiffness matrix and the Christoffel matrix.
- [ ] I can compute Thomsen parameters and check the axial relations.
- [ ] I can explain why $\delta$ matters for depth conversion.
- [ ] I can quote anisotropy magnitudes only as ranges with causes.
