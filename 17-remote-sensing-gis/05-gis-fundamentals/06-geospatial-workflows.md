---
id: 17-05-06
title: "Reproducible Geospatial Workflows (QGIS, Python)"
level: graduate
prereqs: ["17-05-02", "17-05-03", "22-02-02"]
tags: [gis, geospatial, remote-sensing, gis-fundamentals, reproducibility, provenance, workflow, qgis]
---

# Reproducible Geospatial Workflows (QGIS, Python)

A geospatial result is a claim about a place, and it is only usable if someone
else can obtain the same number from the same inputs. That property — 
**reproducibility** — is not a virtue of the analyst, it is a set of engineering
properties of the pipeline: a pure function of its inputs, a canonical output
encoding, a stated tolerance for numeric comparison, fixed iteration order, a
record of the environment, and validation that can fail. This lesson builds a
small pipeline in memory and measures each property, including the ones that are
usually assumed rather than tested.

The GUI case is treated as a special case of the same discipline: a QGIS model or
a Graphical Modeler workflow is a program, and it is reproducible only to the
extent that it records its inputs, parameters, projections and processing
versions — which is exactly the manifest built in §6.

All models and data in this module are **SYNTHETIC**. The sites, the zones and
the rasters below are generated in memory from a fixed seed. Nothing is read from
or written to disk, and the "hashes" are computed in RAM from in-memory objects.

## Learning objectives

By the end of this lesson you will be able to:

1. **Design** a geospatial pipeline as a pure function of its inputs and
   **demonstrate** that equal inputs give equal outputs.
2. **Distinguish** bitwise from numeric reproducibility, and **state** the
   tolerance under which a projection round trip is a reproduction.
3. **Detect** order dependence in a dissolve or group-by and **fix** it by
   canonicalising the output.
4. **Explain** why a random seed alone does not make a stochastic step portable,
   and **demonstrate** the effect of iteration order.
5. **Write** unit- and CRS-guards that fail loudly instead of silently producing
   a unitless or degree-based result.
6. **Assemble** a provenance record containing input hash, parameters, code and
   library versions, and **justify** why the projection library version is part of
   it.
7. **Validate** an output against schema, CRS, extent and nodata expectations, and
   **prove** the validation can fail.
8. **State** the manifest that must be equal for two runs to be the same run.

## Prerequisites

- [02 Vector Data Model and Attribute Operations](02-vector-data-model.md) —
  the joins and dissolves being made reproducible.
- [03 Raster Data Model, Resolution and Resampling](03-raster-data-model.md) —
  the transforms and nodata conventions being recorded.
- [22-02-02 Environment Pinning](../../22-data-engineering-reproducibility/02-reproducible-workflows/02-environment-pinning.md) —
  dependency pinning, extended here to spatial data and projection grids.

## 1. A pipeline as a pure function

The pipeline under study buffers a synthetic sample layer and summarises the
buffered area by zone:

```python
def process(points, params):
    buffered = points.copy()
    buffered["geometry"] = buffered.geometry.buffer(params["buffer_m"])
    buffered["area_m2"] = buffered.geometry.area
    summary = (buffered.groupby("zone", sort=params["sort_groups"])
               .agg(n=("site", "count"), mean_area=("area_m2", "mean"))
               .reset_index())
    return summary
```

Run twice on equal inputs, it returns the same result:

```
  input layer: 60 synthetic points, no CRS declared
 zone  n     mean_area
north 36 784137.122636
south 24 784137.122636

  hash(run 1)                 : 42f29febf5ce42b7
  hash(run 2)                 : 42f29febf5ce42b7
  hashes equal                : True
  hash(different input)       : f10fe2f68ff766de
  hash differs on new input   : True
```

The function has no hidden state: no clock, no unseeded randomness, no reliance
on dictionary or file-system ordering, no absolute paths. Those four are the
usual sources of irreproducibility, and none of them is detectable from a single
run — a pipeline is reproducible because its *inputs are complete*, not because
it ran successfully.

The `mean_area` values are equal for the two zones here only because the buffer
radius exceeds the zone geometry, which is a coincidence of the synthetic
construction and an illustration of the point: an aggregation can be
*insensitive* to the grouping variable, which is worth noticing before
interpreting it.

## 2. Bitwise versus numeric reproducibility

A projection is an iterative evaluation of a series, so its last digits depend on
the route taken, on the library version and on the datum grid files. The
demonstration reprojects 40 synthetic points through two routes and measures:

| quantity | value |
|---|---|
| EPSG:4326 → EPSG:32631 → EPSG:4326, max longitude discrepancy | 1.540 × 10⁻¹⁵ deg = 1.715 × 10⁻¹⁰ m |
| same route, max latitude discrepancy | 1.421 × 10⁻¹⁴ deg = 1.579 × 10⁻⁹ m |
| bitwise identical coordinates | **False** |
| a second route via EPSG:3857, max discrepancy | 1.901 × 10⁻¹⁵ deg |
| the two routes agree with each other to | 1.193 × 10⁻¹⁵ deg |

Nanometres. The honest target is not bitwise equality but agreement to a **stated
tolerance**:

$$
\lVert \mathbf{x}_{\text{run}} - \mathbf{x}_{\text{reference}} \rVert_\infty
\le \varepsilon, \qquad \varepsilon = 10^{-9}\ \text{deg} \approx 0.1\ \text{mm}.
$$

A workflow that asserts bitwise equality across library versions will fail the day
the library is upgraded, and a workflow that accepts any difference will never
notice a real bug — a wrong datum, a swapped axis order, a missed projection.
Choosing $\varepsilon$ from the physics (a tenth of a millimetre is far below any
geophysical measurement) makes the test both stable and meaningful. Note the
asymmetry: the *positions* are reproduced to nanometres, but the *encoding* is
not, so any cache keyed on raw bytes will miss on every run. That is the next
section's problem.

## 3. Order dependence and canonicalisation

The same numeric result can be encoded differently depending on row order. A
dissolve on the same rows in a different order:

```
  dissolve(sort=True) on the original order : index ['north', 'south']
  dissolve(sort=True) on a shuffled copy    : index ['north', 'south']
  dissolve(sort=False) on the shuffled copy : index ['south', 'north']
  encoding WITHOUT canonicalisation, d1 vs d2: 91a8b644f9c1f1a1 vs 91a8b644f9c1f1a1 (equal: True)
  encoding WITHOUT canonicalisation, d1 vs d3: 91a8b644f9c1f1a1 vs 683921bab283a397 (equal: False)
  encoding WITH canonicalisation,   d1 vs d3: 91a8b644f9c1f1a1 vs 91a8b644f9c1f1a1 (equal: True)
  mean values identical despite the order   : True
```

The numbers are identical and the files are not. Since a diff, a cache lookup and
a content hash all operate on the *encoding*, an unsorted group key is enough to
make two identical analyses look different — and, worse, to make a genuine change
invisible inside a large spurious diff.

The fix is a **canonical encoding** with three elements:

1. **sort** on every non-geometry column (or on an explicit ordering key);
2. **snap coordinates** to a stated precision before serialising, which absorbs
   the nanometre differences of §2;
3. **fix the column order** (and the row order of the header) explicitly, since
   column order is not semantically meaningful but *is* byte-visible.

GeoPackage, GeoParquet and every sensible interchange format are designed to be
written canonically for exactly this reason. A shapefile is not: its `.dbf` field
order, its `.shp` record order and its 100-byte headers make byte-level
reproducibility a project of its own, which is one reason it is a poor archive
format despite its ubiquity.

## 4. Randomness: a seed is not portability

Deterministic code plus a seed gives a deterministic result:

```
  seeded twice with 20261014  : [-0.470931  0.461829 -0.810164]
  identical                   : True
  seeded with a different value: [ 0.00123   0.298746 -0.274138]
```

But the seed fixes the *sequence*, not the *assignment*. Visiting six rows in a
different order with the same seed gives:

```
  same seed, rows visited 0..5        : [-0.023547  0.023091 -0.040508  0.093048 -0.073082 -0.012827]
  same seed, rows visited 3,0,5,1,4,2 : [ 0.023091  0.093048 -0.012827 -0.023547 -0.073082 -0.040508]
  the two MULTISETS of draws are equal : True
  the two ASSIGNMENTS are equal        : False
  max difference between the two jitters: 0.116595
```

Same seed, same numbers, different rows. Reordering an input, adding a filter or
parallelising a loop therefore changes every random number's destination while
leaving the seed untouched. The rule for a stochastic geospatial step (a
simulation, a bootstrap, a jittered location) is:

1. fix the seed **and** the iteration order (sort before drawing);
2. draw per entity from a **deterministic per-entity seed** — a hash of the
   entity's key combined with the global seed — so that the assignment is
   independent of traversal order;
3. record the seed and the generator in the provenance record.

The third point matters because generators differ: a NumPy `default_rng`
(PCG64) stream is not the same as a legacy `RandomState` stream, so a seed alone
does not reproduce a result across a library change.

## 5. Guards: fail loudly at the cheapest moment

Silent unit errors are the most expensive class of geospatial bug, because the
result looks plausible. A guard turns an invisible assumption into an exception:

```
  no CRS declared             : guard raised -> layer has no CRS: distances and areas would be unitless
  geographic (degree) CRS     : guard raised -> CRS units are 'degree', expected 'metre'
  projected metre CRS         : guard passed (metre)
```

Note that the pipeline in §1 applied a 500-unit buffer to a layer with **no CRS**.
With no CRS the number 500 has no unit, and the pipeline cannot know whether the
analyst meant 500 m or 500 degrees. The guard converts that into a two-line
error message at the point of the mistake.

Five guards worth writing once and reusing:

| guard | condition | why |
|---|---|---|
| CRS present | `frame.crs is not None` | otherwise every distance is a coordinate difference |
| CRS units | `axis_info[0].unit_name == "metre"` | degree arithmetic is not a length |
| geometry validity | `is_valid(geom).all()` | every area and overlay is undefined otherwise |
| geometry type | expected type set | `.area` on a mixed layer is defined and meaningless |
| extent overlap | the layer intersects the study area | a layer from the wrong continent is otherwise silent |

## 6. A provenance record

```
{
  "geopandas": "1.2.0",
  "input_hash": "27bff0a3339d2403",
  "input_rows": 60,
  "numpy": "2.5.4",
  "output_hash": "42f29febf5ce42b7",
  "pandas": "3.0.6",
  "parameters": { "buffer_m": 500.0, "sort_groups": true },
  "proj": "9.8.1",
  "pyproj": "3.8.0",
  "python": "3.14.8",
  "shapely": "2.2.0"
}
```

Every field is a fact about the machine, measured rather than assumed. Three are
easy to forget and two are usually forgotten:

* **The projection library and its datum/grid database version.** `PROJ 9.8.1`
  here. A time-dependent datum transformation depends on the *grid files*
  installed, not only on the library, so two machines with the same `pyproj`
  version can differ at the centimetre level on a real dataset. Recording the
  version is necessary and not sufficient; a container or an environment file is
  the way to pin the grids themselves.
* **The parameters**, including the ones that look cosmetic
  (`sort_groups`). They change the bytes and sometimes the numbers.
* **The input hash and row count**, so that a change in the input is visible in
  the record rather than in the result.

A QGIS processing model is the same object with a different front end: its
`processing.run` history, layer sources, projection choices and Processing
Toolbox version are the manifest. Saving a model without its parameter values is
equivalent to versioning a script without a lockfile — the code is there and the
run is not reproducible.

## 7. Validation that can fail

```
  PASS  has the expected columns
  PASS  row count equals the zone count
  PASS  no null values
  PASS  all areas positive
  PASS  within the buffered study area

  the deliberately corrupted copy was caught -> negative area: the pipeline is broken
```

Five checks, each a statement that must hold for the *result* to mean anything,
plus a deliberately corrupted copy to confirm the checks are wired up rather than
merely present. A validation suite that has never failed is indistinguishable
from one that cannot.

The checks are ordered from cheap-and-inevitable to expensive-and-conditional: a
schema check catches a renamed column in microseconds; a spatial check catches a
wrong CRS in milliseconds. Both are worth having, and the cheap ones should run
first so that a doomed run fails before it costs an hour.

## 8. Worked example: a cache key

A pipeline that takes 6 hours per run needs a cache. The cache key must be the
manifest, not the file name:

$$
\text{key} = H\!\left( \text{input hash} \,\Vert\,
\text{parameters} \,\Vert\, \text{code revision} \,\Vert\,
\text{library versions} \right).
$$

The demonstration measures why the parameters must be in the key:

| run | hash | equal to run 1 |
|---|---|---|
| `buffer_m = 500.0`, `sort_groups = True` | 42f29febf5ce42b7 | — |
| identical manifest | 42f29febf5ce42b7 | True |
| `buffer_m = 501.0` | 4301c689d4254fbb | **False** |

and the size of the change a one-metre parameter edit makes: the reported mean
buffer area changes by 3139.685039 m², i.e. **0.4004 %**. That is the exact
analytic value for a disc, $2\pi r \,\Delta r = 2\pi \times 500 \times 1
\approx 3141.6\ \mathrm{m^2}$, differing only because the synthetic cells are
polygons rather than perfect circles.

A 1 m change in a parameter changes every reported number, so a cache keyed on
the input file alone would serve a stale result and never say so. The manifest is
the smallest set of facts that must be equal for two runs to be the same run —
and the same list defines what a reader needs in order to reproduce your figure.

## Assumptions and regime of validity

1. **The projection metadata is honest.** Every guard in §5 trusts the declared
   CRS. A layer with the wrong EPSG code assigned is undetectable by any of them,
   and a sanity check against an independent position is the only defence.
2. **The tolerance is chosen from the physics.** $10^{-9}$ deg is far below any
   geophysical measurement, so it cannot hide a real error; a tolerance chosen to
   make a test pass does the opposite.
3. **The canonical encoding is the interchange format.** If a downstream tool
   reads a shapefile and rewrites it, byte-level reproducibility is lost at that
   boundary, and the responsible claim is numeric equivalence.
4. **Version pinning covers data as well as code.** Raster and vector products
   are versioned (collections, reprocessing dates); the same script on the same
   tile of a *different* collection version is a different input.
5. **"Deterministic" is a claim about the whole chain.** A seeded NumPy step
   inside a pipeline whose rows are visited in thread-completion order is not
   deterministic.
6. **Validation is not verification.** The checks above confirm the output has the
   shape it should; they do not confirm that the physics or the model is right
   ([19-07](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md)).

## Python demonstration

[`code/geospatial_workflows_demo.py`](code/geospatial_workflows_demo.py) builds
the whole pipeline in memory:

1. defines a pure-function pipeline and hashes its output across equal and
   different inputs;
2. reprojects synthetic points by two routes and measures the numeric difference
   against the bitwise test;
3. dissolves the same data in two row orders and contrasts canonicalised with
   non-canonicalised encodings;
4. demonstrates that a fixed seed with a different iteration order reassigns the
   same random draws to different rows;
5. runs three CRS/unit guards, two of which raise;
6. assembles a provenance record from measured library versions;
7. runs five output-validation checks plus a deliberately corrupted copy;
8. shows that a 1 m parameter change alters the output hash and the mean by
   0.4 %.

```bash
cd 17-remote-sensing-gis/05-gis-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geospatial_workflows_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/06-geospatial-workflows-exercises.md`](exercises/06-geospatial-workflows-exercises.md)
and the
[solutions](exercises/06-geospatial-workflows-solutions.md):

- **★** Compute a canonical hash of a small table by hand under two row orders.
- **★★** Write a guard set for a raster pipeline and justify each check.
- **★★★** Design the manifest for a multi-stage workflow with a stochastic step
  and state which entries are necessary and which are merely useful.

## Mastery checkpoint

Without notes:

> A pipeline reads a synthetic site layer, buffers it by a parameterised distance,
> joins a zone layer and writes a summary. **(a)** List the six entries you would
> put in a manifest for it and say which one a code-only commit would miss.
> **(b)** The pipeline's buffer step draws a random jitter per site from a seeded
> generator. Explain in two sentences how to make the jitter independent of row
> order. **(c)** A colleague reports that two runs differ by 3 × 10⁻¹² degrees and
> concludes that the workflow is broken. What do you tell them, and what tolerance
> would you propose? **(d)** The raster branch of the pipeline produces areas
> 0.4 % larger after a 1 m parameter change. Explain the magnitude without
> running anything.

A worked version of (a)–(c) is in the
[solutions](exercises/06-geospatial-workflows-solutions.md).

## Common pitfalls

1. **Hashing whatever the library wrote.** Byte-visible but semantically
   irrelevant differences (row order, column order, float formatting) destroy
   cache hits and obscure real changes.
2. **Asserting bitwise equality of projected coordinates.** It fails across
   versions and proves nothing.
3. **Relying on a seed without fixing iteration order.** The assignment changes
   while the seed does not.
4. **Caching on the file name.** Parameters and code revision are part of the
   input.
5. **Recording library versions but not the projection grids.** The grids are
   data and they move.
6. **A validation suite that has never failed.** Add a corrupted case.
7. **Treating a GUI workflow as self-documenting.** The model file records the
   graph; the parameters and versions are the manifest.

## Related modules

- [02 Vector Data Model and Attribute Operations](02-vector-data-model.md).
- [05 Spatial Interpolation: IDW, Kriging, Splines](05-spatial-interpolation-gis.md) —
  an inference step whose variogram and trend must appear in the manifest.
- [06-gis-fundamentals README](README.md).
- [22-02 Reproducible Workflows](../../22-data-engineering-reproducibility/02-reproducible-workflows/README.md) —
  containers, workflow managers and data versioning.
- [22-03 Data Formats and Engineering](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/README.md) —
  which spatial formats are canonical and which are not.

## Self-assessment checklist

- [ ] I can write a pipeline as a pure function and hash its output.
- [ ] I can state a numeric tolerance for a projection round trip and justify it.
- [ ] I can canonicalise an output so that row order does not change the hash.
- [ ] I can make a stochastic step independent of iteration order.
- [ ] I can write the five guards and say what each prevents.
- [ ] I can assemble a provenance record including projection-library versions.
- [ ] I can show that my validation can fail.
- [ ] I can state the manifest that defines "the same run".

