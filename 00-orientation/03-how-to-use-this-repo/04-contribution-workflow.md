---
id: 00-03-04
title: "Batch Workflow for Adding Lessons and Projects"
level: intermediate
prereqs: ["00-03-01"]
estimated_minutes: 45
tags: [workflow, contribution, repository, tooling]
---

# Batch Workflow for Adding Lessons and Projects

## Learning objectives

- Apply the repository's three-step contract — declare in the plan, write the
  file, validate and regenerate — to any new lesson or project.
- Choose an `id`, slug, title and level that stay consistent across the plan and
  the file.
- Plan a **batch** of lessons so that dependencies are satisfied and validation
  runs once per batch rather than once per file.
- Use the pre-commit checklist to catch the failure modes that the automated gate
  cannot see.

## Prerequisites

[Running the Link, Formula and Duplication Checks](./03-quality-gate.md) for what
each validation tool does, and
[Repository Navigation and File Naming Conventions](./01-navigation.md) for the
layout.

## 1. The three-step contract

Every piece of content in this repository is added in the same three steps, in
this order:

```text
1. DECLARE   add the lesson tuple to tools/curriculum_plan.py
2. WRITE     create the Markdown file with matching frontmatter
3. VALIDATE  run check_all.py, then build_index.py, then verify_links.py
```

The order is not arbitrary. The plan is the source of truth, so the tuple comes
first; the file's `id`, `title` and `level` are then *copied* from the plan rather
than invented. Doing it in the other order is how the two drift apart, and drift
is the first thing the gate reports.

## 2. Step 1 — declare in the plan

`tools/curriculum_plan.py` holds a nested tuple structure, documented in its own
module docstring:

```text
Lesson tuple layout:  (number, slug, title, level)
Module tuple layout:  (number, slug, title, lessons)
Folder tuple layout:  (number, slug, title, stage, modules)
```

The lesson `id` and the file path are both derived mechanically:

```text
id    = f"{folder_number}-{module_number}-{lesson_number}"
path  = f"{folder_slug}/{module_number}-{module_slug}/{lesson_number}-{lesson_slug}.md"
```

So a lesson declared as:

```python
("03", "self-assessment", "Diagnostic Self-Assessment and Placement Quiz", "beginner"),
```

inside module `("01", "study-roadmap", ...)` of folder `"00-orientation"` becomes
`id: 00-01-03` at path
`00-orientation/01-study-roadmap/03-self-assessment.md`.

**Choices to make deliberately:**

| Field | Guidance |
|---|---|
| Number | Next unused two-digit number in the module; order should follow teaching order |
| Slug | Lowercase, hyphenated, descriptive, stable. It appears in paths and cross-references, so avoid changing it later |
| Title | Specific enough to be globally unique — include the method, dataset or scope — and match it exactly in the frontmatter |
| Level | The *lesson's* level, from `beginner`, `intermediate`, `advanced`, `graduate`, `doctoral`, `research`. Check the module's other lessons for calibration |

Level calibration matters more than it looks: the level drives the stage
aggregation in [CURRICULUM.md](../../CURRICULUM.md), and a lesson marked
`beginner` that assumes multivariable calculus misleads every reader who trusts
the marker. Compare with
[The Six Stages and Their Mastery Checkpoints](../01-study-roadmap/02-six-stages.md)
and pick the stage whose entry requirement matches what the lesson assumes.

## 3. Step 2 — write the file

Frontmatter, with the fields the parser requires:

```markdown
---
id: 00-01-03
title: "Diagnostic Self-Assessment and Placement Quiz"
level: beginner
prereqs: ["00-01-01"]
estimated_minutes: 40
tags: [self-assessment, study-method, placement]
---
```

Then the body, using the repository's lesson anatomy. The mandated order is:

```text
# Title (matching the frontmatter title)

## Learning objectives
## Prerequisites
## 1. ...  ## 2. ...
## Common mistakes
## Real-world applications
## Further reading
## Related lessons
```

Within the numbered sections, include whichever of the following the topic
supports: intuition before formalism, precise definitions, equations in LaTeX,
step-by-step derivations, physical interpretation, assumptions and validity, units
and dimensional analysis, worked examples, a short Python demonstration, and
exercises graded ★ / ★★ / ★★★.

**Content rules that the gate cannot enforce but a reviewer will:**

1. **Do not invent facts, numbers, dates, names, URLs or citations.** If you are
   unsure of a figure, say the figure varies by source and should be checked.
   Stating uncertainty is always better than stating a fabricated number.
2. **Cite only registered external URLs.** Add a new URL to
   `tools/verified_links.tsv` only after confirming it in a browser, with the
   observed status and date.
3. **Use relative links only**, and prefer links to paths the plan declares.
4. **Label datasets** `SYNTHETIC`, `OBSERVED` or `ILLUSTRATIVE` so readers know
   how much weight the numbers carry.
5. **Balance LaTeX delimiters**, and prefer one formula per line so that a
   misplaced inline delimiter is easy to find.
6. **State uncertainty** wherever you produce a number, and say what the number
   does not constrain.

## 4. Step 3 — validate and regenerate

```bash
python3 tools/check_all.py         # structure, links, LaTeX, duplicates
python3 tools/build_index.py       # regenerate CURRICULUM.md
python3 tools/verify_links.py      # audit cited URLs against the registry
```

Fix every `FAIL` line and re-run until `check_all.py` prints `RESULT: PASS`.
Because the four checks are independent, one run lists all current problems; fix
them together and re-run once.

If you added external URLs, also run:

```bash
python3 tools/verify_links.py --check    # needs network access
```

Treat a batch as finished only when: `check_all.py` passes, `CURRICULUM.md` has
been regenerated, and the URL audit is clean.

## 5. Batching

Write in batches of one module (three to five lessons). Batching is not only
about efficiency; it is what makes a module coherent.

**Before starting a batch:**

1. Read the module's plan entry and its `README.md` (or plan to write the README
   as part of the batch).
2. Read one existing written lesson from the same folder to calibrate voice,
   depth and section structure.
3. List the lessons in teaching order and write down the prerequisite each one
   assumes. If a prerequisite is not yet written, either write it in the same
   batch or link to the planned path (pending links are allowed).
4. Decide the level of each lesson *before* writing it, not after.

**During a batch:**

- Write all lessons' frontmatter first, then fill bodies. This makes drift in
  ids and titles almost impossible.
- Keep a running list of any new external URL as you write, so the registry update
  happens once at the end rather than during each lesson.
- Reuse the same recurring structure (objectives, mistakes, applications,
  reading, related lessons) so that the module reads as one unit.

**After a batch:**

- Update the module `README.md` lesson table so it lists every lesson with its
  level.
- Update the `Related lessons` sections of the neighbouring lessons you touched.
- Run the three validation commands.

## 6. Worked example: adding one lesson to an existing module

Suppose the module `06-seismology/02-ray-theory-and-travel-times` has lessons
`01`–`04` and needs a new lesson on the eikonal equation.

**Step 1 — declare it.**

```python
("05", "eikonal-equation", "The Eikonal Equation and High-Frequency Ray Theory", "advanced"),
```

**Step 2 — write the file.** Path:
`06-seismology/02-ray-theory-and-travel-times/05-eikonal-equation.md`. Its
frontmatter must contain `id: 06-02-05`, the title exactly as declared, and
`level: advanced`.

**Step 3 — validate.**

```bash
python3 tools/check_all.py
python3 tools/build_index.py
python3 tools/verify_links.py
```

**Step 4 — link it in.** Add a row to
`06-seismology/02-ray-theory-and-travel-times/README.md` and a line in the
`Related lessons` section of the adjacent lessons.

The failure to watch for: if the frontmatter says
`"The Eikonal Equation and High Frequency Ray Theory"` — no hyphen — the structure
check fails with a title mismatch. Copy-paste from the plan; do not retype.

## 7. Adding a module, or a new folder

**A new module** is a new numbered subfolder with a `README.md`, plus a module
tuple in the plan. Module READMEs carry no frontmatter and follow this structure:

```text
# Module NN-MM — Title
**Stage:** ... · **Prerequisites:** ...
A short statement of what the module is for.
## Learning objectives      (numbered list, 4–6 items)
## Lessons                  (table: number, link, level)
## Mastery checkpoint       (checkbox list of things you can do unaided)
## Related modules
```

**A new folder** additionally requires a folder tuple with its own stage range, a
folder `README.md` acting as the entry point, and — for a whole new thematic area
— an update to the folder overview in the root [README](../../README.md).

**Projects** follow the same contract, with the plan entry in
[25-projects-capstone](../../25-projects-capstone/README.md): declare the project
lesson, state the data and the expected artefact, and make the deliverable
checkable. A project whose success criterion is "explore the dataset" is not a
project, by the standard in
[Research Milestones](../01-study-roadmap/05-milestones.md).

## 8. Pre-commit review checklist

Run through this list before committing a batch. The first block is what the gate
checks; the second is what only you can check.

**Mechanical (the gate will catch these, but check anyway):**

- [ ] Every new lesson file has frontmatter with `id`, `title`, `level`,
      `prereqs`, `tags`.
- [ ] `id`, `title` and `level` match the plan character for character.
- [ ] Every relative link resolves, or is a planned path.
- [ ] No absolute filesystem paths in links.
- [ ] Every line has balanced inline delimiters; display-math blocks are closed.
- [ ] No duplicate id or title anywhere in the repository.
- [ ] `CURRICULUM.md` has been regenerated.

**Editorial (the gate cannot see these):**

- [ ] Section order follows the mandated anatomy.
- [ ] Every objective is checkable; none is "understand X" without an observable.
- [ ] Worked examples are actually worked, with the arithmetic shown.
- [ ] Units appear on every quantity, and one dimensional check is shown.
- [ ] Uncertainty is stated wherever a number is produced.
- [ ] No invented facts, dates, statistics, names or citations.
- [ ] Every external URL is registered in `tools/verified_links.tsv`.
- [ ] Datasets are labelled `SYNTHETIC` / `OBSERVED` / `ILLUSTRATIVE`.
- [ ] `prereqs` names lessons that exist or are planned.
- [ ] `Common mistakes` entries are specific to this topic, not generic advice.
- [ ] `Related lessons` links forward and backward sensibly.
- [ ] No placeholder text, no "TODO", no stub section headings.
- [ ] The lesson is 150–350 lines of substantive content, or an explicit decision
      is recorded for why it is shorter.
- [ ] The module `README.md` lists the lesson.

## 9. Version control

- **One batch, one commit**, with a message that names the module and the
  lessons, for example: `Add 00-03 how-to-use-this-repo module (4 lessons)`.
- **Regenerate before committing.** Committing a stale `CURRICULUM.md` means the
  coverage figures are wrong in the history.
- **Review the diff of generated files.** A large `CURRICULUM.md` diff is normal
  after a batch; an unexpected one is a signal that something was renumbered.
- **Do not commit environments or data.** `.venv` is ignored; large datasets
  should be fetched from their archive by URL rather than committed.

## Common mistakes

1. **Writing the file before declaring it.** The gate then reports "not declared
   in tools/curriculum_plan.py", and the fix requires re-checking that the id and
   path match.
2. **Retyping titles.** Retype risk is why the check is character-for-character.
   Copy from the plan.
3. **Writing lessons in a module out of order.** It is legal (numbers are just
   names) but it confuses batching and cross-references.
4. **Forgetting `build_index.py`.** Coverage then understates the work, and
   `build_index.py --check` fails in continuous integration.
5. **Adding a URL while writing and forgetting the registry.** The audit will
   fail later, usually at an inconvenient moment.
6. **Reusing a generic title** such as "Data processing" across folders.
7. **Leaving placeholder sections.** A stub passes the mechanical gate and fails
   the reader.
8. **Skipping the editorial checklist** because the gate is green. The gate
   checks consistency, not truth.

## Real-world applications

- **Documentation-as-code workflows.** The plan-then-write-then-validate loop is
  the same shape as infrastructure-as-code and specification-first development.
- **Data product release.** Batching, a fixed checklist and an automated gate are
  how a data product is assembled predictably instead of heroically.
- **Research group practice.** A lab writing a shared handbook needs exactly these
  conventions: a declared structure, a cheap validator, and a review checklist
  that separates mechanical from scientific review.
- **Teaching a course.** The same batch discipline is how a lecture sequence is
  built, checked and revised between terms without breaking its internal links.

## Further reading

- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K.
  (2017). Good enough practices in scientific computing. *PLOS Computational
  Biology*, 13(6), e1005510. — On the value of cheap, frequent checks over rare,
  expensive ones.
- Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. — Chapter 2 covers
  the commit and diff workflow used in section 9.
- Gawande, A. (2009). *The Checklist Manifesto.* Metropolitan Books. — A
  widely-read argument for checklists in complex work; the mechanical versus
  judgement split in section 8 is deliberately of that kind.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [Running the Link, Formula and Duplication Checks](./03-quality-gate.md)
- [Repository Navigation and File Naming Conventions](./01-navigation.md)
- [Research Milestones from Beginner to Independent Investigator](../01-study-roadmap/05-milestones.md)
- [Master Curriculum Map: How the 27 Folders Connect](../02-curriculum-map/01-master-map.md)
