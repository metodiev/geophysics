# Solutions — 16-05-06 Emulators and Surrogate Models for Climate

> Read after attempting the exercises. Lesson:
> [06 Emulators and Surrogate Models](../06-emulation-and-surrogates.md).

---

## ★1 — One-point GP prediction

With one training point, $K = \sigma_f^{2}+\sigma_n^{2}$ (a scalar),
$k_* = \sigma_f^{2}\exp\!\left[-(x-x_1)^{2}/(2\ell^{2})\right]$, and
$\bar y$ the prior mean:

$$\mu_*(x) = \bar y + \frac{k_*(x)}{\sigma_f^{2}+\sigma_n^{2}}\,(y_1-\bar y),
\qquad
\sigma_*^{2}(x) = \sigma_f^{2} - \frac{k_*(x)^{2}}{\sigma_f^{2}+\sigma_n^{2}}.$$

At $x = x_1$: $k_* = \sigma_f^{2}$, so

$$\mu_* = \bar y + \frac{\sigma_f^{2}}{\sigma_f^{2}+\sigma_n^{2}}(y_1-\bar y),
\qquad
\sigma_*^{2} = \sigma_f^{2}\left(1-\frac{\sigma_f^{2}}{\sigma_f^{2}+\sigma_n^{2}}\right)
= \frac{\sigma_f^{2}\sigma_n^{2}}{\sigma_f^{2}+\sigma_n^{2}},$$

which is the noise floor: with $\sigma_n \ll \sigma_f$ it is
$\approx\sigma_n^{2}$, and with $\sigma_n \gg \sigma_f$ it is
$\approx\sigma_f^{2}$.

As $|x-x_1|\to\infty$: $k_*\to0$, so $\mu_*\to\bar y$ and
$\sigma_*^{2}\to\sigma_f^{2}$. The prediction reverts to the prior and the
uncertainty saturates at the prior variance — it does **not** grow without bound,
which is why a very wrong extrapolation can carry a modest-looking stated
uncertainty.

---

## ★2 — Interpolation versus extrapolation

$$\frac{3.2512}{0.0830} = 39.2.$$

The emulator's error is nearly forty times larger outside the training range than
inside. The ratio measures how much of the emulator's skill is supplied by the
data rather than by its smoothness prior; outside the design there is no data,
so the emulator can only return its prior.

---

## ★3 — Linear surrogate error at $F = 6.0$

Absolute error: $7.5000 - 4.3290 = 3.1710\ \mathrm{K}$ (the demonstration prints
this difference). Relative error: $3.1710/4.3290 = 0.7325$, i.e. $73.3\%$. The
surrogate over-predicts by nearly three-quarters of the true response, and the
error is systematically one-signed: it does not average out over a range of
forcings.

---

## ★4 — Prior covariance at a separation of $4.0$

$$k = \sigma_f^{2}\exp\!\left(-\frac{4.0^{2}}{2(2.0)^{2}}\right)
= 1.0 \times e^{-2} = 0.1353\ \mathrm{K^{2}}.$$

As a fraction of the prior variance $\sigma_f^{2} = 1.0\ \mathrm{K^{2}}$:
$0.1353$, i.e. $13.5\%$. Two inputs separated by $2\ell$ are therefore nearly
uncorrelated under the RBF kernel ($1-e^{-2} = 86.5\%$ of the variance is
independent). This is the quantitative meaning of the length scale: it is the
distance over which the function is assumed to remember itself.

---

## ★5 — The interval that does not contain the answer

Nominal $95\%$ interval half-width:

$$1.96 \times 0.0605 = 0.1186\ \mathrm{K}.$$

Actual mean absolute error in the window: $0.6944\ \mathrm{K}$.

$$\frac{0.6944}{0.1186} = 5.85.$$

So the typical error is nearly six nominal $95\%$ half-widths — equivalently the
error-to-sd ratio is $11.47$ (the demonstration's value, using the standard
deviation rather than the half-width). The emulator is not merely uncertain; it
is miscalibrated, and the miscalibration is invisible from its own output.

---

## ★6 — Placing five points near a transition

**Placement.** Spread them across the window, for example at
$F = 3.6, 3.8, 4.0, 4.2, 4.4\ \mathrm{W\,m^{-2}}$. A single point at the
transition is not enough, because a smooth kernel will bend a single point back
toward the surrounding trend; several points establish the local gradient on each
side.

**Expected changes.** (i) The RMSE *away* from the transition should be almost
unchanged: those regions already have data, and adding points elsewhere does not
improve them. (ii) The error-to-uncertainty ratio in the window should fall
sharply, from $11.470$ toward $\mathcal{O}(1)$, because the emulator now has data
where the response changes and its predictive variance is calibrated by the local
residuals. A ratio near 1 is the diagnostic of a calibrated emulator.

---

## ★7 — GP versus cubic polynomial

**Interpolation.** Prefer the GP: it reports a predictive variance, so its
confidence is inspectable, and its length-scale-driven smoothness adapts to the
data density. A cubic fitted by least squares will match a smooth region well and
give no local error estimate at all.

**Extrapolation.** Trust neither. The GP reverts to its prior mean with
prior-sized variance (measured in the demonstration: error $5.8037\ \mathrm{K}$
against a stated sd of $0.9988\ \mathrm{K}$ at
$F = 12\ \mathrm{W\,m^{-2}}$). A cubic extrapolates its leading term, which will
diverge rapidly and with no warning at all.

**What to report.** For any prediction outside the design: the range of the
training data, the emulator's stated uncertainty, and an explicit statement that
the prediction is an extrapolation. Where possible, report a physical bound
instead of an extrapolated number.

---

## ★8 — Critique of a projection whose uncertainty is the emulator's sd

**Missing quantities.**

1. **Structural model error.** The emulator approximates a *particular*
   simulator (see [16-05-05](../05-coupled-model-intercomparison.md)). Its
   variance says nothing about whether that simulator represents the Earth.
2. **Inter-model spread.** A single emulated model gives no information about
   the dispersion across models, which dominates the total uncertainty at long
   horizons.
3. **Emulator bias.** Section 6 of the lesson measures an error eleven times the
   stated standard deviation in an unsampled region; a miscalibrated emulator
   understates uncertainty by construction.
4. **Forcing and scenario ambiguity.** The emulator is conditioned on an input
   pathway; uncertainty in the pathway is a separate term.
5. **Training-design dependence.** The stated sd is a function of where the
   training points were placed, not of the physics.

**What would have to be true for the reported uncertainty to be the total one.**
That the emulator is the only source of uncertainty — i.e. that the simulator is
the Earth (it is not), that the design samples the relevant regime densely and
uniformly, that the emulator is perfectly calibrated, and that emissions,
concentrations and the model's structural response are known exactly. None of
these holds, so the reported number is a lower bound on the uncertainty and
should be labelled as such.
