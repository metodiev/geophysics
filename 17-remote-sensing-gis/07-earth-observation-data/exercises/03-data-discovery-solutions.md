# Solutions — 17-07-03 Data Discovery, Access and Licensing

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [03 Data Discovery, Access and Licensing](../03-data-discovery.md).

---

## ★1 — Precision, recall, $F_1$

$$
P = \frac{13}{13+4} = \frac{13}{17} = 0.765, \qquad
R = \frac{13}{13+3} = \frac{13}{16} = 0.812,
$$
$$
F_1 = \frac{2 \times 0.765 \times 0.812}{0.765 + 0.812} = \frac{1.242}{1.577} = 0.788.
$$

---

## ★2 — Overlap predicate

$$
\text{overlap}(\mathbf{a}, \mathbf{b}) =
x_0^{a} \le x_1^{b} \;\wedge\; x_0^{b} \le x_1^{a} \;\wedge\;
y_0^{a} \le y_1^{b} \;\wedge\; y_0^{b} \le y_1^{a}.
$$

The first two conditions state that the $x$-intervals are not disjoint; the
second two that the $y$-intervals are not disjoint. Both must hold for the boxes
to share any area. Touching boxes are counted as overlapping.

---

## ★3 — Does the box intersect the ROI?

(i) $(55, 58, 70, 72)$: $55 \le 60$ and $40 \le 70$ (x overlap); $58 \le 60$ and
$40 \le 72$ (y overlap). **Yes.**

(ii) $(70, 70, 80, 80)$: $70 \le 60$ is false. **No.**

---

## ★4 — A second confusion table

$$
P = \frac{32}{50} = 0.640, \qquad
R = \frac{32}{40} = 0.800, \qquad
F_1 = \frac{2 \times 0.640 \times 0.800}{0.640 + 0.800}
= \frac{1.024}{1.440} = 0.711.
$$

---

## ★5 — Why both fall together

Position error shifts each reported footprint by a random amount, so some
records move *into* the ROI that are not there (false positives) and some move
*out* that are (false negatives). Since the shifts are independent of relevance,
both error types grow, and precision and recall fall together. A stricter query
*threshold* is different: it removes candidate records on a criterion, which
tends to cut false positives at the cost of some true positives — a deliberate
trade of precision for recall. Position error is not a trade; it is a loss of
information, so both metrics degrade.

---

## ★6 — Licence filtering

Four records are free to view but not to redistribute
($14 - 10 = 4$), so a mosaic project loses those four. It must filter on the
**redistribution** permission, not on access — being able to download a scene is
not permission to publish a mosaic built from it.

---

## ★7 — Metadata-completeness audit (specification)

- **Fields.** Footprint geometry, start/end time, licence, processing level,
  resolution, and a stable identifier plus version.
- **Metrics (rates, not counts).** Fraction of records with each field present
  and non-null; fraction with geometry that parses and has positive area;
  fraction with an identifier that is unique in the catalogue.
- **Thresholds.** For example, fail the audit if any field is missing on more
  than $1\%$ of records, or if identifiers are non-unique.
- **Decision.** Whether the catalogue is fit as a *filter*: a field that is
  missing cannot be queried, so its absence caps the attainable recall
  regardless of query design. The audit decides whether discovery can be trusted
  or must be supplemented by a manual check.

---

## ★8 — Systematic versus random metadata error

**Mechanism.** Random error displaces records symmetrically, so some errors fall
inside the ROI and some outside; with a large enough ROI the two partly cancel
and the *bias* is near zero, though precision and recall still fall. A
**systematic** shift (a datum mismatch, a swapped axis, a constant offset) moves
every record the same way: near one edge of the ROI every affected record is
pushed the *same* direction, so the errors do not cancel and the false
positives and negatives become spatially *structured* — clusterable, and
correlated with location.

**Experiment.** In the synthetic catalogue, add a constant $+3\ \mathrm{km}$
shift to every reported centre (same magnitude as the random $\sigma = 4\
\mathrm{km}$), then recompute precision and recall. If the systematic version
produces a *similar* quality number but a *spatially clustered* set of errors,
the point is made: the aggregate metric hides a structural failure that a
per-region breakdown would expose. The proper check is to map the residuals, not
only to summarise them.
