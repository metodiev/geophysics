# Exercises — 04-07-03 Landslides, Slope Stability and Geotechnical Geophysics

Attempt these **closed-book** before opening the
[solutions](./03-landslides-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/landslides_demo.py`](../code/landslides_demo.py) require you to run it
and report its actual output.

---

## ★ Foundational

**★1.** A slope of unit weight $\gamma = 19$ kN m⁻³ has $c' = 8$ kPa,
$\phi' = 28^\circ$, a slip plane 4 m below the surface, and a slope angle
$\beta = 25^\circ$.

(a) Compute the normal and shear stresses on the slip plane.
(b) Compute the factor of safety dry.
(c) Compute the factor of safety with a pore-pressure ratio $r_u = 0.35$.
(d) Compute the pore-pressure ratio at failure.

---

**★2.** The same geometry has $\beta = 25^\circ$ and $\phi' = 30^\circ$, with
$c' = 0$.

(a) Compute the static factor of safety.
(b) Compute the exact critical pseudo-static coefficient $k_h$ and the
small-slope approximation, and their ratio.
(c) Compute the critical acceleration in m s⁻².
(d) State whether the approximation is safe or unsafe to use, and why.

---

**★3.** A rectangular acceleration pulse has amplitude 3 m s⁻² and duration
0.4 s. The critical acceleration is 1.5 m s⁻².

(a) Compute the relative displacement using the closed form.
(b) Halve the pulse duration and compute the new displacement.
(c) State the scaling of the displacement with the excess acceleration
$(a - a_c)$ at fixed $a_c$, and with $a_c$ at fixed $a$.

---

**★4.** A refraction survey over a soil slope gives $v_1 = 500$ m s⁻¹ and an
intercept time of 14 ms on a head-wave branch with $v_2 = 2400$ m s⁻¹.

(a) Compute the depth to the refractor.
(b) State the two quantities that dominate the uncertainty in that depth.
(c) State what the survey would show if the layer between 3 and 8 m had a
velocity of 300 m s⁻¹ instead.

---

## ★★ Applied

**★★5.** Run the demo's section 1, which uses $\phi' = 32^\circ$, $c' = 0$,
$z = 3$ m, $\gamma = 18$ kN m⁻³.

(a) Report the factor of safety at $\beta = 32^\circ$ dry and state the general
rule it illustrates.
(b) Report the fully saturated pore-pressure ratio and the critical $r_u$ at
$\beta = 10^\circ$, $15^\circ$ and $20^\circ$.
(c) Identify the steepest whole-degree slope angle that survives full
saturation, and explain the criterion you used.
(d) A piezometer in the 3 m column reads 1.5 m of head above the slip plane.
Compute $r_u$, compare it with the critical value at 20°, and state the factor
of safety.

---

**★★6.** Run the demo's section 3.

(a) Report the numerical and closed-form displacements and the relative
differences.
(b) Explain why the zero-acceleration part of the record is essential.
(c) Using the closed form, compute the displacement for $a = 5$ m s⁻²,
$a_c = 0.86$ m s⁻² and $t_0 = 0.3$ s.
(d) Recompute it for $a_c = 1.03$ m s⁻² (a 20 per cent increase) and give the
percentage change. Then do the same for $a_c = 4.8$ m s⁻² against
$a_c = 4.0$ m s⁻² and comment on the difference.

---

**★★7.** Run the demo's section 5 with $\phi = 0.35$.

(a) Report the velocities at $\theta = 0.05$ and $\theta = 0.30$ and their
ratio.
(b) Report $\mathrm{d}\theta/\mathrm{d}v$ and the water-content precision
corresponding to 0.001 m ns⁻¹ of velocity precision.
(c) A field survey measures $v = 0.090$ m ns⁻¹. Invert CRIM for $\theta$.
(d) State two reasons the answer to (c) might be wrong by more than the
precision in (b).

---

## ★★★ Research-oriented

**★★★8.** A three-layer section has $v_1 = 500$ m s⁻¹ from 0 to 3 m,
$v_2 = 300$ m s⁻¹ from 3 to 8 m, and $v_3 = 2000$ m s⁻¹ below 8 m.

(a) Explain why first arrivals never travel through layer 2.
(b) Compute the intercept time of the head wave refracting along the top of
layer 3, using the two critical angles involved.
(c) Invert that intercept time as if the section were two layers, and compare
the result with the true depth of 8 m.
(d) State, in two sentences, what a geophysical survey must do differently to
detect the weak layer, and why that method is more expensive.

---

**★★★9.** A slope has $c' = 0$, $\phi' = 34^\circ$, $\gamma = 20$ kN m⁻³,
$z = 6$ m, and a slope angle of $18^\circ$.

(a) Compute $r_u^\mathrm{crit}$ and the fully saturated $r_u$.
(b) A rainfall event raises the water table to 2 m below the surface. Assuming
hydrostatic conditions below that level, compute the pore pressure at the slip
plane and hence $FS$. State every assumption.
(c) Compute the rainfall threshold (in metres of water-table rise) at which
$FS = 1.0$.
(d) Explain how you would use (c) operationally, and state one reason the real
threshold will differ from the computed one.
