---
id: 08-05-05
title: "Airborne EM for Conductivity Mapping"
level: doctoral
prereqs: ["08-05-01", "08-05-03", "08-05-04"]
tags: [geomagnetism, electromagnetism, airborne-em, conductivity-mapping, height, survey-design]
---

# Airborne EM for Conductivity Mapping

Airborne EM is frequency- or time-domain EM with the coils carried on a bird
towed under a helicopter or fixed-wing aircraft. Everything in
[08-05-01](01-frequency-domain-em.md), [08-05-02](02-time-domain-em.md) and
[08-05-03](03-em-modelling.md) applies unchanged; what changes is that the
**geometry is now a data uncertainty**. The bird flies at tens of metres, its
height varies metre by metre along every line, and the signal falls off steeply
with that height. This lesson is about that single fact and its consequences: a
height error is indistinguishable from a conductivity error over a wide range, so
the quality of a conductivity map is set by an altimeter and by survey design
before any inversion is run.

It is also the lesson in this module where the *product* is furthest from the
measurement. A drill-core conductivity is a property of a rock; an airborne
conductivity map is a map of the conductivity of a one-dimensional model that
best fits a response measured from a moving platform. The gap between the two —
lateral resolution, footprint, layering, anisotropy, cultural metal — is the
subject of the last sections.

All models and data in this module are **SYNTHETIC**. The conductivities,
thicknesses, heights, separations and frequencies are chosen teaching values; no
real survey, system or alteration zone is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the height dependence of the coplanar-coil response, including the
   exact weak-induction factor $r/\sqrt{r^2+4h^2}$, and **state** why the primary
   field is height independent for a transmitter and receiver at the same height.
2. **Quantify** the height–conductivity trade-off from measured sensitivities,
   and **state** the height accuracy required for a stated conductivity accuracy.
3. **Compute** the masking effect of a conductive overburden on a target anomaly
   and **explain** why it is a conductance problem, not a noise problem.
4. **Determine** the frequency channel that carries the most information about a
   target at a given depth, and **state** the implications for system bandwidth.
5. **Estimate** the survey cost of flying higher, in terms of stacking and
   passes, from a stated signal-to-noise target.
6. **Distinguish** the quantity an airborne conductivity map measures from a
   rock property, and **name** the five largest sources of that gap.
7. **Specify** a levelling and quality-control procedure that would expose a
   height-correlated bias in a delivered conductivity map.

## Prerequisites

- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the response integral, the skin depth and the induction number.
- [08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods](03-em-modelling.md)
  — the layered solver and the effect of a height unknown.
- [08-05-04 EM Inversion and Dimensionality](04-em-inversion.md) — what the
  per-sounding inversion can and cannot resolve.

## 1. The airborne measurement

A transmitter coil on a towed bird induces currents in the ground; receiver coils
measure the secondary field after the free-space primary has been bucked
(frequency domain) or after the transmitter has switched off (time domain). Three
consequences of flying the system follow immediately:

- The **geometry is known only to the accuracy of the navigation and the
  altimeter**: radar or laser altitude to the ground typically $0.1$–$1\ \mathrm{m}$
  over favourable terrain, worse over vegetation, and the bird's attitude varies
  along the line.
- The **footprint is large**: a bird at $40\ \mathrm{m}$ with an $8\ \mathrm{m}$
  coil separation responds to a volume whose lateral extent is tens of metres, so
  the mapping resolution is not the line spacing.
- The **coupling is weak**: at $40\ \mathrm{m}$ the signal is a few per cent of
  what the same system measures on the ground (Section 2).

The product is usually an **apparent conductivity** or a conductivity–depth
section obtained by inverting each sounding independently, with a one-dimensional
model, and then interpolating between lines. Everything that follows is about how
much structure that procedure can and cannot support.

## 2. Height enters as a geometric factor

### 2.1 The kernel

With the transmitter and receiver both at height $h$ above the ground, the
vertical magnetic field of the layered ground at the receiver is, in the Hankel
domain, multiplied by $\exp(-2\lambda h)$: one factor of $\exp(-\lambda h)$
carries the source down to the ground at a given horizontal wavenumber $\lambda$,
and one carries the response back up. From
[08-05-03](03-em-modelling.md) §2.3 the coplanar response is therefore

$$S(\omega,h)=-r^3\left[
\frac{R_\infty}{\sqrt{r^2+4h^2}}
+\int_0^\infty\left(\lambda^2R(\lambda)-R_\infty\right)
e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda\right],$$

and the weak-induction limit of the first term is

$$\boxed{\;S_{\text{LIN}}=\frac{k^2r^2}{4}\cdot
\frac{r}{\sqrt{r^2+4h^2}},\qquad
S_{\text{LIN}}(h=0)=\frac{k^2r^2}{4},\;}$$

so height multiplies the response by a factor between $1$ and $1/(2h/r)$. **The
primary field is unaffected**: for a transmitter and receiver at the same height,
the free-space primary is $H_p=-m/(4\pi r^3)$ independent of $h$, so the ratio
$S=H_s/H_p$ is a true signal loss and not a change of reference.

### 2.2 Measured height dependence

SYNTHETIC system: $r=8\ \mathrm{m}$, halfspace $\sigma=0.05\ \mathrm{S\,m^{-1}}$;
the table gives the ratio of the response at height $h$ to the response at
$h=0$.

| $h$ (m) | ratio at 1 kHz | ratio at 1 Hz | weak-induction factor |
|---|---|---|---|
| 0 | 1.0000 | 1.0000 | 1.0000 |
| 2 | 0.8854 | 0.8940 | 0.8944 |
| 5 | 0.5890 | 0.6233 | 0.6247 |
| 10 | 0.3151 | 0.3691 | 0.3714 |
| 20 | 0.1349 | 0.1932 | 0.1961 |
| 40 | 0.0474 | 0.0963 | 0.0995 |
| 60 | 0.0232 | 0.0632 | 0.0665 |

At $1\ \mathrm{Hz}$ (induction number $0.011$) the measured ratios reproduce the
analytic factor to a few per cent — the residual is the $O(\theta)$ correction
measured in [08-05-01](01-frequency-domain-em.md) §7(c). At $1\ \mathrm{kHz}$
($\theta=0.11$) the response has fallen well *below* the weak-induction factor,
because height also enters the correction term. Both columns are geometry: the
ground is identical in every row.

**Read the last row.** A bird at $60\ \mathrm{m}$ keeps $2\%$ of the signal the
same system would see on the ground. Altitude is not a correction applied at the
end of processing; it is the largest single factor in the signal budget.

## 3. The height–conductivity trade-off

Height and conductivity both change the response, and over a range of conditions
they change it in nearly the same way, which makes them tradeable. Measure the
relative sensitivities by finite differences on the layered solver and form

$$\text{trade-off}=\frac{\partial\ln|S|/\partial h}
{\partial\ln|S|/\partial\ln\sigma}
\quad\text{[per metre]},$$

i.e. the fractional conductivity change that produces the same response change as
one metre of height:

| $h$ (m) | 400 Hz | 1.6 kHz | 6.4 kHz | 25.6 kHz |
|---|---|---|---|---|
| 20 | 7.29% | 9.62% | 14.40% | 24.97% |
| 40 | 4.91% | 7.31% | 12.57% | 24.74% |
| 60 | 4.08% | 6.59% | 12.30% | 25.54% |

($\sigma=0.05\ \mathrm{S\,m^{-1}}$, $r=8\ \mathrm{m}$; each entry is the
percentage change in $\sigma$ equivalent to $1\ \mathrm{m}$ of height error.)

Three design statements follow directly.

- **A $1\ \mathrm{m}$ height error is a $4$–$25\%$ conductivity error.** An
  altimeter accurate to $0.1\ \mathrm{m}$ reduces this to $0.4$–$2.5\%$, which is
  comparable with the noise-driven uncertainty of a single sounding.
- **The trade-off grows with frequency.** The high-frequency channels, which carry
  the shallow information and are the ones a conductivity map is usually built
  from, are exactly the ones most sensitive to height. This is why an airborne
  system's useful upper frequency is set by its altimeter, not by its electronics.
- **The trade-off is not a constant that can be calibrated out.** It varies with
  height and frequency along a line, so a *relative* levelling (Section 6) removes
  the line-to-line part of the bias, not the bias itself.

The practical inversion includes the height as a free parameter with a prior from
the altimeter, or inverts for a flight-height correction. Either way, the answer's
conductivity accuracy is bounded by the height accuracy, and the bound is the
table above.

## 4. Overburden masking

A conductive cover — saprolite, clay, saline groundwater, wet soil — attenuates
the response of everything beneath it. SYNTHETIC test: a target layer of
$0.5\ \mathrm{S\,m^{-1}}$ and $20\ \mathrm{m}$ thickness with its top at
$60\ \mathrm{m}$, in a $0.01\ \mathrm{S\,m^{-1}}$ host, measured at $1\ \mathrm{kHz}$
from a bird at $40\ \mathrm{m}$; a $40\ \mathrm{m}$ cover of variable conductivity
sits above the target.

| cover $\sigma$ (S/m) | cover conductance $\sigma d$ (S) | target anomaly (ppm) | relative to no cover |
|---|---|---|---|
| $10^{-6}$ | 0.0000 | 77.83 | 1.000 |
| $0.02$ | 0.8 | 67.56 | 0.868 |
| $0.05$ | 2.0 | 52.55 | 0.675 |
| $0.20$ | 8.0 | 17.33 | 0.223 |
| $0.50$ | 20.0 | 3.92 | 0.050 |
| $1.00$ | 40.0 | 0.72 | 0.009 |

The masking is governed by the cover's **conductance** $\sigma d$, not by its
conductivity or its thickness separately: a $2\ \mathrm{S}$ cover passes $68\%$ of
the anomaly, a $20\ \mathrm{S}$ cover $5\%$. Two implications:

- **It is not a signal-to-noise problem.** More stacking cannot recover a target
  whose response has been attenuated by a factor of $20$, because the attenuation
  multiplies signal and noise alike from the ground's point of view; the target's
  contribution is simply a smaller fraction of what the receiver sees.
- **The remedy is frequency.** Higher frequency has a shorter in-ground
  wavelength and therefore sees the cover more than the target — which is the
  opposite of what is wanted — but it also reduces the *relative* weight of the
  deep, screened part of the response. In practice the diagnosis is a
  conductance–depth trade-off (exactly the ambiguity measured in
  [08-05-03](03-em-modelling.md) §5): a cover whose conductance is uncertain makes
  the target's depth and conductance uncertain in a correlated way.

## 5. Depth of investigation and the useful band

SYNTHETIC test: a thin conductive sheet (conductance $2\ \mathrm{S}$, thickness
$4\ \mathrm{m}$) buried in a $0.01\ \mathrm{S\,m^{-1}}$ halfspace, bird at
$40\ \mathrm{m}$, $r=8\ \mathrm{m}$. The tabulated quantity is the **relative**
anomaly $|S_{\text{sheet}}-S_{\text{host}}|/|S_{\text{host}}|$ in per cent — the
absolute difference would be dominated by the host response at high frequency and
would say nothing about detectability.

| depth (m) | 100 Hz | 400 Hz | 1.6 kHz | 6.4 kHz | 25.6 kHz | 100 kHz |
|---|---|---|---|---|---|---|
| 10 | 325.2 | 332.7 | 292.6 | 179.9 | 75.0 | 24.2 |
| 30 | 165.2 | 158.0 | 118.9 | 56.5 | 15.3 | 1.3 |
| 60 | 78.1 | 67.1 | 40.4 | 13.0 | 1.4 | 0.5 |
| 120 | 27.1 | 18.7 | 7.3 | 1.0 | 0.2 | 0.5 |
| 240 | 6.4 | 2.9 | 0.5 | 0.1 | 0.2 | 0.5 |

The channel carrying the largest anomaly moves downward in frequency as the target
deepens: $400\ \mathrm{Hz}$ at $10\ \mathrm{m}$, and $100\ \mathrm{Hz}$ — the
lowest channel in this synthetic system — for every depth from $30\ \mathrm{m}$
down. **For the deeper targets the optimum lies below the system's band**, which
is the practical statement that a system built for shallow targets cannot be
pushed to deep ones by processing. The rule of thumb is the skin-depth argument of
[08-05-01](01-frequency-domain-em.md) applied to a target rather than to a
sounding curve: the channel whose diffusion length is comparable with the target
depth carries the most information about it.

Note also the fine structure at low anomaly levels (the $240\ \mathrm{m}$ row is
not monotone in frequency): at a few tenths of a per cent, the "anomaly" is
comparable with the numerical resolution of the model itself, which is why the
resolution check of [08-05-03](03-em-modelling.md) §7.3 belongs in any
depth-of-investigation claim.

## 6. Noise, height and survey cost

With a SYNTHETIC receiver noise of $20\ \mathrm{ppm}$ per sample, the
signal-to-noise of one stack at $1\ \mathrm{kHz}$ over the same halfspace is
$35.4$ at $20\ \mathrm{m}$, $11.3$ at $40\ \mathrm{m}$ and $5.0$ at $60\ \mathrm{m}$.
To reach a target signal-to-noise of $20$ therefore requires $1.0$, $3.1$ and
$16.1$ stacked passes respectively: the signal falls as the geometric factor of
Section 2 while the noise does not, so **height is paid for in survey time, with
a squared cost**.

Two survey-design consequences and one quality-control procedure:

- **Line spacing is a footprint question, not a wavelength question.** The
  lateral support of the measurement is set by the height and the separation, so
  the maximum useful line spacing is of the order of that support. Flying more
  closely spaced lines than the footprint does not add resolution; it adds
  correlation.
- **Tie lines are not a formality.** A grid crossed by perpendicular tie lines is
  how a height-correlated bias is exposed: if a levelling adjustment needed to
  reconcile the lines is proportional to flight height, the conductivity map is
  carrying an altimeter error (Section 3).
- **Levellings must not hide the trade-off.** Multiplying each line's data by a
  constant to match tie-line values removes line-to-line amplitude bias, and with
  it any real geological contrast that happens to run parallel to the flight
  direction. The adjusted data must be reported alongside the raw.

**The gap between a map and a rock.** Five sources, in decreasing order of
magnitude for typical surveys: (1) the one-dimensional assumption applied to
structures that are not layered (Section 6 of
[08-05-04](04-em-inversion.md) measures the consequence); (2) height errors and
their trade-off with conductivity (Section 3); (3) the conductance–depth
equivalence of thin conductors (Section 4 and
[08-05-03](03-em-modelling.md) §5); (4) the footprint, which smooths structure
smaller than tens of metres into a single apparent value; (5) cultural metal,
which is a perfect conductor and therefore produces a large, spatially incoherent
anomaly. A conductivity map is a *measurement* of the EM response and a *model* of
the ground, and the two must be labelled separately.

## 7. Assumptions and regime of validity

1. **Quasi-static**: $\omega\varepsilon_0/\sigma\ll1$, verified in
   [08-05-01](01-frequency-domain-em.md). Fails in resistive dry rock or ice at
   the top of a high-frequency band.
2. **Dipole approximation**: the finite coil radii must be small compared with
   both the separation and the height; the error was measured in
   [08-05-01](01-frequency-domain-em.md) §4 ($0.57\%$ at $a/s=0.05$, $10\%$ at
   $a/s=0.2$). At $8\ \mathrm{m}$ separation with $1\ \mathrm{m}$ coils, $a/s=0.125$:
   a few per cent.
3. **Flat ground at zero height datum**: topography along the line changes the
   effective height of every sounding independently, which is the same trade-off
   as Section 3 with a topographic error. Dragged-bird geometry and irregular
   terrain make this the largest unmodelled term in steep country.
4. **Layered ground**: the inversion of Section 4 is one-dimensional per sounding.
   Two-dimensional and three-dimensional targets produce responses that a 1-D
   model reproduces with a smooth, wrong structure.
5. **Non-magnetic ground**: susceptibility responses add an in-phase term (see
   [08-03-02](../03-magnetic-anomalies-and-modelling/02-koenigsberger-and-remanence.md));
   in magnetic terrain they must be separated from the conductivity response,
   which needs the multi-frequency or time-domain decay shape.
6. **The primary is removed.** Frequency-domain systems rely on bucking to parts in
   $10^5$ ([08-05-01](01-frequency-domain-em.md) §4); time-domain systems rely on
   a clean switch-off. Both set the smallest usable secondary signal.
7. **The noise is white per sample.** Stacked, correlated noise (bird motion,
   sferics) violates this and inflates the true error beyond the $\sqrt{n}$ rule
   used in Section 6.

## 8. Fully worked numeric example

A target is a $4\ \mathrm{m}$-thick sheet of conductance $2\ \mathrm{S}$ at
$60\ \mathrm{m}$ depth; the survey is flown at $40\ \mathrm{m}$ with
$r=8\ \mathrm{m}$ and $1\ \mathrm{kHz}$; the altimeter is good to $1\ \mathrm{m}$.

1. **Relative anomaly available.** From the table in Section 5, at $1.6\ \mathrm{kHz}$
   the relative anomaly is $40.4\%$; at $1\ \mathrm{kHz}$ (interpolating between
   the $400\ \mathrm{Hz}$ and $1.6\ \mathrm{kHz}$ columns) it is about $50\%$.
   Compare this with the same target at $120\ \mathrm{m}$ depth, where the
   $1.6\ \mathrm{kHz}$ anomaly is $7.3\%$: the deep target is still detectable but
   its anomaly is a factor of $5.5$ smaller.
2. **Conductivity error from height.** At $40\ \mathrm{m}$, $1.6\ \mathrm{kHz}$, the
   trade-off is $7.31\%$ of $\sigma$ per metre, so a $1\ \mathrm{m}$ altimeter error
   contributes $7.31\%$ to the target conductance and depth. Reducing the target's
   anomaly to an *apparent conductivity* at $60\ \mathrm{m}$ and $1.6\ \mathrm{kHz}$
   therefore carries a $7\%$ systematic error unless the height is treated as a
   free parameter with a $1\ \mathrm{m}$ prior.
3. **Stacking.** At $40\ \mathrm{m}$ the single-stack signal-to-noise is $11.3$;
   reaching $20$ needs $\left(20/11.3\right)^2=3.1$ stacks. Since stacking costs
   survey time linearly, the same line flown at $60\ \mathrm{m}$ instead costs
   $16.1\times$ the time for the same final signal-to-noise — an example of the
   squared height cost of Section 6.
4. **What is claimed.** The defensible statement is: "a conductor with conductance
   $2\pm0.4\ \mathrm{S}$ at a depth of $60\pm15\ \mathrm{m}$, the uncertainties
   dominated by the altimeter and by the conductance–depth equivalence, not by
   noise." The indefensible statement is "a rock of conductivity
   $0.5\ \mathrm{S\,m^{-1}}$ at $60\ \mathrm{m}$."

## 9. Python demonstration

`code/airborne_em_demo.py` computes everything above. It:

1. tabulates the response at height against the weak-induction factor, at two
   frequencies;
2. measures the height–conductivity trade-off at three heights and four
   frequencies;
3. measures the masking of a target anomaly by covers of increasing conductance;
4. tabulates the relative anomaly of a buried sheet against depth and frequency
   and reports the best channel for each depth;
5. converts a signal-to-noise target into a stacking and survey-time cost.

It is print-only, uses `np.random.default_rng(20261014)`, needs no network, and
finishes in under a second.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/05-airborne-em-exercises.md`](./exercises/05-airborne-em-exercises.md)
and
[`exercises/05-airborne-em-solutions.md`](./exercises/05-airborne-em-solutions.md).

- **★** Compute the weak-induction height factor for $h=25\ \mathrm{m}$,
  $r=8\ \mathrm{m}$ and state the signal loss in dB.
- **★★** Derive the height factor from the $\exp(-2\lambda h)$ kernel and the
  identity $\int_0^\infty e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda
  =1/\sqrt{r^2+4h^2}$.
- **★★** Using the trade-off table, decide the altimeter specification needed to
  hold the conductivity error below $3\%$ at $6.4\ \mathrm{kHz}$.
- **★★★** Design a levelling and QC procedure for an airborne survey that would
  detect a height-correlated bias in a delivered conductivity map, and state the
  null result that would give you confidence.

## Mastery checkpoint

Without notes:

> A survey at $40\ \mathrm{m}$ with $r=8\ \mathrm{m}$ delivers apparent
> conductivities across a $0.05\ \mathrm{S\,m^{-1}}$ terrain. **(a)** The bird
> height is systematically $2\ \mathrm{m}$ too high in the delivered model. In
> which direction is the conductivity biased, and by roughly how much at
> $1.6\ \mathrm{kHz}$? **(b)** The client wants the map to resolve a
> $2\ \mathrm{S}$-conductance target at $60\ \mathrm{m}$ depth. Is that a
> bandwidth, a height or a processing request? **(c)** State the two quantities you
> would quote for every map cell and why one of them is not a rock property.

## Common pitfalls

1. **Treating height as a post-hoc correction.** It multiplies the signal, and it
   is the largest term in the budget.
2. **Quoting conductivity without the height uncertainty.** The two are
   tradeable, so one is meaningless without the other.
3. **Expecting stacking to defeat an overburden.** Attenuation is multiplicative,
   not additive; the target's contribution is simply smaller.
4. **Read depth from the highest-frequency channel.** The best channel moves to
   lower frequency with depth; deeper than the band, no channel works.
5. **Levelling away the geology.** A constant-per-line adjustment removes real
   contrasts that run parallel to the flight lines.
6. **Calling a footprint-limited map "high resolution".** Lateral resolution is
   set by height and separation, not by line spacing.
7. **Reading one-dimensional inverted conductivity as a rock property.**
   Dimensionality, height, equivalence, footprint and metal all intervene before
   the rock.

## Related modules

- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the response, the induction number and the bucking problem.
- [08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods](03-em-modelling.md)
  — the layered solver used here, and the equivalence classes behind the masking.
- [08-05-04 EM Inversion and Dimensionality](04-em-inversion.md) — per-sounding
  inversion, resolution and the dimensionality error.
- [08-03-02 Koenigsberger Ratio and Remanence Dominance](../03-magnetic-anomalies-and-modelling/02-koenigsberger-and-remanence.md)
  — the magnetic response that accompanies the conductivity response.
- [11-exploration-geophysics](../../11-exploration-geophysics/README.md) — how
  conductivity maps are used in mineral and groundwater exploration.
