---
id: 06-01-07
title: "Scattering, Coda and Random Media"
level: doctoral
prereqs: ["06-01-04", "06-01-06", "06-05-02"]
tags: [seismology, scattering, coda, random-media, born-approximation, heterogeneity]
---

# Scattering, Coda and Random Media

A wave in the real Earth never meets a single clean interface. It meets a
medium whose elastic properties vary from metre to kilometre scales, and every
one of those variations scatters a little energy in directions the ray picture
never mentions. The result is visible on every seismogram ever recorded: after
the direct arrival there is a **coda**, a decaying tail that no reflection
coefficient at a named interface can produce.

This lesson treats scattering quantitatively, and insists on one thing above
all: the single-scattering (Born) approximation is a *measured* regime, not a
default. The demonstration solves the same one-dimensional random medium
**exactly**, by an impedance recursion that keeps every multiple, and then
compares. Everything said below about where Born works and where it fails is a
number printed by that comparison.

The honest difficulty at the centre of the lesson is this: the quantity a
seismologist wants — the statistical description of the heterogeneity — is
never the quantity that is measured. What is measured is a reflectivity, a
frequency band, and a coda envelope. The map from those to a random-medium
parameter is many-to-one, and it depends on an approximation whose validity
must itself be measured.

All models and data in this module are **SYNTHETIC**. The medium below is a
chosen random stack, not a measured rock column, and every number quoted is
printed by `code/scattering_demo.py` or is an exact constant with units.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the exact impedance recursion for normal incidence by summing the
   multiple-reflection series, and **state** the sign convention it requires.
2. **Derive** the Born single-scattering sum as the first-order term of that
   recursion, and **identify** precisely which physical effect it discards.
3. **Derive** the three limiting values of the mean backscattered power — one
   interface, a fully coherent stack, and a randomly phased stack — and
   **compute** them for a stated perturbation strength.
4. **Measure** the exponent of backscattered power in perturbation strength and
   in frequency, and **explain** why the often-quoted $\omega^2$ law fails in a
   medium where the phase wrapped across the volume exceeds one cycle.
5. **Quantify** the frequency at which the exact solution departs from Born, and
   **interpret** the deficit as energy that has been scattered more than once.
6. **State** the assumptions under which a measured reflectivity can be inverted
   for a heterogeneity spectrum, and **explain** why that inversion is
   non-unique.

## Prerequisites

- [06-01-04 Reflected, Refracted and Converted Body Waves](04-body-wave-arrivals.md) —
  reflection coefficients, impedance contrast and the energy-flux balance.
- [06-01-06 Interface Waves, Head Waves and the Total Wavefield](06-interface-waves.md) —
  the total field as a sum of contributions, of which scattering is the
  continuous part.
- [06-05-02 Scattering versus Intrinsic Attenuation](../05-attenuation-and-anelasticity/02-scattering-vs-intrinsic.md) —
  how scattering removes energy from a coherent arrival and where the removed
  energy goes.

## 1. Intuition: a spike becomes a tail

Put a pulse into a homogeneous medium and it comes back as a pulse. Put the same
pulse into a stack of thin layers with slightly varying impedance and the
returned signal has a leading reflection with **extra energy after it**. The
extra energy is not noise and it is not attenuation in the anelastic sense;
nothing was absorbed. It is energy that was scattered twice, three times, many
times, and eventually wandered back to the receiver with a longer path and a
different phase.

Two measurements are therefore available on the same record:

- the **leading** arrival, which is dominated by single scattering and is
  the object of the Born approximation;
- the **coda**, which is built from multiple scattering and which carries
  little of the single-scatterer geometry.

The two disagree in a particular, measurable way at large perturbation, and the
size of the disagreement is the honest measure of how wrong a
single-scattering formula is for that medium. That is the experiment this lesson
performs.

## 2. Precise definitions

**Acoustic impedance.** For a normally incident wave, the relevant combination
of properties is

$$Z = \rho\,v \qquad (\mathrm{kg\,m^{-2}\,s^{-1}}).$$

The unit is a mass per unit area per unit time. For the demonstration's
SYNTHETIC background $v = 3000\ \mathrm{m\,s^{-1}}$,
$\rho = 2500\ \mathrm{kg\,m^{-3}}$, $Z_0 = 7.5\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}}$.

**Impedance perturbation.** The medium is generated as $v_j = v_0(1+\sigma\xi_j)$
and $\rho_j = \rho_0(1+\sigma\eta_j)$ with $\xi,\eta$ independent standard
normal deviates, so that

$$\frac{\delta Z_j}{Z_0} \approx \sigma(\xi_j + \eta_j),
\qquad
\operatorname{Var}\!\left(\frac{\delta Z}{Z_0}\right) = \sigma_Z^2 = 2\sigma^2 .$$

The factor of 2 is not decoration: it is the statement that both the velocity and
the density fluctuate. Writing $\sigma_Z^2 = \sigma^2$ is a common slip that
understates the scattering power by a factor of two.

**Single-interface reflection coefficient.** For a jump between $Z_j$ and
$Z_{j+1}$,

$$r_j = \frac{Z_j - Z_{j+1}}{Z_j + Z_{j+1}},$$

with the sign convention that a *decrease* in impedance gives $r > 0$ when the
reflected potential is measured with the same sign as the incident potential
(see [04 Body-Wave Arrivals](04-body-wave-arrivals.md) for the convention trap).

**Born approximation.** Replace the full response by the sum of contributions
from interfaces that each scatter **once**, ignoring all multiples.

**Coherent / incoherent limits.** If the phase accumulated across the stack is
much less than one, all scatterers add with the same phase (coherent). If the
phases are effectively random, the contributions add in power (incoherent).

**Coda.** The part of the record after the direct/leading arrival, generated by
multiple scattering.

**Scattering attenuation** $Q_{\text{scat}}^{-1}$. The apparent attenuation of
the *coherent* arrival caused by energy diverted into the coda. It is a
measurement on the coherent arrival, not a property of a single grain.

## 3. Derivation: the exact response of a stack, by summing multiples

Consider a stack of $N$ layers of thickness $h$ between two half spaces. Let
$R_{j+1}$ be the reflection coefficient of everything below interface $j$,
referred to that interface, and let

$$\theta_j = e^{\,2\mathrm{i}\omega h/v_j}$$

be the two-way phase across layer $j$. Sum the multiple-reflection series at
interface $j$: the leading term is $r_j$; a wave that transmits down and up
contributes $t_jt_j'\theta_j^2 R_{j+1}$; each further round trip multiplies by
$-r_j\theta_j^2 R_{j+1}$, because the reflection coefficient seen from *below*
an interface is $-r_j$. The geometric series gives

$$R_j = r_j + \frac{(1-r_j^2)\,\theta_j^{2} R_{j+1}}
{1 + r_j\,\theta_j^{2} R_{j+1}}
= \frac{r_j + \theta_j^{2} R_{j+1}}{1 + r_j\,\theta_j^{2} R_{j+1}},$$

where the second form uses $r^2 + tt' = 1$. With $R_{N+1} = 0$ this recursion
computes the exact reflection coefficient of the whole stack, **including every
multiple**. That is the algorithm the demonstration uses as the reference truth.

### 3.1 Two checks that fix the normalisation

| Configuration | Exact result | Demo |
|---|---|---|
| Uniform stack over a half space of the *same* impedance | $R = 0$ | $\lvert R\rvert = 0.000\times10^{0}$ |
| Uniform stack of impedance $Z_0$ over a half space $2Z_0$ | $(2Z_0-Z_0)/(2Z_0+Z_0) = 1/3$ | $+0.3333333333$ |

The second check is the important one. It says the recursion reproduces the
single-interface coefficient where the answers must coincide, so its
normalisation is fixed before it is used on a random medium. A recursion that
gets multiple scattering right but the single-interface limit wrong would be
useless, and the error would be invisible in the random-medium comparison.

## 4. Derivation: the Born approximation as the first-order term

Expand $R_j$ of §3 to first order in the $r$'s:

$$R_j \approx r_j + \theta_j^{2}R_{j+1}
\;\Longrightarrow\;
R \approx \sum_{j=1}^{N} r_j
\exp\!\left(2\mathrm{i}\omega\tau_j\right),
\qquad
\tau_j = \sum_{k<j}\frac{h}{v_k},$$

with $\tau_j$ the one-way travel time from the surface down to interface $j$.
Every term contains exactly one $r_j$, hence the name **single scattering**: the
interface scatters once and the wave never returns to it. The sum is a Fourier
transform of the interface-reflectivity sequence, evaluated at the two-way phase
$2\omega\tau_j$ — which is why reflectivity data are so naturally read as spectra.

Two structural consequences are worth naming:

1. **Linearity.** $R_{\text{Born}}$ is linear in the perturbation, so a
   Born inversion for a reflectivity sequence is a *linear* inverse problem,
   and every linear-inverse difficulty (null space, band limitation,
   regularisation) applies. See
   [18-inverse-problems](../../18-inverse-problems/README.md).
2. **No multiples.** Everything a multiply scattered wave does is absent by
   construction. This is the approximation whose validity §7 measures.

### 4.1 Independent check of the implementation

The demonstration evaluates the same integral two ways — as a sum over interfaces
and as a mid-point quadrature of the Born volume integral — for
$\sigma = 0.01$ at $f = 20\ \mathrm{Hz}$:

| Route | Result |
|---|---|
| Interface sum | $R = -0.0207917170 + 0.0104540751\,\mathrm{i}$ |
| Born integral (quadrature) | $R = -0.0207713185 + 0.0104338844\,\mathrm{i}$ |
| $\lvert\text{difference}\rvert/\lvert R\rvert$ | $1.233\times10^{-3}$ |

Agreement at the level of the neglected quadrature terms is a check on the
assembly of the sum, not on the physics of single scattering.

## 5. Derivation: the statistics of the Born sum

Write $R_{\text{Born}} = \sum_j r_j e^{\mathrm{i}\varphi_j}$ with
$\varphi_j = 2\omega\tau_j$, and ask for the mean power
$\mathbb{E}\lvert R_{\text{Born}}\rvert^2$. Two moments of the interface
coefficients are needed. With $r_j \approx (\delta Z_j - \delta Z_{j+1})/(2Z_0)$
and white-noise fluctuations,

$$\mathbb{E}[r_j^2] = \frac{\sigma_Z^2}{2},
\qquad
\mathbb{E}[r_jr_{j+1}] = -\frac{\sigma_Z^2}{4},$$

the negative correlation being simply the fact that neighbouring interfaces
share a layer, so a positive impedance excursion lowers one coefficient and
raises the next.

### 5.1 Three exact limits

**One interface.** No summing at all: the mean backscattered power of a single
jump is

$$\mathbb{E}\lvert R\rvert^2 = \frac{\sigma_Z^2}{2}.$$

**Fully coherent stack** ($\varphi_j$ all equal, i.e. the phase wrapped across
the stack is $\ll 1$). The sum telescopes:

$$\sum_j r_j = \frac{\delta Z_1 - \delta Z_{N+1}}{2Z_0}
= \frac{\delta Z_1}{2Z_0}
\;\Longrightarrow\;
\mathbb{E}\left\lvert\sum_j r_j\right\rvert^{2} = \frac{\sigma_Z^2}{4},$$

where the last step uses that the terminating half space is fixed. The coherent
limit is therefore **half** the single-interface value, and it does *not* grow
with the number of layers: a coherent stack is not a bigger reflector than one
interface, it is the same reflector counted once.

**Incoherent stack** (phases effectively random). Only $j = k$ survives the
double sum, giving

$$\mathbb{E}\lvert R_{\text{Born}}\rvert^{2} = N\,\frac{\sigma_Z^2}{2},$$

linear in the number of scatterers.

For the demonstration's medium, $\sigma = 0.01$ so
$\sigma_Z^2 = 2\sigma^2 = 2.0\times10^{-4}$, and with $N = 2000$ one-metre layers:

| Limit | Value |
|---|---|
| single interface, $\sigma_Z^2/2$ | $1.00\times10^{-4}$ |
| fully coherent stack, $\sigma_Z^2/4$ | $5.0\times10^{-5}$ |
| incoherent stack, $N\sigma_Z^2/2$ | $2.00\times10^{-1}$ |

The spread between the extremes is a factor of 4000 for this medium: the same
heterogeneity produces anything from $5\times10^{-5}$ to $2\times10^{-1}$ of
mean reflected power depending only on how the phases add. **A reflectivity
measurement alone therefore does not determine a perturbation strength without a
statement about the phase correlation.**

**A note on the demonstration's labels.** The demo prints $\sigma_Z^2/2$ as its
"coherent limit". That value is the *single-interface* variance of §5.1; the
fully coherent stack value is exactly half of it, $\sigma_Z^2/4 = 5.0\times10^{-5}$,
and the measured $2\ \mathrm{Hz}$ power is $6.124800\times10^{-5}$ — between the
two, because at that frequency the phases are only partially correlated. The
measurement, not the label, is what the next sections use.

## 6. Derivation: why the $\omega^2$ law is not universal

The frequently quoted result $|R|^2 \propto \omega^2$ comes from a *small-phase*
expansion. For a weak, smooth perturbation the reflected field is proportional to
the gradient of the perturbation, hence to $\omega$, hence the power to
$\omega^2$ — but the derivation requires the two-way phase accumulated across
the scattering volume to be much less than one radian.

Test that condition on the demonstration's medium. The two-way phase across
$N h = 2000\ \mathrm{m}$ at frequency $f$ is $2(2\pi f/v)(2000\ \mathrm{m})$, and
the number of wrapped cycles is

$$\frac{2(2\pi f/v)(2000)}{2\pi} = \frac{2 f (2000)}{v}
= \frac{2(2)(2000)}{3000} = 2.67\ \text{cycles at } 2\ \mathrm{Hz}.$$

The small-phase condition is *already violated at the lowest frequency in the
band*. The measured behaviour is therefore not the $\omega^2$ law but the
crossover from the coherent plateau toward the incoherent limit $N\sigma_Z^2/2$:

| $f$ (Hz) | mean $\lvert R_{\text{Born}}\rvert^2$ | mean $\lvert R_{\text{exact}}\rvert^2$ | exact/Born |
|---|---|---|---|
| 2.0 | $6.124800\times10^{-5}$ | $6.125089\times10^{-5}$ | 1.000047 |
| 5.0 | $1.043589\times10^{-4}$ | $1.043658\times10^{-4}$ | 1.000066 |
| 10.0 | $2.133667\times10^{-4}$ | $2.133360\times10^{-4}$ | 0.999856 |
| 20.0 | $6.942457\times10^{-4}$ | $6.933573\times10^{-4}$ | 0.998720 |
| 40.0 | $2.492797\times10^{-3}$ | $2.486260\times10^{-3}$ | 0.997378 |
| 80.0 | $1.077638\times10^{-2}$ | $1.069453\times10^{-2}$ | 0.992405 |
| 160.0 | $4.854743\times10^{-2}$ | $4.638588\times10^{-2}$ | 0.955475 |

The fitted exponent over 2–20 Hz is **1.0356**. It is not 2, and it is not a
constant: taking local slopes of the printed values,

$$\frac{\ln(1.0436/0.6125)}{\ln(5/2)} = 0.58,\qquad
\frac{\ln(2.1337/1.0436)}{\ln 2} = 1.03,\qquad
\frac{\ln(6.9425/2.1337)}{\ln 2} = 1.70,$$

so the local exponent *steepens with frequency*, from 0.58 in the lowest octave
to 1.70 in the 10–20 Hz octave. The amplitude grows faster than
$\omega^{0}$ but nowhere reaches $\omega^{2}$ inside this band, because the
condition that would produce $\omega^{2}$ never holds. This is what "measure the
scattering law instead of quoting it" means in practice.

## 7. Where the perturbation expansion breaks down

### 7.1 In perturbation strength

The demonstration grows $\sigma$ at fixed $f = 20\ \mathrm{Hz}$ and fits the
exponent of the mean exact power in $\sigma$ over the weak range
$0.002$–$0.010$:

| $\sigma$ | mean exact power | mean Born power | exact/Born |
|---|---|---|---|
| 0.002 | $2.133619\times10^{-4}$ | $2.134415\times10^{-4}$ | 0.999627 |
| 0.005 | $1.385018\times10^{-3}$ | $1.388799\times10^{-3}$ | 0.997278 |
| 0.010 | $5.050970\times10^{-3}$ | $5.098202\times10^{-3}$ | 0.990735 |
| 0.020 | $2.262413\times10^{-2}$ | $2.389281\times10^{-2}$ | 0.946901 |
| 0.050 | $1.001426\times10^{-1}$ | $1.280645\times10^{-1}$ | 0.781970 |
| 0.100 | $3.285701\times10^{-1}$ | $4.969541\times10^{-1}$ | 0.661168 |

The fitted exponent over $0.002$–$0.010$ is **1.9754**, which is $2$ to within
the fit's precision and must be: the reflected *amplitude* is first-order in the
perturbation, so the power is second order. Beyond $\sigma \approx 0.02$ the
exact power falls below the Born value, and by $\sigma = 0.10$ it is only 66% of
it.

### 7.2 Where the missing energy goes

The deficit is not attenuation. At $\sigma = 0.10$ and $f = 40\ \mathrm{Hz}$ the
demonstration reports

$$\overline{\lvert R_{\text{exact}}\rvert^{2}} = 2.537994\times10^{-1},
\qquad
\overline{\lvert R_{\text{Born}}\rvert^{2}} = 3.594533\times10^{-1},
\qquad
\frac{\text{exact}}{\text{Born}} = 0.706071 .$$

The reflected power is *below* the single-scattering estimate. Energy that Born
sends back once has, in the real medium, already been scattered again: it has
left the leading arrival and appears later in the coda. A single-scattering
formula can therefore **over-predict** reflected energy in a strongly
heterogeneous medium — precisely the regime in which a practitioner is tempted
to use it, because the signal is large and easy to see.

The practical rule that follows is worth stating plainly: the Born
approximation is safe where $\text{exact}/\text{Born} \approx 1$, and the table
in §7.1 localises that regime for this medium at $\sigma \lesssim 0.02$, i.e.
2% impedance fluctuations.

## 8. Assumptions and regime of validity

1. **One-dimensional medium, normal incidence, no mode conversion.** Every
   interface is horizontal and the wave is a scalar (acoustic) normal-incidence
   field; P-to-S conversion, which a real oblique wave would produce, is absent.
2. **White-noise, uncorrelated fluctuations** in $v$ and $\rho$, with equal
   fractional standard deviation $\sigma$ and no spatial correlation length.
   Real media have correlation lengths, which strongly affect the frequency
   dependence of scattering; the measured exponent 1.0356 is a property of
   *this* spectrum.
3. **Layers thin compared with the wavelength** is *not* assumed for the exact
   solution, which is valid at any $h/\lambda$; it is the Born comparison that
   degrades when the layer is no longer thin.
4. **No intrinsic attenuation.** Every loss of coherent amplitude in this model
   is scattering, so the model cannot separate the two mechanisms; doing so is
   the subject of [06-05-02](../05-attenuation-and-anelasticity/02-scattering-vs-intrinsic.md).
5. **Deterministic numerics, random medium.** The medium is random but the
   solution of any one realisation is exact; the reported powers are averages
   over realisations with the stated number of repetitions, so they carry
   sampling error not shown in the tables.
6. **Impedance is the only contrast.** If velocity and density were perturbed
   with different correlation lengths, or correlated rather than independent,
   $\sigma_Z^2 = 2\sigma^2$ would be replaced by a different expression and every
   limit in §5 would move.

## 9. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| impedance | $Z$ | $\mathrm{kg\,m^{-2}\,s^{-1}}$ | $\rho v$ |
| impedance perturbation | $\sigma_Z^2$ | – | variance of a dimensionless ratio |
| interface coefficient | $r_j$ | – | ratio of impedances |
| two-way phase | $2\omega\tau_j$ | rad | $\mathrm{s^{-1}}\times\mathrm{s}$ |
| reflection power | $\lvert R\rvert^2$ | – | energy-flux ratio |

The reflectivity is dimensionless and equals an energy-flux ratio only after the
impedance factor is included in the balance; in a uniform stack
($Z_1 = Z_2$) the two coincide, which is why the recursion in §3 is written in
impedance rather than velocity.

## 10. Worked examples

### 10.1 One interface: amplitude, power, and the exact answer

$Z_1 = 7.5\times10^{6}$, $Z_2 = 9.0\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}}$:

$$r = \frac{7.5-9.0}{7.5+9.0} = -0.0909,\qquad r^2 = 8.26\times10^{-3}.$$

Consistency: a 10% impedance increase gives $|r| \approx 0.0476$ and
$r^2 \approx 2.3\times10^{-3}$ — the coefficient is linear in the contrast to
first order, $r \approx \Delta Z/2Z$, so a 10% contrast is only $1/20$ of it in
amplitude.

### 10.2 The three limits for the demonstration's medium

With $\sigma = 0.01$: $\sigma_Z^2 = 2(0.01)^2 = 2.0\times10^{-4}$.

- single interface: $\sigma_Z^2/2 = 1.00\times10^{-4}$;
- coherent stack: $\sigma_Z^2/4 = 5.0\times10^{-5}$;
- incoherent stack: $N\sigma_Z^2/2 = 2000(1.00\times10^{-4}) = 0.200$.

The measured $2\ \mathrm{Hz}$ value $6.1248\times10^{-5}$ sits a factor 1.22 above
the coherent value and a factor $3.3\times10^{3}$ below the incoherent value — so
the low-frequency end of the band is a *partially* coherent regime, which is
exactly why its exponent is 0.58 and not 0 or 2.

### 10.3 Reading the fitted exponents as measurements

Three exponents come out of the demonstration, each with a stated fit range:
1.9754 for power in $\sigma$ over $0.002$–$0.010$ (theory: exactly 2);
1.0356 for power in $f$ over 2–20 Hz (theory: 2 only under a condition that
fails here); and the local frequency slopes 0.58, 1.03, 1.70 of §6. The first is
a validation; the other two are data. Reporting them as "the scattering law is
$\omega^2$" would be a claim the measurement contradicts.

## 11. Python demonstration

[`code/scattering_demo.py`](./code/scattering_demo.py) runs the whole
comparison, and is print-only, seeded with `np.random.default_rng(20261014)`,
and exits 0:

1. checks the exact recursion on two configurations where the answer is known;
2. sweeps the perturbation $\sigma$ and fits the exponent of exact power in
   $\sigma$, with the Born values alongside;
3. evaluates the Born interface sum and the Born integral independently and
   compares them;
4. measures the frequency dependence and the coherent/incoherent limits;
5. measures the multiple-scattering deficit, which is where the "missing"
   energy goes.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    06-seismology/01-elastic-wave-propagation/code/scattering_demo.py
```

## 12. Exercises

Full sets with worked solutions are in
[`exercises/07-scattering-and-heterogeneity-exercises.md`](./exercises/07-scattering-and-heterogeneity-exercises.md)
and
[`exercises/07-scattering-and-heterogeneity-solutions.md`](./exercises/07-scattering-and-heterogeneity-solutions.md),
covering the recursion derivation, a hand calculation of the three limits, an
exponent measurement from printed values, and a research-level question on
inverting reflectivity for a correlation length.

## Mastery checkpoint

Without notes:

**(a)** Derive the recursion
$R_j = (r_j + \theta_j^2R_{j+1})/(1 + r_j\theta_j^2R_{j+1})$ and state where the
sign of the reflection *from below* enters.
**(b)** Expand it to first order and write the Born sum with its phase.
**(c)** For $\sigma = 0.02$ and $N = 2000$, compute $\sigma_Z^2$, the single-interface
power, the coherent-stack power and the incoherent-stack power, with units.
**(d)** Compute the number of cycles wrapped across a 2 km stack at 2 Hz for
$v = 3000\ \mathrm{m\,s^{-1}}$, and say what that number does to the $\omega^2$ law.
**(e)** The demonstration measures exact/Born $= 0.661168$ at $\sigma = 0.10$.
State in one sentence where the missing energy is, and how a measurement could
confirm it.

A worked version of (a)–(d) is in
[`exercises/07-scattering-and-heterogeneity-solutions.md`](./exercises/07-scattering-and-heterogeneity-solutions.md).

## Common pitfalls

1. **Forgetting the factor of two in $\sigma_Z^2 = 2\sigma^2$.** Both $v$ and
   $\rho$ fluctuate; dropping one halves the predicted power.
2. **Quoting $|R|^2 \propto \omega^2$ as a law.** It is a small-phase
   result; the demonstration fails its precondition by 2.67 cycles at the lowest
   frequency in its band.
3. **Treating the coherent limit as growing with stack thickness.** It
   telescopes to one interface's worth; the incoherent limit is the one that
   grows, linearly in $N$.
4. **Calling the exact/Born deficit "attenuation".** Nothing is absorbed; the
   energy is in the coda, and a coda measurement is what would confirm it.
5. **Reporting a single-scattering inversion as a heterogeneity spectrum.**
   The power depends on the phase correlation as much as on the perturbation
   (§5), so the inversion needs more than a reflectivity.

## Self-assessment checklist

- [ ] I can derive the exact impedance recursion and check it on two known limits.
- [ ] I can derive the Born sum as the first-order term and name the discarded physics.
- [ ] I can compute the single-interface, coherent and incoherent powers for stated inputs.
- [ ] I can compute the wrapped phase across a stack and decide whether the small-phase law applies.
- [ ] I can read a fitted exponent as a measurement with a fit range, not as a constant.
- [ ] I can explain where multiply scattered energy appears and how to look for it.
- [ ] I can state why reflectivity alone cannot determine $\sigma$ without a phase-correlation assumption.

## Related modules

- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  separating scattering from intrinsic absorption, which this model deliberately
  does not do.
- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  the coda used as a signal rather than discarded as noise.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the
  deterministic version of the same heterogeneity, inverted for a smooth model.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the
  same reflection coefficients, band-limited and used for imaging.
- [18-inverse-problems](../../18-inverse-problems/README.md) — why a linear
  reflectivity inversion still has a null space.
