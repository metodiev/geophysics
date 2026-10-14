# Solutions — 14-06-02 Groundwater-Surface Water Interaction

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Groundwater-Surface Water Interaction](../02-groundwater-surface-water.md).

---

## ★1 — Darcy flux and seepage velocity

$$q_z = \frac{K\Delta h}{L} = \frac{2.5 \times 0.060}{8.0}
= 0.01875\ \mathrm{m\,d^{-1}},$$

positive downward because the stream head is above the aquifer head: a **losing**
reach. The seepage velocity is
$v = q_z/n_e = 0.01875/0.25 = 0.075\ \mathrm{m\,d^{-1}}$. Per metre of stream
width, the loss is $0.01875\ \mathrm{m^3\,d^{-1}}$ for every metre of reach, or
$18.75\ \mathrm{m^3\,d^{-1}}$ over a 1000 m reach absent any other exchange.

---

## ★2 — Skin depth at two periods

$$d = \sqrt{\frac{2\kappa}{\omega}} = \sqrt{\frac{2\kappa T}{2\pi}}.$$

- Diurnal, $T = 86400$ s: $d = \sqrt{2\times10^{-6} \times 86400/(2\pi)}
  = \sqrt{0.027503} = 0.16584\ \mathrm{m}$.
- Semidiurnal, $T = 44640$ s: $d = \sqrt{2\times10^{-6} \times 44640/(2\pi)}
  = \sqrt{0.014209} = 0.11920\ \mathrm{m}$.

The higher frequency penetrates only $1/\sqrt{2}$ as deep — the reason probe
spacings must be chosen for the *frequency* being used, not for the material
alone.

---

## ★3 — Dilution gauging

$$Q = \frac{M}{\int\Delta C\,\mathrm{d}t} = \frac{2.00}{23641.18}
= 8.460\times10^{-5}\ \mathrm{m^3\,s^{-1}} = 0.0846\ \mathrm{L\,s^{-1}}.$$

With the longer window, $\int = 24889.25$:

$$Q = \frac{2.00}{24889.25} = 8.036\times10^{-5}\ \mathrm{m^3\,s^{-1}}
= 0.0804\ \mathrm{L\,s^{-1}},$$

so the truncated-window value is $+5.28\%$ high. The *injected mass* is exact in
both cases; only the integral differs.

---

## ★4 — A consistent pair of temperature readings

Using the analytic relations with $\kappa = 1.0\times10^{-6}\ \mathrm{m^2\,s^{-1}}$
and $\omega = 7.2717\times10^{-5}\ \mathrm{s^{-1}}$ over a 0.15 m separation:

- Amplitude ratio $0.7000$: the homogeneous inversion returns
  $v = +0.7897\ \mathrm{m\,d^{-1}}$ (the ratio is monotone in $v$, so the solution
  is unique).
- Phase lag $3.00\ \mathrm{h} = 0.78540$ rad: the inversion returns
  $v = \pm0.7883\ \mathrm{m\,d^{-1}}$ (the phase is even in $v$).

The two magnitudes agree to $0.2\%$ — much better than any field measurement
reproduces — and the amplitude resolves the sign, so the defensible statement is
**$v = +0.79\ \mathrm{m\,d^{-1}}$ downward: a losing reach**. This is the
textbook-consistent case, and it is worth contrasting with ★5.

---

## ★5 — An inconsistent pair, and what to do

With the silt layer present the readings are a ratio of 0.1918 and a lag of
3.9893 h.

- The largest lag any homogeneous bed can produce at a 0.15 m separation is
  **3.4549 h**, attained at $v = 0$ (the phase is maximal for pure conduction).
  A lag of 3.9893 h is **outside the range of the homogeneous model entirely**:
  no velocity can produce it, so the model is rejected by the data and no
  velocity should be quoted from it.
- The amplitude ratio 0.1918 admits a homogeneous solution in the demonstration's
  scan of $v = -0.7268\ \mathrm{m\,d^{-1}}$ — the right sign, and $82\%$ wrong in
  magnitude relative to the true $-0.40\ \mathrm{m\,d^{-1}}$.

**What to do next.** (i) Report the inconsistency rather than one of the two
numbers; it is the strongest statement the data support. (ii) Measure the
layering: a thermal-conductivity profile (a needle probe on a core, or a
temperature-with-depth log under a known gradient) is enough to build a layered
forward model. (iii) Re-invert with the layering included, and re-check that the
amplitude and the phase now agree. (iv) If the layering cannot be measured,
shorten the probe separation until both probes lie within one layer, and accept
the loss of signal that implies.

---

## ★6 — Upstream–downstream differencing

Gain in discharge: $30.07 - 30.00 = 0.07\ \mathrm{L\,s^{-1}}
= 7.0\times10^{-5}\ \mathrm{m^3\,s^{-1}} = 6.048\ \mathrm{m^3\,d^{-1}}$.

Over a 100 m reach of 2 m width, the bed area is $200\ \mathrm{m^2}$, so

$$q_z = \frac{6.048}{200} = 0.03024\ \mathrm{m\,d^{-1}},
\qquad v = \frac{0.03024}{0.25} = 0.1210\ \mathrm{m\,d^{-1}}.$$

The fractional difference between the two gaugings is
$0.07/30.00 = 0.233\%$. **The measurement is not defensible**: dilution gauging
is good to a few per cent on a single gauging (the lesson's window truncation
alone gave 5.3%), so a 0.233% difference is far inside the noise of two
independent gaugings — and the errors are largely *independent*, so they add
rather than cancel.

**What to use instead:** the diurnal temperature method (a signal of order 1 K
with a well-defined phase, and the flux is inferred from a *ratio*, not a
difference), or nested mini-piezometers for a head difference, or a seepage
meter at the bed. If dilution gauging is the only option, the reach must be long
enough that the gain is several per cent of the discharge — which for
$q_z \approx 0.03\ \mathrm{m\,d^{-1}}$ means several kilometres, not 100 m.

---

## ★7 — A temperature array for $0.1\ \mathrm{m\,d^{-1}}$ at $\pm30\%$
(specification)

**Target.** $\sigma_v \le 0.03\ \mathrm{m\,d^{-1}}$ at $v = 0.10$.

**Sensitivity.** The amplitude ratio is the monotone observable. From the
lesson's table, $r(0.10) = 0.4406$ and $r(0.40) = 0.5537$, so
$\mathrm{d}r/\mathrm{d}v \approx (0.5537-0.4406)/0.30 = 0.377$ per m d⁻¹ in this
range. The target $\sigma_v = 0.03$ therefore requires a ratio precision of
$0.03 \times 0.377 = 0.011$, i.e. **about 1% on the amplitude ratio**. That is
the hard requirement, and it is dominated by the accuracy of the *surface*
(water–bed interface) amplitude, which must be measured at the same place and
time as the subsurface probes.

**Why the amplitude and not the phase.** The phase changes from 3.4542 h at
$v = 0$ to 3.4462 h at $v = 0.10$ — a difference of **28.8 s**, far below any
attainable phase resolution. The phase is even in $v$ and flat near $v = 0$, so
at this target velocity it carries essentially no information; the amplitude is
the only usable observable.

**Probe depths.** Two depths at a separation near the skin depth, for example
0.10 m and 0.25 m ($= 0.6d$ and $1.5d$): close enough that the deeper probe still
carries an unambiguous diurnal signal (amplitude of order $A\mathrm{e}^{-1.5}$),
far enough that the ratio is not near 1.

**Sampling and record length.** Sample at 10-minute intervals for at least 14
days. A harmonic fit at the diurnal frequency on a 14-day record has a phase
standard error of about $\sigma_{\text{noise}}/(A\sqrt{N})$ with $N = 14$ cycles,
and — more importantly — averaging over 14 cycles is what stabilises the
*amplitude* ratio, which is the observable that matters (see above). The record
length also averages out the weather-driven variation of the surface amplitude.

**Separating the diffusivity error from the velocity.** A $\pm20\%$ error in
$\kappa$ moves the inferred $v$ by a comparable amount — the two are not
separately identifiable from one pair of probes. Two options: (i) measure
$\kappa$ directly (a divided-bar or needle-probe measurement on a core, plus
water content, gives $5$–$10\%$), which is the recommended route; or (ii) use
three probes at 0.10, 0.20 and 0.40 m: the *ratio of ratios*
$[A(0.40)/A(0.20)]/[A(0.20)/A(0.10)]$ is much less sensitive to $\kappa$ than
either ratio alone, at the cost of a weaker signal at 0.40 m.

---

## ★8 — Certifying the sign at thirty reaches (model answer)

**Method.** A **streambed temperature profile** from a hand-pushed probe rod with
two or three thermistors (0.10, 0.20, 0.40 m), measured repeatedly over a
diurnal cycle, plus the stream temperature at the bed. The two depths allow both
the amplitude ratio and the phase lag to be formed; the *sign* is carried by the
amplitude, which is asymmetric in $v$ (Section 2 of the lesson), and the
*magnitude* is then optional.

**Why it is the cheapest thing that works.** It needs no borehole and no
installation; a rod, a logger and 20 minutes per reach over a full day. The
measurement is a *ratio* of amplitudes, which cancels the sensor calibration, and
its asymmetry is the one observable that is not symmetric in the flow direction.

**Failure modes.** (i) A short field day may not span the diurnal cycle, and the
amplitude cannot be formed from a partial cycle unless a harmonic fit on a site
with a strong single-frequency signal is used; (ii) shading, tributary inflows
and a variable bed conductance distort the surface amplitude; (iii) a coarse
gravel bed with high flow can be advection-dominated, in which case the profile
is nearly uniform in temperature and the ratio is near 1 — the *phase* then
carries the information but not the sign; (iv) a reach with a seepage face above
water is outside the model.

**Expected yield.** On a mixed river, expect about **60–80%** of the reaches to
yield a sign at better than 2 sd, with the failures concentrated on cobble beds
and in the shaded, slow reaches. The deliverable should be a map with three
classes — gaining, losing, undetermined — rather than a binary map, and the
undetermined fraction is itself a useful result: it tells the regulator where the
method must be replaced by a seepage meter or a mini-piezometer.
