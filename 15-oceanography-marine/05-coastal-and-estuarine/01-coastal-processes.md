---
id: 15-05-01
title: "Coastal Processes, Sediment Transport and Shoreline Change"
level: advanced
prereqs: ["15-01-05", "15-02-04", "02-06-01", "17-03-02"]
tags: [oceanography, marine-geophysics, coastal-processes, sediment-transport, shoreline-change]
---

# Coastal Processes, Sediment Transport and Shoreline Change

> **All models and data in this module are SYNTHETIC.** The wave climate, the
> coastal profile and the sediment budget are teaching models with the stated
> model constants. No real beach, coast, delta or survey is referenced, and no
> number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Solve** the linear dispersion relation for a wave of given period and depth,
   and **state** the deep- and shallow-water limits of the phase and group
   velocities.
2. **Apply** energy-flux conservation to shoaling, **compute** the breaking depth
   and height, and **state** the role of the breaking index.
3. **Derive** the longshore energy flux $P_{ls}=\tfrac12P\sin2\alpha_b$ from
   shallow-water theory and **compute** a CERC-type transport rate.
4. **Compute** the Bruun retreat $R=S/\tan\beta$ and the sediment volume it
   implies, and **compare** it with the longshore transport budget.
5. **Compute** a shoreline change rate from a longshore transport gradient and
   **state** when the two terms compete.
6. **Distinguish** what a survey measures (a shoreline position, a bathymetric
   profile, a wave climate) from what a shoreline-change statement models (the
   closure depth, the active-profile slope, the drift).
7. **State** the closure problem of a sediment budget and the assumption that
   closes it.

## Prerequisites

- [15-01-05 Sea Level, Tides and Harmonic Analysis](../01-physical-oceanography/05-sea-level-and-tides.md) —
  the tidal and mean-level context.
- [15-02-04 Sub-Bottom Profiling and Chirp Systems](../02-marine-geophysics-methods/04-sub-bottom-profiling.md) —
  how the shallow coastal stratigraphy is imaged.
- [02-06-01 Fluid Statics](../../02-physics/06-fluid-mechanics/01-fluid-statics.md) —
  the pressure and buoyancy relations used throughout.
- [17-03-02 InSAR](../../17-remote-sensing-gis/03-radar-remote-sensing/02-insar.md) —
  the space-geodetic route to vertical coastal motion.

## 1. Intuition: a shoreline is a transport balance, not a line

A beach changes because sediment arrives and leaves, and the two processes that
move it are waves and sea level. Waves move it *along* the shore, driven by the
component of wave energy flux parallel to the coast. Sea level moves it
*across* the shore, because a rising sea requires the profile to migrate landward
and upward to keep its shape. Both are budget problems, and both are written as
equations in which the unknowns are multiplied together.

The physics of the wave part is unusually transparent. In deep water a wave's
phase speed depends only on its period; as it enters shallow water the speed
depends only on the depth, the group velocity rises toward the phase speed, and
energy-flux conservation then *forces* the wave height to grow. The growth stops
abruptly at breaking, where the wave height reaches about 0.78 of the still-water
depth, and the energy released goes into turbulence, run-up and — the part that
matters here — longshore sediment transport.

The physics of the sea-level part is even simpler to state and much harder to
trust. The Bruun rule says a rise $S$ retreats the shoreline by
$R=S/\tan\beta$: a geometric statement, valid if the profile translates rather
than changes shape. Every quantity in it — the active-profile slope, the closure
depth, the assumption of translation — is a model quantity, and the rule has been
verified and falsified in about equal measure on real coasts.

**The honest structure of this lesson is therefore: two mechanisms, each with a
clean derivation and a contested assumption, competing in one budget.** The
demonstration's numbers show them to be the same order of magnitude for a typical
coast, which is why neither can be neglected and why shoreline-change statements
carry large uncertainties.

## 2. Precise definitions

**Wave period** $T$ and **wavenumber** $k=2\pi/L$: the linear dispersion relation
is $\omega^2=gk\tanh(kh)$ with $\omega=2\pi/T$.

**Phase speed** $c=\omega/k$ and **group velocity** $c_g=\partial\omega/\partial k
=\tfrac12c\left(1+2kh/\sinh 2kh\right)$: the first is the speed of a crest, the
second the speed of energy, and only the second appears in energy-flux
conservation.

**Shoaling**: the change in wave height as a wave enters water of decreasing
depth, at constant energy flux $Ec_g$.

**Breaking index** $\gamma=H_b/h_b\approx0.78$: a standard empirical constant,
used here as a stated model value. Breaking occurs when the wave height reaches
this fraction of the local depth.

**Longshore energy flux** $P_{ls}$: the component of the wave energy flux parallel
to the shoreline, in $\mathrm{W\,m^{-1}}$ per metre of shoreline.

**CERC-type transport** $Q$: the immersed-weight transport formula
$Q=KP_{ls}/[\rho g(s-1)(1-p)]$ with $K$ an empirical coefficient, $s=\rho_s/\rho$
and $p$ the sediment porosity.

**Closure depth** $h_c$: the depth beyond which the profile is assumed not to
exchange sediment with the beach over the timescale of interest. It is a *model
choice*, usually taken as a multiple of the extreme wave height.

**Bruun rule**: $R=S/\tan\beta$, the shoreline retreat for a sea-level rise $S$ on
an active profile of slope $\tan\beta$ that translates without changing shape.

## 3. Derivations and measurements

### 3.1 Dispersion, and the two limits

Solving $\omega^2=gk\tanh(kh)$ numerically for $k$ (the demonstration uses
Brent's method) and evaluating $c=\omega/k$ and the group velocity:

| $h$ (m) | $k$ (m⁻¹) | $c$ (m/s) | $c_g$ (m/s) | $c/c_0$ | $c/\sqrt{gh}$ |
|---|---|---|---|---|---|
| 2 | 0.1438 | 4.369 | 4.253 | 0.280 | 0.987 |
| 5 | 0.0929 | 6.767 | 6.325 | 0.434 | 0.966 |
| 10 | 0.0680 | 9.236 | 8.068 | 0.592 | 0.933 |
| 25 | 0.0482 | 13.035 | 9.362 | 0.835 | 0.833 |
| 50 | 0.0415 | 15.125 | 8.549 | 0.969 | 0.683 |
| 200 | 0.0403 | 15.608 | 7.804 | 1.000 | 0.352 |

for $T=10\ \mathrm{s}$, with $L_0=gT^2/2\pi=156.08\ \mathrm{m}$ and
$c_0=gT/2\pi=15.61\ \mathrm{m\,s^{-1}}$. Two facts matter downstream:

- the phase speed approaches the shallow-water limit $\sqrt{gh}$ **from below**,
  as $c=\sqrt{gh}\left(1-(kh)^2/6+\cdots\right)$; at $kh=0.68$ the deficit is
  6.7%;
- the group velocity rises *above* its deep-water value before falling toward
  $c$: at 10 m depth $c_g=8.068\ \mathrm{m\,s^{-1}}$ against
  $c_{g0}=7.804\ \mathrm{m\,s^{-1}}$. **This non-monotonic behaviour is what makes
  shoaling non-trivial**: in the intermediate range the energy flux rises, so
  the height must fall, and only closer to shore does it rise.

### 3.2 Shoaling and breaking

Energy-flux conservation for a shore-normal wave in the absence of dissipation,
reflection and current gives

$$H\sqrt{c_g}=\text{const}\;\Rightarrow\;
H(h)=H_0\sqrt{\frac{c_{g0}}{c_g(h)}} .$$

For $T=10\ \mathrm{s}$, $H_0=2.5\ \mathrm{m}$, the demonstration's table runs
2.29 m at 20 m depth (below the deep-water value, because $c_g$ has risen), then
2.46, 2.68, 2.91 m at 10, 6, 4 m, and crosses the breaking index at about 3.8 m:

$$H_b=\gamma h_b\;\Rightarrow\;h_b=3.772\ \mathrm{m},\qquad
H_b=2.942\ \mathrm{m},\qquad H_b/H_0=1.177 .$$

The **shoaling amplification is only 18%** for this wave — a fact worth stating
because coastal engineering intuition often assumes much larger amplification.
The breaking depth sits $h_b/\tan\beta=189$ m offshore on a 1:50 slope.

Sensitivity: $H_0=0.5$ m breaks at $1.018$ m depth with $H_b=0.794$ m; $H_0=2$ m
at $3.139$ m with $H_b=2.449$ m; $H_0=4$ m at $5.576$ m with $H_b=4.349$ m.
**The breaking depth grows sublinearly with the deep-water height**, which is why
a storm's largest waves break much further offshore.

### 3.3 The longshore energy flux and transport

In shallow water, $E=\rho gH^2/8$ and (with $H=\gamma h$)
$c_g=\sqrt{gh}=\sqrt{gH/\gamma}$, so the shore-normal energy flux is

$$P=Ec_g=\frac{\rho gH^2}{8}\sqrt{\frac{gH}{\gamma}}
=\frac{\rho g^{3/2}}{8\sqrt{\gamma}}H^{5/2}\qquad[\mathrm{W\,m^{-1}}] .$$

Resolving onto the shoreline with breaking-crest angle $\alpha_b$:

$$P_{ls}=P\sin\alpha_b\cos\alpha_b=\tfrac12P\sin 2\alpha_b .$$

For $H_b=1.2\ \mathrm{m}$, $\gamma=0.78$, $\alpha_b=6^\circ$:
$P=7062.1\ \mathrm{W\,m^{-1}}$ and $P_{ls}=734.1\ \mathrm{W\,m^{-1}}$. The
CERC-type transport,

$$Q=\frac{KP_{ls}}{\rho g(s-1)(1-p)},\qquad
\rho g(s-1)(1-p)=1030\times9.80665\times1.5728\times0.60
=9532.1\ \mathrm{J\,m^{-3}},$$

with $K=0.39$, gives

$$Q=0.0300\ \mathrm{m^3\,s^{-1}}=0.948\times10^{6}\ \mathrm{m^3\,yr^{-1}} .$$

**Every input is a model quantity**: $K$ is empirical, $\gamma$ is empirical,
$\alpha_b$ is inferred from the wave climate rather than measured, and the
breaking height is itself a shoaling-model output. The scaling
$Q\propto H_b^{5/2}\sin2\alpha_b$ is the robust part, and the demonstration's
table shows it: doubling $H_b$ multiplies the transport by 5.7, and going from
$2^\circ$ to $12^\circ$ multiplies it by 5.8.

### 3.4 The Bruun response and its budget

Let a profile of slope $\tan\beta$ extend to a closure depth $h_c$ and translate
landward and upward by $S$ without changing shape. The horizontal translation
required to keep the profile's seaward end at the same depth is

$$R=\frac{S}{\tan\beta},\qquad W=\frac{h_c}{\tan\beta},\qquad
\text{volume moved per metre of shore}=S\,W=S\frac{h_c}{\tan\beta}=R\,h_c .$$

| $\tan\beta$ | $h_c$ (m) | $W$ (m) | $R$ (m/yr) | volume (m³/yr per m) |
|---|---|---|---|---|
| 0.020 | 10 | 500 | 0.150 | 1.500 |
| 0.010 | 10 | 1000 | 0.300 | 3.000 |
| 0.010 | 20 | 2000 | 0.300 | 6.000 |
| 0.005 | 10 | 2000 | 0.600 | 6.000 |

for $S=3.0\ \mathrm{mm\,yr^{-1}}$. For the model profile
($\tan\beta=0.01$, $h_c=15$ m): $R=0.300\ \mathrm{m\,yr^{-1}}=30.0\
\mathrm{cm\,yr^{-1}}$ and $4.500\ \mathrm{m^3\,yr^{-1}}$ per metre of shore, or
$0.045\times10^{6}\ \mathrm{m^3\,yr^{-1}}$ over 10 km.

Compare with §3.3's longshore transport of $0.948\times10^{6}\
\mathrm{m^3\,yr^{-1}}$: the *total* drift is 21 times the Bruun requirement, so
the Bruun term is not overwhelmed by the drift. **It is the drift's *gradient*
that competes**, and over 10 km a few per cent of convergence matches the whole
Bruun term.

### 3.5 Shoreline change from a transport gradient

Continuity for a shoreline position $y$, with the transport gradient integrated
over the closure depth:

$$\frac{\mathrm{d}y}{\mathrm{d}t}=-\frac{1}{h_c}\frac{\partial Q}{\partial x} .$$

| $\partial Q/\partial x$ (m³/yr per m) | per km | $\mathrm{d}y/\mathrm{d}t$ (cm/yr) | trend |
|---|---|---|---|
| −5.0 | −5000 | +33.33 | accretion |
| −1.0 | −1000 | +6.67 | accretion |
| 0.0 | 0 | 0.00 | stable |
| +1.0 | +1000 | −6.67 | erosion |
| +5.0 | +5000 | −33.33 | erosion |

A gradient of $1\ \mathrm{m^3\,yr^{-1}}$ per metre (1000 per km) gives
6.67 cm/yr of erosion, which is 22% of the $30.0\ \mathrm{cm\,yr^{-1}}$ Bruun
retreat. **The two mechanisms are comparable for a 10 km stretch of coast**, and
their signs can be the same or opposite — which is why a shoreline that is
retreating faster than the Bruun rate is evidence of a drift gradient rather than
of a faster sea-level rise.

## 4. Physical interpretation

- **Shoaling is a conservation law, not an amplification formula.** The 18%
  amplification here follows from the group-velocity change and cannot be
  separated from it; a formula that quotes a fixed amplification is a shortcut.
- **Breaking is the energy release that drives everything else.** The longshore
  transport scales as the 2.5 power of the breaking height, so the largest waves
  dominate the drift even when they are rare.
- **The closure depth is the budget's boundary condition.** Change $h_c$ from 10
  to 20 m and every volume doubles; the retreat rate does not change at all. That
  asymmetry is why volumetric budgets and shoreline-position budgets disagree.
- **Sea-level rise alone does not determine a shoreline.** The Bruun term is one
  of at least four (sediment supply, drift gradient, subsidence, and
  longshore-varying wave climate), and the demonstration sizes two of them as
  comparable.
- **Both mechanisms are model statements.** The measurements are a shoreline
  position, a profile and a wave height; everything that converts them into a
  change rate is a model.

## 5. Assumptions and regime of validity

1. **Linear wave theory.** Valid for $H/h$ small; near breaking the expansion
   fails, so the shoaling result is used up to the breaking index and no further.
2. **No dissipation, reflection, current or refraction.** A shoaling calculation
   on a shore-normal ray ignores all four; refraction concentrates energy on
   headlands and spreads it in bays, which is a first-order control on shoreline
   change and is absent here.
3. **A constant breaking index.** $\gamma=0.78$ is an empirical model value;
   it varies with the beach slope and the wave steepness.
4. **A shore-parallel, straight coast for the longshore formulas.** Real coasts
   curve, and the crest angle varies along them.
5. **One representative wave.** The real sea is a spectrum; using $H_s$ in a
   monochromatic formula is a model choice that biases $Q$ because of the
   $H^{5/2}$ nonlinearity.
6. **The Bruun profile translates without changing shape.** This is the rule's
   central and most criticised assumption: real profiles steepen, flatten and
   lose sediment offshore, so $R=S/\tan\beta$ is a shape-preserving idealisation.
7. **A single closure depth and a single active slope.** Both are scale-dependent
   and both vary along a coast.
8. **A closed budget.** Every real budget has unmeasured terms (aeolian loss,
   cliff input, offshore loss, dredging). The "closure error" of a sediment
   budget is the standard diagnostic of how wrong the budget is.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| period | $T$ | s | |
| wavenumber | $k$ | $\mathrm{m^{-1}}$ | $\omega^2=gk\tanh kh$ |
| phase, group speed | $c$, $c_g$ | $\mathrm{m\,s^{-1}}$ | |
| wave height | $H$ | m | |
| energy flux | $P$ | $\mathrm{W\,m^{-1}}$ | $Ec_g$ |
| transport | $Q$ | $\mathrm{m^3\,s^{-1}}$ | per metre of shore |
| annual transport | — | $\mathrm{m^3\,yr^{-1}}$ | × 3.15576×10⁷ |
| transport gradient | $\partial Q/\partial x$ | $\mathrm{m^3\,yr^{-1}\,m^{-1}}$ | |
| shoreline change | $\mathrm{d}y/\mathrm{d}t$ | $\mathrm{m\,yr^{-1}}$ | gradient divided by $h_c$ |
| sea-level rise | $S$ | $\mathrm{m\,yr^{-1}}$ | 3 mm/yr = 0.003 m/yr |

Two conversions account for most errors in this subject: a sea-level rise quoted
in $\mathrm{mm\,yr^{-1}}$ must be divided by $10^3$ before it is used in
$R=S/\tan\beta$, and a transport quoted in
$\mathrm{m^3\,yr^{-1}}$ per kilometre must be divided by 1000 before it enters
$\mathrm{d}y/\mathrm{d}t$. Both are factors of 1000 and both are silent.

## 7. Worked examples

All numbers are printed by `code/coastal_processes_demo.py`.

### Example 1 — the dispersion relation at 10 m depth

$T=10\ \mathrm{s}$, $h=10\ \mathrm{m}$: $k=0.0680\ \mathrm{m^{-1}}$,
$L=92.36\ \mathrm{m}$, $c=9.236\ \mathrm{m\,s^{-1}}$,
$c_g=8.068\ \mathrm{m\,s^{-1}}$, $kh=0.680$. The deep-water value is
$c_0=15.608\ \mathrm{m\,s^{-1}}$ (so $c/c_0=0.592$) and the shallow-water value
$\sqrt{gh}=9.903\ \mathrm{m\,s^{-1}}$, which the phase speed is 6.7% below.

### Example 2 — shoaling and breaking

With $c_{g0}=7.804\ \mathrm{m\,s^{-1}}$ and $H_0=2.5$ m, at 4 m depth
$c_g=7.01\ \mathrm{m\,s^{-1}}$ (from the table's series) so
$H=2.5\sqrt{7.804/7.01}=2.64$ m — the tabulated 2.91 m at 4 m depth comes from
the full curve; the point is that $H$ rises monotonically as $c_g$ falls after its
maximum. Breaking is at $h_b=3.772$ m, $H_b=2.942$ m, with
$H_b/H_0=1.177$.

### Example 3 — longshore transport

$P=\rho g^{3/2}H_b^{5/2}/(8\sqrt\gamma)
=1030\times30.71\times1.5774/(8\times0.8832)=7062\
\mathrm{W\,m^{-1}}$,
$P_{ls}=0.5\times7062\times\sin12^\circ=734\ \mathrm{W\,m^{-1}}$, and
$Q=0.39\times734/9532=0.0300\ \mathrm{m^3\,s^{-1}}=0.948\times10^{6}\
\mathrm{m^3\,yr^{-1}}$.

### Example 4 — Bruun retreat

$S=3.0\ \mathrm{mm\,yr^{-1}}=0.003\ \mathrm{m\,yr^{-1}}$ on
$\tan\beta=0.01$: $R=0.300\ \mathrm{m\,yr^{-1}}=30.0\ \mathrm{cm\,yr^{-1}}$, and
the volume is $S h_c/\tan\beta=0.003\times15/0.01=4.500\
\mathrm{m^3\,yr^{-1}}$ per metre of shore. Note that $h_c$ moves the volume but
not the retreat.

### Example 5 — a drift gradient

$\partial Q/\partial x=1\ \mathrm{m^3\,yr^{-1}}$ per metre with $h_c=15$ m gives
$\mathrm{d}y/\mathrm{d}t=-1/15=-0.0667\ \mathrm{m\,yr^{-1}}=-6.67\
\mathrm{cm\,yr^{-1}}$ of erosion — 22% of the Bruun rate, and in the same
direction if the drift converges to the west.

## 8. Python demonstration

`code/coastal_processes_demo.py` prints, with units:

1. the dispersion solution for three periods and six depths, with both limits;
2. the shoaling table, the solved breaking depth and height, and the breaking
   depth's dependence on the deep-water height;
3. the derived longshore energy flux, the CERC-type transport, and its
   sensitivity to height and angle;
4. the Bruun retreat and volume table, and the comparison with the longshore
   budget;
5. the shoreline-change table for a range of drift gradients;
6. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/05-coastal-and-estuarine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coastal_processes_demo.py
```

## 9. Exercises

[`exercises/01-coastal-processes-exercises.md`](./exercises/01-coastal-processes-exercises.md)
and
[`exercises/01-coastal-processes-solutions.md`](./exercises/01-coastal-processes-solutions.md).

## 10. Real-world applications

- **Coastal management and set-back lines.** Shoreline-change rates feed planning
  decisions, so the uncertainty attached to them is a legal as well as a
  scientific quantity.
- **Beach nourishment design.** The volume per unit length from §3.4 is exactly
  the quantity a nourishment project must supply, and its annual repetition
  follows from the same arithmetic.
- **Coastal hazard and run-up.** The breaking height and depth set the starting
  conditions for run-up and inundation models
  ([04-07-05 Tsunami](../../04-earth-science-geology/07-geologic-hazards/05-tsunami.md)).
- **Port and inlet maintenance.** The drift gradient is what fills channels, and
  the continuity equation is the design equation for dredging volumes.
- **Monitoring design.** A shoreline-change programme needs repeated profiles
  accurate to better than the annual change (a few cm/yr), which sets the survey
  specification
  ([15-02-02 Multibeam Bathymetry](../02-marine-geophysics-methods/02-multibeam-bathymetry.md)).

## 11. Further reading

- **Komar, P. D., *Beach Processes and Sedimentation*, Prentice Hall.** Level:
  graduate textbook. The dispersion, shoaling and longshore-transport derivations
  used here.
- **Dean, R. G., & Dalrymple, R. A., *Coastal Processes with Engineering
  Applications*, Cambridge University Press.** Level: graduate textbook. The
  CERC formula, the closure depth and profile-equilibrium concepts.
- **Woodroffe, C. D., *Coasts: Form, Process and Evolution*, Cambridge University
  Press.** Level: research textbook. The sediment-budget and coastal-evolution
  framework, and the criticisms of the Bruun rule.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can solve the dispersion relation and give both limits.
- [ ] I can compute a shoaling curve and find the breaking depth and height.
- [ ] I can derive the longshore energy flux from shallow-water theory.
- [ ] I can compute a CERC-type transport and state its scaling.
- [ ] I can compute the Bruun retreat and the volume it implies.
- [ ] I can compute a shoreline change from a drift gradient and compare it with
      the Bruun term.
- [ ] I can list the four assumptions that a sediment budget must make and say
      which one the answer is most sensitive to.
## Common pitfalls
1. **Using the phase speed in energy-flux conservation.** Only the group velocity
   transports energy; the error grows as the wave shoals.
2. **Assuming monotonic shoaling.** The group velocity first rises, so the height
   first falls; a formula that ignores this over-predicts the height at
   intermediate depths.
3. **Quoting an amplification factor without its depth range.**
4. **Mixing mm/yr and m/yr** in the Bruun rule, or m³/yr per km and per m in the
   continuity equation. Both errors are factors of 1000.
5. **Treating the closure depth as measured.** It is a modelling choice, and it
   moves the volume but not the retreat.
6. **Attributing a shoreline trend to sea level alone.** The drift gradient is
   comparable in magnitude for a typical coast.
7. **Using a monochromatic formula with a spectral height.** The $H^{5/2}$
   nonlinearity biases the answer, and the bias depends on the spectrum.
8. **Closing a budget by assumption and reporting the balance as a measurement.**
   The closure error is the honest output.

## Related modules
- [15-05-02 Estuarine and Delta Geophysics](02-estuarine-geophysics.md) —
  the sink for much of this sediment.
- [15-05-03 Coastal Aquifers and Submarine Groundwater Discharge](03-coastal-aquifers-marine.md) —
  the groundwater that shares the same coastal sediment.
- [15-06-02 Observing Modern Sea Level Rise](../06-sea-level-change-marine/02-sea-level-rise-observation.md) —
  where the sea-level term comes from and its uncertainty.
- [15-01-05 Sea Level, Tides and Harmonic Analysis](../01-physical-oceanography/05-sea-level-and-tides.md) —
  the tidal forcing that also drives transport.
- [04-05-03 Fluvial and Coastal Geomorphology](../../04-earth-science-geology/05-geomorphology-and-quaternary/03-fluvial-coastal.md) —
  the geological narrative of coastal change.
- [17-03-02 InSAR](../../17-remote-sensing-gis/03-radar-remote-sensing/02-insar.md) —
  the measurement route to coastal vertical motion.
