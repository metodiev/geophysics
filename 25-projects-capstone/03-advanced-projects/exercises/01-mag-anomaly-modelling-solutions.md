# Solutions — 25-03-01 Project: Magnetic Anomaly Modelling and Depth Estimation

> Read after attempting. Lesson:
> [01 Magnetic Anomaly Modelling](../01-mag-anomaly-modelling.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/mag_anomaly_modelling_demo.py`](../code/mag_anomaly_modelling_demo.py).

---

## ★1 — The anomaly at the source position

$$T(x) = k\,\frac{z\cos\theta + (x-x_0)\sin\theta}{(x-x_0)^{2}+z^{2}}.$$

At $x = x_0$ the sine term vanishes:

$$T(x_0) = \frac{k\cos\theta}{z}.$$

For $\theta = 0$: $T = 1000 \times 1 / 4.0 = 250.0\ \mathrm{nT}$ — the
demonstration's body A peak.

For $\theta = 40°$: $T = 1000 \times 0.76604 / 4.0 = 191.5\ \mathrm{nT}$. The
demonstration's body B *peak* is $220.7\ \mathrm{nT}$, larger than the value at
$x_0$, because the skewed anomaly's maximum is displaced: the peak is not at the
source position at all. That displacement is the whole difficulty of §4.

Unit: $[\mathrm{nT\,km}]/[\mathrm{km}] = \mathrm{nT}$ ✔.

---

## ★2 — Half-width of the symmetric anomaly

With $\theta = 0$, $T(x) = kz/((x-x_0)^{2}+z^{2})$, so $T(x_0) = k/z$ and

$$\frac{T(x)}{T(x_0)} = \frac{z^{2}}{(x-x_0)^{2}+z^{2}}
= \frac{1}{2}
\;\Longrightarrow\;
(x-x_0)^{2} = z^{2}
\;\Longrightarrow\;
x_{1/2} = z.$$

The half-width **is** the depth, which is the depth rule for a symmetric line
source: $z = x_{1/2}$. The demonstration confirms it for body A,
$x_{1/2} = 4.000\ \mathrm{km}$ against $z = 4.0\ \mathrm{km}$ exactly.

The rule is only valid at $\theta = 0$. At $40°$ the same rule returns
$4.594\ \mathrm{km}$, a $+14.8\%$ error, which is why the analytic signal of §5 is
preferred.

---

## ★3 — Verifying the gradient pair

$$\left|\mathrm{AS}\right| = \sqrt{40.0740^{2} + (-47.3815)^{2}}
= \sqrt{1605.93 + 2245.01} = \sqrt{3850.94}
= 62.06\ \mathrm{nT\,km^{-1}}.$$

The demo's |AS| peak of $61.1388\ \mathrm{nT\,km^{-1}}$ occurs at $x = 8.00\
\mathrm{km}$ but with the *smoothed* derivative, whereas the printed gradient
values at $x = 8.00$ are the smoothed pair used in the same computation;
$62.06$ here is the value at the centre from the printed numbers, and the small
difference from $61.1388$ is the neighbouring-sample value of the peak of a
Lorentzian sampled at 0.2 km (the true peak lies between samples). Against the
exact $k/z^{2} = 62.5000\ \mathrm{nT\,km^{-1}}$, the reconstruction is within
$0.7\%$ — the residual being the finite-difference and smoothing loss.

---

## ★★4 — Recovering the three parameters

$$k = \frac{1}{a} = \frac{1}{2.5\times10^{-2}} = 40\ \mathrm{nT\,km},$$

$$x_0 = -\frac{b}{2a} = -\frac{-0.4}{2 \times 0.025} = +8.0\ \mathrm{km},$$

$$z = \sqrt{\frac{c}{a} - x_0^{2}} = \sqrt{\frac{2.0}{0.025} - 8.0^{2}}
= \sqrt{80 - 64} = \sqrt{16} = 4.0\ \mathrm{km}.$$

**Which coefficient controls what.**

- $a$: sets the *amplitude* $k$; it is the curvature of the reciprocal parabola.
- $b$: sets the *position* $x_0$; it is the parabola's tilt.
- $c$: with $a$ and $x_0$, sets the *depth*; it is the parabola's intercept.

Units: $a$ in $(\mathrm{km\,nT})^{-1}$, $b$ in $\mathrm{nT^{-1}}$, $c$ in
$\mathrm{km\,nT^{-1}}$ — each obtained by requiring the three terms of
$1/|\mathrm{AS}|$ (unit $\mathrm{km\,nT^{-1}}$) to be homogeneous.

---

## ★★5 — Three biases, two causes

| measurement | value (km) | bias |
|---|---|---|
| body A anomaly half-width ($\theta = 0$) | $4.000$ | $0.0\%$ |
| body B anomaly half-width ($\theta = 40°$) | $4.594$ | $+14.8\%$ |
| body B $|\mathrm{AS}|$ half-width | $4.160$ | $+4.0\%$ |

Both biased figures are computed from the same body at the same depth, so the
comparison isolates the cause:

- the **$+14.8\%$** is **magnetisation-driven**: it is the skew's effect on the
  anomaly's shape, and it would vanish at $\theta = 0$;
- the **$+4.0\%$** is **discretisation-driven**: it is present even for the
  symmetric body's analytic signal, and comes from the finite-difference
  derivative plus the 5-point smoothing over 1 km, which broadens the apparent
  Lorentzian.

The practical consequence is that de-skewing (or using the analytic signal) fixes
the first term but not the second, and the second is the floor on this method's
depth accuracy at 0.2 km sampling.

---

## ★★6 — The trend as a fraction of the signal

$$\frac{c}{\left|\partial T/\partial x\right|_\text{max}}
= \frac{8.0}{54.82} = 14.6\%.$$

**Why a constant offset distorts a Lorentzian but a constant level does not.**
$|\mathrm{AS}| = \sqrt{u^{2}+v^{2}}$ is non-linear in $u$ and $v$, so inserting
$u \to u+c$ produces $\sqrt{(u+c)^{2}+\mathcal{H}(u+c)^{2}}$, which is a *different
function of $x$*, whereas adding a constant to $T$ before differentiating leaves
$\partial T/\partial x$ unchanged — the derivative annihilates it exactly. A
14.6% offset in the derivative is not a small perturbation of a function whose
half-width is meant to be read to a few percent, which is why the demonstration's
$8\ \mathrm{nT\,km^{-1}}$ case moves the raw estimate from $4.195$ to
$4.515\ \mathrm{km}$.

---

## ★★★7 — Joint depth and magnetisation from a grid

**Data.** Total-field anomaly on a regular grid over the source, with flight (or
station) altitude and a line spacing of at most a few source depths — for a
target at 1 km depth, a 200–400 m line spacing. The anomaly must be reduced to
the pole or explicitly modelled with its true field direction, since the
geomagnetic inclination is one of the unknowns.

**Parameterisation.** A compact source as either (a) a uniformly magnetised
**prism** with parameters (centre $x_0, y_0$, depth to top $h$, horizontal
dimensions, thickness, magnetisation vector $\mathbf{M}$ with two angles), or
(b) a **dipole** with $(x_0,y_0,z,M,\theta_M,\phi_M)$. Either way there are two
geometric families and two magnetisation angles.

**Objective.** Least squares of the gridded predicted against observed anomaly,
with a weight matrix that includes the field-removal uncertainty, plus
regularisation on the magnetisation magnitude only if a physical bound exists.
A **reduction-to-the-pole** operator can be applied to the data instead of
modelling the direction, but at the cost of amplifying noise along the
magnetisation direction.

**Expected non-uniqueness and the specific trade-off.** The dominant degeneracy
is **depth against magnetisation magnitude**: a deeper source with a larger
$\mathbf{M}$ produces almost the same amplitude, exactly as in the gravity case.
In addition — and this is the magnetic-specific one — **inclination trades against
source elongation and against the remanence direction**: a rotation of $\mathbf{M}$
can be partly compensated by a rotation of the body's long axis, so an unconstrained
joint fit can return a body whose strike is wrong by tens of degrees. The
parameter that is best constrained is the **depth-to-top divided by the horizontal
extent** (a shape ratio), and the worst constrained is the split between induced
and remanent magnetisation.

**The independent observation.** The **Koenigsberger ratio** from oriented
samples, or better a **palaeomagnetic measurement** giving the natural remanent
magnetisation direction, breaks the induced/remanent split. Absent a sample, a
**borehole intersection** fixes $h$; and a **magnetic gradient (tensor) survey**
constrains depth much better than the total field because the gradient falls off
faster with distance and therefore weights the shallowest part of the source.

**The test that the estimator works.** Generate synthetic grids from a known
model at several field inclinations and noise levels, invert each, and show that
the recovered $h$ is unbiased within its stated uncertainty while the recovered
magnetisation angle carries the expected large error bar; then show that adding
the tensor data narrows the magnetisation angle interval by the predicted factor.
An estimator whose synthetic recovery has never been measured is not validated.
