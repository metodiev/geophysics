# Exercises — 03-01-02 Types, Variables, Expressions and Operator Semantics

Attempt these **closed-book** before opening the
[solutions](./02-types-and-variables-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/types_variables_demo.py`](../code/types_variables_demo.py) require you
to run it and report its **actual** output. Quote every number with its unit.

---

## ★ Foundational

**★1.** Predict the value *and* the type of each expression, then check with
Python. Where the result is a float, write it in `repr` form.

```text
7 / 2     7 // 2     -7 // 2     -7 % 2     2 ** -1
-2 ** 2   (-2) ** 2  3 * 0.1     10 ** 30   10.0 ** 30
```

State in one sentence each: (a) why `-7 // 2` is not `-3`; (b) why `10 ** 30`
is exact while `10.0 ** 30` is not.

---

**★2.** Compute the unit in the last place (ulp) for each stored value, in the
units given.

(a) A gravity reading of 980 000.0 mGal — give the ulp in mGal and in µGal.
(b) A station density of 2670.0 kg m⁻³.
(c) A longitude of 47.3769°.

For each, state the largest number of meaningful decimal places the stored value
can support.

---

**★3.** Using `sys.float_info.epsilon` (not a memorised constant):

(a) print it;
(b) compute the relative resolution of a `float64` as
$1 - (1 + \epsilon/2)/(1 + \epsilon)$ and explain why this is approximately
$\epsilon/2$;
(c) state, in words, what "about 15.95 significant decimal digits" means.

---

## ★★ Applied

**★★4.** A colleague writes `if measured_anomaly == 0.268390:` to test whether a
survey's peak matches the model from lesson 01.

(a) Explain why this test is false even when the model and the data agree to six
decimal places.
(b) Rewrite it correctly using `math.isclose`, choosing a tolerance justified by a
gravimeter repeatability of 3 µGal, and state the tolerance in mGal.
(c) Give one case in which even the corrected test is the *wrong* test.

---

**★★5.** Run `python3 types_variables_demo.py` and report:

(a) the naive loop sum and the `math.fsum` value after one million additions of
0.3086;
(b) the exact rational value;
(c) the absolute and relative error of the naive sum;
(d) the ulp of the final sum;
(e) the ratio error/ulp, to the nearest integer.

Then explain in two sentences why the error is many ulps rather than one.

---

**★★6.** Reproduce the exact-arithmetic result:

(a) Compute, with `fractions.Fraction`, the exact sum of ten intervals of
0.1 m.
(b) Compute the same with `float` and print `repr`.
(c) Compute the difference in metres and express it in nanometres.
(d) Compute the distance light travels in that time in vacuum
($c = 299\,792\,458$ m s⁻¹ exactly), in femtometres, and say whether the error is
physically significant for a survey.

---

## ★★★ Research-oriented

**★★★7.** Measure the accumulation error as a function of $n$.

(a) For $n = 10^{5}, 10^{6}, 10^{7}, 10^{8}$, sum 0.3086 mGal $n$ times with a
naive loop and compute the error against the exact value $3086n/10^{4}$ (use
`Fraction` or exact integer arithmetic). Tabulate $n$, the error in µGal, and the
worst-case bound $n\,\epsilon\,\sum|x_i|$ in µGal.
(b) Divide the observed error by the bound. Is the ratio stable?
(c) The error is **not monotonic in $n$**: at $5\times10^{7}$ it is about
−16.4 µGal, at $7\times10^{7}$ about −3.7 µGal. Explain, in terms of the rounding
model, why monotonicity is not expected.
(d) Decide whether naive summation is safe for a 10⁸-term reduction with a 5 µGal
budget, and state the procedure you would adopt instead.

---

**★★★8.** A microgravity monitoring survey has a target signal of 5 µGal and a
tie-in loop of 20 000 readings per day, each with a nominal free-air and Bouguer
term. Determine, with evidence, whether naive summation of the day's corrections
can exhaust 5 µGal of the budget, and write the three-sentence recommendation you
would give the survey's data manager. Your answer must state the assumption you
made about how the error scales, and it must distinguish the *measured* error from
the *worst-case bound*.

---

**★★★9.** The demo prints, for a longitude near 180°,

```text
  but near 180 deg it is 2.842e-14 deg = 3.164e-09 m.
```

(a) Verify both numbers from `math.ulp(180.0)` and a metres-per-degree conversion
of 111 320 m/deg.
(b) A survey stores positions as longitude in degrees and needs a 1 mm relative
position accuracy. At what longitude does the stored precision become the limiting
factor?
(c) The same survey could store longitude in radians or in arcseconds. Compute the
ulp in metres for each at 180°, and state which you would recommend and why.
