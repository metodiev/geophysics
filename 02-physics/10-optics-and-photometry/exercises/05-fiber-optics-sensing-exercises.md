# Exercises — 02-10-05 Fibre-Optic Sensing and Distributed Acoustic Sensing

Attempt these **closed-book** before opening the
[solutions](./05-fiber-optics-sensing-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/fibre_optics_sensing_demo.py`](../code/fibre_optics_sensing_demo.py)
require you to run it and report its actual output.

Use $c = 299\,792\,458$ m s⁻¹ (exact), a nominal group index $n_g = 1.4682$ at
1550 nm and a nominal loss of 0.20 dB km⁻¹ unless the problem says otherwise.
State clearly when a parameter is adopted rather than computed.

---

## ★ Foundational

**★1.** A single-mode fibre link is 25 km long with a nominal attenuation of
0.20 dB km⁻¹.

(a) Compute the one-way loss in decibels.
(b) Compute the round-trip loss for a distributed sensing measurement.
(c) Convert both to fractions of the launched power.
(d) Compute the attenuation at 1310 nm, assuming the loss is Rayleigh-dominated,
and state one reason the assumption is only approximately true.

---

**★2.** A DAS interrogator launches 40 ns pulses. The group index is 1.4682.

(a) Compute the propagation speed of light in the fibre.
(b) Compute the spatial resolution $\Delta z = vW/2$.
(c) The receiver samples at 250 MS/s. Compute the distance represented by one
sample interval and compare it with (b).
(d) Compute the round-trip time for a 10 km fibre and the maximum pulse
repetition frequency.

---

**★3.** A step-index fibre has a core radius of 4.1 µm, a numerical aperture of
0.14 and operates at 1550 nm.

(a) Compute the V number.
(b) State whether the fibre is single-mode and justify the answer numerically.
(c) Compute the single-mode cutoff wavelength.
(d) Compute the approximate mode count at 800 nm.

---

**★4.** A fibre experiences a strain of 200 nε (nanostrain) over a gauge length
of 20 m at 1550 nm. Use the demo's computed phase sensitivity.

(a) Compute the optical phase change in radians.
(b) Convert it to degrees.
(c) Compute the change in the fibre's optical length $nL$ that produced it.
(d) State whether this phase change is large or small by interferometric
standards, and what that implies for the measurement.

---

## ★★ Applied

**★★5.** Run sections 3 and 5 of
[`../code/fibre_optics_sensing_demo.py`](../code/fibre_optics_sensing_demo.py).

(a) Report the geometric estimate of the backscatter recapture fraction and the
value the demo adopts.
(b) Report the backscatter level for a 10 ns pulse at 0 km and at 10 km.
(c) Report the strain-optic coefficient $\xi$ and the phase sensitivity in
radians per metre per unit strain.
(d) State which of the parameters in (a) is derived and which is adopted, and why
the distinction matters.

---

**★★6.** A DAS channel has a gauge length of 15 m and the ground has a wave
speed of 2500 m s⁻¹.

(a) Compute the frequency of the first null of the gauge transfer function.
(b) Compute the 3 dB frequency.
(c) Compute the same two frequencies if the gauge length is changed to 5 m.
(d) State what happens to the response at the null frequency and why no
correction can recover the signal there.

---

**★★7.** A DAS array has channels spaced 2 m apart, and the ground supports
waves at 1200 m s⁻¹ and 3000 m s⁻¹.

(a) Compute the maximum unaliased spatial wavenumber.
(b) Compute the maximum unaliased frequency for each wave speed.
(c) Compute the same limits for a channel spacing of 0.5 m.
(d) State which parameter a user must change to record a 700 Hz surface wave at
1200 m s⁻¹ without aliasing, and whether that change affects the gauge-length
response.

---

**★★8.** Run section 8 of
[`../code/fibre_optics_sensing_demo.py`](../code/fibre_optics_sensing_demo.py).

(a) Report the temperature equivalent of one kelvin in microstrain.
(b) Report the phase change over a 10 m gauge for a 0.1 K temperature change.
(c) Compute the apparent strain produced by a 5 K daily temperature swing.
(d) State one measurement that would be corrupted by the answer to (c) and one
mitigation.

---

## ★★★ Research-oriented

**★★★9.** Derive the two-point-difference gauge response.

(a) A DAS channel is formed as the difference of the phase measured over two
sections separated by a length $L$. For a sinusoidal strain field with spatial
wavenumber $k$, show that the response magnitude is proportional to
$|\sin(kL/2)|$ rather than to the boxcar response
$|\operatorname{sinc}(kL/2)|$ used in the lesson, and state the assumption that
distinguishes the two models.
(b) Compute the first null wavenumber and the first null frequency for
$L = 10$ m and $v = 3000$ m s⁻¹ under the two-point-difference model.
(c) Compute the response at half the null frequency under both models and state
which is larger.
(d) Explain why the correct model must be established for the specific
interrogator before any amplitude is quoted, and what calibration measurement
would settle it.

---

**★★★10.** Derive the phase-to-strain relation and examine its assumptions.

(a) Starting from $\phi = 2\pi nL/\lambda$, derive
$\Delta\phi/\phi = \xi\epsilon$ with
$\xi = 1-\frac{n^2}{2}[p_{12}-\nu(p_{11}+p_{12})]$, stating what each term
represents physically.
(b) Compute $\xi$ for $n = 1.4504$, $p_{11} = 0.121$, $p_{12} = 0.270$,
$\nu = 0.17$.
(c) State what the answer to (b) would be if the strain-optic effect were
ignored, and the fractional error that would be introduced in a strain
measurement.
(d) A fibre is embedded in a stiff formation whose modulus is ten times that of
the surrounding soft rock. Using the ratio of moduli, estimate the fraction of
the far-field strain that the fibre actually experiences, and state the
assumption that makes this estimate valid.

---

**★★★11.** Design a DAS survey.

(a) For a 12 km fibre, compute the maximum pulse repetition frequency and the
temporal Nyquist frequency.
(b) Compute the spatial Nyquist frequency for 1 m channel spacing at a wave speed
of 2000 m s⁻¹ and at 4000 m s⁻¹.
(c) The target is a 250 Hz surface wave at 500 m s⁻¹. Compute the required
channel spacing to avoid aliasing and the gauge length that gives a 3 dB point
just above 250 Hz.
(d) State two reasons the design in (c) may be unachievable in practice, and what
would be traded to accommodate them.
