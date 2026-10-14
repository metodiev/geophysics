# Solutions — 23-01-04 Permits, Land Access, Cultural Heritage and Ethics

> Read after attempting. Lesson:
> [04 Permits and Ethics](../04-permits-and-ethics.md). All values are
> **SYNTHETIC**.

---

## ★1 — The chain of 40 approvals

$$P(\text{all agreed}) = 0.85^{40} .$$

$\ln 0.85 = -0.162519$, so $40 \times (-0.162519) = -6.500760$ and

$$0.85^{40} = e^{-6.500760} = 0.001502 \;(0.150\ \%).$$

$$\mathbb{E}[\text{refusals}] = 40 \times 0.15 = 6.0 .$$

$$P(\ge 1 \text{ refusal}) = 1 - P(\text{all agreed}) = 1 - 0.001502 = 0.9985 .$$

So a 15 % per-parcel refusal probability produces a 99.85 % chance that the
survey is *not* complete — and an expected six refusals to manage.

---

## ★2 — Per-parcel probability for 95 % overall

$$p_{\text{required}} = 0.95^{1/40} = e^{\ln(0.95)/40}
= e^{-0.0512933/40} = e^{-0.00128233} = 0.998718 .$$

That is **99.87 % per parcel**. No realistic negotiation achieves it, which is the
quantitative statement of the lesson's point: the response to a low $p^{M}$ is a
change of design (parcel-level deliverables, reduced $M$, a negotiating route with
a representative body where one legitimately exists), not more persuasion.

---

## ★3 — Buffer arithmetic

Excluded width: $d + 2b = 20 + 2(15) = 50\ \mathrm{m}$.

Growth factor:

$$F = \frac{d + 2b}{d} = \frac{50}{20} = 2.50 .$$

Excluded fraction of the survey area, where the unbuffered zone coverage is
$a = 0.8\ \%$:

$$a_{\text{excluded}} = F\,a = 2.50 \times 0.8\ \% = 2.0\ \%.$$

The buffer therefore removes 2.0 % of the survey area where the zones themselves
remove 0.8 % — the buffer accounts for 1.2 percentage points, more than half the
loss. On a 3 km² survey that is 0.060 km² excluded, of which 0.036 km² is buffer.

---

## ★★4 — Probability that a line clips a zone

With $n = 150$ segments and areal coverage $a = 0.008$:

$$P(\text{clip}) = 1 - (1-a)^{n} = 1 - 0.992^{150} .$$

$\ln 0.992 = -0.0080322$, so $150 \times (-0.0080322) = -1.20483$ and
$0.992^{150} = e^{-1.20483} = 0.29974$. Therefore

$$P(\text{clip}) = 1 - 0.29974 = 0.7003 .$$

Expected clipping lines out of 90: $90 \times 0.7003 = 63.0$ lines, with binomial
scatter $\sqrt{90 \times 0.7003 \times 0.2997} = 4.35$, so a realised value
between 54 and 72 would be unremarkable.

Note how insensitive this is to the doubt about $a$: halving the coverage to
0.4 % gives $1-0.996^{150} = 0.4519$, still nearly half the lines. Because the
line is long relative to the zone, the probability saturates — the practical
consequence is that mask-based checking is mandatory, not optional.

---

## ★★5 — Resolution over eight weeks

With $K = 12$ parcels and $p_w = 0.35$, the probability that a *given* parcel is
still unresolved after $n = 8$ weeks is

$$(1-p_w)^{n} = 0.65^{8} .$$

$\ln 0.65 = -0.430783$, so $8 \times (-0.430783) = -3.44626$ and
$0.65^{8} = e^{-3.44626} = 0.031855$.

$$\mathbb{E}[\text{unresolved}] = 12 \times 0.031855 = 0.382 \text{ parcels},$$

$$P(\text{all resolved}) = \left(1 - 0.65^{8}\right)^{12}
= 0.968145^{12} = e^{12 \times \ln 0.968145} = e^{-0.388476} = 0.6780 .$$

**Why the two numbers differ in meaning.** The expectation of 0.382 says that the
*typical* outcome is that everything is resolved — it weights a state with one
outstanding parcel and a state with none the same way as far as the sum is
concerned. The probability of 0.678 says that in about one planning case in three
something is still outstanding, and a single outstanding parcel may be the one on
the access road. A mobilisation decision needs the second number.

---

## ★★6 — Consent protocol at 30 parties

$$P(\text{all consent}) = 0.90^{30} .$$

$\ln 0.90 = -0.105361$, so $30 \times (-0.105361) = -3.160820$ and
$0.90^{30} = e^{-3.160820} = 0.042391$.

| Protocol | Publishable fraction |
|---|---|
| All-or-nothing (every party must consent) | 0.042391, i.e. 4.24 % |
| Parcel-level (each party governs its own data) | 0.90, i.e. 90 % |

Ratio $= 0.90/0.042391 = 21.2$. So the design of the protocol, not the parties'
willingness, changes the released data by a factor of 21.

Both numbers are conditional on the *same* underlying willingness. If a
particular community's decision is collective — which is its right — then the
collective outcome is the correct outcome, and the arithmetic above is not a
reason to seek individual consent instead. The arithmetic is a reason to decide
the data model in advance so that whatever is agreed can be honoured.

---

## ★★★7 — Engagement process with free, prior and informed consent

**Sequence of steps.**

1. **Identification and introduction.** Determine which peoples and communities
   have rights, interests or customary ties to the area, and reach them through
   their own representative structures. Do not start with a landowner registry
   alone.
2. **Early notification, before any activity.** Explain the objective, the methods
   (including what will be put in the ground and for how long), the area, the
   schedule, the risks, and who benefits. This is the "prior" requirement:
   consultation precedes, rather than ratifies, the work.
3. **Information in an accessible form.** Plain-language documents and
   face-to-face meetings in the community's preferred language, with time for
   independent advice — the "informed" requirement.
4. **Community-led review.** Allow the community to set conditions: excluded
   areas, timing relative to cultural or seasonal practice, monitoring roles,
   employment, and the treatment of cultural information.
5. **Agreement.** A written agreement covering access, data ownership and
   stewardship, publication and embargo, cultural-data handling, benefit sharing,
   and dispute resolution, signed by the appropriate authority.
6. **Notification of findings.** Report results back before publication, and
   again after, in a form the community can use.
7. **Ongoing consent.** Consent is maintained, not collected: new uses, new
   publications and new personnel are new conversations.

**Documents that result.** A consultation log with dates and attendees; the
plain-language information sheet; the agreement with its schedules (access map,
excluded areas, data clauses); a data-sharing or data-sovereignty annex naming
who decides on release and who holds copies; and a benefit-sharing statement.

**Three metrics for the funder.** (i) *Consent coverage* — fraction of the
intended survey area covered by a signed agreement (dimensionless). (ii)
*Consultation lead time* — weeks between first contact and the agreement, which is
the quantity that has to be scheduled. (iii) *Cultural-data actions completed* —
count of agreed handling measures implemented before, during and after the field
work, with the date of each.

**What the process cannot guarantee.** (i) That all members of a community agree;
a legitimate process can still leave disagreement, and the agreement must come
from the recognised authority. (ii) That the scientific result will be what the
community hoped for — the science is not a bargaining chip and must not be
presented as one. Equally, it cannot guarantee that the team's interpretation of
consent is correct; that is why the agreement is written down and revisited.

**The design decision that precedes negotiation.** Whether the data can be held,
published or embargoed **at parcel level** (Section 5 of the lesson). If the
dataset is one indivisible object, then any partial refusal destroys the whole
release, and no consultation protocol can recover from it. Deciding the data
model first turns a 4 % outcome into an 85–90 % outcome without touching anyone's
rights.

---

## ★★★8 — Cultural-heritage risk assessment for a 3 km² survey

**Data sources.** (i) The statutory heritage register and any interim or
development-protection listings for the area, requested in writing from the
heritage authority. (ii) The archaeological assessment required by that authority
for ground disturbance. (iii) Community-provided information about places of
significance, recorded and handled under the agreement's confidentiality terms —
these locations are usually **not** publishable, so they are held as a restricted
mask rather than in the open dataset. (iv) Historical maps, aerial photography and
lidar-derived relief models that may show earthworks. (v) Utility
easements and pipeline or cable corridors, which are excluded for engineering
reasons.

**Metric.** Expected clipped line-km,

$$\mathbb{E}[\text{clipped line-km}] = N_{\text{line-km}}
\times \left[1 - (1-a_{\text{eff}})^{L/\ell}\right],$$

with $a_{\text{eff}}$ the *buffered* coverage from ★3, $L$ the line length and
$\ell$ the segment length used for the calculation.

**Worked value.** Take $a = 0.008$ unbuffered, a buffer chosen so that
$F = 2.5$, so $a_{\text{eff}} = 0.020$; lines of $L = 200\ \mathrm{m}$ with
$\ell = 5\ \mathrm{m}$ ($n = 40$ segments):

$$P(\text{clip}) = 1 - 0.98^{40} = 1 - e^{40 \ln 0.98}
= 1 - e^{-0.808250} = 1 - 0.44570 = 0.5543 .$$

For a 3 km² block with 30 m line spacing, $N_{\text{line-km}} = 3/0.03 = 100$
line-km = 500 lines of 200 m. Expected clipped lines
$= 500 \times 0.5543 = 277$, and since clipping flags a line for review rather
than deleting it, the *expected deleted line-km* is smaller: it is the product of
the buffered zone length intersected per line and the number of lines, i.e.
approximately $100\ \mathrm{km} \times a_{\text{eff}} = 100 \times 0.020
= 2.0\ \mathrm{line\text{-}km}$ deleted (2 % of the programme), with 277 lines
requiring a check and a shorter re-plan.

**Choosing the buffer.** The trade is explicit: deleted line-km grows linearly in
$F$, and $F$ grows linearly in $b$. Writing
$F(b) = (d + 2b)/d$ with $d$ the zone width, the deleted length is
$N_{\text{line-km}}\,a\,F(b)$, so the marginal cost of widening the buffer by
1 m is $2N_{\text{line-km}}\,a/d$ line-km. Set that against the risk reduction the
wider buffer buys, which is a judgment that must be made with the heritage
authority and, where applicable, the community — not by the survey team alone. In
practice the decision is recorded as: the mask used, the buffer, the authority
that specified it, and the line-km lost as a result.

**Three limitations.** (i) **Registers are incomplete**: they record what is known
and reported, so a zero-overlap mask is not evidence of an empty area — this is
why the stop-work and find-reporting procedure exists regardless of the mask.
(ii) **Uncertainty in zone geometry**: surveyed boundaries may be approximate, and
the true extent may be larger than the polygon. (iii) **Confidential locations**
cannot be shown on published maps or in open data, so a reader of the final
product cannot verify the exclusions — the assessment must therefore be reported
as a summary (count of exclusions, line-km lost, authority consulted) rather than
as a reproducible map.
