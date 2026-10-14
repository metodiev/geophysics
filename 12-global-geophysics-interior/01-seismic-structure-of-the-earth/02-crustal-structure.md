---
id: 12-01-02
title: "Crustal Structure and Continental vs Oceanic Crust"
level: advanced
prereqs: ["12-01-01", "06-02-02", "05-04-01", "06-08-01"]
tags: [global-geophysics, earth-interior, crustal-structure, moho, isostasy, refraction, poisson-ratio]
---

# Crustal Structure and Continental vs Oceanic Crust

> **All models and data in this module are SYNTHETIC.** The two-layer refraction
> model, the continental and oceanic columns, the densities and the gravity
> target in this lesson are all chosen teaching values. No survey, station,
> borehole or published measurement is used, and the interface names ("Moho",
> "basement") are conventional labels.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the head-wave travel-time equation, the critical distance and the
   crossover distance for a two-layer refraction, and **invert** an intercept
   time for layer thickness.
2. **Quantify** how a random pick error becomes a depth uncertainty, and how a
   *systematic* velocity error becomes a much larger depth bias.
3. **Compute** Poisson's ratio from $v_p/v_s$ and state what it does and does not
   indicate about crustal composition.
4. **Compare** a continental and an oceanic column of the same total structure
   and **explain** why the same vertical travel time yields wildly different
   depths under different velocity assumptions.
5. **Derive** the Airy isostatic root and **compute** the crustal-thickness
   changes required by topography and by ocean depth.
6. **Explain** the gravity equivalence problem — one anomaly, infinitely many
   bodies — and name the observable that resolves it.
7. **State** the depth-velocity trade-off precisely and **report** a Moho depth
   as conditional on a stated velocity model.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the layered parametrisation this lesson takes as given.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  refraction and head waves.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  why velocities differ between rock types at all.
- [06-08-01 Receiver Functions: Deconvolution and Ps Conversions](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  the converted-phase estimate used in Section 8.

## 1. The crust, and why its thickness is not one number

The crust is the outermost compositional shell of the Earth, separated from the
mantle by a first-order jump in $v_p$ from roughly 6–7 to roughly 8
$\mathrm{km\,s^{-1}}$. That jump is the **Moho**, and the two words that matter
are "roughly". The Moho is a *boundary defined by a velocity jump*, so:

- where the jump is gradational, the Moho is defined by a convention (for
  instance, the depth at which $v_p$ first exceeds a stated threshold);
- where $v_p$ never reaches the mantle value (as in some thinned or heavily
  intruded crust), the Moho does not exist as a first-order feature at all.

Two consequences run through this entire lesson. First, **a Moho depth is
meaningless without a velocity model and a definition.** Second, the methods that
measure it — refraction, vertical reflection, converted phases, gravity — weight
velocity and depth differently, so they do *not* agree unless the model is
consistent. Reporting one number as "the" crustal thickness is therefore an
overclaim unless the method is stated.

The point of this lesson is not that crustal structure is unknowable. It is that
the information is in the *disagreements* between methods, and in the way each
method's answer moves when its assumption is changed.

## 2. Refraction: the head-wave solution

### 2.1 The travel-time equation

Consider a layer of thickness $H$ and velocity $v_1$ over a half space of
velocity $v_2 > v_1$. A ray that strikes the interface at the critical angle
$\sin i_c = v_1/v_2$ (measured from the vertical) is refracted along the
interface and radiates back to the surface. Its travel time at horizontal offset
$x$ is the sum of three legs — down, along, up:

$$T_\text{head}(x)
= \underbrace{\frac{2H}{v_1\cos i_c}}_{\text{down and up}}
+ \underbrace{\frac{x - 2H\tan i_c}{v_2}}_{\text{along the interface}},
$$

and because only the part of the offset not consumed by the two inclined legs is
travelled at $v_2$, the terms rearrange to

$$T_\text{head}(x) = \frac{x}{v_2} + 2H\left(\frac{1}{v_1\cos i_c}
- \frac{\tan i_c}{v_2}\right)
= \frac{x}{v_2} + \frac{2H\sqrt{v_2^{2} - v_1^{2}}}{v_1 v_2}
= \frac{x}{v_2} + 2H\sqrt{\frac{1}{v_1^{2}} - \frac{1}{v_2^{2}}}.$$

The three forms are algebraically identical (use
$\cos i_c = \sqrt{v_2^2-v_1^2}/v_2$ and
$\tan i_c = v_1/\sqrt{v_2^2-v_1^2}$); the middle one is the easiest to
differentiate, the last the easiest to compute. The **intercept time**

$$t_i = \frac{2H\sqrt{v_2^{2}-v_1^{2}}}{v_1 v_2}
\quad\Longrightarrow\quad
\boxed{\;H = \frac{t_i\,v_1 v_2}{2\sqrt{v_2^{2}-v_1^{2}}}.\;}$$

Note that $t_i$ is *proportional to $H$* at fixed velocities: a 3 % intercept
error is exactly a 3 % thickness error. All the leverage on $H$ comes from the
velocities, not from the intercept.

The direct arrival is $T_\text{direct} = x/v_1$. Three distances organise the
record section:

- the **critical distance**, the smallest offset at which the head wave exists,
  $x_c = 2H\tan i_c = 2H v_1/\sqrt{v_2^2 - v_1^2}$;
- the **crossover distance**, where the head wave overtakes the direct wave,
  $x_\times = t_i/(1/v_1 - 1/v_2)$;
- beyond that, the head wave is the first arrival.

### 2.2 The numbers for the demonstration's model

With $v_1 = 6.00$, $v_2 = 8.00\ \mathrm{km\,s^{-1}}$ and $H = 30.0\ \mathrm{km}$:

| quantity | value |
|---|---|
| critical distance $x_c$ | 68.03 km |
| crossover distance $x_\times$ | 158.75 km |
| intercept time $t_i$ | 6.614 s |
| thickness from the intercept | 30.000 km |

The first-arrival assignment is worth seeing explicitly, because it is what a
survey actually records:

| $x$ (km) | $T_\text{direct}$ (s) | $T_\text{head}$ (s) | first arrival |
|---|---|---|---|
| 10 | 1.667 | 7.864 | direct |
| 68 | 11.333 | 15.114 | direct |
| 150 | 25.000 | 25.364 | direct |
| 159 | 26.500 | 26.489 | **head** |
| 250 | 41.667 | 37.864 | head |

The head wave *exists* from 68 km but only *arrives first* beyond 159 km. An
analyst who fits a straight line to "the second arrival" below the crossover will
measure the direct wave and get a nonsense mantle velocity — which is exactly the
mistake the next section's inversion is designed to avoid.

## 3. Noise, bias, and the depth-velocity trade-off

### 3.1 Random error

The demonstration simulates 300 repeat surveys of 40 offsets with an independent
Gaussian pick error of $\sigma = 20\ \mathrm{ms}$, fits the direct branch for
$v_1$, the head branch for $v_2$ and $t_i$, and inverts for $H$:

| quantity | true | mean of 300 estimates | standard deviation |
|---|---|---|---|
| $v_1$ (km s$^{-1}$) | 6.000 | 6.0014 | 0.0161 |
| $v_2$ (km s$^{-1}$) | 8.000 | 7.9997 | 0.0046 |
| $H$ (km) | 30.000 | 30.011 | 0.201 |

Read this as a statement about *which parameters the data constrain*: the
mantle velocity is recovered 3.5 times more precisely than the layer velocity,
because it comes from the slope of a 21-point branch, while $H$ comes from a
single fitted intercept. The depth uncertainty is 0.7 % — for a 20 ms pick error,
which is optimistic for field data.

The correlation between the recovered $H$ and $v_1$ across the 300 realisations
is $+0.915$. That is not noise: it is the trade-off, visible in the scatter.
When a noisy pick makes $v_1$ look high, the inversion also makes $H$ look large,
because the two must jointly reproduce the same intercept.

### 3.2 Systematic error, and why it is worse

Now hold the picks fixed and give the analyst a wrong $v_1$:

| error in $v_1$ | recovered $H$ (km) | error |
|---|---|---|
| −5 % | 26.87 | −3.13 km (−10.4 %) |
| 0 | 30.00 | 0 |
| +5 % | 33.81 | +3.81 km (+12.7 %) |

A 5 % systematic velocity error produces a **13 % depth error**, twenty times the
1σ random error of Section 3.1. More averaging will not fix it, because it is not
random. This is the depth-velocity trade-off, and it is the same trade-off that
the receiver function encounters in
[06-08-01](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md);
the refraction version is easier to derive because the geometry is simple.

Why is the depth more sensitive than the time? Because $t_i$ is proportional to
$H/\sqrt{v_2^2-v_1^2}$, and near $v_1 \to v_2$ that denominator is small and
strongly curved. The layer thickness and the velocity contrast are being
separated by a *small difference of squares*.

## 4. $v_p/v_s$, Poisson's ratio and composition

For an isotropic elastic solid,

$$\nu = \frac{3K - 2G}{2(3K + 2G)}
= \frac{\left(v_p/v_s\right)^2 - 2}{2\left[\left(v_p/v_s\right)^2 - 1\right]}.$$

The demonstration evaluates it over the range of $k = v_p/v_s$ that crustal rocks
occupy:

| $k = v_p/v_s$ | $\nu$ | $\mathrm{d}\nu/\mathrm{d}k$ |
|---|---|---|
| 1.60 | 0.1795 | 0.658 |
| 1.70 | 0.2354 | 0.476 |
| 1.75 | 0.2576 | 0.411 |
| 1.80 | 0.2768 | 0.359 |
| 1.90 | 0.3084 | 0.279 |

At $k = 1.75$, a 1 % error in $k$ moves $\nu$ by 0.0072. The mapping is smooth,
monotonic and **not very sensitive**: a composition change that moves $\nu$ from
0.24 to 0.28 requires $k$ to change by 0.1, i.e. 6 %, which is a large
seismological error budget. The practical consequences:

- $\nu$ is a *weak* discriminator, useful mainly for separating saturated porous
  rock (high $\nu$) from dry or quartz-rich rock (low $\nu$);
- it is also contaminated by anisotropy and by the presence of fluids, both of
  which change the apparent $v_s$;
- and it assumes that the $v_p$ and $v_s$ estimates sample the same volume, which
  is a strong assumption when one comes from a P refraction and the other from an
  S refraction with different raypaths.

## 5. A continental and an oceanic column

The demonstration builds two SYNTHETIC columns and computes vertical travel
times:

| continental | thickness (km) | $v_p$ (km s$^{-1}$) | $t$ (s) |
|---|---|---|---|
| sediment | 2.0 | 3.00 | 0.667 |
| upper crust | 15.0 | 6.00 | 2.500 |
| lower crust | 18.0 | 6.80 | 2.647 |
| **total** | **35.0** | (harmonic mean 6.0202) | **5.814** |

| oceanic | thickness (km) | $v_p$ (km s$^{-1}$) | $t$ (s) |
|---|---|---|---|
| water | 4.0 | 1.50 | 2.667 |
| sediment | 1.0 | 2.00 | 0.500 |
| basalt | 1.5 | 4.50 | 0.333 |
| gabbro | 3.5 | 6.20 | 0.565 |
| **total** | **10.0** | (harmonic mean 2.4603) | **4.065** |

Now convert each total time to a depth using two different velocities:

| column | conversion velocity (km s$^{-1}$) | depth (km) | error |
|---|---|---|---|
| continental | 6.0202 (correct harmonic mean) | 35.00 | 0.00 |
| continental | 6.0000 | 34.88 | −0.12 |
| oceanic | 2.4603 (correct harmonic mean) | 10.00 | 0.00 |
| oceanic | 6.0000 | 24.39 | **+14.39** |

The last row is the lesson in one line. A 4.065 s vertical travel time through an
*oceanic* column converted with a *continental* velocity gives 24.4 km instead of
10.0 km. In the water layer, $v_p = 1.50\ \mathrm{km\,s^{-1}}$ is a hundred times
slower than nothing in the rock physics: it dominates the time and it has nothing
to do with the crustal velocity. **Any depth conversion must state the column it
assumes.**

This is also why the two crustal types are treated separately in every global
compilation: a single velocity–depth relation cannot represent both, and the
difference is not a small correction.

## 6. Isostasy: why the thickness varies at all

Crustal thickness is not arbitrary. Over long times the crust floats on the
mantle, and Airy's model of local compensation balances the weight of a column.
Take a reference column of crustal thickness $T_0$ and densities $\rho_c$ (crust)
and $\rho_m$ (mantle). Raise the surface by $h$ and require equal pressure at some
deep compensation depth. The extra load $h\rho_c$ must be supported by an extra
root $r$ of crust displacing mantle:

$$h\rho_c = r\left(\rho_m - \rho_c\right)
\quad\Longrightarrow\quad
\boxed{\;r = h\,\frac{\rho_c}{\rho_m - \rho_c}.\;}$$

With $\rho_c = 2.90$ and $\rho_m = 3.30\ \mathrm{g\,cm^{-3}}$ (chosen values), the
scale factor is $\rho_c/(\rho_m-\rho_c) = 7.25$, and the demonstration gives:

| topography $h$ (km) | root $r$ (km) | total thickness (km), $T_0 = 30$ |
|---|---|---|
| 0 | 0 | 30.00 |
| 1 | 7.25 | 38.25 |
| 4 | 29.00 | 63.00 |
| 6 | 43.50 | 79.50 |

Beneath an ocean basin the same balance runs with the water load. The crust must
be *thinner* than the reference by

$$\delta T = d\,\frac{\rho_m - \rho_w}{\rho_m - \rho_c},$$

so with $d = 4\ \mathrm{km}$ of water and $\rho_w = 1.03$:

$$\delta T = 4 \times \frac{3.30 - 1.03}{3.30 - 2.90} = 4 \times 5.675
= 22.70\ \mathrm{km},$$

leaving **7.30 km** of crust beneath that ocean from a 30 km reference. That the
ocean basins are underlain by a thin, dense crust is therefore not an accident of
history: it is what floating requires, once the water load is included. The
arithmetic here is exact; the assumption — *local, complete, Airy compensation* —
is the idealisation, and flexure, thermal support and dynamic topography all
violate it.

## 7. Gravity: identical anomalies, different bodies

A deep buried sphere of radius $a$ and density contrast $\Delta\rho$, centred at
depth $d \gg a$, produces

$$g \approx \frac{4}{3}\pi G\,\Delta\rho\,\frac{a^{3}}{d^{2}}
\qquad (G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}).$$

At fixed $g$ this is one equation in three unknowns $(a, d, \Delta\rho)$, so the
solutions form a **two-parameter family**; fixing $a = d/2$ leaves one. Matching a
10 mGal anomaly with this choice:

| $d$ (km) | $a$ (km) | required $\Delta\rho$ (g cm$^{-3}$) |
|---|---|---|
| 2 | 1.0 | 1.431 |
| 5 | 2.5 | 0.572 |
| 10 | 5.0 | 0.286 |
| 20 | 10.0 | 0.143 |
| 40 | 20.0 | 0.072 |

Every row gives the same anomaly. This is the **fundamental non-uniqueness** of
potential-field data, and it is not a defect of the instrument: gravity sees only
the combination $\Delta\rho\,a^3/d^2$. What breaks the ambiguity is a second
observable that weights the geometry differently — a borehole, a seismic
reflection from the body, a density log, or a *derivative* of the field (higher
derivatives fall off faster with distance and therefore discriminate depth). The
systematic treatment is in
[07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md).

## 8. The same Moho, four methods, four answers

Now the honesty section. Take a single SYNTHETIC structure — Moho at 30.0 km,
$v_p = 6.00$, $v_s = 3.50\ \mathrm{km\,s^{-1}}$ — and ask four methods for the
depth.

**Refraction.** Correct velocities: $H = 30.00\ \mathrm{km}$ (Section 2.2). With
$v_1$ 5 % too high: $H = 33.81\ \mathrm{km}$.

**Converted phases.** For a teleseismic ray with $p = 0.060\ \mathrm{s\,km^{-1}}$
the Ps delay is $\Delta t_{Ps} = H(q_s - q_p) = 3.716\ \mathrm{s}$. Inverting with
different assumed $k = v_p/v_s$:

| assumed $k$ | recovered $H$ (km) | error (km) |
|---|---|---|
| 1.650 | 32.92 | +2.92 |
| 1.700 | 30.60 | +0.60 |
| 1.714 | 30.01 | +0.01 |
| 1.750 | 28.60 | −1.40 |
| 1.800 | 26.84 | −3.16 |

The correct $k$ for this structure is $6.00/3.50 = 1.714$, and only then does the
converted-phase answer match the refraction answer. A 2 % error in $k$ costs
1.4 km of depth.

**Vertical reflection.** A two-way vertical time of 5.814 s (Section 5) converted
with a velocity 10 % too fast gives $1.10 \times 6.0202 \times 5.814 =
38.50\ \mathrm{km}$ — an 8.5 km error, the largest of the four.

**Summary.**

| method | assumed | $H$ (km) |
|---|---|---|
| refraction | correct $v_1$, $v_2$ | 30.00 |
| refraction | $v_1$ +5 % | 33.81 |
| receiver function | $k = 1.714$ (correct) | 30.01 |
| vertical reflection | velocity +10 % | 38.50 |

The four answers agree only when the four assumptions are mutually consistent.
The lesson to carry into the rest of this folder is procedural: **report the
depth with the velocity model attached, and treat a disagreement between methods
as evidence about the assumptions rather than as an error bar.**

## 9. Assumptions and regime of validity

1. **Laterally homogeneous layers.** A dipping Moho or a lateral velocity change
   along the profile maps into apparent thickness and velocity errors that are
   not separable in a single 2-D profile. Crossed profiles or 3-D arrays are
   required.
2. **Sharp, planar interfaces.** A gradational Moho has no intercept time in the
   classical sense; the "arrival" is a gradual onset and $t_i$ is
   definition-dependent.
3. **$v_2 > v_1$ and a half space below.** With a third layer (or a low-velocity
   zone) the two-layer inversion is structurally wrong, not merely noisy.
4. **Isotropy.** Anisotropy of a few per cent maps into both $v_1$ and $H$.
5. **Airy local compensation** for the isostasy of Section 6; the elastic
   thickness of the lithosphere sets the horizontal scale over which a load is
   compensated, and flexural support reduces the root.
6. **Small-amplitude, deep-source gravity** for Section 7; near the body, the
   point-mass approximation fails and the anomaly shape does carry some depth
   information.
7. **Ray theory** for refraction; near the crossover distance the direct and head
   arrivals interfere and amplitudes, not just times, must be considered.

## 10. Worked examples

### Example 1 — intercept time for a crustal refraction

A two-layer model has $v_1 = 6.20\ \mathrm{km\,s^{-1}}$,
$v_2 = 8.10\ \mathrm{km\,s^{-1}}$ and $H = 32\ \mathrm{km}$. Then

$$\sqrt{v_2^2 - v_1^2} = \sqrt{65.61 - 38.44} = \sqrt{27.17}
= 5.2125\ \mathrm{km\,s^{-1}},$$
$$t_i = \frac{2H\sqrt{v_2^2-v_1^2}}{v_1v_2} = \frac{64 \times 5.2125}{50.22}
= 6.643\ \mathrm{s},$$
$$x_c = 2 \times 32 \times \frac{6.20}{5.2125} = 76.13\ \mathrm{km}.$$

A picked $t_i$ of 6.842 s (3 % long) inverts to

$$H = \frac{6.842 \times 6.20 \times 8.10}{2 \times 5.2125}
= \frac{343.66}{10.425} = 32.96\ \mathrm{km},$$

i.e. +0.96 km — exactly the 3 % that was put in, since $H \propto t_i$ at fixed
velocities. Note what that means: **the intercept time cannot correct for a
velocity error.** It propagates one-for-one into the depth.

### Example 2 — the oceanic column with the wrong velocity

From Section 5, the oceanic column's vertical time is 4.065 s. If the analyst
assumes $v_p = 6.20\ \mathrm{km\,s^{-1}}$ (a gabbro velocity, appropriate for only
the deepest 3.5 km of that column):

$$z = v\,t = 6.20 \times 4.065 = 25.20\ \mathrm{km}.$$

The true column is 10.0 km. The error is +15.2 km, and the two largest
contributors are the 4 km of water (2.667 s = 66 % of the total time) and the
1 km of sediment (0.500 s = 12 %). Together, 78 % of the travel time comes from
25 % of the thickness. This is why marine seismic operations use a *known* water
velocity and a *measured* water depth, and treat the rock column separately.

### Example 3 — the isostatic root of a plateau

Consider a SYNTHETIC plateau standing 3.5 km above the reference surface, with
$\rho_c = 2.85$ and $\rho_m = 3.32\ \mathrm{g\,cm^{-3}}$. Then

$$r = 3.5 \times \frac{2.85}{3.32 - 2.85} = 3.5 \times 6.064 = 21.22\ \mathrm{km},$$

so the crust beneath the plateau is $30 + 3.5 + 21.22 = 54.7\ \mathrm{km}$ thick
if the reference is 30 km, and the whole excess (3.5 km of topography plus
21.2 km of root) is a *consequence* of the same mass balance, not two independent
observations. The test of the model is that a seismic crustal-thickness estimate
and the free-air/Bouguer gravity field should give the *same* root; where they do
not, compensation is not local, and that mismatch is the measurement.

## 11. Python demonstration

`code/crustal_structure_demo.py` builds the two-layer refraction, runs the
300-survey inversion, computes Poisson's ratio, the two columns with their depth
conversions, the Airy roots, the gravity equivalence family, and the four-method
comparison. It prints labelled results with units and takes under a second. Run:

```bash
cd 12-global-geophysics-interior/01-seismic-structure-of-the-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python crustal_structure_demo.py
```

## 12. Exercises

Full sets with worked solutions are in
[`exercises/02-crustal-structure-exercises.md`](exercises/02-crustal-structure-exercises.md)
and
[`exercises/02-crustal-structure-solutions.md`](exercises/02-crustal-structure-solutions.md).

- **★** Compute $t_i$, $x_c$, $x_\times$ and $H$ for a given two-layer model.
- **★★** Propagate a 30 ms pick error through the inversion by hand and compare
  with the Monte-Carlo scatter.
- **★★** Compute the Airy root and the crustal thickness beneath a given
  topography and ocean depth.
- **★★★** Design a survey that separates the depth-velocity trade-off, stating
  the observable and the expected improvement.

## Mastery checkpoint

Without notes:

> A refraction profile over a SYNTHETIC crust gives a direct branch with slope
> $0.1580\ \mathrm{s\,km^{-1}}$, a head branch with slope $0.1235\
> \mathrm{s\,km^{-1}}$ and intercept $2.05\ \mathrm{s}$.
> **(a)** Compute $v_1$, $v_2$ and $H$.
> **(b)** Compute the crossover distance and say which branch is the first arrival
> at 60 km.
> **(c)** Compute the Ps delay expected at $p = 0.060\ \mathrm{s\,km^{-1}}$ for
> $k = 1.72$ and the depth from (a).
> **(d)** State one systematic error that would make all three methods disagree in
> the *same* direction, and one that would not.

A worked version of (a)–(c) appears in the lesson-02
[solutions](exercises/02-crustal-structure-solutions.md).

## Common pitfalls

1. **Fitting the second arrival below the crossover.** It is still the direct
   wave; the "mantle velocity" that comes out is really just $v_1$ again.
2. **Quoting a Moho depth with no velocity model.** Section 8: the same structure
   gives 30.0, 33.8, 30.0 or 38.5 km depending on the assumption.
3. **Averaging velocities arithmetically.** The correct average for a travel time
   is the harmonic mean (Section 5); the arithmetic mean always underestimates
   the time.
4. **Treating a gravity anomaly as a shape.** Gravity gives
   $\Delta\rho\,a^3/d^2$ and nothing more; interpreting one anomaly as a body is a
   choice, not a measurement.
5. **Using $\nu$ as a lithology identifier.** A 1 % error in $k$ moves $\nu$ by
   0.007, and anisotropy easily moves it further.
6. **Ignoring the water column in a marine depth conversion.** It carries 66 % of
   the vertical time in the demonstration's oceanic column.
7. **Assuming Airy compensation when flexure is significant.** The root is then
   smaller than the local formula predicts, and the deficit is a measurement of
   the elastic thickness, not a failure of the data.

## 13. Related modules

- [01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the global model that this lesson's crustal structure is inserted into.
- [03 Upper-Mantle Discontinuities at 410 and 660 km](03-upper-mantle-discontinuities.md) —
  the same measurement logic one transition zone deeper.
- [06-08 Receiver Functions and Crustal Structure](../../06-seismology/08-receiver-functions-and-crustal-structure/README.md) —
  the converted-phase method and its own trade-offs.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md) —
  the acquisition and inversion machinery in engineering geometry.
- [07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md) —
  the non-uniqueness of Section 7, with the full toolbox for reducing it.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  where $v_p$, $v_s$ and $\rho$ come from in real rocks.

## Self-assessment checklist

- [ ] I can derive $t_i = 2H/\sqrt{v_2^2-v_1^2}$ and describe what each term is.
- [ ] I can compute the critical and crossover distances and say which arrival is
      first at a given offset.
- [ ] I can turn a Monte-Carlo scatter into a statement about what the data
      constrain.
- [ ] I can explain why a 5 % systematic velocity error beats a 1σ random error.
- [ ] I can compute $\nu$ from $k$ and state the sensitivity.
- [ ] I can compute an Airy root and a water-loaded crustal thickness.
- [ ] I can explain why one gravity anomaly does not define a body.
- [ ] I can report a Moho depth with its conditional velocity model attached.
