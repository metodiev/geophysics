# Solutions — 02-03-10 Attenuation, Absorption and the Quality Factor Q

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Decay parameters

**(a)** $\alpha = \pi f/(Qv)$: at 10 Hz,
$\alpha = \pi\times10/(80\times3200) = 1.22718\times10^{-4}$ m⁻¹; at 50 Hz,
$\alpha = 6.13592\times10^{-4}$ m⁻¹.

**(b)** $1/\alpha = 8148.8$ m (10 Hz) and 1629.8 m (50 Hz).

**(c)** $e^{-\alpha\times2000}$: 0.78228 at 10 Hz and 0.29297 at 50 Hz.

**(d)** The 10 Hz component survives better, by the factor
$0.78228/0.29297 = 2.670$. Note this is exactly $e^{-\alpha_{10}2000}/
e^{-\alpha_{50}2000} = e^{(\alpha_{50}-\alpha_{10})2000}$, and the ratio equals
$(e^{-\alpha_{10}2000})^{4}$ since $\alpha \propto f$ — the fourth power of the
low-frequency survival, which is the quantitative version of "high frequencies die
first".

---

## ★2 — $Q$ from an amplitude ratio

**(a)** $\ln(1.00/0.25) = 1.386294$, so
$\alpha = 1.386294/500 = 2.772588\times10^{-3}$ m⁻¹.

**(b)** $Q = \pi f/(\alpha v) = \pi\times30/(2.772588\times10^{-3}\times2500) =
94.247780/6.931471 = 13.5971$.

**(c)** $\lambda = 2500/30 = 83.333$ m; decay per wavelength
$\alpha\lambda = 0.231049$, i.e. $e^{-0.231} = 0.7937$ per wavelength — a 20 per
cent loss per cycle, appropriate to $Q \approx 13.6$.

**(d)** Geometric spreading (the measurement is at a single offset, so $1/r$ would
contribute a factor of the ratio of distances — here none, since a single
receiver pair is used, but an absolute amplitude measurement would need it);
scattering; transmission losses; and instrument coupling. To test: repeat with a
different receiver separation and check that $\ln(A_1/A_2)$ scales linearly with
the separation (that is the signature of a path effect rather than a coupling
effect), and measure $Q$ at several frequencies to test the frequency dependence.

---

## ★3 — Decay per wavelength

$\alpha\lambda = \pi/Q$: for $Q = 20$, 0.157080; $Q = 100$, 0.031416;
$Q = 500$, 0.0062832.

**(a)** $e^{-\pi/Q}$: 0.854635, 0.969072, 0.993736.

**(b)** dB per wavelength $= 8.686\pi/Q$: 1.3645, 0.27291, 0.054582 dB.

**(c)** Decay length in wavelengths $= Q/\pi$: 6.37, 31.83, 159.15.

**(d)** A 60 dB dynamic range corresponds to $e^{-\alpha x} = 10^{-3}$, i.e.
$8.686\alpha x = 60$ dB, or $\alpha x = 6.9078$. For a 3 km survey at 30 Hz with
$v = 3000$ m s⁻¹ ($\lambda = 100$ m), the number of wavelengths is 30, so the
attenuation is $30\times\pi/Q$ nepers: $Q = 20$ gives 4.712 nepers = 40.9 dB —
right at the limit; $Q = 100$ gives 0.942 nepers = 8.2 dB — comfortable;
$Q = 500$ is negligible. So only the $Q = 20$ case is marginal, and it fails for
longer paths: this is the quantitative basis for the statement that high-attenuation
terranes cannot be imaged to depth at high frequency.

---

## ★4 — The dashpot model

**(a)** $Q = \omega/(2\beta) = 40/4 = 10$.

**(b)** Decay per period: $e^{-2\pi\beta/\omega} = e^{-\pi/Q} = e^{-0.314159} =
0.730403$; per wavelength $= k/(2Q)$ with $k = \omega/c = 0.02$ rad m⁻¹, so
$\alpha\lambda = \pi/Q = 0.314159$: the same number, because the decay per period
and per wavelength are both $\pi/Q$ — a useful identity that follows from
$T = \lambda/v$.

**(c)** No: $Q = \omega/2\beta \propto f$, so a dashpot attenuates low frequencies
strongly. For broadband data this predicts that the low-frequency end of the band
is lost fastest, which is the opposite of what is observed in rocks; a dashpot
model fitted at one frequency will mispredict the whole band.

**(d)** A standard linear solid, or a distribution of them (a superposition of
relaxation mechanisms), which produces a $Q$ that is nearly constant over a
decade or more. See lesson
[02-04-07](../../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md).

---

## ★5 — Reading the simulation

**(a)** Measured decay rate 0.800227 s⁻¹ against the input $\beta = 0.8$ s⁻¹;
measured $Q = 19.6294$ against $\omega/(2\beta) = 19.6350$.

**(b)** The peaks are 0.99992, 0.85205, 0.72605, 0.61867, 0.52718, 0.44921,
0.38277, 0.32616, 0.27792, 0.23681. Successive ratios: 1.17364, 1.17355,
1.17355, 1.17354, 1.17380, 1.17356, 1.17353, 1.17336, 1.17359 — constant to
about $2\times10^{-4}$, which is the signature of a single exponential with a
constant decay rate.

**(c)** The velocity-Verlet integration with a finite time step conserves a nearby
invariant and accumulates an $O(\Delta t^2)$ error in the *phase*, which the
exponential fit of the envelope converts into a small rate error. It is a
numerical artefact, and it is 170 times smaller than any realistic field error.

**(d)** At $\beta = 8$ s⁻¹, $Q = 31.4159/16 = 1.96$: very lossy. The amplitude
falls by $e^{-\pi/1.96} = 0.201$ per period, so after three periods the signal is
at 0.8 per cent — the fit will have four usable peaks and the measured $Q$ will
depart from $\omega/2\beta$ by a few per cent because the exact relation involves
$\omega_d = \sqrt{\omega^2 - \beta^2}$ rather than $\omega$. Verify and report
your measured value.

---

## ★6 — Spectral ratio

**(a)** $\ln(A_1/A_2) = \alpha(f)\Delta x = \pi f\Delta x/(Qv)$, so a plot against
$f$ has slope $\pi\Delta x/(Qv)$ with units of seconds (dimensionless per hertz,
i.e. s), and $Q = \pi\Delta x/(v\times\text{slope})$.

**(b)** Slope $= \pi\times1000/(50\times3000) = 0.020944$ s.

**(c)** $\ln(A_1/A_2) = 0.020944f$, so at 5, 20 and 50 Hz the ratios are
$e^{0.104720} = 1.1104$, $e^{0.418879} = 1.5203$, $e^{1.047198} = 2.8497$.

**(d)** $Q$ is inversely proportional to $v\Delta x$ times the slope, so a 5 per
cent error in $v$ gives a 5 per cent error in $Q$ (opposite in sign, since $Q$
contains $1/v$ in this arrangement: $Q$ would be 5 per cent *high* if $v$ were 5
per cent low). Likewise, an error in $\Delta x$ propagates linearly. This is why
the geometry must be known accurately and why the far more dangerous errors are
the frequency-dependent coupling and source terms, which enter the slope directly
and are not geometric at all.

---

## ★7 — Noise sensitivity

**(a)** $Q$ recovered: 80.0000 (residual $1.36\times10^{-16}$), 79.5882
($8.06\times10^{-3}$), 77.9725 ($4.03\times10^{-2}$) for 0, 1 and 5 per cent
noise.

**(b)** Forty frequencies were fitted, and independent random errors average down;
the slope's standard error is roughly the per-point error divided by
$\sqrt{n_{\text{eff}}}$ times the lever arm in frequency. With 1 per cent
amplitude error over 40 points spanning 5–102.5 Hz, the slope error is of order
$10^{-3}/10 = 10^{-4}$, which is 0.5 per cent of $Q$ — matching the measurement.

**(c)** Halving the separation halves the slope and halves the signal in the ratio,
so the relative error in the recovered $Q$ doubles (roughly): expect about 1 per
cent error at 1 per cent noise, and poorer conditioning. Verify by modifying the
script and reporting the new residuals.

**(d)** Source and receiver coupling variations with frequency, transmission
losses at interfaces (which require a velocity model), and focusing/defocusing
from lateral velocity structure. In most field datasets these dominate the
statistical error by an order of magnitude or more.

---

## ★8 — Dispersion from attenuation

**(a)** $v(1) = 3000[1 + \ln(0.1)/(\pi\times60)] = 3000[1 - 2.302585/188.4956] =
3000\times0.987785 = 2963.36$ m s⁻¹;
$v(100) = 3000[1 + \ln(10)/(\pi\times60)] = 3000\times1.012215 = 3036.65$
m s⁻¹.

**(b)** Fractional difference $= (3036.65-2963.36)/3000 = 2.443$ per cent.

**(c)** Over 100 km, the high-frequency arrival is earlier by
$10^5(1/2963.36 - 1/3036.65) = 10^5\times8.148\times10^{-6} = 0.8148$ s. That is
enormously larger than modern picking precision (milliseconds), so the effect is
not merely measurable but must be modelled: ignoring it would bias the inverted
velocity by of order 1 per cent, which is well above the precision of modern
tomography.

**(d)** A phase-arrival inversion assumes each arrival travelled at a
single-frequency phase velocity; with attenuation-induced dispersion, a broadband
pick corresponds to a group velocity that differs from $v(f)$. Treating the two as
interchangeable introduces a frequency-dependent, path-length-dependent bias that
maps into a spurious velocity anomaly correlated with the $Q$ structure — the
classic trade-off between elastic and anelastic tomography.

---

## ★★★9 — Amplitude model and station corrections

**(a)** $S(f)$ source spectrum; $G(x)$ geometric spreading; $R(\theta,\phi)$
source radiation pattern; $C(x)$ station/site transfer function (coupling,
near-surface structure); $M(f,x)$ other multipliers (transmission losses,
scattering, focusing); $e^{-\alpha(f)x}$ intrinsic attenuation.

**(b)** Taking the ratio of amplitudes at two nearby receivers arranged along
roughly the same ray path cancels $S(f)$, $R(\theta,\phi)$ (to the extent the take-off
angles are equal) and much of $M(f,x)$; the residual is the exponential term plus
the *difference* of the two site terms and the difference in geometric spreading.
The assumption is that the two paths are similar enough that the non-exponential
factors cancel — which fails exactly where the geology changes along the path.

**(c)** A numerical experiment: forward-model amplitudes with a known $Q$,
$G(x) = 1/x$, and a random multiplicative station-correction field $C(x)$ with,
say, a 20 per cent standard deviation. Recover $Q$ (i) using adjacent-station
ratios only, and (ii) using absolute amplitudes with the corrections omitted.
Expect the ratio method to recover $Q$ to within a few per cent and the absolute
method to be biased by tens of per cent, with the bias depending on the
correlation length of $C(x)$. Report your measured values.

**(d)** Site corrections are not a refinement: in most datasets they dominate the
error budget of an attenuation measurement, so a $Q$ map built without them is
mostly a map of station coupling unless the array is dense enough for the
corrections to average out.

---

## ★★★10 — Scattering versus absorption

**(a)** $\alpha_{\text{tot}} = \alpha_{\text{abs}}+\alpha_{\text{scatt}}$, and since
$Q^{-1} = 2\alpha v/\omega$, the reciprocals add:
$Q_{\text{tot}}^{-1} = Q_{\text{abs}}^{-1} + Q_{\text{scatt}}^{-1}$. **Note the
reciprocal**: attenuations add, quality factors do not; combining two loss
mechanisms always gives a lower total $Q$ than either alone.

**(b)** With $\alpha_{\text{scatt}} \propto n a^6 f^4/v$ (Rayleigh) and
$\alpha_{\text{abs}} = \pi f/(Q_{\text{int}}v)$, equality requires
$n a^6 f^4 = \pi f/Q_{\text{int}}$, i.e.
$f^3 = \pi/(Q_{\text{int}}na^6)$ and
$f = [\pi/(200\times10^{10}\times(5\times10^{-3})^6)]^{1/3}$. With
$a^6 = 1.5625\times10^{-14}$ m⁶, $na^6 = 1.5625\times10^{-4}$ m⁻³,
the bracket is $\pi/(200\times1.5625\times10^{-4}) = 100.53$, giving
$f = 4.65$ Hz. **The prefactor in the Rayleigh formula was omitted here and it is
order-unity at best and geometry-dependent; the honest statement is that the
crossover falls in the seismic band for these parameters, with an uncertainty of
perhaps a factor of three, and cannot be pinned down without a specific scattering
model.**

**(c)** A crossover at a few hertz means that for a heterogeneous rock of this
type, scattering dominates the apparent attenuation *below* the crossover
frequency and intrinsic absorption above it — or the reverse, depending on the
actual prefactor, which is why the statement must be tested rather than assumed.
The practical consequence is that a frequency-dependent $Q$ measured over the
seismic band may be a scattering signature rather than a thermal one.

**(d)** The independent measurement is the coda: scattering transfers energy to
later times (a long coda), while intrinsic absorption removes it (a short coda and
a low coda level). Measuring both the direct-wave decay and the coda decay, and
their ratio, separates the two mechanisms — the standard approach in
scattering-attenuation studies — at the cost of requiring good signal-to-noise in
the coda and a model for the source duration.
