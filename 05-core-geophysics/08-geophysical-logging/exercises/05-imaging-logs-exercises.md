# Exercises — 05-08-05 Borehole Imaging, Dipmeter and Fracture Detection

Attempt these **closed-book** before opening the
[solutions](./05-imaging-logs-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/imaging_demo.py`](../code/imaging_demo.py) require
you to run it and report its actual output. **Every dip must state whether it is
relative or true, and every aperture must carry its calibration relation.**

---

## ★ Foundational

**★1.** State what an image log measures and three things it does not measure.

**★2.** For a 0.20 m hole and a sinusoid amplitude of 0.05 m, compute the dip.

**★3.** State what a breakout azimuth indicates and what a drilling-induced
fracture azimuth indicates, in terms of the principal stresses.

---

## ★★ Applied

**★★4.** Run [`../code/imaging_demo.py`](../code/imaging_demo.py).

(a) Report the aliasing table for $m = 4$ with $P \\in \\{3,4,5,6,8,12\\}$,
including the folded order for each row.
(b) State which pad counts are safe for a bed with a harmonic of order 4, and the
rule that decides it.

---

**★★5.** A horizontal well (90° from vertical) crosses a bed dipping 10°. Using
the relative-dip relation, compute the relative dip and state what an uncorrected
image tool would report and how wrong the resulting structural interpretation would
be.

---

**★★6.** For a conductive trace of anomaly 0.20 and the three exponents of the
lesson, report the three apertures and the range, and state what additional
measurement would constrain the exponent.

---

## ★★★ Research-oriented

**★★★7.** Build a synthetic image of a folded surface with harmonics 1 to 6 and
decreasing amplitude, sample it with 4, 6 and 96 pads, and report the dip bias as a
function of fold amplitude. Compare with the folded-order rule and state where the
rule under-predicts the bias.

---

**★★★8.** Design a stress-orientation study for a field with three wells at
different azimuths: state the number of independent orientation measurements, the
expected dispersion, and the tectonic conclusion you could and could not support.

---

## Reference list used in this problem set

- [05-08-05 lesson](../05-imaging-logs.md)
- [05-07-06 Common Interpretation Pitfalls and False Positives](../../07-interpretation-and-integration/06-interpretation-pitfalls.md)
- [Solutions](./05-imaging-logs-solutions.md)
