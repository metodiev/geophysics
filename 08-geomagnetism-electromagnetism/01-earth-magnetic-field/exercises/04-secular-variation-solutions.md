# Solutions — 08-01-04 Secular Variation, Jerks and Core Dynamics

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [04 Secular Variation, Jerks and Core Dynamics](../04-secular-variation.md).

---

## ★1 — A secular variation from two samples

$$\dot{g}_1^0 = \frac{-30132-(-30120)}{1\ \mathrm{yr}}
= -12\ \mathrm{nT\,yr^{-1}}.$$

Per second, dividing by the number of seconds in a Julian year:

$$\dot{g}_1^0 = \frac{-12}{3.1557\times10^{7}}
= -3.803\times10^{-7}\ \mathrm{nT\,s^{-1}}
= -3.803\times10^{-16}\ \mathrm{T\,s^{-1}}.$$

Two-sample differences are secants, not derivatives: with only two samples you
cannot distinguish a constant rate from a rate that changed between them.

---

## ★2 — Characteristic timescale

$$\tau = \frac{|g_1^0|}{|\dot{g}_1^0|} = \frac{28000}{35}
= 800\ \mathrm{yr}.$$

This is the time the coefficient would take to change by its own magnitude at
the current rate. It is a **ratio of observed quantities**, not a physical
constant: the same definition applied to [08-01-04](../04-secular-variation.md)
§1.1 gave 2500 yr, 1326 yr and 912 yr at three different epochs of the same
synthetic series.

---

## ★3 — Drift rate to speed

One degree of longitude at the equator:

$$\frac{2\pi a}{360} = \frac{2\pi\times6371\ \mathrm{km}}{360}
= 111.195\ \mathrm{km}.$$

Then

$$0.20\ \mathrm{deg\,yr^{-1}} = 0.20\times111.195
= 22.239\ \mathrm{km\,yr^{-1}}
= 2.2239\times10^{4}\ \mathrm{m\,yr^{-1}},$$

$$u = \frac{2.2239\times10^{4}}{3.1557\times10^{7}}
= 7.047\times10^{-4}\ \mathrm{m\,s^{-1}}.$$

For comparison, the lesson's $0.150\ \mathrm{deg\,yr^{-1}}$ gave
$5.285\times10^{-4}\ \mathrm{m\,s^{-1}}$; the ratio is exactly
$0.20/0.15 = 1.333$. ✔ The speed is a **phase** speed of a pattern, not the
speed of any material point.

---

## ★4 — Phase of a harmonic pattern

Take the pattern sampled on a uniform grid with weights $w_k$, so
$p_k = \cos m(\phi_k-\Delta)$. Then

$$C = \sum_k \cos m(\phi_k-\Delta)e^{-im\phi_k}
= \tfrac{1}{2}\sum_k\left(e^{im(\phi_k-\Delta)}+e^{-im(\phi_k-\Delta)}\right)
e^{-im\phi_k}$$
$$= \tfrac{1}{2}\sum_k\left(e^{-im\Delta} + e^{-2im\phi_k}e^{im\Delta}\right).$$

For $m\ge1$ and a uniform grid covering a whole number of periods the second sum
vanishes, so $C = \tfrac{1}{2}e^{-im\Delta}$ and
$\arg C = -m\Delta$. Therefore

$$\Delta = -\frac{1}{m}\arg C.$$

With $m = 2$ and $\Delta = 1.2^{\circ}$: $m\Delta = 2.4^{\circ}$, so
$\arg C = -2.4^{\circ}$ and the recovery returns $\Delta = 1.2^{\circ}$ exactly at
grid resolution. (The lesson's demonstration used a westward shift, obtaining
$-1.5^{\circ}$ for a $0.15\ \mathrm{deg\,yr^{-1}}$ drift over 10 yr, i.e.
$1.5^{\circ}$ westward.)

**Ambiguity.** $\arg C$ is defined modulo $360^{\circ}$, so $m\Delta$ is known
modulo $360^{\circ}$ and $\Delta$ modulo $360^{\circ}/m$: for $m = 2$,
$180^{\circ}$. The *usable* half of that is the $\pm90^{\circ}$ range quoted in
the lesson, because a shift of $90^{\circ}$ puts the pattern onto the complement
of itself and the correlation drops.

**Aliasing over 8 yr.** The maximum unambiguous shift is $90^{\circ}$, so the
maximum unambiguous rate is

$$r_{\text{alias}} = \frac{90^{\circ}}{8\ \mathrm{yr}}
= 11.25\ \mathrm{deg\,yr^{-1}}.$$

Any faster drift produces a recovered rate that is wrong by a multiple of
$2\times11.25 = 22.5\ \mathrm{deg\,yr^{-1}}$.

---

## ★5 — Noise gain of centred difference estimators

Let $E_i$ be independent samples with variance $\sigma^2$.

**SV estimator.** $\hat{E}'_i = (E_{i+1}-E_{i-1})/(2\Delta t)$. The two samples are
independent, so

$$\mathrm{Var}\,\hat{E}'_i = \frac{\sigma^2+\sigma^2}{(2\Delta t)^2}
= \frac{\sigma^2}{2\Delta t^2}
\quad\Longrightarrow\quad
\sigma_{\text{SV}} = \frac{\sigma}{\Delta t\sqrt{2}}.$$

With $\Delta t = 1\ \mathrm{yr}$: $\sigma_{\text{SV}} = \sigma/\sqrt{2}
= 0.7071\,\sigma$, the lesson's $\sqrt{1/2}$ factor. The Monte Carlo measured
$0.7062$ against $0.7071$. ✔

**Acceleration estimator.** $\hat{E}''_i = (E_{i+2}-2E_i+E_{i-2})/4$. The
coefficients are $(1,-2,1)$, so

$$\mathrm{Var} = \frac{(1)^2+(-2)^2+(1)^2}{4^2}\sigma^2
= \frac{6}{16}\sigma^2
\quad\Longrightarrow\quad
\sigma_{\text{acc}} = \frac{\sqrt{6}}{4}\sigma = 0.6124\,\sigma.$$

Monte Carlo: $0.6114$ against $0.6124$. ✔

The general rule: for a centred estimator with weights $c_j$,
$\sigma_{\hat E^{(k)}} = \sigma\sqrt{\sum_j c_j^2}$; the lesson's jerk stencil
$(1,-3,3,-1)/8$ gives $\sqrt{20}/8 = 0.5590$, measured $0.5581$.

---

## ★6 — Error of a stale secular-variation model

Let the slope change at $t_c = 2000$ from $\dot{g}_{\text{old}} = -30$ to
$\dot{g}_{\text{true}} = -45\ \mathrm{nT\,yr^{-1}}$, and let the model be fitted
at $t_0 = 1995$ with the old slope. The modelled value at time $t$ is

$$g_{\text{mod}}(t) = g(t_0) + \dot{g}_{\text{old}}(t-t_0),$$

while the true value is

$$g_{\text{true}}(t) = g(t_0) + \dot{g}_{\text{old}}(t-t_0)
+ \left(\dot{g}_{\text{true}}-\dot{g}_{\text{old}}\right)
\max(t-t_c,\,0).$$

Subtracting, the error is

$$\Delta g(t) = -\left(\dot{g}_{\text{true}}-\dot{g}_{\text{old}}\right)
\max(t-t_c,\,0) = -\left(-15\right)\max(t-t_c,\,0)
= +15\,\max(t-t_c,\,0)\ \mathrm{nT},$$

so it is **zero until the slope changes and linear afterwards**:

| year | $t - t_c$ (yr) | $\Delta g$ (nT) |
|---|---|---|
| 2000 | 0 | 0 |
| 2010 | 10 | +150 |
| 2025 | 25 | +375 |

The linear growth is the point: the error is the integral of a *constant* slope
mismatch, so its rate of growth is set by the mismatch and its size by the time
since the change. Extrapolating further does not accelerate the error; it only
prolongs it.

---

## ★7 — A jerk-detection experiment (specification)

**Metric.** Fit a piecewise-linear-plus-quadratic model in time to each Gauss
coefficient:

$$g(t) = a + b\,t + c\left[(t-t_c)H(t-t_c)\right]
+ d\left[(t-t_c)^2H(t-t_c)\right],$$

with $H$ the unit step. The jerk parameter is $c$ (the slope change); report
$c$ with its formal standard error from the linear fit, since the fit error
inflates correctly with the noise.

**Window length.** The record must span at least $5$ times the anticipated rise
time of the transition on *both* sides of the candidate epoch, or the slope
change is not identifiable separately from curvature. For a $\sim3$ yr rise time
that is a 15 yr quiet interval before and after.

**The trade-off.** For drift we want short intervals (§2.2 aliasing); for
derivative estimation we want long intervals and heavy averaging (§4 noise
gains). The resolution is to use *all* the data in a single global fit rather
than successive short differences, and to report the drift estimate and the jerk
estimate from the same fit so their covariance is known.

**Falsification.** A claimed jerk epoch is falsified if (a) removing the
single largest year of data moves the epoch by more than the formal error;
(b) the fitted $c$ is not significant at the level of the data noise propagated
by §4.1; or (c) a data set of the same length but shifted by one year gives an
epoch shifted by a year or more, which indicates the estimator is tracking the
window rather than the transition.

---

## ★8 — An explicit null space of the frozen-flux inversion

Starting point:

$$\frac{\partial B_r}{\partial t} = -\nabla_h\cdot\left(\mathbf{u}B_r\right)
= -B_r\nabla_h\cdot\mathbf{u} - \mathbf{u}\cdot\nabla_h B_r.$$

Choose a horizontal flow that is

1. **divergence-free:** $\nabla_h\cdot\mathbf{u} = 0$, and
2. **along the contours of $B_r$:** $\mathbf{u}\cdot\nabla_h B_r = 0$.

Then both terms vanish and $\partial B_r/\partial t = 0$ **identically**, whatever
$B_r$ is. Such a flow cannot be constrained by any radial SV data.

Construct one explicitly. Let $\psi$ be a stream function with
$\mathbf{u} = \hat{r}\times\nabla_h\psi$, which is automatically divergence-free
on the sphere. Then

$$\mathbf{u}\cdot\nabla_h B_r
= \left(\hat{r}\times\nabla_h\psi\right)\cdot\nabla_h B_r
= \hat{r}\cdot\left(\nabla_h\psi\times\nabla_h B_r\right)
= -\mathcal{J}(\psi, B_r),$$

the horizontal Jacobian. Choosing $\psi = f(B_r)$ for any smooth $f$ makes
$\nabla_h\psi = f'(B_r)\nabla_h B_r$, hence
$\nabla_h\psi\times\nabla_h B_r = 0$ and $\mathcal{J} = 0$. So

$$\mathbf{u} = \hat{r}\times\nabla_h f(B_r)$$

is a one-parameter family (one function $f$) of flows in the exact null space.

**The two assumptions used:** incompressible (divergence-free) horizontal flow,
and no radial diffusion of $B_r$ into the region (frozen flux). Relaxing either
one lifts the degeneracy — which is precisely why upwelling and diffusion
arguments are used in practice to argue for a particular member of the family.
