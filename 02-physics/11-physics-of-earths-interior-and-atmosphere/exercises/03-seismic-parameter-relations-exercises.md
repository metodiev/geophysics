# Exercises — 02-11-03 Seismic Velocities, Elastic Moduli and Mineralogy

Attempt these **closed-book** before opening the
[solutions](./03-seismic-parameter-relations-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/velocity_moduli_demo.py`](../code/velocity_moduli_demo.py) require you
to run it and report its actual output.

**Every problem that asks for a modulus or a density requires you to state
whether the density came from a measurement, a reference model, or an
assumption.** Every density and velocity used here is a **nominal** handbook
characteristic unless stated otherwise.

---

## ★ Foundational

**★1.** Given $\rho = 2900$ kg m⁻³, $v_p = 6.5$ km/s and $v_s = 3.7$ km/s:

(a) Compute $\mu = \rho v_s^2$ and $K = \rho\left(v_p^2-\tfrac43v_s^2\right)$.
(b) Compute $\phi = v_p^2-\tfrac43v_s^2$, and verify $K = \rho\phi$.
(c) Compute Poisson's ratio from
$\nu = (v_p^2-2v_s^2)/[2(v_p^2-v_s^2)]$.
(d) Compute $K/\mu$ two ways and report the agreement.

---

**★2.** Derive the identity
$$\frac{K}{\mu} = \left(\frac{v_p}{v_s}\right)^2 - \frac{4}{3}.$$

(a) Show the derivation from $v_p^2 = (K+\tfrac43\mu)/\rho$ and
$v_s^2 = \mu/\rho$.
(b) For $v_p/v_s = 1.86$, compute $K/\mu$ and then $\nu$ from
$\nu = (\tfrac32K/\mu-1)/(3K/\mu+1)$.
(c) Verify your $\nu$ against $\nu = (v_p^2-2v_s^2)/[2(v_p^2-v_s^2)]$.
(d) A colleague reports "this rock has $K/\mu = 3.2$, so $v_p/v_s = 3.2$."
Identify the error.

---

**★3.** Impedance and reflection. A hypothetical boundary separates
$\rho_1 = 4400$ kg m⁻³, $v_{p1} = 10.3$ km/s from
$\rho_2 = 4600$ kg m⁻³, $v_{p2} = 10.9$ km/s (both nominal).

(a) Compute $Z = \rho v_p$ on each side, being explicit about units.
(b) Compute the normal-incidence amplitude reflection coefficient $R$.
(c) Compute the fraction of *energy* reflected, and state the relation to $R$.
(d) State the two directions in which $R$ would change if instead $v_{p2}$ were
*lower* than $v_{p1}$ at the same density step.

---

**★4.** Limits.

(a) State the values of $v_p/v_s$, $\nu$ and $K/\mu$ for a Poisson solid.
(b) Compute $K/\mu$ and $\nu$ for $v_p/v_s = 1.8$.
(c) Compute $K/\mu$ and $\nu$ for $v_p/v_s\to\infty$ and explain what physical
situation that limit describes.
(d) The inner core has $v_p/v_s \approx 3.1$. Compute $K/\mu$ and comment on
whether that is a large or a small value relative to the mantle.

---

## ★★ Applied

**★★5.** The density–velocity degeneracy. Take $v_p = 8.0$ km/s and
$v_s = 4.5$ km/s fixed.

(a) Compute $\phi$.
(b) For $\rho = 3000$, 5000 and 8000 kg m⁻³, compute $\mu$, $K$ and $\nu$.
(c) State which quantities are independent of $\rho$ and which scale with it.
(d) A seismic model reports a layer with $v_p = 8.0$ and $v_s = 4.5$ km/s.
Explain why the seismologist cannot tell whether it is crustal rock or a much
denser material, and name three measurements that would resolve it.

---

**★★6.** Birch's law. The lesson fits
$v_p = -0.6258 + 2.5576\rho$ (km/s, $\rho$ in g cm⁻³) to four silicate anchors.

(a) Reproduce the prediction and residual at $\rho = 3300$ kg m⁻³ and at
$\rho = 4000$ kg m⁻³, and compare with the demo's table.
(b) Compute the prediction at the transition-zone base density,
$\rho = 4400$ kg m⁻³, and compare with the handbook value $v_p = 10.3$ km/s.
(c) Compute the prediction at $\rho = 11\,050$ kg m⁻³ (the outer core) and state
what the size of the misfit measures physically.
(d) State the assumption under which Birch's law is a correlation, and identify
the boundary at which it is violated.

---

**★★7.** Applying the inversion to the outer core.

(a) Given $\rho = 9900$ kg m⁻³, $v_p = 8.0$ km/s and $v_s = 0$, compute $K$,
$\mu$ and $\phi$.
(b) Compute $\phi$ for the mantle immediately above, with $\rho = 5570$ kg m⁻³,
$v_p = 13.7$ km/s, $v_s = 7.3$ km/s.
(c) Report the ratio of the two $\phi$ values and the ratio of the two $K$
values.
(d) Explain why $K$ barely changes across the boundary while $\phi$ drops by a
factor of 1.8.

---

**★★8.** Impedance contrasts across the real boundaries, using the rounded
handbook values on both sides.

(a) Compute $R$ at the Moho ($\rho$ 2900 → 3300 kg m⁻³, $v_p$ 6.5 → 8.1 km/s) and
at the 410 km discontinuity ($\rho$ 3600 → 3600, $v_p$ 8.1 → 9.1 km/s).
(b) Compute $R$ at the core–mantle boundary ($\rho$ 5570 → 9900, $v_p$ 13.7 →
8.0 km/s) and at the inner-core boundary ($\rho$ 12 200 → 12 800, $v_p$ 10.3 →
11.0 km/s).
(c) Rank the four boundaries by impedance contrast and by density contrast, and
state whether the two rankings agree.
(d) Explain the ranking disagreement for the CMB in terms of the two factors of
$Z = \rho v_p$.

---

## ★★★ Research-oriented

**★★★9.** Distinguishing a phase boundary from a chemical boundary.

(a) State the seismological observables that a boundary produces, and which of
them a phase boundary and a chemical boundary have in common.
(b) Explain how the *sign* of the Clapeyron slope of an inferred phase change
predicts the boundary's depth response to a temperature anomaly, and what the
prediction is for the 410 km and 660 km discontinuities.
(c) Design the observation that would distinguish the two interpretations, being
explicit about what would be measured and what pattern would count as a
confirmation.
(d) Explain why the 410 and 660 satisfy the test and the core–mantle boundary
cannot be tested the same way.

---

**★★★10.** Amplitude, energy and angle.

(a) Show that the energy reflection coefficient for a normal-incidence wave is
$R^2$, and compute it for $R = 0.0186$.
(b) Explain why the $P$-wave reflection coefficient at the CMB is 1.86 per cent
at normal incidence but is not small at all angles.
(c) Explain why $R_S = -1$ exactly at the CMB, and what the minus sign means
physically.
(d) A student computes an energy budget from the CMB using $R = 0.0186$ and
concludes that the boundary is negligible. State two things the calculation has
missed.

---

**★★★11.** What the isotropic inversion omits.

The inversion of §2.1 assumes isotropic elasticity, so a single $v_p$ and a
single $v_s$ describe the material.

(a) State what a reference model reports when the real material is anisotropic.
(b) Explain why an anisotropic medium has more than one shear speed and what
observable that produces.
(c) The lowermost mantle and the inner core are both measurably anisotropic.
Explain why this is *information* about the material rather than merely a
complication.
(d) A colleague applies the isotropic inversion of §2.1 to a region known to be
transversely isotropic with 3 per cent anisotropy and reports the resulting $K$,
$\mu$ and $\nu$ to three significant figures. State the error in the reasoning
and the appropriate precision.
