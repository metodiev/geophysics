# Solutions — 18-02-05 Resolution and Information Matrices in Interpretation

> **Read after attempting the exercises.** Lesson:
> [05 Resolution and Information Matrices](../05-resolution-matrices.md).

---

## ★1 — The three matrices

$R = G^{+}G$ (model resolution), $D = GG^{+}$ (data resolution),
$N = I-R$ (null-space projector). With
$\mathbf{d} = G\mathbf{m}_{\text{true}}+\mathbf{e}$,

$$\hat{\mathbf{m}} = G^{+}\mathbf{d} = G^{+}G\mathbf{m}_{\text{true}}
+ G^{+}\mathbf{e} = R\mathbf{m}_{\text{true}}+G^{+}\mathbf{e}.$$

---

## ★2 — Identities and the errors they catch

| identity | catches |
|---|---|
| $GR = G$ | a mis-scaled or transposed $G^{+}$ |
| $RG^{+} = G^{+}$ | $G^{+}$ computed with the wrong singular directions |
| $R^{2}=R$ | a truncated/untruncated mismatch (a sum of fewer terms is not idempotent) |
| $D^{2}=D$ | the same on the data side |
| $GN = 0$ | a tolerance cut that does not actually annihilate the "null" directions |

---

## ★3 — Traces

$\operatorname{tr}R = 12$ = number of independent model combinations the experiment
determines; $\operatorname{tr}D = 12$ = number of independent data directions
actually used. They are equal because both equal $\operatorname{rank}(G)$: the same
$r$ independent directions are counted once on each side.

---

## ★4 — Reporting resolution

(a) Structure with a wavelength of a few kilometres at best; the measured mean
kernel width is 4.0650 km, so features narrower than that are smeared and their
amplitudes are not recovered.

(b) The cell width is a *parameterisation* choice; the kernel width is an
*experiment* property. Parameterising on 100 m cells would not change the kernel
width at all, so quoting 1 km as the resolution would overstate the experiment by a
factor 4.065.

---

## ★5 — Checkerboard

(a) Invisible energy fraction $= 1-0.7923^{2} = 1-0.6277 = 0.3723$, i.e. $37.2\%$.

(b) The recovered pattern's amplitude is systematically low: roughly
$0.7923\times0.08 = 0.0634\ \mathrm{s}$ if the energy loss is spread over the
pattern, i.e. a $21\%$ underestimate — and because the recovered pattern is also
distorted, the per-trough values vary around that. Predict an *underestimate*, never
a spurious zero.

(c) Add rays that sample odd and even cells differently: for instance rays over
cells (0,1), (2,3), …, which make the alternating pattern lie in
$\operatorname{range}(G^{\!\top})$. Alternatively use two datasets with complementary
coverage (a joint inversion,
[18-07-01](../../07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md)).

---

## ★6 — Combinations

(a) $0.009500/0.002835 = 3.351$.

(b) The average vector $(1/3,1/3,1/3)$ is closer to the row space of $G$ than
individual unit vectors are: the data constrain *weighted sums along the rays*, and
a three-cell average is closer to such a sum than a single cell. Formally the
variance of the estimate is $\mathbf{c}^{\!\top}C_m\mathbf{c}$, and the off-diagonal
elements of $C_m$ are negative where cells are measured together, so averaging
cancels correlated uncertainty.

---

## ★★★7 — Reporting template

| field | content | justification from this lesson |
|---|---|---|
| rank & tolerance | numerical rank at a stated relative tolerance, and the dimension of $\mathcal{N}(G)$ | rank is tolerance-dependent; cell 15 has $R_{jj}=0$ |
| resolution summary | per-region kernel width in km, or a map of $R_{jj}$ with the width | ends have $R_{jj}=0.846$ but width 5.99 km |
| covariance | per-parameter standard deviations, or a statement that only combinations are reported | median per-cell sd 0.0095 s vs 0.0028 s for a 3-cell average |
| pattern tests | recovered fraction for a smooth, a checkerboard and a spike pattern | 0.9348, 0.7923, 0.9200 measured, with 37.2% invisible for the checkerboard |
| verification | measured retrieval error against the covariance + bias prediction | measured/predicted $= 0.9997$ |
| claim rewriting | each unsupportable claim replaced by a resolved combination | the cell-14 and cell-15 examples |

---

## ★★★8 — Correlated noise

(a) With $C_d = C$, the information matrix becomes
$F = G^{\!\top}C^{-1}G$; its eigenvalues are the inverse posterior variances along
the *whitened* model directions. Equivalently, compute the SVD of the whitened
operator $\tilde{G} = L^{-1}G$ with $C = LL^{\!\top}$: the eigenvalues of $F$ are
the squared singular values of $\tilde{G}$ divided by 1 (since the whitened noise has
unit variance).

(b) Which directions gain and which lose depends on the noise colour. For positive
correlation (red noise) the long-wavelength data directions are effectively less
informative because the noise already looks like a long-wavelength signal, so the
**low-order model directions lose** and the eigenvectors rotate towards
higher-order patterns. In the demonstration's trend problem the change was small
(variance ratios 1.05–1.23) precisely because the trend is low-order; for a model
with structure at the correlation scale the gain would be large.

(c) Diagnostic: compute the model covariance (equivalently the resolution and the
eigen-decomposition) both ways and compare the *reported sds* and the *invisible
energy fractions* of §5. If the two analyses disagree about which patterns are
recoverable, then the conclusion is conditional on the covariance and must be
reported as such — the same rule as for a rank tolerance.
