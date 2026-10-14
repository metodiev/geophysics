---
id: 04-04-01
title: "Stress, Strain and Brittle vs Ductile Deformation"
level: advanced
prereqs: ["04-02-03", "02-04-01", "02-04-02"]
estimated_minutes: 90
tags: [stress, strain, rheology, friction, creep, brittle-ductile-transition]
---

# Stress, Strain and Brittle vs Ductile Deformation

The same rock, at the same pressure, deforms in two completely different ways
depending on temperature. Near the surface it fractures; at greater depth, at the
same differential stress, it flows. The boundary between those two behaviours is
not a property of the rock and not a depth: it is the depth at which two *strength
curves cross*, and each curve has its own physics, its own parameters and its own
regime of validity.

That crossing is the organising idea of this lesson, and it is why the lesson is
built as two halves that meet. The **brittle** half is friction: a rock fails when
the shear stress on a favourably oriented plane exceeds a coefficient times the
effective normal stress. The **ductile** half is creep: a rock flows at a strain
rate that depends on stress through a power law and on temperature through an
Arrhenius factor. Both halves are quantitative, both are calibrated against
laboratory experiments, and both are extrapolated to conditions no laboratory can
reproduce. Extrapolation is where the intellectual work is.

## Learning objectives

By the end of this lesson you will be able to:

1. **Represent** a stress state as a tensor, find its principal stresses as
   eigenvalues, and state which invariants do not depend on the frame.
2. **Compute** the effect of pore pressure on the effective stress state and
   explain why it, and not the total stress, controls failure.
3. **Use** the Mohr circle and locate the optimum failure plane by maximising the
   Coulomb function, then verify the result against $45^\circ + \phi/2$.
4. **Derive** the differential stress required to slide a critically oriented
   fault in the normal- and reverse-faulting regimes, and explain why one regime
   needs several times the stress of the other.
5. **Evaluate** a dislocation-creep flow law, recover its stress exponent
   numerically, and explain why the extrapolation to low temperature is outside
   the law's regime of validity.
6. **Locate** the brittle–ductile transition by finding where the two curves
   cross, and describe how it moves with geotherm, strain rate and flow-law
   parameters.
7. **Compute** the finite strain from a deformation gradient tensor, find the
   principal stretches, and demonstrate that simple shear is volume-preserving
   and non-coaxial.

## Prerequisites

- [02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  — the stress tensor, tractions and principal stresses, derived.
- [02-04-02 Strain: Infinitesimal Strain Tensor and Compatibility](../../02-physics/04-elasticity-and-continuum-mechanics/02-strain.md)
  — the strain tensor and its relation to displacement.
- [04-02-03 Mantle Convection, Slab Pull and Ridge Push](../02-plate-tectonics/03-driving-forces.md)
  — the stresses that drive the deformation this lesson describes.
- [01-15-03 Strain and Stress Tensors as Physical Tensors](../../01-mathematics/15-tensors-and-differential-geometry/03-strain-and-stress-tensors.md)
  — the tensor algebra in general form.

## 1. The stress state, and which parts of it matter

A stress tensor is symmetric and has three real eigenvalues: the **principal
stresses** $\sigma_1 \ge \sigma_2 \ge \sigma_3$, with the sign convention that
compression is positive (as is customary in rock mechanics; the geophysics
literature is divided on this, and stating your convention is part of writing
about stress). The eigenvalues are frame-independent, which is why a strength
criterion can be written in terms of them alone: the orientation of the plane
that fails is not known in advance, so the criterion cannot depend on the frame.

Two invariants do most of the work. The **mean stress**

$$p = \frac{\sigma_1 + \sigma_2 + \sigma_3}{3} \tag{1}$$

controls compaction and pore-pressure response, and the **differential stress**

$$\Delta\sigma = \sigma_1 - \sigma_3 \tag{2}$$

controls failure. For a lithostatic column with a tectonic increment, the demo
finds

```text
regime           S1 (MPa)   S2 (MPa)   S3 (MPa)      mean (MPa)   von Mises (MPa)
  normal            264.9      234.9      204.9             234.9             52.0
  strike-slip       294.9      264.9      234.9             264.9             52.0
  reverse           324.9      294.9      264.9             294.9             52.0
```

The mean and the von Mises invariant are identical in the three rows, because the
same three principal-magnitude stresses have simply been assigned to different
axes. **What differs between the three regimes is only which axis the largest
principal stress lies along**, and that is enough to decide whether the crust
faults normally, in strike-slip or in reverse.

A general stress matrix is handled the same way, by eigen-decomposition:

```text
  For a general stress matrix, the principal stresses are its eigenvalues:
    matrix eigenvalues  = 243.39, 265.06, 291.17 MPa
    invariants I1, I2  = 799.61, 212,553.05 MPa^2
    trace(eigenbasis)   = 799.61 MPa (same trace, as required)
```

The trace check is the verification: the trace is the sum of the eigenvalues and
is invariant, so computing it in the eigenbasis and finding the same number is a
check that the decomposition has been read correctly.

## 2. Pore pressure: the variable that decides whether a rock fails

A rock in the crust is porous, and the pore fluid carries part of the load. The
principle of effective stress states that deformation and failure are controlled
by the **effective stress**

$$\sigma' = \sigma - P_f \mathbf{I}, \tag{3}$$

with $P_f$ the pore-fluid pressure. In the crust, $P_f$ is often near
hydrostatic, which for a water column at the same depth is about 0.4 of the
lithostatic stress: the demo uses a pore-fluid factor of 0.38, giving

```text
  depth 10 km, rho = 2700 kg/m^3, pore-fluid factor 0.38
  vertical (lithostatic) stress  Sv = rho g z = 264.9 MPa
  pore pressure                  Pf = 0.38 Sv = 100.7 MPa
  vertical effective stress     Sv' = 164.2 MPa
```

The distinction is not a refinement. Overpressure — $P_f$ approaching or exceeding
the least principal stress — reduces $\sigma_n'$ towards zero and, from the
Coulomb criterion of §3, drives the required differential stress to failure
towards zero. **Overpressure is the mechanism by which a fault moves at a
differential stress far below the rock's dry strength**, and it is why a
pore-pressure estimate is part of every in-situ stress analysis
([13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](../../13-geodynamics-tectonics/04-tectonophysics-deformation/02-fault-mechanics.md)).

## 3. The Mohr circle and the optimum failure plane

On a plane whose normal makes an angle $\theta$ with the $\sigma_3$ axis, the
normal and shear tractions are

$$\sigma_n = \frac{\sigma_1 + \sigma_3}{2} + \frac{\sigma_1 - \sigma_3}{2}
\cos 2\theta, \qquad
\tau = \frac{\sigma_1 - \sigma_3}{2}\sin 2\theta, \tag{4}$$

which are the parametric equations of the Mohr circle: centre
$(\sigma_1+\sigma_3)/2$, radius $(\sigma_1-\sigma_3)/2$. For a stated state
($\sigma_1 = 120$ MPa, $\sigma_3 = 40$ MPa, $P_f = 20$ MPa):

```text
  centre of the circle  = 80.0 MPa
  radius of the circle  = 40.0 MPa  (this is the maximum shear stress)

 theta (deg)  2 theta (deg)  sigma_n (MPa)   tau (MPa)    f(MPa)
          45.0           90.0           80.0        40.0    -11.00
          54.0          108.0           67.6        38.0     -2.45
          60.0          120.0           60.0        34.6      0.64
          75.0          150.0           45.4        20.0     -1.56
```

The column $f$ is the Coulomb failure function

$$f = \tau - \mu(\sigma_n - P_f) - C, \tag{5}$$

with $\mu$ the coefficient of friction and $C$ the cohesion; failure occurs where
$f \ge 0$. It is **negative at $45^\circ$**, which is the angle of maximum shear,
and that is the first non-obvious result in rock mechanics: **the plane of maximum
shear stress is not the plane of failure.** When friction is present, the optimum
plane is rotated towards the compressional axis, because the failure criterion
penalises normal stress and rewards shear stress, and the maximum of a penalised
function is not the maximum of the reward.

Maximising $f$ numerically and comparing with the analytic result:

```text
  located maximum of the Coulomb function: theta = 65.1824 deg
  analytic 45 deg + phi/2 with phi = atan(mu) = 40.365 deg: theta = 65.1823 deg
  difference: 0.000122 deg (the grid spacing of the search, not a physical difference)
```

The angle is $\theta = 45^\circ + \phi/2$ with $\phi = \arctan\mu$ the **angle of
internal friction**. For $\mu = 0.85$ this is $65.18^\circ$, so the two conjugate
planes are at $\pm 65.18^\circ$ from the $\sigma_3$ axis, making an acute angle of
$2(90^\circ - 65.18^\circ) = 49.6^\circ$ with $\sigma_1$. **That prediction is
directly visible in the field**: conjugate fault sets form an X with the acute
bisector along $\sigma_1$, and the angle between the conjugate planes is a
measurement of $\phi$.

## 4. Frictional strength in each regime

On the optimum plane, $\tau = \mu\sigma_n' + C$, and solving for the differential
stress gives the closed form

$$\Delta\sigma = \frac{2\left(\mu\sigma_3' + C\right)}{\sqrt{1 + \mu^2} - \mu}.
\tag{6}$$

The demo checks equation (6) against a numerical search for the failure stress:

```text
   s3 eff (MPa)   closed form (MPa)    search (MPa)   difference
            50.0             183.807         183.807     1.14e-13
           200.0             735.230         735.230     4.55e-13
```

then applies the correct identification of $\sigma_3'$ in each regime. For
**normal faulting** the largest principal stress is vertical and
$\sigma_3' = S_v' - \Delta\sigma$, which on substitution into (6) gives
$\Delta\sigma = 2\mu S_v'/(\sqrt{1+\mu^2} + \mu)$. For **reverse faulting** the
least principal stress is vertical and $\sigma_3' = S_v'$, so equation (6) applies
directly. The resulting strengths:

```text
 depth (km)   Sv (MPa)   Sv' (MPa)   normal (MPa)  reverse (MPa)    ratio
         1       26.5        16.4           12.9           60.4    4.676
        10      264.9       164.2          129.1          603.7    4.676
        30      794.6       492.7          387.3        1,811.1    4.676
```

**The ratio is constant at 4.676.** It depends only on $\mu$, not on depth,
because both expressions are linear in $S_v'$. Byerlee's law therefore predicts
that reverse faulting requires roughly five times the differential stress that
normal faulting does at the same depth — a falsifiable prediction, and the reason
the deepest earthquakes are not normal-faulting ones.

The **strike-slip** case is deliberately absent from that table, and its absence is
the point. In strike-slip faulting the vertical axis is the *intermediate*
principal stress, so the least principal stress is horizontal and **the depth
says nothing about it**. A strength profile must state a regime; the same general
statement appeared in the slip-tendency calculation of
[04-04-02](./02-faults.md).

## 5. Creep, and the strength that falls with depth

At high temperature, rock deforms by dislocation creep, described by the flow law

$$\dot\varepsilon = A\,\sigma^n \exp\!\left(-\frac{Q}{RT}\right), \tag{7}$$

with $A$ a material constant, $n$ the stress exponent (typically 3 for
dislocation creep), $Q$ an activation energy and $R$ the gas constant. Inverting
equation (7) for stress gives the creep strength. Evaluated along a geotherm:

```text
 depth (km)   T (degC)  creep strength (MPa)  friction, reverse (MPa)      mode
          5        135             680,749.1                    301.8   brittle
         10        260               4,004.1                    603.7   brittle
         15        385                 165.7                    905.5   ductile
         20        510                  18.9                  1,207.4   ductile
         30        760                   1.2                  1,811.1   ductile
```

The number at 5 km deserves attention: 680 749 MPa is not a strength, it is a
warning. The flow law was calibrated on experiments near and above roughly
300 °C, and evaluating it at 135 °C is far outside its regime of validity. The
equation produces the number happily and the number means nothing. **A fitted law
has a domain, and a strength profile that does not say where its law stops being
trustworthy is a profile that is confident in the wrong places.**

The stress exponent is recoverable from the law itself, which is a check that the
exponent is implemented rather than assumed:

```text
  stress exponent recovered by fitting log(eps_dot) against log(sigma) at 700 K:
    fitted n = 3.00000000, input n = 3.00000000, difference 4.88e-15
```

## 6. The brittle–ductile transition

The two curves of §4 and §5 cross, and the crossing depth is the
**brittle–ductile transition (BDT)**. Finding it is a root-finding problem:
bisect on the depth at which the frictional and creep strengths are equal.

```text
  reference case (1e-15 s^-1, 25 degC/km, Q = 223 kJ/mol, reverse-faulting friction curve):
    brittle-ductile transition at 12.37 km
    friction strength there 746.9 MPa
    creep strength there    746.9 MPa
    residual -0.0000 MPa (the bisection tolerance)

what is changed                          BDT depth (km)   change (km)
  reference                                       12.37         +0.00
  geotherm 20 degC/km                             15.08         +2.71
  geotherm 30 degC/km                             10.52         -1.85
  strain rate 1e-16 s^-1                          11.35         -1.02
  strain rate 1e-14 s^-1                          13.49         +1.12
  Q = 200 kJ/mol                                  10.20         -2.17
  Q = 250 kJ/mol                                  14.92         +2.54
```

Read the signs, because they are the physics. A **hotter geotherm** shallows the
transition, because creep becomes fast at shallower depth. A **faster strain
rate** deepens it, because the rock must be stronger to reach the higher strain
rate — this is why the ductile strength falls with depth more slowly at a faster
rate. A **higher activation energy** deepens it, because the flow law is more
temperature-sensitive and only becomes weak enough deeper down. The residual at
the crossing is the bisection tolerance, and the two strengths agree to within it,
which is the check that a genuine crossing was found rather than a grid point.

The BDT depth is, to first order, the **thickness of the seismogenic layer**. The
same calculation is why continental earthquakes are concentrated in the upper
crust rather than distributed through the whole lithosphere.

The table has one conspicuous absence, and it is worth naming: **no dependence on
rock type**. That is a consequence of a model with a single creep law. A layered
crust with a quartz-bearing layer over a feldspar-bearing one has two crossovers
and can have two seismogenic layers separated by a ductile zone, and that
structure is observed. Building it means running the calculation twice with two
flow laws and taking the minimum at each depth.

## 7. Strain: the deformation gradient and the finite strain ellipse

Stress is what drives deformation; strain is what the rock records. For a
homogeneous deformation the mapping is a matrix: $x_i = F_{ij}X_j$, and for plane
simple shear

$$F = \begin{pmatrix} 1 & \gamma \\ 0 & 1\end{pmatrix}. \tag{8}$$

The finite strain ellipse is obtained from the eigenvalues of $FF^{\mathsf T}$,
whose square roots are the principal stretches. The demo's results:

```text
 gamma   stretch max   stretch min     area  marker rotation (deg)   analytic
  0.25      1.132782      0.882782    1.000                14.0362    14.0362
  1.00      1.618034      0.618034    1.000                45.0000    45.0000
  4.00      4.236068      0.236068    1.000                75.9638    75.9638
```

Three checks are visible. The **area is exactly 1** at every $\gamma$, because
$\det F = 1$ and plane strain must be volume-preserving. The **rotation of a
marker line** originally perpendicular to the shear plane is exactly
$\arctan\gamma$; a coaxial deformation would produce zero rotation, so any
measured rotation of a marker is direct evidence of a non-coaxial path. And for
$\gamma = 1$ the stretches are $1.618\,034$ and $0.618\,034$, which are the
golden ratio and its reciprocal — the exact value is

$$\lambda_{1,2} = \sqrt{\frac{3 \pm \sqrt5}{2}} = 1.618034^\ldots, \; 0.618034^\ldots,
\tag{9}$$

so the agreement between the eigen-decomposition and the closed form is a check
that the eigenvalues are being read in the right order:

```text
    squared stretches = 2.618034, 0.381966
    expected squared stretches (3 +/- sqrt5)/2 = 2.618034, 0.381966
```

The warning that goes with this: **the axes of the finite strain ellipse bear no
fixed relation to the axes of the infinitesimal strain**. In simple shear the
infinitesimal principal axes are fixed at $45^\circ$ while the finite ellipse
rotates through it, so a strain measurement and an instantaneous-strain
calculation describe different things. Confusing the two is one of the standard
errors in reading a shear zone.

## 8. Assumptions and regime of validity

- **Byerlee's law is empirical.** The coefficient of friction near 0.85 and the
  near-independence of friction from rock type and from normal stress are
  laboratory observations over a limited range of conditions. Clays, serpentinite
  and some evaporites have substantially lower friction, and the transition to
  low friction at high slip velocity and large slip is a research area in its own
  right.
- **Cohesion is neglected here.** For intact rock, and for the first failure of a
  rock mass, cohesion is significant; for the reactivation of existing faults it
  is usually small, which is what makes the reactivation calculation in §4
  defensible for faults and not for intact rock.
- **The flow law is calibrated at high temperature and high strain rate.**
  Extrapolating it to lower temperature or to geological strain rates spans orders
  of magnitude in time, and the resulting strength is a model output, not a
  measurement.
- **A single creep mechanism is assumed.** At low stress and small grain size,
  diffusion creep may dominate, with a different stress exponent and a
  grain-size dependence.
- **The geotherm is assumed steady and conductive.** In an actively extending or
  shortening region it is neither, and the transition depth moves.
- **Pore pressure is assumed to be a fixed fraction of the lithostatic stress.**
  Real pore-pressure profiles are transient, and overpressure is the single
  largest control on frictional strength.
- **Local isostasy and a constant density** are assumed in converting depth to
  stress. Flexure and density stratification make this approximate.

## 9. Python demonstration

[`code/01-stress_strain_demo.py`](./code/01-stress_strain_demo.py) computes the
stress tensors and invariants, the Mohr circle and the located failure angle, the
frictional strength in each regime with its closed-form check, the creep strength
and its recovered stress exponent, the brittle–ductile transition and its
sensitivity, and the finite strain ellipse. Its output is quoted in §1, §3, §4,
§5, §6 and §7.

The two verifications to run yourself are the located failure angle against
$45^\circ + \phi/2$, and the eigen-decomposition against equation (9). Both are
checks in which the code and the analytic result were derived independently.

```bash
cd 04-earth-science-geology/04-structural-geology/code
.venv/bin/python 01-stress_strain_demo.py
```

Every material parameter is labelled TABULATED or TYPICAL, and the flow law in
particular is a stated example: change $A$, $n$ or $Q$ and every strength in §5
changes. The verification structure survives the substitution, which is why it is
there.

## 10. Common mistakes

1. **Using total stress instead of effective stress.** A factor-of-two error in
   the effective normal stress is a factor-of-two error in the failure strength.
2. **Assuming the fault that fails is the plane of maximum shear.** It is rotated
   towards the compressional axis by $\phi/2$; for $\mu = 0.85$ the difference is
   20 degrees.
3. **Forgetting which principal stress is vertical.** The whole of Anderson's
   theory, and the whole of §4, depends on it.
4. **Quoting a strength profile without its strain rate.** The ductile strength
   scales as $\dot\varepsilon^{1/n}$, so a factor of 100 in strain rate is a
   factor of 4.6 in stress for $n = 3$.
5. **Extrapolating a flow law below its calibration temperature** and presenting
   the result as a strength.
6. **Treating the brittle–ductile transition as a material boundary.** It is a
   crossing of two curves, and it moves with every parameter in them.
7. **Using finite strain and infinitesimal strain interchangeably.** They have
   different principal axes and different magnitudes.
8. **Assuming plane strain is volume-preserving in general.** It is for simple
   shear; compaction and dilation are separate terms.
9. **Reading a rotation as a strain.** A rotated marker is evidence of
   non-coaxiality, and rotation and strain are different parts of $F$.
10. **Comparing a model strength to a measured stress without the uncertainties
    of both.** The model's parameters are of order 50 per cent uncertain in
    combination, which is larger than the differences usually being interpreted.

## 11. Real-world applications

- **Earthquake depth distribution.** The seismogenic layer thickness is the
  brittle–ductile transition, at least to first order
  ([04-07-01 Earthquake Hazard and Ground Motion](../07-geologic-hazards/01-earthquake-hazard.md)).
- **In-situ stress and borehole stability.** The same Coulomb calculation decides
  the mud weight needed to keep a wellbore open without fracturing the formation,
  and the same effective-stress principle governs it.
  Compare [05-08 Borehole and Well-Log Geophysics](../../05-core-geophysics/08-geophysical-logging/README.md).
- **Fault reactivation and induced seismicity.** Whether a mapped fault slips
  under an imposed stress change is a slip-tendency and Coulomb calculation
  ([04-04-02](./02-faults.md),
  [13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](../../13-geodynamics-tectonics/04-tectonophysics-deformation/02-fault-mechanics.md)).
- **Seismic anisotropy and shear-wave splitting.** The alignment of
  crystallographic fabrics by ductile strain — a strain measurement of the kind
  in §7 applied to a whole rock — is one of the two main causes of upper-mantle
  anisotropy ([04-04-04](./04-fractures-joints.md),
  [01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes](../../01-mathematics/15-tensors-and-differential-geometry/05-anisotropy-representation.md)).
- **Landslide and slope stability.** Slope failure is a Coulomb problem with a
  pore-pressure term, evaluated for a specific slip surface
  ([04-07-03 Landslides, Slope Stability and Geotechnical Geophysics](../07-geologic-hazards/03-landslides.md)).
- **Geothermal and reservoir engineering.** The ductile strength at reservoir
  temperature sets whether a formation creeps or behaves elastically over the
  lifetime of a project ([04-06-03 Geothermal Systems, Heat Flow and Resource Assessment](../06-petroleum-and-mineral-systems/03-geothermal-systems.md)).

## 12. Further reading

- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Wiley-Blackwell).** The standard textbook for the stress, strain
  and failure mechanics of this lesson. Level: advanced.
- **Byerlee, J. (1978). Friction of rocks. *Pure and Applied Geophysics* 116,
  615–626.** The compilation of rock-friction measurements behind the
  coefficient used in §4. Level: advanced.
- **Brace, W. F., & Kohlstedt, D. L. (1980). Limits on lithospheric stress
  imposed by laboratory experiments.** The construction of a two-mechanism
  strength profile and the argument for the transition depth. Level: advanced.
- **Zoback, M. D. *Reservoir Geomechanics* (Cambridge University Press).** The
  same mechanics applied to in-situ stress, pore pressure and borehole
  stability, with the practice of estimating each term. Level: advanced to
  graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  The creep laws and the thermal structure used in §5 and §6. Level: advanced.
- **Fossen, H. *Structural Geology* (Cambridge University Press).** The
  observational counterpart: what a rock that has deformed in each of these
  regimes looks like. Level: intermediate to advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [02 Fault Geometry, Kinematics and Fault Classification](./02-faults.md) — the
  faults that this stress state produces, and their slip tendencies.
- [03 Fold Geometry, Mechanisms and Interpretation](./03-folds.md) — the
  deformation that the ductile regime produces.
- [04 Fractures, Joints and Their Geophysical Signature](./04-fractures-joints.md)
  — the fractures that the brittle regime produces, and the anisotropy they
  create.
- [02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  — the tensor itself, in general form.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)
  — the fracture mechanics and the rate-and-state description of friction.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)
  — creep as a continuum constitutive law.
- [13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](../../13-geodynamics-tectonics/04-tectonophysics-deformation/02-fault-mechanics.md)
  — the application of this mechanics to earthquake interaction.

Exercises:
[`exercises/01-stress-strain-rocks-exercises.md`](./exercises/01-stress-strain-rocks-exercises.md)
and
[`exercises/01-stress-strain-rocks-solutions.md`](./exercises/01-stress-strain-rocks-solutions.md).

## Self-assessment checklist

- [ ] I can find the principal stresses of a tensor and say which invariants are
      frame-independent. (§1)
- [ ] I can compute the effective stress and explain why pore pressure controls
      failure. (§2)
- [ ] I can construct a Mohr circle, locate the optimum failure plane and verify
      it against $45^\circ + \phi/2$. (§3)
- [ ] I can derive the differential stress for failure in the normal and reverse
      regimes and explain the constant ratio between them. (§4)
- [ ] I can say why strike-slip strength needs an additional assumption. (§4)
- [ ] I can evaluate a creep flow law, recover its stress exponent, and state its
      regime of validity. (§5)
- [ ] I can locate the brittle–ductile transition by root finding and predict how
      it moves with geotherm, strain rate and activation energy. (§6)
- [ ] I can compute the principal stretches of a deformation gradient tensor and
      verify them against a closed form. (§7)
- [ ] I can give three pieces of evidence from $F$ that a deformation is
      volume-preserving and non-coaxial. (§7)
- [ ] I can list the assumptions of a strength profile and the regime in which
      each fails. (§8)
