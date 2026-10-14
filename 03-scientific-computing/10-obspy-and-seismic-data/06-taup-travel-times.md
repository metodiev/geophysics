---
id: 03-10-06
title: "Travel Times with TauP and Phase Naming"
level: intermediate
prereqs: ["03-10-04"]
tags: [obspy, taup, travel-times, ray-parameter, shadow-zone]
---

# Travel Times with TauP and Phase Naming

Everything in observational seismology that connects a time to a place goes
through a travel-time calculation. ObsPy bundles the TauP implementation of
the tau–p method together with the standard Earth models, so the calculation
runs offline in milliseconds. This lesson uses it to do four things: name a
phase correctly, measure the ray parameter and verify it is
$\mathrm{d}T/\mathrm{d}\Delta$, find the shadow zone, and understand what a
travel time does *not* tell you.

Run the demonstration before reading on; every value below is its output.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/taup_travel_times_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** a standard Earth model as a table of layers and **state** the depths
   of the Moho, the core–mantle boundary and the inner-core boundary.
2. **Name** a phase correctly from the sequence of ray-path symbols, and
   interpret `P`, `S`, `c`, `K`, `I`, `diff`, `PKIKP`, `SKS` and `PcP`.
3. **Measure** the ray parameter by numerical differentiation of $T(\Delta)$ and
   **verify** the slowness identity $p = \mathrm{d}T/\mathrm{d}\Delta$.
4. **Locate** the P-wave shadow zone by measurement and explain its cause.
5. **Explain** the difference between take-off and incidence angles, and why the
   ray parameter is constant along a ray.
6. **Quantify** the effect of source depth on the travel time and compare it
   with the effect of distance.

## Prerequisites

- [03-10-04 Event Catalogs, QuakeML and Phase Metadata](./04-catalog-and-events.md)
  — the origin and the arrival that a travel time belongs to.

## 1. Intuition: a ray is a name for a path

A phase name is a compressed description of a ray's journey. Each capital
letter is a leg, and the sequence of letters *is* the path:

| Symbol | Meaning |
|---|---|
| `P` | compressional wave in the mantle |
| `S` | shear wave in the mantle |
| `K` | compressional wave in the outer core |
| `I` | compressional wave in the inner core |
| `J` | shear wave in the inner core |
| `c` | reflection off the core–mantle boundary ("core") |
| `i` | reflection off the inner-core boundary |
| `diff` | diffraction along the core–mantle boundary |
| `m`, `g`, `n` | reflections off the Moho, a discontinuity, the surface |

So `PKIKP` is: compressional in the mantle, compressional in the outer core,
compressional in the inner core, back into the outer core, back into the
mantle. `SKS` is shear to the core, compressional through it, shear out — and
the fact that a shear leg exists on both sides is *evidence that the outer core
is liquid*, because an S wave cannot cross it.

## 2. Precise definitions

### 2.1 The model

`TauPyModel(model="iasp91")` loads a precomputed tau–p table. The model's
properties, measured:

```
model radius                  : 6371.0 km
moho depth                    : 35.0 km
core-mantle boundary depth    : 2889.0 km
inner-core boundary depth     : 5153.9 km
number of constant-velocity layers: 129
```

and its velocity structure at selected depths:

| depth (km) | $v_p$ (km/s) | $v_s$ (km/s) | $\rho$ (g/cm³) |
|---|---|---|---|
| 10 | 5.800 | 3.360 | 2.720 |
| 30 | 6.500 | 3.750 | 2.920 |
| 100 | 8.048 | 4.493 | 3.359 |
| 700 | 10.896 | 6.054 | 4.395 |
| 2890 | 8.011 | **0.000** | 9.916 |
| 4000 | 9.544 | **0.000** | 11.316 |
| 5200 | 11.102 | 3.448 | 12.727 |
| 6000 | 11.227 | 3.553 | 12.983 |

The S velocity is exactly zero from 2890 km to 5153.9 km. That is the outer
core, and it is the physical statement behind `SKS`.

### 2.2 Travel time, ray parameter, slowness

For a spherically symmetric Earth, the ray parameter is

$$p = r\frac{\sin i}{v(r)} = \text{constant along a ray},$$

with $r$ the radius from the centre, $i$ the angle between the ray and the
local vertical, and $v$ the local wave speed. The quantity $p$ has units of
s/rad. When travel times are tabulated against epicentral distance in
**degrees**, the natural unit is s/deg, and the two are related by

$$p_{\text{s/deg}} = p_{\text{s/rad}} \times \frac{\pi}{180}.$$

The fundamental identity is

$$p = \frac{\mathrm{d}T}{\mathrm{d}\Delta},$$

which the demonstration verifies numerically by central differences with a
0.01° step:

| $\Delta$ (deg) | $T$ (s) | $p$ from TauP (s/deg) | $\mathrm{d}T/\mathrm{d}\Delta$ measured | difference |
|---|---|---|---|---|
| 30.0 | 368.7345 | 8.844432 | 8.844561 | $1.29\times10^{-4}$ |
| 45.0 | 495.4003 | 7.958787 | 7.958438 | $-3.50\times10^{-4}$ |
| 60.0 | 606.6711 | 6.873217 | 6.873424 | $2.07\times10^{-4}$ |
| 75.0 | 701.5984 | 5.778215 | 5.777793 | $-4.22\times10^{-4}$ |

Agreement at the level of the finite-difference truncation error
($\sim10^{-4}$ s/deg for a 0.01° step and a curve of curvature
$\sim0.01$ s/deg²). **This is the single best check on a travel-time table,
because it tests the derivative, not the value.**

### 2.3 Take-off and incidence angle

- **Take-off angle** is measured at the source, from straight down, in degrees.
- **Incidence angle** is measured at the receiver, from vertical, in degrees.

They differ because the ray is refracted at every interface and, for a
shallow source, travels a long way before arriving steeply at the surface. The
measurement shows it:

| depth (km) | $T$ at 60° (s) | take-off (deg) | incidence (deg) |
|---|---|---|---|
| 0 | 608.2804 | 21.0168 | 21.0168 |
| 50 | 601.3345 | 30.0108 | 20.9715 |
| 300 | 575.4041 | 33.4003 | 20.6469 |
| 600 | 549.8792 | 40.9761 | 20.1555 |

At zero depth the two coincide to four decimals (21.0168 for both), because the
source sits on the surface and the ray leaves and arrives through the same
surface. As the source deepens, the take-off angle grows from 21° to 41° while
the incidence angle stays within 21 ± 1°. The ray parameter is constant along
each ray; the *angles* are not.

## 3. Derivations and worked reasoning

### 3.1 Why $p = \mathrm{d}T/\mathrm{d}\Delta$: a one-line derivation

Consider two receivers separated by a small angular distance
$\delta\Delta$. The extra path length is the projection of the ray's end
direction onto the direction of increasing distance, which is
$p\,\delta\Delta$ by the definition of the slowness vector. Hence
$\delta T = p\,\delta\Delta$, and in the limit $p = \mathrm{d}T/\mathrm{d}\Delta$.
The derivation is geometric and needs no model; the measurement in the table
above *is* the verification.

### 3.2 Distance, and the effect of source depth

Measured travel times at 10 km source depth (iasp91):

| $\Delta$ (deg) | P (s) | S (s) | PcP (s) | S − P (s) | $v_{\text{app}}$ from $\Delta/ T_P$ (km/s) |
|---|---|---|---|---|---|
| 10.0 | 143.6906 | 257.1100 | 514.3235 | 113.4194 | 7.7385 |
| 20.0 | 272.6760 | 498.4842 | 528.3054 | 225.8082 | 8.1558 |
| 30.0 | 368.7345 | 667.6449 | 550.5120 | 298.9104 | 9.0468 |
| 45.0 | 495.4003 | 894.7249 | 596.2380 | 399.3246 | 10.1005 |
| 60.0 | 606.6711 | 1099.9899 | 652.5180 | 493.3188 | 10.9972 |
| 80.0 | 729.5531 | 1334.2175 | 736.7498 | 604.6644 | 12.1932 |
| 95.0 | 802.6818 | 1477.2641 | 802.8771 | 674.5822 | 13.1603 |

The apparent velocity $\Delta_{\text{km}}/T_P$ is not a material velocity: it
rises from 7.74 km/s to 13.16 km/s because a deeper ray spends more of its path
in faster mantle. Anyone who reads "apparent velocity" as "the speed of P" will
conclude that the mantle accelerates with distance, which it does not.

The effect of source depth, at fixed 60°:

| depth (km) | $T_P$ (s) | $\mathrm{d}T/\mathrm{d}z$ (s/km) |
|---|---|---|
| 0 | 608.2804 | — |
| 10 | 606.6711 | −0.16093 |
| 50 | 601.3345 | −0.13342 |
| 100 | 595.9579 | −0.10753 |
| 300 | 575.4041 | −0.10277 |
| 600 | 549.8792 | −0.08508 |

Moving the source 600 km deeper reduces the P travel time by 58.4 s, i.e.
0.085 s/km. Moving the receiver 1° further at 60° changes it by 6.87 s
(the ray parameter). So **one degree of epicentral distance is worth about
80 km of source depth** in travel time. That ratio is why a location problem
needs depth to be constrained by something other than travel times alone.

### 3.3 The shadow zone, measured

The demonstration scans distance and lists the first reported phase:

| $\Delta$ (deg) | number of P arrivals | first reported phase |
|---|---|---|
| 95 | 1 | P |
| 100 | 1 | P |
| 103 | 0 | Pdiff |
| 110 | 0 | Pdiff |
| 120 | 0 | Pdiff |
| 130 | 0 | Pdiff |
| 140 | 0 | PKIKP |
| 143 | 0 | PKIKP |
| 145 | 0 | PKIKP |
| 150 | 0 | PKIKP |

Beyond 103° there is no direct P arrival: the core–mantle boundary refracts the
ray too steeply for it to reach the surface between 103° and 143°. This is the
**shadow zone**, discovered in 1914 and used by Oldham and Gutenberg to argue
for a liquid outer core. The arrivals present in the shadow are the diffracted
`Pdiff` (energy bent along the core–mantle boundary) and the core phase
`PKIKP`, both of which are one to two orders of magnitude weaker than P. A
catalog that lists "P" at 120° is listing `Pdiff` under a convenient name.

### 3.4 Multiple branches at short distance

At 20° the demonstration returns *six* separate P arrivals:

```
at 20.0 deg : P 272.676 s, P 274.399 s, P 274.619 s, P 278.030 s, P 278.358 s, S 498.484 s, ...
```

They are different ray paths with the same phase name — the upper-mantle
triplication, where the 410 km and 660 km discontinuities create two extra
branches. Their splitting is 5.7 s across the set. Reporting "the P arrival"
without an index is ambiguous, and in a location code it is a source of
systematic error.

## 3b. Worked examples

### 3b.1 From S−P time to distance, and why that is not a location

**Problem.** A station records a local event with $S - P = 12.5$ s. Find the
distance, and state the uncertainty.

For a local event in a uniform crust with $v_p = 6.0$ and $v_s = 3.46$ km/s
($v_p/v_s = 1.73$), the S−P time is

$$S - P = \frac{d}{v_s} - \frac{d}{v_p}
= d\left(\frac{1}{3.46} - \frac{1}{6.0}\right)
= d(0.28902 - 0.16667) = 0.12235\,d .$$

So $d = 12.5/0.12235 = 102.2$ km. Two qualifications follow immediately:

- **The relation is model-dependent.** With $v_p/v_s = 1.75$ instead of 1.73,
  the coefficient changes to $0.12299$ and the distance to $101.6$ km — a 0.6 km
  difference from a 1 % change in the velocity ratio, which is smaller than the
  typical uncertainty in $v_p/v_s$.
- **The uncertainty is dominated by the pick, not the arithmetic.** A pick
  uncertainty of ±0.1 s on each phase gives ±0.2 s on S−P, i.e. ±1.6 km. A wrong
  origin depth is worse: for a surface-focus assumption when the event is at
  10 km, the S−P relation changes by several per cent, i.e. several kilometres.

And even with a perfect distance, the hypocentre is on a **circle of radius
102 km** around the station. Three stations give a location; one gives a
distance, and quoting it as a location is the most common error in a
single-station study.

### 3b.2 Phase identification when two phases arrive together

**Problem.** At 20° a P arrival is observed, but the travel-time table predicts
six P arrivals spanning 5.7 s. Which one was picked, and does it matter?

The six arrivals are different ray paths: direct, and branches refracted by the
410 km and 660 km discontinuities. Their differences at 20° are
272.68, 274.40, 274.62, 278.03, 278.36 and (at longer time) a sixth — a spread of
5.7 s, i.e. 0.6 km of apparent distance at 10 km/s.

Does it matter? **Yes, if the inversions are compared.** A location routine that
picks the first arrival and compares it against a table computed for a later
branch acquires a residual that varies with distance — a systematic bias that
looks like a velocity-model error and is actually a phase-identification error.
The test is to plot residuals against distance: a branch mismatch produces a
piecewise-linear trend with breakpoints where the branches swap dominance.

The practical methods: (a) cross-correlate the observed waveform against
synthetics for each branch and pick the branch with the highest coefficient;
(b) restrict the distance range to where a single branch dominates
(15–25° is not in that range for P); or (c) invert for the branch assignment as
part of the location, which is what modern automated systems do by computing
synthetics for all candidates.

### 3b.3 The shadow zone as a discrimination tool

**Problem.** A catalog lists a `P` arrival at 118°. Is the entry plausible?

From the measured shadow-zone scan, at 118° there are **no direct P arrivals** in
iasp91 for any depth in the range tested: the first reported phase is `Pdiff`,
and beyond about 143° it is `PKIKP`. So the entry is not a direct P.

Three explanations, in order of likelihood:

1. **The pick is `Pdiff`** and the catalog recorded a generic `P`. The travel
   time is 1–2 s later than the direct P extrapolation, which biases the distance
   by 0.2–0.3°.
2. **The distance is wrong.** A depth-phase misidentification or a miscomputed
   epicentral distance could put the event inside the ordered range, where the
   arrival really is P.
3. **The model is wrong for that path.** A fast slab along the ray path can
   advance a P arrival into the shadow zone, and that is exactly the effect
   tomographers measure.

Distinguishing them requires the waveform: `Pdiff` has a distinctly lower
frequency content than `P` (diffraction low-passes the signal) and its amplitude
is one to two orders of magnitude smaller. **A shadow-zone arrival is therefore a
check on the pick, not only on the Earth.**

### 3b.4 What a three-second model difference means for an inversion

**Problem.** Two studies invert the same arrival times using iasp91 and ak135,
which differ by up to 0.9 s at 90° for P (measured). One reports a 1 % fast
anomaly, the other 0.5 %. Which is right?

Neither — they are answers to different questions. A travel-time residual is
measured relative to a reference model, so an inversion reports the *perturbation
with respect to that model*. A 0.9 s model difference, converted at
$p = 4.64$ s/deg at 90°, is 0.19° or 21 km of path length — comparable to the
anomalies being mapped.

The practical rules:

- **Compare anomalies, not absolute velocities.** If both studies report their
  perturbations relative to their own reference, the difference between them is
  partly the difference between the references.
- **State the reference model explicitly**, in the abstract if the anomaly is the
  result.
- **Check the residual distribution.** A model mismatch produces a systematic
  offset in the mean residual; a wrong reference produces an offset that is a
  smooth function of distance. Plotting the mean residual against distance
  reveals which.

The 0.9 s spread is not an error in either study. It is a reminder that "the P
travel time at 90°" is not a datum; "the P travel time at 90° in iasp91" is.

## 4. Physical and computational interpretation

What a travel time does **not** tell you:

- **It does not give an amplitude.** TauP computes times and paths; source
  radiation, geometric spreading and attenuation are separate physics.
- **It is model-dependent.** Comparing `iasp91`, `prem` and `ak135` at 60°
  gives differences of 1–3 s, which is a larger effect than most arrival-time
  residuals.
- **It is exact only for the model, not for the Earth.** Real Earth structure
  perturbs travel times by several seconds at teleseismic distances, and that
  perturbation is the signal in tomography.

The ray parameter is the bridge between the two: it is what a slowness
measurement from an array gives you directly, and it is what the model predicts
for free. Comparing the two is how a model is tested against data.

## 5. Python demonstration

[`code/taup_travel_times_demo.py`](./code/taup_travel_times_demo.py) prints the
model structure, travel-time tables, the numerical verification of
$p = \mathrm{d}T/\mathrm{d}\Delta$, the shadow-zone scan, take-off versus
incidence angles, a single-station distance inversion from an S−P time, and a
three-model comparison. It needs no network: TauP's models are bundled.

## 6. Exercises

Full solutions:
[`exercises/06-taup-travel-times-solutions.md`](./exercises/06-taup-travel-times-solutions.md).

### ★ Foundational

**★1.** Name the depth of the Moho, the core–mantle boundary and the
inner-core boundary in iasp91.

**★2.** Expand `PKIKP`, `SKS`, `PcP` and `Pdiff` into their legs and state which
leg in each demonstrates that the outer core is liquid.

**★3.** State the units of the ray parameter in s/rad and in s/deg, and give the
conversion factor between them.

**★4.** At 60° the ray parameter is 6.873217 s/deg. By how much does the P
travel time change if the distance increases by 0.5°?

### ★★ Applied

**★★5.** Verify the measured difference between `dT/dΔ` and TauP's
`ray_param_sec_degree` at 45°: recompute the central difference with a 0.01°
step from the printed travel times and state the truncation error you expect.

**★★6.** From the depth table, compute the depth change equivalent to a 1°
change in epicentral distance at 60°, and state the practical implication for
hypocentre location.

**★★7.** An S−P time of 900.0 s is measured at an unknown distance. Using the
demo's inversion (which searches 20–100° in 0.05° steps), state how well the
distance is determined and why a single station cannot locate the event.

**★★8.** State the number of direct P arrivals at 20° and explain them in terms
of the upper-mantle discontinuities. Then state why a location code that picks
"the first arrival" is not obviously wrong.

### ★★★ Research-oriented

**★★★9.** Compare `iasp91`, `prem` and `ak135` at 60° and 90° for P and S.
Report the differences in seconds, and convert them to an equivalent distance
error using the local ray parameter. State whether the model choice matters
more for location or for tomography.

**★★★10.** The shadow zone boundary is a property of the model and of the
source depth. Scan source depths from 0 to 600 km and report the distance at
which direct P disappears and at which it returns. Explain the trend in terms
of the ray's turning depth near the core–mantle boundary.
