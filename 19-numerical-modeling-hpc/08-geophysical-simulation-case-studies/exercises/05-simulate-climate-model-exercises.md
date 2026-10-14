# Exercises — 19-08-05 Running a Simple Climate Model

Attempt these before reading the
[solutions](./05-simulate-climate-model-solutions.md). The lesson is
[05 Running a Simple Climate Model](../05-simulate-climate-model.md). All models
are **SYNTHETIC** teaching models.

## ★ Foundational

**★1.** Compute the zero-dimensional equilibrium temperature for $\alpha = 0.35$
with $S_0 = 1361$ W m$^{-2}$ and the standard Stefan-Boltzmann constant.

**★2.** For the same model add a single grey layer with $\varepsilon = 0.9$ and
compute the surface temperature.

**★3.** A model has $C = 2.0\times10^{8}$ J m$^{-2}$K$^{-1}$ and $B = 1.3$
W m$^{-2}$K$^{-1}$. Compute the relaxation time constant in years and state how long
a run must be to support an equilibrium claim.

## ★★ Applied

**★★4.** Consider a two-state albedo: $\alpha = 0.30$ for $T > 250$ K and
$\alpha = 0.60$ for $T \le 250$ K. Find all consistent equilibria of
$(1-\alpha(T))S_0/4 = \sigma T^{4}$ and state which branch survives.

**★★5.** Construct the manufactured source $Q(y)$ for the one-dimensional diffusive
energy-balance equation with $T_m = 1 + 0.5y^{4}$, showing the differentiation.

**★★6.** An anomaly of $10$ K decays exponentially with the time constant computed
in ★3. How long until the anomaly is $1$ K? State the general relation.

## ★★★ Research-oriented

**★★★7.** Design a model-evaluation test for a one-dimensional energy-balance model
that would be *predictive* rather than calibrated. State the observable, the split of
data, the metric and the failure mode that would look like success.

**★★★8.** A report states that a simple climate model "reproduces the observed
temperature record". Write the three questions you would ask, and then write the
strongest claim the authors could defensibly make if all three are answered
unfavourably for them.
