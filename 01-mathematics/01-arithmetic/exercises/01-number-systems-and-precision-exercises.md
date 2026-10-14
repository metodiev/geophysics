# Exercises — 01-01-01 Number Systems, Precision and Scientific Notation

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-number-systems-and-precision-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Write each number in scientific notation with **3 significant figures**.

(a) 0.000482
(b) 91 300
(c) 0.6071
(d) 4 500 000

---

**★2.** Convert each gravity value to SI (m/s²), then to µm/s².
Use $1\ \mathrm{Gal} = 10^{-2}\ \mathrm{m\,s^{-2}}$ and $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

(a) 15.2 mGal
(b) −3.7 mGal
(c) 1.05 Gal

---

**★3.** State the number of significant figures, and say whether each value is
ambiguous as written.

(a) `0.00340`
(b) `1.20×10⁴`
(c) `700`
(d) `7.00×10²`

---

**★4.** Compute and give the answer with the **correct** number of significant
figures, stating which rule you applied.

(a) $4.56 \times 2.1$
(b) $12.5 \div 0.25$
(c) $101.3 + 0.44$

---

## ★★ Applied

**★★5.** A magnetic anomaly is reported as `−1250 nT`.

(a) Express it in tesla.
(b) Express it in gammas, given $1\ \gamma = 1\ \mathrm{nT}$.
(c) The magnetometer resolves 1 nT. How many significant figures may you
defensibly quote, and why?

---

**★★6.** A seismic wave travels 412 km in 68.4 s.

(a) Compute the average velocity in km/s and in m/s.
(b) State the number of significant figures your inputs justify.
(c) Explain specifically why reporting `6.02339 km/s` would be wrong — give a
physical argument, not just "too many digits".

---

**★★7.** A buried body of mass $10^{10}$ kg produces a peak surface gravity
anomaly of exactly 0.05 mGal. Using the point-mass approximation
$g_z = GM/d^{2}$ with $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$:

(a) Estimate $d$ in orders of magnitude first.
(b) Then compute $d$ exactly (in metres and kilometres).
(c) Assuming a density of 3000 kg/m³, estimate the body's radius. Is the
point-mass approximation justified? Support your answer with the ratio $d/R$.
(d) Does the answer depend on whether the body is a sphere or a cube? Explain.

---

**★★8.** A survey grid measures $1.25\ \mathrm{km} \times 0.80\ \mathrm{km}$,
where each dimension is known only to 2 significant figures.

(a) Compute the area exactly as a product of the given numbers.
(b) Give the area in km² and m² using the significant-figures rule.
(c) Now propagate the uncertainty properly, assuming each dimension carries
±0.005 km. Give the relative and absolute uncertainty of the area.
(d) Compare (b) and (c). Which is more informative, and why?

---

## ★★★ Research-oriented

**★★★9.** The supplied demonstration
(`code/number_systems_demo.py`, Section 4) reports that naive summation of
100 000 copies of 0.1 gives an error of about $1.9\times10^{-8}$, while
Kahan-compensated summation is exact.

Design and run an experiment measuring how the naive error grows with $n$:

(a) For $n \in \{10^{3}, 10^{4}, 10^{5}, 10^{6}, 10^{7}\}$, record the error of
naive summation against the exact `Decimal` result.
(b) Plot error versus $n$ on log–log axes and fit a power law. Report the
empirical exponent.
(c) Explain the mechanism. Specifically: the rounding error introduced at step
$k$ scales with the partial sum (roughly $0.1k$), so if all errors accumulated
with the same sign the total would grow as $n^{2}$. Do your data support
$n^{2}$, or is growth slower? If slower, what does that tell you about the
signs of the individual rounding errors?
(d) State the limits of your conclusion: does the exponent you measured depend
on the value being summed, on the summation order, or on the platform?

This is a genuine numerical-experiment report. Write it up with method, result,
and stated limitations.

---

**★★★10.** The gravitational constant is
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ with a relative
standard uncertainty of about $2.2\times10^{-5}$. A student estimates a body's
mass from measured $g_z$ and $d$ using $M = g_z d^{2}/G$ and reports 8
significant figures.

(a) What relative standard uncertainty in $M$ does the uncertainty in $G$ alone
impose?
(b) If $g_z$ and $d$ were each known to 1% relative uncertainty, what is the
relative uncertainty in $M$? (Treat the uncertainties as independent and
combine in quadrature.)
(c) How many significant figures should the student have reported?
(d) Write three or four sentences of constructive feedback to the student.

---

## Extension ideas

- Repeat ★2 for magnetic units: express `500 nT`, `25 000 nT`, and `0.05 mT`
  all in tesla, and decide which SI prefix is most readable for each.
- Rewrite the point-mass feasibility calculation in ★7 as a function
  `detectability(mass_kg, depth_m, resolution_mgal)` returning a boolean, and
  find the depth at which a $10^{9}$ kg body becomes undetectable at 0.01 mGal
  resolution. This is a first *forward model* and previews
  [07-gravity-geodesy](../../../07-gravity-geodesy/README.md).
