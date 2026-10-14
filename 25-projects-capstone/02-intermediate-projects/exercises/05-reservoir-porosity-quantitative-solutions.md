# Solutions — 25-02-05 Project: Porosity from Well Logs with Uncertainty

> Read after attempting. Lesson:
> [05 Reservoir Porosity](../05-reservoir-porosity-quantitative.md). All values
> are **SYNTHETIC** teaching numbers printed by
> [`code/porosity_well_logs_demo.py`](../code/porosity_well_logs_demo.py).

---

## ★1 — Deriving and evaluating the density porosity

The bulk density of a two-component rock is the volume-weighted average:

$$\rho_b = \phi\,\rho_f + (1-\phi)\,\rho_\text{ma}
= \rho_\text{ma} - \phi(\rho_\text{ma}-\rho_f),$$

so

$$\phi_D = \frac{\rho_\text{ma}-\rho_b}{\rho_\text{ma}-\rho_f}.$$

For $\rho_b = 2.40$:

$$\phi_D = \frac{2.65 - 2.40}{2.65 - 1.00} = \frac{0.25}{1.65} = 0.15152
= 15.15\ \mathrm{p.u.}$$

Note the units: both numerator and denominator are
$\mathrm{g\,cm^{-3}}$, so $\phi_D$ is a dimensionless fraction, reported in
**porosity units** where $1\ \mathrm{p.u.} = 0.01$ of bulk volume.

---

## ★2 — Wyllie sonic porosity

$$\phi_S = \frac{\Delta t - \Delta t_\text{ma}}{\Delta t_f - \Delta t_\text{ma}}
= \frac{90.0 - 55.5}{189.0 - 55.5} = \frac{34.5}{133.5} = 0.25843
= 25.84\ \mathrm{p.u.}$$

Unit: dimensionless (slowness over slowness), reported in p.u. The 90 µs ft⁻¹ is
a slow, high-porosity interval; the relation is linear, so a 1 µs ft⁻¹ error
becomes $1/133.5 = 0.0075$ of porosity.

---

## ★3 — Sensitivities to the log measurements

$$\frac{\partial\phi_D}{\partial\rho_b} = -\frac{1}{\rho_\text{ma}-\rho_f}
= -\frac{1}{1.65} = -0.60606\ (\mathrm{g\,cm^{-3}})^{-1},$$

$$\frac{\partial\phi_S}{\partial\Delta t} = \frac{1}{\Delta t_f-\Delta t_\text{ma}}
= \frac{1}{133.5} = 7.491\times10^{-3}\ (\mathrm{\mu s\,ft^{-1}})^{-1}.$$

Per-sample uncertainties:

$$\sigma_{\phi_D} = 0.60606 \times 0.02 = 0.01212 = 1.212\ \mathrm{p.u.},$$

$$\sigma_{\phi_S} = 7.491\times10^{-3} \times 2.0 = 0.01498 = 1.498\ \mathrm{p.u.},$$

both matching the demonstration. The density estimator is the more precise one per
sample, which is why it carries the larger weight in §★★4.

---

## ★★4 — Weights, and which standard error to use

**From the empirical standard errors** $\sigma_{\bar D} = 0.426$ and
$\sigma_{\bar S} = 0.475\ \mathrm{p.u.}$:

$$w_D = \frac{1}{0.426^{2}} = 5.510, \qquad w_S = \frac{1}{0.475^{2}} = 4.432,
\qquad w_D + w_S = 9.942,$$

$$\text{weights } 55.4\%\ /\ 44.6\%, \qquad
\phi = \frac{5.510 \times 19.575 + 4.432 \times 15.761}{9.942} = 17.874\ \mathrm{p.u.},$$

$$\sigma = \frac{1}{\sqrt{9.942}} = 0.3172\ \mathrm{p.u.}$$

**From the propagated standard errors** $\sigma_{\bar D} = 1.212/\sqrt{10} = 0.383$
and $\sigma_{\bar S} = 1.498/\sqrt{10} = 0.474\ \mathrm{p.u.}$, the demonstration
obtains $60.4\% / 39.6\%$, $\phi_w = 18.066\ \mathrm{p.u.}$ and
$\sigma_w = 0.298\ \mathrm{p.u.}$

**Which is right.** The propagated value isolates the *log-noise* contribution and
is the correct weight when the purpose of combining is to reduce log noise; the
empirical value additionally contains geological variability across the ten
samples. That variability is largely **shared** between the two estimators (both
respond to the same rock), so it does not average down when the two are
combined — including it in the weights would overstate the information gained.
The demonstration therefore uses the propagated weights, and *still reports* the
empirical spread, because it is the honest description of the interval's
heterogeneity. The weights are not $50/50$ because the density log's per-sample
porosity sensitivity ($1.212\ \mathrm{p.u.}$) is smaller than the sonic log's
($1.498\ \mathrm{p.u.}$).

---

## ★★5 — The matrix shift, exactly and to first order

**Exact.** With $\rho_b = 2.40\ \mathrm{g\,cm^{-3}}$:

$$\phi_D(\rho_\text{ma} = 2.65) = 15.152\ \mathrm{p.u.},$$

$$\phi_D(\rho_\text{ma} = 2.71) = \frac{2.71-2.40}{2.71-1.00} = \frac{0.31}{1.71}
= 0.18129 = 18.129\ \mathrm{p.u.}$$

Shift: $18.129 - 15.152 = +2.977\ \mathrm{p.u.}$

**First order.** The derivative evaluated at the correct matrix is

$$\frac{\partial\phi_D}{\partial\rho_\text{ma}}
= \frac{\rho_b-\rho_f}{(\rho_\text{ma}-\rho_f)^{2}}
= \frac{1.40}{1.65^{2}} = \frac{1.40}{2.7225} = 0.51422\ (\mathrm{g\,cm^{-3}})^{-1},$$

so

$$\Delta\phi \approx 0.51422 \times 0.06 = +0.03085 = +3.085\ \mathrm{p.u.}$$

The first-order value overstates the exact shift by $3.6\%$, because 0.06
$\mathrm{g\,cm^{-3}}$ is not small relative to $\rho_\text{ma}-\rho_f = 1.65$.
Both directions are worth remembering: for small perturbations the derivative is
exact and cheap; for a mineralogy change of this size the exact recomputation is
better.

**In units of the per-sample density-porosity uncertainty**
($1.212\ \mathrm{p.u.}$):

$$\frac{2.977}{1.212} = 2.46\sigma.$$

A wrong matrix is worth two and a half log-noise standard deviations **on every
sample**, i.e. it does not average out over the interval — the interval mean
inherits it in full while the random term falls as $1/\sqrt{10}$.

---

## ★★6 — Two estimators that disagree

**Consistency test.** Difference $= 18.0 - 16.0 = 2.0\ \mathrm{p.u.}$; combined
standard error

$$\sigma_\Delta = \sqrt{0.3^{2} + 0.4^{2}} = 0.5\ \mathrm{p.u.},
\qquad
\frac{\Delta}{\sigma_\Delta} = \frac{2.0}{0.5} = 4.0.$$

A $4\sigma$ difference is **not** consistent with pure measurement noise at any
conventional threshold, so inverse-variance weighting is **not defensible** as a
way of reducing the uncertainty: the two numbers are not estimates of the same
quantity under the stated assumptions.

**The weighted mean, for completeness.**

$$w_1 = \frac{1}{0.09} = 11.111, \quad w_2 = \frac{1}{0.16} = 6.250, \quad
\sum w = 17.361,$$

$$\phi_w = \frac{11.111 \times 18.0 + 6.250 \times 16.0}{17.361}
= \frac{200 + 100}{17.361} = 17.28\ \mathrm{p.u.}, \qquad
\sigma_w = \frac{1}{\sqrt{17.361}} = 0.240\ \mathrm{p.u.}$$

**What it would be wrong to claim.** That the porosity is
$17.28 \pm 0.24\ \mathrm{p.u.}$ The $\pm 0.24$ accounts only for the two random
terms; a $4\sigma$ inconsistency means the model error dominates, so the honest
statement is $17.3\ \mathrm{p.u.}$ with a systematic uncertainty of order the
discrepancy itself, i.e. about $\pm 2\ \mathrm{p.u.}$ — a factor of eight larger.
The discrepancy, not the weighted error bar, sets the precision.

---

## ★★★7 — Identifying the cause of a density–sonic discrepancy

**Additional logs and what they measure.**

| log | measures | why it separates the causes |
|---|---|---|
| Photoelectric factor (PEF) | effective atomic number of the formation | gives matrix mineralogy directly: quartz $1.81$, dolomite $3.14$, limestone $5.08$ (values vary slightly by tool and source) |
| Gamma ray (GR), spectral GR | natural radioactivity | identifies clay/shale content and its type (Th/K ratio) |
| Neutron porosity (NPHI) | hydrogen index | responds to clay-bound water and to gas in the opposite sense to density |
| Resistivity (deep and shallow) | fluid-filled connected porosity | separates hydrocarbon from water, and indicates invasion |
| NMR (T2 distribution) | free and bound fluid, effective porosity | distinguishes intergranular from vuggy/fractured porosity directly |

**The three candidate causes and their signatures.**

1. **Matrix change (dolomite or limestone instead of quartz).** PEF moves to
   $3.14$ (dolomite) or $5.08$ (limestone); GR stays low; density porosity is
   systematically high because $\rho_\text{ma}$ was assumed too low; the sonic
   porosity moves in the *opposite* direction because $\Delta t_\text{ma}$ was
   also assumed too high. **Separator: PEF.**
2. **Shale.** GR high; neutron porosity elevated (clay-bound water) while density
   porosity is only mildly affected; the two estimators separate with the sonic
   reading low because clay-bound water is slower than the matrix but faster than
   free fluid in the Wyllie average. **Separator: GR, with the Th/K ratio for
   type.**
3. **Secondary (vuggy or fracture) porosity.** PEF unchanged; GR low; the
   Wyllie relation underestimates porosity because it assumes uniform
   intergranular pores, so $\phi_S < \phi_D$ while $\phi_D \approx \phi_\text{NMR}$
   or less. **Separator: NMR free-fluid index**, with the
   $\phi_D - \phi_S$ difference as the "secondary porosity index".

**The measurement that separates them.** PEF plus GR together rule matrix change
and shale in or out; if both are negative, the discrepancy is pore geometry and
NMR confirms it. **A design that omits PEF cannot separate cause 1 from cause 3**,
because both leave GR low and both give $\phi_D > \phi_S$ — so PEF is the
non-negotiable addition.
