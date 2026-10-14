---
id: 24-03-06
title: "Research Ethics, Plagiarism, Authorship and Integrity"
level: graduate
prereqs: ["24-02-03", "24-01-04"]
estimated_minutes: 50
tags: [research, ethics, plagiarism, authorship, integrity, attribution]
---

# Research Ethics, Plagiarism, Authorship and Integrity

Ethics in research is mostly a set of practices that are checkable, and the two
that this lesson quantifies are plagiarism screening and authorship criteria.
Both are usually discussed as matters of character; both are better treated as
measurement problems with thresholds, because a threshold can be chosen
deliberately and a character cannot.

The organising idea is that **credit and text are both attribution systems, and both
fail at the boundary**. Similarity scores cannot separate heavy paraphrase from a
legitimate re-description of a standard method, and authorship criteria cannot
separate substantial contribution from courtesy without a stated rule. The lesson
measures both boundaries and states what each test can and cannot decide.

> **Data provenance.** All numbers are **SYNTHETIC**. The text is a generated word
> sequence over a small vocabulary, not prose from any source, and the contribution
> matrix is invented. Nothing here is compared with any real document.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** plagiarism, self-plagiarism, redundant publication and
   insufficient attribution, and **state** what each requires.
2. **Compute** text similarity with two different measures and **explain** why they
   disagree.
3. **Choose** a similarity threshold and **state** both error rates it trades.
4. **Apply** a stated authorship criterion to a contribution matrix and **compute**
   how the author list changes with the rule.
5. **Quantify** the effect of a gift author and of an omitted contributor on the
   credit per author.
6. **State** the practices that make integrity checkable rather than aspirational:
   data availability, provenance, and a written contribution statement.

## Prerequisites

- [24-02-03 Writing Methods Sections That Can Be Reproduced](../02-scientific-writing/03-writing-methods.md) —
  the reporting practice that integrity depends on.
- [24-01-04 Systematic Literature Search and Reference Management](../01-reading-research-literature/04-literature-search.md) —
  the provenance discipline for sources.

## 1. Four failures, four remedies

| Failure | What it is | Remedy |
|---|---|---|
| Plagiarism | Reusing another's text or idea without attribution | Quote and cite; paraphrase with a citation |
| Self-plagiarism | Reusing your own published text without disclosure | Cite your own work; disclose overlap |
| Redundant publication | Publishing the same result twice as new | State the relationship; cite the earlier version |
| Insufficient attribution | Using data, code or ideas without credit | Cite the dataset, software and prior methods |

The common structure is that attribution is a *claim about provenance*, and it is
checkable in every case: the source either exists and is cited, or it is not.
Where the rules are conventions rather than laws — how much overlap between two
papers is acceptable — journals and publishers state their own, and the honest
practice is to disclose and let an editor decide rather than to self-assess.

## 2. Similarity is two different measurements

The demonstration builds a $220$-word synthetic passage and applies increasing
random word substitution to it:

| Substitution rate | $5$-gram shingle Jaccard | Bag-of-words cosine |
|---|---|---|
| $0\%$ | $1.000$ | $1.000$ |
| $5\%$ | $0.606$ | $0.985$ |
| $10\%$ | $0.385$ | $0.965$ |
| $20\%$ | $0.200$ | $0.950$ |
| $30\%$ | $0.059$ | $0.908$ |
| $50\%$ | $0.019$ | $0.882$ |

The two measures answer different questions. Shingles measure **sequence reuse**:
substituting one word breaks up to five consecutive shingles, so the score
collapses quickly. The cosine measures **vocabulary reuse**: the words are still
there, so it barely moves. A screening system that reports one number is reporting
one of these and not the other, and a reader should know which.

Against four reference texts:

| Text | Shingle Jaccard | Cosine |
|---|---|---|
| verbatim copy | $1.000$ | $1.000$ |
| light paraphrase | $0.346$ | $0.958$ |
| heavy paraphrase | $0.056$ | $0.909$ |
| independent text | $0.000$ | $0.725$ |

A shingle threshold near $0.7$ cleanly separates a copy from any paraphrase; a
cosine threshold near $0.9$ would flag heavy paraphrase as similar and would also
flag a large fraction of independent texts in the same technical domain, because
they share vocabulary. **Both measures are screens, not findings.** What makes a
finding is reading the passage and its source: the score tells you which pairs to
read.

## 3. Authorship is a rule applied to a matrix

Score each contributor against a stated list of criteria (the ICMJE
recommendations use four: substantial contribution; drafting or critical revision;
final approval; accountability). The demonstration's synthetic matrix gives:

| Rule | Authors |
|---|---|
| any contribution ($\geq 1$ criterion) | $6$ |
| $\geq 2$ criteria | $5$ |
| $\geq 3$ criteria | $3$ |
| all $4$ criteria | $1$ |

Six contributors produce four different author lists depending on the rule. The
defensible practice is: choose the rule, state it, apply it uniformly, and record
the contributions themselves in a contribution statement so that the record
survives the choice.

**Gift and ghost authorship, measured.** Taking the $\geq 3$ rule as the stated
rule, the demonstration reports:

| Scenario | List size | Mean criteria per author |
|---|---|---|
| stated rule ($\geq 3$) | $3$ | $3.33$ |
| plus one gift author ($0$ criteria) | $4$ | $2.50$ |
| loosest rule ($\geq 1$) | $6$ | $2.50$ |
| stated rule, strongest contributor omitted | $2$ | $3.00$ |

Adding one gift lowers the mean credit per author from $3.33$ to $2.50$ — exactly
the same dilution as opening the list to everyone with any contribution. Credit is
not conserved in the way authorship lists imply: what changes is the *information
content* of authorship, and a list that includes everybody names nobody. A ghost is
the mirror image: the contributor disappears and the record is simply wrong, which
is a failure of accuracy as well as of fairness.

## 4. Making integrity checkable

Five practices convert integrity from a disposition into a record:

1. **Raw data are immutable and archived.** Every derived product is regenerated;
   see [24-06-01 Publishing Data and Code Alongside Papers](../06-reproducible-publication/01-data-publication.md).
2. **Provenance is recorded as it happens**, not reconstructed: source, query,
   date, parameters, version.
3. **A contribution statement** lists who did what, using a standard taxonomy
   (for example the CRediT roles), and it is written before submission when
   memories are still independent.
4. **Sources are cited with their identifiers** — dataset DOIs, software versions —
   not with a vague acknowledgement; see
   [24-06-04 Citation Practice and Attribution of Data and Software](../06-reproducible-publication/04-citation-and-attribution.md).
5. **Conflicts of interest and funding are disclosed** in the form the venue
   requires, including in-kind support and data-sharing agreements.

## Assumptions and regime of validity

1. **The text is synthetic.** Similarity values depend on the vocabulary, the
   shingle length and the domain; they are illustrative of the mechanism, not of a
   screening service's behaviour.
2. **Substitution is random and positional structure is preserved.** Real paraphrase
   reorders and restructures, which reduces shingle similarity further.
3. **The contribution matrix is invented.** The criterion probabilities are chosen
   to give an interesting spread, not to describe any team.
4. **The four criteria are a summary of a longer standard.** Journals vary, and the
   ICMJE recommendations themselves are revised; check the version a venue cites.
5. **A similarity score is evidence, not a verdict.** Every case requires reading
   the passage and the source, and intent is not measurable from a score.

## The honest summary

Similarity is two measurements — sequence reuse and vocabulary reuse — and they
disagree by design: substitution at $30\%$ drops the shingle score to $0.059$ while
the cosine stays at $0.908$. Authorship is a threshold applied to a matrix: six
contributors give lists of $6$, $5$, $3$ or $1$ authors depending on the rule, and
one gift author dilutes the mean credit exactly as much as opening the list to
everyone. State the rule, record the contributions, and read before you judge.

## Python demonstration

[`code/research_ethics_demo.py`](./code/research_ethics_demo.py) prints four
labelled sections: similarity versus substitution rate under both measures; the
four reference texts; the authorship matrix with four thresholds; and the credit
arithmetic for gift, ghost and loosest-rule lists.

```bash
cd 24-research-papers-writing/03-research-methods-and-rigour/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_ethics_demo.py
```

## Exercises

Problems are in
[`exercises/06-research-ethics-exercises.md`](./exercises/06-research-ethics-exercises.md),
worked answers in
[`exercises/06-research-ethics-solutions.md`](./exercises/06-research-ethics-solutions.md).

## Mastery checkpoint

1. State the difference between plagiarism, self-plagiarism and redundant
   publication, with an example of each from your own field's practice.
2. Compute a shingle similarity and a cosine similarity for two paragraphs you have
   written, and explain the difference between the two numbers.
3. Write your authorship criterion in one sentence and apply it to a paper you are
   writing; list who qualifies and who does not.
4. Write a contribution statement for that paper using standard roles.
5. List the provenance records you did not keep during your last project, and how
   you would keep them next time.

## Common pitfalls

1. **Treating a similarity score as a verdict.** It selects pairs for reading.
2. **Assuming paraphrasing avoids plagiarism.** An unattributed idea is plagiarism
   however the words are arranged.
3. **Reusing your own Methods verbatim across papers without disclosure.** It is
   usually acceptable with a citation; it is a problem when undisclosed.
4. **Deciding authorship at submission.** Contributions should be agreed early and
   recorded as they happen.
5. **Listing a supervisor who did not contribute.** It dilutes the information in
   the list, which is the harm, apart from any fairness question.
6. **Skipping data and software citations.** They are the attribution system for
   the artefacts a result depends on.

## Where this is used

- **Every submission:** the contribution statement, the conflict declaration and
  the data statement are the checkable artefacts.
- **Supervision:** authorship conversations belong at the start of a project, not
  at the end; see
  [24-05-04 Academic CVs, Research Statements and Career Paths](../05-thesis-and-proposals/04-cv-and-career.md).
- **Reviewing:** confidentiality and conflict rules are conduct requirements, not
  courtesies; see [05 Peer Review Practice](05-peer-review-practice.md).
- **Data and code release:** licences and attribution make reuse lawful and
  traceable; see
  [22-01-05 Licensing and Citation](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md).

## Related lessons

- [24-06-04 Citation Practice and Attribution of Data and Software](../06-reproducible-publication/04-citation-and-attribution.md) —
  the attribution system for artefacts.
- [24-03-04 Reproducible Research Practice End to End](04-reproducible-research-practice.md) —
  the provenance practice that integrity depends on.
- [24-01-04 Systematic Literature Search and Reference Management](../01-reading-research-literature/04-literature-search.md) —
  where the source records come from.
- [21-09-03 Data Ethics in the Geosciences](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/03-data-ethics-geoscience.md) —
  the ethical questions that concern data rather than text.

## Self-assessment checklist

- [ ] I can distinguish four attribution failures and their remedies.
- [ ] I can compute two similarity measures and explain their disagreement.
- [ ] I can choose a threshold and state both of its error rates.
- [ ] I can state and apply an authorship criterion.
- [ ] I can quantify the effect of a gift or a ghost on the record.
- [ ] I can name the five practices that make integrity checkable.
