# Solutions — 18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [01 Taxonomy of Uncertainty](../01-uncertainty-taxonomy.md).

---

## ★1 — The mean-square-error identity

$$
\mathbb{E}\bigl[(y^*_{\text{pred}} - y^*_{\text{true}})^2\bigr]
= \underbrace{b(a)^2}_{\text{structural, from the omitted physics}}
+ \underbrace{a^{\top}C_{\text{post}}a}_{\text{epistemic, from the posterior}}
+ \underbrace{\sigma^2}_{\text{aleatory, from the measurement}} .
$$

The terms add because they are assumed independent; with correlated structural error
and epistemic uncertainty the cross terms do not vanish.

---

## ★2 — Budget at $x^* = 6$ km

$$
\text{RMSE} = \sqrt{0.1800^2 + 0.0840^2 + 0.2000^2}
= \sqrt{0.032400 + 0.007056 + 0.040000} = \sqrt{0.079456} = 0.281884,
$$

against the printed $0.2819$ — agreement to four decimals. Bias share:

$$
\frac{0.032400}{0.079456} = 0.407758 = 40.8\%,
$$

against the printed $40.8\%$.

---

## ★3 — Epistemic standard deviation and the aperture

$$
\sigma_{\text{epi}}(x^*) = x^*\frac{\sigma}{\sqrt{\sum x_i^2}}
= 5\cdot\frac{0.1}{\sqrt{100}} = 0.050000 .
$$

Doubling the aperture while keeping the station count multiplies $\sum x_i^2$ by
about $4$ (for a uniform spacing over twice the range), so

$$
\sigma_{\text{epi}}(5) = 5\cdot\frac{0.1}{\sqrt{400}} = 0.025000,
$$

a factor of $2$ smaller. The epistemic standard deviation scales as the inverse
square root of $\sum x_i^2$; a $4\times$ increase in that sum is needed for a
factor of $2$.

---

## ★★4 — Two designs, same number of extra stations

Original: $x = 1,\dots,8$ gives $\sum x^2 = 1^2+\cdots+8^2 = 204\ \mathrm{km^2}$.

Denser: $x$ at $16$ points uniformly over $1$–$8$ km gives
$\sum x^2 = 398\ \mathrm{km^2}$, so the epistemic variance falls by
$398/204 = 1.951$.

Wider: $x = 1,\dots,16$ gives $\sum x^2 = 16(16+1)(32+1)/6 = 1496\ \mathrm{km^2}$,
so the epistemic variance falls by $1496/204 = 7.333$.

At $x^* = 4$ km the epistemic standard deviation is therefore

$$
4\frac{0.2}{\sqrt{204}} = 0.0560, \qquad
4\frac{0.2}{\sqrt{398}} = 0.0401, \qquad
4\frac{0.2}{\sqrt{1496}} = 0.0207
$$

in data units, matching the printed values. **Choose the wider aperture** when the
quantity of interest lies at the far end or beyond it, because the design also
controls the growth of the epistemic term with $x^*$, and because the structural
term grows as $x^{*2}$ whether or not it is measured. Note the same conclusion
cannot be reached from the station count alone.

---

## ★★5 — The ill-conditioned design

$$
G^{\top}G = \begin{bmatrix}1&1\\1.01&1\end{bmatrix}^{\top}
\begin{bmatrix}1&1\\1.01&1\end{bmatrix}
= \begin{bmatrix}2.0201&2.01\\2.01&2\end{bmatrix},
\qquad
\det(G^{\top}G) = 4.0402 - 4.0401 = 1.0\times10^{-4}.
$$

$$
C_{\text{post}} = 0.0025\,(G^{\top}G)^{-1}
= \begin{bmatrix}50.0&-50.25\\-50.25&50.5025\end{bmatrix}.
$$

Eigenvalues: $\lambda \approx 100.503$ and $6.2\times10^{-4}$, so the standard
deviation along the worst direction is $\sqrt{100.503} = 10.025$, against a data
noise of $\sigma = 0.05$. The epistemic uncertainty exceeds the measurement noise by
a factor of about $200$: the design, not the instrument, is the limitation.

---

## ★★6 — Halving the epistemic standard deviation

Since $\sigma_{\text{epi}} \propto \left(\sum x_i^2\right)^{-1/2}$, halving requires

$$
\sum x_i^2 \to 4\sum x_i^2 .
$$

In a field survey with a fixed array length this means roughly four times as many
stations at the same spacing; if the aperture can be extended, a much smaller number
of extra stations suffices, because the sum grows as the cube of the aperture for a
fixed spacing. Either way the same number of extra stations buys different amounts
depending on where they are placed.

---

## ★★7 — What else could be in $\pm 0.05$ km/s

1. **Epistemic uncertainty**: the posterior width from the inversion, which shrinks
   with more or better-placed data.
2. **Structural uncertainty**: model discrepancy — an isotropic assumption, a
   mis-parameterised layer, a mis-tie to a well, a 1-D approximation to a 3-D
   structure. It does not shrink with more data of the same type.

**Diagnostic.** Repeat the inversion with the same data but a different model
parameterisation (for example anisotropic, or an extra layer). If the reported
velocity moves by a substantial fraction of $0.05$ km/s while the posterior width
stays the same, the number is dominated by the structural term; if it does not move
and the width narrows with more data, the number is epistemic. A pure aleatory
component would appear as a record-to-record scatter that does not respond to
either.

---

## ★★8 — A synthetic study separating the three components

- **Injected truths:** a two-layer model with known velocities and thicknesses, plus
  a known measurement noise $\sigma$.
- **Structural omission:** the inversion assumes a laterally invariant, isotropic,
  horizontal-layer model while the synthetic truth includes a small lateral velocity
  gradient, so a bias exists by construction.
- **Observables:** (i) the inversion's posterior mean against the injected truth over
  many noise realisations (bias = structural); (ii) the posterior standard deviation
  against the spread of the recovered means (epistemic); (iii) the residual scatter
  about the injected travel times (aleatory).
- **Criterion:** the study declares the separation successful when the recovered bias
  is stable across realisations and does not shrink with more data (structural), the
  posterior standard deviation matches the spread of recovered means (epistemic
  correctly quantified), and the residual scatter matches the injected $\sigma$
  (aleatory correctly assigned).

The specification is executable because each component has both a generating
mechanism and a diagnostic that responds to it, and none of the three depends on a
quantity that cannot be computed.
