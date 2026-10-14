# Solutions — 11-03-05 Geophysics for Unconventional Reservoirs

> **Read after attempting the exercises.** Numbers were computed rather than
> estimated; where an answer is a range it is said so.

Lesson: [05 Geophysics for Unconventional Reservoirs](../05-unconventional-geophysics.md).

---

## ★1 — Elastic moduli

$$v_p^{2} = 1.4440\times10^{7}, \qquad v_s^{2} = 4.2025\times10^{6},$$
$$3v_p^{2} = 4.3320\times10^{7}, \qquad 4v_s^{2} = 1.6810\times10^{7}, \qquad
3v_p^{2}-4v_s^{2} = 2.6510\times10^{7},$$
$$v_p^{2}-v_s^{2} = 1.02375\times10^{7},$$
$$E = \rho v_s^{2}\frac{3v_p^{2}-4v_s^{2}}{v_p^{2}-v_s^{2}}
= 2480\times4.2025\times10^{6}\times\frac{2.6510\times10^{7}}{1.02375\times10^{7}}
= 2.70\times10^{10}\ \mathrm{Pa} = 27.0\ \mathrm{GPa},$$
$$\nu = \frac{v_p^{2}-2v_s^{2}}{2\left(v_p^{2}-v_s^{2}\right)}
= \frac{1.4440\times10^{7}-8.4050\times10^{6}}{2\times1.02375\times10^{7}}
= \frac{6.0350\times10^{6}}{2.0475\times10^{7}} = 0.295 .$$

---

## ★2 — Brittleness indices, and leaving the range

$$\text{BI}_E = \frac{27.0-15.4}{80.2-15.4} = \frac{11.6}{64.8} = 0.179,$$
$$\text{BI}_\nu = \frac{0.287-0.295}{0.287-0.206} = \frac{-0.008}{0.081}
= -0.10 .$$

$\text{BI}_\nu$ is **negative**: the rock's Poisson's ratio (0.295) lies outside
the calibration range (0.206–0.287). The index is then not interpretable — it
says "more ductile than anything in the calibration set", and reporting it as
$-0.10$ invites misuse.

**The lesson:** a brittleness index is a *normalisation*, and normalisations are
only defined inside their endpoint range. Any index value outside $[0,1]$ must
be reported as "outside the calibration range", with the endpoints quoted, not
as a number.

---

## ★3 — Shear-wave splitting

Exact: $v_{\text{fast}} = 2900\sqrt{1+2(0.03)} = 2900\times1.0295630
= 2985.7\ \mathrm{m\,s^{-1}}$.

$$\Delta t = 80\left(\frac{1}{2900}-\frac{1}{2985.7}\right)
= 80\left(3.44828\times10^{-4}-3.34927\times10^{-4}\right)
= 80\times9.901\times10^{-6} = 7.92\times10^{-4}\ \mathrm{s} = 0.792\ \mathrm{ms}.$$

First-order: $\gamma d/v_s = 0.03\times80/2900 = 8.276\times10^{-4}$
s $= 0.828$ ms, which is **4.5% high**.

Both are far below the 1 ms sampling of a typical surface record: the
measurement requires either a thicker interval, higher $\gamma$, or a
higher-sampling downhole sensor. That is a design statement, not a caveat.

---

## ★★4 — An event, and what is assumed

$$M_w = \frac{2}{3}\left(\log_{10}(4\times10^{12}) - 9.1\right)
= \frac{2}{3}(12.602-9.1) = 2.33 .$$

Radius, from $M_0 = \tfrac{16}{7}\Delta\sigma a^{3}$:

$$a = \left(\frac{7M_0}{16\Delta\sigma}\right)^{1/3}
= \left(\frac{7\times4\times10^{12}}{16\times2\times10^{6}}\right)^{1/3}
= \left(8.75\times10^{5}\right)^{1/3} = 95.6\ \mathrm{m}.$$

Mean slip:

$$\bar{u} = \frac{M_0}{\mu\pi a^{2}}
= \frac{4\times10^{12}}{20\times10^{9}\times\pi\times9139}
= 6.97\times10^{-3}\ \mathrm{m} = 7.0\ \mathrm{mm}.$$

**Assumed:** the stress drop (2 MPa). Measured: the moment (amplitude) and,
with an independent corner frequency, the radius. The slip follows from the
assumption and inherits its uncertainty — a 5 MPa assumption would give about
2.5× the slip.

---

## ★★5 — Detection radius versus magnitude

From the lesson's table: $M_w = 1$ → 6200 m; $M_w = 2$ → 19 600 m; a factor of
**3.2** for one magnitude unit.

Physically: the corner frequency falls with rupture size, so a larger event
radiates its energy at lower frequency, where absorption
($\exp(-\pi f r/Qv)$) is weaker, and it also has a larger moment. Both effects
push the detection radius up.

**Consequence.** A catalogue assembled at a fixed amplitude threshold is
**spatially biased**: the completeness magnitude grows with distance from the
network. Any magnitude-frequency or event-rate analysis must therefore carry a
completeness map, not a single $M_c$ (lesson [11-04-03](../../04-geothermal-exploration-geophysics/03-microseismic-geothermal.md)
quantifies the resulting $b$-value bias).

---

## ★★6 — Distance error from one pick

$$\delta r \approx v\,\delta t = 3000\times0.002 = 6\ \mathrm{m}.$$

So each pick constrains the hypocentral distance to ~6 m. Why can the location
error be ten times larger?

Because the location is the intersection of spheres (or hyperboloids), and the
*geometry* amplifies the pick error. If all the stations lie nearly in one plane
(a surface array) or nearly on one line (a vertical array), the depth and the
origin time trade off: many different (depth, origin time) pairs reproduce the
same travel times. The amplification factor is a property of the network
geometry, not of the picking — which is why the lesson's demonstration shows
20 m for a wide 16-station array and 1827 m for four symmetric stations with the
same pick error.

---

## ★★★7 — A monitoring design

**Target:** $M_c = 0$ throughout a 3 km deep, 2×2 km reservoir.

1. From the detection model, an $M_w = 0$ event has a detection radius of
   2000 m at the reference noise floor. So every point in the reservoir must be
   within 2000 m of a sensor.
2. The reservoir is 3 km deep and 2 km across, so its corners are
   $\sqrt{(1000)^{2}+(1000)^{2}+3000^{2}} = 3317$ m from a surface point directly
   above its centre — beyond 2000 m. A surface-only network cannot meet the
   target unless the noise floor is lowered or the sensors are closer.
3. **Geometry:** place sensors in two or three deep wells that penetrate the
   reservoir (e.g. levels from −2.0 to −3.5 km, as in the lesson's location
   example) at the reservoir corners, giving ranges below 1.5 km within the
   volume, plus a surface array for larger events ($M_w \ge 1$, radius
   6200 m) and for focal-mechanism coverage.
4. **Count:** at least 8 downhole levels per well (the lesson's 8-level array
   plus 4 surface stations gave a 35 m location error and no depth bias) and
   stations on both sides of the target volume for azimuthal coverage.
5. **The one thing the design cannot deliver:** the *permeability* of the
   fractures it maps. The events locate slip on pre-existing fractures whose
   hydraulically active subsets may be a small fraction of the cloud. No
   refinement of this network changes that — it is a physical, not an
   instrumental, limit.

---

## ★★★8 — Coulomb condition

**Derivation.** Slip occurs when the resolved shear stress exceeds the frictional
strength, and the pore pressure reduces the effective normal stress:

$$\tau \ge \mu_f\left(\sigma_n - P\right).$$

Rearranging for the pressure needed to initiate slip:

$$P \ge \sigma_n - \frac{\tau}{\mu_f}
= \sigma_n\left(1 - \frac{1}{\mu_f}\frac{\tau}{\sigma_n}\right).$$

**Critical ratio.** For $\mu_f = 0.6$ the required pressure is zero when
$\tau/\sigma_n = \mu_f = 0.6$; below that ratio the fracture is stable with
$P = 0$, and above it the fracture is already critically stressed and any
perturbation (including the Earth's own stress changes) can cause slip.

**Numbers.** At $\sigma_n = 50$ MPa:

| $\tau/\sigma_n$ | required $P$ (MPa), $\mu_f = 0.6$ |
|---|---|
| 0.30 | 25.0 |
| 0.45 | 12.5 |
| 0.60 | 0.0 (already critical) |
| 0.75 | −12.5 (already sliding) |

**Why the surface cannot measure it.** The resolved shear and normal stresses
on a specific fracture depend on the full 3-D stress tensor and on that
fracture's orientation — quantities known only from borehole measurements
(breakouts, drilling-induced fractures, leak-off tests) and, even then, only
near the well. Surface geophysics constrains structure and, at best, fracture
intensity; it cannot supply the stress tensor orientation and magnitude at the
fracture scale. That is why induced-seismicity prediction is a statistical
enterprise and mitigation is an operational protocol.
