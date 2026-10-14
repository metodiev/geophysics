# Exercises — 02-08-02 Laplace's Equation and Harmonic Functions

Attempt these **closed-book** before opening the
[solutions](./02-laplace-equation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/laplace_harmonic_demo.py`](../code/laplace_harmonic_demo.py)
require you to run it and report its actual output. Use
$G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$.

---

## ★ Foundational

**★1.** Decide whether each function is harmonic, and state where.

(a) $u = x^2 + y^2 - 2z^2$.
(b) $u = x^2 - y^2$.
(c) $u = 1/\sqrt{x^2+y^2+z^2}$ away from the origin.
(d) $u = e^{-(x^2+y^2+z^2)}$.
(e) $u = \ln\sqrt{x^2+y^2}$ away from the $z$ axis.

---

**★2.** Let $f = x^2 + 2y^2$ and $\mathbf{p} = (3, -1, 0)$.

(a) Compute $\nabla^2f$.
(b) Use the mean value expansion
$\overline{f} = f(\mathbf{p}) + \tfrac{R^2}{6}\nabla^2f + O(R^4)$ to predict the
sphere mean about $\mathbf{p}$ at $R = 1$.
(c) Compute the mean exactly by integrating.
(d) Explain why the answer is not $f(\mathbf{p})$.

---

**★3.** For $u = x^2 - y^2$ on the disk $x^2+y^2\le1$:

(a) Show $u$ is harmonic.
(b) Find the maximum and minimum of $u$ over the closed disk and say where they lie.
(c) Verify the mean value property at the centre.
(d) Verify the mean value property at the point $(0.5, 0)$ for $R = 0.4$.

---

**★4.** A gravity survey has a mis-levelled line: every station on one line reads
$0.5$ mGal too high.

(a) State whether the resulting anomaly field is harmonic.
(b) Describe what the finite-difference Laplacian of the grid would look like along
that line.
(c) Explain why the discrete mean value property is used as a quality-control test.

---

## ★★ Applied

**★★5.** Run [`../code/laplace_harmonic_demo.py`](../code/laplace_harmonic_demo.py).

(a) Report the mean-value relative difference for the source-free sphere at
$R = 1000$ m and for the sphere that encloses the source at $R = 200$ m.
(b) Report the interior maximum and the boundary maximum in the maximum-principle
test, and the location of the maximum.
(c) Report the finite-difference Laplacian residuals for the harmonic function at
$h = 100$ and $h = 12.5$ m, and the ratio between them.
(d) Report the Laplacian residual for $f = x^2$ at any $h$.
(e) State, in one sentence each, which property of harmonic functions each of the
four blocks tests.

---

**★★6.** A potential is $\mathbf{g}$-field data with wavenumber spectrum
$\tilde g(k)$. A downward continuation by depth $d$ multiplies the spectrum by
$e^{\lvert k\rvert d}$.

(a) For $d = 1000$ m, compute the amplification at wavelengths $60$ km, $6$ km and
$600$ m (i.e. $k = 2\pi/\lambda$).
(b) If the data contain $1$ per cent noise at all wavelengths, compute the noise
level after continuation at each of the three wavelengths.
(c) State the wavelength at which the amplified noise reaches $100$ per cent, for a
$1$ per cent initial level.
(d) Explain in one paragraph why the problem is still unique even though the answer
is useless.

---

**★★7.** For a point mass at depth $h$,
$g_z(x) = GMh/(x^2+h^2)^{3/2}$.

(a) Derive the peak value and the curvature $d^2g_z/dx^2$ at $x = 0$.
(b) Evaluate both for $M = 1.0\times10^{12}$ kg at $h = 1000$ m, and confirm
against the demonstration's table.
(c) Show that the curvature scales as $h^{-4}$ and state what that implies for the
stability of estimating depth by double differentiation.
(d) Use the mean value property to explain why the *potential* has no such
sharpening.

---

**★★8.** A harmonic function is sampled on a grid with spacing $2$ km, and the
second-difference Laplacian returns residuals of order $5\times10^{-11}$ s$^{-2}$,
while $-4\pi G\rho$ for a crustal density of $2700$ kg m$^{-3}$ is
$2.264\times10^{-6}$ s$^{-2}$.

(a) Compute the ratio of the residual to the crustal Laplacian.
(b) State whether the grid may be treated as harmonic, and with what justification.
(c) The stencil is second order in $h$. What residual would you expect on a grid of
spacing $1$ km if the field were exactly harmonic?
(d) What would it mean if the residual did *not* fall when the grid was refined?

---

## ★★★ Research-oriented

**★★★9.** Prove that a continuous function on a connected open set that satisfies
the mean value property for every sphere is harmonic. Your proof should proceed by
showing that the function cannot have a strict interior maximum or minimum unless
it is constant, and then invoking the standard argument that a function whose
Laplacian were, say, everywhere positive would violate the mean value property on a
sufficiently small sphere.

(a) Write out the proof carefully, stating every assumption.
(b) Explain where connectedness is used and give a counterexample on a
disconnected domain.
(c) Show that on a domain that is a ball with a point removed, a function can be
harmonic and bounded but not constant, and explain why this does not contradict
anything you proved.

---

**★★★10.** The maximum principle applies to every elliptic equation of the form
$\nabla\cdot(k\nabla u) = 0$ with $k > 0$.

(a) State the maximum principle for this equation and prove it using the same
manipulation as Green's first identity.
(b) Apply it to steady heat conduction with temperature-dependent conductivity and
state the physical interpretation.
(c) Apply it to DC resistivity in a medium of variable conductivity and state what
it forbids about the potential field.
(d) Construct a physical situation in which the maximum is attained in the interior
and explain which hypothesis fails.
(e) Explain why the same argument does *not* give a maximum principle for
$\nabla\cdot(k\nabla u) = f$ with $f$ of both signs.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
