# Exercises — 22-06-03 Cost, Scaling and Practical Efficiency

Attempt these before reading the
[solutions](./03-cost-and-scaling-solutions.md). The lesson is
[03 Cost, Scaling and Practical Efficiency](../03-cost-and-scaling.md).

Adopt the **SYNTHETIC** teaching rates used throughout the lesson and the demonstration:
0.05 units per core-hour, 20 units per TB-month of storage, 90 units per TB of egress, and
a serial fraction of 0.05 unless a problem says otherwise.

## ★ Foundational

**★1.** Write the three cost terms of one result and name the quantity each one is
proportional to.

**★2.** A run uses 128 cores for 6 hours and writes 1 TB kept for 18 months.

(a) Compute each of the three terms and the total. (b) Compute the storage-plus-egress
share of the total. (c) State which single change would save the most, with the number.

**★3.** State why the cost per unit of work rises under weak scaling even when the wall
time does not change, and give two mechanisms.

## ★★ Applied

**★★4.** A project produces 300 TB of raw data per year and keeps it for five years.

(a) Compute the five-year storage cost at the teaching rate. (b) Compute the annual cost
if only one year of raw data is kept and older data is deleted after being reduced to a
10 TB derived product. (c) State the scientific risk introduced by (b) and the mitigation.

**★★5.** A 10-hour run at 128 cores has $p = 0.06$.

(a) Compute the wall time and cost at 128, 512 and 2 048 cores. (b) Find the smallest
core count that reaches a 4-hour deadline, and the cost. (c) Compute the serial floor and
state whether a 30-minute deadline is reachable.

**★★6.** A group's annual bill is 1 000 units, split as in the lesson's Table 5.

(a) Compute the amount in compute, in storage, in egress and in recomputation.
(b) A solver change makes the compute 30 % faster; compute the new bill and the
improvement. (c) Deleting regenerable intermediates removes half of the derived-product
storage and half of the recomputation; compute the new bill from the original and state
which intervention was more effective.

## ★★★ Research-oriented

**★★★7.** Forecast the cost of a 10 000-realisations ensemble in which each realisation
takes 3 core-hours and writes 40 GB kept for two years, with a 5 % failure rate and one
retry. State the five forecast lines, the arithmetic, the dominant term, and the one
measurement you would make first to reduce the uncertainty.

**★★★8.** Design an experiment to measure a group's true cost per unit of work from
their own records: state the data you would need to record per run (compute, storage
space and duration, transfer volumes, failures, who and which project), how you would
attribute shared infrastructure, and the three ways the resulting number would mislead
if used naively.

**★★★9.** A colleague argues for buying twice the cores to halve every deadline, quoting
a speedup curve. Analyse the argument: state when it is right, when the serial floor
makes it impossible, the marginal cost of the last halving, and the evidence you would
require before approving the spend. State the non-cost reason a shorter deadline can
still be worth the money.
