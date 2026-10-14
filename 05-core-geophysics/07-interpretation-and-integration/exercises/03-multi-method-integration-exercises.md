# Exercises — 05-07-03 Integrating Multiple Methods and Constraints

Attempt these **closed-book** before opening the
[solutions](./03-multi-method-integration-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/multimethod_demo.py`](../code/multimethod_demo.py) require you to run it
and report its actual output. **No answer may present a single "best" model as
the result of a joint interpretation; the feasible set is the result.**

Constants: $\mu_0 = 4\pi\times10^{-7}$ H m⁻¹. The MT forward recursion used in the
demonstration is

$$Z_{j} = Z_j^{\text{int}}\frac{Z_{j+1} + Z_j^{\text{int}}\tanh(k_j h_j)}
{Z_j^{\text{int}} + Z_{j+1}\tanh(k_j h_j)},\qquad
Z_j^{\text{int}} = \frac{\mathrm{i}\omega\mu_0}{k_j},\qquad
k_j = \sqrt{\frac{\mathrm{i}\omega\mu_0}{\rho_j}}.$$

---

## ★ Foundational

**★1.** A uniform half-space of resistivity $\rho$ has $Z = \mathrm{i}\omega\mu_0/k$
with $k = \sqrt{\mathrm{i}\omega\mu_0/\rho}$.

(a) Show $\rho_a = |Z|^2/(\omega\mu_0) = \rho$.
(b) Explain why this identity is a *validation* of a forward operator and not a
physical result.

---

**★2.** Compute the conductance $S = h/\rho$ for each of:

(a) $h = 50$ m, $\rho = 1$ Ω m;
(b) $h = 100$ m, $\rho = 2$ Ω m;
(c) $h = 500$ m, $\rho = 5$ Ω m;
(d) $h = 1000$ m, $\rho = 20$ Ω m.

State which two are equivalent in the thin-layer regime and which is not, and why.

---

**★3.** State, in one sentence each, the difference between an *ambiguous*
parameter and an *insensitive* one, and give one geophysical example of each from
the lesson.

---

## ★★ Applied

**★★4.** Run [`../code/multimethod_demo.py`](../code/multimethod_demo.py).

(a) Record the number of feasible models, the thickness range and the conductance
range.
(b) Re-run the search with a 3 per cent tolerance and report the new ranges.
(c) Report the ratio of the thickness spread to the conductance spread in both
cases, and state what the data constrain.

---

**★★5.** Using the seismic constraint of the demonstration:

(a) Report the thickness and resistivity ranges before and after.
(b) Compute the factor by which the resistivity range narrows.
(c) Explain, using the notion of transverse sensitivity, why the improvement in
resistivity is so much smaller than the improvement in thickness.

---

**★★6.** For the conflicting seismic pick of 150 m:

(a) Report the minimum achievable MT log-misfit and the ratio to the tolerance.
(b) Recompute the minimum misfit for thicknesses of 200 m and 400 m by re-running
the search restricted to those values.
(c) State the thickness at which the misfit falls inside the tolerance, and what
that tells you about the direction of the disagreement.

---

## ★★★ Research-oriented

**★★★7.** Extend the model family to allow a linear conductivity ramp over a
transition zone of thickness $t$ at the base of the target layer.

(a) Show numerically that a transition of 25 m is indistinguishable from a sharp
boundary at 1 per cent tolerance, and find the thickness at which it becomes
distinguishable.
(b) Discuss whether that bound is adequate for the geological question of whether
the boundary is a fault, an unconformity, or a gradational contact.
(c) State what you would need to measure to set a tighter bound.

---

**★★★8.** Design a resolution study for a target at 800 m depth, chosen from your
own field of interest.

(a) Specify the primary method and its sensitivity kernel.
(b) Identify the null-space direction.
(c) Choose a second method whose sensitivity is transverse to it, and derive or
estimate the reduction in the feasible-set size.
(d) State the assumptions the estimate rests on and the observation that would
falsify it.

---

## Reference list used in this problem set

- [05-07-03 lesson](../03-multi-method-integration.md)
- [05-07-02 Quantitative Interpretation and Depth Estimation](../02-quantitative-interpretation.md)
- [Solutions](./03-multi-method-integration-solutions.md)
