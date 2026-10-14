# Exercises — 25-06-05 Capstone: Presentation, Defence and Peer Critique

Attempt these before reading the
[solutions](./05-capstone-defence-solutions.md). The lesson is
[05 Capstone Defence](../05-capstone-defence.md); all numbers are **SYNTHETIC** and
printed by [`code/capstone_defence_demo.py`](../code/capstone_defence_demo.py):

| Quantity | Value |
|---|---|
| claim | $H = 35.00 \pm 2.00$ km (1 sd); 95% interval $\pm 3.91$ km |
| dominant assumption | $V_p/V_s = 1.75 \pm 0.03$, 47% of the variance |
| questions analysed | 8; 2 move the answer by more than 1 sd |
| $V_p/V_s = 1.70$ | $37.45 \pm 2.22$ km, swing 2.46 km $= 1.23$ sd |
| $V_p/V_s = 1.80$ | $32.85 \pm 1.82$ km, swing 2.16 km $= 1.08$ sd |
| $V_p$ 5% lower | $33.47 \pm 1.94$ km, swing 1.53 km $= 0.77$ sd |
| picking error 0.30 s | $35.00 \pm 2.90$ km, swing 0.90 km $= 0.45$ sd |
| 10 independent clusters | $35.00 \pm 3.02$ km, swing 1.02 km $= 0.51$ sd |
| ray parameter $+0.01$ s/km | $34.42 \pm 1.97$ km, swing 0.58 km $= 0.29$ sd |
| doubled systematic budget | $35.00 \pm 3.47$ km, swing 1.47 km $= 0.74$ sd |
| filter widens $t$ by 0.05 s | $35.40 \pm 2.03$ km, swing 0.40 km $= 0.20$ sd |
| measuring $V_p/V_s$ to $\pm 0.01$ | budget falls to about 1.51 km |

## ★ Foundational

**★1.** State the eight question forms of §2 and, for each, the element of the analysis
it tests.

**★2.** Compute the swing in standard deviations for a question that moves the central
value from $35.00$ to $33.47$ km with the quoted uncertainty of $2.00$ km, and state the
verdict rule that decides whether a prepared answer is required.

**★3.** The claim is $35.00 \pm 2.00$ km. Convert it into a sentence that names the
dominant assumption and its contribution, using the numbers in the table.

## ★★ Applied

**★★4.** For the $V_p/V_s = 1.70$ question, separate the swing into its two components
(the change in the central value and the change in the width) and state which of the two
a panel is more likely to challenge. Justify your answer with the numbers.

**★★5.** Rank the three questions in §3 of the demo by the risk they pose to the
*argument* rather than to the number, and explain why a question's ranking on the swing
table is not the same as its ranking on argument risk.

**★★6.** The 10-cluster question changes the width from 2.00 to 3.02 km while leaving
the central value unchanged. Compute the ratio of the two widths, verify it against the
$1/\sqrt{N}$ scaling, and state what the answer means for the independence of the
station set.

**★★7.** Write, word for word, the two answers you would give to the most dangerous
question: the short answer (with the number) and, if new data were needed, the boundary
statement. Then write the sentence you must *not* say, and explain why it is circular.

**★★8.** Draft the five-step peer critique of a capstone whose manuscript reports
$H = 35.04 \pm 1.20$ km with no uncertainty budget and no verification section. Each
step must be an action the recipient can take.

## ★★★ Research-oriented

**★★★9.** Build the question-impact table for your own capstone: at least eight
questions, each mapped to a re-computation of your own analysis, with the swing
measured against your own quoted uncertainty, the verdicts, and the two questions whose
answers require new data. Then state (a) the assumption your result is most vulnerable
to, (b) the measurement that would remove it, and (c) the sentence in your abstract that
would have to change if that measurement were made. A table whose swings are estimated
rather than recomputed is a failed answer.
