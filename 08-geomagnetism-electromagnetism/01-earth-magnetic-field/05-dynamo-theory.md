---
id: 08-01-05
title: "The Geodynamo: Mechanism and Evidence"
level: research
prereqs: ["08-01-04", "02-07-04", "02-07-06", "08-01-03"]
tags: [geomagnetism, geodynamo, induction-equation, magnetic-reynolds-number, dynamo-theory, ohmic-dissipation]
---

# The Geodynamo: Mechanism and Evidence

The Earth's field is old, it is strong, and it reverses. None of those three
facts is compatible with a passive magnetised body: a field left to itself decays
by ohmic dissipation on a timescale far shorter than the age over which it is
observed. This lesson states that problem quantitatively, develops the induction
equation that any explanation must satisfy, exhibits a working (mean-field)
dynamo mechanism with its growth rates and its saturation, and prices the
energy budget. What it does **not** do is claim that a solution of the induction
equation is evidence about the Earth: the evidence is observational, and the
mechanism is a consistency argument.

**All models and data in this module are SYNTHETIC.** The core conductivity, size
scale, flow speed and dynamo numbers below are chosen teaching values. The only
standard constants used are $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ and
$a = 6371\ \mathrm{km}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the magnetic induction equation and identify its advective and
   diffusive terms.
2. **Compute** the magnetic diffusivity $\eta = 1/(\mu_0\sigma)$, the diffusion
   time $L^2/\eta$ and the free-decay time of a dipole mode, and state the
   resulting problem for the Earth.
3. **Compute** the magnetic Reynolds number and use it to decide which term of
   the induction equation dominates on a given scale.
4. **State** Cowling's theorem and the reason an axisymmetric field cannot be
   maintained, and show its consequence in a simple mean-field model.
5. **Derive** the growth condition $D = \alpha\omega/k^2 > 1$ of an
   $\alpha$–$\omega$ dynamo and compute growth rates on either side of it.
6. **Explain** saturation and why a linear dynamo is not a physical answer.
7. **Estimate** the magnetic energy and the ohmic dissipation of a synthetic
   core and compare them with the advection timescale.

## Prerequisites

- [08-01-04 Secular Variation, Jerks and Core Dynamics](04-secular-variation.md) —
  the observed timescales that constrain the mechanism.
- [02-07-04 Faraday's Law, Induction and Eddy Currents](../../02-physics/07-electromagnetism/04-em-induction.md)
  — induction in a moving conductor.
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
  — diffusion of a magnetic field, and $\eta$.
- [08-01-03 Spherical Harmonic Analysis of the Magnetic Field](03-spherical-harmonic-magnetic.md) —
  the modes whose decay is computed here.

## 1. The induction equation

In a conductor moving with velocity $\mathbf{u}$, Ohm's law in the moving frame
plus Faraday's law and Ampère's law combine into

$$\boxed{\;\frac{\partial \mathbf{B}}{\partial t}
= \nabla\times\left(\mathbf{u}\times\mathbf{B}\right)
+ \eta\nabla^{2}\mathbf{B}, \qquad
\eta = \frac{1}{\mu_0\sigma}.\;}$$

The two terms have names and units worth keeping separate:

| term | meaning | scales as |
|---|---|---|
| $\nabla\times(\mathbf{u}\times\mathbf{B})$ | **advection**: field carried and stretched by the flow | $UB/L$ |
| $\eta\nabla^2\mathbf{B}$ | **diffusion**: field destroyed by ohmic dissipation | $\eta B/L^2$ |

Their ratio is the **magnetic Reynolds number**

$$Rm = \frac{UB/L}{\eta B/L^2} = \frac{UL}{\eta}.$$

$Rm\gg1$ means advection wins and field lines are frozen into the fluid;
$Rm\ll1$ means the field leaks through the fluid and decays. Note the asymmetry:
advection can *amplify* field through stretching, while diffusion can only
destroy it. A self-sustaining field therefore needs the advective term to
out-produce the diffusive term indefinitely — and that is the dynamo problem.

### 1.1 Worked example — diffusivity, diffusion time, Reynolds number

With SYNTHETIC values $\sigma = 5.0\times10^{5}\ \mathrm{S\,m^{-1}}$,
$L = 2.10\times10^{6}\ \mathrm{m}$ and $U = 5.0\times10^{-4}\ \mathrm{m\,s^{-1}}$:

$$\eta = \frac{1}{\mu_0\sigma}
= \frac{1}{4\pi\times10^{-7}\times5.0\times10^{5}}
= 1.5915\ \mathrm{m^{2}\,s^{-1}},$$

$$\tau_{\text{diff}} = \frac{L^2}{\eta}
= \frac{(2.10\times10^{6})^2}{1.5915}
= 2.7709\times10^{12}\ \mathrm{s} = 8.7804\times10^{4}\ \mathrm{yr},$$

$$Rm = \frac{UL}{\eta}
= \frac{5.0\times10^{-4}\times2.10\times10^{6}}{1.5915} = 659.7.$$

The advection time is $L/U = 133.09\ \mathrm{yr}$, and
$\tau_{\text{diff}}/\tau_{\text{adv}} = Rm = 659.7$ consistently. The scale at
which advection and diffusion balance is
$l \sim \sqrt{\eta L/U} = 81.8\ \mathrm{km}$: below that scale the field
diffuses, above it the field is carried.

## 2. The free-decay problem

If $\mathbf{u} = 0$ the induction equation reduces to a diffusion equation, and
each spherical-harmonic mode decays at its own rate. For a sphere of radius $L$
the slowest decaying, degree-1 mode has rate $2\eta/L^2$, so its free-decay time
is $\tau_{\text{free}} = L^2/(2\eta) = 4.3902\times10^{4}\ \mathrm{yr}$ for the
parameters above. The demonstration integrates the decay:

| time (yr) | $|B|$ (nT) | % of initial |
|---|---|---|
| 0 | 300000.0 | 100.000 |
| 10000 | 267706.8 | 89.236 |
| 20000 | 238889.8 | 79.630 |
| 30000 | 213174.8 | 71.058 |
| 40000 | 190227.8 | 63.409 |
| 50000 | 169751.0 | 56.584 |

After $50\,000$ yr the field retains 56.6% of its strength. A field observed to
persist for intervals far longer than this free-decay time is evidence for
**continuous maintenance**, not for a fossil field. That is the observational
argument, and it is worth stating precisely: it is an argument by *comparison of
timescales*, and its strength depends entirely on $\sigma$ and $L$. A lower
conductivity shortens the decay time and strengthens the argument; a higher one
weakens it.

## 3. Why axisymmetry is not enough: Cowling's theorem

**Cowling's theorem.** A steady, axisymmetric magnetic field cannot be maintained
by a dynamo. The physics is a flux-conservation statement: in an axisymmetric
configuration the poloidal field lines close in meridional planes, and whatever
the axisymmetric flow does to them, it cannot produce a poloidal field from a
toroidal one. Concretely, if the flow has no non-axisymmetric part, then the
"regeneration" term that closes the loop between toroidal and poloidal fields
vanishes identically.

The demonstration makes this visible in the simplest possible mean-field model.
Write $P$ and $T$ for the amplitudes of the poloidal and toroidal fields, with
$k$ a diffusive decay rate, $\omega$ the shear (differential rotation) and
$\alpha$ the regeneration (helical flow):

$$\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix}P\\ T\end{pmatrix}
= \begin{pmatrix}-k & \alpha\\ \omega & -k\end{pmatrix}
\begin{pmatrix}P\\ T\end{pmatrix}.$$

The eigenvalues are $-k \pm \sqrt{\alpha\omega}$, so the field grows **if and only
if**

$$D \equiv \frac{\alpha\omega}{k^{2}} > 1.$$

Set either $\alpha = 0$ (no helicity) or $\omega = 0$ (no shear) and $D = 0$: the
system decays at rate $k$ whatever else is present. The demonstration's decay
rate is $k = 1/\tau_{\text{free}} = 2.2778\times10^{-5}\ \mathrm{yr^{-1}}$ and the
growth rates are

| $D$ | growth rate (yr⁻¹) | regime |
|---|---|---|
| 0.25 | $-1.1389\times10^{-5}$ | decay |
| 0.90 | $-1.1689\times10^{-6}$ | decay |
| 1.00 | $-3.4\times10^{-21}$ | marginal |
| 1.21 | $+2.2778\times10^{-6}$ | growth |
| 2.00 | $+9.4350\times10^{-6}$ | growth |
| 4.00 | $+2.2778\times10^{-5}$ | growth |

At $D = 1$ the growth rate is numerically zero (the eigenvalue is $0$ to
$10^{-21}$, which is round-off): that is the critical dynamo number, and it is a
genuine threshold. Note how slowly the field grows near criticality: at
$D = 1.21$ the e-folding time is $1/2.28\times10^{-6} = 4.4\times10^{5}$ yr,
comparable with the free-decay time. **A dynamo only just above criticality
cannot build a field in the age of the Earth**; a working dynamo must be
comfortably supercritical, which is a physical constraint on $\alpha$ and
$\omega$, not a mathematical one.

## 4. Saturation, and why a linear dynamo is unphysical

A linear dynamo grows without bound. Real dynamos do not, so the regeneration
must switch off as the field grows — through the Lorentz force, or through
buoyancy modification. The demonstration implements the simplest such
feedback, an $\alpha$-quenching $\alpha\to\alpha/(1+B^2/B_0^2)$ with
$B_0 = 10^{-2}$ in the same units as the amplitudes, and integrates:

| time (yr) | poloidal | toroidal | $\sqrt{P^2+T^2}$ |
|---|---|---|---|
| 0 | $9.9544\times10^{-4}$ | $6.4426\times10^{-6}$ | $9.9547\times10^{-4}$ |
| 2000 | $9.5319\times10^{-4}$ | $6.7748\times10^{-5}$ | $9.5559\times10^{-4}$ |
| 10000 | $8.3457\times10^{-4}$ | $2.6596\times10^{-4}$ | $8.7593\times10^{-4}$ |
| 40000 | $7.8070\times10^{-4}$ | $6.7483\times10^{-4}$ | $1.0319\times10^{-3}$ |
| 200000 | $2.7682\times10^{-3}$ | $2.9433\times10^{-3}$ | $4.0405\times10^{-3}$ |
| 799800 | $5.7712\times10^{-3}$ | $8.1576\times10^{-3}$ | $9.9926\times10^{-3}$ |

The amplitude grows from a seed at $10^{-4}$ and saturates at
$10^{-2} = B_0$ by construction, with the toroidal component eventually
dominating the poloidal — the reverse of the seed. Three lessons:

1. **Saturation is a feedback, and its form is a modelling choice.** Different
   quenching laws saturate at different amplitudes with different ratios of
   toroidal to poloidal field. The saturated state is not a prediction of the
   equations; it is a prediction of the equations *plus* the closure.
2. **The ratio $T/P$ is diagnostic.** It is observable in principle (a strong
   toroidal field is invisible at the surface) and is a standard test of dynamo
   models.
3. **Saturation takes many e-folding times.** The chain above is still rising at
   $8\times10^{5}$ yr, which is the point of §3: a near-critical dynamo is slow.

## 5. The energy budget

For a synthetic core of radius $L = 2.10\times10^{6}\ \mathrm{m}$ and typical
field $B = 3.0\times10^{-4}\ \mathrm{T}$:

$$V = \tfrac{4}{3}\pi L^{3} = 3.879\times10^{19}\ \mathrm{m^{3}}, \qquad
\frac{B^{2}}{2\mu_0} = 3.581\times10^{-2}\ \mathrm{J\,m^{-3}},$$

$$E_{\text{mag}} = 3.581\times10^{-2}\times3.879\times10^{19}
= 1.389\times10^{18}\ \mathrm{J} = 1.389\times10^{6}\ \mathrm{TJ}.$$

The characteristic current density and the ohmic dissipation follow from
$J \sim B/(\mu_0 L)$ and $P = J^2/\sigma \times V$:

$$J = \frac{B}{\mu_0 L} = 1.137\times10^{-4}\ \mathrm{A\,m^{-2}}, \qquad
P_{\text{ohm}} = \frac{J^{2}}{\sigma}V = 1.003\times10^{6}\ \mathrm{W},$$

$$E_{\text{mag}}/P_{\text{ohm}} = 4.390\times10^{4}\ \mathrm{yr}
= \tau_{\text{free}}.$$

The exact agreement with $\tau_{\text{free}}$ is not a coincidence: the ratio
$B^{2}/(2\mu_0)\big/\left[B^{2}/(\mu_0^{2}L^{2}\sigma)\right]$ is
$\tfrac{1}{2}\mu_0\sigma L^{2} = L^{2}/(2\eta)$, which is the same quantity by
construction. It is a **consistency check on the algebra**, not independent
evidence — a point worth stating because the coincidence is easy to present as a
result.

What the budget does buy is a scale: the dissipation is of order a megawatt for
these parameters, and any mechanism must supply it from the same energy source
that drives the flow. That is the form in which the dynamo problem couples to
core thermodynamics and to the global heat budget
([12-03-02 Global Heat Flow and Its Distribution](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md)).

## 6. Evidence, and what kind of evidence it is

Collect the strands, explicitly labelled:

| statement | status |
|---|---|
| The field exists and changes on $10^{2}$–$10^{3}$ yr timescales | **observation** (§1.1 of [08-01-04](04-secular-variation.md)) |
| A passive field would decay in $\sim10^{4}$ yr | **calculation** from $\eta$ and $L$, sensitively dependent on both |
| The field is therefore maintained | **inference** from the timescale comparison |
| The maintenance requires advection, not diffusion | **inference** from $Rm \gg 1$ |
| The dynamo must be non-axisymmetric (Cowling) | **theorem**, given the assumptions |
| The mechanism is $\alpha$–$\omega$ with quenching | **model**, not observation |
| A numerical dynamo reproduces the observed spectrum | **consistency**, not proof |

The honest summary is that the geodynamo is the only mechanism known to be
*possible* given the constraints, and that its quantitative predictions are still
model-dependent. See
[12-04-02 Numerical Geodynamo Models](../../12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md)
for what three-dimensional simulations add and where they remain ambiguous.

## 7. Assumptions and regime of validity

1. **A single scale $L$ and a single $U$.** Real core flow is a spectrum, and
   $Rm$ is scale-dependent: a flow can be advective at large scales and diffusive
   at small ones in the same fluid.
2. **$\sigma$ is known.** Every timescale here is proportional to $\sigma$.
   Conductivity is the single most influential and least certain input.
3. **Uniform $\eta$.** $\eta$ depends on temperature and composition, both of
   which vary in the core.
4. **Mean-field closure.** The $\alpha$–$\omega$ model replaces a turbulent,
   three-dimensional flow by two coefficients. It is a closure, and its
   parameters are not measured.
5. **Boussinesq-like kinematics.** The demonstration's amplitudes are not a
   solution of the magnetohydrodynamic equations; they are a toy that exhibits
   the threshold, the growth and the saturation.
6. **Synthetic parameters.** Nothing here is the Earth's conductivity, size,
   speed or field strength. The qualitative conclusions are robust to the
   numbers; the numbers are not conclusions about the Earth.

## 8. Python demonstration

`code/dynamo_theory_demo.py` prints, with units:

1. $\eta$ from $\sigma$, the diffusion time and the free-decay time;
2. $Rm$, the advection time, and the balance scale $\sqrt{\eta L/U}$;
3. an integration of the free-decay law over $50\,000$ yr;
4. the $\alpha$–$\omega$ eigenvalues, the critical dynamo number and the growth
   rates on both sides of it;
5. a time integration with $\alpha$-quenching, showing growth to saturation;
6. the magnetic energy, current density, ohmic dissipation and their ratio;
7. exact spectral advection and diffusion operators from the same initial
   pattern, showing that one preserves amplitude while the other destroys it.

Exercises and solutions:
[`exercises/05-dynamo-theory-exercises.md`](./exercises/05-dynamo-theory-exercises.md),
[`exercises/05-dynamo-theory-solutions.md`](./exercises/05-dynamo-theory-solutions.md).

## Mastery checkpoint

1. Derive $\eta = 1/(\mu_0\sigma)$ from the diffusion term of the induction
   equation, and state its unit.
2. Compute $Rm$ for $U = 10^{-3}\ \mathrm{m\,s^{-1}}$, $L = 2\times10^{6}\
   \mathrm{m}$, $\sigma = 10^{5}\ \mathrm{S\,m^{-1}}$ and state which term of the
   induction equation dominates.
3. Show that the eigenvalues of the two-by-two mean-field system are
   $-k\pm\sqrt{\alpha\omega}$, and give the critical condition.
4. Explain in two sentences why a linear dynamo cannot describe the Earth.
5. Compute the magnetic energy of a $2\times10^{6}$ m sphere with
   $B = 5\times10^{-4}\ \mathrm{T}$.
6. State which of the six rows of §6 are observations and which are inferences.

## Common pitfalls

1. **Citing Cowling's theorem as "the dynamo is impossible".** It rules out a
   class of solutions, not dynamos.
2. **Treating $\eta$ as a measured constant.** It is a derived quantity and it
   is uncertain by a large factor.
3. **Forgetting the $(n+1)$-like geometric factors.** The free-decay rate is
   $n(n+1)\eta/L^{2}$ for degree $n$, not $\eta/L^{2}$.
4. **Reporting a numerical dynamo's saturation amplitude as a prediction.**
   Section 4 is the reason it is not.
5. **Mixing advection and diffusion times.** Their ratio *is* $Rm$; using one
   while claiming the other is a bookkeeping error.
6. **Presenting the energy/dissipation ratio as independent confirmation.**
   Section 5 shows it is an identity.

## Related modules

- [08-01-04 Secular Variation, Jerks and Core Dynamics](04-secular-variation.md) —
  the observations that set the timescale.
- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](06-palaeomagnetism.md) —
  the field's behaviour over geological time, including reversals.
- [12-04-02 Numerical Geodynamo Models](../../12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md) —
  full magnetohydrodynamic simulations.
- [12-03-02 Global Heat Flow and Its Distribution](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md) —
  where the power comes from.
- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  the conductivity that sets every number here.

## Self-assessment checklist

- [ ] I can derive the induction equation and name both terms.
- [ ] I can compute $\eta$, the diffusion time and the free-decay time.
- [ ] I can compute $Rm$ and interpret it.
- [ ] I can state Cowling's theorem and demonstrate its consequence in a toy
      model.
- [ ] I can derive and evaluate the critical dynamo number.
- [ ] I can explain saturation and price the energy budget.
