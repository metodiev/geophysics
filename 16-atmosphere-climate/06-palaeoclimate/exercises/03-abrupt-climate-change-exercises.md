# Exercises — 16-06-03 Abrupt Climate Change and Tipping Elements

Attempt these before reading the
[solutions](./03-abrupt-climate-change-solutions.md). Lesson:
[03 Abrupt Climate Change and Tipping Elements](../03-abrupt-climate-change.md).
All models are **SYNTHETIC**: every threshold computed here is a property of the
model, not of the Earth. The demonstration is
[`../code/abrupt_climate_change_demo.py`](../code/abrupt_climate_change_demo.py).

## ★ Foundational

**★1.** The two-box model's steady state satisfies
$q = 1/(1+2|q|) - H/(2|q|)$. Verify by substitution that $q = -0.0522$ is a
steady solution at $H = 0.10$, and report the residual.

**★2.** The zero-dimensional energy-balance model has warm branch
$T = (0.70Q-210)/2$ and cold branch $T = (0.38Q-210)/2$ (degrees Celsius), with
the ice threshold at $-10\ \mathrm{{}^{\circ}C}$. Compute both branch
temperatures at $Q = 400\ \mathrm{W\,m^{-2}}$ and state whether each is
self-consistent.

**★3.** At what value of $Q$ does the warm branch cease to be self-consistent?
Compute it from the condition $T_{\text{warm}} = -10\ \mathrm{{}^{\circ}C}$.

## ★★ Applied

**★★4.** The upper edge of the bistable range moves from $379.5$ to
$678.5\ \mathrm{W\,m^{-2}}$ as the ice albedo moves from $0.50$ to $0.72$.
Compute the change per $0.01$ of albedo.

**★★5.** Explain why the intermediate steady solution of the two-box model is
unstable, and describe a numerical test that would confirm it without solving for
the eigenvalues.

**★★6.** In the energy-balance model the two stable branches at
$Q = 340.25\ \mathrm{W\,m^{-2}}$ are $+14.09$ and $-40.35\ \mathrm{{}^{\circ}C}$.
Compute their mean and state why that number is not a meaningful "expected
temperature" for this model.

## ★★★ Research-oriented

**★★★7.** Design a numerical test that distinguishes a genuine fold bifurcation
from a numerical artefact in a simulation that shows a rapid change. State the
observable you would vary, the diagnostic you would monitor, and what result
would indicate an artefact.

**★★★8.** Write a short critique of the statement "model X predicts that
component Y of the climate system will pass a tipping point at a warming of
$Z\ \mathrm{K}$". State what additional information would be needed for the
statement to be a scientific claim rather than a report about the model.
