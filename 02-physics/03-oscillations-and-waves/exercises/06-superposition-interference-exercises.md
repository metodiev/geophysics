# Exercises — 02-03-06 Superposition, Interference and Standing Waves

Attempt these **closed-book** before opening the
[solutions](./06-superposition-interference-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/interference_demo.py`](../code/interference_demo.py) require you to run
it and report its actual output.

---

## ★ Foundational

**★1.** Two loudspeakers 3.0 m apart emit 500 Hz in phase; the speed of sound is
343 m s⁻¹. A listener stands 8.0 m in front of the midpoint.

(a) Compute the wavelength.
(b) Compute the path difference at the midpoint and state whether it is
constructive or destructive.
(c) Find the lateral positions of the first two maxima on a line 8.0 m away,
using both the exact condition and the far-field formula.
(d) State which answer you would trust and why.

---

**★2.** A string of length 0.60 m is fixed at both ends and carries waves at
180 m s⁻¹.

(a) Compute the three lowest mode frequencies.
(b) Compute the node positions of the second mode.
(c) Explain why a pluck excites several modes and what determines the relative
amplitudes.
(d) State the frequency of a note one octave above the fundamental of this
string, in terms of the mode number.

---

**★3.** Two waves of equal amplitude travel in opposite directions with
$\lambda = 2.0$ m and $A = 0.03$ m.

(a) Write the standing-wave expression.
(b) Locate the nodes and antinodes for the convention $2A\cos(kx)\cos\omega t$.
(c) Compute the maximum particle speed at an antinode given $f = 20$ Hz.
(d) State the net energy flux and justify it in one sentence.

---

**★4.** Two coherent beams of intensities 4.0 and 1.0 (arbitrary units) interfere
on a screen.

(a) Compute the maximum intensity.
(b) Compute the minimum intensity.
(c) Compute the average intensity and verify that it equals the sum.
(d) Compute the visibility (fringe contrast)
$(I_{\max}-I_{\min})/(I_{\max}+I_{\min})$.

---

## ★★ Applied

**★★5.** The demo measures the fringe spacing of a two-source pattern at
$\lambda = 0.5$ m, $d = 2.0$ m and $L = 40$ m.

(a) Report the measured half-spacing, the exact value and the far-field value.
(b) Compute the relative error of the far-field value and check that it scales as
$(x/L)^2$ by repeating the calculation for $L = 20$ m.
(c) Explain physically why the fringe spacing *increases* with distance from the
axis.
(d) State what measurement you would make to determine $d$ if $\lambda$ and $L$
were known, and how precisely.

---

**★★6.** A seismic vibrator of bandwidth 5–50 Hz is used in a two-source
"shot-coded" array.

(a) Compute the coherence time for a 45 Hz bandwidth source.
(b) Compute the corresponding coherence length in a medium at 2500 m s⁻¹.
(c) State the maximum path difference over which fringes will survive, and
whether the array will produce a stationary pattern at 1 km range.
(d) Explain why the answer depends on the *bandwidth*, not on the centre
frequency.

---

**★★7.** A layer of thickness $h$ and velocity $v$ lies between two identical
half-spaces.

(a) Derive the condition for the reflected amplitude to be maximal to first order
in the reflection coefficient, and show that it is
$\lambda = 4h/(2n-1)$ — the quarter-wave (tuning) condition.
(b) For $h = 20$ m and $v = 2400$ m s⁻¹, compute the tuning frequency.
(c) Explain why the amplitude *decreases* for thinner beds and why this sets the
limit of detectability.
(d) State the difference between the tuning thickness and the resolution limit of
lesson 02-03-09, in one sentence each.

---

**★★8.** Run the demo's standing-wave section.

(a) Report the measured error in the energy profile and the node positions.
(b) Explain why the error is at the level of round-off rather than of the order of
the grid, and state what property of the sampling makes that possible.
(c) Predict what would happen to the measured profile if the time average were
taken over 0.9 of a period instead of exactly one period, and verify by modifying
the script.
(d) State the practical lesson for measuring a standing-wave or resonance curve in
the field.

---

## ★★★ Research-oriented

**★★★9.** A surface-wave field from a distant noise source is recorded at two
stations separated by $D$, and the cross-correlation of the two records is used to
recover the travel time.

(a) Show that for a *coherent* plane wave the cross-correlation peak is at the
lag $D/v$, and that its width is set by the coherence time.
(b) Show that for *incoherent* noise arriving from all directions the
cross-correlation is the time derivative of the Green function between the two
stations (state the result; a full proof requires the reciprocity theorem of
[02-04-05](../../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)).
(c) Design a numerical experiment that demonstrates (a): synthesise a coherent
wave plus noise at two stations, compute the cross-correlation and report the
measured lag and its error as a function of the signal-to-noise ratio.
(d) State the two conditions under which the recovered arrival time is a genuine
travel time, and what ruins it.

---

**★★★10.** Two coherent sources of unequal amplitude $A_1$ and $A_2$ radiate with
a relative phase $\varphi$.

(a) Derive the intensity pattern and show that the visibility is
$V = 2A_1A_2/(A_1^2+A_2^2)$.
(b) Show that $V=1$ requires equal amplitudes and that $V$ falls as
$2A_2/A_1$ for $A_2 \ll A_1$.
(c) Write a program that produces the pattern for
$(A_1,A_2) = (1,1), (1,0.5), (1,0.1)$, measures the visibility from the extrema
and reports a table of measured against predicted values.
(d) State the practical consequence for seismic interferometry: why does a
strongly asymmetric source distribution reduce the quality of the recovered Green
function?

Report measured values only if you verify them numerically, and state which of
your results are analytic.
