# Solutions — 03-13-06 Git for Scientific Collaboration: Branching, Review, History Hygiene

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; derived values are shown with the arithmetic
> that produced them.

---

## ★1 — Content addressing and what it pins

**(a)** The identifier is a function of the bytes, so identical content always
yields the same hash — as measured for the two identical strings — and a single
changed byte yields a different one. That means citing a hash names a *content*
rather than a location, so the citation survives a rename, a move between hosts,
and any change to the default branch.

**(b)** The number that matters most is **`tracked files with a large-binary
extension: 0`**. File count and byte total are descriptive; zero binaries is the
property that makes the repository clonable in seconds by every student and CI
runner and mergeable by git at all. A curriculum about geophysics could easily
carry a 200 MB seismic volume, and its presence would be invisible in the file
count while dominating the clone.

**(c)** Pins: the exact content of the tracked tree at that commit, including
every script, configuration file and test. Leaves unpinned: the interpreter and
its packages, the BLAS build, the platform, the thread count, and the data — the
five items measured in the environments lesson.

---

## ★2 — What belongs in git

**(a)** Two questions, in order: **can git merge a change to it?** (a text file
with a defined syntax, usually yes) and **would a human want to read the diff?**
If both answers are yes, it belongs in git; otherwise it belongs in an archive,
and the repository holds the script that fetched it plus a record of which
version it fetched.

**(b)** The negation re-includes one small file inside a directory that is
otherwise ignored, so a 3 kB purpose-built fixture can be committed while the
3 GB dataset it was cut from stays out. For it to be honest, the repository must
contain, beside the file, a README stating **where the data came from, which
version or date, how it was subsetted, and what licence applies** — otherwise the
next reader cannot tell a synthetic fixture from a real extract, and cannot
regenerate the excerpt when the upstream dataset is revised.

**(c)** A script that decides "ignored" from the exit status inverts every
negation, because `check-ignore` exits 0 for a negated match as well. The correct
predicate is to parse the printed pattern and test for the leading `!`:

```python
out = run(["git", "check-ignore", "-v", "--no-index", path]).stdout.strip()
ignored = bool(out) and not out.split(":", 2)[2].split("\t")[0].startswith("!")
```

---

## ★3 — Git or archive

| file | verdict | why |
|---|---|---|
| 4 kB Python fetch script | git | text, diffable, and the reviewer wants to read it |
| 400 MB miniSEED day-file | archive | binary, unmergeable, and not part of the software's identity |
| 12 MB CSV of station coordinates | git | text, diffable, and small enough that the history cost is acceptable |
| notebook, outputs cleared | git | the JSON diff is meaningful when the cell outputs are stripped |
| notebook with a 60 MB embedded raster | archive the figure; keep the notebook with a link | the binary payload dominates and the diff becomes a base64 blob |

The last row is the case people get wrong in both directions: deleting the plot
loses information, and committing it makes every subsequent diff unreadable. The
correct arrangement is the notebook plus the script that regenerates the figure,
with the figure itself archived and referenced by DOI.

---

## ★4 — `git archive` as a clean checkout

**(a)** It reconstructs the committed tree directly from the object database,
without consulting the index, the working directory or `.gitignore`. Its input is
a commit, and its output is the bytes of that commit's tree, so two machines
extracting the same commit get identical file sets and identical content.

**(b)** It enables the honest form of "it works on my machine": extract the
archive elsewhere and run the gate. The defect it detects — and that no other
review does — is a **test that depends on an untracked file**. Locally the file is
present and the suite is green; in a fresh clone it is absent and the suite fails.
Review cannot see it, because the untracked file never appears in the diff, and
the author has no reason to mention it.

**(c)** Uses: it identifies the exact tree (append it to a reproducibility
statement), and it lets you compare two trees cheaply to detect which of them
changed. What it does not prove: that the code is correct, that the dependencies
resolve, or that the tests pass — those require running the extraction, which is
what the gate does next.

---

## ★5 — `.gitignore` for a project

```gitignore
# --- data: never commit raw data; keep small fixtures only ---
data/*
!data/small-*.csv
*.nc
*.mseed

# --- results: figures ARE committed, they are the output of the work ---
!results/

# --- Python ---
__pycache__/
*.py[cod]
.venv/

# --- scratch ---
scratch/
```

Verification, one command per rule:

```bash
git check-ignore -v data/raw/line1.mseed    # expect *.mseed
git check-ignore -v data/small-demo.csv     # expect the ! negation
git check-ignore -v results/fig1.pdf        # expect NO output (committed)
git check-ignore -v __pycache__/x.pyc       # expect __pycache__/
git check-ignore -v scratch/notes.txt       # expect scratch/
```

Two subtleties. `data/*` with `!data/small-*.csv` is deliberate rather than
`data/`: ignoring the *contents* after a negation is the pattern that works
reliably, because git does not descend into an excluded directory and therefore
never sees a negation for a file inside an ignored *directory*. And the
`results/` line is a no-op if `results/` contains no ignored files — it documents
the intent, which is why the verification for it expects no output.

---

## ★6 — Commit messages

**(a)** `fix bug` — names neither what was wrong nor where. Rewritten: *"Fix sign
of the free-air correction: observed gravity decreases with elevation, so the
term is added. Previous version was 61.72 mGal low at 100 m of relief; existing
test values updated against the conventional 0.3086 mGal/m gradient."*

**(b)** `updates for paper` — bundles unrelated changes under a deadline label.
Rewritten as the two or three commits it really is, for example: *"Tighten prism
kernel tolerance to 1e-10 relative after measuring amplification 3.2e5"* and
*"Add figure-generation script for submission version of Fig. 3"*. The deadline
belongs in the pull-request description, not in the history.

**(c)** `reformat everything + fix the sign...` — hides a one-line logic change
inside a 240-file diff. Split into: *"Reformat with ruff format 0.x; no semantic
change"* followed by *"Fix sign of the free-air correction (see message of the
preceding revert)"*. The reviewer then reads one small diff, and CI can verify the
first commit is whitespace-only by comparing `git diff -w` with the full diff.

---

## ★7 — Five people, an old `dev`, and no tags

**(a)** The figure cannot be reproduced from any named revision: `dev` has moved
three months past the state that produced it, and there is no immutable
identifier for the state the paper used.

**(b)** Minimal fix, in four steps and no reorganisation:

1. Find the commit `dev` was at when the figures were produced (from the
   colleague's local reflog, a CI log, or the date in the figure files) and tag
   it retrospectively.
2. Tag the current `dev` as a prerelease if it matters.
3. Adopt the convention that every paper cites a tag, and add a `CITATION.cff`
   naming it.
4. Shorten the `dev` branch's lifetime by merging it to `main` weekly, so a
   three-month divergence cannot recur.

**(c)** The tag does not fix the other two obligations: the **environment** (the
pinned package set and interpreter with which the figures were produced) and the
**data** (the catalogue version and, ideally, a payload digest). Tagging the code
makes one of the three links checkable; the figure is still not reproducible
without the other two.

---

## ★8 — Reproducing a tag without disturbing `main`

**(a)** `git worktree add` (a second working directory sharing the object
database) and `git stash` (shelving uncommitted changes). The **worktree** is
what this module's demo measures — it prints the attached worktrees with
`git worktree list --porcelain`. Stashing is the mechanism the question's third
part shows to be the risky one.

**(b)**

```bash
git worktree add ../paper-v0.9.2 v0.9.2
cd ../paper-v0.9.2 && .venv/bin/python scripts/make_fig3.py
git worktree remove ../paper-v0.9.2
```

**(c)** Two failure modes of the stash route: **the stash may not apply cleanly**
after the checkout, because the files it contains were modified at `main` and the
tag's version differs — producing an unresolvable three-way merge in a working
tree whose state you have already destroyed; and **`git stash pop` leaves a
dirty tree that is neither revision**, so any test you run afterwards is testing a
third thing that exists nowhere in history. A detached HEAD checkout has the same
hazard in a different form: committing anything while detached creates a commit
reachable from no branch, which is easy to lose. The worktree avoids both by
keeping `main`'s working directory untouched, on its own branch, with its own
index.

---

## ★9 — Hygiene versus a clean history

**(a)** History hygiene wants a history that is *usable*: one idea per commit,
messages that state why, and no trace of the debugging dead ends that produced the
change. A clean history wants a history that *looks tidy*: no merge commits, no
reverted commits, a linear sequence of green commits. The two agree on most
practices and conflict sharply on one, because the second is willing to destroy
the record of what actually happened — including the reverted attempt that
explains why the current approach exists — in exchange for a diagram.

**(b)** Safe: **amending or rebasing commits that have never been pushed**, since
no one else has a copy and no shared state is invalidated. Never safe:
**force-pushing a rewritten history to a shared branch**, because anyone who has
already pulled has commits whose parents no longer exist; their next pull becomes
an unresolvable divergence, and their work — and the review trail — is the price.
The rule is not about tidiness but about who else holds a copy.

**(c)** Procedure: ask for the diff to be split, and show that it can be. Run
`git diff -w` and compare it with the full diff; if the logic change is present in
`git diff -w` and everything else vanishes, then the formatting is provably
semantic-free and the reviewer needs to read only the `-w` output. Requesting the
split is reasonable rather than pedantic because the author already has the two
changes as separate edits in their editor history — the cost is a few minutes, and
the alternative is a reviewer who cannot find a sign error in 3000 lines, which
is exactly the defect class this module's coverage lesson plants in a one-line
function.
