# Exercises — 05-06-04 Gain Control, Amplitude Recovery and True-Amplitude Handling

Attempt these **closed-book** before opening the
[solutions](./04-gain-and-amplitude-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement (SYNTHETIC, 25 Hz Ricker,
$Q = 80$, reference time 0.2 s, noise 0.0008 in trace units): decay factors 0.82172,
0.28573, 0.11398, 0.05131, 0.02217, 0.00909 at $t$ = 0.2, 0.45, 0.8, 1.2, 1.7,
2.3 s; recovered amplitudes under *no gain* 0.69732, 0.11478, −0.03439, 0.01198,
−0.00319, −0.00164; under *t-gain* 0.13946, 0.05165, −0.02751, 0.01436, −0.00540,
−0.00370; under *AGC* 5.77319, 5.79769, −5.70997, 6.33801, −3.46617, −2.31223;
under *true amplitude* 0.84860, 0.40171, −0.30172, 0.23273, −0.14279, 0.18389
against true coefficients 0.85, 0.40, −0.30, 0.20, −0.12, 0.07. Ratio of event 2 to
event 4 (true 2.000): 9.577 (+378.8 %), 3.597 (+79.9 %), 0.915 (−54.3 %), 1.726
(−13.7 %). Gain factors and event S/N: 1.22/717.43, 3.50/40.82, 8.77/4.87,
19.49/0.66, 45.11/0.07, 109.99/0.01.

---

## ★ Foundational

**★1.** Derive the geometric-spreading amplitude law for a point source and for a
line source, and state why they differ by a square root.

---

**★2.** State the absorption law $A = \exp(-\pi f t/Q)$ and evaluate it for
$f = 30$ Hz, $t = 1.5$ s, $Q = 60$.

---

**★3.** Distinguish, in one sentence each, a *correction* from a *normalisation*, and
give one example of each.

---

**★4.** Compute the gain factor $(t/t_0)\exp(\pi f t/Q)$ for $t = 3$ s, $t_0 = 0.2$ s,
$f = 25$ Hz, $Q = 100$.

---

**★5.** State why an amplitude correction cannot improve the signal-to-noise ratio of
an event.

---

## ★★ Applied

**★★6.** A trace is recorded with a 0.5 s reflection of amplitude 0.30 and a 3.0 s
reflection of amplitude 0.003, in the same units.

(a) Compute the apparent ratio of the shallow to the deep event.
(b) Using the decay model with $t_0 = 0.2$ s, $f = 30$ Hz, $Q = 90$, compute the
true coefficient ratio, assuming both events have the same coefficient.
(c) State what an interpreter would conclude from the raw amplitudes, and why that
conclusion would be wrong.

---

**★★7.** A true-amplitude correction is applied with an assumed $Q$ of 120 when the
true $Q$ is 80. The deepest event is at 3.5 s at 25 Hz.

(a) Compute the amplitude error introduced at that time.
(b) State whether the error is a bias or noise.
(c) State what must be reported so a reader can assess the correction.

---

**★★8.** A 3-D survey is processed with a $1/t$ gain, but the data were acquired with
a long single line and a 2-D processing sequence.

(a) Compute the extra factor applied to an event at 2.5 s relative to one at 0.25 s.
(b) Compare its size with the absorption term at $Q = 80$, 25 Hz over the same
interval.
(c) State which correction should be fixed first, and why.

---

**★★9.** A relative-amplitude measurement is quoted as "the amplitude of event B is
0.6 times that of event A".

(a) Using the lesson's S/N table, state the latest time at which such a ratio is
meaningfully measurable in the demonstration's synthetic trace.
(b) State two pieces of information the quoted ratio must be accompanied by.
(c) State what would change if event B were measured at S/N = 0.7.

---

## ★★★ Research-oriented

**★★★10.** Implement surface-consistent amplitude scaling (equation (5) of the
lesson) as a least-squares problem in the log domain, and demonstrate on synthetic
data with known per-trace factors that the decomposition recovers the factors up to
the expected constant. Report the recovery error as a function of the number of
traces, and state the condition under which the problem becomes ill-conditioned.

---

**★★★11.** Design a numerical experiment that measures how much of a *lithological*
amplitude anomaly (a 30 % reflection-coefficient change over a 200 m interval) is
recoverable after each of the four schemes of Section 4 of the lesson. Report the
recovered anomaly magnitude as a percentage of the true one, and state the scheme's
usable depth range.

---

**★★★12.** The lesson argues that the −13.7 % residual in the true-amplitude case is
noise, not a method failure. Test that claim: repeat the experiment with the noise
amplitude reduced by factors of 2, 4 and 10, and report the recovered ratio error as a
function of the input noise. Extrapolate to zero noise and state whether the ratio
error vanishes, and what the residual at zero noise would then represent.
