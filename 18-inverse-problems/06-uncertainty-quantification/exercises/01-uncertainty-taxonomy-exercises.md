# Exercises — 18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural

Lesson: [01 Taxonomy of Uncertainty](../01-uncertainty-taxonomy.md). Attempt these
before reading the [solutions](./01-uncertainty-taxonomy-solutions.md). All models
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the mean-square-error identity for a prediction that carries a
structural bias, an epistemic variance and an aleatory variance, and name each term.

**★2.** Using the demonstration's budget at $x^* = 6$ km — bias $0.1800$, epistemic
s.d. $0.0840$, aleatory s.d. $0.2000$ — compute the total RMSE and the bias share,
and check them against the printed table.

**★3.** An inversion gives $\sum x_i^2 = 100\ \mathrm{km^2}$ with
$\sigma = 0.1$ data units. Compute the epistemic standard deviation at
$x^* = 5$ km. State what it becomes if the aperture is doubled while the number of
stations is unchanged.

## ★★ Applied

**★★4.** The demonstration used the same eight extra stations two ways: doubling the
density inside $1$–$8$ km, or extending the aperture to $16$ km. Compute
$\sum x_i^2$ in each case, and the ratio of the resulting epistemic variances at
$x^* = 4$ km. State which design you would choose and why.

**★★5.** For the ill-conditioned SYNTHETIC design
$G = \begin{bmatrix}1&1\\1.01&1\end{bmatrix}$ with $\sigma = 0.05$, compute
$C_{\text{post}} = \sigma^2(G^{\top}G)^{-1}$ and its eigenvalues. Report the
standard deviation along the worst direction and compare it with the data noise
scale.

**★★6.** At a fixed prediction location, how much must $\sum x_i^2$ increase for the
epistemic standard deviation to halve? State the answer as a factor and as a
sentence about what the factor means in a field survey.

**★★7.** A colleague reports an uncertainty of $\pm 0.05$ km/s on a layer velocity
and calls it "the measurement error". List two other components that could be in
that number and state the diagnostic that would separate them.

## ★★★ Research-oriented

**★★★8.** Design a synthetic study that separates the three components in a
reflection-travel-time inversion. State the injected truths, the deliberate
structural omission, the observable you would compare, and the criterion that
declares each component separately recovered. A specification that could not be
executed is a failed answer.
