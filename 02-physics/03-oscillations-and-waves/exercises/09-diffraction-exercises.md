# Exercises — 02-03-09 Diffraction, Scattering and Resolution Limits

Attempt these **closed-book** before opening the
[solutions](./09-diffraction-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/diffraction_demo.py`](../code/diffraction_demo.py) require you to run
it and report its actual output.

---

## ★ Foundational

**★1.** A slit of width 0.20 mm is illuminated with $\lambda = 600$ nm.

(a) Compute the angle of the first minimum.
(b) Compute the angular width of the central maximum.
(c) Compute the linear width of the central maximum on a screen 2.0 m away.
(d) State what happens to that width if the slit is halved.

---

**★2.** A telescope has a 0.30 m aperture observing at $\lambda = 550$ nm.

(a) Compute the diffraction-limited angular resolution.
(b) Compute the smallest crater it can resolve on the Moon at
$3.84\times10^8$ m, stating the assumption that this is a diffraction limit
and not an atmospheric one.
(c) Compute the resolution of a 0.30 m radio dish at a wavelength of 21 cm.
(d) State which aperture would be needed at 21 cm to match the optical
resolution, and comment on why radio interferometry exists.

---

**★3.** A reflection survey has $v = 2500$ m s⁻¹, $f = 40$ Hz and a target at
600 m depth.

(a) Compute the wavelength.
(b) Compute the first Fresnel zone radius.
(c) Compute the lateral footprint diameter.
(d) Compute the migrated resolution limits for $\lambda/4$ and $\lambda/2$.

---

**★4.** Classify the following scatterers by the size parameter $ka$ and name the
regime (Rayleigh, resonant, geometric):

(a) a 1 mm grain with a 100 m seismic wavelength;
(b) a 20 m fracture set with a 100 m seismic wavelength;
(c) a 500 m fault with a 100 m seismic wavelength;
(d) a 1 mm raindrop with a 1 cm radar wavelength.

---

## ★★ Applied

**★★5.** Run the demo's slit section.

(a) Report the maximum difference between the quadrature and the closed form, and
the located first zero.
(b) Explain why the located zero differs from the analytic value by
$8\times10^{-4}$ relative.
(c) Increase the quadrature points by a factor of ten and predict the new maximum
difference; verify.
(d) State why the trapezoid rule is so accurate here, in terms of a property of
the integrand.

---

**★★6.** Run the demo's Airy section.

(a) Report the first zero of $J_1$ and the derived constant in
$\sin\theta_{\min} = C\lambda/D$.
(b) Compute the value of $C$ to five decimals and compare with 1.22.
(c) Explain why the Airy pattern is $(2J_1(q)/q)$, not $J_1(q)/q$ or
$J_0(q)$ — i.e. where each factor comes from.
(d) State the physical meaning of the negative values of the quadrature at
0.1401° and 0.2000°.

---

**★★7.** A GPR survey images a target at 2.0 m depth using a 400 MHz antenna in
soil with $\varepsilon_r = 6$.

(a) Compute the velocity and the wavelength.
(b) Compute the first Fresnel zone radius in the soil.
(c) Compute the migrated lateral resolution for $\lambda/4$ and $\lambda/2$.
(d) Explain why the factor $\lambda z/2$ makes GPR resolution much better than
seismic resolution at the same *relative* depth.

---

**★★8.** Run the demo's Fresnel-zone section.

(a) Report the maximum difference between the numeric integral and the closed form
and the located first maximum.
(b) Explain why the difference is largest at the largest radii.
(c) Explain why the amplitude at $r = 20$ m is small but not zero, and what the
zeros of equation (7) correspond to physically.
(d) Show that the areas of successive Fresnel zones are equal, and explain why
that makes the zone construction simplify.

---

## ★★★ Research-oriented

**★★★9.** A medium contains spherical heterogeneities of radius $a$ and fractional
velocity contrast $\epsilon = \delta c/c$.

(a) Show that in the Rayleigh regime the scattered power scales as
$\epsilon^2a^6k^4$ and state where each power comes from (a dipole argument is
acceptable if you state it).
(b) Show that the scattering mean free path scales as $1/(n\sigma)$ with $n$ the
number density and $\sigma \propto a^6k^4$, and hence that scattering attenuation
grows as $f^4$ in the Rayleigh regime.
(c) A medium has $Q_{\text{scatt}} \propto f^{-4}$ behaviour; estimate the ratio
of scattering attenuation at 5 Hz and 50 Hz and state whether this is a plausible
explanation for an observed frequency-dependent $Q$.
(d) State the independent measurement that would test the hypothesis.

---

**★★★10.** Resolution depends on the signal-to-noise ratio, not only on
wavelength.

(a) Argue, using the Rayleigh two-source problem, that the minimum detectable
separation scales roughly as $\lambda D^{-1}\text{(SNR)}^{-1/4}$ for a
signal-dominated measurement — state clearly that this is an empirical scaling
rather than an exact result.
(b) Write a program that synthesises two Airy patterns separated by a variable
angle, adds Gaussian noise at several levels, and reports the separation at which
the double peak becomes detectable (define your criterion explicitly).
(c) Report a table of measured detectable separation against SNR, and fit the
scaling exponent.
(d) State the practical consequence for survey design: why does stacking improve
resolution, and what is the limit of the improvement?

Report measured values only if you verify them numerically, and state which of
your results are analytic.
