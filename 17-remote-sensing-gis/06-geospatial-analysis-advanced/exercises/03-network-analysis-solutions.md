# Solutions — 17-06-03 Network Analysis and Least-Cost Paths

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Network Analysis](../03-network-analysis.md).

---

## ★1 — Two edge costs

The edge weight is the mean friction times the step length:

$$\text{rook} = \frac{1.0 + 3.0}{2} \times 100 = \mathbf{200\ cost\text{-}metres},$$
$$\text{diagonal} = \frac{1.0 + 3.0}{2} \times 100\sqrt2 = 200\sqrt2
= \mathbf{282.84\ cost\text{-}metres}.$$

Note that the averaging convention matters: using the friction of the *departing*
cell only would give 100 and 141.42 respectively for a step leaving the smooth cell,
a factor-of-two difference on this sharp contrast.

---

## ★2 — Mean friction along a path

$$\bar c = \frac{C}{L} = \frac{42\,000}{15\,000} = 2.8.$$

Consistency checks: $2.8$ lies inside the range $[0.5, 4.0]$ ✔, but it is **above**
the areal mean of 2.0, which is a warning. A least-cost path should prefer cheap
ground, so its mean friction should normally be *below* the areal mean — as it was
in the lesson (1.2477 against 1.845, 32 % lower). A path whose mean friction is
40 % *higher* than the surface's areal mean suggests either (i) the endpoints
require crossing expensive ground and no cheap alternative exists, or (ii) the
surface is not what the cost is computed from (for example the slope penalty
dominates, or the wrong raster band was used). The check cannot distinguish these;
it can only flag the anomaly, which is why it is worth reporting `C` and `L`
separately.

---

## ★3 — Sinuosity

$$\text{sinuosity} = \frac{L}{D} = \frac{18}{15} = \mathbf{1.20}.$$

---

## ★4 — Two corridors

$$C_1 = 20\ \mathrm{km} \times 1.0 = 20\,000\ \text{cost-metres},$$
$$C_2 = 22\ \mathrm{km} \times 1.4 = 30\,800\ \text{cost-metres}.$$

The **first corridor is optimal** by 10 800 cost-metres, i.e. 35 % cheaper. The
margin is set by the ratio of frictions and lengths, so a friction error of 10 %
(1.4 → 1.26) still leaves the first corridor optimal; the ranking would reverse
only if the friction contrast were much smaller than 1.0 : 1.4 or the lengths much
closer.

---

## ★5 — Direction dependence

A→B (uphill, mean grade 4 %):

$$\bar m_{A\to B} = 1 + 2(0.04) = 1.08 .$$

B→A (downhill, mean grade 3 %):

$$\bar m_{B\to A} = 1 + 1(0.03) = 1.03 .$$

Since both directions traverse the same ground, the ratio of costs is the ratio of
the multipliers, $\mathbf{1.08/1.03 = 1.049}$, i.e. **A→B costs 4.9 % more than
B→A**. The graph **is directed**: the uphill and downhill multipliers differ, so
the edge weights are asymmetric. Note that if the downhill penalty were 2 as well,
the multipliers would depend on $|g|$ only, the graph would be symmetric, and the
two trips would cost exactly the same — which is the behaviour the lesson measured
at a penalty of 1 even with a slope exponent of 4.

---

## ★6 — Path cost from step counts

$$C = \bar c\left(40 \times 250 + 30 \times 250\sqrt2\right)
= 1.5\left(10\,000 + 10\,606.6\right)
= 1.5 \times 20\,606.6 = \mathbf{30\,910\ cost\text{-}metres}.$$

Path length $= 20\,606.6$ m $= 20.61$ km; mean friction $= 1.5$ by construction.

---

## ★7 — A near-optimal corridor

**Definition.** All cells (or all simple paths) whose accumulated cost from the
source is within 1 % of the optimal cost **and** that lie on some path to the
target. The practical construction is a *bidirectional* search: run Dijkstra from
the source and from the target, then keep every edge $(u, v)$ with

$$d_s(u) + w(u, v) + d_t(v) \le (1 + \epsilon)\,C^{*},
\qquad \epsilon = 0.01,$$

which is the standard definition of a near-shortest-path subgraph and is exact for
the stated tolerance.

**Summary.** Report the corridor as a raster with each cell's *slack*, the
difference between the cheapest route through it and $C^{*}$; report the corridor's
area, the number of distinct route "branches", and the maximum slope and total
ascent of the optimal route. The lesson measured the need for this: a 5.4 % friction
error changed the route by roughly 70 % of its cells while changing its cost by
0.7 %, so any single line is one of many near-equal options.

**Validation.** Two checks: (i) the corridor must contain the optimal route
(trivial if implemented as above, and worth asserting), and (ii) the corridor's
cost-to-slack relationship must be monotone — every cell in the corridor with
slack $s$ must have a route with cost $C^{*} + s$, which a random subset of
corridor cells can be made to confirm by explicit path reconstruction.

---

## ★8 — Separating friction and slope uncertainty

Design a two-factor experiment, holding everything else fixed:

| factor | levels | realisation |
|---|---|---|
| friction values | the stated per-class accuracy (for example ±20 % per class, or a class-specific interval) | perturb the lookup table, not each cell independently, plus an independent per-cell component if within-class variation is claimed |
| slope penalty | the plausible range of the exponent (for example 2 to 6) and of the downhill penalty | recompute the directed graph |

The full design is a small factorial: perturb the friction table (say 100 draws) at
each of the 4 slope exponents, and compute the response surface. Separating the
contributions is then a variance decomposition — for each output quantity, the
fraction of its variance attributable to the friction factor, to the exponent
factor, and to their interaction. The interaction term is the interesting one: a
steeper penalty makes the route more dependent on the DEM and therefore amplifies
the friction uncertainty's effect on the route's *geometry*.

**Reported quantity.** Not a single route, but per output: (i) the cost of the
optimum as a median with a 5–95 % interval; (ii) the fraction of the optimal route's
cells that appear in at least 80 % of realisations ("always-used" cells) — a
frequency map that is the honest geometric product; (iii) the variance
decomposition table, which tells the reader which uncertainty to reduce first. The
lesson's measurements are the one-factor version of this: 0.7 % on cost and a
Jaccard of 0.28 on geometry for the friction factor alone.
