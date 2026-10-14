# Solutions — 02-10-01 Geometrical Optics, Refraction and Lenses

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Refraction out of water

Snell's law: $\sin\theta_2 = (n_1/n_2)\sin\theta_1$ with $n_1 = 1.333$,
$n_2 = 1.000293$.

**(a)** $\sin\theta_2 = 1.333\times0.5/1.000293 = 0.666305$, so
$\theta_2 = 41.7825°$.

**(b)** $\sin\theta_2 = 1.333\times0.707107/1.000293 = 0.942085$, so
$\theta_2 = 70.4410°$.

**(c)** $\sin\theta_2 = 1.333\times0.766044/1.000293 = 1.02077 > 1$: no real
refracted angle, so **total internal reflection**. The transmitted wave is
evanescent and carries no net energy into the air.

**(d)** $\sin\theta_2 = 1.333\times0.750111/1.000293 = 0.999392$, so
$\theta_2 = 88.3899°$ — the ray emerges almost parallel to the surface.

**Critical angle.** With $n_2 = 1.000293$,
$\theta_c = \arcsin(1.000293/1.333) = 48.6257°$. With $n_2 = 1$ exactly,
$\theta_c = \arcsin(1/1.333) = 48.6066°$. The difference is $0.019°$, or 1.1
arcmin: small enough to ignore in a qualitative discussion, large enough to
matter if you are fitting a critical-angle refractometer to three decimal
places. The correct practice is to state the second medium's index, and air at
ambient conditions is not 1.

---

## ★2 — A step-index fibre

**(a)** $\mathrm{NA} = \sqrt{1.470^2-1.455^2}
= \sqrt{0.015\times2.925} = \sqrt{0.043875} = \mathbf{0.209465}$.

**(b)** $\theta_{\text{accept}} = \arcsin(0.209465) = \mathbf{12.0909°}$.

**(c)** $V = \dfrac{2\pi a}{\lambda}\mathrm{NA}
= \dfrac{2\pi\times3.0\times10^{-6}}{1.3\times10^{-6}}\times0.209465
= 14.503\times0.209465 = \mathbf{3.0372}$.
The approximate mode count is $M \approx V^2/2 = 4.6$, i.e. of order five
modes.

**(d)** $\lambda_c = \dfrac{2\pi a\,\mathrm{NA}}{2.4048}
= \dfrac{2\pi\times3.0\times10^{-6}\times0.209465}{2.4048}
= 1.6418\ \mu\text{m}$.

At 1300 nm the operating wavelength is **below** the cutoff of 1642 nm, so
$V = 3.04 > 2.4048$ and the fibre is **multimode**. To make it single-mode at
1300 nm the core radius would have to fall to
$a = 2.4048\lambda/(2\pi\,\mathrm{NA}) = 2.38\ \mu$m, or the index step would
have to be reduced.

---

## ★3 — A 35 mm lens

**(a)** $s' = \left(\frac1f-\frac1s\right)^{-1}
= \left(\frac{1}{0.035}-\frac{1}{2.0}\right)^{-1}
= \left(28.5714 - 0.5\right)^{-1} = \mathbf{35.6234}$ **mm**.

**(b)** $m = -s'/s = -0.0356234/2.0 = \mathbf{-0.017812}$.

**(c)** A 1 m object images to $|m|\times1.0 = \mathbf{17.812}$ **mm** on the
sensor.

**(d)** $F = f/D = 35/25 = \mathbf{1.4}$. The diffraction-limited spot
diameter is $2\times1.2197\lambda F = 2.4394\times550\times10^{-9}\times1.4
= 1.878$ µm — the demo computes the first-null *radius* as 0.939 µm, and the
diameter as twice that. Note that a real f/1.4 lens is not diffraction-limited
at the centre of the field: geometric aberrations are far larger than 1.9 µm at
full aperture, which is the point of §3.1 of the lesson — diffraction is a floor,
not a prediction.

---

## ★4 — A window and a pool

**(a)** $\sin\theta_2 = \sin30°/1.52 = 0.328947$, so $\theta_2 = 19.2049°$.

**(b)** $d = t\dfrac{\sin(\theta_1-\theta_2)}{\cos\theta_2}
= 12\ \text{mm}\times\dfrac{\sin(10.7951°)}{0.944295}
= 12\times\dfrac{0.187310}{0.944295} = \mathbf{2.380}$ **mm**.

Note that this must equal the demo's 30° row scaled from 10 mm to 12 mm:
$1.982359\times1.2 = 2.379$ mm ✓. Checking a new case by scaling a computed case
is the cheapest verification available and catches unit and algebra slips
immediately.

**(c)** At normal incidence $\theta_1 = \theta_2 = 0$, so
$\sin(\theta_1-\theta_2) = 0$ and the displacement is **zero**. This is why a
window can be placed at a pupil: on axis it is optically neutral, and only the
off-axis rays are displaced. It is also why a window *cannot* be corrected by
tilting — tilting introduces a displacement on axis.

**(d)** $d_{\text{app}} = d_{\text{real}}/n = 3.0/1.333
= \mathbf{2.2506}$ **m**.

---

## ★5 — Reading the demo

**(a)** $R = 0.02033$ at normal incidence. At 30° of incidence the refracted
angle is **22.0369°**, and the unpolarised reflectance is 0.02139.

**(b)** Brewster angle $= \arctan(1.333/1.000293) = \mathbf{53.115°}$; there
$R_s = 0.0781$ and $R_p = 0$ (numerically $4.8\times10^{-33}$).

**(c)** $\mathrm{NA} = 0.128460$, acceptance half-angle $7.3806°$,
$V = 2.1350$, cutoff wavelength $1376.1$ nm.

**(d)** The reflection at the water surface is polarised: at and near the
Brewster angle $R_p$ vanishes while $R_s$ does not. Glint, which is *reflected*
light, therefore carries mostly s-polarisation; light that has entered the water
and been scattered back out by the water body is multiply scattered and
essentially unpolarised. A polariser that rejects s-polarised light removes the
glint much more strongly than it removes the signal, which is exactly the
discrimination ocean-colour radiometry needs.

---

## ★6 — A large-core multimode fibre

**(a)** $V = \dfrac{2\pi\times50\times10^{-6}}{850\times10^{-9}}\times0.20
= 369.6\times0.20 = \mathbf{73.9}$.

**(b)** $M \approx V^2/2 = 2732$, i.e. of order 2700 guided modes.

**(c)** $\lambda_c = \dfrac{2\pi a\,\mathrm{NA}}{2.4048}
= \dfrac{2\pi\times50\times10^{-6}\times0.20}{2.4048} = 26.13\ \mu$m. The fibre
is multimode at every wavelength of practical interest; to reach single-mode
operation the core radius would have to shrink from 50 µm to
$2.4048\times850\times10^{-9}/(2\pi\times0.20) = 1.63\ \mu$m.

**(d)** Each mode propagates with a different group delay, so the phase of the
light returning from any section of fibre is a sum of several mode phases and
the measured phase is speckle, not strain: a multimode fibre has no single
optical phase to measure.

---

## ★7 — A satellite imager

**(a)** $\theta_{\min} = 1.2197\dfrac{\lambda}{D}
= 1.2197\times\dfrac{550\times10^{-9}}{0.30} = 2.236\times10^{-6}$ rad
$= 0.461″$.

**(b)** GSD $= \theta_{\min}\times h = 2.236\times10^{-6}\times700\times10^3
= \mathbf{1.565}$ **m**.

**(c)** The diffraction-limited GSD is 1.565 m and the pixel projects to 10 m.
Since the pixel is more than six times coarser than the diffraction blur, the
instrument is **pixel-limited**: the aperture delivers resolution the detector
cannot sample, and the quoted 10 m product is a sampling limit, not an optical
one. The design lever for a sharper product is a longer focal length or a finer
pixel, not a larger mirror.

**(d)** $\theta_{\min} = 1.2197\times550\times10^{-9}/0.25
= 2.683\times10^{-6}$ rad, so GSD $= 2.683\times10^{-6}\times500\times10^3
= \mathbf{1.342}$ **m**.

---

## ★8 — Reading the demo

**(a)** 3.353618 mm at 45° for the 10 mm slab.

**(b)** The apparent-depth factor is **0.7502** (i.e. $1/1.333$).

**(c)** $4.5\times0.7502 = 3.376$ m. Cross-check with ★4(d):
$3.0\times0.7502 = 2.2506$ m, and $3.376/4.5 = 0.7502$ — the factor is
independent of depth, as it must be for a flat interface, so the two answers
are consistent.

**(d)** Any instrument with a window ahead of a detector: a borehole camera or
video logger behind a pressure window; a spectrometer behind a sapphire or
fused-silica port; an underwater housing; a laser interferometer's vacuum
window. In each case the off-axis image is displaced by a wavelength-dependent
amount (because $n(\lambda)$ differs), which produces both a geometric
distortion and a chromatic shift unless the window is placed at a pupil or
calibrated out.

---

## ★★★9 — Reflectance from impedance, and the cost of uncoated optics

**(a)** At normal incidence, the amplitude reflection coefficient of a
discontinuity in wave impedance is

$$r = \frac{Z_2-Z_1}{Z_2+Z_1},$$

which follows from continuity of the tangential electric and magnetic fields at
the interface. With $Z = Z_0/n$ for a non-magnetic dielectric,

$$r = \frac{1/n_2-1/n_1}{1/n_2+1/n_1} = \frac{n_1-n_2}{n_1+n_2},$$

and the intensity reflectance is
$R = |r|^2 = \left(\dfrac{n_1-n_2}{n_1+n_2}\right)^2$. This is the same
impedance-mismatch algebra that gives the normal-incidence reflection
coefficient of a seismic interface, with $Z = \rho v$ in place of $Z_0/n$: the
formulas are identical because the boundary conditions are identical.

**(b)** $R = \left(\dfrac{1-1.52}{1+1.52}\right)^2
= \left(\dfrac{-0.52}{2.52}\right)^2 = 0.042580$, i.e. **4.258 per cent**.

**(c)** The first-order (ignoring multiple reflections between surfaces)
transmission of 12 surfaces is $(1-R)^{12} = 0.5932$, i.e. **40.7 per cent
lost**. The more careful incoherent treatment, which sums the internal
multiple reflections of each element and then multiplies the six elements
together, gives $\left(\dfrac{1-R}{1+R}\right)^{6} = 0.5997$ — the same answer
to 1 per cent, which is why the simple product is the standard estimate.
Assumption: reflections are incoherent (thicknesses far larger than a
wavelength), so intensities rather than amplitudes add.

**(d)** A lens system that throws away 40 per cent of the light before it
reaches the detector is paying for that loss twice: in exposure time and in
noise. A quarter-wave coating of the right index reduces 4.26 per cent to about
1.26 per cent per surface with one layer, and multi-layer stacks reduce it
further, so the 12-surface transmission rises from 0.59 to above 0.9 and the
instrument becomes radiometrically and photonically viable
([02-10-02](../02-interference-diffraction-optics.md) §1.3).

---

## ★★★10 — Atmospheric refraction and the flat-layer trap

**(a)** The flat-layer invariant $n\sin\theta = \text{const}$ gives, at the top
of the atmosphere where $n = 1$, $\sin\theta_{\text{top}} = n_0\sin\theta_0$.
A ray escapes only if $\sin\theta_{\text{top}} \le 1$, so

$$\theta_0 \le \arcsin(1/n_0) = \arcsin(1/1.000293) = 88.6132° .$$

The flat-layer model therefore predicts that every ray within **1.3868°** of the
horizon is total-internally-reflected and cannot reach space — a trapped zone
that would make the sky near the horizon a mirror.

**(b)** The model is wrong because the atmosphere is *spherical*: the invariant
for a spherically symmetric medium is $n\,r\sin\theta = \text{const}$ with $r$
the geocentric distance, and $r$ grows with height. The extra factor $r/R$
allows the grazing rays to escape, which is exactly why the sky is bright at the
horizon rather than mirror-like.

**(c)** The escape condition becomes $n_0\sin\theta_0 \le r_{\text{top}}/R_\oplus$.
With $R_\oplus = 6371$ km and an effective top of the atmosphere at
$h = 100$ km, $r_{\text{top}}/R_\oplus = 1.01570$, so
$n_0\sin\theta_0 \le 1.01570$ is satisfied for *every* zenith angle including
90° — all rays escape. Even with a modest $h = 8$ km the ratio is 1.00126, which
still exceeds $n_0\sin\theta_0 \le n_0 = 1.000293$. Statement: the spherical
factor exceeds $n_0$ at sea level for any realistic atmosphere height, so
grazing rays are never trapped.

**(d)** Because the bending of a grazing ray is the accumulated refraction along
its whole path, and that path samples the entire vertical profile of $n$, which
depends on temperature, pressure, humidity and their gradients. The horizon
refraction is therefore a weather-dependent quantity, of order half a degree
(commonly quoted as about 34 arcmin under standard conditions) but changing by
arcminutes as the profile changes. This is why refraction corrections for
astrometry, precise levelling and satellite laser ranging are computed from an
atmospheric model with measured surface meteorology, and never from a constant.

---

## ★★★11 — Designing a single-mode fibre

**(a)** From $\lambda_c = \dfrac{2\pi a\,\mathrm{NA}}{2.4048}$,

$$\mathrm{NA} = \frac{2.4048\,\lambda_c}{2\pi a}
= \frac{2.4048\times1.300\times10^{-6}}{2\pi\times4.5\times10^{-6}}
= \mathbf{0.110568} .$$

**(b)** With $\mathrm{NA} \approx n_1\sqrt{2\Delta}$ and $n_1 \approx 1.45$,

$$\Delta \approx \frac{\mathrm{NA}^2}{2n_1^2}
= \frac{0.110568^2}{2\times1.45^2} = \frac{0.012225}{4.205} = 0.002907,$$

i.e. an index step $n_1\Delta = 1.45\times0.002907 = 0.004215$, so
$n_1 = 1.45$ and $n_2 \approx 1.4458$. (Using the exact form
$\Delta = (n_1-n_2)/n_1$ with $\mathrm{NA} = \sqrt{n_1^2-n_2^2}$ gives an
absolute step of 0.004216, agreeing to three significant figures — the
small-index-difference approximation is good to $O(\Delta^2)$.)

**(c)** $V = \dfrac{2\pi\times4.5\times10^{-6}}{1.55\times10^{-6}}\times0.110568
= 18.243\times0.110568 = \mathbf{2.0169}$, below 2.4048: the fibre is
**single-mode** at the operating wavelength, and becomes multimode only for
wavelengths shorter than 1300 nm.

**(d)** At 400 nm, $V = 2.0169\times(1550/400) = 7.815$, so
$M \approx V^2/2 = 30.5$, i.e. about 30 modes. This does not matter for the
intended application, because the fibre is used at 1550 nm where it is
single-mode; but it does matter if the same fibre is used with a visible
alignment laser, a common laboratory practice, because the light then
propagates multimodally and the alignment does not represent the 1550 nm mode
field.
