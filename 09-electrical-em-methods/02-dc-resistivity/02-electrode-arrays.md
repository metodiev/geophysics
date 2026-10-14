---
id: 09-02-02
title: "Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole"
level: advanced
prereqs: ["09-02-01"]
tags: [electrical-methods, arrays, sensitivity, depth-of-investigation, dipole-dipole, werner]
---

# Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole

An array is a choice about *where* to put sensitivity, and every choice is paid
for in signal. This lesson computes the geometric factor of every standard
layout from one formula, measures the signal each delivers, and then measures
the depth sensitivity properly — using the exact layered forward model, not a
rule of thumb — including a result that surprises most practitioners: half of a
DC array's total sensitivity sits in an unmeasurable surface step, and the
buried half is the honest measure of depth penetration.

**All models and data in this module are SYNTHETIC.** The half-space and layered
models, the current and the electrode geometries are chosen teaching values; no
survey or instrument is referred to.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the geometric factor of Wenner, Schlumberger, dipole-dipole,
   pole-dipole and pole-pole layouts from the general four-electrode formula and
   **verify** each against its closed form.
2. **Compute** the signal level each array delivers for a stated current, and
   the ratio to the Wenner value.
3. **Define** the cumulative sensitivity $F(z)$ and use the exact layered
   forward model to compute it.
4. **Explain** why $F(0^+) = 1/2$ for every DC array, and why that forces a
   factor 2 into any depth-of-investigation statement.
5. **Compute** a depth of investigation, a peak sensitivity depth and a
   normalisation integral for each array.
6. **Verify** the differential sensitivity against the analytic Fréchet kernel
   of a homogeneous half-space.
7. **Explain** why a dipole-dipole array has negative sensitivity at depth.

## Prerequisites

- [09-02-01 Resistivity Principle and the Four-Electrode Arrangement](01-resistivity-principle.md) —
  the geometric factor and the point-source potential.

## 1. Five layouts, one formula

With $k$ from lesson [09-02-01](01-resistivity-principle.md), each named array
is a choice of electrode positions:

| array | positions ($a$ = unit spacing) | closed form for $k$ |
|---|---|---|
| Wenner | $-1.5a,\ 1.5a,\ -0.5a,\ 0.5a$ | $2\pi a$ |
| Schlumberger | $-L/2,\ L/2,\ -l/2,\ l/2$ | $\pi(L^{2}-l^{2})/(4l)$ |
| dipole-dipole | $0,\ a,\ (n+1)a,\ (n+2)a$ | $\pi n(n+1)(n+2)a$ |
| pole-dipole | $0,\ \infty,\ (n+1)a,\ (n+2)a$ | $2\pi(n+1)(n+2)a$ |
| pole-pole | $0,\ \infty,\ a,\ -\infty$ | $2\pi a$ |

The demo prints the general formula and the closed form side by side with their
ratio, and every ratio is $1.000000$:

| array ($a = 5$ m) | $|k|$ general | $|k|$ closed | ratio |
|---|---|---|---|
| Wenner | 31.4159 | 31.4159 | 1.000000 |
| Schlumberger $L = 4a$, $l = a$ | 58.9049 | 58.9049 | 1.000000 |
| dipole-dipole $n = 1$ | 94.2478 | 94.2478 | 1.000000 |
| dipole-dipole $n = 3$ | 942.4778 | 942.4778 | 1.000000 |
| dipole-dipole $n = 6$ | 5277.8757 | 5277.8757 | 1.000000 |
| pole-dipole $n = 3$ | 628.3185 | 628.3185 | 1.000000 |
| pole-pole | 31.4159 | 31.4159 | 1.000000 |

Because $\rho_a = k\Delta V/I$, a large $k$ means a small voltage for the same
apparent resistivity. The demo's signal table for $\rho = 100\
\Omega\,\mathrm{m}$, $I = 0.10\ \mathrm{A}$:

| array | $|k|$ (m) | $\Delta V$ (mV) | relative to Wenner |
|---|---|---|---|
| Wenner | 31.4159 | 318.3099 | 1.0000 |
| Schlumberger $L = 4a$, $l = a$ | 58.9049 | 169.7653 | 0.5333 |
| dipole-dipole $n = 1$ | 94.2478 | 106.1033 | 0.3333 |
| dipole-dipole $n = 3$ | 942.4778 | 10.6103 | 0.0333 |
| dipole-dipole $n = 6$ | 5277.8757 | 1.8947 | 0.0060 |
| pole-dipole $n = 3$ | 628.3185 | 15.9155 | 0.0500 |
| pole-pole | 31.4159 | 318.3099 | 1.0000 |

Going from $n = 1$ to $n = 6$ in the dipole-dipole array costs a factor 30 in
signal. **Depth is bought with voltage, and the exchange rate is fixed.** That
is the design problem in one sentence.

## 2. Depth sensitivity, defined correctly

Perturb the resistivity of a thin layer at depth $z$ by a small fraction
$\varepsilon$ and measure the fractional change of $\Delta V$:

$$s(z) = \frac{1}{\varepsilon t}\,
\frac{\Delta V(\rho\to\rho(1+\varepsilon)\ \text{in layer}) - \Delta V}
{\Delta V},$$

with $t$ the layer thickness, so $s$ has units $\mathrm{m^{-1}}$. Two facts
follow from the layered forward model, and the demo computes both exactly
(it uses the recurrence of [09-02-06](06-resistivity-forward-modelling.md), so
no approximation is involved):

- **A uniform perturbation of everything gives $\Delta V \to (1+\varepsilon)
  \Delta V$**, because $\Delta V \propto \rho$. So the *cumulative* response
  $F(z)$ for a perturbed layer from the surface to depth $z$ must run from
  $F(0^+)$ to $1$.
- The demo measures $F(0^+)$ by perturbing a layer of thickness $0.05\ \mathrm{m}$
  and prints values between $0.49826$ and $0.50022$ for seven different arrays:
  $F(0^+)=1/2$, **for every DC array**.

The first half of the sensitivity lives in a *surface step*: perturbing an
arbitrarily thin layer at the surface changes the reading by $\varepsilon/2$,
which does not shrink with the layer. The buried half is what a survey can
resolve, so the density must be normalised as

$$s(z) = 2\,\frac{\mathrm{d}F}{\mathrm{d}z}, \qquad \int_0^\infty s(z)\,
\mathrm{d}z = 1 \quad\text{(buried half)},$$

and the depth of investigation is defined as the depth above which half of that
buried mass lies.

| array | $F(0.05\ \mathrm{m})$ | $F(1\ \mathrm{m})$ | $F(5\ \mathrm{m})$ | $F(20\ \mathrm{m})$ |
|---|---|---|---|---|
| Wenner | 0.50017 | 0.56175 | 0.90630 | 0.99723 |
| Schlumberger $L = 4a$, $l = a$ | 0.50011 | 0.53275 | 0.83559 | 0.99334 |
| dipole-dipole $n = 1$ | 0.50022 | 0.58246 | 0.97380 | 1.00219 |
| dipole-dipole $n = 3$ | 0.50002 | 0.51622 | 0.76242 | 1.00849 |
| dipole-dipole $n = 6$ | 0.49826 | 0.50976 | 0.60842 | 0.97948 |
| pole-dipole $n = 3$ | 0.50003 | 0.50601 | 0.62080 | 0.94194 |
| pole-pole | 0.50010 | 0.53572 | 0.77634 | 0.93797 |

Values above 1 (dipole-dipole) are not an error: those arrays have **negative
sensitivity** at depth, so the cumulative function can overshoot and come back.
A *deeper resistor* can therefore lower the apparent resistivity of a
dipole-dipole array, which is one of the classic traps of the method.

## 3. Depth of investigation versus signal

| array ($a = 5$ m) | DOI (m) | peak depth (m) | $\int_0^{40} s\,\mathrm{d}z$ | $\Delta V$ (mV) |
|---|---|---|---|---|
| Wenner | 2.60 | 1.60 | 1.0008 | 318.31 |
| Schlumberger $L = 4a$, $l = a$ | 3.63 | 2.30 | 0.9999 | 169.77 |
| dipole-dipole $n = 1$ | 2.08 | 1.50 | 1.0024 | 106.10 |
| dipole-dipole $n = 3$ | 4.81 | 3.70 | 1.0066 | 10.61 |
| dipole-dipole $n = 6$ | 8.62 | 1.00 | 1.0195 | 1.89 |
| pole-dipole $n = 3$ | 8.54 | 5.50 | 0.9802 | 15.92 |
| pole-pole | 4.33 | 1.75 | 0.9386 | 318.31 |

The DOI is the depth where the *buried* sensitivity integral reaches one half.
Note the sign of the trade: the pole-pole array has the same signal as Wenner
with a deeper DOI, but it needs a remote electrode and it has no lateral
resolution to speak of; dipole-dipole $n = 6$ reaches 8.62 m with $1/168$ of the
Wenner voltage. The integral column is 1 to within the truncated deep tail —
except where the sensitivity changes sign, which is where the array's
interpretation needs the most care.

## 4. Verification against the analytic kernel

For a homogeneous half-space the exact first-order sensitivity with respect to
resistivity is analytic:

$$S_\rho(x,y,z) = \frac{I}{8\pi^{2}}\,
\nabla\!\left(\frac{1}{r_A}-\frac{1}{r_B}\right)\cdot
\nabla\!\left(\frac{1}{r_M}-\frac{1}{r_N}\right),$$

so that a perturbation $\delta\rho$ changes the reading by
$\delta(\Delta V) = \int S_\rho\,\delta\rho\,\mathrm{d}V$ and a thin layer's
sensitivity is $s_\text{kernel}(z) = \rho\int\!\!\int S_\rho\,\mathrm{d}x\,
\mathrm{d}y/\Delta V$.

The demo evaluates the two-dimensional integral numerically for four arrays at
$z = 2, 5, 10, 20$ m and compares with the layered-model profile. The printed
ratio is $2.000$ with no trend in depth or array (2.0000–2.0083 where the
sensitivity is large, degrading to 1.84 where it is nearly zero and the
derivative of the numerical profile is dominated by quadrature noise). The
factor of 2 is exactly the definition $s = 2\,\mathrm{d}F/\mathrm{d}z$: the
kernel returns $\mathrm{d}F/\mathrm{d}z$, and the agreement is the verification,
fixing the constant $1/(8\pi^2) = 0.012665$. Two independent routes — an exact
layered forward solution and an analytic half-space kernel — agreeing to a few
per cent is the standard this folder requires of its modelling.

## 5. Worked example: choosing an array for a target

Target: a conductive horizon at depth $d = 5\ \mathrm{m}$, in ground of
$100\ \Omega\,\mathrm{m}$, with a receiver noise floor of $0.5\ \mathrm{mV}$ at
$I = 0.1\ \mathrm{A}$.

1. Wenner $a = 5$ m: DOI 2.60 m at $a = 5$ m, so use $a \approx 10$ m
   (DOI scales with $a$, see [09-02-05](05-ert-tomography.md)); $k = 62.83$ m and
   $\Delta V = 100\times0.1/62.83 = 0.159\ \mathrm{V}$ — 300 times the noise.
2. dipole-dipole $n = 3$, $a = 5$ m: DOI 4.81 m, $\Delta V = 10.61\
   \mathrm{mV}$ — 20 times the noise, and it works with a multi-channel cable.
3. dipole-dipole $n = 6$, $a = 5$ m: DOI 8.62 m, $\Delta V = 1.89\ \mathrm{mV}$
   — under four times the noise, so it is usable only with stacking.

So for 5 m, both $n = 3$ and a longer Wenner work; the dipole-dipole is chosen
when the *lateral* coverage matters, the Wenner when the *signal* does. The
decision is quantitative, and it is made before the survey, not after.

## 6. Regime of validity

1. **The sensitivity profiles assume a homogeneous reference model.** For a
   strongly layered or three-dimensional ground the profiles shift; they are
   design tools, not survey results.
2. **Point electrodes on a flat surface.** Array geometry errors cost
   0.13–0.31% per centimetre ([09-02-01](01-resistivity-principle.md)).
3. **$F(0^+)=1/2$ is a statement about the *perturbation* problem**, not about
   where the current flows: it says that the linearised response cannot separate
   the top few centimetres from the surface itself.
4. **The analytic kernel is exact only to first order and only away from the
   electrodes**, where the field is singular; the demo's ratios degrade exactly
   where the sensitivity vanishes.
5. **Induced polarisation is ignored.** The same arrays in a polarisable ground
   have a time-varying response; module 09-03 handles that.

## 7. Mastery checkpoint

1. Compute $k$ for a Wenner array with $a = 20$ m and for a dipole-dipole array
   with $n = 4$, $a = 5$ m, and state the signal ratio between them.
2. Explain in two sentences why $F(0^+) = 1/2$ and what it implies for any
   statement of the form "this array sees to 10 m".
3. From the DOI table, estimate the spacing of a Wenner array that would reach
   8 m, and state two costs of that choice.
4. A dipole-dipole array shows an *apparent* resistivity that increases with
   depth. Give two explanations consistent with negative sensitivity.

## 8. Common pitfalls

1. **Quoting a DOI without saying how it was defined.** With the surface step
   included, half of a DC array's sensitivity is at the surface, and the number
   changes by a factor of two.
2. **Choosing the largest $n$ for depth.** The signal collapses as $n^{-3}$.
3. **Assuming larger arrays are always better.** They are weaker and they smear
   lateral detail.
4. **Treating the sensitivity profiles as exact for a real ground.** They are
   computed for a homogeneous model.
5. **Ignoring the sign change.** A deeper resistor can lower $\rho_a$ for a
   dipole-dipole array.

## 9. Related modules

- [09-02-03 Apparent Resistivity and Geometric Factors](03-apparent-resistivity.md).
- [09-02-04 Vertical Electrical Sounding vs Profiling](04-sounding-profiling.md).
- [09-02-05 ERT Acquisition and Design](05-ert-tomography.md) — the same
  sensitivities arranged as a survey.
- [09-02-06 Forward Modelling Resistivity Data](06-resistivity-forward-modelling.md) —
  the layered forward model used here.
- [09-02 Resistivity Methods](README.md).

## 10. Demonstration and exercises

- [`code/electrode_arrays_demo.py`](code/electrode_arrays_demo.py) prints the
  geometric-factor table, the signal table, $F(z)$ for every array, the DOI
  table and the kernel cross-check.
- [Exercises](exercises/02-electrode-arrays-exercises.md) and
  [worked solutions](exercises/02-electrode-arrays-solutions.md).
