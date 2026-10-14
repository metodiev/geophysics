# Exercises — 22-03-04 Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)

Attempt these before reading the
[solutions](./04-getting-earth-data-solutions.md). The lesson is
[04 Programmatic Access to Earth Data](../04-getting-earth-data.md). Numbers refer to
the **SYNTHETIC** service model of `code/getting_earth_data_demo.py`: 1.0 s per
request, 30-day window cap, 5 MB/s, 40 MB per day of record, 60 requests per minute,
5 % per-request failure probability, 2 retries. No real service limit is quoted.

## ★ Foundational

**★1.** State the two differences between a query to a data service and a file on
disk, and explain why each makes an unrecorded fetch non-reproducible.

**★2.** For the demonstration's fetch of 365 days at a 7-day window: (a) compute the
request count, the latency total and the transfer total; (b) state the plan's total
and compare it with the 1-day-window plan; (c) state which quantity the window length
controls.

**★3.** State the five fields a reproducible fetch must record, and for each the
question it answers that a checksum cannot.

## ★★ Applied

**★★4.** A service caps requests at 10 days and serves data at 4 MB/s with a 2 s
per-request latency. You need 500 days of a 20 MB/day stream.

(a) Compute the requests, latency total, transfer total and plan total. (b) State what
the totals would be with 1-day windows and give the overhead saving of the cap.
(c) State the assumption about the service that makes the larger window legitimate.

**★★5.** A 25-request fetch has a per-request failure probability of 0.06.

(a) Compute the probability that at least one request fails. (b) Compute the expected
attempts per request with two retries, and the extra latency if each request costs
1.2 s. (c) State the check that catches a request which failed all attempts, and why
retries alone are insufficient.

**★★6.** A group's analysis reads a service at run time, and the same script produces
a 0.8 % different result in two consecutive months. List three explanations consistent
with this observation, and state the one piece of the fetch record that would
distinguish them.

## ★★★ Research-oriented

**★★★7.** Design the fetch layer for a study that needs (i) 120 broadband stations'
continuous waveforms for 18 months, (ii) an event catalogue for the same period, and
(iii) a reanalysis product for the region. State the plan for each service (windows,
rates, totals from stated assumptions), the adapters, the caching and the archive, and
the completeness gate per service. State the one thing you cannot control.

**★★★8.** The lesson's plan model assumes a constant rate limit and uniform daily
volume. Design a measurement that characterises a real service's effective limits
before a large fetch: state what you probe, the statistic, the cost of the probe, and
the two ways the measurement could mislead you. State what you must do with the
result.

**★★★9.** A service announces that it will reprocess its archive next year, changing
magnitudes and adding stations. Specify the repository practice that would let a
reader in three years tell whether a published result used the old or the new
processing, and state what that practice costs per year for a 2 TB/year ingest. State
what the practice cannot guarantee.
