# Solutions — 09-02-06 Forward Modelling Resistivity Data

> **Read after attempting the exercises.** Lesson:
> [06 Forward Modelling Resistivity Data](../06-resistivity-forward-modelling.md).
> Arithmetic below was checked by hand and, where the demonstration covers the
> same model, against its printed values.

---

## ★1 — Reflection coefficient

$$k = \frac{\rho_2-\rho_1}{\rho_2+\rho_1} = \frac{400-80}{400+80}
= \frac{320}{480} = 0.666667.$$

---

## ★2 — Three image terms

$$V(r) = \frac{\rho_1 I}{2\pi}\left[\frac{1}{r}
+\frac{k}{\sqrt{r^{2}+(2h)^{2}}}
+\frac{k^{2}}{\sqrt{r^{2}+(4h)^{2}}}
+\cdots\right],$$

with $2h = 10$ m, $4h = 20$ m, $k = 0.666667$, $k^{2} = 0.444444$ and
$\rho_1 I/2\pi = 80\times0.1/6.28319 = 1.27324$:

| term | value |
|---|---|
| $1/r$ | $0.100000$ |
| $k/\sqrt{100+100}$ | $0.666667/14.1421 = 0.047140$ |
| $k^{2}/\sqrt{100+400}$ | $0.444444/22.3607 = 0.019876$ |

Sum: $0.167016$, so $V \approx 1.27324\times0.167016 = 0.212647\ \mathrm{V}$.

The next term ($k^{3} = 0.296296$, $6h = 30$ m) contributes
$0.296296/31.6228 = 0.009369$, about 5.6% of the three-term sum: the
geometric convergence is visible and slow enough that at this $r$ about ten
terms are needed for 1%.

---

## ★3 — The recurrence

$R_N = 0$ is the statement that the **basement has no interface below it**: the
reflection coefficient of the last interface is the last computed one, and there
is nothing to reflect from deeper. The recursion must run from the bottom because
each layer's ratio $R_i$ depends on the ratio of everything below it — the total
reflection response of the lower half-space as seen from layer $i$. Computing it
upward from the surface is impossible without knowing the downward answer first.

---

## ★4 — Half-space limit

If all $\rho$ are equal, every $k_i = 0$, so $R_N = 0$ and, by the recurrence,
$R_{N-1} = \cdots = R_1 = 0$. Then

$$\frac{1}{1-R_1} - 1 = \frac{1}{1} - 1 = 0,$$

the integrand vanishes identically, and

$$V(r) = \frac{\rho I}{2\pi}\cdot\frac{1}{r},$$

the half-space potential. The demonstration prints this check for
$\rho = 10, 100, 1000\ \Omega\,\mathrm{m}$ with differences of $0$,
$5.55\times10^{-17}$ and $0$ V.

---

## ★5 — Coverage by spacing

- At $a = 1$ m the sensitivities to $\ln\rho_2$, $\ln\rho_3$, $\ln h_2$ are
  $0.0011$, $0.0000$ and $0.0006$: below 0.5% — the array is effectively a
  two-electrode measurement of the top layer. Information about anything below
  the second layer is essentially absent until $a \gtrsim h_1$.
- At $a = 48$ m the sensitivity to $\ln\rho_1$ is still $0.6273$: the long
  spacing has not escaped the top layer, because a 5 m first layer is a small
  fraction of the 48 m aperture but the current must still pass through it. The
  large-spacing data are therefore **not** "deep data" in the simple sense; they
  are data in which the top layer still carries most of the sensitivity.

This is the quantitative version of the lesson's remark that the sounding
"measures a conductance or a resistance, not a thickness".

---

## ★6 — Conservation of $h_2\rho_2$

First-order change: $\mathrm{d}\ln(h_2\rho_2) = \mathrm{d}\ln h_2 +
\mathrm{d}\ln\rho_2$. Moving by $\varepsilon$ along $\hat{v}$ gives
$\mathrm{d}\ln\rho_2 = 0.6899\varepsilon$ and
$\mathrm{d}\ln h_2 = -0.7196\varepsilon$, so

$$\mathrm{d}\ln(h_2\rho_2) = (0.6899-0.7196)\varepsilon
= -0.0297\,\varepsilon.$$

At $\varepsilon = 0.05$ this is $-0.001485$, i.e. $-0.15\%$ — exactly the
$-0.15\%$ the demonstration prints for $T$. The small residual is second order;
to first order the null direction is *exactly* the line of constant
$h_2\rho_2$ (its components satisfy $v_{\ln\rho_2} = -v_{\ln h_2}$ to within
4%).

---

## ★7 — A conductive third layer

**Prediction.** For a *thin conductive* layer the relevant invariant is the
longitudinal conductance $S = h/\rho$: current flows along the layer, and the
data are sensitive to $h/\rho$. So the null direction should be dominated by
$(\ln h_2, \ln\rho_2)$ with the **same** sign (both increasing together keeps
$h/\rho$ fixed), rather than opposite signs.

**Test.** Compute the Jacobian and its SVD for the conductive model exactly as
the demonstration does, then evaluate
$\mathrm{d}\ln(h_2/\rho_2)\cdot\varepsilon$ along $\hat{v}_\text{min}$ and
compare it with $\mathrm{d}\ln(h_2\rho_2)\cdot\varepsilon$: the prediction is
that the *first* is the smaller of the two by an order of magnitude. No data are
needed — the test is a property of the forward model.

---

## ★8 — Falsification test for a learned inversion

From the SVD analysis, the data have near-zero sensitivity along
$\hat{v}_\text{min}$: the map from data to model is not injective, so a network
that outputs a five-layer model with no uncertainty is outputting one arbitrary
member of an equivalence class.

**Falsification test.** Construct two models $m_1$ and $m_2$ that differ by
several per cent along the *known null direction* of the model class, and whose
synthetic data differ by less than the noise. Feed both data sets to the
network:

- If it returns two different models with narrow, non-overlapping uncertainty
  bands, it has invented resolution. **Fail.**
- If it returns bands that overlap and contain both models, it has learned the
  null space. **Pass**, provided the bands are calibrated (the frequency with
  which the truth falls inside the band matches the claimed coverage).

**What it must output.** A predictive distribution over models together with a
calibration statement — for example, a posterior sample set whose 90% intervals
cover the truth in 90% of a held-out test set *including cases constructed along
the null direction*. Point estimates alone cannot pass this test, and that is a
statement about the physics, not about the network.
