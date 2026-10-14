# Solutions — 13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. $g = 9.81\ \mathrm{m\,s^{-2}}$,
> $1\ \mathrm{yr} = 3.1557\times10^{7}\ \mathrm{s}$,
> $1\ \mathrm{Myr} = 3.1557\times10^{13}\ \mathrm{s}$.

Lesson: [04 Subduction Dynamics](../04-subduction-dynamics.md).

---

## ★1 — Slab pull

For a uniform mean anomaly the force per unit trench length is
$F = g\,\overline{\Delta\rho}\,h\,L$:

$$F = (9.81)(50)(6\times10^{4})(5\times10^{5})
= (9.81)(50)(3\times10^{10})
= 1.4715\times10^{13}\ \mathrm{N\,m^{-1}} = 14.72\ \mathrm{TN\,m^{-1}} .$$

(With the $\mathrm{erf}$ thermal profile the same $h$ and $L$ give
$31.77\ \mathrm{TN\,m^{-1}}$ at $t = 100$ Myr and
$\langle\Delta\rho\rangle = 80.96\ \mathrm{kg\,m^{-3}}$; a uniform 50
kg m$^{-3}$ slab is therefore a *conservative* representation — the real profile
is bottom-heavy in its cold part, as the lesson shows.)

---

## ★2 — Sinking speed

$$u = \frac{\overline{\Delta\rho}\,g\,h^{2}}{2\eta}
= \frac{(50)(9.81)(6\times10^{4})^{2}}{2(5\times10^{20})}
= \frac{1.766\times10^{12}}{10^{21}}
= 1.766\times10^{-9}\ \mathrm{m\,s^{-1}},$$

$$u = 1.766\times10^{-9}\times3.1557\times10^{7}\times10^{3}
= 55.72\ \mathrm{mm\,yr^{-1}},$$

$$t_{660} = \frac{6.6\times10^{5}}{1.766\times10^{-9}}
= 3.737\times10^{14}\ \mathrm{s} = 11.84\ \mathrm{Myr} .$$

Note the factor of two in the drag: a slab is pulled on both faces. Omitting it
halves the inferred time to the transition zone.

---

## ★3 — Rigidity and bending length

$$D = \frac{E T_e^{3}}{12(1-\nu^{2})}
= \frac{(7\times10^{10})(2\times10^{4})^{3}}{11.25}
= 4.9778\times10^{22}\ \mathrm{N\,m},$$

$$q = \overline{\Delta\rho}\,g\,h = (50)(9.81)(6\times10^{4})
= 2.943\times10^{7}\ \mathrm{Pa},$$

$$l_b = \left(\frac{2D}{q}\right)^{1/3}
= \left(\frac{2\times4.9778\times10^{22}}{2.943\times10^{7}}\right)^{1/3}
= \left(3.382\times10^{15}\right)^{1/3}
= 1.501\times10^{5}\ \mathrm{m} = 150.1\ \mathrm{km} .$$

**Unit:** $D/q$ has units $\mathrm{N\,m}/\mathrm{Pa} = \mathrm{N\,m}/
(\mathrm{N\,m^{-2}}) = \mathrm{m^{3}}$, so the cube root is a length. ✔ The
bending length is comparable to the slab thickness — which is the reason slabs
curve on the scale of a few hundred rather than a few tens of kilometres.

---

## ★★4 — The elastic core

Solving $\sigma_y = E\,y/R$ for the half-thickness $y$ that reaches yield at
radius $R$, and doubling for the core thickness:

$$h_{el} = 2y = \frac{2\sigma_y R}{E}
= \frac{2(5\times10^{8})(2.5\times10^{5})}{7\times10^{10}}
= 3.571\times10^{3}\ \mathrm{m} = 3.57\ \mathrm{km}.$$

**Comparison:** the elastic core is 3.57 km against a slab thickness of 60 km — a
factor of 17 smaller. **Implication:** a model that treats a subducting slab as a
thick elastic plate is wrong by more than an order of magnitude in the quantity
that controls bending. The physical picture is a thin elastic shell, capable of
transmitting the large deviatoric stresses that carry slab pull along its length,
wrapped around an interior that yields and flows at the bend. This is why flexural
rigidity estimated from slab curvature is not simply
$D=E h^{3}/12(1-\nu^{2})$ with $h$ the slab thickness.

---

## ★★5 — Force balance and plate speed

$$F_{\text{net}} = |F_{SP}| + |F_{RP}| = 14.72 + 4.11
= 18.83\ \mathrm{TN\,m^{-1}} = 1.883\times10^{13}\ \mathrm{N\,m^{-1}},$$

$$u = \frac{F_{\text{net}}d}{\eta L_p}
= \frac{(1.883\times10^{13})(2\times10^{5})}{(10^{21})(5\times10^{6})}
= \frac{3.766\times10^{18}}{5\times10^{27}}
= 7.532\times10^{-10}\ \mathrm{m\,s^{-1}} = 23.76\ \mathrm{mm\,yr^{-1}} .$$

**Sensitivity.** $u = F_{\text{net}}d/(\eta L_p)$ is a product of powers, so the
*same* fractional error in any input gives the same fractional error in $u$: all
four enter with exponent $\pm1$. The viscosity is nevertheless the dominant
practical uncertainty, because it is the only one of the four that plausibly
varies by an order of magnitude between plates (and because it is inferred, not
measured). The slab thickness and the density anomaly enter only through the
driving force and are constrained to tens of per cent.

---

## ★★6 — Equilibration time and depth

$$t_{\text{eq}} = \frac{(h/2)^{2}}{\kappa}
= \frac{(3\times10^{4})^{2}}{10^{-6}}
= 9\times10^{14}\ \mathrm{s} = 2.85\times10^{7}\ \mathrm{yr} = 28.5\ \mathrm{Myr},$$

$$\text{depth} = u\,t_{\text{eq}}
= (70\times10^{-3}/3.1557\times10^{7})(9\times10^{14})
= 1.996\times10^{6}\ \mathrm{m} = 1996\ \mathrm{km}.$$

At 70 mm/yr the slab's anomaly would survive to about 2000 km — well below
1500 km. **Conclusion:** the slab should be seismically detectable at 1500 km
depth, and its fast anomaly there is the expected consequence of its own thermal
inertia rather than evidence for unusually deep subduction. Note how strongly this
depends on speed: at 20 mm/yr the same calculation gives 570 km, i.e. the anomaly
would be erased in the upper mantle, and at 140 mm/yr it would survive to
4000 km — deeper than the mantle. Because $t_{\text{eq}}\propto h^{2}$, the
result is also very sensitive to slab thickness, which is why estimates of
"how deep slabs stay cold" must state the thickness they assume.

---

## ★★★7 — Testing slab stagnation at 660 km

**Data.** (i) Seismic tomography of the transition-zone region, with resolution
stated; (ii) the depth distribution of deep earthquakes in the slab; (iii) the
trench-normal geometry of the slab from receiver functions or converted phases;
(iv) convergence rate and plate age as boundary conditions.

**Forward model.** A viscous sheet with a viscosity increase across 660 km
(a factor of 10–100) and a phase-change buoyancy (the negative Clapeyron slope
resists downward motion across the same boundary), descended from an assumed
trench geometry. Predict the slab's deflection and whether it folds, ponds or
passes.

**Diagnostic.** The slab's dip and its along-strike continuity across 660 km: a
measure of the "kink" and the accumulation of fast material in the transition
zone.

**Signatures.** *Pass-through:* a continuous, coherent fast anomaly with a dip
that resumes below 660 km, and no accumulation. *Stagnation:* a horizontal,
faster-than-average sheet lying near 660 km, with a decrease or sharp bend in dip
and locally thickened material above 660 km; the deeper mantle below is
unaffected.

**The trade-off.** A viscosity increase at 660 km and a phase-change buoyancy both
resist penetration, and both produce a deflection of similar amplitude; they are
not separable from slab geometry at a single trench. The separations are
(i) the *viscosity* increase also stiffens the surrounding mantle, changing the
trench migration and the rate of dip change, whereas the *buoyancy* acts only at
the interface; and (ii) the *buoyancy* is temperature-dependent through the
Clapeyron slope, so cold fast slabs are resisted more than warm slow ones at the
same geometry. A sample of trenches spanning a range of slab ages (hence
temperatures) at otherwise similar convergence rates is required to break the
trade-off.

---

## ★★★8 — Dip rate from rollback

With $\mathrm{d}\theta/\mathrm{d}t \approx v_r/L$ and $L = 5\times10^{5}$ m:

| $v_r$ (mm/yr) | $v_r$ (m/s) | $\mathrm{d}\theta/\mathrm{d}t$ (rad/Myr) | (deg/Myr) |
|---|---|---|---|
| 10 | $3.169\times10^{-10}$ | 0.0200 | 1.15 |
| 20 | $6.338\times10^{-10}$ | 0.0400 | 2.29 |
| 30 | $9.507\times10^{-10}$ | 0.0600 | 3.44 |

Conversion used: $1\ \mathrm{rad\,Myr^{-1}} = 3.1557\times10^{13}\ \mathrm{rad\,s^{-1}}$,
i.e. multiply the rate in $\mathrm{s^{-1}}$ by $3.1557\times10^{13}\times180/\pi$.

**Why the convergence rate does not appear.** The relation is pure geometry:
$\sin\theta = \text{depth}/L$ ties the dip to the ratio of the slab's reach to its
down-dip length, and it is the *trench position* and the *slab length* that change
with time. Convergence adds material to the slab and lengthens $L$, but at fixed
$L$ the dip changes only if the trench moves. Assuming the convergence rate sets
the dip is the classic kinematic fallacy.

**Breaking the degeneracy.** Rollback steepening and buoyancy-driven steepening
produce the same dip evolution, so dip alone cannot separate them. The
discriminating observations are (i) *trench migration*: rollback requires the
trench to move oceanward relative to the plate interior, which is observable in
GNSS-based plate reconstructions, whereas buoyancy-driven steepening pulls the
slab down without moving the trench; and (ii) *the slab's tip depth and
morphology*: a buoyancy-driven slab accelerates downward, deepening its tip,
while a rolling-back slab maintains its length with a shallow dip change. A joint
dataset of trench motion plus slab-tip depth through time — from a plate
reconstruction with well-constrained kinematics — is what makes the two
hypotheses testable rather than merely distinguishable in principle.
