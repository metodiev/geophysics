# Module 14-03 — Petrophysical Relations for Saturated Media

**Stages:** graduate → research · **Prerequisites:** modules
[05-04](../../05-core-geophysics/04-rock-physics/README.md),
[09-01](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md)
and [14-01](../01-hydrology-fundamentals/README.md).

Geophysics measures bulk properties — resistivity, velocity, density — and
hydrology needs flow properties and water content. This module is about the
transforms between them: the porosity–permeability relation of Kozeny and
Carman, Archie's formation factor and saturation law, Gassmann's fluid
substitution with the two fluid-mixing limits, and the construction of a
composed proxy with a quantified uncertainty. It is the bridge between the
surveys of module 14-02 and the hydrological questions of module 14-01.

The module's stance is that every one of these transforms is a *model with
assumptions*, not a conversion factor. Each lesson derives what can be derived
(a bundle-of-tubes formation factor, the $\phi^{3}$ scaling, the
$K_\text{fl} = K_\text{min}$ limit of Gassmann), fits what cannot (the Kozeny
constant, the cementation exponent, the saturation exponent, the dry frame),
and then measures the failure numerically — the clay over-prediction, the
impossible saturation, the $309\ \mathrm{m\,s^{-1}}$ gap between two fluid
geometries. The final lesson turns the whole thing into an error budget and asks
the only question that matters: is the answer good enough for the decision?

**All models and data in this module are SYNTHETIC.** Grain sizes, porosities,
exponents, resistivities, moduli and posteriors are chosen teaching values, not
measurements from any site. The only numbers treated as constants are exact unit
definitions and the standard bulk moduli and densities of water, air and quartz
substitutes, each stated with its unit where used.

## Learning objectives

By the end of this module you will be able to:

1. Derive the capillary-bundle permeability and show it is algebraically
   identical to Kozeny–Carman, then quantify the sensitivity of $k$ to porosity,
   grain size and the Kozeny constant.
2. Convert intrinsic permeability to hydraulic conductivity with the fluid
   properties stated, and recognise the unit traps.
3. Derive the formation factor of a simplified pore geometry, explain why
   Archie's cementation exponent is fitted rather than derived, and invert a
   resistivity for a water saturation.
4. Diagnose clay conduction from an inverted $S_w > 1$ and use the size of the
   excess as information rather than discarding it.
5. Apply Gassmann fluid substitution correctly, verify it against its two
   analytic limits, and compute $V_p(S_w)$ under uniform and patchy mixing.
6. Quantify the non-uniqueness of saturation from velocity alone and state the
   measurement that resolves it.
7. Compose the transforms into a proxy, compute the amplification factor, build a
   two-parameter posterior and decide whether the result answers the question.

## Prerequisites

- [Module 05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md) —
  porosity–density–velocity relations, effective-medium bounds, Gassmann, and
  Archie from the rock-physics side.
- [Module 09-01 Electrical Properties of the Earth](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md) —
  conduction mechanisms, Archie's law and clay conduction.
- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  Darcy's law, aquifer types, groundwater chemistry and the unsaturated zone.
- [Module 18-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md)
  and [Module 21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md)
  for lesson 04: forward operators, ill-posedness, likelihoods and posteriors.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Porosity-Permeability and Kozeny-Carman Relations](01-porosity-permeability-relations.md) | doctoral | $k \propto \phi^{3}d^{2}$; porosity alone cannot determine permeability |
| 02 | [Archie's Law and Saturation Estimation](02-archie-and-saturation.md) | graduate | $m>1$ is fitted, not derived; $S_w > 1$ is a measurement of clay |
| 03 | [Seismic Velocity vs Saturation and Gassmann](03-seismic-velocity-saturation.md) | doctoral | The fluid geometry matters as much as the saturation |
| 04 | [Building Geophysical Proxies for Hydrological Properties](04-geophysical-proxy-relations.md) | research | Amplification is the transform's; non-uniqueness is the data's |

## Suggested path

**If you are new to petrophysics:** lessons 01 and 02 in order, running each
demonstration. Lesson 02 is where the numbers become field-like; lesson 01 is
where the arithmetic that governs everything else appears.

**If you already know Archie and Gassmann:** read 01 §5 (scaling and
amplification), 02 §8 (the $S_w>1$ diagnostic), 03 §4 (the gap between the two
mixing models) and then all of 04.

**If you are preparing a research project:** 01 §10, 03 §9–10 and all of 04, plus
the ★★★ exercises. The error budget in 04 §7 is the template to reuse.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-porosity-permeability-relations.md`](01-porosity-permeability-relations.md) | Lesson 01 |
| [`02-archie-and-saturation.md`](02-archie-and-saturation.md) | Lesson 02 |
| [`03-seismic-velocity-saturation.md`](03-seismic-velocity-saturation.md) | Lesson 03 |
| [`04-geophysical-proxy-relations.md`](04-geophysical-proxy-relations.md) | Lesson 04 |
| [`code/`](code) | Four runnable demonstrations, one per lesson |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and SymPy:

```bash
cd 14-hydrology-hydrogeophysics/03-petrophysics-hydrology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python porosity_permeability_relations_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python archie_and_saturation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_velocity_saturation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geophysical_proxy_relations_demo.py
```

Every demo is print-only (no figures, no `plt.show()`), uses the fixed seed
`np.random.default_rng(20261014)` where it needs randomness, prints labelled
results with units and the label `SYNTHETIC` on model inputs, runs in under a
second, needs no network access, and exits 0.

## Mastery checkpoint

Complete this without notes.

> A synthetic aquifer rock has $\phi = 0.22$, mean grain diameter
> $d = 0.15\ \mathrm{mm}$, and a pore fluid of $\rho_w = 2.00\
> \Omega\,\mathrm{m}$. **(a)** Compute $S_0$, $R_h$ and $k$ for $\tau = 2.5$, and
> convert to hydraulic conductivity for water at $20\ ^\circ\mathrm{C}$.
> **(b)** A resistivity of $70\ \Omega\,\mathrm{m}$ is measured with
> $a = 1$, $m = 2$, $n = 2$; compute $S_w$ and state three assumptions.
> **(c)** Compute $K_\text{sat}$ and $V_p$ for $K_\text{dry} = 9.0$,
> $\mu_\text{dry} = 8.0$, $K_\text{min} = 36.0\ \mathrm{GPa}$ at $S_w = 1$ under
> uniform mixing. **(d)** State which of the two measured quantities better
> constrains porosity and why. **(e)** Write the error budget for the proxy
> $\rho_t \to \phi \to k$ and name the term you would attack first.

## Common pitfalls

1. **Quoting a transform's output without its assumptions.** Every number in
   this module is conditional.
2. **Confusing intrinsic permeability with hydraulic conductivity.** They differ
   by $\rho_f g/\mu$, which is $9.769\times10^{6}\ \mathrm{s\,m^{-1}}$ for water
   at $20\ ^\circ\mathrm{C}$.
3. **Clipping an impossible saturation.** $S_w > 1$ is the measurement of the
   model error.
4. **Using $K_\text{sat}$ where Gassmann requires $K_\text{dry}$.**
5. **Assuming a fluid geometry silently.** Uniform and patchy mixing differ by
   $309\ \mathrm{m\,s^{-1}}$ in $V_p$ at the same saturation.
6. **Mixing units conventions in a sensitivity factor.** $3/\phi + 2/(1-\phi)$
   acts on an absolute porosity; $-1/m$ acts on a relative resistivity.
7. **Acquiring more of the same data.** Amplification is not reduced by repeating
   the same measurement; only a differently shaped sensitivity helps.

## Related modules

- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  Darcy, storativity, well hydraulics, unsaturated zone.
- [Module 14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) —
  the surveys whose outputs these transforms consume.
- [Module 14-04 Contaminant and Environmental Geophysics](../04-contaminant-and-environmental/README.md) —
  where the fluid *changes* rather than the saturation.
- [Module 14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  the same transforms applied to differences between surveys.
- [Module 05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md).
- [Module 09-01 Electrical Properties of the Earth](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md).
- [Module 18 Inverse Problems](../../18-inverse-problems/README.md) — the
  systematic treatment of non-uniqueness, regularisation and uncertainty.
