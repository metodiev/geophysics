# Solutions — 22-02-02 Pinning Environments and Managing Dependencies

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [02 Pinning Environments and Managing Dependencies](../02-environment-pinning.md).

---

## ★1 — The six components

1. The interpreter/library runtime, with version and build.
2. Direct dependencies with versions.
3. Transitive dependencies (the closure).
4. System libraries and toolchain (BLAS/LAPACK, compiler, MPI, CUDA).
5. Hardware and scheduling (CPU generation, core count, thread count).
6. Versioned input data and configuration.

A `requirements.txt` naming only direct dependencies is silent about **items 3–5**,
and it is item 3 — the transitive closure, 960 packages by depth 6 in the
demonstration's model — that the solver chooses rather than the author.

## ★2 — Size of the unpinned space

(a) $40 \times \log_{10} 6.2 = 40 \times 0.79239 = 31.70$. The printed value is
30.9, which is lower because the demonstration draws each dependency's release
count as an integer in $\{3,\dots,9\}$ and sums the actual $\log_{10}$ values
rather than using the mean. The two figures agree to within one order of
magnitude, which is the precision the argument needs: the space is about
$10^{31}$ by the mean and $10^{30.9}$ as printed.

(b) $P(\text{two unpinned installs agree}) = V^{-1} = 10^{-30.9}$.

(c) Real solvers share preference rules, mirrors and constraint geometry, so
installs made close in time tend to make the same choices; the product is an
unconstrained upper bound on the freedom, so the true collision probability is
larger than $10^{-30.9}$ — but still far smaller than one.

## ★3 — The four levels and silent re-uploads

| Level | Detects a silent re-upload? |
|---|---|
| 1. Floating ranges | No |
| 2. Exact versions | No — the version is unchanged by definition |
| 3. Lock file with hashes | **Yes**, in proportion to coverage |
| 4. Container digest | **Yes** — the digest changes if any byte of the image changes |

## ★★4 — Hash coverage

(a) Coverage $= 45/180 = 0.250$. The probability that a single silent change is
detected equals the coverage: **0.250**.

(b) Expected silent changes $= 0.03 \times 180 = 5.4$. Expected detected
$= 5.4 \times 0.25 = 1.35$.

(c) To detect at least half of the silent changes the expected detected count must
be at least half the expected changes, i.e. coverage $\ge 0.50$, which here means
hashes for at least **90 of the 180** artefacts. Because detection is a binomial
sampling of coverage, at coverage 0.5 there is still substantial run-to-run
variation in how many of the 5.4 expected changes are caught.

## ★★5 — Closure growth

(a) Start 6; level 1: $6 \times 2.2 = 13.2$; level 2: $13.2 \times 2.2 = 29.04$;
level 3: $29.04 \times 2.2 = 63.888$. The demonstration truncates each level to an
integer before adding it — $13 + 29 + 63 = 105$, cumulative $6 + 105 = 111$ —
which is why the hand computation with rounding ($14 + 29 + 64$) gives 112 and the
printed value is 111. The difference is the truncation convention in the demo, not
a difference in the model.

(b) Continuing with the same truncation: level 4 $= 140.6 \to 140$ (cumulative
251); level 5 $= 309.2 \to 309$ (cumulative 560); level 6 $= 680.2$ capped to
$400$ (cumulative 960); levels 7 and 8 are also capped at 400 → cumulative
$960 + 400 + 400 = 1760$.

(c) Two differences from a real closure, with directions:

1. **No sharing.** Real closures re-use packages across branches, so distinct
   packages grow sub-exponentially; the model's factor 2.2 without deduplication
   **overstates** growth at large depth.
2. **No pruning.** Real solvers drop optional and platform-irrelevant
   dependencies; the model includes everything, again **overstating** the count.
   Both errors point the same way, so 960 is an upper-ish estimate of closure
   size for the modelled shape.

## ★★6 — A difference in the fourth significant digit

The two most likely components:

1. **A rebuilt artefact at the same version** (item 1 or 2 of §2): a wheel with a
   different BLAS/LAPACK build changes reduction order and hence the last digits —
   the effect is real and was measured at a relative $1.04 \times 10^{-7}$ between
   float32 and float64 accumulation of a million samples in
   [22-02-06](../06-containers-reproducibility.md).
2. **Hardware and scheduling** (item 5): a different thread count or CPU
   generation changes the order of floating-point additions in a reduction.

The single change that would discriminate: **ship a container with a digest** (level
4 pinning) and report the figure's number computed inside it. If the reviewer's
number then matches, the cause was the environment; if it still differs, the cause
is in the arithmetic or the data, and the search moves to the data version and the
accumulation dtype.

## ★★★7 — A ten-year release policy

**Pinning level.** Level 3 for development (a lock file with hashes, solved for
each supported platform) and level 4 for each *published* figure (a container
image referenced by digest, archived alongside the release). Both are needed:
the lock file keeps day-to-day work reproducible, the digest is what survives a
decade of registry drift.

**Per-platform handling.** Never ship a single lock for several operating systems.
Produce one lock per supported platform from a clean solve in the target base
image, and record which lock produced which figure. Wheels and builds differ by
platform, so a cross-platform lock is a false claim.

**CI check.** On every change, install *from the lock file* on a clean runner,
then run the tests. This is the check that detects a yanked artefact or an
unavailable index — the failure that appears on a reader's machine. Archive the
resolved artefact hashes with the release so a future reader can compare.

**Upgrade procedure.** Upgrades happen in a branch, one dependency family at a
time, with the full test suite as the referee and the numerical differences
recorded. An upgrade is treated as a method change until the tests say otherwise,
and the release notes record the version transitions.

**The component no policy freezes.** The **host CPU and its scheduling** — thread
count, SIMD width, BLAS threading decisions. A digest pins the software, not the
arithmetic.

**What the policy cannot guarantee.** That the numbers are *correct* (they could
be reproducibly wrong), and that the container registry will still serve the
digest in ten years — which is why the archive, not the registry, owns the
release, and why a checksum of the image is recorded with the paper.

## ★★8 — Incompatible dependencies and infeasibility

**How a lock workflow surfaces it.** A resolver works on the whole constraint set
at once and reports the conflict explicitly (which requirements, which versions,
which dependency chain) instead of silently choosing an older combination. The
failure appears at *lock time*, on the author's machine, rather than at install
time on a reader's.

**Quantifying the infeasible region.** Enumerate the candidate versions of the two
conflicting dependencies (for example $a \in \{a_1..a_m\}$ and
$b \in \{b_1..b_n\}$) and evaluate the constraint predicates on every pair, giving
an $m \times n$ boolean matrix. Report the fraction of pairs that are infeasible
and the boundary (the newest $a$ compatible with each $b$). That matrix is the
evidence for the claim that the conflict is unavoidable at the current versions,
rather than an artefact of the solver's search order.

**Why "upgrade everything" is not a solution.** If the offending dependency is not
under your control, its newest version may simply be incompatible with the other
project's newest version; upgrading converts a known incompatibility into an
unknown one and may break the other side. The available moves are: pin the last
mutually compatible pair and record it; contribute the constraint fix upstream;
isolate the two uses in separate environments and exchange data through a file or
a stable interface; or replace one of the dependencies. Each is a documented
decision, and the constraint matrix is what makes the decision defensible.

## ★★★9 — Measuring real detection performance

**Data.** For each of the group's lock files, the recorded artefact hashes
together with an *external* record of what the artefact content actually was: an
artefact-repository audit log (re-upload events, if the registry provides one), or
the group's own cache of downloaded artefacts with timestamps and hashes. Without
an external record the measurement is circular — the lock file cannot testify to
its own coverage.

**Statistic.** The **detection rate** — the fraction of externally observed
re-uploads (artefact, version) whose content hash differs from the hash recorded
in the lock file at that time. Report it per registry and per artefact type
(wheels, sdists, conda packages), with a binomial confidence interval, because
re-upload rates vary by ecosystem and by artefact type.

**Two ways the measurement can overstate protection.**

1. **Coverage counted, not verified.** A lock file can *list* a hash for an
   artefact that was never actually verified at install time (a `--no-deps`
   install, a cached artefact, a skipped check). Measuring "hashes present" rather
   than "hashes compared" overstates detection.
2. **Survivorship in the cache.** Artefacts that were re-uploaded and never
   downloaded again cannot appear as a difference, so the denominator counts only
   the artefacts the group happened to re-fetch; the rate is then estimated on the
   subset most likely to be stable. Report the denominator explicitly and state
   the observation window.
