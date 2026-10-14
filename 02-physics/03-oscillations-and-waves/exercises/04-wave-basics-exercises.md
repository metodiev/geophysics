# Exercises — 02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity

Attempt these **closed-book** before opening the
[solutions](./04-wave-basics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/wave_basics_demo.py`](../code/wave_basics_demo.py) require you to run
it and report its actual output. Take $g = 9.80665\ \mathrm{m\,s^{-2}}$ where
needed.

---

## ★ Foundational

**★1.** Complete the table, using $v = \lambda f$.

| Case | $v$ (m s⁻¹) | $f$ (Hz) | $\lambda$ (m) | $T$ (s) | $k$ (rad m⁻¹) | $\omega$ (rad s⁻¹) |
|---|---|---|---|---|---|---|
| (a) | 4000 | 25 | ? | ? | ? | ? |
| (b) | 1500 | ? | 0.30 | ? | ? | ? |
| (c) | ? | 200 000 | 0.025 | ? | ? | ? |

---

**★2.** For $u = 0.02\cos(12x - 300t + \pi/3)$ (SI units):

(a) State the amplitude, wavenumber, angular frequency and phase constant.
(b) Compute the wavelength, period and phase velocity.
(c) State the direction of propagation and justify the answer in one sentence.
(d) Compute $u$ at $x = 0.25$ m and $t = 0.01$ s.

---

**★3.** A seismic wave has a dominant frequency of 25 Hz and travels at
4.5 km s⁻¹.

(a) Compute the wavelength.
(b) State the vertical resolution limit usually quoted for a reflection survey in
terms of $\lambda$.
(c) Compute the smallest feature the survey can resolve at that frequency.
(d) Compute the frequency that would be needed to resolve a 10 m bed.

---

**★4.** A signal contains 20, 55 and 130 Hz components and is sampled at 100 Hz.

(a) Compute the Nyquist frequency.
(b) Compute the apparent frequency of each component.
(c) State which of the apparent frequencies are unchanged and why.
(d) State what must be done before sampling to preserve the 130 Hz component, and
why no digital processing after sampling can do it.

---

## ★★ Applied

**★★5.** A two-receiver array has receivers 12 m apart. A 30 Hz wave arrives with
a measured phase difference of $150^\circ$.

(a) Compute the apparent phase velocity using equation (3) of the lesson.
(b) Compute the wavelength this implies and state the ratio $\Delta x/\lambda$.
(c) List the velocities that would give the same measured phase difference, and
explain why they cannot be distinguished from this measurement alone.
(d) State what additional information would resolve the ambiguity.

---

**★★6.** The demo reports for the deep-water swell row $v = 15.608\
\mathrm{m\,s^{-1}}$, $f = 0.1$ Hz, $\lambda = 156.08$ m.

(a) Verify all three numbers against $c = gT/(2\pi)$ and $c = \sqrt{g\lambda/2\pi}$.
(b) Explain why the speed is *not* a material constant for these waves, and state
what property of the medium does control it.
(c) Compute the period, wavelength and speed of a 15 s swell and compare.
(d) State one consequence for a surfer waiting on a beach: which swell arrives
first from a distant storm, and why.

---

**★★7.** A GPR survey uses a 200 MHz antenna in soil with relative permittivity
$\varepsilon_r = 9$.

(a) Compute the propagation speed, taking $c = 2.998\times10^8$ m s⁻¹.
(b) Compute the wavelength in the soil.
(c) Compute the two-way travel time to a reflector at 3 m depth.
(d) State the resolution limit and compare with a 100 MHz antenna in the same
soil.

---

**★★8.** A pulse has a Gaussian envelope of width 40 m containing a 50 Hz
carrier, and travels at 3000 m s⁻¹ in a medium with $Q = 50$.

(a) Estimate the bandwidth of the pulse and state the range of wavelengths
present.
(b) Using the result of lesson 02-03-10 that the amplitude decays by $e^{-\pi/Q}$
per wavelength, estimate the amplitude ratio between the high- and low-frequency
ends of the band over 1 km of travel.
(c) State whether neglecting the frequency dependence of $Q$ is defensible here,
with a reason.

---

## ★★★ Research-oriented

**★★★9.** A line of receivers is deployed with spacing $\Delta x$ to record a
surface wave whose speed varies with frequency.

(a) Derive the spatial Nyquist condition: any wavenumber with $|k| > \pi/\Delta x$
aliases into $|k| < \pi/\Delta x$.
(b) Show that a phase-velocity measurement from adjacent receivers is unambiguous
only if $\lambda > 2\Delta x$.
(c) For a surface wave with $v(f) = 3000\ \mathrm{m\,s^{-1}}$ at 5 Hz falling to
$1000\ \mathrm{m\,s^{-1}}$ at 50 Hz, compute the minimum receiver spacing needed
to measure the whole band unambiguously, and state which end of the band
controls it.
(d) State the practical trade-off between spacing, array aperture and the
resolution of the resulting dispersion curve, and quantify it in one sentence.

---

**★★★10.** A monochromatic wave is recorded at three receivers in a line at
$x = 0, \Delta x, 2\Delta x$, with $f = 20$ Hz and a true speed of
$2500\ \mathrm{m\,s^{-1}}$ but with a 2 per cent random amplitude error and a
$5^\circ$ random phase error on each trace.

(a) Write a program that synthesises the three traces and estimates the speed by
(i) a two-receiver phase difference and (ii) a least-squares fit of phase against
distance over the three receivers.
(b) Repeat with 200 realisations (use a deterministic pseudo-random generator) and
report the standard deviation of each estimator.
(c) Explain why the three-receiver fit is more robust to random phase error than
the two-receiver difference, and by roughly what factor.
(d) State the residual systematic error both estimators share, and what causes it.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
