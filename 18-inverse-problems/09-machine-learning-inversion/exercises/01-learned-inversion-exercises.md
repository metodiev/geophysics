# Exercises — 18-09-01 Learned Inversion: Direct and Iterative Networks

Attempt these before reading the
[solutions](./01-learned-inversion-solutions.md). The lesson is
[01 Learned Inversion: Direct and Iterative Networks](../01-learned-inversion.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the empirical-risk objective for a direct learned inverse and mark
which factor introduces the prior distribution $p(\mathbf{m})$.

**★2.** State the network architecture, parameter count and training time used in
the demonstration, and the in-distribution MSE of the network and the linear
reference.

**★3.** Define "out of distribution" for this problem in terms of the training
ensemble, and give one example family used in the demonstration.

## ★★ Applied

**★★4.** The network beats the linear inversion by a factor 1.6 in rms
in-distribution. Explain, in terms of the objective, why the advantage does not
come from the operator $G$ (which both methods are given).

**★★5.** Compute the ratio of the network's out-of-distribution error to the
linear method's error on the 8-mode set, and state in one sentence what the
figure means for deployment.

**★★6.** The network's forward pass costs 2.0 µs and the linear solve 0.5 µs,
with 0.07 s of training. For a study that will invert 10 data sets of the same
size, compute which method has the lower total cost, and state the number of
data sets at which the comparison reverses.

## ★★★ Research-oriented

**★★★7.** Design an experiment that would determine whether a deployed learned
inverse is being used inside its training distribution, given only real data and
no labels (the true models are unknown). Specify the diagnostic you would compute
and the decision rule. A specification that could not be executed is a failed
answer.

**★★★8.** An iterative network unrolls a proximal-gradient scheme for a fixed
number of steps. Argue whether unrolling changes the distributional argument of
§1 at all, and construct a case in which the unrolled network's error is
*controlled* by the physics rather than by the ensemble.
