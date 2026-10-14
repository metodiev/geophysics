# Solutions — 14-03-01 Porosity-Permeability and Kozeny-Carman Relations

> Read after attempting. Lesson:
> [01 Porosity-Permeability and Kozeny-Carman Relations](../01-porosity-permeability-relations.md).
> All models **SYNTHETIC**. $\tau = 2.5$, $c_K = 5$, $S_0 = 6/d$,
> $1\ \mathrm{darcy} = 9.869233\times10^{-13}\ \mathrm{m^{2}}$.

---

## ★1 — KC permeability

$d = 0.15\ \mathrm{mm} = 1.50\times10^{-4}\ \mathrm{m}$.

$$S_0 = \frac{6}{d} = \frac{6}{1.50\times10^{-4}} = 4.00\times10^{4}\ \mathrm{m^{-1}}.$$

$$R_h = \frac{\phi}{S_0(1-\phi)} = \frac{0.20}{4.00\times10^{4}\times0.80}
= \frac{0.20}{3.20\times10^{4}} = 6.25\times10^{-6}\ \mathrm{m}.$$

$$k = \frac{\phi R_h^{2}}{2\tau}
= \frac{0.20\times(6.25\times10^{-6})^{2}}{5.0}
= \frac{0.20\times3.906\times10^{-11}}{5.0}
= 1.5625\times10^{-12}\ \mathrm{m^{2}}.$$

Cross-check with the $d$-form:
$k = d^{2}\phi^{3}/(180(1-\phi)^{2})
= (2.25\times10^{-8}\times0.008)/(180\times0.64)
= 1.5625\times10^{-12}\ \mathrm{m^{2}}$. Agreement is exact.

In millidarcy: $1.5625\times10^{-12}/9.869233\times10^{-16}
= 1583.2\ \mathrm{mD} = 1.583\ \mathrm{D}$.

---

## ★2 — Hydraulic conductivity

$$K = \frac{k\rho g}{\mu}
= \frac{1.5625\times10^{-12}\times998.2\times9.80665}{1.002\times10^{-3}}
= 1.5265\times10^{-5}\ \mathrm{m\,s^{-1}}.$$

In $\mathrm{m\,d^{-1}}$: $1.5265\times10^{-5}\times86400
= 1.3189\ \mathrm{m\,d^{-1}}$.

---

## ★3 — Units

$\phi$ dimensionless; $c_K$ dimensionless; $S_0$ in $\mathrm{m^{-1}}$, so
$S_0^{2}$ in $\mathrm{m^{-2}}$; $(1-\phi)^{2}$ dimensionless. Then

$$\frac{[\phi^{3}]}{[c_K][S_0^{2}][(1-\phi)^{2}]}
= \frac{1}{1\cdot\mathrm{m^{-2}}\cdot1} = \mathrm{m^{2}},$$

which is the unit of intrinsic permeability. A useful consequence: if you feed
$S_0$ in $\mathrm{mm^{-1}}$ the answer comes out in $\mathrm{mm^{2}}$, a factor
$10^{6}$ wrong.

---

## ★★4 — Sensitivity

$$\frac{\mathrm{d}\ln k}{\mathrm{d}\phi} = \frac{3}{\phi} + \frac{2}{1-\phi}
= \frac{3}{0.30} + \frac{2}{0.70} = 10.000 + 2.857 = 12.857.$$

An absolute error $\delta\phi = 0.01$ gives
$\delta k/k \approx 12.857\times0.01 = 12.9\%$.

At $\phi = 0.25$ the factor is $12 + 2.667 = 14.667$, i.e. $14.7\%$. The
sensitivity **falls as porosity rises**: at high porosity the medium is already
conducting and each extra pore matters less, whereas at low porosity the
$(1-\phi)^{-2}$ term amplifies the change. For $\phi = 0.10$ the factor is
$30 + 2.22 = 32.2$, so a one-point porosity error is a third of the answer.

---

## ★★5 — Which grain size is plausible

Invert $k = d^{2}\phi^{3}/(180(1-\phi)^{2})$:

$$d = \sqrt{\frac{180\,k\,(1-\phi)^{2}}{\phi^{3}}}.$$

$\phi = 0.18$: $d = \sqrt{180\times5.0\times10^{-13}\times0.6724/0.005832}
= \sqrt{1.0377\times10^{-8}} = 1.0187\times10^{-4}\ \mathrm{m}
= 0.102\ \mathrm{mm}$.

$\phi = 0.28$: $d = \sqrt{180\times5.0\times10^{-13}\times0.5184/0.021952}
= \sqrt{2.1254\times10^{-9}} = 4.610\times10^{-5}\ \mathrm{m}
= 0.046\ \mathrm{mm}$.

The first is a fine sand — plausible. The second is coarse silt, at the lower
edge of what is normally called "sand", and a well-sorted sand with
$\phi = 0.28$ and $k = 5\times10^{-13}\ \mathrm{m^{2}}$ is geologically
inconsistent: a 0.046 mm medium should have a markedly lower permeability than
$5\times10^{-13}\ \mathrm{m^{2}}$ unless it is much better sorted or the pore
geometry differs. Both pairs reproduce the measurement exactly, which is the
non-uniqueness point.

---

## ★★6 — Implied flow porosity

$k_\text{true} = 2353.94\ \mathrm{mD}
= 2353.94\times9.869233\times10^{-16} = 2.32316\times10^{-12}\ \mathrm{m^{2}}$.

KC at $\phi_f = 0.190$ with $d = 0.20\ \mathrm{mm}$:

$$k = \frac{(2.0\times10^{-4})^{2}\times0.190^{3}}{180\times(1-0.190)^{2}}
= \frac{4.0\times10^{-8}\times6.859\times10^{-3}}{180\times0.6561}
= \frac{2.7436\times10^{-10}}{118.10} = 2.3232\times10^{-12}\ \mathrm{m^{2}},$$

i.e. $2353.9\ \mathrm{mD}$ — the generator's value.

So $\phi_f = 0.190$. The clay rule gives
$\phi_\text{clay} = \min(0.06, 0.35\times0.25) = \min(0.06, 0.0875)
= 0.060$, and $\phi - \phi_\text{clay} = 0.250 - 0.060 = 0.190$. ✓

KC applied to the *total* porosity over-predicts by
$6254.63/2353.94 = 2.66$.

---

## ★★7 — One-sigma range and what it omits

$\mathrm{d}\ln k/\mathrm{d}\phi = 14.667$ at $\phi = 0.25$, so
$\sigma_{\ln k} = 14.667\times0.012 = 0.1760$, i.e. a one-sigma spread of
$17.6\%$:

$$k = 6.2\times10^{-12}\ \mathrm{m^{2}},\quad
5.29\times10^{-12}\ \text{to}\ 7.11\times10^{-12}\ \mathrm{m^{2}}.$$

Not in that error bar:

1. **The grain size and hence $S_0$.** A factor $1.5$ in $d$ is a factor $2.25$
   in $k$, and no resistivity measurement sees it.
2. **The Kozeny constant $c_K = 2\tau$.** The lesson measures $0.60\times$ to
   $1.60\times$ over $\tau = 1.5$–$4.0$.
3. **The clean-sand assumption.** If the rock contains clay, the lesson measures
   an over-prediction of $2.1\times$ to $4.1\times$ even when the clay fraction
   is only a few points.

The quoted range is therefore a lower bound on the uncertainty, not a total
error bar.

---

## ★★★8 — The cubic law versus Kozeny–Carman

**(a) Derivation.** Laminar flow between two smooth parallel walls of aperture
$b$ and width $W$ under a head gradient $\nabla h$ follows from
Navier–Stokes with the parabolic profile:

$$Q = \frac{\rho g}{\mu}\cdot\frac{b^{3}}{12}\,W\,\nabla h .$$

The transmissivity per unit width of the fracture is therefore
$T' = \rho g b^{3}/(12\mu)$. A set of fractures with spacing $s$ gives, per unit
bulk width, a total flux $\tfrac{1}{s}Q/W$, and Darcy's law requires that to
equal $\tfrac{k\rho g}{\mu}\nabla h$. Equating:

$$\frac{b^{3}}{s}\cdot\frac{\rho g}{12\mu} = \frac{k\rho g}{\mu}
\;\;\Longrightarrow\;\;
k = \frac{b^{3}}{12s}.$$

**(b)** $b = 5.0\times10^{-5}\ \mathrm{m}$, $s = 1.0\ \mathrm{m}$:

$$k = \frac{(5.0\times10^{-5})^{3}}{12}
= \frac{1.25\times10^{-13}}{12} = 1.0417\times10^{-14}\ \mathrm{m^{2}}
= 10.55\ \mathrm{mD}.$$

**(c)** The fracture porosity is $\phi = b/s = 5.0\times10^{-5}$. KC with
$d = 0.15\ \mathrm{mm}$ and $\tau = 2.5$:

$$k_\text{KC} = \frac{(1.5\times10^{-4})^{2}\times(5.0\times10^{-5})^{3}}
{180\times(1-5\times10^{-5})^{2}}
\approx \frac{2.25\times10^{-8}\times1.25\times10^{-13}}{180}
= 1.5625\times10^{-23}\ \mathrm{m^{2}}
= 1.58\times10^{-8}\ \mathrm{mD}.$$

The mismatch is

$$\frac{k_\text{cubic}}{k_\text{KC}} = \frac{1.0417\times10^{-14}}
{1.5625\times10^{-23}} = 6.7\times10^{8},$$

about nine orders of magnitude.

**(d)** Report the cubic-law value, $1.04\times10^{-14}\ \mathrm{m^{2}}$
($10.55\ \mathrm{mD}$), with the aperture, the spacing and the assumption of
smooth parallel walls stated. KC is not merely imprecise here: it is the wrong
model, because its $S_0 = 6/d$ describes a granular surface, not two planar
walls, and its $\phi^{3}$ scaling assumes the flow cross-section shrinks with
porosity rather than in proportion to $b^{3}$.

---

## ★★★9 — Calibration design (model answer)

**(a)** Nine synthetic samples: three grain sizes $d$ crossing a factor of three,
three porosities per grain size, all with a measured $k$ at a stated effective
stress and with the fluid properties stated. Plot $\ln k$ against
$\ln[\phi^{3}/(S_0^{2}(1-\phi)^{2})]$; the slope should be $1$ and the intercept
gives $-\ln c_K$. Fit one $c_K$ per grain size *and* one pooled $c_K$.

**(b)** $c_K$ absorbs pore shape, pore-size distribution and the bound-water
layer. A finer grain size means a larger specific surface and a larger
bound-water fraction, so the effective flow area is smaller and the fitted $c_K$
drifts. If the three per-grain-size fits differ by more than the measurement
scatter, KC is not transferring, and the pooled $c_K$ is a fiction.

**(c)** The test that separates "bad fit" from "wrong model": **check the
exponent, not just the constant.** KC predicts slope $1$ on the plot in (a) and,
independently, $k \propto d^{2}$ at fixed $\phi$. If the measured slope on
$d$ differs from $2$, or the plot in (a) has a slope different from $1$, no
choice of $c_K$ can repair it. A second check is the residual pattern: a
systematic curvature in (a) as $\phi \to 0.40$ is the signature of the
$(1-\phi)^{2}$ divergence failing, not of a wrong constant.
