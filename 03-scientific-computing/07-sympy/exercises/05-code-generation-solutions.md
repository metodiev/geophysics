# Solutions — 03-07-05 Generating Fast Numerical Code from Symbolic Results

> **Read this after attempting the exercises.** Values marked as measured are the
> demonstration's output, produced with sympy 1.14.0, NumPy 2.5.4, SciPy 1.18.1
> and Apple clang 21.0.0 on Python 3.14.4.

---

## ★1 — `lambdify` targets

```python
f = sp.lambdify(x, sp.sin(k * x), "numpy")     # array-capable
g = sp.lambdify(x, sp.erfc(x), "numpy")        # maps to whatever NumPy provides
h = sp.lambdify(x, sp.gamma(x), "numpy")       # needs scipy.special
```

(a) and (b) are array-capable. (c) is **not** reliably so: NumPy has no `gamma`,
so the generated source refers to `gamma`, which does not exist in the NumPy
namespace. The fix is `lambdify(x, sp.gamma(x), ["scipy", "numpy"])`, which maps
it to `scipy.special.gamma`. **Always read the generated source** — the lesson's
warning about backend function choice is this exact trap.

---

## ★2 — Call counts

Measured, from the demonstration:

```
  grid: 1000000 points ((100, 100, 100) array)
  Python calls to the lambdified function: 1 (whole array at once)
  Python calls a scalar 'math' module lambdify would need: 1000000
```

The `numpy` route makes one Python-level call and does the arithmetic in compiled
code; the `math` route makes one call per point. For 10 000 points that is 1 against
10 000 — a factor of 10 000 in interpreter overhead, with identical arithmetic.

---

## ★3 — `cse` on a quadratic and its derivative

```python
ax2, ax, c = sp.symbols("a x")
exprs = [a*x**2 + b*x + c, 2*a*x + b]
sp.cse(exprs)
```

Temporaries: `x0 = x**2` (shared between the two? no — the derivative has no
`x**2`), and possibly `2*a` reused between the derivative's `2*a*x` and the
expression's coefficient. The honest result: **this particular pair has almost no
common structure to eliminate**, which is the same finding as the demonstration's
26.9 % reduction being modest. Report what you measure rather than what you
expected.

---

## ★4 — Ordering temporaries

Because `cse` returns assignments in an order that is not guaranteed to be
evaluable top to bottom; a temporary may be defined in terms of one that appears
later. C requires a declaration before use, so the generator must topologically
order them. The demonstration's implementation raises
`RuntimeError("circular or unordered cse replacements")` when it cannot make
progress, which turns a silent ordering bug into a failed build:

```python
pending = list(replacements)
while pending:
    progressed = False
    for item in list(pending):
        sym, value = item
        if value.free_symbols <= defined:
            lines.append(f"    const double {sym} = {sp.ccode(value)};")
            defined.add(sym)
            pending.remove(item)
            progressed = True
    if not progressed:
        raise RuntimeError("circular or unordered cse replacements")
```

Note the seeded set: `defined` must start with the free symbols of the bundle
(the C variables that already exist), or the loop makes no progress at all.

---

## ★5 — What `count_ops` counts

It counts the operations in the expression tree as SymPy constructs them:
multiplications, additions, powers, function applications. It does **not** count
the cost of evaluating a function, the number of machine instructions, memory
access, or the effect of the compiler's own optimisations. It is a static,
machine-independent proxy — which is exactly why this lesson quotes it instead of
wall-clock times.

---

## ★6 — A horizontal line mass

The kernel for a line mass of linear density $\lambda$ at depth $z$ is
$\mathrm{d}g_z = 2G\lambda z/((x-\xi)^2 + z^2)$, so the anomaly is that expression
with the body's mass per unit length. Verifying it against a numerical integral
over the body's cross-section gives agreement at the level of the quadrature
tolerance, as in the demonstration's prism check:

```
      x =       0 m: closed form -44.186027660 mGal, dblquad -44.186027660 mGal, relative difference 1.35e-15
      x =    1500 m: closed form -36.549373953 mGal, dblquad -36.549373953 mGal, relative difference 2.97e-16
      x =    5000 m: closed form -2.277684886 mGal, dblquad -2.277684886 mGal, relative difference 3.08e-14
```

Report your own three offsets with their relative differences.

---

## ★7 — `cse` on your own expression

The measured calibration is `167 → 122` operations with 22 temporaries, a 26.9 %
reduction, for the multipole bundle and its three derivatives. If your expression
has fewer repeated subexpressions the reduction will be smaller, and **that is the
answer** — cse is a syntactic transform, not an algebraic one.

---

## ★8 — Generating and comparing C

The measurable checklist:

```
  wrote generated_multipole.c: 105 lines, 5774 characters
  'cc -O2' exit code: 0
  compiled binary size: 33440 bytes
  bit-identical at 9 of 12 (probe, output) pairs; worst relative difference 2.04e-16
```

Expect a compile exit code of 0 and either bit-identical values or a handful of
ulps of difference. A larger difference means the C generator emitted something
different from what you think it did — print the generated source and compare it
with the expression.

---

## ★9 — Cancellation in $\ln(1+x)$

At small $x$, `np.log1p(x)` is the accurate route; `np.log(1+x)` is not, because
$1+x$ rounds. The worst relative error over 100 points will occur at the smallest
$x$ sampled. For $x = 10^{-16}$ the float `1 + x` is exactly 1.0, so `log` returns
0 and the relative error is 1.0 — the same total failure as the lesson's measured
`1 - cos(1e-8)` case.

The symbolic fix is the series, $\ln(1+x) = x - x^2/2 + x^3/3 - \cdots$, truncated
where the measured error is acceptable.

---

## ★10 — Verifying the prism closed form

Use `scipy.integrate.dblquad` with an explicit tolerance and report the *requested*
tolerance beside the difference — the difference is limited by the quadrature, not
by the closed form. Measured calibration: requests of `epsabs=1e-12, epsrel=1e-12`
produced relative differences of `1.35e-15`, `2.97e-16` and `3.08e-14` — the last
being larger than the tolerance because of the integrand's behaviour at the
corner closest to the observation point. **Report which offset gave the worst
agreement and why that offset is the hardest case** (the near-corner geometry
gives a nearly singular integrand).

---

## ★11 — A full pipeline

The measured anchors: the derivation's two antiderivative checks (`0` and `0`),
the quadrature comparison (≤3.08e-14 relative), the cse reduction (26.9 %), the
NumPy agreement (4.795e-16), the float-versus-40-digit distribution (93 of 200
bit-identical, worst 1.86 ulp) and the C comparison (9 of 12 bit-identical, worst
2.04e-16).

For the line-count question, the demonstration's own numbers are the answer to
expect: **105 lines of generated C for a four-output expression**, against a
hand-written NumPy implementation of about 15 lines. Generated code is longer and
that is fine — it is not read by humans.

---

## ★12 — `cse` on five expressions

A defensible conclusion from such a study: the reduction correlates most strongly
with the number of repeated subexpressions of size two or more, weakly with the
raw operation count, and not at all with the presence of special functions. State
the sample size (five) and be explicit that a five-expression study cannot
distinguish these hypotheses; report the numbers as a preliminary observation.
