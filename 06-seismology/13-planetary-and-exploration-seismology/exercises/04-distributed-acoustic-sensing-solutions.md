# Solutions — 06-13-04 Distributed Acoustic Sensing: A New Observational Regime

The lesson is [04 Distributed Acoustic Sensing](../04-distributed-acoustic-sensing.md).
All models are **SYNTHETIC**.

## ★ Foundational

**★1.** With $L/\lambda = 30/120 = 0.25$:
$$\mathrm{sinc}(\pi \times 0.25) = \frac{\sin(0.785398)}{0.785398}
= \frac{0.707107}{0.785398} = 0.900316,$$
so the amplitude loss is
$$20\log_{10}(0.900316) = 20 \times (-0.045605) = -0.912\ \mathrm{dB}.$$
Note the sign convention: $\mathrm{sinc}$ is positive here, so the gauge attenuates
without inverting the waveform. Inversion only begins past $L = \lambda$.

**★2.**
$$k = \frac{2\pi}{\lambda} = \frac{2\pi}{120} = 0.052360\ \mathrm{m^{-1}}, \qquad
k_{\text{Nyq}} = \frac{\pi}{d} = \frac{\pi}{20} = 0.157080\ \mathrm{m^{-1}} .$$
Since $k < k_{\text{Nyq}}$ (equivalently $d = 20\ \mathrm{m} < \lambda/2 =
60\ \mathrm{m}$), the array is **not aliased** and the measured wavenumber is the
true one.

**★3.**
$$|\varepsilon| = \frac{v_0}{c} = \frac{3.0\times10^{-5}}{600}
= 5.0\times10^{-8} \quad(-),$$
$$|\dot\varepsilon| = \omega|\varepsilon| = 2\pi f |\varepsilon|
= 2\pi \times 12 \times 5.0\times10^{-8} = 3.77\times10^{-6}\ \mathrm{s^{-1}} .$$
Units check: $\mathrm{m\,s^{-1}}/(\mathrm{m\,s^{-1}})$ is dimensionless, so strain
is dimensionless; multiplying by $\mathrm{s^{-1}}$ gives $\mathrm{s^{-1}}$ for the
rate.

## ★★ Applied

**★★4.** **(a)** The P-wave response is $\cos^{2}\theta$, so at $\theta =
40^{\circ}$ it is $\cos^{2}40^{\circ} = 0.7660^{2} = 0.5868$ — a $41\%$ amplitude
reduction (equivalently $20\log_{10}0.5868 = -4.63\ \mathrm{dB}$).

**(b)** An SH wave polarised perpendicular to the fibre gives **exactly zero**:
the strain component measured is
$\varepsilon_{xx} = \partial u_x/\partial x$, and this polarisation has
$u_x = 0$ everywhere and for all time, so the derivative vanishes identically.
The physical statement is that a wave displacing the ground across the fibre does
not change the fibre's length.

**(c)** The SV response is $\frac{1}{2}\sin 2\theta$, which is maximum at
$\theta = 45^{\circ}$ with value $\frac{1}{2}\sin 90^{\circ} = 0.5$. It vanishes
both along the fibre ($\theta = 0$) and broadside ($\theta = 90^{\circ}$),
because in both cases the SV displacement has no component along the fibre *or*
no gradient along it.

**★★5.** **(a)** With $c_{\text{app}} = 2500\ \mathrm{m\,s^{-1}}$ at
$f = 4\ \mathrm{Hz}$ and $\omega = 25.1327\ \mathrm{rad\,s^{-1}}$:
$$k_{\text{app}} = \frac{\omega}{c_{\text{app}}}
= \frac{25.1327}{2500} = 0.010053\ \mathrm{m^{-1}} .$$
Since $d = 30\ \mathrm{m}$ and $2\pi/d = 0.209440\ \mathrm{m^{-1}}$, the possible
true wavenumbers are $k = k_{\text{app}} + m(2\pi/d)$:

| $m$ | $k$ ($\mathrm{m^{-1}}$) | $c = \omega/k$ ($\mathrm{m\,s^{-1}}$) |
|---|---|---|
| 0 | $0.010053$ | $+2500.0$ |
| 1 | $0.219493$ | $+114.5$ |
| $-1$ | $-0.199386$ | $-126.1$ |
| 2 | $0.428932$ | $+58.6$ |

**(b)** All four are consistent with the observed $d = 30\ \mathrm{m}$ phase
differences; the two non-zero-velocity alternatives are a fast wave in the
expected band and a very slow wave (or a backward-propagating apparent wave)
that would normally be filtered out by other criteria.

**(c)** **Repeat the measurement at half the channel spacing** (or decimate the
existing data by two and re-measure): the true wave keeps its true velocity at
every spacing, whereas aliases move to different apparent velocities. A second,
independent check is the *physical plausibility* of each candidate against the
site's known dispersion (a $2500\ \mathrm{m\,s^{-1}}$ branch may be known from a
co-located array), but that is a consistency argument, not a measurement.

**★★6.** **(a)**
$$k_{\text{Nyq}} = \frac{\pi}{d} = \frac{\pi}{5} = 0.628319\ \mathrm{m^{-1}},
\qquad \text{temporal Nyquist} = \frac{500}{2} = 250\ \mathrm{Hz}.$$

**(b)** At $30\ \mathrm{Hz}$ with $c = 200\ \mathrm{m\,s^{-1}}$,
$\lambda = 200/30 = 6.667\ \mathrm{m}$, so
$$\frac{L}{\lambda} = \frac{20}{6.667} = 3.000
\;\Rightarrow\;
\mathrm{sinc}(3\pi) = \frac{\sin(9.4248)}{9.4248} \approx 0 .$$
The response is **exactly zero** ($L$ is an integer multiple of $\lambda$), so
this wave produces no signal at all on this configuration.

**(c)** Both parameters fail, but the **gauge length** is the binding constraint
in the strict sense that it nulls the wave: $L = 3\lambda$ gives a zero response,
whereas the channel spacing would merely alias it ($k = 2\pi/6.667 =
0.942478\ \mathrm{m^{-1}} > k_{\text{Nyq}} = 0.628319\ \mathrm{m^{-1}}$; also
$d = 5\ \mathrm{m} > \lambda/2 = 3.33\ \mathrm{m}$). An aliased wave is at least
present (in the wrong place); a nulled wave is absent. To record this target on
this fibre, $L$ must be reduced to $\lesssim 0.44 \times 6.667 = 2.9\ \mathrm{m}$
and $d$ to $< 3.33\ \mathrm{m}$.

## ★★★ Research-oriented

**★★★7. Specification.**

- **Channel spacing.** The shortest wavelength is $\lambda_{\min} =
  c_{\min}/f_{\max} = 200/15 = 13.3\ \mathrm{m}$, so
  $$d < \frac{\lambda_{\min}}{2} = 6.7\ \mathrm{m}
  \quad\Rightarrow\quad \boxed{d = 5\ \mathrm{m}} \ \text{(margin for the anti-alias filter)} .$$
- **Gauge length.** For a broadband objective, the measured optimum is
  $L \approx 0.4\lambda_{\min} = 5.3\ \mathrm{m}$; for a full-band narrowband
  objective, $L \lesssim 0.44\lambda_{\min} = 5.9\ \mathrm{m}$. Both land on
  $\boxed{L = 5\ \mathrm{m}}$ (i.e. $M = 1$ channel spacing — a legitimate and
  common configuration). If a smaller $d$ were used, $L$ would be set to
  $\sim 5\ \mathrm{m}$ independently of $d$.
- **Sample rate.** $f_s > 2 f_{\max} = 30\ \mathrm{Hz}$; with a practical margin
  of $4\times$ for the anti-alias filter and oversampling gains,
  $\boxed{f_s = 200\ \mathrm{Hz}}$ (or $250\ \mathrm{Hz}$ if the instrument's
  native rate is fixed).
- **Aperture.** $20\ \mathrm{km}$ of fibre at $5\ \mathrm{m}$ spacing gives 4000
  channels; the longest wavelength fully sampled across the aperture is
  $\lambda_{\max} \approx$ the array length, i.e. $20\ \mathrm{km}$, so the
  longest usable wavelength is roughly $2\ \mathrm{km}$ (requiring several
  wavelengths across the array for a resolvable wavenumber). At
  $c = 1500\ \mathrm{m\,s^{-1}}$ that corresponds to $f \gtrsim 0.75\ \mathrm{Hz}$:
  **the aperture, not the sample rate or the channel spacing, limits the
  low-frequency end of the target band.**
- **What the aperture costs.** Because $\lambda_{\max} \sim 2\ \mathrm{km}$
  corresponds to $f \gtrsim 0.75\ \mathrm{Hz}$ at the fast end of the target
  band, the $0.5\ \mathrm{Hz}$ part of the specification is not achievable with
  this deployment as stated; the honest response is to restate the band or to
  extend the aperture.
- **Assumptions to test before publishing amplitudes.** (i) **Coupling**: that
  the fibre's strain equals the ground's strain over the whole band (test with a
  co-located point sensor at two or three positions along the fibre). (ii)
  **Instrument response**: that the scale factor and phase are calibrated and
  stable (test with a known source, e.g. a hammer blow, and by comparing
  repeated recordings). (iii) **Noise independence**: that the noise is not
  common-mode across channels (test the cross-spectrum at large channel
  separations; a non-zero limit indicates a shared laser or timing term).

**★★★8. Derivation.**

Let the recorded field after gauge averaging over $M$ channel spacings be
$y[n] = s_M A\cos(knd) + n_g[n]$, where $s_M = \mathrm{sinc}(\pi M d/\lambda)$ and
the gauge-averaged noise is
$$n_g[n] = \frac{1}{M}\sum_{j=0}^{M-1} w[n-j], \qquad
\mathrm{Var}(w) = \sigma^{2}, \quad w \text{ independent between channels}.$$

The matched filter at the signal's wavenumber is
$S = \sum_{n=0}^{N-1} y[n]e^{-\mathrm{i}knd}$.

**Signal.** $\mathbb{E}[S] = A s_M \sum_n \cos(knd)e^{-\mathrm{i}knd}
\approx \frac{A s_M N}{2}$ (the counter-rotating term averages away).

**Noise variance.** The gauge-averaged noise has covariance
$\mathrm{Cov}(n_g[n], n_g[n+j]) = (\sigma^{2}/M^{2})(M - |j|)$ for $|j| < M$, so
$$\mathrm{Var}(S) = \sum_{j=-(M-1)}^{M-1}(N-|j|)\frac{\sigma^{2}}{M^{2}}
(M-|j|)e^{-\mathrm{i}kjd}
\approx \frac{N\sigma^{2}}{M^{2}}
\left|\sum_{m=0}^{M-1} e^{-\mathrm{i}kmd}\right|^{2}
= N\sigma^{2}\,s_M^{2}.$$

**The cancellation.** The key step is the last one: the *same* geometric sum
$\sum_{m=0}^{M-1}e^{-\mathrm{i}kmd} = M s_M$ that attenuates the signal also
determines the noise power **at the signal's own wavenumber**, because gauge
averaging is a linear filter and the noise passes through it exactly as the
signal does. Therefore
$$\mathrm{SNR} = \frac{\mathbb{E}[S]}{\sqrt{\mathrm{Var}(S)}}
= \frac{A s_M N/2}{\sigma\sqrt{N}\,s_M}
= \frac{A\sqrt{N}}{2\sigma},$$
**independent of $M$.** The naive "$1/\sqrt{M}$ noise reduction" is a statement
about the *total* noise power, $\mathrm{Var}(n_g) = \sigma^{2}/M$; it is not a
statement about the noise power in a single wavenumber bin, which is what a
matched filter estimates.

**When a longer gauge does help a narrowband detector.** Write the noise
spectral density (in wavenumber) as $S_{n}(k')$ and the gauge filter response as
$W(k') = \mathrm{sinc}(k'M d/2)$. The filtered noise power in the signal's bin is
proportional to $\int S_n(k')|W(k'-k)|^{2}\mathrm{d}k'$, while the signal
amplitude is proportional to $s_M = W(k)$. The two are equal-proportional only if
$S_n$ is *white* (constant in $k'$). If instead the noise is concentrated at
wavenumbers well above the signal's — as interrogator noise is, since it lives at
the channel scale — then increasing $M$ narrows $W$ and reduces the integral much
faster than it reduces $W(k) \approx 1$. **The condition is therefore: the noise
must be concentrated at wavenumbers larger than the signal's**, which is exactly
the physical situation the naive rule assumes and the demonstration's white-noise
model violates.
