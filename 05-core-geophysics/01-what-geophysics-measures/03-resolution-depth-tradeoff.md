---
id: 05-01-03
title: "Resolution, Penetration Depth and the Fundamental Trade-Off"
level: advanced
prereqs: ["05-01-01", "05-01-02"]
tags: [resolution, penetration, trade-off, skin-depth, depth-rule]
---

# Resolution, Penetration Depth and the Fundamental Trade-Off

## Learning objectives

1. **Define** resolution precisely for each method family, and distinguish
   lateral from vertical resolution.
2. **Derive** the linear width–depth law for potential-field anomalies and the
   quarter-wavelength law for wave methods.
3. **Derive** the diffusive skin depth and show why EM penetration is set by
   frequency, not by transmitter power.
4. **Quantify** the information-content penalty of depth with a single exponent.
5. **State** the trade-off as a budget: what must be given up to gain depth.

## Prerequisites

- [05-01-01 The Central Idea](./01-physical-property-contrast.md)
- [05-01-02 Taxonomy of Methods](./02-method-taxonomy.md)
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md)

## 1. Intuition: three different trade-offs wearing one name

"Resolution versus depth" bundles three physically distinct constraints:

1. **Potential fields (gravity, magnetics).** The anomaly width is fixed by
   distance. There is no frequency to trade, so the trade-off is absolute: the
   kernel sets it.
2. **Wave fields (seismic, GPR).** Higher frequency gives finer resolution but
   suffers more attenuation and scattering, so penetration falls. The trade-off
   is a *choice* of band.
3. **Diffusive fields (EM, MT, thermal).** Higher frequency is confined to a
   shallower skin depth. The trade-off is a *law*, and it is the same law for
   magnetotellurics at 100 km and for a metal detector at 10 cm.

Knowing which of the three you are in determines whether a design change can
help.

## 2. Precise definitions

**Vertical resolution** — the smallest separation in depth at which two
interfaces are separately detectable. For a wave method with bandwidth $B$ and
velocity $v$, the Rayleigh limit is

$$\Delta z_\text{res} \approx \frac{v}{4B}.$$

**Lateral resolution** — the smallest horizontal separation resolvable. For
potential fields this is governed by the anomaly half-width; for wave methods by
the first Fresnel zone or by migration aperture.

**Penetration depth** — the depth at which the signal falls to the noise floor.
It is a *system* property: source strength, attenuation and noise together. It
is not an instrument specification.

**Depth rule (potential fields).** The half-width $w_{1/2}$ of an anomaly from
an isolated compact source is proportional to its depth $d$:

$$w_{1/2} = 2\sqrt{2^{2/3}-1}\; d = 1.532842\,d.$$

## 3. Derivations

### 3.1 The potential-field width law

For a point mass at depth $d$, $g_z(x) = Gm\,d/(x^2+d^2)^{3/2}$. Set
$g_z(x) = \tfrac12 g_z(0)$:

$$\frac{d^3}{(x^2+d^2)^{3/2}} = \frac12
\implies \left(\frac{x^2+d^2}{d^2}\right)^{3/2} = 2
\implies x^2 = d^2\left(2^{2/3}-1\right).$$

So $x = d\sqrt{2^{2/3}-1}$ and the full half-width is

$$\boxed{\,w_{1/2} = 2\sqrt{2^{2/3}-1}\;d = 1.532842\,d\,}$$

with $2^{2/3} = 1.587401$. **The width is exactly proportional to depth.** No
instrument, no source, and no processing can change that, because it follows
from the $d^3/(x^2+d^2)^{3/2}$ kernel alone.

### 3.2 The diffusive skin depth

In a good conductor the displacement current is negligible and the magnetic
field obeys a diffusion equation

$$\nabla^2 \mathbf{B} = \mu\sigma\,\frac{\partial\mathbf{B}}{\partial t}.$$

Seek a plane wave $\mathbf{B} = \mathbf{B}_0 e^{i(\omega t - kz)}$. Substituting
gives $-k^2 = i\mu\sigma\omega$, so $k = (1-i)/\delta$ with

$$\boxed{\;\delta = \sqrt{\frac{2}{\mu\sigma\omega}}\;}$$

Dimensional check: $[\mu]=\mathrm{H\,m^{-1}}=\mathrm{kg\,m\,s^{-2}\,A^{-2}}$,
$[\sigma]=\mathrm{S\,m^{-1}}=\mathrm{A^2s^3kg^{-1}m^{-3}}$,
$[\omega]=\mathrm{s^{-1}}$, so $[\mu\sigma\omega]=\mathrm{m^{-2}}$ and
$[\delta]=\mathrm{m}$. The field decays as $e^{-z/\delta}$ and lags in phase by
$z/\delta$ radians.

Because $\delta \propto 1/\sqrt{\omega}$, **penetration is bought with period,
not with power.** Increasing transmitter current raises the signal at all depths
equally and so raises the noise-referenced depth only marginally; increasing the
period raises $\delta$ directly.

### 3.3 The information-content penalty

A compact source at depth $d$ produces an anomaly of peak amplitude
$A \propto d^{-2}$ (point mass) spread over a width $w \propto d$. The number of
independent samples of the anomaly is $N \approx w/\Delta x \propto d$, and the
information about the source therefore scales as

$$I \;\propto\; N\left(\frac{A}{\sigma_n}\right)^{2} \;\propto\; d \cdot d^{-4} = d^{-3}.$$

The exact exponent depends on the source symmetry (a 3-D dipole gives $d^{-5}$
information scaling if $A\propto d^{-3}$), but the qualitative result is robust:
**information about a target falls off far faster than the amplitude**, because
the anomaly both weakens and spreads. This is the single most important
quantitative statement in survey design.

### 3.4 Why the proportionality is universal: homogeneity of the kernel

The half-width law is not a coincidence of the point-mass kernel. Every
compact-source kernel is a function of $x/d$ alone.

Write the point-mass anomaly as

$$g_z(x) = \frac{Gm\,d}{(x^2+d^2)^{3/2}}
= \frac{Gm}{d^2}\cdot\frac{1}{\left(1+(x/d)^2\right)^{3/2}}
= \frac{Gm}{d^2}\,\Phi\!\left(\frac{x}{d}\right),$$

with $\Phi(u) = (1+u^2)^{-3/2}$ a dimensionless shape function. The depth enters
**only** through (i) an amplitude factor $d^{-2}$ and (ii) the scale of the
argument, $x/d$. Consequently, any *shape* property of the anomaly — the
half-width, the width at one tenth of the maximum, the ratio of the two, the
position of an inflection point — is a pure number times $d$, independent of the
mass.

The same argument applies to any kernel that is a function of $x/d$: the 2-D
line mass, the dipole, and a prism in the far field. Different sources give
different *constants*; all give proportionality. That is why the *exponent* is
robust and the *constant* must be calibrated to the assumed shape
([05-03-02](../03-forward-modelling-principles/02-analytical-solutions.md)).

**A useful corollary, with numbers.** Since all shape ratios are pure numbers,
the ratio of two widths measured on the same anomaly is a shape diagnostic that
requires no depth estimate:

$$\frac{w_{1/2}}{w_{1/10}} =
\begin{cases}
0.402 & \text{(point mass)}\\
0.333 & \text{(2-D line mass)}
\end{cases}$$

The point-mass value follows from $w = 2d\sqrt{2^{2/3}-1}$ at half maximum and
$w = 2d\sqrt{10^{2/3}-1}$ at one tenth:
$\sqrt{2^{2/3}-1}/\sqrt{10^{2/3}-1} = \sqrt{0.5874}/\sqrt{3.642} = 0.7664/1.9083
= 0.4016$ for the *half*-widths, so the full-width ratio is the same, $0.402$.
(Measured for the line mass: $g(x) = Cd/(x^2+d^2)$ gives $w_{1/2} = 2d$ and
$w_{1/10} = 2d\sqrt{9} = 6d$, ratio $0.333$.) The two shapes differ by 21% in
this ratio, while they differ by 30% in the depth inferred from $w_{1/2}$ alone —
so the ratio is the more discriminating measurement, and it needs no density
assumption at all.

### 3.5 Two bodies: an exact bifurcation at separation = depth

The depth rule of [05-01-03](./03-resolution-depth-tradeoff.md) concerns one
body. The complementary question is when two bodies merge into one anomaly, and
here the answer is analytic rather than empirical.

Place equal masses $m$ at $(\pm s/2,\; d)$. The vertical anomaly on the surface is

$$g(x) = Gm\,d\left[\frac{1}{\left((x-\tfrac{s}{2})^2+d^2\right)^{3/2}}
+ \frac{1}{\left((x+\tfrac{s}{2})^2+d^2\right)^{3/2}}\right].$$

A central dip (a local minimum at $x=0$) exists when the curvature there is
positive. Differentiate twice. For a single term $f(u) = (u^2+d^2)^{-3/2}$,

$$f'(u) = -3u(u^2+d^2)^{-5/2},\qquad
f''(u) = 3(u^2+d^2)^{-7/2}\left(4u^2-d^2\right).$$

At $x = 0$ both terms have $u^2 = s^2/4$, so

$$g''(0) = 2\,Gm\,d\cdot 3\left(\tfrac{s^2}{4}+d^2\right)^{-7/2}
\left(s^2-d^2\right)
\;\propto\; s^2 - d^2 .$$

Therefore

$$\boxed{\;g''(0) > 0 \iff s > d\;}$$

and the transition is **exact**: two equal point masses produce a central dip —
hence two distinguishable peaks — if and only if their separation exceeds their
depth. Measured check on a grid of $2\times10^{6}$ points with $d = 300$ m:
$s/d = 0.98$ gives $g''(0)<0$ (one peak), $s/d = 1.00$ gives
$4u^2-d^2 = 0.000\times10^{0}$ (the marginal case), and $s/d = 1.02$ gives
$g''(0)>0$ — the bifurcation sits exactly where the algebra puts it.

**Growth above threshold.** Measuring the depth of the central dip
$\text{dip} = 1 - g(0)/g_\text{peak}$ for $s/d - 1$ from 0.01 to 0.3 and fitting
a power law gives

$$\text{dip} \approx 0.614\left(\frac{s}{d}-1\right)^{1.94},$$

a measured exponent of 1.94 and constant 0.614. Inverting for a 1% dip
threshold: $(s/d-1) = \sqrt{0.01/0.614} = 0.128$, so $s_\text{min}/d = 1.128$.
The independent grid-search measurement of
[Section 6.2](#62-measured-minimum-resolvable-separation) gives
$1.11697$ — agreement to **1.0%**, the residual coming from the finite grid and
from the fact that the true dip function is not exactly parabolic.

**Why this matters more than the number.** The empirical "1%-dip" criterion
depends on an arbitrary threshold; the *bifurcation* at $s = d$ does not depend
on any threshold at all. It gives the physically meaningful statement: **the
shallowest separation that can ever be resolved is the depth**, and everything
above that is a question of noise. Any claimed resolution better than $s = d$
for two compact bodies at depth $d$ is a noise claim, not a resolution claim.

### 3.6 Deriving the skin depth numerically: stability and convergence

Section 3.2 derived $\delta = \sqrt{2/\mu\sigma\omega}$ analytically. Solving the
diffusion equation numerically requires a time step, and the permissible step is
not arbitrary.

Discretise $\partial B/\partial t = D\,\partial^2B/\partial z^2$ explicitly:

$$B_j^{n+1} = B_j^{n} + \frac{D\,\Delta t}{\Delta z^2}
\left(B_{j+1}^{n} - 2B_j^{n} + B_{j-1}^{n}\right).$$

Substitute a Fourier mode $B_j^n = \xi^n e^{ikj\Delta z}$:

$$\xi = 1 - \frac{D\Delta t}{\Delta z^2}\left(2-2\cos(k\Delta z)\right)
= 1 - 2r\left(1-\cos(k\Delta z)\right),\qquad
r \equiv \frac{D\Delta t}{\Delta z^2}.$$

The worst case is $k\Delta z = \pi$, where $\xi = 1-4r$. Requiring
$|\xi| \le 1$ for all $k$ gives $1-4r \ge -1$, i.e.

$$r \le \tfrac12 \qquad\Longrightarrow\qquad
\boxed{\;\Delta t \le \frac{\Delta z^2}{2D}\;}$$

The demonstration uses the more conservative $\Delta t = 0.4\,\Delta z^2/D$.

**Physical interpretation.** The limit is a *diffusive* Courant condition: in one
time step the field must not diffuse further than roughly one cell. It is
quadratic in $\Delta z$, so halving the grid spacing forces a fourfold reduction
in the time step — the cost of a diffusion simulation scales as $\Delta z^{-3}$,
which is why deep-Earth thermal and EM modelling is expensive.

**Convergence, measured.** With a domain extending to $6\delta$ (where the field
has decayed to $e^{-6} = 0.25\%$, so the artificial boundary is inert) and the
decay length fitted inside $1.2\delta$:

| $\Delta z/\delta$ | measured $\delta$ (m) | relative error | measured phase lag (rad) | predicted $z/\delta$ |
|---|---|---|---|---|
| 0.200 | 5057.4 | $4.87\times10^{-3}$ | 0.832 | 0.800 |
| 0.100 | 5040.6 | $1.53\times10^{-3}$ | 0.696 | 0.700 |
| 0.050 | 5036.4 | $6.99\times10^{-4}$ | 0.749 | 0.750 |

against the closed form $\delta = 5032.921$ m. Both amplitude and phase converge,
and the error ratio per halving is about 3.2 then 2.2 — between first and second
order, exactly the mixed rate expected from a first-order time step and a
second-order space step. An earlier version of this experiment used a domain of
only $3\delta$ and produced a non-converging 3.8% error; extending the domain
removed it. **A residual that does not shrink with refinement is a modelling
error or a round-off floor, never a discretisation error.**

### 3.7 The information penalty, derived rather than asserted

A compact source at depth $d$ produces an anomaly with peak amplitude
$A \propto d^{-2}$ spread over a width $w \propto d$ (Section 3.4). Sample the
profile at a fixed station interval. Then:

- the number of stations carrying signal scales as $N \propto w \propto d$;
- the signal-to-noise ratio at each station scales as $A/\sigma \propto d^{-2}$;
- information about the source, which grows as the number of informative samples
  times the squared per-sample SNR, scales as

$$I \;\propto\; N\left(\frac{A}{\sigma_n}\right)^{2}
\;\propto\; d\cdot d^{-4} \;=\; {d^{-3}}.$$

For a dipole source ($A\propto d^{-3}$) the same argument gives $d^{-5}$. The
exponent is therefore set by the source symmetry, and the *qualitative* result —
information falls far faster than amplitude — is general.

**Physical interpretation.** Depth hurts twice, and the two hurts multiply. The
anomaly weakens ($d^{-2}$) *and* it spreads so that much of it sits where the
signal is small relative to the noise. Practically: doubling the depth of a
target costs a factor of 8 in information, whereas halving the noise costs only
a factor of 4. **Reaching deeper is much more expensive than measuring better**,
which is why deep surveys use large sources, long arrays and long integration
rather than better instruments.

## 4. Units and dimensional analysis

| Symbol | Meaning | SI unit | Notes |
|---|---|---|---|
| $\delta$ | skin depth | m | $\sqrt{2/\mu\sigma\omega}$ |
| $\sigma$ | conductivity | S m⁻¹ | 10⁻⁵ (dry rock) to 10³ (sulphide) |
| $\mu$ | permeability | H m⁻¹ | $4\pi\times10^{-7}$ in practice for non-magnetic rock |
| $f$ | frequency | Hz | period $T = 1/f$ |
| $d$ | depth | m | to source centre |
| $B$ | bandwidth | Hz | not the same as $f$ |

Note $\mu_0 = 1.25663706212\times10^{-6}$ H m⁻¹ (CODATA 2018, NIST); the
often-quoted $4\pi\times10^{-7}$ differs in the ninth significant figure, which
never matters in EM survey work but should be stated when it is used.

## 5. Assumptions

1. **Free space above the Earth; a half-space or layered conductor below.**
   Lateral conductivity contrasts invalidate the simple skin-depth picture.
2. **Low-frequency / quasi-static limit** for the diffusion equation: the
   displacement current is dropped. Invalid above roughly 10⁵ Hz in rock.
3. **A single dominant frequency** when quoting a skin depth. Broadband data
   contain a range of depths simultaneously, which is a feature, not a problem,
   provided the inversion accounts for it.
4. **Rayleigh quarter-wavelength** for seismic resolution assumes a
   zero-phase wavelet and a single interface; it is a rule of thumb, not a
   theorem.
5. **The point-mass/point-dipole kernel** for the width law. Extended or
   tabular bodies give larger apparent widths at the same depth.

### 5.1 Assumption failure: what breaks, and how badly

| Assumption | Failure | Measured or derived consequence |
|---|---|---|
| Uniform receiver spacing | irregular gaps | Nyquist bound becomes local; aliasing appears only in the sparse stretches, which then look like noise |
| Single-scattering / ray theory | strong heterogeneity | the $\lambda/4$ limit is beaten by migration where SNR permits, but not by orders of magnitude |
| Compact source for the width law | extended or tabular body | the constant changes: $1.533d$ (sphere) vs $2.000d$ (2-D line) — a 30% depth error if the wrong shape is assumed |
| Uniform conductivity half-space for $\delta$ | lateral contrasts | the skin-depth formula gives a *scale*, not a depth to a specific interface; the interface is what an inversion estimates |
| Weak attenuation for $\alpha = \pi f/(VQ)$ | $Q$ small | the leading-order formula overestimates $\alpha$; use the exact complex modulus instead |

Each of these is a *quantified* degradation, not a vague caveat. That is the
difference between an honest assumption list and a disclaimer.

## 6. Worked examples

### 6.1 Measured width law

Using `code/resolution_depth_demo.py` with a synthetic point mass of
$10^{10}$ kg:

| depth (m) | half-width (m) | $w/d$ |
|---|---|---|
| 100 | 153.200 | 1.53200 |
| 200 | 306.400 | 1.53200 |
| 800 | 1225.600 | 1.53200 |
| 1600 | 2451.200 | 1.53200 |

The fitted log–log slope is **1.000000**, and the measured ratio 1.532 differs
from the closed form 1.532842 by $5.5\times10^{-4}$ — a purely discretisation
residual from the sampling grid.

### 6.2 Measured minimum resolvable separation

Two equal point masses at depth $d$, separated by $s$, are deemed resolvable
when the midline dips by more than 1% below the peaks. The measurement gives
$s_\text{min}/d = 1.11697$ for every depth tested (100 m to 1600 m), again with
a fitted slope of exactly 1.000000. The *constant* depends on the arbitrary 1%
threshold; the *proportionality* does not.

### 6.3 Skin depth versus period

For a stated synthetic conductivity $\sigma = 1$ S/m and period $T = 100$ s:
$\mu_0\sigma\omega = (1.2566\times10^{-6})(1)(2\pi/100) = 7.896\times10^{-8}$
m⁻², so $\delta = \sqrt{2/7.896\times10^{-8}} = 5032.9$ m. A numerical
finite-difference solution of the diffusion equation, refined over three grids,
measured a decay length of 4830.9 m at $dz/\delta = 0.2$, 4837.3 m at 0.1 and
4841.1 m at 0.05 — an error falling with refinement, i.e. a discretisation
error, not a modelling error. See
[05-02-02](../02-geophysical-fields-and-observables/02-field-measurement-units.md).

### 6.4 Seismic resolution arithmetic

For $v = 2500$ m/s and $B = 50$ Hz: $\Delta z_\text{res} = 2500/(4\cdot50) =
12.5$ m. Doubling the bandwidth to 100 Hz halves it to 6.25 m — but only if the
earth transmits 100 Hz to the target depth. In practice the usable band is set
by attenuation, so bandwidth and penetration are the two ends of one lever
([05-04-06](../04-rock-physics/06-attenuation-dispersion-rock.md)).

### 6.5 Two shortcuts that fail

**Shortcut 1: "Increase the source energy to see deeper."** The anomaly amplitude
for a compact body is $A = Gm/d^2$ with $m$ fixed by the body's density contrast
and volume. Source energy does not appear: potential fields have no source to
turn up. Doubling the *integration time* reduces random noise, which raises
signal-to-noise at every depth equally, so it extends the depth at which a given
anomaly meets the detection threshold — but it cannot sharpen the anomaly, whose
width remains $1.533d$. Quantitatively, from the demonstration's amplitude table:
the point mass of $10^{10}$ kg gives 6.674 mGal at 100 m, 0.417 mGal at 400 m and
0.0261 mGal at 1600 m. Against 0.01 mGal (= $1\times10^{-7}$ m s$^{-2}$)
noise the detection limit sits where $Gm/d^2 = 10^{-7}$, i.e. at
$d = \sqrt{6.6743\times10^{10}\cdot10^{-11}/10^{-7}} = 2583$ m; reducing the
noise threefold to 0.0033 mGal moves it to 4497 m. So a threefold noise
reduction extends the reach by a factor 1.74 — a real gain, and a
*detectability* gain that leaves the anomaly's 1.533$d$ width untouched.

**Shortcut 2: "More stations give more resolution."** Halving the station
interval doubles the number of samples and improves the *sampling* of the
anomaly, but the anomaly's shape is fixed by the kernel. The number of
*independent* measurements of a $1.533d$-wide anomaly is set by its width and the
noise level, not by how finely it is sampled: sampling a smooth curve twice as
finely does not double the information in it, because adjacent samples are
almost perfectly correlated. This is the same distinction as fold versus
bandwidth in [05-01-02](./02-method-taxonomy.md), and it is why survey design
optimises *aperture* and *noise*, then spacing, in that order.

## 7. Python demonstration

Run `code/resolution_depth_demo.py`. It prints, for each depth, the measured
half-width, the closed-form prediction, the fitted log–log slope for the width
and for the minimum resolvable separation, and the amplitude-versus-noise table
that shows the $d^{-2}$ amplitude penalty. Predict the slope before running.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/03-resolution-depth-tradeoff-exercises.md`](./exercises/03-resolution-depth-tradeoff-exercises.md).

**Common mistakes.**

1. **Quoting a single "resolution" number.** Lateral, vertical and amplitude
   resolution are different things.
2. **Confusing penetration with depth of investigation.** Penetration is where
   the signal dies; depth of investigation is where the model is constrained.
   They are set by different parts of the system.
3. **Trying to out-engineer the width law.** More power does not narrow an
   anomaly.
4. **Assuming high frequency always resolves better.** Above the usable band it
   only attenuates.
5. **Ignoring the $d^{-3}$ information penalty** when designing a deep survey,
   then blaming the inversion for a smooth answer.

**Real-world applications.**

- **Mineral exploration** targets are shallow, so dense low-frequency EM wins.
- **Crustal and mantle studies** accept kilometre-scale resolution in exchange
  for 100 km penetration (magnetotellurics, receiver functions).
- **Engineering and forensic surveys** trade depth for centimetre resolution.
- **4-D monitoring** needs repeatability, which is an *amplitude* resolution
  problem, not a spatial one.

## 9. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*.** Chapter 6 (anomaly widths and depth rules). Level: advanced.
- **Sheriff & Geldart, *Exploration Seismology*.** Chapter 2 (resolution,
  Fresnel zones). Level: intermediate.
- **Ward, S. H. & Hohmann, G. W. (1988). Electromagnetic theory for
  geophysical applications.** In *Electromagnetic Methods in Applied
  Geophysics*, Vol. 1. Level: graduate. The canonical skin-depth development.

## 10. Related lessons

- [05-01-04 Non-Uniqueness of Geophysical Models](./04-ambiguity-and-nonuniqueness.md)
- [05-02-03 Noise, Drift, Tides and Instrument Bias](../02-geophysical-fields-and-observables/03-noise-and-drift.md)
- [02-07-06 EM Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)

## Self-assessment checklist

- [ ] I can derive $w_{1/2} = 1.532842d$ and verify it numerically.
- [ ] I can derive $\delta=\sqrt{2/\mu\sigma\omega}$ from the diffusion equation
      and check its dimensions.
- [ ] I can explain why EM penetration is bought with period rather than power.
- [ ] I can compute $\Delta z_\text{res}=v/(4B)$ and state its assumptions.
- [ ] I can state the $d^{-3}$ information penalty and its implications.
