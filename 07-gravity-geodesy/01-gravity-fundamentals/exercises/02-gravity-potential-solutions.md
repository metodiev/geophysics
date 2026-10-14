# Solutions — 07-01-02 Gravitational Potential, Equipotentials and the Geoid

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Gravitational Potential, Equipotentials and the Geoid](../02-gravity-potential.md).

---

## ★1 — Potential and field of a point mass

$GM = 6.67430\times10^{-11}\times3.00\times10^{11} = 20.02290\
\mathrm{m^{3}\,s^{-2}}$.

$$r = 1000\ \mathrm{m}:\quad U = -\frac{20.02290}{1000}
= -2.002290\times10^{-2}\ \mathrm{m^{2}\,s^{-2}},$$

$$g = \frac{20.02290}{10^{6}} = 2.002290\times10^{-5}\
\mathrm{m\,s^{-2}} = 2.00229\ \mathrm{mGal}.$$

$$r = 3000\ \mathrm{m}:\quad U = -\frac{20.02290}{3000}
= -6.674300\times10^{-3}\ \mathrm{m^{2}\,s^{-2}},$$

$$g = \frac{20.02290}{9\times10^{6}} = 2.224767\times10^{-6}\
\mathrm{m\,s^{-2}} = 0.222477\ \mathrm{mGal}.$$

**Units.** $U$ is energy per unit mass: $\mathrm{m^{2}\,s^{-2}}$. $g$ is an
acceleration: $\mathrm{m\,s^{-2}}$. The ratio $U/g$ has units of length, and here
it equals $r$ exactly: $2.002290\times10^{-2}/2.002290\times10^{-5} = 1000\
\mathrm{m}$. ✔

---

## ★2 — The Laplacian of $-GM/r$

Write $r = \left(x^{2}+y^{2}+z^{2}\right)^{1/2}$ and use
$\partial r/\partial x = x/r$. Then

$$\frac{\partial U}{\partial x} = \frac{GM x}{r^{3}},$$

$$\frac{\partial^{2}U}{\partial x^{2}} = \frac{GM}{r^{3}}
- \frac{3GM x^{2}}{r^{5}}
= \frac{GM}{r^{3}}\left(1 - \frac{3x^{2}}{r^{2}}\right).$$

Summing the three axes:

$$\nabla^{2}U = \frac{GM}{r^{3}}\left[
3 - \frac{3\left(x^{2}+y^{2}+z^{2}\right)}{r^{2}}\right]
= \frac{GM}{r^{3}}\left(3 - 3\right) = 0 \qquad (r \neq 0).$$

**Which equation.** $\nabla^{2}U = 4\pi G\rho$ with $\rho = 0$ at every point
except the origin: this is Laplace's equation, with the whole of the mass
concentrated in a measure-zero set. A rigorous treatment recovers the missing
$4\pi GM\delta(\mathbf{r})$ from the flux through a small sphere. Physically:
outside a mass the potential is harmonic.

---

## ★3 — Uniform sphere in scale-free units

Interior potential at $r = 0.5$, $R = 1$, $M = 1$:

$$U(0.5) = -\frac{1\cdot1}{2\cdot1^{3}}\left(3 - 0.25\right) = -1.375.$$

Interior field: $g = GMr/R^{3} = 0.5$; expressed as $-dU/dr$:
$\mathrm{d}U/\mathrm{d}r = GMr/R^{3}$ from the interior formula, so
$g = -\mathrm{d}U/\mathrm{d}r = -0.5$ in vector terms and $0.5$ in magnitude;
the sign difference is the convention that the field points inwards.

**Poisson check.** $U = -\tfrac{M}{2R^{3}}\left(3R^{2}-r^{2}\right)
= -\tfrac{3}{2} + \tfrac12\left(x^{2}+y^{2}+z^{2}\right)$, so each second
derivative is $\partial^{2}U/\partial x^{2} = +1$ and

$$\nabla^{2}U = 3 = 4\pi G\rho, \qquad
\rho = \frac{M}{\tfrac43\pi R^{3}} = 0.238732.$$

**Centre values.** $U(0) = -\tfrac{3}{2}$ against $U(1) = -1$: the centre value is
$1.5\times$ the surface value, the same factor the demonstration reports
($-9.384722\times10^{7}$ against $-6.256482\times10^{7}\
\mathrm{m^{2}\,s^{-2}}$).

---

## ★★4 — Mass excess: potential, anomaly, geoid

$GM = 6.67430\times10^{-11}\times8.00\times10^{11} = 53.39440\
\mathrm{m^{3}\,s^{-2}}$.

**(a) Potential** directly above the centre ($z = 2000\ \mathrm{m}$):

$$U_{\text{anom}} = \frac{GM}{z} = \frac{53.39440}{2000}
= 2.669720\times10^{-2}\ \mathrm{m^{2}\,s^{-2}}.$$

(The physical potential of the excess is $-2.669720\times10^{-2}$; the geoid is
raised for a mass excess, so the magnitude is what enters $N$.)

**(b) Gravity anomaly:**

$$\Delta g = \frac{GM}{z^{2}} = \frac{53.39440}{4.000000\times10^{6}}
= 1.334860\times10^{-5}\ \mathrm{m\,s^{-2}} = 1.334860\ \mathrm{mGal}.$$

**(c) Geoid undulation:**

$$N = \frac{\left|U_{\text{anom}}\right|}{\gamma}
= \frac{2.669720\times10^{-2}}{9.820250}
= 2.718587\times10^{-3}\ \mathrm{m} = 2.7186\ \mathrm{mm}.$$

**(d) Identity check:**

$$\frac{N}{\Delta g} = \frac{2.718587\times10^{-3}}{1.334860\times10^{-5}}
= 203.66\ \mathrm{m\ per\ m\,s^{-2}}, \qquad
\frac{z}{\gamma} = \frac{2000}{9.820250} = 203.66\ \mathrm{m\ per\ m\,s^{-2}}. ✔$$

The identity $N/\Delta g = z/\gamma$ holds for a point mass because
$N = (GM/z)/\gamma$ and $\Delta g = GM/z^{2}$; it is a quick numerical check that
the two computations used the same geometry.

---

## ★★5 — A fast-rotating synthetic planet

**(a) Rotation parameter.**

$$m = \frac{\omega^{2}a^{2}b}{GM}
= \frac{\left(3.64606\times10^{-4}\right)^{2}\times\left(6.378137\times10^{6}
\right)^{2}\times6.356752\times10^{6}}{3.986004418\times10^{14}}
= 8.62447\times10^{-2}.$$

(Equivalently $25\times$ the Earth's $m = 3.449786507\times10^{-3}$.)

**(b) Flattening and $J_2$** with the uniform-fluid result $f = \tfrac54 m$:

$$f = 1.25\times8.62447\times10^{-2} = 1.07806\times10^{-1},$$

$$J_2 = \tfrac23 f - \tfrac13 m
= 7.18705\times10^{-2} - 2.87482\times10^{-2} = 4.31223\times10^{-2}.$$

**(c) Are the relations trustworthy?** No. The relations are first-order in $f$
and $m$; here $f = 0.108$ and $m = 0.086$, so the "small" parameters are of order
$0.1$ and the neglected terms are of order $f^{2} \approx 10^{-2}$ — comparable to
the difference between the two terms being subtracted. The numbers above are
order-of-magnitude illustrations. This is the honest boundary of the regime, and
it is why the real Earth ($f = 3.35\times10^{-3}$) is comfortably inside it while
a fast rotator is not.

**Density-concentration caveat.** Even at small $f$, $f = \tfrac54 m$ holds only
for a *uniform* body. The Earth's ratio of measured flattening to the
uniform-fluid value is
$3.352811\times10^{-3}/(1.25\times3.449787\times10^{-3}) = 0.777$: the Earth is
much less flattened than a uniform fluid at the same rotation rate. That is the
signature of central condensation — mass concentrated towards the centre is
harder to deform.

---

## ★★6 — Depth sensitivity of the anomaly and of the geoid

$GM$ for the sphere: $M = 2670\times\tfrac43\pi\left(500\right)^{3}
= 1.398009\times10^{12}\ \mathrm{kg}$, so $GM = 93.3057\
\mathrm{m^{3}\,s^{-2}}$.

| centre depth $z$ | $\Delta g$ (mGal) | $N$ (mm) |
|---|---|---|
| 800 m | 14.5793 | 11.8769 |
| 1600 m | 3.6448 | 5.9384 |

**Factors:** $\Delta g$ falls by $14.5793/3.6448 = 4.00$; $N$ falls by
$11.8769/5.9384 = 2.00$.

**What the difference means.** Doubling the depth halves the potential
($U \propto 1/z$) but quarters the field ($\Delta g \propto 1/z^{2}$). The geoid
therefore retains deep structure that the anomaly has already lost: the geoid is
dominated by long wavelengths (deep, broad sources) and the anomaly by shorter
ones. This is the quantitative reason why satellite geoid models and terrestrial
gravity anomalies are complementary data sets, and why "the anomaly is large" and
"the geoid is high" are independent statements.

---

## ★★★7 — Level-surface residual versus truncation order (specification)

**Potential.** Use the axisymmetric exterior expansion

$$W(r,\varphi) = \frac{GM}{r}\left[1 - \sum_{k\ge1}
J_{2k}\left(\frac{a}{r}\right)^{2k}P_{2k}(\sin\varphi)\right]
+ \tfrac12\omega^{2}r^{2}\cos^{2}\varphi,$$

and form partial sums $K = 1, 2, 3, \dots$ harmonics. The $J_{2k}$ are *not* free:
they are fixed by requiring the spheroid to be a level surface, which is the same
condition that defects the residual — so the experiment must state which set is
being used (fitted to the level-surface condition, or taken from an external
model) and the answer depends on that choice.

**Sampling.** The ellipsoid surface $r(\varphi)$ at, say, $200$ equally spaced
geodetic latitudes, excluding the poles if the parameterisation degenerates there.

**Residual metric.**

$$\varepsilon(K) = \frac{\max_{\varphi}W_{K}(\varphi) -
\min_{\varphi}W_{K}(\varphi)}{\left|W_{K}\right|_{\text{mean}}},$$

i.e. the relative spread of $W$ on the surface. Also report the equivalent height
$\varepsilon\,GM/(a\gamma_{e})$ so the number has a geodetic meaning.

**Expected scaling.** With the coefficients determined by the level-surface
condition order by order, the residual should fall by a factor of the order of
$f^{2} \approx 10^{-5}$ for each additional pair of harmonics — the natural
expansion parameter is $f$, not $f^{2}$, when only $J_2$ is retained, which is why
the lesson's one-harmonic residual is $3.46\times10^{-3}$.

**Arithmetic check.** Re-run with the sampling doubled and with a higher-precision
summation. If $\varepsilon$ changes proportionally to $N_{\text{samples}}^{-1}$ the
result was limited by the sampling; if it does not change, the residual is physical
truncation. Only then is the scaling statement about the theory.

---

## ★★★8 — Identical exterior potentials from different interiors

**Family.** Let a spherically symmetric body have any radial density profile
$\rho(r)$ with the same total mass $M$ and the same outer radius $R$. Decompose it
into concentric shells of thickness $\mathrm{d}r$. By the shell theorem each shell
of mass $\mathrm{d}M$ contributes exactly $\mathrm{d}M/r$ to the exterior
potential at radius $r_{\text{obs}} > R$, independent of the shell's radius. Hence

$$U_{\text{ext}}(r_{\text{obs}}) = -\frac{G}{r_{\text{obs}}}
\int_{0}^{R}4\pi r^{2}\rho(r)\,\mathrm{d}r = -\frac{GM}{r_{\text{obs}}},$$

**identical for every profile**. At the first interior radius the profiles do
differ: an observation inside the body sees only the mass interior to it, so the
interior potential *does* discriminate. Numerically this is the same computation
as the shell theorem check in
[lesson 01](../01-newtonian-gravity.md), where the exterior field equals $GM/r^{2}$ to
7 significant figures and the interior residual falls as the point set is
refined.

**What the exterior potential determines.** For an isolated, static body, the
exterior potential determines the entire multipole sequence: total mass (the
monopole), the centre of mass (the dipole, which can be set to zero by choosing the
origin), and then the quadrupole, octupole, … of the mass distribution. It does
**not** determine the radial distribution at all — a point mass, a uniform sphere
and a shell of the same total mass are indistinguishable from outside.

**Consequence.** A gravity survey can recover the mass moment sequence of a body,
never its density distribution without additional information (seismic velocities,
petrophysics, drilling). Any reported "density model" from gravity alone is one
member of an equivalence class, and the class must be stated — the theme developed
in module [03](../../03-gravity-anomalies-and-modelling/README.md).

---

## ★★★9 — Conventions in a modernised vertical datum

**Conventions that must be fixed.**

1. **The reference potential $W_{0}$** that defines the zero-height surface. Two
   models with different $W_{0}$ differ by a constant offset of order tens of
   centimetres, which is larger than the precision of modern levelling.
2. **The tide system** (conventional tide-free, mean tide, zero tide). Converting
   between tide systems changes geoid heights at the level of tens of centimetres,
   and mixing them produces systematic inconsistencies between satellite-derived
   and terrestrial geoid models.
3. **The ellipsoid and frame** in which ellipsoidal heights are expressed
   (including its epoch and realisation), because $H = h - N$ mixes an ellipsoidal
   height, a geoid height and an orthometric height, each in its own frame.
4. **The height type** (orthometric, normal, dynamic), which changes how the
   geopotential number is converted to a metric length and therefore changes the
   numbers without changing the physics.

**What stays arbitrary.** The absolute value of $W_{0}$ cannot be measured; only
differences of potential are observable. Consequently the datum's *shape* is
determined by data and its *level* by agreement. Equally, the choice among height
types is a convention, not a measurement.

**Detecting a mismatched reference potential.** Compare a model's value with an
independent determination at the same point: a single constant offset across a
network indicates a different $W_{0}$ (or a different tide system), whereas a
spatially varying difference indicates a genuine model discrepancy or a datum
distortion. A constant offset is therefore diagnosable with a small number of
well-connected stations, and estimating it as one extra parameter in a
least-squares adjustment is the standard remedy.
