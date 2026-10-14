# Module 02-07 — Electromagnetism and Electromagnetic Induction

**Stages:** intermediate → graduate · **Prerequisites:**
[01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
(divergence, curl, the integral theorems and potentials),
[01-11 Complex Analysis](../../01-mathematics/11-complex-analysis/README.md)
(complex amplitudes and phases, for lessons 05–06),
[02-03 Oscillations and Waves](../03-oscillations-and-waves/README.md)
(the wave equation, dispersion and impedance language).

This module is **the physical basis of every electromagnetic method**. Every EM
survey — magnetotellurics, controlled-source EM, airborne EM, induction logging,
ground-penetrating radar — is an application of the four Maxwell equations to a
conducting, polarisable, weakly magnetic Earth. The module builds the subject in
the order the physics demands: electrostatic and magnetostatic fields, the four
equations and their physical meaning, induction, waves, the diffusive limit, and
finally the material property — magnetisation — that makes rock magnetism and
magnetic surveying possible.

Three features distinguish this module:

- **One dichotomy organises everything.** Maxwell's equations give a *wave*
  equation when the displacement current dominates and a *diffusion* equation
  when the conduction current dominates. The single dimensionless ratio
  $\sigma/(\omega\varepsilon)$ decides which, and it spans ten orders of magnitude
  between magnetotelluric and GPR frequencies. Lesson
  [03](./03-maxwell-equations.md) derives both from the same four equations;
  lessons [04](./04-em-induction.md), [05](./05-em-waves.md) and
  [06](./06-em-in-conductors.md) develop each side and the transition between them.
- **Two analogies are stated and bounded.** The electrostatic–gravitational analogy
  is exact mathematics and fails in four specific physical respects (lesson
  [01](./01-electrostatics.md) §6). The $\mathbf B$/$\mathbf H$ distinction is a
  dimensional fact, not a convention, and conflating them is the commonest error
  in this subject.
- **Every number is computed.** Skin depths, impedances, attenuation constants,
  diffusion times, dipole moments and anomalies are all produced by the demos in
  [`code/`](./code) and quoted as observed output. No skin depth in this module is
  asserted without a numerical check against the differential equation it came
  from.

## Learning objectives

By the end of this module you will be able to:

1. Use Coulomb's law, Gauss's law and the electric potential; construct potentials
   by superposition; solve boundary-value problems by images; and state precisely
   where the gravitational analogy holds and where it breaks.
2. Compute magnetic fields from Biot–Savart and Ampère's law, derive the field of a
   current loop, and use the magnetic dipole field and moment — including the
   factor $-2$ between the axial and equatorial amplitudes — as the kernel of every
   transmitter-coil and anomaly calculation.
3. **State all four Maxwell equations, give the physical meaning of each, derive
   the wave equation from them, and then derive the diffusion equation from the
   same equations in a conductor.** Evaluate $\sigma/(\omega\varepsilon)$ and say
   which regime applies.
4. Apply Faraday's law to transformer and motional induction, derive the magnetic
   induction equation and the magnetic Reynolds number, solve the step-diffusion
   problem, and use the diffusion time to argue quantitatively for dynamo action in
   the core.
5. Derive the wave impedance $\eta = \sqrt{\mu/\varepsilon}$, verify that
   $E/H$ has the dimensions of an ohm, compute apparent resistivity from the MT
   impedance, and explain why the ratio is a property of the ground.
6. Derive the skin depth $\delta = \sqrt{2/(\mu\sigma\omega)}$, demonstrate the
   $\sqrt f$ scaling numerically, compute the period required for a stated sounding
   depth, and evaluate the exact attenuation of a lossy dielectric to see where the
   textbook approximations fail.
7. Quantify induced and remanent magnetisation, susceptibility, demagnetising
   factors and the Curie depth, and estimate the anomaly of a buried magnetised
   body.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Electrostatics, Coulomb's Law and Electric Potential](./01-electrostatics.md) | intermediate | $1/r^2$ forces share Laplace's equation — and differ in four decisive ways |
| 02 | [Magnetostatics, Biot–Savart and Ampère's Law](./02-magnetostatics.md) | intermediate | The loop is the elementary source; there is no magnetic monopole |
| 03 | [Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md) | advanced | **The mastery lesson**: the same four equations give a wave *or* a diffusion |
| 04 | [Faraday's Law, Induction and Eddy Currents](./04-em-induction.md) | advanced | Every EM method is induction; eddy currents are the measurement |
| 05 | [Electromagnetic Waves, Impedance and Polarisation](./05-em-waves.md) | advanced | $E/H$ is an impedance in ohms — and it is what an MT survey measures |
| 06 | [EM Fields in Conductors: Skin Depth and Diffusion](./06-em-in-conductors.md) | graduate | $\delta \propto 1/\sqrt f$: a decade of frequency buys a factor 3.16 of depth |
| 07 | [Magnetisation, Susceptibility and Magnetic Materials](./07-magnetisation-materials.md) | graduate | Induced versus remanent magnetisation decides what a magnetic map shows |

## Suggested path

**If you are working through the physics folder in order:** all seven lessons in
numeric order. Lessons 01–02 are self-contained; 03 is the pivot and must not be
skipped; 04–06 are the three faces of Maxwell's equations in the Earth; 07 is the
material-property lesson that connects to the geomagnetism folder.

**If you are here for exploration EM (TEM, FDEM, AEM, induction logging):** read
[02](./02-magnetostatics.md) §4–5 (loop and dipole), [03](./03-maxwell-equations.md)
§4–5 (the diffusion limit and the ratio), [04](./04-em-induction.md) in full
(eddy currents and diffusion times), and [06](./06-em-in-conductors.md) §2–4
(skin depth and scaling). That is the working toolkit.

**If you are here for magnetotellurics:** read [03](./03-maxwell-equations.md) §4–5,
[04](./04-em-induction.md) §4, then [05](./05-em-waves.md) §2–3 (impedance and
apparent resistivity) and [06](./06-em-in-conductors.md) §2–7 (skin depth,
sounding depth and where the half-space model fails).

**If you are here for GPR:** read [03](./03-maxwell-equations.md) §3–5 (waves and
the crossover frequency), [05](./05-em-waves.md) §2, §4–5 (impedance, polarisation,
reflection coefficients) and [06](./06-em-in-conductors.md) §6 (where the
skin-depth formula is *wrong*, which is the regime you work in).

**If you are here for magnetics or palaeomagnetism:** read [02](./02-magnetostatics.md)
§5–6, [04](./04-em-induction.md) §3–4 (the core's field and its maintenance) and
[07](./07-magnetisation-materials.md) in full, then continue into
[08 Geomagnetism and Electromagnetic Fields](../../08-geomagnetism-electromagnetism/README.md).

**If you already have an electromagnetism background:** attempt ★★★9–10 of
[03](./03-maxwell-equations.md), ★★★9 of [05](./05-em-waves.md) and ★★★9 of
[06](./06-em-in-conductors.md) first. If those come out cleanly, use the rest as
reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-electrostatics.md`](./01-electrostatics.md) … [`07-magnetisation-materials.md`](./07-magnetisation-materials.md) | The seven lessons |
| [`exercises/`](./exercises) | Exercise and solution companions for every lesson (14 files) |
| [`code/electrostatics_demo.py`](./code/electrostatics_demo.py) | Superposition, $E=-\nabla V$, Laplace and its $O(h^2)$ truncation, dipole limit, image charges, line and shell fields, the gravity analogy |
| [`code/magnetostatics_demo.py`](./code/magnetostatics_demo.py) | Biot–Savart versus closed forms, loop field, $\nabla\cdot\mathbf B=0$, Ampère's law for linking and non-linking paths, dipole limit, Earth's moment, coil versus geomagnetic field |
| [`code/maxwell_demo.py`](./code/maxwell_demo.py) | All four equations on a plane wave with $O(h^2)$ residuals, discrete curl–curl dispersion, Yee/FDTD dispersion, time-domain diffusion against $\exp(-z/\delta)$ and $\operatorname{erfc}$ |
| [`code/em_induction_demo.py`](./code/em_induction_demo.py) | Faraday EMF, motional EMF, step diffusion against $\operatorname{erfc}$, eddy-current density and dissipation, diffusion times and $R_m$ |
| [`code/em_waves_demo.py`](./code/em_waves_demo.py) | Wave impedance of media, MT impedance and apparent resistivity for a half-space and a two-layer model, Stokes parameters, the dimension check |
| [`code/em_in_conductors_demo.py`](./code/em_in_conductors_demo.py) | $\sqrt f$ scaling, $\delta$ verified against a direct complex tridiagonal ODE solve, the 10 km period, sounding depths, exact versus approximate attenuation |
| [`code/magnetisation_materials_demo.py`](./code/magnetisation_materials_demo.py) | $\mathbf B$–$\mathbf H$–$\mathbf M$ tables, Curie depths, Koenigsberger ratios, dipole anomalies, core magnetisation, demagnetising factors |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> Take a rock with $\rho = 100\ \Omega\,\mathrm m$, $\varepsilon_r = 6$ and
> $\mu = \mu_0$. **(a)** Derive the wave equation from Maxwell's equations for a
> non-conducting medium, and then derive the diffusion equation for a conductor,
> stating exactly which term is dropped and the dimensionless ratio that justifies
> dropping it. **(b)** Evaluate that ratio at $10^{-3}$ Hz and at $10^{8}$ Hz and
> say which regime each frequency is in. **(c)** Derive
> $\delta = \sqrt{2/(\mu_0\sigma\omega)}$ and compute the period needed for a skin
> depth of 10 km. **(d)** For that period, compute $|Z|$ and $\rho_a$ for a
> uniform half-space and state the phase. **(e)** A 5 km layer of this rock overlies
> a 1000 Ω·m basement: state, with reasoning, what happens to $\rho_a$ and to the
> phase as the period grows through the crossover, and why the phase is the more
> diagnostic quantity.

Parts (a)–(b) are lesson [03](./03-maxwell-equations.md) §3–5; (c) is
[06](./06-em-in-conductors.md) §2 and §5; (d)–(e) are
[05](./05-em-waves.md) §3.

**Worked answer for parts (b)–(d):**

$$\frac{\sigma}{\omega\varepsilon}
= \frac{1/\rho}{2\pi f\,\varepsilon_r\varepsilon_0} ,$$

so at $f = 10^{-3}$ Hz,
$\sigma/(\omega\varepsilon) = 0.01/(2\pi\times10^{-3}\times5.31\times10^{-11})
= 3.0\times10^{10}$ — diffusive; and at $f = 10^{8}$ Hz it is
$3.0\times10^{-1}$ — a lossy dielectric, i.e. propagation with real attenuation
but neither of the two simple limits. The crossover frequency is
$f_c = \sigma/(2\pi\varepsilon) = 3.0\times10^{6}$ Hz.

The required period follows from $\delta = \sqrt{\rho T/(\pi\mu_0)}$:

$$T = \frac{\pi\mu_0\delta^2}{\rho}
= \frac{\pi(1.2566\times10^{-6})(10^4)^2}{100} = 3.9478\ \mathrm s .$$

At that period the half-space impedance is
$|Z| = \sqrt{\omega\mu_0\rho} = \sqrt{(2\pi/3.9478)(1.2566\times10^{-6})(100)}
= 1.414\times10^{-2}$ Ω, and
$\rho_a = |Z|^2/(\omega\mu_0) = 100.000$ Ω·m with a phase of $+45.000°$ (with the
$e^{+i\omega t}$ convention used throughout this module). Two properties of a
uniform half-space: the apparent resistivity is exact, and the phase is
constant — which is why *any* departure from 45° is information, and why a
half-space sounding carries no depth information at all.

## Common pitfalls across this module

1. **Conflating $\mathbf B$ (T) with $\mathbf H$ (A/m).** Different dimensions;
   only $\mathbf B = \mu_0\mathbf H$ in vacuum, and $E/B$ is a speed while $E/H$ is
   an ohmic resistance.
2. **Using the skin-depth formula in the wrong regime.** It is a factor 4.7 wrong
   at 100 MHz in wet soil, and it is exact for magnetotellurics. Evaluate
   $\sigma/(\omega\varepsilon)$ before choosing a formula.
3. **Reading an EM delay as a propagation time.** Diffusion has no wavefront; the
   penetration is $z\sim\sqrt{Dt}$ and the "velocity" $\omega\delta$ is not a
   transport speed.
4. **Reporting a sounding depth without stating the convention.** $\delta$,
   $\delta/\sqrt2$ and $0.5\delta$ differ by factors of up to four in the required
   period.
5. **Quoting a phase without a time convention.** $+45°$ and $-45°$ both appear in
   the MT literature for the same physics.
6. **Quoting $\mu_0 = 4\pi\times10^{-7}$ as exact.** Since the 2019 SI redefinition
   it is measured; the numerical difference is negligible for geophysics, but the
   statement is wrong and the practice is habit-forming.
7. **Treating a tabulated susceptibility as a property of a rock.** It is a
   measurement of a sample, it depends on mineralogy, grain size and field, and
   pre-1980 tables are usually in cgs, where $\chi_{\text{SI}} = 4\pi\chi_{\text{cgs}}$.
8. **Assuming induced magnetisation only.** Rocks with $Q = M_r/(\chi H) > 1$ are
   common, and an induced-only interpretation is systematically wrong rather than
   merely imprecise.
9. **Assuming a half-space model where the layer is thinner than $\delta$.** The
   layer thickness, not the skin depth, then controls the response — the
   half-space formula becomes an upper bound and, taken literally, a nonsense.
10. **Reporting a computed quantity to more digits than its inputs.** A skin depth
    from a nominal conductivity is an order of magnitude, whatever the arithmetic
    says.

## Related modules

- [02-03 Oscillations and Waves](../03-oscillations-and-waves/README.md) — the
  scalar wave equation, impedance and reflection language reused here.
- [02-04 Elasticity and Continuum Mechanics](../04-elasticity-and-continuum-mechanics/README.md)
  — the other wave-physics module: compare $v = 1/\sqrt{\mu\varepsilon}$ with
  $v_p = \sqrt{(\lambda+2\mu)/\rho}$, and note that both are stiffness-to-inertia
  ratios with entirely different physical origins.
- [02-08 Potential Theory](../08-potential-theory/README.md) — Laplace's equation
  and the harmonic machinery that gravity, magnetics and steady currents share.
- [05-core-geophysics](../../05-core-geophysics/README.md) and
  [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) — the
  methods built on this module.
- [10 GPR and Near-Surface](../../10-gpr-near-surface/README.md) — the wave regime
  in engineering practice.
- [08 Geomagnetism and Electromagnetic Fields](../../08-geomagnetism-electromagnetism/README.md)
  — the main field, rock magnetism, palaeomagnetism, instruments and surveys; it
  begins where lesson [07](./07-magnetisation-materials.md) ends.
- [26-reference-library](../../26-reference-library/README.md) — constants, units
  and symbols with their provenance.
