# Solutions — 02-02-02 Newton's Laws and Free-Body Analysis

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed with $g = 9.82025\ \mathrm{m\,s^{-2}}$,
> $\omega = 7.292\,115\times10^{-5}$ rad s⁻¹, $R = 6\,371$ km.

---

## ★1 — Force lists with sources and third-law partners

**(a) Book on a table.** Forces *on the book*: weight $mg$ downward, exerted by
the Earth (partner: the book's gravitational pull on the Earth); normal force $N$
upward, exerted by the table (partner: the book's push on the table).

**(b) Block sliding down a rough incline.** Forces *on the block*: weight
(exerted by the Earth); normal force (exerted by the plane); kinetic friction up
the plane (exerted by the plane). Note the normal force and the friction force
are both exerted by the *plane* but are not a third-law pair with each other —
each is paired with the block's reaction on the plane.

**(c) Moon in orbit.** Force *on the Moon*: the Earth's gravity (partner: the
Moon's gravitational pull on the Earth). If we include radiation pressure, its
partner is the momentum change of the absorbed/reflected photons.

**What is not a pair, and why it matters.** The book's weight and the normal force
from the table are *equal in magnitude and opposite in direction* in this
equilibrium, and they are **not** third-law partners — they act on the same body
and involve different sources (Earth and table). Mistaking them for a pair leads
directly to the classic errors: concluding that the normal force always equals
$mg$ (false on an incline, in a lift, or on any accelerating surface), and
concluding that a body cannot accelerate while "forces balance".

---

## ★2 — Inclined-plane threshold

**(a)** Along the plane, on the point of slipping with $a = 0$:
$mg\sin\theta_c = \mu_sN$; perpendicular to it: $N = mg\cos\theta_c$. Dividing:

$$\tan\theta_c = \mu_s.$$

**(b)** $\theta_c = \arctan(0.55) = 28.811°$.

**(c)** No. The mass appears on both sides of the along-plane equation and
cancels; the threshold is a property of the *contact*, i.e. of the two material
surfaces, not of the block's size or mass. This is why a landslide's onset angle
is a material diagnostic — and why it is not, by itself, a diagnostic of
scale (see [02-01-03](../../01-measurement-and-physical-reasoning/03-scaling-laws.md) §3.6).

---

## ★3 — Normal force in a lift

**(a)**
- Accelerating upward at 1.2 m/s²: $N = m(g+a) = 70\times(9.82025+1.2)
  = \mathbf{771.42\ N}$.
- Accelerating downward at 1.2 m/s²: $N = m(g-a) = 70\times8.62025
  = \mathbf{603.42\ N}$.

**(b)** In free fall ($a = g$ downward): $N = 0$ — apparent weightlessness.

**(c)** The person's **weight** is $mg = 687.42$ N, exerted by the Earth and
independent of the lift's motion. The **scale reading** is the normal force the
person exerts on the scale (equal and opposite to $N$), and it changes with the
acceleration. The distinction is not pedantic: a gravimeter's reading is a
normal-force measurement, so a moving platform or a seismic disturbance corrupts
it.

---

## ★4 — Three quantities, two dimensions

$[F] = \mathrm{M\,L\,T^{-2}}$ (N); $[\tau] = \mathrm{M\,L^{2}\,T^{-2}}$ (N m);
$[E] = \mathrm{M\,L^{2}\,T^{-2}}$ (J). Torque and energy share a dimension because
both are the product of a force and a length, but torque is a *vector formed from
a cross product* (and is pseudovector under reflection) while energy is a *scalar
formed from a dot product*; adding them would have no coordinate-independent
meaning.

---

## ★★5 — Atwood machine with $m_1 = 6$, $m_2 = 4$ kg

**(a)** With $a$ the downward acceleration of $m_1$:
$m_1g - T = m_1a$ and $T - m_2g = m_2a$. Adding gives

$$a = \frac{m_1-m_2}{m_1+m_2}g, \qquad
T = \frac{2m_1m_2}{m_1+m_2}g.$$

**(b)** $a = (2/10)\times9.82025 = \mathbf{1.96405\ m\,s^{-2}}$;
$T = 2\times6\times4\times9.82025/10 = \mathbf{47.1372\ N}$.

**(c)** With $s = 1$ m: $v^{2} = 2as = 3.92810$ m² s⁻². Kinetic energy gain
$= \tfrac12(m_1+m_2)v^{2} = \tfrac12\times10\times3.92810 = 19.6405$ J. Potential
energy lost $= (m_1-m_2)gs = 2\times9.82025\times1 = 19.6405$ J. **Equal** — the
energy route reproduces the force route exactly.

**(d)** If the string is cut, $T = 0$ and each mass falls freely with $a = g$.
This is the $m_2 \to 0$ limit of the formula, and it is a useful sanity check:
the tension is a *constraint* force that vanishes when the constraint is removed.

---

## ★★6 — Apparent gravity at 60° latitude

**(a)** $\omega^{2}R = (7.292\,115\times10^{-5})^{2}\times6\,371\,000
= \mathbf{0.0338778\ m\,s^{-2}}$, which is **0.34498%** of
$g_r = GM/R^{2} = 9.82025\ \mathrm{m\,s^{-2}}$.

**(b)** At $\phi = 60°$:
$g_{\text{vert}} = g_r - \omega^{2}R\cos^{2}60° = 9.82025 - 0.0338778\times0.25
= 9.811781\ \mathrm{m\,s^{-2}}$;
$g_{\text{horiz}} = \omega^{2}R\cos60°\sin60° = 0.0146695\ \mathrm{m\,s^{-2}}$;
$g_{\text{eff}} = 9.811792\ \mathrm{m\,s^{-2}}$;
$\delta = \arctan(0.0146695/9.811781) = \mathbf{0.0857°}$ = **5.14 arcmin**.

**(c)** Omitted: (i) the gravitational effect of the Earth's *flattening*, which
is of the same order as the centrifugal term and partially cancels it in the
deflection; and (ii) the fact that the reference surface is a geoid, not a sphere
of radius 6371 km. Both are of order the quantity computed — arcminutes — so
this calculation identifies the mechanism and its order of magnitude, and cannot
be used as a geodetic value. Geodetic deflections of the vertical are computed
from a gravity model ([07-gravity-geodesy](../../../07-gravity-geodesy/README.md)).

---

## ★★7 — Airy root for a 2 km plateau

**(a)** $r = \rho_ch/(\rho_m-\rho_c) = 2700\times2000/600 = \mathbf{9000\ m}
= 9$ km.

**(b)** With a 35 km reference crust, the pressure at the depth of the root base
(35 + 9 = 44 km below the datum, i.e. 2 km below the plateau surface at
46 km depth under the load):

- column away from the load: $\rho_cg\times35\,000 + \rho_mg\times9000
  = 1.219675\times10^{9}$ Pa;
- column under the load: $\rho_cg\times(2000+35\,000+9000)
  = 1.219675\times10^{9}$ Pa.

They agree **exactly** — because the root was derived from that balance. The
check is therefore a check on the algebra, and the *physics* is entirely in the
density contrast and in the assumption of local (Airy) compensation.

**(c)** With $\Delta\rho = 600\pm50$:
$u(r) = r\,u(\Delta\rho)/\Delta\rho = 9000\times50/600 = \mathbf{750\ m}$ (the
exact recomputation at $\Delta\rho = 550$ gives 9818 m, a difference of 818 m —
the linearisation is already 9% off at a 8% parameter change, which is worth
noticing). Report $r = (9.0 \pm 0.8)$ km and say the linearisation is at its
limit.

---

## ★★8 — Settling of a quartz grain

**(a)** Stokes terminal velocity:
$$v = \frac{(\rho_s-\rho_w)gd^{2}}{18\eta}
= \frac{1650\times9.82025\times(10^{-4})^{2}}{18\times10^{-3}}
= \mathbf{9.0019\times10^{-3}\ m\,s^{-1}}.$$

**(b)** $\mathrm{Re} = \rho_wvd/\eta = 1025\times9.0019\times10^{-3}\times10^{-4}/10^{-3}
= \mathbf{0.90}$. This is below 1, so the creeping-flow assumption behind the
Stokes formula is self-consistent — but only just, and a grain twice as large
would violate it.

**(c)** $9.0019\times10^{-3}\ \mathrm{m\,s^{-1}} = \mathbf{777.8\ m\,day^{-1}}$.
A sediment trap at 100 m depth would be reached in about 3.1 hours of quiescent
water, so a trap deployed for a day collects everything that settles — which is
why trap results are dominated by flocculation and currents rather than by
individual-grain settling speeds.

---

## ★★★9 — Levelling requirement from a gravity gradient

**(a)** $\dfrac{dg}{dr} = -\dfrac{2GM}{R^{3}} = -3.0828\times10^{-6}\ \mathrm{s^{-2}}
= 0.30828\ \mathrm{mGal\,m^{-1}}$.

**(b)** For a 0.01 mGal tolerance: $\Delta z = 0.01/0.30828 = 0.0324$ m —
**3.2 cm**.

**(c)** The centrifugal term contributes a *latitude* dependence
$dg/d\phi = 2\omega^{2}R\cos\phi\sin\phi$ (at 60°: $0.029339\ \mathrm{m\,s^{-2}\,rad^{-1}}
= 51.2$ mGal per degree of latitude). Over a 50 km north–south span
($\approx 0.45°$) that is about **23 mGal** — four orders of magnitude larger
than the instrument's resolution, and therefore a correction that must come from
the normal-gravity formula, not from the survey's own levelling. Elevation and
latitude are simply not separable by the instrument alone.

**(d)** A defensible sensitivity statement: *"Station positions are determined to
0.03 m vertically and 10 m horizontally; the vertical gradient is
0.3083 mGal/m, so the levelling contribution to the anomaly uncertainty is
0.009 mGal. The latitude correction is computed from the WGS 84 normal-gravity
formula; a 10 m horizontal position error contributes
$x\,\partial g/\partial x$ with $\partial g/\partial x$ of order
0.8 mGal/km at this latitude, i.e. under 0.01 mGal. Neither term is the
dominant one."* The final clause is the point: it is the *statement of the
ranking* that makes the budget useful.

---

## ★★★10 — Slope stability with pore pressure

**(a) Drained case.** With no pore pressure, the along-slope driving stress for a
slab of thickness $h$ is $\tau = \rho_{\text{sat}}gh\sin\theta$ and the effective
normal stress is $\sigma_n = \rho_{\text{sat}}gh\cos\theta$. Setting
$\tau = \sigma_n\tan\phi'$ gives the familiar

$$\tan\theta_c = \tan\phi' \;\Longrightarrow\; \theta_c = \phi'.$$

**Saturated case.** Now the pore pressure reduces the effective normal stress:
$\sigma_n - p = \rho_{\text{sat}}gh\cos\theta - \rho_wgh\cos\theta$
(for saturation to the surface, the pore pressure at depth $h$ along the slope is
$\rho_wgh\cos\theta$). Then

$$\tan\theta_c = \frac{\rho_{\text{sat}}-\rho_w}{\rho_{\text{sat}}}\tan\phi'
= \left(1 - \frac{\rho_w}{\rho_{\text{sat}}}\right)\tan\phi'.$$

**(b)** With $\phi' = 30°$: drained $\theta_c = 30.00°$. Saturated with
$\rho_{\text{sat}} = 2000$: the factor is $1 - 1000/2000 = 0.5$, so
$\tan\theta_c = 0.5\times0.57735 = 0.28868$ and $\theta_c = \mathbf{16.10°}$.

**(c)** Saturation does not change the *friction angle* or the slope's
geometry: it changes the **normal force** between the sliding mass and the
plane, because water pressure pushes the two apart, reducing the contact force
that friction can act on. Since the driving component (the along-slope weight) is
unchanged, the ratio of driving to resisting stress rises by the factor
$\rho_{\text{sat}}/(\rho_{\text{sat}}-\rho_w) = 2$ here. A rainfall event raises
the water table, hence the pore pressure, hence this ratio — and it can do so in
hours, whereas the geometry and the friction angle change over geological time.
That asymmetry is why pore pressure, not material strength, is the usual trigger
in shallow landslides.
