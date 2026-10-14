# Solutions — 05-07-05 Reporting Geophysical Results with Honest Uncertainty

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values computed for this problem set state their
> seed and sample count. Every parameter is SYNTHETIC.

---

## ★1 — A detectability statement

> "A compact body of $5\times10^{9}$ kg at 300 m depth would produce a peak
> anomaly of 0.43 mGal; against a station noise of 0.02 mGal this is 21.5 times
> the noise, so it is detected at a 3σ threshold. Expressed as a mass limit, the
> smallest body detectable at 300 m and 3σ is $8.1\times10^{8}$ kg."

Check: $z_{\max} = \sqrt{GM/(3\sigma)} = \sqrt{6.674\times10^{-11}\times5.79\times10^{9}/
(3\times2\times10^{-7})} = 802.5$ m, so 300 m is comfortably inside the limit.

---

## ★2 — An honest replacement for "500 ± 10 m"

> "Depth 383–500 m. The lower and upper ends correspond to a 2-D (cylindrical)
> source and a compact 3-D source respectively; both fit the profile to 0.02 mGal
> RMS and the data do not distinguish them. Within the chosen shape the depth is
> determined to ±10 m, but the shape choice contributes ±117 m, which dominates."

The phrase "±10 m" alone is not wrong, it is *incomplete in a misleading
direction*: it implies a precision 12 times better than the data support.

---

## ★3 — Four metadata items for a Bouguer map

1. **Datum and reference ellipsoid** (e.g. the IGSN71 datum, the ellipsoid used).
   Omit it and absolute values are wrong by a constant that varies between
   surveys, so grids cannot be merged or compared.
2. **Bouguer reduction density** (e.g. 2670 kg m⁻³). Omit it and the amplitude of
   every anomaly is wrong by an amount that grows with elevation.
3. **Terrain correction radius and method.** Omit it and anomalies in rough
   topography are biased by tens of per cent in a way that correlates with the
   relief.
4. **Regional-removal method and parameters** (polynomial order, filter, upward
   continuation height, wavelength). Omit it and the residual map is not
   reproducible, and the interpreted depths change by a factor of up to 2.8
   ([05-07-06](./06-interpretation-pitfalls-solutions.md)).

A fifth, equally important item: **the noise level and how it was estimated**,
because it sets every threshold in the interpretation.

---

## ★4 — The uncertainty budget under a worse half-width reading

**(a)** With the half-width read to 2 per cent (7.66 m): depth percentiles 5/16/50/
84/95 = 373.4 / 379.7 / 469.6 / 504.7 / 512.8 m. Measurement contribution 10.0 m;
shape contribution 116.8 m; ratio 11.7. Total 5–95 range 139.4 m.

**(b)** With the half-width read to 10 per cent (38.32 m): percentiles
333.9 / 365.0 / 434.1 / 523.6 / 564.2 m; measurement contribution 50.0 m;
shape contribution unchanged at 116.8 m; ratio 2.34; total 5–95 range 230.3 m.

**(c)** The two contributions are equal when
$1.30477\,\sigma_w = 116.8$ m, i.e. $\sigma_w = 89.5$ m $= 23.4$ per cent of the
half-width. So **even a 23 per cent half-width reading would leave the model term
dominant at best equality**, and the actual reading is 2 per cent. The survey
design implication is unambiguous: money spent on denser or quieter gravity
acquisition does not reduce the depth uncertainty of this target; money spent on a
shape constraint does.

---

## ★5 — A non-detection paragraph

Assume a compact body, contrast 200 kg m⁻³. Detectable mass at 4σ and
$z = 500$ m:

$$M_{\min} = \frac{4\sigma z^2}{G} = \frac{4(5\times10^{-7})(500^2)}
{6.674\times10^{-11}} = 7.49\times10^{9}\ \mathrm{kg}.$$

At 200 kg m⁻³ that is a volume of $3.75\times10^{7}$ m³, i.e. a sphere of radius
**207.6 m**. The report:

> "No anomaly exceeding 4σ = 0.20 mGal was found in the survey area. At this
> threshold a compact body of 200 kg m⁻³ contrast must have a mass above
> $7.5\times10^{9}$ kg (a sphere of 208 m radius) at 500 m depth to be detected;
> bodies smaller than that, or deeper, are not excluded by this survey. No
> statement is made about non-compact geometries."

The 4σ threshold is the survey-level value for the station count used; state the
count. If the survey had 500 stations, a 4σ per-station rule is roughly a 20 per
cent family-wise rate — too weak for a "no anomaly" claim, and the threshold must
be raised accordingly
([05-07-06 §3.1](./06-interpretation-pitfalls-solutions.md)).

---

## ★6 — Critique of "the gravity data confirm the seismic interpretation"

**(a)** Problems:

1. **Confirmation language is not testable.** Neither the gravity model nor the
   seismic model is stated, so no observation could contradict the claim.
2. **Gravity and seismics are not independent if the gravity was interpreted using
   the seismic model** (e.g. a starting model, a depth–density function derived
   from the seismic velocities). If so, the "confirmation" is circular.
3. **"A 300 m deep basin" is a location claim presented as an identification.**
   Gravity cannot confirm a depth to better than the model family allows, and
   neither method measures "basin".
4. **No uncertainty is given**, so the reader cannot tell whether 300 m means
   ±20 m or ±150 m.

**(b)** Rewrite:

> *Detection:* "The Bouguer anomaly exceeds three times the 0.02 mGal station
> noise across the basin."
> *Location:* "A model with a 300 m deep density contrast of 200 kg m⁻³ fits the
> anomaly to 0.03 mGal RMS. The feasible depth range, for contrasts of
> 150–300 kg m⁻³, is 240–340 m. The gravity data constrain the product of depth
> and contrast, not each separately."
> *Identification:* "Both datasets are consistent with a sedimentary basin of
> low density; identification rests on the well at location X and on the regional
> geology, not on either geophysical dataset."

---

## ★7 — A full uncertainty budget (worked method)

The structure, with the numbers to be obtained from your own runs (state seeds and
grids; the lesson's own figures are quoted where they exist):

| Term | Mechanism | Value | Share of variance |
|---|---|---|---|
| Station noise | half-width read to 2 % | 10.0 m | 0.7 % |
| Regional order | order 1 vs 5 changes depth 235 → 213 m | ≤ 40 m | ≤ 10 % |
| Profile half-length | short profiles bias the spectral and trend terms | 0–50 m | ≤ 15 % |
| Shape family | compact vs 2-D | 116.8 m | ≥ 85 % |

**Which two could a field campaign reduce?** Profile half-length and station noise
— both are acquisition parameters. Regional order is a *processing* choice, and
although a longer profile helps, the dominant term (shape family) is not reducible
by acquisition at all, because it is a null-space direction of the potential-field
inverse problem.

**Mechanism, stated so it can be checked:** a longer profile moves the spectral
band to larger $kz$ (reducing the 3-D bias of §3.2 of
[05-07-02](../02-quantitative-interpretation.md)) and reduces the trend leakage;
lower noise reduces the half-width error and therefore the measurement term
proportionally. Nothing in either mechanism touches the shape ambiguity, whose
removal requires a dataset with transverse sensitivity.

---

## ★8 — Reviewing a published interpretation

A full-credit answer must be *specific*, and must state what it could not assess.
A worked template, using the demonstration's own case as the "paper":

**(a)** Model: a compact body of $5.8\times10^{9}$ kg at 300–310 m, host density
2670 kg m⁻³ (chosen, not measured), density contrast 800 kg m⁻³.
Uncertainties: ±11 m on depth (statistical), plus an unquantified shape family.
Assumptions: isolated source, a 2nd-order regional, flat ground, no density
heterogeneity in the host.

**(b)** Falsifiability: a borehole intersecting barren host rock between 180 and
420 m would contradict it. (Contrast: "the anomaly indicates mineralisation" is not
falsifiable.)

**(c)** Independent test: a downhole gravity log from 500 to 1300 m. It would
measure the vertical gradient of $g$, whose value distinguishes mass at 300 m from
mass distributed between 300 and 900 m — the test the demonstration performs, with
a 58-fold failure in the two-body case.

**(d)** Could not assess: the gravity datum and correction parameters, the noise
estimate and its correlation structure, whether the regional order was chosen
before or after seeing the anomaly, and whether the density contrast came from a
measurement or a prior.
