---
id: 10-04-02
title: "Shear-Wave Velocity Modelling and Site Classification"
level: graduate
prereqs: ["10-04-01", "06-01-02", "06-10-04"]
tags: [gpr, near-surface, geotechnical, shear-wave-velocity, site-classification, stiffness, liquefaction]
---

# Shear-Wave Velocity Modelling and Site Classification

**All models and data in this module are SYNTHETIC.** The velocity profiles,
densities, footing, shaking parameters and uncertainties below are chosen teaching
values. No site, borehole, foundation or earthquake is described from measurement.
The empirical relations used as relations (the liquefaction screening procedure,
the modulus-reduction form, the site-class boundaries of the building codes) are
attributed and labelled; every number they produce here comes from SYNTHETIC input.

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a shear-wave velocity profile from measurements with different
   resolutions, and **compute** the $V_{S30}$ each construction implies.
2. **Derive** the travel-time-average definition of $V_{S30}$, **prove** that the
   weight of a layer is its travel time, and **explain** why an arithmetic average
   is not a velocity average.
3. **Convert** a profile into $G_{\max} = \rho V_s^2$ and $E = 2G(1+\nu)$, and
   **state** exactly which part of that conversion is exact and which is an
   assumption.
4. **Compute** the operative modulus at a working strain with a modulus-reduction
   relation, and **show** the factor by which using $G_{\max}$ changes a settlement
   prediction.
5. **Derive** the cyclic stress ratio from a peak shear-stress ratio and the
   equivalent-uniform-cycle convention, and **compute** a factor of safety against
   liquefaction from both a penetration index and a shear velocity.
6. **Assign** a code site class from a $V_{S30}$, and **state** when the class is
   decided by the data rather than by the ground.
7. **Propagate** a velocity uncertainty into a $V_{S30}$, a class, a stiffness and
   a factor of safety, and **report** a probability rather than a value.

## Prerequisites

- [10-04-01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](01-spt-cpt-crosshole.md)
  — where the penetration and velocity measurements come from, and what an index
  parameter is.
- [06-01-02 P and S Waves](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md)
  — the shear modulus, the shear speed and Poisson's ratio.
- [06-10-04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](../../06-seismology/10-refraction-and-near-surface-seismology/04-masw-sasw.md)
  — the non-invasive route to the same profile, and its own resolution limit.

## 1. Intuition: the deliverable is a construction

A geotechnical engineer asks for a shear-wave velocity profile because they want
stiffness: how much will this settle, how will it shake, will it liquefy. The
profile is the intermediary, and it is *built* — from borehole interval
measurements, a surface-wave dispersion curve, a refraction model, and sometimes a
converted penetration index. Each source has a different vertical resolution, a
different lateral footprint and a different error structure.

The demonstration makes the consequence concrete. Three defensible constructions of
the same SYNTHETIC site give

$$V_{S30} = 408.5,\quad 317.9,\quad 318.5\ \mathrm{m\,s^{-1}},$$

a spread of $28.5\%$ — and the first falls in one code site class and the other two
in the next. The ground did not change. What changed is what each method weights:
a travel-time average is dominated by the slow layers, a dispersion curve is
dominated by the layers its wavelengths sample, and a coarse refraction model
cannot represent a thin soft layer at all.

Two further honest difficulties follow, and they are the content of this lesson:

- **the answer depends on the strain you will load the soil to.** $G_{\max}$ is the
  infinitesimal-strain modulus; a footing at working load sees a modulus two to four
  times smaller, and the settlement scales inversely.
- **a screening calculation is not a prediction.** A liquefaction factor of safety
  computed from a profile carries the profile's uncertainty, which in the
  demonstration is $\pm 0.39$ on a central value of $0.96$ — a probability of
  triggering, not a yes/no.

## 2. Precise definitions

| Quantity | Symbol | Definition | Unit |
|---|---|---|---|
| time-average shear velocity | $V_{S30}$ | $30/\sum_i (h_i/V_{s,i})$ over $0$–$30\ \mathrm{m}$ | m/s |
| small-strain shear modulus | $G_{\max}$ | $\rho V_s^{2}$ | Pa |
| elastic modulus | $E$ | $2G(1+\nu)$ | Pa |
| shear strain | $\gamma$ | displacement gradient | — |
| reference strain | $\gamma_r$ | $\tau_{\max}/G_{\max}$ | — |
| cyclic stress ratio | $CSR$ | $0.65(\sigma_v/\sigma'_v)(a_{\max}/g)r_d$ | — |
| cyclic resistance ratio | $CRR$ | resistance at $15$ uniform cycles | — |
| magnitude scaling factor | $MSF$ | $10^{2.24}/M^{2.56}$ | — |
| factor of safety | $FS$ | $(CRR/MSF)/CSR$ | — |
| site class | A–F | a code band of $V_{S30}$ | — |

The $V_{S30}$ definition is not an average of velocities in the arithmetic sense:
it is $30\ \mathrm{m}$ divided by the total travel time, which is what makes it a
physical quantity (an average *speed*) rather than a bookkeeping number.

## 3. Derivations

### 3.1 $V_{S30}$ and its weights

If the vertical travel time through a layered column to $30\ \mathrm{m}$ is
$T = \sum_i h_i/V_{s,i}$, then

$$V_{S30} = \frac{30}{T} = \frac{\sum_i h_i}{\sum_i h_i/V_{s,i}}.$$

Treating $V_{S30}$ as a function of the layer velocities and differentiating,

$$\frac{\partial \ln V_{S30}}{\partial \ln V_{s,i}}
= \frac{h_i/V_{s,i}}{\sum_j h_j/V_{s,j}} = \frac{t_i}{T} \equiv w_i,$$

the layer's fractional travel time. *Numerical check.* For the demonstration's
borehole profile,

| layer (m) | $h$ (m) | $V_s$ (m/s) | $h/V_s$ (ms) | $w_i$ |
|---|---|---|---|---|
| $0$–$2$ | $2$ | $175$ | $11.43$ | $0.156$ |
| $2$–$4$ | $2$ | $245$ | $8.16$ | $0.111$ |
| $4$–$8$ | $4$ | $320$ | $12.50$ | $0.170$ |
| $8$–$12$ | $4$ | $430$ | $9.30$ | $0.127$ |
| $12$–$20$ | $8$ | $520$ | $15.38$ | $0.209$ |
| $20$–$30$ | $10$ | $600$ | $16.67$ | $0.227$ |

$T = 73.44\ \mathrm{ms}$, so $V_{S30} = 30/0.07344 = 408.5\ \mathrm{m\,s^{-1}}$
(the demonstration prints $408.5$). The top $2\ \mathrm{m}$ — $6.7\%$ of the
column — carries $15.6\%$ of the weight; the deepest $10\ \mathrm{m}$, a third of
the column, carries $22.7\%$. **The slow layers dominate**, and a soft layer
*below* $30\ \mathrm{m}$ contributes nothing at all — the most common way a
$V_{S30}$ is under-estimated in practice is a profile that stops at the base of the
borehole.

### 3.2 Stiffness from a velocity: the exact part

For a linear elastic, isotropic medium,

$$G = \rho V_s^{2}, \qquad E = 2G(1+\nu), \qquad
M = \rho V_p^{2}, \qquad \nu = \frac{V_p^{2}-2V_s^{2}}{2(V_p^{2}-V_s^{2})}.$$

These are algebra, not correlation. *Numerical check.* $\rho = 1850\
\mathrm{kg\,m^{-3}}$, $V_s = 245\ \mathrm{m\,s^{-1}}$:

$$G = 1850(245)^{2} = 1.1104\times10^{8}\ \mathrm{Pa} = 111.0\ \mathrm{MPa},$$

$$E = 2(111.0)(1.30) = 288.7\ \mathrm{MPa}\quad(\nu = 0.30).$$

The demonstration prints $111.0$ and $288.7$. The assumptions are: the medium is
elastic and isotropic, and $\rho$ and $\nu$ are known. **Given those, no empirical
step has been taken.** That is the difference between this number and anything
derived from a blow count.

### 3.3 The modulus that a structure actually loads

A soil is not linear, and the modulus falls with strain. A widely used algebraic
form is the hyperbolic (Hardin–Drnevich) family,

$$\frac{G}{G_{\max}} = \frac{1}{1+\gamma/\gamma_r}, \qquad
\gamma_r = \frac{\tau_{\max}}{G_{\max}},$$

where $\tau_{\max}$ is a shear strength and $\gamma_r$ the strain at which the
modulus has halved. *Numerical check* ($\rho = 1850\ \mathrm{kg\,m^{-3}}$,
$\tau_{\max} = 60\ \mathrm{kPa}$):

| $V_s$ (m/s) | $G_{\max}$ (MPa) | $\gamma_r$ | $G/G_{\max}$ at $\gamma = 10^{-3}$ | $G$ (MPa) |
|---|---|---|---|---|
| $175$ | $56.7$ | $1.06\times10^{-3}$ | $0.514$ | $29.1$ |
| $245$ | $111.0$ | $5.40\times10^{-4}$ | $0.351$ | $39.0$ |
| $320$ | $189.4$ | $3.17\times10^{-4}$ | $0.241$ | $45.6$ |
| $430$ | $342.1$ | $1.75\times10^{-4}$ | $0.149$ | $51.0$ |
| $520$ | $500.2$ | $1.20\times10^{-4}$ | $0.107$ | $53.6$ |
| $600$ | $666.0$ | $9.01\times10^{-5}$ | $0.083$ | $55.0$ |

Read the last two columns together: **a factor of $3.4$ in $V_s$ becomes a factor
of $1.9$ in the operative modulus**, because the stiffer soil also has the smaller
reference strain and therefore degrades more at the same $\gamma$. The
modulus-reduction curve is where the *form* is a model and the coefficients are
empirical; the demonstration's coefficients are SYNTHETIC teaching values, and the
lesson's point survives any of them: the operative modulus is a strong function of
strain, and the strain is a design input.

### 3.4 Settlement: the operative modulus in a design formula

For a rigid circular footing of radius $a$ on an elastic half-space under uniform
pressure $q$, the classic solution is a punch problem whose settlement is

$$\delta = \frac{\pi}{2}\,\frac{q\,a\,(1-\nu^{2})}{E}.$$

For a flexible uniformly loaded area the centre settlement is
$2qa(1-\nu^2)/E$, so the rigid footing settles
$(\pi/2)/2 = 0.785$ of that — the well-known ratio, and the internal check that the
constant is right.

*Numerical check.* $q = 150\ \mathrm{kPa}$, a $2.0\ \mathrm{m}$ square footing, so
$a = B/\sqrt{\pi} = 1.1284\ \mathrm{m}$ (equal area), $\nu = 0.30$:

| layer | modulus used | $E$ (MPa) | $\delta$ (mm) |
|---|---|---|---|
| $V_s = 245\ \mathrm{m\,s^{-1}}$ | $G_{\max}$ | $288.7$ | $0.84$ |
| $V_s = 245\ \mathrm{m\,s^{-1}}$ | $G$ at $\gamma = 10^{-3}$ | $101.3$ | $2.39$ |
| $V_s = 320\ \mathrm{m\,s^{-1}}$ | $G_{\max}$ | $492.5$ | $0.49$ |
| $V_s = 320\ \mathrm{m\,s^{-1}}$ | $G$ at $\gamma = 10^{-3}$ | $118.5$ | $2.04$ |

**Using $G_{\max}$ under-predicts the settlement by a factor of $2.9$ to $4.2$** in
the demonstration. Note also the inversion that follows: with the operative moduli
the two layers give almost the same settlement ($2.39$ and $2.04\ \mathrm{mm}$),
whereas with $G_{\max}$ they differ by a factor of two. At design strain, the
*stiffer* layer is not much stiffer — which is exactly the fact that the
small-strain profile hides.

### 3.5 Liquefaction screening

The pseudo-static argument: during shaking with peak horizontal acceleration
$a_{\max}$, the peak cyclic shear stress on a horizontal plane at depth $z$ is

$$\tau_{\mathrm{peak}} = \sigma_v\,\frac{a_{\max}}{g}\,r_d,$$

where $r_d \le 1$ accounts for the deformability of the column (a rigid column
would have $r_d = 1$). Normalising by the effective stress gives the **cyclic
stress ratio**

$$CSR = \frac{\tau_{\mathrm{peak}}}{\sigma'_v}=\frac{\sigma_v}{\sigma'_v}
\frac{a_{\max}}{g}\,r_d.$$

An earthquake is not a train of equal cycles, so the irregular history is replaced
by an equivalent number of uniform cycles at a stress level conventionally taken as
$0.65$ of the peak:

$$CSR_{7.5} = 0.65\,\frac{\sigma_v}{\sigma'_v}\,\frac{a_{\max}}{g}\,r_d.$$

**The $0.65$ is a convention, not a measurement**, and it embodies a judgement
about which uniform history does the same damage as the irregular one. The depth
factor used here is the simplified form $r_d = 1-0.00765z$ for $z \le 9.15\
\mathrm{m}$ (an empirical fit), and the resistance is the NCEER form

$$CRR_{7.5} = \frac{1}{34-(N_1)_{60cs}} + \frac{(N_1)_{60cs}}{135}
+ \frac{50}{[10(N_1)_{60cs}+45]^{2}} - \frac{1}{200},$$

$$MSF = \frac{10^{2.24}}{M^{2.56}}, \qquad
FS = \frac{CRR_{7.5}/MSF}{CSR_{7.5}}.$$

The alternative, velocity-based route normalises the velocity to
$\sigma'_v = 100\ \mathrm{kPa}$ with an adopted exponent,

$$V_{s1} = V_s\left(\frac{100}{\sigma'_v}\right)^{0.25},$$

and evaluates a fitted resistance curve at $V_{s1}$ (the Andrus–Stokoe form).
**The exponent $0.25$ is an adopted empirical value**, not a derivation; the
square-root form $C_N$ of the SPT in the previous lesson is a different fit to the
same physical effect.

*Measured table* (SYNTHETIC profile, $a_{\max} = 0.30\,g$, $M = 7.0$ so
$MSF = 1.193$):

| $z$ (m) | $\sigma_v$ (kPa) | $\sigma'_v$ (kPa) | $CSR$ | $(N_1)_{60cs}$ | $CRR_N$ | $FS_N$ | $V_{s1}$ (m/s) | $CRR_V$ | $FS_V$ |
|---|---|---|---|---|---|---|---|---|---|
| $2.0$ | $36.0$ | $36.0$ | $0.192$ | $8.0$ | $0.096$ | $0.42$ | $316.3$ | $0.179$ | $0.78$ |
| $4.0$ | $76.0$ | $56.4$ | $0.255$ | $12.0$ | $0.131$ | $0.43$ | $369.3$ | $0.269$ | $0.88$ |
| $6.0$ | $116.0$ | $76.8$ | $0.281$ | $16.0$ | $0.170$ | $0.51$ | $341.9$ | $0.222$ | $0.66$ |
| $8.0$ | $156.0$ | $97.1$ | $0.294$ | $20.0$ | $0.215$ | $0.61$ | $433.1$ | $0.387$ | $1.10$ |
| $10.0$ | $196.0$ | $117.5$ | $0.300$ | $24.0$ | $0.273$ | $0.76$ | $413.0$ | $0.348$ | $0.97$ |

The two routes disagree by a factor of about two at $2\ \mathrm{m}$ ($FS_N = 0.42$
against $FS_V = 0.78$) and cross over at depth. They are fitted to different
datasets and are not calibrated against each other; the honest use is to apply both,
report both, and treat a disagreement as a statement about confidence rather than
as a contradiction to be resolved by choosing one.

## 4. Physical interpretation

- **A profile is a construction with a resolution.** The vertical resolution is the
  layer spacing of the model, the lateral footprint is the array length (for surface
  waves), and the depth of investigation is the longest wavelength. Two methods
  with different resolutions cannot agree in detail, and the difference is not
  error to be averaged away.
- **$V_{S30}$ weights the slow layers.** $15.6\%$ of the weight sits in the top
  $3\%$ of the column in the demonstration; anything below $30\ \mathrm{m}$ is
  invisible to it by definition.
- **A code class is a decision boundary, not a measurement.** A profile within
  $42$–$48\ \mathrm{m\,s^{-1}}$ of a boundary (the demonstration's numbers) has its
  class decided by the measurement error: the Monte Carlo puts $92.9\%$ of the
  probability in class C and $7.1\%$ in D.
- **Strain is a design input.** The same profile gives settlements differing by a
  factor of three to four depending on the modulus chosen, and the choice is a
  statement about the strain level under working load.
- **Screening is probabilistic.** With $FS = 0.96 \pm 0.39$, the probability of
  $FS<1$ is $0.64$: the useful output is that number, not the central value.

## 5. Worked examples

### Example 1 — $V_{S30}$ from a profile, by hand

From the borehole profile of Section 3.1, $T = 73.44\ \mathrm{ms}$:

$$V_{S30} = \frac{30}{0.07344} = 408.5\ \mathrm{m\,s^{-1}},$$

which falls in the code class $360$–$760\ \mathrm{m\,s^{-1}}$. Suppose instead that
the survey had started $2\ \mathrm{m}$ down, at the base of the topsoil — a
perfectly ordinary thing for a line laid out below a farm track. The travel time
loses the first layer's $11.43\ \mathrm{ms}$, becoming $62.02\ \mathrm{ms}$, and

$$V_{S30} = \frac{30}{0.06202} = 483.7\ \mathrm{m\,s^{-1}},$$

$18\%$ higher, from the same ground and the same instrument. **The top two metres
are worth more to $V_{S30}$ than the bottom ten**, which is why the specification
for a $V_{S30}$ measurement says "from the ground surface" explicitly.

### Example 2 — the settlement factor

$V_s = 245\ \mathrm{m\,s^{-1}}$, $q = 150\ \mathrm{kPa}$, $B = 2.0\ \mathrm{m}$,
$\nu = 0.30$:

$$\delta_{\mathrm{small}} = \frac{\pi}{2}\frac{(150)(1.1284)(1-0.09)}{288.7\times10^{3}}
= \frac{\pi}{2}\cdot\frac{154.04}{288.7\times10^{3}}\ \mathrm{m} = 0.84\ \mathrm{mm},$$

$$\delta_{\mathrm{op}} = 0.84 \times \frac{288.7}{101.3} = 2.39\ \mathrm{mm}.$$

Both numbers are the demonstration's. The second is the one that belongs in a
design check at working load; the first is the one that belongs in a statement about
the soil's small-strain behaviour, for example in a dynamic-response calculation
where the strains really are of order $10^{-6}$.

### Example 3 — from a velocity to a factor of safety

At $z = 8.0\ \mathrm{m}$: $\sigma_v = 156$ kPa, $\sigma'_v = 97.1$ kPa,
$V_s = 430\ \mathrm{m\,s^{-1}}$.

1. $r_d = 1-0.00765(8.0) = 0.9388$.
2. $CSR = 0.65(156/97.1)(0.30)(0.9388) = 0.294$ (the demonstration prints $0.294$).
3. $V_{s1} = 430(100/97.1)^{0.25} = 430(1.02986)^{0.25} = 433.1\ \mathrm{m\,s^{-1}}$.
4. The resistance curve at $V_{s1} = 433.1$ gives $CRR = 0.387$.
5. $FS = (0.387/1.193)/0.294 = 1.10$.

A factor of safety of $1.10$ is *not* a demonstration that the layer will not
liquefy: it is a screening value from an empirical curve, and the demonstration's
Monte Carlo at a nearby depth gives $\pm 0.39$ on a central $0.96$. The
decision-relevant output is the probability.

## 6. Assumptions and regime of validity

1. **The profile is one-dimensional.** A laterally varying site (a buried channel,
  a fill edge) is not represented by a single column, and $V_{S30}$ for such a site
  is an average over the footprint of the measurement, not over the site.
2. **1-D linear elastic half-space response** underlies the settlement formula and
  the site-response concept. Layered, non-linear, and topographic effects are
  additive models, each with its own assumptions.
3. **$G/G_{\max}$ form and coefficients.** The hyperbolic family is a model; the
  coefficients are empirical and material-specific. Using a generic curve is an
  assumption of the same weight as using a generic correlation.
4. **The screening procedure's conventions**: $0.65$ as the equivalent uniform
  ratio, $r_d = 1-0.00765z$, the $7.5$-magnitude reference, the $0.25$ normalisation
  exponent. Changing any of them changes $FS$.
5. **Water table and unit weights.** Every stress in the procedure depends on them;
  they are inputs, not corrections.
6. **The measurement errors are the profile's.** A $V_{S30}$ cannot be more
  accurate than the profile's velocities and thicknesses, and a profile that ends at
  $20\ \mathrm{m}$ cannot include the $20$–$30\ \mathrm{m}$ layers at all.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| velocity | $V_s$, $V_{S30}$, $V_{s1}$ | m/s | length/time |
| travel time | $T$ | s (printed in ms) | $\sum h_i/V_{s,i}$ |
| density | $\rho$ | $\mathrm{kg\,m^{-3}}$ | — |
| modulus | $G$, $E$ | Pa | $\rho V_s^{2}$ |
| stress | $\sigma_v$, $\sigma'_v$, $q$ | kPa | $\mathrm{kN\,m^{-3}}\times\mathrm{m}$ |
| strain | $\gamma$, $\gamma_r$ | — | dimensionless |
| settlement | $\delta$ | m | $q\,a/E \times$ dimensionless |
| ratios | $CSR$, $CRR$, $FS$ | — | stress/stress |

The settlement formula's units repay a check: $q/E$ is dimensionless, $a$ is a
length, so $\delta$ is a length. If an expression for settlement comes out in
$\mathrm{m^2}$ or in $\mathrm{Pa}$, a length or a stress has been misplaced.

## 8. Python demonstration

[`code/shear_wave_velocity_modelling_demo.py`](code/shear_wave_velocity_modelling_demo.py)
prints every number quoted above:

1. three profiles for one site and the $V_{S30}$ each implies ($408.5$, $317.9$,
   $318.5\ \mathrm{m\,s^{-1}}$, a $28.5\%$ spread), with the site class of each;
2. the distance of each $V_{S30}$ from the nearest code boundary;
3. $G_{\max}$, $E$, the reference strain and the modulus reduction at
   $\gamma = 10^{-3}$ for six velocities;
4. settlements with the small-strain and the operative moduli, and the factor
   between them ($2.85$ and $4.16$);
5. the liquefaction table: $CSR$, $CRR$ and $FS$ from both a penetration index and
   a velocity, with the two routes disagreeing by up to a factor of two;
6. two Monte Carlos: the class probability given an $8\%$ velocity uncertainty
   ($92.9\%$ C, $7.1\%$ D) and the distribution of the factor of safety
   ($0.96 \pm 0.39$, $P(FS<1) = 0.641$).

The demo is print-only, uses the fixed seed `20261014`, needs no network, and
exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-shear-wave-velocity-modelling-exercises.md`](exercises/02-shear-wave-velocity-modelling-exercises.md)
and
[`exercises/02-shear-wave-velocity-modelling-solutions.md`](exercises/02-shear-wave-velocity-modelling-solutions.md).

- **★** A three-layer profile: $4\ \mathrm{m}$ at $160$, $10\ \mathrm{m}$ at $240$,
  $16\ \mathrm{m}$ at $420\ \mathrm{m\,s^{-1}}$. Compute $V_{S30}$ and the weight
  of each layer.
- **★★** For $V_s = 300\ \mathrm{m\,s^{-1}}$, $\rho = 1900\
\mathrm{kg\,m^{-3}}$, compute $G_{\max}$ and $E$ ($\nu = 0.35$), then the operative
modulus at $\gamma = 5\times10^{-4}$ with $\tau_{\max} = 50\ \mathrm{kPa}$, and the
settlement of a $2\ \mathrm{m}$ square footing at $120\ \mathrm{kPa}$ with each.
- **★★★** A site has a soft layer at $18$–$24\ \mathrm{m}$ that a $30\ \mathrm{m}$
profile includes and a $20\ \mathrm{m}$ profile does not. Quantify the $V_{S30}$
difference, state the class consequences, and design the measurement that would
settle the question.

## 10. Further reading

- **Hardin, B. O., & Drnevich, V. P. (1972). Shear modulus and damping in soils.
  *Journal of the Soil Mechanics and Foundations Division, ASCE*, 98.** Level:
  research. The hyperbolic modulus-reduction family used in Section 3.3.
- **Seed, H. B., & Idriss, I. M. (1970). *Soil moduli and damping factors for
  dynamic response analyses.* Report EERC 70-10, University of California,
  Berkeley.** Level: research. The origin of the modulus-reduction and depth-factor
  forms used in every simplified site-response calculation.
- **Youd, T. L., et al. (2001). Liquefaction resistance of soils: summary report
  from the 1996 NCEER and 1998 NCEER/NSF workshops. *Journal of Geotechnical and
  Geoenvironmental Engineering*, 127.** Level: reference. The simplified procedure
  of Section 3.5, including the $0.65$ convention and the magnitude scaling factor.
- **Andrus, R. D., & Stokoe, K. H. (2000). Liquefaction resistance of soils from
  shear-wave velocity. *Journal of Geotechnical and Geoenvironmental Engineering*,
  126.** Level: research. The velocity-based resistance curve and the
  $V_{s1}$ normalisation.
- **The current building-code provisions for site classification** (for example the
  NEHRP recommended provisions adopted into the International Building Code, and
  Eurocode 8's ground-type definitions). Level: reference. The class boundaries are
  code definitions and must be quoted from the edition in force, not from a
  secondary summary.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A $24\ \mathrm{m}$ profile has $6\ \mathrm{m}$ at $150$, $8\ \mathrm{m}$ at
> $260$ and $10\ \mathrm{m}$ at $480\ \mathrm{m\,s^{-1}}$ over a half-space of
> $700\ \mathrm{m\,s^{-1}}$. $\rho = 1900\ \mathrm{kg\,m^{-3}}$,
> $\nu = 0.30$. **(a)** Compute $V_{S30}$ for the profile and for a variant in
> which the top layer is omitted (a survey that started at $6\ \mathrm{m}$), and
> state the class of each. **(b)** State the weight of each layer in $V_{S30}$ and
> which layer dominates. **(c)** Compute $G_{\max}$ for the $260\
\mathrm{m\,s^{-1}}$ layer and the operative modulus at $\gamma = 10^{-3}$ with
> $\tau_{\max} = 45\ \mathrm{kPa}$. **(d)** Compute the settlement of a
> $2.5\ \mathrm{m}$ square footing at $180\ \mathrm{kPa}$ with each modulus.
> **(e)** With $a_{\max} = 0.25\,g$, $M = 6.5$ and the water table at $3\
\mathrm{m}$, compute $CSR$ at $6\ \mathrm{m}$ and state what else you would need
> before quoting a factor of safety.

Worked versions of (a)–(d) appear in the
[solutions](exercises/02-shear-wave-velocity-modelling-solutions.md).

## Common pitfalls

1. **Averaging velocities arithmetically.** $V_{S30}$ is $30/\sum(h/V_s)$; the
   arithmetic mean of the demonstration's profile is far larger and has no physical
   meaning.
2. **Letting the profile stop at the borehole base or the array's reach.** Anything
   below the deepest sampled depth is neither measured nor included, and a
   $V_{S30}$ from a $20\ \mathrm{m}$ profile is missing a third of its own
   definition.
3. **Quoting one $V_{S30}$.** The demonstration's three constructions differ by
   $28.5\%$ and fall in different classes.
4. **Using $G_{\max}$ as the design modulus.** The demonstration's settlements
   differ by a factor of $2.9$ to $4.2$.
5. **Treating a code class as a site response.** Two profiles with the same class
   can respond differently; the class is a band, not a measurement.
6. **Reporting a factor of safety without its distribution.** $0.96 \pm 0.39$ is
   the usable statement; $0.96$ is not.
7. **Mixing up the normalisation exponents.** $C_N$ uses a square root (stress to
   the $0.5$), $V_{s1}$ uses the $0.25$ power; they are different fits to different
   measurements and are not interchangeable.

## Related modules

- [10-04 Near-Surface Seismic and Geotechnical Methods](./README.md) — the module
  this lesson belongs to.
- [10-04-01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](01-spt-cpt-crosshole.md)
  — where the velocities and penetration indices come from.
- [06-10-05 Site Characterisation: Vs30 and Site Response](../../06-seismology/10-refraction-and-near-surface-seismology/05-seismic-hazards-site.md)
  — the seismological side of the same number, including the transfer function.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
  — where $a_{\max}$ comes from, and with what probability.
- [10-06 Near-Surface Monitoring and Time-Lapse](../06-nearsurface-monitoring/README.md)
  — repeating a velocity survey to detect change (a rising water table, a
  compaction).

## Code and exercises

| Path | Contents |
|---|---|
| [`code/shear_wave_velocity_modelling_demo.py`](code/shear_wave_velocity_modelling_demo.py) | The six computations of Section 8 |
| [`exercises/02-shear-wave-velocity-modelling-exercises.md`](exercises/02-shear-wave-velocity-modelling-exercises.md) | Graded problems |
| [`exercises/02-shear-wave-velocity-modelling-solutions.md`](exercises/02-shear-wave-velocity-modelling-solutions.md) | Worked solutions |

```bash
cd 10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shear_wave_velocity_modelling_demo.py
```
