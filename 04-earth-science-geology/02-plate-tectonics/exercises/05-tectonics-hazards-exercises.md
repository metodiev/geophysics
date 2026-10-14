# Exercises — 04-02-05 Tectonics and the Distribution of Earthquakes and Volcanoes

Attempt these **closed-book** before opening the
[solutions](./05-tectonics-hazards-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/tectonics_hazards_demo.py`](../code/tectonics_hazards_demo.py) require
you to run it and report its actual output. Use $\mu = 3\times10^{10}$ Pa,
$g = 9.81$ m/s², $3.15576\times10^7$ s per year and
$M_0 = 10^{1.5M_w+9.1}$ N·m.

---

## ★ Foundational

**★1.** A catalogue is complete above magnitude 4.0 with 20 events per year.

(a) Using $b = 1$, compute the rate of $M \ge 6$.
(b) Compute the mean recurrence interval.
(c) Compute the probability of at least one such event in 50 years, using
$P = 1 - e^{-\text{rate}\times T}$.
(d) State why the probability is not exactly 1 even though the interval is 5
years.

---

**★2.** Repeat for magnitude 7.

(a) Compute the rate.
(b) Compute the interval and $P(\ge 1 \text{ in } 50 \text{ a})$.
(c) Compare the probability with the interval divided by the window, and explain
the difference.
(d) State which of the two numbers an engineering decision uses.

---

**★3.** Tsunami speed.

(a) Compute $c = \sqrt{gh}$ for $h = 3000$ m, in m/s and km/h.
(b) Compute the travel time over 6000 km in hours.
(c) Compute $c$ for $h = 200$ m.
(d) State why the speed does not depend on the wave's amplitude or period.

---

## ★★ Applied

**★★4.** A $b$-value by maximum likelihood: $b = \log_{10}e/(\bar M - M_c)$.

(a) A catalogue complete above $M_c = 3.0$ has a mean magnitude of 3.43. Compute
$b$.
(b) Compute it for a mean magnitude of 3.60.
(c) Compute it for a mean magnitude of 3.30.
(d) State which of the three corresponds to a catalogue that is *incomplete*,
and why.

---

**★★5.** Completeness bias. The same catalogue is analysed at $M_c = 3.2$.

(a) Compute the $b$-value with the mean magnitude unchanged at 3.43.
(b) State the direction of the bias relative to ★★4(a).
(c) State how the implied rate of $M \ge 6$ changes.
(d) State what a completeness analysis is and why it is not optional.

---

**★★6.** Shoaling.

(a) Compute the amplification $H_2/H_1 = (h_1/h_2)^{1/4}$ for $h_1 = 5000$ m and
$h_2 = 25$ m.
(b) Compute the offshore wave height that becomes 9 m at the coast.
(c) Recompute (a) for $h_1 = 4000$ m.
(d) State two effects Green's law ignores, and whether each would raise or lower
the coastal height.

---

## ★★★ Research-oriented

**★★★7.** A moment-balanced recurrence. A 600 km long megathrust has a 120 km
seismogenic width and converges at 70 mm/a.

(a) Compute its moment rate in N·m per year.
(b) Using the balancing relation
$$10^a = \frac{\dot M_0}{2\cdot10^{9.1}\left(10^{0.5M_\text{max}}
- 10^{0.5M_\text{min}}\right)}$$
with $b = 1$, $M_\text{min} = 6.0$ and $M_\text{max} = 9.5$, compute $a$.
(c) Compute the mean interval of $M_w \ge 8$ events.
(d) Recompute (c) with a coupling coefficient of 0.6.
(e) State what the naive calculation — attributing the whole budget to $M_w$ 8 —
would give, and why it is a *lower bound* on the interval.

---

**★★★8.** Run
[`../code/tectonics_hazards_demo.py`](../code/tectonics_hazards_demo.py) and
report:

(a) the recovered $b$-value from the complete catalogue and from the incomplete
catalogue analysed at the wrong and right completeness magnitudes;
(b) the rate, interval and $P(\ge 1 \text{ in } 50 \text{ a})$ rows for $M$ 5, 7
and 9;
(c) the area, the moment rate per second and per year, and the Gutenberg–Richter
intercept $a$;
(d) the rates and intervals for $M \ge 6, 7, 8, 9$ from the balanced calculation;
(e) the naive single-magnitude intervals for $M_w$ 7.5 to 9;
(f) the tsunami speed and travel time over 8000 km at depths 4000 and 5000 m, and
the shoaling factor from 4000 m to 20 m;
(g) three sentences on which numbers are computed, which are tabulated, and which
are labelled illustrative.

---

**★★★9.** The coupling coefficient. A margin's seismicity releases only part of
its convergence.

(a) State three mechanisms by which the aseismic fraction is accommodated.
(b) State how each affects the recurrence interval of large earthquakes.
(c) State how each affects the *maximum* magnitude a margin can produce.
(d) State what a hazard assessment must therefore measure rather than assume, and
name one observation that constrains it.
