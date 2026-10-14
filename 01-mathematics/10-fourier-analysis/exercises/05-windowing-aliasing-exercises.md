# Exercises — 01-10-05 Sampling, Aliasing, Leakage and Windowing

Attempt these **closed-book** before opening the
[solutions](./05-windowing-aliasing-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Useful values: rectangular-window first sidelobe $-13.3$ dB, scalloping loss
$2/\pi = 0.6366$; Hann coherent gain 0.5, Hamming 0.54, Blackman 0.42.

---

## ★ Foundational

**★1.** Compute the Nyquist frequency and the apparent frequency of each tone.

(a) $f = 12$ Hz sampled at $f_s = 20$ Hz
(b) $f = 45$ Hz sampled at $f_s = 100$ Hz
(c) $f = 75$ Hz sampled at $f_s = 100$ Hz
(d) $f = 5$ Hz sampled at $f_s = 4$ Hz

For each, state whether the tone is aliased.

---

**★2.** A survey uses receivers every 20 m and must record a steepest event with
apparent velocity 800 m/s.

(a) What is the highest unaliased frequency?
(b) The target bandwidth is 60 Hz. What receiver spacing is required?
(c) State the relation you used in the general form.

---

**★3.** A record is 512 samples long with $dt = 0.004$ s.

(a) State $T$, $df$ and the Nyquist frequency.
(b) Two tones are 0.1 Hz apart. Can this record resolve them?
(c) Two tones are 3 Hz apart. Can it resolve them?
(d) Zero padding to 8192 samples: what is the new bin spacing, and does it change
the answers to (b) and (c)?

---

**★4.** A tone sits exactly halfway between two DFT bins of a record windowed
with a rectangular window.

(a) State the scalloping loss in linear and dB terms.
(b) State what happens to the *total* energy in the spectrum.
(c) State one way to recover the correct amplitude, and what it does *not* fix.

---

## ★★ Applied

**★★5.** A seismic trace is sampled at 4 ms.

(a) What is the Nyquist frequency?
(b) Ground roll travels at 300 m/s and is observed on receivers 25 m apart. What
is the spatial alias frequency?
(c) The ground roll band is 5–15 Hz. Is the recorded ground roll aliased?
(d) The survey is re-designed with 10 m spacing. Recompute (b) and (c).

---

**★★6.** A gravity profile shows a long-wavelength linear trend of 0.05 mGal/km
across a 100 km profile.

(a) Explain why this trend leaks across the whole spectrum.
(b) What is the decay exponent of its amplitude spectrum, and what does the
supplied script measure for a synthetic ramp?
(c) The profile is detrended before spectral analysis. What is the residual
leakage level, and what else is removed?
(d) Quote the measured bias on a periodic tone in the record after detrending,
from the script.

---

**★★7.** A spectrum is computed with a Hann window on a record whose amplitude
must be reported in physical units.

(a) By what factor are all amplitudes wrong if the coherent gain is ignored?
(b) Compute the error in dB, in amplitude and in power.
(c) The Hann-windowed spectrum of a unit-amplitude tone reads 0.5. Is that
correct? Explain.
(d) State the same for Blackman (coherent gain 0.42).

---

**★★8.** Two tones of equal amplitude are separated by $2/T$.

(a) Using the lesson's table, state which windows resolve them under the stated
criterion (two maxima with a valley at least 3 dB below the lower one).
(b) Explain why the answer is different at $3/T$.
(c) A colleague claims 2 Hz resolution from a 1 s record with a Blackman window.
Comment, using the measured threshold for Blackman and its main-lobe width.

---

## ★★★ Research-oriented

**★★★9.** Using [`code/aliasing_leakage_demo.py`](../code/aliasing_leakage_demo.py):

(a) Report the measured leakage floor of a strong tone at the position of a weak
tone 3 bins away, for the rectangular and Hann windows, and the weakest weak-tone
amplitude that reaches twice the floor.
(b) Repeat for 8 bins separation. Report both tables.
(c) Explain why Blackman is worse than rectangular at 3 bins but better at 8
bins, using the main-lobe widths.
(d) A processing sequence applies a Hann window, then a deconvolution, then
reports amplitudes. List in order the three amplitude corrections that must be
made, and the consequence of omitting each.

---

**★★★10.** Aliasing and resolution interact, and both are decided at acquisition
time.

(a) Derive the spatial alias frequency $f_a = v/(2\,dx)$ from the requirement
that the phase step between neighbouring receivers not exceed $180^\circ$.
(b) A 3-D survey has $dx = 25$ m. Ground roll travels at 350 m/s and occupies
5–18 Hz. Is it aliased? Support with numbers.
(c) The same survey needs 40 Hz reflections at apparent velocities down to
2500 m/s. Is $dx = 25$ m adequate for those? Support with numbers.
(d) The two answers conflict, as they usually do. State the three standard
resolutions of that conflict, and the cost of each, in one paragraph.
