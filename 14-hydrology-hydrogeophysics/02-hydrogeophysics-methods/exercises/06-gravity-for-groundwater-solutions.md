# Solutions — 14-02-06 Microgravity and Satellite Gravity for Water Storage Change

> **Read after attempting the exercises.** Arithmetic is shown in full. Every
> network, storage figure and load is **SYNTHETIC**.

Lesson: [06 Microgravity and Satellite Gravity for Water Storage Change](../06-gravity-for-groundwater.md).

Constants: $G = 6.67430 \times 10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$,
$\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$, so
$$2\pi G \rho_w = 2\pi(6.67430 \times 10^{-11})(1000)
= 4.1936 \times 10^{-7}\ \mathrm{m\,s^{-2}\,m^{-1}}
= 41.94\ \mathrm{\mu Gal\ m^{-1}}.$$

---

## ★1 — One metre of water-table decline in an unconfined aquifer

**The mass that moves.** In an unconfined aquifer a 1 m decline releases only the
*drainable* water, i.e. a water column $S_y \Delta h$:
$$\text{water column} = 0.12 \times 1\ \mathrm{m} = 0.12\ \mathrm{m}
= \mathbf{120\ mm}.$$
$$\Delta m = \rho_w S_y \Delta h = 1000 \times 0.12 = 120\ \mathrm{kg\,m^{-2}}.$$

**The gravity change.**
$$\Delta g = 2\pi G \Delta m = (4.1936 \times 10^{-10})(120)
= 5.032 \times 10^{-8}\ \mathrm{m\,s^{-2}} = \mathbf{5.03\ \mu Gal}.$$

Equivalently $\Delta g = 41.94 \times 0.12 = 5.03$ µGal.

**Why not 41.94 µGal?** Because gravity responds to the *mass* removed, and an
unconfined water table that falls by 1 m removes 0.12 m of water per unit area, not
1 m; the 41.94 µGal value applies when a **1 m thickness of water** is added or
removed, which happens for a confined (artesian) head change, or for a fully
saturated body whose top rises through an impermeable boundary. Quoting 41.94 µGal
for a water-table change in an unconfined aquifer is the single most common error in
this calculation — it overstates the signal by $1/S_y$, a factor of 8.3 here.

---

## ★2 — Repeatability to storage

$$\text{water column} = \frac{5 \times 10^{-8}}{4.1936 \times 10^{-10}}
= 119.2\ \mathrm{kg\,m^{-2}} = \mathbf{119.2\ mm\ of\ water}.$$

**Water-table change.** Gravity fixes the *storage*, so the water-table change depends
on $S_y$:

| $S_y$ | meaning | water-table change |
|---|---|---|
| 0.12 | unconfined, draining | $119.2/0.12 = \mathbf{993\ mm \approx 1.0\ m}$ |
| 1.00 | confined head (no drainage) | $119.2\ \mathrm{mm} = \mathbf{0.119\ m}$ |

**Consequence.** At 5 µGal the instrument resolves about 119 mm of storage
everywhere, but in an unconfined aquifer with $S_y = 0.12$ that is a water-table
resolution of only **≈1 m**. The specific yield is therefore the dominant uncertainty
in the storage→level conversion, not the gravimeter: a 20% error in $S_y$ is a 20%
error in the level change, dwarfing the instrument error.

---

## ★3 — Equivalent water height from $\Delta C_{20}$

$$\mathrm{EWH} = 1.8713 \times 10^{8}\ \mathrm{m} \times \Delta C_{20}
= 1.8713 \times 10^{8} \times 2 \times 10^{-10}\ \mathrm{m}
= 3.743 \times 10^{-2}\ \mathrm{m} = \mathbf{37.4\ mm}.$$

(Consistency check against the lesson's table: $1 \times 10^{-10}$ gives 18.713 mm,
so $2 \times 10^{-10}$ gives 37.43 mm ✓.)

**Mass change over 200 000 km².**
$$A = 200\,000\ \mathrm{km^2} = 2.0 \times 10^{11}\ \mathrm{m^2},$$
$$\Delta M = \rho_w \times \mathrm{EWH} \times A
= 1000 \times 0.03743 \times 2.0 \times 10^{11}
= 7.486 \times 10^{12}\ \mathrm{kg} = \mathbf{7.49\ km^3\ of\ water}.$$

(Volume check: $0.03743\ \mathrm{m} \times 2 \times 10^{11}\ \mathrm{m^2} =
7.49 \times 10^{9}\ \mathrm{m^3} = 7.49$ km³ ✓.)

**Scale sense.** 7.5 km³ of storage change is a measurable, decision-relevant volume;
note that it comes from a coefficient of only $2 \times 10^{-10}$, which is why the
gravity field must be known to that precision and why degree-1 (geocentre) terms must
be removed before any of it is interpreted.

---

## ★★4 — Levelling error

**Free-air gradient.**
$$\frac{2g}{a} = \frac{2(9.81)}{6.371 \times 10^{6}} = 3.0796 \times 10^{-6}\ \mathrm{s^{-2}}
= 307.96\ \mathrm{\mu Gal\,m^{-1}} = 3.080\ \mathrm{\mu Gal\,cm^{-1}}.$$

**1 cm of height error.**
$$1\ \mathrm{cm} \times 3.080\ \mathrm{\mu Gal\,cm^{-1}} = \mathbf{3.08 \approx 3.1\ \mu Gal}.$$

**As a fraction of the signal in ★1** ($5.03$ µGal):
$$\frac{3.08}{5.03} = \mathbf{61\%}.$$

**Height control for a 10% error budget.**
$$0.10 \times 5.03 = 0.503\ \mathrm{\mu Gal}
\Longrightarrow
h = \frac{0.503}{307.96}\ \mathrm{m} = 1.63 \times 10^{-3}\ \mathrm{m}
= \mathbf{1.6\ mm}.$$

**Interpretation.** Centimetre levelling is *not* enough: for this signal the network
must be tied to a few millimetres, which in practice means (i) a common benchmark
network re-levelled each survey, (ii) GPS/GNSS heights with long occupations and
modelled troposphere, and (iii) **relative** gravity measured pillar-to-pillar so
that the free-air term cancels between occupations wherever the pillar heights are
unchanged. A survey that moves its pillars, or re-occupies with fresh levelling each
round, injects an error larger than the storage signal it is trying to measure.

---

## ★★5 — The water-level versus saturation ambiguity

**(i) Water-table decline from the observed storage loss.** The gravity change fixes
the *mass*,
$$\Delta m = \frac{2.20 \times 10^{-8}}{4.1936 \times 10^{-10}}
= 52.5\ \mathrm{kg\,m^{-2}} = 52.5\ \mathrm{mm\ of\ water},$$
$$\Delta g = (4.1936 \times 10^{-10})(52.5) = 2.202 \times 10^{-8}
= \mathbf{2.20\ \mu Gal}\ \text{(as given)},$$
$$\Delta h = \frac{\Delta m}{\rho_w S_y} = \frac{52.5\ \mathrm{kg\,m^{-2}}}
{1000 \times 0.12} = \mathbf{0.44\ m}.$$

**(ii) The same signal from a saturation change.** A saturation decrease of 0.05
over 3 m at $\phi = 0.35$ removes a water column
$$\Delta \theta \, b = (0.05 \times 0.35) \times 3.0 = 0.0175 \times 3.0
= 0.0525\ \mathrm{m} = 52.5\ \mathrm{mm},$$
i.e. exactly the same 52.5 kg m$^{-2}$, so
$$52.5\ \mathrm{mm} \times 4.1936 \times 10^{-10}
= 2.20\ \mathrm{\mu Gal}\ \text{by construction},$$
and it **mimics a water-table decline of 0.4375 ≈ 0.44 m** under interpretation (i).

**(iii) Comment.** Gravity alone cannot distinguish the two: it measures the mass
deficit per unit area, and a 0.44 m water-table decline and a 0.05 saturation
decrease over 3 m are degenerate to machine precision. The degeneracy is broken by:
- a **direct water-level measurement** (a piezometer, or a pressure transducer) in
  the same footprint, and
- **soil-moisture or ERT/GPR monitoring** of the unsaturated zone, which measures the
  saturation term directly.

Two further discriminants are worth naming: **time structure** — water-table drainage
continues for days to months after rain, whereas a wetting-front saturation change is
transient and tied to rainfall — and the **water balance** (recharge versus
abstraction), which fixes the expected sign and magnitude. Microgravity should
therefore be deployed as one observable in a combined monitoring programme, never as a
stand-alone storage gauge in a dual-mechanism setting.

---

## ★★6 — Degree truncation and leakage

Missing fraction $= 100\% -$ captured:

| disk radius | $l_{\max} = 10$ | 20 | 40 |
|---|---|---|---|
| 2.0° (≈222 km) | $100 - 19.5 = \mathbf{80.5\%}$ | $100 - 39.8 = \mathbf{60.2\%}$ | $100 - 72.1 = \mathbf{27.9\%}$ |
| 10.0° (≈1112 km) | $100 - 81.6 = \mathbf{18.4\%}$ | $100 - 97.1 = \mathbf{2.9\%}$ | $100 - 99.2 = \mathbf{0.8\%}$ |

**Worst affected: the small (2°) disk at $l_{\max} = 10$**, with 80.5% of its
degree-variance above the truncation — the truncated model simply cannot represent the
load. The truncation loss falls monotonically with both increasing radius and
increasing $l_{\max}$: a load whose spatial extent is huge compared with the
wavelength of degree 10 ($\approx$ 40 000/10 km) is already well described by low
degrees.

**Why it appears as leakage rather than as a small error at the basin centre.** The
missing high-degree power is not *lost*; the inversion redistributes it. A regional
solution that fits the observed low-degree field with a basis of smooth (truncated)
functions must place mass somewhere, and the only place it can put the missing
signal is in the surrounding cells: the basin's own mass is smeared outwards
(leakage out) while mass from the neighbouring region is smeared inwards (leakage
in), so the *centre* of the basin can appear almost correct while the edges are badly
wrong and the total is biased by whatever the surroundings are doing. That is why a
basin-scale mass balance must state the filter, the truncation degree, the
regularisation and the **leakage correction** — and why two published products with
different truncations can give opposite signs for the same basin's annual change.

---

## ★★★7 — Network design for a 0.25 m annual change

**The signal.**
$$\Delta m = \rho_w S_y \Delta h = 1000 \times 0.12 \times 0.25
= 30\ \mathrm{kg\,m^{-2}}\ (= 30\ \mathrm{mm\ of\ water}),$$
$$\Delta g = (4.1936 \times 10^{-10})(30)
= 1.258 \times 10^{-8}\ \mathrm{m\,s^{-2}} = \mathbf{1.258\ \mu Gal}.$$

**Required repeatability at 2σ.**
$$2\sigma \le 1.258\ \mathrm{\mu Gal}
\Longrightarrow
\sigma \le \mathbf{0.629\ \mu Gal}.$$

**Repeat occupations** from $\sigma_0 = 5$ µGal with noise falling as
$1/\sqrt{N}$ (i.e. $N = (\sigma_0/\sigma)^{2}$):
$$N = \left(\frac{5}{0.629}\right)^{2} = 63.2 \ \longrightarrow\ \mathbf{64\ occupations}.$$

**Is it achievable?** Not as a routine annual survey. Sixty-four full occupations of
a 4 km × 4 km network is *more than one occupation per week per year*, and the
assumption that the noise averages as $1/\sqrt{N}$ fails over such a period: the
"noise" that dominates is not white instrument noise but **drift, tidal model error
and hydrology-driven soil-moisture change**, all of which are correlated over weeks
and will not average down. In practice the correlated terms set a floor near
1–3 µGal (see the lesson's correction budget), so the requirement is out of reach for
this instrument and this signal.

**What I would change**, in order of leverage:

1. **Change what is measured.** A co-located piezometer resolves 0.25 m of
   water-table change to millimetres at a fraction of the cost — microgravity is only
   worth its effort where the *mass* change is the target (storage in an
   inaccessible or heterogeneous medium) or where saturation and level changes must
   be separated together.
2. **Use the free-air lever instead of the gravimeter.** If the water table is
   accessible, measure **level** directly and convert to mass with a measured $S_y$:
   the free-air gradient of 3.080 µGal cm$^{-1}$ means a centimetre of *height* is
   worth more gravity signal than the storage change being sought, so precise
   levelling plus a level record beats precision gravimetry here.
3. **Shorten the time base or enlarge the signal.** Detect the signal where it is
   bigger: a decadal change, a confined (artesian) head change where
   $S_y \to S_s b \approx$ the full column, or an area with larger storage
   variability. Sensitivity scales with the signal, not with the instrument alone.
4. **Choose satellite gravimetry** if the requirement can be relaxed to basin scale:
   from §5 of the lesson, 20 mm of EWH over 200 000 km² is 4 km³, comfortably within
   the range of time-variable gravity products — but with the leakage caveat of ★★6
   and at resolutions of hundreds of kilometres, so it cannot substitute for a
   4 km network.

**Transfer error.** If each occupation is tied to a distant absolute reference and
the transfer introduces a 2 µGal relative error, that alone is 3.2× the required
0.629 µGal: **the transfer, not the meter, would dominate.** Every occupation must
therefore share the same pillars, use the same reference station, and be levelled to
a common datum whose stability is itself monitored (e.g. by a continuously recording
gravimeter or by repeated absolute measurements at one pillar).

---

## ★★★8 — Verification versus validation

**(a) Disk integral → Bouguer slab** (37.7631 µGal at $R = 1$ km, 41.5165 at 10 km,
41.8939 at 100 km, 41.9317 at 1000 km, 41.9358 at 100 000 km, against the analytic
slab 41.9359 µGal). *Verifies:* that the numerical surface integral is implemented
with the right factors of $2\pi G$, depth and area — an error there would make the
limit wrong on every horizon. *Does not verify:* that the slab formula is the right
*physical* model for a real water-table change (it is only an approximation valid
where the layer is thin compared with its lateral extent and the observation is close
to it).

**(b) Exact linearity** in $\Delta C_{20}$ (ratio 2.000000) and in $(1 + k_l)$ (ratio
2.000000 for $0.7$ against $1.4$; the intermediate $0.85/0.70$ gives 1.214286).
*Verifies:* that the implementation is linear where it must be and that no term is
hidden inside a quantity that should be independent — a normalisation error or an
accidental dependence on the coefficient value would break the ratio.
*Does not verify:* the value of $k_2$, the convention of the normalised Legendre
function, or the reference radius; a wrong $k_2$ passes (b) perfectly.

**(c) Structure of the general-degree formula** ($l = 2$ gives 1.8713 mm, $l = 4$
gives 4.5191 mm, ratio 2.4150). *Verifies:* the combination
$(2l+1)/[(1+k_l)\bar P_{l0}(1)]$ behaves as the theory requires, i.e. that the
code is a *general* degree-$\ell$ implementation and not a hard-wired degree-2
special case; the expected ratio is $(9 \times 3)/(5 \times \sqrt{5}) = 2.41495$.
*Does not verify:* any physics of the loading response, since $k_4 = k_2$ was
assumed for the illustration.

**What none of the three can verify.** They are all self-consistency checks of one
piece of code against its own algebra. No combination of them can establish that the
model represents a real water reservoir — the **non-uniqueness** is physical, not
numerical: a given low-degree gravity change is reproduced by an infinite family of
(saturation, level-gauge, $S_y$) combinations, as ★★5 shows to machine precision. A
verification suite can make the family *well computed*; it cannot make it *unique*.
(This is the standard distinction: **verification** asks "am I solving the equations
right?", **validation** asks "are these the right equations?")

**A validation.** Borehole-constrained forward modelling: take the *measured*
water-level records from piezometers inside the network and the *measured* $S_y$ from
pumping tests or cores, predict the expected gravity change at each pillar from
$\Delta g = 2\pi G \rho_w S_y \Delta h$, and compare with the observed microgravity
difference including its stated error bar. This would catch what (a)–(c) cannot:
- a **wrong physical coefficient** in the survey reduction (e.g. a scale-factor or
  calibration error in the gravimeter, or a wrongly applied tide/Earth-tide factor),
  which would make every station wrong by a constant multiple;
- a **systematic offset** between the modelled and real store, i.e. storage change
  living somewhere the network's footprint does not see (leakage at the network
  boundary, or an unsaturated-zone term the piezometer does not record) — exactly the
  degeneracy of ★★5;
- a **$S_y$ error**, since the comparison is sensitive to the ratio of gravity change
  to water-level change, and it fixes $S_y$ *in situ* (the best available
  calibration of the storage↔level conversion).

It still would not prove the interpretation generalises to a neighbouring basin — that
requires repeating the validation there, which is the honest, unglamorous conclusion
of gravity-based hydrology.

---

## Module mastery checkpoint, part (c)

A 0.25 m water-table decline in an unconfined aquifer with $S_y = 0.12$ releases
$$\Delta m = \rho_w S_y \Delta h = 1000 \times 0.12 \times 0.25
= 30\ \mathrm{kg\,m^{-2}}\ (= 30\ \mathrm{mm\ of\ water}),$$
$$\Delta g = 2\pi G \Delta m = (4.1936 \times 10^{-10})(30)
= 1.258 \times 10^{-8}\ \mathrm{m\,s^{-2}} = \mathbf{1.258\ \mu Gal}.$$

**Levelling error for 10% of that signal.** The budget is
$0.10 \times 1.258 = 0.126\ \mathrm{\mu Gal}$, and the free-air gradient is
$307.96\ \mathrm{\mu Gal\,m^{-1}} = 3.080\ \mathrm{\mu Gal\,cm^{-1}}$, so
$$h = \frac{0.126}{3.080} = 0.041\ \mathrm{cm} = \mathbf{0.41\ mm}.$$

**Interpretation.** A tenth of the annual storage signal is destroyed by **less than
half a millimetre** of height change — a frost heave, a settling pillar, or the
difference between two levelling campaigns. The only workable strategy is to keep the
pillars fixed and re-occupy them (so the free-air term cancels between occupations)
rather than to re-level absolutely each round; a network that cannot guarantee repeat
occupation to this tolerance cannot measure this signal, whatever the gravimeter's
specification.
