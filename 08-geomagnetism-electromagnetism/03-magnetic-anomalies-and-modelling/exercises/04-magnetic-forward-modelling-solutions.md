# Solutions — 08-03-04 Forward Modelling Magnetic Bodies

> **Read after attempting the exercises.** The lesson is
> [04 Magnetic Forward Modelling](../04-magnetic-forward-modelling.md).

---

## ★1 — The charged disk at $h = R$

$$H_z = \frac{\sigma}{2}\left(1 - \frac{h}{\sqrt{R^{2}+h^{2}}}\right)_{h=R}
= \frac{1.0}{2}\left(1 - \frac{R}{\sqrt{2R^{2}}}\right)
= \frac{1}{2}\left(1 - \frac{1}{\sqrt2}\right) = \frac{0.29289}{2}
= 0.14645\ \mathrm{A\,m^{-1}} .$$

As a fraction of the infinite-sheet value $\sigma/2 = 0.5$ A m$^{-1}$, this is
$0.2929$, i.e. 29.3%. The transition from the near-field (nearly the sheet value)
to the far-field (a monopole $\propto h^{-2}$) happens over a few radii, which is
the same scale as the dipole-approximation criterion for a body.

---

## ★2 — Charges on a prism

With $M_x = 4.0$, $M_y = 0$, $M_z = 3.0$ A m$^{-1}$ and outward normals on the six
faces, $\sigma_m = \mathbf{M}\cdot\hat n$:

| Face | Outward normal | $\sigma_m$ (A m$^{-1}$) |
|---|---|---|
| $x = x_{\min}$ | $-\hat x$ | $-4.0$ |
| $x = x_{\max}$ | $+\hat x$ | $+4.0$ |
| $z = z_{\min}$ (top) | $-\hat z$ | $-3.0$ |
| $z = z_{\max}$ (bottom) | $+\hat z$ | $+3.0$ |
| $y = y_{\min}, y = y_{\max}$ | $\pm\hat y$ | $0$ |

Four charged faces, and two uncharged. Note that a *vertical* magnetisation would
charge only the top and bottom, which is why the far-field anomaly of a thin
vertical prism is dominated by a dipole whose axis is vertical.

---

## ★3 — Two representations

The **surface-charge** integral and the **volume-dipole** integral. They are
algebraically equivalent outside the body, but they are discretised differently
(faces versus cells), carry different singularities, and require different
quadratures and different sign conventions for the normals. Agreement between two
independent implementations to 0.1% is therefore evidence that both are correct,
whereas agreement of one implementation with itself is not evidence of anything.

---

## ★4 — The dipole failure factor

$$\frac{13856.4}{920.8} = 15.05 .$$

An inversion that fits single dipoles to anomalies measured directly above
shallow bodies is fitting a model whose error is a **factor of fifteen**, not a
few per cent. The result is a depth and a moment that are both wrong, in a way
that depends on the assumed body size — which the inversion does not know. The
only safe procedures are (i) to use a body model whose size is parametrised, or
(ii) to restrict the interpretation to anomalies measured several body widths
from the source, which for a shallow body means having data that extend far
beyond it.

---

## ★5 — Amplitude against burial depth

$$\frac{392.16}{1168.71} = 0.3355 \quad\Longrightarrow\quad \text{a factor of }2.98
\text{ less at }2.0\text{ km than at }0.5\text{ km}.$$

An inverse-cube law applied to the *centre* depth would predict
$\left(0.5/2.0\right)^{3} = 0.0156$, a factor of 64 — enormously stronger than
the observed factor of 3. The reason is that the body is 4 km wide, so even at
4 km depth the observation is not in the far field of a compact source: what is
sensed is the *top face*, whose solid angle falls much more slowly. The measured
per-kilometre decay of 2.5× (from the table) is an empirical property of a body
wide compared with its depth, and it is one reason depth estimation is
model-dependent.

---

## ★6 — Half-width against burial depth

$$\frac{2.65}{1.75} = 1.51 \quad\text{for a } 8\times \text{ change in top depth}
\left(0.5\to4.0\ \mathrm{km}\right).$$

The half-width grows by only 51% while the depth grows by a factor of eight,
because it is already dominated by the **body's own width** of 4 km. The practical
rule: for a body wide compared with its depth, the half-width measures the
*width*, and only for a compact or deeply buried body does it track the depth.
Attempting to read a depth from a half-width in the first regime produces an
answer that is too small and insensitive — a failure mode that the half-width
rule of [05 Depth Estimation](../05-magnetic-depth-estimation.md) shows in a
simpler setting.

---

## ★★7 — Experiment design (specification)

**Reference.** The surface-charge model, itself validated against the exact axial
disk field to $O(10^{-15})$ relative, on a fine quadrature ($48\times48$ nodes per
face or better).

**Geometry.** A prism of width $w$ and thickness $t$, magnetised at a fixed
direction; observations along a straight profile at horizontal offsets
$x = 0.5w, w, 2w, 3w, 5w, 10w$ at the surface; and additionally at the same
offsets with the *body* moved to a larger depth so that the profile spans the
same body-widths.

**Error control.** Because both the quadrature error and the approximation error
grow as the observation approaches the body, the two must be separated: refine the
quadrature at fixed geometry and confirm the reference has converged before
attributing the residual to the dipole approximation. Report the convergence of
the quadrature separately.

**Expected result.** The 5% threshold is crossed at about $2.5$–$3$ body widths
along the profile, consistent with the demonstration's 8.2% at two body widths
(8 km for a 4 km wide body) and 3.9% at three.

---

## ★★8 — What the 0.096% residual measures

It measures the **discretisation of the volume sum**: the cells are cubes whose
magnetisation is placed at their centres, so the body is represented as a
distribution of point dipoles rather than as a continuum. The staircase
approximation at the boundary of the body is the dominant term, and it is
second-order in the cell size because errors on opposite sides of the boundary
partially cancel.

Refining by a factor of two in each direction reduces the cell volume by eight and
the boundary error by about $\left(1/2\right)^{2} = 1/4$, so the residual should
fall to roughly $0.02$–$0.03\%$ of the peak. If it does not, the surface-charge
quadrature (not refined) becomes the limiting error and the comparison loses its
diagnostic value.

---

## ★★9 — A strongly magnetic body

With $\chi = 1.0$ the induced magnetisation is comparable to $H_0$, so the body's
own field is a significant fraction of the field it is responding to. The internal
field is then $H_0$ minus the demagnetising field $N M$, which depends on the
body's *shape*; for a flat or elongated body the demagnetising factor varies from
point to point, so the magnetisation is not uniform. The consequences:

- the anomaly is no longer the field of a uniformly charged surface, and the
  effective moment is *smaller* than $\chi H_0 V$ because the interior field is
  reduced;
- the reduction depends on orientation, so the anomaly's direction dependence
  differs from the $\cos$-type projection of the uniform case;
- in the limit $\chi\to\infty$ the moment saturates, as quantified for a sphere in
  [07 Applications](../07-magnetic-uses.md), where $M\to3H_0$ regardless of
  composition.

The correct treatment is a self-consistent (demagnetisation) forward model or a
finite-element solution of the magnetostatic problem.
