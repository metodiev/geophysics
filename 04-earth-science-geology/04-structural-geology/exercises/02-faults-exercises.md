# Exercises — 04-04-02 Fault Geometry, Kinematics and Fault Classification

Attempt these **closed-book** before opening the
[solutions](./02-faults-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/02-faults_demo.py`](../code/02-faults_demo.py)
require you to run it and report its actual output.

**Conventions.** Coordinates are (east, north, up). Strike is clockwise from
north; dip is to the right of strike; rake is measured in the fault plane from
the strike direction, positive anticlockwise seen from the hanging wall, so rake
0 is left-lateral, 90 reverse, 180 right-lateral and 270 normal. **State these
conventions in every answer**, because the geometry is convention-independent and
the labels are not.

---

## ★ Foundational

**★1.** A fault strikes 000 and dips 60° to the east.

(a) Write down its upward pole $\mathbf{n}$.
(b) Write down its strike direction $\mathbf{d}$ and up-dip direction
$\mathbf{u}$, and verify that $\mathbf{d}\cdot\mathbf{u} = 0$,
$\mathbf{u}\cdot\mathbf{n} = 0$ and $\mathbf{d}\times\mathbf{u} = \mathbf{n}$.
(c) Write down the slip vector for a rake of 270°.
(d) State the fault type and verify it from the sign of the vertical component of
the slip vector.

---

**★2.** For each slip vector from a fault with $\mathbf{u} =
(-0.5, 0, 0.866)$, $\mathbf{d} = (0, 1, 0)$ and $\mathbf{n} = (0.866, 0, 0.5)$,
compute $s_{ss} = \mathbf{s}\cdot\mathbf{d}$ and
$s_{ds} = \mathbf{s}\cdot\mathbf{u}$, and classify:

(a) $\mathbf{s} = (0.5, 0, -0.866)$;
(b) $\mathbf{s} = (0, 1, 0)$;
(c) $\mathbf{s} = (0.3536, 0.7071, 0.6124)$;
(d) state the threshold convention used and why it must be stated.

---

**★3.** A fault has a net slip of 100 m and dips 60°.

(a) Compute the throw and the heave.
(b) Compute their ratio and compare with $\tan 60^\circ$.
(c) Verify the Pythagorean identity.
(d) State the difference between the throw and the stratigraphic separation.

---

## ★★ Applied

**★★4.** A bed strikes 060 and dips 40°.

(a) Compute the apparent dip in a section with an azimuth of 090°.
(b) Compute it for azimuths of 120° and 150°.
(c) Compute it for an azimuth of 240° and state what the sign means.
(d) State why a section at 45° to strike cannot be corrected by multiplying the
true dip by $\sin 45^\circ$, and give the numerical comparison for a true dip of
40°.

---

**★★5.** Run [`../code/02-faults_demo.py`](../code/02-faults_demo.py).

(a) Report the rake recovered from the slip vector for each of the four cases and
compare with the input.
(b) Report the slip-tendency and Coulomb optima for the normal-faulting regime,
and state the two dips.
(c) Report the closed-form values those optima are compared against and the
differences.
(d) Report the fault type read off for each regime.

---

**★★6.** A stress state at 10 km has $S_v = 264.9$ MPa, pore pressure 100.7 MPa
and a tectonic differential stress of 100 MPa.

(a) Compute the effective vertical and least horizontal effective stresses for the
normal-faulting case, given $\sigma_1$ vertical with $S_v$ and
$\sigma_3 = S_v - \Delta\sigma$.
(b) Compute the slip-tendency optimum dip from
$\tan\alpha = \sqrt{\sigma_1'/\sigma_3'}$.
(c) Compute the Coulomb optimum dip from $45^\circ + \phi/2$ for $\mu = 0.85$.
(d) State which criterion answers "which fault is most likely to move" and which
answers "does this fault fail".

---

## ★★★ Research-oriented

**★★★7.** For a strike-slip regime with $\sigma_1$ horizontal along east,
$\sigma_3$ horizontal along north and $\sigma_2$ vertical,

(a) explain why the optimum faults are vertical;
(b) compute the optimum strike for the Coulomb criterion from
$90^\circ - (45^\circ - \phi/2)$ and state the conjugate;
(c) compute the optimum strike for the slip-tendency criterion from
$\beta = \arctan\sqrt{\sigma_1'/\sigma_3'}$, including the change of reference
direction, and compare with the demo's scanned value;
(d) explain why the two criteria give different strikes for the same stress
state.

---

**★★★8.** A double-couple moment tensor is built from a plane normal
$\mathbf{n}$ and a slip vector $\mathbf{s}$ as
$M = \tfrac12(\mathbf{s}\mathbf{n}^{\mathsf T} +
\mathbf{n}\mathbf{s}^{\mathsf T})$.

(a) Show that the eigenvalues are $+\tfrac12$, 0 and $-\tfrac12$.
(b) Show that $\mathbf{n} + \mathbf{s}$ and $\mathbf{n} - \mathbf{s}$ are
eigenvectors and identify which is the T axis and which the P axis.
(c) Show that $M\mathbf{n}$ is parallel to $\mathbf{s}$ and that
$M\mathbf{s}$ is parallel to $\mathbf{n}$, and state what that means about the
two nodal planes.
(d) Run the demo and report the round trip: the strike, dip and rake of both
nodal planes, and compare with the input. State what a focal mechanism cannot
determine and what resolves it.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
