# Exercises — 02-03-10 Attenuation, Absorption and the Quality Factor Q

Attempt these **closed-book** before opening the
[solutions](./10-attenuation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/attenuation_demo.py`](../code/attenuation_demo.py) require you to run it
and report its actual output.

---

## ★ Foundational

**★1.** A rock has $Q = 80$, $v = 3200$ m s⁻¹.

(a) Compute $\alpha$ at 10 Hz and at 50 Hz.
(b) Compute the decay length $1/\alpha$ at each frequency.
(c) Compute the amplitude ratio over 2 km at each frequency.
(d) State which frequency survives the path better and by what factor.

---

**★2.** A wave has amplitude 1.00 at $x = 0$ and 0.25 at $x = 500$ m, at 30 Hz in
a medium with $v = 2500$ m s⁻¹.

(a) Compute $\alpha$, assuming all the loss is intrinsic.
(b) Compute $Q$.
(c) Compute the wavelength and the decay per wavelength.
(d) State two other mechanisms that could explain the decay and how you would test
for them.

---

**★3.** Show that $\alpha\lambda = \pi/Q$ and use it to compute the amplitude ratio
per wavelength for $Q = 20, 100, 500$.

(a) Report the three ratios.
(b) Convert each to dB per wavelength using 8.686$\alpha\lambda$.
(c) State the decay length in wavelengths for each.
(d) State which of these rocks a 3 km reflection survey at 30 Hz could image
through, given a dynamic range of 60 dB.

---

**★4.** A damped wave simulation has $\beta = 2.0$ s⁻¹ at a frequency of 40 rad s⁻¹
and satisfies $u_{tt} + 2\beta u_t = c^2u_{xx}$.

(a) Compute $Q$ from $Q = \omega/(2\beta)$.
(b) Compute the amplitude decay per period and per wavelength (take
$c = 2000$ m s⁻¹).
(c) State whether the dashpot model gives a frequency-independent $Q$ and what
that implies for broadband data.
(d) State what model would be needed for a nearly constant $Q$.

---

## ★★ Applied

**★★5.** Run the demo's decay-rate measurement.

(a) Report the measured decay rate, the input $\beta$, and the measured and
predicted $Q$.
(b) Report the peak amplitudes per period and verify that the ratios are
consistent with a constant decay rate.
(c) Explain why the measured decay rate differs from the input by 0.03 per cent,
in terms of the integrator.
(d) Predict what happens if the damping is raised to $\beta = 8.0$ s⁻¹ and verify
by running.

---

**★★6.** A spectral-ratio measurement is made between receivers 1000 m apart in a
medium with $v = 3000$ m s⁻¹.

(a) Derive the relation between the slope of $\ln(A_1/A_2)$ against frequency and
$Q$, and state the units of the slope.
(b) For $Q = 50$, compute the slope.
(c) Compute the ratio $A_1/A_2$ at 5, 20 and 50 Hz.
(d) State how an error of 5 per cent in $v$ propagates into $Q$ and how an error
in the receiver separation propagates into it.

---

**★★7.** Run the demo's spectral-ratio section with noise.

(a) Report the recovered $Q$ and the fit residual for the three noise levels.
(b) Explain why 1 per cent amplitude noise moves $Q$ by only 0.5 per cent here,
in terms of the number of frequencies fitted.
(c) Predict the effect of halving the receiver separation on the recovered $Q$'s
sensitivity to noise, and verify by modifying the script.
(d) State the three corrections that would dominate the error in a field
measurement of the same $Q$.

---

**★★8.** A medium conforms to the nearly-constant-$Q$ model with $Q = 60$ and a
reference velocity 3000 m s⁻¹ at 10 Hz.

(a) Compute the velocity at 1 Hz and at 100 Hz using equation (6) of the lesson.
(b) Compute the fractional velocity difference across the band.
(c) Compute the travel-time difference over a 100 km path that results, and state
whether it is measurable.
(d) Explain why ignoring this dispersion would bias a tomographic inversion that
used phase arrivals.

---

## ★★★ Research-oriented

**★★★9.** A regional dataset has amplitudes at several distances and frequencies.

(a) Write down the full amplitude model
$A(f,x) = S(f)G(x)R(\theta,\phi)C(x)M(f,x)e^{-\alpha(f)x}$ and name each factor.
(b) Show that taking ratios between nearby stations with similar paths isolates
the exponential term better than an absolute amplitude inversion, and state the
assumption this requires.
(c) Design a numerical experiment that measures $Q$ from synthetic data generated
with a known $Q$, a known geometric spreading law and a known station-correction
field; report your recovered $Q$ and the bias you measure with and without the
station corrections.
(d) State the conclusion in one sentence about the role of station corrections in
attenuation tomography.

---

**★★★10.** Scattering and absorption both remove energy from the direct arrival.

(a) Write the total attenuation as $\alpha_{\text{tot}} = \alpha_{\text{abs}} +
\alpha_{\text{scatt}}$ and state the corresponding relation for $Q$.
(b) Show that in the Rayleigh regime the scattering contribution scales as
$a^6f^4$ and that the intrinsic contribution is approximately linear in $f$ for
constant $Q$; compute the frequency at which the two are equal for
$a = 5$ mm, $\epsilon = 0.05$, $n = 10^{10}$ m⁻³ and $Q_{\text{int}} = 200$
(stating the prefactor you assume and its uncertainty).
(c) Discuss whether the crossover frequency you computed is above or below the
seismic band, and what that implies for the interpretation of a measured
frequency-dependent $Q$.
(d) State the independent measurement that would discriminate the two
mechanisms, and what it requires.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
