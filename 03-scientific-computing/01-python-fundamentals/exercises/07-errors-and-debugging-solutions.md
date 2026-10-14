# Solutions — 03-01-07 Exceptions, Assertions and Systematic Debugging

> **Read this after attempting the exercises, not before.** Numbers attributed to
> the demo are its actual printed output.

---

## ★1 — Assertion or validation

| Check | Kind | Under `python3 -O` |
|---|---|---|
| (a) `assert 0 < vs < vp` | assertion (a law of isotropic elasticity) | **removed** |
| (b) `if rho <= 0: raise ValueError` | validation (a user or file can supply it) | unchanged |
| (c) `assert 0 <= latitude <= 90` | depends: validation if a file supplies it, assertion if the code constructed it internally | removed if written as `assert` |
| (d) `if len(samples) == 0: raise` | validation | unchanged |
| (e) `assert isclose(vp, expected, rel_tol=1e-12)` | assertion — this is a *test*, and its purpose is to fail loudly in development | removed, hence tests must not be run with `-O` |

The rule: **assertions may be optimised away, so anything required for
correctness — and anything a user can trigger — must be an `if`/`raise`.** (c) is
the instructive case: a latitude range check is a physical law *and* an input
check, and where it belongs depends on where the value came from. If a CSV supplied
it, it is validation; if the code computed it from a station's coordinates, an
assertion is defensible.

---

## ★2 — An exception that carries units

```python
class UnitError(ValueError):
    """Raised when a value's unit contradicts the contract of the function."""
    def __init__(self, parameter, value, expected_unit, inferred_unit):
        self.parameter, self.value = parameter, value
        self.expected_unit, self.inferred_unit = expected_unit, inferred_unit
        super().__init__(
            f"{parameter} = {value!r}: expected {expected_unit}, "
            f"looks like {inferred_unit}")
```

Two raises:

```python
raise UnitError("density", 2.67, "kg m^-3", "g cm^-3")
# density = 2.67: expected kg m^-3, looks like g cm^-3

raise UnitError("depth", 0.5, "m", "km")
# depth = 0.5: expected m, looks like km
```

Inheriting from `ValueError` means a caller that already catches `ValueError`
still works, while a caller that wants the structured fields can catch `UnitError`.
The message names the *expected* and the *inferred* unit, which is what turns a
failure into a fix: the reader knows both what to change and why the code
recognised the problem.

---

## ★3 — Which clause

**(a)** `try` for the write, `except` for the failure, and the header write belongs
*inside* the guarded block — but note that a header that must exist before the
computation is a sequencing problem, so the file write and the computation should be
in separate `try` blocks and the computation must not start until the header write
has succeeded. `else` is the natural place for the computation: it runs only if the
write succeeded.

**(b)** `finally`. The lock must be released whether the block succeeded, failed or
returned early; `finally` is the only clause with that guarantee. (Prefer a context
manager, lesson 10.)

**(c)** `else`. The parse belongs after the `try`, and `else` is what expresses
"only if no exception occurred" without widening the `try`.

**(d)** `except ZeroDivisionError as exc: raise UnitError(...) from exc`. Catching
the specific type is required — a bare `except Exception` would also catch a bug in
the conversion code. `raise ... from exc` preserves the original traceback, so the
log shows both the division by zero and the domain-level message.

---

## ★4 — The demo's validation and clauses

**(a)**

```text
  density 2670.0     -> accepted, ok
  density 8100.0     -> accepted, warning: denser than iron (7874 kg m^-3)
  density 30000.0    -> REJECTED: density = 30000.0 kg m^-3: exceeds osmium (22590 kg m^-3)
  density 0.0        -> REJECTED: density = 0.0 kg m^-3: must be positive
  density nan        -> REJECTED: density = nan kg m^-3: NaN: the measurement failed
  density '2670'     -> REJECTED: density = '2670' kg m^-3: not a number
```

**(b)**

```text
  reciprocal_velocity(3000.0)
    else: slowness = 3.333333e-04 s/m
    finally: this runs either way (closing files, releasing locks)
  reciprocal_velocity(0.0)
    except: velocity was zero
    finally: this runs either way (closing files, releasing locks)
```

**(c)**

```text
  the call path, outermost first (4 frames):
    part6_traceback()  line 178:  outer(5.0)
    outer()  line 169:  return middle(n)
    middle()  line 172:  return inner(n)
    inner()  line 175:  return [0.0] * n[0]         # n is a float, not a sequence
  the exception: TypeError: 'float' object is not subscriptable
```

**Why 8 100 does not raise but 30 000 does.** The bound is a *physical* one:
osmium is the densest naturally occurring element, at approximately
22 590 kg m⁻³, so no sample of terrestrial rock can exceed it and a value above the
bound is not a measurement error but an *interpretation* error — a unit mistake, a
misparsed field, or a corruption. 8 100 kg m⁻³ is denser than iron (≈ 7 874 kg m⁻³)
and is entirely possible for a massive sulphide or magnetite ore, so rejecting it
would reject real data.

**The design principle:** *reject the impossible, warn about the surprising.* A
validator that rejects the merely unusual is switched off within a week, and then
it rejects nothing at all. The bound is a named constant with a comment for exactly
this reason: it is a fact about the periodic table, not a preference.

---

## ★5 — Silent versus counted skips

```text
  with 'except ValueError: pass' -> total = 21.5
  with a counted skip            -> total = 21.5, skipped = 1
```

**(a)** Both totals are 21.5 because the input is `["12.4", "oops", "9.1"]` and
$12.4 + 9.1 = 21.5$: the unparseable row contributed nothing either way. Only the
second is trustworthy because it reports that one of three rows was discarded;
without that number, a reader cannot know whether the sum covers all the data or
two thirds of it. **The number is right; the population is wrong.**

**(b)** Adding `"12.0"` (a magnitude above any terrestrial earthquake, whose
largest recorded values are around 9.5):

- the silent version sums it: $21.5 + 12.0 = 33.5$ — a total that now includes a
  physically impossible datum, and no line of output announces it;
- a range-checking version reports `total = 21.5, skipped = 2 (out of range)`.

The second is auditable. Note that a parse-only check (the demo's version) would
*happily accept* 12.0, which is why the validation must be physical and not merely
syntactic: **`float("12.0")` succeeds, and that is exactly the problem.**

**(c)** The one-line change: count the skipped rows and print the count with the
total, i.e. replace

```python
except ValueError:
    pass
```

with

```python
except ValueError:
    skipped += 1
```

and report `skipped` beside the result. Everything else — logging the offending
field, raising above a threshold — builds on that count.

---

## ★6 — The unit bug

**(a)** The demo's §5 function is a *normalised kernel*,
`anomaly(offset, depth) = 1.0 / (offset**2 + depth**2) ** 1.5`, with no $G$, no
mass and no mGal conversion; at $x = 0$ it reduces to $1/z^3$. The call
`anomaly(0.0, 0.5)` therefore treats the depth as 0.5 m and returns
$1/0.5^3 = 8.0$, whereas a depth of 500 m gives $1/500^3 = 8\times10^{-9}$ — a
factor of $10^{9}$. Because the epicentral kernel is a **cube law** in depth, a
linear 1000× unit error enters as its cube.

(The full physical forward model of lesson 01 is $GMz/(x^2+z^2)^{3/2}$, which at
$x=0$ is $GM/z^2$ — a *square* law, so the same 1000× unit error would enter as
$10^{6}$ there and the returned value would be 0.268390 mGal times $10^{6}$. The
demo uses the simplified kernel to keep the arithmetic visible; the lesson is the
same either way: **a unit error enters as a power law, and the power is set by the
model**.)

**(b)** No `except` clause can catch it because **nothing illegal happened**:
`0.5` is a valid `float`, the division is well defined, the result is finite. An
exception is raised only for conditions the interpreter can *name* — a type error,
a missing file, a division by zero. A unit error produces a perfectly valid number,
and the only signals are dimensional (not available to the interpreter) or
contextual (a range, a comparison with a known case).

**(c)** The five-line test:

```python
def test_anomaly_known_case():
    # A body of radius 200 m, excess density 300 kg/m3, at 500 m depth:
    # the peak is 0.268390 mGal by hand (lesson 01).
    value = sphere_anomaly_mgal(300.0, 200.0, 500.0, 0.0)
    assert abs(value - 0.268390) < 1e-5, value
```

The test fails loudly when the units are wrong, because it compares against a
number derived independently of the code.

**(d)** Two naming changes: `depth_m` instead of `depth` (the unit travels with
every use of the name, including at the call site) and `anomaly_mgal` instead of
`anomaly` (so the return value's unit is also part of the name). Neither is a
check; both are documentation that cannot drift, which is why they are more
reliable than a comment.

---

## ★★7 — A layered velocity-model validator

```python
class ModelError(ValueError):
    def __init__(self, layer_index, field, value, reason):
        super().__init__(f"layer {layer_index} field {field!r} = {value!r}: {reason}")

def validate_model(layers):
    previous_top = 0.0
    for i, (top_km, vp, vs, rho) in enumerate(layers):
        if not isinstance(top_km, (int, float)) or isinstance(top_km, bool):
            raise ModelError(i, "top_depth_km", top_km, "not a number")
        if top_km < 0.0:
            raise ModelError(i, "top_depth_km", top_km, "depth cannot be negative")
        if top_km <= previous_top:
            raise ModelError(i, "top_depth_km", top_km,
                             f"must exceed the previous layer top {previous_top}")
        if not 1400.0 <= vp <= 8500.0:
            raise ModelError(i, "vp_m_s", vp,
                             "outside 1400-8500 m/s (water to the deepest mantle rock)")
        if not 0.0 < vs < 5000.0:
            raise ModelError(i, "vs_m_s", vs, "outside 0-5000 m/s (a fluid has vs = 0)")
        if vs >= vp:
            raise ModelError(i, "vs_m_s", vs, f"an isotropic solid requires vs < vp = {vp}")
        if not 900.0 <= rho <= 8000.0:
            raise ModelError(i, "density_kg_m3", rho,
                             "outside 900-8000 kg/m^3 (ice to iron-rich ore)")
        previous_top = top_km
    return layers
```

**(a)** Bounds and their justifications:

| Field | Bound | Justification |
|---|---|---|
| `vp_m_s` | 1 400–8 500 | 1 400 is below the speed in water (≈ 1 500 m/s), so a rock slower than that is a saturated sediment or an error; 8 500 is above the fastest mantle values, so a higher value is a unit or formula error |
| `vs_m_s` | 0 < $v_s$ < 5 000 | a fluid has $v_s = 0$ exactly, which is legal but must be handled downstream; 5 000 exceeds any terrestrial rock |
| `rho_kg_m3` | 900–8 000 | 900 is roughly the density of ice, the lightest plausible crustal material; 8 000 slightly exceeds iron and is below osmium |
| `top_depth_km` | ≥ 0, strictly increasing | depth below a datum is non-negative, and layers are ordered by construction |

**(c)** The cross-field check used is **$v_s < v_p$**, with the message naming both
values. This is the isotropic-solid condition; $v_p > v_s\sqrt{2}$ holds only for
$\nu > 0$ (which fails for auxetic media), so the weaker condition is the correct
one. A second useful cross-check — that $v_p/v_s$ lies in roughly 1.4–2.5 for a
rock — is deliberately *not* enforced, because a gas-saturated or highly porous
rock can fall outside it and the check would reject real models.

**(d)** Demonstration output:

```text
valid model: accepted, 3 layers
ModelError: layer 1 field 'top_depth_km' = 1.0: must exceed the previous layer top 2.0
ModelError: layer 0 field 'vs_m_s' = 5000.0: an isotropic solid requires vs < vp = 3500.0
ModelError: layer 2 field 'vp_m_s' = 2670.0: outside 1400-8500 m/s (water to the deepest mantle rock)
```

Note the third case: 2 670 is a *density*, passed where a velocity was expected —
the classic argument-order error, caught because the bound is physical.

---

## ★★8 — 588 missing rows

**(a)** Four mechanisms and their detectability:

| Mechanism | Detectable from inputs? |
|---|---|
| Rows skipped by a caught exception (parse failure) | Yes, if counted; the input row count is known |
| Rows lost by a `dict` key collision — two rows mapping to the same key in a dedupe step | Yes, by comparing the count of distinct keys against the count of rows |
| Rows filtered by a range or completeness cut (e.g. magnitude below threshold) | Yes, but only if the filter is declared; an implicit filter is invisible |
| Rows silently overwritten by an output file opened per row rather than appended | **No** — detectable only from the output count vs the input count |
| Rows lost to a buffer that was never flushed at exit | Partially — detectable by re-reading the output |

**(b)** Bias:

- **Parse failures**: biased if the failing rows share a property (a network, an
  epoch, a magnitude format). A magnitude that fails to parse is often a
  placeholder, and placeholders cluster in early instrumental periods, so the
  surviving sample is biased *old-to-new*; the resulting $b$-value and the
  completeness threshold shift.
- **Key collisions**: strongly biased — the surviving row is whichever came last
  in the file, so duplicates are resolved by file order, which correlates with
  catalogue version.
- **Declared range filter**: unbiased *if* the cut is on the variable being
  analysed, and a pure sample-size reduction; biased if the cut correlates with
  another variable (a magnitude cut correlates with depth of detection).
- **Overwritten output**: noisier, not biased, if the loss is a random subset; but
  a file-per-row bug loses a *contiguous* block (all but the last), which is a
  catastrophic bias.

**(c)** The audit line:

```python
log.info("ingest: read=%d accepted=%d rejected_parse=%d rejected_range=%d "
         "duplicate_keys=%d written=%d", n_read, n_ok, n_parse, n_range, n_dup, n_written)
```

Printing the *inputs and outputs of every stage* rather than a single "processed"
count is what makes a deficit attributable without a re-run. The single most
valuable term is `written`, because the input-side counters cannot detect a loss
that happens on output.

---

## ★★9 — Failure policy for a 10⁶-row ingest

| Defect class | Policy | Reason |
|---|---|---|
| Blank field | **Skip and count** | The row is unusable; the defect rate is informative, and a blank in one field does not invalidate the file |
| Unparseable number | **Skip and count** | Same, but count *per column*, because a column that fails often is a format change, not a data defect |
| Physically impossible value (magnitude > 10, depth < 0, latitude 91) | **Raise if systematic, warn and skip if isolated** | An impossible value is evidence of a unit or schema error upstream; one occurrence is a bad row, a hundred is a broken pipeline |
| Duplicate event ID | **Warn, keep first, count** | Duplicates are a property of the catalogue; silently dropping them changes the event count and any rate statistic |
| Missing required column | **Raise** | Every subsequent row would be misinterpreted; the interpretation of the file is impossible, so no output is valid |

**(b)** The physics: magnitudes, depths and coordinates each have hard physical
bounds, and a value outside them cannot be a measurement, so it must be an
input-side error. The *purpose* of the catalogue matters too: a catalogue used for
a $b$-value estimate is sensitive to which rows are dropped (the drop is a
completeness effect), whereas one used to locate a single well-recorded event is
not.

**(c)** Escalation threshold: a skip-and-count policy should fail the run when the
rejected fraction exceeds a pre-declared limit, and when the rejects are
*systematic* rather than scattered. A defensible default: fail if more than 1 per
cent of rows are rejected, or if any single column accounts for more than 0.1 per
cent of rejects, or if the rejects are contiguous in the file (which indicates a
truncation or a format change partway through). Declare the limit *before* looking
at the data, and record it with the result: a threshold chosen after seeing the
defect rate is not a threshold, it is a rationalisation.
