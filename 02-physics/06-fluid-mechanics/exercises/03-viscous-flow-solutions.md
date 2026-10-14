# Solutions — 02-06-03 Viscous Flow, Reynolds Number and Boundary Layers

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Couette flow

**(a)** $u(y) = Uy/h = 0.1\,y/10^{-3}$, so at mid-gap $y = 5\times10^{-4}$ m,
$u = \mathbf{0.05\ m\,s^{-1}}$.

**(b)** $\tau = \mu\,\mathrm{d}u/\mathrm{d}y = \mu U/h = 10^{-3}\times0.1/
10^{-3} = \mathbf{0.1\ Pa}$, the same at every $y$. It is uniform because the
velocity profile is linear, so the shear rate is constant, and stress = $\mu\times$
shear rate. This is a property of Couette flow with no pressure gradient, not a
general result.

**(c)** $\mathrm{d}u/\mathrm{d}y = U/h = 100\ \mathrm{s^{-1}}$.

**(d)** A rotational viscometer measures the **torque** required to rotate one
cylinder relative to the other at a known angular velocity. The torque gives the
shear stress at the cylinder, the angular velocity gives the shear rate, and
their ratio is $\mu$ — provided the gap is small enough that the curvature can be
ignored and the flow is laminar and Newtonian. If the fluid is non-Newtonian the
ratio depends on the shear rate and one measurement is not enough.

---

## ★2 — Fracture flow

**(a)** $q = \dfrac{b^3G}{12\mu} =
\dfrac{(5\times10^{-4})^3\times10^4}{12\times10^{-3}} =
\mathbf{1.042\times10^{-4}\ \mathrm{m^2\,s^{-1}}}$ per unit width.

**(b)** $k = b^2/12 = (5\times10^{-4})^2/12 = 2.083\times10^{-8}$ m²
$= 2.083\times10^{-8}/0.9869\times10^{-12} = \mathbf{2.11\times10^4\ darcy}$.

**(c)** $u_{\text{mean}} = q/b = 1.042\times10^{-4}/5\times10^{-4} = \mathbf{0.208\
\mathrm{m\,s^{-1}}}$; $u_{\text{max}} = \tfrac32 u_{\text{mean}} = 0.313\
\mathrm{m\,s^{-1}}$ (equivalently $Gb^2/(8\mu) = 0.3125$ m s⁻¹).
$Re = \rho u_{\text{mean}}b/\mu = 1000\times0.208\times5\times10^{-4}/10^{-3} =
\mathbf{104}$. Laminar, so the cubic law is internally consistent — but note
that this is well above the range in which Darcy's law is trusted for a *porous
medium* (see ★★★10).

**(d)** $Q = qW = 1.042\times10^{-4}\times10 = \mathbf{1.04\times10^{-3}\
\mathrm{m^3\,s^{-1}}}$, about a litre per second through a single 10 m wide,
half-millimetre fracture.

---

## ★3 — Borehole flow

**(a)** $\Delta p = \rho g h = 1000\times9.81\times1 = \mathbf{9810\ Pa}$.

**(b)** $Q = \dfrac{\pi\Delta p R^4}{8\mu L} =
\dfrac{\pi\times9810\times(0.05)^4}{8\times10^{-3}\times100} =
\mathbf{0.2408\ m^3\,s^{-1}}$.

**(c)** $\bar u = Q/(\pi R^2) = 0.2408/7.854\times10^{-3} = \mathbf{30.66\
\mathrm{m\,s^{-1}}}$; $Re = \rho\bar u(2R)/\mu =
1000\times30.66\times0.1/10^{-3} = \mathbf{3.07\times10^{6}}$.

**(d)** $f = 64/Re = \mathbf{2.09\times10^{-5}}$. **Not applicable**: the laminar
friction law is valid for $Re \lesssim 2000$, and this Reynolds number exceeds it
by three orders of magnitude. The computed 30.7 m s⁻¹ is what the laminar formula
says; a real borehole with a 1 per cent hydraulic gradient carries a few metres
per second at most, because turbulent wall friction is enormously larger. The
formula has not failed; the assumption behind it has.

---

## ★4 — Boundary layer on a plate

**(a)** $Re_x = Ux/\nu = 0.1\times10/10^{-6} = \mathbf{10^{6}}$.

**(b)** $\delta_{\text{lam}} = 5\sqrt{\nu x/U} =
5\sqrt{10^{-6}\times10/0.1} = 5\times10^{-2} = \mathbf{0.05\ m}$.

**(c)** $\delta_{\text{turb}} = 0.37\,x\,Re_x^{-1/5} =
0.37\times10\times(10^6)^{-0.2} = \mathbf{0.233\ m}$.

**(d)** With $Re_x = 10^6 > 5\times10^5$, the **turbulent** estimate applies.
Quoting the laminar value would understate the thickness by a factor of
$0.233/0.05 = \mathbf{4.7}$. This is a regime error, not a rounding error.

---

## ★★5 — Cubic-law sensitivity

**(a)** $(1/0.5)^3 = \mathbf{8}$: halving the aperture reduces flow eightfold.

**(b)** $(2/1)^3 = \mathbf{8}$: doubling the aperture multiplies flow by eight.

**(c)** Because a factor of two in aperture is a factor of eight in flow, and
aperture in a real rock mass varies by much more than a factor of two across a
fracture network, crustal permeability spans many orders of magnitude — which is
why the handbook quotes crustal hydraulic diffusivity as a range $10^{-2}$ to
$10^{0}\ \mathrm{m^2\,s^{-1}}$ rather than a value.

**(d)** $q \propto (0.8)^3 = 0.512$: the flow falls by **48.8 per cent**. A
20 per cent change in aperture almost halves the flow. This is the quantitative
reason stress changes and poroelastic coupling matter so much in fractured
aquifers and in induced-seismicity studies.

---

## ★★6 — Reading the demo

**(a)** At $U = 0.1\ \mathrm{m\,s^{-1}}$: fracture $Re = 1.000\times10^{2}$
(laminar); borehole $Re = 1.000\times10^{4}$ (turbulent). Same water, same
speed, one geometry laminar and the other turbulent.

**(b)** Cubic law $q = 8.333\times10^{-4}\ \mathrm{m^2\,s^{-1}}$; quadrature
$q = 8.333\times10^{-4}\ \mathrm{m^2\,s^{-1}}$; relative error
$1.25\times10^{-11}$.

**(c)** $k = b^2/12 = 8.3333\times10^{-8}$ m² $= 84.4375\times10^{3}$ darcy
(the demo prints $84.4375\times10^{3}$).

**(d)** $\bar u = 30.6563\ \mathrm{m\,s^{-1}}$ at $Re = 3.066\times10^{6}$. The
laminar result must not be used because at that Reynolds number the flow is
violently turbulent; the parabolic profile is not the profile, and the friction
law that applies is $f \approx 0.316\,Re^{-1/4}$ (Blasius turbulent) or a
Colebrook-type law, not $64/Re$. The lesson is not that the formula is wrong but
that its *regime of validity* has been exceeded, and the demo prints the
Reynolds number precisely so that the reader can see it.

---

## ★★7 — Settling of a quartz grain

**(a)** $w = \dfrac{2(2650-1000)\times9.81\times(2.5\times10^{-4})^2}
{9\times10^{-3}} = \mathbf{0.2248\ m\,s^{-1}}$.

**(b)** $Re = \rho w(2a)/\mu = 1000\times0.2248\times5\times10^{-4}/10^{-3} =
\mathbf{112}$. **Not self-consistent**: Stokes' law assumes $Re \ll 1$.

**(c)** At $Re \sim 100$ the appropriate correction is a drag-correlation
regime (Newton regime or a Schiller–Naumann-type correction), in which the drag
coefficient is larger than $24/Re$; the true settling velocity is therefore
**lower** than the Stokes prediction, by roughly a factor of two at this $Re$.

**(d)** For $a = 0.05$ mm, $w = 0.2248\times(0.05/0.25)^2 = 8.99\times10^{-3}$
m s⁻¹ and $Re = 112\times(0.2)^3 = 0.899$ — because $Re \propto a^3$. That is
marginally inside the Stokes regime. The general rule is that Stokes settling is
secure for fine silt and clay and must be used with a check for sand.

---

## ★★8 — Hydraulic versus mechanical aperture

**(a)** $b_h = \left(\dfrac{12\mu q}{G}\right)^{1/3} =
\left(\dfrac{12\times10^{-3}\times2.083\times10^{-4}}{10^4}\right)^{1/3} =
\left(2.5\times10^{-10}\right)^{1/3} = \mathbf{6.30\times10^{-4}\ m} =
0.63$ mm.

**(b)** $b_h/b_{\text{mech}} = 0.63/1.0 = \mathbf{0.63}$: the hydraulic aperture
is 37 per cent smaller.

**(c)** A real fracture's walls are rough and its aperture varies from point to
point. Because the local flux scales as the *cube* of the local aperture, the
flow is dominated by the widest patches, and the fluid effectively follows a
tortuous path of connected wide zones rather than the whole nominal opening. The
equivalent smooth parallel-plate aperture that reproduces the measured flux —
the hydraulic aperture — is therefore smaller than the average mechanical
opening. This is the same reason that the "mean" aperture is not the right
variable: the correct average is a cube-weighted average, which is biased towards
the wide patches.

**(d)** The **hydraulic** aperture. It is the only one that reproduces the
measured flux, and it is what a discrete-fracture flow model needs. The
mechanical aperture is a geometric observation; it cannot be converted to a
hydraulic aperture by geometry alone, because the ratio depends on the aperture
distribution and the contact area. Flow tests are therefore the primary
measurement, and the cubic law supplies only the scaling.

---

## ★★★9 — The lubrication approximation

**(a)** Let $u$ vary from 0 to $U$ across the gap $h$, so
$\partial^2u/\partial y^2 \sim U/h^2$ and $\mu\partial^2u/\partial y^2 \sim
\mu U/h^2$. Along $x$ the same viscous term acts on a scale $L$, so
$\mu\partial^2u/\partial x^2 \sim \mu U/L^2$. The ratio of the transverse to the
streamwise viscous term is therefore $(h/L)^2$. Since the only other force in the
$x$ direction is the pressure gradient, and the $y$ momentum equation has no
driving term of comparable size, the transverse pressure gradient is smaller than
the streamwise gradient by $(h/L)^2$, so $p = p(x)$ to leading order.

**(b)** With $p = p(x)$, the $x$-momentum equation is
$\mu\,\mathrm{d}^2u/\mathrm{d}y^2 = \mathrm{d}p/\mathrm{d}x$, giving the
parabolic profile of equation (3) with $G = -\mathrm{d}p/\mathrm{d}x$ and
$q = -\dfrac{h^3}{12\mu}\dfrac{\mathrm{d}p}{\mathrm{d}x}$. Continuity for steady
incompressible flow requires $q$ to be independent of $x$ (no accumulation), so

$$\frac{\partial}{\partial x}\left(\frac{h^3}{12\mu}
\frac{\partial p}{\partial x}\right) = 0 .$$

**(c)** For constant $h$, the equation integrates to $\mathrm{d}p/\mathrm{d}x =
$ const, i.e. a linear pressure drop, and $q = -h^3 G/(12\mu)$ — the cubic law.
The regime of validity is $h/L \ll 1$, with the error in the neglected transverse
pressure gradient of order $(h/L)^2$.

**(d)** The approximation fails where the gap is comparable to the extent of the
flow, for example at the **entrance** to a conduit or in a **wide karst
conduit** or a small lake: there $h/L$ is of order one, the flow separates, and
neither a parabolic profile nor a constant pressure across the section is a good
description. This is the same limitation as the "fully developed flow" caveat of
section 5.

---

## ★★★10 — Darcy validity

**(a)** With the Darcy-velocity convention $Re_p = \rho q d/\mu$ and
$d = 2\times10^{-4}$ m and $\phi = 0.2$:

| $q$ (m s⁻¹) | $v = q/\phi$ (m s⁻¹) | $Re_p = \rho q d/\mu$ |
|---|---|---|
| $10^{-5}$ | $5\times10^{-5}$ | 0.002 |
| $10^{-4}$ | $5\times10^{-4}$ | 0.02 |
| $10^{-3}$ | $5\times10^{-3}$ | 0.2 |
| $10^{-2}$ | $5\times10^{-2}$ | 2 |

The pore-velocity column is shown for reference only; using $v$ in place of $q$
would multiply every $Re_p$ by $1/\phi = 5$, which is why the convention must be
stated.

**(b)** $Re_p = 1$ at $q = \mu/(\rho d) = 10^{-3}/(1000\times2\times10^{-4}) =
\mathbf{5\times10^{-3}\ m\,s^{-1}}$.

**(c)** $5\times10^{-3}\times86\,400 = \mathbf{432\ m\,day^{-1}}$. Typical
groundwater velocities are $0.1$–$1$ m per day, two to three orders of magnitude
below the limit. The demo prints exactly this threshold: `d = 2.0e-04 m -> q* =
5.000e-03 m/s = 4.320e+02 m/day`.

**(d)** Because the limit is at 432 m per day, ordinary groundwater flow is
nowhere near it, and Darcy's law is valid with a wide margin — which is why
hydrogeology can be built on a linear law. Near a gravel-packed well, or in a
karst conduit, the same discharge passes through much larger pores or a free
conduit: the length scale $d$ jumps from 0.2 mm to centimetres or more and the
specific discharge reaches metres per second, so $Re_p$ exceeds 10 and the
quadratic (Forchheimer) correction becomes necessary. The demo's table makes the
contrast explicit: at $q = 10^{-2}$ m s⁻¹ the 0.2 mm sand is at $Re_p = 2$ while a
10 mm gravel is at $Re_p = 100$. The transition is not about the water; it is
about the geometry the water is forced through.
