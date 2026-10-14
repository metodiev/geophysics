# Solutions — 02-03-09 Diffraction, Scattering and Resolution Limits

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Single slit

**(a)** $\sin\theta_1 = \lambda/a = 600\times10^{-9}/0.2\times10^{-3} = 3\times10^{-3}$,
so $\theta_1 = 0.171887^\circ = 3.000\times10^{-3}$ rad.

**(b)** The central maximum spans $\pm\theta_1$, i.e. an angular width of
$6.000\times10^{-3}$ rad.

**(c)** Linear width $= 2L\tan\theta_1 \approx 2\times2.0\times3\times10^{-3} =
0.012$ m = 12 mm.

**(d)** Halving the slit doubles the width to 24 mm: the central maximum is
inversely proportional to $a$.

---

## ★2 — Aperture resolution

**(a)** $\theta = 1.21967\lambda/D = 1.21967\times550\times10^{-9}/0.30 =
2.236\times10^{-6}$ rad (using the exact constant; the 1.22 approximation gives
$2.237\times10^{-6}$).

**(b)** Linear resolution $= \theta\times3.84\times10^8 = 859$ m. The assumption is
that the atmosphere does not limit the measurement — for a ground-based telescope
at visible wavelengths, atmospheric seeing is often several times worse, which is
why adaptive optics and space telescopes exist.

**(c)** At 21 cm: $\theta = 1.21967\times0.21/0.30 = 0.8538$ rad = 48.9° — the dish
is barely a telescope at all at that wavelength.

**(d)** To reach $2.236\times10^{-6}$ rad at 21 cm requires $D =
1.21967\times0.21/2.236\times10^{-6} = 1.15\times10^5$ m = 115 km. No single dish
can be that large, which is precisely why radio interferometry synthesises the
aperture from separated antennas — the resolution is set by the *baseline*, not by
the dish.

---

## ★3 — Seismic resolution

**(a)** $\lambda = 2500/40 = 62.5$ m.

**(b)** $r_F = \sqrt{\lambda z/2} = \sqrt{62.5\times600/2} = \sqrt{18750} =
136.93$ m.

**(c)** Footprint diameter $= 2r_F = 273.86$ m.

**(d)** $\lambda/4 = 15.63$ m and $\lambda/2 = 31.25$ m. Note the migrated limits
are independent of depth in this approximation, which is why deeper targets are
not intrinsically less resolvable laterally once migration has been applied —
they are, however, illuminated by a narrower range of angles, which in practice
degrades the achievable migration resolution.

---

## ★4 — Scattering regimes

**(a)** $ka = 2\pi\times10^{-3}/100 = 6.3\times10^{-5} \ll 1$: Rayleigh.
Scattered amplitude $\propto a^3/\lambda^2$, extremely weak.

**(b)** $ka = 2\pi\times20/100 = 1.26 \sim 1$: resonant (Mie-like). Strong,
structured scattering; this is the regime that dominates seismic coda from
fractured rock.

**(c)** $ka = 2\pi\times500/100 = 31 \gg 1$: geometric. The fault is a reflector
and a diffractor of its edges, described by ray theory plus diffraction at its
terminations.

**(d)** $ka = 2\pi\times10^{-3}/10^{-2} = 0.628$: resonant. This is why radar
rain-clutter is strong and strongly frequency-dependent — the regime is
uncomfortably in the middle of the size parameter range.

---

## ★5 — Reading the slit check

**(a)** Maximum difference $7.685\times10^{-7}$; located first zero at
$\sin\theta = 0.250200$.

**(b)** The zero is located by scanning the analytic closed form on a grid of
2001 points over $0 \le \sin\theta \le 1.2$, so the grid spacing is
$6\times10^{-4}$ and the located zero cannot be more accurate than about half
that. The observed difference $2.0\times10^{-4}$ is within half the grid spacing,
which is the correct conclusion: the *method* limits the precision.

**(c)** The trapezoid rule on a smooth periodic integrand converges faster than any
power of the number of points (spectrally), so multiplying the points by ten should
reduce the maximum difference by orders of magnitude rather than by a constant
factor. Verify: if the residue is dominated by the endpoint treatment, expect a
reduction to the $10^{-10}$ level. Report your measured value.

**(d)** The integrand $e^{-ik\sin\theta x}$ is smooth and, over the aperture, spans
a whole number of half-periods for the angles tested; the trapezoid rule is
spectrally accurate for periodic functions sampled to their period, which is why
the residuals are so far below the $O(n^{-2})$ expectation.

---

## ★6 — Reading the Airy check

**(a)** First zero of $J_1$ at 3.831705970, giving
$C = 3.831705970/\pi = 1.2196699$.

**(b)** $C = 1.21967$ to five decimals: the "1.22" of the textbooks is a
rounding, and quoting 1.22 rather than 1.2197 is a 0.03 per cent error — harmless
for an estimate, not for a calibration.

**(c)** The Bessel function $J_1$ appears because the aperture integral over a disk
reduces to a Bessel integral of order 1 ($\int_0^{2\pi}e^{iq\cos\phi}d\phi =
2\pi J_0(q)$, and the radial integral of $\rho J_0(q\rho)$ gives
$J_1(q)/q$). The factor 2 normalises the on-axis value to 1 (since
$J_1(q)/q \to 1/2$ as $q\to0$). $J_0$ would be the answer for a *ring* or for the
one-dimensional case; the aperture shape determines the order.

**(d)** The negative values mean the *field* has reversed sign: the complex
amplitude of the diffracted wave is negative there, so that the intensity (its
square) has a local maximum after the first zero — the second bright ring of the
Airy pattern. The quadrature returns the signed real part because the aperture is
centrosymmetric.

---

## ★7 — GPR resolution

**(a)** $v = c/\sqrt{\varepsilon_r} = 2.99792458\times10^8/\sqrt6 =
1.22383\times10^8$ m s⁻¹; $\lambda = v/f = 1.22383\times10^8/4\times10^8 =
0.30596$ m.

**(b)** $r_F = \sqrt{\lambda z/2} = \sqrt{0.30596\times2.0/2} = \sqrt{0.30596} =
0.55314$ m (this is the ideal estimate, and it can exceed the depth — a sign that
the paraxial approximation, which assumes $z \gg r_F$, is only marginally valid
here; state that caveat).

**(c)** $\lambda/4 = 0.0765$ m and $\lambda/2 = 0.153$ m.

**(d)** Because resolution scales with $\lambda z$, and $\lambda$ is 2–4 orders of
magnitude smaller for GPR (centimetres versus tens of metres) even though the
relative depth $z/\lambda$ is comparable; the absolute resolution is therefore far
better. The price is that attenuation at those frequencies limits penetration to
metres rather than kilometres.

---

## ★8 — Reading the Fresnel check

**(a)** Maximum difference $1.089\times10^{-4}$; first maximum located at
$r = 14.1421$ m with amplitude 2.000000.

**(b)** The integrand oscillates more rapidly as $\rho$ grows (its phase is
$\propto\rho^2$), so a fixed-step Simpson rule accumulates more error at larger
radii; the error scales with the number of oscillations per step.

**(c)** At $r = 20$ m the phase $\pi r^2/(2\lambda z) = \pi\times400/400 = \pi$, so
$\sin(\pi) = 0$ — the analytic value is exactly zero and the numerical value
$1.05\times10^{-4}$ is entirely quadrature error. The zeros correspond to
aperture radii at which the zones cancel perfectly in pairs
($r^2 = 2n\lambda z$): an even number of half-period zones contributes nothing on
axis.

**(d)** The area between successive zone boundaries $r_n$ and $r_{n+1}$ is
$\pi(r_{n+1}^2-r_n^2) = \pi\lambda z$ — independent of $n$. That is why each zone
contributes the same magnitude of amplitude, and why the on-axis amplitude is a
simple alternating sum of equal terms, which is the origin of equation (7).

---

## ★★★9 — Rayleigh scattering scaling

**(a)** A small scatterer responds to the incident wave as a secondary source whose
strength is proportional to its volume $a^3$ times the contrast $\epsilon$ (a
dipole/born argument). The radiated amplitude of a dipole source scales as
$k^2$, so the scattered amplitude $\propto \epsilon a^3k^2$, and the scattered
*power* $\propto \epsilon^2a^6k^4$ ✓. The $k^4$ (i.e. $f^4$) is the signature of
Rayleigh scattering.

**(b)** With number density $n$, the scattering mean free path is
$\ell = 1/(n\sigma)$ with $\sigma \propto a^6k^4$; the corresponding scattering
attenuation is $\alpha_{\text{scatt}} = 1/(2\ell) \propto n a^6k^4$, and since
$Q^{-1} = 2\alpha v/\omega$, this gives $Q_{\text{scatt}}^{-1} \propto
n a^6\omega^3$ (i.e. $Q \propto f^{-3}$), with the extra power of frequency coming
from the $1/\omega$ in the definition. **State which convention you use**: many
texts quote $Q^{-1}\propto f^4$ by absorbing a factor differently, so the
exponent quoted must be accompanied by its definition.

**(c)** A factor of ten in frequency gives a factor of $10^3$–$10^4$ in scattering
attenuation depending on convention, which is far steeper than the weak frequency
dependence of intrinsic anelastic $Q$. A measured $Q$ falling steeply with
frequency is therefore more plausibly scattering-dominated than intrinsically
anelastic — but see (d).

**(d)** The hypothesis is testable by measuring the *scattering* independently, for
example from the coda decay at fixed source–receiver distance (which is sensitive
to scattering) compared with the direct-wave decay (sensitive to total
attenuation), or by comparing $Q$ measured on body waves (short path, little
scattering) with surface waves (long path, much scattering) in the same region.
Agreement between the two would favour intrinsic attenuation.

---

## ★★★10 — Resolution versus signal-to-noise

**(a)** An empirical scaling, widely quoted in optics and imaging: the detectable
separation of two equal point sources falls with improving SNR roughly as
$\text{SNR}^{-1/4}$ for a signal-dominated experiment. State explicitly that this
is an empirical result: the exact exponent depends on the detection criterion, on
the noise statistics and on whether the estimator is maximum-likelihood.

**(b)** A suitable program: generate two Airy patterns at separation $\Delta\theta$
with amplitude 1, add zero-mean Gaussian noise of standard deviation
$\sigma = 1/\text{SNR}$ using a deterministic generator, and define "detectable"
as a dip between the two peaks of a stated depth (say 5 per cent of the peak) in
the *smoothed* profile. Report the criterion you used; a different criterion
gives a different exponent.

**(c)** Expected result: the measured detectable separation falls roughly as
$\text{SNR}^{-1/4}$ over two or three decades of SNR, with a floor at about
$\lambda/(4D)$ beyond which no improvement occurs because the information is
genuinely absent. Report your measured exponents.

**(d)** Stacking $N$ traces improves SNR as $\sqrt N$ and therefore improves the
detectable separation as $N^{-1/8}$ — a very weak gain, which is why stacking
helps detectability far more than it helps resolution, and why the answer to "can
we resolve this?" is usually "no, but we can detect it". The limit of the
improvement is the wavelength floor: no amount of stacking creates spatial
frequencies the acquisition never recorded.
