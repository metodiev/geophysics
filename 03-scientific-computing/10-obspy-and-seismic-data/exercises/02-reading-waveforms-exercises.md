# Exercises — 03-10-02 Reading MiniSEED/SAC: Trace and Stream

Attempt these **closed-book** before opening the
[solutions](./02-reading-waveforms-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to the demonstration require you to run it and report its
actual output:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/reading_waveforms_demo.py
```

The demo writes 3000 `int32` samples at 100 Hz and deletes its scratch
directory on exit.

---

## ★ Foundational

**★1.** The demo reports a MiniSEED file of 8192 bytes for 3000 samples. State
the bytes per sample and the bits per sample, and compare with uncompressed
`int32`. Give the ratio as a compression factor.

**★2.** A SAC file is 12632 bytes for a 3000-sample trace. Show, by arithmetic,
that a 632-byte header and `float32` samples account for the size exactly.

**★3.** Name the MiniSEED encoding code for `int32`, `float32` and Steim-2, and
state which ObsPy selects by default for integer data.

**★4.** The demo writes `calib = 5.1e8`, reads the file back, and prints
`calib = 1.0`. Which format lost the field? What should a reader use instead?

**★5.** State, for each SEED band code, the nominal sample-rate range: `LH`,
`BH`, `HH`, `EH`. Then write the full id of a broadband vertical channel at
station `ABCD` in network `XX`, location `00`.

---

## ★★ Applied

**★★6.** Write `describe(path)` that prints, per trace, the id, sample rate,
`npts`, dtype and start time, plus the number of samples implied by the time
span. Run it on a MiniSEED file and on a SAC file written from the same data
and report the single place where the two disagree.

**★★7.** Explain why the file size *increases* with the amplitude of the
waveform when the waveform shape and length are unchanged. Quote the three
measured sizes and bytes-per-sample values, and state the amplitude at which
Steim becomes worse than raw `int32`.

**★★8.** A 60 s, 100 Hz waveform of small amplitudes is written to SAC and
read back. Predict the maximum relative error from `float32` epsilon, then
compare with the measured value and account for the ratio.

**★★9.** Write code that creates a `Stream` with a 4.5 s gap and produces both
a gap-preserving and a gap-filled version. Report `len(st)` and `npts` for
both, the number of filled samples, and the exact error you get if you pass
`fill_value=0.0` to integer data.

**★★10.** The demo writes MiniSEED into a file named `.bin` and reads it
successfully. Explain how the format was determined, and describe a realistic
failure this behaviour can hide.

---

## ★★★ Research-oriented

**★★★11.** Measure the compression ratio of Steim-2 against raw `int32` for
three 20 000-sample signals of equal dynamic range: a smooth sinusoid,
band-limited noise (1–20 Hz) and white noise. Report bytes per sample for each
and explain the ordering using the distribution of first differences. State
which signal is representative of real seismic data and why.

**★★★12.** Write a provenance record for a waveform file: service URL, query
parameters, request time, channel list and checksum. Implement it offline (for
a file you generated), list which fields you could not populate, and argue why
the checksum is the minimum viable field.

**★★★13.** Two archives store the same 10-year, three-component, 100 Hz
channel. Archive A stores MiniSEED at 2.7 bytes per sample; archive B stores
SAC at 4 bytes per sample plus a 632-byte header per file, with files split per
day. Compute both volumes in GB for one channel of three components, state the
number of files each archive holds, and recommend one for long-term storage
with two quantitative reasons.
