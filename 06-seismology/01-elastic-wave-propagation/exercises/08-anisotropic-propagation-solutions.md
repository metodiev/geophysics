# Solutions — 06-01-08 Wave Propagation in Anisotropic Media

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [08 Wave Propagation in Anisotropic
Media](../08-anisotropic-propagation.md).

---

## ★1 — The axis stiffnesses

$$C_{33} = \rho\alpha_0^2 = 2600 \times (4000)^2
= 2600 \times 1.6\times10^{7} = 4.16\times10^{10}\ \mathrm{Pa}
= 41.6000\ \mathrm{GPa},$$

$$C_{44} = \rho\beta_0^2 = 2600 \times (2400)^2
= 2600 \times 5.76\times10^{6} = 1.4976\times10^{10}\ \mathrm{Pa}
= 14.9760\ \mathrm{GPa}.$$

**Dimensional check:**
$\mathrm{kg\,m^{-3}} \times \mathrm{m^2\,s^{-2}} =
\mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{Pa}$ ✔. Both are the printed values to four
decimals.

---

## ★2 — The anisotropy parameters enter as factors

$$C_{11} = C_{33}(1+2\varepsilon) = 41.6(1.4) = 58.2400\ \mathrm{GPa},$$
$$C_{66} = C_{44}(1+2\gamma) = 14.976(1.4) = 20.9664\ \mathrm{GPa},$$
$$C_{12} = C_{11} - 2C_{66} = 58.2400 - 41.9328 = 16.3072\ \mathrm{GPa}.$$

An isotropic medium with the same $\alpha_0$ would have $C_{11} = C_{33}$, so the
anisotropy makes $C_{11} - C_{33} = 58.2400 - 41.6000 = 16.6400\ \mathrm{GPa}$
larger, i.e. the medium is stiffer horizontally than vertically by 40% — which is
exactly the statement $\varepsilon = (C_{11}-C_{33})/(2C_{33}) = 0.20$.

---

## ★3 — Christoffel tensor on the symmetry axis

For $\mathbf n = (0,0,1)$, $\Gamma_{ik} = C_{i3k3}$, which in Voigt notation gives
the diagonal

$$\Gamma = \mathrm{diag}(C_{44},\ C_{44},\ C_{33}).$$

The eigenvalues are $\rho v^2 = C_{33}$ (once) and $C_{44}$ (twice), so

$$v_{qP} = \sqrt{C_{33}/\rho} = \alpha_0 = 4000\ \mathrm{m\,s^{-1}},\qquad
v_{qS} = \sqrt{C_{44}/\rho} = \beta_0 = 2400\ \mathrm{m\,s^{-1}} .$$

The **S branch is doubly degenerate** on the axis, and the demonstration confirms
it: `measured qP along z = 4000.0000, qSH/qSV along z = 2400.0000, 2400.0000`.

---

## ★4 — $C_{13}$ and the round trip

With $C_{33} = 4.16\times10^{10}$, $C_{44} = 1.4976\times10^{10}\ \mathrm{Pa}$,
$C_{33}-C_{44} = 2.6624\times10^{10}\ \mathrm{Pa}$:

$$2C_{33}(C_{33}-C_{44})\delta
= 2(4.16\times10^{10})(2.6624\times10^{10})(0.15)
= 3.3226752\times10^{20},$$

$$(C_{33}-C_{44})^2 = (2.6624\times10^{10})^2 = 7.08837376\times10^{20},$$

$$\text{sum} = 1.041104896\times10^{21}
\;\Longrightarrow\; \sqrt{\text{sum}} = 3.2266157\times10^{10}\ \mathrm{Pa},$$

$$C_{13} = 3.2266157\times10^{10} - 1.4976\times10^{10}
= 1.7290157\times10^{10}\ \mathrm{Pa} = 17.2902\ \mathrm{GPa},$$

which is the printed value. Feeding the result back:

$$\delta = \frac{(C_{13}+C_{44})^2 - (C_{33}-C_{44})^2}{2C_{33}(C_{33}-C_{44})}
= 0.1500000000,$$

matching the input — the demonstration prints exactly this round trip, so the
tensor and the parameter set are the same object written two ways.

---

## ★5 — The exact SH speed

$$v_{SH}(\theta) = \beta_0\sqrt{1+2\gamma\sin^2\theta} .$$

| $\theta$ | $\sin^2\theta$ | $v_{SH}$ (m/s) | demonstration |
|---|---|---|---|
| $0^\circ$ | 0 | $2400\sqrt{1} = 2400.0000$ | 2400.0000 |
| $45^\circ$ | 0.5 | $2400\sqrt{1.2} = 2629.0683$ | 2629.0683 |
| $90^\circ$ | 1 | $2400\sqrt{1.4} = 2839.7183$ | 2839.7183 |

All three agree. Note the shape: the speed grows *monotonically* with angle and
saturates at the horizontal value — no maximum at intermediate angle, unlike qSV.

---

## ★6 — Thomsen approximations at $45^\circ$

At $\theta = 45^\circ$: $\sin^2\theta\cos^2\theta = 0.25$,
$\sin^4\theta = 0.25$.

$$v_{qP} \approx \alpha_0\left(1 + \delta(0.25) + \varepsilon(0.25)\right)
= 4000\left(1 + 0.0375 + 0.05\right) = 4000(1.0875) = 4350.0000,$$

$$v_{qSV} \approx \beta_0\left(1 + \frac{\alpha_0^2}{\beta_0^2}
(\varepsilon-\delta)(0.25)\right)
= 2400\left(1 + 2.777778 \times 0.05 \times 0.25\right)
= 2400(1.034722) = 2483.3333 .$$

Errors, expressed both ways:

$$v_{qP}: \frac{4350.0000 - 4346.0321}{4346.0321} = 0.0913\%
\quad\text{relative to exact},\qquad
\left\lvert\frac{4346.0321}{4350.0000} - 1\right\rvert = 0.0912\%,$$

$$v_{qSV}: \frac{2483.3333 - 2464.1439}{2464.1439} = 0.7787\%
\quad\text{relative to exact},\qquad
\left\lvert\frac{2464.1439}{2483.3333} - 1\right\rvert = 0.7728\%.$$

The demonstration prints $0.0912$ and $0.7727$, i.e. it normalises by the
**approximate** value; the two conventions differ by about 0.006 percentage points
at this anisotropy and the convention should always be stated with the number.

The qP approximation is **much better** at $45^\circ$ — by a factor of about 8 —
because the qSV expansion carries the factor
$(\alpha_0/\beta_0)^2 = 2.7778$ that amplifies the same small parameter
$(\varepsilon-\delta)$.

---

## ★★★7 — The group-velocity relation (worked derivation)

Let the phase speed depend only on the angle $\theta$ from the axis, so
$\omega = v(\theta)k$ with $k = \lvert\mathbf k\rvert$ and
$\mathbf k = k(\sin\theta, 0, \cos\theta)$ (in the $x$–$z$ plane). Write
$\hat{\mathbf n} = \mathbf k/k$ and let
$\hat{\boldsymbol\theta} = (\cos\theta, 0, -\sin\theta)$ be the unit vector
increasing $\theta$.

Along the ray of constant $\theta_r$, $\mathrm{d}\omega = k\,\mathrm{d}v +
v\,\mathrm{d}k$. The phase speed is a function of $\theta$ alone, so
$\mathrm{d}v = (\mathrm{d}v/\mathrm{d}\theta)\,\mathrm{d}\theta$, and differentiating
$\theta = \arctan(k_x/k_z)$ relates $\mathrm{d}\theta$ to the components of
$\mathrm{d}\mathbf k$. Carrying that through gives the standard result

$$\mathbf v_g = \frac{\partial\omega}{\partial\mathbf k}
= v\,\hat{\mathbf n} + \frac{\mathrm{d}v}{\mathrm{d}\theta}\,
\hat{\boldsymbol\theta},$$

which is what the lesson quotes. Its magnitude is
$\lvert\mathbf v_g\rvert = \sqrt{v^2 + (\mathrm{d}v/\mathrm{d}\theta)^2}$ and its
direction deviates from $\hat{\mathbf n}$ by

$$\Delta = \arctan\!\left(\frac{1}{v}\frac{\mathrm{d}v}{\mathrm{d}\theta}\right).$$

**On the axis and perpendicular to it** the phase speed is stationary with respect
to $\theta$ (both are symmetry directions), so
$\mathrm{d}v/\mathrm{d}\theta = 0$ and $\Delta = 0$. Away from the symmetry
directions $\Delta \ne 0$. This is exactly the pattern the demonstration measures:
the ray–phase angle is $0$ at $\theta = 0$ and $90^\circ$ and reaches
$9.845299^\circ$ near $\theta = 45^\circ$, where $\mathrm{d}v/\mathrm{d}\theta$ is
a maximum.

---

## ★★★8 — Minimum directions to constrain $\gamma$ and the axis (design)

**Model.** A transversely isotropic medium with an unknown symmetry-axis
direction; the observable is the S-wave splitting from a ray of known azimuth and
known incidence. Splitting depends on the angle $\phi$ between the ray and the
symmetry axis.

**Why one direction is not enough.** Along the axis the splitting is exactly zero
whatever $\gamma$ is, so a single measurement that happens to be axial yields no
constraint at all; and one off-axis measurement constrains the product
$\gamma\sin^2\phi$-like combination, leaving $\gamma$ and $\phi$ degenerate.

**Minimum design.** Use at least **three** distinct ray directions with
non-coplanar geometry:

1. **Two near-vertical directions along different azimuths.** Their difference in
   splitting identifies the azimuth of the symmetry axis (an HTI medium splits
   most for rays perpendicular to the cracks and not at all along them).
2. **One oblique direction.** Its splitting, crossing axis and perpendicular,
   measures the angular dependence and hence $\gamma$, once the axis is known.

**What each adds.** The azimuth pair breaks the axis-orientation degeneracy but is
blind to $\gamma$ if both rays are far off-axis; the oblique ray supplies the
$\gamma$-sensitive angle dependence. With fewer than three directions one of the
two unknowns (orientation, strength) remains unconstrained, and the honest
statement of a two-measurement result is a trade-off curve, not a value.

---

## ★★★9 — Angular behaviour of the two truncation errors

Both approximations truncate the same expansion, but at different orders and with
different angular weights.

- **qP.** The leading omitted term involves the product of $\delta$ and
  $\varepsilon$ weighted by $\sin^2\theta\cos^2\theta$ and $\sin^4\theta$. These
  weights are *maximal* near $\theta = 45^\circ$–$75^\circ$ but the omitted term
  itself contains a factor $(\varepsilon^2, \varepsilon\delta, \delta^2)$, so the
  error stays small near the axis where the angular weights vanish and grows
  monotonically toward $75^\circ$ — the measured $0.0044\% \to 1.1265\%$.
- **qSV.** The first-order correction already carries
  $(\alpha_0/\beta_0)^2(\varepsilon-\delta)\sin^2\theta\cos^2\theta$, and the
  omitted term is second order in the same combination. The angular factor
  $\sin^2\theta\cos^2\theta$ peaks at $45^\circ$ and vanishes at both axes, which
  is exactly the measured shape: $0.3179\%$ at $30^\circ$, a maximum $0.8014\%$ at
  $60^\circ$, and back to $0.3163\%$ at $75^\circ$.

**Implication for a fit band.** Inverting for $\varepsilon$ and $\delta$ from
qP travel times should use mid-angles ($\sim40^\circ$–$60^\circ$), where the
parameters have their strongest signature *and* the approximation error is still
below a per cent; a fit dominated by near-axial rays has almost no sensitivity
(the angular weights vanish), and a fit dominated by $70^\circ+$ rays pays a
systematic error of order $1\%$ at $\varepsilon = 0.20$. For qSV, by contrast, the
mid-angle band is exactly where its approximation error is largest, so qSV is best
used as a *relative* measurement between directions rather than as an absolute
speed, or computed exactly as the demonstration does.
