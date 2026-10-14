# Module 06-12 — Induced and Triggered Seismicity

**Stages:** graduate → research · **Prerequisites:** modules 06-03 and 06-04;
elasticity up to failure and friction.

This module is about earthquakes that humans may have caused, and it is built
around the one thing that makes the subject hard rather than the one thing that
makes it interesting. The interesting part is the physics: pore-pressure
diffusion, poroelastic stress transfer, rate-and-state friction. All of it is
derivable, and this module derives it. The hard part is that the question people
actually ask — *was this earthquake induced, and by whom?* — is an attribution
question, and the observations available to answer it are also produced by
perfectly natural processes.

Every lesson therefore separates three statements that are routinely blurred:
what the physics predicts (a model output), what the catalogue measures (a
statistic), and what a protocol decides (a policy). The demonstration for the
first lesson shows that the *sign* of a Coulomb stress change is a property of the
source–receiver pair, not of the source, and flips for a quarter of cases at
$55^\circ$ of receiver-plane uncertainty. The demonstration for the last lesson
shows that a natural swarm placed at the well, at reservoir depth and inside the
operations window is statistically indistinguishable from an induced sequence
using every statistic except the temporal tracking — and that in a basin with
tens of operations windows, a time coincidence is *expected*. The intermediate
lessons quantify the degeneracies that make a diffusivity or an Omori $p$-value
conditional on choices the data do not constrain.

All models and data in this module are **SYNTHETIC**. No real field, well,
catalogue or project is measured, and no published number is quoted. The four
named settings in lesson 05 (Basel, Oklahoma, Groningen, Pohang) are used as
*argument archetypes* — types of evidence and types of uncertainty — and the
lesson states explicitly that it makes no factual claims about those projects.

## Learning objectives

By the end of this module you will be able to:

1. Write the Coulomb failure function with a stated sign convention, derive the
   pressure-only result $\Delta CFS = \mu_f\Delta p$, and compute the Biot
   coefficient from the elastic moduli.
2. Compute the static stress change of a point double couple, verify its $1/r^3$
   decay and its symmetry, and state the geometric conditions under which a
   Coulomb sign flip occurs.
3. Derive the pressure field of a constant-rate source, measure the $t^{1/2}$
   triggering front, and state why a front constrains only the product $Dx_c$.
4. Distinguish the reduction of a random location error with catalogue size from
   the irreducible bias of a systematic velocity error.
5. Derive the Dieterich seismicity response from rate-and-state friction and
   explain why Omori's $p = 1$ is a limit rather than a law.
6. Fit Omori-Utsu parameters to a synthetic catalogue, report their trade-off, and
   state the window and completeness conditions that a quoted $(c, p)$ requires.
7. Compute traffic-light exceedance probabilities and the distribution of the
   largest event, and explain why no protocol can bound the maximum magnitude.
8. Evaluate the four standard attribution statistics against an *adversarial*
   natural population, and price the coincidence probability of a time test.

## Prerequisites

- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) — moment
  tensors and the static field of a double couple.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  hypocentre uncertainty and magnitude scales, both of which enter every statistic
  below.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  constitutive laws, and
  [08 Failure and Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)
  for the friction laws used in lesson 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Causes of Induced Seismicity: Injection, Extraction, Reservoirs](01-induced-seismicity-causes.md) | doctoral | The sign of $\Delta CFS$ is a property of the source–receiver pair, not of the source |
| 02 | [Pore-Pressure Diffusion and Triggering Mechanisms](02-pore-pressure-triggering.md) | doctoral | A front measures the product $Dx_c$ and therefore nothing about $D$ alone |
| 03 | [Rate-and-State Friction and the Dieterich Seismicity Model](03-rate-state-triggering.md) | research | $p \approx 1$ is a limit of a transient, not a law; $(c,p)$ needs its window |
| 04 | [Traffic-Light Protocols, Monitoring and Mitigation](04-monitoring-and-mitigation.md) | graduate | A threshold is a policy output; the maximum magnitude is unbounded by any accepted model |
| 05 | [Documented Case Studies: Basel, Oklahoma, Groningen, Pohang](05-case-studies-induced.md) | graduate | Against an adversarial natural population, only temporal tracking discriminates |

## Suggested path

**If you are new to the subject:** lessons 01 and 02 in order, running each
demonstration. Lesson 02 is the one that fixes the scale of the physics: how far
a pressure front travels in a year, and why that number is the whole argument.

**If you are working on a screening study:** lesson 01 §3.3–3.4 and lesson 05.
The pair of questions you need — "which receiver plane, and how well constrained?"
and "how often does coincidence happen anyway?" — are answered there.

**If you are preparing a research project:** lesson 02 §3.4–3.5 (the $D$–$x_c$
degeneracy), lesson 03 §3.2–3.3 (the Omori limit and its window dependence), and
the ★★★ exercises in every companion.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-induced-seismicity-causes.md`](01-induced-seismicity-causes.md) | Lesson 01 |
| [`02-pore-pressure-triggering.md`](02-pore-pressure-triggering.md) | Lesson 02 |
| [`03-rate-state-triggering.md`](03-rate-state-triggering.md) | Lesson 03 |
| [`04-monitoring-and-mitigation.md`](04-monitoring-and-mitigation.md) | Lesson 04 |
| [`05-case-studies-induced.md`](05-case-studies-induced.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/12-induced-and-triggered-seismicity/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coulomb_sign_flip_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python diffusion_front_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rate_state_omori_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python traffic_light_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python natural_vs_induced_demo.py
```

Every demonstration prints labelled section headers and every result **with
units**, uses a fixed random seed (`np.random.default_rng(20261014)`), requires no
network access, and exits 0.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC operation injects for 16 months. The triggering front reaches
> $r_c = 3.888\ \mathrm{km}$ after one year (take
> $1\ \mathrm{yr} = 3.1553\times10^{7}\ \mathrm{s}$). **(a)** Compute the migration
> rate $a = r_c^2/t$ with its unit, and the diffusivity you would infer for an
> assumed threshold ratio giving $x_c = 1.1977$. **(b)** State what happens to that
> inferred diffusivity, with a factor, if the true threshold ratio were ten times
> larger. **(c)** A natural swarm is sited at the well, at reservoir depth and
> inside the window. State which single statistic still separates it from the
> induced population in this module's models, and why the separation is fragile.
> **(d)** Compute the probability that a randomly timed natural swarm in a 20-year
> catalogue falls inside a 16-month window.

A worked version of (a)–(b) appears in the lesson-02
[solutions](exercises/02-pore-pressure-triggering-solutions.md), and of (d) in the
lesson-05 [solutions](exercises/05-case-studies-induced-solutions.md).

## Common pitfalls across this module

1. **Reporting a Coulomb stress change without the receiver plane.** Half of all
   orientations have $\Delta CFS > 0$ at every friction coefficient, and a
   quarter flip at $\pm55^\circ$ of receiver-plane uncertainty.
2. **Quoting a diffusivity from a front.** The front gives $Dx_c$; the
   demonstration's inferred $D$ spans a factor of 267 across plausible thresholds.
3. **Chasing catalogue size to fix a velocity-model bias.** Systematic distance
   error scales $D$ by $(1+b)^2$ and never shrinks with more events.
4. **Quoting $(c,p)$ without the window.** The same catalogue gives $p = 0.9967$
   over 30 days and $p = 0.4186$ over 365 days.
5. **Treating a traffic-light threshold as a physical limit.** It is the output of
   a cost model, and a tenfold change in one cost can remove the rationale for a
   threshold entirely.
6. **Testing a coincidence without counting the windows.** With 30 windows in a
   basin the probability of at least one natural coincidence is $0.874$.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the elastic moduli and Green's functions used for the static stress field.
- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) — moment
  tensors, source spectra and the physics of rupture, of which this module uses
  only the static part.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  Gutenberg-Richter, declustering and the limits of prediction, which this module
  applies to a different question.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the flow and transport physics behind the diffusivity.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the systematic
  treatment of degeneracy, regularisation and resolution that lessons 02 and 03
  meet in concrete form.
