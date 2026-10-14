# Exercises — 05-09-03 Geothermal Exploration Geophysics

Attempt these **closed-book** before opening the
[solutions](./03-geothermal-exploration-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/geothermal_demo.py`](../code/geothermal_demo.py) require you to run it and
report its actual output. **Never present a heat-in-place figure as a resource, and
state explicitly which quantities the geophysics cannot measure.**

---

## ★ Foundational

**★1.** State the three requirements of a geothermal resource and which of them
geophysics measures directly.

**★2.** Explain the clay-cap model in three sentences, saying what is conductive and
what is resistive.

**★3.** Compute $H/A$ for $\rho c_p = 2.4\times10^{6}$ J m⁻³ K⁻¹, $h = 200$ m,
$\phi S = 0.04$ and $\Delta T = 150$ K, and state what the number is not.

---

## ★★ Applied

**★★4.** Run [`../code/geothermal_demo.py`](../code/geothermal_demo.py).

(a) Report the measured critical Rayleigh numbers and their agreement with the
closed form and the reference value.
(b) State the caveat the script reports about the numerical method.
(c) Explain why those two numbers are quoted in this repository.

---

**★★5.** For $q = 75$ mW m⁻² and a column of 40 per cent shale
(1.5 W m⁻¹ K⁻¹), 40 per cent sandstone (3.5) and 20 per cent limestone (2.8):

(a) compute $k_\perp$;
(b) compute the temperature at 2 km for a 12 °C surface;
(c) state how much the answer changes if the sandstone fraction were 60 per cent
instead.

---

**★★6.** A prospect has an MT conductive cap from 300 to 900 m and a resistive zone
below. State what that establishes, what it does not, and the two additional
measurements that would most reduce the risk.

---

## ★★★ Research-oriented

**★★★7.** Implement a simple conductive–convective model of a fault-hosted system: a
stated vertical conduit in a conductive half-space. Compute the surface heat-flow
anomaly and the temperature profile in a well 500 m from the fault, compare with a
purely conductive profile, and state the diagnostic that distinguishes them in a
temperature log.

---

**★★★8.** Design an exploration programme for a greenfield prospect: methods,
acquisition parameters, interpretation chain, decision points, and the stated
uncertainty in heat in place and in the probability of permeability. State which
decisions rest on geophysics and which require a well, and what the first well must
measure to be decisive.

---

## Reference list used in this problem set

- [05-09-03 lesson](../03-geothermal-exploration.md)
- [11-04-01 Geophysical Signatures of Geothermal Reservoirs](../../../11-exploration-geophysics/04-geothermal-exploration-geophysics/01-geothermal-signatures.md)
- [Solutions](./03-geothermal-exploration-solutions.md)
