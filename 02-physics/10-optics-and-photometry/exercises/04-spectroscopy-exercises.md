# Exercises — 02-10-04 Spectroscopy Principles for Remote Sensing

Attempt these **closed-book** before opening the
[solutions](./04-spectroscopy-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/spectroscopy_demo.py`](../code/spectroscopy_demo.py) require you to run
it and report its actual output. The demo's spectrum is **synthetic**; do not
report any of its feature positions as a measurement of a real mineral.

Mineral feature positions must be given as **ranges** with a pointer to a
spectral library, never as single constants.

---

## ★ Foundational

**★1.** Wavelength and wavenumber.

(a) Convert 2.33 µm into wavenumbers in cm⁻¹.
(b) Convert 2200 cm⁻¹ into a wavelength in µm.
(c) Compute the wavenumber interval corresponding to a 1 nm step at 0.9 µm and at
2.2 µm.
(d) Explain, using your answer to (c), why an FTIR interferogram is sampled at
equal optical path difference rather than at equal wavelength.

---

**★2.** Beer–Lambert.

(a) Compute the transmittance and absorptance for an optical depth of 0.3.
(b) Compute the absorptance for an optical depth of 0.6.
(c) Compute the ratio of the two absorptances and compare it with the ratio of
the optical depths.
(d) State at what optical depth the depth/abundance response has fallen to half
of its weak-absorption value, and justify the answer with the demo's table.

---

**★3.** Instrument specification.

(a) Compute the resolving power $\mathcal{R}$ of a 10 nm band centred on 2.2 µm.
(b) Compute the same for a 10 nm band at 10 µm.
(c) Compute the number of contiguous 10 nm bands spanning 0.4–2.5 µm.
(d) Explain the difference between the two instruments' *resolving powers* and
their ability to **detect** a 25 nm wide absorption feature, identifying which
specification governs each ability.

---

**★4.** A narrow absorption feature has a Gaussian profile with FWHM 20 nm and a
true band depth of 0.30. It is observed by an instrument whose response function
is Gaussian with FWHM 30 nm.

(a) Compute the standard deviations of the feature and of the instrument
function, using $\sigma = \mathrm{FWHM}/2.355$.
(b) Using the approximation that a Gaussian feature of depth $d$ and width
$\sigma_f$ convolved with an instrument of width $\sigma_i$ has observed depth
$d\,\sigma_f/\sqrt{\sigma_f^2+\sigma_i^2}$, compute the observed depth.
(c) Compute the fractional depth loss.
(d) State whether the feature's *position* or its *depth* is more robust to the
broadening, and why.

---

## ★★ Applied

**★★5.** Run sections 2 and 3 of
[`../code/spectroscopy_demo.py`](../code/spectroscopy_demo.py).

(a) Report the true depth of the narrow 2.20 µm feature and the depth recovered
by a 40 nm FWHM instrument.
(b) Report the same for the broad 0.90 µm feature and state the two fractional
losses.
(c) Report the depth and the recovered centre for 10 nm and 20 nm sampling.
(d) Explain why the answer to (c) at 50 nm sampling is not a small error but a
false negative.

---

**★★6.** A normalised difference index is formed from two bands with
reflectances 0.20 and 0.35.

(a) Compute the index.
(b) Compute the index if both reflectances are multiplied by 0.5 and again if
they are multiplied by 2.
(c) Compute the un-normalised difference for the same three cases and comment.
(d) State one atmospheric effect the index removes and one it does not.

---

**★★7.** An opaque, isothermal surface has a reflectance of 0.45 at a given
wavelength and viewing angle.

(a) Compute its emissivity.
(b) Compute its emitted flux at 300 K relative to a blackbody at the same
temperature.
(c) Using the broadband greybody relation, compute the brightness temperature if
the emissivity is assumed to be 1, and the error.
(d) State the two conditions on the surface that make (a) valid.

---

**★★8.** Run section 7 of
[`../code/spectroscopy_demo.py`](../code/spectroscopy_demo.py).

(a) Report the model reflectance and emissivity at the 2.20 µm feature and on the
2.10 µm shoulder.
(b) Report the spectral contrast in emissivity.
(c) Explain why the contrast is equal and opposite to the reflectance contrast.
(d) State why this equivalence is the reason a reflectance library can be used
to interpret a thermal infrared measurement, and give one condition under which
it fails.

---

## ★★★ Research-oriented

**★★★9.** Quantitative abundance from a band depth.

(a) Derive $D = 1-e^{-\tau}$ for a purely absorbing layer of optical depth
$\tau$, stating whether $D$ here is a transmittance-derived absorptance or a
reflectance band depth, and why they behave the same way at small $\tau$.
(b) Compute the optical depth at which $D = 0.5$.
(c) Compute $\mathrm dD/\mathrm d\tau$ at that point and compare it with the
weak-absorption limit $\mathrm dD/\mathrm d\tau \to 1$.
(d) State what a measurement of $D = 0.5$ tells you about abundance and what it
does not.

---

**★★★10.** Continuum choice and its consequences. Using the demo's synthetic
spectrum, compute the band depth of the 2.20 µm feature with a straight-line
continuum fitted between

(a) 2.14 and 2.26 µm;
(b) 2.10 and 2.33 µm;
(c) 1.90 and 2.45 µm.

(d) State which of the three is the "correct" continuum, and what an author must
report so that their band depths are comparable with someone else's.

---

**★★★11.** Two minerals A and B have diagnostic absorption features at
$\lambda_A$ and $\lambda_B$, and the scene contains both.

(a) Explain why a single-band index cannot separate abundance from mineralogy in
general.
(b) Explain why the *position* of a shifted feature is more diagnostic than its
depth, in terms of the physical origin of the shift.
(c) A library match returns a single mineral with a residual of 2 per cent
reflectance. State three reasons this is not proof of identification.
(d) State the four instrument parameters that must be specified before any
statement about "detectability" of a mineral can be made.
