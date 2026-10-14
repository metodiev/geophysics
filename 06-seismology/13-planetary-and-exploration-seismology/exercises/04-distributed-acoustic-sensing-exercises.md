# Exercises — 06-13-04 Distributed Acoustic Sensing: A New Observational Regime

Attempt these before reading the
[solutions](./04-distributed-acoustic-sensing-solutions.md). The lesson is
[04 Distributed Acoustic Sensing](../04-distributed-acoustic-sensing.md). All
models are **SYNTHETIC**.

## ★ Foundational

**★1.** A gauge of length $L = 30\ \mathrm{m}$ records a wave with wavelength
$\lambda = 120\ \mathrm{m}$. Compute the response factor
$\mathrm{sinc}(\pi L/\lambda)$ and the amplitude loss in dB
($20\log_{10}$ of the factor).

**★2.** For the same wave, compute $k$ and $k_{\text{Nyq}}$ for a channel spacing
$d = 20\ \mathrm{m}$, and state whether the array is aliased.

**★3.** A surface wave has particle velocity amplitude
$v_0 = 3.0\times10^{-5}\ \mathrm{m\,s^{-1}}$ at $c = 600\ \mathrm{m\,s^{-1}}$ and
$f = 12\ \mathrm{Hz}$. Compute the axial strain amplitude and the strain rate
amplitude, with units.

## ★★ Applied

**★★4.** A wavefront crosses a fibre at $40^{\circ}$ to the fibre axis. **(a)**
By what factor is the response to a P wave reduced? **(b)** What is the response
to an SH wave polarised perpendicular to the fibre, and why? **(c)** At what
angle is the SV response maximum, and what is its value there?

**★★5.** Channels at $d = 30\ \mathrm{m}$ record an apparent phase velocity of
$+2500\ \mathrm{m\,s^{-1}}$ at $4\ \mathrm{Hz}$. **(a)** Compute the true
wavenumber of that wave. **(b)** Determine the true wavenumber(s) that would alias
to it, and the corresponding true phase velocities. **(c)** State the
measurement you would make to decide which is correct.

**★★6.** A fibre is deployed with $d = 5\ \mathrm{m}$, $L = 20\ \mathrm{m}$,
sampled at $500\ \mathrm{Hz}$. **(a)** Compute the Nyquist wavenumber and the
range of the temporal band. **(b)** Compute the gauge response at $30\ \mathrm{Hz}$
for a $200\ \mathrm{m\,s^{-1}}$ wave. **(c)** State which of the two sampling
parameters is the binding constraint for this target and why.

## ★★★ Research-oriented

**★★★7.** A research programme proposes to use a $20\ \mathrm{km}$ trench-deployed
fibre to image a sedimentary basin to $500\ \mathrm{m}$ depth, with targets from
$0.5$ to $15\ \mathrm{Hz}$ and phase velocities between $200$ and
$1500\ \mathrm{m\,s^{-1}}$. Specify $d$, $L$ and the sample rate with the
arithmetic that justifies each, state the aperture implied and the longest
wavelength it can measure, and list the three assumptions about coupling and
instrument response that must be tested before publishing an amplitude.

**★★★8.** The lesson measures that a longer gauge improves the signal-to-noise of
a broadband detector while leaving a narrowband detector unchanged. Derive that
result analytically for spatially independent noise: show that the
signal-to-noise of a matched filter at the signal's own wavenumber is independent
of $M = L/d$, and identify the step at which the naive $1/\sqrt{M}$ noise
reduction is cancelled. Then state the condition on the noise spectrum under
which a longer gauge *does* help a narrowband detector.
