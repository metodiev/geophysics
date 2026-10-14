---
id: 01-08-06
title: "Green's Functions and Impulse Response"
level: graduate
prereqs: ["01-08-02", "01-08-03"]
estimated_minutes: 90
tags: [greens-function, impulse-response, convolution, causality, instrument-response]
---

# Green's Functions and Impulse Response

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the defining property of a Green's function — that it solves the
   operator equation with a unit impulse as the source, subject to homogeneous
   conditions — and explain why that one solution determines the response to
   *every* source through convolution.
2. **Construct** the Green's functions of the first-order operator, the
   undamped oscillator and the damped oscillator, and of the one-dimensional
   diffusion operator on an interval.
3. **Explain** the impulse as a weak limit, and predict the order of accuracy
   with which a finite-width pulse reproduces the impulse response, then verify
   it numerically.
4. **Verify** convolution against a direct ODE integration, and explain what
   the residual measures.
5. **Derive** causality as a statement about the frequency-domain response, and
   demonstrate it by numerically inverting a transfer function.
6. **Use** the concept where it matters: instrument-response correction,
   source-time-function deconvolution and the seismic representation theorem.

## Prerequisites

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  the damped oscillator whose impulse response is the central example.
- [03 Damped and Driven Oscillators as Physical Models](./03-oscillators.md) —
  the transfer function $\hat X(\omega)$ which is the Fourier transform of the
  Green's function.
- [01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md) —
  the quadrature used for every convolution below.

## 1. Intuition: one response to rule them all

A linear system is completely characterised by its response to a single
impulse. Push it once, sharply, and record what it does; the response to *any*
other input is then a weighted sum — a convolution — of shifted copies of that
record. This is the single most powerful idea in applied linear physics, and
the Green's function is its mathematical form.

Three reasons it matters so much in geophysics:

1. **It separates the instrument from the medium.** A recorded seismogram is
   (source) $\ast$ (Earth's response) $\ast$ (instrument response). If the
   instrument's impulse response is known, it can be removed by deconvolution,
   which is why seismograph manufacturers publish calibration curves.
2. **It separates the source from the propagation.** The displacement field
   from an earthquake is a convolution of the moment-tensor source with the
   medium's Green's function. This is the **representation theorem**, and it is
   the reason seismology can do source inversion at all.
3. **It turns a differential equation into an integral equation.** For
   complicated geometry the Green's function may be easier to compute (or to
   measure) than to solve the boundary-value problem directly — the basis of
   the boundary-element methods of
   [19-05-02](../../19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/02-boundary-element.md).

Before the algebra, one warning about terminology. "The" Green's function
depends on the operator, the domain and the boundary conditions. Change the
boundary condition and you have a different Green's function. This lesson keeps
the conditions fixed as homogeneous, which is what makes superposition clean.

## 2. Definitions

### 2.1 Definition

Let $L$ be a linear differential operator. The **Green's function** $G$ for $L$
with homogeneous boundary/initial conditions is the solution of

$$\boxed{\;L\,G = \delta\;}$$

satisfying those conditions, where $\delta$ is the unit impulse: the Dirac
delta in space and time for a boundary-value problem, or $\delta(t-t')$ for an
initial-value problem. For an initial-value problem, "homogeneous conditions"
means $G$ and its derivatives up to one less than the order vanish at $t=t'$,
and $G$ itself is defined to be zero for $t<t'$:

$$G(t,t') = 0 \quad\text{for } t<t' .$$

That last statement is **causality**, and it is not an extra assumption: it is
what makes the solution of the initial-value problem unique.

### 2.2 Superposition and convolution

Once $G$ is known, the solution of $L y = f$ with the same conditions is

$$\boxed{\;y(t) = \int G(t,t')\,f(t')\,dt'\;}$$

For a time-invariant operator $G(t,t') = G(t-t')$ and the integral is a
**convolution**, $y = G \ast f$. Three consequences:

- **Linearity** means the response to a sum of impulses is the sum of the
  responses, so an arbitrary source can be decomposed.
- **Causality** means the integral runs only over past times, $t' \le t$.
- **Time invariance** means only the elapsed time matters, so the Green's
  function is a one-parameter family.

### 2.3 The frequency-domain form

For a time-invariant operator, Fourier transforming $L G = \delta$ gives

$$\hat G(\omega) = \frac{1}{\hat L(\omega)},$$

so the Green's function *is* the transfer function — the same object as the
$\hat X(\omega)$ of [03 Oscillators](./03-oscillators.md), up to normalisation.
Convolution in time becomes multiplication in frequency, which is the reason
deconvolution is done in the frequency domain and why "instrument response
correction" means "divide by $\hat G$".

## 3. Derivations, step by step

### 3.1 The first-order operator

For $L = \tfrac{d}{dt} + a$ with $y(0)=0$, we need $G' + aG = \delta(t-t')$ and
$G=0$ for $t<t'$. For $t>t'$ the right-hand side is zero, so
$G = A e^{-a(t-t')}$. Integrating the equation from $t'-\epsilon$ to
$t'+\epsilon$ and letting $\epsilon\to0$:

$$G(t'+)-G(t'-) + a\int_{t'-\epsilon}^{t'+\epsilon}G\,dt = 1
\;\Longrightarrow\; G(t'+) = 1,$$

so $A = 1$ and

$$G(t-t') = e^{-a(t-t')}H(t-t'),$$

with $H$ the unit step. Then
$y(t) = \int_0^t e^{-a(t-t')}f(t')\,dt'$ solves $y' + ay = f$ with $y(0)=0$.

The demonstration tests this against a fourth-order Runge–Kutta integration of
the ODE itself, for $a = 2$ and $f(t) = \sin 3t$:

| $t$ | convolution | RK4 | difference |
|---|---|---|---|
| 0.5 | 0.222032053 | 0.222032053 | $1.2\times10^{-14}$ |
| 1.0 | 0.281401797 | 0.281401797 | $5.2\times10^{-14}$ |
| 2.0 | $-0.260338072$ | $-0.260338072$ | $6.6\times10^{-14}$ |
| 4.0 | $-0.277207794$ | $-0.277207794$ | $2.8\times10^{-14}$ |

**The two calculations share no code path**: one is a quadrature of an
analytically known kernel, the other is a time-stepping integration of the
differential equation. Agreement at $10^{-14}$ is as strong a verification as
this problem admits, and it is the standard to which every Green's function in
this lesson is held.

### 3.2 The oscillator, and the meaning of the pulse width

For $L = \tfrac{d^2}{dt^2} + 2\zeta\omega_0\tfrac{d}{dt} + \omega_0^2$ with
zero initial conditions, the same two-step argument gives

$$G(t) = \frac{e^{-\zeta\omega_0t}\sin(\omega_dt)}{\omega_d}\,H(t), \qquad
\omega_d = \omega_0\sqrt{1-\zeta^2},$$

and the undamped limit is $G(t) = \sin(\omega_0t)/\omega_0$.

Now the point that is usually glossed over. A delta function is not a function,
so a numerical "impulse" is always a narrow pulse of finite width $\epsilon$
and unit area. **What order of accuracy does that give?** Replace
$\delta(t)$ by $\tfrac{1}{\epsilon}$ on $[0,\epsilon]$. Then

$$\int_0^tG(t-s)\,\frac{1}{\epsilon}\mathbb{1}_{[0,\epsilon]}(s)\,ds
= \frac{1}{\epsilon}\int_0^{\epsilon}G(t-s)\,ds
= G(t) - \frac{\epsilon}{2}G'(t) + O(\epsilon^2),$$

so the error is **first order in the pulse width**. The demonstration measures
this at $\zeta = 0.08$, $\omega_0 = 2$, $t = 1$:

| $\epsilon$ | pulse response | $G(t)$ | $\lvert$error$\rvert$ | ratio |
|---|---|---|---|---|
| 0.400 | 0.429714085 | 0.389804081 | $3.99\times10^{-2}$ | — |
| 0.200 | 0.420822401 | 0.389804081 | $3.10\times10^{-2}$ | 1.29 |
| 0.100 | 0.407871735 | 0.389804081 | $1.81\times10^{-2}$ | 1.72 |
| 0.050 | 0.399362737 | 0.389804081 | $9.56\times10^{-3}$ | 1.89 |
| 0.025 | 0.394537748 | 0.389804081 | $4.73\times10^{-3}$ | 2.02 |

The ratios climb toward 2 as $\epsilon$ shrinks: **the error is asymptotically
first order, with a pre-asymptotic regime at large $\epsilon$.** The pulse
response converges to $G(t)$ but never equals it at finite width. Anyone who
has wondered why a "spike" test in a finite-difference code gives a slightly
wrong amplitude now has the answer, and the answer is not a bug.

### 3.3 Convolution with a smooth source

For a smooth forcing the convolution should agree with a direct integration at
the quadrature floor. The demonstration uses the symmetric wavelet
$f(s) = \left[1-2((s-t_c)/b)^2\right]e^{-((s-t_c)/b)^2}$ with $t_c = 2$,
$b = 0.4$, and $\zeta = 0.08$, $\omega_0 = 2$:

| $t$ | convolution | RK4 | difference |
|---|---|---|---|
| 1.0 | $-0.000147756$ | $-0.000147756$ | $1.2\times10^{-15}$ |
| 2.0 | $-0.050912793$ | $-0.050912793$ | $3.4\times10^{-13}$ |
| 3.0 | $0.070115424$ | $0.070115424$ | $6.7\times10^{-15}$ |
| 4.0 | $-0.058611840$ | $-0.058611840$ | $2.6\times10^{-13}$ |
| 6.0 | $0.049581971$ | $0.049581971$ | $1.0\times10^{-13}$ |

Notice that at $t = 1$ the response is $10^{-4}$ while the forcing peak is
$O(1)$: the oscillator has barely started to move. **The Green's function
carries the timing as well as the amplitude**, which is the property that makes
it useful for picking arrival times and for deconvolution.

### 3.4 Resonance without damping, and where the amplitude comes from

Drive an undamped oscillator at its own frequency from rest:

$$x'' + x = \sin t, \qquad x(0) = x'(0) = 0 .$$

The Green's function is $G(t) = \sin t$, so

$$x(t) = \int_0^t\sin(t-s)\sin(s)\,ds = \frac{\sin t - t\cos t}{2}.$$

The demonstration confirms this against the convolution numerically:

| $t$ | convolution | $(\sin t - t\cos t)/2$ | difference |
|---|---|---|---|
| 5.0 | $-1.188617601$ | $-1.188617601$ | $5.1\times10^{-15}$ |
| 10.0 | $3.923347090$ | $3.923347090$ | $1.8\times10^{-14}$ |
| 20.0 | $-3.624347993$ | $-3.624347993$ | $4.9\times10^{-14}$ |
| 40.0 | $13.711317813$ | $13.711317813$ | $9.8\times10^{-14}$ |

The envelope grows as $t/2$: **resonance in an undamped system is linear growth
in time, not infinite amplitude.** Damping is what converts that growth into a
finite amplitude $Q$, as
[03 Oscillators](./03-oscillators.md) shows. The naive statement "the response
is infinite at resonance" is an artefact of looking for a periodic
steady-state solution where none exists.

### 3.5 The spatial Green's function, and how a source should be discretised

For $L = -\tfrac{d^2}{dx^2}$ on $(0,1)$ with $u(0)=u(1)=0$, the Green's
function is the famous tent:

$$G(x,\xi) = \begin{cases}x(1-\xi), & x\le\xi\\ \xi(1-x), & x\ge\xi\end{cases}$$

The demonstration solves the discrete problem with a three-point stencil and the
Thomas algorithm, then compares with the exact $G$. Two results, both
instructive:

**Result 1: a source exactly on a node is reproduced to machine precision.**
The exact $G$ is piecewise linear, so its second difference vanishes identically
at every node except the source node, where it equals $-1/h$ in the scaled
equation. The discrete solution therefore equals the exact $G$ at the nodes.
The demonstration measures the maximum nodal error over $n = 20, 40, 80, 160$
interior nodes and obtains $8.3\times10^{-17}$, $3.6\times10^{-16}$,
$4.7\times10^{-16}$, $1.7\times10^{-15}$ — machine precision, growing only
because the number of operations grows.

**Result 2: the way the source is spread costs an order of accuracy.** With the
source midway between two nodes, placing all of its weight on the nearer node
gives the errors

| nodes | max error | ratio |
|---|---|---|
| 20 | $1.474\times10^{-2}$ | — |
| 40 | $7.733\times10^{-3}$ | 1.91 |
| 80 | $4.039\times10^{-3}$ | 1.91 |
| 160 | $2.045\times10^{-3}$ | 1.98 |

— first order, not second. Distributing the source with the grid's own hat
function instead restores machine precision.

**The lesson: a source term is a functional, not a function.** $\delta$ is
defined by what it does under an integral, and discretising it carelessly can
cost more accuracy than the scheme's formal order. This is one of the most
common silent errors in potential-field and diffusion modelling.

### 3.6 Reciprocity and superposition, exactly

For this self-adjoint operator, $G(x,\xi) = G(\xi,x)$. The demonstration solves
with the source at node 45 and reads the response at node 10, then reverses the
two, with $n = 60$ interior nodes:

$$\text{source at 45, response at 10} = 0.044342919, \qquad
\text{source at 10, response at 45} = 0.044342919,$$

a relative asymmetry of $3.1\times10^{-16}$. Superposition is checked in the
same way: the response at node 25 to sources at both nodes 10 and 45 is
$0.208277345$, identically the sum of the two individual responses.

**Reciprocity is the physical reason a seismic experiment is interchangeable.**
A source at $A$ and receiver at $B$ records the same trace (for a reciprocal
sensor and a time-invariant medium) as the reverse configuration. That is what
makes it legitimate to combine many sources and receivers into a single
inverse problem — and it is a property of the *operator's symmetry*, not of
the data processing.

### 3.7 Causality from the frequency-domain response

The last construction is the most revealing. Take the damped oscillator with
$\omega_0 = 1$, $\zeta = 0.1$, so that

$$\hat G(\omega) = \frac{1}{\omega_0^2 - \omega^2 + 2i\zeta\omega_0\omega} .$$

If $G$ is causal, the inverse Fourier transform must vanish for $t<0$. The
demonstration evaluates

$$G(t) = \frac{1}{\pi}\int_0^{\infty}\operatorname{Re}\left[\hat G(\omega)e^{i\omega t}\right]d\omega$$

by Simpson quadrature on $\omega\in[0,1200]$ with 120 000 points, and finds

| $t$ | inverse transform | $G(t)$ from the formula | difference |
|---|---|---|---|
| $-6.0$ | $1.9\times10^{-8}$ | 0 | $1.9\times10^{-8}$ |
| $-3.0$ | $1.9\times10^{-8}$ | 0 | $1.9\times10^{-8}$ |
| $-1.0$ | $2.0\times10^{-8}$ | 0 | $2.0\times10^{-8}$ |
| $0.5$ | $0.456236945$ | $0.456236966$ | $2.1\times10^{-8}$ |
| $1.0$ | $0.762757698$ | $0.762757679$ | $2.0\times10^{-8}$ |
| $4.0$ | $-0.500924375$ | $-0.500924394$ | $1.9\times10^{-8}$ |
| $8.0$ | $0.449061869$ | $0.449061851$ | $1.8\times10^{-8}$ |

**One function, two behaviours.** For $t>0$ it is the damped oscillation; for
$t<0$ it is zero to the width of the integration band. The asymmetry is not put
in by hand — it is a consequence of where the poles of $\hat G$ sit. In this
convention the poles are in the *upper* half plane, and a pole in the lower half
plane would produce a non-zero result for $t<0$, i.e. an acausal system. This is
the reason the placement of poles, and the dispersion relations that follow from
it, are treated as physics rather than as complex analysis:
[01-11-06 Dispersion Relations and Causality](../11-complex-analysis/06-dispersion-relations.md).

## 4. Physical interpretation

**The Green's function is the medium's memory.** Convolution says the current
response is a weighted average of all past inputs, with the weights given by
$G$. A short-memory medium has a $G$ that decays quickly; a ringing medium
remembers for many periods.

**A Green's function is defined by its conditions, not only by its operator.**
Change the boundary conditions and $G$ changes everywhere. This is why an
instrument's response cannot be reused as an Earth response, and why "the"
Green's function is always shorthand for "the Green's function *for this
problem*".

**Causality is a constraint on the frequency-domain description.** $\hat G$
cannot be chosen freely: its real and imaginary parts are related by the
Kramers–Kronig relations, and its poles are confined to one half plane. A model
that fits a measured amplitude response but violates causality corresponds to a
system that responds before it is driven; it will fit the amplitude data and
fail the phase data. **Checking both amplitude and phase is therefore not
pedantry but a consistency test.**

**The impulse response of an instrument is a measurable object.** A calibration
coil, a step test or a reference seismometer gives it directly, and once it is
known the deconvolution is a division in the frequency domain (with care at
frequencies where $\hat G$ is small, where the division amplifies noise —
regularisation of exactly the kind discussed in
[18-inverse-problems](../../18-inverse-problems/README.md)).

**What the construction assumes.** Linearity, time invariance and homogeneous
conditions. A non-linear medium has no Green's function; a slowly varying medium
has one that depends on the source and receiver positions separately; and a
problem with inhomogeneous initial conditions needs an extra term. Each of
these is a real limitation in geophysics.

## 5. Python demonstration

The companion script is
[`code/green_functions_demo.py`](./code/green_functions_demo.py), standard
library only.

| Section | Claim being tested | Observed result |
|---|---|---|
| 1 | Convolution reproduces the ODE solution | agreement at $10^{-14}$ for $y'+2y=\sin3t$ |
| 2 | The pulse response converges at first order in $\epsilon$ | error ratios 1.29, 1.72, 1.89, 2.02 |
| 3 | Convolution with a smooth source | agreement at $10^{-13}$ or better |
| 4 | Undamped resonance grows linearly | $x = (\sin t - t\cos t)/2$ matched to $10^{-14}$ |
| 5 | Source placement controls accuracy | node-centred and hat-distributed: $10^{-16}$; nearest-node: first order, ratio 1.91 |
| 6 | Reciprocity and superposition | asymmetry $3.1\times10^{-16}$; superposition exact |
| 7 | Causality from the inverse Fourier transform | $G(t<0)\sim2\times10^{-8}$; $G(t>0)$ matched to $2\times10^{-8}$ |

Two methodological notes. First, the convolution in Section 1 shares no code
with the ODE integration in the same section, which is what makes the agreement
evidence rather than tautology. Second, in Section 7 the residual for $t<0$ is
*not* machine zero and is not meant to be: it is set by the finite upper limit
of the integration band, and the script says so. Reporting a limit honestly is
part of the result.

> **Breaking exercise.** In Section 7, reduce the integration band from 1200 to
> 60 and predict whether the error for $t<0$ will grow or shrink, and by roughly
> what factor. Then check, and reconcile the answer with the $1/\Omega$ tail of
> an oscillatory integral.

## 6. Exercises

Attempt these closed-book. See
[`exercises/06-green-functions-exercises.md`](./exercises/06-green-functions-exercises.md)
and the worked
[`exercises/06-green-functions-solutions.md`](./exercises/06-green-functions-solutions.md).

## 7. Common mistakes

1. **Using the wrong boundary conditions.** $G$ is defined together with its
   conditions; a Green's function for a free end will not satisfy a clamped end.
2. **Forgetting that $G$ solves the equation with the *impulse* on the
   right-hand side and *zero* initial conditions.** Mixing in a non-zero
   initial condition double-counts the transient.
3. **Convolving in the wrong direction.** $y(t) = \int G(t-t')f(t')dt'$ is not
   the same as $\int G(t'-t)f(t')dt'$ unless $G$ is even, which for a causal
   system it is not.
4. **Treating a finite-width pulse as an exact impulse.** The error is first
   order in the width (Section 3.2), and it can dominate everything else in a
   convergence study.
5. **Misplacing the source in a discretisation.** Section 3.5 shows this costs
   an order of accuracy even when the stencil is correct.
6. **Deconvolving without regularisation.** Dividing by $\hat G$ where
   $|\hat G|$ is small amplifies noise without bound; this is an inverse problem,
   not a division.
7. **Assuming a Green's function exists for a non-linear problem.** It does not.
   In non-linear problems the superposition principle fails, and "impulse
   response" is meaningful only as a small-signal linearisation.
8. **Trusting an amplitude fit that violates causality.** Fit phase as well as
   amplitude, or the model is not physical.

## 8. Real-world applications

- **Instrument-response correction.** Seismograms are corrected by dividing by
  the sensor's transfer function. See
  [23-02-01 Seismometers](../../23-field-methods-instruments/02-seismic-instruments-and-fieldwork/01-seismometers.md).
- **Source-time-function deconvolution.** The shape of an earthquake or
  explosion source is recovered by deconvolving the medium and instrument
  responses from the recorded trace.
- **The seismic representation theorem.** The displacement field is a
  convolution of a moment-tensor source with the medium's Green's function,
  summed over source and receiver components and over the moment-tensor indices.
  This is the forward model of source inversion.
- **Numerical Green's functions.** For realistic Earth models the Green's
  function is computed numerically, by finite differences or by modal summation;
  see
  [19-05-03 Numerical Green's Functions and Their Computation](../../19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/03-greens-function-numerics.md).
- **Heat kernels and diffusion.** The Green's function of the diffusion
  equation is the Gaussian kernel whose width grows as $\sqrt{\kappa t}$, which
  is the mathematical content of a diffusion "length scale". See
  [01-09-02 The Diffusion/Heat Equation](../09-partial-differential-equations/02-heat-equation.md).
- **Potential-field kernels.** Gravity and magnetic kernels for simple bodies
  are Green's functions, and the identical anomalies of different bodies are a
  statement about their non-uniqueness. See
  [01-06-08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md).
- **Ambient-noise interferometry.** Retrieving a Green's function by
  cross-correlating noise is the modern observational counterpart; see
  [06-seismology](../../06-seismology/README.md).

## 9. Further reading

- **Stakgold, I., & Holst, M. *Green's Functions and Boundary Value Problems.*
  Wiley.** The standard reference, covering construction by eigenfunction
  expansion and by the adjoint method, with the symmetry and positivity
  properties proved. Level: graduate.
- **Roach, G. F. *Green's Functions.* Cambridge University Press.** A compact
  and careful account, including the generalised Green's function for
  non-self-adjoint problems. Level: graduate.
- **Duffy, D. G. *Green's Functions with Applications.* Chapman & Hall/CRC.**
  Hundreds of worked constructions for the equations a physicist or engineer
  actually meets, including the heat and wave kernels. Level: advanced.
- **Bender, C. M., & Orszag, S. A. *Advanced Mathematical Methods for
  Scientists and Engineers.* Springer.** The chapter on Green's functions,
  including the asymptotic and boundary-layer methods that replace them when no
  closed form exists. Level: advanced.
- **Aki, K., & Richards, P. G. *Quantitative Seismology.* University Science
  Books.** The representation theorem, the moment tensor and the elastodynamic
  Green's function, in the notation of observational seismology. Level:
  graduate.
- **Dahlen, F. A., & Tromp, J. *Theoretical Global Seismology.* Princeton
  University Press.** The derivation of the representation theorem from first
  principles, with the reciprocity relations. Level: graduate to doctoral.
- **Havskov, J., & Ottemöller, L. *Routine Data Processing in Earthquake
  Seismology.* Springer.** Response removal as it is actually done, including
  the practical treatment of the low-frequency limit.
- **Nabighian, M. N. (ed.). *Electromagnetic Methods in Applied Geophysics,
  Vol. 1.* Society of Exploration Geophysicists.** The EM Green's function for
  a layered half-space and its use in forward modelling.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted
> text, and you should confirm current editions and availability through your
> library before citing them yourself.

## 10. Related lessons

- [03 Damped and Driven Oscillators as Physical Models](./03-oscillators.md) —
  the transfer function whose inverse transform is this lesson's central object.
- [05 Sturm–Liouville Theory and Eigenfunction Expansions](./05-sturm-liouville.md) —
  an alternative construction of the same Green's function, as a sum over
  eigenfunctions.
- [07 Stiff Systems and Numerical Stability Challenges](./07-stiff-systems.md) —
  what happens to the impulse response of a diffusion operator, where the
  relaxation is a continuum of timescales.
- [01-10-03 Convolution, Filtering and the Convolution Theorem](../10-fourier-analysis/03-convolution.md) —
  the transform side of the same statement.
- [01-11-06 Dispersion Relations and Causality](../11-complex-analysis/06-dispersion-relations.md) —
  the pole-placement argument of Section 3.7 in full.
- [01-09-02 The Diffusion/Heat Equation](../09-partial-differential-equations/02-heat-equation.md) —
  the Gaussian kernel and the diffusive length scale.
- [19-05-03 Numerical Green's Functions and Their Computation](../../19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/03-greens-function-numerics.md) —
  how the object is computed when no formula exists.
- [18-inverse-problems](../../18-inverse-problems/README.md) — deconvolution as
  a regularised inverse problem.

## Self-assessment checklist

- [ ] I can state the defining equation for a Green's function and the meaning
      of the homogeneous conditions. (2.1)
- [ ] I can derive $G$ for the first-order operator and for the damped
      oscillator, including the jump condition that fixes the amplitude. (3.1,
      3.2)
- [ ] I can explain why convolution gives the response to any source, and state
      the roles of linearity, causality and time invariance. (2.2)
- [ ] I can predict and verify the order of accuracy of a finite-width pulse.
      (3.2)
- [ ] I can verify a convolution against a direct ODE integration and say what
      the residual measures. (3.1, 3.3)
- [ ] I can explain why a node-centred source is exact for the three-point
      stencil and why a misplaced source costs an order. (3.5)
- [ ] I can state reciprocity and superposition and what they permit in data
      processing. (3.6)
- [ ] I can demonstrate causality from a transfer function and identify the
      pole placement that would break it. (3.7)
