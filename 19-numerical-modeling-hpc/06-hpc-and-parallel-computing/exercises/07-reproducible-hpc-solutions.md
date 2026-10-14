# Solutions — 19-06-07 Reproducibility and Provenance in HPC Workflows

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs.

Lesson: [07 Reproducibility and Provenance in HPC Workflows](../07-reproducible-hpc.md).

---

## ★1 — The spread

Absolute spread: $|-604.9947385276926 - (-604.9947385276923)| = 3\times10^{-13}$.

Relative:
$3\times10^{-13}/604.9947385276926 = 4.96\times10^{-16}$, i.e. about $2.2$
unit roundoffs of a double ($\epsilon = 2.22\times10^{-16}$) — exactly the order a
changed summation order produces on a few hundred thousand terms.

---

## ★2 — What `fsum` guarantees and costs

**Guarantee:** the returned value is the correctly rounded sum of the exact
inputs. Because the exact sum does not depend on order, the result cannot depend on
order either — measured as one digest across six decompositions.

**Cost:** it uses an extended-precision accumulator and, in CPython, works
through a Python-level argument list rather than a vectorised loop, so it is far
slower than `np.sum` on large arrays. It belongs on reductions whose bits matter
and not on inner loops.

---

## ★3 — The two claims

- **"The result is reproducible"** says nothing testable: reproducible to how
  many digits, under what change, on what platform?
- **"Bitwise reproducible across pool sizes at a fixed decomposition"** names the
  perturbation (pool size), the thing held fixed (the decomposition) and the
  observable (bit equality). It can be tested and it can fail.

The measurement supports the second claim (one digest across pool sizes $1\ldots8$)
and refutes its over-generalisation: chunk counts produced four distinct digests,
so dropping the "fixed decomposition" clause makes the claim false.

---

## ★4 — Verifying the ulp count

$$\text{ulp} = \frac{7.162\times10^{-12}}{2.22\times10^{-16} \times |{-556.4892}|}
= \frac{7.162\times10^{-12}}{1.236\times10^{-13}} = 58 .$$

The printed value is $63.0$ ulp, which differs because the demonstration computes
the ulp against `np.spacing(|plain|)` — the actual spacing at that magnitude, which
is a power of two and not $\epsilon\times|value|$. Using the exact spacing
(here $\approx 1.137\times10^{-13}$) gives $63.0$ ✔. The lesson: an ulp count
must name its reference spacing, and `np.spacing` is the reference that matches
IEEE-754 spacing exactly.

---

## ★5 — Six-digit checkpoints

The largest absolute error is $4.999\times10^{-7}$, which for values of order
$1$ is a relative error of about $5\times10^{-7}$ — nine orders of magnitude
larger than $\epsilon$ and larger than any tolerances a nonlinear solver or a
chaotic trajectory would tolerate. A restart from such a file does **not**
reproduce the trajectory; it starts a neighbouring trajectory that may diverge
slowly (linear cases) or rapidly (nonlinear, chaotic cases).

Therefore: a checkpoint is state and must be lossless — `.npy` or seventeen
digits. Six digits is a plot.

---

## ★6 — Manifests and canonical form

Two manifests differing in `dt_s` will, with cryptographic hashing, have
different digests with overwhelming probability — the question is what "the
manifest" means. Without a canonical form (sorted keys, fixed separators, fixed
number formatting), the *same* run can produce two different manifests depending
on dictionary insertion order or on whether a value was written as `0.004` or
`4e-3`, and then two digests for one run. Canonicalisation is what makes
`digest(A) == digest(B)` mean "same run" rather than "same JSON string",
and that is a prerequisite for the hash being an identity at all.

---

## ★7 — A claim and three falsification attempts

**Claim:** "On this machine, with numpy 2.5.4 and CPython 3.14, the solver
reproduces bitwise for a fixed $256\times256$ grid, a fixed time step and a fixed
8-chunk decomposition, across thread-pool sizes $1\ldots8$; the manifest digest is
`dc1e910e…`."

**Falsification attempts:**

| attempt | observable |
|---|---|
| change the pool size from $1$ to $8$ at a fixed decomposition | digest of the result; measured invariant, so the claim stands or falls here |
| change the chunk count from $8$ to a data-dependent auto-tuning value | digest; if the code auto-tunes, the claim is already false, and this detects it |
| run with `OMP_NUM_THREADS` unset — i.e. with a multi-threaded BLAS | digest plus the recorded environment; a threaded reduction changes order and can change the last bits |

A fourth attack is worth naming though it is outside the claim: change numpy's
version, which changes its pairwise-summation threshold, and the bits move with no
code change — which is why the version is in the manifest.

---

## ★8 — Provenance for two devices and three pool sizes

Fields required, and the measurement that justifies each:

| field | why it exists |
|---|---|
| `device` per kernel launch, and the backend | [04 §5](../04-gpu-computing.md): a portability layer does not guarantee identical results or speed |
| `pool_size` and `decomposition` per run | [02 §6](../02-shared-memory-parallelism.md): pool size did not change the digest, chunk count did |
| `reduction_order` (tree shape, merge order) | [03 §5](../03-mpi-distributed.md): the tree and the gather differ by 1 ulp |
| `float64_eps`, `byte_order` | [07 §4](../07-reproducible-hpc.md): the last-bit claims depend on them |
| library versions (numpy, BLAS, compiler) | pairwise thresholds and reassociation change bits without code changes |
| the seed and the sequence of random draws | a synthetic input is not reproducible without them |
| hashes of the inputs (`sha256`) | the manifest identifies the *configuration*; the input hashes identify the data |
| the git commit and the dirty flag | a manifest describing code that no longer exists is provenance theatre |

The shortest defensible record keeps all of these and labels which were held fixed
in the experiment and which varied — because a provenance record whose purpose is
to answer "is this the same run?" must distinguish the knobs from the identity.
