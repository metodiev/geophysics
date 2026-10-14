# Solutions — 05-01-01 The Central Idea: Property Contrasts Produce Signals

> Attempt the exercises first. Numbers marked *verified* were computed, not
> estimated by hand.

---

## ★1

Because the field of any infinite horizontal layer is fixed by that layer, and
in a uniform half-space the contribution from every depth is the same
everywhere on the surface: the field is a constant. A constant field cannot be
separated from any other constant, and it carries no information about the
horizontal or vertical structure of the half-space. Information enters only
where the property *varies*.

---

## ★2

Sign: **positive** (the body is denser than the host, so it adds downward
acceleration). Relative contrast $= 400/2600 = 0.1538 = 15.4\%$.

---

## ★3 *(verified)*

(a) $12.4\ \mathrm{mGal}\times10^{-5} = 1.24\times10^{-4}\ \mathrm{m\,s^{-2}}$
(exact by the definition of the Gal).
(b) $850\ \mathrm{nT}\times10^{-9} = 8.50\times10^{-7}\ \mathrm{T}$ (exact by
the definition of the gamma/nT).
(c) $2.67\ \mathrm{g\,cm^{-3}}\times10^{3} = 2670\ \mathrm{kg\,m^{-3}}$
(exact, arithmetic on the prefix).
(d) $4500\ \mathrm{m\,s^{-1}} = 4.5\ \mathrm{km\,s^{-1}}$ (exact).

All four are exact conversions of units, not measurements. The *measured*
inputs (12.4, 850, 2.67, 4500) each carry their own limited precision, so the
results should be reported with the same number of significant figures.

---

## ★4

With the mass at $(0,0,d)$ and the observer at $(0,0,z)$,
$r = \sqrt{(z-d)^2} = |z-d|$. Then

$$\frac{\partial r^{-1}}{\partial z} = -\frac{1}{|z-d|^2}\cdot\frac{(z-d)}{|z-d|}
= -\frac{\operatorname{sgn}(z-d)}{(z-d)^2},$$

and at $z=0$ this is $+1/d^{2}$, so $g_z = Gm/d^{2}$ (positive downward toward
the mass). Dimensions: $\mathrm{m^3kg^{-1}s^{-2}}\cdot\mathrm{kg}\cdot
\mathrm{m^{-2}} = \mathrm{m\,s^{-2}}$. ✓

---

## ★★5 *(verified)*

$m = 350\cdot\frac43\pi(40)^3 = 350\cdot2.6808\times10^{5}
= 9.383\times10^{7}\ \mathrm{kg}$.

| $d$ (m) | $g_z = Gm/d^2$ (m/s²) | (mGal) | detectable? |
|---|---|---|---|
| 100 | $6.262\times10^{-8}$ | 0.006262 | no |
| 200 | $1.566\times10^{-8}$ | 0.001566 | no |
| 400 | $3.914\times10^{-9}$ | 0.000391 | no |

The combined uncertainty is $\sqrt{0.01^2+0.05^2} = 0.051$ mGal, so even the
shallowest case is a factor of 8 below the detection threshold. Conclusion:
**not detectable at any of these depths.** This is the correct outcome for a
small, modest-contrast body, and reporting it plainly is the point of a
feasibility calculation.

---

## ★★6

Peak at $x=0$: $g_z^\text{peak} = 2G\lambda d/d^2 = 2G\lambda/d$, so
$\propto d^{-1}$.

The difference from the sphere follows from the source's dimensionality: a
point mass has one characteristic length (its depth), while an infinite line has
a fixed cross-section regardless of depth. Adding the second horizontal
dimension (the 3-D case) adds one more power of $d$ in the kernel. Practical
consequence: **tabular bodies remain detectable to far greater depth than
equidimensional bodies of the same density contrast**, which is why dykes and
faults are classic gravity/magnetic targets.

---

## ★★7 *(verified)*

$|\mathbf{m}| = 3\cdot2\times10^{6} = 6\times10^{6}\ \mathrm{A\,m^2}$.

Directly above the dipole, $\mathbf{r}$ is vertical and
$\hat{\mathbf{r}} = \hat{\mathbf{z}}$, so
$\mathbf{B} = \frac{\mu_0}{4\pi}(2 M V / d^3)\hat{\mathbf{z}}$. With
$d = 200$ m and $\mu_0 = 1.2566\times10^{-6}$ H/m:

$$B_z = \frac{1.2566\times10^{-6}}{4\pi}\cdot\frac{2\cdot6\times10^{6}}{8\times10^{6}}
= 1.500\times10^{-7}\ \mathrm{T} = 150.0\ \mathrm{nT}.$$

Projections: $\Delta T = \hat{\mathbf{b}}\cdot\mathbf{B} =
150.0\sin(\text{inclination})$ nT, giving **0.0 nT at 0°, 106.1 nT at 45° and
150.0 nT at 90°**. The horizontal-field case (0°) gives no total-field anomaly
directly above the body — a null that is a property of the projection, not of
the magnetisation.

---

## ★★8 *(verified)*

$R = (9.6-8.0)/(9.6+8.0) = 1.6/17.6 = +0.0909$.

A second pair with the same $R$: scale both impedances by any factor, e.g.
$4.0\times10^{6}$ and $4.8\times10^{6}$ kg m⁻² s⁻¹, giving
$R = 0.8/8.8 = +0.0909$. At normal incidence the reflection coefficient depends
only on the *ratio*, so a density–velocity trade-off is invisible: increasing
$\rho$ and decreasing $v_p$ while holding $\rho v_p$ fixed changes nothing.
The data cannot separate the two ingredients.

---

## ★★★9

A good answer contains: (i) an objective stated numerically; (ii) the contrast
with an explicit source or an explicit synthetic statement; (iii) the correct
geometry — the 3-D point-mass formula only if the body is compact, the 2-D line
formula for a tabular body; (iv) each noise term listed separately, including a
geological term; (v) a CNR with the comparison threshold stated; and (vi) a
sensitivity statement naming the assumption whose factor-of-two error flips the
conclusion. Marks are lost for unlabelled "typical" property values and for
omitting units.

---

## ★★★10

Method: forward-model a compact body at a geometric sequence of depths, add
fixed absolute noise, fit mass (and optionally depth) by least squares, and
record the parameter uncertainty (from the covariance or by Monte Carlo).
Report the fitted log–log slope of uncertainty against depth.

Expected result: with the depth **fixed and known**, mass uncertainty scales as
$d^{2}$ for a point mass (amplitude $\propto d^{-2}$), because only the
amplitude changes. With the depth **free**, the uncertainty grows much faster
because the amplitude and the width trade off, which is the practical
realisation of the information penalty. The exponent therefore depends on the
source symmetry *and* on how many parameters are free — state which case you
measured. A defensible conclusion says: "for a fixed-known depth the measured
exponent was 2.0 ± 0.1 over the range 100–800 m; with depth free, 3.4 ± 0.3, and
the larger value reflects the width–depth trade-off rather than noise." Any
claim beyond the tested depth range should be flagged as extrapolation.
