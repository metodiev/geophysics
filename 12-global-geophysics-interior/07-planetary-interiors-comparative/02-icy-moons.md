---
id: 12-07-02
title: "Icy Moons, Subsurface Oceans and Induction Studies"
level: research
prereqs: ["12-07-01", "08-04-01", "12-06-02"]
tags: [global-geophysics, earth-interior, planetary-interiors, electromagnetic-induction, subsurface-ocean, conductance]
---

# Icy Moons, Subsurface Oceans and Induction Studies

> All models and data in this module are **SYNTHETIC**. The body, its shell
> thickness, its conductivity and every "measured" response below are teaching
> values. No number is a measurement of any real moon. Externally quoted
> constants are $\mu_{0}$ and the definition of the skin depth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the skin depth $\delta = \sqrt{2/(\omega\mu_{0}\sigma)}$ for a
   given period and conductivity, and **state** when a layer is
   electromagnetically thin.
2. **Formulate** the degree-$n$ induction problem for a spherical conducting
   shell: the radial diffusion equation, the poloidal field representation and
   the boundary conditions.
3. **Verify** a numerical solution of that problem against an independent
   analytic (spherical-Bessel) solution and against two exact limits: the
   insulating limit ($|Q| = 0$, transparent) and the perfect-conductor limit
   ($|Q| \to n/(n+1)$, fully screened).
4. **Explain** why the measurement constrains the *conductance* $\sigma d$ rather
   than the conductivity and thickness separately, and **measure** the collapse.
5. **Invert** a synthetic single-frequency response into a conductance, report
   the admitted range, and **state** what the range depends on.
6. **Identify** the frequency band where a response is neither too small to
   measure nor saturated, and **explain** why saturation destroys the
   information rather than degrading it.
7. **State** the assumptions that connect a measured conductance to an ocean, and
   name the observation that would test each one.

## Prerequisites

- [12-07-01 Interiors of Mars, Venus, Mercury and the Moon](01-terrestrial-planets-interiors.md) —
  the comparative framing and the interior scaling arguments.
- [08-04-01 EM Induction Basics](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/01-em-induction-basics.md) —
  time-varying fields in conductors, the diffusion equation and the skin depth.
- [12-06-02 Love Numbers and Theoretical Tides](../06-geodesy-constraints-interior/02-tidal-love-numbers.md) —
  the other "response function" route to an internal layer, and the same
  pattern of resolving one combination rather than a profile.

## 1. What a magnetic measurement can see

A body without an internal dynamo still has a time-varying magnetic environment:
the ambient field of its parent body varies as the body orbits and rotates. If
the body contains a conducting layer, that layer responds with induced currents,
and the induced field is observable from outside. The measurement is therefore a
*response function*: an amplitude ratio and a phase lag between the driving field
and the induced field. The physics that matters is the one thing an ocean has and
ice does not: **electrical conductivity**.

Nothing in this lesson needs the ocean to be liquid. What the induction response
measures is a *conducting layer*; the inference "liquid water" imports additional
assumptions — that the conductivity comes from dissolved ions, and that a
conducting layer deep enough to matter cannot be anything else. The honest
chain is

$$
\text{amplitude and phase} \longrightarrow \text{conductance}\ \sigma d
\longrightarrow \text{a conductive layer} \longrightarrow \text{a candidate ocean}.
$$

Each arrow is a model step. This lesson measures what happens at the first arrow
and states the rest.

## 2. The induction problem

### 2.1 The equations

Write the poloidal magnetic field through a radial function $h(r)$:

$$
B_{r} = \frac{n(n+1)}{r^{2}}\,h(r)\,P_{n}(\cos\theta),
\qquad
B_{\theta} = \frac{h'(r)}{r}\,\frac{\partial P_{n}}{\partial\theta},
\qquad
B_{\varphi} = 0 .
$$

In a region of zero current the field is potential and $h$ satisfies

$$
h'' - \frac{n(n+1)}{r^{2}}h = 0
\qquad\Longrightarrow\qquad
h \propto r^{n+1}\ (\text{regular interior}),\quad h \propto r^{-n}\ (\text{exterior}),
$$

while in a conductor with conductivity $\sigma$ the quasi-static diffusion
equation is

$$
h'' - \frac{n(n+1)}{r^{2}}h = i\omega\mu_{0}\sigma\,h .
$$

### 2.2 Boundary conditions and the response

In the insulating regions it is convenient to use the magnetic potential
$V$ (with $\mathbf{B} = -\nabla V$). The exterior field is a superposition of the
driving and induced parts,

$$
V_{\text{ext}} = E\,r^{n} + Q\,\frac{a^{2n+1}}{r^{n+1}},
\qquad a = r_{2},
$$

and the interior field must be regular at the origin, $V_{\text{in}} = I\,r^{n}$.
Continuity of the radial and tangential field at both shell boundaries gives four
conditions, which for a linear problem determine the complex unknowns
$(I, Q)$ given $E = 1$. The **response** is $Q$: the ratio of the induced to the
driving potential coefficient. Its magnitude is the observable amplitude ratio
and its argument is the observable phase lag.

The boundary conditions can be stated in one line and should be checked in code:

$$
h \ \text{continuous},\qquad h' \ \text{continuous},
\qquad\text{at } r = r_{1} \ \text{and}\ r = r_{2}.
$$

### 2.3 Skin depth

The depth over which a diffusing field decays is

$$
\delta = \sqrt{\frac{2}{\omega\mu_{0}\sigma}},
$$

and the demonstration tabulates it:

```text
   period        sigma (S/m)   delta (km)   delta/shell for d = 5 km
    1.0e+04 s        1.00         50.3         10.066
    1.0e+05 s        0.10        503.3        100.658
    1.0e+06 s        0.01       5032.9       1006.584
```

At the periods of an orbiting body's environment, a plausible ocean conductivity
gives a skin depth of tens to thousands of kilometres — *far larger than any
plausible layer thickness*. The layer is electromagnetically **thin**, and the
field therefore sees only $\sigma d$. This single observation is the source of
the central non-uniqueness of the method.

## 3. Verification against three independent references

A numerical solution that has not been checked against something known is not a
result. The demonstration checks three things.

```text
   sigma (S/m)    delta (km)   |Q|      arg Q (deg)   |1+Q| interior
            0          inf    0.0000        180.00           1.0000
         0.01      1591.55    0.0007         89.92           1.0000
           1       159.15    0.0646         82.54           0.9915
          10        50.33    0.3954         37.37           0.6070
         100        15.92    0.4961          4.37           0.0761
        1e+04         1.59    0.4988          0.14           0.0003
  Check 1 (insulating limit): sigma = 0 gives |I| = 1.0000000000, |Q| = 1.51e-17
  Check 2 (perfect conductor): at sigma = 1e6 S/m, |Q| = 0.499881, |I| = 1.55e-17
  Check 3 (independent route): the analytic spherical-Bessel solution
   sigma (S/m)   |Q| RK4      |Q| Bessel     |I| RK4      |I| Bessel
          0.1     0.006514     0.006514     0.999914     0.999914
            1     0.064591     0.064591     0.991536     0.991537
           10     0.395388     0.395388     0.606956     0.606956
```

Read what each check establishes:

- **Check 1 (insulating limit).** With no conductor the shell is transparent:
  $|I| = 1$ exactly and $|Q| = 1.5\times10^{-17}$, i.e. numerical zero. This is
  the algebra of §2.2 reproduced by the solver.
- **Check 2 (perfect conductor).** A perfectly conducting shell expels the field
  from its interior, which requires $|Q| \to n/(n+1) = 0.5$ for $n = 1$ and
  $|I|\to0$. Both hold. Note that the ceiling $\tfrac12$ is **geometry**, not a
  property of the body: it is the price of screening a dipole.
- **Check 3 (independent route).** The same boundary-value problem solved with
  exact spherical modified Bessel functions (${i}_{n}$ and ${k}_{n}$) reproduces
  the RK4 values to six digits.

**A physical reading of the table.** At low conductivity the induced field is
small and in *phase quadrature* with the driver ($90^{\circ}$): it is the field
of a current proportional to the rate of change of the driver, exactly as an
inductor behaves. As conductivity rises the response grows, the phase falls, and
beyond $C = \sigma d \sim 10^{5}$ S the response flattens against the ceiling.
That is the entire phenomenology of the method, and every observable feature of
it is visible in one table.

## 4. The collapse: $\sigma$ and $d$ are not separately measurable

Four shells with the same conductance $C = \sigma d$ but very different
conductivity and thickness:

```text
   sigma (S/m)   d (km)   C (S)     |Q|      arg Q (deg)
            1       5.0     5000.0    0.0646         82.54
          0.5      10.0     5000.0    0.0640         82.58
          0.2      25.0     5000.0    0.0621         82.69
          0.1      50.0     5000.0    0.0591         82.87
```

Amplitude and phase agree to about ten percent across a factor 10 in thickness.
The small residual is the physical thickness entering the geometry; it is a
second-order effect at these parameters, and the honest statement is
*approximately* collapse rather than exact collapse. Within that approximation,

$$
\text{one complex response} \approx \text{one real number: the conductance } \sigma d .
$$

Separating $\sigma$ from $d$ requires either a second frequency far enough away
to break the thin-layer limit, or — much more powerful — an independent
constraint on what the layer can be made of.

## 5. Worked example: inverting a measured amplitude

Take a 5.0 km layer with $\sigma = 0.5$ S/m and a frequency corresponding to a
period of $10^{5}$ s. The model gives $|Q| = 0.0325$, and the sensitivity to the
conductance at that frequency is
$\mathrm{d}\ln|Q|/\mathrm{d}\ln C = 0.9957$ — nearly linear. Inverting with a
stated amplitude error:

```text
     period 1e+05 s (sensitive band): |Q| = 0.0325
        a 1% error in |Q| admits sigma from 0.4950 to 0.5050 S/m
        a 5% error in |Q| admits sigma from 0.4749 to 0.5251 S/m
```

The admitted range is symmetric about the truth, and the inversion is honest: the
relative error in $\sigma$ equals the relative error in $|Q|$ because the
response is linear in the conductance here. Note also what the *relative*
sensitivity table shows at the other end:

```text
   period (s)   C (S)     |Q|      dln|Q|/dlnC
    1.0e+03    2500.0    0.4918           0.0228
    1.0e+05    2500.0    0.0325           0.9957
    1.0e+07    2500.0    0.0003           1.0000
```

At long periods the relative sensitivity is *best* (1.00) but the response itself
is $3\times10^{-4}$: it cannot be measured. At short periods the response is
large (0.49) and almost blind to the conductance (0.02). **Neither extreme is
useful, for opposite reasons**, and choosing a mission's frequency band is
choosing a point in that trade-off.

## 6. Saturation, and why it destroys information

Inverting the same body from a *saturated* observation shows the asymmetry that
the amplitude alone conceals:

```text
     period 1e+03 s (saturated): |Q| = 0.4918
        a 1% error in |Q| admits sigma from 0.3636 to 1.3562 S/m
        a 5% error in |Q| admits sigma from 0.2087 to 100000.0000 S/m
```

A 5% amplitude error admits a conductivity range spanning nearly six orders of
magnitude, open-ended upwards. This is not a numerical artefact; it is the
geometry of the $\tfrac12$ ceiling. A measured $|Q|$ of 0.4918 is consistent with
a body whose true conductance is $10^{3}$ S or $10^{6}$ S, because both screen
almost completely. The information has not been degraded — it has been destroyed,
and the correct conclusion is that the observation constrains *a lower bound* on
the conductance, not a value.

The scan of §5 of the demonstration makes the window explicit:

```text
   conductance C (S)    |Q|        information about C
                100    0.0013   response too small to measure
               1000    0.0129   response too small to measure
              10000    0.1248   usable
             100000    0.4622   saturated against the 0.5 ceiling
            1000000    0.4947   saturated against the 0.5 ceiling
```

## 7. Assumptions and regime of validity

| Assumption | Where it enters | Failure mode |
|---|---|---|
| Spherically symmetric conductivity | §2 | A non-uniform ocean (a partial shell) changes the response by an amount comparable to the signal |
| Quasi-static (no displacement current) | §2 | Safe at these frequencies; $\omega\mu_{0}\sigma R^{2}\ll1$ |
| A single, spatially uniform shell | §§4–6 | A layered or depth-varying conductivity makes the response a *sum* of shells, and the inversion becomes a profile problem with its own null space |
| No internal dynamo | §1 | A dynamo field dominates the induced field and the response is not separable without modelling the dynamo |
| Induction only (no other current systems) | all | Ionospheric or plasma currents in the environment must be modelled or removed |
| The external driving field is known in amplitude and phase | all | The normalisation is usually the hardest observational step, and it is not a physics assumption but a data one |

Two of these deserve emphasis. First, the *driving field's normalisation* sets the
scale of the whole measurement: an error in the assumed amplitude propagates
directly into $\sigma$. Second, a **partial** (non-global) ocean is not a
small perturbation: its response is smaller and depends on the geometry of the
conducting region, so the inversion must state the assumed geometry, and the
result is conditional on it.

## 8. Python demonstration

[`code/icy_moons_demo.py`](code/icy_moons_demo.py):

1. skin depth and the induction parameter across periods and conductivities;
2. the shell response verified three ways (insulating limit, perfect-conductor
   limit, and an independent spherical-Bessel solution);
3. the conductance collapse across four shells of equal $\sigma d$;
4. the sensitivity spectrum and a synthetic inversion in the sensitive band;
5. saturation, the inversion from a saturated observation, and the resolvable
   window.

```bash
cd 12-global-geophysics-interior/07-planetary-interiors-comparative/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python icy_moons_demo.py
```

## 9. Exercises

[`exercises/02-icy-moons-exercises.md`](exercises/02-icy-moons-exercises.md) and
the worked
[`exercises/02-icy-moons-solutions.md`](exercises/02-icy-moons-solutions.md).

## Mastery checkpoint

Without notes:

> **(a)** Compute the skin depth in a layer of conductivity 0.05 S/m at a period
> of $5\times10^{4}$ s, and compare it with a 20 km layer. State whether the
> layer is electromagnetically thin.
> **(b)** Write the diffusion equation for degree $n = 1$ and state the two
> boundary conditions at each shell interface.
> **(c)** A response is measured with $|Q| = 0.30$ and a phase of $45^{\circ}$.
> Say whether the observation is in the sensitive band, and what a 3% amplitude
> error does to the admitted conductance.
> **(d)** Explain in three sentences why an observed conductance of $10^{4}$ S is
> consistent with both a 5 km layer at 2 S/m and a 50 km layer at 0.2 S/m, and
> name one measurement that would separate them.

A worked version of (a)–(c) appears in the lesson-02
[solutions](exercises/02-icy-moons-solutions.md).

## Common pitfalls

1. **Reporting a conductivity from a single-frequency amplitude.** The
   observable is a conductance; the conductivity requires thickness.
2. **Not checking the insulated and saturated limits.** They are exact and they
   catch sign, normalisation and boundary-condition errors.
3. **Treating a saturated measurement as a precise one.** Large amplitude means
   small sensitivity, not a good constraint.
4. **Forgetting that the ceiling $\tfrac12$ is geometry.** It is not a physical
   upper bound on the field, and it does not indicate a special body.
5. **Assuming a global ocean.** A partial shell gives a different response, and
   the difference is the signal in some geometries and a bias in others.
6. **Confusing conductance units.** $\sigma d$ in siemens; $\sigma$ in S/m;
   the distinction is a factor of the layer thickness.

## Related modules

- [08-04-06 Geomagnetic Depth Sounding](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/06-geomagnetic-depth-sounding.md) —
  the terrestrial version of the same inverse problem, where the target layers
  are the mantle and an ocean.
- [12-07-01 Interiors of Mars, Venus, Mercury and the Moon](01-terrestrial-planets-interiors.md) —
  what gravity and the figure can and cannot see about an interior, for
  comparison with what induction adds.
- [12-07-03 Giant Planet Interiors and Magnetic Fields](03-giant-planets.md) —
  the opposite regime: an internal dynamo whose field is generated rather than
  induced.
- [04-08-03 Planetary Geophysics from Orbiters and Landers](../../04-earth-science-geology/08-planetary-science/03-planetary-geophysics-missions.md) —
  how these measurements are actually acquired.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the general theory behind the collapse of §4.
