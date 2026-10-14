# Exercises — 12-06-03 Nutation and Constraints on Core Properties

Attempt these before reading the
[solutions](./03-nutation-constraints-solutions.md). The lesson is
[03 Nutation and Constraints on Core Properties](../03-nutation-constraints.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A synthetic body has dynamical ellipticity $H = 1/400$ and spins once per
sidereal day. Compute the inertial and body-frame periods of its free wobble, and
state which one a station fixed to the body would see.

**★2.** Compute the free-core-nutation period in sidereal days for
$A_{m} = 0.99$, $C_{m} = 1.00$, $C_{c} = 0.10$ and $e_{c} = 1/500$, using

$$
T_{\text{FCN}} = \frac{A_{m}A_{c}}{e_{c}C_{c}(A_{m}+A_{c})}\ \text{sidereal days},
\qquad A_{c} = C_{c}(1-e_{c}).
$$

**★3.** In the two-mode picture of the lesson, one mode is a whole-body Euler
mode and one is the free core nutation. State which is the slow (long-period)
mode and explain, in two sentences, why an oblate core is required for either to
exist at all.

## ★★ Applied

**★★4.** An observation gives $T_{\text{FCN}} = 400$ sidereal days with a 2%
error, with the inertia ratios held fixed. Compute the recovered $e_{c}$ and the
admitted range of $e_{c}$ and of $1/e_{c}$.

**★★5.** Using the classical precession rate
$\dot\psi = \tfrac32(n^{2}/\Omega)H\cos\varepsilon$, compute the precession rate
in rad/s and the nodal period in years for $H = 1/400$, a two-year circular orbit
and $\varepsilon = 45^{\circ}$. State how the period changes if the obliquity is
$60^{\circ}$.

**★★6.** In the chain "period $\to$ core oblateness $\to$ core mass $\to$ core
mean density", take the measured period to have a 2% error and the assumed core
radius to have a 5% error. Compute the fractional errors in $e_{c}$, $M_{c}$ and
the mean density, and state which error dominates.

## ★★★ Research-oriented

**★★★7.** A single nutation period leaves a one-parameter family of
$(e_{c}, C_{c}/C_{m})$ cores. Specify a second observable that would break that
degeneracy, say what precision it needs (use the scaling measured in the
lesson's §4 as your guide), and state the assumption that would remain
afterwards.

**★★★8.** Derive the reduced-inertia result

$$
A_{\text{red}}\frac{\partial\theta}{\partial t} = -i\Omega K\theta,
\qquad
A_{\text{red}} = \frac{A_{m}A_{c}}{A_{m}+A_{c}},
\qquad K = C_{c}-A_{c},
$$

starting from the two angular-momentum equations for the tilts $m_{m}$ and $m_{c}$
of a rigid mantle and a rigidly rotating fluid core coupled by a torque
proportional to the relative tilt. Show each algebraic step, and verify that the
result reduces correctly when the core is spherical.
