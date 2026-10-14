# Exercises — 03-01-03 Conditionals, Loops and Loop-Invariant Reasoning

Attempt these **closed-book** before opening the
[solutions](./03-control-flow-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/control_flow_demo.py`](../code/control_flow_demo.py) require you to run
it and report its **actual** output. Show your units.

---

## ★ Foundational

**★1.** Write a function `classify_anomaly(peak_mgal)` that returns one of

- `"below instrument noise"` for $|g| < 0.01$ mGal,
- `"weak target"` for $0.01 \le |g| < 0.5$ mGal,
- `"routine exploration target"` for $0.5 \le |g| < 5$ mGal,
- `"strong target"` otherwise.

(a) State the unit of every threshold.
(b) Explain why the conditions use `<` and `>=` and not `==`.
(c) Test it at $g = 0.01$, $0.5$ and $5.0$ exactly, and at each boundary minus
$10^{-6}$ mGal. Report the outputs and say whether every boundary behaves as
specified.

---

**★2.** Rewrite each loop in the idiom the lesson recommends, and say what the
rewrite removes.

```python
# (a)
total = 0.0
for i in range(len(elevations)):
    total += elevations[i] - elevations[0]

# (b)
for i in range(len(stations)):
    print(i, stations[i], heights[i])

# (c) find the first station below sea level
found = False
for h in heights:
    if h < 0.0:
        found = True
        first = h
        break
if not found:
    first = None
```

---

**★3.** For each quantity, say whether it is **loop-invariant** with respect to a
loop over stations, and why.

(a) The source mass $M$ of a buried sphere.
(b) The station elevation $h$.
(c) The Bouguer slab gradient $2\pi G \rho$ when $\rho$ is a single survey-wide
reference density.
(d) The free-air correction $0.3086\,h$.
(e) The instrument's calibration factor, if it is read once per station from a
per-station header.

---

## ★★ Applied

**★★4.** Write a bounded `while` loop that computes $\sqrt{a}$ by Newton's method
to a relative tolerance of $10^{-12}$, with a maximum of 30 iterations, from an
initial guess of $a/2$.

(a) Report the iteration count for $a = 2$.
(b) Report the iteration count for $a = 10^{12}$.
(c) Explain why the iteration count barely changes with $a$, and what that says
about the number of *significant digits* versus the number of *iterations*.

---

**★★5.** Run `python3 control_flow_demo.py` and report:

(a) the two hoisting timings and the speed-up;
(b) whether the two sums are bit-identical;
(c) the four Newton iterations' $z$ values and their successive differences.

Then answer: the demo's speed-up varies between runs (the lesson quotes a range of
about 1.1 to 2.1). State two reasons the *ratio* is noisier than the individual
times.

---

**★★6.** A survey line has 25 m of relief, symmetric about the mean elevation,
and is reduced with a nominal density of 2670 kg m⁻³.

(a) Compute the slab gradient in mGal per metre.
(b) Compute the worst-case error if the slab term is computed once from the mean
elevation and hoisted out of the loop.
(c) The target anomaly is 0.3 mGal. Express the worst-case error as a fraction of
the target, and state whether the survey is salvageable by post-hoc correction.
(d) The instrument's barometric elevation error is 0.3 m. Compute the resulting
Bouguer error per station and compare it with (b).

---

## ★★★ Research-oriented

**★★★7.** Prove invariance before hoisting.

(a) For the point-mass anomaly $g(x) = GMz/(x^2+z^2)^{3/2}$, list every symbol and
classify each as loop-invariant or loop-variant with respect to a loop over $x$.
(b) A colleague hoists $G$, $M$, $z$ and the constant $z$ but also hoists
$(x^2+z^2)^{-3/2}$ into a variable `r3`. Show by substitution that `r3` is
loop-variant, and compute the anomaly error at $x = 1$ km, $z = 500$ m if `r3` is
evaluated at $x = 0$ and reused.
(c) State the general test you would apply to decide hoistability, in one sentence,
and give the condition under which the compiler may perform the hoist safely.

---

**★★★8.** A processing script reduces 10⁶ stations. Profiling shows 60 per cent of
the time in the per-station slab term $2\pi G \rho h_i$ and 40 per cent in the
free-air term $0.3086\,h_i$.

(a) One colleague proposes hoisting both terms out of the loop. Evaluate the
proposal physically and numerically.
(b) A second colleague proposes computing the *gradient* $2\pi G \rho$ once and
multiplying by $h_i$ inside the loop. Evaluate this proposal and estimate the
speed-up from Amdahl's law, stating the fraction of time that is the invariant
recomputation.
(c) A third proposes vectorising the whole loop with NumPy. Without using NumPy,
argue from the lesson's measured numbers why this is a different *kind* of
optimisation from (b) — and say which you would do first.

---

**★★★9.** Write a one-page note (350–450 words) on why the *loop-invariance test*
is a correctness tool before it is a performance tool, using the 0.8958 mGal
elevation-hoisting error as your worked example. Your note must contain: the
computation of the worst-case error, a statement of the class of survey that the
error would destroy, and the single line of code that makes the bug possible.
