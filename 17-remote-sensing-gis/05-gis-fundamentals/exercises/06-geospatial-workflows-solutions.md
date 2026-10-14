# Solutions — 17-05-06 Reproducible Geospatial Workflows (QGIS, Python)

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [06 Reproducible Geospatial Workflows](../06-geospatial-workflows.md).

---

## ★1 — Row order and a hash

No: SHA-256 over the raw bytes of two differently ordered encodings gives two
different digests, because the byte stream differs. Two fixes, both needed:

1. **Sort** the rows on a complete key (every non-geometry column, plus the
   geometry's own coordinates already being compared), so the encoding is
   invariant to input order.
2. **Snap coordinates** to a stated precision before serialising, so the last
   digits of a projection or a float printing difference do not change the bytes.

Fixing the column order explicitly is the third element: column order is not
semantically meaningful but is byte-visible, and a library change that reorders
columns will break a canonical hash.

---

## ★2 — Nanometres, not a bug

$3 \times 10^{-12}$ degrees at the equator is

$$3\times10^{-12} \times 111\,319\ \mathrm{m} = 3.34 \times 10^{-7}\ \mathrm m
= \mathbf{3.3 \times 10^{-4}\ mm}.$$

That is 0.3 micrometres — twelve orders of magnitude below any geophysical
measurement and consistent with double-precision round-off through two projection
evaluations. The lesson measured $1.5\times10^{-15}$ degrees (0.17 nanometres) on a
clean round trip and $1.9\times10^{-15}$ degrees through a second route. A
difference of this size is evidence that the computation is *working*; the
question is whether the workflow's stated tolerance is consistent with it. A
tolerance of $10^{-9}$ degrees (0.1 mm) is both stable and meaningful.

---

## ★3 — Manifest without parameters

The cache key is incomplete, so a **changed parameter serves a stale result**: a
run with `buffer_m = 500` is returned for a request with `buffer_m = 501`, and the
output is different from the one requested by 0.4 % of the reported area (see
★4). Nothing in the output says which parameters produced it, so the error is
undetectable from the result and appears as a slowly accumulating inconsistency
between figures produced on different days.

---

## ★4 — One metre of buffer radius

For a disc of radius $r$,

$$\Delta A = \pi\left[(r + \Delta r)^2 - r^2\right] = \pi(2r\Delta r + \Delta r^2)
= \pi(1000 \times 1 + 1) = 3144.7\ \mathrm{m^2},$$

of which the leading term is $2\pi r\Delta r = 3141.6\ \mathrm{m^2}$;

against $A = \pi(500)^2 = 785\,398\ \mathrm{m^2}$, so

$$\frac{\Delta A}{A} = \frac{3144.7}{785\,398} = \mathbf{0.4004\%}.$$

The lesson measured 3139.685039 m² and 0.4004 % on a polygon buffer: the
percentage matches, and the absolute difference (3144.7 exact disc versus 3139.7
polygon) is the polygonal approximation of the disc, about 0.16 % of the change. Both numbers say the
same thing: a 0.2 % change in a radius changes every reported area by 0.4 %, which
is far larger than most reporting precision.

---

## ★5 — Seeded jitter in a shuffled order

What does **not** change: the sequence of random numbers, because the seed fixes
the generator's stream. What **does** change: which site receives which draw,
because the numbers are consumed in the order the code visits the rows. The
multiset of jitters is identical; the assignment is not, and the two outputs
differ by up to the difference between two draws (the lesson measured a maximum of
0.116595 on unit-scale jitters).

The fix is to make the draw a function of the entity rather than of the traversal:

```python
rng = np.random.default_rng(seed)
for site_id in sorted(sites["site_id"]):
    sub = np.random.default_rng([seed, hash_of(site_id)])
    jitter = sub.normal(0.0, scale)
```

A per-entity seed derived from the global seed and the entity's key makes the
assignment independent of order, and it also makes the result stable under
parallelisation — which is the case where order changes silently.

---

## ★6 — Five guards

| guard | prevents | cannot detect |
|---|---|---|
| CRS present (`crs is not None`) | unitless distances and areas | a wrong but present CRS |
| CRS units are metres | degree-arithmetic areas | a distorted projection in metres |
| geometry validity | meaningless areas, overlays and buffers | a valid but wrong polygon |
| geometry type is expected | `.area` on a mixed layer returning zeros | a correct type with wrong vertices |
| extent overlaps the study area | a layer from the wrong tile or the wrong continent | a layer from the right area with a wrong attribute join |

The pattern is that every guard tests a *metadata* property, and none of them tests
whether the data are correct. That is why the pipeline also needs a validation set
and, where possible, an independent measurement.

---

## ★7 — A four-stage manifest

**Necessary** (two runs with different values are different computations):

| stage | entries |
|---|---|
| clip | clip geometry and its CRS, the clip predicate, the source-layer version and hash |
| resample | source grid and CRS, target grid, cell size, resampling statistic, NoData policy |
| kriging | sample hash, trend model, variogram family and parameters (or the fit specification), search radius, nugget, seed if simulation is used |
| overlay | normalisation rule and its ranges, weight vector, aggregation rule, candidate set and mask |
| all stages | code revision, library versions (`numpy`, `geopandas`, `shapely`, `pyproj`, `proj`), Python version |
| stochastic step | seed **and** the per-entity seed derivation rule, plus the iteration order |

**Useful but not necessary**: wall-clock time, host name, input file paths (as
opposed to hashes), intermediate checksums, and any parameter that is provably
unused.

The distinction matters because the manifest is also the cache key: including
merely useful entries (a timestamp, a host name) makes the key unstable and
destroys cache hits, while omitting a necessary one serves stale results. The
stochastic step is the entry most often omitted, and it is the one whose omission
is invisible, because a re-run with a different assignment looks like a new result
rather than a broken one.

---

## ★8 — A diagnostic sequence

Order the checks so that each one eliminates a class of cause, cheapest first:

1. **Compare the inputs by hash**, not by name. A silently updated input explains
   everything and is the commonest cause.
2. **Compare the manifests.** If the parameters or library versions differ, that
   is the answer; this costs one command.
3. **Compare the outputs at the first differing stage**, using a canonical encoding
   (sorted rows, snapped coordinates). This localises the divergence to one stage
   rather than to the whole chain.
4. **Re-run that stage twice in the same environment.** If it is not idempotent,
   the cause is iteration order or an unseeded random step — check the seed's
   *derivation*, not only its value.
5. **Re-run that stage with the same code but a different library version.** A
   change here is a version effect; for projections, check the PROJ database
   version and the datum grid files, not only `pyproj`.
6. **Compare with a stated tolerance**, not for equality. If the difference vanishes
   at $10^{-9}$ degrees or $10^{-6}$ relative, it was round-off and the workflow's
   comparison rule was too strict — which is a workflow defect worth fixing, not a
   computational one.

Only after 1–6 have been eliminated is it worth reading the code — and at that
point the code is usually the explanation for a difference that steps 1–6 have
already localised.
