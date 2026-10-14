# Exercises — 03-10-08 Fetching Data from FDSN Web Services

Attempt these **closed-book** before opening the
[solutions](./08-fdsn-clients-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first; it makes no network request:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/fdsn_clients_demo.py
```

---

## ★ Foundational

**★1.** Name the three FDSN services, the format each returns and the question
each answers.

**★2.** State the base URL that ObsPy's `IRIS` and `EARTHSCOPE` short names
resolve to, and name one endpoint that returns HTTP 404.

**★3.** Explain in two sentences why constructing a client needs no network
access, and state how many short names this installation knows.

**★4.** Give the four required parameters of a dataselect query with their
units, and the name of the station service that supplies the metadata.

**★5.** State what the channel codes `BHZ`, `HHZ` and `LHZ` promise, and what
you must check instead of trusting the promise.

---

## ★★ Applied

**★★6.** Write the complete URL, with parameters, for a dataselect request of
`IU.ANMO.00.BHZ` for the hour beginning 2024-03-15T08:00Z. State the base URL.

**★★7.** Implement the two validation checks and run them on three traces: a
healthy one, one truncated in time, and one with a shifted start time. Report
which checks fire for each and why the third is the dangerous case.

**★★8.** Write a provenance record for a downloaded waveform. List every field,
and state which you cannot populate offline.

**★★9.** A 24-hour query returns four traces with different start times. Give
two reasons the archive would split the data, and the two lines of code that
combine them safely.

**★★10.** State the ObsPy exception for a channel absent from the station
service, the behaviour for a window with no samples, and what happens when the
channel exists with a different sample rate than assumed.

---

## ★★★ Research-oriented

**★★★11.** Design a caching layer for a workflow downloading 200 station-days
per run: file naming, directory layout, invalidation rule and provenance
record. Then state the failure mode the cache introduces and how you would
detect it.

**★★★12.** Design a check that detects when the dataselect service returns a
different MiniSEED encoding from the one expected. State whether the difference
matters for the samples, the file size, or both.

**★★★13.** Write a rate-limited downloader with exponential backoff. State the
parameters chosen, the failure mode the retry introduces, and how the workflow
remains reproducible when a request ultimately fails.
