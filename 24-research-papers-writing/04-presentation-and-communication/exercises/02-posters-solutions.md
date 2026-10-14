# Solutions — 24-04-02 Designing Effective Scientific Posters

> Read after attempting. Numbers computed. Lesson:
> [02 Designing Effective Scientific Posters](../02-posters.md).

---

## ★1 — Maximum viewing distances

$$d_{14} = \frac{0.014\ \mathrm{m}}{0.0085} = 1.65\ \mathrm{m},$$
$$d_{9} = \frac{0.009\ \mathrm{m}}{0.0085} = 1.06\ \mathrm{m}.$$

Both are closer than a typical standing distance of $1.5$–$2\ \mathrm{m}$, so a
$14\ \mathrm{mm}$ body is marginal and a $9\ \mathrm{mm}$ caption is effectively a
visual element rather than text. If the caption carries the result, it must be larger;
if it is only a label, it does not need to be read.

---

## ★2 — Minimum height at $2.0\ \mathrm{m}$

$$h_{\min} = 2.0 \times 0.0085 = 0.0170\ \mathrm{m} = 17.0\ \mathrm{mm}.$$

$10\ \mathrm{mm}$ text is legible from $1.18\ \mathrm{m}$ — barely, and only if the
visitor stands directly in front of that panel, which blocks it for everyone else.
The choice is therefore explicit: either set the body at $17$–$18\ \mathrm{mm}$ and
accept the reduced word budget, or plan for close reading and expect only the title
and figures to work at distance.

---

## ★3 — Capacity and the scaling rule

$$N_{10} = 1.00\ \mathrm{m^{2}} \times 420 = 420\ \text{words},$$
$$N_{20} = 1.00 \times 420 \times \left(\frac{10}{20}\right)^{2}
= 420 \times 0.25 = 105\ \text{words}.$$

The rule is $N \propto h^{-2}$: doubling the text height quarters the capacity.
This is why "make the text bigger" and "keep the detail" cannot both be satisfied,
and why the decision about what to leave out is forced rather than optional.

---

## ★4 — Session capacity

$$N_{\max} = \frac{120}{2.5} = 48\ \text{engaged visitors if never free},$$
$$N_{\text{realistic}} = 0.5 \times 48 = 24,$$
$$\text{engaged fraction} = \frac{24}{250} = 9.6\%.$$

About one passer-by in ten stops long enough to take in the poster, which sets the
design target: the poster must deliver its claim in the first ten seconds and its
evidence in the next two minutes, because that is the budget of the visitors who
actually engage.

---

## ★5 — Two-element readership

Under independence, the expected count of visitors reading both figures and body
text is

$$90 \times 0.667 \times 0.222 = 13.3 \approx 13\ \text{visitors}.$$

Independence is an approximation — a visitor who engages deeply reads both, so the
true joint count is probably above $13$ — but the order of magnitude is the point:
the body text reaches about one visitor in seven. The primary result must therefore
appear in the **figure** and in the **title or a heading**, with the body text as
supporting detail for the small minority who engage.

---

## ★6 — The text size needed for $150$ words

The density rule gives capacity $N = A \times 420 \times (10/h)^{2}$ words with $h$
in mm. Solving for $h$ at $N = 150$ and $A = 1.00$:

$$\left(\frac{10}{h}\right)^{2} = \frac{150}{420} = 0.357
\;\Rightarrow\; \frac{10}{h} = 0.598
\;\Rightarrow\; h = 16.7\ \mathrm{mm}.$$

That is legible from

$$d = \frac{0.0167}{0.0085} = 1.96 \approx 2.0\ \mathrm{m},$$

so $150$ words at $17\ \mathrm{mm}$ is exactly the design that works at $2\ \mathrm{m}$
— a useful coincidence to remember: about $150$ words of body text is the honest
budget of an A0 poster read at two metres.

---

## ★7 — Do self-contained captions increase dwell time?

**Unit.** One visitor–poster encounter, in a session containing posters of both kinds
(with and without self-contained captions).

**Outcome.** Dwell time in seconds, measured by a discreet observer with a stopwatch
or by a passive sensor, together with whether the visitor read the caption (observable
as time spent facing the caption panel).

**Instrument.** Two observers with a written definition of the start and end of an
encounter; a $10\%$ double-coded pilot with the agreement reported. Anonymous
observation raises an ethics question: observe only in a public session with a notice,
record no identifying information, and report only aggregate times.

**Confound.** The topic. Visitors stop at posters whose subject they already care
about, and captions correlate with well-designed posters, which correlate with
important results. Control by (a) pairing each poster with a version that differs only
in its caption — a within-poster, between-visitor design — and (b) recording a
topic-interest proxy (the poster's subject area) and analysing it as a covariate.

---

## ★8 — The viewing-distance distribution

**Measurement.** For each poster, at the moment of an encounter, estimate and record
the distance from the visitor's eyes to the poster plane. Practical instruments: a
floor grid marked in half-metre bands (least intrusive, coarse) or a laser rangefinder
at sampled moments (accurate, intrusive). Record the distance at the moment of
closest reading.

**Sample.** At least $200$ encounters across at least $15$ posters, so that
poster-to-poster variation can be separated from the overall distribution; report both
the pooled distribution and the per-poster medians.

**Statistic.** The median and the 5th percentile of the distance distribution. The
median sets the text size for the body, and the 5th percentile is the distance at
which the poster sees its closest readers — the captions and detail panels can be set
for the 5th percentile rather than the median, which recovers some word budget.

**Consequence for the rule.** If the measured median is $1.2\ \mathrm{m}$ rather than
the assumed $1.5$–$2.0$, the minimum text height falls from $17\ \mathrm{mm}$ to
$1.2 \times 0.0085 = 10.2\ \mathrm{mm}$, roughly tripling the word budget
($N \propto h^{-2}$). A single afternoon of measurement therefore changes the design
decision more than any style guide, which is the strongest argument for doing it.
