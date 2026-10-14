---
id: 08-05-02
title: "Time-Domain EM (TDEM): Sounding, Transients and Decay Curves"
level: graduate
prereqs: ["02-07-04", "02-07-06", "08-05-01"]
tags: [geomagnetism, electromagnetism, tdem, diffusion, decay-curves, sounding]
---

# Time-Domain EM (TDEM): Sounding, Transients and Decay Curves

A time-domain system does the simplest possible thing to a conductive Earth: it
turns the transmitter off and listens. The primary field that dominated
[the frequency-domain measurement](01-frequency-domain-em.md) disappears in
microseconds, and what is left is the field of the eddy currents that the
transmitter induced — currents that must decay away, and that take a time set by
the conductivity and the size of the conductor. The measured quantity is a
**decay curve**, and every useful interpretation of it is a statement about
diffusion.

This lesson derives the two exact solutions that make TDEM quantitative: the
eigenmode decay of a body, and the self-similar spreading of a diffusing field.
Both are verified against a finite-difference solution of the same equation, so
the numbers can be trusted. The lesson then does something TDEM practice often
skips: it states precisely what a decay curve does and does not determine.

All models and data in this module are **SYNTHETIC**. Conductivities,
thicknesses, times and the noise level are chosen teaching values, not
measurements of a real ground or of a real instrument.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the magnetic diffusion equation
   $\partial_t \mathbf{B} = D\nabla^2\mathbf{B}$ with $D=1/(\mu_0\sigma)$ from
   Faraday's and Ampère's laws, and **state** why there is no wave speed in it.
2. **Derive** the eigenmode decay of a slab, $\tau_n=\mu_0\sigma d^2/(n^2\pi^2)$,
   by separation of variables, and **compute** the decay constant of a body.
3. **Derive** the halfspace similarity solution
   $B=B_0\operatorname{erf}\left(z/(2\sqrt{Dt})\right)$ and use its
   half-decay depth to show the depth scale grows as $\sqrt{t}$.
4. **Verify** a finite-difference solution against the analytic series, the exact
   *discrete* eigenvalue, and the similarity solution, and **report** the observed
   convergence order.
5. **Invert** a measured decay constant for a conductivity given a thickness, and
   **propagate** an error in the thickness into the conductivity.
6. **State** the $\sigma d^2$ versus $\sigma d$ ambiguity, and explain why the
   early-time amplitude and the late-time slope carry different information.
7. **Estimate** the usable late-time window from a stated noise floor, and explain
   why that window is a fixed fraction of the decay constant rather than a fixed
   time.

## Prerequisites

- [02-07-04 Electromagnetic Induction](../../02-physics/07-electromagnetism/04-em-induction.md)
  — Faraday's law, inductance and Lenz's law.
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
  — the diffusion equation in a conductor.
- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the same physics measured in the frequency domain, and the bucking problem
  that switch-off makes trivially easy.

## 1. What a TDEM system measures

A transmitter loop carries a current for a few milliseconds. During the "on"
time the current builds a magnetic field that penetrates the ground, limited by
diffusion to roughly one diffusion length. The current is then switched off as
fast as the circuit allows. Two things happen at once:

- the primary field of the loop collapses, so the enormous free-space coupling
  that dominates an FDEM measurement disappears after the switch-off ramp;
- the eddy currents induced in the ground are left to decay, and their field is
  the entire signal.

The receiver measures the **emf**, which is the negative time derivative of the
magnetic flux through it. Hence a TDEM record is a voltage (or a "dB/dt"
channel) as a function of time after the switch-off, in units of V or nT/s. Two
consequences shape the whole method:

- The measurement begins after a finite switch-off ramp; everything earlier is
  inaccessible. The **early-time** part of the record is limited by the
  transmitter, the **late-time** part by the receiver noise (Section 7).
- Because the primary is gone, TDEM needs no bucking. That is the single largest
  practical advantage over the frequency-domain geometry of
  [08-05-01](01-frequency-domain-em.md).

## 2. The diffusion equation

In a non-magnetic conductor with no free charge and no displacement current
(the criterion of [08-05-01 §3](01-frequency-domain-em.md)), the quasi-static
Maxwell pair is

$$\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t},
\qquad
\nabla\times\mathbf{B}=\mu_0\sigma\mathbf{E},$$

with $\mathbf{B}=\mu_0\mathbf{H}$. Taking the curl of the second equation and
substituting the first:

$$\nabla\times(\nabla\times\mathbf{B})
=\mu_0\sigma\nabla\times\mathbf{E}
=-\mu_0\sigma\frac{\partial\mathbf{B}}{\partial t}.$$

With $\nabla\cdot\mathbf{B}=0$ and the identity
$\nabla\times\nabla\times\mathbf{B}=\nabla(\nabla\cdot\mathbf{B})
-\nabla^2\mathbf{B}$,

$$\boxed{\;\frac{\partial\mathbf{B}}{\partial t}
=D\,\nabla^2\mathbf{B},\qquad
D=\frac{1}{\mu_0\sigma}\;\;[\mathrm{m^2\,s^{-1}}].\;}$$

This is the heat equation. There is no wave speed; the field does not travel, it
**diffuses**, and the depth it reaches in time $t$ is a length of order
$\sqrt{Dt}$:

$$\sqrt{D t}=
\begin{cases}
39.89\ \mathrm{m} & \sigma=0.5,\ t=1\ \mathrm{ms}\\
126.2\ \mathrm{m} & \sigma=0.05,\ t=1\ \mathrm{ms}\\
282.1\ \mathrm{m} & \sigma=0.01,\ t=1\ \mathrm{ms}\\
892.1\ \mathrm{m} & \sigma=0.001,\ t=1\ \mathrm{ms}
\end{cases}
\qquad
\sqrt{D\cdot1\ \mathrm{s}} = 3.99\ \mathrm{km}\ (\sigma=0.05).$$

Two lessons are already visible in that table. First, the *time* at which a
target answers is a direct measurement of depth: the same body at twice the depth
answers four times later. Second, the relevant quantity is always the product
$\mu_0\sigma t$, not either one alone.

## 3. Eigenmode decay of a conductive body

### 3.1 The slab problem and its solution

Consider a slab of thickness $d$ whose two faces are held at zero field (a
conducting host that screens the field, or the idealisation of a body much less
conductive than its surroundings). Take a field $B(z,t)\hat{\mathbf{z}}$ with
$B=1$ at $t=0$. Separating variables, $B(z,t)=Z(z)T(t)$ in the diffusion
equation gives

$$\frac{T'}{T}=D\frac{Z''}{Z}=-\frac{1}{\tau}
\quad\Longrightarrow\quad
Z(z)=\sin\frac{n\pi z}{d},\qquad
\boxed{\;\tau_n=\frac{\mu_0\sigma d^2}{n^2\pi^2}.\;}$$

The $t=0$ condition is expanded in the odd modes,
$B(z,0)=\sum_{n\ \mathrm{odd}}\frac{4}{n\pi}\sin\frac{n\pi z}{d}$, so

$$B(z,t)=\sum_{n\ \mathrm{odd}}\frac{4}{n\pi}
\sin\frac{n\pi z}{d}\,e^{-t/\tau_n}.$$

The demonstration prints, for the SYNTHETIC reference slab
($\sigma=0.01\ \mathrm{S\,m^{-1}}$, $d=20\ \mathrm{m}$):

$$\tau_1=\frac{\mu_0\sigma d^2}{\pi^2}=\frac{1.2566\times10^{-6}\times0.01
\times400}{9.8696}=0.5093\ \mathrm{\mu s},\qquad
\tau_2=\frac{\tau_1}{4}=0.1273\ \mathrm{\mu s}.$$

The structure is the physics: $\tau_1\propto\sigma d^2$, all higher modes decay
in a factor $n^2$ faster and are therefore invisible at late times, and the
answer is independent of the field amplitude (a linear problem).

*Worked example — other bodies.* For $\sigma=0.05\ \mathrm{S\,m^{-1}}$ and
$d=10\ \mathrm{m}$: $\tau_1 = \mu_0\sigma d^2/\pi^2
= 1.2566\times10^{-6}\times0.05\times100/9.8696 = 0.6366\ \mathrm{\mu s}$.
For $\sigma=0.005$ and $d=50\ \mathrm{m}$: $1.5915\ \mathrm{\mu s}$. Note which
pair wins: doubling the thickness (a factor $4$ in $\tau$) beats a tenfold
increase in conductivity (a factor $10$ in $\tau$) only when both are quotable —
the point is that $\tau$ alone cannot separate them (Section 5).

### 3.2 Verification against a finite-difference solution

The demonstration solves the same problem numerically,
$u^{n+1}_i=u^n_i+\lambda(u^n_{i+1}-2u^n_i+u^n_{i-1})$ with
$\lambda=D\,\Delta t/\Delta z^2=0.4$ (the stability limit is $0.5$), on a grid
whose nodes sit **on both faces**, where the Dirichlet conditions apply. Two checks
matter:

- **The discrete eigenvalue.** With $N$ cells the operator's fundamental
  eigenvalue is known exactly:
  $\tau_{\text{disc}}=d^2/\left[4DN^2\sin^2\left(\pi/(2N)\right)\right]$. At
  $N=32$, $\tau_{\text{disc}}=0.5097\ \mathrm{\mu s}$, which is $+0.0804\%$ from
  the continuum $0.5093\ \mathrm{\mu s}$.
- **The measured decay.** Starting from the exact eigenmode and fitting its
  decay, the demonstration recovers $\tau$ to within $7.7\times10^{-3}$ at
  $N=16$, $1.9\times10^{-3}$ at $N=32$, $4.8\times10^{-4}$ at $N=64$ and
  $1.2\times10^{-4}$ at $N=128$: each refinement divides the discrepancy by
  $4.00$. The residual is the first-order time-stepping error of the explicit
  scheme — confirmed by rerunning at $N=32$ with $\lambda=0.1$, which drops the
  discrepancy to $4.8\times10^{-4}$, a factor of four. The discrete eigenvalue
  itself converges to $\mu_0\sigma d^2/\pi^2$ as $\Delta z^2$ ($+3.2\times10^{-3}$,
  $+8.0\times10^{-4}$, $+2.0\times10^{-4}$, $+5.0\times10^{-5}$).

This is what "verified" means in this curriculum: agreement with a closed form,
plus a measured convergence order, plus an explanation of the residual.

### 3.3 The switch-off initial condition is a kink — and it costs

A real switch-off is not the fundamental eigenmode; it is closer to a *uniform*
field removed at both faces, which is a discontinuity at $t=0$. Fitting the late
window ($2.5$–$3.0\,\tau_1$, where the $n=3$ mode has decayed by $e^{-10}$) of
that run gives $\tau=0.5087\ \mathrm{\mu s}$, i.e. $0.9989$ of the continuum
value — the late-time slope is dominated by the fundamental eigenvalue, exactly
as the series predicts. But at $t=0.2\,\tau_1$ the numerical profile differs from
the analytic series by $2.99\times10^{-3}$ of the peak with $32$ cells: the kink
is resolved only to $O(\Delta z)$, so early-time amplitudes converge *more
slowly* than late-time decay constants. In practice this is why the early
channel of a TDEM record is the hardest part to model, not the easiest.

## 4. The similarity solution and the $\sqrt{t}$ depth law

Now let the ground be a halfspace with a uniform initial field $B_0$ which is
removed at the surface at $t=0$: $B(0,t)=0$ for $t>0$, $B(z,0)=B_0$,
$B\to B_0$ as $z\to\infty$. Seek $B=B_0 f(\zeta)$ with
$\zeta=z/(2\sqrt{Dt})$. Then

$$\frac{\partial B}{\partial t}=-B_0
\frac{z}{4\sqrt{D}\,t^{3/2}}f'(\zeta),\qquad
\frac{\partial^2 B}{\partial z^2}
=\frac{B_0}{4Dt}f''(\zeta),$$

so the diffusion equation collapses to $f''+2\zeta f'=0$, with solution
$f=\operatorname{erf}(\zeta)$ satisfying $f(0)=0$, $f(\infty)=1$. Hence

$$\boxed{\;B(z,t)=B_0\operatorname{erf}\!\left(\frac{z}{2\sqrt{Dt}}\right).\;}$$

The demonstration's finite-difference halfspace run reproduces this to
$3.2\times10^{-5}$ of the initial field at $t=66.7\ \mathrm{\mu s}$ and to about
$10^{-5}$ over the rest of the run. The **half-decay depth** is where
$\operatorname{erf}=1/2$, i.e. $\zeta=0.4769$, giving

$$z_{1/2}=0.9539\sqrt{Dt},$$

and the measured exponent of $z_{1/2}$ against $t$ is $0.5000$ for the whole run
(Table in the demonstration: $31.07\ \mathrm{m}$ at $66.7\ \mathrm{\mu s}$,
$76.11\ \mathrm{m}$ at $400\ \mathrm{\mu s}$, both matching $0.9539\sqrt{Dt}$ to
$0.01\ \mathrm{m}$). Two depth scales are in circulation and differ by
$\sqrt2$: $\sqrt{2t/(\mu_0\sigma)}$ and $\sqrt{4Dt}$. For
$\sigma=0.01\ \mathrm{S\,m^{-1}}$ at $t=1\ \mathrm{ms}$ they are $398.9\ \mathrm{m}$
and $564.2\ \mathrm{m}$. They are the same length scale with different
conventions for locating the "front"; a number quoted without its definition is
not usable.

**Interpretive consequence.** A decay curve is a depth sounding *because* the
diffusion front advances as $\sqrt{t}$: early channels see the shallow
conductors, late channels see the deep ones. But the front is broad (the profile
is an error function, not a step), so "the depth of the conductor" is always a
statement about the part of the record the conductor dominates — which is
Section 5.

## 5. What a decay curve determines, and what it does not

The decay constant gives **one** number, $\sigma d^2$ per unit thickness scale:

$$\tau_1=\frac{\mu_0\sigma d^2}{\pi^2}
\quad\Longrightarrow\quad
\sigma d^2 = \frac{\pi^2\tau_1}{\mu_0}.$$

The demonstration makes the ambiguity explicit: four synthetic bodies,

| $\sigma$ (S/m) | $d$ (m) | $\sigma d$ (S) | $\tau_1$ ($\mathrm{\mu s}$) |
|---|---|---|---|
| 0.01000 | 20.0 | 0.20000 | 0.5093 |
| 0.04000 | 10.0 | 0.40000 | 0.5093 |
| 0.00250 | 40.0 | 0.10000 | 0.5093 |
| 0.16000 | 5.0 | 0.80000 | 0.5093 |

have *identical* decay constants. Their conductances $\sigma d$ differ by a
factor of 8, which is precisely why the **early-time amplitude** matters: for a
slab in a normal field $B_0$, the flux that must be removed per unit area is
$B_0d$, and it is removed by a sheet of conductance $\sigma d$. So

- the **late-time slope** measures $\sigma d^2$,
- the **early-time amplitude** measures $\sigma d$ (times the geometry and the
  transmitter moment),
- and the *pair* gives $\sigma$ and $d$ separately — but only if the model is
  right and only within the noise.

Two caveats must be stated with that. First, if the geology is one conductive
sheet (a thin, laterally extensive conductor), then $\sigma d$ and $d$ are not
both physical parameters: a TDEM sounding measures the **conductance** $\sigma d$
of such a sheet and the depth to it, and never its thickness. That is not a
failure of the method; it is the correct parameterisation, and the standard
practice of TDEM interpretation is to report conductance–depth pairs. Second, if
the body is three-dimensional and small, the "conductance" idea itself becomes an
approximation, and the decay is no longer a sum of slab eigenmodes but a
superposition with a geometry-dependent spectrum — the subject of
[08-05-03 EM Forward Modelling](03-em-modelling.md).

## 6. Fully worked numeric example

A decay curve from a SYNTHETIC survey over a $20\ \mathrm{m}$-thick body decays
with $\tau=0.5093\ \mathrm{\mu s}$ (fitted over $2.5$–$3.0\tau_1$; the measured
value in the numerical run is $0.5087\ \mathrm{\mu s}$, $0.13\%$ lower, which is
the discretisation of the switch-off kink, not noise).

1. Invert for the conductivity, assuming $d=20\ \mathrm{m}$:

$$\sigma=\frac{\pi^2\tau}{\mu_0d^2}
=\frac{9.8696\times0.5093\times10^{-6}}
{1.2566\times10^{-6}\times400}
=\frac{5.0263\times10^{-6}}{5.0265\times10^{-4}}
=0.0100\ \mathrm{S\,m^{-1}},$$

which is the input value to three figures. The round trip is exact because the
relation is algebraic.

2. Propagate a thickness error. From $\sigma\propto\tau d^{-2}$,

$$\frac{\delta\sigma}{\sigma}=\frac{\delta\tau}{\tau}
+2\frac{\delta d}{d}.$$

A $10\%$ error in the thickness — entirely typical for a body whose extent is
inferred from a single sounding — produces a $20\%$ error in the conductivity.
**The depth is the weak link, and the depth is what a TDEM sounding determines
least directly.**

3. Convert to a conductance, which is the quantity the data actually control:
$\sigma d = 0.0100\times20 = 0.20\ \mathrm{S}$. If the same decay curve came from
a $5\ \mathrm{m}$ body, the conductivity would be
$\sigma = \pi^2\tau/(\mu_0 25) = 0.64\ \mathrm{S\,m^{-1}}$ and the conductance
$0.64\times5 = 3.2\ \mathrm{S}$ — a factor of 16 different in conductance from the
same measured decay constant. Nothing in the late-time curve distinguishes them.

4. Time scale. The whole measurement occupies $0.5\ \mathrm{\mu s}$ of decay
constant, i.e. a usable window of about $8.5\tau_1 = 4.3\ \mathrm{\mu s}$ at a
$1\times10^{-4}$ noise floor (Section 7). A TDEM system whose earliest usable
channel is $10\ \mathrm{\mu s}$ after switch-off cannot see this body at all: the
target's decay is over before the receiver is listening. Conductivity and *system
timing* must be matched.

## 7. Noise, the usable window, and the detection limit

Let the noise be $1\times10^{-4}$ of the initial amplitude per sample. The decay
falls below it when $e^{-t/\tau}>2\times10^{-4}$, i.e. at $t=8.52\,\tau_1$ — the
same fraction of $\tau_1$ for every conductivity:

| $\sigma$ (S/m) | $\tau_1$ ($\mathrm{\mu s}$) | window ends ($\tau_1$) | window ends ($\mathrm{\mu s}$) |
|---|---|---|---|
| 1.0000 | 50.93 | 8.52 | 433.7 |
| 0.1000 | 5.093 | 8.51 | 43.37 |
| 0.0100 | 0.5093 | 8.52 | 4.337 |
| 0.0010 | 0.05093 | 8.52 | 0.4337 |

The window in *time* scales with the conductivity; the window in *units of the
decay constant* does not. Fitting $\tau$ over $0.1$–$3.0\tau_1$ with 40 samples
and this noise, 200 realisations give a mean of $0.5093\ \mathrm{\mu s}$ (bias
$+0.002\%$) and a standard deviation of $0.0001\ \mathrm{\mu s}$
($0.020\%$ of $\tau_1$) — so the *statistical* precision is far better than the
*model* precision, which is limited by the thickness unknown of Section 6. That
inversion of the usual ranking (model error dominating noise) is the normal
situation in EM, and it is the reason this module insists on stating what is
measured separately from what is modelled.

## 8. Assumptions and regime of validity

1. **Quasi-static.** $\omega\varepsilon_0/\sigma\ll1$; the same criterion as
   [08-05-01](01-frequency-domain-em.md). For the *transient* problem the relevant
   statement is that the shortest time in the record exceeds
   $\varepsilon_0/\sigma$ — for $\sigma=10^{-2}\ \mathrm{S\,m^{-1}}$ that is
   $8.9\times10^{-10}\ \mathrm{s}$, never a limitation in geophysics, but a real
   one for a laboratory measurement on a good conductor.
2. **Non-magnetic ground.** $\mu=\mu_0$ inside the conductor. Ferromagnetic
   ground invalidates the diffusion constant and is a real limitation in
   magnetic soils.
3. **Linear and Ohmic.** The decay is independent of the transmitter current and
   obeys superposition. Induced polarisation violates this and is measured as
   such.
4. **The slab model is an idealisation.** Its two faces at zero field stand for a
   conductor bounded by much more resistive material. A body with a resistive skin
   or a gradational boundary has a different, broader spectrum than
   $\sum e^{-t/\tau_n}$.
5. **No self-induction.** The derivation omits the fact that the decaying
   currents' own field drives them (inductive retardation), which matters when the
   body is large compared with the diffusion length
   $(\mu_0\sigma d^2\omega\gtrsim1$, i.e. at early times). It is why early-time
   amplitudes are fitted, not inverted analytically.
6. **The fit window is a choice, and it is part of the answer.** A slope fitted
   over $0.5$–$1.5\tau_1$ is contaminated by the $n=3$ mode; one fitted over
   $20$–$30\tau_1$ is noise. State the window, as the demonstration does.
7. **3-D bodies are out of scope.** Everything in Sections 3–6 is one-dimensional.
   The 3-D problem needs the machinery of
   [08-05-03 EM Forward Modelling](03-em-modelling.md).

## 9. Python demonstration

`code/tdem_decay_demo.py` computes everything above. It:

1. tabulates the diffusion constant and the diffusion length, and prints the
   worked-example decay constants and depth scales used here;
2. solves the slab problem by finite differences, measures the decay constant,
   and compares it with the discrete and continuum eigenvalues;
3. solves the halfspace problem, compares the profile with
   $B_0\operatorname{erf}(z/(2\sqrt{Dt}))$, and measures the $\sqrt{t}$ exponent;
4. tabulates the $\sigma d^2$ ambiguity and the conductance that separates it;
5. reports the convergence of the scheme (ratios of $4.00$ on refining);
6. propagates a synthetic noise floor into the usable window and into a
   Monte-Carlo distribution of recovered decay constants (200 realisations).

It is print-only, uses `np.random.default_rng(20261014)`, needs no network, and
finishes in about a third of a second.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/02-time-domain-em-exercises.md`](./exercises/02-time-domain-em-exercises.md)
and
[`exercises/02-time-domain-em-solutions.md`](./exercises/02-time-domain-em-solutions.md).

- **★** Compute $\tau_1$, $\tau_2$ and the diffusion length for
  $\sigma=0.02\ \mathrm{S\,m^{-1}}$, $d=30\ \mathrm{m}$.
- **★★** Derive $\tau_n=\mu_0\sigma d^2/(n^2\pi^2)$ from the diffusion equation
  and boundary conditions, showing the separation constant.
- **★★** A decay curve gives $\tau=2.0\ \mathrm{\mu s}$. Quantify everything a
  late-time-only interpretation can say about it.
- **★★★** Design a two-channel (early amplitude, late slope) experiment to
  separate $\sigma$ from $d$ for a $20$–$50\ \mathrm{m}$ conductor, and state the
  largest source of error.

## Mastery checkpoint

Without notes:

> A SYNTHETIC TDEM sounding over a compact body gives a late-time decay
> $\tau=(1.00\pm0.01)\ \mathrm{\mu s}$ and an early-time amplitude implying a
> conductance $\sigma d=(0.30\pm0.03)\ \mathrm{S}$. **(a)** Compute $\sigma d^2$
> from $\tau$. **(b)** Hence solve for $d$ and $\sigma$ separately, and give each
> with its uncertainty. **(c)** State which of the two is better determined and
> why. **(d)** The same decay is observed at a site $200\ \mathrm{m}$ away with
> the same amplitude. What does that tell you about the body's lateral extent?
> **(e)** Name one measurement that would test the slab assumption.

## Common pitfalls

1. **Quoting a conductivity without a thickness.** $\tau$ measures
   $\sigma d^2$; the conductivity is a derived quantity.
2. **Fitting the whole decay.** The early part carries the transmitter ramp- and
   self-induction-dominated behaviour, and the late part is noise. State the
   window.
3. **Confusing the two depth scales.** $\sqrt{2t/(\mu_0\sigma)}$ and
   $\sqrt{4Dt}$ differ by $\sqrt2$; quote the definition.
4. **Using a diffusion length as a resolution.** The diffusion front is an error
   function, not a step; "detectable at" is not "resolved at".
5. **Assuming the late-time slope is unbiased.** It is a good measurement *if* the
   body is a slab and the window is late enough; otherwise it is a mixture of the
   geometry and the spectrum.
6. **Forgetting the timing window.** A useful body can decay entirely before the
   first usable channel.
7. **Reading "apparent conductivity" as a conductivity.** In TDEM practice it is
   usually a conductance–depth pair in disguise.

## Related modules

- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the same diffusion problem, measured in the frequency domain.
- [08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods](03-em-modelling.md)
  — the three-dimensional version of the slab problem solved here.
- [08-05-04 EM Inversion and Dimensionality](04-em-inversion.md) — what the
  $\sigma d^2$ ambiguity looks like as a null space.
- [08-05-05 Airborne EM for Conductivity Mapping](05-airborne-em.md) — TDEM and
  FDEM as flown, where the height unknown replaces the thickness unknown.
- [08-04-01 Induction, Skin Depth, Diffusion and Conductivity Structure](../04-electromagnetic-induction/01-em-induction-basics.md)
  — conductivity ranges and the induction picture.
- [01-09 Partial Differential Equations](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md)
  — separation of variables and similarity solutions, used here without proof.
