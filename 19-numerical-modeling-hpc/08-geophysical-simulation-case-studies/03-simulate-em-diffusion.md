---
id: 19-08-03
title: "Simulating EM Diffusion in Conductive Media"
level: research
prereqs: ["19-07-01", "19-02-06", "19-07-03"]
tags: [numerical-modelling, verification, em-diffusion, magnetotellurics, diffusion, skin-depth]
---

# Simulating EM Diffusion in Conductive Media

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the quasi-static diffusion equation for the electric field in a
   conductor and the exact half-space impedance
   $Z = \sqrt{\mathrm{i}\omega\mu_0\rho}$ from it.
2. **Derive** the skin depth $\delta = 503.29\sqrt{\rho/f}$ m from $\mu_0$ and
   $\pi$, and **check** it against an independent computation.
3. **Verify** a time-domain diffusion solver against the exact error-function
   solution and **measure** its order in space and time.
4. **Verify** a layered frequency-domain solver against the exact recursion, and
   **state** why an independent implementation is the strongest available
   reference when no closed form exists.
5. **Measure** how the interface treatment changes the order of accuracy, and
   **state** the discretisation choice a benchmark must fix.
6. **Quantify** the conductance equivalence $S = \sigma h$ and **state** the
   periods at which two models with the same $S$ are distinguishable.

## Prerequisites

- [19-02-06 FD for Diffusion, Laplace and Poisson Problems](../02-finite-difference-methods/06-fd-diffusion-and-potential.md)
  — the discretisation of a diffusion operator.
- [19-07-01 Code Verification](../07-verification-validation-uncertainty/01-code-verification.md)
  and [19-07-03 Model Validation](../07-verification-validation-uncertainty/03-model-validation.md)
  — the discipline this lesson applies.
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md) — the
  acquisition context (helpful, not essential).

All models and data in this module are **SYNTHETIC**: chosen resistivities,
thicknesses and periods. The half-space impedance, the error-function solution and
the layered recursion are exact solutions of the stated equations; every other
number is printed by this lesson's demonstration.

## 1. Intuition: there is no wavefront

Electromagnetic fields in the Earth diffuse. In the quasi-static limit the
governing equation is a diffusion equation, not a wave equation, and the
difference is not cosmetic:

- **There is no arrival time.** A change in the source is felt, formally, at every
  depth immediately. What limits detection is amplitude, not travel time, and the
  "depth of investigation" is a detection threshold rather than a wavefront.
- **The response is a phase as well as an amplitude.** A diffusing field carries a
  phase lag, and the pair (apparent resistivity, phase) constrains the resistivity
  and its depth dependence jointly. Over a uniform half-space the phase is exactly
  $45^\circ$, so *any* deviation from $45^\circ$ is a statement about layering.
- **Conductance is what long periods measure.** Two layers with the same product
  $\sigma h$ look identical at long periods, so a sounding cannot separate a thin
  good conductor from a thick poor one without a short enough period — the
  equivalence the demonstration measures in Section 5.4.

The numerical consequences follow from the same structure. A diffusion solver is
unconditionally stable when implicit, is rarely limited by accuracy in time, and
its hardest requirement is resolving the *decaying* field with enough points per
skin depth. The verification tests are correspondingly straightforward: an exact
impedance for a half-space, an exact error function for a step in time, and an
exact recursion for layered models.

## 2. Definitions

**Quasi-static diffusion.** Neglecting displacement current,
$\nabla\times\mathbf{E} = -\mathrm{i}\omega\mu_0\mathbf{H}$ and
$\nabla\times\mathbf{H} = \sigma\mathbf{E}$ combine (for a 1-D layered Earth with
$E_y$ varying only with depth $z$) into $E'' = \mathrm{i}\omega\mu_0\sigma E$.

**Impedance.** $Z = E_y/H_x$ at the surface, from which the apparent resistivity is
$\rho_a = \lvert Z\rvert^{2}/(\omega\mu_0)$ and the phase is
$\arctan(\mathrm{Im}Z/\mathrm{Re}Z)$.

**Skin depth.** The e-folding depth of a diffusing field,
$\delta = \sqrt{2\rho/(\omega\mu_0)} = 503.29\sqrt{\rho/f}$ m for $\rho$ in
$\Omega$ m and $f$ in Hz.

**Conductance.** $S = \sigma h = h/\rho$, in siemens. The response of a thin layer
at long periods depends on $S$, not on $\sigma$ and $h$ separately.

**Verification by independent implementation.** Two algorithms that share no code
solving the same equations; if they agree to their measured discretisation errors,
both are likely right. The layered recursion and a finite-difference discretisation
are such a pair.

## 3. Derivations

### 3.1 From Maxwell to a diffusion equation

For a 1-D Earth with conductivity $\sigma(z)$ and $E_y(z)e^{\mathrm{i}\omega t}$,
Faraday's law gives $\mathrm{d}E_y/\mathrm{d}z = -\mathrm{i}\omega\mu_0 H_x$ and
Ampère's law gives $\mathrm{d}H_x/\mathrm{d}z = \sigma E_y$. Eliminating $H_x$:

$$\frac{\mathrm{d}^{2}E_y}{\mathrm{d}z^{2}} = \mathrm{i}\omega\mu_0\sigma E_y ,$$

a diffusion equation with a complex coefficient. Note the *sign* convention: the
solution that decays with depth is
$E_y \propto e^{-(1+\mathrm{i})z/\delta}$, and substituting it gives
$((1+\mathrm{i})/\delta)^{2} = 2\mathrm{i}/\delta^{2} = \mathrm{i}\omega\mu_0\sigma$
exactly when $\delta^{2} = 2/(\omega\mu_0\sigma)$ — the definition of $\delta$.

### 3.2 The exact half-space impedance and the constant 503.29

With $E_y = E_0e^{-(1+\mathrm{i})z/\delta}$,
$H_x = -E_y'/(\mathrm{i}\omega\mu_0)$ and therefore

$$Z = \frac{E_y(0)}{H_x(0)} = \frac{\mathrm{i}\omega\mu_0}{(1+\mathrm{i})/\delta}
= \sqrt{\mathrm{i}\omega\mu_0\rho},$$

from which $\lvert Z\rvert^{2} = \omega\mu_0\rho$ and
$\rho_a = \rho$ **exactly**, with phase $45^\circ$. The skin-depth constant follows
from $\delta = \sqrt{2/(\omega\mu_0\sigma)}$ with $\omega = 2\pi f$:

$$\delta = \sqrt{\frac{2\rho}{2\pi f\mu_0}} = \sqrt{\frac{\rho}{\pi f\mu_0}}
= \frac{1}{\sqrt{\pi\mu_0}}\sqrt{\frac{\rho}{f}} = 503.29\sqrt{\frac{\rho}{f}}\ \mathrm{m},$$

where $1/\sqrt{\pi\mu_0} = 503.29$ is a derived constant, not a remembered one.

### 3.3 The exact step response

In the time domain, with $D = 1/(\mu_0\sigma) = \rho/\mu_0$, a step in the surface
field $B(0,t) = B_0$ for $t>0$ produces

$$B(z,t) = B_0\,\mathrm{erfc}\!\left(\frac{z}{2\sqrt{Dt}}\right),$$

verified by substitution. This is the exact reference for a time-domain solver, and
it exhibits the "no wavefront" property: $\mathrm{erfc}$ is non-zero at every
$z>0$ for every $t>0$.

### 3.4 The layered recursion

For layers of resistivity $\rho_i$ and thickness $h_i$ over a half-space, define
$k_i = \sqrt{\mathrm{i}\omega\mu_0/\rho_i}$ and the intrinsic impedance
$\eta_i = \mathrm{i}\omega\mu_0/k_i$. Propagating upward from the half-space,

$$Z_N = \eta_N, \qquad
Z_i = \eta_i\,\frac{Z_{i+1} + \eta_i\tanh(k_i h_i)}
{\eta_i + Z_{i+1}\tanh(k_i h_i)} .$$

This is exact, and it is *algorithmically independent* of a finite-difference
discretisation — which is what makes it a strong verification reference.

## 4. Assumptions and regime of validity

1. **Quasi-static.** Displacement currents are neglected, valid for periods long
   compared with the dielectric relaxation time of the medium; at audio and radio
   frequencies in resistive media this must be checked.
2. **One-dimensional.** Lateral homogeneity. Any 2-D or 3-D structure invalidates
   the layered recursion and the 1-D solver together; verification against it then
   proves nothing about the code's ability to handle structure.
3. **Isotropic and non-polarisable.** Induced polarisation adds a frequency-
   dependent complex conductivity; the response is then not a diffusion response.
4. **The grid resolves the shortest skin depth in the model.** For the layered
   solver, the relevant resolution is $\delta_{\min}/\Delta z$, and the
   demonstration's measured errors quantify the consequence.
5. **Interface treatment stated.** Section 5.3 measures an order of accuracy lost
   to a conductivity sampled at a node that sits exactly on a layer boundary.
6. **What is not established.** Nothing here tests 3-D structure, anisotropy or
   galvanic distortion of the measured fields — the parts of the problem where
   real surveys go wrong.

## 5. Measured evidence

The demonstration `code/simulate_em_diffusion_demo.py` runs in about $0.3$ s.

### 5.1 Half-space response and the skin depth

Synthetic half-space with $\rho = 100$ $\Omega$ m:

| period (s) | $f$ (Hz) | $\delta$ (m) | $503.29\sqrt{\rho/f}$ (m) | $\rho_a$ ($\Omega$ m) | phase |
|---:|---:|---:|---:|---:|---:|
| 1 | 1.0000 | 5032.9 | 5032.9 | 100.0000 | 45.000 |
| 10 | 0.1000 | 15915.5 | 15915.4 | 100.0000 | 45.000 |
| 100 | 0.0100 | 50329.2 | 50329.0 | 100.0000 | 45.000 |
| 1000 | 0.0010 | 159154.9 | 159154.3 | 100.0000 | 45.000 |
| 10000 | 0.0001 | 503292.1 | 503290.0 | 100.0000 | 45.000 |

The apparent resistivity reproduces $\rho$ to machine precision and the phase is
$45.000^\circ$ at every period. For a uniform half-space the response carries
exactly one piece of information, the resistivity, which is why a *sounding* needs
many periods and why a layered inversion without them is underdetermined
([18-01-03 Null Space and Non-Uniqueness](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)).

### 5.2 The time-domain solver against the error function

$\rho = 100$ $\Omega$ m, so $D = \rho/\mu_0 = 7.9577\times10^{7}$ m$^{2}$s$^{-1}$;
comparison at $t = 0.01$ s, where the diffusion length is $\sqrt{Dt} = 892.1$ m,
against $B_0\,\mathrm{erfc}(z/(2\sqrt{Dt}))$:

| $\Delta z$ (m) | $\Delta t$ (s) | steps | max error | $L^{2}$ error | order |
|---:|---:|---:|---:|---:|---:|
| 100 | $2.513\times10^{-5}$ | 398 | $1.702\times10^{-4}$ | $6.494\times10^{-5}$ | — |
| 50 | $6.283\times10^{-6}$ | 1592 | $4.262\times10^{-5}$ | $1.629\times10^{-5}$ | 2.00 |
| 25 | $1.571\times10^{-6}$ | 6366 | $1.066\times10^{-5}$ | $4.078\times10^{-6}$ | 2.00 |

Crank-Nicolson with $\Delta t \propto \Delta z^{2}$ gives exactly second order, the
time error being two orders smaller than the space error by construction. Note the
absence of any wavefront in the reference and the solution alike: the field at
$892$ m is $48$ per cent of the surface value at $t = 0.01$ s, and the "depth of
investigation" is the depth at which that ratio falls below a stated detection
threshold.

### 5.3 A layered solver against the exact recursion

Two-layer model $\rho = [100, 10]$ $\Omega$ m, $h = [500]$ m; three-layer model
$\rho = [100, 10, 1000]$ $\Omega$ m, $h = [500, 5000]$ m; finite-difference grid
$\Delta z = 25$ m:

| period (s) | $\rho_a$ exact | $\rho_a$ FD | difference | phase exact | phase FD |
|---:|---:|---:|---:|---:|---:|
| 0.01 | 112.1555 | 111.3896 | −0.683% | 52.462 | 53.090 |
| 0.10 | 41.1989 | 40.1817 | −2.469% | 64.438 | 64.393 |
| 1.00 | 17.1777 | 16.9634 | −1.248% | 56.606 | 56.410 |
| 10.00 | 11.9457 | 11.8933 | −0.439% | 49.597 | 49.494 |
| 100.00 | 10.5814 | 10.5665 | −0.141% | 46.565 | 46.527 |
| 1000.00 | 10.1804 | 10.1759 | −0.045% | 45.507 | 45.494 |

The three-layer model behaves the same way (−0.683%, −2.469%, −1.244%, −0.399%,
$+0.016$%, $+0.025$%). Two implementations that share no code reproduce each
other to a fraction of a per cent over five decades of period: **this is the
strongest verification available for a layered code, and it is why the recursion is
worth writing even when a numerical solver exists.**

### 5.4 Why the layered solver converges at first order, not second

Same two-layer model at $T = 0.1$ s, refining $\Delta z$:

| $\Delta z$ (m) | boundary on a node? | relative error | order |
|---:|---|---:|---:|
| 200 | no | 2.0617% | — |
| 100 | yes | 9.4259% | −2.19 |
| 50 | yes | 4.8623% | 0.95 |
| 25 | yes | 2.4689% | 0.98 |

A layer boundary exactly on a node puts a jump in $E''$ there, and the three-point
stencil loses an order at that node: the measured order is $1$, not $2$, whenever
the boundary is node-aligned. The fix — placing boundaries on cell faces, or
solving the magnetic field in flux-conservative form, where the continuous quantity
is $\rho H'$ rather than $H'$ — is a *modelling choice* that a benchmark must fix
and a report must state. This is the same class of defect as the source
discretisation of [19-07-04](../07-verification-validation-uncertainty/04-benchmark-problems.md):
two consistent codes, different orders, and a comparison that cannot be interpreted
until the choice is stated.

### 5.5 Conductance equivalence

Two models over the same half-space ($\rho_2 = 1000$ $\Omega$ m) with the same
conductance: $\rho_1 = 100$ $\Omega$ m with $h_1 = 100$ m, and $\rho_1 = 50$
$\Omega$ m with $h_1 = 50$ m; both have $S = \sigma h = 1.0000$ S.

| period (s) | $\rho_a$ A | $\rho_a$ B | difference | phase difference |
|---:|---:|---:|---:|---:|
| 0.1 | 704.3758 | 690.7162 | −1.939% | 0.5645$^\circ$ |
| 1 | 893.3093 | 887.7251 | −0.625% | 0.1787$^\circ$ |
| 10 | 964.8764 | 962.9616 | −0.198% | 0.0568$^\circ$ |
| 100 | 988.7543 | 988.1332 | −0.063% | 0.0180$^\circ$ |
| 1000 | 996.4299 | 996.2320 | −0.020% | 0.0057$^\circ$ |
| 10000 | 998.8697 | 998.8069 | −0.006% | 0.0018$^\circ$ |

The two models are distinguishable at $0.1$ s (a $1.9$ per cent amplitude
difference and a $0.56^\circ$ phase difference) and indistinguishable at $10^4$ s.
**A model that reports a thin good conductor and one that reports a thick poor
conductor are the same statement until the periods are long enough to separate
them**, and the separation scale is the layer's own diffusion time.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| resistivity, conductivity | $\rho$, $\sigma$ | $\Omega$ m, S m$^{-1}$ | $\sigma = 1/\rho$ |
| angular frequency | $\omega$ | s$^{-1}$ | $2\pi f$ |
| impedance | $Z$ | $\Omega$ | $E_y/H_x$ |
| apparent resistivity | $\rho_a$ | $\Omega$ m | $\lvert Z\rvert^{2}/(\omega\mu_0)$ |
| phase | — | degrees | $\arctan(\mathrm{Im}Z/\mathrm{Re}Z)$ |
| skin depth | $\delta$ | m | $\sqrt{2\rho/(\omega\mu_0)}$ |
| diffusivity | $D$ | m$^{2}$s$^{-1}$ | $1/(\mu_0\sigma) = \rho/\mu_0$ |
| conductance | $S$ | S | $h/\rho$ |

Dimensional checks worth doing once: $\mu_0$ is H m$^{-1}$, so
$\omega\mu_0/\rho$ has units m$^{-2}$ as required for a diffusion term; and
$D = \rho/\mu_0$ has units $(\Omega\,\mathrm{m})/(\mathrm{H\,m^{-1}}) =
\mathrm{m^{2}s^{-1}}$ because $\Omega\,\mathrm{s^{-1}H^{-1}} = 1$.

## 7. Worked examples

### Example 1 — the skin depth two ways

For $\rho = 100$ $\Omega$ m at $f = 1$ Hz: $\omega = 6.2832$ s$^{-1}$,
$\omega\mu_0 = 7.8957\times10^{-6}$ $\Omega$ m$^{-1}$,

$$\delta = \sqrt{\frac{2\times100}{7.8957\times10^{-6}}}
= \sqrt{2.5330\times10^{7}} = 5032.9\ \mathrm{m},
\qquad 503.29\sqrt{\frac{100}{1}} = 5032.9\ \mathrm{m}.$$

The two agree to five figures, which is the demonstration's table.

### Example 2 — the diffusion length and the depth of investigation

With $\rho = 100$ $\Omega$ m, $D = 100/\mu_0 = 7.9577\times10^{7}$ m$^{2}$s$^{-1}$.
At $t = 0.01$ s, $\sqrt{Dt} = 892.1$ m, and the exact solution gives
$B/B_0 = \mathrm{erfc}(892/(2\times892.1)) = \mathrm{erfc}(0.5) = 0.4795$. So a
surface step is reduced to $48$ per cent at a depth equal to the diffusion length.
The e-folding depth is smaller: $\mathrm{erfc}(x) = 1/e = 0.3679$ at
$x \approx 0.634$ (since $\mathrm{erfc}(0.6) = 0.3961$ and
$\mathrm{erfc}(0.65) = 0.3580$), i.e. $z \approx 2\times892.1\times0.634
= 1130$ m for this time. **Quoting a
"depth of investigation" without stating the threshold and the time is quoting a
number without a meaning.**

### Example 3 — conductance equivalence, quantified

Model A: $h = 100$ m, $\sigma = 10^{-2}$ S m$^{-1}$ → $S = 1.0000$ S.
Model B: $h = 50$ m, $\sigma = 2\times10^{-2}$ S m$^{-1}$ → $S = 1.0000$ S.
At $T = 1$ s the responses differ by $0.625$ per cent in apparent resistivity and
$0.18^\circ$ in phase. To detect the difference at the $1$ per cent level one needs
$T \lesssim 0.2$ s, i.e. a period comparable to the layer's own diffusion time
$T \sim \mu_0\sigma h^{2} = 4\pi\times10^{-7}\times10^{-2}\times10^{4} = 0.126$ s
for model A. The rule is general: **equivalence holds for periods long compared
with the internal diffusion time of the layer.**

### Example 4 — a verification statement for a sounding code

> Verification: half-space impedance against the exact
> $Z = \sqrt{\mathrm{i}\omega\mu_0\rho}$, $\rho_a$ reproduced to machine precision
> and phase to $45.000^\circ$; time-domain solver against
> $B_0\mathrm{erfc}(z/(2\sqrt{Dt}))$, second order in $\Delta z$ with
> $\Delta t \propto \Delta z^{2}$ (measured orders $2.00$, $2.00$); layered solver
> against the exact recursion, agreement better than $2.5$ per cent at the shortest
> period and $0.05$ per cent at the longest, with a measured first-order
> convergence attributed to node-aligned layer boundaries. Not established: 3-D
> structure, anisotropy, induced polarisation, or that any of the layered models
> resembles the Earth.

## 8. Python demonstration

```bash
cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_em_diffusion_demo.py
```

Print-only, no file output, no network, exits 0.

## 9. Exercises

[`exercises/03-simulate-em-diffusion-exercises.md`](exercises/03-simulate-em-diffusion-exercises.md)
and
[`exercises/03-simulate-em-diffusion-solutions.md`](exercises/03-simulate-em-diffusion-solutions.md)
include deriving the skin depth, a period-range design exercise for a target
layer, and a critical review of a "depth of investigation" claim.

## 10. Applications

- **Magnetotellurics and controlled-source EM.** Both use layered or 3-D diffusion
  solvers; the 1-D recursion remains the reference for the simplest models and the
  most reliable benchmark ([09-electrical-em-methods](../../09-electrical-em-methods/README.md)).
- **Airborne EM.** The same physics with a moving source; the resolution limit is
  the same skin depth, and the same conductance equivalence applies
  ([11-05 Airborne Groundwater](../../11-exploration-geophysics/05-groundwater-exploration/README.md)).
- **Induction in the oceans and in icy moons.** The same equations with different
  conductivities and periods
  ([12-07-02 Icy Moons](../../12-global-geophysics-interior/07-planetary-interiors-comparative/02-icy-moons.md)).
- **Time-lapse monitoring.** Diffusion makes the response a low-pass filter in
  space and time, which sets what a monitoring survey can resolve.

## 11. Further study

- [19-02-06](../02-finite-difference-methods/06-fd-diffusion-and-potential.md) —
  the discretisation and its stability.
- [19-07-01](../07-verification-validation-uncertainty/01-code-verification.md) and
  [19-07-03](../07-verification-validation-uncertainty/03-model-validation.md).
- [18-inverse-problems](../../18-inverse-problems/README.md) — inverting soundings
  and the equivalence that limits them.
- [04-earth-science-geology](../../04-earth-science-geology/README.md) — what a
  conductivity structure means geologically.

## Mastery checkpoint

Without notes:

> A layered model has a $100$ m thick layer of resistivity $20$ $\Omega$ m over a
> $1000$ $\Omega$ m half-space. **(a)** Compute its conductance. **(b)** Compute the
> skin depth in the layer at $10$, $100$ and $1000$ s and state the periods at
> which the layer is "thin" and "thick" in the diffusion sense. **(c)** State two
> other layered models with the same response at the longest period, and the
> observation that would distinguish them. **(d)** If the layer boundary were placed
> exactly on a grid node with $\Delta z = 25$ m, state what the demonstration
> predicts about the convergence order of the finite-difference solution.

Worked answers appear in
[`exercises/03-simulate-em-diffusion-solutions.md`](exercises/03-simulate-em-diffusion-solutions.md).

## Common pitfalls

1. **Expecting an arrival time.** Diffusion has infinite propagation speed; what
   decays is amplitude, and the depth of investigation needs a stated threshold.
2. **Reporting a depth of investigation without the period.** The depth scales as
   $\sqrt{\rho/f}$, so the number is meaningless without both.
3. **Quoting $\rho_a$ and ignoring the phase.** The phase is what shows that the
   Earth is layered.
4. **Assuming a layered solver is verified by its own output.** The recursion is
   the independent check; the two must agree to the measured discretisation error.
5. **Node-aligned layer boundaries.** The demonstration measures a lost order of
   accuracy and a several-per-cent error at a working grid.
6. **Reading $S = \sigma h$ equivalence as universal.** It holds for periods long
   compared with the layer's internal diffusion time, and the demonstration
   measures where it breaks.

## Related modules

- [19-08 Geophysical Simulation Case Studies](README.md).
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md).
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md).
- [11-exploration-geophysics](../../11-exploration-geophysics/README.md).
- [18-inverse-problems](../../18-inverse-problems/README.md).

## Self-assessment checklist

- [ ] I can derive the diffusion equation, the impedance and the skin depth.
- [ ] I can state the constant 503.29 and derive it from $\mu_0$ and $\pi$.
- [ ] I can verify a time-domain solver against the error function and measure the
      order in space and time.
- [ ] I can explain the value of an independent implementation as a reference.
- [ ] I can explain the node-aligned interface defect and its consequence.
- [ ] I can compute a conductance and state when two models are distinguishable.
