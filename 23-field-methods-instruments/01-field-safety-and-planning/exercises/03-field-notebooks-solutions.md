# Solutions — 23-01-03 Field Notebooks, Metadata and Data Provenance

> Read after attempting. Lesson:
> [03 Field Notebooks](../03-field-notebooks.md). All values are **SYNTHETIC**.

---

## ★1 — Completeness score

$$S = \frac{11}{14} = 0.7857 .$$

$0.7857 < 0.80$, so the record **fails** the threshold.

Smallest passing count: we need $n/14 \ge 0.80$, i.e. $n \ge 11.2$, so $n = 12$
filled fields, giving $12/14 = 0.8571$. One more field is required than the
threshold "rounds to"; a real protocol should state whether the threshold is
applied to the count or the score, because with $F = 14$ the two answers differ.

---

## ★2 — Expected score from the form's design

If each field is filled independently with its own probability $p_f$, then
$\mathbb{E}[m_{if}] = p_f$ and, by linearity of expectation,

$$\mathbb{E}[S_i] = \frac{1}{F}\sum_{f=1}^{F} p_f .$$

Sum the probabilities:

$$3(0.99) + 0.95 + 0.98 + 0.90 + 0.99 + 0.85 + 0.97 + 0.80 + 0.99
+ 0.60 + 0.55 + 0.45 = 12.00 .$$

$$\mathbb{E}[S] = \frac{12.00}{14} = 0.8571 \;(85.71\ \%).$$

The demonstration measures $0.8625$ on 40 records; the difference of 0.005 is the
sampling error of a mean of 40 bounded scores, whose standard deviation is about
$0.0880$, giving a standard error of $0.0880/\sqrt{40} = 0.0139$. The measured
value is therefore within $0.4$ standard errors of the predicted one.

**The assumption** is independence of the fields within a record. Real forms
violate it: an operator who is behind schedule omits several fields together, so
the score distribution has more mass at low values than the independent model
predicts.

---

## ★3 — Time-zone slip

Local 08:00 at offset $+05{:}30$ means the true UTC time is 5 h 30 min earlier:

$$\text{UTC} = 08{:}00 - 05{:}30 = 02{:}30 .$$

If the logger's clock is left in local time but the file is labelled UTC, the
recorded start time is 5.5 h late relative to the truth:

$$\delta t = 5.5 \times 3600 = 19\,800\ \mathrm{s}, \qquad
n_{\text{samples}} = 19\,800 \times 100 = 1\,980\,000 \text{ samples}.$$

A record with $1.98 \times 10^{6}$ samples of offset cannot be repaired by
inspecting the data: the error is consistent internally, so every relative
arrival time within the file is right and only the origin is wrong. It is found
by comparing with an independent clock, a catalogue origin time, or the field
notebook's own record — which is exactly why the notebook records UTC.

---

## ★★4 — Clock error budget

Accumulated error is the fractional error times the elapsed time:

$$\delta t = \epsilon\,t = 10^{-6} \times 45 \times 86\,400\ \mathrm{s}
= 10^{-6} \times 3\,888\,000\ \mathrm{s} = 3.888\ \mathrm{s}.$$

Apparent distance error at $V = 2.5\ \mathrm{km/s}$:

$$\delta R = V\,\delta t = 2.5 \times 3.888 = 9.72\ \mathrm{km}.$$

**Inverting for the requirement.** Hold $\delta t \le 10^{-3}\ \mathrm{s}$ over
$t = 60 \times 86\,400 = 5\,184\,000\ \mathrm{s}$:

$$\epsilon \le \frac{10^{-3}}{5\,184\,000} = 1.93 \times 10^{-10}.$$

That is about 2 parts in $10^{10}$, four orders of magnitude tighter than the
1 ppm used above and far beyond an uncompensated quartz oscillator. It is the
quantitative reason a long deployment uses a clock disciplined to an external
reference — and the reason a short refraction survey, which needs millisecond
accuracy over hours, does not.

---

## ★★5 — Chain length after an edit

With $c_i = H(c_{i-1} \,\|\, d_i)$, changing $d_{12}$ changes $c_{12}$, and
because $c_{13}$ is computed from $c_{12}$, it changes too, and so on to $c_{100}$.
Entries $c_1 \dots c_{11}$ are unaffected. So

$$100 - 12 + 1 = 89 \text{ chain entries change}.$$

**What a reader can conclude.** That the affected record is number 12 or earlier
— more precisely, that the first *differing* entry identifies the record that
changed. The chain therefore localises an edit to a position in the sequence. It
does not reveal *which field* was changed (the digest is one-way), nor whether the
new value is correct, nor whether the recomputed chain is the "official" one
unless the chain head was published independently of the person doing the editing.

---

## ★★6 — Minimum metadata set for a three-component station

| Class | Items | Recoverable? |
|---|---|---|
| Identity | station code; operator; date of deployment | Yes, from roster |
| Position | latitude/longitude with coordinate reference system; position method and stated accuracy | By re-survey |
| Position | elevation, with the height system named (ellipsoidal or orthometric) | Expensively |
| Time | UTC start time; sample rate; clock source and lock status at start and end | Only if clock source logged |
| Instrument | sensor type and serial number; datalogger serial and firmware | Only if recorded |
| Instrument | gain or full-scale range; filter settings | Only if recorded |
| Geometry | orientation angle of component 1 relative to a named reference (e.g. magnetic north) and the method used; component mapping to channels | **No** |
| Geometry | sensor levelling or tilt, if the sensor is not self-levelling | **No** |
| Condition | ground type and coupling method (spiked, buried, sandbagged, cemented) | **No** |
| Condition | weather at deployment; ground state (frozen, saturated); vegetation and nearby disturbance | **No** |

**The critical field.** The **orientation angle with its reference** (together
with the component mapping). Without it, the horizontal components cannot be
rotated into a geographic frame, so they cannot be compared with a model, with a
second station, or with a catalogue mechanism; the data remain usable only for
scalar quantities computed from the components in an unknown frame. The vertical
component is unaffected, which is why an omission of this kind often survives
undetected until someone attempts a horizontal-component analysis.

---

## ★★★7 — A custody protocol for a 30-day campaign

**What is logged when.**

- *Per station, at deployment*: the metadata table of ★★6, with the operator's
  initials and a photo identifier.
- *Daily, on return*: a session note listing files produced, instruments used,
  deviations from the plan, and anything that failed.
- *Daily, after download*: a manifest listing every file with its byte size and
  its SHA-256 digest.
- *Daily, at the end of processing*: the chain head
  $c_{\text{day}} = H(c_{\text{day}-1} \,\|\, d_1 \,\| \dots \|\, d_k)$.

**When the head is published.** The chain head and the file count are written to
the notebook and sent to a person or system outside the field team (a project
repository, a mailing list, or a signed daily email). Publishing outside the team
is what makes the chain tamper-evident rather than merely self-consistent.

**Acceptance test at the end of each day.** Recompute the digests of all files
from that day, recompute the chain head, and compare it with the published value;
then read every file end to end once and assert that the sample count matches the
recorded duration times the sample rate, that no channel is constant, and that the
timing difference between overlapping stations is consistent with the recorded
geometry. A day that fails the test is re-downloaded from the instrument before
the instrument is reused.

**Metrics reported to the project.**

1. **File coverage** — fraction of expected files present in the chain
   (dimensionless, target 1.000).
2. **Integrity failures per day** — count of days whose recomputed head does not
   match the published head (count per campaign).
3. **Detection latency** — time from the moment a file is written to the moment a
   failure is detected (hours; the protocol's design target is one working day).
4. Optional but useful: **metadata completeness**, the score of Section 4, per
   day, with its trend, so that the workflow effect is visible while it can still
   be corrected.

**What it would not detect.** (i) A wrong value that was recorded consistently and
hashed — integrity is not correctness. (ii) An instrument malfunction that produced
plausible-looking data. (iii) A change made *before* the digest was taken, for
example in the logger's own transfer software. (iv) A deliberate rewrite by
someone who controls both the data and the published heads from that day onward.
(v) Misconfiguration that is internally consistent, such as the wrong gain stored
in both the data and the metadata.

---

## ★★★8 — Where the completeness score improves cheapest

Baseline sum of per-field probabilities $= 12.00$, so baseline
$\mathbb{E}[S] = 12.00/14 = 0.8571$.

**Raise the three lowest (0.45, 0.55, 0.60) to 0.95.** The gain in the sum is

$$\Delta = (0.95-0.45) + (0.95-0.55) + (0.95-0.60) = 0.50 + 0.40 + 0.35 = 1.25,$$

$$\mathbb{E}[S] = \frac{12.00 + 1.25}{14} = \frac{13.25}{14} = 0.9464 .$$

**Raise only the two lowest (0.45, 0.55) to 0.95.** The gain is

$$\Delta = 0.50 + 0.40 = 0.90, \qquad
\mathbb{E}[S] = \frac{12.90}{14} = 0.9214 .$$

**Ranking by score bought per field changed.**

| Change | Score gain | Gain per field |
|---|---|---|
| 0.45 → 0.95 | 0.50/14 = 0.0357 | 0.0357 |
| 0.55 → 0.95 | 0.40/14 = 0.0286 | 0.0286 |
| 0.60 → 0.95 | 0.35/14 = 0.0250 | 0.0250 |
| 0.80 → 0.95 | 0.15/14 = 0.0107 | 0.0107 |
| 0.99 → 0.95 (a *decrease*) | −0.0029 | — |

Order the work by the deficit $(0.95 - p_f)$, i.e. work on the worst field first.
The nine fields already at or above 0.95 buy nothing and should not be touched;
lowering them would reduce the score.

**The assumption that makes the ranking valid.** That all fields carry equal
weight. If a weight vector $w_f$ reflecting the *scientific* cost of a missing
field is used, the ranking changes completely: for example, a missing orientation
may be worth more than all the narrative fields combined, in which case the
correct action is to protect the 0.45-probability field only if it is the
scientifically critical one. The score's equal-weight convention, and its
consequences, must be stated wherever the score is reported.
