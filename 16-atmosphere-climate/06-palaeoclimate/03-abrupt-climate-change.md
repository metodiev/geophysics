---
id: 16-06-03
title: "Abrupt Climate Change and Tipping Elements"
level: research
prereqs: ["16-06-02", "16-04-02", "16-04-03"]
tags: [atmosphere, climate, palaeoclimate, abrupt-change, tipping-elements, hysteresis, bistability]
---

# Abrupt Climate Change and Tipping Elements

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by
> [`code/abrupt_climate_change_demo.py`](code/abrupt_climate_change_demo.py).
> The box model and the energy-balance model are chosen teaching constructions.
> **The thresholds computed here are properties of these models, not estimates of
> any real threshold, and nothing in this lesson is a statement about when or
> whether a real component of the Earth system would change state.**

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** abruptness of *response* from abruptness of *forcing*, and
   **state** why the difference matters for prediction.
2. **Define** a fold (saddle-node) bifurcation, bistability and hysteresis, and
   **relate** them to the number of steady solutions of a model.
3. **Derive** the steady-state relation of a two-box ocean circulation model
   with freshwater forcing, including the appearance of a fold.
4. **Measure** a hysteresis loop by integrating the model forward and backward
   through the forcing range.
5. **Find** the multiple steady solutions by root finding and **classify** which
   are stable from the direction of the flow.
6. **Demonstrate** ice-albedo bistability in a zero-dimensional energy-balance
   model and **quantify** how the thresholds move when one closure parameter
   changes.
7. **State** why a tipping threshold from a simple model is a statement about the
   model's closures and initial conditions.

## Prerequisites

- [16-06-02 Model-Data Comparison in Palaeoclimate](02-paleoclimate-model-data.md) —
  how palaeoclimate states are inferred at all.
- [16-04-02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](../04-climate-system-and-feedbacks/02-climate-feedbacks.md) —
  the feedbacks whose strength determines whether multiple states exist.
- [16-04-03 Climate Sensitivity: Definitions and Estimation](../04-climate-system-and-feedbacks/03-climate-sensitivity.md) —
  the response coefficient and its relation to the feedback parameter.

## 1. Intuition: why a small push can do nothing, then everything

A linear system responds to a forcing change in proportion to the forcing: halve
the forcing, halve the response. Systems with a feedback strong enough to create
several steady states do not behave that way. Over most of the range they resist
— the response is small and reversible — and then, past a threshold, the state
jumps to a different branch, irreversibly in the sense that undoing the forcing
does not undo the state.

Three ideas must be kept apart, because they are frequently conflated:

- **Abruptness of the forcing** is an external property (a volcanic eruption, a
  meltwater pulse). It can be abrupt without any tipping.
- **Abruptness of the response** is a property of the system: a slow forcing
  change can produce a rapid transition if the system crosses a bifurcation.
- **Reversibility** is separate again. A large but smooth response to a smooth
  forcing is not a tipping point unless the reverse path differs.

This lesson builds two small systems, one oceanic and one radiative, in which
these distinctions can be measured rather than asserted.

## 2. Definitions

- **Tipping point.** A threshold in a control parameter beyond which the state
  changes to a qualitatively different one. It is a property of a model; applied
  to the Earth it is an inference.
- **Bistability.** The existence of two stable steady states at the same
  parameter value.
- **Fold (saddle-node) bifurcation.** The parameter value at which a stable and
  an unstable steady state appear or annihilate, marking the edge of a
  bistable range.
- **Hysteresis.** The dependence of the state on the *history* of the control
  parameter, observed as different forward and backward branches.
- **Circulation index $q$.** Here, a dimensionless measure of the two-box
  overturning: positive when the thermal (temperature-driven) contribution
  dominates, negative when the haline (salinity-driven) contribution does.
- **Snowball (ice-albedo) bistability.** Two stable temperatures for the same
  solar forcing, one warm and ice-free, one cold and ice-covered, arising
  because a high albedo is self-sustaining.

## 3. Derivation: the two-box circulation model

### 3.1 The model

Take two well-mixed boxes, one polar (subscript $p$) and one equatorial
(subscript $e$), with temperatures $T$ and salinities $S$. Let
$\Delta T = T_e - T_p$ and $\Delta S = S_e - S_p$. The temperature relaxes to a
reference at rate $\gamma_T$; the transport, whose magnitude is $|q|$, mixes the
boxes. Salinity has **no restoring term**: its difference is set by the balance
between salt transport and the freshwater flux $H$ (this is the classic Stommel
closure). With scales $\Delta T_{\text{ref}}$ and $\Delta S_{\text{ref}}$:

$$\frac{\mathrm d\Delta T}{\mathrm dt} = \gamma_T(\Delta T^{*}-\Delta T) - 2|q|\Delta T,
\qquad
\frac{\mathrm d\Delta S}{\mathrm dt} = -2|q|\Delta S + 2H,$$

$$\boxed{\;q = \frac{\Delta T}{\Delta T_{\text{ref}}}
- \frac{\Delta S}{\Delta S_{\text{ref}}}.\;}$$

With the demonstration's chosen values $\gamma_T = 1.0$,
$\Delta T^{*} = 20\ \mathrm{K}$, $\Delta T_{\text{ref}} = 20\ \mathrm{K}$,
$\Delta S_{\text{ref}} = 2\ \mathrm{psu}$ and $H$ in $\mathrm{psu}$ per unit
time, the steady state satisfies

$$\Delta T = \frac{20}{1+2|q|},\qquad \Delta S = \frac{H}{|q|},
\qquad q = \frac{1}{1+2|q|} - \frac{H}{2|q|}.$$

### 3.2 Why a fold must exist

The right-hand side is a function of $|q|$ only. Write it $G(|q|)$. For small
$|q|$ the second term dominates and $G$ is large and negative; for large $|q|$
it approaches zero from above or below depending on $H$. A steady state solves
$q = G(|q|)$, i.e. the graph of $q\mapsto G(|q|)$ must cross the line
$q = q$. Because $G$ has an interior maximum in the region where the two terms
trade off, the crossing can happen three times — and where it does, there are
two stable states separated by an unstable one. That is a fold, and it is a
property of the *functional form*, not of the particular numbers chosen.

### 3.3 Reading stability

The direction of the flow in the $\Delta S$ equation gives the stability of the
salinity mode; combined with the temperature equation, the steady state with the
intermediate $|q|$ is unstable, and the two outer ones are stable. The
demonstration confirms this by finding three roots and by integrating from
different initial conditions to different branches.

## 4. Measurement: the hysteresis loop

The demonstration starts from a symmetric state ($\Delta S = 0$, $q = 0.5000$),
ramps $H$ from $0.00$ to $1.20$ in 49 steps, then ramps it back, allowing
$200$ time units at each step to reach a steady state.

| $H$ | $q$ forward | $q$ backward | $\Delta T$ (K) | $\Delta S$ (psu) |
|---|---|---|---|---|
| 0.000 | $+0.5000$ | $+0.5000$ | 10.000 | 0.0000 |
| 0.125 | $+0.3994$ | $-0.0658$ | 11.118 | 0.3129 |
| 0.250 | $-0.1355$ | $-0.1355$ | 15.735 | 1.8445 |
| 0.500 | $-0.2718$ | $-0.2718$ | 12.956 | 1.8393 |
| 1.000 | $-0.5000$ | $-0.5000$ | 10.000 | 2.0000 |
| 1.125 | $-0.5486$ | $-0.5486$ | 9.537 | 2.0508 |

The two branches differ by up to $\lvert\Delta q\rvert = 0.4955$, over a forcing
range of about $0.025$ to $0.200$ psu per unit time. Outside that range the
forward and backward paths coincide: the system is on a single branch and
the response is reversible.

Note also how $\Delta T$ behaves: it is *largest* at intermediate $H$
($15.735\ \mathrm{K}$ at $H = 0.25$) rather than at either end. The transport
term is weakening with $|q|$, so a weaker circulation supports a larger
temperature difference while the salinity difference grows and eventually
reverses the sign of $q$. A counter-intuitive internal result like this is a
reason to distrust summary statements about "stronger circulation" without the
model in front of you.

## 5. Measurement: the fold, by root finding

Scanning $q$ and refining sign changes of $q - G(|q|)$ for each $H$:

| $H$ | number of solutions | solutions ($q$) |
|---|---|---|
| 0.00 | 1 | $+0.5000$ |
| 0.05 | 3 | $-0.0256$, $+0.0271$, $+0.4646$ |
| 0.10 | 3 | $-0.0522$, $+0.0600$, $+0.4234$ |
| 0.15 | 3 | $-0.0796$, $+0.1034$, $+0.3718$ |
| 0.20 | 3 | $-0.1075$, $+0.1803$, $+0.2868$ |
| 0.30 | 1 | $-0.1636$ |
| 0.45 | 1 | $-0.2456$ |
| 0.90 | 1 | $-0.4590$ |

Three steady states exist for $H$ between about $0.05$ and $0.20$ (the exact
fold values lie between the sampled grid points; the branch table in Section 4
puts the lower edge between $0.025$ and $0.200$ for a $|\Delta q| > 0.05$
criterion). Within that window the two outer solutions are the two states the
system can occupy, selected by its initial condition; the middle one
($+0.0271$, $+0.0600$, $+0.1034$, $+0.1803$) is unstable.

The statement "the circulation collapsed at $H^{*}$" is therefore imprecise.
The correct statement is: *for $H$ above the fold, the thermal branch no longer
exists as a steady solution, so the system must be on the haline branch; for $H$
between the folds, both branches exist and the state depends on the path taken.*

## 6. Ice-albedo bistability and the fragility of a threshold

The second system is a zero-dimensional energy balance,

$$Q\,(1-\alpha(T)) = A + BT,
\qquad
\alpha = \begin{cases}0.30, & T > -10\ \mathrm{{}^{\circ}C},\\
0.62, & T \le -10\ \mathrm{{}^{\circ}C},\end{cases}$$

with $A = 210\ \mathrm{W\,m^{-2}}$ and $B = 2.0\ \mathrm{W\,m^{-2}\,K^{-1}}$
(the same synthetic values as
[16-05-01 Model Hierarchy](../05-climate-models/01-climate-model-hierarchy.md)),
and $Q$ the absorbed-flux equivalent of the solar forcing. Solving each branch
and requiring self-consistency:

- Both branches are self-consistent for
  $Q \in [271.5,\ 499.5]\ \mathrm{W\,m^{-2}}$.
- Present-day $Q = S/4 = 1361/4 = 340.25\ \mathrm{W\,m^{-2}}$ lies inside that
  range, giving a warm branch of $+14.09\ \mathrm{{}^{\circ}C}$ and a cold branch
  of $-40.35\ \mathrm{{}^{\circ}C}$.

**This is a statement about the model.** The model has no clouds, no ocean, no
ice flow and a step-function albedo. What the exercise demonstrates is the
*structure* of the problem: with an albedo feedback, two stable climates can
exist for the same forcing, and the boundary between them is a fold.

Now change one closure parameter, the ice albedo:

| ice albedo | bistable range starts (W/m²) | ends (W/m²) | width (W/m²) |
|---|---|---|---|
| 0.50 | 271.5 | 379.5 | 108.0 |
| 0.62 | 271.5 | 499.5 | 228.0 |
| 0.72 | 271.5 | 678.5 | 407.0 |

The lower edge is fixed by the warm-branch condition (it depends only on the warm
albedo and the threshold); the upper edge moves by $299\ \mathrm{W\,m^{-2}}$ as
the ice albedo moves by $0.22$. A threshold estimate from a model of this kind is
therefore *conditional on a closure*, and reporting it without the closure would
be reporting a property of the parameter choice as though it were a property of
the Earth.

## 7. Worked example: verifying one root by hand

*Problem.* Verify that $q = -0.1075$ is a steady solution of the saline branch at
$H = 0.20$.

*Solution.* With $|q| = 0.1075$:

1. $\Delta T = 20/(1+2(0.1075)) = 20/1.215 = 16.4605\ \mathrm{K}$, so
   $\Delta T/20 = 0.82303$.
2. $\Delta S = 0.20/0.1075 = 1.86047\ \mathrm{psu}$, so
   $\Delta S/2 = 0.93023$.
3. $G = 0.82303 - 0.93023 = -0.10721$.

The computed $G = -0.10721$ differs from the assumed $q = -0.1075$ by
$2.9\times10^{-4}$, i.e. by $0.27\%$ — the residual expected from the rounding
of the printed root to four decimals. Repeating the substitution from
$q = -0.10721$ gives $\Delta T = 20/(1+0.21442) = 16.4687$,
$\Delta S = 0.20/0.10721 = 1.86549$, and
$G = 0.82343 - 0.93275 = -0.10932$: the residual *grows*.

*Interpretation.* That growth is a property of the fixed-point map, not a
verdict on the steady state: here $|G'| \approx 7.3 > 1$ near the root, so
naive substitution is not a contraction and bisection (as in the demonstration)
is the correct tool. Convergence of an iteration and stability of a steady state
are different questions, and conflating them is a standard error. The hand
calculation gives a residual, not a proof; the demonstration's root finder
bisects to $10^{-6}$, and the arithmetic above reproduces it to four decimals.

## 8. Assumptions and regime of validity

1. **Two boxes.** The model has one polar and one equatorial reservoir. Real
   overturning has continuous structure, multiple water masses and strong
   regional dependence.
2. **No salinity restoring.** The classic Stommel closure omits any relaxation of
   salinity to a reference. Adding a restoring term changes the location and
   existence of the fold — this is a closure choice with a qualitative effect.
3. **Instantaneous, complete mixing.** Each box is assumed well mixed;
   finite mixing timescales change the transient behaviour.
4. **Symmetry and no seasonal cycle.** The demonstration uses symmetric
   reference temperatures; a seasonal cycle or asymmetric geometry shifts the
   fold.
5. **The forcing is a steady ramp.** Rate-induced effects — a threshold that
   depends on how fast the forcing moves, not only on how far — are outside this
   analysis.
6. **The energy-balance threshold is a step function.** Sharp albedo thresholds
   are an idealisation; smooth albedo functions give a smoother but still
   nonlinear response.
7. **Model thresholds are not Earth thresholds.** Every number in Sections 4–6
   is a property of the equations and parameters in the demonstration. No
   inference about any real climate component follows from them without a
   validated model of that component.

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| freshwater flux | $H$ | psu per unit time | salinity per time |
| circulation index | $q$ | 1 | dimensionless by construction |
| temperature difference | $\Delta T$ | K | $\gamma_T\Delta T^{*}/(\gamma_T+2|q|)$ |
| salinity difference | $\Delta S$ | psu | $H/|q|$ |
| absorbed flux | $Q$ | $\mathrm{W\,m^{-2}}$ | $S/4$ |
| albedo | $\alpha$ | 1 | |

The two box equations must be dimensionally consistent before they are coupled:
$|q|$ appears as a rate multiplying a difference (K or psu) and as a
dimensionless index in the definition of $q$. The model is built by taking the
scales $\Delta T_{\text{ref}}$ and $\Delta S_{\text{ref}}$ to be one unit each,
which is what makes $q$ dimensionless; changing either scale rescales the fold.

## 10. Python demonstration

[`code/abrupt_climate_change_demo.py`](code/abrupt_climate_change_demo.py):

1. ramps the freshwater forcing forward and backward and tabulates the
   hysteresis loop;
2. finds the steady solutions by scanning and bisection, and shows that three
   exist over a range of forcing;
3. solves the two-branch energy-balance model, reports the bistable range and the
   two stable temperatures at the present-day absorbed flux;
4. repeats the range calculation for three ice albedos to show the sensitivity of
   the thresholds to the closure.

It is print-only, seeded with `np.random.default_rng(20261014)`, and exits 0.

## 11. Exercises

See [`exercises/03-abrupt-climate-change-exercises.md`](exercises/03-abrupt-climate-change-exercises.md)
and [`exercises/03-abrupt-climate-change-solutions.md`](exercises/03-abrupt-climate-change-solutions.md).

## Mastery checkpoint

> **(a)** Write the steady-state condition of the two-box model for $H = 0.1$ and
> verify by substitution that $q = -0.0522$ satisfies it to three decimals.
> **(b)** The fold exists between $H = 0.05$ and $H = 0.20$ in the demonstration.
> Explain why three solutions can appear and why the middle one is unstable.
> **(c)** For the energy-balance model, compute the two branch temperatures at
> $Q = 400\ \mathrm{W\,m^{-2}}$ and state whether both are self-consistent.
> **(d)** The upper edge of the bistable range moves from $379.5$ to
> $678.5\ \mathrm{W\,m^{-2}}$ when the ice albedo changes from $0.50$ to $0.72$.
> Compute the change per $0.01$ of albedo and state what kind of uncertainty this
> illustrates.
> **(e)** A model run shows a rapid change in a diagnostic. List two checks that
> distinguish a genuine bifurcation from a diagnostic artefact.

## Common pitfalls

1. **Reporting a model threshold as an Earth threshold.** The threshold is
   conditional on the closure, as Section 6 measures.
2. **Equating abruptness with tipping.** A fast response to a fast forcing is not
   a bifurcation.
3. **Assuming reversibility.** Hysteresis means the reverse path differs; measure
   both directions.
4. **Ignoring the initial condition.** Inside a bistable range, the state depends
   on where the trajectory started.
5. **Treating the ensemble mean of a bistable system as meaningful.** If members
   occupy different branches, the mean lies between the branches and describes
   neither.
6. **Confusing an unstable solution with an unphysical one.** The middle branch
   is a real steady solution; it is simply not attracting.

## Related modules

- [16-06 Palaeoclimate](README.md).
- [16-04-02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](../04-climate-system-and-feedbacks/02-climate-feedbacks.md) —
  what makes a feedback strong enough to create multiple states.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  internal variability, often confused with abrupt change.
- [16-05-05 CMIP, Model Intercomparison and Ensemble Design](../05-climate-models/05-coupled-model-intercomparison.md) —
  why an ensemble mean is the wrong statistic for a bistable system.
- [01-08 Ordinary Differential Equations](../../01-mathematics/08-ordinary-differential-equations/README.md) —
  fixed points, stability and bifurcation in general.
