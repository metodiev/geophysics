---
id: 14-03-01
title: "Porosity-Permeability and Kozeny-Carman Relations"
level: doctoral
prereqs: ["04-06-04", "05-04-01", "02-06-05", "14-01-02"]
tags: [hydrology, hydrogeophysics, petrophysics, permeability, porosity, kozeny-carman, specific-surface]
---

# Porosity-Permeability and Kozeny-Carman Relations

> **All models and data in this module are SYNTHETIC.** The grain sizes,
> porosities, Kozeny constants and "datasets" below are chosen teaching values.
> No field, core, log or published compilation is quoted as a measurement.

Permeability is the property hydrogeology cares about and geophysics cannot see.
A resistivity or velocity measurement returns a bulk property that responds to
the *volume* of pore space; the flow of water depends on the *geometry* of the
connections between pores. This lesson takes the standard route across that gap —
the capillary-bundle model and the Kozeny–Carman (KC) relation — and then spends
most of its length measuring where the route fails.

The reason to be careful is arithmetic. Permeability spans at least thirteen
orders of magnitude between a clay and a gravel, and it depends on porosity
roughly as the third power. A five per cent relative error in porosity is
therefore a twenty per cent error in permeability before anything else is
counted, and the relation itself carries a fitted constant that can move the
answer by a factor of three. The honest output of a KC calculation is a range
with a stated pore-geometry assumption, not a number.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** total porosity, effective porosity and specific surface, and
   **state** which of them enters a flow law.
2. **Derive** the capillary-bundle permeability
   $k = \phi R_h^{2}/(2\tau)$ from Hagen–Poiseuille and the hydraulic radius, and
   **show** that it is algebraically identical to the Kozeny–Carman form
   $k = \phi^{3}/(2\tau S_0^{2}(1-\phi)^{2})$.
3. **Compute** the Kozeny constant $c_K = 2\tau$ from a sphere-pack geometry and
   **state** the pore-shape assumption it silently carries.
4. **Quantify** the sensitivity of $k$ to porosity, to grain size and to the
   Kozeny constant, and **explain** why porosity alone cannot determine
   permeability.
5. **Convert** intrinsic permeability to hydraulic conductivity with the fluid
   properties stated, and **show** the unit ladder between $\mathrm{m^2}$,
   darcy and $\mathrm{m\,s^{-1}}$.
6. **Demonstrate** KC's failure in clay-bearing and fractured media, and
   **estimate** the misfit factor it produces.
7. **Propagate** a geophysical porosity uncertainty into a permeability
   uncertainty, and **decide** whether the resulting range is narrow enough to
   answer a hydrological question.

## Prerequisites

- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md) —
  Darcy's law, transmissivity, and the aquifer/aquitard distinction.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the density mixing law and the definitions of porosity used here.
- [02-06-05 Flow in Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md) —
  Darcy's law derived as the low-Reynolds-number limit of a viscous flow.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md) —
  the hydrogeological vocabulary this lesson quantifies.

## 1. Intuition: why one number cannot carry permeability

Take two samples with exactly the same porosity, $\phi = 0.25$: a well-sorted
medium sand and a cemented sandstone whose pore space has been reduced to
isolated pockets. Both are one-quarter void. Water flows through the first in
hours and through the second in years, because flow is carried by the *smallest
cross-section along a connected path*, and the second sample has almost no
connected path at all.

Flow is therefore controlled by three things that porosity does not record:

- the **size** of the conduits,
- the **connectedness** of the pore network, and
- the **tortuosity**, the ratio of the actual path length to the straight-line
  distance.

The capillary-bundle model is the smallest model that contains all three. It
imagines the pore space as a set of tubes of some characteristic radius, tortuous
by a factor $\tau$. It is wrong in detail — real pores are not tubes — but it
gets the *scaling* right, and the scaling is what matters: $k \propto d^{2}$,
$k \propto \phi^{3}$ in the dilute limit.

## 2. Definitions

### 2.1 Porosity

$$
\phi = \frac{V_\text{void}}{V_\text{total}}, \qquad
\phi_\text{eff} = \frac{V_\text{connected, mobile}}{V_\text{total}}.
$$

**Total porosity** $\phi$ counts every void, including sealed pores and water
held on clay surfaces that never moves. **Effective porosity** $\phi_\text{eff}$
counts only what can flow. Viscous-flow laws need $\phi_\text{eff}$; electrical
laws (Archie, next lesson) need the connected pore volume, which is usually
closer to $\phi_\text{eff}$ than to $\phi$. In clean sand the two differ by a
point or two; in a clay the difference is most of the porosity, and that gap is
the reason permittivity-style proxies fail in clay-rich media.

### 2.2 Specific surface

The specific surface $S_0$ is the interstitial surface area per unit **grain**
volume,

$$
S_0 = \frac{A_\text{pore wall}}{V_\text{solid}} \qquad (\mathrm{m^{-1}}).
$$

For spheres of diameter $d$, $S_0 = (4\pi r^{2})/(4\pi r^{3}/3) = 3/r = 6/d$.
Small grains mean a large specific surface, and the surface is where the
viscous dissipation happens. This single fact explains why KC needs a grain size
or a specific surface as an input: porosity alone does not supply one.

### 2.3 Permeability and conductivity

Darcy's law in its intrinsic form is

$$
\mathbf{q} = -\frac{k}{\mu}\left(\nabla P - \rho_f \mathbf{g}\right),
$$

with $\mathbf{q}$ the **superficial** (Darcy) velocity in $\mathrm{m\,s^{-1}}$,
$k$ the **intrinsic permeability** in $\mathrm{m^{2}}$, $\mu$ the dynamic
viscosity in $\mathrm{Pa\,s}$. When the driving term is written as a head
gradient the fluid factors collect into the **hydraulic conductivity**

$$
K = \frac{k \rho_f g}{\mu} \qquad (\mathrm{m\,s^{-1}}),
$$

so $K$ is a property of the rock *and* the fluid, while $k$ is a property of the
rock alone. Reporting one without saying which is a common and serious error.

### 2.4 Unit ladder

The two permeability units are related by an exact definition:

$$
1\ \text{darcy} = 9.869233\times10^{-13}\ \mathrm{m^{2}}, \qquad
1\ \text{millidarcy} = 9.869233\times10^{-16}\ \mathrm{m^{2}}.
$$

The demonstration prints the ladder: $1\ \mathrm{m^{2}} = 1.0132\times10^{12}$
darcy. Reservoir petrophysics quotes millidarcy; soil physics quotes
$\mathrm{m\,s^{-1}}$; groundwater hydrology usually quotes $\mathrm{m\,d^{-1}}$.
Keep $k$ in $\mathrm{m^{2}}$ internally and convert at the boundary.

## 3. Derivation: from a bundle of tubes to Kozeny–Carman

**Step 1 — one tube.** Hagen–Poiseuille gives the volume flux through a circular
tube of radius $R$ under a pressure gradient $\nabla P$ along the tube,

$$
Q = \frac{\pi R^{4}}{8\mu}\nabla P .
$$

The mean velocity along the tube is $u = Q/(\pi R^{2}) = R^{2}\nabla P/(8\mu)$.
Written with the **hydraulic radius** $R_h$ of the tube ($R_h = $ area/perimeter
$= R/2$ for a circle), this is

$$
u = \frac{R_h^{2}}{2\mu}\nabla P .
$$

That factor $\tfrac12$ instead of $\tfrac18$ is the entire reason the standard
constant comes out as $5$ rather than $20$.

**Step 2 — the hydraulic radius of a pore network.** The hydraulic radius of the
pore space is its volume divided by the wetted surface:

$$
R_h = \frac{\text{pore volume}}{\text{wetted surface}}
    = \frac{\phi}{S_0(1-\phi)} .
$$

*Check.* With $\phi = 0.25$, $d = 0.20\ \mathrm{mm}$ we have
$S_0 = 6/d = 30000\ \mathrm{m^{-1}}$, wetted surface per bulk volume
$S_0(1-\phi) = 22500\ \mathrm{m^{-1}}$, and $R_h = 0.25/22500
= 1.1111\times10^{-5}\ \mathrm{m}$. The demonstration prints exactly this.

**Step 3 — tortuosity.** Fluid follows a path of length $L_e = \tau L$, so the
gradient along the path is $\nabla P/\tau$ rather than $\nabla P$. The
superficial Darcy velocity is the pore velocity times porosity,
$q = \phi u$:

$$
q = \phi \cdot \frac{R_h^{2}}{2\mu}\cdot\frac{\nabla P}{\tau}
  = \frac{\phi R_h^{2}}{2\tau}\cdot\frac{\nabla P}{\mu}.
$$

**Step 4 — read off $k$.** Comparing with $\mathbf q = -(k/\mu)\nabla P$,

$$
\boxed{\;k = \frac{\phi R_h^{2}}{2\tau}\;}
\qquad\Longrightarrow\qquad
\boxed{\;k = \frac{\phi^{3}}{2\tau\,S_0^{2}(1-\phi)^{2}} .}
$$

Both boxed forms are the same number; the second is the Kozeny–Carman relation.
With $S_0 = 6/d$ it becomes

$$
k = \frac{d^{2}\phi^{3}}{72\,\tau\,(1-\phi)^{2}}
  = \frac{d^{2}\phi^{3}}{180\,(1-\phi)^{2}} \quad \text{when } \tau = 2.5 ,
$$

so the familiar denominator $180$ is $36 \times (2\tau)$ with $\tau = 2.5$:
$36 \times 5 = 180$. Writing $c_K \equiv 2\tau$ gives the compact form

$$
k = \frac{\phi^{3}}{c_K S_0^{2}(1-\phi)^{2}}, \qquad c_K = 2\tau \approx 5 .
$$

The demonstration verifies numerically that the bundle form and the KC form
return the same value to floating-point rounding (a difference of
$1.6\times10^{-27}\ \mathrm{m^{2}}$ on a value of
$6.2\times10^{-12}\ \mathrm{m^{2}}$) and that the same number comes out of
$d^{2}\phi^{3}/(180(1-\phi)^{2})$ — the check that the algebraic rearrangement
from Section 3 was done correctly.

## 4. Interpretation and the meaning of $\tau$ and $c_K$

$\tau$ is not a fitted fudge; it is a geometric ratio. It enters squared because
it dilates the path length ($\tau$) *and* reduces the effective gradient along
the path ($1/\tau$). For an aligned bundle of straight tubes $\tau \to 1$;
for a real sand $\tau \approx \sqrt{2}$ to $\sqrt{3}$; that is why $c_K \approx 5$.

Three practical consequences follow.

- Because $c_K$ is a *shape* factor, it absorbs everything the bundle model
  ignores: non-circular pores, dead ends, constrictions, grain angularity. The
  model cannot distinguish them, so $c_K$ is fitted when data are available and
  assumed otherwise.
- Sphere-pack geometries give a useful calibration. The demonstration computes
  the two exact packings: simple cubic gives $\phi = 1-\pi/6 = 0.47640$ and
  rhombohedral gives $\phi = 1-\pi/(3\sqrt{2}) = 0.25952$. Both are derived from
  geometry, not measured, and both are *higher* than the porosity of a natural
  sand, which is a first hint that real grains are not spheres.
- Because $\tau$ is not measured, a KC estimate should be quoted as a factor,
  not a decimal. The demonstration shows that a $\tau$ range from $1.5$ to $4.0$
  moves $k$ by $0.60\times$ to $1.60\times$ around the $\tau = 2.5$ value.

## 5. Scaling laws and sensitivity

From $k \propto d^{2}\phi^{3}/(1-\phi)^{2}$, two exact statements:

**Grain size.** At fixed porosity, $k \propto d^{2}$ exactly. The demonstration
confirms that $d: 0.10 \to 0.20\ \mathrm{mm}$ multiplies $k$ by $4.0$.

**Porosity.** The porosity factor $f(\phi) = \phi^{3}/(1-\phi)^{2}$ has

$$
\frac{\mathrm{d}\ln k}{\mathrm{d}\phi}
= \frac{3}{\phi} + \frac{2}{1-\phi} .
$$

At $\phi = 0.25$ this is $12 + 2.667 = 14.667$ per unit porosity, so an absolute
porosity error of $\pm 0.01$ is a permeability error of $\pm 14.7\%$. The
demonstration prints $7.3\%$, $14.7\%$ and $29.3\%$ for $\delta\phi = 0.005,
0.010, 0.020$.

The full porosity table from the demonstration ($d = 0.20\ \mathrm{mm}$,
$\tau = 2.5$) is:

| $\phi$ | $k$ ($\mathrm{m^{2}}$) | $k$ (mD) | ratio to $\phi = 0.20$ |
|---|---|---|---|
| 0.10 | $2.743\times10^{-13}$ | 278.0 | 0.099 |
| 0.15 | $1.038\times10^{-12}$ | 1051.8 | 0.374 |
| 0.20 | $2.778\times10^{-12}$ | 2814.6 | 1.000 |
| 0.25 | $6.173\times10^{-12}$ | 6254.6 | 2.222 |
| 0.30 | $1.224\times10^{-11}$ | 12407.1 | 4.408 |
| 0.35 | $2.255\times10^{-11}$ | 22849.8 | 8.118 |
| 0.40 | $3.951\times10^{-11}$ | 40029.6 | 14.222 |

Doubling porosity from $0.20$ to $0.40$ multiplies permeability by $14.2$ — the
concrete meaning of "third power".

## 6. Worked example 1 — the reference KC number

**Problem.** A synthetic clean sand has $\phi = 0.250$ and a mean grain diameter
$d = 0.200\ \mathrm{mm}$. Compute $S_0$, $R_h$ and $k$ with $\tau = 2.5$, and
report $k$ in $\mathrm{m^{2}}$, darcy and millidarcy.

**Solution.** All quantities are lengths, so work in metres throughout:
$d = 2.00\times10^{-4}\ \mathrm{m}$.

$$
S_0 = \frac{6}{d} = \frac{6}{2.00\times10^{-4}} = 3.00\times10^{4}\ \mathrm{m^{-1}} .
$$

$$
R_h = \frac{\phi}{S_0(1-\phi)}
     = \frac{0.250}{3.00\times10^{4}\times0.750}
     = 1.1111\times10^{-5}\ \mathrm{m}.
$$

$$
k = \frac{\phi R_h^{2}}{2\tau}
  = \frac{0.250 \times (1.1111\times10^{-5})^{2}}{5.0}
  = \frac{0.250 \times 1.2346\times10^{-10}}{5.0}
  = 6.173\times10^{-12}\ \mathrm{m^{2}} .
$$

Converting:
$k = 6.1728\times10^{-12}/9.869233\times10^{-13} = 6.2546$ darcy
$= 6254.6$ millidarcy. The demonstration prints $6.172840\times10^{-12}$,
$6.2546\ \mathrm{D}$ and $6254.6\ \mathrm{mD}$.

**Interpretation.** Six darcy is a clean, well-sorted sand. Quote it as
"$6.2\times10^{-12}\ \mathrm{m^{2}}$ assuming $\tau = 2.5$ and spherical grains
of $0.20\ \mathrm{mm}$", never as "the permeability".

## 7. Worked example 2 — conductivity, and an ambiguity that does not go away

**Problem.** (a) Convert the permeability above to hydraulic conductivity for
water at $20\ ^\circ\mathrm{C}$ ($\rho_f = 998.2\ \mathrm{kg\,m^{-3}}$,
$\mu = 1.002\times10^{-3}\ \mathrm{Pa\,s}$, $g = 9.80665\ \mathrm{m\,s^{-2}}$).
(b) Two synthetic samples are reported to have
$k = 1.0\times10^{-12}\ \mathrm{m^{2}}$. One has $\phi = 0.20$, the other
$\phi = 0.30$. What grain sizes does KC require?

**Solution (a).**

$$
K = \frac{k\rho_f g}{\mu}
  = \frac{6.1728\times10^{-12}\times998.2\times9.80665}{1.002\times10^{-3}}
  = 6.0305\times10^{-5}\ \mathrm{m\,s^{-1}} .
$$

In the units used by hydrogeologists,
$K = 6.0305\times10^{-5}\times86400 = 5.210\ \mathrm{m\,d^{-1}}$. The
demonstration prints $6.0305\times10^{-5}\ \mathrm{m\,s^{-1}}$ and
$5.2104\ \mathrm{m\,d^{-1}}$, and also prints the ratio
$K/k = 9.769\times10^{6}\ \mathrm{s^{-1}\,m^{-1}}$ at $20\ ^\circ\mathrm{C}$,
which is all you need for any other rock.

**Solution (b).** Invert $k = d^{2}\phi^{3}/(180(1-\phi)^{2})$ for $d$:

$$
d = \sqrt{\frac{180\,k\,(1-\phi)^{2}}{\phi^{3}}} .
$$

For $\phi = 0.20$: $d = \sqrt{180\times10^{-12}\times0.64/0.008}
= \sqrt{1.44\times10^{-8}} = 1.200\times10^{-4}\ \mathrm{m} = 0.120\ \mathrm{mm}$.

For $\phi = 0.30$: $d = \sqrt{180\times10^{-12}\times0.49/0.027}
= \sqrt{3.267\times10^{-9}} = 5.716\times10^{-5}\ \mathrm{m} = 0.0572\ \mathrm{mm}$.

The demonstration prints $0.1200\ \mathrm{mm}$ and $0.0572\ \mathrm{mm}$ for the
same $k$. **A factor of two in grain size compensates a ten-point porosity
difference.** This is the non-uniqueness of the porosity–permeability relation in
its simplest form: the measurement fixes one number, and the relation needs two.

## 8. Where KC fails

The demonstration constructs a synthetic "clayey sand" whose generator is
different from KC: a fraction of the pore space, $\phi_\text{clay} =
\min(0.06, 0.35\phi)$, is microporous clay that carries no flow, so the flow
porosity is $\phi_f = \phi - \phi_\text{clay}$. KC, applied to $\phi$ as if the
medium were clean, then over-predicts:

| $\phi$ | $\phi_f$ | $k_\text{true}$ (mD) | $k_\text{KC}$ (mD) | ratio |
|---|---|---|---|---|
| 0.15 | 0.098 | 256.2 | 1051.8 | 4.11 |
| 0.20 | 0.140 | 835.4 | 2814.6 | 3.37 |
| 0.25 | 0.190 | 2353.9 | 6254.6 | 2.66 |
| 0.30 | 0.240 | 5389.0 | 12407.1 | 2.30 |
| 0.35 | 0.290 | 10893.9 | 22849.8 | 2.10 |

The over-prediction ranges from $2.1\times$ to $4.1\times$ while the porosity
itself is only a few points different from the flow porosity. KC cannot see clay,
because clay enters not through $\phi$ but through (i) a large $S_0$, (ii)
water bound on surfaces, and (iii) a different conduction mechanism entirely.

The failure modes you must state before using KC are:

1. **Clay- and silt-rich media.** $S_0$ is dominated by the fine fraction, not by
   the sand grains, and the bound-water layer is immobile. KC over-predicts.
2. **Fractured rock.** Flow is in apertures of tens of micrometres occupying
   $\sim1\%$ of the volume. Using $\phi = 0.01$ in KC gives a permeability orders
   of magnitude too low, because $S_0$ of a fracture set is not $6/d$.
3. **Very high porosity.** As $\phi \to 1$ the $(1-\phi)^{2}$ denominator drives
   $k$ to infinity, which is unphysical (a suspension does not have infinite
   permeability). KC is only sane for $\phi \lesssim 0.45$.
4. **Diagenesis and cementation.** The pore-size distribution, not just $\phi$,
   changes. Two rocks with the same $\phi$ can differ by $10^{3}$ in $k$.
5. **Anisotropy.** KC returns a scalar. A layered or fractured medium needs the
   tensor $\mathbf k$.

## 9. Assumptions and regime of validity

State these every time you quote a KC number.

**Fluid and flow.** Newtonian fluid of constant viscosity; single phase;
saturated; laminar; no inertial (Forchheimer) term; no slip at the pore wall; the
no-slip bound-water layer is ignored. KC is invalid near a pumping well where
velocities are high and the local Reynolds number is not small.

**Pore geometry.** A bundle of tubes of a single characteristic radius; a
tortuosity $\tau$ that is constant and independent of $\phi$; a specific surface
$S_0$ that is known (normally from a grain size, which assumes spheres). For
these reasons $c_K$ is a *fitted* constant in practice, and honest practice is to
write KC as a scaling law $k = \phi^{3}/(c_K S_0^{2}(1-\phi)^{2})$ and quote the
$c_K$ you used.

**Scale.** Darcy's law and KC are continuum statements: the representative volume
must contain many pores. A single fracture or a gravel lens violates this, and no
porosity average fixes it.

**What KC does *not* claim.** It does not predict $k$ from a geophysical
measurement. It predicts $k$ from $\phi$ *and* a length scale. The geophysical
measurement supplies $\phi$, or a proxy for it, and stays silent about the length
scale. That silence is the subject of lesson 04.

## 10. From a geophysical porosity to a permeability

Suppose resistivity data, inverted through Archie (lesson 02), give
$\phi = 0.25 \pm 0.012$. Pushing that through KC by Monte Carlo — the calculation
is in
[`code/geophysical_proxy_relations_demo.py`](./code/geophysical_proxy_relations_demo.py),
and it is the same propagation used in Section 10 of lesson 04 — gives:

| $\sigma_\phi$ | $\sigma_\phi/\phi$ | median $k$ ($\mathrm{m^{2}}$) | relative sd of $k$ |
|---|---|---|---|
| 0.012 | 4.8% | $6.1696\times10^{-12}$ | 17.5% |
| 0.025 | 10.0% | $6.1795\times10^{-12}$ | 36.7% |
| 0.050 | 20.0% | $6.1543\times10^{-12}$ | 72.1% |

The relative spread of $k$ is $3.65\times$ the relative spread of $\phi$,
exactly as $3/\phi + 2/(1-\phi) = 14.667$ times $\phi = 0.25$ predicts. And the
uncertainty is *only* the porosity part: the grain size, the specific surface and
$c_K$ are all still assumed. A survey that reports $k = 6\times10^{-12}\
\mathrm{m^{2}}$ from resistivity has published a number whose real uncertainty is
a factor of two before geology is even discussed.

The demonstration also shows the skew: because $k(\phi)$ is convex, the
distribution of $k$ has its mean $1.2\%$ above its median even for a modest
$4.8\%$ porosity spread. Reporting $k$ at the mean porosity is a defensible
point summary; reporting it as a median is more accurate; reporting a range is
honest.

## 11. Python demonstration

[`code/porosity_permeability_relations_demo.py`](./code/porosity_permeability_relations_demo.py)
prints, in order: the unit ladder; specific surfaces and the two exact sphere
packings; the bundle derivation checked against KC term by term; $k$ versus
$\phi$; $k$ versus $d$; the non-uniqueness table of Section 7; the sensitivity to
$\tau$; the $k \to K$ conversion; the clay failure table of Section 8; and the
error amplification of Section 10.

```bash
cd 14-hydrology-hydrogeophysics/03-petrophysics-hydrology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python porosity_permeability_relations_demo.py
```

Every number printed carries its unit and its status (standard definition,
derived value, or synthetic model input).

## 12. Exercises

Graded problems for this lesson are in
[`exercises/01-porosity-permeability-relations-exercises.md`](./exercises/01-porosity-permeability-relations-exercises.md),
with arithmetic shown in the
[worked solutions](./exercises/01-porosity-permeability-relations-solutions.md).

## Mastery checkpoint

Answer without notes.

> A synthetic aquifer has $\phi = 0.22$ and a mean grain diameter
> $d = 0.15\ \mathrm{mm}$. **(a)** Compute $S_0$, $R_h$ and the KC permeability
> for $\tau = 2.5$, and state every assumption in one sentence. **(b)** Convert
> to hydraulic conductivity for water at $20\ ^\circ\mathrm{C}$ and report it in
> $\mathrm{m\,d^{-1}}$. **(c)** Give two other $(\phi, d)$ pairs that produce the
> same permeability, and say what additional measurement would break the
> ambiguity. **(d)** The porosity is known only to $\pm 0.01$. Compute the
> resulting permeability range. **(e)** The same rock is found to contain 5%
> clay. Predict the direction and approximate size of the KC error and say why.

## Common pitfalls

1. **Quoting permeability without the pore-geometry assumption.** KC without a
   stated $\tau$ (or $c_K$) and a stated $S_0$ is not reproducible.
2. **Using total porosity where effective porosity belongs.** In clay-rich media
   this alone can be a factor of ten.
3. **Confusing permeability and hydraulic conductivity.** They differ by
   $\rho_f g/\mu$, which is $9.769\times10^{6}\ \mathrm{s\,m^{-1}}$ for water at
   $20\ ^\circ\mathrm{C}$ — and by much more for a gas.
4. **Reporting $k$ beyond the model's range.** KC diverges as $\phi \to 1$ and
   collapses for fractured rock.
5. **Treating the third power as a curiosity.** It is the amplification factor
   $3/\phi + 2/(1-\phi)$; at $\phi = 0.25$ a one-point porosity error is a
   fifteen per cent permeability error.
6. **Forgetting the unit of $d$.** $S_0 = 6/d$ needs $d$ in metres. Millimetres
   give a permeability $10^{6}$ times wrong.

## Related modules

- [02 Archie's Law and Saturation Estimation](02-archie-and-saturation.md) —
  where the porosity in Section 10 would come from.
- [03 Seismic Velocity vs Saturation and Gassmann](03-seismic-velocity-saturation.md) —
  a second, independent bulk property that also responds to pore fluid.
- [04 Building Geophysical Proxies for Hydrological Properties](04-geophysical-proxy-relations.md) —
  the systematic version of the error budget begun here.
- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  Darcy's law, storativity and well hydraulics in full.
- [Module 14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) —
  the surveys that supply the porosity.
- [Module 05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md) —
  bounds, effective media and the same warnings from the other direction.
- [Module 09-01 Electrical Properties of the Earth](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md) —
  the conduction mechanisms behind the resistivity-to-porosity step.
