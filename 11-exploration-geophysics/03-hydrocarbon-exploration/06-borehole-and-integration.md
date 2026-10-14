---
id: 11-03-06
title: "Integrating Borehole Data with Seismic"
level: graduate
prereqs: ["11-03-01", "11-03-03", "05-08-06", "05-08-07"]
tags: [exploration-geophysics, borehole, well-tie, time-depth, backus, anisotropy]
---

# Integrating Borehole Data with Seismic

**All models and data in this module are SYNTHETIC.** The log model, the
wavelet, the migration-velocity error and the calibration geometries below are
chosen teaching values. No well, field or company is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a synthetic seismogram from a sonic and density log, at the right
   step in the workflow.
2. **Explain** why a single bulk shift cannot tie a log to a seismic volume, and
   **measure** the shift a velocity error requires as a function of time.
3. **Derive** the two-way time for $v(z) = v_0 + kz$ and **compute** the depth
   error produced by an error in each parameter.
4. **Quantify** how many calibration levels are needed, with noisy picks, and
   **compare** that with the error from using the wrong velocity-function form.
5. **Construct** the Backus equivalent of a layered medium and **verify** it
   against the exact travel-time average.
6. **Explain** why layering produces positive $\varepsilon$ while intrinsic clay
   anisotropy adds to it.
7. **Quantify** the depth error produced by a wavelet phase error.
8. **Report** a well tie with the information it actually validates.

## Prerequisites

- [11-03-01 Reflection Seismic in Exploration](01-seismic-in-exploration.md) —
  resolution, sampling, and bin geometry.
- [11-03-03 Reservoir Characterisation and Property Prediction](03-reservoir-characterisation.md) —
  what the tied seismic is subsequently used for.
- [05-08-06 Vertical Seismic Profiling and Check Shots](../../05-core-geophysics/08-geophysical-logging/06-seismic-while-drilling.md) —
  the measurement that provides the time-depth relation.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](../../05-core-geophysics/08-geophysical-logging/07-log-interpretation.md) —
  the log processing that must precede a synthetic.

## 1. What a well tie is for

A well tie answers one question: **which seismic event corresponds to this
rock?** It is the bridge between the log world (metres, high vertical
resolution, one location) and the seismic world (time, ~25 m resolution, a
volume). Without a tie, an interpretation is a set of surfaces with unknown
stratigraphic meaning; with a tie, an amplitude anomaly has a rock type and a
depth.

The measurement chain is:

$$\text{sonic} + \text{density} \;\rightarrow\;
Z(z) \;\rightarrow\; r(z) \;\rightarrow\;
r(t) \;\rightarrow\; \text{convolve with } w(t) \;\rightarrow\;
\text{synthetic}$$

and each arrow carries an assumption: that the logs are calibrated (sonic,
density), that $r \approx (Z_2-Z_1)/(Z_2+Z_1)$ computed from samples 0.5 m apart
represents the interfaces, that the time-depth relation is known, and that the
wavelet is known. The demonstration's log is 6001 samples at 0.5 m over 3000 m
with $v_p$ from 1766 to 3192 m/s and $\rho$ from 2090 to
2518 kg/m³; its reflectivity has rms 0.0007 and a maximum of 0.0033, and the
two-way time to the bottom of the log on the well velocity is **2.4905 s**.

**A tie is not proof.** A good tie means the log's reflectivity, the time-depth
function and the wavelet are mutually consistent at that location. It does not
mean the surfaces are chronostratigraphic, and it says nothing about 3 km away.
It is a *validation of the model*, not of the geology.

## 2. The tie: a shift, or a stretch?

Suppose the seismic volume was migrated with a velocity 5% too high, so every
event sits at $t_{\text{seis}} = t_{\text{well}}/1.05$. The demonstration
measures the correlation between the log synthetic and the seismic trace under
three tie strategies:

| tie applied | correlation |
|---|---|
| none (raw seismic) | −0.105 |
| best single bulk shift (+27 ms) | 0.206 |
| shift + the correct stretch | **0.927** |

and the shift a perfect tie would require at each time:

| time (s) | required shift (ms) |
|---|---|
| 0.5 | 23.8 |
| 1.0 | 47.6 |
| 1.5 | 71.4 |
| 2.0 | 95.2 |

The required shift **grows with time** — it is not a shift at all, it is a
stretch — so no single constant can tie the log. The residual correlation of
0.21 after the best shift, against 0.93 after the correct stretch, is the
measurement that separates the two hypotheses, and it is exactly the diagnostic
to use in practice. A tie that is good at the top and poor at the bottom is a
statement about **velocity**, not about the wavelet.

For a quantitative sense of scale: a 5% velocity error is 150 m of depth error
at 3 km (§3). A tie residual of tens of milliseconds is a hundred metres of
depth, so a "cosmetic" tie is a structural error.

## 3. Time-depth conversion and the depth error from velocity error

A widely used simple form is a linear velocity gradient,

$$v(z) = v_0 + kz
\qquad\Longrightarrow\qquad
t(z) = \frac{2}{k}\ln\left(1+\frac{kz}{v_0}\right),
\qquad
z(t) = \frac{v_0}{k}\left(e^{kt/2}-1\right).$$

*Derivation.* $\mathrm{d}t = 2\,\mathrm{d}z/v(z)$, and
$\int_0^{z}\mathrm{d}z/(v_0+kz) = \ln(1+kz/v_0)/k$. Inverting gives the second
expression.

The demonstration compares the log's own time with the analytic form
($v_0 = 1800\ \mathrm{m\,s^{-1}}$, $k = 0.45\ \mathrm{s^{-1}}$):

| depth (m) | log time (s) | analytic time (s) | difference (ms) |
|---|---|---|---|
| 500 | 0.5262 | 0.5235 | 2.69 |
| 1000 | 0.9947 | 0.9917 | 2.98 |
| 2000 | 1.8045 | 1.8021 | 2.39 |
| 3000 | 2.4905 | 2.4872 | 3.27 |

The few-millisecond difference is the layering in the log, which the smooth
analytic form does not contain — small here, and larger in a real well with
thick low-velocity shales.

The **depth error** from a 5% error in each parameter:

| depth (m) | $v_0$ +5% | $v_0$ −5% | $k$ +5% | $k$ −5% |
|---|---|---|---|---|
| 1000 | +50.0 | −50.0 | +5.8 | −5.8 |
| 2000 | +100.0 | −100.0 | +21.8 | −21.5 |
| 3000 | +150.0 | −150.0 | +46.3 | −45.4 |

Two conclusions:

1. **A 5% error in $v_0$ is a 5% error in depth** — 150 m at 3 km, which is two
   orders of magnitude larger than the seismic vertical resolution (25 m). Depth
   conversion error is a *velocity* problem, and no amount of picking precision
   touches it.
2. **The gradient term matters about three times less**, because it acts
   cumulatively from the surface. Getting $v_0$ right (a check shot at shallow
   depth, or a reliable replacement velocity) is the highest-value calibration.

## 4. How much calibration is enough?

With noisy picks the answer is quantitative. The demonstration fits
$v(z) = v_0+kz$ to $n$ check-shot picks carrying a 2 ms time error, over 200
realisations, and converts the true two-way time at 3 km:

| $n$ levels | mean depth error (m) | 90th percentile (m) |
|---|---|---|
| 2 | 3.0 | 5.8 |
| 3 | 2.3 | 4.7 |
| 5 | 2.4 | 5.0 |
| 10 | 1.8 | 3.7 |
| 20 | 1.3 | 2.6 |

The improvement from 2 to 20 levels is a factor of 2.3 — real but modest. Now
change the *model form* instead: fit a straight line $t = a+bz$ to 20 noise-free
picks of the same log (whose true $t(z)$ is logarithmic). The fit gives
$t(3\ \mathrm{km}) = 2.5856$ s against the true 2.4872 s, and a depth error of
**+156.8 m**.

> **Noise is not the limiting factor. Model form is.** With the right function
> a handful of levels suffices; with the wrong function any number of levels
> gives the wrong depth.

The practical rule follows immediately: state the velocity-function form, put
VSP levels *through the interval of interest* (not just near the surface), and
show the residual of the fit rather than only the fit.

## 5. Layer-induced anisotropy: Backus averaging

A log samples rock at 0.5 m; seismic averages over ~25 m. The correct
long-wavelength equivalent of a stack of thin isotropic layers is the **Backus**
medium, which is transversely isotropic. For volume fractions $f_i$ and Lamé
parameters $\lambda_i, \mu_i$:

$$C_{33} = \left\langle \frac{1}{\lambda+2\mu} \right\rangle^{-1}, \qquad
C_{13} = C_{33}\left\langle \frac{\lambda}{\lambda+2\mu} \right\rangle,$$

$$C_{11} = \left\langle \frac{4\mu(\lambda+\mu)}{\lambda+2\mu} \right\rangle
+ C_{33}\left\langle \frac{\lambda}{\lambda+2\mu} \right\rangle^{2},$$

$$C_{44} = \left\langle \frac{1}{\mu} \right\rangle^{-1}, \qquad
C_{66} = \left\langle \mu \right\rangle, \qquad
\bar{\rho} = \left\langle \rho \right\rangle,$$

where $\langle\cdot\rangle = \sum_i f_i(\cdot)_i$ is a volume-fraction average.
Two structural facts are worth reading off before any numbers:

- $C_{33}$ is a **harmonic** ($\langle 1/M\rangle^{-1}$) type of average — the
  layers are "in series" vertically;
- $C_{11}$ is an **arithmetic** ($\langle M\rangle$) type — the layers are
  "in parallel" in the plane.

Hence $C_{11} > C_{33}$ for a layered medium, and the Thomsen parameter
$\varepsilon = (C_{11}-C_{33})/(2C_{33})$ is **positive** for layering. Fine
layering makes the horizontal P velocity the *fast* direction.

*Numbers.* Sand (40%, $v_p = 3600$, $v_s = 2100$, $\rho = 2200\
\mathrm{kg\,m^{-3}}$) and shale (60%, 2900, 1550, 2400):

| | vertical | horizontal |
|---|---|---|
| $v_p$ (m/s) | 3138.6 | 3183.6 |
| $v_s$ (m/s) | 1722.4 | 1778.8 |

$C_{11} = 23.51$, $C_{33} = 22.85$, $C_{13} = 8.80$, $C_{44} = 6.88$,
$C_{66} = 7.34$ GPa; $\bar\rho = 2320\ \mathrm{kg\,m^{-3}}$;
$\varepsilon = +0.0144$, $\delta = -0.0126$, $\gamma = +0.0332$.

**Independent check.** The vertical travel time through a stack is exactly the
sum of the layer travel times, giving an effective velocity of
$3144.6\ \mathrm{m\,s^{-1}}$ for this mixture. The Backus vertical velocity is
$3138.6\ \mathrm{m\,s^{-1}}$ — 0.19% different. That agreement is the sense in
which both numbers describe the same limit; they are not identical in general,
and the difference is what the physics of a finite stack adds to the
long-wavelength equivalent medium.

**Interpretation.** Layer-induced anisotropy is small here
($\varepsilon = 0.014$) and *not* the whole story in shale, where measured
$\varepsilon$ is typically much larger. The difference is **intrinsic**
anisotropy: clay platelets themselves are anisotropic, and aligned clay adds to
the layering effect. A depth-conversion workflow that assumes
$\varepsilon = 0$ because "the layers are isotropic" is therefore wrong even in
principle, and one that estimates $\varepsilon$ from layering alone is wrong by
a factor that depends on clay content and alignment.

## 6. Wavelet phase

A phase error is the quiet killer of ties. The demonstration rotates a 30 Hz
Ricker by $\varphi$ using the real-signal rotation
$W_{\varphi}(f) = W(f)e^{i\varphi\,\mathrm{sgn}(f)}$ and correlates the
resulting synthetic with the zero-phase one:

| phase rotation (°) | correlation | wavelet peak (ms) | wavelet trough (ms) |
|---|---|---|---|
| 0 | 1.000 | 0.0 | −13.0 |
| 15 | 0.966 | −1.0 | 12.0 |
| 30 | 0.866 | −2.0 | 11.0 |
| 45 | 0.707 | −3.0 | 10.0 |
| 60 | 0.500 | −4.0 | 8.0 |
| 90 | −0.001 | −6.0 | 6.0 |

A 90° rotation is the Hilbert transform: orthogonal to the original, so the
correlation collapses to zero *even though every event is in the right place*.
And the lobe an interpreter picks moves: the trough goes from −13.0 ms to
+6.0 ms, a **19 ms** change, which at 3150 m/s is **30 m** of depth.

So a phase error has three consequences at once: it destroys the tie
correlation, it moves picked horizons, and it biases every amplitude-based
quantity — inversion, AVO gradients and impedance maps alike
([11-03-04](04-seismic-inversion-reservoir.md)). Phase must be estimated
(statistically from the data, or from a VSP) and **stated**; it must not be
assumed.

## 7. Worked example — a complete tie and depth conversion

**Statement.** A well is logged to 3 km. The check shots are sparse; you
propose a $v(z) = v_0+kz$ form. The synthetic correlates at 0.55 without a
shift and 0.78 with a +12 ms constant shift, but the correlation to the deeper
half of the log stays near 0.4. The target is at 2.5 km.

1. **Diagnose the tie.** A correlation that improves with a constant shift at
   the top and does not improve at the bottom is the signature of a velocity
   (stretch) error, not of a wavelet problem (§2). A 5% velocity error is
   125 m of depth at 2.5 km.
2. **Fix the model, not the shift.** Fit $v_0$ and $k$ to the check shots.
   With 5 levels and 2 ms picking, the demonstration's error budget is ~2.4 m
   at 3 km; the fit is not the limiting factor.
3. **Check the form.** If the check shots span only the top 800 m and the
   target is at 2500 m, the form is being extrapolated over 1700 m. A
   straight-line time-depth assumption in that situation costs ~157 m at 3 km
   (§4).
4. **Quantify.** Report the depth with the velocity uncertainty, not with the
   seismic resolution: $2.5\ \mathrm{km}\pm 5\%$ from velocity, versus ±25 m
   from seismic bandwidth.
5. **Upscale correctly.** For the impedance background used by inversion,
   Backus-average the log rather than boxcar-smoothing it: the effective medium
   is anisotropic, and the vertical velocity is a harmonic-type average
   (§5).

## 8. Assumptions and regime of validity

1. **The logs are calibrated.** An uncalibrated sonic produces a systematic
   depth error that no tie can repair; density errors show up as amplitude
   errors.
2. **The reflectivity is computed at the right scale.** Sampling a log densely
   and convolving produces a synthetic dominated by the log's high-frequency
   detail, which the seismic does not contain; the log must be upscaled to the
   seismic band (Backus, or a band-limited equivalent) before comparison.
3. **$r = (Z_2-Z_1)/(Z_2+Z_1)$ assumes normal incidence and no tuning.**
   Offset-dependent reflectivity belongs to AVO
   ([06-09-05](../../06-seismology/09-reflection-seismology/05-amplitude-vs-offset.md)).
4. **The velocity function form is a choice.** $v_0+kz$ is convenient and
   often adequate; the error from the wrong form exceeds the error from sparse
   picks (§4).
5. **Backus averaging assumes long wavelengths compared with layer thickness,
   no intrinsic anisotropy, and isotropic layers.** Where the layers are
   anisotropic themselves, the Backus result is a lower bound on the total
   anisotropy.
6. **The wavelet is stationary and its phase is known.** Both are commonly
   false; both must be tested (§6).
7. **A tie at one well does not transfer laterally.** Wavelet, velocity and
   facies all vary; a tie is evidence for a model, and the model must be
   re-checked at every subsequent well.

## 9. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| velocity | $v$ | m s⁻¹ | |
| gradient | $k$ | s⁻¹ | $v$ in m/s divided by $z$ in m |
| two-way time | $t$ | s | $2\int\mathrm{d}z/v$ |
| reflectivity | $r$ | 1 | ratio of impedances |
| stiffness | $C_{ij}$ | Pa | $\rho v^2$ |
| Thomsen parameters | | 1 | ratios of stiffnesses |
| depth error | | m | (m/s)/(m/s) × m |

Note $k$ has units of s⁻¹: if your gradient is in "m/s per km" it must be
converted (a value of 0.45 s⁻¹ is 0.45 m/s per metre, i.e. 450 m/s per km).

## 10. Python demonstration

`code/borehole_and_integration_demo.py` prints:

1. the log statistics, the reflectivity, and the synthetic seismogram;
2. the tie correlations for no tie, a bulk shift and a shift plus stretch, with
   the shift required at four times;
3. the log-versus-analytic time comparison and the depth error from
   $\pm5\%$ errors in $v_0$ and $k$;
4. the calibration experiment with 2–20 noisy levels, and the error from a
   straight-line model form;
5. the Backus equivalent medium, the Thomsen parameters, and the check against
   the travel-time average;
6. the phase-rotation table with the picked-lobe displacement in ms and metres.

It is print-only, seeded with `np.random.default_rng(20261014)` and exits 0.

## 11. Exercises

- [`exercises/06-borehole-and-integration-exercises.md`](exercises/06-borehole-and-integration-exercises.md)
- [`exercises/06-borehole-and-integration-solutions.md`](exercises/06-borehole-and-integration-solutions.md)

## Mastery checkpoint

> A well is logged to 3 km with check shots every 500 m. **(a)** Write the
> two-way time for $v(z) = v_0+kz$ and evaluate it for
> $v_0 = 1900\ \mathrm{m\,s^{-1}}$, $k = 0.4\ \mathrm{s^{-1}}$ at 2 km.
> **(b)** The analyst assumes $v_0 = 2000\ \mathrm{m\,s^{-1}}$ with the same
> $k$: compute the depth error at 2 km. **(c)** The tie requires a shift of
> 20 ms at 1 s and 44 ms at 2 s: state the diagnosis and the approximate
> velocity error. **(d)** A 30° phase error is discovered after inversion:
> state the two artefacts it produces and their approximate sizes, using the
> table of §6.

## Common pitfalls

1. **Tying a log with a constant shift when the error is a stretch.** The
   required shift grows linearly with time under a velocity error.
2. **Reporting a depth without the velocity-function form.** The form's error
   can exceed the noise's by two orders of magnitude.
3. **Fitting more levels instead of fixing the form.** Twenty levels of the
   wrong function still give 157 m at 3 km.
4. **Convolving a raw 0.5 m log with a 30 Hz wavelet.** The synthetic is then
   dominated by detail the seismic cannot contain; upscale first.
5. **Assuming zero-phase.** A 90° error nulls the tie correlation while leaving
   event positions intact.
6. **Assuming layering gives all the anisotropy.** Intrinsic clay anisotropy
   adds to it, often dominating.
7. **Extrapolating a tie laterally.** The model is validated at one location.

## Related modules

- [05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md) —
  the measurements being tied: sonic, density, VSP, imaging.
- [11-03-01 Reflection Seismic in Exploration](01-seismic-in-exploration.md) —
  the acquisition that the tie relates to.
- [11-03-04 Seismic Inversion for Reservoir Properties](04-seismic-inversion-reservoir.md) —
  the workflow that consumes the wavelet and the low-frequency model a tie
  provides.
- [05-07 Interpretation and Integration](../../05-core-geophysics/07-interpretation-and-integration/README.md) —
  ground truthing and reporting with honest uncertainty.
- [05-04-02 Effective-Medium Theories](../../05-core-geophysics/04-rock-physics/02-effective-medium-theory.md) —
  the theory behind Backus averaging.

## Further reading

- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Synthetic seismograms and
  time-depth relations.
- Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists. Level: reference. Wavelet estimation, well ties and the
  time-to-depth conversion workflow.
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook.
  Borehole geophysics and its integration with surface data.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
