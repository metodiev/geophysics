# Module 23-01 — Field Safety, Planning and Logistics

**Stages:** beginner → intermediate · **Prerequisites:** none beyond the
orientation module; the safety lesson is written to be the first field lesson in
the curriculum.

This module is the part of geophysics that happens before any data exist. It
treats a campaign as an engineering project with four coupled budgets — attention,
time, access and money — and it makes each of them computable. The organising
idea is that **every one of these budgets is arithmetic, and none of it is
announced as a warning**. A schedule is $\mathbb{E}[T] = D/w$ with a
$\sqrt{D(1-w)}/w$ spread; a permission chain is $p^{M}$; a detection protocol is
$\tau/2 + g$; a metadata form has an expected completeness score computed from its
own field probabilities. Each of those is a number you can compute in a plan,
compare with a requirement, and be held to afterwards.

The second theme is that **the field is the only place where some things can be
obtained**. Sensor orientation, ground coupling, the actual instrument serial
number, what departed from the plan — these are recorded or lost. The module
therefore spends as much time on the record as on the activity: what a field
notebook must contain, which items are recoverable, and what a content hash does
and does not prove.

The third theme is honesty about scope. Risk scores are ordinal and rank; they do
not measure. Permission probabilities are a design tool, not a forecast of
anybody's willingness to agree. Consent is an obligation, not a transaction, and
no arithmetic converts it into an option. Where a real process — heritage
protection, land tenure, free, prior and informed consent — is discussed, the
lesson says what is general and refers the specific requirement to the responsible
authority and the affected community.

All numbers in this module are **SYNTHETIC**: the hazards, ratings, weather
probabilities, completion probabilities, digests and rights-of-way are chosen
teaching values printed by the demonstrations in [`code/`](code). No real risk
assessment, incident statistic, land record, weather series or commercial rate is
used or reproduced.

## Learning objectives

By the end of this module you will be able to:

1. **Build** a risk register with ordinal ratings, rank it, and measure the effect
   of a stated control on the total and on the residual severity.
2. **Compute** the detection delay $\tau/2 + g$ of a check-in protocol, the
   probability of responding inside a stated rescue window, and the alarm burden
   the protocol generates.
3. **Turn** a scientific objective into a number of productive days, then into a
   calendar schedule with a mean, a spread and a quantile.
4. **Measure** how weather persistence raises the mean, the spread and the overrun
   probability of a campaign at an unchanged long-run working fraction.
5. **Price** a campaign from a mobilisation charge and a daily rate, and quote the
   90th percentile rather than the expectation.
6. **Specify** the metadata a field record needs, score the completeness of a
   recording workflow, and design a provenance chain that localises edits.
7. **Compute** the probability that a many-part permission chain succeeds, the
   excluded area a buffer adds, and the lead time an access problem requires.
8. **State** what free, prior and informed consent requires in practice and which
   design decisions must be made before it is negotiated.

## Prerequisites

- [00-01-01 How to Learn Geophysics: A Method, Not a Reading List](../../00-orientation/01-study-roadmap/01-how-to-learn-geophysics.md) —
  why written procedures, not intentions, are the unit of learning.
- [05-01-02 Taxonomy of Methods: Active/Passive, Source/Receiver Geometry](../../05-core-geophysics/01-what-geophysics-measures/02-method-taxonomy.md) —
  what a field campaign is doing to the ground.
- [05-05-01 Survey Planning: Objectives, Target Resolution, Budget](../../05-core-geophysics/05-survey-design-and-acquisition/01-survey-planning.md) —
  the geophysical design that this module schedules and permits.
- [22-03-06 Metadata Standards and Controlled Vocabularies](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md) —
  the vocabulary the field record must eventually satisfy.
- [21-09-03 Data Ethics, Indigenous Data Sovereignty and Geoscience](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/03-data-ethics-geoscience.md) —
  the governance framework behind lesson 04.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Field Safety, Risk Assessment and Remote-Area Protocols](01-field-safety.md) | beginner | A halved-likelihood control removed 42.2 % of the score and left 5 of 8 hazards severe; a 24 h check-in interval put two thirds of incidents outside a 10 h rescue window |
| 02 | [Planning a Field Campaign: Objectives, Permits, Logistics](02-field-planning.md) | intermediate | 20 productive days became $37.1 \pm 5.6$ calendar days; persistence added 2.0 d to the mean and 13 % to the overrun risk at an unchanged working rate |
| 03 | [Field Notebooks, Metadata and Data Provenance](03-field-notebooks.md) | beginner | A 14-field form predicts its own completeness (0.857); a one-character correction changed 35 of 40 chain entries and left 11 of 40 records below threshold |
| 04 | [Permits, Land Access, Cultural Heritage and Ethics](04-permits-and-ethics.md) | intermediate | 25 parcels at 80 % give a 0.378 % chance of a complete survey; a 0.5 % zone coverage clipped 79 of 120 lines; a $\pm25$ m buffer tripled the excluded area |

## Suggested path

**If you have never been in the field:** read 01, then 03, and run both
demonstrations. Together they cover the two things that go wrong most often —
detection and metadata — and both are cheap to fix before mobilisation.

**If you are planning a campaign:** 02 for the schedule and the cost model, 04
for the permission chain and the lead time, and then 01 §5–§6 for the protocol the
schedule must accommodate.

**If you supervise field work:** 01 in full (including the failure-mode analysis
of §7) and 04 §5–§7, which is where the obligations that outlast the campaign
live.

**If you are preparing a research project or a proposal:** 02 §3–§6 for the
quantitative schedule justification, 03 §4–§5 for the data-management commitments,
and the ★★★ exercises of all four lessons.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-field-safety.md`](01-field-safety.md) | Lesson 01 |
| [`02-field-planning.md`](02-field-planning.md) | Lesson 02 |
| [`03-field-notebooks.md`](03-field-notebooks.md) | Lesson 03 |
| [`04-permits-and-ethics.md`](04-permits-and-ethics.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/field_safety_demo.py`](code/field_safety_demo.py) | Risk register and controls, check-in alarm burden, detection delay and window probability |
| [`code/field_planning_demo.py`](code/field_planning_demo.py) | Schedule mean, spread and quantiles; persistent versus independent weather; cost and sensitivity |
| [`code/field_notebooks_demo.py`](code/field_notebooks_demo.py) | Metadata completeness, SHA-256 digest and chain behaviour, timing errors in distance and samples |
| [`code/permits_and_ethics_demo.py`](code/permits_and_ethics_demo.py) | Permission chain, line-versus-zone clipping, buffer arithmetic, consent protocols, access lead time |

## How to run the demos

Use the project virtual environment:

```bash
cd 23-field-methods-instruments/01-field-safety-and-planning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_safety_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_planning_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_notebooks_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python permits_and_ethics_demo.py
```

Each demo prints labelled results under numbered section banners, starts from
`np.random.default_rng(20261014)`, uses no network and no file I/O, prints a
`SYNTHETIC` provenance line and exits 0. All four run in well under a second.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> You are asked to plan a 4 km² near-surface survey with 50 m line spacing and a
> production rate of 4 line-km per productive day. **(a)** Compute the productive
> days and then the calendar schedule at an independent daily working probability
> of 0.55, including its standard deviation and its 90th percentile. **(b)** The
> area is divided into 30 parcels agreed with probability 0.85 each. State the
> probability that the survey is complete and the two design changes that would
> make the outcome degrade gracefully. **(c)** A heritage mask covers 0.6 % of the
> area and requires a $\pm20$ m buffer around zones of 30 m width. Compute the
> buffered coverage and the probability that a 2 km line clips a zone. **(d)**
> Name three metadata items that must be recorded in the field because they cannot
> be recovered, and one arithmetic consequence of a one-hour time-zone slip.

## Common pitfalls across this module

1. **Planning productive days as calendar days.** The gap is a factor of about
   two at typical working fractions, and it is the single largest schedule error.
2. **Quoting an expected value as a plan.** A plan that finishes on the mean is
   late half the time; quote a quantile.
3. **Assuming independence where it does not hold.** Weather persistence raised
   the 90th percentile by 7.2 days at $D = 20$, and a single hostile access road
   correlates many parcels.
4. **Treating an ordinal score as a measurement.** Averaging risk scores, or
   taking percentages of them, invents precision the scale does not have.
5. **Designing detection that needs the casualty's cooperation.** If the missing
   party must raise the alarm, the protocol has no detection function.
6. **Leaving the data model until after consent is negotiated.** An embargo that
   cannot be represented cannot be honoured.
7. **Reading a completeness score as a quality score.** It measures form filling,
   and it is dominated by the two or three worst fields.

## Related modules

- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  the geophysical design decisions this module schedules and permits.
- [22-02 Reproducible Workflows](../../22-data-engineering-reproducibility/02-reproducible-workflows/README.md) —
  what happens to the field record once it reaches a computer.
- [23-02 Seismic Instruments and Fieldwork](../02-seismic-instruments-and-fieldwork/README.md) —
  the first method-specific module, where these plans become a deployment.
- [23-07 Field Campaign Case Studies](../07-field-campaign-case-studies/README.md) —
  the whole sequence carried through end to end.
- [21-09 Ethical and Responsible Analytics](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/README.md) —
  the reporting and data-ethics obligations that begin in the design.
