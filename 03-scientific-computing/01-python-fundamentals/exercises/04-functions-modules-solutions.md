# Solutions — 03-01-04 Functions, Scope, Modules and Packages

> **Read this after attempting the exercises, not before.** Anything attributed to
> a demo is its actual printed output.

---

## ★1 — Velocities of an idealised medium

**(a)**

$$v_p = \sqrt{\frac{\lambda + 2\mu}{\rho}}
= \sqrt{\frac{8.0\times10^{9} + 8.0\times10^{9}}{2200}}
= \sqrt{7.2727\times10^{6}} = 2696.8\ \text{m s}^{-1},$$

$$v_s = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{4.0\times10^{9}}{2200}}
= \sqrt{1.81818\times10^{6}} = 1348.4\ \text{m s}^{-1}.$$

**(b)** $v_p/v_s = 2696.8/1348.4 = 2.0000$ exactly (to four decimals).

$$\nu = \frac{v_p^2 - 2v_s^2}{2(v_p^2 - v_s^2)} = \frac{4 - 2}{2(4-1)} = \frac{2}{6}
= \frac{1}{3}.$$

**(c)** `velocity_lib.vp_from_moduli(8.0e9, 4.0e9, 2200.0)` returns
`2696.7994498529683`; `vs_from_moduli(4.0e9, 2200.0)` returns `1348.3997249264842`;
`poisson_ratio(2696.799…, 1348.399…)` returns `0.33333333333333337`. The hand and
library values agree to the digits carried.

**(d)** The ratio of squares is
$(v_p/v_s)^2 = (\lambda + 2\mu)/\mu = 1 + \lambda/\mu$, so it depends only on
$\lambda/\mu$: here $\lambda = 2\mu$, giving $(v_p/v_s)^2 = 4$, $v_p/v_s = 2$ and
$\nu = 1/3$. The single input number that determines $\nu$ is therefore the ratio
$\lambda/\mu$; the absolute scale of the moduli and the value of $\rho$ set the
speeds but not $\nu$.

$\nu = 1/3$ implies $v_p/v_s = 2$. Worth keeping apart: the classical "Poisson
solid" has $\nu = 0.25$, hence $v_p/v_s = \sqrt{3} \approx 1.732$, and that is the
value often quoted for a homogeneous mantle-like material. This example, with
$\lambda = 2\mu$, is *not* a Poisson solid.

---

## ★2 — What each command tests

```text
velocity_lib: all self-tests passed
```

`python3 velocity_lib.py` runs the module's `_self_test()`, which asserts physical
invariants (a solid has $0 < v_s < v_p$; Poisson's ratio lies in $(-1, 0.5)$; a
fluid has zero shear velocity; impedance scales linearly) and that the two guard
rails raise.

`python3 -m doctest velocity_lib.py` produces **no output** when all docstring
examples pass, and a count of failures when they do not. It tests that the
executable examples embedded in the docstrings still match the code.

`python3 functions_modules_demo.py` runs the lesson's demonstration, which imports
`velocity_lib` first. That import is safe — no self-test runs, no table prints —
because the self-test is behind `if __name__ == "__main__":`. **The guard is what
makes a module importable.** Without it, the middle command would print the
self-test output before its own results, and a test runner importing the module
would execute the demo.

Both of the first two commands can be run without the third because the module is
self-contained; that is precisely the property a module is supposed to have.

---

## ★3 — The mutable default

`bad2` is `['STA01', 'STA02']` and `bad1 is bad2` is `True`: both names refer to
the *same* list object.

The second call did not start from an empty list. The default `[]` in the `def`
statement was evaluated once, when the module was defined, and every call that
omits the argument receives a reference to that one list. The first call appended
`'STA01'` to it; the second appended `'STA02'` to the same object, so the first
call's returned value grew. The demo prints `bad1 is now ['STA01', 'STA02']` to
make the aliasing visible.

---

## ★4 — The safe version with a proof

```python
def add_reading(value, readings=None):
    if readings is None:
        readings = []
    readings.append(value)
    assert len(readings) == 1 or readings is not None   # nothing meaningful
    return readings
```

A stronger, actually meaningful proof: pass the *expected* length so the function
can check itself, or check identity between calls.

```python
def add_reading(value, readings=None):
    if readings is None:
        readings = []
    before = len(readings)
    readings.append(value)
    assert len(readings) == before + 1, "the append did not add exactly one"
    return readings

a = add_reading(1.0)
b = add_reading(1.0, add_reading(2.0))
c = add_reading(1.0, add_reading(2.0, add_reading(3.0)))
print(len(a), len(b), len(c))      # 1 2 3
print(a is b, b is c, a is c)      # False False False
```

**(a)–(b)** as above. The assertion that the append adds exactly one item is the
invariant worth stating; an assertion comparing `len(readings)` with the number of
items passed would need that number, which is `1` for this function, giving
`len(readings) == 1` — and that is only true when the caller passed no list. Note
the trap in the first draft above: a tautology like
`assert len(readings) == 1 or readings is not None` tests nothing. **An assertion
that cannot fail is worse than no assertion, because it looks like a check.**

**(c)** Lengths 1, 2, 3 and `a is b is c` all `False`. The identity test is the
one that actually proves the fix.

---

## ★5 — The demo's scope and defaults output

**(a)**

```text
  after two nonlocal bumps, counter = 2
  after leak(), the module global ACCIDENTAL = 42
  helper() = 0.6172: the global was read at call time
```

**(b)**

```text
  bad:  first call  -> ['STA01']
  bad:  second call -> ['STA01', 'STA02']   <- second call edited the first result
        bad1 is now ['STA01', 'STA02']
        bad1 is bad2 -> True
  good: first call  -> ['STA01']
  good: second call -> ['STA02']
        good1 is good2 -> False
```

**(c)**

```text
  pure:   7,500,000.0 then 7,500,000.0
  impure: 7,500,000.0 and the
          module now carries 1 entry outside the function
```

`helper()` is 0.6172 because the module set `hidden = 1.0`, then defined `helper`
(which multiplies `hidden` by 0.3086), then *reassigned* `hidden = 2.0`, and only
then called `helper()`. The free name `hidden` is resolved at call time, not at
definition time — late binding — so the function sees 2.0 and returns
$2.0 \times 0.3086 = 0.6172$. It is the same mechanism that makes a list of lambdas
created in a loop all capture the loop variable's *final* value.

---

## ★6 — A signature with keyword-only options

```python
def terrain_correction(
    station_elevation_m,
    surrounding_elevations_m,
    density_kg_m3=2670.0,
    *,
    max_radius_m=None,
    return_diagnostics=False,
):
    """Compute an approximate terrain correction for one station.

    Parameters
    ----------
    station_elevation_m : float
        Station elevation above the datum, in metres.
    surrounding_elevations_m : sequence of float
        Elevations of the surrounding terrain samples, in metres.
    density_kg_m3 : float
        Nominal rock density, in kg m^-3.  Must be positive.
    max_radius_m : float or None
        Ignore terrain samples further than this, in metres.  None uses all.
    return_diagnostics : bool
        If True, return (correction_mgal, diagnostics_dict).

    Returns
    -------
    float or tuple
        The correction in mGal, optionally with a diagnostics dict.
    """
```

**(b)** The bare `*` is placed after `density_kg_m3` because density is a *physical
parameter of the problem* — it is meaningful to pass it positionally — while
`max_radius_m` and `return_diagnostics` are *settings* that a reader should have to
name. The bare `*` prevents
`terrain_correction(h, neighbours, 2670.0, True)` from silently setting
`max_radius_m = True`, which without the `*` it would do.

**(c)** As written: every parameter carries its unit in its name **and** in the
docstring, which is redundant on purpose — the name is what a reader sees at the
call site, the docstring is what a reader sees in `help()`.

---

## ★7 — The module

```python
"""Small gravity-reduction helpers.  Standard library only."""
from __future__ import annotations
import math

G = 6.67430e-11
M_PER_S2_PER_MGAL = 1.0e-5
FREE_AIR_GRADIENT_MGAL_PER_M = 0.3086
REFERENCE_DENSITY_KG_M3 = 2670.0

def free_air_mgal(h_m, gradient=FREE_AIR_GRADIENT_MGAL_PER_M):
    """Free-air correction in mGal: positive with height."""
    return gradient * h_m

def slab_mgal(h_m, rho=REFERENCE_DENSITY_KG_M3):
    """Infinite-slab (simple Bouguer) term in mGal: 2*pi*G*rho*h."""
    if rho <= 0.0:
        raise ValueError(f"density must be positive, got {rho!r}")
    return 2.0 * math.pi * G * rho * h_m / M_PER_S2_PER_MGAL

def simple_bouguer_mgal(observed_mgal, h_m, rho=REFERENCE_DENSITY_KG_M3):
    """Simple Bouguer anomaly: observed + free-air - slab."""
    return observed_mgal + free_air_mgal(h_m) - slab_mgal(h_m, rho)

def _self_test():
    assert free_air_mgal(0.0) == 0.0
    assert free_air_mgal(100.0) > 0.0
    assert abs(free_air_mgal(100.0) - 30.86) < 0.01
    assert slab_mgal(0.0) == 0.0
    assert slab_mgal(100.0, 2670.0) > 0.0
    assert abs(slab_mgal(100.0) - 11.1969) < 1e-3
    assert slab_mgal(200.0) == 2.0 * slab_mgal(100.0)
    assert slab_mgal(100.0, 2670.0) > slab_mgal(100.0, 2400.0)
    for bad in (0.0, -1.0):
        try:
            slab_mgal(100.0, bad)
        except ValueError:
            pass
        else:
            raise AssertionError("non-positive density accepted")
    print("gravity_lib: all self-tests passed")

if __name__ == "__main__":
    _self_test()
```

**(a)** Invariants and why none has an exception:

1. `free_air(0) == 0` — at the datum there is nothing to correct.
2. `free_air(100) > 0` — the correction adds back what height removed.
3. `slab(0) == 0` — a station at the datum has no rock above the datum.
4. `slab(200) == 2*slab(100)` — the slab term is *exactly linear* in $h$; this is
   not an approximation, it is the equation.
5. `slab(h, 2670) > slab(h, 2400)` — the term is monotone in density.
6. The guard rails raise — the module cannot silently accept an impossible density.

**(b)** `slab_mgal(100.0)` returns

$$2\pi \times 6.67430\times10^{-11} \times 2670 \times 100 / 10^{-5}
= 11.1969\ \text{mGal},$$

which is the value quoted in lesson 05 and in lesson 08's demo output.

**(c)** `slab_mgal(100.0, 0.0)` raises
`ValueError: density must be positive, got 0.0`; `slab_mgal(100.0, -1.0)` raises the
same with `got -1.0`. Passing a string for `h_m` raises a `TypeError` from the
multiplication, with no unit information in the message — which is the limitation
the module's documentation should acknowledge.

**(d)** From a second file:

```python
import gravity_lib
print(gravity_lib.slab_mgal(100.0))
```

prints `11.196875606754224` and nothing else. The `__main__` guard is what
prevents the self-test output from appearing.

---

## ★8 — A units bug that validation cannot catch

**(a)** A type hint says `float`; 2670 and 2.67 are both `float`. A docstring is
prose and is not executed. An assertion can only check what it can express, and
"density in the range of rock densities" is satisfied by 2.67 (if the author thinks
in g cm⁻³) — worse, an assertion written as `0 < rho < 4000` accepts both 2670 and
2.67, and one written as `2000 < rho < 3500` would reject a legitimate 1.0 kg m⁻³
soil. **The type is the same, so no type-based check exists; the only signals are
dimensional (unavailable) or contextual (a plausible-magnitude range, which is a
judgement, not a fact).**

**(b)** Three interface changes:

| Change | Effect |
|---|---|
| Rename the parameters `density_kg_m3`, `depth_m` | The unit is visible at every call site; a reviewer sees `density_kg_m3=2.67` immediately |
| Accept a unit-bearing quantity (`dict`, or a small `Quantity` record) instead of a bare float | The unit becomes data, and the function converts or raises; cost: the caller must construct it |
| Require the caller to pass SI and **validate the range with a physically derived bound** (e.g. reject densities outside 900–8000 kg m⁻³, noting 900 is roughly the density of ice and 8000 exceeds iron) | Catches 2.67 and 2670-as-g-cm⁻³ style errors; cost: an artificial input is rejected |

All three cost the caller something, and that is the honest trade: **a unit bug is
prevented by making the interface carry units, not by checking the numbers.**

**(c)** At fixed mass, $g = GM/z^2$ so $z \propto 1/\sqrt{\rho}$ when $M$ is held
at a constant that depends on $\rho$... In the geometry where the *mass* is
inferred from the anomaly and then converted to a depth, the depth scales as
$z \propto \rho^{-1/2}$ for a fixed measured anomaly as well. A factor-of-2 density
error gives a depth error of $\sqrt{2} = 1.41$, i.e. **41 per cent too deep or 29
per cent too shallow** depending on the direction. That would be obvious *if* the
error were 2×.

The subtle case is the realistic one: reading 2.67 as if it were 2670 and *dividing*
rather than multiplying, or a g cm⁻³ value of 2.6 used where 2.67 belongs — a
2.6 per cent density error gives a 1.3 per cent depth error, on a 400 m depth that
is 5 m, and it is invisible. **Factor-of-two unit errors are caught by review;
decade-compatible ones are not.** That asymmetry is why the fix must be at the
interface.

---

## ★9 — Refactoring plan

*Model answer in outline, 400–500 words; the required elements are:*

**Test first, then touch.** Before any refactoring, run the script on a fixed input
and save its output as a regression fixture (or, if it is stochastic, seed it and
save the output). The risk of refactoring without that test is that a 900-line
script has behaviours nobody has documented — a subtle order-dependence, a
temporary file that a later step reads, a default that is only correct for one
data set. Refactoring then changes behaviour invisibly, and the change is
discovered months later.

**The three functions to extract first**, in order:

1. **Input reading and validation.** Everything from `open` to the first numeric
   variable. It is the boundary of the program, it is where bad data enters, and it
   is the piece most likely to be reused. Extracting it forces the units, the
   encoding, the skipped lines and the validation into one place.
2. **The physics reduction.** The block that turns measured values into anomalies,
   velocities or depths. It is the part with a specification, so it is the part
   that can be *tested* against a hand calculation — the highest-value function in
   the file.
3. **Output writing.** The block that formats and writes. Extracting it makes the
   atomic-write discipline (lesson 10) applicable, and it separates "what the
   answer is" from "how it is printed".

**The state that must become a parameter.** Any module-level variable that a
function reads *and* another function writes — typically the density, the datum
elevation, or the survey's reference station. It must become an explicit argument,
because otherwise the function's result depends on call order (the late-binding
demonstration from §3 of the lesson). The tell is a variable assigned near the top
of the script and referenced inside a block you are extracting: if the block would
have to read it, pass it.

**The risk of not doing it.** Without the extracted functions, the script has no
unit under test: there is nothing to call with a known input, so there is nothing
to assert, so the output can only be judged by whether it "looks right" — which is
precisely the judgement that misses a systematic amplitude or unit error.
