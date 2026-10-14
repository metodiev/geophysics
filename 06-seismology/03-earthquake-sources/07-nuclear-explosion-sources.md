---
id: 06-03-07
title: "Discriminating Explosions from Earthquakes"
level: graduate
prereqs: ["06-03-02", "06-03-03"]
tags: [seismology, explosion-sources, discrimination, first-motion, spectral-discriminant]
---

# Discriminating Explosions from Earthquakes

> **All models and data in this module are SYNTHETIC.** Every mechanism, band
> amplitude and probability below is produced by
> [`code/nuclear_explosion_demo.py`](code/nuclear_explosion_demo.py) from chosen
> teaching models. **No nuclear test, yield, catalogue or calibration constant is
> quoted or invented**: the magnitude scales in the demo are explicit SYNTHETIC
> stand-ins, labelled as such, and only *differences* between model populations
> are interpreted. Station counts and probabilities are statements about the
> models, not about any real network.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** why an isotropic source radiates compression in every direction and
   therefore cannot produce a dilatational first motion.
2. **Show** that a double couple radiates compression over exactly half the focal
   sphere, and **compute** the probability $2^{-N}$ that $N$ independent stations
   all read compression under that hypothesis.
3. **Explain** the short-period/long-period discriminant from the source spectrum:
   at the same moment a smaller source has a higher corner frequency and
   comparatively more short-period energy.
4. **Interpret** band-amplitude differences as a *relative* size measure, and
   **state** why the long-period band alone is insensitive to source dimension.
5. **Quantify** the non-uniqueness of a two-band discriminant: which
   combination of $(M_0,\Delta\sigma)$ fits, and how large that set is.
6. **State** why a declared probability from first motions is an upper bound on a
   real discriminant's power.
7. **List** the model assumptions a buried-explosion source model requires, and
   **identify** which of them are measurable.

## Prerequisites

- [06-03-02 The Double-Couple Source and Radiation Patterns](02-double-couple.md) —
  the four-lobe shear pattern and its polarities.
- [06-03-03 Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) —
  the isotropic part $M_{\text{iso}}$ and its volume meaning.

## 1. Intuition: shear and volume change radiate differently

There are only two ways a small region of rock can radiate elastically: it can
**change shape at constant volume** (a shear source) or it can **change volume**
(an isotropic source). A fault slip is the first; a buried explosion is the
second. Everything in this lesson follows from how differently the two radiate.

- An **isotropic** source pushes outward in every direction, so every ray leaves
  compressional: the far-field P amplitude has the *same sign* everywhere and has
  **no nodal planes at all**.
- A **double couple** has two nodal planes and four lobes, compressional in two
  of them. Half of all ray directions are compressional and half dilatational.

That single difference gives the classic first-motion discriminant: an explosion
cannot produce a dilatational first motion *anywhere*, whereas a double couple
produces one at about half of a well-distributed set of stations.

The second discriminant is spectral and less obvious: at the **same seismic
moment**, an explosion's effective source is **smaller** than an earthquake's, so
its corner frequency is higher and its energy is shifted towards short periods.
Two band amplitudes — one short-period, one long-period — therefore separate the
populations even when the moments match.

The honest difficulties are also two. First, a first-motion probability assumes
independent stations, which real networks are not. Second, two band amplitudes are
two numbers, and the source model has at least two parameters, so the two do not
*identify* a source — they can only say which family it is closer to. Both
difficulties are quantified below.

## 2. Precise definitions

| Symbol | Meaning | Unit |
|---|---|---|
| $M_{\text{iso}}$ | isotropic moment $\tfrac13\mathrm{tr}(M)$ | $\mathrm{N\,m}$ |
| $M_0$ | scalar moment from the plateau | $\mathrm{N\,m}$ |
| $a$ | effective source radius | m |
| $f_c$ | corner frequency | Hz |
| $\Delta\sigma_{\text{eff}}$ | effective stress drop (a **modelling choice** for an explosion) | Pa |
| $m_{\text{short}}$, $m_{\text{long}}$ | synthetic band magnitudes (stand-ins) | — |
| $N$ | number of stations with readable first motions | — |

An explosion is modelled by a purely isotropic moment tensor

$$M = M_{\text{iso}}\,I, \qquad M_{\text{iso}}>0,$$

and an earthquake by a double couple with $\mathrm{tr}(M)=0$
([02](02-double-couple.md), [03](03-moment-tensors.md)).

**A warning about $\Delta\sigma_{\text{eff}}$.** A buried explosion has no fault
plane, so "stress drop" does not apply in its usual sense. The demo uses
$\Delta\sigma_{\text{eff}}$ as a *proxy for the ratio of pressure to source
dimension*, and it is a **chosen parameter**, printed and labelled. The demo's two
families use $\Delta\sigma = 3.0\ \mathrm{MPa}$ (earthquake) and
$\Delta\sigma_{\text{eff}} = 300\ \mathrm{MPa}$ (explosion), i.e. a factor $100$,
chosen to make the explosion a smaller source at the same moment. The size of the
resulting separation is a property of that ratio, not a universal constant.

## 3. Derivations

### 3.1 Why an isotropic source radiates compression everywhere

The far-field P amplitude factor comes from the quadrupole projection of the
moment tensor onto the ray direction,
$A(\hat r)\propto\hat r^{\mathsf T}M\hat r$. For $M = M_{\text{iso}}I$,

$$\hat r^{\mathsf T}M\hat r = M_{\text{iso}}\,\hat r^{\mathsf T}\hat r
= M_{\text{iso}}\,\lVert\hat r\rVert^{2} = M_{\text{iso}} > 0,$$

a constant, independent of direction. Hence:

- $A$ has **no nodal surface**: every ray is compressional;
- the amplitude is the *same* in every direction (an isotropic, not just
  sign-uniform, pattern), which is why an explosion has no focal mechanism in the
  usual sense — a focal sphere would be painted entirely in one colour.

*Numerical check.* The demo samples $5000$ random ray directions and measures the
compression fraction for the isotropic source: **1.0000**. Every direction is
compressional, and no sampling scatter appears, because the quantity is exactly
constant.

### 3.2 The double couple covers half the sphere

For $M = M_0(\hat n\hat s^{\mathsf T}+\hat s\hat n^{\mathsf T})$ the amplitude is
$A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s) =
\tfrac12[(\hat r\cdot\hat P)^{2}-(\hat r\cdot\hat T)^{2}]$, which is positive
precisely in the two antipodal cones bisected by $\hat P$ — exactly half the
sphere ([02](02-double-couple.md), Section 3.5).

*Numerical check.* The demo's measured fractions are $0.5008$ (strike-slip),
$0.4946$ (thrust $45^\circ$), $0.5054$ (normal $45^\circ$) and $0.4940$
(oblique), against an expected $0.5000$. The scatter of about $\pm0.006$ is the
sampling error of $5000$ random directions
($1/(2\sqrt{5000}) = 0.0071$).

### 3.3 The first-motion probability

If a double couple radiates compression at a randomly placed station with
probability $1/2$, and $N$ stations are **independent**, then

$$\boxed{\;p(\text{all }N\text{ compressional}\mid\text{double couple})
= \left(\tfrac12\right)^{N} = 2^{-N}.\;}$$

The demo tabulates it:

| $N$ | 1 | 2 | 4 | 6 | 8 | 10 | 15 | 20 |
|---|---|---|---|---|---|---|---|---|
| $2^{-N}$ | $5.000\times10^{-1}$ | $2.500\times10^{-1}$ | $6.250\times10^{-2}$ | $1.562\times10^{-2}$ | $3.906\times10^{-3}$ | $9.766\times10^{-4}$ | $3.052\times10^{-5}$ | $9.537\times10^{-7}$ |
| $-\log_{10}p$ | 0.30 | 0.60 | 1.20 | 1.81 | 2.41 | 3.01 | 4.52 | 6.02 |

Eight stations all reading compression already give $p = 3.9\times10^{-3}$ against
a double couple. To reach $p<10^{-3}$:

$$2^{-N}<10^{-3}
\;\Longrightarrow\;
N>\frac{\log_{10}10^{3}}{\log_{10}2} = \frac{3}{0.30103} = 9.97
\;\Longrightarrow\; N\ge10.$$

**This is a statement about the source, and it is an upper bound on the
discriminant's practical power** (Section 4.3).

### 3.4 The short-period / long-period discriminant

Both families are given the same spectral model,
$\Omega(f) = \Omega_0/(1+(f/f_c)^{2})$ with $\Omega_0\propto M_0$ and
$f_c = k\beta/a$; they differ only in the effective stress drop, hence in $a$ at a
given $M_0$. From $M_0 = \tfrac{16}{7}\Delta\sigma a^{3}$:

$$a\propto\Delta\sigma^{-1/3}, \qquad f_c\propto\Delta\sigma^{1/3},$$

so a factor $100$ in effective stress drop gives a factor

$$\frac{f_c^{\text{exp}}}{f_c^{\text{eq}}}
= 100^{1/3} = 4.642$$

at the same moment. The demo confirms it: at $M_0 = 10^{18}\ \mathrm{N\,m}$ the
earthquake has $a = 5263.6\ \mathrm{m}$, $f_c = 0.2460\ \mathrm{Hz}$, while the
explosion has $a = 1134.0\ \mathrm{m}$, $f_c = 1.1420\ \mathrm{Hz}$, ratio
$1.1420/0.2460 = 4.642$.

The two bands are chosen as

$$\text{short: } 0.5\text{–}2.0\ \mathrm{Hz}, \qquad
\text{long: } 0.02\text{–}0.1\ \mathrm{Hz},$$

and the mechanism is then a statement about *where the corner sits in the short
band*:

- The **long band is below $f_c$ for both families** throughout the table, so both
  families' long-band amplitudes are close to the plateau and are essentially
  **proportional to $M_0$ alone**. The demo shows it directly: $m_{\text{long}}$
  rises by almost exactly $1.000$ per decade of moment ($13.397$, $14.397$,
  $15.396$, $16.391$, $17.369$), and at each moment the two families agree to
  within $0.03$ units ($15.396$ vs $15.397$; $16.391$ vs $16.397$; $17.369$ vs
  $17.396$) even though their radii differ by a factor of $4.6$. The small
  deviations from a perfect decade step grow at the top of the range because the
  earthquake's corner frequency ($0.246\ \mathrm{Hz}$ at $M_0 = 10^{18}\ \mathrm{N\,m}$)
  is approaching the top of the long band ($0.1\ \mathrm{Hz}$).
- The **short band is above the earthquake's corner** for most of the table, so
  the earthquake's short-band amplitude falls below its plateau, while the
  explosion's corner is high enough to keep more energy in the band.

So the discriminant is the **difference** between the two band magnitudes. The
demo's full table:

| family | $M_0$ (N m) | $a$ (m) | $f_c$ (Hz) | $m_{\text{short}}$ | $m_{\text{long}}$ | difference |
|---|---|---|---|---|---|---|
| earthquake | $10^{14}$ | 244.3 | 5.3005 | 14.672 | 13.397 | 1.275 |
| earthquake | $10^{15}$ | 526.4 | 2.4603 | 15.596 | 14.397 | 1.199 |
| earthquake | $10^{16}$ | 1134.0 | 1.1420 | 16.386 | 15.396 | 0.990 |
| earthquake | $10^{17}$ | 2443.2 | 0.5301 | 16.991 | 16.391 | 0.600 |
| earthquake | $10^{18}$ | 5263.6 | 0.2460 | 17.438 | 17.369 | 0.068 |
| explosion | $10^{14}$ | 52.6 | 24.6028 | 14.697 | 13.397 | 1.300 |
| explosion | $10^{15}$ | 113.4 | 11.4196 | 15.692 | 14.397 | 1.295 |
| explosion | $10^{16}$ | 244.3 | 5.3005 | 16.672 | 15.397 | 1.275 |
| explosion | $10^{17}$ | 526.4 | 2.4603 | 17.596 | 16.397 | 1.199 |
| explosion | $10^{18}$ | 1134.0 | 1.1420 | 18.386 | 17.396 | 0.990 |

For the earthquake family the difference falls by

$$1.275 - 0.068 = 1.207$$

over the four decades of moment: as the earthquake grows, its corner frequency
falls *below* the short band, so the short-period amplitude collapses onto the
$f^{-2}$ tail while the long-period amplitude keeps tracking $M_0$. For the
explosion family the corner frequency stays at or above the short band across the
whole tabulated range (from $24.6\ \mathrm{Hz}$ at $10^{14}$ down to
$1.14\ \mathrm{Hz}$ at $10^{18}$), so its short-period amplitude stays near the
plateau and the difference remains large — $1.300$ down to $0.990$.

### 3.5 Comparing the families at matched long-period amplitude

Because $m_{\text{long}}$ depends only on $M_0$ in this model, matching the
long-period amplitude is the same as matching the moment. The demo's matched pairs
are therefore the same-moment rows (its printed "long-period amplitude" column
shows the row index $1$–$3$, i.e. $M_0 = 10^{15}$, $10^{16}$ and
$10^{17}\ \mathrm{N\,m}$):

| $M_0$ (N m) | $m_{\text{short}}$ earthquake | $m_{\text{short}}$ explosion | offset |
|---|---|---|---|
| $10^{15}$ | 15.596 | 15.692 | 0.096 |
| $10^{16}$ | 16.386 | 16.672 | 0.286 |
| $10^{17}$ | 16.991 | 17.596 | 0.605 |

At matched long-period amplitude the short-period amplitude is larger for the
explosion by roughly $0.29$ to $0.61$ in the demo's synthetic magnitude units.
(For the $M_0 = 10^{15}$ row the offset is only $0.096$; the demo's quoted range
of $0.29$–$0.61$ comes from the $10^{16}$ and $10^{17}$ rows.) **That offset is
the discriminant**, and its size is a property of the assumed stress-drop ratio
of $100$, not a universal constant.

### 3.6 How much does a two-band discriminant identify?

Take one explosion from the table, record its two band amplitudes, and ask which
**double-couple** models reproduce both to within $10\%$. The demo grids
$121$ moments ($10^{13}$–$10^{19}\ \mathrm{N\,m}$) by $121$ stress drops
($10^{6}$–$10^{9}\ \mathrm{Pa}$) and finds

$$\text{acceptable fraction} = \frac{51}{14641} = 0.0035,$$

with the moment spanning $10^{16.00}$ to $10^{16.00}\ \mathrm{N\,m}$ ($0.00$
decades — one grid step) and the stress drop spanning $10^{7.75}$ to
$10^{9.00}\ \mathrm{Pa}$ ($1.25$ decades).

**Reading.** The acceptable set is a nearly one-dimensional **curve** in a
two-dimensional parameter plane: the low-frequency level pins the moment, and the
short-period level then determines only a *band* of stress drops. So two band
amplitudes identify **how big** a source is far better than **how small** it is —
the right way round for a size or yield estimate, and the wrong way round for a
source-dimension estimate.

## 4. Physical interpretation

### 4.1 The first-motion discriminant is a *sufficiency* test

A single clearly dilatational first motion **refutes** a pure isotropic source,
because an explosion has no dilatational direction at all. The test is therefore
asymmetric: one dilatational reading is decisive against an explosion, whereas
$N$ compressional readings only accumulate evidence *for* one. This asymmetry,
not the $2^{-N}$ number, is what makes first motions valuable.

### 4.2 The spectral discriminant is a *relative* size measure

The long-period band measures $M_0$; the short-period band measures how much of
the spectrum sits above or below the corner. The explosion's higher corner means
its short-period content is larger *at the same moment*. Stated as an inference:
"for this long-period size, the source is too rich in short periods for a
shear source" is a comparison, and it is family-based rather than event-identifying.

### 4.3 Why $2^{-N}$ is an upper bound

The binomial calculation assumes (i) **independence** of the stations and (ii)
that each reads compression with probability exactly $1/2$. Both fail in practice:

1. A wrong velocity model, a mis-set instrument polarity or a station block on
   one side of the source can make many stations agree, which is *correlated*
   error: the effective $N$ is smaller than the count.
2. Stations near a nodal plane have $A\approx0$ and unreadable first motions;
   they are dropped, which both reduces $N$ and biases the surviving sample away
   from the nodal planes — inflating the apparent agreement.

So the number $2^{-N}$ is a property of the source model, and the honest statement
is: "the source-level probability is $2^{-N}$; the network-level false-positive
rate is larger and must be calibrated empirically."

### 4.4 The discriminant is one of several

Depth (explosions are shallow and detonated in rock, so they lack the depth
distribution of natural seismicity), the ratio of surface-reflected phases, and
the presence of an associated cavity or collapse signature are independent
discriminants. This lesson computes only the two that follow from the source
spectrum and the radiation pattern. **A real discrimination argument combines
independent observables, because each alone is defeatable.**

## 5. Assumptions and regime of validity

1. **Point source, far field.** Both families are modelled as points; finite
   source effects add directionality.
2. **Purely isotropic explosion.** Real explosions impart some deviatoric moment
   through the emplacement geometry and the surrounding structure, so a small
   $\varepsilon$ is expected; the discriminant degrades in proportion.
3. **One $k$ for both families.** The corner-frequency relation
   $f_c = k\beta/a$ is applied with the same $k$; if the effective slip-pulse
   shape differs, the comparison is contaminated.
4. **$\Delta\sigma_{\text{eff}}$ is chosen.** The whole separation scale depends on
   the assumed ratio; it is not a measurement.
5. **The magnitude scales are stand-ins.** The demo's $m_{\text{short}}$ and
   $m_{\text{long}}$ use an explicitly synthetic calibration; only *differences*
   between the families are interpreted.
6. **No attenuation or site difference between the families.** A real comparison
   must equalise path and site effects, or the spectral difference may be
   propagation rather than source.
7. **Independent stations with reliable polarities.** See Section 4.3.

**Non-uniqueness.** A discriminant that reports one number per band cannot
identify a source. It can assign a family with a stated error rate, which is a
different (and more defensible) claim.

## 6. Units and dimensional analysis

| Quantity | Expression | Unit |
|---|---|---|
| $M_{\text{iso}}$ | $\tfrac13\mathrm{tr}(M)$ | $\mathrm{N\,m}$ |
| $\hat r^{\mathsf T}M\hat r$ | $M_{\text{iso}}$ | $\mathrm{N\,m}$ |
| $a$ | $((7/16)M_0/\Delta\sigma)^{1/3}$ | $\mathrm{m}$ |
| $f_c$ | $k\beta/a$ | $\mathrm{s^{-1}}$ |
| band amplitude | average of $\Omega(f)$ over a band | $\mathrm{m\,s}$ (or $\mathrm{m\,Hz}$) |
| $m$ | $\log_{10}(\text{amplitude}/\text{period})+\log_{10}(d/100\,\mathrm{km})$ | — |

The synthetic magnitude's argument is dimensionless because an amplitude is
divided by a period and a distance ratio is taken; that is why a *period* must be
stated for every magnitude (the same point as the offset convention in
[03](03-moment-tensors.md)).

## 7. Worked examples

### Example 1 — how many stations?

$$2^{-N} < 10^{-3} \;\Longrightarrow\; N > \frac{3}{0.30103} = 9.97
\;\Longrightarrow\; N = 10,$$

at which the demo prints $9.766\times10^{-4}$. At $N = 8$ the probability is
$3.906\times10^{-3}$, an order of magnitude larger.

### Example 2 — the corner-frequency ratio

$$\frac{f_c^{\text{exp}}}{f_c^{\text{eq}}}
= \left(\frac{\Delta\sigma_{\text{eff}}^{\text{exp}}}
{\Delta\sigma^{\text{eq}}}\right)^{1/3}
= 100^{1/3} = 4.6416,$$

because $f_c\propto a^{-1}$ and $a\propto\Delta\sigma^{-1/3}$. The demo's
$M_0 = 10^{18}\ \mathrm{N\,m}$ row gives $1.1420/0.2460 = 4.642$ ✔.

### Example 3 — the long-period band is blind to source dimension

At $M_0 = 10^{16}\ \mathrm{N\,m}$ the demo prints
$m_{\text{long}} = 15.396$ for the earthquake and $15.397$ for the explosion,
while the source radii differ by a factor $1134.0/244.3 = 4.64$ and the corner
frequencies by the same factor. **Below the corner, the spectrum is the plateau
and the plateau knows only $M_0$.** That is why the long-period amplitude is used
as the moment ruler and the short-period one as the discriminant.

### Example 4 — the offset at matched long-period amplitude

At $M_0 = 10^{17}\ \mathrm{N\,m}$:

$$m_{\text{short}}^{\text{exp}} - m_{\text{short}}^{\text{eq}}
= 17.596 - 16.991 = 0.605$$

in the synthetic magnitude units. In terms of an amplitude ratio this is a factor
$10^{0.605} = 4.03$ — the explosion radiates about four times more short-period
amplitude than an earthquake of the same long-period size in this model.

### Example 5 — the size of the acceptable set

$$51/14641 = 0.00348 \approx 0.0035.$$

Since the moment is pinned to one grid step ($0.00$ decades) while the stress drop
spans $1.25$ decades, the acceptable set has an aspect ratio of roughly
$1.25/0.05 = 25$ grid steps along the stress-drop direction to one along the
moment direction. **The discriminant is sharp in size and blunt in
source-dimension.**

## 8. Python demonstration

[`code/nuclear_explosion_demo.py`](code/nuclear_explosion_demo.py):

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nuclear_explosion_demo.py
```

Three numbered parts:

1. **First-motion polarity.** The isotropic source's compression fraction
   $1.0000$; the four double-couple measurements $0.5008$, $0.4946$, $0.5054$,
   $0.4940$ against $0.5000$; and the $2^{-N}$ table.
2. **Band-limited amplitudes.** The two families' radii, corner frequencies and
   two band magnitudes, the falling difference for the earthquake
   ($1.275\to0.068$), and the matched-moment comparison showing the
   $0.096$–$0.605$ offsets.
3. **Non-uniqueness.** The $121\times121$ grid, the $51/14641$ acceptable
   fraction, and the asymmetric extents ($0.00$ decades in moment, $1.25$ in
   stress drop).

The demo states plainly that its magnitude calibrations are SYNTHETIC stand-ins
and that only differences between populations are interpreted. That discipline is
the point: the *shape* of the separation is a model result, while any absolute
magnitude would be a convention that cannot be invented.

## 9. Exercises

- [`exercises/07-nuclear-explosion-sources-exercises.md`](exercises/07-nuclear-explosion-sources-exercises.md)
- [`exercises/07-nuclear-explosion-sources-solutions.md`](exercises/07-nuclear-explosion-sources-solutions.md)

## 10. Real-world applications

- **Seismic monitoring and verification.** First-motion and spectral
  discriminants are the classical source-level evidence in monitoring
  underground explosions; they are one component of a multi-observable case.
- **Third source classes.** Mine collapses and cavity collapses are implosive
  ($M_{\text{iso}}<0$) and are separated from both earthquakes and explosions by
  the *sign* of the isotropic part.
- **Volcanic and induced sources.** Long-period volcanic events and fluid-driven
  induced events carry non-double-couple components, and the same machinery
  quantifies *how much*.
- **Calibration of discriminants.** Because $2^{-N}$ is an upper bound, real
  monitoring calibrates false-positive rates empirically on known populations.
- **Magnitude-scale design.** The choice of band and period in a magnitude scale
  determines what a network measures, which is why saturation
  ([05](05-source-spectra.md), Section 3.7) matters for discrimination.

## 11. Further reading

- **Aki, K., & Richards, P. G. (1980). *Quantitative Seismology*.** Level:
  graduate textbook. The radiation of isotropic and shear sources, and the moment
  tensor decomposition the discriminant rests on.
- **Kanamori, H., & Anderson, D. L. (1975). Theoretical basis of some empirical
  relations in seismology.** *Bulletin of the Seismological Society of America*.
  Level: research. The scaling relations that set the corner-frequency ratio used
  here.
- **Brune, J. N. (1970). Tectonic stress and the spectra of seismic shear waves
  from earthquakes.** *Journal of Geophysical Research*. Level: research. The
  spectral model with which both families are compared.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. The discrimination literature is
> large and is deliberately not summarised here, because its calibrations are
> observatory-specific and cannot be reproduced from a synthetic model.

## Mastery checkpoint

Complete this without notes.

> You are given two SYNTHETIC sources with the same long-period amplitude,
> $M_0 = 10^{16}\ \mathrm{N\,m}$. Source A has $\Delta\sigma = 3.0\ \mathrm{MPa}$;
> source B has $\Delta\sigma_{\text{eff}} = 300\ \mathrm{MPa}$. Take
> $\beta = 3500\ \mathrm{m\,s^{-1}}$, $k = 0.37$. **(a)** Compute $a$ and $f_c$
> for both. **(b)** State which band — $0.02$–$0.1\ \mathrm{Hz}$ or
> $0.5$–$2.0\ \mathrm{Hz}$ — is affected by the difference and why.
> **(c)** A network of $N$ stations records compression at every one of them.
> State the source-level probability for a double couple and give the smallest $N$
> for which it is below $10^{-4}$. **(d)** State two reasons the true
> false-positive rate is higher. **(e)** One station reads a clear dilatational
> first motion. State what this refutes and what it does not.
> **(f)** A colleague reports a yield from the short-period amplitude. State two
> model quantities the estimate implicitly assumes, and why the non-uniqueness
> grid makes a source-*dimension* estimate harder than a size estimate.

## Common pitfalls

1. **Treating $2^{-N}$ as the network's error rate.** It is a source-level
   probability under an independence assumption that fails.
2. **Reading a magnitude stand-in as a real magnitude.** The demo's calibrations
   are synthetic; only differences carry meaning.
3. **Assuming the explosion model's "stress drop" is physical.** It is a proxy for
   pressure over source dimension, and a chosen parameter.
4. **Comparing bands without equalising path and site.** A spectral difference can
   be propagation, not source.
5. **Believing two band amplitudes identify a source.** The acceptable set is a
   $1.25$-decade-long curve.
6. **Ignoring the sign of $M_{\text{iso}}$.** Implosive collapse is the third
   class and is separated by sign, not by magnitude.
7. **Forgetting that one dilatational reading is decisive against a pure
   explosion, while many compressional readings are only cumulative evidence.**
   The discriminant is asymmetric.

## Related modules

- [02 The Double-Couple Source and Radiation Patterns](02-double-couple.md) —
  the half-sphere compression fraction.
- [03 Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) —
  $M_{\text{iso}}$ and the CLVD as discrepancy flags.
- [05 Source Spectra, Corner Frequency and Stress Drop](05-source-spectra.md) —
  the spectral model and its saturation.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  how band-limited amplitudes become reported magnitudes.
- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/README.md) —
  non-double-couple sources from fluid and tensile processes.
