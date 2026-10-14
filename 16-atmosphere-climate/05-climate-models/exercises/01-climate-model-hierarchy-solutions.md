# Solutions — 16-05-01 Model Hierarchy: EBMs, EMICs, GCMs, ESMs

> Read after attempting the exercises. Numbers were computed, not estimated by
> hand. Lesson: [01 Model Hierarchy](../01-climate-model-hierarchy.md).

---

## ★1 — Effective radiating temperature

$$F_{\text{abs}} = \frac{S(1-\alpha)}{4} = \frac{1361 \times 0.70}{4}
= \frac{952.7}{4} = 238.175\ \mathrm{W\,m^{-2}}.$$

Units: $S$ is $\mathrm{W\,m^{-2}}$, the factors $1-\alpha$ and $4$ are pure
numbers, so $F_{\text{abs}}$ is $\mathrm{W\,m^{-2}}$.

$$T_{\text{eff}} = \left(\frac{238.175}{5.670374419\times10^{-8}}\right)^{1/4}
= \left(4.2004\times10^{9}\right)^{1/4} = 254.58\ \mathrm{K}.$$

Units: $(\mathrm{W\,m^{-2}})/(\mathrm{W\,m^{-2}\,K^{-4}}) = \mathrm{K^{4}}$, and
the fourth root gives K. The demonstration prints the same value.

---

## ★2 — Equilibrium temperature

$$T_{0} = \frac{F_{\text{abs}}-A}{B} = \frac{238.175-210}{2.0}
= \frac{28.175}{2.0} = 14.09\ \mathrm{{}^{\circ}C} = 287.24\ \mathrm{K}.$$

Implied greenhouse warming:

$$T_{0}-T_{\text{eff}} = 287.24 - 254.58 = 32.66\ \mathrm{K}.$$

This is a property of the *closure* $A = 210\ \mathrm{W\,m^{-2}}$, not a
measurement of a real atmosphere.

---

## ★3 — Relaxation time and the 90% time

$$\tau = \frac{C}{B} = \frac{5.0}{2.0} = 2.50\ \mathrm{yr}.$$

The response to a step is $T(t) = T_{0} + (T(0)-T_{0})e^{-t/\tau}$, so
$90\%$ of the change is reached when $e^{-t/\tau} = 0.10$:

$$t_{90} = \tau\ln 10 = 2.50 \times 2.3026 = 5.76\ \mathrm{yr}.$$

Units: $C/B = \mathrm{W\,yr\,m^{-2}\,K^{-1}} / \mathrm{W\,m^{-2}\,K^{-1}} =
\mathrm{yr}$; $\ln 10$ is dimensionless.

---

## ★4 — Sensitivity to the closure coefficient $B$

| $B$ (W m⁻² K⁻¹) | $T_0$ (°C) | $\Delta T = F/B$ (K) | $\tau = C/B$ (yr) |
|---|---|---|---|
| 1.5 | $(238.175-210)/1.5 = 18.78$ | $3.7/1.5 = 2.47$ | $5.0/1.5 = 3.33$ |
| 2.0 | 14.09 | 1.85 | 2.50 |
| 2.5 | $(238.175-210)/2.5 = 11.27$ | $3.7/2.5 = 1.48$ | $5.0/2.5 = 2.00$ |

The table shows that the equilibrium state, the sensitivity and the response time
all move together when one closure coefficient changes by $\pm25\%$: the warming
varies by $-20\%$ to $+34\%$. A model's output is conditional on its closures,
and the conditionality is not a small correction.

---

## ★5 — Conservation of the global mean

The 1-D steady state satisfies, with $\alpha$ uniform (so absorbed flux
$= Q_{0}S(x)(1-\alpha)$ independent of $T$),

$$0 = D\,\frac{\mathrm d}{\mathrm dx}\left[(1-x^{2})\frac{\mathrm dT}{\mathrm dx}\right]
+ Q_{0}S(x)(1-\alpha) - A - BT.$$

Average over area, i.e. integrate $\mathrm dx$ over $[-1,1]$ and divide by
$\int_{-1}^{1}\mathrm dx = 2$ (the area element in $x=\sin\varphi$ is
$\mathrm dx$, with total 2):

$$\frac{D}{2}\left[(1-x^{2})\frac{\mathrm dT}{\mathrm dx}\right]_{-1}^{+1}
+ \frac{Q_{0}(1-\alpha)}{2}\int_{-1}^{1}S(x)\,\mathrm dx - A - B\bar T = 0.$$

The boundary term is **zero because $(1-x^{2})=0$ at $x=\pm1$**: the poles carry
no area, so the heat flux through them is zero. With $S$ normalised to unit
mean, $\int_{-1}^{1}S\,\mathrm dx = 2$ and

$$Q_{0}(1-\alpha) - A - B\bar T = 0
\qquad\Longrightarrow\qquad
\bar T = \frac{Q_{0}(1-\alpha)-A}{B} = T_{0}.$$

The demonstration confirms this numerically: $14.088\ \mathrm{{}^{\circ}C}$ (1-D)
against $14.087\ \mathrm{{}^{\circ}C}$ (0-D), a difference of
$+0.0000\ \mathrm{K}$ after the discrete insolation shape is renormalised to unit
mean.

---

## ★6 — Why the measured cooling is smaller than the estimate

First-order estimate. The albedo of $11.0\%$ of the area rises by
$0.62-0.30 = 0.32$. Using a globally averaged absorbed flux,

$$\Delta F \approx -Q_{0}\,\Delta\alpha\,f_{\text{ice}}
= -340.25 \times 0.32 \times 0.11 = -11.98\ \mathrm{W\,m^{-2}},$$

$$\Delta T \approx \frac{\Delta F}{B} = \frac{-11.98}{2.0}
= -5.99\ \mathrm{K}.$$

The measured value is $-2.84\ \mathrm{K}$, about $47\%$ of the estimate. The
reason is spatial: the ice appears at high latitudes, where the *local*
insolation shape $S(x)$ is well below its mean, so the flux change at those
points is much smaller than $Q_{0}\Delta\alpha$. A globally averaged estimate
implicitly assumes the albedo change occurs where the mean insolation applies,
which is false exactly where the ice is. This is a concrete example of why a
global-mean budget cannot be used to infer regional effects.

---

## ★7 — Experiment design (specification)

**Runs.** A $2\times2$ design: {no diffusion ($D=0$), diffusion ($D=0.6\
\mathrm{W\,m^{-2}\,K^{-1}}$)} $\times$ {no ice feedback, ice feedback}. Four runs,
each integrated to steady state by the same criterion (maximum change per step
$<10^{-9}$).

**Diagnostic.** The pole-to-equator contrast, $T(x=0)-T(x=\pm1)$, reported with
the global mean as a check that the transport is conservative.

**Interpretation.** The difference between the two no-ice runs isolates the
diffusion closure's contribution to the contrast. The difference between the two
ice runs isolates the feedback's contribution *in the presence of* diffusion.
The interaction term is the difference of differences; if it is large, the two
effects are not separable in this design.

**Confounding not removed.** The ice threshold and the albedo pair are fixed, so
the measured feedback strength is conditional on them. Changing either changes
the interaction term. A full separation would require varying them, which turns
the design into a sensitivity study with its own closure choices.

---

## ★8 — Critique of a tuning-then-predicting plan

**What has been calibrated.** $D$ has been adjusted so that one diagnostic (the
pole-to-equator contrast) matches an observation. That is a one-parameter fit to
one number.

**What has been assumed.** (i) That $D$ is the only unknown affecting the
contrast — but the ice-albedo threshold and the insolation shape also control it,
so $D$ absorbs their errors. (ii) That the fitted $D$ is valid for the changed
forcing used in the prediction; a diffusion closure fitted to today's
circulation need not hold when the circulation changes. (iii) That $A$ has a
known response to a doubling, which is itself the closure being changed — the
model cannot supply the change in $A$ it is asked to respond to.

**What would make the prediction defensible.** Independent evidence on at least
one of the other parameters (for example, an observation of the transport
coefficient from eddy fluxes, or a constraint on the ice threshold), plus a
demonstration that the diagnostic is insensitive to the parameters left free.
Failing that, the correct output is not a number but the range of $\Delta T$
produced by the admissible set of $D$ values — and the statement that the
prediction is conditional on a closure.
