---
id: 13-04-01
title: "Crustal Deformation from GNSS and Strain Rates"
level: graduate
prereqs: ["13-03-01", "02-04-02", "07-04-03"]
tags: [geodynamics, tectonophysics, gnss, strain-rate, deformation, geodesy]
---

# Crustal Deformation from GNSS and Strain Rates

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the velocity-gradient tensor from a set of station velocities, and
   **decompose** it into a symmetric strain-rate tensor and an antisymmetric
   rotation.
2. **Compute** the principal strain rates, their azimuths and the dilatation
   rate, and **explain** why their uncertainties are not the component
   uncertainties.
3. **Show** that strain rate is invariant to a rigid rotation of the reference
   frame while the estimated rotation rate is not, and **state** the consequence
   for what GNSS can and cannot measure.
4. **Predict and measure** how network aperture, not station count, controls the
   strain-rate uncertainty, including the $1/L$ scaling.
5. **Detect** a blunder by residual inspection and **quantify** the damage a
   single bad station does to the recovered tensor.
6. **State** the assumptions (homogeneous strain, small strain, rigid reference
   frame) and **identify** the observations that violate each.

## Prerequisites

- [13-03-01 Plate Kinematic Models and Euler Pole Inversion](../03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  the rigid-motion special case of everything here.
- [02-04-02 Strain](../../02-physics/04-elasticity-and-continuum-mechanics/02-strain.md) —
  the strain tensor, principal values and invariants.
- [07-04-03 GNSS Positioning](../../07-gravity-geodesy/04-geodesy-reference-frames/03-gnss-positioning.md) —
  how the velocities are measured and what their uncertainties mean.

All models and data in this module are **SYNTHETIC**. The network, velocities,
strain rate and noise below are chosen teaching values; no real GNSS site or
published strain-rate map is used. The only exact conversion used is the unit
identity $1\ \mathrm{nanostrain\,yr^{-1}} = 10^{-9}\ \mathrm{yr^{-1}}$.

## 1. From velocities to a tensor

A GNSS station gives two horizontal velocity components. If the deformation
field is approximately **homogeneous** over the network, the velocity varies
linearly with position:

$$
v_i = v_0 + L\,(x_i - x_0),
\qquad
L = \begin{pmatrix}
\partial v_E/\partial x_E & \partial v_E/\partial x_N \\
\partial v_N/\partial x_E & \partial v_N/\partial x_N
\end{pmatrix},
$$

where the derivatives are with respect to local east and north coordinates. $L$
is the **velocity-gradient tensor** and it has four independent components, so
four unknowns plus the two components of the reference velocity $v_0$ make six —
exactly the number of parameters of a two-dimensional affine velocity field.

The decomposition is the whole point of the exercise:

$$
L = \underbrace{\tfrac12\left(L + L^{\mathsf T}\right)}_{\displaystyle E}
+ \underbrace{\tfrac12\left(L - L^{\mathsf T}\right)}_{\displaystyle W},
\qquad
W = \begin{pmatrix} 0 & -w \\ w & 0\end{pmatrix}.
$$

- $E$, the symmetric part, is the **strain-rate tensor**. Its eigenvalues are the
  principal strain rates $e_1 \ge e_2$ with $\dot\varepsilon_1 + \dot\varepsilon_2
  = \mathrm{tr}\,E = \nabla\!\cdot\!v$, the **dilatation rate** (areal strain
  rate in 2-D).
- $W$, the antisymmetric part, is the **rotation rate** $w$ about the vertical
  axis, positive counter-clockwise.

Since both $E$ and $W$ are derived from the same four numbers, and the data
determine only four numbers, everything an analyst reports is some non-linear
function of those four. A useful consequence is that reporting six numbers
(two principal rates, an azimuth, a rotation rate, a dilatation and a residual)
from a four-parameter fit invites inconsistency; the safest practice is to
report $L$ and the covariance and derive the rest consistently.

### 1.1 Units

Velocities are in $\mathrm{mm\,yr^{-1}}$, distances in kilometres, so strain
rates come out in $\mathrm{mm\,yr^{-1}\,km^{-1}} = 10^{-6}\ \mathrm{yr^{-1}}$ —
an inconvenient unit. The field convention is **nanostrain per year**,
$1\ \mathrm{nstrain\,yr^{-1}} = 10^{-9}\ \mathrm{yr^{-1}}$. The conversion
chain is worth memorising:

$$
1\ \mathrm{mm\,yr^{-1}\,km^{-1}} = \frac{10^{-3}\ \mathrm{m}}{10^{3}\
\mathrm{m}} \mathrm{yr^{-1}}
= 10^{-6}\ \mathrm{yr^{-1}} = 10^{3}\ \mathrm{nstrain\,yr^{-1}} .
$$

So **a strain rate of $1\ \mathrm{nstrain\,yr^{-1}}$ produces
$1\ \mathrm{mm\,yr^{-1}}$ of velocity difference across $1000\
\mathrm{km}$**, or $0.1\ \mathrm{mm\,yr^{-1}}$ across $100\ \mathrm{km}$. That
single ratio is why strain-rate estimation is a signal-to-noise problem in
almost every setting.

## 2. The SYNTHETIC experiment

The demonstration builds a velocity field from a known tensor
($\mathrm{nstrain\,yr^{-1}}$):

$$
L = \begin{pmatrix} 30 & -5 \\ 35 & -10\end{pmatrix}\times10^{-9}
\ \mathrm{yr^{-1}}
\quad\Longrightarrow\quad
E = \begin{pmatrix} 30 & 15 \\ 15 & -10\end{pmatrix}\times10^{-9},
\qquad w = 20\times10^{-9}\ \mathrm{yr^{-1}} .
$$

The principal strain rates and the azimuth of $e_1$ (clockwise from north) are

$$
e_1 = 35.000\times10^{-9}\ \mathrm{yr^{-1}},\qquad
e_2 = -15.000\times10^{-9}\ \mathrm{yr^{-1}},\qquad
\text{azimuth} = 71.57^\circ,\qquad
\text{dilatation} = 20.000\times10^{-9}\ \mathrm{yr^{-1}} .
$$

Twenty-four sites are scattered over a $120\ \mathrm{km}\times120\ \mathrm{km}$
square and given $0.5\ \mathrm{mm\,yr^{-1}}$ isotropic velocity noise. Velocity
magnitudes are $0.54$–$2.58\ \mathrm{mm\,yr^{-1}}$ (mean $1.45$): the signal
across the whole network is only a few times the noise, which is typical and is
the reason the estimation is delicate.

The least-squares problem stacks, for each site,

$$
v_E = v_{E0} + L_{EE}\,x_E' + L_{EN}\,x_N', \qquad
v_N = v_{N0} + L_{NE}\,x_E' + L_{NN}\,x_N',
$$

with $x' = x - \bar x$ in millimetres. The recovered tensor and its
residual-derived covariance:

| quantity | true ($10^{-9}\ \mathrm{yr^{-1}}$) | recovered | formal $\sigma$ | (rec − true)/$\sigma$ |
|---|---|---|---|---|
| $E_{EE}$ | 30.000 | 29.941 | 3.080 | $-0.02$ |
| $E_{NN}$ | $-10.000$ | $-11.029$ | 2.966 | $-0.35$ |
| $E_{EN}$ | 15.000 | 13.862 | 2.138 | $-0.53$ |
| $w$ | 20.000 | 18.498 | 2.138 | $-0.70$ |

Residual rms $0.417\ \mathrm{mm\,yr^{-1}}$ against an input noise of
$0.5\ \mathrm{mm\,yr^{-1}}$ — slightly below, as expected when the residuals
have three fewer degrees of freedom than the data.

Principal values from the recovered tensor: $e_1 = 34.190$,
$e_2 = -15.278$ (both $10^{-9}\ \mathrm{yr^{-1}}$), azimuth $72.96^\circ$,
dilatation $18.912$. The azimuth is recovered to $1.4^\circ$ and the eigenvalues
to a few per cent, i.e. **non-linear functions of the tensor can be recovered
well even when the tensor components individually are only good to
$10\%$** — but only because the network is well conditioned. There is no general
rule here; the uncertainty of $e_1$ must be propagated or sampled, and the
demonstration presents the azimuth without an error bar deliberately, to make
that gap visible.

## 3. What the reference frame can and cannot give you

Add a rigid rotation of $10\times10^{-9}\ \mathrm{yr^{-1}}$ to every station
velocity and repeat the inversion. The demonstration finds:

- the strain-rate tensor is **unchanged**: the maximum change in any component
  is $6\times10^{-8}$ in units of $10^{-9}\ \mathrm{yr^{-1}}$, i.e. numerically
  zero ($\sim10^{-14}\ \mathrm{yr^{-1}}$);
- the rotation rate shifts by exactly $10.000\times10^{-9}\ \mathrm{yr^{-1}}$,
  from $18.498$ to $28.498$.

The physical statement is unavoidable: **the deformation field is absolute; the
rotation field is relative to an assumed frame.** A GNSS velocity field can be
expressed in any rigid frame, and the strain rate is frame-invariant by
construction because it is built from velocity *differences*. The rotation rate
is not, so quoting one requires stating the frame — usually a plate-fixed frame
whose realisation is itself a model choice
([13-03-01](../03-plate-tectonics-quantitative/01-plate-kinematics-models.md)).

A second, related caution: the reference velocity $v_0$ and the tensor are
estimated jointly from the same data, so an error in the assumed frame appears
as an apparent rotation, not as apparent strain. That is a **feature**: it means
that a frame error cannot masquerade as deformation, provided the analyst does
not also fix the rotation by construction (e.g. by imposing zero rotation about
a chosen point).

## 4. Aperture, not station count

The scaling argument is the same one derived for Euler poles, applied to a
velocity *gradient*. The velocity difference across a network of aperture $L$ is
$|\nabla v|L$, and the noise is $\sigma$ per component, so

$$
\delta(\text{strain rate}) \sim \frac{\sigma}{L}, \qquad
\text{relative error} \sim \frac{\sigma}{|\nabla v|\,L} .
$$

The demonstration measures it with 20-site networks of increasing aperture, 200
realisations each, at $0.5\ \mathrm{mm\,yr^{-1}}$ noise:

| aperture (km) | 20 | 40 | 80 | 160 | 320 |
|---|---|---|---|---|---|
| rms error in $e_1$ ($10^{-9}\ \mathrm{yr^{-1}}$) | 19.299 | 10.496 | 5.043 | 2.542 | 1.147 |
| rms error in $w$ ($10^{-9}\ \mathrm{yr^{-1}}$) | 14.070 | 7.019 | 3.749 | 1.754 | 0.818 |

Each doubling of the aperture halves the error, to better than $10\%$ over the
whole range. Two practical readings:

- **A dense local network cannot measure a regional strain rate.** In the
  smallest network, the error in $e_1$ ($19.3\times10^{-9}\ \mathrm{yr^{-1}}$)
  is more than half the true value ($35\times10^{-9}$). No amount of extra
  stations inside the same $20\ \mathrm{km}$ can fix it, because they sample the
  same velocity differences.
- **Station count buys $\sqrt N$, aperture buys $N$.** Adding stations inside a
  fixed footprint reduces the error as $\sqrt N$ (averaging independent noise
  measurements of the same gradient); extending the footprint reduces it as $L$
  directly. Both matter, and they are not interchangeable.

The residual check is worth stating in the same breath: in every one of these
networks the residual rms sits at the noise level. A good fit says nothing about
the aperture, and therefore nothing about the strain-rate uncertainty.

## 5. One bad station

Real networks contain blunders: a mis-levelled monument, an incorrectly
attributed antenna, an unmodelled coseismic step. The demonstration offsets
station 4 by $(15, -12)\ \mathrm{mm\,yr^{-1}}$, a $19.2\ \mathrm{mm\,yr^{-1}}$
vector — large, but well within the range of a real decade-scale error.

Consequences:

| quantity | clean estimate | with the blunder | truth |
|---|---|---|---|
| $e_1$ ($10^{-9}\ \mathrm{yr^{-1}}$) | 34.190 | 36.204 | 35.000 |
| change from clean | — | $+2.01$ ($6\%$ of the signal) | — |

and the residual inspection identifies it immediately: the largest residual is
$18.26\ \mathrm{mm\,yr^{-1}}$, the next largest $2.06\ \mathrm{mm\,yr^{-1}}$,
the median $1.03\ \mathrm{mm\,yr^{-1}}$. **The culprit's residual is $17.7$ times
the median of the others.**

Two conclusions:

1. **A single bad station does not destroy a large network's strain rate.** With
   24 sites, one $19\ \mathrm{mm\,yr^{-1}}$ blunder moved $e_1$ by $6\%$. Least
   squares is not robust, but it is not helpless: the blunder's leverage is
   one site out of twenty-four.
2. **Residual inspection is not optional.** The tell-tale is a residual far
   larger than the rest of the population, not a large residual per se. Always
   plot, or at least tabulate, residuals against station before publishing a
   strain-rate field; and re-estimate without the flagged station to see whether
   the deformation field changes materially.

## 6. Assumptions and regime of validity

1. **Homogeneous strain.** The velocity is linear in position across the
   network, which permits exactly one tensor. Real networks span gradients
   (strain-rate changes, fault-block rotation) and the correct treatment
   segments the network or inverts for spatially varying fields.
2. **Infinitesimal, 2-D strain.** The tensor is treated as small and horizontal.
   This fails in a volcanic or coseismic setting where displacements are large;
   it also discards vertical velocities, which is right for far-field
   tectonics and wrong near a magma chamber.
3. **A rigid reference frame.** Velocities must be in a frame whose own motion
   is known; otherwise an unknown rigid rotation is absorbed into $w$ (Section
   3).
4. **Gaussian, independent, isotropic noise.** The covariance assumes it. GNSS
   errors are spatially correlated (orbit, atmosphere, network adjustment), which
   makes the formal uncertainties optimistic, most severely for small networks.
5. **No rigid-block assumption.** Each station is an independent estimate of the
   field. If the region is made of rigid blocks, an affine fit averages their
   different motions into a meaningless tensor.
6. **Aperture smaller than the scale of the strain-rate variation.** If the field
   varies within the network, a single tensor is a spatial average, and its
   uncertainty cannot be obtained from the residual scatter alone.
7. **No transient deformation.** A postseismic or interseismic transient inside
   the observation window biases the estimated field; linear trends must be
   verified against the time series, not assumed
   ([13-04-03](03-postseismic-viscoelastic.md)).

## 7. Worked example — designing a network for a target uncertainty

A SYNTHETIC project needs $e_1$ to $10\%$ of $30\times10^{-9}\ \mathrm{yr^{-1}}$,
i.e. to $3\times10^{-9}\ \mathrm{yr^{-1}}$, with $0.5\ \mathrm{mm\,yr^{-1}}$
noise. From the measured scaling
$\delta e_1 \approx 386/L$ (in $10^{-9}\ \mathrm{yr^{-1}}\,(\mathrm{km})$, fitted
to the table: $19.3\times20 = 386$, $1.147\times320 = 367$):

$$
L = \frac{386}{3} = 129\ \mathrm{km}.
$$

So an aperture of $\sim130\ \mathrm{km}$ is required. From the table, $160\
\mathrm{km}$ gives $2.5\times10^{-9}\ \mathrm{yr^{-1}}$ and is comfortably
inside the target, while $80\ \mathrm{km}$ gives $5.0\times10^{-9}\
\mathrm{yr^{-1}}$ and fails. The lesson's structure is visible in the arithmetic:
a doubling of the aperture is worth more than a doubling of the station count,
so the design decision is about extent, not density.

**A caveat that belongs with the number.** Extending the network to $160\
\mathrm{km}$ risks violating assumption 1: if the region contains a major fault
that partitions it into blocks with different strain rates, the single tensor is
then an average and the extra aperture buys precision at the cost of accuracy.
Section 6, item 5 is the reason that sentence has to be written.

## 8. Python demonstration

`code/crustal_deformation_gps_demo.py` prints labelled results with units and
exits 0. It:

1. builds a synthetic 24-site network and a velocity field from a known tensor;
2. inverts for $L$, $v_0$ and the covariance, and reports the components against
   the truth in units of their formal errors;
3. computes the principal strain rates, azimuths and the dilatation rate;
4. performs the reference-frame test, showing strain rate invariance and the
   exact shift of the rotation rate;
5. measures the aperture scaling over five network sizes with 200 realisations
   each;
6. injects a $19\ \mathrm{mm\,yr^{-1}}$ blunder and shows both the damage and
   the residual signature that identifies it.

## Mastery checkpoint

Complete this without notes.

> A network of 20 sites spans $L = 50\ \mathrm{km}$ with
> $0.4\ \mathrm{mm\,yr^{-1}}$ velocity noise. **(a)** Using
> $\delta e_1 \approx 386/L$ in units of $10^{-9}\ \mathrm{yr^{-1}}$ per km
> (measured at $0.5\ \mathrm{mm\,yr^{-1}}$ noise), estimate the strain-rate
> uncertainty and rescale it to the stated noise. **(b)** A target uncertainty
> of $2\times10^{-9}\ \mathrm{yr^{-1}}$ is required; what aperture is needed?
> **(c)** The velocity field is expressed in a frame that rotates by
> $5\times10^{-9}\ \mathrm{yr^{-1}}$ relative to the intended one. State which
> reported quantities change and by how much. **(d)** One station's residual is
> 25 times the median. State two actions a careful analyst takes and why neither
> is optional.

## Common pitfalls

1. **Reporting a strain rate without a frame.** Strain rate is frame-invariant;
   rotation rate is not, and quoting one without the other hides the choice.
2. **Estimating a strain rate from a small network.** The demonstration's
   $20\ \mathrm{km}$ network has an error of $19.3\times10^{-9}\
   \mathrm{yr^{-1}}$ on a $35\times10^{-9}\ \mathrm{yr^{-1}}$ signal.
3. **Interpreting a good fit as a good estimate.** Residuals sit at the noise
   level for every network in Section 4, including the ones with unusable error
   bars.
4. **Propagating uncertainties linearly through $e_1$ and the azimuth.** They are
   non-linear functions of the components; sample or linearise explicitly.
5. **Ignoring spatial correlation of GNSS errors.** It inflates the true error
   of small-network estimates far above the formal value.
6. **Fitting one tensor to a block-structured region.** The result is an average
   with no physical meaning.
7. **Leaving a blunder in.** One $19\ \mathrm{mm\,yr^{-1}}$ outlier moved $e_1$
   by $6\%$; with a smaller network the damage is proportionally worse.

## Related modules

- [13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](02-fault-mechanics.md) —
  what the strain rate is loading.
- [13-04-04 Interseismic Coupling and Megathrust Locking](04-interseismic-coupling.md) —
  the same data used to infer coupling on a megathrust.
- [13-03-01 Plate Kinematic Models and Euler Pole Inversion](../03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  the rigid-motion limit, and the same aperture argument.
- [13-06-02 Volcano Deformation, Magma Chamber Models and InSAR](../06-crustal-and-lithospheric-dynamics/02-volcano-geodesy.md) —
  where vertical and transient deformation matter.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md).
- [07-04 Geodesy Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md).
