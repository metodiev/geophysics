# Exercises — 05-03-02 Analytical Solutions for Simple Bodies

Difficulty: ★ · ★★ · ★★★. Use $G = 6.67430\times10^{-11}$ SI,
$1\ \mathrm{mGal} = 10^{-5}$ m/s².

---

## ★ Foundational

**★1.** Write the sphere and 2-D line-mass gravity formulas, naming each symbol
with its unit.

**★2.** State the two half-width constants (sphere, cylinder) and explain why
they differ.

**★3.** A measured half-width is 600 m. Compute the implied depth under a sphere
assumption and under a cylinder assumption.

---

## ★★ Applied

**★★4.** A sphere of radius 80 m has density contrast 400 kg/m³ at 300 m depth.
Compute its excess mass and peak anomaly, and its half-width.

**★★5.** A prism with half-extents (80, 60, 50) m and vertical magnetisation has
a moment equal to that of a dipole. At what distance does the dipole
approximation reach 1% accuracy, on the symmetry axis? State the measured
convergence exponent and why it is 2 rather than 1.

**★★6.** Explain why the sheet solution and the line-mass solution are related,
and derive one from the other for a semi-infinite sheet.

**★★7.** A dyke anomaly is interpreted with a cylinder depth rule. If the true
body is a dyke (near-2-D), state the direction of the depth error from using the
cylinder formula versus the sphere formula.

---

## ★★★ Research-oriented

**★★★8.** Numerical benchmark study. For a homogeneous prism, compare the closed
form with (a) volume quadrature and (b) the point-mass/dipole far-field
approximation, over a range of depths. Report the depth at which the far-field
approximation reaches 1%, 5% and 10% relative error, and explain the scaling of
the error with distance in terms of the multipole expansion. State which method
you would use as the reference for a production code and why.

**★★★9.** Depth-rule sensitivity. Generate synthetic anomalies for a sphere, a
cylinder and a prism, all with the same peak amplitude and the same depth, and
extract the depth from each using both the sphere and the cylinder half-width
rules. Tabulate the four combinations of true shape and assumed shape, report
the fractional depth error in each, and conclude with a sentence on what a
potential-field depth estimate is actually reporting.
