# Solutions — 04-04-01 Stress, Strain and Brittle vs Ductile Deformation

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All material parameters are TYPICAL values.

---

## ★1 — A Mohr circle

**(a)** Centre $= (100 + 40)/2 = 70$ MPa; radius $= (100 - 40)/2 = 30$ MPa.

**(b)** From equation (4) of the lesson with $2\theta = 90^\circ$:
$\sigma_n = 70 + 30\cos 90^\circ = 70$ MPa and
$\tau = 30\sin 90^\circ = 30$ MPa.

**(c)** The maximum shear stress equals the radius, 30 MPa, attained at
$\theta = 45^\circ$.

**(d)** No. With friction present, the failure criterion penalises normal stress,
so the optimum is rotated towards the compressional axis: the plane of maximum
shear has the largest available shear stress *and* a non-negligible normal stress,
and shifting the plane towards $\sigma_1$ trades shear for normal stress
favourably. For $\mu = 0.85$ the optimum is at $\theta = 65.18^\circ$, not
$45^\circ$, as ★2 shows.

---

## ★2 — The optimum failure angle

**(a)** $\phi = \arctan 0.85 = 40.365^\circ$ (the demo prints
`phi = atan(mu) = 40.365 deg`).

**(b)** $\theta = 45^\circ + 40.365^\circ/2 = 65.18^\circ$, which the demo
confirms against a numerical search over $\theta$ with a difference of
`0.000122 deg`, i.e. the search grid spacing.

**(c)** The two conjugate planes are at $\pm 65.18^\circ$ from the $\sigma_3$
axis, so the acute angle between them is
$180^\circ - 2 \times 65.18^\circ = 49.63^\circ$, i.e. about $49.6^\circ$.

**(d)** Two sets, symmetric about $\sigma_1$, are equally favoured. In the field
they appear as an X pattern of conjugate faults whose acute bisector is parallel
to $\sigma_1$ — which is why measuring that angle at outcrop is a measurement of
$\phi$, and is one of the few predictions of the theory that is directly visible.

---

## ★3 — Stress at 5 km

**(a)** $S_v = \rho g z = 2700 \times 9.81 \times 5000 = 1.324 \times 10^8$ Pa
$= 132.4$ MPa, matching the demo's 5 km row.

**(b)** $P_f = 0.38 \times 132.4 = 50.3$ MPa.

**(c)** $S_v' = 132.4 - 50.3 = 82.1$ MPa, the demo's `82.1`.

**(d)** Failure. The pore pressure appears in the Coulomb criterion only through
the effective normal stress, and the total stress never enters except through it.
A change in pore pressure at fixed total stress changes the strength directly,
which is why overpressure can reactivate a fault at a differential stress far
below the rock's dry strength.

---

## ★4 — The closed form

**(a)** $\sqrt{1 + 0.85^2} = 1.312\,44$, so the denominator is
$1.312\,44 - 0.85 = 0.462\,44$ and
$\Delta\sigma = 2 \times 0.85 \times 100/0.462\,44 = 367.6$ MPa. The demo prints
`367.615` for this case.

**(b)** The numerical search agrees to $2.27 \times 10^{-13}$ MPa in the demo's
table, which is machine precision: the closed form is exact, and the search
confirms it rather than the other way round.

**(c)** At $\mu = 0.6$: $\sqrt{1.36} = 1.166\,19$, denominator
$0.566\,19$, so $\Delta\sigma = 2 \times 0.6 \times 100/0.566\,19 = 211.9$ MPa.
**Lower friction means lower strength**, which is the entire reason weak
minerals — clays, serpentine, evaporites — control fault behaviour in
sedimentary and subduction settings.

**(d)** On an existing fault surface the cohesive strength is destroyed by the
first slip event, so $C \approx 0$ is defensible for reactivation. Intact rock
has no through-going surface and exhibits a cohesive strength that has to be
overcome before a fault can form, so omitting $C$ for intact rock understates the
strength.

---

## ★5 — The two regimes

**(a)** With $\sigma_3' = S_v' - \Delta\sigma$ substituted into the closed form,

$$\Delta\sigma\left[\sqrt{1 + \mu^2} - \mu\right] = 2\mu\left(S_v' -
\Delta\sigma\right)$$

and collecting terms gives
$\Delta\sigma\left[\sqrt{1 + \mu^2} + \mu\right] = 2\mu S_v'$, hence
$\Delta\sigma_{\text{normal}} = 2\mu S_v'/[\sqrt{1+\mu^2}+\mu]$.

**(b)** Normal: $2 \times 0.85 \times 164.2/2.162\,44 = 129.1$ MPa. Reverse:
$2 \times 0.85 \times 164.2/0.462\,44 = 603.7$ MPa. Both match the demo's 10 km
row.

**(c)** The ratio is
$[\sqrt{1+\mu^2}+\mu]/[\sqrt{1+\mu^2}-\mu] = 2.162\,44/0.462\,44 = 4.676$, and
$\mu$ is its only argument. The demo prints `4.676` for every depth.

**(d)** Because in strike-slip faulting the vertical axis is the *intermediate*
principal stress, so the least principal stress is horizontal and the depth says
nothing about it. Depth alone therefore cannot give a strike-slip frictional
strength, and a statement that quotes one without stating the assumed horizontal
stress is incomplete.

---

## ★6 — The demo

**(a)** `located maximum of the Coulomb function: theta = 65.1824 deg` against
`analytic 45 deg + phi/2 ... theta = 65.1824 deg`, difference `0.000122 deg`.

**(b)** `200.0             735.230         735.230     4.55e-13` — the closed
form and the search agree to $4.6 \times 10^{-13}$ MPa.

**(c)** From the creep table: 165.7 MPa at 15 km and 18.9 MPa at 20 km. The
strength falls by a factor of nine over 5 km, which is the temperature sensitivity
of the flow law.

**(d)** 4.676.

---

## ★7 — The brittle–ductile transition

**(a)** `brittle-ductile transition at 12.37 km`, with
`friction strength there 746.9 MPa` and `creep strength there    746.9 MPa`. The
residual printed is the bisection tolerance, not a physical discrepancy.

**(b)** A geotherm of 20 °C km$^{-1}$ gives 15.08 km and one of
30 °C km$^{-1}$ gives 10.52 km. **A hotter geotherm shallows the transition**,
because the creep law's Arrhenius factor makes the rock weak at a smaller depth.

**(c)** $10^{-16}$ s$^{-1}$ gives 11.35 km and $10^{-14}$ s$^{-1}$ gives
13.49 km. **A faster strain rate deepens the transition**, because
$\sigma \propto \dot\varepsilon^{1/n}$: the rock must be stronger to sustain the
higher rate, and it only reaches that strength where friction has grown enough —
deeper down.

**(d)** $Q = 200$ kJ mol$^{-1}$ gives 10.20 km and 250 kJ mol$^{-1}$ gives
14.92 km: a 25 per cent change in $Q$ moves the transition by 4.7 km, whereas a
factor of 100 in strain rate moves it by 2.1 km. The reason is that the strain
rate enters as a power $\dot\varepsilon^{1/n}$, which is a gentle dependence,
whereas $Q$ enters inside an exponential. **Activation energy, not strain rate,
is the parameter a strength profile most needs to get right**, and it is also the
one most poorly known for natural rocks.

**(e)** The model has a single creep law and therefore a single transition. A
layered crust with a quartz-bearing layer over a feldspar-bearing one has two
crossovers and can have two seismogenic layers separated by a ductile zone, which
is observed in continental settings. Reproducing it requires running the
calculation with two flow laws and taking the minimum strength at each depth.

---

## ★8 — Simple shear

**(a)** $\det F = 1 \times 1 - \gamma \times 0 = 1$. The deformation preserves
area in the profile plane, and since plane strain also preserves the
out-of-plane dimension, it is volume-preserving: simple shear neither compacts
nor dilates. The demo's `area` column is exactly 1.000 at every $\gamma$.

**(b)** For $\gamma = 2$, $FF^{\mathsf T}$ has eigenvalues 2.618034 and 0.381966;
the square roots are the principal stretches 2.414214 and 0.414214, which the demo
prints. The closed form for $\gamma = 1$ is
$\sqrt{(3 \pm \sqrt5)/2}$, giving 1.618034 and 0.618034 — the golden ratio and its
reciprocal — and the demo confirms it.

**(c)** A marker initially along $(0,1)$ maps to $(\gamma, 1)$, so its angle from
the vertical is $\arctan\gamma$. For $\gamma = 2$ that is 63.4349°, which the
demo prints against the analytic `atan(gamma)`.

**(d)** A coaxial (pure shear) deformation has fixed principal strain axes and
produces no rotation of material lines other than the shortening and extension
along those axes. Simple shear rotates every material line. **Rotation is
therefore a qualitative signature that the deformation history was non-coaxial**,
which a strain measurement alone cannot distinguish: the same finite strain
ellipse can be reached by a coaxial path or by a rotating one, and only the
rotation of a marker (or the vorticity structure of the fabric) separates them.
