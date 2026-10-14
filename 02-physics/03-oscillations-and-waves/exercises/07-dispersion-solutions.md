# Solutions — 02-03-07 Dispersion, Group Velocity and Phase vs Group Speed

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. $g = 9.80665$ m s⁻².

---

## ★1 — The three relations

**(a)** $\omega = 500k$: $v_{\text{ph}} = 500$ m s⁻¹, $v_g = 500$ m s⁻¹, ratio 1.

**(b)** $\omega = \sqrt{gk} = \sqrt{9.80665\times2} = 4.429447$ rad s⁻¹;
$v_{\text{ph}} = \omega/k = 2.214723$ m s⁻¹; $v_g = 0.5\sqrt{g/k} =
0.5\sqrt{4.903325} = 1.107362$ m s⁻¹; ratio 0.5.

**(c)** $\omega = 3\times10^{-3}\times4 = 1.2\times10^{-2}$ rad s⁻¹;
$v_{\text{ph}} = \omega/k = 6\times10^{-3}$ m s⁻¹;
$v_g = 2\alpha k = 2\times3\times10^{-3}\times2 = 1.2\times10^{-2}$ m s⁻¹;
ratio 2. The very small speeds here are a reminder that flexural waves are slow —
a 1 m thick steel plate at these wavenumbers moves at millimetres per second, which
is why flexural waves are negligible at seismic frequencies but dominate
free-oscillation spectra of thin elastic shells.

---

## ★2 — Two-frequency packet

**(a)** Carrier $\bar f = 10.25$ Hz; difference $\Delta f = 0.5$ Hz.

**(b)** Envelope period $1/\Delta f = 2.0$ s.

**(c)** The envelope travels at 1950 m s⁻¹ and the carrier at 2000 m s⁻¹, so the
relative slip is 50 m s⁻¹. A full cycle of slip corresponds to the envelope moving
one carrier wavelength relative to the carrier: the time is
$T_c/(1 - v_g/v_{\text{ph}}) = 0.1/0.025 = 4.0$ s, and the distance is
$v_g\times4.0 = 7800$ m.

**(d)** Cross-correlation of a *packet* measures the envelope delay, i.e. the
group velocity, 1950 m s⁻¹. A phase-difference measurement between receivers a few
metres apart measures the local phase velocity, close to 2000 m s⁻¹ for a
narrow-band signal. Both are defensible; the method must be stated.

---

## ★3 — Lattice

**(a)** For small $x$, $\sin x/x \to 1$ so $v_{\text{ph}} = c\sin(ka/2)/(ka/2) \to c$;
and $\cos(ka/2)\to1$ so $v_g\to c$ ✓.

**(b)** At $ka = \pi/2$: $v_{\text{ph}} = c\,\sin(\pi/4)/(\pi/4) =
0.900316c$; $v_g = c\cos(\pi/4) = 0.707107c$.

**(c)** $v_g = c\cos(\pi/2) = 0$: no energy propagates. The mode is a standing
pattern in which adjacent masses move in exact antiphase; the two counter-
propagating waves that compose it have equal and opposite energy fluxes.

**(d)** $\lambda = 2\pi/k = 4a$, so there are 4 grid points per wavelength — far too
few for a usable simulation (compare §6 of lesson 02-03-05 and the 10-point rule).

---

## ★4 — Swell

**(a)** $c_g = \tfrac12 gT/(2\pi)$. For $T = 8$ s: $c_g = 0.5\times9.80665\times8/
6.283185 = 6.243$ m s⁻¹. For $T = 16$ s: $c_g = 12.486$ m s⁻¹.

**(b)** $t = 3\times10^6/c_g$: $4.805\times10^5$ s = 133.5 h for the 8 s component;
$2.403\times10^5$ s = 66.7 h for the 16 s component.

**(c)** The 16 s swell arrives first, 66.7 h ahead of the 8 s swell.

**(d)** Because the long-period components outrun the short ones, the earliest
arrivals at the coast are the longest periods; as the storm's full spectrum
arrives, the observed period steadily lengthens. This is the classic
"period-lengthening" forecast rule for swell arrival, and it is a direct
consequence of $c \propto T$ in deep water.

---

## ★5 — Reading the measurement

**(a)** Non-dispersive: $v_{\text{ph}}$ difference $-1.636\times10^{-13}$,
$v_g$ difference $-2.955\times10^{-12}$. Gravity waves: $v_{\text{ph}}$
$-1.563\times10^{-4}$, $v_g$ $+4.691\times10^{-4}$.

**(b)** The non-dispersive differences are round-off (10⁻¹³–10⁻¹²). The
gravity-wave differences are bandwidth effects, because for a curved dispersion
relation a packet of finite width has a range of group velocities and the
measured envelope speed is a bandwidth average; the phase-gradient measurement
likewise returns a local wavenumber that differs from $k_0$ by $O(\Delta k^2)$.

**(c)** The measured $\omega$ is obtained from the temporal phase change over the
travel window, which samples the packet's average frequency rather than the
carrier, and for the concave dispersion relation $\omega \propto\sqrt k$ the
average over a symmetric band in $k$ is below $\omega(k_0)$ — a Jensen-inequality
effect, since $\omega(k)$ is concave in $k$.

**(d)** Halving $\Delta k$ should halve the local-wavenumber error (which is
$O(\Delta k^2)$) by a factor of four and reduce the group-velocity bandwidth bias
by of order a factor of four, while the round-off contributions stay put. Verify
by re-running and reporting the four numbers.

---

## ★6 — Rayleigh-wave dispersion

**(a)** A Rayleigh wave's sensitivity kernel extends to a depth of about one
wavelength, and the wavelength is $v_{\text{ph}}/f$; low frequencies therefore
have long wavelengths and sample deep material, while high frequencies are
confined to the near surface. This is what makes the dispersion curve a
depth-sounding measurement.

**(b)** At 5 Hz with $v = 1800$ m s⁻¹, $\lambda = 360$ m, so the kernel peaks near
120 m; at 50 Hz with $v = 700$ m s⁻¹, $\lambda = 14$ m, peaking near 4.7 m. The
depth coverage therefore spans a factor of about 25.

**(c)** The group velocity is $d\omega/dk$ of the measured $\omega(k)$, which
requires differentiating the dispersion curve (after smoothing) or using the
relation $v_g = v_{\text{ph}}/(1 - f\,dv_{\text{ph}}/df)$; a finite-difference
derivative of noisy data amplifies noise, so the group velocity is usually derived
from a smoothed or parametrised curve rather than point-by-point.

**(d)** Two sources of error: (i) the non-uniqueness of the inverse problem — a
dispersion curve over a finite band does not determine a unique layered profile,
and layering trade-offs (velocity versus thickness) are severe without additional
constraints; (ii) the assumption of a 1-D layered medium, which is violated by
lateral heterogeneity and by dipping structure, producing apparent dispersion that
is not physical layering.

---

## ★7 — Spreading

**(a)** Widths 20.0000 → 20.0000 (non-dispersive), 20.0000 → 20.1688 (gravity),
20.0000 → 20.6155 (flexural).

**(b)** Ranked by $|d^2\omega/dk^2|$: gravity (3.095) > flexural (1.000) >
non-dispersive (0). Ranked by observed growth: flexural (3.08 %) > gravity
(0.84 %) > none. The rankings differ because the spreading also depends on the
travel *time*, which differs between the relations at a fixed travel distance:
the gravity packet travels at 2.48 m s⁻¹ while the flexural packet travels at
0.40 m s⁻¹, so the flexural packet is in flight 6.2 times longer for the same 20 m.

**(c)** Because of that travel-time factor: growth $\propto |\omega''|t$, and
$t = \text{distance}/v_g$, so the flexural case wins despite its smaller
curvature.

**(d)** From equation (5), the envelope broadening is
$\Delta w \sim |\omega''|\,t/w_0$. Then
growth $= \sqrt{1 + (|\omega''|t/w_0^2)^2}$ for a Gaussian envelope of width
$w_0$. With $\omega'' = -3.0946$, $t = 20/2.4757 = 8.079$ s, $w_0 = 20$:
$|\omega''|t/w_0^2 = 0.0625$, and $\sqrt{1+0.0625^2} = 1.00195$ — considerably
less than the measured 1.00844. The measured value is *four times* the estimate,
which means the broadening is not purely second order in the linearised sense:
with $\Delta k = 0.1$ and $k_0 = 0.4$, the band is wide ($\Delta k/k_0 = 0.25$)
and the next term in the Taylor series contributes. The honest conclusion is that
the scaling is right but the coefficient requires the full integral, so the
measured growth should be compared with a numerical evaluation of equation (2)
rather than with the first-order estimate.

---

## ★8 — Numerical dispersion

**(a)** For small arguments, $\sin x \approx x$, so
$\omega\Delta t/2 \approx r k\Delta x/2$, i.e. $\omega \approx crk\Delta x/\Delta t
= ck$ using $r = c\Delta t/\Delta x$ ✓.

**(b)** Using $\sin x = x - x^3/6$,
$\omega\Delta t/2 = r\left[k\Delta x/2 - (k\Delta x/2)^3/6\right]$, so
$\omega = ck\left[1 - (k\Delta x)^2/24\right]$, i.e.
$v_{\text{ph}} = \omega/k = c\left[1 - (k\Delta x)^2/24\right]$ — note that the
$r$-dependence cancels at this order for the *semi-discretised* form; the standard
result for the fully discrete leapfrog scheme is
$v_{\text{ph}} = c\left[1 + \frac{(k\Delta x)^2}{24}(1-r^2)\right]$, which reduces
to the above when the time discretisation error is included and $r\to1$. Report
which form you derived and verify numerically by solving for $\omega$ from
$\sin(\omega\Delta t/2) = r\sin(k\Delta x/2)$ at several $k$.

**(c)** With $k\Delta x = 2\pi/10 = 0.628319$ and $r = 0.5$:
$(k\Delta x)^2/24 = 0.016449$ and $(1-r^2) = 0.75$, so the bracket is
$1 + 0.012337$: the numerical phase velocity is 1.23 per cent high. Over a
propagation of 100 wavelengths the accumulated phase error is $1.23$ cycles —
catastrophic for waveform matching, and the reason production modelling uses
either higher-order stencils (error $O(\Delta x^4)$) or 15–20 points per
wavelength.

**(d)** Design rule: choose the grid so that the accumulated phase error over the
propagation path is a small fraction of a cycle, i.e.
$N_\lambda (k\Delta x)^2(1-r^2)/24 \ll 1$; with $N_\lambda = 100$ and $r=0.5$ this
requires $k\Delta x < 0.16$, about 40 points per wavelength for a 5 per cent
phase tolerance. Anything less needs a higher-order scheme.

---

## ★★★9 — Group velocity in an attenuating medium

**(a)** With $k = \omega/v(\omega)$ and $v(\omega)$ varying slowly,
$dk/d\omega = 1/v - (\omega/v^2)dv/d\omega$, so
$v_g = d\omega/dk = v/(1 - (\omega/v)dv/d\omega)$ ✓, which for
$v(\omega) \propto 1 + \ln(f/f_0)/(\pi Q)$ gives the stated form.

**(b)** Since $v$ increases with frequency for a constant-$Q$ medium (higher
frequency travels faster), $dv/d\omega > 0$ and $v_g = v/(1-\text{positive})
> v$. **The group velocity exceeds the phase velocity here** — the opposite of the
gravity-wave case. At $Q = 50$ over a decade, $dv/v \approx \ln(10)/(\pi\times50)
= 0.01466$, so the fractional difference between $v_g$ and $v$ is of order 1.5 per
cent. Report your computed values.

**(c)** A program should give $v_{\text{ph}}$ rising by about 1.5 per cent per
decade and $v_g$ rising slightly faster; the absolute values depend on the
reference choice $v(f_0)$ and the sign convention in the logarithm. Report the
table for 1, 5, 10 and 50 Hz.

**(d)** Both are legitimate measurements of different quantities. The honest
practice is to state what was measured: a picked arrival time on a pulse gives the
group velocity; a phase-based (e.g. cross-spectral) estimate gives the phase
velocity at that frequency; and if a velocity is reported for comparison with
laboratory or log data, the frequency and the measurement method must accompany
it. This is one of the most common sources of discrepancy between published
velocity datasets.

---

## ★★★10 — Dispersion from an array

**(a)** With $n$ receivers over an aperture $L$, the wavenumber resolution is
$\Delta k \approx 2\pi/L$ (the Rayleigh limit) and the Nyquist wavenumber is
$k_{\text{Nyq}} = \pi/\Delta x = \pi(n-1)/L$. The usable band is therefore
$2\pi/L \lesssim k \lesssim \pi(n-1)/L$.

**(b)** The band is non-empty when $(n-1)/2 \gg 1$, and the best resolution for a
given mode occurs when $L \sim$ a few wavelengths: shorter apertures cannot
resolve $k$, longer ones push the mode's energy out of the high-$k$ end of the
usable band. The practical condition is $L/\lambda \gtrsim 2$.

**(c)** A synthetic test with 24 receivers over 100 m, two modes crossing at one
frequency, and an f-k transform should recover both branches away from the
crossing, and should show degraded resolution in a neighbourhood of the crossing
of width $\sim\Delta k$. Report your recovered curves and identify the
well-resolved band.

**(d)** At a crossing, two modes share the same $(f,k)$, so the recorded
amplitude is the sum of two contributions that cannot be separated by a linear
transform; the dispersion estimates swap branches or average them, producing a
spurious jump. Standard strategies are to use the *multichannel* nature of the
data with a mode-separation transform, to restrict the inversion to frequencies
away from the crossing, or to use full-waveform inversion, which models both modes
simultaneously.
