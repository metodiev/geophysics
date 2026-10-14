---
id: 10-01-01
title: "GPR Physics: EM Pulses, Dielectric Permittivity and Reflection"
level: intermediate
prereqs: ["02-07-03", "02-07-05", "02-03-08"]
tags: [gpr, near-surface, gpr-principles, maxwell-equations, dielectric-permittivity, reflection-coefficient]
---

# GPR Physics: EM Pulses, Dielectric Permittivity and Reflection

> **All models and data in this module are SYNTHETIC.** The permittivities,
> conductivities and layered models below are chosen teaching values, not
> measurements. The only physical constants used are the speed of light
> $c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$, the vacuum permittivity
> $\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$, the vacuum
> permeability $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ and the static
> relative permittivity of pure water at $20\ ^\circ\mathrm{C}$, $80.1$.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** which quantity a ground-penetrating radar system records, and
   convert between the two-way travel time and depth for a stated wave speed.
2. **Derive** $v = c/\sqrt{\varepsilon_r}$ and
   $\alpha = (\sigma/2)\sqrt{\mu/\varepsilon}$ from Maxwell's equations in the
   low-loss approximation, and **derive** the lossless condition
   $\tan\delta = \sigma/(\omega\varepsilon) \ll 1$.
3. **Compute** the loss tangent for a given conductivity, permittivity and
   frequency, and **decide** whether the low-loss formulas of this module may be
   used at all.
4. **Compute** the normal-incidence reflection and transmission coefficients at a
   dielectric interface and **verify** that the energy fractions sum to one.
5. **Describe** a source pulse by its measured spectrum, and **state** why a
   nominal antenna frequency is a label rather than a bandwidth.
6. **Quantify** the sensitivity of a two-way time to a permittivity error, and
   explain why half of a fractional permittivity error passes into the depth.

## Prerequisites

- [02-07-03 Maxwell's Equations and Their Physical Meaning](../../02-physics/07-electromagnetism/03-maxwell-equations.md) —
  the four equations and what each term means.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../../02-physics/07-electromagnetism/05-em-waves.md) —
  plane waves, wave impedance and the role of $\varepsilon_r$.
- [02-03-08 Reflection, Refraction and Snell's Law for Waves](../../02-physics/03-oscillations-and-waves/08-reflection-refraction.md) —
  the reflection coefficient for a wave crossing an interface.

## 1. What a GPR system actually records

A GPR system is a radar: a transmitter radiates a short electromagnetic pulse
into the ground, and a receiver records the field that returns. What is stored is
a **time series of voltage against time**, after the instrument's own response
and gain have been applied. Everything else — depths, layer thicknesses, water
content, the position of a pipe — is an inference, and every inference imports a
wave speed.

Three arrivals dominate a typical record:

- the **air wave**, the pulse travelling through the air from transmitter to
  receiver at $c$, which arrives first and is used to define time zero;
- the **ground wave**, the pulse travelling through the top layer at $v = c/
  \sqrt{\varepsilon_r}$, which is the first arrival that carries information
  about the ground;
- the **reflections** from interfaces where the permittivity changes, each
  arriving at a two-way time

$$t = \frac{2d}{v}, \qquad d = \frac{v\,t}{2}, \tag{1.1}$$

with $d$ the depth of the interface in metres, $v$ in $\mathrm{m\,ns^{-1}}$ and
$t$ in nanoseconds. Equation (1.1) is the whole of GPR depth conversion, and it
contains one number that the instrument never measures: $v$.

The rest of this lesson derives what $v$ depends on, how strongly, and where the
derivation stops being valid.

## 2. Maxwell's equations in the ground

In a non-magnetic medium with relative permittivity $\varepsilon_r$, conductivity
$\sigma$ and no free charge, Maxwell's equations reduce to the damped wave
equation for the electric field $\mathbf{E}$:

$$\nabla^{2}\mathbf{E} = \mu_0\varepsilon\,\frac{\partial^{2}\mathbf{E}}
{\partial t^{2}} + \mu_0\sigma\,\frac{\partial \mathbf{E}}{\partial t}, \tag{2.1}$$

with $\varepsilon = \varepsilon_0\varepsilon_r$. The two terms on the right are
the two physical processes:

- the second-derivative term is **storage** (displacement current), which
  propagates the wave;
- the first-derivative term is **loss** (conduction current), which absorbs it.

Seek a plane wave $\mathbf{E} = \mathbf{E}_0\exp[i(\omega t - \gamma z)]$ with
complex wavenumber $\gamma = \alpha + i\beta$. Substituting into (2.1):

$$\gamma^{2} = -\omega^{2}\mu_0\varepsilon + i\omega\mu_0\sigma
\;\;\Longrightarrow\;\;
\gamma = i\,\omega\sqrt{\mu_0\varepsilon}\,
\sqrt{1 - i\,\frac{\sigma}{\omega\varepsilon}}. \tag{2.2}$$

Equation (2.2) is exact for a homogeneous, non-magnetic, linear medium. Its real
part $\alpha$ attenuates the field as $\exp(-\alpha z)$; its imaginary part
$\beta$ sets the phase velocity $v = \omega/\beta$.

## 3. The low-loss regime: $v = c/\sqrt{\varepsilon_r}$

Define the **loss tangent**

$$\tan\delta \equiv \frac{\sigma}{\omega\varepsilon}
= \frac{\sigma}{2\pi f\,\varepsilon_0\varepsilon_r}. \tag{3.1}$$

When $\tan\delta \ll 1$ the square root in (2.2) expands as
$\sqrt{1-i\tan\delta} \approx 1 - \tfrac{i}{2}\tan\delta
+ \tfrac{1}{8}\tan^{2}\delta$, giving

$$\beta \approx \omega\sqrt{\mu_0\varepsilon}\,
\left(1 + \frac{\tan^{2}\delta}{8}\right),
\qquad
\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu_0}{\varepsilon}}
\left(1 - \frac{\tan^{2}\delta}{8}\right). \tag{3.2}$$

To leading order the loss vanishes from the speed, and with $\mu_0\varepsilon_0 =
1/c^{2}$:

$$\boxed{\;v = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu_0\varepsilon}}
= \frac{c}{\sqrt{\varepsilon_r}}\;}
\qquad
\boxed{\;\alpha = \frac{\sigma}{2}\sqrt{\frac{\mu_0}{\varepsilon}}
= \frac{\sigma\,\eta_0}{2\sqrt{\varepsilon_r}}\;}, \tag{3.3}$$

where $\eta_0 = \sqrt{\mu_0/\varepsilon_0} = 376.73\ \Omega$ is the impedance of
free space. The first boxed result is the single most-used formula in GPR: **the
speed depends only on the permittivity**, and the second says the loss depends on
the permittivity *and* the conductivity.

Two consequences worth stating plainly:

- The speed is a square-root function of $\varepsilon_r$, so it compresses
  contrast: between dry sand and water the permittivity changes by a factor of
  20 but the speed only by 4.5.
- Conversely, inverting a measured speed for permittivity **amplifies** error:
  $\varepsilon_r = (c/v)^{2}$, so a $10\%$ speed error is a $\left(1.1^{2}-1\right)
  = 21\%$ permittivity error.

## 4. Assumptions and regime of validity

Everything in this lesson, and in every later lesson of the module, rests on
these assumptions. Each is testable, and each is stated where it is used.

1. **Non-magnetic ground** ($\mu_r = 1$). True for soils and rocks to better than
   $0.1\%$; false for steel and for some iron-rich mine waste.
2. **Low loss**, $\tan\delta \lesssim 0.1$. This is the assumption that fails
   first in the field. Section 9 quantifies the cost: at $\tan\delta = 0.2$ the
   low-loss speed is wrong by $0.49\%$, at $\tan\delta = 0.3$ by $1.09\%$, at
   $\tan\delta = 1$ by $9.87\%$ and at $\tan\delta = 2$ by $27.20\%$.
3. **Homogeneous within a layer**, so that a single $\varepsilon_r$ and $v$ apply.
   A gradual moisture profile violates this and produces not a discrete
   reflection but a distributed one.
4. **Negligible relaxation dispersion** over the band. Real water relaxes, so
   $v$ and $\alpha$ vary with frequency; the constant-$\varepsilon_r$ model is an
   average over the band.
5. **Far-field, plane-wave geometry** for the reflection coefficient. Within a
   wavelength of the antenna the near field dominates and (5.1) does not apply.

The practical test is (3.1): compute $\tan\delta$ before using (3.3). Table 1 of
Section 9 shows where the boundary falls.

## 5. Reflection at a dielectric interface

At normal incidence the amplitude reflection coefficient for a non-magnetic
interface follows from the wave impedances
$\eta = \eta_0/\sqrt{\varepsilon_r}$. With
$R = (\eta_2-\eta_1)/(\eta_2+\eta_1)$:

$$\boxed{\;R = \frac{\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2}}
{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}}\;}
\qquad
t_{\mathrm{amp}} = 1 + R = \frac{2\sqrt{\varepsilon_1}}
{\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2}}. \tag{5.1}$$

The energy fractions are $R^{2}$ reflected and $1-R^{2}$ transmitted, and they
must sum to one — a check that catches sign and normalisation errors immediately.

Note what (5.1) does *not* contain: frequency. In the low-loss regime the
reflection coefficient is frequency-independent, which is why GPR reflection
amplitudes can be read as permittivity contrasts at all. In the lossy case the
coefficients become complex and dispersive, and the simple ratio fails.

**Worked example 1 — two interfaces with the same contrast.** A dry sand layer
($\varepsilon_r = 4$) over wet sand ($\varepsilon_r = 9$) over a saturated base
($\varepsilon_r = 16$). Then
$R_{12} = (2-3)/5 = -0.2000$ and $R_{13} = (2-4)/6 = -0.3333$. Both are
negative because both interfaces are increases in permittivity; the sign is
irrelevant to a zero-phase wavelet but matters for polarity-sensitive
interpretation.

## 6. The source pulse in the frequency domain

A GPR antenna does not emit a single frequency. The workhorse model for a
broad-band pulse is the **Ricker wavelet**

$$w(t) = \left[1 - 2\left(\pi f_0 t\right)^{2}\right]
\exp\left[-\left(\pi f_0 t\right)^{2}\right], \tag{6.1}$$

whose amplitude spectrum peaks at $f_0$. Three properties follow analytically and
are measured in the demonstration:

- the spectral **mean** frequency is $\dfrac{2}{\sqrt{\pi}}f_0 = 1.1284 f_0$;
- the spectral **rms bandwidth** is
  $\sqrt{\tfrac{3}{2}-\tfrac{4}{\pi}}\,f_0 = 0.4763 f_0$;
- the first **zero crossing** in time is at
  $t = \dfrac{1}{\sqrt{2}\,\pi f_0} = 0.2251/f_0$, *not* $1/(2f_0)$: the latter
  is the zero crossing of a sine, and confusing them changes a wavelength by
  $11\%$.

The last point is worth a moment. It is common to read that a GPR antenna's
resolution is "one half wavelength at the antenna frequency". Both quantities in
that sentence are conventions: the bandwidth is not a single frequency, and the
resolution criterion is a choice. This module states the criterion every time it
quotes a resolution.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| relative permittivity | $\varepsilon_r$ | 1 | $\varepsilon/\varepsilon_0$ |
| conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | $\mathrm{A\,V^{-1}m^{-1}}$ |
| speed | $v$ | $\mathrm{m\,ns^{-1}}$ | $c/\sqrt{\varepsilon_r}$ |
| depth | $d$ | m | $vt/2$ |
| two-way time | $t$ | ns | $2d/v$ |
| loss tangent | $\tan\delta$ | 1 | $\sigma/(\omega\varepsilon)$ |
| attenuation | $\alpha$ | $\mathrm{m^{-1}}$ | $\mathrm{Np\,m^{-1}}$ |

The useful practical fact is that $c = 0.299792458\ \mathrm{m\,ns^{-1}}$: with
time in nanoseconds and speed in metres per nanosecond, $d = vt/2$ needs no
conversion factors at all. Mixing $\mathrm{m\,ns^{-1}}$ with seconds is the
commonest arithmetic error in the subject.

## 8. Worked examples

**Example 2 — depth conversion is a family, not a number.** A reflection is
picked at $t = 52.04\ \mathrm{ns}$. The dry-sand-and-wet-sand model of Example 1
gives $v_2 = 0.09993\ \mathrm{m\,ns^{-1}}$ in the layer above the reflector, so

$$d = \frac{0.09993 \times 52.04}{2} = 2.600\ \mathrm{m}.$$

With the top-layer speed $v_1 = 0.14990\ \mathrm{m\,ns^{-1}}$ instead the same
pick gives $3.900\ \mathrm{m}$; with a $10\%$ error on $v_1$ it gives
$4.290\ \mathrm{m}$. One measurement, three answers, $65\%$ apart. The
non-uniqueness is in the physics, not the processing.

**Example 3 — how far does a permittivity error propagate?** From $t = 2d\sqrt{
\varepsilon_r}/c$, logarithmic differentiation gives

$$\frac{\delta t}{t} = \frac{1}{2}\frac{\delta\varepsilon_r}{\varepsilon_r}.
\tag{8.1}$$

For $d = 2.0\ \mathrm{m}$ and $\varepsilon_r = 9$ the two-way time is
$2 \times 2.0 \times 3 / 0.299792458 = 40.028\ \mathrm{ns}$. Perturbing the
permittivity by $\pm 10\%$ moves the time by $-5.13\%$ and $+4.88\%$
respectively — the mean of the two is not zero because the relation is not
linear, which is a reminder that "$\pm 10\%$" is not symmetric in the answer.

**Example 4 — reflection and transmission energy.** For $\varepsilon_1 = 4$ and
$\varepsilon_2 = 9$: $R = -0.2000$, $R^{2} = 0.0400$ and $1-R^{2} = 0.9600$.
Ninety-six per cent of the normal-incidence energy crosses the interface. A
useful sanity check on any reflection-coefficient claim is that the two energy
fractions sum to exactly one; in the demonstration the computed sum is
$1.000000$.

## 9. Python demonstration

`code/gpr_physics_demo.py` prints everything in this lesson and is the source of
every number quoted here. It:

1. tabulates $v = c/\sqrt{\varepsilon_r}$ for seven SYNTHETIC media, from air to
   water, giving $0.29979$ down to $0.03350\ \mathrm{m\,ns^{-1}}$;
2. tabulates $R$, $R^{2}$ and $1-R^{2}$ for eight interface pairs and verifies
   the energy sum;
3. tabulates the loss tangent for four conductivities, two permittivities and
   four frequencies, so the reader can see exactly where the low-loss
   approximation stops applying;
4. compares the exact $\alpha$ and $v$ from (2.2) with the low-loss forms (3.3)
   as a function of $\tan\delta$ — the regime-of-validity table of Section 4;
5. measures the Ricker spectrum and compares it with the analytic values of
   Section 6 (measured peak $200.062\ \mathrm{MHz}$ against a $200\ \mathrm{MHz}$
   design value, with a spectral bin spacing of $12.207\ \mathrm{MHz}$; measured
   mean $225.676\ \mathrm{MHz}$ and rms bandwidth $95.239\ \mathrm{MHz}$, both
   matching the analytic expressions to the printed digits);
6. converts a synthetic two-layer model ($16.01\ \mathrm{ns}$ and
   $52.04\ \mathrm{ns}$) to depths at three wave speeds.

Run it before reading further; the arithmetic in this lesson is easier to trust
when you have seen it printed.

## Mastery checkpoint

Without notes:

> A reflection is picked at $t = 30.0\ \mathrm{ns}$ in a soil with
> $\sigma = 5\times10^{-3}\ \mathrm{S\,m^{-1}}$ and $\varepsilon_r$ believed to
> be $9$ at an antenna frequency of $200\ \mathrm{MHz}$.
> **(a)** Compute $\tan\delta$ and decide whether the low-loss formulas apply.
> **(b)** Compute the two-way time that a $2.00\ \mathrm{m}$ deep reflector would
> produce, and check the consistency of the assumed permittivity.
> **(c)** Compute the depth corresponding to the $30.0\ \mathrm{ns}$ pick.
> **(d)** State the depth error for a $10\%$ permittivity error, with its sign.
> **(e)** Compute the reflection coefficient at an interface from this soil into
> a body of water ($\varepsilon_r = 80.1$) and check the energy sum.

Parts (a)–(e) are worked in
[`exercises/01-gpr-physics-solutions.md`](./exercises/01-gpr-physics-solutions.md).

## Common pitfalls

1. **Quoting a depth without its velocity.** $d = vt/2$ has two unknowns and the
   instrument measures one of them.
2. **Using $v = c/\sqrt{\varepsilon_r}$ in a lossy medium.** Check the loss
   tangent first; above $\tan\delta \approx 0.3$ the formula is no longer good to
   one per cent.
3. **Treating an "antenna frequency" as a bandwidth.** A $200\ \mathrm{MHz}$
   antenna may carry usable energy from $98$ to $317\ \mathrm{MHz}$ — a
   fractional width of about $1.1$. Resolution questions must be asked of the
   band, not the label.
4. **Forgetting that permittivity is inverting a square root.** A $10\%$ speed
   error becomes a $21\%$ permittivity error.
5. **Mixing units of speed.** $\mathrm{m\,ns^{-1}}$ and $\mathrm{m\,s^{-1}}$
   differ by $10^{9}$; pick one and write it down.

## Related modules

- [20-signal-processing](../../20-signal-processing/README.md) — the band,
  sampling and convolution used in later lessons of this module.
- [Module 10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md) —
  what is done to these records after they are recorded.
- [08-05 Controlled-Source Electromagnetics](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md) —
  the same Maxwell equations in the diffusive rather than the wave regime.
- [09-01 Electrical Properties of Earth Materials](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md) —
  measured permittivity and conductivity ranges, and why they vary so much.

Materials for this lesson: [`code/gpr_physics_demo.py`](./code/gpr_physics_demo.py),
[`exercises/01-gpr-physics-exercises.md`](./exercises/01-gpr-physics-exercises.md)
and [`exercises/01-gpr-physics-solutions.md`](./exercises/01-gpr-physics-solutions.md).
