# Exercises — 05-06-03 Static Corrections, Datum and Elevation Effects

Attempt these **closed-book** before opening the
[solutions](./03-static-and-datum-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement (SYNTHETIC, 30 Hz Ricker, 400
traces): weathering static $2h(1/v_w - 1/v_r)$ = 2.53, 7.60, 12.67, 25.33 and
38.00 ms for $h = 1, 3, 5, 10, 15$ m at $v_w = 600$, $v_r = 2500$ m/s; stack
attenuation 1.000000, 0.974661, 0.904066, 0.703373, 0.321328, 0.155605, 0.059881
for $\sigma_t = 0, 1, 2, 4, 8, 12, 16$ ms against
$\exp(-2\pi^{2}f^{2}\sigma_t^{2})$ = 1.000000, 0.982392, 0.931405, 0.752583,
0.320787, 0.077444, 0.010589, with a measured implied frequency falling from 36.06
to 23.60 Hz; partial correction retaining 1.001039, 0.984514, 0.903591, 0.682146,
0.306183 for fractions removed 1.00, 0.90, 0.75, 0.50, 0.00; datum spread 57.6 ms
(flat) versus 20.9 ms (floating) with 44.8 ms of long-wavelength time removed.

---

## ★ Foundational

**★1.** Derive $\Delta t = 2h(1/v_w - 1/v_r)$ and state why the factor 2 is there.

---

**★2.** Compute the weathering static for $h = 8$ m, $v_w = 500$ m/s,
$v_r = 3000$ m/s, in ms and in samples at 4 ms sampling.

---

**★3.** State the three kinds of static and, for each, the source of its values.

---

**★4.** State the relation between an elevation error $\Delta z$, a replacement
velocity $v_r$ and the seismic time error, and evaluate it for $\Delta z = 15$ m and
$v_r = 2400$ m/s.

---

**★5.** Explain in one sentence why a statics solution cannot determine the
long-wavelength part of the statics itself.

---

## ★★ Applied

**★★6.** A survey targets a 70 Hz bandwidth and requires the stack to retain at
least 97 % of its ideal amplitude.

(a) Using $\exp(-2\pi^{2}f^{2}\sigma_t^{2})$, compute the maximum residual static
$\sigma_t$.
(b) Convert it to a weathering-thickness accuracy at $v_w = 700$, $v_r = 2800$ m/s.
(c) Comment on whether an independent refraction survey can achieve that.

---

**★★7.** A spread has receiver elevations from 120 m to 175 m, a replacement
velocity of 2200 m/s, and a datum at 100 m.

(a) Compute the two-way elevation static at the highest and lowest receivers.
(b) Compute the range of statics across the spread.
(c) If the replacement velocity is wrong by 10 %, what error does that introduce at
the highest receiver, and what does the lesson's attenuation table say the
consequence is at 40 Hz?

---

**★★8.** A residual-statics algorithm is run and reports a maximum static of 18 ms
with a standard deviation of 4 ms.

(a) Using the lesson's partial-correction table, estimate the fraction of the ideal
amplitude retained at 30 Hz before and after correction, assuming the initial jitter
had $\sigma_t = 8$ ms.
(b) If the algorithm's solution recovers only the short-wavelength part, explain why
the reported $\sigma_t = 4$ ms may not be the residual seen by the stack.

---

**★★9.** Two 2-D seismic lines meet at right angles and are to be merged. Line A was
processed to a floating datum, line B to a flat datum 60 m below the highest receiver
on line A. Explain, with numbers from the lesson, the size of the mismatch at the
junction, and state what must be reported for a future merge to be possible.

---

## ★★★ Research-oriented

**★★★10.** Measure the attenuation of a *correlated* static field (a random walk
along the spread rather than independent jitter) and compare it with the Gaussian
prediction for the same pointwise standard deviation. Report the ratio of the two
attenuations as a function of correlation length, and explain why correlated statics
attenuate the stack more.

---

**★★★11.** Design an experiment that measures the *recoverable* long-wavelength
component of the statics from a stack-power criterion: scan a range of wavelength
cutoffs in the statics solution and report the stack power as a function of the
cutoff. Identify the cutoff beyond which the stack no longer improves, and state what
that cutoff is measuring physically.

---

**★★★12.** The lesson measured that the implied effective frequency in
$\exp(-2\pi^{2}f^{2}\sigma_t^{2})$ falls from 36.06 to 23.60 Hz as $\sigma_t$ grows
from 1 to 16 ms. Derive the *exact* attenuation for a Ricker wavelet subject to
Gaussian static jitter — the expectation of the stacked wavelet — and show
analytically that the implied frequency must fall. Then verify your result
numerically against the measured table.
