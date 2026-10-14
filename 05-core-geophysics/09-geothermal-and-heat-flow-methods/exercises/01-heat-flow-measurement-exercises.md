# Exercises — 05-09-01 Measuring Terrestrial Heat Flow

Attempt these **closed-book** before opening the
[solutions](./01-heat-flow-measurement-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/heatflow_demo.py`](../code/heatflow_demo.py) require you to run it and
report its actual output. **State the sign convention and the direction of $z$ in
every answer, and report the equilibration state of any hole you quote.**

---

## ★ Foundational

**★1.** State the sign convention used in this module, and write $q$ for both
choices of the direction of $z$.

**★2.** A gradient of 22 K km⁻¹ and a conductivity of 2.8 W m⁻¹ K⁻¹: compute the
heat flow in mW m⁻².

**★3.** Distinguish an equilibrium temperature from a bottom-hole temperature, and
state the sign of their difference at depth in a conventionally cooled hole.

---

## ★★ Applied

**★★4.** Run [`../code/heatflow_demo.py`](../code/heatflow_demo.py).

(a) Report the flux-continuity table and state what changes across the contrast and
what does not.
(b) Report the disturbance table and the elapsed time at which the heat-flow bias
falls below 1 per cent.
(c) State the sign of the bias and the physical reason for it.

---

**★★5.** A two-layer model has $k_1 = 2.0$ W m⁻¹ K⁻¹ over 0–800 m and
$k_2 = 4.0$ W m⁻¹ K⁻¹ over 800–2000 m, a surface temperature of 12 °C and a flux of
70 mW m⁻². Compute the gradient in each layer and the temperature at 800 and 2000 m.

---

**★★6.** For $\kappa = 1.2\times10^{-6}$ m² s⁻¹, compute the depth at which a step
surface change has decayed to 10 per cent of its amplitude after 100 yr, 1 ka and
10 ka.

---

## ★★★ Research-oriented

**★★★7.** Invert the demonstration's erfc forward model for a GST history using a
stated parameterisation (say five step changes), synthetic data with 0.02 K noise,
and a Monte Carlo inversion. Report the family of histories consistent with the
data and state which time intervals are resolved and which are not.

---

**★★★8.** A hole shows systematic curvature below 600 m. Using a stated
one-dimensional advection–conduction model with a vertical Darcy velocity, show that
the curvature can be explained by advection, estimate the velocity required, and
state the ambiguity between that velocity and a conductivity that varies with depth.

---

## Reference list used in this problem set

- [05-09-01 lesson](../01-heat-flow-measurement.md)
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../../02-physics/05-thermodynamics/04-heat-conduction.md)
- [Solutions](./01-heat-flow-measurement-solutions.md)
