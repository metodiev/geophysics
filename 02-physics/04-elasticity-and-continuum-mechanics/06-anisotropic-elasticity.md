---
id: 02-04-06
title: "Anisotropic Elasticity (VTI, HTI, Orthorhombic)"
level: doctoral
prereqs: ["02-04-05", "01-15-05", "01-07-06"]
estimated_minutes: 90
tags: [anisotropy, thomsen, vti, shear-wave-splitting]
---

# Anisotropic Elasticity (VTI, HTI, Orthorhombic)

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the stiffness matrix of a transversely isotropic (VTI) medium, list
   its five independent constants, and explain how a layered or cracked rock
   acquires that symmetry.
2. **Define** the Thomsen parameters $\epsilon$, $\delta$ and $\gamma$ and
   interpret each physically.
3. **Solve** the Christoffel problem for a VTI medium and identify the exact
   results: $v_p(0)$, $v_s(0)$, $v_p(90^\circ)$, $v_{sh}(90^\circ)$ and the exact
   SH-wave formula.
4. **Rotate** a stiffness tensor, construct an HTI medium, and verify that the
   rotation exchanges the roles of the axis and the isotropy plane.
5. **Measure** shear-wave splitting, relate it to $\gamma$, and state when the
   weak-anisotropy approximation is adequate.
6. **Verify** all of the above numerically: exact agreement of the SH formula,
   symmetry preservation under rotation, and a measured splitting against the
   weak-anisotropy prediction.

## Prerequisites

- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md)
  — the isotropic Christoffel problem whose generalisation this is.
- [01-15-05 Anisotropy Representation and Elasticity Tensors](../../01-mathematics/15-tensors-and-differential-geometry/05-anisotropy-representation.md)
  — the representation of anisotropic tensors.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../../01-mathematics/07-linear-algebra/06-eigenvalues.md)
  — the $3\times3$ eigenproblem solved at each propagation direction.

## 1. Why anisotropy is the rule, not the exception

Isotropy requires that the elastic response be the same in every direction. Three
common geophysical situations violate it:

- **Layering.** A sequence of thin beds with contrasting properties is
  *transversely isotropic with a vertical symmetry axis* (VTI) at wavelengths long
  compared with the layering. This is the dominant anisotropy in sedimentary
  basins, and it is a property of the *geometry*, not of any mineral.
- **Aligned cracks or fractures.** A preferred crack orientation makes the
  medium stiffer along the cracks than across them, again giving transverse
  isotropy — but with a horizontal axis (HTI) if the cracks are vertical and
  aligned.
- **Crystal preferred orientation.** Olivine in the mantle deforms by dislocation
  creep that aligns its fast axis with the flow direction, producing VTI (from
  horizontal flow) or HTI (from vertical flow) or a more general symmetry.

Isotropy is the idealisation, and the anisotropy actually present is commonly
reported as of order ten to twenty per cent in velocity — far larger than most
processing errors. That range is a summary of published measurements, not a value
verified in this repository, and it varies strongly with lithology and depth; treat
it as the order of magnitude to expect and measure the actual value for any given
setting.
The practical framing for this lesson is: **isotropic formulas applied to an
anisotropic Earth produce systematic errors of tens of metres in depth and
several per cent in velocity**, and the size can be predicted from the Thomsen
parameters.

## 2. Precise definitions

**Transverse isotropy (TI).** Elastic symmetry with a single rotation axis: the
response is the same for all directions perpendicular to that axis. Five
independent constants.

**VTI / HTI.** TI with a vertical axis (layering, sedimentary basins) / with a
horizontal axis (aligned vertical fractures).

**Voigt notation for VTI.** With the symmetry axis along $z$ and the standard index
order $(11,22,33,23,13,12)$:

$$\mathbf{C}_V = \begin{pmatrix}
C_{11}&C_{12}&C_{13}&0&0&0\\
C_{12}&C_{11}&C_{13}&0&0&0\\
C_{13}&C_{13}&C_{33}&0&0&0\\
0&0&0&C_{44}&0&0\\
0&0&0&0&C_{44}&0\\
0&0&0&0&0&C_{66}
\end{pmatrix},
\qquad C_{12} = C_{11}-2C_{66} . \tag{1}$$

**Thomsen parameters.** Dimensionless combinations that measure the anisotropy:

$$\epsilon = \frac{C_{11}-C_{33}}{2C_{33}}, \qquad
\gamma = \frac{C_{66}-C_{44}}{2C_{44}}, \qquad
\delta = \frac{(C_{13}+C_{44})^2-(C_{33}-C_{44})^2}
{2C_{33}(C_{33}-C_{44})} . \tag{2}$$

**Christoffel matrix.** $\Gamma_{ij} = C_{ijkl}n_jn_l/\rho$; its eigenvalues are the
squared phase velocities and its eigenvectors the polarisations (see lesson
02-04-05 for the isotropic case).

**Shear-wave splitting.** The relative difference between the two S-wave speeds
for a given propagation direction.

## 3. Derivations

### 3.1 Where the five constants come from

Start from the general count of lesson 02-04-03: 21 constants. Imposing the
operations of the hexagonal point group (a rotation by $2\pi/6$ about the axis,
plus the mirror symmetries that the elastic tensor requires) reduces the
independent components to five: $C_{11}$, $C_{33}$, $C_{44}$, $C_{66}$ and
$C_{13}$, with the constraint $C_{12} = C_{11}-2C_{66}$. The demo builds the
matrix entry by entry and *verifies* the constraint on the assembled matrix
($C_{11}-C_{12}-2C_{66} = 0.0$ GPa); this check matters because a matrix with the
right *pattern* but the wrong $C_{12}$ still looks like a plausible VTI tensor
and still gives the correct axial speeds, yet it has **tetragonal** rather than
hexagonal symmetry and therefore rotates incorrectly (section 3.4). The demo uses
$C_{11} = 30$ GPa, $C_{33} = 22$ GPa, $C_{44} = 7$ GPa, $C_{66} = 10$ GPa,
$C_{13} = 12$ GPa, $\rho = 2400$ kg m⁻³ — a model shale-like set, chosen to be
self-consistent, not a measurement.

**Physical reading of the constants.** $C_{33}$ is the stiffness for compression
along the axis; $C_{11}$ for compression perpendicular to it; $C_{44}$ is the
shear modulus for shearing in a plane containing the axis; $C_{66}$ for shearing
in the isotropy plane. In a layered medium $C_{33}$ is the *harmonic* average of
the layer moduli (constant-stress, layer-normal), while $C_{11}$ is close to the
*arithmetic* average (constant-strain, layer-parallel) — the same averaging
dichotomy encountered in lessons 02-03-05 and 02-04-03.

### 3.2 Thomsen parameters, and what each measures

The demo's model gives $\epsilon = 0.181818182$, $\gamma = 0.214285714$,
$\delta = 0.206060606$.

- **$\gamma$** measures the *shear* anisotropy between the two S-wave speeds for
  propagation along the axis: $v_{sh}(90^\circ)$ versus $v_{sv}(90^\circ)$. It is
  the parameter most directly measured by shear-wave splitting.
- **$\epsilon$** measures the P-wave anisotropy between the axial and the
  perpendicular directions: $\epsilon \approx [v_p(90^\circ)-v_p(0)]/v_p(0)$ for
  weak anisotropy.
- **$\delta$** is *not* a contrast between two simple directions: it controls the
  P and SV velocities at **intermediate angles**, near the axis. It is the
  parameter that matters most for reflection travel times at moderate offsets, and
  it is the hardest to measure — it can be determined only from non-vertical
  propagation, which is why it is estimated from walkaway VSPs or from
  wide-azimuth surface data.

The widespread statement that "$\delta$ is poorly constrained" is exactly this: it
is the derivative of the velocity near the axis, and all near-vertical
measurements are insensitive to it. The demo's model has $\delta > \epsilon$,
which is the common case for shales and is why depth conversion based on
near-vertical velocities underestimates depth when an isotropic model is used.

### 3.3 The Christoffel problem for VTI, and the exact results

For propagation in the plane containing the axis, with
$\mathbf n = (\sin\theta, 0, \cos\theta)$, the Christoffel matrix is

$$\boldsymbol\Gamma = \frac{1}{\rho}\begin{pmatrix}
C_{11}\sin^2\theta + C_{44}\cos^2\theta & 0 &
(C_{13}+C_{44})\sin\theta\cos\theta\\
0 & C_{66}\sin^2\theta + C_{44}\cos^2\theta & 0\\
(C_{13}+C_{44})\sin\theta\cos\theta & 0 &
C_{44}\sin^2\theta + C_{33}\cos^2\theta
\end{pmatrix} . \tag{3}$$

Two structural features make the problem tractable:

- The $2\times2$ block in the $x$–$z$ plane is coupled — its eigenvectors are the
  **quasi-P (qP)** and **quasi-SV (qSV)** modes, whose polarisations are neither
  purely longitudinal nor purely transverse except at $\theta = 0$ and $90^\circ$.
- The $y$-component decouples entirely. Its eigenvalue gives the **SH mode** with
  the **exact** speed

$$v_{sh}(\theta) = \sqrt{\frac{C_{66}\sin^2\theta + C_{44}\cos^2\theta}{\rho}} .
\tag{4}$$

The demo verifies equation (4) at six angles with a maximum relative difference of
$0.000\times10^0$ — i.e. exactly, because SH motion is purely horizontal, out of
the plane of the axis and the propagation direction, and therefore does not couple
to the other two modes at any angle.

The exact values at the symmetry directions:

$$v_p(0) = \sqrt{\frac{C_{33}}{\rho}}, \qquad
v_{sv}(0) = v_{sh}(0) = \sqrt{\frac{C_{44}}{\rho}}, \qquad
v_p(90^\circ) = \sqrt{\frac{C_{11}}{\rho}}, \qquad
v_{sh}(90^\circ) = \sqrt{\frac{C_{66}}{\rho}} . \tag{5}$$

For the demo's model these are 3027.650354, 1707.825128, 3535.533906 and
2041.241452 m s⁻¹ — the first two are the slow directions (along the axis) and the
last two the fast ones, as the positive $\epsilon$ and $\gamma$ require.

The qP and qSV speeds have no closed form at general $\theta$ (they are the roots
of a quadratic that involves both the axial and the off-diagonal couplings); the
weak-anisotropy approximations

$$v_{qP}(\theta) \approx v_p(0)\left[1+\delta\sin^2\theta\cos^2\theta
+\epsilon\sin^4\theta\right], \qquad
v_{qSV}(\theta) \approx v_s(0)\left[1+\frac{v_p(0)^2}{v_s(0)^2}
(\epsilon-\delta)\sin^2\theta\cos^2\theta\right] \tag{6}$$

are the standard tools of anisotropic processing, and they are first-order in the
Thomsen parameters. The demo's qP and qSV values at 15°, 30°, 45°, 60° are 3068.66
/ 1699.99, 3173.76 / 1686.38, 3304.56 / 1682.23, 3424.29 / 1690.43 m s⁻¹ — note
that qSV passes through a *minimum* near 45° and returns to the axial value at
90°: **the SV velocity is not monotonic in angle**, a feature with no isotropic
analogue and a classic trap for interpretation with isotropic intuition.

### 3.3.1 Phase velocity is not ray velocity

In an isotropic medium the ray and the wavefront normal coincide. In an
anisotropic medium they do not: the group (ray) velocity vector is

$$\mathbf G = \frac{\partial\omega}{\partial\mathbf k}
= V\,\mathbf n + \frac{\mathrm dV}{\mathrm d\theta}\,\mathbf t ,
\qquad \mathbf t = \frac{\mathrm d\mathbf n}{\mathrm d\theta} , \tag{6a}$$

because $\omega = V(\mathbf n)|\mathbf k|$ depends on direction but not on
$|\mathbf k|$. The ray is therefore tilted away from the wavefront normal by

$$\tan\phi_G = \frac{V\sin\theta + V'\cos\theta}{V\cos\theta - V'\sin\theta} ,
\qquad V' = \frac{\mathrm dV}{\mathrm d\theta} , \tag{6b}$$

and the tilt is first order in the anisotropy. The demo measures it for its own
model (section 7, part 5): the qP ray is tilted towards the fast (horizontal)
direction by $+8.54^\circ$ at $30^\circ$, $+8.59^\circ$ at $45^\circ$ and
$+6.64^\circ$ at $60^\circ$, while the qSV tilt is small and changes sign
($-1.38^\circ$, $+0.36^\circ$, $+1.55^\circ$) because its velocity surface has a
minimum near $45^\circ$. **Angular shifts of several degrees are the rule, not an
edge case**, and they are why a ray-angle-based depth conversion or NMO
correction built on isotropic assumptions mis-ties.

### 3.4 Rotation: VTI becomes HTI

A rotation of the medium by $90^\circ$ about the $y$-axis turns the vertical
symmetry axis into a horizontal one. The tensor transforms as

$$C'_{ijkl} = R_{ip}R_{jq}R_{kr}R_{ls}C_{pqrs} , \tag{7}$$

which is the only correct way to rotate a fourth-rank tensor; rotating the
$6\times6$ matrix with a $3\times3$ rotation applied componentwise is wrong. The
demo applies equation (7) and verifies three things:

- **Symmetry is preserved**: the maximum violation of the minor and major
  symmetries after the rotation is $0.000\times10^0$ Pa. A tensor rotation bug
  would break this.
- **The hexagonal identities still hold in the new frame**: the maximum violation
  of $C_{22}-C_{23}-2C_{44} = 0$, $C_{12} = C_{13}$, $C_{22} = C_{33}$ and
  $C_{55} = C_{66}$ is $0.000\times10^0$ Pa — the rotated medium is transversely
  isotropic about $x$, as it must be.
- **The speeds exchange roles**: along the new symmetry axis ($x$) the P speed is
  $\sqrt{C_{33}/\rho} = 3027.650354$ m s⁻¹, identical to the old axial speed, and
  along $z$ (now in the isotropy plane) it is $\sqrt{C_{11}/\rho} =
  3535.533906$ m s⁻¹. The fast direction followed the axis, which is the
  operational test that the rotation was applied correctly.

The rotated matrix is

$$\mathbf{C}'_V = \begin{pmatrix}
22&12&12&0&0&0\\ 12&30&10&0&0&0\\ 12&10&30&0&0&0\\
0&0&0&10&0&0\\ 0&0&0&0&7&0\\ 0&0&0&0&0&7
\end{pmatrix}\ \text{GPa} , \tag{8}$$

which is the standard HTI form: the isotropy plane is now $y$–$z$, the axis is
$x$, with $C_{22} = C_{33}$, $C_{12} = C_{13}$, $C_{55} = C_{66}$ and
$C_{22}-C_{23} = 2C_{44}$.

> **The trap that this test caught.** An earlier version of the demo assembled the
> VTI matrix with $C_{12} = C_{13} = 12$ GPa instead of the required
> $C_{11}-2C_{66} = 10$ GPa. The matrix had the correct VTI *pattern*, and because
> the Christoffel matrix for propagation in the axis plane does not contain
> $C_{12}$, every velocity in section 3.3 was unaffected — the error was invisible
> in the P and SV results. It appeared only on rotation, where the rotated matrix
> gave $C_{23} = 12$ GPa instead of 10 GPa, so $C_{22}-C_{23} = 18 \ne 2C_{44} =
> 20$: the "HTI" medium was in fact tetragonal about $x$ and its splitting table
> was wrong (the azimuth-45° row read 10.42 per cent instead of the correct 14.93
> per cent). Two lessons generalise: **check the symmetry identities on the
> assembled matrix, not on the constants you believe you used**, and **a test that
> never touches the mistake cannot find it** — here only the rotation test did.

### 3.5 Shear-wave splitting, and what it measures

For an HTI medium the two S waves are **degenerate only along the symmetry axis**.
For every other direction they differ, and the demo's measurements at 45° polar
angle show the splitting varying with azimuth:

| $(\theta, \text{azimuth})$ | $v_{S1}$ (m s⁻¹) | $v_{S2}$ (m s⁻¹) | splitting (%) |
|---|---|---|---|
| (90°, 0°) — along the axis | 1707.825128 | 1707.825128 | 0.0000 |
| (60°, 0°) | 1796.988221 | 1686.382249 | 6.3505 |
| (45°, 0°) | 1881.931632 | 1682.230177 | 11.2061 |
| (45°, 45°) | 1963.203165 | 1690.426681 | 14.9318 |
| (45°, 90°) | 2041.241452 | 1707.825128 | 17.7866 |
| (0°, 0°) — perpendicular to the axis | 2041.241452 | 1707.825128 | 17.7866 |

Three things to read from this table:

1. **Degeneracy is confined to the symmetry axis.** Even propagation *in the
   isotropy plane* splits, because one polarisation lies along the axis and the
   other within the plane; the common statement that "TI media do not split in the
   isotropy plane" is wrong (it is true for propagation *along the axis*).
2. **The splitting is of order $\gamma$ but is not equal to it.** With
   $\gamma = 21.43$ per cent the measured splitting ranges from 0 to 17.79 per cent
   depending on direction, and it depends on both the polar angle and the azimuth.
   The weak-anisotropy result $v_{s1}/v_{s2}-1 \approx \gamma$ (for propagation at
   45° to the axis in the plane of the axis) is recovered only for small
   anisotropy; at 21 per cent it is a rough guide, not a formula.
3. **The fast polarisation direction maps the structure.** In an HTI medium the
   fast S wave polarises **parallel to the fracture planes** (the fracture strike),
   while the slow one polarises along the symmetry axis, i.e. along the fracture
   normal. The physical reason is in ★8 of the exercises: shear motion parallel to
   a crack face slides the faces past one another and never opens the crack, so it
   travels at nearly the intact-rock speed; motion normal to the faces opens and
   closes them and is slowed. Measuring the polarisation azimuth therefore maps the
   crack orientation, which is why S-wave splitting is a standard tool for fracture
   characterisation in reservoirs. For mantle anisotropy the same rule is applied
   with the fast polarisation *commonly interpreted* as parallel to the olivine
   $a$-axis, and hence as an indicator of the flow direction — an interpretation
   supported by mineral physics rather than a theorem.

## 4. Physical interpretation

**Anisotropy is a statement about direction, and every isotropic formula is a
special case.** $v_p = \sqrt{(\lambda+2\mu)/\rho}$ becomes five numbers and a
direction-dependent eigenproblem; the two S speeds become three modes (qP, qSV,
SH), of which two are coupled. The hierarchy of complications is worth keeping in
mind: isotropy (2 constants) → VTI (5) → orthorhombic (9) → monoclinic (13) →
triclinic (21).

**$\delta$ is about near-vertical propagation; $\epsilon$ about the extremes;
$\gamma$ about shear.** The practical consequence: a velocity model calibrated
with near-vertical well ties will get the *shallow* travel times right and the
wide-angle ones wrong unless $\delta$ is included.

**The "quasi" in qP and qSV is not decoration.** Away from the symmetry
directions the polarisations are neither longitudinal nor transverse, so the
recorded three-component motion cannot be separated into "P" and "S" by
polarisation alone. This is why anisotropic processing needs the full eigenvector
information, not just the speeds.

**Phase and group velocity differ, and that is a whole separate problem.** Every
anisotropic quantity in this lesson except the symmetry-direction values is a
*phase* velocity — a property of a plane wave, not of a ray. Seismic travel-time
interpretation needs ray geometry, so anisotropic processing works with both and
the translation between them (equations 6a–6b) is where a large fraction of the
implementation difficulty lies.

**Layer-induced anisotropy is a long-wavelength phenomenon.** A stack of beds with
individual thicknesses of centimetres to metres is anisotropic at seismic
wavelengths of tens to hundreds of metres, and *isotropic* to a laboratory
measurement on a single bed. The label "isotropic" always carries an implicit
wavelength (lesson 02-03-05, equation (1)).

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Linear elasticity | Small strain, reversible | Nonlinearity (above $\sim10^{-6}$ in soils), anelasticity |
| Homogeneous TI | Uniform symmetry axis and constants | Depth-varying anisotropy, or a tilted axis (TTI): the axis orientation must be modelled |
| Symmetry class correct | Exactly hexagonal | Cracked rocks with multiple crack sets are orthorhombic or lower |
| Wavelength $\gg$ layering | Effective-medium description applies | Backus averaging is valid only in this limit; at shorter wavelengths the individual reflections matter |
| Weak anisotropy for the Thomsen approximations | $|\epsilon|, |\delta|, |\gamma| \ll 1$ | At 20 per cent the approximations are indicative, not quantitative |
| Phase velocities | Plane waves in an unbounded medium | Group (ray) velocities differ from phase velocities in anisotropic media, and the difference is first-order in the anisotropy — this is a major source of confusion |

## 6. Units and dimensional analysis

- All $C_{ij}$: Pa ✓; all speeds: m s⁻¹ ✓; $\epsilon,\delta,\gamma$ dimensionless
  ✓ (each is a ratio of moduli differences to moduli).
- The hexagonal constraint $C_{11}-C_{12} = 2C_{66}$ is dimensionally homogeneous
  and is an exact identity for VTI ✓ — the quickest test that a measured set of
  five constants is self-consistent.
- $\Gamma_{ij} = C_{ijkl}n_jn_l/\rho$: Pa/Pa/(kg m⁻³) = m² s⁻² ✓, so its square
  roots are speeds.
- For the demo's model: $v_p(0)$ from $\sqrt{C_{33}/\rho} =
  \sqrt{22\times10^9/2400} = 3027.65$ m s⁻¹, and the general-angle qP value must
  lie between 3027.65 and 3535.53 — a bound computed *before* the eigenproblem,
  which is a useful check on the numerics.

## 7. Python demonstration

[`code/anisotropic_elasticity_demo.py`](./code/anisotropic_elasticity_demo.py)
builds the VTI tensor, computes the Thomsen parameters, solves the Christoffel
problem at several angles, rotates the tensor to HTI and measures the splitting.
Observed output:

```text
C11 = 30.0, C33 = 22.0, C44 = 7.0, C66 = 10.0, C13 = 12.0 GPa, rho = 2400 kg/m^3
C12 = C11 - 2 C66 = 10.0 GPa (the hexagonal constraint)
check on the assembled matrix: C11 - C12 - 2 C66 = 0.0 GPa (must be 0 for hexagonal symmetry)
epsilon = (C11 - C33)/(2 C33)                    = 0.181818182
gamma   = (C66 - C44)/(2 C44)                    = 0.214285714
delta   = ((C13 + C44)^2 - (C33 - C44)^2)/(2 C33 (C33 - C44)) = 0.206060606
```

```text
exact results: v_p(0) = sqrt(C33/rho) = 3027.650354 m/s
               v_sv(0) = v_sh(0) = sqrt(C44/rho) = 1707.825128 m/s
               v_p(90) = sqrt(C11/rho) = 3535.533906 m/s
               v_sh(90) = sqrt(C66/rho) = 2041.241452 m/s
 theta (deg)   v_qP (m/s)   v_qSV (m/s)   v_SH (m/s)   SH formula   SH error
         0.0  3027.650354   1707.825128  1707.825128  1707.825128   0.00e+00
        15.0  3068.658837   1699.987431  1732.166502  1732.166502   0.00e+00
        30.0  3173.764575   1686.382249  1796.988221  1796.988221   0.00e+00
        45.0  3304.557706   1682.230177  1881.931632  1881.931632   0.00e+00
        60.0  3424.294229   1690.426681  1963.203165  1963.203165   0.00e+00
        90.0  3535.533906   1707.825128  2041.241452  2041.241452   0.00e+00
max relative difference between the SH eigenvalue and its closed form = 0.000e+00
```

```text
HTI stiffness matrix (GPa), symmetry axis now along x:
   [  22.000,   12.000,   12.000,    0.000,   -0.000,    0.000]
   [  12.000,   30.000,   10.000,    0.000,    0.000,    0.000]
   [  12.000,   10.000,   30.000,    0.000,   -0.000,    0.000]
   [   0.000,    0.000,    0.000,   10.000,    0.000,   -0.000]
   [  -0.000,    0.000,   -0.000,    0.000,    7.000,    0.000]
   [   0.000,    0.000,    0.000,   -0.000,    0.000,    7.000]
max symmetry violation after rotation = 0.000e+00 Pa
max violation of the hexagonal identities of the rotated matrix (TI about x) = 0.000e+00 Pa
speeds along the symmetry axis (x): v_p = 3027.650354 m/s (= sqrt(C33/rho) = 3027.650354)
speeds along z (isotropy plane):    v_p = 3535.533906 m/s (= sqrt(C11/rho) = 3535.533906)
```

```text
 theta (deg)  azimuth (deg)   v_S1 (m/s)   v_S2 (m/s)  splitting (%)  gamma (%)
        90.0            0.0  1707.825128  1707.825128         0.0000    21.4286
        60.0            0.0  1796.988221  1686.382249         6.3505    21.4286
        45.0            0.0  1881.931632  1682.230177        11.2061    21.4286
        45.0           45.0  1963.203165  1690.426681        14.9318    21.4286
        45.0           90.0  2041.241452  1707.825128        17.7866    21.4286
         0.0            0.0  2041.241452  1707.825128        17.7866    21.4286
```

```text
 theta (deg)  mode  phase V (m/s)  group |G| (m/s)  group angle  dphi (deg)
        30.0    qP    3173.764575      3209.323234    38.537002   +8.537002
        30.0   qSV    1686.382249      1686.873700    28.616921   -1.383079
        45.0    qP    3304.557706      3342.012482    53.586054   +8.586054
        45.0   qSV    1682.230177      1682.263736    45.361907   +0.361907
        60.0    qP    3424.294229      3447.449627    66.644437   +6.644437
        60.0   qSV    1690.426681      1691.047288    61.552320   +1.552320
max difference between G = V n + V' t and the direct derivative d(omega)/dk of the Christoffel dispersion relation = 8.626e-04 m/s
```

### What to observe

| Observation | Consequence |
|---|---|
| The SH eigenvalue matches the closed form exactly ($0.00\times10^0$) at every angle | The SH mode decouples completely; this is the one exact non-trivial anisotropic result in the lesson and it is verified, not asserted |
| qSV dips to 1682.23 m s⁻¹ at 45° before returning to 1707.83 m s⁻¹ at 90° | The SV velocity is non-monotonic in angle; isotropic intuition ("faster along the fast axis, slower across it") fails for SV |
| The rotation leaves every symmetry and hexagonal identity intact ($0.000\times10^0$ violation) | The fourth-rank transformation (7) was applied correctly; a componentwise $6\times6$ rotation would have broken the symmetry |
| The speeds exchange roles after rotation, matching $\sqrt{C_{33}/\rho}$ and $\sqrt{C_{11}/\rho}$ | The physical check that the rotation, not the arithmetic, is right |
| The splitting is 0 only along the symmetry axis and up to 17.79 per cent across it | Degeneracy is a symmetry property, not a general one; the "isotropy plane" does not imply degeneracy |
| The qP ray is tilted 6.6–8.6° from the wavefront normal and the qSV tilt changes sign near 45° | Group and phase directions differ by a first-order-in-anisotropy amount; the sign change accompanies the qSV velocity minimum at 45° |
| $G = V\mathbf n + V'\mathbf t$ agrees with the direct numerical derivative $\partial\omega/\partial\mathbf k$ of the Christoffel dispersion relation to $8.6\times10^{-4}$ m s⁻¹ | The group-velocity relation (6a) is verified independently, with the residual set by the finite-difference step ($h = 10^{-6}$ rad, $k$ step $10^{-3}$) rather than by the physics |
| The splitting is of order $\gamma$ but not equal to it | At 21 per cent anisotropy the weak-anisotropy approximations are guides, not formulas; quantitative work needs the exact eigenproblem |

> **Breaking exercise.** Set $C_{13}$ to a value that makes $\delta = \epsilon$
> (solve equation (2) for $C_{13}$) and predict, before running, whether the qP
> velocity at 45° changes and in which direction. Then verify and explain the
> answer in terms of equation (6).

## 8. Common mistakes

1. **Applying isotropic velocity formulas to an anisotropic medium.** The error
   can be 10–20 per cent in $v_p$, and it is systematic, not random.
2. **Building a TI matrix without imposing its identity.** A VTI matrix needs
   $C_{12} = C_{11}-2C_{66}$; omitting it gives a tetragonal tensor that looks
   right, reproduces the axial speeds, and rotates to a *different* (wrong)
   medium. Always test the identity on the assembled matrix (section 3.4).
3. **Rotating a $6\times6$ stiffness matrix componentwise.** The fourth-rank
   transformation (7) is required; the Bond-matrix formulation is the compact way
   to do it correctly.
4. **Assuming "transversely isotropic" means "weakly anisotropic".** "TI" names a
   symmetry, not a magnitude; measured shales commonly have $\epsilon$ and
   $\gamma$ of several per cent to a few tens of per cent, and at the upper end
   the weak-anisotropy approximations of equation (6) become indicative rather
   than quantitative.
5. **Confusing $\epsilon$, $\delta$ and $\gamma$.** They control different
   observables: shear splitting, near-vertical P/SV travel times, and the extreme
   P contrasts respectively.
6. **Reading one of $\epsilon$ or $\delta$ from the other.** They are independent
   measurements; $\delta$ requires non-vertical data.
7. **Conflating phase and group velocity.** In an anisotropic medium the ray
   (group) direction differs from the wavefront (phase) direction, and the
   difference is first order in the anisotropy: the demo measures a 6.6–8.6°
   tilt of the qP ray from the wavefront normal (section 7, part 5).
8. **Treating the symmetry axis as always vertical or horizontal.** Tilted
   transverse isotropy (TTI) is common in folded and dipping sequences, and using
   VTI there produces large imaging errors.
9. **Assuming a single S-wave arrival.** Where splitting exists there are two, and
   "picking the S arrival" without specifying which one is a 10 per cent velocity
   ambiguity.
## 9. Real-world applications

- **Depth conversion.** $\delta$ controls the depth error of a seismic section
  converted with an isotropic velocity model; in shale sequences the errors reach
  several per cent, which is tens of metres at reservoir depths
  ([06-seismology](../../06-seismology/README.md)).
- **Fracture characterisation.** Shear-wave splitting azimuth and magnitude map
  fracture orientation and density, used in reservoir permeability prediction and
  in the design of horizontal wells
  ([05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Mantle flow.** Olivine lattice-preferred orientation produces seismic
  anisotropy; the fast-polarisation directions from SKS splitting are the primary
  observational constraint on asthenospheric and lower-mantle flow
  ([12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)).
- **Anisotropic imaging and inversion.** Modern seismic processing inverts for
  $\epsilon$ and $\delta$ fields together with the velocities; ignoring them
  produces mis-ties between migrated sections and well depths.
- **Effective-medium modelling.** Backus averaging for layering, and crack-density
  theories (Hudson, Eshelby) for fractures, predict the five constants from the
  microstructure — this is how anisotropy is tied to geology.
- **Borehole seismics.** Walkaway VSPs provide the off-vertical angles needed to
  constrain $\delta$, and are the standard source of calibration data.

## 10. Further reading

- **Thomsen, L. (1986), *Weak elastic anisotropy*, Geophysics.** The paper that
  defined the parameters used here; read it for the derivation and the physical
  discussion of $\delta$. Level: advanced.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The anisotropic wave-propagation chapter, including the
  Christoffel problem in its general form. Level: advanced.
- **Tsvankin, I. *Seismic Signatures and Analysis of Reflection Data in
  Anisotropic Media* (Pergamon).** The standard reference for the applied
  treatment: travel times, moveout, inversion for Thomsen parameters. Level:
  advanced.
- **Musgrave, M. J. P. *Crystal Acoustics* (Holden-Day).** The classical
  derivation of the Christoffel equation and the classification of the symmetry
  classes. Level: graduate.
- **Nye, J. F. *Physical Properties of Crystals* (Oxford University Press).** The
  symmetry tables and the transformation properties of tensors. Level: advanced.
- **Backus, G. E. (1962), *Long-wave elastic anisotropy produced by horizontal
  layering*, Journal of Geophysical Research.** The derivation of layer-induced
  anisotropy; read it to see the averaging argument in full. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) —
  the isotropic limit of this lesson, and the origin of the Christoffel method.
- [07 Viscoelasticity, Creep and Anelastic Relaxation](./07-viscoelasticity.md) —
  the symmetry of the time-dependent response, which can itself be anisotropic.
- [03 Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md) —
  the counting of constants by symmetry class.
- [02-03-07 Dispersion, Group Velocity and Phase vs Group Speed](../03-oscillations-and-waves/07-dispersion.md)
  — the phase/group distinction, which is first-order in anisotropic media.
- [01-15-05 Anisotropy Representation and Elasticity Tensors](../../01-mathematics/15-tensors-and-differential-geometry/05-anisotropy-representation.md)
  — the tensor algebra used in the rotation.
- [06-seismology](../../06-seismology/README.md) — anisotropic imaging and
  fracture characterisation.

Exercises:
[`exercises/06-anisotropic-elasticity-exercises.md`](./exercises/06-anisotropic-elasticity-exercises.md)
and
[`exercises/06-anisotropic-elasticity-solutions.md`](./exercises/06-anisotropic-elasticity-solutions.md).

## Self-assessment checklist

- [ ] I can write the VTI stiffness matrix and name the five independent
      constants. (Section 2)
- [ ] I can define $\epsilon$, $\delta$ and $\gamma$ and say which observable each
      controls. (Section 3.2)
- [ ] I can write the VTI Christoffel matrix for propagation in the axis plane and
      identify the decoupled SH mode. (Section 3.3)
- [ ] I can state the exact results at $\theta = 0$ and $90^\circ$ and derive the
      SH formula. (Section 3.3)
- [ ] I can explain why qSV is non-monotonic in angle. (Section 3.3)
- [ ] I can rotate a stiffness tensor with the fourth-rank transformation and
      verify the result by a symmetry and a physical check. (Section 3.4)
- [ ] I can explain where shear-wave splitting is non-zero and what its fast
      direction means. (Section 3.5)
- [ ] I can state the wavelength condition for layer-induced anisotropy.
      (Section 4)
- [ ] I can list three geophysical settings that are anisotropic and the symmetry
      each produces. (Section 1)
