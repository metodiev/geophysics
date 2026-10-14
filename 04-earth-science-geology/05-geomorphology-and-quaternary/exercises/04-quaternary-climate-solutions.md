# Solutions — 04-05-04 Quaternary Climate Change and Landscape Records

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values computed here are labelled as such.

Throughout: the insolation arithmetic is a **derivation** given the stated orbital
elements; the isotope and sea-level numbers are **model results** dependent on
declared inputs; the palaeoclimate conclusions of ★★★8 are **inferences** and are
labelled as such.

---

## ★1 — Orbital geometry

**(a)** $\lambda = 282^\circ$ is perihelion, so
$\cos(0) = 1$ and $(a/r)^{2} = 1 + 2(0.0167) = 1.0334$. At
$\lambda = 102^\circ$, $\cos(180^\circ) = -1$ and $(a/r)^{2} = 1 - 0.0334 =
0.9666$.

**(b)** $\sin\delta = \sin(23.44^\circ)\sin(90^\circ) = 0.39779$, so
$\delta = 23.44^\circ$ — the declination equals the obliquity at the solstice, by
construction.

**(c)** $\tan(65^\circ) = 2.14451$, $\tan(23.44^\circ) = 0.43357$, so
$-\tan\varphi\tan\delta = -0.92979$ and
$H_0 = \arccos(-0.92979) = 2.76464$ rad $= 158.402^\circ$.

Day length $= 2 \times 158.402^\circ / 15^\circ$ per hour $= 21.12$ h.

**(d)** At 45°N, $-\tan\varphi\tan\delta = -0.43357$, so
$H_0 = 2.01924$ rad $= 115.694^\circ$ and the day length is **15.43 h**.

The 5.7 h difference between the two latitudes at the same solar longitude is the
entire reason obliquity matters: it changes *how long* and *how obliquely* the
high-latitude surface is illuminated.

---

## ★2 — Invariance of the global annual mean

**(a)** $S_0/4 = 1361/4 = 340.25$ W m⁻².

**(b)** The demo reports **340.1940** W m⁻² at $\varepsilon = 22.0^\circ$ and
**340.2036** W m⁻² at $\varepsilon = 24.5^\circ$; with the perihelion longitude
moved by 282° it reports the same 340.2036 W m⁻².

**(c)** The two obliquity values agree because the *global annual mean* removes
both $\varepsilon$ and $\varpi$ from the integral — this is the exact invariant,
and the agreement to 0.003 per cent is limited only by the finite latitude and
longitude grids. The residual deficit against $S_0/4$ (0.02 per cent) is the
first-order approximation
$(a/r)^{2} \approx 1 + 2e\cos(\lambda-\varpi)$, whose average over a uniform
$\lambda$ grid is 1 only to the accuracy of the quadrature; the exact factor has
a different mean.

---

## ★3 — Ice volume, sea level and isotopes

**(a)** $V = (3\times10^{6} \times 10^{6})(1800) = 5.4\times10^{15}$ m³.

$$\Delta z = \frac{917}{1000}\frac{5.4\times10^{15}}{3.61\times10^{14}}
= 13.717\ \mathrm{m}.$$

**(b)** $M_o = 3.61\times10^{14} \times 3700 \times 1000 =
1.3357\times10^{21}$ kg; $M_i = 917 \times 5.4\times10^{15} =
4.9518\times10^{18}$ kg. Then

$$\delta' = \frac{-M_i\delta_i}{M_o - M_i}
= \frac{(4.9518\times10^{18})(35)}{1.3307\times10^{21}} = 0.1302\ \text{‰}.$$

Numeric check with the demo's analogous case (10.161 m of sea level, 0.0964‰):
the ratio there is $0.0964/10.161 = 0.009487$‰ m⁻¹, and here
$0.1302/13.717 = 0.009493$‰ m⁻¹ — the same to 0.06 per cent.

**(c)** $0.009494$‰ per metre, i.e. about **105 m of sea-level change per per
mille**.

**(d)** The two assumptions that matter most: (1) the **ice isotopic composition
is constant** and equal to $-35$‰, whereas real ice sheets fractionate
differently as they grow and their marginal and basal ice has a different
composition; and (2) **ocean temperature does not change**, whereas
foraminiferal carbonate records a temperature-dependent fractionation that cannot
be separated from the ice-volume signal in a single record.

---

## ★★4 — The subsurface thermal transient

**(a)** $2\sqrt{\alpha t} = 2\sqrt{(32.47)(15000)} = 2\sqrt{4.8705\times10^{5}}
= 2(697.85) = 1395.7$ m.

**(b)** At 400 m:
$\mathrm{erfc}(400/1395.7) = \mathrm{erfc}(0.28659) = 0.68525$, so
$T = -7(0.68525) = -4.797$ K.
At 800 m: $\mathrm{erfc}(0.57319) = 0.41759$, so $T = -2.923$ K.

**(c)** $2\sqrt{\alpha(1000)} = 360.37$ m;
$\mathrm{erfc}(200/360.37) = \mathrm{erfc}(0.55499) = 0.43253$, so
$T = -7(0.43253) = -3.028$ K.

**(d)** The 15 ka transient has a diffusion length of 1.40 km, so a heat-flow
determination in the top kilometre is contaminated and so is one at 800 m
($-2.9$ K of a $-7$ K step is 42 per cent of the full anomaly at the surface).
A determination below about 2 km is essentially unaffected. The 1 ka event is not
detectable below a few hundred metres. The rule is: **a transient matters over
depths comparable with its diffusion length, and nowhere else.**

---

## ★★5 — Heat-flow bias

**(a)** $q = k\,\partial T/\partial z = 2.5 \times 0.030 =
0.075$ W m⁻² $= 75.0$ mW m⁻².

**(b)** With $z = 500$ m, $t = 10^{5}$ yr and $\alpha = 32.47$ m² yr⁻¹:
$\exp(-z^{2}/4\alpha t) = \exp(-2.5\times10^{5}/1.2988\times10^{7}) =
\exp(-0.019248) = 0.98094$, and
$\sqrt{\pi\alpha t} = \sqrt{1.02003\times10^{7}} = 3193.8$ m. So

$$\frac{\partial T}{\partial z} = \frac{-\Delta T\,e^{-z^{2}/4\alpha t}}
{\sqrt{\pi\alpha t}} = \frac{(5)(0.98094)}{3193.8} = +1.536\times10^{-3}\ \mathrm{K\,m^{-1}},$$

i.e. $+1.5357$ K km⁻¹. Note the sign: the derivative of
$\Delta T\,\mathrm{erfc}(u)$ is $-(\Delta T/\sqrt{\pi\alpha t})e^{-u^{2}}$, so a
past **cooling** ($\Delta T < 0$) gives a **positive** gradient anomaly.

**(c)** $\Delta q = k\Delta(\partial T/\partial z) = 2.5 \times 1.5357\times10^{-3}
= 3.84\times10^{-3}$ W m⁻² $= +3.84$ mW m⁻², which is **+5.12 per cent** of
75.0 mW m⁻². The uncorrected measurement reads **high** (78.8 mW m⁻² instead of
75.0), so the palaeoclimate correction *lowers* the inferred heat flow.

**(d)** The correction removes from each site the transient that its own surface
history implies. Because the surface history differs from place to place — an
area that was ice-covered has a different history from one that was not, deglaciation
timing varies, and vegetation and snow cover change the effective surface
temperature — the size of the correction varies spatially. An uncorrected map
therefore contains a smooth, geographically organised anomaly that has nothing to
do with the crustal heat flow, and which is easily mistaken for a real geothermal
anomaly.

---

## ★★6 — High-latitude summer insolation

**(a)** At 75°N, $\lambda = 90^\circ$: the demo reports **505.86** W m⁻² for
$\varepsilon = 23.44^\circ$ and **527.36** W m⁻² for $\varepsilon = 24.5^\circ$.

**(b)** $100(527.36 - 505.86)/505.86 = +4.25$ per cent. (For the 65°N case the
demo reports $+8.96$ per cent between 22.0° and 24.5°, a larger sensitivity
because the lower latitude also passes through the polar-day condition at high
obliquity.)

**(c)** $S_0/4 = 340.25$ W m⁻², unchanged. The global annual mean is invariant;
only the distribution moved.

**(d)** A glacier grows or shrinks according to whether summer melt removes the
winter snow. A change that increases the *seasonal contrast* — warmer, longer
summers but also colder, longer winters with more snowfall — can leave the
accumulation area larger than the ablation area even though the annual energy is
unchanged, if the summer warming is not enough to melt the extra snow. The
Milankovitch argument is therefore a statement about the *seasonal timing* of
insolation at a latitude where snow survives, and about the feedbacks (albedo,
ice elevation, ocean circulation) that amplify a small forcing.

---

## ★★★7 — Reading the demonstration

Quoted output from `quaternary_climate_demo.py`:

**(a)** Daily insolation, and the annual mean in brackets: 0°N — 436.2, 384.5,
430.2, 410.5 (415.5); 30°N — 377.8, 474.4, 372.6, 226.9 (362.9); 45°N — 308.5,
483.0, 304.2, 120.3 (303.8); 65°N — 184.4, 477.5, 181.8, 3.1 (209.6); 75°N —
112.9, 505.9, 111.3, 0.0 (181.3).

**(b)** 340.1940, 340.2036 and 340.2036 W m⁻²; $S_0/4 = 340.2500$ W m⁻².

**(c)** 454.58 (22.0°), 470.36 (23.0°) and 495.33 (24.5°) W m⁻²; the extremes
differ by $+8.96$ per cent.

**(d)** 65°N June and 65°S December: 493.62/493.62 at $\varpi = 0^\circ$;
542.99/444.26 at 90°; 493.62/493.62 at 180°; 444.26/542.99 at 270°. The
hemispheres are in antiphase.

**(e)** Sea-level equivalents 3.810, 10.161 and 31.752 m; isotope shifts 0.0361,
0.0964 and 0.3030‰.

**(f)** Diffusion lengths: 36.0 m (10 yr), 114.0 (100 yr), 360.4 (1 kyr), 1139.6
(10 kyr), 3603.7 (100 kyr), 11395.9 m (1 Myr). Anomalies for a $-5$ K step: at
250 m, $-0.010$ (100 yr), $-1.633$ (1 kyr), $-3.782$ (10 kyr), $-4.609$ K
(100 kyr); at 1000 m, $-0.000$, $-0.000$, $-1.073$, $-3.474$ K.

**(g)** $+1.5357$ K km⁻¹, i.e. $+5.12$ per cent of 75.0 mW m⁻².

**(h)** The daily and annual insolation, the sea-level equivalent, the isotope
shift from the one-box balance and the thermal transient are **derivations** from
stated formulas. The global-mean values, obliquity sensitivities and precession
table are **model results** that depend on the declared orbital configuration
($e$, $\varepsilon$, $\varpi$) and on the first-order distance factor; they would
change if a full orbital solution were used. The statement that a given insolation
change *caused* a glaciation is an **inference**, and it cannot be established
from this arithmetic at all: it requires a dated record and a demonstration that
the record leads or follows the forcing consistently.

---

## ★★★8 — Interpretation and its limits

**(a)** From ★3(c), 1.0‰ corresponds to about 105 m of sea-level change. Two
reasons the true change could differ by tens of metres:

1. **A temperature component.** Benthic foraminiferal $\delta^{18}\mathrm{O}$
   contains a deep-water temperature signal, and part of a 1.0‰ shift can be
   temperature rather than ice. If 0.2‰ of it is temperature, the sea-level
   estimate is wrong by about 21 m.
2. **A non-constant ice composition, and deep-water mass reorganisation.** The
   effective $\delta_i$ of the ice that grew or melted depends on where it grew,
   and a change in the proportion of northern-source versus southern-source deep
   water changes the $\delta^{18}\mathrm{O}$ of the water in which the foraminifera
   grew, without any change in sea level.

**(b)** Three alternative explanations for an apparent 2 K surface warming over
150 years, and the observation that would rule each out:

1. **Groundwater advection or a changing water table.** Moving water carries heat
   and produces a curved profile that mimics a surface change. Ruled out by a
   measured temperature–depth profile with no curvature at depths where the
   advective signal would be expected, or by an independent piezometric record
   showing stability.
2. **A change in surface cover or land use** (deforestation, urbanisation,
   snow-cover change) rather than air temperature. Ruled out by comparing with a
   nearby station record of air temperature and with a land-use history.
3. **A measurement artefact** — borehole fluid convection, a disturbed annulus, or
   an incorrect thermal conductivity used in converting gradient to temperature
   anomaly. Ruled out by repeat logging, by a calibrated conductivity profile, and
   by agreement between two holes in the same area.

**(c)** The two model inputs are (1) the **age** of the moraine from the dated
sample and the dating method's assumption, and (2) the **equilibrium-line
depression** model that converts the moraine elevation into a change in
equilibrium-line altitude, which requires an assumed lapse rate and an assumed
accumulation–ablation geometry. A single moraine cannot constrain the *second*
one: one elevation fixes a single point on the ELA, whereas a temperature
conclusion needs the ELA reconstruction to be tied to a precipitation (or
accumulation) assumption that only a *set* of moraines at different elevations and
aspects can test.

**(d)** The same transient is a signal when the target *is* the surface history:
then the temperature profile is the measurement and the unknown is the past
climate. It is a correction when the target is the steady-state heat flow: then
the surface history is a nuisance parameter that must be removed to recover the
quantity of interest. Nothing in the physics differs; what differs is which
quantity is treated as known and which is estimated — that is, which parameter is
the target and which is the nuisance.
