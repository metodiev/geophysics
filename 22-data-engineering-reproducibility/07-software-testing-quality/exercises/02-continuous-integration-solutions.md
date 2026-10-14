# Solutions — 22-07-02 Continuous Integration for Research Software

> Read after attempting. Numbers use the lesson's SYNTHETIC model. Lesson:
> [02 Continuous Integration for Research Software](../02-continuous-integration.md).

---

## ★1 — The suite-level red rate

$$P(\text{red}) = 1 - (1-p)^N.$$

Assumptions: (i) the $N$ tests fail **independently** — a shared network, a full disk or a
loaded runner breaks this; (ii) each test fails **without a code change**, so the flake rate
$p$ is a property of the environment, not of the commit. A third, implicit assumption is
that the flake rate is stable across pushes; a rate that changes with machine load makes the
formula a long-run average only.

## ★2 — A 30-job matrix

(a) Jobs $= 2 \times 5 \times 3 = 30$; per job $= 1 + 1.5 + 5 = 7.5$ min; machine-minutes
$= 30 \times 7.5 = 225$.

(b) With $R$ runners, waves $= \lceil 30/R \rceil$ and wall $=$ waves $\times 7.5$:
$R=4 \to 8$ waves $= 60.0$ min; $R=10 \to 3$ waves $= 22.5$ min; $R=30 \to 1$ wave
$= 7.5$ min. The floor is one job, 7.5 min.

(c) Reduce the job duration: install from a warm dependency cache, split the test suite, or
move the expensive combinations to a nightly job so the push-triggered lane has fewer, faster
jobs. Adding runners beyond 30 changes nothing at all.

## ★3 — Laptop versus CI

CI can check: (i) that the package **installs from the lock file in a clean environment**
(the developer's machine has residue from earlier work); (ii) behaviour on **another
operating system or interpreter version**; (iii) that the **full suite passes without local
data**, credentials or an uncommitted working tree. Neither can check whether the model is
the right model — verification and validation
([19-07](../../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md))
is a separate activity.

## ★★4 — One flaky test in 300

(a) $P(\text{red}) = 1 - 0.996^{300} = 1 - e^{-1.2024} = 0.6995$, so about 70 % of pushes
are red because of one test with a 0.4 % flake rate.

(b) Posterior $= \dfrac{0.15}{0.15 + 0.85 \times 0.6995} = \dfrac{0.15}{0.7446} = 0.201$.
A red build means "probably real" only with probability 20 %; four in five red builds are
noise.

(c) Pushes $= 15 \times 220 = 3\,300$ per year; red builds
$= 3\,300 \times 0.6995 \approx 2\,308$ — of which about
$0.85 \times 3\,300 \times 0.6995 \approx 1\,962$ are spurious. That is roughly nine
spurious reds per working day, each interrupting someone's work.

## ★★5 — Silent retries

(a) With three attempts the chance that the flaky test fails all three is
$p^3 = 6.4\times10^{-8}$, so
$P(\text{red}) = 1 - (1 - 6.4\times10^{-8})^{300} \approx 1.9\times10^{-5}$ — two red builds
per 100 000 pushes. The retry is enormously effective against noise.

(b) A bug failing one test in 8 runs has $p = 0.125$; with three attempts the push looks
green unless all three attempts fail the test:
$1 - (1 - 0.125^3)^{300} = 1 - (1 - 1.953\times10^{-3})^{300} = 1 - e^{-0.586} = 0.443$.
So a **real bug that would fail 12.5 % of runs looks green in 44.3 % of pushes** — the same
mechanism that removed the noise removed the signal.

(c) Policy: (i) never retry silently — a retry opens a record naming the test, the commit
and the log; (ii) distinguish the two cases by measurement: loop the suspect test 100–1 000
times and compute its empirical failure rate — a flake near $10^{-3}$ under load is
infrastructure, a rate near $10^{-1}$ is a defect; (iii) fix or quarantine with an owner and
a deadline, listed in the issue tracker. The distinguishing measurement is the **failure
rate and its dependence on load or ordering**: a defect often fails more often with
concurrency or with a different test order, while an infrastructure flake fails when the
runner is busy.

## ★★6 — Sharding ten files into five shards

(a) Contiguous pairs in listing order: $(600+500,\ 450+400,\ 350+300,\ 200+100,\ 60+40)
= (1\,100,\ 850,\ 650,\ 300,\ 100)$ s. Wall time $= 1\,100$ s.

(b) Longest-file-first onto the least loaded shard:

| file | shard loads after assignment |
| ---: | :--- |
| 600 | 600, 0, 0, 0, 0 |
| 500 | 600, 500, 0, 0, 0 |
| 450 | 600, 500, 450, 0, 0 |
| 400 | 600, 500, 450, 400, 0 |
| 350 | 600, 500, 450, 400, 350 |
| 300 | 600, 500, 450, 400, 650 |
| 200 | 600, 500, 450, 600, 650 |
| 100 | 600, 500, 550, 600, 650 |
| 60 | 600, 560, 550, 600, 650 |
| 40 | 600, 560, 590, 600, 650 |

Shard times $(600, 560, 590, 600, 650)$ s, wall time $= 650$ s — a **41 %** reduction from
1 100 s at identical machine-minutes.

(c) The floor is the largest single file, **600 s**, against an ideal of
$3\,000/5 = 600$ s: this particular assignment is optimal. To go below it you must split
that file (or cache what it recomputes): sharding moves work between runners, it never
removes work.

## ★★★7 — A pipeline for library, Fortran kernel, workflow and paper

**Jobs and triggers.**

| job | trigger | duration | checks |
| :--- | :--- | ---: | :--- |
| lint and import check | push | 1 min | style, unused imports, no syntax errors, no accidental absolute paths |
| fast test lane | push | 5 min | unit tests, one interpreter, one system, warm cache |
| build the Fortran kernel | push | 4 min | the wrapper compiles the kernel; the compiled extension imports and runs a smoke call |
| numerical goldens | push | 3 min | tolerance tests and the recorded spread of the golden values |
| docs and metadata | push | 2 min | docstring examples, citation file parses, version string matches the tag |
| full matrix | nightly | 25 min | all systems and interpreter versions, cold install from the lock file |
| workflow dry run | nightly | 20 min | Snakemake dry-run plus a two-stage run on a fixture dataset |
| paper build | nightly + tag | 8 min | figure script on fixtures, then the document compiles from a clean checkout |
| benchmark record | nightly | 10 min | the short benchmark's time and operation counts appended to the trend store |
| release | tag | 40 min | wheel and container build, install from the artifact, run the goldens inside the container |

**Fast lane**: lint, the fast test lane, the kernel build and the goldens — about 13 min, and
the only jobs a merge depends on. Everything long, platform-specific or network-dependent
runs nightly or on a tag.

**Cache and artifacts.** Cache the dependency installation keyed by the lock file hash; cache
the compiled kernel keyed by the compiler version and source hash; publish the wheel, the
container and the benchmark record as artifacts, because the artifact is the thing a reviewer
or a reader can install.

**Goldens.** One audited small case per kernel with the tolerance derived from a measured
spread, plus property tests that need no stored value. The golden file records dtype,
platform, seed, code version and the tolerance's justification, so a future maintainer can
tell a platform shift from a defect.

**Network-dependent tests.** Never in the merge gate. The nightly workflow job uses a
versioned fixture; a separate, optional job checks the real remote data and its failure is
reported as an infrastructure event, not as a red build.

**Expected dominant failures, and their measurement.** (i) **Flakes from the shared build
machines**, measured as `retries / pushes` per test name; the fix is to reduce job-level
parallelism or pin resources, not to retry silently. (ii) **Environment drift between the
cache and the lock file**, measured as the fraction of nightly jobs that pass cold but fail
warm (and vice versa); the fix is to keep the cold install in the nightly matrix and treat a
cache-key bug as a defect. Both are measured from the build history, not from intuition.

## ★★★8 — A pipeline that no longer builds

**Evidence to collect.** The build logs from the original run (if retained), the lock file
or exported environment at the time of the run, the repository tag or commit and its
history, any recorded data versions or checksums, the container image digest if one exists,
and the published outputs with their metadata.

**Four candidate causes and the distinguishing check.**

1. **The lock file was never committed** (or was committed later, after edits). Check: does
   the tag contain a lock file? Does it resolve to the versions in the published
   environment? Distinguishes "no record" from "record with wrong content".
2. **A dependency was yanked, replaced or its transitive resolution changed.** Check:
   attempt the install with the recorded constraints and read the resolver's error; a
   version that no longer exists on the index or a build that needs a compiler version the
   base image lacks appears here.
3. **The code path depended on something outside the repository** — a local file, an
   environment variable, an absolute path, an uncommitted script. Check: run in a clean
   container with no environment variables and see which step fails; the error names the
   missing external.
4. **The pipeline depends on a service or a dataset that has changed** (an API, a
   re-released dataset, a moved archive). Check: compare the recorded data version or
   checksum with what the step fetches now.

**Preventive change.** Every published result is produced by a tag whose build was recorded
as an artifact: a lock file committed with the tag, a container image by digest, a manifest
of input data versions, and a CI job that reruns the pipeline from that tag against the
versioned inputs. The nightly pipeline then acts as a reproducibility test of the *last
release*, not only of the current branch.

**If the environment cannot be rebuilt.** Publish what is honest: the code at the tag, the
recorded versions and constraints, the input data versions, the published outputs, and a
statement of what could not be re-executed and why — plus a rebuilt pipeline that reproduces
the *analysis* on the current environment, with a comparison against the published numbers
stating the differences. An unreproducible environment is a finding to report, not a reason
to publish nothing.

## ★★★9 — Dropping the matrix and dropping retries

**The matrix protects against portability defects**: assumptions about integer size, byte
order, filesystem case sensitivity, path separators, locale-dependent parsing and sorting,
default text encodings, `fork` versus `spawn` process start, and dependency versions that
differ by platform. None of these appear on the developers' single system, and all of them
break a reader's attempt to run the code — which is the audience a research package has.

**Cost of keeping it as a nightly job**: 24 jobs × 8.5 min ≈ 204 machine-minutes per night,
which is small in absolute terms, and it costs no human attention because it does not block a
merge. The honest counter-argument is that a nightly failure is discovered a day late and its
fix is context-switched; that argues for a *fast* multi-platform lane (two systems, newest
interpreter, 2 jobs) on push and the full matrix nightly.

**Evidence about whether flakiness is a test problem or a scheduling problem.** Record, per
test: the failure rate, the runner or job identity, the wall time of the job, and whether the
failure correlates with parallel load, with a specific machine or with ordering. If failures
cluster on one runner type or under high concurrency, it is infrastructure; if they persist on
an idle machine with the same test alone, it is the test.

**Combined policy.** One system on push with the newest interpreter plus the full matrix
nightly; retries retained but instrumented (every retry recorded, per-test rates published in
the build summary); a quarantine list with owners and deadlines; and a rule that a test may
only be removed from the suite by a pull request that says which defect class it covered and
what now covers it.

**The measurement that decides the argument.** Two weeks of retry records: the number of
retries per push, the distribution of per-test failure rates, and the correlation with runner
identity and load. If retries are frequent and clustered on machines, dropping retries
penalises developers for infrastructure — reject that proposal. If there is a single test
with a rate above 1 % under all conditions, dropping retries and fixing that test is right.
**The proposal to accept** in the PI's list is dropping *retries without fixing flaky tests*
only if the records show no clustering; and the matrix reduction to a two-job push lane is
acceptable, since its portability protection is preserved nightly.
