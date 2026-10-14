# Solutions — 22-02-06 Containers for Computational Reproducibility

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [06 Containers for Computational Reproducibility](../06-containers-reproducibility.md).

---

## ★1 — Why layers, and why the cascade

An image is built as a sequence of steps, and each step's result is stored as a
content-addressed **layer**, so a step whose inputs are unchanged can be reused from
cache instead of re-executed. Because each step's inputs are *the previous layer plus
the step's own files*, a change to one step changes the input to every later step,
so those layers are invalidated and rebuilt. That cascade is what makes recipe order
a performance decision rather than a stylistic one.

## ★2 — Size and build shares

(a) Total size $= 120 + 340 + 410 + 900 + 12 = 1782$ MB $= 1.78$ GB. Cold build
$= 0.5 + 4.0 + 6.5 + 2.0 + 0.5 = 13.5$ min. Both match the printed values.

(b) Code share of size: $12/1782 = 0.7\ \%$. Code share of build: $0.5/13.5 =
3.7\ \%$.

(c) The container is 99.3 % environment by size and 96.3 % environment by build time.
The implication is that a group's container work is about *choosing and pinning* the
environment (base, system packages, language packages, data), not about the code it
writes; and that the largest wins come from decisions such as not baking a 900 MB
dataset into the image and from ordering the layers by change frequency.

## ★3 — What a tag pins and what a digest pins

(a) **Patch version — no** for `python:3.11`, **yes** for the digest form: a moving
minor tag is re-pointed as patches are released, while the digest names exact
content.

(b) **System libraries — no** for the tag, **yes** for the digest: the tag's layers
can be rebuilt, the digest's cannot.

(c) **An unpinned `pip install` — neither** pins it, because the resolver runs at
build time and chooses according to what the index serves then. Even the digest-pinned
base leaves this floating unless versions and hashes are explicit.

## ★★4 — Rebuild cascade

(a) The cascade is cumulative from the changed layer to the end of the recipe:

- code (last): 1 layer, $0.5$ min;
- data (second-to-last): 2 layers, $2.0 + 0.5 = 2.5$ min;
- python (middle): 3 layers, $6.5 + 2.0 + 0.5 = 9.0$ min;
- apt (second): 4 layers, $4.0 + 6.5 + 2.0 + 0.5 = 13.0$ min.

All four match the printed values.

(b) The order is base → apt → python → data → code: the fastest-changing item (code)
is last and the slowest-changing (base) is first.

(c) With code second and apt fourth, a code change invalidates code, python, data and
apt — 4 layers, 13.5 minutes. The penalty over the correct order is
$13.5 - 0.5 = 13.0$ minutes **per code edit**, which for a day's work of twenty edits
is over four hours of avoidable build time.

## ★★5 — Bitwise agreement

(a) Independence of the three drifting families:

$$P(\text{identical}) = (1 - 0.15)(1 - 0.25)(1 - 0.05) = 0.85 \times 0.75 \times
0.95 = 0.6056 \approx 0.606,$$

matching the printed value.

(b) With the apt layer pinned:
$P = 1 \times (1-0.25) \times (1-0.05) = 0.75 \times 0.95 = 0.7125$.

(c) Floating payload:
$340 + 410 + 900 = 1650$ MB, i.e. $1650/1782 = 92.6\ \% \approx 93\ \%$ of the image.

(d) The figure says that two unpinned builds agree **in every byte** with probability
0.606 — it is a statement about build artefacts. It does **not** say that a
disagreeing pair produced different results: a re-serialised file or a changed
timestamp breaks bitwise equality and changes nothing numerically. Conversely,
bitwise-identical builds on different hardware can still give different results, so
agreement is neither necessary nor sufficient for numerical reproducibility.

## ★★6 — Moving the dataset out of the image

(a) Two reasons: **size and distribution** — 900 MB of the 1.78 GB image is carried
by every pull, and a data correction means republishing the image rather than
publishing a new data version; and **independent versioning** — data have their own
lifecycle, retention policy and licence, and the provenance record should name the
data identifier rather than an image digest that silently embeds one snapshot.

(b) The provenance record must now name the data by its **own identifier** (hash or
DOI) at run time, alongside the image digest, and the pipeline must mount it by that
identifier rather than by a path. The image's record then covers software only, and
the data record is separately checkable — which is exactly the split
[22-02-05](../05-data-versioning.md) §5 prescribes.

(c) Baking data in is the better choice when the dataset is **small, immutable and
part of the software's contract** — for example, a 2 MB table of physical constants
or a set of regression fixtures that the tests need. There, shipping the data with
the image removes an external dependency and makes the test self-contained; the rule
is about size and change frequency, not about principle.

## ★★★7 — A five-year, three-platform container strategy

**Base image policy.** One minimal, long-term-support base per supported architecture,
recorded by digest. Avoid full desktop distributions; prefer a slim base with no
interpreter pre-installed unless the interpreter's build must be controlled. Keep a
second image (a "cluster" variant) only if the scheduler requires extra clients.

**Pinning.** Base by digest; system packages by version with checksums; languages
packages from a lock file with hashes; every downloaded file by hash. Record the
digest of each produced image next to the recipe's commit.

**Data mounting.** Data are never baked in: they are mounted read-only by version
identifier (hash or DOI) at run time. Small constants and test fixtures are the
documented exception.

**CI checks.** Build the image from the recipe in CI; run the test suite *inside* it
on each supported platform; verify that the analysis reproduces its reference values
within the tolerance measured per platform; and check that a rebuild from the recipe
produces a functional image (bitwise identity is too strict to require — see ★★5(d)).

**Archival.** The recipe and the digest live in the repository and in the paper's
artefact, and the image itself is pushed to an archive or registry with a retention
commitment; a checksum of the image is recorded so a future copy can be verified.
Keeping only the recipe is not enough — recipes stop building when registries move.

**The failure the strategy does not remove.** Differences in the host's arithmetic
and scheduling: the same image on a different CPU or with a different thread count
can change the last digits of a parallel reduction (the demonstration's relative
$1.04 \times 10^{-7}$ is the scale). The strategy therefore pins the software and
leaves a numerical tolerance as a required part of the report.

## ★★★8 — A tolerance policy for in-image regression tests

**Step 1 — measure run-to-run variation on one machine.** Run the reference
computation $R \ge 20$ times in the same image, on the same machine, with the same
thread count and under the same scheduling conditions, recording the relative
difference of each run from the first. This gives $\sigma_{\text{run}}$, the
platform's own reproducibility noise. Report it: a pipeline whose noise is
$10^{-12}$ and one whose noise is $10^{-6}$ need different policies.

**Step 2 — measure across platforms.** Repeat on each supported CPU generation and
with 1, 2 and 4 threads. Take the largest observed relative difference as
$\sigma_{\text{plat}}$. The measured float32/float64 difference of
$1.04 \times 10^{-7}$ is an order-of-magnitude guide for reductions whose dtype
changes, not a value to adopt.

**Step 3 — choose the tolerance.** Set the test tolerance at roughly
$k \times \sigma_{\text{plat}}$ with $k = 5$–$10$, and record the reason in the test
docstring. A tolerance smaller than the platform noise produces a suite that fails
randomly; a tolerance a hundred times larger than the noise hides real regressions.

**Step 4 — separate regression from platform difference.** Compare like with like:
run the reference and the candidate on **the same platform, image and thread count**,
and treat a difference larger than the tolerance as a regression. Maintain the
reference values per platform, or store one canonical platform and re-derive the
others from the recorded $\sigma_{\text{plat}}$.

**What the tolerance cannot detect.** A change that keeps the headline number within
tolerance while changing the model in a way that matters elsewhere — for example a
shift in a parameter that is compensated in the reported value, or a bug in a code
path the reference values do not exercise. Tolerances protect the *checked* outputs;
coverage, not the tolerance, decides what is checked.

## ★★★9 — When a lock file is not enough, and when a container is not the tool

**Case 1 — the interpreter's build or the system libraries matter.** A lock file
pins the *packages it knows about* and says nothing about the C library, the BLAS
implementation the wheels were built against, or the compiler used for a source
build (components 4 of the environment list in
[22-02-02](../02-environment-pinning.md) §2). If a result
depends on the BLAS threading or a source-built extension, the lock file cannot fix
it and a container (or a pinned system package set) can.

**Case 2 — the machine is not under your control.** A container is the only practical
way to obtain the same environment on a laptop, a cluster node and a cloud instance
without installing the toolchain on each. Here the argument is about *portability*
rather than drift: without a container there is no way to give a reviewer the
environment without giving them a build recipe for their own machine.

**Case 3 — a container is the wrong tool.** For a workflow whose heavy dependency is a
specialised hardware or licensed stack (a proprietary compiler, a GPU driver tied to
a node image, a commercial inversion package with node-locked licensing), containerising
adds a layer of indirection that cannot be pinned usefully, and the honest artefact is
a documented environment plus a checksum of the licensed software — the container would
freeze the wrong things and imply a portability it does not have.
