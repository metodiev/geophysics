# Solutions — 04-03-02 Stratigraphic Principles and Relative Dating

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — A single relation, and what it leaves open

**(a)** With only $P \prec Q$ the admissible orders are
$P, Q, R$; $P, R, Q$; and $R, P, Q$.

**(b)** Three.

**(c)** Adding $R \prec P$ leaves exactly one:
$R, P, Q$. Two relations now form a chain that pins every event.

**(d)** A set of relations determines the orders **consistent with all the
observations**; reporting one of them as "the" history discards the information
that the others were admissible, which is exactly the information a reader needs
to know how much the outcrop actually constrains.

---

## ★2 — Naming the principle

**(a)** Superposition (with the caveat that the section must not be overturned,
which is tested independently).

**(b)** Cross-cutting relations.

**(c)** Inclusions: the fragment is older than the rock that contains it.

**(d)** This is the **test for way-up**, not a dating principle: a graded bed
fines upward, so it identifies which way is up and makes superposition
applicable. It is a prerequisite for using (a) rather than an instance of it.

**(e)** Faunal succession, which is the principle that allows correlation when
lithology changes laterally.

---

## ★3 — Bracketing a dyke

**(a)** The dyke is younger than the youngest unit it cuts (unit 3) and older
than the oldest unit that oversteps it (unit 4).

**(b)** The bracket's width is the duration of the gap between unit 3 and unit 4.
If they are consecutive beds the bracket is very sharp in relative terms; if unit
4 rests on an unconformity, the bracket may span tens of millions of years.

**(c)** No. A bracket is a statement about which observations bound the event, in
a relative system. Converting it to a date requires either dating one of the
bracketing units or locating the dyke in a dated sequence, and that conversion is
a separate step with its own assumptions
([04-03-03](./03-radiometric-dating-solutions.md)).

---

## ★4 — A set of relations with a cycle

**(a)** The cycle is $B \prec C \prec D \prec B$. Three relations close a loop.

**(b)** **Zero.** An admissible order requires every relation to be satisfied, and
a cycle cannot be satisfied by any total order, because a total order is
antisymmetric: it cannot place B before C before D and also D before B.

**(c)** Re-examine the outcrop. The algorithm can tell the geologist that a cycle
exists, and it cannot tell them which relation is wrong, because a cycle is a
property of the set and not of any one member. The likely causes are a misread
contact, a misidentified unit, or an overturned section that was not recognised.
The judgement about which observation is least well established is not in the
code and is the geological contribution.

---

## ★5 — The demo

**(a)** `events: 7, relations: 10, consistent total orders: 4 (acyclic)`.

**(b)**

```text
    position 4 is any of: Dike-D, Fault-F
    position 5 is any of: Dike-D, Fault-F, Sst-E
    position 6 is any of: Dike-D, Soil-G, Sst-E
    position 7 is any of: Dike-D, Soil-G
```

So the dyke and the fault are not ordered relative to each other, and nothing
observed distinguishes them.

**(c)** Adding the contradictory pair gives
`consistent total orders: 0; solver verdict: a cycle is present`.

**(d)** The number is a result because it quantifies the constraint: four orders
consistent with ten relations means the relations are strong enough to place the
three oldest units and the youngest, and not strong enough to order the dyke
against the fault. That is a statement about what further fieldwork would buy —
one more cross-cutting observation between the dyke and the fault could reduce
the count to one.

---

## ★6 — Counting violations by hand

**(a)** For the arrangement $T1, T2, T3$ against section 2, the pair $(T2, T3)$
has order $T2$ before $T3$ in the arrangement and $T3$ before $T2$ in the second
section: **1 violation**. Section 1 agrees with the arrangement, contributing
none. Total 1.

**(b)** For the arrangement $T1, T3, T2$ against section 1, the pair $(T2, T3)$
is violated: 1 violation. Against section 2, none. Total 1.

**(c)** The minimum is 1, and it is attained by both arrangements (and by
$T3, T1, T2$ and $T1, T2, T3$'s mirror). The correlation is inconsistent by one
pair and the two sections disagree about the relative order of two taxa.

**(d)** A third section agreeing with section 1 makes the arrangement
$T1, T2, T3$ have 1 violation out of 3 section-pairs, while
$T1, T3, T2$ has 2. The **majority** rule then selects $T1, T2, T3$ and flags the
single disagreeing datum in section 2 as the suspect one — which is the
quantitative form of the reasoning a stratigrapher does by inspection.

---

## ★7 — A non-zero minimum, and two bad data

**(a)** No arrangement of the taxa explains the data: at least one datum must be
wrong, because a non-zero minimum is a property of the whole data set and cannot
be removed by reordering.

**(b)** Because a prior belief about which taxon is reworked is exactly what the
analysis is supposed to test. A taxon that is commonly reworked is a hypothesis,
and the leave-one-out test converts it into a measurement by asking which single
removal improves the correlation. In the demo the test identifies the injected
datum:

```text
    drop T4: minimum violations = 0  <-- removing this datum gives a perfect correlation
  Injected reworking in the synthetic data: BD T4 at 2.5 m.
```

**(c)** Four interpretations, with the distinguishing observation:

- **Reworking** of a fossil into a younger bed. Distinguished by the specimen's
  preservation: abraded, rounded or broken, and often a different lithology from
  the enclosing bed.
- **Caving or contamination of the sample** during drilling or collection.
  Distinguished by its occurrence in a single sample and by the drilling record.
- **Downslope transport** of a live or dead specimen into deeper water.
  Distinguished by sedimentological evidence of transport at that level.
- **A taxonomic error**, so that two species were conflated. Distinguished by
  re-examination of the specimens.

**(d)** Construct a section in which two taxa are each displaced. Removing either
one alone still leaves the other's violations, so the leave-one-out test reports
a non-zero minimum for every single removal. The method then cannot identify
either, and the correct reading is that the search should move to
leave-**two**-out (which raises the combination count from $n$ to $n(n-1)/2$) or
that the section as a whole is suspect. **A leave-one-out test that finds no
single culprit is evidence for a systematic problem, not evidence that the data
are good.**

---

## ★8 — Diachroneity and what it limits

**(a)** $500 \text{ km}/2 \text{ Ma} = 250$ km/Ma, i.e. 0.25 m/a.

**(b)** Datums 150 km apart are diachronous by
$150/250 = 0.6$ Ma.

**(c)** At 20 cm/ka $= 200$ m/Ma, 0.6 Ma corresponds to
$200 \times 0.6 = 120$ m of section. A typical biostratigraphic zone is of order
0.5–2 Ma thick in time, so **the diachroneity of the first appearance is
comparable to the resolution of the zone it is used to define** — the datum is
not a synchronous surface at the precision being claimed.

**(d)** A first-appearance datum may be treated as synchronous when the migration
time is small compared with the resolution required, which in this example means
correlating sections much closer than 250 km or accepting a resolution coarser
than about a million years. When the condition fails, a correlation built on the
datum is a correlation that is systematically misordered by an amount comparable
to its own resolution — and no statistical test of the violation count will reveal
it, because a consistent mapping of diachronous datums still produces zero
violations. **This is the method's floor, and it is geological rather than
arithmetic.**
