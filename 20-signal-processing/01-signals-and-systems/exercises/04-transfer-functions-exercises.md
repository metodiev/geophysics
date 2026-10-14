# Exercises — 20-01-04 Transfer Functions, Poles and Zeros

Attempt these before reading the
[solutions](./04-transfer-functions-solutions.md). The lesson is
[04 Transfer Functions](../04-transfer-functions.md). **All models and data in
this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** For $b = [1, 0.5]$ and $a = [1, -1.1, 0.3]$, write the difference
equation, $H(z)$, and the zero(s) and pole(s) with their radii and angles. State
whether the causal system is stable and give the DC gain.

**★2.** A causal IIR filter has poles at $0.9\angle\pm25^{\circ}$. From the poles
alone, give the decay time constant in samples, the number of samples for a
$60\ \mathrm{dB}$ decay, and the oscillation frequency in Hz at
$f_s = 200\ \mathrm{Hz}$.

**★3.** For the second-order system with $\omega_0 = 2\pi\cdot10\ \mathrm{rad/s}$
and $\zeta = 0.05$, give the resonant frequency in Hz, the peak magnitude, and
the value the shortcut $1/(2\zeta)$ would predict.

## ★★ Applied

**★★4.** An all-pole second-order resonator is to ring at $25\ \mathrm{Hz}$ with
a time constant of $0.2\ \mathrm{s}$ at $f_s = 500\ \mathrm{Hz}$. Give the pole
radius and angle, the coefficients $a_1, a_2$ of
$A(z) = 1 + a_1z^{-1} + a_2z^{-2}$, and the group delay at the resonant
frequency. State which of your numbers is exact and which is an approximation.

**★★5.** Derive the bilinear coefficients for $H(s) = \omega_c/(s+\omega_c)$ with
$f_c = 10\ \mathrm{Hz}$ designed at $f_s = 100\ \mathrm{Hz}$ **with the corner
frequency pre-warped** so that the $-3\ \mathrm{dB}$ point lands exactly on
$10\ \mathrm{Hz}$. Then compute the actual $-3\ \mathrm{dB}$ frequency of the
unwarped design.

**★★6.** Show that the maximum of $\lvert H(i\omega)\rvert$ for the second-order
system occurs at $\omega_r = \omega_0\sqrt{1-2\zeta^{2}}$ by differentiating
$\lvert H\rvert^{2}$ with respect to $\omega^{2}$, and evaluate the peak height
for $\zeta = 0.1$. Then state the largest $\zeta$ for which a peak exists and
what the response looks like at that value.

## ★★★ Research-oriented

**★★★7.** A synthetic instrument response is supplied as two printed pole–zero
tables: one with a pole at $z = 0.98$ and a zero at $z = 0.975$, and one with a
pole at $z = 0.98$ and a zero at $z = 0.9995$. Explain the difference in their
low-frequency gain, estimate the low-frequency group delay of each from the boxed
formula in the lesson, and state which table you would trust if the two were
supposed to describe the same sensor. Say what measurement would settle it.

**★★★8.** Design a notch for a $50\ \mathrm{Hz}$ interference at
$f_s = 500\ \mathrm{Hz}$ that must attenuate by at least $40\ \mathrm{dB}$ over
the band $49.5$–$50.5\ \mathrm{Hz}$ but must not move the passband gain by more
than $0.5\ \mathrm{dB}$ below $40\ \mathrm{Hz}$. Give the filter, the numbers
that demonstrate both requirements, and state which requirement is harder to meet
and why. (A two-zero, two-pole notch is enough; say how you placed the poles.)
