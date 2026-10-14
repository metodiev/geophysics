# Exercises — 02-03-08 Reflection, Refraction and Snell's Law for Waves

Attempt these **closed-book** before opening the
[solutions](./08-reflection-refraction-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/reflection_refraction_demo.py`](../code/reflection_refraction_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** A wave in water ($c_1 = 1500$ m s⁻¹) strikes a limestone interface
($c_2 = 3000$ m s⁻¹) at 20°.

(a) Compute the transmitted angle.
(b) Compute the critical angle.
(c) Compute the horizontal slowness and verify that it is the same on both sides.
(d) State what happens at 45° incidence.

---

**★2.** Two media: $Z_1 = 4.0$ MRayl and $Z_2 = 7.5$ MRayl.

(a) Compute the velocity and pressure reflection coefficients.
(b) Compute the transmission coefficients in both conventions.
(c) Compute the reflected and transmitted energy fractions and verify their sum.
(d) State the polarity you would see on a velocity seismogram and on a
hydrophone record, and explain the difference.

---

**★3.** Derive the law of reflection from the phase-matching argument of §3.1 by
equating the $x$-dependence of the incident and reflected waves.

(a) Write the two fields explicitly.
(b) Show that $\theta_r = \theta_1$ as a consequence.
(c) Explain in one sentence why this derivation does not require any assumption
about the amplitudes.

---

**★4.** A layer sequence has $v_p$ increasing with depth: 1500, 2000, 2500, 3000
m s⁻¹.

(a) Compute the critical angle at each interface for a ray starting in the top
layer.
(b) Compute the ray parameter corresponding to the deepest critically refracted
ray that returns to the surface.
(c) State whether a ray can be critically refracted from the *first* interface
into the second layer.
(d) State what the transmitted ray's angle in the deepest layer would be if the
ray parameter were at the first interface's critical value.

---

## ★★ Applied

**★★5.** Run the demo's normal-incidence section.

(a) Report the measured and predicted $R$ and $T$, and the differences.
(b) Report the measured arrival times and compare with the predictions.
(c) Explain why the incident amplitude is 0.499651 rather than 1, and why that
does not affect the measured coefficients.
(d) State the largest source of error in the measurement and how you could reduce
it.

---

**★★6.** A seismic reflection survey images a shale (2400 kg m⁻³, 2500 m s⁻¹)
overlying a sand.

(a) For a water-saturated sand (2300 kg m⁻³, 2800 m s⁻¹), compute $Z_1$, $Z_2$
and $R_p$.
(b) For a gas-saturated sand (2000 kg m⁻³, 2200 m s⁻¹), compute $R_p$ and its
sign.
(c) Compute the reflected energy fraction in both cases and state which is the
"bright spot".
(d) Explain why the *polarity* is a more robust fluid indicator than the
amplitude when the overburden is unknown.

---

**★★7.** A refraction survey over a two-layer subsurface has a direct arrival at
1500 m s⁻¹ and a head wave at 3000 m s⁻¹, with the crossover distance measured at
60 m.

(a) Compute the critical angle.
(b) Derive the crossover distance for a two-layer model,
$x_c = 2h\sqrt{(v_2+v_1)/(v_2-v_1)}$, and solve for the depth $h$.
(c) Compute the intercept time and state how it constrains $h$ independently.
(d) State the error in $h$ if the direct arrival's velocity were overestimated by
5 per cent.

---

**★★8.** Run the demo's oblique section.

(a) Report the residual magnitudes at 0°, 30° and near the critical angle.
(b) Explain what those residuals prove and what they do not prove.
(c) Report $R_p$ at 0°, 15°, 30° and near-critical, and state whether $R_p$
increases or decreases with angle here, and why.
(d) Explain why $R_p \to -1$ at grazing incidence by reference to equation (9) of
the lesson.

---

## ★★★ Research-oriented

**★★★9.** The full elastic problem at a solid–solid interface.

(a) Write down the four waves that exist for an incident P wave at oblique
incidence, and state what quantity each carries.
(b) State the four boundary conditions (continuity of normal and tangential
traction, and of normal and tangential displacement) and explain why there are
exactly four.
(c) Show that at normal incidence the S terms decouple and the P reflection
coefficient reduces to $(Z_1^p - Z_2^p)/(Z_1^p + Z_2^p)$ with $Z^p = \rho v_p$.
(d) For the shale-over-sand cases of ★★6, compute the normal-incidence
coefficients using $v_p$ and compare with the acoustic values; state when the
difference matters.

---

**★★★10.** A thin layer of thickness $h$ and impedance $Z_2$ lies between media of
impedance $Z_1$ and $Z_3$.

(a) Show by summing the geometric series of internal reflections that the
composite reflection coefficient is
$R = (r_{12} + r_{23}e^{-i2k_2h})/(1 + r_{12}r_{23}e^{-i2k_2h})$ with
$r_{ij} = (Z_i - Z_j)/(Z_i + Z_j)$.
(b) Show that for $Z_1 = Z_3 \ne Z_2$ this reduces to $R = r_{12}(1-e^{-i2k_2h})/
(1 - r_{12}^2e^{-i2k_2h})$ and that $|R|$ oscillates with $h$ with period
$\lambda_2/2$.
(c) Show that the maximum $|R|$ occurs at $h = \lambda_2/4$ and compute its value
for $Z_1 = Z_3 = 6$ MRayl and $Z_2 = 3$ MRayl.
(d) Write a program that computes $|R(h)|$ for that case, measures the position of
the first maximum and reports it against $\lambda_2/4$.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
