---
id: 06-04-06
title: "Energy Release, Moment Calculations and Scaling"
level: graduate
prereqs: ["06-04-05", "06-03-03", "06-03-06"]
tags: [seismology, seismic-moment, radiated-energy, apparent-stress, scaling]
---

# Energy Release, Moment Calculations and Scaling

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the scalar moment from the low-frequency plateau of a far-field
   displacement spectrum and **invert** a measured plateau for $M_0$.
2. **Integrate** the far-field velocity pulse over time and over the focal sphere
   to obtain the radiated energy, in closed form and numerically.
3. **Derive** the scaling $E_R \propto M_0$ for a self-similar family and the
   consequent slope $\mathrm{d}\log_{10}E_R/\mathrm{d}M_w = 3/2$.
4. **Derive** the apparent stress $\tau_a = \mu E_R/M_0$ and compare it with a
   static stress drop computed from a source radius.
5. **Test** self-similarity by measuring the exponent in $r \propto M_0^{p}$
   instead of assuming it.
6. **Quantify** how a fixed recording band biases the energy of small and large
   events, and state what must accompany every $E_R$ estimate.

## Prerequisites

- [05 Magnitude Saturation and Why Moment Magnitude Is Preferred](05-magnitude-saturation.md) —
  the energy-proxy slope this lesson derives.
- [06-03-03 Moment Tensors, Decomposition and Physical Meaning](../03-earthquake-sources/03-moment-tensors.md).
- [06-03-06 Rupture Dynamics, Fracture Energy and Scaling Laws](../03-earthquake-sources/06-rupture-dynamics.md).

## 1. Intuition: two different questions

"How strong was the earthquake?" and "how much energy did it radiate?" are not
the same question, and their answers have different units.

- The **seismic moment** $M_0 = \mu \bar{D} A$ (units $\mathrm{N\,m}$) is a
  *static* property of the source: rigidity times average slip times rupture
  area. It is read from the low-frequency plateau of the displacement spectrum,
  where every event — small or great — has energy.
- The **radiated energy** $E_R$ (units J) is a *dynamic* property: the work done
  by the source on the medium in the form of seismic waves. It is an integral of
  the squared ground velocity over time and over all directions, and it is
  therefore sensitive to the *whole* spectrum, including frequencies the
  recording may not contain.

That difference in units is the honest difficulty of this lesson. A moment can be
measured from a band-limited record, provided the band reaches the plateau. An
energy integral over a band is not the energy; Section 7 measures how large the
difference is for a 2 Hz band, and the answer is a factor of ten for the smallest
events in the family.

## 2. Definitions

| quantity | symbol | definition | unit |
|---|---|---|---|
| scalar moment | $M_0$ | $\mu \bar{D} A$ | $\mathrm{N\,m}$ |
| moment magnitude | $M_w$ | $\tfrac{2}{3}(\log_{10}M_0 - 9.1)$ | — |
| radiated energy | $E_R$ | $\rho\beta R^{2}\oint\int v^{2}\,\mathrm{d}t\,\mathrm{d}\Omega$ | J |
| apparent stress | $\tau_a$ | $\mu E_R/M_0$ | Pa |
| static stress drop | $\Delta\sigma$ | $\tfrac{7}{16} M_0 / r^{3}$ | Pa |
| source radius | $r$ | $2.34\,\beta/(2\pi f_c)$ | m |

The apparent stress is the *dynamic* measure of how energetic the rupture was per
unit of moment; the static stress drop is the *static* measure of how much the
stress changed. They are different quantities, and their ratio is a real,
model-independent number to measure (Example 4).

## 3. Derivations

### 3.1 Moment from the plateau

The far-field displacement of a point source, written with the source's own
spectrum, is

$$
u(f, \text{direction}) = \frac{M_0\,a(\text{direction})}{4\pi\rho\beta^{3}R}
\,S(f)\,e^{-\pi f t^{*}/Q} \qquad (\mathrm{m\,s}),
$$

where the last factor is the attenuation along the path with $t^{*} = R/\beta$,
$a$ is the radiation coefficient, and $S(0) = 1$. Taking the low-frequency limit
removes both the source shape and the attenuation, so

$$
\boxed{\;M_0 = \frac{4\pi\rho\beta^{3}R\,\Omega_0}{a}\;},
$$

a formula that is *inverted* in practice: measure the plateau $\Omega_0$, divide
by the known path and instrument terms, and $M_0$ follows. The dependence on $a$
is the weak link: a single station gives no way to separate $a$ from $M_0$, and
substituting its average is the standard compromise.

### 3.2 Radiated energy from a far-field pulse

The far-field particle velocity in one direction is $v(t)$; the energy flux
carried by a spherical wave is $\rho\beta v^{2}$ per unit area, so the total
radiated energy is the flux integrated over time and over the sphere at radius
$R$:

$$
E_R = \rho\beta R^{2}\oint\!\!\int v^{2}(\theta,\phi,t)\,
\mathrm{d}t\,\mathrm{d}\Omega
= \rho\beta R^{2}\,\langle\,\textstyle\int v^{2}\,\mathrm{d}t\,\rangle\,4\pi ,
$$

where $\langle\cdot\rangle$ is the average over the focal sphere.

For the Brune-type pulse used in this lesson the far-field *displacement* is

$$
u(t) = A\,\frac{t}{\tau^{2}}\,e^{-t/\tau} \qquad (t \ge 0),
\qquad \tau = \frac{1}{2\pi f_c},
$$

so that $\int_0^{\infty} u\,\mathrm{d}t = A$ and the spectral plateau is exactly
$A$; here $A = M_0 a/(4\pi\rho\beta^{3}R)$. Differentiating,

$$
v(t) = \frac{\mathrm{d}u}{\mathrm{d}t}
= \frac{A}{\tau^{2}}\big(1 - t/\tau\big) e^{-t/\tau} ,
$$

and the energy integral in one direction follows from
$\int_{0}^{\infty}\big(1-s\big)^{2}e^{-2s}\,\mathrm{d}s = \tfrac14$ with
$s = t/\tau$:

$$
\int_0^{\infty} v^{2}\,\mathrm{d}t
= \frac{A^{2}}{\tau^{4}}\cdot\frac{\tau}{4}
= \frac{A^{2}}{4\tau^{3}} .
$$

Substituting $A = M_0a/(4\pi\rho\beta^{3}R)$ gives the closed form

$$
\boxed{\;E_R = \rho\beta R^{2}\,4\pi\langle a^{2}\rangle
\left(\frac{M_0}{4\pi\rho\beta^{3}R}\right)^{2}\frac{1}{4\tau^{3}}\;}
$$

and the numerical integral in Section 6 checks it (the agreement is 0.25 per
cent, which is the Monte Carlo error of the sphere average).

### 3.3 The scaling, and why the energy slope in $M_w$ is $3/2$

Everything in the box above scales as a power of $M_0$ except $\tau$:

$$
E_R \propto M_0^{2}\,\tau^{-3} \propto M_0^{2}f_c^{3}
\propto M_0^{2}M_0^{-1} = M_0 ,
$$

using the self-similar $f_c \propto M_0^{-1/3}$. Therefore

$$
\log_{10}E_R = \log_{10}M_0 + \text{const}
= \tfrac{3}{2}M_w + \text{const} ,
\qquad
\frac{\mathrm{d}\log_{10}E_R}{\mathrm{d}M_w} = \frac{3}{2} .
$$

The exponent $3/2$ is usually quoted as an empirical property of the standard
energy–magnitude relation. Here it is *derived*, and the derivation identifies
its assumption exactly: constant stress drop. If stress drop grew with event
size, the exponent would be larger; if it fell, smaller. Measuring the exponent
is therefore a test of self-similarity, not a law of nature.

### 3.4 Apparent stress, and what it is compared with

The apparent stress is

$$
\tau_a = \frac{\mu E_R}{M_0} ,
$$

which is independent of $M_0$ for the self-similar family above. The static
stress drop of a circular crack of radius $r$ is

$$
\Delta\sigma = \frac{7}{16}\frac{M_0}{r^{3}} .
$$

With $r$ from the corner frequency and $E_R \propto M_0$, the ratio
$\tau_a/\Delta\sigma$ is *also* independent of size, and its value is the
model-independent content of the comparison. In the synthetic family of
Section 6 it comes out at 0.23.

## 4. The energy you measure depends on the band

For the pulse above the far-field velocity spectrum has magnitude

$$
|V(f)| = \frac{2\pi f\,A}{1 + (2\pi f\tau)^{2}} .
$$

Parseval gives the total energy integral, and the fraction below a low-pass
$f_{\text{lp}}$ is

$$
\frac{E(f < f_{\text{lp}})}{E_{\text{total}}}
= \frac{2}{\pi}\left[\arctan X - \frac{X}{1 + X^{2}}\right],
\qquad X = \frac{f_{\text{lp}}}{f_c} = 2\pi f_{\text{lp}}\tau ,
$$

which follows from $\int_0^{X} \frac{x^{2}}{(1+x^{2})^{2}}\,\mathrm{d}x =
\tfrac{1}{2}\left[\arctan X - \tfrac{X}{1+X^{2}}\right]$ and the total
$A^{2}/(4\tau^{3})$ derived above. The demonstration checks this closed form
against a direct numerical band integral: at $f_c = 0.6\ \mathrm{Hz}$ both give
$0.639236$.

The limit $X \to 0$ is worth recording. Expanding,
$\arctan X - X/(1+X^{2}) \approx \tfrac{2}{3}X^{3}$, so

$$
\frac{E(f<f_{\text{lp}})}{E_{\text{total}}}
\approx \frac{4}{3\pi}X^{3}
\propto f_{\text{lp}}^{3}\,\tau^{3}
\propto \left(\frac{f_{\text{lp}}}{f_c}\right)^{3},
$$

which is the statement that a band far below the corner frequency captures a tiny
fraction of the energy, growing as the cube of the band edge. This is why a
short-period instrument cannot measure the energy of a small event, and why the
bias of a band-limited energy is size-dependent.

## 5. Worked examples

All numbers are printed by `code/energy_moment_calculations_demo.py`, whose
synthetic model is $\rho = 2700\ \mathrm{kg\,m^{-3}}$,
$\beta = 3500\ \mathrm{m\,s^{-1}}$, $R = 100\ \mathrm{km}$, $Q = 400$ so
$t^{*} = 28.57\ \mathrm{s}$, and $f_c = 0.6\ \mathrm{Hz}$ at
$M_0 = 10^{15}\ \mathrm{N\,m}$.

### Example 1 — the radiation coefficient, integrated

Using the exact double-couple pattern $a^{2}(\mathbf{n}) =
|\mathbf{M}\mathbf{n}|^{2} - (\mathbf{n}^{T}\mathbf{M}\mathbf{n})^{2}$ and a
Monte Carlo average over 40000 directions on the focal sphere,

$$
\langle a^{2}\rangle = 0.4000 \pm 0.0013 ,
\qquad \sqrt{\langle a^{2}\rangle} = 0.6325 .
$$

The analytic value for a double couple is $\langle a^{2}\rangle = 2/5 = 0.4$, so
the numerical integral reproduces it within its own error. Two remarks belong
here: the classic "average radiation coefficient" of 0.63 is not a textbook
constant in this lesson but a quantity the demonstration computed; and a real
moment obtained from a single station carries this factor as a 20 to 30 per cent
uncertainty, because $\langle a^{2}\rangle$ is an average over directions the
station cannot see.

### Example 2 — a moment recovered from a plateau, by hand

For $M_0 = 10^{15}\ \mathrm{N\,m}$, the path factor is

$$
4\pi\rho\beta^{3}R = 4\pi\times2700\times(3500)^{3}\times10^{5}
= 1.4547\times10^{20}\ \mathrm{N\,s^{2}\,m^{-1}} ,
$$

so the plateau is
$\Omega_0 = 10^{15}\times0.6325/1.4547\times10^{20} = 4.348\times10^{-6}\ \mathrm{m\,s}$.
Inverting, $M_0 = 1.4547\times10^{20}\times4.348\times10^{-6}/0.6325 = 10^{15}\ \mathrm{N\,m}$
and $M_w = \tfrac{2}{3}(15 - 9.1) = 3.93$. The demonstration fits a 120-point
spectrum from 0.005 to 20 Hz for $(M_0, f_c)$ in log space with the attenuation
included and recovers both parameters to better than 0.01 per cent at every size
tested.

### Example 3 — what an unmodelled $t^{*}$ costs, with its sign

Fitting the *same* attenuated spectra with a model that omits the attenuation
factor produces a systematic error whose direction is worth knowing:

| $M_0$ (N m) | $M_w$ | $M_0$ error | $f_c$ error |
|---|---|---|---|
| $10^{13}$ | 2.60 | $+4.96\ \%$ | $-63.39\ \%$ |
| $10^{14}$ | 3.27 | $+7.61\ \%$ | $-56.18\ \%$ |
| $10^{15}$ | 3.93 | $+9.87\ \%$ | $-50.25\ \%$ |
| $10^{16}$ | 4.60 | $+12.14\ \%$ | $-45.52\ \%$ |
| $10^{17}$ | 5.27 | $+15.16\ \%$ | $-42.00\ \%$ |

A spectrum falling faster than $f^{-2}$ can only be produced by a model with
$f^{-2}$ decay if the corner moves **down**, so $f_c$ is biased low by 42 to
63 per cent; the plateau is then extrapolated from an over-steepened curve and
the moment comes out 5 to 15 per cent **high**, with the error growing with
event size because a larger event has more of its spectrum inside the attenuated
band. This is why an $M_0$ must always be quoted with the attenuation correction
that produced it.

### Example 4 — radius, self-similarity and stress

Using the Brune circular-crack relation $r = 2.34\beta/(2\pi f_c)$:

| $M_0$ (N m) | $f_c$ (Hz) | $r$ (km) | $\log_{10}M_0$ | $\log_{10}(r/\mathrm{km})$ |
|---|---|---|---|---|
| $10^{13}$ | 2.7850 | 0.47 | 13.00 | $-0.330$ |
| $10^{14}$ | 1.2927 | 1.01 | 14.00 | 0.004 |
| $10^{15}$ | 0.6000 | 2.17 | 15.00 | 0.337 |
| $10^{16}$ | 0.2785 | 4.68 | 16.00 | 0.670 |
| $10^{17}$ | 0.1293 | 10.08 | 17.00 | 1.004 |

A least-squares fit to the last two columns gives

$$
p = 0.3333 \quad\text{in}\quad r \propto M_0^{p} .
$$

The family was built with $p = 1/3$, so the measurement confirms the arithmetic
of the model and, in a real study, would be the *test* of constant-stress-drop
scaling. When a measured $p$ departs from $1/3$, the self-similar assumption has
failed and both $M_0$ and $f_c$ must be reported without it.

At $M_w = 4.60$ ($M_0 = 10^{16}\ \mathrm{N\,m}$, $r = 4.68\ \mathrm{km}$):

$$
\Delta\sigma = \frac{7}{16}\cdot\frac{10^{16}}{(4.68\times10^{3})^{3}}
= 0.0427\ \mathrm{MPa},
\qquad
\tau_a = \frac{\mu E_R}{M_0} = 0.0099\ \mathrm{MPa},
\qquad
\frac{\tau_a}{\Delta\sigma} = 0.23 .
$$

Both are constant across the family, and the ratio is the number a real study
would compare with other regions, because it does not depend on the model's
absolute calibration.

### Example 5 — the energy, and the check on the closed form

| $M_w$ | $E_R$ closed form (J) | $E_R$ Monte Carlo (J) | ratio |
|---|---|---|---|
| 2.60 | $3.0066\times10^{6}$ | $3.0142\times10^{6}$ | 1.0025 |
| 3.27 | $3.0066\times10^{7}$ | $3.0142\times10^{7}$ | 1.0025 |
| 3.93 | $3.0066\times10^{8}$ | $3.0142\times10^{8}$ | 1.0025 |
| 4.60 | $3.0066\times10^{9}$ | $3.0142\times10^{9}$ | 1.0025 |
| 5.27 | $3.0066\times10^{10}$ | $3.0142\times10^{10}$ | 1.0025 |

The Monte Carlo uses only 2000 directions, so an agreement of 0.25 per cent is
the accuracy of the sphere average, not a discrepancy in the physics. The
measured slopes are

$$
\frac{\mathrm{d}\log_{10}E_R}{\mathrm{d}M_w} = 1.500 ,
\qquad
\frac{\mathrm{d}\log_{10}E_R}{\mathrm{d}\log_{10}M_0} = 1.000 ,
$$

which is Section 3.3 reproduced numerically. The apparent stress is
$0.0099\ \mathrm{MPa}$ at every size: constant by construction, because both
$E_R$ and $M_0$ scale together. Its absolute value is a property of this
synthetic pulse shape and says nothing about any real earthquake; the *constancy*
and the *ratio* to the stress drop are the transferable statements.

### Example 6 — the band, by hand

Take $f_{\text{lp}} = 2\ \mathrm{Hz}$ and the $M_w = 3.93$ event with
$f_c = 0.6\ \mathrm{Hz}$, so $X = 2/0.6 = 3.333$:

$$
\frac{E(f<f_{\text{lp}})}{E_{\text{total}}}
= \frac{2}{\pi}\left[\arctan(3.333) - \frac{3.333}{1 + 11.111}\right]
= \frac{2}{\pi}\left[1.2793 - 0.2752\right]
= \frac{2}{\pi}(1.0041) = 0.6392 ,
$$

which is the printed $0.639236$. Across the family, the same 2 Hz low-pass keeps

| $M_w$ | $f_c$ (Hz) | fraction of $E_R$ kept | shortfall (factor) |
|---|---|---|---|
| 2.60 | 2.7850 | 0.0949 | 10.5 |
| 3.27 | 1.2927 | 0.3445 | 2.9 |
| 3.93 | 0.6000 | 0.6392 | 1.6 |
| 4.60 | 0.2785 | 0.8250 | 1.2 |
| 5.27 | 0.1293 | 0.9179 | 1.1 |

and the slope it produces is

$$
\frac{\mathrm{d}\log_{10}(E_R\ \text{low-passed})}{\mathrm{d}M_w} = 1.853
\quad\text{against}\quad 1.500\ \text{broadband}.
$$

The bias is size-dependent and, for this band, it is the **small** events that
are underestimated: the $M_w = 2.60$ event has its corner frequency above the
band edge and loses 90 per cent of its energy. Had the band edge been above every
corner frequency, the large events would have carried the bias instead. This is
the honest limit of every radiated-energy estimate: it is an integral over a
band, the band must be stated with the number, and a band-limited energy cannot
be compared with a broadband one without saying so.

## 6. The demonstration

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python energy_moment_calculations_demo.py
```

It integrates the double-couple pattern over the focal sphere, fits $(M_0, f_c)$
to attenuated spectra with and without the attenuation in the model, computes
$E_R$ in closed form and by Monte Carlo, and evaluates the band fraction
analytically and numerically.

Exercises:
[`exercises/06-energy-moment-calculations-exercises.md`](exercises/06-energy-moment-calculations-exercises.md)
and
[`exercises/06-energy-moment-calculations-solutions.md`](exercises/06-energy-moment-calculations-solutions.md).

> All models and data in this module are **SYNTHETIC**. The source family and the
> path are teaching values. The only borrowed constant in the demonstration is
> the Brune circular-crack coefficient 2.34, named where it is used.

## 7. Assumptions and regime of validity

1. **Self-similarity with constant stress drop.** Used in Section 3.3 to turn
   $E_R \propto M_0^2 f_c^{3}$ into $E_R \propto M_0$. It is testable, and
   Example 4 tests it.
2. **A point source with one corner frequency.** Real sources have a finite
   rupture duration and often a two-corner spectrum; the single-corner shape is
   the simplest model consistent with the data and the one whose arithmetic is
   exact.
3. **A single radiation coefficient for the whole sphere.** Real studies average
   over stations, which is a different (and noisier) operation than integrating
   over the focal sphere.
4. **A known attenuation.** Example 3 shows the cost of getting it wrong: 5 to
   15 per cent in moment and 40 to 60 per cent in corner frequency.
5. **The pulse shape $\tau = 1/(2\pi f_c)$.** The relation between the corner
   frequency and the duration is a modelling choice; a different choice changes
   the constant in $E_R$ but not the scaling.
6. **A stated bandwidth.** $E_R$ is defined over all frequencies; a measurement
   is defined over a band, and Example 6 measures the difference.
7. **The energy integral converges.** For the $f^{-2}$ displacement spectrum the
   acceleration spectrum is flat, so a raw integral over all frequencies would
   diverge; the pulse's exponential decay supplies the required high-frequency
   rolloff. Any real $E_R$ estimate therefore depends on the effective upper
   frequency limit, which must be stated.

## Mastery checkpoint

Without notes:

1. Derive $M_0 = 4\pi\rho\beta^{3}R\Omega_0/a$ and invert it for a measured
   plateau.
2. Show that $\int_0^{\infty}\big(1-s\big)^{2}e^{-2s}\mathrm{d}s = 1/4$ and use
   it to obtain $\int v^{2}\mathrm{d}t = A^{2}/(4\tau^{3})$.
3. Derive $E_R \propto M_0$ and hence the slope $3/2$ in $M_w$.
4. Explain in one sentence why an unmodelled $t^{*}$ biases $M_0$ high and
   $f_c$ low.
5. Compute the fraction of energy kept by a 2 Hz low-pass for an event with
   $f_c = 0.2\ \mathrm{Hz}$.
6. State two things that must accompany any quoted $E_R$.

## Common pitfalls

1. **Quoting $E_R$ without the band.** It is a band integral, not a property of
   the source alone.
2. **Confusing apparent stress with stress drop.** They differ by the ratio
   measured in Example 4 and have different definitions.
3. **Using a single station's amplitude as if $a$ were known.** The radiation
   coefficient is an average, worth 20 to 30 per cent.
4. **Assuming the exponent $3/2$ is a law.** It is a consequence of constant
   stress drop and is falsifiable.
5. **Forgetting that the energy integral needs a high-frequency cutoff.**
   Otherwise it diverges and the number is meaningless.
6. **Comparing an $M_w$ from a catalogue with an $E_R$ computed with a different
   attenuation model.** The two then disagree for bookkeeping reasons.

## Related modules

- [05 Magnitude Saturation and Why Moment Magnitude Is Preferred](05-magnitude-saturation.md).
- [06-03-05 Source Spectra, Corner Frequency and Stress Drop](../03-earthquake-sources/05-source-spectra.md).
- [06-03-06 Rupture Dynamics, Fracture Energy and Scaling Laws](../03-earthquake-sources/06-rupture-dynamics.md) —
  where fracture energy and the rest of the energy budget appear.
- [06-05-01 Measuring Q: Spectral Ratio, Rise Time, Multiple Methods](../05-attenuation-and-anelasticity/01-attenuation-measurement.md) —
  the $t^{*}$ whose omission Example 3 prices.
