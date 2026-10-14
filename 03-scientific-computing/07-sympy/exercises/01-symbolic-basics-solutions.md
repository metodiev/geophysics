# Solutions — 03-07-01 Symbolic Variables, Expressions and Assumptions

> **Read this after attempting the exercises.** Values marked as measured are the
> demonstration's output, produced with sympy 1.14.0 and mpmath (default
> `mpmath.mp.dps = 15`) on Python 3.14.4.

---

## ★1 — Three declarations, four expressions

| Expression | unconstrained | `real=True` | `positive=True` |
|---|---|---|---|
| $\sqrt[3]{x^3}$ | $x$ (odd root, no branch issue) | $x$ | $x$ |
| $\lvert x\rvert$ | $\lvert x\rvert$ | $\lvert x\rvert$ | $x$ |
| $\sqrt{x}\sqrt{x}$ | $x$ (branch choice made) | $x$ | $x$ |
| $e^{\ln x}$ | $x$ | $x$ | $x$ |

The measured lines from the demonstration, which cover the same behaviour:

```
  sqrt(x**2), x unconstrained  -> sqrt(x**2)
  sqrt(x**2), x real           -> Abs(x)
  sqrt(x**2), x positive       -> x
  Abs(x), x positive           -> x
  log(exp(x)), x real          -> x
```

Note that the *even* root is the one that needs an assumption; the odd root is
defined on the reals without one.

---

## ★2 — $\frac17$ and its float

Exact: $\frac17 \times 7 = 1$, and `1/7 * 7 == 1` in SymPy is `True`.

Binary64: `1/7` is `0.14285714285714285`; multiplying by 7 gives
`1.0000000000000002` in general, but Python's rounding can make the last bit come
out exactly 1.0 for this particular pair — which is why the demonstration's
parallel case, `3 * (1/3) == 1`, printed

```
  3 * (1/3) == 1 in binary64             : True
      ^ measured True: rounding hid the error here
```

The exact discrepancy for the $0.1$ case is what the demonstration prints:

```
  Rational(0.1) - Rational(1,10) exactly : 1/180143985094819840
      as a decimal: 5.551e-18, relative 5.551e-17
```

---

## ★3 — Exact rationals and their denominators

| Value | Exact | Binary64-exact? | Denominator |
|---|---|---|---|
| 0.375 | $\frac38$ | yes | 8 = $2^3$ |
| 2.5 | $\frac52$ | yes | 2 |
| 0.1 | $\frac{1}{10}$ | no | 10 = 2·5 |

**A number is exactly representable in binary64 if and only if its reduced
denominator is a power of two.** `Rational(0.1)` returns
$3602879701896397/36028797018963968$, whose denominator is $2^{55}$ — measured as
`denominator = 36028797018963968 = 2**55, the signature of a binary float`.

---

## ★4 — Why precision must be measured

Because it is a property of the session, not of the library: `mpmath.mp.dps` is a
mutable global that any code in the process can change. The demonstration prints
it at the start (15) and then raises it to 50 for the high-precision block, so a
bare claim like "SymPy gives 50 digits" would be meaningless without saying which
call set the precision. The same reasoning applies to `numpy.set_printoptions`,
`pandas` display options, and matplotlib's `rcParams`: **a claim about output
format is a claim about process state.**

---

## ★5 — $0.1 + 0.2 - 0.3$

Measured:

```
  0.1 + 0.2 == 0.3 in binary64           : False
      0.1 + 0.2 - 0.3 = 5.551e-17
  Rational(0.1) - Rational(1,10) exactly : 1/180143985094819840
```

The discrepancy $5.551\times10^{-17}$ is exactly $2^{-54} =
1/180143985094819840$.

---

## ★6 — Mars, symbolically

```python
G, M, R, rho = sp.symbols("G M R rho", positive=True)
g = sp.simplify(G * (sp.Rational(4, 3) * sp.pi * rho * R**3) / R**2)
```

which returns $g = \frac{4}{3}\pi G\rho R$. Evaluating with
$G = 6.67430\times10^{-11}$, $\rho = 3933$, $R = 3.390\times10^6$:

$$g = \frac{4}{3}\pi (6.67430\times10^{-11})(3933)(3.390\times10^6)
= 3.715\ \mathrm{m\,s^{-2}},$$

against the measured $3.71\ \mathrm{m\,s^{-2}}$ — a discrepancy of about 0.1 %.
Reasons: (i) Mars is not a sphere and is not uniform, so the surface gravity varies
by latitude; (ii) the "measured" 3.71 is itself a mean or reference value, and the
comparison is between a model mean and a quoted mean.

---

## ★7 — Equal free-air and slab contributions

The free-air gradient is $-2g_0/R$ and the slab term is $+2\pi G\rho$ per metre.
Equal contributions means

$$\frac{2 g_0}{R}h = 2\pi G\rho h \quad\text{per unit } h,$$

which cancels $h$: **the two are proportional to $h$ and can never be equal for
nonzero $h$.** The correct question is at what depth the two *gradients* have equal
magnitude, which gives

$$\frac{2g_0}{R} = 2\pi G\rho \quad\Longrightarrow\quad \rho = \frac{g_0}{\pi G R}.$$

Evaluating: $\rho = 9.80665/(\pi \times 6.6743\times10^{-11}\times 6.371\times10^6)
= 7338\ \mathrm{kg\,m^{-3}}$ — higher than any crustal rock, so for
$\rho = 2670$ the free-air gradient always exceeds the slab gradient. **The
exercise's value is that the algebra shows the question as posed has no solution.**

---

## ★8 — The Pythagorean identity

```python
expr = sp.sin(x)**2 + sp.cos(x)**2
sp.count_ops(expr)          # 5
sp.trigsimp(expr)           # 1
sp.count_ops(sp.trigsimp(expr))   # 0
```

Measured in the demonstration: `Pythagorean identity         ops   5 ->   0`. The
named function is `trigsimp`; `simplify` reaches the same result by search, and
the measured operation counts were identical, so the reason to name `trigsimp` is
determinism, not speed here.

---

## ★9 — `nsimplify`, right and wrong

Measured:

```
  nsimplify(0.1) = 1/10
  nsimplify(0.1) - Rational(1,10) = 0
  nsimplify(0.1000000000001) = 1/10
```

Right: a constant a human typed as "0.1" is recovered as $\frac{1}{10}$. Wrong:
a value that is genuinely $0.1000000000001$ is *also* snapped to $\frac{1}{10}$,
destroying the difference. The rule: `nsimplify` for hand-written constants, never
for data.

---

## ★10 — Earth's mean density

$$\rho = \frac{3g}{4\pi G R},$$

the LaTeX from the demonstration being `\frac{3 g}{4 G R \pi}`. Measured value
with $g = 9.80665$, $R = 6.371\times10^6$, $G = 6.67430\times10^{-11}$:

```
      rho = 5505.8 kg m^-3
  PREM mean density (textbook reference value, not measured here): 5514.0 kg m^-3
      difference = -8.2 kg m^-3 (0.15 %)
```

Dimensional check:
$[\mathrm{m\,s^{-2}}]/([\mathrm{m^3\,kg^{-1}\,s^{-2}}][\mathrm{m}]) =
\mathrm{kg\,m^{-3}}$. The residual has two contributions — the centripetal
acceleration and the Earth's non-uniformity — and the lesson does not attribute
the 0.15 % between them.

---

## ★11 — A two-layer Earth

With crustal density $\rho_1$ to depth $d$ and mantle $\rho_2$ below radius $R$:

$$\bar\rho = \frac{\rho_1\left(R^3 - (R-d)^3\right) + \rho_2\,(R-d)^3}{R^3}.$$

Solving for $\rho_2$ with $\bar\rho = 5514$, $\rho_1 = 2700$, $d = 35$ km,
$R = 6.371\times10^6$ m gives a value of order $5580\ \mathrm{kg\,m^{-3}}$; the
crust is such a thin shell that it barely moves the mean. **Significant figures:
two.** The inputs are quoted to two or three figures, and the model has two
layers, so quoting $\rho_2$ to four figures would be a claim the model cannot
support.

---

## ★12 — Growth of exact rationals

$S_{10} = 7381/2520$, $S_{100}$ and $S_{1000}$ have numerators and denominators of
hundreds and thousands of digits respectively: the exact harmonic sum grows
super-exponentially in its representation, because the denominator is a highly
composite number.

The practical rule: **use exact rationals for short chains of algebra and for
verification; evaluate to a float before storing in an array.** The demonstration's
`count_ops` measurements (15, 66 and 69 characters of LaTeX for three expressions)
are the same lesson at a smaller scale: representation size is a cost.
