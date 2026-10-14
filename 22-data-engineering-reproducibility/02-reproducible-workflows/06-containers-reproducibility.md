---
id: 22-02-06
title: "Containers for Computational Reproducibility"
level: research
prereqs: ["22-02-02", "22-02-05"]
estimated_minutes: 50
tags: [containers, reproducibility, environments, docker, cloud]
---

# Containers for Computational Reproducibility

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** an image as an ordered stack of content-addressed layers, and
   **state** why layer order determines rebuild cost.
2. **Compute** an image's size and cold-build time from its recipe, and **predict**
   which layers rebuild when a given line changes.
3. **Quantify** the contribution of the analysis code to an image, and **state** the
   consequence for how a group should allocate effort.
4. **Distinguish** a pinned image from a reproducible one, and **compute** the
   probability that two unpinned builds agree bitwise.
5. **List** what a container does not freeze, including hardware, threading and
   external services.
6. **Decide** when a container is the right artefact and when a lock file is
   sufficient, and **justify** the choice by the failure it removes.

Image sizes, build times and drift probabilities in this lesson are **SYNTHETIC**
and chosen for teaching; no image was built, no registry was queried and no
benchmark of a real container system is quoted. The floating-point illustration is
a computation performed by the demonstration, labelled as such.

## Prerequisites

- [22-02-02 Pinning Environments and Managing Dependencies](./02-environment-pinning.md) —
  the four levels of pinning, of which a container digest is the fourth.
- [22-02-05 Data Versioning and Provenance Tracking](./05-data-versioning.md) —
  what to keep outside the image, and how to name it.

## 1. Intuition: a frozen filesystem with a declared entry point

A container image is a filesystem snapshot plus metadata describing the process to
run in it. Running the image gives a process that sees exactly the files, libraries
and interpreters in the snapshot, on any machine that can execute the container
runtime. For reproducibility this is the strongest of the four pinning levels: it
pins the operating system's libraries and the interpreter together, which a
dependency lock file cannot.

The cost follows from the same design. Everything in the image is carried to every
machine that runs it, so the image is the largest artefact a project publishes, and
its size is dominated by things the analyst did not write.

## 2. Layers: the cache is content addressing again

An image is built as an ordered stack of **layers**, each produced by one step of
the recipe. Each layer is content-addressed: if a step's inputs (the previous layer
plus the step's own files) are unchanged, the layer is reused from cache. Changing a
step therefore invalidates that layer **and every layer after it**, which is why
recipe order is a performance decision.

The demonstration's **SYNTHETIC** recipe has five layers:

| Layer | Size (MB) | Build (min) |
|---|---|---|
| base image (digest pinned) | 120.0 | 0.5 |
| apt packages | 340.0 | 4.0 |
| python packages | 410.0 | 6.5 |
| reference data | 900.0 | 2.0 |
| analysis code | 12.0 | 0.5 |
| **total** | **1782.0** | **13.5** |

Two numbers deserve attention. The image is **1.78 GB** and takes **13.5 minutes**
to build cold; the analysis code is **12 MB, 0.7 % of the image and 3.7 % of the
build time**. In every container discussion about reproducibility, the artefact
under discussion is the rounding error inside the environment.

## 3. Rebuild cost, and why order matters

When one layer changes, that layer and all later layers rebuild:

| Changed layer | Layers rebuilt | Rebuild time (min) |
|---|---|---|
| analysis code | 1 | 0.5 |
| reference data | 2 | 2.5 |
| python packages | 3 | 9.0 |
| apt packages | 4 | 13.0 |

The asymmetric cost is the whole design rule: **put the things that change most
often last**. A recipe that installs the analysis code before the package list
reattaches the 6.5-minute package build to every code edit; the same recipe with the
order reversed rebuilds in 30 seconds. Nothing about the resulting image differs —
only the cache behaviour.

## 4. Pinned or unpinned: the measured difference

"The same recipe" is not "the same image". If the recipe resolves packages at build
time — an unpinned `apt install` or a floating Python dependency — two builds
produce different visible layers even when every instruction is identical. The
demonstration models drift probabilities per floating family and computes the
probability that two builds are **bitwise identical**:

$$P(\text{identical}) = \prod_{\text{floating families}} (1 - p_{\text{drift}})
= 0.606 \quad \text{for the unpinned recipe},$$

against $1.000$ when every family is pinned by digest or content hash. The floating
payload in the modelled image is 1650 MB — roughly 93 % of the image depends on a
decision made at build time by a resolver rather than by the author.

The practical instruction is explicit: pin the **base image by digest**
(`@sha256:...`, not `:latest` or a tag), pin package versions and verify their
hashes, and record checksums for any file fetched during the build. A tag is a
mutable name; a digest is a content address, and only the second makes "we used
this image" a checkable statement.

## 5. What a container does not freeze

A container pins the software. It does not pin:

1. **The host CPU and its math libraries.** Reduction order in floating-point sums
   depends on vectorisation and threading. The demonstration measures a relative
   difference of $1.04 \times 10^{-7}$ between summing a million samples in float32
   and in float64 ($-845.3800$ against $-845.3801$), which is the scale of the
   effect that remains after the image is fixed.
2. **The thread count and scheduler.** `OMP_NUM_THREADS`, the number of MPI ranks and
   the CPU allocation change the order of operations in any parallel reduction.
3. **The clock and the network.** A container that fetches data at run time is only
   as reproducible as the service it calls; data belong in the provenance record
   ([22-02-05](05-data-versioning.md)), mounted by identifier, not baked in by URL.
4. **The external state.** Databases, licences, GPU drivers and shared filesystems
   live outside the image.

The consequence for practice is that a container removes *one* class of differences
(the software environment) and leaves the others; numerical results should therefore
be compared under a stated tolerance, not by exact equality, and the tolerance should
be justified by measurement rather than chosen for roundness.

## 6. Containers and licensing

Distributing an image distributes **everything inside it**, so the licence audit of
[22-01-05](../01-research-software-engineering/05-licensing-and-citation.md) applies
to every layer. A copyleft tool that appears in the recipe and never appears in the
published analysis still travels in the image, and with the demonstrated table of
licence pairs only 18 % are permissive-to-permissive. Two practical consequences:
keep the image minimal (a smaller image is also a simpler licence audit), and record
the audit in the release notes rather than assuming that "it is only used for a
figure" removes the obligation.

## 7. Practice: building images that survive

1. **Pin the base by digest.** A tag can be re-pointed; a digest cannot.
2. **Order layers by change frequency.** Base, then system packages, then language
   packages, then data, then code.
3. **Keep data and secrets out of the image.** Mount data by version identifier and
   pass secrets at run time; a baked dataset makes the image huge and unauditable,
   and a baked secret cannot be revoked.
4. **Record the image digest with the output.** The digest, plus the recipe's commit,
   is what lets a reader obtain the same environment; a tag alone does not.
5. **Run the tests inside the image.** A container that has not executed the test
   suite is an untested environment claim:
   see [22-07-02 Continuous Integration for Research Software](../07-software-testing-quality/02-continuous-integration.md).
6. **Keep the recipe in version control next to the code.** The recipe is part of the
   method; a hand-built image has no provenance.
7. **Prefer the smallest artefact that removes the failure.** If the failure is
   dependency drift, a lock file is enough; a container is warranted when the failure
   involves system libraries, the interpreter build, or a machine you do not control.

## 8. Worked example: a 1.78 GB image for a 12 MB analysis

A group publishes an image of the demonstration's recipe alongside a paper.

1. **Is the size a problem?** 1.78 GB per pull, for a 12 MB analysis. If the readers
   are a handful of reviewers, the cost is minutes; if the image is the distribution
   mechanism for a widely used tool, the cost is real and the fix is to move the
   900 MB reference-data layer out of the image and mount it by identifier.
2. **Is the build time a problem?** 13.5 minutes cold, 0.5 minutes for a code change
   with a correct layer order. The order is the difference between an affordable
   iteration loop and an afternoon per edit.
3. **Is the image reproducible?** Only if the base is pinned by digest and the
   packages are pinned; unpinned, the model's two builds agree bitwise with
   probability 0.606.
4. **Is the result reproducible?** The image pins the software, not the arithmetic:
   CPU, thread count and any run-time fetch remain. State the tolerance and the
   data identifier in the paper's artefact, and run the analysis inside the image in
   CI.

## Assumptions and regime of validity

1. **Layer sizes and times are chosen.** Real images vary by orders of magnitude; the
   structure of the argument (code is a small part, order determines rebuild cost)
   is what generalises.
2. **Layer caching is content-addressed and exact.** Build systems differ in whether
   they hash the instruction text or the produced files, and in how they treat
   timestamps; the invalidation cascade is common to all of them.
3. **Drift probabilities are modelled, not measured.** The 0.606 figure is a model
   output for the stated per-family drift rates; the point is the direction and the
   mechanism, not the value.
4. **Bitwise agreement is a strong criterion.** Two builds can differ in
   uninteresting ways (timestamps, file ordering) and still be functionally
   identical; bitwise equality is a sufficient condition for agreement, not a
   necessary one.
5. **The floating-point illustration is a computation, not a measurement of
   operators.** Summing in float32 versus float64 demonstrates the scale of
   arithmetic differences that survive a pinned image.

## The honest summary

A container is the strongest available pinning of the software environment: an
ordered stack of content-addressed layers built from a recipe, distributable as one
artefact. In the demonstration's modelled recipe the image is 1.78 GB and builds in
13.5 minutes, while the analysis code is 0.7 % of the size and 3.7 % of the build —
and layer order decides whether a code edit costs 0.5 minutes or 13. Keeping
`:latest` and floating dependencies drops the probability that two builds agree
bitwise to 0.606 of an image whose floating payload is 93 %; pinning digests and
hashes raises it to 1.000. What a container does not freeze is the host's arithmetic
(a relative difference of $1.04 \times 10^{-7}$ survives between float32 and float64
summation), the thread count, the clock, and everything it calls over the network.
The honest conclusion is therefore narrow and useful: a container removes the
environment as a variable, which is one of the six failure categories in
[22-02-01](01-reproducibility-crisis.md), and it does so at the cost of a large
artefact whose licences must be audited.

## Python demonstration

[`code/containers_reproducibility_demo.py`](./code/containers_reproducibility_demo.py)
prints, under four numbered banners:

1. the five-layer recipe: 1.78 GB total, 13.5 minutes cold, the code's 0.7 % share;
2. the rebuild cascade: 1, 2, 3 and 4 layers and 0.5, 2.5, 9.0, 13.0 minutes;
3. bitwise agreement: 0.606 unpinned against 1.000 pinned, with 1650 MB of floating
   payload;
4. what is not frozen, including the float32/float64 summation difference
   ($-845.3800$ against $-845.3801$, a relative $1.04 \times 10^{-7}$).

```bash
cd 22-data-engineering-reproducibility/02-reproducible-workflows/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python containers_reproducibility_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/06-containers-reproducibility-exercises.md`](./exercises/06-containers-reproducibility-exercises.md)
and
[`exercises/06-containers-reproducibility-solutions.md`](./exercises/06-containers-reproducibility-solutions.md).

## Mastery checkpoint

Without notes: a recipe has a 150 MB base, 200 MB of system packages, 500 MB of
Python packages, 60 MB of code and a 2 GB dataset copied in.

1. Compute the image size and state which single change most reduces it.
2. State the rebuild cascade when the code changes, and where the code step must sit
   in the recipe.
3. Compute the probability that two builds agree bitwise if the base is pinned but
   the package layers drift with probabilities 0.10 and 0.20.
4. State three things that remain unpinned even after digest pinning.

## Common pitfalls

1. **Using a mutable tag.** `:latest` or an unpinned tag names whatever the registry
   currently points at; only a digest is an identifier.
2. **Baking data into the image.** It inflates the image (900 MB of the demonstration's
   1.78 GB), makes updates a rebuild, and cannot be versioned independently.
3. **Ordering the recipe by convenience.** Installing code before packages reattaches
   the package build (6.5 minutes) to every code change (0.5 minutes).
4. **Treating a container as a correctness guarantee.** It freezes the software, not
   the arithmetic, the scheduler or the services the code calls.
5. **Distributing an image without a licence audit.** Distribution includes every
   layer; only 18 % of the demonstrated licence pairs are permissive-to-permissive.
6. **Building by hand and pushing.** The recipe is the method; an unversioned image
   has no provenance and cannot be rebuilt.

## Where this is used

- **Paper artefacts and reviewer access** — a digest-pinned image is the environment a
  referee can run: see [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Cluster and cloud execution** — the same image runs on a laptop, a cluster node
  and a cloud instance: see
  [22-06-02 Cloud Computing for Geophysical Computation](../06-high-performance-and-cloud/02-cloud-computing-research.md).
- **Licence compliance at distribution** — the image is the unit that is distributed
  and therefore the unit that must be audited:
  see [22-01-05](../01-research-software-engineering/05-licensing-and-citation.md).
- **CI for research software** — testing the image is testing the environment claim:
  see [22-07-02 Continuous Integration for Research Software](../07-software-testing-quality/02-continuous-integration.md).

## Related lessons

- [22-02-02 Pinning Environments and Managing Dependencies](./02-environment-pinning.md) —
  the levels of pinning a container extends.
- [22-02-05 Data Versioning and Provenance Tracking](./05-data-versioning.md) —
  what to mount rather than bake in.
- [22-06-01 Running Jobs on HPC Clusters and Schedulers](../06-high-performance-and-cloud/01-cluster-jobs.md) —
  where the image meets the scheduler.
- [22-07-04 Benchmarking, Performance Tracking and Documentation Tests](../07-software-testing-quality/04-benchmarking-and-docs.md) —
  how to justify a numerical tolerance with a measurement.

## Self-assessment checklist

- [ ] I can explain layers and the content-addressed cache.
- [ ] I can compute an image's size and predict its rebuild cascade.
- [ ] I can state why layer order is a performance decision.
- [ ] I can compute the probability that two unpinned builds agree.
- [ ] I can list what a container does not freeze.
- [ ] I can choose between a lock file and a container for a stated failure.
