# Exercises — 01-10-08 Power Spectra, Admittance and Coherence of Geophysical Fields

Attempt these **closed-book** before opening the
[solutions](./08-spatial-spectra-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻² throughout. The trigamma function
satisfies $\psi'(1) = 1.6449$, $\psi'(2) = 0.6449$, $\psi'(4) = 0.2838$,
$\psi'(8) = 0.1331$, $\psi'(16) = 0.0640$.

---

## ★ Foundational

**★1.** A raw periodogram is computed from a single record.

(a) State the standard deviation of $10\log_{10}P$ in dB.
(b) State the same quantity for an estimate averaged over $K = 4$ and $K = 100$
independent segments, using both the exact trigamma expression and the
approximation $5.6/\sqrt{K}$.
(c) State, in one sentence, what is lost by averaging.

---

**★2.** A real, zero-mean series of $N = 1000$ samples at $dt = 1$ s has
$\lvert X[k]\rvert^{2} = 400$ at one bin.

(a) Compute the one-sided PSD at that bin.
(b) Compute the bin spacing $df$.
(c) If this were the only non-zero bin, what variance would the series have, and
what would the PSD integral give?

---

**★3.** State the definitions of the admittance and the coherence between two
fields, including the units of the admittance when one field is gravity in
m s$^{-2}$ and the other is topography in metres.

---

**★4.** For a surface load of density 2670 kg m$^{-3}$ at mean depth $d = 4$ km,
compute the uncompensated admittance $Z(k) = 2\pi G\rho e^{-kd}$ at wavelengths
100, 20 and 10 km.

---

## ★★ Applied

**★★5.** Two fields on the same grid give, in one band,
$S_{xx} = 4.0\times10^{4}$ m², $S_{yy} = 1.6\times10^{-7}$ (m s$^{-2}$)² and
$\lvert S_{xy}\rvert = 1.6\times10^{-3}$ m·m s$^{-2}$.

(a) Compute the admittance in the least-squares form and the amplitude-ratio
form, with units.
(b) Compute the coherence.
(c) Which estimator would you report, and what else must be reported with it?

---

**★★6.** Explain, in two or three sentences, why a coherence computed from a
single frequency bin of a single periodogram is identically 1. Then state what
happens to a coherence computed from 36 independent bins of unrelated data, and
why the expected value is not 0.

---

**★★7.** A PSD is estimated by averaging 16 contiguous segments of a
4096-sample record sampled at $dt = 1$ s.

(a) How long is each segment, and what is the frequency resolution of the
averaged estimate?
(b) What would the resolution have been without averaging?
(c) What is the standard deviation of $10\log_{10}P$ per bin?
(d) The full-resolution spectrum shows a peak at 0.5 Hz. If the feature is
narrower than the averaged resolution, what will the averaged spectrum show?

---

**★★8.** Show that $\lvert S_{xy}\rvert/S_{xx} \le \sqrt{S_{yy}/S_{xx}}$
whenever the coherence is at most 1, and state the condition for equality.

---

## ★★★ Research-oriented

**★★★9.** Using [`code/power_spectra_demo.py`](../code/power_spectra_demo.py):

(a) Report the error factors of the two admittance estimators for
noise/signal $= 0, 0.25$ and $1.0$, and the number of bands used in each case.
(b) The number of usable bands falls from 12 to 5 as the noise rises. Explain why,
in terms of the coherence threshold.
(c) Report the coherence, the two admittance estimates and the truth for the bands
at 25.6 km, 14.2 km and 5.6 km wavelength at noise/signal $= 0.25$, and interpret
each row.
(d) A colleague averages the spectra of a *single* 128 km profile over 12 bands
and reports coherence 0.9 at 25 km wavelength. State two reasons the true
uncertainty on that coherence is larger than it appears, and how you would improve
the estimate.

---

**★★★10.** Designing an admittance study.

You are given satellite-derived gravity (2 km grid) and ship-track bathymetry
over an ocean region 1000 km across, and asked for the effective elastic thickness
of the lithosphere.

(a) State what you will use as $x$ and as $y$, and why the choice of the
independent variable matters for the estimator.
(b) State how many independent wavenumber bands you can expect in the useful
wavelength range 200–20 km on a 1000 km square, and how that constrains the
achievable stability of the estimate.
(c) State the window, the padding and the detrending you would apply, with a
reason for each.
(d) State the band over which you would expect the coherence to fall below 0.5 in
this application, and why that sets the short-wavelength limit of your reported
result.
(e) List, in the order a reader would want them, the quantities that must appear
in your result for it to be reproducible.
