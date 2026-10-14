# Exercises — 17-06-03 Network Analysis and Least-Cost Paths

Attempt these before reading the
[solutions](./03-network-analysis-solutions.md). The lesson is
[03 Network Analysis](../03-network-analysis.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Two adjacent cells of a 100 m grid have friction 1.0 and 3.0. Compute the
edge cost in cost-metres for a rook step and for a diagonal step.

**★2.** A least-cost path costs 42 000 cost-metres and its length is 15 km. Compute
the mean friction along the path and state whether it is consistent with a friction
surface whose range is [0.5, 4.0] and whose areal mean is 2.0.

**★3.** A path has a length of 18 km and its endpoints are 15 km apart. Compute the
sinuosity.

## ★★ Applied

**★★4.** On a synthetic surface with two corridors of friction 1.0 and 1.4, the
first corridor is 20 km long and the second 22 km. Compute the cost of each route
and state which is optimal and by what margin.

**★★5.** A slope penalty gives multipliers of $1 + 2|g|$ uphill and $1 + |g|$
downhill. State the ratio of A→B to B→A cost for a path whose mean uphill grade is
4 % and whose mean downhill grade is 3 %, and state whether the graph is directed.

**★★6.** A friction surface has cells of 250 m and a path crosses 40 rook steps and
30 diagonal steps with a mean friction of 1.5. Compute the path cost.

## ★★★ Research-oriented

**★★★7.** Design a corridor product for a stated pair of endpoints that reports
every route within 1 % of the optimum, and specify how you would compute, summarise
and validate it.

**★★★8.** A friction surface is derived from a land-cover map with 20 classes and a
DEM with 2 m vertical error. Design the sensitivity study that separates the
uncertainty contributed by the friction values from that contributed by the slope
penalty, and state the reported quantity.
