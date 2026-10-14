# Exercises — 02-10-02 Interference and Diffraction in Optical Instruments

Attempt these **closed-book** before opening the
[solutions](./02-interference-diffraction-optics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/interference_diffraction_demo.py`](../code/interference_diffraction_demo.py)
require you to run it and report its actual output.

Use the exact Rayleigh coefficient $C = 3.831\,705\,970/\pi$ where a numerical
answer is requested, and state when you are using the approximation 1.22.

---

## ★ Foundational

**★1.** A two-slit experiment uses $\lambda = 633$ nm, a slit separation of
0.20 mm and a screen 1.5 m away.

(a) Compute the fringe spacing on the screen.
(b) Compute the angular fringe spacing in radians.
(c) Each slit is 0.05 mm wide. Compute the number of interference fringes inside
the central maximum of the single-slit envelope.
(d) State what happens to the fringe spacing if the whole apparatus is immersed
in water ($n = 1.333$), and why.

---

**★2.** A single slit of width 0.10 mm is illuminated at $\lambda = 500$ nm and
observed on a screen 1.5 m away.

(a) Compute the angle of the first minimum.
(b) Compute the angular width of the central maximum.
(c) Compute the linear width of the central maximum on the screen.
(d) State what happens to the answer to (c) if the wavelength is doubled at
fixed slit width.

---

**★3.** A telescope has an aperture of 0.25 m and observes at 600 nm.

(a) Compute the diffraction-limited angular resolution in radians and in
arcseconds.
(b) Compute the smallest separation it can resolve on the Moon at
$3.84\times10^8$ m.
(c) Compute the resolution of a 0.25 m aperture at an altitude of 600 km and
express it as a ground sample distance.
(d) Compute the diffraction-limited angular resolution of the dark-adapted human
eye (pupil 7 mm) at 550 nm and compare it with the classical 60″ physiological
limit.

---

**★4.** A source has a central wavelength of 800 nm and a bandwidth of 2 nm.

(a) Compute its coherence length.
(b) Compute the maximum path difference over which fringes are visible.
(c) Compute the coherence length of a stabilised laser of the same wavelength
with 0.001 nm bandwidth.
(d) State which of the two could be used for white-light interferometry and why.

---

## ★★ Applied

**★★5.** Run sections 2 and 3 of
[`../code/interference_diffraction_demo.py`](../code/interference_diffraction_demo.py).

(a) Report the numerically located first two zeros of the Airy pattern in $q$
and the textbook values.
(b) Report the quadrature's own amplitude error for the single slit and the
value of $\sin\theta/(\lambda/a)$ at which it is worst.
(c) Report the Rayleigh coefficient the demo computes.
(d) Explain why the demo can obtain the zeros of $J_1$ without calling a Bessel
function.

---

**★★6.** A lens is made of glass with $n = 1.70$ and is to be coated for use at
1000 nm.

(a) Compute the ideal quarter-wave coating index.
(b) Compute the coating thickness for that ideal index.
(c) Compute the bare-surface reflectance and the reflectance with an MgF₂
coating of index 1.38.
(d) State the transmission gain of the coating and whether an incorrect coating
index can make matters worse.

---

**★★7.** A reflection grating has 900 grooves per millimetre and is 60 mm wide.
It is used in second order at 1550 nm.

(a) Compute the number of illuminated grooves.
(b) Compute the resolving power.
(c) Compute the smallest resolvable wavelength difference in picometres.
(d) State the same resolving power for the same grating used in first order, and
comment on what is gained by going to second order.

---

**★★8.** An imaging spectrometer has 3.9 µm pixels and is to work at 600 nm.

(a) Compute the f-number above which diffraction dominates the pixel.
(b) State whether an f/4 system is diffraction-limited or pixel-limited.
(c) Compute the diffraction-limited ground sample distance for an aperture of
0.35 m at an altitude of 550 km.
(d) Explain what the answer to (b) implies for the design of an imaging
spectrometer with a fixed detector.

---

## ★★★ Research-oriented

**★★★9.** Derive the Airy pattern from the aperture integral.

(a) Show that the far-field amplitude from a circular aperture of radius $a$
reduces to $\int_0^a \rho J_0(k\rho\sin\theta)\,\mathrm d\rho$, stating the
substitution used.
(b) Show that this integral is $a^2 J_1(q)/q$ with $q = ka\sin\theta$, and hence
that the normalised intensity is $(2J_1(q)/q)^2$.
(c) Show that the first zero satisfies $J_1(q) = 0$ and state the numerical
value, cross-checking against the demo's quadrature.
(d) Explain why the *shape* of the aperture, and not its size, determines the
order of the Bessel function that appears, and what would appear instead for a
square aperture.

---

**★★★10.** The precision of a measured line position is limited by
signal-to-noise, not by the instrument's resolution alone.

(a) For a Gaussian line of FWHM $\Delta\lambda$ measured with signal-to-noise
ratio $S$, the standard error of the line centre is approximately
$\sigma_\lambda \approx \Delta\lambda/(2.355\,S)$. Derive this from the
definition of the standard deviation of a Gaussian, or state clearly why it is a
stated ansatz rather than a derivation.
(b) Compute $\sigma_\lambda$ for a line of FWHM 0.20 nm at 500 nm with $S = 100$.
(c) Convert it into a velocity precision and state the assumption about the line
width that this implies.
(d) Explain why the resolution of an imaging spectrometer is *not* the same as
its compositional sensitivity, and what additional quantity must be specified.

---

**★★★11.** An interferometer is used to measure displacement.

(a) Show that a displacement of $\lambda/2$ of one mirror moves the fringe
pattern by exactly one fringe.
(b) Compute the displacement per fringe for $\lambda = 632.8$ nm.
(c) A fringe position can be measured to 1/1000 of a fringe. Compute the
displacement resolution and compare it with the size of a hydrogen atom (about
0.05 nm, nominal).
(d) State the path-difference budget implied for a 1 m arm interferometer with a
0.002 nm source, using the coherence length from the demo, and explain which
source specification would be relaxed first in a low-cost instrument.
