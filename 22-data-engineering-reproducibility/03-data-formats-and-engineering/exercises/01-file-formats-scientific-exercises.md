# Exercises — 22-03-01 Scientific File Formats

Attempt these before reading the
[solutions](./01-file-formats-scientific-solutions.md). The lesson is
[01 Scientific File Formats](../01-file-formats-scientific.md). All numbers refer to
the **SYNTHETIC** model of `code/file_formats_scientific_demo.py`: 250 000 unit-
variance float64 values, text at 60 MB/s, binary at 2000 MB/s, float32 floor
$2.23 \times 10^{-7}$.

## ★ Foundational

**★1.** List the six items a scientific file must carry from §2, and state which
two are guaranteed by the format itself rather than by the writer's discipline.

**★2.** For the demonstration's array: (a) compute the bytes per value for text at
6 decimals, binary float64 and binary float32; (b) compute the ratio of the text to
the binary64 payload; (c) state the ratio of float32 to float64 and the precision
cost that comes with it.

**★3.** State the maximum round-trip error at 3, 6 and 9 decimals for unit-scale
data, and state which of the three is below a stated measurement uncertainty of
$1 \times 10^{-6}$.

## ★★ Applied

**★★4.** A time series of 500 000 values is to be exchanged with a colleague.

(a) Compute the size in text at 6 decimals, binary float32 and binary float64.
(b) Compute the parse time for each using 60 MB/s (text) and 2000 MB/s (binary).
(c) State the two-question decision you would put to the colleague before choosing.

**★★5.** A netCDF file declares `units = "m/s"` but the values are accelerations in
m/s². (a) State the error a downstream user makes if they trust the attribute.
(b) State what a round-trip check would and would not detect here. (c) State the
check that would detect it.

**★★6.** The demonstration measures a compression ratio of 76.29× on a smooth ramp
and 1.08× on white noise with the same algorithm and container. (a) Explain why.
(b) State the two properties of your own data that predict the ratio. (c) State what
this implies about publishing a compression ratio in a methods section.

## ★★★ Research-oriented

**★★★7.** Design a format and metadata policy for a group that archives (i) a
12-million-row earthquake catalogue, (ii) a daily 2000×2000 gridded product, and
(iii) 400 station parameter files. State the format for each, the metadata each must
carry, the conversion checks, and the one decision that must be revisited if the
group later moves to object storage.

**★★★8.** The round-trip error at a fixed number of decimals depends on the
magnitude of the value. Derive or measure how the *relative* error behaves for
values near zero, and state the resulting rule for choosing decimals for a quantity
that spans several orders of magnitude (for example an amplitude spectrum). State
what a single fixed decimal count cannot guarantee.

**★★★9.** A colleague proposes storing all three data sets in one HDF5 file per
project "so that everything is together". Evaluate the proposal against §2 and §5:
state two advantages, three specific costs, and the failure mode that would appear
only when two people run the pipeline at once.
