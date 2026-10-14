# Exercises — 03-10-03 StationXML Inventory, Response and Instrument Correction

Attempt these **closed-book** before opening the
[solutions](./03-inventory-and-metadata-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first; several answers require its printed values:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/inventory_and_metadata_demo.py
```

---

## ★ Foundational

**★1.** State the units of $H(f)$, the stage gain $G$, the normalisation factor
$A_0$ and the frequency $f$. Verify by dimensional analysis that
$H = A_0 G \prod(s-z)/\prod(s-p)$ has units of counts per (m/s) when the number
of zeros equals the number of poles.

**★2.** The demonstration measures a log-log slope of 2.0000 decades/decade
between 0.004 and 0.02 Hz. Compute $|H(0.01\ \mathrm{Hz})|/|H(0.1\ \mathrm{Hz})|$
in the low-frequency limit and reconcile it with that slope.

**★3.** The measured ratio $|H(f_0)|/|H(\infty)|$ is 0.707130 while
$1/\sqrt2 = 0.707107$. Explain the difference in terms of the evaluation grid.

**★4.** Distinguish `remove_sensitivity` from `remove_response` in one sentence
each, and state the measured ratio between the two for this instrument.

**★5.** Order the stages of a typical station-response chain and state the
units at each stage boundary: ground velocity → sensor output → digitizer
input → counts.

---

## ★★ Applied

**★★6.** From the measured water-level table, state (a) the level that
minimises the error in the 50 mHz amplitude, (b) that error, and (c) the clamp
frequency at the best level. Then estimate by interpolation what happens at
57 dB and say whether 57 dB would be better.

**★★7.** Derive $A_0$ for the demonstration's instrument from the poles and
$f_n = 1$ Hz. Show the two distances $|s_n - p_1|$ and $|s_n - p_2|$, the
product, and that the result is 1.414214.

**★★8.** A broadband sensor has a 120 s corner. Using the clamp-frequency rule
and the low-frequency asymptote $|H| \propto (f/f_0)^2$, compute the water level
needed to recover a 20 mHz signal. Is the 60 dB default clamping anything at
20 mHz for this sensor?

**★★9.** The demonstration reports that a wrong $A_0$ changes the derived
overall sensitivity from $5.1\times10^8$ to $3.60624\times10^8$ counts per m/s.
Compute the implied amplitude error and explain why `remove_response` is still
correct despite the wrong normalisation factor.

**★★10.** The pre-filter at 60 dB reduces the sub-0.04 Hz RMS from 0.7816 to
0.2313 µm/s while leaving the 2–20 Hz RMS unchanged. Explain in three sentences
what the pre-filter does that the water level cannot, and why the two are
complementary rather than alternatives.

---

## ★★★ Research-oriented

**★★★11.** Rebuild the instrument with $f_0 = 0.05$ Hz and repeat the
water-level sweep. Report the clamp frequency at 60 dB and the best level for a
50 mHz target, compare with the 1 Hz geophone, and state the design implication
for a station that targets long-period surface waves.

**★★★12.** Change the added noise from 0.5 counts RMS to 5 counts RMS and
repeat the sweep. Report how the best water level moves and state the rule in
one sentence. Then explain why the optimum is a shallow plateau rather than a
sharp point, and why that matters for the practice of leaving the default at
60 dB.

**★★★13.** Construct an instrument whose response carries **one** zero at the
origin instead of two, so that `remove_sensitivity` produces a genuinely
frequency-dependent error. Measure the peak ratio and the band-limited RMS
error in three bands, and explain why the error cannot be summarised by one
number. Then argue whether the instrument is physically realisable as a
seismometer.
