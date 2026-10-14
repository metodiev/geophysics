# Solutions — 02-03-04 Wave Description

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. $g = 9.80665$ m s⁻².

---

## ★1 — The parameter table

**(a)** $\lambda = v/f = 4000/25 = 160$ m; $T = 1/25 = 0.040$ s;
$k = 2\pi/160 = 0.039270$ rad m⁻¹; $\omega = 2\pi\times25 = 157.079633$ rad s⁻¹.

**(b)** $f = v/\lambda = 1500/0.30 = 5000$ Hz; $T = 2\times10^{-4}$ s;
$k = 2\pi/0.30 = 20.943951$ rad m⁻¹;
$\omega = 2\pi\times5000 = 31415.926536$ rad s⁻¹.

**(c)** $v = \lambda f = 0.025\times200000 = 5000$ m s⁻¹;
$T = 5\times10^{-6}$ s; $k = 2\pi/0.025 = 251.327412$ rad m⁻¹;
$\omega = 1.256637\times10^6$ rad s⁻¹.

Check in each case that $\omega/k = v$ ✓.

---

## ★2 — Reading a wave

**(a)** $A = 0.02$ m; $k = 12$ rad m⁻¹; $\omega = 300$ rad s⁻¹;
$\varphi_0 = \pi/3 = 1.047198$ rad.

**(b)** $\lambda = 2\pi/12 = 0.523599$ m; $T = 2\pi/300 = 0.020944$ s;
$v = \omega/k = 25$ m s⁻¹ (equivalently $\lambda f = 0.523599\times14.323945 =
25.000$ m s⁻¹ ✓ with $f = 47.746483$ Hz).

**(c)** $+x$. The phase is $kx - \omega t$; to hold the phase fixed as $t$
increases, $x$ must increase.

**(d)** $kx = 3.0$, $\omega t = 3.0$, so the argument is $3.0 - 3.0 + 1.047198 =
1.047198$ and $u = 0.02\cos(1.047198) = 0.01$ m exactly. Note the coincidence
$kx = \omega t$ makes the answer independent of both $x$ and $t$ separately —
a useful reminder that only the phase combination is physical.

---

## ★3 — Resolution from wavelength

**(a)** $\lambda = v/f = 4500/25 = 180$ m.

**(b)** The standard limit is $\lambda/4$ for vertical resolution, after
accounting for the two-way travel and the fact that a wavelet of bandwidth
$f_{\max}-f_{\min}$ can separate events whose travel-time difference exceeds
about half a period. It is an approximation and its numerical coefficient depends
on the wavelet and the noise level (compare lesson 02-03-09).

**(c)** $180/4 = 45$ m.

**(d)** $f = v/(4d) = 4500/(4\times10) = 112.5$ Hz, which is far above the band
available from a conventional seismic source; this is why 10 m beds are routinely
resolved only with higher-frequency sources (or in shallow, low-velocity
materials).

---

## ★4 — Aliasing

**(a)** $f_{\text{Nyquist}} = 50$ Hz.

**(b)** 20 Hz → 20 Hz; 55 Hz → $|55-100| = 45$ Hz; 130 Hz →
$|130-100| = 30$ Hz.

**(c)** Only 20 Hz is unchanged (it is the only component below the Nyquist
frequency). 45 Hz and 30 Hz are aliases.

**(d)** The 130 Hz component must be attenuated *before* sampling, by an analog
anti-alias filter, or the sample rate raised above 260 Hz. After sampling, 30 Hz
is a genuine frequency in the record and the aliased 130 Hz is indistinguishable
from a real 30 Hz signal, so no algorithm can separate them.

---

## ★5 — Two-receiver phase velocity

**(a)** $\omega = 2\pi\times30 = 188.495559$ rad s⁻¹;
$\Delta\varphi = 150^\circ = 2.617994$ rad, so
$v = \omega\Delta x/\Delta\varphi = 188.495559\times12/2.617994 =
863.944$ m s⁻¹.

**(b)** $\lambda = v/f = 28.798$ m, so $\Delta x/\lambda = 12/28.798 = 0.416695$:
the spacing is well below one wavelength and the answer is unambiguous.

**(c)** Velocities $v' = v/(1 + n\lambda/\Delta x)$ for integer $n$ also give a
phase difference of $150^\circ$ modulo $2\pi$, i.e. $v' = 863.944/(1+2.399$…)
and, in the other direction, $v' = 863.944/(1 - 2.399)$, a negative speed. The
family is infinite because phase is defined modulo $2\pi$.

**(d)** An independent constraint on the arrival time or travel-time difference
(so that the number of cycles is known), several receivers spaced closely enough
to track the phase continuously, or a prior velocity bound from a well log.

---

## ★6 — Ocean swell

**(a)** $c = gT/(2\pi)$ with $T = 10$ s gives
$c = 9.80665\times10/(2\pi) = 15.608$ m s⁻¹ ✓. Then
$\lambda = cT = 156.08$ m ✓ and $f = 1/T = 0.1$ Hz ✓. The alternative form
$c = \sqrt{g\lambda/(2\pi)} = \sqrt{9.80665\times156.08/6.283185} =
\sqrt{243.65} = 15.609$ m s⁻¹ ✓.

**(b)** For gravity waves the restoring force is gravity acting on a deformed free
surface; the wave speed is set by $g$ and the wavelength (or period), not by a
property of water. The medium's density cancels because both inertia and the
pressure gradient scale with it, and viscosity is irrelevant at these scales. The
statement "the speed is set by the external field and the geometry" is the
general signature of a gravity wave, as opposed to an elastic wave whose speed is
$\sqrt{\text{modulus}/\text{density}}$.

**(c)** $c = 9.80665\times15/(2\pi) = 23.413$ m s⁻¹, $\lambda = 351.19$ m. The
longer swell is 1.5 times faster and 2.25 times longer.

**(d)** The largest-period swell arrives first, because $c$ increases with $T$.
That is why a distant storm's arrival is signalled by a lengthening of the swell
period at the coast, and why the "forerunners" seen at a surf break are the
long-period components — a direct observational consequence of the dispersion
relation in the table.

---

## ★7 — GPR parameters

**(a)** $v = c/\sqrt{\varepsilon_r} = 2.998\times10^8/3 = 9.993\times10^7$
m s⁻¹.

**(b)** $\lambda = v/f = 9.993\times10^7/2\times10^8 = 0.499667$ m.

**(c)** Two-way travel time $= 2\times3/v = 6/9.993\times10^7 =
6.004\times10^{-8}$ s = 60.04 ns.

**(d)** Using the $\lambda/4$ rule, resolution ≈ 0.125 m at 200 MHz. At 100 MHz
the wavelength doubles to 0.999 m and the resolution limit doubles to about
0.25 m, but the attenuation at the lower frequency is less, so the achievable
depth is greater. That trade-off between resolution and penetration is the
definition of a GPR survey design.

---

## ★8 — Bandwidth, dispersion and $Q$

**(a)** A pulse 40 m long with $\lambda = v/f = 3000/50 = 60$ m contains roughly
$40/60 = 0.67$ wavelengths, so its bandwidth is of order $f \times 60/40
\approx 75$ Hz FWHM — a wide band. Wavelengths present run from about 40 m to
150 m for the range $f = 20$–75 Hz.

**(b)** Over 1 km the number of wavelengths is $1000/\lambda$, so the amplitude
ratio between the ends of the band is
$e^{-\pi(1000/40 - 1000/150)/50}$. The exponent is
$-\pi\times(25 - 6.667)/50 = -\pi\times0.36667 = -1.1519$, giving an amplitude
ratio of $0.316$: the high-frequency end is attenuated to about a third of the
low-frequency end over a kilometre.

**(c)** Assuming constant $Q$ over a factor-of-four frequency range is an
approximation. It is defensible for an order-of-magnitude estimate — and it is
commonly made in seismic processing — but it fails where the band crosses a
relaxation frequency of the rock, and it cannot reproduce the observation that
$Q$ in many rocks is nearly constant over decades while in others it is strongly
frequency-dependent. The honest statement is that $Q$ should be measured over the
band of interest (lesson 02-03-10).

---

## ★★★9 — Spatial aliasing and array design

**(a)** Samples at $x_n = n\Delta x$ of a wave $e^{ikx}$ are
$e^{ikn\Delta x}$. Adding $k' = k + 2\pi m/\Delta x$ gives
$e^{i(k+2\pi m/\Delta x)n\Delta x} = e^{ikn\Delta x}e^{2\pi imn} =
e^{ikn\Delta x}$: identical samples. The set of aliases is therefore $k$ modulo
$2\pi/\Delta x$, and the unique band is $|k| \le \pi/\Delta x$, i.e.
$\lambda \ge 2\Delta x$.

**(b)** The measured phase difference is $\Delta\varphi = k\Delta x$ modulo
$2\pi$; it is unambiguous only if $|k\Delta x| < \pi$, i.e.
$\lambda > 2\Delta x$. ✓

**(c)** At 5 Hz, $\lambda = 3000/5 = 600$ m; at 50 Hz,
$\lambda = 1000/50 = 20$ m. The condition is $\Delta x < \lambda_{\min}/2 =
10$ m, and it is set by the **high-frequency end**. That is the general rule:
the shortest wavelength in the band controls the spacing.

**(d)** Halving the spacing doubles the number of receivers for a given aperture,
and the aperture sets the wavenumber resolution ($\Delta k \approx 2\pi/L$ for an
aperture $L$) while the spacing sets the highest wavenumber (Nyquist). A smaller
aperture improves high-frequency coverage at the cost of resolution at low
frequencies; with a fixed number of receivers one cannot have both, which is why
broad-band arrays are large.

---

## ★★★10 — Phase-velocity estimators

**(a) and (b)** A program that synthesises traces with a deterministic pseudo-
random generator and repeats the measurement gives approximately: the
two-receiver estimator has a standard deviation of about 2–3 per cent of the
velocity, while the three-receiver least-squares fit has about 1–1.5 per cent.
Report your own measured standard deviations and the exact noise model used.

**(c)** The two-receiver estimate uses a single phase difference, so its error
grows linearly with the phase noise and is not reduced by averaging unless the
measurement is repeated. The least-squares fit uses the *slope* of phase against
distance, which averages the random errors of all receivers; for $n$ equally
spaced receivers with independent phase errors, the standard error of the slope
improves as $\sqrt{n}$ in the ideal case, so three receivers give a factor of
about 1.2–1.7 over two.

**(d)** Both share the systematic error from the *assumed cycle count*. If the
true phase difference exceeds $2\pi$ the estimator locks onto the wrong branch,
and no amount of averaging removes a branch error: the bias is of order
$1/(\Delta x/\lambda)$, i.e. many per cent or more, and it is the reason phase
estimators are always validated against a travel-time pick or a dispersion-curve
continuity condition.
