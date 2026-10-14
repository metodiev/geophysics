# Solutions — 02-04-07 Viscoelasticity, Creep and Anelastic Relaxation

Solutions to [`07-viscoelasticity-exercises.md`](./07-viscoelasticity-exercises.md).
Numbers were produced with the companion script
[`../code/viscoelasticity_demo.py`](../code/viscoelasticity_demo.py) or with
standard-library Python written for the exercise; each is quoted to the precision
the computation supports. Model parameters are **chosen**, not measured.

---

## ★1

(a) $\tau = \eta/\mu = 3\times10^{19}/4.5\times10^{10} = 6.666667\times10^{8}$ s
$= 21.125392$ years (using 1 yr $= 3.15576\times10^{7}$ s).

(b) $\gamma(t) = \sigma_0/\mu + \sigma_0 t/\eta$ with $\sigma_0 = 2$ MPa:

$$\gamma(t) = 4.444444\times10^{-5} + 6.666667\times10^{-14}\,t .$$

At $t = \tau = 6.666667\times10^{8}$ s the viscous term is
$6.666667\times10^{-14}\times6.666667\times10^{8} = 4.444444\times10^{-5}$, exactly
equal to the elastic term (a general property: at $t = \tau$ the two contributions
to the creep strain are equal). Total $\gamma(\tau) = 8.888889\times10^{-5}$.

(c) $\sigma_0 = \mu\gamma_0 = 4.5\times10^{10}\times10^{-4} = 4.500000$ MPa, and
$\sigma(t) = 4.5 e^{-t/\tau}$ MPa:

| $t$ | $\sigma$ (MPa) |
|---|---|
| 0 | 4.500000 |
| $\tau$ | 1.655457 |
| $3\tau$ | 0.224042 |

(d) Solid for $t \ll \tau$ (elastic response, no appreciable flow); fluid for
$t \gg \tau$ (steady flow at $\sigma_0/\eta$; the stress relaxes to zero at
constant strain). The crossover frequency is
$1/(2\pi\tau) = 2.387\times10^{-10}$ Hz, so **at any seismological or tectonic
frequency this element is a solid**, and only for periods of order $10^{10}$ s
($\sim$ 300 yr) do its fluid properties appear. Compare section 4 of the lesson.

---

## ★2

(a) $\gamma(t) = (\sigma_0/\mu)(1-e^{-t/\tau}) = 4.444444\times10^{-5}(1-e^{-t/\tau})$.

(b)

| $t$ | Kelvin–Voigt $\gamma$ | Maxwell $\gamma$ (★1) |
|---|---|---|
| $\tau$ | $2.809425\times10^{-5}$ | $8.888889\times10^{-5}$ |
| $3\tau$ | $4.223169\times10^{-5}$ | $1.777778\times10^{-4}$ |

Kelvin–Voigt strains *less* and *approaches a limit*; Maxwell strains without
bound.

(c) $\gamma(\infty) = \sigma_0/\mu = 4.444444\times10^{-5}$ — bounded, so the
element is a solid.

(d) $Q = 1/(\omega\tau)$:

| $f$ | $Q$ |
|---|---|
| 1 Hz | $2.387324\times10^{-10}$ |
| 10 Hz | $2.387324\times10^{-11}$ |
| 100 Hz | $2.387324\times10^{-12}$ |

$Q \ll 1$ at every seismic frequency: the element is dashpot-dominated, i.e.
essentially a fluid, which is the opposite of rock behaviour ($Q$ of order tens to
hundreds). To obtain $Q = 200$ at 10 Hz one would need
$\tau = 1/(2\pi f Q) = 7.957747\times10^{-5}$ s and therefore
$\eta = \mu\tau = 3.58\times10^{6}$ Pa s — many orders of magnitude below any rock
viscosity (compare $10^{18}$–$10^{21}$ Pa s for the mantle). **A single
Kelvin–Voigt element cannot simultaneously give a rock-like $Q$ at seismic
frequencies and a rock-like viscosity**, because its $Q$ is inversely
proportional to frequency and to $\tau$ while its viscosity is proportional to
$\tau$.

---

## ★3

(a) With $x = \omega\tau_\sigma$ and $\Delta = \tau_\varepsilon/\tau_\sigma - 1$
(equation 14),

$$Q(x) = \frac{1+x^2(1+\Delta)}{x\Delta} = \frac{1}{\Delta}\left(\frac{1}{x} +
(1+\Delta)x\right),
\qquad \frac{\mathrm dQ}{\mathrm dx} = \frac{1}{\Delta}\left(-\frac{1}{x^2} +
(1+\Delta)\right) .$$

Setting the derivative to zero: $x^2 = 1/(1+\Delta)$, so
$x = 1/\sqrt{1+\Delta}$ ✓.

(b)

$$Q_{\min} = \frac{1}{\Delta}\left(\sqrt{1+\Delta} +
\frac{1+\Delta}{\sqrt{1+\Delta}}\right)
= \frac{1}{\Delta}\left(2\sqrt{1+\Delta}\right)
= \frac{2\sqrt{1+\Delta}}{\Delta} . \ \square$$

(c) $\mathrm d^2Q/\mathrm dx^2 = 2/(\Delta x^3) > 0$ for $x>0$, so the stationary
point is a minimum ✓. This is the *attenuation peak*, since $Q^{-1}$ is
maximised there.

(d) $2\sqrt{1+\Delta}/\Delta = 30$. Squaring after rearranging,
$4(1+\Delta) = 900\Delta^2$, i.e. $900\Delta^2 - 4\Delta - 4 = 0$, giving
$\Delta = 0.068925916$ (positive root). The modulus ratio is
$G_U/G_R = 1+\Delta = 1.068925916$, i.e. a **6.89 per cent** stiffness contrast
between the relaxed and unrelaxed limits.

*Cross-check with the demo:* the demo prints
`relaxed modulus M(0) = 30.000000 GPa, unrelaxed modulus M(inf) = 32.067777 GPa,
contrast Delta = 0.068925916`, and $32.067777/30.000000 - 1 = 0.0689259$ ✓.

---

## ★4

(a) For $\gamma(t) = \gamma_0\sin\omega t$ and
$M = M'(1+i/Q)$, the dissipative (in-quadrature) stress is
$M''\gamma_0\cos\omega t$ with $M'' = M'/Q$. The energy dissipated per cycle is

$$\Delta E = \oint \sigma\,\mathrm d\gamma
= \int_0^{2\pi/\omega} M''\gamma_0\cos\omega t\;\gamma_0\omega\cos\omega t\;\mathrm dt
= \pi M''\gamma_0^2 = \frac{\pi M'\gamma_0^2}{Q} ,$$

and the peak stored energy is $E_{\text{stored}} = \tfrac12 M'\gamma_0^2$. Hence

$$\frac{2\pi E_{\text{stored}}}{\Delta E}
= \frac{2\pi\cdot\tfrac12 M'\gamma_0^2}{\pi M'\gamma_0^2/Q} = Q . \ \square$$

(b) By construction $\tan\delta = M''/M' = 1/Q$, so $Q = 1/\tan\delta$. For small
$\delta$, $\tan\delta = \delta + O(\delta^3)$, so $Q \approx 1/\delta$ with a
relative error of order $\delta^2/3$.

(c) At $Q = 5$: $\delta = \arctan(1/5) = 0.197395560$ rad,
$1/\delta = 5.065970$, so the approximation errs by **1.319 per cent**.

(d) For $Q < 1$ (a fluid-like material: water, the outer core, a melt) the
imaginary part exceeds the real part, and conventions based on $M'/M''$ and
$M''/M'$ give *reciprocal* answers — one greater than one, the other less. Since
neither is small, the ambiguity is not a small correction: quoting "$Q = 3$"
without the convention (or quoting $Q^{-1}$, the internal friction, instead) can
be wrong by a factor of 9. In fluid acoustics and in outer-core attenuation work
the convention is normally stated explicitly for this reason.

---

## ★5

(a) From section 1 of the demo:

- $\tau = \eta/\mu = 33333333.3$ s $= 1.0563$ years.
- Maximum $|$numerical $-$ analytic$|$ over $3\tau$: $1.601\times10^{-8}$ Pa.
- On a 1 MPa signal that is a relative residual of
  $1.6\times10^{-14}$ — round-off, not truncation.

The line-by-line table shows $|\sigma - \sigma_0e^{-t/\tau}|$ of order
$10^{-9}$–$10^{-8}$ Pa at $t/\tau = 0, 0.5, 1, 1.5, 2, 2.5, 3$.

(b) The viscosity recovered from the steady strain rate is
$1.000000\times10^{18}$ Pa s, identical to the input $1.0\times10^{18}$ Pa s; the
strain-rate column is constant at $1.000000\times10^{-12}$ s⁻¹, as a steady state
requires.

(c) Under constant stress, $\dot\gamma = \dot\sigma/\mu + \sigma/\eta$ with
$\dot\sigma = 0$ gives $\dot\gamma = \sigma_0/\eta$, so
$\gamma(t) = \sigma_0/\mu + \sigma_0 t/\eta$. The two quantities read off a creep
curve are therefore the **intercept** $\sigma_0/\mu$ (the elastic compliance, hence
$\mu$) and the **slope** $\sigma_0/\eta$ (hence $\eta$).

(d) Because both the numerical and analytic curves are solutions of the *same*
constitutive ODE: the test measures the integrator's accuracy, not the adequacy of
the Maxwell model. A constitutive model is tested against data, or against
independently derived predictions such as the frequency-domain $\tan\delta$
behaviour, not against its own analytic solution. The SLS section of the demo is
the one that tests a *derived* prediction (equation 16) against a computation
performed a different way.

---

## ★6

(a) Relaxed modulus $M(0) = 30.000000$ GPa, unrelaxed modulus
$M(\infty) = 32.067777$ GPa, contrast $\Delta = 0.068925916$,
$V(f_0) = 3452.9500$ m s⁻¹ at $f_0 = 10$ Hz with $\rho = 2600$ kg m⁻³.

(b) Equation (16): $Q(f) = \tfrac12 Q_{\min}(f/f_{\min} + f_{\min}/f)$ with
$Q_{\min} = 30$, $f_{\min} = 10$ Hz:

| $f$ (Hz) | $Q$ from equation (16) | demo's $Q(f)$ |
|---|---|---|
| 1 | $\tfrac12(0.1+10)\times30 = 151.5$ | 151.5000 |
| 5 | $\tfrac12(0.5+2)\times30 = 37.5$ | 37.5000 |
| 10 | $\tfrac12(1+1)\times30 = 30.0$ | 30.0000 |
| 50 | $\tfrac12(5+0.2)\times30 = 78.0$ | 78.0000 |
| 100 | $\tfrac12(10+0.1)\times30 = 151.5$ | 151.5000 |

Exact agreement at every frequency ✓ — the identity is algebraic, so the agreement
tests the implementation, and the fact that it holds confirms that the demo's
element really is the SLS with $Q_{\min} = 30$ at 10 Hz.

(c) $V(100\ \text{Hz})/V(1\ \text{Hz}) - 1 = 3510.7477/3397.9159 - 1 =
3.320618$ per cent (observed: 3.3206 per cent printed). The full
relaxed-to-unrelaxed contrast is $\sqrt{1+\Delta}-1 = 3.388873$ per cent. The
measured band figure is slightly smaller because 1 Hz and 100 Hz are one decade
either side of the minimum rather than the true $\omega \to 0$ and $\omega \to
\infty$ limits.

(d) The largest difference is $8.493\times10^{-3}$ at $f = 1$ Hz, where
$\ln(f/f_0) = -2.302585$. At that point the predicted change is $-0.024431$ and
the measured change $-0.015938$, i.e. the approximation overstates the effect by
53 per cent *of the measured effect*. The next-largest is $-7.693\times10^{-3}$ at
100 Hz, the mirror image.

---

## ★7

(a) $\alpha = \pi f/(QV)$:

| $f$ | $\alpha$ (m⁻¹) | over 1 km, $20\log_{10}$ |
|---|---|---|
| 10 Hz | $3.926991\times10^{-5}$ | $-0.341094$ dB |
| 100 Hz | $3.926991\times10^{-4}$ | $-3.410941$ dB |

(b) $10\log_{10}e^{-2\alpha x}$ with $x = 1000$ m: $-0.341$ dB at 10 Hz and
$-3.411$ dB at 100 Hz. The loss scales **linearly with frequency** at fixed $Q$,
which is why high frequencies are lost first and why absorption acts as a
low-pass filter.

(c) With $V(f) = V(f_0)[1 + \frac{1}{\pi Q}\ln(f/f_0)]$ and $f_0 = 10$ Hz:

$$V(1\ \text{Hz}) = 4000\left(1 - \frac{2.302585}{628.3185}\right) = 3985.3413\
\text{m s}^{-1}, \qquad V(100\ \text{Hz}) = 4014.6587\ \text{m s}^{-1}.$$

*Regime.* The relation assumes $Q \gg 1$ (here $Q = 200$ ✓) and that $Q$ is
independent of frequency (given in the question ✓). At $|\ln(f/f_0)| = 2.3$ we are
at the edge of the "within a factor of a few" condition: the demo's test at
$Q = 30$ one decade from $f_0$ produced an error 35 per cent of the effect, and if
that error scales as $1/Q$ — as the Kramers–Kronig expansion implies — the error
here is about 5 per cent of the effect, i.e. of order $2\times10^{-4}$ in
$V/V_0$, or about 1 m s⁻¹. That is small but not negligible for a $Q$ study, and
the scaling statement is an extrapolation from one test case, not a proof.

(d) A 20 dB amplitude loss over 1 km at 10 Hz means
$e^{-\alpha(1000)} = 10^{-1}$, so $\alpha = \ln(10)/1000 = 2.302585\times10^{-3}$
m⁻¹ and

$$Q = \frac{\pi f}{\alpha V} = \frac{\pi(10)}{2.302585\times10^{-3}(4000)} =
3.410941 .$$

$Q \approx 3.4$ is far below any rock value; a medium with that attenuation is
closer to a fluid than to a solid, and it is the regime where the $Q \gg 1$
relations of section 5 of the lesson must be replaced by the exact
Kramers–Kronig treatment.

---

## ★8

(a) $\tau = \eta/\mu = 10^{21}/7\times10^{10} = 1.428571\times10^{10}$ s
$= 452.6525$ years (demo prints 452.7 years). Then

| phenomenon | period | $\omega\tau$ |
|---|---|---|
| seismic wave (30 Hz) | $3.333\times10^{-2}$ s | $2.692794\times10^{12}$ |
| solid-earth tide (M2) | $4.471\times10^{4}$ s | $2.007600\times10^{6}$ |
| postglacial rebound | $3.156\times10^{11}$ s ($10^4$ yr) | $2.844100\times10^{-1}$ |

The demo prints 2.693e+12, 2.008e+06 and 0.284 — identical to the precision shown.

(b) $\omega\tau = 1$ at $T = 2\pi\tau = 8.977\times10^{10}$ s $= 2844.1$ years. A
deformation experiment at that timescale would see a stress relaxing by a factor
$e$ over a few thousand years: both the elastic and the viscous terms would
contribute comparably, and neither the elastic nor the viscous idealisation would
be adequate. That is the regime of glacial-isostatic adjustment and of the
longest-period parts of the earthquake cycle.

(c) With $\eta = 10^{20}$ Pa s: $\tau = 1.428571\times10^{9}$ s $= 45.2653$ years;
$\omega\tau = 2.692794\times10^{11}$ (seismic), $2.007600\times10^{5}$ (tide),
$2.844100\times10^{-2}$ (rebound). **The classification of all three regimes is
unchanged** — elastic, elastic, viscous — because reducing $\eta$ by a factor of
ten multiplies every $\omega\tau$ by the same factor, and all three were far from
1 in the same direction. Only a change large enough to bring a timescale through
$\omega\tau = 1$ would change a regime label; here the rebound case moves from
0.28 to 0.028, i.e. deeper into the viscous regime.

(d) The Maxwell $Q = \omega\tau \approx 2.7\times10^{12}$ at 30 Hz means
essentially no attenuation at seismic frequencies. Observed seismic $Q$ in the
mantle is many orders of magnitude smaller (and varies with frequency and region).
Therefore:

- The viscosity inferred from postglacial rebound (a long-time, large-strain,
  high-temperature flow property) and seismic attenuation (a small-strain,
  high-frequency, wave property) are **not two readings of one number**; they
  correspond to different microscopic processes.
- One cannot invert seismic $Q$ for viscosity, or rebound viscosity for
  attenuation, without a specific mechanism-based model linking them.
- The observation is not a defect of the Maxwell element as a *rheological* model
  — it describes creep well — but of using a single relaxation mechanism to cover
  twelve orders of magnitude in frequency.

---

## ★9

(a) For $N$ standard linear solids in parallel, stresses add at common strain, so
the moduli add:

$$G^*(\omega) = \sum_{k=1}^{N} G_{R,k}\frac{1+i\omega\tau_{\varepsilon,k}}
{1+i\omega\tau_{\sigma,k}}, \qquad
G' = \sum_k G'_k, \qquad G'' = \sum_k G''_k,$$

and $Q = (\sum_k G'_k)/(\sum_k G''_k)$. Note that $Q$ of the sum is **not** the sum
of the $Q$'s: the aggregate is a weighted average of the $G''/G'$ ratios with
weights $G'_k/\sum G'$.

(b) Three elements with $Q_{\min} = 30$ at $f_{\min} = 1$, 10 and 100 Hz,
$\tau_{\varepsilon,k}\tau_{\sigma,k} = 1/\omega_{\min,k}^2$, and equal relaxed
moduli:

| $f$ (Hz) | $Q$ three elements | $Q$ single (10 Hz) element |
|---|---|---|
| 0.1 | 408.9105 | 1500.1500 |
| 1 | 72.7301 | 151.5000 |
| 10 | 64.4944 | 30.0000 |
| 100 | 75.1159 | 151.5000 |
| 1000 | 409.2153 | 1500.1500 |

Over 0.1–1000 Hz the three-element model has $Q$ between 64.49 and 409.22 (a ratio
of 6.35), against 30.00 to 1500.15 (a ratio of 50.01) for the single element: the
superposition **flattens $Q$ by roughly a factor of eight in the ratio**, and
brings the minimum up from 30 to 64.5 because equal-weight addition of three
elements with the same peak attenuation is not the same as one element with
$Q_{\min} = 30$.

(c) Two things determine the flatness: the **density of elements per decade** and
the **range of $f_{\min}$** covered. Both must span the band of interest with
enough overlap that the sums of $G'$ and $G''$ are smooth; the price is that each
additional element adds two parameters ($G_{R,k}$ and $f_{\min,k}$, with $Q_{\min}$
or implicitly the contrast as a third), and the number of elements needed grows
with the required dynamic range and with how tight the tolerance on $Q$ is. The
limiting case of infinitely many elements with a specified density is the
continuous "constant-$Q$" model; a discrete implementation is an approximation to
it, chosen so that the aggregate $Q$ meets the tolerance over the band.

(d) Numerical verification (standard library only; complex arithmetic is a
built-in language feature, not a third-party dependency): the values in the table
above were computed with $G^*_k = G_{R,k}(1+i\omega\tau_{\varepsilon,k})/(1 +
i\omega\tau_{\sigma,k})$, $\tau$ values from
$\tau_{\varepsilon,\sigma} = (\sqrt{1+1/Q_{\min}^2} \pm 1/Q_{\min})/\omega_{\min}$,
and $Q = \Re G^*/\Im G^*$ — the same recipe as the demo's section 3, applied to
three terms. Measured dispersion over the band: $V(1000)/V(0.1)-1 = 3.366$ per cent
for the three-element model, against 3.388 per cent for the single element: adding
elements over a finite band does **not** increase the total dispersion, because the
total relaxed-to-unrelaxed modulus contrast is set by the sum of the individual
contrasts and the band covered.

---

## ★10

(a) Intrinsic (energy converted to heat inside the material) versus apparent
(energy removed from the direct arrival by redistribution):

| mechanism | type | frequency dependence (qualitative) |
|---|---|---|
| (i) grain-boundary sliding | intrinsic | peak at a frequency set by grain size and boundary viscosity; broader than a single Debye peak |
| (ii) squirt flow between cracks and pores | intrinsic | peak near the frequency at which the fluid pressure equilibrates between crack and pore; strongly dependent on aspect ratio and saturation |
| (iii) thin-layer interference | apparent | periodic in frequency with period set by the two-way travel time through the layer; can be either a loss or a gain at a given frequency |
| (iv) scattering by heterogeneities of size $\sim$ wavelength | apparent | strongest in the Rayleigh-to-Mie transition; approximately Rayleigh ($f^4$) at long wavelengths and roughly flat at shorter ones |
| (v) thermoelastic relaxation | intrinsic | peak at a frequency set by the thermal diffusion length relative to the heterogeneity scale; weak in most rocks at seismic frequencies |

(b) **Squirt flow** (ii): under a passing wave the compliant (crack) pores are
squeezed more than the stiff (equant) pores, which drives fluid between them;
at low frequency the pressure has time to equilibrate and the rock behaves as if
the fluid were uniformly distributed (Gassmann limit), and at high frequency the
fluid cannot move and the rock is stiffer (unrelaxed limit). The peak is where the
forcing period matches the pressure-diffusion time across the crack, so the
controlling parameter is the crack aspect ratio (equivalently, the ratio of the
fluid-pressure-equilibration time, of order $\eta_f a^2/(K_f \kappa)$ for crack
radius $a$, permeability $\kappa$ and fluid viscosity $\eta_f$, to the wave
period). This is why the peak moves with saturation, viscosity and permeability —
and why the effect is much larger in partially saturated rock. The derivation is
in the rock-physics literature, not reproduced here; the estimate above is
dimensional analysis, stated as such.

(c) **A separating experiment.** Take a cylindrical core of a layered
sandstone/shale composite with a known layer thickness $d$ and sample length
$L$. (i) Measure the dynamic modulus and $Q$ in forced-oscillation or resonant-bar
mode over a band spanning the layer-interference period
$f_{\text{int}} \approx v/(2d)$ and the intrinsic relaxation peaks. (ii) $Q$ from
layer interference must scale with the number of layers $L/d$ and must *vanish*
when the sample is replaced by a homogeneous mixture of the same constituents with
the same bulk density and moduli; intrinsic $Q$ must be nearly independent of
$L/d$ and must persist in the homogeneous sample. So the observable to compare is
$Q(L/d)$ versus $Q$ of the homogenised sample at the same frequency. A second,
independent discriminator: intrinsic attenuation scales with frequency as
predicted by the mechanism, whereas interference attenuation peaks at discrete
frequencies fixed by the geometry.

(d) A single-frequency measurement cannot determine **the frequency dependence**,
and it therefore cannot distinguish a mechanism whose signature is spectral
(intrinsic relaxation with a peak, scattering, interference) from another that
happens to give the same $Q$ at that one frequency. It also cannot separate the
real (dispersive) part from the imaginary (dissipative) part, since a
single-frequency modulus measurement returns one complex number. At least two
frequencies — and in practice a band spanning at least a decade — are needed to
identify a mechanism, and the identification is only as good as the assumed
model family.
