# Module 01-11 — Complex Numbers and Analysis

**Stages:** intermediate → doctoral · **Prerequisites:**
[03 Trigonometry](../03-trigonometry/README.md),
[05 Single-Variable Calculus](../05-single-variable-calculus/README.md),
[06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md),
[10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md)

Complex analysis is not an abstract detour from geophysics; it is the natural
language of waves, linear systems and potential fields. Once a physical
oscillation is written as the real part of a complex exponential, differentiation
becomes multiplication, a filter becomes a rational function, a resonance becomes
a pole, and a stability question becomes a question about which side of a line a
number lies on. This module builds that language and then uses it on the four
problems that matter most in practice.

It begins at the beginning: complex arithmetic, polar form and the Argand diagram,
read as a machine for adding sinusoids — phasors, amplitude and phase, impedance.
It then makes the jump from a complex *number* to a complex *variable*, where the
single extra limit in the derivative forces the real and imaginary parts to
satisfy the Cauchy-Riemann equations and therefore Laplace's equation. That fact
is the bridge to potential fields: **every holomorphic function is a pair of
harmonic functions**, so two-dimensional potential problems — a line mass, a
dipole, the field of a polygon, a half-plane boundary-value problem — are solved
exactly by exhibiting an analytic function, and the poles of that function are the
sources. The module verifies this with finite-difference Laplacians rather than
asserting it.

The middle of the module is the machinery: contour integration, Cauchy's theorem
and the residue theorem. The point is not the algebra but the reach. Real
integrals that no substitution touches — the ones that appear in Fourier analysis,
in Green's functions, in dispersion relations and in series summation — fall in
three lines, provided you choose the contour and account for the closing arc.
That last step is where nearly every error lives, so this module *measures* the arc
contribution rather than waving it away, and shows that for a rational integrand
it cancels to leading order and survives at order $1/R$ with a coefficient of
exactly two.

Two transform lessons follow, and they are the ones with the widest daily use.
The **Laplace transform** converts a transient problem into algebra, carrying the
initial conditions along automatically, and its inversion is a contour integral
whose answer depends on whether the singularities are poles (a sum of decaying
exponentials) or a branch point (a complementary error function, with no
characteristic time at all — diffusion). The **$z$-transform** is the sampled
version: a difference equation is a rational function of $z^{-1}$, the unit circle
is the frequency axis, the pole radius is the per-sample decay, the pole angle is
the frequency, and the pole-zero diagram decides both the design and the
stability of every digital filter in the processing chain.

The last lesson is the deepest and the one with the most physical consequence.
**Causality** — nothing responds before it is driven — forces the transfer
function to be analytic in one half of the complex frequency plane. From that
single fact follows the Kramers-Kronig relation, which says that **the attenuation
and the dispersion of a medium are not independent**: choose one and the other is
determined, up to a constant. This is applied here to the standard linear solid,
where the dissipated energy per cycle is computed directly from the stress-strain
loop to fix the sign of the imaginary part, and it is stated with the caution it
deserves: the *relation* is exact, the *magnitude* of the dispersion depends on how
the loss is distributed in frequency, and a near-constant-$Q$ model is an
assumption about a relaxation spectrum rather than a fact about the Earth.

Every lesson derives the mathematics, interprets it physically and then computes
it. Every number quoted was produced by a runnable standard-library script in
[`code/`](./code); the residues are verified from small contours as well as from
their closed forms, the contour integrals are verified by quadrature of the *real*
integral, the harmonic functions are verified by finite-difference Laplacians with
a demonstrated convergence rate, and the transfer functions are verified against
time-domain integrations that do not use the transform at all.

## Learning objectives

By the end of this module you will be able to:

1. Convert between rectangular and polar form, add and scale phasors, and read the
   amplitude and phase of a sinusoid off a complex number — with a stated branch
   of the argument.
2. Write the impedance of a circuit or a driven oscillator, read its modulus and
   argument as the amplitude and phase response, and verify the result against a
   time-domain integration.
3. Test a function for holomorphy, derive and use the Cauchy-Riemann equations,
   and explain why the real and imaginary parts of a holomorphic function satisfy
   Laplace's equation.
4. Solve two-dimensional potential problems by exhibiting an analytic function:
   line masses, dipoles, and the half-plane Dirichlet problem via the Poisson
   integral.
5. Compute residues of poles of any order, apply the residue theorem, and evaluate
   rational, Fourier-type and principal-value real integrals — with the contour,
   the enclosed poles and the arc argument stated.
6. Solve a transient initial-value problem by the Laplace transform, invert it
   both by residues and by a numerical Bromwich integral, and recognise when the
   inverse is not a sum of exponentials.
7. Convert a difference equation into a transfer function, locate its poles and
   zeros, read stability, decay rate and resonance frequency off the $z$ plane,
   and apply the padding rule for a discrete convolution.
8. Derive the Kramers-Kronig relations from causality, verify them numerically in
   both directions, and explain why the attenuation and the dispersion of a
   dissipative medium cannot be chosen independently.
9. Quantify the dispersion implied by a given attenuation model, state the
   assumptions, and explain why the near-constant-$Q$ logarithmic law is a
   stronger assumption than causality alone.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Complex Numbers, Polar Form and Argand Diagrams](./01-complex-arithmetic.md) | intermediate | A phasor is a sinusoid's amplitude and phase with the time dependence factored out |
| 02 | [Holomorphic Functions and Cauchy-Riemann Equations](./02-complex-functions.md) | graduate | Analytic functions come two at a time: both parts solve Laplace's equation |
| 03 | [Contour Integration, Residues and Real Integrals](./03-contour-integration.md) | graduate | A closed contour pays for the singularity it encloses, and nothing else |
| 04 | [The Laplace Transform and Transient Problems](./04-laplace-transform.md) | graduate | Differentiation becomes multiplication, initial conditions come free, and inversion is a contour |
| 05 | [The z-Transform and Discrete Linear Systems](./05-z-transform.md) | graduate | Pole radius is decay, pole angle is frequency, the unit circle decides stability |
| 06 | [Dispersion Relations and Causality in Wave Physics](./06-dispersion-relations.md) | doctoral | Attenuation and dispersion are two views of one function |

## Suggested path

**If you are working through the mathematics folder in order:** lessons 01–03 in
sequence, with the exercises — that is the core, roughly 8–10 hours, and it is
required before [12 Numerical Methods](../12-numerical-methods/README.md) and
[14 Optimization](../14-optimization/README.md), and assumed in
[16 Functional Analysis](../16-functional-analysis/README.md) and
[18 Inverse Problems](../../18-inverse-problems/README.md).

**If you already use phasors and transfer functions in your own work:** attempt
★★★9 of [01-11-01](./01-complex-arithmetic.md) first. If it comes out cleanly,
start at [01-11-03](./03-contour-integration.md) and work forward; the arithmetic
is a revisiting rather than a beginning.

**If you are here for potential fields and 2-D modelling:** read
[01-11-02](./02-complex-functions.md) in full — Sections 3 to 5 are the bridge —
and then [01-11-03](./03-contour-integration.md) §4.1, which is where the
equivalent-source formulas come from. Then go to
[11-exploration-geophysics](../../11-exploration-geophysics/README.md) and
[07-gravity-geodesy](../../07-gravity-geodesy/README.md).

**If you are here for signal processing and seismology:** read
[01-11-01](./01-complex-arithmetic.md) §4 (impedance), then
[01-11-05](./05-z-transform.md) in full (filters, poles, the resonator peak), and
then [01-11-06](./06-dispersion-relations.md) §4 and §6 (minimum phase, and why
attenuation correction without dispersion correction is wrong). Finish with
[20-signal-processing](../../20-signal-processing/README.md).

**If you are here for the Laplace transform and diffusion:** read
[01-11-03](./03-contour-integration.md) §2–4 as the prerequisite, then
[01-11-04](./04-laplace-transform.md), then §5 of
[01-09-02 The Heat
Equation](../09-partial-differential-equations/02-heat-equation.md).

**If you are here for attenuation and $Q$:** read
[01-11-06](./06-dispersion-relations.md) §2–3 first (the theorem), then §6 (the
model and its numbers), then
[02-03-10
Attenuation](../../02-physics/03-oscillations-and-waves/10-attenuation.md) for the
physical mechanisms and [06-seismology](../../06-seismology/README.md) for the
measurements.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-complex-arithmetic.md`](./01-complex-arithmetic.md) … [`06-dispersion-relations.md`](./06-dispersion-relations.md) | The six lessons |
| [`exercises/`](./exercises) | Graded exercises and full worked solutions for each lesson, twelve files in all |
| [`code/complex_arithmetic_demo.py`](./code/complex_arithmetic_demo.py) | Polar/rectangular round trips, phasor addition against the time domain, $R$–$C$ impedance against an ODE integration, the driven oscillator against Runge–Kutta |
| [`code/holomorphic_laplace_demo.py`](./code/holomorphic_laplace_demo.py) | Cauchy-Riemann residuals, five-point Laplacian convergence, harmonic-conjugate reconstruction, line-mass and dipole complex potentials, orthogonality, the half-plane Poisson integral |
| [`code/contour_residues_demo.py`](./code/contour_residues_demo.py) | Residues from small contours, Cauchy's integral formula, real integrals by quadrature, the measured arc contribution, oscillatory and principal-value integrals |
| [`code/laplace_transient_demo.py`](./code/laplace_transient_demo.py) | Forward transforms with exact tails, the Bromwich integral and its arc, residue inversion, a second-order transient, and diffusion against $\operatorname{erfc}$ and against a finite-difference PDE solve |
| [`code/ztransform_demo.py`](./code/ztransform_demo.py) | Convergence regions, the DFT as the unit circle, recursion against closed form, stability measured as a log-slope, the resonator peak, circular versus linear convolution, $z = e^{sT}$ and bilinear warping |
| [`code/dispersion_causality_demo.py`](./code/dispersion_causality_demo.py) | Causality in the time domain, Kramers-Kronig in both directions, the log-amplitude relation, a non-causal counterexample, and the standard linear solid with its hysteresis loop and dispersion |

All six scripts use only the Python standard library (`cmath` and `math`; NumPy
is not required and is not imported). Each is runnable from the repository root,
for example:

```text
python3 01-mathematics/11-complex-analysis/code/dispersion_causality_demo.py
```

and each prints the tables quoted in its lesson.

## Mastery checkpoint

Complete this without notes:

> A seismic wavelet is recorded at two receivers 500 m apart along a horizontal
> borehole in a homogeneous medium. The amplitude at the second receiver is
> $0.80$ of that at the first, and the arrival time at the second is $10$ ms
> later than at the first. **(a)** Write the medium's response over the 500 m path
> as a complex number at the dominant frequency of $30$ Hz, and identify its
> modulus and argument with the attenuation and the travel time. **(b)** State
> which half of the complex plane the frequency response must be analytic in for
> this to be a physically realisable medium, and why. **(c)** Compute $Q$ from the
> amplitude ratio, stating the formula and the assumption that the path is
> uniform. **(d)** Explain why you cannot now choose the velocity at a second
> frequency freely: state the constraint and say which lesson establishes it.
> **(e)** A colleague corrects the record for attenuation by dividing its spectrum
> by the measured amplitude ratio at each frequency, and leaves the phase alone.
> Explain what is wrong with the result, and what a reader would see in a migrated
> section as a consequence. **(f)** The same correction is applied instead with a
> recursive filter whose pole lies at $z = 1.02$. State what happens to the output
> after $10^{4}$ samples, and what the correct design rule is.

A worked version of (a)–(c) is in the
[solutions](./exercises/06-dispersion-relations-solutions.md) for ★★6, and (d)–(f)
are treated in [01-11-06](./06-dispersion-relations.md) §6,
[01-11-04](./04-laplace-transform.md) §4.2 and
[01-11-05](./05-z-transform.md) §5.1.

## Common pitfalls across this module

1. **Not stating the sign convention.** Every imaginary part in this module —
   of a transfer function, a modulus or an impedance — has a sign that follows
   from $e^{-i\omega t}$ versus $e^{+i\omega t}$. Mixing the two flips the sign of
   one relation and leaves every amplitude plausible
   ([01-11-06](./06-dispersion-relations.md) §2.1).
2. **Confusing harmonic with holomorphic.** A harmonic function is not the real
   part of an analytic function unless its conjugate partner exists; the pair, not
   either member, is what the theorems are about
   ([01-11-02](./02-complex-functions.md) §3.3).
3. **Forgetting that the theorems need a domain, not a point.** Complex
   differentiability at a single point implies nothing; a branch cut, a pole or
   the boundary of the region of convergence is where the theorems stop applying
   ([01-11-02](./02-complex-functions.md) §2.2,
   [01-11-03](./03-contour-integration.md) §3.1).
4. **Closing a contour without checking the arc.** The arc may cancel to leading
   order and survive at order $1/R$, and for an oscillatory integrand the sign of
   the frequency decides which half plane closes
   ([01-11-03](./03-contour-integration.md) §4.3, §5).
5. **Dropping the initial condition in a Laplace transform.** $\mathcal{L}\{f'\} =
   sF(s)-f(0)$, and the missing term is a decaying transient that nothing else
   supplies ([01-11-04](./04-laplace-transform.md) §3).
6. **Expecting a diffusive transient to have a time constant.** A branch point
   inverts to an error function, and the response has no characteristic scale
   ([01-11-04](./04-laplace-transform.md) §5).
7. **Padding a discrete convolution to the length of the input.** The transform
   length must be $n_{x}+n_{h}-1$, or the tail wraps onto the start
   ([01-11-05](./05-z-transform.md) §6).
8. **Quoting a pole angle as a resonance frequency.** The peak is pulled towards
   DC by an amount proportional to $1-r$, which is largest for the sharpest
   resonators ([01-11-05](./05-z-transform.md) §5.2).
9. **Assuming a pole "close to one" is harmless.** A radius $1.01$ over a
   5000-sample record grows by $10^{21}$; the tolerance on a pole radius is about
   one part in a thousand ([01-11-05](./05-z-transform.md) §5.1).
10. **Treating attenuation and dispersion as independent.** They are two views of
    one function, and a correction that removes one and leaves the other is not a
    correction ([01-11-06](./06-dispersion-relations.md) §6).
11. **Quoting a dispersion coefficient without its model.** The Kramers-Kronig
    relation is exact; the magnitude of the resulting dispersion depends on the
    assumed relaxation spectrum, and factors of two between published forms come
    from different definitions ([01-11-06](./06-dispersion-relations.md) §6.5).
12. **Reporting a wrapped phase as if it were smooth.** $\operatorname{Arg}$ jumps
    by $2\pi$ across the negative real axis; unwrap before differentiating
    ([01-11-01](./01-complex-arithmetic.md) §2.3).

## Related modules

- [03 Trigonometry](../03-trigonometry/README.md) — phase, harmonics and the
  superposition of oscillations, which lesson 01 formalises as phasors.
- [05 Single-Variable Calculus](../05-single-variable-calculus/README.md) and
  [06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  the integrals, the vector operators and the potential theory that become
  analyticity and residues here.
- [09 Partial Differential Equations](../09-partial-differential-equations/README.md) —
  where the same problems are solved by separation of variables, and where the
  Laplace-transform route of lesson 04 is the alternative.
- [10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  the real-frequency case, and the DFT that lesson 05 generalises to the $z$
  plane.
- [12 Numerical Methods](../12-numerical-methods/README.md) — quadrature,
  finite differences and the stability analyses whose language is the $z$ plane.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — deconvolution,
  continuation and the regularisation that the analytic inversions here need in
  the presence of noise.
- [20 Signal Processing](../../20-signal-processing/README.md) — where these
  filters, transfer functions and minimum-phase assumptions are used on real
  records.
- [02 Physics: Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md) —
  the damped driven oscillator of lesson 01, the dispersion of lesson 06, and the
  attenuation that makes them one problem.
- [06 Seismology](../../06-seismology/README.md) and
  [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md) — the two
  disciplines where the material of this module is used every day.
