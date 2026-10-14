---
id: 20-06-01
title: "Particle Motion Analysis and Polarisation Attributes"
level: research
prereqs: ["20-01-01", "03-02-05"]
tags: [signal-processing, array-processing, polarisation, particle-motion, three-component, eigenvalue-analysis]
---

# Particle Motion Analysis and Polarisation Attributes

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** the three-component covariance matrix of a wave packet and
   **derive** its eigenvalues and eigenvectors.
2. **Define** rectilinearity, planarity, azimuth and incidence from the
   eigen-decomposition, and state the 180° ambiguity of a polarisation axis.
3. **Derive** the rectilinearity of an elliptical particle motion in closed form
   and check it against measurement.
4. **Estimate** the azimuth scatter as a function of signal-to-noise ratio and
   **verify** the estimate on an ensemble.
5. **Determine** the sense of particle motion (prograde or retrograde) from a
   signed cross-product.
6. **Explain** how a sensor orientation error maps into a bias in the measured
   azimuth, and **quantify** it.
7. **Decide** on a window length that does not mix two polarisations.

All models and data in this module are **SYNTHETIC**. The wave packets below are
constructed by the accompanying demonstration; no real event, station or
waveform is used and no number is quoted from a published measurement.

## Prerequisites

- [20-01-01 Signal Classification: Continuous/Discrete, Deterministic/Random](../01-signals-and-systems/01-signal-classification.md) —
  the deterministic packet used as the carrier here.
- [03-02-05 Linear Algebra with numpy.linalg](../../03-scientific-computing/02-numpy/05-linear-algebra-numpy.md) —
  the symmetric eigenproblem solved in Section 3.
- [06-01-01 Elastic Wave Propagation](../../06-seismology/01-elastic-wave-propagation/README.md) —
  the P, S, Rayleigh and Love motions that the polarisations describe.

## 1. Intuition: a wave leaves a shape behind

A three-component seismometer records the same ground motion projected onto
three orthogonal directions — usually north, east and up. A wave passing through
traces a curve in that three-dimensional space: a **hodogram**. A P arrival is a
nearly straight line along the ray direction; a surface Rayleigh wave is a
retrograde ellipse in the vertical plane containing the propagation direction; a
Love wave is a straight line across that plane. If the curve has a shape, the
shape is information: it tells you the direction of the ray, the phase of the
arrival, and whether the motion is a body or a surface wave — all from a single
station, with no array and no event location.

Making that information quantitative is a small exercise in linear algebra. The
tool is the **covariance matrix** of the three components over a time window. Its
eigenvectors are the principal axes of the hodogram; its eigenvalues measure how
much of the motion lies along each axis. Every "polarisation attribute" in the
literature is a function of those six numbers.

## 2. Precise definitions

### 2.1 The covariance matrix

Let $\mathbf{x}(t) = (x_1, x_2, x_3)^{T}$ be the three components over a window of
$N$ samples, after removing the window mean. The **covariance matrix** is

$$C_{ij} = \frac{1}{N-1}\sum_{n=1}^{N} x_i(t_n)\,x_j(t_n),$$

a symmetric $3\times3$ matrix with real eigenvalues $\lambda_1 \ge \lambda_2 \ge
\lambda_3 \ge 0$ (up to numerical noise) and orthonormal eigenvectors
$\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$.

### 2.2 The attributes

With the eigen-decomposition in hand, define

$$\text{rectilinearity } R = 1 - \frac{\lambda_2+\lambda_3}{2\lambda_1},
\qquad
\text{planarity } P = 1 - \frac{2\lambda_3}{\lambda_1+\lambda_2},$$

both in $[0,1]$ and both dimensionless. $R \to 1$ for a straight line,
$R \to 0$ for isotropic motion; $P \to 1$ for motion confined to a plane,
$P \to 0$ for isotropic motion. The **azimuth** and **incidence** are read from
the principal eigenvector $\mathbf{v} = (v_N, v_E, v_Z)$:

$$\phi = \operatorname{atan2}(v_E, v_N) \mod 180^\circ,
\qquad
\iota = \arccos|v_Z| .$$

**The azimuth of a linear polarisation is an axis, not a direction.** Both
$\mathbf{v}$ and $-\mathbf{v}$ are the same motion, so $\phi$ and $\phi+180^\circ$
are indistinguishable and the reportable quantity lies in $[0^\circ,180^\circ)$.
Confusing the axis with a direction is the commonest error in polarisation
analysis; it is why the demonstration wraps every azimuth to $[0^\circ,180^\circ)$
before computing an error.

## 3. Derivations

### 3.1 A linearly polarised wave has rank-one covariance

Let the packet be $\mathbf{x}(t) = \mathbf{u}\,w(t)$ with $\mathbf{u}$ a fixed
unit vector and $w(t)$ a scalar waveform of variance $\sigma_w^{2}$. Then

$$C_{ij} = \frac{1}{N-1}\sum_n u_i u_j w(t_n)^{2}
= u_i u_j \sigma_w^{2},$$

so $C = \sigma_w^{2}\,\mathbf{u}\mathbf{u}^{T}$: a rank-one matrix with the single
non-zero eigenvalue $\lambda_1 = \sigma_w^{2}$ and eigenvector
$\mathbf{u}$. The measured azimuth and incidence therefore *are* the ray
direction, exactly, with no residual. The demonstration's synthetic P packet at
azimuth $45^\circ$ and incidence $30^\circ$ from vertical, in direction
$\mathbf{u} = (\sin 30^\circ\cos 45^\circ, \sin 30^\circ\sin 45^\circ,
\cos 30^\circ) = (0.3536, 0.3536, 0.8660)$, gives eigenvalues
$4.2922\times10^{-2}$, $1.90\times10^{-18}$ and $-7.13\times10^{-18}$ — the last
two are zero to machine precision — with $R = 1.0000$, $P = 1.0000$, azimuth
$45.00^\circ$ and incidence $30.00^\circ$.

### 3.2 An ellipse: rectilinearity in closed form

Let the horizontal component be $h(t) = a\cos\omega t$ and the vertical be
$z(t) = b\sin\omega t$, a $90^\circ$ quadrature pair with axial ratio $b/a$. Over
many cycles $\langle\cos^{2}\rangle = \langle\sin^{2}\rangle = 1/2$ and
$\langle\cos\sin\rangle = 0$, so in the $(h,z)$ plane

$$C = \begin{pmatrix} a^{2}/2 & 0 \\ 0 & b^{2}/2 \end{pmatrix},
\qquad \lambda_1 = \frac{a^{2}}{2},\quad \lambda_2 = \frac{b^{2}}{2},
\quad \lambda_3 = 0 .$$

Therefore

$$\boxed{\;R = 1 - \frac{b^{2}}{2a^{2}},
\qquad P = 1 .\;}$$

The demonstration uses $a = 1$, $b = 0.70$: $R = 1 - 0.49/2 = 0.7550$, and the
measured value is $0.7550$. A **circular** motion ($b = a$) gives $R = 0.5$: even
a perfect, noise-free circle has a rectilinearity of only one half, because the
motion genuinely occupies two dimensions. For a circle the principal eigenvector
is arbitrary within the plane, and the azimuth is **undefined** — Section 5
measures that.

### 3.3 The sense of rotation

The signed quantity

$$S = \left\langle h\,\dot z - z\,\dot h \right\rangle$$

(the $z$-component of $\mathbf{r}\times\dot{\mathbf{r}}$ in the vertical plane) is
positive for one sense and negative for the other. For the packet above,
$S = +\omega ab/2$ with $z = +b\sin\omega t$ and $-\omega ab/2$ with
$z = -b\sin\omega t$: the demonstration computes $\pm 2.8880$. Surface Rayleigh
waves are **retrograde**, which corresponds to the negative sign in this
convention, and the sign flips with the vertical polarity — which is why a
reversed vertical channel turns prograde motion into retrograde and is a common
instrument fault.

### 3.4 Azimuth error versus SNR

Add noise of per-component standard deviation $\sigma_n$ to a rank-one packet of
amplitude $\sigma_w$. The perturbation of the principal eigenvector is a
first-order perturbation problem: the cross terms of the perturbed covariance are
of order $\sigma_w\sigma_n$ against a gap of $\sigma_w^{2}$, so

$$\delta\phi \sim \frac{\sigma_n}{\sigma_w}
= \frac{1}{\mathrm{SNR}} \quad\text{(radians, order of magnitude)} .$$

The demonstration measures exactly this, with the azimuth wrapped to
$[0^\circ,180^\circ)$ before the error is formed:

| SNR (amplitude) | linear packet az. s.d. | circular packet az. s.d. |
|---|---|---|
| 1 | $50.4^\circ$ | $53.0^\circ$ |
| 2 | $41.7^\circ$ | $57.0^\circ$ |
| 5 | $6.3^\circ$ | $53.6^\circ$ |
| 10 | $2.9^\circ$ | $50.7^\circ$ |
| 20 | $1.3^\circ$ | $48.5^\circ$ |

The linear case falls off as $1/\mathrm{SNR}$ (from $6.3^\circ$ to $1.3^\circ$ for
a factor of four in SNR), while the circular case stays near $50^\circ$ at every
SNR. The circular value is not noise: a standard deviation of about $52^\circ$ is
what a **uniform distribution on $[0^\circ,180^\circ)$** gives
($180^\circ/\sqrt{12} = 52.0^\circ$). The demonstration has recovered the
statement that a circular particle motion has no azimuth at all, at any
signal-to-noise ratio.

## 4. Worked example: Rayleigh and Love at the same station

| packet | eigenvalues | $R$ | $P$ | azimuth | incidence |
|---|---|---|---|---|---|
| P, rectilinear | $4.29\times10^{-2}$, $\sim0$, $\sim0$ | 1.000 | 1.000 | $45.00^\circ$ | $30.00^\circ$ |
| Rayleigh-type, $b/a=0.7$ | $4.29\times10^{-2}$, $2.10\times10^{-2}$, 0 | 0.755 | 1.000 | $0.00^\circ$ | $90.00^\circ$ |
| Love-type, pure transverse | $4.29\times10^{-2}$, $\sim0$, $\sim0$ | 1.000 | 1.000 | $90.00^\circ$ | $90.00^\circ$ |

Three lessons are visible in one table. Rayleigh motion is *planar* ($P = 1$,
since the ellipse lies in one plane) but not *rectilinear* ($R = 0.755$). Its
principal axis is horizontal, so the reported incidence is $90^\circ$ and is
meaningless as an incidence — a Rayleigh wave has no ray direction of the P/S
kind. Love motion is rectilinear and purely horizontal, so it reports $R = 1$ and
incidence $90^\circ$ just like Rayleigh, and the two are distinguished by the
azimuth relative to the propagation direction, not by $R$ alone. **No single
attribute identifies a phase; the attributes must be read together.**

## 5. Worked example: sensor orientation and window choice

**Orientation.** Rotating the two horizontal components by $\theta$ rotates the
measured polarisation by $-\theta$ in this convention (the sensor frame rotates
one way, the reported azimuth the other). The demonstration rotates the data and
measures:

| sensor rotation | reported azimuth | shift |
|---|---|---|
| $0^\circ$ | $45.00^\circ$ | $0.00^\circ$ |
| $+10^\circ$ | $35.00^\circ$ | $-10.00^\circ$ |
| $+20^\circ$ | $25.00^\circ$ | $-20.00^\circ$ |
| $-15^\circ$ | $60.00^\circ$ | $+15.00^\circ$ |

The shift is *exactly* the rotation, so an unknown sensor orientation is an
unknown additive offset in every azimuth, and no amount of data can remove it.
This is why a three-component station is useless for absolute azimuth back-azimuth
work until its orientation has been determined independently.

**Window choice.** A window containing two phases returns an average of two
polarisations, which describes neither. With a P packet at azimuth $20^\circ$ and
a later S packet at azimuth $110^\circ$:

| window | $R$ | azimuth | incidence |
|---|---|---|---|
| whole 5.12 s record | 0.8285 | $29.43^\circ$ | $29.92^\circ$ |
| P window only | 0.9920 | $20.47^\circ$ | $29.98^\circ$ |
| S window only | 0.9313 | $109.13^\circ$ | $78.55^\circ$ |

The whole-record estimate reports $29.4^\circ$ — a number that corresponds to no
physical direction, sitting between the two arrivals — and its rectilinearity is
depressed to $0.83$ by the mixing. Separating the windows recovers both
arrivals. **Rectilinearity is the diagnostic for a mixed window**: a value below
about $0.9$ on a body-wave arrival usually means the window is too long, not that
the medium is anisotropic.

## 6. Assumptions and regime of validity

1. **Stationarity within the window.** The covariance is a single average over
   the window, so the polarisation must be constant there. Frequency-dependent
   polarisation and dispersive surface waves violate this; the remedy is
   time-frequency polarisation, the subject of
   [02-05 Time-Frequency Analysis](../02-fourier-and-spectral-analysis/05-time-frequency.md).
2. **Additive, uncorrelated noise of comparable level on all three components.**
   A single noisy channel biases the principal direction toward that channel; a
   covariance-weighted or channel-normalised analysis is then required.
3. **No instrument-response differences between components.** A phase difference
   between channels turns a linearly polarised wave into an apparent ellipse and
   lowers $R$ — a real and easily missed processing error.
4. **The window mean has been removed.** A DC offset puts the motion off the
   origin in the hodogram and corrupts the ellipse.
5. **A straight line is a line, not a direction.** Every azimuth from a
   linear-polarisation analysis is modulo $180^\circ$; the sign requires
   additional information (first motion, or the sign of the vertical component
   for an upgoing P).

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| components | $x_i$ | m or m s$^{-1}$ | ground motion or velocity |
| covariance | $C_{ij}$ | (component unit)$^{2}$ | product of two components |
| eigenvalues | $\lambda_k$ | (component unit)$^{2}$ | same as the variance |
| rectilinearity, planarity | $R$, $P$ | dimensionless | ratios of eigenvalues |
| azimuth, incidence | $\phi$, $\iota$ | degrees | from unit eigenvector |
| sense | $S$ | (unit)$^{2}\,\mathrm{s^{-1}}$ | $h\dot z$ has s$^{-1}$ |

$R$ and $P$ are dimensionless because they are ratios; a computed $R$ outside
$[0,1]$ for positive eigenvalues means the eigenvalues were not sorted
descending before the formula was applied.

## 8. Python demonstration

[`code/particle_motion_demo.py`](./code/particle_motion_demo.py) builds the
packets and prints every number above:

1. the rank-one covariance of a rectilinear P;
2. the closed-form rectilinearity of an ellipse, with the prograde/retrograde
   sense;
3. azimuth scatter versus SNR for linear and circular motion;
4. the effect of a sensor orientation error;
5. the effect of a window that mixes two phases.

```bash
cd 20-signal-processing/06-polarisation-and-array-processing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python particle_motion_demo.py
```

## 9. Exercises

[`exercises/01-particle-motion-exercises.md`](./exercises/01-particle-motion-exercises.md)
and
[`exercises/01-particle-motion-solutions.md`](./exercises/01-particle-motion-solutions.md).
The ★★★ problem asks you to design a polarisation-based phase detector and to
state its failure modes.

## 10. Mastery checkpoint

1. A packet's covariance has eigenvalues $9.0$, $1.0$ and $0.0$. Compute $R$ and
   $P$ and name the likely motion.
2. A rectilinear arrival is recorded with SNR 4. Estimate the azimuth standard
   deviation in degrees, and state the assumption behind the estimate.
3. The reported azimuth changes by $12^\circ$ when the horizontal channels are
   swapped and one is negated. What physical fault does that describe?
4. A window returns $R = 0.72$. Give the two most likely explanations and a
   measurement that separates them.

## 11. Common pitfalls

1. **Treating the azimuth as a direction.** It is an axis, defined modulo
   $180^\circ$.
2. **Using one long window for two arrivals.** The result is an average that
   describes neither; check $R$.
3. **Reading incidence from a Rayleigh wave.** The ellipse's principal axis is
   horizontal, so the returned incidence is $90^\circ$ by construction.
4. **Ignoring sensor orientation.** An unknown rotation appears as a constant
   azimuth offset that no data can fix.
5. **Calling a low $R$ "anisotropy".** Mis-alignment, instrument phase
   differences and mixed windows all lower $R$ before anisotropy does.

## 12. Related lessons

- [02 Beamforming, Slowness Estimation and f-k Analysis](02-beamforming.md) —
  what an array adds to a single-station polarisation.
- [03 Seismic Array Design and Resolution](03-array-design.md) — the geometry
  that decides how well a direction can be measured.
- [20-02-05 Time-Frequency Analysis: STFT, Wavelets, Spectrograms](../02-fourier-and-spectral-analysis/05-time-frequency.md) —
  the remedy when the polarisation changes within the window.
- [06-08-04 Anisotropy from Receiver Functions](../../06-seismology/08-receiver-functions-and-crustal-structure/04-anisotropy-receiver-functions.md) —
  the transverse-energy problem this lesson's diagnostics help to settle.

## 13. Further reading

Titles are given so the works can be located; this repository does not host or
reproduce copyrighted text.

- **Jurkevics, "Polarization analysis of three-component array data", *Bulletin
  of the Seismological Society of America*, 1988.** Level: research. The
  covariance-eigenvalue attributes used here.
- **Samson, "Matrix and Stokes vector representations of detectors for polarized
  waveforms", *Geophysical Journal International*, 1977.** Level: research. The
  mathematical framework for polarisation, including the quadratic form.
- **Aki & Richards, *Quantitative Seismology*, University Science Books.**
  Level: graduate. The body- and surface-wave particle motions being identified.
- **Havskov & Ottemöller, *Routine Data Processing in Earthquake Seismology*,
  Springer, 2010.** Level: applied. Orientation determination and rotation of
  three-component data.

## 14. Self-assessment checklist

- [ ] I can build a three-component covariance matrix and eigendecompose it.
- [ ] I can define and compute $R$, $P$, azimuth and incidence.
- [ ] I can derive the rectilinearity of an ellipse.
- [ ] I can state the $180^\circ$ ambiguity without being prompted.
- [ ] I can estimate an azimuth error from an SNR.
- [ ] I can recognise a mixed window from its attributes.
