# Solutions — 19-05-02 Boundary Element Methods for Potential Fields

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs. All models are **SYNTHETIC**.

Lesson: [02 Boundary Element Methods for Potential Fields](../02-boundary-element.md).

---

## ★1 — The self term at $N = 32$

$$L = 2(10\,000)\sin(\pi/32) = 20\,000\sin(5.625^{\circ})
= 20\,000(0.098017) = 1960.34\ \mathrm{m}.$$

$$G_{ii} = -\frac{1}{2\pi}(1960.34)\left(\ln\frac{1960.34}{2}-1\right)
= -312.00\,(6.8811-1) = -1834.9 .$$

The arc length at this resolution is $2\pi(10\,000)/32 = 1963.5$ m, so the chord
is $0.16\%$ shorter — the geometric error the row-sum table measures.

---

## ★2 — Why the diagonal of $H$ vanishes

$$H_{ii} = \int_{\Gamma_i}\frac{\partial G}{\partial n'}\,\mathrm{d}l'
= -\frac{1}{2\pi}\int_{\Gamma_i}\frac{(\mathbf{r}'-\mathbf{r}_i)\cdot
\mathbf{n}'_i}{|\mathbf{r}_i-\mathbf{r}'|^{2}}\,\mathrm{d}l' = 0,$$

because a straight panel has $(\mathbf{r}'-\mathbf{r}_i)\perp\mathbf{n}'_i$ for
every $\mathbf{r}'$ on it, so the integrand vanishes identically rather than
merely integrating to zero. This is why a polygonal boundary needs no special
self-term quadrature for $H$ while $G$ does.

---

## ★3 — Why the wrong free term gives almost exactly $2$

For $u = \cos3\theta$ on $r = a$, the interior flux is
$q_{\text{int}} = +3\cos(3\theta)/a$ and the exterior one is its negative, because
the exterior normal points the other way. The maximum relative error of one
against the other is

$$\frac{\max|q_{\text{int}} - q_{\text{ext}}|}{\max|q_{\text{ext}}|}
= \frac{2\max|q_{\text{ext}}|}{\max|q_{\text{ext}}|} = 2,$$

measured as $2.0082$; the extra $0.0082$ is the panel discretisation error of the
same order as the $6.8589\times10^{-3}$ in the correct case. A factor near two is
the signature of a sign error, and it is the reason the exterior test is worth
running even when the interior one passes.

---

## ★4 — Order of the row-sum deviation

Deviations: $7.813\times10^{-3}$ at $N = 64$ and $1.953\times10^{-3}$ at
$N = 256$. The ratio is $4.000$ over a factor of $4$ in $N$, so the deviation
falls as $1/N$: **first order** in the panel length.

At $N = 1024$, $N$ increases by $4$ from $256$, so the deviation is
$1.953\times10^{-3}/4 = 4.88\times10^{-4}$. The deviation is the
chord-versus-arc deficit, which is $O(h^{2})/h = O(h)$ per unit length once
normalised by the panel length; the measured first order is the geometric error of
a straight-panel approximation.

---

## ★5 — The row-sum correction

Improvement factor at $N = 128$: $8.776359\times10^{-3}/9.587218\times10^{-4}
= 9.15$. The corrected column gives $3.654250\times10^{-3}$ at $N = 64$ and
$9.587218\times10^{-4}$ at $N = 128$:

$$\text{order} = \log_2\frac{3.654250\times10^{-3}}{9.587218\times10^{-4}}
= \log_{2}3.812 = 1.93 .$$

So the corrected flux converges at essentially **second order** — the flat-panel
normal error has been removed by construction, and what remains is the quadrature
and the remaining curvature error. The lesson's claim "the flux error is mostly
the free-term error" is supported by the change in order, not only by the factor.

---

## ★6 — Which route for which problem

- **2-D interior:** unknowns ratio $16\,384/128 = 128$ in favour of the boundary
  method, but accuracy ratio $6.7720\times10^{-7}/5.9824\times10^{-4} = 1.13\times10^{-3}$
  in favour of the volume grid. At matched accuracy the volume grid wins, and the
  measured evidence is the table itself.
- **3-D exterior:** the boundary method needs a surface ($n^{2}$) instead of a
  volume ($n^{3}$), a ratio of $128$ at $128$ nodes per direction in each case —
  and it needs no truncation radius at all, which the truncation table shows
  costing $10^{-3}$ at $R/a = 10$. Both effects point the same way.

The deciding ratio in 2-D is accuracy per unknown (volume grid wins); in 3-D it
is unknowns to reach an accuracy (boundary method wins), and the two questions
must not be conflated.

---

## ★7 — Geometry or quadrature?

- **Flat-panel geometry error** is $O(h)$ per panel and is *geometric*: it
  depends on the angle between the chord and the arc, so it depends on $N$ only
  and not on the quadrature order.
- **Panel quadrature error** depends on the number of Gauss nodes per panel.

The experiment: refine $N$ at fixed Gauss order and at a much higher Gauss order.
If the error curve is unchanged, the quadrature is converged and the geometry is
limiting. If the higher-order curve lies below the lower one at the same $N$, the
quadrature is contributing. The row-sum deviation supplies an independent
observable: since it is a pure geometry measure (the free-term deficit) and it
falls at the same first order as the flux error, the geometry is the limiting
factor.

---

## ★8 — The truncation exponent

Ratios: $1.2500\times10^{-1}/1.5625\times10^{-2} = 8$ for $R/a: 2\to4$;
$1.5625\times10^{-2}/1.0000\times10^{-3} = 15.6$ for $4\to10$. A power law
$(a/R)^{m}$ gives $m = \ln 8/\ln 2 = 3$ for the first pair and
$m = \ln 15.6/\ln 2.5 = 3.0$ for the second — but the closed form is
$c\,(r^{3} - R^{6}/r^{3})$ with $c \approx a^{6}/R^{6}$ for large $R$, so the
error scales as $(a/R)^{6}$ evaluated near $r = a$ where the $r^{-3}$ term is
largest: the first two rows are not yet in the $R^{-6}$ regime, and the
$R/a = 100$ value confirms it
($1.5625\times10^{-2}\cdot(4/100)^{6} \approx 1.6\times10^{-8}$ is smaller than
the printed $10^{-6}$, so the asymptotic constant has not settled).

For a target of $1.733\times10^{-4}$ the interpolated rows give $R/a \approx 24$:
between $R/a = 10$ ($10^{-3}$) and $R/a = 100$ ($10^{-6}$), a factor of $5.8$ in
error takes $\log(5.8)/\log(10)$ of the interval in $R/a$, i.e.
$R/a \approx 10\cdot10^{0.38} \approx 24$. A volume solve of this exterior problem
therefore needs a grid extending to $24$ times the body radius for the accuracy
the boundary method reached at $r = 3a$.
