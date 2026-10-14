---
id: 09-02-06
title: "Forward Modelling Resistivity Data"
level: graduate
prereqs: ["09-02-03", "09-02-04"]
tags: [electrical-methods, forward-modelling, image-series, hankel-transform, jacobian, null-space]
---

# Forward Modelling Resistivity Data

An inversion is only as good as the forward model it inverts, and the forward
model must be verified against something independent before it is trusted. This
lesson builds the layered-earth solution from two directions — an exact image
series for two layers and the Stefanescu recurrence for any number — verifies
them against each other to twelve digits, and then uses the derivative of the
model to show, from the model alone, exactly what a sounding cannot resolve.

**All models and data in this module are SYNTHETIC.** The layered models are
chosen teaching values; no field data are used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the two-layer image series from the reflection coefficient and
   state its convergence rate.
2. **Derive** the layered (Stefanescu) recurrence that gives the surface
   potential for an arbitrary stack.
3. **Verify** the two routes against each other and against the half-space
   limit, and **verify** reciprocity.
4. **Construct** the Jacobian of a sounding with respect to log-parameters and
   compute its singular values.
5. **Interpret** the smallest singular vector as a null direction and identify
   it with transverse-resistance equivalence.
6. **Quantify** what a null direction costs: how much the model can move while
   the data move by less than the noise.
7. **State** the accuracy and cost of the Bessel-integral route.

## Prerequisites

- [09-02-03 Apparent Resistivity and Geometric Factors](03-apparent-resistivity.md) —
  sounding curves and the equivalence classes.
- [09-02-04 Vertical Electrical Sounding vs Profiling](04-sounding-profiling.md) —
  what a sounding resolves.

## 1. The two-layer image series

For a layer of resistivity $\rho_1$ and thickness $h$ over a half-space
$\rho_2$, the surface potential of a point source can be written as the
half-space answer plus a series of images:

$$V(r) = \frac{\rho_1 I}{2\pi}\left[\frac{1}{r} +
\sum_{n=1}^{\infty}\frac{k^{n}}{\sqrt{r^{2} + (2nh)^{2}}}\right], \qquad
k = \frac{\rho_2-\rho_1}{\rho_2+\rho_1}.$$

Each term is an image source at depth $2nh$ with amplitude $k^n$; the series is
geometric and converges like $|k|^{n}$. The demo's SYNTHETIC case
$\rho_1 = 100$, $\rho_2 = 500\ \Omega\,\mathrm{m}$, $h = 8$ m gives
$k = 0.666667$ and:

| $r$ (m) | 1 | 4 | 8 | 16 | 40 |
|---|---|---|---|---|---|
| $V$ with 200 images (V) | 1.7006874119 | 0.5049686391 | 0.3003700780 | 0.1862589461 | 0.0955837532 |
| $V$ with 1 image | 1.6577348481 | 0.4622219304 | 0.2582572241 | 0.1463633142 | 0.0644173449 |
| $V$ with 5 images | 1.6971823836 | 0.5014657199 | 0.2968738794 | 0.1827892034 | 0.0922822140 |
| $V$ with 20 images | 1.7006847856 | 0.5049660129 | 0.3003674523 | 0.1862563223 | 0.0955811428 |

At $r = 40$ m the single-image truncation is off by $3.26\times10^{-1}$ relative
and the twenty-image sum by $2.73\times10^{-5}$. A handful of images suffices for
a two-layer earth; a stack of many interfaces does not have a usable image
series, because the number of terms explodes combinatorially.

## 2. The layered recurrence, and the verification

For an arbitrary stack the surface potential is a Hankel transform of a ratio
built from the reflection coefficients. With $\rho_1\dots\rho_N$ the layer
resistivities (the last being the basement) and thicknesses $h_1\dots h_{N-1}$,
define, by recursion from the bottom,

$$R_N(\lambda) = 0, \qquad
R_i(\lambda) = \frac{k_i + R_{i+1}(\lambda)}
{1 + k_iR_{i+1}(\lambda)}\,\mathrm{e}^{-2\lambda h_i}, \qquad
k_i = \frac{\rho_{i+1}-\rho_i}{\rho_{i+1}+\rho_i},$$

and then

$$V(r) = \frac{\rho_1 I}{2\pi}\left[\frac{1}{r} +
\int_0^\infty\left(\frac{1}{1 - R_1(\lambda)} - 1\right)J_0(\lambda r)\,
\mathrm{d}\lambda\right].$$

The subtraction of 1 makes the integrand decay like $\mathrm{e}^{-2h_1\lambda}$,
which is what makes the numerical integral converge; the $1/r$ term carries the
singularity. The demo evaluates this for the same two-layer model and prints the
relative difference against the image series:

| $r$ (m) | 1 | 2 | 4 | 8 | 16 | 40 | 80 |
|---|---|---|---|---|---|---|---|
| relative difference | $1.3\times10^{-16}$ | $6.1\times10^{-16}$ | $1.8\times10^{-15}$ | $3.3\times10^{-15}$ | $5.4\times10^{-15}$ | $8.0\times10^{-15}$ | $8.3\times10^{-11}$ |

Worst case over the range: $8.3\times10^{-11}$, at 80 m where the quadrature
truncation begins to bite. **Two completely different derivations agreeing to
twelve digits is the standard of proof this folder requires before a forward
model is used for inversion.**

## 3. Checks that must pass: half-space limit and reciprocity

Setting $\rho_2 = \rho_1$ gives $k = 0$ and the series must collapse to the
half-space answer. The demo prints, for $\rho = 10$, 100 and
$1000\ \Omega\,\mathrm{m}$ at $r = 5$ m, differences of $0.000\times10^{0}$,
$5.55\times10^{-17}$ and $0.000\times10^{0}$ V.

**Reciprocity** is a property of the conductivity operator: exchanging the
current pair and the potential pair leaves the measurement unchanged. The demo
uses an asymmetric array on a three-layer model
($\rho = (100, 20, 400)\ \Omega\,\mathrm{m}$, $h = (4, 6)$ m, current at 0 and
7 m, potential at 3 and 11 m):

$$\Delta V_{AB\to MN} = 0.349158659075\ \mathrm{V}, \qquad
\Delta V_{MN\to AB} = 0.349158659075\ \mathrm{V},$$

difference $0.000\times10^{0}$ V. A forward model that fails this check is
broken, and the check costs one extra evaluation.

## 4. The Jacobian and its singular values

Parametrise the model logarithmically: $m = (\ln\rho_1, \ln\rho_2, \ln\rho_3,
\ln h_1, \ln h_2)$ and use the data
$d_i = \ln\rho_a(a_i)$ at twelve log-spaced spacings. The normalised sensitivity
$J_{ij} = \partial\ln\rho_a(a_i)/\partial m_j$ for the SYNTHETIC model
$\rho = (100, 500, 20)\ \Omega\,\mathrm{m}$, $h = (5, 4)$ m, is printed in full
by the demo; its first rows show the expected behaviour — the shortest spacing
depends on $\ln\rho_1$ with sensitivity $0.9989$ and on everything else with
sensitivity below $0.006$:

| $a$ (m) | $\partial/\partial\ln\rho_1$ | $\ln\rho_2$ | $\ln\rho_3$ | $\ln h_1$ | $\ln h_2$ |
|---|---|---|---|---|---|
| 1.0 | 0.9989 | 0.0011 | 0.0000 | $-0.0054$ | 0.0006 |
| 4.0 | 0.9535 | 0.0443 | 0.0023 | $-0.1528$ | 0.0285 |
| 12.0 | 0.7133 | 0.2585 | 0.0282 | $-0.1657$ | 0.2302 |
| 48.0 | 0.6273 | 0.2029 | 0.1698 | 0.1566 | 0.2148 |

The singular values of $J$ are

$$2.9229,\quad 0.8891,\quad 0.4088,\quad 0.0930,\quad
\mathbf{0.0021},$$

so the condition number is $1.42\times10^{3}$. The smallest right singular
vector is

$$\hat{v}_{\min} = (+0.0007,\ +0.6899,\ +0.0153,\ +0.0767,\ -0.7196)$$

in the order $(\ln\rho_1, \ln\rho_2, \ln\rho_3, \ln h_1, \ln h_2)$: **a direction
in model space that changes the data by almost nothing.** It is dominated by
$(\ln\rho_2, \ln h_2)$ with opposite signs.

## 5. What the null direction means

Move the model 5% along $\hat{v}_{\min}$ and watch the two candidate invariants:

| quantity | before | after | change |
|---|---|---|---|
| $\rho_2$ | 500.00 | 517.55 $\Omega\,\mathrm{m}$ | $+3.51\%$ |
| $h_2$ | 4.00 | 3.86 m | $-3.53\%$ |
| $T = h_2\rho_2$ | 2000.0 | 1997.0 $\Omega\,\mathrm{m^{2}}$ | $-0.15\%$ |
| $S = h_2/\rho_2$ | 0.008000 | 0.007456 S | $-6.81\%$ |
| max change in $\rho_a$ | — | — | $0.09\%$ |

The transverse resistance $h\rho$ of the thin **resistive** layer is conserved to
0.15% while the thickness changes by 3.5%, and the sounding moves by 0.09% — far
below any realistic noise. This is T-equivalence, *derived* rather than quoted:
it is the null space of the Jacobian, it is why
[09-02-03](03-apparent-resistivity.md)'s equivalence families exist, and it is
why an inversion must report a family or a covariance rather than a thickness.

## 6. Worked example: is the null direction really null?

Test it against a 2% noise level. A model moved along $\hat{v}_{\min}$ by a
fraction $\varepsilon$ changes the sounding by approximately
$\varepsilon\times(\text{max change at } \varepsilon = 0.05)/0.05 = 1.8\%$ per
unit $\varepsilon$ at the 5% point, i.e. the change is proportional to
$\varepsilon$ to first order. Setting the change equal to the 2% noise gives

$$\varepsilon \approx \frac{0.02}{0.018} \approx 1.1,$$

i.e. the null direction can be traversed by *more than 100%* before the data
notice — which is only a formal statement, since at $\varepsilon = 1$ the
linearisation has long since broken down. The practical reading: within the
linear regime there is no bound on the thickness from this data at all, and the
nonlinear behaviour (the 13.988% at $h_2 = 16$ m in
[09-02-03](03-apparent-resistivity.md)) is what eventually limits it. **A
linearised covariance understates the uncertainty of an equivalence direction;
the admitted family must be explored with the nonlinear forward model.**

## 7. Cost and accuracy of the route

The demo measures its own cost: one Wenner $\Delta V$ (two Bessel integrals)
takes $0.28\ \mathrm{ms}$ and about 462 integrand evaluations of $J_0$, with a
quadrature error estimate of $8.4\times10^{-10}$ V on the printed call. That is
fast enough for a full Gauss-Newton inversion with a finite-difference Jacobian
([09-02-07](07-resistivity-inversion.md)) — which is exactly the point of
building the forward model carefully first.

## 8. Regime of validity

1. **Layered (one-dimensional) earth.** Lateral variation needs a numerical
   solver.
2. **The Hankel integral is truncated** at $\lambda_\text{max} = 30/\min(h_i)$;
   the demo's two-layer agreement to $10^{-11}$ at 80 m shows the truncation is
   harmless, but it must be checked per model.
3. **Reciprocity and the half-space limit are exact identities** and are the
   checks that catch coding errors.
4. **The Jacobian is a local, first-order object.** Its null space is a
   *linearised* statement; the nonlinear admitted set must be explored
   separately.
5. **No polarisation, no anisotropy, no three-dimensionality.** Each would
   require a different forward model and would change the null space.

## 9. Mastery checkpoint

1. Derive the image series from the reflection coefficient, and give the
   convergence rate for $k = 1/3$.
2. Verify the half-space limit analytically: show the integrand vanishes when
   all $k_i = 0$.
3. From the sensitivity table, explain why the 1 m spacing contains essentially
   no information about layer 3.
4. Explain in three sentences why a forward model's null space, not the data,
   sets the limit on what an inversion can report.

## 10. Common pitfalls

1. **Inverting with an unverified forward model.** The two-route check of
   Section 2 is the minimum standard.
2. **Truncating the Hankel integral by habit.** The truncation depends on the
   thinnest layer.
3. **Reading singular values as physical uncertainties.** They are normalised
   sensitivities; scale them by the data noise.
4. **Assuming the linearised null space bounds the model.** Section 6 shows the
   linear statement can be meaningless far from the reference model.
5. **Ignoring the $1/r$ term.** The integral alone is not the potential.

## 11. Related modules

- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](07-resistivity-inversion.md).
- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md) —
  where the analytic Fréchet kernel is verified.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../../18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md).
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md).
- [09-02 Resistivity Methods](README.md).

## 12. Demonstration and exercises

- [`code/resistivity_forward_modelling_demo.py`](code/resistivity_forward_modelling_demo.py)
  prints the image-series convergence, the cross-verification, the half-space
  and reciprocity checks, the full Jacobian, its singular values and the null
  direction experiment.
- [Exercises](exercises/06-resistivity-forward-modelling-exercises.md) and
  [worked solutions](exercises/06-resistivity-forward-modelling-solutions.md).
