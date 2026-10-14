---
id: 08-05-01
title: "Frequency-Domain EM (FDEM) Systems and Responses"
level: graduate
prereqs: ["02-07-04", "02-07-06", "08-04-01"]
tags: [geomagnetism, electromagnetism, fdem, skin-depth, induction-number, coil-systems]
---

# Frequency-Domain EM (FDEM) Systems and Responses

A controlled-source electromagnetic (CSEM) survey replaces the Sun and the
ionosphere with a generator. That single change buys amplitude, repeatability and
geometry — and it costs nothing in honesty, because the physics of a conductive
Earth is the same diffusion problem either way. This lesson derives what a
frequency-domain system measures, in the one geometry where the answer can be
written down exactly: a vertical magnetic dipole (a horizontal loop) as
transmitter, and the vertical magnetic field measured at a second coil a
distance $r$ away. The pair is called a **horizontal coplanar** (HCP) system, and
it is the backbone of ground and airborne FDEM.

The second half of the lesson is about the two numbers that decide whether the
measurement means anything: the **induction number** $\theta = r/\delta$, the
ratio of the geometry to the skin depth, and the **coupling** between the coils
in free space, which must be removed before the ground signal is visible. Both
are derived, both are verified numerically, and the residual ambiguity between
conductivity and separation is stated rather than hidden.

All models and data in this module are **SYNTHETIC**. The conductivities,
separations, frequencies and noise level below are chosen teaching values, not
measurements of a real ground or of a real instrument.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the diffusive (quasi-static) field equation in a conductor from
   Faraday's and Ampère's laws, and **state** the exact criterion that licenses
   dropping displacement current.
2. **Compute** the skin depth $\delta=\sqrt{2/(\omega\mu_0\sigma)}$ and the
   induction number $\theta=r/\delta$, and **explain** in one sentence why one
   skin depth corresponds to one radian of phase.
3. **Derive** the free-space primary coupling of a coplanar coil pair, obtain the
   dipole limit $M=-\mu_0A_1A_2/(4\pi s^3)$, and **explain** why the free-space
   term is called the *bucking* problem.
4. **Derive** the exact halfspace response as a Sommerfeld (Hankel) integral from
   the Hertz potential and the interface conditions.
5. **Verify** a numerical response against three independent things: an adaptive
   quadrature of the unregularised kernel, the perfect-conductor image limit, and
   the analytic weak-induction asymptote.
6. **Quantify** the error of the low-induction-number (LIN) form — about
   $1.5\theta$ relative — and **propagate** it into an apparent conductivity.
7. **State** the conductivity–separation ambiguity and name the two ways an
   instrument breaks it.

## Prerequisites

- [02-07-04 Electromagnetic Induction](../../02-physics/07-electromagnetism/04-em-induction.md)
  — Faraday's law and the definition of inductance.
- [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
  — the diffusion equation and the skin depth.
- [08-04-01 Induction, Skin Depth, Diffusion and Conductivity Structure](../04-electromagnetic-induction/01-em-induction-basics.md)
  — the conductivity of rocks and the induction picture of exploration EM.

## 1. Why a controlled source, and what it does not buy

A natural-source measurement (magnetotellurics) is limited by the source: you work
with whatever the ionosphere provides. A controlled source fixes the geometry,
fixes the waveform and lets you repeat the experiment until the noise averages
down. What it does **not** do is change the physics: below a few hundred kilohertz
the field in the ground still satisfies the diffusion equation, and the response
of a homogeneous halfspace is still a monotonically increasing function of the
single dimensionless group $\omega\mu_0\sigma r^2/4$. That last fact has a sharp
consequence — see Section 8 — that no amount of engineering removes.

The reason controlled sources matter is that the interesting targets are *small*:
a mineralised body of a few tens of metres. Diffusion smooths structure over a
skin depth, so the usable information about a small body lives in the residual
after a much larger, much smoother background has been modelled and removed.
Everything in this module is about making that residual trustworthy.

## 2. What is measured, and in what units

A FDEM system is a **transmitter coil** carrying an alternating current and one or
more **receiver coils**. The primary field of a coil is proportional to its
current and to its area (its *moment* $m=NAI$, in $\mathrm{A\,m^2}$), so the
primary field at the receiver is a known multiple of the transmitter current. The
signal of interest is the **secondary** field of the induced currents in the
ground, and it is quoted as a **ratio**:

$$S(\omega) \;=\; \frac{H_s(\omega)}{H_p(\omega)} \;=\;
\underbrace{\mathrm{Re}\,S}_{\text{in-phase}} \;+\; i\,
\underbrace{\mathrm{Im}\,S}_{\text{quadrature}}.$$

Two conventions matter and both must be stated.

- **Time dependence.** We take fields to vary as $e^{+i\omega t}$. Then the
  quadrature is the imaginary part of $S$, and a *good* conductor gives a
  *negative* in-phase part in this convention. Instruments and papers use either
  sign; a defensible figure caption says which. The magnitude and the frequency
  scaling do not depend on the convention, only the sign of the imaginary part
  does.
- **Field ratio or electromotive force.** A real receiver measures an emf
  proportional to $i\omega$ times the field, so a manufacturer's "ppm" curve is
  $i\omega S$ normalised in some stated way. When comparing numbers, check which
  quantity is being quoted; a factor of $\omega$ and a phase shift of
  $90^\circ$ are easy to lose.

The ratio is small. It is customary to quote it in **parts per million** (ppm) of
the primary, $S \times 10^6$, because in the transparent-ground regime it is of
order $10^{-5}$ to $10^{-3}$ (Sections 5–6). The primary coil current is switched
off in phase with the measured quantity — this is called **bucking** — and its
magnitude, derived next, is the reason instruments are built the way they are.

### 2.1 Geometry taxonomy

| Configuration | Transmitter | Receiver measures | Notes |
|---|---|---|---|
| Horizontal coplanar (HCP) | vertical dipole (horizontal loop) | $H_z$ | the geometry of this lesson |
| Vertical coplanar (VCP) | vertical dipole | $H_r$ | better at low $\theta$ |
| Coaxial | vertical dipole | $H_z$ on the axis | nulls for layered ground in the far field |
| Grounded wire / loop | horizontal dipole / large loop | multiple components | the marine and deep CSEM family |

## 3. The governing equation and the skin depth

In a non-magnetic conductor with conductivity $\sigma$ and no free charge, the
quasi-static Maxwell pair is

$$\nabla\times\mathbf{E}=-\mu_0\frac{\partial\mathbf{H}}{\partial t},
\qquad
\nabla\times\mathbf{H}=\sigma\mathbf{E}.$$

Take the curl of the second and substitute the first:

$$\nabla\times(\nabla\times\mathbf{H}) = \sigma\nabla\times\mathbf{E}
= -\mu_0\sigma\frac{\partial\mathbf{H}}{\partial t}
\quad\Longrightarrow\quad
\nabla^2\mathbf{H}=\mu_0\sigma\frac{\partial\mathbf{H}}{\partial t},$$

using $\nabla\cdot\mathbf{H}=0$. For $e^{+i\omega t}$ a plane wave
$\propto e^{ikz}$ requires $k^2=i\omega\mu_0\sigma$, so

$$\boxed{\;k=\frac{1+i}{\delta},\qquad
\delta=\sqrt{\frac{2}{\omega\mu_0\sigma}}.\;}$$

Writing $k=(1+i)/\delta$ and $e^{ikz}=e^{iz/\delta}e^{-z/\delta}$: the amplitude
falls by $1/e$ in one skin depth **and** the phase is retarded by exactly one
radian. Those two facts are one fact — amplitude and phase are the real and
imaginary parts of the same complex wavenumber — which is why a FDEM system
records both.

*Displacement current.* Dropping $\partial\mathbf{D}/\partial t$ from Ampère's law
is legitimate when $\omega\varepsilon_0 \ll \sigma$. With
$\varepsilon_0=8.854\times10^{-12}\ \mathrm{F\,m^{-1}}$ (exact SI value) and
$\sigma=0.05\ \mathrm{S\,m^{-1}}$, the demonstration prints
$\omega\varepsilon_0/\sigma$ from $1.11\times10^{-7}$ at $100\ \mathrm{Hz}$ to
$1.11\times10^{-4}$ at $100\ \mathrm{kHz}$: at least four orders of magnitude of
margin over the whole band. In ice ($\sigma\sim10^{-5}\ \mathrm{S\,m^{-1}}$) or at
radar frequencies the criterion fails and the equations become wave equations —
that is precisely why ground-penetrating radar is a different method.

### 3.1 Worked example — skin depth and induction number

Take the lesson's SYNTHETIC reference model: $\sigma=0.02\ \mathrm{S\,m^{-1}}$,
coil separation $r=15\ \mathrm{m}$, frequency $f=10^3\ \mathrm{Hz}$. With
$\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ (exact in SI),

$$\omega = 2\pi f = 6283.1853\ \mathrm{rad\,s^{-1}},$$
$$\omega\mu_0\sigma = 6283.1853 \times 1.2566\times10^{-6} \times 0.02
= 1.5791\times10^{-4}\ \mathrm{m^{-2}},$$
$$\delta=\sqrt{\frac{2}{\omega\mu_0\sigma}}
= \sqrt{1.2665\times10^{4}} = 112.540\ \mathrm{m},\qquad
\theta=\frac{r}{\delta}=0.1333.$$

The demonstration prints these four numbers, and they are the ones used in
Sections 6 and 7. Note the first thing a reader should notice: a $1\ \mathrm{kHz}$
signal in a $40\ \Omega\,\mathrm{m}$ ground reaches only about $113\ \mathrm{m}$
in one skin depth, so a $15\ \mathrm{m}$ geometry sits comfortably inside the
weak-induction regime.

## 4. Primary coupling and why bucking dominates the design

The primary voltage at the receiver is set by the **mutual inductance** of the two
loops, defined exactly by the Neumann double integral

$$M=\frac{\mu_0}{4\pi}\oint_{C_1}\oint_{C_2}\frac{\mathrm{d}\mathbf{l}_1\cdot
\mathrm{d}\mathbf{l}_2}{R},$$

with $R$ the distance between the two line elements. For two coplanar circles of
radii $a,b$ with centre separation $s$, the demonstration evaluates this integral
directly and compares it with the dipole limit. The dipole limit follows from the
static field of a vertical dipole $m$ at the origin, whose vertical component is

$$H_z=\frac{m\left(2z^2-\rho^2\right)}{4\pi\left(\rho^2+z^2\right)^{5/2}},
\qquad\text{so at } z=0:\quad H_z=-\frac{m}{4\pi\rho^{3}}.$$

Flux through the second loop is $\mu_0 H_z \pi b^2$, giving

$$M_{\text{dipole}}=-\frac{\mu_0\pi a^2b^2}{4s^{3}}.$$

The demonstration (loop radius $1\ \mathrm{m}$) prints
$M_{\text{num}}=-1.24069\times10^{-10}\ \mathrm{H}$ against
$M_{\text{dipole}}=-1.23370\times10^{-10}\ \mathrm{H}$ at $s=20\ \mathrm{m}$ — a
$0.57\%$ difference — and a measured log–log slope of $|M|$ against separation of
$-3.043$ against the theoretical $-3$. Two things follow.

- The **sign** is negative: coplanar coils couple with opposite polarity.
- The free-space primary falls only as $1/s^3$, while the ground response at the
  same separation is of order $10^{-5}$ of it (Section 6). At $s=20\ \mathrm{m}$
  the primary is therefore some five orders of magnitude larger than the signal.
  An instrument that measured the total field would need $160\ \mathrm{dB}$ of
  dynamic range *and* a stability better than $1\ \mathrm{ppm}$ in the primary
  coupling to see the ground at all. Bucking — a third, adjustable coil, or an
  electronic null calibrated in free space — is not an accessory; it is what makes
  the measurement possible, and every residual error in the bucking appears
  directly as a false in-phase response.

## 5. The exact halfspace response

### 5.1 From a Hertz potential to one quadrature

Let the ground occupy $z>0$ and the coils sit at height $h$ in the insulating air
$z<0$, separated horizontally by $r$. A vertical magnetic dipole is a TE source,
so it is represented by a **vertical electric Hertz vector**
$\boldsymbol{\Pi}=\Pi\,\hat{\mathbf{z}}$, with

$$\mathbf{E}=-i\omega\mu_0\nabla\times(\Pi\hat{\mathbf{z}}),\qquad
\mathbf{H}=\nabla\times\nabla\times(\Pi\hat{\mathbf{z}}),$$

so that $\Pi$ satisfies Laplace's equation in the air and
$\nabla^2\Pi=k^2\Pi$ in the ground, with $\Pi$ and $\partial\Pi/\partial z$
continuous at $z=0$ (equivalently: tangential $\mathbf{E}$ and tangential
$\mathbf{H}$ continuous). Taking Hankel transforms in $\rho$,
$J_0(\lambda\rho)$, the air solution for a source at height $h$ is

$$\Pi_a=\frac{m}{4\pi}\int_0^\infty\left[
e^{-\lambda(z+h)}+A(\lambda)e^{\lambda z}\right]J_0(\lambda\rho)\,\mathrm{d}\lambda,
\qquad A=R(\lambda)e^{-\lambda h},$$

and the ground solution is $\Pi_e=\frac{m}{4\pi}\int_0^\infty
B(\lambda)e^{-uz}J_0(\lambda\rho)\,\mathrm{d}\lambda$ with
$u=\sqrt{\lambda^2+k^2}$, $\operatorname{Re}u>0$. Imposing the two interface
conditions gives $B=2\lambda e^{-\lambda h}/(\lambda+u)$, hence the **TE reflection
coefficient**

$$\boxed{\;R(\lambda)=\frac{\lambda-u}{\lambda+u}
=-\frac{k^2}{\left(\lambda+u\right)^{2}}\;}$$

using $\lambda^2-u^2=-k^2$. The secondary vertical field at the receiver
($z=-h$, using $H_z=\partial_z^2\Pi-\nabla^2\Pi= \partial_z^2\Pi$ in the air) and
the primary $H_p=-m/(4\pi r^3)$ give the response

$$\boxed{\;S(\omega)=\frac{H_s}{H_p}
=-r^3\int_0^\infty \lambda^2 R(\lambda)e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda.\;}$$

### 5.2 A form that can be evaluated

For numerical work, split the kernel at its large-$\lambda$ limit. Since
$\lambda^2R\to-k^2/4$ while $\lambda\to\infty$, write
$\lambda^2R=-k^2/4+\left(\lambda^2R+k^2/4\right)$ and use
$\int_0^\infty e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda
=1/\sqrt{r^2+4h^2}$ (the Weber–Schafheitlin identity, exact; at $h=0$ it reduces
to $\int_0^\infty J_0(\lambda r)\,\mathrm{d}\lambda=1/r$, conditionally
convergent). With $\lambda^2R+k^2/4=k^4(u+3\lambda)/\left[4(\lambda+u)^3\right]$
— which is manifestly of order $k^4$, so the second piece is the *correction*:

$$S(\omega)=\underbrace{\frac{k^2r^3}{4\sqrt{r^2+4h^2}}}_{\text{LIN term}}
-\;r^3\underbrace{\int_0^\infty\frac{k^4}{4}
\frac{u+3\lambda}{\left(\lambda+u\right)^3}e^{-2\lambda h}J_0(\lambda r)
\,\mathrm{d}\lambda}_{\text{correction}}.$$

### 5.3 The low-induction-number (LIN) limit

Let $\sigma\to0$ so $u\to\lambda$: the correction vanishes and

$$S_{\text{LIN}}=\frac{k^2r^2}{4}\frac{r}{\sqrt{r^2+4h^2}}
\;\xrightarrow[h=0]{}\;
\frac{k^2r^2}{4}=\frac{i\,\omega\mu_0\sigma r^2}{4}.$$

This is the **whole-space (weak-induction) response**. Its quadrature is
$\omega\mu_0\sigma r^2/4$ and its in-phase part vanishes at leading order: a
transparent ground lags the primary by $90^\circ$ exactly. That is the origin of
the word *quadrature* in FDEM practice and of the phrase "in-phase is a second
order quantity" — with an important qualification quantified in Section 7.

### 5.4 The perfect-conductor limit

Let $\sigma\to\infty$, so $u\to\infty$ and $R\to-1$: the ground becomes a mirror
and the field is that of the image dipole, of opposite sign at depth $2h$. With
the primary $H_p=-m/(4\pi r^3)$ this gives the **screening** limit

$$S_\infty=\frac{r^3\left(8h^2-r^2\right)}
{\left(r^2+4h^2\right)^{5/2}},\qquad
S_\infty(h=0)=-1.$$

The minus one is a strong statement: at the surface of a perfect conductor the
total vertical field is zero, the secondary field cancels the primary exactly, and
no information about a deeper conductor can reach the receiver at that frequency.
A real ground approaches this behaviour as $\theta$ grows (Section 7).

## 6. Fully worked numeric example

Using the demonstration's reference model ($\sigma=0.02\ \mathrm{S\,m^{-1}}$,
$r=15\ \mathrm{m}$, $f=10^3\ \mathrm{Hz}$, $\theta=0.1333$):

$$S_{\text{LIN}}=\frac{i\omega\mu_0\sigma r^2}{4}
=\frac{i(1.5791\times10^{-4})(225)}{4}
=i\,8.8826\times10^{-3},$$

so the LIN prediction is $8882.6\ \mathrm{ppm}$ of quadrature and zero in-phase.
The exact evaluation of the integral gives

$$S = 1.111462\times10^{-3} + i\,7.625809\times10^{-3},$$

that is $1111.5\ \mathrm{ppm}$ in-phase and $7625.8\ \mathrm{ppm}$ quadrature.
Three observations, all quantitative:

1. The quadrature is **$14\%$ smaller** than LIN predicts. Section 7 shows this is
   the systematic LIN bias, of order $1.5\theta = 0.20$ in magnitude; the
   difference here is a bias, not noise.
2. The in-phase part is **not zero**: it is $15\%$ of the quadrature. For a
   halfspace the in-phase part is not a second-order curiosity — it is smaller
   than the quadrature by one factor of $\theta$ (measured scaling exponent
   $1.496$ against the quadrature's $0.995$ in the demonstration).
3. Inverting the LIN formula for an apparent conductivity,

$$\sigma_{\text{app}}=\frac{4\,\mathrm{Im}\,S}{\omega\mu_0 r^2}
=\frac{4\left(7.6258\times10^{-3}\right)}
{6283.1853\times1.2566\times10^{-6}\times225}
=0.017170\ \mathrm{S\,m^{-1}},$$

which is $14.15\%$ **below** the true $0.02\ \mathrm{S\,m^{-1}}$. The bias is the
same $14\%$ as observation 1, because in the LIN regime $\sigma_{\text{app}}$ is
simply proportional to $\mathrm{Im}\,S$.

## 7. Verification, and the measured limits of the approximation

The demonstration verifies the response four ways. Each is an independent check
of a different part of the derivation.

**(a) Adaptive quadrature of the unregularised kernel.** A second code path
integrates $\lambda^2R(\lambda)e^{-2\lambda h}J_0(\lambda r)$ directly with an
adaptive scheme and no analytic term. At $h=2\ \mathrm{m}$ the two routes agree to
$6.5\times10^{-10}$ relative at $10\ \mathrm{Hz}$ and $9.0\times10^{-8}$ at
$1\ \mathrm{kHz}$; at $h=20\ \mathrm{m}$ to $1.6\times10^{-8}$ and
$2.5\times10^{-6}$. The split of Section 5.2 is therefore not changing the
answer. At $h=0$ the unregularised integral converges only conditionally (its
kernel tends to the constant $-k^2/4$), which is exactly why the split is used
there and why the checks below carry the weight at zero height.

**(b) The analytic weak-induction limit.** The LIN term's height dependence
$r/\sqrt{r^2+4h^2}$ is an exact consequence of the Weber–Schafheitlin identity.
At $f=0.05\ \mathrm{Hz}$ ($\theta=0.0020$) the measured ratio of responses at
$h$ and $h=0$ is $0.894205$ against the predicted $0.894427$ at $h=5\ \mathrm{m}$
and $0.240947$ against $0.242536$ at $h=40\ \mathrm{m}$; the residual is itself
of order $\theta$ and shrinks as the frequency is lowered, as the argument
requires.

**(c) The LIN bias, measured.** Holding the model fixed and lowering the
frequency to make $\theta$ small:

| $\theta$ | 0.002 | 0.005 | 0.01 | 0.02 | 0.05 |
|---|---|---|---|---|---|
| $\lvert S/S_{\text{LIN}}-1\rvert$ | 0.003014 | 0.007525 | 0.015014 | 0.029888 | 0.073677 |
| ratio to $\theta$ | 1.5071 | 1.5050 | 1.5014 | 1.4944 | 1.4735 |

The measured exponent of the deviation against $\theta$ is $0.993$: the LIN form
carries a **relative error of about** $1.5\theta$, a bias rather than a scatter.
The reason is structural: $u=\sqrt{\lambda^2+k^2}$ has a branch point at
$\lambda=\pm ik$, so the response is *not* a power series in $\omega$; the branch
cut generates odd powers of $k$, and the first of them is what the $1.5\theta$
term is. That is also why the in-phase part scales as $\omega^{3/2}$ for a
halfspace rather than the $\omega^2$ that a single-relaxation-time target gives.

**(d) Scale invariance, and the ambiguity it exposes.** The response depends on
$\sigma$, $\omega$ and $r$ only through $kr=(1+i)\theta$; substituting
$\lambda=x/r$ into the integral proves it in one line. The demonstration confirms
it numerically: $\sigma=0.05\ \mathrm{S\,m^{-1}}$ with $r=20\ \mathrm{m}$,
$\sigma=0.0125$ with $r=40$, $\sigma=0.2$ with $r=10$ and $\sigma=0.003125$ with
$r=80$ all give
$S=+8.98089260\times10^{-3}+2.78802350\times10^{-2}i$ at $1\ \mathrm{kHz}$, to every
digit printed.

This is the **conductivity–separation ambiguity**: a single frequency and a single
separation determine $\sigma r^2$, not $\sigma$. A ground four times more
conductive looks exactly like a coil pair twice as far apart. Two things break it,
and both are geometry rather than signal processing: **several separations** (the
$\theta$-dependence is not a function of $\sigma r^2$ alone once $h$, layering or
a target is present) and **several frequencies** (layering makes the response a
function of $\delta$ and the layer thicknesses separately). A single-frequency,
single-separation measurement of a homogeneous halfspace has a one-parameter
null space, and any inversion that reports a conductivity from such data is
reporting a choice along that null space.

## 8. Assumptions and regime of validity

1. **Quasi-static.** $\omega\varepsilon_0/\sigma\ll1$; measured margin $\ge10^4$ in
   the model here. Fails in ice, in very dry rock, and at radar frequencies.
2. **Non-magnetic ground.** $\mu=\mu_0$. Ferromagnetic minerals invalidate it and
   are the subject of [08-03-02](../03-magnetic-anomalies-and-modelling/02-koenigsberger-and-remanence.md);
   in FDEM practice the magnetic susceptibility adds an in-phase term that is
   easily mistaken for a conductor.
3. **Homogeneous halfspace, flat interface, dipole sources.** Every real system
   has finite coils, a finite height, topography and layering; a dipole model is
   the limiting case, and the error of the dipole approximation was measured in
   Section 4 ($0.57\%$ at $s=20\ \mathrm{m}$, $10\%$ at $a/s=0.2$).
4. **The interface conditions used are the exact ones** for the TE field; that
   part is not an approximation, and the image limit in Section 5.4 tests it.
5. **Linear response.** Implicit everywhere: the ground is Ohmic, and the
   response is independent of the transmitter current. Induced polarisation —
   where it is not — is a separate method, not a correction.
6. **Weak induction is *not* assumed in the forward solution** (the integral is
   exact) but **is** assumed in most interpretive shortcuts: any use of
   $\sigma_{\text{app}}$ carries the $1.5\theta$ bias of Section 7(c).
7. **No discussion of noise here.** The receiver's internal noise, coil
   misalignment and bucking residuals are treated as a synthetic noise figure in
   the demonstration (2 ppm); their propagation into a conductivity estimate is
   Section 9.

## 9. Detection limits and the shape of a usable band

Two features of the response define the usable window, and the demonstration
locates both for the reference model:

- the quadrature **peaks** at $\theta=0.761$ ($f\approx7.34\ \mathrm{kHz}$),
  with a value of $8.2\times10^{4}\ \mathrm{ppm}$;
- the quadrature **nulls** at $\theta=1.242$ ($f\approx19.5\ \mathrm{kHz}$);
  above the null the ground is a mirror and the response decreases while the
  in-phase part runs to $-1$ (in-phase $-1.0000$ at $\theta=12.57$ in the
  tabulated sweep).

The detection limit is where the quadrature drops to the noise floor. For a
resistive SYNTHETIC ground ($\sigma=0.005\ \mathrm{S\,m^{-1}}$) and a $2\ \mathrm{ppm}$
(1$\sigma$, per component) synthetic noise, the demonstration propagates the noise
into $\sigma_{\text{app}}$ through $\delta\sigma_{\text{app}} =
\sigma_{\text{app}}\times(\text{noise}/\lvert S_{\text{quad}}\rvert)$: the
relative error is $52\%$ at $1\ \mathrm{Hz}$, $17\%$ at $3\ \mathrm{Hz}$, $2.9\%$
at $10\ \mathrm{Hz}$ and $0.08\%$ at $300\ \mathrm{Hz}$. Meanwhile the LIN bias
grows the other way: $\sigma_{\text{app}}$ drifts from
$0.00499\ \mathrm{S\,m^{-1}}$ at $1\ \mathrm{Hz}$ to $0.00474\ \mathrm{S\,m^{-1}}$
at $300\ \mathrm{Hz}$ against a true $0.005$. **The noise falls with frequency and
the bias rises with frequency, so there is an optimum band and it depends on the
target conductivity.** Quoting "a detection limit" without the conductivity, the
geometry and an acceptable bias is not a statement about the method.

## 10. Python demonstration

`code/fdem_response_demo.py` computes everything above and prints labelled
results with units. It:

1. tabulates the skin depth and the displacement-current criterion over
   $100\ \mathrm{Hz}$–$100\ \mathrm{kHz}$;
2. computes the mutual inductance of two coplanar loops by the Neumann integral
   and compares it with the dipole limit and the $1/s^3$ law;
3. tabulates in-phase, quadrature and amplitude in ppm against frequency and
   $\theta$, and locates the quadrature peak and null;
4. prints the worked-example numbers of Sections 3.1 and 6;
5. checks the LIN asymptote and measures the $1.5\theta$ bias and the power laws;
6. verifies the response by adaptive quadrature, the height scaling, the image
   limit and the scale invariance;
7. reports the truncation self-consistency and propagates a synthetic noise floor
   into an apparent conductivity.

It is print-only, uses `np.random.default_rng(20261014)`, needs no network, and
finishes in about one second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/01-frequency-domain-em-exercises.md`](./exercises/01-frequency-domain-em-exercises.md)
and
[`exercises/01-frequency-domain-em-solutions.md`](./exercises/01-frequency-domain-em-solutions.md).

- **★** Compute $\delta$ and $\theta$ for $f=3\ \mathrm{kHz}$,
  $\sigma=0.1\ \mathrm{S\,m^{-1}}$, $r=25\ \mathrm{m}$; state whether LIN applies.
- **★★** Derive $M_{\text{dipole}}=-\mu_0\pi a^2b^2/(4s^3)$ from the static dipole
  field and check the sign physically.
- **★★** Suppose the bucking leaves a residual $20\ \mathrm{ppm}$ in-phase error.
  What does that imply for the smallest quadrature you can trust, and at what
  $\theta$ does it matter for the model of Section 6?
- **★★★** Prove the scale invariance of Section 7(d) by the substitution
  $\lambda=x/r$, and identify precisely which additional measurement breaks it for
  a two-layer ground.

## Mastery checkpoint

Without notes:

> A ground is a homogeneous halfspace of unknown conductivity. A coplanar coil
> pair with $r=30\ \mathrm{m}$ records $S=5.0\times10^{-4}+i\,2.0\times10^{-3}$ at
> $f=1\ \mathrm{kHz}$. **(a)** Compute $\theta$ assuming the LIN form applies and
> hence find $\sigma_{\text{app}}$. **(b)** State the sign of the LIN bias and
> whether the true conductivity is larger or smaller. **(c)** A colleague repeats
> the measurement with $r=60\ \mathrm{m}$ at the same frequency and finds the same
> number. What have they actually measured? **(d)** Name the smallest change to
> the survey that would break that ambiguity, and say what new quantity it
> constrains.

## Common pitfalls

1. **Forgetting the convention.** In-phase/quadrature, $e^{\pm i\omega t}$, and
   field versus emf are three independent sign choices. A number without them is
   not reproducible.
2. **Quoting one detection limit.** Detection depends on $\sigma$, $r$, $h$,
   frequency and the acceptable bias (Section 9).
3. **Treating the LIN form as exact.** Its relative error is about $1.5\theta$; at
   $\theta=0.3$ that is $45\%$, not a rounding error.
4. **Using the wrong asymptote.** "In-phase $\propto\omega^2$" is a statement
   about a compact target with one relaxation time. For a halfspace the measured
   exponent is $3/2$.
5. **Reading ppm as an absolute field.** The ppm ratio depends on the primary
   field, and therefore on the bucking, which is where most instrument errors
   live.
6. **Fitting conductivity at one separation.** That fits $\sigma r^2$ (Section
   7(d)); the number returned is one point on a null space.
7. **Assuming magnetic ground is a small correction.** In many terrains the
   susceptibility response is of the same order as the conductivity response, and
   it is in-phase.

## Related modules

- [08-05-02 Time-Domain EM (TDEM): Sounding, Transients and Decay Curves](02-time-domain-em.md)
  — the same diffusion physics measured after the transmitter switches off, where
  the $90^\circ$ null of the primary has already been solved once.
- [08-04-02 Magnetotellurics](../04-electromagnetic-induction/02-magnetotellurics.md)
  — the natural-source version of the impedance measurement, with the same
  skin-depth physics and the same dimensional scalings.
- [08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods](03-em-modelling.md)
  — how the integral above becomes a numerical solver for arbitrary geometry.
- [08-05-04 EM Inversion and Dimensionality](04-em-inversion.md) — what the null
  space of Section 7(d) looks like in an inversion.
- [08-05-05 Airborne EM for Conductivity Mapping](05-airborne-em.md) — the same
  response with $h$ of tens of metres, where the height–conductivity ambiguity
  replaces the separation–conductivity ambiguity.
- [02-07-06 EM Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
  — the diffusion equation used throughout.
