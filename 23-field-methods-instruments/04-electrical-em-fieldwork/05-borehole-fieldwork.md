---
id: 23-04-05
title: "Borehole Logging Operations and Tool Calibration"
level: graduate
prereqs: ["05-08-01", "23-04-01"]
estimated_minutes: 100
tags: [borehole, logging, calibration, depth-control, resolution, wireline]
---

# Borehole Logging Operations and Tool Calibration

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the elastic stretch of a wireline cable and the depth error it
   produces, and **state** how the correction changes with the tool.
2. **Compute** the response of a finite-length detector to a thin bed, and **state**
   what is lost and what is not recoverable.
3. **Compute** the logging speed a depth-sampling interval requires, and the rig
   time it costs.
4. **Calibrate** a log with a two-point calibration and **state** what limits its
   accuracy.
5. **Compute** a run-to-run depth shift and its residual scatter, and **state** what
   each of the two numbers means.
6. **Design** a logging programme for a stated target, and **state** the depth
   control, calibration and repeat checks it needs.

All tool weights, cable properties, logging speeds, detector lengths and calibration
readings in this lesson are **SYNTHETIC** teaching values, combined with the
standard relations quoted in the text. No field log, tool specification or
manufacturer figure is used or reproduced.

## Prerequisites

- [01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](01-ert-fieldwork.md) —
  the surface electrical methods that borehole logs calibrate.
- [05-08-01 The Borehole Environment and Invasion Profiles](../../05-core-geophysics/08-geophysical-logging/01-borehole-environment.md) —
  what a logging tool is measuring.

## 1. Intuition: in a borehole the depth is as uncertain as the measurement

A wireline log is a measurement of a physical property *as a function of depth*. Two
things can go wrong with the depth axis alone, and both are large compared with the
features being resolved:

- **The cable stretches.** A tool hanging on kilometres of cable elongates it
  elastically, so the tool is *deeper* than the cable payout indicates by an amount
  that depends on the tool's weight, the cable's section and modulus, and the depth.
- **The depth reference drifts between runs.** Different tools, different cable
  tensions and different logging directions give slightly different depth scales,
  so the same feature appears at different depths in two runs.

Both are systematic and correctable, up to the point where they are not — which is
why depth control is a first-class part of a logging programme, not an
administrative detail.

## 2. Cable stretch

A cable of cross-section $A$, elastic modulus $E$ supporting a tool of weight $W$ at
depth $L$ elongates by

$$\Delta L = \frac{W L}{A E},$$

with the cable's own weight adding a term of order $wL^{2}/(2AE)$ for a cable of
weight per unit length $w$. The demonstration's values, for a 10 mm² cable with
$E = 1.1\times10^{11}$ Pa:

| Tool weight (N) | Depth 1000 m | Depth 2000 m |
|---|---|---|
| 250 | 0.2273 m (4.5 samples) | 0.4545 m (9.1 samples) |
| 500 | 0.4545 m (9.1) | 0.9091 m (18.2) |
| 1000 | 0.9091 m (18.2) | 1.8182 m (36.4) |
| 2000 | 1.8182 m (36.4) | 3.6364 m (72.7) |

(The last column counts 0.05 m depth-sampling intervals.) Three consequences:

1. **The error is linear in both depth and tool weight**, so it is exactly the kind
   of systematic error that has to be removed by a depth correction rather than
   averaged away.
2. **The correction changes with the tool**, so a depth-shifted log is not transferable
   between runs without recomputing the stretch.
3. **The stretch is comparable to the target scale.** A 0.91 m stretch at 2000 m is
   larger than many beds of interest, and tens of sampling intervals long.

The practical depth-control measures, in order of reliability:

1. **Log the same hole up and down** and use the *up* pass for the depth scale
   (cable stretch affects the two directions oppositely, and the average cancels
   much of the tension-dependent error).
2. **Include a natural gamma or casing-collar locator** in every run: casing collars
   and other fixed features provide markers for the run-to-run matching of
   Section 5.
3. **Record the tool weight, cable tension and logging speed** with the log, so the
   correction can be recomputed later.
4. **Use a depth encoder at the sheave wheel** with its calibration recorded, plus a
   known cable-mark check before and after the run.

## 3. Tool response and thin beds

A logging tool measures an average over its detector length $L$ (a scintillation
detector, a pair of receiver coils, an electrode array). The response to a bed of
thickness $b$ is a convolution of the bed with the detector's window, so for
$b < L$ the **peak response is $b/L$** while the **apparent thickness is the
detector length**:

| Bed (m) | Peak response | Apparent thickness (m) |
|---|---|---|
| 0.05 | 0.100 | 0.50 |
| 0.10 | 0.200 | 0.50 |
| 0.20 | 0.400 | 0.50 |
| 0.35 | 0.700 | 0.50 |
| 0.50 | 1.000 | 0.50 |
| 1.00 | 1.000 | 0.50 |

The lesson is that **the thickness is lost, not merely blurred**: every bed thinner
than the detector is reported as the same 0.50 m apparent thickness with an
amplitude proportional to the true thickness. A deconvolution can recover *a*
thickness–amplitude pair, but with a 0.5 m detector and a 5 cm bed the recovered
thickness is uncertain by the ratio of the noise to the signal — which is why thin
beds are quantified from amplitude (which is proportional to thickness times
contrast) with the detector length stated, rather than from the apparent thickness.

## 4. Depth sampling and logging speed

The depth sampling interval is the logging speed divided by the tool's sample rate:

$$\Delta z = \frac{v_{\text{log}}}{f_s} .$$

At 20 samples per second the demonstration's table:

| Sampling (m) | Speed (m/s) | Speed (m/h) | Time for 2000 m (min) |
|---|---|---|---|
| 0.02 | 0.400 | 1440 | 83.3 |
| 0.05 | 1.000 | 3600 | 33.3 |
| 0.10 | 2.000 | 7200 | 16.7 |
| 0.20 | 4.000 | 14400 | 8.3 |

The trade is explicit: finer sampling means slow logging means rig time — the
dominant cost in a logging programme. The design rule is to choose the sampling no
finer than what the *tool's* resolution supports: sampling a 0.5 m detector at 0.02 m
records the same information five times more often, and multiplies the acquisition
time by five for nothing. State the detector length with the sampling interval.

## 5. Calibration

A two-point calibration fixes the gain and offset of a log against two known values:

$$g = \frac{V_2 - V_1}{R_2 - R_1}, \qquad o = V_1 - g R_1 .$$

With raw readings 1200 and 8200 corresponding to values 10.0 and 90.0, the
demonstration reports

$$g = \frac{90.0 - 10.0}{8200 - 1200} = \frac{80.0}{7000} = 0.011429
\ \text{value units per count},$$

$$o = 10.0 - 0.011429 \times 1200 = -3.7143\ \text{value units},$$

and the check returns $0.011429 \times 1200 - 3.7143 = 10.0$ and
$0.011429 \times 8200 - 3.7143 = 90.0$ ✔.

The calibration is only as good as the two reference values: if each is known to
±2 %, the gain is uncertain by about ±3 % and the offset correspondingly. In
practice the references are a **primary standard** (a calibration facility or a
reference formation) and a **field check** (a portable source, a jig, or a repeat
of a previous calibration), and the log's *scale* uncertainty is quoted from the
first and its *stability* from the second. What the calibration cannot fix is a
non-linearity between the two points: a tool that is linear over its range is
assumed, and checking that assumption requires a third point.

## 6. Depth matching between runs

Two runs of the same hole rarely give exactly the same depth for the same feature.
Picking $n$ markers on both runs gives a set of shifts whose **mean is a correctable
offset** and whose **scatter about the mean is not**:

| Quantity | Value (20 markers, true shift 0.60 m, picking scatter 0.08 m) |
|---|---|
| fitted shift | 0.5848 m |
| residual scatter | 0.0936 m |
| standard error of the fitted shift | 0.0209 m |
| markers deviating by more than 0.20 m | 0 of 20 |

Two rules follow. First, **report both numbers**: the shift is applied, the scatter
is a quality statement about the matching — a scatter of 0.09 m on a true picking
noise of 0.08 m means the markers are identified consistently, whereas a scatter of
0.5 m would mean they are being matched to the wrong features. Second, **check for
outliers before fitting**: a single wrongly matched marker in 20 shifts the mean by
1/20 of its error, and the standard diagnostic is to fit, remove markers beyond
about three standard deviations, refit, and report how many were removed.

## 7. Assumptions and regime of validity

1. **Elastic stretch only.** The cable also creeps, has a constructional stretch that
   is not recovered, and expands thermally; the elastic term is the largest and the
   one that can be computed.
2. **A known tool weight in the hole.** The weight in fluid is the air weight less
   the buoyancy, and it changes with the tool, the fluid and the depth; the value
   used in the correction must be recorded.
3. **A linear detector response.** Real tools have a response function that is not a
   boxcar (a two-coil induction tool has a more complex geometric factor), so the
   boxcar table is a scaling argument.
4. **A linear calibration.** Established by the two reference values and assumed
   between them; a third point tests it.
5. **Marker identification is correct.** The largest error in depth matching is a
   mis-identified marker, not the picking precision.
6. **The hole does not change between runs.** Borehole conditions (washouts, mud
   cake, swelling clays) change between runs and produce apparent depth shifts that
   are not depth errors at all — the diagnostic is that they do not appear on
   independent curves.

## 8. The honest summary

- Elastic stretch is $WL/(AE)$: 0.91 m for a 500 N tool at 2000 m on a 10 mm² cable,
  and it scales with the tool weight.
- A bed thinner than the detector is reported at the detector's apparent thickness
  with amplitude $b/L$: thickness is lost, not blurred.
- Sampling is speed/sample rate: 0.05 m at 20 samples/s is 3600 m/h.
- A two-point calibration is only as good as its two references.
- Run-to-run depth matching gives a correctable shift and an uncorrectable scatter;
  report both.

## 9. Python demonstration

[`code/borehole_logging_demo.py`](./code/borehole_logging_demo.py) prints every
number quoted above. It:

1. computes cable stretch for four tool weights and two depths;
2. tabulates the boxcar response of a 0.5 m detector to six bed thicknesses;
3. converts four depth-sampling intervals into logging speeds and rig times;
4. performs a two-point calibration and verifies it;
5. fits a depth shift from 20 synthetic marker picks and reports the residual.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/04-electrical-em-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_logging_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/05-borehole-fieldwork-exercises.md`](./exercises/05-borehole-fieldwork-exercises.md)
and
[`exercises/05-borehole-fieldwork-solutions.md`](./exercises/05-borehole-fieldwork-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. Compute the elastic stretch for a 750 N tool at 3000 m on a cable of 12 mm²
   section and $E = 1.1\times10^{11}$ Pa.
2. A 0.6 m detector logs a 0.15 m bed. Compute the peak response and the apparent
   thickness.
3. A tool samples at 50 samples/s and the target sampling is 0.02 m. Compute the
   logging speed and the time for a 1500 m hole.
4. Two calibration readings are 500 → 5.0 and 4500 → 45.0. Compute the gain, the
   offset and the value of a raw reading of 2000.
5. State which part of a depth-matching result is correctable and which is not.

## 12. Common pitfalls

1. **Ignoring cable stretch.** It reaches metres at depth and changes with the tool.
2. **Using the down pass for the depth scale.** The up pass is preferred.
3. **Over-sampling relative to the detector.** It costs rig time and adds nothing.
4. **Quoting a thin bed's thickness from its apparent extent.** The amplitude
   carries the thickness information, and only with a stated detector length.
5. **A two-point calibration treated as a linearity proof.** It assumes linearity.
6. **Fitting a depth shift with an outlier present.** One bad marker in 20 moves the
   mean.
7. **Forgetting to record the tool weight, tension and speed.** The correction
   cannot be recomputed.

## 13. Where this is used

- Open-hole petrophysical logging: gamma, resistivity, density, neutron, sonic and
  imaging tools, all of which need depth control and calibration.
- Cased-hole and production logging, where the depth reference is the completion
  string and the casing collars are the markers.
- Borehole geophysics for mining and geotechnical work: sonic, density, IP and
  imaging for rock-mass characterisation.
- Vertical seismic profiling, where the depth of each receiver level is itself a
  measurement that has to be tied to the surface seismic.
- Any log that will be compared with core, with another log, or with a surface
  survey: the depth scale is the common axis, and it must be established.

## 14. Related lessons

- [01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](01-ert-fieldwork.md) —
  the surface counterpart, and the calibration of a borehole-to-surface dataset.
- [04 GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration](04-gpr-fieldwork.md) —
  another depth-conversion problem, in the shallow subsurface.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](../../05-core-geophysics/08-geophysical-logging/07-log-interpretation.md) —
  what the calibrated log becomes.
- [05-08-06 Vertical Seismic Profiling and Check Shots](../../05-core-geophysics/08-geophysical-logging/06-seismic-while-drilling.md) —
  where the depth tie to surface seismic is made.
- [23-05-04 Calibration, Testing and Traceability](../05-instrumentation-and-electronics/04-calibration-and-testing.md) —
  the general calibration framework.

## 15. Self-assessment checklist

- [ ] I can compute a cable stretch and its depth error.
- [ ] I can compute a thin-bed response for a stated detector length.
- [ ] I can convert a sampling interval into a logging speed and a rig time.
- [ ] I can perform and check a two-point calibration.
- [ ] I can fit a run-to-run depth shift and report its scatter.
- [ ] I can design the depth-control and calibration elements of a logging programme.
