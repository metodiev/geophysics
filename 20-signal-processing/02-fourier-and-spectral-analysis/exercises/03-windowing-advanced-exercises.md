# Exercises — 20-02-03 Window Functions and Spectral Leakage Control

Attempt these before reading the
[solutions](./03-windowing-advanced-solutions.md). The lesson is
[03 Window Functions and Spectral Leakage Control](../03-windowing-advanced.md).
**All models and data in this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** Define coherent gain, ENBW, highest sidelobe level and scalloping loss in
one sentence each, and state what each one costs the analyst.

**★2.** A record of 8192 samples at $f_s = 512\ \mathrm{Hz}$ is windowed with a
Blackman window. Using the measured metric table, give $\Delta f$, the 3-dB
resolution in hertz, and the ENBW in hertz. Then give the same three numbers for
a Hann window and say which is the better choice if the requirement is $5\
\mathrm{Hz}$ resolution.

**★3.** A Hann-windowed amplitude spectrum shows a peak of $0.42\ \mathrm{V}$ at
an unknown bin offset. Give the corrected amplitude for an on-bin tone, and the
range of amplitudes consistent with the reading once scalloping is admitted.

## ★★ Applied

**★★4.** Derive the ENBW of a Hann window from its definition, and then derive
it in general for the $N$-point cosine-sum window
$w[n] = a_0 - a_1\cos(2\pi n/N) + a_2\cos(4\pi n/N)$. Verify your general formula
against the measured values $1.500000$, $1.362826$ and $1.726757$.

**★★5.** Two equal tones are 3 bins apart in a 1024-sample record and must be
separated with at least a $10\ \mathrm{dB}$ dip. Using the measured dip values
from the lesson (or by computing the phase-averaged kernel sum yourself), decide
which windows qualify and explain why the ordering is *not* the same as the
ordering by 3-dB bandwidth.

**★★6.** A record contains a strong off-bin tone and, 20 bins away, a weak tone of
amplitude $1\times10^{-3}$ relative to the strong one. From the measured leakage
floors, decide for each of the six windows whether the weak tone is detectable at
a 3 dB margin, and state the detection limit for the best window.

## ★★★ Research-oriented

**★★★7.** Design a spectral-analysis recipe for a survey with these
requirements: (i) resolve two tones 0.4 % apart in frequency; (ii) detect a tone
$-70\ \mathrm{dB}$ below a strong neighbour 10 bins away; (iii) measure the
amplitude of an isolated tone to $2\%$. State the record length, the window for
each requirement, the ENBW and the detection limit, and say which requirement
dominates the design. If the three requirements cannot be met simultaneously,
say so and give the two alternatives.

**★★★8.** A colleague windows a record with a Hann window *and* segments it into
64-sample pieces at $f_s = 100\ \mathrm{Hz}$, then reports a spectrum down to
$0.5\ \mathrm{Hz}$. Identify the error quantitatively (what does the window do to a
$0.5\ \mathrm{Hz}$ component in a 64-sample segment?), compute the coherent gain
actually seen by that component, and specify the minimum segment length that would
make the window transparent to it. State the general rule.
