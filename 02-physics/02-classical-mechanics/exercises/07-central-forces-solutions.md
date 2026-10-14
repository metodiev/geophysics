# Solutions — 02-02-07 Central Forces, Orbits and the Earth-Moon-Sun System

> **Read this after attempting the exercises, not before.**
>
> All arithmetic was computed with $\mu = GM_\oplus
> = 3.986\,004\,418\times10^{14}$ m³ s⁻² and $R = 6\,371$ km.

---

## ★1 — Central-force conservation laws

**(a)** $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}
= \mathbf{r}\times F(r)\hat{\mathbf{r}} = \mathbf{0}$, because $\mathbf{r}$ and
$\hat{\mathbf{r}}$ are parallel.

**(b)** Since $d\mathbf{L}/dt = \boldsymbol{\tau} = \mathbf{0}$, $\mathbf{L}$ is a
constant vector. And $\mathbf{r}\cdot\mathbf{L} = 0$ always (the cross product is
perpendicular to $\mathbf{r}$), so $\mathbf{r}$ always lies in the fixed plane
normal to $\mathbf{L}$: the motion is planar.

**(c)** The areal rate is $dA/dt = \tfrac12|\mathbf{r}\times\mathbf{v}|
= |\mathbf{L}|/(2m)$, constant. This is Kepler's second law and it holds for *any*
central force, not just gravity.

---

## ★2 — A 400 km orbit

**(a)** $r = 6\,371\,000 + 400\,000 = 6\,771\,000$ m.

$$v = \sqrt{\frac{\mu}{r}} = 7\,672.60\ \mathrm{m\,s^{-1}}, \qquad
T = 2\pi\sqrt{\frac{r^{3}}{\mu}} = 5\,544.86\ \mathrm{s} = \mathbf{1.5402\ h}
\;(92.4\ \mathrm{min}).$$

**(b)** $\varepsilon = -\mu/(2a) = -3.986\,004\,418\times10^{14}/(2\times6.771\times10^{6})
= \mathbf{-2.9435\times10^{7}\ J\,kg^{-1}}$.

**(c)** Negative energy ⇒ **bound** (elliptical; here circular). The orbit decays
only through atmospheric drag, which is exactly why 400 km is the altitude used by
geodesy missions that can be tracked precisely: low enough to sense gravity, high
enough that drag is manageable.

---

## ★3 — Kepler's third law

**(a)** $T^{2} = \dfrac{4\pi^{2}}{\mu}a^{3}$.

**(b)** $a = 2.66\times10^{7}$ m:
$T = 2\pi\sqrt{(2.66\times10^{7})^{3}/3.986\,004\,418\times10^{14}}
= \mathbf{5.9581\times10^{4}\ s} = 16.55$ h.

**(c)** $T^{2}/a^{3}$: for the 26 600 km orbit,
$(5.9581\times10^{4})^{2}/(2.66\times10^{7})^{3} = 9.904258\times10^{-14}$;
for the 400 km orbit at $a = 6.771\times10^{6}$ m,
$(5544.86)^{2}/(6.771\times10^{6})^{3} = 9.904258\times10^{-14}$. And
$4\pi^{2}/\mu = 4\pi^{2}/3.986\,004\,418\times10^{14}
= 9.904258\times10^{-14}$ s² m⁻³. **All three agree**, and they must: the constant
does not depend on the orbit.

---

## ★4 — Vis-viva

**(a)** $v^{2} = \mu\left(\dfrac{2}{r} - \dfrac{1}{a}\right)$.

**(b)** $r_p = a(1-e) = 7.0\times10^{6}$ m, $r_a = 1.3\times10^{7}$ m:
$$v_p = \sqrt{\mu\left(\frac{2}{r_p}-\frac{1}{a}\right)}
= 8603.82\ \mathrm{m\,s^{-1}}, \qquad
v_a = \sqrt{\mu\left(\frac{2}{r_a}-\frac{1}{a}\right)}
= 4632.83\ \mathrm{m\,s^{-1}}.$$

**(c)** $v_p/v_a = 1.8571$. From the geometry, angular momentum conservation gives
$r_pv_p = r_av_a$, so the ratio is $r_a/r_p = 1.3/0.7 = \mathbf{1.8571}$ ✓. This
is the cleanest statement of what an eccentric orbit does: it moves faster where
it is closer, in exactly the inverse ratio of the distances.

---

## ★★5 — Measuring $GM$ from an orbit

**(a)** $GM = \dfrac{4\pi^{2}a^{3}}{T^{2}}$.

**(b)** With $a = 2.66\times10^{7}$ m and $T = 5.9581\times10^{4}$ s:
$GM = 3.986\,004\,418\times10^{14}$ m³ s⁻² to all printed digits — this is exactly
how the defined value is realised in practice (from many satellites, over many
years, with full perturbation models).

**(c)** $\dfrac{\delta(GM)}{GM} = 3\dfrac{\delta a}{a} - 2\dfrac{\delta T}{T}$:

- 1 m in $a$: $3\times(1/2.66\times10^{7}) = \mathbf{1.13\times10^{-7}}$;
- 1 ms in $T$: $2\times(10^{-3}/5.9581\times10^{4})
  = \mathbf{3.4\times10^{-8}}$.

Both are of order $10^{-7}$, so metre-level ranging and millisecond timing give
$GM$ to seven digits **from one satellite**, and averaging over a constellation
over years reaches the nine digits of the defining value.

**(d)** Because the orbit measures $GM$ **directly** — no mass and no gravitational
constant appear separately. Dividing by $G$ to obtain the mass imports
$G$'s relative uncertainty of $2.2\times10^{-5}$, four hundred times worse than
the measurement of $GM$ itself, and limits the mass to about five significant
figures. That is the sense in which $GM_\oplus$ is "known better than the Earth's
mass".

---

## ★★6 — Shell theorem and its look-alikes

**(a)** For a spherically symmetric distribution: the exterior field equals that of
a point mass with the same total mass at the centre; and the field inside a
uniform spherical *shell* is zero.

**(b)** Point mass at depth $d$, offset $\rho$:
$$g_z = \frac{GMd}{(\rho^{2}+d^{2})^{3/2}}$$
(directed along the line to the mass, with a vertical component as written).
Sphere of radius $a$, external point at $z \ge a$: $g = GM/z^{2}$ toward the
centre.

**(c)** For a compact mass $M$ at depth $d = 500$ m:

- at $\rho = 0$: $g_z = GMd/d^{3} = GM/d^{2} = GM/2.5\times10^{5}$;
- at $\rho = 500$ m: $(\rho^{2}+d^{2})^{3/2} = (5\times10^{5})^{3/2}
  = 3.5355\times10^{8}$, so $g_z = GM\times500/3.5355\times10^{8}
  = GM/7.0711\times10^{5}$.

The ratio is $2.5\times10^{5}/7.0711\times10^{5} = 0.3536 = 1/2.828$ — the
profile falls to 35% of its peak at a horizontal offset equal to the depth, which
is the standard "half-width at half-maximum of about the depth" rule of thumb for
a compact source.

Now the modelling error. If the body is a **sphere of radius 100 m** with its
centre at 500 m depth, the shell theorem says the field at the surface directly
above is $GM/500^{2}$ — *identical* to the point-mass value, because the
observation point is outside the sphere. The error in the direct-overhead case is
therefore **zero**, not small: the point-mass formula is exact whenever the source
is spherically symmetric and the observer is outside it. Errors appear only when
(i) the observer is inside the body, (ii) the body is far from spherical (a dyke,
a tabular ore body, a near-surface cavity), or (iii) the offset is large enough
that the body's finite size matters at the $10^{-2}$ level — the quadrupole term,
of order $(a/d)^{2} = (100/500)^{2} = 4\times10^{-2}$ for this geometry.

**(d)** The rule: use $GM/z^{2}$ when the source is spherically symmetric (or
treatable as such) and the observation point is outside it; use
$GMd/(\rho^{2}+d^{2})^{3/2}$ when the source is *compact compared with its depth*
and its external field is being approximated by a point at its centre — then
correct for the body's finite size by a multipole expansion (the next term is the
quadrupole, which scales as $(a/d)^{2}$). Never mix the two: they are different
models, and a dimensional check cannot tell them apart.

---

## ★★7 — Eccentric orbit

**(a)** $r_p = a(1-e) = 10^{7}\times0.7 = \mathbf{7.0\times10^{6}\ m}$;
$r_a = a(1+e) = \mathbf{1.3\times10^{7}\ m}$.

**(b)** $T = 2\pi\sqrt{a^{3}/\mu} = 2\pi\sqrt{10^{21}/3.986\times10^{14}}
= \mathbf{9\,952.01\ s}$ (2.76 h).

**(c)** $\varepsilon = -\mu/(2a) = -3.986\times10^{14}/2\times10^{7}
= \mathbf{-1.9930\times10^{7}\ J\,kg^{-1}}$.

**(d)** Semi-latus rectum: $a(1-e^{2}) = 10^{7}\times0.91
= \mathbf{7.5\times10^{6}\ m}$. From the periapsis, $h = r_pv_p
= 7.0\times10^{6}\times8603.82 = 6.0227\times10^{10}$ m² s⁻¹, so
$h^{2}/\mu = 3.627\times10^{21}/3.986\times10^{14} = 7.5\times10^{6}$ m ✓
(the lesson's demonstration reports this agreement to $6.5\times10^{-15}$
relative). The two routes agree because angular momentum and the orbit elements
are two descriptions of the same conserved quantity.

---

## ★★8 — The Earth–Moon system

**(a)** $\mu = G(M_\oplus + M_{\text{Moon}})$, i.e. the *total* mass, applied to
the *relative* separation. Using $GM_\oplus$ alone neglects the Moon's mass —
a few percent of the total, and therefore not negligible for lunar dynamics
(though it is negligible for an artificial satellite).

**(b)** The barycentre lies inside the Earth. "The Moon orbits the Earth" is a
convenient fiction because both bodies orbit the barycentre; the fiction is
harmless for the Moon's own trajectory but wrong for anything involving the
recoil of the Earth (tides, the Earth's wobble), which is precisely the physics of
interest here.

**(c)** The Moon raises a tidal bulge on the rotating Earth; friction (mostly in
the oceans) **delays** the bulge relative to the Earth–Moon line; the delayed
bulge is no longer aligned with the line, so the Moon exerts a **torque** on the
bulge that transfers spin angular momentum from the Earth to the Moon's orbit; the
Earth's spin slows (the length of day increases) and the Moon's orbit expands.
Total angular momentum of the pair is conserved; the energy does not balance,
because the difference is dissipated as heat.

**(d)** Measured, not derivable: the secular rate of length-of-day increase, the
lunar recession rate from lunar laser ranging, and the tidal dissipation
parameters. All must come from Earth-orientation series and the current literature
(IERS: <https://www.iers.org>). Derived here: the *structure* of the relation
between the rates (the $n/\omega$ energy split of
[02-02-03](../03-work-energy.md) §3.5) and the angular-momentum bookkeeping.

---

## ★★★9 — $J_2$ and nodal regression

**(a)** With $J_2 = 1.08\times10^{-3}$ (a given measured input), $R/p = 6.371/6.871
= 0.9272$, $(R/p)^{2} = 0.8597$, $n = \sqrt{\mu/r^{3}} = 1.1088\times10^{-3}$
rad s⁻¹ for $r = 6.871\times10^{6}$ m:

| inclination | $\cos i$ | $\dot\Omega$ (deg/day) |
|---|---|---|
| 0° | 1.0000 | **−7.643** |
| 53° | 0.6018 | **−4.600** |
| 90° | ≈0 | **−0.000** |
| 98° | −0.1392 | **+1.064** |

**(b)** A sun-synchronous orbit requires the node to regress by about
$+0.9856°$/day (the mean rate at which the Sun's right ascension advances, i.e.
$360°/365.24$ days — a *nominal* astronomical input to be confirmed from an
almanac). From the table, the required positive rate is achieved at
**retrograde inclinations near 98°**, which is why every sun-synchronous
polar-orbiting mission uses about 98°.

**(c)** Because $J_2$'s effect on the node and the argument of perigee is
*deterministic and large*, it is subtracted as a known signal to reveal the
smaller, geophysically interesting perturbations (the higher harmonics, the
time-variable gravity of the GRACE-class missions, and the tide). It is also the
mechanism that keeps a sun-synchronous orbit's local time fixed, which is what
makes change detection possible.

**(d)** As the orbit rises, atmospheric drag falls away and the **third-body
perturbations from the Sun and Moon** become relatively more important; they grow
with orbital radius while $J_2$ falls as $r^{-3.5}$ effective. The crossover for
a near-Earth satellite is of order a few thousand kilometres altitude — the
reason low-Earth-orbit and high-orbit mission design use different perturbation
models. (The precise crossover depends on the mission's tolerance; treat it as an
order-of-magnitude statement.)

---

## ★★★10 — Tidal acceleration as a field gradient

**(a)** The field of the Moon at distance $d$ from its centre is
$GM_m/d^{2}$. At a point displaced by $\Delta d = R_\oplus$ towards the Moon, the
field is $GM_m/(d-R_\oplus)^{2}$; the difference is

$$\Delta g \approx \frac{d(g)}{dr}\Delta r
= \frac{2GM_m}{d^{3}}R_\oplus,$$

which scales as $GM_mR_\oplus/d^{3}$ — the tidal acceleration. On the far side the
sign reverses, giving the second bulge.

**(b)** The ratio is

$$\frac{2GM_mR_\oplus/d^{3}}{GM_m/d^{2}} = \frac{2R_\oplus}{d}
\sim 2\times10^{-2},$$

using the order-of-magnitude $R_\oplus/d \sim 10^{-2}$ — which should be evaluated
from the current lunar distance in an almanac rather than from memory. So the
tidal acceleration is of order **1% of the Moon's central acceleration**; that is
why the Earth is not torn apart, but it is large enough to raise metre-scale ocean
tides.

**(c)** The tidal field has the same magnitude and *inward* direction at the
sub-lunar point and the *antipodal* point (both bulges). A rotating Earth passes
through both bulges twice per lunar day, so the tide at a fixed station has two
high waters per lunar day — **semi-diurnal** — not one. The diurnal inequality
(the difference between the two high waters of a day) arises from the Moon's
declination and is a second-order term.

**(d)** The *model* part is the derivation of the tidal field from the inverse-square
law and the geometry of the two bulges — that is exact for a rigid, uniform,
spherically symmetric Earth and a point source. The *measured* parts are the
response: the actual ocean and solid-Earth tides depend on the Earth's elasticity
(Love numbers), on ocean basin geometry and on the Moon's orbital parameters, and
the tidal amplitudes and phases in any tide table come from observation.
