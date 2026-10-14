# Solutions — 03-01-03 Conditionals, Loops and Loop-Invariant Reasoning

> **Read this after attempting the exercises, not before.** Numbers attributed to
> the demo are its actual printed output; the rest are computed and shown.

---

## ★1 — A classification with unit-bearing thresholds

```python
def classify_anomaly(peak_mgal):
    """Classify a peak anomaly in mGal."""
    g = abs(peak_mgal)
    if g < 0.01:
        return "below instrument noise"
    elif g < 0.5:
        return "weak target"
    elif g < 5.0:
        return "routine exploration target"
    else:
        return "strong target"
```

**(a)** 0.01 mGal (repeatability of a good relative gravimeter), 0.5 mGal (below
the threshold at which an anomaly is usually worth a follow-up line), 5 mGal
(above which regional gradients and terrain effects dominate).

**(b)** Because the quantity is a computed double. Two values that print the same
to six decimals are different doubles; `==` on a float is a test of bitwise
identity, not of agreement. Thresholds are comparisons of *magnitude*, and the
boundary convention (`>=` for the lower bin) is what makes the bins exhaustive and
non-overlapping.

**(c)** Because the function uses `abs`, the boundaries are $g = 0.01, 0.5, 5.0$
with the *smaller* bin taking `g < threshold`. At exactly 0.01 the result is
`"weak target"`; at exactly 0.5, `"routine exploration target"`; at exactly 5.0,
`"strong target"`. Just below each boundary ($10^{-6}$ mGal less) the result is the
lower bin. Every boundary behaves as specified: each threshold belongs to the bin
*above* it, and the classes are exhaustive over all real inputs.

Note what the test *does not* establish: that the thresholds are physically
sensible. Only the survey's noise level and geology can do that, which is why (a)
is part of the question.

---

## ★2 — Idiom rewrites

**(a)**

```python
base = elevations[0]                     # hoisted: genuinely invariant
total = sum(e - base for e in elevations)
```

Removes: the index arithmetic and the repeated `elevations[0]` lookup; the
`base` hoist makes the loop-instant nature of the reference explicit.

**(b)**

```python
for i, (station, height) in enumerate(zip(stations, heights)):
    print(i, station, height)
```

Removes: two index lookups per iteration and the possibility of the two sequences
being walked out of step. Note the caveat: `zip` truncates at the shorter
sequence, so if the two lists may differ in length, assert
`len(stations) == len(heights)` first.

**(c)**

```python
for h in heights:
    if h < 0.0:
        first = h
        break
else:
    first = None
```

Removes: the sentinel flag `found`, which is exactly the state that goes stale.

---

## ★3 — Invariant or not

| Quantity | Invariant? | Reason |
|---|---|---|
| (a) Source mass $M$ | **Invariant** | Depends on $a$ and $\Delta\rho$, neither of which depends on the station |
| (b) Station elevation $h$ | **Variant** | It is indexed by the station — this is the 0.8958 mGal bug if hoisted |
| (c) Slab gradient $2\pi G\rho$ | **Invariant** if $\rho$ is one survey-wide value; **variant** if $\rho$ varies by station | The invariance is a property of the *problem*, not the formula |
| (d) Free-air correction | **Variant** | Linear in $h$, so it varies exactly as $h$ does |
| (e) Calibration factor from a per-station header | **Variant** | The code *looks* like it should be invariant, which is what makes it dangerous: invariance is decided by the data's structure, not by the code's appearance |

(d) and (e) are the cases that matter. Both are expressions that "look constant"
because they are multiplications by a named constant; both are loop-variant
because the other factor changes per iteration.

---

## ★4 — Bounded Newton iteration for a square root

```python
def sqrt_newton(a, rel_tol=1e-12, max_iter=30):
    if a <= 0:
        raise ValueError("a must be positive")
    x = a / 2.0
    for i in range(1, max_iter + 1):
        x_next = 0.5 * (x + a / x)
        if abs(x_next - x) <= rel_tol * abs(x_next):
            return x_next, i
        x = x_next
    raise RuntimeError(f"no convergence in {max_iter} iterations")
```

**(a)** $a = 2$: starting from 1.0, the iterates are 1.0, 1.5, 1.416666…,
1.414215686…, 1.4142135623… — converging to a relative tolerance of $10^{-12}$ in
**5** iterations.

**(b)** $a = 10^{12}$: starting from $5\times10^{11}$, the iterates are
$2.5\times10^{11}$, $1.25\times10^{11}$, $6.25\times10^{10}$,
$3.1252\times10^{10}$, … — the same dozen-ish halvings of the relative error, so
the count lands within one iteration of (a): **5–6** iterations.

**(c)** The iteration count is logarithmic in the *relative* error, and the
relative error is dimensionless. Scaling $a$ by $10^{12}$ scales every iterate by
the same factor, so the ratio between successive errors is unchanged. What does
change with $a$ is the number of *significant digits* the answer must carry: a
relative tolerance of $10^{-12}$ is 12 digits regardless of magnitude, so the
iteration count is essentially independent of $a$, while the number of digits
required to *state* the result grows with $\log_{10}a$.

---

## ★5 — The demo's hoisting and Newton measurements

```text
  A: mass recomputed inside loop  0.013 s   sum = 13.553669
  B: mass hoisted                 0.008 s   sum = 13.553669
  identical results               True
  speed-up                        1.64x
```

**(a)** 0.013 s and 0.008 s, speed-up 1.64× on this run.

**(b)** Yes — `identical results  True`. The sums are bit-identical, which is the
observable consequence of hoisting changing *when* a value is computed and not its
value.

**(c)**

```text
   iteration               z (m)    |change| (m)
           1       500.003519865        5.00e+02
           2       499.999559970        3.96e-03
           3       499.999560017        4.70e-08
           4       499.999560017        5.68e-14
```

The successive differences 5.00 × 10², 3.96 × 10⁻³, 4.70 × 10⁻⁸, 5.68 × 10⁻¹⁴
fall by factors of $1.3\times10^{5}$, $8.4\times10^{4}$ and $8.3\times10^{5}$. The
ratio of successive *differences* is not constant (that would be linear
convergence) and the *number of correct digits* roughly doubles each step (linear
in the log of the error, i.e. quadratic convergence).

**Two reasons the ratio is noisier than the individual times.**

1. **Both times are short.** At 8–13 ms, the measurement is comparable to
   scheduling jitter, cache and branch-predictor warm-up, and any background load;
   each individual time carries a few per cent of noise, and the ratio of two such
   numbers carries the sum of the relative errors.
2. **The two versions differ by a small absolute amount.** A hoisted call that
   saves about 5 ms out of 13 ms is a difference of 60 per cent of the *loop body*,
   but the two runs also differ in memory access patterns and in how the
   interpreter's specialising optimiser warms up, so the *difference* varies more
   between runs than either time does.

---

## ★6 — The 25 m of relief

**(a)** $2\pi G\rho = 2\pi \times 6.67430\times10^{-11} \times 2670
= 1.11969\times10^{-6}$ s⁻², which in mGal per metre is
$1.11969\times10^{-6}/10^{-5} = 0.111969$ mGal m⁻¹. The demo prints **0.1120 mGal
per metre of elevation**.

**(b)** Worst case is the full half-range of 25 m (if the relief is symmetric about
the mean, the extreme station is 12.5 m from the mean — but the *specified* worst
case is the full 25 m span, which is also the answer if the "mean" used was the
first station's elevation rather than the arithmetic mean). Taking the stated
25 m:

$$25 \times 0.111969 = 2.7992\ \text{mGal}.$$

If instead the hoisted value is the true arithmetic mean of a symmetric profile,
the worst-case deviation is 12.5 m and the error is 1.3996 mGal. State which
convention you used; the lesson's demo uses a mean 8 m from the extremes and gets
0.8958 mGal, consistent with $8 \times 0.111969 = 0.8958$.

**(c)** $2.7992 / 0.3 = 9.3$, i.e. the error is more than nine times the target
signal. **The survey is not salvageable by post-hoc correction**, because the
hoisted version never recorded the per-station elevation in the reduced value; the
information needed to undo the error is not in the output. Re-processing from the
raw data is the only fix, which is exactly why the mistake is expensive.

**(d)** A 0.3 m elevation error moves the slab term by
$0.3 \times 0.111969 = 0.0336$ mGal = 33.6 µGal per station. That is 1.2 per cent
of the (b) error — a real but small contribution, and it is the *random* part of
the error budget, whereas (b) is a systematic, spatially correlated error that
looks like structure.

---

## ★7 — Proving invariance

**(a)** $g(x) = GMz/(x^2+z^2)^{3/2}$.

| Symbol | Status | Why |
|---|---|---|
| $G$ | invariant | a physical constant |
| $M$ | invariant | depends on $a$, $\Delta\rho$ — no station dependence |
| $z$ | invariant | the body's depth, fixed for the model |
| $x$ | **variant** | the loop variable |
| the exponent $3/2$ | invariant | a constant |
| $(x^2+z^2)$ | **variant** | contains $x$ |

**(b)** `r3 = (x0**2 + z**2)**(-1.5)` with `x0 = 0` gives `r3 = z^-3`. Reusing it
at $x = 1000$ m computes $g_{\text{wrong}} = GM z \cdot z^{-3} = GM/z^2 = 0.268390$
mGal (the peak), whereas the correct value is

$$g(1000) = \frac{GMz}{(1000^2+500^2)^{3/2}} = 0.024005\ \text{mGal},$$

which the lesson's demo prints as `1000.0         0.024005`. The error is
$0.268390 - 0.024005 = 0.244385$ mGal — **the hoisted version is eleven times too
large at that station**, and the error is largest far from the body, which is
exactly where the anomaly should be smallest. A hoisted variant does not add a
constant offset; it changes the shape, and it changes it most where the signal is
least.

**(c)** The test: *does the subexpression's value depend on any loop variable, or
on anything computed from one?* If not, it may be hoisted. A compiler may perform
the hoist safely when the subexpression is pure — no side effects, no dependence on
mutable state that the loop body modifies — and when the transformation preserves
the floating-point result; the second condition is why optimising compilers are
conservative about reassociating floating-point expressions, and why Python's
interpreter does not hoist anything at all.

---

## ★8 — Three proposals

**(a) Hoist both terms?** No. Both are loop-variant: the slab term depends on
$h_i$ and the free-air term depends on $h_i$. Hoisting either computes one value
and applies it to every station, which is the 2.8 mGal error of ★6(b) in the slab
term and a comparable error in free-air. The proposal is physically wrong, not
merely unhelpful.

**(b) Hoist the gradient.** Correct and worth doing. $2\pi G\rho$ is invariant
when $\rho$ is a survey-wide constant; the loop body then performs one
multiplication instead of two multiplications, a $\pi$, a square root-free
constant expression and a division by $10^{-5}$. Estimate the *invariant
fraction*: from the profiling, 60 per cent of the time is in the slab term, and of
that term the invariant part is perhaps half — so about 30 per cent of the total
runtime is hoistable. Amdahl's law gives a speed-up of

$$S = \frac{1}{(1 - 0.30)} = 1.43.$$

So a 30 per cent saving gives a 1.43× speed-up — worth having, and the same order
as the demo's measured 1.64× on its own loop.

**(c) Vectorisation is a different kind of optimisation.** Hoisting reduces the
*number of operations* by a constant factor and leaves the loop interpreted, so it
is bounded by Amdahl's law and by how much of the body is invariant. Vectorisation
removes the interpreter's per-operation overhead from the whole kernel, moving the
arithmetic into compiled code, and the lesson's own measurements show the two
scales: hoisting bought 1.64×, whereas the same class of numerical code in a
compiled loop is reported in the demo as roughly 10×–100× faster than the
interpreted equivalent. **Do (b) first**: it is free, it is safe, and it is the
same reasoning that tells you which parts of the kernel can be handed to NumPy at
once. Do (c) second, and only after measuring.

---

## ★9 — The invariance test as a correctness tool

*Model answer in outline, ~400 words. Your own wording should contain at least the
following elements.*

**The computation.** The Bouguer slab correction is $2\pi G\rho h$. For a nominal
crustal density of 2670 kg m⁻³ the gradient is
$2\pi \times 6.67430\times10^{-11} \times 2670 = 1.1197\times10^{-6}$ s⁻², or
**0.11197 mGal per metre of elevation**. A line whose elevations vary by ±8 m about
their mean therefore needs a slab term that varies by
$\pm 8 \times 0.11197 = \pm 0.8958$ mGal. Hoisting the term computed at the mean
elevation discards all of that variation, and the discarded amount is a systematic
function of position along the line.

**The class of survey it destroys.** The error is 0.8958 mGal against a target
anomaly of 0.268 mGal — a factor of 3.3. So it destroys:
microgravity monitoring (signals of 5–50 µGal), any survey whose target is a
compact body of modest density contrast (lesson 01's 0.268 mGal sphere), and any
survey in which the residual anomaly is comparable to the topographic relief term.
It does *not* destroy a regional Bouguer map with anomalies of tens of mGal, which
is why the bug survives review: the map "looks right", because a spatially smooth
0.9 mGal error looks like structure and is not obviously wrong.

**The line of code that makes it possible.**

```python
slab = bouguer_slab_mgal(mean_elevation)      # computed once, outside the loop
for station in line:
    anomaly[station] = observed[station] - slab
```

Everything about that code reads as an optimisation: the value is computed once
and reused, which is exactly the advice of every performance guide. The only thing
wrong with it is that the reused value depends on the station, and nothing in the
code says so.

**The conclusion.** The invariance test — *does this subexpression depend on the
loop variable?* — is the same question that decides whether an operation may be
hoisted, vectorised, or parallelised. Because it is asked about *data*, not about
speed, it is a correctness question first: a hoisted variant produces a
plausible-looking, smoothly wrong result, and the only reliable defence is to
classify every symbol in the loop body as invariant or variant **before** moving
anything.
