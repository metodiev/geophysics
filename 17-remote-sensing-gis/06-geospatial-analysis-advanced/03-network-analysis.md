---
id: 17-06-03
title: "Network Analysis and Least-Cost Paths"
level: advanced
prereqs: ["17-05-03", "17-05-04", "03-03-06"]
tags: [gis, geospatial, remote-sensing, geospatial-analysis-advanced, network-analysis, least-cost-path, cost-surface, graph]
---

# Network Analysis and Least-Cost Paths

A cost surface is not a network. Between the raster and the route lie four
decisions that the data cannot make: the connectivity rule that turns cells into
a graph, the way friction is combined along an edge, the treatment of slope
asymmetry, and the definition of "least". This lesson builds those decisions
explicitly, verifies the shortest-path computation against an independent
implementation, and then measures the thing that a published route usually
hides: the optimum is often degenerate, so the *cost* of the best route is stable
while the *line* is not.

All models and data in this module are **SYNTHETIC**. The friction surface, the
terrain, the network and every number below are generated in memory from a fixed
seed. No real road, trail, corridor or place is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a friction raster into a graph and **state** how the connectivity
   rule changes both the graph and the route.
2. **Compute** a least-cost path with two independent implementations and
   **state** what their agreement does and does not establish.
3. **Derive** the cost of a path as a sum of edge costs, and **define** sinuosity
   and the detour factor.
4. **Explain** why a slope-dependent cost makes the graph directed, and
   **demonstrate** when a symmetric graph cannot represent direction dependence
   at all.
5. **Compute** a cost-distance surface and **test** whether it is convex.
6. **Measure** the sensitivity of a route to friction error and **explain** why
   the cost is stable while the geometry is not.
7. **Explain** how an exponent in a slope-penalty function becomes the answer,
   and **state** what would be needed to choose it from data.
8. **Compute** betweenness centrality on a synthetic vector network and **state**
   what it does not measure.

## Prerequisites

- [03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md) —
  the grid, the cell size and the affine transform.
- [04 Map Algebra and Raster Analysis](../05-gis-fundamentals/04-map-algebra.md) —
  focal derivatives, used for the slope penalty.
- [03-03-06 Sparse Matrices](../../03-scientific-computing/03-scipy/06-sparse.md) —
  the adjacency representation and the graph algorithms used here.

## 1. From a friction raster to a graph

A raster of resistance per unit distance, $c(i,j)$, becomes a graph when a
connectivity rule is chosen. Two standard rules and their effect on a synthetic
80 × 120 grid of 250 m cells:

| rule | nodes | directed edges | mean degree |
|---|---|---|---|
| rook (4-neighbour) | 9 600 | 38 000 | 3.96 |
| queen (8-neighbour) | 9 600 | 75 604 | 7.88 |

The synthetic cost surface has a friction from 0.278 to 3.974 (mean 1.845,
median 1.660) and two low-cost corridors. Each edge weight is

$$
w_{u \to v} = \bar c \;\; d_{uv},
\qquad
\bar c = \tfrac12\left(c_u + c_v\right),
\qquad
d_{uv} \in \{\Delta,\ \Delta\sqrt 2\},
$$

so the path cost is measured in **cost-metres** — a length in metres multiplied
by a dimensionless friction. Three consequences:

* **The connectivity rule changes the graph and therefore the route.** Rook and
  queen differ not only in edge count but in the *set of admissible directions*,
  and on a corridor surface that is enough to change the optimum.
* **The averaging convention matters at fine scales.** Using $\bar c$ (the mean of
  the two cells) differs from using $c_u$ (the friction of the cell being left)
  by up to a factor of the local contrast, and every least-cost tool documents
  which one it uses because the two give different paths on sharp boundaries.
* **Cost-metres are not metres.** A path cost divided by its length gives the
  *mean friction along the path*, which is the only quantity on this list that is
  comparable between different study areas.

## 2. Least-cost path, computed twice

The demonstration runs Dijkstra's algorithm twice: once with
`scipy.sparse.csgraph.dijkstra` and once as a hand-written heap-based
implementation.

| quantity | value |
|---|---|
| source (row, col) | (20, 10) |
| target (row, col) | (60, 110) |
| cost by `scipy` | 33 594.512932 cost-metres |
| cost by hand-written Dijkstra | 33 594.512932 cost-metres |
| agreement | 0.000 × 10⁰ relative |
| straight-line distance | 26.9258 km |
| mean friction along the path (cost / length) | 1.2477 |

Exact agreement between two implementations of the same algorithm is not a proof
of correctness: they share the graph construction, so an error in the edge
weights, the cell size or the connectivity rule would be invisible here. What it
*does* establish is that the shortest-path logic — the priority queue, the
relaxation and the reconstruction of the path — is sound, which is where such
errors normally live. The complementary check is physical: the mean friction
along the path, 1.2477, must lie between the minimum (0.278) and the maximum
(3.974) friction on the surface and be *below* the areal mean (1.845), because a
least-cost path should prefer cheap ground. It is, by 32 %.

## 3. Sinuosity and the detour factor

| quantity | value |
|---|---|
| path nodes | 105 |
| path length | 30.1421 km |
| straight-line distance | 26.9258 km |
| sinuosity $L/D$ | 1.1195 |
| $C/L$ (mean friction) | 1.1145 |

Sinuosity is the geometric price of avoiding expensive ground; $C/L$ is the
friction remaining on the cheap route. Both are **joint properties of the surface
and the endpoints**: the same landscape gives a different sinuosity for every
pair of endpoints, so a sinuosity value is not transferable and a published
"least-cost corridor" must state its endpoints as well as its surface.

## 4. Anisotropy: cost that depends on direction

A slope-dependent cost makes the graph **directed**: the multiplier for going
uphill need not equal the one for going downhill. On a synthetic terrain with
grades from 0.20 % to 15.19 %, with multiplier
$1 + e\,|\text{grade}|$ uphill and $1 + e\,\rho\,|\text{grade}|$ downhill
($\rho$ the downhill penalty):

| exponent $e$ | penalty $\rho$ | cost A→B | cost B→A | asymmetry |
|---|---|---|---|---|
| 0.0 | 1.0 | 116.569 | 116.569 | 0.000 % |
| 2.0 | 0.5 | 124.571 | 120.586 | 3.199 % |
| 4.0 | 0.5 | 132.573 | 124.603 | 6.012 % |
| 4.0 | 1.0 | 132.595 | 132.595 | 0.000 % |

Three of the four rows are the lesson:

$$
\rho = 1 \;\Longrightarrow\; \text{multiplier depends on } |\text{grade}| \text{ only}
\;\Longrightarrow\; \text{symmetric graph, no asymmetry, even at } e = 4.
$$

Asymmetry appears **only** when the uphill and downhill multipliers differ, and
then grows with the exponent. So a tool that builds a symmetric graph is not
modelling direction-dependent cost at all, however steep the terrain it is given
— a fact that is invisible from the output unless the two directions are computed
separately.

## 5. Cost-distance surfaces are not buffers

The set of all least-cost paths from one source is a **cost-distance surface**,
and its level sets are travel-cost isochrones. Measured on the synthetic surface
(budgets expressed in multiples of the cost-free straight-line distance):

| budget | cells reachable | area |
|---|---|---|
| 0.80 | 4 418 | 276.12 km² |
| 1.00 | 6 360 | 397.50 km² |
| 1.20 | 8 016 | 501.00 km² |
| 1.50 | 9 299 | 581.19 km² |

A reachability region from a least-cost surface is not a disc, and it is **not
convex** either: of 4 000 random pairs of cells reachable within the 1.20 budget,
8 (0.20 %) have a straight-line midpoint that is *not* reachable within the same
budget. The fraction is small here because the surface is smooth; the existence
of such pairs is the point. Two places are each within the budget while the
ground between them is not, which is exactly what makes routing different from
buffering, and why a buffer around a facility is not a service area.

## 6. Sensitivity: the cost is stable, the line is not

Twelve independent noise realisations of the same friction surface, with
additive Gaussian noise of $\sigma = 0.1$ cost units (5.4 % of the mean friction
of 1.845):

| surface | cost of the route (mean, sd) | Jaccard overlap of the path with the reference |
|---|---|---|
| two-corridor surface | 33 604.098, 244.230 (0.73 % of the mean) | mean 0.2806, min 0.1042 |
| low-contrast surface | 28 137.097, 175.722 (0.62 % of the mean) | mean 0.1670, min 0.0466 |

Read the two columns together. The **cost** of the optimum barely moves — well
under one per cent — while the **route** shares only about a quarter of its
cells with the reference, and only about a sixth on the low-contrast surface
where two corridors cost nearly the same. The optimum is therefore
**geometrically degenerate**: many different lines have nearly the same cost.

This is the honest result that a single published line hides. Where two routes
are within the cost error of each other, the ranking between them is
unresolvable, and the defensible products are

* the cost surface itself (a raster), or
* a **corridor** of near-equal paths — for example all paths within 1 % of the
  optimum cost — rather than one line.

## 7. One landscape, five assumed trade-offs

The slope-penalty exponent is not measured by the path; the path is what the
exponent implies. On a synthetic terrain consisting of a 500 m ridge with a pass
(the grade range reaches 31.72 %), with a fixed downhill penalty of 0.5:

| exponent | cost | max grade on the path | total ascent | Jaccard vs exponent-0 route |
|---|---|---|---|---|
| 0.0 | 116.569 | 31.69 % | 839.16 m | 1.0000 |
| 2.0 | 120.099 | 6.45 % | 427.54 m | 0.1285 |
| 4.0 | 123.630 | 8.88 % | 427.54 m | 0.0688 |
| 8.0 | 130.691 | 6.84 % | 427.54 m | 0.1676 |
| 16.0 | 144.813 | 6.45 % | 427.54 m | 0.0151 |

Every route here has the same 101 nodes and the same 29.142 km length, because
all of them are monotone from source to target with the same 40 diagonal steps:
**the exponent does not change the length, it changes where the steep steps are
taken.** Adding any slope penalty at all drops the maximum grade from 31.7 % to
about 6.5 % and the total ascent from 839 m to 428 m, and the route moves to the
synthetic pass. The small non-monotonicity of the maximum grade (8.88 % at
exponent 4) is the optimum trading a shorter route against a steeper one, and it
is a reminder that these are not smooth functions of the parameter.

Five distinct routes come out of five assumed trade-offs on one landscape. To
choose an exponent from data requires independent travel observations — measured
times, effort or cost — and without them a "least-cost corridor" is a restatement
of the assumption with a number attached.

## 8. Centrality on a synthetic vector network

A raster cost path and a road network are different objects, and mixing them is
the second commonest error in this area. On a synthetic 20 × 8 junction network
with 25 % of the links removed:

| quantity | value |
|---|---|
| nodes | 160 |
| links | 218 (436 directed) |
| connected components | 2 |
| degree | min 0, mean 2.725, max 4 |
| top-5 betweenness centralities | (7,2) 3704.02; (8,2) 3608.76; (9,2) 3553.08; (6,2) 3154.10; (13,4) 3012.59 |

$$
C_B(v) = \sum_{s \ne v \ne t} \frac{\sigma_{st}(v)}{\sigma_{st}},
$$

the fraction of shortest paths between all pairs that pass through $v$, computed
by Brandes' algorithm in $O(nm)$. Three caveats:

1. **Centrality is a statement about the graph, not about traffic.** A node is
   central because of its position in the network; whether vehicles use it
   depends on demand, capacity and congestion.
2. **It is defined only within a connected component.** With 2 components here,
   paths between components do not exist and contribute nothing, which
   mathematically deflates the centrality of every node in a small component.
3. **A high value has two explanations.** A node can be a genuine hub or the only
   bridge across a gap created by the link-removal rule. The metric cannot
   distinguish them; the network's construction has to be reported with the map.

And a fourth, structural caveat that applies to the whole lesson: **a road
distance and a raster cost distance are not comparable quantities.** One is
measured along a surveyed alignment with a legal speed limit; the other is an
integral of a modelled friction over a grid. Reporting the difference between
them as a "detour" compares a measurement with a model.

## 9. Worked example: costing a synthetic alignment

A synthetic 12 km route crosses a friction surface whose cell values along the
alignment average 1.6, with one 900 m segment at friction 3.0.

1. **Cost of the cheap part.** $(12\,000 - 900)\ \mathrm m \times 1.6
   = 17\,760$ cost-metres.
2. **Cost of the expensive part.** $900 \times 3.0 = 2\,700$ cost-metres.
3. **Total.** $20\,460$ cost-metres, mean friction $20\,460/12\,000 = 1.705$.
4. **Alternative.** A 13.5 km alignment averaging 1.45: $13\,500 \times 1.45
   = 19\,575$ cost-metres — cheaper despite being 12.5 % longer, which is the
   entire content of least-cost routing.
5. **Statement.** "13.5 km at a mean friction of 1.45 (19 575 cost-metres) versus
   12.0 km at 1.705 (20 460 cost-metres), from a friction surface with cells of
   250 m and rook connectivity, slope penalty exponent 2." Every element of that
   sentence is needed: with a different exponent the ranking of the two
   alignments can reverse.

## Assumptions and regime of validity

1. **Friction is additive and path-independent.** Cost accumulates along the
   path and does not depend on what has been traversed before. That rules out
   fuel, fatigue and cumulative-impact models, which need a state variable.
2. **Friction is isotropic unless the graph is directed.** A symmetric graph
   cannot represent uphill/downhill asymmetry (§4).
3. **The connectivity rule is a model of movement.** Rook restricts motion to
   four directions, so it quantises every bearing to a multiple of 90°; queen
   allows 45° steps. Neither is a continuum, and both bias path length.
4. **Cost is time-like, not distance-like.** $C/L$ is a mean friction, and a
   published $C$ must state its units.
5. **The source and target are cells, not places.** Moving the endpoint by one
   cell can change the optimum and the cost.
6. **Centrality assumes unweighted or correctly weighted shortest paths**, and its
   interpretation is confined to each connected component.
7. **The DEM or friction field is accurate.** §6 measures the consequence: the
   cost is robust and the route is not.

## Python demonstration

[`code/network_analysis_demo.py`](code/network_analysis_demo.py) builds every
object above in memory. It:

1. builds a synthetic friction surface and shows the rook and queen graphs;
2. computes a least-cost path with `scipy` and with a hand-written Dijkstra and
   reports their agreement;
3. measures path length, sinuosity and the mean friction along the path;
4. computes directed costs under four anisotropy settings and reports the
   symmetry behaviour;
5. builds a cost-distance surface, reports reachability at four budgets and tests
   convexity by sampling pairs whose midpoint is unreachable;
6. re-runs 12 noise realisations on two surfaces and reports the stability of the
   cost and of the geometry;
7. fits the trade-off between length and steepness at five anisotropy exponents
   on a ridge-and-pass terrain;
8. builds a synthetic 160-node vector network and computes degrees, components
   and Brandes betweenness.

```bash
cd 17-remote-sensing-gis/06-geospatial-analysis-advanced/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python network_analysis_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/03-network-analysis-exercises.md`](exercises/03-network-analysis-exercises.md)
and the
[solutions](exercises/03-network-analysis-solutions.md):

- **★** Compute a path cost by hand on a stated 3 × 3 friction block.
- **★★** Derive how the cost-distance region differs from a Euclidean buffer on
  a stated two-corridor surface.
- **★★★** Design a corridor product for a stated pair of endpoints and specify
  the tolerance that defines it.

## Mastery checkpoint

Without notes:

> A synthetic friction surface has cells of 100 m, friction between 0.5 and 4.0,
> and a mean of 2.0. **(a)** State the edge cost of a diagonal step between two
> cells of friction 1.0 and 3.0 cost units, in cost-metres. **(b)** A least-cost
> path costs 42 000 cost-metres over 15 km. Compute the mean friction and say
> whether it is consistent with the surface's range and mean. **(c)** With a
> slope penalty that differs between uphill and downhill, state what happens to
> the graph and give the measurement that demonstrates it. **(d)** The friction
> field has a 5 % error and the cost of the optimum changes by 0.6 % while the
> route changes by 70 %. Explain both numbers and state what you would publish.

A worked version of (a)–(c) is in the
[solutions](exercises/03-network-analysis-solutions.md).

## Common pitfalls

1. **Treating a cost surface as a network without stating the connectivity.**
2. **Using a symmetric graph for direction-dependent cost.** The asymmetry
   silently disappears.
3. **Reporting a least-cost line as the route.** The optimum is often degenerate;
   report the corridor or the cost surface.
4. **Confusing cost-metres with metres.** A path cost is not a length.
5. **Comparing a raster cost distance with a surveyed road distance.**
6. **Choosing a slope-penalty exponent from the path it produces.** The path is
   the consequence, not the evidence.
7. **Reading centrality as traffic.** It is graph position, not demand.
8. **Buffering instead of computing a service area.** Reachability is not convex.

## Related modules

- [01 Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation](01-terrain-analysis.md) —
  the slope field a movement cost usually depends on.
- [02 Hydrological and Watershed Analysis in GIS](02-hydrological-gis.md) — the
  same graph machinery with water as the moving quantity.
- [06-geospatial-analysis-advanced README](README.md).
- [18-04 Nonlinear Inversion](../../18-inverse-problems/04-nonlinear-inversion/README.md) —
  optimisation on a cost function, of which a least-cost path is a discrete case.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  scaling shortest-path search over large graphs.

## Self-assessment checklist

- [ ] I can convert a friction raster into a graph and state the rule.
- [ ] I can compute a path cost, a sinuosity and a mean friction.
- [ ] I can explain when a graph must be directed.
- [ ] I can test whether a cost-distance region is convex.
- [ ] I can measure the stability of a route under friction error.
- [ ] I can explain why the path is not evidence for the cost model.
- [ ] I can compute betweenness and state what it does not measure.

