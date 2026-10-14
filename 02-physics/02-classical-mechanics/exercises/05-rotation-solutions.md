# Solutions — 02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum

> **Read this after attempting the exercises, not before.**
>
> All arithmetic was computed. $\omega_\oplus = 7.292\,115\times10^{-5}$ rad s⁻¹
> (defining), $I = 8.4699\times10^{37}$ kg m² for ★★6 (the two-layer model value
> derived in ★★5), $1\ \mathrm{yr} = 3.1557\times10^{7}$ s.

---

## ★1 — Moments of inertia of three shapes

**(a)** Disk: $I = \tfrac12mR^{2} = 0.5\times2\times0.09 = \mathbf{0.09\ kg\,m^{2}}$.

**(b)** Solid sphere: $I = \tfrac25mR^{2} = 0.4\times5\times0.04
= \mathbf{0.08\ kg\,m^{2}}$.

**(c)** Thin shell: $I = \tfrac23mR^{2} = 0.6667\times5\times0.04
= \mathbf{0.1333\ kg\,m^{2}}$.

**(d)** At the same $\omega$ the rotational energy is $\tfrac12I\omega^{2}$, so the
shell stores $0.1333/0.08 = \mathbf{1.667}$ times as much. Physically: the shell
has all its mass at the largest radius, so its $I/(MR^{2})$ is 2/3 against the
sphere's 2/5.

---

## ★2 — Rod and the parallel-axis theorem

**(a)** $I_{\text{cm}} = ML^{2}/12 = 3\times1.44/12 = \mathbf{0.36\ kg\,m^{2}}$.

**(b)** $I_{\text{end}} = I_{\text{cm}} + M(L/2)^{2} = 0.36 + 3\times0.36
= \mathbf{1.44\ kg\,m^{2}} = ML^{2}/3$ ✓ (exactly, as the theorem is an identity).

**(c)** $ML^{2}/12$ assumes a **thin** rod: all the mass on the axis line, with
negligible extent perpendicular to its length. For a stubby body (a brick, a
plate, a short cylinder) the true $I_{\text{cm}}$ is larger and the formula
underestimates it.

---

## ★3 — Torque and the disk

**(a)** $\alpha = \tau/I = 5/0.09 = \mathbf{55.556\ rad\,s^{-2}}$.

**(b)** From rest, $\omega = \alpha t = 55.556\times3 = \mathbf{166.67\ rad\,s^{-1}}$
(about 26.5 revolutions per second — unrealistically fast, which tells you the
torque is large for this small disk).

**(c)** $L = I\omega = 0.09\times166.67 = \mathbf{15.0\ kg\,m^{2}\,s^{-1}}$.

**(d)** $\tau = I\alpha$ requires (i) a **fixed axis** — the axis direction does
not change, so the vector character of $\boldsymbol{\omega}$ contributes nothing;
and (ii) a **rigid body**, so every element shares the same $\alpha$ and the
distances do not change. For a body free to reorient, Euler's equations (lesson
08) are required.

---

## ★4 — Rotation periods

**(a)** $T_{\text{sid}} = 2\pi/\omega_\oplus
= 2\pi/(7.292\,115\times10^{-5}) = \mathbf{86\,164.10\ s}$. It is not 86 400 s
because 86 400 s is the *mean solar* day, and during one solar day the Earth must
rotate slightly more than $2\pi$ to bring the Sun back to the same meridian: the
difference is one part in 365.24, i.e. the ratio 86 400/86 164.1 = 1.00274 =
$1 + 1/365.24$. (The year length used here is a nominal value; the exact
relationship depends on which year definition is used.)

**(b)** $\Delta\omega/\omega = -\Delta T/T$, so
$\Delta\omega = -\omega_\oplus(10^{-3}/86\,400) = \mathbf{-8.4402\times10^{-13}\ rad\,s^{-1}}$.
**Approximation involved:** the fractional change in the day is defined with
respect to the *solar* day (86 400 s) while $\omega$ is the *sidereal* rate; the
two differ by 0.274%, so the answer carries that relative error — irrelevant here
(where the numbers are quoted to a few digits) but worth stating, since it is the
kind of 0.3% that matters in LOD work.

---

## ★★5 — Two-layer Earth

**(a)** $M_c = \rho_c\tfrac43\pi r_c^{3} = 11\,000\times\tfrac43\pi(3.48\times10^{6})^{3}
= 1.9420\times10^{24}$ kg; the total mass (core plus uniform shell out to
6 371 km at 4500 kg m⁻³) is $6.0219\times10^{24}$ kg, so the core mass fraction is
$\mathbf{0.3225}$.

**(b)** $I_{\text{core}} = \tfrac25M_cr_c^{2} = 9.4067\times10^{36}$ kg m²;
$I_{\text{mantle}} = \tfrac{8\pi}{15}\rho_m(R^{5}-r_c^{5})
= 7.5292\times10^{37}$ kg m²; total
$I = \mathbf{8.4699\times10^{37}\ kg\,m^{2}}$.

**(c)** $I/(MR^{2}) = 8.4699\times10^{37}/(6.0219\times10^{24}\times(6.371\times10^{6})^{2})
= \mathbf{0.3465}$.

**(d)** The measured factor is **smaller**, which requires the density to increase
towards the centre of the core more steeply than the two-layer model does — i.e.
a dense inner core. The measured value is obtained from satellite gravity: the
$C_{20}$ coefficient supplies $C-A$, and combining it with the rotation rate and
with the free-precession period supplies the principal moments separately
([02-02-08](../08-rigid-body.md) §4.1). The current value and its uncertainty
should be taken from the geodetic literature and the IERS conventions.

---

## ★★6 — The Earth's spin

**(a)** $L = I\omega = 8.4699\times10^{37}\times7.292\,115\times10^{-5}
= \mathbf{6.1764\times10^{33}\ kg\,m^{2}\,s^{-1}}$;
$E = \tfrac12I\omega^{2} = \mathbf{2.2519\times10^{29}\ J}$.

**(b)** With $\Delta T = 10^{-3}$ s:
$\Delta\omega = -8.4402\times10^{-13}$ rad s⁻¹, so

$$\Delta L = I\Delta\omega = -7.1486\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}},
\qquad
\Delta E = I\omega\,\Delta\omega = -5.2128\times10^{21}\ \mathrm{J}.$$

**(c)** $\Gamma = |\Delta L|/\Delta t = 7.1486\times10^{25}/3.1557\times10^{7}
= \mathbf{2.2653\times10^{18}\ N\,m}$.

**(d)** $10^{6}\times6.371\times10^{6} = 6.371\times10^{12}$ N m — smaller by a
factor of $3.6\times10^{5}$. No point force can do it: the torque is a
*distributed* tidal torque acting over the entire planet, and the number is the
leverage the planet-scale dynamics has.

---

## ★★7 — Rolling race

**(a)** For rolling without slipping from a height $h$,
$v^{2} = 2gh/(1+I/(mR^{2}))$:

| body | $I/(mR^{2})$ | $v$ from 1 m (m/s) |
|---|---|---|
| solid sphere | 0.4 | 3.7455 |
| solid cylinder | 0.5 | 3.6185 |
| thin shell | 0.6667 | 3.4328 |

**(b)** Rotational share $= (I/mR^{2})/(1+I/mR^{2})$: 28.57%, 33.33%, 40.00%.

**(c)** The **solid sphere arrives first**, then the cylinder, then the shell.
The result does **not** depend on mass or radius: the factor $I/(mR^{2})$ is
dimensionless and depends only on the *shape*, and $m$ and $R$ cancel completely
in $v^{2} = 2gh/(1+kmR^{2}/mR^{2})$. This is the cleanest example in the module of
a dimensionless shape factor deciding a physical outcome.

---

## ★★8 — Radius of gyration

**(a)** $k = \sqrt{I/M}$, so $k/R = \sqrt{I/(MR^{2})}$: for a uniform sphere
$k = \sqrt{0.4}\,R = \mathbf{0.6325R}$; for a thin shell
$k = \sqrt{0.6667}\,R = \mathbf{0.8165R}$.

**(b)** The radius of gyration is the radius at which *all* the mass could be
placed (as a ring) to give the same $I$. The shell's larger $k$ just says that its
mass is already near the outside; the Earth's $k/R = \sqrt{0.3465} = 0.589$ for the
model, and smaller for the real Earth, says the mass is concentrated well inside
the outer radius.

**(c)** Knowing $I$ and $M$, the radius of gyration gives the *typical* distance
of mass from the rotation axis — a single number that characterises a whole
density profile. It is the natural summary for comparing planets, and it is what
makes $I/(MR^{2})$ a useful diagnostic rather than an abstract moment.

---

## ★★★9 — Interior inference from $I$

**(a)** Mean density from the handbook: $\approx 5514\ \mathrm{kg\,m^{-3}}$
(derived from mass and volume), roughly twice the 2700 kg m⁻³ of surface rock.
That comparison alone implies that the interior is much denser than the crust —
i.e. that the body is **differentiated** — without saying anything about where the
dense material sits.

**(b)** For a two-layer model (uniform core of density $\rho_c$ inside radius
$r_c$, uniform mantle $\rho_m$ out to $R$), the polar moment is

$$C = \frac{8\pi}{15}\left[\rho_cr_c^{5} + \rho_m\left(R^{5}-r_c^{5}\right)\right],
\qquad M = \frac{4\pi}{3}\left[\rho_cr_c^{3} +
\rho_m\left(R^{3}-r_c^{3}\right)\right],$$

so $C/(MR^{2})$ is a continuous function of $\rho_c$, $\rho_m$ and $r_c$. Its
bounds are **0.4** for a uniform body (set $\rho_c = \rho_m$, or $r_c\to0$) and
**arbitrarily close to 0** as the mass is concentrated at the centre
($r_c\to0$ with $\rho_c\to\infty$ at fixed $M$). Every value in $(0,0.4)$ is
therefore attainable, so the factor constrains the mass distribution without
determining it.

**(c)** Because $C/(MR^{2})$ is a single number and the two-layer family has (at
least) three adjustable parameters ($\rho_c$, $\rho_m$, $r_c$, with $M$ and $R$
fixed), the inversion is under-determined: a *smaller, denser* core and a *larger,
less dense* core can give the same factor. This is the null-space problem of
[01-06-08](../../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
appearing in a planetary context.

**(d)** Two further observables: (i) the **seismic $P$ and $S$ velocity profile**,
which supplies density jumps and mantle discontinuities and hence where the
composition changes; and (ii) the **free oscillation frequencies** of the Earth,
which are sensitive to the radial structure and are used to build reference
models. Either, combined with $I$, breaks much of the degeneracy.

---

## ★★★10 — Atmosphere–solid Earth angular momentum exchange

**(a)** The atmosphere and the solid Earth exert torques on each other through
surface friction and pressure (mountain) torques. If the *total* angular momentum
of the atmosphere plus solid Earth is conserved — which requires that torques from
outside the pair (the Sun, the Moon) and from other components (oceans,
cryosphere) be negligible over the interval considered — then
$\Delta L_{\text{atm}} = -\Delta L_{\text{solid}}$. The assumption is the
important part: over a season the tidal torque's contribution is small, but the
oceanic and hydrological terms are not always negligible, which is why a
"closure" check on the budget is itself a research result.

**(b)** $\Delta\omega_{\text{solid}} = -\Delta L/I = -10^{26}/8.4699\times10^{37}
= \mathbf{-1.1807\times10^{-12}\ rad\,s^{-1}}$.

**(c)** $\Delta T = -T\,\Delta\omega/\omega = 86\,400\times1.1807\times10^{-12}/
7.292\,115\times10^{-5} = \mathbf{+1.399\times10^{-3}\ s} = +1.4$ ms. A
millisecond-scale LOD signal is the size of the **seasonal** variation (the annual
and semi-annual terms), which is exactly what the physics predicts: it is a
seasonal redistribution of angular momentum, not a change in the Earth's total
angular momentum. (The current amplitude should be taken from IERS Earth
orientation series rather than from a textbook.)

**(d)** It is invisible in the secular trend because it *reverses* twice a year:
the atmosphere takes angular momentum and gives it back, so the time-averaged
contribution to the trend is near zero, while its instantaneous amplitude is the
largest periodic term. The secular trend (the tidal despinning) is far smaller
per year but accumulates monotonically, which is why the two are separated by
fitting, not by eye.
