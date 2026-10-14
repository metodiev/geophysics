# Exercises — 25-02-05 Project: Porosity from Well Logs with Uncertainty

Attempt these before reading the
[solutions](./05-reservoir-porosity-quantitative-solutions.md). The project is
[05 Reservoir Porosity](../05-reservoir-porosity-quantitative.md). Values printed
by
[`code/porosity_well_logs_demo.py`](../code/porosity_well_logs_demo.py):

| Quantity | Demonstration value |
|---|---|
| samples | 10, depths 2000–2009 m |
| $\rho_b$ | $2.3270 \pm 0.0222\ \mathrm{g\,cm^{-3}}$ (log $\sigma = 0.02$) |
| $\Delta t$ | $76.5405 \pm 2.0061\ \mathrm{\mu s\,ft^{-1}}$ (log $\sigma = 2.0$) |
| matrix / fluid (density) | $2.65$ / $1.00\ \mathrm{g\,cm^{-3}}$ |
| matrix / fluid (sonic) | $55.5$ / $189.0\ \mathrm{\mu s\,ft^{-1}}$ |
| $\phi_D$ mean / sd / SEM | $19.575$ / $1.348$ / $0.426\ \mathrm{p.u.}$ |
| $\phi_S$ mean / sd / SEM | $15.761$ / $1.503$ / $0.475\ \mathrm{p.u.}$ |
| per-sample $\sigma$ | $1.212$ (density), $1.498$ (sonic) p.u. |
| weights | $60.4\%$ density, $39.6\%$ sonic |
| weighted porosity | $18.066 \pm 0.298\ \mathrm{p.u.}$ |
| estimator discrepancy | $3.814\ \mathrm{p.u.} = 6.3\sigma$ |
| $\partial\phi_D/\partial\rho_\text{ma}$ | $0.4874\ (\mathrm{g\,cm^{-3}})^{-1}$ |
| limestone matrix shift | $+2.925$ (first order), $+2.82$ p.u. (exact) |
| sonic matrix shift | $+4.763\ \mathrm{p.u.}$ |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Derive $\phi_D = (\rho_\text{ma}-\rho_b)/(\rho_\text{ma}-\rho_f)$ from the
volumetric mixing equation, and compute $\phi_D$ for
$\rho_b = 2.40\ \mathrm{g\,cm^{-3}}$ with a quartz matrix
($\rho_\text{ma} = 2.65$) and a $1.00\ \mathrm{g\,cm^{-3}}$ fluid. Give the answer
in p.u.

**★2.** Compute $\phi_S$ for $\Delta t = 90.0\ \mathrm{\mu s\,ft^{-1}}$ with
$\Delta t_\text{ma} = 55.5$ and $\Delta t_f = 189.0\
\mathrm{\mu s\,ft^{-1}}$, and state the unit.

**★3.** Compute the two partial derivatives
$\partial\phi_D/\partial\rho_b$ and $\partial\phi_S/\partial\Delta t$ from the
assumed parameters, and use them to convert the log uncertainties
$\sigma_{\rho_b} = 0.02\ \mathrm{g\,cm^{-3}}$ and
$\sigma_{\Delta t} = 2.0\ \mathrm{\mu s\,ft^{-1}}$ into per-sample porosity
uncertainties.

## ★★ Applied

**★★4.** Using the demonstration's interval means and standard errors
($0.426$ and $0.475\ \mathrm{p.u.}$), recompute the inverse-variance weights and
the weighted porosity, and state the standard error of the result. Explain why
the weights are not $50/50$.

**★★5.** Compute the porosity shift from using $\rho_\text{ma} = 2.71$ instead of
$2.65\ \mathrm{g\,cm^{-3}}$ when $\rho_b = 2.40\ \mathrm{g\,cm^{-3}}$, both
exactly and to first order, and express the shift in units of a single-sample
$\phi_D$ uncertainty.

**★★6.** Two estimators return $18.0 \pm 0.3$ and $16.0 \pm 0.4\ \mathrm{p.u.}$
Compute their difference in units of the combined standard error and state whether
inverse-variance weighting of the two is defensible. Then compute the weighted
mean anyway and state what it would be wrong to claim about it.

## ★★★ Research-oriented

**★★★7.** Design an interpretation that identifies the cause of a
density–sonic porosity discrepancy at a specific interval. Name the additional
logs, state what each measures, give the expected signature in each of the three
candidate causes (matrix/dolomite, shale, secondary porosity or gas), and state
the measurement that would separate them. A design that cannot separate the three
is a failed answer.
