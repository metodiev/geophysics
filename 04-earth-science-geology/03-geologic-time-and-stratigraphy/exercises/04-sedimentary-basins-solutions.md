# Solutions — 04-03-04 Sedimentary Basins: Formation, Fill and Subsidence

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All parameters are commonly quoted values,
> labelled TYPICAL in the demo; a real study cites its own.

---

## ★1 — Instantaneous subsidence

**(a)** $\rho_m - \rho_c = 500$ kg m$^{-3}$ and
$\rho_m - \rho_w = 2270$ kg m$^{-3}$.

**(b)** $500/2270 = 0.2203$.

**(c)** $S_i = 35\,000 \times 0.5 \times 0.2203 = 3854.6$ m, matching the demo's
`2.00         3,854.6` in the $S_{\text{initial}}$ column.

**(d)** Because the lithosphere is in isostatic balance: removing light crust and
replacing it with dense mantle changes the buoyancy of the column by the *density
contrast*, not by the thickness. The crust is only 500 kg m$^{-3}$ lighter than
the mantle, so replacing 17.5 km of it with mantle produces a surface drop of less
than 4 km. Isostasy is a very efficient damper, and this factor is why
continental extension does not immediately produce an ocean basin of crustal
thickness.

---

## ★2 — Thermal subsidence

**(a)** $\tau = a^2/(\pi^2\kappa) = (1.25 \times 10^5)^2/(\pi^2 \times 10^{-6}) =
1.583 \times 10^{15}$ s. Dividing by the number of seconds in a Julian year,
$3.155\,76 \times 10^7$, gives $5.017 \times 10^7$ a $= 50.17$ Ma, which is what
the demo prints.

**(b)** $E_0 = \alpha\rho_mT_ma(1 - 1/\beta)/[2(\rho_m - \rho_w)]$. The numerator's
first part is $3.28 \times 10^{-5} \times 3300 \times 1330 \times 1.25 \times
10^5 = 1.7995 \times 10^7$; dividing by $2 \times 2270 = 4540$ gives $3963.7$ m,
and the factor $(1 - 1/2) = 0.5$ gives $E_0 = 1981.8$ m — the demo's
`asymptotic thermal subsidence E0 = 1,981.8 m`.

**(c)** $S_{\text{total}} = 3854.6 + 1981.8 = 5836.4$ m, matching the demo's
`S_total (m)  5,836.4` row for $\beta = 2$.

**(d)** The instantaneous term dominates, by about 1.95 to 1, and this is general
for large $\beta$: the crustal-thinning term scales as $t_c$ while the thermal
term scales as $a/2$ times a factor of order 0.4, and with $t_c = 35$ km and
$a = 125$ km the crustal term wins. **But the two terms differ in *when* they
appear**: the crustal term is instantaneous and the thermal term accumulates over
$\tau \approx 50$ Ma, so a basin's *early* history is dominated by thinning and its
*late* history by cooling.

---

## ★3 — Decompaction

**(a)** Using $\phi(z) = 0.55e^{-z/2000}$ at the present mid-depths 200, 750,
1550 and 2600 m:

$$\phi = 0.498,\ 0.378,\ 0.253,\ 0.150.$$

These are the demo's `phi now` column.

**(b)** For the topmost unit, $\Delta z_{\text{now}} = 400$ m,
$\phi = 0.498$, so the solid thickness is
$400(1 - 0.498) = 200.8$ m and the deposited thickness is
$200.8/(1 - 0.55) = 446.2$ m, which the demo reports as 447 m.

**(c)** Because the unit is less buried now than it will be later, and less buried
means less compacted, which means more porosity and therefore more thickness for
the same solid volume. Decompaction restores the unit to its depositional state.

**(d)** It assumes the porosity–depth law measured today applies throughout
burial, i.e. that the unit followed the same compaction path and that no
secondary porosity was created or destroyed by cementation or dissolution. Where
that fails — in a unit with late cementation, or one that has been exhumed — the
decompaction is wrong by more than the tectonic signal being measured.

---

## ★4 — The demo

**(a)** The demo reports, for the single-mode test,

```text
      100     0.020     25.0    0.392422        0.392387    3.49e-05
      400     0.001     25.0    0.392464        0.392462    2.18e-06
```

The error falls from $3.49 \times 10^{-5}$ to $2.18 \times 10^{-6}$, a factor of
16, when the time step falls by a factor of 20: this is the first-order
time-discretisation error of the explicit scheme, and its convergence is the
evidence that the code solves the equation it claims to.

**(b)** From the modal-weight table: $n = 1$ gives $+1.03205$, $n = 3$ gives
$-0.03822$, $n = 5$ gives $+0.00826$. The signs alternate because the initial
perturbation changes sign relative to the modes, and the magnitudes decay as
$1/n^3$.

**(c)** `worst |numeric - exact|   : 5.416e-03 m (2.733e-06 of E0)` and
`worst |1-mode law - exact|: 39.6 m (2.00% of E0)`.

**(d)** The first is a defect (a discretisation error, reducible by refining the
grid). The second is a property of the approximation: the single-exponential law
is the truncation of the exact series to its first mode, and no amount of care in
using it will reduce the 2 per cent error, because the error is in the formula.

---

## ★5 — Inverting for $\beta$

**(a)** $(1 - 1/\beta) = 3000/11\,673 = 0.2570$, so
$\beta = 1/(1 - 0.2570) = 1.346$.

**(b)** Crustal thinning is $t_c(1 - 1/\beta) = 35 \times 0.2570 = 9.00$ km.

**(c)** Because $S_{\text{total}}$ is a single number and the model has at least
two contributions whose sum is not separately determined: more thinning with less
thermal subsidence gives the same total, as does the reverse. The *shape* of the
subsidence curve as a function of time separates them, and shape is exactly what
a single observation discards.

**(d)** The thermal contribution is constrained by the **post-rift part of the
curve and by its curvature**, i.e. by the approach to the asymptote. The
single-exponential approximation errs by up to 2 per cent of $E_0$ — about 40 m in
the demo's case — and its largest error is at early times, which is precisely
where a syn-rift to post-rift transition is dated. Using the closed form to
interpret the first 25 Myr is therefore using it where it is worst.

---

## ★6 — Sensitivity

**(a)** From $\phi_0 = 0.45$ to 0.65 the tectonic subsidence moves from 3873 m to
4403 m: **530 m**.

**(b)** From a decay length of 1500 m to 3000 m it moves from 4319 m to 3693 m:
**626 m**.

**(c)** From 2650 to 2850 kg m$^{-3}$ it moves from 4009 m to 4215 m: **206 m**.

**(d)** The porosity model dominates — up to 710 m across the full range of the
porosity assumptions, against 206 m for the grain density, on a total of about
4000 m. A backstripped curve therefore needs a sensitivity table, and a
tectonic conclusion that depends on a difference smaller than the spread of that
table is not supported by the data. The demo prints the same conclusion:
`Spread caused by the porosity assumptions alone: 710 m; by grain density alone:
205 m.`

---

## ★7 — Why the closed form is not the solution

**(a)** Because the initial condition has a **kink** at $z = a/\beta$: the geotherm
is linear with slope $\beta T_m/a$ above that depth and constant below it. A
function with a discontinuous derivative cannot be represented by a single sine
mode, and the demo's weights show it: the first mode carries 1.032 of the total
and the third subtracts 0.038.

**(b)** Because the diffusion operator's eigenvalues are $-(n\pi/a)^2\kappa$, and
$\tau = a^2/(\pi^2\kappa)$ is defined so that the first mode decays as
$e^{-t/\tau}$; the $n$-th therefore decays as $e^{-n^2t/\tau}$.

**(c)** At $t = 0.1\tau$: mode 1 gives
$1.03205(1 - e^{-0.1}) = 1.03205 \times 0.09516 = 0.0982$; mode 3 gives
$-0.03822(1 - e^{-0.9}) = -0.03822 \times 0.5934 = -0.0227$; mode 5 gives
$0.00826(1 - e^{-2.5}) = 0.00826 \times 0.9179 = 0.0076$. The sum is **0.0831**
and the remaining modes add about $0.001$, giving $\approx 0.084$. The
single-mode law gives $1 - e^{-0.1} = 0.0952$, which overstates the subsidence by
about 13 per cent at this time — consistent with the demo's table, where at 5 Ma
($t/\tau = 0.0997$) the numeric value is 160.1 m against the law's 188.0 m.

**(d)** When the initial condition is smooth enough that its expansion in the
eigenfunctions is dominated by the first mode — practically, when the initial
condition has no internal kink or jump. The post-rift geotherm fails that test;
a sinusoidally perturbed geotherm passes it.

---

## ★8 — A sediment-filled basin

**(a)** With $\rho_L = 2500$ kg m$^{-3}$,
$\rho_m - \rho_L = 800$ kg m$^{-3}$ and
$S_i = 35\,000 \times 0.5 \times 500/800 = 10\,937$ m.

**(b)** The ratio is $10\,937/3854.6 = 2.84$.

**(c)** Airy isostasy balances the load against the displaced mantle, and a dense
load displaces more mantle per unit thickness than a light one. Tautologically, a
basin filled with rock rather than water must have subsided further to hold the
same mass. The implication is that **a basin's present depth reflects what filled
it, not only what created it**, so the same tectonic event produces a deeper basin
if it fills with sediment: the filling is part of the subsidence, not a
consequence of it.

**(d)** Computing the tectonic subsidence with the wrong load density is an error
of a factor of 2.84 in the *instantaneous* term — far larger than any porosity or
grain-density uncertainty in ★6, and larger than the tectonic signal itself. This
is why every equation in the lesson writes the load density explicitly rather than
absorbing it into a constant: the load density is a first-order parameter, and
choosing it silently is the largest single error available in a subsidence
calculation.
