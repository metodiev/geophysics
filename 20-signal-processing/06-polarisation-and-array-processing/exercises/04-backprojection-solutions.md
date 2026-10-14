# Solutions — 20-06-04 Back-Projection Imaging of Rupture

> Read after attempting. Numbers computed. Lesson:
> [04 Back-Projection](../04-backprojection.md).

---

## ★1 — Rupture velocity from a ridge

$$\frac{\mathrm{d}\tau}{\mathrm{d}\xi} = \frac{14-6}{35-15} = \frac{8}{20}
= 0.400\ \mathrm{s\,km^{-1}}
\;\Longrightarrow\;
v_r = \frac{1}{0.400} = 2.50\ \mathrm{km\,s^{-1}} .$$

**Assumption:** the rupture velocity is **constant**, so the ridge is a straight
line through the two points. This is a physical assumption about the source, not
a data-processing choice; if the rupture accelerates, a two-point slope is an
average and the ridge should be fitted piecewise with the point-spread function
as the resolution limit.

---

## ★2 — What a 3-km spot means

The image is the true source convolved with a 4-km point-spread function. A
3-km-wide spot is narrower than the point-spread function, so it is consistent
with a **point source**. The strongest defensible claim is:

> "All the high-frequency radiation imaged by this array comes from a volume
> smaller than about 4 km; the data cannot distinguish a point source from any
> source distribution narrower than the point-spread function."

Any statement about a 3-km extent, or about where inside the spot the energy
originates, exceeds what the data support.

---

## ★3 — Two arrays disagreeing by 3 km

Candidate explanations:

1. **Different travel-time models** — the locations are conditional on the model,
   and the lesson measured a 1-km bias at 20 km from a 5% velocity error, growing
   with distance;
2. **Different frequency content** — back-projection images high-frequency
   radiation, and two arrays with different instrument responses and filters
   image different parts of the source spectrum, which can peak at different
   positions and times;
3. also possible: different array geometry and hence different point-spread
   functions, so a fixed threshold picks the peak at slightly different places.

**Observation that separates them.** Image both arrays **with the same
travel-time model and the same frequency band**. If the 3-km difference persists,
it is an array-geometry or data effect (candidate 2 or 3); if it disappears, the
discrepancy was the model (candidate 1). A second discriminating observation is
to vary only the band on one array: if the apparent position moves with the band,
the frequency effect is real and the arrays simply see different bands.

---

## ★★4 — Aperture for 1-km sub-events

The point-spread function is 2 km for the 80-km aperture. Since it scales as
$1/L$,

$$L_{\text{required}} = 80 \times \frac{2}{1} = 160\ \mathrm{km}.$$

With the existing 80-km aperture the study **cannot** resolve 1-km sub-events; no
processing can, because the resolution is set by the geometry. Doubling the
aperture halves the point-spread function to 1 km, at which point 1-km features
are exactly at the resolution limit and should be reported as "consistent with
1 km", not as a measured 1-km extent. The demonstration's table showed the
improvement saturating (2 km at both 60 and 80 km apertures) once the width
becomes comparable to the 1-km fault grid — so a real design must also refine the
grid or the gain is illusory.

---

## ★★5 — Pulse width and sub-event spacing

Sub-events are spaced along the fault by the grid, so their radiation times are
spaced by $\Delta\tau = \Delta\xi/v_r$. For them to be individually radiated
requires

$$\sigma < \frac{\Delta\xi}{v_r} = \frac{2}{3.0} = 0.667\ \mathrm{s}.$$

If the real pulse is twice that ($\sigma = 1.33\ \mathrm{s}$), the pulses
overlap, the records become a continuous smear with no distinguishable arrival
times, and the ridge is not recoverable — the demonstration found exactly this
failure when $\sigma = 0.3\ \mathrm{s}$ against a 0.4-s spacing. The remedies are
to use a higher-frequency band (where the effective pulse is shorter), to image on
a coarser grid (larger $\Delta\xi$, larger spacing), or to accept that only the
envelope of the rupture — not its sub-events — is imaged.

---

## ★★6 — Bias at 60 km

If the bias scales linearly with distance from the array centre, then at 60 km:

$$\text{bias} = 1\ \mathrm{km} \times \frac{60}{20} = 3\ \mathrm{km}$$

for the same 5% velocity error.

**Assumption:** the location bias is proportional to distance, because a velocity
error maps a distance $R$ into an apparent distance $R\,v_{\text{assumed}}/
v_{\text{true}}$, so $\Delta R = R(\delta v/v)$. The lesson's measurements are
consistent with this: a $-5\%$ error moved the 20-km sub-event by $-1\ \mathrm{km}$
($5\%$ of 20 km exactly), and a $-10\%$ error by $-2\ \mathrm{km}$.

**Test:** repeat the demonstration's point-source experiment at
$\xi = 40$, $60$ and $80$ km with the same four velocity models and check the bias
against $0.05\,\xi$. If the measured bias is proportional to $\xi$, the scaling is
confirmed and the 3-km estimate stands; if it saturates (because the far end of
the fault is poorly illuminated by the array), the estimate is an upper bound and
should be reported as such.

---

## ★★★7 — A design for a 100-km rupture

**Array.** Aperture 80 km (20–40 stations) on a two-dimensional layout if the
slip direction is unknown; a line along the expected strike if it is known. The
point-spread function for an 80-km aperture from the lesson's table is 2 km along
strike — adequate for a 100-km rupture whose interesting features are tens of
kilometres.

**Sampling.** High enough that the shortest source pulse is oversampled: for
expected pulses of $\sim0.2$–$0.5$ s, 50–100 Hz. (The lesson used 50 Hz for a
0.2-s pulse: about 10 samples per pulse.)

**Fault grid.** 1 km along strike, i.e. five times finer than the point-spread
function. Coarser than the point-spread function is wasteful; much finer is
misleading, because the image cannot be sharper than the point-spread function.

**Travel-time model requirements.** The bias is the dominant error, so the
velocity model must be good to a few per cent along the source–receiver paths,
and the station positions surveyed. Report the sensitivity explicitly, as the
lesson did, rather than quoting a single location.

**The design supports:**

- a space–time map of high-frequency radiation, i.e. when each part of the fault
  radiated;
- the average rupture velocity along strike and along dip, from the ridge slope,
  provided the ridge is straight to within the point-spread function;
- a comparison of the rupture direction with aftershock locations or a finite-fault
  inversion.

**The design does not support:**

- a **slip distribution**. Back-projection images radiated high-frequency energy,
  which is not proportional to slip; a study that reports the bright spot as the
  "asperity" with a slip value has left the method's domain;
- an absolute hypocentre to better than a few kilometres, because the location is
  conditional on a velocity model with a measured 1–3 km sensitivity.

---

## ★★★8 — Distinguishing propagation from an extended simultaneous source

**Observable difference.** A propagating rupture produces a **ridge in the
$(\xi,\tau)$ image whose slope is $1/v_r$** and whose apparent $(\xi,\tau)$
positions **move with frequency in a specific way**: dispersion-free radiation
from a moving front has a kinematic delay that is independent of the band, so the
ridge slope is the same at 1 s and 0.25 s period. A spatially extended source
radiating simultaneously has **no ridge**: its image is confined to a narrow band
of $\tau$ at fixed $\xi$ (all points radiate within the pulse width), so the
image extent along strike is set by the fault extent and the point-spread
function, as the demonstration's 39-km result showed.

**The test.**

1. Compute the image in two frequency bands, e.g. 0.5–1 Hz and 2–4 Hz.
2. Measure the slope of the ridge in each band and the total $\tau$-extent of the
   imaged energy.
3. **Propagation predicts** the same ridge slope in both bands, and a $\tau$
   extent at each $\xi$ comparable to the pulse width.
4. **A simultaneous extended source predicts** no systematic slope, a $\tau$
   extent comparable to the point-spread function's time width at *every* $\xi$,
   and no band dependence of the pattern.

**A caution.** A rupture that is both propagating *and* has a long source pulse
(the lesson's $\sigma > \Delta\xi/v_r$ case) produces an intermediate image that
mimics a simultaneous source. The test therefore has to be run after checking the
pulse-spacing condition of ★5, not instead of it.
