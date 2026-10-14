---
id: 22-01-02
title: "Version Control with Git: Branching, Rebasing, Conflicts"
level: intermediate
prereqs: ["03-13-06", "22-01-01"]
estimated_minutes: 45
tags: [version-control, git, collaboration, reproducibility, software-engineering]
---

# Version Control with Git: Branching, Rebasing, Conflicts

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** a Git repository as a directed acyclic graph of immutable
   snapshots, and **distinguish** a branch (a movable pointer) from a tag (a
   fixed name).
2. **Describe** a three-way merge in terms of the merge base, and **predict** when
   two edits will conflict.
3. **Compute** the conflict probability of two edits from the distance between
   them and the merge context, and **measure** the fall-off with a simulation.
4. **Choose** between merging and rebasing for a given history, and **state** what
   rebasing rewrites and what it consequently costs.
5. **Justify** a branch cadence from the measured probability of a conflict as a
   function of how long a branch waits.
6. **Diagnose** a messy history (merge commits, duplicated work, lost commits)
   and **prescribe** the recovery that preserves provenance.

Git commands and workflows in this lesson are standard and can be checked against
the official documentation. The conflict statistics are **SYNTHETIC**: they come
from a line-overlap model run by the demonstration with chosen parameters, not
from any repository that was measured.

## Prerequisites

- [03-13-06 Git Workflow for Scientific Projects](../../03-scientific-computing/13-testing-profiling-packaging/06-git-workflow.md) —
  `add`, `commit`, `push` and the everyday commands this lesson assumes.
- [22-01-01 Designing Software for Scientific Research](./01-software-design-science.md) —
  why a change reaches further than the file it touches.

## 1. Intuition: a history, not a folder

A version-control repository is a **history of states**, not a copy of a
directory. Each commit is an immutable snapshot of the whole tree, identified by
the hash of its contents and its parents. The hash is a function of the content,
so the same content always produces the same identifier and a changed byte
produces a different one. Everything else in Git is a convenience built on those
two facts: a **branch** is a pointer to one commit that moves as you commit, a
**tag** is a pointer that does not move, and `HEAD` is a pointer to the pointer
you are using.

The practical consequence is that "losing work" almost always means losing the
*name* of a commit, not the commit. Objects stay in the database until they are
unreachable and garbage-collected, and even then `git reflog` holds the recent
names. Teaching this first prevents the most expensive beginner behaviour:
copying a directory "just in case" and then having two divergent analyses.

## 2. Branching as a pointer

Three kinds of movement matter:

| Operation | What moves | What it records |
|---|---|---|
| `git commit` | the current branch pointer | a new snapshot whose parent is the previous one |
| `git branch feature` | nothing; a new pointer is created | a name for an existing commit |
| `git checkout -b feature` | `HEAD` and the new pointer | that subsequent commits belong to the feature |
| `git tag -a v1.0 -m "…"` | nothing; an annotated tag object | a fixed name for a release |
| `git merge`, `git rebase` | pointers, and the graph shape | integration of two lines of work |

Because a pointer is a name for a commit, the same commit can carry many names
and a branch with no unnamed work can be deleted without losing content.

## 3. Merging: the merge base and the conflict geometry

A merge of two branches is a **three-way merge** with three inputs: the two tips
and their **merge base**, the most recent common ancestor. The algorithm applies
the diff from base to each tip; a hunk changed on only one side is taken
automatically, and a hunk changed on **both sides** is a conflict that a human
must resolve.

Whether a conflict occurs therefore depends on whether the two edit **regions**
touch after the diff's context is added. Git's default diff context is three
lines on each side, so two hunks that are closer than roughly six lines become
one overlapping region. The prediction is that the conflict probability depends
on the **gap between edit regions**, not on the size of the file, and that it
saturates only because the edits are short.

## 4. Measured conflict geometry

The demonstration simulates a 800-line file edited by 40 feature branches whose
edit lengths are Poisson-distributed with mean 20 lines, and measures the
probability that a pair of edits conflicts as a function of the separation of
their starting lines. The **SYNTHETIC** results, with 20 000 trials per row and a
three-line context:

| Separation (lines) | Conflict probability |
|---|---|
| 0 | 1.000 |
| 5 | 1.000 |
| 10 | 1.000 |
| 15 | 0.998 |
| 20 | 0.932 |
| 30 | 0.216 |
| 40 | 0.003 |
| 60 | 0.000 |

The risk decays over roughly one edit length: it is near-certain below 15 lines,
about 22 % at 30 lines and effectively zero beyond 40 lines. In the same
simulation, 56 of the 780 branch pairs (7.2 %) have overlapping regions, with
mean lifetimes of $6.9 \pm 7.3$ days (one standard deviation) and
$20.4 \pm 3.5$ lines touched per branch.

Holding the separation fixed at 20 lines and varying only the context shows what
the metric actually depends on:

| Context (lines) | Conflict probability at separation 20 |
|---|---|
| 0 | 0.531 |
| 1 | 0.704 |
| 3 | 0.937 |
| 6 | 0.999 |

Here is the honest difficulty: **the context window is not under most users'
control** in a helpful way. Increasing it finds more conflicts (safer merges,
more human work); decreasing it resolves more automatically and risks
semantically wrong but textually clean merges. What *is* under your control is
the distance between edits, which is a question of how the work is partitioned.

## 5. Merge or rebase?

Both integrate work; they differ in what they preserve.

- **Merge** creates a commit with two parents. History records that two lines of
  work existed and when they met. Non-linear, complete, and safe after pushing.
- **Rebase** replays your commits onto a new base, producing **new** commits with
  new hashes. History becomes linear and easier to read, and the commits that
  recorded how you actually worked are replaced.

Rebase is appropriate for local, unpushed work; it is destructive for shared
branches because everyone who already has the old commits now holds a divergent
history. Merging is the safe default for anything another person may have.

The cost of rebasing is dominated by **how long the branch waited**, because the
number of upstream edits it must replay grows with the wait. In the
demonstration's model — five upstream edits per day, each conflicting with
probability 0.03 — the probability of at least one conflict is

| Wait | Upstream edits | $P(\text{at least one conflict})$ |
|---|---|---|
| 1 day | 5 | 0.141 |
| 3 days | 15 | 0.367 |
| 10 days | 50 | 0.782 |
| 30 days | 150 | 0.990 |

$$P(\text{no conflict}) = (1-p)^{n}, \qquad n = 5W \ \text{edits for a wait of } W \text{ days},$$

with $p = 0.03$ the per-edit conflict probability. The arithmetic for $W = 10$ is
$0.97^{50} = 0.218$, so $P(\ge 1) = 1 - 0.218 = 0.782$.

The conclusion is a cadence, not a tool choice: integrate at least daily and the
conflict probability stays near 10 %; wait a month and it is a near-certainty
regardless of how clever the merge tool is.

## 6. History hygiene for research code

1. **One logical change per commit.** A commit that fixes a bug and reformats a
   file cannot be reverted without losing the fix.
2. **Write messages that explain why.** The diff already says what changed; the
   message is the only place the reason can live.
3. **Never commit data or secrets.** Large binaries bloat the repository
   permanently; data belongs in a data citation, secrets belong nowhere.
4. **Tag releases used in a paper.** Report the tag and the commit hash in the
   paper so a reader can obtain exactly the code that produced the figure.
5. **Keep a linear or a documented history, not an accidental one.** If the
   history is a record of the analysis, say so in the README; a reviewer will ask.

## 7. Worked example: reading the simulation

In the synthetic history, mean branch lifetime is 6.9 days and 7.2 % of branch
pairs overlap. Two actions follow.

1. **Shorten the cadence.** At the model's rate, a 6.9-day wait corresponds to
   about 35 upstream edits, so
   $P(\text{conflict}) = 1 - 0.97^{35} = 0.655$. Merging daily would give
   $1 - 0.97^{5} = 0.141$: a factor of 4.6 in risk for the same total work.
2. **Partition by file, not by person.** Conflict probability is a function of how
   near two edits are in the *file*. Two people working on different modules of a
   well-separated codebase rarely touch the same region, which is why the
   separation column above matters more than the number of developers.

## Assumptions and regime of validity

1. **Line-based merge semantics.** The model assumes edits are contiguous
   regions of a text file, which is what Git's default merge driver does. Binary
   files, `git rerere` reuse and custom merge drivers behave differently.
2. **Poisson edit lengths and uniform positions.** Real edits cluster near
   recently changed code; clustered edits conflict more often than the uniform
   model predicts.
3. **Independence of pairs.** The per-pair probability is treated as independent;
   in reality one conflict often implies nearby ones.
4. **Context of three lines.** The numbers scale with the context; the table is
   reported for the default so the comparison is fixed.
5. **A conflict is textual.** A clean merge can still be wrong: two branches can
   change a formula and its units in textually disjoint places and merge without
   a marker. The model measures merge friction, not semantic correctness.

## The honest summary

Git is a content-addressed snapshot store with movable names; branching is
cheap, merging is a three-way edit against a merge base, and conflicts are a
property of **edit proximity**, not of file size or team size. The synthetic
measurement puts the useful boundary at roughly one edit length: about 93 % of
edit pairs conflict at 20 lines of separation, 22 % at 30 lines, and essentially
none beyond 40 lines. Because conflict risk in a rebase grows as
$(1-p)^{5W}$, the cadence decision dominates every other choice: daily integration
holds the risk near 10 %, while a monthly wait makes a conflict essentially
certain. Rebase locally, merge anything shared, tag what a paper used, and keep
each commit a single explained change.

## Python demonstration

[`code/version_control_git_demo.py`](./code/version_control_git_demo.py) builds a
synthetic branch history with `np.random.default_rng(20261014)` and prints, under
four numbered banners:

1. the history's shape — 275 commits, mean lifetime, lines touched, and the
   fraction of overlapping branch pairs (7.2 %);
2. the conflict probability table versus edit separation;
3. the effect of the merge context at fixed separation;
4. the rebase model, $P(\ge 1\ \text{conflict})$ for waits of 1, 3, 10 and 30
   days.

```bash
cd 22-data-engineering-reproducibility/01-research-software-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python version_control_git_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/02-version-control-git-exercises.md`](./exercises/02-version-control-git-exercises.md)
and
[`exercises/02-version-control-git-solutions.md`](./exercises/02-version-control-git-solutions.md).

## Mastery checkpoint

Without notes: you and a colleague both edit `inversion.py`, a 600-line file.
Your edits start at line 120 and line 300, and each region is about 25 lines.

1. Using the demonstration's separation table, state whether the merge is likely
   to conflict, and what changes if your colleague's file was reformatted first.
2. Explain in one sentence what the merge base is and why it is needed.
3. Your colleague rebased a branch that three people had already pulled. State
   what those three people must now do and why the history diverged.
4. State what a clean merge does **not** establish about the merged code.

## Common pitfalls

1. **Believing a branch is a copy.** It is a pointer; deleting it loses a name,
   not usually content, which is why `git reflog` is a recovery tool.
2. **Rebasing shared history.** After a push that others have fetched, a rebase
   forces everyone to re-synchronise on a rewritten history.
3. **Conflict-avoidance by large files or one writer.** Both reduce conflicts by
   removing the collaboration that the conflicts were a symptom of.
4. **Treating "no conflict" as "no problem".** Textual merges do not check
   semantics: a changed formula and a changed unit can merge cleanly and be wrong.
5. **Long-lived feature branches.** At the model's rates, a 30-day branch has a
   99 % chance of at least one conflict; the cadence, not the tool, is the lever.
6. **Committing data to Git.** A 2 GB binary in history stays in every clone;
   data needs versioning of its own (see
   [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md)).

## Where this is used

- **Reproducible publication** — the tag and commit hash are the identifier a
  reader needs: see [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Collaborative analysis** — the cadence recommendation applies to notebooks
  and scripts as much as to packages.
- **Software citation** — a versioned release is what `CITATION.cff` and a
  Zenodo archive point at: see [22-01-05](./05-licensing-and-citation.md).
- **Debugging a numerical discrepancy** — `git bisect` finds the commit that
  introduced it, which requires small, single-purpose commits.

## Related lessons

- [22-01-01 Designing Software for Scientific Research](./01-software-design-science.md) —
  why a change is rarely local, which is what makes history valuable.
- [22-01-03 Code Review and Collaborative Development](./03-code-review.md) —
  the review that happens before a merge.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the same snapshot idea for data, where the sizes need storage of a different kind.
- [03-13-06 Git Workflow for Scientific Projects](../../03-scientific-computing/13-testing-profiling-packaging/06-git-workflow.md) —
  the introductory workflow this lesson extends.

## Self-assessment checklist

- [ ] I can explain commits, branches, tags and `HEAD` as pointers and objects.
- [ ] I can describe a three-way merge using the merge base.
- [ ] I can state why conflict risk depends on edit proximity.
- [ ] I can compute a conflict probability for a given wait from $(1-p)^{n}$.
- [ ] I can choose merge or rebase and state the consequence of each.
- [ ] I can name what a clean merge does not establish.
