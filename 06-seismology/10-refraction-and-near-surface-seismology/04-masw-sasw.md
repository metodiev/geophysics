---
id: 06-10-04
title: "MASW/SASW: Surface-Wave Dispersion and Vs Profiles"
level: advanced
prereqs: ["06-01-03", "06-10-01"]
tags: [seismology, near-surface, surface-waves, dispersion, masw, vs-profile]
---

# MASW/SASW: Surface-Wave Dispersion and Vs Profiles

> **All models and data in this module are SYNTHETIC.** The layered model, the
> frequencies, the noise level and the grid of trial models are chosen teaching
> values. No field dispersion curve, site or borehole is used, and no published
> $V_S$ profile is referred to.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Love-wave dispersion relation for one layer over a half-space
   from the wave equation, the free-surface condition and the two interface
   conditions, and **state** the two exact limits $c \to v_{s2}$ as
   $f \to 0$ and $c \to v_{s1}$ as $f \to \infty$.
2. **Explain** why a dispersion curve is a sounding rather than a single
   measurement, and **compute** the wavelength and the $\lambda/3$ depth estimate
   at any frequency.
3. **Measure** the depth sensitivity of the curve through its logarithmic
   Jacobian, and **quantify** the thickness–velocity trade-off (correlation
   $-0.936$ for the demonstration model).
4. **Explain** why the solution of a dispersion inversion is a *set* of acceptable
   models and **measure** the width of that set at a stated noise level.
5. **Show** how the frequency band and the receiver offset determine which depths
   are constrained, and **state** which end of the band controls which parameter.
6. **Distinguish** the active MASW and SASW geometries, and **state** what each
   costs in resolution and field time.
7. **State** the assumptions that make a 1-D dispersion inversion valid, and the
   two that most often fail at a real site.

## Prerequisites

- [06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity](../01-elastic-wave-propagation/03-surface-waves.md) —
  why surface waves disperse, and the meaning of a mode.
- [01 Refraction Survey Geometry and Travel-Time Interpretation](01-refraction-basics.md) —
  the spread, the offset and the first-arrival bookkeeping that the same field
  layout also produces.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  the multichannel records this method analyses.

## 1. Intuition: the noise that carries the answer

In reflection and refraction work, ground roll is the enemy: a slow, high-amplitude
train that arrives after the first breaks and buries the reflections. Its
diagnostic property, the one that gets it filtered out, is that it **disperses** —
different frequencies travel at different speeds. A refraction interpretation
throws that away. This lesson does the opposite: it treats the dispersion as the
signal and asks what it says about the shear-wave velocity beneath the line.

Two physical facts make the method work.

- **Surface waves are trapped near the free surface.** A mode's amplitude decays
  with depth, and the depth of the decay scales with wavelength. Long wavelengths
  sample deep, short wavelengths sample shallow. That is a sounding.
- **The Love and Rayleigh dispersion relations depend on shear velocity, density
  and layer thickness, and on nothing else about the source.** The source sets
  amplitude and band, not the curve. So the curve can be inverted for a $V_S$
  profile without knowing the source.

Two physical facts limit it, and they are the honest difficulty of this lesson.

- **Phase velocity is bounded by the body-wave velocities.** For the model below,
  the curve can never leave the interval between $200$ and
  $800\ \mathrm{m\,s^{-1}}$ no matter how accurately it is measured. A dispersion
  curve is a shape inside a bracket, not a free measurement.
- **Thickness and velocity trade off.** Over most of the band a thinner, faster
  layer produces almost exactly the same curve as a thicker, slower one. The
  solution is therefore a *ridge* in model space, and the width of that ridge is
  set by the noise level, not by the inversion algorithm.

## 2. Precise definitions

| Term | Meaning |
|---|---|
| phase velocity $c(f)$ | speed of a constant-phase point of a single frequency |
| group velocity $U(f)$ | speed of the envelope; $U = c + f\,\mathrm{d}c/\mathrm{d}f$ |
| dispersion curve | $c$ as a function of $f$ |
| fundamental mode | the slowest trapped mode at each frequency |
| higher modes | faster trapped modes, with more depth oscillations |
| MASW | multichannel analysis of surface waves: many receivers, active source, usually $f$–$k$ or phase-shift imaging |
| SASW | spectral analysis of surface waves: two receivers, phase difference as a function of frequency |
| $\lambda/3$ rule | the conventional depth attributed to a wavelength |

The active methods differ in how the phase difference between receivers is
estimated. MASW uses an array and transforms to the frequency–wavenumber domain,
so that a coherent surface wave appears as a ridge whose slope at each frequency
is the phase slowness; the fundamental mode is picked from the ridge. SASW uses
two receivers and computes the phase of the cross-spectrum, which requires the
analyst to resolve the $2\pi$ ambiguity ("unwrapping") at every frequency — cheap
in equipment, fragile in processing. Passive variants (usually written
reMi, passive MASW, or microtremor array methods) use ambient noise instead of a
hammer and reach longer wavelengths, hence greater depths, at the cost of
attributing the energy to the wrong mode.

## 3. Derivation of the Love-wave dispersion relation

For a closed-form derivation that can be checked numerically, take SH motion
$u(z)$ polarised along $y$, with $z$ measured **downward** from the free surface,
a layer of thickness $H$, shear velocity $v_{s1}$ and rigidity $\mu_1 =
\rho_1 v_{s1}^{2}$ over a half-space with $\mu_2 = \rho_2 v_{s2}^{2}$. Let $k =
\omega/c$ be the horizontal wavenumber and

$$k_1^{2} = \frac{\omega^{2}}{v_{s1}^{2}} - k^{2}, \qquad
k_2^{2} = k^{2} - \frac{\omega^{2}}{v_{s2}^{2}}.$$

A trapped mode requires $v_{s1} < c < v_{s2}$, so that $k_1$ is real inside the
layer (oscillatory) and $k_2$ is real in the half-space (decaying).

**Free surface.** Zero traction at $z = 0$ means $\mathrm{d}u/\mathrm{d}z = 0$;
writing the layer field as $u_1 = A\cos(k_1 z)$ satisfies it identically.

**Half-space.** Only the decaying solution is physical,
$u_2 = B e^{-k_2(z-H)}$.

**Continuity at $z = H$.** Displacement gives
$A\cos(k_1H) = B$; traction $\mu\,\mathrm{d}u/\mathrm{d}z$ gives
$-\mu_1 A k_1\sin(k_1H) = -\mu_2 B k_2$. Substituting $B$ and dividing by
$\cos(k_1H)$:

$$\tan\left(k_1H\right) = \frac{\mu_2}{\mu_1}\frac{k_2}{k_1},$$

or, in the form the demonstration solves,

$$\boxed{\;\sin x - \frac{\mu_2}{\mu_1}
\frac{\sqrt{1/c^{2} - 1/v_{s2}^{2}}}{\sqrt{1/v_{s1}^{2} - 1/c^{2}}}\cos x = 0,
\qquad x = \omega H\sqrt{\frac{1}{v_{s1}^{2}} - \frac{1}{c^{2}}}.}\;}$$

The substitution $x = k_1 H$ removes the poles of $\tan$, so the roots can be
found by scanning for sign changes of $g(x) = \sin x - R\cos x$ with $R$ the
right-hand side: the **smallest root is the fundamental mode**, and successive
roots are the higher modes, which are faster at the same frequency. This is
exactly what the demonstration does.

### 3.1 The two exact limits

- **$f \to 0$: $c \to v_{s2}$.** Physically, a very long wave is barely aware of a
  thin layer, so it travels at the half-space speed. Algebraically, $c = v_{s2}$
  makes the right-hand side zero, so the root is $x = 0$, i.e. $\omega \to 0$.
- **$f \to \infty$: $c \to v_{s1}$.** A very short wave is confined to the layer
  and travels at the layer speed. At $c = v_{s1}$ the left-hand square root in the
  denominator vanishes.

The demonstration measures both limits on its SYNTHETIC model
($v_{s1} = 200\ \mathrm{m\,s^{-1}}$, $\rho_1 = 1800\ \mathrm{kg\,m^{-3}}$,
$H = 10\ \mathrm{m}$; $v_{s2} = 800\ \mathrm{m\,s^{-1}}$,
$\rho_2 = 2000\ \mathrm{kg\,m^{-3}}$; rigidity ratio $\mu_2/\mu_1 = 17.778$):

| $f$ (Hz) | $c$ (m/s) | $c/v_{s2}$ | $c/v_{s1}$ |
|---|---|---|---|
| 0.01 | 799.992 | 0.99999 | 4.0000 |
| 0.10 | 799.916 | 0.99990 | 3.9996 |
| 1.00 | 798.132 | 0.99767 | 3.9907 |
| 10.00 | 229.359 | 0.28670 | 1.1468 |
| 100.00 | 200.250 | 0.25031 | 1.0012 |
| 1000.00 | 200.002 | 0.25000 | 1.0000 |

At $f = 0.01\ \mathrm{Hz}$ the computed value is within $0.0010\%$ of
$v_{s2}$; at $f = 1000\ \mathrm{Hz}$ it is within $0.0012\%$ of $v_{s1}$. **The
phase velocity is bounded by the two body-wave velocities: a dispersion curve
alone cannot produce a velocity outside that bracket, however accurately it is
recorded.**

### 3.2 Phase velocity, wavelength and the $\lambda/3$ estimate

| $f$ (Hz) | $c$ (m/s) | $\lambda$ (m) | $\lambda/3$ (m) | $c/2f$ (m) |
|---|---|---|---|---|
| 2.0 | 790.98 | 395.49 | 131.83 | 197.74 |
| 5.0 | 472.12 | 94.42 | 31.47 | 47.21 |
| 10.0 | 229.36 | 22.94 | 7.65 | 11.47 |
| 20.0 | 206.43 | 10.32 | 3.44 | 5.16 |
| 30.0 | 202.80 | 6.76 | 2.25 | 3.38 |
| 50.0 | 201.00 | 4.02 | 1.34 | 2.01 |

$\lambda = c/f$ is exact; $\lambda/3$ is a **rule of thumb**, not a derivation: it
is the depth at which the mode's sensitivity to a thin perturbation peaks, and it
moves with frequency, which is what makes the curve a sounding. $c/2f$ is the
other common rule, half the wavelength; the two disagree by a factor of $1.5$ at
every frequency by construction, which is the reason a depth from a dispersion
curve must always be stated with the convention used to obtain it.

## 4. What the curve constrains: the Jacobian

Differentiate the dispersion relation with respect to each parameter and form the
relative-sensitivity matrix $J_{ij} = \partial\ln c(f_i)/\partial\ln p_j$ for
$p = (H, v_{s1}, v_{s2})$:

| $f$ (Hz) | $\partial\ln c/\partial\ln H$ | $\partial\ln c/\partial\ln v_{s1}$ | $\partial\ln c/\partial\ln v_{s2}$ |
|---|---|---|---|
| 2.0 | $-0.02869$ | $0.05453$ | $0.97416$ |
| 5.0 | $-2.51077$ | $3.37332$ | $0.13744$ |
| 10.0 | $-0.30633$ | $1.30574$ | $0.00059$ |
| 20.0 | $-0.06467$ | $1.06462$ | $0.00004$ |
| 30.0 | $-0.02803$ | $1.02801$ | $0.00001$ |
| 50.0 | $-0.00999$ | $1.00999$ | $0.00000$ |

Read it row by row. At $2\ \mathrm{Hz}$ the curve is sensitive to the **half-space
velocity** ($0.974$) and almost blind to everything else. At $50\ \mathrm{Hz}$ it
is sensitive only to the **layer velocity** ($1.010$), and a velocity change maps
almost one-for-one into a phase-velocity change. In between, around
$5\ \mathrm{Hz}$, all three matter.

Now the correlation between columns:

$$\mathrm{corr}\!\left(\frac{\partial\ln c}{\partial\ln H},
\frac{\partial\ln c}{\partial\ln v_{s1}}\right) = -0.9356,\qquad
\mathrm{corr}\!\left(\frac{\partial\ln c}{\partial\ln H},
\frac{\partial\ln c}{\partial\ln v_{s2}}\right) = +0.0892.$$

**The $H$ and $v_{s1}$ columns are almost perfectly anticorrelated over this
band.** A thinner layer with a faster velocity produces almost the same curve as a
thicker layer with a slower one. The singular values of the
$6 \times 3$ relative-sensitivity matrix are $4.6499$, $1.05777$ and $0.96363$, a
condition number of $4.825$ — the small singular value is the direction in which
the data are nearly silent, and it is a direction that mixes $H$ and $v_{s1}$.

Note carefully what the correlation does *not* mean. It does not mean the
inversion will return a wrong layer; it means the *data alone* do not choose
between a family of models, and that the choice must come from something else:
the range of plausible velocities for the material, an independent $V_S$
measurement, or the low-frequency end of the band where the half-space is felt and
the trade is broken.

## 5. Worked example — checking one point of the curve

**Problem.** For the model above, verify that $c = 229.3587\ \mathrm{m\,s^{-1}}$
satisfies the dispersion relation at $f = 10\ \mathrm{Hz}$, and state the
wavelength and the two depth estimates.

**Step 1 — the argument.** With $\omega = 2\pi f = 62.8319\
\mathrm{rad\,s^{-1}}$ and $H = 10\ \mathrm{m}$,

$$x = \omega H\sqrt{\frac{1}{v_{s1}^{2}} - \frac{1}{c^{2}}}
= 628.319\sqrt{2.500000\times10^{-5} - 1.900945\times10^{-5}}
= 628.319 \times 0.002447560 = 1.537847\ \mathrm{rad}.$$

**Step 2 — the right-hand side.**
$\sqrt{1/c^{2}-1/v_{s2}^{2}} = \sqrt{1.900945\times10^{-5} - 1.5625\times10^{-6}}
= 4.176955\times10^{-3}$, and
$\sqrt{1/v_{s1}^{2}-1/c^{2}} = 2.447560\times10^{-3}$, so their ratio is
$1.706579$ and

$$\frac{\mu_2}{\mu_1} \times 1.706579 = 17.7778 \times 1.706579 = 30.3389.$$

**Step 3 — the check.** $\tan 1.537847 = 30.3389$. The two sides agree to five
digits, so $c = 229.3587\ \mathrm{m\,s^{-1}}$ is a root of the dispersion relation
at $10\ \mathrm{Hz}$: the physical root computed by the demonstration.

**Step 4 — the depth statements.** $\lambda = c/f = 22.9359\ \mathrm{m}$, so the
$\lambda/3$ estimate is $7.6453\ \mathrm{m}$ and the alternative
$c/2f = 11.4679\ \mathrm{m}$. **Two conventions, two depths, a factor of $1.5$
apart.** Neither is a measurement; both are sensitivity-weighted averages, and the
fixed answer to "what depth does this frequency see?" does not exist.

## 6. The trade-off ridge, measured

The demonstration takes the curve of Section 3.2 as a target, perturbs each
frequency by an independent $3\%$ relative error, and searches a grid of $1089$
models ($H$ from $4$ to $20\ \mathrm{m}$ in $0.5\ \mathrm{m}$ steps; $v_{s1}$ from
$140$ to $300\ \mathrm{m\,s^{-1}}$ in $5\ \mathrm{m\,s^{-1}}$ steps). A model is
"acceptable" if its RMS misfit is below the noise level of $3\%$.

| band | acceptable models | $H$ range (m) | $v_{s1}$ range (m/s) | corr$(H,v_{s1})$ | best fit |
|---|---|---|---|---|---|
| 8–40 Hz (short spread) | 6 of 1089 | 9.00–11.00 | 195.0–200.0 | $+0.7016$ | $H=10.00$, $v_{s1}=200.0$, RMS 2.101% |
| 1–10 Hz (wide band) | 3 of 1089 | 9.50–10.50 | 195.0–205.0 | $+1.0000$ | $H=10.00$, $v_{s1}=200.0$, RMS 1.643% |
| 1–40 Hz (both) | 2 of 1089 | 10.00–10.50 | 195.0–200.0 | $+1.0000$ | $H=10.50$, $v_{s1}=200.0$, RMS 2.533% |

Four statements follow directly from this table, and they are the practical
content of the lesson.

1. **The answer is a set, not a point.** With a true $H = 10.0\ \mathrm{m}$ and
   $v_{s1} = 200\ \mathrm{m\,s^{-1}}$, the acceptable set spans $2\ \mathrm{m}$ of
   thickness in the short-spread case — $20\%$ — at a noise level of $3\%$.
2. **The set is a ridge, not a blob.** The correlation between the accepted $H$ and
   $v_{s1}$ is $+0.70$ to $+1.00$: thicker and faster versus thinner and slower,
   exactly as the Jacobian of Section 4 predicted.
3. **Widening the band narrows the ridge.** Adding the low frequencies shrinks the
   $H$ half-width from $1.00\ \mathrm{m}$ to $0.25\ \mathrm{m}$, because the low
   frequencies are where the mode feels the whole layer and the high frequencies
   are where it feels $v_{s1}$.
4. **A better fit is not a better model.** The best-fitting model in the widest
   band has $H = 10.5\ \mathrm{m}$ — a $5\%$ error in the parameter the study
   wanted — and it is *inside* the acceptable set. Quoting that value alone, with
   no ridge, is the error the demonstration is designed to expose.

## 7. Resolution: what the spread length limits

Two empirical rules decide what an active survey can record: reliable dispersion is
available up to a wavelength comparable to the source–receiver offset, and the
mode averages the structure over roughly $\lambda/3$. Applying both consistently
(they are rules of thumb, not physics) gives:

| offset (m) | $\lambda_{\max}$ (m) | $f_{\min}$ (Hz) | $z_{\max} = \lambda/3$ (m) |
|---|---|---|---|
| 5 | 10.0 | 20.6663 | 3.33 |
| 10 | 20.0 | 11.1782 | 6.67 |
| 20 | 40.0 | 6.9428 | 13.33 |
| 50 | 100.0 | 4.9516 | 33.33 |

A short spread misses the low frequencies; the low frequencies are the long
wavelengths; and the long wavelengths are the only ones that feel the half-space.
A short spread therefore constrains a thin, fast layer and a thick, slow one
equally well — which is the same statement as the anticorrelation of Section 4,
expressed in metres of geophone cable instead of in a singular value.

## 8. Assumptions and regime of validity

1. **Horizontally layered, laterally homogeneous media.** A dipping interface, a
   lateral velocity change, or a buried channel violates the 1-D assumption
   directly. A 1-D inversion of a 2-D site returns the average, and the average may
   not exist at any point on the line.
2. **Small strain, linear elasticity.** Surface-wave methods measure the
   small-strain modulus; the strain level relevant to a design question is a
   different number (Lesson 06 quantifies the gap).
3. **The fundamental mode is identified correctly.** A picked higher mode inverted
   as the fundamental produces a plausible and wrong profile, and mode
   misidentification is the single most common failure in practice.
4. **The source–receiver offset is long enough for a plane-wave assumption**, and
   short enough that the near-field is negligible. Both failure modes look like
   dispersion.
5. **Density is assumed, not measured.** The dispersion relation depends on
   $\mu = \rho v_s^{2}$, so an error in $\rho$ is traded into $v_s$: a $10\%$
   density error biases $v_s$ by about $5\%$ in the same direction.
6. **The 1-D profile is a statement about the average beneath the array**, over a
   lateral footprint of roughly one wavelength — so the deepest part of the profile
   is also the most laterally smeared.
7. **Anisotropy is ignored.** A vertically transversely isotropic soil (a
   common result of layering at a scale below the wavelength) is inverted as an
   isotropic profile whose velocities are some average of $v_{sv}$ and $v_{sh}$.

## Mastery checkpoint

Use the demonstration's SYNTHETIC model
($v_{s1} = 200\ \mathrm{m\,s^{-1}}$, $\rho_1 = 1800\ \mathrm{kg\,m^{-3}}$,
$H = 10\ \mathrm{m}$ over $v_{s2} = 800\ \mathrm{m\,s^{-1}}$,
$\rho_2 = 2000\ \mathrm{kg\,m^{-3}}$, $\mu_2/\mu_1 = 17.778$).

**(a)** State the interval within which the phase velocity of the fundamental mode
must lie, and the two frequencies at which the demonstration comes within
$0.0012\%$ of the two bounds.
**(b)** At $f = 20\ \mathrm{Hz}$ the measured phase velocity is
$206.43\ \mathrm{m\,s^{-1}}$. Compute $\lambda$, the $\lambda/3$ depth and $c/2f$.
**(c)** Explain in three sentences why the Jacobian's $H$ column and $v_{s1}$ column
are $93.6\%$ anticorrelated, and what measurement a practitioner would add to break
the trade.
**(d)** From the ridge table, quote the accepted $H$ and $v_{s1}$ ranges for the
short spread, and state what fraction of the true thickness that half-width
represents.
**(e)** A 10 m spread is used. What is the deepest depth the $\lambda/3$ rule
attributes to the recorded band, and why does extending the *source-to-first-
receiver* offset help?

A worked version is in the
[solutions](exercises/04-masw-sasw-solutions.md).

## Common pitfalls

1. **Reporting one $V_S$ profile with no acceptable range.** Section 6's ridge is
   $2\ \mathrm{m}$ of thickness wide at $3\%$ noise; a single profile hides that.
2. **Quoting a depth with no depth convention.** $\lambda/3 = 7.65\ \mathrm{m}$ and
   $c/2f = 11.47\ \mathrm{m}$ describe the same frequency of the same curve.
3. **Reading a minimum-misfit model as the answer.** The best fit in the broadest
   band was $H = 10.5\ \mathrm{m}$ for a $10.0\ \mathrm{m}$ truth, and it was
   acceptable — which is the point.
4. **Assuming the fundamental mode was picked.** Higher-mode misidentification
   produces a smooth, plausible, wrong profile with a good misfit.
5. **Expecting the method to see below the longest wavelength recorded.** It cannot;
   the half-space velocity is constrained only if the band reaches far enough
   asymptotically, which the sensitivity row at $2\ \mathrm{Hz}$ ($0.974$) shows.
6. **Transferring a $V_{S30}$ from this method to a design number without stating
   strain.** The measurement is small-strain; the operative modulus at strong
   shaking is not (Lesson 06).
7. **Ignoring the lateral footprint.** The profile is an average over roughly one
   wavelength horizontally, so the deepest layers in it are smeared over tens of
   metres laterally.

## Related modules

- [06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity](../01-elastic-wave-propagation/03-surface-waves.md) —
  the dispersion mechanism and mode shapes in general.
- [05 Site Characterisation: Vs30 and Site Response](05-seismic-hazards-site.md) —
  what is done with the $V_S$ profile once it exists, and why $V_{S30}$ is not the
  profile.
- [06 Engineering Seismology Applications](06-engineering-seismics.md) —
  the downhole and refraction measurements that constrain the same profile from
  other directions.
- [10-05-02 Surface-Wave Methods for Shallow Layers](../../10-gpr-near-surface/05-other-near-surface-methods/02-seismic-surface-wave-nearsurface.md) —
  the field practice of the method derived here.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general treatment
  of ridge-shaped acceptable sets and regularisation.

## Code and exercises

The demonstration is
[`code/masw_dispersion_demo.py`](code/masw_dispersion_demo.py):

```bash
cd 06-seismology/10-refraction-and-near-surface-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python masw_dispersion_demo.py
```

It solves the Love-wave dispersion relation for one layer over a half-space (the
closed-form case), prints every number quoted above with units, and exits 0.
Rayleigh waves, which is what an MASW survey actually records, have the same
qualitative behaviour — a fundamental mode bounded by the two body-wave
velocities, sensitivity that peaks near $\lambda/3$, and a thickness–velocity
trade — but no equally short closed form, so the numerical check in this lesson is
performed on Love waves and stated as such.

Exercises:
[`exercises/04-masw-sasw-exercises.md`](exercises/04-masw-sasw-exercises.md);
solutions:
[`exercises/04-masw-sasw-solutions.md`](exercises/04-masw-sasw-solutions.md).
Module overview: [`README.md`](README.md).
