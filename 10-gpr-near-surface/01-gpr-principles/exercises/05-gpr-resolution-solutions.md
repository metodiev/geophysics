# Solutions — 10-01-05 Resolution Limits

> Read after attempting. Lesson: [05 Resolution Limits](../05-gpr-resolution.md).

---

## ★1 — Reference lengths

$\lambda = v/f = 0.09993/0.2\ \mathrm{GHz} = 0.49965\ \mathrm{m}$ (the
demonstration prints $0.4996$).

$\lambda/2 = 0.2498$ m, $\lambda/4 = 0.1249$ m, $\lambda/8 = 0.0625$ m.

---

## ★2 — Fresnel radius at 1 m

Exact: $r = \sqrt{\lambda d/2 + \lambda^{2}/16}
= \sqrt{0.4996\times1.0/2 + 0.24960/16}
= \sqrt{0.2498 + 0.01560} = \sqrt{0.26540} = 0.5152\ \mathrm{m}$.

Approximate: $\sqrt{\lambda d/2} = \sqrt{0.2498} = 0.4998\ \mathrm{m}$.

Difference: $0.4998/0.5152 - 1 = -2.98\%$; the approximation is *low*.

---

## ★3 — Unaliased dip

$\sin\theta_{\max} = \lambda/(4\Delta x)$.

$\Delta x = 0.125\ \mathrm{m}$: $\sin\theta_{\max} = 0.4996/0.5 = 0.9992$,
$\theta_{\max} = 87.7^\circ$ — this is the $\lambda/4$ rule.

$\Delta x = 0.25\ \mathrm{m}$: $\sin\theta_{\max} = 0.4996/1.0 = 0.4996$,
$\theta_{\max} = 29.98^\circ$.

---

## ★4 — Two reflectors at 0.30 m

Rayleigh-type limit: $0.170\lambda = 0.170\times0.4996 = 0.0849\ \mathrm{m}$.

$0.30\ \mathrm{m} > 0.0849\ \mathrm{m}$, so they are comfortably **resolved** by
that criterion. (The criterion is generous here: the empirical "$\lambda/4$"
rule gives $0.1249\ \mathrm{m}$, also below $0.30\ \mathrm{m}$.)

Two-way time separation: $\Delta t = 2\Delta z/v = 2\times0.30/0.09993
= 6.00\ \mathrm{ns}$ — more than one dominant period ($5\ \mathrm{ns}$), so no
interference question arises.

---

## ★5 — Thin-bed thickness from amplitude

$A/A_{\text{single}} = 0.35$, and the linear regime gives
$\Delta z \approx 0.35/21.32 = 0.0164\ \mathrm{m} = 1.64\ \mathrm{cm}$.

One-sided because the relation holds only **below** the tuning thickness: the
amplitude–thickness curve is monotone only up to $\Delta z \approx
0.100\ \mathrm{m}$ and then *decreases*. The same amplitude of $0.35$ could
correspond to a thickness on the far side of the tuning peak, so the estimate is
a lower bound unless the thickness is independently known to be small. The
correct statement is "$0.016\ \mathrm{m}$, if the bed is thinner than the tuning
thickness".

---

## ★6 — Aliased apparent dip

$\sin\theta = \sin30^\circ = 0.5000$.

$\lambda/(2\Delta x) = 0.4996/0.60 = 0.8327$, so wrapping with $m = 1$:

$$\sin\theta_{\text{app}} = 0.5000 - 0.8327 = -0.3327
\Rightarrow \theta_{\text{app}} = -19.43^\circ.$$

Check the Nyquist band: the allowed range is
$|\sin\theta_{\text{app}}| \le \lambda/(4\Delta x) = 0.4163$, and
$0.3327 < 0.4163$, so $m=1$ is the correct choice. A $30^\circ$ dip would be
reported as an apparent $-19.4^\circ$ dip.

---

## ★7 — Aperture for 0.2 m separation

The measured widths (at $z = 1\ \mathrm{m}$, $\lambda = 0.4996\ \mathrm{m}$) are
$0.475$, $0.275$, $0.225$ and $0.175\ \mathrm{m}$ for apertures $\pm0.5$, $\pm1$,
$\pm2$ and $\pm4\ \mathrm{m}$. A separation of $0.2\ \mathrm{m}$ needs an image
width no larger than about that value, which is first achieved at
$\pm2\ \mathrm{m}$ ($0.225\ \mathrm{m}$) and is comfortable at $\pm4\
\mathrm{m}$ ($0.175\ \mathrm{m}$).

The assumption that limits the extrapolation is that resolution keeps improving
with aperture. It does not: at large aperture the width saturates at the
bandwidth limit (about a third of a wavelength here), so beyond a few target
depths extra aperture buys nothing, and the Fresnel-zone-limited regime becomes
the bandwidth-limited one.

---

## ★8 — Why vertical resolution is the more reliable improvement

Vertical resolution is set by the **temporal bandwidth** alone: from the
measurement, the Rayleigh-type separation is $0.170\lambda$, so it scales exactly
as $1/f$ — doubling the frequency halves it, and nothing about the acquisition
geometry intervenes.

Horizontal resolution is set by the **aperture** as well as the band: the same
measurement shows the point-spread width falling from $0.951\lambda$ to
$0.350\lambda$ purely by widening the aperture at fixed frequency. Raising the
frequency shortens $\lambda$, which helps, but if the aperture is small the width
stays pinned near the Fresnel diameter
($2\sqrt{\lambda d/2+\lambda^{2}/16} = 1.030\ \mathrm{m}$ at $z = 1\
\mathrm{m}$), and at $400\ \mathrm{MHz}$ in a wet medium the penetration
(6.48 dB/m at $\alpha$ of the earlier lesson at $200\ \mathrm{MHz}$; higher still
at $400$) may remove the target entirely. So the frequency is a blunt instrument
for horizontal resolution, and the aperture is a sharper one.
