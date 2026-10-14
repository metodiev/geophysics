---
id: 05-06-06
title: "Documenting Processing: Reproducibility in Practice"
level: advanced
prereqs: ["05-06-01", "22-02-01"]
tags: [reproducibility, provenance, metadata, workflow, hashing, audit-trail]
---

# Documenting Processing: Reproducibility in Practice

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the levels of reproducibility and state which one a claim of
   reproducibility is actually asserting.
2. **Write** a machine-readable processing record that contains the input, the ordered
   steps, the parameters, the software environment and the output.
3. **Verify** a record by re-execution, and explain why a bit-identical match is the
   weakest useful form of verification.
4. **Demonstrate** that step order changes the result, and quantify the change.
5. **Choose** between comparing results and comparing parameter text, and state the
   tolerance.
6. **List** the sources of irreproducibility in a typical geophysical processing chain,
   including the ones that are not computational.

## Prerequisites

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — the stages
  whose record this lesson defines.
- [22-02-01 The Reproducibility Crisis](../../22-data-engineering-reproducibility/02-reproducible-workflows/01-reproducibility-crisis.md)
  — the general problem, which this lesson instantiates for geophysical processing.

## 1. Intuition: a processed dataset without its history is an opinion

Two people can process the same raw survey and produce contour maps that differ by
more than the anomalies they are interpreting. If neither published the sequence of
steps, neither can be checked, and the difference cannot be attributed to geology,
to software or to a parameter.

The situation is not symmetric between the two extremes:

- **A raw dataset is reproducible by construction.** Anyone can re-analyse it.
- **A processed dataset is reproducible only if the processing is a *record* rather
  than an *activity*.** A record is executable: someone else can run it and obtain the
  same numbers.

This lesson treats the record as the deliverable. The processing code is secondary;
a well-specified record can be re-implemented in any software, while a sophisticated
script with undocumented parameters cannot be checked by anyone, including its author
a year later.

## 2. Precise definitions

### 2.1 Levels of reproducibility

| level | claim | how it is verified | how strong it is |
|---|---|---|---|
| **bit-identical** | the same bytes come out | compare cryptographic hashes | strong but fragile: it depends on library versions, thread counts and machine architecture |
| **numerically equivalent** | the results agree within a stated tolerance | compare arrays with a stated absolute or relative tolerance | the practically meaningful level |
| **statistically equivalent** | the results differ by less than the data's own uncertainty | compare against the measured noise | the level that matters for interpretation |
| **conceptually equivalent** | the results support the same conclusion | compare downstream inferences | the weakest, and the one most often claimed silently |

A paper that claims "the processing is reproducible" without saying which of these is
asserted has said very little. The useful statement is of the form: *the record
reproduces the output bit for bit on the same environment; on a different NumPy
version the maximum difference is $10^{-15}$ mGal, which is $10^{-13}$ of the anomaly
peak and negligible against the 0.01 mGal noise.*

### 2.2 The processing record

A processing record is a structured document containing:

1. the **input** — a file reference plus a content hash;
2. the **ordered steps**, each with an operation name and its parameters;
3. the **environment** — library and interpreter versions, and anything else that
   affects arithmetic;
4. the **output** — a content hash;
5. the **verification** — what was compared with what, and at what tolerance.

Items 1–4 make the record; item 5 makes it a *claim*.

### 2.3 Content hashes

A hash is a fixed-length digest of a byte sequence. For floating-point data the record
must state the exact representation hashed (here, the C-contiguous IEEE-754 binary64
image of the array) because the same numbers stored as text with different precision
hash differently. Hashing is not a substitute for verification; it is a cheap,
unambiguous *fingerprint* of what was verified.

## 3. A measured record

[`code/processing_transparency_demo.py`](./code/processing_transparency_demo.py)
processes a synthetic 200-station profile with a three-step pipeline and produces a
record. The recorded content:

```json
{
  "input_file": "synthetic_profile.bin",
  "input_sha256": "593210de12ea00fd9568c805e311a60a...",
  "grid": {"dx_m": 25.0, "n_samples": 200},
  "software": {"numpy": "<version>", "python_hash_seed": 0},
  "steps": [
    {"op": "despike", "params": {"window": 5, "n_sigma": 4.0}},
    {"op": "level",   "params": {"order": 1}},
    {"op": "lowpass", "params": {"cutoff_wavelength": 400.0}}
  ],
  "steps_executed": [
    {"op": "despike", "params": {"window": 5, "n_sigma": 4.0}, "samples_changed": 3},
    {"op": "level",   "params": {"order": 1}, "coeffs": [...]},
    {"op": "lowpass", "params": {"cutoff_wavelength": 400.0}}
  ],
  "output_sha256": "caf44226281451d7a9c861f0ed6f96de..."
}
```

Note what the record contains beyond the parameter list: **the outcomes**. The despike
changed 3 samples (`samples_changed`), and the levelling fitted coefficients that are
recorded. Those outcomes are the first thing a reviewer checks, because they are
directly comparable between runs and they reveal, for example, a spike detector that
flagged 77 of 200 samples instead of 3.

Measured ranges for this dataset: the input spans −0.3829 to 1.5823 mGal, the output
−0.5059 to 0.7765 mGal.

## 4. Verification by re-execution

Re-running the same record in the same environment:

| check | result |
|---|---|
| re-run output hash equals the recorded hash | **True** |
| maximum absolute difference between runs | 0.000e+00 |

Bit-identical reproduction is achievable and worth having, because it is the only check
that needs no tolerance to interpret. But its scope must be stated honestly:

- it holds **on one machine, one library version, and one thread count**;
- it does **not** transfer to a different BLAS, a different compiler, or a different
  array order, because floating-point addition is not associative: summing the same
  values in a different order can change the last bit;
- it is therefore *evidence that the record is complete*, not evidence that the
  result is portable.

The last point is the useful one. A record that reproduces bit for bit leaves no room
for a forgotten parameter, because a forgotten parameter would have produced a
different hash.

## 5. Order matters, and the difference is measurable

The same three steps, with despiking and levelling swapped, give a different dataset:

| quantity | measured |
|---|---|
| output hash identical? | **False** |
| RMS difference between the two outputs | 0.007976 |
| ratio to the anomaly peak | 1.027 % of the peak |
| samples changed by despiking, in the recorded order | 3 |
| samples changed by despiking, in the swapped order | 3 |

The RMS difference is 1 % of the peak: small enough to escape a visual check, large
enough to matter when the target differences are of the same order. Both orders are
defensible — despiking first means the trend fit is not contaminated by spikes;
levelling first means the spike threshold is estimated on de-trended data — and that is
exactly why the order is part of the record rather than an implementation detail.

**A record that lists a set of operations without their order is a description of a
toolbox, not of a processing sequence.**

## 6. Comparing results, not text

The demo compares a parameter written as `0.3` with the same parameter written as
`0.1 + 0.2`:

| check | result |
|---|---|
| `0.3 == 0.1 + 0.2` | **False** |
| $\lvert 0.3 - (0.1+0.2)\rvert$ | $5.551\times10^{-17}$ |
| outputs bit-identical? | **True** |
| maximum difference between the outputs | 0.000e+00 |

Two lessons, pointing in opposite directions:

- **A workflow that declares "reproduced" because the parameter text matched is
  checking the wrong thing.** The parameters differed and the results did not.
- **A workflow that declares failure because the parameter text differed will produce
  false alarms on every machine.** Floating-point arithmetic does not represent decimal
  fractions exactly, so text comparison of parameters is a fragile test.

The correct procedure is to compare **results** with a stated tolerance, and to record
the tolerance in the claim. Section 2.1's levels exist precisely because "the same" is
too coarse a phrase for numerical work.

## 7. The verdict table

The demo's summary, as it should appear in a processing report:

| check | verdict | note |
|---|---|---|
| same record, same machine | PASS | bit-identical |
| same record, reordered steps | FAIL (by design) | differs by 0.007976 RMS |
| numerically equal parameter written differently | PASS | identical output; parameter text differs by $5.6\times10^{-17}$ |

The report must state which checks were run, on which software versions, with which
tolerance — otherwise the word "reproducible" carries no information.

## 8. What a processing report must contain

A checklist that follows from the measurements above:

| item | why it is needed |
|---|---|
| input datasets with hashes, sizes and acquisition dates | a survey that is re-levelled or re-released changes the input |
| every step, in order, with parameters **and units** | the order matters (Section 5); units prevent factor-of-1000 errors |
| parameter *provenance* — measured, assumed, or defaulted | an assumed parameter is a hidden assumption; a defaulted one is a hidden decision |
| the outcomes of data-dependent steps (samples flagged, coefficients fitted) | the first thing a reviewer checks (Section 3) |
| software names and versions, including library versions | arithmetic and algorithms change between versions |
| random seeds, if any step is stochastic | identified as a source of irreproducibility below |
| the band limits, datums and reference frames used | a processed field without a datum or a band limit is not interpretable |
| the verification performed: what was compared, at what tolerance | the claim of Section 2.1 |
| residuals of any inversion or fit | the diagnostic that reveals a wrong parameter |

The choice of file format and vocabulary for the metadata is a solved problem in the
wider community; the conventions are covered in
[22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md)
and
[22-02-02 Environment Pinning](../../22-data-engineering-reproducibility/02-reproducible-workflows/02-environment-pinning.md).

## 9. Worked example: choosing the tolerance from the noise

The tolerance in a reproducibility claim is not a matter of taste; it follows from the
data's own uncertainty. Suppose a processed gravity grid has a measured noise level of
0.012 mGal and an anomaly peak of 0.6 mGal. Then:

- a **bit-identical** claim asserts agreement to about $10^{-16}$ mGal, which is
  $10^{-14}$ of the noise — a far stronger statement than the science needs, and one
  that will fail on a different library version;
- a **numerically equivalent** claim at a tolerance of $10^{-9}$ mGal is still $10^{-7}$
  of the noise, and is safe on any environment;
- a **statistically equivalent** claim is satisfied by any tolerance below
  0.012 mGal, because a difference smaller than the noise cannot be detected in the
  data;
- a tolerance of 0.1 mGal would be **too loose**: it is eight times the noise, so two
  results could disagree by an amount a subsequent interpretation would notice, and the
  claim would still pass.

The rule is: **the tolerance must be at least an order of magnitude below the noise and
at least an order of magnitude above the machine precision of the arithmetic, and the
chosen value must be stated in the units of the data.** For the example above, a
tolerance of $10^{-6}$ mGal satisfies both bounds with room to spare, and it is the
number that belongs in the processing report.

## 10. Sources of irreproducibility, ranked by how often they bite

1. **A step performed by hand.** Moving a file, deleting a trace, applying an "obvious"
   correction in a spreadsheet. Nothing records it.
2. **A default parameter.** The value was chosen by the software, not by the analyst,
   and it may change between versions.
3. **A wrong step order in the documentation.** Section 5's 1 % difference.
4. **A missing environment specification.** A different NumPy or a different BLAS
   changes the last bits and, at a discontinuity in the algorithm (a threshold test),
   can change a decision.
5. **An unrecorded random seed.** Every stochastic step — a bootstrap, a k-means
   initialisation, a simulated anneal — is irreproducible without its seed. All the
   demos in this module use `np.random.default_rng(seed)` with the seed stated in the
   file for exactly this reason.
6. **Thread-count or hardware dependence.** Reduction order in parallel linear algebra
   is not fixed, so a sum can differ in the last bits between runs on different
   machines. This is why bit-identical reproduction is scoped to one environment.
7. **A file-order dependence.** A pipeline that globs a directory and processes files
   in whatever order the filesystem returns is not reproducible; sort explicitly.
8. **A silent data substitution.** A "cleaned" version of an input file replacing the
   original.

Note the pattern: items 1 and 3 are *human* sources, and they are the most common. The
computational sources (4–7) are easier to fix once they are recognised, because the
fix is a configuration file.

## 11. Assumptions

1. **The record is complete.** Everything in Section 3 is necessary; the claim is that
   it is *sufficient*, which holds only if no step exists outside the record. A record
   cannot detect a manual edit made between two recorded steps.
2. **Deterministic hardware arithmetic.** Bit-identical reproduction assumes the
   arithmetic is deterministic given the same environment; this is true for the same
   binary on the same machine and stated thread count, and false in general.
3. **The hash is of the data, not of a rendering.** Two arrays that plot identically can
   hash differently (and vice versa, in principle). Hashing a plot is not verification.
4. **Tolerance is chosen from the science, not from convenience.** A tolerance of
   $10^{-3}$ mGal is meaningful against a 0.01 mGal noise level and meaningless against
   a 1 mGal anomaly. The tolerance must be justified by the noise.
5. **The synthetic demonstration is a demonstration.** The hashes and differences in
   Section 4–6 are from one synthetic dataset; they illustrate the method, not a
   property of any particular software.

## 12. Units and dimensional analysis

Hashes are dimensionless digests: fixed-length hexadecimal strings independent of the
units of the data — which is a real limitation, since hashing the same physical data in
mGal and in m s⁻² gives different digests for the same information. The record must
therefore state the units *as well as* the hash; the hash establishes identity, the
units establish meaning.

The tolerances in Section 2.1 carry the unit of the quantity compared (mGal, nT,
m s⁻²). A relative tolerance is dimensionless and must be quoted as a fraction or a
percentage; mixing the two in one document is a common source of apparent
disagreement between two reports that in fact agree.

## 13. Python demonstration

[`code/processing_transparency_demo.py`](./code/processing_transparency_demo.py)
produces every number in Sections 3–7. The hashing and the ordered execution are the
core:

```python
def h256(a):                              # fingerprint of an array or a string
    if isinstance(a, str):
        return hashlib.sha256(a.encode("utf-8")).hexdigest()
    return hashlib.sha256(np.ascontiguousarray(a, dtype=np.float64).tobytes()).hexdigest()

def run_pipeline(data, x, dx, steps):      # steps are ORDERED, with parameters
    y, executed = data.copy(), []
    for step in steps:                     # the loop order IS the record
        ...
    return y, executed
```

`run_pipeline` executes the record rather than the analyst's intentions, which is the
only way to know that the record is complete.

## 14. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/06-processing-transparency-exercises.md`](./exercises/06-processing-transparency-exercises.md)
and [`exercises/06-processing-transparency-solutions.md`](./exercises/06-processing-transparency-solutions.md).

### Common mistakes

1. **Claiming reproducibility without a level.** Section 2.1.
2. **Comparing parameter text instead of results.** Section 6: equal text can mean
   unequal results and vice versa.
3. **Recording parameters but not outcomes.** The outcome (`samples_changed = 3`) is
   what a reviewer can check in one glance.
4. **Omitting the order.** Section 5: 1 % of the peak.
5. **Omitting units.** A parameter without a unit is not a parameter.
6. **Forgetting the seed of a stochastic step.** Every run differs, and the cause is
   invisible in the output.
7. **Leaving a manual step in the chain.** The most common source of irreproducibility,
   and the hardest to detect.

### Real-world applications

- **Regulatory and resource reporting.** Mineral resource estimates and environmental
  assessments require an auditable data chain; the record is the deliverable.
- **Multi-agency compilations.** Merging surveys from different decades requires that
  each survey's processing history be available, or the merged product's long
  wavelengths become uninterpretable.
- **Reproducibility in published research.** Journals increasingly request the
  processing workflow with the data; this lesson's record is a minimal sufficient form
  for a geophysical dataset.
- **Operational handover.** A processing sequence that must be re-run next season, by a
  different crew, on different software, is exactly the case where the record earns its
  keep.

## 15. Further reading

- **Donoho, D. L. (2010). An invitation to reproducible computational research.
  *Biostatistics*, 11(3), 385–388.** A short and influential statement of the problem
  and of what a record must contain. Level: accessible.
- **Buckheit, J. B., & Donoho, D. L. (1995). WaveLab and reproducible research.** In
  *Wavelets and Statistics*, Springer. The origin of the "reproducible research"
  formulation.
- **Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data
  management and stewardship. *Scientific Data*, 3, 160018.** Findable, Accessible,
  Interoperable, Reusable — the data-side counterpart of this lesson.
- **Peng, R. D. (2011). Reproducible research in computational science. *Science*,
  334(6060), 1226–1227.** A concise statement of the levels in Section 2.1.
- **USGS data and software release policies** — <https://www.usgs.gov> — an example of
  an agency-level requirement for documented processing chains.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 16. Related lessons

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — the stages the record must describe.
- [05-06-05 Gridding, Merging and Levelling of Survey Data](./05-merge-and-regularisation.md) — the interpolator, depth and band limits that must be recorded.
- [05-05-05 Acquisition QC](../05-survey-design-and-acquisition/05-quality-control.md) — the metadata that must be captured in the field.
- [22-02-01 The Reproducibility Crisis](../../22-data-engineering-reproducibility/02-reproducible-workflows/01-reproducibility-crisis.md) — the general problem.
- [22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md) — the vocabularies and formats.

## 17. Self-assessment checklist

- [ ] I can name the four levels of reproducibility and say which one a claim asserts.
- [ ] I can write a machine-readable processing record with input, ordered steps, parameters, environment and output.
- [ ] I can verify a record by re-execution and state the scope of a bit-identical result.
- [ ] I can demonstrate that order changes the result and quote the measured difference.
- [ ] I can choose between text comparison and result comparison, and state a tolerance.
- [ ] I can list the sources of irreproducibility and rank them by frequency.
- [ ] I can state what a processing report must contain and why each item is needed.
- [ ] I can explain why a hash must be accompanied by units.
