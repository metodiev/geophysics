# Solutions — 09-03-01 IP Principle: Time-Domain and Frequency-Domain Measurement

> **Read after attempting the exercises.** Numbers are computed, not estimated.
> Lesson: [01 IP Principle](../01-ip-principle.md). All models **SYNTHETIC**.

---

## ★1 — Chargeability against the window

$$M_{\text{int}}(T) = m\tau\left(1 - e^{-T/\tau}\right), \qquad
M_{\text{avg}} = M_{\text{int}}/T, \qquad m\tau = 0.08 \times 0.90
= 0.0720\ \mathrm{s} = 72.0\ \mathrm{ms}.$$

| $T$ (s) | $1 - e^{-T/\tau}$ | $M_{\text{int}}$ (ms) | $M_{\text{avg}}$ (mV/V) |
|---|---|---|---|
| 0.50 | $1 - e^{-0.5556} = 0.42625$ | $30.690$ | $61.380$ |
| 1.00 | $1 - e^{-1.1111} = 0.67088$ | $48.298$ | $48.298$ |
| 4.00 | $1 - e^{-4.4444} = 0.98826$ | $71.155$ | $17.789$ |

At $T = 1.00$ s the two conventions coincide in value ($48.298$), which is the
numerical content of "$1\ \mathrm{mV\,V^{-1}} = 1$ ms for a one-second window".
They differ at every other window.

---

## ★2 — Peak phase and peak frequency

$$\tan\lvert\varphi_{\max}\rvert = \frac{0.25}{2\sqrt{0.75}}
= \frac{0.25}{1.732051} = 0.144338\ \Longrightarrow\
\lvert\varphi_{\max}\rvert = 0.143348\ \mathrm{rad} = 143.348\ \mathrm{mrad},$$

$$f_{\max} = \frac{1}{2\pi \times 0.40 \times \sqrt{0.75}} = 0.459441\ \mathrm{Hz}.$$

---

## ★3 — The two conventions

$M_{\text{int}} = T \times M_{\text{avg}} = 2.0 \times 25.0 = 50.0$ ms.

The window-integral chargeability has units of time, while the window-average is
dimensionless: they differ by exactly the factor $T = 2$, so the same ground
gives $50.0$ ms and $25.0$ mV/V. Neither can be reported without its window.

---

## ★4 — Only the ratio $T/\tau$ matters

$$M_{\text{int}}(T) = m\tau\left(1 - e^{-T/\tau}\right), \qquad
M_{\text{int}}(\infty) = m\tau
\;\Longrightarrow\;
\frac{M_{\text{int}}(T)}{M_{\text{int}}(\infty)} = 1 - e^{-T/\tau}.$$

The right-hand side contains $T$ and $\tau$ only through their ratio, so the
*fraction* of the total chargeability captured by a window is a universal
function of $T/\tau$ — independent of $m$.

Check at $\tau = 1.5$ s, $T = 2.0$ s: $T/\tau = 1.3333$,
$1 - e^{-1.3333} = 0.73640$; and
$110.460/149.997 = 0.73641$. The two agree to the printed digits, so the
demonstration's table is consistent with the closed form.

---

## ★5 — Inverting with the wrong assumption

If charging is ignored, the analyst uses
$M = m\tau\left(1 - e^{-T/\tau}\right)$ with the printed
$\left(1 - e^{-1/1.5}\right) = 0.486583$ and the known $\tau = 1.5$ s:

$$m_{\text{inferred}} = \frac{35.514\ \mathrm{ms}}
{1000 \times 1.5 \times 0.486583} = \frac{0.035514}{0.729875} = 0.04866.$$

The true value is $m = 0.100$, so the inferred chargeability is low by
$\left(0.04866 - 0.100\right)/0.100 = -51.3\%$. This is not a small correction:
it is the factor $\left(1 - e^{-t_{\text{on}}/\tau}\right) = 0.4866$ in disguise,
and it can be mistaken for a weakly polarisable ground.

---

## ★6 — Drift bias

$$\Delta M_{\text{int}} = \frac{\frac{1}{2}sT}{V_p}
= \frac{0.5 \times 5.0\times10^{-3}\ \mathrm{V\,s^{-1}} \times 2.0\ \mathrm{s}}
{10.0\ \mathrm{V}} = 5.0\times10^{-4}\ \mathrm{s} = 0.500\ \mathrm{ms}.$$

With a drift of this sign, the measured $V_s$ is larger than the decay, so the
apparent chargeability is **raised** by $0.500$ ms. Note the scaling: both the
drift rate and the window appear linearly, so halving the drift halves the bias
and doubling the window doubles it.

---

## ★7 — Measuring the on-time bias (specification)

**Model.** A synthetic Debye ground with $m = 0.10$, $\tau = 0.50$ s, driven with
a step-off current; the decay is $V_s(t) = mV_p e^{-t/\tau}$.

**Quantity varied.** $t_{\text{on}} \in \{0.25, 0.5, 1, 2, 4\}$ s — five
charging times, one field campaign's worth of settings.

**Held fixed.** $m$, $\tau$, $V_p$, the integration window $T = 0.50$ s, the
sampling rate and the noise realisation (same seed for every $t_{\text{on}}$, so
the comparison is paired).

**Metric.** $M_{\text{int}} = \frac{1}{V_p}\int_0^{T}V_s\,\mathrm{d}t$ and its
ratio to the fully charged reference
$M_{\text{ref}} = m\tau\left(1 - e^{-T/\tau}\right)$.

**Predicted outcome.** The measured value is
$m\tau\left(1 - e^{-t_{\text{on}}/\tau}\right)\left(1 - e^{-T/\tau}\right)$, so
the ratio is $1 - e^{-t_{\text{on}}/\tau}$ evaluated at
$t_{\text{on}}/\tau = 0.5, 1, 2, 4, 8$, i.e.
$0.3935, 0.6321, 0.8647, 0.9817, 0.9997$. The bias therefore saturates only
beyond about five time constants; a survey that fixes $t_{\text{on}} = 1$ s
silently measures $63\%$ of the chargeability of this ground.

**Executable check.** The same arithmetic is the section-6 table of
[`code/ip_principle_demo.py`](../code/ip_principle_demo.py), which prints the
bias for a $\tau = 1.5$ s model; substituting $\tau = 0.5$ s reproduces the five
ratios above.

---

## ★8 — Same chargeability, different phase

Solve for $m_2$ with $\tau_2 = 0.30$ s:

$$\left(1 - e^{-1/0.30}\right) = 0.964326, \qquad
m_2 = \frac{0.072987}{0.30 \times 0.964326} = \frac{0.072987}{0.289298}
= 0.252290.$$

So $\left(m_2, \tau_2\right) = \left(0.2523, 0.30\ \mathrm{s}\right)$ reproduces
$M_{\text{int}}(0\text{–}1\,\mathrm{s}) = 72.987$ ms exactly.

Phases at $1$ Hz, from
$\rho/\rho_0 = (1-m) + m/(1+i\omega\tau)$ with $\omega = 2\pi$:

- model 1 ($m = 0.100$, $\tau = 1.5$ s): $11.643$ mrad (the lesson's value);
- model 2 ($m = 0.2523$, $\tau = 0.30$ s): $129.326$ mrad.

The two models are indistinguishable in the time-domain window integral
($72.987$ ms each) and differ by a factor $11.1$ in the $1$ Hz phase. Any
procedure that converts one domain to the other through an assumed model will
give a different answer for the two grounds; the data cannot choose between them
without a frequency-domain measurement.

*Useful extra check.* The phase of model 2 is also obtainable from the closed
forms: its peak is at
$f_{\max} = 1/(2\pi\times0.30\times\sqrt{0.7477}) = 0.6135$ Hz, so $1$ Hz is
above the peak, on the descending branch, which is why $129$ mrad is well below
its peak value — a reminder that a single-frequency phase is not a peak phase.
