---
id: 00-01-03
title: "Diagnostic Self-Assessment and Placement Quiz"
level: beginner
prereqs: ["00-01-01"]
estimated_minutes: 40
tags: [self-assessment, study-method, placement, assessment]
---

# Diagnostic Self-Assessment and Placement Quiz

## Learning objectives

- Explain why an honest diagnostic *before* studying is worth more than a quick
  skim of the first lesson.
- Work through a three-part diagnostic that measures foundations, interpretation
  and computational readiness separately.
- Score your own answers against explicit criteria and map the result to a
  defensible entry point in the curriculum.
- Distinguish a **knowledge gap** (you never learned it) from a **vocabulary
  gap** (you know the idea but not the term) and treat the two differently.

## Prerequisites

[How to Learn Geophysics: A Method, Not a Reading List](./01-how-to-learn-geophysics.md).
You should already accept that reading produces recognition, and that only
retrieval and computation produce recall and transfer. That is what makes this
diagnostic meaningful: you will be *retrieving*, not recognising.

## 1. Why diagnose before you study

A curriculum that is meant to be studied in order is also meant to be entered at
the right place. Two failure modes are common and both are expensive:

1. **Starting too early.** The learner meets a derivation that assumes comfort
   with trigonometry, cannot follow it, and concludes that geophysics is beyond
   them. Usually a single missing foundation is the real cause.
2. **Starting too late.** The learner with a physics degree re-reads school
   algebra for six weeks and loses momentum before reaching anything new.

A diagnostic is not an exam. Its only job is to answer one question: **which
lesson should I open tomorrow?** It is allowed to be imperfect, because you will
re-take it.

Use three rules when you take it:

- **Closed book.** No searching, no notes. A diagnostic taken open-book measures
  your search skill, which is not what is in question here.
- **Two minutes per item, maximum.** If you cannot start, write "cannot start"
  and move on. That is data, not a failure.
- **Write your reasoning, not just the answer.** A right answer with wrong
  reasoning means you will eventually get the wrong answer.

## 2. What this diagnostic measures

Five strands, deliberately separated because they fail independently:

| Strand | What it measures | Where it is built |
|---|---|---|
| A. Units and dimensional reasoning | Converting and sanity-checking quantities | [01-mathematics/01-arithmetic](../../01-mathematics/01-arithmetic/README.md) |
| B. Physical intuition | Knowing what each measurement is sensitive to and why | [02-physics](../../02-physics/README.md), [05-core-geophysics](../../05-core-geophysics/README.md) |
| C. Data literacy | Reading plots, maps and logs; labelling axes; spotting artefacts | [03-scientific-computing](../../03-scientific-computing/README.md) |
| D. Quantitative estimation | Fermi estimation, orders of magnitude, limiting cases | [01-mathematics/01-arithmetic/02-orders-of-magnitude.md](../../01-mathematics/01-arithmetic/02-orders-of-magnitude.md) |
| E. Computational readiness | Writing a short Python script that computes and plots | [03-scientific-computing/01-python-fundamentals/README.md](../../03-scientific-computing/01-python-fundamentals/README.md) |

A learner can be strong in C and E and weak in A. That combination is common in
people arriving from software work, and it has a specific fix: arithmetic and
units, not more programming.

## 3. Part A — Foundations (units, magnitudes, definitions)

Answer each item, then compare with the "what a correct answer must contain"
column. Do not mark yourself correct because the right word appeared; mark
yourself correct only if the *content* matches.

| # | Item | What a correct answer must contain |
|---|---|---|
| 1 | Convert $1\ \text{mGal}$ to SI units. | $1\ \text{mGal} = 10^{-5}\ \text{m}\,\text{s}^{-2}$; recognises that the Gal is a cgs unit of acceleration |
| 2 | Which is larger, $500\ \text{nT}$ or $1\ \mu\text{T}$? | $1\ \mu\text{T} = 1000\ \text{nT}$; both are units of magnetic flux density $B$ |
| 3 | A wave crosses $60\ \text{km}$ in $10\ \text{s}$. Apparent velocity? | $6\ \text{km}\,\text{s}^{-1}$, with units stated and the word *apparent* queried (is the path straight or refracted?) |
| 4 | What does a relative gravimeter physically measure? | The extension of a spring / force on a proof mass, i.e. an *acceleration*, relative to a reference station — not a density |
| 5 | Speed of light in vacuum, in SI, to two significant figures | $3.0\times10^{8}\ \text{m}\,\text{s}^{-1}$ |
| 6 | Give SI units for density, electrical conductivity, thermal conductivity | $\text{kg}\,\text{m}^{-3}$; $\text{S}\,\text{m}^{-1}$; $\text{W}\,\text{m}^{-1}\,\text{K}^{-1}$ |
| 7 | A perfectly insulating layer cannot be crossed by what kind of measurement? | Any method relying on direct current flow across it (e.g. d.c. resistivity sounding through a massive insulator); motivates inductive/EM methods |
| 8 | If the mass of a buried sphere stays constant but its depth doubles, how does the peak gravity anomaly change? | Falls by roughly a factor of 4 for a compact source (inverse-square dependence of $g$), though the anomaly *width* is what determines apparent depth |
| 9 | Roughly what is gravitational acceleration at the Earth's surface? | About $9.8\ \text{m}\,\text{s}^{-2}$; values vary slightly with latitude, elevation and local mass distribution |
| 10 | What is the difference between a *potential-field* method and a *wave* method? | Potential fields respond instantaneously and decay with distance from the source; wave methods involve finite travel time and propagation, so they give kinematic information (arrival times) as well as amplitude |
| 11 | A map has scale $1{:}50\,000$. How far is $4\ \text{cm}$ on the map? | $4\ \text{cm}\times50\,000 = 2\ \text{km}$ |
| 12 | Estimate the mass of a cubic metre of typical crustal rock. | Order $2.5$–$3.0\times10^{3}\ \text{kg}$; any answer within a factor of 2 with reasoning is acceptable |

**Scoring Part A.** One mark per item, 12 marks total.

## 4. Part B — Interpretation (what does the anomaly mean?)

These items test whether you can reason from a *response* back to a *cause* — the
backward half of the inference chain.

**B1.** Two surveys over the same small target produce (i) a gravity anomaly that
is a smooth, symmetric low and (ii) a magnetic anomaly that is asymmetric with a
positive lobe to the south and a negative lobe to the north. Explain why one
anomaly is symmetric and the other is not.

A correct answer notes that gravity depends only on the distribution of *mass*,
which is symmetric about the body, whereas a magnetic anomaly depends on the
vector sum of the inducing field (inclined at the survey latitude) and any
natural remanent magnetisation, whose direction need not be the present field
direction. Asymmetry therefore carries information about field direction and
remanence — see [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md).

**B2.** A seismic record shows a travel-time curve that is a straight line
through the origin out to $40\ \text{km}$, then a second straight segment with a
shallower slope. What geometry produces that?

A correct answer: a two-layer model with a faster layer beneath a slower one;
direct arrivals in the upper layer give the first segment, and head waves
critically refracted along the interface give the second with slope $1/v_2$. The
break point in distance marks where the head wave overtakes the direct arrival.

**B3.** A resistivity survey reports very low apparent resistivity over a valley
floor. Give two physically different explanations and one measurement that would
discriminate them.

Correct answers include: a clay-rich, water-saturated unit (electrolytic
conduction), or a fracture zone saturated with mineralised groundwater. A
discriminating measurement could be induced polarisation (chargeability) or
seismic refraction (velocities differ between clay and fractured rock).

**B4.** A time-series plot shows a strong daily cycle. What physical effect could
produce a daily cycle in a gravity or magnetic record, and why is this not an
Earthquake signal?

Correct: solid Earth tides (and, in magnetics, ionospheric/thermal effects)
driven by solar and lunar forcing have dominant daily and semi-daily periods;
tides are predictable from astronomical theory, so they are modelled and removed
rather than interpreted.

**Scoring Part B.** Four items; award 0, 1 or 2 marks each for "no useful
content", "partly correct", "fully reasoned", 8 marks total.

## 5. Part C — Computation (can you compute and check?)

Do this on your own machine, or with pencil and calculator, but do the
arithmetic yourself at least once.

**C1.** The gravity anomaly of an infinite horizontal slab is

$$\Delta g = 2\pi G \rho h,$$

where $G \approx 6.674\times10^{-11}\ \text{m}^{3}\,\text{kg}^{-1}\,\text{s}^{-2}$,
$\rho$ is the density contrast and $h$ the slab thickness. Compute the anomaly
in mGal for a $200\ \text{m}$ thick slab with a density contrast of
$0.3\ \text{g}\,\text{cm}^{-3}$.

Work it in two independent ways and require the answers to agree.

*Route 1 — SI.* Convert the density contrast to $\rho = 300\ \text{kg}\,\text{m}^{-3}$,
then

$$\Delta g = 2\pi \times 6.674\times10^{-11} \times 300 \times 200
\approx 2.52\times10^{-5}\ \text{m}\,\text{s}^{-2}.$$

Convert to mGal by dividing by $10^{-5}\ \text{m}\,\text{s}^{-2}$ per mGal:
about $2.5\ \text{mGal}$.

*Route 2 — rule of thumb.* For $\rho$ in $\text{g}\,\text{cm}^{-3}$ and $h$ in
metres, $\Delta g \approx 0.0419\,\rho h$ mGal, so
$0.0419 \times 0.3 \times 200 \approx 2.5\ \text{mGal}$.

The two routes must agree. If they do not, the error is almost always in the
density or the power of ten, and finding that disagreement is the entire point
of the exercise.

**C2.** Write a Python function that converts a list of anomaly values in
$\text{mGal}$ to SI and prints both, then verify it against item C1.

Reference solution, deliberately short and standard-library only:

```python
MGAL_TO_SI = 1.0e-5  # 1 mGal = 1e-5 m/s^2


def mgal_to_si(values):
    """Convert gravity anomalies from mGal to m/s^2."""
    return [value * MGAL_TO_SI for value in values]


if __name__ == "__main__":
    readings = [2.5, -12.0, 0.4]
    for reading, si in zip(readings, mgal_to_si(readings)):
        print(f"{reading:8.3f} mGal = {si:.3e} m/s^2")
```

Check the output: $2.5\ \text{mGal}$ must print as $2.500\times10^{-5}$, not
$2.5\times10^{-4}$. If it prints the wrong power of ten, that is the same error
class as C1, and it costs the two marks for this item even though the code ran.

**C3.** Extend the script to compute the infinite-slab anomaly and plot
anomaly against density contrast. Use $\Delta g = 2\pi G \rho h$ and print a
table. Do not import any library beyond the standard library for this item;
`matplotlib` is intentionally not required.

**Scoring Part C.** Three items; 0, 1 or 2 each, 6 marks total.

## 6. Scoring and placement

Total: 26 marks. Use the table below, but treat your *pattern* of marks as more
important than the total.

| Result | Likely situation | Recommended entry point |
|---|---|---|
| Part A below 8/12 | Foundation gap in arithmetic, units or vocabulary | [01-mathematics/01-arithmetic](../../01-mathematics/01-arithmetic/README.md), then [02-physics/01-measurement-and-physical-reasoning](../../02-physics/01-measurement-and-physical-reasoning/README.md) |
| Part A strong, Part B weak | Can compute but cannot reason from an observation back to a cause | [05-core-geophysics](../../05-core-geophysics/README.md), reading every "physical interpretation" section aloud |
| Part A strong, Part B strong, Part C weak | Understands geophysics but not yet productive computationally | [03-scientific-computing/01-python-fundamentals](../../03-scientific-computing/01-python-fundamentals/README.md), fast-track to NumPy |
| Proficient in A, B and C | Ready for the quantitative core | [01-05 single-variable calculus](../../01-mathematics/05-single-variable-calculus/README.md) in parallel with [05-core-geophysics](../../05-core-geophysics/README.md) |
| Comfortable across all four parts, professional background | Needs the map, not the foundations | [02-curriculum-map](../02-curriculum-map/README.md), then a domain track |

Two warnings about this table. First, a strong overall score with a hole in
*one* strand is worse than a middling score without holes, because the hole is
exactly what will stop you four modules later. Second, do not use the table to
skip prerequisites that the [dependency graph](../02-curriculum-map/02-dependency-graph.md)
declares; placement selects your *starting* lesson, not a bypass.

## 7. A worked diagnostic example

Consider a learner with a biology degree and two years of Python:

- Part A: 7/12. Wrong on the mGal conversion and the gravimeter's physical
  response; right on the map scale and magnitudes.
- Part B: 6/8. Strong reasoning on the seismic travel-time item.
- Part C: 4/6. Correct script, wrong power of ten in the printed conversion.

Diagnosis: the tools are there (Part C script worked, Part B reasoning worked),
but the habit of *dimensional checking* is missing. Part A item 1 and Part C
failed for the same underlying reason — no dimensional check after conversion.

Prescription: work [01-arithmetic/03-units-and-dimensional-analysis.md](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
before anything else, then enter [05-core-geophysics](../../05-core-geophysics/README.md).
The learner does not need to restart mathematics from the beginning; they need
one lesson and a habit enforced until it is automatic.

That is what a useful diagnosis looks like: it identifies a *single* missing
habit, not a general deficiency.

## 8. Re-taking the diagnostic

Re-take the diagnostic:

- **before each stage transition**, as defined in
  [The Six Stages and Their Mastery Checkpoints](./02-six-stages.md);
- **after any long break**, because retention decays and the decay is uneven;
- **whenever a lesson feels opaque**, because the cause is usually an earlier
  gap, not the current material.

Keep your answers. The comparison across attempts — which items stayed wrong,
which strand is improving — is more informative than any single score.

## Common mistakes

1. **Marking yourself right because the term was familiar.** Mark the *content*
   of the answer, not its vocabulary.
2. **Taking the diagnostic open-book.** You will place yourself too high and
   meet the consequences several modules later.
3. **Reading the placement table as a verdict on ability.** It is a routing
   decision, and routing decisions are cheap to revise.
4. **Skipping Part C because "I'll learn the coding later".** Estimations and
   conversions are where most silent errors enter geophysical work.
5. **Ignoring the pattern of marks.** A single weak strand, not the total, is
   what determines where you should start.

## Real-world applications

Diagnostic thinking is not a study-only habit:

- **Survey planning** begins with the question "what property contrast exists
  here, and which method is sensitive to it?" — the same reasoning Part B tests.
- **Quality control** of a delivered dataset is a dimensional and magnitude
  check: are the numbers in the range physics permits?
- **Technical interviews and qualifying exams** present exactly this kind of
  two-minute item, expecting a spoken estimate and a stated limitation.

## Further reading

- Bloom, B. S. (Ed.) (1956). *Taxonomy of Educational Objectives, Handbook I:
  Cognitive Domain.* Longmans, Green. — The origin of the distinction between
  recall and application that this diagnostic is built on.
- Anderson, L. W., & Krathwohl, D. R. (Eds.) (2001). *A Taxonomy for Learning,
  Teaching, and Assessing.* Longman. — The revised taxonomy used to write the
  learning objectives throughout this curriculum.
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning.
  *Assessment in Education*, 5(1), 7–74. — A review of the evidence that
  formative assessment — checking understanding to change what you do next —
  produces large learning gains.
  Citations are bibliographic records only. Confirm availability through your
  library or a DOI resolver before citing them yourself.

## Related lessons

- [How to Learn Geophysics: A Method, Not a Reading List](./01-how-to-learn-geophysics.md)
- [The Six Stages and Their Mastery Checkpoints](./02-six-stages.md)
- [Deliberate Practice, Spaced Repetition and Problem-Solving Habits](./04-study-habits.md)
- [Master Curriculum Map: How the 27 Folders Connect](../02-curriculum-map/01-master-map.md)
