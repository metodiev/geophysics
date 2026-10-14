# Solutions — 22-07-03 Regression Testing Against Known Results

> Read after attempting. Numbers are measured on this platform's IEEE-754 doubles or come
> from the lesson's SYNTHETIC pipeline. Lesson:
> [03 Regression Testing Against Known Results](../03-regression-testing-data.md).

---

## ★1 — The three obligations

1. **Someone must know what the value should be** — an independent source, a closed-form
   case, a published dataset, or an audited physical result.
2. **The tolerance must be justified by arithmetic** — measured round-off floor, dtype and
   problem size stated.
3. **The value must be invalidated deliberately** — a defined invalidation rule, a
   reblessing process and a reviewer.

A tolerance satisfies only the second, and only if it was measured; the demonstration's
cancellation case shows that a perfectly justified tolerance cannot rescue a golden derived
from a bad formula.

## ★2 — A floor of 4e-13

(a) A tolerance two orders of magnitude above the floor: `rtol = 1e-11` (with an explicit
`atol` for values near zero — say `atol = 1e-30` for values of order 1 down to 1e-16, or an
`atol` matched to the smallest meaningful magnitude of the quantity).

(b) Headroom $= 10^{-11}/4\times10^{-13} = 25$, which is the *minimum* acceptable; a safer
choice is $10^{-10}$ (250× headroom). The smallest error still caught is of order the
tolerance: $10^{-11}$, i.e. a change of 0.000 000 001 % of the value. Anything smaller is
deliberately classified as round-off.

(c) Record: the measured floor (4e-13, and how it was measured — two orderings, two dtypes,
two thread counts), the tolerance and its headroom, the dtype, the problem size, the platform
on which the measurement was taken, and the reason this value is the reference.

## ★3 — The eight fields

Value; tolerance (`atol`/`rtol` with the measured floor); dtype; seed and input identifier;
platform; code version; environment (lock file hash or container digest); reviewer, date and
the **reason** the value is correct. The reason is the field that keeps a golden honest: it is
the only one that does not change if the code changes, so it is what a maintainer must argue
with.

## ★★4 — Variance of a large-offset series

(a) The two terms are $\mathbb{E}[x^2] \approx (5\times10^7)^2 + 4 = 2.5\times10^{15}$ and
$\mathbb{E}[x]^2 \approx 2.5\times10^{15}$; the quantity of interest, 4, is $10^{15}$ times
smaller than the terms. In double precision ($\varepsilon = 2.2\times10^{-16}$) each term
carries an absolute error of about $2.2\times10^{-16} \times 2.5\times10^{15} \approx 0.55$,
so the difference has an error of order 1 against a value of 4 — roughly 25 % error, and the
sign is not guaranteed. (The demonstration's version, with a mean of $10^8$ and unit
variance, is even worse: an error of 500 % and a negative result.)

(b) Two assertions a stored value does not provide: (i) the **property** `variance >= 0` (and
`variance <= (max-min)^2/4`), which catches the catastrophic form of the failure; (ii) an
**offset-invariance** metamorphic assertion — adding a constant to all values must leave the
variance unchanged to within the tolerance, which catches a formula that is losing the
offset.

(c) In float32 the resolution is 1.2e-07 while the squares reach $2.5\times10^{15}$; the
terms cannot be represented, so the formula returns a garbage number (the demonstration's
float32 result is −2 948 661 248.0). That is not inaccuracy but a breakdown of the
representation, which is why the dtype must be stated with the tolerance.

## ★★5 — Pipeline invalidation

(a) Total $= 0.3 + 0.7 + 1.2 + 5.0 + 2.0 + 0.5 + 0.2 = 9.9$ hours.

(b)

| changed stage | invalidated stages | cost (h) | share |
| :--- | ---: | ---: | ---: |
| `load` | 6 (`qc` … `report`) | 9.6 | 97.0 % |
| `qc` | 5 | 9.3 | 93.9 % |
| `grid` | 4 | 8.6 | 86.9 % |
| `invert` | 3 | 7.4 | 74.7 % |
| `post` | 2 | 0.7 | 7.1 % |
| `figures` | 1 | 0.2 | 2.0 % |
| `report` | 0 | 0.2 | 2.0 % |

(c) `figures` (and `report`): a change there invalidates at most 2 % of the pipeline, and
the figures are the stage most frequently edited for presentational reasons. Content-addressed
keys on the late stages are where the savings are; caching `load` is worth doing for other
reasons (it avoids re-reading the data), but its invalidation reach is inherently almost the
whole pipeline.

## ★★6 — `rtol = 1e-14` fails on a new machine

(a) Either (i) the two machines genuinely differ by more than 1e-14 — a different BLAS,
vectorisation, FMA contraction or reduction order, which the demonstration measures at
2.6e-14 for a reordered sum, larger than the tolerance; or (ii) the comparison is comparing
something that is not reproducible — reading uninitialised memory, hashing a set with
unstable ordering, or timing-dependent iteration order. Distinguish them by printing the two
values, their difference and the magnitudes involved: a difference at the round-off floor of
the magnitudes (a) is (i); a difference many orders of magnitude larger, or a difference that
changes between runs on the same machine, is (ii) and is a defect.

(b) At `rtol=1e-14` legitimate refactors alarm on **69.874 %** of changes (139 747 of
200 000 simulated); at `1e-12` the rate is effectively **0 %** (0 alarms in the same
simulation, with 25 alarms at 1e-13). The change: set the tolerance two orders of magnitude
above the **measured** floor on the two machines — for floors of 2.6e-14, `rtol=1e-12` is
the floor-plus-100 choice — and record both measured floors in the test.

(c) Before loosening: confirm the change is round-off, not a defect (compare the reference
against an independent implementation or a property); check the dtype; and check that the
difference does not grow with problem size, which would indicate an algorithmic change rather
than noise. Loosening to `1e-3` would stop catching units errors, formula errors of order
1e-4 and layout mistakes — i.e. it would leave only structural changes detectable.

## ★★★7 — Regression layer for a seismic processing pipeline

**Golden artefacts, each small.**

1. **A tiny synthetic shot gather** (a 2-D acoustic model with an analytic solution): the
   full wavefield for 50 receivers is small enough to version, and the answer is known
   independently.
2. **Summary statistics of the migrated image** for one audited field line: the image itself
   is far too large, but its envelope statistics, the position and amplitude of the brightest
   reflector, and the misfit measure are small and meaningful.
3. **Intermediate QC metrics** per stage (amplitude ranges, noise estimates, dead traces,
   the count of samples above a threshold), which localise a change to the stage responsible.

**Tolerance and its justification.** For each artefact, measure the floor: run the two
legal variants (FFT-based versus direct convolution, two orderings of a stack, float32 versus
float64) and take the largest relative difference; set the tolerance two orders above it and
record both numbers. For the analytic case, the tolerance is instead the discretisation error
measured across two grid refinements — a *convergence* assertion, not a round-off one.

**Properties instead of stored values.** Zero-offset symmetry of the correct wavefield;
receiver reciprocity; energy decay with time for a damped medium; the migrated image's
amplitude at the known reflector exceeding the background by a stated factor; the dead-trace
count in the QC metrics.

**Cache keys.** Per stage: the hash of the stage's code, the lock file, the container digest,
and the content hash of each input artefact (trace data, velocity model, processing
parameters). Any change to a stage's code invalidates its descendants, which is why the QC
metrics are recorded per stage: their diff names the stage that moved.

**Reblessing.** A golden may only change in a pull request that (i) states which artefact
changed, (ii) states the measured difference, (iii) states the cause, (iv) is approved by a
second person who understands that stage, and (v) records the new measured floor if the
change is a platform upgrade. Regeneration is performed by a script committed in the same
pull request.

**The class it cannot detect.** A physically wrong but internally consistent processing
choice — a wrong taper, a wrong datum correction, a wrong polarity convention — that changes
all goldens *consistently*. Only validation against real data with independent ground truth,
or comparison with an independent implementation, addresses that.

## ★★★8 — Comparing against a closed commercial package

**What can be compared.** Values at a small set of points (a known analytic model), summary
statistics of a real dataset (misfit distributions, amplitude spectra, reflector positions),
derived quantities (gradients or adjoints of a chosen objective, which test more of the code
than a forward value), and behaviour under parameter changes (a perturbation test: perturb one
parameter and compare the *ratio* of the two packages' changes, which cancels much of the
implementation difference).

**Tolerance measurement.** On a fixed case, run both packages twice on the same machine (to
measure each one's own reproducibility — a threaded or randomised solver may not be
reproducible at all), then across machines, then at different problem sizes. The tolerance is
taken from the larger of the two packages' own floors, with headroom, and the floors are
recorded. If a package is not reproducible with itself, only statistics can be compared.

**Versioning and recording.** Record the package version, the licence environment, the
platform, the case definition and the raw reference outputs as artefacts, plus the date of
the comparison. Keep the reference outputs with the same eight-field provenance as any golden
and state that the reference is a *comparison*, not a truth.

**A version change.** Treat it as a new measurement, not a reblessing: run the old and new
versions against the case, quantify the difference, and record whether the difference is
within the floors. Escalate a difference larger than the rounds-off floors to the vendor with
the case files, and disclose the difference in publications that rely on the comparison.

**Honest statement to publish.** "Compared against package X, version Y, on platform Z, for
case C: agreement to within A relative at the points tested, with the differences shown in
Figure N." Never "validated against package X" — agreement is not validation.

**Two ways it could mislead.** (i) The commercial package may be wrong in the same way (a
common convention or formula error), which agreement cannot detect; (ii) the comparison may
be made on cases where the physics is not exercised (a homogeneous model, a 1-D profile), so
agreement proves nothing about the interesting regime. Both are addressed by comparing
*perturbations* on heterogeneous, anisotropic cases.

## ★★★9 — "We compare it bitwise, so we catch everything"

**False-alarm rate and the suite's lifetime.** Bitwise comparison sits above the
`rtol=1e-14` row of the lesson's table, where legitimate refactors alarm on **69.874 %** of
changes (139 747 of 200 000 simulated perturbations at the measured floor 2.6e-14). Any
compiler, BLAS or thread-count change moves the bits; the realistic lifetime of such a test
is until the first such change, after which it is regenerated, and after the second
regeneration it compares the machine with itself.

**What bitwise comparison genuinely catches.** Every difference in the artefact, including a
single wrongly rounded value, an ordering change, a missing record, a changed dtype, and any
change in a quantity that *must* be exact: record counts, identifiers, masks, checksums,
integer indices, file schemas.

**Three assertions to add in place of the bytes.** (i) A small audited case with an
independently known answer and a measured tolerance; (ii) properties of the large output —
mass or energy balance, finiteness, value ranges, record counts, per-record checksums of the
inputs; (iii) a comparison against a *second* implementation or a higher-precision variant,
which turns "the bits changed" into "the answer changed by this much, and here is why".

**Costs of the large file.** Repository size and clone time for everyone; review burden
(a 40 MB diff cannot be reviewed, so approvals become rubber stamps); merge conflicts in a
binary or generated file; and the temptation to regenerate it, which deletes the test.
Version-controlled goldens should be small enough to read in a diff.

**When bitwise comparison is right.** When the artefact is produced by exact integer or
string operations and must not change: a checksum manifest, a schema file, an index, a
catalogue's identifier ordering, a serialised configuration; and when a byte-level difference
is itself the defect — for example a reproducibility test asserting that the same seed
produces the same bytes.
