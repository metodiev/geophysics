# Exercises — 13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength

Attempt these before reading the
[solutions](./01-isostasy-flexure-modelling-solutions.md). The lesson is
[01 Isostasy and Flexure](../01-isostasy-flexure-modelling.md) and its numbers
come from
[`code/isostasy_flexure_modelling_demo.py`](../code/isostasy_flexure_modelling_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Derive the Airy root formula $r = [\rho_c/(\rho_m-\rho_c)]h$ and compute
$r$ for $h = 3$ km with $\rho_c = 2800$ and $\rho_m = 3350$ kg/m³.

**★2.** Compute the flexural rigidity $D = ET_e^3/[12(1-\nu^2)]$ for
$E = 70$ GPa, $\nu = 0.25$ and $T_e = 30$ km, and state the units.

**★3.** Compute the flexural parameter $\alpha = (D/\Delta\rho g)^{1/4}$ for that
$D$ and $\Delta\rho = 500$ kg/m³, and state the compensation wavelength
$\lambda_c = 2\pi\sqrt{2}\,\alpha$ in kilometres.

## ★★ Applied

**★★4.** For a periodic load of wavelength 150 km at depth, compute the
attraction $2\pi G\Delta\rho a e^{-kz}$ for $\Delta\rho = 600$ kg/m³,
$a = 1$ km and $z = 30$ km, in mGal, and compare with the surface attraction
$2\pi G\rho_c a$ for $\rho_c = 2700$ kg/m³.

**★★5.** Show that the ratio of the line-load deflection
$w(0) = V_0\alpha^3/(8D)$ to $V_0/(\Delta\rho g\alpha)$ is exactly $1/8$.

**★★6.** A synthetic admittance measurement is fitted by $T_e = 25$ km with a
compensation depth of 34.7 km and an rms misfit of 1.01%, and by $T_e = 20$ km
with 41.0 km and 4.10%. The noise is 1%. Which models are acceptable and why,
and what does the pair of them say about the depth?

**★★7.** Using the lesson's reduction factors, compute the fraction of the Airy
deflection achieved at $\lambda = 500$ km for $T_e = 10$ and 50 km, and explain
why the same measurement cannot distinguish $T_e = 10$ km from $T_e = 5$ km.

## ★★★ Research-oriented

**★★★8.** Design an admittance study that could break the $(T_e, t)$ trade-off.
State the additional observable, the wavelength band it constrains, and the
precision required.

**★★★9.** The admissible set at the 2% level is $T_e \in [23.0, 26.5]$ km with
$t \in [32.6, 37.3]$ km. Write the two-sentence result you would publish, and
name three assumptions that must be stated with it.

**★★★10.** A load is buried at 10 km depth rather than at the surface. Explain
qualitatively how the admittance $Z(k)$ changes, why the same $T_e$ would then be
inferred incorrectly, and how the error would appear in a misfit-versus-$T_e$
curve.
