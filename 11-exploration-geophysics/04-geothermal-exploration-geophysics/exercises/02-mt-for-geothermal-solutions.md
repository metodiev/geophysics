# Solutions — 11-04-02 Magnetotellurics for Geothermal Resource Assessment

> **Read after attempting the exercises.** Numbers were computed with the
> relations of the lesson; assumptions are labelled.

Lesson: [02 Magnetotellurics for Geothermal Resource Assessment](../02-mt-for-geothermal.md).

---

## ★1 — Skin depth

$$\delta = 503.3\sqrt{\frac{\rho}{f}}
= 503.3\sqrt{\frac{15}{0.05}} = 503.3\sqrt{300} = 503.3\times17.3205
= 8717\ \mathrm{m} = 8.72\ \mathrm{km}.$$

Units: $\sqrt{(\Omega\,\mathrm{m})/\mathrm{Hz}} =
\sqrt{(\mathrm{m^{2}\,s^{-1}})/(\mathrm{s^{-1}})} = \mathrm{m}$, so the constant
carries the square root of $\mathrm{s}$. ✔

---

## ★2 — Apparent resistivity from an impedance

$$\rho_a = \frac{|Z|^{2}}{\omega\mu_0}
= \frac{(0.020)^{2}}{2\pi\times0.5\times4\pi\times10^{-7}}
= \frac{4.0\times10^{-4}}{3.9478\times10^{-6}} = 101.3\ \Omega\,\mathrm{m}.$$

A phase of 45° with a frequency-independent apparent resistivity is the exact
signature of a **uniform half-space**, so the section beneath this station is
approximately homogeneous to the depth reached by the longest period with this
behaviour.

---

## ★3 — Conductance

$$S = \frac{h}{\rho} = \frac{300}{5} = 60\ \mathrm{S}.$$

Alternatives with $S = 60$ S: **600 m at 10 $\Omega$ m** and **150 m at
2.5 $\Omega$ m**. The lesson's forward modelling shows that these three models
differ by less than 0.012 in $\log_{10}\rho_a$ above 10 s period — a third of a
0.03 noise level — so at those periods they are indistinguishable.

---

## ★★4 — The transition period of a two-layer model

$$\delta = 503.3\sqrt{\frac{\rho}{f}} = 600
\qquad\Longrightarrow\qquad
f = \frac{503.3^{2}\times20}{600^{2}}
= \frac{5.066\times10^{6}}{3.6\times10^{5}} = 14.1\ \mathrm{Hz},
\qquad T = 0.071\ \mathrm{s}.$$

- **Shorter periods** ($T < 0.07$ s, $\delta < 600$ m): the sounding is inside
  the layer, $\rho_a \to 20\ \Omega$ m and $\varphi \to 45^\circ$.
- **Longer periods**: the current system samples the resistive half-space,
  $\rho_a$ rises toward 200 $\Omega$ m and, because the apparent resistivity is
  rising, the **phase falls below 45°** (the dispersion relation of the lesson).
  Only at very long periods does the phase return to 45° at the new level.

This is the classic two-layer curve, and it is why the *phase minimum* is the
practical datum for the layer boundary: it is static-shift free.

---

## ★★5 — What the data constrain

**Above 10 s:** the response is a function of the conductance $S = h/\rho$ —
three models with $S = 60$ S differ by ≤ 0.012 in $\log_{10}\rho_a$, below the
noise. So the data constrain the **product** and not the factors; any thickness
quoted in that band comes from the regularisation or a starting model, and the
conductance is the measurement to report.

**At short periods:** the skin depth becomes comparable to the layer thickness,
so the thin-sheet approximation fails, the wave *propagates* within the layer
rather than diffusing through it as a sheet, and the response depends on
$\rho$ and $h$ separately — up to 0.29 in $\log_{10}\rho_a$ between the
equivalent models in the demonstration. So the short-period data do constrain
the pair, but only for the layer, not for what lies beneath it.

---

## ★★6 — A static shift of 2.0

Apparent resistivity: multiplied by the **square** of the electric-field shift
factor, so a factor 2 in the shift gives a factor 4 in $\rho_a$ if the shift
acts on $E$. Taking the lesson's convention (a factor 2 in $\rho_a$):
apparent resistivity is in error by **+100%**, and the phase by **0%**.

If the interpretation attributes the factor 2 to the layer resistivity, then for
fixed conductance the thickness must also double, or for fixed thickness the
conductance halves — a **factor 2 error in either**. This is why the amplitude
curve is not interpretable alone.

**Two remedies.**

1. **A collocated TEM sounding** (controlled source, so not statically
   shifted): limitation — it senses only the shallow, most-conductive part of
   the section, so it constrains the shift when the near surface is the culprit
   and can be inconclusive over a resistive surface.
2. **A resistivity log in a nearby well**: limitation — the shift is a
   *site* property, so a log 5 km away only constrains the regional component,
   and the local shift remains.

A third option — fitting the shift as a free inversion parameter — is not a
remedy but a trade-off: it adds one unknown per site and absorbs real structure
into the shift.

---

## ★★★7 — A survey band

**Shortest period.** The wave must reach 1.5 km with enough sensitivity. Using
three skin depths as a practical penetration criterion in the 25 $\Omega$ m
overburden, $\delta = 500$ m:

$$f = \frac{503.3^{2}\times25}{500^{2}} = \frac{1.267\times10^{7}}{2.5\times10^{5}}
= 50.7\ \mathrm{Hz},
\qquad T_{\min} = 0.020\ \mathrm{s}.$$

A more conservative one-skin-depth criterion gives
$f = 253\,303\times25/1500^{2} = 2.8$ Hz, $T = 0.36$ s. So acquire from
**0.02 s** (resolution of the cap top) — and note that both numbers assume a
single overburden resistivity; a conductive layer near the surface would make
the required periods shorter.

**Longest period.** The reservoir at 2.5 km must be sensed, and below a
conductive overburden the current must diffuse through it. Using the *cap*
resistivity (say $5\ \Omega$ m) for a 500 m path plus the remaining 2 km in
25 $\Omega$ m, a practical target is a skin depth of 3–5 km in the overburden:
$f = 253\,303\times25/3000^{2} = 0.70$ Hz, $T = 1.4$ s; for 10 km reach,
$T \approx 16$ s. Acquire to **at least 100 s** to see structure below the
reservoir and to constrain the long-period trend.

**Dead band.** The natural MT signal is weak around 0.5–5 s in many regions, so
the band that contains the transition to the reservoir may be exactly where the
data are noisiest. Plan for longer recording times, remote reference processing,
and a stated fallback: report the structure as constrained by the phases on
either side rather than pretending to a resolution the gap does not support.

---

## ★★★8 — Separability test for two cap models

**Models.** A: $5\ \Omega$ m over 300 m ($S = 60$ S); B: $10\ \Omega$ m over
600 m ($S = 60$ S), both over the same reservoir/basement.

**Metric.** $\max|\Delta\log_{10}\rho_a|$ and $\max|\Delta\varphi|$ over the
band, evaluated with the same forward code, in three bands: full, $T > 10$ s and
$T > 100$ s. Separability requires **either** metric to exceed the stated noise
(0.03 in $\log_{10}\rho_a$ or 1.0° in phase) *in the band the interpretation
will use*.

**Expected result** (from the lesson's table): in the long-period band the two
models differ by 0.011 in $\log_{10}\rho_a$ — below the noise — so they are
**not** separable there, while at short periods they differ by up to 0.29 and
are separable. So the test's outcome depends entirely on the band, and the
answer to report is "separable at $T < 1$ s, equivalent at $T > 10$ s".

**Alternative measurement if not separable.** A collocated TEM sounding
(constrains the shallow conductance without static shift), a resistivity log in
a well, or a broader band that samples the internal resolution of the layer. Any
of the three supplies an independent constraint on one of the two factors.

**Failure mode.** If the two models are compared using data that have been
inverted with different regularisation or starting models, or with different
static-shift treatments per model, the difference measured is the inversion's,
not the data's. The test must use identical processing on both — which is why
it is specified as a forward-modelling comparison, with no inversion in the
loop.
