# Solutions — 03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* were produced by
> running the code in this module, with the modification stated.

---

## ★1 — Acceptance bands

The rules, measured by bisection against the installed pytest 9.1.1 and NumPy
2.5.4: pytest uses $\tau = \max(\tau_{rel}|y^\ast|, \tau_{abs})$ with defaults
$10^{-6}$ and $10^{-12}$; a *specified* `abs` alone gives a pure absolute band;
NumPy uses $\tau = \tau_{atol} + \tau_{rtol}|y^\ast|$ with defaults $0$ and
$10^{-7}$.

**(a)** $\tau = \max(10^{-6}\times1.0,\ 10^{-12}) = 10^{-6}$, and the difference
is $10^{-8}$. **Passes.**

**(b)** $\tau = \max(10^{-6}\times10^6,\ 10^{-12}) = 1.0$, difference $1.0$.
**Passes** — at the boundary, and only just.

**(c)** Difference $2.0 > 1.0$. **Fails.**

**(d)** $\tau = 0 + 10^{-7}\times10^6 = 0.1$, and the stored difference is
$0.09999999997671694$. **Passes** — by $2.3\times10^{-11}$, i.e. by a quarter of
one ulp of the band. This is worth seeing once: an assertion that sits at the
boundary of a relative band is decided by the last bits of the operands.

**(e)** $\tau = 0 + 10^{-7}\times0 = 0$, difference $10^{-13} > 0$. **Fails.**
This is the numpy default with no absolute floor, and it is why a residual
assertion needs `atol`.

**(f)** **Passes.** The relative band is $10^{-17}\times0.3 =
3\times10^{-18}$, which the difference $5.551\times10^{-17}$ exceeds — but
pytest's default `abs=1e-12` still applies, and
$\max(3\times10^{-18}, 10^{-12}) = 10^{-12} > 5.551\times10^{-17}$. To obtain the
pure relative band the assertion must read
`pytest.approx(0.3, rel=1e-17, abs=0)`, which the demo measures as failing. This
is the trap the lesson flags: **passing `rel` does not remove the absolute
floor.**

---

## ★2 — Equality and ulp

**(a)** *Measured*: `math.ulp(1e8) = 1.4901161193847656e-08`.

**(b)** `(0.1 + 0.2) * 10` stores `3.0000000000000004`, so the comparison is
**False**.

**(c)** `0.1 + 0.2 + 0.3` stores `0.6000000000000001`, so the comparison is
**False**.

**(d)** `sum([0.1] * 10) == 1.0` is **True**.

**(e)** Only (d) is true. The reason is measurable rather than lucky: on this
interpreter (CPython 3.14.8) `sum` uses compensated summation for floats, so
`sum([1e16, 1.0, -1e16])` returns `1.0` where a naive `for` loop returns `0.0`
— *measured*. So (d) is not a coincidence in the arithmetic but a property of
the reducer, and that is precisely why it should not be relied on: the same
expression in a hand-written loop, or in an older interpreter, gives a different
answer. The pattern across (b), (c) and (d) is what matters: three arithmetically
identical questions, three different answers, none of them predictable from the
surface form. A suite that depends on such coincidences passes or fails according
to the accumulation order, the platform and the version — exactly the
non-reproducibility a tolerance exists to remove.

---

## ★3 — Two moveout tests

```python
def test_zero_offset_is_exactly_t0():
    assert gt.normal_moveout(1.0, 2000.0, 0.0) == 1.0


def test_moveout_increases_with_offset():
    times = [gt.normal_moveout(0.8, 2500.0, x) for x in (0.0, 500.0, 1000.0, 2000.0)]
    assert all(b > a for a, b in zip(times, times[1:]))
```

The first can be an exact equality, and the reason is structural rather than
lucky: at zero offset the expression reduces to $\sqrt{t_0^2 + 0} = |t_0|$, and
`math.sqrt` of a perfect square is exactly rounded, so the function returns `t0`
to the last bit. The second is an *ordering* assertion, which
`np.all(np.diff(times) > 0)` expresses; it needs no tolerance at all, because
strict monotonicity is a discrete property that floating point preserves for
offsets this well separated. Property assertions like these are the strongest
kind of test and the easiest to get right, because they need no reference value
and therefore cannot be defeated by a wrong reference.

---

## ★4 — Variance conditioning at two offsets

**(a)** *Measured* with the same generator and 100 000 samples, offset $10^9$:

```
offset 1e+08: naive 2.0            two-pass 1.000257024601711  rel 9.995e-01  cond 9.997e+15
offset 1e+09: naive -128.0         two-pass 1.004543438347577  rel 1.284e+02  cond 9.955e+17
```

The relative difference at $10^9$ is $1.284\times10^{2}$, i.e. **12 840%**.

**(b)** The amplification is $\bar{x}^2/\mathrm{var} = 9.955\times10^{17}$ (it
scales as offset$^2$), and the predicted relative error is
$9.955\times10^{17} \times 2.220\times10^{-16} = 221$. The measured relative
difference is 128. Both exceed 1 by two orders of magnitude, which is the model
saying "there are no correct digits"; the factor-of-two disagreement between 221
and 128 is the model's constant being unknown, not a failure of the model.

**(c)** A negative variance is not merely imprecise; it is diagnostic. The
formula's operands are two nearly equal large numbers
($\bar{x^2} \approx 10^{18}$, $\bar{x}^2 \approx 10^{18}$, whose difference is
$\approx1$), and their individual rounding errors are of order
$10^{18}\times10^{-16} = 100$. Subtracting them leaves a remainder whose sign is
decided by round-off. **Any** result — positive, negative, or zero — is equally
meaningless. The remedy is the two-pass (or Welford) form, not a tolerance.

---

## ★5 — Forward-difference tolerances

**(a)** The truncation model gives error $\approx h/2$, so at $h = 10^{-5}$,
$5\times10^{-6}$; at $h = 10^{-6}$, $5\times10^{-7}$. *Measured* at
$h = 10^{-5}$: $4.2074\times10^{-6}$; at $h = 10^{-6}$: $4.2075\times10^{-7}$.
The measured truncation constant is $0.4207$, not $0.5$, because the next term
in the Taylor series contributes — the model is right to first order and 16% off
in the constant.

**(b)** Below $h \approx 10^{-7}$ the rounding of $\sin(1+h) - \sin(1)$ dominates:
the two values differ by about $h \approx 10^{-8}$, which is of order
$u \times |\sin(1)|/h$ relative to their own magnitude after division. The error
therefore *improves* from $4.1828\times10^{-8}$ at $h = 10^{-7}$ to
$1.4072\times10^{-8}$ at $h = 10^{-8}$ because the truncation term continues to
shrink as $h/2$ while the round-off term, at $u/h \approx 2.2\times10^{-8}$, is
still comparable; the two are crossing over in this range rather than one
dominating cleanly.

**(c)** The measured error at $h = 10^{-8}$ is $1.4072\times10^{-8}$, so any
absolute tolerance must exceed that; a defensible choice is $2\times10^{-8}$.
Below about $10^{-9}$ the tolerance is smaller than the round-off floor of the
*chosen* $h$, so the assertion would be testing whether this platform's `sin`,
division and subtraction happen to agree with the reference to that many digits
— which is a property of the C library, not of the code under test.

---

## ★6 — Bouguer round trip

```python
def test_bouguer_slab_round_trip():
    for drho in (200.0, 400.0, 600.0):
        thickness = 1500.0
        dg = 2.0 * math.pi * gt.G_SI * drho * thickness * gt.GAL_PER_MS2
        assert gt.bouguer_slab_thickness_m(dg, drho) == pytest.approx(thickness, rel=1e-12)
```

The tolerance is `rel=1e-12` — tighter than any assertion against a *measured*
gravity value could be, because nothing physical is involved. Both sides of the
comparison are analytic evaluations of the same expression with the same
constants, so the only discrepancy is the round-off of one division and one
multiplication, of order $u = 2.2\times10^{-16}$; the tolerance of $10^{-12}$
leaves four orders of margin. A measured gravity value would carry instrument
noise, a latitude-dependent normal-gravity term and terrain effects, and the
tolerance would have to cover all of them.

What the round trip cannot catch: **a wrong constant that appears on both
sides.** The test uses `gt.G_SI` and `gt.GAL_PER_MS2` from the module under test,
so if `G_SI` were wrong by 1%, the round trip would still return 1500.0 exactly.
That is the same defect class as the characterisation test in the coverage
demonstration — a test that compares the code with itself. Catching it requires
an independent reference: the accepted value of $G$, or a published slab excess
for a known density contrast.

---

## ★7 — Why "abs=1e-6 everywhere" fails

**(a) It is meaningless at large magnitudes.** For a gravity anomaly of order
$10^6$ mGal — the raw observed value, before reduction — an absolute $10^{-6}$
mGal band is a relative tolerance of $10^{-12}$, below the round-off floor of a
double for that magnitude ($\mathrm{ulp}(10^6) \approx 1.2\times10^{-10}$). The
assertion fails on correct code.

**(b) It is vacuous at small magnitudes.** For a cancellation residual of order
$10^{-17}$, an absolute band of $10^{-6}$ accepts *anything* the arithmetic can
produce, including a sign error that produces $-10^{-7}$. The assertion passes on
wrong code.

**(c) It has no relation to conditioning.** The lesson's two examples have
required tolerances of $2\times10^{-14}$ relative (the well-conditioned sum) and
"impossible" (the one-pass variance). One number cannot serve both; the policy
encodes no analysis at all, and it fails in both directions simultaneously on
different assertions in the same suite. The remedy is the recipe in the lesson's
Section 3.4: measure $\kappa$, add the discretisation term, set
$\tau_{rel} \approx c\,\kappa\,u$, and write the derivation in a comment.

---

## ★8 — Tolerance policy for a prism

**(a)** The two candidate references are (i) the exact gravity anomaly of a
rectangular prism, which has a closed form in terms of arctangents and logarithms
(the Nagy formula), and (ii) the shell-theorem limit, which is exact when the
prism is replaced by a sphere of equal mass at large distance. For a first test
use **(ii) in the far field** *and* **(i) for the algebra**, because (ii) alone
verifies only the total mass and the $1/d^2$ behaviour, while (i) exercises the
corner terms that the summation implements.

**(b)** Amplification is measured by evaluating the same geometry two ways that
differ only in the order of the eight-term summation — for example the natural
corner order against a reversed order — and comparing the results at high
precision. The measured relative difference is the amplification $\kappa$ for
this problem. A second estimate comes from shifting the observation point by one
ulp and observing the relative change in the output; the ratio is
$\kappa$ to first order.

**(c)** With $n = 8$ terms and amplification $\kappa$, the tolerance is

$$\tau_{rel} = c\,\kappa\,n\,u, \qquad c \sim 100 .$$

The factor $n u$ bounds the summation error and $c$ provides margin for the
trigonometric and logarithmic terms, whose cancellation is usually worse than
the sum's. In the far field the amplification is $\mathcal{O}(1)$ and
$\tau_{rel} \approx 10^{-12}$ is defensible; near a corner of the prism at
$d \sim$ the prism dimension, measured amplification rises sharply and the same
constant gives a much looser — and much more honest — band.

**(d)** **Near-field geometries where the observation point approaches a corner
or an edge of the prism.** The arctangent and logarithm terms then have
near-cancellations whose amplification grows without bound as the distance to the
corner goes to zero, and no fixed relative tolerance in double precision survives.
The correct response is not to loosen the tolerance but to change the
implementation: use a formulation written for the near field, or compute that
geometry in extended precision, or exclude the regime from the function's
documented domain and raise on it. A guard test asserting the raised exception is
worth more than any number the function could return.

---

## ★9 — The `xfail`, and a wrong claim versus wrong code

**(a)** The `xfail` documents an *executable expectation of failure*. A
commented-out test records nothing about why it is commented out, cannot be
counted, and therefore cannot fail if the platform or the library changes so that
it would now pass. `xfail` produces a reported line in the summary
(`1 xfailed`), and set to `strict` it turns an unexpected pass into a failure —
which is the behaviour you want when the "known failure" was a bug that has
since been fixed.

**(b)**

```python
@pytest.mark.xfail(reason="numpy has no absolute floor at a zero reference")
def test_default_allclose_cannot_assert_a_residual():
    np.testing.assert_allclose(0.1 + 0.2 - 0.3, 0.0)
```

That is legitimate because it asserts a property *of the library's default
configuration*, and the correct fix is to change the call, not the code —
`atol=1e-16` passes. It would be wrong for a physical quantity, because there the
correct fix is to correct the science, and an `xfail` would conceal an error the
suite is supposed to catch.

**(c)** `spherical_free_air_gradient_mgal_per_m()` computes $2g/R$ with
$g = 9.80665$ m s$^{-2}$ and $R = 6.371\times10^{6}$ m, giving **0.30785** mGal/m.
The conventional free-air gradient is **0.3086** mGal/m, which differs by 0.24%,
or about 0.8 mGal over 1 km of relief. The code implements the spherical formula
correctly; the *claim* — "this function returns the conventional free-air
correction" — was wrong, because the conventional value carries flattening and
centrifugal terms that the spherical derivation omits. Loosening to `rel=1e-3`
would have made the test pass while leaving the documentation wrong, and the
0.24% error would have propagated silently into every reduction. The correct fix
was to rename the function, state the formula in its docstring, and assert
against 0.30785 to five digits — which is what the module does, and what the
suite reports as passing.
