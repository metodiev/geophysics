---
id: 06-05-02
title: "Separating Scattering from Intrinsic Attenuation"
level: doctoral
prereqs: ["06-05-01", "06-01-07", "06-02-02"]
tags: [seismology, attenuation, scattering, apparent-q, random-media, coda]
---

# Separating Scattering from Intrinsic Attenuation

Wave energy leaves a coherent arrival by two physically different routes.
**Intrinsic** attenuation converts organised motion into heat: the energy is
gone from the wavefield and the medium is genuinely anelastic. **Scattering**
redistributes the energy within the wavefield: it removes amplitude from the
direct arrival and deposits it in the coda, and a perfectly elastic random
medium does exactly this. Both produce a direct arrival whose amplitude decays
approximately exponentially with distance, and a single amplitude-versus-distance
measurement cannot tell which one it is looking at.

This is the central honesty point of the module. A measured $Q$ from a direct
arrival is an **apparent** $Q$, and the only physically defensible claims that can
be made from it alone are the inequality $Q_{\text{app}} \le Q_{\text{int}}$ and a
statement about the frequency band. Turning an apparent $Q$ into a temperature, a
fluid content or a melt fraction requires an independent measurement that breaks
the ambiguity, and this lesson is about which measurements do that, how much they
are worth, and where the additivity rule that makes the whole discussion
quantitative stops working.

All models and data in this module are **SYNTHETIC**. The random media below are
chosen teaching models, not imaged structures, and no observational $Q$ is
quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** intrinsic from scattering attenuation in terms of where the
   energy goes, and **state** why a coherent-amplitude measurement sees both.
2. **Derive** the additivity rule $1/Q_{\text{app}} = 1/Q_{\text{int}} +
   1/Q_{\text{scat}}$ from the addition of independent loss coefficients, and
   **bound** the error it carries.
3. **Classify** a scattering regime by the product $ka$ of wavenumber and
   correlation length, and **compute** the crossover frequency from a stated
   correlation length.
4. **Measure** the apparent $Q$ of a purely elastic random stack from the exact
   transmission coefficient, and interpret the result as a scattering artefact
   rather than as absorption.
5. **Demonstrate** that a single-band amplitude measurement is non-unique, by
   constructing two physically different media that fit it.
6. **Design and interpret** a two-band frequency test that discriminates the two
   mechanisms, including its false-positive and false-negative modes.
7. **Quantify** the ensemble size needed before a measured scattering $Q$ is
   meaningful, and explain why a single realisation is not an estimate.

## Prerequisites

- [01 Measuring Q: Spectral Ratio, Rise Time, Multiple Methods](01-attenuation-measurement.md) —
  the definitions of $Q$, $\alpha$ and $t^{*}$, and the estimator errors.
- [06-01-07 Scattering, Coda and Random Media](../01-elastic-wave-propagation/07-scattering-and-heterogeneity.md) —
  the scattering vocabulary: coherent field, coda, correlation length.
- [06-02-02 Snell's Law and Layered Media](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  ray theory, which is the limit scattering invalidates.

## 1. Two mechanisms, one signature

Write the coherent (ensemble-averaged) direct-wave amplitude as
$A(x) = A_0\exp(-\alpha_{\text{app}} x)$ and define the apparent quality factor by
the same relation as in [lesson 01](01-attenuation-measurement.md):

$$\alpha_{\text{app}} = \frac{\pi f}{Q_{\text{app}} v}.$$

- **Intrinsic attenuation** comes from the imaginary part of the elastic
  moduli. Energy is converted to heat. $Q_{\text{int}}$ is a material property
  (a function of temperature, fluid content, melt fraction and frequency band)
  and is the quantity one wants when interpreting seismology for rock physics.
- **Scattering attenuation** comes from heterogeneity. The coherent field loses
  amplitude because the *phases* of the contributions from different parts of the
  wavefront no longer add constructively. No energy is lost: the total
  wavefield energy is conserved, and the missing amplitude reappears as coda.
  $Q_{\text{scat}}$ is not a material property at all — it is a property of the
  *statistics of the structure* and of the band.

The word **coherent** is doing the work. Any seismogram is one realisation of a
random medium, so the ensemble average is an idealisation; what we measure is one
draw, and §7 quantifies how badly a single draw estimates the mean.

## 2. Scattering regimes and the crossover frequency

The single dimensionless group that organises scattering is

$$ka = \frac{2\pi f}{v}\,a,$$

where $a$ is the correlation length of the velocity or impedance fluctuations and
$k = 2\pi f/v$ is the wavenumber. The crossover between the two physically
different limits is at $ka \approx 1$, which defines a frequency

$$\boxed{\;f_{c} = \frac{v}{2\pi a}.\;}$$

Two limits govern the frequency dependence of scattering attenuation:

- **Rayleigh regime, $ka \ll 1$** (heterogeneities much smaller than a
  wavelength). Each scatterer acts as a point source whose radiated power grows as
  $(ka)^4$, so $\alpha_{\text{scat}} \propto a^{3} f^{4} / v^{4}$. The dependence
  is *steep in frequency*, and this is the regime in which a measured $Q$ that
  depends strongly on $f$ is the signature of small-scale heterogeneity.
- **Geometric regime, $ka \gg 1$** (heterogeneities much larger than a
  wavelength). Rays travel through a smoothly varying structure; the loss of
  coherence is a *ray-geometrical* effect, with
  $\alpha_{\text{scat}} \approx 1/(2a)$ — approximately **independent of
  frequency**, and set by how far a ray must travel before the accumulated
  travel-time perturbation dephases it from its neighbours. A frequency-flat
  apparent $1/Q$ with no intrinsic cause lives here.

Between the two, at $ka \sim 1$, scattering has its maximum efficiency per unit
length and neither limit applies; this is the hardest regime to interpret and the
one most likely to be mistaken for intrinsic absorption.

*Worked example (SYNTHETIC).* Take $v = 3500\ \mathrm{m\,s^{-1}}$ and a Gaussian
correlation length $a = 800\ \mathrm{m}$. Then

$$f_c = \frac{v}{2\pi a} = \frac{3500}{2\pi \times 800}
= \frac{3500}{5026.5} = 0.6963\ \mathrm{Hz},$$

so the demonstration's band $[3, 15]\ \mathrm{Hz}$ lies entirely in the
geometric regime ($ka$ from $4.3$ to $21.5$): expect an approximately
frequency-independent scattering loss, and therefore an apparent $Q$ with little
curvature *within* that band. §6 shows that this is exactly what the
two-band test detects, and why a *wider* band is what the test needs.

## 3. The additivity rule

If the coherent amplitude obeys a single exponential
$A = A_0\exp(-(\alpha_{\text{int}}+\alpha_{\text{scat}})x)$ — that is, if
intrinsic and scattering losses are independent multiplicative factors — then
because $\alpha = \pi f/(Q v)$ at fixed $f$ and $v$,

$$\frac{1}{Q_{\text{app}}} = \frac{\alpha_{\text{app}}v}{\pi f}
= \frac{(\alpha_{\text{int}}+\alpha_{\text{scat}})v}{\pi f}
= \frac{1}{Q_{\text{int}}} + \frac{1}{Q_{\text{scat}}}.$$

The rule is exact if the two losses are independent, and it carries two
**immediate** consequences:

1. $Q_{\text{app}} \le Q_{\text{int}}$. **A measured $Q$ is a lower bound on the
   intrinsic $Q$.** A small measured $Q$ proves that coherent energy is
   disappearing; it does not prove that the energy became heat.
2. The rule is symmetric, so it cannot be inverted without a second
   measurement. Given only $1/Q_{\text{app}}$, the pair
   $(1/Q_{\text{int}}, 1/Q_{\text{scat}})$ is any point on a line: an exact
   one-parameter family of physically different Earths, all consistent with the
   data. This is the module's second non-uniqueness, and it is not a technicality
   — it is the reason that attenuation images of the mantle can be read either as
   temperature or as heterogeneity.

The demonstration tests the rule by adding a *known* intrinsic $Q$ to the same
random stacks and re-measuring the coherent decay. With a measured scattering
term $1/Q_{\text{scat}} = 7.7476\times10^{-3}$ (from a purely elastic medium, so
$Q_{\text{int}} = \infty$ by construction):

| $Q_{\text{int}}$ | $Q_{\text{measured}}$ | $1/Q_{\text{meas}}$ | $1/Q_{\text{int}} + 1/Q_{\text{scat}}$ | difference |
|---|---|---|---|---|
| 20 | 16.735 | 0.059756 | 0.057748 | $+3.48\%$ |
| 35 | 26.676 | 0.037487 | 0.036319 | $+3.22\%$ |
| 50 | 34.999 | 0.028572 | 0.027748 | $+2.97\%$ |
| 100 | 55.045 | 0.018167 | 0.017748 | $+2.36\%$ |
| 300 | 89.053 | 0.011229 | 0.011081 | $+1.34\%$ |

The rule holds to a few per cent over a factor of $15$ in intrinsic $Q$. The
residual growth of the discrepancy as $Q_{\text{int}}$ *falls* is the signal that
additivity is itself an approximation: it assumes the two mechanisms do not
interfere, which degrades as the total loss per wavelength grows. State the
regime with the rule.

## 4. How large is the artefact? The measurement

The demonstration computes the **exact** frequency-domain transmission
coefficient $T(f)$ of a $10\ \mathrm{km}$ random stack (100 layers of $100\
\mathrm{m}$, $20\%$ fractional rms velocity fluctuation, Gaussian correlation
length $800\ \mathrm{m}$, density uniform, 4000 realisations of a Thomson-Haskell
recursion for SH waves) and measures how the coherent mean $\langle T \rangle$
decays with frequency. There is **no intrinsic attenuation anywhere in this
model**: $Q_{\text{int}} = \infty$ by construction. Two calibrations come first:

- a uniform elastic stack returns $|T| = [1, 1, 1]$ exactly, as it must;
- a uniform anelastic stack with $Q_{\text{int}} = 100$ returns a fitted slope of
  $-8.975730\times10^{-2}\ \mathrm{Hz^{-1}}$ against the predicted
  $\pi L/(Qv) = -8.975979\times10^{-2}\ \mathrm{Hz^{-1}}$, i.e. a recovered
  $Q = 100.003$. Both limits are reproduced to six significant figures, so the
  recursion is right and the anelastic layers carry the intended loss.

Now the elastic random stack:

| $f$ (Hz) | $|\langle T\rangle|$ | $-\ln|\langle T\rangle|$ |
|---|---|---|
| 3.000 | 0.9416704 | 0.0601000 |
| 4.139 | 0.9069323 | 0.0976875 |
| 5.711 | 0.8464600 | 0.1666923 |
| 7.880 | 0.7478842 | 0.2905071 |
| 10.872 | 0.5975232 | 0.5149621 |
| 15.000 | 0.3963686 | 0.9254108 |

A straight-line fit of $-\ln|\langle T\rangle|$ against $f$ over the 16
frequencies of the band gives a slope
$6.954190\times10^{-2}\ \mathrm{Hz^{-1}}$, and inverting the definition
$\alpha = \pi f/(Qv)$ for a path length $L = 10\ \mathrm{km}$:

$$Q_{\text{app}} = \frac{\pi L}{v\,m}
= \frac{\pi \times 10^{4}}{3500 \times 0.0695419}
= \frac{31415.9}{243.40} = 129.07 .$$

**A perfectly elastic medium has produced a $Q$ of $129$.** Nothing was
absorbed; the amplitude left the coherent arrival and entered the coda. The
scatter about this number, from six independent sub-ensembles of about 667
realisations each, is
$1/Q_{\text{app}} = 7.751223\times10^{-3} \pm 4.670219\times10^{-4}$, i.e.
$Q_{\text{app}} = 129.01$ with a standard error of $7.77$ in $Q$ — about $6\%$.
With a *single* realisation instead of 4000, the same demo's own scaling
argument puts the scatter at order $100\%$: the apparent $Q$ of one random stack
is not a measurement of anything.

## 5. Why one band is not enough — the non-uniqueness made explicit

Fit a straight line to $\ln A(f)$ over one band and you obtain one number,
$m = \pi t^{*}$, hence one $Q_{\text{app}}$. Two different models that produce
the same $m$ are:

- **Model A** (pure intrinsic, band-averaged): $Q_{\text{int}} = 129$,
  $Q_{\text{scat}} = \infty$;
- **Model B** (pure scattering, elastic): $Q_{\text{int}} = \infty$,
  $Q_{\text{scat}} = 129$.

They are indistinguishable in the direct-arrival amplitude spectrum, band for
band, to machine precision — model B is the demonstration's *calculated* random
medium, and model A is a material that absorbs. Any mixture between them is
equally consistent: $1/Q_{\text{int}} = 1/Q_{\text{app}} - 1/Q_{\text{scat}}$
for any $Q_{\text{scat}} \ge Q_{\text{app}}$. This is a genuine non-uniqueness of
the observable, not an artefact of a bad estimator, and no amount of
signal-to-noise ratio removes it.

What removes it is a measurement that responds differently to the two:

| measurement | why it discriminates |
|---|---|
| **Frequency dependence over a wide band** | intrinsic $1/Q$ is flat or smoothly varying in a plateau; scattering turns over between the Rayleigh ($f^{4}$) and geometric ($f^{0}$) limits with a maximum near $ka \sim 1$ |
| **Coda decay versus direct-wave decay** | single-scattering coda is fed by the whole illuminated volume and decays with the *intrinsic* loss, so $Q_{\text{coda}} \approx Q_{\text{int}}$, while the direct arrival decays with $Q_{\text{app}}$; the pair gives both terms |
| **Spatial coherence across an array** | scattering decorrelates the wavefield over a length set by $a$; intrinsic loss does not change coherence at fixed amplitude |
| **Amplitude versus travel time for the same path** | intrinsic loss changes amplitude but leaves travel time alone; scattering perturbs both (travel-time fluctuations and amplitude fluctuations are coupled through the same structure) |
| **Energy balance** | intrinsic loss removes energy from the whole wavefield; scattering conserves it, so coda energy compensates a direct-wave deficit |

None of these is a proof in a single application. Each is a *different*
projection of the same structure, and each carries its own assumptions; that is
exactly why an attenuation interpretation should report the discriminating
measurement it used.

## 6. The two-band test, measured

The cheapest discriminator is to fit $Q$ separately in the lower and the upper
half of one band and compare. Intrinsic attenuation obeys
$\alpha = \pi f/(Qv)$ **exactly**, so a fit in any sub-band returns the same
number; scattering does not, so the two halves disagree in a *predictable
direction* (the low-frequency half sits closer to the $f^{4}$ regime and is
steeper, giving a larger apparent $Q$).

| band (Hz) | $Q$, elastic stack | err (6 sub-ensembles) | $Q$, uniform $Q_{\text{int}} = 100$ |
|---|---|---|---|
| $[3, 6.7]$ | 215.6 | $\pm 8.4$ | 100.00 |
| $[6.7, 15]$ | 110.6 | $\pm 7.6$ | 100.00 |

Ratio of the two answers: **1.95** for the elastic stack, **1.00** for the
intrinsic one. The elastic medium's apparent $Q$ halves across one decade,
against a standard error of a few per cent: a $16\sigma$ effect, so this is a
detection, not a fluctuation. And the statement is one-sided in the useful
direction:

- a **purely intrinsic** attenuator cannot produce a ratio away from $1$;
- a **scattering-contaminated** measurement cannot avoid one over a band that
  spans a regime change.

It is still not a proof. Two honest failure modes: a genuine intrinsic
attenuation with a relaxation peak *inside* the analysis band produces a ratio
away from $1$ too (see §6 of
[lesson 01](01-attenuation-measurement.md)); and a scattering medium whose band
lies entirely within one regime, as this one does in $[3,15]\ \mathrm{Hz}$
relative to $f_c = 0.70\ \mathrm{Hz}$, produces a ratio close to $1$ within that
band and only reveals itself when the analysis is extended across $f_c$.

## 7. Worked numeric examples

### Example 1 — from a measured slope to an apparent $Q$

A $10\ \mathrm{km}$ path in a medium with $v = 3500\ \mathrm{m\,s^{-1}}$ gives a
fitted slope $m = 0.0695419\ \mathrm{Hz^{-1}}$ for $-\ln A(f)$ versus $f$. Then
$\alpha(f) = m f$, and with $L = 10^{4}\ \mathrm{m}$,

$$Q_{\text{app}} = \frac{\pi L}{v m} = \frac{3.141593\times10^{4}}{3500\times0.0695419}
= 129.07, \qquad
\alpha(10\ \mathrm{Hz}) = \frac{\pi f}{Q_{\text{app}} v} = 6.954\times10^{-5}\ \mathrm{m^{-1}} .$$

The units check: $Q$ is $\mathrm{m}/(\mathrm{m\,s^{-1}}\times \mathrm{s})$,
dimensionless. The value of $1/\alpha$ at $10\ \mathrm{Hz}$,
$1.438\times10^{4}\ \mathrm{m}$, is *not* a wavelength: it is the
$1/e$ amplitude-decay length, and it shrinks as $f$ rises.

### Example 2 — recovering $Q_{\text{int}}$ when $Q_{\text{scat}}$ is known

From the additivity table, the measured $1/Q_{\text{app}}$ for the
$Q_{\text{int}} = 100$ case is $0.018167$. Using the independently measured
scattering term $1/Q_{\text{scat}} = 7.7476\times10^{-3}$:

$$\frac{1}{Q_{\text{int}}} = 0.018167 - 0.007748 = 0.010419
\qquad\Longrightarrow\qquad Q_{\text{int}} = \frac{1}{0.010419} = 95.98,$$

against a true value of $100$: a $-4.0\%$ error, entirely from the additivity
approximation (§3) rather than from data noise. Compare that with the error of
*not* subtracting the scattering term:
$1/Q_{\text{app}} = 0.018167 \Rightarrow Q = 55.0$, a $-45\%$ error in $Q$
(equivalently $+82\%$ in $1/Q$, relative to the true $0.01$). **The correction
is worth roughly an order of magnitude more than it costs.**

### Example 3 — the ensemble size needed

The measured $1/Q$ of a single realisation of a random medium is a random
variable. The demonstration's six sub-ensembles of about 667 realisations give a
standard error of $4.67\times10^{-4}$ in $1/Q_{\text{app}}$, i.e. about $6\%$,
and its own scaling argument puts a single realisation at order $100\%$. Since
the standard error of a mean falls as $1/\sqrt{N}$, reaching $1\%$ requires

$$N \approx \left(\frac{100\%}{1\%}\right)^{2} \approx 10^{4}\ \text{realisations} .$$

For a *measured* scattering $Q$ (not a modelled one) each realisation is a
different structure, which is unavailable: this is precisely why scattering $Q$
values are usually quoted as *modelled* quantities for a stated statistical
description of the medium, and why a single-path apparent $Q$ cannot be
separated into its two parts.

### Example 4 — crossing the regime boundary

With $a = 800\ \mathrm{m}$ and $v = 3500\ \mathrm{m\,s^{-1}}$ the crossover is
$f_c = 0.696\ \mathrm{Hz}$. At $f = 3\ \mathrm{Hz}$, $ka = 2\pi f a/v = 4.31$
(geometric); at $f = 0.1\ \mathrm{Hz}$, $ka = 0.144 \ll 1$ (Rayleigh). If a
measurement band were $[0.02, 2]\ \mathrm{Hz}$, it would span $ka$ from $0.029$
to $2.87$ and the Rayleigh $f^{4}$ turn-on would be visible as a strong
frequency dependence of the apparent $Q$; if the band is $[3,15]\ \mathrm{Hz}$
as in the demonstration, the test of §6 is blind to the crossover and only the
*curvature within* the geometric regime is available.

## 8. Assumptions and regime of validity

1. **Statistical stationarity** of the random medium along the path, and a
   single characteristic correlation length $a$. Real crustal heterogeneity is
   multi-scale, and the appropriate $a$ depends on the band being analysed.
2. **Weak fluctuations** ($\delta v/v \ll 1$). At $20\%$ rms as used here,
   single-scattering theory is already approximate; beyond roughly this level
   the coherent field's decay is not exponential in a simple way and the
   additivity rule degrades (§3).
3. **Separated length scales**: a finite layer thickness with a correlation
   length much shorter than the path, so that an ensemble average is meaningful.
4. **Independence of mechanisms** for the additivity rule (§3). Measured error
   a few per cent up to $\sim 30\%$ total loss over the path.
5. **The coda is single-scattered** if $Q_{\text{coda}} \approx Q_{\text{int}}$ is
   to be used. In the multiple-scattering (diffusive) regime the coda decay is
   set by the transport mean free path, not by the intrinsic $Q$ alone.
6. **The coherent field is what is measured.** Array processing that stacks
   incoherently, or a single-station pick that follows an early coda arrival,
   measures a different quantity.
7. **The band is stated.** Both $Q_{\text{app}}$ and the two-band ratio are band
   averages, for the reasons given in
   [lesson 01](01-attenuation-measurement.md) §5.

## 9. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| correlation length | $a$ | $\mathrm{m}$ | |
| wavenumber | $k$ | $\mathrm{m^{-1}}$ | $2\pi f/v$ |
| $ka$ | — | dimensionless | the only scaling group |
| crossover frequency | $f_c$ | $\mathrm{Hz}$ | $v/(2\pi a)$ |
| scattering attenuation | $\alpha_{\text{scat}}$ | $\mathrm{m^{-1}}$ | $1/(2a)$ in the geometric limit |
| apparent / intrinsic / scattering $Q$ | $Q$ | dimensionless | $1/Q$ values add |

The geometric-limit result $\alpha_{\text{scat}} = 1/(2a)$ is a useful sanity
check on any fitted scattering coefficient: it says the decay length is about
twice the correlation length, and it has the right dimensions
($\mathrm{m^{-1}}$) with no velocity in it — a purely geometrical statement.

## 10. Python demonstration

[`code/scattering_vs_intrinsic_demo.py`](code/scattering_vs_intrinsic_demo.py)
computes the exact transmission coefficient of a randomly layered medium and
measures the apparent attenuation of its coherent mean. It is the numerical heart
of this lesson: read section 1 (the two calibrations), then section 2 (the
elastic stack's apparent $Q$), then section 3 (additivity) and finally section 4
(the two-band test). Section 2 is the one that changes how a $Q$ value should be
read.

Full sets with worked solutions are in
[`exercises/02-scattering-vs-intrinsic-exercises.md`](exercises/02-scattering-vs-intrinsic-exercises.md)
and
[`exercises/02-scattering-vs-intrinsic-solutions.md`](exercises/02-scattering-vs-intrinsic-solutions.md).

## Mastery checkpoint

Without notes:

> A $10\ \mathrm{km}$ path in a medium with $v = 3500\ \mathrm{m\,s^{-1}}$
> yields $-\ln A(f)$ with a fitted slope $m = 0.05\ \mathrm{Hz^{-1}}$ over
> $[2, 12]\ \mathrm{Hz}$. **(a)** Compute $Q_{\text{app}}$ and $\alpha$ at
> $5\ \mathrm{Hz}$ with units. **(b)** A companion coda measurement gives
> $Q_{\text{coda}} = 260$; assuming $Q_{\text{coda}} \approx Q_{\text{int}}$,
> compute $Q_{\text{scat}}$ and state the assumption you used. **(c)** The same
> medium is measured over $[12, 40]\ \mathrm{Hz}$ and yields a $Q$ that is
> $1.4\times$ larger; is that consistent with intrinsic absorption, with
> scattering, or with neither? Justify with the regime argument. **(d)** A
> colleague reports "the mantle here has $Q = 60$, hence it is hot". Give two
> distinct reasons the inference can fail and one measurement that would test
> each.

A worked version appears in the
[solutions](exercises/02-scattering-vs-intrinsic-solutions.md).

## Common pitfalls

1. **Reading an apparent $Q$ as a material property.** $Q_{\text{app}} \le
   Q_{\text{int}}$, and only a discriminator (not a slogan) upgrades the bound to
   an equality.
2. **Fitting one band and quoting a mechanism.** Two models fit any single-band
   number exactly (§5).
3. **Using the additivity rule outside its regime.** A few per cent up to
   $\sim 30\%$ total loss; not at $Q \sim 10$ with strong scattering.
4. **Reporting a scattering $Q$ from one realisation.** The scatter is of order
   $100\%$ (§7, Example 3).
5. **Forgetting the regime parameter $ka$.** "Frequency-dependent $Q$ implies
   scattering" is only true in the Rayleigh regime; in the geometric regime the
   scattering loss is nearly frequency-independent and *mimics* a flat intrinsic
   $Q$.
6. **Confusing coda $Q$ with direct-wave $Q$ without saying so**, and using the
   coda equivalence outside single scattering.
7. **Assuming the correlation length is known.** It is usually the least
   constrained parameter, and $\alpha_{\text{scat}} = 1/(2a)$ shows why its
   error propagates straight into the correction.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the scattering and coda vocabulary this lesson quantifies.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the same
  ray-path integrals applied to travel time rather than amplitude.
- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  coherence-based measurement, the third discriminator in §5.
- [18-inverse-problems](../../18-inverse-problems/README.md) — underdetermination
  and how added measurements collapse a null space.

## Self-assessment checklist

- [ ] I can state where the energy goes in each mechanism.
- [ ] I can derive $1/Q_{\text{app}} = 1/Q_{\text{int}} + 1/Q_{\text{scat}}$.
- [ ] I can compute $f_c$ and classify a band by $ka$.
- [ ] I can compute $Q_{\text{app}}$ from a fitted slope with units.
- [ ] I can run and interpret the two-band test, including its failure modes.
- [ ] I can construct two distinct media consistent with one measured $Q$.
- [ ] I can estimate the ensemble size needed for a stated precision.
