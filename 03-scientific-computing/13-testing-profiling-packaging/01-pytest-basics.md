---
id: 03-13-01
title: "pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons"
level: intermediate
prereqs: ["03-01-04", "03-01-07", "01-01-04"]
estimated_minutes: 90
tags: [testing, pytest, fixtures, parametrisation, floating-point, tolerances]
---

# pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons

A test is a falsifiable claim about a program's behaviour. In most software the
claim is "equal": a parser either returns the expected string or it does not. In
geophysics the claim is almost never equality. It is "equal to within what this
computation can deliver", and knowing *what that is* requires the analysis in
[01-01-04 Floating-Point Representation](../../01-mathematics/01-arithmetic/04-floating-point.md)
and [01-01-05 Error, Conditioning and Stability](../../01-mathematics/01-arithmetic/05-error-and-conditioning.md).

This lesson builds a test suite for a small geophysical module. Along the way it
measures, rather than asserts, the four facts that decide whether a numerical
test is meaningful: what `==` actually compares, what `pytest.approx` and
`numpy.testing.assert_allclose` actually accept, why a tolerance has to be
derived from the arithmetic, and why a test that passes is not yet evidence.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why `assert a == b` on computed floats tests the last bit rather
   than the physics, and quantify the discrepancy in ulp.
2. **Derive** a tolerance from the floating-point model and the amplification
   factor of the formula, instead of choosing one that "looks small".
3. **State** the exact acceptance bands of `pytest.approx` and
   `numpy.testing.assert_allclose`, including the defaults and the traps in each.
4. **Structure** a suite with fixtures at three scopes, parametrisation,
   `pytest.raises`, `tmp_path`, `monkeypatch`, `skipif` and `xfail`.
5. **Decide** what to assert as opposed to what to merely execute, and say why
   executing is nearly free and asserting is the whole point.
6. **Run** a suite, read its report, and describe what CI adds to running it
   yourself.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — a test is a function, and a suite is a module.
- [03-01-07 Errors, Exceptions and Debugging](../01-python-fundamentals/07-errors-and-debugging.md)
  — `AssertionError` is an exception, and `pytest.raises` tests exceptions.
- [01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../../01-mathematics/01-arithmetic/04-floating-point.md)
  — the model that makes a tolerance necessary and computable.

## 1. Why `==` cannot be an assertion about physics

Run this:

```python
>>> 0.1 + 0.2 == 0.3
False
```

The difference is not a bug in Python. `0.1` and `0.3` have no finite binary
expansion, so the stored values are the nearest binary64 numbers to them, and
their sum is one unit in the last place away from the stored `0.3`. In this
repository's environment the measured difference is

$$|(0.1 + 0.2) - 0.3| = 5.551\times10^{-17},$$

which is exactly one `ulp` of $0.3$ — the spacing between adjacent representable
doubles near that magnitude, `math.ulp(0.3) = 5.551e-17`. A test written
`assert 0.1 + 0.2 == 0.3` fails, and it fails for a reason with no physical
content whatsoever.

The same happens to real geophysics. Two algebraically identical routeings of
the inverse-square factor in a gravity calculation, $d^{-2}$ and $(1/d)^2$ with
$d = 300$ m, differ by

$$|d^{-2} - (1/d)^2| = 1.694\times10^{-21} = 1\ \mathrm{ulp},$$

equivalent to about $3\times10^{-13}$ mGal. The number is far below any
instrument, and `assert d**-2 == (1/d)**2` fails anyway. Worse, it fails on some
machines and not others, because IEEE 754 permits a compiler to contract or
reassociate such expressions. **A test whose outcome depends on the vendor of
the compiler is not a test of your science.**

> **The principle.** Equality of floating-point numbers is a statement about
> bit patterns. What you mean when you write a numerical test is a statement
> about a *ball* around the true value, and writing that ball down explicitly is
> the work.

## 2. Precise definitions

### 2.1 The floating-point error model

Let $\mathrm{fl}(x)$ be the double nearest to a real $x$. Then

$$\mathrm{fl}(x) = x(1 + \delta), \qquad |\delta| \le u, \qquad
u = 2^{-53} = 1.110\times10^{-16},$$

where $u$ is the *unit roundoff*. Python reports `sys.float_info.epsilon` as
$2u = 2.220\times10^{-16}$, the gap between $1.0$ and the next float. Everything
that follows is stated relative to $u$.

### 2.2 Absolute, relative and mixed tolerance

A comparison of a computed $y$ against a reference $y^\ast$ is decided by a
band. Three forms are in common use:

- **absolute**: $|y - y^\ast| \le \tau_{abs}$;
- **relative**: $|y - y^\ast| \le \tau_{rel}\,|y^\ast|$;
- **mixed**: $|y - y^\ast| \le \tau_{abs} + \tau_{rel}\,|y^\ast|$.

The mixed form is what you almost always want: relative where the answer is
large, absolute where the answer is near zero and the relative band would
collapse to nothing. The two libraries differ precisely here, and the difference
is a source of silent bugs.

### 2.3 The measured acceptance bands

These bands were obtained by bisection against the installed pytest 9.1.1 and
NumPy 2.5.4, not read from documentation.

| Assertion | Accepts $\lvert a-b\rvert$ up to |
|---|---|
| `pytest.approx(1.0)` | $1.000\times10^{-6}$ |
| `pytest.approx(1.0, rel=0)` | $1.000\times10^{-12}$ |
| `pytest.approx(1.0, abs=0)` | $0$ (exact equality) |
| `pytest.approx(0.0)` | $1.000\times10^{-12}$ |
| `pytest.approx(1e6)` | $1.0$ |
| `pytest.approx(0.3, rel=1e-3)` | $3.000\times10^{-4}$ |
| `np.testing.assert_allclose(1.0, ·)` | $1.000\times10^{-7}$ |
| `np.testing.assert_allclose(1e6, ·)` | $0.1000$ |

The rules underneath:

$$\text{pytest: } \tau = \max(\tau_{rel}|y^\ast|,\ \tau_{abs}), \qquad
\tau_{rel} = 10^{-6},\ \tau_{abs} = 10^{-12}\ \text{by default};$$

$$\text{numpy: } \tau = \tau_{atol} + \tau_{rtol}|y^\ast|, \qquad
\tau_{rtol} = 10^{-7},\ \tau_{atol} = 0\ \text{by default}.$$

Two consequences are easy to miss and were measured:

1. **Passing `rel` to pytest does not remove the $10^{-12}$ floor.** With the
   installed version, `pytest.approx(0.3, rel=1e-17)` *passes* against
   `0.1 + 0.2`, because $\max(3\times10^{-18}, 10^{-12}) = 10^{-12}$. To get a
   pure relative tolerance you must pass `abs=0.0` as well. The demonstration
   does, and only then does `rel=1e-17` fail as the arithmetic says it should.
2. **numpy has no floor at all.** `np.testing.assert_allclose(5.551e-17, 0.0)`
   **fails**: at a reference of zero the relative band is zero, and the absolute
   band was never asked for. An assertion about a cancellation residual is, in
   numpy, a bitwise assertion unless you pass `atol`.

## 3. Choosing the tolerance from the arithmetic

This is the part that separates a test suite from a ritual. Three examples,
each measured.

### 3.1 A well-conditioned sum

Sum $n = 100$ terms of magnitude $1$ (here $1/3$ each). The textbook bound for
recursive summation is a relative error of order $n u$:

$$|\text{relative error}| \lesssim n\,u = 100 \times 2.220\times10^{-16}
= 2.220\times10^{-14}.$$

The measured relative error was $2.132\times10^{-16}$, comfortably inside the
bound, and a tolerance of $10^{-14}$ sits at $0.45\times$ the textbook bound —
tight but defensible.

### 3.2 A formula that no tolerance can rescue

The one-pass variance $(x^2)_{\mathrm{mean}} - (x_{\mathrm{mean}})^2$ of $10^5$
samples offset by $1.0\times10^8$:

| Quantity | Measured |
|---|---|
| one-pass $(x^2)_{\text{mean}} - \bar{x}^2$ | $2.0$ |
| two-pass `x.var()` | $1.000257$ |
| relative difference | $9.995\times10^{-1}$ |
| amplification $\bar{x}^2/\mathrm{var}$ | $9.997\times10^{15}$ |
| predicted relative error, amplification $\times\,u$ | $2.220$ |

The one-pass answer is wrong by 100%. The predicted error exceeds 1, which is
the model telling you the formula has no correct digits left. **There is no
tolerance that makes this test meaningful**, because the failure is in the
formula, not in the comparison. The test you want is one that pins the
conditioning: assert that the two-pass result is within $10^{-12}$ relative of
the one-pass result *only after* rewriting the one-pass form, or assert the
relative error directly against the conditioning bound.

### 3.3 A numerical derivative: two error terms, opposite signs

Approximating $\cos(1)$ by the forward difference of $\sin$ at $x = 1$:

$$D(h) = \frac{\sin(1+h) - \sin(1)}{h}, \qquad
\text{truncation} \sim \frac{h}{2}, \qquad
\text{round-off} \sim \frac{u}{h}.$$

| $h$ | measured error | $\sim h/2$ | $\sim u/h$ |
|---|---|---|---|
| $10^{-4}$ | $4.207\times10^{-5}$ | $5\times10^{-5}$ | $2.2\times10^{-12}$ |
| $10^{-6}$ | $4.207\times10^{-7}$ | $5\times10^{-7}$ | $2.2\times10^{-10}$ |
| $10^{-7}$ | $4.183\times10^{-8}$ | $5\times10^{-8}$ | $2.2\times10^{-9}$ |
| $10^{-8}$ | $1.407\times10^{-8}$ | $5\times10^{-9}$ | $2.2\times10^{-8}$ |

The measured optimum is $h = 10^{-8}$, against the classical prediction
$h^\ast \sim u^{1/2} = 1.49\times10^{-8}$. A test of this derivative must use a
tolerance above the *round-off floor at the $h$ you chose* — about
$2\times10^{-8}$ absolute at $h = 10^{-8}$, not $10^{-15}$. Writing
`assert D == pytest.approx(cos(1), abs=1e-15)` is not a stricter test; it is a
test that is guaranteed to fail on correct code.

### 3.4 The recipe

1. Write down the conditioning: how much does a relative perturbation of the
   inputs amplify into the output? Call it $\kappa$, and estimate it by
   comparing two algebraically different routeings.
2. Add the discretisation error if the method is approximate; it is usually the
   dominant term and it is *deterministic*, so it is the thing your tolerance
   must cover.
3. Set $\tau_{rel} \approx c\,\kappa\,u$ with $c \sim 10$ to $100$ for margin,
   and never below the discretisation floor.
4. State the derivation in a comment. A tolerance with a derivation can be
   reviewed; a tolerance without one is a number somebody will "fix" by
   loosening.

## 4. Fixtures, parametrisation and the rest of the machinery

A test suite needs three things beyond assertions: shared setup, repetition over
cases, and control over the environment.

**Fixtures** are functions that produce a value a test asks for by name. Their
*scope* is the design decision: a session-scoped fixture is built once and
shared, a function-scoped fixture is rebuilt for every test. Reproducible random
data belongs in a session or module fixture, because rebuilding it per test
costs time and gains nothing; a mutable array that a test might modify must be
function-scoped, or the tests become order-dependent.

**Parametrisation** turns one test function into many tests with distinct names.
This matters more in science than elsewhere: a suite that appears to have
40 tests and is really one test applied to 40 inputs gives a report that says
"40 passed" when one concept was checked once.

**`pytest.raises`** asserts that invalid input is rejected. For numerical code
this is where the physical validity checks live: a negative velocity, a zero
density contrast, a time step that violates a stability condition. A function
that silently returns a plausible-looking number for unphysical input is worse
than one that raises.

**`tmp_path`** gives each test a fresh directory, so a test that writes a file
cannot corrupt a neighbour or the repository. **`monkeypatch`** sets an
environment variable or replaces an attribute and undoes it afterwards, which is
how you test code that reads `OMP_NUM_THREADS` without permanently changing your
own environment. **`skipif`** documents a platform or version dependency;
**`xfail`** documents a *known* failure so that a real failure is still visible.

## 5. Python demonstration

The module's `code/` directory contains:

- `geophys_tools.py` — eight short functions under test (moveout, point-mass
  gravity, free-air gradient, Bouguer slab, phase wrapping, a seeded synthetic
  profile, a two-column file reader, a dominant-frequency estimator);
- `pytest_basics_demo.py` — a script that prints every measurement quoted above;
- `test_pytest_basics.py` — a genuine pytest suite: three fixture scopes four
  parametrised tests, `pytest.raises`, `tmp_path`, `monkeypatch`, a `skipif` and
  one `xfail`.

Run them with the project virtual environment:

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/pytest_basics_demo.py
.venv/bin/pytest 03-scientific-computing/13-testing-profiling-packaging/code/test_pytest_basics.py -q
```

The measured result of the suite in this environment is

```
22 passed, 1 xfailed in 0.06s
```

The `xfail` is the assertion that $d^{-2} = (1/d)^2$ bitwise. It is in the suite
on purpose: it documents, executably, that the bitwise expectation is wrong, so
that nobody "fixes" the tolerance by removing the tolerance.

Three assertions from that suite are worth reading as models:

```python
def test_inverse_square_routeings_are_not_bit_identical():
    """`d**-2` and `(1/d)**2` differ by 1 ulp -- so equality is the wrong test."""
    d = 300.0
    assert d ** -2 != (1.0 / d) ** 2
    assert d ** -2 == pytest.approx((1.0 / d) ** 2, rel=1e-15)
```

```python
def test_bouguer_slab_round_trip():
    """Thickness -> effect -> thickness must return the input."""
    for drho in (200.0, 400.0, 600.0):
        thickness = 1500.0
        dg = 2.0 * math.pi * gt.G_SI * drho * thickness * gt.GAL_PER_MS2
        assert gt.bouguer_slab_thickness_m(dg, drho) == pytest.approx(thickness, rel=1e-12)
```

```python
def test_synthetic_profile_is_reproducible(noisy_profile):
    again = gt.synthetic_elevation_profile(512, seed=20240101)
    np.testing.assert_array_equal(noisy_profile, again)
```

The first asserts a *dis*equality as the physical fact and then bounds the
inequality; the second is a round trip, which needs no reference value at all
and therefore cannot be defeated by a wrong reference; the third is a bitwise
assertion, which is legitimate **only** because the two arrays are produced by
the same code path from the same seed, and so are required to be identical
rather than merely close.

### 5.1 A measured correction to a common assumption

The suite asserts the free-air gradient against the spherical formula
$2g/R = 0.30785$ mGal/m, not against the conventional $0.3086$ mGal/m. The
difference is $0.24\%$ — about $0.8$ mGal over 1 km of relief, which is larger
than most targets. The conventional value carries flattening and centrifugal
terms that the spherical formula omits. Writing
`assert gradient == pytest.approx(0.3086, rel=1e-4)` would have failed, and the
honest response is to fix the *claim*, not to loosen the tolerance until the
number fits.

## 6. Assumptions and limits

- **`approx` and `assert_allclose` assume the reference value is exact.** If
  the reference itself came from a previous run of the same code, the test
  compares the code with itself. That is a *regression* test, useful for
  detecting change and useless for detecting error.
- **A passing suite bounds nothing about untested behaviour.** Executing a line
  is not the same as checking what it computed; the failure mode is
  demonstrated with measured line coverage in
  [03-13-04 Code Quality](./04-code-quality.md) and in
  `code/coverage_demo.py`.
- **Timing is not testable.** Wall-clock assertions fail on a loaded CI runner
  and pass on a developer's laptop. Assert counts or residuals instead.
- **Randomised tests need a seed**, and the seed belongs in the test, not in the
  environment. See [03-02-06 Random Numbers](../02-numpy/06-random-module.md)
  for why `default_rng(seed)` is preferred to the legacy global `np.random.seed`.

## 7. Common mistakes

1. `assert a == b` on computed floats. It tests the last bit; it will differ
   between machines.
2. `assert a == pytest.approx(b)` where `b` is zero and the tolerance is
   relative-only. For a cancellation residual, pass `atol` derived from the
   arithmetic.
3. Passing `rel=` and believing the tolerance is now purely relative. The
   measured $10^{-12}$ floor remains until `abs=0` is passed.
4. Using `abs=` with pytest and assuming the relative band is still active. A
   specified `abs` alone switches to a pure absolute band.
5. Loosening a tolerance until the test passes. If the derivation is right and
   the test fails, the code is wrong or the derivation is; loosening hides which.
6. Writing one long test that asserts twelve things. When it fails you learn
   which twelve you just invalidated; the parametrised form reports the exact
   case.
7. Putting mutable shared state in a session-scoped fixture and then mutating it.
8. Treating `pytest.raises(Exception)` as validation. Be specific: a typo in the
   function name raises `AttributeError` and would satisfy `Exception`.

## 8. Continuous integration

Running the suite by hand is the same computation as running it in CI; what CI
adds is that it happens without being asked. Described in prose — this
repository has no workflow files and nothing here was executed on a runner — the
standard arrangement is a YAML file under `.github/workflows/`:

```yaml
name: tests
on:
  push:
    branches: [main]
  pull_request:
jobs:
  pytest:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest -q
```

The matrix is the part that earns its keep for a numerical library: the same
assertions on two interpreter versions catch bit-level differences that a single
run cannot. See the [GitHub Actions documentation](https://docs.github.com/en/actions)
and the [workflow syntax reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).

## 9. Real-world applications

- **A gravity reduction pipeline.** A sign error in the free-air correction
  produces an anomaly wrong by $2 \times 0.3086 \times h$ mGal — measured as
  $61.72$ mGal at 100 m of relief in `code/coverage_demo.py`. A round-trip test
  (correct, then invert, then compare) catches it; a smoke test does not.
- **Seismic processing.** Moveout, statics and gain are all short formulas with
  a few branches. Parametrised tests over the physical ranges of $t_0$, $v$ and
  $x$ catch the sign and unit errors that elude review.
- **Instrument-level regression suites.** Observatories test a processing chain
  against a stored "golden" record. Golden tests detect change; they do not
  detect error, which is why they are paired with an analytic check.
- **Publication code.** A journal increasingly asks for tests. The minimum
  credible set is: one analytic check per numerical routine, one property
  (round trip, monotonicity, symmetry), and one guard per physical constraint.

## 10. Further reading

- **pytest documentation.** [Assertions and `approx`](https://docs.pytest.org/en/stable/how-to/assert.html),
  [fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html),
  [parametrisation](https://docs.pytest.org/en/stable/how-to/parametrize.html),
  [`monkeypatch`](https://docs.pytest.org/en/stable/how-to/monkeypatch.html).
  Level: reference. Read `ApproxScalar.tolerance` in the installed
  `_pytest/python_api.py` once; the $10^{-12}$ floor becomes obvious and stops
  being a surprise.
- **NumPy.** [`numpy.testing.assert_allclose`](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html).
  Level: reference. The `rtol`/`atol` defaults and the `equal_nan` flag.
- **Python standard library.** [`unittest`](https://docs.python.org/3/library/unittest.html)
  for the framework pytest replaces, and
  [`random`](https://docs.python.org/3/library/random.html) for seeding.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapter 1. Level: advanced. The source of the $nu$ bound
  used in Section 3.1 and of the conditioning viewpoint throughout.
- **Goldberg, D. (1991). What every computer scientist should know about
  floating-point arithmetic. *ACM Computing Surveys*, 23(1), 5–48.** Level:
  intermediate. The accessible account of the model in Section 2.1.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> current editions through your library.

## 11. Related lessons

- [03-13-02 Testing Numerical Code Against Analytic Solutions](./02-testing-scientific-code.md)
  — what to compare against when there is no other implementation to compare to.
- [03-13-03 Profiling CPU and Memory](./03-profiling.md) — measuring instead of
  guessing, for time rather than for values.
- [03-13-04 Code Quality](./04-code-quality.md) — the static checks that catch
  the defects no test exercises, and the coverage measurement that misleads.
- [03-13-08 Reproducible Environments](./08-reproducible-environment.md) — why
  the same suite can pass on one machine and fail on the next.
- [03-02-06 The NumPy Random Module](../02-numpy/06-random-module.md) — seeding,
  and what "reproducible" does and does not guarantee.

## 12. Self-assessment checklist

- [ ] I can explain, in one sentence, why `assert 0.1 + 0.2 == 0.3` fails and
      why that failure carries no information. (§1)
- [ ] I can state the acceptance band of `pytest.approx(1e6)` without running
      it. (§2.3)
- [ ] I know that passing `rel` to pytest leaves a $10^{-12}$ absolute floor,
      and what to pass to remove it. (§2.3)
- [ ] I know that `assert_allclose` defaults to a zero absolute band, and that
      a residual assertion therefore needs `atol`. (§2.3)
- [ ] I can derive a tolerance from $u$ and an amplification factor I measured,
      and write the derivation in a comment. (§3.4)
- [ ] I can recognise a formula whose conditioning makes any tolerance
      meaningless, and say what to fix instead. (§3.2)
- [ ] I can choose a fixture scope and justify it. (§4)
- [ ] I can write a round-trip test that needs no reference value. (§5)
- [ ] I can name one assertion in my own work that would pass on wrong code, and
      say what I am going to replace it with. (§7)
