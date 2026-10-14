---
id: 07-05-02
title: "GOCE, Gravity Gradients and the Static Field"
level: graduate
prereqs: ["07-01-02", "07-01-03", "07-05-01"]
tags: [gravity, geodesy, satellite-gravimetry, gravity-gradients, spherical-harmonics]
---

# GOCE, Gravity Gradients and the Static Field

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the gravity-gradient tensor $\Gamma_{ij} = \partial^{2}U/\partial
   x_i\partial x_j$ and **derive** its two symmetries — symmetry and zero trace —
   from the physics of a potential in vacuum.
2. **Compute** the tensor of the monopole field in the local orbital frame and
   **express** every component in SI units and in Eötvös.
3. **Derive** the exact radial degree scaling $\partial^{2}U_l/\partial r^{2}
   \propto (l+1)(l+2)\,r^{-(l+3)}$ and **verify** it by finite differences.
4. **Analyse** the transfer function $T(l) = (l+1)(l+2)(R/a)^{l+2}$, find its
   peak analytically and numerically, and explain why the peak degree falls as
   the orbit rises.
5. **Estimate** the degrees at which a gradient measurement is noise-limited,
   given a stated synthetic coefficient spectrum and a stated per-component
   noise, and compare two altitudes.
6. **Explain** why a gravity-gradient mission determines the **static** field
   (and its tide-free reference) rather than mass change, and what that implies
   for the combination of the two mission types.
7. **Use** the trace of the measured tensor as a consistency check and
   **quantify** the scale error it can detect.

## Prerequisites

- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../01-gravity-fundamentals/02-gravity-potential.md) —
  the potential and its derivatives, and Laplace's equation in vacuum.
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md) —
  the normal field that must be subtracted before an anomaly means anything.
- [01 GRACE and GRACE-FO: Mission Concept and Data Products](01-grace-gracefo.md) —
  the range-link observable and the downward-continuation limit, which this
  lesson's observable is compared against.

> **All models and data in this module are SYNTHETIC.** The altitudes,
> coefficients, spectra and noise levels below are teaching values, not the
> parameters of any real mission. No measured gravity field is used.

## 1. Why measure a gradient instead of a range?

The [range-link](01-grace-gracefo.md) observable is the *second difference* of
the potential along a $220\ \mathrm{km}$ baseline — an average of curvature over
a long piece of the field. A gravity gradiometer instead measures the **local
curvature of the potential at the spacecraft**, as a $3\times3$ tensor,

$$\Gamma_{ij} = \frac{\partial^{2}U}{\partial x_i\,\partial x_j},$$

using pairs of proof masses on a rotating boom. The practical difference is
threefold, and each part is a lesson in itself.

- **No drag-free requirement on the same scale.** A gradiometer differences two
  accelerometers a few tens of centimetres apart, so the *non-gravitational*
  acceleration is common to both and cancels to first order. The range link, by
  contrast, must model the non-gravitational acceleration of two spacecraft. This
  is why a gradient mission can fly lower — and lower means stronger signal.
- **Local measurement, local resolution.** The baseline is centimetres rather
  than hundreds of kilometres, so the observable is a *point* curvature, not an
  average. The demonstration shows the two differ by about $1\%$ at a
  $220\ \mathrm{km}$ baseline for the same anomaly.
- **Static, not time-variable.** A gradiometer measures the total field at every
  instant; separating a mass *change* from the static field is a differencing of
  two satellite solutions, so gradient missions are used for the static field and
  the range links for the time-variable field.

## 2. The gradient tensor and its symmetries

Because $\Gamma_{ij}$ is a matrix of second partial derivatives of a scalar, it
is **symmetric**: $\Gamma_{ij} = \Gamma_{ji}$, so at most six of the nine
components are independent. In the space between the masses, the potential
satisfies Laplace's equation,

$$\nabla^{2}U = \Gamma_{xx} + \Gamma_{yy} + \Gamma_{zz} = 0
\qquad\Longrightarrow\qquad
\operatorname{tr}\boldsymbol{\Gamma} = 0 .$$

So the tensor has **five** independent components, and the trace is a quantity
whose value the physics *guarantees* and the instrument does not need to be told.
The demonstration verifies this numerically: a finite-difference Hessian of a
synthetic zonal field at $250\ \mathrm{km}$ has largest component $0.856\
\mathrm{E}$ and trace $3.4\times10^{-8}\ \mathrm{E}$, a ratio of
$4.0\times10^{-8}$ — pure round-off.

In the local orbital frame (radial $\hat r$, along-track, cross-track) the
monopole field $\mathrm{GM}/r$ gives

$$\Gamma_{rr} = +\frac{2GM}{r^{3}}, \qquad
\Gamma_{tt} = \Gamma_{cc} = -\frac{GM}{r^{3}},$$

because $\partial^{2}r^{-1}/\partial r^{2} = 2r^{-3}$ while the tangential
curvature is $-r^{-3}$, and the trace $2-1-1 = 0$ holds exactly.

*Worked example 1.* At $250\ \mathrm{km}$ altitude, $r = 6.621\times10^{6}\
\mathrm{m}$:

$$r^{3} = 2.9027\times10^{20}\ \mathrm{m^{3}},\qquad
\frac{GM}{r^{3}} = \frac{3.986004418\times10^{14}}{2.9027\times10^{20}}
= 1.3733\times10^{-6}\ \mathrm{s^{-2}}
= 1373.3\ \mathrm{E},$$

$$\Gamma_{rr} = 2746.6\ \mathrm{E}, \qquad
\Gamma_{tt} = \Gamma_{cc} = -1373.3\ \mathrm{E},$$

where $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$ (the Eötvös unit). At
$500\ \mathrm{km}$ the same components are $2457.6\ \mathrm{E}$ and
$-1228.8\ \mathrm{E}$. **The monopole curvature is of order $10^{3}$ E, while
useful anomalies are of order $1$–$100$ E**: the dynamic range is five to six
orders of magnitude, and it is handled by subtracting a very good reference
field, not by instrument precision.

## 3. The anomalous part, and how it is separated

Write the potential as the normal field of a reference ellipsoid plus the
anomalous part $T$ (the disturbing potential). The tensor splits the same way:

$$\boldsymbol{\Gamma} = \boldsymbol{\Gamma}_{\text{normal}} +
\boldsymbol{\Gamma}_{T}, \qquad
\operatorname{tr}\boldsymbol{\Gamma}_{T} = 0,$$

so removing the normal field removes $10^{3}$ E and leaves the $1$–$100$ E of
interest. Everything the mission reports is a statement about
$\boldsymbol{\Gamma}_{T}$, and its quality depends on the normal field being
known far better than the anomaly. This is the same bookkeeping as in
[07-04-02 height systems](../04-geodesy-reference-frames/02-height-systems.md):
what is measured is a **difference from a reference**, and the reference is an
assumption, not a measurement.

## 4. Degree scaling: why a gradiometer sees high degrees better

Take one spherical-harmonic term. Outside the masses,

$$U_{lm}(r,\theta,\phi) = \frac{GM}{r}\left(\frac{R}{r}\right)^{l}
\left[C_{lm}\cos m\phi + S_{lm}\sin m\phi\right]\bar P_{lm}(\cos\theta),$$

i.e. the radial dependence is exactly $r^{-(l+1)}$ times a dimensionless angular
factor. Differentiating twice with respect to $r$:

$$\frac{\partial^{2}U_{lm}}{\partial r^{2}}
= (l+1)(l+2)\,\frac{GM}{r^{3}}\left(\frac{R}{r}\right)^{l}
\left[\ldots\right]\bar P_{lm}(\cos\theta)
= (l+1)(l+2)\,\frac{GM\,R^{l}}{r^{l+3}}\,\left[\ldots\right]\bar P_{lm}.$$

Two factors therefore work in opposite directions when a coefficient is referred
to a *fixed surface amplitude*:

$$\underbrace{\frac{(l+1)(l+2)}{\text{curvature grows as }l^{2}}}_{\text{signal}}
\qquad\text{and}\qquad
\underbrace{\left(\frac{R}{a}\right)^{l+2}}_{\text{attenuation}} ,$$

so define the **transfer function**

$$T(l) = (l+1)(l+2)\left(\frac{R}{a}\right)^{l+2}.$$

*Worked example 2.* Find the peak of $T(l)$ for $h = 250\ \mathrm{km}$, i.e.
$a/R = 1.03924$. Setting $\mathrm{d}\ln T/\mathrm{d}l = 0$:

$$\frac{1}{l+1} + \frac{1}{l+2} = \ln\!\frac{a}{R} = 0.038489
\;\Longrightarrow\; 0.038489\,l^{2} - 1.8845\,l - 2.9230 = 0
\;\Longrightarrow\; l^{*} = 50.5 .$$

The cruder approximation $l^{*} \approx 2/\ln(a/R) = 52.0$ is $3\%$ high. The
demonstration's integer peak is degree $50$, and at $500\ \mathrm{km}$
($a/R = 1.07848$) both routes give $l^{*}\approx 25$. **A gradiometer is most
sensitive, relative to the same surface coefficient, at a degree set by its
altitude** — roughly $1/\ln(a/R)$ to $2/\ln(a/R)$.

## 5. Where the measurement actually runs out of signal

The peak of $T(l)$ is not the end of the usable range; the noise decides that.
Propagating a per-component noise $\sigma_{\Gamma}$ to a degree-$l$ coefficient
estimate, the number of independent tensor samples per degree grows as
$2l+1$, so the noise in a degree-$l$ estimate falls as
$\sigma_{\Gamma}/\sqrt{2l+1}$. Comparing with a **stated** synthetic surface
radial-gradient spectrum $A_s(l) = 1.0\times10^{-10}(2/l)^{1.5}\
\mathrm{s^{-2}}$ and a per-component noise of $0.10\ \mathrm{E}$:

| altitude | S/N at $l=10$ | S/N at $l=50$ | highest $l$ with S/N $>1$ | half-wavelength |
|---|---|---|---|---|
| 250 km | 34.09 | 28.81 | 167 | 120 km |
| 300 km | 31.15 | 19.48 | 135 | 148 km |
| 500 km | 21.85 | 4.19 | 73 | 274 km |

*Worked example 3.* Check the same coefficient at degree 100 on both orbits. The
synthetic surface amplitude is
$A_s(100) = 1.0\times10^{-10}(2/100)^{1.5} = 2.83\times10^{-13}\
\mathrm{s^{-2}} = 0.283\ \mathrm{mE}$ and the noise is the same at both
altitudes, $0.10/\sqrt{201}\ \mathrm{E} = 7.05\ \mathrm{mE}$. Then

$$250\ \mathrm{km}:\quad T(100) = 203 \Rightarrow
\text{signal} = 0.283 \times 203 = 57.4\ \mathrm{mE}
\Rightarrow \mathrm{S/N} = 8.2,$$
$$500\ \mathrm{km}:\quad T(100) = 4.64 \Rightarrow
\text{signal} = 0.283 \times 4.64 = 1.31\ \mathrm{mE}
\Rightarrow \mathrm{S/N} = 0.19 .$$

**The same coefficient is detected at $250\ \mathrm{km}$ and lost at
$500\ \mathrm{km}$**, and the factor of $43$ between the two measurements is
entirely the $(R/a)^{l}$ attenuation produced by a $250\ \mathrm{km}$ difference
in altitude.

This is the central quantitative statement of this lesson and it is worth saying
in words: *the resolution of a satellite gravity mission is set by its altitude
first and its instrument noise second*, because the altitude enters
exponentially in degree and the noise enters only as $\sqrt{2l+1}$.

## 6. Static versus time-variable — what a gradient mission can and cannot do

A gradiometer measures the *instantaneous* tensor. Two consecutive solutions from
the same mission differ by the mass redistribution that occurred between them,
but the difference is:
- small compared with the static field (this is the same small-residual problem as
  in [01](01-grace-gracefo.md));
- dominated by the *orbit and reference-field* errors, which do not cancel in a
  difference of two static solutions;
- and, because gradient missions fly lower for signal, they fly shorter
  lifetimes: the parameter choices that make a gradient mission excellent at
  high-degree *static* structure are exactly the choices that make it poor at
  long-term mass trends.

So the two mission types answer different questions, and both appear in the
same combined models:

| | range link | gradient tensor |
|---|---|---|
| observable | second difference over a long baseline | local curvature at a point |
| best degrees | low (long wavelength) | medium to high, by altitude |
| time-variable mass | yes, its purpose | not its purpose |
| needs drag model | yes | largely cancels |
| natural altitude | higher, longer life | lower, shorter life |

Reporting a *mass trend* from a gradient-only solution, or a *high-degree static
field* from a range-only solution, is possible but requires stating the
regularisation that stands in for the missing sensitivity.

## 7. Assumptions and regime of validity

1. **Vacuum.** Laplace's equation holds between the masses. Inside a
   mass — for a satellite still inside the atmosphere this is still true for
   gravity, but the *non-gravitational* acceleration does not cancel perfectly,
   and the residual appears in the trace.
2. **Point measurement.** The tensor is assumed constant over the instrument
   baseline. At an orbit radius, the curvature changes over a scale of order
   $r^{2}/\rho$; for a $0.5\ \mathrm{m}$ baseline and $r = 6.6\times10^{6}\
   \mathrm{m}$ the variation is of order $10^{-7}$ of the signal, negligible
   compared with the target accuracy but not compared with $10^{-9}$ of the
   monopole (which is why the reference field must be excellent).
3. **Known orientation.** The tensor must be rotated from the instrument frame
   into the local frame; the attitude error enters directly and cannot be
   averaged away because it is smooth.
4. **Linear response.** The proof-mass differential acceleration is assumed
   proportional to the true tensor; calibration factors are per-component and are
   what the trace check of Section 8 detects.
5. **Tide-free / zero-tide convention.** The solid Earth tide changes the tensor,
   so results are reported in a stated tide convention (see
   [06-01 Solid Earth Tides](../06-earth-tides-and-rotation/01-solid-earth-tides.md)).

## 8. The trace as a free diagnostic

Because the true trace is zero, a measured trace is a direct readout of
inconsistency. The demonstration quantifies both sides:

- For pure, consistent symmetrised noise of per-component rms $\sigma$, the trace
  rms is $\sqrt{3}\,\sigma$ and the off-diagonal norm rms is
  $\sqrt{3/2}\,\sigma$, so their ratio is
  $\sqrt{3/(3/2)} = \sqrt{2} \approx 1.414$ — measured as $1.39$–$1.43$ over
  three noise levels. That is what a *quiet* trace looks like.
- A calibration error of relative size $\epsilon$ in the radial component
  injects $\epsilon\,\Gamma_{rr}$ into the trace. With $\Gamma_{rr} = 2746.6\
  \mathrm{E}$ at $250\ \mathrm{km}$ and a stated noise of $0.10\ \mathrm{E}$:
  $\epsilon = 10^{-4}$ gives $0.27\ \mathrm{E}$ ($2.7\sigma$) and
  $\epsilon = 10^{-3}$ gives $2.75\ \mathrm{E}$ ($27\sigma$).

So the trace detects a one-part-in-a-thousand scale error at high significance.
What it cannot do is tell you *whether* the culprit is the instrument or the
non-gravitational acceleration model — both enter the trace additively. A check
that flags a problem without diagnosing it is still worth having.

## 9. Python demonstration

`code/goce_demo.py` prints, with units:

1. **Monopole tensor** at $250$ and $500\ \mathrm{km}$: $\Gamma_{rr} = 2746.6$
   and $2457.6\ \mathrm{E}$, tangential components $-1373.3$ and
   $-1228.8\ \mathrm{E}$, trace exactly $0$.
2. **Trace-free check** on a finite-difference Hessian of a synthetic zonal field
   ($C_{20} = 10^{-4}$): largest component $0.856\ \mathrm{E}$, trace
   $3.4\times10^{-8}\ \mathrm{E}$, ratio $4.0\times10^{-8}$.
3. **Exact degree scaling**: the finite-difference
   $\partial^{2}U/\partial r^{2}$ against
   $(l+1)(l+2)\mathrm{GM}C_{l0}(R/r)^{l}P_l/r^{3}$ for $l$ up to $120$, agreeing
   to $2\times10^{-8}$–$3\times10^{-7}$.
4. **Transfer function**: the peak degree ($50$ at $250\ \mathrm{km}$, $25$ at
   $500\ \mathrm{km}$) against the exact continuous solution
   ($l^{*} = 50.47$ and $24.98$) and the crude $2/\ln(a/R)$.
5. **Signal-to-noise crossover** for the synthetic spectrum: usable degrees
   $167$, $135$, $73$ at $250$, $300$ and $500\ \mathrm{km}$.
6. **Trace diagnostics**: the $\sqrt{2}$ signature of consistent noise and the
   detection of a scale error down to $10^{-4}$.

The demonstration is print-only, fixed-seed, network-free, and exits 0.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/02-goce-exercises.md`](./exercises/02-goce-exercises.md) and
[`exercises/02-goce-solutions.md`](./exercises/02-goce-solutions.md).

- **★** Compute $\Gamma_{rr}$ and the trace of the monopole tensor at
  $h = 300\ \mathrm{km}$, in $\mathrm{s^{-2}}$ and E.
- **★** Verify that $\operatorname{tr}\boldsymbol{\Gamma} = 0$ for a point-mass
  field by direct differentiation of $-Gm/|\mathbf{r}-\mathbf{r}_m|$.
- **★★** Derive $T(l)$ and find its peak degree at $h = 400\ \mathrm{km}$ both
  exactly and with $2/\ln(a/R)$.
- **★★** Using the lesson's synthetic spectrum and $0.10\ \mathrm{E}$ noise,
  find the degree at which S/N falls below 1 for $h = 350\ \mathrm{km}$.
- **★★★** Design a numerical experiment that separates the effect of altitude
  from the effect of noise on the usable degree, and state what a single
  mission cannot distinguish without a second mission.

## 11. Mastery checkpoint

Do this without notes:

> A synthetic gradiometer flies at $h = 300\ \mathrm{km}$ and delivers
> $\Gamma_{rr}$, $\Gamma_{tt}$, $\Gamma_{cc}$ plus three off-diagonal
> components with a per-component noise of $0.10\ \mathrm{E}$. **(a)** Compute
> $\Gamma_{rr}$ for the monopole field in E and state the trace. **(b)** A
> synthetic zonal coefficient $C_{20} = 10^{-4}$ produces a largest anomalous
> component of $0.86\ \mathrm{E}$: what fraction of the monopole term is that?
> **(c)** Find the degree at which the transfer function
> $T(l) = (l+1)(l+2)(R/a)^{l+2}$ peaks at this altitude, exactly and with
> $2/\ln(a/R)$. **(d)** Which of $250\ \mathrm{km}$, $300\ \mathrm{km}$ and
> $500\ \mathrm{km}$ reaches degree 100 at S/N $> 1$? **(e)** What does the
> trace detect, and what can it not diagnose?

*Answers.* **(a)** $r = 6671\ \mathrm{km}$,
$GM/r^{3} = 1.342657\times10^{-6}\ \mathrm{s^{-2}}$, so
$\Gamma_{rr} = +2685.31\ \mathrm{E}$ and the trace is $0$ by Laplace's
equation. **(b)** $0.86/2685 = 3.2\times10^{-4}$, i.e. about three parts in ten
thousand — the dynamic-range problem in one number. **(c)** $a/R = 1.04709$,
$\ln(a/R) = 0.046013$; solving $1/(l+1)+1/(l+2) = 0.046013$ gives
$l^{*} = 41.97$, and the crude $2/\ln(a/R) = 43.47$ is high by $3.6\%$.
**(d)** $250\ \mathrm{km}$ (usable degree 167) and $300\ \mathrm{km}$
(135) do; $500\ \mathrm{km}$ (73) does not. **(e)** The trace detects an
inconsistent component — a scale error $\epsilon$ injects
$\epsilon\Gamma_{rr}$, so $10^{-3}$ is already $27\sigma$ — but it cannot
separate an instrument error from a mis-modelled non-gravitational acceleration,
since both enter additively.
## 12. Common pitfalls

1. **Quoting a gradient in mGal.** Gradients are in $\mathrm{s^{-2}}$ or E;
   $\mathrm{mGal}$ is a unit of acceleration, not curvature. Converting between
   them without a length is a dimensional error.
2. **Forgetting the trace.** Reporting six independent components (or ignoring a
   nonzero sum) discards the single cheapest consistency check available.
3. **Thinking the instrument measures gravity.** It measures curvature;
   recovering the field is an inversion with its own regularisation.
4. **Comparing noise figures from different altitudes.** A better instrument at
   a higher altitude can be a worse mission.
5. **Assuming the reference field is exact.** The subtracted normal field is two
   to five orders larger than the anomaly.
6. **Treating attitude error as random.** It is smooth and correlated, so it
   biases the solution rather than averaging out.

## 13. Real-world applications

- **The static global geoid.** Gradient data are the principal contributor to the
  medium- and high-degree static field, which is what makes a global geoid
  accurate enough for the height systems of
  [module 07](../07-geoid-and-height-modern/README.md).
- **Combined models.** Global gravity models combine several data types; the
  degree range in which each dominates is a direct consequence of the transfer
  functions derived here.
- **Orbit and attitude estimation.** The tensor's sensitivity to attitude makes
  the same data useful for spacecraft engineering.
- **Reference for exploration.** High-resolution static fields are the reference
  from which airborne and ground surveys subtract the long-wavelength field
  (see [07-02-05](../02-gravity-instruments-and-surveys/05-airborne-marine-gravity.md)).

## 14. Further reading

- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the potential-theory
  basis of the tensor and its degree scaling.
- **Torge, W. & Müller, J., *Geodesy*** — satellite missions in context and the
  combination of observables.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — modern
  treatments of boundary-value problems and gradient data.
- **Kaula, W. M., *Theory of Satellite Geodesy*** — the degree-variance
  description used to compare a signal spectrum with a noise spectrum.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 15. Related lessons

- [01 GRACE and GRACE-FO: Mission Concept and Data Products](01-grace-gracefo.md) —
  the range-link observable and its downward-continuation limit.
- [03 Spherical Harmonic Solutions and Coefficient Interpretation](03-spherical-harmonic-solutions.md) —
  the coefficient formalism whose radial derivatives are used here.
- [04 Mass Concentration Solutions, Leakage and Filtering](04-mascons-and-leakage.md) —
  what happens when either observable is turned into a map.
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md) —
  the normal tensor that is subtracted.
- [07-06-01 Solid Earth Tides and Their Gravity Signature](../06-earth-tides-and-rotation/01-solid-earth-tides.md) —
  the time-variable part that must be modelled out.

## 16. Related modules

- [Satellite Gravimetry](./README.md) — this module's index.
- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential and the reference ellipsoid whose tensor is subtracted here.
- [12 Global Geophysics and the Interior](../../12-global-geophysics-interior/README.md) —
  where a high-degree static field is used as a constraint on the interior.
- [26-reference-library](../../26-reference-library/README.md) — symbols, units
  and constants used without re-derivation.

## 17. Self-assessment checklist

- [ ] I can define $\Gamma_{ij}$ and prove it is symmetric and trace-free.
- [ ] I can compute the monopole tensor at any altitude in E.
- [ ] I can derive $\partial^{2}U_{l}/\partial r^{2} \propto (l+1)(l+2)r^{-(l+3)}$.
- [ ] I can find the peak degree of $T(l)$ exactly and approximately.
- [ ] I can decide which of two altitudes reaches a given degree at S/N $>1$.
- [ ] I can explain why a gradient mission is for the static field.
- [ ] I can use the trace to bound a scale error.
