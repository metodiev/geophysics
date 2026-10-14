# Exercises — 03-01-01 Why Python for Geophysics: The Scientific Ecosystem

Attempt these **closed-book** before opening the
[solutions](./01-why-python-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/why_python_demo.py`](../code/why_python_demo.py) or
[`../code/geophys_core.py`](../code/geophys_core.py) require you to run them and
report their **actual** output. Anything you compute, compute with units, and
state the units in your answer.

---

## ★ Foundational

**★1.** A compact body is modelled as a sphere of radius $a = 150$ m with excess
density $\Delta\rho = 250$ kg m⁻³ at centre depth $z = 400$ m. Use
$G = 6.67430\times10^{-11}$ m³ kg⁻¹ s⁻².

(a) Compute the mass contrast $M = \frac{4}{3}\pi a^3 \Delta\rho$.
(b) Compute the peak vertical anomaly at the epicentre,
$g = GM/z^2$, in m s⁻² and in mGal (1 mGal $= 10^{-5}$ m s⁻²).
(c) Verify both answers by importing `sphere_mass` and `sphere_anomaly_mgal` from
`geophys_core` and printing them.

---

**★2.** For the body of ★1:

(a) Without recomputing, state the peak anomaly if the same *mass* were moved to
$z = 800$ m. Give the reason in one sentence.
(b) Verify (a) with `sphere_anomaly_mgal`.
(c) At what surface offset is the anomaly equal to half its peak value? Express
the answer in metres and as a multiple of $z$, and say which property of the curve
this demonstrates.

---

**★3.** Classify each task by the ecosystem layer that owns it. Give one library
name for each, and say why the neighbouring layer is *not* the right place.

(a) Subtract two 10⁸-element arrays.
(b) Fit a curve to 15 measurements with uncertainties.
(c) Read a miniSEED waveform and remove the instrument response.
(d) Group a 10⁵-row catalogue by station and average the magnitudes.
(e) Draw a map of a gravity anomaly with a colour bar and a coastline.

---

## ★★ Applied

**★★4.** Run `python3 why_python_demo.py` and report:

(a) the mass contrast and peak anomaly of its synthetic body;
(b) the number of stations, the wall-clock time and the per-station cost;
(c) the interpreter version printed by the script.

Then answer: **at the measured per-station cost, how long would one billion
stations take?** Give the answer in seconds and in hours, and state the two
assumptions in that extrapolation.

---

**★★5.** The demo's synthetic line is 4 km long with 200 000 stations.

(a) Why is that station spacing physically absurd?
(b) Compute the spacing in metres.
(c) The demo's comment says the spacing is chosen "to make the timing measurable
on a laptop". Rewrite the demo's timed section so that it uses a realistic spacing
of 20 m over 4 km, and report the measured time. Explain why that measurement is
less useful as a *benchmark* even though it is the more realistic survey.

---

**★★6.** A relative gravimeter has a repeatability of 10 µGal and the target
anomaly of ★1 must be detected at three times that level.

(a) Convert 10 µGal to mGal.
(b) Compute the minimum excess density $\Delta\rho$ for a sphere of radius 500 m
at centre depth 2 km to produce a peak anomaly of 30 µGal.
(c) Is that density contrast geologically plausible for a crustal rock? State your
criterion explicitly (compare against a nominal crustal density of 2670 kg m⁻³ and
against the density of iron).

---

## ★★★ Research-oriented

**★★★7.** Invert the peak anomaly for depth. For a body with $a = 200$ m and
$\Delta\rho = 300$ kg m⁻³, the peak is $g = GM/z^2$.

(a) Derive $\mathrm{d}z/\mathrm{d}g$ and evaluate it in metres per mGal for
$z = 400$ m using the $g$ from ★1(b).
(b) A survey measures the peak with a 0.5 µGal uncertainty. What depth
uncertainty does that imply at $z = 400$ m?
(c) A geologist is confident in $a$ to ±10 per cent and in $\Delta\rho$ to
±20 per cent. Propagate those to a depth uncertainty at $z = 400$ m. State
whether the geometric/parameter uncertainty or the measurement uncertainty
dominates.

---

**★★★8.** Write a one-page (350–450 word) instrument specification for
`why_python_demo.py`'s forward model, using the five properties from §1 of the
lesson: specification, calibration, precision, failure mode and cost. For each,
state the property **and** how you would *test* or *measure* it. The failure-mode
section must name at least three input classes the current code does not detect.

---

**★★★9.** The demo reports a mean anomaly over the line of 0.065094 mGal and a
peak of 0.268390 mGal. Design a second model — a horizontal cylinder rather than a
sphere — and, *before* coding it, predict whether its mean-to-peak ratio over a
4 km line would be larger or smaller than the sphere's. Then implement it (the
vertical anomaly of a horizontal cylinder of radius $a$ at depth $z$ is
$g = 2\pi G a^2 \Delta\rho\, z/(x^2 + z^2)$ with the same $\Delta\rho$) and test
your prediction. Report both ratios and whether you were right.
