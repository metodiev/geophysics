# Exercises — 01-10-07 Two-Dimensional Fourier Analysis and Wavenumber Filtering

Attempt these **closed-book** before opening the
[solutions](./07-2d-fourier-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Convention: forward kernel $e^{-2\pi i(k_x x + k_t t)}$, so an event with arrival
time increasing with offset ($t = t_0 + p\,x$, $p>0$) sits at $k_x = -p\,f$.

---

## ★ Foundational

**★1.** A 2-D transform is computed on a grid of 64 traces at $dx = 12.5$ m and
256 samples at $dt = 4$ ms.

(a) State $L$, $T$, $dk_x$, $df$, the Nyquist wavenumber and the Nyquist
frequency.
(b) A plane wave has apparent velocity 2000 m/s and frequency 25 Hz. At which
$k_x$ bin (as a signed integer) does its energy sit?
(c) Repeat for an apparent velocity of $-1200$ m/s at 15 Hz.

---

**★2.** An event is visible on a shot gather and its first breaks advance by
2.5 ms per trace, with traces 12.5 m apart.

(a) Compute its apparent slowness and apparent velocity.
(b) At 30 Hz, compute its wavenumber.
(c) Is it aliased at this trace spacing?

---

**★3.** Explain in two sentences why a 2-D transform can be computed as one 1-D
transform per trace followed by one 1-D transform per frequency, and state what
goes wrong if the second pass is applied to the wrong axis.

---

**★4.** Sketch (describe in words) the f-k plane for a gather containing,
   simultaneously:

(a) a fast reflection dipping one way,
(b) a fast reflection dipping the other way,
(c) slow ground roll,
(d) random noise.

State which of these appear as lines through the origin and which do not.

---

## ★★ Applied

**★★5.** A fan filter is to remove ground roll at 400 m/s while keeping
reflections above 1600 m/s.

(a) State the slowness range that must be rejected.
(b) Write the mask condition in terms of $k_x$ and $f$.
(c) At 10 Hz, how many wavenumber bins from the origin does the boundary lie,
on the grid of ★1?
(d) What happens to the decision at $f = 2$ Hz, and what does that imply for the
origin region?

---

**★★6.** Two plane waves are placed exactly on the bin grid with
$k_x = +10$ and $k_x = -24$ bins at $k_f = 14$ bins, and a fan filter keeps
$\lvert k_x/f\rvert < 1/800$ s/m.

(a) Compute the two apparent velocities.
(b) Using the lesson's measurements, state how much of each event survives, and
interpret the two numbers.
(c) The same events are then built as finite wave packets. State the approximate
fractions that survive and leak, and explain the change in one sentence.

---

**★★7.** A quadrant filter is applied to two on-grid plane waves of opposite
slowness.

(a) State which half-plane is kept for an event with $p > 0$, and why its
conjugate half is also kept.
(b) What happens if the conjugate half is *not* kept — describe the output.
(c) The lesson reports leakage of $2.0\times10^{-15}$ and loss of
$1.6\times10^{-15}$. Interpret both numbers.
(d) Why is the cone around the origin left unmuted in practice?

---

**★★8.** A 2-D wavenumber cut is applied to an event whose wavenumber is 10 bins,
with the cut at 6 bins.

(a) State what fraction of the event's energy is removed by the cut, and why
that is not the whole story.
(b) The lesson measures an edge-to-middle RMS ratio of 6.237 with no taper and
4.136 with a 10% cosine taper, and a taper that removes 14.38% of the total
energy. Comment on whether the taper is worth it.
(c) State two alternatives to tapering and one cost of each.

---

## ★★★ Research-oriented

**★★★9.** Using [`code/fk_filter_demo.py`](../code/fk_filter_demo.py):

(a) Report the leakage and loss fractions for wave packets of widths 0.06, 0.12,
0.24 and 0.48 s, and describe the trend.
(b) Explain why the trend does not reach zero as the packet lengthens
indefinitely, relating your answer to the array length rather than to the packet.
(c) Design a test to determine how the leakage depends on the ratio of the
array's *effective* length for the event (the number of traces lit at once) to the
wavenumber resolution. Describe the measurement and the plot you would make.
(d) A processing report states that ground roll was removed by an f-k filter and
shows a section with no ground roll. List the additional information you would
require before accepting the section as interpretable.

---

**★★★10.** Aliasing, sign conventions and their consequences.

(a) Derive the spatial alias frequency from the phase-step argument, and compute
it for $dx = 12.5$ m and $v = 850$ m/s.
(b) The lesson measures that at 52 Hz with $v = 1000$ m/s and $dx = 12.5$ m the
apparent velocity reads 1809 m/s and the apparent wavenumber changes sign.
Reproduce both numbers from the fold of the wavenumber axis.
(c) A fan filter is designed to keep $v > 800$ m/s. Using (a) and (b), explain why
the filter's behaviour above the alias frequency is not what its designer
intended, and quantify the consequence for the 850 m/s event at 60 Hz.
(d) If the convention were reversed, the mask would keep the opposite half-plane.
Describe how you would detect the mistake from the processed output alone, and
state whether detection is guaranteed.
