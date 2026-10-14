# Exercises — 02-11-05 Comparative Planetary Physics and Interiors

Attempt these **closed-book** before opening the
[solutions](./05-planetary-physics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/planetary_physics_demo.py`](../code/planetary_physics_demo.py) require
you to run it and report its actual output.

**Every problem that asks for a core size, a core density, a field strength or an
atmospheric inventory requires you to state which quantity is measured, which is
assumed, and which is computed.** Earth values are **nominal** handbook
characteristics; the moment-of-inertia factor is **nominal and rounded**; and no
values for other bodies are given here — the formulae are evaluated over
parameter ranges so that you can substitute whichever body's measured values you
have from a mission source.

---

## ★ Foundational

**★1.** Two-layer moment of inertia. For a core of radius fraction $f$ and density
$\alpha$ times the mantle density,

$$k \equiv \frac{C}{MR^2} = 0.4\,\frac{f^5\alpha+1-f^5}{f^3\alpha+1-f^3}.$$

(a) State the value of $k$ for a homogeneous sphere and for a point mass, and
derive the first from $C = \tfrac25MR^2$.
(b) Evaluate $k$ for $f = 0.5$, $\alpha = 3$.
(c) Evaluate $k$ for $f = 0.5$, $\alpha = 1$ and explain the result without
arithmetic.
(d) Explain why $k$ cannot exceed 0.4 for any spherically symmetric body.

---

**★2.** The two-layer inversion. With $f = 0.6$, $M = 5.972\times10^{24}$ kg and
$R = 6.371\times10^6$ m:

(a) Solve $k = 0.33$ for $\alpha$.
(b) Compute the mantle density from
$M = \tfrac43\pi R^3\rho_m(f^3\alpha+1-f^3)$.
(c) Compute the mean core density.
(d) State whether that core density is credible against the handbook's range
(outer core top 9900 kg m⁻³, inner-core centre 13 100 kg m⁻³).

---

**★3.** Dynamo diagnostics. With $\sigma = 5\times10^5$ S m⁻¹,
$U = 2\times10^{-4}$ m s⁻¹ and $L = 1.5\times10^6$ m:

(a) Compute $Rm = \mu_0\sigma UL$ with
$\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N A⁻².
(b) Compute the magnetic diffusion time $\tau_\eta = \mu_0\sigma L^2$ in seconds
and in years.
(c) State whether $Rm$ in (a) is above or below the dynamo threshold, and how
robust that conclusion is to a factor-of-two error in each input.
(d) Explain in one sentence what $\tau_\eta$ represents physically.

---

**★4.** Jeans escape. For a molecule of mass $m$ at exobase radius $r$ and
exobase temperature $T$:

(a) Derive $\lambda = GMm/(k_BTr)$ from the condition
$\tfrac12mv^2 = GMm/r$.
(b) Show that $\lambda = v_{\text{esc}}^2m/(2k_BT)$.
(c) The Earth's exobase is taken at $r = 6871$ km with $T = 1000$ K. Compute
$\lambda$ for N₂ ($m = 28.014$ u).
(d) State whether N₂ is retained, and give the threshold you used.

---

## ★★ Applied

**★★5.** The degeneracy grid.

(a) Using the formula of ★1, compute $k$ for $f = 0.4$ at $\alpha = 1, 2, 3, 4$.
(b) Compute $k$ for $\alpha = 3$ at $f = 0.2, 0.4, 0.6, 0.8$.
(c) A body has a measured $k = 0.36$. List two $(f,\alpha)$ pairs consistent
with it, and state what further measurement would distinguish them.
(d) Explain why $k$ alone is not a measure of iron content, and name the physical
effect that confuses it.

---

**★★6.** Diffusion timescales compared.

(a) Compute the thermal diffusion time $\tau_\kappa = L^2/\kappa$ for
$L = 1.5\times10^6$ m and $\kappa = 10^{-5}$ m² s⁻¹.
(b) Compare with the magnetic diffusion time of ★3(b) and give the ratio.
(c) Compare $\tau_\kappa$ with the age of the Earth and state the conclusion for
core heat transport.
(d) Explain why the same conclusion — that convection is required — serves both
the thermal and the magnetic requirements.

---

**★★7.** Impedance-like reasoning applied to escape.

(a) Explain why $\lambda\propto m$ at fixed $M$, $r$ and $T$.
(b) Compute $\lambda$ for H₂ ($m = 2.016$ u) and He ($m = 4.003$ u) at the Earth's
exobase as in ★4, by scaling from your N₂ answer.
(c) A body has one tenth the Earth's mass and half its radius, with the same
exobase temperature. Compute $\lambda$ for H₂, N₂ and CO₂ using
$\lambda\propto M/r$.
(d) State which species that body retains and which it loses, and explain the
selection rule.

---

**★★8.** Scale height and escape together. For an atmosphere of mean molecular
mass $m$ on a body of surface gravity $g$ and temperature $T$:

(a) Write $H = k_BT/(mg)$ and state how $H$ and $\lambda$ depend on $m$.
(b) Explain why a species that is hard to remove occupies a thin layer, and a
species that is easy to remove extends far out.
(c) A colleague argues that a body retains whichever species has the *largest*
scale height, because "a thicker atmosphere is harder to lose". Identify the
error.
(d) State the two molecular properties that matter and how each enters.

---

## ★★★ Research-oriented

**★★★9.** The inference loop without seismology.

(a) Write the loop as an algorithm: what is measured, what is assumed, what is
computed, what is compared.
(b) Explain, in terms of the number of unknowns and constraints, why the output is
a family of models rather than a single model.
(c) Name three measurements, each of which adds exactly one constraint, and state
in each case what quantity it constrains.
(d) Explain why the Earth is the calibration point for all of this, and what kind
of difficulty is being extrapolated when the same machinery is applied to a
different body.

---

**★★★10.** Dynamo criteria and the observed pattern.

(a) Name the three requirements for a self-sustaining dynamo and give the physical
reason for each.
(b) Use them to account for why Venus has no present-day intrinsic field, listing
two candidate explanations and stating which observations would discriminate
between them.
(c) Explain why "Mars has no global field" is an incomplete statement, and what
the complete statement is.
(d) Explain what the strongly tilted, strongly offset fields of Uranus and Neptune
imply about the geometry of their dynamo regions, and why that is a stronger
statement than "they have dynamos".

---

**★★★11.** Sensitivity and honest reporting.

(a) Differentiate the two-layer formula of ★1 with respect to $f$ and with respect
to $\alpha$ at $(f,\alpha) = (0.5462, 3.039)$ and report which input $k$ is more
sensitive to.
(b) Holding $f$ fixed, quantify how $\alpha$ and the core density change when $k$
changes from 0.33 to 0.3308.
(c) Given your answer to (a), state which input limits the inferred core density
and why.
(d) Write three sentences reporting a two-layer core-density inference that are
defensible: state the model, the inputs, the sensitivity, and the dominant
systematic. Do not present the result as a measurement.

---

**★★★12.** What would falsify the comparative framework.

For each of the following claims, state an observation that would falsify it, and
say whether the observation is currently available.

(a) A body's low $k$ requires that it has a metallic core.
(b) Magnetic remanence in crustal rocks implies that a dynamo once operated.
(c) A body with no present-day field must have failed one of the three dynamo
requirements.
(d) The observed composition of a terrestrial-planet atmosphere can be explained
by Jeans escape alone.
