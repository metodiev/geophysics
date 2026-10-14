# Module 26-06 — Open Educational Resources and Software Directory

**Stages:** beginner → doctoral · **Prerequisites:** none (lookup resource)

Where to find free and openly licensed teaching material, and which open-source
software to use for which task. Four pages: foundations in mathematics and
computing, Earth-science courses and open journals, an annotated software
directory, and the licensing and attribution policy that governs reuse of
everything the other three list.

The module's working distinction is between **free to read** and **openly
licensed**. Most lecture notes on departmental pages are free to read and retain
all rights; most open textbooks, open-access articles and open-source projects
grant defined reuse rights. Treating the first as the second is the most common
integrity failure in teaching material, and the reason every entry here states
its licence position.

## Lessons

| # | Lesson | Level | Covers |
|---|---|---|---|
| 01 | [OER: Mathematics, Physics and Computing](./01-oer-mathematics.md) | beginner | Open courses, open textbooks, scientific-computing material, language and library documentation |
| 02 | [OER: Geophysics, Seismology and Earth Science Courses](./02-oer-geophysics.md) | intermediate | Open journals, agency publications, course material, data-based exercises |
| 03 | [Software Directory: Open-Source Geophysics Tools](./03-software-directory.md) | advanced | Data access, processing, inversion frameworks, geospatial tooling, numerics and plotting |
| 04 | [Data Licensing, Attribution and Reuse Policy](./04-data-policy-and-licences.md) | graduate | Copyright scope, licence families, attribution wording, choosing a licence for your own output |

## Suggested paths

| Reader | Path |
|---|---|
| Undergraduate needing a second explanation | 01, then 02 for the geoscience-specific material |
| Lecturer assembling a course | 02 for content, 03 for tools, 04 for the licence record |
| Researcher writing a data-availability statement | 04, then the citation guidance in [26-05](../05-open-datasets-catalogue/README.md) |
| Software developer integrating geophysical tools | 03, plus 04 for licence compatibility |
| Reviewer checking a manuscript's data provenance | 04 (checklist), then the dataset's own terms |

## Reuse rules adopted by this module

| Rule | Why |
|---|---|
| No external figures or text are reproduced | Copyright-safe by construction |
| Every external URL is registered and status-checked | Dead links look verified and are not |
| Licences are stated as the project states them, with "verify current terms" where projects relicense | Licence facts change |
| Resources that cannot be located from a stable access point are named without a link | A guessed URL is worse than no URL |
| Free-to-read is distinguished from openly licensed | Reuse rights differ |

## Mastery checkpoint

This module has no checkpoint. The skill it supports is **recording provenance
as you go**: dataset version, access date, licence and modification statement.
Retrofitting provenance at submission time is where irreproducible work comes
from.

## Common pitfalls across this module

1. **Assuming "free" means "reusable".** Check the licence, not the price.
2. **Reusing a figure without its licence.** Figures carry their own terms, often
   stated on the article rather than the journal page.
3. **Forgetting share-alike propagation.** ODbL and CC BY-SA can constrain your
   own downstream licence choice.
4. **Citing a project name without a version.** Results change between releases,
   especially in coordinate transformation and optimisation defaults.
5. **Using a dead access point.** Two NOAA marine-geology paths and the retired
   IRIS event service are documented as dead in the registry.

## Related modules

- [26-04 Annotated Textbook Bibliography](../04-textbook-bibliography/README.md) — the peer-reviewed literature behind these resources.
- [26-05 Catalogue of Open Datasets and Data Services](../05-open-datasets-catalogue/README.md) — the data these tools read, with provenance labels.
- [03-scientific-computing](../../03-scientific-computing/README.md) — the environment, testing and packaging practices assumed here.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) — formats, provenance and reproducible pipelines.
- [24-research-papers-writing](../../24-research-papers-writing/README.md) — how to write data-availability and acknowledgement sections.
