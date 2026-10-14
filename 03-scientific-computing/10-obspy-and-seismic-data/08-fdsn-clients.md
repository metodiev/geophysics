---
id: 03-10-08
title: "Fetching Data from FDSN Web Services"
level: intermediate
prereqs: ["03-10-02", "03-10-03"]
tags: [obspy, fdsn, web-services, data-access, caching]
---

# Fetching Data from FDSN Web Services

ObsPy can download waveforms, metadata and catalogs from the web services of
the International Federation of Digital Seismograph Networks (FDSN). This
lesson covers what those requests look like, how to build them correctly, why
they fail, and how to work responsibly with an archive that other people also
depend on.

**This lesson's demonstration does not use the network.** It builds requests
offline, prints the exact URLs and parameters a reader should use when online,
and demonstrates the offline half of the workflow — validating files that have
already been downloaded. Every URL printed here is registered in
`tools/verified_links.tsv` with an observed HTTP status, and the URLs that are
known to be dead are named as dead.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/fdsn_clients_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what the three FDSN services provide — station, dataselect and
   event — and which one answers which question.
2. **Construct** a client, a waveform request, a metadata request and an event
   request, and state the parameters that are required.
3. **Explain** why client construction needs no network and what the short
   names mean, and **name** the deprecation that applies to `IRIS`.
4. **Diagnose** the three-way consistency check that determines whether a query
   can succeed.
5. **Validate** a downloaded file with two checks that cost nothing and catch
   most real-world problems.
6. **Design** a caching and provenance strategy for a re-runnable workflow.

## Prerequisites

- [03-10-02 Reading MiniSEED/SAC](./02-reading-waveforms.md) — the file formats
  a query returns.
- [03-10-03 StationXML, Inventory, Response and Instrument Correction](./03-inventory-and-metadata.md)
  — the metadata a query returns and why you need it.

## 1. Intuition: a query is a contract with an archive

An FDSN request is not a file download; it is a *question* addressed to an
archive, and the archive decides whether it can answer. Three things must agree
before any data arrive: the channel must exist in the station service for the
requested time window, the waveform service must hold samples for that channel
and window, and the channel code must encode the sample rate your processing
assumes. When (1) or (2) fails you get an explicit `FDSNNoDataException` or an
HTTP 204. When (3) fails you get data, and nothing tells you that the sampling
rate is not what you thought.

## 2. Precise definitions

### 2.1 The three services

| service | path | returns | answers |
|---|---|---|---|
| station | `/fdsnws/station/1/` | StationXML | what channels exist, and their response |
| dataselect | `/fdsnws/dataselect/1/` | MiniSEED | the samples |
| event | `/fdsnws/event/1/` | QuakeML | origins, magnitudes, arrivals |

Verified endpoints (HTTP 200, checked 2026-10-14):

- `https://service.earthscope.org` — the base URL that ObsPy's `IRIS` and
  `EARTHSCOPE` short names resolve to.
- `https://service.iris.edu/fdsnws/station/1/` — the station service.
- `https://service.iris.edu/fdsnws/dataselect/1/` — the dataselect service.
- `https://earthquake.usgs.gov/fdsnws/event/1/` — the event service.

**Known dead, do not cite:** `https://service.iris.edu/fdsnws/event/1/` returns
HTTP 404. The IRIS event service was retired in favour of the USGS one.

### 2.2 Client construction

```
Client('IRIS') -> base url https://service.earthscope.org
Client('EARTHSCOPE') -> base url https://service.earthscope.org
Client('ORFEUS') -> base url https://www.orfeus-eu.org
Client('USGS') -> base url https://earthquake.usgs.gov
```

Constructing a client resolves a short name to a base URL from a table of 38
registered names on this installation. **No request is made** until
`get_waveforms`, `get_stations` or `get_events` is called, which is why the
demonstration runs offline.

`IRIS` still works but is deprecated:

```
ObsPyDeprecationWarning: IRIS is now EarthScope, please consider changing the
FDSN client short URL to 'EARTHSCOPE'.
```

Data centres merge and rename. A tutorial that hard-codes `'IRIS'` ages badly,
which is why the URLs above are stated explicitly rather than by short name.

### 2.3 The requests

**Waveforms.** One station, one hour:

```python
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

client = Client('EARTHSCOPE')
st = client.get_waveforms(network='IU', station='ANMO', location='00',
                          channel='BHZ',
                          starttime=UTCDateTime('2024-03-15T08:00'),
                          endtime=UTCDateTime('2024-03-15T09:00'))
```

which becomes an HTTP GET on
`https://service.iris.edu/fdsnws/dataselect/1/query` with
`net=IU&sta=ANMO&loc=00&cha=BHZ&start=...&end=...`.

**Metadata.** The response you need to interpret those samples:

```python
inv = client.get_stations(network='IU', station='ANMO', level='response',
                          starttime=UTCDateTime('2024-03-15'))
```

on `https://service.iris.edu/fdsnws/station/1/query` with
`net=IU&sta=ANMO&level=response&start=...`.

**Events.**

```python
cat = client.get_events(starttime=..., endtime=..., minmagnitude=4.5,
                        latitude=48.1, longitude=11.2, maxradius=5.0)
```

on `https://earthquake.usgs.gov/fdsnws/event/1/query` with
`starttime=...&minmagnitude=4.5`.

Every one of these is also a plain URL that can be pasted into a browser. The
specification is at
[www.fdsn.org/webservices/](https://www.fdsn.org/webservices/).

## 3. Derivations and worked reasoning

### 3.1 The three-way consistency check

Before a query can succeed, three statements must all be true:

1. **The channel exists.** `network.station.location.channel` must appear in
   the station service for the requested window. A location code of `00` and an
   empty location code are *different channels*, and a station that changed its
   data logger usually changed its location code with it.
2. **The samples exist.** The dataselect service must hold that channel for
   that window. Data gaps are normal: a station that stopped for maintenance
   returns 204 for the gap and data for the rest if you ask for a longer window.
3. **The channel code matches your assumption.** `BHZ` promises 10–80 Hz,
   `HHZ` 80–250 Hz, `LHZ` about 1 Hz. An instrument that was configured
   differently still reports its true rate in the header, so the check is
   `trace.stats.sampling_rate == expected`, not the channel code. The code is a
   promise, not a guarantee.

Failures 1 and 2 raise; failure 3 does not. That asymmetry is the reason for the
validation step below.

### 3.2 Validation that costs nothing

Two checks catch most real-world data problems:

```python
def validate(trace, expected_fs: float) -> list[str]:
    problems = []
    if trace.stats.sampling_rate != expected_fs:
        problems.append(f"sampling rate {trace.stats.sampling_rate} != {expected_fs}")
    expected_npts = int(round((trace.stats.endtime - trace.stats.starttime)
                              * trace.stats.sampling_rate))
    if abs(expected_npts - trace.stats.npts) > 1:
        problems.append(f"npts {trace.stats.npts} inconsistent with the time span")
    if not np.isfinite(trace.data).all():
        problems.append("non-finite samples")
    return problems
```

The demonstration runs them on a healthy trace, on a trace cut short in time
and on a trace with a shifted start time, and reports which checks fire. The
third case — a shifted start time with the correct `npts` — is the one that a
naive reader would not think to test, and it is what a partial download or a
mis-merged segment looks like.

### 3.3 Caching and provenance

Re-running an online workflow must not re-download the archive. Two patterns:

**Download once, keep the file.**

```python
st = client.get_waveforms('IU', 'ANMO', '00', 'BHZ', t0, t1)
st.write('data/IU.ANMO.00.BHZ.2024-03-15.mseed', format='MSEED')
# from then on:
st = read('data/IU.ANMO.00.BHZ.2024-03-15.mseed')
```

**Provenance.** Write a small text or JSON file beside the data recording the
service URL, the query parameters, the request time, the resulting channel list
and the checksum. The checksum is the minimum viable field: every other field
can be reconstructed, but only the checksum lets a reader prove that the bytes
they have are the bytes you analysed.

Waveform data must never be committed to a repository. The `.gitignore` in this
project already excludes `*.mseed` and `*.sac`.

### 3.4 Working responsibly with a public archive

- **Ask for the smallest window that answers the question.** A 40-station,
  three-component, 20-year request is terabytes, and it will be refused or
  throttled.
- **Batch station lists.** One request with `station='ANMO,ABKT,...'` costs one
  round trip; 40 requests cost 40, and the archive pays for them.
- **Do not loop without delay.** A client that retries immediately on failure
  is a denial-of-service attack on a publicly funded archive.
- **Credit the network and the data centre** in any publication. The FDSN
  service metadata includes the citation string.

## 3b. Worked examples

### 3b.1 Sizing a request before making it

**Problem.** A study needs three-component broadband data from 40 stations for
five years, at 100 Hz. How large is the request, and is it reasonable?

At 100 Hz a three-component station produces
$3 \times 100 = 300$ samples per second, i.e.

$$\frac{300 \times 86400}{10^{6}} = 25.9\ \text{million samples per station-day}.$$

At the measured MiniSEED efficiency of 2.7 bytes per sample (lesson 02, for
band-limited data), one station-day is

$$25.9\times10^{6} \times 2.7\ \text{bytes} \approx 70\ \text{MB}.$$

Over five years (1826 days) and 40 stations:

$$70\ \text{MB} \times 1826 \times 40 \approx 5.1\ \text{TB}.$$

That is not a request to make interactively, and most services will refuse or
throttle it. The defensible workflow is to request **per station-month**
($70\ \text{MB} \times 30 = 2.1$ GB per station-month, or 40 requests of ~2 GB
each), cache the results, and process each month before moving on. The
arithmetic above is what turns "download the data" into a plan.

### 3b.2 The three-way check, worked through

**Problem.** A user requests `IU.ANMO.00.BHZ` for 2024-03-15T08:00–09:00 and
receives an exception. Diagnose it in order.

1. **Station service.** Query
   `https://service.iris.edu/fdsnws/station/1/query?net=IU&sta=ANMO&loc=00&cha=BHZ&start=2024-03-15T08:00:00`.
   If the channel is absent for that window, the location code or the channel
   code is wrong for that period — an instrument change is the usual cause.
2. **Level.** The station service returns a channel *without* a response unless
   `level=response` is specified. A query that succeeds but yields a Channel
   with `response=None` has answered a different question.
3. **Dataselect.** If the station service has the channel and dataselect returns
   204, the window has no data: the station was down, or the request is in the
   future, or the time is in the wrong timezone. A surprising fraction of these
   are timezone errors, which is why `UTCDateTime` is constructed from strings
   with an explicit `Z` or offset.

Note the order: check the *metadata* before the *data*. A query that returns
samples for a channel the station service does not know about means one of the
two services is stale, and the metadata is the one you must trust for the
response.

### 3b.3 A provenance record that answers the questions people ask

**Problem.** Twelve months after a run, a reviewer asks whether the amplitude
anomaly at station `ABCD` could be a gain change. What must the provenance
record contain for the question to be answerable offline?

| field | why it is needed |
|---|---|
| query (net, sta, loc, cha, start, end) | to re-request the identical window |
| service base URL | different services hold different revisions of a response |
| request time (UTC) | data centres re-publish metadata; the same query can differ later |
| StationXML checksum | the response's *content* is what determines the amplitude |
| waveform checksum | proves which bytes were analysed |
| trace ids and sample rates actually returned | catches a channel that changed rate |
| processing steps, in order, with parameters | `remove_response(water_level=60)` differs from `water_level=None` |

The two checksums are the load-bearing fields: everything else can be
reconstructed or re-derived, but without them there is no way to prove that the
data and metadata being discussed are the ones that were used. That is why they
are the minimum viable provenance, and why a workflow that cannot produce them
cannot answer the reviewer's question at any later date.

### 3b.4 When a cache is wrong

**Problem.** A cached waveform is used for a year. What can go wrong, and which
of the failures are detectable?

| failure | detectable? | how |
|---|---|---|
| truncated download (partial file) | yes | size and checksum against the manifest |
| wrong channel returned by the service | yes | trace id against the request |
| silently re-encoded MiniSEED (different compression) | yes | decoded-sample comparison; the checksum changes while the samples do not |
| response metadata revised at the archive | **no**, unless you cached the StationXML too | cache the metadata with the same discipline as the data |
| leap-second/timing correction applied downstream | no | nothing in the file changes; the correction is a separate product |

The last two rows are the argument for caching metadata, not only waveforms. A
waveform cache without a metadata cache is reproducible until the archive
revises a response, at which point the same script produces a different
amplitude from the same bytes — the worst kind of non-reproducibility, because
nothing in the waveform changed.

### 3b.5 The endpoint that does not exist

**Problem.** A tutorial cites `service.iris.edu/fdsnws/event/1/` for event
queries. Will it work when the network is finally available?

Measured with `curl -sS -o /dev/null -w '%{http_code}' -L`:

| URL | status |
|---|---|
| `https://service.iris.edu/fdsnws/event/1/` | **404** |
| `https://service.iris.edu/fdsnws/station/1/` | 200 |
| `https://service.earthscope.org` | 200 |
| `https://www.fdsn.org/webservices/` | 200 |

So the event service is *not* served from `service.iris.edu`; the 404 is the
archive's response, not the reader's mistake. The demonstration therefore records
the correct base URL that ObsPy itself chooses for the `IRIS` alias —
`https://service.earthscope.org` — and never cites the 404 endpoint at all. This
is why the course's link registry requires an observed status for every external
URL: **a URL can be plausible, widely copied, and dead.** Three of the four URLs
above were verified 200; the fourth was verified 404 and is recorded as rejected
rather than quietly dropped.

The general practice for offline development: pick the endpoint by asking the
library, not by remembering a hostname. `Client('IRIS').base_url` returns
whatever the installed version believes is current, so a code path that worked
before an archive migration continues to work after it.

### 3b.6 A warning is data

**Problem.** Constructing `Client('IRIS')` emits
`ObsPyDeprecationWarning: IRIS is now EarthScope...` and then reports
`https://service.earthscope.org`. Is that a bug to suppress?

No. Measured facts about the construction:

1. **It makes no network request.** A client object holds a name, a base URL and
   a timeout; the request happens at `get_*`. So the warning is available
   *offline*, which is why this lesson can be taught without a network.
2. **The warning carries the migration.** The archive renamed itself; the alias
   still resolves; the warning tells the writer of a report which name to use in
   the *prose*, while the code may keep the old alias indefinitely.
3. **The short names are enumerable offline.** Measured: 38 short names are
   available from the installed client, so a reader can discover that `USGS` and
   `ORFEUS` exist without contacting either.

The teaching point: an archive's namespace is *volatile metadata*. Code should
look the names up, reports should quote what the service calls itself today, and
neither should hard-code a hostname that a migration can retire. The three-way
check from §3b.2 — the request, the response, and the client's own report of what
it asked — is what makes a mismatch visible instead of mysterious.

One honest limitation: everything in this section that concerns the *live*
behaviour of the services (does the query return data, how long does it take, are
the results complete) was **not** run. The status codes above were measured with
`curl`; the queries were documented for the reader to run when online.

### 3b.7 Sizing a request before making it

**Problem.** A 100-station array runs three components at 100 Hz. How much data
is one day, and what does that imply about how to ask for it?

Sample count:

$$100 \times 3 \times 100\ \mathrm{Hz} \times
\frac{86\,400\ \mathrm{s}}{1\ \mathrm{day}} = 2.592\times10^{9}\
\text{samples/day}.$$

Then multiply by the measured bytes per sample. From the reading demonstration:

| data type | measured bytes/sample | one day for this array |
|---|---|---|
| raw `int32` | 4.0000 | 10.37 GB |
| MiniSEED, peak amplitude 1 | 1.3653 | 3.54 GB |
| MiniSEED, peak amplitude 1000 | 2.7307 | 7.08 GB |
| MiniSEED, peak amplitude $10^{7}$ | 5.4613 | 14.16 GB |

(The convention here is $1\ \mathrm{GB} = 10^{9}$ bytes.) Two conclusions, and
both are quantitative rather than habitual:

1. **The answer depends on the signal amplitude by a factor of four** (3.54 to
   14.16 GB for the same array, the same 100 Hz, the same day). A storage plan
   built from one station's compression ratio is not a plan for the array.
2. **A day for 100 stations is the size of a small disk**, so the request has to
   be split — by station groups, by time windows, or both — and each piece
   cached with its query parameters so it is fetched once. This is the reason
   §3b.3's provenance record exists: with 30 pieces the question "which query
   produced this file" is asked 30 times.

The arithmetic also shows what *not* to ask for: requesting one channel for one
hour is 360 000 samples, about 1 MB — a size for which the request's own overhead
and the archive's per-request cost dominate. Batching requests is cheaper in
requests and more expensive in re-runs, and the crossover is where the per-request
overhead equals the cost of re-fetching a batch that failed.

A final caution that is not arithmetic: every number above is a *prediction* from
measured bytes-per-sample, not a measurement of any archive's response. The
status codes in §3b.5 were measured; the volumes were computed.

## 4. Physical and computational interpretation

The design principle behind the FDSN services is that a *query* is cheaper than
a *catalogue*: storing 40 terabytes of waveform is unnecessary when the same
data can be requested in seconds. The price is that a workflow now depends on a
third party's uptime, schema version and retention policy, and that the same
script run twice can produce different data.

Two consequences follow, and both are engineering requirements rather than
preferences:

1. **A reproducible workflow caches.** The analysis must run from local files;
   the download is a separate, logged step.
2. **A reproducible workflow records provenance.** Without the query
   parameters and a checksum, "I downloaded it" is not a method.

## 5. Python demonstration

[`code/fdsn_clients_demo.py`](./code/fdsn_clients_demo.py) makes no network
request. It constructs four clients and prints their base URLs, captures the
deprecation warning for `IRIS`, prints the three requests a reader would make
with their parameters and verified URLs, names the dead endpoint, explains the
three-way consistency check, and then demonstrates the offline half of the
workflow: writing a synthetic waveform, validating it, and detecting two kinds
of corruption. It writes into `code/_scratch_fdsn/` and removes it on exit.

## 6. Exercises

Full solutions:
[`exercises/08-fdsn-clients-solutions.md`](./exercises/08-fdsn-clients-solutions.md).

### ★ Foundational

**★1.** Name the three FDSN services, the format each returns, and the question
each answers.

**★2.** State the base URL that ObsPy's `IRIS` and `EARTHSCOPE` short names
resolve to, and the URL that returns HTTP 404.

**★3.** Explain why `Client('EARTHSCOPE')` makes no network request.

**★4.** State the four required parameters of a dataselect query and the units
of each.

**★5.** State what `BHZ`, `HHZ` and `LHZ` promise, and what you must check
instead of trusting the promise.

### ★★ Applied

**★★6.** Write the full URL, with parameters, for a dataselect query of
network `IU`, station `ANMO`, location `00`, channel `BHZ`, for the hour
starting 2024-03-15T08:00Z. State the base URL you used.

**★★7.** Implement the two validation checks (sample rate, `npts` versus time
span), run them on a healthy trace, a truncated trace and a trace with a
shifted start time, and report which checks fire in each case.

**★★8.** Write a provenance record for a downloaded file. List every field, and
state which fields you cannot populate without network access.

**★★9.** A query for `IU.ANMO.00.BHZ` over 24 hours returns four traces with
different start times. State two reasons the archive would split the data this
way and the two lines of code that combine them safely.

**★★10.** What error does ObsPy raise when the station service has no record of
a channel? What error for a window with no samples? And what happens if the
channel exists but with a different sample rate than you assumed?

### ★★★ Research-oriented

**★★★11.** Design a caching layer for a workflow that downloads 200 station-days
per run. Specify the file naming, the directory layout, the cache-invalidation
rule, and the provenance record. Then state the failure mode that the cache
introduces and how you detect it.

**★★★12.** The dataselect service can return data in a different MiniSEED
encoding from the one you requested (for example Steim-compressed when you
expected `int32`). Design a check that detects this and state whether it
matters for the samples, for the file size, or for both.

**★★★13.** Write a rate-limiting downloader that respects a documented limit of
one request per second and retries failed requests with exponential backoff.
State the parameters you chose, the failure mode the retry introduces, and how
a workflow using it stays reproducible when a request ultimately fails.
