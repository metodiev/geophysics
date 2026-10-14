# Exercises — 21-09-03 Data Ethics, Indigenous Data Sovereignty and Geoscience

Attempt these before reading the
[solutions](./03-data-ethics-geoscience-solutions.md). The lesson is
[03 Data Ethics](../03-data-ethics-geoscience.md). All numbers are **SYNTHETIC**,
printed by
[`code/data_ethics_geoscience_demo.py`](../code/data_ethics_geoscience_demo.py).

Setup: $800$ records in a $20 \times 20$ km region, clustered around $30$
settlements with a spread of $2.0$ km.

| Cell size | Occupied cells | Mean count | Singleton cells | Records in singleton cells |
|---|---|---|---|---|
| $1$ km | $286$ | $2.80$ | $79$ | $79$ |
| $2$ km | $90$ | $8.89$ | $11$ | $11$ |
| $5$ km | $16$ | $50.00$ | $0$ | $0$ |
| $10$ km | $4$ | $200.00$ | $0$ | $0$ |

| Cell size | $k$ | Cells suppressed | Records suppressed | Records retained |
|---|---|---|---|---|
| $1$ km | $5$ | $243$ | $540$ | $260$ ($32.5\%$) |
| $1$ km | $10$ | $285$ | $790$ | $10$ ($1.2\%$) |
| $2$ km | $5$ | $23$ | $51$ | $749$ ($93.6\%$) |
| $2$ km | $10$ | $52$ | $259$ | $541$ ($67.6\%$) |
| $5$ km | $10$ | $1$ | $8$ | $792$ ($99.0\%$) |
| $10$ km | $5$, $10$ | $0$ | $0$ | $800$ ($100\%$) |

## ★ Foundational

**★1.** Compute the share of records living in singleton cells at each of the four
cell sizes, and state the cell size at which the share falls below $1\%$.

**★2.** Compute the retained fraction of the population for a release whose cells
hold $1, 3, 7, 20, 60$ and $200$ records with occupancy shares $0.05, 0.05, 0.10,
0.20, 0.30, 0.30$, under $k = 5$ suppression. Then repeat for $k = 10$ and state
which threshold is cheaper.

**★3.** From the printed tables, compute the mean count of a *suppressed* cell at
$1$ km with $k = 5$ and with $k = 10$, and state why the mean is not simply
$k - 1$.

## ★★ Applied

**★★4.** Two overlapping releases of the same region are published: one at $2$ km
with $k = 5$ and one at $5$ km with $k = 5$. Explain, with a constructed numerical
example, how differencing them can recover a count that each suppressed, and state
the control that prevents it.

**★★5.** Design the release plan for a data set containing (i) house locations,
(ii) water-quality measurements, (iii) a set of cultural sites. State, for each
layer, the resolution, the control, and the agreement that must exist before the
release.

**★★6.** A journal's data policy requires open release; the community's agreement
requires controlled access. Specify the analysis and the negotiation that resolve
the conflict without either breaching the agreement or abandoning reproducibility.

## ★★★ Research-oriented

**★★★7.** Design a disclosure-risk assessment that models an adversary with
auxiliary information, rather than counting singleton cells. State the adversary
model, the data they hold, the statistic, and the release decision the statistic
informs.

**★★★8.** Design the co-analysis arrangement for a study of a region whose data are
governed by a community. State the decision points, the timetable, the roles, the
benefit pathway, and the criterion by which you would judge the arrangement to have
worked.

**★★★9.** A colleague proposes to publish precise coordinates of endangered-species
sites because "the $k$-anonymity metric is satisfied at the population level".
State the two errors in that argument and the analysis that would replace it.
