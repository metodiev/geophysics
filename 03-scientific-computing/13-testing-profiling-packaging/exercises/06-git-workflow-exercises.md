# Exercises — 03-13-06 Git for Scientific Collaboration: Branching, Review, History Hygiene

Attempt these **closed-book** before opening the
[solutions](./06-git-workflow-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/git_workflow_demo.py`](../code/git_workflow_demo.py); run it and report
actual output. Every command in it is read-only:

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/git_workflow_demo.py
```

The lesson is [`../06-git-workflow.md`](../06-git-workflow.md).

---

## ★ Foundational

**★1. [demo]** The demo's content-addressing section reports:

```
  hash('g = 6.67430e-11' + newline)     = 6620333cff4538c7228978bcf2e2b62e5019724e
  hash(the very same string)            = 6620333cff4538c7228978bcf2e2b62e5019724e
  hash(the same text, one more newline) = 2e12dadadb23a96c6e6eb1e5d6cb8a23c822a874
```

(a) Explain in two sentences why this makes a commit hash a valid citation.
(b) The demo also reports `tracked files: 1012` and `tracked bytes: 15,156,186`.
State the one number in the tracked-content table that matters most for
reproducibility, and why.
(c) State one thing a commit hash pins and one it leaves unpinned.

**★2. [demo]** The `.gitignore` probes report:

```
  IGNORED   data/station_gravity.csv      by .gitignore:30
  IGNORED   waveforms/2019-07-06.mseed    by .gitignore:31
  IGNORED   grids/bouguer.tif             by .gitignore:37
  re-included  examples/small-gravity.csv by .gitignore:42 `!examples/**/small-*.csv`
```

(a) State the decision rule for whether a file belongs in git or in a data
archive, in two questions.
(b) Explain what the `!examples/**/small-*.csv` rule accomplishes and what the
repository must contain alongside the re-included file for it to be honest.
(c) `git check-ignore` exits 0 for the re-included path too. State the consequence
for a wrapper script, and the correct predicate.

**★3.** Classify each as "belongs in git" or "belongs in an archive", with one
clause of justification: (a) a 4 kB Python fetch script; (b) a 400 MB miniSEED
day-file; (c) a 12 MB CSV of station coordinates; (d) a Jupyter notebook with
outputs cleared; (e) the same notebook with a 60 MB embedded raster plot.

---

## ★★ Applied

**★★4. [demo]** The archive comparison reports:

```
  files in `git ls-files`             : 1012
  regular files in `git archive HEAD` : 1012
  sets identical: True
  sha256(git archive HEAD) = 7377c79a22150d6e759fc8f991ffc5f0186a00be...
```

(a) Explain what `git archive` reconstructs and why its content is independent of
the working directory.
(b) State the practical check this enables, and the class of defect it detects
that no other review does.
(c) The demo prints the sha256 of the tar. State one use for that digest and one
thing it does not prove.

**★★5.** Write the `.gitignore` rules for a project with: a `data/` directory that
must never be committed, except a 3 kB `data/small-*.csv` teaching fixture; a
`results/` directory of figures that should be committed; `*.nc` and `*.mseed`
excluded everywhere; `__pycache__` and `.venv` excluded; and a `scratch/`
directory excluded. Then state how you would verify each of the five rules with
one command.

**★★6.** Critique these commit messages and rewrite each:

(a) `fix bug`
(b) `updates for paper`
(c) `reformat everything + fix the sign in the free-air correction`

---

## ★★★ Research-oriented

**★★★7.** A group of five has a repository with `main`, a `dev` branch that is
three months old, and no tags. Their last paper's figures were made from `dev`.

(a) State the reproducibility problem in one sentence.
(b) Propose the minimal set of changes to their workflow that fixes it, without
reorganising their work.
(c) State what the tag alone does not fix, referring to the other two obligations
named in the module.

**★★★8.** You must reproduce a figure from a paper whose code is at tag `v0.9.2`
while continuing to develop on `main`.

(a) State the two git mechanisms that make this possible without disturbing your
work, and which one this module's demo measures.
(b) Write the four commands, in order.
(c) State what would go wrong if you instead stashed your work, checked out the
tag, ran it, and popped the stash — two specific failure modes.

**★★★9.** The lesson says history hygiene is not the same as a clean history.

(a) Reconcile those two ideas: what does each one want?
(b) State the one history-rewriting operation that is safe, and the one that is
never safe on a shared branch, with the reason for each.
(c) A reviewer receives a 3000-line diff containing a formatting sweep and one
logic change. State the review procedure that makes the logic change visible, and
why asking for a split is the right request rather than an unreasonable one.
