---
id: 15-01-05
title: "Sea Level, Tides and Harmonic Analysis"
level: advanced
prereqs: ["02-08-03", "02-03-06", "15-01-02"]
tags: [oceanography, marine-geophysics, sea-level, tides, harmonic-analysis, aliasing, least-squares]
---

# Sea Level, Tides and Harmonic Analysis

> **All models and data in this module are SYNTHETIC.** The tide record analysed
> here is generated from chosen amplitudes and phases with synthetic noise; it is
> not a tide-gauge record and no station is named. The astronomical constants
> used to derive the equilibrium tide are standard values and are stated with
> their units. The constituent periods are conventional astronomical values.

Sea level is the most-measured quantity in oceanography and one of the hardest to
interpret. A tide gauge records a single number per unit time, and that number is
the sum of a periodic astronomical tide, a slow trend, a storm surge, a seasonal
cycle, and the vertical motion of the land the gauge is bolted to. Separating
them is a linear inverse problem, and like every linear inverse problem it has a
resolution limit that can be computed before a single datum is collected.

That is the organising idea of this lesson. **Harmonic analysis is least squares
on a designed matrix**, and the design matrix's conditioning answers the
practical questions: how long must a record be to separate two constituents, what
does a gap do, and why does a once-daily reading of a semidiurnal tide produce a
fictitious fortnightly oscillation?

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the equilibrium tide amplitude $\zeta_{\max} = GMR^{2}/(gd^{3})$
   from the degree-2 tide-generating potential, and **compute** it for a stated
   body and distance with units.
2. **Formulate** harmonic analysis as least squares on a design matrix of
   $\cos(\omega_j t)$ and $\sin(\omega_j t)$ columns, and **obtain** both the
   coefficients and their formal covariance from a stated noise variance.
3. **State and apply** the Rayleigh criterion $T > 1/|f_1-f_2|$, and **quantify**
   what a record shorter than the criterion does to two nearby constituents.
4. **Diagnose** a nearly singular design from its condition number, and
   **explain** why a small formal error from a badly conditioned fit is not a
   licence to quote the number.
5. **Compute** the alias of a tidal constituent for a stated sampling interval,
   and **show** why a once-daily gauge reading turns the semidiurnal tide into a
   fortnightly signal.
6. **Estimate** a sea-level trend and its formal uncertainty, and **state** what
   governs the uncertainty at a given record length.
7. **Separate** in writing what the record measures (a sum of terms, at one
   place) from what a sea-level change claim asserts (a global average).

## Prerequisites

- [02-08-03 Spherical Harmonics and Multipole Expansions](../../02-physics/08-potential-theory/03-spherical-harmonics.md) —
  the degree-2 Legendre term from which the tidal potential is built.
- [02-03-06 Superposition and Interference](../../02-physics/03-oscillations-and-waves/06-superposition-interference.md) —
  why a sum of sinusoids is the natural model for a tide record.
- [15-01-02 Wind-Driven Circulation, Ekman Transport and Gyres](02-wind-driven-circulation.md) —
  where the sea-surface height a gauge sees also drives a current.

## 1. What a tide gauge measures

Write the measured sea level at time $t$ as a sum of terms with different physics
and different timescales:

$$\eta(t) = \underbrace{\bar\eta}_{\text{datum}} +
\underbrace{\sum_j A_j\cos(\omega_j t - \phi_j)}_{\text{astronomical tide}} +
\underbrace{b\,t}_{\text{trend}} + \underbrace{S(t)}_{\text{surge, weather}} +
\underbrace{\Delta u(t)}_{\text{land motion}} + \underbrace{n(t)}_{\text{noise}} .$$

Each term needs a different treatment, and the whole of this lesson is about the
second term and its interaction with the third.

Two structural points before any arithmetic.

- **The tidal frequencies are known in advance.** They come from the orbital
  mechanics of the Earth–Moon–Sun system, so $\omega_j$ are *inputs*, not fitted
  parameters. Only amplitudes and phases are estimated. This is what makes
  harmonic analysis a well-posed (though possibly ill-conditioned) linear problem
  rather than a spectral estimation problem.
- **The datum is not known.** A tide gauge measures relative to a local bench
  mark, whose own vertical motion contaminates any trend. The
  order-one statement "sea level is rising at $x$" therefore has a land-motion
  term inside it that no amount of tide-gauge data can remove; that is the
  subject of
  [Module 15-06](../06-sea-level-change-marine/README.md), and it is mentioned
  here only so the trend in Section 6 is not over-read.

## 2. The equilibrium tide

### 2.1 Derivation

The gravitational potential of a distant body of mass $M$ at distance $d$,
expanded about the Earth's centre in powers of $R/d$ (Legendre expansion, as in
[02-08-03](../../02-physics/08-potential-theory/03-spherical-harmonics.md)):

$$\Omega(\psi) = -\frac{GM}{d}\sum_{n\ge0}\left(\frac{R}{d}\right)^{n}
P_n(\cos\psi),$$

where $\psi$ is the angle from the sub-body direction. The $n=0$ term is a
constant and the $n=1$ term is the orbital acceleration, which is exactly the
acceleration the Earth already has — both are removed by the definition of a
*local* horizontal and vertical at a point. The tide-generating part is:

$$\Omega_2 = -\frac{GMR^{2}}{d^{3}}P_2(\cos\psi),
\qquad P_2(\cos\psi) = \frac{3\cos^{2}\psi - 1}{2}.$$

An ocean that could instantly adjust to equipotential would stand at the
**equilibrium tide** height

$$\zeta(\psi) = -\frac{\Omega_2}{g} = \frac{GMR^{2}}{gd^{3}}P_2(\cos\psi),$$

whose maximum is at the sub-body point ($\psi = 0$, $P_2 = 1$):

$$\boxed{\;\zeta_{\max} = \frac{GMR^{2}}{gd^{3}}.\;}$$

### 2.2 Numerical evaluation

With $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$R = 6.371\times10^{6}\ \mathrm{m}$, $g = 9.81\ \mathrm{m\,s^{-2}}$:

| body | $M$ (kg) | $d$ (m) | $\zeta_{\max}$ (m) | peak-to-trough (m) |
|---|---|---|---|---|
| Moon | $7.342\times10^{22}$ | $3.844\times10^{8}$ | 0.3569 | 0.7139 |
| Sun | $1.989\times10^{30}$ | $1.496\times10^{11}$ | 0.1640 | 0.3281 |

The solar-to-lunar ratio is $0.1640/0.3569 = 0.4596$. **The Moon's tide is more
than twice the Sun's**, even though the Sun is $2.7\times10^{7}$ times more
massive, because the tide falls off as $d^{-3}$ rather than $d^{-2}$: the Sun's
greater distance costs it a factor of $(3.844\times10^{8}/1.496\times10^{11})^{-3}
= 5.9\times10^{4}$ against a mass advantage of only $2.7\times10^{7}$.

If the two bulges were perfectly aligned the total range would be about
$1.042\ \mathrm{m}$. They are not: the lunar and solar bulges drift in and out of
alignment over the spring–neap cycle, which Section 4 turns into a number.

### 2.3 Why the observed tide is much larger

$\zeta_{\max} = 0.36\ \mathrm{m}$ is a *forcing* amplitude, not a sea level. An
ocean basin responds to a forcing whose frequency is close to one of its natural
modes, and coastal and estuarine geometry amplifies the response further. Observed
ranges exceed the equilibrium range by factors of two to ten and more. The
equilibrium tide is therefore useful as a scale and as the source of the
constituent frequencies; it is not a prediction of what a gauge will see, and
quoting it as one is a common error.

## 3. Harmonic analysis as least squares

### 3.1 The model and the design matrix

Write the model for $J$ constituents as a linear system. Using the identity
$A\cos(\omega t - \phi) = a\cos(\omega t) + b\sin(\omega t)$ with
$a = A\cos\phi$, $b = A\sin\phi$:

$$\eta(t_k) = a_0 + \sum_{j=1}^{J}\left[a_j\cos(\omega_j t_k)
+ b_j\sin(\omega_j t_k)\right] + n(t_k),$$

or in matrix form $\mathbf{d} = \mathbf{G}\mathbf{m} + \mathbf{n}$, with
$2J+1$ parameters. The least-squares solution and its covariance are

$$\hat{\mathbf{m}} = (\mathbf{G}^{\mathsf{T}}\mathbf{G})^{-1}
\mathbf{G}^{\mathsf{T}}\mathbf{d},
\qquad
\mathrm{Cov}(\hat{\mathbf{m}}) = \sigma^{2}(\mathbf{G}^{\mathsf{T}}
\mathbf{G})^{-1},$$

with $\sigma^{2}$ estimated from the residual variance. Amplitude and phase are
then $A_j = \sqrt{a_j^{2}+b_j^{2}}$ and $\phi_j = \arctan(b_j/a_j)$.

### 3.2 The demonstration's experiment

Four constituents with **chosen** amplitudes and phases:

| name | period (h) | $\omega$ (rad s$^{-1}$) | amplitude (m) | phase (deg) | deg hour$^{-1}$ |
|---|---|---|---|---|---|
| M2 | 12.4206012 | $1.405189\times10^{-4}$ | 1.20 | 30.0 | 28.9841 |
| S2 | 12.0000000 | $1.454441\times10^{-4}$ | 0.40 | 60.0 | 30.0000 |
| K1 | 23.9344721 | $7.292115\times10^{-5}$ | 0.15 | 200.0 | 15.0411 |
| O1 | 25.8193417 | $6.759774\times10^{-5}$ | 0.10 | 150.0 | 13.9430 |

A 60-day record sampled every 30 min (2880 points) receives Gaussian noise of
$\sigma = 0.05\ \mathrm{m}$; the signal range is $3.521\ \mathrm{m}$, so the M2
amplitude has a signal-to-noise ratio of $24$. The least-squares fit returns

| name | true $A$ (m) | fitted $A$ (m) | error (m) | coefficient $\sigma$ (m) | fitted phase (deg) |
|---|---|---|---|---|---|
| M2 | 1.200 | 1.201 | $+0.001$ | 0.0013 | 29.9 |
| S2 | 0.400 | 0.400 | $+0.000$ | 0.0013 | 60.0 |
| K1 | 0.150 | 0.151 | $+0.001$ | 0.0013 | 200.7 |
| O1 | 0.100 | 0.098 | $-0.002$ | 0.0013 | 150.2 |

The residual rms is $0.0497\ \mathrm{m}$ against the injected $0.050\ \mathrm{m}$,
and the design matrix has condition number $1.466$.

Two observations worth stating explicitly.

- **All four coefficients carry the same formal error** ($0.0013\ \mathrm{m}$),
  because at this record length the design is nearly orthogonal. With enough
  data every constituent is measured to the same precision, and it is the
  *small* constituents — O1 at $0.10\ \mathrm{m}$ — whose relative error is
  worst. Precision is uniform; signal-to-noise is not.
- **The condition number near 1 is the statement that the data are being asked
  independent questions.** It is the diagnostic that will fail in Section 5, and
  it must be reported with any fitted tide.

The **form ratio** $(K1+O1)/(M2+S2) = 0.25/1.60 = 0.1562$ summarises the record
as semidiurnal-dominated. The boundaries between named tidal classes are
conventions; the ratio is the measurement, and it should be quoted in preference
to the class name.

## 4. The Rayleigh criterion

Two constituents of frequencies $f_1$ and $f_2$ are separable only if the record
is long enough for them to complete at least one beat:

$$\boxed{\;T > \frac{1}{|f_1 - f_2|}.\;}$$

For the semidiurnal pair:

$$\Delta f = 30.0000 - 28.9841 = 1.0159\ \mathrm{deg\,hour^{-1}}
= \frac{1.0159}{360} = 2.822\times10^{-3}\ \mathrm{cycles\,hour^{-1}},$$

$$T > \frac{1}{2.822\times10^{-3}} = 354.4\ \mathrm{h} = 14.77\ \mathrm{days}.$$

That is the **spring–neap period**: the same physics that makes the tides wax and
wane makes M2 and S2 separable, and the minimum record is exactly one cycle of
the phenomenon.

Now shorten the record and watch the design degenerate. Same noise realisation,
same constituents:

| record (days) | M2 fitted (m) | M2 error (m) | M2 $\sigma$ (m) | S2 fitted (m) | S2 error (m) | S2 $\sigma$ (m) | cond$(\mathbf{G})$ |
|---|---|---|---|---|---|---|---|
| 1 | 1.238 | $+0.038$ | 1.4515 | 1.417 | $+1.017$ | 1.2996 | 834.7 |
| 2 | 1.214 | $+0.014$ | 0.0309 | 0.401 | $+0.001$ | 0.0306 | 9.21 |
| 5 | 1.209 | $+0.009$ | 0.0080 | 0.401 | $+0.001$ | 0.0078 | 3.48 |
| 10 | 1.204 | $+0.004$ | 0.0036 | 0.404 | $+0.004$ | 0.0035 | 1.85 |
| 15 | 1.200 | $+0.000$ | 0.0026 | 0.403 | $+0.003$ | 0.0026 | 1.48 |
| 30 | 1.199 | $-0.001$ | 0.0018 | 0.402 | $+0.002$ | 0.0018 | 1.48 |
| 60 | 1.201 | $+0.001$ | 0.0013 | 0.400 | $+0.000$ | 0.0013 | 1.47 |

Read the columns together. At one day the **S2 error is $+1.017\ \mathrm{m}$
against a true amplitude of $0.400\ \mathrm{m}$** — the fit has handed S2 the
signal that belongs to M2, which is why M2 is $+0.038\ \mathrm{m}$ high and S2 is
wrong by $254\,\%$. The two constituents **trade off**: a single long sinusoid of
nearly the M2 frequency can be fitted by any mixture of M2 and S2. The condition
number, 834.7, announces exactly that, and the formal $\sigma$ on S2
($1.30\ \mathrm{m}$) is large enough to hint at it — but a formal error computed
from a nearly singular design is a *weak* warning, because it is derived from the
same design that cannot separate the two.

**Practical rule:** report the condition number whenever you report fitted tidal
amplitudes, and do not quote a constituent whose record is shorter than its
Rayleigh period against the nearest constituent.

## 5. Aliasing: what a poor sampling interval does

Sampling at interval $\Delta t$ gives sample frequency $f_s = 1/\Delta t$, and any
constituent at frequency $f$ appears at the **alias frequency**

$$f_{\text{alias}} = f - \mathrm{round}\!\left(\frac{f}{f_s}\right)f_s .$$

For a once-per-day reading, $f_s = 1/24 = 0.041667\ \mathrm{cycles\,hour^{-1}}$:

| constituent | $f$ (cycles h$^{-1}$) | alias $f$ (cycles h$^{-1}$) | alias period (h) |
|---|---|---|---|
| M2 | 0.080511 | $-0.002822$ | 354.37 |
| S2 | 0.083333 | 0.000000 | absorbed into the mean |
| K1 | 0.041781 | $+0.000114$ | 8766.15 |
| O1 | 0.038731 | $-0.002936$ | 340.60 |

Two failures of a different kind appear here.

- **S2 has a period of exactly 24 h**, so a once-daily reading samples it at
  precisely one cycle per sample: it is **aliased onto zero frequency and absorbed
  into the mean sea level**. Its amplitude is unrecoverable, and it contaminates
  the estimate of the datum.
- **M2 aliases to a period of $354.37\ \mathrm{h} = 14.77$ days** — numerically
  identical to the M2–S2 beat period. A fictitious fortnightly oscillation in a
  short record is therefore *indistinguishable from a genuine spring–neap cycle*.
  This is the sharpest single argument for sampling a tide gauge at a fraction of
  an hour, and it is the reason that historical once-daily readings are treated
  with care.

Aliasing is not a filtering problem to be fixed afterwards; the information is
not in the data. The demonstration's K1 alias $8766.15\ \mathrm{h} \approx 1$ year
is a third example: a diurnal constituent read once a day masquerades as an annual
cycle, where it competes directly with the seasonal signal and the trend.

## 6. Trends and their formal uncertainty

Fit a datum, a linear trend and a seasonal cycle to synthetic monthly means:

$$\eta(t) = a_0 + b\,t + c\cos(2\pi t) + s\sin(2\pi t).$$

With 20 years of data, a true trend of $3.00\ \mathrm{mm\,yr^{-1}}$ and Gaussian
noise of $\sigma = 20\ \mathrm{mm}$, the fitted trend is

$$\hat b = 3.147 \pm 0.212\ \mathrm{mm\,yr^{-1}} \quad\text{(formal 1-}\sigma),$$

with a fitted seasonal amplitude of $58.78\ \mathrm{mm}$ (true $60\ \mathrm{mm}$)
and a residual rms of $18.83\ \mathrm{mm}$. The closed form

$$\mathrm{Var}(\hat b) = \frac{\sigma^{2}}{\sum_k (t_k - \bar t)^{2}}$$

gives $0.2236\ \mathrm{mm\,yr^{-1}}$, in agreement with the least-squares
$0.2125$ to the level expected (they differ because the residual variance is
estimated, not known).

Shortening the record moves the answer far more than it moves the error bar's
*credibility*:

| years | fitted trend (mm yr$^{-1}$) | formal $\sigma$ (mm yr$^{-1}$) |
|---|---|---|
| 2 | $-3.774$ | 8.094 |
| 5 | $2.828$ | 1.757 |
| 10 | $3.608$ | 0.638 |
| 20 | $3.002$ | 0.222 |

The two-year record's estimate is the *wrong sign*. Its formal error bar
(8.1 mm yr$^{-1}$) is honest — the truth is within it — but a figure of
$8\ \mathrm{mm\,yr^{-1}}$ on a $3\ \mathrm{mm\,yr^{-1}}$ signal is an admission
that the record cannot answer the question, and it is the reason trend claims
are made from decades of data, not years.

**The general result** is that the trend uncertainty scales approximately as
$N^{-3/2}$ for $N$ equally spaced samples, so quadrupling the record length
quarters the error: this is why a 20-year record is not merely twice as good as a
5-year record but roughly eight times as good.

## 7. Assumptions and regime of validity

1. **Known frequencies, unknown amplitude and phase.** True for astronomical
   tides; not true for surge or for seiche, whose periods are site-specific.
2. **Stationary amplitudes.** Real constituents modulate over the 18.6-year nodal
   cycle and over longer astronomical cycles. Fitting a single amplitude over
   several decades silently averages that modulation.
3. **Additive Gaussian noise with constant variance.** Real sea-level noise is
   correlated (surge has multi-day memory), which makes the formal covariance
   optimistic. The honest statement is that the errors are *at least* this large.
4. **Linear superposition of constituents.** The astronomical forcing is
   essentially linear at these amplitudes; shallow-water tidal harmonics
   (M4, M6) are generated by nonlinearity and must be added as separate
   constituents, not explained as measurement noise.
5. **No datum problem.** The synthetic record has a known datum and no land
   motion. A real trend contains both.
6. **Rayleigh criterion satisfied.** Every constituent quoted in Section 3 has a
   record longer than its separation period from its nearest neighbour;
   Section 4 shows what happens otherwise.

## 8. Worked examples

### Example 1 — the equilibrium tide at two distances

For a body with $GM = 4.900\times10^{12}\ \mathrm{m^{3}\,s^{-2}}$ at two chosen
distances:

$$d = 3.63\times10^{8}\ \mathrm{m}: \quad
\zeta_{\max} = \frac{4.900\times10^{12}(6.371\times10^{6})^{2}}
{9.81(3.63\times10^{8})^{3}}
= \frac{1.9889\times10^{26}}{4.692\times10^{26}} = 0.4239\ \mathrm{m},$$

$$d = 4.06\times10^{8}\ \mathrm{m}: \quad
\zeta_{\max} = \frac{1.9889\times10^{26}}{6.565\times10^{26}} = 0.3030\ \mathrm{m}.$$

The ratio is $0.4239/0.3030 = 1.399$, i.e. a $40\,\%$ variation in the tide-
generating amplitude over a $12\,\%$ variation in distance — the $d^{-3}$ law
again, and the reason perigean spring tides are a real phenomenon rather than a
popular myth. Note how sensitive the answer is: a $1\,\%$ error in $d$ is a
$3\,\%$ error in $\zeta$.

### Example 2 — reading an amplitude from the normal equations

For a record that is an integer number of cycles of every constituent and
uniformly sampled, $\frac{1}{N}\mathbf{G}^{\mathsf{T}}\mathbf{G} \to
\tfrac12\mathbf{I}$ for the oscillatory block, so the cosine and sine
coefficients of constituent $j$ are simply

$$a_j = \frac{2}{N}\sum_k d_k\cos(\omega_j t_k), \qquad
b_j = \frac{2}{N}\sum_k d_k\sin(\omega_j t_k).$$

The demonstration tests exactly this: a 10-day M2-only signal is fitted and
returns an amplitude of $1.200000\ \mathrm{m}$ against a true $1.200000\
\mathrm{m}$, and a phase of $30.0000^\circ$ against $30.0000^\circ$, with a
residual rms of $6.8\times10^{-15}\ \mathrm{m}$. **The agreement is not a
coincidence and not a validation:** the estimator is the exact inverse of the
generator when the basis is orthogonal, so the test verifies the code and says
nothing about the model.

### Example 3 — the trend error, by hand

For $N = 240$ monthly samples with $t_k = k/12$ years and $\sigma = 20\
\mathrm{mm}$:

$$\sum_k (t_k-\bar t)^{2} = \frac{N(N^{2}-1)}{12}\left(\frac{1}{12}\right)^{2}
= \frac{240(57599)}{12}\cdot\frac{1}{144} = 8000\ \mathrm{yr^{2}},$$

$$\mathrm{Var}(\hat b) = \frac{(0.020)^{2}}{8000} = 5.0\times10^{-8}
\ \mathrm{m^{2}\,yr^{-2}} \;\Rightarrow\;
\sigma_{\hat b} = 2.24\times10^{-4}\ \mathrm{m\,yr^{-1}} = 0.224\
\mathrm{mm\,yr^{-1}}.$$

That is the number the least-squares covariance produced ($0.212$), and the
closed form shows *why*: the denominator grows as $N^{3}$, so the trend error
falls as $N^{-3/2}$.

## 9. Python demonstration

`code/sea_level_tides_demo.py` prints all the above with units. It:

1. derives the equilibrium tide amplitude for the Moon and the Sun and their
   ratio, and states the total range if the bulges were aligned;
2. tabulates the four constituents, the M2–S2 separation and the spring–neap
   period;
3. fits the record by least squares, reporting amplitudes, errors, phases, the
   coefficient covariance, the condition number and the form ratio;
4. shortens the record from 1 to 60 days and tabulates the damage;
5. computes the alias of each constituent for a once-daily sampling interval;
6. fits a synthetic trend at four record lengths with formal errors, and checks
   the trend error against the closed form;
7. verifies the fit: residual rms against the injected noise, orthogonality of
   the residual to every column of the design, and an exact analytic case.

Run it with

```bash
cd 15-oceanography-marine/01-physical-oceanography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_level_tides_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/05-sea-level-and-tides-exercises.md`](exercises/05-sea-level-and-tides-exercises.md)
and
[`exercises/05-sea-level-and-tides-solutions.md`](exercises/05-sea-level-and-tides-solutions.md).

- ★ Compute $\zeta_{\max}$ for a body with twice the Moon's mass at the Moon's
  distance, and state the scaling law you used.
- ★★ Derive the Rayleigh period for K1 against O1 and state whether a 20-day
  record can separate them.
- ★★ Compute the alias period of a semidiurnal constituent of period 12.66 h
  sampled every 6 h.
- ★★★ Design a tide-gauge deployment and analysis that would determine a
  $2\ \mathrm{mm\,yr^{-1}}$ trend to $\pm 1\ \mathrm{mm\,yr^{-1}}$, stating the
  record length, sampling, and the terms you cannot control.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use
$G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$R = 6.371\times10^{6}\ \mathrm{m}$, $g = 9.81\ \mathrm{m\,s^{-2}}$.

> A synthetic station records a tide dominated by two constituents: M2
> ($12.4206\ \mathrm{h}$) and S2 ($12.0000\ \mathrm{h}$).
> **(a)** Compute the Rayleigh period for separating M2 from S2, in days.
> **(b)** A 10-day record is fitted and returns M2 $= 1.31\ \mathrm{m}$,
> S2 $= 0.28\ \mathrm{m}$. Using the demonstration's 10-day row
> (M2 $= 1.204$, S2 $= 0.404$, condition number 1.85) as a reference, state
> whether the quoted pair is credible and why.
> **(c)** The same record is sampled once per day. Compute the alias period of
> M2 and state what a naive user would report.
> **(d)** Compute $\zeta_{\max}$ for the Moon and state in one sentence why the
> gauge's observed range can be much larger.

A worked version of (a)–(d) is in the lesson-05
[solutions](exercises/05-sea-level-and-tides-solutions.md).

## Common pitfalls

1. **Quoting a tidal constituent fitted from a record shorter than its Rayleigh
   period.** Section 4: at one day, S2 came out $254\,\%$ wrong.
2. **Ignoring the condition number.** A small formal error from a nearly singular
   design is not evidence of a good estimate; report cond$(\mathbf{G})$ with the
   amplitudes.
3. **Once-daily sampling.** M2 aliases to 14.77 days and S2 aliases onto the
   mean. The information is lost, not degraded.
4. **Reading the equilibrium tide as a prediction.** It is the forcing amplitude
   ($0.36\ \mathrm{m}$ for the Moon); basin and coastal response multiply it.
5. **Treating a formal trend error as the whole uncertainty.** Correlated surge
   noise makes it optimistic, and land motion is not in it at all.
6. **Confusing a class name with a measurement.** "Semidiurnal" is a convention;
   the form ratio 0.1562 is the number.
7. **Fitting a single amplitude over decades.** Constituent amplitudes modulate
   over the 18.6-year nodal cycle.

## Related modules

- [01 Seawater Properties: Temperature, Salinity, Density](01-seawater-properties.md) —
  the density whose changes also appear in a sea-level record.
- [04 Internal Waves, Tides and Mixing](04-internal-waves-and-tides.md) —
  what the tide does to the stratified interior once it leaves the coast.
- [02 Wind-Driven Circulation, Ekman Transport and Gyres](02-wind-driven-circulation.md) —
  the sea-surface height's other role, as the pressure field for geostrophy.
- [Module 15-06 Sea Level Change and Marine Records](../06-sea-level-change-marine/README.md) —
  the trend, the datum and the land motion this lesson deliberately leaves alone.
- [07-06-01 Solid Earth Tides](../../07-gravity-geodesy/06-earth-tides-and-rotation/01-solid-earth-tides.md) —
  the same potential acting on the solid Earth, which shares the ocean's
  Love-number response.
- [20-08-02 Spectral Analysis of Tides and Earth Signals](../../20-signal-processing/08-timeseries-analysis-geophysics/02-spectral-analysis-tides.md) —
  the frequency-domain view of the same estimation problem.

## Self-assessment checklist

- [ ] I can derive and evaluate the equilibrium tide amplitude with units.
- [ ] I can set up the least-squares design and its covariance.
- [ ] I can state and apply the Rayleigh criterion.
- [ ] I can diagnose a nearly singular design from its condition number.
- [ ] I can compute an alias frequency and period for a stated sampling.
- [ ] I can estimate a trend's formal error from a closed form.
- [ ] I can separate "what the gauge measures" from "what the claim asserts".
