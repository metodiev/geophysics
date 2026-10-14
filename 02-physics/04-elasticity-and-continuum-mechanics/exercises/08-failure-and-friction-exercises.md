# Exercises — 02-04-08 Rock Failure, Fracture and Rate-State Friction

Attempt these **closed-book** before opening the
[solutions](./08-failure-and-friction-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/failure_friction_demo.py`](../code/failure_friction_demo.py) require you
to run it and report its actual output.

---

## ★ Foundational

**★1.** For $C = 15$ MPa, $\mu = 0.7$, $\sigma_3' = 50$ MPa:

(a) Compute $\varphi$ and the failure stress $\sigma_1'$.
(b) Compute the orientation of the failure plane (both the angle of its normal and
the inclination of the plane, measured from $\sigma_1$).
(c) Compute $\sigma_n'$ and $\tau$ on the failure plane and verify that
$\tau = C+\mu\sigma_n'$.
(d) State the fault dip for normal faulting and for thrust faulting.

---

**★2.** For the same parameters as ★1, compute the failure stress for
$C = 0$ and compare with the $C = 15$ MPa value.

(a) Compute $\sigma_1'$ for $C = 0$.
(b) Show algebraically that cohesion enters the failure condition through the term
$2C\tan(45^\circ+\varphi/2)$.
(c) Compute that term numerically and verify (b) against (a).
(d) State which of $C$ and $\mu$ matters more for a fault at 10 km depth, and why.

---

**★3.** A rock with $\sigma_3' = 100$ MPa and $C = 0$ has $\mu = 0.6$.

(a) Compute $\sigma_1'$ at failure, and the centre and radius of the Mohr circle
for that stress state.
(b) Compute the tangent-point coordinates, verify $\tau = \mu\sigma_n'$ there, and
compute the orientation of the failure plane (both the angle of its normal and its
inclination to $\sigma_1$).
(c) Compute the largest shear stress over all planes and the orientation at which
it occurs, and check whether the friction law is satisfied there.
(d) Explain why the failure plane is not the plane of maximum shear.

---

**★4.** Write the Dieterich–Ruina law and derive the steady-state friction.

(a) State the law and the state evolution equation.
(b) Show $\theta_{ss} = D_c/V$.
(c) Show $\mu_{ss}(V) = \mu_* + (a-b)\ln(V/V_*)$.
(d) State the physical meaning of $a>b$ and $a<b$, and give one geological
consequence of each.

---

## ★★ Applied

**★★5.** Run section 1 of the demo.

(a) Report the computed failure stress, the maximum residual
$\tau-\mu\sigma_n'-C$, and the orientation found by the scan.
(b) Compare the numerical orientation with the analytic $45^\circ+\varphi/2$ and
$45^\circ-\varphi/2$ values, and state which refers to the normal and which to the
plane.
(c) State why the residual is not exactly zero and estimate the resolution limit
from the grid used.
(d) Explain in one paragraph why this calculation is a *tangency* condition rather
than a separate physical law.

---

**★★6.** Run section 2 of the demo.

(a) Report $\sigma_v$, $\sigma_n'$ and $\tau$ at 2 km and at 30 km, and compute the
slope of the strength profile in MPa km⁻¹.
(b) Verify the slope against $\mu(\rho-\rho_w)g$ with the demo's parameters.
(c) Compute the depth at which $\tau$ would equal 100 MPa, and note the assumption
about normal stress that makes this an envelope rather than a fault-specific
strength.
(d) List four quantities that would have to be specified before quoting a
brittle–ductile transition depth for a specific region, and state why the demo's
table alone cannot supply it.

---

**★★7.** Run section 3 of the demo.

(a) Report $k_c$ and the parameter values used.
(b) Report the growth ratios at $k/k_c = 0.2, 0.9, 1.1$ and $5$, and identify the
transition.
(c) Report the measured threshold and its ratio to $k_c$; then report the exact
linearised trace at $k/k_c = 1.00$.
(d) Explain why the measured threshold deviates from $k_c$ and why the deviation
should not be reported as an error in $k_c$.

---

**★★8.** A fault patch has $\sigma' = 150$ MPa, $D_c = 20\ \mu$m, $a = 0.008$,
$b = 0.012$, in a rock of shear modulus $\mu = 30$ GPa.

(a) Compute $k_c$.
(b) Estimate the stiffness of the surrounding rock for a circular patch of radius
$r$ using $k \sim \mu/r$ (state that this is a scaling estimate, with the
geometrical factor $\sim$1) and compute the patch radius at which $k = k_c$.
(c) State whether patches smaller or larger than that radius tend to slip
unstably, and why.
(d) Compute how $k_c$ changes if $D_c$ is ten times larger, and state the
implication for earthquake nucleation.

---

## ★★★ Research-oriented

**★★★9.** The stress–heat-flow paradox.

(a) Using the strength envelope of section 3.4, compute the shear heating rate per
unit fault area, $q = \tau V$, for a fault slipping at $V = 30$ mm yr⁻¹,
evaluating $\tau$ (i) at 10 km depth with $\mu = 0.6$ and hydrostatic pore
pressure, and (ii) as the average of the linear profile over a 2–12 km brittle
zone. Convert both to mW m⁻².
(b) Compare these with a typical continental background heat flow (state the value
you use and why it is a reasonable choice), and state what *observational
signature* a strong fault would be expected to produce. Then state whether the
comparison is a like-for-like one, and identify the geometric simplification you
are making by treating a narrow fault as a planar heat source.
(c) List the mechanisms proposed to resolve the paradox.
(d) State precisely what is uncertain in your estimate: which numbers you assumed,
and how the conclusion changes if they are wrong by a factor of two.
(e) For each mechanism, state one observation that would support or falsify it.

---

**★★★10.** Stability of a two-patch fault.

(a) Consider two patches in series, one velocity-weakening
($a = 0.010$, $b = 0.014$, $D_c = 10\ \mu$m) and one velocity-strengthening
($a = 0.016$, $b = 0.010$, $D_c = 10\ \mu$m), both at $\sigma' = 100$ MPa.
Compute $k_c$ for each and state which can nucleate.
(b) For the weakening patch, compute the slip-weakening distance implied by
$\Delta\tau = \sigma'(b-a) = k_c D_c$ and interpret it.
(c) Explain qualitatively how the strengthening patch affects the behaviour of the
weakening one (does it raise or lower the effective stiffness seen by the
weakening patch?), and state one observable consequence.
(d) Design a numerical experiment (spring–slider with two blocks coupled by a
spring) that would test your answer to (c), and state what you would measure.

Report measured values only if you verify them numerically, and state clearly which
of your claims are scaling estimates rather than derived results.
