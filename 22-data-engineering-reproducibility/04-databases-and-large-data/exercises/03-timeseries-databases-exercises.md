# Exercises — 22-04-03 Time-Series Databases for Sensor Networks

Attempt these before reading the
[solutions](./03-timeseries-databases-solutions.md). The lesson is
[03 Time-Series Databases for Sensor Networks](../03-timeseries-databases.md). Numbers
refer to the **SYNTHETIC** model of `code/timeseries_databases_demo.py`: $10^{6}$ samples
at 1 Hz, 8-byte values, a quantisation step of $10^{-3}$, 1-minute and hourly aggregate
tiers.

## ★ Foundational

**★1.** Compute the naive storage of $10^{6}$ 1 Hz samples with 8-byte values and
4-byte timestamps, and state how many such spans fit in a year.

**★2.** State what the second difference $d_2 = x_{i+1} - 2x_i + x_{i-1}$ removes, and
why that helps compression.

**★3.** State the ratio between the raw byte count and the 1-minute aggregate byte count
for a one-hour query, and explain where the ratio comes from.

## ★★ Applied

**★★4.** The demonstration measures mean bit widths of 12.8 (noise-dominated) and 6.3
(smooth) for the same scheme.

(a) Compute the storage ratio against float64 (64 bits) for each. (b) State the
quantisation error bound and compare it with the two series' standard deviations.
(c) State what a paper should report when it quotes a compression ratio.

**★★5.** A network has 200 channels at 10 Hz with 8-byte values, retaining raw and
hourly means.

(a) Compute the raw and hourly volumes per channel-year and for the network.
(b) Compute the overhead of the hourly tier as a percentage of raw. (c) State the
decision the arithmetic supports, and the question it does not answer.

**★★6.** A channel has a clock that drifts 12 s per month and is corrected by a service
that also re-delivers the last month of data.

(a) State the schema feature that makes the re-delivery idempotent. (b) State the two
timestamps you would store and what each records. (c) State the failure that would occur
if only the instrument time were stored and the correction were applied in place.

## ★★★ Research-oriented

**★★★7.** Design the storage architecture for a 500-channel network at 100 Hz with a
ten-year lifetime and a requirement to support (i) live monitoring of the last day,
(ii) a research query for a whole year at 1-minute resolution, and (iii) reprocessing
after a calibration change. State the tiers, their retention, the compression per tier,
the partition scheme, and the annual volume. State the one requirement that dominates
the cost.

**★★★8.** The lesson's compression model is lossy by construction. Design a measurement
that determines, for a given channel, the quantisation step at which the loss becomes
irrelevant to the analysis: state the statistic, the reference the loss is compared
against, and the confounder (the analysis's sensitivity). State what the measurement
cannot guarantee for analyses not yet run.

**★★★9.** A group deletes raw data after one year and keeps hourly means forever.
Quantify the failure: state the fraction of the archive that becomes unreprocessable
after five years, the reprocessing scenarios that are blocked, and the storage that would
have been needed to avoid it. State the retention policy you would propose and the
evidence needed to defend it.
