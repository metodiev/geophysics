# Solutions — 11-04-03 Microseismic Monitoring of Geothermal Fields

> **Read after attempting the exercises.** Numbers were computed rather than
> estimated; assumptions are labelled.

Lesson: [03 Microseismic Monitoring of Geothermal Fields](../03-microseismic-geothermal.md).

---

## ★1 — Moment to magnitude

$$M_w = \frac{2}{3}\left(\log_{10}M_0 - 9.1\right)
= \frac{2}{3}\left(\log_{10}(1.5\times10^{12}) - 9.1\right)
= \frac{2}{3}(12.1761-9.1) = \frac{2}{3}(3.0761) = 2.05 .$$

**The convention:** the constant 9.1, and the fact that $M_0$ must be in
**N m**. Using CGS units ($M_0$ in dyn cm) shifts the magnitude by
$\tfrac23\log_{10}(10^{7}) = 4.67$ — a catastrophic error that is easy to make
and impossible to see in the output.

---

## ★2 — Radius from moment and stress drop

$$M_0 = \frac{16}{7}\Delta\sigma a^{3}
\qquad\Longrightarrow\qquad
a = \left(\frac{7M_0}{16\Delta\sigma}\right)^{1/3}
= \left(\frac{7\times1.5\times10^{12}}{16\times2\times10^{6}}\right)^{1/3}
= \left(3.281\times10^{5}\right)^{1/3} = 68.9\ \mathrm{m}.$$

The radius is **conditional on the assumed 2 MPa stress drop**; at 0.5 MPa it
would be $a = (7\times1.5\times10^{12}/(16\times5\times10^{5}))^{1/3} =
(1.3125\times10^{7})^{1/3} = 236$ m, a factor of 3.4 larger.

---

## ★3 — Mean slip

$$\bar{u} = \frac{M_0}{\mu\pi a^{2}}
= \frac{1.5\times10^{12}}{25\times10^{9}\times\pi\times68.9^{2}}
= \frac{1.5\times10^{12}}{3.728\times10^{14}} = 4.02\times10^{-3}\ \mathrm{m}
= 4.0\ \mathrm{mm}.$$

For a 200 m rupture with the *same* moment:

$$\bar{u} = \frac{1.5\times10^{12}}{25\times10^{9}\times\pi\times4\times10^{4}}
= 4.77\times10^{-4}\ \mathrm{m} = 0.48\ \mathrm{mm}.$$

Same moment, eight times less slip over a rupture 2.9× larger in radius. **A
catalogue of moments alone cannot distinguish "many small patches with large
slip" from "few large patches with small slip"** — that distinction requires
corner frequencies (radii), and therefore good bandwidth and attenuation
corrections.

---

## ★★4 — Detection radii and corner frequency

From the lesson's table: $M_w = 0$ → **2000 m**; $M_w = 2$ → **19 600 m**, a
factor of 9.8.

The reason is the corner frequency: $M_w = 0$ corresponds to a ~6 m rupture
radiating near 197 Hz, and at 197 Hz the absorption factor
$\exp(-\pi f r/Qv)$ with $Q = 50$, $v = 3\ \mathrm{km\,s^{-1}}$ at 2 km is
$\exp(-\pi\times196.6\times2000/(50\times3000)) = \exp(-8.24) = 2.6\times10^{-4}$
— the signal is annihilated. An $M_w = 2$ event radiates at ~19.7 Hz, where the
same 2 km path attenuates by $\exp(-0.825) = 0.44$ only (the table's 56% loss),
and its moment is 10⁴ times larger. **Large events are seen far away because
they are both stronger and lower-frequency.**

---

## ★★5 — A $b$-value from a catalogue

$$\hat{b} = \frac{1}{\ln 10\left(\bar{M}-M_c\right)}
= \frac{1}{2.302585\times(1.45-1.00)} = \frac{1}{1.03616} = 0.965 .$$

Consistent with $b = 1$ within the sampling error. The standard error of
Aki's estimator is approximately
$\hat\sigma_b = \hat{b}/\sqrt{N}$ for large $N$ (a convenient and widely used
approximation): $0.965/\sqrt{400} = 0.048$, so $b = 1$ lies within 0.7 standard
errors.

**What would make you doubt it.**

1. **The $M_c$ choice.** If the true completeness magnitude is 1.2 rather than
   1.0, the mean drops and $\hat{b}$ changes; the estimate is fragile to $M_c$
   and a stability plot (b versus Mc) is mandatory.
2. **Spatial completeness.** If the detection threshold varies across the
   network, the catalogue mixes spatial bins with different $M_c$ values, and
   the fit above a single global $M_c$ is still biased (the lesson's
   demonstration).
3. **Small $N$.** 400 events is enough for a handful of per cent, not for
   distinguishing $b = 0.9$ from 1.0.
4. **A magnitude scale change** along the catalogue (a network change, a
   different attenuation correction) can mimic a $b$-value change.

---

## ★★6 — Diffusivity and the front

$$D = \frac{k}{\mu_w\phi c_t}
= \frac{5\times9.869\times10^{-16}}{3\times10^{-4}\times0.04\times10^{-9}}
= \frac{4.93\times10^{-15}}{1.2\times10^{-14}} = 0.411\ \mathrm{m^{2}\,s^{-1}},$$

$$L(30\ \mathrm{d}) = \sqrt{4Dt}
= \sqrt{4\times0.411\times30\times86\,400}
= \sqrt{4.26\times10^{6}} = 2064\ \mathrm{m}.$$

At 50 mD (10× permeability) the diffusivity and the front both scale as
$\sqrt{10} = 3.16$: $D = 4.11\ \mathrm{m^{2}\,s^{-1}}$ and $L = 6530$ m.

So a decade of permeability uncertainty is a factor 3.2 in the *extent* of the
pressure footprint — which is the quantitative reason a microseismic cloud
cannot be converted into a permeability without an independent constraint. The
front also grows as $\sqrt{t}$: reaching 6.5 km takes 300 days, not 30.

---

## ★★★7 — A network for $M_c = 0$ throughout the reservoir

**Target volume.** 1.5 × 1.5 × 1.0 km centred at 3 km depth, i.e. from
−2.5 to −3.5 km.

**Detection requirement.** An $M_w = 0$ event has a 2000 m detection radius at
the reference noise floor, so every point in the volume must lie within 2000 m
of a sensor. The farthest corner of the volume from a sensor must therefore be
< 2000 m.

**Positions.**

- Four sensors near the volume corners at reservoir depth (in a well or wells
  penetrating to −3.0 km), e.g. at (0, 0, −3000), (1500, 0, −3000),
  (0, 1500, −3000), (1500, 1500, −3000) m: then the centre is 1060 m from each
  and the farthest point of the volume is about 1250 m. ✔
- Four more at −2500 m and −3500 m in the same wells to constrain depth: an
  8-level array with 500 m spacing over 1 km of well.
- Two surface stations per corner for azimuthal coverage and larger events
  ($M_w \ge 1$, radius 6200 m).

**Count.** 8 downhole levels + 8 surface stations (or 4 surface stations if
cost-constrained).

**Expected accuracy.** From the lesson's geometry study (8 downhole levels over
1.5 km plus 4 surface stations), the random location error was **35 m** with a
2 ms pick error and no depth bias; with a 5% velocity-model error, the error
rose to **158–186 m** and moved into the horizontal coordinates. Design
expectation: tens of metres with a calibration shot, hundreds without.

**What the design cannot measure.** Permeability. It locates slip on
pre-existing fractures; the hydraulically active subset, and the flow rate
through it, are not determined by event locations at any sensor count.

---

## ★★★8 — A bias study

**Volume.** Events uniform in a half-space to 6 km radius (as in the lesson), or
a rectangular volume if a specific field geometry is being mimicked.

**Magnitudes.** Gutenberg–Richter with $b_{\text{true}} = 1$ above
$M_{\min} = -1.5$, drawn by inverse transform
$M = M_{\min} - \log_{10}(1-U)/b$ with $U$ uniform.

**Detection model.** Amplitudes from
$A(r) = M_0f_c^{2}\exp(-\pi f_c r/Qv)/r$ with $f_c$ from the rupture radius,
normalised to a reference event, thresholded at a stated noise floor (the
lesson uses $10^{-2}$ relative to an $M_w = 0$ event at 1 km with $Q = 50$).

**Fitting.** Aki's estimator $\hat{b} = 1/[\ln 10(\bar{M}-M_c)]$ applied at five
thresholds from $M_{\min}$ to 1.0, reporting the number of events at each.

**Prediction.** The bias is **negative** (the fitted $b$ is too small) and large
at low $M_c$. The lesson measured 0.347 at $M_c = -1.5$ (against a true 1.0),
0.744 at $-0.5$, and 0.98–1.03 at $M_c \ge 0$. The sign is negative because
distant small events are preferentially lost, which removes the low-magnitude
tail and raises $\bar M$.

**Failure mode.** If the volume is small enough that detection is complete
everywhere, the study measures nothing; if the noise floor is set at the mean
amplitude of the smallest events, the result is dominated by a handful of
detections and the fitted $b$ is noise, not bias; and if events are drawn with
a spatially non-uniform density (e.g. clustered in a cloud), the bias is
confounded with the clustering. State the volume, the threshold and the
detection count alongside any $b$-value, or the number is unreproducible.
