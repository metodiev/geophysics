# Exercises — 08-02-03 Optically Pumped Cesium and Potassium Magnetometers

Attempt these before reading the
[solutions](./03-cesium-optically-pumped-solutions.md). The lesson is
[03 Optically Pumped Cesium and Potassium Magnetometers](../03-cesium-optically-pumped.md).
All instrument coefficients are **SYNTHETIC** teaching values; the physical
constants are standard ones.

Use $g_s = 2.00231930436256$, $\mu_B = 9.2740100783\times10^{-24}\ \mathrm{J\,T^{-1}}$,
$h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$,
$m_e/m_p = 5.446170\times10^{-4}$ and
$f_{\text{hfs}}(\mathrm{Cs}) = 9192631770\ \mathrm{Hz}$.

## ★ Foundational

**★1.** Compute $g_F$ for potassium ($I = 3/2$, $J = 1/2$, $F = 2$) and hence
its sensitivity in $\mathrm{Hz\,nT^{-1}}$.

**★2.** Compute the precession frequency of a caesium sensor at
$B = 45000\ \mathrm{nT}$ and of a potassium sensor at $B = 48000\ \mathrm{nT}$.

**★3.** Show algebraically that the Breit–Rabi radical is a perfect square for
the stretched state $m_F = I + 1/2$, and state what that implies for the
linearity of the sensor.

## ★★ Applied

**★★4.** Using the constant $4.2719\times10^{-8}\ \mathrm{Hz\,nT^{-2}}$, compute
the quadratic Zeeman shift of the $(F=3,m_F=0)\to(F=4,m_F=0)$ transition at
$B = 75000\ \mathrm{nT}$. Then find the field at which the shift reaches 100 Hz.

**★★5.** A sensor has a heading-error coefficient $c = 5.0\times10^{-4}$ and sits
in a $50000\ \mathrm{nT}$ field misaligned by $8^{\circ}$. Compute the error in
nT. Compare it with the cross-axis error of a fluxgate misaligned by $1^{\circ}$
in a field with a $50000\ \mathrm{nT}$ perpendicular component.

**★★6.** The signal amplitude falls as $\sin\theta$ and the noise floor is
$5.0\times10^{-3}$ of the full amplitude. Compute the half-angle of the dead-zone
cone, in degrees.

## ★★★ Research-oriented

**★★★7.** Design an airborne installation of a single-beam scalar sensor for a
survey at 55° magnetic inclination. State the mounting geometry, the attitude
envelope to be flown, the expected heading and dead-zone errors, and the
mitigation for each. A specification that could not be executed is a failed
answer.

**★★★8.** Derive the weak-field limit of the Breit–Rabi formula: expand the
radical to second order in $x$, identify the Landé factor $g_F$ that the
first-order term produces, show that the general Landé formula reduces to it when
$J = 1/2$, and obtain the quadratic coefficient for $m_F = 0$. Compare the
quadratic coefficient you derive with the constant
$4.2719\times10^{-8}\ \mathrm{Hz\,nT^{-2}}$.
