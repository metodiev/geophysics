# Exercises — 03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons

Attempt these **closed-book** before opening the
[solutions](./01-pytest-basics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/pytest_basics_demo.py`](../code/pytest_basics_demo.py); run it and
report its actual output rather than a remembered one:

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/pytest_basics_demo.py
```

The lesson is [`../01-pytest-basics.md`](../01-pytest-basics.md). Assume
`sys.float_info.epsilon` $= 2.220\times10^{-16}$ throughout.

---

## ★ Foundational

**★1.** State, without running anything, the acceptance band
$\tau$ of each assertion and say whether it passes.

(a) `1.0 + 1e-8 == pytest.approx(1.0)`
(b) `1e6 + 1.0 == pytest.approx(1e6)`
(c) `1e6 + 2.0 == pytest.approx(1e6)`
(d) `np.testing.assert_allclose(1e6 + 0.1, 1e6)` — pass or fail?
(e) `np.testing.assert_allclose(1e-13, 0.0)` — pass or fail?
(f) `pytest.approx(0.3, rel=1e-17) == 0.1 + 0.2` — pass or fail, and why is the
answer not the one the relative band suggests?

**★2.** Compute and compare.

(a) What is `math.ulp(1e8)`?
(b) Evaluate `(0.1 + 0.2) * 10 == 3.0` and report the exact stored value.
(c) Evaluate `0.1 + 0.2 + 0.3 == 0.6` and report the exact stored value.
(d) Evaluate `sum([0.1] * 10) == 1.0`.
(e) Of (b), (c) and (d), which are true, and what does the pattern tell you about
the danger of relying on equality or on chance for many-term sums?

**★3.** Write a test for `geophys_tools.normal_moveout(t0, v, x)` that asserts
the zero-offset case is exactly `t0`, and a second test that asserts the moveout
is monotone increasing in offset over the offsets `0, 500, 1000, 2000` m with
`t0 = 0.8` s, `v = 2500` m/s. State which of the two can be written as an exact
equality and why.

---

## ★★ Applied

**★★4. [demo]** The demo measures the one-pass variance of $10^5$ samples offset
by $1.0\times10^8$:

```
  E[x^2] - E[x]^2     = 2.0
  two-pass var        = 1.000257024601711
  relative difference = 9.995e-01
  amplification E[x]^2/var = 9.997e+15
```

(a) Reproduce this with the generator you write, using offset $10^9$ instead of
$10^8$. Report the naive value, the two-pass value and the relative difference.
(b) Compute the amplification $\bar{x}^2/\mathrm{var}$ for the new offset and
predict the relative error as amplification $\times\,u$. Compare with the
measurement.
(c) The naive value for the larger offset is negative. Is a negative variance
"just a precision issue", or is it diagnostic of something specific about the
formula? Answer in two sentences.

**★★5. [demo]** The demo tabulates the forward-difference error for
$\mathrm{d}(\sin)/\mathrm{d}x$ at $x = 1$:

```
  h=1e-04 4.2074e-05 | h=1e-05 4.2074e-06 | h=1e-06 4.2075e-07
  h=1e-07 4.1828e-08 | h=1e-08 1.4072e-08
```

(a) From the error at $h = 10^{-5}$, predict the error at $h = 10^{-6}$ using
the truncation model $\sim h/2$, then compare with the measured value.
(b) Explain, in terms of the round-off model $\sim u/h$, why the error stops
improving and then improves again below $h = 10^{-7}$.
(c) State the smallest tolerance a test of this derivative may use at
$h = 10^{-8}$, and say why any tolerance below about $10^{-9}$ is a test of the
platform rather than of the code.

**★★6.** Write a round-trip test for
`geophys_tools.bouguer_slab_thickness_m(dg_mgal, drho_kgm3)`: generate an effect
from a known thickness, invert it, and assert the thickness returns. State the
tolerance you chose and why it can be much tighter than any tolerance you would
use against a *measured* gravity value. Then state one class of defect this test
cannot catch.

**★★7.** A colleague proposes the following as the tolerance policy for a suite:
"every numerical assertion uses `abs=1e-6`, because 1e-6 is small." Identify
three distinct ways this policy fails, using quantities from the lesson.

---

## ★★★ Research-oriented

**★★★8.** You are writing tests for a new function that computes the vertical
gravity anomaly of a rectangular prism by summing eight corner terms. Design the
tolerance policy.

(a) Name the two candidate reference sources and say which one you would use for
the first test.
(b) Describe an experiment that measures the amplification $\kappa$ of the
formula empirically.
(c) Write the tolerance as an expression in $\kappa$, $u$ and the length of the
sum, and state the constant you would choose.
(d) State one regime in which no tolerance you can defend will work, and what you
would do instead of loosening the tolerance.

**★★★9. [demo]** The lesson's suite reports 22 passed and 1 xfailed. The `xfail`
is

```python
def test_this_is_expected_to_fail():
    d = 300.0
    assert d ** -2 == (1.0 / d) ** 2
```

(a) Explain what information the `xfail` carries that a commented-out test would
not.
(b) Construct a second `xfail` around `np.testing.assert_allclose(x, 0.0)` for a
cancellation residual, and say why `xfail` is legitimate there but would be
wrong for an assertion about a physical quantity.
(c) The lesson says a passing suite bounds nothing about untested behaviour.
Using the free-air gradient measurement in `code/geophys_tools.py`
(`spherical_free_air_gradient_mgal_per_m() = 0.30785` against the conventional
`0.3086`), explain why the *claim* was wrong and the *code* was right, and why
loosening the tolerance to `rel=1e-3` would have been the wrong fix.
