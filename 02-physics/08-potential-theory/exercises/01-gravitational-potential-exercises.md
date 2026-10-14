# Exercises — 02-08-01 Newtonian Gravitational Potential and Field

Attempt these **closed-book** before opening the
[solutions](./01-gravitational-potential-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/newtonian_potential_demo.py`](../code/newtonian_potential_demo.py)
require you to run it and report its actual output. Use
$G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$ and the convention
$V > 0$, $\mathbf{g} = \nabla V$, $\nabla^2V = -4\pi G\rho$, and state it in
your answers. Report anomalies in mGal as well as m s$^{-2}$.

---

## ★ Foundational

**★1.** A point mass $M = 1.0\times10^{12}$ kg sits at the origin.

(a) Compute $V$ at $r = 1000$ m.
(b) Compute $\lvert\mathbf{g}\rvert$ at the same point.
(c) Verify $g = -dV/dr$ at that point analytically, and say what the minus sign
means given that $V > 0$.
(d) Find the radius at which $V = 1$ m$^2$ s$^{-2}$.

---

**★2.** A thin spherical shell has radius $a = 1000$ m and total mass
$M = 1.0\times10^{13}$ kg.

(a) Compute the field magnitude at $r = 2000$ m.
(b) Compute the field magnitude at $r = 500$ m.
(c) Compute the potential at $r = 500$ m and at $r = 2000$ m.
(d) State the three parts of Newton's shell theorem and say which part each of
(a)–(c) tests.

---

**★3.** A uniform sphere has the Earth's nominal mean radius and density,
$R = 6.371\times10^6$ m and $\rho = 5514$ kg m$^{-3}$ (both nominal).

(a) Compute $g$ at $r = 0.25R$, $0.5R$, $0.75R$ and $R$ using the interior
formula.
(b) Compute $g$ just outside the surface using $GM/r^2$ and confirm continuity.
(c) Sketch $g(r)$ from $r=0$ to $r=3R$ and identify where it is maximal.
(d) State which of the two branches of the formula you used at each point and why.

---

**★4.** A point mass $M = 1.5708\times10^{12}$ kg is at depth $h = 1500$ m below a
horizontal survey plane.

(a) Write the vertical component $g_z(x)$ and compute it at $x = 0$, $750$ and
$1500$ m.
(b) Compute the half-width at half maximum and compare with the value at $x = 750$ m.
(c) A sphere of radius $500$ m has the same mass and its top is at depth $1000$ m.
Where is its centre, and does it produce the same surface profile as the point mass?
Justify with one sentence.
(d) Compute the peak value of the *wrong* profile obtained by putting the top depth
$1000$ m into the point-mass formula, and report the ratio to your answer in (a).

---

## ★★ Applied

**★★5.** Run [`../code/newtonian_potential_demo.py`](../code/newtonian_potential_demo.py).

(a) Report the worst relative error of $\lvert\mathbf{g}\rvert$ against $GM/r^2$ in
the exterior shell test, and the quadrature resolution at which it occurs.
(b) Report the worst interior field value as a fraction of $GM/a^2$, and the
observation point at which it occurs.
(c) Report the worst relative error of the interior profile against
$\tfrac43\pi G\rho r$, and the number of shells used.
(d) Report the cylinder's measured $x_{1/2}/h$ and the finite-line deviation at
$L = 5h$ and $L = 500h$.
(e) State which of (a)–(d) is limited by physics and which by numerics.

---

**★★6.** Two point masses are buried under a horizontal plane: $M_1 = 2.0\times10^{12}$
kg at horizontal offset $(0,0)$ and depth $800$ m, and $M_2 = 1.0\times10^{12}$ kg
at horizontal offset $(1500, 0)$ m and depth $2000$ m.

(a) Compute the vertical field at a station at the origin $(0,0,0)$.
(b) Compute it at $(1500,0,0)$, directly above the second mass.
(c) Report both in mGal.
(d) State which body dominates the anomaly at each station and why, in terms of the
depth dependence of the peak.

---

**★★7.** A gravity profile across a buried horizontal cylinder is
$g_z(0) = 3.6694\times10^{-5}$ m s$^{-2}$ with a half-width at half maximum of
$2000$ m.

(a) Determine the depth to the cylinder axis.
(b) Determine the mass per unit length $\lambda$.
(c) If the cylinder has a radius of $250$ m, what density does that imply?
(d) The profile is measured across a body you know to be only $2000$ m long. State
whether (a) and (b) are still valid, and quantify the error from the
demonstration's finite-line table.

---

**★★8.** Unit and dimensional questions.

(a) Express $3.6694\times10^{-5}$ m s$^{-2}$ in mGal.
(b) Express $0.01$ mGal in m s$^{-2}$.
(c) Show dimensionally that $2G\lambda h/(x^2+h^2)$ has the units of an
acceleration.
(d) Show dimensionally that $\nabla^2V = -4\pi G\rho$ is homogeneous.
(e) An instrument resolves a vertical gravity gradient of $1$ Eötvös. What
fractional change in $g$ does that represent over $1$ m, and is the corresponding
change in a $100$ mGal anomaly detectable?

---

## ★★★ Research-oriented

**★★★9.** A sphere has a density profile $\rho(r) = \rho_0(1 - r/R)$ for
$0\le r\le R$, with $\rho_0 = 5514$ kg m$^{-3}$ and $R = 6.371\times10^6$ m.

(a) Compute the enclosed mass $M(r)$ and the total mass $M$.
(b) Compute $g(r)$ inside the sphere and show it is no longer linear in $r$.
(c) Find the radius at which $g$ is maximal, and compare with the uniform-sphere
case. Explain physically why the maximum moves inward.
(d) Compute $g_{\max}$ and $g(R)$ and report the ratio.
(e) State which observable would distinguish this profile from a uniform sphere of
the same total mass, and whether surface gravity alone could do it.

---

**★★★10.** The shell theorem's null experiment.

(a) A spherical shell of radius $1000$ m and mass $1.0\times10^{13}$ kg encloses a
gravimeter. Compute the field the shell produces at the instrument, and then
compute the field of the same mass if it were concentrated at $100$ m from the
instrument.
(b) State the ratio, and what it says about the sensitivity required to detect a
shell from inside.
(c) A cave of radius $10$ m and air density $1.2$ kg m$^{-3}$ sits $50$ m below a
survey plane in rock of density $2650$ kg m$^{-3}$. Estimate the anomaly directly
above it by treating it as a sphere of negative density contrast, and report the
result in mGal.
(d) State two reasons your estimate in (c) is approximate, and say whether each
makes it an over- or under-estimate.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
