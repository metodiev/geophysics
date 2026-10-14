---
id: 10-05-04
title: "Nuclear and Radiometric Near-Surface Methods"
level: advanced
prereqs: ["01-02-03", "05-01-01", "05-02-03", "10-05-03"]
tags: [near-surface, radiometrics, gamma-spectrometry, nuclear-gauges, counting-statistics]
---

# Nuclear and Radiometric Near-Surface Methods

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the counting statistics of a radiometric measurement from the
   Poisson distribution, and **compute** the counting time needed for a stated
   precision.
2. **Derive** the critical level and the detection limit for a net count
   measurement, and **state** the confidence convention that defines them.
3. **Derive** the depth distribution of the gamma-ray signal from a uniformly
   active half-space, and **compute** the depths containing 50%, 90% and 95% of
   it.
4. **Invert** a three-window stripping problem, **quantify** its conditioning,
   and **predict** the error amplification of a wrong stripping factor.
5. **Explain** what a neutron moisture gauge measures and why its calibration is
   a property of the material rather than of the instrument.
6. **State** the regime of validity and, in particular, why no amount of counting
   time fixes a calibration error.

## Prerequisites

- [01-02-03 Exponentials, Logarithms and Decay Laws in Earth Science](../../01-mathematics/02-algebra/03-exponentials-logarithms.md) —
  exponential attenuation and logarithmic depth behaviour.
- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md) —
  contrasts and detectability.
- [05-02-03 Noise and Drift](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) —
  random and systematic error.
- [10-05-03 Thermal Methods for Shallow Subsurface Investigation](03-thermal-nearsurface.md) —
  the sibling method whose depth scale is also set by an attenuation length.

> All models and data in this module are **SYNTHETIC**. The attenuating
> materials, activities, stripping factors, detector efficiencies and water
> contents below are chosen teaching values. They are not measurements, not
> detector specifications and not site parameters. The three gamma energies
> quoted are standard nuclear-data constants.

## 1. Intuition: measurements made of counts

Two families of near-surface measurement are nuclear rather than electromagnetic
or elastic.

- **Natural gamma-ray spectrometry** measures the radiation emitted by potassium,
  uranium and thorium in the top few decimetres of soil and rock. It maps
  *geochemistry* rather than a bulk property, which makes it the standard
  companion to magnetic and electromagnetic surveys for mapping soil type,
  weathering and lithology.
- **Nuclear gauges** put a source and a detector in the same probe: gamma
  transmission or backscatter measures bulk density, and a neutron source with a
  moderator-based detector measures water content through thermal-neutron
  moderation. These are borehole tools (the geotechnical cousin of the
  density and moisture logs in
  [05-08-04 Porosity Logs](../../05-core-geophysics/08-geophysical-logging/04-porosity-logs.md)).

Both rest on the same two facts, and the whole lesson is their consequence:

1. **Every measurement is an integer count of random events.** The variance of a
   count equals its mean, so precision costs counting time as $1/\epsilon^{2}$
   and never improves for free.
2. **The signal is attenuated before it is detected, and the attenuation
   coefficient depends on the material.** That is what makes the measurement
   geophysical — and also what makes it ambiguous, because a change of activity
   and a change of density attenuate the same signal.

## 2. Precise definitions

**Activity and count rate.** Activity is the number of decays per second
(becquerel, $\mathrm{Bq}$). A detector records a *count rate* in
$\mathrm{s^{-1}}$, which is the activity times a geometric-and-efficiency factor.

**Windows.** A gamma spectrometer sorts counts into energy windows. Three
windows matter because three decay series dominate natural gamma emission, each
with a standard line:

| Nuclide | Series | Gamma energy |
|---|---|---|
| K-40 | primordial potassium | $1.4608\ \mathrm{MeV}$ |
| Bi-214 | U-238 series | $1.7645\ \mathrm{MeV}$ |
| Tl-208 | Th-232 series | $2.6145\ \mathrm{MeV}$ |

*These three energies are standard nuclear-data constants; every other number in
this lesson is a synthetic teaching value.*

**Stripping.** Because Compton scattering moves counts between windows, a window
does not measure "its" nuclide alone. If $\mathbf c$ is the vector of window
count rates and $\mathbf a$ the vector of nuclide activities,
$\mathbf c = A\mathbf a$ with $A$ the **sensitivity matrix**, and the activities
are recovered from $\mathbf a = A^{-1}\mathbf c$ — the **stripping matrix**.

**Mass attenuation coefficient.** $\mu/\rho$ in $\mathrm{m^{2}\,kg^{-1}}$ (often
quoted as $\mathrm{cm^{2}\,g^{-1}}$) gives the linear attenuation coefficient
$\mu = (\mu/\rho)\rho$. The **half-value layer** is $\ln 2/\mu$ and the
**mean free path** is $1/\mu$.

**Poisson statistics.** For a mean count $\bar N$, the probability of observing
$N$ is $P(N) = \bar N^{N}e^{-\bar N}/N!$, with variance equal to the mean:
$\sigma_N = \sqrt{\bar N}$. Relative precision is $1/\sqrt{N}$.

## 3. Derivations

### 3.1 Why precision is expensive

The Poisson result $\sigma_N^2 = \bar N$ follows directly from the distribution.
A rate $r$ measured for a time $t$ gives $N = rt$ counts, so

$$\frac{\sigma_r}{r} = \frac{\sqrt{rt}}{rt} = \frac{1}{\sqrt{rt}} .$$

Two consequences that shape every radiometric survey:

- **To reach relative precision $\epsilon$ you need $N \ge 1/\epsilon^2$ counts.**
  That is $400$ counts for 5%, $2500$ for 2% and $10000$ for 1%.
- **A small signal is expensive.** The time needed grows as $1/(r\epsilon^2)$, so a
  weak source needs a *quadratically* longer count for the same relative
  precision. Radiometrics is the method where survey speed is set by counting
  statistics rather than by geometry.

### 3.2 Critical level and detection limit

Suppose a sample and a background are counted for the same time, giving net
counts $N = N_s - N_B$. Under the null hypothesis (nothing there)
$\sigma_N = \sqrt{2N_B}$, because both counts are Poisson. With the Gaussian
approximation and a one-sided confidence level set by $k$ (the standard normal
quantile: $k = 1.6449$ for 95%), the **critical level** is

$$L_C = k\sqrt{2N_B},$$

the smallest observed net count that would be called a detection. The true net
signal that is detected 95% of the time is larger, because the variance grows with
the signal, and follows from

$$L_D = L_C + k\sqrt{2N_B + L_D},$$

which is solved numerically. The two are different questions — *what would I
report?* and *what would I reliably find?* — and confusing them is the commonest
error in reporting a detection. Note the scaling: $L_C \propto \sqrt{N_B}$, so
**halving the background** (better shielding, longer count, a lower-activity
detector material) buys a factor $\sqrt{2}$ in detection limit.

### 3.3 Where the gamma-ray signal comes from

Put a detector above a half-space of uniform activity $a$ per unit volume. The
unscattered flux from a volume element at distance $r$ is
$a\,\mathrm dV\,e^{-\mu r}/(4\pi r^2)$ (the point kernel). Integrate over a
horizontal layer at depth $z$: with $\rho\,\mathrm d\rho = r\,\mathrm dr$,

$$\mathrm dF(z) = \frac{a}{2}\left[\int_z^\infty
\frac{e^{-\mu r}}{r}\mathrm dr\right]\mathrm dz
= \frac{a}{2}E_1(\mu z)\,\mathrm dz,$$

where $E_1$ is the exponential integral of the previous lesson. Because
$\int_0^\infty E_1(u)\,\mathrm du = 1$, the total flux is $a/(2\mu)$, and the
fraction originating above depth $z$ is

$$\boxed{\;f(z) = \mu z\,E_1(\mu z) + 1 - e^{-\mu z}\;}$$

using $\int_0^{U}E_1(u)\mathrm du = UE_1(U) + 1 - e^{-U}$.

The same integral gives the **mean depth of origin**,

$$\bar z = \frac{\int_0^\infty zE_1(\mu z)\mathrm dz}{\int_0^\infty E_1(\mu z)\mathrm dz}
= \frac{1}{2\mu},$$

using $\int_0^\infty uE_1(u)\mathrm du = 1/2$. **Two scales matter and they differ
by an order of magnitude for a realistic soil**: the mean depth of origin is
$1/(2\mu)$, a few centimetres, while the *cumulative* 90% depth is much larger,
because the layer response $E_1(\mu z)$ has a long tail. Quoting one number for
"the depth of investigation" of gamma spectrometry therefore hides which question
is being answered.

### 3.4 Stripping and its conditioning

The window count rates are $\mathbf c = A\mathbf a$, so recovering the activities
requires inverting $A$. The error follows from the inverse:

$$\delta\mathbf a = A^{-1}\delta\mathbf c
\quad\Longrightarrow\quad
|\delta a_i| \le \sum_j |(A^{-1})_{ij}|\,|\delta c_j| .$$

The relevant conditioning number is not the spectral condition number of $A$
alone: the *amplification* the analyst experiences is the row sum of $|A^{-1}|$,
which is what the demonstration prints. A useful sanity rule is that the
amplification is roughly $1 + \sum_{j\ne i}|(A^{-1})_{ij}|$, so a stripping matrix
with off-diagonal entries of order $0.2$ amplifies a 1% window error to about
$1.2$–$1.3$%.

### 3.5 Why a gauge calibration is a material property

A neutron gauge counts thermal neutrons produced when fast neutrons from a source
are moderated by hydrogen. The count rate is broadly proportional to the
volumetric water content $\theta$, but the constant of proportionality depends on
the bulk density (which controls how much material the neutrons cross) and on the
absorption cross-section of the matrix (elements such as chlorine and boron). The
calibration is therefore written as a family of lines, one per material type, and
the uncertainty that dominates is not counting statistics but the **distance from
the calibration material to the actual one**. A density gauge has the same
structure through $\mu = (\mu/\rho)\rho$: the count rate measures an *attenuation*,
and separating density from composition requires an assumption about the latter.

## 4. Physical interpretation

**Measured counting statistics.** With a true rate of $12\ \mathrm{s^{-1}}$
counted for $30\ \mathrm{s}$ over $20000$ repeats, the demonstration measures a
mean of $360.33$ counts and a standard deviation of $18.77$, against
$\sqrt{360.33} = 18.98$: the ratio is $0.989$. That is the Poisson law verified —
and it is the only error term in the measurement that more time can reduce.

**Measured detection limits.** With a background of $900$ counts in $60\
\mathrm{s}$ ($15\ \mathrm{s^{-1}}$) and $k = 1.6449$:

| counting time (s) | $N_B$ | $L_C$ | $L_D$ | $L_D$ as a rate |
|---|---|---|---|---|
| 30 | 450.0 | 49.35 | 101.40 | $3.38\ \mathrm{s^{-1}}$ |
| 60 | 900.0 | 69.79 | 142.28 | $2.37\ \mathrm{s^{-1}}$ |
| 120 | 1800.0 | 98.69 | 200.09 | $1.67\ \mathrm{s^{-1}}$ |
| 240 | 3600.0 | 139.57 | 281.85 | $1.17\ \mathrm{s^{-1}}$ |

In counts the detection limit grows with time; in *rate* it falls as
$1/\sqrt{t}$ (a factor of $2.89$ over the eightfold increase in time). This is the
quantitative content of "count longer to see less".

**Measured depth of origin.** With $\mu/\rho = 0.0055\ \mathrm{m^{2}\,kg^{-1}}$
(a teaching value, $0.055\ \mathrm{cm^{2}\,g^{-1}}$) and
$\rho = 1600\ \mathrm{kg\,m^{-3}}$, $\mu = 8.80\ \mathrm{m^{-1}}$ and the
half-value layer for a plane source is $7.88\ \mathrm{cm}$. The demonstration
integrates the layer response:

| depth (m) | cumulative fraction |
|---|---|
| 0.02 | 0.3952 |
| 0.05 | 0.6374 |
| 0.10 | 0.8223 |
| 0.20 | 0.9485 |
| 0.30 | 0.9834 |
| 0.50 | 0.9980 |

So **50% of the signal comes from the top $3.04\ \mathrm{cm}$, 90% from the top
$14.48\ \mathrm{cm}$ and 95% from the top $20.25\ \mathrm{cm}$**, while the mean
depth of origin is $5.68\ \mathrm{cm} = 1/(2\mu)$. The measurement is shallower
than its own folklore and has a longer tail than its own mean. A gravel of
different activity spread over the top centimetre changes the reading by more than
a metre of the same material at depth would.

**Measured stripping behaviour.** For the synthetic sensitivity matrix with
off-diagonal terms of $0.03$–$0.20$, the 2-norm condition number is $1.496$ and the
determinant $0.962$. A 1% error in every window propagates to $1.243\%$, $1.288\%$
and $1.156\%$ in the three activities — a modest amplification, as
Section 3.4 predicts. A **5% error in a single stripping factor**, however,
returns activities $[0.9898, 1.0010, 1.0002]$ for a unit-activity ground: the
error lands almost entirely on the source window of the wrong factor. Stripping
factor accuracy, not counting time, limits the accuracy of a nuclide map.

**Measured gauge behaviour.** A synthetic linear response of
$100 + 900\theta$ counts per second, counted for $60\ \mathrm{s}$, is recovered as
$899.2\theta + 101.1$ — slope error $0.09\%$, intercept error $1.09\%$, both
consistent with Poisson noise. At $\theta = 0.20$ the count is $16800$, so the
one-sigma statistical uncertainty is $2.16\ \mathrm{s^{-1}}$, which is
$0.240$ percentage points of water content. A change of material that shifts the
calibration by two percentage points of water content is an order of magnitude
larger than that. **The precision is statistical; the accuracy is petrophysical.**

## 5. Worked examples

### Example 1 — Counting time for 2% precision

A weak source gives $r = 12\ \mathrm{s^{-1}}$. For $\epsilon = 0.02$,

$$N \ge \frac{1}{\epsilon^{2}} = \frac{1}{0.0004} = 2500 \text{ counts},
\qquad t = \frac{N}{r} = \frac{2500}{12} = 208.3\ \mathrm{s}.$$

The demonstration tabulates the family: $25$ counts for 20%, $400$ for 5%,
$10000$ for 1%. Note the 25-fold increase in time between 5% and 1%.

### Example 2 — Detection limit at two counting times

At $t = 60\ \mathrm{s}$ with $N_B = 900$:

$$L_C = 1.6449\sqrt{2(900)} = 1.6449(42.426) = 69.79 \text{ counts},$$
$$L_D = 69.79 + 1.6449\sqrt{1800 + L_D}
\;\Longrightarrow\; L_D = 142.28 \text{ counts} = 2.37\ \mathrm{s^{-1}} .$$

At $t = 240\ \mathrm{s}$, $N_B = 3600$ and $L_D = 1.17\ \mathrm{s^{-1}}$: a
fourfold longer count halves the detectable rate. Check the algebra in the other
direction: a signal of $2.37\ \mathrm{s^{-1}}$ over a background of
$15\ \mathrm{s^{-1}}$ is a net excess of $15.8\%$ — a large-looking number that
requires the full table to interpret, because the *uncertainty* of a background of
$900$ counts is $\sqrt{2(900)} = 42$ counts, i.e. $4.7\%$.

### Example 3 — Depth of origin and a surface layer

For the teaching soil ($\mu = 8.80\ \mathrm{m^{-1}}$), the layer response at
$z = 0.05\ \mathrm{m}$ is $E_1(0.44)$. Since

$$E_1(u) \approx -\gamma - \ln u + u, \qquad \gamma = 0.5772,$$
$$E_1(0.44) \approx -0.5772 - \ln(0.44) + 0.44 = -0.5772 + 0.8210 + 0.44 = 0.684,$$

against $E_1(\mu z)$ at the surface, which diverges logarithmically — another way
of saying that the layer response is dominated by the near-surface. The
cumulative fraction at $z = 0.05\ \mathrm{m}$ is

$$f = (0.44)(0.684) + 1 - e^{-0.44} = 0.301 + 1 - 0.644 = 0.657,$$

against the demonstration's $0.6374$: the small difference is the neglected
higher terms of the series expansion ($E_1$ converges slowly for $u \sim 1$). Use
the numerical integral, not the expansion, above $u \approx 0.2$.

### Example 4 — Setting a detection threshold for a uranium window

A window has a background of $2500$ counts per $60\ \mathrm{s}$ measurement.
Then

$$L_C = 1.6449\sqrt{2(2500)} = 116.31 \text{ counts}, \qquad
L_D = 116.31 + 1.6449\sqrt{5000 + L_D} = 235.32 \text{ counts}.$$

Dividing by the count time gives $L_D = 3.92\ \mathrm{s^{-1}}$. Translating that
into an activity requires the calibrated sensitivity of the window — and *that*
is where the stripping factor errors of Section 3.4 enter: the threshold is a
statement about counts, converted to a geological statement only through a
calibration whose uncertainty is usually larger than the statistical one.

## 6. Assumptions and regime of validity

1. **Poisson statistics.** Departures occur with dead time (at high count rates
   the detected fraction saturates), with gain drift, and with non-random
   background. A measured $\sigma/\sqrt{N}$ that differs from $1$ by more than a
   few per cent is a diagnostic, not a curiosity.
2. **Unscattered (no build-up) transport.** The point kernel of Section 3.3
   neglects multiple scattering, which returns counts to the detector and makes
   the effective attenuation coefficient *smaller* than $\mu$. For the depths
   quoted here the correction to the *shape* of the depth distribution is real and
   is handled by calibrating against a known standard, not by theory alone.
3. **Uniform activity with depth.** A layered or surface-deposited source changes
   the depth distribution completely; a thin layer of activity on the surface
   dominates the reading far more than the same total activity distributed in the
   soil.
4. **Known detector response and geometry.** Height above the ground, detector
   area and the spectral response must be constant between stations, or the
   survey measures the geometry rather than the ground.
5. **Constant instrument calibration.** Spectral drift and temperature effects on
   the detector (especially for scintillators) shift the windows; a daily check
   against a standard source is the usual defence.
6. **A gauge calibration that applies.** The neutron and density calibrations are
   material-specific. Assuming the wrong matrix is a systematic error that
   averaging cannot remove.
7. **Radiation safety and regulation.** Source-based gauges are controlled
   equipment; natural-gamma surveys are not, but their *interpretation* carries
   the same statistical caveats. Nothing in a lesson changes the licence
   requirement.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| activity | $A$ | $\mathrm{Bq} = \mathrm{s^{-1}}$ | |
| count rate | $c$ | $\mathrm{s^{-1}}$ | |
| counts | $N$ | dimensionless | $\sigma_N = \sqrt{N}$ |
| counting time | $t$ | s | |
| critical level | $L_C$ | counts | $k\sqrt{2N_B}$ |
| mass attenuation coefficient | $\mu/\rho$ | $\mathrm{m^{2}\,kg^{-1}}$ | often $\mathrm{cm^{2}\,g^{-1}}$ |
| linear attenuation coefficient | $\mu$ | $\mathrm{m^{-1}}$ | $(\mu/\rho)\rho$ |
| half-value layer | $\ln 2/\mu$ | m | |
| layer response | $E_1(\mu z)$ | dimensionless | argument $\mu z$ dimensionless |
| water content | $\theta$ | $\mathrm{m^{3}\,m^{-3}}$ | volumetric |

The dimensional check that catches the commonest error: the argument of $E_1$ must
be dimensionless, so $z$ must be multiplied by a $1/\mathrm{length}$
coefficient. Mixing $\mathrm{cm^{2}\,g^{-1}}$ with $\mathrm{m^{2}\,kg^{-1}}$
changes the depth scale by a factor of $10$ — enough to turn "the top few
centimetres" into "the top few decimetres".

## 8. Python demonstration

`code/nuclear_radiometric_demo.py` implements the whole chain and prints labelled
results with units. It:

1. draws $20000$ Poisson realisations and confirms
   $\sigma_N/\sqrt{\bar N} = 0.989$;
2. tabulates the counting time needed for five target precisions;
3. solves for $L_C$ and $L_D$ at four counting times
   ($L_D$ from $3.38$ to $1.17\ \mathrm{s^{-1}}$);
4. integrates the exact layer response $E_1(\mu z)$ of a uniformly active
   half-space and reports the 50%, 90% and 95% depths ($3.04$, $14.48$,
   $20.25\ \mathrm{cm}$) and the mean depth $1/(2\mu) = 5.68\ \mathrm{cm}$;
5. inverts a synthetic stripping matrix, reports its conditioning and the
   error amplification, and shows the effect of a 5% wrong factor;
6. fits a synthetic neutron-gauge calibration with Poisson noise and compares the
   statistical error with a material-calibration shift.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-nuclear-and-radiometric-nearsurface-exercises.md`](./exercises/04-nuclear-and-radiometric-nearsurface-exercises.md)
and
[`exercises/04-nuclear-and-radiometric-nearsurface-solutions.md`](./exercises/04-nuclear-and-radiometric-nearsurface-solutions.md).

- **★** A window records $900$ counts in $60\ \mathrm{s}$. Compute the count rate,
  its one-sigma uncertainty and the relative precision.
- **★** How long must a $12\ \mathrm{s^{-1}}$ source be counted for 1% precision?
- **★★** Compute $L_C$ and $L_D$ for a background of $2500$ counts and convert to
  a rate.
- **★★** Using the teaching attenuation, compute the depth above which 75% of the
  gamma signal originates, and compare with the mean depth of origin.
- **★★★** A stripping factor is wrong by 10%. Predict the activity error and state
  the measurement that would detect the mistake.

## Mastery checkpoint
Complete this without notes:

> A potassium window with a background of $1600$ counts per $60\ \mathrm{s}$
> records $1760$ counts at a station. **(a)** Compute the net count, its one-sigma
> uncertainty, and decide whether it is a detection using $L_C$ at 95%.
> **(b)** State the smallest true K-40 excess that would be detected 95% of the
> time. **(c)** Compute the depth above which 90% of the gamma signal originates
> for the teaching soil, and state the mean depth of origin. **(d)** A colleague
> reports the result as a potassium concentration without a calibration. State two
> reasons that is not yet a measurement. **(e)** State what more counting time
> would and would not fix.

A worked version of (a)–(c) appears in the exercise solutions.

## Common pitfalls
1. **Confusing $L_C$ with $L_D$.** One is a reporting rule, the other a
   performance figure; they differ by a factor of about $2$.
2. **Quoting one "depth of investigation".** The mean depth $\bar z = 1/(2\mu)$ is
   a few centimetres while the 90% depth is several times larger.
3. **Forgetting that attenuation is a product.** Count rate responds to activity
   *and* to density *and* to composition; a change in any one looks like a change
   in the others.
4. **Treating the stripping matrix as exact.** A 5% wrong factor puts almost all
   of the error on one activity.
5. **Assuming the neutron gauge calibration transfers between materials.** It is a
   property of the matrix and of the water chemistry.
6. **Ignoring build-up.** Multiple scattering makes the effective attenuation
   coefficient smaller than $\mu$; calibrate against a standard.
7. **Reporting a detection without its confidence convention.** "Significant" is
   meaningless without the $k$ and the background.
8. **Reading a gamma map as a depth map.** The method is a surface geochemistry
   map with a fixed, shallow depth of origin.

## Related modules
- [10-05-03 Thermal Methods for Shallow Subsurface Investigation](03-thermal-nearsurface.md) —
  the sibling method whose depth scale is an attenuation length rather than a
  wavelength.
- [10-05-05 Integrating Near-Surface Methods](05-multi-method-nearsurface.md) —
  combining a geochemical map with an electrical and an elastic one.
- [05-08 Borehole and Well-Log Geophysics](../../05-core-geophysics/08-geophysical-logging/README.md) —
  the borehole versions of the density and moisture gauges.
- [05-02-03 Noise and Drift](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) —
  the random-versus-systematic distinction that this lesson quantifies.
- [04-06 Petroleum and Mineral Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/README.md) —
  the geochemistry that a radiometric map is a proxy for.
