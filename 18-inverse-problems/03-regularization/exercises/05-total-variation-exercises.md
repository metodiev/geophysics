# Exercises — 18-03-05 Total Variation and Edge-Preserving Inversion

Attempt these before reading the
[solutions](./05-total-variation-solutions.md). The lesson is
[05 Total Variation and Edge-Preserving Inversion](../05-total-variation.md).
All models are **SYNTHETIC**. Reference values: 100 cells over 40 km
($404\ \mathrm{m}$ spacing), line-mass sources at $1.5\ \mathrm{km}$ depth, noise
$1.8589\ \mathrm{mGal}$ ($0.50\%$ of the peak); a blocky model with a largest
jump of $+3.90$ (in $10^{9}\ \mathrm{kg\,m^{-1}}$) and a ramp from $1.0$ to
$4.0$.

## ★ Foundational

**★1.** For the two-sample problem $\min\tfrac12[x_1^2+(x_2-1)^2]+\alpha|x_2-x_1|$
with $\alpha = 0.3$, compute the solution and the resulting step height, and
verify the two stationarity equations.

**★2.** Using $h \mapsto \max(h-2\alpha,0)$, compute the $\alpha$ at which a step
of height $3.90$ is annihilated, and the same for a step of height $0.60$. State
what the two numbers imply for a model that contains both contrasts.

**★3.** Write the ADMM $z$-update for the TV problem and identify which quantity
acts as the threshold and which as the penalty weight.

## ★★ Applied

**★★4.** The best-$\alpha$ edge widths are $960\ \mathrm{m}$ (Tikhonov $L=I$),
$1006\ \mathrm{m}$ (Tikhonov $L=D$) and $325\ \mathrm{m}$ (TV) against a
$1.5\ \mathrm{km}$ source depth. Express each as a fraction of the depth and
explain what "sharper than the data resolution" means physically.

**★★5.** From the summary table, list the residual ratios
$\mathrm{res}^2/(n\sigma^2)$ at each objective's best $\alpha$ for the blocky and
the ramp models. State whether the residual can select the penalty, and justify
the answer with the numbers.

**★★6.** On the ramp, TV produces 11–15 spurious jumps across
$\alpha = 10^{-3}$ to $10^{-1}$ while first-order Tikhonov produces 0 at its best
$\alpha$. Compute the ratio of their best errors and state which penalty is
"right" for that model, with the reason.

## ★★★ Research-oriented

**★★★7.** Show that the ADMM $m$-update solves a linear system whose matrix does
not depend on $\alpha$, and derive what that implies for the cost of a
37-point $\alpha$ sweep compared with solving each $\alpha$ from scratch.

**★★★8.** Design an experiment that distinguishes TV steps that follow the data
from TV steps created by the penalty, using only the data. Specify the statistic,
the design, and the expected behaviour of the statistic under the two
hypotheses.
