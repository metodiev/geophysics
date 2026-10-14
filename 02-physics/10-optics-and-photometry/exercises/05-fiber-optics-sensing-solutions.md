# Solutions — 02-10-05 Fibre-Optic Sensing and Distributed Acoustic Sensing

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Loss budget

**(a)** $0.20\ \mathrm{dB\,km^{-1}}\times25\ \mathrm{km} = \mathbf{5.00}$ **dB**.

**(b)** Round trip $= 2\times5.00 = \mathbf{10.00}$ **dB**.

**(c)** One way: $10^{-5/10} = \mathbf{0.3162}$ (31.6 per cent). Round trip:
$10^{-10/10} = \mathbf{0.1000}$ (10.0 per cent). A distributed measurement on a
25 km fibre therefore receives, in the best case, one tenth of the power it
launched, before the backscatter's own 70–80 dB penalty is applied.

**(d)** Scaling the Rayleigh component by $(1550/1310)^4 = 1.960$:
$\alpha \approx 0.20\times1.960 = \mathbf{0.392}$ **dB km⁻¹**. The assumption is
only approximately true because the *measured* loss is the sum of Rayleigh
scattering and infrared absorption, and the two have opposite wavelength
dependences: absorption is negligible at 1310 nm (so the total there is almost
pure Rayleigh) but not at 1550 nm, where the tail of the infrared absorption edge
contributes. Scaling the *total* loss by $\lambda^{-4}$ therefore overestimates
the 1310 nm loss somewhat, and the correct statement is "the Rayleigh
contribution scales as $\lambda^{-4}$".

---

## ★2 — Resolution and sampling

**(a)** $v = c/n_g = 2.997\,924\,58\times10^8/1.4682
= \mathbf{2.0419\times10^8}$ **m s⁻¹**.

**(b)** $\Delta z = vW/2 = 2.0419\times10^8\times40\times10^{-9}/2
= \mathbf{4.084}$ **m**.

**(c)** One sample interval is 4 ns, corresponding to a one-way distance of
$v\times4\times10^{-9}/2 = \mathbf{0.408}$ **m**. The sampling is ten times finer
than the pulse, i.e. the measurement is heavily oversampled: the useful
resolution is set by the pulse (4.08 m) and the fine sampling only smooths the
pulse's own shape. This is deliberate — oversampling lets the channel positions
be interpolated to a common grid, which matters when combining several gauges.

**(d)** Round trip for 10 km $= 2\times10^4/2.0419\times10^8
= 9.795\times10^{-5}$ s $= \mathbf{97.95\ \mu s}$, so the maximum pulse
repetition frequency is
$f_{\text{prf}} = 1/97.95\ \mu s = \mathbf{10\,209.5}$ **Hz**.

---

## ★3 — V number and mode count

**(a)** $V = \dfrac{2\pi a}{\lambda}\mathrm{NA}
= \dfrac{2\pi\times4.1\times10^{-6}}{1.55\times10^{-6}}\times0.14
= 16.622\times0.14 = \mathbf{2.3268}$.

**(b)** $V = 2.3268 < 2.4048$, so the fibre is **single-mode** at 1550 nm — but
only just: the margin is 3.2 per cent, which means any excursion to a shorter
wavelength (a pump laser at 1480 nm, for example, gives
$V = 2.3268\times1550/1480 = 2.437$) pushes it multimode.

**(c)** $\lambda_c = \dfrac{2\pi a\,\mathrm{NA}}{2.4048}
= \dfrac{2\pi\times4.1\times10^{-6}\times0.14}{2.4048}
= 1.4997\ \mu\mathrm m = \mathbf{1499.7}$ **nm**. Operating at 1550 nm is above
the cutoff, so single mode ✓.

**(d)** At 800 nm, $V = 2.3268\times1550/800 = 4.508$, so
$M \approx V^2/2 = \mathbf{10.2}$ modes, i.e. of order ten spatial modes. The
consequence is practical rather than theoretical: if the fibre is used with a
visible or 800 nm alignment laser, the light propagates multimodally, and the
alignment does not represent the 1550 nm mode field. Use a 1550 nm source for
alignment, or accept the mode mismatch.

---

## ★4 — Phase from strain

**(a)** Using the demo's sensitivity
$\Delta\phi/L = 4.6208\times10^6\ \mathrm{rad\,m^{-1}}$ per unit strain:

$$\Delta\phi = 4.6208\times10^6\times20\times200\times10^{-9}
= \mathbf{18.4832}\ \textbf{rad} .$$

**(b)** $18.4832\times180/\pi = \mathbf{1059.0°}$ — nearly three full cycles of
phase.

**(c)** $\Delta\phi = 2\pi\,\Delta(nL)/\lambda$, so

$$\Delta(nL) = \frac{\Delta\phi\,\lambda}{2\pi}
= \frac{18.4832\times1.55\times10^{-6}}{2\pi}
= 4.560\times10^{-6}\ \mathrm m = \mathbf{4.560}\ \mu\mathrm m .$$

For comparison, the geometric elongation alone is
$L\epsilon = 20\times200\times10^{-9} = 4.000\ \mu$m and the pure length term in
the optical path is $nL\epsilon = 1.4504\times4.000 = 5.802\ \mu$m. The
difference between 5.802 and 4.560 µm is the strain-optic contribution: the index
*decreases* under axial strain and cancels 21.4 per cent of the geometric
effect. Ignoring that term would overestimate the phase by 27 per cent.

**(d)** 18.5 rad is enormous by interferometric standards: a shot-noise-limited
coherent receiver resolves phase to milliradians, so this is a signal-to-noise
ratio of order $10^4$ on a single pulse. The implication is that the limiting
factor for DAS is not sensitivity but **dynamic range and phase unwrapping**: a
near-field earthquake can produce hundreds of radians over one gauge, which the
interrogator must unwrap continuously or the record clips.

---

## ★5 — Reading the demo

**(a)** The geometric estimate is $S \sim 1.9663\times10^{-3}$; the demo adopts
$S = 1.5\times10^{-3}$.

**(b)** For a 10 ns pulse, **−71.52 dB** at 0 km and **−75.52 dB** at 10 km.

**(c)** $\xi = \mathbf{0.785\,921}$ and
$\Delta\phi/L = \mathbf{4.6208\times10^6}$ **rad m⁻¹ per unit strain**.

**(d)** $S_{\text{geometric}}$ is *derived* from the numerical aperture by a
solid-angle argument; the adopted $S = 1.5\times10^{-3}$ is a *parameter* taken
from practice, because Rayleigh scattering in glass is anisotropic, the modes
have polarisation structure, and the effective capture depends on the fibre's
profile. The distinction matters because a derived quantity can be checked and a
parameter must be measured: an error in $S$ propagates directly into every
absolute amplitude and into every range budget, whereas an error in $\xi$
propagates into every strain result. Both must be traceable, and a paper that
presents an adopted parameter as if it were derived is not reproducible.

---

## ★6 — The gauge transfer function

**(a)** First null at $\Lambda = L$, i.e.
$f_{\text{null}} = v/L = 2500/15 = \mathbf{166.7}$ **Hz**.

**(b)** $f_{3\,\mathrm{dB}} = \dfrac{x_3v}{\pi L}$ with
$x_3 = 1.391\,557$ (the solution of $\operatorname{sinc}x = 1/\sqrt2$):

$$f_{3\,\mathrm{dB}} = \frac{1.391557\times2500}{\pi\times15}
= \mathbf{73.82}\ \textbf{Hz} .$$

**(c)** With $L = 5$ m: null at $2500/5 = \mathbf{500.0}$ **Hz** and
$f_{3\,\mathrm{dB}} = \mathbf{221.5}$ **Hz**.

**(d)** At the null the response is **exactly zero**: the gauge averages equal
positive and negative contributions and the channel reports no strain at all.
No correction can recover the signal because the information was never recorded
— it was destroyed by the spatial averaging before the detector saw it. This is
the difference between a filter that attenuates (recoverable, up to noise) and a
filter that nulls (information destroyed). The only remedy is a shorter gauge
length, which is a different experiment.

---

## ★7 — Aliasing

**(a)** $k_{\max} = \pi/\Delta x = \pi/2 = \mathbf{1.5708}$ **rad m⁻¹**.

**(b)** $f_{\max} = v/(2\Delta x)$: **300 Hz** at 1200 m s⁻¹ and **750 Hz** at
3000 m s⁻¹.

**(c)** With $\Delta x = 0.5$ m, $k_{\max} = \mathbf{6.2832}$ rad m⁻¹ and
$f_{\max}$ = **1200 Hz** at 1200 m s⁻¹ and **3000 Hz** at 3000 m s⁻¹.

**(d)** The required spacing is
$\Delta x \le v/(2f) = 1200/(2\times700) = \mathbf{0.857}$ **m**, so the channel
spacing (a configuration parameter) must be reduced — the gauge length does not
help, because it is a different parameter with a different effect (it filters and
nulls, but does not alias). Reducing the channel spacing changes the number of
channels and the data rate; changing the gauge length changes the amplitude and
phase response. The two are set independently and neither substitutes for the
other.

---

## ★8 — Temperature cross-sensitivity

**(a)** **10.35 µε K⁻¹**

**(b)** $47.82\ \mathrm{rad\,m^{-1}K^{-1}}\times10\ \mathrm m\times0.1\ \mathrm K
= \mathbf{47.82}$ **rad** over a 10 m gauge.

**(c)** $10.35\times5 = \mathbf{51.75}$ **µε** of apparent strain, i.e.
$5.175\times10^{-5}$ strain.

**(d)** Any seismic measurement in which the true strain is smaller than
$5\times10^{-5}$ — which is essentially every seismic measurement, since typical
seismic strains are $10^{-9}$ to $10^{-7}$. The daily temperature signal is two
to four orders of magnitude larger than the seismic signal on a shallow,
thermally coupled cable. Mitigations: a strain-free reference fibre in the same
cable to measure the thermal contribution and subtract it; a cable design that
mechanically decouples the fibre from thermal expansion (loose tube, or a
low-thermal-expansion jacket); or restricting the analysis to burial depths and
frequency bands where the thermal signal is small. A purely analytical mitigation
(high-pass filtering) is the weakest of the three, because the thermal and
seismic spectra overlap at low frequency.

---

## ★★★9 — Point-difference gauge response

**(a)** For a strain field $\epsilon(x) = \epsilon_0\sin(kx)$, a channel formed
as the *difference of the strains at two points* separated by $L$ reports

$$D(x) = \epsilon(x+L/2)-\epsilon(x-L/2)
= 2\epsilon_0\sin(kL/2)\cos(kx) ,$$

using $\sin A-\sin B = 2\cos\!\frac{A+B}{2}\sin\!\frac{A-B}{2}$. Its amplitude is
therefore $\propto|\sin(kL/2)|$. The boxcar (sinc) response of the lesson arises
when the channel reports the *average over a continuous section of length $L$*,
$D \propto \int_{x-L/2}^{x+L/2}\cos(kx')\,\mathrm dx' \propto
\operatorname{sinc}(kL/2)$. The distinguishing assumption is whether the
interrogator differences two discrete points (a two-point or "differential"
gauge) or integrates over a continuous section (an average gauge); real
interrogators are closer to the former, which is why the sinc description is an
idealization that should be calibrated.

**(b)** The first null of $|\sin(kL/2)|$ is at $kL/2 = \pi$, so
$k = 2\pi/L = 0.6283$ rad m⁻¹ and $\Lambda = L = 10$ m, giving
$f_{\text{null}} = v/L = \mathbf{300}\ \mathrm{Hz}$ — the same first null as the
boxcar model, because both are governed by the same length $L$.

**(c)** At half the null frequency, $kL/2 = \pi/2$: the point-difference model
gives $|\sin(\pi/2)| = \mathbf{1.000}$ and the boxcar gives
$|\operatorname{sinc}(\pi/2)| = |\sin(\pi/2)/(\pi/2)| = \mathbf{0.6366}$. The
point-difference model predicts a **larger** response — 57 per cent larger at
that frequency — so applying the wrong model over-corrects the amplitudes in the
band between 3 dB and the null.

**(d)** Because the two models differ by up to 57 per cent in the passband and by
a factor in the stopband, and the difference is not a constant that can be
absorbed into a calibration factor. The correct model must be established by a
**controlled calibration**: inject a known, frequency-variable strain (a
piezoelectric stack or a shaker on a bonded section of fibre, or a known
vibrating wire) at several frequencies spanning the band and measure the
response; fit the model; and report the fitted transfer function with the survey.
Without that, any quoted DAS amplitude is an uncalibrated number.

---

## ★★★10 — The phase-to-strain relation

**(a)** With $\phi = 2\pi nL/\lambda$,

$$\frac{\Delta\phi}{\phi}
= \frac{\Delta L}{L}+\frac{\Delta n}{n} .$$

The first term is the geometric elongation, $\Delta L/L = \epsilon$. The second is
the strain-optic (photoelastic) effect: for light polarised transverse to the
strain axis, the index change is

$$\Delta n = -\frac{n^3}{2}\left[p_{12}-\nu(p_{11}+p_{12})\right]\epsilon ,$$

where $p_{11}$ and $p_{12}$ are the Pockels (photoelastic) coefficients of the
glass, $\nu$ is Poisson's ratio (which converts the applied axial strain into the
transverse strains the light samples), and the bracket is the net effect of the
two principal directions on the transverse polarisation. Substituting,

$$\frac{\Delta\phi}{\phi}
= \epsilon\left\{1-\frac{n^2}{2}\left[p_{12}-\nu(p_{11}+p_{12})\right]\right\}
\equiv \xi\epsilon .$$

Physically: the fibre gets longer (which increases the phase) but also less
dense and less polarisable along the strain axis (which decreases the index and
partially cancels the first effect).

**(b)**
$\xi = 1-\frac{1.4504^2}{2}\left[0.270-0.17(0.121+0.270)\right]
= 1-1.0518\times0.20353 = 1-0.21407 = \mathbf{0.7859}$.

**(c)** Ignoring the strain-optic effect would give $\xi = 1$, i.e. a
$\dfrac{1}{0.7859}-1 = \mathbf{0.272}$ = **27.2 per cent** overestimate of the
phase change, and therefore a 27 per cent underestimate of the strain inferred
from a measured phase. That is not a small correction; it is of the same order as
the difference between two plausible rock moduli.

**(d)** For a compliant fibre perfectly bonded into a stiff formation, the strain
is partitioned by the stiffnesses: if the fibre's modulus is much smaller than
the formation's, the fibre takes essentially the formation strain, and the
formation takes $\sim E_{\text{soft}}/E_{\text{stiff}} = 1/10$ of the far-field
strain in a uniaxial, equal-stress configuration. The fibre therefore sees about
$\mathbf{0.1}$ of the far-field strain, and the inferred formation strain is ten
times the phase-derived value. The assumption is that the fibre is a
*compliant inclusion* — its own mechanical stiffness is negligible compared with
the host — and that the deformation is uniaxial, elastic and perfectly coupled
(no slip, no debonding, no grout compliance). A proper treatment uses inclusion
or shear-lag theory, and in practice the coupling is measured with a downhole
comparison against a reference sensor, because a factor-of-ten amplitude error is
otherwise easily mistaken for a difference in formation properties.

---

## ★★★11 — Designing a DAS survey

**(a)** $f_{\text{prf}} = \dfrac{v}{2L}
= \dfrac{2.0419\times10^8}{2\times12\times10^3} = \mathbf{8507.9}$ **Hz**;
temporal Nyquist $= \mathbf{4254.0}$ **Hz**.

**(b)** Spatial Nyquist $= v/(2\Delta x)$: at 2000 m s⁻¹ with $\Delta x = 1$ m,
**1000 Hz**; at 4000 m s⁻¹, **2000 Hz**.

**(c)** For a 250 Hz wave at 500 m s⁻¹, the wavelength is 2 m and the required
channel spacing is

$$\Delta x \le \frac{v}{2f} = \frac{500}{2\times250} = \mathbf{1.0\ m} .$$

For the gauge length, setting the 3 dB frequency to 250 Hz:

$$L = \frac{x_3v}{\pi f_{3\,\mathrm{dB}}}
= \frac{1.391557\times500}{\pi\times250} = \mathbf{0.886\ m} .$$

Both requirements are at or below 1 m, which is a demanding but feasible
configuration.

**(d)** Two practical obstacles. First, gauge lengths approaching or below 1 m
require pulse widths of order 10 ns or less, which reduce the backscattered
signal: from ★5, a 10 ns pulse already returns 71.5 dB below the launch, and
halving the pulse costs another 3 dB. The trade is signal-to-noise against
spatial resolution. Second, 12 km of fibre at 1 m spacing is 12 000 channels at
4254 Hz — of order $10^8$ samples per second before any processing — which is a
substantial data-rate and storage burden; the usual accommodation is to decimate
the channels after beam-forming, or to shorten the fibre, or to accept a shorter
gauge and a longer channel spacing with the aliasing that implies. The general
principle is that DAS design is a three-way trade among spatial resolution,
temporal bandwidth and signal-to-noise, and no two can be improved without
costing the third.
