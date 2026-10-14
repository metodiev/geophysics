# Solutions — 18-01-05 Model Space, Data Space and Mappings Between Them

> **Read after attempting the exercises.** Lesson:
> [05 Model Space and Data Space](../05-model-space-data-space.md).

---

## ★1 — Dimensions

$\dim\operatorname{range}(G) = r = 6$;
$\dim\mathcal{N}(G) = M - r = 12-6 = 6$;
$\dim\operatorname{range}(G)^{\perp} = N - r = 20-6 = 14$. Check:
$6+6 = 12 = M$ and $6+14 = 20 = N$.

---

## ★2 — The projector

$P = GG^{+} = U_rU_r^{\!\top}$ with $U_r$ the first $r$ left singular vectors.

1. idempotent: $P^{2} = U_rU_r^{\!\top}U_rU_r^{\!\top} = U_rU_r^{\!\top} = P$;
2. symmetric: $P^{\!\top} = U_rU_r^{\!\top} = P$ (so the projection is orthogonal);
3. $\operatorname{tr}P = \operatorname{tr}(U_r^{\!\top}U_r) = \operatorname{tr}I_r = r$.

---

## ★3 — The misfit floor

White noise is isotropic, so its energy splits in proportion to the subspace
dimensions: a fraction $(N-r)/N$ lies in the orthogonal complement, where no model
can touch it, and the best achievable misfit norm is
$\sqrt{(N-r)/N}\,\lVert\mathbf{e}\rVert$.

---

## ★4 — Fluctuation of a single draw

(a) Each coordinate of the projection is a linear combination of Gaussians; the
normalised energy in a $k$-dimensional subspace out of $N$ follows a
Beta$(k/2,(N-k)/2)$ distribution, with variance

$$\operatorname{Var} = \frac{2k(N-k)}{N^{2}(N+2)}
= \frac{2\times14\times6}{400\times22} = 0.0191,\qquad \sigma = 0.138 .$$

So a single draw with mean $0.70$ and standard deviation $0.138$ routinely lands
anywhere in $[0.42,0.98]$; the observed $0.89063$ is $1.4$ standard deviations
above the mean — unremarkable.

(b) It is one realisation of a random variable, not an estimate of the mean; only
the ensemble average is the expected fraction.

---

## ★5 — The cost of an accurate projector

(a) At tolerance $10^{-10}$: $\varepsilon\kappa = 2.220\times10^{-16}\times
9.764\times10^{7} = 2.17\times10^{-8}$, and the measured error is
$2.930\times10^{-9}$ — the same order of magnitude, below the bound as it must be.
At tolerance $10^{-6}$: $\varepsilon\kappa = 2.220\times10^{-16}\times
2.259\times10^{4} = 5.01\times10^{-12}$, and the measured error is
$1.740\times10^{-13}$ — again the same order.

(b) The cost is directions: rank 6 versus rank 4. Two singular directions
($\sigma_5/\sigma_1 = 8.47\times10^{-7}$, $\sigma_6/\sigma_1 = 1.02\times10^{-8}$)
are declared unusable to buy the better projector. Since those directions carry
relative information of order $10^{-7}$–$10^{-8}$, the trade is reasonable if the
data are no better than $10^{-6}$ relative; it would be wasteful with
$10^{-12}$-accurate data.

---

## ★6 — A large, invisible component

(a) The model change is $20.0\%$ of the model norm while the data change is
$3.4\times10^{-13}$ of $\lVert\mathbf{d}\rVert$ — a factor
$0.001/(3.4\times10^{-13}) = 2.9\times10^{9}$ below a $0.1\%$ data error. No
plausible measurement could detect it.

(b) The claim is unsupportable: a *lower bound* on a model parameter requires
either a bound in the prior (as in the linear programmes of
[18-01-03 §5](../03-null-space.md)) or a resolved combination. The component in
question lies in the null space, so the data alone say nothing about it; the
number quoted must come from the constraint set, and must be reported as such.

---

## ★★★7 — Designing the "how many data" experiment

**Vary:** the number $N$ of independent data of one type, e.g. the number of
borehole levels added to the surface reading (using the slab geometry of
[18-01-02 §3.1](../02-hadamard-well-posedness.md)) or the number of stations on a
profile.

**Measure, for each $N$:** (i) the numerical rank at a fixed relative tolerance;
(ii) the width of the feasible interval (or the posterior standard deviation) of
the *reported quantity*, $\rho$ at the chosen depth; (iii) the fit of the
minimum-norm model.

**Criterion:** stop when the interval half-width for $\rho$ at the target depth
falls below $5\%$ of the true value *for every one of at least 200 noise
realisations*. Report the $N$ required, the tolerance, the noise level and the
prior bounds; without all four the number is not reproducible.

---

## ★★★8 — The identity and the floating-point discrepancy

**Exactness.** If $G = U\Sigma V^{\!\top}$ then
$G^{\!\top}G = V\Sigma^{2}V^{\!\top}$, so the eigenvalues of $G^{\!\top}G$ are
exactly $\sigma_i^{2}$ and

$$\kappa(G^{\!\top}G) = \frac{\sigma_1^{2}}{\sigma_r^{2}}
= \left(\frac{\sigma_1}{\sigma_r}\right)^{2} = \kappa(G)^{2}.$$

**Floating point.** Computing $G^{\!\top}G$ forms each entry as a sum of products
of $G$ entries, so the *relative* accuracy of the small eigenvalues is limited by
the largest: an eigenvalue that is a fraction $f$ of the largest carries relative
error $\sim\varepsilon/f$. Here the sixth singular direction has
$f = (\sigma_6/\sigma_1)^{2} = (1.024\times10^{-8})^{2} = 1.05\times10^{-16}$, which
is at $\varepsilon$, so its value is entirely roundoff. Measured:
$\kappa(G^{\!\top}G) = 8.808476\times10^{15}$ against the exact
$9.533748\times10^{15}$, a ratio $0.923926$; the missing $7.6\%$ is roundoff in the
sixth eigenvalue.

**Rule.** Never form $G^{\!\top}G$ for an inverse problem. Work with $G$ and its
SVD (or a QR factorisation): the conditioning is then $\kappa(G)$, not
$\kappa(G)^{2}$, and the small directions remain resolvable down to
$\varepsilon\kappa(G)$ instead of $\varepsilon\kappa(G)^{2}$.
