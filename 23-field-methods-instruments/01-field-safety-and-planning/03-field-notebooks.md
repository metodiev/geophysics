---
id: 23-01-03
title: "Field Notebooks, Metadata and Data Provenance"
level: beginner
prereqs: ["23-01-01", "22-03-06"]
estimated_minutes: 60
tags: [fieldwork, metadata, provenance, notebooks, data-quality, reproducibility]
---

# Field Notebooks, Metadata and Data Provenance

## Learning objectives

By the end of this lesson you will be able to:

1. **List** the metadata a field record needs for its numbers to be interpretable,
   and **classify** each item as identity, geometry, time, instrument or
   condition.
2. **Compute** a metadata completeness score for a set of synthetic records, and
   **choose** the fields to improve by their marginal effect on the score.
3. **Convert** a local time with an offset to UTC, and **compute** the sample
   offset that a wrong time zone produces for a given sample rate.
4. **Compute** the accumulated timing error from a fractional clock error over a
   deployment, and **convert** it into an apparent distance for a stated
   velocity.
5. **Explain** what a content hash proves and what it does not, and **describe**
   a hash chain that localises an edit.
6. **Design** a field-recording protocol whose missing items can be reconstructed
   after the campaign, and **name** the items that cannot.

All records, completion probabilities, digests and timing errors in this lesson
are **SYNTHETIC** and are printed by the demonstration. No real station log,
network metadata file or clock measurement is used.

## Prerequisites

- [01 Field Safety, Risk Assessment and Remote-Area Protocols](01-field-safety.md) —
  the itinerary and check-in records that are themselves field metadata.
- [22-03-06 Metadata Standards and Controlled Vocabularies](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md) —
  the vocabulary side of the same problem.

## 1. Intuition: a number without metadata is not data

A value of 4213 sitting in a column means nothing. It becomes a measurement when
it carries the identity of the sensor, the position, the time, the gain, the
sample rate, the orientation and the conditions under which it was produced.
Those attachments are the **metadata**, and a field record without them is a
number that has to be discarded — not because it is wrong, but because nobody can
say what it is.

The field notebook is where metadata is born. Two properties make it different
from a laboratory record:

- **The field is the only place where some metadata can be obtained.** The
  orientation of a sensor relative to magnetic north, the state of the ground
  coupling, whether the ground was frozen, the serial number of the instrument
  that was actually deployed (as opposed to the one on the manifest) — none of
  these can be recovered later. They are recorded or lost.
- **The record is produced under time pressure and in poor conditions.** A
  protocol that requires twenty minutes of paperwork per station will be
  abbreviated at station 30. The design problem is therefore *what is the
  smallest set that is also sufficient*, plus a habit for everything else.

## 2. What a field record must contain

| Class | Items | Recoverable later? |
|---|---|---|
| Identity | site name, station code, operator, date | Usually, from the roster |
| Position | latitude, longitude, coordinate reference system, method and accuracy | Sometimes, by re-surveying |
| Elevation | orthometric or ellipsoidal height, source | Rarely, and expensively |
| Time | start time in UTC, sample rate, clock source and lock status | Only if the clock source is known |
| Instrument | sensor type, serial number, firmware, gain, filter settings | Only if the serial is recorded |
| Geometry | sensor orientation and its reference, component mapping, offsets | **No** |
| Condition | ground type and coupling, weather, vegetation, disturbance | **No** |
| Deviations | anything that departed from the plan, and why | Only if written down |

The last column is the argument for the protocol: the items marked **No** are
cheap to write down in the field and impossible to reconstruct afterwards.

Two conventions are worth fixing once for a campaign:

- **Time is UTC.** Local time, with or without daylight saving, is a hazard.
  Write the offset explicitly if local time is used at all, and never mix the two
  in one file.
- **Orientation is a number with a reference.** "North" is not a measurement.
  Record the angle and the reference direction — for a three-component sensor,
  which component pointed which way, and how that was determined.

## 3. The arithmetic of time errors

Take a homogeneous model velocity $V = 3.0\ \mathrm{km/s}$ and a
source–receiver distance of $R = 30\ \mathrm{km}$. A timing error $\delta t$
appears as an apparent distance error

$$\delta R = V\,\delta t .$$

The demonstration tabulates four errors from a sample rate of 500 sps:

| Error source | $\delta t$ (s) | $\delta R$ (km) | as a fraction of 30 km |
|---|---|---|---|
| one sample | 0.0020 | 0.0060 | 0.0 % |
| a 0.5 s pick error | 0.5000 | 1.5000 | 5.0 % |
| a 1 ppm clock error over 30 days | 2.5920 | 7.7760 | 25.9 % |
| a one-hour time-zone slip | 3600.0000 | 10800.0000 | 36000.0 % |

A fractional clock error $\epsilon$ accumulates linearly with elapsed time $t$:
$\delta t = \epsilon\,t$. One part per million over 30 days is
$10^{-6} \times 30 \times 86\,400\ \mathrm{s} = 2.592\ \mathrm{s}$, which is
already 26 % of the survey's aperture at 30 km. This is why a deployment longer
than a few days uses a clock disciplined by a global navigation satellite system
rather than the free-running oscillator in the logger: an uncompensated quartz
oscillator drifts by parts in $10^{6}$ to $10^{5}$ per day, which is one to two
orders of magnitude worse than the ppm quoted here. The exact performance of any
particular oscillator depends on its type and environment and must be taken from
its documentation, not from this table.

The last row is not a calibration problem. A one-hour offset is a bookkeeping
error, it produces a physically meaningless apparent range, and no processing
step can repair it — which is exactly why UTC is the convention.

A sample-rate conversion finishes the picture: at 500 samples per second, the
one-sample error is $1/500 = 0.002\ \mathrm{s}$; a one-hour slip is
$3600 \times 500 = 1\,800\,000$ samples. Sample counts make the size of a timing
error concrete in the units the data are stored in.

## 4. Metadata completeness as a number

Define a required-field list of $F$ fields, a per-record indicator
$m_{if} \in \{0,1\}$ for record $i$ and field $f$, and the record score

$$S_i = \frac{1}{F}\sum_{f=1}^{F} m_{if}, \qquad 0 \le S_i \le 1 .$$

This is a weighted-nothing score: every field counts the same. That is a defect,
because a missing measurement is not as damaging as a missing operator initial,
and the fix is to use weights $w_f$ with $\sum w_f = 1$ and
$S_i = \sum_f w_f m_{if}$. Either way, the score is a summary of a *workflow*, not
of the site: it measures how often the form was filled, which is a property of
the person, the time pressure and the form's design.

The demonstration scores 40 synthetic records against 14 required fields, with
per-field completion probabilities chosen to resemble a real form: reliable
fields near 0.99 and the narrative fields much lower. It reports

- 560 field slots, of which 483 are filled — **86.2 %**;
- per-record scores: mean $0.8625$, minimum $0.6429$, sd $0.0880$;
- **11 of 40 records** fall below a threshold of 0.80;
- the five weakest fields by assumed probability are ground-coupling notes
  (0.45 assumed, 0.53 observed), soil description (0.55 / 0.65), site photo
  (0.60 / 0.55), clock source (0.80 / 0.72) and gain (0.85 / 0.78).

Two observations follow. First, the expected score is the mean of the per-field
probabilities — here $12.00/14 = 0.8571$, which matches the measured 0.8625 —
so the score is predictable from the form's design before any data are collected.
Second, the score is dominated by the worst fields: the three lowest contribute
$0.45 + 0.55 + 0.60 = 1.60$ of the total 12.00, so fixing those three to 0.95
would raise the expected score to $13.25/14 = 0.9464$. Improving the score is a
targeted problem, not a general exhortation to be more careful.

## 5. Provenance: hashing and chains

A **content hash** is a fixed-length fingerprint of a byte string. The
demonstration uses SHA-256 from the standard library, which
produces 64 hexadecimal characters (256 bits). Its relevant property here is
avalanche behaviour: changing one character of the input changes about
$64 \times 15/16 = 60$ of the 64 hex characters, because each hex character
agrees with probability $1/16$ if the outputs are unrelated. The demonstration
reports 56 of 64 for its corrected value — consistent with the expectation of
60, given that a single realisation of a binomial(64, 1/16) count has a standard
deviation of $\sqrt{64 \times (1/16)(15/16)} = 1.94$.

A **hash chain** extends the idea: let $c_0$ be a fixed initial value and
$c_i = H(c_{i-1} \,\|\, d_i)$ where $d_i$ is the digest of record $i$. Then any
change to record $i$ changes $c_i$ and therefore every later $c_j$. The
demonstration corrects one metadata value in record 05 and reports that **35 of
40** chain entries change — every entry from record 05 onward. That is what makes
a chain useful: it localises a change to an interval rather than merely flagging
that something changed.

State plainly what this buys and what it does not:

- It **proves integrity**: the record has not changed since the chain was
  computed, and a change cannot be made without recomputing the whole chain.
- It does **not** prove correctness. A wrong latitude recorded consistently, hashed
  and chained is still wrong, and the chain will happily certify it.
- It does not protect against an adversary who can recompute the chain, unless
  the head of the chain is published or countersigned somewhere the adversary
  cannot reach.

The practical use in a campaign is a daily "seal": compute the chain over the
day's files, print or transmit the head, and record it in the notebook. Any
subsequent change to a day's file is then detectable by anyone holding the
notebook.

## 6. Paper, digital, and the reconstruction test

A field notebook may be paper or digital; the design criterion is the same. Ask:
**for each item, if it is missing, can it be reconstructed?** Then apply the
following, in order:

1. Automate what a machine knows: position from a receiver, time from a clock,
   serial numbers from the logger. Automatic records do not get abbreviated at
   station 30.
2. Make the manual fields few, adjacent and unavoidable in the recording tool.
   A required field with no default is filled; a free-text box at the bottom of
   the page is not.
3. Write a daily summary while memory is fresh: what departed from the plan, what
   was unusual, what will be checked tomorrow.
4. Keep the *deviations* log as carefully as the data log. A record of what was
   not done is what allows a later reader to bound the effect on the result.

Where the metadata is destined for an archive, the archive's own schema and
controlled vocabulary should be used rather than an invented one — see
[22-03-06 Metadata Standards and Controlled Vocabularies](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md)
and, for seismic station metadata specifically,
[03-10-03 StationXML Inventory, Response and Instrument Correction](../../03-scientific-computing/10-obspy-and-seismic-data/03-inventory-and-metadata.md).

## 7. Assumptions and regime of validity

1. **The required-field list is complete.** A score of 1.0 on an inadequate list
   is worthless; the list is the scientific decision and the score is only
   bookkeeping.
2. **Fields are equally important** unless weights are supplied. The score is
   therefore a workflow indicator, not a data-quality value.
3. **Hash equality implies byte equality** only for the same hash function and
   the same input encoding. State both; a newline-convention change will change
   every digest.
4. **Hash collision resistance** is a property of the function, not of the data.
   SHA-256's collision resistance is beyond reach of current methods; that is a
   statement about the algorithm, not about any particular deployment's key
   management.
5. **Timing arithmetic uses a homogeneous velocity.** The $\delta R = V\delta t$
   conversion is a translation device for sizing an error, not a location
   calculation; with a real velocity model the number differs.

## 8. The honest summary

- Orientation, coupling and condition cannot be recovered later; record them.
- Use UTC and state the clock source. A one-hour slip produced an apparent range
  of 10 800 km in the demonstration's arithmetic.
- A fractional clock error accumulates linearly; one ppm over 30 days is 2.592 s.
- Metadata completeness is predictable from the form's design, and improving the
  worst three fields moves the mean from 0.857 to 0.946.
- A hash chain proves integrity and localises edits; it never proves correctness.

## 9. Python demonstration

[`code/field_notebooks_demo.py`](./code/field_notebooks_demo.py) prints every
number quoted above. It:

1. scores 40 synthetic records against 14 required fields and reports the
   completeness distribution, the number below threshold and the weakest fields;
2. builds SHA-256 digests, chains them, corrects one metadata value and reports
   how many digest characters and chain entries change;
3. converts four timing errors into distance and into samples;
4. shows how many field slots the score covers for three dataset sizes.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/01-field-safety-and-planning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_notebooks_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/03-field-notebooks-exercises.md`](./exercises/03-field-notebooks-exercises.md)
and
[`exercises/03-field-notebooks-solutions.md`](./exercises/03-field-notebooks-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A record form has 14 required fields; 11 are filled. Compute the score and say
   whether it passes a 0.80 threshold. What is the smallest number of filled
   fields that passes?
2. A logger is set to local time at a UTC offset of $+05{:}30$ and started at
   local 08:00. Give the UTC start time and the sample offset at 100 sps if the
   error is not corrected.
3. An oscillator has a fractional error of 1 ppm. Compute the accumulated timing
   error after 45 days and the apparent distance error at 2.5 km/s.
4. State one thing a hash chain proves and one thing it cannot.

## 12. Common pitfalls

1. **Recording local time without the offset.** The most common irreparable field
   error, and the only one that produces a physically absurd answer rather than a
   slightly wrong one.
2. **Recording "north" without a reference or a method.** An orientation with no
   reference is not a measurement.
3. **Trusting the manifest instead of the deployment sheet.** Instrument serial
   numbers swapped in the field invalidate the instrument corrections.
4. **Treating the completeness score as a quality score.** It measures form
   filling, not measurement quality.
5. **Believing a hash makes data trustworthy.** It makes data *unmodified*.
6. **Leaving the deviations out.** What was not done is part of the metadata.

## 13. Where this is used

- Seismic station deployment, where orientation, gain and clock source are
  mandatory archive metadata — see
  [23-02-05 Deployment, Orientation, Timing and Metadata](../02-seismic-instruments-and-fieldwork/05-seismic-deployment.md).
- Gravity and magnetic surveys, where the base-station ties and the loop times
  are the metadata that make drift correction possible.
- ERT and EM campaigns, where electrode positions and contact resistances are
  recorded per station.
- Laboratory programmes, where sample provenance — core, depth, orientation,
  storage history — is the equivalent record.
- Any dataset destined for a repository or a journal supplement, which will be
  judged on its metadata before its physics.

## 14. Related lessons

- [01 Field Safety, Risk Assessment and Remote-Area Protocols](01-field-safety.md) —
  the itinerary and check-in records that are also provenance.
- [02 Planning a Field Campaign: Objectives, Permits, Logistics](02-field-planning.md) —
  where the recording protocol is costed into the schedule.
- [04 Permits, Land Access, Cultural Heritage and Ethics](04-permits-and-ethics.md) —
  the consent records that govern what may be published.
- [05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) —
  the field checks that the notebook must schedule.
- [22-02-05 Data Versioning and Provenance Tracking](../../22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md) —
  the same ideas applied after the data reach a computer.
- [22-05-04 Research Data Management Plans and FAIR Principles](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/04-research-data-management-plan.md) —
  where the required-field list is agreed in advance.

## 15. Further reading

Titles are given so the works can be located; this repository does not host or
reproduce copyrighted text.

- **Python documentation, `hashlib` — secure hashes and message digests.**
  The authoritative description of the hash functions used here:
  <https://docs.python.org/3/library/hashlib.html>.
- **FDSN StationXML specification, Federation of Digital Seismograph Networks.**
  The controlled vocabulary for seismic station metadata; see
  <https://www.fdsn.org>.
- **ObsPy documentation, `obspy.core.inventory`.** How station metadata is read,
  corrected and written in practice; see <https://docs.obspy.org>.

## 16. Self-assessment checklist

- [ ] I can list the metadata classes and name the unrecoverable items.
- [ ] I can compute a completeness score and pick fields to improve.
- [ ] I can convert local time to UTC and size the resulting sample error.
- [ ] I can compute an accumulated clock error and convert it to distance.
- [ ] I can explain avalanche behaviour in a hash and build a chain.
- [ ] I can state what a hash proves and what it does not.
