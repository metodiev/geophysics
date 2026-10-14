---
id: 11-06-03
title: "Buried Objects, UXO Detection and Clearance"
level: graduate
prereqs: ["11-06-01", "08-03-04", "10-01-02"]
tags: [exploration-geophysics, geotechnical, uxo, magnetics, gpr, detection, false-alarm]
---

# Buried Objects, UXO Detection and Clearance

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the magnetic dipole anomaly of a compact ferrous object and
   **compute** its amplitude for a stated moment, size and depth.
2. **Show** that the detectable depth scales as the cube root of the moment, and
   **use** that scaling to extrapolate a detection limit.
3. **Compute** the probability of detection from a stated noise level and
   detection threshold, and **state** the depth at which it falls to 50% and 90%.
4. **Derive** the GPR hyperbola travel time and **quantify** the velocity-depth
   trade that a limited aperture leaves unresolved.
5. **Compute** the probability that a site is fully cleared as $\mathrm{POD}^{n}$,
   and **state** what a "100% clearance" claim actually requires.
6. **Balance** detection against false alarms with an expected-cost argument.

## Prerequisites

- [11-06-01 Site Investigation: Objectives and Method Selection](./01-site-investigation.md)
  — detection limits and value of information.
- [08-03-04 Magnetic Forward Modelling](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/04-magnetic-forward-modelling.md)
  — dipoles, spheres and their fields.
- [10-01-02 GPR Velocity and Depth](../../10-gpr-near-surface/01-gpr-principles/02-gpr-velocity-and-depth.md)
  — the hyperbola and the velocity question.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md)
  — detection statistics.

> All models and data in this module are **SYNTHETIC**. No real site, predicted
> target, clearance specification or survey result is used.

## 1. Intuition: detection is not identification, and identification is not clearance

Three words are used interchangeably in practice and must not be.

- **Detection.** The instrument reports an anomaly above a threshold. This is a
  probability statement: an object of a given size at a given depth is detected
  with probability $\mathrm{POD}$, not always and not never.
- **Identification.** The anomaly is attributed to an object of a given type and
  size. Magnetically, a small object near the surface and a large one deep
  produce nearly the same anomaly; identification requires the shape of the
  anomaly over an array, or a second method.
- **Clearance.** The area is declared free of hazardous objects to a stated
  depth. This is a statement about the *whole population* of objects, and it
  collapses quickly with the number of objects: even a 95% detection rate leaves
  a 7.7% chance that none of 50 objects was missed.

The reason the distinction matters is the asymmetry of the costs. A missed
object is an accident; a false alarm is a dig. Operators optimise a total cost
that includes both, and a higher detection rate bought with a much higher
false-alarm rate can be the worse choice. This lesson derives the physics that
sets the detection limit and then the statistics that turn it into a clearance
statement.

## 2. Precise definitions

### 2.1 Magnetic moment and the dipole model

A uniformly magnetised body of volume $V$ and magnetisation $M$ (A/m) has a
**magnetic moment** $\mathbf{m} = M V \mathbf{\hat{m}}$ in $\mathrm{A\,m^{2}}$.
For a compact body at a distance much larger than its size, its field is that of
a point dipole:

$$ \mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}
\frac{3(\mathbf{m}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}}-\mathbf{m}}{r^{3}}. $$

Directly above a **vertically** magnetised dipole at depth $z$, the vertical
component reduces to

$$ B_z = 2\,\frac{\mu_0}{4\pi}\frac{m}{z^{3}}
= \frac{2\times10^{-7}\,m}{z^{3}}\ \mathrm{T}, $$

with $m$ in $\mathrm{A\,m^{2}}$ and $z$ in m. This $z^{-3}$ falloff is the
signature of a dipole and the reason deep targets are hard.

### 2.2 POD, threshold and noise

With a stated noise $\sigma$ and a detection threshold $T$ (both in nT), the
probability of detecting an object whose true anomaly is $A$ is

$$ \mathrm{POD} = P(A + \text{noise} > T) = \Phi\!\left(\frac{A-T}{\sigma}\right), $$

with $\Phi$ the standard normal CDF. This definition forces two things to be
stated that are usually omitted: the threshold and the noise. A POD without them
is not a number.

### 2.3 False alarms and clutter

A **false alarm** is a threshold crossing with no target. **Clutter** is the
population of non-target sources — magnetic soil and rock, metallic debris,
pipelines, reinforced concrete, power lines. A clearance specification is a
statement about both $\mathrm{POD}$ (what is found) and false alarms per unit area
(what is dug).

## 3. Derivations

### 3.1 The dipole anomaly and the depth limit

From $B_z = 2(\mu_0/4\pi)m/z^{3}$, setting $B_z = T$ gives the detection depth

$$ z = \left(\frac{2(\mu_0/4\pi)m}{T}\right)^{1/3}
\propto m^{1/3} \propto R\,. $$

For a sphere of radius $R$ the moment is $m = M\frac{4}{3}\pi R^{3}$, so
$z \propto R$: **doubling the radius doubles the detection depth** at fixed
threshold and magnetisation. The demonstration prints the anomaly table (with
$M = 1000\ \mathrm{A\,m^{-1}}$, a stated synthetic induced magnetisation):

| Radius (m) | $m$ ($\mathrm{A\,m^{2}}$) | 0.5 m | 1 m | 2 m | 3 m (nT) |
|---|---|---|---|---|---|
| 0.05 | 0.524 | 837.8 | 104.7 | 13.1 | 3.9 |
| 0.10 | 4.189 | 6702.1 | 837.8 | 104.7 | 31.0 |
| 0.20 | 33.510 | 53616.5 | 6702.1 | 837.8 | 248.2 |
| 0.40 | 268.083 | 428932.1 | 53616.5 | 6702.1 | 1985.8 |

### 3.2 POD against depth

Substituting $A = 2(\mu_0/4\pi)m/z^{3}$ into the POD definition and solving for
the depth at a stated POD:

$$ z_{\mathrm{POD}} = \left(\frac{2(\mu_0/4\pi)m}{T + \sigma\,\Phi^{-1}(\mathrm{POD})}
\right)^{1/3}. $$

The demonstration uses $\sigma = 1\ \mathrm{nT}$ and $T = 2\ \mathrm{nT}$:

| Object | $z_{50}$ (m) | $z_{90}$ (m) | $z_{99}$ (m) |
|---|---|---|---|
| small (0.05 m) | 3.74 | 3.17 | 2.89 |
| medium (0.10 m) | 7.48 | 6.34 | 5.79 |
| large (0.20 m) | 14.96 | 12.69 | 11.57 |
| very large (0.40 m) | 29.93 | 25.37 | 23.14 |

The 50% and 90% depths differ by only about 16%, and the 50% and 99% depths by
about 23%. **Detection is a sharp-topped probability function of depth**: an
object is either safely inside the envelope or already lost, and there is little
"marginal" region to negotiate. This is why the clearance depth must be quoted
with a POD, and why a survey that claims detection "to depth $D$" must also state
that its POD at $D$ is only 50% by construction.

### 3.3 The GPR hyperbola: apex and curvature

For a point target at depth $z$ in a medium of velocity $v$, the two-way travel
time at offset $x$ is

$$ t(x) = \frac{2\sqrt{x^{2}+z^{2}}}{v}, \qquad
t(0) = \frac{2z}{v}. $$

The apex time fixes the **ratio** $z/v$, and the curvature
$\mathrm{d}^{2}t/\mathrm{d}x^{2}|_{0} = 2/(vz)$ fixes the product $vz$. Together
they determine both — but only if the aperture is wide enough that the curvature
is measurable. The demonstration fits a noisy hyperbola over three apertures
(true $v = 0.10\ \mathrm{m\,ns^{-1}}$, $z = 0.50\ \mathrm{m}$):

| Aperture | Admitted $v$ (m/ns) | Admitted $z$ (m) |
|---|---|---|
| $\pm0.5$ m | 0.087-0.121 | 0.41-0.64 |
| $\pm1.0$ m | 0.095-0.106 | 0.45-0.56 |
| $\pm2.0$ m | 0.099-0.102 | 0.45-0.55 |

The effect grows as the aperture shrinks relative to the depth. The
demonstration repeats the fit for a target at $z = 1.0\ \mathrm{m}$ with
$v = 0.12\ \mathrm{m\,ns^{-1}}$:

| Aperture | Aperture / depth | Admitted $v$ (m/ns) | Admitted $z$ (m) |
|---|---|---|---|
| $\pm0.4$ m | 0.4 | 0.085-0.215 | 0.69-1.80 |
| $\pm0.6$ m | 0.6 | 0.099-0.166 | 0.79-1.43 |
| $\pm1.5$ m | 1.5 | 0.116-0.126 | 0.93-1.09 |

**The practical rule is that the aperture must exceed the depth** for the
hyperbola to be self-calibrating; below it, a 20% error in the assumed soil
velocity is a 20% error in depth, with nothing in the data to warn you.

### 3.4 Clearance as a product of probabilities

If a site contains $n$ objects and each is detected independently with
probability $\mathrm{POD}$, the probability that *all* are found is
$\mathrm{POD}^{n}$. The demonstration prints:

| $\mathrm{POD}$ | $n = 10$ | $n = 50$ | $n = 100$ | $n = 500$ |
|---|---|---|---|---|
| 0.99 | 0.904 | 0.605 | 0.366 | 0.007 |
| 0.95 | 0.599 | 0.077 | 0.006 | $\approx0$ |
| 0.90 | 0.349 | 0.005 | $\approx0$ | $\approx0$ |
| 0.80 | 0.107 | $\approx0$ | $\approx0$ | $\approx0$ |

For the $n$ to be usable, the object density must be estimated — which is itself
a prior. The honest clearance statement therefore has the form: "with an assumed
density of $n$ objects per hectare and a POD of $\mathrm{POD}$ at the clearance
depth, the residual probability of an undetected object is
$1-\mathrm{POD}^{n}$."

### 3.5 Detecting versus digging

Let $C_{\text{dig}}$ be the cost of excavating and reinstating one false alarm,
$C_{\text{miss}}$ the consequence of a missed object, $N_{\text{fa}}$ the number
of false alarms and $p_{\text{miss}}$ the residual miss probability. The expected
cost of a survey is

$$ \mathbb{E}[\text{cost}] = C_{\text{dig}}N_{\text{fa}}
+ C_{\text{miss}}\,p_{\text{miss}}, $$

and lowering the threshold moves the first term up and the second down. The
demonstration's stated clutter rate ($2$ false alarms per $1000\
\mathrm{m^{2}}$) gives $20$ digs per hectare. If raising the POD from 0.95 to
0.99 doubles the false-alarm rate, the trade is decided by
$C_{\text{dig}}\Delta N_{\text{fa}}$ against $C_{\text{miss}}\Delta p_{\text{miss}}$
— a purely operational calculation, and one that the geophysicist should supply the
inputs to rather than decide.

## 4. Worked examples

### Example 1 — the depth limit of a survey

A magnetometer has $1\ \mathrm{nT}$ noise and a $2\ \mathrm{nT}$ threshold. A
$0.10\ \mathrm{m}$ radius ferrous object with $M = 1000\ \mathrm{A\,m^{-1}}$:

$$ m = 1000 \times \frac{4}{3}\pi(0.10)^{3} = 4.189\ \mathrm{A\,m^{2}}, $$
$$ z_{50} = \left(\frac{2\times10^{-7}(4.189)}{2\times10^{-9}}\right)^{1/3}
= \left(4.189\times10^{5}\right)^{1/3} = 74.8\ \mathrm{cm}. $$

Doubling the radius to $0.20\ \mathrm{m}$ raises $m$ eightfold and $z_{50}$
twofold to $14.96\ \mathrm{m}$, exactly as the table shows: $z \propto m^{1/3}
\propto R$.

### Example 2 — why "clearance to 1 m" is a POD statement

A site specification says "clearance to $1\ \mathrm{m}$ depth". From the table, a
$0.05\ \mathrm{m}$ object (a small fragment) has $z_{50} = 3.74\ \mathrm{m}$ — so
it is detectable well below 1 m. But a much smaller fragment, or one with a lower
magnetisation (a stainless-steel item, or a corroded one), scales down. Setting
$z_{50} = 1\ \mathrm{m}$ and solving for the moment:

$$ m = \frac{T z^{3}}{2(\mu_0/4\pi)} = \frac{(2\times10^{-9})(1)}{2\times10^{-7}}
= 0.01\ \mathrm{A\,m^{2}}, $$

which for $M = 1000\ \mathrm{A\,m^{-1}}$ is a sphere of radius
$R = (3m/4\pi M)^{1/3} = (3(0.01)/(4\pi(1000)))^{1/3} = 1.34\times10^{-3}\
\mathrm{m}$ — about $1.3\ \mathrm{mm}$. So the specification means "detects objects
with a magnetic moment above $0.01\ \mathrm{A\,m^{2}}$ at 1 m with 50%
probability", and a $1.3\ \mathrm{mm}$ fragment is at the boundary. Whether that is
the right specification is a risk decision, not a geophysical one.

### Example 3 — a false-alarm budget

A $5\ \mathrm{ha}$ site is surveyed with a clutter rate of $3$ false alarms per
$1000\ \mathrm{m^{2}}$ and a dig cost of one unit each. The area is
$5\times10^{4}\ \mathrm{m^{2}}$, so

$$ N_{\text{fa}} = 3 \times \frac{5\times10^{4}}{1000} = 150\ \text{digs}. $$

If the target count is $20$ objects, the ratio of digs to real targets is
$7.5$:1. Reducing the false-alarm rate by half saves $75$ units, and if that costs
a 20% reduction in POD it adds $0.20\times20 = 4$ expected misses — so the
false-alarm reduction is normally the right trade **until** the miss cost is very
high. This is exactly the calculation an operator should be shown, with their own
numbers.

## 5. Assumptions and regime of validity

1. **Point-dipole model.** Valid when the source is small compared with its
   depth. A large object near the surface has a resolved shape, and a
   multi-sensor array can fit it; a single-sensor profile cannot.
2. **Induced, not remanent, magnetisation** unless stated. Real ferrous objects
   often carry strong remanence, which changes both magnitude and direction; this
   is why the field strength and orientation are part of the survey report.
3. **Additive Gaussian noise.** Real magnetometer noise is coloured and contains
   spikes; a POD computed from an rms noise figure is optimistic at the tails.
4. **Independent detections.** $\mathrm{POD}^{n}$ assumes objects are independent.
   Overlapping anomalies, or a systematic (for example a line spacing) effect,
   makes the misses correlated and the clearance probability worse than the
   product.
5. **Uniform velocity for GPR.** A layered or wet soil makes the hyperbola
   non-ideal; the velocity derived is an average to the target, not the local
   velocity at the target.

## 6. Python demonstration

`code/buried_objects_uxo_demo.py` prints:

1. the dipole anomaly of four objects at four depths, and the moment scaling;
2. the 50%, 90% and 99% POD depths for each object;
3. the GPR hyperbola fit and the admitted $(v,z)$ ranges for three apertures;
4. the $\mathrm{POD}^{n}$ clearance table and a false-alarm budget.

```bash
cd 11-exploration-geophysics/06-geotechnical-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python buried_objects_uxo_demo.py
```

Companions:
[`exercises/03-buried-objects-uxo-exercises.md`](./exercises/03-buried-objects-uxo-exercises.md)
and
[`exercises/03-buried-objects-uxo-solutions.md`](./exercises/03-buried-objects-uxo-solutions.md).

## Common pitfalls

1. **Reporting the detection rate without the false-negative count.** The
   clearance probability is $\mathrm{POD}^{n}$, and $n$ is large on a real site.
2. **Quoting a "detection depth" without a POD and a threshold.** The 50% depth
   and the 99% depth differ by only ~20%, so the phrase is nearly meaningless
   alone.
3. **Using a single-sensor profile to identify an object.** Shape is what
   distinguishes a small shallow object from a large deep one.
4. **Ignoring magnetic soil.** A modest susceptibility produces anomalies of the
   same order as small debris (see [11-06-04](./04-landfill-and-waste.md)).
5. **Assuming a GPR velocity.** Without an aperture wider than the depth, the
   velocity and the depth trade exactly.

## Mastery checkpoint

Complete this without notes:

> A magnetometer survey has $0.8\ \mathrm{nT}$ noise and a $1.5\ \mathrm{nT}$
> threshold. **(a)** Compute the moment required for a 50% POD at $2\ \mathrm{m}$
> depth, and the radius of the equivalent sphere for
> $M = 1200\ \mathrm{A\,m^{-1}}$. **(b)** Compute the 90% POD depth for an object
> with twice that moment. **(c)** A GPR hyperbola is picked over an aperture of
> $\pm0.4\ \mathrm{m}$ for a target at $0.6\ \mathrm{m}$; state what is and is not
> determined, with a number. **(d)** A site has 15 target objects per hectare and
> the survey's POD is 0.9; compute the probability of missing at least one on
> $2\ \mathrm{ha}$, and the number of objects expected to be missed.

A worked version of (a) and (d) is in the lesson-06-03
[solutions](./exercises/03-buried-objects-uxo-solutions.md).

## Related modules

- [11-06-01 Site Investigation: Objectives and Method Selection](./01-site-investigation.md)
  — value of information and the microgravity alternative.
- [11-06-02 Geophysics for Tunnels, Dams and Foundations](./02-tunnelling-and-dams.md)
  — the false-negative problem on large structures.
- [11-06-04 Landfill, Waste and Brownfield Site Assessment](./04-landfill-and-waste.md)
  — clutter and base rates in a waste context.
- [08-03 Magnetic Anomalies and Modelling](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/04-magnetic-forward-modelling.md).
- [10-02 GPR Acquisition and Processing](../../10-gpr-near-surface/02-gpr-acquisition-and-processing/03-gpr-velocity-analysis.md).

## Self-assessment checklist

- [ ] I can derive the on-axis dipole field and use it.
- [ ] I can compute a detection depth and its $m^{1/3}$ scaling.
- [ ] I can compute a POD from a noise level and a threshold.
- [ ] I can explain the GPR aperture requirement for a self-calibrating hyperbola.
- [ ] I can compute $\mathrm{POD}^{n}$ for a site and state what "clearance" means.
- [ ] I can set out a false-alarm budget and the trade against missed objects.
