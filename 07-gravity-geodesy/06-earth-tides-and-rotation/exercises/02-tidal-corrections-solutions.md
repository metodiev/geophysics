# Solutions — 07-06-02 Tidal Corrections in Precise Measurements

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values or stated standard constants.

Lesson: [02 Tidal Corrections](../02-tidal-corrections.md).

---

## ★1 — Simple correction at $60^\circ$N

$$\text{amplitude} = 95.11\cos^{2}60^\circ = 95.11 \times 0.2500
= 23.778\ \mathrm{\mu Gal}.$$

Ratio to a $20\ \mathrm{\mu Gal}$ target: $23.778/20 = 1.19$, so the tide is
about $19\%$ larger than the target.

**Required accuracy for a $1\ \mathrm{\mu Gal}$ residual:**
$1/23.778 = 4.2\%$. Note that the *relative* requirement is looser at high
latitude simply because the tide is smaller there — which is why surveys at high
latitude can sometimes survive a cruder tide model, and why the same model fails
at the equator.

---

## ★2 — Another $\delta$

$$\delta' = 1 + 0.6140 - 1.5(0.3020) = 1 + 0.6140 - 0.4530 = 1.1610 .$$

Relative to $\delta = 1.1530$:

$$\frac{\delta' - \delta}{\delta} = \frac{0.0080}{1.1530} = +0.694\%,$$

so a fitted M2 amplitude of $42.0\ \mathrm{\mu Gal}$ becomes
$42.0 \times 1.00694 = 42.29\ \mathrm{\mu Gal}$, a change of
$+0.29\ \mathrm{\mu Gal}$.

**Comment.** The change here is larger than in the lesson's example because
$h_2$ rose by $0.0050$ while $k_2$ *fell* by $0.0020$, and the two enter with
opposite signs: $\Delta\delta = \Delta h_2 - 1.5\Delta k_2
= +0.0050 + 0.0030 = +0.0080$. A change in one parameter can be masked by a
change in the other, which is why $h_2$ and $k_2$ cannot both be determined from a
gravity tide alone.

---

## ★3 — Barometric effect in a 4-hour occupation

$$\Delta g_{\text{atm}} = (-0.30\ \mathrm{\mu Gal\,hPa^{-1}})(-8\ \mathrm{hPa})
= +2.40\ \mathrm{\mu Gal}.$$

Comparison with the M2 amplitude at $45^\circ$N: $2.40/42.4 = 5.7\%$.

**Is that large?** Not compared with the tide, but it is $24\%$ of a
$10\ \mathrm{\mu Gal}$ target. And unlike the tide, the pressure change is
*unpredictable*, so it cannot be modelled in advance — it must be measured (a
barometer at the station) and applied. This is the correction most often omitted
in student surveys, and it is the one that produces a "weather-dependent anomaly".

---

## ★4 — Which latitudes a four-constituent model serves

| latitude | four-constituent rms error ($\mathrm{\mu Gal}$) | fraction of a $1\ \mathrm{\mu Gal}$ budget |
|---|---|---|
| $0^\circ$ | $8.208$ | $8.2\times$ over |
| $30^\circ$ | $4.398$ | $4.4\times$ over |
| $45^\circ$ | $5.590$ | $5.6\times$ over |
| $60^\circ$ | $10.145$ | $10.1\times$ over |

**No latitude is served.** The four-constituent model exceeds a
$1\ \mathrm{\mu Gal}$ budget by a factor of $4$–$10$ everywhere, and its error is
*worst* at $60^\circ$N (not at the equator) because that is where the diurnal
species is largest.

**Implication for a global microgravity survey:** a four-constituent model is
never sufficient at the microGal level. A production analysis needs the full
constituent set (including P1, K2, the elliptic terms and, at coastal sites, a
load model), applied with the *same* algorithm at every station so that the
residual error is systematic and cancels in differences between nearby stations.
That last point is the practical resolution: relative surveys can tolerate a
correlated error, because the target is a *difference* between neighbouring
stations taken within a short time, where the tide error is nearly common.

---

## ★5 — A $20\%$ load with a $60^\circ$ lag

$$A_{\text{obs}} = \left|A_{\text{body}}\left(1 + 0.20e^{-i60^\circ}\right)\right|
= A_{\text{body}}\left|1 + 0.1000 - 0.1732i\right|
= A_{\text{body}} \times 1.1136 .$$

So the fitted M2 amplitude grows by **$11.36\%$**, not by $20\%$ and not by zero:
the vector sum of a $20\%$ addition at $60^\circ$ has magnitude
$\sqrt{(1.10)^{2} + (0.1732)^{2}} = 1.1136$.

**Phase of the result:** the load rotates the constituent by
$\arctan(-0.1732/1.100) = -8.95^\circ$ relative to the body tide. So a load
changes not only the amplitude but the *apparent phase*, and a phase anomaly at a
coastal station is as diagnostic of the load as an amplitude anomaly.

**Contrast with the $180^\circ$ case:** a $15\%$ load exactly out of phase gives
$|1 - 0.15| = 0.85$, i.e. a $15\%$ *reduction*. The phase of a load determines
whether it adds or subtracts, which is why a load model must predict phase as
well as amplitude.

---

## ★6 — The possible range of the true drift

The fitted drift is $5.5\ \mathrm{\mu Gal\,h^{-1}}$, and a $10\%$ tide-model error
contributes approximately $\pm2.6\ \mathrm{\mu Gal\,h^{-1}}$. So the true drift
lies in

$$\left[5.5 - 2.6,\; 5.5 + 2.6\right] = \left[2.9,\; 8.1\right]\
\mathrm{\mu Gal\,h^{-1}}$$

if the tide-model error is the only systematic term and is bounded by $10\%$ —
a range of almost a factor of three, which is useless for a tie correction.

**What would resolve it:** measuring the drift *independently* of the tide. Two
standard routes:

1. **Repeat the same loop with a phase-shifted tide.** Two loops at different
   tidal phases give two equations in (drift, tide-error), which can be solved
   provided the tidal phases differ enough — the separation is limited by the
   M2 period, so loops separated by $\sim3\ \mathrm{h}$ are already useful.
2. **Occupy a station continuously for $24$–$25\ \mathrm{h}$ (a "tidal day").**
   The tide completes a full cycle, so a constant drift and the tidal amplitude
   are separable by the shape of the record, not by the model. This is the
   standard method and it converts the problem from modelling to measurement.

Both routes replace a model error with a measurement, which is always the
preferable trade when it can be afforded.

---

## ★7 — Separating body tide, ocean load and lateral structure (specification)

1. **Synthetic truth.** (a) Body tide from the simplified ephemeris of lesson 01;
   (b) an ocean load computed from a synthetic global ocean-tide model
   (a spherical-harmonic field with a stated amplitude and a $30^\circ$ lag in
   the deep ocean and a larger, phase-shifted response on the shelf);
   (c) a lateral-structure anomaly localised within a stated radius of one
   station, produced by a synthetic density contrast at a stated depth, so that
   its signal is known exactly.
2. **Network geometry.** Five stations: two coastal with different aspect (open
   ocean to the east *vs* to the west), one inland in the anomaly's centre, one
   inland far from the anomaly, one island "far-field". This is the minimum set
   that breaks the degeneracies: coastal pairs separate load geometry, inland
   pairs separate structure.
3. **Forward operator.** Body + load + structure, at each station, as a function
   of time, sampled as in the demonstration.
4. **Analysis.** Fit the four main constituents at each station, then solve
   jointly for (i) the load model's scale and phase, (ii) the structure
   anomaly, allowing the Earth-response parameters to float within a stated
   prior.
5. **Diagnostic.** The posterior or least-squares uncertainty on the structure
   amplitude compared with the case where the load is *assumed* exact. The ratio
   quantifies how much the network geometry buys.
6. **Remaining degeneracy.** A load that is spatially uniform across the network
   is indistinguishable from a change in the Earth-response factor $\delta$; and
   a structure anomaly beneath *both* inland stations with the same sign is
   indistinguishable from a larger-scale structure. The specification should
   state that the experiment determines only the *differences* between stations'
   responses.

---

## ★8 — Which omission dominates at which latitude, and how to falsify it

**Argument.** Three omissions are made by the simple model, with different
latitude dependences:

1. **declination modulation of the semidiurnal term**, which enters as
   $\cos^{2}\delta$ multiplying an amplitude that varies as $\cos^{2}\varphi$ —
   so its absolute error ∝ $\cos^{2}\varphi$, maximum at the equator;
2. **the solar semidiurnal term**, whose relative importance is fixed
   ($\approx46\%$ in forcing, less after geometry) and which scales with
   $\cos^{2}\varphi$ as well;
3. **the diurnal species**, which scales as $\sin 2\varphi$ and therefore
   *vanishes at the equator* and peaks at $45^\circ$.

**Prediction.** The residual of the simple model is dominated by (1)+(2) at low
latitude, where it should be largest, and by (3) at mid latitude, where it should
peak near $45^\circ$. The demonstration's numbers match: $54.94\ \mathrm{\mu Gal}$
at $0^\circ$, $48.42$ at $30^\circ$, $49.89$ at $45^\circ$ and $58.89$ at
$60^\circ$ — so there is a local maximum at the equator and a second maximum at
$60^\circ$, with a minimum near $30^\circ$–$45^\circ$ from the competition.

**Falsification.** The argument predicts that a body placed in an exactly
equatorial orbit (so the declination is identically zero) will make the simple
model *far* more accurate at the equator than at $60^\circ$; if instead the
equatorial residual stayed largest, argument (1) would be wrong and the error
would have to come from a term with a different latitude dependence — for
instance a mis-set amplitude constant, which is latitude-independent. **A
prediction that does not name its own falsification is a restatement of the
data.**
