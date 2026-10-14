# Solutions — 24-04-03 Seminars, Qualifying Exams and Thesis Defence

> Read after attempting. Numbers computed. Lesson:
> [03 Seminars, Qualifying Exams and Thesis Defence](../03-seminar-and-defence.md).

---

## ★1 — Questions that fit

Question time $= 50 - 15 = 35$ minutes.

$$\text{at } 3.5\ \mathrm{min}: \frac{35}{3.5} = 10.0\ \text{questions},$$
$$\text{at } 1.5\ \mathrm{min}: \frac{35}{1.5} = 23.3 \approx 23\ \text{questions}.$$

The word total is identical in both cases ($35 \times 130 = 4550$ words); what
changes is how much of the panel's agenda is reached. Thirteen questions unasked is
the cost of long answers, and those are exactly the questions the candidate did not
choose.

---

## ★2 — Coverage and marginal gain

$$C(12) = 1 - e^{-1} = 0.632,\qquad C(24) = 1 - e^{-2} = 0.865,\qquad
C(36) = 1 - e^{-3} = 0.950 .$$

Marginal gain from $24$ to $36$:

$$0.950 - 0.865 = 0.085 = 8.5\ \text{percentage points for twelve more answers}.$$

The first twelve answers bought $63.2$ points; the second twelve bought $23.3$; the
third twelve bought $8.5$. Preparation should therefore cover every area at least
once before it deepens any area, and the knee of the curve is around $20$–$24$
answers.

---

## ★3 — Three-part answer

- **Direct answer:** "The $0.5$–$2.0\ \mathrm{s}$ band is where the dispersion curve
  is measured with an acceptable signal-to-noise ratio."
- **Reason:** "Below $0.5\ \mathrm{s}$ the array's station spacing aliases the
  short-wavelength modes, and above $2.0\ \mathrm{s}$ the coherent part of the noise
  field is weaker than the ambient floor on this array. Both effects are visible in
  the coherence plots in §4.2."
- **Limit:** "If the array were denser, the lower bound could be extended to about
  $0.3\ \mathrm{s}$, which would change the shallowest resolved velocity by a few
  per cent."

Ninety seconds, one claim, one piece of evidence, one boundary. The structure is
visible to the panel, which is what allows them to judge the reasoning rather than
the confidence.

---

## ★4 — Probability of a low-weight area

Each of the two areas has probability $p = 0.08$ of being asked. The probability that
neither appears in $n$ independent draws is $(1 - 0.16)^{n}$, so

$$n = 6:\quad P(\text{at least one}) = 1 - 0.84^{6} = 1 - 0.3513 = 64.9\%,$$
$$n = 12:\quad P(\text{at least one}) = 1 - 0.84^{12} = 1 - 0.1234 = 87.7\%.$$

So an $8\%$ area is not a small risk at the scale of a single examination: in a
six-question panel it appears nearly two times in three. The remedy — two prepared
sentences per area — costs minutes and removes most of the exposure.

---

## ★5 — Questions answered at two paces

$$N_{4.5} = \frac{30}{4.5} = 6.7 \approx 7, \qquad
N_{2.5} = \frac{30}{2.5} = 12.0 .$$

Difference: about $5$ questions, against a plausible agenda of $10$ — half the panel's
questions. Framed as coverage of the agenda:

$$\frac{6.7}{10} = 67\% \quad \text{versus} \quad \frac{12}{10} = \text{all of it}.$$

This is the strongest practical reason to rehearse answers to 90 seconds: the panel
does not ask fewer questions because you are slow, it asks the same questions and
learns less about you.

---

## ★6 — Correcting a wrong premise

1. **Correction:** "The model is spherical rather than flat, so the geometric
   approximation you describe does not apply here."
2. **Quantitative consequence:** "With a flat-Earth assumption the phase shift at
   this distance would be about $3\%$; the spherical model gives $0.2\%$, which is
   within the measurement uncertainty."
3. **The question you think they meant:** "The substantive question, I think, is
   whether the geometric approximation biases the velocity estimate."
4. **Answer:** "It does not, because the bias enters as a common factor across
   stations and cancels in the differential measurement; I verified this against a
   synthetic model where the answer is known, and the recovery was within $2\%$."

Two rules: keep the correction to one sentence, and always end by answering a
question. A candidate who only corrects the premise looks evasive; one who corrects
and then answers looks precise.

---

## ★7 — Does adversarial rehearsal help?

**Unit.** One candidate in one defence.

**Outcome.** The number of questions the candidate could not answer — defined before
the analysis as questions where the candidate said they did not know or gave no
substantive reply — extracted from the recording by two blinded coders.

**Design.** Cluster-randomised by cohort or programme: cohorts either receive a
mandatory adversarial rehearsal with trained questioners, or follow existing practice.
Individual randomisation is not ethical here, because withholding a preparation
intervention from an individual candidate could affect their examination outcome; a
cohort-level design with the intervention offered to the control cohort after the
study period is the defensible version.

**Sample size.** Difference $1.5$ questions, standard deviation $1.8$:

$$n\ \text{per arm} = \frac{2(1.96 + 0.842)^{2}\times 1.8^{2}}{1.5^{2}}
= \frac{2\times 7.851\times 3.24}{2.25} = 22.6 \approx 23\ \text{candidates per arm}.$$

**Ethical constraint.** Randomising candidates affects their examination, which is a
high-stakes assessment. The constraints are: offer the intervention to all cohorts
eventually, obtain consent for the study rather than for the rehearsal (which is part
of normal supervision), measure an outcome that does not alter the examination's own
outcome (a research assistant's coding of a recording, not the examiners' marks), and
have the design reviewed before the first cohort.

---

## ★8 — Distribution of question areas

**Sampling.** All defences in a department over a stated window, with the examinees'
consent, recorded and transcribed; report the flow from all defences to those with
usable recordings, since consent may correlate with outcome.

**Coding unit.** One question (or one substantive examiner turn, since some turns
contain two questions). Each question coded into one of the eight areas with a
codebook that defines the boundaries — the boundary between "method choice" and
"assumptions and limitations" is the one that needs the most care, because questions
about an assumption often begin as questions about the method.

**Agreement.** Two coders on a $20\%$ pilot, Cohen's $\kappa$ with a target of
$\geq 0.6$ for the eight-way code, and a cheaper fallback: collapse to four
super-areas if the eight-way agreement is below target, and report both.

**Using the result.** Report the per-area proportions with Wilson intervals.
A candidate's preparation priority follows directly: areas with high weight and low
prior fluency first, ordered by the product of the two. The study is worth doing in a
department because the weights are local — different committees ask different
questions — and every cohort repeats the exercise on its own.
