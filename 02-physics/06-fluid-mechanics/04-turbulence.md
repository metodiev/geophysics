---
id: 02-06-04
title: "Turbulence, Mixing and Eddy Diffusivity"
level: graduate
prereqs: ["02-06-03", "02-06-02"]
estimated_minutes: 90
tags: [turbulence, mixing, eddy-diffusivity, kolmogorov]
---

# Turbulence, Mixing and Eddy Diffusivity

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why the nonlinear term of the Navier–Stokes equation makes the
   flow unstable, and describe the energy cascade from forcing scales to the
   Kolmogorov scale.
2. **Derive** the Kolmogorov microscales from dimensional analysis and compute
   them for a stream, the ocean surface layer and the atmosphere.
3. **Perform** Reynolds averaging, identify the Reynolds stress, and state the
   **closure problem** precisely: why the averaged equations contain more
   unknowns than equations and cannot be closed by any manipulation of the
   resolved fields.
4. **Derive** the log-law velocity profile as the mixing-length closure, verify
   the implied eddy viscosity, and state the assumptions that make it a closure
   rather than a law.
5. **Compute** the Richardson number, explain the suppression of turbulence by
   stratification, and demonstrate numerically that the eddy diffusivity is not
   determined by the resolved gradients.
6. **Verify** the $-5/3$ spectral slope numerically, and state honestly what a
   spectrum can and cannot determine about dissipation.
7. **State** what is and is not justified when turbulent transport is
   parameterised, and name the observations that test the parameterisation.

## Prerequisites

- [02-06-03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md)
  — the laminar solutions and the transition criterion this lesson starts from.
- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md)
  — the nonlinear term whose consequences these are.
- [02-03-07 Dispersion and the Group Velocity](../03-oscillations-and-waves/07-dispersion.md)
  — spectra and length scales, used here for the energy spectrum.

## 1. The phenomenon, and why it is hard

Above a critical Reynolds number a smooth flow becomes turbulent: chaotic,
three-dimensional, unsteady, with motion over a wide range of scales and with
strong mixing. The transition is not a subtle effect. A laminar pipe flow and a
turbulent one at the same pressure gradient differ in flow rate by a factor of
several, and in the transport of heat and mass by orders of magnitude.

Turbulence is hard for a reason that is structural, not merely technical. The
Navier–Stokes equation is deterministic: given the initial and boundary
conditions, the solution is determined. But turbulent solutions are
*chaotic* — sensitive to initial conditions — so an exact solution is not a
prediction. Worse, the quantity we want (the average transport over a season, or
the drag over a coastline) requires averaging, and averaging does not commute
with the nonlinearity. This is the **closure problem**, and it is the central
intellectual content of the subject.

## 2. Precise definitions

**Reynolds decomposition.** Write any field as $\phi = \overline{\phi} + \phi'$,
where the overbar is an average (time, space or ensemble) and the prime is the
fluctuation, with $\overline{\phi'} = 0$ by construction.

**Reynolds stress.** The tensor $\rho\,\overline{u_i'u_j'}$, an apparent stress
that arises purely from the averaging of the nonlinear term. It is not a
material property; it is a correlation of the flow.

**Kolmogorov microscales.** The length, velocity and time scales at which
viscosity finally dissipates the kinetic energy:

$$\eta = \left(\frac{\nu^3}{\varepsilon}\right)^{1/4}, \qquad
u_\eta = (\nu\varepsilon)^{1/4}, \qquad
\tau_\eta = \left(\frac{\nu}{\varepsilon}\right)^{1/2}, \tag{1}$$

with $\varepsilon$ the rate of kinetic-energy dissipation per unit mass
(m² s⁻³).

**Inertial subrange.** The band of scales between the forcing scale and $\eta$ in
which neither production nor dissipation acts and energy is simply passed down
the cascade.

**Eddy diffusivity $K$.** A coefficient, with the units of a diffusivity
(m² s⁻¹), defined by the assumption that a turbulent flux is proportional to the
mean gradient: $\overline{u'\phi'} = -K\,\partial\overline{\phi}/\partial x$. It
is a *parameterisation*, not a property of the fluid.

**Mixing length $l$.** The distance a fluid parcel is imagined to travel before
losing its identity; the analogue of the mean free path. In the log layer,
$l = \kappa y$ with $\kappa \approx 0.41$ the von Kármán constant.

**Richardson number.** $Ri = N^2/(\partial u/\partial z)^2$ with
$N^2 = (g/\theta)\,\partial\theta/\partial z$ the buoyancy frequency squared. It
measures stratification against shear; above a critical value of order $0.25$
turbulence is suppressed.

## 3. Derivations

### 3.1 Reynolds averaging and the closure problem

Split $\mathbf{u} = \overline{\mathbf{u}} + \mathbf{u}'$ and
$p = \overline{p} + p'$, substitute into continuity and momentum, and average.
For constant density,

$$\nabla\cdot\overline{\mathbf{u}} = 0, \tag{2}$$

$$\frac{\partial\overline{u_i}}{\partial t} +
\overline{u_j}\frac{\partial\overline{u_i}}{\partial x_j} =
-\frac{1}{\rho}\frac{\partial\overline{p}}{\partial x_i} +
\nu\nabla^2\overline{u_i} -
\frac{\partial}{\partial x_j}\overline{u_i'u_j'} + g_i. \tag{3}$$

The last term is the divergence of the Reynolds stress. Counting unknowns:
$\overline{u_i}$ (3) and $\overline{p}$ (1) — four — plus the six independent
components of $\overline{u_i'u_j'}$. Three-plus-one equations for ten unknowns.
**No manipulation of the averaged equations can close this system**, because the
missing information is about the fluctuations, which the averages have discarded.
Any closure — eddy viscosity, mixing length, $k$–$\varepsilon$, large-eddy
simulation — is an *added assumption*, and the honest description of a turbulence
model is a list of its assumptions, not a claim that it solved the equations.

### 3.2 The energy cascade and the Kolmogorov scales

Energy enters at the large scales (size $L$, velocity $U$), where the Reynolds
number is large and viscosity is irrelevant. The nonlinear term transfers energy
to smaller scales at a rate set by the large scales, $\varepsilon \sim U^3/L$,
essentially independently of $\nu$. At the smallest scales viscosity acts and the
cascade terminates. Balancing the inertial transfer rate against viscous
dissipation, using only $\nu$ and $\varepsilon$ (the quantities that matter at
that end of the range), dimensional analysis gives equation (1).

The scale separation is set by

$$\frac{L}{\eta} \sim Re^{3/4}, \tag{4}$$

so the number of grid points needed to resolve every scale in three dimensions
scales as $(L/\eta)^3 \sim Re^{9/4}$. At $Re = 10^{10}$ that is $10^{22.5}$ —
which is why direct numerical simulation cannot reach geophysical Reynolds
numbers and why every geophysical model parameterises something.

### 3.3 The inertial subrange and the $-5/3$ spectrum

In the inertial subrange the energy spectrum depends only on $k$ and
$\varepsilon$, so by dimensional analysis

$$E(k) = C_K\,\varepsilon^{2/3}k^{-5/3}, \tag{5}$$

with $C_K$ the Kolmogorov constant, an empirical number near $1.5$. Equation (5)
is the single most tested prediction in turbulence. It is a *shape* prediction
(the exponent) plus a level whose constant is empirical — an important
distinction, because a measured spectrum determines $C_K\varepsilon^{2/3}$ and
never $\varepsilon$ alone.

### 3.4 The log law as a mixing-length closure

Assume a turbulent flux is proportional to the mean gradient with a mixing
length $l$: $\nu_t \sim l^2|\partial u/\partial z|$, and take $l = \kappa z$ near
a wall. Then

$$\tau = \rho\nu_t\frac{\partial u}{\partial z} =
\rho\kappa^2z^2\left(\frac{\partial u}{\partial z}\right)^2
\;\Longrightarrow\;
\frac{\partial u}{\partial z} = \frac{u_*}{\kappa z}, \tag{6}$$

where $u_* = \sqrt{\tau/\rho}$ is the friction velocity. Integrating,

$$u(z) = \frac{u_*}{\kappa}\ln\frac{z}{z_0}, \tag{7}$$

with $z_0$ the roughness length. Substituting back gives the eddy viscosity

$$\nu_t = l^2\left|\frac{\partial u}{\partial z}\right| = \kappa u_* z,
\tag{8}$$

which grows linearly with height without bound. That unbounded growth is a
symptom, not a success: the closure cannot be valid far from the wall, and it is
patched by extending it to a boundary-layer depth or by switching to a
different closure in the outer layer.

### 3.5 Stratification: the Richardson number

Rotation and stratification compete with the turbulence's own tendency to mix.
For a stably stratified shear flow, the ratio of buoyancy restoring to shear
production is the gradient Richardson number

$$Ri = \frac{N^2}{(\partial u/\partial z)^2}, \qquad N^2 =
\frac{g}{\theta}\frac{\partial\theta}{\partial z}. \tag{9}$$

The classical linear-stability result is that $Ri < 1/4$ is necessary for shear
instability; in practice turbulence is strongly suppressed as $Ri$ approaches
$1/4$ and essentially absent above $Ri \sim 1$. A common closure is

$$K = \frac{l^2|\partial u/\partial z|}{1 + Ri/Ri_c}, \qquad Ri_c \approx 0.25.
\tag{10}$$

Equation (10) contains a parameter that no observation fixes uniquely; it is
calibrated. This is the honest description of the stratified closure.

## 4. Physical interpretation

**Why turbulent transport dominates.** The demo finds $\nu_t \approx 0.0205\
\mathrm{m^2\,s^{-1}}$ at 1 m above a bed with $u_* = 0.05\ \mathrm{m\,s^{-1}}$,
some $2.1\times10^{4}$ times the molecular viscosity of water. That ratio — not
a factor of two but four to five orders of magnitude — is why the ocean mixed
layer, the atmospheric boundary layer and a riffle in a stream are all mixed on
timescales of hours rather than months.

**Why turbulence is irreversible.** The cascade transfers energy from large to
small scales, where viscosity converts it to heat; it does not run backwards.
That is the origin of the arrow of time in fluid mechanics and it is why a
turbulence model needs a dissipation term, not just a diffusion term.

**Why an eddy diffusivity is not a property of the fluid.** Molecular diffusivity
is a property of the substance at a given temperature. Eddy diffusivity is a
property of the *flow*: the demo shows two layers with identical mean shear but
diffusivities differing by a factor of 66 once stratification is included. Two
models that agree perfectly on the mean velocity can still disagree by an order
of magnitude on the flux. This is the single most important idea in the lesson:
**when you see a $K$ or a $\nu_t$ in a geophysical paper, you are looking at a
modelling assumption, and the paper's conclusions inherit that assumption.**

## 5. Assumptions and regime of validity

| Assumption | Valid when | Fails when | What breaks |
|---|---|---|---|
| Statistical stationarity | Averages over a window long compared with the eddy turnover time | Rapidly evolving flows (a storm front, a tidal cycle) | The average is not well defined; use a conditional or wavelet average |
| Homogeneity | Turbulence properties vary slowly in space | Near boundaries, sharp fronts | Horizontal gradients of turbulence statistics matter |
| Gradient-diffusion closure (downgradient flux) | Small eddies, isotropic, weak stratification | Convective boundary layers, strong stratification | **Counter-gradient fluxes**: the flux has the opposite sign to the local gradient |
| Local equilibrium (production = dissipation) | Slow change versus $\tau_\eta$ and outer timescales | Rapid transitions | Transport of turbulent kinetic energy must be retained |
| Isotropy in the small scales | Universally, per Kolmogorov — but only at small scales | Large scales, stratified flow | Anisotropic stresses; scalar and momentum diffusivities differ |
| $l = \kappa z$ | Near a rough wall within the log layer | Free shear layers, outer boundary layers | Mixing length must be prescribed differently |
| $C_K$ universal | Empirically near 1.5 for high $Re$ | Low $Re$, strongly stratified, magnetised | Spectrum level changes; only the exponent is robust |

Three of these deserve emphasis.

**The gradient-diffusion assumption is the one to distrust.** It is the
Boussinesq hypothesis of turbulence modelling, and it is *known to fail* in the
convective boundary layer, where large eddies transport heat counter to the local
gradient. Its failure is not an obscure corner: it is the daytime atmosphere over
land.

**Counter-gradient flux has a direct observational signature**: a region where
the flux and the gradient have opposite signs. A model with a positive $K$ cannot
reproduce it, and this is a testable prediction, not a matter of taste.

**"Parameterised" is not a synonym for "small".** In a climate model the
atmospheric boundary layer is entirely parameterised in its vertical transport,
and it is where the surface fluxes that drive the model are computed. The
parameterisation is not a detail; it is where the physics meets the model.

## 6. Units and dimensional analysis

$$[\varepsilon] = \mathrm{m^2\,s^{-3}}, \qquad [\eta] =
(\mathrm{m^6\,s^{-3}}/\mathrm{m^2\,s^{-3}})^{1/4} = \mathrm{m}, \qquad
[K] = \mathrm{m^2\,s^{-1}}. \tag{11}$$

The Richardson number is dimensionless:
$[N^2] = \mathrm{s^{-2}}$ and $[(\partial u/\partial z)^2] = \mathrm{s^{-2}}$.
Its critical value $1/4$ is therefore a pure number with no units attached, which
is why it can be compared with a laboratory measurement.

Two useful scalings, both dimensional:

- **Dissipation from the large scales:** $\varepsilon \sim U^3/L$. Check:
  $\mathrm{m^3\,s^{-3}}/\mathrm{m} = \mathrm{m^2\,s^{-3}}$. Correct.
- **Eddy diffusivity from a length and a velocity:** $K \sim l\,u'$ with $u'$
  the turbulent velocity scale. Check: $\mathrm{m}\cdot\mathrm{m\,s^{-1}} =
  \mathrm{m^2\,s^{-1}}$. Correct, and it is the same structure as the mixing
  length.

## 7. Python demonstration

[`code/turbulence_demo.py`](./code/turbulence_demo.py) computes Kolmogorov
scales, verifies the log-law closure, shows the non-uniqueness of the eddy
diffusivity, verifies the $-5/3$ slope and compares mixing times. Its actual
output includes:

```text
                      flow   nu (m^2/s)    eps (m^2/s^3)   eta (mm)  u_eta (mm/s)   tau_eta (s)
           mountain stream    1.000e-06        1.000e-01     0.0562       17.7828     3.162e-03
       ocean surface layer    9.756e-07        1.000e-05     0.5520        1.7673     3.123e-01
 atmospheric surface layer    1.500e-05        1.000e-02     0.7622       19.6799     3.873e-02
```

```text
   y (m)    u (m/s)   du/dy (1/s)  l = kappa*y (m)   nu_t = l^2|du/dy|  nu_t/(kappa u* y)
    0.01     0.2808       12.1951          0.00410             0.00020           1.000000
    1.00     0.8424        0.1220          0.41000             0.02050           1.000000
  100.00     1.4040        0.0012         41.00000             2.05000           1.000000
  nu_t at y = 1 m is 0.0205 m^2/s, i.e. 2.101e+04 times the molecular
  viscosity of water. This is the quantitative reason turbulent transport dominates.
```

```text
l = 10.0 m, du/dz = 0.01 1/s, g/theta = 0.03270 K^-1 m s^-2
  dtheta/dz (K/m)   N^2 (1/s^2)        Ri  suppression   K (m^2/s)
            0.000     0.000e+00    0.0000      1.00000     1.00000
            0.010     3.270e-04    3.2700      0.07102     0.07102
            0.050     1.635e-03   16.3500      0.01506     0.01506
  the mean gradient du/dz is identical in every row, yet K spans nearly two decades.
```

```text
synthetic E(k) = C eps^(2/3) k^(-5/3) sampled over k = 1 to 1e3 (121 points)
  fitted slope in log-log        = -1.6666666667  (exact -1.6666666667)
  dissipation rate recovered from the fitted level = 1.000000e-05 m^2/s^3
```

```text
                     setting    h (m)   K (m^2/s)              t
          lake, 10 m, summer       10   1.000e-03     1.0000e+05
       abyssal ocean, 4000 m     4000   1.000e-04     1.6000e+11
  atmospheric boundary layer     1000   1.000e+01     1.0000e+05
```

### What to observe

| Observation | Consequence |
|---|---|
| $\eta$ ranges from 0.056 mm in a mountain stream to 0.76 mm in the atmosphere | The dissipative scales are millimetre-to-sub-millimetre; a model with 10 m grid cells parameterises every one of them |
| The mantle is deliberately absent from the Kolmogorov table | Its effective $Re \sim 10^{-20}$; there is no cascade and no Kolmogorov range. Computing $\eta$ there would be a category error |
| The last column of the log-law table is exactly 1.000000 at every height | The log law *is* the mixing-length closure with $l=\kappa z$; the agreement is a property of the closure, not evidence for it |
| $\nu_t$ at 1 m is $2.1\times10^{4}$ times molecular $\nu$ | Turbulent transport dominates by four to five orders of magnitude, which is why mixing timescales are minutes to hours rather than years |
| With the same mean shear, $K$ falls from 1.0 to 0.015 as stratification rises | The eddy diffusivity is not determined by the resolved field; the closure injects information that the gradients do not contain |
| The fitted spectral slope is $-1.6666666667$, equal to $-5/3$ to ten digits | The spectrum's *shape* is a genuine prediction; it is a robust measurement |
| The recovered $\varepsilon$ equals the input only because $C_K = 1.5$ was assumed | A spectrum fixes $C_K\varepsilon^{2/3}$, never $\varepsilon$ alone. Quoting $\varepsilon$ from a spectrum is quoting a product divided by an assumed constant |
| The abyssal-ocean mixing time is $1.6\times10^{11}$ s, about 5000 years | Ocean ventilation is slow because $K$ there is $10^{-4}$ m² s⁻¹, three orders below a stirred layer |

> **Breaking exercise.** The last statement is testable: change $C_K$ from 1.5 to
> 2.0 in the spectrum section and predict, before running, which outputs change
> and which do not. The **slope** must be unchanged; the recovered $\varepsilon$
> must scale as $C_K^{-3/2}$. Then explain why that is the correct diagnosis of
> any "measured dissipation rate" quoted from a spectrum alone.

## 8. Common mistakes

1. **Treating an eddy diffusivity as a fluid property.** It is a property of the
   flow and of the closure; quoting it without the closure is meaningless.
2. **Assuming downgradient fluxes.** Counter-gradient transport occurs routinely
   in the convective boundary layer, and no positive $K$ reproduces it.
3. **Quoting an $\varepsilon$ from a spectral level without the constant.** A
   spectrum determines $C_K\varepsilon^{2/3}$.
4. **Using the log law far from the wall.** It is a near-wall closure; $\nu_t
   \propto z$ cannot hold to the top of the boundary layer.
5. **Applying turbulence theory where there is no turbulence.** The mantle has no
   cascade; a laminar, viscous-dominated flow has no cascade; a strongly
   stratified fluid may have intermittent, patchy turbulence that no $K$
   represents.
6. **Forgetting that Reynolds averaging is over an ensemble of realisations
   while data are a single time series.** The ergodic assumption is testable and
   not always true.
7. **Assuming isotropy at all scales.** Isotropy is a small-scale property;
   geophysical turbulence is anisotropic at the scales that carry the transport.
8. **Treating a large-eddy simulation as a solution.** It is a model with a
   subgrid closure, and its results inherit that closure.
9. **Ignoring the intermittency of stratified turbulence.** Averaging over a
   window that contains both turbulent and quiescent patches gives a $K$ that
   describes neither.

## 9. Real-world applications

- **Ocean mixing.** Diapycnal mixing rates set the overturning circulation and
  the uptake of heat and carbon; the mixing is parameterised, and constraining
  that parameterisation is an active observational problem in
  [15-oceanography-marine](../../15-oceanography-marine/README.md).
- **Atmospheric boundary layer.** Surface fluxes of heat, moisture and momentum
  are computed from parameterised turbulent transport in every weather and
  climate model — see [16-atmosphere-climate](../../16-atmosphere-climate/README.md).
- **Rivers and floods.** The Manning and Chézy friction laws are
  parameterisations of turbulent wall drag, calibrated for channels, and their
  coefficients are as much empirical as the log law's $z_0$.
- **Sediment and pollutant transport.** The vertical distribution of suspended
  sediment follows from a balance of settling against an eddy diffusivity that
  is itself uncertain by a factor of a few.
- **Magma and hydrothermal systems.** Convective heat transport through a
  fracture network is often represented as an enhanced thermal conductivity —
  the same eddy-diffusivity idea, with the same caveats.
- **Mantle mixing.** Chemical heterogeneity is stirred by convection, but at
  $Re \sim 10^{-20}$ there is no turbulent cascade; mixing is chaotic advection
  by a laminar, time-dependent flow, a genuinely different mechanism.

## 10. Further reading

- **Tennekes, H., & Lumley, J. L. *A First Course in Turbulence* (MIT Press).**
  The standard introduction; especially clear on the closure problem and the
  Kolmogorov hypotheses. Level: graduate.
- **Pope, S. B. *Turbulent Flows* (Cambridge University Press).** The reference
  for the statistical treatment, the closure problem and eddy-viscosity models.
  Level: graduate.
- **Frisch, U. *Turbulence: The Legacy of A. N. Kolmogorov* (Cambridge
  University Press).** The cascade and the spectrum, with the mathematics.
  Level: graduate.
- **Stull, R. B. *An Introduction to Boundary Layer Meteorology* (Kluwer).** The
  applied parameterisation of the atmospheric boundary layer, with the
  counter-gradient problem treated explicitly. Level: graduate.
- **Batchelor, G. K. *An Introduction to Fluid Dynamics* (Cambridge University
  Press).** A careful account of what Reynolds averaging does and does not
  achieve. Level: advanced.
- **Monin, A. S., & Yaglom, A. M. *Statistical Fluid Mechanics* (MIT Press).**
  The comprehensive treatment of the statistical theory. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md) —
  the laminar layer this one replaces.
- [05 Flow in Porous Media: Darcy's Law and Permeability](./05-porous-media-flow.md)
  — the other great volume-averaged closure, with the same honesty requirement.
- [06 Mantle Convection and Rayleigh–Bénard Instability](./06-mantle-convection.md)
  — a high Rayleigh number flow with *no* turbulent cascade.
- [07 Rotating Fluids, Coriolis Effect and Geostrophic Balance](./07-geophysical-fluids.md)
  — rotation further constrains turbulence to quasi-two-dimensional motion.
- [02-03-10 Attenuation and the Quality Factor](../03-oscillations-and-waves/10-attenuation.md)
  — scattering and attenuation, where a stochastic description also replaces a
  deterministic one.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  empirical closure coefficients are parameters to be inferred, with
  uncertainty, like any other.

Exercises:
[`exercises/04-turbulence-exercises.md`](./exercises/04-turbulence-exercises.md)
and [`exercises/04-turbulence-solutions.md`](./exercises/04-turbulence-solutions.md).

## Self-assessment checklist

- [ ] I can perform Reynolds averaging and write the Reynolds-averaged momentum
      equation with the Reynolds stress. (Section 3.1)
- [ ] I can state the closure problem precisely and explain why no manipulation
      closes it. (Section 3.1)
- [ ] I can derive the Kolmogorov microscales and compute them for a given
      $\nu$ and $\varepsilon$. (Sections 3.2, 7)
- [ ] I can derive the log law from a mixing-length closure and explain why its
      agreement with data is not evidence for the closure. (Section 3.4)
- [ ] I can compute a Richardson number and use it to argue about suppression.
      (Section 3.5)
- [ ] I can demonstrate that an eddy diffusivity is not fixed by the resolved
      gradient. (Sections 4, 7)
- [ ] I can verify the $-5/3$ slope and say what a spectrum cannot determine.
      (Sections 3.3, 7)
- [ ] I can name the regime in which each closure fails and the observation that
      falsifies it. (Section 5)
