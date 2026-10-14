---
id: 06-03-05
title: "Source Spectra, Corner Frequency and Stress Drop"
level: graduate
prereqs: ["06-03-03", "06-03-04"]
tags: [seismology, source-spectra, corner-frequency, stress-drop, scaling]
---

# Source Spectra, Corner Frequency and Stress Drop

> **All models and data in this module are SYNTHETIC.** Every spectrum, corner
> frequency and stress drop below is produced by
> [`code/source_spectra_demo.py`](code/source_spectra_demo.py) from the chosen
> teaching model ($\beta = 3500\ \mathrm{m\,s^{-1}}$,
> $\mu = 3.0\times10^{10}\ \mathrm{Pa}$, model constant $k = 0.37$). The model
> constant is a **choice**, labelled as such wherever it is printed. No observed
> spectrum or measured stress drop is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the $\omega^{-2}$ source spectrum and **identify** the low- and
   high-frequency asymptotes and the corner frequency by their slopes.
2. **Derive** the far-field amplitude's proportionality to $M_0$ and **explain**
   why the low-frequency plateau measures moment but the corner frequency alone
   does not measure size.
3. **Derive** the stress drop from $(M_0, f_c)$ using the circular-crack relation
   $M_0 = \tfrac{16}{7}\Delta\sigma a^{3}$ and $f_c = k\beta/a$.
4. **Quantify** how a wrong model constant $k$ propagates into the stress drop,
   and **state** why a stress drop quoted without $k$ is not a measurement.
5. **Derive** the self-similar exponent $M_0\propto f_c^{-3}$ and **measure** it
   from a synthetic population.
6. **Explain** spectral saturation: a band above $f_c$ records
   $M_0^{1/3}$, not $M_0$, and **measure** both exponents.
7. **State** which parts of the analysis are measurement and which are model.

## Prerequisites

- [06-03-03 Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) —
  the scalar moment whose value is measured from the low-frequency plateau.
- [06-03-04 Source Time Functions, Rupture Kinematics and Directivity](04-source-time-function.md) —
  the duration that becomes the corner frequency.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the path effect that superposes on the spectrum derived here.

## 1. Intuition: a size meter that is not a size meter

The far-field spectrum of an earthquake has a simple shape. At low frequencies it
is **flat**, and the height of the plateau is proportional to the seismic moment.
Above a **corner frequency** $f_c$ it falls as $f^{-2}$. The corner frequency is
inversely related to the source dimension: a bigger crack has a lower corner.

This gives two numbers, $M_0$ and $f_c$, from one spectrum, and it is tempting to
read them as "how big" and "how small". The lesson's two honest difficulties are
that:

- $f_c$ alone gives **neither** the size nor the moment: it gives the ratio
  $M_0/a^{3}$, which is the stress drop — and only up to a **model constant**.
- The mapping from $f_c$ to a length contains a constant $k=O(1)$ that is chosen,
  not measured. A stress drop quoted without it is a measurement of the Earth
  multiplied by a number the analyst selected.

Everything else in this lesson follows from taking those two statements seriously
and doing the arithmetic.

## 2. Precise definitions

The **Brune $\omega^{-2}$ model** for the far-field *displacement* amplitude
spectrum is

$$\boxed{\;\Omega(f) = \frac{\Omega_0}{1+(f/f_c)^{2}}.\;}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Omega_0$ | low-frequency spectral plateau, $\propto M_0$ | $\mathrm{m\,s}$ or $\mathrm{m\,Hz}$ |
| $f_c$ | corner frequency | Hz |
| $a$ | effective source radius (circular crack) | m |
| $k$ | model constant in $f_c = k\beta/a$ | — |
| $\Delta\sigma$ | static stress drop | Pa |
| $\beta$ | shear-wave speed at the source | $\mathrm{m\,s^{-1}}$ |
| $\mu$ | shear modulus | Pa |

The two asymptotes follow immediately:

$$\Omega(f)\to\Omega_0 \quad (f\ll f_c),\qquad
\Omega(f)\to\Omega_0 f_c^{2}f^{-2} \quad (f\gg f_c).$$

The **velocity** spectrum is $\omega\Omega(f)$, rising as $f$ below $f_c$
(constant displacement) and falling as $f^{-1}$ above it — the classical
"constant-$Q$" appearance of a displacement spectrum multiplied by frequency.

The two model relations used to convert $(M_0,f_c)$ into stress drop are the
**Eshelby circular-crack** relation and the **corner-frequency–radius** relation:

$$M_0 = \frac{16}{7}\,\Delta\sigma\,a^{3}, \qquad f_c = \frac{k\beta}{a}.$$

Both contain model content: the $16/7$ is an exact elastic result for a circular
crack, but $f_c = k\beta/a$ is a parameterisation whose constant depends on the
assumed slip-velocity time function. The demo uses $k = 0.37$ and states that the
literature uses values of order $0.2$–$0.5$, so $k$ is a **model choice**.

## 3. Derivations

### 3.1 Plateaus, asymptotes and slopes

Divide numerator and denominator by $f^{2}$ for $f\gg f_c$:

$$\Omega(f) = \frac{\Omega_0}{1+(f/f_c)^{2}}
\approx \frac{\Omega_0 f_c^{2}}{f^{2}}
= A f^{-2}, \qquad A = \Omega_0 f_c^{2}.$$

So the high-frequency decay exponent is $-2$ and the corner frequency is where
the two asymptotes meet. Taking logarithms of the two asymptote lines
$\log\Omega = \log\Omega_0$ and $\log\Omega = \log(\Omega_0 f_c^{2}) - 2\log f$
and equating them gives $\log f_c$ at the intersection — which is the standard
graphical estimator the demo implements.

*Numerical check (SYNTHETIC).* For $M_0 = 10^{19}\ \mathrm{N\,m}$ and
$\Delta\sigma = 3.0\ \mathrm{MPa}$ the demo reports an input corner frequency of
$0.11420\ \mathrm{Hz}$ and a **measured** corner of $0.11419\ \mathrm{Hz}$
(relative error $0.0000$); for $M_0 = 10^{17}$ the input/measured pair is
$0.53005 / 0.52991\ \mathrm{Hz}$ (relative error $0.0003$). The fitted
high-frequency slope is $-2.0000$, i.e. the model's own $-2.0$: the measurement is
accurate to the fit window, and the residual is the intersection estimator, not
the physics.

### 3.2 The plateau measures moment

In the far field the low-frequency level is
$\Omega_0 = \mathcal{R}\,M_0/(4\pi\rho\beta^{3}r)$, where $\mathcal{R}$ collects
the radiation pattern and free-surface factors, $\rho$ the density and $r$ the
distance. Everything except $M_0$ is either a constant for a given station or a
quantity that can be modelled; so $\Omega_0\propto M_0$, and the exponent of the
low-frequency level with respect to moment is **exactly 1**. The demo measures
$0.999089$ in the band $10^{-4}$–$10^{-3}\ \mathrm{Hz}$ over a six-decade family
— the deviation from 1 is the finite band and the finite source population.

### 3.3 Corner frequency and radius

Eliminate $a$ between the two model relations:

$$f_c = \frac{k\beta}{a}
\;\Longrightarrow\;
\Delta\sigma = \frac{7}{16}M_0\left(\frac{f_c}{k\beta}\right)^{3}.$$

This is the inversion the demo performs. Its structure is the whole story of the
lesson:

- The **cube** is why $f_c$ errors are amplified: an $f_c$ that is $10\%$ too
  high gives a stress drop $33\%$ too high.
- The constant $k$ enters **cubed** as well.

*Numerical check.* With $M_0 = 10^{19}\ \mathrm{N\,m}$, $k = 0.37$,
$\beta = 3500\ \mathrm{m\,s^{-1}}$:

$$a^{3} = \frac{7}{16}\frac{M_0}{\Delta\sigma}
= 0.43750\times\frac{10^{19}}{3.0\times10^{6}} = 1.45833\times10^{12}
\;\Rightarrow\; a = 11340.2\ \mathrm{m},$$
$$f_c = \frac{0.37\times3500}{11340.2} = \frac{1295}{11340.2}
= 0.11420\ \mathrm{Hz},$$

matching the demo's $a = 11340.2\ \mathrm{m}$ and $f_c = 0.11420\ \mathrm{Hz}$.

### 3.4 The sensitivity to the model constant

Inverting with a different $k'$ while the data were built with $k$ multiplies the
inferred stress drop by $(k/k')^{3}$:

$$\frac{\Delta\sigma(k')}{\Delta\sigma(k)} = \left(\frac{k}{k'}\right)^{3}.$$

*Numerical check.* The demo builds with $k = 0.37$ and inverts with:

| $k$ used to invert | $\Delta\sigma$ recovered (MPa) | ratio to true | error factor |
|---|---|---|---|
| 0.20 | 18.9949 | 6.3316 | 6.3316 |
| 0.37 | 3.0000 | 1.0000 | 1.0000 |
| 0.50 | 1.2157 | 0.4052 | 0.4052 |

Check: $(0.37/0.20)^{3} = 1.85^{3} = 6.3316$ ✔ and
$(0.37/0.50)^{3} = 0.74^{3} = 0.405224$ ✔. Both $0.20$ and $0.50$ are plausible
choices within the literature range, and they give stress drops that differ by
$6.33/0.405 = 15.6$ — a factor of fifteen, from the model constant alone.

### 3.5 Self-similar scaling

For a family of circular ruptures with the **same** stress drop, the two model
relations give

$$M_0 = \frac{16}{7}\Delta\sigma a^{3} \;\Rightarrow\; M_0\propto a^{3},
\qquad f_c = \frac{k\beta}{a} \;\Rightarrow\; f_c\propto a^{-1},$$

so eliminating $a$:

$$\boxed{\;M_0\propto f_c^{-3}.\;}$$

The mean **slip** follows from $M_0 = \mu A \bar D$ with $A = \pi a^{2}$:

$$\bar D = \frac{M_0}{\mu\pi a^{2}}
= \frac{(16/7)\Delta\sigma a^{3}}{\mu\pi a^{2}}
= \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}\,a
\;\Rightarrow\; \bar D\propto a.$$

*Numerical check.* The demo reports a fitted exponent
$\mathrm{d}\log_{10}M_0/\mathrm{d}\log_{10}f_c = -3.000000$ over 60 sources, and
the slip table $a = 50,\ 500,\ 5000\ \mathrm{m}\to\bar D = 0.0036,\ 0.0364,\
0.3638\ \mathrm{m}$: ten times the radius, ten times the slip, a thousand times
the moment, a tenth of the corner frequency. Hand check:
$\bar D = (16/7\pi)(3.0\times10^{6}/3.0\times10^{10})\times50
= 0.72758\times10^{-4}\times50 = 3.638\times10^{-3}\ \mathrm{m}$ ✔.

### 3.6 Corner frequency is not a size meter

Fix $M_0$ and vary $\Delta\sigma$. From Section 3.3,
$a\propto\Delta\sigma^{-1/3}$ and $f_c\propto a^{-1}\propto\Delta\sigma^{1/3}$:

| $\Delta\sigma$ (MPa) | 0.30 | 3.00 | 30.0 | 300 |
|---|---|---|---|---|
| $a$ (m) | 24431.6 | 11340.2 | 5263.6 | 2443.2 |
| $f_c$ (Hz) | 0.05301 | 0.11420 | 0.24603 | 0.53005 |

Every row has $M_0 = 10^{19}\ \mathrm{N\,m}$ and the corner frequency varies by a
factor 10. So a measured $f_c$ alone specifies **neither** size nor moment: it
specifies the ratio $M_0/a^{3}$, which is the stress drop (up to $k$). The pair
$(M_0, f_c)$ determines the stress drop; neither number alone determines the
other.

### 3.7 Spectral saturation

Put the source in a fixed measurement band and let it grow at constant stress
drop. With $f_c\propto M_0^{-1/3}$:

- in a band **below** $f_c$, the amplitude is the plateau, so
  amplitude $\propto M_0$ — exponent $1$;
- in a band **above** $f_c$, the amplitude is
  $\Omega_0 f_c^{2}f^{-2}\propto M_0\cdot M_0^{-2/3} = M_0^{1/3}$ — exponent
  $1/3$.

The demo evaluates both bands:

| $M_0$ (N m) | $f_c$ (Hz) | band $10^{-4}$–$10^{-3}$ Hz | band $2$–$10$ Hz |
|---|---|---|---|
| $10^{18}$ | 0.24603 | $9.9744\times10^{17}$ | $3.0021\times10^{15}$ |
| $10^{19}$ | 0.11420 | $9.9742\times10^{18}$ | $6.4994\times10^{15}$ |
| $10^{20}$ | 0.05301 | $9.9731\times10^{19}$ | $1.4017\times10^{16}$ |
| $10^{21}$ | 0.02460 | $9.9684\times10^{20}$ | $3.0206\times10^{16}$ |
| $10^{22}$ | 0.01142 | $9.9464\times10^{21}$ | $6.5080\times10^{16}$ |
| $10^{23}$ | 0.00530 | $9.8464\times10^{22}$ | $1.4021\times10^{17}$ |

Measured exponents: **$0.999089$** below $f_c$ (predicted $1$) and
**$0.333771$** above (predicted $1/3$). Hand check for the second: from
$3.0021\times10^{15}$ to $1.4021\times10^{17}$ is a factor
$46.70$; over 5 decades of moment the exponent is
$\log_{10}(46.70)/5 = 1.6693/5 = 0.3339$, i.e. $\approx1/3$ ✔.

**That is saturation.** A magnitude defined from a band-limited amplitude is a
logarithmic measure of $M_0$ in the low band and of $M_0^{1/3}$ in the high band;
as the source grows, a fixed high-frequency band stops recording the growth. The
same arithmetic applied to the conventional magnitude scales is lesson
[06-04-05 Magnitude Saturation](../04-earthquake-location-and-magnitude/README.md).

## 4. Physical interpretation

**Where the spectrum comes from.** A circular crack that slips with a short
slip-velocity pulse radiates a pulse whose spectrum is flat to a corner set by
the pulse's duration and falls beyond it. The $f^{-2}$ shape is a model output,
not a physical law; real spectra carry the source shape, attenuation and
scattering, and the measured high-frequency slope is a *joint* property of all
three. The demo's $-2.0000$ is the model's own slope, printed to show that the
estimator is unbiased on model data — not as evidence about the Earth.

**Why the plateau measures moment.** The low-frequency limit is the static
displacement of the source; by the representation theorem it is proportional to
$M_0$. This is the only *absolute* measurement the spectrum provides, and it is
the input to every moment scale.

**Why the corner measures stress drop, not size.** The corner is set by the ratio
of wave speed to source dimension *and* by the shape of the slip pulse. Two
cracks with the same radius but different slip pulses have different $f_c$; two
cracks with the same $f_c$ can differ in radius by a factor of two through $k$.
The parameter that survives is $M_0/a^{3}$ — stress drop.

**Self-similarity is an assumption with a physical reading.** "Constant stress
drop across all sizes" is an empirical regularity (noted already in
[01](01-faulting-and-slip.md)) which makes $M_0\propto a^{3}$ and gives the
$M_0$–$f_c$ law one exponent. Where it fails — for the largest events, whose
width saturates (lesson [06](06-rupture-dynamics.md)) — the law bends.

**Non-uniqueness.** $(M_0, f_c)$ gives three unknowns
$(\Delta\sigma, a, k)$ with $k$ assumed. Without an independent length or an
independent stress drop, the pair is underdetermined, and the standard practice
of fixing $k$ is a **convention that must be reported**.

## 5. Assumptions and regime of validity

1. **Circular crack, uniform stress drop.** Real ruptures are irregular;
   $\Delta\sigma$ is an average and $a$ is an equivalent radius.
2. **$\omega^{-2}$ spectrum.** The high-frequency slope is *assumed*; measuring
   it and asserting it are different operations.
3. **Point source in the far field.** Finite-source and directivity effects
   multiply the corner by an azimuthal factor (lesson [04](04-source-time-function.md)).
4. **$f_c = k\beta/a$ with $k$ chosen.** Its value depends on the slip pulse; the
   demo's $0.37$ is one choice among those of order $0.2$–$0.5$.
5. **The spectrum is the source spectrum.** Attenuation, scattering, site
   response and instrument must be removed first; if they are not, their
   corner-like features are misattributed to the source.
6. **Band covers $f_c$.** If the recording band lies entirely above or entirely
   below $f_c$, the corner is not measured at all and saturation applies.
7. **$M_0$ from the plateau is the *only* absolute scale.** Everything else is
   relative.

**Consequence.** A stress drop quoted without stating $k$, the assumed spectral
model and the $M_0$ method is not comparable with another worker's value. That is
why the demo prints $k$ at the top and labels it.

## 6. Units and dimensional analysis

| Quantity | Expression | Unit | Check |
|---|---|---|---|
| $\Omega$ | $\Omega_0/(1+(f/f_c)^2)$ | $\mathrm{m\,s}$ | denominator dimensionless ✔ |
| $A = \Omega_0f_c^{2}$ | $\mathrm{m\,s}\times\mathrm{Hz}^{2} = \mathrm{m\,s^{3}}$ | so $Af^{-2}$ is $\mathrm{m\,s}$ ✔ |
| $f_c$ | $k\beta/a$ | $\mathrm{m\,s^{-1}}/\mathrm{m} = \mathrm{s^{-1}}$ | Hz ✔ |
| $M_0$ | $\tfrac{16}{7}\Delta\sigma a^{3}$ | $\mathrm{Pa\,m^{3}} = \mathrm{N\,m^{-2}\,m^{3}} = \mathrm{N\,m}$ | ✔ |
| $\Delta\sigma$ | $\tfrac{7}{16}M_0(f_c/(k\beta))^{3}$ | $\mathrm{N\,m}\times\mathrm{s^{-3}}/(\mathrm{m^3s^{-3}}) = \mathrm{N\,m^{-2}}$ | Pa ✔ |
| slip | $\bar D = \tfrac{16}{7\pi}(\Delta\sigma/\mu)a$ | Pa/Pa × m = m | ✔ |

The dimensionless groups here are $k$ and $16/7$; both are model inputs, and a
dimensional check cannot validate them.

## 7. Worked examples

### Example 1 — from $(M_0,\Delta\sigma)$ to $a$ and $f_c$

$M_0 = 10^{19}\ \mathrm{N\,m}$, $\Delta\sigma = 3.0\times10^{6}\ \mathrm{Pa}$,
$k = 0.37$, $\beta = 3500\ \mathrm{m\,s^{-1}}$.

$$a^{3} = \frac{7}{16}\frac{M_0}{\Delta\sigma}
= \frac{0.43750\times10^{19}}{3.0\times10^{6}} = 1.45833\times10^{12}
\;\Rightarrow\; a = 11340.2\ \mathrm{m},$$
$$f_c = \frac{0.37\times3500}{11340.2} = 0.11420\ \mathrm{Hz}.$$

Both match the demo's first table.

### Example 2 — the stress drop, inverted

Take the same numbers and pretend only $(M_0, f_c)$ were measured:

$$\Delta\sigma = \frac{7}{16}M_0\left(\frac{f_c}{k\beta}\right)^{3}
= 0.43750\times10^{19}\left(\frac{0.11420}{1295}\right)^{3}.$$

$\frac{0.11420}{1295} = 8.8185\times10^{-5}$; cubed $= 6.8579\times10^{-13}$;
product $= 0.43750\times10^{19}\times6.8579\times10^{-13} = 3.0003\times10^{6}\
\mathrm{Pa} \approx 3.00\ \mathrm{MPa}$ ✔ (the small residual is the rounding of
$f_c$).

### Example 3 — how wrong can the stress drop be?

A worker assumes $k = 0.50$ on data built with $k = 0.37$:

$$\Delta\sigma_{\text{inferred}} = 3.0\times\left(\frac{0.37}{0.50}\right)^{3}
= 3.0\times0.40522 = 1.216\ \mathrm{MPa},$$

matching the demo's $1.2157\ \mathrm{MPa}$ (ratio $0.4052$). A second worker
assumes $k = 0.20$ and gets $3.0\times1.85^{3} = 18.99\ \mathrm{MPa}$. The two
results differ by a factor $15.6$ — **both published conventions**.

### Example 4 — $M_0$–$f_c$ exponent from two points

From the demo's saturation family, $M_0 = 10^{18}$ has
$f_c = 0.24603\ \mathrm{Hz}$ and $M_0 = 10^{23}$ has $f_c = 0.00530\ \mathrm{Hz}$:

$$p = \frac{\log_{10}(10^{23}/10^{18})}{\log_{10}(0.00530/0.24603)}
= \frac{5.000}{\log_{10}(0.021542)} = \frac{5.000}{-1.6667} = -3.000.$$

So two points on a self-similar family already give $p = -3$; the demo fits all
60 sources and reports $-3.000000$.

### Example 5 — saturation exponent from two points

Band $2$–$10\ \mathrm{Hz}$: at $M_0 = 10^{18}$ the amplitude is
$3.0021\times10^{15}$; at $M_0 = 10^{23}$ it is $1.4021\times10^{17}$. The ratio is
$46.70$, so

$$p = \frac{\log_{10}46.70}{5.000} = \frac{1.6693}{5.000} = 0.3339 \approx 1/3.$$

## 8. Python demonstration

[`code/source_spectra_demo.py`](code/source_spectra_demo.py):

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python source_spectra_demo.py
```

Five numbered parts:

1. **Measuring the corner frequency** by intersecting the low- and
   high-frequency asymptotes, against the value used to build each spectrum
   (relative errors $0.0000$–$0.0003$), with the fitted slope $-2.0000$.
2. **Recovering the stress drop**, and the $k$-sensitivity table of Section 3.4
   (factors $6.3316$, $1.0000$, $0.4052$ for $k = 0.20$, $0.37$, $0.50$).
3. **$M_0$ versus $f_c$** at constant stress drop: fitted exponent
   $-3.000000$, plus the slip table showing $\bar D\propto a$.
4. **Fixed $M_0$, varying stress drop**: the corner frequency moves by a factor
   10 while the moment is constant.
5. **Saturation**: the two-band table and the measured exponents $0.999089$ and
   $0.333771$.

The demo prints $k$ at the top and labels it a model choice; that label is the
most important line in the file.

## 9. Exercises

- [`exercises/05-source-spectra-exercises.md`](exercises/05-source-spectra-exercises.md)
- [`exercises/05-source-spectra-solutions.md`](exercises/05-source-spectra-solutions.md)

## 10. Real-world applications

- **Moment and magnitude.** The low-frequency plateau is the standard route to
  $M_0$ and hence to $M_{\mathrm w}$.
- **Stress-drop surveys.** Comparing $f_c$ across a region is a standard proxy for
  relative stress drop — with the caveat that only *relative* values are robust
  when $k$ is fixed.
- **Magnitude saturation.** The $M_0^{1/3}$ behaviour above $f_c$ is why
  short-period magnitudes saturate for large events.
- **Source scaling and physics.** The $M_0$–$f_c$ relation is the primary test of
  self-similarity and of deviations from it.
- **Ground-motion prediction.** $f_c$ sets the high-frequency content of simulated
  seismograms, which controls the response of short-period structures.

## 11. Further reading

- **Brune, J. N. (1970). Tectonic stress and the spectra of seismic shear waves
  from earthquakes.** *Journal of Geophysical Research*. Level: research. The
  $\omega^{-2}$ model and the corner-frequency relation.
- **Eshelby, J. D. (1957). The determination of the elastic field of an
  ellipsoidal inclusion.** *Proceedings of the Royal Society A*. Level: research.
  The $16/7$ circular-crack relation.
- **Kanamori, H., & Anderson, D. L. (1975). Theoretical basis of some empirical
  relations in seismology.** *Bulletin of the Seismological Society of America*.
  Level: research. The scaling relations that make $M_0\propto f_c^{-3}$.
- **Aki, K., & Richards, P. G. (1980). *Quantitative Seismology*.** Level:
  graduate textbook. Spectra of dislocation sources, including the asymptotes
  used here.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC spectrum has a plateau $\Omega_0$ proportional to
> $M_0 = 4.0\times10^{18}\ \mathrm{N\,m}$ and a measured corner frequency
> $f_c = 0.15\ \mathrm{Hz}$. Take $\beta = 3500\ \mathrm{m\,s^{-1}}$,
> $\mu = 3.0\times10^{10}\ \mathrm{Pa}$ and $k = 0.37$. **(a)** Compute the source
> radius $a$. **(b)** Compute the stress drop. **(c)** Compute the mean slip.
> **(d)** State which of the quantities in (a)–(c) changes, and by what factor, if
> the analyst had used $k = 0.20$ instead. **(e)** State two ways the corner
> frequency could be mis-measured and what each would do to the stress drop.
> **(f)** Explain in two sentences why a fixed high-frequency band stops tracking
> moment as the source grows.

## Common pitfalls

1. **Quoting a stress drop without $k$.** $k$ enters cubed; the conventions span
   a factor of about $15$ in the answer.
2. **Treating $f_c$ as a size measurement.** At fixed $M_0$, $f_c$ varies by a
   factor 10 with stress drop.
3. **Assuming the observed high-frequency slope is the source slope.** Attenuation
   and scattering steepen it.
4. **Forgetting the $\omega^{-2}$ assumption.** It is a model, not a measurement.
5. **Reading a band-limited amplitude as a moment.** Above $f_c$ it measures
   $M_0^{1/3}$.
6. **Comparing stress drops across studies without comparing the $M_0$ method.**
   A plateau measured in a narrow band is not an $M_0$.
7. **Treating an equivalent radius as the fault's dimension.** It is a
   stress-drop-equivalent radius, and for non-circular ruptures it is a
   definition, not a length.

## Related modules

- [03 Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) —
  where $M_0$ is defined and into which the plateau is converted.
- [04 Source Time Functions, Rupture Kinematics and Directivity](04-source-time-function.md) —
  the azimuthal spread of the corner frequency.
- [06 Rupture Dynamics, Fracture Energy and Scaling Laws](06-rupture-dynamics.md) —
  where self-similarity breaks.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  saturation in the conventional magnitude scales.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the path effect that must be removed before any of this.
