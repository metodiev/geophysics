---
id: 02-10-05
title: "Fibre-Optic Sensing and Distributed Acoustic Sensing"
level: graduate
prereqs: ["02-10-01", "02-10-02", "02-07-05"]
estimated_minutes: 90
tags: [fibre-optics, das, rayleigh-scattering, strain, phase, borehole, seismology]
---

# Fibre-Optic Sensing and Distributed Acoustic Sensing

A single strand of glass, kilometres long, buried in a trench or cemented behind
borehole casing, can act as an array of thousands of strain sensors with no
electronics inside the ground. That capability rests on four physical facts, and
this lesson builds all four:

1. **Total internal reflection** confines light to a 9 µm core over kilometres
   (lesson [02-10-01](./01-geometrical-optics.md) §3).
2. **Rayleigh scattering** from density fluctuations in the glass returns a small
   fraction of the light continuously along the fibre, so the fibre itself
   provides the backscatter every sensor needs.
3. **Interference** makes the phase of that backscattered light measurable to
   milliradians (lesson [02-10-02](./02-interference-diffraction-optics.md) §1).
4. **The strain-optic effect** converts mechanical strain into an optical phase
   change with a known coefficient, computed in §5.

Distributed acoustic sensing (DAS) is the geophysical embodiment of these four.
It is now used for borehole seismic acquisition, microseismic monitoring,
vertical-seismic-profile surveys without a geophone array, submarine
seismology on retired telecom cables, and pipeline and perimeter monitoring.
The physics of what it measures — and of what it *mis*-measures — is the subject
of this lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a step-index fibre's numerical aperture, V number, mode count and
   cutoff wavelength, and explain why phase-based sensing requires single mode.
2. **Compute** the Rayleigh scattering loss at any wavelength from the
   $\lambda^{-4}$ law, and compute a two-way loss budget.
3. **Derive** an order-of-magnitude Rayleigh backscatter recapture fraction and
   compute the backscattered power level of a pulse.
4. **Compute** the spatial resolution of an OTDR or DAS measurement from the
   pulse width, and the maximum pulse repetition rate from the fibre length.
5. **Derive** the phase-to-strain relation of a single-mode fibre from the
   strain-optic coefficients, and compute the phase produced by a given strain,
   gauge length and wavelength.
6. **Convert** seismic particle velocity into strain and hence into an optical
   phase shift, using $\epsilon = v/c$.
7. **Compute** the spatial transfer function of a gauge length: its first null
   and its 3 dB frequency, and explain why gauge length is an instrument
   response that must be deconvolved.
8. **Compute** the temperature cross-sensitivity in microstrain equivalent and
   state the design measures that mitigate it.

## Prerequisites

- [02-10-01 Geometrical Optics, Refraction and Lenses](./01-geometrical-optics.md)
  — total internal reflection, numerical aperture, the V number and the
  single-mode condition.
- [02-10-02 Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md)
  — coherence length, fringe counting and the phase measurement that makes DAS
  possible.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
  — the field picture of the guided wave, and the polarisation that a
  polarisation-diverse DAS receiver exploits.

## 1. Why single mode

The fibre design equations were derived in lesson
[02-10-01](./01-geometrical-optics.md); the sensing-relevant conclusions are:

$$\mathrm{NA} = \sqrt{n_1^2-n_2^2}, \qquad
V = \frac{2\pi a}{\lambda}\mathrm{NA}, \qquad
M \approx \frac{V^2}{2} \ \ (V \gg 1),\qquad
V_{\text{single mode}} < 2.4048 . \tag{1}$$

```text
  n_core = 1.4504, n_clad = 1.4447, a = 4.10 um, lambda = 1550 nm
  NA = 0.128460, acceptance half-angle in air = 7.3806 deg
  V  = 2.1350 (single mode below 2.4048)
  cutoff lambda_c = 1376.1 nm
  propagation speed = c/n_group = 2.041905e+08 m/s
```

**A multimode fibre has no single phase.** Each mode propagates at a different
group velocity, so light launched into a multimode fibre emerges with a
mode-dependent phase; interfering it produces speckle, which changes when the
fibre moves. For an interferometric sensor this is not a nuisance but a
fatal ambiguity: the measured phase would change with the mode distribution and
not only with the strain. That is why every phase-based fibre sensor — DAS,
interferometric strainmeters, fibre gyroscopes — operates in single-mode fibre
below $V = 2.405$.

The group index $n_g = 1.4682$ (nominal at 1550 nm) sets the propagation speed
$v = c/n_g = 2.0419\times10^8$ m s⁻¹, which appears in every timing and
spatial-resolution calculation that follows. Note that $n_g$ differs from the
phase index $n = 1.4504$; dispersion means the phase and the pulse travel at
different speeds, and using $n$ where $n_g$ belongs is a 1 per cent timing error.

## 2. Rayleigh scattering: the loss and the signal

### 2.1 Loss scales as $\lambda^{-4}$

Light is lost from a fibre by Rayleigh scattering from density fluctuations
frozen into the glass, and by infrared absorption. The Rayleigh contribution
scales as $\lambda^{-4}$:

$$\frac{\alpha_R(\lambda_2)}{\alpha_R(\lambda_1)}
= \left(\frac{\lambda_1}{\lambda_2}\right)^4 . \tag{2}$$

```text
  wavelength (nm)   scattering ratio vs 1550 nm
              850                        11.057
             1064                         4.504
             1310                         1.960
             1550                         1.000
             1625                         0.828
```

The ratio between 850 and 1550 nm is 11.06, which is why long-haul transmission
runs near 1550 nm; raising the wavelength further is stopped by the rising
infrared absorption edge, so the practical window is 1300–1600 nm with a loss
minimum near 1550. A standard single-mode fibre has a nominal attenuation of
0.20 dB km⁻¹ at 1550 nm, i.e. 0.04605 Np km⁻¹.

### 2.2 The two-way loss budget

A distributed measurement sends a pulse out and detects the light scattered back
along the *same* fibre, so the loss is paid twice. The demo computes both:

```text
  one-way length (km)  one-way (dB)   round trip (dB)   round-trip fraction
                  1.0         -0.20             -0.40             9.120e-01
                  2.0         -0.40             -0.80             8.318e-01
                  5.0         -1.00             -2.00             6.310e-01
                 10.0         -2.00             -4.00             3.981e-01
                 20.0         -4.00             -8.00             1.585e-01
                 50.0        -10.00            -20.00             1.000e-02
```

A 10 km loop returns 4 dB down: 40 per cent of the launched power is absorbed
before the backscatter is even generated. This is the first term in every DAS
range budget, and it is why long-range DAS needs high launch power and a
low-noise coherent receiver rather than a clever pulse shape.

### 2.3 How much comes back: the recapture fraction

Only the fraction of Rayleigh-scattered light that is captured by the
*backward-propagating guided mode* is measured. For isotropic scattering and a
small numerical aperture, that fraction is the backward acceptance solid angle
divided by $4\pi$:

$$S \approx \frac{\theta_{\max}^2}{4}, \qquad
\theta_{\max} = \arcsin\!\left(\frac{\mathrm{NA}}{n_1}\right) . \tag{3}$$

```text
    theta_max in the core = asin(NA/n1) = 5.0813 deg = 0.088685 rad
    S ~ theta_max^2/4 = 1.9663e-03
```

This order-of-magnitude derivation gives $S \sim 2\times10^{-3}$. The demo adopts
$S = 1.5\times10^{-3}$ and labels it as an **adopted parameter, not a computed
one**: Rayleigh scattering in glass is not perfectly isotropic and the modes have
polarisation structure, so the exact value must come from the fibre data sheet or
from a calibration. Stating which parameters are adopted and which are derived is
part of the measurement.

The returned level for a rectangular pulse of width $W$ is

$$\frac{P_{\text{bs}}}{P_0} = S\,\alpha\,\frac{vW}{2}\,e^{-2\alpha L} , \tag{4}$$

with $\alpha$ the loss in Np m⁻¹:

```text
  W (ns)  scattering length (m)   level at 0 km (dB)   level at 10 km (dB)
     5.0                 0.5105               -74.53                -78.53
    10.0                 1.0210               -71.52                -75.52
    20.0                 2.0419               -68.51                -72.51
    50.0                 5.1048               -64.53                -68.53
   100.0                10.2095               -61.52                -65.52
```

The backscatter is 60–80 dB below the launched power, i.e. seven to eight orders
of magnitude. **DAS is a weak-signal technique**: the useful information is a
phase modulation on a carrier attenuated by a factor of $10^{-7}$, and the only
compensations available are more launch power, a longer pulse (at the cost of
resolution) and coherent averaging.

## 3. Spatial resolution and sampling rate

The pulse of width $W$ occupies $vW/2$ of fibre at any instant (the factor 2 is
the round trip), so the **spatial resolution** is

$$\Delta z = \frac{vW}{2} = \frac{cW}{2n_g} . \tag{5}$$

```text
  W (ns)   dz = vW/2 (m)  PRF limit for 10 km (Hz)
     5.0           0.510                   10209.5
    10.0           1.021                   10209.5
    20.0           2.042                   10209.5
    50.0           5.105                   10209.5
   100.0          10.210                   10209.5
   200.0          20.419                   10209.5
```

Resolution and repetition rate are *independent*: a 5 ns pulse resolves better
but does not let the system fire faster, because the fibre must still be
traversed twice by light. The maximum pulse repetition frequency for a fibre of
length $L$ is

$$f_{\text{prf}} = \frac{v}{2L} , \tag{6}$$

which for a 10 km fibre is 10 209.5 Hz. Since a single-ended system cannot
overlap pulses, this is also the *temporal sampling rate* of the recording, and
therefore the Nyquist frequency is half of it:

```text
  range (km)   f_prf = v/(2L) (Hz)  Nyquist = f_prf/2 (Hz)
         1.0              102095.2                 51047.6
         2.0               51047.6                 25523.8
         5.0               20419.0                 10209.5
        10.0               10209.5                  5104.8
        20.0                5104.8                  2552.4
```

A 10 km single-ended system samples at about 10 kHz and is Nyquist-limited to
about 5 kHz: ample for seismic and microseismic work, short of the 10–100 kHz
band of acoustic emission and ultrasound, for which a shorter fibre or a
chirped-pulse scheme is required. Aliasing in DAS is not a subtle failure — an
event above the Nyquist frequency appears at a wrong frequency at full
amplitude.

The spatial analogue: channels spaced $\Delta x$ apart represent wavenumbers only
up to $\pi/\Delta x$, i.e. frequencies up to $v/(2\Delta x)$:

```text
   dx (m)   max wavenumber (rad/m)   max f, v=3000 (Hz)   max f, v=1500 (Hz)
    0.25                  12.5664               6000.0               3000.0
    0.50                   6.2832               3000.0               1500.0
    1.00                   3.1416               1500.0                750.0
    2.00                   1.5708                750.0                375.0
    5.00                   0.6283                300.0                150.0
```

**Channel spacing, not gauge length, sets the spatial Nyquist limit.** With 1 m
spacing, a 3000 m s⁻¹ wave below 1500 Hz is unaliased; a 200 m s⁻¹ surface wave
aliases above 100 Hz. Both numbers are set in the instrument configuration and
neither follows from the other.

## 4. From strain to phase: the measurement

### 4.1 Derivation

The optical phase accumulated over a fibre of length $L$ and index $n$ is

$$\phi = \frac{2\pi n L}{\lambda} . \tag{7}$$

Strain $\epsilon$ changes both factors: $L \to L(1+\epsilon)$, and the index
changes through the strain-optic (photoelastic) effect,

$$\Delta n = -\frac{n^3}{2}\left[p_{12} - \nu(p_{11}+p_{12})\right]\epsilon , \tag{8}$$

for a fibre with light polarised transverse to the strain axis. Combining,

$$\frac{\Delta\phi}{\phi} = \xi\,\epsilon, \qquad
\boxed{\ \xi = 1 - \frac{n^2}{2}\left[p_{12} - \nu(p_{11}+p_{12})\right]\ } \tag{9}$$

and therefore

$$\frac{\Delta\phi}{L} = \frac{2\pi n \xi}{\lambda}\,\epsilon . \tag{10}$$

The demo computes $\xi$ from nominal fused-silica constants:

```text
  p11 = 0.121, p12 = 0.27, nu = 0.17, n = 1.4504
  xi = 1 - (n^2/2)(p12 - nu(p11+p12)) = 0.785921
  (the commonly quoted value for silica is about 0.78)

  phase change per metre per unit strain = 2 pi n xi/lambda =
    4.6208e+06 rad per metre per unit strain

 gauge length L (m)   rad per 1 nstrain   deg per 1 nstrain   rad per 1 ustrain
                1.0             0.00462              0.2648             4.62078
                5.0             0.02310              1.3238            23.10388
               10.0             0.04621              2.6475            46.20775
               20.0             0.09242              5.2950            92.41551
               40.0             0.18483             10.5900           184.83102
```

One nanometre-per-metre of strain over a 10 m gauge produces 0.0462 rad, about
2.65°. Phase is measured interferometrically to milliradians, so the strain
resolution is of order

$$\epsilon_{\min} \sim \frac{10^{-3}}{2\pi n\xi L/\lambda}
= 2.2\times10^{-11} \quad (L = 10\ \mathrm m) , \tag{11}$$

five orders of magnitude below the elastic limit of rock. **DAS does not fail
because it is insensitive; it fails because it is too sensitive to everything**
— temperature, cable coupling, pressure and its own laser noise.

### 4.2 From ground motion to strain

For a plane wave of phase velocity $c$, the strain is the ratio of particle
velocity to phase velocity,

$$\epsilon = \frac{v}{c} , \tag{12}$$

which follows from differentiating the displacement field. The demo converts:

```text
 particle velocity (mm/s)   c (m/s)       strain  phase over 10 m (rad)
                     0.01      1500    6.667e-09                 0.3081
                     0.01      3000    3.333e-09                 0.1540
                     0.10      3000    3.333e-08                 1.5403
                     1.00      3000    3.333e-07                15.4026
                    10.00      1500    6.667e-06               308.0517
```

Typical seismic ground motion of 0.01–1 mm s⁻¹ at 3000 m s⁻¹ gives strains of
$3.33\times10^{-9}$ to $3.33\times10^{-7}$ and phase signals of 0.154 to 15.4 rad
over a 10 m gauge. This is why DAS records large amplitudes without difficulty
and why the limiting factor is dynamic range, not sensitivity: a local earthquake
can produce hundreds of radians of phase over a single gauge, which the
interrogator must unwrap or clip.

## 5. The gauge length is a spatial filter

A DAS channel reports the strain averaged over the **gauge length** $L$, which
convolves the strain field with a boxcar. For a sinusoidal strain field of
spatial wavelength $\Lambda$, the response magnitude is

$$\left|\mathrm{sinc}\!\left(\frac{\pi L}{\Lambda}\right)\right|
= \left|\frac{\sin(\pi L/\Lambda)}{\pi L/\Lambda}\right| , \tag{13}$$

so the channel is **blind** to wavelengths that fit a whole number of
half-cycles in the gauge. With $f = v/\Lambda$:

```text
 gauge L (m)  first null Lambda (m)   first null f, v=3000 (Hz)   3 dB f, v=3000 (Hz)
          1.0                   1.00                      3000.0                1328.8
          2.0                   2.00                      1500.0                 664.4
          5.0                   5.00                       600.0                 265.8
         10.0                  10.00                       300.0                 132.9
         20.0                  20.00                       150.0                  66.4
         40.0                  40.00                        75.0                  33.2
```

and the response across frequency for a 10 m gauge in rock:

```text
   f (Hz)   Lambda (m)   L/Fambda    response  response (dB)
      1.0       3000.0      0.003      1.0000          -0.00
     10.0        300.0      0.033      0.9982          -0.01
     30.0        100.0      0.100      0.9836          -0.07
    100.0         30.0      0.333      0.8270          -0.82
    150.0         20.0      0.500      0.6366          -1.96
    300.0         10.0      1.000      0.0000   -inf
    600.0          5.0      2.000      0.0000   -inf
```

**This is the single most important instrument-response correction in DAS
processing.** A 10 m gauge has a 3 dB point near 133 Hz and a null at 300 Hz for
a 3000 m s⁻¹ wave; recording the same event with a 5 m gauge moves both to
265.8 Hz and 600 Hz. Comparing amplitudes across gauges without applying (13) is
comparing two different instruments, and an apparent "attenuation" in a DAS
section may be nothing but the gauge response.

The relationship between the strain measured by DAS and the true strain field is
therefore a linear filter, and the correct processing step is a deconvolution
within the band where the response is above the noise floor — never an
amplitude-equalisation fudge.

## 6. Temperature cross-sensitivity

Temperature changes the phase through thermal expansion and the thermo-optic
effect:

$$\frac{1}{\phi}\frac{\mathrm d\phi}{\mathrm dT}
= \alpha_T + \frac{1}{n}\frac{\mathrm dn}{\mathrm dT} . \tag{14}$$

```text
  alpha_T            = 5.50e-07 /K  (thermal expansion, nominal)
  (1/n) dn/dT        = 7.5841e-06 /K  (thermo-optic, nominal)
  sum                = 8.1341e-06 /K

  phase per metre per kelvin   = 4.782e+01 rad/m/K
  phase per metre per strain   = 4.621e+06 rad/m per unit strain
  i.e. 1 K is equivalent to 10.35 microstrain.
```

One kelvin produces the same phase shift as about 10 microstrain. Since seismic
strains are $10^{-9}$–$10^{-7}$, a temperature drift of a millikelvin
(0.010 µε equivalent, i.e. $1.0\times10^{-8}$ strain) is already comparable with
a local earthquake, and a diurnal surface swing of a few kelvin is a thousand
times larger than the seismic signal. **This is the dominant systematic error in
near-surface DAS.**

The mitigations are engineering, not analysis:

| Mitigation | How it works | Limitation |
|---|---|---|
| Co-located temperature reference | Measure $T$ independently and subtract | Needs an independent sensor at the same depth |
| Strain-free reference fibre | A loose-tube fibre sees $T$ but not strain | Doubles the fibre and the interrogator channels |
| Coupled cable design | Mechanically couples strain while isolating thermal expansion | Design-specific; rarely perfect |
| Common-mode removal | Remove signals coherent across channels | Fails where the seismic signal is also coherent |
| Band separation | Exploit the different spectral content of thermal drift and seismic signals | The two overlap below 1 mHz and above 1 Hz near the surface |

A DAS record from a cable in a shallow trench carries a strong daily thermal
signal that must be removed before the seismic signal can be interpreted. Any
DAS result presented without a discussion of thermal coupling is incomplete.

## 7. Physical interpretation

**DAS is an array of strain gauges with no gauges in it.** The sensing element is
a section of ordinary fibre; the interrogator measures the phase difference
between backscatter from two positions along it. Ten thousand channels at 1 m
spacing on a 10 km fibre — the demo computes 10 000 channels with a spatial
Nyquist wavenumber of 3.1416 rad m⁻¹, corresponding to 1500 Hz at 3000 m s⁻¹ —
cost one fibre and one instrument, with no downhole electronics and no clamping.
That is the entire engineering case for DAS over a geophone array.

**The gauge length is a low-pass filter, and the channel spacing is a sampling
rate.** They are independent parameters with independent consequences: gauge
length sets which wavelengths are attenuated or nulled, channel spacing sets
which are aliased. Confusing them produces processing that corrects the wrong
error.

**Rayleigh scattering is simultaneously the signal and the loss.** The same
mechanism that returns 10⁻⁷ of the pulse also removes 0.2 dB km⁻¹ of it. A fibre
with less scattering would carry the pulse further but return less of it; the
optimum is set by the ratio of the two, which is why the loss and the backscatter
are computed together (§2) rather than separately.

**Phase is a scalar that hides a vector.** The interrogator measures one number
per channel, but the true mechanical state of the cable has axial strain,
bending, twist and temperature. DAS is therefore sensitive to *everything*, and
the interpretation of a DAS record depends on knowing the cable's coupling to the
ground — a geotechnical question, not an optical one.

## 8. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Single mode | One spatial mode, one phase | Multimode fibre: modal speckle, no single phase |
| Isotropic Rayleigh scattering | $S$ from a solid-angle ratio | The real scattering is anisotropic and polarisation-dependent; $S$ must be calibrated |
| Lossless step index | Constant $n$ along the fibre | Real fibres have index fluctuations, splices, connectors and bends |
| Linear loss | Uniform $\alpha$ | Bend loss, hydrogen ageing, radiation-induced loss |
| Weak strain | Small-perturbation strain-optic coefficients | Large strain, plastic deformation, fibre yield (~5 per cent) |
| Elastic cable coupling | Fibre strain equals ground strain | Slipping, loose-tube, grouted versus trenched versus clamped installation; coupling varies along the cable |
| Constant temperature | $\Delta\phi$ from strain alone | The cross-sensitivity of §6 |
| Plane wave $\epsilon = v/c$ | A single phase velocity | Dispersive surface waves, near-field sources, 3-D scattering |
| Static gauge response | Response is the boxcar of (13) | The real gauge is a weighted average of two separated sections; the response is instrument-specific |
| No strain-optic birefringence | One polarisation state | Birefringence converts strain into polarisation changes; polarisation diversity is used to handle it |
| Aliasing-free acquisition | Sampling above Nyquist in time and space | Real fibre-length limits; §3 gives the numbers |

## 9. Units and dimensional analysis

- NA and $V$: dimensionless; $V$ is compared with 2.4048, never with a length.
  ✓ (demo: $V = 2.1350$.)
- $\alpha$ in dB km⁻¹ and Np m⁻¹ are different units: 0.2 dB km⁻¹ is
  0.04605 Np km⁻¹, and 1 Np = 20/ln 10 dB = 8.6859 dB. Mixing them produces
  answers wrong by a factor of 8.7, silently.
- $S$ in (3): $(\mathrm{rad})^2/1$, dimensionless ✓ — it is a fraction, of order
  $2\times10^{-3}$.
- $P_{\text{bs}}/P_0$: $1\times(\mathrm{m^{-1}})\times(\mathrm m) = 1$
  dimensionless ✓ (check $\alpha (vW/2)$: Np m⁻¹ × m = Np).
- $\Delta z = vW/2$: $\mathrm{m\,s^{-1}}\cdot\mathrm s = \mathrm m$ ✓. The factor
  2 is the round trip and omitting it halves the resolution.
- $f_{\text{prf}} = v/(2L)$: $\mathrm{m\,s^{-1}}/\mathrm m = \mathrm{Hz}$ ✓.
- $\xi$ in (9): dimensionless, and it must be below 1. It is 0.786 for silica: a
  third of the phase change expected from the length change alone is cancelled
  by the strain-optic index change. Ignoring the photoelastic term
  overestimates the sensitivity by 27 per cent.
- $\Delta\phi/L$ in (10): $\mathrm{rad\,m^{-1}}$ per unit strain. Multiply by a
  length in metres and a strain to get radians ✓ (demo: $4.6208\times10^6$
  rad m⁻¹ per unit strain; $10 \times 10^{-9}$ of that is $4.62\times10^{-2}$
  rad ✓).
- $\epsilon = v/c$: $\mathrm{m\,s^{-1}}/\mathrm{m\,s^{-1}}$ ✓ dimensionless.
- Response of a gauge: $|\operatorname{sinc}(\pi L/\Lambda)|$ is dimensionless
  because $L/\Lambda$ is; the argument must be in radians, so
  $\operatorname{sinc}(x) = \sin x/x$ and not $\sin(\pi x)/(\pi x)$ unless you
  intend the latter.
- $(\mathrm d\phi/\mathrm dT)/L$: $\mathrm{rad\,m^{-1}K^{-1}}$, converted to a
  strain equivalent by dividing by $\mathrm{rad\,m^{-1}}$ per unit strain ✓
  (demo: 10.35 µε K⁻¹).
- **Useful anchors:** $n = 1.4504$ and $n_g = 1.4682$ at 1550 nm; 0.2 dB km⁻¹;
  backscatter 60–80 dB below launch; 10 ns pulse → 1.02 m resolution; 10 km →
  10.2 kHz maximum pulse rate; $\xi \approx 0.786$; 1 nε over 10 m → 0.046 rad;
  1 K ≡ 10.35 µε; gauge-length null at $f = v/L$.

## 10. Python demonstration

[`code/fibre_optics_sensing_demo.py`](./code/fibre_optics_sensing_demo.py)
computes the fibre geometry, the Rayleigh loss and its $\lambda^{-4}$ scaling,
the two-way budget, the recapture fraction and backscatter level, the spatial and
temporal resolution limits, the phase-to-strain sensitivity, the gauge-length
transfer function, the sampling limits and the temperature cross-sensitivity. It
uses the standard library only. Every number quoted in this lesson is its actual
output, and every nominal parameter is labelled as such in the output itself.

### What to observe

| Observation | Consequence |
|---|---|
| $V = 2.1350$, cutoff 1376.1 nm | This fibre is single-mode at 1550 nm; the phase is a single number |
| $v = 2.0419\times10^8$ m s⁻¹ from $n_g = 1.4682$ | Use the group index, not the phase index, for timing |
| Loss ratio 11.06 between 850 and 1550 nm | The $\lambda^{-4}$ law decides the operating wavelength |
| 10 km round trip: −4 dB, 39.8 per cent returned | The loss budget is paid twice in a distributed measurement |
| $S \sim 2\times10^{-3}$ derived; $1.5\times10^{-3}$ adopted | Which parameters are computed and which are assumed is stated |
| 10 ns pulse: backscatter −71.5 dB at 0 km, −75.5 dB at 10 km | The signal is seven orders of magnitude below the pulse |
| 10 ns pulse: 1.021 m resolution; 100 ns: 10.210 m | Resolution is bought with signal |
| 10 km fibre: $f_{\text{prf}} = 10\,209.5$ Hz, Nyquist 5104.8 Hz | The geometry of the cable sets the temporal bandwidth |
| 1 m channel spacing: 10 000 channels, spatial Nyquist 1500 Hz at 3000 m s⁻¹ | Aliasing is a configuration choice |
| $\xi = 0.786$; 1 nε over 10 m → 0.0462 rad (2.65°) | The photoelastic effect reduces the phase by 21 per cent |
| 1 mm s⁻¹ ground motion at 3000 m s⁻¹ → 15.4 rad over 10 m | Dynamic range, not sensitivity, is the limit |
| 10 m gauge: 3 dB at 132.9 Hz, null at 300 Hz | The gauge is a spatial filter that must be deconvolved |
| 1 K ≡ 10.35 µε | Temperature is the dominant systematic in near-surface DAS |

> **Breaking exercise.** Before running anything, predict the effect on the
> gauge response of halving the gauge length to 5 m *and* doubling the wave speed
> to 6000 m s⁻¹, and predict the spatial resolution required to avoid aliasing a
> 6000 m s⁻¹ wave at 2000 Hz. Then change the demo and check. Finally, predict
> the two-way loss of a 30 km loop and compare it with the 20 km row.

## 11. Common mistakes

1. **Using a multimode fibre for a phase measurement.** There is no single phase;
   the measurement is speckle, and it changes when the cable moves.
2. **Confusing the phase index with the group index.** $n = 1.4504$ sets the
   phase, $n_g = 1.4682$ sets the pulse speed; use the right one, and state which.
3. **Treating $S$ as a derived constant.** The recapture fraction must be
   calibrated or taken from a data sheet; the geometric estimate is an order of
   magnitude.
4. **Mixing dB and Np.** A factor of 8.7 hides in that confusion.
5. **Forgetting the factor 2 in the round trip.** Both the loss and the spatial
   resolution carry one.
6. **Assuming gauge length sets the spatial resolution of the *image*.** Gauge
   length filters; channel spacing samples. They are different.
7. **Applying a gauge correction as an amplitude fudge.** It is a filter, and at
   the null no correction can recover the signal because it was never measured.
8. **Ignoring thermal coupling.** 1 K ≡ 10.35 µε; a shallow cable in daylight
   sees tens of microstrain of apparent strain.
9. **Reporting DAS amplitudes without stating the installation.** Grouted,
   trenched, clamped and loose-tube cables couple to the ground differently, and
   the coupling function is part of the instrument response.
10. **Assuming the strain measured is the strain of the formation.** The fibre
    measures its own strain; converting to formation strain requires a coupling
    model, and in soft or unconsolidated ground the coupling is neither uniform
    nor linear.
11. **Overlooking polarisation.** Birefringence converts strain into polarisation
    change and back again; a polarisation-diverse receiver exists precisely to
    handle this.
12. **Quoting a quoted strain resolution without the gauge length and the
    bandwidth.** Strain resolution is meaningless without both.

## 12. Real-world applications

- **Borehole seismic and vertical seismic profiling.** A fibre cemented behind
  casing gives a dense, permanent receiver array without a geophone string or a
  wireline run; the gauge-length response of §5 sets the usable bandwidth.
- **Microseismic monitoring.** Hydraulic-fracturing and geothermal reservoirs are
  monitored with DAS arrays at 1 m spacing over kilometres, detecting
  $10^{-9}$-strain events.
- **Submarine seismology.** Retired telecom cables are interrogated as
  seafloor strain arrays, giving ocean-bottom coverage that no seafloor
  seismometer network can match
  ([15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md)).
- **Earthquake and ambient-noise seismology.** DAS arrays measure teleseismic,
  regional and ambient-noise wavefields; the strain-to-velocity conversion (12)
  is the bridge to conventional records
  ([06 Seismology](../../06-seismology/README.md)).
- **Pipeline, perimeter and infrastructure monitoring.** Third-party intrusion,
  leaks and ground movement change the strain field along a buried cable, and DAS
  localises the change in space and time.
- **Distributed temperature sensing (DTS).** The same Rayleigh backscatter with
  a Raman component gives a temperature profile along the same fibre, used for
  borehole thermal profiling and leak detection
  ([05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)).
- **Geotechnical and slope monitoring.** Strain accumulated along a cable in a
  landslide or a dam foundation is a direct measurement of deformation.
- **Interferometric strainmeters and gyroscopes.** The same phase-to-strain
  physics at the highest precision, for geodesy and inertial navigation.

## 13. Further reading

- **Snyder, A. W., & Love, J. D. *Optical Waveguide Theory* (Chapman & Hall).**
  The single-mode condition, mode structure and bend loss, from first
  principles. Level: graduate.
- **Mitschke, F. *Fiber Optics: Physics and Technology* (2nd ed., Springer).**
  Attenuation, Rayleigh scattering, connectors and the practical parameters of
  real fibres. Level: advanced.
- **Hartog, A. H. *An Introduction to Distributed Optical Fibre Sensors* (CRC
  Press).** The authoritative treatment of OTDR, DAS, DTS and their
  interrogator architectures, including the gauge-length response. Level:
  graduate.
- **Bao, X., & Chen, L. (2012), "Recent progress in distributed fibre optic
  sensors", *Sensors* 12, 8601–8639.** A survey of the measurement principles
  and their performance limits. Level: graduate.
- **Lindsey, N. J., & Martin, E. R. (2021), "Fibre-optic seismology", *Annual
  Review of Earth and Planetary Sciences* 49.** DAS in seismology: arrays,
  applications, and the interpretation pitfalls of §7. Level: graduate.
- **Parker, T., Shatalin, S., & Farhadiroushan, M. (2014), "Distributed acoustic
  sensing — a new tool for seismic applications", *First Break* 32.**
  The geophysical case for DAS and the instrument response. Level: advanced.
- **Bakku, S. K. (2015), PhD thesis on DAS in boreholes (Colorado School of
  Mines).** Coupling, the gauge-length transfer function and its deconvolution,
  worked in detail. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [02-10-01 Geometrical Optics, Refraction and Lenses](./01-geometrical-optics.md)
  — total internal reflection and the fibre's design equations.
- [02-10-02 Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md)
  — coherence length and the phase measurement on which DAS rests.
- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](./03-radiative-transfer.md)
  — the same scattering physics in an atmospheric context.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
  — the guided field and the polarisation the receiver must handle.
- [06 Seismology](../../06-seismology/README.md)
  — the wavefields DAS records.
- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — distributed temperature sensing in boreholes.

Exercises:
[`exercises/05-fiber-optics-sensing-exercises.md`](./exercises/05-fiber-optics-sensing-exercises.md)
and
[`exercises/05-fiber-optics-sensing-solutions.md`](./exercises/05-fiber-optics-sensing-solutions.md).

## Self-assessment checklist

- [ ] I can compute NA, V, the mode count and the cutoff wavelength, and explain
      why DAS needs single mode. (§1)
- [ ] I can scale a Rayleigh loss between wavelengths and compute a two-way loss
      budget in dB and Np. (§2.1, §2.2)
- [ ] I can derive an order-of-magnitude recapture fraction and compute a
      backscatter level, stating which parameters are adopted. (§2.3)
- [ ] I can compute the spatial resolution from the pulse width and the maximum
      repetition rate from the fibre length. (§3)
- [ ] I can derive the phase-to-strain relation and compute $\xi$. (§4.1)
- [ ] I can convert particle velocity into strain and then into phase. (§4.2)
- [ ] I can compute a gauge-length transfer function, its first null and its
      3 dB frequency, and explain why it must be deconvolved. (§5)
- [ ] I can compute the temperature cross-sensitivity in microstrain equivalent.
      (§6)
- [ ] I can state the sampling limits in time and in space and how each is set.
      (§3)
- [ ] I can list at least four assumptions of DAS interpretation and the
      observation that would violate each. (§8)
