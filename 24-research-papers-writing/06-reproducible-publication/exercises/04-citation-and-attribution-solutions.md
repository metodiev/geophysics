# Solutions — 24-06-04 Citation Practice and Attribution

> Read after attempting. Numbers computed. Lesson:
> [04 Citation Practice and Attribution](../04-citation-and-attribution.md).

---

## ★1 — Total citations and skew

$$\text{total} = 800 \times 25.8 = 20\,640\ \text{citations}
\ (\text{the demonstration reports } 20\,669 \text{ from the raw counts}),$$
$$\text{ratio} = \frac{25.8}{12} = 2.15 .$$

The mean is more than twice the median, so the mean describes a paper that does not
exist. This is the arithmetic reason to report a distribution rather than a total or a
mean.

---

## ★2 — Share held by the rest

$$\text{other } 94\% \text{ of papers} = 100\% - 49.1\% = 50.9\%\ \text{of citations}.$$

$$\frac{\text{top share}}{\text{proportional share}} = \frac{49.1\%}{6\%} = 8.2 .$$

So the top $6\%$ of papers hold $8.2$ times what proportional distribution would give
them, while $94\%$ of papers share the other half of the citations. Both halves of that
sentence matter: the concentration is extreme at the top and the bulk of papers attract
a substantial fraction of the attention — the distribution is not one where a few
papers hold nearly everything.

---

## ★3 — Citing versus acknowledging

**Acknowledging** names a dependency in prose — "we thank the X project for the data" —
and creates no bibliographic record. **Citing** creates a record with an identifier in
the reference list.

Only the citation enters a citation index, because indexes parse reference lists, not
acknowledgements. The practical consequence is that an acknowledged dependency
accumulates no visible credit, however essential it was, which is why guidance from
repositories and journals asks for formal citations with identifiers.

---

## ★4 — Exponent and its limits

$$\alpha = -(-0.713) + 1 = 1.713 .$$

Two reasons it is not universal:

1. **The fit depends on the range.** The tail of a lognormal behaves differently over
   different windows, so including or excluding the smallest counts changes the slope;
   the reported number is meaningless without the interval $[1, 661]$.
2. **The generating process is not a power law.** The synthetic corpus is lognormal,
   so the exponent describes the local slope of a different distribution's tail. Even
   in real data, several mechanisms produce heavy tails, and the slope does not
   identify which one is at work.

A third, practical reason is field dependence: citation practices differ by an order of
magnitude between subfields, so exponents are comparable only within a corpus and a
range.

---

## ★5 — Citation rates and gaps

$$\text{data rate} = \frac{252}{600} = 42.0\%, \qquad
\text{gap} = 600 - 252 = 348\ \text{uses uncited},$$
$$\text{software rate} = \frac{266}{760} = 35.0\%, \qquad
\text{gap} = 760 - 266 = 494\ \text{uses uncited}.$$

Proportionally, the software gap is larger: $65.0\%$ of software uses are uncited
against $58.0\%$ of data uses. In absolute counts the software gap is also larger
($494$ vs $348$) despite a smaller denominator difference, because more papers use
software than use any single dataset. Both measures point the same way here, which is
not always the case — report both.

---

## ★6 — Invisible dependency credit

Three cited packages and two uncited ones: the paper depends on five, of which two are
invisible to the index:

$$\frac{2}{5} = 40\%\ \text{of the dependency credit is invisible}.$$

A citation index reports the paper's own $25.8$ citations and credits the three cited
packages; the two uncited packages receive nothing from this paper. So the index's
picture of the paper is complete while its picture of the *infrastructure* is missing
two fifths of the dependencies — which is why infrastructure use is systematically
underestimated by bibliometrics and why explicit citation is the only mechanism that
makes it visible.

---

## ★7 — Does a citation requirement work?

**Unit.** One research article.

**Outcome.** The number of software citations in the article's reference list,
restricted to citations that carry an identifier and refer to software (classifiable
from the reference's type, the venue's metadata or the identifier's registry record).

**Design.** Difference-in-differences across journals, with the policy adoption date as
the treatment time and matched non-adopting journals as controls; two periods before
and after the date, sampled at a fixed interval from it so that field-wide trends
affect both arms.

**Sample size.** Difference $0.5$ software citations per paper, standard deviation
$1.2$:

$$n\ \text{per arm} = \frac{2(1.96 + 0.842)^{2}\times 1.2^{2}}{0.5^{2}}
= \frac{2\times 7.851\times 1.44}{0.25} = 90.4 \approx 91\ \text{articles per arm per period},$$

i.e. $182$ articles per arm across the two periods, or $364$ in total.

**Confound.** Software citation norms are changing everywhere and fast, which is why a
before-and-after design within the adopting journal would overstate the effect. The
control group measures that trend, and the effect is the difference in changes — with
the honest caveat that if the adopting journal's community is also the one driving the
norm change, the control under-corrects and the estimate is an upper bound.

---

## ★8 — The software citation penalty

**Matched comparison.** Papers describing software, matched one-to-one with method
papers on field, publication year and venue, and where possible on the number of
figures and the length, since these correlate with citation rates.

**Outcome.** Citations accrued within a fixed window from publication (for example five
years), counted from a single source with a stated date, and reported as a distribution
(median and top-decile share) rather than as a mean, because the distribution is
heavy-tailed.

**Sampling.** Build the software-paper sample from repositories' own publication lists
or from identifiers registered for software releases, then draw the matched method
papers from the same venues and years. Report the match quality, since software papers
are easier to identify in some venues than others.

**Two reasons the measured penalty is partly an artefact.** First, **audience**: a
software paper is read by users, who cite the software in a footnote, in a
documentation page or not at all, whereas a method paper is read by authors who must
cite it to write their Methods. The citation mechanism is not the same for the two
genres, so part of the difference is a difference in citable route, not in value.
Second, **age of the artefact**: software releases are superseded by later versions,
and citations may be split across versions or directed to a project-level record, which
diffuses the count even when credit is given. Any study of the penalty must state which
of these it can and cannot separate — and the honest answer is usually that it can
measure the penalty and cannot attribute it entirely to evaluation bias.
