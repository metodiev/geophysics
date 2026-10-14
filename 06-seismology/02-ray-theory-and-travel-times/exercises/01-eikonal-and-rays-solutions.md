# Solutions — 06-02-01 Eikonal Equation, Rays and Fermat's Principle

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where a problem admits more than one defensible answer it is said so.

Lesson: [01 Eikonal Equation, Rays and Fermat's Principle](../01-eikonal-and-rays.md).

---

## ★1 — A travel-time field and its gradient

$$T(x,z) = \frac{\sqrt{x^{2}+z^{2}}}{v}, \qquad
\nabla T = \frac{(x, z)}{v\sqrt{x^{2}+z^{2}}}, \qquad
|\nabla T| = \frac{1}{v}.$$

At $(4.0, 3.0)$ km: $r = 5.000$ km, so
$T = 5000/3000 = 1.666667$ s.

Unit: $x/v$ is $\mathrm{m}/(\mathrm{m\,s^{-1}}) = \mathrm{s}$, and the gradient
has units $\mathrm{s\,m^{-1}}$ — a slowness, as the eikonal equation requires.

---

## ★2 — The validity group

$$\varepsilon = \frac{1}{f}\left|\frac{\mathrm{d}v}{\mathrm{d}z}\right|
= \frac{0.8}{f}.$$

| $f$ (Hz) | $\varepsilon$ | verdict |
|---|---|---|
| 20 | 0.040 | ray description defensible ($\ll 1$) |
| 5 | 0.160 | marginal: the velocity changes by 16 % within a wavelength |

Note that the group is frequency-dependent only: it does not involve $v$ itself.

---

## ★3 — The closed form at two points

- $T(0,0)$: the argument is $\mathrm{arccosh}(1) = 0$, so $T = 0$ — the source
  condition. It *must* vanish because a travel time from a point to itself is
  zero.
- $T(3000,0)$: $z = 0$, so the argument is
  $1 + g^{2}x^{2}/(2v_0^{2}) = 1 + 0.25(9\times10^{6})/(2\times4\times10^{6})
  = 1.281250$; $\mathrm{arccosh}(1.281250) = 0.733449$; and
  $T = 0.733449/0.50 = 1.466898$ s.

Unit: $\mathrm{s}$.

---

## ★4 — Eikonal and transport

With $\nabla u = (\nabla A + i\omega A\nabla T)e^{i\omega(T-t)}$ and
$\partial_t^{2}u = -\omega^{2}Ae^{i\omega(T-t)}$, substitution gives

$$\omega^{2}A\Big[v^{-2} - |\nabla T|^{2}\Big]
+ i\omega\Big[2\nabla A\cdot\nabla T + A\nabla^{2}T\Big]
+ \nabla^{2}A = 0 .$$

Order $\omega^{2}$ gives the **eikonal equation** $|\nabla T|^{2} = v^{-2}$.
Order $\omega^{1}$ gives the **transport equation**
$2\nabla A\cdot\nabla T + A\nabla^{2}T = 0$, which determines the amplitude (and
with it geometric spreading). The term dropped is the order-$\omega^{0}$ term
$\nabla^{2}A$.

The transport equation is the one that carries amplitude information. It is
exactly the term that becomes singular at a caustic, where the rays focus and
$A$ diverges, while $T$ stays smooth.

---

## ★5 — Measuring the order

| pair | ratio | $p_k = \log_2$(ratio) |
|---|---|---|
| 91.645060 / 53.556648 | 1.711078 | 0.774991 |
| 53.556648 / 30.732574 | 1.742595 | 0.801297 |
| 30.732574 / 17.370528 | 1.769259 | 0.823127 |

Mean: $(0.774991 + 0.801297 + 0.823127)/3 = 0.799805 \approx 0.800$.

The mean reproduces the fitted order printed by the demonstration, and the three
individual estimates tighten as $h$ decreases, which is the expected behaviour of
a measured order: the asymptotic regime is approached, not reached.

---

## ★6 — Which error the theory supplies

Pick noise alone: $r = vt$, so
$\sigma_r = v\sigma_t = 3000 \times 0.005 = 15.0$ m (the demonstration's 4000
realisations give $14.933$ m, consistent with the Monte Carlo).

Velocity error alone: at fixed $t$, $r \propto v$, so
$\delta r = 0.005 \times 8485.281 = 42.43$ m.

Ratio: $42.43/15.0 = 2.8$.

The eikonal solver supplies the *time*. Neither error is produced by the
method: the picking uncertainty comes from the data and the velocity uncertainty
from the model, and both must be propagated by the user.

---

## ★7 — Fermat's principle, and what a broken line cannot do

Parameterise the family by $a$: segment 1 from $(0,0)$ to $(6000a, 1500)$ m,
segment 2 from there to $(6000, 3000)$ m. For a straight segment crossing
$\Delta z$ of depth, $\mathrm{d}s = (\ell/\Delta z)\mathrm{d}z$, so
$\int \mathrm{d}s/v = (\ell/\Delta z)\,(1/g)\ln\!\big[v(z_2)/v(z_1)\big]$ and

$$T(a) = \frac{\ell_1}{1500}\,\frac{1}{0.5}\ln\frac{2750}{2000}
+ \frac{\ell_2}{1500}\,\frac{1}{0.5}\ln\frac{3500}{2750}.$$

Evaluating:

| $a$ | $T(a)$ (s) |
|---|---|
| 0.0 | 2.625581 |
| 0.2 | 2.432685 |
| 0.5 | 2.502678 |
| 1.0 | 3.108361 |
| minimum (numerical, $a = 0.2577$) | **2.425856** |

Three statements follow.

1. The straight chord ($a = 0.5$, $T = 2.502678$ s) is **not** stationary: moving
   the way-point to $a = 0.2577$ reduces the time by 0.076822 s. So the straight
   line is not the ray, and "shortest time" is not "straightest path".
2. The best broken line is **2.425856** s, still 0.035269 s (1.47 %) above the
   closed-form ray time of 2.390587 s. A two-segment path is a restricted family;
   the true ray is a curved arc, and no broken line in this family reproduces it.
   Minimising over a restricted family gives an upper bound on the travel time,
   never the ray itself.
3. Nothing in this calculation proves the ray time is a *minimum* rather than a
   saddle; for this medium it is, but the statement Fermat's principle makes is
   stationarity, and the distinction matters in strongly heterogeneous media.

---

## ★8 — Designing a measurement of ray theory's failure

A specification that can be executed with the tools of this module:

- **Model:** a synthetic stack of constant-velocity layers, one of which has a
  *lower* velocity than the layer above it, with layer thicknesses at least ten
  times the grid spacing so the grid is not the limitation.
- **Prediction A (closed forms):** build the first-arrival curve from the
  analytic branches, with `nan` where a head wave cannot exist (the low-velocity
  interface).
- **Prediction B (grid):** solve the same model with a first-arrival grid
  eikonal solver at two grid spacings.
- **Comparison:** the difference between the two curves as a function of offset,
  reported with units, and the same comparison after halving $h$.
- **Falsification:** the claim "a grid solver loses shallow-angle arrivals" would
  be contradicted if refining $h$ left the grid curve agreeing with the analytic
  branches at all offsets — in particular if the grid reproduced the head-wave
  branch at offsets within a few hundred metres of machine precision at the
  coarsest $h$ tested.

The measurement is executed in Section 7 of the lesson, where the grid misses a
head wave that is 0.129 s earlier than the direct arrival at 60 km offset, and
where the staircase over-estimates the shallow leg by 30.5 %.
