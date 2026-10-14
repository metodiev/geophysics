---
id: 02-02-07
title: "Central Forces, Orbits and the Earth-Moon-Sun System"
level: advanced
prereqs: ["02-02-06", "02-02-04"]
estimated_minutes: 90
tags: [central-forces, kepler, orbits, shell-theorem, satellite-geodesy, tides]
---

# Central Forces, Orbits and the Earth-Moon-Sun System

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** conservation of angular momentum for a central force, and from it
   both the planarity of the orbit and Kepler's second law.
2. **Use** the effective potential to locate circular orbits and to state their
   stability condition.
3. **State** Newton's shell theorem precisely, distinguish it from the field of a
   point source at depth, and verify the distinction numerically.
4. **Derive** the orbit equation $r(\theta)$, Kepler's third law and the vis-viva
   relation, and check each against a numerical orbit.
5. **Invert** Kepler's third law to obtain $GM$ from a satellite's period and
   semi-major axis, with the sensitivity of the result to each measurement.
6. **Explain** the Earth–Moon system as a two-body problem, and identify which
   parts of the tidal-recession story are modelled and which are measured.

## Prerequisites

- [02-02-06 Lagrangian and Hamiltonian Formulations](./06-lagrangian.md) — the
  effective potential, which is the shortest route to circular orbits.
- [02-02-04 Momentum, Impulse and Collisions](./04-momentum.md) — the reduced
  mass and centre-of-mass reduction for two bodies.

## 1. Intuition: one force law, an entire solar system

Newton's inverse-square law is a single sentence, and from it follow the shapes of
planetary orbits, the periods of satellites, the tides, the receding Moon and the
precession of the Earth. The reason so much comes from so little is that a central
inverse-square force has **two** conserved quantities (energy and angular
momentum) in a three-dimensional problem — enough to reduce the motion to
quadrature, and in fact enough to give a closed-form orbit.

For geophysics, the applications are concrete:

| Application | The central-force content |
|---|---|
| GNSS, GRACE, altimetry orbits | circular and near-circular orbit speed and period; $GM$ from tracking |
| the geoid and the gravity field | the exterior potential of a nearly spherical body |
| tides | the *gradient* of the Moon's and Sun's fields across the Earth |
| lunar recession and LOD | two-body angular momentum exchange (lesson 04) |
| Earth's precession | solar and lunar torques on the equatorial bulge (lesson 08) |

And one warning that must come early, because it is a common and consequential
error: **the exterior field of a spherically symmetric body is $GM/z^{2}$ with $z$
the distance to its centre (shell theorem); the field of a *point* mass at depth
$d$ observed at horizontal offset $\rho$ is $GMd/(\rho^{2}+d^{2})^{3/2}$.** These
are different formulas, they describe different geometries, and both are
dimensionally consistent, so no unit check will separate them. Section 3.3
verifies the first by direct quadrature and states when each applies.

## 2. Precise definitions

### 2.1 Central force and its conserved quantities

A **central force** is one directed along the line joining the body to a fixed
centre: $\mathbf{F} = F(r)\hat{\mathbf{r}}$. For such a force the torque about the
centre vanishes identically,

$$\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}
= \mathbf{r}\times F(r)\hat{\mathbf{r}} = \mathbf{0},$$

so (by $\boldsymbol{\tau} = d\mathbf{L}/dt$) the angular momentum $\mathbf{L}$ is
constant. Since $\mathbf{L}$ is perpendicular to the plane spanned by
$\mathbf{r}$ and $\mathbf{v}$, the motion is **planar**.

### 2.2 Areal velocity

With $\mathbf{L} = \mathbf{r}\times m\mathbf{v}$, the rate at which the radius
vector sweeps area is

$$\frac{dA}{dt} = \tfrac12|\mathbf{r}\times\mathbf{v}|
= \frac{L}{2m} = \text{constant}.$$

This is Kepler's second law, and its content is the constancy of angular
momentum — not anything specifically gravitational. Any central force gives it.

### 2.3 Effective potential and orbit elements

For a body of mass $m$ and angular momentum $L$ in a field $-GMm/r$ (with
$U\to0$ at infinity), the radial motion is governed by the **effective
potential**

$$V_{\text{eff}}(r) = \frac{L^{2}}{2mr^{2}} - \frac{GMm}{r},$$

so that the radial kinetic energy is
$\tfrac12m\dot r^{2} = E - V_{\text{eff}}(r)$. The two terms are the centrifugal
barrier and the attraction; their competition locates the circular orbit and
classifies the motion.

The classical **orbit elements** are the semi-major axis $a$, eccentricity $e$,
inclination $i$, longitude of the ascending node $\Omega$, argument of periapsis
$\omega$ and true anomaly $\nu$; the first two fix the size and shape, the last
four the orientation and phase. For a Keplerian orbit,

$$r(\theta) = \frac{p}{1+e\cos\theta}, \qquad
p = a(1-e^{2}) = \frac{L^{2}}{GMm^{2}},$$

with $e = 0$ circular, $0<e<1$ elliptical, $e = 1$ parabolic and $e>1$
hyperbolic.

### 2.4 Specific quantities

Dividing by the mass makes everything independent of the body's mass — the
standard practice in celestial mechanics:

$$\mu = GM\ \ (\mathrm{m^{3}\,s^{-2}}), \qquad
\varepsilon = \tfrac12v^{2} - \frac{\mu}{r}\ \ (\mathrm{m^{2}\,s^{-2}}), \qquad
h = \frac{L}{m}\ \ (\mathrm{m^{2}\,s^{-1}}).$$

## 3. Step-by-step derivations

### 3.1 Planarity and Kepler's second law

From §2.1, $\mathbf{L}$ is constant and $\mathbf{r}\cdot\mathbf{L} = 0$, so the
position vector always lies in the plane perpendicular to the fixed vector
$\mathbf{L}$: the orbit is planar. Writing the position in polar coordinates in
that plane,

$$\mathbf{L} = m r^{2}\dot\theta\,\hat{\mathbf{z}}
\;\Longrightarrow\;
L = mr^{2}\dot\theta = \text{constant},
\;\Longrightarrow\;
\frac{dA}{dt} = \tfrac12r^{2}\dot\theta = \frac{L}{2m}.$$

Numerically, for $a = 10^{7}$ m, $e = 0.5$ and $GM = 3.986\,004\,418\times10^{14}$
m³ s⁻², the demonstration integrates one orbit and measures the areal rate at four
points spanning the orbit: $2.7338175293\times10^{10}$ m² s⁻¹ at every one, with a
spread of $6.1\times10^{-15}$ across the whole orbit. The demonstration's update
order (velocity before position) makes the scheme symplectic Euler, which
conserves angular momentum for a central force as an algebraic identity — so the
spread is round-off, and reversing the update order would make it grow linearly in
time. That is a *numerical* statement about the integrator, not a physical one
about the orbit.

### 3.2 Circular orbits from the effective potential, and their stability

A circular orbit is an extremum of $V_{\text{eff}}$:

$$\frac{dV_{\text{eff}}}{dr} = -\frac{L^{2}}{mr^{3}} + \frac{GMm}{r^{2}} = 0
\;\Longrightarrow\;
L^{2} = GMm^{2}r,$$

which, with $L = mvr$, gives $v^{2} = GM/r$ — the same equation as the
centripetal force balance $v^{2}/r = GM/r^{2}$. Two routes, one result.

**Stability.** The second derivative at the extremum is positive:

$$\frac{d^{2}V_{\text{eff}}}{dr^{2}} = \frac{3L^{2}}{mr^{4}} - \frac{2GMm}{r^{3}}
= \frac{GMm}{r^{3}} > 0,$$

so the circular orbit is a *minimum* and small radial perturbations oscillate
about it. The oscillation frequency is

$$\omega_r = \sqrt{\frac{V_{\text{eff}}''(r)}{m}} = \sqrt{\frac{GM}{r^{3}}}
= \omega_{\text{orbit}},$$

a coincidence special to the inverse-square law: radial and orbital frequencies
are equal, which is why a perturbed circular orbit is a closed ellipse
(Bertrand's theorem) rather than a precessing rosette. Every departure from
$1/r^{2}$ — the $J_2$ oblateness term, the Moon, the Sun — breaks the degeneracy
and produces precession.

The demonstration tabulates circular orbits using $\mu = GM$:

| Altitude | $r$ (m) | $v$ (m/s) | $T$ (s) | $T$ (min) | specific energy (J kg⁻¹) |
|---|---|---|---|---|---|
| 500 km | $6.8710\times10^{6}$ | 7616.5608 | 5668.144 | 94.47 | $-2.9006\times10^{7}$ |
| 800 km | $7.1710\times10^{6}$ | 7455.5387 | 6043.389 | 100.72 | $-2.7793\times10^{7}$ |
| 20 200 km | $2.6571\times10^{7}$ | 3873.1555 | 43 104.522 | 718.41 | $-7.5007\times10^{6}$ |

A 500 km orbit is a low-Earth-orbit geodesy or altimetry orbit; 20 200 km is
close to the semi-synchronous navigation-shell altitude. Both numbers follow from
$\mu$ alone, which is why orbital altitudes are quoted with the mission's
navigation requirements attached.

### 3.3 The shell theorem — and the formula it is often confused with

**Newton's shell theorem.** For a spherically symmetric mass distribution:

1. the external field is the same as if all the mass were at the centre:
   $g = GM/z^{2}$ with $z$ the distance to the *centre*;
2. the field *inside* a uniform spherical shell is zero.

The demonstration verifies both by direct surface quadrature of Newton's law,
with a unit-radius shell of unit surface density $(M = 4\pi)$, so $GM/R^{2} = 4\pi
\approx 12.566$:

| $z$ (from the centre) | $g_z$ from quadrature | $GM/z^{2}$ | relative difference |
|---|---|---|---|
| 1.05 | 11.40457607 | 11.39806858 | $5.709\times10^{-4}$ |
| 1.50 | 5.58512079 | 5.58505361 | $1.203\times10^{-5}$ |
| 3.00 | 1.39626845 | 1.39626340 | $3.614\times10^{-6}$ |
| 10.00 | 0.12566404 | 0.12566371 | $2.649\times10^{-6}$ |

and **inside** ($z = 0.00$, 0.30, 0.70), the quadrature gives
$-1.0\times10^{-16}$, $-2.3\times10^{-5}$ and $-1.7\times10^{-4}$ — i.e.
$<1.4\times10^{-5}$ of the shell's characteristic field $GM/R^{2}$. The residual
is quadrature error, not physics, and it is instructive to measure it: refining
$n$ by a factor of 4 reduces both the near-shell exterior error
($5.709\times10^{-4} \to 3.546\times10^{-5} \to 2.215\times10^{-6}$) and the
interior near-shell error ($1.597\times10^{-2} \to 8.115\times10^{-4}
\to 5.023\times10^{-5}$) by about 16 each time, i.e. as $n^{-2}$.

**The formula it is confused with.** A point mass $M$ at depth $d$, observed at
horizontal offset $\rho$ from the point directly above it, produces

$$g_z = \frac{GMd}{(\rho^{2}+d^{2})^{3/2}},$$

directly downward. This is the standard anomaly profile of a compact body — a
buried sphere *approximated* as a point, a small intrusion, an ore body. The two
formulas agree only in the limit where the body is small compared with its depth
($a \ll d$) *and* the observation is within a few body-radii; and they disagree by
a factor that grows as $(\rho/d)$ grows.

**Which is which, in one table:**

| Geometry | Field | Where it is used |
|---|---|---|
| point mass at depth $d$, offset $\rho$ | $GMd/(\rho^{2}+d^{2})^{3/2}$ | anomaly profile of a compact body; a *model* for a small source |
| uniform sphere of radius $a$, external point at $z \ge a$ | $GM/z^{2}$ | the shell theorem; a planet's exterior field; satellite dynamics |
| uniform ball, *internal* point at $z < a$ | $GMz/a^{3}$ (linear in $z$) | the interior field; depth-varying gravity |
| spherical shell, internal point | 0 | why the interior of a hollow shell is field-free |

The third row is worth knowing too: it is derived in
[01-06-08](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md),
and it is the reason a borehole gravimeter measures a field that *decreases* with
depth inside a uniform body while the layered-Earth field increases.

### 3.4 The orbit equation, Kepler's third law and vis-viva

**Orbit equation.** Eliminating time in favour of $\theta$ (or applying the Binet
formula) gives the differential equation

$$\frac{d^{2}u}{d\theta^{2}} + u = \frac{GMm^{2}}{L^{2}}, \qquad u = \frac1r,$$

whose solution is

$$u = \frac{GMm^{2}}{L^{2}}\left(1 + e\cos(\theta-\theta_0)\right)
\;\Longrightarrow\;
r(\theta) = \frac{p}{1+e\cos\theta}, \qquad
p = \frac{L^{2}}{GMm^{2}},$$

the conic sections — Kepler's first law. The eccentricity is set by the initial
energy and angular momentum:
$e = \sqrt{1 + 2\varepsilon h^{2}/(\mu^{2})}$ in specific variables.

**Kepler's third law.** For an ellipse the area is $\pi ab$ and the areal rate is
$h/2$, so the period is $T = 2\pi ab/h$. Substituting $b = a\sqrt{1-e^{2}}$ and
$h^{2} = \mu a(1-e^{2})$ gives

$$T^{2} = \frac{4\pi^{2}}{\mu}a^{3}.$$

The demonstration evaluates $T^{2}/a^{3}$ for three very different orbits
($a = 7000$, 20 000 and 42 164 km) and obtains $9.904258\times10^{-14}$ s² m⁻³ in
all three cases, matching $4\pi^{2}/GM = 9.904258\times10^{-14}$ s² m⁻³ exactly as
printed. The constancy across three orders of magnitude of $a$ is the law.

**Vis-viva.** Combining energy conservation with the orbit geometry gives

$$v^{2} = \mu\left(\frac{2}{r} - \frac{1}{a}\right),$$

which reduces to $v^{2} = \mu/a$ for a circular orbit ($r = a$) and gives the
maximum speed at periapsis and minimum at apoapsis. The demonstration's
circular-orbit column is exactly this, and its numerical orbit satisfies
$h^{2} = \mu a(1-e^{2})$ to a relative difference of $6.5\times10^{-15}$ —
an independent check that the integrated trajectory is a Kepler ellipse and not
some other curve consistent with the equations.

### 3.5 Inverting Kepler's third law: measuring $GM$ from a satellite

$$GM = \frac{4\pi^{2}a^{3}}{T^{2}}
\;\Longrightarrow\;
\frac{\delta(GM)}{GM} = 3\,\frac{\delta a}{a} - 2\,\frac{\delta T}{T}.$$

This is the operational formula of satellite geodesy, and the sensitivities are
worth stating numerically. For the 500 km orbit above:

- a **1 m** error in $a = 6.8710\times10^{6}$ m gives
  $3\times1.456\times10^{-7} = 4.4\times10^{-7}$ relative;
- a **1 ms** error in $T = 5668.144$ s gives
  $2\times1.76\times10^{-7} = 3.5\times10^{-7}$ relative.

So metre-level orbit determination and millisecond timing give $GM$ to a few parts
in $10^{7}$ from a single pass; averaging over many satellites and years reaches
the defining precision of the WGS 84 value quoted in the constant handbook
($GM_\oplus = 3.986\,004\,418\times10^{14}$ m³ s⁻², defining). Note what is *not*
needed: $G$. This is why $GM_\oplus$ is known to nine digits while the Earth's
mass, obtained as $GM_\oplus/G$, is limited to about five by the $2.2\times10^{-5}$
relative uncertainty in $G$. **Never divide $GM$ by $G$ unless you must.**

### 3.6 The Earth–Moon system as a two-body problem

Two bodies attract with equal and opposite forces, so their centre of mass
(the barycentre) moves uniformly while each body orbits it. With $\mu =
G(M_\oplus + M_{\text{Moon}})$ and relative separation $r$, the relative motion
obeys the same one-body equation as before. The reduction is exact for point
masses; the only approximation is treating each body as a point, which the shell
theorem licenses *provided* both are spherically symmetric — the Earth's
oblateness is a small perturbation ($J_2$ of order $10^{-3}$), and it is the
perturbation that causes the Moon's orbit to precess and the Earth to precess.

Three features of this system matter here:

1. **The barycentre lies inside the Earth** — a statement about the mass ratio,
   and the reason "the Moon orbits the Earth" is a convenient fiction. The
   correct statement is that both orbit the barycentre.
2. **Tidal evolution exchanges angular momentum between spin and orbit.** The
   Moon raises a tide on the rotating Earth; friction delays the tidal bulge
   relative to the Earth–Moon line; the delayed bulge torques the Moon, and the
   reaction torque slows the Earth. Angular momentum is conserved for the pair
   ([02-01-04](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) §3.4)
   while energy is dissipated as heat, and the *orbital* energy grows only by the
   small fraction $n/\omega$ of the released energy
   ([02-02-03](./03-work-energy.md) §3.5).
3. **The rates are measured, not modelled here.** The secular increase in the
   length of day and the recession of the Moon are determined from
   Earth-orientation series and lunar laser ranging; the values change as the
   series are reprocessed. Take them from IERS (<https://www.iers.org>) rather
   than from any textbook, including this one.

The same two-body machinery describes the Sun–Earth pair (with $\mu =
G(M_\odot + M_\oplus)$, again requiring a solar $GM$ from the literature), and
the perturbation of the Earth's orbit by the other planets — which is the
subject of celestial mechanics proper and the reason long-term palaeoclimate
calculations need numerical ephemerides.

## 4. Physical interpretation

### 4.1 What the two conserved quantities buy

Energy and angular momentum (plus the direction of $\mathbf{L}$) reduce six phase
variables to one quadrature. That is why the two-body problem has a closed-form
solution, and why every perturbation theory in celestial mechanics is built on it.
In specific variables:

$$h^{2} = \mu a(1-e^{2}), \qquad
\varepsilon = -\frac{\mu}{2a}, \qquad
T^{2} = \frac{4\pi^{2}}{\mu}a^{3},$$

three relations, any two of which determine the orbit's size and shape. Note that
$\varepsilon$ depends only on $a$ — the eccentricity does not affect the orbital
energy, which is why a family of ellipses with the same $a$ but different $e$ all
have the same period.

### 4.2 What breaks the Kepler problem, in order of size

| Perturbation | Relative size | Observable consequence |
|---|---|---|
| Earth's oblateness $J_2 \sim 10^{-3}$ | large | nodal and apsidal precession of LEO satellites; sun-synchronous orbits |
| atmospheric drag below ~600 km | grows with time | orbit decay; the reason LEO geodesy satellites fly at 400–500 km with drag models |
| solar and lunar third-body attraction | $10^{-5}$–$10^{-6}$ in LEO, larger for higher orbits | resonance and long-period perturbations |
| solar radiation pressure | area/mass dependent | significant for a satellite with large solar panels |
| general relativity | $v^{2}/c^{2} \sim 10^{-8}$ in LEO | measurable for Mercury; frame dragging measured by dedicated missions |

The lesson's Kepler results are therefore the *zeroth-order* description, exact for
point masses in mutual attraction, and the first three rows are the reason orbit
determination software exists.

### 4.3 Tides are the gradient of a central force

The Moon's *field* accelerates the Earth's centre of mass; what deforms the Earth
is the difference between the field at the centre and the field elsewhere — the
**tidal** field, which is the gradient of the potential and falls as $1/r^{3}$.
That single statement explains why the tides are semi-diurnal (two bulges, one
towards and one away from the Moon), why the solar tide is smaller than the
lunar (about half, from the mass-distance combination in $m/d^{3}$), and why the
tidal torque has the sign it does. The tidal potential is treated with spherical
harmonics in
[02-08-03](../08-potential-theory/03-spherical-harmonics.md), and the deformation
response — the Love numbers — in
[02-04-07](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md).

## 5. Assumptions and regime of validity

1. **Point masses, or spherical symmetry.** Justified by the shell theorem, and
   violated by the Earth's oblateness at the $10^{-3}$ level — larger than any
   geodetic signal, so it must be modelled. **This is where the shell theorem's
   applicability must be checked rather than assumed.**
2. **Two bodies only.** A third body's perturbation is comparable to $J_2$ for
   high orbits; for the Moon, the Sun's perturbation is the dominant one after
   the Earth's.
3. **Instantaneous action at a distance.** Adequate at $v/c \sim 10^{-4}$ for the
   Earth's orbital motion (the Earth moves at about 30 km/s);
   $v^{2}/c^{2} \sim 10^{-8}$, which is the size of the relativistic corrections
   that precess Mercury's orbit by arcseconds per century.
4. **Vacuum.** Drag is negligible above a few thousand kilometres, decisive below
   600 km.
5. **One-body reduction assumes a fixed centre.** A fixed point-mass centre is an
   excellent approximation for a satellite, and a bad one for the Earth–Moon
   system — where the barycentre must be used.
6. **Kepler's third law in the form $T^{2} = 4\pi^{2}a^{3}/\mu$ uses the *relative*
   orbit's $a$ and the *total* mass $\mu = G(m_1+m_2)$.** Using $GM_\oplus$ for
   the Earth–Moon system, or a body's centre-of-mass distance instead of the
   relative separation, are both common and both wrong by known factors.
7. **The potential is $1/r$ only outside the body.** Inside, the field is linear
   in $r$ for a uniform body (§3.3, third row) — a completely different regime.
8. **Secular rates are measured quantities** with uncertainties and long
   correlation times; no derivation in this lesson supplies them.

## 6. Units and dimensional analysis

| Quantity | Unit | Note |
|---|---|---|
| $\mu = GM$ | m³ s⁻² | the fundamental orbital parameter; never split into $G$ and $M$ unnecessarily |
| specific energy $\varepsilon$ | m² s⁻² | equals $-\mu/(2a)$ for a bound orbit |
| specific angular momentum $h$ | m² s⁻¹ | equals $r^{2}\dot\theta$ |
| $T^{2}/a^{3}$ | s² m⁻³ | equals $4\pi^{2}/\mu$: the demonstration's $9.904258\times10^{-14}$ |
| $G$ | m³ kg⁻¹ s⁻² | needed only when converting to a mass |

Useful checks: $T^{2}/a^{3}$ must equal $4\pi^{2}/\mu$ *whatever* the orbit, so a
computed value differing between two orbits is a bug, not physics;
$h^{2} = \mu a(1-e^{2})$ must hold for any numerical orbit; and
$\varepsilon = -\mu/(2a)$ must come out negative for a bound trajectory, with
$\varepsilon = 0$ at the parabolic boundary. Each of these is a *dimensionally
legal* relation that can nonetheless be wrong by a factor of 2 — which is why
each is checked numerically in the demonstration rather than asserted.

## 7. Python demonstration

The script (a) verifies both halves of the shell theorem by direct quadrature on a
spherical shell, with a measured convergence study and an explicit statement of
the geometry each formula assumes; (b) tabulates circular orbits at three
altitudes; (c) integrates an eccentric orbit and measures the constancy of the
areal rate; (d) checks $h^{2} = \mu a(1-e^{2})$; and (e) evaluates $T^{2}/a^{3}$
for three orbits against $4\pi^{2}/GM$.

Full listing: [`code/central_forces_demo.py`](./code/central_forces_demo.py).

The shell quadrature, which uses nothing but Newton's law and therefore tests the
theorem rather than assuming it:

```python
def shell_field_z(z, radius, n_theta=400, n_phi=800):
    """Exterior (or interior) axial field of a unit-surface-density shell."""
    dth = math.pi / n_theta
    dph = 2 * math.pi / n_phi
    total = 0.0
    for i in range(n_theta):
        th = (i + 0.5) * dth
        st, ct = math.sin(th), math.cos(th)
        d = math.sqrt(z * z + radius * radius - 2 * z * radius * ct)
        total += (z - radius * ct) / d ** 3 * st * dth
    return total * 2 * math.pi * radius * radius
```

Observed output (Python 3.14.4, standard library only):

```text
{{OUT:out/m02-central_forces.txt}}
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| exterior quadrature reproduces $GM/z^{2}$ (e.g. 5.58512079 against 5.58505361 at $z = 1.5$) | the shell theorem is exact; the residual is quadrature error, which falls as $n^{-2}$ |
| interior values are $<1.4\times10^{-5}$ of $GM/R^{2}$ and shrink with refinement | the interior field of a shell really is zero |
| the shell and point-mass profiles are listed as *different formulas with different geometries* | the model must be checked, not just the dimensions |
| 500 km orbit: 7616.5608 m/s, period 5668.144 s = 94.47 min | one parameter $\mu$ plus one altitude fixes the whole orbit |
| areal rate spread over a full eccentric orbit: $6.1\times10^{-15}$ | angular momentum conservation is an identity for a central force |
| $T^{2}/a^{3} = 9.904258\times10^{-14}$ s² m⁻³ for $a$ spanning 7 000–42 164 km | Kepler's third law, with the constant equal to $4\pi^{2}/GM$ |
| $h^{2}$ and $\mu a(1-e^{2})$ agree to $6.5\times10^{-15}$ relative | the integrated orbit is a Kepler ellipse |

> **Breaking exercise.** In §3 of the script change the launch velocity to
> $1.2v_{\text{circ}}$ and predict, before running, whether the orbit is an
> ellipse with larger $a$ or an escape. Then verify with the sign of
> $\varepsilon$: escaping requires $v \ge \sqrt{2}v_{\text{circ}} = 1.414v_{\text{circ}}$,
> so $1.2v_{\text{circ}}$ must remain bound with $a$ larger by a factor given by
> vis-viva.

## 8. Common mistakes

1. **Using the point-mass offset profile $GMd/(\rho^{2}+d^{2})^{3/2}$ for a
   spherically symmetric body (or $GM/z^{2}$ for a compact source at depth).**
   Both are dimensionally correct and physically different; check the geometry,
   then check which limit your observation satisfies. (Section 3.3.)
2. **Dividing $GM$ by $G$ unnecessarily.** It imports $G$'s $2.2\times10^{-5}$
   relative uncertainty into a quantity known to $10^{-9}$.
3. **Using the body's radius instead of the orbital radius.** The altitude is
   above the surface; $r = R_\oplus + h$.
4. **Forgetting the total mass in the two-body $\mu$.** For the Earth–Moon system
   the correction is the mass ratio, and for equal masses it is a factor of 2.
5. **Treating a circular orbit as "the" orbit.** Any energy between the circular
   value and the escape value gives an ellipse of some eccentricity.
6. **Assuming the areal rate constancy proves anything physical about the
   integrator.** A symplectic scheme conserves it identically; the test of the
   *physics* is that the orbit closes, which needs $V_{\text{eff}}''$ and the
   inverse-square degeneracy of §3.2.
7. **Ignoring $J_2$ because the Earth "is nearly spherical".** At $10^{-3}$ it is
   bigger than most orbit-determination residuals and it is what makes
   sun-synchronous orbits possible.
8. **Quoting a tidal recession rate from memory.** It is a measured, revised
   quantity; use IERS and the current lunar-laser-ranging literature.

## 9. Real-world applications

1. **GNSS constellation design.** Circular orbits in specific shells; the period
   and speed come from $\mu$ alone, and the repeat geometry from the Earth's
   rotation ([07-gravity-geodesy](../../07-gravity-geodesy/README.md)).
2. **Satellite gravimetry.** A pair of satellites in a low orbit measures the
   *variation* of $GM$ in space and time — the perturbations of §4.2 are the
   signal, not the noise, once the known ones are removed.
3. **Altimetry.** The orbit is the datum; a radial orbit error of 1 cm is a 1 cm
   sea-surface error, which is why the sensitivity arithmetic of §3.5 is
   operational.
4. **Tidal prediction.** The tide-generating potential is a gradient of the
   central field, expanded in spherical harmonics; the harmonic amplitudes are
   what tide tables tabulate.
5. **Palaeoclimate and astronomical forcing.** Milanković forcing is the
   perturbation of the Earth's orbit and rotation, computed with the same
   elements and long numerical ephemerides.
6. **Planetary and lunar science.** $I/(MR^{2})$, $J_2$ and the orbit elements of a
   flyby are what a mission measures; all are central-force quantities.
7. **Space debris.** Atmospheric drag in the $1/r$ field gives the decay rate,
   which is the operational input for collision avoidance.

## 10. Further reading

- **Goldstein, H., Poole, C. P., & Safko, J. *Classical Mechanics* (3rd ed.).**
  Chapter 3: the two-body problem, the orbit equation, Kepler's laws and the
  virial relations — everything in §3.4, with the algebra done slowly.
  Level: advanced to graduate.
- **Landau, L. D., & Lifshitz, E. M. *Mechanics* (3rd ed.).** §14–15: the Kepler
  problem by the effective-potential route of §3.2, and the classification of
  orbits by energy. Level: graduate.
- **Murray, C. D., & Dermott, S. F. *Solar System Dynamics.*** The perturbation
  theory that §4.2 only lists, including $J_2$, third-body and resonance effects.
  Level: graduate.
- **Vallado, D. A. *Fundamentals of Astrodynamics and Applications* (4th ed.).**
  The operational version: orbit elements, $J_2$ effects, perturbations and
  determination. Level: advanced to graduate.
- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy.*** The exterior
  potential, spherical harmonics and the relation between $GM$ and the geoid.
  Level: graduate.
- **Lambeck, K. *The Earth's Variable Rotation.*** Tidal friction and the
  Earth–Moon angular-momentum exchange, with the measured rates. Level: graduate.
- **IERS, *IERS Conventions* (current edition).** The authoritative source for the
  Earth-orientation and tidal parameters referenced in §3.6. <https://www.iers.org>
  (level: reference).

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-02-06 Lagrangian and Hamiltonian Formulations](./06-lagrangian.md) — the
  effective potential used in §3.2, and the reason symplectic integrators matter.
- [02-02-08 Rigid-Body Dynamics, Precession and the Earth's Rotation](./08-rigid-body.md) —
  what the solar and lunar torques do to a non-spherical Earth.
- [02-02-04 Momentum, Impulse and Collisions](./04-momentum.md) — the two-body
  reduction and reduced mass.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  the angular-momentum accounting of the Earth–Moon system.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md) —
  the interior linear field, and the non-uniqueness that the shell theorem implies.
- [02-08-03 Spherical Harmonics and Multipole Expansions](../08-potential-theory/03-spherical-harmonics.md) —
  how $J_2$ and the higher moments of the real, non-spherical Earth are described.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the discipline that
  measures $\mu$, $J_2$ and the geoid.

## Exercises

Attempt the graded problems in
[`exercises/07-central-forces-exercises.md`](./exercises/07-central-forces-exercises.md),
then compare with
[`exercises/07-central-forces-solutions.md`](./exercises/07-central-forces-solutions.md).

## Self-assessment checklist

- [ ] I can derive planarity and Kepler's second law from the vanishing torque.
      (Section 3.1)
- [ ] I can locate circular orbits two ways and state the stability condition.
      (Section 3.2)
- [ ] I can state the shell theorem, give the point-mass offset profile, and say
      which geometry each describes. (Section 3.3)
- [ ] I can derive the orbit equation and Kepler's third law, and check them on a
      numerical orbit. (Section 3.4)
- [ ] I can invert $T^{2} = 4\pi^{2}a^{3}/GM$ and state the sensitivity of $GM$ to
      errors in $a$ and $T$. (Section 3.5)
- [ ] I can explain why $GM$ is known far better than the Earth's mass, and avoid
      dividing by $G$ unnecessarily. (Section 3.5)
- [ ] I can list the perturbations to a Keplerian orbit in order of size and say
      which one dominates in low-Earth orbit. (Section 4.2)
- [ ] I can explain the tide as the gradient of the central force, and say which
      parts of the tidal story are measured rather than modelled. (Sections 3.6,
      4.3)
