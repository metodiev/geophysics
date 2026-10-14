---
id: 06-09-07
title: "Seismic Attributes and Quantitative Interpretation"
level: graduate
prereqs: ["06-09-01", "06-09-04"]
tags: [seismology, reflection-seismology, attributes, resolution, tuning]
---

# Seismic Attributes and Quantitative Interpretation

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the complex-trace attributes (envelope, instantaneous phase and
   frequency) and explain what each measures.
2. **Derive** the vertical resolution limits: the Rayleigh-type $\lambda/4$
   criterion and the Widess $\lambda/8$ limit.
3. **Measure** the thin-bed tuning curve and explain why the amplitude maximum
   does not fall exactly at $\lambda/4$.
4. **Distinguish** the *detection* limit from the *resolution* limit, and show
   that a thin bed can be detected far below $\lambda/4$ when its contrast is
   strong.
5. **Derive** the Fresnel-zone horizontal resolution limit and show it degrades
   with depth.
6. **State** which attribute is appropriate for which task and the artefacts each
   introduces.

## Prerequisites

- [01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](01-reflection-principle.md).
- [04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM](04-migration-imaging.md).

## 1. Intuition: attributes are different ways of looking at the same trace

A seismic trace is an oscillating signal; a human eye can see perhaps two or
three of its properties at once. **Attributes** are transforms that make one
property visible: the envelope shows strength, the instantaneous phase shows
continuity (and hence faults), the instantaneous frequency shows local scale
(and hence thickness or attenuation). Used well, they reveal what the raw
amplitude display hides. Used badly, they reveal noise.

Underneath every attribute is a hard physical limit: the data have a finite
bandwidth, so events closer together than about a quarter wavelength interfere.
This is the **vertical resolution limit**, and it is why a "thin bed" is a
different object from a "thin layer that is still detectable". All numbers here
are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 The analytic trace

Given a real trace $s(t)$, form the analytic signal

$$z(t) = s(t) + i\,\mathcal{H}\{s\}(t),$$

where $\mathcal{H}$ is the Hilbert transform (a $90^\circ$ phase shift). Then

- **envelope** (reflection strength): $E(t) = |z(t)|$;
- **instantaneous phase**: $\phi(t) = \arg z(t)$;
- **instantaneous frequency**:
  $f(t) = \frac{1}{2\pi}\frac{\mathrm{d}\phi}{\mathrm{d}t}$.

### 2.2 Wavelength and the resolution scales

For a dominant frequency $f_0$ and velocity $v$,

$$\lambda = \frac{v}{f_0}, \qquad
\text{vertical resolution scale} \approx \frac{\lambda}{4}, \qquad
\text{Widess limit} = \frac{\lambda}{8}.$$

### 2.3 Fresnel zone

For zero offset, the first Fresnel-zone radius at depth $z$ is approximately

$$r_f \approx \sqrt{\frac{\lambda z}{2}}.$$

## 3. Derivations

### 3.1 The complex-trace attributes, and their pitfalls

The Hilbert transform makes $z(t)$ analytic, so its phase advances
monotonically and its modulus is a smooth envelope. Two practical cautions:

- **Instantaneous frequency is undefined where the envelope vanishes.** In the
  demonstration the single 30 Hz Ricker has $E=1.0000$ at its peak and an
  instantaneous frequency there of $33.81\ \mathrm{Hz}$ — *not* the nominal
  30 Hz. The instantaneous frequency of a broadband wavelet is not a constant;
  it equals the dominant frequency only in special cases. Averaging it without an
  amplitude threshold produces enormous spurious values in the low-amplitude
  zones.
- **The envelope's width is a measure of the wavelet, not of the bed.** The
  demonstration's envelope full-width at half maximum is $26\ \mathrm{ms}$ for a
  30 Hz Ricker ($1/f_0 = 33\ \mathrm{ms}$). Any thickness estimate from the
  envelope width must deconvolve the wavelet's own width first.

### 3.2 Vertical resolution: the $\lambda/4$ criterion

Two reflections separated by two-way time $\Delta t$ produce, at the receiver,
the sum of two wavelets. When $\Delta t$ is smaller than about half the dominant
period, the two wavelets overlap and the composite is a single broader event;
the individual reflections can no longer be separated by inspection. Writing
"about half the period" as $\Delta t \gtrsim 1/(2f_0)$ and using
$\Delta t = 2h/v$ for a bed of thickness $h$:

$$\frac{2h}{v} \gtrsim \frac{1}{2f_0}
\;\Longrightarrow\; h \gtrsim \frac{v}{4f_0} = \frac{\lambda}{4}.$$

So the **vertical resolution limit is $\lambda/4$**: beds thinner than a quarter
wavelength cannot be resolved by inspection of the waveform.

### 3.3 The tuning curve, measured

The composite amplitude of a thin bed varies with thickness in a way that is
diagnostic. For a bed with equal and opposite reflection coefficients, the
composite is $R\left[w(t) - w(t-\Delta t)\right]$ with $\Delta t = 2h/v$. The
demonstration computes the maximum amplitude versus $h$ for
$v=3000\ \mathrm{m\,s^{-1}}$, $f_0=30\ \mathrm{Hz}$ ($\lambda = 100\
\mathrm{m}$, $\lambda/4 = 25\ \mathrm{m}$, $\lambda/8 = 12.5\ \mathrm{m}$):

| $h$ (m) | $\Delta t$ (ms) | composite peak amplitude |
|---|---|---|
| 2 | 1.3 | 0.2424 |
| 4 | 2.7 | 0.4776 |
| 8 | 5.3 | 0.8988 |
| 12.5 | 8.3 | 1.2465 |
| 20 | 13.3 | **1.4331** |
| 25 | 16.7 | 1.3467 |
| 40 | 26.7 | 1.0043 |
| 50 | 33.3 | 0.9896 |

Three measured facts:

1. **The amplitude maximum is at $h = 20\ \mathrm{m}$, not $\lambda/4 = 25\
   \mathrm{m}$** — about 20% lower. The $\lambda/4$ figure is a *rule of thumb*
   derived from an idealised wavelet; a Ricker's tuning peak falls earlier. Quote
   the rule of thumb as an order and the measurement for a number.
2. **For very thin beds the amplitude grows roughly linearly with thickness**:
   $h=2\to4\ \mathrm{m}$ multiplies the amplitude by 1.97. This is the *Widess
   regime*: the composite is, in the limit, the derivative of the wavelet, so
   its amplitude is proportional to $\Delta t$ (hence to $h$). Thickness *can*
   therefore be estimated from amplitude below $\lambda/8$ — an exception to the
   resolution limit, but an amplitude-based one, not a waveform-separation one.
3. **Past tuning the amplitude falls again** ($h=20\to40\ \mathrm{m}$: ×0.70) as
   the two wavelets separate and destructively interfere at the composite peak.

### 3.4 Detection versus resolution, measured

Whether a bed is *detected* depends on its impedance contrast, not on
$\lambda/4$. Using a noise rms of $0.05$ per survey and a $3\sigma$ difference
floor of $3\sqrt{2}(0.05) = 0.212$, the demonstration finds:

| thickness (m) | contrast 0.05 | contrast 0.15 | contrast 0.30 |
|---|---|---|---|
| 2 | 0.0121 no | 0.0364 no | 0.0727 no |
| 5 | 0.0295 no | 0.0885 no | 0.1771 no |
| 10 | 0.0536 no | 0.1609 no | 0.3218 **yes** |
| 20 | 0.0717 no | 0.2150 **yes** | 0.4299 **yes** |

A $10\ \mathrm{m}$ bed ($0.4\lambda/4$) is detected at contrast 0.30; a
$20\ \mathrm{m}$ bed (still below the $\lambda/4$ tuning thickness) at contrast
0.15. Conversely, a bed thicker than $\lambda/4$ can be *resolvable in principle*
and yet fall below the noise if its contrast is small enough. **Detection is a
contrast question; resolution is a wavelength question.** Conflating them produces
both false negatives ("there is no thin bed, because thin beds are unresolvable")
and false positives.

### 3.5 Horizontal resolution: the Fresnel zone

At zero offset the energy that reaches a point reflector also reaches a
surrounding area, because the path lengths differ by less than half a wavelength
within a radius $r_f$. Setting the path difference to $\lambda/2$ gives

$$\sqrt{r_f^{2}+z^{2}} - z \approx \frac{r_f^{2}}{2z} = \frac{\lambda}{2}
\;\Longrightarrow\; r_f \approx \sqrt{\frac{\lambda z}{2}}.$$

The radius grows as $\sqrt{z}$, so deeper reflectors have coarser horizontal
resolution:

| depth $z$ (m) | $\lambda$ (m) | $r_f$ (m) |
|---|---|---|
| 500 | 100 | 158.1 |
| 1000 | 100 | 223.6 |
| 2000 | 100 | 316.2 |
| 4000 | 100 | 447.2 |

A fault or a channel narrower than the Fresnel zone cannot be resolved
horizontally no matter how it is processed — *before* migration. **Migration
narrows the effective horizontal resolution** toward $\lambda/4$ in the best
cases, which is why migration is said to "reduce the Fresnel zone", but it does
not remove the $\sqrt{z}$ scaling of the underlying physics or the requirement
for adequate aperture.

### 3.6 Spectral decomposition: resolution as a function of frequency

Because resolution scales with wavelength, a *single* seismic volume has a
*range* of resolutions. **Spectral decomposition** makes this explicit by
producing band-limited volumes centred on different frequencies; each reveals the
scale it is tuned to. Two uses follow:

- **Thickness estimation.** The frequency at which a thin bed's tuning amplitude
  peaks is diagnostic of its thickness: from the tuning relation, a bed of
  thickness $h$ tunes at $f \approx v/(4h)$ (using the $\lambda/4$ rule of thumb)
  or the measured equivalent. Mapping the peak-tuning frequency across a volume
  therefore maps thickness — with the same contrast caveat as Section 3.4.
- **Channel and lobe detection.** Low-frequency volumes emphasise thick,
  laterally continuous features; high-frequency volumes emphasise thin,
  discontinuous ones. A channel visible at 40 Hz but not at 15 Hz is a thin
  feature.

**The catch.** Spectral decomposition does not create bandwidth; it selects
sub-bands of the band that survives to the target depth. Because attenuation
removes high frequencies preferentially (lesson 02), the useful decomposition
band narrows with depth, and the "resolution at depth" is worse than the
source wavelet suggests. Any thickness map from spectral decomposition should
state the frequencies actually present at the target, not the source band.

### 3.7 Which attribute for which question

A short decision table, offered as guidance rather than a rule:

| task | appropriate attribute | inappropriate, and why |
|---|---|---|
| map faults | coherency / discontinuity | amplitude — a fault may not change impedance |
| estimate thickness | amplitude or tuning frequency | instantaneous phase — no thickness information |
| detect a channel | envelope, spectral sub-bands | coherency — a channel interior can be coherent |
| pick a horizon for structure | instantaneous phase | envelope — too broad to pick precisely |
| detect fluid | amplitude (calibrated), AVO | coherency — geometric, not petrophysical |

The last row is the important one: attributes that answer *geometric* questions
cannot answer *petrophysical* ones, and vice versa. A frequent interpretive error
is to use a geometric attribute as evidence about lithology or fluid.

## 4. Physical interpretation

- **Attributes are not data.** They are nonlinear-ish transforms of a band-limited
  signal; each amplifies some features and some noise.
- **Vertical resolution is set by bandwidth, horizontal by geometry (and then by
  migration).** They scale differently with depth and must not be conflated.
- **Tuning is a diagnostic, not a nuisance.** The amplitude-versus-thickness curve
  is monotonic only below the tuning thickness; above it, the ambiguity between
  "thick bed" and "thin bed" is real and must be resolved with other information.
- **The Widess regime is a gift with a catch.** Amplitude can estimate thickness
  below $\lambda/8$, but only if the wavelet and the contrast are known well
  enough.

## 5. Assumptions

1. **A known wavelet.** All amplitude-based thickness estimates require it; an
   unknown wavelet phase (Section 3.3 of [01](01-reflection-principle.md)) biases
   them.
2. **A single isolated bed** for the tuning analysis. Multiple interfering beds
   produce composite tuning curves that cannot be inverted uniquely.
3. **Band-limited data with a well-defined $f_0$.** Broadband data have no single
   $\lambda$; the resolution is then frequency-dependent.
4. **Zero-offset (or migrated) geometry** for the Fresnel formula.
5. **Correctly scaled amplitudes.** Attributes inherit every amplitude error of
   the processing.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $\lambda$ | m | $\mathrm{(m\,s^{-1})/s^{-1}}$ |
| $h$, $z$ | m | |
| $r_f$ | m | $\sqrt{\mathrm{m\cdot m}}$ ✔ |
| $E$ | same as trace | |
| $f$ | Hz | $\mathrm{rad\,s^{-1}}$ if not divided by $2\pi$ |
| $\Delta t$ | s | |

The Fresnel formula is a useful dimensional check: $\lambda z$ has units of
$\mathrm{m^{2}}$, and its square root is a length.

## 7. Worked examples

### Example 1 — resolution scales at two frequencies

$v = 3000\ \mathrm{m\,s^{-1}}$. At $f_0 = 20\ \mathrm{Hz}$:
$\lambda = 150\ \mathrm{m}$, $\lambda/4 = 37.5\ \mathrm{m}$. At
$f_0 = 50\ \mathrm{Hz}$: $\lambda = 60\ \mathrm{m}$, $\lambda/4 = 15\ \mathrm{m}$.
Doubling the bandwidth's dominant frequency halves the resolution scale — but
only if the higher frequencies survive to depth. Overburden attenuation is
frequency-selective, so the *effective* bandwidth narrows with depth and the
resolution degrades even though the nominal wavelet did not change.

### Example 2 — a bed thinner than $\lambda/4$ but detectable

$v = 3000\ \mathrm{m\,s^{-1}}$, $f_0 = 30\ \mathrm{Hz}$: $\lambda/4 = 25\
\mathrm{m}$. A $10\ \mathrm{m}$ bed at contrast 0.30 has composite amplitude
0.3218, well above the noise floor of 0.212 — detectable, and its thickness can
be estimated from the amplitude via the Widess linear regime, provided the
contrast is known. If instead the contrast is 0.05 (amplitude 0.0536), the bed is
invisible. **Same thickness, opposite conclusions.**

### Example 3 — Fresnel zone versus fault throw

A fault with 20 m throw at 2 km depth is a *vertical* feature and is limited by
$\lambda/4 = 25\ \mathrm{m}$ (so 20 m is at the edge of resolution). The
*horizontal* position of the fault is limited by the Fresnel zone, $r_f = 316\
\mathrm{m}$ before migration. These are different limits on different
geometries; a fault can be clearly visible yet laterally misplaced by a few
hundred metres if migration is poor.

## 8. Python demonstration

`code/attributes_demo.py`:

1. computes the envelope, instantaneous phase and frequency of a 30 Hz Ricker,
   reporting $E=1.0000$ at the peak, an instantaneous frequency of
   $33.81\ \mathrm{Hz}$ (not the nominal 30 Hz) and an envelope FWHM of
   $26\ \mathrm{ms}$;
2. computes the tuning curve for $v=3000\ \mathrm{m\,s^{-1}}$,
   $f_0=30\ \mathrm{Hz}$ and locates the amplitude maximum at $h=20\ \mathrm{m}$
   against the $\lambda/4$ rule of thumb of 25 m;
3. builds a detection table as a function of thickness and contrast against a
   stated noise floor;
4. tabulates the Fresnel radius to 4 km depth.

## 9. Exercises

Full sets are in
[`exercises/07-seismic-attributes-exercises.md`](./exercises/07-seismic-attributes-exercises.md)
and
[`exercises/07-seismic-attributes-solutions.md`](./exercises/07-seismic-attributes-solutions.md).

- **★** Compute $\lambda$, $\lambda/4$, $\lambda/8$ for $v=2600\
  \mathrm{m\,s^{-1}}$, $f_0=25\ \mathrm{Hz}$.
- **★★** Derive $r_f\approx\sqrt{\lambda z/2}$ from the half-wavelength path
  criterion.
- **★★** Explain, with numbers, why a 6 m bed at high contrast may be detected
  while a 30 m bed at low contrast is not.
- **★★★** Design a workflow to estimate the thickness of a bed thinner than
  $\lambda/4$ and state every assumption it requires.

## 10. Common mistakes

1. **Reporting an attribute map without its artefact.** Instantaneous frequency
   in low-amplitude zones is meaningless; coherency at the edges of a limited
   window is unreliable.
2. **Using $\lambda/4$ as an exact number.** The measured tuning peak sits ~20%
   lower for a Ricker.
3. **Conflating detection with resolution.** They answer different questions.
4. **Assuming migration removes the Fresnel limit entirely.** It improves
   horizontal resolution but the aperture and velocity errors bound the gain.
5. **Forgetting attenuation.** The effective frequency at depth is lower than at
   the source, so resolution degrades with depth even for a fixed wavelet.

## 11. Real-world applications

- **Reservoir thickness and net-to-gross.** Tuning-curve analysis and its limits
  are central to estimating reservoir thickness from seismic (outside wells).
- **Fault and fracture detection.** Coherency and curvature attributes map
  discontinuities; their lateral precision is set by the Fresnel zone and by
  migration.
- **Channel and stratigraphic interpretation.** The same limits govern whether
  a channel's edges are sharp in the image or blurred.
- **Time-lapse difference attributes.** 4-D signal detection (lesson 08) uses the
  same detection-versus-resolution logic, with the noise floor supplied by
  repeatability rather than by data noise.

## 12. Further reading

- **Widess, M. B. (1973). How thin is a thin bed? *Geophysics*, 38(6),
  1176–1180.** Level: research. The classic limit.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Level: intermediate. Resolution and attributes.
- **Taner, M. T., Koehler, F., & Sheriff, R. E. (1979). Complex seismic trace
  analysis. *Geophysics*, 44(6), 1041–1063.** Level: research. The
  complex-trace attributes.
- **Chopra, S., & Marfurt, K. J. (2007). *Seismic Attributes for Prospect
  Identification and Reservoir Characterization*. Society of Exploration
  Geophysicists.** Level: intermediate to advanced. Practical attribute
  interpretation.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Confirm current editions through
> your library.

## 13. Related lessons

- [01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](01-reflection-principle.md).
- [04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM](04-migration-imaging.md).
- [08 Time-Lapse (4-D) Seismic and Reservoir Monitoring](08-4d-seismic.md) — the
  detection-versus-resolution logic applied to difference data.
- [05-01-03 The Resolution–Depth Trade-off](../../05-core-geophysics/01-what-geophysics-measures/03-resolution-depth-tradeoff.md) —
  the general principle.

## 14. Self-assessment checklist

- [ ] I can compute the three complex-trace attributes and state their pitfalls.
- [ ] I can derive the $\lambda/4$ vertical resolution criterion.
- [ ] I can explain the Widess $\lambda/8$ limit and the linear amplitude regime.
- [ ] I can distinguish detection from resolution with a numerical example.
- [ ] I can derive and apply the Fresnel-zone formula.
- [ ] I can state which limit applies to a vertical versus a lateral feature.
