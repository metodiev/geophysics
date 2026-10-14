---
id: 07-07-02
title: "Vertical Datum Modernisation and National Height Systems"
level: doctoral
prereqs: ["07-04-02", "07-07-01", "07-02-03"]
tags: [gravity, geodesy, height-systems, vertical-datum, levelling, gnss]
---

# Vertical Datum Modernisation and National Height Systems

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the geopotential number from spirit levelling and **explain** why
   it, rather than a height, is the quantity a levelling network measures.
2. **Compute** dynamic, orthometric and normal heights from one set of
   geopotential numbers, and **quantify** the differences between them.
3. **Compute** the orthometric correction and state why it is systematic.
4. **Distinguish** a datum offset (a choice of origin) from a height-system
   difference (a physical/definitional term), and state which of them affects
   differences rather than absolutes.
5. **Build** an error budget for obtaining heights by levelling and by GNSS plus
   a geoid model, and **compute** the baseline length at which they cross over.
6. **Explain** what "modernisation" changes and what it does not, in terms of
   measured, converted and chosen quantities.
7. **State** the conditions under which a modernised datum is *compatible* with
   an older one, and what must be published to make a transformation possible.

## Prerequisites

- [07-04-02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](../04-geodesy-reference-frames/02-height-systems.md) —
  the definitions this lesson computes with.
- [01 Determining the Geoid: Stokes, Remove-Restore, Kriging](01-geoid-determination.md) —
  where the geoid model and its error come from.
- [07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](../02-gravity-instruments-and-surveys/03-survey-procedures.md) —
  the gravity measurements that turn levelling into a geopotential difference.

> **All models and data in this module are SYNTHETIC.** The levelling line, the
> heights, the gravity profile, the geoid, the sea-surface topography and the
> error levels are teaching values. No real network, benchmark, datum or
> published height is used.

## 1. What levelling measures

Spirit levelling measures height *differences* along a line, and it does so by
keeping a level line of sight and reading staffs. With gravity varying along the
line, the sum of the differences is not the difference of any single well-defined
height. What the sum *does* give, if surface gravity is measured at every
setup, is the **geopotential difference**:

$$\Delta C = \sum_i g_i\,\delta n_i ,$$

where $\delta n_i$ is the levelled difference of the $i$-th setup and $g_i$ the
surface gravity there. $C$ has units $\mathrm{m^{2}\,s^{-2}}$ (a potential per
unit mass) and is the physically meaningful quantity: **points with equal $C$ are
on the same equipotential surface**, which is what "level" means.

The demonstration's synthetic line runs 223.5 km from $45^\circ$N to $48^\circ$N
and rises from 0 to $800\ \mathrm{m}$, with surface gravity from $9.806200$ to
$9.806442\ \mathrm{m\,s^{-2}}$ (a decrease from the free-air effect partly
compensated by the latitude increase in normal gravity). The geopotential number
reaches $C = 7845.3\ \mathrm{m^{2}\,s^{-2}}$.

## 2. Three heights from one geopotential number

Any height is a division of $C$ by a gravity. The three standard choices:

| height | definition | gravity used | value at the last station |
|---|---|---|---|
| dynamic | $H_{\text{dyn}} = C/\gamma_{45}$ | fixed $\gamma$ at $45^\circ$ | 800.034 m |
| orthometric | $H = C/\bar g$ | mean *actual* gravity along the plumb line | 800.000 m |
| normal | $H^{*} = C/\bar\gamma$ | mean *normal* gravity along the plumb line | 799.712 m |

*Worked example 1.* With $C = 7845.3\ \mathrm{m^{2}\,s^{-2}}$ and
$\gamma_{45} = 9.806199\ \mathrm{m\,s^{-2}}$:

$$H_{\text{dyn}} = \frac{7845.3}{9.806199} = 800.034\ \mathrm{m}.$$

For the normal height, the mean normal gravity along the plumb line uses the
normal free-air gradient:
$\bar\gamma = \gamma(\varphi) + \tfrac12(0.3086\times10^{-5})H^{*}
= 9.808911 + 1.234\times10^{-3} = 9.810145$ at the last station, giving
$H^{*} = 7845.3/9.810145 = 799.712\ \mathrm{m}$.

**The demonstrations' numbers:**
$\max|H_{\text{ortho}} - H_{\text{norm}}| = 0.288\ \mathrm{m}$ and
$\max|H_{\text{dyn}} - H_{\text{ortho}}| = 0.034\ \mathrm{m}$ over this
223 km line. These are not errors: they are **definitions**. A height is only
comparable with another height if both use the same system, which is why a
transformation between national systems is a modelling exercise, not a
conversion factor.

## 3. The orthometric correction

If a surveyor sums the levelled differences without applying gravity, the result
is a height that is not the orthometric height. The demonstration computes it:

| station | levelled sum (m) | $H_{\text{ortho}}$ (m) | difference (mm) |
|---|---|---|---|
| 0 | 0.0000 | 0.0000 | 0.00 |
| 5 | 200.0008 | 200.0000 | $-0.85$ |
| 10 | 400.0038 | 400.0000 | $-3.81$ |
| 15 | 600.0088 | 600.0000 | $-8.83$ |
| 20 | 800.0159 | 800.0000 | $-15.86$ |

The maximum **orthometric correction** over the line is $15.86\ \mathrm{mm}$.

Two properties matter:

1. It **grows with the height range and the latitude range**, so it is small for
   a survey of a flat region and large for an alpine national network.
2. It is **systematic**. Repeating the levelling does not reduce it, and it is
   highly correlated between neighbouring lines, so it does not average out in a
   network adjustment. Applying it (or carrying the geopotential numbers) is
   therefore a different kind of act from averaging observations.

*Worked example 2 (the structure of the correction).* The correction is
$\int (g - g_0)/g_0\,\mathrm{d}n$ accumulated along the line: the fractional
difference between the actual gravity and the reference gravity, integrated over
the path. Over the demonstration's line the gravity changes by
$(9.806442 - 9.806200)/9.8062 = 2.5\times10^{-5}$, and multiplying by a mean
height gain of 400 m gives $1.0\times10^{-2}\ \mathrm{m} = 10\ \mathrm{mm}$ —
the right order for the measured $15.9\ \mathrm{mm}$ ✓. The estimate also shows
why the correction is second order: it is a *product* of a small gravity change
and the path length in height, not either alone.

## 4. Datum offset: a choice of origin

A national vertical datum is realised by adopting a value at one or more
benchmarks, usually by declaring that mean sea level at a tide gauge is zero. Mean
sea level itself sits above (or below) the geoid by the **sea-surface topography**,
which is of order decimetres to a metre in the open ocean (see
[03](03-sea-surface-topography.md)).

The demonstration takes a synthetic sea-surface topography of $0.30\ \mathrm{m}$
and a synthetic geoid that varies from $0.00$ to $0.18\ \mathrm{m}$ along the
line. The consequences are worth stating precisely:

- **Absolute heights** in the national system differ from geoid-referenced
  orthometric heights by a constant $\mathbf{0.30\ \mathrm{m}}$ — the datum
  offset.
- **Height differences** between benchmarks are *unchanged* (measured change:
  $0.0\ \mathrm{mm}$), because the offset is a constant.

So "is the datum wrong by 30 cm?" is not a well-posed question. It is a
*choice*: any datum is a convention for the origin, and a datum offset only
becomes a problem when absolute heights are compared across datums — for flood
risk, for sea-level trends, for engineering works spanning a boundary, or for
satellite altimetry.

## 5. Modernisation: GNSS plus a geoid, and an honest error budget

The modern alternative obtains an orthometric height from a GNSS ellipsoidal
height $h$ and a geoid model $N$:

$$H = h - N .$$

The error is the quadrature sum of the two, and the *character* of the errors
decides where the method wins. With the demonstration's stated levels — GNSS
$\sigma = 1.5\ \mathrm{cm}$ white, geoid $\sigma = 2.0\ \mathrm{cm}$ correlated
over $\sim100\ \mathrm{km}$ — and levelling at $1\ \mathrm{mm\,\sqrt{km}^{-1}}$:

| method | error at a point | error in a 3 km difference |
|---|---|---|
| spirit levelling from the datum (223 km) | $1.49\ \mathrm{cm}$ | $0.17\ \mathrm{cm}$ |
| GNSS $+$ geoid | $2.50\ \mathrm{cm}$ | $2.13\ \mathrm{cm}$ |

**The numbers do not support the folklore that the new method is always
better.** At 223 km, levelling from the datum (1.49 cm) beats GNSS+geoid
(2.50 cm), because levelling error accumulates only as $\sqrt{L}$ while the
GNSS+geoid error is dominated by two independent terms that do not.

*Worked example 3 (the crossover lengths).* Equating
$10^{-3}\sqrt{L}$ (levelling, in metres, $L$ in km) with the GNSS+geoid error:

- absolute heights: $10^{-3}\sqrt{L} = 0.0250 \Rightarrow L = 625\ \mathrm{km}$;
- a difference over $L$: $10^{-3}\sqrt{L} = 0.0213 \Rightarrow L = 452\
  \mathrm{km}$ (the geoid error largely cancels in the difference, so the
  GNSS+geoid error stops growing with distance).

So in this error model levelling wins below $\sim450$–$600\ \mathrm{km}$ and
GNSS+geoid wins above. Real networks change these numbers — levelling standards
vary, the height-system corrections of Section 3 are systematic, and GNSS errors
are themselves correlated over tens of kilometres — which is why a modernisation
plan must quote its *own* crossover rather than an average improvement.

## 6. What modernisation changes, and what it does not

| aspect | changes | does not change |
|---|---|---|
| the realisation (how a height is obtained) | levelling $\to$ GNSS + geoid | the definition of the height system |
| the origin | possibly a new offset, and ideally the geoid itself | the fact that any origin is a choice |
| absolute accuracy | improves with the geoid model and GNSS | the geoid model's error, which becomes the dominant term |
| differences | improves for long baselines | short-baseline difference accuracy, where levelling remains better |
| the network | benchmarks become less necessary | the need for *some* geodetic control, and for legacy documents |
| compatibility | requires a published transformation | the historical heights, which remain valid in their own system |

**The conditions for compatibility** are the honest content of a modernisation
decision, and they can be stated as a publication list:

1. the height system of the old and new data (orthometric or normal, and which
   normal gravity field);
2. the datum offset between them, with its uncertainty, and the tide gauges used;
3. the geoid model used (degree, data, epoch) and its error;
4. the transformation, applicable to both absolute heights and differences;
5. a set of benchmarks with heights in both systems, so the transformation can be
   *verified* rather than trusted.

Without (5), a transformation is a model; with it, it is a measurement.

## 7. Assumptions and regime of validity

1. **Gravity is measured at every levelling setup.** Without it, geopotential
   numbers are unavailable and the orthometric correction cannot be computed.
2. **The mean-gravity approximation.** The demonstration uses the Poincaré–Prey
   form $\bar g = g_{\text{surface}} + \tfrac12(0.0424\ \mathrm{mGal\,m^{-1}})H$.
   The real $\bar g$ depends on the density distribution between the surface and
   the geoid, so an orthometric height is *conditional on a hypothesis* about
   crustal density; normal heights avoid this by using normal gravity, which is a
   definition rather than a hypothesis.
3. **The geoid model is the reference.** In a modernised system the geoid model
   supplies the long-wavelength reference, and its error is inherited
   (see [01](01-geoid-determination.md)).
4. **Tides and loading.** Mean sea level as a datum requires a tide-system
   convention and a loading model; the same station gives different numbers under
   different conventions.
5. **Time.** Benchmarks move. A height is a statement about an epoch, and a
   modernised datum must include the vertical motion (see
   [07-04-04](../04-geodesy-reference-frames/04-gnss-geodesy-applications.md)).
6. **GNSS heights are ellipsoidal and in a stated frame**, which is what makes
   $H = h - N$ meaningful.

## 8. Python demonstration

`code/vertical_datum_modernisation_demo.py` prints, with units:

1. **A synthetic 223.5 km levelling line** from 45°N to 48°N rising to
   $800\ \mathrm{m}$, with surface gravity from $9.806200$ to
   $9.806442\ \mathrm{m\,s^{-2}}$ and geopotential number to
   $7845.3\ \mathrm{m^{2}\,s^{-2}}$.
2. **Three heights**: $H_{\text{dyn}} = 800.034$, $H_{\text{ortho}} = 800.000$,
   $H_{\text{norm}} = 799.712\ \mathrm{m}$, with the differences
   $0.288\ \mathrm{m}$ (ortho–normal) and $0.034\ \mathrm{m}$ (dyn–ortho).
3. **The orthometric correction**: $15.86\ \mathrm{mm}$ over the line, growing
   with height and latitude.
4. **The datum offset**: $30\ \mathrm{cm}$ in absolute heights, $0.0\ \mathrm{mm}$
   in differences.
5. **The GNSS+geoid versus levelling comparison**, with the crossover lengths
   $625\ \mathrm{km}$ (absolute) and $452\ \mathrm{km}$ (differences) for the
   stated error model.

Print-only, fixed seed, no network, exits 0.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-vertical-datum-modernisation-exercises.md`](./exercises/02-vertical-datum-modernisation-exercises.md)
and
[`exercises/02-vertical-datum-modernisation-solutions.md`](./exercises/02-vertical-datum-modernisation-solutions.md).

- **★** Compute $H_{\text{dyn}}$ for $C = 5000\ \mathrm{m^{2}\,s^{-2}}$ and
  state the gravity used.
- **★** Compute the orthometric correction estimate over a 100 km line that climbs
  500 m, and state what it depends on.
- **★★** Show that a constant datum offset cancels in differences, and state one
  application where it does not.
- **★★** Compute the levelling/GNSS+geoid crossover for a levelling standard of
  $2\ \mathrm{mm\,\sqrt{km}^{-1}}$ and a geoid error of $3\ \mathrm{cm}$.
- **★★★** Design the publication set that would make a national datum change
  verifiable rather than merely documented, and state the diagnostic that would
  detect an error in each item.

## 10. Mastery checkpoint

Do this without notes:

> A national network has orthometric heights in a datum realised at a tide gauge
> where the synthetic sea-surface topography is $0.4\ \mathrm{m}$, and a geoid
> model with a $2\ \mathrm{cm}$ error. **(a)** State the datum offset and its
> effect on absolute heights and on differences. **(b)** A benchmark has
> $C = 4000\ \mathrm{m^{2}\,s^{-2}}$; compute its dynamic, orthometric (with
> $\bar g = 9.8075$) and normal (with $\bar\gamma = 9.8090$) heights.
> **(c)** Compute the difference between the orthometric and normal heights and
> state what kind of quantity it is. **(d)** A GNSS campaign with a $1.5\
> \mathrm{cm}$ error gives $H = h - N$: report the total uncertainty and the
> error in a $2\ \mathrm{km}$ difference if the geoid error is $90\%$ correlated
> over that distance. **(e)** State the one published item without which the
> transformation to the new datum cannot be verified.

*Answers.* **(a)** Offset = $0.4\ \mathrm{m}$; absolute heights shift by
$-0.4\ \mathrm{m}$ (or $+$ depending on the sign convention, and the sign must be
stated), differences are unchanged. **(b)**
$H_{\text{dyn}} = 4000/9.806199 = 407.91\ \mathrm{m}$;
$H_{\text{ortho}} = 4000/9.8075 = 407.85\ \mathrm{m}$;
$H_{\text{norm}} = 4000/9.8090 = 407.79\ \mathrm{m}$.
**(c)** $H_{\text{ortho}} - H_{\text{norm}} = 0.06\ \mathrm{m}$ — a *definitional*
difference, not an error: the two systems divide the same geopotential number by
different gravities. **(d)** $\sigma_H = \sqrt{1.5^{2}+2.0^{2}} = 2.5\ \mathrm{cm}$. For a
difference the two errors behave differently. The GNSS errors are independent:

$$\sigma_{\Delta h} = \sqrt{2}\,\sigma_h = 2.12\ \mathrm{cm}.$$

The geoid errors are correlated with $\rho = 0.9$, so the *difference* of the two
geoid errors has variance $2\sigma_N^{2}(1-\rho)$:

$$\sigma_{\Delta N} = \sqrt{2(2.0)^{2}(0.1)} = 0.89\ \mathrm{cm}.$$

Hence $\sigma_{\Delta H} = \sqrt{2.12^{2}+0.89^{2}} = \sqrt{4.5+0.8}
= 2.30\ \mathrm{cm}$. **The geoid error does not vanish over a $2\ \mathrm{km}$
baseline** — it is reduced by only $\sqrt{1-\rho} = 0.32$, so a correlated error
must be modelled as correlated. Only over baselines long compared with the geoid
correlation length ($\rho \to 0$, i.e. far apart) does the full $\sqrt{2}\sigma_N$
return. **(e)** A set of benchmarks with heights in both systems: without it the
transformation cannot be tested, only asserted.

## 11. Common pitfalls

1. **Treating a height as a length.** It is a geopotential divided by a gravity;
   the system must be named.
2. **Summing levelled differences without gravity** and calling the result an
   orthometric height.
3. **Reducing the orthometric correction by repeating measurements.** It is
   systematic.
4. **Confusing a datum offset with a height-system difference.** One is a choice
   of origin and cancels in differences; the other is a definitional term that
   does not.
5. **Assuming GNSS+geoid is always more accurate.** Below the crossover length it
   is not, and the crossover must be computed.
6. **Treating geoid error as white.** It is strongly correlated, which helps
   differences and hurts absolutes.
7. **Publishing a transformation without checkpoints.** Then it is a model.

## 12. Real-world applications

- **Flood risk and coastal planning.** Absolute heights across a datum boundary
  require the offset and its uncertainty.
- **Sea-level studies.** Comparing a tide-gauge record with a geoid-referenced
  height requires both the datum offset and the land motion.
- **Engineering and deformation.** Differences are what matter, and there the
  correlated part of the geoid error is the main enemy over long baselines.
- **Satellite altimetry.** The altimeter measures an ellipsoidal height; the
  geoid and the datum offset convert it to a dynamic ocean topography
  (see [03](03-sea-surface-topography.md)).

## 13. Further reading

- **Torge, W. & Müller, J., *Geodesy*** — height systems, their definitions and
  the practical realisation of datums.
- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the geopotential
  number, orthometric and normal heights in the classical formulation.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — geoid models as
  the reference for modern height determination.
- **Stacey, F. D. & Davis, P. M., *Physics of the Earth*** — vertical motion and
  the time dependence of any benchmark.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 14. Related lessons

- [01 Determining the Geoid: Stokes, Remove-Restore, Kriging](01-geoid-determination.md) —
  the geoid model whose error a modernised datum inherits.
- [03 Sea Surface Topography and the Marine Geoid](03-sea-surface-topography.md) —
  where the datum's origin (mean sea level) differs from the geoid.
- [07-04-02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](../04-geodesy-reference-frames/02-height-systems.md) —
  the definitions used here.
- [07-04-04 GNSS for Tectonics, Subsidence and Sea Level](../04-geodesy-reference-frames/04-gnss-geodesy-applications.md) —
  the vertical motion that makes a height epoch-dependent.

## 15. Related modules

- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md).
- [07-02 Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  the gravity data that levelling needs.
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md) — the
  long-wavelength field behind the geoid model.
- [23 Field Methods and Instruments](../../23-field-methods-instruments/README.md) —
  the levelling and GNSS practice.
- [26-reference-library](../../26-reference-library/README.md).

## 16. Self-assessment checklist

- [ ] I can derive a geopotential number from levelling and gravity.
- [ ] I can compute dynamic, orthometric and normal heights.
- [ ] I can compute an orthometric correction and say why it is systematic.
- [ ] I can distinguish a datum offset from a height-system difference.
- [ ] I can build the GNSS+geoid error budget and find the crossover length.
- [ ] I can list what modernisation changes and what it does not.
- [ ] I can state the publications that make a datum change verifiable.
