---
id: 10-04-03
title: "Near-Surface Refraction for Static Corrections"
level: graduate
prereqs: ["06-10-02", "06-09-02", "10-04-01"]
tags: [gpr, near-surface, geotechnical, statics, refraction, weathering, seismic-reflection]
---

# Near-Surface Refraction for Static Corrections

**All models and data in this module are SYNTHETIC.** The velocities, weathering
depths, elevations, datum, replacement velocity and timing errors below are chosen
teaching values. No survey, line, datum or processing job is described from
measurement. Physical constants are labelled as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the weathering-layer depth from an intercept time, and **quantify**
   how sensitive that depth is to the overburden velocity it was computed with.
2. **Derive** the weathering + replacement (datum) static and **apply** it to a
   line of stations with varying elevation.
3. **Derive** the stack response to a constant static shift, $\cos(2\pi f\Delta t)$,
   and to random static shifts, $\exp(-2\pi^2f^2\sigma_t^2)$, and **verify** the
   second against a direct stack.
4. **Derive** the surface-consistent statics decomposition $T_{ij}=s_i+r_j$,
   **prove** that its only null direction is a constant, and **state** why the
   absolute level of the static profile must come from outside the data.
5. **Explain** the long-wavelength statics problem as a trade with the subsurface
   model rather than a null space, and **compute** the depth error and apparent dip
   that a $10\ \mathrm{ms}$ static error produces.
6. **Quantify** the difference between a bias in the depth of the surface (a
   structure error) and a loss of high frequencies in the stack (a resolution
   error) caused by the same velocity error.
7. **State** what a refraction-statics solution can and cannot deliver, and which
   external constraint fixes what it cannot.

## Prerequisites

- [06-10-02 Delay-Time (Plus-Minus) Methods and Depth Estimation](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md)
  — the intercept-time/plus-minus depth solution whose sensitivity this lesson
  reuses.
- [06-09-02 The Reflection Processing Flow](../../06-seismology/09-reflection-seismology/02-processing-flow.md)
  — where statics sit in the sequence, and what they are for.
- [10-04-01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](01-spt-cpt-crosshole.md)
  — the borehole measurements that provide the ground truth for a near-surface
  velocity model.

## 1. Intuition: a correction that invents structure

A reflection survey measures times. The near surface — the weathered layer, the
fill, the topography — adds a *static* time shift to every trace, different at
every source and receiver position. If it is not removed, the stack is degraded and
the section acquires structure that does not exist. Removing it is called a static
correction, and it is usually the first processing step that touches the physics of
the site rather than the physics of the wave.

Two facts make statics both necessary and dangerous:

- **Necessary**, because the stack works by summing traces that should share the
  same reflection time. A shift of a few milliseconds costs a large fraction of the
  amplitude at the frequencies that carry resolution (Section 3.3).
- **Dangerous**, because a static shift and a *depth* change move a reflection in
  the same direction. Any error in the static correction appears in the final
  section as structure. The demonstration's arithmetic: a $10\ \mathrm{ms}$ static
  error on a reflector at $2.0\ \mathrm{s}$ with a stacking velocity of
  $2500\ \mathrm{m\,s^{-1}}$ becomes $12.5\ \mathrm{m}$ of apparent depth, an
  apparent dip of $0.298^\circ$ over $2.4\ \mathrm{km}$ — a perfectly plausible
  structural feature.

This lesson is therefore about the *error budget* of a correction, not about the
derivation of a refraction depth, which is
[06-10-02](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md)'s
subject. What is added here is what happens when the correction is applied to a
whole line: what cancels, what cannot be determined, and what the residual does to
the image.

## 2. Precise definitions

| Term | Meaning | Unit |
|---|---|---|
| weathering layer | the low-velocity zone between the surface and the first competent refractor | — |
| $v_w$ | weathering velocity | m/s |
| $v_r$ | refractor velocity | m/s |
| $v_{\mathrm{rep}}$ | replacement velocity used below the datum | m/s |
| datum | the flat surface to which all traces are corrected | m (elevation) |
| $t_i$ | intercept time of the refraction travel-time curve | ms |
| field static | the one-way time from the surface to the datum, in the replacement medium | ms |
| residual static | the static left after the refraction solution | ms |
| surface-consistent | the assumption that the static separates into a source term and a receiver term | — |

**A field static** corrects a trace to the datum by replacing whatever is above it
with the replacement medium. **A residual static** is what remains after the field
statics are applied, and it is estimated by maximising the stack — an
amplitude-based, and therefore non-unique, step.

## 3. Derivations

### 3.1 The weathering depth, and its true sensitivity

For a two-layer ground with a horizontal interface, the head-wave arrival at offset
$x$ is

$$t(x) = \frac{x}{v_r} + \frac{2z\cos\theta_c}{v_w},
\qquad \sin\theta_c = \frac{v_w}{v_r},$$

so the intercept time $t_i = 2z\cos\theta_c/v_w$ can be rewritten as

$$z = \frac{t_i}{2\sqrt{1/v_w^{2} - 1/v_r^{2}}}.$$

*Numerical check.* $v_w = 600$, $v_r = 1800\ \mathrm{m\,s^{-1}}$,
$t_i = 12.0\ \mathrm{ms}$:
$\sqrt{1/600^2 - 1/1800^2} = \sqrt{2.7778\times10^{-6} -
3.0864\times10^{-7}} = \sqrt{2.4691\times10^{-6}} = 1.57144\times10^{-3}$,
so $z = 0.012/(2 \times 1.57144\times10^{-3}) = 3.818\ \mathrm{m}$.

**The sensitivity that decides the error budget** is to $v_w$, not $z$:

| $v_w$ (m/s) | $z$ (m) | change |
|---|---|---|
| $540$ | $3.396$ | $-11.05\%$ |
| $570$ | $3.606$ | $-5.57\%$ |
| $600$ | $3.818$ | — |
| $630$ | $4.035$ | $+5.68\%$ |
| $660$ | $4.256$ | $+11.47\%$ |

The central-difference derivative is
$\mathrm{d}z/\mathrm{d}v_w = 7.16\times10^{-3}\ \mathrm{m}$ per
$(\mathrm{m\,s^{-1}})$, i.e. **about $1.1\%$ of the depth for every $1\%$ of the
weathering velocity**. That velocity is obtained from the same picks that give the
depth, so the two errors are correlated, and the depth is only as good as the
two-layer fit — which
[06-10-02](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md)
shows can be catastrophically wrong in the presence of a low-velocity layer.

### 3.2 The datum static

For a station on the surface, with the weathering layer of thickness $z_w$ and
velocity $v_w$ over a refractor, and the datum at depth $d$ below that station's
surface (with $d$ negative if the station lies *below* the datum), the correction
that moves the trace to the datum in a medium of replacement velocity
$v_{\mathrm{rep}}$ is

$$t_{\mathrm{stat}} = \frac{z_w}{v_w} - \frac{z_w-d}{v_{\mathrm{rep}}}.$$

The term in brackets is the one-way time from the datum down to the base of the
weathering at the replacement velocity. Two limits are worth naming:

- $z_w = 0$ (no weathering, or a station on rock): $t_{\mathrm{stat}} = d/v_{\mathrm{rep}}$,
  the pure elevation static;
- $d = z_w$ (the datum at the base of the weathering): $t_{\mathrm{stat}} = 0$, as
  it must be.

*Measured table* (SYNTHETIC line, $v_w = 600$, $v_{\mathrm{rep}} = 2500\
\mathrm{m\,s^{-1}}$, datum elevation $120\ \mathrm{m}$):

| station | elevation (m) | $z_w$ (m) | $d$ (m) | $t_{\mathrm{stat}}$ (ms) |
|---|---|---|---|---|
| 0 | $124.0$ | $3.80$ | $4.0$ | $6.413$ |
| 1 | $122.5$ | $4.10$ | $2.5$ | $6.193$ |
| 2 | $120.5$ | $4.40$ | $0.5$ | $5.773$ |
| 3 | $118.0$ | $4.00$ | $-2.0$ | $4.267$ |
| 4 | $115.5$ | $3.60$ | $-4.5$ | $2.760$ |

The static profile spans $3.65\ \mathrm{ms}$ across five stations — and a station
below the datum gets a small correction rather than a negative one, because the
weathering term still dominates it. Both effects come out of one formula, which is
the point of writing it as a difference of two times rather than as a table of
rules.

### 3.3 What a static error does to a stack

Sum $N$ traces whose reflection wavelet is the same but whose arrival times differ
by the statics. At frequency $f$ the stack amplitude relative to a perfectly aligned
stack is

$$A(f) = \left|\frac{1}{N}\sum_{k=1}^{N}e^{i2\pi f\,\delta t_k}\right|.$$

- **A constant shift** $\delta t$ for every trace: $A = |e^{i2\pi f\delta t}|$ in
  phase but $\cos(2\pi f\delta t)$ for a real, zero-phase wavelet, i.e.
  $A = \cos(2\pi f\delta t)$ — the sum of cosines.
- **Independent shifts** $\delta t_k$ with standard deviation $\sigma_t$: the mean
  of $e^{i2\pi f\delta t}$ is the characteristic function of the shift
  distribution, which for a Gaussian is

$$A(f) = \exp\!\left(-2\pi^{2}f^{2}\sigma_t^{2}\right).$$

Both expressions are exact; the second needs the shifts to be independent, which is
a statement about the survey, not about the arithmetic.

*Measured verification.* The demonstration stacks $500$ synthetic Ricker wavelets
at $40\ \mathrm{Hz}$ with Gaussian static shifts, measures the amplitude spectrum at
the nearest FFT bin ($40.283\ \mathrm{Hz}$) and compares it with the Gaussian factor
evaluated at the realised rms of the same draw:

| $\sigma_t$ (ms) | $\exp(-2\pi^2f^2\sigma_t^2)$ | measured spectral ratio | ratio |
|---|---|---|---|
| $0.0$ | $1.0000$ | $1.0000$ | $1.000$ |
| $2.0$ | $0.8768$ | $0.8746$ | $0.997$ |
| $4.0$ | $0.6188$ | $0.6121$ | $0.989$ |
| $6.0$ | $0.3689$ | $0.3485$ | $0.945$ |
| $8.0$ | $0.1220$ | $0.1343$ | $1.101$ |

Agreement within $1\%$ for $\sigma_t \le 4\ \mathrm{ms}$ and within $10\%$ beyond
it, the residual being the finite number of draws and the interpolation used to
apply the shifts.

**The consequence for a survey, in numbers** (the demonstration's cosine table):

| $\Delta t$ (ms) | $A$ at $20\ \mathrm{Hz}$ | at $40\ \mathrm{Hz}$ | at $80\ \mathrm{Hz}$ |
|---|---|---|---|
| $0$ | $1.0000$ | $1.0000$ | $1.0000$ |
| $2$ | $0.9686$ | $0.8763$ | $0.5358$ |
| $4$ | $0.8763$ | $0.5358$ | $-0.4258$ |
| $6$ | $0.7290$ | $0.0628$ | $-0.9921$ |

A $4\ \mathrm{ms}$ systematic static error costs $12\%$ of the $20\ \mathrm{Hz}$
content, $46\%$ of the $40\ \mathrm{Hz}$ and *reverses* the $80\ \mathrm{Hz}$
(sixteen times the amplitude for a systematic shift) — the reason a static
correction is judged on the high frequencies, where it shows first. A $6\
\mathrm{ms}$ error all but annihilates $40\ \mathrm{Hz}$.

### 3.4 Surface-consistent statics and their exact null space

If the residual time on the trace from source $i$ to receiver $j$ is the sum of a
source term and a receiver term,

$$T_{ij} = s_i + r_j,$$

then solving for $s$ and $r$ has exactly **one** null direction. Adding a constant
$c$ to every source term and subtracting the same $c$ from every receiver term
leaves every $T_{ij}$ unchanged:

$$(s_i+c) + (r_j-c) = s_i + r_j.$$

Conversely, if $\delta s_i + \delta r_j = 0$ for all pairs, then $\delta s_i$ is the
same for all $i$ and $\delta r_j = -\delta s_i$: the null space is one-dimensional,
spanned by that constant.

*Measured verification.* The demonstration builds a $12 \times 40$ synthetic
$T_{ij}$ and adds $c = 5.0\ \mathrm{ms}$: the maximum change in $T_{ij}$ is
$1.7\times10^{-18}\ \mathrm{s}$ — zero to double precision. A *non-constant*
perturbation is visible: a linear shot term of $0.5\ \mathrm{ms\,km^{-1}}$ changes
$T_{ij}$ by up to $1.20\ \mathrm{ms}$, and $2.0\ \mathrm{ms\,km^{-1}}$ by up to
$4.80\ \mathrm{ms}$.

**What that means.** The *absolute* level of the static profile is not in the data.
Every trace can be shifted by a constant with no change in any residual, so the
solution is unique only up to that constant. Fixing it requires an external
constraint — the datum and replacement velocity of Section 3.2, an uphole time, or
a refraction solution — which is exactly why those measurements are part of the
statics workflow and not an optional extra.

### 3.5 The long-wavelength problem is a trade, not a null space

It is tempting to say that long-wavelength statics are "unresolvable". The correct
statement is narrower, and the difference matters:

- **Not a null space of the statics.** Section 3.4 shows that any non-constant
  static perturbation *does* change the data.
- **A trade with the subsurface model.** A static shift $\delta t$ on a reflection
  and a change of the reflector's depth both move the arrival time. For a stacking
  (or migration) velocity $v$, a static error appears as an apparent depth change

$$\delta z = \frac{v\,\delta t}{2}.$$

*Numerical check.* $\delta t = 10\ \mathrm{ms}$, $v = 2500\ \mathrm{m\,s^{-1}}$:
$\delta z = 2500(0.010)/2 = 12.5\ \mathrm{m}$, and over a $2.4\ \mathrm{km}$ line
that is an apparent dip of

$$\arctan(12.5/2400) = 0.298^\circ.$$

**Twelve and a half metres of structure, created by a correction.** The ambiguity
is resolved only by an independent measurement of the near surface — which is the
refraction survey, the uphole, or a borehole velocity — and it is why the correct
order is to determine the near surface *before* interpreting structure, not to fix
the interpretation afterwards with a statics pass.

## 4. Physical interpretation

- **A static correction is an inverse problem with a small, but real, null space.**
  Its constant is fixed by an external datum; everything else is determined by the
  data, in the sense that a wrong solution will not fit the residuals.
- **A wrong weathering velocity damages the depth far more than the static.** The
  weathering *time* that a refraction solution supplies is
  $t_w = t_i/(2\sqrt{1-(v_w/v_r)^2})$, in which the wrong velocity appears twice —
  once enlarging the depth and once enlarging the divisor — so the errors nearly
  cancel: a $10\%$ velocity error moves the depth by $11.5\%$ and the weathering
  time by only $0.08\ \mathrm{ms}$. **The static is nearly right while the
  weathering surface is wrong**, which is precisely the failure mode this lesson
  warns about, and it is silent.
- **Depth errors and stack losses have different scaling.** The depth error is
  linear in the velocity error; the time error is quadratic in the
  *velocity-ratio* error, and the stack loss is quadratic in the time error. A
  $10\%$ velocity error costs $11.5\%$ of depth and essentially nothing ($0.02\%$)
  of the $40\ \mathrm{Hz}$ amplitude; a $50\%$ error costs $63\%$ of depth and
  $3.3\%$ at $80\ \mathrm{Hz}$. The two consequences therefore arrive at very
  different sizes, and the larger one is the quiet one.
- **Surface consistency is an assumption with consequences.** It is what makes the
  problem solvable from the data at all; it is wrong wherever a source or receiver
  sits in an anomalous near-surface pocket, and the residuals then look like noise
  with a spatial pattern.

## 5. Worked examples

### Example 1 — weathering depth and its error

$v_w = 600$, $v_r = 1800\ \mathrm{m\,s^{-1}}$, $t_i = 12.0\ \mathrm{ms}$ gives
$z = 3.818\ \mathrm{m}$ (Section 3.1). If $v_w$ is really $660$:

$$z = \frac{0.012}{2\sqrt{1/660^{2} - 1/1800^{2}}}
= \frac{0.012}{2\sqrt{2.2957\times10^{-6}-3.0864\times10^{-7}}}
= \frac{0.012}{2.8158\times10^{-3}} = 4.262\ \mathrm{m},$$

$+11.6\%$ — and every depth in the profile moves by the same fraction, so the
*shape* of the weathering surface is preserved and its level is wrong. That is the
signature of a velocity error, as opposed to a pick error, which changes the shape.

### Example 2 — a datum static for a line

Station 0 of Section 3.2: $z_w = 3.80$, elevation $124.0$, datum $120.0$, so
$d = 4.0\ \mathrm{m}$, $v_w = 600$, $v_{\mathrm{rep}} = 2500$:

$$t_{\mathrm{stat}} = \frac{3.80}{600} - \frac{3.80-4.0}{2500}
= 6.333\times10^{-3} + 8.0\times10^{-5} = 6.413\ \mathrm{ms}.$$

Note the second term is *negative* in $z_w-d$ because $d > z_w$: the base of the
weathering lies above the datum, so the replacement term is a small negative
number. Getting the sign convention wrong here is the commonest arithmetic error in
a statics spreadsheet, and the limit checks of Section 3.2 catch it.

### Example 3 — the depth error and the static error are different sizes

Suppose the field crew solves the refraction with $v_w = 660$ where the truth is
$600\ \mathrm{m\,s^{-1}}$, on a layer that is truly $3.50\ \mathrm{m}$ thick. The
intercept time is fixed by the data:

$$t_i = 2(3.50)\sqrt{1/600^{2}-1/1800^{2}} = 10.999\ \mathrm{ms}.$$

1. **Depth** from the wrong velocity:
   $z = 0.010999/(2\sqrt{1/660^{2}-1/1800^{2}}) = 3.90\ \mathrm{m}$: $+11.5\%$.
2. **Weathering time**, which is what the static actually uses:

$$t_w = \frac{t_i}{2\sqrt{1-(v_w/v_r)^{2}}}
= \frac{0.010999}{2(0.93035)} = 5.911\ \mathrm{ms}$$

against a true $5.833\ \mathrm{ms}$ (from $z/v_w = 3.50/600$): an error of
$+0.078\ \mathrm{ms}$.
3. **Stack factors** for that $0.078\ \mathrm{ms}$:
$\exp(-2\pi^{2}(40)^{2}(7.8\times10^{-5})^{2}) = 0.9998$ at $40\ \mathrm{Hz}$
and $0.9992$ at $80\ \mathrm{Hz}$ — nothing.

The demonstration's table extends the comparison to $v_w = 900$ ($+63.3\%$ depth,
$+0.517\ \mathrm{ms}$ time, stack factors $0.9916$ and $0.9668$). **The depth error
is an order of magnitude more serious than the static error for the same mistake**,
because $v_w$ is used twice in $t_w$ and cancels to first order. The one part of the
static that does inherit the full depth error is any term computed as a depth
divided by a velocity — the replacement term of Section 3.2, for instance, where a
$0.31\ \mathrm{m}$ thickness error at $v_{\mathrm{rep}} = 2500\mathrm{m\,s^{-1}}$ is $0.12\ \mathrm{ms}$.

**What this means in practice.** A refraction solution with a wrong weathering
velocity produces a *quiet* error: the stack looks fine (the statics are nearly
right) and the weathering surface is $10$–$60\%$ too thick, which then enters any
depth conversion that uses it and any structural interpretation of the shallow
section. The check is not the stack; it is an independent measurement of the
weathering depth or time — an uphole, a borehole, or a refraction profile with the
offsets needed to see the velocity directly.

## 6. Assumptions and regime of validity

1. **A two-layer near surface.** The formula of Section 3.1 assumes one weathering
   layer over one refractor; a velocity gradient or a third layer makes the
   "weathering depth" a model parameter, and the depth becomes dependent on the
   offset range used. Refraction tomography is the remedy.
2. **A horizontal refractor** beneath each station. A dipping interface requires the
   plus-minus (delay-time) formulation, which is why reversed shots are mandatory —
   see [06-10-02](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md).
3. **A surface-consistent static.** Sources and receivers are assumed to carry the
   same static regardless of which pair they form. An anomalous pocket violates it.
4. **Independent static errors.** The Gaussian factor of Section 3.3 requires it; a
   *systematic* error (a wrong $v_w$) is handled by the cosine factor instead, and
   the two have very different frequency behaviour.
5. **No anisotropy and no lateral velocity change over the Fresnel zone** of a
   reflection. A long-wavelength static error within a Fresnel zone partially
   cancels in the stack (the whole zone shifts together), which is why the
   *short*-wavelength statics are the ones that destroy the stack and the
   *long*-wavelength ones are the ones that create false structure.
6. **A replacement velocity that is a velocity**, not a tuning parameter. Changing
   $v_{\mathrm{rep}}$ changes every static and therefore the absolute level of the
   section; it must be documented with the datum.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| weathering depth | $z_w$ | m | $t_i/(2\sqrt{1/v_w^2-1/v_r^2})$ |
| intercept time | $t_i$ | ms | $2z\cos\theta_c/v_w$ |
| velocity | $v_w, v_r, v_{\mathrm{rep}}$ | m/s | — |
| elevation, datum depth | $e, d$ | m | difference of elevations |
| static | $t_{\mathrm{stat}}$ | ms | distance/velocity |
| frequency | $f$ | Hz | $\mathrm{s^{-1}}$ |
| stack factor | $A(f)$ | — | $|\langle e^{i2\pi f\delta t}\rangle|$ |

The exponent $2\pi^2f^2\sigma_t^2$ is dimensionless: $f$ in $\mathrm{s^{-1}}$ and
$\sigma_t$ in s. Mixing milliseconds into it without conversion is the standard way
to produce a stack factor that is either $1$ or $0$ for every frequency.

## 8. Python demonstration

[`code/refraction_static_demo.py`](code/refraction_static_demo.py) prints every
number quoted above:

1. the weathering depth, the five-way sensitivity table to $v_w$, and the
   central-difference derivative;
2. the datum static for five stations, the residual from a wrong $v_w$, and the
   limit checks;
3. the stack response: the analytic Gaussian factor against a direct $500$-trace
   stack measured in the spectrum (agreement within $1\%$ for
   $\sigma_t \le 4\ \mathrm{ms}$), and the cosine table for systematic shifts;
4. the null-space verification: a constant perturbation changes $T_{ij}$ by
   $1.7\times10^{-18}\ \mathrm{s}$, while a $2.0\ \mathrm{ms\,km^{-1}}$ linear
   perturbation changes it by $4.80\ \mathrm{ms}$ — and the $12.5\ \mathrm{m}$,
   $0.298^\circ$ cost of a $10\ \mathrm{ms}$ error;
5. four wrong weathering velocities, with the depth error and the weathering-time
   error side by side and the $40$ and $80\ \mathrm{Hz}$ stack factors alongside
   them — showing that a $10\%$ velocity error is a $11.5\%$ depth error and
   essentially no stack loss.

The demo is print-only, uses the fixed seed `20261014`, needs no network, and
exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-refraction-static-exercises.md`](exercises/03-refraction-static-exercises.md)
and
[`exercises/03-refraction-static-solutions.md`](exercises/03-refraction-static-solutions.md).

- **★** Compute the weathering depth for $t_i = 9.5\ \mathrm{ms}$,
  $v_w = 500$ and $v_r = 1600\ \mathrm{m\,s^{-1}}$.
- **★★** A $4\ \mathrm{ms}$ systematic static error. Compute the stack factor at
  $25$, $50$ and $100\ \mathrm{Hz}$, and state which frequency band the error
  removes.
- **★★★** Design a statics workflow for a line crossing $15\ \mathrm{m}$ of
  topographic relief, stating what fixes the absolute level, what fixes the
  long-wavelength shape, and how you would verify both.

## 10. Further reading

- **Cox, M. (1999). *Static Corrections for Seismic Reflection Surveys.* SEG
  Geophysical Reference Series.** Level: reference. The standard monograph; the
  source of the surface-consistent formulation and of the practical workflow.
- **Taner, M. T., Koehler, F., & Alhilali, K. A. (1974). Estimation and correction
  of near-surface time anomalies. *Geophysics*, 39.** Level: research. The paper
  that established surface-consistent decomposition as a solvable problem.
- **Marsden, D. (1993). Static corrections — a review. *The Leading Edge*.**
  Level: practitioner review. A clear statement of which statics methods work under
  which near-surface conditions, written for processors.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Level: graduate textbook. The refraction and
  near-surface background, including the intercept-time relations used here.
- **Yilmaz, Ö. *Seismic Data Analysis.* SEG.** Level: reference. Statics within the
  full processing sequence, with the stack-response arguments of Section 3.3.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A line crosses a weathered layer $v_w = 600\ \mathrm{m\,s^{-1}}$ thick over a
> refractor of $1800\ \mathrm{m\,s^{-1}}$, with a replacement velocity of
> $2500\ \mathrm{m\,s^{-1}}$ and a datum $2.0\ \mathrm{m}$ below the highest
> station. A reflection at $1.8\ \mathrm{s}$ is stacked with a velocity of
> $2400\ \mathrm{m\,s^{-1}}$. **(a)** A station has an intercept time of
> $10.0\ \mathrm{ms}$ and lies $2.0\ \mathrm{m}$ below the highest point of the
> line. Compute its weathering depth and its datum static. **(b)** Compute the
> stack factor at $50\ \mathrm{Hz}$ for a systematic static error of
> $3\ \mathrm{ms}$ and for a random error of $3\ \mathrm{ms}$ rms, and state which
> kind of error is worse at that frequency. **(c)** The refraction solution used
> $v_w = 660\ \mathrm{m\,s^{-1}}$. Compute the depth error, the residual static,
> and the resulting apparent depth error and dip over a $3\ \mathrm{km}$ line.
> **(d)** State which external measurement fixes the absolute level of the static
> profile, and why the data cannot.

Worked versions of (a)–(c) appear in the
[solutions](exercises/03-refraction-static-solutions.md).

## Common pitfalls

1. **Forgetting that a static error is a structure error.** $12.5\ \mathrm{m}$ of
   apparent depth from $10\ \mathrm{ms}$ at $2500\ \mathrm{m\,s^{-1}}$; the section
   will look entirely reasonable.
2. **Judging a static correction on low frequencies.** A $3\ \mathrm{ms}$ error
   costs $5\%$ at $25\ \mathrm{Hz}$ and $46\%$ at $50\ \mathrm{Hz}$; the
   high-frequency content is where it shows first.
3. **Treating the weathering velocity as a pick.** The depth is $1.1\%$ per $1\%$ of
   $v_w$, and $v_w$ comes from the same fit.
4. **Conflating systematic and random statics.** They scale differently with
   frequency ($\cos$ against Gaussian) and require different remedies.
5. **Assuming surface consistency is free.** It is the assumption that makes the
   decomposition solvable; anomalous near-surface pockets break it and leave
   spatially patterned residuals.
6. **Changing the replacement velocity without saying so.** Every static changes,
   and so does the absolute level of the section.

## Related modules

- [10-04 Near-Surface Seismic and Geotechnical Methods](./README.md) — the module
  this lesson belongs to.
- [06-10-02 Delay-Time (Plus-Minus) Methods and Depth Estimation](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md)
  — the refraction depth solution whose sensitivity this lesson applies.
- [06-09-02 The Reflection Processing Flow](../../06-seismology/09-reflection-seismology/02-processing-flow.md)
  — where statics sit, and what the stack does with the residual.
- [06-02 Ray Theory and Travel Times](../../06-seismology/02-ray-theory-and-travel-times/README.md)
  — the head-wave geometry and the ray parameter behind the intercept-time formula.
- [10-04-01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](01-spt-cpt-crosshole.md)
  — the borehole measurements that provide the independent near-surface velocity.

## Code and exercises

| Path | Contents |
|---|---|
| [`code/refraction_static_demo.py`](code/refraction_static_demo.py) | The five computations of Section 8 |
| [`exercises/03-refraction-static-exercises.md`](exercises/03-refraction-static-exercises.md) | Graded problems |
| [`exercises/03-refraction-static-solutions.md`](exercises/03-refraction-static-solutions.md) | Worked solutions |

```bash
cd 10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_static_demo.py
```
