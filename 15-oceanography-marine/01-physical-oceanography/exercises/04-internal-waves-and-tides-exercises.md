# Exercises — 15-01-04 Internal Waves, Tides and Mixing

Attempt these before reading the
[solutions](./04-internal-waves-and-tides-solutions.md). The lesson is
[04 Internal Waves, Tides and Mixing](../04-internal-waves-and-tides.md). All
models are **SYNTHETIC** teaching values.

Constants: $\Omega = 7.292115\times10^{-5}\ \mathrm{s^{-1}}$,
M2 period $= 12.4206\ \mathrm{h}$ (a conventional astronomical value),
$\Gamma = 0.20$ where needed.

## ★ Foundational

**★1.** Compute the internal-wave frequency $\omega$ for
$k = m = 2.0\times10^{-3}\ \mathrm{m^{-1}}$ with
$N = 0.012\ \mathrm{rad\,s^{-1}}$ and $f = 1.0\times10^{-4}\ \mathrm{s^{-1}}$.
Give the period in seconds and minutes, and explain why the answer is
independent of the *magnitude* of $k$ and $m$ when $k = m$.

**★2.** State the frequency band in which internal waves exist, and compute both
ends for $N = 0.008\ \mathrm{rad\,s^{-1}}$ at $20^\circ$N.

**★3.** Show dimensionally that the characteristic slope
$s = \sqrt{(\omega^{2}-f^{2})/(N^{2}-\omega^{2})}$ is dimensionless.

## ★★ Applied

**★★4.** Derive $k^{2} = m^{2}(\omega^{2}-f^{2})/(N^{2}-\omega^{2})$ from the
dispersion relation. Evaluate it for the mode-1 internal tide of the lesson
($N = 0.010\ \mathrm{rad\,s^{-1}}$, $H = 1000$ m, $f$ at $45^\circ$N) and report
$k$, $\lambda$ and $c$ with units. Compare $c$ with $NH/\pi$ and state the
factor and its origin.

**★★5.** A tidal beam is generated at $30^\circ$N over topography with slope
$8.0\times10^{-3}$. Using $N = 0.012\ \mathrm{rad\,s^{-1}}$ and the M2 frequency
($1.4052\times10^{-4}\ \mathrm{rad\,s^{-1}}$), compute the characteristic slope,
the criticality $\gamma$, and classify the regime. Would the same topography be
more or less critical at $15^\circ$N? Justify with a computed number.

**★★6.** A microstructure profile gives $\epsilon = 5.0\times10^{-9}\
\mathrm{W\,kg^{-1}}$ in a layer with $N = 0.008\ \mathrm{rad\,s^{-1}}$. (a)
Compute $K_\rho$ with $\Gamma = 0.20$ and with $\Gamma = 0.50$. (b) Compute
$K_\rho$ with $\Gamma = 0.20$ but $N = 0.016\ \mathrm{rad\,s^{-1}}$. (c) State
which of the two changes moves the answer more, and by what factor.

**★★7.** For the lesson's shear profile, $N(z) = 0.010 + 0.006\tanh((z-100)/20)$
and $U(z) = 0.60\tanh((z-100)/25)$, compute $\mathrm{Ri}$ at $z = 95$ m by hand
from $\mathrm{d}U/\mathrm{d}z \approx [U(105)-U(85)]/20$ and
$N \approx N(95)$. Compare with the demonstration's table and state the sign of
the discrepancy.

## ★★★ Research-oriented

**★★★8.** Design a microstructure survey that would determine $K_\rho$ in a
$200\ \mathrm{m}$ water column to within a factor 2. State the instrument, the
sampling in space and time, the quantity you would average, the error budget, and
which single assumption dominates the budget. A specification that could not be
executed is a failed answer.

**★★★9.** The tidal latitude cut-off for the M2 frequency is at
$\phi = 74.5^\circ$. Show this, then state two reasons why an observed absence of
an M2 internal tide at $76^\circ$ latitude would *not* be strong evidence for the
cut-off.
