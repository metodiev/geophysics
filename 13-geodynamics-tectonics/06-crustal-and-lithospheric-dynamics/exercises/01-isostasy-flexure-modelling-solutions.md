# Solutions — 13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength

> **Read after attempting the exercises.** Numbers were computed with the same
> formulas as the lesson's demonstration.

Lesson: [01 Isostasy and Flexure](../01-isostasy-flexure-modelling.md).

---

## ★1 — Airy root

$$\rho_c h = (\rho_m-\rho_c)r \quad\Longrightarrow\quad
r = \frac{\rho_c}{\rho_m-\rho_c}h
= \frac{2800}{3350-2800}\times3 = \frac{2800}{550}\times3 = 5.091\times3
= \mathbf{15.27\ km}.$$

The ratio $r/h = 5.091$ is larger than the lesson's 4.500 because the density
contrast at the Moho is smaller (550 against 600 kg/m³), so a thicker root is
needed to provide the same buoyancy.

---

## ★2 — Flexural rigidity

$$12(1-\nu^2) = 12(1-0.0625) = 11.25,$$

$$D = \frac{70\times10^{9}\times(3.0\times10^{4})^3}{11.25}
= \frac{70\times10^{9}\times2.70\times10^{13}}{11.25}
= 1.68\times10^{23}\ \mathrm{N\,m}.$$

Units: $\mathrm{Pa}\times\mathrm{m^3} = \mathrm{N\,m^{-2}\,m^3} = \mathrm{N\,m}$,
a bending stiffness. (A useful check: $D$ scales as $T_e^3$, so $T_e = 25$ km
gives $D = 1.68\times10^{23}\times(25/30)^3 = 9.72\times10^{22}$ N m, matching
the lesson's table.)

---

## ★3 — Flexural parameter and compensation wavelength

$$\alpha = \left(\frac{1.68\times10^{23}}{500\times9.81}\right)^{1/4}
= \left(3.425\times10^{19}\right)^{1/4} = 7.65\times10^{4}\ \mathrm{m}
= 76.5\ \mathrm{km},$$

$$\lambda_c = 2\pi\sqrt{2}\,\alpha = 8.886\times76.5 = \mathbf{680\ km}.$$

(Check against the lesson: $T_e = 25$ km with $\Delta\rho = 600$ gives 566.5 km;
scaling $\alpha \propto (T_e^3/\Delta\rho)^{1/4}$ from that row,
$\alpha = 63.8\times[(30/25)^3(600/500)]^{1/4} = 63.8\times1.199 = 76.5$ km ✓
consistent.)

---

## ★4 — Attraction of a buried corrugation

$k = 2\pi/150\ \mathrm{km} = 4.189\times10^{-5}$ m$^{-1}$,
$kz = 4.189\times10^{-5}\times3.0\times10^{4} = 1.2566$, so $e^{-kz} = 0.2846$.

$$g = 2\pi G\Delta\rho a e^{-kz}
= 2\pi\times6.674\times10^{-11}\times600\times1000\times0.2846
= 7.16\times10^{-5}\ \mathrm{m\,s^{-2}} = \mathbf{7.16\ mGal}.$$

Surface attraction: $2\pi G\rho_c a = 2\pi\times6.674\times10^{-11}\times2700\times1000
= 1.132\times10^{-3}$ m/s² $= \mathbf{113.2\ mGal}$.

The buried interface produces 6.3% of the surface mass's attraction: attenuation
by $e^{-kz}$ is what makes deep compensation hard to detect, and it is why a
short-wavelength load can look uncompensated even when it is fully compensated.

---

## ★5 — The $1/8$ ratio

$$\frac{w(0)}{V_0/(\Delta\rho g\alpha)}
= \frac{V_0\alpha^3}{8D}\cdot\frac{\Delta\rho g\alpha}{V_0}
= \frac{\alpha^4\Delta\rho g}{8D}
= \frac{D}{8D} = \frac{1}{8},$$

using $\alpha^4 \equiv D/(\Delta\rho g)$. The ratio is a constant because the
flexural parameter is defined by exactly that combination; it is a check of the
algebra, not a physical result, and the demonstration's measured 0.1250 in every
row confirms the implementation.

---

## ★6 — Which models are acceptable?

With 1% noise and two adjustable parameters the reduced misfit at a correct model
is of order the noise, so the 2% level (twice the noise) admits $T_e = 25$ km
(1.01%) and excludes $T_e = 20$ km (4.10%). But the *trend* is the point: the
compensation depth demanded by the data falls as $T_e$ rises (34.7 km at
$T_e = 25$ km, 41.0 km at $T_e = 20$ km), so the two parameters are correlated.
Any model with $T_e$ outside the admitted set can be made to fit by moving $t$,
which is why the honest report is the pair (range of $T_e$, range of $t$) and not
the $T_e$ alone.

---

## ★7 — Reduction factors and the resolution limit

Measured reduction factors at $\lambda = 500$ km: 0.9743 for $T_e = 10$ km and
0.2328 for $T_e = 50$ km. The reduction factor is
$1/(1+Dk^4/\Delta\rho g) = 1/(1+(\lambda_c/\lambda)^4/4)$ with
$\lambda_c = 2\pi\sqrt{2}\alpha$: at $\lambda = 500$ km, $\lambda \gg \lambda_c$
for $T_e = 5$ km ($\lambda_c = 169$ km) and for $T_e = 10$ km
($\lambda_c = 285$ km), so in both cases $(\lambda_c/\lambda)^4 \ll 1$ and the
reduction is close to 1: 0.9967 against 0.9743, a difference of 2.3 percentage
points. Distinguishing them requires a measurement of the reduction factor to
better than ~1%, which in gravity terms means resolving a ~1 mGal difference —
marginally possible for a good survey over a large load, and impossible for a
small one. **The general rule:** $T_e$ is well constrained only at wavelengths
comparable with its own $\lambda_c$.

---

## ★8 — Breaking the $(T_e,t)$ trade-off

**Additional observable.** Independent constraints on the *depth distribution* of
the compensation: seismic Moho depths beneath the load (which fix $t$ directly),
or a joint inversion with heat flow and crustal thickness.

**Wavelength band.** The trade-off is strongest where $k t \sim 1$, i.e.
$\lambda \sim 2\pi t \approx 220$ km for $t = 35$ km: that is where $e^{-kt}$
changes most rapidly with $t$ and therefore where an independent $t$ most reduces
the $T_e$ uncertainty. At much longer wavelengths the compensation term is nearly
unity for any $t$ and carries no depth information.

**Precision required.** To reduce the admitted $T_e$ range from 3.5 km to about
1 km, $t$ must be known to roughly $\pm2$ km, which is comparable with the
resolution of receiver-function Moho depths in a favourable setting. This is the
concrete sense in which the ambiguity is broken by *another measurement* rather
than by a better gravity survey.

---

## ★9 — The published statement

> The admittance of the region is fitted by a surface-load model with a
> compensation at the Moho. At the 2% level (twice the 1% noise) the admitted
> elastic thickness is 23.0–26.5 km, with a corresponding compensation depth of
> 32.6–37.3 km; the two are correlated (a thicker plate requires a shallower
> compensation). The best-fitting model is $T_e = 25$ km with $t = 34.7$ km and
> an rms misfit of 1.01%.

**Assumptions that must be stated:** (i) the load is applied at the surface (a
buried load changes $Z(k)$ and shifts the whole ridge); (ii) the compensation is a
single interface at depth $t$, i.e. the crust does not deform internally; (iii)
the plate is continuous, thin and elastic with $E = 70$ GPa and $\nu = 0.25$, and
the density contrasts are fixed at their stated values. Each one is a modelling
choice that trades against $T_e$.

---

## ★10 — A buried load

(The published statement requested in ★9 appears in the previous section.)

**How $Z(k)$ changes.** For a load buried at depth $z_l$ the surface topography
is no longer the load; the observed admittance becomes a ratio of two exponentials
rather than one, with the load's own depth appearing as $e^{-kz_l}$ in the
numerator. The amplitude is reduced at short wavelengths (the load's effect is
attenuated before it reaches the surface) and the phase of the relation changes.

**Why $T_e$ is misinferred.** Fitting a buried-load signal with a surface-load
model forces the flexural term to absorb the extra attenuation, which it does by
changing $T_e$ — and the misfit surface acquires a *different* minimum rather
than a larger one. Because the two models differ in the exponential's argument,
the misfit-versus-$T_e$ curve shifts and broadens: the apparent best-fit $T_e$ is
biased (typically toward larger values, since more attenuation must be explained)
and the admitted range widens. The diagnostic is that the residual misfit is
systematic in wavelength — a sign that the assumed load geometry, not the fitted
$T_e$, is wrong.
