# Exercises — 02-04-06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)

Attempt these **closed-book** before opening the
[solutions](./06-anisotropic-elasticity-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/anisotropic_elasticity_demo.py`](../code/anisotropic_elasticity_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** For a VTI medium with $C_{11} = 40$ GPa, $C_{33} = 30$ GPa,
$C_{44} = 9$ GPa, $C_{66} = 12$ GPa, $C_{13} = 15$ GPa and
$\rho = 2500\ \mathrm{kg\,m^{-3}}$:

(a) Compute $C_{12}$ from the hexagonal constraint.
(b) Compute $\epsilon$, $\delta$ and $\gamma$.
(c) Compute $v_p(0)$, $v_{sv}(0)$, $v_p(90^\circ)$ and $v_{sh}(90^\circ)$.
(d) State whether the medium is faster along or across the axis for each mode.

---

**★2.** Show that the SH-wave speed in a VTI medium is exactly
$v_{sh}(\theta) = \sqrt{(C_{66}\sin^2\theta+C_{44}\cos^2\theta)/\rho}$.

(a) Write the Christoffel matrix and identify the decoupled entry.
(b) Show that its eigenvector is $(0,1,0)$ at every $\theta$ and interpret that.
(c) Verify the limits at $\theta = 0$ and $\theta = 90^\circ$.
(d) State why this exactness does not extend to qP or qSV.

---

**★3.** A rock has five independent constants. Count the independent constants for
each symmetry class in the list from lesson 02-04-03 and state one geological
setting that produces each.

(a) Triclinic, monoclinic, orthorhombic.
(b) Tetragonal, hexagonal (VTI/HTI), cubic.
(c) Isotropic.
(d) For each class, state which of them can be produced by layering alone.

---

**★4.** An HTI medium has its symmetry axis along $x$.

(a) Write the expected $6\times6$ matrix pattern (state which entries are equal).
(b) Compute the P speed along $x$, $y$ and $z$ for the constants of ★1.
(c) State which directions give degenerate S waves and why.
(d) Explain why an HTI medium is the model for a set of aligned vertical fractures.

---

## ★★ Applied

**★★5.** Run the demo's VTI section.

(a) Report $\epsilon$, $\delta$ and $\gamma$ and each exact symmetry-direction
speed.
(b) Report the SH errors at all six angles and explain why they are exactly zero.
(c) Report the qP and qSV speeds at 0°, 30°, 45°, 60° and 90°, and describe the
non-monotonic behaviour of qSV.
(d) State which of the three Thomsen parameters controls the qP variation with
angle and which controls the near-vertical behaviour, citing equation (6) of the
lesson.
(e) Run section 5 as well and report the phase–group angle difference $\Delta\phi$
for qP and qSV at 30°, 45° and 60°, plus the reported difference between the two
independent ways of computing the group velocity.

---

**★★6.** Run the demo's rotation section.

(a) Report the rotated matrix and identify its symmetry axis.
(b) Report the symmetry violation after rotation and state what it tests.
(c) Report the P speeds along $x$ and $z$ in the rotated medium and verify them
against $\sqrt{C_{33}/\rho}$ and $\sqrt{C_{11}/\rho}$ of the original.
(d) Explain what would go wrong if the $6\times6$ matrix were rotated componentwise
with a $3\times3$ rotation matrix.

---

**★★7.** A shale has $v_p(0) = 3400$ m s⁻¹, $v_p(90^\circ) = 4100$ m s⁻¹ and
$v_{sh}(90^\circ) = 2400$ m s⁻¹, $v_{sv}(0) = 1900$ m s⁻¹, with
$\rho = 2450\ \mathrm{kg\,m^{-3}}$.

(a) Compute $C_{33}$, $C_{11}$, $C_{66}$ and $C_{44}$.
(b) Compute $\epsilon$ and $\gamma$.
(c) A vertical well is tied to the section using $v_p(0)$. Compute the depth error
at 3 km if the true vertical P velocity is $v_p(0)$ but the section was converted
with the isotropic value $\bar v_p = (v_p(0)+v_p(90^\circ))/2$: report the
percentage and the absolute error.
(d) State which parameter is missing for a full anisotropic depth conversion and
what measurement would supply it.

---

**★★8.** A fractured reservoir is modelled as HTI with $\epsilon = 0.08$,
$\gamma = 0.06$ and $v_p(0) = 4000$ m s⁻¹. The symmetry axis is horizontal and
normal to the fracture planes; take $\rho = 2450\ \mathrm{kg\,m^{-3}}$.

(a) Compute the fast and slow S speeds for propagation along the axis, taking
$v_{sv}(0) = 2300$ m s⁻¹.
(b) Compute the splitting for propagation perpendicular to the axis.
(c) State which S polarisation is fast and what that means for fracture
orientation.
(d) Explain why a shear-wave survey with two orthogonal sources and receivers can
determine the fracture azimuth without any velocity model.

---

## ★★★ Research-oriented

**★★★9.** Backus averaging for a finely layered medium.

(a) Derive (or state with a citation) the Backus expressions for $C_{33}$ and
$C_{44}$ of a two-component layered medium in the long-wavelength limit, and
explain why $C_{33}$ is a harmonic-type average and $C_{44}$ also involves a
harmonic combination.
(b) For alternating layers of 60 per cent shale ($v_p = 3200$, $v_s = 1800$,
$\rho = 2400$) and 40 per cent limestone ($v_p = 6000$, $v_s = 3200$,
$\rho = 2650$), compute the layer moduli and then $C_{33}$, $C_{44}$ and $C_{11}$
using the Backus formulae.
(c) Compute $\epsilon$ and $\gamma$ for the stack and state whether the resulting
anisotropy is large enough to matter for depth conversion.
(d) State the wavelength condition required for the effective-medium description
and what happens to the velocities when it is violated.

---

**★★★10.** Phase versus group velocity in an anisotropic medium.

(a) Show that in an anisotropic medium the ray (group) velocity direction differs
from the wavefront (phase) direction unless the slowness surface is a sphere, and
explain why the group velocity is $\partial\omega/\partial\mathbf k$.
(b) For the VTI model of ★1, compute the group velocity vector at
$\theta = 45^\circ$ for qP and qSV from the numerical derivative of the
phase-velocity surface, and report the angular difference between the phase and
group directions.
(c) Compute the same for the demo's model (constants of section 7) and compare the
two angular differences with the anisotropy magnitudes. Confirm your demo values
against section 5 of the demo's output.
(d) Explain the practical consequences: why do well ties and migrated sections
show mis-ties in anisotropic media, and why is a "ray angle" not the same as the
wavefront angle?

Report measured values only if you verify them numerically, and state which of
your results are analytic.
