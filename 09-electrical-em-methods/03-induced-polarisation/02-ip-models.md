---
id: 09-03-02
title: "IP Models: Cole-Cole, Debye, Constant-Phase Element"
level: doctoral
prereqs: ["09-03-01", "09-01-04", "01-11-06", "01-10-04"]
tags: [electrical-methods, induced-polarisation, cole-cole, debye, constant-phase-element, kramers-kronig, causality, non-uniqueness]
---

# IP Models: Cole-Cole, Debye, Constant-Phase Element

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the Cole-Cole complex resistivity and **derive** its DC and
   high-frequency limits, and show that the Debye is exactly the $c = 1$ member
   of the family.
2. **Derive** the phase of the Cole-Cole in terms of two arctangents and
   **compute** the amplitude and phase it predicts at a stated frequency.
3. **Measure** how the peak phase and the peak frequency depend on $m$ and $c$,
   and **state** how much of the Debye result survives at $c < 1$.
4. **Derive** the Kramers-Kronig gain-phase relation and **verify** it
   numerically; **state** what its success implies about how much independent
   information a phase measurement carries.
5. **Distinguish** the model exponent $c$ from the band-limited exponent
   $n_{\text{eff}} = (2/\pi)\lvert\varphi\rvert$ that an amplitude slope measures,
   and **demonstrate** the relation between them.
6. **Fit** a single Cole-Cole to a two-relaxation synthetic response, and
   **report** the parameter spread produced by noise rather than by a single
   number.
7. **Explain** why a fitted $(m, c, \tau)$ triple is an effective description of
   a band and a noise level, not a measurement of a material property.

## Prerequisites

- [09-03-01 IP Principle: Time-Domain and Frequency-Domain Measurement](01-ip-principle.md)
  — chargeability, the Debye element, and the step-off response.
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](../01-electrical-properties-of-earth/04-clay-and-surface-conduction.md)
  — why a real sample has many relaxation times.
- [01-11-06 Dispersion Relations and Causality in Wave Physics](../../01-mathematics/11-complex-analysis/06-dispersion-relations.md)
  — the causality argument behind the Kramers-Kronig relation.
- [01-10-04 Discrete Fourier Transform and the FFT](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md)
  — the discrete machinery of the measurement.

**All models and data in this module are SYNTHETIC.** The resistivities,
chargeabilities, exponents, time constants and noise levels are chosen teaching
values; no number here is a measurement of any sample, and no laboratory or
field value is quoted.

---

## 1. Intuition: one relaxation is a lie that is useful once

The Debye element of [09-03-01](01-ip-principle.md) predicts a phase spectrum
with a single sharp maximum at $\omega = 1/(\tau\sqrt{1-m})$, and it predicts that
the height of that maximum determines $m$ exactly. Measured spectra do not
behave that way: the phase is *broad*, it is often nearly flat over one or two
decades, and its height corresponds to a chargeability that disagrees with the
time-domain chargeability of the same sample.

The reason is structural rather than accidental. A rock contains a distribution
of relaxation times: pores of different sizes, grains of different
mineralogies, a surface charge layer whose thickness varies from point to point.
A sum of relaxations with different $\tau$ has a phase that is the sum of
shifted, overlapping single-relaxation phases, and the sum is **broader and
lower** than any of its parts. Fitting one relaxation to it is not wrong in the
sense of being a bad approximation in the band; it is wrong in the sense that
the parameters it returns are those of the best *effective* model, not of any
physical relaxation in the sample.

This lesson makes that statement quantitative in three ways: by an analytic
family that contains the broadening as a parameter (Cole-Cole), by a
causality argument that shows the amplitude and the phase are not independent
(Kramers-Kronig), and by fitting a single Cole-Cole to an exactly two-relaxation
synthetic response and reporting how far the parameters move.

## 2. Precise definitions

### 2.1 The Cole-Cole complex resistivity

$$
\boxed{\;\rho(\omega) = \rho_0\left[1 - m\left(1 - \frac{1}{1 + (i\omega\tau)^{c}}
\right)\right], \qquad 0 < c \le 1,\;}
$$

with $\rho_0$ the DC resistivity [$\Omega\,\mathrm{m}$], $m$ the chargeability
(dimensionless, $0 < m < 1$), $\tau$ a time constant [s] and $c$ an exponent
(dimensionless). At $c = 1$ this is exactly

$$\rho(\omega) = \rho_0\left[(1-m) + \frac{m}{1 + i\omega\tau}\right],$$

which is the Debye element of the previous lesson written as a resistor in series
with a parallel $RC$ element. So the Cole-Cole is a *one-parameter extension* of
the model already derived, and every limit of the Debye is a limit of the
Cole-Cole.

When $c < 1$ with $m = 1$ (a polarisable element that becomes perfectly
blocking at high frequency), the model reduces to the **constant-phase element**
(CPE) form $\rho \propto (i\omega)^{-c}$ in an intermediate band. The general CPE
is defined directly as

$$Z_{\text{CPE}}(\omega) = \frac{1}{Q(i\omega)^{n}}, \qquad
\varphi_{\text{CPE}} = -\frac{n\pi}{2}\ \text{exactly at every frequency}.$$

Section 5 measures how close a Cole-Cole comes to that idealisation, and finds a
number worth remembering: it is close in *shape* and far in *exponent*.

### 2.2 What the parameters are and are not

- $\rho_0$ is the DC limit, which a resistivity survey measures directly when
  the polarisation is negligible.
- $m$ is the fraction of the DC resistivity removed at infinite frequency. It is
  the same number that the time-domain decay amplitude reports.
- $\tau$ sets where the spectrum bends; it is not a grain diameter and it is not
  a time measured in the field.
- $c$ is a *shape* parameter. It is dimensionless, it has no universal value, and
  Section 6 shows it is the parameter a finite band constrains worst.

## 3. Derivations

### 3.1 Limits, and the exact reduction to the Debye at $c = 1$

Write $z = (i\omega\tau)^{c}$. Then

$$\rho(\omega) = \rho_0\,\frac{1 + (1-m)z}{1 + z}.$$

As $\omega \to 0$, $z \to 0$ and $\rho \to \rho_0$. As $\omega \to \infty$,
$|z| \to \infty$ and

$$\rho(\omega) \to \rho_0\,\frac{(1-m)z}{z} = \rho_0(1-m),$$

so the high-frequency limit is $\rho_0(1-m)$ — **independent of $c$**. The
demonstration prints $99.999999\ \Omega\,\mathrm{m}$ at $10^{-12}$ Hz against an
exact $\rho_0 = 100.0\ \Omega\,\mathrm{m}$, and $90.000000\ \Omega\,\mathrm{m}$
at $10^{12}$ Hz against an exact $90.0\ \Omega\,\mathrm{m}$. At $c = 1$ the
maximum difference between the Cole-Cole form and the Debye closed form over
$10^{-4}$ to $10^{4}$ Hz is $1.42\times10^{-14}\ \Omega\,\mathrm{m}$, i.e.
double-precision round-off: the two forms are the same function.

### 3.2 The phase of the Cole-Cole

Since a ratio of complex numbers has a phase equal to the difference of the
numerator and denominator phases, and $\arg\left[1 + (1-m)z\right]$ and
$\arg(1+z)$ are the only phases involved,

$$\varphi(\omega) = \arg\left[1 + (1-m)z\right] - \arg\left[1 + z\right],
\qquad z = (\omega\tau)^{c}e^{i\pi c/2}.$$

Because $(1-m) < 1$, the first arctangent is always smaller than the second and
$\varphi < 0$: the response lags, as it must for a network of resistors and
capacitors. The magnitude $|z| = (\omega\tau)^{c}$ replaces $\omega\tau$ as the
frequency variable, so **the whole spectrum is stretched in frequency by the
exponent**: a decade of $|z|$ corresponds to $1/c$ decades of $\omega$. That
single observation explains the broadening measured in the next table.

### 3.3 The measured spectra

For $\rho_0 = 100\ \Omega\,\mathrm{m}$, $m = 0.10$, $\tau = 1\ \mathrm{s}$ and
three exponents, the demonstration prints:

| $f$ (Hz) | $c=1.00$: $\lvert\rho\rvert$ / $-\varphi$ | $c=0.60$ | $c=0.25$ |
|---|---|---|---|
| 0.01 | 99.963 / 6.261 | 98.834 / 12.352 | 96.726 / 9.104 |
| 0.10 | 97.274 / 46.327 | 95.900 / 25.929 | 95.307 / 10.399 |
| 1.00 | 90.260 / 17.198 | 92.052 / 19.446 | 93.834 / 10.039 |
| 10.00 | 90.003 / 1.768 | 90.509 / 6.745 | 92.552 / 8.239 |
| 100.00 | 90.000 / 0.177 | 90.125 / 1.834 | 91.594 / 5.923 |

with $|\rho|$ in $\Omega\,\mathrm{m}$ and $-\varphi$ in mrad. Read the rows
across: at $c = 1$ the phase is $46.327$ mrad at $0.1$ Hz and has collapsed to
$0.177$ mrad three decades higher; at $c = 0.25$ the same model gives $10.399$
and $5.923$ mrad at those two frequencies. **The total polarisation is the same
($m = 0.10$, hence $\rho$ falls from $100$ to $90$ in every column), but the
frequency at which it happens is spread over three decades instead of one.**

### 3.4 Peak phase and peak frequency: what survives at $c < 1$

The demonstration locates the phase maximum on a grid of $400001$ frequencies
with a parabolic refinement. For $m = 0.10$:

| $c$ | peak $\lvert\varphi\rvert$ (mrad) | peak frequency $\times\ \tau$ |
|---|---|---|
| 1.00 | 52.656 | 0.1678 |
| 0.80 | 38.261 | 0.1700 |
| 0.60 | 26.834 | 0.1738 |
| 0.40 | 17.112 | 0.1816 |
| 0.25 | 10.476 | 0.1965 |

At $c = 1$ the analytic results of [09-03-01](01-ip-principle.md) hold
exactly: $\tan\lvert\varphi_{\max}\rvert = m/(2\sqrt{1-m}) = 0.052705$ gives
$52.656$ mrad at $f_{\max} = 1/(2\pi\tau\sqrt{1-m}) = 0.16776$ Hz, and the
numerical search returns $52.6559$ mrad at $0.16776$ Hz — the same numbers to
five digits. Below $c = 1$ the peak *height* falls steeply (a factor $5.0$
between $c = 1$ and $c = 0.25$) while the peak *frequency* moves by only $17\%$.

The height falls roughly linearly in $c$ at fixed $m$: a power-law fit over
$0.02 \le m \le 0.30$ at $c = 0.60$ gives

$$\left|\varphi_{\max}\right| = 0.3165\,m^{1.0565}\ \mathrm{rad},$$

so the peak phase is proportional to $m$ to the power $1.06$ — very nearly
linear, as in the Debye case. Two consequences:

- A peak phase of about $10$ mrad does **not** identify $m$: the table's
  $m = 0.02$ row gives $10.101$ mrad at $c = 1$ but only $5.147$ mrad at
  $c = 0.60$ and $2.009$ mrad at $c = 0.25$, while the $m = 0.10$ row gives
  $10.476$ mrad at $c = 0.25$. So one observed peak height of $10$ mrad is
  consistent with $m = 0.02$ or with $m = 0.10$ — a factor of five in
  chargeability, decided by a shape parameter nobody measured.
- The peak *frequency* is a weak function of $m$ and $c$
  ($f_{\max}\tau$ between $0.1608$ and $0.3248$ across the whole measured table),
  so it is a robust but imprecise clock: $\tau$ recovered from it is uncertain by
  a factor of two unless $m$ and $c$ are known.

### 3.5 Causality: the amplitude and the phase are not independent

A response function of a physically realisable, causal, minimum-phase linear
system cannot be chosen freely in amplitude and phase. The two are related by
the Kramers-Kronig (Bode gain-phase) relation:

$$\varphi(\omega_0) = \frac{2\omega_0}{\pi}\,
\operatorname{PV}\!\int_0^{\infty}
\frac{\ln\left|\rho(\omega)\right|}{\omega^2 - \omega_0^2}\,\mathrm{d}\omega,$$

where PV marks the Cauchy principal value and the sign convention is the one
verified below. The demonstration evaluates this principal-value integral with a
Cauchy-weighted quadrature over twenty-five decades of frequency and adds the
out-of-band contributions in closed form from the measured asymptotes. The
check on a first-order pole $H = 1/(1+i\omega\tau)$, whose phase is exactly
$-\arctan(\omega\tau)$, gives agreement between $4.8\times10^{-10}$ and
$5.4\times10^{-10}$ rad at five frequencies. Applied to the Cole-Cole model it
gives, for $c = 1.00$, $0.60$ and $0.25$ and three frequencies each, a maximum
difference of $2.0\times10^{-9}$ mrad ($2.0\times10^{-12}$ rad) between the
reconstructed and the model phase.

**Interpretation, stated carefully.** Every Cole-Cole model is minimum-phase, so
its phase is *determined by* its amplitude. Measuring both is not two
measurements; it is one measurement displayed twice. That does not make phase
useless — it is usually the more precise of the two in a field survey — but it
removes a common argument: one cannot claim independent support for an
interpretation from the agreement of the amplitude and the phase. The
verification also does double duty as a numerical-health check: a large KK
residual on a fitted model means the fit is not a realisable response, which in
practice signals a fitting artefact such as unconstrained high-frequency
behaviour.

### 3.6 The measured exponent of a band is not $c$

If $\lvert\rho\rvert \propto \omega^{-n}$ over a band, then the response is a
CPE with exponent $n$ over that band and its phase is exactly $-n\pi/2$ there.
The demonstration measures, over two decades of frequency, both the amplitude
slope and $(2/\pi)$ times the mean phase:

| $c$ | $\lvert\varphi\rvert$ min–max (mrad) | range/mean | amplitude slope | $(2/\pi)$ mean $\lvert\varphi\rvert$ |
|---|---|---|---|---|
| 1.00 | 1.768–52.656 | 2.264 | $-0.0140$ | $-0.01480$ |
| 0.60 | 6.745–26.834 | 1.445 | $-0.0127$ | $-0.01182$ |
| 0.40 | 9.122–17.112 | 1.191 | $-0.0097$ | $-0.00915$ |
| 0.25 | 8.239–10.476 | 1.070 | $-0.0064$ | $-0.00623$ |
| 0.10 | 4.012–4.145 | 1.009 | $-0.0026$ | $-0.00262$ |

Two separate lessons are in this table. First, the flatness improves as $c$
falls: the ratio of the phase range to its mean drops from $2.264$ to $1.009$,
so at $c = 0.10$ the phase is constant to within $1\%$ over two decades — a
genuine constant-phase *shape*. Second, the exponent that the band measures is
$n_{\text{eff}} = 0.0026$ at $c = 0.10$, not $c = 0.10$: **a flat phase implies a
power law, but its exponent is not the model's $c$.** The two columns agree with
each other to $7\%$ or better at every $c$, which is the practical content of
the relation

$$\text{slope} \approx -\frac{2}{\pi}\left|\varphi\right|
\quad\text{(over a band where the slope varies slowly).}$$

That is the Bode relation applied locally: the exact integral relation of
Section 3.5, restricted to a band over which $\log\lvert\rho\rvert$ is nearly
linear. Inverting it, a field measurement of a slope of $0.0026$ would be
reported as "a CPE with $n = 0.0026$", a statement about the band — and it would
say nothing about how wide the underlying distribution of relaxation times is,
which is what $c$ describes.

## 4. Physical interpretation

- **Broadening is information about heterogeneity, but not about any length
  scale.** The exponent $c$ measures how spread the distribution of relaxation
  times is; it cannot be converted into a pore size, a grain size or a clay
  fraction without an independent petrophysical model.
- **$m$ and $c$ compete.** At fixed $m$ the peak phase falls steeply with $c$
  ($52.656$ to $10.476$ mrad from $c = 1$ to $c = 0.25$). Since $c$ is the
  hardest parameter to measure, $m$ is systematically underestimated when a
  single-relaxation interpretation is applied to broad data.
- **The Debye limit is a diagnostic, not a target.** If a spectrum really is a
  single relaxation, its phase peak height and position give $m$ and $\tau$ with
  no ambiguity. Failing that test is the first useful thing to check.
- **Amplitude and phase are one measurement.** The KK check confirms it. The
  practical corollary is that a misfit in amplitude implies a misfit in phase;
  a model that fits one and not the other is not a candidate model at all.
- **The CPE is a band description.** When a spectrum is flat in phase, the
  useful report is the band, the slope and the phase, not a fitted physical
  time constant that the band cannot constrain.

## 5. Assumptions and regime of validity

1. **Linear, time-invariant, causal response.** This is what licenses the KK
   relation. Nonlinearity (high current density) or a time-varying ground
   (freezing, drainage) breaks it, and then no KK check can succeed.
2. **No electromagnetic coupling.** Induction adds its own phase, quadratically
   growing with frequency, which is *not* polarisation. Above the coupling
   frequency the fitted $c$ mostly measures the coupling.
3. **A single Cole-Cole element is assumed in every fit here.** Real ground is
   better described by a sum of Cole-Cole elements (the "generalised Cole-Cole"
   or a Havriliak-Negami type form); Section 6 measures the cost of not allowing
   for that.
4. **The frequency band is finite.** Every number in the tables above is a
   band-limited quantity. Parameter values obtained on one band do not transfer
   to another.
5. **The noise model is stated and simple:** $1\%$ multiplicative noise on
   $|\rho|$ and $0.5$ to $2$ mrad additive noise on the phase, independent
   between frequencies. Real IP noise is correlated with the telluric field and
   with the electrode state, so the spreads reported here are lower bounds.
6. **$\rho_0$ is treated as known** in Section 6's fits, because a resistivity
   measurement determines it far more precisely than IP does.

## 6. Worked examples

### Example 1 — amplitude and phase at one frequency, by hand

Model: $\rho_0 = 100\ \Omega\,\mathrm{m}$, $m = 0.10$, $c = 0.60$,
$\tau = 1.0$ s. Compute $\rho$ at $f = 0.1$ Hz.

1. $\omega = 2\pi f = 0.628319\ \mathrm{rad\,s^{-1}}$, so
   $\omega\tau = 0.628319$ and $\lvert z\rvert = (\omega\tau)^{c} =
   e^{0.6\ln 0.628319} = e^{-0.278796} = 0.756672$.
2. $\arg z = \pi c/2 = 0.942478$ rad, so
   $z = 0.756672\left(\cos 0.942478 + i\sin 0.942478\right) = 0.444761 +
   0.612161i$.
3. $1 + z = 1.444761 + 0.612161i$, with
   $\lvert1+z\rvert^{2} = 2.462075$, so
   $1/(1+z) = 0.586806 - 0.248636i$.
4. $1 - 1/(1+z) = 0.413194 + 0.248636i$, and
   $\rho/\rho_0 = 1 - 0.10\left(0.413194 + 0.248636i\right) =
   0.958681 - 0.024864i$.
5. $\lvert\rho\rvert = 100 \times 0.958987 = 95.900\ \Omega\,\mathrm{m}$ and
   $\varphi = \arctan(-0.024864/0.958681) = -0.025929$ rad
   $= -25.929$ mrad.

Both printed values — $95.900\ \Omega\,\mathrm{m}$ and $25.929$ mrad — match the
demonstration's table to every printed digit. The same computation at $f = 1$ Hz
gives $\omega\tau = 6.283185$, $z = 1.770625 + 2.437056i$,
$\rho/\rho_0 = 0.920349 - 0.017899i$, i.e. $92.052\ \Omega\,\mathrm{m}$ and
$19.446$ mrad, again matching the table.

### Example 2 — the Debye check at $c = 1$

Same $m$ and $\tau$, now $c = 1$: $\tan\lvert\varphi_{\max}\rvert =
0.10/(2\sqrt{0.90}) = 0.052705$, hence $52.656$ mrad, at
$f_{\max} = 1/(2\pi \times 1.0 \times \sqrt{0.90}) = 0.16776$ Hz. The
demonstration's numerical search returns $52.6559$ mrad at $0.16776$ Hz. Now
apply the *same* closed forms to the $c = 0.60$ case: they predict $52.656$ mrad
at $0.16776$ Hz, whereas the measured Cole-Cole values are $26.834$ mrad at
$0.1738$ Hz. The height is wrong by a factor $1.96$ and the frequency by $3.6\%$.
**A wrong model fails on the peak height, not on the peak position** — which is
why reporting the phase-peak frequency alone is safer than reporting a
chargeability derived from its height.

### Example 3 — what noise does to a fitted triple

The demonstration takes an exact two-relaxation response
($m = 0.120$, $\tau = 0.30$ s with weight $0.45$ and $\tau = 6.00$ s with weight
$0.55$) sampled at $25$ frequencies from $0.01$ to $100$ Hz, fits one Cole-Cole,
and repeats the fit over $150$ noise realisations at $5\%$ amplitude and
$2$ mrad phase noise. The results, read off the demonstration:

| quantity | noise-free fit | $5\%$ / $2$ mrad median | $5$–$95\%$ range |
|---|---|---|---|
| $m$ | 0.1426 | 0.1404 | $[0.1350, 0.1461]$ |
| $c$ | 0.5478 | 0.5565 | $[0.5318, 0.5805]$ |
| $\tau$ (s) | 2.4002 | 2.2690 | $[1.9713, 2.7371]$ |

Three things follow. (i) Even with **no noise at all** the fit returns
$m = 0.1426$ and $\tau = 2.4002$ s, which are not the truth ($0.120$, and two
times of $0.30$ and $6.00$ s): the model family, not the noise, sets a floor on
the error. (ii) The noise widens the admitted ranges to about $\pm 4\%$ in $m$
and $-13\%/+21\%$ in $\tau$ at $5\%$ amplitude noise. (iii) The fitted exponent
and time constant are correlated, with $\mathrm{corr}(c, \log_{10}\tau) = -0.518$
over the Monte Carlo: a slightly larger $c$ is compensated by a slightly smaller
$\tau$, so quoting them as independent numbers overstates what the data contain.

## 7. Python demonstration

`code/ip_models_demo.py` prints every number in this lesson. It:

1. computes the DC and high-frequency limits and the $c = 1$ reduction
   ($1.42\times10^{-14}\ \Omega\,\mathrm{m}$ maximum difference);
2. tabulates $|\rho|$ and $-\varphi$ for the three-exponent family;
3. locates the phase peak for fifteen $(m, c)$ pairs on a fine grid, compares
   $c = 1$ with the analytic formulae, and fits the measured $m$-dependence;
4. evaluates the Kramers-Kronig integral, validated on a first-order pole and
   then applied to Cole-Cole models with three exponents;
5. fits one Cole-Cole to a two-relaxation truth at three noise levels and
   reports a $150$-realisation Monte Carlo;
6. measures the phase flatness, the amplitude slope and the band exponent for six
   exponents.

Run it with the project virtual environment:

```bash
cd 09-electrical-em-methods/03-induced-polarisation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_models_demo.py
```

## 8. Exercises

Full sets with worked solutions are in
[`exercises/02-ip-models-exercises.md`](./exercises/02-ip-models-exercises.md)
and
[`exercises/02-ip-models-solutions.md`](./exercises/02-ip-models-solutions.md).

- **★** Compute $\rho$ at $1$ Hz for $\rho_0 = 200\ \Omega\,\mathrm{m}$,
  $m = 0.05$, $c = 0.5$, $\tau = 0.2$ s, showing each intermediate complex
  number.
- **★★** Explain, using $|z| = (\omega\tau)^c$, why at $c = 0.25$ the phase at
  $0.01$ Hz is $9.104$ mrad, already $87\%$ of that model's $10.476$ mrad peak,
  whereas at $c = 1$ the same frequency gives $6.261$ mrad, only $12\%$ of its
  $52.656$ mrad peak.
- **★★** Show that $\rho(\omega \to \infty) = \rho_0(1-m)$ independently of $c$,
  and explain why that makes the DC and HF limits poor discriminants.
- **★★★** Reproduce the $c$-dependence of the band exponent: for
  $c \in \{1, 0.6, 0.25, 0.1\}$, measure the amplitude slope over two decades and
  compare with $(2/\pi)\lvert\varphi\rvert$, and explain the trend.

## 9. Common mistakes

1. **Reporting $c$ as if it were a physical property.** It is a shape parameter
   of an effective model; Section 3.6 shows the band's own exponent is an order
   of magnitude different at small $c$.
2. **Inverting a phase peak height for $m$ without stating $c$.** The same
   10 mrad corresponds to $m$ from $0.019$ to $0.095$ across the measured table.
3. **Treating phase and amplitude as independent evidence.** The KK relation
   makes them one measurement.
4. **Fitting outside the band where the model is validated.** Every parameter
   here is a band-limited quantity.
5. **Forgetting electromagnetic coupling.** It contributes phase that grows
   with frequency and is easily mistaken for a small $c$.
6. **Quoting a single best-fit triple without a range.** Section 6.3 gives the
   ranges; a single number without them cannot be checked.
7. **Assuming the noise-free fit is the truth.** With two relaxations in the
   ground, the noise-free fit of a one-relaxation model is wrong by more than the
   noise-induced spread.

## 10. Real-world applications

- **Spectral IP (SIP) in the laboratory and the field.** The $(m, c, \tau)$
  triple is the standard report format for laboratory SIP, and the same
  caution applies there as here: the triple is a summary of the measurement
  band.
- **Discrimination of mineralisation styles.** The shape of the spectrum, not
  its level, is what differs between disseminated and massive textures, which is
  the classical use of the frequency dependence.
- **Clay and salinity discrimination.** A change in the pore-fluid conductivity
  flattens the spectrum while a change in surface conduction scales it, so the
  shape is the discriminator — see
  [04 IP for Sulphides, Clays, Contaminants and Permafrost](04-ip-applications.md).
- **Model validation in inversion.** The KK check is a cheap, decisive test that
  an inverted spectrum is physically realisable; automated inversions that report
  models failing it are reporting fitting artefacts.

## 11. Further reading

- **Pelton, W. H., Ward, S. H., Hallof, P. G., Sill, W. R., & Nelson, P. H.,
  "Mineral discrimination and removal of inductive coupling with multifrequency
  IP", *Geophysics* 43 (1978).** Level: research. The paper that put the
  Cole-Cole model into routine IP practice.
- **Macdonald, J. R. (ed.), *Impedance Spectroscopy* (Wiley).** Level:
  advanced textbook. The circuit and the Kramers-Kronig relations as they are
  used in the electrochemical literature.
- **Bode, H. W., *Network Analysis and Feedback Amplifier Design* (Van
  Nostrand).** Level: classic. The gain-phase relation, in the form used here.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*
  (2nd ed., Cambridge University Press).** Level: textbook. The IP field method
  and its conventions.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. No number in this lesson is
> quoted from any of them: every figure comes from
> [`code/ip_models_demo.py`](./code/ip_models_demo.py), apart from exact
> mathematical constants such as $\pi$ and $e$.

## 12. Related lessons

- [01 IP Principle: Time-Domain and Frequency-Domain Measurement](01-ip-principle.md) —
  the Debye element and the chargeability conventions this lesson extends.
- [03 IP Acquisition, Chargeability and Phase Units](03-ip-acquisition.md) —
  how the measurement noise and the window set the admitted parameter ranges.
- [04 IP for Sulphides, Clays, Contaminants and Permafrost](04-ip-applications.md) —
  the pathway model that gives $(m, c, \tau)$ a physical reading.
- [08-05-01 Frequency-Domain EM Systems and Responses](../../08-geomagnetism-electromagnetism/05-controlled-source-em/01-frequency-domain-em.md) —
  the induction response that must be separated from the polarisation phase.
- [01-11-06 Dispersion Relations and Causality in Wave Physics](../../01-mathematics/11-complex-analysis/06-dispersion-relations.md) —
  the general theory behind Section 3.5.

## 13. Self-assessment checklist

- [ ] I can write the Cole-Cole model and derive both of its limits.
- [ ] I can show that $c = 1$ is exactly the Debye element.
- [ ] I can compute $|\rho|$ and $\varphi$ at a stated frequency by hand.
- [ ] I can state the analytic peak-phase and peak-frequency results and use
      them to check a numerical spectrum.
- [ ] I can explain the KK relation and what its success implies.
- [ ] I can distinguish the model exponent $c$ from the band exponent
      $n_{\text{eff}}$.
- [ ] I can fit one relaxation to a two-relaxation response and report the
      admitted range instead of a single triple.
