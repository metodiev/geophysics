# Exercises — 22-04-05 Cloud-Native Geoscience Data Access

Attempt these before reading the
[solutions](./05-cloud-native-geoscience-solutions.md). The lesson is
[05 Cloud-Native Geoscience Data Access](../05-cloud-native-geoscience.md). Numbers refer
to the **SYNTHETIC** model of `code/cloud_native_geoscience_demo.py`: a
$16384 \times 16384$ uint16 raster, chunks of 512, 1024 and 2048, 30 ms per request,
100 MB/s per connection, 16 connections.

## ★ Foundational

**★1.** Name the three object-store operations that matter for scientific data access and
state one consequence of each for a layout.

**★2.** For the $16384^2$ raster: (a) compute its size in MB; (b) compute the bytes a
$1024 \times 1024$ window needs; (c) compute the amplification for chunks of 512 and
2048 and explain the difference.

**★3.** State what an overview level is, and compute the storage of five overviews as a
multiple of the base level.

## ★★ Applied

**★★4.** A client reads $1024 \times 1024$ windows from the demonstration's raster with
chunks of 1024.

(a) State the number of chunks, the amplification, the latency, the transfer and the total
time serially. (b) Compute the same with 16 connections. (c) State which term dominates
and what would change if the store's latency were 5 ms instead of 30 ms.

**★★5.** A viewer serves a $500$ GB raster in $2048^2$ tiles to a client displaying
$256 \times 256$ windows.

(a) Compute the amplification. (b) State the change that reduces the bytes by a factor of
about 64 and its storage cost. (c) State the change that reduces the request count for a
window spanning many chunks.

**★★6.** A team reports 20 requests, 4 s and 120 MB for a single pan.

(a) State the plausible explanation if the tiles are $2048^2$. (b) State the two
measurements that would confirm it. (c) State the change that fixes it and the one that
would not.

## ★★★ Research-oriented

**★★★7.** Design a cloud-native layout for a 100 TB tiled raster archive that must serve
(i) an interactive viewer, (ii) regional window queries of about $1/100$ of the area, and
(iii) a machine-learning training job that reads random $512^2$ patches. State the chunk
size, the pyramid, the object count, the manifest contents, and the one access pattern
your layout serves worst. State what you would measure.

**★★★8.** The lesson's model assumes whole-chunk reads. Design a measurement of the
*effective* bytes per request for a store and format: state the statistic, the two formats
you would compare (a compressed chunked array and an uncompressed one), and the confounder
(server-side caching). State what the measurement cannot tell you for a query you have not
issued.

**★★★9.** A group's analysis reads a cloud archive for eight hours per run and is billed
per request. Propose a design that reduces the bill without changing the analysis's
results: state the layout change, the caching change, and the measurement that shows the
result is unchanged. State the risk the caching introduces.
