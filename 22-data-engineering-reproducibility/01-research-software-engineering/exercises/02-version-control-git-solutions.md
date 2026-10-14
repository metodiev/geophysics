# Solutions — 22-01-02 Version Control with Git: Branching, Rebasing, Conflicts

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [02 Version Control with Git](../02-version-control-git.md).

---

## ★1 — Reading the separation table

| Separation | Conflict probability |
|---|---|
| 15 lines | 0.998 |
| 30 lines | 0.216 |
| 60 lines | 0.000 |

Largest factor of change: between **15 and 30 lines**, where the probability
falls from $0.998$ to $0.216$, a factor of $0.216/0.998 = 0.216$, i.e. it drops
by a factor of 4.6. Between 30 and 60 lines it falls from $0.216$ to
$0.000$ (below the 20 000-trial resolution of $\approx 0.0005$), which is a
larger *relative* drop but from an already small base; the practically important
transition is 15 → 30 lines.

## ★2 — Rebase conflict probability

(a) With $n = 5W$ independent edits at per-edit conflict probability $p$,

$$P(\text{at least one conflict}) = 1 - (1-p)^{5W}, \qquad p = 0.03,\ 1-p = 0.97.$$

(b) $W = 1$: $1 - 0.97^{5} = 1 - 0.8587 = 0.141$.
$W = 10$: $1 - 0.97^{50} = 1 - 0.2181 = 0.782$.
$W = 30$: $1 - 0.97^{150} = 1 - 0.0104 = 0.990$.

All three equal the printed values (0.141, 0.782, 0.990).

## ★3 — Pointers and objects

- **branch** — a pointer (a file under `.git/refs` naming a commit); creating one
  moves nothing, committing moves it forward.
- **tag** — an annotated tag is an *object* (it carries a message and a tagger)
  that points at a commit; a lightweight tag is just a pointer. A tag does not
  move when you commit.
- **`HEAD`** — a pointer, usually to a branch pointer; a *detached* `HEAD` points
  directly at a commit.
- **commit** — an immutable object: a snapshot of the tree plus parent links.
  Nothing about it moves; a rewrite creates a new object with a new hash.

`git commit` moves the **current branch pointer** (and `HEAD` follows because it
points at that branch) to the new commit object.

## ★★4 — Separation 30 in a 900-line file

(a) Separation 30 lines → conflict probability **0.216** from the table. File
size does not enter the table: the model depends on edit proximity, not on the
file's length.

(b) The context table at separation 20 gives $0.531$ for 0 lines, $0.704$ for 1,
$0.937$ for 3 and $0.999$ for 6. The conflict condition is
$\text{gap} \le 2 \times \text{context}$, so reducing the context from 3 to 1
changes the threshold from 6 to 2 lines and cannot *increase* the probability.
Interpolating between the 1-line ($0.704$) and 3-line ($0.937$) rows at fixed
separation is not the relevant use of that table; the correct statement is that
at separation 30 the conflict probability is bounded by the probability that a
randomly long edit reaches within $2c$ lines, and with one line of context that
is roughly $0.216 \times (0.704/0.937) \approx 0.16$. Report it as
$\approx 0.16$, with the uncertainty of an interpolation from two rows.

(c) **Reducing** the context is the safer direction for *merging automatically*
(fewer conflicts to resolve), and it is what a merge tool does when it aligns
hunks aggressively. **Increasing** the context buys a wider safety margin: more
of the surrounding text is treated as one conflict region, so a merge that would
have applied cleanly but wrongly becomes a conflict a human inspects. Neither
direction changes the semantic risk of a silently wrong clean merge.

## ★★5 — Scaling the overlap fraction

(a) The observed fraction is $56/780 = 0.0718$ at a mean lifetime of 6.9 days.
For a mean lifetime of 2 days, scale linearly:

$$0.0718 \times \frac{2}{6.9} = 0.0208, \qquad
0.0208 \times 780 = 16.2 \approx 16\ \text{pairs}.$$

(b) The assumption is that the expected number of overlaps per pair is
**proportional to the lifetime**, i.e. that the rate at which two branches drift
into the same region is constant. It fails when the lifetime distribution is
heavy-tailed (the demonstration's lifetimes are exponential, standard deviation
$7.3$ days, so the mean is far from typical) and when edits are not uniform over
the file: a hotspot module accumulates overlaps faster than proportionality
predicts.

(c) Daily integration from the model is $1 - 0.97^{5} = 0.141$, which is the
probability that **one branch** meets a conflict while rebasing. The 7.2 % is the
fraction of **pairs** whose regions overlap, a different quantity measured over a
different population; the two numbers are not expected to agree, and comparing
them requires stating which population each describes.

## ★★6 — Choosing a history

For a paper's software, choose **(A) the linear history**: 12 tidy commits that
each correspond to a described step of the method are the most useful artefact
for a reader who wants to check the implementation. Then state what is lost: the
merge history (B) preserves the **actual order of work and the points at which
independent lines were integrated**, including failed directions that were later
merged rather than rebased away. (A) presents a cleaned-up narrative; (B) is a
record of the process. If the paper's claim rests on the process — for example a
claim that a second implementation reproduced the first independently — then (B)
is evidence and (A) is not, which is a reason to keep (B) and to say so in the
README rather than to rewrite it.

## ★★★7 — Measuring a real conflict rate

**Population.** All merges recorded in the repository's default branch over a
stated window (e.g. every merge commit whose second parent is not an ancestor of
the first, excluding merges created by a rebase).

**Inclusion rule.** Include a merge if both sides changed at least one file that
the other side also changed; count a **conflicted merge** if the merge commit's
tree differs from a hypothetical automatic resolution — operationally, if
`git rerere` recorded a resolution or if the merge commit's parents' merge
produced conflict markers in any intermediate state (recoverable from the merge
commit or from a re-run of the merge on a scratch clone).

**Operational definition of a conflict.** A merge is conflicted if replaying
`git merge` in a scratch clone at the recorded merge base produces at least one
path with conflict markers. This is repeatable and does not require the original
worktree.

**Confounders.** (i) *File size and shape*: a 5000-line file with long functions
conflicts differently from a directory of short modules at the same edit volume,
so stratify by the size of the changed files. (ii) *Branch lifetime*: as in §5,
long-lived branches accumulate more upstream edits, so record the lifetime of
each branch and either stratify on it or model it.

**Comparison.** The uniform model predicts a per-pair conflict probability from
the separation of edit regions, so for the same population it predicts a
fraction of overlapping pairs; report the measured fraction, the predicted
fraction and a binomial confidence interval on the measured fraction, stratified
by file size and lifetime. A single aggregate number could not distinguish the
model being wrong from the population being unrepresentative.

## ★★★8 — Measuring the per-edit conflict probability

**Design.** From the same repository, extract every merge and the sequence of
upstream edits between the branch point and the merge. For each edit, record
whether replaying the merge conflicts *at that edit's resolution point* — in
practice, mark an edit as conflicting if the automatic merge of the two parents
fails within the edit's hunk region. Estimate $\hat p$ as the number of
conflicting edits divided by the total number of edits, with a Wilson confidence
interval; the estimate must be stratified by file size, since $\hat p$ is not a
constant.

**Uncertainty.** $\hat p$ has binomial standard error
$\sqrt{\hat p(1-\hat p)/n}$ over $n$ edits; for $n = 400$ edits and
$\hat p = 0.03$, $SE = \sqrt{0.03 \times 0.97/400} = 0.0085$, so with 95 % confidence
$\hat p = 0.030 \pm 0.017$. A repository with 400 edits cannot pin a 3 % rate
better than a factor of two.

**Observable that would show independence is wrong.** Under independence the
number of conflicting edits per merge is **binomial** with parameters
$(n_{\text{edits}}, p)$, whose variance is $np(1-p)$ and which approaches Poisson
for small $p$. Non-independence shows up as **over-dispersion**: the empirical
variance of the count per merge exceeds the binomial variance. Conflicting edits
already imply this, because one conflict in a hotspot region makes its neighbours
far more likely to conflict too.

## ★★★9 — Test-based detection of semantic conflicts

**Scheme.** Keep a suite of *invariant* tests that read the merged tree and assert
properties that must hold whatever the change: unit-consistency checks (a computed
quantity equals the same quantity in a stated unit), conservation or limiting-case
checks (a forward model equals its analytic limit), and pinned numerical results
from a frozen reference dataset. Run the suite in continuous integration on every
merge candidate, before the merge is accepted:

```python
def test_unit_consistency():
    assert_close(strain_rate(dt=2.0), expected, atol=1e-12 * expected)
```

**False negative mode.** Tests only cover what they assert. A merge that changes a
coefficient and the units that multiply it can be self-consistent with respect to
every invariant the suite checks and still be wrong, because the suite encodes the
same mistaken assumption as both sides of the merge. Coverage is the limiter, and
coverage is exactly what a semantic conflict is designed to escape.

**What it cannot detect.** It cannot detect a conflict whose resolution requires
information that is nowhere in the repository: which of two competing physical
models the group decided to adopt, a changed instrument calibration, or a
deliberate change of convention. Those require the merge to be reviewed by a
person against the decision record, which is why review
([22-01-03](../03-code-review.md)) is not replaced by CI.
