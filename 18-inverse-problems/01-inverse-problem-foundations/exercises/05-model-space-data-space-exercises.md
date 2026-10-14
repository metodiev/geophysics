# Exercises — 18-01-05 Model Space, Data Space and Mappings Between Them

Attempt these before reading the
[solutions](./05-model-space-data-space-solutions.md). The lesson is
[05 Model Space and Data Space](../05-model-space-data-space.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** An experiment has $N = 20$, $M = 12$ and numerical rank $r = 6$ at the
declared tolerance. Give the dimensions of $\operatorname{range}(G)$,
$\mathcal{N}(G)$ and $\operatorname{range}(G)^{\perp}$.

**★2.** Write down the projector $P = GG^{+}$, and state its three defining
properties (idempotent, symmetric, trace equals rank).

**★3.** Explain in one sentence why the misfit of a least-squares fit to white
noise cannot be driven below $\sqrt{(N-r)/N}\,\lVert\mathbf{e}\rVert$.

## ★★ Applied

**★★4.** The measured unfittable fraction over 2000 draws is $0.6983$ and the
exact expectation is $0.7000$ for $N=20$, $r=6$. (a) Compute the standard
deviation you would predict for a single draw from the projector argument.
(b) Explain why the first draw ($0.89063$ unfittable) is not a contradiction.

**★★5.** The projector error table shows $\lVert P^{2}-P\rVert = 2.930\times10^{-9}$
at tolerance $10^{-10}$ (rank 6, $\kappa = 9.764\times10^{7}$) and
$1.740\times10^{-13}$ at tolerance $10^{-6}$ (rank 4,
$\kappa = 2.259\times10^{4}$). (a) Verify the rule "error $\approx
\varepsilon\kappa$". (b) State the cost of the smaller error.

**★★6.** A model component $\mathbf{m}_{\text{null}}$ has
$\lVert\mathbf{m}_{\text{null}}\rVert = 7.1186\times10^{9}\ \mathrm{kg}$,
which is $20.0\%$ of $\lVert\mathbf{m}_1\rVert = 3.5525\times10^{10}\ \mathrm{kg}$,
but produces data at $3.4\times10^{-13}$ of $\lVert\mathbf{d}\rVert$.
(a) Compare that with a plausible $0.1\%$ data error. (b) State the consequence
for a claim that "the deep mass must be at least $7\times10^{9}\ \mathrm{kg}$".

## ★★★ Research-oriented

**★★★7.** For the same operator, design the numerical experiment you would run to
answer: "how many independent data do I need before $\rho$ at a chosen depth is
determined to $5\%$?" Specify what you vary, what you measure, and the criterion
that ends the experiment.

**★★★8.** The measured $\kappa(G^{\!\top}G)/\kappa(G)^{2} = 0.923926$ instead of
$1$. Show analytically that the identity is exact, and construct the
floating-point argument explaining which singular value is responsible for the
$7.6\%$ discrepancy. State the practical rule that follows.
