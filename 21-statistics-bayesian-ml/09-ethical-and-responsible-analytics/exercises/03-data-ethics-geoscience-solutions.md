# Solutions — 21-09-03 Data Ethics, Indigenous Data Sovereignty and Geoscience

> Read after attempting. Lesson:
> [03 Data Ethics](../03-data-ethics-geoscience.md). Numbers are **SYNTHETIC**,
> printed by
> [`code/data_ethics_geoscience_demo.py`](../code/data_ethics_geoscience_demo.py).

---

## ★1 — Records in singleton cells

| Cell size | Records in singletons | Share of $800$ |
|---|---|---|
| $1$ km | $79$ | $9.88\%$ |
| $2$ km | $11$ | $1.38\%$ |
| $5$ km | $0$ | $0.00\%$ |
| $10$ km | $0$ | $0.00\%$ |

The share falls below $1\%$ between $2$ km and $5$ km; at the $2$ km release
$1.38\%$ of records sit alone in their published cell, and at $5$ km none do.

Note how small the *share* is compared with the *risk*: $9.88\%$ of records at
$1$ km sounds modest, yet it means one record in ten can be placed by anyone holding
an address list. Disclosure risk is not proportional to the share of records
affected — it is a property of the worst case, and a single identified record can
compromise the trust that made the survey possible. That asymmetry between a
population statistic and a per-record harm is why the governance questions of §4 of
the lesson cannot be reduced to this table.

---

## ★2 — Retained fractions under two thresholds

Occupancies and shares: $1$ ($0.05$), $3$ ($0.05$), $7$ ($0.10$), $20$ ($0.20$),
$60$ ($0.30$), $200$ ($0.30$). Suppression removes cells below $k$.

| Occupancy | Share | Records | $k = 5$ retained | $k = 10$ retained |
|---|---|---|---|---|
| $1$ | $0.05$ | $40$ | $0$ | $0$ |
| $3$ | $0.05$ | $40$ | $0$ | $0$ |
| $7$ | $0.10$ | $80$ | $80$ | $0$ |
| $20$ | $0.20$ | $160$ | $160$ | $160$ |
| $60$ | $0.30$ | $240$ | $240$ | $240$ |
| $200$ | $0.30$ | $240$ | $240$ | $240$ |

Take the shares as per-record weights over $800$ records: with $k = 5$ the retained
fraction is $0.10 + 0.20 + 0.30 + 0.30 = 0.90$; with $k = 10$ it is $0.20 + 0.30 +
0.30 = 0.80$. So **$k = 10$ costs ten percentage points of the population** in this
distribution, and the cost is entirely borne by the $7$-record cells — the
intermediate-density ground that is usually the scientifically interesting part
(neither urban nor empty).

The general shape: suppression cost is governed by the mass of occupancy classes
just below the threshold, so raising $k$ usually costs more than the arithmetic
suggests, and the class it removes first is the *transitional* one.

---

## ★3 — The mean occupancy of a suppressed cell

At $1$ km, the total records are $800$ and the retained count under $k = 5$ is
$260$, so the suppressed records are $540$ over $243$ suppressed cells:

$$\bar c_{\text{suppressed}}(k=5) = \frac{540}{243} = 2.22 .$$

Under $k = 10$: $790$ records over $285$ cells,

$$\bar c_{\text{suppressed}}(k=10) = \frac{790}{285} = 2.77 .$$

Neither is $k - 1 = 4$ or $9$, because the *distribution* of small counts matters,
not the threshold: most of the sparse cells contain one or two records (the $79$
singletons contribute $79$ records to $79$ cells, dragging the mean down), and there
are many of them. The threshold removes the *tail* of the occupancy distribution,
and the tail's own mean is far below the threshold.

That is why a suppression rule must be evaluated against the actual occupancy
distribution rather than against a rule of thumb: the same $k$ can cost $4\%$ or
$68\%$ of a region's records depending on how the population is distributed across
cell densities.

---

## ★★4 — Differencing two overlapping releases

**Constructed example.** Suppose a $2$ km cell $A$ contains $4$ records, so it is
suppressed under $k = 5$. Inside $A$ sits one $5$ km cell $B$ that contains $A$ and
two neighbouring $2$ km cells $C$ and $D$ with $6$ and $7$ records, published as a
total of $17$. An adversary who knows (from a cadastral list, a previous survey, or
observation) that $C$ and $D$ together hold $13$ records subtracts:

$$17 - 13 = 4 = \text{the count in } A ,$$

recovering exactly the value the suppression was meant to hide. With a third release
at another resolution, more cells unravel, and the process can continue until the
fine grid is effectively reconstructed.

**The control that prevents it.** Suppression must be applied **consistently across
all releases of the same region and period** — the same cells must be suppressed (or
coarsened) in every published product, so that no total can be differenced to
recover them. In practice this means:

1. maintaining a single suppression list for a data programme, not per release;
2. checking candidate releases against each other (a differencing audit) before
   publication;
3. preferring **coarsening** to suppression, because a coarse release has no
   subtracted remainder to recover — which is why §3 of the lesson found coarsening
   dominates;
4. recording the composition of every release in metadata, so that future releases
   (and future analysts) can perform the same audit.

---

## ★★5 — A release plan for three layers

| Layer | Resolution | Control | Agreement required before release |
|---|---|---|---|
| house locations | none published below the settlement level; coarsened to a grid whose every cell has $\ge k$ households | aggregated release plus controlled access to the fine grid under a stated review | consent for this use; agreement on the fine-grid access process and its records |
| water-quality measurements | published at the station, with the station's coordinates rounded or the station indexed rather than located, if the measurement is tied to a private source | published values with indexed locations; locations under controlled access | agreement on whether the measurement itself may be published, and on the indexing scheme |
| cultural sites | **not published**, at any resolution, unless the data holders decide otherwise | presence in the metadata only if agreed; otherwise withheld or replaced by a generalised extent | the data holders' decision, taken with their own governance process; aggregation is not a substitute |

Three points generalise:

1. **The layers need different treatments.** A single release policy applied to all
   three will either over-protect the water data or expose the sites. Layer-by-layer
   negotiation is the work.
2. **Indexing beats rounding** where the analysis needs the measurements but not the
   coordinates: a station index with a controlled cross-reference gives full
   reproducibility of the analysis without publishing the location.
3. **The cultural-site layer is not a privacy problem.** No $k$ protects it, because
   the sensitive fact is the location itself. The default is non-release, with any
   exception coming from the data holders.

---

## ★★6 — Open release versus controlled access

**The conflict is real and the resolution is not a technical trick.** A journal's
open-data policy serves reproducibility; a community's agreement constrains what may
be published. Neither overrides the other — the agreement was made first, and it
binds.

**Negotiation, in order.**

1. **Ask the data holders what reproducibility requires, in their terms.** Often the
   requirement can be met in ways that do not involve publishing the raw data: a
   published analysis code, a synthetic or perturbed data set with the same
   structure, a described data dictionary, and a **verification** route (a named
   contact who can run an independent analyst's code against the real data and report
   whether the results reproduce).
2. **Offer a tiered release.** Published: metadata, documentation, code, the
   aggregated results, and a synthetic sample. Controlled: the fine-resolution data
   under a stated review and a record of access.
3. **Document it for the reader.** The paper states exactly what is available, to
   whom, and how a reader can obtain access, so that a future analyst can judge what
   could and could not be checked. A paper that says "data are available on request"
   without naming the process is not reproducible even when the data exist.
4. **Record the agreement itself** (insofar as it may be published) as part of the
   methods, so that the constraint is visible as a *decision* rather than as an
   omission.

**The analysis that supports this.** Not a privacy metric but a **reproducibility
gap assessment**: enumerate the claims in the paper, and for each state what would
be needed to verify it (the data, the code, a derived product, or an intermediary).
The output is a table that shows which claims can be verified from the published
material alone and which require the controlled tier — which is what a journal, a
reader and the data holders all need to see.

---

## ★★★7 — An adversary model instead of a singleton count

**Adversary model.** Specify three things: (i) *what the adversary holds* — a
cadastral list, a mobile-phone location history, a previous survey, a
know-your-neighbour knowledge; (ii) *what the adversary knows about the release* —
the aggregation scheme, the suppression rule, and any other release of the same
region; (iii) *what the adversary wants* — the identity of a record, the value of a
sensitive attribute, or the existence of a site.

**Statistics.** Two that go beyond counting:

1. **The differencing residual:** for every suppressed cell, whether the published
   totals of the coarser cells that contain it, minus the published counts of the
   finer cells that do not overlap it, determine its count. Report the share of
   suppressed cells whose value is determined within a stated tolerance.
2. **Attribute disclosure risk:** for each record, the probability that an adversary
   with the stated auxiliary information places it in a group of size $\le g$
   (a distinct-liveness measure) or learns its value class (a prediction-based
   measure).

**The decision it informs.** Not "may we release" but "which of these options do we
present to the data holders": (a) the coarse grid at resolution $R$; (b) the fine
grid under controlled access; (c) a perturbed fine grid; (d) the aggregated results
plus code only. Each option is reported with its measured disclosure risk and its
measured utility loss, so the choice is made with both numbers visible.

**The honest limitation.** Adversary models are constructed, not observed: a release
that resists the modelled adversary may fail against a richer auxiliary data set that
appears later. The metric therefore cannot be a guarantee, only an input — which is
exactly why the release decision belongs with the data holders, who bear the
consequences if it is wrong.

---

## ★★★8 — A co-analysis arrangement

**Decision points.** (i) the research question and the study design; (ii) which data
are collected, by whom and with what consent; (iii) the analysis plan, including
which questions are primary; (iv) the interpretation and framing of the results;
(v) the release decision for every product; (vi) the authorship and credit; (vii) the
arrangements for the data after the project ends.

**Timetable.** Decision points (i)–(ii) precede any fieldwork; (iii) precedes the
analysis; (iv) and (v) precede submission; (vi) is agreed early, not at the end;
(vii) is settled before the project closes, because a data set with no custodian
afterwards is a de facto open release.

**Roles.** A named community representative or body with authority to decide the
release; the researchers; a data custodian for the controlled tier; and a mechanism
for disagreement — which is the part most often omitted. If there is no agreed way
to resolve a dispute, the arrangement is not a governance structure.

**Benefit pathway.** Specific and stated in advance: co-authorship or acknowledged
contribution; training and capacity, named and budgeted; local data infrastructure
(equipment, storage, a maintained repository); employment; or a commitment about how
findings are used. "Capacity building" without a line item is not a pathway.

**Criterion for judging it to have worked.** Not the absence of conflict, and not the
publication. The criteria are: the data holders made the release decisions and would
make the same ones again; the analysis was returned to them before publication and
its framing reflects their corrections; the benefit pathway was delivered on the
stated timetable; and the data set has a custodian and a plan after the project. Each
is checkable by the people concerned, which is what distinguishes an arrangement from
a statement of intent.

---

## ★★★9 — "The $k$-anonymity metric is satisfied at the population level"

**Error 1: the wrong object is being protected.** $k$-anonymity is a property of the
*records* in a release. It says nothing about sites, buildings, graves, species
occurrences or habitats, whose sensitivity lies in their existence and position
rather than in any count of people. An endangered-species location released at any
resolution can be visited; the risk is to the species, not to the anonymity of a
household, and a suppression rule for people does not address it.

**Error 2: the metric's own guarantees are being over-read.** Even for records,
$k$-anonymity protects a single release against an adversary who does not hold
auxiliary information. A species location is exactly the case where the adversary
holds rich auxiliary information — a habitat model, a previous sighting, local
knowledge — and where the *composition* of releases over time (a sequence of survey
reports) recovers what one release withheld.

**The analysis that would replace it.**

1. **Define the sensitivity as the location itself** and treat the coordinates as a
   confidential attribute of the record, not as a harmless index. The relevant
   question becomes "what is the least precise location from which the site could
   still be used for the science?", answered with the data holders and the species
   specialists.
2. **Specify the adversary**: a visitor, a collector, a competitor land user, or an
   agent holding a habitat model; state what each holds and what they would do with a
   given resolution.
3. **Evaluate generalisation options explicitly** — snapping to a coarse grid, a
   random offset within a radius, a bounding region (a watershed, a protected area),
   or withholding the layer — and report, for each, the measured utility loss (does
   the scientific question survive?) and the residual identifiability (can the site
   be found?).
4. **Default to non-release** where the two cannot both be satisfied, with any
   exception coming from the governing body for that site or species. The published
   science can usually proceed with the generalised version plus an access route for
   verified analysts, which is the outcome to work towards rather than a compromise
   to be conceded.
