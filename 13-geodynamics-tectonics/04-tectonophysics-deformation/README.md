# Module 13-04 — Tectonophysics and Deformation

**Stages:** graduate → research · **Prerequisites:** module 13-03 or an
equivalent quantitative background; basic elasticity and inverse theory.

**All models and data in this module are SYNTHETIC.** Every velocity, slip,
viscosity, friction coefficient and coupling distribution is a chosen teaching
value, and every number quoted in a lesson is printed by the demonstration that
accompanies it. No real GNSS site, earthquake, catalogue or published coupling
or viscosity estimate is used or reproduced. The models here are 2-D
anti-plane analogues of real 3-D problems, and each lesson states exactly what
that costs.

The module follows one deformation episode through its whole cycle. A velocity
field measured by GNSS is inverted for a strain-rate tensor
([01](01-crustal-deformation-gps.md)); the loading it implies is expressed as a
Coulomb stress change on faults of any orientation
([02](02-fault-mechanics.md)); the stress released by an earthquake relaxes
viscoelastically over decades ([03](03-postseismic-viscoelastic.md)); and the
deficit that remains locked before the next event is inverted for as a coupling
distribution ([04](04-interseismic-coupling.md)). The thread that connects the
four lessons is the same question the parent folder asks: **what does each
measurement constrain, and what does it leave free?**

The answers are specific and quantitative. Strain rate is determined by network
*aperture*, not by station count, and the error scales as $1/L$. A Coulomb
stress change cannot be quoted without the receiver mechanism, because the same
stress change promotes one fault orientation and inhibits its conjugate. A
postseismic decay constant is only determined if the observation window spans a
few times the constant, and a layered viscosity has no single decay constant at
all. Coupling depth and coupling value trade off so strongly that a land network
starting tens of kilometres inland cannot resolve the locking depth, no matter
how many stations it has.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the velocity-gradient tensor from GNSS velocities and decompose it
   into strain rate and rotation, reporting the frame dependence of each.
2. **Measure** how network aperture controls the strain-rate uncertainty and
   **predict** the $1/L$ scaling before designing a network.
3. **Derive** the optimal fault orientation from the Coulomb criterion and
   **compute** Anderson's dips from the friction coefficient.
4. **Compute** the exact 2-D anti-plane stress change from slip on a strike-slip
   fault and **resolve** it onto receiver faults of arbitrary strike.
5. **Distinguish** the promoted from the shadowed regions around a slipped
   fault, and **state** what a positive Coulomb stress change does and does not
   predict.
6. **Derive** the Maxwell relaxation time and **fit** postseismic transients,
   reporting the parameter correlations and the window dependence.
7. **Compare** the afterslip logarithm with the viscoelastic exponential and
   **state** the physical discriminants that actually work.
8. **Invert** interseismic velocities for a coupling distribution, **interpret**
   the resolution matrix, and **convert** coupling to a moment deficit.

## Prerequisites

- [13-03 Quantitative Plate Tectonics](../03-plate-tectonics-quantitative/README.md) —
  the kinematic framework and the isostasy the deformation rests on.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  stress, strain, constitutive laws, failure and friction.
- [04-04 Structural Geology](../../04-earth-science-geology/04-structural-geology/README.md) —
  faults, stress states and the geological description of deformation.
- [07-04 Geodesy Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md) —
  where the velocities come from.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Crustal Deformation from GNSS and Strain Rates](01-crustal-deformation-gps.md) | graduate | The deformation is absolute, the rotation is frame-dependent; error scales as $1/\text{aperture}$ |
| 02 | [Fault Mechanics, Coulomb Stress and Stress Transfer](02-fault-mechanics.md) | research | $\Delta\mathrm{CFS}$ is meaningless without the receiver mechanism; the 2-D model has no normal-stress term |
| 03 | [Postseismic Relaxation and Viscoelastic Models](03-postseismic-viscoelastic.md) | research | $\tau = \eta/\mu_e$ is only measurable if the window spans a few $\tau$ — and a layered Earth has no single $\tau$ |
| 04 | [Interseismic Coupling and Megathrust Locking](04-interseismic-coupling.md) | research | Coupling value and coupling depth trade off; only the depth extent integral is well determined |

## Suggested path

**If you are new to tectonic geodesy:** lessons 01 → 02 → 04, then 03. Running
each demonstration and checking the printed numbers against your own arithmetic
is the intended route; every lesson's key number is reproducible by hand.

**If you know GNSS processing:** start at 01 §4 (aperture), then 04 §2–3 — the
depth–coupling trade-off is the practical limit on every published coupling
model.

**If you are preparing a research project:** 02 §4 and §6, 03 §3 and §5, and the
★★★ exercises throughout. Those sections are where the module states most
plainly what its models cannot do.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-crustal-deformation-gps.md`](01-crustal-deformation-gps.md) | Lesson 01 |
| [`02-fault-mechanics.md`](02-fault-mechanics.md) | Lesson 02 |
| [`03-postseismic-viscoelastic.md`](03-postseismic-viscoelastic.md) | Lesson 03 |
| [`04-interseismic-coupling.md`](04-interseismic-coupling.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and SymPy:

```bash
cd 13-geodynamics-tectonics/04-tectonophysics-deformation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python crustal_deformation_gps_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fault_mechanics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python postseismic_viscoelastic_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python interseismic_coupling_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC network of 20 sites spans $40\ \mathrm{km}$ with
> $0.5\ \mathrm{mm\,yr^{-1}}$ velocity noise. **(a)** Estimate the strain-rate
> uncertainty using the measured rule
> $\delta e_1 \approx 386/L$ (in $10^{-9}\ \mathrm{yr^{-1}}\,\mathrm{km}$ at
> $0.5\ \mathrm{mm\,yr^{-1}}$ noise) and state whether it is adequate for a
> $30\times10^{-9}\ \mathrm{yr^{-1}}$ signal. **(b)** The region is cut by a fault
> striking $18.4^\circ$ from a fault that has just slipped; state how the Coulomb
> stress change on this fault compares with that on a parallel fault, and which
> orientation would be most inhibited. **(c)** A postseismic transient is fitted
> with $\tau = 6 \pm 3\ \mathrm{yr}$ from $5\ \mathrm{yr}$ of data; compute the
> implied viscosity with its uncertainty and state why the error bar is
> optimistic. **(d)** The same region is modelled for coupling on 10 patches; five
> are recovered near 1.0 and five near 0.3, with a resolution diagonal of $0.2$
> for the deepest. State what may and may not be claimed.

## Common pitfalls across this module

1. **Quoting a rotation rate without its frame.** Strain rate is
   frame-invariant; the rotation is not.
2. **Estimating a strain rate from a small network.** A $20\ \mathrm{km}$ network
   gave an $e_1$ error of $19.3\times10^{-9}\ \mathrm{yr^{-1}}$ on a
   $35\times10^{-9}\ \mathrm{yr^{-1}}$ signal.
3. **Quoting $\Delta\mathrm{CFS}$ without the receiver mechanism.** The same
   stress change is $+1.31$ and $-1.31\ \mathrm{MPa}$ $90^\circ$ apart.
4. **Trusting a good residual.** The wrong compaction model, the wrong
   receiver mechanism and a misidentified postseismic process all fit well.
5. **Fitting a decay constant from too short a window.** A $1.5\ \mathrm{yr}$
   window on a $10.6\ \mathrm{yr}$ transient returned $15.4\ \mathrm{yr}$.
6. **Reading per-patch coupling as if each were resolved.** Only the coupled
   depth extent is well determined; the deep patches are smeared.
7. **Treating a moment deficit as a forecast.** It is the moment that would be
   released if the whole coupled zone failed at once.

## Related modules

- [13-03 Quantitative Plate Tectonics](../03-plate-tectonics-quantitative/README.md) —
  the kinematic and isostatic framework.
- [13-01 Geodynamic Principles](../01-geodynamic-principles/README.md) —
  rheology and lithospheric strength, which set every parameter used here.
- [13-06 Crustal and Lithospheric Dynamics](../06-crustal-and-lithospheric-dynamics/README.md) —
  volcano geodesy (lesson 02 there) is the transient case of the modelling done
  here.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  what to do with a moment deficit.
- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md) —
  the applied side of Coulomb stress transfer.
- [18-inverse-problems](../../18-inverse-problems/README.md) — non-uniqueness,
  resolution and regularisation, treated systematically.
