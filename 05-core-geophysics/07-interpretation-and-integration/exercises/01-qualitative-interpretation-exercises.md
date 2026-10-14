# Exercises — 05-07-01 Qualitative Interpretation: Anomaly Shape and Position Rules

Attempt these **closed-book** before opening the
[solutions](./01-qualitative-interpretation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/qual_interp_demo.py`](../code/qual_interp_demo.py) require you to run it
and report its actual output. **Every depth must name the shape constant it uses,
and no answer may quote a "typical" instrument specification as a fact.**

Constants: $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻²;
$1\ \mathrm{mGal} = 10^{-5}$ m s⁻².

---

## ★ Foundational

**★1.** A magnetic anomaly falls to half its peak value 250 m from the peak.

(a) Give the depth under a compact-body (point-mass) model.
(b) Give the depth under a 2-D (line-mass) model.
(c) State, in one sentence, which assumption each answer rests on.

---

**★2.** Derive the peak vertical gravity of an infinite horizontal line mass of
mass per unit length $\lambda$ at depth $z$ from the expression
$g_z(x) = 2G\lambda z/(x^2+z^2)$.

(a) Show the peak is $2G\lambda/z$.
(b) Evaluate it for $\lambda = 10^{9}$ kg m⁻¹ at $z = 500$ m, in mGal.
(c) Explain why the answer is independent of the density contrast.

---

**★3.** State the far-field log–log slope of the vertical field for:

(a) a point mass;
(b) a line mass;
(c) a semi-infinite slab of finite thickness, observed over the slab interior.

Explain the slab answer in one sentence.

---

## ★★ Applied

**★★4.** A profile over an isolated anomaly has $w(1/2) = 383$ m and
$w(1/4) = 617$ m, each measured with a 20 m uncertainty on the width.

(a) Compute $w(1/4)/w(1/2)$.
(b) Compare it with the point-mass value and the line-mass value.
(c) State what the profile does and does not determine, and identify the smallest
width uncertainty at which the shape would no longer be distinguishable.

---

**★★5.** Run [`../code/qual_interp_demo.py`](../code/qual_interp_demo.py).

(a) Record the edge/interior ratio for interior offsets 100 m and 1000 m for the
slab between 50 and 100 m depth.
(b) Find the offset at which the rule is in error by 5 per cent.
(c) State the general form of the condition for the rule to hold.

---

**★★6.** For a *thin* slab of thickness $t$ at depth $z$ and density contrast
$\Delta\rho$, the horizontal gradient is

$$\frac{\partial g_z}{\partial x} = 2G\Delta\rho\,t\,\frac{z}{x^2+z^2}.$$

(a) Show that the half-width of the gradient profile equals the slab depth $z$.
(b) State the quantity this estimator actually measures for a slab of finite
thickness, and why the label matters.

---

## ★★★ Research-oriented

**★★★7.** The demonstration reports the discrete-sum error decreasing by a factor
of 2.00 per halving of the cell size.

(a) State the convergence order this implies.
(b) Determine, by experiment, whether changing the cell shape (rectangles wider
than they are tall) changes the order.
(c) Propose one modification that would give second order, implement it, and
report the measured order.

---

**★★★8.** Construct a profile that is the sum of a compact body of
$1.2\times10^{10}$ kg at 300 m and a second compact body of $2.4\times10^{10}$ kg
at 1500 m, both on the same axis.

(a) Apply the half-width rule to the summed profile and report the depth.
(b) Compute the depth error relative to the shallower body.
(c) Report the mass ratio at which the shallower body's presence changes the
half-width by less than the reading precision, for a half-width read to 2 per
cent.

Connect your answer to the equivalent-stratum argument of
[`../../../02-physics/08-potential-theory/06-uniqueness-theorems.md`](../../../02-physics/08-potential-theory/06-uniqueness-theorems.md).

---

## Reference list used in this problem set

- [05-07-01 lesson](../01-qualitative-interpretation.md)
- [05-07-02 Quantitative Interpretation and Depth Estimation](../02-quantitative-interpretation.md)
- [Solutions](./01-qualitative-interpretation-solutions.md)
