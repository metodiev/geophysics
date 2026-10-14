---
id: 22-01-03
title: "Code Review and Collaborative Development"
level: graduate
prereqs: ["22-01-02", "22-01-01"]
estimated_minutes: 50
tags: [code-review, collaboration, software-engineering, quality-assurance]
---

# Code Review and Collaborative Development

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** review as a sampling process with a detection probability, not as a
   guarantee, and **state** what a review can and cannot establish.
2. **Compute** the fraction of defects detected for a change of a given size under
   a stated inspection model, and **identify** the size at which the escape rate
   falls below a stated target.
3. **Quantify** the marginal return of a second independent reviewer, in both
   escaped defects and person-hours.
4. **Report** an escape rate with its uncertainty, and **explain** why a single
   review outcome cannot certify a process.
5. **Review** numerical and data-handling code against a checklist of the failure
   modes that matter in geophysics (units, boundary conditions, seeding,
   broadcasting, I/O and dtype).
6. **Write** review comments that are specific, actionable and separated into
   correctness, clarity and preference.

Review is a human process, so this lesson measures a **SYNTHETIC** model of it:
a chosen defect density, inspection rate and detection law. The numbers are model
outputs printed by the demonstration; no defect database or published review
study is quoted.

## Prerequisites

- [22-01-02 Version Control with Git](./02-version-control-git.md) — the branch
  and merge machinery that a review precedes.
- [22-01-01 Designing Software for Scientific Research](./01-software-design-science.md) —
  why a change is rarely local, and therefore what a reviewer must read.

## 1. Intuition: review is a detector, and detectors miss things

A code review is a measurement performed by a person with limited attention. It
does not prove correctness; it changes the probability that a defect survives to
publication. Two consequences follow immediately and both are counter-intuitive:

- **Bigger reviews catch more defects in total but leave more behind per line.**
  Attention is spread thinner as the change grows, so the detection probability
  per defect falls; the escape rate per thousand lines is therefore *worse* for
  large changes even though the reviewer worked longer.
- **A second reviewer is worth more than a longer first review.** Two independent
  passes combine multiplicatively in the miss probability, which the arithmetic
  below makes concrete.

## 2. What review is for in research code

In product software, review enforces a style guide and an interface contract. In
research code the priorities are different and should be stated in the review
template:

1. **Is the method the one described in the paper?** Review the *physics*, not
   the formatting: units, coordinate conventions, sign conventions, boundary
   conditions.
2. **Can the claimed result be reproduced?** Seeded randomness, no hidden state,
   inputs pinned by version.
3. **Are the failure modes handled?** Empty input, single-sample input,
   NaN-producing division, sing-lantern values in a forward model.
4. **Will a stranger understand it?** Naming, the relationship between code and
   equation, the docstring that states units.
5. **Is the change minimal and single-purpose?** A change that does two things
   cannot be reverted in one step.

Clarity and correctness are separated deliberately: a comment about style is
cheap to make and cheap to ignore, while a question about a sign convention can
change a published number.

## 3. A model of detection

Let a change contain $D$ defects, with a chosen defect density $\rho$ defects per
kLOC, so $D = \rho L / 1000$ for $L$ lines. Let the reviewer inspect at rate $R$
lines per person-hour, so the inspection time is $t = L/R$ hours. Assume the
probability that the reviewer detects any one defect grows with time and
saturates:

$$p_{\text{det}}(L) = 1 - e^{-k t} = 1 - e^{-k L / R},$$

with $k$ the detection rate in $\text{hour}^{-1}$. The choice of a saturating law
is not cosmetic: it encodes the observation that a reviewer who has spent an hour
has found most of what inspection will find, and further time adds progressively
less. With the demonstration's teaching values $\rho = 8$ defects/kLOC,
$R = 200$ lines/h and $k = 0.90\ \text{h}^{-1}$, and $L = 200$ lines,

$$t = \frac{200}{200} = 1.0\ \text{h}, \qquad
p_{\text{det}} = 1 - e^{-0.9 \times 1.0} = 1 - 0.4066 = 0.593.$$

The **escape rate per kLOC** is then
$\rho\,(1 - p_{\text{det}}) = 8 \times 0.407 = 3.25$ defects per kLOC, which is
independent of $L$ only through $p_{\text{det}}(L)$ — that is, it falls as the
review grows, which is the counter-intuitive result of §1 made quantitative.

## 4. Measured tables

Detection and inspection cost, for the six sizes simulated:

| Size (lines) | Person-hours | $p_{\text{det}}$ | Defects found in review |
|---|---|---|---|
| 25 | 0.12 | 0.106 | 0.02 |
| 50 | 0.25 | 0.201 | 0.08 |
| 100 | 0.50 | 0.362 | 0.29 |
| 200 | 1.00 | 0.593 | 0.95 |
| 400 | 2.00 | 0.835 | 2.67 |
| 800 | 4.00 | 0.973 | 6.23 |

Escape rate per kLOC, which is what reaches the paper:

| Size (lines) | Escaped defects per kLOC |
|---|---|
| 25 | 7.15 |
| 50 | 6.39 |
| 100 | 5.10 |
| 200 | 3.25 |
| 400 | 1.32 |
| 800 | 0.22 |

Solving $8\,e^{-0.9L/200} < 1$ gives the size at which the escape rate falls below
one defect per kLOC:

$$L > \frac{200}{0.9}\ln 8 = 222.2 \times 2.0794 = 462\ \text{lines},$$

which the demonstration finds by scanning the curve: **462 lines**. Read
carefully: this says a change must be *at least* 462 lines long before review
drives the escape rate below 1 per kLOC, because a short change cannot justify
enough inspection time to reach high detection. The correct response is not to
enlarge changes but to review short changes **more than once**, or to accept a
higher escape rate on them and catch it with tests — a point the module's testing
lesson takes up.

## 5. One reviewer or two?

A second **independent** reviewer with the same detection probability leaves
$(1-p)^2$ of defects:

$$p_2 = 1 - (1-p)^2 = 2p - p^2,$$

and the reduction in escaped defects is:

| Size (lines) | Escapes, one | Escapes, two | Reduction |
|---|---|---|---|
| 25 | 7.15 | 6.39 | 10.6 % |
| 50 | 6.39 | 5.10 | 20.1 % |
| 100 | 5.10 | 3.25 | 36.2 % |
| 200 | 3.25 | 1.32 | 59.3 % |
| 400 | 1.32 | 0.22 | 83.5 % |
| 800 | 0.22 | 0.01 | 97.3 % |

For a 200-line change the arithmetic is
$p_2 = 1 - (1-0.593)^2 = 1 - 0.1656 = 0.834$, so escapes fall from 3.25 to
$8 \times 0.166 = 1.32$ per kLOC, a $59.3\ \%$ reduction. The cost doubles the
person-hours. Two reviewers on a 25-line change buy only $10.6\ \%$, because the
first reviewer already had too little time to find much: redundancy cannot
compensate for insufficient inspection of a short change.

## 6. The escape rate is a distribution

With $D = 1.60$ expected defects in a 200-line change and $p = 0.593$, the number
escaped is random. Simulating 2000 reviews gives a mean of $0.051$ escaped
defects per change with standard deviation $0.020$, and a 5th-to-95th percentile
range of $0.02$ to $0.08$. Two consequences:

- quoting a process's escape rate to two significant figures from one project is
  meaningless: the sampling spread is comparable to the effect being discussed;
- a *process* change (adding a reviewer, shrinking changes) is detectable only
  against this spread, which requires many changes, not one.

## 7. Reviewing numerical and data code: what to look for

A review checklist for geophysical code, ordered by how often each item is the
actual defect:

1. **Units.** Every variable's unit in the docstring; no bare conversions.
2. **Boundary conditions.** What happens at $n=0$, at a single sample, at the
   ends of a convolution, at the first and last element of a filter.
3. **Silent broadcasting.** A `(n,)` array combined with an `(n,1)` array
   produces an `(n,n)` result without error. Check shapes explicitly.
4. **Seeding.** Random draws use an explicit `np.random.default_rng(seed)`; a
   global `np.random.seed` call anywhere else in the process invalidates it.
5. **I/O separation.** The computation takes arrays; reading and writing happen
   in one place at the edge.
6. **Dtype and precision.** `float32` accumulation over a long series loses
   precision; an integer division silently truncates.
7. **Copy versus view.** A slice is a view: an in-place write to a slice of a
   caller's array modifies the caller's data.
8. **Cost.** A loop that allocates inside it dominates runtime for no reason;
   measure before asserting, but say so in the comment.

## 8. Worked example: sizing a review request

A colleague opens a pull request that touches 820 lines across four files and asks
for a review before a deadline.

1. **Compute the cost.** At 200 lines/h, the review is $820/200 = 4.1$ person-hours
   — a day of work, not a coffee break.
2. **Compute the detection.** $p = 1 - e^{-0.9 \times 4.1} = 0.975$; escapes
   $= 8 \times 0.025 = 0.20$ per kLOC, i.e. $0.20 \times 0.82 = 0.16$ defects
   expected.
3. **Compare with splitting.** Four reviews of 205 lines each cost the same
   4.1 hours in total but give four independent passes: escapes per kLOC
   $= 1.32 \times (205/200) \approx 1.35$, an order of magnitude worse. The
   honest recommendation is therefore "split into four pull requests and review
   each **with an explicit budget of an hour**", because the total detection is
   what matters and the review is bounded by attention, not by line count alone.
4. **Ask for the tests.** The measurement cannot tell you what the reviewer will
   find; the tests are what make the escape rate irrelevant for the covered
   behaviour, which is the argument of
   [22-07-01](../07-software-testing-quality/01-test-strategy-science.md).

## Assumptions and regime of validity

1. **Defects are independent and equally detectable.** A real change contains one
   systematic error (a wrong sign, a wrong unit) that is either seen or not, and
   with a much larger consequence than a lone typo; the model treats all defects
   as exchangeable.
2. **Density is constant in time and author.** Defect density varies with
   experience, problem difficulty and churn; the model isolates review size.
3. **The detection law is exponential in time.** Any saturating law gives the same
   qualitative result (large reviews leak), but the *numbers* move with the law.
4. **Reviewers are independent.** Two reviewers who read together, or who share a
   model of the code's intent, duplicate their misses rather than covering each
   other.
5. **Lines are the cost unit.** Time is spent on understanding, not on lines;
   a 30-line change touching a subtle numerical scheme can cost more than a
   reformat of 800 lines.

## The honest summary

Review is the cheapest defect detector available and the hardest to quantify,
because its detection probability depends on attention, which is spread thinner
as a change grows. Under a stated teaching model — 8 defects per kLOC, 200 lines
inspected per hour, exponential detection in time — a 200-line change is reviewed
for one person-hour, detects 59 % of defects, and leaves 3.25 defects per kLOC; an
800-line change detects 97 % but the same *density* of work; and the escape rate
falls below one defect per kLOC only for changes of about 462 lines or more. A
second independent reviewer removes 10.6 % of escapes on a short change and 59.3 %
on a 200-line one. The escape count itself is a distribution (mean 0.051, s.d.
0.020 for a 200-line change), so process claims need many changes to support them.
The practical rules that survive the model are: keep changes small and
single-purpose, review early, use tests as the backstop, and review the physics
before the style.

## Python demonstration

[`code/code_review_demo.py`](./code/code_review_demo.py) prints, with a fixed seed
`np.random.default_rng(20261014)`:

1. detection probability, inspection hours and defects found versus change size;
2. escape rate per kLOC and the 462-line crossing;
3. the one- versus two-reviewer comparison and the percentage reduction;
4. a 2000-review Monte Carlo of escapes for a 200-line change, with the mean and
   the 5th–95th percentile range.

```bash
cd 22-data-engineering-reproducibility/01-research-software-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code_review_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/03-code-review-exercises.md`](./exercises/03-code-review-exercises.md)
and
[`exercises/03-code-review-solutions.md`](./exercises/03-code-review-solutions.md).

## Mastery checkpoint

Without notes: a 100-line change is reviewed by one person for 30 minutes.

1. Compute the detection probability under
   $p = 1 - e^{-0.9t}$ with $t$ in hours, and the escaped defects per kLOC at a
   density of 8 per kLOC.
2. State what changes if the reviewer is given a second hour, and what changes if
   a second reviewer is given the first hour instead.
3. Name three checklist items from §7 that a *test* could check automatically, and
   one that it cannot.
4. Your colleague reports "review found all the bugs". State the measurement that
   would be needed to support that claim.

## Common pitfalls

1. **Reviewing for style and missing the sign convention.** Comments about
   formatting are the cheapest to make and the least valuable here.
2. **Treating review as approval.** The output of a review is a list of questions
   and defects, not a stamp; the author is responsible for correctness.
3. **Reviewing 1500-line pull requests.** The model in §4 measures the penalty:
   detection saturates while the escape density falls slowly.
4. **Assuming two reviewers are independent when they are not.** Sequential
   reviewers who share the same framing duplicate their misses.
5. **Reporting an escape rate from one project.** The escape count is a
   distribution (mean 0.051, s.d. 0.020 on a 200-line change); a single project
   cannot resolve a process effect against that spread.

## Where this is used

- **Preparing a paper's code for release** — the review is where units and
  conventions are caught before a reader runs the code: see
  [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Onboarding a new group member** — reviewing someone's code is the fastest way
  to transfer the conventions of a laboratory's models.
- **Maintenance of long-lived codes** — the change-size discipline is what keeps a
  decade-old inversion package reviewable.
- **Security of shared infrastructure** — reviewing data-handling and credential
  handling is the only defect detector for the code path that runs once a month:
  see [22-05-01 Project Directory Structure and Conventions](../05-collaboration-and-project-management/01-project-structure.md).

## Related lessons

- [22-01-04 Documentation, Docstrings and READMEs That Work](./04-documentation.md) —
  the artefact a reviewer relies on to understand intent.
- [22-07-01 Test Strategy for Numerical and Data Code](../07-software-testing-quality/01-test-strategy-science.md) —
  the automated backstop for what a reviewer misses.
- [22-07-02 Continuous Integration for Research Software](../07-software-testing-quality/02-continuous-integration.md) —
  running that backstop on every change.
- [03-13-04 Code Quality: Style, Linting and Review](../../03-scientific-computing/13-testing-profiling-packaging/04-code-quality.md) —
  the automated style checks that free review time for substance.

## Self-assessment checklist

- [ ] I can state review as a sampling process with a detection probability.
- [ ] I can compute detection and escape rate for a change of a given size.
- [ ] I can compute the effect of a second independent reviewer.
- [ ] I can explain why the escape count needs a distribution, not a number.
- [ ] I can apply the numerical-code checklist to a diff.
- [ ] I can write a review comment that names the consequence of the defect.
