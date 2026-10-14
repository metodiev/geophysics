# Solutions — 05-06-06 Documenting Processing: Reproducibility in Practice

> **Read this after attempting the exercises, not before.**

---

## ★1 — The four levels

**Bit-identical** (hashes agree) → **numerically equivalent** (agree within a stated
tolerance) → **statistically equivalent** (differ by less than the data noise) →
**conceptually equivalent** (support the same conclusion).

The weakest *useful* form is **statistically equivalent**: it is the level at which a
difference cannot be detected in the data, and therefore cannot affect an
interpretation. "Conceptually equivalent" is weaker still but is not useful as a
claim, because it is unfalsifiable without specifying the conclusion and its
uncertainty.

---

## ★2 — The five components

1. the input, with a content hash;
2. the ordered steps with parameters;
3. the environment (library and interpreter versions, and anything affecting
   arithmetic);
4. the output hash;
5. **the verification** — what was compared with what, at what tolerance.

Component 5 turns the record into a claim: items 1–4 describe what was done,
item 5 states what was checked.

---

## ★3 — Hashes, units and representation

A hash establishes *identity* and nothing else: the same physical field stored in
mGal and in m s⁻² hashes differently, and the same numbers stored as text at
different precision also hash differently. So a hash without units does not identify
a physical quantity, and a hash without a stated representation does not identify a
byte sequence. Units establish meaning; the representation makes the hash
well-defined.

---

## ★4 — Ordering rules

1. **Edit before anything that averages** — a spike contaminates its neighbours
   through any averaging or filtering operation.
2. **Tie/level before filtering** — a trend is long-wavelength, and a filter passing
   long wavelengths passes the trend.
3. **Statics before stacking** — alignment is a precondition of averaging.
4. **Filter before differentiating** — the derivative's gain grows with wavenumber
   and the noise is at the highest wavenumbers.
5. **Grid last** — gridding interpolates, so anything uncorrected is interpolated too.

---

## ★5 — The tolerance rule

The tolerance must be **at least an order of magnitude below the data's noise** (so
that a difference passing the test cannot be detected in the data) and **at least an
order of magnitude above the machine precision of the arithmetic** (so that the test
does not fail for arithmetic reasons). It must be quoted in the units of the data.

---

## ★★6 — Choosing a tolerance

**(a)** 0.05 mGal is **6.25 times the noise** (0.008 mGal), i.e. a result differing by
0.05 mGal would still pass — yet such a difference is 6× the noise and would be
plainly visible in the data and would shift the anomaly peak by 14 % of its value.
The tolerance is **too loose**.

**(b)** Within the two bounds: the tolerance must be $< 0.0008$ mGal (a tenth of the
noise) and $> \sim10^{-14}$ mGal (a hundred times binary64 resolution at this
magnitude). A defensible value is **$10^{-6}$ mGal** — comfortably inside both.

**(c)** A $10^{-6}$ mGal tolerance with a *bit-identical* result additionally
establishes the bit-identical level; if the hashes differ but the tolerance passes,
the claim is numerically equivalent (and, since the tolerance is below the noise,
statistically equivalent as well). The lesson's point is that the claim must name
which.

---

## ★★7 — An incomplete record

**(a)** The **order** is implied by the list but not stated as a binding sequence, and
the **outcomes** of data-dependent steps are absent. The lesson's measured consequence
of the ordering ambiguity is an RMS difference of 0.007976, i.e. 1.027 % of the peak —
a difference larger than many interpretations would tolerate, and one that cannot be
attributed to anything if the order is not recorded.

**(b)** An executable record lists the steps as an ordered array, each with an
operation name and a parameters object, and is consumed by a function that loops over
that array — so the record *is* the sequence:

```json
{"steps": [
  {"op": "despike", "params": {"window": 5, "n_sigma": 4.0}},
  {"op": "filter",  "params": {"cutoff_wavelength": 400.0}},
  {"op": "level",   "params": {"order": 1}},
  {"op": "grid",    "params": {"interpolator": "cubic", "spacing_m": 25.0}}
]}
```

**(c)** Two outcomes to record: the **number of samples changed** by the despike step
(the lesson's record stores `samples_changed: 3`; a value of 77 would immediately
reveal a broken threshold), and the **coefficients fitted** by the levelling step
(which show what long-wavelength content was removed).

---

## ★★8 — Stochastic steps

**(a)** For the **k-means** step: the random seed, the initialisation method, the
number of clusters, the convergence tolerance, and the library version — the last
because implementations change their default initialisation between versions. For the
**bootstrap**: the random number generator *and its algorithm* (a generator's stream
is not portable between implementations), the number of resamples, the seed, and the
statistic being computed.

**(b)** A different result is not necessarily a bug because a stochastic algorithm
legitimately explores; only the *distribution* of outcomes is reproducible, not the
individual draw. The honest verification is therefore statistical: report the mean and
spread over $M$ seeds and verify that a re-run's outcome falls within that
distribution.

**(c)** Meaningful verification: (i) the input hash and the environment hash match;
(ii) the *reported summary* of the stochastic step (e.g. the cluster centres, rounded
to a stated precision) agrees within a stated tolerance; (iii) with the seed fixed,
the outcome is bit-identical. Claiming reproducibility for a stochastic step without
fixing the seed is a claim about the algorithm, not about the numbers.

---

## ★★9 — Different levelling choices

**(a)** Not a **bit-identical** failure — the two pipelines are different procedures,
so different outputs are expected. It is not even a **reproducibility** failure in the
strict sense: each analyst's result is reproducible from their own record, if they have
one. The failure is a **documentation** failure: without the record, the 0.04 mGal
difference cannot be attributed to a cause, and a client comparing two maps cannot
tell whether the difference is processing or geology.

**(b)** Each must record: the levelling *type* and its *parameters* (polynomial order,
tie-line set, whether the datum was fixed), the datum and replacement velocity, the
software versions, and the outcomes (the fitted coefficients and the number of
misfitting points). With those, the difference is a computable consequence of two
stated models.

**(c)** Resolvable by re-running: anything with a recorded parameter — analyst A can be
re-run with B's parameters, and the 0.04 mGal should then vanish. **Not** resolvable by
re-running: a step performed by hand, or a parameter that was chosen but not recorded.
That is the residual risk, and it is exactly the first item of the lesson's Section 10
ranking.

---

## ★★★10 — A five-step pipeline with a hidden-parameter test

A satisfactory answer produces a record like:

```json
{"input_sha256": "...", "software": {"numpy": "...", "python": "..."},
 "steps": [
   {"op": "despike",    "params": {"window": 5, "n_sigma": 4.0}},
   {"op": "level",      "params": {"order": 1}},
   {"op": "lowpass",    "params": {"cutoff_wavelength": 400.0}},
   {"op": "continuation","params": {"dz_m": 200.0}},
   {"op": "grid",       "params": {"interpolator": "cubic", "spacing_m": 25.0}}],
 "output_sha256": "..."}
```

Non-commuting pair: **despike and level** (measured RMS difference 0.007976, 1.027 %
of the peak) — despiking changes which samples enter the trend fit, and levelling
changes the data the spike threshold is measured on. A second non-commuting pair:
**lowpass and continuation**, both diagonal in the Fourier domain and therefore
commuting as operators, but *not* interchangeable with gridding, which is not a filter
at all.

Stochastic step: **gridding by a randomised method** (e.g. a stochastic
interpolation, or a k-means-based classification used for a regional/residual split),
which must record its seed.

**Detecting a missing parameter.** Omit `n_sigma` from the record and re-execute the
record with a default: the output hash changes, which is the *only* signal available,
because the missing parameter does not appear anywhere in the input or the output. This
is the strongest argument for hashing the output: the hash turns "something is
different" into a binary, unambiguous detection. The lesson's Section 9 items that
apply: (2) a default parameter, (4) a missing environment specification, (5) an
unrecorded seed, and (7) a file-order dependence if the steps read a directory.

---

## ★★★11 — An automatic classification harness

A satisfactory implementation runs the pipeline, then compares the new output with the
reference and prints one of four verdicts:

| test | condition | verdict |
|---|---|---|
| 1 | hashes equal | bit-identical |
| 2 | $\max\lvert\Delta\rvert \le \tau_{\text{num}}$ | numerically equivalent (state $\tau$) |
| 3 | RMS difference $\le \sigma_{\text{noise}}$ | statistically equivalent |
| 4 | a derived quantity (e.g. the anomaly peak) agrees within its uncertainty | conceptually equivalent |

Demonstrating on a perturbed parameter produces the expected sequence: as the
perturbation grows, the verdict degrades from bit-identical through numerically
equivalent (perturbation $\sim10^{-15}$), through statistically equivalent
(perturbation $\sim10^{-3}$ of the noise), to conceptually equivalent and finally to
"not equivalent at all" once the derived quantity moves beyond its uncertainty.

**The useful report** states the largest perturbation at which each verdict still
holds, because that is the *sensitivity* of the conclusion to the parameter — and it
is the number a reviewer actually needs.

---

## ★★★12 — Testing thread-count dependence

A satisfactory experiment:

1. Choose a reduction whose result depends on summation order: a large
   `np.dot`/`np.sum` over a few hundred thousand elements, or a stack of many traces.
2. Run it with the environment variables that control the BLAS thread count (for
   example `OMP_NUM_THREADS`) set to 1, 2, 4 and 8, hashing each output.
3. Report the hashes and the maximum pairwise differences.

Three honest outcomes, all of which must be reported as they are found:

- **all hashes equal:** this establishes that *on this machine, with this library
  build and these thread counts*, the reduction order did not change. It does **not**
  establish portability: a different BLAS, a different compiler or a different
  architecture may still differ.
- **hashes differ, differences of order machine epsilon:** this confirms the
  lesson's claim, and the correct inference is that bit-identical reproduction must be
  scoped to an environment, while verification should use a tolerance.
- **hashes differ by more than machine epsilon:** this indicates an algorithm whose
  *decisions* depend on floating-point comparisons (a threshold test, a branch, a
  convergence criterion), where a last-bit difference flips a discrete choice and
  amplifies into a large output difference. This is the most consequential outcome,
  and it identifies a pipeline that needs either a deterministic reduction or an
  explicitly recorded tolerance.

The lesson's rule follows from all three: **claim the level you verified, name the
environment, and state the tolerance** — because the experiment's outcome is a
property of the code and the machine, not of the science.
