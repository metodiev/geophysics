---
id: 00-03-03
title: "Running the Link, Formula and Duplication Checks"
level: intermediate
prereqs: ["00-03-01"]
estimated_minutes: 45
tags: [quality-gate, tooling, testing, repository]
---

# Running the Link, Formula and Duplication Checks

## Learning objectives

- Run the repository's quality gate and interpret its output, including the exit
  status, without reading the tool's source.
- State precisely what each of the four checks verifies, and how a failure for
  each is repaired.
- Explain what the gate deliberately does **not** check, and what you must
  therefore verify yourself.
- Use `build_index.py` and `verify_links.py` for their distinct jobs: coverage
  reporting and external-URL auditing.

## Prerequisites

[Setting Up the Python Environment and Tooling](./02-environment-setup.md).
Nothing needs to be installed: the gate uses the Python standard library only,
which is the point of the design.

## 1. What the gate is for

A curriculum of over a thousand planned files assembled in batches accumulates
exactly four kinds of damage:

1. **Metadata drift** — a file's `id`, `title` or `level` no longer matches the
   plan, so coverage reports and prerequisite references become wrong.
2. **Link rot** — a relative link points at a path that no longer exists, or
   never existed and was not in the plan.
3. **Broken formulae** — an unbalanced inline delimiter or an unclosed display
   block, which renders as visible markup rather than mathematics.
4. **Collisions** — two lessons claiming the same id or the same title, which
   makes cross-references ambiguous.

The gate is four independent checks, one per failure mode, in
[`tools/check_all.py`](../../tools/check_all.py). It is intentionally small and
dependency-free so that it can run anywhere, including in continuous
integration, on a bare interpreter.

## 2. Running it

```bash
python3 tools/check_all.py            # full report
python3 tools/check_all.py --quiet    # only failures
echo $?                               # 0 = pass, 1 = fail
```

The output begins with the planned scale, then one block per check:

```text
Geophysics curriculum quality gate
  plan: 27 folders, 216 modules, 1146 lessons

[..] structure & frontmatter
  lessons on disk: 10 / 1146 planned
      ok
[..] relative links
  relative links checked: 1735 (1602 pending, planned but not yet written)
      ok
[..] LaTeX delimiters
  files scanned for formulas: 19
      ok
[..] duplicate identifiers
  distinct lesson ids: 10
      ok

RESULT: PASS
```

The counts are expected to grow as lessons are written; the `plan: ... 1146
lessons` figure is the size of the whole planned curriculum, not a target for a
single batch. **Only `FAIL` lines matter.**

## 3. Check 1 — structure and frontmatter

**What it does.** For every Markdown file whose name begins with two digits and a
hyphen (`NN-...md`, excluding `README.md`), it parses the frontmatter block and
compares three fields against
[`tools/curriculum_plan.py`](../../tools/curriculum_plan.py): `id`, `title` and
`level` must match the plan **character for character**. It also fails if the
file is not declared in the plan at all.

**The parser is deliberately strict.** It accepts only a small subset of YAML —
bare scalars, quoted scalars, integers, booleans, inline lists such as
`[a, b]`, and block lists. It rejects:

- a file that does not begin with `---`;
- frontmatter that is never closed with `---`;
- a line inside the block that is not a `key: value` pair;
- a duplicate key;
- a missing required key (`id`, `title`, `level`, `prereqs`, `tags`);
- an unknown key.

**Typical failures and repairs.**

| Message | Cause | Repair |
|---|---|---|
| `not declared in tools/curriculum_plan.py` | Lesson file exists but no plan entry | Add the lesson tuple to the plan, then re-run |
| `frontmatter id '...' != planned '...'` | Typo or stale id | Fix the frontmatter, or the plan if the plan is wrong |
| `frontmatter title '...' != planned '...'` | Title edited in one place only | Make the two identical, including punctuation |
| `frontmatter level '...' != planned '...'` | Level changed in one place only | Make the two identical |
| `missing required frontmatter key 'tags'` | Field omitted | Add the field |
| `unknown frontmatter key 'difficulty'` | Invented key | Use `level`, or one of the documented optional keys |
| `file does not begin with a '---' frontmatter delimiter` | Missing frontmatter | Add the block |

This check is why titles containing a colon must be quoted in frontmatter: a
colon inside an unquoted scalar is not a parser rule the repository supports.

## 4. Check 2 — relative links

**What it does.** It matches every Markdown link — a bracketed label followed by
a parenthesised target — skips external targets (those beginning with the `http`
or `https` scheme), `mailto:` and pure-fragment (`#...`) targets, and resolves the
rest relative to the directory of the file containing them. (Because the matcher
does not understand code spans, writing a literal link pattern inside backticks
will still be treated as a link.) A target is accepted if either:

- the resolved path **exists** on disk; or
- the resolved path is a repository-relative path **declared in the plan**, in
  which case it is counted as *pending* — planned but not yet written.

Anything else is a failure. Links beginning with `/` are rejected immediately as
**absolute path links**, because they are machine-specific and break for every
other reader.

**Why "pending" exists.** The curriculum is written in batches. A lesson may
legitimately reference a lesson that is planned and not yet written. Distinguishing
*pending* from *broken* keeps the gate useful during construction without letting
genuinely wrong paths through.

**Typical failures and repairs.**

| Message | Cause | Repair |
|---|---|---|
| `broken relative link -> ../../06-seismology/README.md` | Wrong depth or typo in the path | Count the directory levels and correct the path |
| `absolute path link -> /Users/me/...` | Machine-specific absolute path | Rewrite as a repository-relative link |
| Pending count not decreasing over time | Expected, while lessons remain unwritten | No action; check the target spelling is exactly as planned |

**Counting directory levels** is the most common source of errors. A file at
`00-orientation/02-curriculum-map/01-master-map.md` needs `../../README.md` to
reach the repository root, because `..` from a file refers to its own directory
(`02-curriculum-map`), not to the file.

## 5. Check 3 — LaTeX delimiters

**What it does.** It strips fenced code blocks (delimited by ``` or ~~~), since
code may contain literal dollar signs, then checks:

1. **Display math.** The total number of double-dollar delimiters in the file
   must be even.
2. **Inline math, line by line.** On each line, after removing display-math
   delimiters, the number of single-dollar delimiters must be even — unless that
   line contains a double-dollar delimiter.
3. **Escaped dollars.** `\$` counts as a literal currency sign, not a delimiter.
4. **Global check.** If a file uses no display math at all, the *total* number of
   inline `$` across the file must be even as a fallback.

**What it does not do.** It does not parse LaTeX, so it cannot tell whether a
formula is *correct* or whether `\left(` has a matching `\right)`. It only
guarantees the delimiters are balanced, which is the failure that visibly breaks
rendering.

**Typical failures and repairs.**

| Message | Cause | Repair |
|---|---|---|
| `unbalanced display-math delimiters (3)` | A display block opened and never closed | Close the block, or delete the stray display delimiter |
| `file.md:41: odd number of inline '$' delimiters` | A single `$` used as currency, or an unclosed inline formula | Escape it as `\$`, or close the formula |
| Formula renders as text | Delimiters not recognised, often because they sit inside a code fence | Move the formula out of the fence |

A useful habit: write each line so that it contains an even number of `$`
characters. That single rule prevents nearly all of these failures.

## 6. Check 4 — duplicate identifiers

**What it does.** It collects the `id` and the `title` of every lesson file and
fails if either appears more than once, reporting both paths.

**Why both.** Ids must be unique because they are the vocabulary of prerequisites
and cross-references. Titles must be unique because readers, indexes and search
results use them to identify a lesson; two lessons called "Gravity anomalies"
in different folders is a real navigational hazard.

**Typical failures and repairs.**

| Message | Cause | Repair |
|---|---|---|
| `duplicate id '06-04-02' (also in ...)` | Two files claim one plan entry, usually after a renumbering | Renumber the file and its frontmatter, and update references |
| `duplicate title 'Data processing'` | Generic title reused | Make the title specific about the method, dataset or scope |

## 7. The other two tools

### `tools/build_index.py` — coverage

Reconciles the plan with what is actually on disk and regenerates
[CURRICULUM.md](../../CURRICULUM.md). Run it after adding or removing lessons.

```bash
python3 tools/build_index.py           # rewrite CURRICULUM.md
python3 tools/build_index.py --check   # exit 1 if CURRICULUM.md is stale
```

`CURRICULUM.md` is generated; never edit it by hand. Two properties of this tool
matter when you read its output: it reports *real* coverage rather than intended
coverage, and a lesson counts as written only if its frontmatter parses, so a
malformed file is not counted as progress.

### `tools/verify_links.py` — external URLs

Two modes with different requirements:

```bash
python3 tools/verify_links.py                  # audit Markdown against the registry (offline)
python3 tools/verify_links.py --check          # re-request every registered URL (needs network)
```

The default audit extracts every external URL from the Markdown and confirms each
one appears in [`tools/verified_links.tsv`](../../tools/verified_links.tsv). This
is the check that makes it impossible to cite an unverified resource.

`--check` re-requests each registered URL and reports status changes. The status
semantics recorded in the registry are worth knowing:

| Status | Meaning | Action |
|---|---|---|
| `200` | Reachable | Cite normally |
| `403` | Reachable but blocks automated requests, typically bot protection | Treat as valid; verify manually in a browser before relying on it |
| `404` | Not valid | Do not cite; the registry keeps it listed as rejected |
| `000` | Connection or TLS failure from this machine | Do not cite until confirmed |

Note the asymmetry: `check_all.py` ignores external URLs entirely (it skips
`http`/`https` targets), so URL integrity is `verify_links.py`'s job alone. Run
both before treating a batch as finished.

## 8. What the gate does not check

Stated plainly, because the gate's green light is not a certificate of quality:

- **Scientific correctness.** A wrong formula with balanced delimiters passes.
- **Physical plausibility of numbers.** The gate does not know that a crustal
  density of $7\times10^{6}\ \text{kg}\,\text{m}^{-3}$ is absurd; a dimensional
  check and an order-of-magnitude estimate are your tools for that.
- **Whether `prereqs` reference lessons that exist.** Ids in `prereqs` are not
  validated against the plan.
- **Tag vocabulary, prose quality, spelling, or completeness.** No content review
  is performed.
- **Whether cited URLs still resolve.** Only `verify_links.py --check` does that,
  and only for registered URLs.
- **Whether a lesson is substantive.** `build_index.py` counts a lesson as
  written when its frontmatter parses; a stub with valid frontmatter passes both
  tools.

The implication is a division of labour: the gate enforces mechanical
consistency, and a human must supply judgement. Section 6 of
[Research Milestones](../01-study-roadmap/05-milestones.md) is the checklist for
the judgement half.

## 9. A worked repair session

Suppose you add a lesson with a careless cut-and-paste and run the gate:

```text
[..] structure & frontmatter
      FAIL 02-physics/01-measurement-and-physical-reasoning/03-units.md: not declared in tools/curriculum_plan.py
[..] relative links
      FAIL 02-physics/01-measurement-and-physical-reasoning/03-units.md: broken relative link -> ../../../01-mathematics/README.md
[..] LaTeX delimiters
      FAIL 02-physics/01-measurement-and-physical-reasoning/03-units.md:7: odd number of inline '$' delimiters
[..] duplicate identifiers
      FAIL 02-physics/01-measurement-and-physical-reasoning/03-units.md: duplicate title 'Units and Dimensional Analysis' (also in 01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)

RESULT: FAIL
```

Four failures, four distinct causes, and each has a specific repair:

1. **Not in the plan.** The lesson tuple was never added to
   `tools/curriculum_plan.py`. Add it — the file's docstring states the three-step
   procedure.
2. **Broken link.** The link used three `..` segments where two are needed from
   that directory. Count the levels.
3. **Odd `$` on line 7.** Probably a currency sign or an unclosed inline formula;
   inspect the line and escape or close it.
4. **Duplicate title.** The title is too generic and collides with an existing
   lesson; make it specific to this lesson's method and scope, in both the plan
   and the frontmatter.

Re-run the gate after fixing. Because the checks are independent, a single run
tells you the whole list rather than one failure at a time.

## 10. Using the gate continuously

- **Before every commit** that touches Markdown: run `check_all.py`.
- **After adding content:** run `check_all.py` then `build_index.py`.
- **After adding any external URL:** run `verify_links.py` (audit) and register
  the URL with an observed status first if it is new.
- **In continuous integration:** the tools exit non-zero on failure, so they can
  be used as a gate directly. `build_index.py --check` additionally fails when
  `CURRICULUM.md` is stale, which catches "forgot to regenerate".

```yaml
# Illustrative CI steps; adapt to your platform of choice.
steps:
  - run: python3 tools/check_all.py
  - run: python3 tools/build_index.py --check
  - run: python3 tools/verify_links.py
```

## Common mistakes

1. **Treating `RESULT: PASS` as a statement about content quality.** It is a
   statement about metadata, links, delimiters and uniqueness.
2. **Editing `CURRICULUM.md`.** Regenerate it.
3. **Fixing the frontmatter but not the plan, or the reverse.** The check
   compares them, so both must agree.
4. **Miscounting `..` depth in links.** The most frequent failure by a wide
   margin.
5. **Using `$` for currency in prose.** Use `\$`, or restructure the sentence.
6. **Reusing a generic title.** Titles are global identifiers for readers.
7. **Registering a URL without checking it in a browser.** The registry's whole
   value is that a human saw the page.

## Real-world applications

- **Documentation and knowledge-base maintenance.** The same four failure modes
  appear in any large Markdown corpus; the automated gate is what keeps a
  thousand-file repository navigable.
- **Data product quality control.** The gate is a small example of a general
  pattern: automate the mechanical checks so that human review time goes to the
  parts only humans can judge.
- **Research software practice.** Test scripts that are fast, standard-library
  only and runnable anywhere are the reason a project can be validated on a
  reviewer's machine — see
  [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md).

## Further reading

- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K.
  (2017). Good enough practices in scientific computing. *PLOS Computational
  Biology*, 13(6), e1005510. — On keeping checks cheap and running them often.
- Roache, P. J. (1998). *Verification and Validation in Computational Science and
  Engineering.* Hermosa. — The distinction between verifying that you solved the
  equations correctly and validating that you solved the right equations; the same
  distinction applies to checking a document versus checking its content.
- Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. — For running a
  check automatically at commit time, and for reading the diff of a regenerated
  file.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [Repository Navigation and File Naming Conventions](./01-navigation.md)
- [Batch Workflow for Adding Lessons and Projects](./04-contribution-workflow.md)
- [Setting Up the Python Environment and Tooling](./02-environment-setup.md)
- [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](../02-curriculum-map/04-cross-cutting.md)
