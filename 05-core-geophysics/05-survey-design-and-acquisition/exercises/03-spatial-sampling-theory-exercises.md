# Exercises — 05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction

Attempt these **closed-book** before opening the
[solutions](./03-spatial-sampling-theory-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement: a 100 m wavelength sampled at
$\Delta x = 60$ m gives an apparent wavelength of 150.000 m; the folded wavenumber
is $-0.041888$ rad/m against $k_0 = 0.062832$ and $k_N = 0.052360$ rad/m; both a
100 m and a 150 m sinusoid fit the ten samples with RMS residual below
$10^{-15}$; sampling at $\Delta x = 2$ m recovers the 100 m wavelength.

Folding formula: $k_{\text{app}} = \big((k_0+k_N)\bmod 2k_N\big) - k_N$ with
$k_N = \pi/\Delta x$.

---

## ★ Foundational

**★1.** Compute $k_N$ and the Nyquist wavelength for $\Delta x = 25$, 50 and 200 m.

---

**★2.** A true anomaly has $\lambda_0 = 250$ m. Compute the apparent wavelength for
station spacings of (a) 100 m, (b) 200 m, (c) 50 m. State which are aliased.

---

**★3.** State the sampling theorem's condition in both wavelength and wavenumber
form, and state in one sentence why the condition is about the *spectrum*, not the
wavelength of the dominant feature.

---

**★4.** A profile samples a field at 40 m spacing. (a) What is the shortest
wavelength that can appear in the record without ambiguity? (b) If a 30 m feature is
present, at what wavelength will it be reported?

---

**★5.** Explain in one sentence why a longer profile does not reduce aliasing.

---

## ★★ Applied

**★★6.** A gravity survey for a target whose anomaly half-width is 400 m is planned
at 250 m spacing. (a) Compute $k_N$ and $\lambda_N$. (b) Is a 200 m anomaly
wavelength representable? (c) Estimate the highest wavenumber present in the
target's own field, using the rule that a body at depth $h$ has little energy above
$k\sim2/h$, and state whether *geological* aliasing is a concern here.

---

**★★7.** A seismic receiver line uses 25 m spacing and records a ground-roll
arrival with an apparent velocity of 400 m/s. (a) What is the highest unaliased
frequency for that arrival? (b) A reflection arrives with an apparent velocity of
3000 m/s; what is its highest unaliased frequency? (c) Explain why the same spacing
is adequate for one and not the other.

---

**★★8.** A magnetic survey at 200 m line spacing detects a coherent "dyke" trending
across the flight direction with a reported width of 400 m. A reconnaissance survey
had previously reported a 800 m feature at the same location. Both cannot be right.
Using the folding arithmetic, state which spacing each survey used and which
interpretation is likely wrong.

---

**★★9.** A grid is sampled with $\Delta x = 20$ m and $\Delta y = 40$ m. A linear
structure runs at 45° to both axes with a wavelength of 100 m measured along the
structure. (a) Compute the $k_x$ and $k_y$ components. (b) Are both within the
per-axis Nyquist limits? (c) What would a contour map show, and why is that a
sampling artefact rather than a geological observation?

---

## ★★★ Research-oriented

**★★★10.** Construct a numerical experiment that measures the *reconstruction*
error of the sinc interpolant as a function of the number of samples per shortest
wavelength, for a band-limited test field. Truncate the sinc interpolant at
$\pm m$ samples and report the RMS reconstruction error as a function of $m$ and of
the samples-per-wavelength ratio. State the empirical rule you would give a survey
designer, and state the conditions under which it fails.

---

**★★★11.** Write a program that takes a *regularly aliased* 2-D field and attempts
to recover the true field by (i) assuming a single fold, (ii) assuming the spectrum
is compactly supported, and (iii) using prior knowledge that the field is an
anomaly of a buried compact body. Report which cases succeed, which fail, and why.
This is the aliasing version of a super-resolution problem; state the role of the
prior.

---

**★★★12.** The lesson asserts that a low-pass filter "would remove the peak and
leave nothing, not the truth". Verify this numerically for a field that contains
*two* components — a 100 m wavelength at amplitude 1 and a 600 m wavelength at
amplitude 0.4 — sampled at 60 m spacing. Report the spectrum, the apparent
wavelengths, and what a 150 m-cutoff low-pass leaves behind.
