# Solutions — 13-03-04 Basin Formation and Subsidence Modelling

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Basin Formation and Subsidence Modelling](../04-basin-geodynamics.md).

---

## ★1 — Backstripping two beds

The factor for each bed is $(\rho_m-\rho_i)/(\rho_m-\rho_w)$ with
$\rho_m-\rho_w = 2300$.

Upper bed: $(3330-2100)/2300 = 1230/2300 = 0.53478$; contribution
$0.53478\times0.8 = 0.42783\ \mathrm{km}$.

Lower bed: $(3330-2450)/2300 = 880/2300 = 0.38261$; contribution
$0.38261\times1.1 = 0.42087\ \mathrm{km}$.

$$
Y = d_w + 0.42783 + 0.42087 = 0.2 + 0.8487 = 1.049\ \mathrm{km}.
$$

The stage-1 value (upper bed only) is $0.2+0.428 = 0.628\ \mathrm{km}$, so the
tectonic subsidence grew from $0.63$ to $1.05\ \mathrm{km}$ between the two
horizons.

---

## ★2 — Limits

- $\rho_i \to \rho_w$: the factor tends to $1$ and the bed contributes its full
  thickness. Correct, because water replacing water is no change of load.
- $\rho_i \to \rho_m$: the factor tends to $0$ and the bed contributes nothing.
  Correct, because removing material as dense as the mantle it displaces does
  not change the isostatic balance.

---

## ★3 — Rigidity and flexural parameter, $T_e = 15\ \mathrm{km}$

$$
D = \frac{E T_e^{3}}{12(1-\nu^{2})}
= \frac{70\times10^{9}\times(1.5\times10^{4})^{3}}{12(1-0.0625)}
= \frac{70\times10^{9}\times3.375\times10^{12}}{11.25}
= 2.10\times10^{22}\ \mathrm{N\,m}.
$$

$$
\alpha = \left(\frac{4D}{\Delta\rho g}\right)^{1/4}
= \left(\frac{4\times2.10\times10^{22}}{2300\times9.81}\right)^{1/4}
= \left(3.723\times10^{18}\right)^{1/4} = 4.39\times10^{4}\ \mathrm{m}
= 43.9\ \mathrm{km}.
$$

Check against the lesson's values: $\alpha$ grows from $32.4\ \mathrm{km}$ at
$T_e = 10$ to $54.5\ \mathrm{km}$ at $T_e = 20$, and $43.9\ \mathrm{km}$ at
$15\ \mathrm{km}$ interpolates correctly (indeed
$15^{3/4}/10^{3/4} = 1.355$ and $32.4\times1.355 = 43.9$ ✔).

---

## ★4 — Building the beds

Post-rift subsidence of the model column (from the lesson's tables):
$S(0) = 3.118$, $S(20) = 3.676$, $S(40) = 4.050$, $S(60) = 4.300$,
$S(80) = 4.469\ \mathrm{km}$. Subtracting $S(0)$ and multiplying by
$2300/1130 = 2.0354$:

| $t$ (Myr) | $S(t)-S(0)$ (km) | $X(t)$ (km) |
|---|---|---|
| 0 | 0.000 | 0.000 |
| 20 | 0.558 | 1.135 |
| 40 | 0.932 | 1.897 |
| 60 | 1.182 | 2.406 |
| 80 | 1.351 | 2.750 |

Boundary depths measured down from the present surface are
$X(80) - X(t)$: $2.750$ (basement), $1.615$, $0.853$, $0.344$ (present).
Compare with the lesson's $1.616$, $0.854$, $0.343\ \mathrm{km}$ — agreement to
$1\ \mathrm{m}$, the difference being rounding in the table.

---

## ★5 — Backstrip with present densities versus a constant density

With the lesson's present densities ($2328$, $2151$, $1987$, $1851\ \mathrm
{kg\,m^{-3}}$) and thicknesses ($1.134$, $0.762$, $0.511$, $0.343\ \mathrm{km}$
from oldest to youngest — note the table's tops and bottoms are cumulative
depths, so the thickness of bed 1 is $2.750-1.616 = 1.134\ \mathrm{km}$), and
stripping **oldest first**:

| bed | $(\rho_m-\rho_i)/2300$ | $t$ (km) | contribution (km) | cumulative $Y$ (km) |
|---|---|---|---|---|
| 1 (80 Ma) | 0.4357 | 1.134 | 0.494 | 0.494 |
| 2 (60 Ma) | 0.5126 | 0.762 | 0.391 | 0.885 |
| 3 (40 Ma) | 0.5839 | 0.511 | 0.298 | 1.183 |
| 4 (20 Ma) | 0.6430 | 0.343 | 0.221 | 1.404 |

These are exactly curve B of the lesson ($0.494$, $0.885$, $1.183$, $1.404$ —
note that the third value coincides numerically with curve A).

With every density set to $2200$ the contributions are all
$(1130/2300)t = 0.4913t$: $0.557$, $0.932$, $1.183$, $1.351$ km, which is
curve A.

**Sign of the difference.** Curve B uses lower densities for the *upper* beds
($1851$ and $1987$ against $2200$) and higher for the *lower* beds ($2151$,
$2328$). A lower density means a bigger factor $(\rho_m-\rho_i)$ and therefore a
**larger** contribution per unit thickness, but those beds are also thinner
after compaction. The two effects nearly cancel for the shallow beds and the net
result at $80\ \mathrm{Ma}$ is B lower than A by $63\ \mathrm{m}$
($0.494$ against $0.557$). The physical reading: the deepest bed is the densest
and therefore buoyant-least, so representing it as a uniform $2200\
\mathrm{kg\,m^{-3}}$ overestimates its contribution.

---

## ★6 — Foreland depth and width

For the line-load solution, $w(0) = V_0\alpha^{3}/(8D)$ and the forebulge lies at
$\pi\alpha$. The distance from the depocentre to the forebulge is thus
$\pi\alpha$, so

$$
\alpha \approx \frac{90\ \mathrm{km}}{\pi} = 28.6\ \mathrm{km},
$$

and inverting $\alpha = (4D/\Delta\rho g)^{1/4}$:

$$
D = \frac{\alpha^{4}\Delta\rho g}{4}
= \frac{(2.86\times10^{4})^{4}\times2300\times9.81}{4}
= \frac{6.69\times10^{17}\times22563}{4} = 3.77\times10^{21}\ \mathrm{N\,m},
$$

$$
T_e = \left[\frac{12(1-\nu^{2})D}{E}\right]^{1/3}
= \left[\frac{11.25\times3.77\times10^{21}}{70\times10^{9}}\right]^{1/3}
= \left(6.06\times10^{11}\right)^{1/3} = 8.46\times10^{3}\ \mathrm{m}
= 8.5\ \mathrm{km}.
$$

**Assumptions.** (i) one line load rather than a distributed load over the thrust
belt, which overestimates the deflection near the load and shifts the measured
forebulge outward; (ii) the observed "depocentre to forebulge" distance equals
$\pi\alpha$, which assumes the depocentre is at the load's edge — in a real
basin it is displaced basinward; (iii) a constant $T_e$ and a purely elastic
response, ignoring viscous relaxation of the lower lithosphere. Quote
$T_e \approx 8$–$10\ \mathrm{km}$ with those caveats rather than a single digit.

---

## ★7 — $\beta$ from total subsidence alone

McKenzie closed form:
$S(60) - S(0) = [S(\infty)-S(0)][1-e^{-60/\tau}]$ with
$\tau = 50.17\ \mathrm{Myr}$, so
$1-e^{-1.196} = 1-0.3025 = 0.6975$ and

$$
S(\infty) - S(0) = \frac{2.4}{0.6975} = 3.441\ \mathrm{km}.
$$

The total subsidence splits as $S(0) = (1-1/\beta)(A-B)$ and
$S(\infty)-S(0)$ from the closed forms of
[13-03-02](../02-rift-and-breakup.md). The
thermal part for $\beta = 2$ is $1.695\ \mathrm{km}$; scaling approximately with
$(1-1/\beta)$:

$$
1.695\times\frac{1-1/\beta}{0.5} = 3.441
\ \Rightarrow\ 1-\frac{1}{\beta} = 0.5\times\frac{3.441}{1.695} = 1.015 .
$$

That is greater than one, which is impossible: **no $\beta$ explains
$2.4\ \mathrm{km}$ of post-rift subsidence at $60\ \mathrm{Myr}$ if
$\tau = 50.17\ \mathrm{Myr}$ is imposed.** *This is the correct answer*, and it is
a useful outcome: the data are inconsistent with the assumed $\tau$, so either
$\tau$ is wrong (a different $a$ or $\kappa$) or the basin is not a simple
McKenzie basin.

**Why it is sensitive to $\tau$:** with $\tau = 50\ \mathrm{Myr}$ and
$t = 60\ \mathrm{Myr}$, only $69.8\%$ of the equilibrium subsidence has occurred.
If instead $\tau = 25\ \mathrm{Myr}$, then $1-e^{-2.4} = 0.909$ and the required
amplitude is $2.4/0.909 = 2.64\ \mathrm{km}$. Since the amplitude scales as
$3.39\,(1-1/\beta)$ km for these parameters (it is $1.695\ \mathrm{km}$ at
$\beta = 2$), $1-1/\beta = 2.64/3.39 = 0.779$ and $\beta = 4.5$. The same
measured subsidence therefore demands $\beta = 4.5$ rather than "impossible"
depending only on $\tau$, which is exactly the trade-off measured in the
lesson's fitting exercise.

---

## ★8 — Flexural backstripping (specification)

**Equation.** Replace the local (Airy) balance with

$$
D\nabla^{4}w + (\rho_m - \rho_w)\,g\,w = q(x)
$$

where $q(x)$ is the **unloaded** sediment load distribution and $w$ the
deflection.

**Unknown.** The water depth $Y(x)$ (or equivalently the tectonic deflection)
as a function of position, after removing the sediment load; in practice the
problem is solved forward and iterated.

**Boundary conditions.** $w \to 0$ and $\nabla w \to 0$ far from the basin;
symmetry ($\mathrm dw/\mathrm dx = 0$) at an axis of symmetry if one exists.

**Extra parameters relative to local backstripping.** $D$ (equivalently $T_e$),
and therefore $E$, $\nu$; plus the along-strike and across-strike extent of the
load, because the solution is non-local.

**Observation that reveals inadequacy of local backstripping.** Two independent
tests: (i) the basin is narrower than about $4\alpha$
($\sim 200\ \mathrm{km}$ for $T_e = 20\ \mathrm{km}$), so flexural support must
matter; (ii) the gravity anomaly or the margin's flank uplift shows a forebulge
or peripheral bulge that local isostasy cannot produce. A third, weaker test:
local backstripping applied to a narrow basin systematically overestimates the
tectonic subsidence near the basin edges by an amount that grows as the basin
narrows.

---

## ★9 — Detecting a wrong compaction model (specification)

**The problem.** Backstrips A, B and C produce fits with residuals of
$1.9$, $3.8$ and $5.9\ \mathrm{m}$ and $\beta$ of $2.00$, $2.70$ and $3.35$. The
misfit cannot choose between them, so an external test is needed.

**Test 1: independent measurement of crustal thinning.** $\beta$ predicts the
present crustal thickness $t_{c0}/\beta$. For $t_{c0} = 35\ \mathrm{km}$,
$\beta = 2$ predicts $17.5\ \mathrm{km}$ while $\beta = 3.35$ predicts
$10.4\ \mathrm{km}$. Receiver functions can distinguish those two at a few
kilometres' accuracy
([06-08-01](../../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md)),
so a measured Moho depth decides the question.

**Test 2: independent measurement of the thermal state.** $\beta$ predicts the
lithospheric thinning and hence the heat flow and $\tau$; borehole heat flow,
or the depth of a maturity indicator, tests it.

**Test 3: physical consistency of the compaction model.** Measure porosity
directly (wireline density and sonic logs, core plugs) and check the assumed
$\phi(z)$ law in the actual lithologies. If the measured law differs materially
from the one assumed, the backstrip is biased by a computable amount.

**Falsification.** Test 1 fails if the seismological Moho is
$\sim 17.5\ \mathrm{km}$ (then the constant-density model was right) or if it is
$\sim 10\ \mathrm{km}$ (then the decompacted model was right). If neither, all
three models are wrong. Test 3 fails if the measured porosity law reproduces the
assumed one yet the seismic Moho disagrees with the backstrip prediction — that
would point to a failure of the thermal or isostatic model rather than of the
compaction model, and the two must then be separated by the heat-flow test.
