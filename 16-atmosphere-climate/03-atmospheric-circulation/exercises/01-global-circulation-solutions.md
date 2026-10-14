# Solutions — 16-03-01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets

> **Read after attempting the exercises.** Several problems have more than one
> defensible answer; where that is true it is said so. Numbers were computed, not
> estimated by hand.

Lesson: [01 Global Circulation](../01-global-circulation.md).
Constants: $\Omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$a = 6.371\times10^6$ m, $g = 9.81\ \mathrm{m\,s^{-2}}$.

---

## ★1 — Coriolis parameter and inertial period

$f = 2\Omega\sin\phi$, period $= 2\pi/|f|$.

- $20^\circ$: $f = 2(7.292115\times10^{-5})(0.342020)
  = 4.98810\times10^{-5}\ \mathrm{s^{-1}}$;
  $2\pi/f = 1.2596\times10^{5}$ s $= 34.99$ h.
- $70^\circ$: $f = 2(7.292115\times10^{-5})(0.939693)
  = 1.37047\times10^{-4}\ \mathrm{s^{-1}}$;
  $2\pi/f = 4.5847\times10^{4}$ s $= 12.74$ h.

**Check.** The exact closed form is $\pi/(\Omega\sin\phi)$ with
$\pi/\Omega = 11.967$ h, so the period is $11.967/\sin\phi$ h:
$11.967/0.342020 = 34.99$ h and $11.967/0.939693 = 12.73$ h. ✔ (The familiar
"$12\ \mathrm{h}/\sin\phi$" is the rounded version of the same formula.)

---

## ★2 — Rossby number

$\mathrm{Ro} = U/(fL)$ with $U = 15\ \mathrm{m\,s^{-1}}$, $L = 2\times10^6$ m.

- $20^\circ$: $\mathrm{Ro} = 15/(4.98810\times10^{-5}\times2\times10^6)
  = 15/99.762 = 0.150$.
- $70^\circ$: $\mathrm{Ro} = 15/(1.37047\times10^{-4}\times2\times10^6)
  = 15/274.09 = 0.055$.

**Answer.** $70^\circ$ is rotation-dominated ($\mathrm{Ro}<0.1$); $20^\circ$ is
borderline. Note that $\mathrm{Ro}$ is *never* much larger than $1$ for
planetary-scale flows: it takes either a small scale ($L\sim10^2$ m) or a small
$U$ to become advection-dominated.

---

## ★3 — Conserved wind

$u_M = \Omega a\sin^2\phi/\cos\phi$ with $\Omega a = 464.6\ \mathrm{m\,s^{-1}}$.

- $5^\circ$: $464.6\times0.087156^2/0.996195 = 464.6\times0.007596/0.996195
  = 3.54\ \mathrm{m\,s^{-1}}$.
- $15^\circ$: $464.6\times0.066987/0.965926 = 32.2\ \mathrm{m\,s^{-1}}$.
- $40^\circ$: $464.6\times0.413176/0.766044 = 250.6\ \mathrm{m\,s^{-1}}$.

**Why $40^\circ$ is not believable.** $250\ \mathrm{m\,s^{-1}}$ is far above any
wind the momentum budget can maintain against friction and eddy mixing; the
conservation law that produced it has simply been applied outside its regime,
where the $\cos\phi$ denominator is becoming small and the neglected friction
term is no longer negligible.

---

## ★4 — Derivation of $\mathrm{d}M/\mathrm{d}t$

With $M = \Omega a^2\cos^2\phi + u\,a\cos\phi$ and $\phi$ changing along a
trajectory at rate $v/a$:

$$\frac{\mathrm{d}M}{\mathrm{d}t}
= \frac{\partial M}{\partial t} + \frac{v}{a}\frac{\partial M}{\partial\phi}.$$

Now $\partial M/\partial t = a\cos\phi\,\partial u/\partial t$, and

$$\frac{\partial M}{\partial\phi}
= -2\Omega a^2\sin\phi\cos\phi - u a\sin\phi
+ a\cos\phi\frac{\partial u}{\partial\phi},$$

so

$$\frac{v}{a}\frac{\partial M}{\partial\phi}
= -a\cos\phi\left(2\Omega\sin\phi + \frac{u\tan\phi}{a}\right)v
+ v\cos\phi\frac{\partial u}{\partial\phi}.$$

Substituting the momentum equation
$\partial_t u = -\,(v/a)\partial_\phi u + (f + u\tan\phi/a)v - u/\tau$ and
multiplying through by $a\cos\phi$, the term
$(f + u\tan\phi/a)v\,a\cos\phi$ from the curvature/Coriolis part of
$\partial_t M$ cancels the first term above, and the advection terms
$v\cos\phi\,\partial_\phi u$ cancel too, leaving

$$\frac{\mathrm{d}M}{\mathrm{d}t} = -\frac{a\cos\phi}{\tau}u.$$

With $\tau\to\infty$ this is $\mathrm{d}M/\mathrm{d}t = 0$: **the total angular
momentum is materially conserved**, while the planetary part converts to wind as
air moves meridionally.

---

## ★5 — Plateau depth and where the quartic fails

**(a)** Quartic form with $\theta_0 = 300$ K, $H = 10$ km:
$\theta_t-\theta_t(0) = -\theta_0\Omega^2a^2\phi^4/(gH) = -660.05\,\phi^4$ K
with $\phi$ in radians.

| $\phi$ | $\phi$ (rad) | $\phi^4$ | drop (K) |
|---|---|---|---|
| $10^\circ$ | 0.17453 | $9.279\times10^{-4}$ | $-0.61$ |
| $20^\circ$ | 0.34907 | $1.4837\times10^{-2}$ | $-9.80$ |
| $30^\circ$ | 0.52360 | $7.5166\times10^{-2}$ | $-49.61$ |

Exact bracket values, $C = 2640.2$ K: $-0.61$, $-9.80$, $-49.74$ K. The quartic
is exact to the printed precision at $10^\circ$ and $20^\circ$.

**(b)** The relative error of the quartic is $-0.26\%$ at $30^\circ$, $-1.5\%$ at
$45^\circ$, $-2.4\%$ at $50^\circ$, and reaches $-5\%$ at about $58.8^\circ$.
So over the whole plateau region the quartic is not merely qualitatively right
but quantitatively excellent; it fails only well poleward of the cell edge,
where the profile has already plunged by hundreds of kelvin and the underlying
assumption of a uniform tropical surface temperature has long since broken down.

---

## ★6 — Ferrel-cell momentum budget

**(a)** Friction drag per unit area: $\rho H U/\tau$ with $\rho = 1.0\
\mathrm{kg\,m^{-3}}$, $H = 10^4$ m, $U = 20\ \mathrm{m\,s^{-1}}$,
$\tau = 5\times86400 = 4.32\times10^5$ s:

$$1.0\times10^4\times20/4.32\times10^5 = 0.463\ \mathrm{N\,m^{-2}}.$$

**(b)** Coriolis torque per unit area: $\rho H f v$ with
$f(45^\circ) = 1.03126\times10^{-4}\ \mathrm{s^{-1}}$ and
$v = -1\ \mathrm{m\,s^{-1}}$:

$$10^4\times1.03126\times10^{-4}\times(-1) = -1.031\ \mathrm{N\,m^{-2}}.$$

**(c)** Required eddy momentum flux convergence:
$0.463-(-1.031) = 1.494\ \mathrm{N\,m^{-2}}$.

**Meaning.** The Coriolis torque acts in the *same* direction as friction, both
decelerating the westerlies, so the mean meridional circulation cannot be the
jet's engine. The jet is maintained by convergence of eddy momentum fluxes of
order $1\ \mathrm{N\,m^{-2}}$. Eddies are not a correction; they are the
mechanism.

---

## ★7 — Propagating the assumptions in the cell-edge match

The edge solves $C(\ln\cos\phi + \sin^2\phi/2) = -\Delta\theta_e\sin^2\phi$ with
$C = 4\theta_0\Omega^2a^2/(gH) = 2640.2$ K at $H = 10$ km.

Admitted ranges: $\Delta\theta_e\in[30,70]$ K (a nominal $50\pm20$ K) and
$H\in[8,12]$ km.

| | $H=8$ km | $H=10$ km | $H=12$ km |
|---|---|---|---|
| $\Delta\theta_e=30$ K | $10.9^\circ$ | $12.1^\circ$ | $13.3^\circ$ |
| $\Delta\theta_e=50$ K | $14.0^\circ$ | $15.6^\circ$ | $17.0^\circ$ |
| $\Delta\theta_e=70$ K | $16.5^\circ$ | $18.3^\circ$ | $20.0^\circ$ |

**Admitted range: $10.9^\circ$ to $20.0^\circ$**, a factor of 1.8.

**Why narrower than the demonstration's $10.9^\circ$–$22.6^\circ$?** The
demonstration's upper end came from $\Delta\theta_e = 90$ K, which is outside
the stated uncertainty band. The range is narrower because two of the four
corners that produced the extreme values have been excluded, *not* because the
uncertainty has been reduced. If anything the honest uncertainty is larger, since
$\theta_0$ and the assumed shear profile (the factor 2) are also assumptions that
were held fixed here.

---

## ★8 — Partitioning the transport (specification)

**What can be computed from this lesson alone.** The required total transport
$T(\phi)$ from the prescribed flux profile, and the eddy momentum flux
convergence needed to maintain a jet of stated speed against stated friction
(Section 7).

**The closure that must be added.** A relation between a *heat* flux and a
*mean state*. The cheapest is a downgradient diffusive closure
$F_\text{eddy}(\phi) = -2\pi a\cos\phi\,\rho c_p H\,D\,\partial\theta/\partial y$
with an eddy diffusivity $D$. Section 7's arithmetic shows what that closure
demands: carrying $3.825$ PW across a $3.3\times10^6$ m span with a $15$ K
contrast requires $D = 2.96\times10^6\ \mathrm{m^2\,s^{-1}}$.

**What would have to be measured to test it.** A meridional heat flux of resolved
eddies, and the eddy kinetic energy or mixing-length scale that sets $D$ — i.e.
time-resolved meridional wind and temperature on a latitude–height grid, so that
$\overline{v'\theta'}$ can be formed. That is *not* obtainable from a zonal-mean
data set, which is the point: the closure is a statement about unresolved
quantities, and its validity is an empirical question, not a derivation.

**Acceptable alternative answers.** A mean-cell closure
($\bar v$ from the thermodynamic equation) or a two-box energy-budget closure are
equally defensible, provided the answer states the closure explicitly and says
which quantity must be measured to test it. An answer that does not name the
closure, or that claims a partition without saying what is assumed, is wrong.
