---
id: 22-03-04
title: "Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)"
level: graduate
prereqs: ["22-03-03", "03-10-08"]
estimated_minutes: 50
tags: [data-access, fdsn, earthdata, copernicus, provenance, data-engineering]
---

# Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a data service as a query interface with limits, and **state** why a
   query is a moving target where an archive is not.
2. **Model** a fetch as requests plus bytes, and **compute** the total time of a plan
   under latency, transfer and rate limits.
3. **Choose** a window length from the service's cap and the binding constraint, and
   **state** which constraint binds at a given plan.
4. **Compute** the cost of retries for a flaky service and **explain** why a partial
   archive is worse than a failed fetch.
5. **Record** the request plan, the service's own version identifiers and a checksum
   per response, so a fetch can be reconstructed and audited.
6. **Diagnose** the four access failures — silent truncation, rate-limit throttling,
   response version drift, and unchecked completeness — from their symptoms.

The service model in this lesson — per-request latency, window cap, transfer rate,
rate limit and failure probability — is **SYNTHETIC** with chosen values, and the
endpoint families are described generically. No service was called, no API key was
used, and no published performance figure or service limit is quoted: every service's
actual limits must be read from its documentation at the time of use.

## Prerequisites

- [22-03-03 Designing Robust Data Pipelines for Earth Data](./03-data-pipelines.md) —
  the retries, gates and reconciliation this lesson's fetch feeds.
- [03-10-08 FDSN Clients and Data Requests](../../03-scientific-computing/10-obspy-and-seismic-data/08-fdsn-clients.md) —
  the library-level introduction to waveform clients.

## 1. Intuition: a query is a moving target

A field recording on a disk is a fixed artefact. A *query* to a data service returns
whatever the service holds at the moment it is asked, processed by whatever software
version it runs. This is the single most important difference between downloading a
file and fetching from an API, and it has two consequences:

- **The result is not an archive.** "We downloaded the catalogue for 2019" is not a
  reproducible description unless the retrieval is dated, the request is recorded, and
  the response is checksummed — because the same query a month later can return a
  different set (reprocessed events, revised magnitudes, new stations).
- **Completeness is a claim, not a default.** A fetch that returns *some* of the
  requested window looks exactly like a fetch that returned all of it, unless the plan
  says how many records were expected and the response is checked against that number.

Everything the lesson measures follows from treating a fetch as an operation with a
plan, a cost and a completeness obligation.

## 2. The service families, described generically

Earth-science data services differ in subject (waveforms, events, imagery, reanalysis)
but share a structure worth knowing:

| Aspect | What to establish from the documentation |
|---|---|
| Query axes | time window, spatial extent, channel/variable, level of processing |
| Window cap | the maximum span one request may ask for |
| Rate limit | requests or bytes per unit time, and per what (IP, key, user) |
| Bulk route | whether a request may ask for a whole day, month or granule |
| Identifier scheme | how a returned granule or record is named and versioned |
| Reproducibility notes | whether the service publishes processing versions and change logs |
| Credit and licence | attribution requirements, and what may be redistributed |

The two operational facts to extract first are the **window cap** and the **rate
limit**, because they determine the shape of the fetch plan. Both change over time, so
they belong in the fetch record rather than in a script's constant.

Waveform services (the FDSN family), the Earthdata family of archives and the
Copernicus services each fix these differently, and a group that uses all three
usually ends up writing one thin adapter per service — which is exactly what the
stage decomposition of
[22-03-03](03-data-pipelines.md) §7 anticipates.

## 3. The cost of a fetch plan

Model a fetch as $n$ requests, each paying a fixed latency $\ell$, plus a transfer of
the total payload at rate $B$:

$$T = n\,\ell + \frac{S}{B}, \qquad
n = \left\lceil \frac{T_{\text{span}}}{w} \right\rceil,$$

where $w$ is the window length and $S$ the total data volume. The demonstration's
**SYNTHETIC** service fetches 365 days of a 40 MB/day stream with $\ell = 1\ \text{s}$
and $B = 5\ \text{MB/s}$:

| Window (days) | Requests | Latency (s) | Transfer (s) | Total (s) |
|---|---|---|---|---|
| 1 | 365 | 365.0 | 2920.0 | 3285.0 |
| 7 | 53 | 53.0 | 2920.0 | 2973.0 |
| 30 | 13 | 13.0 | 2920.0 | 2933.0 |

The transfer cost is fixed by the volume; the latency cost scales with the request
count. This is why **the window cap is the most valuable number in the service's
documentation**: moving from one-day windows to the 30-day cap saves 352 seconds of
pure overhead on this fetch, and the saving grows linearly with the span and the
latency.

Two refinements make the model useful in practice:

$$T_{\text{plan}} = \max\left(n\,\ell + \frac{S}{B}, \ \frac{n}{r}\right),$$

where $r$ is the rate limit in requests per second. In the demonstration's plan the
13 requests at 60 requests per minute give a floor of 13.0 s, far below the 2933 s of
transfer, so the binding constraint is latency plus transfer. A plan that fetches
many small windows from a strict service can invert this, and quoting only the
transfer time then misleads: the rate limit decides.

## 4. Failure, retries, and why partial is worse than absent

Services fail, throttle and time out. With a per-request failure probability $p$ and
$R$ retries, the probability that at least one request of a plan fails at least once
is

$$P(\text{at least one failure}) = 1 - (1-p)^{n},$$

which for $n = 13$ and $p = 0.05$ is **0.487**. Left unhandled, that is a coin flip on
whether the archive is complete. The retry cost is small and computable: the expected
attempts per request are $\sum_{k \le R} p^{k} = 1.0525$, so 13 requests cost 0.7
extra requests and 0.7 s of extra latency — 5.25 % more time against a 49 % chance of
an incomplete archive.

The subtlety is what a *partial* archive does downstream. A missing day in a waveform
archive propagates as a gap in a spectrum, and a gap in a spectrum is easy to
misread as a physical absence of energy. This is why the correct design is not merely
"retry" but **"retry, and then reconcile"**: the fetch's plan states how many windows
were requested, and the pipeline's gate asserts that all of them arrived
([22-03-03](03-data-pipelines.md) §6).

## 5. Making a fetch reproducible

A fetch is reproducible when a reader can re-run it and obtain the same data, or can
explain why not. Five fields are required:

1. **The plan**: the list of requests (time windows, spatial extent, channel or
   variable, level), in the order attempted, with the window length and the cap in
   force.
2. **The service identity**: the endpoint family, the query interface version, the
   service's own processing version or change-log identifier for the response.
3. **The retrieval timestamp**: when each request was made, in UTC.
4. **A checksum per response**, so a re-fetch can be compared rather than trusted.
5. **The failure log**: which windows failed, how many attempts, and the terminal
   outcome (arrived, arrived after retry, or recorded as missing).

Fields 2 and 3 are the ones most often omitted and the ones that explain a
discrepancy: a service that reprocessed its archive will return different bytes for
the same query, and without the timestamp and version identifier you cannot tell
whether the difference is your error or theirs.

## 6. Practice: fetching without losing control

1. **Read the limits, then plan.** Window cap and rate limit first, from the
   documentation, recorded with the fetch.
2. **Prefer the bulk route.** If the service offers day- or granule-level requests,
   use them: fewer requests, fewer failure opportunities, less overhead (§3).
3. **Fetch by identifier when possible.** A named granule is a stable target; a query
   is not.
4. **Check completeness against the plan.** One gate, one comparison, per fetch.
5. **Cache locally and never re-query for a figure.** A figure must be reproducible
   from the archived bytes, not from a repeat query
   ([22-02-05](../02-reproducible-workflows/05-data-versioning.md)).
6. **Respect the service.** Backoff with jitter on throttle responses, a bounded
   concurrency, and an identifying contact string: a group's scripts are guests, and
   one runaway loop can get an institution throttled.
7. **Version the adapter.** The code that speaks to a service changes when the service
   changes; keep it thin, tested and separate from the analysis.

## 7. Worked example: an archive that cannot be rebuilt

A group's published figure uses a 2016–2019 waveform archive retrieved in 2020 from a
service that has since reprocessed its data. The figure must be checked.

1. **Can the original fetch be repeated?** Only if the plan and the retrieval record
   exist. In this case none of the five fields of §5 were kept, so the original bytes
   cannot be identified; the request can be re-made, but the response is now the
   reprocessed version.
2. **What can be established?** Whether the *result* is sensitive to the
   reprocessing: re-run the analysis on the current data and compare with the
   published numbers, and, if any station's raw files were archived locally, compare
   those against the service's current copies to size the change.
3. **What would have prevented it?** Fields 2–4 of §5 — the service's processing
   version, the retrieval date and a checksum per response — plus a copy of the bytes
   that mattered, which for a figure is usually a modest subset.
4. **What is the honest report?** "The analysis was re-run on the current archive; the
   quantity changed by X, which is (or is not) within the stated uncertainty; the
   original bytes were not archived and could not be recovered." That paragraph is a
   scientific result; a claim of reproduction without the bytes is not.

## Assumptions and regime of validity

1. **Latency and bandwidth are chosen constants.** Real latencies depend on the
   service, the payload and the network; the structure (latency × requests + volume /
   bandwidth) is what generalises.
2. **A constant rate limit.** Real limits are often per-key, per-IP and bursting, and
   a shared institutional address changes what a single user may do; measure the
   effective limit and record it.
3. **Uniform data volume per day.** Real streams have gaps, outages and varying
   channel counts, so the transfer time is an estimate and the plan must tolerate
   variation.
4. **Service semantics are stable within a fetch.** A mid-fetch schema change (a new
   channel code, a revised magnitude) produces internally inconsistent data; a plan
   that spans a maintenance window should record it.
5. **The lesson does not state any service's real limits.** Capacities, caps and
   policies change and must be read from the documentation of the service in use; no
   number here should be quoted as a service's behaviour.

## The honest summary

Programmatic access replaces a fixed file with a query whose result depends on when it
is asked and what the service currently holds. The arithmetic of a fetch is simple —
$n$ requests times latency plus volume over bandwidth — and it makes the window cap the
most valuable number in a service's documentation: 365 daily requests cost 3285 s
where 13 monthly-cap requests cost 2933 s for the same 2920 s of transfer. With a 5 %
per-request failure rate, a 13-request plan has a 48.7 % chance of at least one
failure, so retries (5.25 % extra time) and, crucially, a completeness gate are not
optional. The reproducibility of a fetch rests on five recorded fields — plan, service
version, retrieval time, checksums and failure log — and their absence is what turns a
late-discovered discrepancy into an unrecoverable one.

## Python demonstration

[`code/getting_earth_data_demo.py`](./code/getting_earth_data_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the fetch plan for 365 days at 1-, 7- and 30-day windows, with requests, latency,
   transfer and totals (3285.0 s, 2973.0 s, 2933.0 s);
2. which constraint binds at the cap, including the 13.0 s rate-limit floor;
3. the retry arithmetic for a 5 % per-request failure rate (48.7 % chance of a
   failure, 1.0525 attempts per request);
4. the five fields a fetch must record to be reproducible.

```bash
cd 22-data-engineering-reproducibility/03-data-formats-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python getting_earth_data_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/04-getting-earth-data-exercises.md`](./exercises/04-getting-earth-data-exercises.md)
and
[`exercises/04-getting-earth-data-solutions.md`](./exercises/04-getting-earth-data-solutions.md).

## Mastery checkpoint

Without notes: a service caps a request at 7 days, limits a user to 30 requests per
minute, and serves data at 3 MB/s with a 1.5 s per-request latency. You need two years
of a 25 MB/day stream.

1. Compute the number of requests, the latency total, the transfer total and the
   plan's total time.
2. Compute the rate-limit floor and state which constraint binds.
3. Compute the probability that at least one request fails if the per-request failure
   probability is 0.04, and the expected extra time with two retries.
4. State the five fields you would archive with the fetch, and the gate that would
   catch a missing week.

## Common pitfalls

1. **Treating a query as an archive.** The same query later returns a different set.
2. **Ignoring the window cap.** Daily requests cost 352 s more overhead than monthly
   ones on the demonstration's fetch.
3. **Quoting transfer time without the rate-limit floor.** Some plans are
   request-bound, and the transfer time then says nothing useful.
4. **Retrying without reconciling.** Retries reduce the chance of a gap; only a count
   gate detects one that survived.
5. **Re-querying for a figure.** A figure must come from archived bytes, not from a
   fresh request.
6. **Not recording the service's processing version.** A reprocessing at the service
   is indistinguishable from your own error without it.

## Where this is used

- **Waveform and catalogue archives** — the FDSN service family, with clients that
  wrap the query interface:
  see [03-10-08 FDSN Clients and Data Requests](../../03-scientific-computing/10-obspy-and-seismic-data/08-fdsn-clients.md).
- **Earth-observation archives** — granule-level retrieval and ordering workflows:
  see [17-07 Earth Observation Data](../../17-remote-sensing-gis/07-earth-observation-data/README.md).
- **Data management planning** — retention and licensing for fetched data:
  see [22-05-04 Research Data Management Plans and FAIR Principles](../05-collaboration-and-project-management/04-research-data-management-plan.md).
- **Cloud-native access** — the same windowed-read arithmetic against object stores:
  see [22-04-05 Cloud-Native Geoscience Data Access](../04-databases-and-large-data/05-cloud-native-geoscience.md).

## Related lessons

- [22-03-03 Designing Robust Data Pipelines for Earth Data](./03-data-pipelines.md) —
  what happens to the fetched data downstream.
- [22-03-05 Automated Quality Control and Flagging](./05-data-quality-control.md) —
  the checks that catch a truncated or shifted response.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the identifiers a fetch record feeds into.
- [22-03-06 Metadata Standards and Controlled Vocabularies](./06-metadata-standards.md) —
  the station and channel vocabularies that make a query meaningful.

## Self-assessment checklist

- [ ] I can describe a service as a query interface with caps and limits.
- [ ] I can compute a fetch plan's time from requests, latency and volume.
- [ ] I can identify the binding constraint of a plan.
- [ ] I can compute the failure probability of a multi-request fetch.
- [ ] I can list the five fields a reproducible fetch records.
- [ ] I can name the access failures and their symptoms.
