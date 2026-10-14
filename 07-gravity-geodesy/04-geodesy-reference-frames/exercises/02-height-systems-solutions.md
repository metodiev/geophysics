# Solutions — 07-04-02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [02 Height Systems](../02-height-systems.md).

---

## ★1 — Normal gravity

| $\varphi$ | $\gamma$ ($\mathrm{m\,s^{-2}}$) |
|---|---|
| 0 | 9.780325 |
| 45 | 9.806198 |
| 90 | 9.832185 |

Polar minus equatorial: $0.051860\ \mathrm{m\,s^{-2}} = \mathbf{5186.0\ mGal}$,
i.e. $\mathbf{0.530\%}$ of $g$. This is the largest single systematic in gravity
measurement, and it is why every gravimeter survey is tied to a normal-gravity
formula before any interpretation.

---

## ★2 — Geopotential number

$$C = \int g\,\mathrm{d}n \approx g\,\Delta h
= 9.81\ \mathrm{m\,s^{-2}}\times200\ \mathrm{m}
= \mathbf{1962.0\ m^{2}\,s^{-2}} .$$

Units: $\mathrm{m\,s^{-2}}\times\mathrm{m} = \mathrm{m^{2}\,s^{-2}}$, which is a
potential per unit mass — as it must be. Sanity: dividing by
$9.8\ \mathrm{m\,s^{-2}}$ returns $200\ \mathrm{m}$, the expected height scale.

---

## ★3 — The four systems

- **Ellipsoidal** $h$: geometric height above the ellipsoid; measured by GNSS;
  needs a datum.
- **Orthometric** $H = C/\bar{g}$: height above the geoid; needs the **mean gravity
  along the plumb line**, hence information about the Earth's internal density
  distribution — the hardest of the four.
- **Dynamic** $H_{\text{dyn}} = C/\gamma_{45^{\circ}}$: one constant divisor, so the
  numbers are comparable globally; not a geometric distance.
- **Normal** $H^{*} = C/\bar{\gamma}$: uses mean *normal* gravity, computable
  everywhere without knowing the crust's density; the standard choice in many
  national systems.

---

## ★4 — Dynamic and normal heights for $C = 1961.2\ \mathrm{m^{2}\,s^{-2}}$

$$H_{\text{dyn}} = \frac{1961.2}{9.806198} = \mathbf{199.9960\ m},$$

$$H^{*} = \frac{1961.2}{9.8050} = \mathbf{200.0204\ m}.$$

Difference: $H^{*}-H_{\text{dyn}} = +0.0244\ \mathrm{m} = \mathbf{24.4\ mm}$.

Interpretation: the two systems differ by whichever gravity value divides the same
potential. Here $\gamma(\varphi) = 9.8050 < \gamma_{45^{\circ}} = 9.806198$, a
$1.2\times10^{-4}$ relative difference, which on a $200\ \mathrm{m}$ height is
$24\ \mathrm{mm}$. Over a $1000\ \mathrm{m}$ height the same relative difference
gives $122\ \mathrm{mm}$ — the difference scales linearly with height, which is the
quantitative statement of §3 of the lesson.

---

## ★5 — Error from ignoring gravity on a $500\ \mathrm{m}$ climb

The error is the covariance

$$\sum\Delta n_i - \frac{C}{\bar{g}}
\approx\frac{1}{\bar{g}}\sum_i\left(g_i-\bar{g}\right)\Delta n_i .$$

With the anomaly confined to the climb, $\left(g-\bar{g}\right) \approx
+20\ \mathrm{mGal} = 2.0\times10^{-4}\ \mathrm{m\,s^{-2}}$ over the $500\ \mathrm{m}$:

$$\text{error} \approx \frac{2.0\times10^{-4}\times500}{9.8}
= 1.02\times10^{-2}\ \mathrm{m} = \mathbf{10.2\ mm}.$$

**Why a uniform offset gives zero:** if $g_i = \bar{g}$ for every increment, every
term in the sum vanishes. The error depends only on the *variation* of gravity that
correlates with the climb, not on the magnitude of gravity — which is why the
demonstration's antisymmetric latitude example produced only $0.022\ \mathrm{mm}$
while a one-sided anomaly produced $0.360\ \mathrm{mm}$ on the same line.

---

## ★6 — A loop misclosure of $8\ \mathrm{mm}$ in $40$ setups

Two hypotheses:

- **Random**, per-setup error $\sigma$: misclosure $\approx\sigma\sqrt{40} = 6.32\sigma$.
  For $8\ \mathrm{mm}$ this gives $\sigma = 1.27\ \mathrm{mm}$ per setup.
- **Systematic**, per-setup bias $b$: misclosure $= 40b$. For $8\ \mathrm{mm}$ this
  gives $b = 0.20\ \mathrm{mm}$ per setup.

**The test that settles it:** repeat the loop, or compare loops of different setup
counts. If the misclosure scales with $\sqrt{n}$ it is random; if it scales with
$n$ it is systematic. A single loop cannot distinguish $\sigma = 1.27\ \mathrm{mm}$
random from $b = 0.20\ \mathrm{mm}$ systematic — both produce $8\ \mathrm{mm}$ — so
the answer must be "undetermined from one loop", and the discriminating experiment
is the scaling test. This is precisely the demonstration's structure: it prints
both predictions ($3.873\ \mathrm{mm}$ random, $6.000\ \mathrm{mm}$ systematic) and
shows that only the scaling resolves them.

---

## ★7 — Levelling to $1\ \mathrm{cm}$ over $100\ \mathrm{km}$

**Error terms** for orthometric heights from levelling plus gravity:

| term | size over $100\ \mathrm{km}$ | how controlled |
|---|---|---|
| random levelling error | $0.5\ \mathrm{mm}\sqrt{n}$; with $1000$ setups, $\sim16\ \mathrm{mm}$ | more setups, shorter sights, repeat lines |
| systematic levelling error | $0.1\ \mathrm{mm}\times n$; with $1000$ setups, $100\ \mathrm{mm}$ | instrument calibration, two-instrument procedures, loop closure |
| gravity sampling | $\Delta g$ interpolation error, e.g. $1\ \mathrm{mGal}$ over a $5\ \mathrm{km}$ block with $100\ \mathrm{m}$ relief: $\approx0.05\ \mathrm{mm}$ per block, but systematic if unsampled | gravity readings at every $1$–$2\ \mathrm{km}$ and at every benchmark |
| mean-gravity approximation $\bar{g}\approx g_{\text{surface}}$ | $\sim0.4\ \mathrm{mGal}$ for $1\ \mathrm{km}$ of relief, i.e. $\sim0.04\ \mathrm{mm}$ per $1000\ \mathrm{m}$ of height — negligible at this target | none needed below $1\ \mathrm{cm}$ |
| datum/geoid change | metres if the reference changes | fix the datum |

**Dominant term:** the **systematic levelling error** — it grows linearly with the
number of setups, so over $100\ \mathrm{km}$ it dwarfs everything else unless the
procedure is hardened (two independent instruments, many repeats, loop closures,
and a rod-calibration protocol). A $1\ \mathrm{cm}$ target over $100\ \mathrm{km}$
is $0.1\ \mathrm{ppm}$ and is at the limit of what high-order levelling achieves.
Gravity sampling is the second term, and it is controlled by taking gravity
readings at every benchmark and at a spacing related to the terrain.

**Procedure:** spirit levelling in closed loops with two instruments, gravity at
every benchmark plus a $1$–$2\ \mathrm{km}$ profile, geopotential numbers computed
per segment, mean gravity from the measured profile, and a loop-closure budget
allocated in proportion to the square root of the number of setups (random part)
with any systematic part corrected, not distributed.

---

## ★8 — Modernising a vertical datum

**What changes.**

1. **The numbers.** Orthometric heights $H$ are replaced by ellipsoidal heights $h$
   and a geoid model $N$, with $h = H+N$. Since $N$ ranges from tens of metres to
   tens of *negative* metres depending on region, the tabulated numbers change by
   the full undulation — metres to tens of metres, not centimetres.
2. **The reference surface.** The geoid (a physical, non-analytic surface) is
   replaced by the ellipsoid (mathematical, exactly representable). Heights become
   reproducible anywhere without a levelling network.
3. **The error structure.** Levelling error (systematic, growing with distance) is
   replaced by GNSS error plus *geoid model* error — the latter now dominant and
   spatially correlated.

**Size for a mountainous country:** the change to each benchmark's number is
$N$ at that point, which varies by metres across a country (and by
$10\ \mathrm{cm}$ over tens of kilometres, as the lesson's synthetic
$30\ \mathrm{mm\,km^{-1}}$ slope shows). The change is large but *known* if the
geoid model is good.

**Calibration measurements that keep it consistent:**

1. **Collocated GNSS and levelling** on a dense, well-distributed set of
   benchmarks — the only way to evaluate the geoid model where it matters, and the
   residuals of $h-(H+N)$ are the accuracy statement.
2. **Gravity data** for the geoid model itself, especially in the mountains where
   the model is weakest.
3. **Tide gauges and repeat levelling** to tie the vertical datum to the ocean and
   to monitor subsidence, which otherwise appears as a datum change.
4. **A published transformation** (a list of old and new heights with an
   uncertainty) so that past work can be reinterpreted without distortion.

**The honest caveat:** a new datum is not more accurate everywhere; it is
*consistently* accurate, with a *stated* error budget, which is the property that
lets results be compared across a country.
