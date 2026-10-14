---
id: 13-04-04
title: "Interseismic Coupling and Megathrust Locking"
level: research
prereqs: ["13-04-01", "13-04-02", "13-02-04"]
tags: [geodynamics, tectonophysics, interseismic, coupling, megathrust, subduction, back-slip]
---

# Interseismic Coupling and Megathrust Locking

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the interseismic surface-velocity profile of a fault locked from
   the surface to depth $d$ in 2-D anti-plane strain, including the
   surface-relative-velocity limit that defines the coupling.
2. **Build** a discretised back-slip model from the single-patch solution, and
   **verify** it against the closed form.
3. **Quantify** the trade-off between coupling value and coupling depth, and
   **demonstrate** which stations resolve it.
4. **Invert** for a patchwise coupling distribution, and **interpret** the
   resolution diagonal and the parameter standard deviations rather than the
   patch values alone.
5. **Compute** the moment deficit rate from a coupling model and **convert** it
   into a magnitude and a recurrence time.
6. **State** the assumptions of the elastic back-slip model and **identify** the
   observations that require a 3-D, dipping, viscoelastic alternative.

## Prerequisites

- [13-04-01 Crustal Deformation from GNSS and Strain Rates](01-crustal-deformation-gps.md) —
  the velocity field that is inverted here.
- [13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](02-fault-mechanics.md) —
  the anti-plane solution reused, and the friction that limits the locked zone.
- [13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull](../02-mantle-convection/04-subduction-dynamics.md) —
  the geometry of the interface being locked.

All models and data in this module are **SYNTHETIC**. The plate rate, coupling
distribution, fault length and noise are chosen teaching values; no real
subduction zone, GNSS site or published coupling model is used. The elastic
model is the exact 2-D anti-plane solution for a **vertical** fault — a teaching
analogue of a dipping megathrust, whose limitation is stated in Section 6. The
exact constants used are $1\ \mathrm{mm\,yr^{-1}} = 1\ \mathrm{km\,Myr^{-1}}$
and the standard moment–magnitude relation
$M_w = \tfrac23(\log_{10}M_0 - 9.1)$.

## 1. The back-slip model

An interseismic velocity field contains the long-term plate motion plus a
perturbation caused by friction on the locked part of the interface. The
**back-slip** device separates them:

$$
v_{\text{observed}} = v_{\text{creep everywhere}} + v_{\text{back-slip}},
$$

where the back-slip is the (negative) slip on the locked zone that would cancel
the long-term sliding there. In 2-D anti-plane strain — the medium moves only
along strike — a **surface-breaking patch** spanning depths $[0, d]$ with slip
rate $s$ produces a surface velocity

$$
v_{\text{patch}}(x) = -\frac{2s}{\pi}\operatorname{atan2}(d, x)
\quad\text{(up to a constant step)},
$$

and Section 1.1 shows how the step is fixed by the requirement that the far
fields differ by the plate rate $V$.

### 1.1 The closed-form profile

Requiring (i) no relative motion at the fault trace when the fault is fully
locked, (ii) a far-field relative velocity $V$, and (iii) a transition spread
over the depth scale $d$, gives

$$
\boxed{\;v(x) = \frac{V}{2}\operatorname{sgn}(x)
- \frac{\chi V}{\pi}\left[\operatorname{atan2}(d, x)
- \operatorname{atan2}(0, x)\right]\;}
$$

with $\operatorname{atan2}(0,x) = 0$ for $x>0$ and $\pi$ for $x<0$, and
$\chi \in [0,1]$ the **coupling coefficient** of the patch. Two limits are worth
tabulating, because they are the checks the demonstration performs:

| $\chi$ | $v(0^+)$ | $v(10\ \mathrm{km})$ | $v(50\ \mathrm{km})$ | $v(\infty)$ |
|---|---|---|---|---|
| $1.0$ (locked) | 0.00 | 4.10 | 13.12 | 20.00 |
| $0.5$ | 10.00 | 12.05 | 16.56 | 20.00 |
| $0.0$ (creeping) | 20.00 | 20.00 | 20.00 | 20.00 |

with $V = 40\ \mathrm{mm\,yr^{-1}}$, $d = 30\ \mathrm{km}$ and all velocities in
$\mathrm{mm\,yr^{-1}}$. In every case the far-field velocity is $V/2 = 20\
\mathrm{mm\,yr^{-1}}$, and the **relative** velocity across the fault is
$V(1-\chi)$ at the trace against $V$ far away. That relative velocity is what
"coupling" means: the fraction of the long-term slip rate that is *not*
currently being accommodated by slip.

### 1.2 From one patch to many

Linearity of the anti-plane problem means patches superpose. Discretising the
fault into $N$ patches with bounds $z_j$ and couplings $\chi_j$ gives

$$
v(x) = \frac{V}{2}\operatorname{sgn}(x) - \frac{V}{\pi}
\sum_{j=1}^{N}\chi_j\left[\operatorname{atan2}(z_{j+1},x)
- \operatorname{atan2}(z_j, x)\right],
$$

which is a **linear** function of the coupling vector. That single fact is what
makes the inverse problem tractable — and, as Section 4 shows, it is also what
makes it ill-posed.

The demonstration verifies the discretisation against the closed form: for a
single patch to $30\ \mathrm{km}$ represented on $10$ patches spanning
$0$–$80\ \mathrm{km}$ (with the straddling patch partially coupled), the
maximum difference over 22 stations is $0.0605\ \mathrm{mm\,yr^{-1}}$ — an order
of magnitude below the $1\ \mathrm{mm\,yr^{-1}}$ noise. Discretisation error is
therefore not the limitation; the trade-off in Section 3 is.

## 2. The depth–coupling trade-off, quantified

Take two SYNTHETIC coupling models that store the **same** total slip deficit
rate:

- **Model A:** $\chi = 1.0$ from $0$ to $20\ \mathrm{km}$ (deficit
  $20\times V$);
- **Model B:** $\chi = 0.6$ from $0$ to $40\ \mathrm{km}$ (deficit
  $0.6\times40\times V = 24\times V$ — the demonstration uses these values and
  reports the *profile difference*, so the comparison is of shapes rather than of
  identical deficits).

| $x$ (km) | $v_A$ | $v_B$ | $A - B$ (mm/yr) |
|---|---|---|---|
| 5 | 3.236 | 8.950 | $-5.714$ |
| 10 | 6.069 | 9.871 | $-3.802$ |
| 20 | 10.127 | 11.542 | $-1.415$ |
| 35 | 13.444 | 13.491 | $-0.048$ |
| 50 | 15.179 | 14.845 | $+0.334$ |
| 75 | 16.690 | 16.257 | $+0.433$ |
| 110 | 17.713 | 17.336 | $+0.377$ |
| 220 | 18.846 | 18.626 | $+0.220$ |
| 300 | 19.153 | 18.987 | $+0.165$ |

Two numbers decide whether an experiment can tell them apart, and they disagree:

- **Near the fault ($\lvert x\rvert \le 30\ \mathrm{km}$)** the models differ by
  up to $5.714\ \mathrm{mm\,yr^{-1}}$, **5.7 times** the
  $1\ \mathrm{mm\,yr^{-1}}$ SYNTHETIC noise. Such stations separate them cleanly.
- **Inland ($\lvert x\rvert \ge 50\ \mathrm{km}$)** the maximum difference is
  $0.433\ \mathrm{mm\,yr^{-1}}$, **0.4 times** the noise. A land network whose
  closest station is $50\ \mathrm{km}$ from the trace cannot distinguish the two
  models at all.

**This is the central practical result of the lesson.** Coupling depth is
resolved by stations close to the fault trace, and almost nothing else:
the kernel for a patch at depth $z$ decays over a distance of order $z$, so a
network that begins tens of kilometres inland is blind to the deepest part of
the locking zone. It is the quantitative justification for seafloor geodesy,
and for using independent observables — seismicity, tsunami data, gravity — as
additional constraints.

## 3. Inverting for coupling

The inversion is linear and can be written directly. With the kernel matrix
$K$ (in $\mathrm{mm\,yr^{-1}}$ per unit coupling) and the observed velocities
relative to a creeping reference,

$$
\Delta v = K\,\chi, \qquad
\begin{pmatrix} K \\ \lambda D\end{pmatrix}\chi =
\begin{pmatrix}\Delta v \\ 0\end{pmatrix},
$$

where $D$ is a first-difference (smoothness) operator and $\lambda$ a weight.
The damping is not cosmetic: without it, patches with nearly identical kernels
produce large oscillating couplings that cancel in the predicted velocities.

The demonstration uses $10$ patches over $0$–$80\ \mathrm{km}$, the 16 SYNTHETIC
stations of Section 2, $1.0\ \mathrm{mm\,yr^{-1}}$ noise, 200 realisations and
$\lambda = 2.0$:

| patch | depth range (km) | true $\chi$ | recovered mean | std | resolution diag |
|---|---|---|---|---|---|
| 1 | 0–8 | 1.00 | 1.00 | 0.07 | 0.91 |
| 2 | 8–16 | 1.00 | 1.05 | 0.10 | 0.39 |
| 3 | 16–24 | 1.00 | 0.97 | 0.13 | 0.30 |
| 4 | 24–32 | 1.00 | 0.80 | 0.12 | 0.21 |
| 5 | 32–40 | 1.00 | 0.60 | 0.10 | 0.16 |
| 6 | 40–48 | 0.00 | 0.41 | 0.08 | 0.15 |
| 7 | 48–56 | 0.00 | 0.24 | 0.11 | 0.16 |
| 8 | 56–64 | 0.00 | 0.11 | 0.17 | 0.18 |
| 9 | 64–72 | 0.00 | 0.02 | 0.22 | 0.21 |
| 10 | 72–80 | 0.00 | $-0.03$ | 0.25 | 0.23 |

Read the table as an analyst, not as a scorecard:

1. **The resolution diagonal falls from $0.91$ to $0.15$.** A value near $1$ means
   the patch is determined by the data; near $0.15$ means it is mostly determined
   by the damping and its neighbours.
2. **The best-determined quantity is an integral.** The coupled depth extent is
   recovered as $41.3\ \mathrm{km}$ against a true $40.0\ \mathrm{km}$, and the
   slip-deficit integral as $1654$ against $1600\
   \mathrm{mm\,yr^{-1}\,km}$ ($+3.4\%$), while individual deep patches are
   off by tens of per cent.
3. **The deep recovery is a smeared ramp, not a step.** The true coupling jumps
   from $1$ to $0$ between patches 5 and 6; the recovered values decay gradually.
   Reporting "coupling $= 0.41$ at $40$–$48\ \mathrm{km}$" would be a
   misinterpretation — the correct statement is "the data cannot place the
   transition more precisely than $\pm10\ \mathrm{km}$, and the smooth model
   spreads it".

## 4. From coupling to moment deficit and magnitude

The slip deficit rate on patch $j$ is $\chi_j V$, so the moment deficit rate is

$$
\dot M_0 = \mu \int \chi V\,\mathrm dA = \mu\,V\,L_{\text{strike}}
\sum_j \chi_j\,\Delta z_j ,
$$

with $L_{\text{strike}}$ the along-strike length. For the SYNTHETIC model
($\mu = 30\ \mathrm{GPa}$, $V = 40\ \mathrm{mm\,yr^{-1}}$, $L = 200\
\mathrm{km}$, coupled depth extent $40\ \mathrm{km}$):

$$
A_c = 200\ \mathrm{km}\times40\ \mathrm{km} = 8000\ \mathrm{km^{2}}
= 8.000\times10^{9}\ \mathrm{m^{2}},
$$
$$
\dot M_0 = 3\times10^{10}\times0.040\times8.000\times10^{9}
= 9.60\times10^{18}\ \mathrm{N\,m\,yr^{-1}} .
$$

Over $100\ \mathrm{yr}$ the accumulated deficit is
$9.60\times10^{20}\ \mathrm{N\,m}$, which corresponds to

$$
M_w = \tfrac23\left(\log_{10}9.60\times10^{20} - 9.1\right)
= \tfrac23\left(20.98 - 9.1\right) = 7.92 .
$$

Two honest observations about that arithmetic:

- **The magnitude is not a forecast.** It is the moment that *would* be released
  if the entire coupled zone failed in one event after $100\ \mathrm{yr}$ of
  unrelieved deficit. Real subduction zones release much of it in smaller
  events, aseismically, or not at all.
- **The sensitivity is asymmetric.** A coupling error of $0.1$ over the same
  area changes the moment rate by $10\%$ and the magnitude by $0.028$ units —
  small. But an error in the **coupled depth extent** changes the moment rate
  proportionally: underestimating the locked zone from $40$ to $20\ \mathrm{km}$
  halves the moment rate and reduces $M_w$ by $0.20$ units. Section 2 says the
  depth extent is exactly the quantity that inland networks cannot resolve.

## 5. Assumptions and regime of validity

1. **2-D anti-plane strain on a vertical fault.** This is the model's most
   serious limitation. A real megathrust dips at $10^\circ$–$30^\circ$, so
   (i) the surface projection of a patch is not its depth, (ii) the vertical and
   horizontal components of the deformation couple, and (iii) the kernel has a
   different shape and a different along-dip dependence. The *qualitative*
   conclusions — near-trench stations resolve depth, inland stations do not, and
   depth trades against coupling — survive the upgrade to 3-D; the numbers do
   not.
2. **A purely elastic medium.** Viscoelastic relaxation redistributes stress
   between earthquakes and biases the velocities used as data
   ([13-04-03](03-postseismic-viscoelastic.md)). Postseismic transients from the
   previous event must be removed first, and that removal is itself a model.
3. **Steady state.** The interseismic interval is assumed to be a steady phase of
   the seismic cycle. Ten to twenty years of GNSS data are a small fraction of a
   $200$–$1000\ \mathrm{yr}$ cycle, and slow transients within the window can be
   mistaken for the steady field.
4. **A known long-term rate $V$.** Taken as an input. An error in $V$ propagates
   directly into $\chi$, and $V$ usually comes from a plate model with its own
   frame and its own uncertainty.
5. **Simple coupling as the only unknown.** Real interfaces also have
   along-strike segmentation, a downdip transition zone, and possibly a
   permanent slip deficit that never fails; all of these are absorbed into
   $\chi$ if the model has one parameter per patch.
6. **Point-geometry kernels.** The discretisation treats patches as a stack of
   dislocations; the demonstration verified the discretisation error
   ($0.06\ \mathrm{mm\,yr^{-1}}$) is negligible compared with the noise, so this
   assumption is safe *given* the other five.
7. **The moment–magnitude relation and a single-event assumption.** Both are
   conventions for reporting, not physics.

## 6. Worked example — does this network resolve the locking depth?

A SYNTHETIC network has stations at $x = 5$, $15$, $50$, $120$ and
$250\ \mathrm{km}$, with $1\ \mathrm{mm\,yr^{-1}}$ noise. Compare the models of
Section 2 at those stations:

| $x$ (km) | $v_A$ | $v_B$ | difference |
|---|---|---|---|
| 5 | 3.236 | 8.950 | $-5.714$ |
| 15 | 8.351 | 10.741 | $-2.390$ |
| 50 | 15.179 | 14.845 | $+0.334$ |
| 120 | 17.899 | 17.542 | $+0.357$ |
| 250 | 19.038 | 18.858 | $+0.180$ |

1. **Near-field stations** ($5$ and $15\ \mathrm{km}$) see differences of
   $5.7$ and $2.4\ \mathrm{mm\,yr^{-1}}$: decisive.
2. **Far-field stations** see $\le 0.36\ \mathrm{mm\,yr^{-1}}$: not decisive on
   their own, but they constrain the far-field rate $V/2$ and therefore the
   reference frame.
3. **Design conclusion.** Two stations at $5$ and $15\ \mathrm{km}$ plus three
   inland are enough to distinguish these models; the same five stations placed
   all inland would not be. **The information is in the aperture of the
   near-trench sampling, not in the number of stations.**

A caveat that belongs with the design: the $5\ \mathrm{km}$ station is usually
underwater. That is precisely why the trade-off in Section 2 is a real
limitation and not a hypothetical one.

## 7. Python demonstration

`code/interseismic_coupling_demo.py` prints labelled results with units and exits
0. It:

1. evaluates the closed-form profile for $\chi = 1$, $0.5$ and $0$ and checks
   the limits against the derivation;
2. compares the discretised back-slip model with the closed form
   ($0.0605\ \mathrm{mm\,yr^{-1}}$ maximum difference);
3. quantifies the depth–coupling trade-off between models A and B, reporting
   separately what near-fault and inland stations can and cannot resolve;
4. inverts for coupling on ten patches over 200 realisations, reporting the
   resolution diagonal, the recovered coupled depth extent and the
   slip-deficit integral;
5. converts coupling to a moment deficit rate, an accumulated moment and a
   magnitude, and quantifies the sensitivity to a coupling error.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC megathrust-analogue is modelled as a vertical fault with
> $V = 50\ \mathrm{mm\,yr^{-1}}$, $\mu = 30\ \mathrm{GPa}$ and a strike length of
> $150\ \mathrm{km}$. **(a)** Write the surface velocity profile for a patch
> fully coupled from $0$ to $25\ \mathrm{km}$ and compute $v$ at $x = 10$ and
> $x = 100\ \mathrm{km}$ relative to the far field. **(b)** A second model has
> $\chi = 0.5$ from $0$ to $50\ \mathrm{km}$. At what distance do the two
> profiles differ by less than $1\ \mathrm{mm\,yr^{-1}}$, and what does that imply
> for a land network starting $40\ \mathrm{km}$ inland? **(c)** Compute the
> moment deficit rate and the $100$-year magnitude for the fully coupled model.
> **(d)** State the three assumptions in that calculation that would most change
> the answer.

## Common pitfalls

1. **Reading coupling per patch as if each were resolved.** The resolution
   diagonal in Section 3 falls to $0.15$; only the integral is well determined.
2. **Quoting a coupled depth from an inland network.** Inland stations see a
   $\le0.43\ \mathrm{mm\,yr^{-1}}$ difference between very different models.
3. **Ignoring postseismic transients.** A decaying transient inside the window
   biases every coupling estimate and is easily mistaken for a steady field.
4. **Forgetting that the fault dips.** A $40\ \mathrm{km}$ depth on a $20^\circ$
   interface is about $117\ \mathrm{km}$ from the trench; in the model here it is
   $40\ \mathrm{km}$. The geometries are not interchangeable.
5. **Treating the moment–magnitude conversion as a forecast.** It is the moment
   that would be released if everything failed at once.
6. **Undamped inversions.** Without smoothness damping, adjacent patches produce
   cancelling oscillations that the residual does not penalise.
7. **Taking $V$ as given.** The coupling coefficient scales as $1/V$; an error
   in the plate rate is an error in every patch.

## Related modules

- [13-04-01 Crustal Deformation from GNSS and Strain Rates](01-crustal-deformation-gps.md) —
  the velocities and their uncertainties.
- [13-04-03 Postseismic Relaxation and Viscoelastic Models](03-postseismic-viscoelastic.md) —
  the transient that must be removed before coupling is estimated.
- [13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull](../02-mantle-convection/04-subduction-dynamics.md).
- [13-03-01 Plate Kinematic Models and Euler Pole Inversion](../03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  the same aperture argument for a different inverse problem.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  what to do with a moment deficit once it is estimated.
- [18-03 Tikhonov Regularisation](../../18-inverse-problems/03-regularization/README.md) —
  the systematic treatment of the damping used in Section 3.
