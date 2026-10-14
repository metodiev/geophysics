# Exercises — 20-01-05 Sampling, Nyquist and Reconstruction

Attempt these before reading the
[solutions](./05-sampling-theory-solutions.md). The lesson is
[05 Sampling, Nyquist and Reconstruction](../05-sampling-theory.md).
**All models and data in this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** A synthetic source produces a clean $62\ \mathrm{Hz}$ tone, which is
sampled at $100\ \mathrm{Hz}$ without an anti-alias filter. Give the apparent
frequency, the sign of the fold, and state what the record "looks like" to an
analyst who does not know the source.

**★2.** For each pair, give the folded frequency and say whether the fold is
above or below the Nyquist frequency: $(f, f_s) = (45, 100)$, $(75, 100)$,
$(140, 250)$, $(270, 500)$, $(11, 20)\ \mathrm{Hz}$.

**★3.** A 14-bit converter has a range of $\pm5\ \mathrm{V}$. Compute the step
size $q$, the maximum magnitude of the rounding error, and the SNR for a
full-scale sine. Then give the SNR if the sine only reaches $1\ \mathrm{V}$.

## ★★ Applied

**★★4.** A recording is made at $f_s = 250\ \mathrm{Hz}$ with a $12$-bit
converter. The source radiates a clean $130\ \mathrm{Hz}$ tone that reaches the
sensor at an amplitude $40\ \mathrm{dB}$ *below* the full-scale level of the
band of interest. (a) Where does the tone appear in the record? (b) Is it above
or below the quantisation floor? (c) What anti-alias filter attenuation (in dB at
$125\ \mathrm{Hz}$) would put it at the noise floor? State every assumption.

**★★5.** You need 12 effective bits from a 10-bit converter, and the signal band
of interest is $0$–$20\ \mathrm{Hz}$. What sample rate and what oversampling ratio
do you need, what decimation filter would you specify, and what does dither cost
you at $\mathrm{OSR} = 1$? Use the measured numbers from the lesson where they
apply.

**★★6.** A digitising board holds each sample for one full sample interval. At
what fraction of the sample rate does its amplitude response fall by $1\
\mathrm{dB}$? Give the loss at $f/f_s = 0.25$ and at Nyquist, and state whether
this effect can be corrected after acquisition.

## ★★★ Research-oriented

**★★★7.** A microseismic array has receivers every $15\ \mathrm{m}$ and must
record $P$ waves with apparent velocities between $2000$ and $5000\ \mathrm{m/s}$
up to $80\ \mathrm{Hz}$. Compute $f_{\max}$ for each extreme, decide whether the
array meets the requirement, and specify the redesign (spacing, or a spatial
anti-alias filter, or both) that does. Then state the single field measurement
that would tell you whether your assumed $f_{\max}$ is realistic, and what you
would do with the data if it turned out to be optimistic.

**★★★8.** A colleague reports "we oversampled 16x, so we gained 4 bits". Test
that claim using the measurements in the lesson: state what improvement 16x
oversampling can deliver with and without dither, compute the bits implied in
each case, and describe the experiment that would demonstrate which regime their
system is in. Then explain why no amount of oversampling removes an aliased tone,
using the fold map, and state the smallest modification to the acquisition that
would.
