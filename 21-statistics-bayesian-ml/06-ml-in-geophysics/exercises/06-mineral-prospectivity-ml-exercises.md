# Exercises — 21-06-06 ML for Mineral Prospectivity Mapping

Attempt these before reading the
[solutions](./06-mineral-prospectivity-ml-solutions.md). The lesson is
[06 Mineral Prospectivity](../06-mineral-prospectivity-ml.md). All values are
**SYNTHETIC**, printed by
[`code/mineral_prospectivity_ml_demo.py`](../code/mineral_prospectivity_ml_demo.py).

Measured quantities: grid 60 × 60 cells of 1 km (3 600 cells); evidence fields
smoothed at $\sigma = 6$ cells; 95 deposits drawn with probability proportional to
$\mathrm{sigmoid}(\text{latent})$; 800 negatives in every design; 4 × 4 spatial
blocks of 15 × 15 cells; model = logistic regression on four standardised
layers.

| negative design | AUC, 5 random folds | AUC, leave-one-block-out | difference |
|---|---|---|---|
| uniform random cells | $0.619$ | $0.612$ | $+0.007$ |
| cells within 3 cells of a deposit | $0.513$ | $0.539$ | $-0.026$ |

Targeting efficiency of the uniform-negative model: the top 10% of all 3 600
cells captures $0.116$ of the deposits.

## ★ Foundational

**★1.** Compute the number of cells in a 10% exploration budget, the number of
cells a *random* selection of that size would be expected to contain deposits
from, and hence the uplift of the model. Then express the captured fraction as
the number of deposits.

**★2.** Compute the AUC change attributable to the negative design and the
largest AUC change attributable to the fold design. State the ratio, and say
which choice a methods section must describe first.

**★3.** The evidence fields are smoothed with $\sigma = 6$ cells and a matched
negative is drawn within 3 cells of a deposit. Compute the ratio of the matching
radius to the correlation length and state, in one sentence, what that ratio
implies about the separability of a matched negative from a deposit.

## ★★ Applied

**★★4.** Derive the relation between the AUC and the target quantity of
interest: show why an AUC computed against uniform random negatives is an
average over a negative population whose "distance from a deposit" distribution
is dominated by far cells, and hence why it is an upper bound on the AUC against
matched negatives. State the quantity that would replace it for a decision-maker.

**★★5.** Design the block-size sensitivity study. State the block sizes, the
metric, the plot, the prediction for a district whose correlation length is
6 cells, and the rule you would use to choose the block size for a new district.

## ★★★ Research-oriented

**★★★6.** Design the leave-one-out distance-to-deposit feature so that it can be
used without leaking the held-out block's labels, and state exactly which
deposits are used for each cell under a spatial block split. Then state what the
feature still leaks and why that leak cannot be removed by any fold design.

**★★★7.** Design the experiment that measures the inventory reporting bias. State
how you would simulate an access-biased inventory, the metric, and the observed
pattern that would show the bias is being learned rather than the geology.

**★★★8.** A study reports an out-of-sample targeting efficiency of $1.16\times$
at a 10% budget and claims economic significance. Specify the additional
information — geological, economic and statistical — needed to evaluate the
claim, and the result that would falsify it.
