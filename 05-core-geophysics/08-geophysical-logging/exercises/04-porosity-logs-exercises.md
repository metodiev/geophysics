# Exercises — 05-08-04 Density, Neutron and Sonic Porosity Logs

Attempt these **closed-book** before opening the
[solutions](./04-porosity-logs-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/porosity_demo.py`](../code/porosity_demo.py) require you to run it and
report its actual output. **Never call any of these an porosity measurement without
naming the matrix and fluid assumption it rests on.**

Constants: quartz matrix 2650 kg m⁻³, 182 µs m⁻¹; calcite 2710, 156; dolomite 2870,
143; water 1000, 620 µs m⁻¹, $HI = 1.00$; oil 800, 760, $HI = 0.95$; gas 150,
1150, $HI = 0.35$. All are STATED SYNTHETIC values from the demonstration.

---

## ★ Foundational

**★1.** State what each of the four porosity measurements physically measures and
one assumption each requires.

**★2.** Compute $\phi_D$ for $\rho_b = 2450$ kg m⁻³ with a quartz matrix and (a)
water, (b) oil of 800 kg m⁻³.

**★3.** Convert $\Delta t = 100$ µs ft⁻¹ to µs m⁻¹ and compute the two-way travel
time over a 1000 m vertical interval at that constant slowness.

---

## ★★ Applied

**★★4.** Run [`../code/porosity_demo.py`](../code/porosity_demo.py).

(a) Report the crossover for hydrogen indices of 0.20, 0.35 and 0.60 at a true
porosity of 0.20 (interpolate or recompute).
(b) State the hydrogen index at which the density and neutron apparent porosities
agree, and explain why such a value must exist.

---

**★★5.** For a limestone layer with 8 per cent porosity containing water, compute
the density, neutron and sonic readings from the demonstration's parameters, then
invert them with a dolomite assumption and report the three errors.

---

**★★6.** A sonic log has a 2 m washed-out interval in which the tool read the mud's
slowness of 660 µs m⁻¹ instead of the formation's 250 µs m⁻¹. Estimate the two-way
time error, convert it to depth at 3000 m s⁻¹, and state how the interval would be
detected from the caliper.

---

## ★★★ Research-oriented

**★★★7.** Set up the density–neutron system for the three unknowns (porosity,
fluid density, fluid hydrogen index) with a known matrix, and show that it is
underdetermined. Then add a stated petrophysical relation between fluid density and
hydrogen index and report the condition number of the resulting system as a
function of the slope of that relation. Identify the slope at which the inversion
becomes ill-conditioned and explain the result physically.

---

**★★★8.** Build a complete synthetic well from rock physics (Gassmann fluid
substitution plus a stated velocity-porosity model), forward-model all four logs
including a 1 m bed and an invaded zone, then run the workflow of
[05-08-07](../07-log-interpretation.md) and report where it fails and by how much.

---

## Reference list used in this problem set

- [05-08-04 lesson](../04-porosity-logs.md)
- [05-04-04 Velocity-Porosity-Clay Models and Empirical Relations](../../04-rock-physics/04-velocity-porosity-clay.md)
- [Solutions](./04-porosity-logs-solutions.md)
