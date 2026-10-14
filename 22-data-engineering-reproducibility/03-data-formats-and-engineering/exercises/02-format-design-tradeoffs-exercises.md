# Exercises — 22-03-02 Format Trade-Offs: Access Patterns, Compression, Portability

Attempt these before reading the
[solutions](./02-format-design-tradeoffs-solutions.md). The lesson is
[02 Format Trade-Offs](../02-format-design-tradeoffs.md). All numbers refer to the
**SYNTHETIC** model of `code/format_design_tradeoffs_demo.py`: $1024 \times 1024$
float32 grid, $256 \times 256$ query window, 200 MB/s read bandwidth, 0.1 ms local
and 20 ms object-store request latency.

## ★ Foundational

**★1.** Write the two-term read cost model and state which term a chunk shape
controls directly.

**★2.** For the demonstration's grid and window: (a) compute the bytes read by a
row-major scan and the amplification; (b) do the same for chunks of $128$ and $64$;
(c) state the approximate formula for the amplification and check it against (b).

**★3.** State what the demonstration measures for compression of a smooth ramp and
of white noise, and what single property of the data explains the difference.

## ★★ Applied

**★★4.** Using the amplification formula $((w+c)/w)^{2}$ for a window $w = 256$:
(a) compute the amplification for $c = 256, 128, 64, 32$; (b) for each, compute the
time on a local disk (0.1 ms per request, 200 MB/s) and on an object store (20 ms per
request, 200 MB/s), given 262 kB of useful bytes; (c) state which chunk is optimal
for each backend and why.

**★★5.** A group writes a daily $256 \times 256$ float32 snapshot and ten years of
1 Hz samples at 8 bytes per value.

(a) Compute the bytes per day and per decade for each. (b) Compute the number of
objects in each case if one file is written per day. (c) State which figure drives
the operational cost and what to change.

**★★6.** A colleague reports "our netCDF files compress about 10×". State the three
things the claim is missing, and design the one-page measurement that would make it
usable in a methods section.

## ★★★ Research-oriented

**★★★7.** Design the storage layout for a 30-year archive of hourly gridded model
output ($1°$ global, float32) that must support (i) full-field reads for plotting,
(ii) point time series for 50 named cities, and (iii) regional windows for a
downscaling study. State the format, the chunking, the partitioning, the object
count, the annual storage, and the one query that your layout makes expensive. State
what you would measure to check the claim.

**★★★8.** The demonstration's local-disk optimum is $128$ and its object-store
optimum is $256$. Derive the request latency at which the two become equal, as a
function of the window, bandwidth and chunk sizes, and state the practical
consequence for a layout that must serve both backends from one archive.

**★★★9.** Compression interacts with chunking because chunks are compressed
independently. Specify a measurement that determines the chunk size at which
compression efficiency stops improving, state the confounder (read amplification
from §2), and describe the single experiment that trades the two effects off
against each other. State what the experiment cannot tell you.
