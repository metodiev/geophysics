# Solutions — 02-07-03 Maxwell's Equations and Their Physical Meaning

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Constants: $\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A²,
$\varepsilon_0 = 8.854\,187\,812\,8\times10^{-12}$ F/m,
$c = 299\,792\,458$ m/s (exact), $\eta_0 = 376.730\,314$ Ω.

---

## ★1 — The four equations

| # | Differential | Integral | Meaning | Static limit |
|---|---|---|---|---|
| I | $\nabla\cdot\mathbf D = \rho$ | $\oint\mathbf D\cdot\mathrm d\mathbf A = Q$ | field lines begin and end on charge | Gauss's law |
| II | $\nabla\cdot\mathbf B = 0$ | $\oint\mathbf B\cdot\mathrm d\mathbf A = 0$ | no magnetic monopoles | unchanged |
| III | $\nabla\times\mathbf E = -\partial\mathbf B/\partial t$ | $\oint\mathbf E\cdot\mathrm d\boldsymbol\ell = -\mathrm d\Phi_B/\mathrm dt$ | changing flux drives circulation | $\nabla\times\mathbf E = \mathbf 0$: electrostatics |
| IV | $\nabla\times\mathbf H = \mathbf J + \partial\mathbf D/\partial t$ | $\oint\mathbf H\cdot\mathrm d\boldsymbol\ell = I + \mathrm d\Phi_D/\mathrm dt$ | currents and changing flux drive circulation | $\nabla\times\mathbf H = \mathbf J$: Ampère's law |

---

## ★2 — Continuity and the displacement current

**(a)** $\nabla\cdot(\nabla\times\mathbf H) = 0$ identically, so from IV
$0 = \nabla\cdot\mathbf J + \partial(\nabla\cdot\mathbf D)/\partial t
= \nabla\cdot\mathbf J + \partial\rho/\partial t$ using I. Without the
displacement current, IV would give directly $\nabla\cdot\mathbf J = 0$.

**(b)** That is unacceptable because a charging capacitor has
$\nabla\cdot\mathbf J \neq 0$ on the plates (current flows in, no current between
the plates) — a steady-current assumption of the kind that would forbid the
capacitor from charging at all. Charge conservation demands the continuity
equation, so the displacement current must exist; it is not optional.

**(c)** Conduction current $I = 10^{-3}$ A, so the rate of charge accumulation is
$\mathrm dQ/\mathrm dt = 10^{-3}$ C/s. Gauss's law gives
$\Phi_D = Q$, so the displacement current
$\mathrm d\Phi_D/\mathrm dt = 10^{-3}$ A — equal and opposite in the bookkeeping
sense: the conduction current into one plate is exactly matched by the
displacement current between the plates. The closure of the circuit is the
displacement current.

---

## ★3 — The wave equation

**(a)** Take the curl of III:
$\nabla\times(\nabla\times\mathbf E) = -\partial(\nabla\times\mathbf B)/\partial t$.
Using $\nabla\times\mathbf B = \mu\varepsilon\,\partial\mathbf E/\partial t$
(from IV with $\mathbf J = 0$, $\mathbf D = \varepsilon\mathbf E$) gives the right
side $-\mu\varepsilon\,\partial^2\mathbf E/\partial t^2$. Using
$\nabla\times(\nabla\times\mathbf E) = \nabla(\nabla\cdot\mathbf E) -
\nabla^2\mathbf E$ and $\nabla\cdot\mathbf E = \rho/\varepsilon = 0$ gives the left
side $-\nabla^2\mathbf E$. Equating: $\nabla^2\mathbf E =
\mu\varepsilon\,\partial^2\mathbf E/\partial t^2$ ✓.

**(b)** $v = c/\sqrt{\varepsilon_r} = 2.997\,924\,58\times10^{8}/2.449\,489\,743
= 1.223\,90\times10^{8}$ m/s $= 0.408\,248\,c$.

**(c)** $\lambda = v/f = 1.223\,90\times10^{8}/10^{8} = \mathbf{1.2239}$ m.

**(d)** It establishes that light *is* an electromagnetic wave — the constant fixed
by electrostatic and magnetostatic experiments coincides with the measured speed of
light to the precision of the day. Observable consequences are that
$\varepsilon_r$ (a dielectric property) sets an optical refractive index, and that
the whole electromagnetic spectrum is one phenomenon.

---

## ★4 — Diffusion in a conductor

**(a)** Keep $\mathbf J = \sigma\mathbf E$ and drop
$\mu_0\varepsilon\,\partial\mathbf E/\partial t$ from IV. Then
$\nabla\times\mathbf H = \sigma\mathbf E$, and the curl-of-the-curl step gives
$\nabla^2\mathbf E = \mu\sigma\,\partial\mathbf E/\partial t$. The dropped term is
the displacement current, and it is negligible because
$|\mu\varepsilon\partial^2\mathbf E/\partial t^2| \ll
|\mu\sigma\partial\mathbf E/\partial t|$ whenever $\sigma/(\omega\varepsilon)\gg1$.

**(b)** $D = 1/(\mu_0\sigma) = \rho/\mu_0 = 100/1.2566\times10^{-6}
= 7.9577\times10^{7}$ m²/s.

**(c)** $z_{1/2} = 0.954\sqrt{Dt}$: at $t = 1$ s, 8508 m; at $t = 10$ s, 26 906 m;
at $t = 100$ s, 85 085 m. (The demo's diffusion run gives the same law at much
shorter times and length scales: $z/\sqrt{Dt} = 0.9538$ at three times spanning a
factor 4.)

**(d)** Because there is no wavefront: the field amplitude at depth $z$ is nonzero
for every $t>0$, and the penetration depth grows as $\sqrt{Dt}$. The correct
statement is "at time $t$ the field has decayed to a specified fraction of its
surface value at depth $z_{1/2}(t)$", or equivalently "the response at time $t$ is
sensitive to conductivity within roughly $\sqrt{Dt}$". Any quoted "velocity" is
$\omega\delta$, which depends on frequency and is not a transport speed.

---

## ★5 — The ratio $\sigma/(\omega\varepsilon)$

**(a)** $\rho = 1000$ Ω·m gives $\sigma = 10^{-3}$ S/m and
$\varepsilon = 6\varepsilon_0 = 5.3125\times10^{-11}$ F/m, so
$\omega\varepsilon = 2\pi f\times5.3125\times10^{-11}$:

| $f$ (Hz) | $\sigma/(\omega\varepsilon)$ | regime |
|---|---|---|
| $10^{-3}$ | $3.00\times10^{9}$ | diffusion |
| 1 | $3.00\times10^{6}$ | diffusion |
| $10^{6}$ | 3.00 | neither (transition) |
| $10^{8}$ | 0.0300 | wave (low-loss) |

**(b)** $f_c = \sigma/(2\pi\varepsilon) = 10^{-3}/3.3379\times10^{-10}
= 2.9959\times10^{6}$ Hz $\approx3.0$ MHz. It depends on $\varepsilon_r$ because
the competition is between two *currents* — conduction $\sigma E$ and displacement
$\omega\varepsilon E$ — and $\varepsilon$ sets the latter. A medium with the same
conductivity but ten times the permittivity has its crossover ten times lower.

**(c)** $\sigma = 0.01$ S/m, $\varepsilon = 20\varepsilon_0 = 1.7708\times10^{-10}$:
$8.99\times10^{9}$ at $10^{-3}$ Hz; $8.99\times10^{6}$ at 1 Hz; 8.99 at
$10^{6}$ Hz; 0.0899 at $10^{8}$ Hz. $f_c = 8.9876\times10^{6}$ Hz $\approx9.0$ MHz.

**(d)** Entries with ratio $\gg1$: diffusion equation (both media at $10^{-3}$ Hz
and 1 Hz). Ratio $\ll1$: wave equation (both at $10^{8}$ Hz). Ratio $\sim1$–10:
neither — the full Helmholtz form must be used (both at $10^{6}$ Hz). Note that a
ratio of 3 is *not* "almost diffusive": it produces a 20 % error in both $\alpha$
and $\beta$. The transition zone is wide, and it is exactly where cross-hole radar
operates.

---

## ★6 — The exact Helmholtz equation

**(a)** With $\partial/\partial t\to i\omega$, Ampère's law becomes
$\nabla\times\mathbf H = (\sigma + i\omega\varepsilon)\mathbf E$. Take the curl of
Faraday's law and use the identity
$\nabla\times(\nabla\times\mathbf E) = \nabla(\nabla\cdot\mathbf E)
- \nabla^2\mathbf E = -\nabla^2\mathbf E$ (the divergence term vanishes in a
charge-free region), and substitute Ampère's law on the right:
$-\nabla^2\mathbf E = -i\omega\mu(\sigma+i\omega\varepsilon)\mathbf E$.
Hence

$$\nabla^2\mathbf E = \left(i\omega\mu\sigma - \omega^2\mu\varepsilon\right)\mathbf E
= -k^2\mathbf E, \qquad k^2 = \omega^2\mu\varepsilon - i\omega\mu\sigma .$$

**(b)** Write $k^2 = \omega^2\mu\varepsilon(1 - i\sigma/\omega\varepsilon)$ and
$k = \beta - i\alpha$, so $k^2 = \beta^2-\alpha^2-2i\alpha\beta$. Matching real and
imaginary parts: $\beta^2-\alpha^2 = \omega^2\mu\varepsilon$ and
$2\alpha\beta = \omega\mu\sigma$. Solving gives

$$\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}}
\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}-1\right]^{1/2},
\qquad
\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}}
\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}+1\right]^{1/2}.$$

**(c)** At $\sigma/(\omega\varepsilon) = 1$: $\sqrt{1+x^2} = \sqrt2 = 1.414\,214$, so
$\alpha = 0.643\,594\,\omega\sqrt{\mu\varepsilon/2} = 0.455\,090\,\omega\sqrt{\mu\varepsilon}$
and $\beta = 1.553\,774\,\omega\sqrt{\mu\varepsilon/2}
= 1.098\,684\,\omega\sqrt{\mu\varepsilon}$. Hence
$\alpha/\beta = 0.414\,214$ exactly ($= \sqrt{(\sqrt2-1)/(\sqrt2+1)}$), and

$$\frac{v}{c/\sqrt{\varepsilon_r}} = \frac{\omega/\beta}{\omega\sqrt{\mu\varepsilon}}
= \frac{1}{1.098\,684} = 0.910\,180 .$$

The wave is 9 % slower than lossless — a measurable difference, and one that a
lossless-velocity assumption would attribute to a different permittivity.

**(d)** At $x = 1$ we have $\sigma = \omega\varepsilon$, so the low-loss
attenuation is

$$\alpha_{\text{LL}} = \frac{\sigma}{2}\sqrt{\frac{\mu}{\varepsilon}}
= \frac{\omega\varepsilon}{2}\sqrt{\frac{\mu}{\varepsilon}}
= \frac{\omega\sqrt{\mu\varepsilon}}{2} = 0.5\,\omega\sqrt{\mu\varepsilon} .$$

Compare $\alpha = 0.4551\,\omega\sqrt{\mu\varepsilon}$: the low-loss formula is
9.9 % high. And $1/\delta$ with
$\delta = \sqrt{2/(\omega\mu\sigma)}$ gives
$1/\delta = \sqrt{\omega\mu\sigma/2} = \omega\sqrt{\mu\varepsilon}\sqrt{1/2}
= 0.7071\,\omega\sqrt{\mu\varepsilon}$: 55 % high. So at the crossover the
strong-conductor result is worse than the low-loss one, and **neither** is
acceptable — which is the point of the transition regime.

---

## ★7 — Poynting's theorem

**(a)** $\nabla\cdot(\mathbf E\times\mathbf H) = \mathbf H\cdot(\nabla\times\mathbf E)
- \mathbf E\cdot(\nabla\times\mathbf H)$. Substitute III and IV:
$= \mathbf H\cdot(-\partial\mathbf B/\partial t) -
\mathbf E\cdot(\mathbf J + \partial\mathbf D/\partial t)$
$= -\frac12\frac{\partial}{\partial t}(\mu H^2 + \varepsilon E^2) -
\mathbf J\cdot\mathbf E$ for linear media with constant $\mu,\varepsilon$.
Rearranging gives the stated form.

**(b)** $u = \frac12(\varepsilon E^2+\mu H^2)$ in J/m³ is the energy density;
$\mathbf S = \mathbf E\times\mathbf H$ in W/m² is the energy flux density.

**(c)** In vacuum, $S = E^2/\eta_0 = 1/376.730 = 2.6544\times10^{-3}$ W/m². With
$\varepsilon_r = 6$, $S = E^2/\eta = 1/153.800 = 6.5020\times10^{-3}$ W/m² — 2.45
times larger, because the impedance is lower: the same electric amplitude drives a
larger magnetic amplitude and hence a larger flux. The demo's impedance table
gives $\eta(\varepsilon_r = 4) = 188.37$ Ω and $\eta(20) = 84.24$ Ω, from which the
same scaling follows.

**(d)** $\mathbf J\cdot\mathbf E = \sigma E^2$ is the ohmic dissipation. It removes
energy from the field irreversibly, which is why the field amplitude decays with
depth (skin depth) and why penetration is limited by conductivity rather than by
geometry.

---

## ★8 — Numerical verification

**(a)** The demo reports, for the exact vacuum plane wave,

| $\Delta z$ (m) | Faraday residual (scaled) | Ampère residual (scaled) |
|---|---|---|
| $10^{-2}$ | $9.016\times10^{-6}$ | $3.007\times10^{-14}$ |
| $5\times10^{-3}$ | $2.254\times10^{-6}$ | $7.519\times10^{-15}$ |
| $2.5\times10^{-3}$ | $5.635\times10^{-7}$ | $1.880\times10^{-15}$ |

Both fall by exactly 4.00 per halving of the step: second-order convergence to zero
in both cases.

**(b)** Ampère's two terms — $\nabla\times\mathbf B$ and
$\mu_0\varepsilon_0\partial\mathbf E/\partial t$ — agree to
$\sim10^{-15}$ relative to the magnitude $kE_0$, i.e. to round-off, whereas
Faraday's two terms agree only to second order in $\Delta z$. The reason is the
choice $\Delta t = 0.4\Delta z/c$: the Faraday residual is dominated by
discretisation, while the Ampère residual's leading errors happen to be smaller by
construction for this sampling. The physics conclusion, however, does not depend on
that accident: **the residual is finite and scales to zero, which is possible only
because the displacement current is included.** Omit it and the Ampère residual is
order unity, not $10^{-15}$.

**(c)** Both divergences are exactly zero. The fields vary only in $z$ and are
transverse to $z$, so every term in $\nabla\cdot\mathbf E$ and $\nabla\cdot\mathbf B$
is identically zero — no numerical check is even needed, though the demo reports
$0.000\times10^{0}$.

**(d)** Faraday's law fixes the amplitude *ratio* $B_0 = E_0/c$ and the mutual
orthogonality; Ampère's law then fixes the *speed* through $k = \omega/c$. Two
independent equations, two unknowns — which is why the plane wave is determined and
no further freedom remains.

---

## ★9 — Yee dispersion

**(a)** From $\sin(\omega\Delta t/2) =
\mathrm{cfl}\sin(k\Delta x/2)$, take arcsines and divide by
$k\Delta x/2$ using $\mathrm{cfl} = c\Delta t/\Delta x$:

$$\omega = \frac{2}{\Delta t}\arcsin\!\left[\mathrm{cfl}\sin\frac{k\Delta x}{2}\right]
\;\Longrightarrow\;
\frac{c_{\text{num}}}{c} = \frac{\omega}{kc}
= \frac{\arcsin\!\left[\mathrm{cfl}\sin(k\Delta x/2)\right]}
{\mathrm{cfl}\,k\Delta x/2} .$$

**(b)** Let $u = k\Delta x/2$. Expand
$\sin u = u - u^3/6+\ldots$ and
$\arcsin x = x + x^3/6+\ldots$:

$$\arcsin(\mathrm{cfl}\sin u) \approx \mathrm{cfl}\,u
- \frac{\mathrm{cfl}u^3}{6} + \frac{\mathrm{cfl}^3u^3}{6}
= \mathrm{cfl}\,u\left[1 - \frac{u^2}{6}(1-\mathrm{cfl}^2)\right] ,$$

so

$$\frac{c_{\text{num}}}{c} = 1 - \frac{u^2}{6}(1-\mathrm{cfl}^2)
= 1 - \frac{(k\Delta x)^2}{24}(1-\mathrm{cfl}^2) + O((k\Delta x)^4) .$$

**(c)** At $\mathrm{cfl} = 1$ the correction vanishes *identically* to all orders,
because the dispersion relation becomes $\sin(\omega\Delta t/2) =
\sin(k\Delta x/2)$, hence $\omega = ck$ exactly. The accident is that in one
dimension the staggered differences in space and time have the same argument; in
2-D and 3-D the relation contains $\sin$ terms in several directions and no time
step makes all of them cancel. The demo verifies the exactness at $\mathrm{cfl} =
1$ (error $0.000\times10^{0}$) and the non-zero errors at $\mathrm{cfl} = 0.9$,
0.5, 0.25.

**(d)** With $k\Delta x = 2\pi/15 = 0.418\,879$ and $\mathrm{cfl} = 0.5$:

$$-\frac{(k\Delta x)^2}{24}(1-0.25) = -\frac{0.175\,460\times0.75}{24}
= -5.483\times10^{-3},$$

against the demo's $-5.498\times10^{-3}$. The 0.3 % difference is the neglected
$O((k\Delta x)^4)$ term, which for $k\Delta x = 0.42$ is of relative order
$(k\Delta x)^2/30\sim6\times10^{-3}$ of the leading term — the right order of
magnitude to explain the residual ✓. The demo's scaled column
$\text{error}/(k\Delta x)^2$ is 0.0313, 0.0313, 0.0313, 0.0315 at 60, 30, 15 and 8
points per wavelength, converging to $(1-\mathrm{cfl}^2)/24 = 0.031\,25$ exactly as
predicted.

---

## ★10 — Charge relaxation

**(a)** Take the divergence of $\mathbf J = \sigma\mathbf E$ with
$\nabla\cdot\mathbf E = \rho/\varepsilon$: $\nabla\cdot\mathbf J =
\sigma\rho/\varepsilon$. The continuity equation then gives
$\partial\rho/\partial t = -\sigma\rho/\varepsilon$, whose solution is exponential
decay with $\tau_e = \varepsilon/\sigma$.

**(b)** Rock: $\tau_e = 6\varepsilon_0/0.01 = 5.31\times10^{-9}$ s (about 5 ns).
Copper: $\tau_e = \varepsilon_0/5.96\times10^{7} = 1.49\times10^{-19}$ s. Both are
far shorter than any measurement interval, so free charge in either is neutralised
essentially instantaneously.

**(c)** Since any charge placed in rock disappears in nanoseconds, no electrostatic
*charge* distribution can exist at depth and no electrostatic field can be measured
from the surface — the negative statement opening the lesson. Self-potential
measurements are not electrostatic charge measurements: the sources are *current*
generators (electrokinetic flow, redox and thermoelectric gradients) that maintain a
steady current field, and the observed potentials are produced by that steady
current, not by stored charge. The decay time is irrelevant because the source is
continuously active.

**(d)** For steady currents $\nabla\cdot\mathbf J = 0$, and with
$\mathbf J = \sigma\mathbf E$ and uniform $\sigma$ this gives
$\nabla\cdot\mathbf E = 0$; with $\nabla\times\mathbf E = \mathbf 0$ it follows that
$V$ with $\mathbf E = -\nabla V$ satisfies Laplace's equation. The measured
quantity — the ratio of potential difference to injected current at a given
electrode geometry — depends on the conductivity distribution, because
$\sigma$ is what relates the *current* (known: we inject it) to the field
(measured). Charge never appears in the observable; conductivity always does. That
is why every EM method is an inference about conductivity, and why the
displacement current, permittivity and free charge enter only in the high-frequency
and interface details.
