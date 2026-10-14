---
id: 02-11-02
title: "Equations of State and High-Pressure Mineral Physics"
level: doctoral
prereqs: ["02-11-01", "02-05-07", "01-05-04"]
estimated_minutes: 90
tags: [equation-of-state, birch-murnaghan, adams-williamson, gruneisen-parameter]
---

# Equations of State and High-Pressure Mineral Physics

Lesson [01](./01-pressure-density-depth.md) took the density profile as given and
integrated hydrostatic balance over it. This lesson asks the question that the
previous one deferred: *where does $\rho(P,T)$ come from?* The answer is an
equation of state, and the equation of state is the bridge between a laboratory
measurement made on a microscopic crystal and a density at 360 GPa that no
laboratory can reach in a volume of Earth-sized extent.

There are three ideas in this lesson, and they build on each other.

**The equation of state itself.** The Birch–Murnaghan form is the workhorse. It
expands the elastic energy of a crystal in the Eulerian finite strain, keeps
terms to second or third order, and yields $P(V)$ with two parameters: the
zero-pressure bulk modulus $K_0$ and its pressure derivative $K_0'$. It is a
*model*, not a law, and §6 says exactly when it fails.

**The seismic parameter, which turns seismology into an equation of state.**
$$\phi \equiv v_p^2 - \tfrac{4}{3}v_s^2 = \frac{K}{\rho}.$$
This one combination of the two observable seismic velocities equals $K/\rho$,
and $K/\rho = \mathrm{d}P/\mathrm{d}\rho$ for adiabatic compression. That identity
— not any correlation between velocity and density — is what allows a seismogram
to constrain composition. §3 derives the resulting **Adams–Williamson** relation and
explains both what it proves and what it assumes.

**The thermal equation of state.** Pressure, volume and temperature cannot be
separated in the deep Earth. The thermal pressure at the core–mantle boundary is
tens of gigapascals against a total of 135 GPa, and the adiabatic temperature
gradient is a few tenths of a kelvin per kilometre in the mantle and near one
kelvin per kilometre in the core. §4 derives both and computes them.

The three together are the entire methodological content of deep-Earth mineral
physics, and the last section of each is a statement of what the method cannot
do.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what an equation of state must supply and why a single $P(V)$ curve
   at 300 K is not it.
2. **Write** the Birch–Murnaghan equation of state to second and third order,
   explain what the Eulerian strain variable is, and derive the second-order form.
3. **Show** that the third-order term is proportional to $K_0'-4$ and vanishes
   identically when $K_0' = 4$, and explain why that is not an accident.
4. **Invert** the equation of state for $V$ at a given $P$ and verify the
   inversion by round-tripping.
5. **Derive** $\phi = v_p^2 - \tfrac{4}{3}v_s^2 = K/\rho$ and the
   Adams–Williamson relation $\mathrm{d}\rho/\mathrm{d}z = \rho g/\phi$, and
   state the two physical assumptions they carry.
6. **Derive** the adiabatic temperature gradient
   $(\mathrm{d}T/\mathrm{d}z)_s = \gamma gT/\phi$ from
   $(\mathrm{d}T/\mathrm{d}P)_S = \gamma T/K$, and integrate it to obtain a mantle
   and core adiabat.
7. **Estimate** the thermal pressure $\alpha K\,\Delta T$ at depth and compare it
   with the total pressure.
8. **Explain** why an isothermal, single-phase equation of state under-predicts
   the pressure required to reach the core–mantle-boundary density, and identify
   both missing terms.

## Prerequisites

- [02-11-01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the hydrostatic integration this lesson supplies the density for, and the
  reference-model numbers reused throughout.
- [02-05-07 Thermodynamic Phase Equilibria and Mantle Mineralogy](../05-thermodynamics/07-phase-equilibria.md)
  — the Clapeyron relation, and why the mantle has phase changes at all.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../../01-mathematics/05-single-variable-calculus/04-taylor-series.md)
  — the expansion that generates the finite-strain equation of state, and the
  Newton-type iteration used to invert it.

## 1. What an equation of state has to do

An equation of state is a relation $F(P,V,T) = 0$ for a material. Three
specialisations are used constantly:

- the **isothermal** equation of state $P(V)$ at a reference temperature,
  measured in a diamond-anvil cell or a shock experiment;
- the **adiabatic** equation of state along an isentrope, which is what a
  convecting layer follows;
- the **full** $P(V,T)$ surface, which requires the thermal pressure as well.

Deep-Earth work translates between them. A mineral physicist measures $P(V)$ at
300 K up to maybe 200 GPa and adds a thermal term calibrated separately. A
geophysicist then asks whether some assemblage, at the model's $(P,T)$ at a given
depth, predicts the model's $\rho$, $v_p$ and $v_s$. If it does, the assemblage is
admissible; if it does not, either the assemblage or the model is wrong.

The key structural fact is that $P(V,T)$ is a three-dimensional surface and any
single experiment explores a one-dimensional path through it. This is why mineral
physics is a field of *constraints* rather than measurements, and why the
equations of state in this lesson are chosen for the behaviour of their
derivatives rather than for the elegance of their algebra.

## 2. The Birch–Murnaghan equation of state

### 2.1 Eulerian finite strain

Let the material be compressed from a reference volume $V_0$ to $V$. The
linear compression in each direction is $(V/V_0)^{1/3}$, and the straightforward
measure of strain would be $1-(V/V_0)^{1/3}$. That measure is *Lagrangian*: it
describes the deformation with reference to the undeformed state, and it
outperforms well under tension. Birch used the *Eulerian* measure, referenced to
the deformed state,

$$f = \frac{1}{2}\left[\left(\frac{V_0}{V}\right)^{2/3} - 1\right], \qquad (1)$$

because the elastic energy of a crystal under great compression is more naturally
expressed in the deformed coordinates. Expanding the elastic energy in $f$ to
third order and differentiating with respect to volume gives the pressure.

### 2.2 Second order

Keeping the energy to second order in $f$ gives the **second-order**
Birch–Murnaghan equation,

$$P_2 = \frac{3}{2}K_0\left(x^7 - x^5\right), \qquad
x \equiv \left(\frac{V_0}{V}\right)^{1/3}. \qquad (2)$$

Where does that expression come from? The second-order expansion gives
$P = 3K_0f(1+2f)^{5/2}$, and the substitution
$1+2f = (V_0/V)^{2/3} = x^2$ makes the two forms identical. It is worth checking
at $V = V_0$: then $f = 0$ and $P = 0$ ✓. And the derivative checks too:

$$\left.\frac{\mathrm{d}P}{\mathrm{d}V}\right|_{V_0}
= -\frac{3}{2}K_0\left.\frac{\mathrm{d}}{\mathrm{d}V}(x^7-x^5)\right|_{V_0}
= -\frac{K_0}{V_0},$$

because $K_0 \equiv -V\left.\mathrm{d}P/\mathrm{d}V\right|_{V_0}$ — which is the
definition of the bulk modulus. Any candidate equation of state must reproduce
that, and equation (2) does.

### 2.3 Third order, and why $K_0' = 4$ is special

Keeping one more term gives the **third-order** form actually used in practice,

$$P_3 = \frac{3}{2}K_0\left(x^7-x^5\right)
\left[1 + \tfrac{3}{4}\left(K_0'-4\right)\left(x^2-1\right)\right],
\qquad K_0' \equiv \left.\frac{\mathrm{d}K}{\mathrm{d}P}\right|_{P=0}. \qquad (3)$$

The correction factor is *linear in $K_0'-4$*. When $K_0' = 4$ the two forms
coincide **exactly**, not approximately:

```text
  K0 (GPa)  K0_prime   V/V0        P2        P3       P3-P2
     160.0       4.0   0.95      9.09      9.09   0.000e+00
     160.0       4.0   0.85     36.01     36.01   0.000e+00
     160.0       4.5   0.85     36.01     37.55   1.545e+00
     160.0       5.0   0.85     36.01     39.10   3.090e+00
     260.0       4.0   0.85     58.51     58.51   0.000e+00
```

The difference is $0.000\times10^0$ at $K_0'=4$ and grows linearly with
$K_0'-4$ at fixed compression: 0.155 GPa per unit of $K_0'$ at $V/V_0 = 0.85$
with $K_0 = 160$ GPa. This is not a numerical accident. The third-order term is
the next term in the strain expansion, and its coefficient is fixed by demanding
that the *derivative* of the resulting $P(V)$ reproduce the measured $K_0'$.
At $K_0'=4$ that demand is satisfied by the second-order form itself, so the
third-order term has nothing left to do.

The practical consequence: for most mantle minerals $K_0'$ lies between 3.9 and
4.2, so the second-order form is an excellent approximation over moderate
compression, and quoting $K_0'$ matters mainly where it departs from 4 — which is
precisely the case of iron, with $K_0'\approx5$. That is why the parameter matters
for the core and can often be set to 4 for the mantle.

### 2.4 The curve, evaluated

With the nominal, illustrative parameters in the table below — **rounded
literature anchors quoted to two significant figures, not measured constants, and
listed only to show the functional form** — equation (3) gives:

| $V/V_0$ | $\rho/\rho_0$ | Forsterite (128 GPa, 4.2) | Periclase (160, 4.0) | Bridgmanite (260, 4.0) | hcp Fe (165, 5.0) |
|---|---|---|---|---|---|
| 1.00 | 1.000 | 0.0 | 0.0 | 0.0 | 0.0 |
| 0.95 | 1.053 | 7.3 | 9.1 | 14.8 | 9.6 |
| 0.90 | 1.111 | 16.8 | 20.8 | 33.8 | 22.6 |
| 0.85 | 1.176 | 29.3 | 36.0 | 58.5 | 40.3 |
| 0.80 | 1.250 | 45.7 | 55.8 | 90.7 | 64.5 |
| 0.70 | 1.429 | 97.2 | 116.7 | 189.7 | 144.6 |

(Pressures in GPa; $K_0$ and $K_0'$ in the column headings.)

Two features matter. **Pressure is strongly nonlinear in volume**: compressing
from 0.95 to 0.80 — a further 18 per cent of volume — multiplies the pressure by
6.3 for periclase, because $K$ itself grows as the material is squeezed.
**Bridgmanite is much stiffer than forsterite**: at the same compression it
requires 2.5 times the pressure. That single fact is why the 660 km discontinuity
is a major structural boundary and the 410 km one a lesser one.

## 3. The seismic parameter and Adams–Williamson

### 3.1 Defining $\phi$

For an isotropic elastic solid, the two body-wave speeds are

$$v_p = \sqrt{\frac{K+\tfrac{4}{3}\mu}{\rho}}, \qquad
v_s = \sqrt{\frac{\mu}{\rho}}. \qquad (4)$$

Form the combination that removes the shear modulus:

$$v_p^2 - \tfrac{4}{3}v_s^2
= \frac{K+\tfrac{4}{3}\mu}{\rho} - \frac{\tfrac{4}{3}\mu}{\rho}
= \frac{K}{\rho} \equiv \phi. \qquad (5)$$

This is an *identity*, not an approximation. It holds for any isotropic elastic
material, whatever its mineralogy. And $K/\rho$ is, up to a factor, the inverse of
the compressibility per unit mass — the quantity that appears whenever pressure
is converted to density.

The value of $\phi$ across the reference model, computed from the handbook's
rounded velocity ranges (lesson [01](./01-pressure-density-depth.md) §3.3), spans
a factor of nearly 6:

| Region | $\phi$ (km² s⁻²) | $K = \rho\phi$ (GPa) |
|---|---|---|
| Crust | 20.0 | 52 |
| Upper mantle | 38.6 | 127 |
| Transition zone (top → base) | 49.5 → 64.3 | 178 → 283 |
| Lower mantle (base) | 116.6 | 650 |
| Outer core (top) | 64.0 | 634 |
| Inner core (top → centre) | 104.7 → 109.4 | 1340 → 1434 |

Note the *discontinuity in the wrong direction*: $\phi$ rises to 116.6 km² s⁻² at
the base of the mantle and then **drops** to 64.0 km² s⁻² just inside the outer
core. This is the CMB signature of lesson [01](./01-pressure-density-depth.md) §4,
now expressed in the quantity that controls the density gradient.

### 3.2 Deriving Adams–Williamson

Suppose a layer is chemically homogeneous and is compressed adiabatically. Then
the density is a function of pressure alone along that path, and

$$\frac{\mathrm{d}\rho}{\mathrm{d}P} = \frac{\rho}{K} = \frac{1}{\phi}, \qquad (6)$$

because for a fixed composition $\mathrm{d}\rho/\rho = \mathrm{d}P/K$ from the
definition of $K$. Combine equation (6) with hydrostatic balance (lesson
[01](./01-pressure-density-depth.md) equation (1)) written in terms of depth $z$
increasing downward, $\mathrm{d}P/\mathrm{d}z = \rho g$:

$$\frac{\mathrm{d}\rho}{\mathrm{d}z}
= \frac{\mathrm{d}\rho}{\mathrm{d}P}\frac{\mathrm{d}P}{\mathrm{d}z}
= \frac{\rho\,g}{\phi}. \qquad (7)$$

That is the **Adams–Williamson equation**. Its content is a claim of the form
"if the layer is homogeneous and adiabatic, then the density gradient is
$\rho g/\phi$, and $\phi$ is seismologically observable". Its use is the
contrapositive:

> Integrate equation (7) downward with the observed $\phi(z)$ and $g(z)$. If the
> result matches the density that free oscillations require, the layer is
> homogeneous and adiabatic. If it does not, the mismatch measures the
> compositional and thermal contribution.

This is how the CMB was recognised as a compositional boundary long before any
laboratory work on iron. Integrating an adiabatic, homogeneous mantle across the
CMB cannot produce a factor-of-1.78 density jump at essentially fixed pressure;
the observed density therefore demands a different material, and the observed
$\phi$ drop tells you what kind. Lesson [01](./01-pressure-density-depth.md) §4.3
shows the local version of the argument as a table of ratios, and the outer core
comes out at 1.00 — which is the modern confirmation of the idea that the outer
core *is* homogeneous and adiabatic, once you are inside it.

### 3.3 What the seismic equation of state is *not*

Three cautions, because this method is easy to misuse.

**It is not a velocity–density correlation.** "Faster rocks are denser" is a
rule of thumb in the crust and a coincidence elsewhere. What makes composition
inference possible is equation (5) plus equation (6), which are exact and
conditional. Lesson [03](./03-seismic-parameter-relations.md) §4 demonstrates
empirically how badly the correlation version fails when extrapolated across the
CMB.

**It does not determine $\rho$ pointwise from $\phi$ alone.** Equation (7) is a
differential equation: it needs a starting density $(\rho_0, P_0)$ at the top of
the interval, and it integrates any error downward. That is why lesson
[01](./01-pressure-density-depth.md) §3.4's moment-of-inertia constraint matters —
it is the absolute anchor that the differential relation lacks.

**It assumes homogeneity, which is what you are trying to test.** The transition
zone is exactly the case where the assumption fails (ratio 0.22 in lesson
[01](./01-pressure-density-depth.md) §4.3), and the failure is not a defect of the
method but its diagnostic output.

## 4. The thermal equation of state

### 4.1 Why an isothermal equation of state is not enough

A completely explicit demonstration that the isothermal description fails is worth
carrying out in full, because it sets the scale for everything else. Take the top
of the lower mantle from lesson [01](./01-pressure-density-depth.md) as the
reference state: $\rho_0 = 4400$ kg m⁻³, $K_0 = 283$ GPa (from $\rho\phi$ with the
handbook velocities), $K_0' = 4$. Compress that material isothermally to the
CMB density of 5570 kg m⁻³, so $V/V_0 = 4400/5570 = 0.7899$. Equation (3) gives

$$P_{\text{EOS}} = 107.0\ \text{GPa}
\qquad\text{against}\qquad
P_{\text{hydrostatic}} = 134.6\ \text{GPa}.$$

The isothermal, single-phase equation of state **under-predicts the pressure by
20 per cent.** Two physical terms are missing, and both push the required
pressure up:

- **Temperature.** The real lower mantle is hotter at depth, and a hotter
  material is *less* dense at a given pressure. So more pressure is needed to
  reach the same density. §4.4 quantifies this.
- **Phase change.** Bridgmanite is denser than the ringwoodite it replaces at
  660 km, so some of the density increase at depth is mineralogical rather than
  compressional and requires no pressure at all. Excluding it from the reference
  state inflates the apparent compression needed.

The measured 20 per cent is the size of the error you make by extrapolating a
room-temperature, single-phase equation of state across 2000 km of mantle. It is
larger than most of the effects one wants to resolve, which is why every serious
mantle model carries a thermal term.

### 4.2 The Grüneisen parameter

The parameter that connects the thermal and elastic descriptions is the
Grüneisen parameter,

$$\gamma \equiv \frac{\alpha K_T}{\rho\,c_V} \approx \frac{\alpha K_S}{\rho\,c_p}, \qquad (8)$$

with $\alpha$ the volumetric thermal expansion coefficient and $c_V$, $c_p$ the
specific heats. Physically, $\gamma$ measures how much the vibrational frequencies
of the lattice change when the volume changes; it is of order 1 to 2 for mantle
minerals and close to 1.5 for the core. Its near-constancy under compression —
$\gamma\rho \approx$ constant, the *quasi-harmonic* approximation — is what makes
a simple thermal equation of state usable:

$$P(V,T) \approx P(V,T_{\text{ref}}) + \alpha K\,(T - T_{\text{ref}}).
\qquad (9)$$

### 4.3 Deriving the adiabatic gradient

The gradient along an isentrope follows from the entropy differential. With
$S = S(T,P)$,

$$\mathrm{d}S = \frac{c_p}{T}\,\mathrm{d}T - \alpha V\,\mathrm{d}P.$$

Setting $\mathrm{d}S = 0$ for an adiabatic (isentropic) path,

$$\left(\frac{\mathrm{d}T}{\mathrm{d}P}\right)_S
= \frac{\alpha T V}{c_p} = \frac{\alpha T}{\rho c_p}. \qquad (10)$$

Substituting the Grüneisen definition (8) turns this into
$(\mathrm{d}T/\mathrm{d}P)_S = \gamma T/K$, and multiplying by
$\mathrm{d}P/\mathrm{d}z = \rho g$ gives the **adiabatic temperature gradient in
depth**:

$$\left(\frac{\mathrm{d}T}{\mathrm{d}z}\right)_S
= \frac{\gamma\,g\,T}{K/\rho} = \frac{\gamma\,g\,T}{\phi}.
\qquad (11)$$

Notice that this is structurally the *same* relation as Adams–Williamson, equation
(7): both are $\gamma$-weighted or unweighted ratios of $gT$ or $g\rho$ to $\phi$.
That is not a coincidence. Both describe an isentropic, self-compressed column,
one tracking density and the other temperature, and $\phi = K/\rho$ is the single
quantity that controls both.

### 4.4 The adiabat, integrated

Equation (11) is computed and then integrated. Using $\gamma = 1.5$ (nominal),
the reference model's $\rho$, $g$ and $\phi$, and one anchor temperature of
1900 K at 660 km:

| Depth (km) | Region | $\rho$ | $g$ | $\phi$ (m²/s²) | $T$ (K) | $\mathrm{d}T/\mathrm{d}z$ (K/km) |
|---|---|---|---|---|---|---|
| 660 | lower mantle top | 4400 | 9.947 | $6.428\times10^7$ | 1900 | 0.441 |
| 1000 | lower mantle | 4578 | 9.883 | $7.126\times10^7$ | 2050 | 0.426 |
| 2000 | lower mantle | 5103 | 9.882 | $9.388\times10^7$ | 2476 | 0.391 |
| 2891 | just above CMB | 5570 | 10.510 | $1.166\times10^8$ | 2825 | 0.382 |
| 2891 | just below CMB | 9900 | 10.510 | $6.400\times10^7$ | 2825 | 0.696 |
| 4000 | outer core | 11028 | 7.745 | $8.331\times10^7$ | 3596 | 0.502 |
| 5153 | inner-core boundary | 12166 | 4.387 | $1.047\times10^8$ | 4175 | 0.262 |

Read three things.

**The mantle adiabat is 0.4 K/km, not 0.3 or 30.** A few tenths of a kelvin per
kilometre across 2200 km of mantle gives about 925 K of adiabatic heating — the
same order as the temperature difference between the top and bottom of the mantle.
This is the number that a geotherm has to exceed for convection to occur
([02-06-06](../06-fluid-mechanics/06-mantle-convection.md)).

**The gradient doubles at the CMB, discontinuously.** From 0.382 to 0.696 K/km.
The physics is entirely in the denominator: $gT$ is continuous ($g$ and $T$ are
both continuous at the CMB, unlike $\rho$ and $v_p$), but $\phi$ collapses from
$1.166\times10^8$ to $6.400\times10^7$ m² s⁻². A lower $\phi$ means a *lower*
resistance to compression per unit mass, so a given pressure step produces a
larger temperature step along the adiabat. The core adiabat is near 0.5 K/km on
average, which is the correct order.

**Absolute temperature is *not* fixed by all this.** The whole table scales with
the 1900 K anchor, and equation (11) alone cannot set it: an adiabat is a
family of solutions, and picking one requires an independent constraint — a
melting-point estimate, a heat-flow budget, or a laboratory determination. The
table gives 2825 K at the CMB and 4175 K at the inner-core boundary; a model that
anchored at 2200 K instead would give roughly 3250 K and 4700 K. Quoting "the
temperature of the core" to four digits misrepresents the state of the knowledge;
quoting the *gradient* to two is entirely defensible, because the gradient is what
the physics fixes.

### 4.5 The thermal pressure, sized

Equation (9) evaluated with nominal $\alpha$ and the adiabat temperatures of §4.4
($T_{\text{ref}} = 300$ K):

| Region | $\alpha$ (K⁻¹) | $K$ (GPa) | $\Delta T$ (K) | $\alpha K\Delta T$ (GPa) |
|---|---|---|---|---|
| Lower mantle, 2000 km | $3.0\times10^{-5}$ | 300 | 2176 | 19.6 |
| Core–mantle boundary | $2.5\times10^{-5}$ | 650 | 2525 | 41.0 |
| Outer core, 4000 km | $1.0\times10^{-5}$ | 700 | 3296 | 23.1 |
| Inner-core boundary | $1.0\times10^{-5}$ | 1400 | 3875 | 54.2 |

The thermal pressure at the CMB is **41 GPa against a total of 135 GPa** — about
30 per cent. This is not a correction; it is a leading term. Any comparison of a
laboratory equation of state with a seismological model in the deep Earth that
ignores it is wrong at the level of the parameter being measured.

The expansion coefficients are nominal, decrease with pressure and rise with
temperature, so these are anchors rather than calculations. The conclusion does
not depend on their third digit.

## 5. Physical interpretation: why this constrains composition

Assemble the argument in the order it is actually used.

1. **Seismology gives $\phi(z)$**, an exact function of the two measured
   velocities. This is $K/\rho$, no mineralogy assumed.
2. **If the layer is homogeneous and adiabatic**, equation (7) integrates
   $\phi(z)$ into $\rho(z)$ up to an anchor.
3. **The anchor comes from outside seismology** — the Earth's mass and moment of
   inertia (lesson [01](./01-pressure-density-depth.md) §3.4), or free-oscillation
   data.
4. **Mineral physics supplies $K$, $\mu$ and $\rho$ for a candidate assemblage**
   at the model's $(P,T)$, through an equation of state plus a thermal term.
5. **Compare.** An assemblage reproduces the observed $(v_p,v_s,\rho)$ or it does
   not. If it does not, either the assemblage or the $(P,T)$ is wrong — and the
   *pattern* of the misfit says which: a density that is too high at the right
   velocities points to composition, a small uniform offset in both velocities
   points to temperature.
6. **Where step 2 fails**, that is the signal. The transition zone's ratio of 0.22
   (lesson [01](./01-pressure-density-depth.md) §4.3) is mineral physics being
   discovered by seismology.

That is the whole loop, and it works only because $K/\rho$ is directly
observable. If the elastic moduli entered the velocities in some other
combination, none of this would be possible.

## 6. Assumptions and regime of validity

| Assumption | Where used | Regime of validity | What breaks it |
|---|---|---|---|
| Birch–Murnaghan is the correct energy expansion | §2 | Excellent to $V/V_0 \gtrsim 0.7$ for most minerals; the standard to ~200 GPa | Extreme compression, and materials with soft modes or electronic transitions; alternative forms (Vinet, Holzapfel) differ by a few GPa in the extrapolation |
| $K_0$, $K_0'$ are constants | §2 | Along an isotherm, at temperatures near the calibration | $K$ falls by 10–20 per cent from 300 K to mantle temperatures, so a room-temperature $K_0$ is not the mantle value |
| Isotropic elasticity | §3, equation (4) | Mantle minerals are elastically anisotropic; the *mean* of the single-crystal moduli enters | The lowermost mantle and the inner core are measurably anisotropic — a separate observable |
| Homogeneous layer | §3.2 | A convecting, well-mixed layer | The transition zone, the D″ region, and any compositional boundary |
| Adiabatic compression | §3.2, §4.3 | Fast or convecting regions | Conductive boundary layers; the lithosphere is not adiabatic |
| Quasi-harmonic thermal equation of state | §4.2 | $\gamma$ nearly independent of $V$ and $T$ | Anharmonicity at high $T$; electronic contributions in iron |
| $\Delta T = T - 300$ K in equation (9) | §4.5 | A linearised thermal pressure | Large $\Delta T$, where $\alpha$ varies strongly — which is exactly the situation being estimated, whence the caution |

## 7. Units and dimensional analysis

- **$P(V)$ in Birch–Murnaghan.** $x$ is dimensionless, so $P$ carries the units
  of $K_0$: GPa in, GPa out. Neither $K_0'$ nor $x$ has units.
- **$\phi$.** $v_p^2$ in (km/s)² = km² s⁻², which is $10^6$ m² s⁻². Then
  $\rho\phi$ with $\rho$ in kg m⁻³ gives kg m⁻¹ s⁻² = Pa. **The factor $10^6$ is
  the commonest arithmetic error in this subject.**
- **Adams–Williamson.** $\rho g/\phi$: $\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}}
  / (\mathrm{m^2\,s^{-2}}) = \mathrm{kg\,m^{-3}\,m^{-1}}$ ✓ — a density gradient
  per metre, conventionally reported per kilometre after multiplying by $10^3$.
- **Adiabatic gradient.** $\gamma gT/\phi$: $1\cdot\mathrm{m\,s^{-2}}\cdot
  \mathrm{K}/(\mathrm{m^2\,s^{-2}}) = \mathrm{K\,m^{-1}}$ ✓. Reported as K/km.
- **Thermal pressure.** $\alpha K\Delta T$: $\mathrm{K^{-1}}\cdot\mathrm{Pa}\cdot
  \mathrm{K} = \mathrm{Pa}$ ✓.
- **Useful anchor.** $\gamma = 1.5$ and $\phi \approx 10^8$ m² s⁻² in the deep
  mantle give $\mathrm{d}T/\mathrm{d}z \approx 1.5\times10^{-8}\,gT$ K/m, i.e.
  $1.5\times10^{-5}\,gT$ K/km. With $g\approx10$ and $T\approx2000$ that is
  0.3 K/km, which is the order to remember.

## 8. Python demonstration

[`code/eos_mineral_physics_demo.py`](./code/eos_mineral_physics_demo.py)
evaluates the equation of state, inverts it, compares it with the reference model,
and builds the adiabat. The blocks below are the script's actual output,
**abridged by omission** where a block would otherwise repeat rows already
tabulated above; every line shown is reproduced verbatim.

```text
   V/V0  rho/rho0   forsterite    periclase   bridgmanit          hcp
                       P (GPa)      P (GPa)      P (GPa)      P (GPa)
   1.00     1.000          0.0          0.0          0.0          0.0
   0.95     1.053          7.3          9.1         14.8          9.6
   0.90     1.111         16.8         20.8         33.8         22.6
   0.85     1.176         29.3         36.0         58.5         40.3
   0.80     1.250         45.7         55.8         90.7         64.5
   0.70     1.429         97.2        116.7        189.7        144.6
```

```text
mineral                   P target     V/V0  rho/rho0    P back   residual
forsterite Mg2SiO4              10   0.9345    1.0701    10.000  -7.99e-14
forsterite Mg2SiO4             135   0.6527    1.5322   135.000   2.56e-13
periclase MgO                  135   0.6787    1.4734   135.000  -5.68e-14
bridgmanite MgSiO3             135   0.7481    1.3367   135.000   2.27e-13
hcp iron Fe                    330   0.5903    1.6939   330.000  -7.96e-13
```

```text
  Compress that material isothermally to the CMB density
    rho = 5570 kg/m3  =>  V/V0 = 0.7899
    Birch-Murnaghan pressure at that compression = 107.0 GPa
    hydrostatic pressure at the CMB             = 134.6 GPa
    ratio EOS / hydrostatic                     = 0.795
```

```text
 depth km              region    rho      g  phi (m2/s2)   T (K)  dT/dz (K/km)
      660    lower mantle top   4400  9.947    6.428e+07    1900         0.441
     2000        lower mantle   5103  9.882    9.388e+07    2476         0.391
     2891      just above CMB   5570 10.510    1.166e+08    2825         0.382
     2891      just below CMB   9900 10.510    6.400e+07    2825         0.696
     4000          outer core  11028  7.745    8.331e+07    3596         0.502
     5153 inner-core boundary  12166  4.387    1.047e+08    4175         0.262
```

```text
region                alpha (1/K)  K (GPa)  dT (K)  dP_th (GPa)
lower mantle 2000 km      3.0e-05      300    2176         19.6
core-mantle boundary      2.5e-05      650    2525         41.0
outer core 4000 km        1.0e-05      700    3296         23.1
inner-core boundary       1.0e-05     1400    3875         54.2
```

### What to observe

| Observation | Consequence |
|---|---|
| $P_3 - P_2 = 0.000\times10^0$ when $K_0'=4$ | The third-order term is proportional to $K_0'-4$; the identity is exact |
| 0.155 GPa per unit of $K_0'$ at $V/V_0=0.85$, $K_0=160$ GPa | The third-order correction is small for mantle minerals but not for iron |
| Round-trip residuals of order $10^{-13}$ GPa | The inversion is exact to bisection tolerance; an EOS you cannot invert is unusable |
| Bridgmanite needs 58.5 GPa where forsterite needs 29.3 at $V/V_0=0.85$ | Stiffness, not density, is what distinguishes the lower mantle |
| EOS/hydrostatic ratio 0.795 at the CMB | The isothermal single-phase EOS misses 20 per cent of the pressure; §4.1 names what is missing |
| $\phi$ falls from $1.166\times10^8$ to $6.400\times10^7$ m² s⁻² at the CMB | The $\sim$1.8× jump in $\gamma gT/\phi$ across a boundary at which $g$ and $T$ are continuous |
| Mantle adiabat 0.44 → 0.38 K/km | A few tenths of a kelvin per kilometre, set by $\phi$, $g$ and $T$ |
| Core adiabat 0.70 → 0.50 K/km | Factor-of-two larger than the mantle at the CMB |
| Adiabat 1900 → 4175 K | The absolute value is set by the anchor, not by the equations |
| Thermal pressure 41 GPa against 135 GPa total | 30 per cent of the pressure at the CMB is thermal |

> **Breaking exercise.** Set $\gamma = 1.0$ and then $\gamma = 2.5$ in the demo and
> predict both the new gradients and the new CMB temperature before running.
> Then answer the question the two runs raise: $\gamma$ is described as being
> "close to 1.5" in the core, yet it appears *linearly* in the gradient, so an
> error of 0.5 in $\gamma$ is a 33 per cent error in $\mathrm{d}T/\mathrm{d}z$.
> Given that the absolute temperature is anyway anchored rather than derived, what
> can a core adiabat calculation legitimately be used for? (Answer: comparing the
> adiabat with a melting curve, and computing a *difference* of temperatures
> between two depths, both of which are far less sensitive to the anchor than an
> absolute value is.)

## 9. Common mistakes

1. **Forgetting the $10^6$ in $\phi$.** $v_p$ and $v_s$ in km/s give $\phi$ in
   km² s⁻². Multiplying by $\rho$ without converting gives a $K$ six orders of
   magnitude too small.
2. **Using a room-temperature $K_0$ at mantle temperature.** $K$ falls by 10–20
   per cent over that range.
3. **Treating Birch–Murnaghan as exact.** It is a truncated expansion. Different
   truncations — Vinet, Holzapfel — agree to within a few GPa at 200 GPa and
   disagree more beyond it; the spread is the honest uncertainty of the
   extrapolation.
4. **Assuming $K_0' = 4$ universally.** It is a good approximation for silicates
   and a poor one for iron, and the difference appears where the interesting
   physics is.
5. **Applying Adams–Williamson to a layer that is not homogeneous.** Its failure
   is informative; using it anyway throws away the information.
6. **Integrating the adiabat without a stated anchor.** Equation (11) gives the
   slope of a family, not a member of it.
7. **Quoting a core temperature to four digits.** See mistake 6.
8. **Ignoring the thermal pressure because it is "a correction".** At the CMB it
   is 30 per cent of the total.
9. **Assuming $\alpha$ is constant.** It falls with pressure, so a thermal
   pressure scaled linearly in $\Delta T$ over 4000 K overestimates the deep
   contribution *and* underestimates the shallow one; the sign of the error
   depends on where you are.
10. **Confusing the adiabatic gradient with the actual gradient.** The mantle's
    real gradient is the adiabat plus a superadiabatic excess that drives
    convection; the difference is small but not zero, and it is the driving term.

## 10. Real-world applications

- **Diamond-anvil cell and shock experiments.** Every reported pressure is
  calibrated by an equation of state, usually of a standard such as gold, platinum
  or MgO. Change the calibration EOS and every pressure in the literature shifts.
- **Interpretation of seismic tomography.** Converting a velocity anomaly into a
  temperature anomaly requires $\partial v/\partial T$ at fixed pressure, which is
  an equation-of-state derivative
  ([12-global-geophysics-interior/04-02](../../12-global-geophysics-interior/02-composition-and-mineral-physics/03-ab-initio-mineral-physics.md)).
- **Core composition.** The density deficit of the outer core relative to pure
  iron at the same $(P,T)$ is the central quantity in the problem of what light
  elements the core contains.
- **Geodynamo modelling.** The adiabatic gradient sets whether the core is
  thermally or compositionally convecting, and hence whether the dynamo is
  efficient enough to explain the palaeomagnetic record
  ([12-global-geophysics-interior/04-02](../../12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md)).
- **Mantle convection and the geotherm.** The adiabat is the reference against
  which the geotherm's superadiabatic excess is measured
  ([13-geodynamics-tectonics/02-01](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md)).
- **Exoplanet and super-Earth interiors.** With no seismology available, mass and
  radius alone are fitted by an equation of state, and the degeneracy between
  composition and temperature is the dominant uncertainty.

## 11. Further reading

- **Birch, F. (1952).** "Elasticity and constitution of the Earth's interior."
  *Journal of Geophysical Research* **57**, 227–286. The origin of both the
  finite-strain equation of state and the velocity-density correlation. Level:
  graduate.
- **Poirier, J.-P. *Introduction to the Physics of the Earth's Interior* (2nd ed.,
  Cambridge University Press, 2000).** The clearest short development of
  finite-strain equations of state and the Grüneisen parameter for a geophysical
  audience. Level: graduate.
- **Anderson, O. L. *Equations of State of Solids for Geophysics and Ceramic
  Science* (Oxford University Press, 1995).** The definitive treatment, including
  the comparison of the competing EOS forms. Level: doctoral.
- **Stacey, F. D., & Davis, P. M. *Physics of the Earth* (4th ed., Cambridge
  University Press, 2008).** The equation of state *inside the Earth*, including
  the thermal terms and their size. Level: graduate.
- **Dziewonski, A. M., & Anderson, D. L. (1981).** "Preliminary reference Earth
  model." *Physics of the Earth and Planetary Interiors* **25**, 297–356. The
  reference model against which any EOS prediction is tested.
- **Jackson, I. *The Earth's Mantle: Composition, Structure and Evolution*
  (Cambridge University Press, 1998).** The experimental and observational
  context, including what can and cannot be measured.
- **Anderson, D. L. *Theory of the Earth* (Blackwell, 1989).** The seismic
  equation of state and the Bullen–Adams–Williamson method in their historical
  development.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the reference model this lesson supplies the density for.
- [03 Seismic Velocities, Elastic Moduli and Mineralogy](./03-seismic-parameter-relations.md)
  — the mineralogical interpretation of $\phi$ and of the 410 and 660 km
  discontinuities.
- [05 Comparative Planetary Physics and Interiors](./05-planetary-physics.md)
  — the same equations of state applied where seismology is unavailable.
- [02-05-07 Phase Equilibria and Mantle Mineralogy](../05-thermodynamics/07-phase-equilibria.md)
  — the Clapeyron slopes that make the phase changes.
- [02-04-04 Elastic Moduli](../04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
  — where $K$, $\mu$ and the wave speeds come from.
- [12-global-geophysics-interior/02-02 High-Pressure Experiments](../../12-global-geophysics-interior/02-composition-and-mineral-physics/02-high-pressure-experiments.md)
  — how $K_0$ and $K_0'$ are actually measured.

Exercises:
[`exercises/02-equations-of-state-exercises.md`](./exercises/02-equations-of-state-exercises.md)
and
[`exercises/02-equations-of-state-solutions.md`](./exercises/02-equations-of-state-solutions.md).

## Self-assessment checklist

- [ ] I can write the Birch–Murnaghan equation to second and third order and
      define $x$, $f$, $K_0$ and $K_0'$. (§2)
- [ ] I can show that $P_3 = P_2$ exactly when $K_0' = 4$ and explain why. (§2.3)
- [ ] I can check that any $P(V)$ reproduces $K_0 = -V_0\,\mathrm{d}P/\mathrm{d}V$
      at the reference volume. (§2.2)
- [ ] I can invert the EOS for $V(P)$ and verify the inversion. (§8)
- [ ] I can derive $\phi = v_p^2-\tfrac43v_s^2 = K/\rho$ in two lines. (§3.1)
- [ ] I can derive Adams–Williamson and state the two assumptions it carries.
      (§3.2)
- [ ] I can state what the ratio $\mathrm{d}\rho/\mathrm{d}z$ (A–W) / (model)
      being 1.00 or 0.22 means. (§3.2)
- [ ] I can derive $(\mathrm{d}T/\mathrm{d}z)_s = \gamma gT/\phi$ from
      $\mathrm{d}S=0$. (§4.3)
- [ ] I can integrate an adiabat from a stated anchor and say what the anchor
      does and does not determine. (§4.4)
- [ ] I can estimate the thermal pressure at the CMB and compare it with the
      total. (§4.5)
- [ ] I can explain the 20 per cent shortfall of the isothermal EOS at the CMB
      with both missing terms named. (§4.1)
