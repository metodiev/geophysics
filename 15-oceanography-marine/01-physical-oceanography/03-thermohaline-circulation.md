---
id: 15-01-03
title: "Thermohaline Circulation and Deep Water Formation"
level: doctoral
prereqs: ["15-01-01", "02-05-04", "02-06-03"]
tags: [oceanography, marine-geophysics, thermohaline, overturning, box-model, multiple-equilibria, heat-transport]
---

# Thermohaline Circulation and Deep Water Formation

> **All models and data in this module are SYNTHETIC.** The box model below is
> this module's construction with chosen coefficients, printed by the
> demonstration in `code/`. It is not calibrated to any ocean, and no
> hydrographic section, mooring, tracer release or reanalysis is used. No real
> water mass is named.

The wind-driven circulation of
[Lesson 02](02-wind-driven-circulation.md) is forced from above and can be
understood, to first order, without any thermodynamics. The **thermohaline**
circulation is different: it is driven by the surface fluxes of heat and fresh
water, and it is therefore a statement about buoyancy. Its two central features —
that it is slow (centuries for a full circuit) and that it transports a
comparable amount of heat as the atmosphere — make it hard to observe and easy to
over-claim about.

This lesson is built around a specific honesty point: **a circulation whose
strength is set by buoyancy can have more than one stable state.** That statement
does not require a general circulation model. It appears in two boxes, three
algebraic relations and a `for` loop, and it can be checked by hand. What cannot
be produced so cheaply is a statement about *the real ocean's* threshold, and the
lesson is careful to separate the two.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a two-box buoyancy-driven model with a prescribed freshwater
   flux, and **explain** why the salinity balance (a flux, not a relaxation) is
   what permits more than one steady state.
2. **Solve** the steady-state condition as a scalar equation in the overturning
   $q$, and **find all** its roots without assuming uniqueness.
3. **Derive** the condition for a quadratic-fold (saddle-node) bifurcation and
   **locate** it numerically, reporting the freshwater-forcing threshold as a
   value of the model.
4. **Linearise** the model about each steady state and **classify** it as stable
   or unstable from the eigenvalues, checking the trace identity
   $\sum\lambda = -C_T - 3|q|$.
5. **Derive** the advective–diffusive thermocline profile
   $T(z) = T_d + (T_0-T_d)e^{-z/\delta}$ with $\delta = \kappa/w$, and **verify**
   it by substitution.
6. **Compute** an overturning heat transport $\rho c_p\Psi\Delta T$ and **state**
   precisely which combination of unknowns the observable constrains.
7. **Distinguish** a statement about the model from a statement about the ocean,
   and **say** what data would be needed to move from one to the other.

## Prerequisites

- [15-01-01 Seawater Properties: Temperature, Salinity, Density](01-seawater-properties.md) —
  the equation of state and the buoyancy frequency, used throughout.
- [02-05-04 Heat Conduction and the Diffusion Equation](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  the balance between advection and diffusion that sets the thermocline scale.
- [02-06-03 Viscous Flow and Boundary Layers](../../02-physics/06-fluid-mechanics/03-viscous-flow.md) —
  why a "diffusivity" is a closure rather than a property.

## 1. What is actually being driven

The surface ocean exchanges heat and fresh water with the atmosphere. Both
exchanges change buoyancy, and buoyancy changes density. A region that loses heat
becomes denser and can convect; a region that gains fresh water becomes lighter
and resists convection. Deep water formation is therefore a competition, and the
two competing terms have different *units of memory*:

- a temperature anomaly is erased by surface heat exchange on a timescale of
  months to a few years;
- a salinity anomaly is erased only by mixing with the surrounding water, on the
  timescale of the circulation itself.

**The salinity anomaly outlives the temperature anomaly.** That asymmetry is the
whole mechanism, and it is why the interesting behaviour appears in the salinity
equation and not the temperature equation.

## 2. A two-box model

Divide the ocean into a warm low-latitude box and a cold high-latitude box, and
let $T$ and $S$ be the *differences* between them. Let $q$ be the overturning
strength (units of $\mathrm{yr^{-1}}$ here, i.e. box volumes exchanged per year,
positive when the cold box sinks). The model is

$$\frac{\mathrm{d}T}{\mathrm{d}t} = C_T\left(T_a - T\right) - |q|\,T,
\qquad
\frac{\mathrm{d}S}{\mathrm{d}t} = F_S - |q|\,S,
\qquad
q = K_Q\left(\alpha T - \beta S\right).$$

Each term has a reading.

- $C_T(T_a - T)$: the atmosphere relaxes the thermal contrast toward its own
  contrast $T_a$, at rate $C_T$.
- $|q|T$: advection with strength $|q|$ destroys the contrast, at a rate
  proportional to the contrast. This is the only place $q$ enters, and it enters
  with a **modulus** — the transport destroys contrast whichever way it runs.
- $F_S$: the **imposed** freshwater flux, which *creates* a salinity contrast.
  This is the crucial modelling choice. $S$ is not relaxed toward a prescribed
  value; it is whatever balances the flux against advection.
- $q = K_Q(\alpha T - \beta S)$: the buoyancy difference drives the overturning.
  This is the only place the equation of state enters.

Chosen coefficients:

$$C_T = \frac{1}{25}\ \mathrm{yr^{-1}},\quad T_a = 25\ ^\circ\mathrm{C},\quad
\alpha = 1.70\times10^{-4}\ ^\circ\mathrm{C}^{-1},\quad
\beta = 7.60\times10^{-4}\ \mathrm{(g\,kg^{-1})^{-1}},$$

$$K_Q = 30\ \mathrm{yr^{-1}},\quad F_S = 0.020\
\mathrm{(g\,kg^{-1})\,yr^{-1}}.$$

**Every one of these is a chosen number.** The structure of what follows does not
depend on them; the threshold does, and the threshold is therefore the least
transferable output in the lesson.

### 2.1 Why a flux and not a relaxation

If $S$ were relaxed toward a prescribed $S_a$ instead of forced by a flux, the
salinity equation would be a second relaxation and the map $q \mapsto$ RHS would
be *monotone decreasing*, giving exactly one steady state. The demonstration
makes the difference visible: the salinity steady state is
$S = F_S/|q|$, which **diverges as the circulation weakens**. A weak circulation
cannot carry the freshwater away, so the salinity contrast grows, which weakens
the circulation further. That positive feedback is the mechanism, and it exists
only because the flux is prescribed.

## 3. Steady states

Setting both tendencies to zero:

$$T = \frac{C_T T_a}{C_T + |q|}, \qquad S = \frac{F_S}{|q|},$$

and substituting into the overturning relation gives one scalar equation:

$$\boxed{\;F(q) \equiv q - K_Q\left(\alpha\frac{C_T T_a}{C_T + |q|}
- \beta\frac{F_S}{|q|}\right) = 0 .\;}$$

$F$ is **continuous but not differentiable at $q = 0$**, because of the modulus.
The demonstration measures one-sided derivatives there of
$-4.56\times10^{8}$ and $+4.56\times10^{8}$ for a finite-difference step of
$10^{-9}$: infinite slopes of opposite sign. A Newton method started near
$q=0$ can therefore be thrown out of the basin; the demonstration uses a
sign-change scan and bisection, which cannot.

At $F_S = 0.020$ the demonstration finds **two** roots:

| $q$ (yr$^{-1}$) | $T$ ($^\circ$C) | $S$ (g kg$^{-1}$) | $\alpha T - \beta S$ | mode |
|---|---|---|---|---|
| 0.004086 | 22.683 | 4.895 | $+1.362\times10^{-4}$ | thermal (weak) |
| 0.048311 | 11.324 | 0.414 | $+1.610\times10^{-3}$ | thermal (strong) |

The two states differ in character, not just in magnitude. The strong state has
$T = 11.3\ ^\circ$C and $S = 0.41\ \mathrm{g\,kg^{-1}}$: a healthy thermal
contrast and a small salinity contrast. The weak state has almost the full
thermal contrast ($22.7\ ^\circ$C) but has accumulated a salinity contrast of
$4.9\ \mathrm{g\,kg^{-1}}$, which cancels most of the buoyancy difference and
leaves the circulation crawling. Both satisfy the same equations with the same
forcing.

The strong state's overturning period is $1/q = 20.7$ years; the weak state's is
244.7 years. **A factor of 12 in circulation strength, from the same freshwater
flux**, with no way to tell from the equations alone which the ocean has.

## 4. The fold

Sweep the freshwater forcing and count the solutions:

| $F_S$ ((g kg$^{-1}$) yr$^{-1}$) | states | $q$ (yr$^{-1}$) |
|---|---|---|
| 0.001 | 2 | 0.000180, 0.053894 |
| 0.016 | 2 | 0.003173, 0.049576 |
| 0.031 | 2 | 0.006952, 0.044479 |
| 0.046 | 2 | 0.012313, 0.037806 |
| 0.056 | 2 | 0.018783, 0.030466 |
| 0.061 | 0 | none |

The two branches converge and annihilate at $F_S = 0.05864\
\mathrm{(g\,kg^{-1})\,yr^{-1}}$, where $q = 0.024509$ and $0.024511$ — two roots
separated by $2\times10^{-6}$. Beyond that forcing, **no positive-$q$ steady
state exists in this model at all**.

This is a **saddle-node bifurcation**, and it has a signature that can be checked:
at the fold one eigenvalue of the linearised system passes through zero. The
demonstration prints exactly that ($-0.11353$, $+0.00000$) at $F_S = 0.05864$.
The physical reading is that the fold is the point where the stabilising and
destabilising feedbacks are exactly balanced — the marginal case of the
linearised analysis in Section 5.

Two cautions, both important.

- The value 0.05864 is a property of the *coefficients we chose*. It is not a
  property of the ocean, and it must never be quoted as "the freshwater threshold
  for the real circulation".
- Two-fold hysteresis is a robust *structure*: any model in this family with a
  prescribed freshwater flux and a buoyancy-driven transport has one. What the
  structure predicts is that the collapse is abrupt and that recovery requires
  forcing to return well below the collapse threshold — the two thresholds are
  different, and that asymmetry survives the loss of the numbers.

## 5. Stability

Linearise about a steady state. With $s = \mathrm{sign}(q)$ and $A = |q|$, the
Jacobian of $(\dot T, \dot S)$ is

$$J = \begin{pmatrix}
-C_T - A - T s K_Q\alpha & +T s K_Q\beta\\
-S s K_Q\alpha & -A + S s K_Q\beta
\end{pmatrix}.$$

The trace has a closed form. Since $\alpha T - \beta S = q/K_Q$,

$$\operatorname{tr}J = -C_T - 2A + sK_Q(\beta S - \alpha T)
= -C_T - 2A - s\,q = -C_T - 3A.$$

**The trace is always negative**, so a state is unstable only if the determinant
is negative — there is no route to instability through a pair of growing
oscillations. This is a useful structural result: the model cannot oscillate on
its way to (or away from) an equilibrium, and any oscillation in a bigger model
must come from physics this one omits.

At $F_S = 0.020$ the demonstration prints:

| $q$ (yr$^{-1}$) | eigenvalues | verdict |
|---|---|---|
| 0.004086 | $-0.09648$, $+0.04423$ | unstable (a saddle) |
| 0.048311 | $-0.14071$, $-0.04423$ | stable (a node) |

Check the trace identity for the stable state:
$-0.14071 - 0.04423 = -0.18494$, and $-C_T - 3A = -0.04 - 3(0.048311)
= -0.18493$. The two agree to five figures, which is a consistency check on the
algebra rather than a numerical coincidence. The determinant of the stable state
is $(-0.14071)(-0.04423) = +0.006223$, and for the saddle
$J = (-0.09648)(+0.04423) = -0.004267 < 0$, as required.

**The intermediate branch of a fold is always a saddle.** So between the two
stable states lies an unstable one, and the basin boundary between them is the
stable manifold of that saddle. Which state a basin finds depends on its history:
this is hysteresis, not bistability with a preferred answer.

## 6. The thermocline: advection against diffusion

The depth scale over which the temperature changes is set by a one-dimensional
balance between downward advection and vertical diffusion:

$$w\frac{\mathrm{d}T}{\mathrm{d}z} = \kappa\frac{\mathrm{d}^{2}T}
{\mathrm{d}z^{2}}, \qquad T(0) = T_0, \quad T(\infty) = T_d .$$

Substituting $T - T_d \propto e^{-z/\delta}$ gives
$\delta = \kappa/w$ and therefore

$$\boxed{\;T(z) = T_d + (T_0 - T_d)\exp\!\left(-\frac{z}{\delta}\right),
\qquad \delta = \frac{\kappa}{w}.\;}$$

With the chosen $\kappa = 1.0\times10^{-4}\ \mathrm{m^{2}\,s^{-1}}$:

| $w$ (m s$^{-1}$) | $w$ (m yr$^{-1}$) | $\delta$ (m) | Péclet $wH/\kappa$ ($H=4000$ m) |
|---|---|---|---|
| $3.17\times10^{-8}$ | 1.000 | 3155 | 1.3 |
| $1.00\times10^{-7}$ | 3.156 | 1000 | 4.0 |
| $3.17\times10^{-7}$ | 10.005 | 316 | 12.7 |
| $1.00\times10^{-6}$ | 31.560 | 100 | 40.0 |

The demonstration substitutes the analytic solution back into the differential
equation at six depths and finds a worst residual of $4.6\times10^{-9}\ \mathrm{K\,s^{-1}}$,
i.e. machine-level agreement. **The exponential thermocline is an exact solution
of the model equation, which is precisely why it is dangerous.** It contains one
number, $\kappa/w$, and it assumes that $\kappa$ is constant. A turbulent ocean's
$\kappa$ varies by orders of magnitude with depth and with the local Richardson
number, so an exact solution of a slightly wrong equation can be confidently,
precisely wrong.

## 7. Heat transport: what the observable constrains

The overturning transports heat at the rate

$$Q = \rho\,c_p\,\Psi\,\Delta T,$$

with $\rho = 1025\ \mathrm{kg\,m^{-3}}$ and $c_p = 3994\
\mathrm{J\,kg^{-1}\,K^{-1}}$ (the conventional reference value used throughout
this folder; other references quote values within about $0.5\,\%$ depending on
$T$ and $S$). For $\Psi = 15\ \mathrm{Sv}$ and $\Delta T = 15\ ^\circ$C:

$$Q = 1025 \times 3994 \times 15\times10^{6} \times 15
= 9.211\times10^{14}\ \mathrm{W} = 0.92\ \mathrm{PW}.$$

A dimensional check: $\mathrm{(kg\,m^{-3})(J\,kg^{-1}\,K^{-1})(m^{3}\,s^{-1})(K)}
= \mathrm{J\,s^{-1}} = \mathrm{W}$. ✔

Now the honesty point. An independent estimate of ocean heat transport — from
the atmospheric energy budget, or from an air–sea flux climatology integrated
meridionally — constrains the **product** $\Psi\,\Delta T$. It does not
constrain $\Psi$ alone, and dividing by an assumed $\Delta T$ to obtain "the
overturning" imports the assumption silently. With $\Psi$ ranging over a factor
1.5 and $\Delta T$ over a factor 1.3 within the demonstration's own table, the
product spans a factor 1.9 — and *every one of those combinations* is
indistinguishable by a heat-transport measurement alone. Mass and tracer
observations are what break the product apart.

## 8. Assumptions and regime of validity

1. **Two boxes.** No geography, no basin shape, no boundary currents. Box models
   are statements about *mechanism*.
2. **Prescribed freshwater flux.** The freshwater flux is an input, not a
   response. A coupled model that lets precipitation depend on the circulation
   changes the bifurcation structure.
3. **A linear equation of state with constant coefficients.** See
   [Lesson 01](01-seawater-properties.md) for the measured error of that
   assumption.
4. **Instantaneous response of $q$ to buoyancy.** No inertia in the momentum
   balance. The real adjustment involves Kelvin and Rossby waves on timescales of
   months to decades.
5. **A single overturning variable.** No distinction between interhemispheric,
   basin-scale and local convection; no distinction between the surface and deep
   branches.
6. **$|q|$, not $q$, in the advection terms.** The model is symmetric in the sense
   that it does not know which box is sinking except through the sign of $q$.
7. **Constant $\kappa$** in Section 6 — the single largest idealisation, since
   mixing is intermittent and spatially heterogeneous.

## 9. Worked examples

### Example 1 — the two steady states, from scratch

At $F_S = 0.020$, guess $q = 0.048$:

$$T = \frac{0.04 \times 25}{0.04+0.048} = \frac{1.0}{0.088} = 11.36\ ^\circ\mathrm{C},
\qquad S = \frac{0.020}{0.048} = 0.4167\ \mathrm{g\,kg^{-1}},$$

$$K_Q(\alpha T - \beta S) = 30\left(1.70\times10^{-4}(11.36)
- 7.60\times10^{-4}(0.4167)\right)$$
$$= 30\left(1.931\times10^{-3} - 3.167\times10^{-4}\right)
= 30(1.615\times10^{-3}) = 0.04844 .$$

Compare with the guess $0.048$: the right-hand side is $0.9\,\%$ high, so the
root is just below. The demonstration's root is $0.048311$, and one more
iteration lands on it. **The fixed-point iteration converges here because the map
is a contraction on this branch**; it will *not* converge to the other (saddle)
branch, which is the practical face of the stability result in Section 5.

### Example 2 — the trace identity as a diagnostic

For the weak state $q = 0.004086$, the identity predicts
$\operatorname{tr}J = -0.04 - 3(0.004086) = -0.052258$. The demonstration's
eigenvalues sum to $-0.09648 + 0.04423 = -0.05225$. Two consequences:

- the identity is a free check on any linearisation code: if the computed trace
  disagrees with $-C_T - 3|q|$, the Jacobian is wrong;
- the *product* (determinant) is what flips sign, so a plot of $\det J$ against
  the control parameter crosses zero exactly at the fold and nowhere else. That
  is the cheapest way to locate the bifurcation numerically.

### Example 3 — heat transport, and the error of quoting a circulation

An observational estimate reports $Q = 1.2\ \mathrm{PW}$ with a stated
uncertainty of $\pm0.3\ \mathrm{PW}$. Assume $\Delta T = 15\ ^\circ$C. Then

$$\Psi = \frac{Q}{\rho c_p \Delta T}
= \frac{1.2\times10^{15}}{1025 \times 3994 \times 15}
= \frac{1.2\times10^{15}}{6.141\times10^{7}}
= 1.954\times10^{7}\ \mathrm{m^{3}\,s^{-1}} = 19.5\ \mathrm{Sv},$$

with the $\pm0.3\ \mathrm{PW}$ becoming $\pm4.9\ \mathrm{Sv}$ — and that is
*before* allowing for the uncertainty in $\Delta T$. At $\Delta T = 20\ ^\circ$C
the same $Q$ gives $\Psi = 14.7\ \mathrm{Sv}$. **The range spanned by the
$\Delta T$ assumption alone (14.7–19.5 Sv) is larger than the quoted
observational error.** This is the arithmetic reason that heat transport does not
measure a circulation.

## 10. Python demonstration

`code/thermohaline_circulation_demo.py` prints everything above with units:

1. the model equations, the coefficients, and **all** the steady states at the
   reference forcing, located by a sign-change scan over $10^{5}$ grid points;
2. the hysteresis scan and the fold, located by bisection to machine precision;
3. the eigenvalues of each branch, with the trace identity available for checking;
4. $\delta = \kappa/w$ and the residual of the analytic thermocline;
5. the heat-transport table and the product ambiguity;
6. verification: root residuals ($<10^{-17}$), the one-sided slopes at the
   $|q|$ kink, a dimensional check, and a check that the steady-state relations
   reproduce the defining equations.

Run it with

```bash
cd 15-oceanography-marine/01-physical-oceanography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermohaline_circulation_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, and
about 6 s of run time (the sign-change scan is deliberately fine so the fold is
not missed).

## 11. Exercises

Full sets with worked solutions are in
[`exercises/03-thermohaline-circulation-exercises.md`](exercises/03-thermohaline-circulation-exercises.md)
and
[`exercises/03-thermohaline-circulation-solutions.md`](exercises/03-thermohaline-circulation-solutions.md).

- ★ Evaluate $T$, $S$ and $q$ for a trial value $q = 0.030\ \mathrm{yr^{-1}}$ at
  $F_S = 0.020$ and say which branch it is nearest.
- ★★ Derive $\operatorname{tr}J = -C_T - 3|q|$ and state what the result forbids.
- ★★ Compute the thermocline depth for $w = 2\ \mathrm{m\,yr^{-1}}$ and the depth
  at which $T$ has fallen $63\,\%$ of the way to $T_d$.
- ★★★ Design the measurement that would distinguish the two stable states of a
  two-box ocean, stating what you would measure, over what duration, and the size
  of the signal.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use $C_T = 1/25\ \mathrm{yr^{-1}}$,
$T_a = 25\ ^\circ$C, $\alpha = 1.70\times10^{-4}\ ^\circ\mathrm{C}^{-1}$,
$\beta = 7.60\times10^{-4}\ \mathrm{(g\,kg^{-1})^{-1}}$,
$K_Q = 30\ \mathrm{yr^{-1}}$, $\rho = 1025\ \mathrm{kg\,m^{-3}}$, $c_p = 3994\
\mathrm{J\,kg^{-1}\,K^{-1}}$.

> **(a)** At $F_S = 0.010\ \mathrm{(g\,kg^{-1})\,yr^{-1}}$ and
> $q = 0.050\ \mathrm{yr^{-1}}$, compute $T$, $S$ and $K_Q(\alpha T - \beta S)$.
> Is $q = 0.050$ above or below the steady state at this forcing?
> **(b)** Compute $\operatorname{tr}J$ for the steady state you are nearest, and
> state whether the trace alone can establish stability.
> **(c)** A colleague reports an overturning heat transport of
> $1.0\ \mathrm{PW}$ and concludes that the circulation is $16\ \mathrm{Sv}$.
> State the assumption they made and compute the value of $\Psi$ they obtain.
> **(d)** State the two structural predictions of the two-box model that do not
> depend on its coefficients, and one prediction that does.

A worked version of (a)–(c) is in the lesson-03
[solutions](exercises/03-thermohaline-circulation-solutions.md).

## Common pitfalls

1. **Quoting the fold value as a property of the ocean.** $F_S = 0.05864\
   \mathrm{(g\,kg^{-1})\,yr^{-1}}$ is a property of our coefficients. The
   *existence* of a fold is robust; the number is not.
2. **Reporting "the" overturning for a bistable model.** Between the two stable
   states there is a saddle, and which state a basin occupies is a question about
   its history.
3. **Relaxing salinity to a fixed value.** That removes the mechanism
   (Section 2.1) and the multiple equilibria with it. The freshwater flux is not
   an optional detail.
4. **Using Newton's method across $q=0$.** $F$ has infinite one-sided slopes
   there. Use a sign-change scan or bracket the roots.
5. **Treating $\kappa$ as a fluid property.** It is a closure for turbulence that
   varies by orders of magnitude; the exponential thermocline is an exact
   solution of an approximate equation.
6. **Dividing a heat transport by an assumed $\Delta T$ and calling the result a
   measurement.** Example 3: the $\Delta T$ assumption can move the answer more
   than the quoted observational error.
7. **Forgetting the modulus.** The model's advection term is $|q|T$, not $qT$;
   dropping the modulus changes the equilibrium structure qualitatively, not
   quantitatively.

## Related modules

- [01 Seawater Properties: Temperature, Salinity, Density](01-seawater-properties.md) —
  the equation of state and cabbeling, both of which this model strips out.
- [02 Wind-Driven Circulation, Ekman Transport and Gyres](02-wind-driven-circulation.md) —
  the other half of the circulation, which shares the same water.
- [04 Internal Waves, Tides and Mixing](04-internal-waves-and-tides.md) —
  where the mixing that sets $\kappa$ actually comes from.
- [Module 15-04 Gas Hydrates: Occurrence, Geophysics and Resource Potential](../04-seafloor-mapping-and-habitats/02-gas-hydrates.md) —
  a temperature- and pressure-dependent phase whose stability is set by the same
  deep-water properties.
- [13-02-01 Rayleigh–Bénard Convection and the Mantle](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md) —
  the same buoyancy-versus-diffusion balance in a completely different fluid.
- [16-04-03 Climate Sensitivity and Feedbacks](../../16-atmosphere-climate/04-climate-system-and-feedbacks/03-climate-sensitivity.md) —
  the atmospheric side of the same coupling.

## Self-assessment checklist

- [ ] I can write the two-box equations and say which term makes multiple
      equilibria possible.
- [ ] I can reduce the steady state to one scalar equation and find all its roots.
- [ ] I can locate a saddle-node bifurcation and say what its eigenvalue signature
      is.
- [ ] I can derive the trace identity and use it as a code check.
- [ ] I can derive and verify the exponential thermocline, and state its
      assumption.
- [ ] I can compute a heat transport and explain why it constrains a product.
- [ ] I can separate a claim about this model from a claim about the ocean.
