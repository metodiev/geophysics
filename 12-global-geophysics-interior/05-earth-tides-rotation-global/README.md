# Module 12-05 — Tides, Rotation and the Global Earth Response

**Stages:** doctoral → research · **Prerequisites:** modules
[07-06](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md) (Earth
tides and rotation) and [12-01](../01-seismic-structure-of-the-earth/README.md)
(the reference models a mode calculation needs); the normal-mode theory of
[02-03](../../02-physics/03-oscillations-and-waves/README.md) is assumed.

This module treats the Earth as a single physical body and asks what its global
response measures. Three responses are covered: the free oscillations, whose
discrete periods are weighted integrals of the interior structure; the tidal
response, whose phase lag is the only reason the Moon recedes; and the rotation,
whose millisecond length-of-day variations are an audit of every process that can
exchange angular momentum between the atmosphere, the oceans, the mantle and the
core. In each case the *derivation* is the point — a period, a lag and an LOD
change are all model outputs, and the lesson is what they are model outputs *of*.

The organising honesty of the module is that **every one of these observables is a
product of a measurement and a model.** A normal-mode period is a measurement; the
reference structure that reproduces it is a model. A tidal phase lag is a
measurement; the Love numbers that convert it into a quality factor are a model. A
length-of-day change is a measurement; the partition of that change between the
atmosphere, the oceans and the core is a model, and the coupling mechanism that
permitted the core's share is an estimate with an order-unity coefficient. The
lessons therefore derive each observable's forward model first, verify the
solver against an analytic limit, and only then interpret.

A second thread is the tension between **global averages and local mechanisms**.
A single whole-Earth quality factor can serve the tides, the free oscillations and
the surface waves only because the absorption band is broad — which the lessons
demonstrate by showing that a single relaxation time is wrong by four orders of
magnitude over the same frequency range. Similarly, the topographic coupling
capacity computed here exceeds the required torque by seven orders of magnitude,
which is not a proof that topographic coupling dominates but a demonstration that
capacity estimates cannot settle the question.

All models and data in this module are **SYNTHETIC**. The elastic structure, the
ephemeris inputs, the Love numbers, the moments of inertia, the conductivities,
the CMB topography and the wind series are adopted teaching inputs; no measured
mode period, tide, LOD value or coupling strength appears anywhere. Every number
quoted in a lesson is printed by the demonstration that lesson points to.

## Learning objectives

By the end of this module you will be able to:

1. **Formulate** the radial eigenproblem for a spherically symmetric elastic body
   and **derive** the transcendental eigenvalue equation of the homogeneous case.
2. **Build** and **verify** a finite-difference eigenproblem for a layered model,
   measuring its order of convergence against an analytic reference.
3. **Interpret** mode energy profiles as sensitivity kernels and **quantify** how
   a structural perturbation moves a period.
4. **Convert** a complex Love number's phase lag into a whole-Earth quality factor
   and **derive** the hysteresis relation $P = \omega E\tan\delta$.
5. **Compute** the M2 dissipation rate in terawatts and **convert** it into a
   tidal torque and an implied length-of-day trend.
6. **Demonstrate** why a single relaxation time cannot fit $Q$ across the tidal and
   seismic bands, and **compute** the absorption-band exponent required instead.
7. **Budget** axial angular momentum and **separate** an atmospheric contribution
   from the residual attributed to the core.
8. **Estimate** the electromagnetic and topographic coupling timescales,
   **verify** the topographic torque by quadrature, and **state** which
   mechanism the observations can discriminate.

## Prerequisites

- [07-06-01 Solid Earth Tides and Their Gravity Signature](../../07-gravity-geodesy/06-earth-tides-and-rotation/01-solid-earth-tides.md) —
  the tidal potential, the constituents and the gravity amplitude factor.
- [07-06-03 Earth Rotation, Polar Motion, LOD and Excitation](../../07-gravity-geodesy/06-earth-tides-and-rotation/03-earth-rotation.md) —
  the angular momentum budget and the excitation functions; lesson 03 builds on
  its results for the core-mantle coupling it leaves open.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../../02-physics/03-oscillations-and-waves/10-attenuation.md) —
  the meaning of $Q$.
- [12-04-03 Palaeomagnetic Record and Reversal Frequency](../04-geomagnetism-and-core/03-palaeomagnetic-record.md) —
  the field history that sets the electromagnetic coupling.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Free Oscillations of the Earth (Normal Modes)](01-free-oscillations.md) | research | A period is a weighted integral of structure, and $T \propto R/\alpha$ unless something breaks the degeneracy |
| 02 | [Tidal Response and the Quality Factor of the Whole Earth](02-tidal-response.md) | doctoral | A phase lag of $0.57°$ is a $Q$ of 100; one relaxation time is wrong by four orders of magnitude |
| 03 | [Rotation Variations, LOD and Core-Mantle Coupling](03-rotation-and-length-of-day.md) | research | An LOD change proves an internal torque exists, never which mechanism supplied it |

## Suggested path

**If you are new to global geophysics:** lesson 01 in full, then 02 §1–4, then 03
§1–3. Each demonstration prints the tables the lesson discusses, so run them as
you read.

**If you already know tides and rotation:** start at 01 §4 (the verification
strategy), read 02 §2 and §5 (the hysteresis identity and the absorption band),
and finish with 03 §3–6 (the coupling estimates and the conservation check).

**If you are preparing a research project:** 01 §5–7 (kernels, scaling and what
is omitted), 02 §5–7 (absorption bands and what a tide-derived $Q$ is not), and
03 §4–7 (capacities versus requirements, and the discrimination problem), plus the
★★★ exercises of all three lessons.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-free-oscillations.md`](01-free-oscillations.md) | Lesson 01 — radial eigenproblem, layered solver, kernels, scaling |
| [`02-tidal-response.md`](02-tidal-response.md) | Lesson 02 — complex Love numbers, dissipation, $Q$, absorption band |
| [`03-rotation-and-length-of-day.md`](03-rotation-and-length-of-day.md) | Lesson 03 — the LOD budget, coupling mechanisms, inner core |
| [`code/free_oscillations_demo.py`](code/free_oscillations_demo.py) | Lesson 01 demonstration |
| [`code/tidal_response_demo.py`](code/tidal_response_demo.py) | Lesson 02 demonstration |
| [`code/rotation_and_length_of_day_demo.py`](code/rotation_and_length_of_day_demo.py) | Lesson 03 demonstration |
| [`exercises/01-free-oscillations-exercises.md`](exercises/01-free-oscillations-exercises.md) | Lesson 01 problems |
| [`exercises/01-free-oscillations-solutions.md`](exercises/01-free-oscillations-solutions.md) | Lesson 01 worked solutions |
| [`exercises/02-tidal-response-exercises.md`](exercises/02-tidal-response-exercises.md) | Lesson 02 problems |
| [`exercises/02-tidal-response-solutions.md`](exercises/02-tidal-response-solutions.md) | Lesson 02 worked solutions |
| [`exercises/03-rotation-and-length-of-day-exercises.md`](exercises/03-rotation-and-length-of-day-exercises.md) | Lesson 03 problems |
| [`exercises/03-rotation-and-length-of-day-solutions.md`](exercises/03-rotation-and-length-of-day-solutions.md) | Lesson 03 worked solutions |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 12-global-geophysics-interior/05-earth-tides-rotation-global/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python free_oscillations_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_response_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rotation_and_length_of_day_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. The
free-oscillation demonstration takes about ten seconds because it solves several
hundred dense eigenproblems; the other two take under a second.

## Mastery checkpoint

Complete this without notes:

> A synthetic homogeneous sphere has $R = 6371$ km, $\alpha = 8.0\
> \mathrm{km\,s^{-1}}$, $\beta = 4.5\ \mathrm{km\,s^{-1}}$. **(a)** Write the
> radial equation of motion and its two boundary conditions, and derive the
> transcendental eigenvalue equation. **(b)** Compute the fundamental period and
> predict what happens to it if $\alpha$ is increased by 5%. **(c)** For an
> adopted tide of stored energy $7.6\times10^{16}$ J and frequency
> $1.4\times10^{-4}\ \mathrm{rad\,s^{-1}}$, compute the dissipation rate at
> $Q = 100$. **(d)** Compute the angular momentum change corresponding to a 1-ms
> length-of-day change with $C = 8.04\times10^{37}\ \mathrm{kg\,m^{2}}$.
> **(e)** Compute the topographic coupling capacity of a 1-km, $m = 2$ CMB
> topography and state what the comparison with (d) does and does not prove.

A worked version of (a)–(b) appears in the
[solutions to lesson 01](exercises/01-free-oscillations-solutions.md) and of
(c)–(d) in the [solutions to lesson 03](exercises/03-rotation-and-length-of-day-solutions.md).

## Common pitfalls across this module

1. **Quoting a period, a $Q$ or an LOD trend without its model.** All three are
   products of a measurement and a model.
2. **Testing a discretisation against itself.** The analytic homogeneous case
   exists in the demonstration for exactly this reason.
3. **Forgetting the degeneracy $T \propto R/\alpha$.** One period cannot separate
   size from speed.
4. **Using a real Love number with its imaginary part omitted**, which removes the
   entire dissipation.
5. **Fitting $Q$ with a single relaxation time** and then applying it four decades
   away in frequency.
6. **Treating an LOD change as an energy statement.** It is angular momentum, and
   it is conserved in any internal exchange.
7. **Equating a coupling capacity with a coupling mechanism.** The topographic
   capacity computed here is seven orders of magnitude larger than required, and
   that settles nothing.

## Related modules

- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the reference models that supply the structure a mode calculation needs.
- [12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md) —
  the energy budget into which tidal and core dissipation enter.
- [12-04 Geomagnetic Field and Core Dynamics](../04-geomagnetism-and-core/README.md) —
  the field strength and history that set the electromagnetic coupling.
- [12-06 Geodetic Constraints on the Interior](../06-geodesy-constraints-interior/README.md) —
  the moment of inertia, figure and nutation constraints used throughout.
- [07-06 Earth Tides and Rotation](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md) —
  the tidal potential, the constituents, the rotation budget and the wobble.
- [02-03 Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md) —
  normal modes, damping and the quality factor.
