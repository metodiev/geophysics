# Solutions — 14-02-03 Seismic Methods for Aquifer Geometry

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All models are **SYNTHETIC**.

Lesson: [03 Seismic Methods for Aquifer Geometry](../03-seismic-hydrogeophysics.md).

---

## ★1 — Water-table reflection coefficient

$$Z_1 = \rho_1 v_{p1} = 1800 \times 900 = 1.620 \times 10^{6}\
\mathrm{kg\,m^{-2}\,s^{-1}},$$
$$Z_2 = \rho_2 v_{p2} = 2050 \times 1700 = 3.485 \times 10^{6}\
\mathrm{kg\,m^{-2}\,s^{-1}},$$
$$R = \frac{3.485 - 1.620}{3.485 + 1.620} = \frac{1.865}{5.105} = +0.3653.$$

**Polarity convention.** $R > 0$ means $Z_2 > Z_1$: the reflector is "hard", the
reflected wave has the same polarity as the downgoing wave, and the transmitted
amplitude is $1 + R = 1.365$. On a real section, the top of a saturated sand under
a dry cover is therefore typically a peak (positive) event, whereas the transition
*into* a soft, slow layer would be a trough. Note also that $R = 0.365$ is
unusually large — real water-table reflections are usually $0.05$–$0.2$ — and the
lesson attributes that to the dryness of the cover.

---

## ★2 — Wavelength and resolution

$$\lambda = \frac{v}{f} = \frac{1500}{100} = 15\ \mathrm{m}, \qquad
\frac{\lambda}{4} = 3.75\ \mathrm{m}.$$

So a layer thinner than about **3.75 m** cannot have its thickness measured from
travel time with a 100 Hz source in this medium; its presence may still be detected
through the tuning amplitude (Section 3 of the lesson). Increasing the frequency to
200 Hz halves the limit to 1.9 m, at the cost of twice the attenuation — which is
the trade that governs shallow high-resolution surveys.

---

## ★3 — Crossover distance

$$x_{\text{cross}} = 2h\sqrt{\frac{v_2 + v_1}{v_2 - v_1}}
= 2(8)\sqrt{\frac{1500 + 500}{1500 - 500}} = 16\sqrt{2} = 22.63\ \mathrm{m}.$$

**Design consequence.** The refracted arrival from the saturated layer becomes the
first arrival only beyond 22.6 m, so the spread must be at least about 45 m
(twice the crossover, to sample the head wave's slope at both ends) to determine
the layer's depth and velocity. A 24 m spread would record the crossing but not
constrain the velocity, and a 10 m spread would see nothing at all.

---

## ★★4 — Reading the tuning curve

**(i) Half the tuning peak.** $1.409/2 = 0.705$. Between 1.0 m (0.361) and 2.0 m
(0.853), interpolating linearly in thickness:
$$b = 1.0 + (2.0 - 1.0)\frac{0.705 - 0.361}{0.853 - 0.361}
= 1.0 + 0.699 = 1.70\ \mathrm{m}.$$

**(ii) 20% of the thick-layer value.** The thick-layer peak is 1.000, so target
0.200, between 0.5 m (0.183) and 1.0 m (0.361):
$$b = 0.5 + 0.5\frac{0.200 - 0.183}{0.361 - 0.183} = 0.5 + 0.048
= 0.55\ \mathrm{m}.$$

**(iii) Thinnest thickness readable from travel time.** Where the top and base
wavelets separate, i.e. where the response has returned to the thick-layer value
1.000: from the table that happens by 12 m (1.008 before rounding) and certainly by
20 m. A defensible answer is **$b \gtrsim \lambda/2 = 13.8$ m**, consistent with the
table's 12 m value being within 1% of the asymptote.

**Interpolation and its justification.** Linear interpolation in thickness is
justified on the *thin* branch (where the response is proportional to thickness,
confirmed by the table: 0.183 at 0.5 m versus 0.361 at 1.0 m, a ratio of 1.97 for a
ratio of 2.00), but is only a rough approximation near and above the tuning peak,
where the curve is nonlinear. The honest statement of (i) is therefore
"$1.7 \pm 0.3$ m", and the exercise's real content is realising that a
interpolated inversion of the tuning curve requires the peak location to be known
from a wavelet estimate, not assumed.

---

## ★★5 — Hidden layer: deriving the condition

**Setup.** Layer 2 has velocity $v_2$ and thickness $h_2$, sitting at depth $h_1$
below the surface. Layer 3's head wave arrives first from its own crossover
distance measured from the surface, at depth $h_1 + h_2$:
$$x_{\text{cross},13} = 2(h_1+h_2)\sqrt{\frac{v_3+v_1}{v_3-v_1}},$$
while layer 2's head wave appears at
$$x_{\text{cross},12} = 2h_1\sqrt{\frac{v_2+v_1}{v_2-v_1}}.$$

**Condition for layer 2 to be invisible** (its branch suppressed before it can
appear): $x_{\text{cross},13} < x_{\text{cross},12}$, i.e.

$$(h_1 + h_2)\sqrt{\frac{v_3+v_1}{v_3-v_1}}
< h_1\sqrt{\frac{v_2+v_1}{v_2-v_1}}
\;\Longrightarrow\;
h_2 < h_1\left[\sqrt{\frac{v_2+v_1}{v_2-v_1}}\bigg/\sqrt{\frac{v_3+v_1}{v_3-v_1}}
- 1\right].$$

**Evaluate** with $h_1 = 2$ m, $v_1 = 400$, $v_2 = 1200$, $v_3 = 2000$:
$$\sqrt{\frac{v_2+v_1}{v_2-v_1}} = \sqrt{\frac{1600}{800}} = 1.4142, \qquad
\sqrt{\frac{v_3+v_1}{v_3-v_1}} = \sqrt{\frac{2400}{1600}} = 1.2247,$$
$$h_2^{\max} = 2\left(\frac{1.4142}{1.2247} - 1\right) = 2(0.1547)
= 0.309\ \mathrm{m}.$$

**Conclusion.** Layer 2 must be thinner than about **0.31 m** to be hidden, which is
thin. For a more realistic $h_2 = 2$ m the crossover distances are
$x_{\text{cross},12} = 5.66$ m and $x_{\text{cross},13}$ measured from the surface
through the layer stack $= 2(4)(1.2247) = 9.80$ m, so the $v_2$ branch spans
**5.7–9.8 m** and is visible on any spread longer than about 20 m that has
geophones in that window. **The layer becomes visible as soon as the spread
includes the crossing at 9.8 m**, and the design requirement is dense geophones
between 5 and 10 m — a spacing of 1 m, not 5 m, or the short branch is missed
between samples.

This is the arithmetic that must be done *before* a survey: how long is the
intermediate branch, and what geophone spacing samples it?

---

## ★★6 — Velocity error to depth error

Correct: $d = 1800 \times 0.030/2 = 27.0$ m.
With the wrong velocity: $d = 1500 \times 0.030/2 = 22.5$ m.

Error: $22.5 - 27.0 = -4.5$ m, i.e. $-16.7\%$ of the correct depth.

**Why it is not small.** A 4.5 m depth error is comparable with the entire
thickness of a typical alluvial aquifer and larger than the seasonal water-level
change the survey may be trying to detect. In groundwater work the depths of
interest are a few metres to a few tens of metres, so a percentage velocity error
translates directly into a metre-scale depth error — unlike in deep crustal
seismology, where the same percentage error is kilometres and is reported as such.

---

## ★★★7 — Combined programme for a 3 m aquifer at 15 m

**Target:** 3 m thick aquifer, top at 15 m; depth to $\pm 0.5$ m (3.3%); water
content to $\pm 0.02$.

**Seismic.** For the depth to be resolved to 0.5 m at a TWT determined by the
(variable) near-surface velocity, the *velocity* must be known to about
$0.5/15 = 3.3\%$. That is not achievable from first-break refraction alone in a
heterogeneous vadose zone without dense sampling, so the design must include a
direct velocity measurement (borehole). Source frequency: to detect a 3 m aquifer
the tuning thickness $\lambda/4 \le 3$ m requires
$\lambda \le 12$ m, i.e. $f \ge v/12$. With an aquifer $v_p = 1700\
\mathrm{m\,s^{-1}}$ that is **$f \ge 142$ Hz** — achievable only with a small
source and a short spread (a hammer or a small accelerated weight drop), and only if
the near-surface is not too attenuating. Spread: to place the water table as a
refractor (if used) with $h = 15$ m and, say, $v_1 = 500$,
$v_2 = 1700\ \mathrm{m\,s^{-1}}$, the crossover is
$2(15)\sqrt{2200/1200} = 40.6$ m, so a **spread of at least 81 m** with 1–2 m
receiver spacing in the critical window. That conflict — high frequency for
resolution, long spread for depth — is the central seismic design tension and is
resolved here by preferring reflection with a borehole velocity tie rather than
refraction alone.

**GPR.** To measure water content to $\pm 0.02$ in the vadose zone above 15 m, the
permittivity must be known to about 8% ($\mathrm{d}\varepsilon/\mathrm{d}\theta
= 16\sqrt{\varepsilon}$; see
[14-01-06 §5](../../01-hydrology-fundamentals/06-unsaturated-zone.md)). A 250 MHz
antenna in a sandy vadose zone reaches 5–10 m at best; a 100 MHz antenna reaches
15 m with poorer resolution. So **GPR covers the top of the profile well and the
target depth marginally**: it constrains the near-surface velocity for the seismic
time-to-depth conversion (its real value here) and gives water content above the
water table, not at 15 m.

**Boreholes.** Two to three, to $\sim$20 m: one to log (density/neutron/NMR for
porosity and water content, and a gamma log for clay), one for a suspended-velocity
or downhole-geophone profile to give the interval velocity, and one as the water
sample and water-level datum for the chemistry and the chloride tie-in. **The
boreholes break the time-to-depth circularity; nothing in the seismics does.**

**Error budget for the depth.**

| Contribution | Magnitude | Effect on 15 m depth |
|---|---|---|
| interval velocity from the borehole | 1% | 0.15 m |
| TWT picking | 0.5 ms on 17.6 ms | 0.43 m |
| capillary fringe / transition zone | ~1 m thickness | apparent shift of 0–1 m |
| lateral velocity variation between boreholes | 3% | 0.45 m |
| Combined (quadrature, excluding the fringe bias) | | ~0.65 m |

So $\pm 0.5$ m is **marginally achievable**, and only with the borehole tie. The
capillary fringe is a systematic, not random, error and must be reported separately:
a 1 m fringe in a fine sand moves the apparent water table up by up to 1 m and
reduces the amplitude.

**Water content to $\pm 0.02$.** Achievable from GPR in the vadose zone and from
borehole logs at depth, combined through one rock-physics calibration. It is *not*
achievable from the seismics alone, because the $v_p(S_w)$ relation has several
free parameters (frame moduli, fluid distribution) that the seismic data cannot
separate.

---

## ★★★8 — Verification and validation plan

### (a) The reflection modelling code

**Verification 1 — analytic half-space.** For a single interface between two
half-spaces the reflected pulse is $R \cdot w(t - t_0)$ with
$R = (Z_2-Z_1)/(Z_2+Z_1)$ and $t_0$ set by the depth. Test: model a half-space
interface, deconvolve the wavelet, and compare the recovered amplitude with $R$ to
within $10^{-6}$. **Catches:** a wrong impedance formula, a polarity error, a
units error in density or velocity. **Misses:** everything with more than one
interface.

**Verification 2 — the tuning curve.** For a layer whose top and base are both
modelled, the peak amplitude as a function of thickness must follow the analytic
difference-of-wavelets curve (the lesson's table). Test: model a wedge in
$\Delta b$ steps and compare with the analytic difference at each thickness.
**Catches:** a mis-timed second interface, a sign error in the second reflection,
an incorrect internal-multiple suppression. **Misses:** a systematic amplitude error
common to both reflections (for example a wrong geometrical-spreading correction).

**Verification 3 — convergence.** Refine the depth sampling (and the time step, if
finite-difference) and measure
$p = \log_2\lVert E(\Delta z)\rVert/\lVert E(\Delta z/2)\rVert$ against a fine-grid
reference, where $E$ is a travel-time or amplitude error. For a second-order scheme
expect $p \to 2$; **state the refinement rule for the time step as well**, because
the observed order is meaningless if the temporal and spatial errors are not
refined in a controlled ratio. **Catches:** an implementation error in the
stencil order. **Misses:** a wrong physical model (the code can be consistent and
wrong).

**Validation.** Compare the modelled seismogram with real data from a site where
the reflectivity is independently known (a borehole log converted to acoustic
impedance, or a zero-offset VSP): the modelled and observed traces must agree within
the stated noise, including amplitudes, not just arrival times. That tests the
source wavelet, the spreading and transmission losses, and attenuation — none of
which the verification tests touch.

### (b) The $v_p(S_w)$ relation

**What would establish it empirically.** A laboratory programme on cores from the
site: measure $v_p$ (and $v_s$, for $K_{\text{dry}}$) at a series of known
saturations, with careful control of the saturation *distribution* (uniform by slow
imbibition versus patchy by drainage), plus porosity, mineralogy and the frame
bulk and shear moduli. Then either fit Gassmann (uniform) with a patchiness
correction, or fit an empirical relation with stated uncertainty. The essential
point is that the relation is a **rock property of a specific material and a
specific saturation history**, not a universal law.

**Why a code test cannot do it.** A code test compares a numerical implementation
with an equation — including the equation that embeds the $v_p(S_w)$ relation. If
the relation is wrong, every verification test still passes, because they test the
solver, not the physics. This is the verification/validation distinction in its
sharpest form: **verification asks "did I solve the equations right?", validation
asks "are these the right equations for this rock?"**

**Consequence for interpretation.** Any hydrological interpretation that depends on
seismic velocity to infer saturation carries the uncertainty of an essentially
uncalibrated rock-physics relation. That is why the standard practice in
hydrogeophysical work is to (i) report seismic results as *geometry* and
*velocity*, (ii) infer saturation only where a borehole calibration exists, and
(iii) prefer a method that measures water content directly — GPR permittivity or
surface NMR ([05 Surface NMR](../05-nmr-for-groundwater.md)) — when saturation itself is the
target.

### Ranking, with one number each

| Target | Best | Second | Reason (one number) |
|---|---|---|---|
| Water table | seismic reflection (arid, coarse) | GPR | $R$ up to $+0.41$ in a dry sand, structurally simple and laterally continuous |
| Clay layer base | ERT | seismic | bulk resistivity contrast of a factor of 10 or more, versus $R = +0.058$ for the synthetic sand–clay contact |
| Water content | GPR (vadose) / NMR (saturated) | borehole logs | $\mathrm{d}\varepsilon/\mathrm{d}\theta = 46$ near $\theta = 0.15$, i.e. a 1% water-content change is a 5.5% permittivity change |

The ranking is not a competition: the productive design is seismic for geometry,
ERT for clay and salinity, GPR and NMR for water content, and a borehole to tie
them together.

---

## Mastery checkpoint — worked

Synthetic site: 4 m of unsaturated sand ($v_p = 700\ \mathrm{m\,s^{-1}}$,
$\rho = 1700\ \mathrm{kg\,m^{-3}}$) over saturated gravel
($v_p = 1800\ \mathrm{m\,s^{-1}}$, $\rho = 2100\ \mathrm{kg\,m^{-3}}$), water table
at 4 m, 50 Hz source.

**(a) Two-way time and reflection coefficient.**
$$\mathrm{TWT} = \frac{2 \times 4}{700} = 0.011429\ \mathrm{s} = 11.43\
\mathrm{ms}.$$
$$Z_1 = 1700 \times 700 = 1.190 \times 10^{6}, \qquad
Z_2 = 2100 \times 1800 = 3.780 \times 10^{6},$$
$$R = \frac{3.780 - 1.190}{3.780 + 1.190} = \frac{2.590}{4.970} = +0.5211.$$

$R = 0.52$ is very large — larger than the lesson's own example — because the sand
is dry and slow. Treat it as an upper bound and remember that $R$ scales with the
dryness of the cover, not with the aquifer.

**(b) Tuning thickness.**
$$\lambda = \frac{v}{f} = \frac{1800}{50} = 36\ \mathrm{m}, \qquad
\frac{\lambda}{4} = 9.0\ \mathrm{m}, \qquad \frac{\lambda}{2} = 18.0\ \mathrm{m}.$$

The aquifer is 15 m thick, i.e. $0.42\lambda$: **above** the tuning thickness
(9 m) but **below** $\lambda/2$ (18 m). The base is therefore discernible and the
thickness can be estimated from the travel time, but the amplitude is still
enhanced by partial wavelet overlap (from the lesson's table, a $0.42\lambda$ layer
sits at about 1.0–1.1 times the thick-layer amplitude, so the enhancement is
modest). The honest statement is "15 m thick, resolvable at the 10–20% level from
travel time, with the amplitude method available as a cross-check".

**(c) Refraction crossover and intercept time.**
$$x_{\text{cross}} = 2(4)\sqrt{\frac{1800 + 700}{1800 - 700}} = 8\sqrt{2.2727}
= 12.06\ \mathrm{m},$$
$$t_i = \frac{2(4)\sqrt{1800^{2} - 700^{2}}}{700 \times 1800}
= \frac{8 \times 1658.3}{1.260 \times 10^{6}}
= 1.053 \times 10^{-2}\ \mathrm{s} = 10.53\ \mathrm{ms}.$$

Design note: a spread must exceed about 24 m to determine the refractor's velocity,
and the water table is shallow enough (4 m) that this is comfortable — the opposite
of the deep-target case.

**(d) Depth error from the wrong velocity.** Using $1600\ \mathrm{m\,s^{-1}}$ (a
"saturated-zone" velocity) instead of the correct interval velocity of the
*unsaturated* zone (700 m/s):
$$d_{\text{wrong}} = \frac{1600 \times 0.011429}{2} = 9.14\ \mathrm{m},$$
against a true depth of 4.00 m: an error of $+5.14$ m, or **$+129\%$**.

The lesson to draw is not "velocities are uncertain" but "**which** velocity". The
time picked to the water table accumulates only in the unsaturated zone, so the
correct conversion velocity is that interval's — and using the aquifer's velocity is
wrong by a factor of 2.3. This is the most common quantitative error in shallow
seismic hydrogeophysics.

**(e) After a wet winter.** With $S_w = 0.5$ in the unsaturated sand, using the
lesson's interpolation scaled to this site's end members
($v_p = 700 + 1100[1-(1-S_w)^{2}]$, $\rho = 1700 + 400S_w$):
$$v_p = 700 + 1100(0.75) = 1525\ \mathrm{m\,s^{-1}}, \qquad
\rho = 1700 + 200 = 1900\ \mathrm{kg\,m^{-3}},$$
$$Z_1 = 1900 \times 1525 = 2.8975 \times 10^{6},$$
$$R = \frac{3.780 - 2.898}{3.780 + 2.898} = \frac{0.882}{6.678} = +0.132.$$

**The reflection amplitude falls by a factor of 3.94** (from 0.521 to 0.132) with
no change at all in the aquifer. This is the quantitative form of the lesson's
warning: a time-lapse seismic survey designed to watch a water table would see the
seasonal wetting of the *cover* as a dominant amplitude change, and could easily
misread it as a change in the aquifer. Any such survey needs an independent
near-surface water-content measurement (GPR or a shallow TDR array) to separate the
two.

**(f) The measurement to insist on.** A **direct in-situ velocity measurement in a
borehole** — an uphole survey, a downhole geophone, or a suspended-velocity
(sediment velocity) log from the surface down through the unsaturated zone. It is
the only measurement in the list that supplies the *interval* velocity actually
required by the time-to-depth conversion, and it does so without assuming the
$v_p(S_w)$ relation that part (e) shows to be unreliable. GPR can substitute
partially (it measures the radar velocity, hence water content, hence constrains the
seismic velocity through rock physics), and a refraction tomogram can substitute
partially (it uses the seismic data to build a near-surface model), but neither
closes the circle; the borehole does.
