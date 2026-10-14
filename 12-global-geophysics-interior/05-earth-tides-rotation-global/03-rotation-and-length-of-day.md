---
id: 12-05-03
title: "Rotation Variations, LOD and Core-Mantle Coupling"
level: research
prereqs: ["07-06-03", "12-04-03", "12-05-02"]
tags: [global-geophysics, earth-interior, rotation, length-of-day, core-mantle-coupling, angular-momentum]
---

# Rotation Variations, LOD and Core-Mantle Coupling

**All models and data in this module are SYNTHETIC.** The moments of inertia, the
conductivity, the CMB topography and the wind series below are adopted inputs; no
measured length-of-day value, coupling torque or lower-mantle conductivity is
quoted. Every number is printed by
[`code/rotation_and_length_of_day_demo.py`](./code/rotation_and_length_of_day_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the axial angular momentum budget and **convert** a length-of-day
   change into an angular momentum change in kg m² s⁻¹.
2. **Separate** a synthetic LOD signal into an atmospheric part and a residual,
   and **compute** the torque the residual requires.
3. **Derive** and **apply** the scaling estimate for electromagnetic coupling,
   and **invert** it for the lower-mantle conductivity a decadal timescale
   requires.
4. **Derive** the topographic coupling torque, **verify** it by direct
   quadrature, and **compare** its capacity with the required torque.
5. **Compute** the differential rotation of the core and of the inner core that a
   given angular momentum exchange implies.
6. **Demonstrate** with a two-layer integration that the exchange conserves total
   angular momentum, so an LOD change is evidence of an internal torque.
7. **State** which of the coupling mechanisms the observations can and cannot
   discriminate.

## Prerequisites

- [07-06-03 Earth Rotation, Polar Motion, LOD and Excitation](../../07-gravity-geodesy/06-earth-tides-and-rotation/03-earth-rotation.md) —
  the angular momentum budget, the axial angular momentum of a wind field, the
  free wobble and the excitation function. This lesson uses those results and
  concentrates on the **core-mantle coupling** they leave open.
- [12-04-03 Palaeomagnetic Record and Reversal Frequency](../04-geomagnetism-and-core/03-palaeomagnetic-record.md) —
  the magnetic field's history, which sets the field strength available for
  electromagnetic coupling.
- [02 Tidal Response and the Quality Factor of the Whole Earth](02-tidal-response.md) —
  the tidal torque that competes with core-mantle exchange.

## 1. The budget, and why it is a partition

The axial angular momentum of the Earth is the sum of its parts. Write
$H_3 = C\Omega$ for the solid body and $h$ for the part carried by motions
relative to the solid body (winds, currents, core flow). Then conservation gives

$$\Delta\Omega = -\frac{\Delta h}{C}, \qquad\text{or, in
fractional form,}\qquad \frac{\Delta\,\mathrm{LOD}}{\mathrm{LOD}}
= \frac{\Delta h}{C\Omega} .$$

With adopted $C = 8.04\times10^{37}\ \mathrm{kg\,m^{2}}$,
$\Omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$ and
$\mathrm{LOD} = 86400$ s, the budget is

$$C\Omega = 5.8629\times10^{33}\ \mathrm{kg\,m^{2}\,s^{-1}},$$

| $\Delta$LOD (ms) | $\Delta L/H_3$ | $\Delta L$ (kg m² s⁻¹) |
|---|---|---|
| 0.1 | $1.16\times10^{-9}$ | $6.79\times10^{24}$ |
| 0.5 | $5.79\times10^{-9}$ | $3.39\times10^{25}$ |
| 1.0 | $1.16\times10^{-8}$ | $6.79\times10^{25}$ |
| 5.0 | $5.79\times10^{-8}$ | $3.39\times10^{26}$ |

The fractional change in the day length *is* the fractional change in axial
angular momentum — the two differ only by the factors that cancel. A millisecond
is $1.2\times10^{-8}$ of the day and therefore costs
$6.8\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}}$, which is a physical quantity that
some part of the Earth must actually deliver.

## 2. A synthetic wind series and the residual

The demonstration adopts a zonal-wind angular momentum series with an annual term
of amplitude $0.60\times10^{25}$, a decadal term of amplitude
$1.10\times10^{25}$ and a linear drift, in kg m² s⁻¹. Its full range is
$3.431\times10^{25}$, corresponding to

$$\Delta\,\mathrm{LOD}_{\text{range}} = 0.506\ \mathrm{ms},
\qquad \text{rms} = 0.132\ \mathrm{ms}.$$

It then adds a synthetic core contribution of amplitude $0.35\times10^{25}$ with
a 7-yr period. The three resulting numbers are the whole point of the exercise:

| quantity | value |
|---|---|
| total synthetic LOD range | 0.582 ms |
| residual after removing the winds | 0.103 ms |
| core angular momentum implied by the residual | $0.350\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}}$ |

To deliver that change in 7 years requires a mean torque of

$$\tau = \frac{\Delta L}{\Delta t} = 3.169\times10^{16}\ \mathrm{N\,m}.$$

**This is the number every coupling mechanism must be compared against**, and the
rest of the lesson is that comparison.

## 3. Electromagnetic coupling

The physical picture: a poloidal magnetic field threads a layer of the lowermost
mantle of thickness $d$ and conductivity $\sigma$; differential rotation shears
it into a toroidal field; the shear field diffuses back across the layer and
communicates the torque. The time for that diffusion over a horizontal scale $D$
is, dimensionally,

$$\tau_{\text{EM}} \sim \mu_0\sigma\,d\,D .$$

With $D$ taken as the circumference of the CMB, $2\pi R_{\text{cmb}}
= 2.187\times10^{7}$ m, inverting for the conductivity required by a given
timescale gives

| $d$ (km) | $\sigma$ for $\tau = 1$ yr (S/m) | for $\tau = 10$ yr | for $\tau = 30$ yr |
|---|---|---|---|
| 50 | $2.30\times10^{2}$ | $2.30\times10^{3}$ | $6.89\times10^{3}$ |
| 100 | $1.15\times10^{2}$ | $1.15\times10^{3}$ | $3.45\times10^{3}$ |
| 200 | $5.74\times10^{1}$ | $5.74\times10^{2}$ | $1.72\times10^{3}$ |

The statement that matters is the *order of magnitude*: a decadal timescale with a
100-km layer requires

$$\sigma \approx 1.15\times10^{3}\ \mathrm{S\,m^{-1}}$$

— a semiconductor, three orders of magnitude less conductive than the core. The
inference is therefore a bound on the *lowermost mantle*, not a measurement of the
core, and it is one of the few observational handles on that region.

Two cautions. The estimate is dimensional: the order-unity coefficient depends on
the field geometry and on the radial profile of $\sigma$, and different published
treatments differ by a factor of a few. And the mechanism only works if the field
at the CMB is strong enough; the palaeomagnetic record of
[12-04-03](../04-geomagnetism-and-core/03-palaeomagnetic-record.md) is what makes
that a statement about various epochs rather than about today.

## 4. Topographic coupling

If the CMB is not a perfect equipotential, the fluid core feels the bumps,
generates pressure perturbations against them, and exchanges angular momentum. The
axial torque is

$$\tau = \oint p\,\frac{\partial h}{\partial\phi}\,R^{2}\sin^{2}\theta\,
\mathrm{d}\theta\,\mathrm{d}\phi,$$

where $h(\theta,\phi)$ is the topographic departure from the equipotential and $p$
is the pressure on it. Taking $h = h_0\cos m\phi$ and a pressure in quadrature,
$p = \Delta\rho\,g\,h_0\sin m\phi$, gives

$$\boxed{\;\tau_{\max} = \frac{\pi^{2}}{2}\,\Delta\rho\,g\,h_0^{2}m\,R^{2}\;}$$

With adopted $\Delta\rho = 4400\ \mathrm{kg\,m^{-3}}$ and
$g_{\text{cmb}} = 10.7\ \mathrm{m\,s^{-2}}$:

| $h_0$ (km) | $\tau_{\max}$ (N m) | ratio to the required $3.17\times10^{16}$ N m |
|---|---|---|
| 0.1 | $5.63\times10^{22}$ | $1.8\times10^{6}$ |
| 0.5 | $1.41\times10^{24}$ | $4.4\times10^{7}$ |
| 1.0 | $5.63\times10^{24}$ | $1.8\times10^{8}$ |
| 2.0 | $2.25\times10^{25}$ | $7.1\times10^{8}$ |

**Verification.** The demonstration evaluates the same torque by direct
two-dimensional quadrature over the sphere:

$$\tau_{\text{numerical}} = -1.4068\times10^{24}\ \mathrm{N\,m}
\qquad\text{against}\qquad
\tau_{\text{analytic}} = +1.4068\times10^{24}\ \mathrm{N\,m},$$

a difference of **0.001%** with the sign set by the assumed phase lag. The formula
is therefore not an assertion; it is a computed identity.

The comparison is then almost embarrassing: a 0.5-km topography has a torque
capacity $4.4\times10^{7}$ times the requirement. Topographic coupling is not
marginal, it is overwhelming — **provided** the long-wavelength topography exists,
is not dynamically compensated by a density anomaly that cancels its effect, and
is not so rough that the flow is locked. Those three provisos are the entire
research problem, and they are why the mechanism is not simply accepted as the
explanation of decadal LOD changes.

## 5. The inner core

The required angular momentum is $3.50\times10^{24}\ \mathrm{kg\,m^{2}\,s^{-1}}$.
Dividing by a moment of inertia gives the rotation change needed to supply it:

| body | $C$ (kg m²) | $\Delta\Omega$ (rad s⁻¹) | $\Delta\Omega/\Omega$ | $\Delta\Omega$ (° yr⁻¹) |
|---|---|---|---|---|
| whole core | $9.44\times10^{36}$ | $3.71\times10^{-13}$ | $5.08\times10^{-9}$ | $6.70\times10^{-4}$ |
| inner core | $5.85\times10^{34}$ | $5.98\times10^{-11}$ | $8.20\times10^{-7}$ | $1.08\times10^{-1}$ |

The same angular momentum is a 160-fold larger rotation change for the inner core
than for the whole core, because the inner core's moment of inertia is 160 times
smaller. That asymmetry is why the inner core is the most sensitive detector of
core-mantle angular momentum exchange, and why claims about its differential
rotation are claims about very small angles: the last column shows that the
inner-core case needs a tenth of a degree per year, which is measurable only with
decades of repeated observations.

## 6. Why an LOD change is evidence of an internal torque

The demonstration integrates a two-layer model: a mantle and a core with a linear
coupling torque $\tau = k(\Omega_c - \Omega_m)$, an initial shear of
$1.0\times10^{-10}\ \mathrm{rad\,s^{-1}}$, and $k = 10^{29}$ N m per rad s⁻¹. The
coupling time constant is $1/[k(1/C_m + 1/C_c)] = 2.64$ yr, and

| $t$ (yr) | shear (rad s⁻¹) | $\Delta\Omega_m$ (rad s⁻¹) | $\Delta$LOD (ms) |
|---|---|---|---|
| 0 | $1.00\times10^{-10}$ | 0 | 0 |
| 10 | $2.26\times10^{-12}$ | $1.148\times10^{-11}$ | −13.60 |
| 20 | $5.13\times10^{-14}$ | $1.174\times10^{-11}$ | −13.90 |
| 40 | $2.63\times10^{-17}$ | $1.174\times10^{-11}$ | −13.91 |

The total angular momentum before and after is $5.862861404000\times10^{33}$
kg m² s⁻¹ in both cases, with a conservation residual of $0.000\times10^{0}$.

The physics of the table: a faster-spinning core drags the mantle along, the LOD
shortens (negative $\Delta$LOD), and the process stops when the shear has decayed.
Nothing has been created or destroyed — angular momentum has moved from the core
to the mantle. **An observed LOD change therefore tells you that an internal
torque exists; it cannot, by itself, tell you which mechanism supplied it.**

## 7. Assumptions and regime of validity

1. **Axial symmetry.** Only the $z$-component of angular momentum is budgeted;
   polar motion (the wobble) mixes the equatorial components and is treated in
   [07-06-03](../../07-gravity-geodesy/06-earth-tides-and-rotation/03-earth-rotation.md).
2. **A rigid mantle.** Real mantle deformation changes $C$ by a small amount; the
   correction is second order for millisecond LOD changes but not for
   microsecond ones.
3. **The coupling estimate is dimensional.** $\tau_{\text{EM}} \sim \mu_0\sigma dD$
   has an order-unity coefficient that depends on geometry and on the profile of
   $\sigma(d)$.
4. **The topographic torque formula assumes a full quadrature pressure.** Real
   flows produce a partially compensated pressure, which reduces the torque —
   potentially by orders of magnitude.
5. **The wind series is synthetic.** No atmospheric reanalysis or angular
   momentum budget is used, and the annual and decadal amplitudes are chosen to be
   representative, not measured.
6. **A single linear coupling constant.** Real coupling is neither linear nor
   frequency-independent, and the two-layer model cannot represent radial or
   lateral structure in the core.

## 8. Mastery checkpoint

Without notes:

> A synthetic Earth has $C = 8.0\times10^{37}\ \mathrm{kg\,m^{2}}$,
> $\Omega = 7.29\times10^{-5}\ \mathrm{rad\,s^{-1}}$ and
> $\mathrm{LOD} = 86400$ s. **(a)** Compute the angular momentum change
> corresponding to a 2-ms LOD change. **(b)** A wind field delivers
> $1.5\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}}$ of that; compute the residual in
> ms. **(c)** Compute the torque needed to deliver the residual in 5 years.
> **(d)** Compute the electromagnetic coupling time for $\sigma = 10^{3}$ S/m,
> $d = 100$ km and $D = 2\pi R_{\text{cmb}}$. **(e)** Compute the topographic
> torque capacity of a 0.5-km, $m = 2$ CMB topography and state whether the
> observed residual could, in principle, be explained by it.

## 9. Common pitfalls

1. **Treating an LOD change as an energy statement.** It is an angular momentum
   statement, and angular momentum is conserved in any internal exchange.
2. **Quoting an electromagnetic coupling time without $d$ and $D$.** Both appear
   linearly in the estimate.
3. **Assuming a topographic torque is available because the formula is large.**
   Compensation and locking can remove orders of magnitude.
4. **Comparing a required torque with a capacity and declaring the mechanism
   established.** The capacity calculation is an upper bound at best.
5. **Forgetting the inner core's small moment of inertia.** It amplifies any
   differential-rotation signal by an order of magnitude, which is either an
   opportunity or a source of large errors.
6. **Using a two-layer model for microsecond LOD work.** Deformation, oceans and
   the atmosphere all enter at that level.

## 10. Related modules

- [02 Tidal Response and the Quality Factor of the Whole Earth](02-tidal-response.md) —
  the tidal torque that competes with core-mantle coupling.
- [01 Free Oscillations of the Earth](01-free-oscillations.md) — the other global
  mode family, and the source of the $C$-dependent splitting observations.
- [12-04 Geomagnetic Field and Core Dynamics](../04-geomagnetism-and-core/README.md) —
  the field strength and its history, which set the electromagnetic coupling.
- [07-06 Earth Tides and Rotation](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md) —
  the rotation budget, the wobble and the excitation functions.
- [12-06 Geodetic Constraints on the Interior](../06-geodesy-constraints-interior/README.md) —
  the moment-of-inertia constraints used throughout this module.
- [12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md) —
  the thermal evolution that sets the core's buoyancy and its coupling.
