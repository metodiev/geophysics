# Solutions — 04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — A two-layer mass, gravity and pressure

**(a)** The shell volume is
$$\frac{4\pi}{3}\left(R^3 - r^3\right) = \frac{4\pi}{3}\left(6.371^3 - 6.341^3\right)\times10^{18}
= 1.523\times10^{19}\ \text{m}^3 .$$
With $\rho = 2750$ kg/m³ the crustal mass is
$1.523\times10^{19} \times 2750 = 4.19\times10^{22}$ kg, which is 0.7 per cent of
the total Earth mass — a useful scale check, because the crust is thin and light
even though it is what we live on.

**(b)** $g = GM/R^2 = 6.674\times10^{-11} \times 5.9722\times10^{24}/(6.371\times10^6)^2
= 9.820$ m/s². The standard value 9.80665 m/s² is 0.14 per cent lower because
the Earth is not a sphere of radius 6371 km: the equatorial radius is larger and
the rotation contributes.

**(c)** $P = \rho g h = 2750 \times 9.81 \times 3.0\times10^4 = 8.09\times10^8$ Pa.

**(d)** $8.09\times10^8$ Pa $= 0.81$ GPa, close to the 0.8 GPa quoted in the
lesson. The depth at which $P = 1$ GPa at this density is
$1\times10^9/(2750\times9.81) = 37$ km.

---

## ★2 — Conversions and a modulus

**(a)** $13.7$ km/s $= 1.37\times10^4$ m/s.

**(b)** $5570$ kg/m³ $= 5.57$ g/cm³, using 1 g/cm³ = 1000 kg/m³.

**(c)** With SI units,
$$K = 5570\left[(1.37\times10^4)^2 - \tfrac43(7.3\times10^3)^2\right]
= 5570\left[1.877\times10^8 - 7.105\times10^7\right]
= 6.50\times10^{11}\ \text{Pa} = 650\ \text{GPa}.$$
A 650 GPa bulk modulus for lower-mantle material is the right order; a
perovskite-structured silicate at those pressures is extremely stiff.

**(d)** $K/\rho$ has units $\text{Pa}/(\text{kg/m}^3) =
\text{m}^2\text{s}^{-2}$, so $\sqrt{K/\rho}$ is in m/s. This is the reason a
velocity can be computed from a modulus and a density with no conversion factor.

---

## ★3 — The grazing ray

**(a)** $p = 3480/13.7 = 254.0$ s. The unit is seconds: $[r/v] =
\text{km}/(\text{km/s})$.

**(b)** $\sin\theta_\text{core} = 254.0 \times 8.0/3480 = 0.584$.

**(c)** Since $\sin\theta < 1$ the ray is transmitted, and the direction changes
from nearly horizontal (grazing) to 35.8° from the radial direction — i.e. it is
bent **away** from the boundary and steeply into the core. It therefore turns
deep inside the core and re-emerges much further away, leaving a gap between the
grazing distance and its own re-emergence distance. That gap is the P-wave
shadow.

**(d)** $\sin\theta_\text{core} = 254.0 \times 16.0/3480 = 1.168 > 1$, which has
no solution: the ray cannot be transmitted and is totally reflected back into
the mantle. There is then no core branch and no shadow, so direct P would be
observed continuously.

---

## ★4 — Moment of inertia

**(a)** Core mass: $\frac43\pi(3.48\times10^6)^3 \times 11000 = 1.94\times10^{24}$
kg. Mantle mass: $\frac43\pi[(6.371\times10^6)^3 - (3.48\times10^6)^3]\times4500
= 4.08\times10^{24}$ kg. Total $6.02\times10^{24}$ kg, 0.8 per cent above the
true value.

**(b)** With the closed form,
$$I = \frac{8\pi}{15}\left[\rho_c r_c^5 + \rho_m(R^5-r_c^5)\right]
= \frac{8\pi}{15}\left[11000(3.48\times10^6)^5 + 4500\left((6.371\times10^6)^5 - (3.48\times10^6)^5\right)\right]
= 8.46\times10^{37}\ \text{kg m}^2 .$$

**(c)** $I/(MR^2) = 8.46\times10^{37}/(6.02\times10^{24}\times(6.371\times10^6)^2)
= 0.3465$. The observed value is 0.3307, so the model is 4.8 per cent too high.

**(d)** The model is missing the **density gradient within the mantle**. A real
mantle runs from about 3300 kg/m³ at the top to 5570 kg/m³ at the base, so more
of its mass sits at small radii than a uniform 4500 kg/m³ layer puts there.
Concentrating mass toward the centre lowers $I/(MR^2)$, and the missing gradient
is exactly the deficit.

---

## ★5 — Central pressure

**(a)** $g_\text{CMB} = GM_c/r_c^2 = 6.674\times10^{-11}\times1.94\times10^{24}/
(3.48\times10^6)^2 = 10.69$ m/s².

**(b)** The mantle layer is 2891 km thick. With $g$ varying from 10.69 to
9.82 m/s², a mean of about 10.3 m/s² is a reasonable estimate, so
$\Delta P_m \approx 4500 \times 10.3 \times 2.891\times10^6 = 1.34\times10^{11}$
Pa $= 134$ GPa. This is the demo's computed core–mantle boundary pressure.

**(c)** For the core, $g$ falls from 10.69 m/s² at the CMB to 0 at the centre, so
a crude mean is about 5.3 m/s²:
$\Delta P_c \approx 11000 \times 5.3 \times 3.48\times10^6 = 2.03\times10^{11}$
Pa $= 203$ GPa.

**(d)** Total $= 134 + 203 = 337$ GPa, against the demo's 356.6 GPa. The 5 per
cent difference is the crude mean-$g$ approximation; the demo integrates
$\mathrm{d}P = -\rho g\,\mathrm{d}r$ properly. Both agree that the central
pressure is of order 350 GPa, which is the point of the estimate.

---

## ★6 — The constant-velocity shadow

**(a)** $p = 3480/7.3 = 476.7$ s, and
$$\Delta = 2\left[\arcsin(1) - \arcsin\!\left(\tfrac{3480}{6371}\right)\right]
= 2\left[90° - 33.11°\right] = 113.8° .$$

**(b)** The demo's twelve-node model gives 90.4° and the observation is ~103°.
The constant-velocity value, 113.8°, is 10.8° *above* the observation.

**(c)** It corresponds to the large-$\alpha$ end of the sweep — the limit in
which the velocity is nearly uniform through the mantle and rays are barely bent
back to the surface. The demo's $\alpha = 8$ row gives 111.3°, approaching the
analytical 113.8° as $\alpha$ grows. The two limits therefore **bracket** the
observation: a uniform mantle overestimates the shadow distance and the demo's
linear gradient underestimates it, so the observation requires a gradient
between them. That is the inversion the sweep performs.

---

## ★★★7 — Refining the model

**(a)–(c)** Adding a node with $v_s = 7.1$ km/s at $r = 3980$ km makes the
velocity gradient *steeper* in the deepest part of the mantle, which bends rays
back to the surface sooner and **reduces** $\Delta_S$. The value therefore moves
away from 103° and further below 90.4°, so the node as specified is the wrong
direction. To reach 103° the gradient must be made *weaker* through the deep
mantle — a nearly constant velocity from about 5000 km to the CMB, with the
increase concentrated higher up. A velocity of about 13.4 km/s at $r = 3980$ km
(a near-constant lower mantle) brings $\Delta_S$ to within a degree of 103°.

**(d)** No. A model with a free parameter tuned until it reproduces one
observation has been *fitted* to that observation, and it makes no prediction.
The test is whether the same model, with no further tuning, reproduces an
independent observation — the travel times of P and S at other distances, the
free oscillations, the gravity field, or the density from the moment of inertia.
Reference models are built to satisfy many observations at once for exactly this
reason.

---

## ★★★8 — The demo's output

**(a)** `model mass = 5.9528e+24 kg` against `TABULATED 5.9722e+24 kg`
(−0.3 per cent); `model surface gravity = 9.7884 m/s^2` against
`9.80665 m/s^2` (−0.2 per cent); `model moment-of-inertia factor = 0.3327`
against `0.3307` (+0.6 per cent).

**(b)** `10.508 m/s^2`. The dense core below the boundary pulls outward while the
light mantle above contributes little inward attraction at that radius, so $g$
peaks at the CMB.

**(c)** `134.6 GPa` at the core–mantle boundary (−1.0 per cent against 136.0),
`322.0 GPa` at the inner-core boundary (−2.1 per cent against 329.0) and
`356.6 GPa` at the centre.

**(d)** `Delta = 90.4 deg` and `T = 24.54 min`.

**(e)** Mantle ray: `Delta = 89.1 deg, T = 13.14 min`. Transmitted into the core,
turning at `r = 2329 km`: `Delta = 172.0 deg, T = 22.02 min`.

**(f)** $\alpha = 1$: 85.8°; $\alpha = 2$: 102.9°; $\alpha = 4$: 108.8°. The
closest to the observed 103° is $\alpha = 2$.

**(g)** The `TABULATED` rows — Earth mass, standard gravity, $I/(MR^2)$, the two
pressures and the two shadow-zone angles — are the independent observations. The
model values are all *computed* from the seven-layer table, and the five per cent
residuals are reported rather than hidden.

---

## ★★★9 — Sorting inputs by kind

| Input | Kind | How it could be tested |
|---|---|---|
| Earth radius 6371 km | Definition (a chosen mean radius) | Not testable; it is a convention. A different choice changes the numbers slightly and nothing else |
| Outer-core density | Assumption (nominal PREM value) | By requiring the model to reproduce the mass, the moment of inertia and the free-oscillation periods simultaneously |
| Sharpness of the core–mantle boundary | Measurement (it is sharp in seismological data, to within a few km) | Increasingly precise waveform modelling, and observations of reflections off the boundary |
| $v_s = 0$ in the outer core | Measurement (the S shadow) | A positive $v_s$ would produce arrivals inside the shadow; none are observed |
| Depth of the 660 km discontinuity | Measurement with a real range | Seismic tomography shows it to vary laterally by tens of km, so it is a measured, variable quantity rather than a fixed constant |

The first row is the interesting one. "The Earth's radius" is a *choice*: a
spherical Earth has one radius and a real Earth has many, so the number is a
convention adopted for convenience. Every model in this lesson depends on it,
and none of them is tested by it.
