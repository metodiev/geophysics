---
id: 08-03-03
title: "Reduction to the Pole and Equator; Why It Matters"
level: graduate
prereqs: ["08-03-01", "08-03-02"]
tags: [geomagnetism, electromagnetism, reduction-to-pole, fourier-filtering, potential-fields, low-latitude]
---

# Reduction to the Pole and Equator; Why It Matters

A magnetic anomaly over a body at high magnetic latitude sits on top of the
body and looks like the body. The same body at low magnetic latitude produces an
anomaly that is **displaced**, **asymmetric**, and often dominated by a negative
lobe that has no counterpart in the geology. Almost every interpretation tool —
depth estimation, automatic picking, gravity correlation — assumes the first
case. **Reduction to the pole** (RTP) is the transformation that makes the
second look like the first. This lesson derives it from the Poisson relation,
verifies the derivation numerically, and is honest about what it costs: RTP is
not a correction, it is an *assumption* that the magnetisation direction is
known, and at low latitude it amplifies noise without bound.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Poisson relation for a magnetised body and **verify** it by
   finite differences, reporting the order of convergence.
2. **Derive** the spectral form of the anomaly from the Fourier transform of
   $1/r$ and the symbols of the directional derivatives.
3. **Derive** the RTP filter as the ratio of the pole operator to the actual one,
   and **show** that it is the identity at the pole.
4. **Apply** RTP to a synthetic anomaly and **measure** how far the peak moves
   and how well the amplitude is recovered.
5. **Quantify** the low-latitude instability: noise gain as a function of
   inclination, and the resulting loss of signal-to-noise.
6. **State** which magnetisation direction RTP assumes, and **identify** the
   artefacts it produces when that assumption is wrong.
7. **Explain** when reduction to the equator is used instead, and why the two are
   not interchangeable.

## Prerequisites

- [08-03-01 Magnetic Anomaly Physics](01-magnetic-anomaly-basics.md) — the dipole
  field and $\Delta T$.
- [08-03-02 Koenigsberger Ratio and Remanence Dominance](02-koenigsberger-and-remanence.md) —
  why the magnetisation direction is not simply the field direction.
- [01-10-02 The Fourier Transform](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md) —
  the conventions used in the spectral derivation.

## 1. The Poisson relation

Lesson 01 gave the anomaly of a point dipole. Multiply out the algebraic form
and it can be recognised as a second directional derivative of the Green's
function $1/r$. With $\hat m$ the magnetisation direction, $\hat f$ the ambient
field direction, $C = \mu_0/4\pi$ and $m$ the moment,

$$\Delta T(\mathbf{r}) = C\,m\,\frac{3\left(\hat m\!\cdot\!\hat r\right)\left(\hat f\!\cdot\!\hat r\right)
- \hat m\!\cdot\!\hat f}{r^{3}}
= C\,m\,\left(\hat m\!\cdot\!\nabla\right)\left(\hat f\!\cdot\!\nabla\right)\frac{1}{r},\qquad
r = \left|\mathbf{r}\right|.$$

This is the **Poisson relation** in its point form: a magnetic anomaly is two
directional derivatives of a potential. Its usefulness is that it separates the
*geometry* (the $1/r$ and the derivatives) from the *directions*
($\hat m$ and $\hat f$), and therefore makes it obvious what has to be undone to
change the directions.

**Verification.** The demonstration evaluates both sides independently on a 3-D
grid of spacing $h$, the right-hand side by central differences of $1/r$ and the
left-hand side from the closed form, with the source 3 km outside the sampled
volume:

| $h$ (km) | $\max\left|\text{FD} - \text{analytic}\right| / \max\left|\text{analytic}\right|$ |
|---|---|
| 0.200 | $2.96\times10^{-2}$ |
| 0.100 | $8.66\times10^{-3}$ |
| 0.050 | $2.37\times10^{-3}$ |
| 0.025 | $6.21\times10^{-4}$ |

Successive ratios are 3.4, 3.7 and 3.8, converging on 4: the error falls as
$h^{2}$, exactly as a second-order difference should. The identity is therefore
verified numerically as well as algebraically.

## 2. The anomaly in the wavenumber domain

Write the observation plane as $z=0$ and the source at depth $z_0$ below it, so
that $\mathbf{r} = (x, y, -z_0)$ and $r = \sqrt{x^{2}+y^{2}+z_0^{2}}$. With the
convention $F(\mathbf{k}) = \int f(\mathbf{x})e^{-i\mathbf{k}\cdot\mathbf{x}}
\,\mathrm{d}^{2}x$ and $k = |\mathbf{k}|$ in rad m$^{-1}$,

$$\mathcal{F}\left[\frac{1}{r}\right](\mathbf{k}) = \frac{2\pi\,e^{-k z_0}}{k}.$$

The derivative symbols follow from the same convention. Derivatives in the plane
multiply by $i k_x$ and $i k_y$. The vertical derivative is fixed by the fact
that a potential field above its source satisfies Laplace's equation and decays
upwards, so $\partial/\partial z \leftrightarrow +k$ on the datum plane. Define

$$\hat{\mathcal{O}}_d(\mathbf{k}) = i\left(k_x d_x + k_y d_y\right) + k\,d_z.$$

Then the spectrum of the anomaly of a point dipole is

$$\widetilde{\Delta T}(\mathbf{k}) = C\,m\;
\hat{\mathcal{O}}_{\hat m}(\mathbf{k})\,\hat{\mathcal{O}}_{\hat f}(\mathbf{k})\;
\frac{2\pi e^{-k z_0}}{k}.$$

The factor $e^{-k z_0}$ carries the depth; the two $\hat{\mathcal{O}}$ factors
carry the directions. **RTP is the removal of the two directional factors.**

**Verification.** The demonstration builds a synthetic dipole anomaly, tapers the
grid (a Hann-like flat-top window covering the central 50%), and checks the
spectral construction in two steps. The vertical derivative of the tapered
$1/r$ field agrees with the analytic $z_0/r^{3}$ to a maximum of
$1.1\times10^{-3}$ of the analytic maximum over the 1–8 km shell; the full
composite $\hat{\mathcal{O}}_{\hat m}\hat{\mathcal{O}}_{\hat f}$ applied to
$1/r$ reproduces the analytic anomaly to $9.0\times10^{-3}$ of its peak. That
residual is dominated by the finite aperture — the spectrum of $1/r$ decays only
as $1/k$, so the grid and the taper, not the operator, set the accuracy.

## 3. The RTP filter

The pole-equivalent anomaly is the one that would be measured if both the
magnetisation and the ambient field were vertical, $\hat m = \hat f = \hat z$,
for which $\hat{\mathcal{O}}_{\hat z} = k$ and
$\hat{\mathcal{O}}_{\hat z}^{2} = k^{2}$. Dividing one spectrum by the other,

$$\boxed{\;\mathrm{RTP}(\mathbf{k}) = \frac{k^{2}}
{\hat{\mathcal{O}}_{\hat m}(\mathbf{k})\,\hat{\mathcal{O}}_{\hat f}(\mathbf{k})}.}$$

Three properties follow at once.

1. **At the pole the filter is the identity.** With
   $\hat m = \hat f = \hat z$ the numerator and denominator are the same, and the
   demonstration measures
   $\max_k\left|\mathrm{RTP}-1\right| = 1.7\times10^{-16}$ over all modes except
   $\mathbf{k} = 0$. RTP does nothing where nothing needs doing.
2. **The filter is real in the wavenumber domain only if the two directions are
   equal**, because otherwise the two $i k_x$ terms combine into a complex
   factor. In general RTP is a **phase** as well as an amplitude operation: it
   moves the anomaly.
3. **It is singular at low latitude.** Take the equator, $\hat m = \hat f =
   \hat x$, so $\hat{\mathcal{O}} = i k_x$ and
   $\mathrm{RTP} = -k^{2}/k_x^{2}$. Along the line $k_x = 0$ the denominator
   vanishes: RTP is unbounded, and any noise on that line is multiplied by an
   arbitrarily large factor.

## 4. Worked example: what RTP does to one anomaly

A **synthetic** dipole with $M = 2.00$ A m$^{-1}$ and $V = 1.00$ km$^{3}$
($m = 2.00\times10^{9}$ A m$^{2}$) lies 3.0 km deep. The grid is
$400$ m spacing over $64\times64$ km, and the ambient field is vertical so that
the *measurement* direction is fixed while the *magnetisation* direction is
varied.

- On-axis, pole-equivalent anomaly (expected):
  $(\mu_0/4\pi)(2m/z_0^{3}) = 10^{-7}\times2\times2.00\times10^{9}/(3.0\times10^{3})^{3}
  = 14.815$ nT. The demonstration measures $14.815$ nT, and the peak sits
  $0.0$ km from the source.
- At $I = 45^\circ$ the same body gives a peak of $9.098$ nT displaced
  $1.2$ km from the source.
- After RTP the peak moves to $0.00$ km and is $14.802$ nT, which is $-0.09\%$
  from the analytic pole value. Over the flat central region the RTP result
  differs from the analytic pole anomaly by at most $1.1\times10^{-3}$ of the
  peak.

So RTP works: it recovers both the position and the amplitude of the
pole-equivalent anomaly, to a fraction of a per cent, from data taken at an
inclined magnetisation.

## 5. Why it matters, and what it costs

**Why.** Almost every downstream tool is built on the pole case. Depth estimators
of [05](05-magnetic-depth-estimation.md) assume a symmetric, centred anomaly;
automatic source picking, upward continuation, derivative maps and
gravity–magnetic correlation all behave better when the anomaly sits over its
source. RTP is also the cheapest way to compare data sets acquired at different
magnetic latitudes on a common basis.

**What it costs.** The same filter that removes the directional factors
multiplies the noise by the RMS of $\left|\mathrm{RTP}\right|$ over the
wavenumber plane. Measured on the synthetic grid:

| Magnetisation inclination | Peak $\Delta T$ (nT) | Peak displacement (km) | RTP white-noise gain |
|---|---|---|---|
| $90^\circ$ | 14.815 | 0.0 | 1.00 |
| $75^\circ$ | 14.069 | 0.4 | 1.04 |
| $60^\circ$ | 12.009 | 0.8 | 1.16 |
| $45^\circ$ | 9.098 | 1.2 | 1.44 |
| $30^\circ$ | 6.019 | 2.0 | 2.15 |
| $20^\circ$ | 4.192 | 2.4 | 3.48 |
| $15^\circ$ | 3.354 | 2.8 | 5.07 |
| $10^\circ$ | 2.647 | 2.8 | 8.93 |
| $5^\circ$ | 2.027 | 3.2 | 24.65 |

Both columns move the wrong way together: the further the magnetisation from
vertical, the more the data must be re-arranged and the more noise is amplified.
At $45^\circ$ the noise gain is 1.44 — acceptable. At $5^\circ$ it is 24.7, which
means that a survey with 0.1 nT of noise acquires 2.5 nT of noise in the RTP
product, while the anomaly peak is only about 2 nT.

The demonstration measures the consequence directly. With $0.10$ nT rms of added
noise, the un-filtered ratio of peak to background is 91; after RTP at
$I = 45^\circ$ it is 12.9, and at $I = 10^\circ$ it is 7.0. The transformation
buys a map that looks like the geology, and pays for it in
signal-to-noise.

## 6. Reduction to the equator, and the honest alternative

At very low inclination the reverse transformation is used: **reduction to the
equator** (RTE) rewrites the data as if the magnetisation were horizontal, which
at the equator is the natural geometry and is numerically stable there (and
unstable at the pole, symmetrically). The pair RTP/RTE is a single rotation in
direction space; which end you rotate to is a numerical question, not a physical
one.

Three honest alternatives to pretending the magnetisation is vertical:

1. **Invert for the magnetisation vector.** If the vector is unknown, treat it as
   a parameter; the cost is that the inverse problem gains two or three
   dimensions of ambiguity, exactly as in
   [06 Magnetic Inversion](06-magnetic-inversion.md).
2. **Use pseudogravity.** Because the anomaly is a directional derivative of a
   potential, the vertical derivative of the magnetic anomaly of a body is
   proportional to the gravity field of the same body with density replaced by
   magnetisation. The transformation removes the *field* direction factor and
   leaves a quantity that looks like a gravity map — useful, but it still assumes
   the magnetisation direction.
3. **Do nothing and interpret the skewed anomaly.** The displacement is
   information: it is a constraint on the direction of $\mathbf{M}$, and
   discarding it by filtering throws that constraint away.

## 7. Assumptions and regime of validity

1. **The magnetisation direction is known and uniform.** This is the operative
   assumption. If it is wrong — and for a remanence-dominated body it usually is
   ([02](02-koenigsberger-and-remanence.md)) — RTP produces a *different* wrong
   answer, with artefacts elongated in the direction of the assumed $\hat m$.
2. **The anomalies are caused by induced magnetisation in the direction of the
   ambient field.** This is the default assumption in commercial practice, and it
   is the one to state explicitly whenever RTP is applied.
3. **The data are on a level surface and the field is a potential field.** RTP is
   a wavenumber-domain operation and inherits all the faults of the grid:
   levelling errors, flight-line corrugation and edge effects.
4. **The survey is large enough.** The filter's long-wavelength behaviour
   requires a wide survey; the demonstration tapers the grid before transforming,
   and reports the residual that this leaves.
5. **Adequate noise control at low latitude.** The gain table of Section 5 is the
   quantitative statement: below roughly $20^\circ$ inclination, RTP should be
   applied only with a stabilised (regularised) denominator, or not at all.
6. **A true dipole is not required for the filter, but the derivation above
   used one.** The filter depends only on the directional factors, which are
   properties of any uniformly magnetised body's field; the depth factor cancels
   in the ratio.

## 8. Python demonstration

`code/reduction_to_pole_demo.py`:

1. builds a synthetic dipole anomaly and measures the peak displacement;
2. verifies the Poisson identity in 3-D by finite differences and reports the
   $h^{2}$ convergence;
3. verifies the spectral construction against the analytic anomaly;
4. applies RTP, shows the identity at the pole and the recovery to $-0.09\%$ at
   $I = 45^\circ$;
5. tabulates displacement and noise gain against inclination;
6. measures the loss of signal-to-noise in noise-injected data.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reduction_to_pole_demo.py
```

Fixed seed, print-only, exits 0.

## 9. Exercises

[`exercises/03-reduction-to-pole-exercises.md`](./exercises/03-reduction-to-pole-exercises.md)
and
[`exercises/03-reduction-to-pole-solutions.md`](./exercises/03-reduction-to-pole-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** anomaly is measured at $I = 25^\circ$ inclination,
> $D = 0^\circ$ declination, over a body $1.0$ km deep. **(a)** Write the RTP
> filter and identify the direction along which it is singular. **(b)** Read the
> noise gain for $I = 25^\circ$ from the table and estimate the inclination at
> which a survey with 0.2 nT of noise can no longer be RTP'd. **(c)** State the
> assumption RTP makes about the magnetisation and describe the artefact it
> produces if the body is remanence-dominated with $Q = 5$ pointing across the
> field. **(d)** Name one transformation that avoids the assumption, and one
> measurement that would fix the direction.

## Common pitfalls

1. **Calling RTP a correction.** It is a change of reference that assumes a
   direction; if that assumption is false the output is wrong, not merely noisy.
2. **Applying RTP at low latitude without stabilisation.** The filter is
   unbounded on a line in the wavenumber plane, and real grids have energy there.
3. **Ignoring the phase part of the filter.** RTP moves anomalies; a reader who
   compares source positions before and after must expect the move.
4. **Forgetting the taper.** Spectral filters on a truncated grid produce edge
   artefacts that are easy to mistake for geology.
5. **Confusing reduction to the pole with reduction to the equator.** They are
   different targets; the choice is made by which is numerically stable at the
   survey's latitude.
6. **Using RTP to make two surveys comparable without checking the remanence.**
   Two surveys agree after RTP only if both obey the induced-magnetisation
   assumption.

## Related modules

- [02 Koenigsberger Ratio and Remanence Dominance](02-koenigsberger-and-remanence.md) —
  why the assumed direction is often wrong.
- [04 Magnetic Forward Modelling](04-magnetic-forward-modelling.md) — the
  model whose anomaly is filtered here.
- [05 Magnetic Depth Estimation](05-magnetic-depth-estimation.md) — the
  interpretation tools that assume a pole-equivalent map.
- [01-10 Fourier Analysis](../../01-mathematics/10-fourier-analysis/README.md) —
  the transform conventions and the filtering techniques used.
- [03-11 PyGMT and Mapping](../../03-scientific-computing/11-pygmt-and-mapping/README.md) —
  how filtered grids are displayed and what the display hides.
