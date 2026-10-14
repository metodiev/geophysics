# Exercises — 05-08-02 Natural Gamma and Spectral Gamma Logging

Attempt these **closed-book** before opening the
[solutions](./02-gamma-logging-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/gamma_demo.py`](../code/gamma_demo.py) require you
to run it and report its actual output. **No API-to-element conversion may be
quoted as universal; state the calibration and the tool kernel for every
resolution claim.**

Constants used where stated: $N_A = 6.02214076\times10^{23}$ mol⁻¹;
$1\ \mathrm{MeV} = 1.602176634\times10^{-13}$ J;
$1\ \mathrm{yr} = 3.155693\times10^{7}$ s.

---

## ★ Foundational

**★1.** State what a natural-gamma tool physically measures, and name three rock
properties it does not measure.

**★2.** For an attenuation length $\lambda = 8$ cm, compute the depths containing
50 and 90 per cent of the count rate.

**★3.** Given a clean baseline of 25 API and a shale baseline of 130 API, compute
$I_{\mathrm{GR}}$ for a reading of 74 API, and $V_{\mathrm{sh}}$ under (a) the
linear relation and (b) $V_{\mathrm{sh}} = 0.33(2^{2I}-1)$.

---

## ★★ Applied

**★★4.** Run [`../code/gamma_demo.py`](../code/gamma_demo.py).

(a) Report the derived coefficients for K, U and Th and the differences from the
conventional set.
(b) Compute the heat production of a rock with 3.0 wt% K, 2.0 ppm U and 8.0 ppm Th
at $\rho = 2650$ kg m⁻³ using both coefficient sets.
(c) State which is more defensible and why.

---

**★★5.** A 0.6 m bed of 140 API lies in a 25 API background. Using the
demonstration's kernel (Gaussian, half-width 0.50 m):

(a) estimate the logged peak by interpolating the measured table;
(b) compute the $V_{\mathrm{sh}}$ error the attenuation would cause, using the
baselines of ★3 and the linear relation;
(c) state the direction of the bias.

---

**★★6.** Explain, in terms of the hydrogen index and the attenuation length, why
the uranium window needs a longer counting time than the potassium window for the
same precision in a typical formation.

---

## ★★★ Research-oriented

**★★★7.** Uranium-series disequilibrium is common in organic-rich mudstones.
Construct a two-box model (uranium in the rock, radon partially expelled) and
compute the bias in the "uranium" window reading as a function of the expelled
fraction. State what measurement would detect the disequilibrium, and how you would
report it.

---

**★★★8.** Using the derived coefficient set, integrate the heat production of a
layered crustal column from a synthetic spectral log that you define, and compare
the resulting surface heat flow with a measured value. State every assumption and
quantify the largest one.

---

## Reference list used in this problem set

- [05-08-02 lesson](../02-gamma-logging.md)
- [12-03-01 Radiogenic Heat Production and Mantle Geotherms](../../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md)
- [Solutions](./02-gamma-logging-solutions.md)
