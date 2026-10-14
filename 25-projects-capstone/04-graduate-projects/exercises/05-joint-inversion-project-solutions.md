# Solutions — 25-04-05 Project: Joint Gravity-Seismic Inversion

> Read after attempting. Lesson:
> [05 Joint Inversion](../05-joint-inversion-project.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/joint_inversion_demo.py`](../code/joint_inversion_demo.py).

---

## ★1 — The two kernels

$$A^{g}_{ji} = \frac{\partial g_j}{\partial\rho_i} = 2G\iint_{\text{block }i}
\frac{z'}{(x_j - x')^{2} + z'^{2}}\,\mathrm{d}x'\,\mathrm{d}z'
\qquad [\mathrm{mGal\ per\ kg\,m^{-3}}],$$

$$A^{t}_{pi} = \frac{\partial t_p}{\partial\rho_i}
= -\frac{\ell_{pi}\beta}{v_i^{2}}
\qquad [\mathrm{s\ per\ kg\,m^{-3}}],$$

with $\ell_{pi}$ the length of path $p$ inside block $i$ and
$\beta = \mathrm{d}v/\mathrm{d}\rho$.

The travel-time kernel is **sparse**: $\ell_{pi}$ is zero for every block the path
does not cross, so each row has only a few non-zeros (a path through a 4-layer
model touches at most a handful of the 32 blocks). The gravity kernel is **dense**:
every block contributes to every station, because gravity is a long-range field
whose integrand decays only as $1/r$. That difference is what "complementary
sensitivities" means precisely — the row spaces differ in *which* model directions
they can see, and the sparse kernel sees local combinations the smooth one cannot.

---

## ★2 — Sensitivity of one path

$$v = 4500 + 0.40 \times 250 = 4600\ \mathrm{m\,s^{-1}},$$

$$\frac{\Delta v}{v} = \frac{100}{4500} = 2.22\%,$$

$$t = \frac{\ell}{v},\qquad
\Delta t \approx -\frac{\ell\,\Delta v}{v^{2}}
= -\frac{40\,000 \times 100}{4500^{2}} = -0.198\ \mathrm{s}.$$

Against a stated noise of $0.05\ \mathrm{s}$ that is a $4\sigma$ signal **for a
single path through one block** — but the path's length is distributed over several
blocks and the anomaly is spread over three of them, so the effective signal per
path is smaller; and 24 paths provide 24 such constraints against 32 parameters.
That is the quantitative reason the joint gain in §5 of the lesson is only a factor
of $1.02$ rather than a factor of several: the per-datum signal is real but the
parameter count is larger than the number of independent path combinations.

---

## ★3 — The two ratios

$$\frac{\text{joint }\sigma}{\text{gravity }\sigma}
= \frac{14.23}{14.56} = 0.977,
\qquad
\frac{\text{joint error}}{\text{gravity error}}
= \frac{21.09}{22.36} = 0.943.$$

**What each measures.** The first ratio compares the *formal* posterior
uncertainties: it says the seismic data reduce the propagated data-noise
uncertainty by $2.3\%$. The second compares the *actual* model errors against the
known truth: it says the joint model is $5.7\%$ closer to the truth. The two are
not the same number because the formal uncertainty excludes the regularisation bias
(module 25-03's §6), and the model error includes it. Both belong in the report:
the first is the claim, the second is the evidence that the claim is realised.

---

## ★★4 — Cost and benefit

$$\text{additional resolved parameters} = 19.65 - 19.23 = 0.42,$$

against **24 additional data** and a petrophysical link whose scale the data cannot
constrain (§6 of the lesson).

**Cost–benefit in one sentence:** 24 seismic paths purchased $0.42$ of an
additional resolved parameter — about $1.8\%$ of one parameter for each new path —
at the price of an unverifiable scaling assumption, so this dataset would not
justify the acquisition cost if resolving density structure were the only
objective.

The honest qualification is that the seismic data were not acquired to resolve
density: they resolve *velocity*, and this project's link converts velocity to
density. A joint inversion is justified when the objective is the shared structure
(e.g., a target depth), not when it is the converted physical property.

---

## ★★5 — Why a doubled link is invisible

The travel time enters through the path integral

$$t_p = \sum_i \frac{\ell_{pi}}{v_i}
\qquad\text{with}\qquad v_i = V_0 + \beta(\rho_i - \rho_0),$$

so to first order the data constrain the **combination** $\beta\,\rho_i$: halving
$\rho_i$ and doubling $\beta$ leaves every $v_i$, and hence every travel time,
unchanged. A model that satisfies the shifted link therefore fits *exactly as
well* — which is what the demonstration measures, a model change of
$268\ \mathrm{kg\,m^{-3}}$ at a misfit of $0.7462$ against $0.7697$ for the correct
link.

**What would break the degeneracy.** Any information that is not a function of the
product: (i) an **independent density** measurement — a borehole density log, a
core sample, or a gravity-derived density in a region where gravity is
well-conditioned; (ii) a **non-linear** link, since
$v = V_0 + \beta(\rho-\rho_0)^{n}$ has a $\beta\,\rho^{n}$ structure that a
single scaling cannot absorb, so wide density ranges make $\beta$ identifiable;
(iii) a **bounded** model, since the physical range of $\rho$ is limited and a
scaled link would drive it outside.

---

## ★★6 — The unresolved fraction and its location

$$\text{gravity: } \frac{32 - 19.23}{32} = 39.9\%,
\qquad
\text{joint: } \frac{32 - 19.65}{32} = 38.6\%.$$

So roughly **40% of the model space remains unresolved** in both cases: the seismic
data reduced the unresolved fraction by $1.3$ percentage points.

**Where it sits.** The layer-by-layer errors are $13.13$ (layer 1) and $19.66$
(layer 4) for gravity alone, and $10.91$ and $22.23$ for the joint inversion. Two
readings:

1. The **deep layer's error is larger in both** (19.66 vs 13.13, and 22.23 vs
   10.91), consistent with gravity's kernel being smoother and weaker at depth —
   the deep blocks trade against each other and against the shallow ones.
2. The joint inversion **improved the shallow layer and degraded the deep one**.
   With a regularised objective this is expected: the travel-time constraints are
   concentrated where the paths run (shallow to mid-crustal), so the joint fit
   pulls the shallow densities toward the velocity-derived values and lets the
   deep ones float further. The residual null space therefore moves *deeper*, which
   is why a joint inversion's resolution must be reported layer by layer and not
   as a single trace.

---

## ★★★7 — A joint inversion that constrains the link

**Parameterisation.** Let the model be $(\rho_i,\ V_0,\ \beta,\ n)$ with

$$v = V_0 + \beta\,\mathrm{sign}(\rho-\rho_0)\,\left|\rho-\rho_0\right|^{n},
\qquad \beta > 0,$$

so the link has three parameters alongside the 32 densities. Report the posterior
(or the resolution matrix) for $(\beta, n)$ as part of the result, not as a
nuisance.

**Why identifiability appears.** In the linear case the data constrain only the
product $\beta\rho$, leaving a one-dimensional degeneracy. With $n \ne 1$ the
sensitivity of $t_p$ to $\rho_i$ depends on $\rho_i$ itself, so two blocks at
different densities respond differently to a change in $\beta$; the degeneracy is
broken by the **spread** of density in the model. The condition for identifiability
is therefore a **wide density range** across the model: with
$\Delta\rho \sim 500\ \mathrm{kg\,m^{-3}}$ and $n$ free, the travel times constrain
$\beta$ and $n$ jointly, albeit with strong correlation.

**Independent data that pin the scale.** At least one of:

1. **Borehole or core density** in one block, which fixes $\rho_i$ directly and
   breaks the product degeneracy at that location;
2. **a well-log velocity**, which fixes the link at one depth and moves the
   degeneracy to the whole model;
3. **gravity gradiometry**, whose kernel is different enough to constrain the
   shallow density independently of the velocity-derived values.

**Resolution statement for the link.** Report the marginal posterior (or profile
likelihood) for $\beta$ and $n$ **and** their correlation with the mean density;
the honest output is an ellipse in the $(\beta, \bar\rho)$ plane. If that ellipse's
major axis runs along the $\beta\bar\rho = \text{const}$ direction, the link is
still degenerate and must be said so.

**The synthetic test.** Generate travel times from a known $(\beta, n)$ with a
realistic density range and noise, invert for all parameters, and show that
$\beta$ is recovered within its stated interval — then repeat with a narrow density
range and show that it is not. A design whose link recovery has never been
demonstrated on synthetic data with a known answer has not established that the
link is identifiable.
