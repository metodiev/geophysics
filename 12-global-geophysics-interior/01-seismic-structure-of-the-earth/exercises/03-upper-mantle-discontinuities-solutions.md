# Solutions — 12-01-03 Upper-Mantle Discontinuities at 410 and 660 km

Worked solutions for
[03-upper-mantle-discontinuities-exercises.md](./03-upper-mantle-discontinuities-exercises.md).
The lesson is
[03 Upper-Mantle Discontinuities at 410 and 660 km](../03-upper-mantle-discontinuities.md).
All parameters are **SYNTHETIC**.

---

## ★ Foundational

### ★1 — Topographic response and a precursor delay

$$\frac{\mathrm{d}z}{\mathrm{d}T} = \frac{\gamma}{\rho g}
= \frac{2.5\times10^{6}}{3700 \times 9.81} = 68.88\ \mathrm{m\,K^{-1}}.$$

For $\Delta T = +150\ \mathrm{K}$:

$$\delta z = 68.88 \times 150 = 1.033\times10^{4}\ \mathrm{m}
= 10.33\ \mathrm{km\ deeper}.$$

Precursor delay at 400 km, $v_s = 4.75$, $p = 0.050$:

$$q_s = \sqrt{\frac{1}{4.75^{2}} - 0.050^{2}}
= \sqrt{0.044321 - 0.002500} = \sqrt{0.041821} = 0.204502\ \mathrm{s\,km^{-1}},$$
$$\Delta t_\text{prec} = 2 \times 400 \times 0.204502 = 163.60\ \mathrm{s}.$$

The boundary arrives 163.6 s before the surface reflection. Note the unit chain:
$z$ (km) $\times$ $q_s$ (s km$^{-1}$) = s, and the factor 2 is the two-way path.

### ★2 — Clapeyron slope from entropy and volume

$$\gamma = \frac{\Delta S}{\Delta V}
= \frac{-6.0}{-2.8\times10^{-6}} = +2.14\times10^{6}\ \mathrm{Pa\,K^{-1}}
= +2.14\ \mathrm{MPa\,K^{-1}}.$$

$\Delta S < 0$ means the high-pressure assemblage has *lower* entropy, so the
transition releases heat as it proceeds: it is **exothermic**. The slope is
positive, so a cold downwelling (which lifts a boundary with $\gamma > 0$)
encounters the transition at shallower depth; because the reaction is exothermic,
it releases heat into the descending material, **opposing** further cooling and
therefore resisting the descent. An exothermic transition with a positive slope
acts as a *brake* on downwelling.

### ★3 — Reflection coefficient

$$Z_1 = \rho_1 v_{s1} = 3.30 \times 4.40 = 14.520\
\mathrm{g\,cm^{-3}\,km\,s^{-1}},$$
$$Z_2 = 3.42 \times 4.62 = 15.800,$$
$$R = \frac{15.800 - 14.520}{15.800 + 14.520} = \frac{1.280}{30.320} = +0.04223.$$

So **4.2 % of the incident amplitude** is reflected, with the same polarity (a
positive $R$ means an increase in impedance). The units of $Z$ cancel in the
ratio, which is why any consistent unit system works — but mixing
$\mathrm{kg\,m^{-3}}$ with $\mathrm{km\,s^{-1}}$ while another term uses
$\mathrm{g\,cm^{-3}}$ with $\mathrm{m\,s^{-1}}$ does *not*, because the ratio is
of differences and sums of the same quantity, not of the quantity itself.

---

## ★★ Applied

### ★★4 — Two boundaries, one temperature?

$q_s^{410} = \sqrt{1/4.70^2 - 0.055^2} = \sqrt{0.045269-0.003025} = 0.205532\
\mathrm{s\,km^{-1}}$,
$q_s^{660} = \sqrt{1/5.80^2 - 0.055^2} = \sqrt{0.029727-0.003025} = 0.163407\
\mathrm{s\,km^{-1}}$.

**(a) Displacements.** $\delta z = \delta(\Delta t)/(2q_s)$:

$$\delta z_{410} = \frac{-1.5}{2 \times 0.205532} = -3.649\ \mathrm{km},$$
$$\delta z_{660} = \frac{+2.0}{2 \times 0.163407} = +6.120\ \mathrm{km}.$$

**(b) Transition-zone thickness change:**

$$\delta H_{TZ} = \delta z_{660} - \delta z_{410} = 6.120 - (-3.649)
= +9.769\ \mathrm{km}.$$

The transition zone is 9.77 km thicker than the reference.

**(c) Mean-depth change:**

$$\delta \bar{z} = \frac{-3.649 + 6.120}{2} = +1.235\ \mathrm{km}.$$

**(d) Temperatures.** With $\mathrm{d}z_{410}/\mathrm{d}T = +56.63$ and
$\mathrm{d}z_{660}/\mathrm{d}T = -69.50\ \mathrm{m\,K^{-1}}$:

$$\Delta T_{410} = \frac{-3649}{56.63} = -64.4\ \mathrm{K}, \qquad
\Delta T_{660} = \frac{+6120}{-69.50} = -88.1\ \mathrm{K}.$$

**Self-consistency.** The two boundaries *agree in sign* (both cold, which is why
the transition zone is thicker: a cold anomaly lifts the 410 and deepens the 660)
but disagree in magnitude by 37 %. A single, uniform thermal anomaly cannot do
that. Either the Clapeyron slopes used differ from the true ones in that
proportion, or the region carries a compositional or dynamical-pressure component,
or the reference model's depths are wrong at one boundary by 1–2 km. Reporting the
average (−76 K) would hide all three possibilities; reporting both is the honest
answer. This is the practical value of measuring the two boundaries separately.

### ★★5 — Transition widths from a half-amplitude measurement

**(a)** Half amplitude means $\operatorname{sinc}(\pi f\tau) = 0.5$, whose first
solution is $\pi f \tau = 1.8955$ rad. At $f = 0.25\ \mathrm{Hz}$:

$$\tau = \frac{1.8955}{\pi \times 0.25} = 2.4136\ \mathrm{s},\qquad
w = v_s\tau = 4.70 \times 2.4136 = 11.34\ \mathrm{km}.$$

**(b)** At $f = 0.10\ \mathrm{Hz}$ the same half amplitude requires

$$\tau = \frac{1.8955}{\pi \times 0.10} = 6.034\ \mathrm{s},\qquad
w = 4.70 \times 6.034 = 28.36\ \mathrm{km}.$$

**(c)** A 12 km ramp at $f = 0.10\ \mathrm{Hz}$:
$\tau = 12/4.70 = 2.553$ s, $\pi f\tau = 0.8021$ rad,
$\operatorname{sinc}(0.8021) = \sin(0.8021)/0.8021 = 0.7191/0.8021 = 0.8962$ —
**90 %** of the sharp-boundary amplitude survives.

The lesson: **the same physical ramp is "sharp" at 0.1 Hz and strongly filtered
at 0.25 Hz.** Quoting 11.3 km without the frequency is meaningless, and combining
measurements at two frequencies constrains the *shape* of the transition, not just
its width.

### ★★6 — Two explanations of a $+2.0\ \mathrm{s}$ change

*Displacement:*

$$\delta z = \frac{+2.0}{2 \times 0.205532} = +4.865\ \mathrm{km}
\;\Rightarrow\;
\Delta T = \frac{4865}{56.63} = +85.9\ \mathrm{K}\ (\text{hot}).$$

*Velocity:* with the transition zone 250 km thick and $v_s = 4.70$,

$$\delta(\Delta t) \approx \frac{2 H_{TZ}\epsilon}{v_s}
= \frac{2 \times 250 \times \epsilon}{4.70} = 106.4\,\epsilon\ \mathrm{s},
\;\Rightarrow\;
\epsilon = \frac{2.0}{106.4} = +0.0188,$$

i.e. a **1.88 % reduction** in S velocity across the transition zone.

**Signs are consistent.** A hot anomaly both deepens the 410 (+4.87 km) and
reduces $v_s$ (by ~1.9 % if the thermal sensitivity were large enough), and both
make the precursor arrive later. So the two explanations do not merely
*coincidentally* fit: they are the two faces of the same thermal anomaly. The
degeneracy is therefore quantitative, not qualitative, and it is *severe* here:
the required 1.9 % velocity reduction at these depths is large for an 86 K anomaly
(a typical mantle $|\partial \ln v_s/\partial T|$ gives a few tenths of a per cent
for 86 K), which means the velocity explanation is the less plausible of the two
*for the assumed sensitivities*. Precisely because the sensitivities are assumed,
the honest conclusion is that the delay change can be explained topographically
with a modest anomaly, or by a velocity change that would be unusually large —
and distinguishing these needs an independent velocity estimate.

---

## ★★★ Research-oriented

### ★★★7 — Separating temperature from dynamical pressure

A uniform dynamic-pressure change $\delta P$ displaces *every* boundary in the
same direction by $\delta z = \delta P/(\rho g)$; a temperature change displaces
them in *opposite* directions (because the Clapeyron slopes have opposite signs).
The two boundary depths therefore carry two orthogonal signals, and the
thickness/difference combination diagonalises them:

$$\frac{\partial H_{TZ}}{\partial T} = \frac{\gamma_{660}}{\rho_{660}g}
- \frac{\gamma_{410}}{\rho_{410}g}
= -69.50 - 56.63 = -126.13\ \mathrm{m\,K^{-1}},$$
$$\frac{\partial \bar{z}}{\partial T} = \frac{1}{2}\left(\frac{\gamma_{410}}{\rho_{410}g}
+ \frac{\gamma_{660}}{\rho_{660}g}\right)
= \frac{56.63 - 69.50}{2} = -6.44\ \mathrm{m\,K^{-1}},$$
$$\frac{\partial H_{TZ}}{\partial P} = \frac{1}{\rho_{660}g}
- \frac{1}{\rho_{410}g} = -5.15\ \mathrm{m\,MPa^{-1}},$$
$$\frac{\partial \bar{z}}{\partial P} = \frac{1}{2}\left(\frac{1}{\rho_{410}g}
+ \frac{1}{\rho_{660}g}\right) = +25.74\ \mathrm{m\,MPa^{-1}}.$$

**Cross-talk matrix** (how much of the *other* parameter a 10-unit change mimes):

| perturbation | effect on $H_{TZ}$ | apparent $T$ error | effect on $\bar z$ | apparent $P$ error |
|---|---|---|---|---|
| $\Delta T = +10$ K | +1.261 km | — | −0.064 km | −2.50 MPa |
| $\Delta P = +10$ MPa | −0.051 km | −0.41 K | +0.257 km | — |

**Reading of the matrix.** Use the thickness for temperature (126 m K$^{-1}$,
with a pressure leak equivalent to only 0.4 K per 10 MPa) and the mean depth for
dynamical pressure (25.7 m MPa$^{-1}$, with a thermal leak equivalent to 2.5 MPa
per 10 K). Note the important practical asymmetry: the *pressure* leak into the
thermometer is small (0.4 K per 10 MPa), so a temperature estimate from
transition-zone thickness is robust; whereas the *thermal* leak into the pressure
estimate is large (2.5 MPa per 10 K), so a dynamic-pressure estimate from mean
depth demands an independent temperature. In practice the temperature comes from
the thickness first, and that temperature is then used to correct the mean depth.
The 100 MPa scale of a dynamic pressure corresponds to a 2.8 km displacement —
comparable to a 50 K thermal anomaly, which is why the separation matters at all.

### ★★★8 — If the 660 had a positive slope

With $\gamma_{660} = +3.0\ \mathrm{MPa\,K^{-1}}$ instead of $-3.0$
(everything else unchanged):

$$\frac{\partial H_{TZ}}{\partial T} = +69.50 - 56.63 = +12.87\
\mathrm{m\,K^{-1}}, \qquad
\frac{\partial \bar z}{\partial T} = \frac{56.63 + 69.50}{2}
= +63.07\ \mathrm{m\,K^{-1}}.$$

The roles of the two combinations **swap**: the thickness becomes nearly
temperature-insensitive (12.9 m K$^{-1}$, a factor of 10 worse than before) and
the *mean depth* becomes the thermometer (63.1 m K$^{-1}$).

**What is lost.** (i) The thermometer's leverage drops from 126.1 to
63.1 m K$^{-1}$ — a factor of 2, so temperature errors double. (ii) The clean
separation is destroyed: the pressure sensitivities are unchanged
(−5.15 m MPa$^{-1}$ for thickness, +25.74 m MPa$^{-1}$ for mean), so the mean
depth is now sensitive to *both* parameters (63.07 m K$^{-1}$ and
25.74 m MPa$^{-1}$) while the thickness is sensitive to *neither* strongly. The
cross-talk becomes:

- a $10\ \mathrm{K}$ error moves the thickness by $+0.129\ \mathrm{km}$,
  equivalent to $0.129/0.00515 = 25.0\ \mathrm{MPa}$ of apparent pressure
  (against 2.5 MPa in the real configuration — 10× worse);
- a $10\ \mathrm{MPa}$ error moves the mean by $+0.257\ \mathrm{km}$, equivalent
  to $257.4/63.07 = 4.08\ \mathrm{K}$ of apparent temperature (against 0.41 K —
  10× worse on the thermometer side).

**What the difference would measure instead.** With the same sign, the
transition-zone thickness becomes a near-pure *pressure* gauge
(−5.15 m MPa$^{-1}$) and the mean depth a mixed thermometer/pressure gauge; the
*composition-sensitive* quantity that the mean depth provides in the real Earth
would then have to come from elsewhere. The general lesson: **a pair of
boundaries is useful in proportion to the contrast between their Clapeyron
slopes**, and the opposite-sign pair 410/660 is close to the best case the mantle
offers.

### ★★★9 — The slowness gap of a triplication

$U = r/v_s$ on either side of a jump at 660 km depth, using radii
$r = 6371 - 659 = 5712$ km above and $r = 6371 - 661 = 5710$ km below:

$$U_\text{above} = \frac{5712}{5.80} = 984.83\ \mathrm{s\,rad^{-1}}, \qquad
U_\text{below} = \frac{5710}{6.30} = 906.35\ \mathrm{s\,rad^{-1}},$$
$$\Delta p = 984.83 - 906.35 = 78.48\ \mathrm{s\,rad^{-1}}
= \frac{78.48 \times 100}{906.35} = 8.66\ \%.$$

**Why the gap matters more than the jump.** A travel-time record section displays
$T(\Delta)$. Rays with $p$ inside the gap do not exist, so the branch that would
carry them is *missing*: the observed curve is broken, with the small-$p$ branch
arriving later at the same distance than an extrapolation of the large-$p$ branch
would predict. The width of the gap in $p$ sets (i) the range of distances over
which the two branches coexist — hence the width of the amplitude caustic — and
(ii) the size of the time offset between the branches. A velocity jump of the same
size at a different depth would give a *different* gap, because $\Delta p$ depends
on $r$ and on the local $v$, not only on the contrast. So the observable constrains
a combination of depth, contrast and local velocity — which is why triplications
are interpreted with a full forward model rather than a formula, and why the gap
is a *sharpness* measurement of the same family as the amplitude filter of
Section 5 of the lesson.

---

## Mastery checkpoint — worked version

> $\delta z_{410} = -4.0\ \mathrm{km}$, $\delta z_{660} = +5.5\ \mathrm{km}$.

**(a) Thickness and temperature.**

$$\delta H_{TZ} = +5.5 - (-4.0) = +9.5\ \mathrm{km},$$
$$\Delta T = \frac{\delta H_{TZ}}{\mathrm{d}H_{TZ}/\mathrm{d}T}
= \frac{9500\ \mathrm{m}}{-126.13\ \mathrm{m\,K^{-1}}} = -75.3\ \mathrm{K}.$$

The region is ~75 K colder than the reference. (The two boundaries individually
give $-4000/56.63 = -70.6$ K and $+5500/(-69.50) = -79.1$ K — a 12 % spread, the
same self-consistency test as exercise ★★4.)

**(b) Precursor delay change at 410.**

$$\delta(\Delta t)_{410} = 2q_s\,\delta z_{410}
= 2 \times 0.205532 \times (-4.0) = -1.644\ \mathrm{s}.$$

**(c) Competing explanation.** A 1.5 % S-velocity *reduction* across the 250 km
transition zone changes the delay by $+106.4 \times 0.015 = +1.596\ \mathrm{s}$,
which is the *opposite* sign to the $-1.644$ s from (b). So the tomographic
preference and the topographic displacement point in **opposite directions** and
cannot be reconciled by scaling one of them: the delay in (b) favours either a
cold anomaly (a boundary 4 km shallower, which is what the delay asks for) or a
*faster* transition zone (≈ +1.5 %), not a slower one. Since (a) independently
requires a cold anomaly from the pair of boundaries, the consistent reading is a
cold region with a *normal or faster* transition zone; the tomographic 1.5 %
slow anomaly contradicts it and must come from resolution smear, from a
compositional effect, or from an error in the reference velocity.

**(d) Measurement that settles it.** A triplication or a *transmitted* phase whose
travel time depends on the velocity *and* the depth differently from a precursor
delay — for example a regional triplication from the 410 (Section 7 of the lesson,
with its $\Delta p$ gap), or a second precursor slowness. Alternatively, an
absolute depth constraint from a body-wave turning point, which fixes $z$ and
leaves the velocity to be inferred from the residual.
