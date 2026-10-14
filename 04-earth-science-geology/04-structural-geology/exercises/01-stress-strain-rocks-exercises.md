# Exercises — 04-04-01 Stress, Strain and Brittle vs Ductile Deformation

Attempt these **closed-book** before opening the
[solutions](./01-stress-strain-rocks-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/01-stress_strain_demo.py`](../code/01-stress_strain_demo.py) require you
to run it and report its actual output.

**Parameters.** Use $\mu = 0.85$ (Byerlee, TYPICAL), a pore-fluid factor of 0.38,
$\rho = 2700$ kg m$^{-3}$ and $g = 9.81$ m s$^{-2}$ unless a problem states
otherwise. These are commonly quoted values; a strength profile cites its own.

---

## ★ Foundational

**★1.** A stress state has $\sigma_1 = 100$ MPa and $\sigma_3 = 40$ MPa with zero
pore pressure.

(a) Compute the centre and the radius of the Mohr circle.
(b) Compute $\sigma_n$ and $\tau$ on a plane at $\theta = 45^\circ$ from the
$\sigma_3$ axis.
(c) State the maximum shear stress available.
(d) State whether that plane is the plane of failure when $\mu = 0.85$, and why.

---

**★2.** For $\mu = 0.85$,

(a) compute the angle of internal friction $\phi = \arctan\mu$;
(b) compute the optimum failure angle $\theta = 45^\circ + \phi/2$;
(c) compute the acute angle between the two conjugate failure planes;
(d) state how many conjugate sets are equally favoured and what that predicts in
the field.

---

**★3.** At a depth of 5 km with $\rho = 2700$ kg m$^{-3}$ and a pore-fluid factor
of 0.38,

(a) compute the lithostatic vertical stress in MPa;
(b) compute the pore pressure;
(c) compute the vertical effective stress;
(d) state which of the three controls failure.

---

## ★★ Applied

**★★4.** The closed form for the differential stress at frictional failure on the
optimum plane is
$\Delta\sigma = 2(\mu\sigma_3' + C)/[\sqrt{1 + \mu^2} - \mu]$.

(a) Evaluate it for $\mu = 0.85$, $\sigma_3' = 100$ MPa, $C = 0$.
(b) Verify your answer by maximising the Coulomb function numerically over
$\theta$.
(c) Evaluate it for $\mu = 0.6$ and state how the strength changes.
(d) State why cohesion may be neglected for a reactivated fault and not for
intact rock.

---

**★★5.** In normal faulting the largest principal stress is vertical, so
$\sigma_3' = S_v' - \Delta\sigma$; in reverse faulting the least principal stress
is vertical, so $\sigma_3' = S_v'$.

(a) Derive $\Delta\sigma_{\text{normal}} = 2\mu S_v'/[\sqrt{1 + \mu^2} + \mu]$.
(b) Compute both strengths at 10 km with $S_v' = 164.2$ MPa.
(c) Compute the ratio and show that it depends only on $\mu$.
(d) State why strike-slip faulting is absent from this comparison.

---

**★★6.** Run [`../code/01-stress_strain_demo.py`](../code/01-stress_strain_demo.py).

(a) Report the located failure angle and the analytic value, and the difference
between them.
(b) Report the closed-form and searched failure stresses for $\sigma_3' = 200$ MPa
and the difference.
(c) Report the creep strength at 15 km and at 20 km.
(d) Report the ratio of the normal to the reverse frictional strength.

---

## ★★★ Research-oriented

**★★★7.** The brittle–ductile transition is located by finding where the
frictional and creep strength curves cross.

(a) Run the demo and report the transition depth and the two strengths there.
(b) Report how the depth changes when the geotherm is changed from 20 to
30 °C km$^{-1}$, and explain the sign.
(c) Report how it changes when the strain rate is changed from $10^{-16}$ to
$10^{-14}$ s$^{-1}$, and explain the sign using $\sigma \propto
\dot\varepsilon^{1/n}$.
(d) Report how it changes when $Q$ is changed from 200 to 250 kJ mol$^{-1}$, and
explain why the sensitivity to $Q$ is larger than the sensitivity to strain rate.
(e) State one structural feature that this single-flow-law model cannot
reproduce, and what would be required to reproduce it.

---

**★★★8.** The deformation gradient for plane simple shear is
$F = \begin{pmatrix}1 & \gamma\\0&1\end{pmatrix}$.

(a) Show that $\det F = 1$ and state the physical meaning.
(b) Compute the principal stretches for $\gamma = 2$ and verify them against
$\sqrt{(3 \pm \sqrt5)/2}$ scaled appropriately, or by direct eigen-decomposition.
(c) Compute the rotation of a marker line initially perpendicular to the shear
plane, and compare with $\arctan\gamma$.
(d) Explain why a rotation of a marker is evidence of a non-coaxial deformation
path, while a strain measurement alone is not.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
