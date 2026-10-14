# Exercises — 02-09-04 Gamma-Ray Spectrometry and Natural Radioelements

Attempt these **closed-book** before opening the
[solutions](./04-gamma-spectrometry-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/gamma_spectrometry_demo.py`](../code/gamma_spectrometry_demo.py)
require you to run it and report its actual output. **Every answer must state
which numbers are measured, which are model inputs and which are tabulated.**

Tabulated values to use (state them): $T_{1/2}(^{232}\mathrm{Th}) =
1.405 \times 10^{10}$ a; $T_{1/2}(^{40}\mathrm{K}) = 1.248 \times 10^9$ a;
$T_{1/2}(^{238}\mathrm{U}) = 4.468 \times 10^9$ a; abundance of $^{40}$K
$= 1.17 \times 10^{-4}$; $M(^{232}\mathrm{Th}) = 232.038$ g mol⁻¹;
$M(\mathrm{K}) = 39.0983$ g mol⁻¹; $N_A = 6.022\,140\,76 \times 10^{23}$ mol⁻¹.
$m_ec^2 = 0.510\,998\,95$ MeV.

---

## ★ Foundational

**★1.** (a) Compute the specific activity of 1 ppm of $^{232}$Th in secular
equilibrium, in Bq per kg of rock.
(b) Compare with the widely quoted survey factor of 4.1 Bq kg⁻¹ per ppm Th.
(c) Compute the specific activity of 1 % natural K, in Bq per kg.
(d) Explain in one sentence what "equivalent thorium, eTh" assumes.

---

**★2.** A NaI detector is specified as 7.00 per cent FWHM at 662 keV, and the
resolution is modelled as $\mathrm{FWHM} = k\sqrt E$.

(a) Compute $k$ from the specification.
(b) Compute the FWHM in keV and in per cent at 1460.8 keV.
(c) Compute it at 2614.5 keV.
(d) Explain why the *relative* resolution improves with energy while the
absolute width grows.

---

**★3.** (a) Compute the Compton edge energy for a 2.6145 MeV photon.
(b) Compute it for 1.7645 MeV.
(c) Compute it for 1.4608 MeV.
(d) Using these three numbers and the window definitions (K 1.37–1.57 MeV,
U 1.66–1.86 MeV, Th 2.41–2.81 MeV), explain why the potassium window suffers
least from its own Compton continuum and why the thorium continuum contaminates
the uranium window.

---

## ★★ Applied

**★★4.** Three-window stripping. With $\alpha = 0.36$, $\beta = 0.52$,
$\gamma = 0.74$, the true contributions are $t_\mathrm{K} = 850.0$,
$t_\mathrm{U} = 420.0$, $t_\mathrm{Th} = 260.0$ counts.

(a) Compute the measured window counts $c_\mathrm{K}$, $c_\mathrm{U}$,
$c_\mathrm{Th}$.
(b) Invert the system and recover the three contributions.
(c) Recompute the recovered potassium when $\gamma$ is 1 per cent larger than
assumed, and state the error in counts and in per cent.
(d) Repeat for a 1 per cent error in $\beta$, and state which coefficient the
potassium result is more sensitive to and why.

---

**★★5.** Depth of investigation. The demo computes
$\mu = 0.08369$ cm⁻¹ for the potassium window in soil of density
1.60 g cm⁻³.

(a) Compute $z(0.5)$, $z(0.9)$ and $z(0.99)$ from $z(f) = -\ln(1 - f)/\mu$.
(b) Compare $z(0.9)$ with the commonly quoted "top 30 cm".
(c) Using the thorium $\mu = 0.06018$ cm⁻¹, compute $z(0.9)$ and the ratio to
the potassium value.
(d) Explain why a few centimetres of snow can change the K/Th window ratio
without changing either concentration.

---

**★★6.** Radiogenic heat production. Take $\rho = 2700$ kg m⁻³, $C_\mathrm{K} =
2.5$ %, $C_\mathrm{U} = 2.5$ ppm, $C_\mathrm{Th} = 11.0$ ppm.

(a) Compute $A$ in µW m⁻³ from the tabulated coefficient form.
(b) Compute the percentage contribution of each element.
(c) Compute the implied energy deposited per $^{238}$U decay by dividing the
uranium coefficient by the specific activity per ppm, and state whether the
result is physically sensible.
(d) Explain why the potassium coefficient is the smallest of the three yet the
potassium term can still be a fifth of the total in a rock.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/gamma_spectrometry_demo.py`](../code/gamma_spectrometry_demo.py)
and report:

(a) the three computed specific activities and the three widely quoted factors,
with the percentage differences;
(b) the naively measured and the correctly stripped window counts;
(c) the recovered potassium for a 1 per cent error in each of $\alpha$, $\beta$,
$\gamma$ and in all three;
(d) the infinity-norm condition number of the stripping matrix and of its
inverse, and their product;
(e) the radiogenic heat production computed for granite, and the three
percentage contributions;
(f) the $z(0.9)$ depth for each of the three windows.
(g) Two sentences on which of these outputs are computed, which are tabulated and
which are model inputs.

---

**★★★8.** Interpretation and its limits.

(a) A survey reports 4.2 ppm eU over a granite and 2.1 ppm eU over an adjacent
soil-covered area mapped as the same granite. Give two mechanisms that could
produce the difference without any difference in uranium concentration.
(b) The thorium window has the lowest count rate in a typical survey. Using the
demo's detection-limit logic, explain why that window also has the largest
relative uncertainty in its concentration.
(c) A radiometric map is described in a report as "a map of the potassium
content of the bedrock". Rewrite the sentence correctly in two sentences.
(d) State why the ratio of two windows is more robust to soil moisture than
either window alone.
