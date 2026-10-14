---
id: 23-04-03
title: "Magnetotelluric Fieldwork: Sites, Remote Reference, Noise"
level: research
prereqs: ["08-04-02", "23-04-02"]
estimated_minutes: 110
tags: [magnetotellurics, fieldwork, remote-reference, coherence, dead-band, noise]
---

# Magnetotelluric Fieldwork: Sites, Remote Reference, Noise

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the impedance magnitude and the telluric field produced by a stated magnetic signal, and **convert** between impedance, apparent resistivity and phase.
2. **Compute** the coherence required for a stated impedance accuracy from a stated number of independent estimates.
3. **Compute** the recording time a weaker signal band requires, and **state** the quantitative content of the MT dead band.
4. **Choose** a telluric dipole length from the expected field and the electrode noise floor.
5. **Compute** the bias a coherent local noise source produces, and **state** what a remote reference removes.
6. **Size** a site's footprint and cable budget, and **state** the layout rules that keep the electric and magnetic sensors independent.

All resistivities, dipole lengths, noise levels, coherences and recording times in
this lesson are **SYNTHETIC** teaching values, combined with the standard
magnetotelluric relations quoted in the text. No field dataset, instrument
specification or published MT response is used or reproduced.

## Prerequisites

- [02 EM Fieldwork: Loop, Coil and Grounded-Source Configurations](02-em-fieldwork.md) —
  the controlled-source counterpart of the same physics.
- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the method this lesson equips in the field.

## 1. Intuition: an MT site measures a ratio, and the ratio is fragile

A magnetotelluric site measures the horizontal electric field (from two orthogonal
telluric dipoles) and the horizontal magnetic field (from three magnetic sensors),
and forms the **impedance**

$$\mathbf{E} = \mathbf{Z}\,\mathbf{H}, \qquad
\rho_a = \frac{|\mathbf{Z}|^{2}}{\omega \mu_0}, \qquad
\phi = \arg \mathbf{Z} .$$

Because it is a *ratio*, anything that contaminates both fields in a common way
cancels, and anything that contaminates one field only does not. The whole of MT
field practice follows from that observation:

- **Coherent noise in one field biases the impedance.** A coherent noise source
  (a power line, a pipeline, an industrial plant) can couple into both the electric
  and the magnetic channels in a correlated way, and the bias can be severe.
- **A remote reference** — a second magnetic sensor far enough away to see the
  natural field but not the local noise — removes the part of the bias that is
  caused by noise coherent between the *local* E and H but not present at the
  remote site.
- **Coherence is the currency.** The accuracy of the impedance estimate depends on
  the number of independent estimates and on their coherence, and increasing either
  costs recording time.

## 2. Impedance levels and the telluric signal

For a uniform half-space of resistivity $\rho$, the impedance magnitude is

$$|Z| = \sqrt{\omega \mu_0 \rho} ,$$

so the same resistivity gives a larger impedance at higher frequency. The
demonstration evaluates it, and converts a 1 nT magnetic signal into the telluric
field it produces, using $E = Z\,H$ with $H = B/\mu_0$:

| $\rho_a$ (Ω·m) | $f = 0.1$ Hz | $f = 1$ Hz | $f = 10$ Hz |
|---|---|---|---|
| 10 | $|Z| = 0.00281$ Ω, 2.236 mV/km | 0.00889 Ω, 7.073 | 0.02810 Ω, 22.36 |
| 100 | 0.00889 Ω, 7.073 mV/km | 0.02810 Ω, 22.36 | 0.08886 Ω, 70.73 |
| 1000 | 0.02810 Ω, 22.36 mV/km | 0.08886 Ω, 70.73 | 0.28099 Ω, 223.6 |

(Each cell lists $|Z|$ and the telluric field produced by a 1 nT magnetic signal.)
Two design consequences follow:

1. **The telluric signal is small.** Tens of millivolts per kilometre, which is why the electric dipoles are long and the electrode noise floor matters.
2. **The signal grows with the impedance**, so a resistive site gives a *larger* telluric signal for the same magnetic field, and therefore better electric signal-to-noise at high frequency — a small compensation for the fact that resistive sites are usually the harder ones to interpret.

The conversion back is worth writing down because it is the most common
arithmetic error in MT: with $E$ in mV/km and $H$ in nT-equivalent
($1\ \mathrm{nT} = 7.96\times10^{-4}\ \mathrm{A/m}$), $Z$ in Ω is obtained by
$\mathbf{Z} = \mathbf{E}/\mathbf{H}$ with the fields converted to V/m and A/m.

## 3. Coherence: the currency of an MT estimate

The impedance is estimated from many short segments (or from a spectral estimate
over a band). For an estimator formed from $N$ independent estimates with a true
coherence $\gamma^{2}$ between the two fields, the fractional standard error of
$|Z|$ is approximately

$$\frac{\sigma_{|Z|}}{|Z|} \approx \sqrt{\frac{1-\gamma^{2}}{2\,N\,\gamma^{2}}} ,$$

which rearranges to the coherence required for a stated accuracy:

$$\gamma = \frac{1}{\sqrt{1 + 2N\sigma^{2}}} .$$

The demonstration's table:

| Target accuracy | $N = 20$ | $N = 100$ | $N = 400$ |
|---|---|---|---|
| 1 % | 0.9980 | 0.9901 | 0.9623 |
| 2 % | 0.9921 | 0.9623 | 0.8704 |
| 5 % | 0.9535 | 0.8165 | 0.5774 |

Read the table against a target. A 1 % impedance accuracy — a level of precision
that many published MT responses imply — requires a coherence of 0.998 from 20
estimates, or 0.990 from 400. Those are high coherences; the practical conclusion
is that **the precision of a published MT response is limited by coherence, and
coherence is limited by noise**, so a reported "1 % error bar" is a statement about
the estimation, not about the accuracy. A coherent noise source that raises the
apparent coherence without adding signal produces an *underestimated* error bar —
one of the classic traps of MT processing.

## 4. The dead band

Between roughly 0.1 Hz and a few hertz the natural MT signal is weak: the
ionospheric and magnetospheric sources that dominate above and below this band fall
away, and cultural noise rises. The consequence is a *lower coherence*, and the
number of independent estimates required for a fixed accuracy scales as

$$N \propto \frac{1-\gamma^{2}}{\gamma^{2}} .$$

The demonstration's table, relative to $\gamma = 0.99$:

| Coherence $\gamma$ | Relative $N$ | Relative to $\gamma = 0.99$ |
|---|---|---|
| 0.99 | 0.02030 | 1.00 |
| 0.98 | 0.04123 | 2.03 |
| 0.95 | 0.10803 | 5.32 |
| 0.90 | 0.23457 | 11.55 |
| 0.80 | 0.56250 | 27.70 |

**A band whose coherence falls from 0.99 to 0.90 needs about 11.6 times the
recording time** for the same impedance accuracy. That is the quantitative content
of the MT dead band: it is not that the data are unusable, it is that they cost an
order of magnitude more time, which is why deep-probing MT campaigns record for
days per site with a remote reference rather than for hours without one.

The practical responses, in order of effectiveness:

1. **Record longer** at the same site — the only universally applicable answer.
2. **Use a remote reference**, which raises the coherence in the band by removing the local noise contribution.
3. **Process robustly** — bounded-influence estimators down-weight the noisy segments instead of averaging them in, which is equivalent to raising the effective coherence.
4. **Choose the site** away from infrastructure, which lowers the noise floor before any processing.

## 5. The telluric dipole

The electric field is measured as a voltage between buried electrodes separated by
a **dipole length** $L$, so the signal is $V = E\,L$. With a typical field of
1 mV/km and an electrode-plus-preamplifier noise floor of 5 µV, the demonstration
reports

| $L$ (m) | Signal (µV) | SNR (dB) |
|---|---|---|
| 25 | 25.00 | 14.0 |
| 50 | 50.00 | 20.0 |
| 100 | 100.00 | 26.0 |
| 200 | 200.00 | 32.0 |
| 400 | 400.00 | 38.1 |

The signal is proportional to $L$ and the noise is not, so **dipole length is the
cheapest SNR available**: a 200 m dipole buys 18 dB over a 25 m one at the same
field. The cost is the land required, the cable, and the fact that a long dipole
senses a spatially averaged field — which is exactly what the MT assumption of a
uniform plane wave wants, so the averaging is an advantage up to the scale at which
the field's own spatial variation becomes significant.

Layout rules that follow from the physics:

1. **Two orthogonal dipoles**, each with its own pair of non-polarising electrodes, with the electrode spacing measured and recorded. Bentonite or a mud slurry in the electrode pit lowers the contact resistance and the noise.
2. **The magnetic sensors must be far enough from the electrodes and their cables** that the current in the telluric cables does not contaminate the magnetic measurement — a rule of a few tens of metres, verified by a test recording with the dipoles connected and disconnected.
3. **The telluric lines should not follow cultural features** (a road, a fence, a pipeline) more closely than necessary, because a line that does becomes an antenna.
4. **Everything must be levelled, oriented and recorded**, with the magnetic sensor orientation measured against true north and the dipole azimuths measured.

## 6. Remote reference and the bias it removes

Consider a coherent noise source that appears in both the local electric and the
local magnetic channel with coherence $\gamma_n$ between the noise in the two. The
single-station estimate of the impedance is then biased upward by

$$\frac{|Z_{\text{est}}|}{|Z_{\text{true}}|}
= \frac{1}{\sqrt{1-\gamma_n^{2}}} ,$$

so the apparent resistivity is biased by the square of that factor:

| $\gamma_n$ | Bias factor in $|Z|$ | Apparent-resistivity error |
|---|---|---|
| 0.3 | 1.0483 | 9.9 % |
| 0.5 | 1.1547 | 33.3 % |
| 0.7 | 1.4003 | 96.1 % |
| 0.9 | 2.2942 | 426.3 % |

A coherent noise source with 0.9 coherence between the noise in E and H **doubles
the impedance and quadruples the apparent resistivity** — a factor of five, which
is the size of the artefacts that appear in single-station MT data near
infrastructure and that are absent when a remote reference is used.

The mechanism is worth stating precisely, because it explains the limitations of
the method: the reference removes the noise that is present locally but *not* at
the remote site. If the noise appears at both, it is removed as signal; if it
appears in the local E and H but not remotely, it is removed as noise. What cannot
be removed is noise that is local, coherent between E and H, and also present at
the remote site — which is why the remote site must be remote, several tens of
kilometres away in a quiet direction, and why its own noise must be checked.

## 7. Site footprint and logistics

For a site with two orthogonal 100 m dipoles, four electrodes per dipole and three
magnetic sensors offset at least 10 m from the electrodes, the demonstration
reports:

| Item | Value |
|---|---|
| footprint | 100 m × 100 m = 0.010 km² |
| electrodes | 8, each in a lined pit with backfill |
| telluric cable | 400 m of four leads |
| magnetic sensors | 3, levelled and oriented, offset ≥ 10 m |

At this dipole length a site occupies about 0.01 km², which is the number to
compare with the land available, the grid spacing of a planned array, and the
access arrangements of
[23-01-04 Permits, Land Access, Cultural Heritage and Ethics](../01-field-safety-and-planning/04-permits-and-ethics.md).
The logistics that follow: transport of 8 electrode pits' worth of equipment, a crew
of two to three, and a recording period that is measured in days — which means the
site must be secure overnight and its power budget planned for the whole recording.

## 8. Assumptions and regime of validity

1. **A plane wave.** The MT impedance is defined for a uniform source field; source effects at long periods (the magnetospheric ring current) and at high latitudes make the impedance time-dependent, which is a physics limitation, not a field error.
2. **A homogeneous half-space for the $\rho_a$ formula.** For layered or
   two-dimensional ground, $\rho_a$ and $\phi$ are the data, and the model comes
   from inversion.
3. **Independent estimates.** The coherence formula assumes independent spectral estimates; overlapped or smoothed estimates are correlated, and the effective
   $N$ is smaller than the count.
4. **A true coherence.** The formula uses the true coherence, not the estimated one; using an estimated coherence that has been raised by coherent noise understates the error bar.
5. **A remote reference uncorrelated with the local noise.** If it is not, the
   method removes signal and leaves the bias.
6. **The electrode noise floor is the limiting noise.** Real telluric noise includes
   electrode drift (polarisation), which is why non-polarising electrodes are used
   and why the dipoles are checked between recording days.

## 9. The honest summary

- $|Z| = \sqrt{\omega\mu_0\rho}$; a 1 nT signal at 1 Hz over 100 Ω·m gives about
  22 mV/km.
- A 1 % impedance accuracy needs coherence 0.998 from 20 estimates, or 0.990 from
  400.
- A coherence drop from 0.99 to 0.90 costs 11.6× the recording time: the dead band
  is a time cost.
- Dipole length is the cheapest SNR: 200 m buys 18 dB over 25 m.
- Coherent noise with 0.9 coherence quadruples the apparent resistivity; a remote
  reference removes it.
- A 100 m dipole site occupies about 0.01 km².

## 10. Python demonstration

[`code/mt_fieldwork_demo.py`](./code/mt_fieldwork_demo.py) prints every number
quoted above. It:

1. tabulates the impedance magnitude and the telluric field from a 1 nT magnetic
   signal over three resistivities and three frequencies;
2. computes the coherence required for 1 %, 2 % and 5 % accuracy from 20, 100 and
   400 estimates;
3. tabulates the recording time required as the coherence falls;
4. computes the telluric signal and SNR for five dipole lengths;
5. tabulates the single-station bias from four noise coherences;
6. computes the footprint, electrode count and cable length of a site.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/04-electrical-em-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_fieldwork_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/03-mt-fieldwork-exercises.md`](./exercises/03-mt-fieldwork-exercises.md)
and
[`exercises/03-mt-fieldwork-solutions.md`](./exercises/03-mt-fieldwork-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. Compute $|Z|$ for a 50 Ω·m half-space at 2 Hz, and the apparent resistivity a
   measurement of $|Z| = 0.05$ Ω at 2 Hz implies.
2. Compute the coherence required for a 3 % accuracy in $|Z|$ from 50 estimates.
3. A band's coherence falls from 0.97 to 0.88. Compute the relative recording time
   required, relative to 0.97.
4. Compute the telluric signal and SNR for a 150 m dipole with a 1 mV/km field and
   a 5 µV noise floor.
5. Compute the apparent-resistivity error from a coherent noise source with
   coherence 0.6.
6. State the two properties a remote reference site must have.

## 13. Common pitfalls

1. **Treating the reported error bar as an accuracy.** It is an estimation error,
   and coherent noise can make it too small.
2. **Recording without a remote reference near infrastructure.** The bias factor
   reaches 1.4 at coherence 0.7.
3. **Short dipoles for convenience.** 25 m costs 18 dB against 200 m.
4. **Placing magnetic sensors close to the telluric cables.** The cable currents
   contaminate the magnetic channels.
5. **Ignoring the source effect at long periods.** The impedance is not
   time-independent.
6. **Using an estimated coherence in the error formula.** It is biased upward by
   coherent noise.
7. **Underestimating the recording time.** The dead band costs an order of
   magnitude, and the site must be secure for the whole period.

## 14. Where this is used

- Crustal and mantle resistivity studies, where the target response is at
  $10^{-3}$–$10^{3}$ s periods and the recording times are days to weeks.
- Geothermal exploration, where MT is the primary method for locating the
  conductive clay cap and the resistive reservoir.
- Mineral exploration for base and precious metals, at higher frequencies and
  shorter deployments.
- Hazard and monitoring studies, where the repeated response is compared against
  itself and coherence stability matters more than absolute accuracy.
- Any MT dataset archived for reuse: the site coordinates, sensor orientations,
  dipole lengths and the reference site's identity are part of the data.

## 15. Related lessons

- [02 EM Fieldwork: Loop, Coil and Grounded-Source Configurations](02-em-fieldwork.md) —
  the controlled-source physics and the coupling arguments.
- [04 GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration](04-gpr-fieldwork.md) —
  the high-frequency end of the same spectrum.
- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the theory behind these field measurements.
- [11-04-02 Magnetotellurics for Geothermal Resource Assessment](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/02-mt-for-geothermal.md) —
  a major application.
- [23-07-03 Case Study: A Magnetotelluric Campaign](../07-field-campaign-case-studies/03-case-study-mt-campaign.md) —
  this design carried through a whole campaign.

## 16. Self-assessment checklist

- [ ] I can convert between impedance, apparent resistivity and telluric field.
- [ ] I can compute the coherence a stated accuracy requires.
- [ ] I can compute the recording time a weaker band costs.
- [ ] I can choose a dipole length from the field and the noise floor.
- [ ] I can compute the bias a coherent noise source produces.
- [ ] I can size a site and state the layout rules.
