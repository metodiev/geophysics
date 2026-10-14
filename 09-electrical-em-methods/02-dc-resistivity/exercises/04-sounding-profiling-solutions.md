# Solutions — 09-02-04 Vertical Electrical Sounding vs Profiling

> **Read after attempting the exercises.** Lesson:
> [04 Vertical Electrical Sounding vs Profiling](../04-sounding-profiling.md).

---

## ★1 — The two surveys

- A **sounding** varies the spacing at a fixed centre, resolving *vertical*
  structure; it is limited by equivalence (a thin layer's thickness and
  resistivity trade) and by the noise on the small voltages at long spacings.
- A **profile** fixes the spacing and moves the array, resolving *lateral*
  structure; it is limited by the array footprint, which smears any edge over
  about the aperture.

---

## ★2 — Spacing choices for the aquifer model

| purpose | spacing | reason |
|---|---|---|
| (a) detect the aquifer | 8–12 m | the curve is already 30–40% below the top-layer value, ten times the noise |
| (b) estimate its resistivity | 12–20 m | the minimum of the curve approaches the layer value (108–129 $\Omega\,\mathrm{m}$) |
| (c) test for bedrock | 80–120 m | only these spacings begin to rise toward the resistive basement; even then it is not approached |

A single sounding cannot do all three well; the long-spacing data are needed for
(c) and are the noisiest.

---

## ★3 — Noise level

At $a = 20$ m, $k = 125.66$ m, $\Delta V = 108.2\times0.1/125.66 = 0.08611\
\mathrm{V}$, $P = I^2R = I\Delta V = 8.611\ \mathrm{mW}$; $2\%$ of $\Delta V$ is
$0.001722\ \mathrm{V}$, so

$$\sigma_{\rho_a} = k\,\sigma_{\Delta V}/I = 125.66\times0.001722/0.1
= 2.164\ \Omega\,\mathrm{m},$$

i.e. 2% of $\rho_a$ as expected (the conversion is linear).

---

## ★4 — Resolving a 2 m aquifer

$$\frac{115.68-113.32}{117.86} = 2.00\%.$$

With 5% voltage error the difference is $2.00/5.0 = 0.4\sigma$: **not
resolved.** Even at 2% noise the discrimination is marginal
($\chi^{2}$ per datum $\approx 1$ for a single spacing, and a single spacing is
not a test). A resolution claim requires several spacings and a fitted model.

---

## ★5 — Scaling the footprint

Widths scale with the array: $11.3/5.0 = 2.26$, so
$18.2\times2.26 = 41.1$ m. The DOI at $a = 11.3$ m is, from
[02](02-electrode-arrays-solutions.md)-style scaling, $2.60\times2.26 = 5.88$ m.

So at ~5.9 m depth the lateral resolution (10–90% width) is 41 m — seven times
the depth. This is the quantitative statement of "you cannot see a narrow
feature at depth with a long array", and it is independent of any inversion.

---

## ★6 — Ratio of drops at $x = 100$ m

|$a$|$\rho_a$ at $x=100$ m|drop from 200|
|---|---|---|
|2 m|194.4|5.6|
|10 m|123.7|76.3|

Ratio: $76.3/5.6 = 13.6$.

Direction explained by depth sensitivity: at the position where the interface is
4 m deep, the $a = 10$ m array has a DOI of about 5.2 m
($2.60\times2$) and its sensitivity is concentrated where the conductor is,
while the $a = 2$ m array (DOI ~1.0 m) is still almost entirely in the resistive
top layer. The long array therefore sees the conductor much more strongly, which
is exactly what makes it useful — and exactly what makes it smear the edge
(Section 4 of the lesson).

---

## ★7 — Which output is trustworthy?

**Edge position: more trustworthy.** The locally 1-D model puts a zero-thickness
conductor at the outcrop and reproduces the observed 200 $\Omega\,\mathrm{m}$ at
$x = 80$ m; as the traverse proceeds it tracks the depth of the interface
through the crossover spacing, which is a *geometric* quantity. Channelling
redistributes current but does not move the position at which the array first
senses the conductor, to better than about half an aperture.

**Amplitude: less trustworthy.** The two-layer contrast here is 200:20, i.e. 10:1.
From [02](02-electrode-arrays-solutions.md) the sensitivity profile of an array
at a 10:1 contrast has large regions of the model contributing with
*reversed* sign; the locally 1-D model has no mechanism to represent that, and
it will over- or underestimate the anomaly amplitude by tens of per cent,
depending on whether the conductor is channelled toward or away from the array.
The correct statement from a locally 1-D profile is "the contact is here, to
within an aperture", plus an explicit statement that amplitudes are
model-dependent and require a 2-D solver.

---

## ★8 — Three-spacing discriminator

1. **Acquire** three profiles (same centres, same spacing set), e.g. $a = 5$,
   10 and 20 m, over 5–10 stations.
2. **Compute the ratio field** $R(x) = [\rho_a^{(10)}(x)-\rho_a^{(20)}(x)] /
   [\rho_a^{(5)}(x)-\rho_a^{(10)}(x)]$ — the *curvature* of the sounding at each
   station.
3. **Discriminator:**
   - A **dipping interface** moves the crossover spacing spatially: $R(x)$
     varies smoothly and monotonically across the traverse, and the position
     where each spacing's profile crosses 50% of its anomaly moves
     *systematically* with spacing in the direction of the dip.
   - A **lateral thickness change** at fixed interface depth changes the
     *amplitude* of the anomaly at all spacings together: $R(x)$ stays
     approximately constant while all three profiles change amplitude in
     step.
4. **Quantitative test:** fit the two alternative models (locally 1-D with a
   dipping interface; locally 1-D with varying thickness) to all three profiles
   jointly and compare $\chi^{2}$. Report the difference and the admitted set;
   do not choose by eye.
