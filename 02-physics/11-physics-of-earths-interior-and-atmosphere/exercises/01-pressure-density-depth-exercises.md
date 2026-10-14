# Exercises — 02-11-01 Pressure, Density and Gravity Inside the Earth

Attempt these **closed-book** before opening the
[solutions](./01-pressure-density-depth-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/interior_pressure_demo.py`](../code/interior_pressure_demo.py) require
you to run it and report its actual output. This is the module's mastery lesson:
**every problem that asks for a pressure, a mass or a moment of inertia requires
you to state the density profile you assumed, and whether the number you quote is
computed, measured or nominal.**

Keep the three classifications of the
[constant handbook](../../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
§3.3 separate throughout: $G$ is **measured**, $GM_\oplus$ and the standard
atmosphere are **exact**, and every interior density and velocity is **nominal**.

---

## ★ Foundational

**★1.** For a spherically symmetric body of **constant** density $\rho_0$, radius
$R$ and mass $M$:

(a) Derive $g(r) = \tfrac43\pi G\rho_0 r$ for $r \le R$.
(b) Integrate $\mathrm{d}P/\mathrm{d}r = -\rho_0 g$ from $P(R) = 0$ and show that
$P(r) = \tfrac23\pi G\rho_0^2(R^2-r^2)$.
(c) Evaluate $P_c$ for $\rho_0 = 5513$ kg m⁻³ and $R = 6.371\times10^6$ m, and
compare with $0.1194\,GM^2/R^4$ using $M = 5.972\times10^{24}$ kg.
(d) Evaluate $P(R/2)$ and state its ratio to $P_c$ without any further
arithmetic.

---

**★2.** Using $\rho_0 = 5513$ kg m⁻³, $R = 6.371\times10^6$ m and
$M = 5.972\times10^{24}$ kg:

(a) Evaluate the scale $GM^2/R^4$ in GPa.
(b) The layered reference model of the lesson gives $P_c = 356.7$ GPa. Express
that as a multiple of $GM^2/R^4$, and compare with the uniform-sphere
coefficient 0.1194.
(c) State in one sentence what the comparison establishes about the Earth's
density distribution, and why no seismology was needed to establish it.

---

**★3.** A two-layer planet has a mantle of density $\rho_m$ out to $r_c$ and a
core of density $\rho_c = \alpha\rho_m$ inside, so that
$k \equiv C/(MR^2) = 0.4(f^5\alpha+1-f^5)/(f^3\alpha+1-f^3)$ with $f = r_c/R$.

(a) Show that $k = 0.4000$ for $\alpha = 1$ for every $f$, and that $k = 0.4000$
for $f = 0$ for every $\alpha$. Explain both geometrically.
(b) Evaluate $k$ for $f = 0.5$ and $\alpha = 3$.
(c) A body has $k = 0.34$ from such a model with $f = 0.5$. Solve for $\alpha$.
(d) Comment on whether the value in (c) is physically credible for a
terrestrial planet, given the handbook's core density range.

---

**★4.** A body has a mantle of density 4138 kg m⁻³ for $r > r_c$ and a core of
uniform density 12 576 kg m⁻³ for $r < r_c$, with $r_c = 3.480\times10^6$ m and
$R = 6.371\times10^6$ m.

(a) Compute the total mass, using
$M = \tfrac43\pi R^3\rho_m[f^3\alpha + 1 - f^3]$, and compare with
$5.972\times10^{24}$ kg.
(b) Compute $k = C/(MR^2)$.
(c) Compute $g$ at the core–mantle boundary from $g = GM_c/r_c^2$ where
$M_c$ is the core mass, and compare with the layered model's 10.51 m/s².
(d) Explain the sign of the discrepancy in (c).

---

**★5.** At the Moho the rounded handbook values are $\rho = 3300$ kg m⁻³,
$v_p = 8.1$ km/s, $v_s = 4.5$ km/s, and the layered model gives $g \approx 9.81$
m/s² there.

(a) Compute $\phi = v_p^2 - \tfrac43 v_s^2$ in km² s⁻² and in m² s⁻².
(b) Compute the Adams–Williamson density gradient $\rho g/\phi$ in
kg m⁻³ km⁻¹.
(c) The rounded model's own density gradient over the 35–410 km interval is
$0.80$ kg m⁻³ km⁻¹. Compute the ratio and state what it means.
(d) State the two assumptions Adams–Williamson carries, and say whether they
are satisfied here.

---

## ★★ Applied

**★★6.** Using the two-layer family of ★3, with the Earth's mass and radius:

(a) For $f = 0.5$, 0.55, 0.6 and 0.65, solve $k = 0.33$ for $\alpha$, then find
$\rho_m$ from the mass and hence $\rho_c = \alpha\rho_m$.
(b) Tabulate the four $(\alpha, \rho_c)$ pairs.
(c) Requiring the mean core density to lie between the handbook's outer-core top
value (9900 kg m⁻³) and its inner-core centre value (13 100 kg m⁻³), state the
range of $f$ that the moment of inertia and the mass alone permit.
(d) Compare that range with the seismic core radius fraction
$3480/6371 = 0.546$. State what this comparison shows about the strength of the
combined mass-and-moment-of-inertia constraint.

---

**★★7.** Two-layer central pressures. Using
$$P_c = \tfrac23\pi G\rho_c^2r_c^2
+ \tfrac43\pi G\rho_m\left[(\rho_c-\rho_m)r_c^2\left(1-\frac{r_c}{R}\right)
+ \tfrac{\rho_m}{2}(R^2-r_c^2)\right],$$

(a) Evaluate $P_c$ for the $f=0.5462$, $\alpha = 3.039$ model (the favoured one)
and for the $f = 0.5$, $\alpha = 3.435$ model of ★6.
(b) Compare both with the numerically integrated layered-model value of
356.7 GPa, and compute the percentage by which each over-predicts.
(c) Explain, in terms of the pressure integrand, why the smaller, denser core
gives the *larger* central pressure.
(d) State which of the two models the mass, radius and moment of inertia
*prefer*, and therefore why those three constraints alone cannot settle the
question.

---

**★★8.** In the layered reference model, use the demo's own output rather than
the table in the lesson.

(a) Report $P$ at 3000 km and 4000 km depth, and interpolate linearly to obtain
$P$ at the radius $R/2$ (depth 3185.5 km).
(b) Compute the uniform-sphere pressure at the same radius from ★1(b), and give
the ratio.
(c) The layered model's $g$ is 10.51 m/s² at the core–mantle boundary and 4.39
m/s² at the inner-core boundary. A uniform outer core of density 11 050 kg m⁻³
extending to $r = 3480$ km would give $g(r) \propto r$; compute the implied $g$
at the inner-core boundary from that scaling and report the discrepancy.
(d) Explain why the discrepancy in (c) is a direct measurement of the density
gradient inside the outer core.

---

**★★9.** Dimensional checking, without computing anything numerically.

(a) Show that $GM^2/R^4$ has the dimensions of pressure.
(b) Show that $\rho g/\phi$ has the dimensions of a density gradient per unit
length, and state the conversion factor to kg m⁻³ km⁻¹ for $\rho$ in kg m⁻³,
$g$ in m s⁻² and $\phi$ in km² s⁻².
(c) A student writes $P_c = GM^2/R^3$. Identify the dimensional error and state
what the resulting number would be (you may give it as a multiple of the correct
$GM^2/R^4$).
(d) A student reports a mantle density gradient of $8.4\times10^{-4}$ kg m⁻³ per
metre and then, "to convert to per kilometre", divides by $10^3$. Explain the
error and give the correct value.

---

## ★★★ Research-oriented

**★★★10.** Verification of a numerical hydrostatic integrator.

(a) Design a verification test for an integrator that computes $M(r)$, $g(r)$
and $P(r)$ from a supplied $\rho(r)$. Specify the two exact solutions you would
use and the quantity you would measure.
(b) The demo reports relative errors of $3.14\times10^{-4}$ (uniform sphere) and
$2.53\times10^{-4}$ (two-layer sphere) at $\Delta r = 500$ m. Explain why these
two numbers being *different* is expected rather than a defect.
(c) Explain precisely why the pressure loop must accumulate from the surface
inward, and what a student who writes it the other way round would observe.
(d) A colleague's integrator reproduces the total mass to 6 significant figures
but gives a central pressure 30 per cent too low. List three possible causes and
say how each would be distinguished.
(e) State one verification test that the uniform-sphere test does **not**
provide, and design a test that does.

---

**★★★11.** The Adams–Williamson method as an inversion.

(a) Write down the method as an algorithm: what is measured, what is assumed,
what is integrated, and what is compared with what.
(b) The demo reports ratios of A–W gradient to model gradient of 1.11, 0.22,
1.06, 1.00 and 1.09 for the upper mantle, transition zone, lower mantle, outer
core and inner core. For each, state the physical interpretation in one sentence.
(c) Explain why the transition zone's value of 0.22 is *not* a failure of the
method but its most valuable output.
(d) The method integrates an error downward from the top of an interval. Explain
why that makes it unsuitable for determining an absolute density, and what
independent quantity supplies the anchor.
(e) A colleague proposes applying the method to the whole mantle in one step
from the Moho to the CMB. Explain why the result would be meaningless even
though the arithmetic would work.

---

**★★★12.** Inference with stated uncertainty.

The two-layer inversion of ★6 gives a range of core radii because the density
contrast and the core size are not separately determined by $M$ and $k$ alone.

(a) Write the two-layer model's $M$ and $k$ as two equations, and count equations
and unknowns. State whether the system is determined, over-determined or
under-determined, and hence what kind of solution set you should expect.
(b) Differentiate $k(f,\alpha)$ with respect to each argument at
$(f,\alpha) = (0.5462, 3.039)$ and report which of $f$ and $\alpha$ the moment of
inertia is more sensitive to. Use your answer to say which input limits the
inferred core density most.
(c) The Earth's $k$ is quoted as 0.33 here and is closer to 0.3308 in the precise
geodetic literature. Quantify the change in $\alpha$ caused by that shift, holding
$f$ fixed.
(d) Write two sentences, suitable for a paper abstract, reporting the core density
implied by a two-layer fit while being honest about its provenance and its
uncertainty. Do not state a value you have not computed.
