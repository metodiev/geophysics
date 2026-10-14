# Exercises — 09-03-01 IP Principle: Time-Domain and Frequency-Domain Measurement

Attempt these before reading the
[solutions](./01-ip-principle-solutions.md). The lesson is
[01 IP Principle](../01-ip-principle.md). All models are **SYNTHETIC** teaching
values throughout.

## ★ Foundational

**★1.** A synthetic ground has $m = 0.08$ and $\tau = 0.90$ s. Compute the
window-integral chargeability $M_{\text{int}}$ in ms and the window-average
chargeability $M_{\text{avg}}$ in mV/V for windows of $0.50$, $1.00$ and
$4.00$ s, using $M_{\text{int}} = m\tau\left(1 - e^{-T/\tau}\right)$.

**★2.** For $m = 0.25$ and $\tau = 0.40$ s, compute the peak phase magnitude in
mrad and the frequency at which it occurs, using
$\tan\lvert\varphi_{\max}\rvert = m/(2\sqrt{1-m})$ and
$f_{\max} = 1/(2\pi\tau\sqrt{1-m})$.

**★3.** A survey reports a window-average chargeability of
$25.0\ \mathrm{mV\,V^{-1}}$ measured over a $2.0$ s window. State the value of
$M_{\text{int}}$ in ms, and explain in one sentence why the number is not
$25.0$ ms.

## ★★ Applied

**★★4.** Show that $M_{\text{int}}(T)/M_{\text{int}}(\infty)$ depends only on
the ratio $T/\tau$, and check it against the lesson's demonstration table for
$\tau = 1.5$ s at $T = 2.00$ s, where the printed values are $110.460$ ms and
$149.997$ ms.

**★★5.** A survey used a charging time $t_{\text{on}} = 1.00$ s and a $1$ s
integration window, and reported $M_{\text{int}} = 35.514$ ms. The ground is in
fact the lesson's model ($\tau = 1.5$ s, fully charged value $72.987$ ms). If an
analyst ignores the incomplete charging and inverts $35.514$ ms with the
assumption of full charge, what $m$ do they infer instead of the true $0.100$?
Give the percentage error.

**★★6.** A linear drift of $s = 5.0$ mV/s acts over a $T = 2.0$ s window with
$V_p = 10.0$ V. Using
$\Delta M_{\text{int}} = \frac{1}{2}sT/V_p$, compute the bias in ms and state
whether it raises or lowers the apparent chargeability.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures the on-time bias rather than
assuming it: state the model, the quantity varied, the quantity held fixed, the
metric, and the predicted outcome for a ground with $\tau = 0.5$ s and
$t_{\text{on}} \in \{0.25, 0.5, 1, 2, 4\}$ s. A specification that could not be
executed with the tools in this module is a failed answer.

**★★★8.** Construct a second single-relaxation model with the **same**
$M_{\text{int}}(0\text{–}1\,\mathrm{s})$ as the lesson's model
($m = 0.10$, $\tau = 1.5$ s, $M = 72.987$ ms) but a different phase at $1$ Hz.
Use $\tau_2 = 0.30$ s, solve for $m_2$, then compute both models' phases at
$1$ Hz and quantify the difference.
