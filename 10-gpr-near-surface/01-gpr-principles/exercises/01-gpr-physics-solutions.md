# Solutions — 10-01-01 GPR Physics

> Read after attempting. Lesson: [01 GPR Physics](../01-gpr-physics.md).
> $c = 0.299792458\ \mathrm{m\,ns^{-1}}$, all models SYNTHETIC.

---

## ★1 — Speeds

$v = c/\sqrt{\varepsilon_r}$ with $c$ in $\mathrm{m\,ns^{-1}}$:

- $\varepsilon_r = 1$: $v = 0.299792 \approx 0.29979\ \mathrm{m\,ns^{-1}}$
- $\varepsilon_r = 4$: $\sqrt{4} = 2$, $v = 0.14990\ \mathrm{m\,ns^{-1}}$
- $\varepsilon_r = 16$: $\sqrt{16} = 4$, $v = 0.07495\ \mathrm{m\,ns^{-1}}$
- $\varepsilon_r = 80.1$: $\sqrt{80.1} = 8.950$, $v = 0.03350\
  \mathrm{m\,ns^{-1}}$

$c$ carries $\mathrm{m\,ns^{-1}}$, $\varepsilon_r$ is dimensionless, so $v$ is
$\mathrm{m\,ns^{-1}}$: a length divided by a time.

---

## ★2 — Depth conversion

$d = vt/2$ with $t$ in ns:

- $v = 0.060$: $d = 0.060 \times 40.0/2 = 1.200\ \mathrm{m}$
- $v = 0.075$: $d = 0.075 \times 40.0/2 = 1.500\ \mathrm{m}$

One pick, two depths $25\%$ apart: the velocity is an assumption.

---

## ★3 — Reflection coefficient

$$R = \frac{\sqrt{4}-\sqrt{25}}{\sqrt{4}+\sqrt{25}} = \frac{2-5}{2+5}
= -0.4286.$$

$R^{2} = 0.1837$ (reflected energy), $1-R^{2} = 0.8163$ (transmitted energy);
the sum is $1.0000$.

---

## ★4 — Loss tangent

$$\tan\delta = \frac{\sigma}{2\pi f\varepsilon_0\varepsilon_r}
= \frac{2\times10^{-3}}{2\pi \times 10^{8} \times 8.854\times10^{-12} \times 9}
= \frac{2\times10^{-3}}{5.004\times10^{-2}} = 0.0400.$$

$\tan\delta = 0.04 \ll 0.1$, and from the demonstration the error of the low-loss
speed at $\tan\delta = 0.03$ is $+0.01\%$ and at $0.04$ well under $0.1\%$. The
formula may be used; state the value $0.040$ with the answer.

---

## ★5 — Speed to permittivity

$\varepsilon_r = (c/v)^{2} = (0.299792458/0.07)^{2} = (4.2828)^{2} = 18.34$.

For a fractional error $\delta v/v = 0.03$,
$\delta\varepsilon_r/\varepsilon_r = 2\,\delta v/v = 0.06$, i.e.
$\varepsilon_r = 18.3 \pm 1.1$ (or $\pm 6\%$). The factor of two is the point:
inverting a square root doubles the relative error.

---

## ★6 — Ricker spectral mean

$$\frac{2}{\sqrt{\pi}}f_0 = 1.1284 \times 200 = 225.676\ \mathrm{MHz}$$

which matches the measurement exactly. The mean exceeds the peak because the
spectrum $\propto f^{2}\exp(-f^{2}/f_0^{2})$ is skewed towards high frequencies
(it is zero at $f = 0$ by construction, since a Ricker carries no DC).

---

## ★7 — Depth error from a permittivity error

$t = 2d\sqrt{\varepsilon_r}/c = 2 \times 2.0 \times
\sqrt{9}/0.299792458 = 40.028\ \mathrm{ns}$.

With the true $\varepsilon_r = 16$ the depth is
$d = v t/2 = \left(0.299792458/\sqrt{16}\right) \times 40.028/2
= 0.07495 \times 20.014 = 1.500\ \mathrm{m}$.

Reported depth $2.000\ \mathrm{m}$ against a true $1.500\ \mathrm{m}$: an error of
$+0.500\ \mathrm{m}$ ($+33.3\%$). It is exactly
$1 - \sqrt{9/16} = -25\%$... in the other direction: using too high a speed (the
assumed $\varepsilon_r = 9$ gives $v = 0.09993$ against the true $0.07495$)
overestimates the depth by the ratio $v_{\text{assumed}}/v_{\text{true}} = 1.333$,
i.e. $+33.3\%$. The assumption that caused it is the permittivity, not the
arithmetic.

---

## ★8 — Depth error at large loss tangent

The instrument records a *time*. If the analyst converts with a speed that is
$9.87\%$ too high, the depth is $9.87\%$ too large:

$$\delta d = 0.0987 \times 3.0 = 0.296\ \mathrm{m},$$

always **too deep**, on every pick: a systematic bias, not scatter. (The
comparison is at fixed measured time, which is the correct one: the wave really
did arrive at that time, it simply travelled slower than assumed.)
