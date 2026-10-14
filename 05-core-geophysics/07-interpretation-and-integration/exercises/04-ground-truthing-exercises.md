# Exercises — 05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core

Attempt these **closed-book** before opening the
[solutions](./04-ground-truthing-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/groundtruth_demo.py`](../code/groundtruth_demo.py) require you to run it
and report its actual output. **Every statement about a well must distinguish
"tested, passed", "tested, failed" and "not tested".**

Constants: $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻²;
$1\ \mathrm{mGal} = 10^{-5}$ m s⁻².

---

## ★ Foundational

**★1.** A model predicts a body at $300 \pm 40$ m (1σ); a well finds it at
$310 \pm 5$ m.

(a) Compute the standardised prediction residual $r$ of the lesson's equation (1).
(b) State whether the model passes at the 5 per cent level.
(c) State what fraction of the residual is contributed by the model uncertainty.

---

**★2.** A seismic average velocity is 5 per cent too high; a reflector is picked
at 2.000 s two-way time.

(a) Compute the true velocity if the measured value is 3000 m s⁻¹.
(b) Compute the depth the wrong velocity gives and the depth the right one gives.
(c) State the sign of the error and one reason a systematic velocity bias is more
dangerous than random noise.

---

**★3.** In three sentences, explain why using a well log as a constraint inside
the inversion removes its value as a ground-truth test.

---

## ★★ Applied

**★★4.** Run [`../code/groundtruth_demo.py`](../code/groundtruth_demo.py).

(a) Compare the surface RMS residuals of cases A and B.
(b) Compare the downhole RMS mismatches as multiples of the station noise.
(c) Compare the implied densities with the core density in each case, and state
which error source dominates in case B.

---

**★★5.** Using equation (4) of the lesson, $|\delta(\Delta\rho)/\Delta\rho| =
|\delta M/M| + 3|\delta R/R|$:

(a) With $\delta R/R = 10$ per cent and $\delta M/M = 5$ per cent, compute the
density uncertainty.
(b) Recompute for $\delta R/R = 20$ per cent.
(c) State the implication for the precision with which a borehole must determine a
body's extent.

---

**★★6.** Design a prediction test for a gravity anomaly with a feasible depth
range of 250–400 m and a mass of $(9 \pm 1)\times10^{9}$ kg.

(a) Write the falsifiable prediction.
(b) State the required precision of the borehole measurement.
(c) State the falsification condition, in the form it would appear in a drilling
proposal *before* the hole is drilled.

---

## ★★★ Research-oriented

**★★★7.** Extend the demonstration to three boreholes in a triangle of 600 m side.

(a) Compute the smallest body each hole can detect, and the joint test's
sensitivity compared with one hole.
(b) Report the reduction in the feasible set.
(c) Discuss whether the reduction justifies the cost, stating the cost model you
assume.

---

**★★★8.** The demonstration discretises each sphere into 257 point masses.

(a) Determine the number of points at which the downhole prediction RMS changes by
less than 1 per cent.
(b) State the discretisation error you would quote for the test.
(c) Explain the difference between this discretisation error and the model error
the test is designed to expose.

---

## Reference list used in this problem set

- [05-07-04 lesson](../04-ground-truthing.md)
- [05-07-03 Integrating Multiple Methods and Constraints](../03-multi-method-integration.md)
- [05-08-01 The Borehole Environment and Invasion Profiles](../../08-geophysical-logging/01-borehole-environment.md)
- [Solutions](./04-ground-truthing-solutions.md)
