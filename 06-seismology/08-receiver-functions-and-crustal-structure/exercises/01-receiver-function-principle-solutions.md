# Solutions — 06-08-01 Receiver Functions: Deconvolution and Ps Conversions

> **Read after attempting the exercises.** Several problems have more than one
> defensible answer; where that is true it is said so. Numbers were computed, not
> estimated by hand.

Lesson: [01 Receiver Functions](../01-receiver-function-principle.md).

---

## ★1 — Vertical slowness

$$q = \sqrt{v^{-2}-p^{2}}.$$

For $v = 3.50$: $v^{-2} = 0.081633$, $p^{2} = 0.003600$,
$q = \sqrt{0.078033} = 0.279343\ \mathrm{s\,km^{-1}}$.

For $v = 6.00$: $v^{-2} = 0.027778$, $q = \sqrt{0.024178}
= 0.155492\ \mathrm{s\,km^{-1}}$.

**Unit:** $v^{-2}$ is $\mathrm{s^{2}\,km^{-2}}$, so $q$ is
$\mathrm{s\,km^{-1}}$ — the same unit as $p$, as it must be.

---

## ★2 — Ps delay

$$v_s^{-2} = 1/3.60^{2} = 0.077160, \quad q_s = \sqrt{0.077160 - 0.003025}
= \sqrt{0.074135} = 0.272284,$$
$$v_p^{-2} = 1/6.20^{2} = 0.026015, \quad q_p = \sqrt{0.026015 - 0.003025}
= \sqrt{0.022990} = 0.151624,$$
$$\Delta t_{Ps} = 30(0.272284 - 0.151624) = 30(0.120660)
= 3.6198\ \mathrm{s}.$$

---

## ★3 — Dimensional check

$H q_s$ has units $\mathrm{km}\times\mathrm{s\,km^{-1}} = \mathrm{s}$: a length
times a slowness is a time. ✔

---

## ★4 — Depth sensitivity to $k$

$$\frac{\mathrm{d}H}{\mathrm{d}k}\bigg|_{\Delta t}
= -\frac{H^{2}}{\Delta t}\,\frac{k}{v_p^{2}q_s}.$$

$k = 6.20/3.60 = 1.722$. $H^{2}/\Delta t = 900/3.6198 = 248.6\ \mathrm{km}$.
$k/(v_p^{2}q_s) = 1.722/(38.44\times0.272284) = 1.722/10.467 = 0.16453\ \mathrm{km\,s^{-1}}$.
Product: $-40.9\ \mathrm{km}$ per unit $k$.

A $4\%$ error: $\delta k = 0.0689$, so $\delta H = -40.9\times0.0689
= -2.82\ \mathrm{km}$ (about $-8\%$ of $35\ \mathrm{km}$... here $H = 30$ given
the delay at the assumed $k$; the relevant point is the magnitude, $\sim 2.8\
\mathrm{km}$).

---

## ★5 — Choosing a water level

Requirements: noise gain $<2\times$ and pulse FWHM small relative to
$0.4\ \mathrm{s}$.

From the demonstration table: gain $1.60\times$ at $10^{-5}$ (FWHM
$0.180\ \mathrm{s}$) and $1.26\times$ at $10^{-4}$ (FWHM $0.200\ \mathrm{s}$).
Both satisfy the gain constraint. The $0.4\ \mathrm{s}$ resolution requirement is
met comfortably by either, so the *tighter* of the two on noise is preferred:
**$10^{-4}$**, gain $1.26\times$, FWHM $0.200\ \mathrm{s}$, i.e. half the
resolution target. Choosing $10^{-5}$ would buy $0.02\ \mathrm{s}$ of sharpness
for $27\%$ more noise — a poor trade when the target is $0.4\ \mathrm{s}$.

**Note.** The defensible answer must state the noise metric. Gain here is
(tail rms of a noise-only receiver function)/(input noise rms), as defined in the
demonstration.

---

## ★6 — The 12.5 s peak is a multiple

For $H = 30$, $k = 1.726$, $p = 0.055$:
$q_p = \sqrt{0.025194-0.003025} = 0.148893$,
$q_s = \sqrt{0.075061-0.003025} = 0.268391$.

$$t_{PpPs} = H(q_s+q_p) = 30(0.417284) = 12.519\ \mathrm{s}.$$

The observed $12.5\ \mathrm{s}$ matches the PpPs multiple of the $30\ \mathrm{km}$
Moho to $0.02\ \mathrm{s}$. A deep converter at $100\ \mathrm{km}$ would require
$H(q_s-q_p) = 100(0.119498) = 11.95\ \mathrm{s}$ at this $p$ — close in time, so
the timing alone is ambiguous. The discriminator is **moveout**: the multiple's
delay decreases with $p^{2}$ (measured slope $-160\ \mathrm{s}$ per
$(\mathrm{s\,km^{-1}})^{2}$ in the demonstration), whereas a primary's increases
($+45.7$). A primary at $100\ \mathrm{km}$ would have the opposite sign.

---

## ★7 — Experiment design (specification)

**Metric:** $G(w) = \mathrm{rms}\big(\mathrm{RF}_{\text{noise-only}}(t>10\
\mathrm{s})\big)/\mathrm{rms}(\text{input noise})$, evaluated on a realisation
with the direct P but no Ps, so the ideal receiver function is a single spike at
zero.

**Prediction:** $G(w)$ is approximately independent of the input noise level for
a linear deconvolution, because both numerator and denominator scale with the
noise. The curves should therefore nearly coincide. The genuine effect of the
noise level is on the *reliability* of the result at a given $w$, not on $G$.
If the curves separate, the likely cause is a finite-precision floor or a
non-linear step such as a trace normalisation.

**Conclusion expected:** choose $w$ from the noise gain and the resolution
target, not from the noise level; the noise level sets how much gain you can
tolerate before the conversion is buried.

---

## ★8 — Why the check is restricted, and why $10^{-7}$

**Restriction.** Where $|V|^{2}\le 10^{-6}\max|V|^{2}$ the source truly has no
energy (the Ricker spectrum underflows), so the spectral ratio is $0/0$ and no
analytic value is meaningful. Comparing there would test the water-level
regulariser, not the mathematics.

**Magnitude.** The ratio is a sum of ~1000 complex operations with condition
number around $10^{7}$–$10^{9}$ because it divides by small $|V|$ within the
passband; double precision carries ~$10^{-16}$ relative error, so an absolute
deviation of order $10^{-7}$ is exactly what the conditioning predicts. A
deviation of $10^{-15}$ would indicate the division was never actually performed
(for example if both sides were computed from the same formula). The check is
therefore meaningful, and its size is a *measured conditioning diagnostic*.
