---
id: 06-03-02
title: "The Double-Couple Source and Radiation Patterns"
level: graduate
prereqs: ["06-03-01", "06-01-02"]
tags: [seismology, double-couple, focal-mechanism, radiation-pattern, moment-tensor]
---

# The Double-Couple Source and Radiation Patterns

> **All models and data in this module are SYNTHETIC.** Every mechanism, axis and
> amplitude below comes from
> [`code/double_couple_demo.py`](code/double_couple_demo.py), which uses a single
> SYNTHETIC scale $M_0 = 1.0\times10^{19}\ \mathrm{N\,m}$. No real earthquake,
> focal mechanism or catalogue is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a source of elastic deformation in the Earth cannot be a net
   force or a net torque, and **derive** the double couple as the simplest
   admissible point source.
2. **Construct** the moment tensor $M = M_0\left(\hat n\hat s^{\mathsf T} +
   \hat s\hat n^{\mathsf T}\right)$ from strike, dip and rake, and **verify** it
   against the closed-form components.
3. **Derive** the far-field P amplitude $A(\hat r)\propto(\hat r\cdot\hat n)
   (\hat r\cdot\hat s)$ and **show** that it vanishes on the two nodal planes.
4. **Prove** the identity $(\hat r\cdot\hat n)(\hat r\cdot\hat s) =
   \tfrac12[(\hat r\cdot\hat P)^{2}-(\hat r\cdot\hat T)^{2}]$ and use it to
   **measure** the fraction of the focal sphere that is compressional.
5. **Compute** the first-motion polarity on a vertical ray for normal, thrust and
   strike-slip mechanisms, and **state** the correct rule connecting a vertical
   $T$ axis to normal faulting.
6. **Quantify** how the plunge of the compressional axis depends on fault dip,
   and **explain** why "vertical axis means thrust" is only a rule of thumb.
7. **State** the fault-plane ambiguity: first motions alone cannot distinguish the
   fault plane from the auxiliary plane.

## Prerequisites

- [06-03-01 Faulting, Slip and the Elastic Rebound Cycle](01-faulting-and-slip.md) —
  slip, area and the definition of seismic moment.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  the polarisation of the far-field P and S waves whose amplitudes we compute.
- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  module-level background.

## 1. Intuition: why the radiation pattern has four lobes

An earthquake is a patch of rock that suddenly slides. Deep underground, it
cannot push the whole planet in one direction: momentum must be conserved, so a
source that *injects* net linear momentum is impossible. What a fault can do is
apply a **couple** — two equal and opposite forces offset from one another, like
two hands twisting a lid. That couple has no net force and no net torque, so it is
admissible.

One couple alone is still not the whole story, for a reason that the demo makes
numerical: the far-field displacement produced by a moment tensor depends on the
*product* $(\hat r\cdot\hat n)(\hat r\cdot\hat s)$, and that product changes sign
when one of the two dot products changes sign. The result is not a single-lobed
pattern but **four lobes**: two compressional and two dilatational, separated by
two nodal planes.

Everything in this lesson follows from a single small matrix and one algebraic
identity. It is the cleanest piece of source theory in seismology, and it is also
where the two most common sign errors live — so the lesson measures where it can
and flags the conventions where it cannot.

## 2. Precise definitions

Throughout, the frame is Aki & Richards':

$$x = \text{North},\qquad y = \text{East},\qquad z = \text{Down}.$$

| Symbol | Meaning | Convention |
|---|---|---|
| $\hat n$ | fault normal (unit) | points from footwall to hanging wall |
| $\hat s$ | slip vector (unit) | **motion of the hanging wall** relative to the footwall; $\hat n\cdot\hat s = 0$ |
| $M_0$ | scalar seismic moment | $\mathrm{N\,m}$ |
| $M$ | moment tensor | $M = M_0(\hat n\hat s^{\mathsf T} + \hat s\hat n^{\mathsf T})$ |
| $\hat r$ | unit ray direction | from source to receiver |
| $A(\hat r)$ | far-field P amplitude factor | $\propto(\hat r\cdot\hat n)(\hat r\cdot\hat s)$, dimensionless |
| $\hat P$ | compressional bisector | $\hat P = (\hat n + \hat s)/\sqrt{2}$ |
| $\hat T$ | dilatational bisector | $\hat T = (\hat n - \hat s)/\sqrt{2}$ |

**Strike, dip, rake.** Strike $\phi$ is measured clockwise from North to the
fault's surface trace, dip $\delta$ from horizontal down to the fault plane, and
rake $\lambda$ in the fault plane from the strike direction to the slip vector.
The sign convention used here — and by essentially every catalogue — is
$\lambda = +90^\circ$ **thrust** (hanging wall up-dip), $\lambda = -90^\circ$
**normal** (hanging wall down-dip), $\lambda = 0$ left-lateral, $\lambda =
\pm180^\circ$ right-lateral. The demo builds $\hat n$ and $\hat s$ from
$(\phi,\delta,\lambda)$ and checks them against the closed-form components of
Aki & Richards (1980), eq. 4.88.

Two symmetry facts to keep in view, both proved in Section 3:

- $M$ is **symmetric** and **traceless**. Symmetry is why six components suffice;
  tracelessness is why a double couple cannot change volume.
- Reversing $\hat s$ (equivalently swapping which wall moved) changes the sign of
  $M$. Reversing *both* $\hat n$ and $\hat s$ leaves the radiation pattern
  unchanged, which is the fault-plane ambiguity in its algebraic form.

## 3. Derivations

### 3.1 Symmetry and tracelessness

Write the tensor as a matrix of force couples:

$$M = M_0\left(\hat n\hat s^{\mathsf T} + \hat s\hat n^{\mathsf T}\right).$$

Take the transpose: each outer product becomes its transpose and the two terms
swap, so $M^{\mathsf T} = M$. Symmetric, hence six independent components.

The trace: $\mathrm{tr}(M) = M_0\left(\hat s^{\mathsf T}\hat n +
\hat n^{\mathsf T}\hat s\right) = 2M_0\,\hat n\cdot\hat s = 0$, because the slip
vector lies in the fault plane and is therefore orthogonal to the fault normal.
**A double couple cannot change volume**, and its moment tensor has eigenvalues
$+M_0$, $0$, $-M_0$.

*Numerical check (SYNTHETIC).* $M_0 = 1.0\times10^{19}\ \mathrm{N\,m}$; the demo
compares the $(\hat n,\hat s)$ construction against the closed-form components for
six mechanisms and reports a worst absolute difference of
$2.048\times10^{3}\ \mathrm{N\,m}$ on components of size
$1.0\times10^{19}\ \mathrm{N\,m}$, i.e. a relative agreement of
$2.05\times10^{-16}$. The two constructions are the same object to round-off.

### 3.2 The far-field P radiation pattern

In the far field of a point source in a homogeneous isotropic medium, the P-wave
displacement is proportional to the quadrupole projection of the moment tensor
onto the ray direction (Aki & Richards 1980, ch. 4):

$$u_{\text{P}}(\hat r) \propto \frac{1}{4\pi\rho v_p^{3}\,r}\,
\hat r^{\mathsf T} M\,\hat r.$$

For $M = M_0(\hat n\hat s^{\mathsf T} + \hat s\hat n^{\mathsf T})$,

$$\hat r^{\mathsf T}M\hat r
= M_0\left[(\hat r\cdot\hat n)(\hat s\cdot\hat r)
+ (\hat r\cdot\hat s)(\hat n\cdot\hat r)\right]
= 2M_0\,(\hat r\cdot\hat n)(\hat r\cdot\hat s).$$

So the amplitude pattern, up to a positive factor, is

$$\boxed{\;A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s),\;}$$

and the **sign of $A$ is the first-motion polarity**: $A>0$ means compressional
(ground first moves away from the source along the ray), $A<0$ dilatational.

### 3.3 Nodal planes

$A$ vanishes when either dot product vanishes:

- $\hat r\cdot\hat n = 0$: the plane whose normal is $\hat n$ — the **fault
  plane**;
- $\hat r\cdot\hat s = 0$: the plane whose normal is $\hat s$ — the **auxiliary
  plane**.

These are two orthogonal great circles that cut the focal sphere into four lobes.
An equivalent, coordinate-free statement is often more convenient:

$$M\hat n = M_0\left(\hat n(\hat s\cdot\hat n) + \hat s(\hat n\cdot\hat n)\right)
= M_0\hat s,\qquad M\hat s = M_0\hat n.$$

A double couple maps the fault normal to the slip direction and vice versa.
The demo checks $\|M\hat n - M_0\hat s\|$ and $\|M\hat s - M_0\hat n\|$ and finds
worst values of $2.220\times10^{-16}$ in units of $M_0$ — i.e. zero.

### 3.4 The bisector identity

Define the unit bisectors $\hat P = (\hat n+\hat s)/\sqrt2$ and
$\hat T = (\hat n-\hat s)/\sqrt2$ (they are orthogonal and unit, since
$\hat n\perp\hat s$). Then

$$(\hat r\cdot\hat P)^{2}-(\hat r\cdot\hat T)^{2}
= \frac{1}{2}\left[(\hat r\cdot\hat n+\hat r\cdot\hat s)^{2}
- (\hat r\cdot\hat n-\hat r\cdot\hat s)^{2}\right]
= \frac{1}{2}\left[4(\hat r\cdot\hat n)(\hat r\cdot\hat s)\right],$$

so

$$\boxed{\;A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s)
= \tfrac12\left[(\hat r\cdot\hat P)^{2}-(\hat r\cdot\hat T)^{2}\right].\;}$$

*Numerical check.* Over $20\,000$ random directions the demo finds a maximum
$|\mathrm{LHS}-\mathrm{RHS}|$ of $3.331\times10^{-16}$, i.e. a relative deviation
of $6.664\times10^{-16}$ from a maximum $|A|$ of order $0.5$. The identity is
exact.

The identity says something important: the sign of $A$ is decided by whether the
ray direction is closer to the $\hat P$ axis than to the $\hat T$ axis. The
**compressional quadrants are those bisected by $\hat P$**, the dilatational
quadrants those bisected by $\hat T$.

### 3.5 Half the focal sphere is compressional

Write $\hat r$ in a frame where $\hat P$ and $\hat T$ are two of the axes. If
$\theta$ is the angle from $\hat P$, then
$\cos\theta = \hat r\cdot\hat P$ and $\hat r\cdot\hat T = \pm\sin\theta$, so
$A = \tfrac12(\cos^2\theta - \sin^2\theta) = \tfrac12\cos2\theta$. The set
$A>0$ is $\theta\in(0^\circ,45^\circ)\cup(135^\circ,180^\circ)$ — two antipodal
cones whose solid angles are equal by symmetry. Together they contain **exactly
half the sphere**.

*Numerical check.* The demo samples $400\,000$ directions and measures the
compressional fraction as $0.50153$, $0.49846$ and $0.50162$ for three
mechanisms, against an expected $0.50000$. The scatter is the sampling error of a
finite random sample, not a physical asymmetry. **A double couple radiates
compression over half of all directions whatever the mechanism**, and the sign is
the *same* in antipodal lobes (so a station and its antipode read the same
polarity).

## 4. Physical interpretation

### 4.1 First motion on a vertical ray, and the vertical-axis rule

A ray going straight up has $\hat r = (0,0,-1)$ in the $N,E,\text{Down}$ frame.
Then $A = (\hat r\cdot\hat n)(\hat r\cdot\hat s) = n_z s_z$ (up to an overall
sign from the $-1$ factors, which the demo tracks explicitly). The demo prints:

| mechanism | $(\hat n\!\cdot\!\text{up})(\hat s\!\cdot\!\text{up})$ | polarity straight up |
|---|---|---|
| normal, dip $45^\circ$ | $-0.5000$ | DILATATIONAL |
| thrust, dip $45^\circ$ | $+0.5000$ | COMPRESSIONAL |
| strike-slip | $+0.0000$ | NODAL (no P) |
| normal, dip $60^\circ$ | $-0.4330$ | DILATATIONAL |
| thrust, dip $20^\circ$ | $+0.3214$ | COMPRESSIONAL |

The physical reading of the two rules of thumb:

- **A thrust gives compression directly above the source**, so its compressional
  ($P$) axis is near-vertical. The demo reports $P$ plunge $-90^\circ$ (i.e.
  straight up) for a thrust at $45^\circ$ dip.
- **A normal fault gives dilatation above the source**, because the hanging wall
  slides *down* and the rock above the source is stretched. So a normal fault has
  a near-vertical $T$ axis — and the demo reports $T$ plunge $-90^\circ$ for the
  normal mechanism. Note carefully: *a normal fault does not push the ground
  above it upwards.* The rule "a vertical $T$ axis means normal faulting" is
  correct and is consistent *only* with dilatation above the source.
- **A strike-slip on a vertical plane radiates nothing along the vertical**, which
  is why its $P$ and $T$ axes are both horizontal ($P$ plunge $-0.0^\circ$,
  $T$ plunge $-0.0^\circ$ in the demo).

### 4.2 How vertical is "vertical"? The dip dependence

The vertical-axis rules are exact only at $45^\circ$ dip. The demo tabulates the
plunge of the compressional axis for pure dip-slip mechanisms:

| dip (deg) | 5 | 10 | 20 | 30 | 40 | 45 | 50 | 60 | 70 | 80 | 85 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| thrust $P$ plunge (deg) | 50 | 55 | 65 | 75 | 85 | 90 | 85 | 75 | 65 | 55 | 50 |

The pattern is $\text{plunge} = 90^\circ - |\text{dip}-45^\circ|$, i.e.
$45^\circ+\text{dip}$ for $\text{dip}\le45^\circ$ and $135^\circ-\text{dip}$ for
$\text{dip}>45^\circ$: exactly $90^\circ$ at $45^\circ$, and symmetric about it. At a thrust dip of
$20^\circ$ the compressional axis plunges only $65^\circ$. So the identity is the
tabulated plunge; "vertical axis" is a rule of thumb valid for dips near
$45^\circ$.

### 4.3 P and T axes are not the fault planes

The $\hat P$ and $\hat T$ axes are the bisectors of the *dihedral angles between
the two nodal planes*, not the planes themselves. Plotting $\hat P$ and $\hat T$
gives a compact picture of the stress orientation that a mechanism implies, and
this is why focal-mechanism maps of, say, a subduction zone are read as a stress
field. But the axes are derived quantities; they are not observed directly and
they are not unique to a mechanism (a mechanism and its counterpart rotated by
$90^\circ$ about the $\hat P$ axis share $\hat P$ and $\hat T$).

### 4.4 The fault-plane ambiguity, and the sign trap

Two facts together:

1. **Ambiguity.** First motions determine the two nodal planes but not which is
   the fault. The radiation pattern is invariant under $(\hat n,\hat s)\to
   (-\hat n,-\hat s)$, i.e. under exchanging the fault and auxiliary planes.
2. **Sign trap.** Reversing *only* $\hat s$ (using footwall motion instead of
   hanging-wall motion) flips the sign of the whole pattern, which swaps the
   labels $P$ and $T$.

The demo makes the trap visible: obspy's eigen-labels for the same tensor come
out as the mirror image for the normal and thrust cases (obspy $T$ dip $0.0$ where
the demo has $P$ dip $90.0$, and vice versa), and they agree for strike-slip. The
disagreement is a slip-sign convention, not a disagreement about physics, and it
is why this lesson computes the axes from an explicitly printed convention
instead of trusting a library's labels.

**Consequence.** Any statement of the form "the $P$ axis is here" is incomplete
without the slip-sign convention. The convention in this module is written at the
top of the demo and repeated in Section 2.

## 5. Assumptions and regime of validity

1. **Point source.** The formula holds in the far field, at distances large
   compared with the source dimension. The whole of
   [04 Source Time Functions](04-source-time-function.md) is what happens when
   this fails.
2. **Homogeneous, isotropic medium.** Anisotropy rotates the polarisations and
   the radiation pattern away from $A(\hat r)$; see
   [06-01-08 Anisotropic Propagation](../01-elastic-wave-propagation/README.md).
3. **Far-field P only.** The near-field and static terms, and the S radiation
   (which is a *vector* pattern $\propto(\hat s - (\hat s\cdot\hat r)\hat r)$-like
   combination, not a scalar), are omitted. The demonstration's amplitudes are P
   amplitudes.
4. **No attenuation or scattering.** Amplitudes are compared at the same distance
   and frequency band; real amplitudes are filtered by $Q$ (see
   [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md)).
5. **Elastic, instantaneous slip.** No friction law, no rupture propagation; the
   slip is a step on a prescribed plane.
6. **The moment tensor is symmetric and traceless.** Volume-changing sources
   (explosions, [07](07-nuclear-explosion-sources.md)) break tracelessness, and a
   single force or a single couple would break symmetry and is physically
   inadmissible.

**Consequence for interpretation.** A focal mechanism is an *inversion result*
under assumptions 1–6. It is not an observation. The four-lobe pattern is
observed; the tensor is inferred; the fault plane is a further inference that
needs aftershocks, surface geology or geodesy to settle.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $\hat n$, $\hat s$, $\hat r$, $\hat P$, $\hat T$ | — | unit vectors; their dot products are dimensionless |
| $A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s)$ | — | product of two dimensionless numbers; the demo prints it as a pure number |
| $M$, each component | $\mathrm{N\,m}$ | $M_0 \times$ (dimensionless outer products) |
| $\hat r^{\mathsf T}M\hat r$ | $\mathrm{N\,m}$ | a tensor component times dimensionless factors |

The demo normalises all amplitudes by $M_0$ so that the printed numbers are
dimensionless. The identities it checks ($\|M\hat n - M_0\hat s\|/M_0$, the nodal
products, the bisector identity) are therefore pure-number comparisons, and their
residuals near $10^{-16}$ are double-precision round-off, not physical error.

## 7. Worked examples

### Example 1 — build the tensor for a vertical strike-slip

$\phi = 0^\circ$, $\delta = 90^\circ$, $\lambda = 0^\circ$.

From Section 2's geometry, $\sin\delta = 1$, $\cos\delta = 0$,
$\sin\phi = 0$, $\cos\phi = 1$:

$$\hat n = \left(-\sin\delta\sin\phi,\ \sin\delta\cos\phi,\ -\cos\delta\right)
= (0,1,0),$$
$$\hat s = \left(\cos\lambda\cos\phi + \cos\delta\sin\lambda\sin\phi,\
\cos\lambda\sin\phi - \cos\delta\sin\lambda\cos\phi,\ -\sin\lambda\sin\delta\right)
= (1,0,0).$$

Assembling $M = M_0(\hat n\hat s^{\mathsf T} + \hat s\hat n^{\mathsf T})$:

$$M = M_0\begin{pmatrix} 0 & 1 & 0\\ 1 & 0 & 0\\ 0 & 0 & 0\end{pmatrix}.$$

Trace $= 0$ ✔; symmetric ✔. Cross-check with Aki & Richards (1980) eq. 4.88 at
these angles: $M_{xy} = M_0(\sin\delta\cos\lambda\cos2\phi
+ \tfrac12\sin2\delta\sin\lambda\sin2\phi) = M_0$, all other components zero — the
same matrix. The far-field P amplitude is $A(\hat r) = r_x r_y$: largest on the
diagonals, zero in the horizontal coordinate planes and on the vertical.

### Example 2 — the identity, by hand

With $\hat n = (0,1,0)$ and $\hat s = (1,0,0)$, $A = r_x r_y$. Now

$$\hat P = \tfrac{1}{\sqrt2}(1,1,0),\qquad \hat T = \tfrac{1}{\sqrt2}(-1,1,0),$$
$$(\hat r\cdot\hat P)^{2} = \tfrac12(r_x+r_y)^{2},\qquad
(\hat r\cdot\hat T)^{2} = \tfrac12(-r_x+r_y)^{2},$$
$$\tfrac12\left[(\hat r\cdot\hat P)^{2}-(\hat r\cdot\hat T)^{2}\right]
= \tfrac14\left[(r_x+r_y)^{2}-(r_x-r_y)^{2}\right]
= \tfrac14\left[4r_x r_y\right] = r_x r_y = A. ☑$$

### Example 3 — plunge of the compressional axis

For a thrust with dip $\delta\le45^\circ$ the tabulated plunge is
$45^\circ+\delta$. At $\delta = 20^\circ$ that is $65^\circ$; the demo's table
gives $65.00^\circ$. For a normal fault at $\delta = 60^\circ$ the $\hat T$ axis
plunges $75^\circ$ and its $\hat P$ axis plunges $15^\circ$ — which is the
demo's printed $P$ plunge of $-15.0^\circ$ (the sign carrying the up/down
orientation). A near-vertical $\hat T$ axis is the signature of normal faulting,
and here it takes a $60^\circ$ dip to make $\hat T$ distinctly non-vertical.

### Example 4 — no compressional lobe in the horizontal plane for a thrust

For pure dip-slip ($\lambda = \pm90^\circ$), a ray in the horizontal plane
gives, after the algebra carried out in the demo,

$$A_{\text{horizontal}} = -\sin\delta\cos\delta\,\sin^{2}(\text{azimuth}),$$

whose right-hand side is never positive, because $\sin\delta\cos\delta>0$ for
$0<\delta<90^\circ$ and $\sin^2\ge0$. Hence a thrust has **no compressional
horizontal-P lobe**: its compressional energy goes up and down, which is the
quantitative statement behind "thrusts have vertical $P$ axes".

## 8. Python demonstration

[`code/double_couple_demo.py`](code/double_couple_demo.py) performs the checks
above and prints them:

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python double_couple_demo.py
```

- **(a)** $M$ from $(\hat n,\hat s)$ against the closed form for six mechanisms:
  worst difference $2.048\times10^{3}\ \mathrm{N\,m}$ on $10^{19}$-sized
  components, relative agreement $2.05\times10^{-16}$.
- **(b)** The bisector identity on $20\,000$ random directions: maximum
  $|\mathrm{LHS}-\mathrm{RHS}| = 3.331\times10^{-16}$.
- **(c)** The nodal-plane identities $M\hat n = M_0\hat s$ and
  $M\hat s = M_0\hat n$ (worst $2.220\times10^{-16}$), and the measured
  compressional fraction $0.50$ to within sampling error over $400\,000$
  directions.
- **(d)** The first-motion table of Section 4.1, including the vertical-ray
  polarities.
- **(e)** The plunge-versus-dip table of Section 4.2.

The script's own comment notes that the antipodal-same-sign fact "was got wrong
first, which is why it is measured rather than asserted" — a good model for how
to treat every sign in this lesson.

## 9. Exercises

- [`exercises/02-double-couple-exercises.md`](exercises/02-double-couple-exercises.md)
- [`exercises/02-double-couple-solutions.md`](exercises/02-double-couple-solutions.md)

## 10. Real-world applications

- **Focal-mechanism catalogues.** Almost every regional and global catalogue
  reports a double couple from $(\phi,\delta,\lambda)$ or a full six-component
  tensor; the geometry of Section 2 is the reporting format.
- **First-motion polarity inversion.** Networks of up/down readings, as in
  Section 3.5, are inverted for the two nodal planes — the classic method when
  amplitudes are unavailable.
- **Resolving the fault-plane ambiguity.** Aftershock alignment, surface rupture,
  geodetic strain or geological mapping decide which nodal plane is real.
- **Stress-field maps.** $\hat P$ and $\hat T$ axes from many mechanisms give the
  principal-stress directions of a region, used in tectonic and hazard studies.
- **Monitoring.** Source mechanisms of induced events constrain which existing
  faults are being reactivated and how.

## 11. Further reading

- **Aki, K., & Richards, P. G. (1980). *Quantitative Seismology*.** Level:
  graduate textbook. Chapter 4 is the source of the representation theorem and
  the closed-form eq. 4.88 used as an independent check here.
- **Kanamori, H., & Anderson, D. L. (1975). Theoretical basis of some empirical
  relations in seismology.** *Bulletin of the Seismological Society of America*.
  Level: research. Where the double couple is placed in the broader family of
  sources.
- **ObsPy beachball documentation.** Level: reference. The library used by the
  demo for the independent beachball rendering, and the source of the sign trap
  in Section 4.4.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC mechanism has $\phi = 0^\circ$, $\delta = 45^\circ$,
> $\lambda = -90^\circ$ (normal). **(a)** Compute $\hat n$ and $\hat s$. **(b)**
> Write out the six independent components of $M/M_0$. **(c)** Evaluate
> $A(\hat r)$ for a ray going straight up and state the polarity. **(d)** State
> where the two nodal planes are and why their normals are $\hat n$ and $\hat s$.
> **(e)** Compute $\hat P$ and $\hat T$ and state which is vertical. **(f)** A
> colleague reports the mechanism from first motions only and says the fault
> plane is the other nodal plane. Explain why both readings fit the same data and
> name one measurement that would break the tie.

## Common pitfalls

1. **Getting the slip-vector sign backwards.** Reversing $\hat s$ alone swaps
   $P$ and $T$. Always state the convention (here: hanging-wall motion) before
   writing a tensor.
2. **Reading a normal fault as compression above the source.** It is
   dilatational; the vertical axis is $\hat T$, not $\hat P$.
3. **Calling a nodal plane "the fault plane" without evidence.** First motions
   cannot decide it.
4. **Assuming $P$ and $T$ axes are the fault or auxiliary planes.** They are
   bisectors.
5. **Treating "vertical axis" as an identity.** It holds exactly only at
   $45^\circ$ dip.
6. **Comparing against a library's axis labels without checking its slip-sign
   convention.** The demo shows obspy's labels are the mirror image of the
   convention used here.

## Related modules

- [01 Faulting, Slip and the Elastic Rebound Cycle](01-faulting-and-slip.md) —
  where slip, area and $M_0$ come from.
- [03 Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) —
  the general tensor, of which the double couple is one special point.
- [04 Source Time Functions, Rupture Kinematics and Directivity](04-source-time-function.md) —
  what a finite, propagating source does to this pattern.
- [07 Discriminating Explosions from Earthquakes](07-nuclear-explosion-sources.md) —
  the isotropic source that completes the polarity story.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  how mechanisms are estimated in practice.
