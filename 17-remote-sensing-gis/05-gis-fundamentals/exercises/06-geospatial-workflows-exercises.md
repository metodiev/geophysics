# Exercises — 17-05-06 Reproducible Geospatial Workflows (QGIS, Python)

Attempt these before reading the
[solutions](./06-geospatial-workflows-solutions.md). The lesson is
[06 Reproducible Geospatial Workflows](../06-geospatial-workflows.md). All models
are **SYNTHETIC**.

## ★ Foundational

**★1.** Two encodings of the same three-row table differ only in row order. State
whether a SHA-256 hash of the raw bytes will match, and state the two changes to
the encoding that would make it match.

**★2.** A projection round trip returns coordinates differing from the input by
$3 \times 10^{-12}$ degrees. Convert that to millimetres at the equator and state
whether the difference is evidence of a bug.

**★3.** A pipeline's manifest contains the input hash and the code revision but
not the parameters. State the failure mode with a concrete example.

## ★★ Applied

**★★4.** A buffer parameter changes from 500 m to 501 m. Compute the resulting
change in the area of a circular buffer of that radius, and state the percentage
change.

**★★5.** A random jitter is drawn per site from a seeded generator. 500 sites are
processed in a shuffled order some days and in sorted order other days. Explain
what changes and what does not, and give the fix.

**★★6.** Write the five guards you would place on a raster pipeline and say, for
each, what specific defect it prevents and what it cannot detect.

## ★★★ Research-oriented

**★★★7.** Design the manifest for a four-stage workflow (vector clip, raster
resample, kriging interpolation, suitability overlay) that includes a stochastic
step. State which entries are necessary for reproducibility and which are merely
useful, and justify each.

**★★★8.** A colleague cannot reproduce your map from the same input file. Write
the diagnostic sequence that would isolate the cause among: library version,
parameter value, iteration order, projection grid data, and a floating-point
comparison tolerance.
