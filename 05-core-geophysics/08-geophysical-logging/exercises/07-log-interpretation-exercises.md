# Exercises — 05-08-07 Log Interpretation, Petrophysics and Uncertainty

Attempt these **closed-book** before opening the
[solutions](./07-log-interpretation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/petrophysics_demo.py`](../code/petrophysics_demo.py) require you to run it
and report its actual output. **Every answer must carry an uncertainty and name the
model it used; a saturation without either is not an answer.**

---

## ★ Foundational

**★1.** List the five stages of the standard petrophysical workflow and name one
constant each contains.

**★2.** Convert a measured depth of 2500 m at 25° deviation to true vertical depth.

**★3.** State the difference between a cement bond log and a flow log, and what
each establishes.

---

## ★★ Applied

**★★4.** Run [`../code/petrophysics_demo.py`](../code/petrophysics_demo.py).

(a) Report the point estimate of $S_w$ and the 90 per cent interval.
(b) Recompute the point estimate with $m = 1.8$ and $R_w = 0.15$ Ω m.
(c) State which of the two changes moves the answer more and why.

---

**★★5.** Two logs are depth-matched with a residual 0.35 m misfit. Compute the
fractional thickness error for beds of 0.5, 1, 3 and 10 m, and state which
interpretation is affected most.

---

**★★6.** For a net-to-gross of $0.42 \\pm 0.06$, mean porosity $0.171 \\pm 0.021$ and
hydrocarbon saturation $0.523 \\pm 0.207$ (the 90 per cent half-interval from the
lesson, treated as 1σ for this exercise), compute the volumetric uncertainty by
first-order propagation and state the dominant term.

---

## ★★★ Research-oriented

**★★★7.** Build a complete synthetic well from rock physics (Gassmann plus a
stated velocity–porosity model), forward-model all logs, and run the whole workflow
including depth matching and environmental corrections. Report the $S_w$ error for
layers where (a) all assumptions hold, (b) the mineralogy is wrong, (c) the rock is
shaly and Archie is used anyway. Rank the three.

---

**★★★8.** Design an acquisition programme that would halve the saturation
uncertainty of the lesson's §3.2. State what is measured, how it constrains the
dominant term, its cost in principle, and the residual uncertainty. Then state the
observation that would prove your programme unnecessary.

---

## Reference list used in this problem set

- [05-08-07 lesson](../07-log-interpretation.md)
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](../../07-interpretation-and-integration/05-reporting-results.md)
- [Solutions](./07-log-interpretation-solutions.md)
