# Solutions — 10-01-03 Attenuation, Penetration Depth and Frequency Trade-Offs

> Read after attempting. Lesson:
> [03 Attenuation, Penetration and Frequency](../03-gpr-attenuation-penetration.md).

---

## ★1 — Attenuation constant

$$\alpha = \frac{\sigma}{2}\sqrt{\frac{\mu_0}{\varepsilon_0\varepsilon_r}}
= \frac{2\times10^{-3}}{2}\sqrt{\frac{1.2566\times10^{-6}}
{8.854\times10^{-12}\times 9}}
= 1\times10^{-3}\sqrt{1.5767\times10^{4}} = 0.1256\ \mathrm{m^{-1}}.$$

In dB: $8.686 \times 0.1256 = 1.091\ \mathrm{dB\,m^{-1}}$ (one way). Skin depth
$1/\alpha = 7.96\ \mathrm{m}$; two-way $1/e$ depth $1/(2\alpha) = 3.98\
\mathrm{m}$.

---

## ★2 — Two-way loss

$8.686 \times 2\alpha d = 8.686\times 2\times 0.1\times 3.0
= 5.21\ \mathrm{dB}$.

---

## ★3 — Constant-Q attenuation

$\alpha_Q = \pi f/(vQ)$ with $v$ in $\mathrm{m\,s^{-1}}$:

- $100\ \mathrm{MHz}$: $\pi\times10^{8}/(7.5\times10^{7}\times20)
  = 0.2094\ \mathrm{m^{-1}}$
- $400\ \mathrm{MHz}$: $0.8378\ \mathrm{m^{-1}}$

$Q$ loss is exactly linear in frequency, unlike conduction loss.

---

## ★4 — Combined attenuation

$$\alpha(200\ \mathrm{MHz}) = 0.0471 + \frac{\pi\times2\times10^{8}}
{7.495\times10^{7}\times12} = 0.0471 + 0.6986 = 0.7457\ \mathrm{m^{-1}},$$

of which conduction is $0.0471/0.7457 = 6.3\%$. In dB/m:
$8.686\times0.7457 = 6.48\ \mathrm{dB\,m^{-1}}$ — matching the demonstration's
$200\ \mathrm{MHz}$ row.

---

## ★5 — Spectral ratio inversion

$\alpha_{\mathrm{cond}} = \text{intercept}/(2\Delta d) = 0.15/3.0
= 0.0500\ \mathrm{m^{-1}}$.

The slope is expressed with the frequency in hertz, so the velocity must be in
metres per second: $v = 0.075\ \mathrm{m\,ns^{-1}} = 7.5\times10^{7}\
\mathrm{m\,s^{-1}}$. Then

$$Q = \frac{2\pi\Delta d}{v\,\text{slope}}
= \frac{2\pi\times1.5}{7.5\times10^{7}\times1.2\times10^{-8}}
= \frac{9.4248}{0.900} = 10.47.$$

**Unit trap:** the slope in $2\pi\Delta d/(vQ)$ is in *seconds* only if
$\Delta d$ is in metres and $v$ in $\mathrm{m\,s^{-1}}$. Carrying
$\mathrm{m\,ns^{-1}}$ into this formula without converting gives an answer
$10^{9}$ too large — and the number still looks reasonable.

---

## ★6 — Depth at the threshold

Solve $-20\log_{10}(2d) - 8.686\times2\times0.3\times d
+ 20\log_{10}0.2 = -70$:

$$\text{total}(d) = -13.98 - 20\log_{10}(2d) - 5.2116\,d.$$

Try $d = 1.0$: $-13.98 - 6.02 - 5.21 = -25.21\ \mathrm{dB}$. Try $d = 3.0$:
$-13.98 - 15.56 - 15.63 = -45.17$. Try $d = 6.0$:
$-13.98 - 21.58 - 31.27 = -66.83$. Try $d = 6.5$:
$-13.98 - 22.26 - 33.88 = -70.12$. So $d \approx 6.4$–$6.5\ \mathrm{m}$.

Note how the three terms trade: spreading supplied only $22\ \mathrm{dB}$ of the
$56\ \mathrm{dB}$ loss at that depth; attenuation supplied the rest.

---

## ★7 — Centroid estimator beyond first order

Tripling $t_{\mathrm{eff}}$ roughly triples the centroid shift (to about $8.2\%$
of the centroid) and triples the loss over the path in decibels. The first-order
expansion assumes the attenuated spectrum still resembles the reference one; at
$8\%$ upshift of the reference centroid the expansion's second-order term is
already comparable with the first, so the recovered $Q$ drifts high by tens of
per cent. The assumption that breaks is **weak attenuation over the path**, not
the signal-to-noise ratio.

---

## ★8 — Frequency design for $4\ \mathrm{m}$ at $-75\ \mathrm{dB}$

Assumptions to state: normal-incidence specular reflector with $|R| = 0.2$;
far-field $1/r$ spreading with a 1 m reference; $\alpha_{\mathrm{cond}} =
0.0471\ \mathrm{m^{-1}}$; $Q = 20$; no transmission losses.

Budget at $d = 4\ \mathrm{m}$: reflection $-13.98\ \mathrm{dB}$, spreading
$-18.06\ \mathrm{dB}$, leaving $-43.0\ \mathrm{dB}$ for attenuation, i.e.
$\alpha \le 43.0/(8.686\times2\times4) = 0.619\ \mathrm{m^{-1}}$.

Then $\alpha_Q \le 0.619 - 0.047 = 0.572\ \mathrm{m^{-1}}$, and from
$\alpha_Q = \pi f/(vQ)$ with $v = 0.09993\ \mathrm{m\,ns^{-1}} = 9.993\times
10^{7}\ \mathrm{m\,s^{-1}}$:

$$f_{\max} = \frac{\alpha_Q\,v\,Q}{\pi}
= \frac{0.572\times9.993\times10^{7}\times20}{\pi} = 3.64\times10^{8}\
\mathrm{Hz}.$$

So a frequency **below about $360\ \mathrm{MHz}$** meets the budget, and lower is
better for penetration but worse for resolution. The design choice is then made
against the resolution requirement of
[05 Resolution Limits](../05-gpr-resolution.md).
