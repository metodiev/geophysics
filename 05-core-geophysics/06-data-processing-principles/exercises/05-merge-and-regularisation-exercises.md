# Exercises — 05-06-05 Gridding, Merging and Levelling of Survey Data

Attempt these **closed-book** before opening the
[solutions](./05-merge-and-regularisation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurements. Gridding from a 21 × 21 grid at
200 m into a 201 × 201 grid at 20 m, true peak 0.34807 mGal: RMS errors 0.00897
(nearest), 0.00262 (linear), 0.00065 (cubic), 0.01917 (IDW $p{=}2$), 0.00531
(IDW $p{=}4$), 0.00054 (thin-plate RBF), 0.00031 (multiquadric RBF); peaks 0.33337,
0.33337, 0.34417, 0.33337, 0.33337, 0.33895, 0.34341, i.e. peak errors −4.22, −4.22,
−1.12, −4.22, −4.22, −2.62, −1.34 %, with a spread of 0.01081 mGal = 3.1 % of the
true peak. Undersampling with linear interpolation: peak error −46.34 % at 1000 m,
−37.93 % at 500 m, −9.51 % at 250 m, −3.84 % at 100 m. Noisy samples
($\sigma = 0.005$): RMS at the samples 0.00480 for linear, cubic and RBF alike.
Upward continuation of a 500 m dipole: retained 57.88, 29.67, 12.57, 3.84 % for
$\Delta z$ = 100, 250, 500, 1000 m against $(h/(h+\Delta z))^{3}$ = 57.87, 29.63,
12.50, 3.70 %. Downward continuation: signal peaks 1.8661e3, 2.1947e3, 3.1249e3,
4.7412e3, 2.1773e5 nT and noise 3.3056e2, 1.4071e4, 5.1486e7, 2.4961e11, 1.3350e15
nT for $\Delta z$ = 25, 50, 100, 150, 200 m against predicted gains 2.057e1, 8.534e2,
2.989e6, 1.428e10, 7.700e13. Stabilised continuation (band-limited to
$\lambda > 6\Delta z$): noise 3.9068, 1.8751, 9.0447e−1 nT and gains 2.601e−1,
1.112e−1, 5.930e−2 against plain gains 2.934e6, 8.389e13, 1.053e29. RTP with a
measured operator for a 60° assumption: errors 5.51 % (45°), 0.00 % (60°), 5.26 %
(75°), 9.85 % (90°). Derivative noise gains at $\Delta x = 25$ m: 0.07210, 0.00706,
0.00075, 0.00008 for $n = 1,2,3,4$ against $k_N^{n}/\sqrt{2n+1}$ = 0.07255, 0.00706,
0.00075, 0.00008.

---

## ★ Foundational

**★1.** State why gridding is interpolation and therefore an invention, and give one
situation in which the invention is unavoidable.

---

**★2.** Derive the continuation transfer functions for upward and downward
continuation by $\Delta z$ from Laplace's equation, and state which is bounded.

---

**★3.** Derive the noise gain of the $n$-th derivative,
$k_N^{n}/\sqrt{2n+1}$, from the mean of $k^{2n}$ over the band.

---

**★4.** Compute the derivative noise gain for $\Delta x = 50$ m and $n = 1, 2$.

---

**★5.** State in one sentence what reduction to the pole assumes, and what happens
when the assumption fails.

---

## ★★ Applied

**★★6.** A grid is sampled at 250 m spacing over a body at 300 m depth.

(a) Using the measured undersampling table, estimate the peak error for linear
interpolation.
(b) What spacing would reduce the error below 5 %?
(c) Explain why no choice of interpolator changes the answer to (a).

---

**★★7.** A dipole at 400 m depth is to be continued downward by 100 m.

(a) Compute the expected signal amplification $(h/(h-\Delta z))^{3}$.
(b) Compute the predicted white-noise gain, i.e. the RMS of $e^{|k|\Delta z}$ over a
grid with $\Delta x = 20$ m.
(c) If the field's noise is 5 nT, what is the noise after continuation, and is the
continuation meaningful?

---

**★★8.** A magnetic survey over a dyke is processed with RTP using an assumed
inclination of 65°. The true inclination is 40°.

(a) Using the lesson's measured errors for a 15° and a 25° discrepancy, estimate the
systematic error as a percentage of the peak.
(b) State whether the error would be detected by a repeat survey.
(c) State the alternative product you would deliver instead, and why.

---

**★★9.** A grid has a 30 % error in the peak amplitude, of which 25 % comes from
undersampling and 5 % from the interpolator.

(a) What is the dominant term?
(b) Would a more sophisticated interpolator help?
(c) Write a two-sentence recommendation.

---

## ★★★ Research-oriented

**★★★10.** Implement a minimum-curvature gridding algorithm (or an equivalent
bending-energy minimiser) and compare it with the interpolators of Section 2 of the
lesson on the same synthetic field. Report the peak error, the RMS error and the
behaviour in a data gap, and explain why minimum curvature is *not* a reconstruction.

---

**★★★11.** Measure the effect of FFT wraparound on continuation: compute the
continuation of the same field with and without a taper of varying width, and report
the interior error and the edge error as functions of the taper width. State the
practical rule you would adopt, and its cost.

---

**★★★12.** Construct an experiment that quantifies how much *real* structure a
micro-levelling pass removes. Generate a field containing both line-correlated
stripes (acquisition artefacts) and a genuine linear dyke, apply a micro-levelling
filter, and report the recovered dyke amplitude as a function of the filter's
correlation length. State the criterion you would use to choose the filter, and
whether it is checkable on real data.
