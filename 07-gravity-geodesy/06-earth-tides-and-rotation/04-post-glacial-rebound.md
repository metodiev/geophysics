---
id: 07-06-04
title: "Post-Glacial Rebound: Viscosity and Ice History Inference"
level: research
prereqs: ["07-06-01", "07-06-03", "02-04-07"]
tags: [gravity, geodesy, post-glacial-rebound, viscosity, inverse-problems]
---

# Post-Glacial Rebound: Viscosity and Ice History Inference

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the relaxation time of a harmonic surface load on a viscous
   half-space and **compute** its spectrum over degree and viscosity.
2. **Explain** why the direction of the degree dependence is a property of the
   *model* (unconfined half-space versus a channel of fixed thickness) and not of
   the Earth.
3. **Build** a synthetic ice history and **predict** the relative-sea-level curve
   and the present-day uplift rate it implies at two sites with different
   harmonic content.
4. **Fit** viscosity and ice scale to synthetic data and **measure** the
   degeneracy between them as the fraction of parameter space that remains
   acceptable.
5. **Compare** observables by their constraining power — one rate, two rates, a
   curve in time, and combinations — and state which kind of additional
   observation is worth acquiring.
6. **Explain** why a present-day gravity rate and a present-day uplift rate are
   *not* independent measurements of the viscosity, and what a space-gravity
   mission adds instead.
7. **State** the model assumptions that a rebound-based viscosity estimate
   inherits, and which of them dominates the uncertainty.

## Prerequisites

- [01 Solid Earth Tides and Their Gravity Signature](01-solid-earth-tides.md) —
  the degree-2 formalism and Love numbers this lesson's viscoelastic response
  parallels.
- [03 Earth Rotation, Polar Motion, LOD and Excitation](03-earth-rotation.md) —
  the other observable of the same mass redistribution.
- [02-04-07 Viscoelasticity](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  the constitutive behaviour of a material that flows on glacial timescales.

> **All models and data in this module are SYNTHETIC.** The ice history, the
> viscosity, the site geometry, the noise and the observations are teaching
> values. No real ice sheet, site, uplift rate or published viscosity is used.

## 1. Why the mantle flows on glacial timescales

Ice sheets several kilometres thick load the crust with pressures of order
$\rho_igH \approx 10^{7}\ \mathrm{Pa}$. The mantle beneath responds to such a load
over $10^{3}$–$10^{5}$ years by creeping, and its response is observed as
post-glacial rebound: uplift rates of millimetres per year today, relative
sea-level records that fall by tens to hundreds of metres over the last
$10^{4}$ years, and a present-day gravity change that is part of the budget of
satellite gravimetry (see
[07-05-05](../05-satellite-gravimetry/05-grace-applications.md)).

The physics is that of a **linear viscous (or Maxwell) half-space**: an
incompressible fluid with shear viscosity $\eta$ and a free surface, loaded
periodically in space. The starting result is the Stokes solution for a
periodic surface traction $p_0\cos kx$, whose surface vertical velocity is
$p_0\cos kx/(2\eta k)$. Since the driving pressure is the weight of the load minus
the buoyancy of the displaced mantle,

$$p_0 = \rho_i g L - \rho_m g w ,$$

the deflection $w$ obeys

$$\dot w = \frac{\rho_m g w - \rho_i g L}{2\eta k}
\;\Longrightarrow\;
\boxed{\;\tau_l = \frac{2\eta\,k_l}{\rho_m g},\qquad k_l = \frac{l}{R}\;}$$

for a degree-$l$ load, and the equilibrium deflection is
$w_\infty = L\rho_i/\rho_m$ (the fully compensated value, which for the
demonstration's $1200\ \mathrm{m}$ of ice is $333\ \mathrm{m}$).

**The direction of the degree dependence is model-dependent and must be
checked.** In an *unconfined* half-space a short-wavelength load drives flow in a
thin surface region of thickness $\sim1/k$, so higher degrees relax *slower*
($\tau \propto k$). In a *channel of fixed thickness* $d$ the Poiseuille result
$\tau = 12\eta/(d^{3}\rho_m g k^{2})$ makes them relax *faster*
($\tau \propto 1/k^{2}$). A rebound study that does not say which regime its
Earth model is in cannot be compared with another one, because the two predict
opposite behaviour.

## 2. The relaxation-time spectrum

With $R = 6371\ \mathrm{km}$, $\rho_m = 3300\ \mathrm{kg\,m^{-3}}$ and
$g = 9.81\ \mathrm{m\,s^{-2}}$:

| degree $l$ | $\tau$ at $\eta = 10^{20}$ | at $10^{21}$ | at $10^{22}\ \mathrm{Pa\,s}$ |
|---|---|---|---|
| 2 | 61.5 yr | 614.6 yr | 6145.6 yr |
| 5 | 153.6 yr | 1536.4 yr | 15364.0 yr |
| 10 | 307.3 yr | 3072.8 yr | 30728.1 yr |
| 20 | 614.6 yr | 6145.6 yr | 61456.2 yr |
| 50 | 1536.4 yr | 15364.0 yr | 153640.4 yr |
| 100 | 3072.8 yr | 30728.1 yr | 307280.8 yr |

*Worked example 1.* For $l = 2$, $\eta = 10^{22}\ \mathrm{Pa\,s}$:

$$k_2 = \frac{2}{6.371\times10^{6}} = 3.139\times10^{-7}\ \mathrm{m^{-1}},
\qquad
\tau_2 = \frac{2(10^{22})(3.139\times10^{-7})}{(3300)(9.81)} = 1.94\times10^{11}\
\mathrm{s} = 6146\ \mathrm{yr}.$$

So a viscosity of $10^{22}\ \mathrm{Pa\,s}$ in this model gives a degree-2
relaxation time comparable to the deglaciation duration, which is precisely the
regime in which a present-day signal survives. **A spherical treatment multiplies
these times by a degree-dependent factor of order unity** (roughly
$(2l^{2}+4l+3)/(l(l+1))$, i.e. $3.2$ at $l = 2$), and a layered viscosity
structure changes them by much more; the demonstration uses the half-space form
and labels it as its approximation.

## 3. A synthetic history, and two sites with different degrees

The demonstration builds a load that grows linearly to a peak of $1200\
\mathrm{m}$ at $20\ \mathrm{ka}$ before present and decays to zero by
$10\ \mathrm{ka}$, superimposed on a $400\ \mathrm{m}$ local dome peaked at
$17\ \mathrm{ka}$. Site A sees the large-scale (degree-2) field; site B sees the
local dome (degree 10). With $\eta = 10^{22}\ \mathrm{Pa\,s}$:

| quantity | site A (degree 2) | site B (degree 10) |
|---|---|---|
| relaxation time | 6146 yr | 30728 yr |
| peak RSL | 187.6 m | 22.2 m |
| RSL today | 38.9 m | 18.1 m |
| uplift rate today | $+4.272\ \mathrm{mm\,yr^{-1}}$ | $+0.298\ \mathrm{mm\,yr^{-1}}$ |

Both sites share a viscosity but respond on different timescales — the whole
basis of the inference, and the reason a *network* is worth more than a better
instrument.

## 4. Measuring the degeneracy

The demonstration fits two parameters — $\log_{10}\eta$ and an overall ice scale
$s$ — on a $41\times41$ grid, and counts the fraction of the plane that is
acceptable ($\Delta\chi^{2} < 2.3$, roughly the $68\%$ level for two parameters).
Using a synthetic uplift rate with $0.20\ \mathrm{mm\,yr^{-1}}$ of noise:

| data used | acceptable grid points | $\eta$ range accepted | ice-scale range |
|---|---|---|---|
| site A rate alone | 86 of 1681 ($5.1\%$) | $6.3\times10^{21}$–$2.8\times10^{22}$ | 0.82–1.50 |
| site B rate alone | 795 of 1681 ($47.3\%$) | $8.9\times10^{21}$–$1.0\times10^{23}$ | 0.50–1.50 |
| A $+$ B rates | 46 of 1681 ($2.7\%$) | $1.1\times10^{22}$–$2.8\times10^{22}$ | 0.85–1.50 |

Three measured facts, and the honest reading of each:

1. **One rate per site is a weak constraint.** Five per cent of the plane for the
   well-observed site, and $47\%$ for the site whose rate is small — because a
   rate is a single number and both the viscosity and the ice thickness scale it.
2. **A second site halves it, not eliminate it.** The two rates leave $2.7\%$:
   the degeneracy is real but it is a broad region rather than a narrow valley,
   and the correlation between $\log_{10}\eta$ and $s$ inside the accepted set is
   not significant.
3. **The wording matters.** "Viscosity is determined to within a factor of three"
   is what $5\%$ of a plane means; "viscosity is determined" is not.

*Worked example 2 (how much does a rate constrain?).* Suppose the truth were
$\eta = 10^{22}\ \mathrm{Pa\,s}$ and $s = 1.0$. Doubling $s$ doubles the load and
therefore nearly doubles the rate; *halving* $\eta$ does not double the rate,
because it also shortens $\tau$, so the residual deflection — and hence the rate
— is smaller by the time we observe it. That asymmetry is what makes the
accepted region a blob with structure rather than a line, and it is why simply
adding precision to the same rate does not converge to a point.

## 5. Observables ranked by what they constrain

Adding a *time curve* of relative sea level (four epochs, $5\ \mathrm{m}$ of
noise) is much more powerful than adding a second rate:

| data used | acceptable grid points |
|---|---|
| A rate $+$ B rate (no curve) | $46$ ($2.7\%$) |
| A RSL curve alone | $6$ ($0.36\%$) |
| A rate $+$ A RSL curve | $5$ ($0.30\%$) |
| A rate $+$ A RSL curve $+$ B rate | $4$ ($0.24\%$) |

The curve measures the *shape* of the decay, which is the relaxation time itself;
a rate measures only a product of the relaxation time and the load. This is the
general principle this lesson exists to teach:

> **Breaking a degeneracy requires an observable whose sensitivity to the
> parameters differs — a different degree, a different epoch, or a different
> physical quantity. More precision on the same observable does not help.**

## 6. Why a gravity rate is not an independent viscosity measurement

It is tempting to argue that satellite gravity measures the *mass* while
geodesy measures the *height*, so combining them breaks the degeneracy. In the
linear viscous model this is not true: both the uplift rate and the gravity rate
are proportional to the current rate of change of the deflection, at the same
degree and epoch,

$$\dot g \propto \frac{\rho_m g}{R}\dot w ,$$

so they are related by a constant and carry the same information about
$(\eta, s)$. What space gravimetry actually adds is:

1. **Several degrees at once.** A single satellite solution contains degrees 2
   through $\sim L$, whose relaxation times differ; a *spectrum* of rates is a
   set of observables with different sensitivities, which is exactly what is
   needed.
2. **A global integral.** The degree-2 rate in particular responds to the whole
   glacier inventory, not to one site.
3. **A time series.** Filling in the recent decades, where RSL indicators are
   sparse.

**Not** because gravity and height measure different physics: to first order, they
measure the same relaxation with different weights.

## 7. Assumptions and regime of validity

1. **Linear viscous rheology.** A Maxwell solid with a single viscosity; real
   mantle flow is nonlinear, and the linearisation is justified only for small
   stress perturbations.
2. **Uniform viscosity.** Real mantle viscosity varies by orders of magnitude with
   depth, and the inferred "viscosity" is an effective value for the mode being
   fitted. Two studies with different Earth models can infer different values
   from the same data.
3. **No lithosphere.** The model has no elastic lid; a lithosphere reduces the
   deflection for short wavelengths and changes the higher-degree relaxation.
4. **Fixed ocean geometry and no meltwater redistribution.** The model ignores
   the sea-level equation: meltwater is returned to the ocean, and the ocean load
   then responds as well. In a self-consistent treatment the ocean's geometry and
   the load change together, and ignoring this makes the assumed load wrong at
   the few-metre level in sea level.
5. **A prescribed ice history.** The load is an input. Its uncertainty is the
   dominant one in every rebound inference, which is why the fit must include it
   as a parameter (as the demonstration's ice scale does).
6. **No erosion, sedimentation or thermal effects on $\eta$.**
7. **Rotational and tidal forcing are separate.** This lesson's uplift is purely
   from the load; the same relaxation also changes the rotation
   (see [03](03-earth-rotation.md)).

## 8. Python demonstration

`code/post_glacial_rebound_demo.py` prints, with units:

1. **The relaxation-time spectrum** for six degrees and three viscosities, with
   the derivation and the model-dependence warning.
2. **A synthetic ice history** (1200 m peak at 20 ka, gone by 10 ka; a 400 m dome
   at 17 ka) and the fully compensated deflection (333 m).
3. **Two sites**: degree 2 and degree 10, with $\tau$ differing by a factor of
   five, RSL 187.6/38.9 m and 22.2/18.1 m, and uplift rates
   $4.272$/$0.298\ \mathrm{mm\,yr^{-1}}$.
4. **The degeneracy**, as the fraction of the parameter plane that is acceptable:
   $5.1\%$ (one rate), $47.3\%$ (the small-rate site), $2.7\%$ (both rates).
5. **Observables ranked**: the RSL curve leaves $0.36\%$ and the combination
   $0.24\%$.
6. **A statement** of why the gravity rate is not independent, and what space
   gravimetry actually adds.

Print-only, fixed seed, no network, runs in under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-post-glacial-rebound-exercises.md`](./exercises/04-post-glacial-rebound-exercises.md)
and
[`exercises/04-post-glacial-rebound-solutions.md`](./exercises/04-post-glacial-rebound-solutions.md).

- **★** Compute $\tau_3$ and $\tau_{30}$ for $\eta = 5\times10^{21}\
  \mathrm{Pa\,s}$.
- **★** Compute the equilibrium deflection for a 2000 m ice load and state the
  ratio used.
- **★★** Show why doubling the ice scale and halving the viscosity do not
  produce the same uplift rate, and estimate the residual factor from the
  demonstration's numbers.
- **★★** Given the accepted fractions, state the factor by which each additional
  observable narrows the viscosity range, and rank the observables.
- **★★★** Design an experiment that tests whether a layered viscosity structure
  can be recovered from a network of RSL curves, specifying what is degenerate
  even in the best case.

## 10. Mastery checkpoint

Do this without notes:

> Using the demonstration's model ($\tau_l = 2\eta k_l/(\rho_mg)$,
> $R = 6371\ \mathrm{km}$, $\rho_m = 3300\ \mathrm{kg\,m^{-3}}$,
> $g = 9.81\ \mathrm{m\,s^{-2}}$): **(a)** compute $\tau_2$ for
> $\eta = 10^{21}\ \mathrm{Pa\,s}$; **(b)** compute the equilibrium deflection for
> 800 m of ice and the ratio that gives it; **(c)** state which of two sites —
> degree 2 or degree 40 — still shows a present-day signal 10 kyr after the load
> vanished, and why; **(d)** a fit leaves $5\%$ of a $(\log\eta, s)$ plane
> acceptable: state what that means for the viscosity in words;
> **(e)** name the largest assumption in the inference.

*Answers.* **(a)** $k_2 = 2/6.371\times10^{6} = 3.139\times10^{-7}\
\mathrm{m^{-1}}$; $\tau_2 = 2(10^{21})(3.139\times10^{-7})/(32373)
= 1.94\times10^{10}\ \mathrm{s} = 614.6\ \mathrm{yr}$.
**(b)** $w_\infty = L\rho_i/\rho_m = 800\times917/3300 = 222.3\ \mathrm{m}$: the
deflection is the ice thickness scaled by the density ratio, which is the
requirement that the load's weight be supported by the buoyancy of displaced
mantle. **(c)** Degree 2. The present-day rate is the current deflection divided by the
relaxation time, $|\dot w| \approx w(t)/\tau$, and $w(t) =
w_\infty e^{-\Delta t/\tau}$ with $\Delta t = 10\ \mathrm{kyr}$ the time since
the load vanished. So the rate is
$w_\infty e^{-\Delta t/\tau}/\tau$, which is largest when $\tau \approx
\Delta t$. Here $\tau_2 = 6146\ \mathrm{yr}$ is close to $\Delta t$ while
$\tau_{40}$ is far longer, so degree 2 wins — and the demonstration measures
exactly that: $4.272\ \mathrm{mm\,yr^{-1}}$ at the degree-2 site against
$0.298\ \mathrm{mm\,yr^{-1}}$ at the degree-10 site. (In a channel model,
where $\tau$ *decreases* with degree, the answer would reverse: another reason
the model must be stated.)
**(d)** The acceptable region is $5\%$ of the plane, with the viscosity spanning
roughly $6\times10^{21}$ to $3\times10^{22}\ \mathrm{Pa\,s}$ for the
demonstration's grid: the data determine the viscosity to within about a factor
of four, *given* the assumed ice history. Saying "the viscosity is
$10^{22}\ \mathrm{Pa\,s}$" would be an overclaim.
**(e)** The ice history: it is an input, its uncertainty is larger than the data
uncertainty, and the whole degeneracy is between it and the viscosity.

## 11. Common pitfalls

1. **Quoting a viscosity without the Earth model.** Uniform vs layered, with or
   without a lithosphere, changes the inferred value by an order of magnitude.
2. **Forgetting that the degree dependence is model-dependent.** Half-space and
   channel models predict opposite trends.
3. **Treating a rate as a viscosity measurement.** It is a product of viscosity,
   load and history.
4. **Adding precision instead of adding a different observable.** $2.7\%$ of a
   plane is not a measurement, however small the error bar on the rate.
5. **Assuming gravity and height measurements are independent.** In the linear
   model they differ by a constant.
6. **Ignoring the sea-level equation.** Meltwater redistribution changes the load
   and therefore the answer.
7. **Fitting a load you cannot check.** An ice history with enough freedom can fit
   any rebound curve.

## 12. Real-world applications

- **Mantle rheology.** Rebound is the main constraint on the viscosity of the
  upper and lower mantle, and hence on convection and plate dynamics.
- **Sea level.** Relative sea level at a rebound site is a *local* measurement of
  a global problem; separating the rebound component is essential for sea-level
  budgets.
- **Satellite gravimetry.** The solid-Earth trend is one of the background terms
  removed in every mass-change estimate
  (see [07-05-05](../05-satellite-gravimetry/05-grace-applications.md)).
- **Ice-sheet history.** Conversely, *given* a viscosity model, rebound data
  constrain the size and timing of past ice sheets — the same degeneracy read in
  the other direction.

## 13. Further reading

- **Turcotte, D. L. & Schubert, G., *Geodynamics*** — viscous flow, relaxation
  times and the standard rebound treatment.
- **Lambeck, K., *The Earth's Variable Rotation*** — rebound as a rotation and
  gravity signal.
- **Stacey, F. D. & Davis, P. M., *Physics of the Earth*** — mantle rheology and
  the observational constraints on viscosity.
- **Torge, W. & Müller, J., *Geodesy*** — uplift, gravity change and their
  measurement.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 14. Related lessons

- [01 Solid Earth Tides and Their Gravity Signature](01-solid-earth-tides.md) —
  the elastic response to a periodic load; here the load is glacial and the
  response viscous.
- [03 Earth Rotation, Polar Motion, LOD and Excitation](03-earth-rotation.md) —
  the same mass redistribution seen in the rotation.
- [02 Tidal Corrections in Precise Measurements](02-tidal-corrections.md) —
  the other correction that must be applied to a gravity reading.
- [07-05-05 Applications: Groundwater Depletion, Ice Loss, Sea Level](../05-satellite-gravimetry/05-grace-applications.md) —
  where the rebound trend must be removed from a mass budget.

## 15. Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md).
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md).
- [12 Global Geophysics and the Interior](../../12-global-geophysics-interior/README.md) —
  mantle viscosity as an interior property.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — degeneracy,
  parameter trade-offs and resolution.
- [26-reference-library](../../26-reference-library/README.md).

## 16. Self-assessment checklist

- [ ] I can derive the relaxation time and compute its spectrum.
- [ ] I can state why the degree dependence is model-dependent.
- [ ] I can build a load history and predict the RSL curve and its rate.
- [ ] I can measure a degeneracy as a fraction of parameter space.
- [ ] I can rank observables by their constraining power.
- [ ] I can explain why gravity and uplift rates are not independent.
- [ ] I can list the assumptions and name the dominant one.
