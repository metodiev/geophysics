# Solutions — 06-08-03 Moho Discontinuity Depth and Sharpness

> Read after attempting. Lesson: [03 Moho Interface](../03-moho-interface.md).

---

## ★1 — Depth

$v_s = 6.30/1.72 = 3.663\ \mathrm{km\,s^{-1}}$.
$q_p = \sqrt{1/39.69-0.0036} = \sqrt{0.021595} = 0.146954$.
$q_s = \sqrt{1/13.417-0.0036} = \sqrt{0.070938} = 0.266342$.
$H = 4.10/(0.266342-0.146954) = 4.10/0.119388 = 34.34\ \mathrm{km}$.

State the assumption: "34.3 km assuming $v_p = 6.30$ and $k = 1.72$".

---

## ★2 — Units

$q_p = 0.146954\ \mathrm{s\,km^{-1}}$, $q_s = 0.266342\ \mathrm{s\,km^{-1}}$.
Both are slownesses; $H(q_s-q_p)$ is a time.

---

## ★3 — Depth error from $\delta p$

$$\delta H = \delta p\,\frac{H\,p}{q_s-q_p}
\left(\frac{1}{q_p}-\frac{1}{q_s}\right).$$

$q_p = \sqrt{1/38.44-0.003025} = 0.151746$,
$q_s = \sqrt{1/12.99-0.003025} = \sqrt{0.073956} = 0.271949$.
$q_s-q_p = 0.120203$. $1/q_p - 1/q_s = 6.5900 - 3.6772 = 2.9128\
\mathrm{km\,s^{-1}}$.

$$\delta H = 0.008 \times \frac{35\times0.055}{0.120203} \times 2.9128
= 0.008 \times 16.014 \times 2.9128 = +0.373\ \mathrm{km}.$$

So a $+0.008\ \mathrm{s\,km^{-1}}$ ($+15\%$) reference error inflates the depth
by about $0.37\ \mathrm{km}$ ($\sim1\%$).

---

## ★4 — Transition width

Solve $\operatorname{sinc}(\pi f w_z q_s) = 0.62$. The first root of
$\sin x/x = 0.62$ is $x \approx 1.62$, so

$$w_z = \frac{1.62}{\pi\times0.25\times0.27} = \frac{1.62}{0.21206}
= 7.64\ \mathrm{km}.$$

The transition is about $7.6\ \mathrm{km}$ thick **at $0.25\ \mathrm{Hz}$**.

---

## ★5 — The 13.5 s peak is a multiple

$v_s = 6.2/1.72 = 3.605\ \mathrm{km\,s^{-1}}$.
At $p = 0.055$: $q_p = \sqrt{0.026015-0.003025} = 0.151624$,
$q_s = \sqrt{1/12.995-0.003025} = \sqrt{0.073930} = 0.271920$.

$$t_{PpPs} = 30(0.271920+0.151624) = 30(0.423544) = 12.706\ \mathrm{s},$$
$$t_{PpSs} = 2(30)(0.271920) = 16.315\ \mathrm{s}.$$

$13.5\ \mathrm{s}$ lies between these; a multiple from a slightly thicker layer
or a different phase fits it far better than a deep converter, which would need a
*positive* moveout. Moveout slopes for these multiples:
$\partial t_{PpPs}/\partial p^{2} = -H(1/q_s+1/q_p)/2
= -30(3.6774+6.5953)/2 = -154.1\ \mathrm{s}$ per $(\mathrm{s\,km^{-1}})^{2}$;
$\partial t_{PpSs}/\partial p^{2} = -H/q_s = -110.3$. A deep primary would have a
*positive* slope of order $+45$. The negative sign rules out a primary.

---

## ★6 — Bandwidth study

$w_z = 4\ \mathrm{km}$, $q_s = 0.27\ \mathrm{s\,km^{-1}}$, so
$\pi f w_z q_s = 3.393 f$ (with $f$ in Hz).

| $f$ (Hz) | argument | $\operatorname{sinc}$ | verdict at this $f$ |
|---|---|---|---|
| 0.2 | 0.679 | 0.892 | sharp |
| 0.5 | 1.696 | 0.588 | gradational |
| 1.0 | 3.393 | −0.284 | thin-bed / sign-reversed |
| 2.0 | 6.79 | 0.145 | thin-bed ringing |

At $0.2\ \mathrm{Hz}$ the interface looks nearly sharp; at $1\ \mathrm{Hz}$ the
response is small and reversed, the signature of a layer near the tuning
thickness. **Choose $0.2$–$0.3\ \mathrm{Hz}$** to characterise sharpness: it is
the band where the amplitude varies smoothly and monotonically with width, so
inversion for $w_z$ is well posed. At $1\ \mathrm{Hz}$ the sinc has a sign change
and the amplitude–width relation is non-monotonic, hence ambiguous.

---

## ★7 — $k$ versus $p$

From the demonstration: a $0.010\ \mathrm{s\,km^{-1}}$ change in the reference
slowness ($17\%$) gives $\sim0.4\ \mathrm{km}$ of depth error, i.e.
$\sim1.25\%$. A $5\%$ error in $k$ ($1.714\to1.800$) gives
$-3.38\ \mathrm{km}$, i.e. $\sim10.6\%$. Per unit fractional error, $k$ hurts
roughly $8$–$9$ times more than $p$ for this model. **A Moho map is far more
sensitive to the assumed velocity ratio than to the ray-parameter bookkeeping**,
which is why velocity-ratio assumptions must be stated and tested first.
