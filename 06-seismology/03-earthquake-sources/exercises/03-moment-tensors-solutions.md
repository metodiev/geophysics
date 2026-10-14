# Solutions — 06-03-03 Moment Tensors, Decomposition and Physical Meaning

> **Read after attempting the exercises.** All tensors are SYNTHETIC. Arithmetic
> is shown so each number can be checked; logarithms are quoted to five decimals.

Lesson: [03 Moment Tensors, Decomposition and Physical Meaning](../03-moment-tensors.md).

Conventions: $M_{\text{iso}} = \mathrm{tr}(M)/3$;
$\lambda_1\ge\lambda_2\ge\lambda_3$ on the deviatoric part with
$\sum\lambda_i = 0$; $M_0 = (\lambda_1-\lambda_3)/2$;
$\varepsilon = -\lambda_2/\max(|\lambda_1|,|\lambda_3|)$;
$M_{\mathrm w} = \tfrac23\log_{10}M_0[\mathrm{N\,m}] - 6.033333$.

---

## ★1 — Invariants of $\mathrm{diag}(4,-1,-3)\times10^{19}$

$$\mathrm{tr}(M) = (4-1-3)\times10^{19} = 0
\;\Rightarrow\; M_{\text{iso}} = 0, \qquad M' = M.$$

Eigenvalues (already diagonal): $\lambda = (4,-1,-3)\times10^{19}$.

$$M_0 = \tfrac12\left(4-(-3)\right)\times10^{19}
= \tfrac12(7)\times10^{19} = 3.5\times10^{19}\ \mathrm{N\,m},$$
$$\varepsilon = -\frac{\lambda_2}{\max(|\lambda_1|,|\lambda_3|)}
= -\frac{-1}{\max(4,3)} = +\frac14 = +0.25.$$

---

## ★2 — Explicit parts

$$M^{\text{dc}} = M_0\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix}
= \begin{pmatrix}3.5&0&0\\0&0&0\\0&0&-3.5\end{pmatrix}\times10^{19},$$

$$M^{\text{clvd}} = \lambda_2\begin{pmatrix}-\tfrac12&0&0\\0&1&0\\0&0&-\tfrac12\end{pmatrix}
= \begin{pmatrix}0.5&0&0\\0&-1&0\\0&0&0.5\end{pmatrix}\times10^{19}.$$

Sum (all in $10^{19}\ \mathrm{N\,m}$):

$$\begin{pmatrix}3.5+0.5&0&0\\0&0-1&0\\0&0&-3.5+0.5\end{pmatrix}
= \begin{pmatrix}4&0&0\\0&-1&0\\0&0&-3\end{pmatrix} = M. ☑$$

---

## ★3 — Magnitude two ways for $M_0 = 3.5\times10^{19}$

$$\log_{10}(3.5\times10^{19}) = 19.54407,$$
$$M_{\mathrm w}^{\text{exact}} = \tfrac23(19.54407) - 6.033333
= 13.02938 - 6.033333 = 6.99605 \approx 6.9960,$$
$$M_{\mathrm w}^{\text{quoted}} = 13.02938 - 6.07 = 6.95938 \approx 6.9594.$$

Difference: $6.99605 - 6.95938 = 0.03667$ magnitude units, the constant gap
between the two offsets. Factor in $M_0$:

$$10^{1.5\times0.03667} = 10^{0.05500} = 1.1350.$$

So the two conventions describe moments differing by $13.5\%$ — well above the
precision of most moment estimates, which is why the offset must be stated.

---

## ★4 — Isotropic plus a strike-slip double couple

$$M = 2.0\times10^{19}\,\mathrm{I}
+ \mathrm{diag}(5,0,-5)\times10^{19}
= \mathrm{diag}(7,2,-3)\times10^{19}\ \mathrm{N\,m}.$$

$$\mathrm{tr}(M) = (7+2-3)\times10^{19} = 6.0\times10^{19}
\;\Rightarrow\; M_{\text{iso}} = 2.0\times10^{19},$$
$$M' = \mathrm{diag}(5,0,-5)\times10^{19},$$
$$M_0 = \tfrac12(5-(-5))\times10^{19} = 5.0\times10^{19}\ \mathrm{N\,m},
\qquad \varepsilon = 0 \quad(\lambda_2 = 0).$$

$$\frac{M_{\text{iso}}}{\max|M_{ij}|} = \frac{2.0\times10^{19}}{7.0\times10^{19}}
= 0.285714.$$

**Comparison with the demo.** The demo's "isotropic + DC" row gives $0.336744$ for
a *different* geometry (dip $40^\circ$, rake $90^\circ$, $M_0^{\text{dc}} =
2.0\times10^{19}$) combined with the same isotropic scalar $10^{19}$. The ratio
depends on both the isotropic scalar and the largest component, and the largest
component depends on the mechanism's orientation. Same structure, different
number — the ratio is a derived diagnostic, not an invariant of the source.

---

## ★5 — Orthogonality and Pythagoras

$$\langle M_{\text{iso}}, M'\rangle
= \sum_{ij}\left(\frac{\mathrm{tr}M}{3}\delta_{ij}\right)M'_{ij}
= \frac{\mathrm{tr}M}{3}\sum_{i}M'_{ii}
= \frac{\mathrm{tr}M}{3}\,\mathrm{tr}(M') = 0,$$

because $\mathrm{tr}(M') = \mathrm{tr}(M) - \mathrm{tr}\!\left(\tfrac{\mathrm{tr}M}{3}I\right)
= \mathrm{tr}M - \mathrm{tr}M = 0$.

Then, since $M$ is symmetric ($M:M' = M':M$),

$$\lVert M\rVert^2 = \langle M_{\text{iso}}+M',\,M_{\text{iso}}+M'\rangle
= \lVert M_{\text{iso}}\rVert^2 + \lVert M'\rVert^2 + 2\langle M_{\text{iso}},M'\rangle
= \lVert M_{\text{iso}}\rVert^2 + \lVert M'\rVert^2. ☑$$

This is the Pythagorean residual the demo checks; its measured value
$-3.56\times10^{-16}$ is round-off.

---

## ★6 — Eigenvalues of a double couple

With $M = M_0(\hat n\hat s^{\mathsf T} + \hat s\hat n^{\mathsf T})$ and
$\hat n\perp\hat s$, $\lVert\hat n\rVert = \lVert\hat s\rVert = 1$, compute the
action on three orthogonal vectors:

$$M\hat n = M_0\left(\hat n(\hat s\cdot\hat n) + \hat s(\hat n\cdot\hat n)\right)
= M_0\hat s, \qquad
M\hat s = M_0\hat n, \qquad
M(\hat n\times\hat s) = 0.$$

- $(\hat n+\hat s)/\sqrt2$: $M(\hat n+\hat s)/\sqrt2
  = M_0(\hat s+\hat n)/\sqrt2$ — eigenvector, eigenvalue $+M_0$.
- $(\hat n-\hat s)/\sqrt2$: $M(\hat n-\hat s)/\sqrt2
  = M_0(\hat s-\hat n)/\sqrt2 = -M_0(\hat n-\hat s)/\sqrt2$ — eigenvalue $-M_0$.
- $\hat n\times\hat s$ — eigenvalue $0$.

So $\lambda = (+M_0,0,-M_0)$, hence $(\lambda_1-\lambda_3)/2 = M_0$ ✔ and
$\varepsilon = -0/M_0 = 0$ ✔. The trace is $0$, confirming no volume change.

---

## ★7 — Why the two "trace" numbers differ

The spacing of IEEE-754 double-precision numbers near $x$ is
$\mathrm{ulp}(x) = 2^{\lfloor\log_2 x\rfloor - 52}$. With
$x = 3.4\times10^{18}$:

$$\log_2(3.4\times10^{18}) = 61.56 \;\Rightarrow\; \lfloor\cdot\rfloor = 61
\;\Rightarrow\; \mathrm{ulp} = 2^{61-52} = 2^{9} = 512\ \mathrm{N\,m}.$$

Relative size: $512/(3.4\times10^{18}) = 1.51\times10^{-16}$ — the double-precision
floor, as expected.

The source is *built* to be traceless, so the algebraic trace is exactly zero.
Both printed values ($+256$ and $-512\ \mathrm{N\,m}$) are *below one ulp* of
$3.4\times10^{18}$, so both are round-off:

- $\mathrm{tr}(M) = M_{xx}+M_{yy}+M_{zz}$ sums three numbers of order $10^{18}$
  whose exact sum is zero; the result is a rounding residue of order half an ulp.
- $\sum\lambda_i$ sums the eigenvalues in descending order; the first partial sum
  $+3.4\times10^{18} - 4.824\times10^{2}$ rounds to a multiple of $512$, and adding
  $-3.4\times10^{18}$ then leaves $-512$, not $+256$.

Two different summation orders, two different round-off residues. Neither is a
property of the source; the physically meaningful statement is
$\mathrm{tr}(M) = 0$ to within $1.5\times10^{-16}$ relative.

---

## ★8 — Causes of a large $\varepsilon$, ordered for a shallow, fluid-affected event

From **most** to **least** plausible for this setting, and the test for each:

1. **A genuine volume/tensile component from fluid.** Injection opens or
   pressurises fractures, radiating a source with a real isotropic-plus-CLVD
   part. *Test:* relocalise the event and compare $\varepsilon$ with the
   injection history and with $\varepsilon$ of nearby tectonic events; a
   monotone relation with pore pressure supports this.
2. **Velocity-model error (1-D model for a 3-D structure).** Mislocated
   take-off angles map into spurious non-double-couple radiation. *Test:* invert
   the same data with a site-specific 3-D or calibrated local model and check
   whether $\hat\varepsilon$ moves towards zero.
3. **Poor focal-sphere coverage at shallow depth.** Few stations at the right
   range of take-off angles leave the CLVD poorly constrained. *Test:* bootstrap
   the inversion over station subsets and report the spread of $\hat\varepsilon$;
   a wide spread means the value is geometry-limited.
4. **Anisotropy or heterogeneity near the source.** Intrinsic anisotropy
   radiates a pattern an isotropic double couple cannot fit. *Test:* compare
   source-mechanism scatter across azimuths with the shear-wave splitting
   directions at nearby stations.

---

## ★9 — Bias in $\varepsilon$ from using a 1-D model (specification)

**Forward model.** A 3-D model built by perturbing a 1-D background with a
Gaussian velocity anomaly of fractional amplitude $a$ centred at the source
depth, horizontal correlation length $2\ \mathrm{km}$, $a\in\{0,1,5,10,20\}\%$.
Generate synthetic three-component waveforms for a known double couple
($\varepsilon = 0$) at $1000$ event positions drawn uniformly in a
$2\times2\ \mathrm{km}$ box.

**Inversion.** A moment-tensor inversion using the **unperturbed 1-D** background,
with the standard linearised least squares and a fixed noise level of $5\%$ on
each component. Add Gaussian noise per realisation.

**Metric.** For each $a$: the mean bias
$\langle\hat\varepsilon\rangle$ over realisations, the spread
$\mathrm{std}(\hat\varepsilon)$, and the ratio
$|\langle\hat\varepsilon\rangle|/\mathrm{std}(\hat\varepsilon)$.

**Prediction.** The noise-only spread at $a = 0$ is the baseline; the bias should
grow roughly linearly with $a$ and should exceed the baseline spread at
$a \approx 5\%$ for this geometry, i.e. the prediction to test is
$a^\ast \approx 5\%$. Because the true source has $\varepsilon = 0$, any
systematic nonzero $\langle\hat\varepsilon\rangle$ is *entirely* a model artefact
— which is exactly why this experiment is worth doing rather than arguing about.

---

## ★10 — Magnitude resolution

$$M_{\mathrm w} = \tfrac23\log_{10}M_0 + C
\;\Rightarrow\;
\Delta M_{\mathrm w} = \tfrac23\,\Delta\log_{10}M_0
\;\Rightarrow\;
\frac{M_0'}{M_0} = 10^{\Delta\log_{10}M_0} = 10^{1.5\,\Delta M_{\mathrm w}}.$$

**Significant figures.** Quoting $M_{\mathrm w}$ to two decimal places implies a
resolution $\Delta M_{\mathrm w} = 0.005$, hence a moment resolution

$$10^{1.5\times0.005} = 10^{0.0075} = 1.0174,$$

i.e. about $1.7\%$ in $M_0$ — roughly **two significant figures** of moment. For
$M_0 = 3.5\times10^{19}\ \mathrm{N\,m}$ this means the third digit is not
meaningful: $3.5\times10^{19}$ is honest, $3.54\times10^{19}$ is not.

**Implication.** $M_{\mathrm w}$ is a logarithmic *reporting* device that compresses
an uncertain moment into a compact number. Because the map is logarithmic, small
differences in $M_{\mathrm w}$ correspond to large differences in $M_0$: two
events that differ by $0.2$ magnitude units differ by a factor
$10^{0.3} = 2.0$ in moment. Reporting $M_0$ to many digits therefore over-states
the precision of the underlying measurement, which is limited by the velocity
model, the attenuation correction and the bandwidth, not by the arithmetic.
