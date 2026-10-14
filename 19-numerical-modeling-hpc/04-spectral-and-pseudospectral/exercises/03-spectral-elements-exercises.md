# Exercises — 19-04-03 Spectral Element Methods and Their Geophysical Use

Attempt these before reading the
[solutions](./03-spectral-elements-solutions.md). The lesson is
[03 Spectral Element Methods and Their Geophysical Use](../03-spectral-elements.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the exactness degree of a $(p+1)$-node Gauss-Lobatto-Legendre rule
and compare with a Gauss-Legendre rule of the same node count.

**★2.** State, with reasons, why the GLL-quadrature mass matrix is diagonal and
what that costs.

**★3.** For a generalised eigenproblem $Kv = \lambda Mv$ with the explicit
stability condition $\Delta t \le 2/\sqrt{\lambda_{\max}}$, compute the timestep
limit for the measured $\lambda_{\max} = 3245.7555$ at $p = 6$, $h = 0.5$.

## ★★ Applied

**★★4.** The measured $\lambda_{\max}$ at $p = 4$, $h = 0.5$ is $766.9212$ and at
$p = 8$, $h = 0.5$ is $9397.6063$. Compute the ratio, the exponent implied by
$p^n$ scaling, and the timestep limit at $p = 8$.

**★★5.** Using the measured exponents 3.469 in $p$ and 2.009 in $1/h$, predict
$\lambda_{\max}$ at $p = 12$ with $h = 0.125$, and the timestep limit that
follows. State one reason the prediction will be approximate.

**★★6.** The $h$-refinement study at $p = 4$ measures $\mathrm{L}^2$ orders of
4.995, 4.999, 5.000, 5.000. State the theoretical rate and explain why the first
value is low.

## ★★★ Research-oriented

**★★★7.** A wave-propagation code needs a timestep small enough that the wave
crosses no more than a fixed fraction of a node spacing. Using the measured
$\lambda_{\max}$ scalings, compare the cost in timesteps of reaching a given
accuracy by (i) doubling $p$ from 4 to 8 at fixed $h$, and (ii) halving $h$ at
$p = 4$. Use the measured accuracy from the lesson's tables and state which is
cheaper.

**★★★8.** Design a measurement that separates the *lumping* error from the
*discretisation* error in the SEM stiffness eigenvalue spectrum, and state the
predicted outcome for each configuration.
