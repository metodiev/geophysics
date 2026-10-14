# Solutions — 13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson:
[03 Lithospheric Strength](../03-lithospheric-strength.md). Constants used:
$E = 70\ \mathrm{GPa}$, $\nu = 0.25$,
$\Delta\rho = 2300\ \mathrm{kg\,m^{-3}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$.

---

## ★1 — Rigidity and flexural parameter for $T_e = 15$ km

$$D = \frac{E T_e^{3}}{12(1-\nu^{2})}
= \frac{(7\times10^{10})(1.5\times10^{4})^{3}}{12(0.9375)}
= \frac{2.3625\times10^{23}}{11.25}
= 2.100\times10^{22}\ \mathrm{N\,m},$$

$$\alpha = \left(\frac{D}{\Delta\rho g}\right)^{1/4}
= \left(\frac{2.100\times10^{22}}{2.2563\times10^{4}}\right)^{1/4}
= \left(9.307\times10^{17}\right)^{1/4} = 3.106\times10^{4}\ \mathrm{m}
= 31.06\ \mathrm{km}.$$

---

## ★2 — Deflection for $T_e = 20$ km

$$D = \frac{(7\times10^{10})(2\times10^{4})^{3}}{11.25}
= \frac{5.6\times10^{23}}{11.25} = 4.9778\times10^{22}\ \mathrm{N\,m},$$

$$\alpha = \left(\frac{4.9778\times10^{22}}{2.2563\times10^{4}}\right)^{1/4}
= 3.854\times10^{4}\ \mathrm{m} = 38.54\ \mathrm{km}.$$

$$w_{\text{cont}}(0) = \frac{V_0\alpha^{3}}{2D}
= \frac{(2\times10^{12})(5.724\times10^{13})}{9.9556\times10^{22}}
= 1150.0\ \mathrm{m},$$

$$w_{\text{broken}}(0) = \frac{V_0\alpha^{3}}{D} = 2300.0\ \mathrm{m}.$$

A broken plate deflects exactly twice as much at the load, because there is no
bending-moment continuity to share the load.

---

## ★3 — Units of $\alpha$

$$\left[\frac{D}{\Delta\rho g}\right]
= \frac{\mathrm{N\,m}}{\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}}}
= \frac{\mathrm{kg\,m\,s^{-2}}\,\mathrm{m}}{\mathrm{kg\,m^{-2}\,s^{-2}}}
= \mathrm{m^{4}},$$

so the fourth root is a length. ✔ (Equivalently, $\Delta\rho g$ is a pressure
gradient, $\mathrm{N\,m^{-3}}$, and $\mathrm{N\,m}/\mathrm{N\,m^{-3}} =
\mathrm{m^{4}}$.)

---

## ★★4 — The isostatic-area identity

Write the line-load solution as
$w(x) = \frac{V_0\alpha^{3}}{2D}e^{-|x|/\alpha}
\left[\cos(|x|/\alpha) + \sin(|x|/\alpha)\right]$ and substitute $r = |x|/\alpha$,
$\mathrm{d}x = \alpha\,\mathrm{d}r$. Both halves of the profile contribute
equally:

$$\int_{-\infty}^{\infty}w\,\mathrm{d}x
= 2\cdot\frac{V_0\alpha^{3}}{2D}\cdot\alpha\int_0^{\infty}e^{-r}(\cos r +
\sin r)\,\mathrm{d}r .$$

The elementary integral is

$$\int_0^{\infty}e^{-r}\cos r\,\mathrm{d}r = \frac{1}{2},
\qquad
\int_0^{\infty}e^{-r}\sin r\,\mathrm{d}r = \frac{1}{2},
\qquad
\text{sum} = 1 .$$

Hence

$$\int_{-\infty}^{\infty}w\,\mathrm{d}x = \frac{V_0\alpha^{4}}{D}
= \frac{V_0}{\Delta\rho g}
\qquad\text{because } \alpha^{4} = \frac{D}{\Delta\rho g} . \qquad\checkmark$$

**Physical statement:** the plate redistributes where the displaced mass sits but
does not change how much there is — the *area* of the deflection equals the load
divided by the substrate's buoyancy gradient, which is local (Airy) isostasy.
Flexure is a redistribution, not a violation.

---

## ★★5 — Inverting a deflection for $T_e$

From $w(0) = V_0\alpha^{3}/(2D)$ and $\alpha^{4} = D/(\Delta\rho g)$:

$$\frac{w(0)}{V_0} = \frac{\alpha^{3}}{2D}
= \frac{\alpha^{3}}{2\Delta\rho g\,\alpha^{4}} = \frac{1}{2\Delta\rho g\,\alpha}
\;\;\Longrightarrow\;\;
\alpha = \frac{V_0}{2\Delta\rho g\,w(0)} .$$

$$a = \frac{3\times10^{12}}{2(2300)(9.81)(1500)}
= \frac{3\times10^{12}}{6.7689\times10^{7}} = 4.432\times10^{4}\ \mathrm{m}
= 44.32\ \mathrm{km}.$$

$$D = \Delta\rho g\,\alpha^{4}
= (2.2563\times10^{4})(4.432\times10^{4})^{4}
= 8.706\times10^{22}\ \mathrm{N\,m},$$

$$T_e = \left[\frac{12(1-\nu^{2})D}{E}\right]^{1/3}
= \left[\frac{11.25\times8.706\times10^{22}}{7\times10^{10}}\right]^{1/3}
= \left(1.399\times10^{13}\right)^{1/3}
= 2.410\times10^{4}\ \mathrm{m} = 24.1\ \mathrm{km}.$$

Check: $V_0\alpha^{3}/(2D) = (3\times10^{12})(8.706\times10^{13})/
(1.7412\times10^{23}) = 1500.0$ m ✔.

**Which data dominate the error?** $\alpha\propto V_0/w(0)$ and
$T_e\propto D^{1/3}\propto\alpha^{4/3}\propto(V_0/w(0))^{4/3}$. So a fractional
error in the *load* propagates amplified by $4/3$ into $T_e$, and in practice the
load magnitude is far less certain than the deflection, which is measured to a few
per cent. The inversion is therefore load-limited, not data-limited — a point
that generalises to every flexure study.

---

## ★★6 — Narrow or wide?

With $\alpha = 38.54$ km from ★2 and $a = 30$ km:

$$\frac{a}{\alpha} = \frac{30}{38.54} = 0.778 .$$

Interpolating the lesson's measured table (which uses $\alpha = 45.56$ km):
$a/\alpha = 0.55$ gives 0.51 and $a/\alpha = 1.10$ gives 0.86, so at
$a/\alpha = 0.78$,

$$\frac{w(0)}{w_{\text{Airy}}} \approx 0.51 + \frac{0.78-0.55}{1.10-0.55}(0.86-0.51)
\approx 0.51 + 0.146 = 0.66 .$$

**Answer:** the load is *intermediate* — neither comfortably narrow nor
comfortably wide. The plate holds up about two-thirds of the "missing" buoyancy
and the remaining third is compensated locally. This is the case where assuming
Airy compensation is wrong by 34% and assuming pure flexure is wrong by 66%: the
transition band is where the modelling choice matters most, and it is set by
$a/\alpha$ near 1.

---

## ★★★7 — Curvature dependence of $T_e$

From the measured triple (83.8 km at $10^{-8}$, 49.5 km at $10^{-7}$, 24.4 km at
$10^{-6}$ m$^{-1}$):

$$p = \frac{\ln(83.8/24.4)}{\ln(10^{2})} = \frac{1.234}{4.605} = 0.268
\;\;\Longrightarrow\;\;
T_e \propto \kappa^{-0.27} .$$

For a perfectly plastic envelope, in which the whole plate is at the yield stress
except a thin neutral fibre, the bending moment is
$M \approx \sigma_y h^{2}/4$ — *independent of curvature* — so
$T_e\propto M^{1/3}\kappa^{-1/3}$... and once $M$ saturates the correct statement
is that $T_e\propto\kappa^{-1/3}$, with the exact limiting exponent depending on
how the neutral axis migrates; the idealised "two rigid blocks separated by a
hinge" limit gives $-1/2$.

**Why the measured exponent is smaller in magnitude (0.27 rather than 0.33–0.5):**
the envelope is not perfectly plastic. At the curvatures tested a substantial
part of the plate is still elastic, so $M$ continues to grow with $\kappa$ rather
than saturating, and $T_e$ falls more slowly. The exponent is therefore itself a
function of the curvature range over which it is measured — a clean example of a
"scaling exponent" that is not a material constant.

---

## ★★★8 — Inverting for $T_e$ with an unknown load density

**Parameterisation.** $T_e$ (1 km steps from 5 to 80 km) and the load density
$\rho_{\text{load}}$ (2400–3000 kg m$^{-3}$), with $\rho_m$ fixed by the seismic
model and $\Delta\rho = \rho_m - \rho_{\text{infill}}$.

**Data.** Deflection profile $w(x_i)$ from a mapped top of the load (bathymetry or
seismic horizon), with an uncertainty per point, plus the load's *geometry* if it
is resolvable.

**Forward model.** $w(x) = \int G(x-x';T_e)\,\rho_{\text{load}}g\,h(x')\,
\mathrm{d}x'$ with $G$ the line-load Green's function of
[13-01-03 §2.3](../03-lithospheric-strength.md), convolved numerically.

**Misfit.** Weighted least squares; regularise only by bounding the parameters,
not by smoothing, since the model has two parameters and they are physically
interpretable.

**Diagnostic for the trade-off.** The misfit surface $\chi^{2}(T_e,
\rho_{\text{load}})$: a long valley running diagonally means the two parameters
trade off. Also compute the correlation coefficient of the two parameters from
the linearised Jacobian, and the admitted range at 1.5× the minimum misfit along
the valley.

**What success looks like.** A two-dimensional admitted region — not a single
number — in which $T_e$ is constrained to a factor of about 1.5 and the load
density only to the range where the valley runs. If the valley is unbounded
within the prior box, the honest report is that the deflection alone cannot
separate the two, and an independent density constraint (from gravity, seismic
velocities or drilling) is required.

---

## ★★★9 — Explaining a flexure/envelope discrepancy

The reported pair is $T_e = 30 \pm 2$ km (flexure) versus $T_e = 50$ km
(envelope). Three physically distinct explanations, each with a test:

1. **The geotherm is wrong.** The envelope's $T_e$ is controlled by the
   brittle–ductile transition depth, which moves with heat flow
   (measured: 21.6 km at 10 K/km versus 11.8 km at 20 K/km in the crust).
   *Test:* an independent heat-flow or Curie-depth estimate, or seismically
   determined lithospheric thickness.
2. **The load model is wrong.** If the load is denser or thicker than assumed, the
   flexure inversion returns a larger $T_e$; if the load has a buried part (a
   subaerial volcano with a large Edifice-to-root ratio), the inversion is biased
   low. *Test:* gravity modelling of the load's total mass, or a seismic
   cross-section of the load.
3. **The curvature used in the envelope is wrong.** The envelope $T_e$ falls with
   curvature (measured: 83.8 km at $\kappa = 10^{-8}$ versus 24.4 km at
   $10^{-6}\ \mathrm{m^{-1}}$), so a mismatch in the loading amplitude alone can
   produce a factor-of-two difference. *Test:* measure the curvature from the
   deflection profile itself, then recompute both estimates at that curvature.

A fourth, and often decisive, explanation is that the two estimates measure
different things: flexure measures the strength *integrated over the loading
period*, while the envelope measures the instantaneous strength of the *present*
temperature field. A plate that was hotter in the past, or that carries inherited
weak zones, will show them differently.
