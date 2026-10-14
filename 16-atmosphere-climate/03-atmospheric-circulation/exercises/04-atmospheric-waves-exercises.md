# Exercises — 16-03-04 Atmospheric Waves: Rossby, Kelvin, Gravity Waves

Attempt these before reading the
[solutions](./04-atmospheric-waves-solutions.md). The lesson is
[04 Atmospheric Waves](../04-atmospheric-waves.md). All models are
**SYNTHETIC** teaching values. Use $\Omega = 7.292115\times10^{-5}\
\mathrm{rad\,s^{-1}}$, $a = 6.371\times10^6$ m, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$2\Omega/a = 2.2892\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$.

## ★ Foundational

**★1.** Compute $\beta = 2\Omega\cos\phi/a$ at $30^\circ$ and $60^\circ$. For a
barotropic Rossby wave with $\lambda_x = 4000$ km and $l = 0$, compute the
frequency, the period in days and the phase speed at each latitude, and state
which latitude gives the shorter period.

**★2.** For an equivalent depth $H = 200$ m compute the Kelvin-wave speed $c$,
the trapping scale $\sqrt{c/\beta}$ (equatorial $\beta$) and the period of the
$k = 1/a$ Kelvin wave. State the unit of the trapping scale.

**★3.** An internal gravity wave has $N = 10^{-2}\ \mathrm{s^{-1}}$ and a
wavevector at $45^\circ$ to the vertical. Compute $\omega$ and the period, and
state whether the mode exists.

## ★★ Applied

**★★4.** Starting from $\omega^3 - \omega(c^2k^2+\beta c(2n+1)) - \beta c^2k = 0$
with $n = 0$, show that $\omega = -ck$ is always a root, and give the other two
roots in closed form. Evaluate all three for $c = 62.64$ m s⁻¹,
$\beta = 2.2892\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$ and
$k = 1.5696\times10^{-7}$ m⁻¹.

**★★5.** Derive $\mathbf{c}_g\cdot\mathbf{k} = 0$ for internal gravity waves
from $\omega = N k_h/\sqrt{k_h^2+m^2}$ by explicit differentiation, and verify
it numerically for $\lambda_h = 200$ km, $\lambda_z = 800$ km,
$N = 10^{-2}$ s⁻¹.

**★★6.** The demonstration measures the Rossby frequency at
$\Delta x = 500, 250, 125$ km and finds errors against the continuum
dispersion relation of $3.22\times10^{-3}$, $8.03\times10^{-4}$ and
$2.01\times10^{-4}$.
**(a)** Compute the ratio between successive errors and state the order of the
scheme.
**(b)** Predict the error at $\Delta x = 62.5$ km.
**(c)** State one thing this check does *not* verify.

## ★★★ Research-oriented

**★★★7.** A simulated equatorial Kelvin wave decays as it propagates across a
basin. Design a sequence of experiments that separates a numerical cause from a
physical one; state the diagnostic you would plot against what abscissa, and the
outcome that would indicate each cause. Include at least one experiment that
tests the boundary treatment explicitly.
