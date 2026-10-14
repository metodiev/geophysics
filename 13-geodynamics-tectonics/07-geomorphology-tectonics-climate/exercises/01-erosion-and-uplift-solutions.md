# Solutions — 13-07-01 Erosion, Uplift and Thermochronology

> **Read after attempting the exercises.** Numbers were computed with the same
> formulas as the lesson's demonstration.

Lesson: [01 Erosion, Uplift and Thermochronology](../01-erosion-and-uplift.md).

---

## ★1 — Péclet number

$E = 0.3$ mm/yr $= 3.0\times10^{-4}$ m/yr. $\kappa = 1.0\times10^{-6}$ m²/s
$= 1.0\times10^{-6}\times3.1557\times10^{7} = 31.56$ m²/yr.

$$Pe = \frac{EL}{\kappa} = \frac{3.0\times10^{-4}\times3.5\times10^{4}}{31.56}
= \frac{10.5}{31.56} = \mathbf{0.333}.$$

Advection matters but does not dominate: the geotherm is perturbed by of order
$Pe/2 = 17\%$ relative to the conductive profile.

---

## ★2 — Mid-layer temperature at $Pe = 1$

$$\frac{1-e^{-0.5}}{1-e^{-1}} = \frac{1-0.6065}{1-0.3679} = \frac{0.3935}{0.6321}
= 0.6225,$$

$$T(L/2) = 10 + 1340\times0.6225 = 10 + 834.2 = \mathbf{844.2\ °C}.$$

For comparison the conductive value $(Pe = 0)$ would be
$10+1340\times0.5 = 680$ °C: exhumation at $Pe = 1$ raises the mid-layer
temperature by 164 °C, which is the effect that makes the closure isotherm shallower.

---

## ★3 — The three words

**Rock uplift:** the vertical displacement of a rock parcel relative to the geoid.
**Surface uplift:** the change in the mean elevation of the Earth's surface.
**Exhumation:** the thickness of rock removed from above a parcel, i.e. the
integral of erosion plus the change in surface elevation.

A thermochronometer measures **cooling**, and in a steady thermal state that
converts to exhumation; it does not measure either uplift.

---

## ★4 — Exhumation rate from one age

$$\text{rate} = \frac{z_c}{t} = \frac{4.0\times10^{3}\ \mathrm{m}}{8.0\times10^{6}\ \mathrm{yr}}
= 5.0\times10^{-4}\ \mathrm{m/yr} = \mathbf{0.5\ mm/yr}.$$

---

## ★5 — Age–elevation slope

The higher sample is 1.5 km further up, i.e. 1.5 km closer to the surface, so its
depth below the closure isotherm is $4.0-1.5 = 2.5$ km:

$$\text{slope} = \frac{8.0-2.0\ \mathrm{Ma}}{4.0-2.5\ \mathrm{km}} = \frac{6.0}{1.5}
= 4.0\ \mathrm{Ma/km} \quad\Longrightarrow\quad
E = \frac{1}{4.0\ \mathrm{Ma/km}} = 0.25\ \mathrm{km/Ma} = 0.25\ \mathrm{mm/yr}.$$

This disagrees with ★4 (0.5 mm/yr) because ★4 used the *closure depth* implied by
a supposed steady state, while ★5 uses the observed ages: with the two ages given,
the data imply 0.25 mm/yr and therefore a closure depth of
$0.25\ \mathrm{mm/yr}\times8.0\ \mathrm{Ma} = 2.0$ km, not 4.0 km. The lesson's
point is exactly this: a single age gives a rate only if $z_c$ is known, whereas
two ages give it without knowing $z_c$ at all. (The problem as posed is
deliberately inconsistent to make that concrete.)

---

## ★6 — Apparent ages at the closure isotherm

At the closure isotherm the depth is $z_c$ and the age is $z_c/E$: 4.35/0.5 =
8.70 Ma and 2.21/2.0 = 1.105 Ma. The ratio of the ages is
$8.70/1.105 = 7.87$ against the inverse ratio of the rates $2.0/0.5 = 4.00$.
The ages do not scale inversely with rate because the closure depth *itself*
shrinks as the rate rises (from 4.35 to 2.21 km, a factor 1.97). The measured
lesson values are 8.69 and 1.10 Ma, giving the ratio 7.9 ✓.

---

## ★7 — Two-stage history

The break occurs at the depth exhumed during the first phase:
$0.2\ \mathrm{mm/yr}\times15\ \mathrm{Myr} = 3.0$ km below the closure isotherm.
Below the break the slope is $1/0.2 = 5.0$ Ma/km (measured: 5.000 ✓); above it
$1/1.0 = 1.0$ Ma/km (measured: 1.000 ✓). A study that samples only above the
break infers 1.0 mm/yr and calls it "the present rate", which happens to be right;
one that samples only below infers 0.2 mm/yr and calls it the present rate, which
is wrong by a factor of five.

---

## ★8 — Topographic bias

$k = 2\pi/30\ \mathrm{km} = 2.094\times10^{-4}$ m$^{-1}$,
$kz_c = 2.094\times10^{-4}\times4350 = 0.911$, $e^{-kz_c} = 0.402$.

$$\Delta T = A\Gamma e^{-kz_c} = 1500\times0.006\times0.402 = 3.62\ \mathrm{°C},$$

$$\Delta z = \frac{\Delta T}{\mathrm{d}T/\mathrm{d}z}
= \frac{3.62}{0.04222} = 85.7\ \mathrm{m}, \qquad
\Delta t = \frac{85.7}{0.5\times10^{-3}\ \mathrm{m/yr}} = 1.71\times10^{5}\ \mathrm{yr}
= 0.171\ \mathrm{Ma}.$$

**Is it detectable?** The ages at this rate are of order a few Ma to tens of Ma;
0.171 Ma is 5% of a 3.4 Ma age and 1% of a 17 Ma age. Against a 5% analytical
uncertainty, the bias is marginal at short ages and negligible at long ones — but
it is *systematic* with elevation, so it biases a slope rather than merely adding
scatter: for a 2 km elevation range the introduced age difference is
$\sim2\times0.17 = 0.34$ Ma, which is 3.4% of the time span for a 0.5 mm/yr
exhumation over 2 km (4 Ma). That is comparable with the analytical uncertainty
and must be modelled, not ignored.

---

## ★9 — Sampling to resolve two rates

**Strategy.** Collect a vertical profile through at least 3 km of relief with
8–12 samples, densest where the age–elevation relation might break, plus samples
from several *horizontal* transects at different elevations to test whether the
slope varies laterally. Plot age against elevation *and* against $\chi$-like
coordinates (for a river profile) and against depth below the closure isotherm;
fit piecewise-linear segments rather than a single line.

**Why.** The break in slope sits at the depth exhumed during the earlier phase
(3 km in ★7), so relief of 3–4 km is needed to bracket it. A single line through
a two-stage history returns an average rate with a bias that grows with the
fraction of the profile above the break; two segments return both rates and their
transition depth, and the transition depth times the older rate gives the timing
of the change.

---

## ★10 — Questions for a surface-uplift claim

1. **Is the reported quantity exhumation or surface uplift?** The slope measures
   exhumation; converting to surface uplift requires the change in surface
   elevation over the same interval. *Defensible answer:* report exhumation, and
   state that surface uplift is not measured.
2. **Is the thermal steady state justified, and over what interval?** The slope
   measures a rate averaged over the ages present, not the present rate.
   *Defensible answer:* the age–elevation relation is linear over the sampled
   range, with a stated test for curvature, and the sampled ages are quoted.
3. **Was lateral transport, tilting or a changing closure temperature
   excluded?** *Defensible answer:* structural data bound rotation, and the
   closure-temperature assumption is stated with its sensitivity (the lesson
   measures a factor-of-ten range in absolute age).

**Additional observation needed.** A datum for the palaeo-surface: a marine
terrace, a dated lava flow or a palaeo-erosion surface whose present elevation is
known, or a geodetic vertical velocity. Exhumation gives the depth removed;
without an independent surface marker, the division between "the rock came up" and
"the surface went down" cannot be made.
