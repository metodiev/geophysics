---
id: 13-03-01
title: "Plate Kinematic Models and Euler Pole Inversion"
level: doctoral
prereqs: ["04-02-04", "13-01-04", "07-04-05"]
tags: [geodynamics, tectonophysics, plate-kinematics, euler-pole, inverse-problems, gnss]
---

# Plate Kinematic Models and Euler Pole Inversion

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the surface velocity field of a rigid plate from an Euler vector,
   $v = \omega \times r$, and **state** the units in which it is evaluated.
2. **Construct** the design matrix for the pole inversion from horizontal
   velocities and **explain** why the inverse problem is linear in $\omega$ but
   non-linear in $(\text{lat}, \text{lon}, \omega)$.
3. **Show**, by singular-value decomposition, that one site cannot determine a
   pole, and **identify** the null-space direction as the site radius.
4. **Quantify** how network aperture, not station count, controls the recovered
   pole, and **predict** the $1/L$ scaling of the error.
5. **Compute** a least-squares pole covariance from residual variance and
   **judge** whether a quoted pole error is consistent with the residuals.
6. **Distinguish** instantaneous from finite rotations, **verify** circuit
   closure, and **explain** why Euler vectors cannot be added for long intervals.
7. **State** the assumptions under which a single Euler vector describes a
   plate's motion, and the observations that violate them.

## Prerequisites

- [04-02-04 Plate Motion Frames, Euler Poles and Global Models](../../04-earth-science-geology/02-plate-tectonics/04-plate-motion-frames.md) —
  the qualitative version of Euler's theorem and the frame problem.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](../01-geodynamic-principles/04-forces-and-stresses.md) —
  what the kinematics is the surface expression of.
- [07-04-05 ITRF and Plate Models](../../07-gravity-geodesy/04-geodesy-reference-frames/05-itrf-and-plate-models.md) —
  the reference frames in which velocities are actually expressed.

Throughout this lesson every model and every number is **SYNTHETIC**. All
models and data in this module are SYNTHETIC. The only exact constants used are
the mean Earth radius $R = 6371\ \mathrm{km}$ and the conversion
$1\ \mathrm{km\,Myr^{-1}} = 1\ \mathrm{mm\,yr^{-1}}$.

## 1. Why a rigid rotation, and why it is not a simplification

Euler's theorem says that any rigid body displacement that keeps one point
fixed is a rotation about an axis. For a plate moving on a sphere, the axis
through the centre of the Earth pierces the surface at two points, the **Euler
poles**, and the motion is a rotation about that axis at an angular speed
$\omega$. The instantaneous velocity of a surface point at position vector
$r$ is

$$
\boxed{\;v = \omega \times r\;}
$$

with $r$ in kilometres and $\omega$ in radians per unit time, giving $v$ in
kilometres per unit time.

Three facts make this useful rather than decorative.

- A rotation about a pole has **three** degrees of freedom: two for the pole
  direction, one for the rate. A velocity field, which naively looks like it
  has hundreds of degrees of freedom, therefore has only three if the plate is
  rigid. That collapse is what makes the inverse problem solvable at all.
- The velocity varies **linearly** in $\omega$ for fixed $r$. That is the whole
  reason the pole inversion is a linear least-squares problem; the non-linearity
  appears only when we re-parameterise $\omega$ by latitude, longitude and rate.
- The velocity is **perpendicular** to both $\omega$ and $r$, so it lies in the
  local horizontal plane. A vertical (radial) velocity is not predicted by
  rigid-body rotation and is therefore a direct measure of non-rigidity or of
  an error.

## 2. Averaging and inversion: setting up the linear problem

Write the Earth-centred Cartesian frame with $x$ towards $(0^\circ, 0^\circ)$,
$y$ towards $(0^\circ, 90^\circ)$ and $z$ towards the north pole. A site at
latitude $\varphi$ and longitude $\lambda$ has unit vector

$$
n = \begin{pmatrix} \cos\varphi\cos\lambda \\ \cos\varphi\sin\lambda \\
\sin\varphi \end{pmatrix}, \qquad r = R\,n .
$$

Because $\omega \times (Rn) = R\,(\omega \times n)$ and
$\omega \times n = -\,n \times \omega = -[n]_\times \omega$, where

$$
[n]_\times = \begin{pmatrix} 0 & -n_z & n_y \\ n_z & 0 & -n_x \\
-n_y & n_x & 0 \end{pmatrix},
$$

each site contributes three linear equations

$$
v_i = A_i\,\omega, \qquad A_i = -R\,[n_i]_\times .
$$

Stacking $N$ sites gives $A$ of size $3N \times 3$ and the least-squares
solution

$$
\hat\omega = (A^{\mathsf T} A)^{-1} A^{\mathsf T} b, \qquad
\mathrm{Cov}(\hat\omega) = \sigma^2 (A^{\mathsf T} A)^{-1},
$$

where $\sigma^2$ is estimated from the residual sum of squares divided by
$3N-3$ degrees of freedom. Writing the problem this way rather than directly
for $(\text{lat}, \text{lon}, \omega)$ matters: the least-squares problem is
exactly linear, so noise propagates by a known rule, and only the final
conversion to geographic coordinates is non-linear.

### 2.1 The pole as a geographic object

Given $\hat\omega$, the recovered parameters are

$$
|\omega| = \lVert \hat\omega \rVert, \quad
\varphi_p = \arcsin\!\left(\hat\omega_z / \lVert \hat\omega\rVert\right), \quad
\lambda_p = \operatorname{atan2}\!\left(\hat\omega_y, \hat\omega_x\right).
$$

The map $\hat\omega \mapsto (\varphi_p, \lambda_p, |\omega|)$ is non-linear, so
the covariance of the geographic pole is obtained by linearising it:
$\mathrm{Cov}_{\text{geo}} = J\,\mathrm{Cov}(\hat\omega)\,J^{\mathsf T}$ with
$J = \partial(\varphi_p, \lambda_p, |\omega|)/\partial \omega$. The
demonstration computes $J$ numerically, because the longitude uncertainty
diverges as the pole approaches the equator ($\omega_z \to 0$) and an analytic
form is easy to get wrong.

### 2.2 Velocity units that make the arithmetic trivial

Distances are kilometres, rates are Myr, so $\omega$ is in
$\mathrm{rad\,Myr^{-1}}$ and $v$ in $\mathrm{km\,Myr^{-1}}$. Then

$$
1\ \mathrm{km\,Myr^{-1}} = \frac{10^{6}\ \mathrm{mm}}{10^{6}\ \mathrm{yr}}
= 1\ \mathrm{mm\,yr^{-1}} .
$$

The numerical value of a velocity is therefore the same in both unit systems,
which is why plate-motion papers mix them freely. The demonstration prints both
labels to keep the identity visible.

## 3. Every number in this lesson

All results below come from `code/plate_kinematics_models_demo.py`, which builds
a SYNTHETIC plate with Euler pole at $\varphi_p = +58.0^\circ$,
$\lambda_p = -118.0^\circ$ and $\omega = 0.72\ \mathrm{deg\,Myr^{-1}}$, that is
$|\omega| = 0.012566\ \mathrm{rad\,Myr^{-1}}$. The Euler vector is

$$
\omega = \begin{pmatrix} -0.00312629 \\ -0.00587969 \\ 0.01065689
\end{pmatrix} \mathrm{rad\,Myr^{-1}} .
$$

### 3.1 A worked velocity

Take the demonstration's third site at $\varphi = 61.045^\circ$,
$\lambda = 16.231^\circ$.

1. $n = (0.46469,\ 0.13532,\ 0.87508)$ and $r = 6371\,n =
   (2960.4,\ 862.1,\ 5575.1)\ \mathrm{km}$.
2. $\omega \times r$ component by component:
   $v_x = (-0.00587969)(5575.1) - (0.01065689)(862.1) = -32.778 - 9.187
   = -41.965$; $v_y = (0.01065689)(2960.4) - (-0.00312629)(5575.1)
   = 31.549 + 17.431 = 48.980$; $v_z = (-0.00312629)(862.1) -
   (-0.00587969)(2960.4) = -2.695 + 17.406 = 14.711$, in
   $\mathrm{km\,Myr^{-1}}$.
3. Resolve onto the local east and north unit vectors,
   $\hat e = (-\sin\lambda, \cos\lambda, 0) = (-0.27961, 0.96013, 0)$ and
   $\hat n = (-\sin\varphi\cos\lambda, -\sin\varphi\sin\lambda, \cos\varphi)
   = (-0.84020, -0.24469, 0.48399)$:
   $v_{\text{east}} = 58.76\ \mathrm{mm\,yr^{-1}}$,
   $v_{\text{north}} = 30.40\ \mathrm{mm\,yr^{-1}}$,
   $|v| = 66.16\ \mathrm{mm\,yr^{-1}}$.

That number agrees with the demonstration to the printed digits; the point of
doing it by hand once is that the units and the sign conventions are checked.

### 3.2 Recovery from a noise-free global network

Forty sites spread near-uniformly over the sphere give $120$ equations for
$3$ unknowns. The recovered pole is

$$
\varphi_p = +58.0000^\circ, \quad \lambda_p = -118.0000^\circ, \quad
\omega = 0.720000\ \mathrm{deg\,Myr^{-1}},
$$

with pole error $6\times10^{-14}$ degrees and residual rms
$4.3\times10^{-14}\ \mathrm{km\,Myr^{-1}}$. That is machine precision: the
forward problem is linear and the data are exact, so the inversion is exact.
Anything larger would be a bug, not physics — which is what makes this
noise-free case a useful unit test before any real data are inverted.

## 4. What one site cannot do

For a single site, $A = -R[n]_\times$ has rank 2. The singular values of $A$
are, in the demonstration, $(6371.0,\ 6371.0,\ 5.4\times10^{-14})$ — the third
is numerical zero, and its right singular vector is the site's own radius
$n$ to $|n \cdot \text{null}| = 1.000000$.

The interpretation is exact and worth stating slowly: adding any multiple of $n$
to $\hat\omega$ changes no predicted velocity, because
$n \times n = 0$. The pole is therefore not a point but a **one-parameter
family**: the component of $\omega$ along $n$ is invisible. Geometrically, the
family is the curve of Euler vectors whose projection onto the site radius
matches the observation. Two sites are still not enough in general — the
null space has dimension $3 - \text{rank}(A)$, and rank reaches 3 as soon as
the sites are not collinear with the origin in a degenerate way — but with
three well-spread sites the problem becomes solvable and *horribly*
ill-conditioned. That distinction, solvable versus well determined, is the
subject of the next section.

## 5. Coverage, not count: the aperture argument

Consider $N$ sites confined to a cap of angular radius $\Theta$ (a linear
aperture $L \approx R\Theta$). The velocity difference between two sites in the
cap is

$$
\Delta v \approx |\omega|\,L ,
$$

while each velocity carries noise $\sigma$. The information about $\omega$ grows
with $\Delta v$ while the noise does not, so the relative error in the recovered
rate must scale as

$$
\frac{\delta\omega}{|\omega|} \sim \frac{\sigma}{|\omega|L} .
$$

The demonstration tests this with a fixed $1\ \mathrm{mm\,yr^{-1}}$ noise per
component, 200 realisations per network, and reports rms errors in the pole:

| network | sites | $\operatorname{cond}(A)$ | rms pole-lat error | rms pole-lon error | rms $\omega$ error | mean formal $\sigma$(lat) |
|---|---|---|---|---|---|---|
| global | 40 | $1.0\times10^{0}$ | $0.136^\circ$ | $0.246^\circ$ | $0.0016\ \mathrm{deg\,Myr^{-1}}$ | $0.137^\circ$ |
| one $4^\circ$ cap | 15 | $2.25\times10^{1}$ | $3.599^\circ$ | $4.250^\circ$ | $0.0064\ \mathrm{deg\,Myr^{-1}}$ | $3.475^\circ$ |
| two caps $70^\circ$ apart | 16 | $1.45\times10^{0}$ | $0.218^\circ$ | $0.454^\circ$ | $0.0027\ \mathrm{deg\,Myr^{-1}}$ | $0.235^\circ$ |

Three conclusions, each with a number attached:

1. **A cluster is not a network.** Fifteen sites inside a $\sim 445\ \mathrm{km}$
   cap give a pole good to only $\sim 3.6^\circ$; sixteen sites split between two
   caps give $0.22^\circ$, better by a factor $16$, with essentially the same
   number of stations.
2. **Condition number is the warning light.** It rises from $1$ (global) to
   $22.5$ (one cluster) even though the residual rms stays at the noise level in
   both cases. A good fit is not a determined model.
3. **The aperture scaling is measurable.** On a square network with 20 sites and
   apertures $20$ to $320\ \mathrm{km}$, the rms error in the largest principal
   strain rate falls $19.30 \to 10.50 \to 5.04 \to 2.54 \to 1.15$ (in
   $10^{-9}\ \mathrm{yr^{-1}}$). Each doubling of aperture halves the error, as
   $\delta\omega \propto 1/L$ predicts.

The formal uncertainty tracks the realised error: for the three networks the
ratios (rms realised error)/(mean formal $\sigma$) are $1.15$, $1.01$ and
$1.09$. That agreement is the check that the covariance formula is being applied
consistently with the noise model; an analyst who quotes errors a factor of ten
below the realised scatter has made an arithmetic or a weighting error.

## 6. Finite rotations are not vectors

For a finite rotation by angle $\theta$ about a unit axis $\hat k$, the
rotation matrix is Rodrigues' formula,

$$
\mathcal R(\hat k, \theta) = \mathcal I\cos\theta
+ \sin\theta\,[\hat k]_\times + (1-\cos\theta)\,\hat k\hat k^{\mathsf T},
$$

and a sequence of plate motions is a product of such matrices. Three rotation
matrices about three plates must multiply to the identity around a closed
circuit:

$$
\mathcal R_{AB}\,\mathcal R_{BC}\,\mathcal R_{CA} = \mathcal I .
$$

The demonstration builds two SYNTHETIC rotations, $\mathcal R_{AB}$ about
$(25^\circ, -10^\circ)$ at $0.551\ \mathrm{deg\,Myr^{-1}}$ and
$\mathcal R_{BC}$ about $(-55^\circ, 130^\circ)$ at
$0.441\ \mathrm{deg\,Myr^{-1}}$, and reports:

| duration | closure $\lVert\mathcal R_{AB}\mathcal R_{BC}\mathcal R_{CA} - \mathcal I\rVert$ | pole separation from the vector sum |
|---|---|---|
| $1\ \mathrm{Myr}$ | $2.2\times10^{-16}$ | $0.2198^\circ$ |
| $5\ \mathrm{Myr}$ | $2.0\times10^{-18}$ | $1.0990^\circ$ |
| $10\ \mathrm{Myr}$ | $2.5\times10^{-16}$ | $2.1982^\circ$ |
| $25\ \mathrm{Myr}$ | $1.9\times10^{-16}$ | $5.4974^\circ$ |

Two different statements live in those columns.

- **Closure is machine-exact.** Composing rotation matrices is exact algebra; no
  approximation enters. Any closure misfit larger than machine precision is an
  error in the reconstruction, not a physical effect.
- **Vector addition is wrong, and increasingly so.** The composite pole lies
  $0.22^\circ$ from $\omega_A + \omega_B$ at $1\ \mathrm{Myr}$ but $5.50^\circ$
  away at $25\ \mathrm{Myr}$. Each doubling of duration multiplies the
  separation by about four, i.e. it grows as $\theta^2$. Adding Euler vectors
  is a small-angle approximation, valid for the instantaneous rate and
  progressively worse for reconstructions over tens of millions of years.

A third check makes the same point at the level of a single site. A point on
the equator of the rotation moves at $|v| = R|\omega| = 80.06\
\mathrm{mm\,yr^{-1}}$. Its path is a circular arc; the straight-line
approximation is the tangent. The difference between the arc and the chord is
$R(\theta - 2\sin(\theta/2))$, which measures

$$
5.3\times10^{-7}\ \mathrm{mm} \ (1000\ \mathrm{yr}),\quad
5.3\times10^{-4}\ \mathrm{mm} \ (10^4\ \mathrm{yr}),\quad
5.3\times10^{-1}\ \mathrm{mm} \ (10^5\ \mathrm{yr}),\quad
5.3\times10^{2}\ \mathrm{mm} \ (1\ \mathrm{Myr}).
$$

Each factor of ten in time multiplies the gap by a thousand: the error scales
as $\theta^3$, because a chord differs from an arc only at second order in the
angle and the angle is itself first order. Negligible for a decade of
observations, decisive for a $50\ \mathrm{Myr}$ reconstruction.

## 7. Assumptions and regime of validity

1. **Rigidity.** The plate does not deform internally over the interval. This
   is the assumption that reduces hundreds of unknowns to three, and it is the
   one that fails first: intraplate strain rates of a few
   $10^{-9}\ \mathrm{yr^{-1}}$ accumulate to metres over $10^6\ \mathrm{yr}$.
2. **A single reference frame.** Velocities must be expressed in a frame that is
   itself rigid and constant. A frame defined by a subset of the same stations
   introduces a correlation between the frame parameters and the pole (see
   [07-04-05](../../07-gravity-geodesy/04-geodesy-reference-frames/05-itrf-and-plate-models.md)).
3. **Instantaneous versus finite.** The linearised $v = \omega \times r$ is
   exact for the instantaneous rate. For a finite interval, integrate the
   rotation; vector addition of $\omega$ is a small-angle approximation whose
   error scales as $\theta^2$ (measured above).
4. **Small network linearisation.** Treating the pole as a local linear velocity
   gradient is adequate only when $L \ll R$. At $445\ \mathrm{km}$ aperture
   ($\theta = 4^\circ$) the curvature of the sphere is negligible; the
   demonstration shows that the error there is dominated by conditioning, not by
   geometry.
5. **Horizontal-only data.** Vertical velocities are not inverted. Using them
   would absorb non-rigid processes (postglacial rebound, volcanic inflation)
   into the pole.
6. **Gaussian, isotropic noise.** The covariance formula assumes it. Real GNSS
   velocity fields have spatially correlated noise from orbit and atmosphere
   errors, which inflates the formal errors of a small network far above the
   white-noise value.

## 8. Worked example — how much does aperture buy?

A $\mathrm{SYNTHETIC}$ campaign has 10 sites at $1\ \mathrm{mm\,yr^{-1}}$ noise
on a $60\ \mathrm{km}$ baseline. From the scaling derived in Section 5, the
signal is $|\omega|L$. Taking $|\omega| = 0.0126\ \mathrm{rad\,Myr^{-1}}$ and
$L = 60\ \mathrm{km}$ gives $\Delta v = 0.75\ \mathrm{mm\,yr^{-1}}$ — below the
noise. The recovered rate would be dominated by noise, with a formal uncertainty
comparable to the signal itself.

Extending the network to $400\ \mathrm{km}$ raises $\Delta v$ to
$5.03\ \mathrm{mm\,yr^{-1}}$, five times the noise, so the rate is recovered to
about $20\%$ and the pole direction to a few degrees. The demonstration's
measured errors bear this out: the pole error falls from
$3.60^\circ$ at $445\ \mathrm{km}$ aperture when the sites are clustered, to
$0.22^\circ$ when the same number of sites is spread over two caps $70^\circ$
apart.

**Conclusion.** Adding stations inside an existing footprint does not remove
this limit; only extending the footprint does. This is why plate-motion solutions
use global or continental-scale networks and why regional studies carefully
separate the pole they can determine from the one they must assume.

## 9. Python demonstration

`code/plate_kinematics_models_demo.py` prints labelled results with units and
exits 0. It:

1. builds the SYNTHETIC velocity field from the Euler vector and prints
   $v_{\text{east}}$, $v_{\text{ north}}$ and $|v|$ for the first five sites;
2. inverts the global network and reports the recovered pole to machine
   precision;
3. performs the singular-value decomposition for a single site and shows the
   null vector equals the site radius;
4. compares global, single-cap and two-cap networks at
   $1\ \mathrm{mm\,yr^{-1}}$ noise over 200 realisations, with condition numbers;
5. compares the formal covariance with the realised rms error for each network;
6. verifies the closure of a three-plate circuit and measures the growth of the
   error in adding Euler vectors;
7. computes the arc-versus-chord gap and shows its $\theta^3$ scaling.

## 10. Exercises

Companion sets, with full worked solutions:

- [`exercises/01-plate-kinematics-models-exercises.md`](exercises/01-plate-kinematics-models-exercises.md)
  and the [solutions](exercises/01-plate-kinematics-models-solutions.md).
- Keyed to the tiers ★ (foundational), ★★ (applied), ★★★ (research-oriented).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC network of 12 sites occupies a single $3^\circ$ cap. The
> velocities are fitted by a rotation and the residual rms equals the assumed
> $1\ \mathrm{mm\,yr^{-1}}$ noise. **(a)** Using the aperture argument, estimate
> the uncertainty in the angular rate for this network if the true rate is
> $0.7\ \mathrm{deg\,Myr^{-1}}$ and the cap is about $330\ \mathrm{km}$ across.
> **(b)** The software reports a formal pole uncertainty of $0.05^\circ$. Is it
> believable? Justify your answer with the measured numbers in Section 5.
> **(c)** State two changes to the experiment that would reduce the pole
> uncertainty by a factor of five, and say which one the measured scaling
> supports. **(d)** Explain in one sentence why a good fit to the velocities does
> not imply a well-determined pole.

## Common pitfalls

1. **Reporting a pole from a local network without its uncertainty.** The
   demonstration's one-cap network fits its data as well as the global network
   and is wrong by degrees.
2. **Adding Euler vectors for a long reconstruction.** The error grows as
   $\theta^2$; at $25\ \mathrm{Myr}$ the pole moves by $5.5^\circ$ in the
   demonstration's own geometry.
3. **Quoting a formal error smaller than the residual scatter.** Check that the
   formal $\sigma$ reproduces the realised error; the demonstration gets ratios
   of $1.01$–$1.15$ from a correct covariance.
4. **Mixing $\mathrm{s\,km^{-1}}$ and $\mathrm{s\,m^{-1}}$** or
   $\mathrm{km\,Myr^{-1}}$ and $\mathrm{mm\,yr^{-1}}$ without noticing that the
   latter pair is numerically identical.
5. **Ignoring vertical velocities.** Leaving them out is correct for a rigid
   plate; including them silently imports non-rigid signals.
6. **Treating the pole as a physical object.** It is a parameter of a model of
   rigid motion; if the plate is not rigid, the pole is a weighted average of a
   time-varying field.

## Related modules

- [13-03-02 Rifting, Break-Up and Passive Margin Formation](02-rift-and-breakup.md) —
  what happens when the rigidity assumption fails inside a continent.
- [13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull](../02-mantle-convection/04-subduction-dynamics.md) —
  the driving-side view of the velocities inverted here.
- [13-01-04 Forces and Intraplate Stress](../01-geodynamic-principles/04-forces-and-stresses.md).
- [07-04 Geodesy Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md) —
  where the velocities come from.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  the general theory of the linear system solved here.
- [13-04-01 Crustal Deformation from GNSS and Strain Rates](../04-tectonophysics-deformation/01-crustal-deformation-gps.md) —
  the same data inverted for internal deformation instead of rigid motion.
