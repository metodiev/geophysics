# Solutions — 22-01-05 Licensing, Citation and Software Credit (CITATION.cff)

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [05 Licensing, Citation and Software Credit](../05-licensing-and-citation.md).
> Not legal advice; verify against the licence texts and the SPDX compatibility
> notes before relying on any conclusion.

---

## ★1 — Families and forced combined licences

(a) MIT — **permissive**. (b) MPL-2.0 — **weak copyleft**, per file.
(c) LGPL-3.0 — **weak copyleft**, per library. (d) GPL-3.0 — **strong copyleft**.
(e) AGPL-3.0 — **network copyleft** (strong copyleft plus a network clause).

Forced combined licences:

- MIT + GPL-3.0 → **GPL-3.0**: strong copyleft dominates permissive.
- LGPL-3.0 + GPL-3.0 → **GPL-3.0**: the stronger of the two weak/strong terms.
- GPL-3.0 + AGPL-3.0 → **AGPL-3.0**: the network clause dominates.

The general rule visible in all three cases: the **strongest** obligation in the
combination sets the terms of the distributed work.

## ★2 — `CITATION.cff`

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
title: "Tidal strain-rate toolkit"
version: 1.1.3
license: MIT
doi: 10.0000/example.doi
authors:
  - family-names: Rossi
    given-names: Anna
    orcid: "0000-0000-0000-0000"     # placeholder in the ORCID iD format
  - family-names: Nkosi
    given-names: Bila
```

The `orcid` value is a **placeholder in the ORCID iD format**
(`0000-0000-0000-0000`, written as an identifier string rather than a link), included
only to show where the field goes; it is illustrative and not resolvable, and a real
iD must not be invented.

**Required by the format:** `cff-version`, `message`, `title`, `authors` (with at
least one of `family-names`/`given-names` per author, or `name` for an entity
author).

**Optional but recommended:** `version`, `doi`, `license`, `orcid` per author,
`abstract`, `keywords`, `repository-code`, `preferred-citation` when a method
paper should be cited instead of (or in addition to) the software. `orcid` is
omitted for Bila Nkosi rather than invented: never fabricate an identifier.

## ★3 — Admissible release sets

Release list: `1.0.0, 1.0.3, 1.1.0, 1.1.3, 1.2.0, 1.2.3, 1.3.0, 1.3.3, 2.0.0,
2.0.3, 2.1.0, 2.1.3, 2.2.0, 2.2.3, 2.3.0, 2.3.3` (16 releases).

- `~2.1` means $\ge 2.1.0$ and $< 2.2.0$ → `2.1.0`, `2.1.3` → **2** releases.
- `>=1.3,<2.1` means $\ge 1.3.0$ and $< 2.1.0$ → `1.3.0, 1.3.3, 2.0.0, 2.0.3` →
  **4** releases.
- Strictest of the lesson's three: `~1.2` (2 releases) is strictest, then `^1.2`
  (4), then `>=2.0,<3` (8). The tilde is strictest because it pins the minor
  version as well as the major.

## ★★4 — Citation thresholds

(a) With $c_0 = 8$, $r = 0.35$: $e^{r} - 1 = e^{0.35} - 1 = 1.41907 - 1 =
0.41907$. Setting $\text{cum}(m) = 25$:

$$\frac{8\,(e^{0.35m} - 1)}{0.41907} = 25
\;\Longrightarrow\;
e^{0.35m} - 1 = \frac{25 \times 0.41907}{8} = 1.3096,$$

$$e^{0.35m} = 2.3096 \;\Longrightarrow\; 0.35m = \ln 2.3096 = 0.8372
\;\Longrightarrow\; m = 2.39 \approx 2.4\ \text{years},$$

matching the printed 2.4.

(b) Target 200:

$$e^{0.35m} = 1 + \frac{200 \times 0.41907}{8} = 1 + 10.477 = 11.477,
\qquad m = \frac{\ln 11.477}{0.35} = \frac{2.4403}{0.35} = 6.97\ \text{years}.$$

(c) With $r = 0.20$: $e^{0.20} - 1 = 1.22140 - 1 = 0.22140$. For a target of 25,

$$e^{0.20m} = 1 + \frac{25 \times 0.22140}{8} = 1 + 0.6919 = 1.6919,
\qquad m = \frac{\ln 1.6919}{0.20} = \frac{0.5259}{0.20} = 2.63\ \text{years}.$$

All three crossing years move later (25: 2.4 → 2.6 years; 100: 5.2 → 8.5 years).
The point is that the crossing year is a function of the growth assumption; a
threshold quoted without it is not a fact about the software.

## ★★5 — Dependency licence audit

(a) **Distributed by the container:** everything copied into the image, which is
all four dependencies if they are installed in it — irrespective of whether the
published *analysis* imports them. `some-gpl-tool` is in the image, so its
GPL-3.0 terms govern the distributed image even though no figure uses it.

(b) **Forced combined licence:** GPL-3.0 (from `some-gpl-tool`), with the AGPL
network clause absent because no AGPL dependency is present. `libfoo`'s LGPL-3.0
obligations are satisfied by the GPL-3.0 terms; `numpy` (BSD-3-Clause) and
`chartlib` (MPL-2.0) require only their notices and, for MPL, that MPL-covered
files stay under MPL.

(c) **One change that removes the obligation:** drop `some-gpl-tool` from the
image — install it outside the distributed environment, or replace it with a
permissively licensed equivalent. A copyleft dependency that is *used* but not
*distributed* carries no distribution obligation, which is precisely the
internal-use versus distribution distinction.

## ★★6 — Software-availability statement

> The analysis code is archived at DOI `10.0000/example.doi`, version `1.1.3`,
> under the MIT licence; the environment used to run it is defined by the
> `environment.yml` file included in that archive.

The three environment facts needed to reproduce a figure:

1. the **file** that specifies the environment (`environment.yml`,
   `requirements.txt`, or a container image digest) and the implementation it was
   solved with;
2. the **versions** of every dependency, pinned exactly, plus the Python version;
3. the **platform or image identifier** (for numerical results, the architecture
   and BLAS implementation can change the last digits).

## ★★★7 — Measuring the credit a package receives

**Population.** All works published after the software's first release that cite
its DOI (from the archive's citation records) plus works that cite the method
paper (from the paper's citation index).

**Identifying a software citation.** A work counts as citing the software if its
reference list contains the software DOI, or a reference to the method paper
**and** the availability statement names the package — the second condition is
needed because a reader must be able to resolve the credit. Record the artefact
cited (software DOI, method paper, both) so the split of the lesson's model
(40 % to the software DOI) can be measured instead of assumed.

**Confounders.** (i) *Field and venue*: citation density differs by an order of
magnitude between subfields and between journals and preprints. (ii) *Age*: a
package released four years earlier has had four more years to accrue citations;
comparisons must be age-matched or modelled with the growth curve.

**What the DOI guarantees.** That the cited work is resolvable and, if the
archive is a preservation service, that the content persists. It does **not**
guarantee that the citation is accurate, that the citing work used the software
correctly, or that the archive will maintain the identifier for ever if the
service ceases to operate.

## ★★★8 — Is a citation count associated with correctness?

**Design.** Take a sample of packages in one subfield released over a bounded
window (say 5 years) with an archived version and a method paper. For each,
measure:

- **citations** (age-matched, from the DOI and the paper);
- **correctness**, operationally defined as the result of a **verification
  programme**, not of opinion: does the package reproduce its own published
  benchmark to a stated tolerance, is it tested against an analytic solution or a
  reference implementation, and does an independent group reproduce one figure
  from the archive? Score each of the three as pass/fail and report the vector,
  not a single index, because "correctness" of a scientific package is not one
  number.

Then fit a model for the pass rate as a function of log-citations, controlling
for:

1. **age** (older packages accrue more citations), by matching or by including
   years-since-release;
2. **field/venue** (a seismology tool and a machine-learning tool live in
   different citation regimes), by restricting to one subfield or by including it
   as a factor.

**Two biases the design must control, plus one more.** Besides age and field,
there is **exposure**: packages described in a widely read paper accumulate both
citations and users, so a positive association may be mediated by the paper's
reach rather than by quality.

**What you could and could not conclude.** A positive association permits:
"among packages in this subfield and age window, more-cited packages were more
likely to pass the verification programme, with the effect size X (95 % CI …)".
It does not permit "a citation count measures correctness": the association is
observational, the correctness measure is a proxy, and a reverse pathway
(correct, useful tools attract users, and users cite) is fully consistent with —
and more plausible than — citation count causing correctness.

## ★★★9 — Publishing a container with a GPL-3.0 dependency

**Policy 1 — remove.** Exclude the GPL tool from the distributed image; document
how to install it outside the image for the one calibration figure. *Cost:* one
extra documented step for a reader, and the calibration figure is not bit-for-bit
reproducible inside the container. *Scientific consequence:* the published
analysis is unaffected if the tool truly is not used in it.

**Policy 2 — replace.** Substitute a permissively licensed equivalent and
re-do the calibration. *Cost:* development time and a possible change of the
calibration numbers. *Scientific consequence:* if the equivalent is not as
accurate, a published value changes — that is a scientific decision, not a
licensing one.

**Policy 3 — comply.** Distribute the whole image under GPL-3.0, with complete
corresponding source for the covered work and the licence notices. *Cost:*
choosing GPL-3.0 for your own code in that image; downstream users inherit the
obligation. *Scientific consequence:* none for reproducibility, but the group's
code in that artefact can no longer be reused under a permissive licence.

**Facts a data management plan must record for Policy 3:** (i) the exact
dependency versions and their licences, with the evidence (licence text or
metadata) that the audit read; (ii) the licence assigned to the group's own code
in the distributed artefact, and the fact that it is GPL-3.0 rather than the
group's usual permissive default; (iii) where the corresponding source is
published, and who is responsible for keeping it available for as long as the
image's DOI resolves. Without (iii) the "source available" obligation is an
intention, not a plan.
