# Exercises — 02-04-05 Elastodynamic Equation of Motion and Wave Speeds

Attempt these **closed-book** before opening the
[solutions](./05-elastodynamics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

This is the mastery-checkpoint lesson of the physics folder. Problems ★6, ★7 and
★★★9 are the ones to do with no notes and no computer beyond arithmetic. Problems
referring to [`../code/elastodynamics_demo.py`](../code/elastodynamics_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** Derive $v_p = \sqrt{(\lambda+2\mu)/\rho}$ and $v_s = \sqrt{\mu/\rho}$ from
the three ingredients of §2 of the lesson, showing every step.

(a) Write the three ingredients.
(b) Eliminate the stress to obtain the Navier–Cauchy equation.
(c) Use the Helmholtz decomposition to separate the two modes.
(d) Verify both speeds by direct plane-wave substitution.

---

**★2.** For a material with $\lambda = 20$ GPa, $\mu = 22$ GPa and
$\rho = 2500\ \mathrm{kg\,m^{-3}}$:

(a) Compute $v_p$, $v_s$ and the ratio.
(b) Compute $M$, $K$ and $\nu$.
(c) Compute the ratio from $K/\mu+4/3$ and from $2(1-\nu)/(1-2\nu)$ and verify
agreement.
(d) State whether this is a plausible crustal rock and why.

---

**★3.** A grout is injected with $K = 4$ GPa, $\rho = 1400\
\mathrm{kg\,m^{-3}}$ and $\mu = 1.5$ GPa.

(a) Compute $v_p$ and $v_s$.
(b) Compute the ratio and compare with the two bounds of §4.1.
(c) Compute the angle of the P-wave polarisation with respect to the propagation
direction for a plane wave. Explain your answer.
(d) Explain what happens to both speeds if the material sets and $\mu$ rises to
6 GPa while $K$ and $\rho$ are unchanged.

---

**★4.** Prove that a fluid transmits no shear wave, stating precisely which term
of the constitutive law is responsible.

(a) Write the constitutive law with $\mu = 0$ and interpret it.
(b) Show that the shear wave equation degenerates and say what the failure is
physically.
(c) Compute $v_p$ for water ($K = 2.2$ GPa, $\rho = 1000\ \mathrm{kg\,m^{-3}}$).
(d) State what an observed $v_s$ of 100 m s⁻¹ in a "water-filled" rock implies
about the rock.

---

## ★★ Applied

**★★5.** Run the demo's speed section and use its numbers.

(a) Report $v_p$, $v_s$ and the ratio for the granite-like model.
(b) Report the Poisson-solid values and verify $\sqrt3$.
(c) Report the water values.
(d) Explain why the same formula gives 1483 m s⁻¹ for water and 5611 m s⁻¹ for
granite, identifying which parameter is responsible.

---

**★★6.** **Mastery problem (do this with no notes).** State the formulas for
$v_p$ and $v_s$ and then answer:

(a) Which modulus does each speed measure?
(b) Why does $v_p > v_s$ always? Give both the physical argument and the algebra.
(c) A rock has $v_p = 4000$ m s⁻¹ and $v_s = 2000$ m s⁻¹. Compute $\mu/\rho$,
$K/\mu$ and $\nu$, and state whether it is plausible.
(d) A rock has $v_p = 4000$ m s⁻¹ and $v_s = 3900$ m s⁻¹. Compute the implied
$\nu$ and state whether it can be a stable elastic solid, with a reason.

---

**★★7.** **Mastery problem.** Partial fluid saturation.

(a) State which of $\lambda$, $\mu$, $\rho$ change when the pore fluid is
replaced, and which does not.
(b) Deduce the direction of the change in $v_s$ and justify it in one sentence.
(c) For a sandstone with $v_s = 2000$ m s⁻¹ and $\rho = 2150\
\mathrm{kg\,m^{-3}}$ dry, compute $v_s$ when the pores are filled with water,
taking $\phi = 0.25$ and $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$.
(d) Explain why the corresponding statement for $v_p$ requires a model, and name
the two models that bracket the possibilities.

---

**★★8.** Run the demo's plane-wave and divergence sections.

(a) Report the residuals for the P and S plane waves.
(b) Report the divergence and curl magnitudes for the P, S and mixed fields, and
interpret each.
(c) Explain why the mixed field has both, and state what that implies for a real
seismic wavefield.
(d) State what the residual magnitude demonstrates about the derivation, and what
it does not demonstrate.

---

## ★★★ Research-oriented

**★★★9.** **Mastery problem.** A two-layer Earth model has a solid crust
($v_p = 6000$, $v_s = 3500$ m s⁻¹) over a liquid layer with $\mu = 0$.

(a) Write the slowness condition and determine the critical angle for P waves at
the interface, treating the liquid as having $v_p = 8000$ m s⁻¹.
(b) Explain what happens to a downgoing S wave at the interface, naming every
transmitted and reflected wave that can exist.
(c) Explain, in terms of the derived formulas, why an S wave that reaches the
liquid can still generate a P wave in it, and why no S wave appears beyond the
interface.
(d) Explain how the observed absence of S arrivals beyond 103° from an earthquake
is used to determine the radius of the outer core, and what additional data are
required (state your sources honestly for any numerical value you quote).

---

**★★★10.** Stress-induced anisotropy.

(a) Starting from the elastodynamic equation with a static pre-stress, state the
form of the effective stiffness that appears (a derivation is not required; state
the result and cite a source).
(b) Explain why a uniaxial pre-stress makes an otherwise isotropic rock
transversely isotropic to first order, and identify the symmetry axis.
(c) Estimate the size of the effect for a deviatoric stress of 10 MPa in a rock
with $\mu = 30$ GPa, expressing it as a fractional change in $v_s$ (an
order-of-magnitude answer with a stated argument is sufficient).
(d) State two observations that would distinguish stress-induced anisotropy from
intrinsic (lattice- or crack-preferred) anisotropy.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
