# Exercises — 02-08-06 Uniqueness Theorems and Boundary Conditions

Attempt these **closed-book** before opening the
[solutions](./06-uniqueness-theorems-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/uniqueness_demo.py`](../code/uniqueness_demo.py)
require you to run it and report its actual output. Use
$G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$.

---

## ★ Foundational

**★1.** State the exterior Dirichlet problem for Laplace's equation, including the
regularity condition.

(a) Write the equation, the domain and the boundary condition.
(b) Write the regularity condition and explain in one sentence what it excludes.
(c) Give two harmonic functions that satisfy the equation in the exterior domain but
violate the regularity condition.
(d) Explain why the problem has infinitely many solutions without (b).

---

**★2.** State the exterior Neumann problem.

(a) Write the boundary condition, defining the direction of the normal.
(b) State the uniqueness result, and explain why the additive constant that is free
in the bounded-domain case is not free here.
(c) Show that the uniqueness proof is the same as for Dirichlet except that the
boundary term vanishes for a different reason.
(d) Explain what a solution's behaviour at infinity has to do with whether an
additive constant is determined.

---

**★3.** Gauss's law in flux form.

(a) Write the flux form of Gauss's law for the gravity field with the convention
$\mathbf{g} = \nabla V$.
(b) Apply it to a sphere of radius $a$ enclosing a mass $M$ and compute the flux
through the sphere with the outward normal pointing *into* the source region.
(c) Relate your answer to the far-field behaviour $V\sim GM/r$.
(d) Explain why this shows that $\oint g\,dS = 0$ is the wrong existence condition
for the exterior Neumann problem.

---

**★4.** Construct a trivial annihilator and a non-trivial equivalence.

(a) Two infinite slabs of density $\rho$ and thickness $t$ and of density $-\rho$
and thickness $-t$ occupy the same space. State their total field and whether they
form an annihilator.
(b) Give two infinite slabs with different densities and thicknesses that produce
the same field.
(c) Write the signed density distribution equal to their difference and state its
field.
(d) State why (c) is an annihilator even though its density is negative somewhere.

---

## ★★ Applied

**★★5.** Run [`../code/uniqueness_demo.py`](../code/uniqueness_demo.py).

(a) Report the maximum difference between the two Dirichlet solutions after $10$,
$100$, $1000$ and $4000$ sweeps.
(b) Report the maximum error of the numerical solution against the exact series
solution.
(c) Report the peak density and the FWHM of the equivalent strata at $h = 500$,
$1000$ and $1500$ m.
(d) Report the worst relative difference between the equivalent-stratum field and
the line-mass field over the stations, and the value at the finest quadrature
refinement.
(e) Report the annihilator's largest field as a fraction of the peak, and its peak
density as a fraction of the signal's peak density.
(f) Report the relative difference between the horizontal derivatives.
(g) Report the four slab results and their relative deviations.

---

**★★6.** The equivalent stratum.

(a) Derive $\sigma_h(x) = (\lambda/\pi)(z_0-h)/(x^2+(z_0-h)^2)$ by the Fourier
argument.
(b) Show that $\int\sigma_h\,dx = \lambda$ for every $h$ and explain why this is
required.
(c) Compute the peak density and the FWHM for $h = 1900$ m with $z_0 = 2000$ m and
$\lambda = 5.0\times10^8$ kg m$^{-1}$.
(d) Comment on the value in (c) and state what it says about how deep a source can
be pushed.

---

**★★7.** Uniqueness is not stability.

(a) Write the upward-continuation operator in the wavenumber domain for
continuation over a height $h$.
(b) Write the downward-continuation operator.
(c) Compute both at $\lvert k\rvert = 10^{-2}$ m$^{-1}$ and
$h = 1000$ m.
(d) State which is bounded and which is not, and explain how a problem can be
unique and still ill-conditioned.

---

**★★8.** Applying the ambiguity.

(a) Explain why the answer to "is the gravity field unique given complete surface
data?" is yes, and the answer to "is the density unique?" is no, without
contradiction.
(b) A colleague reports a density model obtained by inverting a gravity survey. List
the three things you must ask before accepting the *structure* of the model.
(c) Name two kinds of additional measurement that would constrain the solution and
say which part of the ambiguity each addresses.
(d) State whether acquiring gravity gradients, in principle, breaks the ambiguity.

---

## ★★★ Research-oriented

**★★★9.** The equivalent stratum in the wavenumber domain.

(a) Write the wavenumber-domain relation between the measured field and the density
of an equivalent stratum at depth $h$.
(b) Show that the required density spectrum is
$\tilde\sigma(k) = \tilde g(k)/(2\pi G e^{-\lvert k\rvert h})$.
(c) Explain why a solution exists for every $k$ and every $h$ and what that implies
about the dimension of the null space.
(d) Take a Gaussian anomaly of width $w$ and show that the required density
amplitude at large $\lvert k\rvert$ grows as $e^{\lvert k\rvert h}$; estimate the
depth at which the required density exceeds $10^6$ kg m$^{-2}$ for
$\lvert k\rvert = 0.01$ m$^{-1}$ and a field amplitude of $10^{-5}$ m s$^{-2}$.

---

**★★★10.** What additional information chooses a model?

(a) State precisely why a positivity constraint on the density reduces but does not
eliminate the null space.
(b) Construct two non-negative density distributions that produce the same field,
or explain why none exists in the two-dimensional line-mass case and what changes in
three dimensions.
(c) Discuss how a joint inversion with a seismic velocity model reduces the feasible
set, and what assumption about the density–velocity relation it introduces.
(d) State the honest form of a conclusion from a potential-field inversion, in one
paragraph, that a referee would accept.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
