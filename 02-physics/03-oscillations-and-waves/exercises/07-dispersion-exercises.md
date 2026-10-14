# Exercises — 02-03-07 Dispersion, Group Velocity and Phase vs Group Speed

Attempt these **closed-book** before opening the
[solutions](./07-dispersion-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/dispersion_demo.py`](../code/dispersion_demo.py) require you to run it
and report its actual output. Take $g = 9.80665$ m s⁻².

---

## ★ Foundational

**★1.** For each dispersion relation, compute $v_{\text{ph}}$, $v_g$ and the
ratio at $k = 2.0\ \mathrm{rad\,m^{-1}}$:

(a) $\omega = 500k$;
(b) $\omega = \sqrt{gk}$;
(c) $\omega = 3.0\times10^{-3}k^2$ (with $\alpha$ in m² s⁻¹).

---

**★2.** A packet consists of two frequencies, 10.0 and 10.5 Hz, travelling at
$v_{\text{ph}} = 2000$ m s⁻¹ in a medium with $v_g = 1950$ m s⁻¹.

(a) Compute the carrier frequency and the difference frequency.
(b) Compute the envelope (beat) period.
(c) Over what distance does the envelope slip a full cycle relative to the
carrier?
(d) State which speed you would measure with a cross-correlation of two receivers
10 m apart, and why.

---

**★3.** The lattice dispersion relation is
$\omega = (2c/a)\sin(ka/2)$.

(a) Show that $v_{\text{ph}} \to c$ and $v_g \to c$ as $ka \to 0$.
(b) Compute both speeds at $ka = \pi/2$ and give the ratios to $c$.
(c) Compute the group velocity at $ka = \pi$ and explain the physical meaning.
(d) State how many points per wavelength correspond to $ka = \pi/2$.

---

**★4.** A storm generates swell with periods from 8 to 16 s, 3000 km from a coast.

(a) Compute the group velocity of the 8 s and 16 s components in deep water.
(b) Compute the travel times of the two groups to the coast.
(c) State which arrives first and how many hours separate them.
(d) Explain why the incoming swell appears to grow in period with time.

---

## ★★ Applied

**★★5.** Run the demo's packet-speed section.

(a) Report the measured and analytic $v_{\text{ph}}$ and $v_g$ for the
non-dispersive and gravity-wave cases, and the relative differences.
(b) State which of the four differences are consistent with round-off and which
are bandwidth effects, with a reason.
(c) Explain why the measured $\omega$ for the gravity-wave packet
(1.980261 rad s⁻¹) differs from $\omega(k_0) = 1.980571$ rad s⁻¹.
(d) Predict the effect of halving the bandwidth on each of the four differences
and verify by running the modified script.

---

**★★6.** A Rayleigh wave in a layered medium has the dispersion relation
$v_{\text{ph}}(f)$ measured between 5 and 50 Hz, falling from 1800 to 700 m s⁻¹.

(a) Explain physically why the low frequencies sample deeper.
(b) Estimate the depth sampled at 5 Hz and at 50 Hz, given that the sensitivity
kernel peaks near a depth of about $\lambda/3$.
(c) Explain why the group velocity is not simply the arithmetic mean of the phase
velocities and how it must be computed.
(d) State two sources of error in the resulting shear-velocity profile.

---

**★★7.** Run the demo's spreading section.

(a) Report the measured widths at $t=0$ and after 20 m for the three cases, and
the ratios.
(b) Rank the three by $d^2\omega/dk^2$ and by observed growth, and explain why the
rankings differ.
(c) Explain why the flexural case grows more than the gravity-wave case even
though $|d^2\omega/dk^2|$ is smaller for the flexural case.
(d) Derive the scaling of the growth with $|d^2\omega/dk^2|$, the travel time and
the initial width, and check it against the measured numbers.

---

**★★8.** A finite-difference scheme for a scalar wave equation on a grid of
spacing $\Delta x$ has the numerical dispersion relation
$\sin(\omega\Delta t/2) = r\sin(k\Delta x/2)$ with $r = c\Delta t/\Delta x$.

(a) Show that for $r \ll 1$ this reduces to $\omega \approx ck$ to leading order.
(b) Derive the leading correction and show that the numerical phase velocity is
$v_{\text{ph}} \approx c\left[1 + \frac{k^2\Delta x^2}{24}(1 - r^2)\right]$.
(c) For $r = 0.5$ and 10 points per wavelength, compute the fractional error in
$v_{\text{ph}}$ and compare with the number needed to keep a 100-wavelength
propagation path coherent.
(d) State the design rule that follows.

---

## ★★★ Research-oriented

**★★★9.** A medium has attenuation $Q(f)$ and, by Kramers–Kronig consistency, a
velocity dispersion.

(a) Using the nearly-constant-$Q$ relation of lesson 02-03-10, derive the group
velocity $v_g = d\omega/dk$ in terms of $v(f)$ and $dv/df$, and show that
$v_g \approx v\,[1 - \frac{1}{\pi Q}(1+\ln(f/f_0))]^{-1}$ for small loss.
(b) Show that $v_g < v$ for a constant-$Q$ medium, and estimate the fractional
difference at $Q = 50$ over a decade of frequency.
(c) Write a program that computes $v_{\text{ph}}(f)$ and $v_g(f)$ for a
constant-$Q$ model with $Q = 50$, $v(f_0) = 3000$ m s⁻¹, and report both curves at
1, 5, 10 and 50 Hz.
(d) State the practical consequence: a travel-time measurement made on a pulse
arrival measures the *group* velocity, while a phase-based measurement of an
arrival measures the *phase* velocity. Which one should be reported, and what
must be stated?

---

**★★★10.** Surface-wave dispersion is measured with an array.

(a) Derive the relation between the array aperture $L$, the number of receivers
$n$, the wavenumber resolution $\Delta k$ and the Nyquist wavenumber. State both
limits explicitly.
(b) Show that there is an optimal frequency band for a given array and give the
condition on $L/\lambda$.
(c) Simulate a two-mode dispersion curve (a fundamental and a higher mode)
crossing at one frequency, generate synthetic records at 24 receivers over a 100 m
aperture, and apply a simple f-k (frequency–wavenumber) transform to recover the
curves. Report the recovered curves and which parts of them are well resolved.
(d) Explain how a crossing of two modes corrupts a dispersion measurement, and
state one processing strategy for dealing with it.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
