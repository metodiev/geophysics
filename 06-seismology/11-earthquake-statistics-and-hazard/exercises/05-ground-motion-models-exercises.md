# Exercises — 06-11-05 Ground-Motion Prediction Equations and Their Uncertainty

Attempt these before reading the
[solutions](./05-ground-motion-models-solutions.md). The lesson is
[05 Ground-Motion Models](../05-ground-motion-models.md). All models and data in
this module are **SYNTHETIC**.

## ★ Foundational

**★1.** Using $\ln \hat z = 1.411 + 1.00(M-6) - 1.30\ln(R+5)$, compute the median
PGA in g for $M6.0$ at $30\ \mathrm{km}$. State the factor by which the median
changes per magnitude unit.

**★2.** A dataset reports $\sigma_\text{total} = 0.65$ and
$\sigma_\varepsilon = 0.52$. Compute $\tau$ and the fraction of the total variance
that is between-event.

**★3.** Compute $\mathrm{mean}/\mathrm{median}$ for $\sigma = 0.80$ and state the
resulting percentage by which the mean exceeds the median.

## ★★ Applied

**★★4.** For the scenario $M6.5$ at $15\ \mathrm{km}$ ($\hat z = 0.1376\ \mathrm{g}$),
compute $P(PGA > 0.4\ \mathrm{g})$ for $\sigma = 0.60$ and for $\sigma = 0.80$.
Compute the ratio and state the implication for a hazard calculation that adopts
the smaller value.

**★★5.** The demonstration reports that the standard deviation of a median
estimate from $n$ records is $\sigma/\sqrt n$. For $\sigma = 0.60$, compute the
value for $n = 50$, and the $n$ required for a standard error of $0.05$.

**★★6.** Using the two fitted models of the demonstration
($\ln PGA = 1.0091m - 8.8194$ and $\ln PGA = 5.2615\ln m - 12.2224$), compute the
predicted ratio at $M6.0$, $M7.5$ and $M8.0$ (all at 20 km) and state what the
sequence of ratios demonstrates.

## ★★★ Research-oriented

**★★★7.** Design a study that measures the magnitude dependence of the scatter
$\sigma$ and state, with the algebra of the lognormal tail, how a
magnitude-dependent $\sigma$ changes a hazard curve relative to a constant-$\sigma$
model. A specification that could not be executed is a failed answer.

**★★★8.** A station's single record at 60 km from a $M5.0$ event is inverted for
the layer thickness above it, using a 1D model with $\sigma_\varepsilon = 0.5$ and
$\tau = 0.35$, and the inversion assumes the median relation is exact. State the
posterior uncertainty on the thickness, and design the measurement programme that
would reduce it most per unit cost.
