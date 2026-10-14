# Solutions — 25-06-04 Capstone: Manuscript-Style Write-Up and Code Release

Reference solutions. Every number is printed by
[`code/capstone_writeup_demo.py`](../code/capstone_writeup_demo.py); the manuscript is
**SYNTHETIC**.

## ★1. What a registry entry carries

Five fields, each with a purpose in the audit:

| field | example | why the audit needs it |
|---|---|---|
| identifier | `H_sd` | so a claim can cite the value rather than repeat it |
| value | 2.001 | the number itself |
| unit | km | catches unit and conversion errors, and stops a km value being quoted in metres |
| precision / derivation | "standard deviation of 40 000 budget draws" | lets a derived claim be recomputed rather than compared with the wrong quantity |
| provenance | `capstone_execution` with a commit | tells the reader *which* run produced it, so a stale registry is detectable |

The 95% interval is **derived**, not stored:

$$\text{id } \texttt{H\_ci95},\quad \text{value } 1.959964 \times \texttt{H\_sd} = 3.9219\
\text{km},\quad \text{unit km},\quad \text{provenance } \texttt{H\_sd} \text{ at commit } \ldots$$

Storing it as a literal would remove the ability to catch the $z = 1.645$ error, which
is precisely the defect the audit found.

## ★2. The four recomputations

| quantity | manuscript | recomputed | verdict |
|---|---|---|---|
| 95% interval, $z = 1.96$ | 3.92 | $1.959964 \times 2.001 = 3.9219$ | correct |
| 95% interval, $z = 1.645$ | 3.29 | $3.9219$ (the derivation is wrong) | **flag** |
| systematic share of the variance | 71% | $1.600^2/2.001^2 \times 100 = 63.94\%$ | **flag** |
| stations accepted | 92% | $45/52 \times 100 = 86.54\%$ | **flag** |

The $z = 1.645$ value is *arithmetically consistent* with a one-sided 90% or two-sided
90% interval, so the number 3.29 is not an arithmetic error — it is the right number for
the wrong interval. That is why recomputation from the registry, and not a calculator
check, is the required audit.

## ★3. Why 71% and 64% both look plausible

$1.600/2.001 = 0.7996$, and $0.7996^2 = 0.6394$. So:

- **64%** is the variance share, $\sigma_\text{sys}^2/\sigma_\text{total}^2$ — the
  correct quantity when contributions are combined in quadrature and the budget is
  reported as variances.
- **71%** is neither: it is not the standard-deviation ratio (which is 80%) and not the
  variance share (64%). It is a number in between, which is exactly what a reader
  cannot check without the derivation.

The lesson is larger than this arithmetic: *both* 80% and 64% are defensible sentences
("the systematic term is 80% of the standard deviation" and "64% of the variance"), and
the manuscript must say which one it means. Contributions combine in quadrature as
standard deviations, so that is the convention to quote and the one to make explicit —
see [25-06-03](./03-capstone-execution-solutions.md), where the same numbers give
$\sqrt{1.198^2 + 1.600^2} = 1.999$ km.

## ★★4. Classification, and what catches each

| flag | class | caught by reading? | caught by abstract/results pairing? | caught by recomputation? |
|---|---|---|---|---|
| $z = 1.645$ interval | wrong derivation | no | no | **yes** |
| "71% of the variance" | wrong quantity | no | no | **yes** |
| "92%" of stations | arithmetic slip | no | no | **yes** |
| "the budget exceeds 2400 m" | untraceable claim | sometimes (if it looks unrelated) | **yes** (no Results item restates it) | yes (no registry reference) |
| `figure_04_resolution` | miscited artefact | no | no | **yes** (citation audit) |

Four of the five are invisible to a careful reader: they are errors in a *computation*
or in a *reference*, not in a sentence. Only the untraceable claim is also caught by the
claim–evidence pairing, because it has no Results item to restate — which is why the
pairing check and the numerical audit are complements, not alternatives.

## ★★5. Two citation problems

- **Three listed figures never cited.** The reader meets figures the text never uses,
  cannot tell which one supports which claim, and a referee will ask which of them is
  the evidence for the headline number. It reads as a manuscript assembled from parts.
- **A cited figure does not exist.** The reader following the pointer finds nothing; in
  a submitted manuscript this indicates either a figure dropped in revision or a
  reference to a *different* document's figure, and it makes the surrounding claim
  unsupported.

The **non-existent citation is the more serious**: the first is a presentation defect
that a referee can resolve, while the second means a quantitative claim has no evidence
at all, and a referee cannot reconstruct the missing figure. Both are cheap to fix and
both belong to the audit, because a citation list is a machine-checkable object.

## ★★6. The quadrature check

$$\frac{2.001 - 1.999}{2.001} = 0.1\%.$$

For an exactly linear model the sampled total equals the quadrature sum exactly, because
variance is additive along a linear combination of independent inputs. A **nonlinear**
model would show a systematic gap that grows with the input uncertainties, and the
*fractional excess* of the sampled total over the quadrature sum is a direct estimate of
the interaction contribution ($\sum_{i<j} S_{ij}$ plus higher orders). The demo's Sobol
indices sum to $0.991$, leaving $0.9\%$ of the variance as interaction — consistent with
the $0.1\%$ standard-deviation difference ($2 \times 0.1\%$ in variance). Automating the
check is worthwhile for three reasons: it validates the arithmetic of the budget, it
quantifies the linearity assumption that the quadrature reporting relies on, and it
fails loudly when a component is inadvertently dropped from the sum — the most common
budget error of all.

## ★★7. An abstract claim list

Six sentences with their registry identifiers and Results items (a template; the
identifiers are this demonstration's):

| abstract sentence | claim | registry id(s) | Results item |
|---|---|---|---|
| "We invert Ps delay times at 45 stations to obtain crustal thickness." | 45 stations | `n_accepted` | Results 1 (data table) |
| "The mean Moho depth is $35.0$ km." | 35.04 km | `H_mean` | Results 2 |
| "The total uncertainty is $2.0$ km (1 sd)." | 2.001 km | `H_sd` | Results 3 (budget) |
| "The uncertainty is dominated by the assumed $V_p/V_s$, which contributes 47% of the variance." | $S_k = 0.474$ | `S_k` | Results 3 |
| "The systematic budget is 1.6 km against a statistical 1.2 km." | 1.600/1.198 | `H_sd_sys`, `H_sd_stat` | Results 3 |
| "The result agrees with the published value of $34 \pm 3$ km (reproduced)." | comparison | `H_mean`, `H_sd`, literature value | Discussion 2 |

An audit of a manuscript written from memory would be expected to flag the fourth and
sixth first: the sensitivity share is the number most often quoted from a different run
(or inverted, as the "71%" flag shows), and the comparison sentence is the one whose
uncertainty units are most often mismatched — a 95% interval in the paper compared with
a one-sigma value from the analysis.

## ★★8. The release elements, and the one whose absence is fatal

| element | what the reader does with it |
|---|---|
| repository structure | finds the step that produces the headline number |
| environment lock file | gets the same numerical results rather than slightly different ones |
| data statement / `download.py` | obtains the input at all |
| one-command reproduction | regenerates `results/registry.json` |
| tests | checks that the release works on their machine |
| licence and `CITATION.cff` | uses and cites the work legally |
| limitations | knows what will *not* reproduce |

The fatal omission is **the data statement with its query parameters and filters** — for
a seismic capstone, the network, station list, channels, time windows, magnitude and
distance ranges, and the access date. Without it the reader cannot obtain the input, so
every other element is inert: a correct, well-tested, licensed, one-command pipeline
that has no data to run on. Note the asymmetry with the environment: a missing lock file
changes the last digits of the result, while a missing data statement removes the result
entirely. If only one can be fixed, fix the data statement.

## ★★★9. Specification for your own capstone

**Audit specification.**

1. **Registry generation.** `scripts/make_registry.py` imports nothing from the
   manuscript; it runs the analysis modules and writes `results/registry.json` with, for
   each entry, `id`, `value`, `unit`, `derived_from`, `commit`. The registry is a
   build artefact, never edited by hand — a hand edit is detectable by regenerating and
   diffing.
2. **Claim list.** `manuscript/claims.yaml` lists every quantitative claim with its
   quoted value, its registry id(s) and the derivation expression. The audit evaluates
   the expression and compares with the quoted value under a **rounding-aware
   tolerance**: the tolerance is half a unit in the last quoted digit relative to the
   quoted precision (so "35.0 km" tolerates $\pm 0.05$, "4.35 s" tolerates $\pm 0.005$),
   and the comparison is done in the *quoted* units.
3. **Checks.** (a) value; (b) derivation, by recomputing from the registry expression;
   (c) quadrature of components against the total; (d) unit conversions between the
   abstract, tables and figures, driven by a declared unit per artefact; (e) tracing,
   every claim has at least one registry id; (f) citation, every cited figure and table
   exists and every existing one is cited at least once; (g) staleness, the registry's
   commit matches the current `HEAD` of the analysis.
4. **Rounding policy.** Quoted precision is declared per claim; the audit fails if the
   quoted value differs from the recomputed value by more than half the last quoted
   digit, and warns if the recomputed value has fewer significant digits than the
   quoted one (a precision claim that the analysis cannot support).
5. **Continuous integration.** The audit runs on every push and on the tagged release;
   a stale registry, a failing derivation or a missing citation fails the build. A
   release is tagged only when the audit passes on a freshly generated registry — which
   is what makes the release a *verified* commit rather than a convenient one.

**Release checklist.** Environment pinned and recreated in CI from scratch; data
statement with queries, filters, counts, hashes and access date, plus `download.py`;
one-command reproduction (`make reproduce`) writing the registry and the figures; tests
covering the analytic check, the synthetic recovery and at least one constant-change
failure; `LICENSE` for code and a separate statement for data; `CITATION.cff` with
version and DOI; a Limitations section naming what does not reproduce and pointing to
the synthetic example that exercises the same code path.

**What this specification does not catch.** It validates the manuscript against the
*analysis as it currently stands*; it cannot detect that the analysis itself is wrong —
a mis-specified forward model, a unit error inside a library call, a
mis-interpreted dataset. Those are caught by the verification step of
[25-06-03](../03-capstone-execution.md) (analytic check, synthetic recovery, end-to-end
test) and by the peer critique of [25-06-05](../05-capstone-defence.md). An audit
enforces consistency; verification establishes correctness; the two are different
guarantees, and a report that claims the first as if it were the second is the failure
mode this exercise is designed to expose.
