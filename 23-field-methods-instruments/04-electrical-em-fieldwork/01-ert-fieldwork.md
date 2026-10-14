---
id: 23-04-01
title: "ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity"
level: graduate
prereqs: ["09-02-05", "23-01-03"]
estimated_minutes: 100
tags: [ert, resistivity, fieldwork, electrodes, contact-resistance, reciprocity]
---

# ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the geometric factor of a four-electrode array from its electrode
   positions, and **verify** it against the closed-form expression for the Wenner,
   Schlumberger and dipole-dipole arrays.
2. **Compute** an apparent resistivity from a measured voltage and current, and
   **propagate** the two relative errors into the result.
3. **Compute** the loop resistance, injected current and signal level of an array,
   and **state** what a poor electrode contact costs.
4. **Compute** the reciprocal-measurement tolerance and **use** it as a
   quality-control test.
5. **Compute** the number of configurations an electrode spread allows and
   **explain** why a field protocol measures a tiny fraction of them.
6. **Design** an electrode layout for a stated target depth, and **state** the
   layout, contact and reciprocity checks that verify it in the field.

All electrode spacings, resistances, compliance limits and measured values in this
lesson are **SYNTHETIC** teaching values printed by the demonstration. No field
measurement, instrument specification or commercial protocol is used or reproduced.

## Prerequisites

- [09-02-05 Electrical Resistivity Tomography (ERT) Acquisition and Design](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) —
  the method this lesson equips in the field.
- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record of electrode positions and readings.

## 1. Intuition: the electrode layout is the measurement

A direct-current resistivity measurement injects a current between two electrodes
and measures the resulting potential difference between two others. Everything
about the resulting apparent resistivity — its value, its depth sensitivity, its
noise level — follows from **where the four electrodes are**. There is no
processing that recovers a measurement the layout did not make.

Three quantities therefore have to be controlled in the field, and each is
computable in advance:

- **The geometric factor $K$** — a pure function of the four positions, which
  converts a voltage and a current into a resistivity.
- **The contact resistance** — which sets how much current can be injected through
  a voltage-limited transmitter, and therefore how large the measured signal is.
- **The reciprocity** — whether the array is behaving as a linear, passive system,
  which is a check on cables, electrodes and geometry rather than on the ground.

## 2. The four-electrode formula

For electrodes at positions $A$, $B$ (current) and $M$, $N$ (potential), the
potential difference produced by a current $I$ in a homogeneous half-space of
resistivity $\rho$ is

$$\Delta V = \frac{\rho I}{2\pi}
\left(\frac{1}{AM} - \frac{1}{BM} - \frac{1}{AN} + \frac{1}{BN}\right),$$

so that with the **geometric factor**

$$K = \frac{2\pi}{\dfrac{1}{AM} - \dfrac{1}{BM} - \dfrac{1}{AN} + \dfrac{1}{BN}}
\qquad\text{and}\qquad \rho_a = K\frac{\Delta V}{I},$$

the same formula defines the **apparent resistivity** $\rho_a$ for any array on any
ground. This single expression is the whole of the array algebra; the named arrays
are special cases. The demonstration evaluates it for three of them:

| Array | Geometry | $K$ (m) | Closed form | Closed-form value |
|---|---|---|---|---|
| Wenner | $a = 5$ m | 31.4159 | $2\pi a$ | 31.4159 |
| Schlumberger | $L = 50$ m, $b = 5$ m | 777.5442 | $\pi(L^{2}-b^{2})/(2b)$ | 777.5442 |
| Dipole-dipole, $n = 1$ | $a = 5$ m | 94.2478 | $\pi n(n+1)(n+2)a$ | 94.2478 |
| Dipole-dipole, $n = 3$ | $a = 5$ m | 942.4778 | $\pi n(n+1)(n+2)a$ | 942.4778 |
| Dipole-dipole, $n = 6$ | $a = 5$ m | 5277.8757 | $\pi n(n+1)(n+2)a$ | 5277.8757 |

Two practical observations. First, **$K$ grows rapidly with the separation
between the current and potential dipoles**: from 94 to 5278 m between $n = 1$ and
$n = 6$, a factor of 56. Since $\rho_a = K\Delta V/I$, the measured voltage for a
given ground resistivity falls by the same factor: the far separations are the
weak-signal measurements, which is why they are the noisiest part of an ERT
section and why a robust inversion is needed for a large $n$ range. Second, **the
closed forms are checks, not definitions.** Implementing the exact formula from
positions removes any ambiguity about whether $L$, $b$ or $a$ is a full or a half
separation — an ambiguity that has produced wrong resistivity values in more than
one survey. Compare the computed $K$ against the closed form before every campaign.

## 3. Apparent resistivity and its error

With $K = 31.4159$ m, $\Delta V = 12.50$ mV and $I = 5.0$ mA, the demonstration
reports

$$\rho_a = K\frac{\Delta V}{I} = 31.4159 \times \frac{12.5\times10^{-3}}{5.0\times10^{-3}}
= 31.4159 \times 2.5 = 78.5398\ \Omega\,\mathrm{m}.$$

The measurement has two independent relative errors, and they add in quadrature:

$$\frac{\delta \rho_a}{\rho_a}
= \sqrt{\left(\frac{\delta V}{V}\right)^{2}
+ \left(\frac{\delta I}{I}\right)^{2}} .$$

| Voltage error | Current error | $\rho_a$ error |
|---|---|---|
| 1.0 % | 0.5 % | 1.118 % |
| 2.0 % | 1.0 % | 2.236 % |
| 5.0 % | 2.0 % | 5.385 % |

The number that matters for inversion is not the relative error of a single
measurement but the **error model** that is supplied with the data. Most inversion
codes accept either a percentage error or a voltage-dependent error; stating which,
and quoting the two components separately, is what lets a reader judge whether a
feature in the model is supported by the data. A 5.4 % error bar on every reading
limits what an inversion can resolve: the noise floor of the model is roughly the
error bar, so resistivity contrasts smaller than that are not recoverable, whatever
the colour scale shows.

## 4. Contact resistance and the injected current

The current that a transmitter can inject is limited by its compliance $V_{\max}$
and by the total **loop resistance**

$$R_{\text{loop}} = R_A + R_B + R_{\text{ground}},$$

in which the two contact resistances usually dominate. For a voltage-limited
transmitter, $I = V_{\max}/R_{\text{loop}}$, so with $V_{\max} = 100$ V:

| Contact resistance (Ω) | Loop resistance (Ω) | $I$ (mA) | $\Delta V$ (mV) | Relative signal (dB) |
|---|---|---|---|---|
| 200 | 450 | 222.222 | 555.5556 | 0.0 |
| 1000 | 2050 | 48.780 | 121.9512 | −13.2 |
| 5000 | 10050 | 9.950 | 24.8756 | −27.0 |
| 20000 | 40050 | 2.497 | 6.2422 | −39.0 |
| 100000 | 200050 | 0.500 | 1.2497 | −53.0 |

The lesson is the last column: a 100 kΩ contact against a 200 Ω contact costs
**53 dB** of signal, because the signal is inversely proportional to the loop
resistance. Improving a contact is therefore a data-quality action, not a
convenience:

- **Water or brine** the electrode hole, or use a bentonite or clay slurry in dry
  or sandy ground.
- **Drive the electrode deeper** through the dry, high-resistivity surface layer
  into moist material.
- **Use more electrodes in parallel** at each station, which divides the contact
  resistance.
- **Measure the contact resistance** at every electrode before starting, and record
  it. A reading of tens of kilo-ohms is a warning; a reading above the transmitter's
  limit means no measurement at all at that position.

Note also what the table does *not* say: it does not model the receiver noise floor,
so the last column is the signal relative to the best contact, not a
signal-to-noise ratio. A large loop resistance hurts twice — less signal *and* more
electrical noise coupled into the cables — which is why the field check is to look
at the measured voltage quality, not only at the contact resistance.

## 5. Reciprocity as a field test

Electromagnetically, a four-electrode array is a linear passive network, so
**swapping the current and potential pairs must give the same apparent
resistivity**:

$$\rho_a(A,B;M,N) = \rho_a(M,N;A,B).$$

To within noise, that is a free check on the array: it is independent of the ground,
so any disagreement beyond the noise indicates a problem with the *system* — a
cable fault, a poor electrode contact that changed between the two measurements, a
geometry error (an electrode in the wrong place), or a non-linear coupling at an
electrode. The tolerance follows from the two voltage errors:

$$\frac{\delta\rho_a}{\rho_a}\bigg|_{\text{reciprocal}}
= \sqrt{2}\,\frac{\delta V}{V},$$

so 1 % voltage noise gives a 1.414 % tolerance, 2 % gives 2.828 %, 5 % gives
7.071 % and 10 % gives 14.142 % (the demonstration's table). The practice is to
check a subset — a few per cent of the measurements — and to require the
disagreement to be within the stated factor. A reciprocal difference that exceeds
the tolerance by several times is a defect to find, not noise to average.

## 6. Data density and the shape of a protocol

A spread of $n$ electrodes allows $\binom{n}{4}$ distinct four-electrode
configurations:

| Electrodes | Configurations | A typical protocol measures | Fraction of the space |
|---|---|---|---|
| 24 | 10 626 | ~480 | 4.52 % |
| 48 | 194 580 | ~960 | 0.49 % |
| 96 | 3 321 960 | ~1 920 | 0.06 % |

The configuration count grows as $n^{4}$ while the electrode count grows as $n$: a
protocol is a *choice* of a few thousand configurations out of millions, and that
choice is what determines the depth coverage, the resolution and the acquisition
time. The three families of choice are:

1. **Depth coverage** — the largest current–potential separation sets the deepest
   information; the smallest sets the shallowest. The depth of investigation grows
   roughly with the separation, and the factor relating them is array-dependent
   (for the Wenner array the median depth is conventionally about half the spacing
   $a$), so establish it by modelling the specific problem rather than assuming a
   factor.
2. **Resolution** — the number of configurations sampling each depth interval
   determines how well a layer at that depth is resolved.
3. **Time** — acquisition time is proportional to the number of configurations,
   and each configuration requires the transmitter to switch, settle and measure.
   A doubling of the protocol doubles the field time.

The practical design loop is therefore: choose the electrode spacing from the
target depth, choose the number of electrodes from the target area and the access,
choose a standard protocol that covers the depth range of interest at adequate
resolution, and *then* check the data density against the inversion's requirements.

## 7. Assumptions and regime of validity

1. **A homogeneous half-space** underlies the definition of $\rho_a$. The value is
   an average over the volume the array senses, not a property of any layer, and it
   is what the inversion interprets.
2. **The four-electrode formula assumes point electrodes on a flat surface.** Real
   electrodes have a length and a radius, the surface is not flat, and on a steep
   slope the geometry must be measured in three dimensions; the errors matter at
   short spacings.
3. **A voltage-limited transmitter.** A current-limited transmitter keeps $I$
   constant and the analysis changes; state the instrument's mode.
4. **Linear, passive, reciprocal behaviour.** Non-linear coupling at an electrode
   (a corroded stake, an electrode in contact with a metallic object) breaks it, and
   that is exactly what the reciprocity test detects.
5. **Independent voltage and current errors.** A systematic gain error in the
   receiver affects every measurement coherently and does not average out; it must
   be calibrated, not estimated from repeats.
6. **The electrode positions are the ones recorded.** A 10 % error in a separation
   changes $K$ by a comparable amount at short spacings; positions must be measured,
   not paced.

## 8. The honest summary

- $K$ follows from the four electrode positions; the closed forms are checks.
- $K$ grew from 94 to 5278 m over $n = 1$ to 6 in the dipole-dipole array, so the
  far separations are the weak-signal measurements.
- The apparent resistivity error is the quadrature sum of the voltage and current
  errors: 5 % and 2 % give 5.4 %.
- A 100 kΩ contact costs 53 dB of signal against a 200 Ω contact at a
  voltage-limited transmitter.
- Reciprocity is a free system test with a $\sqrt{2}\,\delta V/V$ tolerance.
- A protocol measures under 1 % of the configurations a 48-electrode spread allows.

## 9. Python demonstration

[`code/ert_fieldwork_demo.py`](./code/ert_fieldwork_demo.py) prints every number
quoted above. It:

1. evaluates the exact geometric-factor formula for the Wenner, Schlumberger and
   dipole-dipole arrays and compares each with its closed form;
2. computes an apparent resistivity and its error for three voltage/current error
   pairs;
3. tabulates loop resistance, injected current, measured voltage and relative
   signal for five contact resistances;
4. computes the reciprocal tolerance for four voltage errors;
5. counts the configurations available to 24, 48 and 96 electrodes.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/04-electrical-em-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_fieldwork_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/01-ert-fieldwork-exercises.md`](./exercises/01-ert-fieldwork-exercises.md)
and
[`exercises/01-ert-fieldwork-solutions.md`](./exercises/01-ert-fieldwork-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. Compute $K$ for a Wenner array with $a = 10$ m, both from the closed form and
   by reasoning about the electrode positions.
2. An apparent resistivity is 120 Ω·m from $\Delta V = 20$ mV and $I = 4$ mA.
   Compute $K$, and the resistivity error for a 3 % voltage and a 1 % current error.
3. A transmitter has 200 V compliance and a ground resistance of 30 Ω. Compute the
   injected current for contact resistances of 500 Ω and 50 kΩ, and the ratio of
   the two signals in dB.
4. State the reciprocity tolerance for a 4 % voltage error, and one defect it would
   reveal.
5. State how many configurations a 32-electrode spread allows.

## 12. Common pitfalls

1. **Confusing full and half separations** in the closed-form expressions. Compute
   $K$ from positions.
2. **Pacing the electrode positions.** A 10 % separation error is a 10 % $K$ error.
3. **Ignoring poor contacts.** They cost signal and add noise; measure the contact
   resistance at every electrode.
4. **Averaging a reciprocity failure away.** It is a system defect.
5. **Assuming the inversion removes the noise.** It cannot recover resolution the
   error bars do not support.
6. **Designing the protocol before the target depth.** The largest separation sets
   the deepest information.
7. **Forgetting the receiver's own gain error.** It is a systematic term that
   repeats never reveal.

## 13. Where this is used

- Hydrogeological and environmental surveys: aquifer geometry, salinity,
  contaminant plumes and landfill boundaries.
- Engineering and geotechnical work: depth to bedrock, voids, foundations.
- Archaeology and forensics, where the layout is chosen to fit the site rather than
  the target.
- Time-lapse monitoring, where the *repeatability* of the electrode positions and
  contacts becomes the limiting factor.
- Any ERT dataset archived for reuse: the electrode positions and contact
  resistances belong in the metadata.

## 14. Related lessons

- [02 EM Fieldwork: Loop, Coil and Grounded-Source Configurations](02-em-fieldwork.md) —
  the inductive counterpart of the galvanic array.
- [04 GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration](04-gpr-fieldwork.md) —
  the high-frequency electromagnetic method at the same sites.
- [05 Borehole Logging Operations and Tool Calibration](05-borehole-fieldwork.md) —
  depth control and tool response.
- [23-03-04 Field Data QC for Potential-Field Surveys](../03-gravity-magnetic-fieldwork/04-field-data-qc-gravmag.md) —
  the general QC framework these checks instantiate.
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](../../09-electrical-em-methods/02-dc-resistivity/07-resistivity-inversion.md) —
  what the error model becomes in the inversion.

## 15. Self-assessment checklist

- [ ] I can compute $K$ from electrode positions and check it against a closed form.
- [ ] I can compute an apparent resistivity and its relative error.
- [ ] I can compute the injected current from the loop resistance.
- [ ] I can state and use the reciprocity tolerance.
- [ ] I can count the configurations of a spread and explain the protocol choice.
- [ ] I can design a layout for a stated target depth.
