# 26 — Reference Library, Glossary and Formula Handbook

**Stages:** all stages (beginner → research) · **Prerequisites:** none

This folder is a **lookup resource**, not a course. Nothing here is meant to be
read start to finish. Come here when you need to resolve a symbol, check a unit
conversion, find the accepted value of a constant, look up a term, recall a
formula, decide which textbook to consult next, or find out where the data
actually live.

It is the only folder in this curriculum with no exercises and no companion
files, by design: reference pages are for consulting during other work, not for
practice on their own.

## Modules

| # | Module | Lessons | Use it for |
|---|---|---|---|
| 01 | [Glossary of Geophysical Terms](./01-glossary/README.md) | 4 | Resolving terminology, acronyms, and overloaded words across four letter ranges (A–F, G–M, N–S, T–Z) |
| 02 | [Symbols, Units and Conventions](./02-symbols-and-units/README.md) | 4 | Symbol notation, unit conversions, physical constants, dimensional quick-reference |
| 03 | [Formula Handbook](./03-formula-handbook/README.md) | 7 | Compact formula sheets by subject area, each with conditions and a print-only verification script |
| 04 | [Annotated Textbook Bibliography](./04-textbook-bibliography/README.md) | 8 | What to read, at what level, and why — including what each book is *not* for |
| 05 | [Catalogue of Open Datasets and Data Services](./05-open-datasets-catalogue/README.md) | 6 | Where to get real data, with provenance labels and verified access points |
| 06 | [Open Educational Resources and Software Directory](./06-open-educational-resources/README.md) | 4 | Free courses, open-source tools, and the licensing rules for reusing either |

## How to study with this folder

| Situation | Start at |
|---|---|
| You met an unfamiliar word | 01 — search the letter range |
| You are unsure what a symbol or unit means | 02 — symbol handbook, then units handbook |
| A formula's sign, factor or condition is unclear | 03 — the subject sheet, then run its verification script |
| You have the right formula but no intuition for the assumptions | 03 (conditions column), then the taught lesson linked from that sheet |
| You want a second source on a topic | 04 — the annotated bibliography for that subject |
| You need data | 05 — the subject catalogue, then the provider's own documentation |
| You are building a course or a toolbox | 06 — OER and software, then the licence policy before you publish |

## How the cross-references work

Lessons throughout the curriculum link here when they introduce a symbol, unit or
formula. The most-consulted pages are:

- [Symbol Handbook](./02-symbols-and-units/01-symbol-handbook.md)
- [Units Handbook](./02-symbols-and-units/02-units-handbook.md)
- [Formula Sheet: Waves, Elasticity and Seismology](./03-formula-handbook/03-formulas-waves-seismology.md)
- [Glossary: A-F](./01-glossary/01-glossary-a-f.md)

Reference pages link *out* to the lesson that teaches each topic properly, so a
lookup leads on to the real treatment rather than stopping at a definition.

## A standing warning about constants and conventions

Reference values go stale, and conventions differ between subfields. Every entry
in this folder therefore distinguishes three cases, and you should too:

| Case | Example | How it is marked |
|---|---|---|
| **Defining (exact)** | Speed of light $c$, standard gravity $g_n$ | Stated as exact, because international agreement makes it so |
| **Measured (uncertain)** | Gravitational constant $G$ | Value given with its uncertainty and the determining body |
| **Nominal or conventional** | Mantle viscosity, mean crustal density | Given as an order of magnitude or a typical range, never as a single precise value |

**Before using any value from this folder in publishable work, verify it against
the current official release** of the responsible body: NIST CODATA for physical
constants, the IERS for Earth orientation and geodetic parameters, the EPSG
registry for coordinate-system and ellipsoid parameters, and the relevant
national or international data centre for geophysical compilations.

This folder does not reproduce copyrighted tables. It states values and points
you to the authoritative source.

## Honesty rules that apply to this folder

| Rule | Where it is visible |
|---|---|
| Real works only in the bibliography; no invented authors, titles, DOIs or URLs | [26-04](./04-textbook-bibliography/README.md) |
| Only URLs registered in [`tools/verified_links.tsv`](../tools/verified_links.tsv) are cited, with dead ones flagged | [26-05](./05-open-datasets-catalogue/README.md), [26-06](./06-open-educational-resources/README.md) |
| Every dataset carries a provenance label: OBSERVED, ILLUSTRATIVE or SYNTHETIC | All of [26-05](./05-open-datasets-catalogue/README.md) |
| Every statement of what data do *not* constrain is written explicitly | The last column of every dataset table |
| Verification scripts are print-only, seeded and print a SYNTHETIC provenance line | [26-03 code](./03-formula-handbook/README.md) |

## Related folders

- [01-mathematics](../01-mathematics/README.md) — where the notation is introduced and derived.
- [02-physics](../02-physics/README.md) — where the constants acquire their physical meaning.
- [18-inverse-problems](../18-inverse-problems/README.md) — the taught treatment behind the inverse and statistics sheets.
- [22-data-engineering-reproducibility](../22-data-engineering-reproducibility/README.md) — how to make a result reproducible, including its data provenance.
- [00-orientation](../00-orientation/README.md) — how to use the repository as a whole.
