---
id: 15-03-02
title: "Oceanic Crust Structure and Ophiolites"
level: doctoral
prereqs: ["15-03-01", "15-02-06", "06-02-02", "05-04-01"]
tags: [oceanography, marine-geophysics, seafloor-tectonics, oceanic-crust, refraction, ophiolite]
---

# Oceanic Crust Structure and Ophiolites

> **All models and data in this module are SYNTHETIC.** The velocity model, the
> travel times and the mixing calculation below are teaching models built from
> stated model constants. No real ridge, ophiolite massif, borehole or survey is
> used, and no number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the layer-cake architecture of oceanic crust and **name** the
   petrological unit that each seismic layer corresponds to.
2. **Derive** the head-wave travel-time equation
   $t(x)=x/v_k+2\sum_{i<k}h_i\cos\theta_i/v_i$ from Snell's law and ray geometry.
3. **Invert** a set of picked first-arrival branches for layer velocities and
   thicknesses by the slope–intercept method, and **state** why the recursion
   propagates error downward.
4. **Compute** crossover distances and **design** an offset range for each
   refractor.
5. **Quantify** the velocity–depth trade-off for the shallowest layer and
   **explain** why well-constrained velocity and thickness still trade off.
6. **Compute** Voigt and Reuss bounds for a serpentinised mantle and **show** with
   numbers that $v_p$ alone cannot place the petrological Moho.
7. **Propagate** a picking error to a crustal thickness uncertainty by Monte
   Carlo, and **state** which layer carries the largest relative error.

## Prerequisites

- [15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](01-mid-ocean-ridges.md) —
  where the crust is built and why it cools.
- [15-02-06 Ocean-Bottom Seismology and OBS Networks](../02-marine-geophysics-methods/06-obn-ocean-bottom-seismology.md) —
  the acquisition geometry used here.
- [06-02-02 Snell's Law and Layered Media](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter and head waves.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the rock-physics link between pore space, hydration and velocity.

## 1. Intuition: a layer cake that is also an outcrop

Oceanic crust is made at a spreading axis in a fixed sequence: lava erupts and
quenches into pillows, the plumbing below it freezes into a sheeted dyke complex,
and the frozen magma chamber beneath that crystallises into gabbro. Each unit has
a different porosity, mineralogy and therefore seismic velocity, and the sequence
repeats with little variation across tens of thousands of kilometres of ridge. A
marine refraction experiment measures the velocity structure of that stack; a
refraction survey is, in effect, a remote stratigraphic log.

Two facts make the problem interesting rather than routine.

First, **the sequence is exposed on land**. Where oceanic crust has been
obducted onto a continent — the ophiolite massifs — the same stack can be walked
out and sampled. That gives seismologists an unusually direct calibration, and it
also warns them: the ophiolite pseudostratigraphy is not uniform, and the field
relationships are more complicated than the idealised layer cake.

Second, **the velocity structure is not the rock structure**. A velocity step does
not have to be a lithological boundary, and a lithological boundary does not have
to be a velocity step. The classic case is the Moho: hydration of mantle
peridotite to serpentinite lowers its velocity from about $8.1$ to about
$5.1\ \mathrm{km\,s^{-1}}$, so a serpentinised mantle can sit directly beneath
crust-like velocities. A refraction line that reports "Moho at 5.6 km" has
measured a velocity step, and it takes an independent measurement — $v_s$, or a
density from gravity — to say whether the petrological Moho is there.

## 2. Precise definitions

**Layer 2A**: the uppermost extrusive basalt, high porosity, low velocity.
**Layer 2B**: the sheeted dyke complex, low porosity, velocity set by the
mineralogy of the dykes. **Layer 3**: gabbro, the highest crustal velocity.
**Moho**: the level at which the velocity steps up to mantle peridotite values —
a seismological definition.

**Apparent velocity** $v_{\text{app}}$: the reciprocal of the slope of a
first-arrival branch, $\mathrm{d}x/\mathrm{d}t$. For a flat refractor it equals the
refractor velocity; for a dipping refractor it is the *apparent* velocity and must
be reduced to a true velocity with a reversed (two-way) spread.

**Intercept time** $t_i$: the extrapolation of a refractor branch back to zero
offset. It is not a physical arrival time at zero offset; it is an algebraic
quantity that carries the thickness information.

**Crossover distance** $x_c$: the offset at which a deeper refractor becomes the
first arrival, i.e. where its branch intersects the branch above it. It tells you
how far the spread must reach.

**Ray parameter** $p=\sin i/v$, constant along a ray (Snell). For the head wave
along the top of layer $k$, $p=1/v_k$ exactly, which is what makes the branch
linear.

**Voigt and Reuss bounds**: arithmetic and harmonic averages of a two-phase
mixture property, the standard rigorous bounds when the geometry is unknown.
Their geometric mean is used here as a middle estimate *model*, not as a bound.

## 3. Derivations

### 3.1 The head-wave travel time

Consider a stack of flat layers with thicknesses $h_i$ and velocities $v_i$, and a
source and receiver both on the top surface. A ray that travels down through
layers $0,\dots,k-1$, runs along the interface at the top of layer $k$, and comes
back up, must be critically refracted at that interface, so in every layer $i<k$:

$$\sin\theta_i=\frac{v_i}{v_k},\qquad \cos\theta_i=\sqrt{1-\frac{v_i^2}{v_k^2}} .$$

The vertical distance travelled in layer $i$ is $2h_i$, so the time spent there is
$2h_i/(v_i\cos\theta_i)$ — but it is easier to write it as $2h_i\cos\theta_i/v_i$
by using $\cos\theta_i = 1/(v_i q_i)$ with the vertical slowness
$q_i=\cos\theta_i/v_i$; both forms are the same number, and the second is what a
refraction nomogram uses. The horizontal run along the interface contributes
$x/v_k$ measured between the entry and exit points, and the projections of the
up- and down-going legs combine with the geometric offset to leave simply

$$\boxed{\;t(x)=\frac{x}{v_k}+\underbrace{2\sum_{i=0}^{k-1}
h_i\frac{\cos\theta_i}{v_i}}_{\textstyle t_i}\;}$$

The demonstration computes, for its SYNTHETIC model ($h=[0.45,1.10,4.00]$ km,
$v=[3.00,5.20,6.80,8.10]$ km/s, Moho at 5.55 km):

| refractor | $v_k$ (km/s) | $t_i$ (s) |
|---|---|---|
| top of 2B | 5.20 | 0.2450 |
| top of layer 3 | 6.80 | 0.5418 |
| mantle | 8.10 | 1.2423 |

and the first line of the derivation can be checked by hand: for the top of 2B,
$\sin\theta_0 = 3.00/5.20=0.5769$, $\cos\theta_0=0.8168$,
$t_i=2\times0.45\times0.8168/3.00=0.2450\ \mathrm{s}$.

### 3.2 The slope–intercept inversion, and why errors cascade

Fitting a straight line to each branch gives $\mathrm{d}t/\mathrm{d}x=1/v_k$
exactly, so the refractor velocity comes out of the slope with no assumption at
all. The intercept then gives the thickness of the layer *immediately above* the
refractor, using the overburden already recovered:

$$h_{k-1}=\frac{\left(t_i^{(k)}-2\sum_{i=0}^{k-2}h_i\cos\theta_i/v_i\right)v_{k-1}}
{2\cos\theta_{k-1}} .$$

Note the sum now stops at $k-2$: the layer being solved for is *excluded*,
otherwise the equation would be circular.

The recursion is the vulnerability. $h_0$ comes from the 2B branch and uses the
recovered $v_0$; $h_1$ uses $h_0$ and $v_0,v_1$; $h_2$ uses both. An error in
$v_0$ propagates into $h_0$, then into $h_1$, then into $h_2$, so **the shallowest
layer's error contaminates every deeper thickness**. The demonstration's
noise-free inversion recovers all three velocities and thicknesses exactly
(residuals $\le10^{-5}$ km), which is the verification that the algebra and the
code agree; with $10\ \mathrm{ms}$ picking noise the thickness uncertainties
become

| unit | true $h$ (km) | mean $\hat h$ (km) | std (km) | std/true |
|---|---|---|---|---|
| layer 2A | 0.45 | 0.457 | 0.048 | 10.7% |
| layer 2B | 1.10 | 1.099 | 0.051 | 4.6% |
| layer 3 | 4.00 | 4.005 | 0.079 | 2.0% |
| Moho (sum) | 5.55 | 5.561 | 0.063 | 1.1% |

The thin top layer carries a 10.7% relative error while the Moho *total* is
determined to 1.1%: the errors of adjacent layers are anti-correlated because the
same picks are used twice. **A well-determined total thickness does not mean the
internal division is well determined.**

### 3.3 Crossover distances

Setting the two branch times equal, $x_c/v_{k-1}+t_i^{(k-1)}=x_c/v_k+t_i^{(k)}$:

$$x_c=\frac{t_i^{(k)}-t_i^{(k-1)}}{1/v_{k-1}-1/v_k} .$$

For the model, the demonstration computes $x_c=1.738$ km from the direct wave to
the 2B refractor, $6.559$ km from 2B to layer 3, and $29.677$ km from layer 3 to
the mantle. These are *design* numbers: a spread that reaches only 20 km never
sees the mantle refraction, and a survey with no offsets below about 1.8 km never
sees the direct wave. Since the near-offset picks are what break the
velocity–depth trade-off (§3.4), the short offsets are not optional.

### 3.4 The velocity–depth trade-off

Differentiate the intercept time of the first refractor,

$$t_i=\frac{2h_0\sqrt{1-v_0^2/v_1^2}}{v_0}=2h_0\sqrt{v_0^{-2}-v_1^{-2}} ,$$

holding $t_i$ fixed (the fit is what it is):

$$\frac{\mathrm{d}h_0}{h_0}=\frac{v_1^2}{v_1^2-v_0^2}\,\frac{\mathrm{d}v_0}{v_0}
=1.499\,\frac{\mathrm{d}v_0}{v_0}$$

for $v_0=3.00$, $v_1=5.20\ \mathrm{km\,s^{-1}}$. A 10% error in the top-layer
velocity requires a **15% error in the same direction** in its thickness to
absorb it: the fit cannot tell them apart from the head waves alone. Exactly
solving the same constraint at $v_0=3.30$ km/s gives
$h_0=0.2450\times3.30/(2\times0.7729)=0.523\ \mathrm{km}$ (the linearisation
predicts $0.45\times1.1^{1.499}=0.519$ km; both round to 0.52).

The demonstration confirms this against a grid search. Using the 2B branch alone
with $10\ \mathrm{ms}$ of pick noise, the best-fitting cells are
$(v,h)=(3.40,0.55)$ km/s/km — biased away from the true $(3.00,0.45)$ by the noise
realisation — and pairs from $v=2.50$ to $3.60\ \mathrm{km\,s^{-1}}$ remain
admissible along the trade-off band. Adding the four near-offset direct picks
(0.6 km of offset range) collapses the admitted set to the single cell
$(3.00,0.45)$ and moves $\chi^2$ at $v=2.70\ \mathrm{km\,s^{-1}}$ from 12.5 to
104.0. **The short offsets carry the top-layer velocity; the long offsets carry
the structure.**

### 3.5 Serpentinisation: velocity bounds and the Poisson-ratio test

Model the hydrated mantle as a two-phase mixture of peridotite
($v_p=8.10\ \mathrm{km\,s^{-1}}$, $\rho=3.30\ \mathrm{g\,cm^{-3}}$) and
serpentinite ($v_p=5.10$, $\rho=2.55$). Without knowing the geometry, the
rigorous bounds are the Voigt (arithmetic) and Reuss (harmonic) averages:

$$v_{\text{Voigt}}=f v_a+(1-f)v_b,\qquad
v_{\text{Reuss}}=\left(\frac{f}{v_a}+\frac{1-f}{v_b}\right)^{-1}.$$

The demonstration's table spans $(8.10,8.10)$ at $f_{\text{serp}}=0$ to
$(5.10,5.10)$ at $f_{\text{serp}}=1$, with the bounds reaching
$(7.50,7.25)\ \mathrm{km\,s^{-1}}$ at 20% serpentine. Interpolating the Reuss
average, $v_p$ falls to $7.50\ \mathrm{km\,s^{-1}}$ — a velocity a refraction
survey would happily interpret as lower crust — at only $0.14$ serpentine
fraction.

The discriminator is the Poisson ratio. From the model end-members,

$$\nu=\frac{v_p^2-2v_s^2}{2(v_p^2-v_s^2)}:
\qquad \nu_{\text{peridotite}}=0.277,\qquad \nu_{\text{serpentinite}}=0.324 .$$

A serpentinised mantle has a high $v_p/v_s$; lower crust does not. Measuring $v_s$
from the same ocean-bottom data separates two models that $v_p$ alone cannot.
**Both numbers are model values**: the end-member velocities and densities are
chosen teaching constants, and the bounding algebra is exact only for the two
idealised geometries. The conclusion — "$v_p$ alone does not distinguish them" —
is a statement about the ambiguity, not about the rock.

## 4. Physical interpretation

- **Why the branch is linear.** A head wave travels along the interface at exactly
  $v_k$, so the only offset-dependent term is $x/v_k$. Linearity is a property of
  the flat-layered model; a dipping interface or lateral heterogeneity curves the
  branch, and that curvature is the signal, not noise.
- **Why the velocities are well determined and the thicknesses are not.** The
  velocity comes from a slope, which uses the whole branch; the thickness comes
  from an intercept, which is an extrapolation beyond the data. Extrapolations
  have no noise-averaging.
- **Why layer 2A is the hard layer.** It is thin, and its velocity is low, so the
  intercept is small and short, and it also carries the largest relative
  uncertainty. In real data 2A's velocity and thickness are also affected by
  anisotropy: dykes and fissures make the velocity azimuth-dependent, so the
  apparent velocity changes with the strike of the survey line.
- **Why the Moho is a convention.** The seismological Moho is where $v_p$ steps to
  mantle values. The petrological Moho is the base of the gabbro. Serpentinisation
  decouples them, and so does underplating, and so does a thick gabbro-to-
  peridotite transition. Reporting "Moho depth" without saying which definition is
  in use is a category error.

## 5. Assumptions and regime of validity

1. **Flat, horizontal, homogeneous, isotropic layers.** Dipping interfaces require
   reversed spreads; anisotropy (layer 2B) makes the result azimuth-dependent;
   heterogeneity along the line smears the branch.
2. **Every picked arrival is the head wave from the intended refractor.** Cycle
   skipping — picking the wrong swing of the wavelet — biases the intercept by
   one period, which is often larger than the whole thickness signal.
3. **First arrivals only.** Later arrivals (reflections, converted phases) carry a
   different geometry and must be modelled separately.
4. **Source and receiver on the seafloor.** With a surface source, the water-path
   delay, the seafloor relief and the water-velocity model must be removed first;
   each contributes error of the same order as the crustal signal.
5. **Velocity increases with depth.** A low-velocity layer (a thin sediment or a
   breccia zone) hides everything below it from head waves.
6. **Thicknesses are inferred given the overburden velocities.** The inversion is
   recursive, so its errors are correlated; the Monte Carlo in the demonstration
   is what makes that statement quantitative.
7. **The mixing calculation assumes two pure phases and no porosity.** Real
   serpentinites carry pore water and the transition is gradational.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| offset | $x$ | km | |
| thickness | $h_i$ | km | |
| velocity | $v_i$ | $\mathrm{km\,s^{-1}}$ | |
| slowness | $1/v$ | $\mathrm{s\,km^{-1}}$ | |
| intercept time | $t_i$ | s | $\mathrm{km}\times\mathrm{s\,km^{-1}}$ |
| Poisson ratio | $\nu$ | dimensionless | ratio of squared velocities |
| density | $\rho$ | $\mathrm{g\,cm^{-3}}$ | $1\ \mathrm{g\,cm^{-3}}=10^3\ \mathrm{kg\,m^{-3}}$ |

Every term in $t(x)$ must be a time: $x/v$ is
$\mathrm{km}/(\mathrm{km\,s^{-1}})=\mathrm{s}$ and $h\cos\theta/v$ likewise. If a
computed intercept has units of $\mathrm{km\,s^{-1}}$, a velocity has been used
where its reciprocal was needed — the commonest algebra slip in this calculation.

## 7. Worked examples

All numbers are printed by `code/oceanic_crust_structure_demo.py`.

### Example 1 — the 2B intercept by hand

$v_0=3.00$, $v_1=5.20\ \mathrm{km\,s^{-1}}$, $h_0=0.45$ km.
$\sin\theta_0=0.5769$, $\cos\theta_0=0.8168$, so

$$t_i=\frac{2\times0.45\times0.8168}{3.00}=0.2450\ \mathrm{s}.$$

The travel time at 20 km is $20/5.20+0.2450=4.0912$ s, matching the
demonstration. The 3 km pick is $3/5.20+0.2450=0.8220$ s.

### Example 2 — why 20 km is enough for layer 3 but not for the mantle

The layer-3 branch is a first arrival beyond $6.559$ km, so a 20 km spread sees
it; the mantle branch needs $29.677$ km, so the same spread does not. Extending
to 100 km gives $t=100/8.10+1.2423=13.5880$ s. The design consequence: to see
the Moho beneath 5.55 km of crust in this model, the spread must reach roughly
$5\times$ the Moho depth.

### Example 3 — the trade-off, checked two ways

Keeping the 2B intercept fixed at $0.2450$ s while raising $v_0$ to
$3.30\ \mathrm{km\,s^{-1}}$ requires
$h_0=0.2450\times3.30/(2\times0.7729)=0.523$ km. The grid search admits
$h_0=0.50$ and $0.55$ km as its best cells at that velocity, and the linearised
trade-off $1.499\,\delta v_0/v_0$ predicts $0.519$ km. All three agree to better
than the 0.05 km grid step.

### Example 4 — a 10 ms pick error, propagated

$h_0=0.45$ km is recovered as $0.457\pm0.048$ km; the Moho total as
$5.561\pm0.063$ km. The Moho uncertainty is *smaller* than any single layer's
because the three layers are fitted from the same picks. If a study quotes
"Moho at 5.6 km" with no uncertainty, it has discarded the only number that says
whether the result is meaningful.

### Example 5 — serpentinised mantle or lower crust?

At 14% serpentine (Reuss average) the hydrated mantle has
$v_p=7.50\ \mathrm{km\,s^{-1}}$, indistinguishable from lower crust in a $v_p$
section. Its Poisson ratio would be between 0.277 and 0.324 rather than the
$\approx0.25$ typical of a gabbro, so a $v_s$ measurement resolves it. Without
$v_s$, the honest statement is: "a velocity step at 5.55 km; the petrological
boundary may be up to a few kilometres deeper."

## 8. Python demonstration

`code/oceanic_crust_structure_demo.py` prints, with units:

1. the layered model, the three intercept times and the fitted apparent
   velocities (which recover the model velocities exactly);
2. the crossover distances $1.738$, $6.559$ and $29.677$ km;
3. the noise-free inversion, as a verification of the algebra;
4. the Monte-Carlo thickness table for a $10\ \mathrm{ms}$ pick error;
5. the velocity–depth trade-off with and without the near-offset direct branch,
   with $\chi^2$ values;
6. the Voigt/Reuss serpentinisation table and the Poisson-ratio test.

```bash
cd 15-oceanography-marine/03-seafloor-tectonics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python oceanic_crust_structure_demo.py
```

## 9. Exercises

[`exercises/02-oceanic-crust-structure-exercises.md`](./exercises/02-oceanic-crust-structure-exercises.md)
and
[`exercises/02-oceanic-crust-structure-solutions.md`](./exercises/02-oceanic-crust-structure-solutions.md).

## 10. Real-world applications

- **Crustal thickness maps.** Refraction and wide-angle data are the only
  measurements that give crustal thickness directly rather than through a gravity
  or isostasy assumption.
- **Ophiolite interpretation.** Field mapping of obducted oceanic crust is
  calibrated against, and calibrates, the seismic layer cake; the sheeted dyke
  complex is a field outcrop of layer 2B.
- **Ridge and hydrothermal studies.** The depth to the axial magma lens, and the
  porosity structure of layer 2A, control where hydrothermal circulation reaches.
- **Subduction inputs.** The thickness and hydration state of the incoming plate
  set the water budget of the arc
  ([15-03-03](03-subduction-zones-marine.md)).
- **Site characterisation for drilling.** A refraction line is the cheapest way to
  decide whether a proposed borehole will reach the target unit.

## 11. Further reading

- **Turcotte, D. L., & Schubert, G., *Geodynamics*, Cambridge University Press.**
  Level: graduate textbook. The thermal and mechanical context for the layer
  structure.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*,
  Cambridge University Press.** Level: textbook. The slope–intercept and
  plus–minus refraction methods used above, in their classical form.
- **Kearey, P., Brooks, M., & Hill, I., *An Introduction to Geophysical
  Exploration*, Wiley-Blackwell.** Level: textbook. Refraction survey design and
  crossover geometry.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can write the head-wave travel-time equation and explain each term.
- [ ] I can compute an intercept time by hand from a two-layer model.
- [ ] I can invert a three-branch data set for velocities and thicknesses.
- [ ] I can compute crossover distances and use them to design offset ranges.
- [ ] I can derive the velocity–depth trade-off coefficient for a two-layer case.
- [ ] I can explain why the Moho total is better determined than a single layer's
      thickness.
- [ ] I can state what $v_p$ alone cannot determine at the Moho, and what would.
## Common pitfalls
1. **Reading a velocity step as a lithological boundary.** The Moho is a
   convention; serpentinisation moves it.
2. **Quoting a thickness without its velocity assumption.** The trade-off
   coefficient here is 1.5, so the velocity error is *amplified* into the
   thickness.
3. **Ignoring the near offsets.** They are what fixes the top-layer velocity;
   without them the whole column drifts.
4. **Treating the layer stack as uniform.** 2A thins and thickens, the dyke
   complex has an anisotropic fabric, and layer 3 is neither homogeneous nor a
   single unit.
5. **Cycle skipping.** A one-period pick error is often bigger than the signal
   being measured, and it biases thicknesses systematically rather than randomly.
6. **Forgetting the water-path correction.** With a surface source, the water
   column contributes roughly $2\times$ the water depth divided by
   $1.5\ \mathrm{km\,s^{-1}}$ of travel time to every pick, and its error enters
   the crustal solution directly.
7. **Summing layer uncertainties as if they were independent.** They are
   correlated by the recursion; Monte Carlo, not quadrature, is the correct
   propagation.

## Related modules
- [15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](01-mid-ocean-ridges.md) —
  where this structure is created, and why layer 2A is porous.
- [15-03-03 Marine Subduction Zones, Trenches and Accretionary Prisms](03-subduction-zones-marine.md) —
  where the hydrated crust is consumed.
- [15-04-02 Gas Hydrates](../04-seafloor-mapping-and-habitats/02-gas-hydrates.md) —
  the same velocity-based inference of a solid phase in pore space.
- [06-09-01 The Reflection Principle](../../06-seismology/09-reflection-seismology/01-reflection-principle.md) —
  the reflection counterpart of the refraction problem solved here.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  how porosity and hydration become velocity.
- [15-02-06 Ocean-Bottom Seismology and OBS Networks](../02-marine-geophysics-methods/06-obn-ocean-bottom-seismology.md) —
  the instrument that makes seafloor-source geometry possible.
