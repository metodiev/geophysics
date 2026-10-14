# Exercises — 03-05-05 Seismic Displays: Wiggle, Variable-Density and Colormaps

Attempt these **closed-book** before opening the
[solutions](./05-seismic-displays-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/05_seismic_displays_demo.py`](../code/05_seismic_displays_demo.py)
require you to run it and report its **actual** output.

The section used throughout is **synthetic**, built from a stated three-horizon
model convolved with a 28 Hz Ricker wavelet at a 2 ms sample interval. Its
amplitudes are dimensionless constructions and are not measurements of any real
survey.

---

## ★ Foundational

**★1.** A section has a 99th percentile of $|a|$ equal to 0.70 and a maximum of
1.55.

(a) Compute the ratio of the maximum clip to the p99 clip in decibels.
(b) Convert the tight clip at $0.25\,a_{\max} = 0.3875$ to decibels relative to
p99.
(c) State in words what a 6.9 dB compression does to the apparent amplitude of
every reflector.

---

**★2.** An amplitude is quoted as $\sigma = 0.4$ mGal with a stated coverage of one
standard deviation.

(a) Compute the half-widths of a 1σ, 2σ and 3σ interval.
(b) Compute the half-width of a 90 % interval using the Gaussian factor 1.645.
(c) State which of these is the correct choice for a "detection threshold" and why
the coverage must be stated before the number is used.

---

**★3.** A wiggle display is drawn 6.4 in wide.

(a) Compute the trace spacing in millimetres and points for 60, 120 and 300 traces.
(b) The demonstration scales the peak amplitude so that one full swing equals one
trace spacing. State what happens visually when the amplitude exceeds that scale.
(c) At which of the three densities would you switch to a variable-density display,
and why?

---

**★4.** Match each display choice to its consequence.

1. Automatic gain control.
2. `interpolation="bilinear"` on a section.
3. A rainbow palette on signed amplitudes.
4. No clip level stated in the caption.
5. A colour bar without units.

(a) Apparent continuity is invented between traces.
(b) Absolute amplitude information is destroyed.
(c) Apparent amplitude ratios depend on the display rather than the data.
(d) The section has no amplitude axis.
(e) The sign of a reflection coefficient cannot be read.

---

## ★★ Applied

**★★5.** Run [`../code/05_seismic_displays_demo.py`](../code/05_seismic_displays_demo.py).

(a) Report the section dimensions, mean, standard deviation and the fraction of
samples that are exactly zero.
(b) Report the 50th, 90th, 99th and 99.5th percentiles of the nonzero amplitudes
and the largest $|a|$.
(c) Report the trace spacing and scale factor for the 60-trace wiggle display.
(d) Report the three clip levels, their saturated percentages and their decibel
offsets from p99.
(e) Report the data mean, the symmetric clip and the asymmetry of the percentile
clip.

---

**★★6.** Modify the demonstration's clip list to include $0.5\,a_{\max}$.

(a) Compute the value.
(b) Predict whether its saturated fraction will be larger or smaller than the
0.25-max clip's 4.22 %, and why.
(c) Run the modification and report the measured fraction.
(d) State which clip you would choose for a figure whose purpose is to compare the
lateral continuity of the strongest reflector, and justify the choice.

---

**★★7.** The wavelet used is a Ricker with 28 Hz peak frequency, sampled at
$dt = 2$ ms.

(a) Compute the dominant period and the number of samples per period.
(b) Compute the Nyquist frequency and the fraction of Nyquist at which the wavelet
sits.
(c) Recompute (a) and (b) for a 45 Hz wavelet and explain what changes about the
optimum clip level and the fraction of zero samples.
(d) State why the *polarity* argument is unaffected by changing the wavelet
frequency.

---

**★★8.** Two panels show the same synthetic section, one under `RdBu_r` and one
under `RdBu`.

(a) State precisely what differs between them.
(b) Explain why the choice cannot be inferred from the data.
(c) Write the caption sentence that resolves the ambiguity.

---

## ★★★ Research-oriented

**★★★9.** You must publish a section to support an amplitude-versus-offset
argument that a particular reflector brightens downdip.

(a) Specify the gain convention, the palette, the interpolation and the clip, and
justify each.
(b) State which of the four would invalidate the argument if chosen differently.
(c) List every display parameter you would record in the caption.

---

**★★★10.** A two-way travel time of 1.00 s is to be converted to depth.

(a) Compute the depth for an average velocity of 2.0 km/s.
(b) Recompute for 2.5 and 3.0 km/s and state the range this implies for an
unknown velocity between those values.
(c) Explain why a seismic figure that labels its vertical axis "depth (km)" while
plotting travel time misleads a reader by more than the axis label alone suggests.
