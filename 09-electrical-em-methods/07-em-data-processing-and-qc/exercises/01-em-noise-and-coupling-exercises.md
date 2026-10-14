# Exercises — 09-07-01 EM Noise, Coupling and Cultural Effects

Attempt these before reading the
[solutions](./01-em-noise-and-coupling-solutions.md). The lesson is
[01 EM Noise, Coupling and Cultural Effects](../01-em-noise-and-coupling.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A Wenner sounding uses spacings 1, 2, 4, 8, 16 and 32 m. A constant
potential error $\sigma_V$ is chosen so that the 1 m spacing has a $1\%$ error.
Compute $\sigma_{\rho_a}$ and the relative error at each spacing, and state which
spacing limits the sounding.

**★2.** Classify each of the following as incoherent noise, coherent noise or
systematic error, and say whether stacking helps: (a) thermal noise in the
receiver; (b) a 50 Hz line whose phase is locked to the acquisition clock;
(c) a buried metal pipe crossing the array; (d) telluric fluctuations with a
period of minutes measured during a 30 s repeat; (e) a drifting electrode
contact resistance.

**★3.** A phase-locked line has amplitude $3\sigma_V$ in volts and the geometric
factor is $K = 2\pi a$. Compute its amplitude in apparent-resistivity units at
1 m and at 32 m for $\sigma_V = 0.04$ (arbitrary volt units).

## ★★ Applied

**★4.** Derive the $1/\sqrt{N}$ law for the mean of $N$ independent samples with
variance $\sigma^{2}$, and state the two assumptions it needs. Then say which
assumption the demonstration's drifting-phase case violates and how.

**★5.** The demonstration measures rms errors of 3.940 (mean) and 2.181 (median)
$\Omega\,\mathrm{m}$ under a $2\%$, $15\sigma$ spike population, and states that
the median is about $1.571$ times less efficient than the mean under pure
Gaussian noise. Compute the rms error you would expect from the median on the
*clean* data, and decide which stacker you would use for a survey with a $5\%$
contamination rate.

**★6.** In the phase-locked case the design matrix of a repeat-axis notch has
singular values 11.3137, 0 and 0 over 64 repeats. Explain in one paragraph why
the notch makes the estimate *worse* (73.588 against 22.698 $\Omega$ m in the
demonstration) rather than merely failing to help.

## ★★★ Research-oriented

**★★★7.** Design an acquisition scheme whose repeat interval guarantees a
minimum phase advance of $0.4$ rad between consecutive repeats for a 50 Hz line,
for a repeat period of about 1 s and a sampling rate of 1 kHz. State the interval
you choose, the resulting phase advance, and the residual coherent amplitude
after 64 repeats. A specification that could not be executed is a failed answer.

**★★★8.** The demonstration inverts a sounding containing a phase-locked line and
finds $\rho_2$ biased by $+11\%$ to $+38\%$ while $H$ moves by under 0.7 m.
Explain why the coherent error lands mostly on $\rho_2$ rather than on $H$, using
the sensitivity matrix of module [09-07-03](../03-em-uncertainty.md), and design
a survey change that would move the bias onto a parameter you would rather
sacrifice.
