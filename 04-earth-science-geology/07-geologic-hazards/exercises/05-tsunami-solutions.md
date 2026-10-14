# Solutions — 04-07-05 Tsunami Generation, Propagation and Warning

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Speed and travel time

**(a)** $c = \sqrt{gh}$: 99.03 m s⁻¹ (356.5 km h⁻¹) at 1000 m, 171.52 m s⁻¹
(617.5 km h⁻¹) at 3000 m and 198.06 m s⁻¹ (713.0 km h⁻¹) at 4000 m.

**(b)** 2000 km at 1000 m: 5.61 h. At 3000 m: 3.24 h. At 4000 m: 2.81 h.

**(c)** 1000 km at 4000 m: $10^6/198.06 = 5049$ s $= 1.40$ h.
1000 km at 1000 m: $10^6/99.03 = 10\,098$ s $= 2.81$ h. Total $4.21$ h — and
the shallow half takes twice as long as the deep half for the same distance.

**(d)** The travel time is $\int \mathrm{d}s/\sqrt{gh}$, so each kilometre costs
$1/\sqrt{gh}$: the cost per kilometre is *smaller* where the water is deeper.
The deep segment therefore contributes little to the total and the shallow
segment dominates, even though they are equal in length. The same reasoning
means a travel-time prediction is insensitive to errors in the deepest part of a
path and sensitive to errors on the shelf.

---

## ★2 — Wavelength and regime

**(a)** $L = T\sqrt{gh} = 900\times198.06 = 178.3$ km.

**(b)** $h/L = 4000/1.783\times10^5 = 0.0224$, far below the $1/20$ criterion:
the shallow-water approximation applies comfortably.

**(c)** A 10 s wave at 4000 m: $L = 10\times198.06 = 1.98$ km and
$h/L = 2.02$: it is a **deep-water** wave.

**(d)** The tsunami is non-dispersive because $c$ does not depend on $L$ in the
long-wave limit, so a front survives the crossing; the wind wave disperses,
which is why a storm sea arrives spread out over hours and a tsunami arrives as
a front. In a bottom-pressure record the same distinction means the tsunami is
visible and the sea state is not.

---

## ★3 — Shoaling

**(a)** Green's law is $A \propto h^{-1/4}$. Derivation: energy per unit area is
$\tfrac12\rho gA^2$, the energy travels at $c_g = \sqrt{gh}$, and energy flux per
unit crest length is conserved, so $A^2\sqrt{gh}$ is constant.

**(b)** $A = 0.4(4000/50)^{1/4} = 0.4\times2.991 = 1.196$ m.

**(c)** $A = 0.4(4000/10)^{1/4} = 0.4\times4.472 = 1.789$ m.

**(d)** Real amplitudes depart because (i) the wave breaks once its height
becomes comparable with the local depth, which caps the growth; (ii) bays,
harbours and the beach profile produce resonance and run-up that (5) does not
describe; and (iii) bottom friction and lateral spreading remove energy. Green's
law gives the offshore amplitude at a depth contour, not the run-up.

---

## ★4 — The bore

**(a)** In the frame of the front, mass conservation gives $ch_1 = (c-v)h_2$,
so $v = c(1-h_1/h_2)$. Momentum conservation across the front gives
$\tfrac12 g(h_2^2-h_1^2) = ch_1v$. Eliminating $v$:

$$c^2 = \frac{g(h_2^2-h_1^2)h_2}{2h_1(h_2-h_1)}
= \frac{g h_2(h_1+h_2)}{2h_1}.$$

**(b)** With $h_1 = 2$ m and $h_2 = 4$ m:
$c = \sqrt{9.80665\times4\times6/(2\times2)} = \sqrt{58.84} = 7.67$ m s⁻¹ and
$v = 7.67(1-2/4) = 3.84$ m s⁻¹.

**(c)** With $h_2 = 3$ m: $c = \sqrt{9.80665\times3\times5/4} = \sqrt{36.77}
= 6.06$ m s⁻¹ and $v = 6.06(1-2/3) = 2.02$ m s⁻¹. Halving the height reduces
the speed by 21 per cent and the onshore flow by 47 per cent.

**(d)** Set $h_2 = h_1 + H$ and let $H \to 0$:
$h_2(h_1+h_2)/(2h_1) \to h_1(2h_1)/(2h_1) = h_1$, so $c \to \sqrt{gh_1}$, the
linear shallow-water speed. The nonlinear relation contains the linear theory as
its small-amplitude limit, which is the check that it was derived correctly.

---

## ★★5 — The exact dispersion relation

**(a)**

| $T$ (s) | $c_\mathrm{exact}$ (m s⁻¹) | $\sqrt{gh}$ (m s⁻¹) | relative error |
|---|---|---|---|
| 300 | 192.136 | 198.057 | $3.082\times10^{-2}$ |
| 600 | 196.579 | 198.057 | $7.516\times10^{-3}$ |
| 1200 | 197.688 | 198.057 | $1.868\times10^{-3}$ |

**(b)** The $(kh)^2/6$ column is $3.169\times10^{-2}$, $7.567\times10^{-3}$ and
$1.871\times10^{-3}$: it agrees with the measured error to three significant
figures at every period. The relative error of the shallow-water approximation
is $k^2h^2/6$, at least while $kh$ is small, which is the leading term of the
expansion of $\tanh(kh)$. The agreement is a numerical confirmation of an
analytic prediction rather than a repetition of the same calculation.

**(c)** $k^2h^2/6 = 0.01$ gives $kh = 0.245$. With $kh = 2\pi f h/\sqrt{gh}
= 2\pi\sqrt h/(T\sqrt g)$, $kh = 0.245$ in 4000 m corresponds to
$T = 2\pi h/(0.245\sqrt{gh}) = 2\pi\times4000/(0.245\times198.06) = 518$ s, so
periods shorter than about **8 to 9 minutes** carry more than 1 per cent error.

**(d)** At $T = 120$ s, $L = 120\times198.06 = 23.8$ km and $h/L = 0.168$: not
shallow by the $1/20$ criterion, though the error in $c$ is still only 23 per
cent. At $T = 1200$ s, $L = 237.7$ km and $h/L = 0.0168$: shallow by a factor
of three.

---

## ★★6 — The bore and the warning time

**(a)**

| $H$ (m) | $h_2$ (m) | $c$ (m s⁻¹) | $c$ (km h⁻¹) | $v$ (m s⁻¹) |
|---|---|---|---|---|
| 0.5 | 1.5 | 4.288 | 15.44 | 1.429 |
| 1.0 | 2.0 | 5.424 | 19.53 | 2.712 |
| 2.0 | 3.0 | 7.671 | 27.61 | 5.114 |
| 4.0 | 5.0 | 12.128 | 43.66 | 9.703 |

**(b)** For $H \gg h_1$, $h_2 \approx H$ and
$c \approx \sqrt{gH(H+h_1)/(2h_1)} \propto \sqrt{H}$: quadrupling the height
from 1 to 4 m multiplies the speed by $\sqrt4 = 2$ (5.424 to 12.128, ratio 2.24,
slightly above 2 because $H$ is not yet much greater than $h_1$).

**(c)** At $c = 7.671$ m s⁻¹, 200 m takes 26.1 s. The *flow* behind the front is
slower at 5.11 m s⁻¹, so water continues to arrive for a further 13 s after the
front has passed; the front itself is the timescale that matters.

**(d)** Because it sets the interval between the first visible sign and the
arrival of the damaging flow, and it is of order half a minute over 200 m. Any
warning that leaves people within a few hundred metres of the shoreline has to be
acted on before the wave is visible at all, which is why the operational timescale
is the *offshore* travel time rather than the run-up time.

---

## ★★7 — Detection

**(a)** 10.10 Pa for 0.1 cm, 101.01 Pa for 1 cm and 5050.42 Pa for 50 cm.

**(b)** $\eta = 10/(1030\times9.80665) = 9.90\times10^{-4}$ m $= 0.99$ mm. A
10 Pa resolution is a **1 mm** sea-surface resolution, which is why bottom
pressure is such an effective way to watch the ocean surface.

**(c)**

| $L$ | $kh$ at 4000 m | $1/\cosh(kh)$ |
|---|---|---|
| 250 m | 100.5 | $2.2\times10^{-44}$ |
| 1 km | 25.1 | $1.2\times10^{-11}$ |
| 25 km | 1.005 | 0.645 |
| 100 km | 0.251 | 0.969 |

The crossover is at $kh = 1$, i.e. $L = 2\pi h = 25.1$ km.

**(d)** The depth attenuation factor $1/\cosh(kh)$ is one formula, and its two
limits are opposite. A wind sea has $kh$ of order 100, so its pressure signal is
attenuated by tens of orders of magnitude and the sensor cannot see the waves
above it. A tsunami has $kh \approx 0.1$ to 1, so its signal reaches the bottom
almost unattenuated. The ocean is therefore transparent to one and opaque to the
other, and the distinction is set by the wavelength rather than by the amplitude
— which is why a 1 cm tsunami is detectable while a 10 m swell is not.

---

## ★★★8 — Travel time along a segmented path

**(a)** $c = 221.43$ m s⁻¹ at 5000 m, $171.52$ m s⁻¹ at 3000 m and
$99.03$ m s⁻¹ at 1000 m, giving 3.763 h, 6.478 h and 2.805 h, and a total of
**13.05 h** for 8000 km.

**(b)** A uniform 3500 m gives $c = 185.3$ m s⁻¹ and
$8000\times10^3/185.3 = 43\,172$ s $= 11.99$ h — **8.1 per cent shorter** than
the correct 13.05 h, which is a difference of an hour in a warning that matters
at the level of tens of minutes.

**(c)** The equivalent uniform depth is $d = (8000\times10^3/46\,967)^2/g
= (170.32)^2/9.80665 = 2958$ m, which is closer to the deepest segment (5000 m)
than to the arithmetic mean (3000 m). It is the *harmonic* mean of the depth in
the travel-time sense: the travel time is dominated by
$1/\sqrt h$, so the shallow segments weigh more and the equivalent depth is
pulled below the arithmetic mean.

**(d)** Two reasons: the real path is a great circle through a bathymetry that
varies continuously, so the integral must be discretised finely; and refraction
means the actual ray path bends towards shallow water, so the path is not the
straight great circle at all. The second changes the arrival time less than the
first in the deep ocean — refraction is weak where the depth gradients are gentle
— but it changes it substantially for a wave that crosses a ridge or a
continental slope.

---

## ★★★9 — What the ocean filters out

**(a)** For the sea surface to rise, water must be displaced horizontally: the
water is effectively incompressible, so a surface elevation requires a
convergence of horizontal flow. A bottom displacement of wavelength $L$ drives
flow whose vertical extent is limited to the depth $h$, and the resulting
horizontal velocity is $u \sim (h/L)\dot\eta_0$ — small when $L \gg h$. The
potential-flow solution of Laplace's equation with a moving bottom gives exactly
$\eta = \eta_0/\cosh(kh)$. The assumption is that the seafloor moves
**instantaneously** compared with the ocean's response time
$L/\sqrt{gh}$: if the rupture is slow, water has time to flow away laterally and
the surface response is suppressed even at long wavelengths, which is why a slow
"tsunami earthquake" can be deceptive in the other direction.

**(b)** At 10 km: 16.1 per cent. At 25 km: 64.5 per cent. At 100 km:
96.9 per cent.

**(c)** At 400 km and at 100 km both wavelengths are far above the crossover at
$2\pi h = 25$ km, so the transmitted fractions are $0.969$ and $0.969$: **the
filter does not discriminate between these two events at all**, and the ratio of
their initial sea-surface amplitudes is 1.0 before the source displacement is
considered. The filter becomes discriminating only when a rupture length
approaches or falls below about 25 km: a 20 km rupture transmits 52.7 per cent
against 96.9 per cent for 100 km, a factor of **1.84** in initial sea-surface
amplitude at equal seafloor displacement. For the case as posed, the interesting
consequence is the opposite of the intuitive one: for a **fixed moment**, the
100 km fault has four times the mean slip of the 400 km fault (if their widths
are equal), so its seafloor displacement is larger and its initial tsunami
amplitude is larger — not smaller. Tsunami size is set by the displacement and
the depth, and only for short ruptures by the filter.

**(d)** A magnitude in the first ten minutes constrains the *moment*, not the
geometry, and the geometry determines the seafloor displacement (through the
slip and the area) and whether the rupture is shallow and dip-slip rather than
mostly strike-slip (which displaces very little water). Its effect on the
Kajiura filter is decisive only for short ruptures, but its effect on the
displacement is decisive always. A magnitude-only warning therefore has a large
intrinsic spread in amplitude while being accurate in arrival time. The
practical response is to issue the warning on the magnitude and the travel time —
which are robust — and to refine the amplitude forecast as the rupture geometry,
the seafloor deformation and the sea-level observations arrive. Anything else
overstates what the first ten minutes can know.
