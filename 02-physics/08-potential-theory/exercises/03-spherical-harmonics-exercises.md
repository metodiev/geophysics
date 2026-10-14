# Exercises — 02-08-03 Spherical Harmonics and Multipole Expansions

Attempt these **closed-book** before opening the
[solutions](./03-spherical-harmonics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/spherical_harmonics_demo.py`](../code/spherical_harmonics_demo.py)
require you to run it and report its actual output. Use the conventions of the
lesson: complex $Y_{lm}$ with the Condon–Shortley phase,
$C_{00} = \sqrt{4\pi}$, and $J_l$ defined by
$V = (GM/r)[1 - \sum_{l\ge1}J_l(a/r)^lP_l(\cos\theta)]$ for an axisymmetric body.

---

## ★ Foundational

**★1.** Compute $P_0(x)$ through $P_4(x)$ from the Bonnet recurrence.

(a) Write the four polynomials explicitly.
(b) Evaluate $P_4$ at $x = 1$, $0$ and $-1$ and check against $P_l(\pm1) = (\pm1)^l$.
(c) Evaluate $P_3(0.5)$ and verify it against the Rodrigues formula by direct
differentiation.
(d) Compute $\int_{-1}^{1}P_2(x)P_4(x)\,dx$ and confirm it is zero.

---

**★2.** Using $Y_{00} = 1/\sqrt{4\pi}$,
$Y_{10} = \sqrt{3/4\pi}\cos\theta$ and
$Y_{11} = -\sqrt{3/8\pi}\sin\theta\,e^{i\phi}$:

(a) Evaluate all three at $\theta = \pi/3$, $\phi = \pi/4$, giving complex values.
(b) Compute $\lvert Y_{00}\rvert^2$, $\lvert Y_{10}\rvert^2$ and
$\lvert Y_{11}\rvert^2$ at that point and check that
$\sum_{m=-1}^{1}\lvert Y_{1m}\rvert^2$ is independent of angle.
(c) State the value of that sum and prove it is constant (this is the addition
theorem for $l=1$).
(d) Compute $q_{11}$ for a point mass $M = 1.0\times10^{11}$ kg at
$r' = 500$ m, $\theta' = \pi/4$, $\phi' = 0$.

---

**★3.** Show that a spherically symmetric density leaves only $l=0$.

(a) Write the angular integral that must vanish.
(b) State which property of harmonic functions makes it vanish.
(c) Compute $C_{00}$ for the general spherically symmetric body and show it is
$\sqrt{4\pi}$.
(d) Explain why this is a *statement about symmetry* and not an approximation.

---

**★4.** Two equal masses $m = 5.0\times10^{10}$ kg sit on the $z$ axis at
$z = +d$ and $z = -d$ with $d = 1000$ m (a "dumbbell", total mass $M = 2m$), and
the origin is at the centre.

(a) Compute the $l=0$ coefficient.
(b) Compute $q_{20}$ and hence $J_2$ with the reference radius $a = d$. Report the
sign.
(c) State whether the body is prolate or oblate and check the sign of $J_2$ against
your expectation.
(d) Compute the potential at $(0,0,5000)$ m by the exact sum over the two masses,
and by the monopole plus quadrupole terms, and compare.

---

## ★★ Applied

**★★5.** Run [`../code/spherical_harmonics_demo.py`](../code/spherical_harmonics_demo.py).

(a) Report the worst deviation from orthonormality over $l,l'\le3$ and the pair at
which it occurs.
(b) Report the truncated multipole potential at $L = 0$, $2$ and $8$ and the
relative errors against the direct sum.
(c) Report the dipole magnitude $\lvert q_1\rvert$ for the centred and the shifted
origin.
(d) Report $\lvert C_{l0}/C_{00}\rvert$ for $l = 2$ and $l = 6$ for the uniform
ball.
(e) Report the $J_2$ values from the volume quadrature and from $(2f-f^2)/5$ at
$f = 0.0033528107$, and the ratio of the measured Earth value to the homogeneous
value.

---

**★★6.** Derive the coefficient $C_{00}$ from the definition and confirm it against
the demonstration.

(a) Write $q_{00}$ for a body of total mass $M$.
(b) Apply the normalisation $\int Y_{00}^*dV = 1$ appropriately and derive
$C_{00} = \sqrt{4\pi}$.
(c) Substitute the $l=0$ term back into the expansion and show it is $GM/r$.
(d) Explain why $C_{00}$ is the same for every body.

---

**★★7.** A homogeneous oblate spheroid has flattening $f = 0.001$.

(a) Compute $J_2$ from $(2f-f^2)/5$.
(b) Compute $J_2$ from $C-A$ using $C = \tfrac25Ma^2$ and $A = \tfrac15M(a^2+c^2)$,
and confirm agreement.
(c) For $f = 0.05$, repeat both and state whether the agreement is still exact.
(d) Explain why the spheroidal moments give an exact $J_2$ whereas the
"flattening" alone does not determine $J_2$ for a non-homogeneous body.

---

**★★8.** The Earth's flattening and rotation rate are defining parameters of
WGS 84: $f = 1/298.257\,223\,563$ and $\omega = 7.292\,115\times10^{-5}$ rad s$^{-1}$,
with $a = 6\,378\,137$ m and $GM = 3.986\,004\,418\times10^{14}$ m$^3$ s$^{-2}$.

(a) Compute $q = \omega^2a^3/GM$.
(b) Compute $J_2$ from the hydrostatic relation $J_2 = (2f-q)/3$.
(c) Compute the homogeneous-spheroid $J_2 = (2f-f^2)/5$.
(d) Report the ratio and state in one sentence what it says about the Earth's
interior.

---

## ★★★ Research-oriented

**★★★9.** Derive the addition theorem for $l = 1$ explicitly.

(a) Write $P_1(\cos\gamma) = \cos\gamma$ in terms of the directions
$(\theta,\phi)$ and $(\theta',\phi')$.
(b) Show it equals $\frac{4\pi}{3}\sum_{m=-1}^{1}Y_{1m}(\theta,\phi)
\overline{Y}_{1m}(\theta',\phi')$ using the explicit forms of $Y_{1m}$.
(c) Verify your expression numerically at three pairs of directions, using the
demonstration's $\theta,\phi$ values.
(d) Explain what the theorem buys you: what does it replace, and in which kind of
integral does it appear?

---

**★★★10.** A homogeneous triaxial ellipsoid has semi-axes $a_1 > a_2 > a_3$.

(a) Explain why the $l=1$ coefficients vanish but the $l=2$ coefficients need
$C_{20}$, $C_{21}$ and $C_{22}$ in general.
(b) Show that if the body is symmetric under $x\to-x$ and $y\to-y$ (as an ellipsoid
is), the odd-$m$ and odd-$l$ coefficients vanish.
(c) Write the leading non-zero quadrupole terms in terms of the second moments
$\int x'^2\rho\,dV'$, $\int y'^2\rho\,dV'$, $\int z'^2\rho\,dV'$, and show that only
two of the three combinations are independent (the trace is fixed by the total
mass and the reference radius).
(d) Compute the two independent combinations for a homogeneous ellipsoid with
semi-axes $a,b,c$, and state the value of $C_{22}$ when $a=b$.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
