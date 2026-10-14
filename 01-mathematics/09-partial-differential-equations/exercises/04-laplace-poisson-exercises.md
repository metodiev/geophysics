# Exercises — 01-09-04 Laplace and Poisson Equations in Earth Systems

Attempt these **closed-book** before opening the
[solutions](./04-laplace-poisson-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $V$ is **positive** and $\mathbf{g} = \nabla V$, so Poisson's
equation reads $\nabla^2V = -4\pi G\rho$; $\mathbf{g}$ therefore points toward the
mass. Use $G = 6.674\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$ and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$. State the convention you use
whenever a sign is at stake.

---

## ★ Foundational

**★1.** A uniform sphere has radius 1.2 km and density
$3000\ \mathrm{kg\,m^{-3}}$.

(a) Compute its mass.
(b) Compute the exterior potential at $r = 5$ km.
(c) Compute the surface gravity, in SI and in mGal.
(d) State the value of $\nabla^2V$ inside the sphere, outside it, and exactly on
its surface, and explain the last case.

---

**★2.** State the mean value property and verify it for $V = GM/r$ on a sphere of
radius $R$ centred at a point $\mathbf{c}$ with
$\lvert\mathbf{c}\rvert > R$. Explain in one sentence what the property forbids in
a potential-field map.

---

**★3.** For the Dirichlet problem on the unit square with $u(x,1) = \sin\pi x$ and
$u = 0$ on the other three sides, the exact solution is
$u = \sinh(\pi y)\sin(\pi x)/\sinh\pi$.

(a) Compute $u$ at the centre.
(b) The numerical demonstration reports a maximum interior value of
$0.924180$ and a maximum boundary value of $0.961349$. Check consistency of the
centre value with both numbers.
(c) State which value the maximum principle says must be the largest, and whether
the reported numbers obey it.

---

**★4.** Derive the 2-D Green's function $\frac{1}{2\pi}\ln(1/r)$ by solving
$\nabla^2u = \delta$ in plane polar coordinates. State why the additive constant is
irrelevant, and what fails if the 3-D form $1/(4\pi r)$ is used in a 2-D model.

---

## ★★ Applied

**★★5.** Prove uniqueness for the Neumann problem
$u_{xx}+u_{yy} = 0$ in $\Omega$ with $\partial u/\partial n = g$ on
$\partial\Omega$, stating the identity you use and every step. Then state the
compatibility condition the data must satisfy when sources are present inside
$\Omega$, and interpret it physically for gravity.

---

**★★6.** A gravity map shows a clear local maximum 3 km from the nearest boundary
of the survey area.

(a) Give the shortest possible argument that something in the interpretation is
wrong.
(b) List the three explanations that are consistent with the mathematics.
(c) State which of the three you would test first, and how.

---

**★★7.** Two density models of a 30 km-radius ball produce exterior potentials
differing by 1 part in $10^{7}$ at $r = 60$ km.

(a) Using the demonstration's cancellation factor of $4.2\times10^{5}$, estimate
the largest *uncompensated* relative density contrast that such a measurement
cannot detect if the perturbation is spherically symmetric with zero total mass.
(b) State the assumptions of the estimate.
(c) Explain why the answer is not "zero contrast is undetectable at any
precision", and why it is also not "any contrast up to 4 % is undetectable".

---

**★★8.** Show that downward continuation from $z=0$ to $z=-h$ amplifies the
wavenumber-$k$ component by $\mathrm{e}^{kh}$. For a continuation of 1 km, compute
the cutoff wavenumber and wavelength above which a 0.1 % data error is amplified by
more than a factor of 100, and state what this implies for the practical resolution
of a downward-continued gravity map.

---

## ★★★ Research-oriented

**★★★9.** Construct a *non-spherical* zero-total-mass density perturbation inside
a uniform ball, and compute its exterior potential at two or three heights.

(a) Report whether it is a null vector of the exterior-potential map.
(b) Explain the result using the multipole expansion: state which moment vanishes
and which does not.
(c) Report how the relative effect varies with height, and relate the variation to
the order of the surviving multipole.
(d) State clearly what your computation does and does not establish.

---

**★★★10.** Critically evaluate two published-style claims using only the
mathematics of this lesson:

(a) "the anomaly requires a body at 4 km depth";
(b) "the potential-field data rule out a body deeper than 8 km".

For each claim state: which class of equation is involved; which part of the data
would have to be complete and noise-free for the claim to hold; what prior
information the claim is silently using; and how you would rewrite the claim so
that it is consistent with the uniqueness theorems of Section 4 of the lesson.
