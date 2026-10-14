# Solutions — 06-11-06 Hazard Maps, Site Amplification and Design Codes

> Read after attempting the exercises. Numbers were computed with the formulas of
> the lesson. All values are **SYNTHETIC**.

Lesson: [06 Hazard Mapping](../06-hazard-mapping.md).

---

## ★1 — impedance ratio, resonance and peak

$$\frac{Z_2}{Z_1} = \frac{\rho_2\beta_2}{\rho_1\beta_1}
= \frac{2.5\times900}{1.7\times180} = \frac{2250}{306} = 7.353.$$

$$f_0 = \frac{\beta_1}{4H} = \frac{180}{4\times25} = \frac{180}{100}
= 1.80\ \mathrm{Hz}.$$

Lossless peak amplification at $f_0$ equals the impedance ratio, **7.353**. This
profile amplifies more than the lesson's example (5.333) because the velocity
contrast is larger, and it resonates at a higher frequency because the layer is
thinner (25 m against 30 m) despite the slower soil.

---

## ★2 — damping and the peak

Interpolating between $Q = 20$ ($A = 4.408$) and $Q = 10$ ($A = 3.755$) gives
approximately

$$A(15) \approx \tfrac{1}{2}(4.408 + 3.755) = 4.08,$$

i.e. about 77% of the lossless 5.333.

**Trend:** the peak amplification falls monotonically with $Q$, and — note — it
falls *fast* at low $Q$: halving $Q$ from 10 to 5 costs 0.86 in $A$, while
halving it from 100 to 50 (interpolating) would cost only a few hundredths. The
peak is controlled by the ratio of the impedance contrast to the damping, and for
soft soils with $Q$ near 10–20 the damping term dominates.

---

## ★3 — surface rate with a linear site factor

$$\lambda_\text{surface}(0.2) = \lambda_\text{bedrock}\!\left(\frac{0.2}{1.5}\right)
= \lambda_\text{bedrock}(0.1333).$$

$$\lambda = 0.002\left(\frac{0.1333}{0.1}\right)^{-2.5}
= 0.002 \times 1.3333^{-2.5}.$$

$\ln 1.3333 = 0.28768$, so the exponent is $-0.71920$ and
$e^{-0.71920} = 0.4872$:

$$\lambda = 0.002\times0.4872 = 9.74\times10^{-4}\ \mathrm{yr^{-1}},
\qquad T = 1026\ \mathrm{yr}.$$

For comparison the bedrock rate at $0.2\ \mathrm{g}$ is
$0.002\times2^{-2.5} = 3.54\times10^{-4}\ \mathrm{yr^{-1}}$ ($T = 2828$ yr): the
site factor of 1.5 has shortened the return period of $0.2\ \mathrm{g}$ by a factor
of 2.8.

---

## ★4 — the nonlinear factor

With $z_s = 0.30\ \mathrm{g}$ and $F_\text{lin} = 1.7989$:

$$F(0.30) = 1 + \frac{1.7989 - 1}{1 + (0.30/0.30)^2}
= 1 + \frac{0.7989}{2} = 1.3995.$$

Implied bedrock PGA:

$$\frac{z_s}{F} = \frac{0.30}{1.3995} = 0.2144\ \mathrm{g}.$$

The nonlinear factor 1.3995 is **below** the linear 1.7989 — a 22% reduction —
because the denominator $1 + (z_s/z_\text{ref})^2$ grows with the surface
amplitude: the soil stiffens (relatively) as it strains, so it amplifies less. The
correction vanishes at small $z_s$ (where $F \to F_\text{lin}$) and is the reason a
linear site factor overestimates strong surface motion.

---

## ★5 — why the band matters

The fundamental resonance of the demonstration's profile is at
$f_0 = 1.6667\ \mathrm{Hz}$, where the lossless amplitude would be 5.333 and the
damped ($Q = 20$) value is 4.408. The 0.5–2 Hz band contains that peak; the
0.5–10 Hz band dilutes it with the anti-resonance near 3.33 Hz (where $A = 1$) and
the second peak near 5 Hz. Hence the narrow-band mean (2.1254) exceeds the
wide-band mean (1.7989).

A structure with a 1 s period responds near 1 Hz, i.e. *below* the site resonance
at 1.67 Hz, so it neither sees the peak (4.41) nor the band average (1.80); it
sees whatever the transfer function is at 1 Hz, which for this profile is about
1.65. This is the reason spectral site factors are period-dependent and a single
"amplification factor" is only an approximation.

---

## ★6 — three interpolation rules at one point

**Linear interpolation** between $x = 4$ km (260 m/s) and $x = 9$ km (620 m/s) at
$x = 6.5$ km, i.e. halfway:

$$V_{S30} = 260 + (620 - 260)\times\frac{6.5-4}{9-4} = 260 + 360\times0.5
= 440.0\ \mathrm{m\,s^{-1}}.$$

Amplification: $A = (760/440.0)^{0.5} = \sqrt{1.7273} = 1.314$.

Summary of the three rules at $x = 6.5$ km:

| rule | $V_{S30}$ (m/s) | $A$ |
|---|---|---|
| nearest borehole ($x = 4$ km) | 260.0 | 1.710 |
| inverse-distance weighting | 425.1 | 1.337 |
| linear interpolation | 440.0 | 1.314 |

The nearest-borehole rule gives 30% more amplification than the other two, because
it ignores the 620 m/s borehole at $x = 9$ km that is doing most of the smoothing.

**What to report:** the interpolation rule *and* a measure of its effect. The
defensible practice is to map with a stated rule and also publish the range
obtained with the alternatives (or with a geostatistical method that provides a
prediction variance). Reporting 440 m/s alone hides a 69% spread in $V_{S30}$ and a
factor of 1.30 in amplification.

---

## ★7 — field programme for a site transfer function

**Observable.** Horizontal-to-vertical spectral ratios (HVSR) from ambient noise for
the resonance frequency and its amplitude, plus site-to-reference spectral ratios
(SSR) from earthquake records for the full transfer function.

**Estimator.** HVSR: the mode of the H/V curve over long, quiet windows with
window-by-window rejection of transients. SSR: the spectral ratio of the target
station to a nearby reference station on rock, computed for each event and
averaged after removing the source and path terms common to both.

**Band in which it must work.** The design band of the structures of interest — for
a 0.5–10 Hz band the measurement must resolve the fundamental and at least the
second peak, which requires a usable signal up to several times $f_0$ and therefore
a soil column whose resonance is inside the band.

**Validation metric.** Predicted transfer function versus measured SSR, compared
as (i) the resonance frequency $f_0$ to within a stated tolerance, (ii) the peak
amplitude with its bootstrap interval, and (iii) the full curve via a misfit such
as $\sum[\ln A_\text{obs} - \ln A_\text{pred}]^2$ over the band. Predict in
advance the tolerance from the borehole parameters' uncertainties.

**One systematic effect to handle.** The reference station is not on an ideal
half-space: if it sits on soft rock or has its own resonance, the "site" ratio
divides one site response by another and both the peak amplitude and its frequency
are biased. A second classic contaminant is 2D/3D focusing, which shows up as a
peak that does not move when the layer parameters are perturbed, and which no 1D
model can reproduce.

---

## ★8 — decomposing the epistemic spread of a hazard pixel

**Design.** Hold the source model fixed and vary one component at a time, then all
combinations, and record the hazard amplitude at the design probability:

1. *Interpolation*: nearest, inverse-distance, linear and a geostatistical
   prediction with its variance — four branches.
2. *Site relation*: two or three defensible $V_{S30}$-to-amplification relations
   plus the nonlinear correction on/off — four branches.
3. *GMPE*: at least three published relations, plus the two functional forms of
   [lesson 05](../05-ground-motion-models.md) to represent the extrapolation
   ambiguity — five branches.
4. *Source rate*: the rate estimate and its plausible range from the catalogue
   completeness and declustering choices of
   [lesson 07](../07-catalog-declustering.md) — three branches.

Enumerate the $4\times4\times5\times3 = 240$ combinations, weight the branches with
pre-declared logic-tree weights, and record the design amplitude for each.

**Score.** A variance decomposition: the share of the total variance of the
$\log$ design amplitude explained by each factor, computed as the reduction in
variance when that factor is fixed. Report the shares, the total 5–95% range, and
the factor interaction terms. Use a fractional-factorial design (for example a
resolution-IV design with a few dozen runs) if the full enumeration is expensive,
and verify a subset of the full runs to confirm the design's correctness.

**How to report it so a map user can act on it.** Publish the design amplitude with
its 5–95% branch range, and state which factor dominates: if the GMPE dominates,
the user must know that the number is transferable but model-dependent; if the
interpolation dominates, the number is site-specific but only as good as the local
borehole coverage and cannot be improved by better GMPEs. Without that statement
the map user cannot tell which of those two very different situations they are in.
