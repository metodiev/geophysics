# Solutions — 04-01-02 Lithosphere, Asthenosphere and the Rheological Definition

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — Maxwell relaxation and the Deborah number

**(a)** $\tau_M = 1.0\times10^{20}/6.5\times10^{10} = 1.538\times10^{9}$ s.
Dividing by the Julian year, $1.538\times10^9/3.15576\times10^7 = 48.8$ a.

**(b)** For $T = 1$ s, $De = 1.538\times10^{9}$. For $T = 1$ Ma
$= 3.156\times10^{13}$ s, $De = 4.88\times10^{-5}$.

**(c)** $De \gg 1$ means elastic; $De \ll 1$ means viscous. So a seismic wave
sees an elastic solid and a million-year plate motion sees a fluid, in the same
rock with the same two constants.

---

## ★2 — Airy isostasy

**(a)** $r/h = 2750/(3300-2750) = 2750/550 = 5.00$.

**(b)** $r = 5.00 \times 3 = 15.0$ km.

**(c)** $35 + 3 + 15 = 53$ km.

**(d)** A larger mantle density means a larger $\rho_m - \rho_c$ and therefore a
*smaller* root ratio, so less compensation is needed to support the same
topography.

---

## ★3 — Flexure

**(a)** $D = 70\times10^9 \times (2.0\times10^4)^3/[12(1-0.0625)]
= 70\times10^9 \times 8\times10^{12}/(11.25) = 4.98\times10^{22}$ N·m.

**(b)** $\alpha = (4.98\times10^{22}/(3300\times9.81))^{1/4}
= (1.538\times10^{18})^{1/4} = 3.52\times10^4$ m $= 35.2$ km.

**(c)** Loads wider than a few times $\alpha$ — say above about 70 km at this
$T_e$ — are flexurally supported; narrower loads are buoyancy-supported and Airy
isostasy applies. The demo quotes the threshold as $2\alpha = 70$ km.

---

## ★★4 — Post-glacial rebound

**(a)** $k = 2\pi/2.5\times10^6 = 2.513\times10^{-6}$ m⁻¹, so
$\tau = 2\times10^{21}\times2.513\times10^{-6}/(3300\times9.81)
= 5.026\times10^{15}/32373 = 1.552\times10^{11}$ s $= 4920$ a.

**(b)** Inverting for $\eta$ at an observed $\tau = 5000$ a:
$$\eta = \frac{\tau\,\rho g}{2k} = \frac{5000\times3.15576\times10^7\times32373}
{2\times2.513\times10^{-6}} = 1.016\times10^{21}\ \text{Pa·s}.$$
So an observed 5000 a rebound at a 2500 km wavelength implies
$\eta \approx 1.0\times10^{21}$ Pa·s.

**(c)** At 5000 km, $k$ halves, so the same observed $\tau$ requires *twice* the
viscosity: $\eta \approx 2.0\times10^{21}$ Pa·s. The physical reason is that a
longer-wavelength load samples a thicker column of mantle, and the deeper
material is more viscous, so a wider load relaxes more slowly for the same
viscosity.

---

## ★★5 — Temperature and viscosity

**(a)** $E_a/R = 300000/8.314 = 3.608\times10^4$ K. Then
$$\frac{\eta(1600)}{\eta(1700)} = \exp\left[\frac{E_a}{R}\left(\frac1{1600}-\frac1{1700}\right)\right]
= \exp(1.326) = 3.77 .$$
A 100 K rise cuts the viscosity by a factor of 3.8. This is the number quoted in
the demo's table as `eta/eta0` = 1 at 1600 K and 3.77 at 1700 K.

**(b)** $\exp[3.608\times10^4(1/1500 - 1/1700)] = \exp(2.829) = 16.9$. A 200 K
rise cuts it by a factor of 17.

**(c)** Setting $\eta(1600)/\eta(T) = 10$ gives
$$\frac1T = \frac1{1600} - \frac{\ln 10 \times R}{E_a}
= 6.25\times10^{-4} - 6.381\times10^{-5} = 5.612\times10^{-4},$$
so $T = 1782$ K, a rise of 182 K.

**(d)** A 200 K rise at 1600 K gives
$\exp[3.608\times10^4(1/1600-1/1800)] = \exp(2.506) = 12.2$, and the 182 K rise
of (c) gives exactly 10. So a temperature change of two to three hundred kelvin
is enough to produce the order-of-magnitude viscosity contrast that a
lithosphere–asthenosphere boundary requires — and it produces it by an
*exponential*, which is why the boundary is sharp in rheology while being
gradual in temperature.

---

## ★★6 — The seismic signature

**(a)** $\Delta v_s = -0.5 \times 182 = -91$ m/s.

**(b)** $-91/4500 = -2.0$ per cent.

**(c)** The viscosity changes by a factor of 10 while the velocity changes by
2 per cent. The two columns move on different scales because viscosity is
*exponential* in temperature while velocity is roughly *linear*: a factor in the
exponent becomes a percentage in the prefactor. That asymmetry is why the
asthenosphere is easy to detect rheologically and hard to detect seismically.

---

## ★★★7 — Inverting the demo's rebound table

**(a)** From the demo's output: $\lambda = 1000$ km gives
$\eta = 3.66\times10^{20}$; 3000 km gives $1.10\times10^{21}$; 6000 km gives
$2.20\times10^{21}$ Pa·s.

**(b)** $\log_{10}\eta$ against $\log_{10}\lambda$:
$(3, 20.563)$, $(3.477, 21.041)$, $(3.778, 21.342)$. The slope from the first to
the last is $(21.342-20.563)/(3.778-3) = 0.779/0.778 = 1.00$, so
$m = 1$: the implied viscosity is **directly proportional** to the wavelength.

**(c)** From $\tau = 2\eta k/(\rho g)$ with $k = 2\pi/\lambda$,
$\eta = \tau\rho g\lambda/(4\pi)$. With $\tau$ fixed at the observed value, $\eta$
is exactly proportional to $\lambda$. So the exponent $m = 1$ is a consequence of
the model and of holding the observed relaxation time fixed, not an empirical
finding.

**(d)** Three wavelengths give three points and a slope; five would give five
points and a *goodness of fit*, so the question of whether the model's
$\eta \propto \lambda$ is adequate could be answered rather than assumed. Real
rebound datasets do not fall on a line, and the departure from it is the
information about a layered viscosity structure.

---

## ★★★8 — The demo's output

**(a)** `asthenosphere, eta = 1e+19 Pa s -> tau_M = 1.429e+08 s = 5 a`;
`mantle, eta = 1e+21 Pa s -> tau_M = 1.429e+10 s = 453 a`. Deborah numbers:
seismic P wave `1.429e+10`, plate motion `4.527e-04`.

**(b)** $1.429\times10^{10}$ to $4.527\times10^{-6}$ is a span of about
$3.2\times10^{15}$, i.e. fifteen orders of magnitude.

**(c)** At $T_e = 60$ km: `D = 1.344e+24 N m`, `alpha = 80.3 km`.

**(d)** For $h = 4$ km: root `22.40 km`, Moho depth `61.4 km`.

**(e)** `eta/eta0` is 0.00549 at 1300 K and 35.2 at 1900 K; the ratio is
$35.2/0.00549 = 6.4\times10^3$, i.e. 3.8 orders of magnitude.

**(f)** `dVs/Vs` is +3.33 per cent at 1300 K (relative to 1600 K) and −3.33 per
cent at 1900 K.

**(g)** A factor of $6.4\times10^3$ in viscosity corresponds to a change of a few
per cent in velocity. The ratio of the two sensitivities is therefore of order
$10^3$: a measurement that resolves the seismic anomaly to a fraction of a per
cent would still leave the viscosity uncertain by more than an order of
magnitude. Mapping the asthenosphere from seismic velocities alone is therefore
ill-conditioned, which is why the boundary's depth is quoted as a range and why
independent constraints — conductivity, anisotropy, and the rebound viscosity
profile — are needed to locate it.

---

## ★★★9 — Critiquing the Maxwell model

Three respects in which the real mantle differs, and what each mis-predicts.

1. **The mantle has a spectrum of relaxation times, not one.** A single
   relaxation time predicts that all loads relax with the same time constant
   scaled by their wavelength, and a real rebound dataset does not follow the
   line of ★7(b). The mis-predicted observation is the wavelength dependence of
   post-glacial rebound, which requires a layered or a transient (Burgers,
   Andrade) rheology.
2. **The mantle is non-Newtonian.** Dislocation creep gives a strain rate
   proportional to about the third power of stress, so the *effective* viscosity
   depends on the stress. A Maxwell model with a fixed $\eta$ mis-predicts the
   deformation around a subducting slab, where stresses are high, and predicts a
   mantle that is too stiff there.
3. **Viscosity is not a material constant at all.** It depends on temperature,
   pressure, grain size, water content and melt fraction. A Maxwell model with a
   single $\eta$ mis-predicts the response of anything that changes one of those
   — the postseismic relaxation of a fault after a large earthquake, for
   example, which shows a transient viscosity lower than the steady-state value.
