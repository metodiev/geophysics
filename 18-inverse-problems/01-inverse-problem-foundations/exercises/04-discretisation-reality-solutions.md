# Solutions — 18-01-04 Discretisation, Parameterisation and Model Choice

> **Read after attempting the exercises.** Lesson:
> [04 Discretisation and Model Choice](../04-discretisation-reality.md).

---

## ★1 — Three errors

| error | introduced by |
|---|---|
| measurement / theory error | the acquisition and the physics in the kernel |
| representation (discretisation) error | the choice of parameterisation and basis |
| estimator bias | the selection rule (damping, norm, prior) |

---

## ★2 — Convergence order

$5.550\times10^{-3}/1.887\times10^{-3} = 2.94$ for a block-size ratio of $2$.
Second-order convergence predicts a ratio of $2^{2} = 4$; the first refinement
step is a bit better than that because the profile's curvature is not uniform.
Across the later rows, $1.302\times10^{-4}/2.224\times10^{-5} = 5.85$ for a factor
$2$ in $h$ — better than fourth order would be wrong, so the honest statement is
that the *fitted* order over the last five refinements, $2.045$, is the number to
quote, and single-step ratios fluctuate.

---

## ★3 — Top and bottom readings

The sensor at the bottom of the stack has every layer above it, so each layer
contributes $-2\pi G_N\rho h$; the surface sensor has every layer below it and each
contributes $+2\pi G_N\rho h$. The two rows of $G$ are exact negatives, so the
readings satisfy $d_{\text{bottom}} = -d_{\text{surface}}$ and the row space has
dimension $6$, not $7$: numerical rank $6$.

---

## ★4 — Non-monotone model error

(a) Model error falls from $0.9999\%$ ($M=3$) to $0.6334\%$ ($M=4$), rises to
$0.8773\%$ ($M=5$) and $1.6433\%$ ($M=7$), then settles at $1.3618\%$ ($M=20$).

(b) All solutions are minimum-norm members of their equivalence classes. As $M$
grows past the number of independent data (6), the added directions are
null-space directions, and the min-norm rule spreads the model over them in a way
that has nothing to do with the truth. The error therefore reflects the *rule*,
not the data.

(c) Report the parameterisation whose reported quantity you are prepared to
defend. Here $M = 4$ gives the smallest model error in the table ($0.6334\%$),
but that is partly luck of the realisation; a defensible answer is to report the
range over $M = 3$–$5$ ($0.63\%$ to $1.0\%$) and state that the fine-grid models
are estimator artefacts, supported by the measured equivalence-class spread of
§5 of the lesson.

---

## ★5 — Relative singular value and amplification

$$\frac{\sigma_7}{\sigma_1} = \frac{3.949768\times10^{-17}}{8.136166\times10^{-2}}
= 4.855\times10^{-16}.$$

Since $\varepsilon = 2.220\times10^{-16}$, this is about $2.2\varepsilon$: the
direction is empty.

Amplification: $1/3.949768\times10^{-17} = 2.532\times10^{16}$. A data error of
$10^{-3}\ \mathrm{mGal}$ in that direction becomes
$2.532\times10^{13}\ \mathrm{kg\,m^{-3}}$ in the model — larger than the mass of
the Earth per cubic metre, which is the giveaway that the number is meaningless.

---

## ★6 — Reporting a spread

(a) $580.5/2909.9 = 0.1995$, i.e. $20.0\%$ of the truth.

(b) The sampled models fit the data at $0.0434\%$ of $\lVert\mathbf{d}\rVert$ —
*identical* to the min-norm fit, because the perturbations lie in the exact null
space (their data contribution is $10^{-12}$ relative).

(c) Report the resolved quantity and its range: "the data determine
$\rho(5\ \mathrm{km})$ only to within $[2620,3201]\ \mathrm{kg\,m^{-3}}$ given the
stated bounds and the declared tolerance; the minimum-norm representative is
$2960\ \mathrm{kg\,m^{-3}}$." Quote the fit as well, so the reader can see that
all members of the range are equally consistent.

---

## ★★★7 — Blocks versus linear elements

For an exactly linear truth, the measured block-basis data errors are
$1.675\times10^{-3}$ (4 blocks) down to $2.423\times10^{-5}$ (32 blocks), while the
linear-basis errors are $2.746\times10^{-16}$ to $1.209\times10^{-15}$ — machine
precision at every resolution. Choose the linear basis: for the same number of
parameters it removes the representation error entirely, so all remaining error is
measurement or estimator error.

**Condition under which the justification fails.** If the target is *not* smooth
— a sharp interface, a fault, a thin high-density layer — the linear basis spreads
it over neighbouring nodes and needs many nodes to represent it, while a block (or
an $L_{1}$-regularised) parameterisation captures it sharply. The correct test is
to measure the representation error for a *plausible* extreme target, not only for
a smooth one.

---

## ★★★8 — Reply to "the regulariser invented structure"

| $\alpha$ | data misfit | model error vs truth | $\rho(5\ \mathrm{km})$ |
|---|---|---|---|
| $0$ (truncated min-norm) | 0.0434% | 1.5037% | 2960.4 |
| $10^{-4}$ | 0.0434% | 1.5038% | 2960.4 |
| $10^{-2}$ | 1.9486% | 4.9405% | 2947.2 |
| $3\times10^{-2}$ | 13.1057% | 20.6076% | 2785.9 |

The unregularised answer ($\alpha = 0$) is *better* by both measures here, because
the heavy damping of $\alpha = 3\times10^{-2}$ throws away resolvable information
(misfit $13.1\%$). So in this experiment the objection is not supported: the
sharpness was not invention. The honest limitation: this compares each model with
a *known* synthetic truth, which is precisely what you do not have in practice —
with real data the correct reply is a synthetic recovery test on a plausible model
([18-08-02](../../08-practical-inversion-workflow/02-synthetic-testing.md)), plus a
statement of the misfit each $\alpha$ achieves.
