# Exercises — 02-04-02 Strain: Infinitesimal Strain Tensor and Compatibility

Attempt these **closed-book** before opening the
[solutions](./02-strain-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/strain_demo.py`](../code/strain_demo.py) require
you to run it and report its actual output.

---

## ★ Foundational

**★1.** A displacement field is $\mathbf u = (ax+by,\ cx+dy,\ 0)$ with
$a = 0.002$, $b = 0.001$, $c = -0.001$, $d = 0.003$.

(a) Compute the strain tensor.
(b) Compute the rotation tensor and the rotation vector.
(c) Compute the dilatation.
(d) State whether the deformation is pure strain, pure rotation, or both.

---

**★2.** For the strain tensor

$$\boldsymbol{\varepsilon} = \begin{pmatrix} 5 & 2 & 0\\ 2 & -3 & 0\\ 0 & 0 & 1
\end{pmatrix}\times10^{-4}$$

(a) Compute the principal strains.
(b) Compute the volumetric strain.
(c) Compute the maximum shear strain.
(d) Identify the principal directions in the $xy$ plane.

---

**★3.** A 30 cm long concrete core shortens by 0.045 mm under load.

(a) Compute the axial strain in microstrain.
(b) State whether this is small enough for the infinitesimal tensor, and justify
the answer with a number.
(c) The core also dilates laterally by 0.012 mm over the same length. Compute the
lateral strain and the ratio of lateral to axial strain.
(d) State what that ratio is called and what it measures.

---

**★4.** A body is rotated rigidly by 5° about the $z$-axis.

(a) Write the displacement field.
(b) Compute the apparent $\varepsilon_{xx}$ from the infinitesimal tensor.
(c) Compare with $\theta^2/2$ and report the relative difference.
(d) State the size of the error in the strain one would report if this rotation
were mistaken for a deformation.

---

## ★★ Applied

**★★5.** Run the demo's strain section.

(a) Report the numeric strain tensor and the maximum difference from the analytic
value.
(b) Report the rotation vector and the dilatation, and verify the latter against
the analytic expression.
(c) Explain why the rotation components are of the same size as the strain
components in this field.
(d) State what would change in the strain tensor if the whole field were rotated
by 10° about the $z$-axis.

---

**★★6.** Run the demo's convergence section.

(a) Report the errors and the measured orders.
(b) Derive the expected order analytically from the central-difference error term.
(c) Predict the error at $h = 3.125\times10^{-4}$ and verify.
(d) At what $h$ would round-off begin to dominate, given that the displacement
components are of order $10^{-2}$ m in double precision?

---

**★★7.** A GNSS network has 20 stations with 1 mm horizontal position precision
per epoch, spread over a 50 km × 50 km region.

(a) Estimate the precision of a strain component computed from the two most
distant stations.
(b) Estimate the precision from the *median* station spacing (take 15 km).
(c) Reduce the epoch-to-epoch noise to 0.2 mm by averaging a decadal time series
and recompute (a) and (b).
(d) State which spacing you would use for a regional strain map and why, referring
to the trade-off between noise and spatial resolution.

---

**★★8.** A measured 2-D strain field is reported as
$\varepsilon_{xx} = 0.5y$, $\varepsilon_{yy} = 0.5x$, $\varepsilon_{xy} = 0$.

(a) Test the compatibility condition and report the residual.
(b) State whether a displacement field exists for it.
(c) If the true field were $\varepsilon_{xx} = 0.5y$, $\varepsilon_{yy} = -0.5y$,
$\varepsilon_{xy} = 0$, retest and state whether it is compatible.
(d) Explain the practical consequence: which class of measured strain fields can be
integrated to a displacement, and what must be done with the others?

---

## ★★★ Research-oriented

**★★★9.** Finite strain measures.

(a) For a 1-D extension $\delta$ over an initial length $L$, write the
infinitesimal strain, the Green (Lagrangian) strain
$E = \frac12[(\ell/L)^2-1]$ and the logarithmic (Hencky) strain
$H = \ln(\ell/L) = \ln(1+\delta/L)$, and expand each to second order in
$\varepsilon = \delta/L$.
(b) Tabulate the three for $\varepsilon = 0.001$, $0.01$, $0.1$, $0.5$ and $1.0$
and report the maximum difference between the measures at each level.
(c) State the strain magnitude at which the infinitesimal measure is in error by
more than 1 per cent, and comment on whether seismic or tectonic deformation
crosses that threshold.
(d) Show that different finite-strain measures disagree with each other at second
order, and explain why the choice of measure must be stated in a finite-strain
analysis.

---

**★★★10.** A strain rosette consists of three strain gauges at 0°, 45° and 90°.

(a) Show that the measured strains $\varepsilon_{0},\varepsilon_{45},
\varepsilon_{90}$ determine the 2-D strain tensor completely, and write the
inversion explicitly.
(b) Given $\varepsilon_0 = 120\ \mu\varepsilon$,
$\varepsilon_{45} = 40\ \mu\varepsilon$,
$\varepsilon_{90} = -20\ \mu\varepsilon$, compute the tensor, the principal
strains and their directions.
(c) Derive the propagation of independent gauge errors $\sigma$ into the principal
strains and state which combination is best determined and which worst.
(d) Write a program that simulates the measurement with 5 $\mu\varepsilon$ Gaussian
noise on each gauge, repeats 500 times with a deterministic generator, and reports
the standard deviation of each principal strain and of the principal angle.
Comment on the precision of the principal angle when the two principal strains are
nearly equal.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
