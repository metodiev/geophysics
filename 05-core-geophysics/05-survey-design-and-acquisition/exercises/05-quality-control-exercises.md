# Exercises — 05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata

Attempt these **closed-book** before opening the
[solutions](./05-quality-control-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement: budget terms 0.0100 (instrument),
0.1540 (vertical positioning), 0.0500 (terrain), 0.0150 (tide), 0.0200 (drift) and
0.0050 (coupling) mGal, total 0.1642 mGal with the positioning term carrying 87.9 %
of the variance; repeated occupations raw $\sigma = 0.43096$ mGal falling to
0.01262 mGal after removing a fitted drift of 0.02987 mGal/min over 44 min; 8 loops
of 25 min giving a mean closure of 0.74495 mGal, a closure scatter of 0.00984 mGal,
an estimated rate of 0.02980 against a true 0.03000 mGal/min, and a residual of
0.00505 mGal against a prediction $\sigma_c/\sqrt{m} = 0.00348$ mGal.

---

## ★ Foundational

**★1.** Combine 0.020, 0.050 and 0.100 mGal in quadrature. Which term carries most
of the variance?

---

**★2.** A station is occupied 5 times with readings (mGal) 979.100, 979.104,
979.098, 979.102, 979.096. Compute the mean and the sample standard deviation, and
state the relative standard error of your estimate of $\sigma$.

---

**★3.** State the difference between a **tie** and a **loop closure**.

---

**★4.** A drift rate is 0.025 mGal/min. Compute the misclosure of a 30-minute loop,
and the residual in the next 30-minute loop if the rate was estimated from 4 loops
with closure noise 0.008 mGal.

---

**★5.** List four metadata items that cannot be reconstructed after a survey, and
say why each is irrecoverable.

---

## ★★ Applied

**★★6.** A survey budget is dominated by a terrain-correction residual of
0.080 mGal, with all other terms contributing 0.030 mGal in quadrature.

(a) Compute the total.
(b) If the terrain term is halved, what is the new total, and what is the fractional
improvement?
(c) Repeat for halving the "all other" term instead. Compare the two answers.

---

**★★7.** A field crew reports a repeatability of 0.015 mGal from 6 repeat
occupations.

(a) What is the relative standard error of that figure?
(b) Give the 95 % interval for $\sigma$ (use the fact that
$(N-1)s^{2}/\sigma^{2}$ is chi-square distributed; for 5 degrees of freedom the
2.5 % and 97.5 % quantiles are 0.831 and 12.83).
(c) How many repeats would be needed to state the repeatability to 10 %?

---

**★★8.** A survey runs for 9 hours. The instrument drift is 0.02 mGal/h and is
linear. The crew returns to the base station every 45 minutes.

(a) Compute the maximum accumulated drift within a loop.
(b) Compute the residual after correcting with a rate estimated from 12 loops with
0.010 mGal closure noise.
(c) If the loop interval is doubled to 90 minutes, what happens to the part of the
residual that comes from *nonlinear* drift, and why does the $\sigma_c/\sqrt{m}$
formula not capture it?

---

**★★9.** A base station is re-occupied 20 times over a day; the readings drift by
0.9 mGal monotonically and the scatter about a fitted line is 0.011 mGal.

(a) Estimate the drift rate if the day is 8 hours.
(b) Estimate the repeatability of a single occupation.
(c) State what the *absolute* accuracy of the survey depends on, given that the base
station's own absolute value came from a previous campaign.

---

## ★★★ Research-oriented

**★★★10.** Design a numerical experiment that quantifies how the *correlation
length* of correlated noise (for instance cultural noise along a line) affects the
measured repeatability estimated from a set of repeated stations. Report the bias in
the repeatability estimate as a function of correlation length, and state the
practical implication for quoting a repeatability from a survey.

---

**★★★11.** The lesson's budget assumes the terms are independent. Construct two
plausible pairs of terms that are strongly correlated, and compute the correct total
for a stated correlation coefficient. Report the error made by adding them in
quadrature for $\rho = 0.5$ and $\rho = 0.9$, using the general variance of a sum,
$\sigma_{1+2}^{2} = \sigma_1^{2} + \sigma_2^{2} + 2\rho\sigma_1\sigma_2$.

---

**★★★12.** A colleague proposes to estimate the survey repeatability by occupying a
single station 200 times consecutively, arguing that the resulting 5 % relative
uncertainty is satisfactory. Write a critique of the proposal in 300–400 words,
identifying what such an experiment *does* measure (and what it does not), which
terms of the budget it constrains, and what experimental design would be needed to
constrain the terms it misses.
