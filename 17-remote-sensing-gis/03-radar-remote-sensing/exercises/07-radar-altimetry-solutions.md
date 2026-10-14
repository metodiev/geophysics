# Solutions — 17-03-07 Radar Altimetry and Sea/Ice Surface Height

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [07 Radar Altimetry](../07-radar-altimetry.md).

---

## ★1 — Range from a round-trip time

$$r = \frac{ct}{2} = \frac{299\,792\,458 \times 5.3347\times10^{-3}}{2}
= 799\,650\ \mathrm{m}\ (5\ \text{s.f.}).$$

Height above the reference ellipsoid:
$$h_{\text{surf}} = 800\,000 - 799\,650 = 350\ \mathrm{m}.$$

**Corrections ignored:** (i) the atmospheric path delay — the wet and dry
tropospheric delays and the ionospheric delay, of the order of decimetres to
metres in range, which is *larger* than the geophysical signal; (ii) the
solid-Earth and ocean tides, which move the reference surface itself by up to a
decimetre. A further class, the instrument's own bias and the retracking choice,
also belongs in the list. The point of the exercise is that a 1 cm height claim
requires all of these at the centimetre level.

---

## ★2 — Pulse-limited footprint

$$\rho = \sqrt{c\tau h} = \sqrt{299\,792\,458 \times 2\times10^{-9}
\times 9.0\times10^{5}} = \sqrt{5.3963\times10^{5}} = 734.6\ \mathrm{m}.$$

Area:
$$A = \pi\rho^{2} = \pi \times (734.6)^{2} = 1.6950\times10^{6}\ \mathrm{m^{2}}
= 1.6950\ \mathrm{km^{2}}.$$

Note the square-root dependence: doubling the altitude increases the radius by
$\sqrt{2}$ and the area by 2, while doubling the pulse length does the same for
both. Shrinking the footprint therefore requires a shorter pulse, which requires
more bandwidth — the same trade as range resolution in
[lesson 01](../01-sar-principles.md).

---

## ★3 — Wave height from the leading edge

$$\text{SWH} = \frac{0.80}{0.6407} = 1.2487\ \mathrm{m}.$$

For $\tau = 1\ \mathrm{ns}$ the flat-pulse rise contributes
$c\tau/2 = 0.1499\ \mathrm{m}$ of range, which is $c\tau/2 / (0.6407\times SWH)
= 0.1499/(0.6407\times1.2487) = 18.7\%$ of the measured width. So this is the
**regime where the correction matters**: a $\sim19\%$ error would be incurred by
using the converged factor blindly. The demonstration's own numbers show the same
effect: the converged ratio 0.6407 becomes 0.6550 (a $2.2\%$ correction) only
once $SWH$ reaches 1 m.

---

## ★4 — Geostrophic speed and latitude

$$f = 2\Omega\sin\phi,\qquad u = -\frac{g}{f}\frac{\partial h}{\partial y}.$$

**(a)** At $60^\circ$ N: $f = 2(7.292\,115\times10^{-5})\sin 60^\circ
= 1.2630\times10^{-4}\ \mathrm{s^{-1}}$. The slope is
$0.02/50\,000 = 4.0\times10^{-7}$, so
$$u = \frac{9.80665}{1.2630\times10^{-4}}\times4.0\times10^{-7}
= 7.7637\times10^{4}\times4.0\times10^{-7} = 0.03106\ \mathrm{m\,s^{-1}}.$$

**(b)** At $10^\circ$ N: $f = 2(7.292\,115\times10^{-5})\sin 10^\circ
= 2.5325\times10^{-5}\ \mathrm{s^{-1}}$, giving
$$u = \frac{9.80665}{2.5325\times10^{-5}}\times4.0\times10^{-7}
= 0.15489\ \mathrm{m\,s^{-1}},$$

five times larger for the *same* height gradient.

**Comment:** as $\phi \to 0$ the geostrophic relation diverges, and the balance
itself fails (the Coriolis force vanishes and the dynamics become ageostrophic).
The practical consequence is that equatorial currents cannot be inferred from SSH
slopes with this formula at all: near the equator the geostrophic
approximation, not the measurement, is the limiting problem. It also means that a
*small* height error produces a large velocity error at low latitude, so
altimetric current products are least reliable exactly where the strongest
currents are.

---

## ★5 — Aliasing M2

**(a)** $T_r = 15$ d, so $f_s = 1/360\ \mathrm{h^{-1}} = 2.7778\times10^{-3}$.
$f_{M2} = 1/12.4206012 = 0.0805114\ \mathrm{h^{-1}}$.
$n = \operatorname{round}(0.0805114/0.0027778) = \operatorname{round}(28.98) = 29$.
$$f_{\text{alias}} = \left|0.0805114 - 29\times2.7778\times10^{-3}\right|
= \left|0.0805114 - 0.0805556\right| = 4.42\times10^{-5}\ \mathrm{h^{-1}}.$$
$$T_{\text{alias}} = \frac{1}{4.42\times10^{-5}} = 22\,624\ \mathrm{h}
= 942.7\ \mathrm{days} \approx 2.58\ \mathrm{yr}.$$

A semidiurnal tide appears as a two-and-a-half-year signal — and it is perfectly
coherent with the sampling, so it will look like a trend or a very low-frequency
ocean signal to any analysis that does not model it.

**(b)** To resolve a constituent rather than alias it, the repeat cycle must be
chosen so that the aliased frequency of each constituent of interest falls where
it can be separated from the others and from the true low-frequency variability.
In practice this means (i) a cycle incommensurate with the tidal periods, so that
the aliases of M2, S2, K1 and O1 land far apart in frequency, and (ii) a long
enough record that the alias periods are covered several times. The dependence is
extreme — the 5, 10, 20 and 35-day cycles of the lesson give aliases of 14.8,
31.0, 56.4 and 94.5 days — which is why mission repeat cycles are chosen with the
tide model and the science target in hand, not for operational convenience.

---

## ★6 — Freeboard to thickness with uncertainties

Thickness:
$$T = F\frac{\rho_w}{\rho_w-\rho_i} = 0.40 \times 9.2613 = 3.7045\ \mathrm{m}.$$

**From the freeboard alone:** $\partial T/\partial F = 9.2613$, so
$$\delta T_F = 9.2613 \times 0.03 = 0.278\ \mathrm{m}.$$

**From the density:** $\partial T/\partial\rho_i = F\rho_w/(\rho_w-\rho_i)^{2}
= 0.40\times1.028/0.111^{2} = 33.38\ \mathrm{m\ per\ g\,cm^{-3}}$, so
$$\delta T_{\rho} = 33.38 \times 0.002 = 0.0668\ \mathrm{m}.$$

**Which dominates:** the freeboard term, $0.278$ m against $0.0668$ m — a factor
of $4.2$. Combined in quadrature:
$$\delta T = \sqrt{0.278^{2} + 0.0668^{2}} = 0.286\ \mathrm{m},$$
so the density contributes only $2.6\%$ of the variance here.

**The honest reading:** for *this* freeboard and density uncertainty the
measurement is limited by the freeboard, but the balance is not robust — the
density term grows linearly with $F$ while the freeboard term does not shrink, so
for a 1 m freeboard with a $0.002\ \mathrm{g\,cm^{-3}}$ density uncertainty the
density term would be $0.167$ m and would matter more. Both uncertainties must be
propagated and reported; neither may be assumed away.

---

## ★7 — Error budget for a 5 cm/s current (specification)

**Required height precision.** From the lesson's rule at $45^\circ$ N,
$u = (g/f)\times$slope with $g/f = 9.51\times10^{4}$, so
$5\ \mathrm{cm\,s^{-1}} = 0.05\ \mathrm{m\,s^{-1}}$ requires
$$\text{slope} = \frac{0.05}{9.51\times10^{4}} = 5.26\times10^{-7}
\;\Longrightarrow\;
\Delta h = 5.26\times10^{-7}\times2.0\times10^{4} = 1.05\ \mathrm{cm}$$
over $20\ \mathrm{km}$. So the required precision is **about 1 cm of SSH**, and it
must be achieved *differentially* over the 20 km, not absolutely — a smooth
common error cancels in the gradient.

**Spatial averaging and its cost.** The lesson's speckle table: for a
$\sigma_1 = 45\ \mathrm{cm}$ single-pulse precision, 1 cm needs
$N = (45/1)^{2} = 2025$ pulses. The averaging length along track is $N$ divided by
the pulse rate; at $2\ \mathrm{kHz}$ that is about 1 s of flight, i.e. roughly
7 km along track for a $7\ \mathrm{km\,s^{-1}}$ platform. **The 20 km gradient is
therefore resolved with about three independent estimates** — a marginal, not
comfortable, measurement, and the resolution cost is the reason the current
cannot be mapped at finer scales by this method.

**Corrections to apply, in order of expected size.** (i) the geoid/mean-sea-surface
removal — largest in absolute terms, but smooth and therefore partially
cancelling in a short gradient; (ii) the wet tropospheric delay from a
radiometer — the dominant *non-smooth* error at the centimetre level; (iii) the
solid-Earth and ocean tides; (iv) the ionosphere, which is small at these
frequencies but not negligible at solar maximum; (v) the inverse barometer;
(vi) the orbit, which must be consistent between epochs.

**Expected dominant term:** the wet tropospheric delay, because it is spatially
variable at the scale of tens of kilometres and can reach several centimetres —
exactly the scale of the signal. The budget should state the radiometer's
accuracy and the spatial structure of its residual, not only its mean.

---

## ★8 — Why the ratio exceeds 0.6407 at small wave heights

**(a) Mechanism.** The measured leading edge is the convolution of the
flat-pulse response with the surface height distribution. The flat-pulse response
is not a step but a ramp of length $c\tau/2$ in range, so it contributes its own
variance. Writing $\sigma_{\text{eff}}^{2} = \sigma_z^{2} +
(c\tau/2)^{2}/12$ (the second moment of a uniform distribution of width
$c\tau/2$),
$$\frac{w}{SWH} = \frac{2.5628\,\sigma_{\text{eff}}}{4\sigma_z}
= 0.6407\sqrt{1 + \frac{(c\tau/2)^{2}}{12\,\sigma_z^{2}}}.$$

At $SWH = 1\ \mathrm{m}$ ($\sigma_z = 0.25$ m) with $c\tau/2 = 0.1499\ \mathrm{m}$:
$$0.6407\sqrt{1 + \frac{0.1499^{2}}{12\times0.0625}}
= 0.6407\sqrt{1.02996} = 0.6502,$$
against the measured $0.6550$ — a $0.7\%$ difference attributable to the
rectangular pulse not being Gaussian, which is the level at which a real
retracker must model the waveform rather than apply a factor.

At $SWH = 8\ \mathrm{m}$ ($\sigma_z = 2$ m) the same bracket is
$\sqrt{1.000117} = 1.00006$, i.e. $0.6407$ to four decimals — which is exactly
the measured convergence.

**(b) The limit $SWH \to 0$.** The bracket diverges as $1/\sigma_z$: as the sea
flattens, the measured width stops shrinking with the wave height and is pinned by
the pulse. Numerically the width tends to the finite value
$$w \to 2.5628\,\frac{c\tau}{2\sqrt{12}} = 2.5628 \times 0.04327
= 0.11089\ \mathrm{m},$$
while $SWH \to 0$, so the ratio diverges. Two evaluations of the exact
expression:

| $SWH$ | $\sigma_z$ | $\sigma_{\text{eff}}$ | $w$ | $w/SWH$ |
|---|---|---|---|---|
| 1.00 m | 0.2500 m | 0.25371 m | 0.6502 m | 0.6502 |
| 0.25 m | 0.0625 m | 0.076020 m | 0.19480 m | 0.7792 |

At a $25\ \mathrm{cm}$ sea the ratio is $0.779$, a $22\%$ error against the
converged factor.

**(c) Practical implication.** A wave-height retrieval for a calm sea
($SWH \lesssim 0.5\ \mathrm{m}$) that uses the converged factor $0.6407$ will
overestimate the wave height systematically, because part of the measured width is
the instrument's own pulse. The remedy is retracking with a model that includes
the flat-pulse response; the honest report states the retracker used, its
validated wave-height range, and the fact that below some $SWH$ the retrieval is
limited by the pulse rather than by the sea.
