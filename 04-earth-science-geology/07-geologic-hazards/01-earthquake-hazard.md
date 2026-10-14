---
id: 04-07-01
title: "Earthquake Hazard and Ground Motion"
level: advanced
prereqs: ["04-04-02", "02-03-01", "04-02-05"]
estimated_minutes: 75
tags: [earthquakes, ground-motion, seismic-hazard, site-response, response-spectrum]
---

# Earthquake Hazard and Ground Motion

An earthquake is not a hazard. A hazard is what happens to a building, a bridge
or a slope when the ground under it moves in a particular way for a particular
length of time, and the chain from a rupture on a fault to the load on a column
has four links: **source**, **path**, **site** and **structure**. Each link is a
separate physical problem, each one is where the previous link's uncertainties
become somebody else's input, and the discipline that adds them up is called
probabilistic seismic hazard analysis.

This lesson builds the mechanical content of the first three links and the
element of the fourth that can be derived. It deliberately stops where
[06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
begins: the recurrence statistics, the logic trees, the ground-motion models and
the disaggregation of a hazard curve belong there, and duplicating them here
would create two versions of the same subject that could drift apart. What this
lesson owes that one is the physics of the terms being summed.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the three magnitude scales that matter for different
   purposes — local, surface-wave and moment magnitude — and state which one is
   defined by a physical quantity rather than by an amplitude on an instrument.
2. **Derive** the seismic moment of a rectangular rupture and compute a moment
   magnitude, and state where the offset in the magnitude relation comes from
   and why two published offsets disagree by 0.037.
3. **Explain** the empirical magnitude–energy relation, identify the slope as a
   fitted constant rather than a derivation, and compute the energy ratio
   between two magnitudes.
4. **Derive** the free-surface amplification of a vertically incident SH wave
   and explain why the factor of 2 is not a site effect.
5. **Derive** the transfer function of a single elastic layer over a half-space,
   obtain the resonant amplification as the impedance ratio, and compute the
   fundamental frequency $f_0 = v_S/(4H)$.
6. **Compute** the amplitude decay of a body wave and a surface wave from
   geometric spreading and anelastic attenuation, and state which term dominates
   where.
7. **Derive** the steady-state dynamic amplification $1/(2\zeta)$ of a
   single-degree-of-freedom oscillator and interpret a response spectrum.
8. **Compute** the geometric transit probability of a recurrence model and a
   Poisson probability of exceedance, and say which of the numbers involved is
   estimated rather than computed.
9. **State** the regime of validity of each relation in this lesson, and in
   particular what a vertical-incidence one-dimensional site-response
   calculation cannot represent.

## Prerequisites

- [04-04-02 Fault Geometry, Kinematics and Fault Classification](../04-structural-geology/02-faults.md)
  — strike, dip, rake, slip and rupture area. The seismic moment is built from
  these.
- [02-03-01 Simple Harmonic Motion and Small-Oscillation Approximation](../../02-physics/03-oscillations-and-waves/01-simple-harmonic-motion.md)
  — the oscillator whose response spectrum is defined here, and the language of
  resonance that §4 uses.
- [04-02-05 Tectonics and the Distribution of Earthquakes and Volcanoes](../02-plate-tectonics/05-tectonics-hazards.md)
  — where the earthquakes are and why, which is what a hazard map inherits.

## 1. Magnitude is not one number

Three scales are in everyday use and they answer different questions.

**Local magnitude $M_\mathrm{L}$** is defined by the maximum trace amplitude
recorded on a specified seismograph as a function of distance. It was designed
for California and it **saturates**: above about $M_\mathrm{L} = 7$ the recorded
amplitude stops growing because the recording system's dominant period no longer
matches the radiated spectrum, so two very different earthquakes report similar
$M_\mathrm{L}$.

**Surface-wave magnitude $M_\mathrm{s}$** is defined from the amplitude of
surface waves with periods near 20 s. It works to larger size but it too
saturates, because a 20 s wave samples only the shallowest part of a long
rupture.

**Moment magnitude $M_\mathrm{w}$** is defined from the seismic moment, which is
a physical quantity:

$$M_0 = \mu \bar{D} A , \tag{1}$$

with $\mu$ the shear modulus at the source, $\bar{D}$ the average slip on the
rupture, and $A$ its area. $M_0$ has units of N m, i.e. of torque, and it does
not saturate because a bigger earthquake has more slip, more area, or both.

The scale is defined so that $M_\mathrm{w}$ agrees with the amplitudes
$M_\mathrm{s}$ was built to measure, which is why the relation contains a
constant that is a convention rather than a derivation:

$$M_\mathrm{w} = \tfrac{2}{3}\log_{10} M_0 - 10.7 \qquad (M_0 \text{ in dyn cm}). \tag{2}$$

Modern practice quotes $M_0$ in N m, and the usual N m form is written with the
offset $-6.07$. Convert (2) exactly — one newton-metre is $10^7$ dyn cm — and
the offset becomes

$$-10.7 + \tfrac{2}{3}\cdot 7 = -6.0333 . \tag{3}$$

The two offsets differ by 0.037 magnitude units, which is a factor of
$10^{1.5\times0.037} = 1.13$ in $M_0$. Both are in the literature, because the
offsets were rounded independently when the N m form was adopted. This is worth
knowing for one reason: a magnitude is a *reporting convention*, and when two
catalogues disagree by a few hundredths in $M_\mathrm{w}$ the reason is usually
the convention rather than the earthquake.

## 2. Seismic moment and radiated energy

The moment is the quantity a source model produces. A rupture 50 km long and
20 km wide with 2 m of mean slip in rock with $\mu = 30$ GPa gives

$$M_0 = 3.0\times10^{10} \times (5\times10^{4})(2\times10^{4}) \times 2.0
= 6.0\times10^{19}\ \mathrm{N\,m},$$

and hence $M_\mathrm{w} = 7.15$. Every input in that line is uncertain by tens of
per cent: $\mu$ varies with depth and rock type, $\bar{D}$ is a spatial average
over a heterogeneous slip field, and $A$ depends on how the rupture is
delimited. A moment magnitude quoted to three decimals is therefore quoted to
one decimal of physics.

The energy radiated as elastic waves is *not* $M_0$ and is not proportional to
it. The empirical Gutenberg–Richter relation is

$$\log_{10} E \,[\mathrm{J}] = 1.5\,M + 4.8 , \tag{4}$$

so a unit of magnitude is a factor of $10^{1.5} = 31.6$ in energy, and the
slope $3/2$ is a *fitted constant*. It is not derived here and it is not derived
anywhere in this lesson. Its consequence is the shape of the hazard problem: one
magnitude unit is a factor of 31.6 in energy but only about a factor of 3 in
ground-motion amplitude, because amplitude depends on energy only through a
square root (and on the source spectrum, the path and the site).

The ratio $E/M_0$ is an *apparent stress* — a measured, source-specific quantity
that varies between earthquakes by more than an order of magnitude. Two
earthquakes of the same moment can therefore radiate very different amounts of
high-frequency energy, which is why magnitude alone does not tell you what a
city will feel.

## 3. Path: geometric spreading and attenuation

A body wave from a point source spreads over a sphere, so its amplitude falls as
$1/r$; a surface wave spreads over a cylinder, so it falls as $1/\sqrt{r}$. In
addition, anelastic attenuation removes energy at a rate set by the quality
factor $Q$:

$$A(r) = A_0\,\frac{r_0}{r}\,
\exp\!\left[-\frac{\pi f (r - r_0)}{Q v}\right] \tag{5}$$

for a body wave, with $1/\sqrt{r}$ replacing $1/r$ for a surface wave. Both
factors are derived: the geometric one from conservation of energy on a sphere
or cylinder, the exponential from the definition of $Q$ as
$2\pi \times$ (energy stored)/(energy lost per cycle).

With $Q = 300$, $v = 3500$ m s⁻¹ and $f = 2$ Hz, the anelastic exponent is

$$\frac{\pi f}{Qv} = \frac{\pi \times 2}{300 \times 3500}
= 5.984\times10^{-6}\ \mathrm{m^{-1}} , \tag{6}$$

so over 90 km of path the amplitude is reduced by $e^{-0.54} = 0.58$. The
geometric term over the same path is $10/100 = 0.10$. **Geometric spreading
dominates anelastic attenuation by a factor of about six at regional distance**,
and the balance only reverses when $r$ becomes comparable with $Qv/(\pi f)$,
which is $1.7\times10^5$ m here — 170 km. That is the length scale at which a
regional network stops being able to use amplitude as a distance measure.

## 4. Site: the factor of two, and the impedance ratio

**The free-surface doubling.** Consider a vertically propagating SH wave in a
homogeneous half-space with a free surface. The free surface cannot support
shear traction, so the shear stress must vanish there. Write the displacement as
the sum of an upgoing wave $A e^{ikz}$ and a downgoing reflected wave
$B e^{-ikz}$; the traction-free condition at $z = 0$ gives $A = B$, and hence a
surface displacement of $2A$ against an incident displacement of $A$. The
amplification is **exactly 2**, for any frequency, in any medium, at normal
incidence, and it is the reason a downhole and a surface sensor record different
motions. It is not a site effect: it happens on bare rock as well.

**The impedance ratio.** Put a layer of thickness $H$, density $\rho_1$ and shear
velocity $v_1$ over a half-space with $\rho_2$, $v_2$, and take the SH wave
vertical again. Displacement is $u_1 = U\cos(k_1 z)$ in the layer, which already
satisfies the free surface, and
$u_2 = I e^{-ik_2 z} + R e^{ik_2 z}$ in the half-space. Continuity of
displacement and of shear traction at $z = H$ gives two equations, and the
normalisation that the *bedrock outcrop* motion is $2I$ (the free-surface
response of the half-space alone) produces

$$|T(f)| = \frac{1}{\sqrt{\cos^2(k_1H)
+ \left(\frac{Z_1}{Z_2}\right)^{\!2}\sin^2(k_1H)}} ,
\qquad Z_i = \rho_i v_i . \tag{7}$$

At the resonances $k_1H = \pi/2,\ 3\pi/2,\ \dots$ the cosine vanishes and

$$|T|_\mathrm{max} = \frac{Z_2}{Z_1} = \frac{\rho_2 v_2}{\rho_1 v_1} , \tag{8}$$

so the peak amplification of a soft layer relative to the rock it sits on is
**the impedance contrast**, and the fundamental frequency is

$$f_0 = \frac{v_1}{4H} . \tag{9}$$

For $H = 50$ m of material with $v_S = 200$ m s⁻¹ and $\rho = 1800$ kg m⁻³ over
rock with $v_S = 800$ m s⁻¹ and $\rho = 2500$ kg m⁻³, the impedances are
$3.6\times10^5$ and $2.0\times10^6$ kg m⁻² s⁻¹, so $|T|_\mathrm{max} = 5.56$ at
$f_0 = 1.00$ Hz. Note that the factor of 2 does **not** multiply this: it applies
to the soil surface and to the rock outcrop alike, so it cancels in the ratio and
appears only when you compare a surface motion with the *incident* wave.

Equation (8) is the single most useful number in engineering seismology.
It says that the damage potential of a site is set by a property that a seismic
refraction line or an array measurement can determine — $v_S$ and, less often,
density — and it says that the tuning is to a frequency, which is what makes a
city of tall buildings and a city of low ones respond differently to the same
earthquake.

## 5. Structure: the single-degree-of-freedom oscillator

A building, to first order, is a mass on a spring. Its equation of motion under
a ground acceleration $\ddot u_g(t)$ is

$$\ddot x + 2\zeta\omega_0\dot x + \omega_0^2 x = -\ddot u_g(t) , \tag{10}$$

with $\omega_0 = 2\pi/T$ and $\zeta$ the damping ratio. For harmonic forcing at
frequency $\omega$ the steady-state relative displacement has amplitude

$$|x| = \frac{|a_g|}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\zeta\omega_0\omega)^2}} , \tag{11}$$

and at resonance $\omega = \omega_0$ this is

$$|x|_\mathrm{max} = \frac{|a_g|}{2\zeta\omega_0^2}
\quad\Longrightarrow\quad
\omega_0^2|x|_\mathrm{max} = \frac{|a_g|}{2\zeta} . \tag{12}$$

The quantity $\omega_0^2|x|$ is called the **pseudo-acceleration** and it has the
units of acceleration; it is what a response spectrum plots against period
(Figure-free, but you can compute it: `response spectrum` below). The peak
value $1/(2\zeta) = 10$ for $\zeta = 0.05$ is the amplification a lightly damped
structure experiences, and it is why damping is worth more than strength in a
resonant situation.

## 6. A response spectrum, and what a hazard curve is

Run the ground motion through (10) for a set of periods and plot the
pseudo-acceleration against period: that is the **response spectrum**. For a
short, energetic pulse, the spectrum peaks near the period of the pulse, and the
peak value is typically 2 to 3 times the peak ground acceleration for 5 per cent
damping. That factor of 2 to 3 is the whole reason a design spectrum exists: a
building does not experience the ground acceleration, it experiences its own
response to it.

A **hazard curve** is the probability, per year, that the spectral acceleration
at a given period exceeds a given level. The three ingredients are: how often
earthquakes of each size occur near the site (a recurrence model, from a
catalogue and a fault inventory), how much shaking each produces (a
ground-motion model, empirical or simulated), and how the probability of
exceeding a level is accumulated over all possible sources and magnitudes. The
first is a fitted empirical law, the second is a regression on recorded data or a
simulation, and only the third is arithmetic that can be checked. That asymmetry
is not a defect of the method; it is the method, and it is why a hazard
assessment is quoted with an uncertainty and a logic tree rather than as a
number.

The recurrence side has one piece of arithmetic that belongs here because it is
pure probability. If exceedances are independent events with a mean rate
$\lambda$, the number in a time $t$ is Poisson and

$$P(\text{at least one in } t) = 1 - e^{-\lambda t} . \tag{13}$$

The Gutenberg–Richter relation $N(\ge M) = 10^{a - bM}$ is *empirical*, with
$b \approx 1$ for most catalogues and $b$ itself varying between tectonic
settings. What matters here is the shape: the rate increases by a factor of 10
per unit decrease in magnitude while the ground motion decreases by a factor
near $3$, so the hazard is usually dominated by **moderate** earthquakes close
by, not by the largest possible event. That conclusion follows from the two
scalings and is a genuine, checkable result of the arithmetic — the numbers in
the scalings are not.

## 7. Physical interpretation

- A magnitude is a statement about a source, not about shaking. Two $M_0$ equal
  events at different depths, with different rupture directivity and different
  stress drops, produce different ground motions.
- The **site term is a ratio of impedances**, so it is a material property that
  can be measured before an earthquake. It is the one link in the chain that a
  geophysical survey can pin down in quiet conditions.
- The **factor of two** and the impedance ratio are different quantities. The
  first is a boundary condition, the second is a resonance. Confusing them is
  the most common conceptual error in this subject.
- The response spectrum is a *set of structures*, not a ground motion. Nothing
  physical oscillates at all periods at once; the spectrum is a cataloguing
  device.

## 8. Units and dimensional analysis

Every relation above can be checked dimensionally, and two of them hide a
constant that is not dimensionless.

| Quantity | Expression | Units |
|---|---|---|
| Seismic moment | $\mu \bar D A$ | Pa × m × m² = N m |
| Moment magnitude | $\frac{2}{3}\log_{10}M_0 - 6.0333$ | dimensionless, with a convention-dependent offset |
| Anelastic exponent | $\pi f/(Qv)$ | s⁻¹ × s m⁻¹ = m⁻¹ |
| Impedance | $\rho v$ | kg m⁻³ × m s⁻¹ = kg m⁻² s⁻¹ |
| Fundamental frequency | $v/(4H)$ | (m s⁻¹)/m = s⁻¹ |
| Dynamic amplification | $1/(2\zeta)$ | dimensionless |
| Poisson exceedance | $1 - e^{-\lambda t}$ | dimensionless, $\lambda t$ dimensionless |

The offsets in the magnitude relation are not dimensionless in the sense that
matters: they were chosen to make one scale agree with another, and they carry
the unit of the $\log_{10}$ argument with them. Always state the unit of $M_0$
when you quote an offset.

## 9. Assumptions and regime of validity

1. **Linear elasticity** in §3 to §5. Real soils are nonlinear above roughly
   $10^{-4}$ shear strain, $v_S$ falls, damping rises, and the resonant
   frequency of the site drifts downward during strong shaking. A linear site
   response is the *small-strain* limit.
2. **One-dimensional, horizontally layered, vertically incident** in §4. This
   ignores surface waves, basin edge effects, two- and three-dimensional
   focusing, and the coupling between vertical and horizontal motion. Basins
   amplify by more than the impedance ratio for reasons this model cannot see.
3. **Constant $Q$, frequency-independent** in §3. Real attenuation is mildly
   frequency-dependent, which is why $Q$ is quoted for a band.
4. **A point source and a single path** in §3. A finite rupture radiates
   differently in different directions (**directivity**), and this can double the
   ground motion at a site in the rupture's forward direction. It is not a small
   correction.
5. **Pseudo-static and single-degree-of-freedom** in §5. Real structures have
   many modes, and only the modes near the dominant ground-motion period matter.
6. **Poisson occurrence** in (13). Clustered aftershocks and quasi-periodic
   characteristic earthquakes violate it, in opposite directions.

## 10. Python demonstration

[`code/earthquake_hazard_demo.py`](./code/earthquake_hazard_demo.py) computes
every quantity in this lesson from the printed inputs. It labels each model
input NOMINAL and each empirical constant as empirical, and it verifies two
things numerically: the numerically located maximum of (7) against the closed
form (8), and a Newmark-$\beta$ integration of (10) against the closed form
(12).

The moment and magnitude section:

```text
  M0 = mu * A * D         = 6.000000e+19 N m
  M0 in dyn cm            = 6.000000e+26 dyn cm
  Mw from dyn cm form     = 7.1521
  Mw from converted offset= 7.1521   (offset -6.0333)
  Mw from the usual -6.07 = 7.1154
  difference between the two SI conventions = 0.0367 magnitude units
  -> a factor 1.1350 in M0: the offsets were rounded
     independently in the literature, and both are in use.
```

The site response, where the transfer function is checked against the impedance
ratio:

```text
  numerical maximum of |T| = 5.555556 at f = 13.0000 Hz
  (grid offset from the exact resonances on purpose)
  closed form Z2/Z1        = 5.555556
  relative difference      = 3.061e-10
```

The oscillator check and the response spectrum:

```text
    T (s)   peak|x| (m)   w^2 peak|x|   1/(2 zeta)   rel. diff
    0.50      0.063322      9.99946     10.00000   5.37e-05
    1.00      0.253300      9.99987     10.00000   1.32e-05
    2.00      1.013208      9.99997     10.00000   3.30e-06
```

```text
    T (s)    Sa (m/s^2)    Sd (m)   Sa/PGA
    0.30       1.9966    0.00453    1.997
    0.40       2.3911    0.00965    2.391
    0.50       2.0933    0.01319    2.093
    1.00       0.6031    0.01516    0.603
```

### What to observe

- The integrator reproduces $1/(2\zeta)$ to a few parts in $10^5$, which is what
  licenses its use on a ground motion with no closed form. Verifying an
  integrator on a case with an answer is not a formality; it is the only way to
  know that the code's period, its forcing and its damping convention are all
  what you think they are.
- The response-spectrum peak sits at $T = 0.40$ s for a pulse whose dominant
  period is $0.50$ s. The peak is *near*, not *at*, the pulse period: a pulse is
  not a harmonic wave and its spectrum is broad. Any statement that a building
  "resonates with an earthquake" is a shorthand for a comparison of two broad
  spectra.
- The peak spectral acceleration is $2.39\times$ the peak ground acceleration.
  For 5 per cent damping and a pulse-like motion this ratio is routinely
  between 2 and 3, and it never approaches $1/(2\zeta) = 10$, because a pulse
  does not last long enough to drive an oscillator to steady state.

## 11. Common mistakes

1. **Multiplying by the factor of 2 twice.** It applies to the soil surface and
   to the rock outcrop; in the ratio it cancels. A site amplification of
   $2\times5.56 = 11.1$ is wrong; the answer is $5.56$ relative to the outcrop.
2. **Quoting a magnitude without its scale.** $M_\mathrm{L}$, $M_\mathrm{s}$ and
   $M_\mathrm{w}$ differ systematically at large size, and two catalogues using
   different scales differ by tenths.
3. **Treating the energy relation as derived.** The slope $3/2$ is fitted. Use
   it to compare energies, not to compute a source property.
4. **Using $1/(2\zeta)$ as the spectral amplification.** It is the steady-state
   harmonic value, an upper bound that a transient rarely reaches.
5. **Forgetting the impedance in the amplification.** A low-velocity layer with
   a high density may have a small impedance contrast and amplify very little.
6. **Assuming a resonant period from the soil type.** $f_0 = v_S/(4H)$ needs
   both numbers, and $v_S$ for the same described soil spans a factor of two.
7. **Using the surface acceleration as the engineering demand.** It is not; the
   structural response is.
8. **Reporting a hazard as a deterministic worst case.** A worst case is not a
   probability, and a probability requires the recurrence model and its
   uncertainty.
9. **Confusing the return period with the lifetime probability.** A 500-year
   return period is a 10 per cent chance in 50 years (from (13)), not a
   guarantee of one event per 500 years.
10. **Assuming the largest possible earthquake dominates the hazard.** Because
    the rate grows tenfold per magnitude unit while the motion grows by about
    three, it usually does not.

## 12. Real-world applications

- **Building codes.** Design spectra are specified as spectral acceleration
  against period, which is the language of §5 and §6, not of magnitude.
- **Site characterisation.** $v_S$ to 30 m depth, or the impedance profile, is
  the measurement that ties a code's site class to a real place
  ([05-05 Survey Design and Data Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md)
  for the acquisition, [06-10 Refraction and Near-Surface
  Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  for the method).
- **Strong-motion networks.** The recordings that calibrate ground-motion models
  are the same records used to test a site-response calculation.
- **Induced seismicity.** The same moment–magnitude conversion applies to
  events caused by fluid injection; the difference is in the source physics and
  in the depth, not in the arithmetic
  ([06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md)).
- **Insurance and catastrophe modelling.** The same four links, with the
  exposure and vulnerability of the built environment appended.
- **Early warning.** A warning system exploits the difference between the
  propagation speed of the information-carrying electronic signal and the
  $3$ to $7$ km s⁻¹ of the S wave.

## 13. Further reading

- **Kanamori, H. (1977). "The energy release in great earthquakes." *Journal of
  Geophysical Research*.** Where the moment magnitude scale and the energy
  relation were defined, and where the offsets in (2) are stated. Level: graduate,
  historical.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (University Science
  Books).** The source representation and the moment tensor; the reference for
  §1 and §2 beyond what this lesson derives. Level: graduate.
- **Hanks, T. C., & Kanamori, H. (1979). "A moment magnitude scale." *Journal of
  Geophysical Research*.** The short paper that made $M_\mathrm{w}$ standard.
  Level: advanced.
- **Kramer, S. L. *Geotechnical Earthquake Engineering* (Prentice Hall).** The
  standard text for §4 to §6: site response, the response spectrum and
  equivalent-linear analysis. Level: advanced to graduate.
- **USGS Earthquake Hazards Program, <https://earthquake.usgs.gov>.** The
  authoritative public source for event parameters, magnitudes and the
  conventions used in the ANSS catalogue; confirm any magnitude you quote
  against the catalogue's stated scale. The event service endpoint is
  <https://earthquake.usgs.gov/fdsnws/event/1/>. Level: reference.
- **USGS, *Preliminary Reference Earth Model* and its successors, distributed
  through the IRIS/EarthScope data services, <https://www.earthscope.org/data/>.**
  Where the $Q$ and velocity values used in this lesson's nominal examples come
  from, in a form you can query. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
  — the department where hazard analysis proper lives: recurrence models,
  logic trees, ground-motion models and disaggregation.
- [06-03 Earthquake Sources](../../06-seismology/03-earthquake-sources/README.md)
  — the moment tensor and the source spectrum behind the moment in (1).
- [06-04 Earthquake Location and Magnitude](../../06-seismology/04-earthquake-location-and-magnitude/README.md)
  — how $M_\mathrm{L}$ and $M_\mathrm{w}$ are actually determined from records.
- [06-05 Attenuation and Anelasticity](../../06-seismology/05-attenuation-and-anelasticity/README.md)
  — where $Q$ comes from and what it means.
- [04-04-02 Fault Geometry, Kinematics and Fault Classification](../04-structural-geology/02-faults.md)
  — the geometry that $A$ and $\bar D$ refer to.
- [04-07-05 Tsunami Generation, Propagation and Warning](./05-tsunami.md) — the
  hazard that follows a shallow, large, offshore rupture.
- [07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md)
  — the frames in which the GNSS deformation used in hazard studies is measured.

Exercises:
[`exercises/01-earthquake-hazard-exercises.md`](./exercises/01-earthquake-hazard-exercises.md)
and
[`exercises/01-earthquake-hazard-solutions.md`](./exercises/01-earthquake-hazard-solutions.md).

## Self-assessment checklist

- [ ] I can define $M_0$ and explain why it, unlike $M_\mathrm{L}$, does not
      saturate. (§1)
- [ ] I can compute a moment magnitude from a rupture and state which offset
      convention I used. (§2)
- [ ] I can state the empirical magnitude–energy relation, its slope, and why
      the slope is not derived. (§2)
- [ ] I can derive the free-surface factor of 2 from the traction-free boundary
      condition. (§4)
- [ ] I can derive $|T(f)|$ for a layer over a half-space and show that the
      resonance value is $Z_2/Z_1$. (§4)
- [ ] I can compute $f_0$ and the resonant amplification from $H$, $v_S$ and
      density. (§4)
- [ ] I can compute the amplitude of a body wave and a surface wave at a given
      distance, and say which loss term dominates. (§3)
- [ ] I can state the steady-state amplification of an oscillator and explain
      why a pulse does not reach it. (§5, §6)
- [ ] I can convert a return period into a probability over an exposure time.
      (§6)
- [ ] I can name three things a 1-D vertical-incidence site-response
      calculation cannot represent. (§9)
