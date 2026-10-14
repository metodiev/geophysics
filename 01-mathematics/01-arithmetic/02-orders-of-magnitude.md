---
id: 01-01-02
title: "Orders of Magnitude and Fermi Estimation in Earth Science"
level: beginner
prereqs: ["01-01-01"]
estimated_minutes: 75
tags: [estimation, scaling, fermi, feasibility]
---

# Orders of Magnitude and Fermi Estimation in Earth Science

## Learning objectives

By the end of this lesson you will be able to:

1. **Estimate** any geophysical quantity to within one order of magnitude using
   only reasoning about scales and a handful of memorised anchors.
2. **Use** a rough estimate to detect arithmetic blunders before trusting a
   precise computation.
3. **Judge feasibility** — whether a target is detectable by a given method
   before committing to a survey.
4. **Explain** why logarithmic scales, not linear ones, are the natural language
   of Earth science.
5. **State** the uncertainty in an estimate honestly, rather than implying
   false precision.

## Prerequisites

[01-01 Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md).

## 1. Intuition: why estimation is a professional skill, not a shortcut

Beginners often regard estimation as what you do when you cannot compute
properly. Professionals use it for the opposite reason: **it is how you know
whether a computation is worth trusting.**

Consider a real failure mode. You write a gravity forward-modelling script,
run it, and it reports a Bouguer anomaly of 2400 mGal over a mine shaft. The
number is printed with eight digits. Is it wrong? A practitioner answers in
seconds: crustal-scale Bouguer anomalies are at most a few hundred mGal, and a
shaft is metres across, so its anomaly should be microgals. The output is
absurd. Estimation caught in one second what debugging might take an hour.

Estimation does three jobs:

| Job | Question it answers |
|---|---|
| **Sanity check** | Is this output physically possible? |
| **Feasibility** | Can this target be detected by this method at all? |
| **Design** | What instrument, spacing, and survey size do I need? |

All three come *before* precise computation, not after it.

## 2. Precise definitions

### 2.1 Order of magnitude

Two quantities differ by **one order of magnitude** if their ratio is about 10.
The order of magnitude of a number $x$ is the integer $n$ such that

$$10^{n - 1/2} \le |x| < 10^{n + 1/2},$$

i.e. $n = \mathrm{round}(\log_{10}|x|)$. So $7\times10^{2}$ has order of
magnitude 3 (because $\log_{10} 700 \approx 2.85 \to 3$).

### 2.2 Fermi estimation

A **Fermi estimate** is a structured guess formed by decomposing a hard quantity
into factors, each of which can be bounded independently. The errors in the
factors tend to cancel, so the product is usually good to a factor of a few even
when each factor is only good to a factor of 3.

### 2.3 Anchors

Estimation is impossible without memorised **anchors** — values you know to
roughly one significant figure. You need perhaps thirty of them for geophysics.
The essential set:

| Quantity | Anchor value |
|---|---|
| Earth radius | $6.4\times10^{6}$ m |
| Earth mass | $6\times10^{24}$ kg |
| Mean crustal density | 2700 kg/m³ |
| Mantle density | 3300–5500 kg/m³ |
| Core density | 10 000–13 000 kg/m³ |
| P-wave speed, crust | 6 km/s |
| P-wave speed, mantle | 8–13 km/s |
| S-wave speed, crust | 3.5 km/s |
| $g$ at surface | 9.81 m/s² |
| Crustal geothermal gradient | 25 K/km |
| Surface heat flow | 60–90 mW/m² |
| Earth's magnetic field, surface | 25 000–65 000 nT |
| Mantle viscosity | $10^{21}$ Pa·s |
| Earth age | $4.5\times10^{9}$ yr |
| 1 year | $3.15\times10^{7}$ s |

Memorising these is not rote learning for its own sake; they are the units in
which you will think.

## 3. Derivations and worked reasoning

### 3.1 The Fermi method, step by step

**Problem.** Estimate the total seismic energy released by all earthquakes
worldwide in one year.

**Step 1 — decompose.** Total energy = (number of events) × (energy per event),
summed over magnitude. Rather than summing, use the fact that energy release is
dominated by the largest events, and estimate the "effective" contribution.

**Step 2 — bound the number of events.** From long-term catalogues, the
Gutenberg–Richter relation gives roughly a tenfold decrease in the number of
events per unit magnitude increase. Anchor: about 15–20 events of $M \ge 7$ occur
per year globally, and roughly one $M \ge 8$ per year. These are order-of-
magnitude anchors, not precise counts.

**Step 3 — bound the energy per event.** The empirically calibrated relation
between radiated seismic energy $E_s$ (joules) and magnitude is of the form

$$\log_{10} E_s \approx 1.5 M + 4.8.$$

So $M = 7$ gives $E_s \sim 10^{15.3} \approx 2\times10^{15}$ J, and $M = 8$
gives $E_s \sim 10^{16.8} \approx 6\times10^{16}$ J. Because of the 1.5 factor in
the exponent, each magnitude unit is about $10^{1.5} \approx 32$ times more
energy — **the largest events dominate completely.**

**Step 4 — combine.** Take ~18 events at $M \approx 7$ (≈ $3.6\times10^{16}$ J
total) plus ~1 event at $M \approx 8$ (≈ $6\times10^{16}$ J):

$$E_{\text{total}} \sim 10^{17}\ \mathrm{J}.$$

**Step 5 — interpret.** To make this tangible: global annual energy consumption
is of order $10^{20}$ J. So the entire year's seismicity releases roughly
**one thousandth** of what humanity burns in a year — and the 2011 Tōhoku event
alone released about $10^{17}$ J, comparable to the world's annual total in one
event.

**Step 6 — state the uncertainty.** The estimate is good to roughly one order of
magnitude, limited by the catalogue completeness at low magnitude and by the
scatter in the energy–magnitude relation. You should say "$10^{17}$ J, probably
within a factor of 3" rather than "1.4×10¹⁷ J".

> **Now go verify.** Look up a peer-reviewed estimate of global seismic energy
> release and compare. This is the discipline: an estimate is a hypothesis to be
> checked, not a conclusion.

### 3.2 Feasibility: is a target detectable?

**Problem.** A tunnel of 6 m diameter lies 25 m below the surface in soil, and
is air-filled. Can a microgravity survey find it? Surface gravity resolution is
about 0.01 mGal for a careful survey.

**Step 1 — what is the anomaly?** Approximate the tunnel by an infinite
horizontal cylinder (justified because 6 m diameter ≪ its length). The vertical
gravity anomaly above a cylinder of radius $a$, density contrast $\Delta\rho$,
axis at depth $z$ is

$$g_z = \frac{2\pi G \Delta\rho\, a^{2}}{z},$$

evaluated directly above the axis.

**Step 2 — insert numbers.** Here we need the *density deficit* of air relative
to soil. Taking soil at 2000 kg/m³ and air at ~1 kg/m³, the contrast is

$$\Delta\rho \approx -(2000 - 1) \approx -2\times10^{3}\ \mathrm{kg\,m^{-3}}.$$

With $G = 6.674\times10^{-11}$, $a = 3$ m, $z = 25$ m:

$$g_z = \frac{2\pi (6.674\times10^{-11})(2\times10^{3})(3)^{2}}{25}
\approx \frac{2\pi \times 6.674\times10^{-11} \times 1.8\times10^{4}}{25}.$$

Compute the numerator: $2\pi \approx 6.283$,
$6.283 \times 6.674\times10^{-11} = 4.19\times10^{-10}$,
$\times 1.8\times10^{4} = 7.55\times10^{-6}$.
Divide by 25: $g_z \approx 3.0\times10^{-7}\ \mathrm{m\,s^{-2}}$.

**Step 3 — convert to mGal.** $3.0\times10^{-7} / 10^{-5} = 3.0\times10^{-2}$,
so

$$g_z \approx 0.030\ \mathrm{mGal}.$$

**Step 4 — compare with resolution.** 0.030 mGal is **three times** the 0.01 mGal
resolution. Detectable, but only with: careful survey design (station spacing
smaller than the depth so the anomaly is sampled, not aliased), terrain
correction, tidal correction, and repeat readings. In practice a real survey
would want a signal-to-noise ratio better than 3, so this is **marginal**.

**Step 5 — what would you do about it?** Options: reduce noise (repeat
measurements), increase the signal (survey in winter when the water table
differs, or use a second method such as GPR or seismic), or use a more sensitive
instrument.

**The general shape of a feasibility calculation.** Always:

$$\text{signal} > \text{resolution} \times \text{(safety factor of 3–10)}.$$

A signal equal to the resolution is not detectable in practice.

### 3.3 Diffusion: how long does heat take to reach a given depth?

This estimate recurs constantly in geophysics — heat, groundwater pressure, and
electromagnetic fields all obey diffusion equations, and they all share the
scaling derived here.

The diffusion equation for a scalar field $T$ with diffusivity $\kappa$ is

$$\frac{\partial T}{\partial t} = \kappa \frac{\partial^{2} T}{\partial z^{2}}.$$

**Dimensional reasoning.** If the only length scale is $L$ and the only
timescale is $\tau$, then dimensional homogeneity requires

$$\frac{[T]}{\tau} \sim \kappa \frac{[T]}{L^{2}}
\quad\Longrightarrow\quad
\tau \sim \frac{L^{2}}{\kappa}.$$

**This is the single most useful scaling law in geophysics.** Note that the
timescale goes as the *square* of the length, so diffusion is brutally slow at
large scales.

**Apply it.** Take rock thermal diffusivity
$\kappa \approx 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$ (a standard value, of order
1 mm²/s). How long for a surface temperature change to reach 100 m depth?

$$\tau \sim \frac{(100)^{2}}{10^{-6}} = 10^{10}\ \mathrm{s}.$$

Convert: $10^{10} / 3.15\times10^{7} \approx 320$ years.

So a surface temperature change takes **centuries** to propagate to 100 m. This
one estimate explains a great deal of geophysics:

- Why borehole temperature profiles record past climate (and how they are
  analysed) — relevant to
  [16-atmosphere-climate](../../16-atmosphere-climate/README.md).
- Why deep geothermal systems respond slowly to exploitation.
- Why induced seismicity from fluid injection appears days to months after
  injection begins — pore-pressure diffusion, with a much smaller hydraulic
  diffusivity, over hundreds of metres. The same $\tau \sim L^2/\kappa$ law
  governs it. See
  [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md).
- Why magnetotelluric sounding depth is frequency-dependent: skin depth
  $\delta \sim \sqrt{2/(\mu_0 \sigma \omega)}$ is the diffusion scaling applied
  to EM fields. See
  [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md).

**One scaling law, four subdisciplines.** This is what makes order-of-magnitude
reasoning powerful: it identifies *structural similarity* between problems that
look different.

## 4. Python demonstration

Save as `code/fermi_estimation.py`. The functions are designed to be reused in
later projects as quick feasibility checks.

```python
"""Order-of-magnitude estimation utilities for geophysics.

Run:  python3 fermi_estimation.py
Requires: Python standard library only.
"""

from __future__ import annotations

import math

G = 6.674e-11          # gravitational constant, m^3 kg^-1 s^-2
MGAL = 1.0e-5          # 1 mGal in m/s^2
YEAR = 3.156e7         # seconds in a Julian year

# Anchors, quoted to roughly one significant figure (see lesson Section 2.3).
ANCHORS = {
    "earth_radius_m": 6.371e6,
    "earth_mass_kg": 5.972e24,
    "mean_crust_density_kg_m3": 2.7e3,
    "p_velocity_crust_m_s": 6.0e3,
    "g_surface_m_s2": 9.81,
    "surface_heat_flow_mW_m2": 7.0e1,
    "mantle_viscosity_Pa_s": 1.0e21,
    "thermal_diffusivity_m2_s": 1.0e-6,
}


def gravity_anomaly_cylinder_mgal(
    radius_m: float, depth_m: float, density_contrast_kg_m3: float
) -> float:
    """Peak vertical gravity anomaly above an infinite horizontal cylinder.

    g_z = 2*pi*G*drho*a^2 / z, converted from m/s^2 to mGal.

    Validity: the cylinder length must greatly exceed the observation
    distance, and the observation point must be directly above the axis.
    """
    g_si = 2.0 * math.pi * G * density_contrast_kg_m3 * radius_m ** 2 / depth_m
    return g_si / MGAL


def diffusion_time_seconds(length_m: float, diffusivity_m2_s: float) -> float:
    """Characteristic diffusion time, tau ~ L^2 / kappa (order of magnitude)."""
    return length_m ** 2 / diffusivity_m2_s


def magnetic_dipole_field_nT(
    moment_A_m2: float, distance_m: float, mu0: float = 4e-7 * math.pi
) -> float:
    """Approximate equatorial field of a dipole, in nT.

    On the magnetic equator the field magnitude is mu0*m/(4*pi*r^3).
    """
    b_tesla = mu0 * moment_A_m2 / (4.0 * math.pi * distance_m ** 3)
    return b_tesla * 1e9


def report(label: str, value: float, unit: str) -> None:
    print(f"{label:<52} {value:>12.3e} {unit}")


def main() -> None:
    print("=" * 80)
    print("1. Feasibility: air-filled tunnel under 25 m of soil")
    print("=" * 80)
    a = 3.0                    # radius of a 6 m diameter tunnel
    z = 25.0                   # depth to axis
    drho = -(2000.0 - 1.0)     # air in soil: negative contrast
    anomaly = gravity_anomaly_cylinder_mgal(a, z, drho)
    resolution = 0.010         # mGal
    report("peak anomaly", anomaly, "mGal")
    report("survey resolution", resolution, "mGal")
    print(f"{'signal-to-resolution ratio':<52} {abs(anomaly) / resolution:>12.2f}")
    print("Verdict:", "DETECTABLE but marginal (SNR < 10)" if 1 < abs(anomaly) / resolution < 10
          else "review survey design")

    print()
    print("=" * 80)
    print("2. How deep does the anomaly of a buried sphere reach?")
    print("=" * 80)
    for mass_kg in (1e9, 1e10, 1e11):
        for depth in (100.0, 300.0, 1000.0):
            g_si = G * mass_kg / depth ** 2
            print(f"  M = {mass_kg:.0e} kg, depth = {depth:>6.0f} m -> "
                  f"{g_si / MGAL:>10.4f} mGal")

    print()
    print("=" * 80)
    print("3. Diffusion timescale tau ~ L^2 / kappa")
    print("=" * 80)
    for length, name in ((10.0, "10 m"), (100.0, "100 m"),
                         (1000.0, "1 km"), (1e5, "100 km")):
        tau = diffusion_time_seconds(length, ANCHORS["thermal_diffusivity_m2_s"])
        print(f"  heat over {name:>7}: {tau:>10.3e} s = {tau / YEAR:>10.3e} yr")
        tau_h = diffusion_time_seconds(length, 1e-2)
        print(f"  {'':>8}  (hydraulic, kappa=1e-2 m^2/s): {tau_h / 86400:>10.3e} days")

    print()
    print("=" * 80)
    print("4. Earth's dipole moment and surface field at the equator")
    print("=" * 80)
    # Order-of-magnitude anchor for the present geomagnetic dipole moment.
    dip = 8.0e22   # A m^2, approximately the current axial dipole moment
    r = ANCHORS["earth_radius_m"]
    report("equatorial dipole field", magnetic_dipole_field_nT(dip, r), "nT")
    print("Compare with the anchored surface range 25 000 - 65 000 nT.")

    print()
    print("=" * 80)
    print("5. Sanity check: catch an absurd model output")
    print("=" * 80)
    implausible = 2400.0   # mGal claimed over a mine shaft
    plausible_max = 300.0  # mGal, crustal-scale Bouguer anomaly
    print(f"claimed anomaly      = {implausible} mGal")
    print(f"plausible upper bound= {plausible_max} mGal")
    print("Verdict:", "REJECT - physically implausible" if implausible > 3 * plausible_max
          else "plausible")


if __name__ == "__main__":
    main()
```

### What to observe

| Observation | Lesson |
|---|---|
| The tunnel anomaly is ~0.03 mGal — only 3× resolution | Signal comparable to noise needs repeat measurement |
| Heat takes ~320 yr to diffuse 100 m, but hydraulic pressure only ~days | Same law, different diffusivity — orders of magnitude apart |
| The 2400 mGal claim is rejected instantly | This is the sanity check working |

> **Breaking exercise.** In the cylinder function, change the depth from 25 m to
> 50 m and predict the new anomaly *before* running. (Answer: the anomaly scales
> as $1/z$, so it halves.) Now change the radius from 3 m to 6 m and predict
> again. (Answer: it scales as $a^2$, so it quadruples.) Confirm both. **These
> two scalings — $1/z$ for depth and $a^2$ for size — are worth remembering
> permanently.**

## 5. Exercises

★★ and ★★★ exercises have solutions in
[`exercises/02-orders-of-magnitude-solutions.md`](./exercises/02-orders-of-magnitude-solutions.md).

### ★ Foundational

**★1.** Round each to one significant figure and state its order of magnitude:
(a) 8.4×10³, (b) 2.7×10⁻⁵, (c) 6.02×10²³, (d) 9.81.

**★2.** Estimate without calculating precisely, then check: how many seconds in
a century? How many metres in a degree of latitude at the equator? (Use the
Earth radius anchor.)

**★3.** Sketch, without computing, whether a $10^{12}$ kg orebody at 1 km depth
produces an anomaly above or below a 0.01 mGal detection threshold.

### ★★ Applied

**★★4.** Estimate the mass of the Earth's atmosphere. Decompose as
(mean surface pressure × Earth surface area / g). Compare your answer with the
commonly quoted order of magnitude.

**★★5.** A fluid-injection well raises pore pressure at 500 m distance. Using
$\tau \sim L^{2}/\kappa$ with a hydraulic diffusivity of
$\kappa = 10^{-2}\ \mathrm{m^{2}\,s^{-1}}$, estimate the delay before the
pressure change arrives. Express in days. Then repeat for $\kappa = 10^{-1}$
and explain why the answer is so sensitive to $\kappa$.

**★★6.** A magnetotelluric survey wishes to sound to 10 km depth in a
half-space of resistivity 100 Ω·m. Using the skin-depth relation
$\delta \approx 503\sqrt{\rho T}$ (with $\delta$ in metres, $\rho$ in Ω·m,
$T$ in seconds), estimate the period $T$ required. Is this a practical survey?

**★★7.** Detectability: an unexploded ordnance item of mass 20 kg (steel,
density 7800 kg/m³) lies at 3 m depth in soil of density 1800 kg/m³. Estimate
the peak magnetic anomaly if its induced magnetisation is
$M \approx 1\ \mathrm{A\,m^{-1}}$ and it may be treated as a dipole of moment
$m = M V$. Compare with a typical total-field magnetometer resolution of 0.1 nT.
State your assumptions explicitly.

### ★★★ Research-oriented

**★★★8.** Estimate the rate at which the Earth's core–mantle boundary is losing
heat, using: core radius $\approx 3480$ km, CMB heat flow of order
$10\ \mathrm{TW}$, and the mass of the outer core. Then estimate how long the
core can sustain this before solidifying, assuming a latent heat of order
$10^{6}$ J/kg and a core mass of order $10^{24}$ kg. State every assumption and
give your answer as a range, not a value. **Then check your reasoning against a
review paper on the geodynamo's thermal evolution**, and report where your
estimate diverges and why. (This is the standard research workflow: estimate,
then compare, then explain the discrepancy.)

**★★★9.** The diffusive scaling $\tau \sim L^{2}/\kappa$ was derived by
dimensional analysis. Verify it numerically: solve the 1-D heat equation
$\partial_t T = \kappa \partial_{zz} T$ for a step change in surface temperature,
and measure the time at which the temperature at depth $L$ has risen to half its
final value. Repeat for several $L$ and $\kappa$ and confirm the $L^{2}$ and
$1/\kappa$ scalings. Report the constant of proportionality you measure (it
should be of order 0.1). Explain why the dimensional estimate cannot supply that
constant but can supply the scaling exponents.

## 6. Common mistakes

1. **Estimating only to confirm what you already computed.** The estimate must
   come *first*, or it cannot detect your error.
2. **Quoting a Fermi estimate to three significant figures.** It is good to a
   factor of a few; saying so is part of the answer.
3. **Forgetting the safety factor.** Signal equal to resolution is a detection
   on paper only.
4. **Using the wrong density contrast.** Whether a target is a high or low
   relative to its host determines the *sign* and often the *size* of the
   anomaly. Air in soil is a large negative contrast; a sulphide orebody in
   granite is a modest positive one.
5. **Assuming $L^2/\kappa$ where advection dominates.** The scaling applies to
   *diffusion*. Where a fluid flows, advective timescales
   ($\tau \sim L/v$) control, and they can be enormously shorter.
6. **Treating anchors as exact.** Crustal density ranges 2200–3000 kg/m³. Your
   estimate inherits that range.

## 7. Real-world applications

- **Survey feasibility and cost.** Before a multi-million-dollar acquisition,
  the first question is always "is the expected anomaly above the noise floor?"
  This lesson is that calculation.
- **Environmental investigations.** Estimating whether a 0.05 mGal anomaly can
  resolve a buried tank, or whether a 5 nT anomaly can locate a drum.
- **Hazard assessment.** Diffusion timescales govern how quickly pressure
  changes from a reservoir can reach a fault — the central question in induced
  seismicity.
- **Instrument specification.** Deciding whether you need a 0.001 mGal
  superconducting gravimeter or whether a 0.01 mGal relative instrument
  suffices is a feasibility calculation.
- **Interpreting published work.** When a paper reports an anomaly, estimating
  what the source must have been tells you immediately whether the
  interpretation is plausible.

## 8. Further reading

- **Turcotte, D. L., & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Chapter 1 and the heat-transfer chapters. Level: advanced
  undergraduate to graduate. The $L^{2}/\kappa$ scaling and diffusion
  timescales are treated rigorously, and the book is full of the kind of
  scaling arguments this lesson introduces.
- **Stein, S., & Wysession, M. (2003). *An Introduction to Seismology, Earthquakes,
  and Earth Structure*. Blackwell.** Level: intermediate to graduate. Contains
  the magnitude–energy relations used in Section 3.1 and extensive order-of-
  magnitude reasoning about the Earth.
- **Fermi, E. (1950).** *Two notes on the estimation of the energy released by an
  atomic explosion* (technical notes); and the widely-circulated "Fermi problems"
  as used in physics education. Level: accessible. The origin of the method.
- **Bohren, C. F., & Huffman, D. R. (1983). *Absorption and Scattering of Light
  by Small Particles*. Wiley.** Level: advanced. Included because its
  dimensional-analysis arguments (and its opening chapter on the value of
  physical reasoning) are a model of the technique used in Section 3.3.
- **Anderson, D. L. (1989). *Theory of the Earth*. Blackwell.** Level: graduate.
  Extensive use of scaling and order-of-magnitude arguments for the Earth's
  interior; see especially the discussion of seismic velocities and density.

> Citation note: bibliography only. Confirm editions and availability through
> your library; this repository does not host copyrighted text.

## 9. Related lessons

- [01 Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md) — the feasibility calculation here extends Section 4.3 of that lesson.
- [03 Units, SI Conventions and Dimensional Analysis](./03-units-and-dimensional-analysis.md) — the systematic form of the dimensional reasoning used in Section 3.3.
- [01-05 Absolute vs Relative Error, Conditioning and Stability](./05-error-and-conditioning.md) — what to do when your estimate disagrees with your computation.
- [05-core-geophysics](../../05-core-geophysics/README.md) — feasibility and survey design in full.
