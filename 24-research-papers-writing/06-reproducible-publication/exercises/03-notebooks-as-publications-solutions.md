# Solutions — 24-06-03 Notebooks as Publications

> Read after attempting. Numbers computed. Lesson:
> [03 Notebooks as Publications](../03-notebooks-as-publications.md).

---

## ★1 — Chain probability for $25$ cells

$$h = 0.30 \times 0.03 = 0.009,$$
$$\mathbb{P}(\text{at least one}) = 1 - (1 - 0.009)^{25}
= 1 - 0.991^{25} = 1 - 0.7977 = 20.2\%.$$

About one notebook in five of this length contains a hidden dependency. The per-cell
hazard is small; the exponentiation is what makes it matter.

---

## ★2 — Length dependence

| Cells | $\mathbb{P}$(at least one hidden dependency) |
|---|---|
| $5$ | $1 - 0.991^{5} = 4.4\%$ |
| $10$ | $8.6\%$ |
| $50$ | $36.4\%$ |
| $100$ | $59.5\%$ |

The probability rises steeply and then flattens, growing from $4.4\%$ to $59.5\%$ as
the notebook grows twentyfold. The trend in one sentence: **doubling the number of
cells roughly doubles the failure probability while that probability is small, and
saturates near one for long notebooks.**

---

## ★3 — Three symptoms, one visible offline

1. **Missing execution counts** — a cell with output but no stored count. Visible in
   the file, offline.
2. **Non-monotonic execution counts** — counts that jump, recording a re-run session.
   Visible in the file, offline.
3. **Variables used before definition** — the true failure. Visible only by running the
   notebook from the top, or by inspecting the source and tracking definitions, which
   is slow and error-prone by hand.

So two of the three symptoms are visible in the deposited file, which is what makes an
offline audit possible at all.

---

## ★4 — Failure and reproduction probability

$$\mathbb{P}(\text{at least one failure}) = 1 - (1 - 0.30)(1 - 0.04)
= 1 - 0.70 \times 0.96 = 1 - 0.672 = 32.8\%,$$
$$\mathbb{P}(\text{reproduces}) = 0.672 = 67.2\%.$$

Note that the two causes are combined multiplicatively, not additively: a notebook
survives only if it avoids both. The additive approximation ($34\%$) overstates the
failure rate slightly, and the error grows as both probabilities grow.

---

## ★5 — Pinning versus discipline

$$\text{hidden state} = 0.30, \quad p_{\text{env}} = 0.05 \to 0.01:$$
$$\text{total failure unpinned} = 1 - 0.70 \times 0.95 = 1 - 0.665 = 33.5\%,$$
$$\text{total failure pinned} = 1 - 0.70 \times 0.99 = 1 - 0.693 = 30.7\%.$$

If hidden state is removed:

$$\text{total failure unpinned} = 0.05 = 5.0\%, \qquad
\text{total failure pinned} = 0.01 = 1.0\%.$$

Pinning alone moves the failure rate by $2.8$ percentage points; removing hidden state
moves it by $28.5$ points, and only then does pinning's own improvement ($4$ points)
become visible in relative terms. The order matters: **fix hidden state first**, then
pin.

---

## ★6 — Splitting a large notebook

All five notebooks reproduce:

$$0.86^{5} = 0.4704 = 47.0\%.$$

At least four reproduce:

$$0.86^{5} + 5 \times 0.86^{4} \times 0.14
= 0.4704 + 5 \times 0.5470 \times 0.14 = 0.4704 + 0.3829 = 85.3\%.$$

So a $100$-cell notebook at $35\%$ becomes, as five $20$-cell notebooks, a $47.0\%$
chance that everything runs and an $85.3\%$ chance that at least four of the five do.
The second number is the practically useful one: a reader who needs four of the five
analyses to work has an $85\%$ chance, and can fix the fifth in isolation — which is
the real gain from splitting, since the failures are now independent and locatable.

---

## ★7 — Does an execution-order test help?

**Unit.** One deposited notebook.

**Outcome.** Whether the notebook runs to completion and produces outputs matching the
deposited ones, when executed on a machine other than the author's, from the deposited
materials alone.

**Design.** Difference-in-differences across research groups or repositories: groups
that add an automated order test to their continuous integration are the treated units,
matched against groups that do not. Compare the change in the failure rate before and
after adoption.

**Confound.** Groups that adopt execution tests are, by that act, better maintained:
they have active CI, they review code, they pin environments. So the measured
improvement includes everything else that makes a group careful. The honest report
presents the difference-in-differences estimate with this stated, adds a measure of
general maintenance activity as a covariate, and — where possible — examines a
placebo outcome that the test should not affect (for example, whether figures are
regenerated, which no order test checks).

---

## ★8 — Auditing notebooks offline

**Sampling.** Supplementary notebooks attached to articles in a stated window and
journal set, including those that failed to run when a reader attempted them. Report
the flow from articles to analysable notebooks; a common and important result is that
many articles carry no notebook at all.

**Three offline checks.**

1. **Execution-count monotonicity**: extract the stored execution counts in source
   order and test whether they are strictly increasing.
2. **Output-without-count**: count cells that carry outputs but no execution count.
3. **Static dependency order**: parse the source, build the set of variables each cell
   defines and each cell uses, and flag cells that use a name defined later. This
   requires careful handling of loops, function scopes and magics, so state the parser
   and its known limitations.

**Agreement statistic.** Two coders apply the third check to a $10\%$ sample, because
it is the one needing judgement; report Cohen's $\kappa$ for the binary "uses a later
definition" flag. Checks 1 and 2 are mechanical and need no agreement figure, but a
$10\%$ double-extraction is still worthwhile to catch parser bugs.

**Why offline detection underestimates.** The three checks find signatures of hidden
state; a notebook can be non-reproducible for reasons that leave no signature:
environment differences, hard-coded absolute paths, data that were never deposited,
and interactive steps that were never cells. So the audit's rate is a **lower bound**
on the failure rate, and the report should say so — or better, pair the offline audit
with an execution attempt on a sample, and report both rates.
