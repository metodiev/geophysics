# Exercises — 21-04-02 Bias-Variance Trade-Off

Attempt these before reading the [solutions](./02-bias-variance-solutions.md). The
lesson is [02 Bias-Variance](../02-bias-variance.md). All data are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the bias-variance decomposition of the expected squared prediction
error and name each term.

**★2.** A model with $p = 10$ parameters is fitted to $n = 25$ points with noise
variance $\sigma^{2} = 0.09$. Compute the expected training MSE
$\sigma^{2}(1 - p/n)$ and test MSE $\sigma^{2}(1 + p/n)$ for an uninformative
model, and compare the first with the demonstration's measured $0.0477$.

**★3.** The demonstration's degree-9 decomposition gives bias² $= 0.35657$,
variance $= 293.86961$ and noise $0.09000$. Compute the percentage of the total
attributable to each term.

## ★★ Applied

**★★4.** Explain why the training error falls monotonically with model complexity
while the test error does not, using the decomposition rather than a verbal
argument.

**★★5.** The test MSE rises from $0.1098$ at degree 5 to $59.1868$ at degree 9
and $1.27\times10^{5}$ at degree 12. Compute the ratios and state what part of
the increase is statistical variance and what part is numerical ill-conditioning.

**★★6.** A model has a small train-test gap and a high error on both. Diagnose
the failure, state which term dominates, and give two remedies.

## ★★★ Research-oriented

**★★★7.** Specify a **learning-curve study** that separates bias from variance
for a stated model class: an experiment that measures test error as a function of
training-set size, at fixed and varying complexity. State the metric, the sizes,
the replicate count, and the predicted shape of the curves in the bias-dominated
and variance-dominated regimes. A specification that could not be executed is a
failed answer.

**★★★8.** Design an experiment that measures how the **optimal complexity**
depends on the noise level $\sigma$ for the demonstration's truth function. State
the noise levels, the metric, the replicate count, and the predicted direction of
the shift in the optimal degree.
