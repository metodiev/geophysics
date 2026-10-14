---
id: 26-02-04
title: "Dimensional Analysis Quick Reference"
level: intermediate
prereqs: ["01-01-03"]
estimated_minutes: 20
tags: [reference, dimensional-analysis, dimensions]
---

# Dimensional Analysis Quick Reference

A lookup page for dimensions. Use it to check an equation in seconds rather than
minutes.

## 1. Dimensions of common quantities

Written in the base-dimension symbols $\mathrm{L}$ (length), $\mathrm{M}$
(mass), $\mathrm{T}$ (time), $\mathrm{I}$ (current), $\Theta$ (temperature),
$\mathrm{N}$ (amount), $\mathrm{J}$ (luminous intensity).

| Quantity | Symbol | Dimensions | SI unit |
|---|---|---|---|
| Length | $L$ | $\mathrm{L}$ | m |
| Area | $A$ | $\mathrm{L^2}$ | m² |
| Volume | $V$ | $\mathrm{L^3}$ | m³ |
| Plane angle | $\theta$ | $1$ | rad |
| Time | $t$ | $\mathrm{T}$ | s |
| Frequency | $f$ | $\mathrm{T^{-1}}$ | Hz |
| Angular frequency | $\omega$ | $\mathrm{T^{-1}}$ | rad/s |
| Mass | $m$ | $\mathrm{M}$ | kg |
| Density | $\rho$ | $\mathrm{M\,L^{-3}}$ | kg/m³ |
| Velocity | $v$ | $\mathrm{L\,T^{-1}}$ | m/s |
| Acceleration | $a$ | $\mathrm{L\,T^{-2}}$ | m/s² |
| Force | $F$ | $\mathrm{M\,L\,T^{-2}}$ | N |
| Pressure, stress | $p$ | $\mathrm{M\,L^{-1}\,T^{-2}}$ | Pa |
| Energy, work | $E$ | $\mathrm{M\,L^2\,T^{-2}}$ | J |
| Power | $P$ | $\mathrm{M\,L^2\,T^{-3}}$ | W |
| Momentum | — | $\mathrm{M\,L\,T^{-1}}$ | kg m/s |
| Angular momentum | — | $\mathrm{M\,L^2\,T^{-1}}$ | kg m²/s |
| Gravitational potential | $V$ | $\mathrm{L^2\,T^{-2}}$ | m²/s² |
| Gravitational constant | $G$ | $\mathrm{L^3\,M^{-1}\,T^{-2}}$ | m³ kg⁻¹ s⁻² |
| Dynamic viscosity | $\eta$ | $\mathrm{M\,L^{-1}\,T^{-1}}$ | Pa·s |
| Kinematic viscosity, diffusivity | $\nu,\kappa$ | $\mathrm{L^2\,T^{-1}}$ | m²/s |
| Surface tension | $\gamma$ | $\mathrm{M\,T^{-2}}$ | N/m |
| Wavenumber | $k$ | $\mathrm{L^{-1}}$ | rad/m |
| Slowness | $s$ | $\mathrm{L^{-1}\,T}$ | s/m |
| Thermal conductivity | $k$ | $\mathrm{M\,L\,T^{-3}\,\Theta^{-1}}$ | W m⁻¹ K⁻¹ |
| Specific heat capacity | $c_p$ | $\mathrm{L^2\,T^{-2}\,\Theta^{-1}}$ | J kg⁻¹ K⁻¹ |
| Heat flux density | $q$ | $\mathrm{M\,T^{-3}}$ | W/m² |
| Entropy | $S$ | $\mathrm{M\,L^2\,T^{-2}\,\Theta^{-1}}$ | J/K |
| Elastic stiffness | $C_{ijkl}$ | $\mathrm{M\,L^{-1}\,T^{-2}}$ | Pa |
| Young's modulus | $E$ | $\mathrm{M\,L^{-1}\,T^{-2}}$ | Pa |
| Strain | $\varepsilon$ | $1$ | — |
| Electric charge | $q$ | $\mathrm{I\,T}$ | C |
| Electric field | $\mathbf{E}$ | $\mathrm{M\,L\,T^{-3}\,I^{-1}}$ | V/m |
| Electric potential | $\phi$ | $\mathrm{M\,L^2\,T^{-3}\,I^{-1}}$ | V |
| Magnetic flux density | $\mathbf{B}$ | $\mathrm{M\,T^{-2}\,I^{-1}}$ | T |
| Magnetic field strength | $\mathbf{H}$ | $\mathrm{I\,L^{-1}}$ | A/m |
| Electric conductivity | $\sigma$ | $\mathrm{M^{-1}\,L^{-3}\,T^3\,I^2}$ | S/m |
| Electric resistivity | $\rho_e$ | $\mathrm{M\,L^3\,T^{-3}\,I^{-2}}$ | Ω·m |
| Impedance | $Z$ | $\mathrm{M\,L^2\,T^{-3}\,I^{-2}}$ | Ω |
| Magnetic permeability | $\mu$ | $\mathrm{M\,L\,T^{-2}\,I^{-2}}$ | H/m |
| Electric permittivity | $\varepsilon$ | $\mathrm{M^{-1}\,L^{-3}\,T^4\,I^2}$ | F/m |
| Radioactivity (activity) | — | $\mathrm{T^{-1}}$ | Bq |
| Absorbed dose | — | $\mathrm{L^2\,T^{-2}}$ | Gy |

**Two entries worth noting deliberately:**

- $\mathbf{B}$ and $\mathbf{H}$ have **different dimensions**. This is a
  frequent source of confusion in geomagnetism, where both appear.
- Absorbed dose (gray) has the same dimensions as gravitational potential
  (m²/s²), because both are energy per unit mass. The identity is real, not a
  coincidence of the table.

## 2. The eight most useful equations, checked

Each row shows an equation, its dimensional check, and whether it balances.

| Equation | Description | Left | Right | Balances? |
|---|---|---|---|---|
| $g = GM/r^2$ | Point-mass gravity | $\mathrm{L\,T^{-2}}$ | $\mathrm{L^3M^{-1}T^{-2}\cdot M/L^2} = \mathrm{L\,T^{-2}}$ | ✓ |
| $g = \tfrac{4}{3}\pi G\rho r$ | Interior gravity (uniform sphere) | $\mathrm{L\,T^{-2}}$ | $\mathrm{L^3M^{-1}T^{-2}\cdot ML^{-3}\cdot L} = \mathrm{L\,T^{-2}}$ | ✓ |
| $V = GM/r$ | Gravitational potential | $\mathrm{L^2T^{-2}}$ | $\mathrm{L^3M^{-1}T^{-2}\cdot M/L} = \mathrm{L^2T^{-2}}$ | ✓ |
| $\tau = L^2/\kappa$ | Diffusion timescale | $\mathrm{T}$ | $\mathrm{L^2/(L^2T^{-1})} = \mathrm{T}$ | ✓ |
| $\omega = ck$ | Dispersion relation | $\mathrm{T^{-1}}$ | $\mathrm{LT^{-1}\cdot L^{-1}} = \mathrm{T^{-1}}$ | ✓ |
| $\delta = \sqrt{2/(\mu_0\sigma\omega)}$ | EM skin depth | $\mathrm{L}$ | $\sqrt{(\mathrm{MLT^{-2}I^{-2}\cdot M^{-1}L^{-3}T^3I^2\cdot T})^{-1}} = \mathrm{L}$ | ✓ |
| $\rho_a = \|Z\|^2/(\mu_0\omega)$ | MT apparent resistivity | $\mathrm{ML^3T^{-3}I^{-2}}$ | $\mathrm{M^2L^4T^{-6}I^{-4}/(MLT^{-2}I^{-2}\cdot T^{-1})} = \mathrm{ML^3T^{-3}I^{-2}}$ | ✓ |
| $Q = 2\pi E_{\text{stored}}/E_{\text{dissipated}}$ | Seismic quality factor | $1$ | $1$ | ✓ |

**Use this table as a template.** When you derive something new, add a row.
The act of writing the dimensions *is* the check.

## 3. Dimensionless groups that govern behaviour

These ratios, not the raw dimensional quantities, determine physical behaviour.
This is the single most useful consequence of dimensional analysis.

| Group | Definition | Compares | Governs |
|---|---|---|---|
| Reynolds $\mathrm{Re}$ | $\rho vL/\mu = vL/\nu$ | inertia / viscosity | laminar vs turbulent flow |
| Rayleigh $\mathrm{Ra}$ | $\alpha\rho g\Delta T L^3/(\kappa\eta)$ | buoyancy / diffusion | onset of thermal convection |
| Nusselt $\mathrm{Nu}$ | $qL/(k\Delta T)$ | convective / conductive heat transport | efficiency of convection |
| Prandtl $\mathrm{Pr}$ | $\nu/\kappa$ | momentum / thermal diffusivity | structure of convection |
| Péclet $\mathrm{Pe}$ | $vL/\kappa$ | advection / diffusion | whether transport is advective |
| Mach $\mathrm{Ma}$ | $v/c$ | flow / wave speed | compressibility effects |
| Froude $\mathrm{Fr}$ | $v/\sqrt{gL}$ | inertia / gravity | free-surface flows, tsunamis |
| Rossby $\mathrm{Ro}$ | $v/(fL)$ | inertia / Coriolis | geostrophic balance in oceans and atmosphere |
| Bond $\mathrm{Bo}$ | $\rho gL^2/\gamma$ | gravity / surface tension | droplet and bubble dynamics |
| Elasticity $\mathrm{E}$ (Euler number) | $p/(\rho v^2)$ | pressure / inertia | acoustic impedance matching |

**The three that matter most in this curriculum:**

- $\mathrm{Ra}$ — determines whether the mantle, a magma chamber, a
  hydrothermal system or a lake convects. Mantle $\mathrm{Ra}\sim10^{7}$, about
  $10^{4}$ times critical, so convection is inevitable. See
  [01-01-03 §3.4](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md).
- $\mathrm{Re}$ — determines whether flow in a fracture, conduit, or borehole is
  laminar (Darcy's law applies) or turbulent (it does not). Darcy's law requires
  $\mathrm{Re} \lesssim 1$–10 in porous media.
- $\mathrm{Pe}$ — determines whether heat or solute transport is dominated by
  advection or conduction. This decides whether you model a thermal problem with
  the diffusion equation or with an advection–diffusion equation.

## 4. The Buckingham Pi procedure

For a system with $n$ dimensional variables and $k$ independent base dimensions,
there are $n-k$ independent dimensionless groups.

**Procedure:**

1. List every variable that could matter, with its dimensions.
2. Count the independent base dimensions $k$.
3. Form $n-k$ dimensionless products by combining variables into power-law
   monomials.
4. Verify each product is genuinely dimensionless.
5. Interpret each group physically.

**Worked example (mantle convection).** Nine variables
($L$, $\Delta T$, $g$, $\rho$, $\alpha$, $\kappa$, $\eta$, $c_p$, $q$) in four
base dimensions ($\mathrm{M}$, $\mathrm{L}$, $\mathrm{T}$, $\Theta$) give
$9-4 = 5$ groups; two of them, $\mathrm{Ra}$ and $\mathrm{Nu}$, carry the
physics. The full treatment, including the caution that the scaling exponent
must be cited from the literature rather than assumed, is
[01-01-03 exercise ★★★9](../../01-mathematics/01-arithmetic/exercises/03-units-and-dimensional-analysis-solutions.md).

## 5. What dimensional analysis cannot do

| It cannot | Example | Remedy |
|---|---|---|
| Fix dimensionless constants | The factor 2 in $z/(2\sqrt{\kappa t})$ | Derive it, or measure it numerically |
| Detect unit errors within the same dimension | 24 mGal/km vs 2.4 Eötvös (both $\mathrm{T^{-2}}$) | Numerical comparison against known ranges |
| Check $\omega$ against $f$ | Radians are dimensionless | Track the factor $2\pi$ explicitly |
| Validate physical assumptions | A dimensionally consistent but physically wrong model | Compare with observation |
| Establish a numerical value | $\mathrm{Ra}$ gives the scaling, not the constant | Measure or look up |

**The practical rule:** dimensional analysis catches errors of *form*, not
errors of *magnitude* or *interpretation*. Use it always, but never as your only
check.

## 6. Common mistakes

1. **Adding different dimensions.** $1\ \mathrm{m} + 1\ \mathrm{s}$ is meaningless.
2. **Non-dimensionless exponential or logarithm arguments.** $\exp(x)$ requires $[x]=1$.
3. **Assuming a balanced equation is correct.** See Section 5.
4. **Forgetting that radians are dimensionless.** Which is why $\omega$ and $f$
   share dimensions and the $2\pi$ is invisible to checking.
5. **Confusing $\mathbf{B}$ and $\mathbf{H}$.** Different dimensions, and both
   appear in geomagnetism.
6. **Treating $\mathrm{M\,L^{-1}\,T^{-2}}$ as only "pressure".** It is also
   elastic stiffness, stress, energy density, and Young's modulus — all the same
   dimension, and this is physically meaningful.

## 7. Further reading

- **Bridgman, P. W. (1922). *Dimensional Analysis*. Yale University Press.**
  Level: intermediate, historical. The rigorous derivation of the Buckingham Pi
  theorem and the foundations of similitude.
- **Barenblatt, G. I. (1996). *Scaling, Self-similarity, and Intermediate
  Asymptotics*. Cambridge University Press.** Level: graduate. The modern
  treatment; explains why dimensional analysis works so well in problems with
  self-similar solutions — which includes a surprising amount of geophysics.
- **Bohren, C. F., & Huffman, D. R. (1983). *Absorption and Scattering of Light
  by Small Particles*. Wiley.** Level: advanced. Chapter 1 is an outstanding
  essay on the power of dimensional reasoning in physical argument.
- **Turcotte, D. L., & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Level: advanced undergraduate to graduate. Extensive use of
  dimensionless groups; the mantle convection chapters are the standard
  reference.
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).**
  Level: beginner to intermediate.

> Citation note: bibliography only; no copyrighted text reproduced. Confirm
> editions through your library.

## Related lessons

- [Symbol Handbook: Notation Used Throughout](./01-symbol-handbook.md)
- [Units Handbook, Conversions and Preferred Conventions](./02-units-handbook.md)
- [Physical Constants and Earth Parameters with Sources](./03-constant-handbook.md)
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
