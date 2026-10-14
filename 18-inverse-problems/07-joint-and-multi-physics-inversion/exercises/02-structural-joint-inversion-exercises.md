# Exercises — 18-07-02 Structural (Cross-Gradient) Coupling

Attempt these before reading the
[solutions](./02-structural-joint-inversion-solutions.md). The lesson is
[02 Structural (Cross-Gradient) Coupling](../02-structural-joint-inversion.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For $\mathbf{m}_1 = (x+2y)$ and $\mathbf{m}_2 = (3x+6y)$ on a unit grid
($\Delta x = \Delta y = 1$), compute $\partial_x m_1$, $\partial_y m_1$,
$\partial_x m_2$, $\partial_y m_2$ and the cross-gradient $t$. State whether the
two fields share geometry.

**★2.** Repeat ★1 for $\mathbf{m}_2 = (3x-6y)$ and state the sign of $t$ and what
the sign means geometrically.

**★3.** Give the cross-gradient of two constant fields and explain in one
sentence why this matters for the penalty $\lambda_x\sum t_i^2$.

## ★★ Applied

**★★4.** Using the demonstration's sweep, state the weight $\lambda_x$ you would
choose if the requirement were "neither misfit may rise by more than 10% of its
uncoupled value", and justify it with the printed numbers. State what you give
up in return.

**★★5.** Verify the scaling identity for $\alpha = 3$, $\beta = 2$ by reasoning
about the definition of $t$ (no computation needed), and then state one
practical consequence for a study in which one property is measured in
g cm$^{-3}$ and the other in $\Omega$ m.

**★★6.** In the inconsistent-truth experiment, at $\lambda_x = 100$ the error of
model 2 is 0.0753 against 0.0222 uncoupled (a factor of 3.4), while misfit 2
rises from 0.0107 to 0.0315 (a factor of 2.9). Explain why a practitioner who
only watched the forward-modelled predictions would not see the problem, and
what diagnostic would.

## ★★★ Research-oriented

**★★★7.** Design an experiment that separates "the coupling failed because the
structures differ" from "the coupling failed because the weight was too large".
Specify the diagnostic quantity, the control experiment, and the decision rule.
A specification that could not be executed is a failed answer.

**★★★8.** The penalty is amplitude-blind and has a flat global minimum. Propose
a modified penalty that keeps the orientation information but removes the flat
minimum, write it as a formula, and state the new failure mode you have
introduced.
