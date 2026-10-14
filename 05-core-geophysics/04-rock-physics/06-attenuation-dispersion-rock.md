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

## Extended worked example: turning Q into a resolution-versus-depth budget

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
