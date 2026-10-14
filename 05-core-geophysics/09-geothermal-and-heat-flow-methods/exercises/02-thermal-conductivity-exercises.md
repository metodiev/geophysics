# Exercises — 05-09-02 Thermal Conductivity Measurement and Corrections

Attempt these **closed-book** before opening the
[solutions](./02-thermal-conductivity-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/thermal_cond_demo.py`](../code/thermal_cond_demo.py) require you to run it
and report its actual output. **Every conductivity must carry its orientation,
saturation and temperature, and every mixing order must be named.**

---

## ★ Foundational

**★1.** State the units and the physical meaning of $k$ and $\kappa$, and the
relation between them.

**★2.** For equal thicknesses of $k = 1.0$ and $k = 4.0$ W m⁻¹ K⁻¹, compute
$k_\parallel$, $k_\perp$ and the anisotropy.

**★3.** State which of the two means is always smaller and why.

---

## ★★ Applied

**★★4.** Run [`../code/thermal_cond_demo.py`](../code/thermal_cond_demo.py).

(a) Report the three means for the demonstration's stack and the parallel–series
ratio.
(b) Recompute all three for 50 per cent shale (1.5), 30 per cent sandstone (3.5) and
20 per cent evaporite (5.0) W m⁻¹ K⁻¹.
(c) State which mean belongs in a vertical heat-flow calculation and why.

---

**★★5.** A divided bar reads $\Delta T_r = 2.00$ K over 50 mm with
$k_r = 3.50$ W m⁻¹ K⁻¹ and $\Delta T_s = 2.80$ K over 40 mm.

(a) Compute $k_s$.
(b) Compute the uncertainty for a 0.03 K thermocouple uncertainty on each
temperature difference.
(c) State which input dominates the uncertainty.

---

**★★6.** For a rock with $\rho = 2700$ kg m⁻³, $c_p = 900$ J kg⁻¹ K⁻¹ and
$k = 2.6$ W m⁻¹ K⁻¹: compute $\kappa$, the diffusion time over 1 km and the
diffusion length in 1 Ma.

---

## ★★★ Research-oriented

**★★★7.** Build a two-component mixing model with a statistical orientation
distribution (neither purely series nor parallel) and compute the effective
conductivity as a function of the orientation parameter. Report the bounds and state
which geological textures fall where.

---

**★★★8.** Design a conductivity measurement programme for a 2 km hole in a
lithologically heterogeneous basin: sample count, orientations, pressures and
saturations, and how the cores are combined with a borehole method. State the
resulting uncertainty in $k_\perp$ per interval and its effect on the heat flow.

---

## Reference list used in this problem set

- [05-09-02 lesson](../02-thermal-conductivity.md)
- [05-09-01 Measuring Terrestrial Heat Flow](../01-heat-flow-measurement.md)
- [Solutions](./02-thermal-conductivity-solutions.md)
