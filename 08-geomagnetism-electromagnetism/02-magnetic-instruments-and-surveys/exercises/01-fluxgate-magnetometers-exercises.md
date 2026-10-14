# Exercises — 08-02-01 Fluxgate Magnetometers: Principle and Use

Attempt these before reading the
[solutions](./01-fluxgate-magnetometers-solutions.md). The lesson is
[01 Fluxgate Magnetometers](../01-fluxgate-magnetometers.md). All instrument
parameters are **SYNTHETIC** teaching values.

Use $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

## ★ Foundational

**★1.** A sense coil has $N = 200$ turns and $A = 2.0\times10^{-5}\
\mathrm{m^2}$. The flux density through it changes at
$|\mathrm{d}B/\mathrm{d}t| = 3.9473\times10^{4}\ \mathrm{T\,s^{-1}}$. Compute
$|e|_{\max}$ and state the unit chain.

**★2.** Compute $\mu_0H_k$ in nT for a core with $H_k = 20\
\mathrm{A\,m^{-1}}$, and say in one sentence what it represents physically.

**★3.** A sensor has a sensitivity of $75.4807\ \mu\mathrm{V\,nT^{-1}}$. Express
it in nT per volt.

## ★★ Applied

**★★4.** The synthetic response has slope
$9.4852\times10^{-2}\ \mathrm{V\,(A\,m^{-1})^{-1}}$. Convert it to
$\mu\mathrm{V\,nT^{-1}}$ and verify the value quoted in the lesson.

**★★5.** A sense coil is misaligned by $\alpha = 0.3^{\circ}$ and the
perpendicular component is $48000\ \mathrm{nT}$. Compute the leak into the
reading. Repeat for $\alpha = 0.05^{\circ}$ and state the mechanical requirement
for a 1 nT component survey.

**★★6.** The synthetic electronics noise is $3.162\times10^{-4}\
\mathrm{V/\sqrt{Hz}}$ over a 10 Hz bandwidth. Compute the field noise per reading,
the field noise if the bandwidth is narrowed to 0.1 Hz, and the number of
independent readings needed to reach 0.5 nT.

## ★★★ Research-oriented

**★★★7.** Design a calibration experiment that determines the three sense-axis
misalignments and the three sensitivities of a three-axis fluxgate, using only
rotations in a field you can assume constant. State the measurements, the
algebra, and the identifiability problem: which parameters cannot be separated
without an absolute reference. A specification that could not be executed is a
failed answer.

**★★★8.** The second-harmonic response of this model is linear to 0.35% up to
3200 nT. Derive the leading correction to the linear response by expanding
$M_s\tanh((H_d\sin\omega t + H_e)/H_k)$ to third order in $H_e/H_k$, identify the
harmonic at which the correction appears, and predict whether the $2f$ amplitude
grows or saturates as $H_e$ rises.
