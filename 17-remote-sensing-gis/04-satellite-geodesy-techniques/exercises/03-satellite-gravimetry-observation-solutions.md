# Solutions — 17-04-03 Satellite Gravimetry as an Observation System

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [03 Satellite Gravimetry](../03-satellite-gravimetry-observation.md).

---

## ★1 — Orbit at 300 km

$$r = R_E + 300\ \mathrm{km} = 6671\ \mathrm{km},\qquad
v = \sqrt{\frac{GM}{r}} = \sqrt{\frac{3.986\,004\,418\times10^{14}}{6.671\times10^{6}}}
= \sqrt{5.9752\times10^{7}} = 7730.0\ \mathrm{m\,s^{-1}}.$$

$$T = 2\pi\sqrt{\frac{r^{3}}{GM}} = 2\pi\sqrt{\frac{2.9692\times10^{20}}{3.986\times10^{14}}}
= 2\pi\sqrt{7.4491\times10^{5}} = 2\pi\times863.0 = 5422.8\ \mathrm{s},$$

i.e. $5422.8/86400 = 0.06276$ days.

*Check:* the period must lie between the 250 km value (5361.6 s) and the 400 km
value (5544.9 s) from the lesson table — it does.

---

## ★2 — Attenuation and the suitable depths

$$\frac{g(h)}{g(0)} = \left(\frac{d}{d+250}\right)^{2}$$

| $d$ | ratio | interpretation |
|---|---|---|
| 5 km | $(5/255)^{2} = 3.84\times10^{-4}$ | essentially invisible from orbit |
| 50 km | $(50/300)^{2} = 2.78\times10^{-2}$ | 2.8% survives: detectable only if large |
| 200 km | $(200/450)^{2} = 0.1975$ | 20% survives: well suited |

**Conclusion:** the orbit is a **deep-source instrument**. Its sensitivity grows
with depth, while a terrestrial or airborne gravimeter is most sensitive to
shallow, near-surface mass. The two are complements, not competitors, and any
comparison of "satellite versus ground gravity" must state the depth window.

---

## ★3 — M2 alias for a 5-day repeat

$$f_s = \frac{1}{5\times24} = 8.3333\times10^{-3}\ \mathrm{h^{-1}},
\qquad f_{M2} = \frac{1}{12.4206012} = 8.05114\times10^{-2}\ \mathrm{h^{-1}}.$$

$$n = \operatorname{round}\left(\frac{8.05114\times10^{-2}}{8.3333\times10^{-3}}\right)
= \operatorname{round}(9.6614) = 10,$$
$$f_{\text{alias}} = \left|8.05114\times10^{-2} - 10\times8.3333\times10^{-3}\right|
= \left|8.05114 - 8.33333\right|\times10^{-2} = 2.8219\times10^{-3}\ \mathrm{h^{-1}},$$
$$T_{\text{alias}} = \frac{1}{2.8219\times10^{-3}} = 354.4\ \mathrm{h}
= 14.77\ \mathrm{days}.$$

A $12.42$-hour tide sampled every 5 days appears as a 14.8-day variation — note
this is the same alias the radar-altimetry lesson obtained for a 5-day repeat,
because the arithmetic depends only on the repeat cycle and the tidal period.
Being coherent with the sampling, it cannot be averaged away.

---

## ★4 — Ground-track spacing and repeat compatibility

**(a)** Twelve revolutions per repeat:
$$\Delta x = \frac{2\pi R_E}{12} = \frac{2\pi\times6371\ \mathrm{km}}{12}
= 3335.9\ \mathrm{km}.$$

**(b)** The spacing is the *equatorial* gap between adjacent ascending ground
tracks, so it sets the along-track sampling of the static field: a field feature
of half-wavelength smaller than $\Delta x$ cannot be resolved by the track
geometry alone, independently of the instrument. (Crossing tracks and multiple
repeat cycles fill in coverage, at the cost of sampling a field that changes.)

**(c)** A 4-day repeat with 12 revolutions requires the orbital period to be
$4/12 = 1/3$ day $= 8$ hours, which corresponds to an orbital radius of
$$r = \left(\frac{GM\,T^{2}}{4\pi^{2}}\right)^{1/3}
= \left(\frac{3.986\times10^{14}\times(2.88\times10^{4})^{2}}{39.478}\right)^{1/3}
= \left(8.379\times10^{21}\right)^{1/3} = 20\,310\ \mathrm{km},$$
i.e. an altitude of $\sim13\,900\ \mathrm{km}$ — far outside the low-orbit regime
this lesson assumes, where the attenuation is severe and the drag budget is
irrelevant for a different reason. **So the answer is no, not at low altitude**;
the repeat cycle and the altitude are linked by the orbital period, and a
designer cannot choose them independently. This is the quantitative version of
the statement that the repeat cycle is a scientific choice: it constrains, and is
constrained by, everything else.

---

## ★5 — The drag budget

**(a)** Required relative accuracy:
$$\frac{5\times10^{-8}}{3.0\times10^{-6}} = 1.67\times10^{-2},$$
i.e. the drag must be known to about **1.7%** — and that is only to make the drag
comparable to the signal; to resolve the signal at useful signal-to-noise the
requirement is a further factor of a few, so order $0.5\%$.

**(b)** Thermosphere models rely on empirical density relations driven by solar
and geomagnetic activity; their errors are tens of per cent, and the density
varies on timescales of minutes at these altitudes. No model reaches $0.5\%$, so
the non-gravitational acceleration must be **measured** with an accelerometer
(which is why the accelerometer is part of the gravity instrument) or avoided by
flying high enough that drag falls to the level of the other errors.

**(c)** The accelerometer's own calibration and bias error then becomes a
*systematic* gravity error at the same degree and with the same time signature as
the signal. It is not random and it does not average out; estimating it jointly
with the gravity field risks absorbing real signal into the accelerometer scale
factor — a classic degeneracy of exactly the kind measured in lesson 04 §3.3.

---

## ★6 — Mass required at depth

**(a)** For a compact anomaly at depth $d = 100\ \mathrm{km}$ seen at
$h = 250\ \mathrm{km}$:
$$g = \frac{GM}{(d+h)^{2}} \;\Longrightarrow\;
M = \frac{g\,(d+h)^{2}}{G}
= \frac{1\times10^{-8}\times(3.5\times10^{5})^{2}}{6.674\,30\times10^{-11}}
= \frac{1.225\times10^{3}}{6.674\,30\times10^{-11}} = 1.8354\times10^{13}\ \mathrm{kg}.$$

**(b)** The surface case required $9.364\times10^{12}\ \mathrm{kg}$, so the deep
anomaly must be larger by
$$\frac{1.8354\times10^{13}}{9.364\times10^{12}} = 1.960.$$

The ratio is $(350/250)^{2} = 1.96$ — exactly the inverse of the attenuation ratio
computed in ★2: the deep source sits $100\ \mathrm{km}$ further away, so its mass
must be larger by the squared-distance factor for the same observed acceleration.
**Interpretation:** the orbit's preference for deep sources is not a statement that
deep sources are easy to see (they are not; they need more mass for the same
signal) but that they are *less* suppressed than shallow ones. It is the *relative*
attenuation, compared with the ground-based alternative that sees a shallow mass
at its full strength, that makes the two techniques complementary.

---

## ★7 — A seasonal deep-anomaly mission (specification)

**Target.** A mass anomaly at $20\ \mathrm{km}$ depth with a seasonal amplitude of
$2\times10^{-8}\ \mathrm{m\,s^{-2}}$ at the satellite.

**Altitude.** Choose low (250–300 km) for two reasons: attenuation at $20\ \mathrm{km}$
depth is $(20/270)^{2} = 5.5\times10^{-3}$ at $250\ \mathrm{km}$, so every
kilometre of extra altitude costs signal directly; and a low orbit repeats
quickly. The cost is drag, which is why the accelerometer is mandatory and why the
mission lifetime is short.

**Repeat cycle.** Must place the aliases of the annual and semiannual signals away
from the frequencies of interest. With a 0.99-day repeat the M2 alias is
11.37 days (lesson table); the annual signal is directly observable (it is far
below the sampling frequency), so the requirement is to avoid aliasing the
*semidiurnal* signals into the seasonal band. A cycle of order 1 day, chosen so
that the alias of M2 falls near a period well separated from the seasonal and
monthly bands, satisfies this; the exact value must be searched with the alias
formula, not guessed.

**Instrument suite.** (i) An accelerometer, because the required accuracy is
$5.5\times10^{-3}\times2\times10^{-8} = 1.1\times10^{-10}\ \mathrm{m\,s^{-2}}$,
five orders below drag. (ii) A satellite-to-satellite range or range-rate link
between two spacecraft, because the *difference* is what cancels the common
orbit error and measures the differential field at the target degree. (iii) High-
quality orbit determination from GNSS. (iv) Star cameras for attitude, since the
accelerometer is not at the centre of mass and its measurements must be rotated.

**Error terms to control.** Accelerometer scale and bias, attitude errors,
the orbit determination, the thruster and outgassing disturbances, the Earth
radiation pressure (an order of magnitude smaller than the solar term but
seasonal — which makes it a *confounder* for this particular target), and the
aliasing of the semidiurnal tide.

**The alias structure to choose.** The seasonal signal is the target, so the
alias of any other signal must not land in the seasonal band. The dominant risk is
the semidiurnal tide, whose alias period depends on the repeat cycle; the design
therefore searches the repeat cycle so that the M2 and S2 aliases are far from
1 year and 0.5 year, and validates the choice with the alias formula given in the
lesson.

---

## ★8 — Above the crossover degree

**(a)** Above the crossover degree the attenuated signal is smaller than the
noise, so the estimated coefficients are determined by whatever constraint the
analyst imposed — a Kaula-like a priori spectrum, a smoothing condition, or a
positive-definite requirement — rather than by the data. The correct description
is "**not resolved**" or "regularisation-dominated": the numbers are a *model*
that is consistent with the data, complete with a variance ratio, but any other
model satisfying the same constraint would fit equally well. Calling them
"measured" implies the data determined them, which is precisely what the
crossover computation disproves.

**(b)** With a steeper spectrum (say $n^{-3}$ instead of $n^{-2}$) the signal at
high degree is *smaller*, so it crosses the noise sooner and the **crossover degree
falls**. Fewer degrees are resolved, and a larger fraction of a reported solution
is regularisation. This is why the true spectrum's steepness is one of the most
consequential facts in the field, and why quoting a maximum degree without the
spectrum and the noise is not a statement about the mission.

**(c)** A higher orbit shifts the crossover degree in two competing directions:
attenuation is the factor $(R_E/(R_E+h))^{n}$, which for fixed $n$ is smaller when
$h$ is larger — so a higher orbit sees *less* deep signal and the crossover degree
falls. But a higher orbit also has smaller non-gravitational accelerations
(drag falls off roughly exponentially with altitude), so the *noise* is lower,
which raises the crossover degree. The two effects therefore compete, and which
wins depends on the degree and on the instrument: this is exactly why both a
low-flying accelerometer-carrying design and a high-flying radiometer-carrying
design exist, and why the choice between them cannot be made by quoting an
altitude alone.
