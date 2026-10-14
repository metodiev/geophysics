# Solutions — 02-11-01 Pressure, Density and Gravity Inside the Earth

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Every interior density is a **nominal**
> characteristic of a reference model; $G$ is **measured**; $GM_\oplus$ and the
> standard atmosphere are **exact**.

---

## ★1 — The constant-density sphere

**(a)** With constant $\rho_0$,
$M(r) = \tfrac43\pi r^3\rho_0$, so
$g(r) = GM(r)/r^2 = \tfrac43\pi G\rho_0 r$ — linear in $r$, as it must be inside a
uniform shell.

**(b)** $\dfrac{\mathrm{d}P}{\mathrm{d}r} = -\rho_0 g
= -\tfrac43\pi G\rho_0^2 r$, so integrating from $r$ to $R$ with $P(R)=0$:

$$P(r) = \tfrac43\pi G\rho_0^2\int_r^R r'\,\mathrm{d}r'
= \tfrac23\pi G\rho_0^2\left(R^2-r^2\right).$$

**(c)** At $r=0$: $P_c = \tfrac23\pi G\rho_0^2R^2$ with
$\rho_0 = 5513$ kg m⁻³, $R = 6.371\times10^6$ m,
$G = 6.674\,30\times10^{-11}$ m³ kg⁻¹ s⁻²:

$$P_c = 2.0944\times6.6743\times10^{-11}\times(5513)^2\times(6.371\times10^6)^2
= 1.725\times10^{11}\ \text{Pa} = 172.5\ \text{GPa}.$$

The alternative form gives $0.1194\times GM^2/R^4 =
0.1194\times1444.8 = 172.5$ GPa ✓. The coefficient
$3/(8\pi) = 0.1194$ is the same number arrived at two ways.

**(d)** At $r = R/2$, $R^2-r^2 = \tfrac34R^2$, so
$P(R/2) = \tfrac34P_c = 129.3$ GPa. The ratio is exactly $3/4$ — a property of
the uniform sphere only.

---

## ★2 — The uniform sphere as a bound

**(a)** $GM^2/R^4 = 6.6743\times10^{-11}\times(5.972\times10^{24})^2
/(6.371\times10^6)^4 = 1.4448\times10^{12}$ Pa $= 1444.8$ GPa.

**(b)** $356.7/1444.8 = 0.2469$. That is **2.07 times** the uniform-sphere
coefficient 0.1194.

**(c)** The Earth's density must be concentrated toward the centre; a uniform
body of the same mass and radius would produce only 172.5 GPa. No seismology is
needed because both the mass and the radius are measured at the surface —
$M$ through the defining $GM_\oplus$, $R$ by geodesy — so the comparison is
between two surface quantities and one observation about the interior, namely
that it is centrally condensed.

---

## ★3 — The two-layer moment of inertia

**(a)** For $\alpha = 1$ every term in the fraction contains $\alpha=1$ and the
fraction reduces to $(1)/(1) = 1$, so $k = 0.4$ — a homogeneous body, however the
boundary is labelled. For $f=0$, $f^3 = f^5 = 0$ and the fraction is again 1:
a core of zero radius changes nothing. Both are geometric, not physical.

**(b)** $f=0.5$: $f^3 = 0.125$, $f^5 = 0.03125$,
$k = 0.4(0.03125\times3 + 0.96875)/(0.125\times3 + 0.875)
= 0.4\times1.0625/1.25 = 0.34$.

**(c)** $0.34 = 0.4(0.03125\alpha + 0.96875)/(0.125\alpha+0.875)$ gives
$0.34(0.125\alpha+0.875) = 0.4(0.03125\alpha+0.96875)$, i.e.
$0.0425\alpha + 0.2975 = 0.0125\alpha + 0.3875$, so
$\alpha = 0.09/0.03 = 3.0$.

**(d)** With $\alpha=3$ and the mass constraint, $\rho_m$ comes out near
$4200$ kg m⁻³ and $\rho_c$ near $12\,600$ kg m⁻³ — inside the handbook's plausible
core range of 9900–13 100 kg m⁻³. So yes, credible.

---

## ★4 — Mass, moment of inertia and core gravity

**(a)** $f = 3480/6371 = 0.54621$, $f^3 = 0.162\,997$,
$\alpha = 12\,576/4138 = 3.0391$, so
$S = f^3\alpha + 1 - f^3 = 0.495\,36 + 0.837\,00 = 1.332\,36$.
With $\tfrac43\pi R^3 = 1.083\,21\times10^{21}$ m³,
$M = 1.083\,21\times10^{21}\times4138\times1.332\,36
= 5.97\times10^{24}$ kg ✓ against the nominal $5.972\times10^{24}$ kg.

**(b)** $f^5 = 0.048\,651$,
$k = 0.4(0.048\,651\times3.0391 + 0.951\,349)/1.332\,36
= 0.4\times1.099\,21/1.332\,36 = 0.3300$.

**(c)** $M_c = \tfrac43\pi(3.480\times10^6)^3\times12\,576
= 1.9508\times10^{24}$ kg, so
$g = 6.6743\times10^{-11}\times1.9508\times10^{24}/(3.480\times10^6)^2
= 10.75$ m/s², against the layered model's **10.51** m/s².

**(d)** The two-layer core is *too massive at the top*: it holds all its mass at
12 576 kg m⁻³ right up to $r_c$, whereas the real outer core is only about
9900 kg m⁻³ there. A heavier shell at the CMB raises the enclosed mass, hence
$g$, at that radius. The 2.3 per cent excess is precisely the error made by
smearing the core's density gradient.

---

## ★5 — Adams–Williamson at the Moho

**(a)** $\phi = 8.1^2 - \tfrac43(4.5)^2 = 65.61 - 27.00
= 38.61$ km² s⁻² $= 3.861\times10^7$ m² s⁻².

**(b)** $\dfrac{\rho g}{\phi} = \dfrac{3300\times9.81}{3.861\times10^7}
= 8.38\times10^{-4}$ kg m⁻³ m⁻¹, i.e. **0.838 kg m⁻³ km⁻¹**.

**(c)** Ratio $= 0.838/0.80 = 1.05$. The observed density increase across the
upper mantle is within 5 per cent of what adiabatic self-compression of a
homogeneous layer would give — so the upper mantle's density gradient is
essentially explained by compression, with a small residual that the rounding of
the densities makes meaningless.

**(d)** The two assumptions are (i) the layer is chemically homogeneous, and
(ii) the compression is adiabatic (isentropic). Both are reasonable for a
convecting upper mantle over this interval; the failure mode appears in the
transition zone, where phase changes violate homogeneity.

---

## ★6 — The two-layer family from $M$ and $k$

**(a)–(b)** Solving $k=0.33$ for $\alpha$ at each $f$, then
$\rho_m = M/(\tfrac43\pi R^3 S)$ with $S = f^3\alpha+1-f^3$:

| $f$ | $\alpha$ | $\rho_m$ (kg m⁻³) | $\rho_c$ (kg m⁻³) |
|---|---|---|---|
| 0.50 | 3.4348 | 4226.8 | 14 518 |
| 0.53 | 3.1604 | 4171.6 | 13 184 |
| 0.5462 | 3.0391 | 4138.2 | 12 577 |
| 0.55 | 3.0131 | 4130.0 | 12 444 |
| 0.60 | 2.7423 | 4005.7 | 10 985 |
| 0.65 | 2.5832 | 3842.6 | 9926 |
| 0.70 | 2.5230 | 3621.5 | 9137 |

**(c)** Requiring 9900 < $\rho_c$ < 13 100 kg m⁻³ gives
$0.53 \lesssim f \lesssim 0.65$. Both limits come from the same physics: too
small a core requires an implausibly dense core, too large a core requires an
implausibly light one.

**(d)** The seismic value 0.546 lies comfortably inside the permitted range but
is not *pinpointed* by it: the permitted band is $\pm11$ per cent wide in $f$,
which corresponds to $\pm25$ per cent in volume and much more in core mass. So the
combination of $M$ and $k$ establishes that a dense core exists and gives its
density to roughly 10 per cent, but a seismological length (or a third
independent constraint) is required to fix its size. This is the honest answer to
"how well do we know the core?" and it is why the Earth's core radius is quoted
from seismology, not from geodesy.

---

## ★7 — Central pressure of the two-layer models

**(a)** Using the formula given:

| Model | $P_{\text{core}}$ (GPa) | $P_{\text{mantle}}$ (GPa) | $P_c$ (GPa) |
|---|---|---|---|
| $f=0.5462$, $\alpha=3.039$ | 267.7 | 121.8 | **389.5** |
| $f=0.50$, $\alpha=3.435$ | 298.9 | 137.7 | **436.7** |

**(b)** Against the layered model's 356.7 GPa: the favoured model over-predicts
by 9.2 per cent, and the smaller-core model by 22.4 per cent.

**(c)** The pressure integrand is $\rho(r)g(r)$, and $g(r)$ at a given radius
depends on the mass *inside* that radius. Putting a given amount of core mass into
a smaller volume concentrates it deeper, but it also means the mantle above starts
at a smaller radius and carries more of the total mass at larger radii where $r^2$
weights the enclosed mass. The net effect of the smaller, denser core is a larger
$g$ through most of the mantle column and hence a larger integral.

**(d)** $M$, $R$ and $k$ *prefer* the $f = 0.5462$ model, and it is the one that
matches both the seismic core radius and the handbook's core densities. But the
preference is not logic: all four models in ★6 satisfy $M$ and $k$ exactly. The
constraints select the model only once the *plausible density range* is imposed.
That is the sense in which the two-layer fit is under-determined until an
independent physical bound is added.

---

## ★8 — The pressure at half the Earth's radius

**(a)** The demo gives $P = 145.90$ GPa at 3000 km and $240.74$ GPa at 4000 km,
so at 3185.5 km, $P \approx 145.90 + 0.1855\times(240.74-145.90) = 163.9$ GPa.
(An exact evaluation at the grid point nearest 3185.5 km gives **164.7** GPa; the
difference from the linear interpolation is the curvature of the profile.)

**(b)** For the uniform sphere of ★1(d) at the same radius, $P = 129.3$ GPa. The
ratio is $164.7/129.3 = \mathbf{1.27}$.

**(c)** $g \propto r$ for a uniform core, so from $g = 10.51$ m/s² at
$r = 3480$ km: $g = 10.51\times1218/3480 = 3.68$ m/s² at the inner-core boundary,
against the model's **4.39** m/s². The uniform-core assumption under-estimates $g$
there by 16 per cent.

**(d)** $g = GM(r)/r^2$ involves only the enclosed mass, so a deficit in $g$
relative to the uniform-core prediction is a deficit in the mass inside $r$ — and
since $r$ is known, it is a deficit in the mean density of the shell between the
inner-core boundary and the CMB relative to 11 050 kg m⁻³. In the model the outer
core's density rises from 9900 to 12 200 kg m⁻³, so the enclosed mass grows faster
than $r^3$ and $g$ falls more slowly than linearly. That is a measurement of the
outer core's density gradient by the same logic as Adams–Williamson.

---

## ★9 — Dimensional checks

**(a)** $GM^2/R^4$:
$\mathrm{m^3\,kg^{-1}\,s^{-2}}\cdot\mathrm{kg^2}/\mathrm{m^4}
= \mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{Pa}$ ✓.

**(b)** $\rho g/\phi$:
$\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}}/(\mathrm{m^2\,s^{-2}})
= \mathrm{kg\,m^{-4}} = \mathrm{kg\,m^{-3}\,m^{-1}}$ ✓. With $\phi$ in km² s⁻² it
must first be multiplied by $10^6$ to give m² s⁻²; then multiply the result by
$10^3$ to get kg m⁻³ km⁻¹.

**(c)** $GM^2/R^3$ has dimensions $\mathrm{kg\,m^{-1}\,s^{-2}}\times\mathrm{m}
= \mathrm{kg\,s^{-2}}$, which is not a pressure. Numerically it would be
$1444.8\ \text{GPa}\times R = 1444.8\times6.371\times10^6$ in the same working
units — a nonsense number, and the giveaway is that the units do not close.

**(d)** Converting per metre to per kilometre means *multiplying* by 1000, because
there are 1000 metres in a kilometre and a per-kilometre gradient is 1000 times
larger in number. The correct value is $8.4\times10^{-1}$ kg m⁻³ km⁻¹, i.e.
0.84 kg m⁻³ km⁻¹. Dividing by $10^3$ would give $8.4\times10^{-7}$, a thousand
times too small.

---

## ★★★10 — Verification of a hydrostatic integrator

**(a)** Two exact solutions, both integrable in closed form: the **uniform
sphere** ($M(r) = \tfrac43\pi r^3\rho_0$, $g = \tfrac43\pi G\rho_0 r$,
$P_c = 3GM^2/(8\pi R^4)$) and the **two-layer sphere** (analytic $P_c$ from
the core and mantle integrals of ★7). Measure the relative error in $P_c$ and the
error in the total mass, on grids of decreasing $\Delta r$.

**(b)** The uniform sphere's integrand is a smooth quadratic in the interior and
its quadrature error is correspondingly small; the two-layer profile has a
discontinuity in $\rho$ and $g$ at $r_c$ that the grid resolves differently
depending on whether a grid point lands on the boundary. Different profiles have
different error constants, so different errors at the same $\Delta r$ is the
expected outcome. Both are at the $10^{-4}$ level, consistent with a
$\Delta r = 500$ m step over $R \approx 6.4\times10^6$ m.

**(c)** Because $P(R) = 0$ is the only boundary condition available. Accumulating
outward has no boundary condition and produces a profile whose *value* depends on
an arbitrary integration constant, i.e. a pressure that is small at the centre and
largest at the surface — inverted, and unbounded above.

**(d)** Three candidates. (i) A wrong boundary condition (integrating outward, or
using $P(R) \ne 0$): the profile would be inverted or shifted. (ii) A $g$ array
computed from a mass array that was built with the wrong shell volume, e.g.
$\tfrac43\pi(r^3-r'^3)$ replaced by $4\pi r^2\Delta r$ inconsistently: the mass
would still integrate correctly only if the same error cancels, so check $g$
against the analytic uniform-sphere value. (iii) A unit error, e.g. $\Delta r$ in
kilometres in one loop and metres in the other: recognisable because the answer
would be wrong by a clean power of ten. The distinguishing test in every case is
comparison with the analytic uniform-sphere values of $g$ and $P$, to which the
integrator must converge as $\Delta r\to0$.

**(e)** The uniform-sphere test gives no information about how the integrator
handles a *discontinuity* in the integrand, since there is none. The two-layer
test supplies exactly that, and it is the reason both are used. More generally,
verification only tests the cases you construct: an integrator can pass both and
still be wrong for a profile whose shell-volume weighting differs.

---

## ★★★11 — Adams–Williamson as an inversion

**(a)** *Measured*: $v_p(r)$ and $v_s(r)$, hence $\phi(r)$; and either $g(r)$ or
$M(r)$. *Assumed*: the layer is chemically homogeneous and the compression is
adiabatic. *Integrated*: $\mathrm{d}\rho/\mathrm{d}z = \rho g/\phi$ downward from
a starting density. *Compared*: the resulting $\rho(r)$ with the density implied
by the mass, the moment of inertia and free oscillations. A ratio near 1 means
the assumptions hold; a departure measures the compositional or thermal
contribution.

**(b)** Upper mantle 1.11: the gradient is close to adiabatic self-compression,
slightly steeper than assumed; consistent with a homogeneous layer plus a weak
temperature effect. Transition zone 0.22: the gradient is four to five times
steeper than compression alone, because mineral phase changes add density without
pressure. Lower mantle 1.06: close to adiabatic, consistent with a well-mixed
convecting layer. Outer core 1.00: exactly adiabatic within the model's
resolution, the sharpest result of the table. Inner core 1.09: mildly less steep
than adiabatic, within the resolution of the rounded densities.

**(c)** The method is *designed* to detect departure from homogeneity, and the
transition zone is the one place where the departure is large and unambiguous. Its
failure there is the discovery that the mantle's density structure is set by
phase equilibria, not only by compression. A method that only confirmed its own
assumptions would be worth little.

**(d)** Because equation (7) is a first-order differential equation, its solution
is determined only up to the choice of starting density; any error in that anchor
propagates downward, and any error in $\phi$ accumulates. The anchor must come
from an integral constraint — the total mass (with the radius) and the moment of
inertia, or free-oscillation frequencies — which is insensitive to the *local*
profile and therefore complementary to the local differential relation.

**(e)** Because it would assume homogeneity across 660 km and 410 km
discontinuities, where the assumption fails by a factor of four. The arithmetic
would produce a number, but the number would be the integral of a differential
equation whose coefficients are wrong in exactly the interval where the physics
matters. This is the general hazard of applying a local constitutive relation
globally.

---

## ★★★12 — Inference with stated uncertainty

**(a)** Unknowns: $f$, $\alpha$, $\rho_m$ (three). Equations: the mass constraint
and the moment-of-inertia constraint (two). Under-determined: the solution set is
a **one-parameter family**, a curve in $(\alpha,\rho_m)$ for each $f$, exactly as
seen in ★6. A unique answer requires a third constraint, e.g. a seismological
core radius or a bound on the plausibility of $\rho_c$.

**(b)** Numerically at $(f,\alpha) = (0.5462, 3.0391)$:
$\partial k/\partial f = -0.1796$ per unit $f$ and
$\partial k/\partial\alpha = -0.02577$ per unit $\alpha$. The ratio is
$6.97$, so **$k$ is about seven times more sensitive to the core radius fraction
than to the density contrast.** Consequently a given uncertainty in $k$ maps into
a seven-times-smaller relative uncertainty in $\alpha$ than in $f$ — the density
contrast is comparatively well determined *once $f$ is known*, and $f$ is the
input that limits the inferred core density.

**(c)** With $f = 0.5462$ fixed, $k = 0.33$ gives $\alpha = 3.0391$ and
$\rho_c = 12\,577$ kg m⁻³; $k = 0.3308$ gives $\alpha = 3.0082$, $\rho_m = 4154$
kg m⁻³ and $\rho_c = 12\,496$ kg m⁻³. The shift is $-81$ kg m⁻³, or $-0.64$ per
cent. So the third digit of $k$ matters at the 1 per cent level in the core
density — small, but not negligible against the systematic uncertainty of the
two-layer assumption, which is of order 10 per cent.

**(d)** A defensible abstract sentence, using only computed numbers:

> A two-layer fit to the Earth's mass, radius and nominal moment-of-inertia factor
> $C/(MR^2) = 0.33$, holding the seismic core radius fraction at 0.546, implies a
> mean core density of $1.26\times10^4$ kg m⁻³ and a core/mantle density contrast
> of 3.04. Because the moment of inertia is seven times more sensitive to the core
> radius than to the density contrast, the density contrast is well determined
> only once the core radius is fixed independently; the two-layer assumption
> itself is the dominant systematic uncertainty.

Note what the statement does *not* do: it does not present $1.26\times10^4$
kg m⁻³ as a measurement, and it says which constraint is doing the work.
