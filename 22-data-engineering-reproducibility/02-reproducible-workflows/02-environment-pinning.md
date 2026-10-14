---
id: 22-02-02
title: "Pinning Environments and Managing Dependencies"
level: advanced
prereqs: ["22-02-01", "22-01-05"]
estimated_minutes: 45
tags: [dependencies, environments, reproducibility, lock-files, software-engineering]
---

# Pinning Environments and Managing Dependencies

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** an environment as a solved set of artefacts, and **list** the six
   components that decide a run's numbers.
2. **Compute** the size of an unpinned environment's admissible version space, and
   **state** what that size implies for two independent installs.
3. **Distinguish** four levels of pinning — floating ranges, exact versions, a
   lock file with hashes, and a container digest — and **say** what each detects.
4. **Compute** the detection probability of a silent artefact change from hash
   coverage, and **explain** why a version string is not evidence.
5. **Quantify** the growth of the transitive dependency closure and **explain**
   why the lock file, not the human, must own it.
6. **Diagnose** an environment failure from a solver error or a drifting result,
   and **prescribe** the pinning change that removes it.

The environment numbers in this lesson are **SYNTHETIC**: the dependency set and
its admissible ranges are generated with chosen parameters, and the closure growth
is a chosen branching model. No package index is queried and no lock file is read.

## Prerequisites

- [22-02-01 The Reproducibility Problem in the Computational Sciences](./01-reproducibility-crisis.md) —
  the failure taxonomy this lesson addresses for the environment category.
- [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md) —
  the version arithmetic that citations and environments share.

## 1. Intuition: the environment is part of the method

A numerical result is produced by code **executed by a particular set of
artefacts**. Change a library and the result may change; the change may be a
different rounding order, a changed default, a bug fix, or a different algorithm
selected for the same call. An environment file is therefore not housekeeping — it
is the part of the method that says *which implementation of each operation ran*.

The practical statement "it worked on my machine" is a statement about one draw
from a very large space, and the demonstration puts a number on the space: 40
direct dependencies with a mean of 6.2 admissible releases each admit
$10^{30.9}$ combinations. Two unpinned installs agreeing is a
$10^{-30.9}$ event. What made it work was not skill but the fact that both
installs happened to make the same choices — usually because they were close in
time.

## 2. What an environment actually contains

Six components decide a run's numbers, and only the first two are usually
recorded:

1. **The interpreter/library runtime**, with its version and build
   (`python 3.11.7`, a conda build string, a container digest).
2. **Direct dependencies**, with versions.
3. **Transitive dependencies**, the closure reached through those — the
   demonstration's model reaches 960 packages by depth 6.
4. **System libraries and the toolchain**: BLAS/LAPACK implementation, compiler,
   MPI, CUDA.
5. **Hardware and scheduling**: CPU generation, core count, thread count.
6. **Input data and configuration**, in their versioned form.

Items 3–5 are the ones that make an environment irreproducible in practice: they
are large (item 3), invisible in the file a human writes (item 4), or outside the
software at all (item 5).

## 3. Sizes, and what they mean

With $v_i$ admissible releases of dependency $i$, the number of admissible
combinations of an unpinned install is

$$V = \prod_{i=1}^{N} v_i, \qquad \log_{10} V = \sum_{i=1}^{N} \log_{10} v_i .$$

For the demonstration's synthetic environment, $\log_{10} V = 30.9$, so
$V \approx 8 \times 10^{30}$ combinations. The probability that two independent
unpinned installs resolve to the same combination is $V^{-1} = 10^{-30.9}$ before
any further constraints. This is not a lower bound on how often problems occur:
in practice solvers share preferences and mirrors, and the shared constraints make
agreement far more likely than $10^{-30.9}$. The useful statement is the directional
one — the space is astronomically larger than any engineer's mental model of it,
which is why "the same requirements file" is not a reproducibility claim.

## 4. Four levels of pinning

| Level | File content | Reproduces | Detects a silent re-upload |
|---|---|---|---|
| 1. Floating ranges | `numpy>=1.4,<2` | one draw from the space | no |
| 2. Exact versions | `numpy==1.26.4` | the version, not the build | no |
| 3. Lock file with hashes | every artefact, version and hash | version and build | yes |
| 4. Container digest | a digest pinning the whole image | the whole machine image | yes |

Level 2 is the level most projects reach and is a large improvement over level 1:
it removes the resolution freedom and makes the version set explicit. It is not
sufficient, for two reasons: the same version can be published with a different
build (a wheel rebuilt against a different BLAS), and the *transitive* set is
still resolved by the solver unless the lock file records it.

Level 3 is the level to aim for. A lock file produced by a resolver records every
transitive artefact with its version and a hash of its content, which makes the
install verifiable rather than merely specified. For Python, tools such as
`pip-compile`, `uv` or `conda-lock` produce such files; the names matter less than
the property: **every artefact is named and hashed**.

## 5. Hashes: what they detect

A version string is an assertion by the publisher; a hash is evidence about the
content. With $k$ of $n$ artefacts carrying recorded hashes and a fraction $p$ of
artefacts silently re-uploaded at the same version string, the detection
probability is the **coverage** $k/n$ of the hash set (for a single changed
artefact). The demonstration's SYNTHETIC model with $n = 60$ and $p = 2\ \%$
gives an expected 1.20 silent changes and:

| Hashes recorded | Coverage | $P(\text{change detected})$ |
|---|---|---|
| 0 | 0.000 | 0.000 |
| 1 | 0.017 | 0.017 |
| 10 | 0.167 | 0.167 |
| 30 | 0.500 | 0.500 |
| 60 | 1.000 | 1.000 |

Half-measures are exactly half-measures: a lock file with hashes for a third of
the artefacts detects a third of the silent changes. Note also what hashes do not
detect: a change made *before* the environment was locked, a changed *default* in
an unchanged artefact, and any drift in components 4–6 of §2.

## 6. The closure is the part a human never reads

The demonstration's chosen branching model (factor 2.2 per depth, capped at 400
new packages per level) reaches 19, 48, 111, 251, 560 and 960 packages after six
depth levels. Nothing about that growth is extraordinary; it is what a modern
scientific stack looks like from inside a solver. Two consequences:

1. **A human-written requirements file cannot pin the closure.** It is
   unreadable at that size and changes with every solve. The lock file must be
   generated by the resolver and committed to the repository.
2. **The closure is where a breaking change usually arrives.** The direct
   dependencies were chosen deliberately; the closure was chosen by a solver.

## 7. Practice: rules that hold up

1. **Commit the lock file.** It is the environment; a repository with only a
   human-written list has specified inputs and an unspecified environment.
2. **Record the solve platform.** Wheels and builds differ by platform; a lock
   produced for one operating system is not a lock for another. Either produce one
   lock per target or record the image the lock was solved in.
3. **One environment per deliverable.** A figure's environment and a web
   application's environment have different stability requirements; sharing one
   file couples them.
4. **Test the solve in CI.** Install from the lock file on a clean machine and run
   the tests. This detects a yanked artefact or an unavailable index — the failure
   that appears on a reader's machine and not on yours.
5. **Upgrade deliberately, in a branch, with the tests as the referee.** Upgrade
   the lock, run the suite, and record the numerical differences: an upgrade is a
   change of method until the tests say otherwise.
6. **Do not edit the lock by hand.** A lock file is a solver output; a hand edit
   makes the next solve inconsistent with it.

## 8. Worked example: diagnosing a drift

A figure produced in March does not reproduce in November. The code is unchanged
and the requirements file is unchanged. Work through the possibilities:

1. **Was the environment pinned at all?** With floating ranges, the November
   solve is a different draw from a $10^{30.9}$ space; check the resolution date
   and the versions actually installed at the time if a log exists.
2. **Was the *closure* pinned?** Even exact direct pins leave the closure to the
   solver; the demonstration's closure reaches 960 packages by depth 6, so an
   unpinned closure is the likely culprit.
3. **Was the artefact content pinned?** Builds at the same version differ; without
   hashes, a rebuilt wheel with a different BLAS changes floating-point results in
   the last digits.
4. **Did the machine change?** Thread count and CPU affect reduction order; a
   relative difference of $1.04 \times 10^{-7}$ was measured between float32 and
   float64 accumulation of a million samples in
   [22-02-06](06-containers-reproducibility.md), which is the scale of the
   arithmetic effect.
5. **Which of the two numbers is right?** Neither is established by this analysis:
   the reproduction protocol tells you whether the number is stable, not whether
   it is correct. Correctness needs a reference (module 22-07).

The prescription follows from the diagnosis: a committed lock file with hashes,
solved for the target platform, plus the tests run in CI from that lock.

## Assumptions and regime of validity

1. **The version space is a product.** Real solves are constrained: shared
   dependencies, pinned minimum versions and platform wheels remove large regions
   of the product. The $10^{30.9}$ figure describes the *unconstrained* space and
   must be read as an order-of-magnitude statement about resolution freedom.
2. **Independence of dependencies.** The model treats each dependency's release
   count as independent; in a real ecosystem they are correlated through
   dependency constraints.
3. **Detection is coverage.** The hash table assumes one silently changed artefact
   and a hash set that is a uniform sample; correlated changes and partial
   coverage change the arithmetic.
4. **Closure growth is a chosen model.** A branching factor of 2.2 per level is a
   teaching value; real closures grow sub-exponentially because of shared
   dependencies.
5. **Pinning cannot freeze arithmetic.** A fully pinned container still runs on a
   host CPU whose reduction order may differ; the last bits are not pinned by any
   environment file.

## The honest summary

An environment is the set of artefacts that executed the method, and the
difference between a specification and a reproduction is whether that set is
recorded and verifiable. An unpinned install with 40 direct dependencies admits
some $10^{30.9}$ combinations; exact pins remove the resolution freedom but not
the closure, which the model grows to 960 packages by depth 6; a lock file with
hashes makes the install verifiable and detects a silently re-uploaded artefact in
proportion to its coverage (0.500 at 30 of 60 artefacts). The rules that survive
the arithmetic are: commit a lock file, include hashes, record the platform,
install from the lock in CI, and upgrade in a branch with the tests as the
referee. None of this establishes correctness — it establishes that the number you
report came from the environment you specified.

## Python demonstration

[`code/environment_pinning_demo.py`](./code/environment_pinning_demo.py) prints,
with `np.random.default_rng(20261014)`:

1. the admissible version space: 40 dependencies, mean 6.2 releases each,
   $10^{30.9}$ combinations, $10^{-30.9}$ chance of an accidental match;
2. what a lock file changes, at each of the four levels of §4;
3. the hash-coverage detection table (0.000, 0.017, 0.167, 0.500, 1.000);
4. the closure growth to 960 packages by depth 6.

```bash
cd 22-data-engineering-reproducibility/02-reproducible-workflows/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python environment_pinning_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/02-environment-pinning-exercises.md`](./exercises/02-environment-pinning-exercises.md)
and
[`exercises/02-environment-pinning-solutions.md`](./exercises/02-environment-pinning-solutions.md).

## Mastery checkpoint

Without notes: a project has 25 direct dependencies, each with an average of 6
admissible releases, and a closure 200 artefacts deep in total.

1. Compute the log-scale size of the unpinned space and the probability that two
   unpinned installs agree.
2. State what an exact-pin file fixes and what it leaves to the solver.
3. Compute the detection probability for a silent re-upload with hashes recorded
   for 50 of the 200 artefacts.
4. A colleague says "the CI passes on the lock file, so the paper's number is
   correct". State the two things the CI run does and does not establish.

## Common pitfalls

1. **Believing an unpinned requirements file is an environment.** It is a
   constraint set, and it admits $10^{30.9}$ combinations in the demonstration's
   model.
2. **Pinning only dependencies.** The runtime, the system libraries and the
   thread count are part of the environment.
3. **Editing a lock file by hand.** The next solve will not match it.
4. **Hashes for part of the closure.** Detection is coverage: 30 of 60 artefacts
   detects half the silent changes.
5. **One environment for everything.** Coupling a paper's figure to a web
   service's upgrade cadence makes the figure unreproducible for no benefit.
6. **Expecting a pinned environment to make results identical.** Reduction order
   and hardware still move the last digits.

## Where this is used

- **Paper artefacts** — the environment file is what makes the reviewer's run
  possible: see [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Containers** — level 4 pinning is the container digest: see
  [22-02-06 Containers for Computational Reproducibility](./06-containers-reproducibility.md).
- **Continuous integration** — testing the solve is the step that catches a
  vanished artefact before a reader does: see
  [22-07-02 Continuous Integration for Research Software](../07-software-testing-quality/02-continuous-integration.md).
- **Long-running model codes** — a decade-old code's result depends on the
  compiler and BLAS of the era, which only a lock file or an image preserves.

## Related lessons

- [22-02-01 The Reproducibility Problem in the Computational Sciences](./01-reproducibility-crisis.md) —
  where environment drift sits in the failure taxonomy.
- [22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect](./03-workflow-managers.md) —
  the tool that consumes the environment and reruns what changed.
- [22-02-06 Containers for Computational Reproducibility](./06-containers-reproducibility.md) —
  the same problem at the level of the whole machine.
- [22-01-05 Licensing, Citation and Software Credit](../01-research-software-engineering/05-licensing-and-citation.md) —
  version constraints as citation practice.

## Self-assessment checklist

- [ ] I can list the six components of an environment.
- [ ] I can compute the size of an unpinned version space.
- [ ] I can name the four levels of pinning and what each detects.
- [ ] I can compute a hash-coverage detection probability.
- [ ] I can explain why the closure must be pinned by a solver.
- [ ] I can state what pinning does not establish about a result.
