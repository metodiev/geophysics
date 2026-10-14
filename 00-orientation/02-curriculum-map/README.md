# Module 00-02 — Curriculum Map and Dependency Graph

**Stage:** all stages · **Prerequisites:** [00-01 study roadmap](../01-study-roadmap/README.md)

This module is the **map of the curriculum**. It answers three questions that
otherwise cost learners weeks of wrong turns: what the 27 folders contain, which
folders genuinely depend on which, and how to assemble a defensible study order
for a specific goal.

Read it once to orient yourself, then return whenever you are choosing what to
study next, changing specialisation, or planning a project with a deadline.

## Learning objectives

By the end of this module you will be able to:

1. Describe the four functional layers of the curriculum and place any folder in
   its layer without consulting a table.
2. Read the prerequisite structure as a directed graph, and state what an edge
   does and does not imply.
3. Identify folders that may safely be studied in parallel, and orders that are
   guaranteed to fail.
4. Choose a domain track — seismology, potential fields, electromagnetics,
   climate, or near-surface — for a stated goal, with an explicit account of what
   that choice omits.
5. Interleave the cross-cutting skills (mathematics, computing, inverse theory)
   with the domain material that needs them, instead of deferring them.

## Lessons

| # | Lesson | Level |
|---|---|---|
| 01 | [Master Curriculum Map: How the 27 Folders Connect](./01-master-map.md) | beginner |
| 02 | [Prerequisite Dependency Graph and Valid Study Orders](./02-dependency-graph.md) | beginner |
| 03 | [Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface](./03-domain-tracks.md) | beginner |
| 04 | [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](./04-cross-cutting.md) | beginner |

## The map in one table

| Layer | Folders | What it supplies |
|---|---|---|
| Orientation | 00 | Method, map, repository mechanics, what geophysics is |
| Foundations | 01–03 | Mathematics, physics, scientific computing |
| Earth context and methods | 04–17 | Earth science, core geophysics, then the domain methods |
| Inference and computation | 18–22 | Inverse problems, numerical modelling, signal processing, statistics, data engineering |
| Practice and integration | 23–26 | Field methods, writing, projects, reference library |

The full folder-by-folder view, including module and lesson counts and what each
folder feeds into, is in [lesson 01](./01-master-map.md).

## The spine

Whatever track you choose, the entry spine is the same:

```text
01-mathematics → 02-physics → 05-core-geophysics → domain folder (06–17)
                        ↑
              03-scientific-computing (in parallel from the start)
```

Everything else — [18-inverse-problems](../../18-inverse-problems/README.md),
[19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md),
[20-signal-processing](../../20-signal-processing/README.md),
[21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md),
[22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
is drawn on *when the domain material needs it*, not saved until the end.

## Mastery checkpoint

You have completed this module when you can, without notes:

- [ ] Sketch the dependency graph from memory at folder level, and say why
      folder 18 sits where it does.
- [ ] Name two pairs of folders that are safe to study in parallel, and justify
      each from the absence of an edge between them.
- [ ] Given a goal such as "map a shallow aquifer" or "estimate seismic hazard",
      write a valid study order with an explicit artifact at each stage.
- [ ] State one thing you have chosen *not* to learn by selecting your current
      track, and why that is acceptable.

## Related modules

- [01-study-roadmap](../01-study-roadmap/README.md) — the stages and checkpoints
  that motivate choosing an order at all.
- [03-how-to-use-this-repo](../03-how-to-use-this-repo/README.md) — where the
  files described on this map actually live, and how to run them.
- [04-orientation-geophysics](../04-orientation-geophysics/README.md) — what the
  subject is, before deciding which part of it to specialise in.
