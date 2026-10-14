---
id: 11-04-02
title: "Magnetotellurics for Geothermal Resource Assessment"
level: research
prereqs: ["11-04-01", "08-04-02", "08-04-04"]
tags: [exploration-geophysics, geothermal, magnetotellurics, resistivity, inversion]
---

# Magnetotellurics for Geothermal Resource Assessment

**All models and data in this module are SYNTHETIC.** The layered resistivity
models, the noise levels and the equivalence pairs below are chosen teaching
values, and no field dataset is used. Physical constants (the permeability of
free space) are exact.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the skin depth from the diffusion equation and **compute** the
   depth reach for a stated resistivity and period.
2. **Define** the MT impedance, apparent resistivity and phase, and **derive**
   the half-space response (45° phase) as a check on any code.
3. **Compute** a 1-D layered MT response with the impedance recursion and
   **interpret** the resulting apparent-resistivity and phase curves.
4. **Demonstrate** conductance equivalence: show that the response is a function
   of $h/\rho$ in the band where the layer is thin compared with the skin
   depth, and **state** which band constrains what.
5. **Quantify** the effect of a static shift on apparent resistivity and on
   phase, and **describe** how the shift is removed.
6. **Compute** the cap-thickness change that is detectable at a stated noise
   level, and **write** the resulting uncertainty statement.
7. **State** the assumptions (1-D, isotropy, undistorted, non-dispersive) that
   a geothermal MT interpretation rests on.

## Prerequisites

- [11-04-01 Geophysical Signatures of Geothermal Reservoirs](01-geothermal-signatures.md) —
  what the resistivity anomaly means physically.
- [08-04-02 Magnetotellurics: Impedance and Apparent Resistivity](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the field measurement and the impedance concept.
- [08-04-04 MT Inversion: 1-D, 2-D and 3-D](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/04-mt-inversion.md) —
  the inversion machinery that follows the forward modelling shown here.

## 1. Why MT is the workhorse method

Geothermal exploration needs to map a **conductor** at a kilometre or two: the
clay-altered caprock and the hot, saline reservoir
([11-04-01 §5.1](01-geothermal-signatures.md)). Magnetotellurics is the natural
tool because

1. its depth reach is set by the **skin depth**, which grows as the square root
   of period, so a single station covers metres to tens of kilometres;
2. it is sensitive to **conductance**, and a thin, very conductive clay cap has a
   large conductance;
3. it needs no source, so it is cheap enough to deploy in an array.

The costs are equally structural: it needs a *natural* electromagnetic field
(so it is noisy where industry is), it is distorted by near-surface
heterogeneity, and it measures a *product* of conductivity and thickness rather
than a depth.

## 2. Skin depth

In a conductive medium with negligible displacement current, the magnetic field
diffuses according to

$$\nabla^{2}\mathbf{H} = \mu_0\sigma\frac{\partial \mathbf{H}}{\partial t}.$$

For a time dependence $e^{i\omega t}$ and a plane wave, the solution decays as
$e^{-z/\delta}$ with

$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}
= \sqrt{\frac{2\rho}{\omega\mu_0}}
= 503.3\sqrt{\frac{\rho}{f}}\ \mathrm{m}
\quad(\rho\ \text{in}\ \Omega\,\mathrm{m},\ f\ \text{in Hz}).$$

*Derivation of the constant:* $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$
and $\omega = 2\pi f$ give
$\delta = \sqrt{\rho/(\pi f \mu_0)} = \sqrt{\rho/(3.948\times10^{-6} f)}
= 503.3\sqrt{\rho/f}$.

Skin depth is the e-folding depth for the field, and the usual rule that "MT
sees to roughly one skin depth" is an order-of-magnitude statement: the
sensitivity of a sounding extends to a few skin depths, and the resolution
degrades with depth.

The demonstration tabulates $\delta$ in kilometres:

| $\rho$ ($\Omega$ m) | 0.001 Hz | 0.01 Hz | 0.1 Hz | 1 Hz | 10 Hz |
|---|---|---|---|---|---|
| 1 | 15.92 | 5.03 | 1.59 | 0.50 | 0.16 |
| 10 | 50.33 | 15.92 | 5.03 | 1.59 | 0.50 |
| 100 | 159.15 | 50.33 | 15.92 | 5.03 | 1.59 |
| 1000 | 503.29 | 159.15 | 50.33 | 15.92 | 5.03 |

Two operational consequences are visible immediately. A 1 $\Omega$ m clay cap is
sensed through a few kilometres at 1 Hz, so the *cap* is easy. Seeing *through*
it requires longer periods, and the deeper the resistive basement, the longer
the period: a 100 $\Omega$ m basement at 15 km needs periods near 5000 s. Band
selection is therefore a design decision, taken before the survey.

## 3. The impedance, apparent resistivity and phase

MT measures the horizontal magnetic and electric fields and forms the impedance
tensor. In 1-D,

$$Z(\omega) = \frac{E_x(\omega)}{H_y(\omega)},
\qquad
\rho_a = \frac{|Z|^{2}}{\omega\mu_0},
\qquad
\varphi = \arg Z .$$

For a uniform half-space, $Z = \sqrt{i\omega\mu_0\rho}$, so

$$|Z|^{2} = \omega\mu_0\rho \;\Longrightarrow\;
\boxed{\rho_a = \rho}, \qquad \varphi = \arg\sqrt{i} = 45^\circ .$$

**A 45° phase and a frequency-independent apparent resistivity are the signature
of a half-space**, and they are the first thing to check in any code or dataset:
departures at the long-period end mean the model is finite (a resistive
basement), and departures at the short-period end mean the top layer is not
what was assumed.

### 3.1 The layered recursion

For a stack of layers with resistivities $\rho_j$ and thicknesses $h_j$ over a
half-space, the impedance is built from the bottom up:

$$Z_j = Z_{0j}\,\frac{Z_{j+1} + Z_{0j}t_j}{Z_{0j} + Z_{j+1}t_j},
\qquad
Z_{0j} = \sqrt{i\omega\mu_0\rho_j},
\qquad
t_j = \tanh\left(\gamma_j h_j\right),
\qquad
\gamma_j = \sqrt{i\omega\mu_0\sigma_j} = \frac{1+i}{\delta_j}.$$

The demonstration implements exactly this and checks it on a uniform
100 $\Omega$ m half-space:

| $f$ (Hz) | $\rho_a$ ($\Omega$ m) | $\varphi$ (°) |
|---|---|---|
| 0.0010 | 100.0000 | 45.0000 |
| 0.0158 | 100.0000 | 45.0000 |
| 0.2512 | 100.0000 | 45.0000 |
| 3.9811 | 100.0000 | 45.0000 |
| 100.0000 | 100.0000 | 45.0000 |

with $\max|\rho_a-100| = 5.7\times10^{-14}\ \Omega$ m and
$\max|\varphi-45^\circ| = 7.1\times10^{-15}$ degrees. The recursion reproduces
the analytic result to machine precision, **which is the only check available
before it is applied to a model whose answer is not known in advance**. That is
the standard of verification this repository asks for.

## 4. A geothermal model and how to read it

Cap 5 $\Omega$ m / 300 m; reservoir 30 $\Omega$ m / 1000 m; basement
200 $\Omega$ m half-space:

| period (s) | $\rho_a$ ($\Omega$ m) | $\varphi$ (°) | $\delta$ in cap (m) |
|---|---|---|---|
| 1000.000 | 171.50 | 40.93 | 35588 |
| 251.189 | 147.62 | 37.50 | 17836 |
| 63.096 | 111.16 | 32.13 | 8939 |
| 15.849 | 67.89 | 25.33 | 4480 |
| 3.981 | 32.39 | 19.58 | 2245 |
| 1.000 | 13.06 | 19.23 | 1125 |
| 0.251 | 6.02 | 28.45 | 564 |
| 0.063 | 4.51 | 40.36 | 283 |
| 0.016 | 4.94 | 45.62 | 142 |

Reading the curve is the interpretable skill, and the pattern is generic:

1. **Short periods** see only the cap: $\rho_a \to 5\ \Omega$ m and the phase
   returns to 45° once the skin depth is small compared with the cap thickness
   ($\delta = 142$ m at 0.016 s, 283 m at 0.063 s).
2. **Intermediate periods** see the cap *and* what lies beneath: $\rho_a$ rises
   (4.5 → 32 → 68 → 111 $\Omega$ m between 0.063 and 63 s) and the **phase
   falls below 45°**. The two are not independent: for a 1-D earth the phase and
   the slope of the apparent-resistivity curve are related by the MT dispersion
   relation
   $$\varphi \approx 45^\circ - \frac{\pi}{4}\,
   \frac{\mathrm{d}\ln\rho_a}{\mathrm{d}\ln T},$$
   so a rising apparent resistivity necessarily means a phase below 45°. (The
   sign was checked numerically in this repository: a 10 $\Omega$ m layer over
   a 100 $\Omega$ m half-space has a slope of $+0.43$ and a phase of 27.4°,
   while the reversed model has a slope of $-0.18$ and a phase of 53.8°.)
3. **Long periods** approach the basement: $\rho_a \to 200\ \Omega$ m, phase
   returns toward 45°.
4. The **phase minimum** (19.2° here, near 1 s) marks the cap-to-reservoir
   transition; the *period* of that minimum is the datum that converts to a
   depth, using the period–skin-depth relation and an assumed conductivity.

This is why the phase is the most robust part of the response: it is unaffected
by static shift (§6), and its extrema are tied to layer boundaries.

## 5. Non-uniqueness I: conductance equivalence

A thin conductive layer responds to its **conductance**

$$S = \frac{h}{\rho}\ \ (\mathrm{siemens}),$$

which is the product that the long-period data constrain. The demonstration
compares responses with the 5 $\Omega$ m / 300 m cap ($S = 60$ S):

| model | $S$ (S) | $\max|\Delta\log_{10}\rho_a|$: full band | $T > 10$ s | $T > 100$ s |
|---|---|---|---|---|
| 5 $\Omega$ m / 300 m | 60 | 0.0000 | 0.0000 | 0.0000 |
| 10 $\Omega$ m / 600 m | 60 | 0.2931 | 0.0114 | 0.0035 |
| 2.5 $\Omega$ m / 150 m | 60 | 0.1876 | 0.0056 | 0.0017 |
| 10 $\Omega$ m / 300 m | 30 | 0.3559 | 0.1664 | 0.0663 |

Read the two faces of this table:

- **At long periods the equivalence holds.** Three different models with
  $S = 60$ S differ by less than 0.012 in $\log_{10}\rho_a$ above 10 s and by
  less than 0.004 above 100 s — a factor of three *smaller than the 0.03 noise
  level* assumed in §7. In that band the data constrain the product and nothing
  else, and any thickness quoted there is supplied by the regularisation or the
  starting model.
- **At short periods the layer is resolved internally.** The skin depth becomes
  comparable to the layer thickness, the thin-sheet approximation fails, and the
  models separate by up to 0.29 in $\log_{10}\rho_a$ — a factor of two in
  apparent resistivity. The 30 S model (half the conductance) differs from the
  reference by 0.17 even above 10 s, so the discrimination is selectively
  against *equal-conductance* alternatives only.

The practical statement is that a geothermal MT interpretation must say **which
band** the cap thickness rests on. If the answer comes from the long-period
equivalence band, the thickness is not determined; if from the short-period
internal resolution, the cap resistivity and thickness are jointly resolved but
the reservoir beneath may not be. Breaking the deadlock requires an independent
measurement — a resistivity log in a well, or a TEM sounding at the same site
([09-05-01 TEM Sounding](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md)).

## 6. Non-uniqueness II: static shift

Charge accumulation at a near-surface inhomogeneity multiplies the measured
electric field by a real, frequency-independent factor, which multiplies
apparent resistivity by its square and leaves the phase **exactly** unchanged:

| shift factor | change in $\rho_a$ | change in phase |
|---|---|---|
| 0.5 | −50% | 0 |
| 1.0 | 0 | 0 |
| 2.0 | +100% | 0 |
| 4.0 | +300% | 0 |

A factor of two in $\rho_a$ is a factor of two in every interpreted resistivity
— and hence in every conductance, and hence (for a fixed conductance) in the
inferred thickness. Two consequences:

1. **The phase is the reliable curve.** Inversions that weight phase heavily
   recover the structure; amplitude-only inversions may be shifted.
2. **The shift must be measured, not fitted.** It is a property of the site, not
   of the target, and the standard remedy is a collocated TEM sounding (which
   is not statically shifted because it uses a controlled source) or a
   resistivity log. Fitting a static shift as a free parameter per station adds
   one unknown per site to the inversion, and it is traded off against the
   layer resistivities — a classic source of apparent structure that is not
   there.

## 7. What the curve actually constrains

The demonstration asks a direct question: at a stated noise level of 0.03 in
$\log_{10}\rho_a$ and 1.0° in phase, how large a change in cap thickness is
detectable?

| cap thickness change | $\max|\Delta\log_{10}\rho_a|$ | $\max|\Delta\phi|$ (°) | detectable? |
|---|---|---|---|
| 5% | 0.021 | 0.81 | no |
| 10% | 0.042 | 1.60 | yes |
| 20% | 0.081 | 3.07 | yes |
| 40% | 0.153 | 5.74 | yes |

So a 5% change in cap thickness is below the noise; a 10% change is already
visible, and visible **in the phase** first. This is the resolution the survey
delivers at that noise level, and it is what an uncertainty statement should
quote.

A defensible summary for a report is therefore of the form:

> Cap conductance $60\pm3$ S (approximately 5%) from 0.01–100 s data;
> thickness $300\pm40$ m if the cap resistivity is $5\pm0.7\ \Omega$ m, an
> equivalence that requires a collocated TEM sounding to break; depth to
> basement from the long-period phase rise, with a static-shift uncertainty of
> a factor of two in the amplitude curve.

Every clause names a band, a quantity and an assumption. That is the standard.

## 8. Worked examples

### Example 1 — depth reach for a target

A reservoir cap sits at 1.5 km. The overburden is 20 $\Omega$ m on average and
you want the data to sense *through* the cap. Required period from
$\delta = 503.3\sqrt{\rho/f}$ with $\delta = 1500$ m and $\rho = 20$:

$$f = \frac{503.3^{2}\times20}{1500^{2}} = \frac{5.066\times10^{6}}{2.25\times10^{6}}
= 2.25\ \mathrm{Hz}
\qquad\Longrightarrow\qquad T = 0.44\ \mathrm{s}.$$

But the *cap* is 5 $\Omega$ m, and within the cap the skin depth at 0.44 s is
$503.3\sqrt{5/2.25} = 750$ m — only half the 1.5 km depth, so the sounding is
still partly inside the cap. In practice you would acquire down to periods of
tens of seconds to be safely past it: **the reach calculation must be done in
the layer you are actually in**, not in an average overburden.

### Example 2 — conductance equivalence, by hand

Cap thickness 200 m at 4 $\Omega$ m gives $S = 50$ S. An alternative with the
same conductance: 250 m at 5 $\Omega$ m. If the inversion resolves only the
conductance, the reported thickness will depend on the resistivity the
regularisation chooses — a factor of 1.25 here. The honest report gives $S$ and
the assumed $\rho$; the thickness follows from them and inherits their
uncertainty.

### Example 3 — reading a phase curve

A sounding shows a phase minimum of 15° at 0.3 s and a phase of 45° below
0.01 s. Then:

- the 45° plateau identifies a homogeneous top layer (its resistivity is the
  apparent resistivity there);
- the minimum identifies a transition to a more **resistive** medium below the
  conductive layer: the phase is below 45° because the apparent resistivity is
  *rising* with period as the sounding passes out of the conductor;
- the period of the minimum, 0.3 s, corresponds to a skin depth in the cap of
  $503.3\sqrt{\rho_{\text{cap}}/3.33}$. For a 5 $\Omega$ m cap that is 617 m —
  so the cap is of order a few hundred metres thick, and the *number* requires
  the conductivity assumption.

## 9. Assumptions and regime of validity

1. **1-D layered Earth.** Real geothermal targets are 3-D (faults, dykes,
   volcanic units). 1-D inversion of 3-D data produces artefacts that look like
   layers; the dimensionality must be tested (impedance tensor skew and
   induction vectors) before a 1-D interpretation is reported.
2. **Plane-wave source.** The natural MT source must be a uniform plane wave;
   the source-field assumption fails at the longest periods in some regions, and
   the "dead band" around 1 s is a signal-to-noise problem, not a physics one.
3. **Isotropic layers.** Electrical anisotropy is rarely resolvable with MT
   alone and is often ignored silently.
4. **Static shift is removed independently.** It is the leading systematic error
   in the amplitude curve (§6).
5. **No induced polarisation effects.** At the frequencies used here, IP is
   small; where the target is clay-rich and polarisable, it is not.
6. **Displacement currents and induced currents in the air are negligible** at
   these frequencies (a valid assumption below roughly 10 kHz).
7. **The noise level is known and Gaussian in $\log\rho_a$.** Real MT noise is
   heavy-tailed and correlated between stations; the 0.03 figure is a
   convenient stand-in.

## 10. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| skin depth | $\delta$ | m | $\sqrt{\rho/(\pi f\mu_0)}$ |
| impedance | $Z$ | $\Omega$ | E/H = (V/m)/(A/m) |
| apparent resistivity | $\rho_a$ | $\Omega$ m | $|Z|^2/(\omega\mu_0)$ |
| phase | $\varphi$ | degrees or rad | $\arg Z$ |
| conductance | $S$ | S = Ω⁻¹ | $h/\rho$ |
| $\mu_0$ | | $4\pi\times10^{-7}$ H m⁻¹ | exact |

Two conversions that cause errors: $\omega = 2\pi f$ (not $f$), and conductance
in siemens versus conductivity in S/m — the first is a product over thickness,
the second an intensive property.

## 11. Python demonstration

`code/mt_for_geothermal_demo.py` prints:

1. the skin-depth table over four resistivities and five frequencies;
2. the half-space verification, with the maximum deviation from
   $\rho_a = \rho$ and $\varphi = 45^\circ$;
3. the geothermal-model response with periods, apparent resistivity, phase and
   in-cap skin depth;
4. the conductance-equivalence comparison in three period bands;
5. the static-shift table;
6. the cap-thickness detectability table against a stated noise level.

It is print-only, seeded with `np.random.default_rng(20261014)` and exits 0.

## 12. Exercises

- [`exercises/02-mt-for-geothermal-exercises.md`](exercises/02-mt-for-geothermal-exercises.md)
- [`exercises/02-mt-for-geothermal-solutions.md`](exercises/02-mt-for-geothermal-solutions.md)

## Mastery checkpoint

> A three-layer model: 8 $\Omega$ m over 200 m, 40 $\Omega$ m over 800 m,
> 300 $\Omega$ m half-space. **(a)** Compute the skin depth in each layer at
> 0.1 Hz and at 100 s period. **(b)** State the two periods at which the phase
> should show a transition, and justify them with skin depths. **(c)** State the
> conductance of the top layer, and construct a different (thickness,
> resistivity) pair with the same conductance. **(d)** A static shift of 1.5 is
> present: state the percentage error in apparent resistivity and in the
> interpreted conductance of the top layer, and how you would remove it.

## Common pitfalls

1. **Inverting a 1-D model to 3-D data.** The result is a plausible layered
   artefact; test dimensionality first.
2. **Quoting a cap thickness without its conductance.** They are one
   measurement and two unknowns.
3. **Fitting static shifts as free parameters.** They trade against layer
   resistivities and manufacture structure.
4. **Reading amplitude and ignoring phase.** The phase is shift-free and is
   where the layer boundaries show.
5. **Using one skin depth as the depth of investigation.** Sensitivity extends
   to a few skin depths, with degrading resolution.
6. **Forgetting the dead band.** A data gap near 1 s is a signal problem, not
   evidence of no structure.

## Related modules

- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  MT theory, processing and inversion in full.
- [09-05 EM Methods Applications](../../09-electrical-em-methods/05-em-methods-applications/README.md) —
  TEM, FEM and CSEM, including the geothermal and permafrost applications and
  the tie that removes static shift.
- [05-09-03 Geothermal Exploration Geophysics](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md) —
  the survey-level treatment of the same method.
- [11-04-01 Geophysical Signatures of Geothermal Reservoirs](01-geothermal-signatures.md) —
  what the conductor means.
- [18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md) —
  how the ambiguity is formally reduced by a second dataset.

## Further reading

- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook.
  Electromagnetic methods, skin depth and MT.
- Kearey, P., Brooks, M., & Hill, I. (2002). *An Introduction to Geophysical
  Exploration* (3rd ed.). Blackwell. Level: textbook. Method selection for
  geothermal and other targets.
- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. For the seismic constraints
  that complement MT in a geothermal survey.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
