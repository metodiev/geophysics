# Exercises — 04-07-02 Volcanic Hazards, Monitoring and Precursors

Attempt these **closed-book** before opening the
[solutions](./02-volcanic-hazards-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/volcanic_hazards_demo.py`](../code/volcanic_hazards_demo.py) require
you to run it and report its actual output.

---

## ★ Foundational

**★1.** A magma body is modelled as a pressurised spherical cavity of radius
$a = 500$ m in rock of shear modulus $\mu = 25$ GPa, with an overpressure
$\Delta P = 20$ MPa, at a depth of 2 km.

(a) Compute the wall displacement and the cavity volume change.
(b) Compute the Mogi strength $C$ and verify the ratio $C/\Delta V = 3/(4\pi)$.
(c) Compute the maximum surface uplift and the uplift at a radial distance of
4 km.
(d) Show that $u_r = u_z$ at $r = d$ and verify it numerically from (3).

---

**★2.** A buoyant plume obeys $H = C(F/N^3)^{1/4}$.

(a) Compute the change in column height if the buoyancy flux doubles.
(b) Compute the change in buoyancy flux required for the column height to
increase by 50 per cent.
(c) State which of the two quantities in (a) and (b) is a measurement and which
is an inference.
(d) State which part of the relation dimensional analysis does not determine.

---

**★3.** An SO₂ measurement gives a line-averaged concentration of
$5\times10^{-4}$ kg m⁻³ across a plume 2 km wide, with a cross-plume wind speed
of 8 m s⁻¹.

(a) Compute the mass flux in kg s⁻¹.
(b) Convert it to tonnes per day.
(c) State which of the three factors in the flux is usually taken from a model
rather than measured, and why that matters.

---

**★4.** A volcano has an annual eruption probability of 0.02. A precursor has a
sensitivity of 0.8 and a false-alarm rate of 0.1.

(a) Compute the probability of an eruption given that the precursor appears.
(b) Compute the false-alarm rate required for that probability to be 0.9.
(c) Compute the same for a target of 0.99.
(d) State, in one sentence, why the answer to (b) and (c) is the hard part of
forecasting.

---

## ★★ Applied

**★★5.** Run the demo's section 1.

(a) Report the wall displacement, the cavity volume change, the Mogi strength and
the ratio $C/\Delta V$.
(b) Report the maximum uplift and the value of $r$ at which $u_r = u_z$.
(c) Report the location and value of the peak tilt.
(d) Now change the source depth to 6 km, keeping $C$ fixed. Predict the new
uplift and the new peak tilt before running it, then verify. State the two
scaling laws you used.

---

**★★6.** Run the demo's section 2.

(a) Report the gravity change for the 1 km radius body at 3 km depth, and the
values at 5 km and 10 km.
(b) Compute the density change that would be needed at 5 km depth to produce
100 µGal.
(c) Explain why a repeat microgravity survey is more sensitive to a shallow
intrusion than a deep one, and state the scaling.
(d) A gravimeter repeatability of 5 µGal is quoted. Compute the depth at which
the body of part (a) falls to that level.

---

**★★7.** For each of the following, compute the posterior probability of an
eruption given a precursor, and comment on which case could support an
evacuation decision:

| $p$ (annual) | sensitivity | false-alarm rate |
|---|---|---|
| 0.001 | 0.90 | 0.05 |
| 0.01 | 0.90 | 0.05 |
| 0.05 | 0.95 | 0.02 |

Then compute the probability of an eruption given the *absence* of the
precursor for the middle row, using the same numbers, and state what that tells
you about the value of the monitoring.

---

## ★★★ Research-oriented

**★★★8.** A volcano inflates. Two hypotheses are considered: (A) new magma is
intruded, with a density contrast of $+300$ kg m⁻³ relative to the displaced
host rock; (B) the volume change is caused by exsolution and expansion of a gas
phase already present, with an effective density contrast of $-100$ kg m⁻³.

(a) Derive the ratio $\Delta g/u_z$ for a Mogi source plus a compact mass change
at the same depth, and show that it is independent of the depth.
(b) Evaluate it numerically in µGal per metre of uplift for both hypotheses.
(c) For an observed uplift of 0.15 m, compute the expected gravity change for
each hypothesis.
(d) State what a measured gravity change can therefore distinguish that the
uplift alone cannot, and name one assumption that would break the diagnostic.

---

**★★★9.** The false-alarm rate of a precursor is estimated from $n$ monitoring
intervals as a proportion. Treat the number of false alarms as binomial.

(a) Compute the number of intervals required for a standard error of 0.005 when
the rate is 0.05, and the number for a standard error of 0.01.
(b) Compare that with the number of years for which a single newly instrumented
volcano is likely to have comparable-quality records, and state the implication
for its ability to issue a quantified forecast.
(c) Discuss, in no more than five sentences, what pooling records across many
volcanoes would require to be legitimate, and what it would cost if that
assumption were false.
(d) Suggest one design change to a monitoring programme that would improve the
false-alarm statistics faster than adding another instrument to the same
volcano.
