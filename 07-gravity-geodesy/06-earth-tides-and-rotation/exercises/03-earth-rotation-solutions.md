# Solutions — 07-06-03 Earth Rotation, Polar Motion, LOD and Excitation

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values or stated standard constants.

Lesson: [03 Earth Rotation](../03-earth-rotation.md).

---

## ★1 — Momentum for a $0.5\ \mathrm{ms}$ LOD change

$$\Delta H_3 = C\,\Omega\,\frac{\Delta\mathrm{LOD}}{\mathrm{LOD}}
= (8.4022\times10^{37})(7.2921150\times10^{-5})
\frac{0.5\times10^{-3}}{86164} = 3.5554\times10^{25}\
\mathrm{kg\,m^{2}\,s^{-1}} .$$

**Sign:** a positive $\Delta H_3$ in the non-solid part (the atmosphere gaining
westerly momentum) means the solid Earth loses angular momentum, so the day
*lengthens*. The relation is
$\Delta\mathrm{LOD}/\mathrm{LOD} = +\Delta H_3/(C\Omega)$.

---

## ★2 — Rigid Euler period

$$T = \frac{2\pi}{\Omega H}.$$

For $H = 0.00300$:
$T = 2\pi/[(7.2921150\times10^{-5})(0.00300)] = 2.8723\times10^{7}\ \mathrm{s}
= 332.42\ \mathrm{d}$.

For $H = 0.00350$:
$T = 2.4619\times10^{7}\ \mathrm{s} = 284.93\ \mathrm{d}$.

A $17\%$ increase in $H$ (from $0.00300$ to $0.00350$) shortens the period by
$(332.42-284.93)/332.42 = 14.3\%$, i.e. by the factor
$1/1.1667 = 0.857$ to first order. **The period is inversely proportional to the
dynamical ellipticity**, so an Earth model that gets $H$ wrong by $10\%$ gets the
rigid wobble period wrong by the same $10\%$ in the opposite direction — one of
the reasons the wobble period is a useful constraint on the Earth's figure when
the elasticity and ocean corrections are modelled.

---

## ★3 — A hemispheric wind

Thin-shell formula: $H_3 = \int\sigma u_\phi R\sin\theta\,\mathrm{d}A$ with
$\sigma = M_{\text{atm}}/(4\pi R^{2})$, so

$$H_3 = \frac{M_{\text{atm}}u}{4\pi R^{2}}R^{3}2\pi\!\!\int_0^{\pi/2}\!\!
\sin^{2}\theta\,\mathrm{d}\theta
= \frac{M_{\text{atm}}uR}{2}\left(\frac{\pi}{4}\right) .$$

(Using $\int_0^{\pi/2}\sin^{2}\theta\,\mathrm{d}\theta = \pi/4$ and
$\mathrm{d}A = R^{2}\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\phi$.)

Numbers: $M_{\text{atm}} = 5.15\times10^{18}\ \mathrm{kg}$,
$u = 20\ \mathrm{m\,s^{-1}}$, $R = 6.371\times10^{6}\ \mathrm{m}$:

$$H_3 = \frac{(5.15\times10^{18})(20)(6.371\times10^{6})}{2}(0.7854)
= 2.578\times10^{26}\ \mathrm{kg\,m^{2}\,s^{-1}} .$$

$$\Delta\mathrm{LOD} = \mathrm{LOD}\frac{H_3}{C\Omega}
= 86164 \times \frac{2.578\times10^{26}}{6.127\times10^{33}}
= 86164 \times 4.207\times10^{-8} = 3.63\times10^{-3}\ \mathrm{s}
= 3.63\ \mathrm{ms}.$$

**Units:** $\mathrm{kg\,m\,s^{-1}}\times\mathrm{m} = \mathrm{kg\,m^{2}\,s^{-1}}$
✔; $C\Omega$ has the same units, so the ratio is dimensionless ✔.

---

## ★4 — The $(2/3)$ factor, and a thick shell

**Thin shell.** With $u_\phi = \Omega R\sin\theta$,

$$H_3 = \frac{M}{4\pi R^{2}}R^{2}\Omega R^{2}2\pi\!\!\int_0^{\pi}\!\!
\sin^{2}\theta\,\mathrm{d}\theta
= M\Omega R^{2}\frac{2\pi(4/3)}{4\pi} = \frac{2}{3}M\Omega R^{2},
\qquad\blacksquare$$

using $\int_0^{\pi}\sin^{3}\theta\,\mathrm{d}\theta = 4/3$.

**Thick shell.** A shell of thickness $\mathrm{d}r$ at radius $r$ carries mass
$\mathrm{d}M = 4\pi r^{2}\rho(r)\,\mathrm{d}r$ and angular momentum
$(2/3)\,\mathrm{d}M\,\Omega r^{2}$ by the thin-shell result, so for a general
density profile

$$H_3 = \Omega\!\int_0^{R}\!\rho(r)\,\frac{8\pi}{3}\,r^{4}\,\mathrm{d}r
= C\,\Omega ,$$

because that integral *is* the definition of the axial moment of inertia $C$.
The $(2/3)MR^{2}$ form is therefore the special case of a thin shell at the outer
radius; for a general body the correct statement is simply $H_3 = C\Omega$.

**Mass concentrated at $r = R/2$:** $C = MR^{2}/4$, so
$H_3 = \Omega MR^{2}/4$, which is $(1/4)/(2/3) = 0.375$ times the thin-shell
value: moving mass inward reduces the angular momentum for the same rotation rate
by the square of the radius of gyration.

---

## ★5 — Steady forced pole displacement

$$|m| = \frac{|\chi_0|}{\left|1-\sigma/\sigma_c\right|} .$$

**400-day forcing.** $\sigma/\sigma_c = T_c/T = 304.98/400 = 0.7624$, so

$$|m| = \frac{1.0\times10^{-8}}{1-0.7624} = \frac{1.0\times10^{-8}}{0.2376}
= 4.209\times10^{-8}\ \mathrm{rad}
= 4.209\times10^{-8}\times206264.8\times10^{3} = 8.68\ \mathrm{mas}.$$

**305-day forcing.** $\sigma/\sigma_c = 304.98/305 = 0.99993$, so the
amplification is $1/(7\times10^{-5}) = 1.4\times10^{4}$ and
$|m| = 1.0\times10^{-8}\times1.4\times10^{4} = 1.4\times10^{-4}\ \mathrm{rad}
= 29\ \mathrm{arcsec}$.

**Comment.** The same $10^{-8}$ excitation gives $8.7\ \mathrm{mas}$ at 400 days
and $29\ \mathrm{arcsec}$ at 305 days: a factor $3400$. This is why any excitation
whose spectrum happens to have power near the free period dominates the observed
polar motion, and why attributing a wobble to a particular physical process
requires the *spectra* of all the candidate excitations to be compared, not their
total amplitudes. In the real Earth damping prevents the response from diverging,
but the amplification over a broad band remains.

---

## ★6 — The $10^{6}$ error

Multiplying the momentum integral by the Earth's mass instead of the
atmosphere's replaces the density of the moving fluid by the density of the whole
planet. Physically it says "the *Earth* is moving with the wind", i.e. it computes
the angular momentum of the solid Earth rotating with a zonal velocity field of
$30\ \mathrm{m\,s^{-1}}$ — a quantity $10^{6}$ times larger and physically
unrelated to the atmospheric budget.

**The check that catches it:** compare against the analytically known solid-body
value. For any shell, $H_3 = C_{\text{shell}}\Omega$; for the atmosphere that is
$(2/3)M_{\text{atm}}\Omega R^{2} = 1.016\times10^{28}\ \mathrm{kg\,m^{2}\,s^{-1}}$
(the demonstration verifies this to $2.2\times10^{-16}$). Any wind momentum must
be *smaller* than this by roughly $u/(\Omega R)$ — i.e. by about
$30/465 = 6.5\%$ — so a momentum of $10^{33}$ is immediately impossible. **An
order-of-magnitude bound against a quantity you can compute exactly is the
cheapest possible error check**, and in this case it is decisive.

---

## ★7 — Core effect versus damping (specification)

1. **Model.** A two-layer fluid-core/mantle model with a stated coupling
   (a simple no-torque or a stated viscous/electromagnetic coupling constant),
   giving equations for the mantle wobble and the core wobble coupled by the
   coupling constant; optionally add a damping term with a stated quality factor.
2. **Synthetic data.** Generate a synthetic polar-motion time series by
   integrating the coupled system with a *known* step excitation, sampled at a
   daily cadence for several years.
3. **Analysis.** Fit the free period and the decay time constant to the synthetic
   series with (a) the coupled two-layer model and (b) the rigid one-layer model
   with a damping term.
4. **Diagnostic.** The *shape* of the misfit residual, not its rms: a core
   coupling that is not modelled produces a phase-dependent residual (a second
   frequency beating with the main wobble), while a wrong damping gives an
   amplitude-decay misfit with the *same* frequency. Plot the residual's
   frequency content: a beat peak near the core–mantle coupling frequency is the
   signature.
5. **Prediction.** The core raises the effective moment of inertia participating
   in the wobble, shifting the period against the direction of a pure damping
   change (damping alters the period only at second order in $1/Q$). So a period
   *shift with little amplitude decay* indicates the core.
6. **Distinguishing observation.** A long, well-sampled series (decades) with
   independent excitation estimates: with the excitation known, the wobble's
   response function can be measured directly and its frequency dependence
   (period shift *vs* decay) separates the two mechanisms. A single short series
   cannot.

---

## ★8 — Degeneracy in the excitation budget (specification)

1. **Model.** Four synthetic excitation series (atmosphere, ocean, land water,
   cryosphere), each a smooth seasonal-plus-trend field expanded in the same
   spherical-harmonic band as the observations, generated from a stated
   power-spectrum model.
2. **Observation operator.** **Excitation** above degree 3 (say), plus white noise
   with a stated per-coefficient variance, and, importantly, the *temporal*
   sampling (monthly), so the analysis sees what is actually observable.
3. **Analysis.** Solve for the four series jointly and then examine the
   Hessian/covariance: the eigenvector with the smallest eigenvalue identifies the
   combination of the four that the data cannot separate.
4. **Diagnostic.** The variance inflation on each term when the others are
   removed, and the singular values of the design matrix. Report the *null
   combination*, whose coefficients state explicitly which mixtures of the four
   excitations are indistinguishable.
5. **Prediction.** The atmosphere and the ocean are most degenerate at the
   frequencies where the atmosphere forces an ocean response with a fixed
   admittance (the inverted-barometer-like regime), and the cryosphere and land
   water are most degenerate in the trend, where both produce a slow secular
   excitation at low degree.
6. **The measurement that breaks it.** Independent data with a *different*
   spatial or temporal signature: for atmosphere–ocean, a barometer network gives
   the atmospheric term directly so the residual ocean term is isolated; for
   cryosphere–water, a glacier inventory or a GRACE-like mass field separates the
   mass change by region or by its gravity signature. The specification must name
   which of these is available, because a degeneracy that no measurement can break
   is a statement about the problem, not a defect of the analysis.
