---
id: 10-03-01
title: "GPR for Soil Moisture, Water Table and Aquifer Structure"
level: doctoral
prereqs: ["10-01-01", "10-01-02", "10-01-03", "09-01-01"]
tags: [gpr, near-surface, geotechnical, hydrogeology, soil-moisture, permittivity, water-table]
---

# GPR for Soil Moisture, Water Table and Aquifer Structure

**All models and data in this module are SYNTHETIC.** No number below is a site
measurement. The physical constants that are not chosen are labelled as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the low-loss phase speed $v = c/\sqrt{\varepsilon_r}$ from the
   Maxwell equations for a non-magnetic dielectric, and **state** the loss
   tangent that bounds its validity.
2. **Derive** the complex refractive index mixing model (CRIM) as a volumetric
   average of refractive indices, and **compute** the permittivity, speed and
   wavelength of a soil from its porosity and water content.
3. **Invert** the mixing model for water content, and **quantify** the error that
   the unknown porosity injects into that inversion.
4. **Compute** the reflection coefficient of a wetting front or water table, and
   **explain** why a graded contact of one wavelength costs most of the echo
   amplitude while a sharp weak contact of the same amplitude sits elsewhere in
   time.
5. **Convert** a two-way time to a depth with a layered velocity model, and
   **quantify** the error made by converting with a single shallow velocity.
6. **Compute** the attenuation of a soil from its conductivity and permittivity,
   and **decide** from the loss tangent when the low-loss formula may be used.
7. **Propagate** an uncertainty budget from a picked time and a velocity into a
   water-table depth, and **name** the dominant term.

## Prerequisites

- [10-01-01 GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](../01-gpr-principles/01-gpr-physics.md)
  — the wave speed, the reflection coefficient and the loss tangent.
- [10-01-02 Velocity Estimation and Depth Conversion](../01-gpr-principles/02-gpr-velocity-and-depth.md)
  — why a two-way time is not a depth without a velocity.
- [10-01-03 Attenuation, Penetration Depth and Frequency Trade-Offs](../01-gpr-principles/03-gpr-attenuation-penetration.md)
  — the absorption constant and the depth of investigation.
- [09-01-01 Resistivity, Conductivity and the Electrical Properties of Rocks](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — where the conductivity in the loss tangent comes from.
- [14-01-06 The Unsaturated Zone](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/06-unsaturated-zone.md)
  — porosity, saturation and the moisture profile that GPR is trying to see.

## 1. Intuition: a radar measures the refractive index of a mixture

A soil is not a material. It is a three-phase mixture: mineral grains, water, and
air. GPR does not measure water content, or porosity, or density. It measures one
electromagnetic property of the mixture — the **relative permittivity** — and every
hydrological quantity is then inferred from it with a mixing model.

That single sentence controls this whole lesson. The permittivity of a soil
ranges from about $3$ when dry to above $20$ when saturated, so the GPR speed
ranges over a factor of more than two (the demonstration measures $2.54$ for its
teaching soil). A profile in which the moisture changes with depth is therefore a
profile in which the *conversion factor from time to depth changes with depth*
— and that is the difference between a radar section and a depth section.

Two consequences are worth stating before any algebra:

- **Water content is the loudest signal GPR sees in the shallow subsurface.** A
  change from dry soil to saturated soil changes the permittivity by a factor of
  three or more, which is a reflection coefficient of about $-0.3$, i.e. a
  $-10\ \mathrm{dB}$ echo. That is why the water table is one of the classic GPR
  targets.
- **The same change destroys the method if it is spread out or if the water is
  salty.** A transition spread over a metre cancels most of the echo, and a
  conductivity of $0.05\ \mathrm{S\,m^{-1}}$ costs $16\ \mathrm{dB\,m^{-1}}$,
  which spends a $60\ \mathrm{dB}$ budget in under two metres.

## 2. Precise definitions

### 2.1 Moisture variables

| Symbol | Name | Definition | Typical teaching range |
|---|---|---|---|
| $\phi$ | porosity | void volume / total volume | $0.25$–$0.50$ |
| $\theta$ | volumetric water content | water volume / total volume | $0$–$\phi$ |
| $S$ | saturation | $\theta/\phi$ | $0$–$1$ |
| $\varepsilon_r$ | relative permittivity | $\varepsilon/\varepsilon_0$, dimensionless | $3$–$25$ in soils |

The three moisture variables are one degree of freedom short of three: $\theta$,
$\phi$ and $S$ satisfy $\theta = S\phi$, so any two determine the third. A GPR
measurement supplies one number, the permittivity. That is the counting argument
behind the non-uniqueness demonstrated in Section 5.

### 2.2 The loss tangent

For a non-magnetic medium with permittivity $\varepsilon$ and conductivity
$\sigma$, the loss tangent is

$$\tan\delta = \frac{\sigma}{\omega\varepsilon} = \frac{\sigma}{2\pi f \varepsilon_0 \varepsilon_r}.$$

It is the ratio of the conduction current to the displacement current, and it is
the single number that decides which regime a GPR survey is in:

- $\tan\delta \ll 1$ — **low-loss**: the speed is $c/\sqrt{\varepsilon_r}$ and the
  reflections are computed from real permittivities alone.
- $\tan\delta \gtrsim 1$ — **lossy**: the speed departs from the low-loss value,
  the attenuation is no longer linear in $\sigma$, and the reflections acquire a
  phase shift.

The demonstration measures $\tan\delta = 0.018$ for dry sand at $250\ \mathrm{MHz}$
and $\tan\delta = 1.438$ for a saline wet soil at $100\ \mathrm{MHz}$: the same
formula cannot be used across that range.

### 2.3 The reflection coefficient

At normal incidence from medium 1 to medium 2 the amplitude reflection
coefficient is

$$R = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}, \qquad \eta = \frac{Z_0}{\sqrt{\varepsilon_r}},$$

with $Z_0$ the impedance of free space. Substituting $\eta$ gives the form used
throughout this module,

$$R = \frac{\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2}}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}}.$$

$R$ is dimensionless. Its magnitude is the amplitude ratio of the reflected to the
incident wave; its sign says whether the reflection is phase-reversed relative to
the incident pulse.

### 2.4 The mixing model

The complex refractive index model (CRIM) is the standard volumetric mixing model
of petrophysics: the refractive index of the mixture is the volume-weighted mean
of the refractive indices of its constituents,

$$\sqrt{\varepsilon} = (1-\phi)\sqrt{\varepsilon_g} + \theta\sqrt{\varepsilon_w} + (\phi-\theta)\sqrt{\varepsilon_a}.$$

Here $\varepsilon_g$, $\varepsilon_w$ and $\varepsilon_a$ are the permittivities
of the grain, water and air, and the three volume fractions are $1-\phi$,
$\theta$ and $\phi-\theta$. It is a *model*, and the next section is explicit
about what it assumes.

## 3. Derivations

### 3.1 The low-loss speed

In a source-free, non-magnetic, insulating medium the Maxwell equations give the
wave equation

$$\nabla^{2}\mathbf{E} - \mu_0\varepsilon\frac{\partial^{2}\mathbf{E}}{\partial t^{2}} = 0,$$

whose plane-wave solutions travel at

$$v = \frac{1}{\sqrt{\mu_0\varepsilon}} = \frac{1}{\sqrt{\mu_0\varepsilon_0}}\cdot\frac{1}{\sqrt{\varepsilon_r}} = \frac{c}{\sqrt{\varepsilon_r}}.$$

*Numerical check (SYNTHETIC).* With $\varepsilon_r = 9.0$:

$$v = \frac{0.299792458\ \mathrm{m\,ns^{-1}}}{\sqrt{9.0}} = \frac{0.299792458}{3.0} = 0.0999308\ \mathrm{m\,ns^{-1}}.$$

The demonstration prints $0.0999\ \mathrm{m\,ns^{-1}}$. The unit $\mathrm{m\,ns^{-1}}$
is the unit GPR practice works in; it equals $10^{9}\ \mathrm{m\,s^{-1}}$.

### 3.2 CRIM from phase delays

Take a slab of mixture of thickness $L$ filled with grains, water and air, and
imagine the wave crossing it. If each constituent were a separate layer of
thickness $f_i L$ with refractive index $n_i$, the total travel time would be

$$t = \sum_i \frac{f_i L}{c/n_i} = \frac{L}{c}\sum_i f_i n_i.$$

The mixture is not a stack of layers, but if the inclusions are small compared
with the wavelength the wave samples them in parallel and the *effective*
refractive index of the mixture is the volume average $\sum_i f_i n_i$. With
$n = \sqrt{\varepsilon_r}$ and the fractions $(1-\phi)$, $\theta$, $\phi-\theta$
this is CRIM. The assumption is stated in Section 6: it fails when the water is
not evenly distributed at the scale of the wavelength.

### 3.3 Inverting for moisture, and the porosity problem

Let $n_w = \sqrt{\varepsilon_w}$, $n_a = \sqrt{\varepsilon_a}$,
$n_g = \sqrt{\varepsilon_g}$, and let $\sqrt{\varepsilon}$ be measured. Solving
CRIM for $\theta$:

$$\theta = \frac{\sqrt{\varepsilon} - (1-\phi)n_g - \phi n_a}{n_w - n_a}.$$

The porosity appears linearly, so

$$\frac{\partial\theta}{\partial\phi} = \frac{n_g - n_a}{n_w - n_a}.$$

With the demonstration's SYNTHETIC values $n_g = \sqrt{5.0} = 2.2361$,
$n_a = 1$, $n_w = \sqrt{80.1} = 8.9508$:

$$\frac{\partial\theta}{\partial\phi} = \frac{1.2361}{7.9508} = 0.15547.$$

**A porosity error of $0.05$ is a water-content error of $0.0078$** — small
against a saturated content of $0.35$, but not against the differences a
hydrological study usually wants. The demonstration confirms this exactly: at a
measured $\varepsilon_r = 9.00$, $\phi = 0.30$ gives $\theta = 0.1427$ and
$\phi = 0.40$ gives $\theta = 0.1583$, a difference of $0.0155$ per $0.10$ of
porosity, i.e. $0.0078$ per $0.05$.

The same inversion with an *empirical* calibration (a Topp-type polynomial) gives
$\theta = 0.1684$ at the same measured permittivity, against $0.1505$ from CRIM.
The $+1.79$ percentage points between them is **model error, not measurement
error** — two defensible petrophysical models disagree by more than the porosity
term changes. This module shows that number so the reader never has to guess it.

### 3.4 The water-table reflection and the graded contact

The water table is not a material boundary; it is a moisture boundary. Its
reflection coefficient follows from the permittivities on either side. With
$\varepsilon_1 = 5.95$ (dry, $\theta = 0.08$) and $\varepsilon_2 = 21.03$
(saturated, $\theta = 0.35$):

$$R = \frac{\sqrt{5.95} - \sqrt{21.03}}{\sqrt{5.95} + \sqrt{21.03}} = \frac{2.4393 - 4.5859}{2.4393 + 4.5859} = -0.3055,$$

which is $-10.3\ \mathrm{dB}$ in power. The sign is negative: the wave crosses
from a faster medium into a slower one and the reflection reverses phase relative
to the incident pulse.

Now suppose the moisture change is spread over a thickness $h$ rather than being
sharp — a capillary fringe. Write the contact as $N$ thin slabs with interface
coefficients $r_i$, and add the reflections with their two-way delays (the
single-scattering, or Born, sum):

$$R(f) = \sum_i r_i\,e^{-i 2\pi f \tau_i}.$$

For a linear ramp this sum has a closed form in the weak-contrast limit: with
$\tau$ the two-way time across the ramp,

$$R(f) \simeq R_0\,\mathrm{sinc}(f\tau)\,e^{-i\pi f\tau},$$

where $\mathrm{sinc}(x) = \sin(\pi x)/(\pi x)$. The mechanism is phase
cancellation: contributions from the top of the ramp and the bottom arrive half a
cycle apart and subtract.

*Numerical check.* The demonstration sums the Born series over $400$ slabs and
compares with the sinc form on a weak ramp ($\varepsilon$ from $5.95$ to $6.55$
over $0.15\ \mathrm{m}$ at $250\ \mathrm{MHz}$): summed $0.011298$ against
analytic $0.011285$, a relative deviation of $0.12\%$. The formula is right; the
regime is what matters. On the strong water-table contrast the same two numbers
disagree by tens of per cent, because the denominator $\sqrt{\varepsilon}$ is not
linear across the ramp.

The measured effect on the echo is large:

| fringe (m) | two-way time across it (ns) | $f\tau$ | amplitude / sharp amplitude |
|---|---|---|---|
| $0.05$ | $1.23$ | $0.306$ | $0.894$ |
| $0.10$ | $2.45$ | $0.613$ | $0.567$ |
| $0.15$ | $3.68$ | $0.919$ | $0.308$ |
| $0.30$ | $7.35$ | $1.838$ | $0.207$ |

**A fringe of $0.15\ \mathrm{m}$ costs $70\%$ of the amplitude.** A weak echo at
$1.5\ \mathrm{m}$ is therefore not evidence that the moisture change is small: it
may be evidence that the change is gradual. Contrast and transition thickness are
traded against each other, and one amplitude cannot separate them.

### 3.5 From two-way time to depth

In a layered medium the two-way time is the sum of the layer times,

$$t = 2\sum_i \frac{\Delta z_i}{v_i}, \qquad v_i = \frac{c}{\sqrt{\varepsilon_i}},$$

and the depth is $z = \sum_i \Delta z_i$. There is no single velocity in that
expression. If a shallow measurement (a common-midpoint fit, a diffraction
hyperbola, or a known target) supplies $v_1$, and it is applied to the whole
section, the reported depth is

$$z_{\text{rep}} = \frac{v_1 t}{2} = v_1\sum_i\frac{\Delta z_i}{v_i}
= \sum_i \Delta z_i \frac{v_1}{v_i}.$$

Every layer is scaled by $v_1/v_i$, which is greater than one for every layer
slower than the shallow one. Since moisture increases with depth in a soil
profile and speed falls with moisture, **the reported depth is systematically too
large**, and the error grows with depth. The demonstration's synthetic profile
(Table in Section 5) reports $6.78\ \mathrm{m}$ for a $4.00\ \mathrm{m}$ depth:
$+69.6\%$.

## 4. Physical interpretation: what the measurement constrains

- A GPR trace constrains a **two-way time** and an **amplitude ratio**. Both are
  converted into geology through models: the velocity model and the petrophysical
  model. Neither conversion is optional and neither is self-evident from the data.
- The permittivity of a soil is dominated by its water because water's
  permittivity ($80.1$ at $20\ ^\circ\mathrm{C}$) is an order of magnitude larger
  than any mineral's. That is why GPR is a moisture sensor, and it is also why a
  small change in $\theta$ produces a large change in $\varepsilon$ only at low
  saturation: from the demonstration's table, $\theta$ from $0.00$ to $0.05$ moves
  $\varepsilon$ from $3.25$ to $4.84$ ($+49\%$), while $0.30$ to $0.35$ moves it
  from $17.54$ to $21.03$ ($+20\%$).
- Conductivity is set by the pore fluid, not by the water content alone: a small
  amount of salt in the pore water raises $\sigma$ by orders of magnitude and
  removes the echo entirely. **GPR maps moisture only where the pore water is
  fresh.**
- The water table is often the *capillary fringe boundary* rather than the
  saturated surface, and the two are separated by more than a GPR resolution
  length in coarse material. The reflector is then an interpretation, not a
  measurement.

## 5. Worked examples

### Example 1 — permittivity, speed and wavelength of one soil

SYNTHETIC soil: $\phi = 0.35$, $\varepsilon_g = 5.0$, $\theta = 0.15$.

1. $\sqrt{\varepsilon} = 0.65(2.2361) + 0.15(8.9508) + 0.20(1) = 1.4535 + 1.3426 + 0.2000 = 2.9961$.
2. $\varepsilon = 8.98$ (the demonstration prints $8.98$).
3. $v = 0.299792458/\sqrt{8.98} = 0.1001\ \mathrm{m\,ns^{-1}}$.
4. At $f = 250\ \mathrm{MHz}$, $\lambda = v/f = 0.1001/0.250 = 0.400\ \mathrm{m}$,
   and the quarter-wavelength resolution limit is $0.100\ \mathrm{m}$.

Note that $S = \theta/\phi = 0.429$: less than half saturated, and the speed has
already fallen from $0.1662$ to $0.1001\ \mathrm{m\,ns^{-1}}$, a factor of $1.66$.

### Example 2 — the depth error of a single velocity

The demonstration's SYNTHETIC three-layer profile, at $250\ \mathrm{MHz}$:

| layer | depth interval (m) | $\theta$ | $\varepsilon_r$ | $v$ (m/ns) | 1-way time (ns) | cumulative TWT (ns) |
|---|---|---|---|---|---|---|
| dry topsoil | $0.00$–$0.50$ | $0.08$ | $5.95$ | $0.1229$ | $4.07$ | $8.14$ |
| transition | $0.50$–$1.20$ | $0.22$ | $12.62$ | $0.0844$ | $8.29$ | $24.73$ |
| saturated zone | $1.20$–$4.00$ | $0.35$ | $21.03$ | $0.0654$ | $42.83$ | $110.39$ |

1. The two-way time to the $4.00\ \mathrm{m}$ base is $110.39\ \mathrm{ns}$.
2. Converted with the dry topsoil velocity: $z = 0.1229 \times 110.39/2
   = 6.78\ \mathrm{m}$, i.e. $+69.6\%$ against $4.00\ \mathrm{m}$.
3. The water table at $24.73\ \mathrm{ns}$ converts to $1.52\ \mathrm{m}$ against
   a true $1.20\ \mathrm{m}$: $+26.6\%$.
4. The velocity that would return the correct total depth is
   $v = 2(4.00)/110.39 = 0.0725\ \mathrm{m\,ns^{-1}}$ — a *travel-time weighted*
   average that no surface measurement returns, because it is defined by the very
   profile we are trying to find. Quoting it as "the velocity" is circular.

The honest deliverable is a velocity model with a stated uncertainty, or a depth
stated conditionally on one.

### Example 3 — attenuation and the depth of investigation

The demonstration computes the exact attenuation constant of a lossy dielectric,

$$\alpha = \omega\sqrt{\mu\varepsilon'}\sqrt{\frac{\sqrt{1+\tan^{2}\delta}-1}{2}},
\qquad \tan\delta = \frac{\sigma}{\omega\varepsilon'},$$

and compares it with the low-loss form $\alpha \simeq \sigma Z_0/(2\sqrt{\varepsilon_r})$.

| medium | $\varepsilon_r$ | $\sigma$ (S/m) | $f$ (MHz) | $\tan\delta$ | $\alpha$ exact (Np/m) | dB/m | 60 dB two-way depth (m) |
|---|---|---|---|---|---|---|---|
| dry sand | $4.0$ | $10^{-3}$ | $250$ | $0.018$ | $0.0942$ | $0.82$ | $36.7$ |
| moist soil | $9.0$ | $10^{-2}$ | $250$ | $0.080$ | $0.6274$ | $5.45$ | $5.5$ |
| clay-rich soil | $25.0$ | $5\times10^{-2}$ | $250$ | $0.144$ | $1.8788$ | $16.3$ | $1.8$ |
| saline wet soil | $25.0$ | $2\times10^{-1}$ | $100$ | $1.438$ | $6.4237$ | $55.8$ | $0.5$ |

Two lessons are in that table. First, **the low-loss approximation is excellent
until it is not**: at $\tan\delta = 0.36$ the exact and approximate values differ
by $1.5\%$, while at $\tan\delta = 1.44$ they differ by $17\%$. Second, a
conductivity of $0.2\ \mathrm{S\,m^{-1}}$ — a modest amount of salt — puts the
water table below the depth of investigation. The method does not fail because
the physics changed; it fails because the echo is absorbed.

## 6. Assumptions and regime of validity

1. **Low loss, non-magnetic.** $v = c/\sqrt{\varepsilon_r}$ and the reflection
   coefficients above require $\tan\delta \ll 1$ and $\mu_r = 1$. The loss tangent
   is printed for every medium in the demonstration precisely so that this can be
   checked rather than assumed.
2. **CRIM.** A volumetric average of refractive indices assumes the constituents
   are mixed at a scale small compared with the wavelength and that the mixture
   is statistically isotropic. Clay, with its bound water and plate-like grains,
   violates it and is the main reason empirical calibrations differ from CRIM.
3. **A local measurement.** A GPR velocity is an average over the first Fresnel
   zone, not a point value. A profile reported with metre-scale layers is being
   reported at the resolution of the footprint.
4. **Fixed porosity for the inversion.** $\theta$ from a measured
   $\varepsilon_r$ requires $\phi$, which GPR does not measure. Every moisture
   number in this module is conditional on a porosity, and the sensitivity is
   $\partial\theta/\partial\phi = 0.155$.
5. **Sharp or known-way contacts for amplitudes.** An amplitude converts to a
   contrast only if the transition thickness is known to be small compared with
   the wavelength; otherwise Section 3.4 applies.
6. **Additive, independent noise and a known source wavelet.** Required for the
   amplitude work; the depth work needs only the time.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| relative permittivity | $\varepsilon_r$ | dimensionless | $\varepsilon/\varepsilon_0$ |
| conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | $\mathrm{A\,V^{-1}m^{-1}}$ |
| loss tangent | $\tan\delta$ | dimensionless | $\sigma/(\omega\varepsilon)$ |
| speed | $v$ | $\mathrm{m\,ns^{-1}}$ | $c/\sqrt{\varepsilon_r}$, $c = 0.299792458\ \mathrm{m\,ns^{-1}}$ |
| two-way time | $t$ | ns | $2z/v$ |
| attenuation | $\alpha$ | $\mathrm{Np\,m^{-1}}$ | $\sigma Z_0/(2\sqrt{\varepsilon_r})$, $Z_0 = 376.73\ \Omega$ |
| reflection coefficient | $R$ | dimensionless | ratio of two amplitudes |

The only way to get a time from a length in this module is length divided by
speed. If an arithmetic line produces $\mathrm{m^2\,ns^{-1}}$ or
$\mathrm{ns\,m^{-1}}$, a velocity has been multiplied where it should have been
divided.

## 8. Python demonstration

[`code/gpr_hydrogeology_demo.py`](code/gpr_hydrogeology_demo.py) computes every
number quoted above and prints labelled results with units. It:

1. tabulates CRIM permittivity and speed against water content, giving the
   $2.54$ speed ratio between dry and saturated;
2. inverts for moisture at five assumed porosities and compares CRIM with an
   empirical calibration ($+1.79$ percentage points at $\varepsilon_r = 9$);
3. builds the three-layer moisture profile, computes the two-way times, and
   reports the two depth-conversion errors ($+69.6\%$ and $+26.6\%$);
4. sums the Born series across a graded water-table contact, verifies the
   summation against the analytic sinc form on a weak ramp ($0.12\%$), and
   reports the amplitude lost to a fringe;
5. computes the exact and low-loss attenuation constants with the loss tangent
   as a printed regime check;
6. propagates a depth budget by Monte Carlo ($0.0563\ \mathrm{m}$ total, of which
   $0.0475\ \mathrm{m}$ is velocity and $0.0306\ \mathrm{m}$ is picking).

It is print-only, uses the fixed seed `20261014`, and exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-gpr-hydrogeology-exercises.md`](exercises/01-gpr-hydrogeology-exercises.md)
and
[`exercises/01-gpr-hydrogeology-solutions.md`](exercises/01-gpr-hydrogeology-solutions.md).

- **★** Compute $\varepsilon_r$, $v$ and $\lambda$ at $250\ \mathrm{MHz}$ for
  $\phi = 0.40$, $\theta = 0.20$, $\varepsilon_g = 5.0$.
- **★★** A water-table reflection has $R = -0.18$. Assuming $\varepsilon$ below
  the contact is $21.0$, find $\varepsilon$ above it, and state one other
  combination of moisture and fringe thickness that would give the same $R$.
- **★★★** Design an experiment that separates the porosity term from the
  moisture term in a CRIM inversion, stating what is measured, at what
  resolution, and what assumption remains untestable.

## 10. Further reading

- **Topp, G. C., Davis, J. L., & Annan, A. P. (1980). Electromagnetic
  determination of soil water content. *Water Resources Research*, 16(3).**
  Level: research. The empirical moisture calibration used as a reference curve
  in the demonstration.
- **Davis, J. L., & Annan, A. P. (1989). Ground-penetrating radar for
  high-resolution mapping of soil and rock stratigraphy. *Geophysical
  Prospecting*, 37(5).** Level: research. The paper that defined the survey
  practice this lesson quantifies.
- **Neal, A. (2004). Ground-penetrating radar and its use in sedimentology.
  *Earth-Science Reviews*, 66.** Level: research. A critical survey of what
  radar stratigraphy can and cannot claim.
- **Jol, H. M. (ed.). *Ground Penetrating Radar: Theory and Applications.*
  Elsevier.** Level: reference. The standard handbook; the chapters on
  hydrogeology and on antenna behaviour sit directly under this lesson.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A soil has $\phi = 0.35$ and $\varepsilon_g = 5.0$. A GPR survey at
> $250\ \mathrm{MHz}$ measures $\varepsilon_r = 12.0$ in the top $1.40\ \mathrm{m}$
> and $\varepsilon_r = 21.0$ below it, with a two-way time to the deeper contact
> of $40.0\ \mathrm{ns}$. **(a)** Compute $\theta$ in both layers from CRIM and
> the implied saturations. **(b)** Compute $R$ at the contact and state its sign.
> **(c)** Convert the $40.0\ \mathrm{ns}$ to a depth using a two-layer velocity
> model, then again using only the top-layer velocity, and quote the error. **(d)** The same contact is later found to be graded over
> $0.2\ \mathrm{m}$. State the direction of the error this introduces in the
> amplitude-derived contrast and give the approximate sinc factor. **(e)** State
> what single additional measurement would most reduce the depth uncertainty.

Worked versions of (a)–(c) are in the
[solutions](exercises/01-gpr-hydrogeology-solutions.md).

## Common pitfalls

1. **Reporting a moisture content without the porosity.** The inversion
   $\theta(\varepsilon_r)$ is a function of two variables; fixing one by habit is
   an assumption, not a measurement.
2. **Quoting a single velocity for a profile.** The conversion error is
   systematic and grows with depth ($+69.6\%$ in the demonstration profile).
3. **Treating the water table as a step.** A capillary fringe of a quarter
   wavelength removes most of the amplitude; the reflector is then a transition,
   not a boundary.
4. **Using the low-loss formulas at high loss.** At $\tan\delta = 1.44$ the
   low-loss attenuation is $17\%$ too large; the speed is wrong too, and the
   error is silent.
5. **Ignoring salinity.** The moisture that raises $\varepsilon_r$ can also raise
   $\sigma$; the echo may never return.
6. **Confusing model error with measurement error.** CRIM and an empirical
   calibration differ by $1.79$ percentage points of water content at the same
   permittivity.

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the wave physics and
  the resolution limits this lesson uses.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md)
  — survey design, velocity analysis from CMP soundings, and processing.
- [10-05 Other Near-Surface Methods](../05-other-near-surface-methods/README.md)
  — EMI conductivity, which measures the salinity term GPR cannot.
- [10-06 Near-Surface Monitoring and Time-Lapse](../06-nearsurface-monitoring/README.md)
  — repeating a moisture survey to see infiltration move.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)
  — the hydrological quantities this measurement is trying to estimate.

## Code and exercises

| Path | Contents |
|---|---|
| [`code/gpr_hydrogeology_demo.py`](code/gpr_hydrogeology_demo.py) | The six computations of Section 8 |
| [`exercises/01-gpr-hydrogeology-exercises.md`](exercises/01-gpr-hydrogeology-exercises.md) | Graded problems |
| [`exercises/01-gpr-hydrogeology-solutions.md`](exercises/01-gpr-hydrogeology-solutions.md) | Worked solutions |

Run the demonstration with the project virtual environment:

```bash
cd 10-gpr-near-surface/03-gpr-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_hydrogeology_demo.py
```
