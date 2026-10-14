# Exercises — 21-04-05 Decision Trees, Random Forests and Gradient Boosting

Attempt these before reading the
[solutions](./05-trees-and-ensembles-solutions.md). The lesson is
[05 Trees and Ensembles](../05-trees-and-ensembles.md). All data are
**SYNTHETIC**.

## ★ Foundational

**★1.** Compute the Gini impurity $G(p) = 2p(1-p)$ at $p = 0.5$, $p = 0.9$ and
$p = 1$, and state which value is the maximum.

**★2.** A node with $p = 0.5$ is split into a left child with $w_L = 0.5$ and
$p_L = 0.1$ and a right child with $p_R = 0.9$. Compute the gain
$\Delta = G(p) - [w_LG(p_L) + w_RG(p_R)]$.

**★3.** The demonstration's depth-5 tree has training accuracy $0.9600$ and test
accuracy $0.8900$; the depth-8 tree has $0.9900$ and $0.8800$. Compute both
train–test gaps and state which tree is overfitting.

## ★★ Applied

**★★4.** Using $\operatorname{Var} = \rho\sigma^{2} +
(1-\rho)\sigma^{2}/B$, compute the ensemble variance for $\rho = 0.9$,
$\sigma^{2} = 1$ and $B = 100$, and state what happens in the limits
$B \to \infty$ and $\rho \to 0$.

**★★5.** Derive the gradient-boosting update for squared loss: show that the
negative gradient of $\frac12\sum_i(y_i - F(x_i))^{2}$ with respect to
$F(x_i)$ is the residual, and state the update $F_m = F_{m-1} + \nu h_m$.

**★★6.** The demonstration's boosting residual falls from $1.40289$ at round 1 to
$0.07656$ at round 10 and $0.05947$ at round 200, with a noise floor of $0.04$.
Compute the reduction per decade of rounds and the fraction of the floor reached.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures the **correlation between bagged
trees** as a function of the number of features considered at each split, and its
effect on ensemble accuracy. State the design, the metric, the replicate count,
and the prediction for the accuracy as the feature subset grows. A specification
that could not be executed is a failed answer.

**★★★8.** Design a study of **boosting under label noise**: an experiment that
measures the optimal number of rounds (by validation error) as a function of the
label-noise fraction. State the noise levels, the metric, the replicate count, and
the predicted direction of the shift in the optimal round count.
