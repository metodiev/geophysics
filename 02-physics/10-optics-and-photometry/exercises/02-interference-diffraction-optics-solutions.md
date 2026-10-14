# Solutions — 02-10-02 Interference and Diffraction in Optical Instruments

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Two slits

**(a)** $\Delta y = \dfrac{\lambda L}{d}
= \dfrac{633\times10^{-9}\times1.5}{0.20\times10^{-3}} = 4.7475\times10^{-3}$ m
$= \mathbf{4.75}$ **mm**.

**(b)** $\Delta\theta = \lambda/d = 633\times10^{-9}/2.0\times10^{-4}
= 3.165\times10^{-3}$ rad $= 0.1813°$.

**(c)** The envelope's first minimum is at $\sin\theta = \lambda/a$; the
interference maxima are at $\sin\theta = m\lambda/d$. The envelope contains
fringes for $|m| < d/a$, so the number of fringes is
$2d/a = 2\times0.20/0.05 = \mathbf{8}$.

**(d)** Immersing the apparatus multiplies every optical path by $n$: the
wavelength in the medium becomes $\lambda/n$, so
$\Delta y = \lambda L/(nd) = 4.7475/1.333 = \mathbf{3.56}$ **mm** — the fringes
get *closer*. The physical reason is that the phase difference is
$(2\pi/\lambda_{\text{medium}})\,d\sin\theta$ and the shorter wavelength in the
medium increases the phase change per unit path difference.

---

## ★2 — Single slit

**(a)** $\sin\theta_1 = \lambda/a = 500\times10^{-9}/1.0\times10^{-4}
= 5.0\times10^{-3}$, so $\theta_1 = \mathbf{0.2865°}$.

**(b)** The central maximum spans $\pm\theta_1$: $2\times0.2865 = 0.5730°$.

**(c)** Linear width $= 2L\tan\theta_1 \approx
2\times1.5\times5.0\times10^{-3} = \mathbf{15.0}$ **mm**.

**(d)** Doubling the wavelength doubles the width: 30.0 mm. The width is
proportional to $\lambda/a$ with no other dependence, so a longer wavelength is
diffracted into a wider angle by the same aperture.

---

## ★3 — Aperture resolution

**(a)** $\theta_{\min} = 1.219\,669\,9\times\dfrac{600\times10^{-9}}{0.25}
= 2.9272\times10^{-6}$ rad $= \mathbf{0.604″}$.

**(b)** $2.9272\times10^{-6}\times3.84\times10^8 = \mathbf{1124}$ **m**.

**(c)** $2.9272\times10^{-6}\times600\times10^{3} = \mathbf{1.756}$ **m**.

**(d)** $\theta_{\min} = \dfrac{3.8317}{\pi}\dfrac{550\times10^{-9}}{7\times10^{-3}}
= 9.5831\times10^{-5}$ rad $= \mathbf{19.77″}$.

The diffraction limit (19.77″) is three times finer than the classical 60″
physiological limit, which means the eye is normally *not*
diffraction-limited: the limit is set by the spacing of retinal photoreceptors
and by the eye's aberrations. This is why the 60″ figure is quoted for daylight
vision, where the pupil is 2.5 mm and the diffraction limit is 55.3″ — the two
numbers coincide there, which is a coincidence of biology and optics rather than
a law.

---

## ★4 — Coherence lengths

**(a)** $l_c = \dfrac{\lambda^2}{\Delta\lambda}
= \dfrac{(800\times10^{-9})^2}{2\times10^{-9}} = 3.2\times10^{-4}$ m
$= \mathbf{0.320}$ **mm**.

**(b)** Fringes are visible for path differences **less than about 0.32 mm** —
0.32 mm of path difference is 400 wavelengths, so a bench-top interferometer
with centimetre-scale path differences sees no fringes at all with this source.

**(c)** $l_c = (800\times10^{-9})^2/0.001\times10^{-9} = \mathbf{0.640}$ **m**.

**(d)** The 2 nm source, because *white-light* interferometry deliberately uses a
broadband source and relies on the fringes appearing only where the path
difference is near zero: the position of the white-light fringe is an absolute
zero-order marker, which is the whole point of the technique. A narrowband laser
would produce fringes everywhere, removing the zero-order reference.

---

## ★5 — Reading the demo

**(a)** $q = 3.831650$ against a textbook 3.831706, and $q = 7.015725$ against
7.015587 — the located values differ from the true zeros by the quadrature's
resolution, $5.6\times10^{-5}$ and $1.4\times10^{-4}$ in $q$.

**(b)** The aperture quadrature's amplitude error for the single slit is
$2.66\times10^{-4}$, worst at $\sin\theta/(\lambda/a) = 0.876$ — i.e. near, but
not at, the first zero, where the integrand oscillates most rapidly across the
0.2 mm aperture.

**(c)** $C = 3.831\,705\,970/\pi = 1.219\,669\,9$.

**(d)** Because the far-field amplitude of a circular aperture *is* the Bessel
integral: $\int_0^a\rho J_0(k\rho\sin\theta)\,\mathrm d\rho = a^2J_1(q)/q$. The
demo evaluates the aperture integral numerically — a straightforward sum of
sines over the chord of the disk — and therefore obtains the zeros of $J_1$
as a by-product, without ever evaluating $J_1$. This is the standard way to
check a special-function identity: compute both sides and compare.

---

## ★6 — Coating design at 1000 nm

**(a)** $n_c = \sqrt{n} = \sqrt{1.70} = \mathbf{1.3038}$.

**(b)** $t = \dfrac{\lambda}{4n_c} = \dfrac{1000}{4\times1.3038}
= \mathbf{191.74}$ **nm**.

**(c)** Bare glass:
$R = \left(\dfrac{1-1.70}{1+1.70}\right)^2 = \left(\dfrac{-0.70}{2.70}\right)^2
= \mathbf{0.06722}$ (6.72 per cent).
With MgF₂ ($n_c = 1.38$):
$R = \left(\dfrac{1.70-1.38^2}{1.70+1.38^2}\right)^2
= \left(\dfrac{-0.2044}{3.6044}\right)^2 = \mathbf{0.003216}$ (0.32 per cent).

**(d)** Transmission gain
$= \dfrac{1-0.003216}{1-0.067215} = \mathbf{1.0686}$, i.e. 6.9 per cent more light
transmitted. And yes, an incorrect index can make matters worse: with
$n_c = 1.70$ (index-matched to the substrate but with the quarter-wave
condition still imposed) equation (4) of the lesson gives
$R = \left(\dfrac{1.70-2.89}{1.70+2.89}\right)^2 = 0.0672$ — no better than
bare — while a genuinely wrong, higher index returns *more* reflectance than the
bare surface.

---

## ★7 — A grating

**(a)** $N = 900\ \text{mm}^{-1}\times60$ mm $= \mathbf{54\,000}$ grooves.

**(b)** $\mathcal{R} = mN = 2\times54\,000 = \mathbf{108\,000}$.

**(c)** $\Delta\lambda = \lambda/\mathcal{R}
= 1550\ \mathrm{nm}/108\,000 = 1.435\times10^{-2}$ nm
$= \mathbf{14.35}$ **pm**.

**(d)** In first order $\mathcal{R} = 54\,000$. Going to second order doubles the
resolving power, because the resolving power is proportional to the number of
grooves *times the order*, and the second-order beam has sampled the same
grating twice. What is bought is resolution; what is paid is efficiency and
free-spectral-range: the second order overlaps the third, so the input must be
pre-filtered exactly as for the etalon of the lesson's §4. A grating is a
single-pass interference instrument and behaves like a low-finesse etalon in
this respect.

---

## ★8 — Pixels and diffraction

**(a)** $F_{\text{crossover}} = \dfrac{2p}{\lambda}
= \dfrac{2\times3.9\times10^{-6}}{600\times10^{-9}} = \mathbf{13.0}$.

**(b)** An f/4 system has $F = 4 < 13$, so the diffraction blur
($1.22\lambda F = 2.93$ µm) is *smaller* than the pixel (3.9 µm): the system is
**pixel-limited**. At f/16 the diffraction blur would be 11.7 µm, three times
the pixel, and the system would be diffraction-limited.

**(c)** GSD
$= \dfrac{3.8317}{\pi}\dfrac{550\times10^{-9}}{0.35}\times550\times10^{3}
= \mathbf{1.054}$ **m**.

**(d)** With a fixed detector, the only way to change whether the instrument is
pixel- or diffraction-limited is to change the f-number, i.e. the focal length
for a given aperture — that is, to change the field of view and the plate scale.
An imaging spectrometer that needs both a wide swath and diffraction-limited
sampling is therefore over-constrained, and the design compromise is exactly the
trade of (a)–(c): the spectral channels need a long focal length for dispersion,
while the swath needs a short one.

---

## ★★★9 — The Airy pattern from the aperture integral

**(a)** The far-field amplitude is the aperture integral

$$A(\theta) \propto \int\!\!\int_{\text{disk}}
e^{-ik(x\sin\theta)}\,\mathrm dx\,\mathrm dy .$$

Substituting $x = \rho\cos\phi$, $y = \rho\sin\phi$ gives
$\mathrm dx\,\mathrm dy = \rho\,\mathrm d\rho\,\mathrm d\phi$ and

$$A \propto \int_0^a\!\!\int_0^{2\pi}
e^{-ik\rho\cos\phi\sin\theta}\,\mathrm d\phi\;\rho\,\mathrm d\rho
= \int_0^a 2\pi J_0(k\rho\sin\theta)\,\rho\,\mathrm d\rho ,$$

using the integral representation of the Bessel function of order zero,
$\int_0^{2\pi}e^{iq\cos\phi}\mathrm d\phi = 2\pi J_0(q)$.

**(b)** With $q = ka\sin\theta$ and $u = k\rho\sin\theta$ (so
$\rho\,\mathrm d\rho = u\,\mathrm du/k^2\sin^2\theta$),

$$\int_0^a \rho J_0(k\rho\sin\theta)\,\mathrm d\rho
= \frac{1}{k^2\sin^2\theta}\int_0^q uJ_0(u)\,\mathrm du
= \frac{a^2}{q}J_1(q) ,$$

using $\dfrac{\mathrm d}{\mathrm du}\left[uJ_1(u)\right] = uJ_0(u)$. Normalising
to 1 at $q = 0$ (where $J_1(q)/q\to1/2$, so the normalisation contributes the
factor 2) gives $A(q) = 2J_1(q)/q$ and hence $I(q) = (2J_1(q)/q)^2$.

**(c)** The zeros of $J_1$: the first is $q_1 = 3.831\,705\,970$ and the second
is $q_2 = 7.015\,586\,670$. The demo's quadrature returns 3.831650 and 7.015725
— agreement to the precision the 2001-point sum supports, which is what makes
the check meaningful. The Rayleigh coefficient follows as
$q_1/\pi = 1.219\,669\,9$.

**(d)** The order of the Bessel function is fixed by the *rotational symmetry* of
the aperture, not by its size: the $\phi$ integral over a disk produces $J_0$,
and the radial integral of $\rho J_0$ produces $J_1$. A square aperture has no
such symmetry and its amplitude is the product of two sinc functions,
$\operatorname{sinc}(k a_x\sin\theta_x/2)\operatorname{sinc}(k a_y\sin\theta_y/2)$
— the one-dimensional result applied twice. This is the optical counterpart of
the aperture-shape dependence of the seismic Fresnel zone.

---

## ★★★10 — Position precision from signal-to-noise

**(a)** The relation $\sigma_\lambda \approx \Delta\lambda/(2.355\,S)$ is a
**stated result, not a derivation included here**: for a Gaussian line of
standard deviation $\sigma_\ell$ equal to FWHM/2.355, in additive Gaussian noise
of standard deviation $\sigma_n$, the maximum-likelihood (and Cramér–Rao
optimal) estimator of the line centre has variance
$\sigma_\lambda^2 = \sigma_\ell^2/S^2$ with $S$ the peak signal-to-noise ratio,
which gives $\sigma_\lambda = \sigma_\ell/S =
\Delta\lambda/(2.355\,S)$. It is exact for a known line shape and a
signal-independent, additive, Gaussian noise model, and it is an approximation
for everything else. Present it as an ansatz with those assumptions stated.

**(b)** $\sigma_\lambda = \dfrac{0.20\ \mathrm{nm}}{2.355\times100}
= 8.49\times10^{-4}\ \mathrm{nm} = \mathbf{0.849}$ **pm** at 500 nm.

**(c)** Using the Doppler relation, with the assumption that the line width is
dominated by the instrument rather than by the source:

$$\sigma_v = c\frac{\sigma_\lambda}{\lambda}
= 3\times10^8\times\frac{8.49\times10^{-4}}{500} = \mathbf{510\ m\,s^{-1}} .$$

The assumption matters: if the line were intrinsically broader than the
instrument function, the same formula with the intrinsic width would apply, and
the velocity precision would be worse.

**(d)** Resolution is what the instrument can *separate*; compositional
sensitivity is what abundance change it can *detect*, and the two differ by the
signal-to-noise ratio, the number of diagnostic features available, and the width
of each feature relative to the instrument function. A specification for a
mapping instrument must therefore state band count, band width, sampling
interval **and** SNR per band, because any one of them alone can be the binding
constraint. Lesson [02-10-04](../04-spectroscopy.md) §4 quantifies the depth loss
from a wide band and §4.2 the position error from coarse sampling.

---

## ★★★11 — Interferometric displacement

**(a)** Moving one mirror by $\Delta x$ changes the path length by $2\Delta x$
(round trip). One fringe corresponds to a phase change of $2\pi$, i.e. a path
change of $\lambda$, so

$$2\Delta x = \lambda \quad\Longrightarrow\quad \Delta x = \frac{\lambda}{2}.$$

**(b)** $\lambda/2 = 632.8/2 = \mathbf{316.4}$ **nm per fringe**.

**(c)** $316.4/1000 = \mathbf{0.316}$ **nm** — about six hydrogen-atom diameters
if the nominal atomic size of 0.05 nm is used as a yardstick. This is why
interferometry is the standard method for calibrating displacement transducers
and why it measures thermal expansion of the instrument itself as a systematic
error.

**(d)** The demo gives a coherence length of 200.218 mm for a 0.002 nm source at
632.8 nm. A 1 m arm interferometer has a round-trip path of 2 m, which is two
orders of magnitude beyond 0.2 m, so fringes would be invisible: the source
bandwidth must be reduced by two orders of magnitude (to about
$2\times10^{-5}$ nm) or the arms must be balanced to within 0.2 m. In a low-cost
instrument the first specification to relax is usually the *stabilisation* of
the laser (single-frequency operation, temperature control) rather than its
linewidth, because most of the cost of a laser is in the stabilisation, and
because a well-balanced interferometer tolerates a moderate linewidth.
