---
id: 07-07-03
title: "Sea Surface Topography and the Marine Geoid"
level: doctoral
prereqs: ["07-07-01", "07-07-02", "07-06-03"]
tags: [gravity, geodesy, geoid, sea-surface-topography, geostrophic-flow, altimetry]
---

# Sea Surface Topography and the Marine Geoid

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the mean dynamic topography (MDT) as the difference between the sea
   surface and the geoid, and **state** why it is not zero.
2. **Derive** the geostrophic balance and **compute** the velocity and transport
   implied by a given MDT.
3. **Quantify** how a geoid error propagates into a velocity error, and **explain**
   why the error grows towards short wavelengths.
4. **Compare** the MDT spectrum with a stated geoid-error spectrum and **find** the
   wavelength below which the circulation cannot be recovered.
5. **Explain** why altimetry alone cannot determine the ocean's absolute
   circulation, and what combination of data can.
6. **State** the independent observations that validate a geoid-based circulation,
   and why the geoid and the ocean cannot check each other.
7. **Write** a circulation claim that names the geoid model, the error band and the
   validation data.

## Prerequisites

- [01 Determining the Geoid: Stokes, Remove-Restore, Kriging](01-geoid-determination.md) —
  where the geoid model and its error come from.
- [02 Vertical Datum Modernisation and National Height Systems](02-vertical-datum-modernisation.md) —
  the same geoid used as a vertical reference.
- [07-06-03 Earth Rotation, Polar Motion, LOD and Excitation](../06-earth-tides-and-rotation/03-earth-rotation.md) —
  the reference frame and rotation parameters needed to refer altimetry to a
  terrestrial frame.

> **All models and data in this module are SYNTHETIC.** The jet, the geoid, the
> geoid-error levels and the validation strategy are teaching constructs. No
> measured sea surface, geoid model or ocean current is used.

## 1. Why the sea surface is not the geoid

If the ocean were at rest, its surface would be an equipotential of gravity — the
geoid. It is not at rest, and the persistent slopes that drive its currents appear
as a departure from the geoid:

$$\text{MDT} = \text{SSH} - N \quad (\text{mean dynamic topography}),$$

of order $1$–$2\ \mathrm{m}$ over the ocean basins. The scale comparison is what
makes the marine geoid hard: the geoid undulation $N$ is of order
$100\ \mathrm{m}$, so the ocean's signal is a **$\sim1\%$ departure** from the
quantity that must be subtracted from an altimetric measurement.

Two systematic terms must be separated before the MDT means anything:

- **the geoid** (a gravity quantity, tens of metres);
- **the ocean's response to the atmosphere** — the inverted-barometer effect and
  the wind-driven set-up — which is of order decimetres and is removed with
  atmospheric pressure fields;
- and the **steric** (density) contribution to sea level, which is a change in
  volume rather than in mass and is therefore invisible to gravity.

## 2. The geostrophic balance, and what a jet looks like

For a steady, frictionless, hydrostatic flow the horizontal momentum balance
reduces to

$$f\,v = g\,\frac{\partial \eta}{\partial x},
\qquad
f = 2\Omega\sin\varphi ,$$

with $f$ the Coriolis parameter, $\eta$ the MDT, and $x$ across the flow. The
demonstration uses a synthetic jet,
$\eta(x) = 1.00\ \mathrm{m}\,\operatorname{sech}^{2}(x/100\ \mathrm{km})$, at
$40^\circ$N where $f = 9.3746\times10^{-5}\ \mathrm{s^{-1}}$, and computes:

| $x$ (km) | $\eta$ (m) | $v$ (m/s) |
|---|---|---|
| $-300$ | 0.0099 | 0.0205 |
| $-150$ | 0.1807 | 0.3423 |
| $-60$ | 0.7116 | 0.7998 |
| 0 | 1.0000 | 0.0000 |
| 60 | 0.7116 | $-0.7998$ |
| 300 | 0.0099 | $-0.0205$ |

peak velocity $0.806\ \mathrm{m\,s^{-1}}$ and, with an effective depth of
$1000\ \mathrm{m}$, a transport of $209\ \mathrm{Sv}$.

*Worked example 1 (the slope that drives a jet).* A velocity of
$0.8\ \mathrm{m\,s^{-1}}$ at $40^\circ$N requires a cross-stream slope

$$\frac{\partial\eta}{\partial x} = \frac{fv}{g}
= \frac{(9.3746\times10^{-5})(0.8)}{9.81} = 7.6\times10^{-6},$$

i.e. **$7.6\ \mathrm{mm}$ of sea-surface height per kilometre**. Over the
$\sim130\ \mathrm{km}$ width of the jet that is about $1\ \mathrm{m}$, exactly the
synthetic amplitude. The ocean's energetic currents are therefore written in
millimetres of height per kilometre, which is the precision at which the geoid
must be known.

## 3. The geoid error appears directly in the velocity

Since $\text{MDT} = \text{SSH} - N$, a geoid error is an MDT error, and the
geostrophic balance **differentiates** it:

$$\delta v = \frac{g}{f}\frac{\partial (\delta N)}{\partial x}
= \frac{g}{f}\,k\,\delta N,
\qquad k = \frac{2\pi}{\lambda}.$$

*Worked example 2.* A geoid error of $5\ \mathrm{cm}$ at a wavelength of
$200\ \mathrm{km}$ gives, with $k = 2\pi/2\times10^{5} = 3.14\times10^{-5}\
\mathrm{m^{-1}}$,

$$\delta v = \frac{9.81}{9.3746\times10^{-5}}(3.14\times10^{-5})(0.05)
= 0.1644\ \mathrm{m\,s^{-1}},$$

which is $20.4\%$ of the jet's $0.806\ \mathrm{m\,s^{-1}}$. The demonstration
tabulates $1$, $5$ and $20\ \mathrm{cm}$ of geoid error: $\delta v = 0.033$,
$0.164$ and $0.658\ \mathrm{m\,s^{-1}}$, i.e. $4.1\%$, $20.4\%$ and $81.6\%$ of
the jet.

**The error grows as $1/\lambda$** — the differentiation penalises short
wavelengths — so a geoid model that is excellent in the mean can still be useless
for a western-boundary current whose signal sits at a few hundred kilometres.

## 4. Where the signal stops: MDT spectrum against geoid error

The honest comparison is spectrum against spectrum. The demonstration takes the
Fourier transform of its synthetic jet and compares it with a constant $5\
\mathrm{cm}$ geoid error:

| wavelength | MDT amplitude | geoid error | signal/error |
|---|---|---|---|
| 50 km | 0.000 cm | 5.00 cm | 0.000 |
| 100 km | 0.034 cm | 5.00 cm | 0.007 |
| 200 km | 2.369 cm | 5.00 cm | 0.474 |
| 400 km | 14.054 cm | 5.00 cm | 2.811 |
| 800 km | 21.984 cm | 5.00 cm | 4.397 |
| 1200 km | 29.843 cm | 5.00 cm | 5.969 |

The MDT amplitude falls with decreasing wavelength while the geoid error does not,
so the two cross: with these numbers the MDT falls below the geoid error at
wavelengths shorter than **$267\ \mathrm{km}$**.

Three statements that must be kept separate:

1. **The number $267\ \mathrm{km}$ is not a constant.** It is a property of the
   assumed error spectrum and of the jet. Change either and it moves.
2. **The structure of the argument is general**: a geoid error of a given size at
   a given wavelength limits the oceanographic scales that can be recovered, and
   the limit must be computed for the specific model rather than quoted.
3. **The requirement is relative, not absolute.** A "$1\ \mathrm{cm}$ geoid" is
   neither necessary nor sufficient: what matters is the error in the band the
   oceanographic target occupies. Basin-scale transports live at thousands of
   kilometres; jets at hundreds.

## 5. What altimetry alone cannot do

Satellite altimetry measures the sea surface height above a reference ellipsoid to
centimetres, at wavelengths from tens of kilometres upward. It therefore measures
$\text{SSH} = N + \text{MDT}$ and cannot separate the two terms without an
independent $N$. A geoid model is that independent information, and — this is the
central difficulty — **the geoid and the ocean cannot check each other**, because
any error in $N$ appears as an ocean current that looks entirely plausible.

The validation must therefore be *external*:

| validation data | what it tests | what it cannot test |
|---|---|---|
| drifting buoys and shipboard ADCP | the velocity field at the surface | absolute transport |
| Argo float displacements | the deep velocity shear and the reference level | the surface geostrophic part alone |
| moored current meters | the absolute transport across a section | spatial coverage |
| satellite gravity (the geoid itself) | the gravity field's consistency | whether the *ocean* is consistent with it |
| a longer altimetric record | the *mean* MDT, by averaging the eddy field | the geoid error, which does not average down |

The last row is worth stating as a principle: **averaging in time reduces the
ocean's variability but not the geoid error**, so a very long altimetric record
converges to the truth *plus the geoid error*, not to the truth.

## 6. Assumptions and regime of validity

1. **Geostrophic balance.** Valid where the Rossby number is small
   ($\mathrm{Ro} = U/(fL) \ll 1$): away from the equator and for scales larger
   than the deformation radius. Near the equator $f \to 0$ and the balance fails;
   the demonstration's $f$ is at $40^\circ$N.
2. **A level of no motion or an independent reference.** The geostrophic velocity
   from a height field is *baroclinic* unless a reference velocity is assumed; the
   MDT gives the surface-referenced part.
3. **A known geoid.** The MDT is only as good as the geoid in the target band.
4. **Mean fields.** The demonstration's jet is a *mean* MDT; altimetry measures
   instantaneous SSH, whose eddy variability is a separate (and larger) signal at
   short scales.
5. **The inverted-barometer and steric corrections are applied**, and each is a
   model with its own error.
6. **The reference frame and the rotation parameters are adequate**, since SSH is
   referred to an ellipsoid in a terrestrial frame.

## 7. Python demonstration

`code/sea_surface_topography_demo.py` prints, with units:

1. **A synthetic jet** ($1.00\ \mathrm{m}$ sech², $100\ \mathrm{km}$ half-width) at
   $f = 9.3746\times10^{-5}\ \mathrm{s^{-1}}$: peak velocity
   $0.806\ \mathrm{m\,s^{-1}}$, transport $209\ \mathrm{Sv}$.
2. **The velocity error** from geoid errors of $1$, $5$ and $20\ \mathrm{cm}$ at a
   $200\ \mathrm{km}$ wavelength: $0.033$, $0.164$, $0.658\ \mathrm{m\,s^{-1}}$
   ($4.1\%$, $20.4\%$, $81.6\%$ of the jet).
3. **The spectrum comparison** and the crossover at **$267\ \mathrm{km}$** for a
   constant $5\ \mathrm{cm}$ error.
4. **The validation argument**, and the statement that a longer altimetric record
   does not reduce a geoid error.

Print-only, fixed seed, no network, exits 0.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/03-sea-surface-topography-exercises.md`](./exercises/03-sea-surface-topography-exercises.md)
and
[`exercises/03-sea-surface-topography-solutions.md`](./exercises/03-sea-surface-topography-solutions.md).

- **★** Compute the cross-stream slope required for a $0.5\ \mathrm{m\,s^{-1}}$
  current at $50^\circ$N, in millimetres per kilometre.
- **★** Compute the geostrophic velocity implied by a $2\ \mathrm{m}$ MDT across a
  $200\ \mathrm{km}$ jet at $35^\circ$N (use a constant slope estimate).
- **★★** Compute the velocity error from a $3\ \mathrm{cm}$ geoid error at
  wavelengths of $100$, $300$ and $1000\ \mathrm{km}$, and state which scale the
  geoid model must be good at for a jet of that width.
- **★★** Explain why a $20$-year altimetric mean does not reduce the geoid error,
  and what it does reduce.
- **★★★** Design a validation experiment for an MDT product, specifying the
  independent data, the diagnostic at each scale, and the degeneracy that remains.

## 9. Mastery checkpoint

Do this without notes:

> A $1.2\ \mathrm{m}$ MDT jet of $120\ \mathrm{km}$ half-width at $40^\circ$N
> ($f = 9.3746\times10^{-5}\ \mathrm{s^{-1}}$) is to be derived from altimetry and
> a geoid model with a $4\ \mathrm{cm}$ error at $250\ \mathrm{km}$ wavelength.
> **(a)** Compute the required cross-stream slope and the peak geostrophic
> velocity. **(b)** Compute the velocity error from the geoid error at that
> wavelength, as a fraction of the jet. **(c)** State whether the jet is
> recoverable at that scale, and what would be needed if not. **(d)** State two
> independent observations that could validate the recovered velocity.
> **(e)** Explain why increasing the altimetric record length does not help with
> the geoid error.

*Answers.* **(a)** For a $1.2\ \mathrm{m}$ amplitude and a $120\ \mathrm{km}$
half-width the maximum slope of sech² is about $0.77\times(1.2/1.2\times10^{5})
= 7.7\times10^{-6}$ (dimensionless), so

$$v_{\max} = \frac{g}{f}\frac{\partial\eta}{\partial x}
= \frac{9.81}{9.3746\times10^{-5}}(7.7\times10^{-6}) = 0.806\
\mathrm{m\,s^{-1}}.$$

**(b)** At $\lambda = 250\ \mathrm{km}$, $k = 2\pi/2.5\times10^{5}
= 2.513\times10^{-5}\ \mathrm{m^{-1}}$, so

$$\delta v = \frac{9.81}{9.3746\times10^{-5}}(2.513\times10^{-5})(0.04)
= 0.1052\ \mathrm{m\,s^{-1}} = 13.1\%\ \text{of the jet}.$$

**(c)** Recoverable in principle at the $13\%$ level — acceptable for a transport
estimate, marginal for a jet-core study. Improving the geoid error to
$1\ \mathrm{cm}$ would reduce the velocity error to $2.6\%$; alternatively, use a
low-pass filter matched to the scales where the geoid is good, and state that the
short scales are interpolated from an ocean model rather than measured.
**(d)** Drifting buoys or shipboard ADCP sections (surface velocity), and moored
current meters (absolute transport across a section); Argo displacements provide
an independent shear profile.
**(e)** The geoid error is a *fixed* field, not a random one: it is the same in
every cycle of the altimeter, so averaging reduces only the ocean's own
variability (the eddy field) and leaves the geoid-induced part of the MDT
untouched. A 20-year mean converges to the truth plus the geoid error.

## 10. Common pitfalls

1. **Treating the MDT as a measurement.** It is a difference between a
   measurement and a model.
2. **Quoting a geoid accuracy without the band.** A $1\ \mathrm{cm}$ geoid at
   $2000\ \mathrm{km}$ wavelength says nothing about a $200\ \mathrm{km}$ jet.
3. **Forgetting the differentiation.** The velocity error scales as $k\delta N$,
   so short wavelengths are penalised.
4. **Assuming averaging removes geoid error.** It removes variability, not bias.
5. **Comparing an MDT with a model's MDT computed against a different geoid.**
   The difference of two MDTs is the difference of two geoid models.
6. **Ignoring the steric and inverted-barometer terms.** Both are decimetre-scale
   and neither is in the geoid.
7. **Applying the geostrophic balance near the equator.** $f \to 0$ and the
   balance fails.

## 11. Real-world applications

- **Absolute ocean transports.** Heat and freshwater transports require absolute
  velocities, which only a geoid-based MDT can supply from space.
- **Altimeter product development.** Every MDT product is defined by its geoid
  model and its error band, and the two must be published together.
- **Sea-level and climate.** The separation of mass (gravity) from steric
  (density) sea-level change requires the geoid and the altimeter together.
- **Navigation and geodesy.** The marine geoid is also the vertical datum over the
  ocean, and hence the reference for offshore engineering and for any height
  referred to a coastal datum (see [02](02-vertical-datum-modernisation.md)).

## 12. Further reading

- **Torge, W. & Müller, J., *Geodesy*** — the geoid over the oceans and the use of
  altimetry.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — the boundary-value
  problem in its marine setting.
- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the classical treatment
  of sea surface topography and the geoid.
- **Turcotte, D. L. & Schubert, G., *Geodynamics*** — the physical oceanography
  and geostrophy assumed here.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 13. Related lessons

- [01 Determining the Geoid: Stokes, Remove-Restore, Kriging](01-geoid-determination.md) —
  the geoid model that the MDT subtracts.
- [02 Vertical Datum Modernisation and National Height Systems](02-vertical-datum-modernisation.md) —
  the geoid as a datum, on land and offshore.
- [07-05-05 Applications: Groundwater Depletion, Ice Loss, Sea Level](../05-satellite-gravimetry/05-grace-applications.md) —
  the mass (gravity) part of sea-level change, which this lesson's steric part
  complements.
- [07-04-04 GNSS for Tectonics, Subsidence and Sea Level](../04-geodesy-reference-frames/04-gnss-geodesy-applications.md) —
  the land-motion part of the same budget.

## 14. Related modules

- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md).
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md).
- [07-06 Earth Tides and Rotation](../06-earth-tides-and-rotation/README.md).
- [15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md) —
  where the MDT is used.
- [26-reference-library](../../26-reference-library/README.md).

## 15. Self-assessment checklist

- [ ] I can define the MDT and say why it is not zero.
- [ ] I can compute the geostrophic velocity and transport from an MDT.
- [ ] I can compute the velocity error from a geoid error and a wavelength.
- [ ] I can compare an MDT spectrum with a geoid-error spectrum.
- [ ] I can explain why altimetry alone gives no absolute circulation.
- [ ] I can name the independent data that validate an MDT product.
- [ ] I can explain why averaging does not reduce a geoid error.
