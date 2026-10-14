---
id: 10-06-02
title: "Monitoring Dams, Embankments and Foundations"
level: doctoral
prereqs: ["05-06-01", "09-02-02", "09-02-05", "10-06-01"]
tags: [near-surface, monitoring, ert, embankments, internal-erosion, detectability]
---

# Monitoring Dams, Embankments and Foundations

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Wenner array factor for line electrodes from the half-space
   Green's function, and **verify** it numerically against a finite-difference
   forward model.
2. **Compute** the apparent-resistivity change produced by a wetting front at a
   stated depth and **state** how the anomaly decays with depth.
3. **Choose** an electrode spacing from the depth of the feature to be watched,
   and **quantify** the cost of choosing it too small or too large.
4. **Convert** a measured change in apparent resistivity into a change in water
   content through the petrophysical chain, and **list** every assumption the
   conversion imports.
5. **Compute** the family-wise false-alarm probability of a threshold applied to
   many measurements, and **state** the amplitude penalty of correcting for it.
6. **Distinguish** what geophysics monitors (a property) from what the engineering
   decision needs (pore pressure, integrity, factor of safety), and **name** the
   measurements that bridge the two.

## Prerequisites

- [05-06-01 The Processing Pipeline Concept](../../05-core-geophysics/06-data-processing-principles/01-processing-pipeline-concept.md) —
  the processing and QC vocabulary a permanent array needs.
- [09-02-02 Electrode Arrays](../../09-electrical-em-methods/02-dc-resistivity/02-electrode-arrays.md) —
  Wenner, dipole-dipole and their geometric factors.
- [09-02-05 ERT Tomography](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) —
  the inversion of an electrode array into a resistivity section.
- [10-06-01 Time-Lapse Near-Surface Geophysics](01-time-lapse-nearsurface.md) —
  repeatability, detection thresholds and the ambiguity of change hypotheses.

> All models and data in this module are **SYNTHETIC**. The conductivities, front
> depths, electrode spacings, noise levels and threshold choices below are chosen
> teaching values, not measurements and not site parameters.

## 1. Intuition: an asset that fails quietly

An embankment fails for reasons that are invisible from the surface: internal
erosion along a pipe, a wetting front that saturates a weak layer, a shallow
slip surface, or differential settlement under a structure. The engineer's
question is *is the factor of safety changing?*, and the honest statement of the
geophysicist's contribution is narrower: **we can monitor a physical property that
changes when water content or pore-water chemistry changes, and we can do it over
a volume rather than at a point.** Closing the gap between the two — from a
conductivity change to a safety statement — needs a petrophysical relation, a
mechanical model, and information that geophysics does not supply.

This lesson therefore does three things in a deliberately quantitative way. It
builds a forward model of the measurement (so that "the change is detectable" is a
statement with a number behind it), it measures how the anomaly decays with depth
for a realistic wetting front, and it treats the *statistics of looking many times
at many places*, because a permanent monitoring array is a multiplicity problem
before it is anything else.

## 2. Precise definitions

**ERT.** Electrical resistivity tomography: a set of four-electrode measurements on
a spread, inverted for a conductivity (or resistivity) section. Permanent
installations use fixed electrode lines, often buried along a crest and a toe.

**Apparent resistivity.** $\rho_a$ is the resistivity a homogeneous half-space
would need in order to produce the measured transfer resistance with the same
array. For point electrodes the Wenner factor is $2\pi a$:
$\rho_a = 2\pi a\,\Delta V/I$. For **line** electrodes — the 2-D convention used
by every 2-D modelling code — the factor is instead $\pi/(2\ln 2)$ with the
current taken per unit electrode length, as derived in Section 3.1. Mixing the two
conventions is a factor-of-several error, and it is the commonest arithmetic
mistake in shallow resistivity.

**Depth of investigation (DOI).** The depth range to which a given array is
sensitive, usually specified as the depth containing half the sensitivity — a
quantity that must be computed, not assumed
([10-05-01](../05-other-near-surface-methods/01-electromagnetic-induction-nearsurface.md)
makes the same point for the conductivity meter).

**Saturation and water content.** $\theta$ (volumetric water content) and
$S_w = \theta/\phi$ are the state variables; conductivity responds to both, and to
the pore-water conductivity $\sigma_w$
([10-05-05](../05-other-near-surface-methods/05-multi-method-nearsurface.md)).

**Internal erosion and piping.** The transport of soil particles by seepage,
which increases porosity and permeability locally and is the dominant internal
failure mode of embankments. Its geophysical signature is a local change in
conductivity, often accompanied by a change in temperature and in
self-potential.

**Reciprocity check.** A measurement of the same quadrupole with the current and
potential pairs exchanged; the two values must agree in a linear, passive,
time-invariant model. It is the cheapest field test for electrode and wiring
faults, and a permanent array should be built so that it can be run.

## 3. Derivations and measurements

### 3.1 The line-electrode Wenner factor, verified

For a two-dimensional model (line electrodes, which is the standard convention for
2-D resistivity modelling) a line source of current $I$ on the surface of a
half-space produces

$$V(r) = -\frac{I\rho}{\pi}\ln r + C,$$

because the 2-D Green's function of the Laplacian is $\ln r$ and the surface
image doubles the field. For a Wenner array with electrodes at $x = 0$ (source
$+I$), $a$ ($P_1$), $2a$ ($P_2$) and $3a$ ($-I$):

$$V(P_1) = -\frac{I\rho}{\pi}\left[\ln a - \ln 2a\right] = +\frac{I\rho}{\pi}\ln 2,$$
$$V(P_2) = -\frac{I\rho}{\pi}\left[\ln 2a - \ln a\right] = -\frac{I\rho}{\pi}\ln 2,$$
$$\Delta V = V(P_1)-V(P_2) = \frac{2I\rho}{\pi}\ln 2
\qquad\Longrightarrow\qquad
\boxed{\;\rho_a = \frac{\pi\,\Delta V}{2 I \ln 2}\;}.$$

**Verification.** The demonstration solves the anomalous-potential problem on a
finite-difference grid whose nodes are placed exactly at the electrode positions.
For a homogeneous ground the anomaly is zero and the computed $\rho_a$ is
$50.000000\ \Omega\,\mathrm{m}$ against $1/\sigma_0 = 50.000000\
\Omega\,\mathrm{m}$ — an exact agreement that validates both the analytic primary
potential and the array factor above. For a wetting front the same code gives the
anomalies reported below, and doubling the grid refinement from $0.50$ to
$0.25\ \mathrm{m}$ changes the anomalous result by $1.05\%$, which is the
discretisation error of the numbers used in this lesson.

### 3.2 The anomaly produced by a wetting front

Teaching model: background $\sigma_0 = 0.020\ \mathrm{S\,m^{-1}}$
($\rho_0 = 50\ \Omega\,\mathrm{m}$), a $1\ \mathrm{m}$ thick front of
$\sigma = 0.050\ \mathrm{S\,m^{-1}}$, Wenner spacing $2.00\ \mathrm{m}$.

| front top (m) | $\rho_a$ ($\Omega$ m) | change from dry |
|---|---|---|
| 0.5 | 33.29 | $-33.41\%$ |
| 1.0 | 35.43 | $-29.14\%$ |
| 2.0 | 42.67 | $-14.66\%$ |
| 3.0 | 46.42 | $-7.16\%$ |
| 5.0 | 48.89 | $-2.23\%$ |
| 8.0 | 49.69 | $-0.62\%$ |

The sign is the physics: a conductive (wet) layer lowers the apparent resistivity.
The magnitude halves roughly every metre to two metres of extra depth, which is the
quantitative form of "resistivity sees the shallowest water".

### 3.3 Choosing the spacing: depth against amplitude

The same front, seen by four spacings (change in $\rho_a$ against the dry state):

| spacing (m) | front at 1 m | front at 2 m | front at 4 m |
|---|---|---|---|
| 1.0 | $-21.90\%$ | $-6.15\%$ | $-1.14\%$ |
| 2.0 | $-29.14\%$ | $-14.66\%$ | $-3.83\%$ |
| 4.0 | $-19.92\%$ | $-17.85\%$ | $-8.70\%$ |
| 8.0 | $-7.89\%$ | $-9.75\%$ | $-9.19\%$ |

Each spacing is most sensitive at a depth of order its own length, and the largest
anomaly for a given front moves to larger spacings as the front deepens: the $1\
\mathrm{m}$ front is best seen at $2\ \mathrm{m}$ spacing, the $4\ \mathrm{m}$
front at $4$–$8\ \mathrm{m}$ spacing. **The design rule is that the spacing is
chosen from the depth of the feature that must be watched, and the cost of getting
it wrong is a factor of two to three in the anomaly amplitude** — the same factor
that decides detectability in Section 3.4.

### 3.4 Detectability and multiplicity

Assume the transfer resistance is measured with a $1\%$ one-sigma error (a
realistic figure for a well-installed array with good contact). Then:

| front | top 0.5 m | top 1 m | top 2 m | top 3 m | top 5 m |
|---|---|---|---|---|---|
| $1.0\ \mathrm{m}$, $0.050\ \mathrm{S\,m^{-1}}$ | $33.4\sigma$ | $29.1\sigma$ | $14.7\sigma$ | $7.2\sigma$ | $2.2\sigma$ |
| $0.25\ \mathrm{m}$, $0.026\ \mathrm{S\,m^{-1}}$ | $2.9\sigma$ | $2.9\sigma$ | $1.4\sigma$ | $0.7\sigma$ | $0.2\sigma$ |

A doubling of conductivity is detectable at any of these depths; a *modest*
wetting change ($+30\%$ conductivity over $0.25\ \mathrm{m}$) is detectable at
2$\sigma$ only within the top metre. That table is the honest deliverable of a
feasibility study, and it must be produced *before* the array is installed.

**Multiplicity.** A permanent array does not make one measurement; it makes
thousands, at many electrodes, spacings and times. With $m = 100$ independent
measurements and a naive $2\sigma$ threshold,

$$p_{\text{per test}} = 2[1-\Phi(2)] = 4.55\%, \qquad
P_{\text{family}} = 1 - (1 - 0.0455)^{100} = 99.1\% .$$

**The naive threshold produces at least one false anomaly, with near-certainty.**
The Bonferroni-corrected threshold for a family-wise rate of 5% is
$z = 3.481$ instead of $2.000$: a factor of $1.74$ in amplitude for the same power.
The practical consequences are that (i) detection claims must be stated with the
number of tests that were scanned, (ii) spatial coherence across neighbouring
electrodes is a far stronger discriminator than amplitude (a real anomaly appears
in several adjacent measurements with the sign the physics predicts), and (iii) a
monitoring threshold belongs in the design document, not in the interpretation
report written afterwards.

### 3.5 From a resistivity change to an engineering statement

Take the $14.66\%$ change produced by the front at $2\ \mathrm{m}$ and ask what it
means. For a **uniform** relative conductivity change, $\rho_a = \rho_0/(1+\Delta
\sigma/\sigma)$, so

$$\Delta\sigma/\sigma = \frac{-\Delta\rho_a/\rho_a}{1+\Delta\rho_a/\rho_a}
= \frac{0.1466}{0.8534} = +17.2\%.$$

Through the Archie-type relation $\sigma = \sigma_w\theta^{m}$ with $m = 1.5$ and
**fixed** $\sigma_w$, a $17.2\%$ conductivity increase corresponds to

$$\frac{\Delta\theta}{\theta} = \frac{1}{m}\frac{\Delta\sigma}{\sigma}
= \frac{0.172}{1.5} = 11.5\%\ \text{relative},$$

i.e. a water content from $0.200$ to $0.223$ in the teaching model. The chain has
three links and each imports assumptions: (i) the change is uniform over the
sensitivity of the array (it is not — it is a $1\ \mathrm{m}$ layer, so the layer
change is *larger* than the apparent change by roughly $1/W$, with $W$ the layer's
weight); (ii) $\sigma_w$, $m$ and $\phi$ are known and unchanged; (iii) nothing
else changed (temperature, electrode contact, salinity).

**And the engineering statement still needs more.** A water-content change is not
a factor of safety. The bridge is a mechanical model (effective stress, suction,
shear strength), calibrated to the same material, and the geophysical monitoring
supplies the *time series of the input* to that model — which is genuinely
valuable, because the alternative is extrapolating from a piezometer at one point.

## 4. Physical interpretation

**What the method is good at.** Detecting a *change*, in the top few metres, over a
large volume, with equipment that can be left in place. The absolute resistivity
image matters far less than the difference between epochs, because the baseline's
systematic errors cancel in the difference (that is the definition of a 4-D
survey).

**Where it is weak.** Deep features, subtle changes, and anything whose signature
is a change in *mechanics* rather than in *water*. The DOI of a surface array is
set by the spread length, and the anomaly of a deep feature is small by the
numbers of Section 3.2.

**Coupling drift is the main practical failure.** Electrode contact resistance
depends on moisture and temperature; a permanent array's electrodes dry out, freeze
and corrode. Because the injection current is measured and the transfer resistance
formed, a change in contact resistance changes the *measured* transfer resistance
directly. The defences are (i) buried, corrosion-resistant electrodes with a
backfill, (ii) a reciprocity check at every epoch, (iii) recording the transmitted
current and the contact resistance per electrode, and (iv) treating any
single-electrode outlier as a hardware fault until proved otherwise.

**Temperature is a confounder with a known structure.** A seasonal temperature
wave changes both the pore-water conductivity and the electrode contact; its depth
dependence is known from
[10-05-03](../05-other-near-surface-methods/03-thermal-nearsurface.md), so its
signature can be predicted and separated from a target change with a different
depth dependence — the sensitivity-vector argument of
[10-06-01](01-time-lapse-nearsurface.md) applied in depth rather than in time.

**Self-potential is the natural companion.** Seepage drives a measurable
streaming potential, so a self-potential array responds to *flow* where ERT
responds to *water content*; the pair is the standard combination for internal
erosion monitoring, and their sensitivity vectors are not parallel.

## 5. Worked examples

### Example 1 — Verify the array factor by hand

A Wenner array with $a = 2\ \mathrm{m}$, current $I = 0.10\ \mathrm{A}$, in a
half-space of $\rho = 50\ \Omega\,\mathrm{m}$. Then

$$\Delta V = \frac{2I\rho}{\pi}\ln 2
= \frac{2(0.10)(50)}{\pi}(0.6931) = 2.206\ \mathrm{V},$$
$$\rho_a = \frac{\pi \Delta V}{2 I \ln 2} = 50.0\ \Omega\,\mathrm{m} .$$

The demonstration reproduces this as $50.000000$ from the numerical model, which is
the numerical proof that the array factor is right.

### Example 2 — Is a 3 m deep front detectable?

From Section 3.2 a $1\ \mathrm{m}$ front at $3\ \mathrm{m}$ gives a $-7.16\%$
change at a $2\ \mathrm{m}$ spacing, i.e. $7.2\sigma$ for a $1\%$ measurement
error — detectable. But note the trade made: at $2\ \mathrm{m}$ spacing the
anomaly for a front at $3\ \mathrm{m}$ is $7\%$, while at $4\ \mathrm{m}$ spacing
it is larger (the spacing study shows $4\ \mathrm{m}$ spacing giving $-17.85\%$ for
a front at $2\ \mathrm{m}$, and by symmetry a front at $3$–$4\ \mathrm{m}$ is best
served by $4$–$8\ \mathrm{m}$ spacing). **Choosing the spacing is choosing which
depth to defend.**

### Example 3 — The cost of not correcting for multiplicity

A monitoring report compares 500 measurements between two epochs and flags every
change exceeding $2\sigma$. Under the null hypothesis the expected number of
flagged measurements is $500 \times 0.0455 = 22.8$. The report's "22 anomalies" are
therefore entirely consistent with noise, and the *inference* that something
changed requires either a corrected threshold ($z = 3.891$ for 500 tests at a 5%
family-wise rate, an amplitude penalty of $1.95$), or a spatial-coherence
criterion, or both. Reporting the count without either is a false discovery.

### Example 4 — The conversion chain, with its assumptions

A measured $-14.66\%$ change at a $2\ \mathrm{m}$ spacing, at a site where
$\phi = 0.45$, $m = 1.5$ and a water sample gives $\sigma_w = 0.25\
\mathrm{S\,m^{-1}}$:

1. uniform-change inversion gives $\Delta\sigma/\sigma = +17.2\%$;
2. Archie with fixed $\sigma_w$ gives $\Delta\theta/\theta = +11.5\%$;
3. if the front is actually confined to a layer carrying only $W = 0.4$ of the
   array's sensitivity, the layer's own change is larger: $\Delta\sigma/\sigma
   \approx 17.2\%/0.4 = 43\%$, so the layer's water content change is
   $\Delta\theta/\theta \approx 29\%$.

The same measurement supports conclusions differing by a factor of $2.5$ depending
on where the change is assumed to sit. **Report the sensitivity weighting
explicitly, or the engineering interpretation is not reproducible.**

## 6. Assumptions and regime of validity

1. **Two-dimensional, line-electrode geometry** for the model, and a stated
   relationship between it and the real (three-dimensional) array. Mixing them is
   a factor-of-two error.
2. **A known background.** The petrophysical conversion requires $\sigma_w$, $m$
   and $\phi$; without them only *relative* changes survive, which is usually
   acceptable for monitoring and not acceptable for a design document.
3. **Repeatable electrode contact.** A change in contact resistance is
   indistinguishable from a change in the ground unless it is measured.
4. **The target perturbs a linear, passive medium.** Large currents can generate
   non-linear responses in some ground; the reciprocity check catches this.
5. **Stationary noise between epochs.** Wetting, freezing and vegetation change the
   noise level, not only the signal, so the repeatability must be re-measured at
   each epoch rather than assumed from the baseline.
6. **Spatial coherence of the true anomaly.** The multiplicity correction and the
   coherence criterion both assume a real target is spatially contiguous; a
   single-electrode anomaly is more likely to be hardware.
7. **A mechanical model exists to receive the output.** Without it, the monitoring
   produces a time series of water content, which is a contribution and not a
   safety assessment.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | |
| resistivity | $\rho$ | $\Omega$ m | $1/\sigma$ |
| current | $I$ | A | |
| potential difference | $\Delta V$ | V | |
| transfer resistance | $\Delta V/I$ | $\Omega$ | array-independent |
| apparent resistivity | $\rho_a$ | $\Omega$ m | geometric factor times $\Delta V/I$ |
| array factor (line electrodes) | $\pi/(2\ln 2)$ | dimensionless | $=2.266$ for $\rho_a/(\Delta V/I)$ |
| depth of investigation | | m | of order the spacing |
| water content | $\theta$ | $\mathrm{m^3\,m^{-3}}$ | $\le\phi$ |

The check that catches the classic error: a *transfer resistance* is
$\Delta V/I$ and, once the array and the electrode type are fixed, is the raw
measurement; a *resistivity* is that transfer resistance times a geometric factor.
For point electrodes the factor is $2\pi a$ (units of length, hence the spacing
appears); for line electrodes with current per unit length it is the dimensionless
$\pi/(2\ln 2) = 2.266$. Comparing raw transfer resistances between different
arrays is meaningless in either convention, and the two conventions differ by
$4a\ln 2$ — a factor of $11$ at $a = 4\ \mathrm{m}$.

## 8. Python demonstration

`code/geotechnical_monitoring_demo.py` builds the whole chain from the field
equation to the statistics. It:

1. assembles and solves the anomalous-potential finite-difference problem, checks
   the discrete residual and the symmetry of the interior operator, and verifies
   the homogeneous Wenner result ($50.000000\ \Omega\,\mathrm{m}$ against
   $1/\sigma_0 = 50.000000$), with a grid-convergence difference of $1.05\%$;
2. reports the depth decay of the anomaly from a $1\ \mathrm{m}$ front
   ($-33.41\%$ at $0.5\ \mathrm{m}$ to $-0.62\%$ at $8\ \mathrm{m}$);
3. measures the spacing sensitivity matrix ($4$ spacings $\times$ $3$ depths);
4. computes the $2\sigma$ detectability of a strong and of a modest front against
   a $1\%$ noise level;
5. computes the family-wise false-alarm probability for $100$ tests
   ($99.1\%$ at $2\sigma$) and the Bonferroni threshold ($3.481\sigma$, an
   amplitude penalty of $1.74$).

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in about seven
seconds.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-geotechnical-monitoring-exercises.md`](./exercises/02-geotechnical-monitoring-exercises.md)
and
[`exercises/02-geotechnical-monitoring-solutions.md`](./exercises/02-geotechnical-monitoring-solutions.md).

- **★** Compute the transfer resistance and apparent resistivity of a line-electrode
  Wenner array with $a = 4\ \mathrm{m}$ and $I = 0.05\ \mathrm{A}$ in a
  $50\ \Omega\,\mathrm{m}$ half-space.
- **★** Using the measured table, state the depth decay factor per metre of front
  depth between $1$ and $3\ \mathrm{m}$.
- **★★** A front at $2\ \mathrm{m}$ gives $-14.66\%$ at a $2\ \mathrm{m}$ spacing.
  Convert it to a water-content change under a uniform-change assumption and list
  the assumptions.
- **★★** Compute the family-wise false-alarm probability for 400 tests at $2\sigma$
  and at the Bonferroni threshold, and state the amplitude penalty.
- **★★★** Design a permanent monitoring array for a $6\ \mathrm{m}$ high embankment
  with a target wetting front at $2$–$4\ \mathrm{m}$ depth, stating the spacing,
  the expected anomaly, the threshold, and the falsification test.

## Mastery checkpoint
Complete this without notes:

> A permanent array has electrodes at $2\ \mathrm{m}$ spacing along a crest, a
> measurement error of $1.0\%$ on the transfer resistance, and $200$ quadrupoles
> per epoch. **(a)** State the depth at which a wetting front produces its largest
> anomaly, and the anomaly for a front at $2\ \mathrm{m}$ from the measured table.
> **(b)** Compute the $2\sigma$ detection threshold in per cent and the
> family-wise false-alarm probability for $200$ tests. **(c)** Compute the
> corrected threshold and the change amplitude needed there. **(d)** Convert a
> detected $-10\%$ change to a water content change under stated assumptions.
> **(e)** Name two confounders and the measurement that identifies each.

A worked version of (a)–(d) appears in the exercise solutions.

## Common pitfalls
1. **Reporting an anomaly without the number of tests.** The multiplicity
   calculation is trivial and, uncorrected, it turns noise into findings.
2. **Choosing the spacing for convenience.** The spacing chooses the depth that is
   defended; a factor of two in the wrong direction costs a factor of two to three
   in detectability.
3. **Comparing a 2-D model with a 3-D array factor.** A factor-of-two error in
   apparent resistivity, and a factor-of-four in the derived conductivity.
4. **Assuming the petrophysical constants transfer.** $\sigma_w$, $m$ and $\phi$
   are site properties; without them the output is a relative change, not a water
   content.
5. **Ignoring coupling drift.** Electrodes dry out, freeze and corrode; a change in
   contact resistance appears as a change in the ground.
6. **Believing one epoch.** A single difference without a re-measured repeatability
   has no error bar.
7. **Confusing monitoring with an assessment.** A water-content time series is an
   input to a stability model, not a factor of safety.
8. **Ignoring spatial coherence.** A real change appears in adjacent quadrupoles
   with a physically consistent pattern; a single outlier is usually hardware.

## Related modules
- [10-06-01 Time-Lapse Near-Surface Geophysics](01-time-lapse-nearsurface.md) —
  repeatability and the detection framework this lesson applies.
- [10-06-03 Monitoring Contaminant Transport with Geophysics](03-contaminant-monitoring.md) —
  the same machinery for a designed change with a known transport model.
- [10-05-05 Integrating Near-Surface Methods](../05-other-near-surface-methods/05-multi-method-nearsurface.md) —
  the petrophysical chain from a property to a state variable.
- [09-02 DC Resistivity](../../09-electrical-em-methods/02-dc-resistivity/README.md) —
  arrays, sounding, ERT inversion and its resolution limits.
- [09-04 Self-Potential](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/README.md) —
  the companion method for seepage flow.
- [04-06 Petroleum and Mineral Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/README.md) —
  the geotechnical context of fluid flow in porous media.
