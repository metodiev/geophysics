---
id: 09-02-03
title: "Apparent Resistivity and Geometric Factors"
level: advanced
prereqs: ["09-02-01", "09-02-02"]
tags: [electrical-methods, apparent-resistivity, sounding-curve, equivalence, non-uniqueness]
---

# Apparent Resistivity and Geometric Factors

Apparent resistivity is a *number that makes a measurement look like a
resistivity*. Over a uniform half-space it is exact; over anything else it is a
weighted average whose weights change with spacing. This lesson computes real
sounding curves for two-layer models, derives the two equivalence relations that
limit every sounding, and shows how to state the admitted model family instead
of a single number.

**All models and data in this module are SYNTHETIC.** The layered models, the
resistivities and the noise level are chosen teaching values; no field data are
used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a Wenner sounding curve for a two-layer model and identify its
   asymptotes.
2. **Explain** why $\rho_a$ equals the true resistivity at both limits and
   nowhere in between.
3. **Compute** the voltage a receiver must resolve for a stated array and
   apparent resistivity.
4. **Derive** the transverse-resistance equivalence ($h\rho$ constant for a thin
   *resistive* layer) and the longitudinal-conductance equivalence
   ($h/\rho$ constant for a thin *conductive* layer), and state which applies
   when.
5. **Quantify** an equivalence family with numbers rather than words.
6. **Compute** a $\chi^{2}$ test against an assumed noise level and report the
   admitted family of models.
7. **Explain** why a single sounding can never give both the thickness and the
   resistivity of a thin layer.

## Prerequisites

- [09-02-01 Resistivity Principle and the Four-Electrode Arrangement](01-resistivity-principle.md) —
  the geometric factor.
- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md) —
  spacings, signal and sensitivity.

## 1. A two-layer sounding curve

Take a SYNTHETIC two-layer model: $\rho_1 = 100\ \Omega\,\mathrm{m}$,
$h_1 = 10\ \mathrm{m}$, and a half-space $\rho_2$ of either 1000 or
$10\ \Omega\,\mathrm{m}$. The demo computes a Wenner sounding with the exact
layered solution:

| $a$ (m) | 0.5 | 2 | 5 | 8 | 12 | 20 | 30 | 50 | 80 | 120 | 200 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $\rho_a$, $\rho_2 = 1000$ | 100.00 | 100.27 | 103.62 | 111.67 | 127.30 | 162.65 | 202.88 | 266.38 | 332.96 | 390.73 | 454.47 |
| $\rho_a$, $\rho_2 = 10$ | 100.00 | 99.78 | 97.20 | 91.46 | 81.85 | 66.93 | 58.95 | 55.63 | 55.16 | 55.06 | 55.02 |
| $\Delta V$ (V), resistive case, $I = 0.1$ A | 3.183238 | 0.797934 | 0.329836 | 0.222151 | 0.168838 | 0.129431 | 0.107630 | 0.084790 | 0.066240 | 0.051822 | 0.036166 |

Three features matter. First, at small spacing $\rho_a \to \rho_1 = 100.00\
\Omega\,\mathrm{m}$ for both models; at large spacing it tends to $\rho_2$ (454
and 55 $\Omega\,\mathrm{m}$ at $a = 200$ m, still approaching 1000 and 10 — the
approach is slow because $\rho_a$ is an average over a growing volume). Second,
a conductive half-space pulls $\rho_a$ *down* and a resistive one pulls it *up*;
the sign is the first thing to read from a sounding. Third, the maximum
deviation from $\rho_1$ exceeds 5% only for $a \gtrsim 5$ m: **the horizontal
resolution of a sounding is about one layer thickness**, and the crossing of the
curve through the geometric mean of the two resistivities happens where the
array aperture is a few times $h_1$.

## 2. What the receiver must deliver

$\Delta V = \rho_a I/k$ with $k = 2\pi a$ for Wenner, so for a fixed
$\rho_a = 100\ \Omega\,\mathrm{m}$ and $I = 0.1\ \mathrm{A}$:

| $a$ (m) | 1 | 5 | 20 | 100 | 500 |
|---|---|---|---|---|---|
| $k$ (m) | 6.28 | 31.42 | 125.66 | 628.32 | 3141.59 |
| $\Delta V$ (mV) | 1591.55 | 318.31 | 79.58 | 15.92 | 3.18 |

A sounding is therefore a battle between two fixed trends: **longer spacings
carry deeper information and less voltage**, and the ratio is set by geometry
alone. A 100 mV signal at $a = 20$ m becomes the noise floor at
$a \approx 1$ km for the same current — which is why deep soundings use high
current, long stacking, or both, and why the design question is always
"how much voltage can I afford at the spacing that reaches my target?"

## 3. Worked example: a two-layer inversion by inversion of the asymptotes

For the resistive case, suppose only two spacings are measured: $a = 2$ m gives
$\rho_a = 100.27$ and $a = 8$ m gives $\rho_a = 111.67$. Assume the small-spacing
limit is the top layer: $\rho_1 \approx 100.3\ \Omega\,\mathrm{m}$. Assume the
half-space is resistive, and use the standard two-layer approximation that at
$a = h_1$ the apparent resistivity is the geometric mean of $\rho_1$ and
$\rho_2$ — check it against the model:

$$\sqrt{\rho_1\rho_2} = \sqrt{100\times1000} = 316.2\ \Omega\,\mathrm{m},$$

which the table reaches only at $a \approx 75$ m, **not** at $a = h_1 = 10$ m
where the model gives 120.3 $\Omega\,\mathrm{m}$. The "geometric mean at the
layer thickness" rule of thumb is off by a factor 2.6 here. The lesson: use the
exact forward model, and use an inversion
([09-02-07](07-resistivity-inversion.md)) rather than a nomogram rule.

## 4. The two equivalences

Consider a thin layer of thickness $h$ and resistivity $\rho$ between two
others, in the limit $h \ll$ electrode spacing. Two limits are exact and they
are different:

- **Thin resistive layer** ($\rho$ larger than its neighbours): current crosses
  it nearly vertically, so the layer acts as a series resistance per unit area,
  the **transverse resistance**

  $$T = h\rho \qquad (\Omega\,\mathrm{m^{2}}).$$

- **Thin conductive layer** ($\rho$ smaller than its neighbours): current flows
  along it, so the layer acts as a shunt, the **longitudinal conductance**

  $$S = \frac{h}{\rho} \qquad (\mathrm{S}),\qquad 1\ \mathrm{S} = 1\
  \Omega^{-1}.$$

The demo tests this: for the resistive case
$\rho = (100, 500, 20)\ \Omega\,\mathrm{m}$, $h = (5, 4)\ \mathrm{m}$, so
$T = 2000\ \Omega\,\mathrm{m^{2}}$, and it holds $T$ fixed while varying the
layer:

| $h_2$ (m) | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| $\rho_2$ kept at $T/h_2$ ($\Omega\,\mathrm{m}$) | 2000 | 1000 | 500 | 250 | 125 |
| max $\lvert\Delta\rho_a\rvert/\rho_a$ | 1.585% | 1.254% | 0% | 4.021% | 13.988% |
| mean $\rho_a$ ($\Omega\,\mathrm{m}$) | 94.39 | 94.30 | 93.94 | 92.75 | 89.76 |

A **factor 16 in thickness and in resistivity** produces at most a 4% change
over the spacing range used. For the conductive case
$\rho = (100, 5, 500)\ \Omega\,\mathrm{m}$, $h = (5, 4)$ m, $S = 0.8\ \mathrm{S}$:

| $h_2$ (m) | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| $\rho_2 = h_2/S$ ($\Omega\,\mathrm{m}$) | 1.25 | 2.50 | 5.00 | 10.00 | 20.00 |
| max $\lvert\Delta\rho_a\rvert/\rho_a$ | 0.525% | 0.419% | 0% | 1.530% | 6.329% |

The equivalence weakens as the layer thickens, which is exactly the statement
that the limit is $h \ll$ spacing. **Only $T$ or $S$ is measured; the thickness
appears only through the ratio.**

## 5. Equivalence against noise: the admitted family

The tables in Section 4 assume perfect data. With 2% noise on $\Delta V$, the
demo computes $\chi^{2}$ per datum between each member of the family and the
reference curve:

| $h_2$ (m) | max $\lvert\Delta\rho_a\rvert/\rho_a$ | inside the noise? | $\chi^{2}$ |
|---|---|---|---|
| 1 | 1.585% | yes | 0.15 |
| 2 | 1.254% | yes | 0.09 |
| 4 | 0.000% | yes | 0.00 |
| 8 | 4.021% | marginal | 1.03 |
| 16 | 13.988% | no | 11.95 |

So at 2% noise this sounding admits thicknesses from about 1 to 8 m for a
resistive layer whose transverse resistance is known to 1%: an **eight-fold
range in thickness**. Reporting "$h = 4$ m" from this data is a choice, not a
measurement. The $\chi^{2}$ value is the honest statement; it is also the input
that [09-02-07](07-resistivity-inversion.md) turns into a model covariance.

## 6. Regime of validity

1. **One-dimensional, layered ground.** Lateral variation makes $\rho_a$ depend
   on the traversed geology ([09-02-04](04-sounding-profiling.md)).
2. **Small perturbations in the equivalence analysis.** The equivalences are
   limits; at 4–16 m thickness the 13.988% deviation shows the limit failing.
3. **Known array geometry.** Geometry errors propagate into $\rho_a$ at
   0.13–0.31% per centimetre over a layered ground
   ([09-02-01](01-resistivity-principle.md)).
4. **$\Delta V$ is the measured quantity, not $\rho_a$.** Noise enters in volts;
   converting to resistivity first hides where the noise came from.
5. **No polarisation.** A ground with IP has a frequency-dependent $\rho_a$; the
   values here are the high-frequency or instantaneous limit.

## 7. Mastery checkpoint

1. From the two-layer table, estimate the spacing at which $\rho_a$ is halfway
   (in the log sense) between $\rho_1$ and $\rho_2$ for the conductive case, and
   compare it with $h_1$.
2. Compute $\Delta V$ for a Wenner array with $a = 50$ m reading
   $\rho_a = 30\ \Omega\,\mathrm{m}$ at $I = 0.25\ \mathrm{A}$.
3. A thin layer has $\rho = 1000\ \Omega\,\mathrm{m}$, $h = 2$ m in a
   100 $\Omega\,\mathrm{m}$ host. Compute $T$ and predict the sounding change
   for a second model with $\rho = 500\ \Omega\,\mathrm{m}$, $h = 4$ m.
4. State, with numbers, the thickness range your answer to (3) leaves unresolved
   at 2% noise.

## 8. Common pitfalls

1. **Reading $\rho_a$ as a layer resistivity.** It equals a layer resistivity
   only in the two asymptotic limits.
2. **Using the geometric-mean rule at $a = h$.** Section 3 shows the rule is off
   by a factor 2.6 for a 10:1 contrast.
3. **Reporting one thickness from an equivalent family.** Always state the
   admitted range.
4. **Confusing the two equivalences.** $T = h\rho$ for resistive layers,
   $S = h/\rho$ for conductive ones; swapping them changes the answer by
   $\rho^{2}$.
5. **Forgetting the signal cost of long spacings.** $\Delta V \propto 1/a$
   exactly.

## 9. Related modules

- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md).
- [09-02-04 Vertical Electrical Sounding vs Profiling](04-sounding-profiling.md).
- [09-02-06 Forward Modelling Resistivity Data](06-resistivity-forward-modelling.md) —
  where the curves come from.
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](07-resistivity-inversion.md) —
  what to do with them.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md).

## 10. Demonstration and exercises

- [`code/apparent_resistivity_demo.py`](code/apparent_resistivity_demo.py)
  prints the two-layer curves, the voltage table, the two equivalence families
  and the $\chi^{2}$ analysis.
- [Exercises](exercises/03-apparent-resistivity-exercises.md) and
  [worked solutions](exercises/03-apparent-resistivity-solutions.md).
