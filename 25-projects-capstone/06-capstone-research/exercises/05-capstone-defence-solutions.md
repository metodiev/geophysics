# Solutions — 25-06-05 Capstone: Presentation, Defence and Peer Critique

Reference solutions. Every number is printed by
[`code/capstone_defence_demo.py`](../code/capstone_defence_demo.py); the claim is
**SYNTHETIC**.

## ★1. The eight question forms and what they test

| question form | tests | evidence the answer should cite |
|---|---|---|
| "What exactly did you measure?" | the claim | the headline with its budget and the assumption it depends on |
| "Why that value of $X$?" | the design decisions | the tested range and the swing it produces |
| "How do you know the code is right?" | verification | the analytic check, the synthetic recovery, the coverage result |
| "What if the assumption is wrong?" | robustness | the recomputation, then the boundary: new data needed |
| "Why not method $Y$?" | awareness | the reason, and the study that used $Y$ on this problem |
| "What is the uncertainty?" | discipline | the budget with its statistical/systematic split |
| "What did you *not* establish?" | scientific judgement | a specific list of unestablished claims |
| "What next?" | the contribution | the measurement that would remove the dominant term |

The mapping matters because the *answer* must match the *form*: a robustness question
answered as a claim question ("the result is $35.0 \pm 2.0$ km") is heard as evasion,
even when the number is right.

## ★2. Swing in standard deviations and the verdict rule

$$\text{swing} = \frac{|33.47 - 35.00|}{2.00} = 0.77\ \text{sd}.$$

The demonstration's rule combines the change in the central value and the change in the
standard deviation,

$$\text{swing} = \sqrt{(\Delta H)^2 + (\Delta \mathrm{sd})^2},$$

and the verdict is **prepare an answer if the swing exceeds one standard deviation**.
For the $V_p$ question, $\Delta H = 1.53$ km and $\Delta \mathrm{sd} = 0.06$ km, giving
$1.53$ km $= 0.77$ sd: answerable on the fly (the recomputation takes milliseconds, the
number is in the table, and no rehearsal is needed). For $V_p/V_s = 1.70$ the swing is
$2.46$ km $= 1.23$ sd, above the threshold — and the reason is that the question
*changes the answer* by more than the result's own uncertainty, which is the definition
of a claim-breaking question.

## ★3. The claim sentence

> "The Moho depth beneath the array is $35.0 \pm 2.0$ km (1 sd), where the budget is
> dominated by the assumed $V_p/V_s = 1.75 \pm 0.03$, which contributes $47\%$ of the
> variance; a $V_p/V_s$ of 1.70 instead of 1.75 would give 37.5 km."

Three elements, all compulsory: the value, the budget, and the assumption that dominates
it. The trailing clause is optional but pre-empts the question that the table shows to
be the most dangerous — answering it before it is asked converts the most dangerous
question in the room into a demonstration that the candidate knows where their result
ends.

## ★★4. Decomposing the swing for $V_p/V_s = 1.70$

| component | baseline | at $V_p/V_s = 1.70$ | change |
|---|---|---|---|
| central value | 35.00 km | 37.45 km | $+2.45$ km ($+7.0\%$) |
| standard deviation | 2.00 km | 2.22 km | $+0.22$ km ($+11\%$) |
| quadrature swing | — | — | $\sqrt{2.45^2 + 0.22^2} = 2.46$ km $= 1.23$ sd |

The central value dominates the swing by a factor of eleven, and a panel is far more
likely to challenge it: the question "what if $V_p/V_s$ is 1.70?" is really the question
"is your number 35 km or 37.5 km, depending on something you did not measure?" That is a
challenge to the *claim*, whereas a change in width is a challenge to the *precision* —
and a panel can forgive a wide error bar far more easily than a value that moves by 7%
when an assumption moves by 3%.

## ★★5. Ranking by argument risk rather than by number

Demonstration order by swing: 1.70 (1.23 sd), 1.80 (1.08), $V_p$ (0.77), doubled
systematic (0.74), 10 clusters (0.51), picking error (0.45), ray parameter (0.29),
filter (0.20).

Ranking by argument risk is different, and the reason is instructive:

1. **The $V_p/V_s$ questions remain first**, because they attack the claim's honesty: if
   the answer moves 7% under a plausible alternative, the result must be *stated* as a
   conditional dependence, and a manuscript that reports a single number is exposed.
2. **The 10-cluster question rises above its 0.51 sd.** It does not change the number, it
   changes the *meaning* of $N$: if the 45 stations carry only 10 independent samples,
   the study's power claim from [25-06-01](./01-capstone-design-solutions.md) is
   invalid, and a design-level error is more damaging than a 0.5 sd numerical swing.
3. **The $V_p$ question falls.** A 5% error in an assumed constant is a known and
   expected limitation; the panel will accept "the regional $V_p$ is known to 2.5%,
   which is why the budget includes it".
4. **The filter-width question stays last**, because a 0.05 s shift in the picked time
   moves the result by 0.2 sd — the evidence that the processing choice is not the
   problem.

The general rule: **rank by what the question attacks** (the claim, the design, the
execution, or the presentation), then by the swing. A question that attacks the design
outranks a larger numerical swing.

## ★★6. The independence question

With $N$ independent samples the mean's standard error scales as $1/\sqrt N$, so reducing
$N$ from 45 to 10 multiplies the *statistical* part of the budget by

$$\sqrt{\frac{45}{10}} = 2.121.$$

The statistical contribution was 1.198 km, so it becomes $1.198 \times 2.121 = 2.541$ km,
and the total becomes

$$\sqrt{2.541^2 + 1.600^2} = \sqrt{6.457 + 2.560} = 3.003\ \mathrm{km},$$

against the printed 3.02 km — the small excess is the sampling error of the 20 000-draw
budget. The ratio of widths is $3.02/2.00 = 1.51$, against the predicted
$1/\sqrt{45/10}$-scaled quadrature ratio of $3.003/2.001 = 1.50$, so the arithmetic is
confirmed.

What it means: **$N$ is not the number of stations but the number of independent
measurements**, and a 300 km array with 10 km spacing may carry only 10 independent
samples. The demonstration's consequence is that the station count is a design variable
whose *effective* value must be argued from the correlation length (the Fresnel zone at
Moho depth, ~50 km, giving $300/50 = 6$–$10$ clusters), not assumed from the deployment
list.

## ★★7. The two answers, and the sentence never to say

**Short answer (with the number).**

> "That is in my table: with $V_p/V_s = 1.70$ instead of 1.75 the depth is
> $37.45 \pm 2.22$ km, a $7\%$ increase, and the budget widens by 11% because the ratio
> enters the slowness conversion directly. The 1.70 value is outside the $\pm 0.03$ range
> I used, which came from the regional compilation; if the local ratio were 1.70, every
> depth in this study would scale by the same factor."

**Boundary statement (new data needed).**

> "I cannot measure $V_p/V_s$ from this dataset without also assuming the $V_p$.
> A joint inversion of the receiver functions with the surface-wave dispersion at these
> stations would determine it to about $\pm 0.01$, which would reduce the budget from
> 2.0 km to roughly 1.5 km. That is the next study, and it is the measurement that would
> remove the dominant term rather than shrink it."

**The sentence never to say.**

> ~~"That is within the error bars."~~

It is circular because the quoted interval was computed *conditional on*
$V_p/V_s = 1.75 \pm 0.03$: the systematic budget already contains the effect of the
ratio varying *within* that range, so an alternative ratio *outside* it is not a draw
from the distribution the interval describes. The interval says nothing about the
consequence of a different ratio; the correct form of the answer is "that assumption
contributes 1.4 km of the 2.0 km budget, and a ratio outside the assumed range moves the
result by the 7% above".

## ★★8. Five-step critique of a manuscript claiming $35.04 \pm 1.20$ km

1. **Restate the claim.** "I understand the claim to be a Moho depth of
   $35.0 \pm 1.2$ km (1 sd). Is that the intended uncertainty on the depth, or the
   statistical uncertainty of the measurement?" — an action: ask them to confirm which
   quantity the interval covers.
2. **Identify the dominant assumption.** The manuscript has no budget, so the critique's
   first action is: "report the statistical/systematic split; the assumed $V_p/V_s$
   contributes more than half the variance in the comparable analysis I ran, so the
   $\pm 1.2$ km is likely a large understatement."
3. **Ask for the verification.** Action: "add the synthetic recovery and the interval
   coverage check to the Results section, and state the coverage percentage."
4. **Separate the three judgements.** (i) The analysis appears internally correct; (ii)
   it is *not* adequate for the claim as stated, because the interval excludes the
   dominant systematic term; (iii) the claim is interesting and worth fixing — say so
   explicitly, so the recipient knows the criticism is about (ii) and not (iii).
5. **Write actions, not preferences.** (a) report the budget with its split; (b) name
   the dominant assumption and its contribution in the abstract; (c) state the tested
   ranges of the filter width and the ray parameter; (d) cite the comparison value's
   uncertainty type; (e) re-run the audit after the changes.

The critique never says "the uncertainty is wrong" without quantifying: the actionable
statement is "the $\pm 1.2$ km is a statistical-only interval; the comparable budget
gives $\pm 2.0$ km, of which 1.6 km is systematic".

## ★★★9. Question-impact table for your own capstone

**The table.** For each question, the re-computation must be performed, not estimated;
the swing is measured against your own quoted uncertainty with the same rule as §2, and
each question gets a verdict. Two entries must be questions whose answers require new
data — the existence of such questions is the honest boundary of the study, and a table
with none of them is a table that has not looked.

**The three statements to attach.**

1. **The most vulnerable assumption.** For a depth or velocity result it is usually the
   one entering the conversion between the measured observable and the target quantity
   (a slowness ratio, a velocity, a density, a source term) rather than a
   processing choice, because the former multiplies the answer while the latter shifts
   it. State it as a name, a value, an uncertainty and a contribution in km or %.
2. **The measurement that would remove it.** Not "more data" but a specific
   observation: a joint inversion with a stated target precision, a borehole, a
   refraction profile, a published compilation with a stated uncertainty type. Give the
   measurement, the precision it would deliver, and the budget it would produce
   (1.51 km in this demonstration) so the panel hears a plan rather than a wish.
3. **The abstract sentence that would change.** In this capstone the sentence is
   "the Moho depth is $35.0 \pm 2.0$ km, dominated by the assumed $V_p/V_s$". If the
   ratio were measured, it becomes "the Moho depth is $35.0 \pm 1.5$ km, with the
   residual uncertainty split almost equally between the picking precision and the
   assumed $V_p$". Writing out the replacement sentence is the test that the candidate
   knows which part of their claim is conditional — and it is the answer to the
   question "what next?" that a panel will always ask.
