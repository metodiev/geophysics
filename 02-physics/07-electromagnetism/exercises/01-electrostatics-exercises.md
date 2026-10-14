# Exercises — 02-07-01 Electrostatics, Coulomb's Law and Electric Potential

Attempt these **closed-book** before opening the
[solutions](./01-electrostatics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/electrostatics_demo.py`](../code/electrostatics_demo.py) require you to
run it and report its actual output. State the unit system in every answer; SI
throughout unless a question says otherwise.

---

## ★ Foundational

**★1.** A charge $q_1 = +3$ nC sits at the origin and a charge $q_2 = -2$ nC sits
at $x = 0.04$ m.

(a) Compute $\mathbf E$ and $V$ at the point $(0, 0.03, 0)$ m.
(b) Find the point on the $x$-axis where $\mathbf E = \mathbf 0$. Explain why
there is exactly one such point (apart from $|x|\to\infty$) and why it is *not*
between the charges.
(c) Compute the potential at that null point.
(d) Compute the work required to move a $+1$ nC test charge from $x = 0.06$ m to
$x = 0.10$ m along the axis.

---

**★2.** A total charge $Q = 1$ nC is spread uniformly over a spherical shell of
radius $a = 0.5$ m.

(a) Give the field inside, at, and outside the shell, from Gauss's law.
(b) Evaluate the field at $r = 0.5$ m and at $r = 1$ m, and compare the first with
the field of a point charge $Q$ at the same distance. Explain the factor.
(c) Repeat for an infinite line of charge with linear density
$\lambda = 2$ nC/m, evaluating the field at $s = 0.05$ m, and state the
assumption you made.
(d) State which of (a) and (c) is used as a model in borehole geophysics, and why
the other one fails there.

---

**★3.** A point charge $q = +2$ nC is held at height $d = 0.01$ m above an
infinite grounded conducting plane.

(a) Write the image-charge configuration and verify that $V = 0$ everywhere on the
plane.
(b) Compute the force on the real charge.
(c) Explain in one sentence why there is no gravitational analogue of this
construction.
(d) Explain why the method works only if the plane is a conductor, and what the
answer would be if the plane were dry resistive rock.

---

**★4.** Use the point-charge potential $V = q/(4\pi\varepsilon_0 r)$.

(a) Show analytically that $\nabla^2V = 0$ for $r > 0$ by computing
$\frac1{r^2}\frac{\mathrm d}{\mathrm dr}\left(r^2\frac{\mathrm dV}{\mathrm dr}\right)$.
(b) State the *mean-value property* for harmonic functions and verify it
numerically for a sphere of radius $R = 0.05$ m whose centre is 0.1 m from a
$+1$ nC charge. Quote your numerical ratio of mean to centre value.
(c) Explain why the numerical Laplacian of a sampled point-charge potential is
*not* zero and yet does not contradict (a).

---

## ★★ Applied

**★5.** A finite line of charge of half-length $L$ and linear density $\lambda$
has perpendicular field at distance $s$ from its midpoint

$$E = \frac{\lambda L}{2\pi\varepsilon_0\,s\sqrt{s^2+L^2}} ,$$

which reduces to the infinite-line result $\lambda/(2\pi\varepsilon_0s)$ as
$L\to\infty$.

(a) Verify that the bracket tends to the infinite-line value as $L\to\infty$ and
evaluate the shortfall at $L = s$ and $L = 10s$.
(b) A borehole electrode is 1 m long and the rock is sampled at 0.5 m from its
midpoint. Compute the correction factor and state whether the infinite-line model
is adequate.
(c) The demonstration reports 0.7071 and 0.9950 for $L/s = 1$ and 10. Reconcile
these with your answer to (a).
(d) State the general criterion $L/s \gg ?$ you would apply before using any
2-D line-charge model.

---

**★6.** Two charges $+1$ nC and $-1$ nC are separated by $2d = 0.02$ m.

(a) Compute the dipole moment magnitude in SI units.
(b) Show from the exact two-charge potential that at large $r$ along the
perpendicular bisector the potential falls as $1/r^2$ and the field as $1/r^3$,
and give the field formula.
(c) Evaluate the field at $r = 0.1$ m and $r = 2$ m perpendicular to the axis and
compare with the exact numeric result reported by the demo (0.9852 and 1.0000
ratios of exact to dipole).
(d) Explain why the *perpendicular* field and the *axial* field of a dipole differ
in magnitude, giving the ratio.

---

**★7.** A ring of radius $a = 0.1$ m carries a total charge $Q = 1$ nC uniformly.

(a) Derive the on-axis potential $V(z)$ and field $E_z(z)$ by integration.
(b) Evaluate both at $z = a$.
(c) Obtain the small-$z$ and large-$z$ limits and interpret them physically.
(d) Show that no closed-form expression exists for the *off-axis* field, and state
what one must do instead — noting that the demo does exactly this for the magnetic
analogue.

---

**★8.** Work with the numerical facts the demo establishes: the coupling ratio
$(1/4\pi\varepsilon_0)/G = 1.346\,591\times10^{20}$ and the field required to
support a body of unit charge-to-mass ratio against gravity, $9.806\,65$ V/m.

(a) Reproduce both numbers from first principles, using
$G = 6.674\,30\times10^{-11}$ m³ kg⁻¹ s⁻² and the standard gravity
$g_n = 9.806\,65$ m/s².
(b) Show that the ratio in (a) is dimensionally *not* a pure number and state its
dimensions.
(c) Explain, with the image-charge result of ★3 as your example, in what sense
electrostatics *can* be screened and gravity cannot.
(d) State the observation that would be needed to falsify "gravity cannot be
screened", and explain why no such observation exists to date.

---

## ★★★ Research-oriented

**★9.** Multipole expansion.

(a) For four charges $+q$ at $(\pm d, 0)$ and $-q$ at $(0, \pm d)$, with
$q = 1$ nC and $d = 1$ mm, show that the total charge and the dipole moment both
vanish.
(b) Define the quadrupole moment tensor
$D_{ij} = \sum_k q_k(3x_ix_j - r^2\delta_{ij})$, compute $D_{xx}$ for this
configuration, and derive the far-field potential on the $x$-axis.
(c) Verify your formula numerically: the exact four-charge potential times $r^3$
should approach $2.696\,3\times10^{-5}$ V m³. Explain the sign and the units.
(d) Gravity has (to observational accuracy) no negative mass, so the Earth's
external field is monopole-dominated. Magnetism has no monopole. Explain how the
"lowest surviving multipole" changes the *inversion* problem in each case, and
why gravity anomalies are reported as a fractional change of $g$ while magnetic
anomalies are reported in nanotesla against a background of tens of thousands.

---

**★10.** Screening, and why electrostatics is useless in the Earth.

(a) For rock with $\varepsilon_r = 6$ and $\sigma = 0.01$ S/m, compute the
dielectric relaxation time $\tau_e = \varepsilon/\sigma$ and state what it means
for a free charge placed in the rock.
(b) Explain why $\rho = 0$ in the bulk of a conductor, and why the *steady*
current field nevertheless obeys Laplace's equation.
(c) A self-potential anomaly of a few tens of millivolts is observed over a
mineralised zone. Explain why this is not an electrostatic measurement in the
sense of this lesson, and what class of source it must be.
(d) Explain in one paragraph why the "electric charge at depth" thought experiment
fails while the "density anomaly at depth" thought experiment succeeds, relating
your answer to the two charges in ★1 and the single-sign mass in the gravity
analogy.
