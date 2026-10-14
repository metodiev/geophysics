# Solutions — 10-01-04 Antennas

> Read after attempting. Lesson: [04 Antennas](../04-gpr-antennas.md).

---

## ★1 — Half-wave lengths

Air: $\lambda = c/f = 0.299792458/0.25\ \mathrm{GHz} = 1.199\ \mathrm{m}$, so
$L/2 = 0.600\ \mathrm{m}$.

$\varepsilon_r = 9$: $\lambda = 1.199/\sqrt{9} = 1.199/3 = 0.400\ \mathrm{m}$, so
$L/2 = 0.200\ \mathrm{m}$ — a factor $3 = \sqrt{\varepsilon_r}$ shorter, matching
the demonstration's table ($0.200\ \mathrm{m}$ at $250\ \mathrm{MHz}$).

---

## ★2 — Critical angle and footprint

$\theta_c = \arcsin(1/\sqrt{6.25}) = \arcsin(0.4) = 23.578^\circ$.

Footprint radius at $1.5\ \mathrm{m}$:
$d\tan\theta_c = 1.5\times0.4364 = 0.655\ \mathrm{m}$. Equivalently
$d/\sqrt{\varepsilon_r-1} = 1.5/\sqrt{5.25} = 0.655\ \mathrm{m}$.

---

## ★3 — Air wave, ground wave, blind zone

$t_{\mathrm{air}} = 0.50/0.299792458 = 1.668\ \mathrm{ns}$.

$t_{\mathrm{ground}} = 0.50/0.075 = 6.667\ \mathrm{ns}$.

$d_{\min} = x/2 = 0.25\ \mathrm{m}$. Note the ratio
$t_{\mathrm{ground}}/t_{\mathrm{air}} = 4.00 = \sqrt{\varepsilon_r}$, giving
$\varepsilon_r = 16$ from the two arrival times alone.

---

## ★4 — Polarisation angles

$|\cos\psi| = 0.40$, so $\psi = \arccos(0.40) = 66.42^\circ$ or
$180^\circ - 66.42^\circ = 113.58^\circ$ — i.e. $\pm$ the same angle about the
quadrature. Power factor $\cos^{2}\psi = 0.16$, i.e. $-7.96\ \mathrm{dB}$.

Neither amplitude alone distinguishes the two: a repeat line with the antennas
rotated by $90^\circ$ does (the relative amplitudes swap), and a target whose
axis is not linear (a cylinder end-on) needs the full azimuthal response.

---

## ★5 — Power inside a cone

$F(30^\circ) = 0.01286$ and $F(45^\circ) = 0.05806$ (both from the demonstration,
and both reproducible from
$F(\theta) = \tfrac{3}{4}\left(\cos^{3}\theta/3 - \cos\theta + 2/3\right)$).

The $45^\circ$ cone holds $4.5$ times the power of the $30^\circ$ cone — a
statement about how diffuse a dipole's radiation is: widening the cone from
$30^\circ$ to $45^\circ$ adds almost as much power as the first $30^\circ$
contained.

---

## ★6 — Offset penalty at a shallow target

Zero offset: $t_0 = 2\times0.40/0.09993 = 8.006\ \mathrm{ns}$.

With $x = 0.40\ \mathrm{m}$:
$t = \sqrt{4\times0.40^{2}+0.40^{2}}/0.09993 = \sqrt{0.64+0.16}/0.09993
= 0.8944/0.09993 = 8.951\ \mathrm{ns}$.

$\Delta t = 0.945\ \mathrm{ns}$, so the depth error if the offset is ignored is
$(v/2)\Delta t = 0.09993/2 \times 0.945 = 0.0472\ \mathrm{m} = 4.7\
\mathrm{cm}$ — about $12\%$ of the target depth.

---

## ★7 — One dipole, several media

$f_{\mathrm{res}} = c/(2L\sqrt{\varepsilon_r})$ with $L = 0.150\ \mathrm{m}$:

| $\varepsilon_r$ | 1 | 4 | 9 | 16 | 25 |
|---|---|---|---|---|---|
| $f_{\mathrm{res}}$ (MHz) | 999.3 | 499.7 | 333.1 | 249.8 | 199.9 |

The antenna's electrical length is set by the medium it is coupled to, so the
*same* physical object is a $1\ \mathrm{GHz}$ antenna in air and a $200\
\mathrm{MHz}$ antenna in saturated clay. Since moisture changes with depth and
season, the radiated band moves with it: a survey cannot assume a fixed band, and
that is one reason the recorded spectrum is measured rather than assumed. The
practical consequence is that "the $250\ \mathrm{MHz}$ antenna" is a design
label, and the band in the ground must be checked (Section 2 of
[02 Processing](../../02-gpr-acquisition-and-processing/02-gpr-processing.md)).

---

## ★8 — Footprint versus Fresnel zone

Footprint radius at $1\ \mathrm{m}$, $\varepsilon_r = 9$:
$d/\sqrt{\varepsilon_r-1} = 1/\sqrt{8} = 0.354\ \mathrm{m}$.

Fresnel radius at $1\ \mathrm{m}$ for $f = 200\ \mathrm{MHz}$ in the same medium
($v = 0.07495\ \mathrm{m\,ns^{-1}}$, $\lambda = 0.375\ \mathrm{m}$):
$r = \sqrt{\lambda d/2 + \lambda^{2}/16} = \sqrt{0.1875+0.0088} = 0.4437\
\mathrm{m}$.

The two are comparable but not equal, and they answer different questions. The
**footprint** is where energy is delivered; a target anywhere inside it can be
*detected*. The **Fresnel zone** is the coherent reflecting area that determines
the *shape* of the received pulse and hence the horizontal resolution. Confusing
them is a common way to over-claim: a target the size of the footprint radius is
detectable and completely unresolvable.
