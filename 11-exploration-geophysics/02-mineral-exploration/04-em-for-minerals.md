---
id: 11-02-04
title: "EM for Conductors, Massive Sulphides and Graphite"
level: graduate
prereqs: ["09-01-01", "08-05-02", "11-02-01"]
tags: [exploration-geophysics, mineral-exploration, electromagnetics, conductivity, tem, ambiguity]
---

# EM for Conductors, Massive Sulphides and Graphite

Electromagnetic methods are the most direct tool available for sulphide
exploration, because a massive sulphide body is one of the few things in the
crust that conducts electricity well. The catch is stated in the title of this
lesson: **so is graphite, and the two are the same target to EM.** The physics
that makes EM sensitive is also the physics that makes it ambiguous, and both come
from a single fact — a diffusive field in a conductor responds to *conductance*
and to a *time constant*, not to mineralogy. This lesson derives the skin depth,
proves the exact conductance degeneracy, derives and numerically verifies the
conductor time constant, measures why a short time window cannot separate a
target from its host, and quantifies the trade-off between target coupling and
overburden screening.

**All models and data in this module are SYNTHETIC.** Resistivities, conductances,
sizes, overburden parameters, noise floors and time windows are chosen teaching
values, not measurements or properties of any real deposit.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the skin depth from the diffusive Helmholtz equation and **use** it
   to decide whether a target is a compact inductor or part of a conducting host.
2. **Prove** the thin-sheet conductance degeneracy and **state** what measurement
   would break it.
3. **Derive** the decay time constant of a conducting sphere,
   $\tau = \mu_0\sigma a^{2}/\pi^{2}$, from the lowest diffusion mode, and
   **verify** it by solving the radial diffusion equation numerically.
4. **Compute** the $(\sigma,a)$ pairs that share a time constant and **explain**
   the resulting ambiguity.
5. **Measure** how the length of a late-time window controls whether an
   exponential target response can be distinguished from a power-law host
   response.
6. **Compute** the coupling, attenuation and screening terms of a target index,
   and **explain** the frequency trade-off between induction strength and
   overburden screening.
7. **State** which additional property separates a sulphide from a graphite
   response, and why conductivity alone cannot.

## Prerequisites

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — the property being measured and its ranges.
- [08-05-02 Time-Domain EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/02-time-domain-em.md)
  — the measurement geometry and the transient response.
- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — where conductivity sits in the signature vector.

## 1. Skin depth: the one equation that governs everything

In a good conductor with negligible displacement current the field obeys
$\nabla^{2}\mathbf{E} = i\omega\mu_0\sigma\mathbf{E}$, whose plane-wave solution is
$e^{-z/\delta}$ with

$$\boxed{\;\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}} = \sqrt{\frac{\rho}
{\pi f \mu_0}}\;}$$

The demonstration checks the algebra against the numerical wavenumber
$\mathrm{Im}\,k$ of the same operator: at $25$, $100$ and $2000\ \mathrm{Hz}$ the
two agree to within $2.3\times10^{-13}\ \mathrm{m}$, which is rounding.

For the SYNTHETIC targets of this lesson ($a = 120\ \mathrm{m}$, host
$300\ \Omega\,\mathrm{m}$):

| $f$ (Hz) | sulphide 1 Ω m (m) | graphite 0.5 Ω m (m) | disseminated 30 Ω m (m) | strong conductor 0.02 Ω m (m) |
|---|---|---|---|---|
| 25 | 100.7 | 71.2 | 551.3 | 14.2 |
| 100 | 50.3 | 35.6 | 275.7 | 7.1 |
| 400 | 25.2 | 17.8 | 137.8 | 3.6 |
| 2000 | 11.3 | 8.0 | 61.6 | 1.6 |

The host skin depth at $100\ \mathrm{Hz}$ is $871.7\ \mathrm{m}$, an order of
magnitude larger than the target's. **The ratio $\delta_{\text{target}}/a$ is the
qualitative discriminator:** when it is much less than 1 the induced currents are
confined inside the body, which then behaves as a *compact inductor* with its own
time constant; when it approaches or exceeds 1 the body is simply part of the host
and the host's response dominates.

## 2. The conductance degeneracy is exact

For a body whose thickness $t$ is small compared with its lateral extent and with
the skin depth, the induced current is a *sheet current* whose density is set by
the electric field times the total conductivity-thickness product. The response
therefore depends on

$$S = \sigma t \qquad (\mathrm{S}, \text{siemens, the ``conductance''})$$

and **not** on $\sigma$ and $t$ separately. The demonstration computes the
response index of four sheets with $\sigma t = 100\ \mathrm{S}$:

| $\sigma$ (S m⁻¹) | $t$ (m) | $S$ (S) | response index |
|---|---|---|---|
| 1.0 | 100.00 | 100.0 | 1.00000×10⁻⁵ |
| 10.0 | 10.00 | 100.0 | 1.00000×10⁻⁵ |
| 100.0 | 1.00 | 100.0 | 1.00000×10⁻⁵ |
| 1000.0 | 0.10 | 100.0 | 1.00000×10⁻⁵ |

**The spread across the four is exactly zero** — not small, zero, because the
dependence on $S$ alone is structural. A $100\ \mathrm{m}$ thickness with
$\sigma = 1\ \mathrm{S\,m^{-1}}$ and a $0.1\ \mathrm{m}$ film with
$\sigma = 1000\ \mathrm{S\,m^{-1}}$ are indistinguishable, at any frequency,
with any noise level, forever. This is not a resolution limit that better
instrumentation can push: it is a degeneracy of the physics, and only a
measurement of the *physical* thickness — drilling, or an array whose geometry
resolves the two independently — can break it.

The same argument explains why EM cannot report a conductivity for a sheet
target: reported "conductivity" values for conductive units are almost always
conductivities *for an assumed thickness*, and the assumption is rarely stated.

## 3. The time constant of a compact conductor

Because the geometry is discrete, a compact conductor has a spectrum of decay
modes rather than a single response. For a sphere of radius $a$ the lowest mode
of the diffusion equation in spherical coordinates is $j_1(\pi r/a)$ — the
spherical Bessel function with its first zero at the surface — so the decay rate is

$$k^{2}D = \left(\frac{\pi}{a}\right)^{2}\frac{1}{\mu_0\sigma}
\;\Longrightarrow\;
\boxed{\;\tau = \frac{\mu_0 \sigma a^{2}}{\pi^{2}}\;}$$

for the magnetic field. The **measured** consequences for
$a = 120\ \mathrm{m}$:

| target | $\rho$ (Ω m) | $\sigma$ (S m⁻¹) | $\tau$ (ms) | corner $1/(2\pi\tau)$ (Hz) |
|---|---|---|---|---|
| massive sulphide | 1.00 | 1.00 | 1.833 | 86.8 |
| graphite schist | 0.50 | 2.00 | 3.667 | 43.4 |
| disseminated sulphide | 30.00 | 0.033 | 0.061 | 2604 |
| strong conductor (0.02 Ω m) | 0.02 | 50.0 | 91.67 | 1.7 |

The demonstration verifies $\tau$ twice: analytically against the corner
frequency of the induction-number response ($\omega\tau = 1$ at
$86.8056\ \mathrm{Hz}$, matching $1/(2\pi\tau)$ to $1.4\times10^{-14}\
\mathrm{Hz}$), and numerically by solving the radial diffusion equation inside
the sphere and measuring the late-time decay rate: **$1.8335\ \mathrm{ms}$
measured against $1.8335\ \mathrm{ms}$ closed form, a relative difference of
$0.000\%$.** The numerical route shares no algebra with the derivation, so the
agreement is evidence rather than tautology.

### The $(\sigma,a)$ trade-off

Since $\tau \propto \sigma a^{2}$, a **four-times-larger body with one-sixteenth
of the conductivity has exactly the same time constant**:

| radius (m) | required $\rho$ (Ω m) for $\tau = 1.833$ ms | resulting $\tau$ (ms) |
|---|---|---|
| 60 | 0.2500 | 1.833 |
| 120 | 1.0000 | 1.833 |
| 240 | 4.0000 | 1.833 |
| 480 | 16.0000 | 1.833 |

Two consequences, both central to interpretation:

1. **A decay time is not a conductivity.** Converting a measured $\tau$ into a
   conductivity requires an assumed radius, and the radius enters squared; a
   $40\%$ error in radius is a factor-$2$ error in conductivity.
2. **The sulphide/graphite separation is not available from $\tau$.** In the
   table above graphite's $\tau$ is $3.667\ \mathrm{ms}$ against the sulphide's
   $1.833\ \mathrm{ms}$ — a factor of exactly two, *and* a factor of two follows
   equally well from a $41\%$ change in the assumed radius. The two hypotheses
   are not separable from a decay curve alone.

## 4. Target versus host: it is the shape of the decay, and the window

A compact conductor decays **exponentially** in the late time. A uniform
conductive host decays as a **power law**; for a uniform half-space the standard
late-time asymptotic form of the step response is

$$V(t) \;\propto\; \sigma^{3/2}\,t^{-5/2}.$$

This is quoted as the standard result; the demonstration verifies its
consequences rather than re-deriving it. The practical question is how long a
window is needed to tell an exponential from a power law. Fitting an exponential
$Ae^{-t/\tau}$ to the power law (and a power law to the exponential) over windows
of increasing length, for a target with $\tau = 1.833\ \mathrm{ms}$:

| window (decades) | $t$ range (ms) | fitted $\tau$ (ms) | relative rms misfit |
|---|---|---|---|
| 0.25 | 0.92–1.63 | 0.496 | 3.1% |
| 0.50 | 0.92–2.90 | 0.689 | 11.9% |
| 1.00 | 0.92–9.17 | 1.435 | 45.3% |

Over a quarter-decade window the exponential fits the host's power law to $3\%$,
and the fitted time constant ($0.496\ \mathrm{ms}$) is not even the target's
($1.833\ \mathrm{ms}$). Over one decade the misfit reaches $45\%$, and beyond
roughly two decades the exponential has decayed below any measurable level, so
the two shapes become trivially distinguishable only because one of them has
vanished.

**The discriminating window is therefore a narrow band, of order one to two
decades of decay**, and this is the quantitative reason why: (a) broadband
(time-domain or multi-frequency) systems are used, (b) a single-window
measurement cannot classify a conductor at all, and (c) the *choice* of late-time
window is an interpretation decision that must be reported, because the fitted
$\tau$ — and hence the inferred conductivity — changes by a factor of three
across the windows in the table above.

## 5. Coupling, attenuation, screening and the frequency trade-off

The demonstration uses a target index of the same multiplicative form as in
[11-01-02](../01-exploration-workflow/02-targeting-and-strategy.md), extended with
an overburden screening factor:

$$\text{index} = \underbrace{\left(\frac{a}{z}\right)^{3}}_{\text{coupling}}
\times \underbrace{e^{-2z/\delta_{\text{host}}}}_{\text{host attenuation}}
\times \underbrace{\frac{\omega\tau}{\sqrt{1+(\omega\tau)^{2}}}}_{\text{induction}}
\times \underbrace{\frac{1}{1+\mu_0\omega S z/2}}_{\text{screening}} ,$$

where $S$ (S) is the overburden conductance and the screening factor is the
standard thin-sheet form. Measured, for $S = 5\ \mathrm{S}$ and $a = 120\
\mathrm{m}$:

| $z$ (m) | sulphide | graphite | disseminated | screen at 25 Hz | 100 Hz | 2000 Hz |
|---|---|---|---|---|---|---|
| 100 | 1.0374 | 1.2602 | 0.0527 | 1.05 | 1.20 | 4.95 |
| 250 | 0.0471 | 0.0572 | 0.0024 | 1.12 | 1.49 | 10.87 |
| 400 | 0.0081 | 0.0099 | 0.0004 | 1.20 | 1.79 | 16.79 |
| 700 | 0.0008 | 0.0009 | 0.0000 | 1.35 | 2.38 | 28.63 |

Two different effects of a conductive overburden, both now quantified:

1. **Screening.** At $25\ \mathrm{Hz}$ and $250\ \mathrm{m}$ the screen is only
   $1.12$: at low frequency the overburden is mainly a competing *response*. At
   $2000\ \mathrm{Hz}$ and the same depth the screen is $10.9$, and at
   $400\ \mathrm{m}$ it is $16.8$ — the target response is divided by an order of
   magnitude.
2. **The frequency trade-off has no free setting.** Higher frequency strengthens
   the induction term for a *small or weakly conducting* target (the
   $\omega\tau$ factor rises toward 1) but multiplies the screening term, and
   lowers $\delta_{\text{host}}$ so that attenuation through the host grows as
   well. **The optimum frequency is a property of the target-and-overburden
   combination, which is why a survey configuration that works in one terrain can
   fail in another with identical targets.**

## 6. Worked example — the graphite false positive

A SYNTHETIC airborne EM survey defines an isolated, strongly conductive anomaly.
Four candidate causes, with the index values of §5 at $250\ \mathrm{m}$ and the
property contrasts of [11-02-01](01-deposit-signatures.md):

| target | EM index at 250 m | magnetics (nT) | IP chargeability (mV/V) |
|---|---|---|---|
| massive sulphide | 0.04706 | 208.0 | 12.0 |
| graphite schist | 0.05717 | 4.0 | 3.0 |
| disseminated sulphide | 0.00239 | 60.0 | 15.0 |
| strong conductor (0.02 Ω m) | 0.06231 | 10.0 | 5.0 |

1. **EM alone.** Graphite and massive sulphide differ by $21\%$ in the EM index —
   and a $10\%$ error in the assumed radius moves the index by more than that,
   through the $a^{2}$ in $\tau$. On top of that, the *same* index is produced by
   any $(\sigma,t)$ pair on the conductance line of §2. **EM cannot distinguish
   them, and the reason is structural, not a matter of data quality or
   processing.**
2. **Magnetics resolves it here.** $208\ \mathrm{nT}$ against $4\ \mathrm{nT}$ is a
   factor of $50$, because the sulphide body carries pyrrhotite-scale
   susceptibility in this SYNTHETIC table and graphite does not. Where the
   sulphide is non-magnetic (pyrite-dominated, or above the Curie depth of its
   magnetite), this test fails.
3. **IP resolves it differently.** Chargeability responds to polarisable grain
   *surface area*, and graphite is far less polarisable per unit conductance than
   sulphide — treated in [11-02-06](06-ip-for-minerals.md). This is the standard
   second discriminator when magnetics is uninformative.

**The honest statement.** "The anomaly is a conductor with a late-time decay
consistent with a time constant of $2$–$4\ \mathrm{ms}$; its conductance is
$\ge 50\ \mathrm{S}$ for any thickness under $20\ \mathrm{m}$; the magnetics
excludes a magnetic sulphide assemblage; the graphite hypothesis cannot be
excluded without an IP or geological test." Note what has *not* been claimed:
conductivity, thickness, or tonnage.

## 7. Assumptions and regime of validity

1. **No induced polarisation.** The response is treated as purely inductive;
   a polarisable ground adds a dispersive conductivity that changes both the
   amplitude and the phase, and the two effects cannot be separated from a
   single-component measurement.
2. **Resistive-limit or circuit-model response.** The conductance argument of §2
   holds in the resistive limit (small induction number); at high induction
   number the geometry of the *current distribution* matters and the degeneracy
   weakens — but the required frequencies are usually unavailable.
3. **Thin sheet, or compact ellipsoid.** Real bodies are neither, and a body whose
   thickness is comparable to its lateral extent has a response that depends on
   both.
4. **Homogeneous, isotropic, flat-lying overburden.** The screening factor used
   here is the thin-sheet form; a thick conductive overburden changes both the
   amplitude and the *shape* of the decay, mimicking a longer target $\tau$.
5. **A known transmitter–receiver geometry.** Offset, orientation and waveform
   all enter the coupling; a discrepancy between modelled and actual geometry
   appears as an apparent conductivity change.
6. **An isolated target.** Two conductors in the same footprint produce a
   composite decay which an inversion will happily fit with one body of
   intermediate $\tau$ — a systematic error that no noise model reveals.
7. **The host power law is quoted, not derived, here.** The $t^{-5/2}$ asymptotic
   form is a standard result of the diffusion problem; deriving it requires the
   half-space solution, which is beyond this lesson.
8. **All numbers SYNTHETIC.** The strongest caution is the one in §2: the
   quantity EM measures first is *conductance*, and turning it into a
   conductivity requires an assumption that the data cannot check.

## 8. Units, dimensional checks and the identities worth memorising

| Quantity | Unit | Check |
|---|---|---|
| conductivity $\sigma$ | S m⁻¹ | 1/Ω m ✔ |
| conductance $S = \sigma t$ | S | S m⁻¹ × m ✔ |
| skin depth $\delta$ | m | $\sqrt{2/(\omega\mu_0\sigma)}$: s /(s⁻¹ H m⁻¹ S m⁻¹) = m² ✔ |
| $\tau = \mu_0\sigma a^{2}/\pi^{2}$ | s | H m⁻¹ × S m⁻¹ × m² = s ✔ |
| index, screen | – | ratios of fields ✔ |

Three identities that make good self-checks on any EM calculation:

1. $\delta = \sqrt{2/(\omega\mu_0\sigma)}$ and $\tau = \mu_0\sigma a^{2}/\pi^{2}$
   must both scale as $\sqrt{\rho}$ and $\rho$ respectively — a check on the
   exponents;
2. the induction response $\omega\tau/\sqrt{1+(\omega\tau)^{2}}$ reaches
   $1/\sqrt{2}$ exactly at $\omega\tau = 1$, which the demonstration confirms to
   $1.4\times10^{-14}\ \mathrm{Hz}$;
3. the screening factor is 1 when either $\omega \to 0$, $S \to 0$ or
   $z \to 0$ — a target at the surface is not screened by a cover above it.

## 9. Exercises

Full sets with worked solutions:
[`exercises/04-em-for-minerals-exercises.md`](exercises/04-em-for-minerals-exercises.md)
and
[`exercises/04-em-for-minerals-solutions.md`](exercises/04-em-for-minerals-solutions.md).

## Mastery checkpoint

Without notes:

> A SYNTHETIC conductor has a measured late-time time constant of
> $5.0\ \mathrm{ms}$ in a host of $200\ \Omega\,\mathrm{m}$, and the target is
> believed to be roughly $150\ \mathrm{m}$ across. **(a)** Compute the
> conductivity and resistivity implied by $\tau = \mu_0\sigma a^{2}/\pi^{2}$ at
> $a = 75\ \mathrm{m}$ (radius), and state the resistivity you would infer if the
> radius were actually $100\ \mathrm{m}$. **(b)** Compute the skin depth in the
> target at $100\ \mathrm{Hz}$ for both conductivities and state whether the body
> is a compact inductor. **(c)** Compute the conductance of a $20\ \mathrm{m}$
> thick sheet with the conductivity of (a), and state the conductivity a
> $2\ \mathrm{m}$ sheet would need for the same EM response. **(d)** Compute the
> overburden screening factor for $S = 10\ \mathrm{S}$ at $100\ \mathrm{Hz}$ and
> $z = 200\ \mathrm{m}$. **(e)** State the one measurement that would distinguish
> graphite from a sulphide body with the same $\tau$.

A worked version is in the
[solutions](exercises/04-em-for-minerals-solutions.md).

## Common pitfalls

1. **Reporting a conductivity from an EM anomaly.** The observable is
   conductance; the conductivity requires a thickness assumption.
2. **Treating a time constant as a conductivity.** $\tau \propto \sigma a^{2}$,
   and the radius is usually the least known parameter.
3. **Choosing the late-time window by habit.** The fitted $\tau$ changes by a
   factor of three across the windows tested in §4.
4. **Believing more EM data will separate graphite from sulphide.** The
   degeneracy is structural; the separation needs a different property.
5. **Ignoring the overburden.** It screens, it responds, and its screen grows with
   frequency — the optimum is target-and-terrain specific.
6. **Fitting one body to a two-body decay.** The result is a plausible
   intermediate $\tau$ and no warning.
7. **Forgetting that polarisation is dispersive.** A polarisable ground has a
   frequency-dependent conductivity, so the derived "conductivity" depends on the
   frequency used to derive it.

## Related modules

- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — the signature vector and the classes this ambiguity applies to.
- [11-02-02 Magnetics for IOCG, Porphyry and Magmatic Sulphides](02-magnetics-for-minerals.md)
  — the discriminator used in §6, and its own failure modes.
- [11-02-06 IP for Disseminated Sulphides and Porphyry Systems](06-ip-for-minerals.md)
  — the property that separates graphite from sulphide where magnetics cannot.
- [08-05 Controlled-Source EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md)
  and [09-05 EM Methods and Applications](../../09-electrical-em-methods/05-em-methods-applications/README.md)
  — the forward modelling and acquisition detail behind this index.
