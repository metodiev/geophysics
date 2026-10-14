# Solutions — 22-01-04 Documentation, Docstrings and READMEs That Work

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [04 Documentation, Docstrings and READMEs That Work](../04-documentation.md).

---

## ★1 — Coverage, stale and accurate at release 8

Total functions $n = 152$.

- documented: $0.645 \times 152 = 98.0$ (the simulation has 98 of 152);
- stale: $0.211 \times 152 = 32.1$ (the simulation printed 32.0);
- accurate: $98.0 - 32.1 = 65.9$, i.e. $65.9/152 = 43.4\ \%$.

The demonstration's "accurate %" column is coverage minus stale as fractions of
the same total: $64.5 - 21.1 = 43.4$. Both routes agree, as they must, because
both are fractions of the same 152 functions.

## ★2 — Docstring with units

```python
def depth_from_pressure(p, rho):
    """Return the depth of a fluid column from its pressure.

    Parameters
    ----------
    p : float
        Pressure difference across the column, in pascals (Pa).
    rho : float
        Fluid density in kilograms per cubic metre (kg/m^3). Must be positive.

    Returns
    -------
    float
        Depth in metres (m), using g = 9.81 m/s^2.

    Raises
    ------
    ZeroDivisionError
        If `rho` is zero.

    Notes
    -----
    Assumes a constant density and constant gravity; a depth from a real
    pressure record needs a density profile and a latitude-dependent g.
    """
    return p / (rho * 9.81)
```

The failure mode stated is the division by a zero density, which is exactly what
the code does; the assumptions paragraph is what a reader needs to decide whether
the function is legitimate for a given dataset.

## ★3 — README order

1. *What this code does* — orientation: the reader deciding whether to invest.
2. *Install* — task: the reader setting up.
3. *Quickstart* — task: the shortest path to a result.
4. *Data provenance* — explanation and reproducibility: the reader checking the
   inputs.
5. *How to cite* — orientation: the reader using the result.
6. *Licence* — orientation: the reader reusing the code.
7. *Known limitations* — explanation: the reader judging how far to trust it.

## ★★4 — The long-run stale ratio

Per release, a fraction $P(1-u)$ of **documented** functions becomes stale and a
fraction $Pu$ of **stale** functions is healed. In equilibrium the two flows
balance, so with $D$ documented and $S$ stale:

$$P(1-u)\,D = P u\,S
\;\Longrightarrow\;
\frac{S}{D} = \frac{1-u}{u}.$$

For $u = 0.55$: $S/D = 0.45/0.55 = 0.818$, matching the printed
"81.8 % of documented functions stale", which at the modelled coverage of 64.5 %
is $0.818 \times 64.5 = 52.8\ \%$ of all functions — also printed.

For $S/D < 0.10$:

$$\frac{1-u}{u} < 0.10
\;\Longrightarrow\;
1 - u < 0.10u
\;\Longrightarrow\;
u > \frac{1}{1.10} = 0.909.$$

So an update rate above **91 %** is needed to keep the long-run stale fraction of
documented functions below 10 %. Note that the change probability $P$ cancels:
the required update rate depends only on the ratio of the two rates, not on how
fast the code changes.

## ★★5 — Recomputing the reader cost

At release 8 there are 32 stale functions. With 12 reader-minutes per consulted
function and a 30 % consultation fraction:

$$32 \times 12\ \text{min} \times 0.30 = 115\ \text{min} \approx 1.9\ \text{h}.$$

Report it as: "under the model's assumptions (12 reader-minutes per consulted
stale function, 30 % of stale docstrings consulted before the error is noticed),
one team pass costs about 1.9 h; the consultation fraction is a chosen value and
is the dominant uncertainty, so the statement to defend is that the cost recurs,
not that it equals 1.9 h." Changing the consultation fraction from 10 % to 30 %
multiplies the estimate by three, which is the honest scale of the uncertainty.

## ★★6 — What `--doctest-modules` catches

**Catches:**

1. **Signature drift** — a renamed or reordered parameter makes the example
   `TypeError`; the documentation is then guaranteed to be wrong.
2. **Changed return shape or dtype** — an example that asserts
   `array([1., 2.])` fails if the function now returns a list, a 2-D array or an
   integer dtype.
3. **Missing import or removed function** — an example that calls a helper which
   no longer exists fails at collection time, so the example cannot silently rot
   into unreachable prose.

**Cannot catch:**

1. **A convention change that the example does not exercise.** If
   `np.diff(data, axis=0) / dt` changes from a forward to a central difference,
   the documented example `strain_rate(np.array([0.0, 2.0, 6.0]), 2.0)` would have
   to be rewritten for the test to fail; with the old example retained the test
   still passes and the documentation is wrong about the scheme.
2. **A wrong-but-consistent unit.** If the docstring says "per second" and the
   code divides by a `dt` given in minutes, an example with
   `dt = 2.0` cannot tell the difference between seconds and minutes — both give
   a number. Only a test with a physical reference does.

## ★★★7 — Measuring real documentation decay

**Population.** Every public function of the package at each released tag, taken
from the API listing (`__all__`, or the docs build's autodoc inventory) so that
only functions a reader can call are counted.

**Operational definition of "stale".** A docstring is stale at release $r$ if the
function's signature or documented example differs from the docstring text: parse
the docstring's parameter list and compare with `inspect.signature`, and execute
every example against the release's test environment. This makes "stale"
mechanical rather than a judgement.

**Ground truth.** Where the mechanical test is silent (a changed convention, a
changed unit), use a **triangulation** protocol: two readers, working from the
docstring alone, write down what they expect the function to compute and in what
unit; disagreements with each other or with the author are examined. The rate of
disagreement is the estimate of convention-level staleness, and it is the only
measure of the failure the mechanical test cannot see.

**Confounders.** (i) *Documentation scope*: a package that documents only public
API looks better than one that documents everything, at the same decay rate, so
the denominator must be stated. (ii) *Function lifetime*: functions that are
rarely touched stay accurate by accident, so decay must be conditioned on the
change rate, not averaged over the package.

**Test of the $(1-u)/u$ prediction.** Record, per release, which documented
functions had a signature change and which of those had a docstring update
(available from the diff), giving $\hat u$ directly. Then check whether
$S/D$ approaches $(1-\hat u)/\hat u$ over a window long enough that the transient
has decayed — the prediction fails if the update probability is itself correlated
with the type of change (for example trivial renames are updated more often than
semantic changes).

## ★★★8 — Testing a changed convention

**Test.** Pin the function's *definition* against an independent implementation
for a case where the schemes differ, not merely against a fixed output:

```python
def test_strain_rate_is_forward_difference():
    x = np.array([0.0, 2.0, 6.0, 12.0])
    # forward difference: (x[i+1] - x[i]) / dt, so the result has n-1 entries
    assert strain_rate(x, dt=2.0).shape == (3,)
    assert np.allclose(strain_rate(x, dt=2.0), [1.0, 2.0, 3.0])
```

A central-difference implementation returns four values, or three values with
different numbers, so the shape or the values change and the test fails. The test
names the convention in its name, which is what makes the failure readable.

**False-positive mode.** The test encodes one convention, so a *deliberate*
migration (the group decides to use central differences everywhere) now fails for
every call site, and the failure must be distinguished from a regression. Keep
the convention in a single named function and update one test, rather than
repeating the pinned values across a suite.

**What it cannot check.** Whether the convention is the *right* one for the
physics — both forward and central differences are legitimate; the test documents
which is used, and the decision record documents why.

## ★★★9 — Two documentation policies

**Long-run stale fraction of the documented set**, using $S/D = (1-u)/u$:

- Policy (A), $u = 0.55$: $S/D = 0.45/0.55 = 0.818$ — 82 % of the documented
  functions are stale in the long run.
- Policy (B), $u = 0.95$: $S/D = 0.05/0.95 = 0.053$ — 5.3 % stale.

Policy (B) is a factor of $0.818/0.053 = 15.5$ better *as a fraction of the
documented set*. That is not yet the answer to the question asked, because the
two policies document different sets: (A) documents, say, $D_A = 98$ functions
and leaves $0.818 \times 98 = 80$ stale; (B) documents a smaller external-API set
$D_B$, of which 5.3 % are stale. (B) produces fewer stale docstrings in total
whenever

$$0.053\,D_B < 0.818\,D_A
\;\Longrightarrow\;
D_B < 15.4\,D_A,$$

so (B) wins for any plausible set unless the external API is more than fifteen
times larger than the whole public API, which cannot happen.

**The measurement that decides it.** Count, in the real project, the number of
public functions that are *used outside their own module* (import graph plus
notebook usage), and the number of public functions in total; then apply both
policies' $\hat u$ measured from the project's own history and compare
$0.818\,D_A$ with $0.053\,D_B$ in absolute counts. The decision needs the
count of stale docstrings, not the ratio, and it needs the project's own update
rates rather than the teaching values.
