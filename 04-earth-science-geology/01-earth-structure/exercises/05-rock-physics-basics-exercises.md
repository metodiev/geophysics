# Exercises — 04-01-05 Density, Porosity, Permeability and Elastic Properties

Attempt these **closed-book** before opening the
[solutions](./05-rock-physics-basics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/rock_physics_basics_demo.py`](../code/rock_physics_basics_demo.py)
require you to run it and report its actual output. Use
$\rho_\text{quartz} = 2650$ kg/m³, $\rho_\text{water} = 1000$ kg/m³,
$\rho_\text{gas} = 100$ kg/m³, $K_\text{quartz} = 37$ GPa,
$K_\text{brine} = 2.2$ GPa, $K_\text{gas} = 0.02$ GPa,
$\mu_\text{rock} = 3\times10^{10}$ Pa, and 1 darcy $= 9.869\times10^{-13}$ m².

---

## ★ Foundational

**★1.** A sandstone has a grain density of 2650 kg/m³ and a porosity of 15 per
cent.

(a) Compute its dry bulk density.
(b) Compute its bulk density saturated with water.
(c) Compute its bulk density saturated with gas.
(d) State the density contrast between (b) and (c) in kg/m³ and as a percentage.

---

**★2.** A rock is 30 per cent quartz and 70 per cent clay by volume. Take
$K_\text{quartz} = 37$, $K_\text{clay} = 21$ GPa.

(a) Compute the Voigt (upper) bound for $K$.
(b) Compute the Reuss (lower) bound.
(c) Compute the Hill average.
(d) State what the width of the bound means physically.

---

**★3.** Kozeny–Carman: $k = d^2\phi^3/[180(1-\phi)^2]$.

(a) Compute $k$ in m² for $d = 0.15$ mm and $\phi = 0.20$.
(b) Convert to darcy.
(c) Recompute for $d = 1.5$ mm and state the scaling.
(d) State what the relation assumes and one way a real rock violates it.

---

## ★★ Applied

**★★4.** Gassmann: $K_\text{sat} = K_\text{dry} + (1-K_\text{dry}/K_\text{min})^2
/[\phi/K_\text{fl} + (1-\phi)/K_\text{min} - K_\text{dry}/K_\text{min}^2]$.

Use $K_\text{dry} = 9.92$ GPa, $G_\text{dry} = 6.87$ GPa, $K_\text{min} = 37$ GPa.

(a) Compute $K_\text{sat}$ for $\phi = 0.15$ with brine.
(b) Compute $K_\text{sat}$ for $\phi = 0.15$ with gas.
(c) Compute $v_p$ and $v_s$ for both, with the corresponding saturated densities.
(d) Compare the size of the gas effect at $\phi = 0.15$ with the demo's value at
$\phi = 0.20$ and state the trend.

---

**★★5.** Archie's law: $S_w = (aR_w/(\phi^m R_t))^{1/n}$ with $a = 1$, $m = 2$,
$n = 2$.

(a) Compute $S_w$ for $\phi = 0.22$, $R_w = 0.05$ Ω·m, $R_t = 10$ Ω·m.
(b) Compute $S_w$ for $R_t = 40$ Ω·m.
(c) State how the saturation scales with $R_t$ and why.
(d) Compute the porosity required for $S_w = 1.0$ at $R_t = 10$ Ω·m and comment.

---

**★★6.** Error propagation.

Take $v_p = 3500$ m/s, $v_s = 2000$ m/s, $\rho = 2300$ kg/m³.

(a) Compute $K$ and $G$ in GPa.
(b) Recompute $K$ with $v_s$ increased by 1 per cent.
(c) Report the percentage change in $K$.
(d) State why the amplification is what it is.

---

## ★★★ Research-oriented

**★★★7.** Two porosity models disagree.

(a) Compute $v_p$ from the time average
$1/v_p = \phi/v_f + (1-\phi)/v_m$ with $\phi = 0.20$,
$v_f = 1500$ m/s, $v_m = 5500$ m/s.
(b) Take the Gassmann $v_p$ for the same porosity with brine from the demo
(`3228 m/s`) and compute the difference.
(c) Convert the difference into an apparent porosity by inverting both to a
porosity from a common velocity — state the ambiguity in one sentence.
(d) Explain why the two models are not measuring the same "porosity".

---

**★★★8.** Run
[`../code/rock_physics_basics_demo.py`](../code/rock_physics_basics_demo.py) and
report:

(a) the bulk density at $\phi = 0.20$ for a brine- and a gas-filled quartz
framework, and the contrast in per cent;
(b) the Voigt–Reuss spread for $K$ and for $G$ at a 50/50 quartz–calcite mix;
(c) the $K_\text{sat}$, $v_p$ and $v_s$ for brine, oil and gas at $\phi = 0.20$;
(d) the percentage changes in $v_p$ and $v_s$ from brine to gas and the signs;
(e) the Kozeny–Carman permeability at $d = 0.20$ mm for $\phi = 0.15, 0.25$ and
$0.35$, in darcy;
(f) the percentage permeability loss from 0.25 to 0.20 and from 0.15 to 0.10;
(g) the Archie saturation that returns a value above 1, and what it means;
(h) two sentences on which outputs are computed and which are tabulated.

---

**★★★9.** Sensitivity of fluid substitution to the dry-rock moduli.

Using Gassmann with $\phi = 0.20$, $K_\text{min} = 37$ GPa and brine:

(a) compute $K_\text{sat}$ for $K_\text{dry} = 5$, 10 and 20 GPa with
$G_\text{dry} = 6.87$ GPa;
(b) compute the brine-to-gas change in $K_\text{sat}$ for each;
(c) state how the size of the fluid effect depends on the dry-rock stiffness and
why;
(d) state which real rocks a time-lapse seismic survey would therefore be able to
monitor and which it would not.
