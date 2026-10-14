# Solutions — 06-13-02 Glacial and Cryoseismology: Icequakes and Calving

The lesson is [02 Glacial and Cryoseismology](../02-glacial-seismology.md). All
models are **SYNTHETIC**.

## ★ Foundational

**★1.** With $E = 9.0\times10^{9}\ \mathrm{Pa}$, $\nu = 0.33$,
$\rho = 920\ \mathrm{kg\,m^{-3}}$:

$$G = \frac{E}{2(1+\nu)} = \frac{9.0\times10^{9}}{2.66}
= 3.3835\times10^{9}\ \mathrm{Pa}, \qquad
K = \frac{E}{3(1-2\nu)} = \frac{9.0\times10^{9}}{1.02}
= 8.8235\times10^{9}\ \mathrm{Pa},$$

$$V_s = \sqrt{\frac{G}{\rho}} = \sqrt{\frac{3.3835\times10^{9}}{920}}
= 1917.7\ \mathrm{m\,s^{-1}},$$

$$V_p = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}
= \sqrt{\frac{8.8235\times10^{9} + 4.5113\times10^{9}}{920}}
= \sqrt{1.44944\times10^{7}} = 3807.2\ \mathrm{m\,s^{-1}},$$

so $V_p/V_s = 3807.2/1917.7 = 1.985$. Unit check:
$\sqrt{\mathrm{Pa}/(\mathrm{kg\,m^{-3}})} =
\sqrt{\mathrm{kg\,m^{-1}\,s^{-2}}/(\mathrm{kg\,m^{-3}})} =
\sqrt{\mathrm{m^{2}\,s^{-2}}} = \mathrm{m\,s^{-1}}$.

**★2.**
$$\frac{\mathrm{d}V_s}{\mathrm{d}T} = -\frac{\gamma_T V_s}{2}
= -\frac{3.0\times10^{-3} \times 1917.7}{2}
= -2.877\ \mathrm{m\,s^{-1}\,K^{-1}},$$
and over $30\ \mathrm{K}$:
$$\frac{\Delta V_s}{V_s} = -\frac{\gamma_T \Delta T}{2}
= -\frac{3.0\times10^{-3} \times 30}{2} = -4.5\times10^{-2} = -4.5\%.$$
(The exact expression is $\sqrt{1 - \gamma_T\Delta T} - 1 = -4.61\%$; the tangent
and the exact value differ by the curvature of the square root, which is the
point of using a *linearised* coefficient only over a small range.)

**★3.** The limits are $c \to \beta_2$ at low frequency (long wavelengths sample
mostly the substrate, which therefore controls the phase velocity) and
$c \to \beta_1$ at high frequency (short wavelengths are confined to the slow
layer). For $H = 1000\ \mathrm{m}$ and $f = 0.2\ \mathrm{Hz}$ with
$\beta_2 \approx 3000\ \mathrm{m\,s^{-1}}$, the wavelength is
$\lambda \approx 3000/0.2 = 15\,000\ \mathrm{m} = 15H$: far in the long-wavelength
limit, so $c$ is close to $\beta_2$ and the measurement has little sensitivity to
$H$.

## ★★ Applied

**★★4.**
$$\frac{\mu_2}{\mu_1} = \frac{2600 \times 2800^{2}}{917 \times 1800^{2}}
= \frac{2.0384\times10^{10}}{2.9711\times10^{9}} = 6.861,$$
and the fundamental Love mode requires $\beta_1 < c < \beta_2$, i.e.
$1800 < c < 2800\ \mathrm{m\,s^{-1}}$. At $1\ \mathrm{Hz}$ with
$c = 2000\ \mathrm{m\,s^{-1}}$:
$$\lambda = \frac{c}{f} = 2000\ \mathrm{m}, \qquad
\frac{\lambda}{H} = \frac{2000}{800} = 2.5,$$
i.e. the wavelength is two and a half times the layer thickness — inside the
transition, which is where the thickness information is concentrated.

**★★5.** **(a)** The accepted family is narrow: $H$ is determined to
$\pm 50\ \mathrm{m}$ at the true $\beta_1$, and the *entire* family disappears
when $\beta_1$ is wrong by $5\%$. So the dispersion curve constrains the layer
velocity strongly enough that a $5\%$ velocity error cannot be traded away by any
thickness (the demonstration measures the same for a $1\%$ rms slowness tolerance
over a band bracketing the transition). The trade-off exists in the mathematics
but is narrow in this band, and the honest description is "the two parameters are
tightly determined, jointly, given the substrate".

**(b)** Letting $\beta_2$ vary introduces a third parameter that enters the
dispersion relation directly: a faster substrate mimics a thinner layer at long
wavelengths, because both push the low-frequency branch upward. So the family
must widen — the previous result was conditional on a *fixed* substrate, and that
fixing, not the data, was what removed the extra freedom. This is why the lesson
insists that "the substrate is assumed known" is part of the result rather than a
separate caveat.

**★★6.** With $H = 1200\ \mathrm{m}$ and $t = 0.6280\ \mathrm{s}$:
$$V_s = \frac{H}{t} = \frac{1200}{0.6280} = 1910.8\ \mathrm{m\,s^{-1}} .$$
A time shorter by $10\ \mathrm{ms}$ ($t' = 0.6180\ \mathrm{s}$) at fixed $H$ gives
$$V_s' = \frac{1200}{0.6180} = 1941.7\ \mathrm{m\,s^{-1}},$$
a change of $+30.9\ \mathrm{m\,s^{-1}}$, i.e. $+1.62\%$. With
$\mathrm{d}V_s/\mathrm{d}T = -2.9\ \mathrm{m\,s^{-1}\,K^{-1}}$, the implied
temperature change is $\Delta T = -30.9/2.9 = -10.7\ \mathrm{K}$ — a *cooling* of
about $11\ \mathrm{K}$ to explain $10\ \mathrm{ms}$. That is a large temperature
change for an ice column but not impossible near the surface; more importantly, a
$1\%$ thickness error ($12\ \mathrm{m}$) produces the same $10\ \mathrm{ms}$, so a
single travel time cannot separate the two and the conclusion would need the
differential (repeating-source) measurement of ★★★8 or an independent thickness.

## ★★★ Research-oriented

**★★★7. Design.**

- **Targets.** $H$ to $\pm 10\ \mathrm{m}$ ($\sim 1\%$ at $1\ \mathrm{km}$) and
  $\beta_1$ to $\pm 1\%$.
- **Geometry.** A linear array on the ice surface, aperture at least the longest
  wavelength of interest (aperture $> \lambda_{\max}$), with geophones or a fibre
  for dense sampling; source offsets spanning $0.2$ to $5\ H$.
- **Band.** Dispersion should bracket the transition, i.e. span
  $\lambda/H \sim 0.2$ to $\sim 5$. For $H = 1000\ \mathrm{m}$ and
  $\beta_1 \approx 1900\ \mathrm{m\,s^{-1}}$, that is roughly
  $0.4$ to $10\ \mathrm{Hz}$ — consistent with the lesson's demonstration band.
- **Sources.** Active: hammer/seismic source or explosive at the low-frequency end
  (needed for the long wavelengths); passive: icequakes and calving events, which
  supply the high-frequency end and the ambient-noise Green's functions.
- **Independent constraint.** A ground-penetrating radar profile for $H$ (metres
  accuracy, subject to a velocity assumption for the radio wave) and/or a
  borehole; a $P$-wave refraction profile to fix $V_p$ and hence $\nu$.
- **Synthetic test before the survey.** Forward-model the expected dispersion for
  the target model, then invert with the actual geometry, band and noise, and
  report the accepted family and its marginal widths (exactly the procedure of
  the lesson's demonstration). Include a known-wrong substrate to measure how
  much of the resolution that assumption is supplying.

**Which target is harder.** The **thickness** is harder, because
$\beta_1$ appears linearly in the forward model's high-frequency limit
($c \to \beta_1$), where the measurement is nearly a direct velocity reading,
while $H$ enters only through the *location* of the transition — a feature that
is broad in frequency and easily smeared by a firn layer, a soft bed, or a
laterally varying thickness. That asymmetry is why the lesson recommends using
radar for $H$ and dispersion for $\beta_1$.

**★★★8. Differential monitoring.**

From the lesson's §2, at $V_s = 1952.6\ \mathrm{m\,s^{-1}}$ the sensitivity is
$\mathrm{d}V_s/\mathrm{d}T \approx -2.9\ \mathrm{m\,s^{-1}\,K^{-1}}$, i.e. a
fractional change of $-2.9/1952.6 = -1.485\times10^{-3}$ per kelvin. Over a
$900\ \mathrm{m}$ path the travel time is $t = 900/1952.6 = 0.46092\ \mathrm{s}$,
so a warming $\Delta T$ produces

$$\Delta t = -1.485\times10^{-3}\,\Delta T \times t
= -6.845\times10^{-4}\,\Delta T\ \mathrm{s}.$$

For $\Delta T = 5\ \mathrm{K}$: $\Delta t = -3.42\ \mathrm{ms}$. For
$\Delta T = 1\ \mathrm{K}$: $\Delta t = -0.685\ \mathrm{ms}$ — so the timing
precision needed to detect a $1\ \mathrm{K}$ change is better than about
$0.7\ \mathrm{ms}$, which correlation on repeating events can deliver
(sub-millisecond), and hand picking cannot.

**The assumption.** That the source is *reproducible*: the two events have the
same waveform, the same position, and the same radiation pattern, so that any
change in the differential travel time is caused by the medium. Testing it:
compare the differential travel time between repeats at a *reference* station
close to the source — a source change appears at both stations, a medium change
appears only along the affected path; and monitor the waveform correlation
coefficient itself, since a source change degrades the similarity while a
velocity change only shifts it.
