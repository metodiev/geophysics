# Solutions — 04-07-04 Subsidence, Sinkholes and Karst

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Effective stress and compaction

**(a)** $\Delta\sigma' = \rho_w g\Delta h = 1000\times9.80665\times8
= 7.85\times10^4$ Pa $= 78.5$ kPa.

**(b)** $\Delta H = m_v\Delta\sigma'H_0
= 0.4\ \mathrm{m^2\,MN^{-1}} \times 0.07848\ \mathrm{MN\,m^{-2}} \times 25$ m
$= 0.785$ m. Note the unit bookkeeping: $m_v$ is quoted per MN, so the stress
must be converted, and that conversion is where most $10^3$ errors occur.

**(c)** One-dimensional consolidation (zero lateral strain) and a constant $m_v$
over the stress increment. The first is the oedometer condition, which is a good
approximation under a wide load; the second is an approximation because $m_v$
depends on the stress level and on the history.

**(d)** No. For a normally consolidated clay the loading and unloading paths are
different curves and most of the volume change is plastic. Recharging restores
the pressure and the effective stress, not the elevation — which is why
subsidence is called a permanent loss of aquifer storage.

---

## ★2 — Gravity gradients

**(a)** $g = GM/r^2$ gives $\mathrm{d}g/\mathrm{d}z = -2GM/r^3 = -2g/R
= -3.0785\times10^{-6}$ (m s⁻²) per m, i.e. **0.30785 mGal m⁻¹** and
**3.0785 µGal cm⁻¹**.

**(b)** $2\pi G\rho = 2\pi\times6.6743\times10^{-11}\times2670
= 1.1197\times10^{-6}$ s⁻² $= 0.11197$ mGal m⁻¹.

**(c)** $0.30785 - 0.11197 = 0.19588$ mGal m⁻¹.

**(d)** The residual gradient of 0.1959 mGal m⁻¹, in uniform rock. A departure
means the density between the two measurement stations differs from the assumed
2670 kg m⁻³, and since the station separation is known, the departure can be
inverted for the density of the intervening rock. That is the whole content of
borehole gravimetry: it measures density at depth, in situ, over a longer
baseline than a gamma–gamma log.

---

## ★3 — Karst denudation

**(a)** $D = cP/\rho = (0.080\ \mathrm{kg\,m^{-3}})(0.6\ \mathrm{m\,a^{-1}})
/(2700\ \mathrm{kg\,m^{-3}}) = 1.78\times10^{-5}$ m a⁻¹ $= 17.8$ mm ka⁻¹.

**(b)** $t = 20/1.78\times10^{-5} = 1.13\times10^6$ a $= 1125$ ka.

**(c)** The concentration. Recharge can be estimated from a water balance over a
catchment and the rock density is measured on a hand specimen, but the dissolved
load varies with season, with flow path and with the extent of mixing between
soil-derived and deep-sourced water. A single sample from one spring is
not the catchment average, and the difference is easily a factor of two.

**(d)** The *void inventory*: where cavities exist and how thick their roofs
are. That is what determines whether a collapse happens in a particular place,
and it is exactly what (8) cannot deliver.

---

## ★4 — The compression-index form

**(a)** $\Delta H = \dfrac{C_c}{1+e_0}H_0\log_{10}
\dfrac{\sigma'_0+\Delta\sigma'}{\sigma'_0}
= \dfrac{0.35}{1.9}\times20\times\log_{10}\dfrac{180}{120}
= 3.684\times0.17609 = 0.649$ m.

**(b)** Normally consolidated means the clay is currently on the virgin
compression curve: the largest stress it has ever carried is the one it carries
now. If it were over-consolidated — for example if a former ice sheet had loaded
it and then melted away — the first part of the stress increase would follow a
reloading curve with a slope $C_r$ typically five to ten times smaller, and only
after the pre-consolidation stress was exceeded would (3) apply. The same
drawdown therefore produces a much smaller settlement in an over-consolidated
clay.

**(c)** Because $m_v$ falls as the stress rises, so a single value fitted at one
stress level overestimates the response at higher stress and underestimates it
at lower. The logarithmic form contains the stress level explicitly, and it is
the same reason the void ratio is plotted against $\log\sigma'$ rather than
against $\sigma'$ in a consolidation test.

---

## ★★5 — Running the compaction section

**(a)** With $\Delta\sigma' = 49.03$ kPa and $H = 30$ m: $m_v = 0.10$ gives
0.1471 m (147 mm), $m_v = 0.50$ gives 0.7355 m (736 mm) and $m_v = 1.50$ gives
2.2065 m (2207 mm).

**(b)** With $C_c = 0.3$, $e_0 = 1.0$ and the same 49.03 kPa increment:
$\sigma'_0 = 50$ kPa gives 1.3356 m, 100 kPa gives 0.7798 m and 200 kPa gives
0.4285 m.

**(c)** $m_v = \Delta H/(\Delta\sigma' H_0)
= 1.0/(0.049033\times30) = 0.68$ m² MN⁻¹ — squarely inside the quoted range for
a soft clay, which is the point: the answer is not determined by the physics but
by which clay this is.

**(d)** A seismic reflection section can map the *top and base of the
compressible layer* and its lateral continuity, and a velocity analysis gives an
estimate of its stiffness-related velocity — so it can tell you where the
calculation applies and how thick the layer is everywhere, which is exactly what
a borehole cannot. It cannot give $m_v$ or the pre-consolidation stress, because
those are strain properties measured in a laboratory, not elastic properties
measured by a wave.

---

## ★★6 — The residual gravity and its sensitivity

**(a)** Mass term $-62.904$ µGal; free-air term $+1539.264$ µGal; sum
$1476.360$ µGal.

**(b)** For $\phi = 0.15$: $\Delta\rho = -150$ kg m⁻³, so the mass term is
$-31.45$ µGal and the sum is $1507.81$ µGal. For $\phi = 0.45$: $\Delta\rho =
-450$ kg m⁻³, mass term $-94.36$ µGal, sum $1444.91$ µGal.

**(c)** The ratio is
$\dfrac{2g/R}{2\pi G\phi\rho_w} = \dfrac{3.0785\times10^{-6}}
{2\pi(6.6743\times10^{-11})(0.3)(1000)} = 24.5$.
Neither the layer's depth nor the fluid's identity appears: the free-air term
depends only on the geometry of the elevation change and the mass term only on
the mass removed per unit volume of lowering. That is why the *gradient* of
$\Delta g$ against $\Delta h$ is the diagnostic quantity and why the depth of the
compacting layer must come from somewhere else.

**(d)** $\Delta h_\mathrm{min} = 5\times10^{-8}/(2\pi G\phi\rho_w)
= 5\times10^{-8}/(1.2576\times10^{-7}) = 0.397$ m, i.e. about **0.4 m** of
water-level decline. A monitoring programme that resolves 0.4 m of head change
is useful; one that cannot resolve a metre is an inventory tool only.

---

## ★★7 — InSAR sensitivity and geometry

**(a)** $1$ cm gives $\Delta\phi = 4\pi(0.01)/0.0556 = 2.260$ rad
$= 0.360$ fringes. One fringe ($2\pi$) is $\lambda/2 = 2.78$ cm of line-of-sight
motion.

**(b)** $\cos 39^\circ = 0.7771$, so one fringe needs
$u_z = 2.78/0.7771 = 3.58$ cm of vertical motion.

**(c)** With (13):
$u_z\cos\theta = (2.0 + (-1.0))/2 = 0.50$ cm, so $u_z = 0.50/0.7771
= 0.64$ cm; and $u_h\sin\theta = (2.0-(-1.0))/2 = 1.50$ cm, so
$u_h = 1.50/0.6293 = 2.38$ cm.

**(d)** A single track would have reported the line-of-sight value converted at
$\cos\theta$, i.e. $2.0/0.7771 = 2.57$ cm of "vertical" motion for the ascending
track — four times the true vertical displacement of 0.64 cm, and it would have
attributed to vertical motion a horizontal displacement that is larger than
either. The geometry, not the precision, is the error.

---

## ★★★8 — Cavity stability and cavity detection

**(a)** $D_c = \sqrt{4\sigma_tt/(3\rho g)}
= \sqrt{4(20\times10^3)(3)/(3\times1800\times9.807)} = \sqrt{4.532} = 2.13$ m.
Doubling the roof thickness to 6 m multiplies $D_c$ by $\sqrt2 = 1.414$, to
3.01 m: a 100 per cent increase in thickness buys 41 per cent in span, because
the weight of the roof also doubles and the two effects partly cancel.

**(b)** $V = \tfrac43\pi(1.5)^3 = 14.14$ m³, so the missing mass is
$1800\times14.14 = 2.54\times10^4$ kg and
$\Delta g = G M/d^2 = 6.6743\times10^{-11}\times2.545\times10^4/9
= 1.887\times10^{-7}$ m s⁻² $= 18.9$ µGal.

**(c)** For $D = 1$ m: $V = 0.524$ m³, $M = 942$ kg, and
$\Delta g = 6.99\times10^{-9}$ m s⁻² $= 0.70$ µGal. Against a 5 µGal
repeatability, the 3 m cavity is a 3.8σ signal and the 1 m cavity is invisible.

**(d)** Microgravity can find cavities of a few metres diameter at a few metres
depth in a good survey, and cannot find metre-scale cavities at the same depth
whatever the survey is worth — the signal falls as $D^3$ and as $1/d^2$, so a
factor of 3 in size is a factor of 27 in signal. The method to add is **GPR**
(or, in a clay-rich soil where GPR fails, resistivity), because it responds to
the *roof* and the *void boundary* rather than to the mass deficit: a thin roof
over a cavity is a strong dielectric contrast and a weak mass anomaly, so the two
methods fail in opposite circumstances and are complementary. Neither predicts
when a collapse happens.

---

## ★★★9 — Elevation control for a gravity survey

**(a)** $3.0785$ µGal cm⁻¹, so a 1 cm elevation error is **3.08 µGal** of
apparent gravity change — more than half the 5 µGal repeatability of a good
survey.

**(b)** To keep the elevation-induced error below 5 µGal the elevation must be
known to $5/3.0785 = 1.6$ cm, and to keep it below half of that (so that the
elevation error does not dominate) to about 0.8 cm. This is why a 4-D
microgravity programme is always run with levelling or GNSS on the same
benchmarks, and why the elevation measurement is usually the more demanding of
the two.

**(c)** For $\phi = 0.30$, the mass term per metre of decline is
$2\pi G(0.3)(1000) = 1.258\times10^{-7}$ m s⁻² $= 12.58$ µGal. So 1 m of decline
gives 12.6 µGal of mass signal against 3.1 µGal of elevation-induced error per
centimetre of levelling error: the signal is measurable, but only with
centimetre-class elevation control.

**(d)** Because the free-air term from the elevation change is 24 times larger
than the mass term it is supposed to measure, a gravity time series with no
elevation information is dominated by a quantity that has nothing to do with
mass: the benchmark's height. The free-air correction converts a
height measurement into a gravity correction, so without an independent
elevation the two effects are inseparable and the mass change is
unidentifiable — the two hypotheses ("the ground went down but no mass left" and
"mass left but the ground did not move") predict different gravity changes but
the same *total* only if the elevation is known. An independent elevation from
levelling, GNSS or InSAR supplies the missing equation, which is why the
monitoring programme is a joint one.
