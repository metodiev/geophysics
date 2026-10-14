# Solutions — 08-02-01 Fluxgate Magnetometers: Principle and Use

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [01 Fluxgate Magnetometers](../01-fluxgate-magnetometers.md).

---

## ★1 — The sense-coil EMF

$$|e|_{\max} = NA\left|\frac{\mathrm{d}B}{\mathrm{d}t}\right|_{\max}
= 200\times2.0\times10^{-5}\times3.9473\times10^{4}
= 157.892\ \mathrm{V}.$$

Unit chain: $\left[\mathrm{turns}\right]$ is dimensionless;
$\mathrm{m^2}\times\mathrm{T\,s^{-1}} = \mathrm{T\,m^2\,s^{-1}} = \mathrm{V}$
because $1\ \mathrm{V} = 1\ \mathrm{T\,m^2\,s^{-1}}$ (the SI weber per second).

The lesson's coil ($N = 50$, $A = 1.0\times10^{-5}\ \mathrm{m^2}$) gave
$19.736\ \mathrm{V}$; scaling by $(200/50)\times(2.0/1.0) = 8$ gives
$157.89\ \mathrm{V}$ ✔. The lesson that matters: the EMF is proportional to
$NA$, so a **voltage** specification is meaningless without the coil.

---

## ★2 — Knee field in field units

$$\mu_0H_k = 4\pi\times10^{-7}\times20 = 2.5133\times10^{-5}\ \mathrm{T}
= 25133\ \mathrm{nT} = 25.13\ \mu\mathrm{T}.$$

Physical meaning: it is the flux density at which the core's magnetisation
reaches the knee of its curve, i.e. the field scale over which the core stops
being a high-permeability material. It is therefore the field scale at which the
second-harmonic response stops being linear: **the dynamic range of the sensor
is set by the core, not by the electronics.**

---

## ★3 — Sensitivity in nT per volt

$$75.4807\ \mu\mathrm{V\,nT^{-1}}
= 7.54807\times10^{-5}\ \mathrm{V\,nT^{-1}}
\;\Longrightarrow\;
\frac{1\ \mathrm{V}}{7.54807\times10^{-5}\ \mathrm{V\,nT^{-1}}}
= 13248.4\ \mathrm{nT}.$$

So one volt of output corresponds to $1.3\times10^{4}\ \mathrm{nT}$ of field.
Note the reciprocal relationship with the noise calculation of ★6: sensitivity
and noise must be quoted as a pair.

---

## ★4 — Converting the slope

$$\frac{\mathrm{d}A(2f)}{\mathrm{d}H_e}
= 9.4852\times10^{-2}\ \mathrm{V\,(A\,m^{-1})^{-1}}.$$

One nanotesla is $10^{-9}/\mu_0 = 10^{-9}/1.256637\times10^{-6}
= 7.957747\times10^{-4}\ \mathrm{A\,m^{-1}}$, so

$$9.4852\times10^{-2}\times7.957747\times10^{-4}
= 7.5481\times10^{-5}\ \mathrm{V\,nT^{-1}}
= 75.481\ \mu\mathrm{V\,nT^{-1}},$$

matching the lesson's $75.4807\ \mu\mathrm{V\,nT^{-1}}$. ✔

---

## ★5 — Cross-axis leak

$$B_{\text{leak}} = B_\perp\sin\alpha.$$

$\alpha = 0.3^{\circ}$: $\sin\alpha = 5.23599\times10^{-3}$, so
$B_{\text{leak}} = 48000\times5.23599\times10^{-3} = 251.33\ \mathrm{nT}$.

$\alpha = 0.05^{\circ}$: $\sin\alpha = 8.72665\times10^{-4}$,
$B_{\text{leak}} = 41.888\ \mathrm{nT}$.

**Requirement for 1 nT:** $\sin\alpha \le 1/48000 = 2.0833\times10^{-5}$, so
$\alpha \le 0.00119^{\circ}$ — about **4.3 arcseconds**. That is not achievable
by mechanical mounting. The practical route is calibration: measure the sensor's
response to a known field in several orientations and solve for the alignment
matrix, which reduces the effective $\alpha$ to the calibration's own
uncertainty. This is why component surveys are calibrated rather than aligned.

---

## ★6 — Noise and averaging

Bandwidth 10 Hz:

$$v_{\text{rms}} = 3.162\times10^{-4}\times\sqrt{10}
= 1.000\times10^{-3}\ \mathrm{V}, \qquad
\sigma_B = \frac{1.000\times10^{-3}}{7.54807\times10^{-5}}
= 13.248\ \mathrm{nT}.$$

Bandwidth 0.1 Hz:

$$v_{\text{rms}} = 3.162\times10^{-4}\times\sqrt{0.1}
= 1.000\times10^{-4}\ \mathrm{V}, \qquad
\sigma_B = \frac{1.000\times10^{-4}}{7.54807\times10^{-5}}
= 1.325\ \mathrm{nT}.$$

**To reach 0.5 nT** by averaging at 10 Hz bandwidth requires a reduction by
$13.248/0.5 = 26.496$, and since averaging $N$ independent readings reduces the
standard error by $\sqrt{N}$,

$$N = 26.496^{2} = 702.0 \quad\Longrightarrow\quad N \approx 702.$$

Narrowing the bandwidth to 0.1 Hz achieves most of the same gain with no
averaging at all, because it is mathematically the same operation — provided the
noise is white and the signal is steady over the longer integration.

---

## ★7 — Calibrating a three-axis fluxgate (specification)

**Model.** Write the measured vector $\mathbf{m}$ as
$\mathbf{m} = S R \mathbf{B} + \mathbf{o}$, where $R$ is an unknown rotation
(three small angles), $S$ a diagonal matrix of sensitivities, and $\mathbf{o}$ a
constant offset vector.

**Measurements.** Place the sensor in a field you can hold constant (a
Helmholtz coil set, or the Earth's field over a few minutes) at $K \ge 12$
orientations covering the sphere. At each orientation record the three channel
outputs.

**Algebra.** The unknown parameters are $3 + 3 + 3 = 9$; with 12 orientations
there are 36 equations, so the system is over-determined and can be solved by
least squares. A convenient parametrisation is a $3\times3$ matrix
$M = SR$ (9 entries) plus $\mathbf{o}$ (3), fitted by minimizing
$\sum_k\left|\mathbf{m}_k - M\mathbf{B}_k - \mathbf{o}\right|^2$ with
$|\mathbf{B}_k| = B_0$ imposed as a constraint — the classic "ellipsoid fit".

**Identifiability.** With only the field's magnitude known, the product $MB_0$ is
all that can be determined: a global scale factor is unidentifiable without an
absolute scalar instrument. Similarly, a rotation of the *reference frame*
cannot be separated from a rotation of the sensor, so the sensor's alignment with
north is unidentifiable from the coil data alone. The remedy is one scalar
magnetometer for the scale and one astronomical or gyroscopic azimuth for the
frame; everything else can then be solved. **Stating which parameters require
which external reference is the point of the exercise.**

---

## ★8 — Leading nonlinearity of the second-harmonic response

Write $u = H_d\sin\omega t/H_k$ and $\epsilon = H_e/H_k$, so
$M = M_s\tanh(u+\epsilon)$, and expand about $u$:

$$\tanh(u+\epsilon) = \tanh u + \epsilon\,\operatorname{sech}^2 u
- \epsilon^{2}\operatorname{sech}^2u\,\tanh u
+ \frac{\epsilon^{3}}{3}\operatorname{sech}^2u\left(3\tanh^2u-2\right)
+ O(\epsilon^4).$$

The EMF is $-NA\mu_0(\mathrm{d}M/\mathrm{d}t)$ plus the vacuum term, so each
power of $\epsilon$ contributes a distinct harmonic structure:

- the $\epsilon^0$ term is odd in $t$ about the drive zero: **odd** harmonics;
- the $\epsilon^1$ term, $\operatorname{sech}^2u\,\mathrm{d}u/\mathrm{d}t$, is
  even in $t$ after differentiating: **even** harmonics, linear in $H_e$. This
  is the measurement;
- the $\epsilon^2$ term is odd: odd harmonics only, no contribution at $2f$;
- the $\epsilon^{3}$ term is even again: **even** harmonics, cubic in $H_e$.

So the **leading correction to the $2f$ amplitude is cubic in $H_e/H_k$**, and it
appears at the same frequency as the signal, which is why it cannot be removed by
filtering. Its sign: the coefficient $3\tanh^2u-2$ is negative where the core is
saturated and positive in the knee region, so its time average at $2f$ opposes
the linear term and the response **saturates** — exactly what the demonstration
shows, with a 0.35% departure from linearity already at
$H_e = 3200\ \mathrm{nT}$ ($H_e/H_k = 0.13$).

**Practical consequence.** The cubic term is why a fluxgate calibration is a
curve, not a constant, once the field becomes a non-negligible fraction of
$\mu_0H_k$; and it is why larger dynamic range is bought by choosing a core with
a larger knee field, at the cost of sensitivity.
