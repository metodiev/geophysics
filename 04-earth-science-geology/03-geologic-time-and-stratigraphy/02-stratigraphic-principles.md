---
id: 04-03-02
title: "Stratigraphic Principles and Relative Dating"
level: beginner
prereqs: ["04-03-01"]
estimated_minutes: 75
tags: [stratigraphy, superposition, cross-cutting, biostratigraphy, correlation]
---

# Stratigraphic Principles and Relative Dating

Relative dating is a deductive system, and it is worth saying plainly what kind
of system it is. The field observations are premises; the principles are rules of
inference; the geological history is the conclusion. This structure has two
consequences that are easy to miss. First, **the observations are the
authority**: if the conclusion contradicts an observation, the observation wins
and the conclusion is wrong. Second, **a set of observations can be
inconsistent**. When it is, there is no history to be found and the honest output
is a statement that the data contradict each other — not the ordering that
quietly ignores the awkward outcrop.

That second case is the one this lesson is built around, because it is where
students (and experienced geologists under time pressure) most often produce a
confident wrong answer: they find *an* order consistent with most of the
relations and report it.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the principles of superposition, original horizontality, lateral
   continuity, cross-cutting relations, inclusions and faunal succession, and
   identify which one each field observation is an instance of.
2. **Represent** a set of field relations as a set of pairwise ordering
   constraints and solve for the orders consistent with all of them.
3. **Detect** an inconsistent set of relations and explain why the correct output
   is "no consistent history" rather than a preferred order.
4. **Bracket** the age of a fault or intrusion between the youngest unit it cuts
   and the oldest unit that oversteps it, and state how sharp the bracket is.
5. **Correlate** two or more sections of first-appearance datums and quantify the
   number of sequence violations rather than asserting a correlation.
6. **Identify** a reworked fossil from its effect on a correlation, using a
   leave-one-out test rather than a prior belief about the taxon.
7. **Explain** why relative dating is not obsolete in a world of radiometric
   ages: it supplies the constraints that a numerical age is fitted into.

## Prerequisites

- [01 The Geologic Time Scale and Deep Time](./01-geologic-time-scale.md) — the
  hierarchy of names that a relative ordering is expressed in.
- [04-01-04 Igneous, Sedimentary and Metamorphic Rocks](../01-earth-structure/04-rock-types.md)
  — what the units being ordered actually are.

## 1. The principles, as inference rules

Each principle is a statement of the form "if you observe $X$, then event $A$
precedes event $B$". Stated that way, they are the premises of a deduction rather
than a list to memorise.

**Superposition.** In a sequence that has not been overturned, each bed is older
than the bed above it. Observation: bed A lies above bed B. Inference:
$B \prec A$. The condition "not overturned" is a real one, and it is tested
independently — by cross-bedding, graded bedding, or geopetal structures — not
assumed.

**Original horizontality.** Sediment is deposited in layers that are
approximately horizontal at deposition. Inference: a bed that is now dipping was
tilted after deposition, so the tilting postdates the bed.

**Lateral continuity.** A layer of sediment extends laterally until it thins to
nothing or meets a barrier. Inference: two outcrops of lithologically and
stratigraphically identical rock separated by cover are presumed continuous, and
the presumption can be tested and refuted.

**Cross-cutting relations.** A feature that cuts another is younger than the
feature it cuts. Observation: a dyke cuts a sandstone. Inference: the dyke is
younger. This principle is what extends relative dating beyond sedimentary
sequences to faulting, intrusion and metamorphism.

**Inclusions.** A fragment enclosed in a rock is older than the rock that
encloses it. Inference: a granite containing a sandstone xenolith postdates that
sandstone.

**Faunal succession.** Fossil assemblages succeed one another in a definite and
recognisable order, so a fossil content can date a bed relative to another. This
principle is empirical — it was established by observation across Europe before
there was any theory to explain it — and its modern explanation is evolution. It
is what makes long-distance correlation possible when lithologies change
laterally, as they nearly always do.

## 2. From relations to an order

Put the principles together and each field observation yields a pair $(A, B)$
meaning $A$ is older than $B$. The geological history is any **total order** of
the events consistent with every pair. That is a topological sort, and it can be
solved by enumeration when the number of events is small.

The demo does exactly this for a synthetic history of seven events — three
sedimentary units, a dyke, a fault, an overlying unit and a soil — and ten
relations that the history would produce. It solves for the admissible orders
from the relations alone and never shows the solver the constructed history
until it checks the answer.

The output is that the recovered order equals the constructed history, and — more
informatively — that **four** total orders are consistent with the ten relations:

```text
  events: 7, relations: 10, consistent total orders: 4 (acyclic)
  one consistent order (oldest first):
    1. Sst-A
    2. Sh-B
    3. Lst-C
    4. Dike-D
    5. Fault-F
    6. Sst-E
    7. Soil-G
  4 consistent orders exist, so the relations constrain the history only partly:
    position 4 is any of: Dike-D, Fault-F
    position 5 is any of: Dike-D, Fault-F, Sst-E
    position 6 is any of: Dike-D, Soil-G, Sst-E
    position 7 is any of: Dike-D, Soil-G
```

This is the honest output of a relative-dating analysis, and it is more useful
than a single preferred order. The relations determine that the three sediments
came first and the soil last, and they leave the relative timing of the dyke and
the fault unconstrained: **the dyke could have been intruded before or after the
faulting**, because nothing observed distinguishes the two. A report that
presented one of the four orders as *the* history would be discarding
information.

## 3. When the observations contradict each other

Now add one contradictory pair: the dyke is recorded as cutting the soil *and*
as being cut by it. Both cannot be true. The demo's answer:

```text
  Now add the contradictory pair (Dike-D cuts Soil-G, and Soil-G cuts Dike-D):
  consistent total orders: 0; solver verdict: a cycle is present
```

Zero admissible orders. This is a genuinely different kind of output from "the
relations constrain the history only partly", and the correct response is to
return to the outcrop. In practice the contradiction comes from one of a small
number of mistakes: a misread contact (a fault contact interpreted as an
intrusive one), a misidentification of a unit (two lithologically similar units
of different ages), or an overturned section that was not recognised.

Note what the algorithm cannot do. It can tell you that a cycle exists. It cannot
tell you which relation is wrong, because a cycle is a property of the set. The
geologist's job is to find the observation that is least well established and
re-examine it, and that judgement is not in the code.

## 4. Bracketing: the practical use of cross-cutting relations

The most common quantitative use of these principles is not a full ordering but a
**bracket**. A fault that cuts units A, B, C and D but is overlapped by unit E is
younger than D and older than E, and that is all the stratigraphy can say.

```text
  units offset by Fault-F:            Sst-A, Sh-B, Lst-C, Dike-D
  units that post-date faulting:      Sst-E, Soil-G
  => Fault-F is younger than the youngest unit it cuts (Dike-D)
  => Fault-F is older than the oldest unit that oversteps it (Sst-E)
```

The sharpness of the bracket is the duration of the gap between those two units,
and that gap is whatever it is: a single bed, or an unconformity representing
tens of millions of years. The bracket is a statement about *which* observations
bound the event, not about how well it is dated, and a bracket is what a
numerical age is then tied to. This is why relative dating is not obsolete: an
age of $312.4 \pm 0.3$ Ma on an ash bed is only useful if it can be placed in a
sequence, and placing it is relative dating.

## 5. Correlation and its quantification

Correlating two sections means proposing that a set of first-appearance datums
are the same geological instant. The proposal can be tested, and the test is
arithmetic: **count the sequence violations**.

Take two sections and the levels at which several taxa first appear. If the taxa
appeared in the same order in both sections, the correlation is consistent with
zero violations. If one section has them in a different order, the number of
pairs whose order disagrees is a measure of the inconsistency. Extending to
several sections, define a taxon ordering and count the pairs that disagree with
the observed levels in any section. Then search the possible orderings for the
one that minimises the total, exactly as the demo does for six taxa and three
sections.

The demo constructs three sections whose levels are the same synchronous set
rescaled by a per-section factor of 1.00, 0.55 and 1.35 — a condensed section and
an expanded one — and then injects a single reworked specimen of one taxon,
placing it well below its true first appearance. The result:

```text
  violations of the section data against the true order: 2
  minimum achievable violations over all 720 arrangements: 2, attained by T1 T2 T3 T4 T5 T6
  the minimum-violation arrangement equals the true order: True
```

Two things are worth extracting. First, **rescaling a section does not create
violations**: a condensed section is not an inconsistent one, and this is why
graphic correlation works across sections of very different thickness. Second,
the minimum is **not zero**. A non-zero minimum is a structural statement: no
ordering can remove those violations, so at least one datum is out of place.

Which datum? That question is answered by a leave-one-out test rather than by
knowing the answer in advance:

```text
  Leave-one-out test (which single datum, if removed, restores a zero-violation correlation?):
    drop T1: minimum violations = 2
    drop T2: minimum violations = 1
    drop T3: minimum violations = 1
    drop T4: minimum violations = 0  <-- removing this datum gives a perfect correlation
    drop T5: minimum violations = 2
    drop T6: minimum violations = 2
  Injected reworking in the synthetic data: BD T4 at 2.5 m.
```

The test identified the injected datum, and it did so from the data alone. That
is the methodological point: an outlier in a biostratigraphic correlation is
detected by its effect, and only then interpreted — as reworking, as a
downslope-transported specimen, as a taxonomic error, or as a genuinely
diachronous first appearance. The interpretation is geological; the detection is
arithmetic.

## 6. Assumptions and regime of validity

- **The ordering principles assume no post-depositional overturning** unless
  tested. Overturned sections are common in fold-and-thrust belts, and a section
  that is overturned without being recognised produces a complete, consistent and
  exactly wrong history.
- **Cross-cutting relations assume that the cutting feature is younger than
  everything it cuts.** A fault that reactivates an older fault, or a dyke that
  intrudes along an existing fault, satisfies the principle but yields a
  composite relationship that a single bracket cannot express.
- **Faunal succession assumes that first appearances are approximately
  synchronous** over the correlation distance. Species migrate, and the
  diachroneity of a first appearance is a real limit on the method's resolution.
- **Graphic correlation assumes that the sections sample the same sequence.** If
  one section straddles an unconformity that the other does not, the violation
  count will be non-zero for a reason that is geological and not an outlier.
- **The minimum-violation order is not a unique answer** in general. Several
  orderings can attain the same minimum count; ties must be reported rather than
  broken arbitrarily.

## 7. Units, and what a correlation result carries

Correlation as practised here produces a **dimensionless** ordering and,
optionally, a pair of violation counts. Nothing in it has units. The moment a
correlation is converted into an age, units enter through the time scale, and
through the age model applied to the section — a thermal-maturity model for a
well, a biozone duration from the chart, or a radiometric age on a bed. The
conversion is where the assumption enters, and it is worth keeping the
dimensionless ordering separate from the dated one so that a revision of the
chart does not silently change the correlation.

## 8. Python demonstration

[`code/02-stratigraphic_principles_demo.py`](./code/02-stratigraphic_principles_demo.py)
implements the constraint solver, the bracket, the violation count and the
leave-one-out test. Its output is quoted in §2, §3, §4 and §5 above, and it
prints a summary of the six taxa, three sections and the constructed
synchronous levels.

The section table, in which the ordering is the same in every column and the
scaling differs:

```text
taxon    true position (a.u.)        AN        BD        CD
  T1                     4.00      4.00      2.20      5.40
  T2                    11.00     11.00      6.05     14.85
  T3                    19.00     19.00     10.45     25.65
  T4                    26.00     26.00      2.50     35.10
  T5                    38.00     38.00     20.90     51.30
  T6                    47.00     47.00     25.85     63.45
```

Column BD is the condensed section, column CD the expanded one, and the T4 row of
BD is the injected reworking: 2.50 m is below the T1 datum at 2.20 m in that
section, so a first-appearance ordering that puts T4 above T1 is violated twice
in BD and nowhere else.

## 9. Common mistakes

1. **Reporting the preferred order when the relations admit several.** The set of
   admissible orders is the answer; a single one of them is not.
2. **Solving through a contradiction.** If a cycle exists in the relations,
   finding "the best" order hides the error instead of exposing it.
3. **Treating a bracket as a date.** A bracket bounds an event between two other
   events; its width is the duration of the gap and may be arbitrarily large.
4. **Assuming a condensed section is inconsistent.** Rescaling creates no
   violations; only genuinely different orders do.
5. **Calling a taxon reworked before testing.** Detect the outlier by
   leave-one-out, then interpret it.
6. **Correlating on lithology alone.** Lithofacies are diachronous by
   construction; biostratigraphy and geochronology are what tie two sections to
   the same instant.
7. **Ignoring an unconformity in one of the correlated sections.** The
   violation count will be non-zero for a structural reason, and no outlier
   removal will fix it.
8. **Forgetting that first appearances are diachronous.** The method's resolution
   is the migration time of the taxon, which for some groups is millions of
   years.

## 10. Real-world applications

- **Basin correlation and reservoir zonation.** Field-scale sequence stratigraphy
  is applied superposition and cross-cutting reasoning, and the resulting
  framework is what a numerical age is slotted into
  ([04](./04-sedimentary-basins.md)).
- **Fault-seal and trap analysis.** Whether a fault juxtaposes a reservoir
  against a seal depends on the throw, which is a relative-dating and geometry
  question, and on whether the fault is younger and thus a potential seal
  ([04-06-01](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Archaeology and Quaternary geology.** Where numerical dating is imprecise or
  impossible, stratigraphic ordering and cross-cutting relations carry most of
  the chronological content
  ([04-05-04](../05-geomorphology-and-quaternary/04-quaternary-climate.md)).
- **Tectonic histories in fold-and-thrust belts.** The ordering of deformation
  events is established by cross-cutting relations before any age is attached
  ([13-03 Quantitative Plate Tectonics](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/README.md)).
- **Hazard chronologies.** Ground-rupture histories are sequences of
  cross-cutting relations between fault strands and dated deposits; the ordering
  is relative and the dates are fitted to it.
- **Sequence stratigraphy.** The ordering of unconformity-bounded units is a
  global correlation framework, and its age assignments come from the chart
  ([26-05-05 Open Data: Geology, Geodesy and Reference Frames](../../26-reference-library/05-open-datasets-catalogue/05-datasets-geology-geodesy.md)).

## 11. Further reading

- **Nichols, G. *Sedimentology and Stratigraphy* (Wiley-Blackwell).** The
  principles as they are applied at outcrop and in the subsurface, with the
  correlation methods in context. Level: beginner to intermediate.
- **Boggs, S. *Principles of Sedimentology and Stratigraphy* (Pearson).** A
  complementary treatment with a stronger emphasis on the physical processes that
  produce the sequences. Level: intermediate.
- **Shaw, A. B. *Time in Stratigraphy* (McGraw-Hill).** The original systematic
  treatment of graphic correlation, including the construction of a composite
  standard. Level: advanced.
- **International Commission on Stratigraphy, *International
  Chronostratigraphic Chart* (current version).** The framework the correlations
  are expressed in, with the definition of every boundary. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 The Geologic Time Scale and Deep Time](./01-geologic-time-scale.md) — the
  hierarchy of names that the ordering is expressed in.
- [03 Radiometric Dating Methods and Their Assumptions](./03-radiometric-dating.md)
  — how numbers are attached to the bracketed events, and what those numbers
  assume.
- [04 Sedimentary Basins: Formation, Fill and Subsidence](./04-sedimentary-basins.md)
  — the sequences that these principles order, and the subsidence that made room
  for them.
- [04-04-05 Reading Geological Maps and Constructing Cross-Sections](../04-structural-geology/05-geologic-maps-sections.md)
  — the same reasoning applied to a map, where the cross-cutting relations are
  drawn rather than seen.
- [04-01-04 Igneous, Sedimentary and Metamorphic Rocks](../01-earth-structure/04-rock-types.md)
  — what each unit in a sequence is, and the diagnostic features that show
  whether it is overturned.
- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](../../01-mathematics/12-numerical-methods/05-linear-solvers.md)
  — the combinatorics that underlies constraint enumeration, in general form.

Exercises:
[`exercises/02-stratigraphic-principles-exercises.md`](./exercises/02-stratigraphic-principles-exercises.md)
and
[`exercises/02-stratigraphic-principles-solutions.md`](./exercises/02-stratigraphic-principles-solutions.md).

## Self-assessment checklist

- [ ] I can state each principle as an inference rule and give an observation
      that instantiates it. (§1)
- [ ] I can turn a set of field relations into pairwise constraints and say how
      many total orders are consistent with them. (§2)
- [ ] I can recognise a contradiction in a set of relations and explain why the
      output is "no consistent history". (§3)
- [ ] I can bracket a fault's age and say what determines the sharpness of the
      bracket. (§4)
- [ ] I can count sequence violations between two sections and say why
      rescaling creates none. (§5)
- [ ] I can run and interpret a leave-one-out test for a suspect datum. (§5, §8)
- [ ] I can state three assumptions of the correlation method and the regime in
      which each fails. (§6)
- [ ] I can explain why relative dating remains necessary alongside radiometric
      dating. (§4)
