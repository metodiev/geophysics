# Solutions — 03-13-08 Reproducible Environments: pip-tools, conda, Containers

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; derived values are shown with the arithmetic
> that produced them.

---

## ★1 — Printing an environment

**(a)** *"Analyses used CPython 3.14.8 in a virtual environment (`sys.prefix`
`…/geophysics/.venv`) on arm64 macOS with 10 logical CPUs; the exact package set
is pinned by the sha256 fingerprint `e7ef1812…` over 155 distributions."* The
item a typical methods section omits is the **prefix** — whether the interpreter
was inside an environment at all — and, usually, the **architecture**.

**(b)** Because two interpreters of the same version with different
`site-packages` are different environments, and the failure they produce is the
worst kind: the code runs locally and raises `ModuleNotFoundError` on somebody
else's machine, after a successful-looking install. The version tells the reader
which interpreter to install; the prefix tells them whether the packages they
installed are the ones that were used.

**(c)** It is a function of the sorted `name==version` pairs of every distribution
visible to the interpreter — so it changes whenever any package is added,
removed or upgraded. It is **not** a function of the platform, the BLAS build,
the wheel provenance, or the interpreter: two machines with the same 155 pins can
legitimately produce different floating-point results, and a fingerprint that does
not say `arm64` is incomplete.

---

## ★2 — The BLAS underneath

**(a)** A dot product is a reduction, floating-point addition is not associative,
and the order in which a vectorised kernel accumulates its partial sums is decided
by the kernel — so a different BLAS, or a different version of the same BLAS,
returns a different last bit for the same mathematical expression.

**(b)** A lock file pins the **NumPy version** (and the dependency set, and with
`--require-hashes` the distribution bytes). It does not pin the **BLAS**, the
**SIMD instructions used**, or the interpreter, which is why the lesson lists
those separately in Section 6.1.

**(c)** It is not a bug. A difference in the fourteenth significant figure, arising
from a different reduction order, is indistinguishable from the arithmetic's own
round-off and lies far below any scientific tolerance. The correct response is to
**state a tolerance derived from the effect** — for a length-$n$ reduction,
$\lVert \Delta \rVert / \lVert s \rVert = \mathcal{O}(n u)$, which for $n =
10^6$ gives $\approx 1.1\times10^{-10}$ — and to assert against that, rather than
requiring bit-for-bit agreement that no cross-platform claim can deliver.

---

## ★3 — What a lock file pins

| item | pinned by lock + `--require-hashes`? |
|---|---|
| transitive dependency set | **yes** — that is the point of a lock file |
| exact distribution bytes | **yes** — that is what `--require-hashes` adds |
| interpreter patch version | no — pin it in `requires-python` *and* in the CI matrix |
| platform | no — record it in the fingerprint and the statement |
| thread count | no — set it in the environment and record it |

The pattern is worth internalising: a lock file pins **what pip installs**, and
nothing about the machine it installs onto.

---

## ★4 — Reduction order

**(a)** $3.274\times10^{-11}/998.571 = 3.28\times10^{-14}$.

**(b)** With $\mathrm{ulp}(1000) \approx 1.14\times10^{-13}$ — *measured* as
`math.ulp(1000.0) = 1.1368683772161603e-13` — the three differences are
$2.274\times10^{-13}/1.137\times10^{-13} = 2.0$ ulp, $4.0$ ulp, and
$288$ ulp respectively. So the pairwise-versus-blocked differences are a couple of
ulp, while the sorted-sum difference is a few hundred ulp, because sorting
destroys the near-cancellation that pairwise summation exploits on unordered data.

**(c)** A tolerance of $10^{-12}$ relative passes all four values and the
independent bound from the model: the accumulated error for a length-$n$ reduction
is $\mathcal{O}(n u)$, and $10^6 \times 1.11\times10^{-16} = 1.11\times10^{-10}$
— so $10^{-12}$ is *tighter* than the model bound and would fail on a longer
array. The defensible choice is

$$\tau_{rel} = 10\,\times\,n\,u = 10 \times 10^6 \times 1.11\times10^{-16}
= 1.1\times10^{-9},$$

with the factor 10 as margin. The measurement says $10^{-12}$ would happen to work
here; the model says it would fail if the array grew, which is the difference
between a tolerance that was measured once and one that was derived.

---

## ★5 — The thread-count experiment

**(a)** It establishes that **on this machine, with Accelerate, at 600×600, for
matmul and solve, the thread count 1/2/4/8 produced bit-identical results, and
that for a fixed thread count the digests reproduce exactly across independent
processes**. It does not establish that thread count can never change a result:
another BLAS is free to partition a reduction by thread count, and a last-bit
difference can flip a comparison and hence a branch.

**(b)** The most likely reversal is **a larger problem size and a different
BLAS**: OpenBLAS and MKL both choose blocking and threading strategies from the
matrix dimensions, and at sizes where a single thread's working set exceeds cache,
the parallel partition becomes a genuine change of summation order. Running the
same probe at 2000×2000 and 5000×5000, and on a machine with OpenBLAS, is the
experiment that would test it.

**(c)** Phrasing that over-claims: *"results are independent of thread count."*
Phrasing that is a result: *"For a fixed thread count the computed arrays were
bit-identical across repeated runs; changing the thread count between 1 and 8 did
not change the results for the 600×600 matmul and solve tested here (Accelerate,
arm64, NumPy 2.5.4). This does not generalise to other BLAS implementations or
problem sizes."*

---

## ★6 — Auditing a declaration

**(a)** An **absence** means the environment does not contain a declared package:
the fix is to install it, and nothing already computed is affected. A **version
mismatch** means the environment contains a version that contradicts the
declaration: an installed version that does not satisfy the declaration can
silently change a numerical result. Merging them into one count hides the fact
that nothing *present* is wrong, and that is the distinction that decides whether
you must re-run anything.

**(b)** They differ because they check different declarations:
`requirements.txt` is the pip list (33 requirements, including packages the pip
environment was never expected to have such as `pyrocko`, `simpeg`, `torch` and
`seisbench`), while `environment.yml` is the conda specification (30 conda
dependencies), and the two lists overlap but are not identical. Both audits are
meaningful; the right one to run is **the one for the environment you are actually
in** — here, both, because the module demonstrates both mechanisms. Running the
`environment.yml` audit inside a pip venv is the common mistake, and it produces
absences that are not defects.

**(c)** The audit cannot tell you whether the environment *works*: it checks names
and version specifiers only. It says nothing about whether the BLAS is the
expected one, whether a compiled extension actually loads, whether the platform's
SIMD baseline supports the wheels, or whether the code's own tests pass. It is a
precondition check, not a verification — the distinction the testing lesson draws
between "installed" and "verified".

---

## ★7 — A geodynamics reproducibility package

**(a)** **A container**, because the dependencies are not Python-only: a Fortran
compiler, an MPI implementation, PETSc and a specific BLAS are all system-level
libraries with interlocking versions, and a lock file cannot express any of them.
The choice is driven by the same rule as Section 7 of the lesson: use the cheapest
mechanism that pins everything the result depends on, and here that is not the
cheapest one. Inside the container, a Python lock file with `--require-hashes`
still pins the Python layer, and the base image is pinned by digest so that
`FROM python:3.12-slim` cannot move.

**(b)** The three artefacts, each at a DOI-bearing archive:

| artefact | what it is | archive |
|---|---|---|
| the code | the release tag, archived as a snapshot | Zenodo (code DOI) |
| the environment | the container image digest, plus the `Dockerfile` and lock file in the repository | a container registry (digest), and Zenodo for the metadata |
| the data | the input fields/catalogues actually used | Zenodo, PANGAEA, or the discipline archive, depending on the data |

**(c)** Unpinned even then: the **host kernel** (a container shares the host's
kernel), the **hardware** — CPU model, cache sizes, and whether the SIMD
instructions used by the pinned BLAS exist on the reader's machine — and the
**thread count and MPI rank count**, which the container does not fix. In the
paper I would measure and record the thread/rank count and the hardware class
(e.g. "64-core AMD EPYC, OpenBLAS, 8 ranks per node"), because MPI
decomposition changes reduction order and hence the last bits; I would not attempt
to pin the kernel, and I would say so rather than implying bit-for-bit
reproducibility across kernels.

---

## ★8 — The three obligations

**(a)**

| obligation | mechanism from this module | identifier |
|---|---|---|
| code | git commit and tag | the full commit hash, e.g. `494c6712…`, or a release DOI |
| data | a fetch script plus a payload digest, with the data archived | the archive DOI plus the sha256 of the payload |
| environment | a lock file with `--require-hashes`, and an image digest if non-Python libraries are involved | the environment fingerprint and the image digest |

**(b)** **Data provenance has no purely technical solution** — at least, not the
part that matters. You can hash what you fetched and record where it came from,
but nothing in the toolchain can tell you whether the dataset is the *right* one
for the question, whether the processing that produced it was sound, or whether
its stated calibration still holds. That is a judgement about the science, made by
a person who understands the measurement, and it is why the FAIR principles talk
about documentation and provenance rather than about hashes alone.

**(c)** A stranger's sequence, in order:

```bash
git clone <repository> && cd <name> && git checkout v1.2.0
git rev-parse HEAD                      # confirm the hash quoted in the paper
docker pull <image>@sha256:<digest>     # the environment, pinned by digest
docker run --rm -v "$PWD":/w -w /w <image>@sha256:<digest> \
    python -m pip install --require-hashes -r requirements.lock
docker run --rm -v "$PWD":/w -w /w <image>@sha256:<digest> \
    python -m pytest -q
python scripts/fetch_catalogue.py --out data/catalogue.json
sha256sum data/catalogue.json           # compare with the paper's digest
python scripts/make_figure3.py
```

The order matters: commit hash first (cheap, and it fails fast), then the
environment, then the data (the slowest and the only step that leaves the
repository), then the figure. If any digest check fails, the run stops before
producing a number that would look right.

---

## ★9 — "No difference" versus "no difference detected"

**(a)** The measured statement is **"we detected no difference"**: four thread
counts, one problem size, one operation, and identical hashes. The stronger
statement is **"there is no difference"**, which is a universal claim that the
experiment cannot support — non-detection is bounded by the resolution of the
test, and here the resolution is one bit per element (an exact hash), so what the
experiment really shows is that this BLAS did not choose a different partition at
these sizes. The statistical concept is the distinction between failing to reject
and accepting, compounded here by sampling only a single point of a design space
(size, shape, dtype, BLAS, thread count).

**(b)** The stronger experiment is a factorial over the factors the mechanism
depends on: **BLAS** (at least two: Accelerate and OpenBLAS, or MKL),
**operation** (matmul, solve, dot, reduction), **size** (smaller than cache,
larger than cache, much larger), **shape** (square, tall, wide), and **thread
count** (1, 2, 4, 8, plus oversubscribed). With 2 BLAS × 3 operations × 3 sizes ×
3 shapes × 4 thread counts that is 216 configurations, each run at least three
times in a fresh process — 648 runs, of which perhaps 30 would show a difference
if the mechanism is real. The result to report is not "identical" but the
*distribution* of digests per configuration.

**(c)** You would not run it if the downstream use is **a tolerance-based
comparison anyway**: if every consumer of the result asserts against a tolerance
derived from $\mathcal{O}(nu)$, then a last-bit difference is already handled, and
proving its existence buys nothing that the tolerance did not. That is a
defensible decision — it is a decision about *what the result is used for* — and
the honest thing is to say so explicitly: "we did not test thread-count
dependence, because all comparisons downstream are tolerance-based with a band
larger than $nu$".
