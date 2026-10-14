# Solutions — 02-04-06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)

Solutions to [`06-anisotropic-elasticity-exercises.md`](./06-anisotropic-elasticity-exercises.md).
Numerical answers were produced with the companion script
[`../code/anisotropic_elasticity_demo.py`](../code/anisotropic_elasticity_demo.py)
or with the closed forms quoted; wherever a value came from a computation it is
given to the precision the computation supports. Model parameters are **chosen**,
not measured.

---

## ★1

(a) Hexagonal constraint:

$$C_{12} = C_{11}-2C_{66} = 40-2(12) = 16\ \text{GPa}.$$

(b) Thomsen parameters:

$$\epsilon = \frac{40-30}{2(30)} = 0.166666667, \qquad
\gamma = \frac{12-9}{2(9)} = 0.166666667,$$

$$\delta = \frac{(15+9)^2-(30-9)^2}{2(30)(30-9)}
= \frac{576-441}{1260} = 0.107142857 .$$

(c) Symmetry-direction speeds, from $v = \sqrt{C/\rho}$:

| quantity | formula | value (m s⁻¹) |
|---|---|---|
| $v_p(0)$ | $\sqrt{C_{33}/\rho}$ | 3464.101615 |
| $v_{sv}(0)$ | $\sqrt{C_{44}/\rho}$ | 1897.366596 |
| $v_p(90^\circ)$ | $\sqrt{C_{11}/\rho}$ | 4000.000000 |
| $v_{sh}(90^\circ)$ | $\sqrt{C_{66}/\rho}$ | 2190.890230 |

(d) Both modes are **faster across the axis** than along it, because $\epsilon>0$
and $\gamma>0$. Note that this is what the Thomsen parameters say: $\epsilon>0$
means $C_{11}>C_{33}$, and $\gamma>0$ means $C_{66}>C_{44}$.

*Check:* all speeds are between the slowest and fastest of the four tabulated
values, and each is the square root of a modulus ratio, so the units are
m s⁻¹ ✓.

---

## ★2

(a) With $n_x = \sin\theta$, $n_y = 0$, $n_z = \cos\theta$, the Christoffel matrix is
equation (3) of the lesson. The $y$–$y$ entry involves no coupling to the other
components:

$$\Gamma_{yy} = \frac{C_{66}\sin^2\theta + C_{44}\cos^2\theta}{\rho} .$$

(b) If $\mathbf u = (0,1,0)$ then $\boldsymbol\Gamma\mathbf u = \Gamma_{yy}\mathbf u$
because the only non-zero entries of the first and third rows are in the
$x$–$z$ block. So $(0,1,0)$ is an exact eigenvector for every $\theta$. Physically
the polarisation is purely horizontal and perpendicular to the plane containing
the symmetry axis and the propagation direction, so the motion never compresses
the layered/cracked structure in a way that would couple it to the other modes.

(c) $\theta = 0$: $v_{sh} = \sqrt{C_{44}/\rho}$. $\theta = 90^\circ$:
$v_{sh} = \sqrt{C_{66}/\rho}$ ✓ — both match equation (5).

(d) Because qP and qSV polarisations are not purely longitudinal/transverse
except at $\theta = 0$ and $90^\circ$: their $2\times2$ Christoffel block is
coupled through the off-diagonal entry $(C_{13}+C_{44})\sin\theta\cos\theta/\rho$,
so the eigenvectors rotate with $\theta$ and the eigenvalues are the roots of a
quadratic rather than single entries.

*Numerical confirmation.* The demo reports a maximum relative difference of
$0.000\times10^0$ between the SH eigenvalue and equation (4) over six angles
(0°, 15°, 30°, 45°, 60°, 90°).

---

## ★3

(a) **Triclinic** 21, **monoclinic** 13, **orthorhombic** 9.
(b) **Tetragonal** 6 (or 7 depending on the class; the elastic classes of
tetragonal symmetry have 6 or 7), **hexagonal** 5 (VTI/HTI are the transversely
isotropic member of this group), **cubic** 3.
(c) **Isotropic** 2 ($\lambda$, $\mu$).
(d) **Layering alone** with a horizontal symmetry axis is *exactly* the
hexagonal (VTI) case in the long-wavelength limit, whatever the number of
constituents — Backus (1962). Layering cannot produce lower symmetry than VTI,
because a stack of beds is invariant under every rotation about the stack normal.
All classes below hexagonal require additional structure (cracks, crystals,
preferred orientation, dipping or tilted layers).

*Note on the counts:* numbers of independent elastic constants per symmetry class
vary with the point group within a crystal system (for example tetragonal classes
have 6 or 7). The values quoted here are the ones standard in elasticity texts;
if a specific application depends on the count for a particular point group,
check the group's tables rather than a summary.

---

## ★4

(a) HTI with the symmetry axis along $x$, Voigt order $(11,22,33,23,13,12)$:

$$\mathbf C_V = \begin{pmatrix}
C_{33}&C_{12}&C_{12}&0&0&0\\
C_{12}&C_{11}&C_{13}&0&0&0\\
C_{12}&C_{13}&C_{11}&0&0&0\\
0&0&0&C_{66}&0&0\\
0&0&0&0&C_{44}&0\\
0&0&0&0&0&C_{44}
\end{pmatrix},$$

with $C_{22} = C_{33} = C_{11}$ (old frame), i.e. the entries $C_{22}=C_{33}$ and
$C_{13}=C_{23}$ in the new frame, and $C_{55}=C_{66}$. The identity of the
isotropy plane ($y$–$z$) is $C_{22}-C_{23} = 2C_{44}$.

(b) For the ★1 constants: $v_p$ along $x$ (the axis) is
$\sqrt{C_{33}/\rho}$ with $C_{33}$ now the original $C_{11}$, so
$v_p(x) = 4000.000000$ m s⁻¹; along $y$ and $z$ (both in the isotropy plane) it
is $\sqrt{C_{33}^{\text{old}}/\rho} = 3464.101615$ m s⁻¹.

(c) Degenerate S waves occur **only for propagation along the symmetry axis**,
where every direction perpendicular to the axis is crystallographically
equivalent. With the ★1 constants the degenerate S speed along $x$ is
$\sqrt{C_{44}^{\text{old}}/\rho} = 1897.366596$ m s⁻¹ (the S polarisation is
free to lie anywhere in the isotropy plane, all of them equivalent).

(d) A set of aligned vertical fractures is *parallel planes*; the medium is
invariant under every rotation about the normal to those planes, and that normal
is therefore the symmetry axis. Equivalently: a shear wave polarised parallel to
the fracture planes slides the crack faces past one another and never opens them,
so it travels at the intact-rock speed, while a shear polarised normal to the
planes opens and closes them and is slowed. That is exactly the HTI pattern.

---

## ★5

(a) From the demo: $\epsilon = 0.181818182$, $\gamma = 0.214285714$,
$\delta = 0.206060606$; $v_p(0) = 3027.650354$, $v_{sv}(0) = v_{sh}(0) =
1707.825128$, $v_p(90^\circ) = 3535.533906$, $v_{sh}(90^\circ) = 2041.241452$
m s⁻¹.

(b) All six SH errors are $0.00\times10^0$; the maximum relative difference
between the SH eigenvalue and its closed form is also $0.000\times10^0$. It is
*exact* rather than small because the SH motion is purely horizontal and out of
the axis–propagation plane, so $\Gamma_{yy}$ is an eigenvalue with eigenvector
$(0,1,0)$ rather than a coupled block (★2).

(c)

| $\theta$ | $v_{qP}$ (m s⁻¹) | $v_{qSV}$ (m s⁻¹) | $v_{SH}$ (m s⁻¹) |
|---|---|---|---|
| 0° | 3027.650354 | 1707.825128 | 1707.825128 |
| 30° | 3173.764575 | 1686.382249 | 1796.988221 |
| 45° | 3304.557706 | 1682.230177 | 1881.931632 |
| 60° | 3424.294229 | 1690.426681 | 1963.203165 |
| 90° | 3535.533906 | 1707.825128 | 2041.241452 |

qP increases monotonically from the axis to the isotropy plane. qSV does **not**:
it *decreases* from 1707.825 at 0° to a minimum of 1682.230 at 45°, then rises
back to 1707.825 at 90°. So qSV can be slower at 45° than along the symmetry axis
— an effect with no isotropic counterpart.

(d) Both $\epsilon$ and $\delta$ enter the qP approximation (equation 6), so both
control the variation with angle; the **near-vertical** behaviour is controlled by
$\delta$ alone, because the $\epsilon$ term is $O(\sin^4\theta)$ while the $\delta$
term is $O(\sin^2\theta\cos^2\theta)$ — at small $\theta$ the $\delta$ term
dominates even for $\epsilon \sim \delta$. $\gamma$ controls neither (it is a
shear parameter).

(e) From section 5 of the demo (its own model):

| $\theta$ | $\Delta\phi$ qP (deg) | $\Delta\phi$ qSV (deg) |
|---|---|---|
| 30° | $+8.537002$ | $-1.383079$ |
| 45° | $+8.586054$ | $+0.361907$ |
| 60° | $+6.644437$ | $+1.552320$ |

The qP ray is tilted towards the fast direction by roughly half the anisotropy
magnitude; the qSV tilt is small and changes sign, consistent with the qSV
velocity minimum near 45°. The two independent group-velocity computations agree
to $8.626\times10^{-4}$ m s⁻¹ (finite-difference truncation, not physics).

---

## ★6

(a) The rotated matrix (GPa) is

```
   [  22.000,   12.000,   12.000,    0.000,    0.000,    0.000]
   [  12.000,   30.000,   10.000,    0.000,    0.000,    0.000]
   [  12.000,   10.000,   30.000,    0.000,    0.000,    0.000]
   [   0.000,    0.000,    0.000,   10.000,    0.000,    0.000]
   [   0.000,    0.000,    0.000,    0.000,    7.000,    0.000]
   [   0.000,    0.000,    0.000,    0.000,    0.000,    7.000]
```

with all symmetries satisfied to $0.000\times10^0$ Pa. The symmetry axis is
now **$x$** (the axis along which $C_{11} = 22$ GPa is the smallest axial
modulus), the isotropy plane is $y$–$z$, and
$C_{22}-C_{23} = 30-10 = 20 = 2C_{44}$ ✓.

(b) Maximum symmetry violation after rotation = $0.000\times10^0$ Pa; the maximum
violation of the hexagonal identities of the rotated matrix is also
$0.000\times10^0$ Pa. This tests that the *fourth-rank* transformation (7) was
applied and that the result really is TI about the new axis — not merely that the
matrix is symmetric.

(c) Original $C_{33} = 22$ GPa, $C_{11} = 30$ GPa; $v_p$ along the rotated axis
$x$ is 3027.650354 m s⁻¹ $= \sqrt{C_{33}/\rho}$, and along $z$ (in the isotropy
plane) 3535.533906 m s⁻¹ $= \sqrt{C_{11}/\rho}$ — identical to the original
axial and in-plane speeds, as they must be.

(d) Rotating a $6\times6$ Voigt matrix componentwise ignores that each entry is a
component pair; for example a rotation mixes $C_{11}$, $C_{33}$, $C_{13}$ and
$C_{44}$, and the correct transformation of a fourth-rank tensor maps a VTI
matrix to an HTI matrix in which $C_{12}$ becomes the old $C_{13}$ and $C_{23}$
becomes the old $C_{12}$. Componentwise rotation silently produces a tensor that
does not satisfy the elastic symmetries, and the resulting Christoffel matrix
gives wrong (often complex or negative) eigenvalues.

---

## ★7

(a) From $v = \sqrt{C/\rho}$ with $\rho = 2450$ kg m⁻³:

$$C_{33} = \rho v_p(0)^2 = 2.832200\times10^{10}\ \text{Pa (28.3220 GPa)},$$
$$C_{11} = \rho v_p(90^\circ)^2 = 4.118450\times10^{10}\ \text{Pa (41.1845 GPa)},$$
$$C_{66} = \rho v_{sh}(90^\circ)^2 = 1.411200\times10^{10}\ \text{Pa (14.1120 GPa)},$$
$$C_{44} = \rho v_{sv}(0)^2 = 8.844500\times10^{9}\ \text{Pa (8.8445 GPa)}.$$

(b) $\epsilon = (C_{11}-C_{33})/(2C_{33}) = 0.227076125$;
$\gamma = (C_{66}-C_{44})/(2C_{44}) = 0.297783934$. Both are large — this is a
strongly anisotropic shale, and the weak-anisotropy approximations would be poor.

(c) Isotropic average $\bar v_p = (3400+4100)/2 = 3750$ m s⁻¹. A two-way time
converted with 3750 instead of 3400 overstates the depth by
$3750/3400 - 1 = 10.2941$ per cent, i.e. **+0.3088 km at a true depth of 3 km**
(3.3088 km reported). Sign and size matter: the error is a *bias*, not noise, and
it grows with depth.

*Comment.* This is why anisotropic depth conversion is standard practice in
shale-prone basins; the error is not a processing artefact but a consequence of
using a model with the wrong symmetry.

(d) The missing parameter is $\delta$, which controls the P and SV velocities at
intermediate angles (equation 6) and therefore the moveout. It can be measured
from data with non-vertical propagation: a walkaway (offset) VSP, a
multi-offset/multi-azimuth surface survey, or a dipole-sonic cross-dipole logging
run for the shear part.

---

## ★8

(a) Along the symmetry axis (propagation normal to the fracture planes) the two S
waves are **degenerate**: both have speed $v_{s}(0) = 2300$ m s⁻¹, so the
splitting is 0.

(b) Perpendicular to the axis (propagation in the isotropy plane), the two S
speeds are $v_{s,\text{slow}} = \sqrt{C_{44}/\rho}$ and
$v_{s,\text{fast}} = \sqrt{C_{66}/\rho}$ with
$C_{44} = \rho v_s(0)^2 = 1.296050\times10^{10}$ Pa and
$C_{66} = C_{44}(1+2\gamma) = 1.451576\times10^{10}$ Pa. Hence

$$v_{s,\text{fast}} = 2434.091206\ \text{m s}^{-1}, \qquad
v_{s,\text{slow}} = 2300.000000\ \text{m s}^{-1} .$$

Splitting, using the demo's mean-normalised convention
$(v_1-v_2)/[\tfrac12(v_1+v_2)]$: **5.6649 per cent**. Using the slow speed as
reference: 5.8301 per cent.

*Regime note.* This splitting is **not** equal to $\gamma = 6$ per cent, but it is
close to it; the discrepancy is $O(\gamma^2)$, which is why the weak-anisotropy
rule of thumb works at 6 per cent and would be misleading at 30 per cent (compare
★7).

(c) The **fast** polarisation is parallel to the fracture planes (the fracture
strike); the slow one is parallel to the symmetry axis, i.e. normal to the
fracture planes. Verified physically: shear motion parallel to the crack faces
slides them past each other (crack stays shut, rock-like stiffness), while motion
normal to them opens and closes the cracks (softened, slower).

(d) With two orthogonal source/receiver orientations the shear wave is split into
a fast and a slow arrival; the polarisation of the fast arrival is read directly
from the records, without needing any velocity model, because it is a *direction*
(the azimuth of the leading motion), not a velocity. Alignment of the two
horizontal components along the fast azimuth gives the fracture strike; the
*time delay* between the fast and slow arrivals gives the magnitude (here a
5.7 per cent velocity contrast) once a path length is assumed.

---

## ★9

(a) **Backus (1962) averaging.** For finely layered isotropic constituents with
volume fractions $f_i$, Lamé parameters $\lambda_i,\mu_i$ and
$M_i = \lambda_i+2\mu_i$, the long-wavelength effective medium is VTI with

$$C_{33} = \left\langle \frac{1}{M}\right\rangle^{-1}, \qquad
C_{44} = \left\langle \frac{1}{\mu}\right\rangle^{-1}, \qquad
C_{66} = \langle\mu\rangle,$$

$$C_{13} = \left\langle\frac{\lambda}{M}\right\rangle
\left\langle\frac{1}{M}\right\rangle^{-1}, \qquad
C_{11} = \left\langle\frac{4\mu(\lambda+\mu)}{M}\right\rangle
+ \left\langle\frac{\lambda}{M}\right\rangle^{2}
\left\langle\frac{1}{M}\right\rangle^{-1},$$

where $\langle\cdot\rangle$ is the volume-fraction-weighted average.
$C_{33}$ is a harmonic average because a wave travelling normal to the layers puts
every layer in the **same stress** state (constant-stress / Reuss-type averaging),
and the compliant layer dominates the strain. $C_{44}$ is likewise a harmonic-type
average of the shear moduli: for shear with displacement along the layer, all
layers share the same shear stress and the softest layer dominates. The
combination in $C_{11}$ is not a simple average, because in-plane normal strain is
shared (constant-strain) but the axial strain is free, which mixes both limits.
Backus's paper derives these from the elastic wave equation in the
long-wavelength limit, and is the standard primary source for the result.

*Sanity check of the expressions:* for a single isotropic layer,
$\langle1/M\rangle^{-1} = M$, $\langle1/\mu\rangle^{-1} = \mu$,
$\langle\lambda/M\rangle/\langle1/M\rangle = \lambda$ and
$\langle4\mu(\lambda+\mu)/M\rangle + \lambda^2/M = (4\mu\lambda+4\mu^2+\lambda^2)/M
= M$, so $C_{11} = C_{33} = M$ ✓ (isotropy is recovered).

(b) Layer moduli (from $\mu = \rho v_s^2$, $\lambda = \rho(v_p^2-2v_s^2)$):

| layer | $f$ | $\lambda$ (Pa) | $\mu$ (Pa) | $M = \lambda+2\mu$ (Pa) |
|---|---|---|---|---|
| shale (3200, 1800, 2400) | 0.6 | $9.024000\times10^{9}$ | $7.776000\times10^{9}$ | $2.457600\times10^{10}$ |
| limestone (6000, 3200, 2650) | 0.4 | $4.112800\times10^{10}$ | $2.713600\times10^{10}$ | $9.540000\times10^{10}$ |

Effective density $= 0.6(2400)+0.4(2650) = 2500$ kg m⁻³. Applying the formulae:

$$C_{33} = 3.495656\times10^{10}\ \text{Pa}, \quad
C_{44} = 1.088127\times10^{10}\ \text{Pa}, \quad
C_{66} = 1.552000\times10^{10}\ \text{Pa},$$
$$C_{13} = 1.372943\times10^{10}\ \text{Pa}, \quad
C_{11} = 4.921753\times10^{10}\ \text{Pa}, \quad
C_{12} = 1.817753\times10^{10}\ \text{Pa}.$$

*Checks.* $C_{11}-C_{12} = 3.104000\times10^{10} = 2C_{66}$ ✓ (the hexagonal
identity, which the Backus formulae satisfy identically — a free consistency test
on the algebra). $C_{33}$ lies between the layer values $2.4576\times10^{10}$ and
$9.54\times10^{10}$ ✓.

Resulting velocities: $v_p(0) = \sqrt{C_{33}/\rho} = 3739.3347$ m s⁻¹;
$v_p(90^\circ) = \sqrt{C_{11}/\rho} = 4437.0050$ m s⁻¹. For comparison, the
arithmetic mean of the layer $v_p$ is 4320.0000 m s⁻¹ and the harmonic mean
3934.4262 m s⁻¹: the normal-incidence speed 3739.33 is **below** the harmonic mean
because it is a harmonic average of $M$, not of $v_p$, so the comparison is
indicative only of the correct ordering.

(c)

$$\epsilon = \frac{4.921753-3.495656}{2(3.495656)} = 0.203981394, \qquad
\gamma = \frac{1.552000-1.088127}{2(1.088127)} = 0.213152225 .$$

Both are about 0.2 — **large enough to matter**: a 20 per cent $\epsilon$ means a
horizontal-versus-vertical $v_p$ difference of about 1 km s⁻¹ here, so isotropic
depth conversion over such a stack would be biased by roughly 10 per cent
(compare ★7(c)). This is the standard explanation for why thick
sand–shale sequences are routinely found to be anisotropic.

(d) The condition is that the wavelength be much larger than the layer thickness
(and, more precisely, larger than the layer thickness divided by the
anisotropy contrast). If it is violated — at high seismic frequencies, or for
thin/thick alternations — the stack must be treated as a set of reflectors: the
response becomes a series of reflections and interbed multiples rather than a
single anisotropic medium, dispersion appears at the transition scale, and the
effective-medium anisotropic speeds are no longer the speeds of the wavefronts.
The transition scale is not a single number; it is of order the layer thickness
divided by the fractional contrast, so a 1 per cent contrast layer is already
"thin" at many wavelengths while a 50 per cent contrast layer is not.

---

## ★10

(a) In a homogeneous medium $\omega = V(\mathbf n)|\mathbf k|$ depends on the
*direction* of $\mathbf k$ but not on its magnitude, so
$\mathbf G = \partial\omega/\partial\mathbf k$ has a component along
$\mathbf n$ (from $\partial|\mathbf k|$) and one along
$\mathbf t = \mathrm d\mathbf n/\mathrm d\theta$ (from $\partial V/\partial\theta$):

$$\mathbf G = V\,\mathbf n + \frac{\mathrm dV}{\mathrm d\theta}\,\mathbf t .$$

$\mathbf G$ is parallel to $\mathbf n$ only if $\mathrm dV/\mathrm d\theta = 0$ —
i.e. only if the slowness surface is a sphere, which is exactly the isotropic
case (or the symmetry directions). Since $\partial\omega/\partial\mathbf k$ is the
definition of the group velocity in a linear, non-dissipative medium, this is also
the ray direction, and hence ray and wavefront angles differ.

(b) For the model of ★1 ($C_{11}=40$, $C_{33}=30$, $C_{44}=9$, $C_{66}=12$,
$C_{13}=15$ GPa, $\rho=2500$ kg m⁻³) at $\theta = 45^\circ$, computed with a
centred difference of the exact Christoffel phase velocities ($h = 10^{-6}$ rad):

| mode | phase $V$ (m s⁻¹) | $\mathbf G$ (m s⁻¹) | $|\mathbf G|$ (m s⁻¹) | group angle | $\Delta\phi$ |
|---|---|---|---|---|---|
| qP | 3701.764480 | $(3011.1490,\ 2223.9366)$ | 3743.382421 | 53.551632° | $+8.551632°$ |
| qSV | 1974.066800 | $(1374.1828,\ 1417.5693)$ | 1974.305175 | 44.109641° | $-0.890359°$ |

Independently verified by differentiating the dispersion relation directly,
$\mathbf G = \partial\omega/\partial\mathbf k$ with $\omega = V(\theta)|\mathbf k|$
and a $k$ step of $10^{-3}$: the components agree to better than
$8.3\times10^{-4}$ m s⁻¹, i.e. to the finite-difference truncation level.

(c) The demo's model (section 7) gives

| mode | $\theta$ | $\Delta\phi$ (deg) |
|---|---|---|
| qP | 30° | $+8.537002$ |
| qP | 45° | $+8.586054$ |
| qP | 60° | $+6.644437$ |
| qSV | 30° | $-1.383079$ |
| qSV | 45° | $+0.361907$ |
| qSV | 60° | $+1.552320$ |

Comparing with the anisotropy magnitudes ($\epsilon = 0.182$,
$\gamma = 0.214$ for the demo model; $\epsilon = \gamma = 0.167$ for ★1): the qP
angular difference is roughly half of $\epsilon$ expressed in degrees — i.e.
several degrees for 15–20 per cent anisotropy, and it grows roughly linearly with
the anisotropy (the ★1 model's slightly smaller $\epsilon$ gives a slightly
smaller shift). The qSV shifts are an order of magnitude smaller and change sign,
as expected from its velocity minimum near 45°. Both are first-order in the
anisotropy, which is the statement that group and phase directions coincide only
in the isotropic limit.

(d) Practical consequences:

1. **Well ties and migrated sections mis-tie** because the migration uses *phase*
   velocities and ray (group) geometry, while the well tie is a vertical
   (phase-along-the-axis) measurement. In an HTI or VTI medium the two are not the
   same quantity, so the mismatch is systematic and grows with offset.
2. **A "ray angle" is not a wavefront angle**: in anisotropic ray tracing one must
   use $\mathbf G$ for the ray and $\mathbf n$ for the phase, and the mapping
   between them (itself derived from the slowness surface) is what makes
   anisotropic ray tracing more involved than "trace the normal".
3. **NMO and moveout velocities are not simply the vertical velocity**: the
   anisotropy parameters enter the moveout at the same order as the velocity, so
   a $\delta$ error of 0.05 produces travel-time errors comparable with a 5 per
   cent velocity error.

*Caveat on magnitude claims.* The numbers given here are for the model
parameters of the demo and ★1; the general statements ("several degrees",
"grows with anisotropy") follow from the first-order structure of
equation (6) and are not claimed as measurements for a specific rock.
