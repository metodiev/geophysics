# Solutions — 06-09-06 Multiple Attenuation: SRME, Radon and Deconvolution

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [06 Multiple Elimination](../06-multiple-elimination.md).

---

## ★1 — Curvatures

$$q = \frac{1}{2t_0v^{2}}:$$

$$\text{primary: } q = \frac{1}{2\times1.2\times2400^{2}}
= \frac{1}{2\times1.2\times5.76\times10^{6}} = 7.234\times10^{-8}\
\mathrm{s\,m^{-2}},$$
$$\text{multiple: } q = \frac{1}{2\times2.0\times1500^{2}}
= \frac{1}{2\times2.0\times2.25\times10^{6}} = 1.111\times10^{-7}\
\mathrm{s\,m^{-2}},$$
$$\frac{q_{\text{mult}}}{q_{\text{prim}}} = 1.536 .$$

**Units:** $q$ multiplies $x^{2}$ to give a time, so $[q] =
\mathrm{s}/\mathrm{m^{2}} = \mathrm{s\,m^{-2}}$. A ratio of curvatures is
dimensionless.

---

## ★2 — The demonstration's curvatures

$$\text{primary: } q = \frac{1}{2\times1.00\times2500^{2}}
= \frac{1}{2\times6.25\times10^{6}} = 8.000\times10^{-8}\ \mathrm{s\,m^{-2}},$$
$$\text{multiple: } q = \frac{1}{2\times1.80\times1200^{2}}
= \frac{1}{2\times1.80\times1.44\times10^{6}} = 1.929\times10^{-7}\
\mathrm{s\,m^{-2}},$$
$$\frac{q_{\text{mult}}}{q_{\text{prim}}} = \frac{1.929\times10^{-7}}{8.000\times10^{-8}}
= 2.411 . \quad\checkmark$$

Both match the printed values. The multiple is *more curved* because it is both
later ($t_0$ larger, which by itself would reduce $q$) and slower
($v$ smaller, which increases $q$ as $1/v^{2}$); the velocity effect wins by a
factor of $2.4$.

---

## ★3 — The parabolic approximation

Start from the exact hyperbola and factor out $t_0$:

$$t(x) = \sqrt{t_0^{2}+\frac{x^{2}}{v^{2}}}
= t_0\left(1+\frac{x^{2}}{t_0^{2}v^{2}}\right)^{1/2}.$$

Expanding the square root for small argument, $(1+u)^{1/2} = 1+u/2-u^{2}/8+\dots$
with $u = x^{2}/(t_0^{2}v^{2})$:

$$t(x) \approx t_0 + \frac{x^{2}}{2t_0v^{2}}
- \frac{x^{4}}{8t_0^{3}v^{4}} + \dots$$

so the moveout is

$$\Delta t(x) \approx \frac{x^{2}}{2t_0v^{2}} - \frac{x^{4}}{8t_0^{3}v^{4}}
= qx^{2} - \frac{(qx^{2})^{2}}{2t_0} + \dots,
\qquad q \equiv \frac{1}{2t_0v^{2}}.$$

**Neglected term:** the quartic term $x^{4}/(8t_0^{3}v^{4})$, i.e. order $x^{4}$
in offset. It matters when $x^{2}/(t_0^{2}v^{2})$ is not small — the same
condition as the anellipticity residual measured in lesson 02.

---

## ★4 — Why the curvature mute is blunt

The demonstration measures the *price* of a mute in an underdetermined
transform: 31 curvature values and 220 intercept times define 6820 model
parameters for 3300 data values. The LSQR solution is therefore smeared across
curvature values, and a primary at one curvature has energy spread over several
neighbouring curvature rows; muting 4 rows removes part of the multiple *and*
part of the primary. The measured trade is symmetric and poor:

$$\text{primary preserved} = \frac{0.5505}{0.6464} = 85.2\%, \qquad
\text{multiple remaining} = \frac{0.4402}{0.5214} = 84.4\%.$$

**A change to the inversion, not the mute.** Impose a **sparsity or
high-resolution constraint** on the Radon model (for example an
$\ell_1$-regularised or high-resolution Radon inversion) so that each event
collapses onto few curvature values. Then the mute removes the multiple's rows
without touching the primary's rows, and both numbers improve. A second option
is to make the transform's sampling match the data better (fewer, better-chosen
curvature values with a design matrix conditioning check) before applying the
mute.

---

## ★5 — Predictive deconvolution

$$\text{attenuation} = 20\log_{10}\frac{0.8000}{0.3220}
= 20\log_{10}2.484 = 20\times0.39515 = 7.90\ \mathrm{dB}.$$

The primary is unchanged in *amplitude* ($1.0000 \to 1.0000$), so the
primary-to-multiple ratio improves from $1.250$ to $3.106$.

**What the table does not show.** Predictive deconvolution is a *shaping*
operation: it also shortens the wavelet (the autocorrelation's non-zero-lag
terms are suppressed along with the multiple's periodic term). That means:
(i) the primary's wavelet is now different from the input, so any amplitude
comparison before and after is invalid; (ii) where the multiple and primary
overlap in time, the operation removes part of the primary's own energy; and
(iii) the filter's design assumes the multiple lag is stationary over the
window, which fails where the water depth or the moveout changes. This is why
predictive deconvolution belongs **early** in the flow, before amplitudes are
interpreted.

---

## ★6 — Three-stage sequence (specification)

| stage | mechanism | QC number | failure mode that hurts the next stage |
|---|---|---|---|
| 1. Deterministic + predictive deconvolution | multiple periodicity from the surface (multiples are *periodic* along a trace) | multiple amplitude before/after; autocorrelation of the output | over-shortens the wavelet and removes primary energy at interfering lags, biasing later amplitude work |
| 2. Radon (parabolic) transform + mute | multiple has a larger *curvature* (measured: $q$ ratio $2.41$) | round-trip residual of the transform; primary preserved versus multiple attenuated, both as numbers | smeared model means the mute also cuts the primary (the measured $85.2\%$), and steep dips alias into the mute zone |
| 3. SRME | multiple is *predicted from the data* by surface-consistent convolution, so it needs no velocity separation | residual of the adaptive subtraction; the predicted multiple's own coherence | aggressive subtraction removes primary energy where the prediction is wrong (over-subtraction); fails where the near-offset data needed for the prediction are missing |

**Justification of the order.** Deconvolution first (it operates trace by trace
and needs no velocity). Radon second (it needs a velocity to parametrise
curvature, so it must follow velocity analysis). SRME third, because it works
best on data already free of the short-period multiples (otherwise it predicts
multiples *of* multiples and the adaptive subtraction has more to do); and last
because its over-subtraction risk is the hardest to detect, so it should operate
on the cleanest input.

**The cascade risk.** Each stage is judged by the *ratio* it improves, and each
can improve its own metric while damaging the next stage's input. That is why
the QC numbers must be defined on the *final* objective (residual multiple
energy *and* primary amplitude at the target) and not only on the intermediate
metric of the stage being tuned.

---

## ★7 — The round-trip residual and the mute

The round-trip residual is
$\Vert\mathbf{G}\hat{\mathbf m}-\mathbf d\Vert/\Vert\mathbf d\Vert$: it measures
how well the model reproduces the data after inversion. A residual of $1.30\%$
means the transform pair is effectively invertible in this discretisation, so the
Radon panel is a faithful re-parametrisation of the data and the *only* reason a
mute damages the primary is the smearing of the model — not a lossy transform.

With a $30\%$ round-trip residual the panel would no longer represent the data:
muting curvature rows would leave the residual energy in the unmuted-data space,
i.e. the multiple would reappear as a model residual *and* the primary would be
damaged by the imperfect inverse. **The mute's selectivity would degrade in both
directions at once**, and the primary/multiple ratio could get *worse* after the
mute than before — a strong diagnostic that the transform, not the mute, is
broken.

**Experiment that would establish the trade-off versus iteration count.**

1. Fix the geometry and the events (the demonstration's primary and multiple).
2. For $N_{\text{iter}} \in \{25, 50, 100, 200, 400, 800\}$, invert, record the
   round-trip residual, apply the *same* 4-row mute, invert back, and measure
   (a) primary preserved, (b) multiple remaining, (c) their ratio.
3. Plot all three against $N_{\text{iter}}$ with the residual as the abscissa;
   report the iteration count at which the ratio stops improving.
4. The decision rule is then:"use the smallest $N_{\text{iter}}$ whose
   primary-preserved is within some tolerance of its converged value", and the
   honest caveat is that the answer depends on the curvature separation (the
   measured $2.41$) and on the noise level.
