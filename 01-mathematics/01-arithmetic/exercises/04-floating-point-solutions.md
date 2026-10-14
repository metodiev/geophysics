# Solutions — 01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Every numeric value below was produced by running
> the stated computation (Python 3, standard library only) rather than estimated
> by hand. Where an answer depends on the machine or the interpreter version,
> that is stated explicitly.

---

## ★1 — Machine epsilon, unit roundoff, and the threshold at 1

**(a)** $\varepsilon_{\text{mach}} = 2^{-52} = 2.220446049250313\times10^{-16}$.

**(b)** $u = \tfrac{1}{2}\varepsilon_{\text{mach}} = 2^{-53}
= 1.110223024625157\times10^{-16}$.

**(c)** $53\log_{10}2 = 15.9546$, so **about 16** digits are carried in total,
and **15** are guaranteed without an argument about how the rounding falls.
Python reports the guaranteed figure directly as `sys.float_info.dig == 15`.

The three checks:

| expression | differs from 1.0? | reason |
|---|---|---|
| `1.0 + 1e-17` | **no** | $10^{-17} \ll 2^{-53}$, so the exact sum rounds back to $1$ |
| `1.0 + 1e-16` | **no** | $10^{-16} < 2^{-53} = 1.11\times10^{-16}$; still rounds to $1$ |
| `1.0 + 2.3e-16` | **yes** | $2.3\times10^{-16} > 2^{-52}$, i.e. more than one ulp |

Verified: `1.0 + 1e-17 == 1.0` is `True`, `1.0 + 1e-16 == 1.0` is `True`, and
`1.0 + 2.3e-16` is `1.0000000000000002`.

**The threshold to remember.** The smallest value that changes $1.0$ is *just
above* $2^{-53}$. Exactly $2^{-53}$ is a tie between $1.0$ and
$1.0 + 2^{-52}$, and ties-to-even sends it back to $1.0$. So the practical rule
is: additions smaller than $u = 2^{-53}$ relative to the running total are lost.

---

## ★2 — ulp and the magnitude rule

| $x$ | `math.ulp(x)` |
|---|---|
| $1$ | $2.220446049250313\times10^{-16}$ |
| $1000$ | $1.136868377216160\times10^{-13}$ |
| $10^{6}$ | $1.164153218269348\times10^{-10}$ |
| $10^{16}$ | $2.0$ |

**Rule.** If $2^{k} \le |x| < 2^{k+1}$, then
$\mathrm{ulp}(x) = 2^{k-52}$. In words: *the gap doubles with every doubling of
the magnitude*, so the **relative** spacing is bounded by
$\varepsilon_{\text{mach}} = 2^{-52}$ for every normal number.

That is the precise sense in which floating point has "constant relative
precision and variable absolute precision". It is the opposite of a fixed-point
representation.

**The check.** `1.0 - 0.4 == 0.6` evaluates to **`True`**, and that is a trap
rather than a proof of exactness. The exact decimal expansion of the computed
difference is

$$0.59999999999999997779553950749686919152736663818359375,$$

which is not $0.6$. But $0.6$ is itself not representable (denominator $5$), so
the literal `0.6` is the *same* binary64 value as that difference, and the
comparison succeeds because both sides are equally "wrong".

The subtraction is in fact exact *for the two stored operands*:
$\mathrm{fl}(1.0) - \mathrm{fl}(0.4)$ has an exactly representable result. The
error entered earlier, in storing $0.4$. So the honest reading is: the arithmetic
is not the problem here, and the equality test tells you nothing about whether
the numbers are the mathematical $1.0$, $0.4$ and $0.6$.

---

## ★3 — Which decimals are exactly representable

**Criterion.** Write the number in lowest terms as $p/q$. It is exactly
representable in binary if and only if $q$ is a power of two. The reason is the
binary point: $x = p/2^{n}$ is a finite binary expansion with $n$ fractional
bits, whereas any factor of $5$, $3$, $7,\dots$ in the denominator produces a
repeating binary expansion, just as a factor of $3$ in a decimal denominator
produces a repeating decimal.

| number | lowest terms | exact in binary64? |
|---|---|---|
| $0.5$ | $1/2$ | **yes** |
| $0.25$ | $1/4$ | **yes** |
| $0.75$ | $3/4$ | **yes** |
| $3/8$ | $3/8$ | **yes** |
| $0.1$ | $1/10 = 1/(2\cdot5)$ | **no** |
| $0.2$ | $1/5$ | **no** |
| $1/3$ | $1/3$ | **no** |

Verified with `Decimal`: `Decimal(0.5) == Decimal("0.5")` is `True`, and
`Decimal(0.1) == Decimal("0.1")` is `False`.

**Scope note.** This is about *representation*. A value may still be recovered
exactly by a computation (integer arithmetic on exactly representable inputs),
which is why `0.5 + 0.25 == 0.75` is `True`.

---

## ★4 — `0.1 + 0.2`

**(a)** `0.1 + 0.2 == 0.3` is **`False`**; the sum is
`0.30000000000000004`.

**(b)** The exact stored value of the sum is

$$0.3000000000000000444089209850062616169452667236328125,$$

and the exact stored value of `0.3` is

$$0.299999999999999988897769753748434595763683319091796875.$$

**(c)** The computed sum is **larger** than $0.3$ by

$$\frac{0.3000000000000000444\ldots - 0.3}{0.3} \approx 1.5\times10^{-16},$$

which is one unit roundoff, the smallest relative discrepancy the format can
express at this magnitude. The two stored values differ by one ulp
($5.55\times10^{-17}$ absolute, $1.85\times10^{-16}$ relative).

**Why this is not a "bug".** `0.1` and `0.2` each enter as their nearest doubles;
their exact sum is then rounded once more. Three roundings, each at most $u$
relative, compose into a discrepancy of order $u$. Any language using IEEE 754
binary64 behaves this way.

---

## ★★5 — Cancellation in $(1-\cos x)/x^{2}$

**(a)** Naive evaluation against the limit $1/2$:

| $x$ | naive value | relative error |
|---|---|---|
| $10^{-4}$ | $0.4999999969613$ | $5.24\times10^{-9}$ |
| $10^{-6}$ | $0.5000444502912$ | $8.89\times10^{-5}$ |
| $10^{-8}$ | $0.0000000000000$ | $1.0$ (total loss) |

**(b)** The half-angle identity: $\cos x = 1 - 2\sin^{2}(x/2)$, so
$1 - \cos x = 2\sin^{2}(x/2)$ and

$$f(x) = \frac{2\sin^{2}(x/2)}{x^{2}}.$$

Verified values of this form: $0.4999999995833$ at $x=10^{-4}$,
$0.5000000000000$ at $x=10^{-6}$, and $0.5000000000000$ at $x = 10^{-8}$ — all
correct to the digits printed.

**(c)** The naive form returns exactly `0.0` at $x = 10^{-8}$ (and stays at zero
for smaller $x$). Mechanism: $\cos x$ rounds to exactly $1.0$ once
$x^{2}/2 < u$, so the numerator $1-\cos x$ is computed as $1.0 - 1.0 = 0.0$ and
the true magnitude $x^{2}/2 \approx 5\times10^{-17}$ is annihilated.

**(d)** Ship the half-angle (or an equivalent series) form. The reason is
*relative* error: in the naive form the numerator is a difference of two
quantities of size $1$ whose answer is of size $x^{2}/2$, so the relative error
is amplified by $2/x^{2}$ — it grows without bound as $x\to0$. The rewritten
form has no such amplification, and its relative error stays at the level of the
final division. This pattern appears whenever an instrument or a formula
differences two nearly equal outputs: two-way travel times, phase differences,
and Bouguer anomalies all share it.

---

## ★★6 — Growth of the naive summation error

**(a)** Dividing each error by $n^{2}$:

| $n$ | error | error / $n^{2}$ |
|---|---|---|
| $10^{4}$ | $1.588\times10^{-10}$ | $1.588\times10^{-18}$ |
| $10^{5}$ | $1.885\times10^{-8}$ | $1.885\times10^{-18}$ |
| $10^{6}$ | $1.333\times10^{-6}$ | $1.333\times10^{-18}$ |
| $10^{7}$ | $1.610\times10^{-4}$ | $1.610\times10^{-18}$ |

The ratio is nearly constant at about $1.6\times10^{-18}$. Since
$\text{error} \approx C n^{2}$, the error grows **quadratically** in $n$ over
this range — far worse than the $\mathcal{O}(n)$ growth one might naively expect,
and the signature of rounding errors that share a sign rather than cancelling.

**Why quadratic is plausible.** The rounding at step $k$ is proportional to the
partial sum $\approx 0.1k$, so it is of order $u\cdot0.1k$. If those roundings
accumulate systematically, the total is
$\sum_{k\le n} u\cdot0.1k \approx u\cdot0.1\,n^{2}/2 = 5.55\times10^{-18}n^{2}$,
which is the right order of magnitude (observed coefficient $1.6\times10^{-18}$,
about a factor of 3.5 smaller).

**(b)** With $C \approx 1.6\times10^{-18}$, the prediction at $n=10^{8}$ is

$$C n^{2} = 1.6\times10^{-18}\times10^{16} = 1.6\times10^{-2}.$$

That is an absolute error of about $0.016$ on a total of $10^{7}$ — a relative
error of $1.6\times10^{-9}$.

The prediction assumes (i) the quadratic form and its coefficient persist to
$n=10^{8}$, and (ii) the value being summed and the summation order are
unchanged. It does **not** assume that the coefficient is universal: change the
addend, the order, or the interpreter's evaluation, and the coefficient will
move.

**(c)** For $n = 10^{6}$:

| method | result |
|---|---|
| explicit accumulation loop | `100000.00000133288` |
| Kahan compensated | `100000.0` |
| `math.fsum` | `100000.0` |

The exact answer is $10^{5} = 100000$. Both compensated routes are exact *to the
format* here; the loop is not.

**(d)** With $u = 2^{-53}$ and $\sum|x_k| = 10^{5}$,

$$(n-1)\,u\sum|x_k| = (10^{6}-1)\times1.1102\times10^{-16}\times10^{5}
= 1.110\times10^{-5}.$$

The observed error is $1.333\times10^{-6}$, so the bound is about **8× larger**
than reality. It is a genuine upper bound (correct order of magnitude, correct
scaling in $n$) but not tight, because it assumes every rounding is maximal and
identically signed. Do not read such bounds as forecasts; read them as
worst-case guarantees.

---

## ★★7 — Mixed magnitudes

**(a)** Explicit loop from `0.0`:

```text
0.0 + 1e16    = 1e16
1e16 + 1.0    = 1e16        (the 1 is below the ulp of 1e16)
1e16 - 1e16   = 0.0
```

Verified result: **`0.0`**, while the true sum is $1.0$.

**(b)** `math.fsum([1e16, 1.0, -1e16])` gives **`1.0`** — exactly right, because
`fsum` accumulates the exact sum and rounds once.

**(c)** The built-in `sum()` also gives **`1.0`**. Since CPython 3.12, `sum()`
applies compensated (Neumaier) summation to floats, so it is no longer naive.
Implication: in modern Python the *loop you write by hand* is the naive
construct, not `sum()`. Code that "avoids `sum` for accuracy" and writes an
explicit loop has it exactly backwards.

**(d)** Order that makes the loop exact:
`[1e16, -1e16, 1.0]` — the $1e16$ terms cancel first, leaving
$0.0 + 1.0 = 1.0$. Sorting by magnitude (ascending) and accumulating small
values first achieves the same effect more generally: the small terms combine
with each other before meeting a large one that would swallow them.

---

## ★★8 — Anomaly from a difference of large numbers

**(a)** $\;979\,812.37 - 979\,802.15 = 10.22$ mGal.

**(b)** The ratio is

$$\frac{979\,812.37}{10.22} = 9.59\times10^{4}, \qquad
\log_{10} = 4.98,$$

so about **five decimal digits** of each datum are shared with the other and
carry no information about the anomaly. Only the last digits matter.

**(c)** With $u = 1.11\times10^{-16}$, each datum carries an absolute
representation error of order

$$979\,812.37 \times 1.11\times10^{-16} = 1.09\times10^{-10}\ \text{mGal},$$

which is a relative error of

$$\frac{1.09\times10^{-10}}{10.22} = 1.06\times10^{-11}$$

in the anomaly — about $10^{-11}$, i.e. eleven significant digits survive the
subtraction even though five were consumed by the common part.

**(d)** The instrument resolution, of order $0.01$ mGal, is about
$1.0\times10^{8}$ times larger than the floating-point error estimated in (c).
**Measurement dominates completely**; the floating-point error is irrelevant at
this station. This is the normal situation in potential-field work, and it is
why the careful floating-point treatment of Section 4.3 of the lesson matters
only for the *modelling* side, where a theoretical field may be differenced
repeatedly over millions of cells.

---

## ★★9 — The stable quadratic formula

Coefficients: $a = 1$, $b = -10^{8}$, $c = 1$; discriminant
$\sqrt{b^{2}-4ac} = \sqrt{10^{16}-4}$.

**(a)** Naive formulas:

| root | value |
|---|---|
| $x_1 = (-b + \sqrt{\cdot})/(2a)$ | `100000000.0` |
| $x_2 = (-b - \sqrt{\cdot})/(2a)$ | `7.450580596923828e-09` |

**(b)** Stable route for the small root:

$$x_2 = \frac{c}{a\,x_1} = \frac{1}{10^{8}} = 1.0\times10^{-8}.$$

**(c)** The exact small root, from 40-digit decimal arithmetic, is

$$1.000000000000000100000000\times10^{-8}.$$

| route | absolute error | relative error |
|---|---|---|
| naive $(-b-\sqrt{\cdot})/2a$ | $2.55\times10^{-9}$ | $\approx 0.25$ (25%) |
| stable $c/(a x_1)$ | $7.9\times10^{-25}$ | $\approx 8\times10^{-17}$ |

So the naive route delivers **one correct significant digit**, and the stable
route delivers full double precision.

**(d)** Why the large root survives: for $x_1$, the numerator
$-b + \sqrt{b^{2}-4ac} \approx 2\times10^{8}$ involves **addition** of two nearly
equal quantities, which does not cancel — it merely doubles. For $x_2$, the
numerator $-b - \sqrt{b^{2}-4ac} \approx 10^{8} - 9.9999999999999998\times10^{7}$
subtracts two numbers that agree to sixteen digits to produce a result five
digits smaller, so the relative error grows by about $10^{9}$: from
$10^{-16}$ to $10^{-7}$. Using the product of the roots ($x_1x_2 = c/a$) removes
every subtraction from the path.

---

## ★★★10 — Emulating binary32

**(a)** Bisection on $k$ in `to_float32(1.0 + 2**-k) != 1.0`:

- $k = 24$: `1.0 + 2**-24` rounds back to `1.0`;
- $k = 23$: `1.0 + 2**-23` rounds to `1.0000001192092896`.

So $\varepsilon_{\text{mach}}(\text{binary32}) = 2^{-23}
= 1.1920928955078125\times10^{-7}$, consistent with
$\varepsilon_{\text{mach}} = 2^{-(p-1)} = 2^{-23}$, i.e. a 24-bit significand
($p = 24$: one implicit bit plus 23 stored bits).

**(b)** `to_float32(0.1)` is $0.10000000149011612$, and exactly

$$0.100000001490116119384765625.$$

Relative representation error:

| format | relative error storing 0.1 |
|---|---|
| binary32 | $1.490\times10^{-8}$ |
| binary64 | $5.551\times10^{-17}$ |

The ratio is about $2.7\times10^{8}$, close to $2^{28}$ — as expected when
$\varepsilon_{\text{mach}}$ grows by $2^{29}$ but the specific value of $0.1$
happens to round a little favourably in both formats.

**(c)** Rounding every intermediate result through `to_float32`, the naive
$(1-\cos x)/x^{2}$ gives:

| $x$ | $1-\cos x$ (binary32) | value |
|---|---|---|
| $10^{-3}$ | $4.7683716\times10^{-7}$ | $0.47683710$ (4.6% low) |
| $10^{-4}$ | $0.0$ | $0.0$ |
| $10^{-5}$ and below | $0.0$ | $0.0$ |

The binary32 calculation collapses at $x = 10^{-4}$, four decades earlier than
binary64, which survives until $x = 10^{-8}$. The reason is exactly the ulp of
$\cos x \approx 1$: it is $2^{-23}$ in binary32 versus $2^{-52}$ in binary64, so
$x^{2}/2$ falls below half an ulp at a $2^{29}$-fold larger $x$.

**(d) Report.**

*Method.* Single precision was emulated with a `struct` round-trip (pack to
`'f'`, unpack), which rounds a binary64 value to the nearest binary32. Machine
epsilon was found by bisection on powers of two; the cancellation test rounded
every intermediate result to binary32 before combining.

*Results.* $\varepsilon_{\text{mach}} = 2^{-23}$; the representation error of
$0.1$ is $1.5\times10^{-8}$ relative; and the naive $(1-\cos x)/x^{2}$ fails
completely at $x \le 10^{-4}$.

*Practical precision.* Binary32 gives about 7 decimal significant digits and
roughly 7 safe orders of magnitude of dynamic range for cancellation-free work.
Any calculation built on differencing values of order one — normalized
correlations, phase residuals, $(1-\cos\theta)$ corrections — loses those digits
quickly and should be done in double precision.

*Limits.* These measurements concern one function, on one argument range, with
one emulation path through `struct`. They do not establish the accuracy of
binary32 for other functions, do not capture extended-exponent behaviour, and
say nothing about how a compiled language with fused multiply-add or different
optimisation levels would round the same expressions. The *order of magnitude* of
$\varepsilon_{\text{mach}}$ is a property of the format; the *specific digit
patterns* are not.

---

## ★★★11 — Central differences and the $u^{2/3}$ floor

**(a)** Taylor expansions about $x$:

$$f(x+h) = f + hf' + \frac{h^{2}}{2}f'' + \frac{h^{3}}{6}f''' + O(h^{4}),$$
$$f(x-h) = f - hf' + \frac{h^{2}}{2}f'' - \frac{h^{3}}{6}f''' + O(h^{4}).$$

Subtracting removes the $f''$ term and leaves

$$f(x+h) - f(x-h) = 2hf' + \frac{h^{3}}{3}f''' + O(h^{5}),
\qquad\text{so}\qquad
\text{truncation error} = \frac{h^{2}}{6}|f'''| + O(h^{4}).$$

For round-off: each evaluated $f$ carries absolute error at most $u|f|$; the
numerator therefore carries about $2u|f|$, and dividing by $2h$ gives

$$\text{round-off error} \approx \frac{2u|f|}{2h}\Big|_{\text{per unit of the quotient}}
= \frac{u|f|}{h} \quad\text{to leading order.}$$

**(b)** Minimise $E(h) = \dfrac{h^{2}|f'''|}{6} + \dfrac{u|f|}{h}$:

$$\frac{dE}{dh} = \frac{h|f'''|}{3} - \frac{u|f|}{h^{2}} = 0
\;\Longrightarrow\; h^{3} = \frac{3u|f|}{|f'''|}
\;\Longrightarrow\; h^{*} = \left(\frac{3u|f|}{|f'''|}\right)^{1/3}.$$

(With the slightly larger round-off constant $2u|f|/h$ used in part (a), the
prefactor becomes $6$; the scaling $h^{*}\propto u^{1/3}$ is unaffected.) At
$h = h^{*}$ both terms are equal to $\tfrac{1}{2}E_{\min}$ and
$E_{\min} = \mathcal{O}(u^{2/3})$.

For $f = \sin x$ at $x=1$: $|f| = \sin 1 = 0.84147$,
$|f'''| = |\cos 1| = 0.54030$, $u = 1.1102\times10^{-16}$, so

$$h^{*} = \left(\frac{6\times1.1102\times10^{-16}\times0.84147}{0.54030}\right)^{1/3}
= 1.012\times10^{-5}.$$

**(c)** Observed error table (computed, not estimated):

| $h$ | central difference | absolute error |
|---|---|---|
| $10^{-1}$ | $0.5394022521697600$ | $9.001\times10^{-4}$ |
| $10^{-2}$ | $0.5402933008747335$ | $9.005\times10^{-6}$ |
| $10^{-3}$ | $0.5403022158177451$ | $9.005\times10^{-8}$ |
| $10^{-4}$ | $0.5403023049677103$ | $9.004\times10^{-10}$ |
| $10^{-5}$ | $0.5403023058569989$ | $\mathbf{1.114\times10^{-11}}$ (best) |
| $10^{-6}$ | $0.5403023058958567$ | $2.772\times10^{-11}$ |
| $10^{-7}$ | $0.5403023056738121$ | $1.943\times10^{-10}$ |
| $10^{-8}$ | $0.5403023028982545$ | $2.970\times10^{-9}$ |
| $10^{-10}$ | $0.5403022473871033$ | $5.848\times10^{-8}$ |
| $10^{-13}$ | $0.5401235014801387$ | $1.788\times10^{-4}$ |

Observed best: $h = 10^{-5}$ with error $1.114\times10^{-11}$. Note the
truncation-dominated $h^{2}$ decay down to $h=10^{-4}$ (each factor of ten in $h$
buys two decades of accuracy), the flat minimum, and the $1/h$ round-off rise
afterwards.

**(d)** Predicted $h^{*} = 1.0123\times10^{-5}$; observed best $h = 10^{-5}$.
Ratio $1.01$ — agreement to better than 2%, far inside a factor of two. The
predicted minimum error, substituting $h^{*}$ into $E$ with the $6u$ prefactor,
is $E(h^{*}) = 2.77\times10^{-11}$ against an observed
$1.114\times10^{-11}$ — agreement to within a factor of 2.5, which is the
expected quality of an error model that ignores the actual rounding pattern.

**(e)** Comparison of the two schemes:

| scheme | optimal $h$ | minimum error |
|---|---|---|
| forward difference | $\propto u^{1/2}$ | $\mathcal{O}(u^{1/2}) \approx 10^{-8}$ |
| central difference | $\propto u^{1/3}$ | $\mathcal{O}(u^{2/3}) \approx 10^{-11}$ |

The central difference is worth the extra function evaluation: it buys about
three orders of magnitude in accuracy. For an inversion code that differentiates
a misfit, the central difference with $h$ chosen near $u^{1/3}$ times the
characteristic scale of the parameter — or, better, an analytic derivative or
automatic differentiation — is the defensible choice. Note also that the best
$h$ is a *relative* quantity: choose it as $u^{1/3}$ multiplied by the scale on
which the function varies, or the optimum will drift with the units.

---

## Notes on what these exercises do not settle

- Every number above was produced on one machine with one interpreter (CPython
  3.14). The *order of magnitude* of $\varepsilon_{\text{mach}}$ is fixed by
  IEEE 754 and will not vary; the exact digit patterns in the storage of $0.1$
  are also fixed by the standard. But behaviour such as the built-in `sum()`
  being compensated is an implementation choice that changed at CPython 3.12,
  and library `sum` implementations differ between languages and versions.
- The summation-growth coefficient ($\approx1.6\times10^{-18}$) is specific to
  summing $0.1$ in ascending order of index. It is a property of the
  data *and* the order, not a universal constant.
- No claim is made here about GPU or SIMD reduction orders, which can differ
  from sequential summation and therefore change results in the last digits.
