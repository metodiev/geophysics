# Solutions — 22-01-01 Designing Software for Scientific Research

> Read after attempting. Numbers are computed here and, where they come from the
> demonstration, equal its printed output. Lesson:
> [01 Designing Software for Scientific Research](../01-software-design-science.md).

---

## ★1 — Graph density and degree means

(a) Possible ordered pairs of distinct modules: $60 \times 59 = 3540$. The
demonstration builds edges only in one direction (an acyclic graph), so the
possible edges are the upper triangle, $3540/2 = 1770$. Density:

$$d = \frac{101}{1770} = 0.0571 = 5.7\ \%.$$

(b) Mean fan-out from the edge count: $101/60 = 1.683$ edges per module. The
demonstration's per-module mean is $1.68$. Agreement to the printed precision.

(c) Every edge contributes exactly one unit to exactly one module's fan-out and
one unit to exactly one module's fan-in. The two sums are therefore the same
number, $101$, so the two means are equal at $1.68$ — on any graph.

## ★2 — Instability

$$I_A = \frac{2}{8+2} = 0.20, \qquad
I_B = \frac{5}{0+5} = 1.00, \qquad
I_C = \frac{0}{0+0} \;\text{(undefined; report as } 0\text{)}.$$

Module **B** changes most often. It is depended on by nothing, so no other module
constrains it, and it depends on five modules, so upstream changes reach it
freely. A is the opposite: eight modules depend on it, so its interface is a
contract. C is isolated and is not a coupling risk, though it may be dead code.

## ★3 — Blast radius on a small DAG

Reachability (`x` can be reached from `y` if a directed path $y \to \dots \to x$
exists):

- $A$: reached from $D$ only → blast radius **1**.
- $B$: reached from $A$ and $D$ → blast radius **2**.
- $C$: reached from $A$, $B$ and $D$ → blast radius **3**.

$C$ is the worst single point of change in the sense that only one module
depends on it directly ($B$), yet three modules depend on it transitively. This
is the mechanism behind the demonstration's $4.72/1.68 = 2.80\times$
amplification.

## ★★4 — Density of a single coupled module

$$\text{decisions} = 1 + 2 + 8 = 11, \qquad
\text{density} = 0.50 + 0.30 \times 11 = 3.80\ \text{defects per KLOC}.$$

That is above both the package mean ($1.81$ per KLOC) and the mean over
high-blast modules ($2.45$ per KLOC). The reason is that the group mean averages
many modules with fan-in and fan-out near 1, where
$0.50 + 0.30 \times 3 = 1.40$ per KLOC, with a few hubs. A single module can be
an outlier while its group mean stays modest; the demonstration's maximum
fan-in is 8, so a module at the maximum sits at the top of the distribution, not
at its centre.

## ★★5 — Separating computation from surroundings

Pure core — no files, no plotting, no clock:

```python
def strain_rate(data, dt):
    """Return d(data)/dt along axis 0, in data units per second."""
    return np.diff(data, axis=0) / dt
```

Boundary — the only place that touches the outside world:

```python
def run(cfg):
    data = np.loadtxt(cfg["path"])
    rate = strain_rate(data, cfg["dt"])
    plt.plot(rate)
    plt.savefig(cfg["fig"])
    return rate.mean()
```

The one place for each side effect is `run`: file reading (`np.loadtxt`), figure
writing (`savefig`) and reporting (the returned scalar). The test the original
could not pass, and the rewrite can, is:

```python
def test_strain_rate_units():
    x = np.array([[0.0, 0.0], [2.0, 4.0]])
    assert np.allclose(strain_rate(x, dt=2.0), [[1.0, 2.0]])
```

It asserts a **unit** result (data units per second) on an input constructed in
the test, with no file, no `plt` global state and no figure. The original could
only be tested by writing a file and running a plotting backend.

## ★★6 — Amplification

(a) $4.72/1.68 = 2.810 \approx 2.80\times$, matching the demonstration.

(b) In a path $m_1 \to m_2 \to \dots \to m_n$, the root $m_1$ has direct reach 1
and transitive reach $n-1$, so the amplification is $n-1$: it grows **linearly**
with the length of the chain, without bound.

(c) The measured $2.80\times$ is far below a chain value because the synthetic
graph is a random DAG, not a path. Edges are spread over many modules
(5.7 % of the possible pairs), most modules have fan-out 0 or 1, and the mean
number of modules reachable from a node in a sparse random DAG with mean degree
$\lambda = 1.68$ is small. The graph has a density of only $5.7\ \%$; a random
graph with mean degree $\lambda < 1$ would
have a finite mean component size; at $\lambda = 1.68$ a giant component exists
for undirected graphs but the **directed acyclic** structure, with edges only
from lower to higher index, strongly limits reach.

## ★★★7 — Measuring hidden filesystem coupling

**Data.** The shell/Python call graph: for every script, the literal filenames it
opens for writing and for reading (`open`, `np.loadtxt`, `np.save`, `to_csv`,
`xarray.to_netcdf`), extracted by static parse plus a run-time audit hook that
records `open()` calls during a test execution.

**Proxy for an edge.** Script $u \to$ script $v$ if $v$ **writes** a path that $u$
**reads** in the same workflow run, with the edge weighted by the number of
shared paths. Inferred (static) edges are kept separate from observed (audit)
edges so that dynamically constructed filenames are visible as a discrepancy.

**Metric.** Report the ratio of observed edges to import-graph edges, and the
blast radius distribution recomputed on the union graph, as a fraction of package
size so it can be compared across packages.

**Two ways it can be wrong.** (i) *False edges* from scratch files: a temporary
file written and read by the same script appears as coupling to itself or to a
neighbour, inflating the count. (ii) *Missing edges* from dynamic paths, where a
filename is built at run time from a configuration value, so static parsing sees
nothing and the audit hook only sees it on the branch that executed.

## ★★★8 — Splitting the hub

Split the hub $H$ (fan-in 8, fan-out 2) into $H_c$ (the computation) and $H_a$
(the adapters that the eight dependents actually use). Move as many dependents as
possible to $H_c$: suppose 6 of the 8 depend on the computation, giving
$H_c$ fan-in 6, and the remaining 2 depend on the adapter, giving $H_a$ fan-in 2.

**Prediction.** Blast radius is monotone in the fan-in of the node being changed.
Because the largest fan-in falls from 8 to 6, the maximum single-change radius
falls as well; with the demonstration's measured correlation of $0.831$ between
fan-in and blast radius, a 25 % reduction in fan-in predicts a reduction of
roughly $0.25 \times 0.831 \approx 21\%$ in the group-mean radius, which is
$4.72 \times 0.79 \approx 3.7$ modules.

**Assumption.** The prediction rests on **interchangeability of the change
targets** — that the module which changes is drawn from the same distribution
before and after the split, and that the new adapter does not itself become the
hub. It also assumes the fan-in/blast-radius relation is linear over this range,
which a two-point correlation does not establish.

**Falsification measurement.** Locate the actual hub, split it in a branch,
recompute the transitive closure of the import graph and compare the measured
maximum and mean blast radius with the prediction. If the radius does not fall,
the cause is a second hub (the largest radius was never the split module) or the
adapters' own coupling.

## ★★★9 — Making the defect model falsifiable

1. **Churn interaction.** Replace the additive term with
   density $= a + b\,C + c\,\log(1 + \text{churn}) + d\,C\log(1+\text{churn})$,
   where $C$ is the decision count and churn is the number of lines changed per
   year from version-control history. *Observable that distinguishes it:* in the
   additive model the defect density of a high-coupling module is **independent**
   of its churn; in the interaction model it **rises** with churn. Fit both and
   compare the coefficient on the interaction term against its standard error.

2. **Saturating coupling.** Replace the linear term with
   $b\,(1 - e^{-C/C_0})$, so that beyond a scale $C_0$ extra coupling adds little.
   *Observable:* the additive model's density is linear in fan-in and extrapolates
   to arbitrarily high values; the saturating model predicts a **concave**
   density-versus-fan-in curve, testable by binning modules by fan-in and fitting
   a monotone concave function to the binned means.

**What neither model can tell you.** Neither is about correctness of a specific
module: the density is an expected defect count over a population of similar
modules, so it cannot say that *this* function is right or wrong, nor locate the
defect. Structure predicts where to look and what a change will cost; verification
establishes whether the number is correct, and it needs a test with a known
answer, not a metric.
