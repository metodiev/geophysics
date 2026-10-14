# Solutions — 03-10-08 Fetching Data from FDSN Web Services

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output. **These solutions were not verified against a live
> service**: this machine's demonstration makes no request, and where a live
> value would be needed the answer states the uncertainty rather than inventing
> a number.

---

## ★1 — The three services

| service | path suffix | returns | answers |
|---|---|---|---|
| station | `/fdsnws/station/1/` | StationXML | which channels exist, with what response and for what time window |
| dataselect | `/fdsnws/dataselect/1/` | MiniSEED | the samples |
| event | `/fdsnws/event/1/` | QuakeML | origins, magnitudes, arrivals |

---

## ★2 — Base URLs

```
Client('IRIS')       -> https://service.earthscope.org
Client('EARTHSCOPE') -> https://service.earthscope.org
```

`https://service.iris.edu/fdsnws/event/1/` returns **HTTP 404** — the IRIS
event service was retired in favour of the USGS event service at
`https://earthquake.usgs.gov/fdsnws/event/1/`. Also dead:
`https://service.iris.edu/fdsnws/event/1/query`, verified 404.

---

## ★3 — Why no request is needed

Constructing a `Client` resolves a short name against a table embedded in
ObsPy and constructs a `RequestsClient` object. The service is contacted only
when a method that needs data is called. On this installation the table has
**38** entries, including `AUSPASS`, `BGR`, `BGS`, `EARTHSCOPE`, `EIDA` and
`USGS`.

The measurement that confirms it: the demonstration runs with no network access
and prints all four base URLs, including `https://service.earthscope.org` for
both `IRIS` and `EARTHSCOPE`.

---

## ★4 — Dataselect parameters

| parameter | meaning | unit |
|---|---|---|
| `net` | network code | — |
| `sta` | station code | — |
| `cha` | channel code | — |
| `start` | start time | UTC instant |
| `end` | end time | UTC instant |

plus `loc` (location code, which may be empty but must be specified when it is
not). The metadata comes from the **station** service, requested separately with
`get_stations(..., level='response')`.

---

## ★5 — What channel codes promise

| code | promise |
|---|---|
| `BHZ` | broadband, 10–80 Hz sample rate, vertical |
| `HHZ` | high broadband, 80–250 Hz sample rate, vertical |
| `LHZ` | long period, ~1 Hz sample rate, vertical |

The promise is a convention, not a guarantee: an instrument reconfigured to a
different rate keeps the code it was assigned until someone changes it.
**Check `trace.stats.sampling_rate` on every trace you receive**, and compare
it with the rate your processing assumes.

---

## ★★6 — A complete dataselect URL

```
https://service.iris.edu/fdsnws/dataselect/1/query
    ?net=IU&sta=ANMO&loc=00&cha=BHZ
    &start=2024-03-15T08:00:00&end=2024-03-15T09:00:00
```

Base URL: `https://service.iris.edu/fdsnws/dataselect/1/` (verified HTTP 200 on
2026-10-14). The observed behaviour of the response — number of records, exact
byte count, HTTP status — cannot be stated offline and is deliberately not
quoted here. The station service for the same channel would be

```
https://service.iris.edu/fdsnws/station/1/query?net=IU&sta=ANMO&level=response
```

---

## ★★7 — Three validation cases

| trace | sample-rate check | `npts` vs time-span check |
|---|---|---|
| healthy (3600 samples, 100 Hz, 36 s span) | passes | passes |
| truncated to 100 samples, start/end unchanged | passes | **fires**: the span implies 3600 samples |
| start time shifted by 5 s, `npts` correct | passes | **fires**: the span implies 3100 samples |

The third case is the dangerous one because **nothing else is wrong**: the
sample rate is right, the dtype is right, the samples are finite, and the data
are intact — they are simply 5 s later than the metadata claims. A reader who
checks `npts` against the array length (a natural check) sees agreement, and a
reader who plots the trace against time gets a shifted waveform with no warning.
The only check that catches it compares the *metadata* against *itself*,
which is why the time-span test is worth its two lines.

---

## ★★8 — A provenance record

```json
{
  "file": "IU.ANMO.00.BHZ.2024-03-15T08-00.mseed",
  "bytes": 163840,
  "sha256": "<64 hex characters>",
  "service": "https://service.iris.edu/fdsnws/dataselect/1/",
  "query": {"net": "IU", "sta": "ANMO", "loc": "00", "cha": "BHZ",
            "start": "2024-03-15T08:00:00", "end": "2024-03-15T09:00:00"},
  "requested_at": "2024-03-16T09:12:44Z",
  "trace_ids": ["IU.ANMO.00.BHZ"],
  "npts": [360000],
  "recorded_at": "2024-03-16T09:12:45Z"
}
```

**Cannot be populated offline:** `service` (a network endpoint's identity),
`query` (a request that was not made) and `requested_at`. Everything else —
file name, size, checksum, trace ids from the file's own headers, sample
counts — is a property of the bytes and can be computed with no network at all.

That asymmetry is the point: a provenance record is *mostly* reproducible from
the data, and the fields that are not are exactly the ones that say where the
data came from.

---

## ★★9 — Why a 24-hour query returns four traces

Two reasons:

1. **Real gaps.** The station stopped, a data logger restarted, or a
   telemetry link dropped. Gaps are normal and are recorded in the archive; the
   service does not invent samples to fill them.
2. **Archive-side segmentation.** Data centres store data in fixed-length
   volumes (one file per day, or per hour) and some services return one
   response per volume rather than concatenating them.

Two lines that combine them *safely*:

```python
st.merge(method=-1)          # keep gaps as gaps: two traces, not one
st.sort(keys=['starttime'])  # deterministic order before any further use
```

Note what the safe version does *not* do: it does not fill. If the analysis
genuinely needs a continuous trace, the gap must be handled explicitly and the
choice justified, as in lesson 05.

---

## ★10 — Failure modes

- **Channel absent from the station service:** ObsPy raises
  `obspy.clients.fdsn.header.FDSNException` (typically
  `FDSNNoDataException`, a subclass) after the HTTP 204/404 response.
- **Window with no samples:** the dataselect service returns HTTP 204 and ObsPy
  raises `FDSNNoDataException`. It is *not* an empty `Stream` — the difference
  matters for code that iterates over results.
- **Channel exists with a different sample rate than assumed:** **nothing is
  raised.** The service returns the data it has, with the true rate in the
  MiniSEED header, and your assumption is silently wrong. This is the case the
  validation function in the lesson exists for, and the only one of the three
  that a user must catch themselves.

---

## ★★★11 — A caching layer for 200 station-days per run

```
data/raw/<service-shortname>/<network>/<station>/<channel>/<YYYY>/<DDD>/
        <network>.<station>.<location>.<channel>.<YYYY>-<DDD>.mseed
data/raw/.../manifest.jsonl          # one provenance record per file
```

- **Naming:** the SEED identifier plus the day, so the file name is derivable
  from the query and a directory listing is a catalog.
- **Invalidation:** never. A day of data does not change; if a data centre
  revises it (a timing correction, a response update), the revision is a new
  *version* of the file, and the manifest records the checksum that was used.
- **Manifest:** append-only JSONL, one record per file, with the query, the
  checksum and the request time.
- **Cache-invalidation rule:** none for the data; the *stations* cache does need
  one, because a station's response and channel list can be revised. Use a
  validity window (for example 30 days) on the station cache only.

**Failure mode the cache introduces:** a workflow that silently uses stale or
incomplete data forever. It is detected by recomputing the checksum of every
file against the manifest at the start of each run and failing loudly on a
mismatch, and by recording the file count and total byte count per run so that
a truncated download is visible as a deficit.

---

## ★★★12 — Detecting a different MiniSEED encoding

A MiniSEED record header declares its encoding in byte 20 of the fixed header:
0 ASCII, 1 `int16`, 3 `int32`, 4 `float32`, 10 Steim-1, 11 Steim-2.

```python
def encodings(path: str) -> set[int]:
    from obspy.io.mseed import get_record_information
    info = get_record_information(path)
    return {info["encoding"]} if "encoding" in info else set()
```

**Does it matter?**

- **For the samples:** no, provided the encoder was fed integers that fit. Steim
  is lossless for integer data, so the decoded sample values are identical.
- **For the file size:** yes, by a factor of up to 4. It also matters for
  *arithmetic*: a file in `float32` (code 4) carries values that have already
  been rounded to 24 bits of mantissa, and a reader who assumed `int32` will
  conclude that the instrument has a fractional noise floor that it does not
  have.
- **For reproducibility:** yes. Two runs of the same query can return different
  encodings if the archive re-encodes its holdings, so the checksum changes
  while the samples do not. A pipeline that compares checksums as a proxy for
  "same data" will report a spurious difference. Compare the decoded samples for
  equality and the checksum only for identity.

---

## ★★★13 — A rate-limited downloader

```python
import time
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.header import FDSNException

def fetch(client: Client, query: dict, attempts: int = 5,
          min_interval: float = 1.0):
    last = [0.0]
    for attempt in range(attempts):
        wait = min_interval - (time.monotonic() - last[0])
        if wait > 0:
            time.sleep(wait)
        try:
            result = client.get_waveforms(**query)
            last[0] = time.monotonic()
            return result
        except FDSNException as exc:
            last[0] = time.monotonic()
            if attempt == attempts - 1:
                raise
            time.sleep(min_interval * 2 ** attempt)   # exponential backoff
    raise RuntimeError("unreachable")
```

Parameters chosen: minimum interval 1 s (the documented courtesy limit for most
FDSN services), five attempts, backoff factor 2, so waits of 1, 2, 4, 8 s.

**Failure mode the retry introduces:** a transient failure and a permanent one
become indistinguishable in the log — both appear as "succeeded after 3
attempts". Record the attempt count and the exception text per request, so that
a systematic problem is visible as a rising attempt count rather than as an
occasional delay.

**Reproducibility when a request ultimately fails:** the run must fail, not
continue with partial data. A workflow that catches the final exception and
carries on produces a result computed from an unknown subset of the intended
network, and the missing stations are invisible in the output. The correct
design is: fail the run, write the failed query to a retry file, and require a
human decision — or a documented policy — before proceeding.
