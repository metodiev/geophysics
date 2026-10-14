---
id: 07-04-02
title: "Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models"
level: graduate
prereqs: ["07-04-01", "07-01-03"]
tags: [gravity, geodesy, heights, geoid, levelling, geopotential]
---

# Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models

All models and data in this module are SYNTHETIC, with one exception: the
normal-gravity values below come from the standard closed-form Somigliana formula
evaluated with WGS 84 defining constants. Every levelling line, gravity reading,
loop and geoid undulation is a chosen teaching value.

## Learning objectives

By the end of this lesson you will be able to:

1. **Evaluate** normal gravity on an ellipsoid with the Somigliana formula and
   **state** its variation from equator to pole in mGal.
2. **Compute** geopotential numbers from levelling increments and measured
   gravity, with units checked.
3. **Distinguish** orthometric, dynamic, normal and ellipsoidal heights, and
   **compute** the differences among them for a given line.
4. **Explain** why the difference between "summing increments" and "orthometric
   height" is a covariance, not a magnitude, and **demonstrate** a case where it
   vanishes.
5. **Compute** $h = H + N$ and **separate** the ellipsoidal, orthometric and
   geoid contributions to a height difference.
6. **Interpret** loop misclosure, distinguishing random from systematic
   components.
7. **State** which height system a number belongs to before using it in gravity
   reduction or in a climate study.

## Prerequisites

- [01 Geodetic Datums, Ellipsoids and Coordinate Frames](01-geodetic-datums.md) —
  the ellipsoid, its curvatures and $h = H + N$.
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md) —
  normal gravity as a defined function of latitude.

## 1. The problem with "height"

Height is a potential difference in disguise. Water flows from high potential to
low, a levelling instrument measures vertical increments, and GNSS measures a
geometric distance from an ellipsoid. These three are different quantities, and
their differences are centimetres to metres — larger than many of the effects
people use heights to study.

The organising quantity is the **geopotential number**

$$C(P) = W_0 - W(P) = \int_{A}^{P} g\,\mathrm{d}n
\;\approx\;\sum_i g_i\,\Delta n_i
\qquad (\mathrm{m^{2}\,s^{-2}}),$$

where $\mathrm{d}n$ is the increment measured upward along the vertical. $C$ is
independent of the path, because the potential is; that path-independence is
exactly why levelling must be weighted by measured gravity.

## 2. Normal gravity

Normal gravity on the ellipsoid is the closed-form Somigliana expression

$$\gamma(\varphi) = \frac{\gamma_e\left(1 + k\sin^{2}\varphi\right)}
{\sqrt{1-e^{2}\sin^{2}\varphi}},
\qquad \gamma_e = 9.7803253359\ \mathrm{m\,s^{-2}},\;
k = 0.00193185265241,$$

with $\gamma_e$ and $k$ defining constants of WGS 84. The demonstration prints:

| $\varphi$ (deg) | $\gamma$ ($\mathrm{m\,s^{-2}}$) | $\gamma - \gamma_{\text{eq}}$ (mGal) |
|---|---|---|
| 0 | 9.780325 | 0.00 |
| 15 | 9.783785 | 345.96 |
| 30 | 9.793247 | 1292.19 |
| 45 | 9.806198 | 2587.24 |
| 60 | 9.819177 | 3885.16 |
| 75 | 9.828697 | 4837.13 |
| 90 | 9.832185 | 5185.96 |

The polar/equatorial ratio is $1.005302441$: gravity is $0.53\%$ larger at the
pole. Normal gravity is a *definition* on a chosen ellipsoid; it is not a
measurement, and it is not real gravity — the difference between the two is the
gravity anomaly of [07-01-04](../01-gravity-fundamentals/04-gravity-reduction.md).

## 3. Four heights from one geopotential number

| height system | definition | unit | needs |
|---|---|---|---|
| ellipsoidal | $h$ | m | a datum and GNSS |
| orthometric | $H = C/\bar{g}$ | m | mean gravity along the plumb line |
| dynamic | $H_{\text{dyn}} = C/\gamma_{45^{\circ}}$ | m | one number: $\gamma$ at $45^{\circ}$ |
| normal | $H^{*} = C/\bar{\gamma}$ | m | mean normal gravity along the plumb line |

*Numerical example (SYNTHETIC).* A $100\ \mathrm{km}$ levelling line with a height
rise of $45.00\ \mathrm{m}$, its ends $0.90^{\circ}$ of latitude apart, a
synthetic $-40\ \mathrm{mGal}$ gravity anomaly in the middle, and
geopotential number

$$C = 441.287230\ \mathrm{m^{2}\,s^{-2}},\qquad
\bar{g} = 9.806388\ \mathrm{m\,s^{-2}} .$$

Then

- orthometric: $H = C/\bar{g} = 44.999978\ \mathrm{m}$,
- dynamic: $H_{\text{dyn}} = C/\gamma_{45^{\circ}} = 45.000849\ \mathrm{m}$
  ($+0.87\ \mathrm{mm}$),
- normal: $H^{*} = C/\gamma(\varphi) = 44.997482\ \mathrm{m}$
  ($-2.50\ \mathrm{mm}$),
- the plain sum of increments: $45.000000\ \mathrm{m}$ ($+0.02\ \mathrm{mm}$).

The spread is $0.02$ to $2.5\ \mathrm{mm}$ on a $45\ \mathrm{m}$ rise — $0.5$ to
$56$ parts per million. **Scale it:** a $1000\ \mathrm{m}$ relief gives $0.5$ to
$56\ \mathrm{mm}$, and a $4\ \mathrm{km}$ mountain pass $2$ to $220\ \mathrm{mm}$.
The choice of system is invisible in a car park and decisive in a mountain range.

## 4. Ignoring gravity: a covariance, not a magnitude

The difference between the plain increment sum and the orthometric height is

$$\sum_i \Delta n_i - \frac{C}{\bar{g}}
\;\approx\; \frac{1}{\bar{g}}\sum_i \left(g_i - \bar{g}\right)\Delta n_i ,$$

which is the **covariance between the gravity variation and the height gain**. A
uniform gravity offset cancels exactly; only the part of the gravity field that
correlates with the climb survives. The demonstration makes this visible with two
$45\ \mathrm{m}$ climbs on the same line:

| height profile | error of the plain sum (mm) |
|---|---|
| steady climb with the latitude-varying gravity | $+0.022$ |
| the same climb confined to the $40\ \mathrm{mGal}$ anomaly | $+0.360$ |

In the first case the gravity excess is antisymmetric about the midpoint while the
height gain is not, and the first-order term cancels — a symmetric example can
hide a real effect. Both numbers are small here because the synthetic line has
only $45\ \mathrm{m}$ of relief; with $1\ \mathrm{km}$ against the same anomaly
the covariance term reaches about $40\ \mathrm{mm}$. The rule that follows is not
"weight the levelling in mountains" but **weight it always**, because you cannot
know in advance how the terrain and the gravity field correlate.

## 5. Loop closure

A levelling loop must close: the geopotential returns to its starting value. The
misclosure is therefore a measurement diagnostic. In the demonstration's
synthetic loop of $60$ setups whose true increments sum to zero, with
$0.50\ \mathrm{mm}$ random error and $0.10\ \mathrm{mm}$ systematic error per
setup:

| quantity | value |
|---|---|
| raw misclosure | $+4.460\ \mathrm{mm}$ |
| expected from noise, $1\sigma$ | $3.873\ \mathrm{mm}$ |
| expected from the systematic part | $6.000\ \mathrm{mm}$ |
| systematic part estimated from the closure | $0.074\ \mathrm{mm}$ per setup |
| scatter about the trend after adjustment | $0.510\ \mathrm{mm}$ per setup |

The diagnostic rule is the one worth remembering: **a misclosure that grows in
proportion to the number of setups is systematic** — an instrument or procedure
effect, which repeating the loop does not remove — **while a misclosure that grows
as the square root of the number of setups is random**, and does average away.
Here the raw closure of $4.460\ \mathrm{mm}$ sits between the two predictions, and
only the scaling test tells which part dominates.

## 6. Heights and the geoid

For any station, $h = H + N$. Three consequences matter in practice:

1. **A height difference is not a potential difference.** Levelling gives
   $\Delta H$; GNSS gives $\Delta h$; the two differ by $\Delta N$, which can
   reach metres over hundreds of kilometres.
2. **A national height network is a potential network.** Benchmarks carry
   orthometric (or normal) heights tied to a geopotential datum, and converting
   one to the other requires the gravity field.
3. **The geoid model is usually the limiting error.** In the demonstration's line
   a geoid slope of $30\ \mathrm{mm\,km^{-1}}$ produced a $1.200\ \mathrm{m}$
   difference over $40\ \mathrm{km}$, and using a single mean $N$ left
   $600\ \mathrm{mm}$ of error at the ends. The undulations there are synthetic —
   the geometry is the point, not the numbers.

## 7. Worked example

*A $50\ \mathrm{km}$ levelling line climbs $800\ \mathrm{m}$. The mean gravity
along the line is $9.8040\ \mathrm{m\,s^{-2}}$ and normal gravity at the mean
latitude is $9.8062\ \mathrm{m\,s^{-2}}$.*

1. **Geopotential number.** Approximating
   $C \approx \bar{g}\,\Delta h = 9.8040\times800 = 7843.2\ \mathrm{m^{2}\,s^{-2}}$.
2. **Orthometric height.** $H = C/\bar{g} = 800.00\ \mathrm{m}$ by construction —
   so this route only shows the definition. The informative comparison is with
   the *dynamic* height:
   $H_{\text{dyn}} = C/\gamma_{45^{\circ}} = 7843.2/9.806198 = 799.82\ \mathrm{m}$.
   The difference, $0.18\ \mathrm{m}$, is the systematic separation of the two
   systems over $\sim800\ \mathrm{m}$ of relief.
3. **Normal height.** With $\bar{\gamma} = 9.8040$ the normal height is
   $800.00\ \mathrm{m}$ as well; a realistic calculation uses
   $\gamma(\varphi)$ varying along the line, giving a difference of the same order
   as the dynamic one.
4. **Ellipsoidal height.** With $N$ changing by, say, $+0.5\ \mathrm{m}$ between
   the two ends of the line, the GNSS height difference is
   $\Delta h = \Delta H + \Delta N = 800.00 + 0.5 = 800.5\ \mathrm{m}$. Reporting
   $800.5\ \mathrm{m}$ as "the climb" is an error of half a metre.
5. **Conclusion.** The physical statement "the line climbs $800\ \mathrm{m}$" needs
   a system; the ellipsoidal difference is a different number, and both are
   legitimate.

## 8. Assumptions and regime of validity

1. **Newtonian gravity and a static Earth.** Tides and time-variable mass change
   shift heights at the centimetre level
   ([07-06-01 Solid Earth Tides and Their Gravity Signature](../06-earth-tides-and-rotation/01-solid-earth-tides.md)).
2. **Mean gravity along the plumb line** is approximated by surface gravity.
   Between the surface and the geoid the difference is small but systematic; it is
   the reason orthometric heights are the hardest of the four to compute exactly.
3. **Orthometric corrections assume the levelling is measured along the vertical**
   and that the geoid is smooth enough locally for the correction to be
   path-independent in practice.
4. **Normal gravity is a definition.** Mixing a gravity value from a different
   ellipsoid into $\gamma$ introduces a systematic offset of up to a few mGal.
5. **The geoid model's accuracy is the height system's accuracy** when GNSS and
   levelling are combined, typically centimetres at best.
6. **Loop closure tests measure the instrument and the procedure**, not the
   reduction model — a closed loop closes for any consistent reduction.

## 9. Physical interpretation

- A height is a normalised potential: $C$ divided by a gravity value that is
  chosen for convenience. Orthometric heights divide by actual mean gravity
  (so a level surface is nearly the geoid), dynamic heights divide by one
  constant (so the numbers are comparable globally but not geometric), normal
  heights divide by normal gravity (so the numbers are computable everywhere
  without knowing the crust's density).
- The centimetre-to-metre differences between systems come from the $0.53\%$
  variation of gravity with latitude acting on a height of hundreds of metres:
  $0.005\times800 = 4\ \mathrm{m}$ would be the naive scale, reduced to metres by
  the near-cancellation of the latitude and height profiles.
- Loop closure is a conservation law test: potential differences must sum to
  zero around a closed path. Everything else in this lesson is bookkeeping about
  which normalisation you write down.
- Because $N$ is a surface with slopes of a few centimetres per kilometre, any
  product that mixes GNSS heights with levelled heights inherits the geoid
  model's errors as a *gradient*, not as a constant.

## 10. Python demonstration

`code/height_systems_demo.py` prints:

1. normal gravity at seven latitudes with the polar-equatorial difference;
2. the $100\ \mathrm{km}$ line: $C$, $\bar{g}$ and the four heights with their
   differences in millimetres;
3. the covariance demonstration with two height profiles;
4. the loop-closure experiment, with the random and systematic predictions;
5. the four legitimate heights of a single station.

All output carries units; the script exits 0 and uses
`np.random.default_rng(20261014)`.

## 11. Exercises

See
[`exercises/02-height-systems-exercises.md`](./exercises/02-height-systems-exercises.md)
and
[`exercises/02-height-systems-solutions.md`](./exercises/02-height-systems-solutions.md).

- **★** Evaluate $\gamma(0)$, $\gamma(45^{\circ})$ and $\gamma(90^{\circ})$ and
  give the difference in mGal.
- **★** Compute $C$ for a $200\ \mathrm{m}$ climb at constant
  $g = 9.81\ \mathrm{m\,s^{-2}}$, with units.
- **★★** For a line climbing $500\ \mathrm{m}$ with a $+20\ \mathrm{mGal}$
  anomaly confined to the climb, estimate the error of the plain increment sum.
- **★★** A loop of $40$ setups has a misclosure of $8\ \mathrm{mm}$. Decide
  whether it is random or systematic, and state the test.
- **★★★** Design a levelling-plus-gravity procedure that would determine
  orthometric heights to $1\ \mathrm{cm}$ over a $100\ \mathrm{km}$ line, and
  state which term in the error budget dominates.

## Mastery checkpoint

Without notes:

> A station has geopotential number $C = 1961.2\ \mathrm{m^{2}\,s^{-2}}$, and sits
> where $\gamma(\varphi) = 9.8050\ \mathrm{m\,s^{-2}}$ and
> $N = 42.0\ \mathrm{m}$.

**(a)** Compute the dynamic height, using $\gamma_{45^{\circ}} = 9.806198\
\mathrm{m\,s^{-2}}$.
**(b)** Compute the normal height.
**(c)** Compute the ellipsoidal height given an orthometric height of
$200.0\ \mathrm{m}$.
**(d)** State which of the four heights you would quote to a hydrologist and why.

## Common pitfalls

1. **Mixing height systems.** A number called "height" is meaningless without its
   system and its datum.
2. **Treating $N$ as constant.** The demonstration's error was $600\ \mathrm{mm}$
   over $40\ \mathrm{km}$.
3. **Skipping gravity weighting in levelling.** The error is a covariance with
   terrain, and it is systematic.
4. **Reading a loop misclosure as pure noise.** Its scaling with setup count is
   the diagnostic.
5. **Using normal gravity from a different ellipsoid.** A few mGal of systematic
   offset in the heights.
6. **Assuming orthometric heights are geometric.** They are not parallel to the
   ellipsoid; that is the whole reason the geoid exists.

## 12. Applications

- **National levelling networks.** Every country maintains a vertical datum in
  one of these systems, and conversions between them are a standing geodetic
  task ([07-07-02 Vertical Datum Modernisation and National Height Systems](../07-geoid-and-height-modern/02-vertical-datum-modernisation.md)).
- **Gravity reduction.** Free-air and Bouguer corrections need a consistent height
  ([07-01-04](../01-gravity-fundamentals/04-gravity-reduction.md)).
- **Flood and sea-level studies.** Mixing orthometric and ellipsoidal heights
  produces apparent trends of centimetres per year.
- **Glaciology and geodesy.** Ice-surface elevation change is measured
  ellipsoidally and interpreted physically; the distinction is not cosmetic.

## Related modules

- [01 Geodetic Datums, Ellipsoids and Coordinate Frames](01-geodetic-datums.md).
- [03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](03-gnss-positioning.md).
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md).
- [07-07-01 Determining the Geoid: Stokes, Remove-Restore, Kriging](../07-geoid-and-height-modern/01-geoid-determination.md).
- [02-08-05 Equipotential Surfaces, Geoid and Level Surfaces](../../02-physics/08-potential-theory/05-equipotentials.md).

## 13. Self-assessment checklist

- [ ] I can evaluate Somigliana normal gravity and quote its range in mGal.
- [ ] I can compute a geopotential number with units.
- [ ] I can compute all four heights for a given line and rank their differences.
- [ ] I can explain the covariance argument for gravity-weighted levelling.
- [ ] I can interpret a loop misclosure by its scaling.
- [ ] I can assemble $h = H + N$ and separate the three contributions.
