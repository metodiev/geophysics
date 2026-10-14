---
id: 08-01-06
title: "Palaeomagnetism, Reversals and Magnetostratigraphy"
level: graduate
prereqs: ["08-01-02", "08-01-04", "04-03-03", "21-01-01"]
tags: [geomagnetism, palaeomagnetism, reversals, magnetostratigraphy, fisher-statistics, palaeolatitude]
---

# Palaeomagnetism, Reversals and Magnetostratigraphy

Rock magnetism ([08-01-07](07-rock-magnetism.md)) explains how a rock acquires a
remanence. This lesson is about what that remanence can be made to say: it is the
only direct record of the geomagnetic field older than a few centuries, and every
palaeomagnetic conclusion passes through one of two statistical inferential
chains — a **mean direction** with a confidence cone, or a **polarity pattern**
matched to a reference chronology. Both chains are quantified here, and both
carry assumptions that are stated rather than buried.

**All models and data in this module are SYNTHETIC.** The directions, poles,
polarity sequence and reversal statistics come from a seeded generator and from
chosen teaching parameters. No site, section, core or published polarity
timescale is used. Standard values are $a = 6371\ \mathrm{km}$ and the
$11.5^{\circ}$ dipole tilt.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a Fisher mean direction, its resultant length $R$, its precision
   $\hat k$ and its 95% confidence cone $\alpha_{95}$ from a set of directions.
2. **Quantify** the scatter of $\hat k$ and $\alpha_{95}$ for a given number of
   sites, and explain why $\alpha_{95}$ is the quantity to report.
3. **Convert** inclination to palaeolatitude and propagate the inclination error
   into a palaeolatitude error, including its strong latitude dependence.
4. **Compute** a virtual geomagnetic pole (VGP) from a site position and a
   direction, and state how a declination error maps into a pole error.
5. **Interpret** a synthetic reversal chronology, including the difference
   between a long-term rate and a windowed rate.
6. **State** the assumptions of the geocentric axial dipole hypothesis and which
   conclusions depend on it.
7. **Decide** how many reversals a polarity pattern needs before a correlation
   with a reference chronology is meaningful.

## Prerequisites

- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](02-dipole-and-igrf.md) —
  the dipole relation $\tan I = 2\tan\lambda$ derived there.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](04-secular-variation.md) —
  the timescales that separate palaeosecular variation from reversal behaviour.
- [04-03-03 Radiometric Dating Methods and Their Assumptions](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md)
  — the independent ages that turn a polarity pattern into a chronology.
- [21-01-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md)
  — estimators, bias and confidence statements.

## 1. What is measured, and what is assumed

A palaeomagnetic sample yields a **direction** $(D, I)$ and an **intensity** in
the laboratory frame after demagnetisation. To convert a direction into a
palaeolatitude, palaeomagnetists invoke the **geocentric axial dipole (GAD)**
hypothesis: that the field, averaged over $10^{4}$–$10^{5}$ yr, is that of a
dipole aligned with the rotation axis. Under GAD,

$$\tan I = 2\tan\lambda,$$

with $\lambda$ the palaeolatitude. Everything else in this lesson is either a
statistical treatment of the measured directions or a chronological treatment of
polarity.

The GAD hypothesis is not a theorem. Its support is the near-coincidence of the
time-averaged dipole axis with the rotation axis, and its failures are what
palaeosecular variation studies look for. Two consequences to keep separate:

- **Palaeolatitude** is a single number that inherits every failure of GAD.
- **Tectonic rotation** inferred from declination does *not* depend on GAD, only
  on the field having been dipolar at the site — which is why declination-based
  reconstructions are considered the more robust of the two products.

## 2. Fisher statistics on directions

Directions on a sphere are not vectors in a linear space, so the arithmetic mean
is meaningless. **Fisher (1953)** statistics replace it. Model the $N$ unit
vectors $\hat{\mathbf{v}}_i$ as drawn from

$$p(\theta)\propto e^{\kappa\cos\theta}\sin\theta,$$

a distribution on the sphere with a single concentration parameter $\kappa$.
Then:

- **Mean direction** $\hat{\mathbf{v}}_R = \sum_i \hat{\mathbf{v}}_i / R$ with
  $R = \left|\sum_i\hat{\mathbf{v}}_i\right|$ the **resultant length**;
- **Precision** $\hat k = \dfrac{N-1}{N-R}$;
- **95% confidence cone radius**
  $\alpha_{95} = \arccos\left[1 - \dfrac{N-R}{R}
  \left(\left(\tfrac{1}{0.05}\right)^{1/(N-1)}-1\right)\right]$.

Note carefully that $R$ here is the **length of the vector sum**, not the mean unit
vector: the estimators use $R$ directly. Confusing the two is the commonest
arithmetic error in the subject, and it produces $\alpha_{95}$ values that are
not even defined (the argument of `arccos` leaves $[-1,1]$).

### 2.1 Worked example — one synthetic sample

The demonstration draws $N = 24$ directions from a Fisher distribution with
**true** mean $D = 12.000^{\circ}$, $I = 48.000^{\circ}$ and $\kappa = 30.0$, and
recovers

| quantity | value |
|---|---|
| mean $D$ | $11.8649^{\circ}$ |
| mean $I$ | $48.6342^{\circ}$ |
| $R$ | 23.003665 |
| $\hat k = (N-1)/(N-R)$ | 23.0846 |
| $\alpha_{95}$ | $6.2928^{\circ}$ |

The mean lies within $\alpha_{95}$ of the true mean (the demonstration tests this
and prints `True`). Note that $\hat k = 23.08$ is well below the true
$\kappa = 30$: a single sample of 24 directions is a poor precision estimate.

### 2.2 How noisy is $\hat k$?

Over 400 independent samples of the same size:

| estimator | median | 5–95% range |
|---|---|---|
| $\hat k$ | 30.882 | 22.358 – 43.245 |
| $\alpha_{95}$ | $5.410^{\circ}$ | $4.551^{\circ}$ – $6.399^{\circ}$ |

$\hat k$ has a skewed distribution spanning nearly a factor of two; the median is
close to the true $\kappa$ (slightly high at this $N$, which is the known
behaviour of the estimator), but an individual value is not a reliable statement
about precision. $\alpha_{95}$ states the same information as an interval and is
the number to report. **This is the first non-uniqueness of the lesson: one
sample gives a direction and a cone, not a direction and a precision.**

### 2.3 More sites, how much better?

| $N$ sites | median $\alpha_{95}$ (°) | median $\hat k$ |
|---|---|---|
| 5 | 13.5668 | 32.764 |
| 10 | 8.9458 | 30.122 |
| 24 | 5.5187 | 29.720 |
| 50 | 3.7731 | 29.484 |
| 100 | 2.5951 | 30.648 |
| 400 | 1.3031 | 30.065 |

$\alpha_{95}$ falls from $13.567^{\circ}$ at $N=5$ to $1.303^{\circ}$ at
$N=400$: a factor of 10.41 for an $N$-ratio of 80, against the $1/\sqrt N$
prediction of 8.94. The median $\hat k$ is stable at about 30 for $N\ge10$ —
the precision estimator stops being badly biased, while the confidence cone keeps
shrinking. **Below $N\approx20$ the estimator is itself unreliable**, which is
why palaeomagnetic studies pool sites rather than quoting single-site cones.

## 3. Inclination to palaeolatitude, and the error that comes with it

Invert $\tan I = 2\tan\lambda$:

$$\lambda = \arctan\!\left(\frac{\tan I}{2}\right).$$

| $I$ (°) | palaeolatitude $\lambda$ (°) | shift in $\lambda$ for $I\to I+5^{\circ}$ (°) |
|---|---|---|
| 0 | 0.0000 | 2.5048 |
| 15 | 7.6307 | 2.6834 |
| 30 | 16.1021 | 3.1932 |
| 45 | 26.5651 | 4.2247 |
| 60 | 40.8934 | 6.1035 |
| 75 | 61.8132 | 8.7614 |
| 85 | 80.0750 | 9.9250 |

*Hand check of the $I = 45^{\circ}$ row:* $\tan 45^{\circ} = 1$, so
$\lambda = \arctan(0.5) = 26.5651^{\circ}$ ✔. And for
$I = 50^{\circ}$: $\tan 50^{\circ} = 1.19175$, $\lambda = \arctan(0.595877)
= 30.7896^{\circ}$, a shift of $4.2245^{\circ}$ — the tabulated 4.2247 with
rounding. ✔

The table is the quantitative form of a practical rule: **a fixed inclination
error produces a palaeolatitude error that grows with latitude**, from
$2.5^{\circ}$ at the equator to nearly $10^{\circ}$ at $I = 85^{\circ}$. Two
consequences:

- Equatorial sites give the best-constrained palaeolatitudes, and polar sites the
  worst — the opposite of the intuition that "more vertical field is easier to
  measure".
- Reported palaeolatitudes must come with the inclination uncertainty, not as bare
  numbers. A palaeolatitude quoted to $0.1^{\circ}$ from a direction with
  $\alpha_{95} = 6^{\circ}$ is a false precision: the propagated error is several
  degrees.

Two further, non-statistical errors act on $I$ and are not visible in
$\alpha_{95}$: **inclination shallowing** (compaction of a sediment rotates
grains towards the bedding plane, reducing $|I|$) and **overprinting** (a later
remanence partially replacing the primary one). Neither is a random error, so
neither averages out across sites.

## 4. Virtual geomagnetic poles

A single site's direction defines a **virtual geomagnetic pole** (VGP): the pole
its position would imply, *if* the field were that of a geocentric dipole.
Convert the inclination to a magnetic colatitude
$p = \arctan(2/\tan I)$, then move $p$ degrees from the site along the
declination's great circle:

$$\sin\lambda_p = \sin\lambda_s\cos p + \cos\lambda_s\sin p\cos D,$$
$$\phi_p = \phi_s + \arctan\!\left(\frac{\sin p\sin D}
{\cos\lambda_s\cos p - \sin\lambda_s\sin p\cos D}\right).$$

*Worked example.* Site $\lambda_s = 42.0^{\circ}$, $\phi_s = -18.0^{\circ}$,
$D = 14.5^{\circ}$, $I = 52.0^{\circ}$:

$$p = \arctan\!\left(\frac{2}{\tan 52^{\circ}}\right)
= \arctan(1.562587) = 57.3819^{\circ},$$

$$\sin\lambda_p = \sin 42^{\circ}\cos 57.3819^{\circ}
+ \cos 42^{\circ}\sin 57.3819^{\circ}\cos 14.5^{\circ}
= 0.669131\times0.539170 + 0.743145\times0.842195\times0.968148,$$
$$= 0.360786 + 0.605863 = 0.966649
\quad\Longrightarrow\quad \lambda_p = 75.1692^{\circ},$$

and the same construction with
$\phi_p = \phi_s + \arctan\left[\sin p\sin D / (\cos\lambda_s\cos p
- \sin\lambda_s\sin p\cos D)\right]$ gives
$\phi_p = 106.5225^{\circ}$. The pole is $90.0 - 75.1692 = 14.8308^{\circ}$ from
the geographic pole.

*Sensitivity.* Changing $D$ by $+10^{\circ}$ moves the VGP latitude by
$-6.6931^{\circ}$. The VGP therefore inherits:

- the site's direction error (propagated through a nonlinear map),
- the site's own position error, and
- **the assumption of a geocentric dipole field**, which is the GAD hypothesis
  applied pointwise.

The scatter of VGPs computed from many sites of similar age is the standard
measure of **palaeosecular variation**: it is a measure of what the field was
doing, provided the dipole assumption holds and the ages are correct.

## 5. Reversals and magnetostratigraphy

The field reverses polarity at irregular intervals. A synthetic chronology with
exponentially distributed intervals of mean $0.22\ \mathrm{Myr}$ spanning
$10\ \mathrm{Myr}$ yields

| quantity | value |
|---|---|
| number of reversals | 50 |
| mean interval between them | 0.1963 Myr |
| mean reversal rate | 5.000 per Myr |

and, estimated in 2 Myr windows:

| window (Myr) | reversals | rate (per Myr) |
|---|---|---|
| 0.0–2.0 | 11 | 5.50 |
| 2.0–4.0 | 16 | 8.00 |
| 4.0–6.0 | 7 | 3.50 |
| 6.0–8.0 | 10 | 5.00 |
| 8.0–10.0 | 6 | 3.00 |

Two points follow, and both are about inference rather than about reversals:

1. **A windowed rate is a noisy estimate of a long-term rate.** The windows
   differ by a factor of more than two, purely from exponential spacing. A claim
   that "the reversal rate changed" requires an interval long enough that the
   expected count is large — otherwise the claim is unfalsifiable.
2. **Exponential intervals are consistent with the absence of periodicity.** The
   lag-1 autocorrelation of the interval series is $-0.0087$, i.e. zero. The
   theory of reversals therefore does not require a clock; a random-libration
   process produces the same statistics.

### 5.1 How many reversals make a correlation?

The polarity of each interval is a binary variable. The chance that a random
sequence of $n$ intervals matches a given pattern is $2^{-n}$:

| $n$ | $2^{-n}$ |
|---|---|
| 4 | $6.25\times10^{-2}$ |
| 6 | $1.56\times10^{-2}$ |
| 8 | $3.91\times10^{-3}$ |
| 10 | $9.77\times10^{-4}$ |
| 12 | $2.44\times10^{-4}$ |

A section with three or four reversals can be matched to almost any part of a
reference chronology; one with ten or more is effectively unique. **The rule is
that magnetostratigraphy needs either many reversals or independent dates**, and
in the absence of both, a correlation is a hypothesis with a stated chance of
being a coincidence.

## 6. Assumptions and regime of validity

1. **GAD.** Every palaeolatitude and every VGP uses it. Section 3 shows that the
   mapping is steep at high latitude, so the assumption is most damaging exactly
   where it is hardest to test.
2. **The remanence is primary and stable.** A direction is only a field
   measurement if the magnetisation has not been overprinted or
   partly remagnetised; that is the subject of [08-01-07](07-rock-magnetism.md).
3. **Fisher (or another) distribution applies.** Real directions are often
   elongated or clustered, and $\alpha_{95}$ assumes rotational symmetry.
4. **Site ages.** A VGP scatter is only a palaeosecular-variation measure if the
   sites are the same age; otherwise it mixes secular variation with motion.
5. **Exponential reversal spacing.** The demonstration generates intervals that
   way; the Earth is not required to, and the rate estimates above depend on it.
6. **Synthetic data.** No number in this lesson is a measurement of the Earth.

## 7. Python demonstration

`code/palaeomagnetism_demo.py` prints:

1. Fisher statistics on a synthetic sample plus a 400-realisation Monte Carlo of
   $\hat k$ and $\alpha_{95}$;
2. the inclination-to-palaeolatitude table with the $5^{\circ}$ error propagation;
3. a VGP computation with its declination sensitivity;
4. median $\alpha_{95}$ and $\hat k$ versus the number of sites;
5. a synthetic reversal chronology with windowed rates and the interval
   autocorrelation;
6. the $2^{-n}$ correlation-probability table.

Exercises and solutions:
[`exercises/06-palaeomagnetism-exercises.md`](./exercises/06-palaeomagnetism-exercises.md),
[`exercises/06-palaeomagnetism-solutions.md`](./exercises/06-palaeomagnetism-solutions.md).

## Mastery checkpoint

1. For 20 directions with $R = 18.5$, compute $\hat k$ and $\alpha_{95}$,
   showing that the argument of `arccos` stays in range.
2. Compute the palaeolatitude for $I = 38^{\circ}$ and for $I = 43^{\circ}$, and
   state how much a $5^{\circ}$ inclination error costs there.
3. Compute the magnetic colatitude for $I = 65^{\circ}$.
4. A section has eight polarity intervals. State the probability that a random
   sequence matches it, and what additional information you would require before
   publishing a correlation.
5. A colleague reports "the reversal rate doubled in this window". Give two
   questions that must be answered before the claim can be assessed.

## Common pitfalls

1. **Averaging directions linearly.** $(D_1+D_2)/2$ is not a mean direction; use
   Fisher statistics.
2. **Using the mean unit vector instead of $R$.** The estimators require the
   vector sum's length.
3. **Quoting a palaeolatitude without an inclination uncertainty.**
4. **Treating VGP scatter as pure palaeosecular variation** without checking
   ages and the GAD assumption.
4. **Correlating polarity patterns with fewer than about ten reversals.**
5. **Reading a windowed reversal rate as a long-term rate.** Section 5 gives the
   counterexample.
6. **Forgetting inclination shallowing in sediments.** It is systematic, not
   random.

## Related modules

- [08-01-07 Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy](07-rock-magnetism.md) —
  how the remanence is acquired and whether it can be trusted.
- [08-01-05 The Geodynamo: Mechanism and Evidence](05-dynamo-theory.md) — why
  reversals happen at all.
- [12-04-03 Palaeomagnetic Record and Reversal Frequency](../../12-global-geophysics-interior/04-geomagnetism-and-core/03-palaeomagnetic-record.md) —
  the global record.
- [04-03-03 Radiometric Dating Methods and Their Assumptions](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md) —
  the ages that anchor a polarity pattern.
- [21-01-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  estimators, confidence and bias.

## Self-assessment checklist

- [ ] I can compute a Fisher mean, $\hat k$ and $\alpha_{95}$.
- [ ] I can state why $\alpha_{95}$ is more useful than $\hat k$.
- [ ] I can convert inclination to palaeolatitude and propagate an error.
- [ ] I can compute a VGP and state what makes it uncertain.
- [ ] I can compute a reversal rate and say how reliable the window estimate is.
- [ ] I can state the GAD assumption and which conclusions need it.
