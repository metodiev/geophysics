# Exercises — 05-06-01 The Processing Pipeline: Editing, Correction, Enhancement

Attempt these **closed-book** before opening the
[solutions](./01-processing-pipeline-concept-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement (synthetic profile, 200 stations at
25 m, noise $\sigma = 0.008$ mGal, three spikes, a linear drift of 0.0995 mGal over
the line): RMS error vs truth 0.14377 (raw) → 0.05756 (edit) → 0.01242 (level) →
0.01177 (filter); the robust difference-based scale 0.01143 mGal against a true
0.00800, and the naive running-median scale 0.00069 mGal which would flag 77 of 200
samples; the straight-line levelling removed 0.1162 mGal of which 0.0134 mGal was
true regional signal; the filter sweep has its minimum RMS error at a 150 m cutoff;
the first-derivative noise gain is 0.07210 at $\Delta x = 25$ m against a predicted
$\pi/(\Delta x\sqrt3) = 0.07255$.

---

## ★ Foundational

**★1.** List the seven stages of the universal processing chain, and for each state
one assumption it makes and one thing it removes.

---

**★2.** A Gaussian low-pass has $H(k) = \exp(-0.5(k/k_c)^{2})$. Compute the
attenuation at (a) $k = k_c$, (b) $k = 2k_c$, (c) $k = k_c/2$. Which of these is the
"cutoff"?

---

**★3.** State what "zero phase" means for a filter and why it matters for event
times.

---

**★4.** A running median with a window of $w$ samples is used to estimate the noise
scale from its residual. What fraction of the residual samples is exactly zero, and
why does that break the estimate?

---

**★5.** State the ordering rule that links statics and stacking, and the one that
links band-limiting and differentiation.

---

## ★★ Applied

**★★6.** A profile has 400 stations with a spike at every 50th station and a linear
drift of 0.15 mGal over the line.

(a) Predict the number of samples a correct despiker will flag.
(b) Predict the drift rate per station.
(c) If the pipeline is run in the order *level → despike → filter*, explain what can
go wrong with the spike detector's threshold estimate, and what the measured
difference was in the lesson's example.

---

**★★7.** The lesson's sweep of the Gaussian cutoff gives the following RMS error
against the truth (mGal): 0.01242 (none), 0.01183 (50 m), 0.01117 (100 m),
0.01114 (150 m), 0.01309 (250 m), 0.02094 (400 m).

(a) Interpolate to estimate the cutoff that minimises the error.
(b) For a target anomaly whose dominant wavelength is 1500 m, would a 250 m cutoff
be acceptable? Justify with the numbers.
(c) State how you would choose the cutoff if you had no truth to compare against.

---

**★★8.** A pipeline applies (i) a derivative, (ii) a 200 m low-pass, (iii) a spike
removal, in that order. (a) State what is wrong with the order. (b) Reorder the steps
and justify each position. (c) For a 25 m grid, compute the noise gain of the
derivative and the noise gain the 200 m low-pass would have had.

---

**★★9.** The lesson measures a 1.03 % of peak RMS difference between two step
orders. A target anomaly is 0.5 mGal and the survey's noise is 0.01 mGal.

(a) Is the ordering difference larger or smaller than the noise, and by what factor?
(b) Does that mean the order does not matter? Explain.

---

## ★★★ Research-oriented

**★★★10.** Implement the difference-based robust scale estimator and compare its
breakdown behaviour with the running-median MAD estimator: contaminate a synthetic
profile with 1 %, 5 %, 10 %, 25 % and 40 % spikes and report the estimated scale and
the number of samples flagged for each estimator. Report the contamination fraction
at which each fails, and explain the difference in terms of breakdown points.

---

**★★★11.** Construct an experiment in which a *well-chosen* filter improves the data
and a *habitually chosen* one degrades it, using the same dataset. Report the two
RMS errors and the two peak-amplitude errors, and state the criterion that separates
the two cases. Make the criterion quantitative and independent of the truth (i.e.
usable on real data).

---

**★★★12.** The lesson asserts that a filter changes the whole spectrum, correlates
the noise, and reduces the effective number of independent samples. Design a
numerical experiment that measures the last effect: apply a low-pass to a stack of
$N$ traces, then measure the actual noise reduction against the $1/\sqrt{N}$
prediction, as a function of the filter's cutoff. Report the effective $N$ and
explain the result.
