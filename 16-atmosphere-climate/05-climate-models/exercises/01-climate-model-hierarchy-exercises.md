# Exercises — 16-05-01 Model Hierarchy: EBMs, EMICs, GCMs, ESMs

Attempt these before reading the [solutions](./01-climate-model-hierarchy-solutions.md).
The lesson is [01 Model Hierarchy](../01-climate-model-hierarchy.md). All models
and data are **SYNTHETIC** teaching values. Run
[`../code/climate_model_hierarchy_demo.py`](../code/climate_model_hierarchy_demo.py)
to check the numbers quoted from it.

## ★ Foundational

**★1.** A planet has $S = 1361\ \mathrm{W\,m^{-2}}$ and $\alpha = 0.30$.
Compute the absorbed flux and the effective radiating temperature, and state the
unit of each intermediate step.

**★2.** For the same planet, a zero-dimensional energy-balance model uses
$F_{\text{out}} = A + BT$ with $A = 210\ \mathrm{W\,m^{-2}}$ and
$B = 2.0\ \mathrm{W\,m^{-2}\,K^{-1}}$. Compute $T_{0}$ and the implied greenhouse
warming $T_{0}-T_{\text{eff}}$.

**★3.** With $C = 5.0\ \mathrm{W\,yr\,m^{-2}\,K^{-1}}$ compute the relaxation
time $\tau$, and state the time required to reach $90\%$ of a new equilibrium.

## ★★ Applied

**★★4.** Repeat ★2 with $B = 2.5\ \mathrm{W\,m^{-2}\,K^{-1}}$ and with
$B = 1.5\ \mathrm{W\,m^{-2}\,K^{-1}}$. Tabulate $T_{0}$, the warming from a step
forcing $F = 3.7\ \mathrm{W\,m^{-2}}$, and $\tau$ for all three values of $B$.
State in one sentence what the table shows about the hierarchy's dependence on a
closure coefficient.

**★★5.** Prove that the area-weighted mean of the steady state of the 1-D model
equals the 0-D equilibrium when the albedo is uniform. Start from the integral of
the transport term over $x\in[-1,1]$ and say precisely where the boundary
condition is used.

**★★6.** The demonstration's 1-D run with the ice-albedo feedback cools the
global mean by $2.84\ \mathrm{K}$, with $11.0\%$ of the latitude points becoming
ice-covered (albedo $0.30 \to 0.62$). Estimate the cooling from a globally
averaged absorbed-flux change and explain why your estimate is larger than the
measured value.

## ★★★ Research-oriented

**★★★7.** Design a hierarchy experiment whose purpose is to separate the effect
of the diffusion closure from the effect of the ice-albedo feedback on the
pole-to-equator contrast. Specify the runs, the diagnostic you will compare
across runs, and one confounding effect that your design does not remove.

**★★★8.** A colleague proposes to "validate" the 1-D model by tuning $D$ until
it reproduces an observed pole-to-equator temperature difference, and then to use
the model to predict the response to a doubling of $A$. Write a short critique:
what has been calibrated, what has been assumed, and what independent evidence
would make the prediction defensible.
