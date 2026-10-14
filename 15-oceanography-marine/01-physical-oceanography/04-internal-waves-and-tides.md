---
id: 15-01-04
title: "Internal Waves, Tides and Mixing"
level: doctoral
prereqs: ["15-01-01", "02-03-07", "02-06-04"]
tags: [oceanography, marine-geophysics, internal-waves, tides, mixing, richardson-number, osborn]
---

# Internal Waves, Tides and Mixing

> **All models and data in this module are SYNTHETIC.** The stratification and
> shear profiles below are chosen teaching functions, printed by the
> demonstration in `code/`. No mooring, CTD cast, microstructure profiler,
> altimeter or reanalysis is used.

An ocean that is stratified has a restoring force in its interior: displace a
parcel of water vertically and buoyancy pushes it back. That single fact produces
a spectrum of **internal waves** filling the ocean from the buoyancy frequency
$N$ down to the inertial frequency $f$, and it means that the ocean's interior is
not a still reservoir but a continuously moving medium whose energy is
concentrated in a band of frequencies no surface instrument would see.

Two things make internal waves more than a curiosity. They carry energy from
where the tide and wind generate them to where they break, and they do the
mixing in between. **Mixing is what supplies the potential energy that maintains
the stratification itself**, closing a loop that the box models of
[Lesson 03](03-thermohaline-circulation.md) take as given with a coefficient
$\kappa$. This lesson is about that coefficient.

The honest difficulty: mixing is measured in centimetres and matters at basin
scale, and the conversion from a dissipation measurement to a diffusivity rests
on a closure assumption (the mixing efficiency) that is itself uncertain by a
factor of a few.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the internal-wave dispersion relation
   $\omega^{2} = (N^{2}k^{2} + f^{2}m^{2})/(k^{2}+m^{2})$ from the linearised
   equations, and **state** the two limits $\omega\to N$ and $\omega\to f$ with
   their physical meanings.
2. **Compute** the mode-1 internal tide's phase speed and wavelength at a stated
   latitude, and **quantify** the factor by which rotation lengthens it.
3. **Solve** the vertical-mode problem $( \phi'' + N^{2}\phi/c^{2} = 0 )$ on a
   grid for both constant and structured $N(z)$, **verify** the eigenvector against
   the differential equation, and **state** why the mode speed is an integral of
   stratification.
4. **Compute** the internal-wave characteristic slope
   $s = \sqrt{(\omega^{2}-f^{2})/(N^{2}-\omega^{2})}$ and **classify** a
   topographic slope as subcritical, critical or supercritical against it.
5. **Compute** the Richardson number from co-located shear and stratification
   profiles, and **state** precisely what $\mathrm{Ri}<1/4$ does and does not
   prove.
6. **Apply** the Osborn relation $K_\rho = \Gamma\epsilon/N^{2}$ and **state** the
   assumption it makes and the size of the error that assumption admits.
7. **Distinguish** a measured dissipation from an inferred diffusivity in every
   sentence the two appear together.

## Prerequisites

- [15-01-01 Seawater Properties: Temperature, Salinity, Density](01-seawater-properties.md) —
  the buoyancy frequency $N^{2}$ and its sign convention.
- [02-03-07 Dispersion and Group Velocity](../../02-physics/03-oscillations-and-waves/07-dispersion.md) —
  dispersion relations, phase and group velocity, and why they differ.
- [02-06-04 Turbulence and Eddy Transport](../../02-physics/06-fluid-mechanics/04-turbulence.md) —
  why a turbulent diffusivity is a closure rather than a fluid property.

## 1. The restoring force and the frequency band

Internal waves exist because potential density increases downward. Displace a
parcel upward and, if the displacement is adiabatic and isohaline, it arrives in
an environment heavier than itself and is pushed back. The oscillation frequency
is set by the local stratification through $N$ (Lesson 01):

$$N^{2} = \frac{g}{\rho_0}\frac{\partial\rho_\theta}{\partial z}
\qquad (z \text{ positive downward}).$$

If the ocean were not rotating, internal waves would exist at every frequency
below $N$: they are *not* a narrowband phenomenon. Rotation removes the low
frequencies, because the Coriolis acceleration provides a second restoring force
that dominates as soon as the motion is slow compared with $f$. The result is the
band

$$f < \omega < N .$$

With the demonstration's $N = 0.010\ \mathrm{rad\,s^{-1}}$ (buoyancy period
10.47 min) and $f$ at $45^\circ$N ($1.031\times10^{-4}\ \mathrm{rad\,s^{-1}}$),
that band spans more than two decades in frequency.

## 2. The dispersion relation

### 2.1 Sketch of the derivation

Linearise the Boussinesq equations about a state at rest with
$N = N(z)$ constant and $f$ constant, take two-dimensional motion in the
$(x,z)$ plane, eliminate the pressure, and look for a plane wave
$\propto\exp[\mathrm{i}(kx + mz - \omega t)]$. The result is

$$\boxed{\;\omega^{2} = \frac{N^{2}k^{2} + f^{2}m^{2}}{k^{2} + m^{2}}
= N^{2}\cos^{2}\theta + f^{2}\sin^{2}\theta,\;}$$

where $k$ is the horizontal and $m$ the vertical wavenumber and $\theta$ is the
angle of the wavevector from the **horizontal**. The demonstration's table:

| $k$ (m$^{-1}$) | $m$ (m$^{-1}$) | $\theta$ (deg) | $\omega$ (rad s$^{-1}$) | period (min) |
|---|---|---|---|---|
| $1.0\times10^{-3}$ | $1.0\times10^{-5}$ | 0.57 | $9.9995\times10^{-3}$ | 10.472 |
| $1.0\times10^{-5}$ | $1.0\times10^{-5}$ | 45.00 | $7.0714\times10^{-3}$ | 14.809 |
| $1.0\times10^{-5}$ | $1.0\times10^{-4}$ | 84.29 | $1.0003\times10^{-3}$ | 104.69 |
| $1.0\times10^{-5}$ | $1.0\times10^{-3}$ | 89.43 | $1.4364\times10^{-4}$ | 729.04 |

The two limits are visible in the table: a nearly horizontal wavevector gives
$\omega\to N$, a nearly vertical one gives $\omega\to f$. The last row's period
of 729 min is far longer than the buoyancy period and is set by rotation, not by
stratification.

### 2.2 The consequence that surprises people

Differentiate $\omega^{2} = N^{2}\cos^{2}\theta + f^{2}\sin^{2}\theta$ with
respect to $\theta$: the frequency depends **only on the direction** of the
wavevector, not on its magnitude. Internal waves are therefore strongly
**anisotropic**: for a fixed $\omega$, the permitted wavevectors lie on a cone
whose half-angle is set by $\omega$, and both the phase velocity and the group
velocity have magnitudes that scale with $1/|\mathbf{k}|$ while their directions
are fixed by the frequency. Adding energy at a given $\omega$ cannot change the
direction in which it travels.

A further consequence: the group velocity is **perpendicular** to the
wavevector, so energy travels along the wave crests, not across them. The
demonstration prints, for the mode-1 internal tide in Section 3, a wavevector at
$89.45^\circ$ from the horizontal and an energy-flux direction at $0.55^\circ$
from the horizontal — nearly orthogonal, and the reason tidal beams are observed
as narrow rays across a basin rather than as a diffuse field.

## 3. Rotation and the internal tide

The tide is a large-scale, predictable forcing at the M2 period
$12.4206\ \mathrm{h}$ (a conventional astronomical value) with
$\omega_{M2} = 1.4052\times10^{-4}\ \mathrm{rad\,s^{-1}}$. It generates internal
waves by flowing over topography; the resulting **internal tide** is the
dominant mode-1 signal in most of the deep ocean.

For a flat bottom and a rigid lid at depth $H$ with constant $N$, the mode-1
vertical wavenumber is $m = \pi/H$, and the dispersion relation solved for $k$ is

$$k^{2} = m^{2}\frac{\omega^{2} - f^{2}}{N^{2} - \omega^{2}}.$$

With $N = 0.010\ \mathrm{rad\,s^{-1}}$ and $H = 1000\ \mathrm{m}$:

$$c_{f=0} = \frac{NH}{\pi} = \frac{0.010 \times 1000}{\pi}
= 3.1831\ \mathrm{m\,s^{-1}}, \qquad
k_{f=0} = \frac{\omega}{c} = 4.4145\times10^{-5}\ \mathrm{m^{-1}},
\qquad \lambda = 142.33\ \mathrm{km}.$$

| latitude | $f$ (s$^{-1}$) | $c$ (m s$^{-1}$) | $\lambda$ (km) | $c/c_{f=0}$ |
|---|---|---|---|---|
| $0^\circ$ | 0 | 3.1828 | 142.32 | 0.9999 |
| $15^\circ$N | $3.775\times10^{-5}$ | 3.3042 | 147.75 | 1.0381 |
| $30^\circ$N | $7.292\times10^{-5}$ | 3.7234 | 166.49 | 1.1697 |
| $45^\circ$N | $1.031\times10^{-4}$ | 4.6856 | 209.51 | 1.4720 |
| $60^\circ$N | $1.263\times10^{-4}$ | 7.2618 | 324.71 | 2.2814 |

Solving for the phase speed directly,

$$c = \frac{\omega}{k}
= \frac{\omega H}{\pi}\sqrt{\frac{N^{2}-\omega^{2}}{\omega^{2}-f^{2}}},$$

so the ratio to the non-rotating value at the *same* frequency is

$$\frac{c}{c_{f=0}} = \frac{\omega}{\sqrt{\omega^{2}-f^{2}}}
= \frac{1}{\sqrt{1-(f/\omega)^{2}}},$$

which is $1/\sqrt{1-(0.7339)^{2}} = 1.472$ at $45^\circ$N and $2.28$ at
$60^\circ$N ($\lambda$ grows from 142 km to 325 km). At the **tidal latitude
cut-off**, where $f = \omega_{M2}$ — that is,
$\sin\phi = \omega_{M2}/2\Omega = 0.9635$, or $\phi = 74.5^\circ$ — the ratio
diverges and no freely propagating internal tide of that frequency exists: the
tide becomes evanescent poleward of roughly $74.5^\circ$ latitude for the M2
frequency. This is a sharp, testable prediction that follows from one relation.

## 4. Vertical modes

For a flat bottom, a rigid lid and no rotation, the vertical structure satisfies

$$\frac{\mathrm{d}^{2}\phi}{\mathrm{d}z^{2}} + \frac{N^{2}(z)}{c^{2}}\phi = 0,
\qquad \phi(0) = \phi(H) = 0,$$

a Sturm–Liouville eigenproblem in $\lambda = 1/c^{2}$. Discretising on a grid of
spacing $h$ gives the generalised matrix problem
$-\mathcal{D}_2\boldsymbol{\phi} = \lambda\,\mathrm{diag}(N^{2})\boldsymbol{\phi}$,
which the demonstration solves.

**Constant $N$.** The analytic eigenvalues are $m_n = n\pi/H$, so
$c_n = NH/(n\pi)$:

| mode | $\lambda = 1/c^{2}$ (s$^{2}$ m$^{-2}$) | $c$ from the eigenproblem (m s$^{-1}$) | $c = NH/(n\pi)$ (m s$^{-1}$) |
|---|---|---|---|
| 1 | $9.869553\times10^{-2}$ | 3.1831 | 3.1831 |
| 2 | $3.947760\times10^{-1}$ | 1.5916 | 1.5915 |
| 3 | $8.882231\times10^{-1}$ | 1.0611 | 1.0610 |

The agreement to four figures is the numerical scheme reproducing an analytic
answer — a *verification* against a known solution, not a validation.

**Structured $N(z)$.** With
$N(z) = 0.006 + 0.008e^{-z/300}\ \mathrm{rad\,s^{-1}}$:

| mode | $c$ (m s$^{-1}$) | $c/c(\text{constant } N \text{ at the surface})$ |
|---|---|---|
| 1 | 2.5457 | 0.7998 |
| 2 | 1.3123 | 0.8245 |
| 3 | 0.8789 | 0.8284 |

The mode speed drops by about $20\,\%$. **The mode speed is an integral of
stratification, weighted toward the region where the eigenfunction is large** —
not its surface value. Substituting the computed mode-1 eigenvector back into the
differential equation gives a residual of $6.7\times10^{-7}$ on 398 nodes, which
is grid-truncation error and decreases as $h^{2}$. Reporting a single "internal
wave speed" for a basin is therefore a claim about a particular mode of a
particular stratification.

## 5. Characteristic slopes and generation

Eliminating $k$ and $m$ between the dispersion relation and the definition of the
slope leads to the **characteristic slope** of internal-wave energy propagation:

$$\boxed{\;s = \sqrt{\frac{\omega^{2}-f^{2}}{N^{2}-\omega^{2}}}
\qquad \text{(energy rays at angle } \arctan s \text{ from horizontal)}.\;}$$

With $N = 0.010\ \mathrm{rad\,s^{-1}}$, $f$ at $45^\circ$N and the M2 frequency:

$$s = \sqrt{\frac{(1.4052\times10^{-4})^{2} - (1.0313\times10^{-4})^{2}}
{(0.010)^{2} - (1.4052\times10^{-4})^{2}}}
= \sqrt{\frac{9.110\times10^{-9}}{9.9998\times10^{-5}}}
= 9.546\times10^{-3} = \frac{1}{104.8} .$$

That is **$0.55^\circ$ from horizontal** — tidal beams are nearly flat, which is
why they cross an ocean basin with little attenuation and why a generation site
can influence a coast thousands of kilometres away.

Whether a given topographic slope generates internal tides efficiently depends on
the ratio of the two slopes, the **criticality** $\gamma = s_{\text{topo}}/s$:

| ridge slope | $\gamma$ | regime |
|---|---|---|
| $1.0\times10^{-4}$ | 0.010 | subcritical (weak generation) |
| $1.0\times10^{-3}$ | 0.105 | subcritical |
| $5.0\times10^{-3}$ | 0.524 | near-critical |
| $9.546\times10^{-3}$ | 1.000 | critical (most efficient) |
| $2.0\times10^{-2}$ | 2.095 | supercritical (beams trapped near the slope) |
| $5.0\times10^{-2}$ | 5.238 | supercritical |

The three regimes are distinguishable by an observable: subcritical topography
produces a weak, broad beam; near-critical topography produces a strong beam
along a well-defined direction; supercritical topography traps energy in
small-scale motion near the slope. **The slope ratio, not the topographic height,
is the predictor.**

## 6. Shear instability and the Richardson number

Stratification suppresses shear instability and shear promotes it. The
dimensionless competition is the **gradient Richardson number**

$$\mathrm{Ri} = \frac{N^{2}}{\left(\partial u/\partial z\right)^{2}} .$$

The classical necessary condition for Kelvin–Helmholtz instability in an
inviscid, parallel, stably stratified shear flow is $\mathrm{Ri} < 1/4$
*somewhere* in the flow. The demonstration uses

$$N(z) = 0.010 + 0.006\tanh\!\left(\frac{z-100}{20}\right)\ \mathrm{rad\,s^{-1}},
\qquad
U(z) = 0.60\tanh\!\left(\frac{z-100}{25}\right)\ \mathrm{m\,s^{-1}},$$

| $z$ (m) | $N$ (s$^{-1}$) | $U$ (m s$^{-1}$) | $\mathrm{d}U/\mathrm{d}z$ (s$^{-1}$) | $\mathrm{Ri}$ |
|---|---|---|---|---|
| 0 | 0.0040 | $-0.600$ | 0.0000 | $1.53\times10^{4}$ |
| 60 | 0.0042 | $-0.553$ | 0.0036 | 1.362 |
| 90 | 0.0072 | $-0.228$ | 0.0205 | 0.124 |
| 100 | 0.0100 | 0.000 | 0.0240 | 0.174 |
| 140 | 0.0158 | 0.553 | 0.0036 | 19.09 |
| 200 | 0.0160 | 0.600 | 0.0000 | $2.45\times10^{5}$ |

The minimum is $\mathrm{Ri} = 0.1237$ at $z = 89.3$ m, and
$\mathrm{Ri} < 1/4$ over $z = 74.5$ to $105.1$ m: a **$30.6\ \mathrm{m}$ thick**
layer. Two cautions, both essential:

- $\mathrm{Ri}<1/4$ is **necessary, not sufficient**. It says a layer *may*
  become unstable, not that it has, and it says nothing about the mixing rate
  once it does.
- $\mathrm{Ri}>1/4$ *everywhere* proves nothing about the absence of turbulence,
  because the criterion was derived for an inviscid parallel flow and real
  turbulence can be maintained by other routes.

## 7. From dissipation to diffusivity: the Osborn relation

Turbulent mixing is measured as a **dissipation rate of turbulent kinetic
energy** $\epsilon$ (W kg$^{-1}$), typically by resolving centimetre-scale shear
with a microstructure profiler. Converting that to a **diffusivity** — the
quantity the circulation models need — requires the Osborn (1980) closure

$$\boxed{\;K_\rho = \Gamma\frac{\epsilon}{N^{2}}\;}$$

with the **mixing efficiency** $\Gamma$, conventionally taken as $0.2$. With
$\epsilon = 1.0\times10^{-9}\ \mathrm{W\,kg^{-1}}$ and
$N = 0.010\ \mathrm{rad\,s^{-1}}$:

$$K_\rho = 0.2 \times \frac{1.0\times10^{-9}}{1.0\times10^{-4}}
= 2.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}.$$

The molecular diffusivity of heat in water is about
$1.4\times10^{-7}\ \mathrm{m^{2}\,s^{-1}}$, so this turbulent value is
$\sim14$ times molecular — the "fourteen" is worth remembering, because it is
small: much of the ocean mixes at a rate within an order of magnitude of
molecular diffusion, and the remainder mixes a thousand times faster.

**The honest part.** $K_\rho$ above is not a measurement; it is
$\Gamma\times$(a measurement)/$N^{2}$. With $\Gamma = 0.5$ the same data give
$5.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$ — a factor 2.5 — and nothing in the
dissipation measurement chooses between the two. The conventional $\Gamma = 0.2$
is a modelling choice supported by a body of experiments, not a derivation. Any
budget that consumes $K_\rho$ inherits a factor-of-a-few uncertainty before it
starts.

## 8. Assumptions and regime of validity

1. **Linearised, Boussinesq, $f$-plane, constant $N$.** The dispersion relation
   is exact only under these hypotheses; with $N(z)$ the vertical modes
   (Section 4) must be solved rather than assumed.
2. **Small amplitude.** Nonlinear internal waves — solitons, bores — are a
   separate regime and are not described here.
3. **No background flow for the dispersion relation.** A mean shear Doppler-shifts
   the frequencies; with a mean flow of $U$ along $k$, replace
   $\omega$ by $\omega - kU$.
4. **Flat bottom and rigid lid** for the mode problem. A free surface changes the
   modes by of order $\rho/\rho_{\text{atm}}$; a sloping bottom does not have
   normal modes at all.
5. **$\mathrm{Ri}$ from resolved profiles.** Both $N^{2}$ and shear must be
   resolved. A profiler that averages over the unstable layer will measure an
   $\mathrm{Ri}$ that is too large.
6. **$\Gamma$ constant.** The demonstration's own sensitivity shows a factor 2.5
   across defensible values; $\Gamma$ also varies with the turbulence's
   age and with $\mathrm{Ri}$.

## 9. Worked examples

### Example 1 — the mode-1 internal tide by hand

$N = 0.008\ \mathrm{rad\,s^{-1}}$, $H = 2000\ \mathrm{m}$, $f$ at $30^\circ$N
($7.292\times10^{-5}$), M2 ($\omega = 1.4052\times10^{-4}$).

$$m = \frac{\pi}{2000} = 1.5708\times10^{-3}\ \mathrm{m^{-1}},$$

$$k^{2} = m^{2}\frac{\omega^{2}-f^{2}}{N^{2}-\omega^{2}}
= (1.5708\times10^{-3})^{2}\frac{1.9746\times10^{-8} - 5.317\times10^{-9}}
{6.40\times10^{-5} - 1.9746\times10^{-8}}$$

$$= (2.4674\times10^{-6})\frac{1.4429\times10^{-8}}{6.3980\times10^{-5}}
= (2.4674\times10^{-6})(2.2552\times10^{-4}) = 5.5645\times10^{-10},$$

$$k = 2.359\times10^{-5}\ \mathrm{m^{-1}}, \qquad
\lambda = \frac{2\pi}{k} = 2.664\times10^{5}\ \mathrm{m} = 266.4\ \mathrm{km},$$

$$c = \frac{\omega}{k} = \frac{1.4052\times10^{-4}}{2.359\times10^{-5}}
= 5.957\ \mathrm{m\,s^{-1}} .$$

Cross-check without rotation: $NH/\pi = 0.008 \times 2000/\pi
= 5.093\ \mathrm{m\,s^{-1}}$; rotation has lengthened the wave by the factor
$5.957/5.093 = 1.170$, the same $1.17$ found at $30^\circ$N in Section 3.

### Example 2 — characteristic slope at a different latitude

Same $N$ but at $10^\circ$N, where $f = 2.532\times10^{-5}$:

$$s = \sqrt{\frac{1.9746\times10^{-8} - 6.41\times10^{-10}}
{1.0\times10^{-4} - 1.9746\times10^{-8}}}
= \sqrt{\frac{1.9105\times10^{-8}}{9.9998\times10^{-5}}} = 1.382\times10^{-2},$$

i.e. $1/72$, or $0.79^\circ$ from horizontal — about $1.45$ times the
$45^\circ$N value of $9.546\times10^{-3}$. Since the criticality is
$\gamma = s_{\text{topo}}/s$, a **steeper** characteristic slope means a
**smaller** $\gamma$: the same seafloor slope is *less* critical at low latitude,
because $f$ is smaller there. The characteristic slope is largest at the equator,
where $s = \omega/\sqrt{N^{2}-\omega^{2}} = 1.405\times10^{-2}$ for these values,
and it collapses to zero as $f\to\omega$ at the tidal cut-off. This latitude
dependence is one of the few in physical oceanography that is robust to the
details of the model.

### Example 3 — what a $20\,\%$ $N$ error costs

Suppose the stratification is known only to $20\,\%$. From
$K_\rho = \Gamma\epsilon/N^{2}$, a $20\,\%$ error in $N$ gives a $44\,\%$ error in
$K_\rho$ at fixed $\epsilon$ (since $1/(1.2)^{2} = 0.694$). Combined with the
factor $2.5$ from $\Gamma$, an inferred diffusivity carries an uncertainty of
roughly a factor $1.7$ from these two sources alone, with no other error
included. The honest report is "$K_\rho$ between $x$ and $y$", never a single
number without its closure.

## 10. Python demonstration

`code/internal_waves_tides_demo.py` prints everything above with units:

1. the dispersion relation on a grid of $(k,m)$, including both limits;
2. the mode-1 internal tide with and without rotation, at five latitudes;
3. the vertical-mode eigenproblem for constant and structured $N(z)$, with the
   eigenvector residual;
4. characteristic slopes and a criticality table;
5. $\mathrm{Ri}$ from synthetic $N(z)$ and $U(z)$, with the unstable layer's
   thickness;
6. the Osborn table and the $\Gamma$ sensitivity;
7. two numerical verifications: the wavenumber and angle forms of the dispersion
   relation agree to $1.1\times10^{-18}$, and the mode-1 wavenumber substituted
   back into the dispersion relation returns the forcing frequency with a
   relative error of $0.000\times10^{0}$.

Run it with

```bash
cd 15-oceanography-marine/01-physical-oceanography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python internal_waves_tides_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/04-internal-waves-and-tides-exercises.md`](exercises/04-internal-waves-and-tides-exercises.md)
and
[`exercises/04-internal-waves-and-tides-solutions.md`](exercises/04-internal-waves-and-tides-solutions.md).

- ★ Compute the internal-wave frequency for $k = m = 2\times10^{-3}\
  \mathrm{m^{-1}}$ with $N = 0.012$ and $f = 1.0\times10^{-4}$.
- ★★ Derive $k^{2} = m^{2}(\omega^{2}-f^{2})/(N^{2}-\omega^{2})$ from the
  dispersion relation and evaluate it for the lesson's mode-1 tide.
- ★★ Solve the vertical-mode problem by hand for a two-layer stratification and
  compare with the continuous result.
- ★★★ Design a microstructure survey that would determine $K_\rho$ to within a
  factor 2, and state which assumption dominates your error budget.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use $N = 0.010\
\mathrm{rad\,s^{-1}}$, $f = 1.0313\times10^{-4}\ \mathrm{rad\,s^{-1}}$ (the
value at $45^\circ$N), M2 period $12.4206\ \mathrm{h}$, and
$\Gamma = 0.2$.

> **(a)** Compute the frequency of an internal wave with
> $k = 5.0\times10^{-5}\ \mathrm{m^{-1}}$ and $m = 5.0\times10^{-4}\
> \mathrm{m^{-1}}$, and state whether it lies in the permitted band.
> **(b)** Compute the internal-wave characteristic slope $s$ for the M2
> frequency, and the topographic slope that would be critical for it.
> **(c)** A microstructure profile reports $\epsilon = 5.0\times10^{-9}\
> \mathrm{W\,kg^{-1}}$ in water with $N = 0.008\ \mathrm{rad\,s^{-1}}$. Compute
> $K_\rho$ and state the two assumptions that stand between your number and a
> measurement of mixing.
> **(d)** Doubling $N$ at fixed $\epsilon$ changes $K_\rho$ by what factor?

A worked version of (a)–(d) is in the lesson-04
[solutions](exercises/04-internal-waves-and-tides-solutions.md).

## Common pitfalls

1. **Using $N$ from a surface value.** Section 4: the mode speed is a weighted
   integral of stratification and falls by $20\,\%$ for a realistic $N(z)$.
2. **Assuming internal waves fill the frequency band below $N$.** Rotation
   removes everything below $f$; the band is $f < \omega < N$, and near the
   poles it can close entirely for a given tidal frequency.
3. **Treating the characteristic slope as a property of the topography.**
   Section 5: $s$ depends on the frequency, the stratification and the latitude;
   what matters is the *ratio*.
4. **Reading $\mathrm{Ri}<1/4$ as a prediction.** It is a necessary condition for
   one class of instability, not a statement about mixing intensity.
5. **Quoting $K_\rho$ as a measurement.** It is $\Gamma\epsilon/N^{2}$; the
   demonstration's own sensitivity gives a factor $2.5$ from $\Gamma$ alone.
6. **Forgetting that group velocity is perpendicular to the wavevector.** Energy
   travels along the crests; an energy budget built on the phase velocity will be
   wrong by a rotation of $90^\circ$.
7. **Reporting a buoyancy period without the density that produced it.** $N^{2}$
   comes from a potential density gradient, with all the caveats of Lesson 01.

## Related modules

- [01 Seawater Properties: Temperature, Salinity, Density](01-seawater-properties.md) —
  where $N^{2}$ and its sign convention come from.
- [03 Thermohaline Circulation and Deep Water Formation](03-thermohaline-circulation.md) —
  the circulation that consumes the $\kappa$ this lesson measures.
- [05 Sea Level, Tides and Harmonic Analysis](05-sea-level-and-tides.md) —
  the tidal forcing whose harmonic analysis supplies $\omega$ here.
- [02-06-04 Turbulence and Eddy Transport](../../02-physics/06-fluid-mechanics/04-turbulence.md) —
  the closure this lesson must assume.
- [20-08-02 Spectral Analysis of Tides and Earth Signals](../../20-signal-processing/08-timeseries-analysis-geophysics/02-spectral-analysis-tides.md) —
  extracting the tidal lines from a noisy record.
- [Module 15-02 Marine Geophysical Methods](../02-marine-geophysics-methods/README.md) —
  the acoustic systems whose resolution shares the same wavelength logic.

## Self-assessment checklist

- [ ] I can derive the dispersion relation and state its two limits.
- [ ] I can compute a mode-1 internal tide wavelength, with and without rotation.
- [ ] I can solve the vertical-mode problem numerically and verify the solution.
- [ ] I can compute a characteristic slope and classify topography.
- [ ] I can compute a Richardson number profile and say what it proves.
- [ ] I can apply the Osborn relation and state its uncertainty.
- [ ] I can keep "dissipation" and "diffusivity" separate in my own writing.
