---
id: 05-04-06
title: "Attenuation and Velocity Dispersion in Rocks"
level: doctoral
prereqs: ["05-04-05"]
tags: [attenuation, q, dispersion, zener, kramers-kronig]
---

# Attenuation and Velocity Dispersion in Rocks

## Learning objectives

1. **Define** the quality factor $Q$ and the attenuation coefficient $\alpha$,
   and state the exact relation between them.
2. **State** the Kramers–Kronig relation and explain why attenuation and
   dispersion are two views of one mechanism.
3. **Derive** the Zener (standard linear solid) response and its limits.
4. **Measure** the peak of $1/Q$ and the asymptotic behaviour numerically, and
   check them against the closed-form limits.
5. **Explain** the consequences of attenuation for survey design: bandwidth,
   resolution, and amplitude-based interpretation.

## Prerequisites

- [05-04-05 Anisotropy in Rocks](./05-anisotropy-rock.md)
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)

## 1. Intuition

A perfectly elastic rock transmits a wavelet unchanged. A real rock loses
energy as it propagates, preferentially at high frequency. Two consequences
follow, and they cannot be separated: the wavelet is attenuated *and* it is
dispersed (different frequencies travel at different speeds). Any model of one
implies the other, by causality.

## 2. Definitions

**Quality factor.** For a harmonic wave,

$$Q = 2\pi\frac{\text{energy stored}}{\text{energy lost per cycle}}.$$

Large $Q$ means low loss. In the weak-attenuation limit the amplitude decays as
$e^{-\alpha x}$ with

$$\alpha \approx \frac{\omega}{2VQ} = \frac{\pi f}{VQ},$$

so $\alpha$ (in np/m) and $Q$ are two descriptions of the same thing. The
dimensionless product $\alpha\lambda = 2\pi/Q$ is the fractional loss per
wavelength — a convenient, unit-free form.

**Attenuation coefficient** $\alpha$: np m⁻¹, often quoted in dB per wavelength
with $1\ \mathrm{np} = 8.686$ dB.

**Dispersion**: $V(\omega)$, caused by the same anelastic mechanism.

**Kramers–Kronig relations**: $Q^{-1}(\omega)$ and $V(\omega)$ are Hilbert
transforms of one another. They are a mathematical consequence of linearity and
causality, not a physical hypothesis. Their practical content: **you cannot
choose dispersion and attenuation independently.** Any code that applies an
attenuation-only operator without a matching velocity change is physically
inconsistent, even if it looks acceptable.

## 3. Derivation: the Zener element

A standard linear solid has a complex modulus

$$M(\omega) = M_R\,\frac{1+i\omega\tau_\varepsilon}{1+i\omega\tau_\sigma},
\qquad \frac{\tau_\varepsilon}{\tau_\sigma} = \frac{M_U}{M_R} = 1+\Delta,$$

where $\Delta$ is the relaxation strength. Then

$$\frac{1}{Q} = \Delta\,\frac{\omega\tau}{1+\omega^2\tau^2},
\qquad \tau = \sqrt{\tau_\varepsilon\tau_\sigma}$$

to first order in $\Delta$. Properties, each of which the demonstration verifies:

1. $1/Q$ peaks at $\omega\tau = 1$, i.e. at $f = 1/(2\pi\tau)$, with value
   $\Delta/2$.
2. $1/Q$ is **symmetric** under $\omega\tau \to 1/(\omega\tau)$: the low- and
   high-frequency asymptotes are mirror images.
3. Low-frequency limit: $1/Q \to \Delta\omega\tau$; high-frequency limit:
   $1/Q\to\Delta/(\omega\tau)$.
4. Total velocity dispersion between the limits:
   $V_U/V_R = \sqrt{M_U/M_R} = \sqrt{1+\Delta}$.

### 3.1 Amplitude decay and Q, derived from a complex modulus

Section 2 quoted $\alpha \approx \omega/(2VQ)$. It follows from the complex
modulus in three lines, and deriving it removes the usual hand-waving about
"energy per cycle".

Let the modulus be complex, $M(\omega) = M'(\omega)\left[1 + i/Q(\omega)\right]$
with $Q \gg 1$, the factor $i$ encoding a response that lags the excitation. The
phase velocity follows from $V = \sqrt{M/\rho}$:

$$\frac{1}{V} = \sqrt{\frac{\rho}{M}} = \sqrt{\frac{\rho}{M'}}
\left(1+\frac{i}{Q}\right)^{-1/2}
\approx \frac{1}{V_0}\left(1 - \frac{i}{2Q}\right),
\qquad V_0 \equiv \sqrt{M'/\rho} .$$

The propagation term is $e^{ikz}$ with $k = \omega/V$:

$$k = \omega\sqrt{\frac{\rho}{M}} \approx \frac{\omega}{V_0}
\left(1 - \frac{i}{2Q}\right)
= \underbrace{\frac{\omega}{V_0}}_{\text{phase}}
- \; i\underbrace{\frac{\omega}{2V_0Q}}_{\alpha} .$$

Since $e^{ikz} = e^{i\omega z/V_0}e^{-\alpha z}$, the amplitude decays as
$e^{-\alpha z}$ with

$$\boxed{\;\alpha = \frac{\omega}{2VQ} = \frac{\pi f}{VQ}\;}$$

Units: $\mathrm{s^{-1}/(m\,s^{-1})} = \mathrm{m^{-1}}$ ✓. And the identity
follows: $\alpha\lambda = 2\pi/Q$, the fractional loss per wavelength.

**Physical interpretation.** The two observable consequences come from the *same*
complex number: its imaginary part is attenuation, its real part is velocity.
Splitting them is a modelling choice, not a physical fact — which is precisely
the content of the Kramers–Kronig constraint in Section 3.3.

### 3.2 $1/Q$ for the Zener element, derived

Section 3 quoted $1/Q = \Delta\,\omega\tau/(1+\omega^2\tau^2)$. Derive it.

The standard linear solid has

$$M(\omega) = M_R\,\frac{1 + i\omega\tau_\varepsilon}{1 + i\omega\tau_\sigma},
\qquad \frac{\tau_\varepsilon}{\tau_\sigma} = \frac{M_U}{M_R} = 1+\Delta .$$

Work with the *compliance* $1/M$, which is easier because the denominator in the
expression for $1/Q$ is a modulus ratio:

$$\frac{1}{M} = \frac{1}{M_R}\cdot
\frac{1+i\omega\tau_\sigma}{1+i\omega\tau_\varepsilon}
= \frac{1}{M_R}\cdot\frac{(1+i\omega\tau_\sigma)(1-i\omega\tau_\varepsilon)}
{1+\omega^2\tau_\varepsilon^2}
= \frac{1}{M_R}\cdot\frac{\left(1+\omega^2\tau_\sigma\tau_\varepsilon\right)
+ i\omega\left(\tau_\sigma-\tau_\varepsilon\right)}
{1+\omega^2\tau_\varepsilon^2} .$$

The loss tangent is the ratio of imaginary to real part:

$$\frac{1}{Q} = \frac{\operatorname{Im}(1/M)}{\operatorname{Re}(1/M)}
= \frac{\omega\left(\tau_\sigma-\tau_\varepsilon\right)}
{1+\omega^2\tau_\sigma\tau_\varepsilon} .$$

Now insert the normalisations. Let $\tau \equiv \sqrt{\tau_\sigma\tau_\varepsilon}$
and expand to first order in the (small) relaxation strength
$\Delta$: $\tau_\sigma \approx \tau(1+\Delta/2)$ and
$\tau_\varepsilon \approx \tau(1-\Delta/2)$, so
$\tau_\sigma-\tau_\varepsilon = \tau\Delta$ and
$\tau_\sigma\tau_\varepsilon = \tau^2(1-\Delta^2/4)\approx\tau^2$. Then

$$\boxed{\;\frac{1}{Q} = \Delta\,\frac{\omega\tau}{1+\omega^2\tau^2}\;}$$

as quoted, with all four properties of Section 3 following from the algebra: the
peak at $\omega\tau = 1$ with value $\Delta/2$, the symmetry under
$\omega\tau\to1/(\omega\tau)$, and the two asymptotes. **Measured verification**
for $\tau = 10^{-3}$ s and $\Delta = 0.10$: the numerical maximum of $1/Q$ sits
at 159.239393 Hz against the closed form $1/(2\pi\tau) = 159.154943$ Hz (relative
difference $5.3\times10^{-4}$, from the finite frequency grid), and the peak value
is $0.050000$ against $\Delta/2 = 0.050000$ ✓.

### 3.3 Kramers–Kronig, and the dispersion budget

Linearity plus causality forces the real and imaginary parts of the modulus to be
Hilbert transforms of one another. The practical consequence for a
**constant-$Q$** medium is a logarithmic velocity dispersion,

$$V(f) = V(f_r)\left[1 + \frac{1}{\pi Q}\ln\frac{f}{f_r}\right],$$

so the velocity change across one decade is $\ln 10/(\pi Q) = 2.3026/(\pi Q)$.

**Numbers.** For $Q = 80$ that is $2.3026/251.3 = 0.92\%$ per decade. Across the
total relaxation range of a single Zener mechanism the dispersion is
$\sqrt{1+\Delta}-1$: for $\Delta = 0.10$, **4.88%** — the value the demonstration
measures.

**Physical interpretation and the practical trap.** A few percent of velocity
dispersion sounds negligible beside the velocity itself (3000 m/s), and it is
negligible for computing a velocity. It is *not* negligible for a travel time:
over a 2 km path at 3 km/s the one-way time is 0.667 s, and 4.88% of that is

$$\Delta t = 0.0488 \times 0.667\ \mathrm{s} = 32.5\ \mathrm{ms}.$$

Thirty-two milliseconds is comparable to a seismic period at 30 Hz (33 ms) and
larger than one at 50 Hz (20 ms). **A modelling error in the velocity of a few
percent becomes a half-cycle timing error over a typical target depth** — enough
to mis-tie horizons, corrupt amplitude-versus-offset gradients and defeat 4-D
difference maps. This is the quantitative reason dispersion may not be dropped
merely because it looks small.

### 3.4 The bandwidth of a single relaxation, derived

How wide in frequency is a Zener absorption peak? The answer is a clean number and
it explains a practical problem with fitting laboratory $Q$ measurements.

Set the derived loss function equal to *half* its peak value. Since the peak is
$\Delta/2$ at $\omega\tau = 1$, the half-maximum condition is

$$\Delta\,\frac{\omega\tau}{1+\omega^2\tau^2} = \frac{\Delta}{4}
\qquad\Longrightarrow\qquad
4\omega\tau = 1+\left(\omega\tau\right)^2 .$$

This is a quadratic in the product $\omega\tau = x$:

$$x^2 - 4x + 1 = 0
\qquad\Longrightarrow\qquad
x = 2 \pm \sqrt{3} = 3.7321 \ \text{ or }\ 0.2679 .$$

**So the half-maximum points sit at $\omega\tau$, 13.93 apart**, i.e.

$$\frac{f_\text{upper}}{f_\text{lower}} = \frac{2+\sqrt3}{2-\sqrt3}
= 3.7321/0.2679 = 13.9282
\qquad\Longrightarrow\qquad
\log_{10}(13.9282) = \mathbf{1.144\ \text{decades}} .$$

**Physical interpretation, and the practical problem.** A single Zener element
absorbs over only about **1.1 decades** of frequency, with $1/Q$ falling as
$f^{-1}$ well above the peak and as $f$ well below it. But measurements on real
rocks characteristically show a $Q$ that is **nearly constant over three or more
decades** — from seismic through sonic to ultrasonic frequencies. A single
relaxation cannot produce that; it requires a *distribution* of relaxation times,
whose combined absorption is flat over the measured band (the Cole–Cole and
Kjartansson formulations are the standard devices).

**The consequence for this lesson's models.** The Zener element is the
*pedagogical unit*: everything about the coupling of attenuation and dispersion is
visible in it, and its limits are checkable in closed form (Section 3.2, verified
numerically). It is **not** the right model for broadband field data, and the
assumption table below says so. Fitting a single Zener element to a multi-decade
$Q$ measurement will produce a Poisson ratio of the fit's residuals — the model
cannot represent the data, and the misfit is the diagnostic.

**The checkable prediction.** Because the peak width is exactly 1.144 decades
regardless of $\Delta$ (the relaxation strength scales the *height* of $1/Q$, not
its width in frequency), **a measured $Q^{-1}$ spectrum whose width differs from
1.14 decades is not a single relaxation.** That is a falsifiable test requiring no
fitting, and it is the kind of model-check this module insists on.

## 4. Units and dimensional analysis

| Quantity | Unit |
|---|---|
| $Q$ | dimensionless |
| $\alpha$ | np m⁻¹ (or dB m⁻¹) |
| $\tau$ | s |
| $\Delta, 1/Q$ | dimensionless |
| $V$ | m s⁻¹ |

Check: $\alpha = \pi f/(VQ)$ has units
$\mathrm{s^{-1}/(m\,s^{-1})} = \mathrm{m^{-1}}$. ✓

## 5. Assumptions

1. **Linearity and causality**, giving Kramers–Kronig.
2. **Weak attenuation** ($Q^{-1}\ll1$) for the approximation
   $\alpha = \pi f/(VQ)$ itself; at very low $Q$ the exact form differs.
3. **A single relaxation mechanism** in the Zener model. Real rocks show a
   broad, near-constant $Q$ over decades of frequency, which requires a
   *distribution* of relaxation times (e.g. the Cole–Cole or Kjartansson
   formulations) — the Zener element is the pedagogical unit, not the whole
   story.
4. **No scattering.** $Q$ here is *intrinsic*; apparent attenuation also
   includes scattering from heterogeneities, which is not anelastic and does not
   obey the same dispersion relation.

### 5.1 Assumptions, and the size of each failure

| Assumption | Failure | Quantified consequence |
|---|---|---|
| Linearity and causality | strongly non-linear response | KK transforms fail; irrelevant at seismic strain amplitudes |
| Single relaxation mechanism | broad, near-constant $Q$ | a Zener element gives a *peak* in $1/Q$; real rocks need a distribution of relaxation times |
| $Q^{-1}\ll1$ for $\alpha = \pi f/(VQ)$ | very low $Q$ | the leading-order form overestimates $\alpha$; use the exact complex modulus |
| Purely intrinsic attenuation | scattering | scattering attenuation does not obey the same dispersion and must be modelled separately |
| $Q$ constant over the band | frequency-dependent $Q$ | the log-dispersion law of Section 3.3 assumes constant $Q$; over decades of frequency a $Q(f)$ model is required |
| Isotropic attenuation | anisotropic $Q$ | common in shales; adds an attenuation-anisotropy parameter usually estimated, not measured |

## 6. Worked examples (measured)

Stated SYNTHETIC Zener element: $\tau = 10^{-3}$ s, $\Delta = 0.10$.

- Measured frequency of the peak of $1/Q$: **159.239393 Hz**.
- Closed form $1/(2\pi\tau)$: **159.154943 Hz**.
- Relative difference: $5.3\times10^{-4}$ (from the finite frequency grid).
- $1/Q$ at the peak: $0.050000$, against $\Delta/2 = 0.050000$ (so
  $Q = 20$).

**Asymptotes** at $\omega\tau = 10^{-3}$ and $10^{3}$: numerical
$Q = 10000.0100$ in both cases against asymptotic 10000.0000. The two test
frequencies are reciprocals, and the numerical $Q$ values agree with each other
exactly as the symmetry property requires. Both match the algebra.

**Velocity dispersion.** Total between the limits:
$\sqrt{1+\Delta}-1 = \sqrt{1.1}-1 = 4.8809\%$. For a $Q$ of about 20
($1/Q = 0.05$) the whole accessible band carries a few percent of velocity
dispersion.

**Why that matters numerically.** A few percent dispersion is small compared
with the velocity itself, but it is exactly the size of the anomalies 4-D
seismic tries to measure (the Gassmann example in
[05-04-03](./03-gassmann-fluid-substitution.md) gave a $V_p$ change of
$+1.07\%$). **Attenuation and saturation effects are of the same order**, which
is why time-lapse interpretation must model both together.

### 6.1 Extended worked example: turning Q into a resolution-versus-depth budget

Attenuation is not a curiosity; it sets the resolution you can achieve at a
given depth. The calculation below is the one to do before promising a target
resolution.

**Model.** Constant $Q$ over the band (an assumption — the lesson's Section 5
flags it), velocity $V = 3000$ m/s, and the weak-attenuation relation
$\alpha = \pi f/(VQ)$ with $Q = 80$. Require the amplitude to survive with a
factor $e^{-1}$ over the path, i.e. $\alpha z = 1$, so

$$f_\text{max}(z) = \frac{VQ}{\pi z}.$$

Then convert to vertical resolution with $\Delta z_\text{res} = V/(4B)$ taking
$B \approx f_\text{max}$:

| depth $z$ (m) | $f_\text{max}$ (Hz) | $\Delta z_\text{res}$ (m) |
|---|---|---|
| 500 | 153 | 4.9 |
| 1000 | 76 | 9.8 |
| 2000 | 38 | 19.6 |
| 4000 | 19 | 39.2 |

**Reading the table.** Resolution degrades *linearly* with depth for a
constant-$Q$ medium — precisely the $1/z$ behaviour predicted, and the same
qualitative conclusion as the potential-field width law of
[05-01-03](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md),
though for a completely different reason. At 4 km, a bandwidth of 19 Hz gives
about 40 m vertical resolution: not the 5–10 m that high-frequency shallow
surveys achieve, and no amount of processing changes it, because the
frequencies are gone.

**Two assumptions that would change the answer.** (i) The value of $Q$: halving
it to 40 halves $f_\text{max}$ at every depth and doubles $\Delta z_\text{res}$.
(ii) The survival criterion. Replacing "a factor of $e^{-1}$" with "a factor of
$e^{-3}$" (a stricter signal-to-noise condition) multiplies $f_\text{max}$ by
1/3 and the resolution length by 3 — a much more pessimistic and often more
realistic budget. State the criterion; it is a modelling choice, not a law.

**Connection to dispersion.** The constant-$Q$ model implies a specific
velocity dispersion (through Kramers–Kronig). For $Q = 80$, the dispersion
across a decade of frequency follows $V(f) = V(f_r)[1+(1/\pi Q)\ln(f/f_r)]$, so
over one decade ($\ln 10 = 2.3026$) the velocity changes by
$2.3026/(\pi\cdot80) = 0.92\%$ — small, but systematically biasing
travel-time-to-depth conversion if ignored over three decades of bandwidth.
Attenuation and dispersion must be applied together.

### 6.2 Worked arithmetic: what ignoring dispersion costs

Take a 2 km target at 3 km/s in a medium with $Q = 80$ (a $Q$ consistent with the
demonstration's relaxation strength of 0.10, which gives $Q = 20$ at the
attenuation peak; use $Q = 80$ for an off-peak, more typical propagation).

| quantity | value |
|---|---|
| one-way travel time, 2 km at 3000 m/s | 0.667 s |
| dispersion across the band, $\sqrt{1+\Delta}-1$ with $\Delta = 0.10$ | 4.88% |
| resulting timing spread | $32.5$ ms |
| period at 30 Hz | 33 ms |
| fraction of a cycle | 0.98 |

**Read the last row.** The dispersion is worth *almost exactly one full cycle* at
30 Hz over this path. A processing chain that applies frequency-independent
velocity while the earth disperses by this amount will stack the 30 Hz component
out of phase with the 100 Hz component over the deeper part of the section —
destroying the very bandwidth that the survey paid for.

**The generalisable rule.** Convert any percentage velocity uncertainty into a
timing error at the target depth *before* deciding it is small:

$$\Delta t = \frac{\%V}{100}\cdot\frac{2z}{V} .$$

For a 1% velocity error at 2 km and 3 km/s that is 6.7 ms — a third of a period
at 50 Hz. **Percentages of velocity are always worth checking in milliseconds of
time.**

### 6.3 A shortcut that fails: applying attenuation without dispersion

**The shortcut.** An inverse-$Q$ filter is applied to compensate amplitude loss,
with the velocity left unchanged.

**Why it fails, derived.** Section 3.1 shows that both $\alpha$ and $V$ come from
the *same* complex modulus $M(\omega) = M'(\omega)[1+i/Q(\omega)]$. Choosing
$\alpha(\omega)$ therefore determines $M'(\omega)$ up to a constant, and hence
$V(\omega)$, through the Kramers–Kronig relation of Section 3.3. Applying a
frequency-dependent amplitude without the accompanying frequency-dependent phase
is not a small approximation: it corresponds to a non-causal operator, one whose
output contains energy before its input arrives.

**Quantified.** The demo's Zener element has $\Delta = 0.10$, hence a total
dispersion of 4.88%. An attenuation-only filter applied over that band leaves a
timing error of 32.5 ms over 2 km (previous section) — that is, the *phase*
error equals the *amplitude* effect in magnitude, because both are the same
complex number. In practice the artefact appears as a systematic mis-tie that
grows with depth and with the amount of $Q$ correction applied, and it is often
misattributed to static or velocity-model error.

**What to do instead.** Use an operator that is a proper complex modulus —
a Zener or Cole–Cole element, or a constant-$Q$ filter implemented in the
frequency domain as $e^{i(\omega/V(\omega))z}e^{-\alpha(\omega)z}$ with
$V(\omega)$ from the same dispersion relation. It costs nothing extra and it is
the only version that is causal.

## 7. Python demonstration

Run `code/petrophysics_demo.py` Section 3. It computes $1/Q(f)$ on a logarithmic
frequency grid, locates the peak numerically, and compares with $1/(2\pi\tau)$,
then checks the asymptotes and the dispersion. Change $\Delta$ and confirm the
peak location is unchanged while its height scales linearly — that is the
signature of a single mechanism.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/06-attenuation-dispersion-exercises.md`](./exercises/06-attenuation-dispersion-rock-exercises.md).

**Common mistakes.** (1) Applying attenuation without dispersion. (2) Confusing
intrinsic $Q$ with apparent (scattering) attenuation. (3) Assuming a constant
$Q$ over a decade of frequency without checking — most rocks show roughly
constant $Q$ only over limited bands. (4) Using the weak-attenuation formula
$\alpha=\pi f/(VQ)$ when $Q$ is small. (5) Reporting $Q$ without the frequency
band it was measured over.

**Applications.** Seismic resolution versus depth budgets (high frequencies die
first); amplitude-versus-offset analysis and its need for a $Q$ correction;
inverse-$Q$ filtering; monitoring of fluids via attenuation at seismic and
laboratory frequencies; earthquake source and path studies.

## 9. Further reading

- **Aki, K. & Richards, P. G. *Quantitative Seismology* (2nd ed.).** Chapters 5
  and 7. Level: graduate. The canonical development of $Q$ and its measurement.
- **Kjartansson, E. (1979).** Constant $Q$-wave propagation and attenuation.
  *JGR* 84, 4737–4748. Level: graduate. The constant-$Q$ formulation.
- **Mavko, Mukerji & Dvorkin, *The Rock Physics Handbook*.** Chapter 6. Level:
  graduate. Laboratory $Q$ measurements and mechanisms.

## 10. Related lessons

- [05-04-05 Anisotropy in Rocks](./05-anisotropy-rock.md)
- [05-04-03 Gassmann Fluid Substitution](./03-gassmann-fluid-substitution.md)
- [02-04-07 Viscoelasticity](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)

## Self-assessment checklist

- [ ] I can define $Q$ and relate it to $\alpha$ with units checked.
- [ ] I can state the Kramers–Kronig constraint and its practical consequence.
- [ ] I can derive the Zener $1/Q$ and its peak frequency.
- [ ] I can verify the peak and the asymptotes numerically.
- [ ] I can explain why attenuation and dispersion must be modelled together.
