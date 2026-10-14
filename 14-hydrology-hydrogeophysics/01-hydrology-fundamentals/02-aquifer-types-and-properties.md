---
id: 14-01-02
title: "Aquifers, Porosity, Permeability and Storativity"
level: intermediate
prereqs: ["14-01-01", "04-06-04", "05-04-01"]
tags: [hydrology, hydrogeophysics, porosity, permeability, storativity, specific-yield, kozeny-carman]
---

# Aquifers, Porosity, Permeability and Storativity

An aquifer is a rock that both **stores** and **transmits** water. Those are two
independent properties, and the vocabulary of hydrogeology is a list of ways of
being specific about them: total porosity, effective porosity, specific yield,
specific retention, hydraulic conductivity, intrinsic permeability,
transmissivity, storativity. This lesson derives each one from the other where a
derivation exists, states the model constant where none does, and quantifies the
sensitivities that decide which measurement a project should buy.

**All models and data in this module are SYNTHETIC.** The rocks, grain sizes,
compressibilities and layer stacks below are invented teaching values. No named
formation, core sample or published table is used. The only numbers not from this
module's own demonstration are stated physical constants of water and of the
darcy, listed with units where they are used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** total porosity from bulk and grain density and **verify** it against
   a saturated mass balance.
2. **Distinguish** total porosity, effective porosity, specific yield and specific
   retention, and **state** the inequality that orders them.
3. **Derive** specific storage as $S_s = \rho_w g(\alpha + n\beta)$ and **explain**
   why a confined aquifer's storativity is three orders of magnitude smaller than
   an unconfined one's.
4. **Convert** between hydraulic conductivity and intrinsic permeability, and
   **state** which fluid properties the conversion requires.
5. **Apply** the Kozeny–Carman relation to predict $K$ from grain size and
   porosity, and **quantify** its sensitivity to each input.
6. **Compute** horizontal and vertical effective conductivities of a layered
   aquifer and **explain** why they differ by orders of magnitude.
7. **Estimate** the volume of water a stated area can actually yield under a
   stated head change.

## Prerequisites

- [14-01-01 The Hydrologic Cycle and Water Balance](01-hydrologic-cycle.md) —
  storage change and residence time, the quantities this lesson explains.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)
  — the geological classification of aquifers and aquitards.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md)
  — how porosity enters the density and velocity of a rock, which is what most
  geophysical methods actually measure.

---

## 1. Intuition: two properties, and the pairs they come in

Take a dry sand and a dry clay. Both can have $30\%$ of their volume as pore space.
Dry, both are "porous". Pour water on them: the sand yields nearly all of it to a
well; the clay yields almost none. The difference is not how much water the rock
contains but how easily it moves, and how much of it drains.

That gives two axes, and each axis has a pair of numbers that beginners routinely
confuse:

| Axis | Pairs to keep apart |
|---|---|
| how much is stored | total porosity $n$ vs **effective** porosity $n_e$; storativity $S$ vs specific yield $S_y$ |
| how easily it flows | hydraulic conductivity $K$ (rock **and** fluid) vs intrinsic permeability $k$ (rock only) |

Add the scale question — a thin layer of very permeable gravel contributes little
water if it is 0.5 m thick — and you need **transmissivity** $T = Kb$, which is
conductivity integrated over the saturated thickness $b$.

Every geophysical method in
[module 14-02](../02-hydrogeophysics-methods/README.md) is a bet about which of
these numbers it can see. Electrical methods see the pore fluid and its
connectivity; seismic velocities see the frame and the fluid's bulk modulus;
gravity and NMR see mass and pore water directly. Knowing this table is what makes
a geophysical survey designable.

## 2. Precise definitions

**Total porosity** — the fraction of bulk volume that is not solid:

$$n = \frac{V_{\text{pores}}}{V_{\text{bulk}}} = 1 - \frac{\rho_b}{\rho_s},
\qquad \text{(dimensionless)},$$

where $\rho_b$ is bulk density and $\rho_s$ grain (particle) density, in the same
units (the ratio is dimensionless, which is why g cm$^{-3}$ may be used freely).

**Effective porosity** $n_e \le n$ — the fraction of bulk volume that is
*connected* and can conduct. Dead-end pores and water bound in clay interlayers
are excluded.

**Specific yield** $S_y$ — the volume of water that drains from a unit area of
unconfined aquifer per unit drop of the water table, as a fraction. It is the
storage coefficient of an unconfined aquifer:

$$S_y = \frac{V_{\text{drained}}}{A\,\Delta h}.$$

**Specific retention** $S_r$ — the water that *does not* drain, held by surface
tension as films and in fine pores. For a sandy material,

$$S_r = n_e - S_y, \qquad S_y + S_r = n_e \le n.$$

**Specific storage** $S_s$ [m$^{-1}$] — the volume released from a unit volume of
confined aquifer per unit decline in head. **Storativity** $S$ (also called the
storage coefficient) is the depth-integrated value:

$$S = S_s\,b.$$

**Hydraulic conductivity** $K$ [m s$^{-1}$] and **intrinsic permeability** $k$
[m$^2$] are related by

$$K = \frac{k \rho_w g}{\mu_w} \quad \Longleftrightarrow \quad
k = \frac{K \mu_w}{\rho_w g},$$

with $\rho_w$ the fluid density, $\mu_w$ its dynamic viscosity, and $g$ gravity.

**Transmissivity** $T = K b$ [m$^2$ s$^{-1}$] is the depth-integrated conductivity
of the saturated interval.

## 3. Derivations

### 3.1 Porosity from densities

For a sample of bulk volume $V$ and dry mass $m_s$: $m_s = \rho_s (1-n) V$ and
$m_s = \rho_b V$. Eliminating $m_s$ gives $\rho_b = \rho_s(1-n)$, hence

$$n = 1 - \frac{\rho_b}{\rho_s}.$$

This is exact for a two-phase (solid + pore) rock. It becomes an *interpretation*
the moment one of the two densities is assumed — which is why the grain density
must be stated: a sandstone whose $\rho_s$ is really $2.65\ \mathrm{g\,cm^{-3}}$
but is assumed to be $2.71$ has its porosity wrong by
$0.06/2.71 \approx 0.022$, i.e. 2.2 porosity units, which for $n = 0.20$ is an 11%
relative error.

### 3.2 Why the two storage mechanisms differ by orders of magnitude

Consider a unit bulk volume of confined aquifer. Head declines by $\Delta h$. The
effective stress on the framework rises by $\Delta\sigma' = \rho_w g \Delta h$
(because the pore-pressure drop is $\rho_w g \Delta h$ and total stress is
unchanged over the timescale of interest).

Two things happen:

1. **The framework compresses** by the fractional amount
   $\alpha \Delta \sigma' = \alpha \rho_w g \Delta h$, where $\alpha$ is the
   vertical compressibility of the drained rock skeleton [Pa$^{-1}$].
2. **The water expands** by $\beta \Delta \sigma'$ per unit *pore* volume, so by
   $n \beta \rho_w g \Delta h$ per unit bulk volume, where $\beta$ is the
   compressibility of water [Pa$^{-1}$].

Both effects deliver water. Adding them per unit bulk volume per unit head:

$$\boxed{\;S_s = \rho_w g\left(\alpha + n\beta\right).}$$

Now put in synthetic numbers. With $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$g = 9.81\ \mathrm{m\,s^{-2}}$, $n = 0.25$, $\alpha = 1.0 \times 10^{-9}\
\mathrm{Pa^{-1}}$ (stiff sandstone), and $\beta = 4.4 \times 10^{-10}\
\mathrm{Pa^{-1}}$ (water at $20\ ^\circ\mathrm{C}$ — a standard property of water):

$$\alpha + n\beta = 1.0 \times 10^{-9} + 0.25(4.4 \times 10^{-10})
= 1.110 \times 10^{-9}\ \mathrm{Pa^{-1}},$$
$$S_s = 1000 \times 9.81 \times 1.110 \times 10^{-9}
= 1.089 \times 10^{-5}\ \mathrm{m^{-1}}.$$

For $b = 30\ \mathrm{m}$, $S = S_s b = 3.27 \times 10^{-4}$. Compare the
unconfined value for the same rock, $S = S_y = 0.20$: a ratio of

$$\frac{0.20}{3.27 \times 10^{-4}} = 612.$$

Three orders of magnitude, from the same grains. The unconfined case releases water
by **emptying pores** (the water is replaced by air); the confined case releases
water by **compressing the rock and expanding the water**, at essentially constant
saturation. This is not a small correction — it is a different physics, and it is
the reason a pumping test in a confined aquifer needs long times and small
drawdowns to see anything at all.

Note the asymmetry in what each mechanism responds to: $\alpha$ is a property of
the *framework*, so a fractured rock with a stiff matrix can have a small $\alpha$
while having a large $K$; and $\beta$ scales with $n$, so a high-porosity rock gains
a little from water expansion but loses much more from weak frame stiffness.

### 3.3 Conductivity to permeability

Darcy's law written with fluid properties exposed is

$$q = -\frac{k}{\mu_w}\left(\nabla p - \rho_w \mathbf{g}\right)
= -K \nabla h,$$

so that $K = k\rho_w g/\mu_w$. With $\mu_w = 1.002 \times 10^{-3}\
\mathrm{Pa\,s}$ (water at $20\ ^\circ\mathrm{C}$), $\rho_w = 1000\
\mathrm{kg\,m^{-3}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$:

$$K = 1.0 \times 10^{-4}\ \mathrm{m\,s^{-1}}
\;\Longrightarrow\;
k = \frac{1.0 \times 10^{-4} \times 1.002 \times 10^{-3}}{1000 \times 9.81}
= 1.021 \times 10^{-11}\ \mathrm{m^2}.$$

Using the definition $1\ \mathrm{darcy} = 9.869233 \times 10^{-13}\ \mathrm{m^2}$
(exact), $k = 10.35\ \mathrm{D}$. Because $\mu_w$ falls by about a factor of 1.9
between $5\ ^\circ\mathrm{C}$ and $30\ ^\circ\mathrm{C}$, **the same rock has a
$K$ that changes by a factor of 1.9 with temperature** while $k$ does not. Any
$K$ quoted without a temperature (or a viscosity) is incomplete at the 2× level,
which matters in geothermal and permafrost problems and is negligible in most
shallow water-supply work — say which one you are doing.

### 3.4 Kozeny–Carman: $K$ from grain size and porosity

Model the pores as a bundle of capillaries of diameter $d$ through which
Hagen–Poiseuille flow occurs. The flux per unit area, corrected for the fraction
of area occupied by pores, for tortuosity, and for the pore shape, is proportional
to $d^2$, to the driving gradient, and inversely to $\mu$. Converting the result to
permeability and collecting the geometric factors into one constant $c_{\text{KC}}$:

$$K = \frac{\rho_w g}{\mu_w}\cdot\frac{d^{2} n^{3}}{c_{\text{KC}}\,(1-n)^{2}},
\qquad c_{\text{KC}} = 180 \text{ for a circular-capillary bundle}.$$

The two powers carry all the physical content: the $d^{2}$ is Poiseuille, the
$n^{3}/(1-n)^{2}$ is the area fraction times the tortuosity correction. The constant
is **not** physics; it is a calibration, and values from about 10 to 200 are
defensible depending on pore shape. State it.

With $n = 0.2830$ and $d = 0.50\ \mathrm{mm} = 5.0 \times 10^{-4}\ \mathrm{m}$:

$$K = \frac{1000 \times 9.81}{1.002 \times 10^{-3}}
\cdot \frac{(5.0 \times 10^{-4})^{2}(0.2830)^{3}}{180\,(1 - 0.2830)^{2}}
= 9.790 \times 10^{6}
\cdot \frac{2.5 \times 10^{-7} \times 0.022665}{180 \times 0.514089}
= 5.995 \times 10^{-4}\ \mathrm{m\,s^{-1}}.$$

Sensitivity, measured in the demonstration: $K \propto d^{2}$, so a 10% error in
grain diameter is a 21% error in $K$; and at this porosity a 10% error in $n$
changes $K$ by **44%**. Porosity is the more dangerous input, and it is also the
one that is usually estimated from a log rather than measured.

Inverting the same relation for the grain size that gives
$K = 1.0 \times 10^{-4}\ \mathrm{m\,s^{-1}}$ at $n = 0.2830$:

$$d = \sqrt{\frac{K\,\mu_w\,c_{\text{KC}}(1-n)^{2}}{\rho_w g\,n^{3}}}
= 2.04 \times 10^{-4}\ \mathrm{m} = 0.204\ \mathrm{mm}.$$

### 3.5 Layered media: two different effective conductivities

For flow **parallel** to the layers, the head gradient is common to all layers and
the fluxes add, giving the thickness-weighted arithmetic mean:

$$K_h = \frac{\sum_i b_i K_i}{\sum_i b_i}.$$

For flow **perpendicular** to the layers, the flux is common and the head losses
add, giving the harmonic mean:

$$K_v = \frac{\sum_i b_i}{\sum_i b_i/K_i}.$$

Since the harmonic mean is dominated by the smallest term and the arithmetic mean
by the largest, a single thin clay layer can make $K_h/K_v$ enormous. For the
synthetic stack in the demonstration (2 m sand at $5 \times 10^{-4}$,
5 m silty sand at $2 \times 10^{-5}$, 1 m clay at $1 \times 10^{-9}$, 3 m sand at
$4 \times 10^{-4}\ \mathrm{m\,s^{-1}}$, total $b = 11$ m):

$$K_h = \frac{2(5\!\times\!10^{-4}) + 5(2\!\times\!10^{-5}) + 1(10^{-9}) + 3(4\!\times\!10^{-4})}{11}
= 2.09 \times 10^{-4}\ \mathrm{m\,s^{-1}},$$
$$K_v = \frac{11}{\frac{2}{5\times10^{-4}} + \frac{5}{2\times10^{-5}}
+ \frac{1}{10^{-9}} + \frac{3}{4\times10^{-4}}}
= 1.10 \times 10^{-8}\ \mathrm{m\,s^{-1}},$$
$$\frac{K_h}{K_v} = 1.9 \times 10^{4}.$$

A factor of 19,000 in the same rock package, decided by the direction of flow. The
$1\ \mathrm{m}$ clay layer is $9\%$ of the thickness and controls $K_v$ entirely.
Transmissivity with $K_h$ is $T = K_h b = 2.30 \times 10^{-3}\ \mathrm{m^2\,s^{-1}}
= 198.7\ \mathrm{m^2\,d^{-1}}$.

## 4. Worked example — what a synthetic aquifer actually contains

**Synthetic sandstone**: $\rho_b = 1.90\ \mathrm{g\,cm^{-3}}$,
$\rho_s = 2.65\ \mathrm{g\,cm^{-3}}$, $n_e = 0.25$, $S_y = 0.20$, saturated
thickness $b = 20\ \mathrm{m}$, area $A = 1\ \mathrm{km^2}$.

**Step 1 — total porosity.**
$$n = 1 - \frac{1.90}{2.65} = 1 - 0.7170 = 0.2830.$$

**Step 2 — water in place.** Per unit area, the water volume is $n b$; over
$1\ \mathrm{km^2}$,
$$V_{\text{in place}} = n A b = 0.2830 \times 10^{6}\ \mathrm{m^2} \times 20\ \mathrm{m}
= 5.66 \times 10^{6}\ \mathrm{m^3}.$$

**Step 3 — drainable water.** The useful volume is set by specific yield, not
porosity:
$$V_{\text{drainable}} = S_y A b = 0.20 \times 10^{6} \times 20
= 4.00 \times 10^{6}\ \mathrm{m^3}.$$
The difference, $1.66 \times 10^{6}\ \mathrm{m^3}$, is water the rock holds. A
resource statement that used $n$ instead of $S_y$ would overstate the yield by
$42\%$ — and it is a common mistake in exactly this form.

**Step 4 — head change needed.** If the aquifer is confined with
$S = 3.27 \times 10^{-4}$ instead, the volume released for a 10 m head decline is
$$V = S A \Delta h = 3.27 \times 10^{-4} \times 10^{6} \times 10
= 3.27 \times 10^{3}\ \mathrm{m^3},$$
about $1220\times$ less than the drainage of Step 3. The word "aquifer" alone tells
you nothing about which number applies; the **confinement** does.

## 5. Python demonstration

`code/aquifer_types_and_properties_demo.py` computes every number above and prints
labelled results with units. It:

1. computes porosity for three synthetic rocks and verifies it against a
   saturated mass balance (agreement to $1.7 \times 10^{-16}$);
2. tabulates effective porosity, specific yield and specific retention;
3. builds $S_s$ from $\alpha$ and $n\beta$ for three frameworks and computes the
   storativity ratio ($612\times$);
4. converts $K$ to $k$ over five decades of $K$, in m$^2$ and darcy;
5. applies Kozeny–Carman over grain sizes from 0.05 to 2 mm, inverts it for a
   target $K$, and measures the sensitivity to $d$ and $n$;
6. computes $K_h$, $K_v$, the anisotropy ratio and $T$ for a four-layer stack;
7. tabulates the water released per unit area for four storage cases.

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aquifer_types_and_properties_demo.py
```

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| porosity, specific yield, retention, storativity | $n, S_y, S_r, S$ | – | volume per volume |
| bulk and grain density | $\rho_b, \rho_s$ | kg m$^{-3}$ | ratio is dimensionless |
| compressibility | $\alpha, \beta$ | Pa$^{-1}$ | $\rho_w g \alpha$ is m$^{-1}$ |
| specific storage | $S_s$ | m$^{-1}$ | $\rho_w g \alpha$: kg m$^{-3}$ · m s$^{-2}$ · Pa$^{-1}$ |
| conductivity | $K$ | m s$^{-1}$ | |
| intrinsic permeability | $k$ | m$^2$ | |
| transmissivity | $T$ | m$^2$ s$^{-1}$ | $K b$ |
| viscosity | $\mu_w$ | Pa s | $k\rho_w g/\mu_w$ must give m s$^{-1}$ |

Check the one that is easy to get wrong: $k = K\mu_w/(\rho_w g)$ has units
$\mathrm{m\,s^{-1}} \cdot \mathrm{Pa\,s} / (\mathrm{kg\,m^{-3}} \cdot
\mathrm{m\,s^{-2}}) = \mathrm{m^2}$. If your answer is in m s$^{-1}$, you forgot
to divide by $\rho_w g$.

## 7. Assumptions and regime of validity

1. **Two-phase porosity is exact; the densities are not.** $n = 1 -
   \rho_b/\rho_s$ assumes all solid is one mineral with a known density. A
   clay-bearing rock has a lower effective $\rho_s$ and its density porosity is
   biased. State the assumed mineralogy.
2. **Elastic, recoverable storage.** $S_s = \rho_w g(\alpha + n\beta)$ assumes small
   strain, constant compressibilities, and no permanent compaction. In a
   subsiding aquifer or a compacting clay, the released volume exceeds this
   prediction and the deformation is partly irrecoverable.
3. **$S_s \ll n/b$ in confined units.** The derivation neglects flow to the
   neighbouring layers (leakage) and assumes the release is instantaneous relative
   to the observation window. A leaky aquifer's apparent storativity is larger.
4. **Kozeny–Carman requires a clean, well-sorted, uncemented, single-mineral
   granular medium.** Clay, cement, dual porosity and fractures all break it, and
   each does so in the direction of under-predicting $K$. Treat it as an
   order-of-magnitude predictor, and state $c_{\text{KC}}$.
5. **$k$ is scale-dependent.** A laboratory plug of a fractured or
   heterogeneous rock measures a matrix or a single-fracture permeability, not the
   formation's. Field-scale $K$ from a pumping test may exceed plug values by
   orders of magnitude. The comparison is a statement about scale, not an error.
6. **Arithmetic and harmonic means assume perfect layering.** Real aquifers have
   discontinuous layers; the effective conductivity then depends on the geometry
   and on connectivity, and lies between the two means.

## Mastery checkpoint

A synthetic core reports $\rho_b = 2.05\ \mathrm{g\,cm^{-3}}$ with assumed
$\rho_s = 2.67\ \mathrm{g\,cm^{-3}}$; the measured $K = 2.0 \times 10^{-5}\
\mathrm{m\,s^{-1}}$ at $20\ ^\circ\mathrm{C}$. The unit is $15\ \mathrm{m}$ thick
and drains over $1\ \mathrm{km^2}$.

**(a)** Compute $n$. **(b)** Given $n_e = 0.20$ and $S_y = 0.15$, compute $S_r$ and
state the inequality that orders $n$, $n_e$, $S_y$. **(c)** Compute the water in
place and the drainable volume per km$^2$, in m$^3$. **(d)** Convert $K$ to $k$ in
m$^2$ and in darcy. **(e)** Use Kozeny–Carman with $c_{\text{KC}} = 180$ to
estimate the grain diameter, and say whether the result is consistent with the
assumed $K$ being a *matrix* value. **(f)** A colleague quotes $S = 0.15$ for this
unit under 30 m of head decline; what do you ask?

## Common pitfalls

1. **Reporting porosity as yield.** Only $S_y$ drains by gravity; using $n$
   overstates the resource (by $42\%$ in Section 4).
2. **Using one storativity for both confinement regimes.** A confined and an
   unconfined aquifer with the same rock differ by three orders of magnitude in
   storage.
3. **Quoting $K$ without fluid properties.** $\mu_w$ changes $K$ by a factor of
   1.9 between 5 and 30 $^\circ$C; $k$ does not change at all.
4. **Applying Kozeny–Carman to a clay or a cemented rock.** It fails in the
   direction of under-prediction, silently.
5. **Treating a lab permeability as the formation permeability.** Scale and
   fractures are not measurement noise.
6. **Assuming isotropy.** The synthetic stack's $K_h/K_v$ is $1.9 \times 10^{4}$;
   a single layer can control vertical flow completely.
7. **Forgetting that porosity from a density log needs a matrix density.** The
   grain-density assumption usually dominates the porosity error budget.

## Related modules

- [01 The Hydrologic Cycle and Water Balance](01-hydrologic-cycle.md) — the
  fluxes whose storage term these properties quantify.
- [03 Hydraulic Head and Darcy's Law](03-hydraulic-head-darcy.md) — the derivation
  of the flow law that $K$ appears in, and the validity condition for it.
- [04 Well Hydraulics and Pumping Tests](04-well-hydraulics.md) — how $K$, $S$ and
  $T$ are measured in the field.
- [02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) — which
  method sees which property in this lesson.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md)
  and [05-04-07 Electrical Properties of Rock](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md)
  — how these properties enter the geophysical observables.

## Code and exercises

- Demonstration:
  [`code/aquifer_types_and_properties_demo.py`](code/aquifer_types_and_properties_demo.py)
- Exercises: [`exercises/02-aquifer-types-and-properties-exercises.md`](exercises/02-aquifer-types-and-properties-exercises.md)
- Worked solutions: [`exercises/02-aquifer-types-and-properties-solutions.md`](exercises/02-aquifer-types-and-properties-solutions.md)
