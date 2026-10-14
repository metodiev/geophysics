# Solutions — 14-03-04 Building Geophysical Proxies for Hydrological Properties

> Read after attempting. Lesson:
> [04 Building Geophysical Proxies for Hydrological Properties](../04-geophysical-proxy-relations.md).
> All models and posteriors **SYNTHETIC**.

---

## ★1 — Amplification at $\phi = 0.30$

$$\frac{\mathrm{d}\ln k}{\mathrm{d}\phi} = \frac{3}{\phi} + \frac{2}{1-\phi}
= \frac{3}{0.30} + \frac{2}{0.70} = 10.000 + 2.857 = 12.857 .$$

$$\frac{\mathrm{d}\ln\phi}{\mathrm{d}\ln\rho_t} = -\frac{1}{m} = -0.500,$$

$$\frac{\mathrm{d}\ln k}{\mathrm{d}\ln\rho_t}
= 12.857 \times 0.30 \times (-0.500) = -1.9286 .$$

At $\phi = 0.25$ the same chain gives $-1.8333$, so the chain amplifies *more*
at higher porosity? No — read the factor carefully: $12.857 < 14.667$ but
$\phi = 0.30 > 0.25$, and the product gives $1.929 > 1.833$. The chain
amplification is $\phi\,(3/\phi + 2/(1-\phi))/m = (3 + 2\phi/(1-\phi))/m$,
which increases with $\phi$. **This is a genuine and slightly counter-intuitive
result: a more porous rock is more sensitive to a relative resistivity error in
this proxy**, because the extra porosity is bought at the price of a larger
$(1-\phi)^{-2}$ term in KC.

---

## ★2 — Permeability error from a 3% resistivity error

$$\Delta\ln k \approx -1.9286 \times 0.03 = -0.0579
\;\;\Longrightarrow\;\; \frac{\Delta k}{k} \approx -5.8\% .$$

**Units convention.** The derivative is taken with respect to $\ln\rho_t$, so the
input must be a *relative* resistivity error and the output is a *relative*
permeability error. If you instead differentiate with respect to $\phi$ you get
$12.857$ per unit porosity, and feeding it a $3\%$ number gives $0.386$ — a
$39\%$ error, wrong by a factor of $6.7$. The two conventions differ by
$\phi/m$, so state which one you mean.

---

## ★3 — Monte Carlo prediction

$$\frac{\sigma_k}{k} = \left|\frac{\mathrm{d}\ln k}{\mathrm{d}\ln\phi}\right|
\times \frac{\sigma_\phi}{\phi}
= \left(\frac{3}{\phi} + \frac{2}{1-\phi}\right)\phi \times 0.10 .$$

At $\phi = 0.25$: $(12 + 2.667)\times0.25 = 3.667$, so
$\sigma_k/k \approx 3.667\times0.10 = 0.367$, i.e. $36.7\%$.

The lesson's table gives $36.7\%$ for $\sigma_\phi = 0.025$
($\sigma_\phi/\phi = 10.0\%$) — agreement to three figures, which is the point:
the local amplification factor predicts the propagated spread accurately for
spreads up to at least $10\%$.

---

## ★★4 — What the single number hides

**(a) and (b)**

| assumed quantity | status | why it matters |
|---|---|---|
| grain diameter / specific surface $S_0$ | **measurement** (usually one or two sieve analyses) | $k \propto d^{2}$; a factor $1.5$ in $d$ is $2.25$ in $k$ |
| Kozeny constant $c_K = 2\tau$ | **fitted model parameter** | the lesson measures $0.60\times$–$1.60\times$ over $\tau = 1.5$–$4.0$ |
| porosity $\phi$ | derived, from a measurement via a **model** | the amplification is $3/\phi + 2/(1-\phi)$ per unit $\phi$ |
| clean-matrix assumption | **model choice** | the clay example over-predicts by $2.1\times$–$4.1\times$ |

**(c) Attack first.** The grain size. It carries the largest single contribution
in the error budget computed in the lesson ($0.6000$ in $\ln k$ for a $\pm30\%$
uncertainty, against $0.4697$ for a $\pm0.2$ exponent error and $0.0363$ for a
$2\%$ resistivity error), it is cheap to constrain (grain-size analysis on
additional samples, or an NMR surface-to-volume measurement), and it is
independent of the geophysical inversion.

---

## ★★5 — Why two operators help so much

**(a) The operators' shapes.**

| operator | behaviour in $\phi$ | behaviour in $S_w$ |
|---|---|---|
| Archie: $\rho_t = a\rho_w/(\phi^{m}S_w^{n})$ | strong ($\phi^{-2}$) but shared with $S_w^{-2}$ | strong, but shared with $\phi$ |
| Gassmann: $V_p(\phi, S_w)$ | strong through the dry frame and density | weak: the lesson measures only $\sim3\times10^{2}\ \mathrm{m\,s^{-1}}$ across the whole saturation range, and that range depends on the fluid geometry |

The key is the *interaction*: in $\rho_t$, $\phi$ and $S_w$ enter through a single
monomial $\phi^{m}S_w^{n}$, so the data constrain the product
$\phi S_w$ (for $m = n$) and not the two factors separately — a ridge with a
single direction. In $V_p$ the two enter through different physics (frame
stiffness and density), so the $V_p$ likelihood is curved in a different
direction. The two likelihoods therefore intersect in a short segment rather
than overlapping along the same ridge.

**(b) Why the gain is super-additive in standard deviation.** With a
$10545$-point grid, resistivity alone gives $\sigma_\phi = 0.0636$ and velocity
alone $0.0077$; the joint gives $0.0043$. If the two were independent
measurements of the same quantity, combining would give
$1/\sigma_\text{joint}^{2} = 1/\sigma_1^{2} + 1/\sigma_2^{2}$, i.e.
$\sigma_\text{joint} = (0.0636^{-2}+0.0077^{-2})^{-1/2} = 0.0077$ — barely better
than velocity alone, because $\rho_t$ adds almost nothing about $\phi$. The
measured joint value is $0.0043$, which is *less* than either, because the
information is not "about $\phi$" in either case: it is information about the
*trade-off*, and only the pair removes the trade-off.

---

## ★★6 — Error budget

Reference state: $\phi = 0.25$, $S_w = 0.60$, $\rho_t = 111.111\
\Omega\,\mathrm{m}$, $d = 0.20\ \mathrm{mm}$.

| source | stated 1 sigma | contribution to $\sigma_{\ln k}$ |
|---|---|---|
| $\rho_t$ | $2\%$ relative | $0.0363$ |
| $m$ | $\pm0.2$ | $0.4697$ |
| $d$ | $\pm30\%$ relative | $0.6000$ |
| **quadrature total** | | $\mathbf{0.7628}$ |

Arithmetic for the exponent term: with
$C = a\rho_w/(\rho_t S_w^{n}) = 1\times2.50/(111.111\times0.36) = 0.062500$,
the inferred porosity at $m = 2.2$ is $\phi = C^{1/2.2} = 0.28358$ against
$0.25000$ at $m = 2.0$. Then

$$\ln\frac{k(0.28358)}{k(0.250)}
= \ln\left[\left(\frac{0.28358}{0.250}\right)^{3}
\left(\frac{0.75000}{0.71642}\right)^{2}\right]
= \ln(1.5995) = 0.4697 .$$

Arithmetic for the grain-size term: $k \propto d^{2}$, so
$2\times0.30 = 0.6000$.

**Ranking:** $d$ ($0.6000$) $>$ $m$ ($0.4697$) $\gg$ $\rho_t$ ($0.0363$).

**Single most effective action.** Improve the *specific surface*, i.e. the grain
size. Even removing the grain-size term entirely leaves
$\sqrt{0.0363^{2}+0.4697^{2}} = 0.4711$, so it must be attacked together with
$m$; but it is the largest term and the cheapest to reduce. Improving the
resistivity from $2\%$ to $0.5\%$ changes the total from $0.7628$ to $0.7620$.

---

## ★★★7 — Orthogonal versus parallel measurements

**(a) General result.** If two independent data sets have Gaussian likelihoods,
the posterior precision (inverse variance) in a parameter is the **sum of the
Fisher informations**:

$$\frac{1}{\sigma_\text{joint}^{2}} = \mathcal{I}_1 + \mathcal{I}_2,
\qquad \mathcal{I}_i = \frac{1}{\sigma_i^{2}} \text{ for a directly measured parameter}.$$

*Same direction.* Two equally good measurements of the same parameter
($\mathcal{I}_1 = \mathcal{I}_2 = \mathcal{I}$) give
$\sigma_\text{joint} = \sigma/\sqrt{2}$: a factor of $1.41$ at best. **Adding a
second copy of the same experiment is the worst possible use of resources.**

*Orthogonal directions.* If measurement 1 constrains only $\phi$ and measurement
2 constrains only $S_w$, each joint marginal is limited by its own datum, but the
*trade-off* direction is removed and the joint posterior volume shrinks by the
product. In a two-parameter problem the joint uncertainty area is
$\sigma_1\sigma_2$ (orthogonal) versus $\sigma_1\sigma_2\sqrt{1-\rho^{2}}$ (with
correlation $\rho$): the gain over the better single marginal is the whole
correlation, not the $1/\sqrt{2}$.

**(b) Are the two operators orthogonal here?** Compare the marginal widths.

| | $\sigma_\phi$ | $\sigma_{S_w}$ |
|---|---|---|
| $\rho_t$ only | 0.0636 | 0.1578 |
| $V_p$ only | 0.0077 | 0.2742 |
| ratio $\rho_t/V_p$ | $8.3$ | $0.58$ |

Resistivity is $8.3$ times *worse* at porosity than velocity, and $1.7$ times
*better* at saturation; the two log-ratio widths differ by a factor of about
$14$ in the opposite sense. That is much closer to orthogonal than to parallel:
if the two data sets constrained the same combination, their marginal widths
would be in the *same* ratio for both parameters. The measured joint widths
($0.0043$, $0.0122$) are smaller than either single width, which cannot happen
for parallel measurements at all — it is only possible when the constraints lie
in different directions.

**(c) Practical acquisition rule.** Choose the second measurement to have a
**different sensitivity pattern**, not merely a better noise level. A second,
quieter resistivity survey is a factor of $1.41$ at best (and in practice
nothing, because the errors are correlated). A velocity measurement on the same
volume, whose sensitivity to porosity runs through the dry frame and therefore
differs in shape, is worth an order of magnitude. Concretely:

1. Map each candidate measurement's sensitivity vector to the target parameters.
2. Reject candidates whose vector is nearly parallel to one you already have.
3. Acquire the pair that maximises the *angle* between sensitivities.

---

## ★★★8 — A tracer monitoring proxy (model answer)

**(a) Chain.** Measured quantity: the apparent resistivity at a set of
electrodes. Target: the change in water saturation. Chain:
$\rho_a \to \rho_t$ (geometric factor / inversion, itself a model),
$\rho_t \to S_w$ (Archie: $S_w = (a\rho_w/(\phi^{m}\rho_t))^{1/n}$), and then to
volumetric water content $\theta = \phi S_w$ if that is the hydrological target.
The chain must be written with each step's assumptions before any number is
quoted.

**(b) Smallest detectable saturation change.** A $5\%$ change in $S_w$ changes
$\rho_t$ by

$$\frac{\Delta\rho_t}{\rho_t} = \frac{\Delta(S_w^{-n})}{S_w^{-n}}
\approx n\frac{\Delta S_w}{S_w} = 2\times0.05 = 10\% .$$

For the change in $\rho_t$ to be seen above a $2\%$ measurement noise on each of
two surveys, the *difference* has a noise of $\sqrt{2}\times2\% = 2.8\%$, so the
$10\%$ signal-to-difference-noise ratio is $10/2.8 = 3.5$, comfortably above a
detection threshold of about $2$. **The $5\%$ saturation change is detectable**,
with a resolution limit of about $\Delta S_w/S_w = 2\times(2.8/2)\times\frac{1}{2}
= 2.8\%$ — i.e. changes below about $3\%$ are not reliably separated from noise.
(Recompute with the actual survey repeatability; the structure of the argument,
not the value $2\%$, is the answer.)

**(c) Dominant modelling assumption.** That the *pore-fluid resistivity is
unchanged* between the two surveys. A tracer that is ionic changes $\rho_w$ as
well as $S_w$, and the two effects are indistinguishable in a single resistivity
measurement. Test it in the field by (i) sampling the fluid at a monitoring well
on each survey, and (ii) acquiring one datum that responds to $S_w$ but not to
$\rho_w$ — for example a neutron or NMR measurement in a borehole, or a
time-lapse velocity. If no such datum is available, the honest output is a joint
$(\Delta S_w, \Delta\rho_w)$ estimate with a stated trade-off.

**(d) Why a difference is better.** Differencing removes every *static* error:
the geometric factor of the array, the near-surface static shifts, the electrode
position error and the unknown background geology. What remains is the
repeatability of the system plus the genuine change, and the systematic part of
the error cancels rather than adding. **The noise penalty** is that each survey's
independent (random) noise adds in quadrature to the difference:
$\sigma_\Delta = \sqrt{\sigma_1^{2}+\sigma_2^{2}} = \sqrt{2}\,\sigma$ for two
equal surveys, a $41\%$ penalty on the random component — a bargain compared
with the systematic components removed. The quantitative test of whether
differencing is worth it is the ratio of the systematic to the random error in a
single survey: if that ratio is larger than $\sqrt{2}$, differencing wins.
