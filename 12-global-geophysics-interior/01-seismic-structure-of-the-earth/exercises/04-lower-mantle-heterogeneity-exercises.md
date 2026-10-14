# Exercises — 12-01-04 Lower-Mantle Heterogeneity and LLSVPs

Attempt these before reading the
[solutions](./04-lower-mantle-heterogeneity-solutions.md). The lesson is
[04 Lower-Mantle Heterogeneity and LLSVPs](../04-lower-mantle-heterogeneity.md).
All models and data are **SYNTHETIC** teaching values.

Useful relations: $\delta t = \int \delta u\,\mathrm{d}l = -\int \frac{\delta v}{v^2}\mathrm{d}l$;
$\mathbf{m} = (\mathbf{G}^{T}\mathbf{G}+\lambda^{2}\mathbf{I})^{-1}\mathbf{G}^{T}\mathbf{d}$;
$\mathbf{R} = (\mathbf{G}^{T}\mathbf{G}+\lambda^{2}\mathbf{I})^{-1}\mathbf{G}^{T}\mathbf{G}$;
$\mathbf{C}_m = \sigma^{2}\mathbf{A}^{-1}\mathbf{G}^{T}\mathbf{G}\mathbf{A}^{-1}$
with $\mathbf{A} = \mathbf{G}^{T}\mathbf{G}+\lambda^{2}\mathbf{I}$;
$\Delta T = \delta\ln v_s / (\partial \ln v_s/\partial T)$ with
$\partial \ln v_s/\partial T = -1.2\times10^{-5}\ \mathrm{K^{-1}}$ (a chosen value).

## ★ Foundational

**★1.** A ray with local $v = 11.5\ \mathrm{km\,s^{-1}}$ crosses a 1500 km long
anomaly with $\delta v = -0.115\ \mathrm{km\,s^{-1}}$. Compute $\delta u$ in
$\mathrm{s\,km^{-1}}$ and the resulting travel-time residual in seconds, and state
its sign.

**★2.** A chain of residuals along one ray accumulates the effect of three
segments: $+0.40$ s, $+0.55$ s and $-0.25$ s. Compute the total residual and
explain why a single residual cannot be attributed to a single depth.

**★3.** Convert recovered anomalies of 0.25 %, 1.00 % and 2.00 % (slow) into
temperature anomalies. Express the answer in kelvin and state the sensitivity used
in K per per cent.

## ★★ Applied

**★★4.** For the two-cell problem
$\mathbf{G} = \begin{pmatrix}1&1\\1&1\end{pmatrix}$ and $\lambda^{2} = 2$, compute
$\mathbf{R}$ and interpret every entry. What is the largest diagonal value
reachable for any $\lambda$, and what does that say about the best possible
resolution for this experiment?

**★★5.** An inversion has 240 rays, a grid of 1200 cells, a stated data noise of
0.05 s, and this misfit table:

| $\lambda$ | rms misfit (s) |
|---|---|
| 5 | 0.002 |
| 20 | 0.010 |
| 60 | 0.048 |
| 150 | 0.210 |
| 400 | 0.900 |

(a) Which $\lambda$ does the discrepancy principle select? (b) The recovered peak
at that $\lambda$ is 1.10 %; at $\lambda = 150$ it is 0.80 %. Convert both to
temperature and state the range. (c) How many model-space directions are
unconstrained at best?

**★★6.** A study reports a deep anomaly of 1.5 % slow. The authors also publish a
resolution diagonal of 0.35 at that depth and state that they used
$\lambda = 80$. Estimate the plausible range of the *true* anomaly, explaining
which effect sets the lower bound and which sets the upper bound.

## ★★★ Research-oriented

**★★★7.** Design an experiment to raise the resolution diagonal at the base of the
mantle from the demonstration's 0.065 to at least 0.2. State the data you would
add, quantify the expected effect on the resolution matrix, and describe how you
would verify the improvement without knowing the true model.

**★★★8.** Prove that the recovered-model excess over the true rms in the
shallowest layer is a resolution effect rather than a noise effect. State the two
quantities to compute, give their formulas, and explain what each would look like
if the other were responsible.

**★★★9.** Estimate the size of the second-order error committed by linearising
about the reference ray path. Estimate the transverse displacement of a ray that
passes through a 1 % anomaly over 1000 km, compare it with the cell size, and
state the anomaly magnitude at which the linearisation breaks down for a 500 km
grid.
