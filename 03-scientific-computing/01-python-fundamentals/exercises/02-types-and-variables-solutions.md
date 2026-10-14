# Solutions — 03-01-02 Types, Variables, Expressions and Operator Semantics

> **Read this after attempting the exercises, not before.** Every value attributed
> to the demo is its actual printed output; every other number was computed with
> the interpreter and is reproducible from the code shown.

---

## ★1 — Types and values

| Expression | Value | Type | Note |
|---|---|---|---|
| `7 / 2` | `3.5` | `float` | `/` always returns a float |
| `7 // 2` | `3` | `int` | floors |
| `-7 // 2` | `-4` | `int` | floors towards −∞ |
| `-7 % 2` | `1` | `int` | sign follows the divisor |
| `2 ** -1` | `0.5` | `float` | a negative power is a reciprocal |
| `-2 ** 2` | `-4` | `int` | `**` binds tighter than unary minus |
| `(-2) ** 2` | `4` | `int` | parentheses change the meaning |
| `3 * 0.1` | `0.30000000000000004` | `float` | binary representation of 0.1 |
| `10 ** 30` | `1000000000000000000000000000000` | `int` | arbitrary precision |
| `10.0 ** 30` | `1e+30` | `float` | rounded to 53 bits |

**(a)** `-7 // 2` is −4 because Python's `//` is a **floor**, not a truncation
towards zero: the largest integer not exceeding $-3.5$ is $-4$. In C, Java and
Fortran the same expression truncates to $-3$. The choice matters whenever you bin
a signed quantity — depth below sea level, a residual anomaly, a UTC offset — and
it is the reason Python's `%` is a true modulo (it always returns a result with the
sign of the divisor) rather than a remainder.

**(b)** `10 ** 30` is exact because Python integers have arbitrary precision:
the value is stored as a big integer and is exact. `10.0 ** 30` is a `float`,
stored as a 53-bit significand times a power of two. $10^{30}$ is not a dyadic
rational, so it is rounded to the nearest representable double; `repr` shows
`1e+30`, which is the shortest decimal string that round-trips, not the exact
value. **The type decided the exactness, not the operator.**

---

## ★2 — Unit in the last place

**(a)** `math.ulp(980000.0)` = `1.1641532182693481e-10`, so the ulp is
$1.164\times10^{-10}$ mGal $= 1.164\times10^{-4}$ µGal.

That supports about 11 meaningful decimal places *in absolute terms* around
$9.8\times10^{5}$: the value has 16 significant digits and 6 of them are spent on
the integer part, leaving 10–11 fractional digits. Since a survey resolves a few
microgal, i.e. $10^{-3}$ mGal, stored precision is 7 orders of magnitude finer than
the measurement — double precision is not the limitation.

**(b)** `math.ulp(2670.0)` = `4.547473508864641e-13` kg m⁻³, about
$4.5\times10^{-13}$, i.e. 13 meaningful decimal places. A rock density is never
known to better than the third decimal, so 10 of those digits are decoration.

**(c)** `math.ulp(47.3769)` = `7.105427357601002e-15` degrees. At
111 320 m per degree that is $7.9\times10^{-10}$ m — under a nanometre. The
*stored* precision is far finer than any geodetic measurement; the loss of
precision in practice comes from differences of positions, not from the
representation of one.

---

## ★3 — Epsilon and significant digits

**(a)** `sys.float_info.epsilon = 2.220446049250313e-16`.

**(b)** With $\epsilon = 2^{-52}$:

$$1 - \frac{1 + \epsilon/2}{1 + \epsilon}
= \frac{(1+\epsilon) - (1+\epsilon/2)}{1+\epsilon}
= \frac{\epsilon/2}{1+\epsilon}
\approx \epsilon/2 \;(1 - \epsilon + \dots).$$

So the number is approximately $\epsilon/2 = 1.11\times10^{-16}$, which is the
**gap between 1 and the next representable double**, i.e. one ulp at 1.0. The
weaker assertion "epsilon is the gap" is off by a factor of two; the demo prints
epsilon exactly so that the distinction is checkable.

**(c)** The number of significant decimal digits is the number of binary
significand bits times $\log_{10}2$:

$$53 \times 0.30103 = 15.95 \quad(\text{or } 52 \times 0.30103 = 15.65
\text{ if you count only the stored fractional bits}).$$

In words: **a double distinguishes about 15 to 16 significant decimal digits, so a
quantity quoted to more than 16 significant digits claims precision the
representation cannot hold.** The practical rule: a computed value of magnitude
$10^{m}$ carries $15.95 - m$ meaningful fractional decimal digits.

---

## ★4 — Comparing a computed float

**(a)** The measured peak is a computed double. Stored as IEEE-754 it is
`0.26838952765253565...` for the model, while the literal `0.268390` is a
*different* double — the nearest one to the six-digit decimal. Equality of doubles
requires bit-for-bit identity, so the test is `False` even though the two values
agree to six decimal places. Nothing about the arithmetic guarantees that a
computation lands on the same double as a truncated decimal literal.

**(b)**

```python
import math
if math.isclose(measured_anomaly, model_anomaly_mgal, abs_tol=0.003):
    accept_the_measurement()
```

With a repeatability of 3 µGal $= 3\times10^{-3}$ mGal, the tolerance is
`abs_tol=0.003` mGal. Use an absolute tolerance here rather than the default
relative one: the default `rel_tol=1e-9` on a value of 0.268 mGal corresponds to
$2.7\times10^{-10}$ mGal, far tighter than any instrument, and a relative
tolerance that *scales* with the anomaly is not what an instrument repeatability
does.

**(c)** Even the corrected test is the wrong test when the quantity in question is
a **shape** or a **range** rather than a value. A survey peak that matches to
3 µGal but at the wrong station offset, or a b-value whose uncertainty is ±0.05
against a 0.01 difference in the estimate, is a comparison where the tolerance must
come from the *science*, not from the arithmetic. In particular, comparing two
depth estimates with `isclose` is meaningless: the right question is whether the
confidence intervals overlap.

---

## ★5 — The accumulation measurement

```text
  adding 0.3086 mGal exactly 1,000,000 times
  naive loop sum        = 308599.9999943999
  math.fsum             = 308600.0
  exact rational value  = 308600
  naive  - exact        = -5.6001e-06 mGal   (-1.81e-11 relative)
  fsum   - exact        = 0.0000e+00 mGal
  ulp of the final sum  = 5.8208e-11 mGal
```

**(a)** Naive: `308599.9999943999`. `math.fsum`: `308600.0`.

**(b)** `Fraction(3086, 10000) * 10**6` = `308600` exactly.

**(c)** Absolute error $-5.6001\times10^{-6}$ mGal; relative error
$-1.81\times10^{-11}$.

**(d)** `math.ulp(308600.0)` $= 5.8208\times10^{-11}$ mGal.

**(e)** $5.6001\times10^{-6} / 5.8208\times10^{-11} = 9.6\times10^{4}$, that is
about ninety-six thousand ulps of the final sum. The demo itself prints "about 96
thousand ulps" for exactly this reason: a ratio computed against the *final* sum's
ulp is large, because the additions happen at magnitudes below the final one.

Two-sentence explanation: each addition rounds the running total to the precision
of its current magnitude, so every step injects an error of up to half an ulp, and
because the running total grows, later steps inject *larger* absolute errors than
earlier ones. The errors therefore accumulate roughly as $n\epsilon$ times the
final magnitude rather than as $\sqrt{n}$ times one ulp; `math.fsum` avoids this
entirely by tracking the lost low-order bits in a separate compensated
accumulator and returning the correctly rounded result.

---

## ★6 — Exact decimal versus binary

**(a)** `Fraction(1, 10) * 10` = `Fraction(1, 1)`, exactly one metre.

**(b)** `repr(0.1 * 10)` in a loop of ten additions gives
`0.9999999999999999`.

**(c)** The difference is $1.11\times10^{-16}$ m $= 1.11\times10^{-7}$ nm, or
about 0.1 femtometre.

**(d)** In vacuum, light travels

$$\Delta x = c\,\Delta t = 2.99792458\times10^{8} \times 1.11\times10^{-16}
= 3.33\times10^{-8}\ \text{m} = 33\ \text{nm} = 3.33\times10^{7}\ \text{fm}.$$

**The error is 33 nanometres — seven orders of magnitude below the millimetre a
survey resolves.** The exactness of `Fraction` is a statement about the arithmetic,
not about the measurement: use it to check the arithmetic, then go back to `float`.

---

## ★7 — Accumulation error versus $n$

**(a)** Measured on one machine (CPython 3.14), summing the step 0.3086:

| $n$ | Naive sum | Error (µGal) | Bound $n\epsilon\sum|x_i|$ (µGal) | Ratio |
|---|---|---|---|---|---|
| $10^{5}$ | 30860.00000002487 | $+2.49\times10^{-5}$ | $6.85\times10^{-4}$ | 0.036 |
| $10^{6}$ | 308599.9999943999 | $-5.60\times10^{-3}$ | $6.85\times10^{-2}$ | 0.082 |
| $10^{7}$ | 3086000.000667438 | $+6.67\times10^{-1}$ | 6.85 | 0.097 |
| $10^{8}$ | 30860000.02737371 | $+2.74\times10^{1}$ | 685 | 0.040 |

The bound is $n\,\epsilon\,S$ with $S = 0.3086n$ mGal and
$\epsilon = 2.2204\times10^{-16}$, converted to µGal by $\times 1000$.

**(b)** The ratio is **not stable**: it wanders over 0.036 to 0.097, a factor of
2.7, with no trend. That is expected: the bound is a worst case, and the actual
error is a *random walk* of roundings whose realized value is a fraction of the
bound that depends on the particular sequence of magnitudes and on the binary
expansion of the step. Reporting the ratio as "about 0.05" is defensible; reporting
it as a constant is not.

**(c)** Monotonicity is not expected because each addition rounds with an error of
either sign, of magnitude up to half an ulp of the *current* running total. Those
errors partly cancel and partly accumulate; changing $n$ changes not only how many
terms are added but also every intermediate magnitude at which rounding occurs.
A deterministic but chaotic dependence on $n$ follows, and the measured
non-monotonicity (−16.4 µGal at $5\times10^{7}$, −3.7 µGal at $7\times10^{7}$) is
exactly that.

**(d)** Not safe in general. At $n = 10^{8}$ the measured error is 27 µGal, more
than five times a 5 µGal budget, and at $5\times10^{7}$ it is 16 µGal — also over
budget. The worst-case bound at $10^{8}$ is 685 µGal, two orders of magnitude over
budget. Procedure: use `math.fsum` (or NumPy's pairwise summation) for any
reduction above roughly $10^{6}$–$10^{7}$ terms whose budget is at the microgal
level; if bit-for-bit reproducibility across runs and machines is required, fix
the summation order explicitly.

---

## ★8 — A microgravity tie-in loop

**Evidence.** Twenty thousand readings per day is far below the $10^{6}$ at which
the demo measures a $-5.6\times10^{-3}$ µGal error, and four orders of magnitude
below the $10^{8}$ at which the measured error is 27 µGal. Scaling the $10^{6}$
measurement linearly in $n$ gives an error of about
$5.6\times10^{-3} \times 0.02 \approx 1.1\times10^{-4}$ µGal at $n = 2\times10^{4}$;
scaling it as $n^{2}$ (the pessimistic end of the measured behaviour) gives
$5.6\times10^{-3}\times0.0004 = 2.2\times10^{-6}$ µGal. Both are nine orders of
magnitude below 5 µGal.

**Assumption stated:** the error scales between linearly and quadratically in $n$,
as the measured data at $n = 10^{5}\ldots10^{8}$ show; the estimate uses the
pessimistic end.

**Measured versus bound, distinguished:** the *measured* error at the relevant $n$
is negligible; the *worst-case bound* $n\epsilon\sum|x_i|$ at $n = 2\times10^{4}$ is
about $1.4\times10^{-4}$ µGal, also negligible. Both agree that this loop is not a
threat.

**Three-sentence recommendation.**

> Naive summation in a 20 000-reading daily tie-in loop contributes on the order of
> $10^{-4}$ µGal, which is nine orders of magnitude below the 5 µGal target, so no
> change is required for correctness at this scale. Escalate to `math.fsum` if the
> loop grows past about $10^{6}$ terms, or if the same accumulator is reused across
> a season without being re-zeroed, because the error grows faster than linearly in
> the term count. Whichever is chosen, record the summation method with the
> result, since a change of method changes the last two digits of the total.

---

## ★9 — Positional precision

**(a)** `math.ulp(180.0)` $= 2.842170943040401\times10^{-14}$ degrees, which the
demo prints as `2.842e-14`. In metres:

$$2.84217\times10^{-14} \times 111\,320\ \text{m/deg}
= 3.1639\times10^{-9}\ \text{m} = 3.164\ \text{nm},$$

matching the printed `3.164e-09 m`. The conversion $111\,320$ m/deg is a nominal
figure for the metric size of a *longitude* step at the equator; at higher latitudes
it shrinks as $\cos\phi$, which is a separate effect from the representation's
precision.

**(b)** The stored ulp exceeds 1 mm when

$$111\,320 \times \mathrm{ulp}(\lambda) > 10^{-3}\ \text{m}
\;\Longrightarrow\; \mathrm{ulp}(\lambda) > 8.98\times10^{-9}\ \text{deg}.$$

Since $\mathrm{ulp}(\lambda) \approx \lambda \times 2.22\times10^{-16}$,

$$\lambda > \frac{8.98\times10^{-9}}{2.22\times10^{-16}} = 4.0\times10^{7}\ \text{degrees}.$$

Forty million degrees — so **the representation is never the limiting factor** for
a longitude in degrees; only when *differences* of large longitudes are formed does
the loss of significance appear. The correct statement of the risk is about
differences, exactly as the lesson says.

**(c)** Storing the same physical angle in different units changes the ulp in
degrees but not the metric precision, because the ulp scales with the *magnitude*
of the stored number:

| Unit | Value at 180° | ulp in that unit | ulp in metres |
|---|---|---|---|
| degrees | 180.0 | $2.84\times10^{-14}$ deg | $3.16\times10^{-9}$ m |
| radians | $3.14159\ldots$ | $4.44\times10^{-16}$ rad | $2.83\times10^{-9}$ m |
| arcseconds | $648\,000.0$ | $1.16\times10^{-10}$ arcsec | $3.60\times10^{-9}$ m |

The ulp *in the unit* differs by nearly three orders of magnitude across the three
rows, but the ulp *in metres* is the same to within 25 per cent. That is the lesson
in one table: **the 53-bit relative precision is the invariant, and the ulp in any
chosen unit is that relative precision times the value's magnitude.** Quoting a
unit-space ulp as if it were a precision is a category error.
Recommendation: store angles in radians or degrees and **form differences before
converting**, because the metric precision of a coordinate difference depends on
the difference's own magnitude, not on the coordinate's. Converting to arcseconds
to "gain precision" gains nothing.
