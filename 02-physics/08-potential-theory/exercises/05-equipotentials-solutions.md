# Solutions — 02-08-05 Equipotential Surfaces, Geoid and Level Surfaces

> **Read this after attempting the exercises, not before.** WGS 84 defining
> parameters: $a = 6\,378\,137$ m, $1/f = 298.257\,223\,563$,
> $\omega = 7.292\,115\times10^{-5}$ rad s$^{-1}$,
> $GM_\oplus = 3.986\,004\,418\times10^{14}$ m$^3$ s$^{-2}$;
> $G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$. Values attributed to the
> demonstration are its actual output.

---

## ★1 — Definitions

**(a)** The geoid is the equipotential surface of the actual gravity potential
(gravitation plus centrifugal) that best fits mean sea level, continued
mathematically under the continents.

**(b)** The reference ellipsoid is a mathematically defined surface of revolution —
for WGS 84, the ellipsoid with semi-major axis $6\,378\,137$ m and inverse flattening
$298.257\,223\,563$ — chosen by convention so that coordinates are comparable
worldwide. It is a datum, not a physical surface.

**(c)** The geoid undulation is $N = h - H$, the height of the geoid above the
reference ellipsoid, positive where the geoid lies outside (above) the ellipsoid.

**(d)** The geoid is an **equipotential** (a level surface of the actual potential);
the ellipsoid is a **convention**. Topography is neither — it is the irregular
physical surface of the ground.

**(e)** Because the sea surface is a moving fluid in equilibrium with the atmosphere
and with ocean currents, so it departs from the geoid by the dynamic topography, of
order a metre. A "geoid from altimetry" must model and remove that signal.

---

## ★2 — $q$ and the flattening

**(a)** $q = \omega^2a^3/GM = 3.461\,391\,8985\times10^{-3}$.

**(b)** $f = 1/298.257\,223\,563 = 3.352\,810\,6647\times10^{-3}$.

**(c)** $b = a(1-f) = 6\,356\,752.314$ m; $a-b = 21\,384.686$ m ≈ $21.4$ km.

**(d)** $J_2 = (2f-q)/3 = 1.081\,409\,8103\times10^{-3}$.

**(e)** The datum quotes the **inverse** flattening ($1/f = 298.257$), so $f$ itself
is $3.3528\times10^{-3}$. Reading the wrong one as $f$ makes the flattening
$298.257$, i.e. $89\,000$ times too large: every derived quantity — the polar
radius, the ellipsoid's eccentricity, any $J_2$ — is then absurd, and the arithmetic
will look suspicious rather than subtly wrong, which is a mercy.

---

## ★3 — Bruns' formula

**(a)** $N = T/\gamma$, where $T$ is the disturbing potential (the difference between
the actual and reference gravity potentials, evaluated on the reference surface) and
$\gamma$ is the normal gravity (the magnitude of the gradient of the reference
potential), in m$^2$ s$^{-2}$ and m s$^{-2}$ respectively, giving $N$ in m.

**(b)** $N = 9.8/9.8 = 1.0$ m.

**(c)** $N = 98/9.8 = 10.0$ m.

**(d)** Bruns' formula is valid to first order in $T/\gamma$; the neglected term is of
order $(T/\gamma)^2$ times a curvature scale, i.e. roughly $N^2/a$ relative. For
$N = 1$ m, $N^2/a = 1/6.4\times10^6 = 1.6\times10^{-7}$ m — entirely negligible. For
$N = 10$ m it is $1.6\times10^{-5}$ m, still negligible. The demonstration measures
the first-order error directly: $1.07\times10^{-5}$ relative for $N = 0.107$ m and
$3.5\times10^{-5}$ for $N = 1.42$ m, both consistent with an error quadratic in
$T/\gamma$.

---

## ★4 — Deflection of the vertical

**(a)** The deflection is the angle between the local vertical (the direction of
$-\nabla U$, equivalently of $\nabla U$ pointing "down") and the normal to the
reference ellipsoid at the same point. It has two components, north–south and
east–west, and is conventionally quoted in arcseconds.

**(b)** $\varepsilon = 1.0\times10^{-4}/9.8 = 1.0204\times10^{-5}$ rad
$= 2.1047$ arcsec.

**(c)** $1$ arcsec $= \pi/(180\times3600) = 4.848\,136\,8\times10^{-6}$ rad.

**(d)** The deflection is proportional to the *horizontal gradient* of the disturbing
potential rather than to its magnitude, so it weights short wavelengths relative to
long ones more heavily than a gravity anomaly does. Its depth sensitivity is
correspondingly shallower: a deep broad mass gives a small deflection and a
comparatively larger geoid signal, while a shallow body gives the opposite.

---

## ★5 — Reading the demonstration

**(a)** $\cos(\text{angle}) = +4.999\,938\times10^{-4}$ at $h = 10^{-3}$ rad and
$+4.999\,081\times10^{-7}$ at $h = 10^{-6}$ rad: a ratio of about $10^{3}$, i.e.
linear in $h$, as predicted by the chord-versus-tangent geometry.

**(b)** Sphericity spread with $\omega = 0$: $9.31\times10^{-10}$ m — floating-point
noise.

**(c)** Model flattening $f_{\text{model}} = 1.727\,705\,8158\times10^{-3}
= 1/578.802$; datum $f = 3.352\,810\,6647\times10^{-3} = 1/298.257$; ratio
$0.5153$.

**(d)** Best-fit polar semi-axis $b = 6\,367\,112.5$ m (the model's own polar radius is $6\,367\,117.46$ m), worst residual $5.0$ m.

**(e)** $J_2$ from $(2f-q)/3$: $1.081\,409\,8103\times10^{-3}$; homogeneous
$(2f-f^2)/5$: $1.338\,875\,9980\times10^{-3}$; ratio $0.8077$.

**(f)** Worst relative difference between Bruns' formula and the solved level
surface: $3.53\times10^{-5}$ (the crustal root at the pole); the small ore body's
worst is $1.07\times10^{-5}$.

**(g)** Peak deflection $2.6411$ arcsec, at a horizontal offset near $d/\sqrt{2}
= 28.3$ km.

---

## ★6 — A shallow mass anomaly

**(a)** $M = \tfrac43\pi(5000)^3\times300 = 1.570\,796\times10^{14}$ kg.

**(b)** $T = GM/d = 6.674\,30\times10^{-11}\times1.570\,796\times10^{14}/10^4
= 1.0484$ m$^2$ s$^{-2}$.

**(c)** $N = T/\gamma = 1.0484/9.8 = 0.1070$ m. (The demonstration's level-surface
solve gives $0.1066$ m and Bruns' formula $0.1066$ m, agreeing to
$1.07\times10^{-5}$; the small difference from the hand estimate is the variation of
$\gamma$ with latitude and of the geometry with $r$.)

**(d)** A $0.1$ m undulation is at the very edge of what a regional geoid model
resolves, and far below the accuracy of a global one. So geoid data do **not** measure
shallow geology: a large shallow ore body is essentially invisible in the geoid while
producing a large gravity anomaly. Geoid anomalies measure deep, broad mass
distributions — a depth filter that is useful precisely because it is different from
gravity.

---

## ★7 — A deeper, broader anomaly

**(a)** $M = \tfrac43\pi(20\,000)^3\times250 = 8.377\,580\times10^{15}$ kg.

**(b)** $T = GM/d = 6.674\,30\times10^{-11}\times8.377\,580\times10^{15}/4\times10^4
= 13.979$ m$^2$ s$^{-2}$, so $N = 13.979/9.8 = 1.426$ m. (Demonstration: level
surface $1.4217$ m, Bruns $1.4217$ m.)

**(c)**

| $X$ (m) | $a_h$ (m s$^{-2}$) | $\varepsilon$ (arcsec) |
|---|---|---|
| $0$ | $0$ | $0.0000$ |
| $10\,000$ | $7.977\times10^{-5}$ | $1.6790$ |
| $20\,000$ | $1.250\times10^{-4}$ | $2.6315$ |
| $40\,000$ | $1.236\times10^{-4}$ | $2.6005$ |
| $80\,000$ | $6.251\times10^{-5}$ | $1.3158$ |

The deflection peaks between $X = 20$ and $40$ km, consistent with the analytic
maximum at $X = d/\sqrt{2}\approx28.3$ km — *not* above the mass, where it vanishes
by symmetry.

**(d)** Geoid undulation ratio: $N_2/N_1 = (M_2/d_2)/(M_1/d_1)
= (8.3776\times10^{15}/4\times10^4)/(1.5708\times10^{14}/10^4) = 13.33$. Peak gravity
anomaly ratio: $(M_2/d_2^2)/(M_1/d_1^2) = (8.3776\times10^{15}/1.6\times10^9)/
(1.5708\times10^{14}/10^8) = 3.333$. The geoid is $13.3$ times larger for the second
body while the gravity anomaly is only $3.33$ times larger — and the ratio of those
ratios is exactly $4$, the ratio of the depths. That is the quantitative statement
that geoid anomaly per unit gravity anomaly scales with **depth**, which is why the
geoid is the tool for deep mass anomalies and gravity for shallow ones. In absolute
terms the peak gravity anomalies are $10.48$ mGal and $34.95$ mGal.

---

## ★8 — The level surface of a rotating point mass

**(a)** $U(r,\theta) = GM/r + \tfrac12\omega^2r^2\sin^2\theta$, with $\theta$ the
colatitude.

**(b)** $\nabla^2U = \nabla^2(GM/r) + \nabla^2(\tfrac12\omega^2r^2\sin^2\theta)
= 0 + 2\omega^2$. The centrifugal term is not harmonic; its Laplacian is
$2\omega^2 = 1.0635\times10^{-8}$ s$^{-2}$, small but non-zero. Gravity as a whole
(gravitation plus centrifugal) is therefore *not* a harmonic field anywhere, which is
why geodesy works with the disturbing potential.

**(c)** Fix $U_0 = U(a,90^\circ) = GM/a + \tfrac12\omega^2a^2 = 6.2602966661\times10^{7}$
m$^2$ s$^{-2}$, then solve $U(r,\theta) = U_0$ at each colatitude. At the pole,
$\sin\theta = 0$ so $r = GM/U_0$: $r(0^\circ) = 6\,367\,117.455611$ m. At the
equator, solving gives $r(90^\circ) = 6\,378\,137.000000$ m — the value imposed by
construction.

**(d)** $f_{\text{model}} = (r_{90}-r_0)/r_{90} = 1.7277\times10^{-3} = 1/578.8$,
against the datum $3.3528\times10^{-3} = 1/298.3$: the model is *less* flattened than
the real Earth. Physically, a point mass has no quadrupole, so with the same rotation
rate it flattens less; the real Earth's mass is distributed, which increases its
quadrupole and hence its flattening (through $f\approx\tfrac12q+\tfrac32J_2$). The
comparison therefore measures the concentration of the Earth's mass — the same
statement as $J_2^{\text{Earth}} < J_2^{\text{homogeneous}}$.

---

## ★★★9 — Geoid versus ellipsoid

**(a)** An equipotential of a rotating fluid body is determined by the balance of
gravitation, centrifugal force and pressure. Its shape is generally not an ellipsoid
because the potential's $r^{-(l+1)}$ terms with $l\ge4$ are non-zero for any
non-uniform density, and each adds a non-quadratic correction to the surface. The
level surface coincides with an ellipsoid only if the density distribution is such
that all $l\ge3$ coefficients vanish — true for a *homogeneous* Maclaurin spheroid to
the extent that its shape is exactly a spheroid (an ellipsoid of revolution), which
is the one classical case where the level surface *is* an ellipsoid.

**(b)** For a homogeneous Maclaurin spheroid the theory of figures gives
$J_2 = (2f-q)/3$ to first order in $q$ (with higher-order terms in $q$ present). An
exactly elliptical level surface requires that all higher multipoles vanish in the
potential, which happens only for the homogeneous case; for a general radially
varying density the quadrupole is set by the density profile through
$J_2 = -\tfrac{1}{Ma^2}\int r'^2P_2(\cos\theta')\rho\,dV'$ and the level surface has
non-elliptical corrections of higher order.

**(c)** The **hydrostatic excess**: with the defining $f$ and $q$ from WGS 84 the
hydrostatic relation predicts $J_2^{\text{hydro}} = 1.0814\times10^{-3}$ (computed in
Section ★8), and the measured value is about $1.08\times10^{-3}$ — so the excess is
only a fraction of a per cent. A non-zero excess would mean the equatorial bulge is
not entirely supported hydrostatically, i.e. that the lithosphere or mantle
convection carries part of the load, and it is one of the standard constraints on
mantle viscosity and on the long-wavelength geoid. Constraining it requires the
measured $J_2$ (and higher coefficients) from satellite tracking and the gravity
model; the authoritative values and their uncertainties come from ICGEM, and the
Earth's rotation parameters from IERS.

**(d)** Parts (a)–(b) are derived from the equations; part (c) is a statement about
the real Earth and requires **data**: the gravity coefficients from ICGEM, the
rotation parameters from IERS, and the WGS 84 defining parameters (which are exact by
definition, so they need no uncertainty). No numerical value for the real excess is
quoted here because it depends on which measured coefficient set and epoch are used.

---

## ★★★10 — Geoid undulation and gravity anomaly

**(a)** With $T(r,\theta,\phi) = (GM/r)\sum_{l\ge2}(a/r)^l
\sum_m C_{lm}Y_{lm}(\theta,\phi)$ (the $l=0$ and $l=1$ terms are removed by the
choice of reference and origin), Bruns' formula gives

$$N(\theta,\phi) = \frac{T(a,\theta,\phi)}{\gamma}
= \frac{GM}{a\gamma}\sum_{l\ge2}\sum_m C_{lm}Y_{lm}(\theta,\phi) .$$

**(b)** The free-air anomaly is
$\Delta g = -\partial T/\partial r - 2T/r$ (the radial derivative plus the
"free-air" term from the curvature of the coordinate system). Applying it term by
term to the series,

$$-\frac{\partial}{\partial r}\left[\frac{1}{r}\Big(\frac{a}{r}\Big)^l\right]
= \frac{l+1}{r^{l+2}}a^l , \qquad
-\frac{2}{r}\cdot\frac{a^l}{r^{l+1}} = -\frac{2a^l}{r^{l+2}} ,$$

so the coefficient of the $(l,m)$ term in $\Delta g$ is
$\tfrac{GM}{a^2}(l-1)(a/r)^{l+2}C_{lm}$, i.e. at $r=a$,
$\Delta g_{lm} = \tfrac{GM}{a^2}(l-1)C_{lm}$.

**(c)** Dividing, the ratio of the gravity anomaly to the geoid undulation for the
same coefficient is

$$\frac{\Delta g_{lm}}{N_{lm}} = \frac{GM(l-1)/a^2}{GM/(a\gamma)}
= \gamma\frac{l-1}{a} .$$

The factor $(l-1)$ is **degree-dependent and increases with $l$**, so a gravity
anomaly emphasises high degrees relative to a geoid undulation. The two fields are
the same information filtered differently.

**(d)** With $\gamma\approx9.8$ m s$^{-2}$ and $a = 6.378\times10^6$ m,
$\gamma/a = 1.5365\times10^{-6}$ s$^{-2}$:

| $l$ | $\gamma(l-1)/a$ (s$^{-2}$) |
|---|---|
| $2$ | $1.537\times10^{-6}$ |
| $100$ | $1.521\times10^{-4}$ |

So degree $100$ contributes about $99$ times more to the gravity anomaly per unit
coefficient than degree $2$ does; a gravity map is a high-pass-filtered version of
the same information that a geoid map shows low-passed. Practically: a gravity survey
sees shallow, local structure; a geoid model sees the deep, broad structure; and
neither sees the other's signal well. Together they span the depth range, which is the
quantitative version of the "depth filter" remark in ★6.
