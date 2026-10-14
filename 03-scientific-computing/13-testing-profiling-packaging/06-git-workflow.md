---
id: 03-13-06
title: "Git for Scientific Collaboration: Branching, Review, History Hygiene"
level: intermediate
prereqs: ["03-13-01"]
estimated_minutes: 95
tags: [git, version-control, collaboration, reproducibility, review, gitignore, data]
---

# Git for Scientific Collaboration: Branching, Review, History Hygiene

Git is usually taught as a set of commands for saving work. For science it is
better understood as a **reproducibility instrument**: it is the thing that makes
"the code that produced Figure 3" a checkable statement rather than a memory.
That reframing changes which features matter. Content addressing matters;
branch naming conventions matter much less. What belongs in the repository and
what belongs in an archive matters enormously; a rebase-versus-merge argument
usually does not.

This lesson measures the repository you are reading, using only read-only git
commands. Nothing is committed, staged, stashed or written, deliberately: a
lesson about history hygiene should not rewrite anybody's history.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a commit hash is a citation, in terms of content addressing,
   and demonstrate it with `git hash-object`.
2. **Audit** what a repository contains, and decide whether each category of file
   belongs in it or in an archive.
3. **Write** `.gitignore` rules that exclude large data, including a negation that
   re-includes a small teaching fixture, and verify them with `git check-ignore`.
4. **Demonstrate** that a fresh clone equals the committed tree, so that "verify
   the build at a clean checkout" is a meaningful instruction.
5. **Choose** a branching and review workflow appropriate to a small scientific
   team, and say what each convention buys.
6. **Use** `git worktree` to test one revision while editing another, and explain
   why it needs no clone.

## Prerequisites

- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — CI runs the tests on a clean checkout, which is this lesson's central object.

## 1. What is actually in a repository

Measured with `git ls-files` on this repository:

| Quantity | Value |
|---|---|
| tracked files | 1012 |
| tracked bytes | 15,156,186 (15.16 MB) |
| most common extensions | `.md` (768), `.py` (240), `.yml` (1), `.txt` (1), `.tsv` (1) |
| largest tracked file | `CURRICULUM.md`, 217,590 B |
| text files that decode as UTF-8 | 1012 |
| total text lines | 312,271 |
| tracked files with a large-binary extension | **0** |

Fifteen megabytes and a million lines of prose is a healthy repository. The
number that matters most in that table is the last one: **zero**. A curriculum
about geophysics could easily contain a 200 MB seismic volume, and the reasons it
does not are worth stating precisely, because they are not about disk quotas.

Git stores a complete copy of every version of a file. A 200 MB binary committed
once is 200 MB in every clone; committed in ten revisions it is roughly 2 GB, and
it is 2 GB for every student, every collaborator and every CI runner, forever,
since history is append-only in practice. Worse, a binary diff is meaningless:
git cannot merge two versions of a seismic volume, so a conflict on a data file
is unresolvable and the only remedy is to pick one. And a dataset is not part of
the software's identity: the code that reads a catalogue is the same code whether
the catalogue is the 2020 or the 2024 release, and coupling them makes both
harder to version.

The correct home for a dataset is an archive that mints a DOI: Zenodo, figshare,
PANGAEA for marine and polar data, or the discipline-specific services for
seismic, gravity and geomagnetic data listed in this curriculum's reference
material. A DOI is citable, versioned, permanently hosted and has a checksum.
A commit in a git repository is none of those things for a hundred-gigabyte file,
and all of them for a 4 kB script.

### 1.1 The rule, stated as a decision procedure

For each file, ask two questions in order:

1. **Can git merge a change to it?** If it is a text file with a defined syntax,
   probably yes. If it is a binary, no — and that alone is not disqualifying, but
   it is a strong signal.
2. **Would a person want to read the diff?** If a change to the file is
   reviewable, it belongs in git. If not, the file belongs in an archive, and the
   repository should contain the *script that fetched it* and a record of which
   version it fetched.

Under this rule a 2 MB CSV of instrument metadata belongs in git, a 2 GB waveform
does not, a Jupyter notebook with cleared outputs belongs in git, and a
`.tif` raster never does.

## 2. Content addressing: why a hash is a citation

`git hash-object` computes the identifier of a blob from its bytes. Measured:

```
hash('g = 6.67430e-11' + newline)     = 6620333cff4538c7228978bcf2e2b62e5019724e
hash(the very same string)            = 6620333cff4538c7228978bcf2e2b62e5019724e
hash(the same text, one more newline) = 2e12dadadb23a96c6e6eb1e5d6cb8a23c822a874
```

Same content, same identifier; one extra byte, a completely different one. That
property is what makes a commit hash a valid citation: it names a *content*, not
a location, so it cannot be invalidated by a rename, a move between hosts, or a
change to the default branch.

The measured state of this repository:

```
  HEAD            = 494c671 (494c6712f94b6ac8355ca64f08f7e7532c5239d6)
  branch          = main
  commits from HEAD = 47
  Co-authored-by trailer on HEAD: Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

Two practical consequences.

- **Cite the full hash, not the branch.** `main` is a moving target; the hash is
  not. A methods section that says "main as of March" is not reproducible, and a
  DOI for a tagged release is the durable form of the same idea.
- **Trailers are machine-readable metadata.** `Co-authored-by`, `Reviewed-by`,
  `Fixes:` and `Signed-off-by` are parsed by git and by hosting platforms. They
  are how authorship of a pair-programmed or agent-assisted commit is recorded
  honestly, and how a change is linked back to an issue.

## 3. What is deliberately excluded

Measured with `git check-ignore -v`, which names the rule responsible:

| probe path | verdict | rule |
|---|---|---|
| `data/station_gravity.csv` | ignored | `.gitignore:30` |
| `waveforms/2019-07-06.mseed` | ignored | `.gitignore:31` |
| `field/line_a.sac` | ignored | `.gitignore:32` |
| `grids/bouguer.tif` | ignored | `.gitignore:37` |
| `model/result.nc` | ignored | `.gitignore:35` |
| `logs/run.log` | ignored | `.gitignore:45` |
| `__pycache__/module.cpython-314.pyc` | ignored | `.gitignore:2` |
| `examples/small-gravity.csv` | **re-included** | `.gitignore:42` |
| `README.md` | committed | no rule matches |

The pattern list is a taxonomy of scientific file types rather than a list of
annoyances: `data/`, `*.mseed`, `*.sac`, `*.segy`, `*.sgy`, `*.nc`, `*.grd`,
`*.tif`, `*.tiff`, `*.h5`, `*.hdf5`, `*.zarr/`. Each is a format that is large,
binary, or both.

The interesting row is the eighth. The rule

```
!examples/**/small-*.csv
```

re-includes a small, purpose-built teaching fixture inside a directory that is
otherwise ignored. This is how you commit a 3 kB demonstration file without
committing the 3 GB dataset it was cut from — with the provenance recorded in a
README beside it, which is what makes the file honest rather than arbitrary.

### 3.1 A detail that causes real bugs

`git check-ignore` exits 0 for a path that matches a negated pattern too, and
prints the negating pattern with a leading `!`. A wrapper script that decides
"ignored" from the exit status alone therefore gets the negation precisely
backwards — the same class of subtlety as the venv predicate in
[03-13-05](./05-packaging.md). The verdict in the table above was derived from
the leading `!`, not from the exit code, and the difference was noticed because
the output was read rather than assumed.

## 4. A clone is exactly the commit

The strongest reproducibility statement a repository can make is that the code in
it is the code in the commit, with nothing else. Measured:

```
  files in `git ls-files`             : 1012
  regular files in `git archive HEAD` : 1012
  sets identical: True
  size of the whole committed tree as a tar: 15.99 MB
  sha256(git archive HEAD) = 7377c79a22150d6e759fc8f991ffc5f0186a00be...
```

`git archive` reconstructs the tree straight from the object database. Its
content does not depend on the working directory, on untracked files, or on
anything in `.gitignore`. **The archive is the clean checkout**, and its hash is
a checkable identity for it. Two consequences:

- **"It works on my machine" is testable.** Extract the archive somewhere else
  and run the gate. If it fails, an untracked file was load-bearing — the most
  common form of the problem, and invisible in every other kind of review.
- **A build can be verified without a second clone.** No network, no
  credentials, no second working directory.

### 4.1 A gate reads `git status`

```
  entries in `git status --porcelain`: 17
     M tools/check_all.py
     M tools/verified_links.tsv
    ?? 03-scientific-computing/13-testing-profiling-packaging/
  staged changes   : 0
  unstaged changes : 3
  untracked paths  : 14
  untracked scratch-looking files: 0
```

A check that a change contains "only its own module's files" is reading exactly
this list. Two habits make it pass without effort: never leave scratch files in
the tree, and never edit a file outside your own task. Both are cheap while you
are working and expensive to reconstruct afterwards — an untracked temporary that
happens to be imported by a test is a defect that only appears on somebody else's
machine.

## 5. Branching and review for a small scientific team

The workflows worth knowing are few, and the choice is driven by team size and
release cadence, not by fashion.

| workflow | shape | suits |
|---|---|---|
| trunk-based | short-lived branches, merged to `main` within a day | 1–10 people, continuous CI |
| feature branch + PR | one branch per change, reviewed, merged | the default for a group with reviewers |
| release tags | `v1.2.0` on `main`, artefacts attached | anything cited in a paper |
| long-lived branches | `dev`, `stable`, `release-2.x` | libraries with external users on old versions |

For a research group the middle two rows carry almost all the value, and the
review is the part that pays. Two review conventions are worth adopting
explicitly, because they prevent the two most common forms of scientific commit
rot:

- **Separate formatting from logic.** A formatter that rewrites thirty lines
  hides a one-line change in the same diff. One commit for the format, one for
  the logic, and the logic diff is reviewable in seconds.
- **One idea per commit.** A commit that adds a function, updates the README and
  fixes an unrelated typo cannot be reverted selectively. This is not aesthetic:
  the ability to revert one change without losing the others is the property that
  makes a history usable during a debugging session.

A commit message that names *why* is the other half. "Fix sign in free-air
correction: observed gravity decreases with elevation, so the correction is
added; previous version was 61.72 mGal low at 100 m" is a message that saves
somebody an afternoon. "fix bug" is a message that costs somebody one.

### 5.1 Tags, releases and citation

A tag is a name for a commit. A release is a tag plus artefacts. For a
scientific code base:

```bash
git tag -a v1.2.0 -m "Release 1.2.0: prism kernel, GRS80 normal gravity"
git push origin v1.2.0
```

Then attach the DOI of that release in the repository's `CITATION.cff`, and cite
the release — not the repository — in the paper. A `CITATION.cff` at the
repository root is machine-readable and is what hosting platforms turn into a
"Cite this repository" button, which is a small usability win with a
surprisingly large effect on whether people cite the software correctly.

## 6. `git worktree`: two revisions, one object database

Measured state:

```
  worktree /Users/miroslav/Documents/workspace/geophysics
  HEAD 494c6712f94b6ac8355ca64f08f7e7532c5239d6
  branch refs/heads/main
```

`git worktree add ../repo-v2 -b feature` creates a second *working directory*
backed by the same object database, checked out on a different branch. Nothing is
downloaded twice, no separate `.git` is created, and both directories share the
history. The uses that matter in practice:

- **Run a long validation on the previous revision while editing the current
  one.** A test suite that takes an hour no longer blocks you.
- **Reproduce a published result** without disturbing your working tree: check
  out the tag in a worktree, run it, remove the worktree.
- **Compare two branches side by side** in two editor windows, with no stashing
  and no risk of losing uncommitted work.

`git worktree remove <path>` cleans up. The important property is that a worktree
is a *view* of the same history rather than a copy of the repository: there is
exactly one object database, so there is nothing to keep in sync.

## 7. Python demonstration

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/git_workflow_demo.py
```

The script runs `ls-files`, `check-ignore -v`, `hash-object`, `archive`,
`status` and `worktree list --porcelain`, and prints the tables above. Every
command is read-only; it commits nothing, stages nothing and creates no worktree.

Expected values in this environment include `tracked files: 1012`,
`tracked files with a large-binary extension: 0`, and
`sets identical: True` for the `ls-files`/`archive` comparison — the three
numbers that together say "the repository contains exactly what it claims, and
none of it is data".

### 7.1 The clean-checkout check in CI

Described, not run here; this repository has no workflow files.

```yaml
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0            # full history, so tags are visible
      - run: python -m pytest -q
      - run: git status --porcelain
```

`actions/checkout` performs a genuine clone at the specified commit, so the job
starts from the same state as `git archive HEAD`. A test that passes locally but
fails there is almost always a dependency on an untracked file, a different
interpreter, or an environment variable set in somebody's shell profile — three
diagnoses that the checkout itself makes possible. See the
[GitHub Actions documentation](https://docs.github.com/en/actions) and
[workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).

## 8. Assumptions and limits

- **Git is not a data management system.** Large-file extensions exist and are
  sometimes the right answer, but they move the problem rather than solving it:
  the data is still not citable, not archived, and not preserved beyond the host.
- **A commit hash pins the code and nothing else.** The environment, the data and
  the random seed are separate obligations; see
  [03-13-08](./08-reproducible-environment.md).
- **History hygiene is not the same as a clean history.** Rewriting history to
  look tidy destroys the record of what actually happened, which is the thing a
  reviewer needs. Amend before pushing; never rewrite published history.
- **Review is human and fallible.** A reviewer who reads a 3000-line diff will
  miss the sign error; that is an argument for small diffs and automated checks,
  not for more reviewers.
- **Git cannot verify science.** It records what changed, by whom and when. It
  has no opinion about whether the change is correct.

## 9. Common mistakes

1. Committing data because a "quick test" needed it, with no path to remove it
   from history later.
2. Reading `git check-ignore`'s exit status instead of its printed pattern, and
   so inverting every negation.
3. Mixing a formatting sweep with a logic change in one commit.
4. Committing `__pycache__`, `.DS_Store`, editor directories or `.venv`. The
   repository already ignores all four; a stray commit means an ignore rule is
   missing or was overridden with `-f`.
5. Writing "fixed bug" or "updates" as a commit message.
6. Citing a branch or a repository URL instead of a tag or hash.
7. Having a test depend on a file that is not tracked, so it passes locally and
   fails for everybody else.
8. Force-pushing to a shared branch. It is unrecoverable for anyone who has
   already pulled, and it destroys the audit trail a reviewer needs.
9. Using `git worktree` and then copying the repository anyway "to be safe",
   recreating the divergence the worktree exists to prevent.

## 10. Real-world applications

- **A published result.** The paper cites `10.5281/zenodo.XXXXXXX`, the archived
  code at the release commit; the repository's `CITATION.cff` names that DOI; the
  data is at its own DOI in an archive; the repository contains the script that
  fetched the data and the version it fetched. Four links, each checkable.
- **A group code base.** Trunk-based development, one review per change, a
  release tag per paper. Boring, and it is what makes a five-year-old figure
  reproducible.
- **A student project.** Even single-author work benefits from one idea per
  commit and messages that state why: the person who needs to understand the
  change six months later is the author.
- **A teaching repository.** Running the quality gate against `git archive HEAD`
  is the cheapest possible check that the lessons a student receives are the
  lessons that were reviewed — this repository's own gate is designed to be run
  exactly that way.

## 11. Further reading

- **Chacon, S. & Straub, B. *Pro Git* (2nd ed.). Apress, free online.** Level:
  beginner to advanced. Chapters 7 (tools, including `archive` and `hash-object`)
  and 10 (internals, including content addressing) are the two that this lesson
  leans on.
- **Git documentation: `git worktree`, `git check-ignore`, `git archive`.**
  Level: reference. `check-ignore -v` is the one worth reading carefully given
  the negation trap of Section 3.1.
- **GitHub Actions documentation.** <https://docs.github.com/en/actions> and
  [workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
  Level: reference. Not executed here; the lesson claims nothing about a run.
- **Wilkinson, M. D. et al. (2016). The FAIR Guiding Principles for scientific
  data management and stewardship. *Scientific Data*, 3, 160018.** Level:
  intermediate. The formal statement of why data belongs in an archive and code
  belongs in a repository.
- **The Turing Way — Guide for Reproducible Research.** Level: intermediate.
  Practical, opinionated and short, on version control for research teams.
- **GitHub, "About CITATION files".** Level: reference. The `CITATION.cff`
  format of Section 5.1.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [03-13-05 Packaging and Distributing a Python Library](./05-packaging.md) —
  what a release tag actually ships.
- [03-13-08 Reproducible Environments](./08-reproducible-environment.md) — the
  half of reproducibility that git cannot pin.
- [03-13-04 Code Quality](./04-code-quality.md) — the automated half of code
  review, which lets the human half talk about physics.
- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — the suite a clean checkout runs.
- [00-03-03 The Quality Gate](../../00-orientation/03-how-to-use-this-repo/03-quality-gate.md)
  — this repository's own gate, and how it is meant to be run.

## 13. Self-assessment checklist

- [ ] I can explain content addressing and why it makes a hash citable. (§2)
- [ ] I can audit a repository's contents and decide, per file, whether it
      belongs in git or in an archive. (§1.1)
- [ ] I can write a `.gitignore` negation and verify it with `git check-ignore`,
      including reading the printed pattern rather than the exit code. (§3)
- [ ] I can demonstrate that a clone equals the committed tree. (§4)
- [ ] I can choose a branching workflow for a five-person group and defend it.
      (§5)
- [ ] I can name the two commit conventions that prevent the most review waste.
      (§5)
- [ ] I can describe what a worktree is and one task it makes possible. (§6)
- [ ] I can state what git pins and what it leaves unpinned. (§8)
