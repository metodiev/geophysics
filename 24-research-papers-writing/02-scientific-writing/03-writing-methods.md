---
id: 24-02-03
title: "Writing Methods Sections That Can Be Reproduced"
level: doctoral
prereqs: ["24-02-02", "24-01-03"]
estimated_minutes: 60
tags: [writing, methods, reproducibility, sensitivity, parameters]
---

# Writing Methods Sections That Can Be Reproduced

A Methods section has one job: to let a competent stranger reproduce the result.
That is a stronger requirement than describing what you did, because it demands
knowing **which details change the answer**. This lesson measures that: given a
processing chain with several parameters, which unreported parameter destroys
reproduction, and how quickly does a reader's chance of matching your number
collapse as reporting becomes partial?

The organising idea is **sensitivity before completeness**. A parameter list is
not a document of everything you touched; it is a ranked statement of what
matters. The demonstration's chain has elasticities spanning a factor of $6$, so
reporting the most influential parameter first is worth more than reporting the
three least influential ones together.

> **Data provenance.** All numbers are **SYNTHETIC**. The chain
> $y = 100\exp(\sum_i e_i d_i)$ is a teaching surrogate with chosen elasticities;
> it is not a geophysical forward model, no seismic data are processed and no
> software is invoked. The parameter names are generic placeholders.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** an elasticity as the fractional output change per fractional
   parameter change and **compute** it for a parameter of a processing chain.
2. **Rank** a parameter set by influence and **state** which parameters must be
   reported for reproduction within a stated tolerance.
3. **Compute** the uncertainty a reader inherits from a set of unreported
   parameters, given a plausible range for each, and **express** it as an interval
   for the reported quantity.
4. **Explain** why partial reporting barely improves reproduction and why complete
   reporting changes the regime entirely.
5. **Write** a Methods section structured as decisions, each with its value, its
   range and its consequence, rather than as a chronological account.
6. **State** the one thing a Methods section cannot promise: that the same inputs
   give the same output on a different implementation.

## Prerequisites

- [24-02-02 Paper Structure: IMRaD and Its Variants](02-paper-structure.md) —
  where the Methods budget sits.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  the audit that reads a published Methods section.

## 1. What reproducibility requires

Three levels are worth separating:

| Level | Requirement | Usually sufficient when |
|---|---|---|
| Repeatability | Same code, same data, same machine | You are the reader |
| Reproducibility | Same inputs, independent implementation | Parameters and versions are stated |
| Replicability | New data, same method | The method is described in prose |

A Methods section supports *reproducibility*. It cannot support replicability,
which is a new experiment, and it cannot guarantee repeatability, which needs the
code and the environment (see
[24-06-01 Publishing Data and Code](../06-reproducible-publication/01-data-publication.md)).

## 2. Elasticity: which parameters matter

For a processing chain $y = f(p_1,\dots,p_k)$, the elasticity of parameter $i$ is

$$e_i = \frac{\partial \ln y}{\partial \ln p_i},$$

the fractional change in the output per fractional change in the parameter. It is
dimensionless, so elasticities of parameters in different units can be compared
directly — which is exactly what a Methods section needs, because it must spend
its word budget in proportion to influence.

The demonstration's chain is $y = 100 \exp(\sum_i e_i d_i)$ with $d_i$ the
deviation of parameter $i$ from its nominal value expressed as a fraction of a
plausible half-range. The chosen elasticities are $0.30$ (high-cut corner),
$0.45$ (taper length), $0.20$ (window length), $0.35$ (velocity step), $0.10$
(damping factor) and $0.60$ (elevation correction).

**Measured sensitivity.** Moving each parameter by $10\%$ of its half-range gives

| Parameter | Output change |
|---|---|
| elevation correction | $+6.18\%$ |
| taper length | $+4.60\%$ |
| velocity step | $+3.56\%$ |
| high-cut corner | $+3.05\%$ |
| window length | $+2.02\%$ |
| damping factor | $+1.01\%$ |

The ratio between the most and least influential parameter is $6.0$. A Methods
section that names the damping factor but not the elevation-correction choice has
spent words in inverse proportion to their importance.

## 3. Worked example: what an unreported parameter costs a reader

Suppose a reader knows the chain but not the parameter values, and guesses each
unreported parameter uniformly within $\pm 50\%$ of its plausible half-range. Then
$d_i \sim U(-0.5, 0.5)$, so the log-deviation $S = \sum_{i \in \text{free}} e_i d_i$
has variance $\sum e_i^2/12$ and standard deviation

$$\operatorname{SD}(S) = \sqrt{\frac{1}{12}\sum_{i \in \text{free}} e_i^{2}} .$$

For all six parameters free, $\sum e_i^{2} = 0.825$, so
$\operatorname{SD}(S) = 0.2622$. The $90\%$ interval for the reader's reproduction
is $100\exp(\pm 1.645 \times 0.2622)$, i.e.

$$y \in [65.0,\ 153.9],$$

against a published $y = 100.0$. The demonstration reports this interval for each
level of reporting:

| Parameters reported | $\operatorname{SD}(S)$ | $90\%$ interval | Measured success at $\pm 2\%$ |
|---|---|---|---|
| 0 of 6 | $0.2622$ | $[65.0, 153.9]$ | $5.6\%$ |
| 1 of 6 | $0.2475$ | $[66.6, 150.2]$ | $5.7\%$ |
| 2 of 6 | $0.2107$ | $[70.7, 141.4]$ | $6.4\%$ |
| 3 of 6 | $0.2026$ | $[71.7, 139.6]$ | $7.0\%$ |
| 4 of 6 | $0.1756$ | $[74.9, 133.5]$ | $6.9\%$ |
| 5 of 6 | $0.1732$ | $[75.2, 133.0]$ | $4.5\%$ |
| 6 of 6 | $0.0000$ | $[100.0, 100.0]$ | $100.0\%$ |

Reporting five of six parameters still leaves a factor of $1.33$ of doubt, and the
measured success rate at a $2\%$ tolerance stays near $6\%$ because a $2\%$
tolerance is far inside the inherited uncertainty. **Completeness is not a
gradual improvement; it is a change of regime.** This is the quantitative form of
the reviewer's sentence "I could not reproduce the result from the description".

**Reporting one parameter alone.** Ranked by elasticity:

| Parameter reported | $\operatorname{SD}(S)$ of the rest | $90\%$ interval |
|---|---|---|
| elevation correction | $0.1969$ | $[72.3, 138.2]$ |
| taper length | $0.2278$ | $[68.8, 145.5]$ |
| velocity step | $0.2420$ | $[67.2, 148.9]$ |
| high-cut corner | $0.2475$ | $[66.6, 150.2]$ |
| window length | $0.2558$ | $[65.7, 152.3]$ |
| damping factor | $0.2606$ | $[65.1, 153.5]$ |

Naming the elevation correction halves the log-deviation variance relative to
naming nothing ($0.1969^2/0.2622^2 = 0.56$); naming the damping factor removes
$1\%$ of it.

## 4. Writing the section as decisions

A reproducible Methods section is a list of **decisions**, and each decision has
four parts:

1. **What was chosen** — the parameter and its value, with units.
2. **Why that value** — the physical or empirical reason, in one clause.
3. **The range that would change the result** — the sensitivity, ideally measured.
4. **What it is not** — the alternative you rejected, when a reader would assume
   it.

The third part is the one almost always missing, and it is the part that
distinguishes "we used a 0.5 s taper" from "we used a 0.5 s taper; tapers from
0.3 s to 0.8 s change the recovered velocity by less than $1\%$, while a 0.1 s
taper produces a 4% artifact". The second sentence is what makes the paper
usable, because it tells the reader where the sensitivity is.

Equations belong in Methods when they define the operator, and in a Theory section
when they develop it. Either way, each symbol must be defined where it first
appears, and every symbol used later must be defined somewhere.

## Assumptions and regime of validity

1. **The chain is a surrogate.** Real processing has interacting and non-smooth
   parameter effects, thresholds and discrete choices that an exponential
   surrogate does not model; elasticities must be measured on the real chain.
2. **The guess distribution is a model of the reader.** $\pm 50\%$ of a plausible
   half-range is a chosen convention; a domain expert's guesses are narrower, so
   the reproduced uncertainty here is an upper bound for experts and a lower bound
   for novices.
3. **A $2\%$ tolerance is severe.** Many papers tolerate $10\%$; the tolerance is
   part of the specification and should be stated in the section itself.
4. **Elasticities are local.** They hold near the nominal values; a parameter
   whose effect is small at the nominal point can dominate at the edge of its
   range.
5. **Reporting everything is not the same as being reproducible.** Software
   versions, compiler flags and hardware can matter and are handled by archiving
   the environment, not by prose.

## The honest summary

Which parameter matters is a measurable question, and the answer is rarely the
one the author expected: the demonstration's influence ratio is $6.0$ between the
largest and smallest, and reporting five of six parameters leaves a factor of
$1.33$ of doubt. The honest Methods section reports the sensitivity of each
choice, states the tolerance at which it claims reproduction, and admits that
prose cannot guarantee bit-identical output.

## Python demonstration

[`code/writing_methods_demo.py`](./code/writing_methods_demo.py) prints four
labelled sections: the surrogate chain and its parameters with units; the
measured elasticity of each parameter; the $90\%$ interval and success rate for
each level of reporting completeness; and the interval obtained when only one
parameter is reported.

```bash
cd 24-research-papers-writing/02-scientific-writing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_methods_demo.py
```

## Exercises

Problems are in
[`exercises/03-writing-methods-exercises.md`](./exercises/03-writing-methods-exercises.md),
worked answers in
[`exercises/03-writing-methods-solutions.md`](./exercises/03-writing-methods-solutions.md).

## Mastery checkpoint

For the method you are currently writing up:

1. List every parameter you chose, with its value and unit.
2. Estimate or measure each one's elasticity by perturbing it by $10\%$ of a
   plausible half-range.
3. State the plausible range of each and compute the inherited interval for the
   published number if it were omitted.
4. Write the four-part sentence for the two most influential decisions.
5. State the tolerance at which you claim reproduction.

## Common pitfalls

1. **Chronological narration.** "We then tried…" reports your path, not the
   decision set; the reader needs the final set.
2. **Reporting everything, ranking nothing.** Word budgets are finite; spend them
   on influence.
3. **Naming a parameter without its range or sensitivity.** The value alone does
   not say whether it matters.
4. **Omitting units.** A number without a unit is not a parameter.
5. **Letting the software description stand in for the method.** "Processed with
   package X" is not a method; the choices inside the call are.
6. **Claiming reproducibility in prose.** Prose supports reproducibility within a
   stated tolerance; bit-identical output needs archived code and environment.

## Where this is used

- **Submission preparation:** the four-part sentence is the checklist for the
  Methods read-through.
- **Reviewing:** elasticity ordering tells a reviewer which missing parameter is
  fatal; see
  [24-03-05 Peer Review Practice](../03-research-methods-and-rigour/05-peer-review-practice.md).
- **Code and data release:** the archived environment closes the loop; see
  [24-06-01 Publishing Data and Code](../06-reproducible-publication/01-data-publication.md).
- **Lab and field handovers:** the same structure documents a protocol for the
  next person.
- **Teaching:** asking students for the elasticity of each choice is a fast way to
  teach that parameters are not equal.

## Related lessons

- [24-02-04 Writing Results and Discussion Without Overclaiming](04-writing-results-discussion.md) —
  what the numbers produced here are allowed to support.
- [24-03-04 Reproducible Research Practice End to End](../03-research-methods-and-rigour/04-reproducible-research-practice.md) —
  the workflow that makes the reported parameters checkable.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  the audit this section must satisfy.
- [22-02-02 Environment Pinning](../../22-data-engineering-reproducibility/02-reproducible-workflows/02-environment-pinning.md) —
  the parts of reproducibility that prose cannot carry.

## Self-assessment checklist

- [ ] I can define and compute an elasticity.
- [ ] I can rank parameters by influence and defend the ranking.
- [ ] I can compute the interval an unreported parameter set leaves a reader.
- [ ] I can explain why partial reporting does not rescue reproduction.
- [ ] I can write a four-part decision sentence with a measured sensitivity.
- [ ] I can state the tolerance at which I claim reproducibility.
