# Exercises — 05-02-03 Noise, Drift, Tides and Instrument Bias

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Name the four error sources, give each one's time signature, and state
the standard remedy.

**★2.** Explain the difference between precision and accuracy with one
geophysical example each.

**★3.** A survey averages 100 samples of a reading with individual scatter
0.02 mGal. State the expected scatter of the mean and one condition for it to
hold.

---

## ★★ Applied

**★★4.** A 6-hour loop has 0.04 mGal/h drift and a tide of 0.18 mGal amplitude
with a 12.42 h period. Compute the maximum drift and the maximum tide
contribution, and state which dominates.

**★★5.** A base station is re-occupied every 90 minutes. If the drift is truly
linear, what error remains? If it has a 0.02 mGal quadratic component over the
day, what error remains at the midpoint of a 90-minute interval?

**★★6.** Explain why repeating a station twice gives an estimate of precision but
not of accuracy, using the reading model $r = g + \beta + \tau + \epsilon$.

**★★7.** A magnetic survey at low latitude shows a diurnal variation of 40 nT.
A target anomaly is 25 nT. State the conclusion and the design change you would
make.

---

## ★★★ Research-oriented

**★★★8.** Design a drift-correction experiment. Build a synthetic 8-hour survey
with (i) linear drift, (ii) linear plus quadratic drift, (iii) a step offset
caused by an accidental bump. Tie the base every 60, 90 and 120 minutes. For
each combination, report the RMS residual after tying and identify which error
structure defeats which tie interval. State your conclusions about the *detection*
of the bump (what in the data would reveal it).

**★★★9.** Quantify the residual after drift and tide removal as a function of
survey duration and tie interval, and produce a plot of residual RMS against tie
interval for a stated drift model. Include the correlated-noise case (a
sinusoidal 0.03 mGal microseismic term at 0.2 Hz) and report how many samples
are needed to average it to 0.005 mGal. State why the $\sqrt{N}$ rule
underestimates the requirement for correlated noise.
