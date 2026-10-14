# Exercises — 23-01-03 Field Notebooks, Metadata and Data Provenance

Attempt these before reading the
[solutions](./03-field-notebooks-solutions.md). The lesson is
[03 Field Notebooks](../03-field-notebooks.md). All records and probabilities are
**SYNTHETIC**.

## ★ Foundational

**★1.** A station form has 14 required fields and 11 are filled in. Compute the
completeness score to four decimal places and state whether it passes a threshold
of 0.80. What is the smallest number of filled fields that passes?

**★2.** A form's 14 fields have **SYNTHETIC** completion probabilities 0.99,
0.99, 0.99, 0.95, 0.98, 0.90, 0.99, 0.85, 0.97, 0.80, 0.99, 0.60, 0.55, 0.45.
Compute the expected completeness score of a record, and state which single
assumption licenses that calculation.

**★3.** A logger is configured in local time at a UTC offset of $+05{:}30$ and
records a start time of 08:00. Give the true UTC start time. If the error is not
corrected, by how many seconds and how many samples is the trace offset at a
sample rate of 100 sps?

## ★★ Applied

**★★4.** An oscillator has a fractional error of 1 ppm. Compute the accumulated
timing error after 45 days, the apparent distance error at $V = 2.5\ \mathrm{km/s}$,
and — inverting the same relation — the fractional clock accuracy needed to hold
the error below 1 ms over 60 days.

**★★5.** A hash chain is built over 100 records of a campaign by
$c_i = H(c_{i-1} \,\|\, d_i)$. A metadata value in record number 12 (counting
from 1) is corrected and the chain is recomputed. How many chain entries change,
and what does that let a reader conclude?

**★★6.** Design the minimum metadata set for a three-component seismic station
deployment: give at least two items in each of the classes identity, position,
time, instrument, geometry and condition, and mark the items that cannot be
recovered after the campaign. State the one field whose absence makes the
horizontal components uninterpretable.

## ★★★ Research-oriented

**★★★7.** Specify a data-custody protocol for a 30-day campaign: what is logged
when, what is hashed and when the chain head is published, what the acceptance
test is at the end of each day, and the three metrics you would report to the
project (with their units). Say what the protocol would *not* detect.

**★★★8.** Using the field probabilities of ★2, compute the expected completeness
score after raising the three lowest probabilities to 0.95, and again after
raising only the two lowest. Rank the candidates by the score they buy per field
changed, and state the assumption that makes this ranking valid.
