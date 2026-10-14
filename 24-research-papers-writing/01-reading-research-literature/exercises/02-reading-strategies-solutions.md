# Solutions — 24-01-02 Reading Strategies

> Read after attempting. Numbers computed. Lesson:
> [02 Reading Strategies](../02-reading-strategies.md).

---

## ★1 — Expected confusion counts at $N = 120$, $p = 0.20$

Relevant $R = 0.20 \times 120 = 24$; non-relevant $N - R = 96$.

$$N_{\mathrm{TP}} = 0.85 \times 24 = 20.4,
\qquad
N_{\mathrm{FP}} = (1-0.90)\times 96 = 9.6,$$
$$N_{\mathrm{FN}} = 0.15 \times 24 = 3.6,
\qquad
N_{\mathrm{TN}} = 0.90 \times 96 = 86.4 .$$

(Expected counts are not integers; the realised integer counts in any single queue
differ by sampling noise.)

$$\text{precision} = \frac{20.4}{20.4+9.6} = \frac{20.4}{30.0} = 68.0\%,
\qquad
\text{recall} = \frac{20.4}{24} = 85.0\%,$$
$$F_1 = \frac{2 \times 0.680 \times 0.850}{0.680 + 0.850} = 0.755 .$$

Number needed to screen $= 1/0.680 = 1.47$ papers per relevant hit.

---

## ★2 — Strategy costs

(a) Brute force: $120 \times 45\ \mathrm{min} = 5400\ \mathrm{min} = 90.0\
\mathrm{h}$.

(b) Two-pass: skim $120 \times 3 = 360\ \mathrm{min} = 6.0\ \mathrm{h}$, plus
$30.0$ screen positives $\times 45\ \mathrm{min} = 1350\ \mathrm{min} = 22.5\
\mathrm{h}$, total $28.5\ \mathrm{h}$.

$$\text{saving} = \frac{90.0 - 28.5}{90.0} = 68.3\%,$$

at the cost of $3.6$ relevant papers (expected). The saving is larger than the
lesson's $57.9\%$ because this queue is shorter and its screen is weaker on
false positives but stronger on sensitivity.

---

## ★3 — Yield per hour

$$\eta = \frac{y}{t}\times 60\ \mathrm{min/h}:$$

$$y = 0.20,\ t = 3\ \mathrm{min}: \eta = \frac{0.20}{3}\times 60
= 4.00\ \text{content-units/h};$$
$$y = 0.50,\ t = 12\ \mathrm{min}: \eta = 2.50\ \text{content-units/h};$$
$$y = 0.90,\ t = 40\ \mathrm{min}: \eta = 1.35\ \text{content-units/h}.$$

Yield falls steeply with pass cost, which is why triage is worthwhile: the cheap
pass captures enough to decide, and the expensive pass is reserved for the papers
where it is not replacing coverage but *adding* it.

---

## ★4 — Break-even of triage

Cost of triage over $N$ papers:

$$C_{\text{triage}} = N t_{\text{skim}} +
N\big[\text{sens}\,p + (1-\text{spec})(1-p)\big] t_{\text{deep}},$$

and brute force is $C_{\text{brute}} = N t_{\text{deep}}$. With the numbers given,
in minutes,

$$240\times 3 + 240\big[0.90p + 0.18(1-p)\big]\times 45 = 240 \times 45 .$$

Dividing by $240$: $3 + 45(0.18 + 0.72p) = 45$, so

$$0.18 + 0.72p = \frac{42}{45} = 0.9333
\;\Rightarrow\; 0.72p = 0.7533
\;\Rightarrow\; p = 1.046 .$$

Since $p \leq 1$, **no relevance rate achieves break-even**: at these costs the
two-pass strategy is cheaper even when every paper is relevant, because a $90\%$
sensitivity screen genuinely removes $10\%$ of the work and the false positives of
a $0.82$-specificity screen are not numerous enough to pay for it.

At $p = 0.25$, break-even requires $240 \times 3 + 240n_{\text{pos}}\times 45 =
240\times 45$, i.e. $n_{\text{pos}} = 224$ screen positives out of $240$ papers:

$$0.90 \times 60 + (1-\text{spec}) \times 180 = 224
\;\Rightarrow\; 1-\text{spec} = \frac{170}{180} = 0.944
\;\Rightarrow\; \text{spec} = 0.056 .$$

Only a screen that passes almost everything would fail to help.

---

## ★5 — Precision by Bayes' rule

$$\text{precision} = \frac{\text{sens}\,p}{\text{sens}\,p + (1-\text{spec})(1-p)}
= \frac{0.90 \times 0.25}{0.90\times 0.25 + 0.18 \times 0.75}
= \frac{0.225}{0.225 + 0.135} = 62.5\%.$$

The demonstration measures $64.7\%$, a difference of $+2.2$ percentage points. The
standard error of a proportion with $n = 85$ screen positives near $0.625$ is

$$\text{SE} = \sqrt{\frac{0.625 \times 0.375}{85}} = 0.0525 = 5.3\%,$$

so a $2.2$-point difference is $0.4$ standard errors: entirely consistent. The
analytic value is the better statement of the design; the measured value is one
draw from it.

---

## ★6 — A more careful skim

New content captured:

$$C_{B} = 240 \times 0.50 + 85 \times 0.95 = 120.0 + 80.75 = 200.75
\ \text{content-units},$$

against brute force $C_A = 240 \times 0.95 = 228.0$:

$$\frac{C_B}{C_A} = \frac{200.75}{228.0} = 88.0\%,$$

up from $67.0\%$. The cost is the extra skim time; if a careful skim takes
$6\ \mathrm{min}$ instead of $3\ \mathrm{min}$, the added time is
$240 \times 3\ \mathrm{min} = 720\ \mathrm{min} = 12.0\ \mathrm{h}$, taking the
two-pass total from $75.8\ \mathrm{h}$ to $87.8\ \mathrm{h}$ — still below the
$180.0\ \mathrm{h}$ of brute force. An extra $12\ \mathrm{h}$ buys $21$ percentage
points of content coverage, or $0.57\ \mathrm{h}$ per point.

---

## ★7 — Do triage false negatives matter?

**Population.** Papers published in the sources you actually scan, over a stated
window (for example six months), so that the false negatives are observable rather
than hypothetical.

**Follow-up.** Twelve months from the screening date.

**Outcome.** A triaged-negative paper counts as *should have been read* if it
(a) is cited by a paper you later wrote, or (b) is cited by two independent papers
in your field that you do regard as central, or (c) is incorporated into a
standard or a working group's report. Pre-register the exact list; a loose outcome
makes the study unfalsifiable.

**Sample size.** If the expected false-negative rate is $5\%$ of $300$ screened
papers ($15$ papers) and the "should have been read" rate among them is $20\%$,
you expect $3$ events. Estimating a proportion from $3$ events is hopeless, so the
study is only viable at a much larger screen (order $1500$ papers) or must be
reframed as a case series with a stated, non-estimable limitation.

**Irreducible bias.** Retrospective knowledge. Once the field moves, you know
which papers mattered, and that knowledge contaminates the judgement of whether
they mattered *at the time*. Report the outcome list as fixed in advance, and
acknowledge that the study measures "mattered eventually", not "should have been
read then".

---

## ★8 — Calibrating your own triage

**Design.** Screen $200$ records. For each, record the screen decision. Then
perform a deep read of a *random* $40\%$ of the screen negatives as well as the
positives, and label relevance from the deep read. Sensitivity and specificity are
then estimated on the labelled subsample, weighted back to the full set.

**Order matters.** Screen and record the decision *before* any deep read, and deep-
read the sampled negatives even when the screening note says "obviously
irrelevant". Otherwise the estimates are circular: you will have defined relevance
by the screen.

**Precision of the estimates.** For a sensitivity near $0.9$ and a target
half-width of $\pm 0.10$ at $95\%$ confidence,

$$n_{\text{relevant}} = \frac{z^{2}\hat p(1-\hat p)}{h^{2}}
= \frac{1.96^{2}\times 0.9 \times 0.1}{0.1^{2}}
= \frac{0.3457}{0.01} = 34.6 \approx 35\ \text{relevant papers}.$$

With an $R \approx 60$ relevant papers per $200$ records, and $40\%$ of negatives
deep-read, the labelled subset contains about $60 + 0.4 \times 140 = 116$ papers,
of which roughly $60$ are relevant — comfortably above $35$. For specificity near
$0.82$ at the same half-width:

$$n_{\text{non-relevant}} = \frac{1.96^{2}\times 0.82\times 0.18}{0.1^{2}}
= 56.6 \approx 57,$$

also satisfied. State both targets; a calibration that reports sensitivity with no
sample size has reported a number, not an estimate.
