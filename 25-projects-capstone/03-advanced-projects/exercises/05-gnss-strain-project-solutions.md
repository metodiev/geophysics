# Solutions — 25-03-05 Project: GNSS Strain Rate Estimation

> Read after attempting. Lesson:
> [05 GNSS Strain Rate](../05-gnss-strain-project.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/gnss_strain_demo.py`](../code/gnss_strain_demo.py).

---

## ★1 — Velocity difference to strain rate

$$\frac{3\ \mathrm{mm\,yr^{-1}}}{50\ \mathrm{km}}
= 0.06\ \mathrm{mm\,yr^{-1}\,km^{-1}},$$

and with $1\ \mathrm{mm\,yr^{-1}\,km^{-1}} = 1000\
\mathrm{nanostrain\,yr^{-1}}$:

$$0.06 \times 1000 = 60\ \mathrm{nanostrain\,yr^{-1}} = 6\times10^{-8}\
\mathrm{yr^{-1}}.$$

Unit algebra: $\mathrm{mm\,yr^{-1}/km} = 10^{-3}\ \mathrm{m\,yr^{-1}}/10^{3}\
\mathrm{m} = 10^{-6}\ \mathrm{yr^{-1}}$, and $1\ \mathrm{nanostrain\,yr^{-1}} =
10^{-9}\ \mathrm{yr^{-1}}$, so the factor is $10^{3}$ ✔. A 60 nanostrain yr⁻¹ rate
is very fast — comparable to a plate-boundary zone — which is the right order for a
3 mm yr⁻¹ signal across only 50 km.

---

## ★2 — Principal rates, azimuth and dilatation

$$\text{mean} = \frac{e_{xx}+e_{yy}}{2} = \frac{20 + (-5)}{2} = 7.5,$$

$$\text{dev} = \sqrt{\left(\frac{e_{xx}-e_{yy}}{2}\right)^{2} + e_{xy}^{2}}
= \sqrt{12.5^{2} + 12^{2}} = \sqrt{156.25 + 144} = \sqrt{300.25} = 17.328,$$

$$e_1 = 7.5 + 17.328 = +24.828\ \mathrm{nanostrain\,yr^{-1}},$$

$$e_2 = 7.5 - 17.328 = -9.828\ \mathrm{nanostrain\,yr^{-1}},$$

$$\theta = \frac{1}{2}\arctan\!\left(\frac{2 \times 12}{20 - (-5)}\right)
= \frac{1}{2}\arctan(0.96) = \frac{43.83°}{2} = +21.92°.$$

Dilatation rate: $\operatorname{tr}\mathbf{e} = 20 - 5 = +15\
\mathrm{nanostrain\,yr^{-1}}$ — the region is extending in area, which is
consistent with both principal axes being large and positive on average.

---

## ★3 — The shear component and the rotation sign

$$\mathbf{e}_{xy} = \frac{G_{xy} + G_{yx}}{2} = \frac{5.579 + 9.576}{2}
= 7.578\ \mathrm{nanostrain\,yr^{-1}},$$

matching the printed $7.577$ (the $0.001$ difference is rounding of the printed
coefficients).

$$\omega = \frac{G_{yx} - G_{xy}}{2} = \frac{9.576 - 5.579}{2}
= +1.999\ \mathrm{nanostrain\,yr^{-1}},$$

again matching the printed value.

**Why the sign is positive.** With $x$ east and $y$ north, the antisymmetric part
of the gradient represents a rotation whose rate is
$\omega = \tfrac{1}{2}(\partial v_y/\partial x - \partial v_x/\partial y)$,
positive **counter-clockwise** (from east toward north). The shear strain
$\mathbf{e}_{xy}$ is the *sum* of the same two coefficients, because it measures
the average of the two off-diagonal components — the symmetric combination — while
the rotation is their difference. Adding a pure rotation changes $G_{xy}$ and
$G_{yx}$ by equal and opposite amounts, leaving $\mathbf{e}$ untouched: that is
precisely why a strain tensor can be computed from a velocity field without first
knowing the reference frame's rotation, and why a *frame* error changes only
$\omega$.

---

## ★★4 — Rotation, dilatation and misfits

$$\omega = \frac{9.576-5.579}{2} = +1.999
\qquad (\text{true } +5.0),$$

$$\operatorname{tr}\mathbf{e} = 23.636 + (-20.913) = +2.723
\qquad (\text{true } +10.0),$$

both in nanostrain yr⁻¹, confirming the demonstration.

**Propagated formal errors.** Since the combination is linear,

$$\sigma_\omega = \tfrac{1}{2}\sqrt{\sigma_{xy}^{2}+\sigma_{yx}^{2}}
= 0.5\sqrt{2.753^{2}+3.147^{2}} = 0.5 \times 4.182 = 2.091,$$

$$\sigma_{\text{dil}} = \sqrt{3.147^{2}+2.753^{2}} = 4.182.$$

**Misfits in units of the formal error:**

| quantity | misfit | in σ |
|---|---|---|
| $\partial v_x/\partial x$ | $23.636-25.000 = -1.364$ | $-0.43$ |
| $\partial v_y/\partial y$ | $-20.913+15.000 = -5.913$ | $-2.15$ |
| $\omega$ | $1.999-5.000 = -3.001$ | $-1.44$ |
| dilatation | $2.723-10.000 = -7.277$ | $-1.74$ |

**Worst determined:** $\partial v_y/\partial y$ at $-2.15\sigma$, and the dilatation
follows it at $-1.74\sigma$ because it is that same component summed with a
well-determined one. All four are within two sigma of a $0.5\
\mathrm{mm\,yr^{-1}}$ noise level except the north-gradient, which sits just
outside — entirely unremarkable for a single realisation, and a reminder that the
formal error is a statement about the ensemble, not about this one field.

---

## ★★5 — The aperture ratio

$$\frac{7.283}{2.950} = 2.469.$$

**Expected from a simple argument.** Twelve stations distributed uniformly over a
$200\times200$ km box: the nearest six occupy roughly the inner half of the *area*,
so their linear aperture is about $\sqrt{1/2} = 0.71$ of the full aperture, i.e.
about 141 km.

The gradient's standard error scales as
$\sigma_G \propto \sigma_v/(L\sqrt{N})$. Halving the station count multiplies the
error by $\sqrt{2} = 1.414$; shrinking the aperture to $0.71L$ multiplies it by
$1/0.71 = 1.408$. The predicted ratio is therefore
$1.414 \times 1.408 = 1.99$, against the measured $2.47$ — the extra $24\%$ comes
from the inner subnetwork's geometry, whose points are less favourably spread for a
four-parameter fit.

**The trade in one sentence.** A smaller network averages the strain rate over a
shorter length scale, at the cost of a formal uncertainty that grows roughly as the
inverse of the aperture and the square root of the station count, so resolution and
precision cannot both be improved by making the network smaller or larger.

---

## ★★6 — Outlier: residuals versus formal errors

$$\text{residual sd factor} = \frac{2.2185}{0.4603} = 4.82,$$

$$\text{formal error factor} = \frac{14.218}{2.950} = 4.82.$$

They are **identical**, and necessarily so: the formal error is computed from the
residual variance, so contaminating one station inflates both together. The
outlier does not sneak past the uncertainty; it enlarges it.

**The diagnostic a practitioner should use.** Compare the residual standard
deviation with the *input* velocity uncertainty that was assumed when the solution
was computed: here $0.5\ \mathrm{mm\,yr^{-1}}$, against a residual sd of
$2.2185$ in the contaminated fit — a ratio of $4.4$. Any ratio appreciably above
1 (say above 1.5–2) means one of three things, in order of likelihood: an outlier
velocity, an underestimated input uncertainty, or a deformation field that the
uniform-strain model cannot represent. The residual *pattern* distinguishes them:
an outlier gives one large residual at one station, a wrong noise model gives
uniformly scaled residuals, and a model failure gives residuals correlated with
position.

---

## ★★★7 — Designing for $2\ \mathrm{nanostrain\,yr^{-1}}$

**Propagation.** For a single gradient component fitted to $N$ stations spread over
an aperture $L$, with uncorrelated velocity errors $\sigma_v$,

$$\sigma_G = \sigma_v\sqrt{\frac{12}{N L^{2}}}
= \frac{3.464\,\sigma_v}{L\sqrt{N}}
\quad\text{(velocity units per length)}.$$

With $\sigma_v = 0.5\ \mathrm{mm\,yr^{-1}}$ and the unit bridge of
$1000\ \mathrm{nanostrain\,yr^{-1}}$ per mm yr⁻¹ km⁻¹,

$$\sigma_G\ [\mathrm{nanostrain\,yr^{-1}}]
= \frac{1000 \times 3.464 \times 0.5}{L\,\sqrt{N}}
= \frac{1732}{L\,\sqrt{N}}.$$

**Station count and aperture.** Requiring $\sigma_G \le 2$ and allowing a safety
factor of $1.5$ for the fact that a principal rate's error can exceed a component's
(quadrature of two components):

$$\frac{1732}{L\sqrt{N}} \le \frac{2}{1.5} = 1.333
\;\Longrightarrow\;
L\sqrt{N} \ge 1299.$$

For a zone 100 km wide, an aperture $L = 200\ \mathrm{km}$ gives
$\sqrt{N} \ge 6.5$, i.e. $N \ge 42$ stations; $L = 300\ \mathrm{km}$ gives
$N \ge 19$. The aperture is the stronger lever because the error scales as
$1/L$ while it scales only as $1/\sqrt{N}$: **doubling the aperture is worth four
times as many stations.**

**Distribution.** Uniform coverage of the aperture, with a modest densification in
the interior, because the leverage of a station grows with its distance from the
centroid; a network with all its stations clustered at the edges and none inside
is efficient for the gradient but cannot detect a strain-rate *gradient*, which is
usually the actual target.

**Covariance assumption (the item that decides the design).** The formula above
assumes uncorrelated station velocities. Real GNSS velocities carry
**common-mode** errors — orbit, reference-frame and large-scale atmospheric
loading errors shared across a network — plus **spatially correlated** errors with
a length scale of hundreds of kilometres. Two consequences:

1. A *uniform* common-mode velocity is annihilated by the gradient operator, so it
   costs nothing; this is the reason strain rates are more robust than velocities.
2. A *spatially varying* common-mode error (a tilt across the network) is
   **indistinguishable from strain rate** and cannot be removed by any statistical
   treatment of a single network's data. The defensible response is to estimate a
   common-mode filter (a Helmholtz decomposition of the velocity field, or a
   reference-frame alignment) and then to inflate the formal errors by the residual
   variance factor; the design must therefore include **more stations than the
   count above suggests** whenever the common-mode error is not independently
   constrained.

**The test that shows the requirement is not met.** After the fit, compare the
residual standard deviation with the input velocity uncertainty. If the ratio
exceeds about $1.5$, the error model is wrong or the field is non-uniform, and the
formal $2\ \mathrm{nanostrain\,yr^{-1}}$ claim is unsupported. Three additional
checks belong in the same breath: refit on two halves of the network and require
consistency within the formal errors; fit quadratic terms and require them to be
insignificant; and compare with an independently derived moment rate from
seismicity, since a GNSS strain rate and a seismic moment rate must be compatible
over a seismic cycle.
