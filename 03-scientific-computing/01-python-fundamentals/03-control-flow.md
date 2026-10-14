---
id: 03-01-03
title: "Conditionals, Loops and Loop-Invariant Reasoning"
level: beginner
prereqs: ["03-01-02"]
estimated_minutes: 75
tags: [control-flow, loops, complexity, loop-invariants, survey-reduction]
---

# Conditionals, Loops and Loop-Invariant Reasoning

A survey line is a loop. For each station you read an instrument value, apply a
correction, compare the result against a threshold, and accumulate a total. Every
one of the constructs in this lesson is a decision about that loop: which values
change from station to station, which do not, and what happens when a value is
out of range.

The distinction that matters is **loop-invariant reasoning**. A quantity that
does not depend on the loop index can be computed once — that is hoisting, and it
is worth a measured factor of about 1.6 in the demo below. But the same
distinction is also a *correctness* tool: a quantity that *does* vary, moved
outside the loop by mistake, is a silent error of almost a milliGal in a survey
where the target anomaly is 0.27 mGal. Speed and correctness are the same
question asked twice.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** `if`/`elif`/`else` chains that classify a physical quantity against
   thresholds with stated units, and say why a float equality test is never one of
   those thresholds.
2. **Use** `break`, `continue` and `for`/`else` to express a search, and explain
   what `else` means on a loop.
3. **Apply** `enumerate`, `zip` and generator expressions to remove index
   bookkeeping from a survey loop.
4. **Identify** the loop invariants of a computation, hoist them, and measure the
   gain — while stating honestly that the gain is usually small compared with
   vectorisation.
5. **Detect** a hoisted *variant* as a bug, and quantify its effect on a Bouguer
   reduction.
6. **Implement** a `while` loop for an iterative physical inversion, with a
   convergence test and an honest account of what the residual means.

## Prerequisites

- [03-01-02 Types, Variables, Expressions and Operator Semantics](./02-types-and-variables.md)
  — the arithmetic and the float comparison rules used here.

## 1. Conditionals that classify physics

A conditional in scientific code is almost always a *classification*: is this
anomaly worth following up? Is this elevation out of range? Is this magnitude
above the completeness threshold? Each of those is a comparison against a
threshold with a unit, and each threshold needs a reason.

```text
  peak =  0.0200 mGal  -> at noise level
  peak =  0.2684 mGal  -> a weak target
  peak =  1.5000 mGal  -> a routine exploration target
  peak = 12.0000 mGal  -> a strong target or a regional gradient
```

The structure is unremarkable; the choice of thresholds is not. They are ordered
so that the first matching branch is the smallest anomaly, and the final `else`
catches everything above. Three properties make this a good conditional:

- **Every threshold has a unit and a justification.** "0.05 mGal" is "at the level
  of repeatability for a modern relative gravimeter"; without that, the number is
  arbitrary.
- **The branches are exhaustive.** The `else` is not an afterthought; it is the
  statement that some anomaly is *large*, which is the case that needs a human.
- **Nothing compares floats for equality.** The demo's comment is the point: a
  printed value of `0.268390` is not the stored double `0.26838952765...`, so
  `peak == 0.268390` is `False` and always will be. Classification uses `>=` and
  `<` against thresholds, and equality tests use `math.isclose`.

There is a fourth, subtler property: **the order of the clauses is a
specification.** Written as `if peak >= 12: ... elif peak >= 0.5: ...`, the code
would be equivalent — but written carelessly, with overlapping and non-monotone
thresholds, a value can match two branches and the answer depends on the order.
When a classification has overlapping rules, say so and test both sides of every
boundary. The exercises ask for exactly that.

## 2. Loops as searches, and the `for`/`else` idiom

The most common scientific loop is a search: find the first station where
something is true.

```text
  Looking for the first station where the anomaly drops below
  0.05 mGal (the 'edge' of the body):
    offset     0.0 m: 0.268390 mGal -> still anomalous
    offset   100.0 m: 0.253055 mGal -> still anomalous
    offset   250.0 m: 0.192044 mGal -> still anomalous
    offset   500.0 m: 0.094890 mGal -> still anomalous
    offset   900.0 m: 0.030741 mGal -> first edge found
```

The `else` clause on a `for` loop runs only if the loop finished *without* a
`break`. That is exactly the semantics of "the search failed", and it removes the
need for a sentinel flag:

```python
for x in offsets:
    g = anomaly(x)
    if g < 0.05:
        print(f"first edge at {x} m: {g:.6f} mGal")
        break
else:
    print("no edge within the line")
```

The flag-based alternative — `found = False`, set it inside the loop, test it
after — is where off-by-one errors and inverted conditions live, because it adds
a second piece of state that must be kept consistent with the loop. Use the
language construct instead.

`continue` is the other half of the idiom: skip the remainder of the body for
this iteration and go to the next. In data cleaning it is how you express "this
row is unusable, move on", and it is clearer than nesting the rest of the body
inside an `if`. What it is *not* is a way to hide a problem: a `continue` on a
condition that should be counted (how many rows were skipped?) is a silent data
loss, which is lesson [07](./07-errors-and-debugging.md)'s theme.

`while` is the right loop when the number of iterations is not known in advance —
an iterative solver, a convergence loop, a reader that consumes until the file
ends. Every `while` needs a termination argument: a maximum iteration count, a
tolerance, or both. A `while` without a bound is an infinite loop waiting for a
numerical accident.

## 3. Removing index bookkeeping

Three idioms carry most of the weight in survey code:

```text
  enumerate : [(0, 'STA01'), (1, 'STA02'), (2, 'STA03')]
  zip       : [('STA01', 112.4), ('STA02', 118.9), ('STA03', 121.7)]
  sum/genexp: total lift = 15.8 m
```

- **`enumerate`** gives the index without arithmetic. Writing
  `for i in range(len(stations)): s = stations[i]` invites an off-by-one and reads
  worse; `for i, s in enumerate(stations)` does not.
- **`zip`** walks two sequences in lockstep. It stops at the shorter one, which
  is a footgun: zipping a 5,000-station list with a 4,999-value list silently
  drops a station. Python's `itertools.zip_longest` exists for the case where the
  mismatch should be detected rather than truncated, and an explicit length check
  is better still.
- **Generator expressions** keep a reduction in one line without materialising an
  intermediate list: `sum(e - e0 for e in elevations)` computes total relief
  without building the differences.

None of these is a micro-optimisation. They are edits that make the *intent* of
the loop visible, which is the only reliable defence against index errors in code
that will be read by someone else.

## 4. Worked walkthrough: loop-invariant hoisting, measured

The source mass of the sphere in the forward model does not depend on the station
offset. It does not depend on anything inside the loop. The demo evaluates the
same profile twice — once recomputing the mass inside the loop, once hoisting it —
over 100 000 stations:

```text
  A: mass recomputed inside loop  0.013 s   sum = 13.553669
  B: mass hoisted                 0.008 s   sum = 13.553669
  identical results               True
  speed-up                        1.64x
```

Two observations, one of them about measurement discipline.

**The results are bit-identical.** Hoisting changes *when* a value is computed,
never its value — provided it really is invariant. That is the test: if moving a
computation out of the loop can change the answer, it was not invariant, and your
reasoning about the physics was wrong.

**The gain is modest, and the demo says so.** Repeated runs of the same script
give speed-ups between about 1.1 and 2.1, clustering near 1.6; the spread is
larger than most people expect because the hoisted quantity is two
multiplications and a function call inside a loop body of ten operations. A
single timing of a single run is not a measurement. If you want to claim a
factor, run it ten times and report the spread — which is what lesson
[13](../13-testing-profiling-packaging/README.md) will formalise.

The important part is not the factor. It is that **loop-invariant reasoning is
the same reasoning that makes vectorisation possible.** To hand a loop to NumPy
you must know which operations are elementwise (per-station) and which are
reductions (accumulations). To parallelise a loop you must know which iterations
are independent. To hoist safely you must know which subexpressions are constant.
It is one question, asked at three levels of ambition.

## 5. Physical interpretation: the same invariant test, with teeth

Here is the payoff. A Bouguer reduction removes the attraction of the rock
between the station and the reference level. The infinite-slab term is

$$g_{\text{slab}} = 2\pi G \rho h, \tag{1}$$

linear in the station elevation $h$. For a nominal crustal density
$\rho = 2670$ kg m⁻³ that is

$$2\pi G \rho = 2\pi \times 6.67430\times10^{-11} \times 2670
= 1.12\times10^{-6}\ \text{s}^{-2},$$

which the demo prints as **0.1120 mGal per metre of elevation**.

Now suppose the elevations vary along the line with a synthetic 8 m sine — a
gentle, entirely plausible profile. If the slab term is computed once from the
mean elevation and hoisted out of the loop, the error is the slab gradient times
the deviation:

```text
   station     h (m)  correct (mGal)  hoisted-mean (mGal)  error (mGal)
         0   120.000         13.4363              13.4363        0.0000
       125   125.657         14.0696              13.4363        0.6334
       250   128.000         14.3320              13.4363        0.8958
       500   120.000         13.4363              13.4363        0.0000
       750   112.000         12.5405              13.4363       -0.8958
       875   114.343         12.8029              13.4363       -0.6334
      1000   120.000         13.4363              13.4363        0.0000

  Worst error from hoisting the mean elevation: 0.8958 mGal,
  which is larger than the 0.268 mGal target anomaly of lesson 01.
```

An error of 0.9 mGal, against a target anomaly of 0.27 mGal. The hoisted version
is not merely less accurate; it inverts the sign of the anomaly over part of the
line. And nothing about the code is illegal, and nothing about the output looks
wrong: the curve is smooth, plausible, and *wrong by a factor of three in the
signal you are looking for*.

This is why the invariance test is a correctness tool, not an optimisation
technique. Applied to every quantity in the loop body, it asks: does this change
with the index? Elevation does. Source mass does not. Density, if it is one value
for the whole survey, does not. Density, if it comes from a station-by-station
measurement, does. **Get the answer wrong and you get an anomaly that looks like
data.**

## 6. Worked walkthrough: a `while` loop for an iterative inversion

The peak anomaly of a point mass at the surface, at the epicentre, is
$g = GM/z^2$. Invert it for $z$ and you have a crude depth estimate. Newton's
method solves $f(z) = GM/z^2 - g_{\text{target}} = 0$ by iterating

$$z_{k+1} = z_k - \frac{f(z_k)}{f'(z_k)}, \qquad f'(z_k) = -\frac{2GM}{z_k^3},
\tag{2}$$

which converges quadratically near the root. Starting from a guess of 1000 m for
a true depth of 500 m:

```text
   iteration               z (m)    |change| (m)
           1       500.003519865        5.00e+02
           2       499.999559970        3.96e-03
           3       499.999560017        4.70e-08
           4       499.999560017        5.68e-14
  recovered depth = 499.999560017 m  (true value 500.0 m)
```

Four iterations from a guess 100 per cent too deep, with the number of correct
digits roughly doubling each step.

Three things deserve attention, and all three are the point rather than asides.

**The residual is not solver error.** The recovered depth is
499.999560017 m, which differs from 500 m by $4.4\times10^{-4}$ m. That difference
is *input* error: the target was the rounded value 0.268390 mGal, while the model
peak is 0.26838953 mGal, and

$$\left|\frac{\mathrm{d}z}{\mathrm{d}g}\right| = \frac{z}{2g}
= \frac{500}{2 \times 0.268390} = 931.5\ \text{m per mGal}$$

amplifies the $4.7\times10^{-7}$ mGal rounding to $4.4\times10^{-4}$ m. This is
the same sensitivity calculation as lesson 01, now measured. **An inversion
never does better than its input error times the model's amplification, and the
amplification should be computed, not hoped for.**

**The iteration has two signed roots and the code must choose.** Because $g$
depends on $z^2$, both $+z$ and $-z$ satisfy the equation, and a first Newton step
from 1000 m overshoots straight through zero to about $-500$ m. The demo takes the
magnitude after each step and says why in a comment. A real inversion has the same
character: there are branches, and the code must state which branch it is on.

**The initial guess is part of the algorithm.** From a guess 100 per cent too
deep, convergence takes four iterations. From a nonsense guess of 0.27 m, the same
Newton step grows by a factor of 1.5 per iteration and needs roughly 19 steps just
to get back to the right magnitude. A production solver states its starting
model, its convergence criterion and its iteration cap, and reports when the cap
is hit.

## 7. Worked walkthrough: nested loops and the accumulator pattern

The last section of the demo is the pattern that all grouping follows:

```text
  line  stations  mean h (m)  slab (mGal)
  L1           3      118.33      13.2496
  L2           3      122.33      13.6975
```

An outer loop over groups, an inner loop accumulating within a group. Nothing
here is clever, and that is the point: this is the explicit form of a group-by,
and lesson [05](./05-data-structures.md) shows how to hold the groups in a
dictionary while module [03-04 pandas](../04-pandas/README.md) shows how to
collapse it into one line. Understanding the explicit version is what makes the
one-liner auditable.

## 8. Assumptions and limits

1. **The classification thresholds are nominal.** "0.05 mGal is noise level" is a
   statement about a modern relative gravimeter, not a law. A different instrument
   moves every threshold.
2. **The hoisting measurement is machine- and version-specific.** The ratio is
   about 1.6 on this interpreter; the *direction* (hoisting is not a large win for
   cheap invariants) is general, and the magnitude is not.
3. **Newton's method is local.** Equation (2) converges quadratically near the
   root and can diverge far from it. There is no global convergence guarantee for
   this iteration, and the demo demonstrates a case where it goes backwards
   through zero.
4. **The depth inversion assumes a sphere and a known excess density.** Neither
   holds. The recovered 500 m is a verification of the solver, not a measurement.
5. **`for`/`else` is unusual.** Many readers have never seen it; use it and expect
   to explain it, or use an explicit flag and accept the extra state. Do not use
   it silently in published code.
6. **`while` loops need bounds.** A tolerance-only loop can run forever on
   oscillating input. Always cap the iterations and report when the cap is hit.

## 9. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 control_flow_demo.py
```

Run it three times and watch the hoisting ratio move. That variability is the
lesson's practical takeaway about measurement: a single timing proves nothing, and
the demo is written so that you can see the noise rather than have it hidden by a
tidy figure.

## 10. Common mistakes

1. **`if peak == 0.268390:`** A float equality test on a computed value. Use a
   threshold or `math.isclose`.
2. **Hoisting a loop-variant.** The mean-elevation Bouguer error above is 0.9 mGal
   on a 0.27 mGal signal.
3. **`continue` without counting.** Every skipped iteration is discarded data;
   count it and report it.
4. **`zip` on unequal lengths.** It truncates silently. Check lengths, or use
   `itertools.zip_longest` with an explicit sentinel.
5. **`while` without an iteration cap.** A non-converging solver must terminate
   and say so.
6. **Recomputing `len(x)` or an attribute inside a loop** while believing it is the
   performance problem. It is not, and the belief hides the real one.
7. **Nesting five levels deep.** Deep nesting is a symptom of doing several things
   in one loop; split them into functions (lesson [04](./04-functions-modules.md)).
8. **Index arithmetic when `enumerate` exists.** Every `range(len(...))` with an
   index into the same sequence is an off-by-one candidate.
9. **Reporting a residual as if it were method error.** The 4.4 × 10⁻⁴ m above is
   input rounding, amplified. Say which.
10. **Assuming a loop is the bottleneck before profiling.** Measure, then decide;
    the answer is often I/O or memory, not the arithmetic.

## 11. Real-world applications

- **Survey reduction.** Free-air, Bouguer, terrain and drift corrections are all
  per-station operations with loop-variant arguments. The slab term above is the
  simplest of them, and the one people hoist by accident.
- **Catalogue processing.** Classifying events by magnitude, filtering by depth,
  and searching for the first event above a threshold are the loop idioms of
  observational seismology.
- **Iterative solvers.** Almost every inverse problem is a `while` loop with a
  convergence test and a maximum iteration count — conjugate gradients, Gauss-
  Newton, simulated annealing. The discipline in §6 is the discipline of module
  [18 Inverse Problems](../../18-inverse-problems/README.md) in miniature.
- **Grid traversal.** Nested loops over x and y are the beginning of every
  finite-difference stencil, which module
  [03-12](../12-numerical-simulation-python/README.md) develops into a real solver.

## 12. Further reading

- NumPy — [numpy.org](https://numpy.org): the array operations that replace the
  inner loops here; module [03-02](../02-numpy/README.md).
- SciPy — [scipy.org](https://scipy.org): `scipy.optimize` provides the robust
  versions of the Newton iteration written by hand in §6; module
  [03-03](../03-scipy/README.md).

## 13. Related lessons

- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) — how
  to package the loop body so it can be tested on one station.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](./05-data-structures.md)
  — why the inner accumulation loop is O(n) and the lookups inside it need not be
  O(n) each.
- [03-01-02 Types, Variables, Expressions and Operator Semantics](./02-types-and-variables.md)
  — the float comparison rules the thresholds rely on.
- [01-12 Numerical Methods](../../01-mathematics/12-numerical-methods/README.md)
  — convergence orders and the analysis behind Newton's method.

## 14. Exercises

[`exercises/03-control-flow-exercises.md`](./exercises/03-control-flow-exercises.md) —
eight problems, ★ to ★★★. Problem ★★5 requires the hoisting and Newton
measurements; problem ★★6 computes the 25 m relief error, and problem ★★★7 asks
you to prove a quantity is loop-invariant before hoisting it.

## 15. Self-assessment checklist

- [ ] I can write a threshold classification with units on every threshold.
- [ ] I can explain what `for ... else` does and when a `break` suppresses it.
- [ ] I can rewrite an indexed loop with `enumerate` or `zip`.
- [ ] I can state the invariant test and apply it to every line of a loop body.
- [ ] I can explain why hoisting the mean elevation produced a 0.8958 mGal error.
- [ ] I can write a bounded `while` loop with a convergence criterion and a
      residual that I can interpret physically.
- [ ] I can compute $\mathrm{d}z/\mathrm{d}g = z/(2g)$ for a peak-anomaly
      inversion and say what it means for the accuracy of a depth estimate.
