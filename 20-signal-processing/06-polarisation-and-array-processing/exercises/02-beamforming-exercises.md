# Exercises — 20-06-02 Beamforming, Slowness Estimation and f-k Analysis

Attempt these before reading the
[solutions](./02-beamforming-solutions.md). The lesson is
[02 Beamforming](../02-beamforming.md). All models are **SYNTHETIC** teaching
values.

## ★ Foundational

**★1.** A linear array has 20 sensors with 1.5 km spacing and records a 4 Hz
wave. Compute the aperture, the first-null offset in slowness, the grating-lobe
spacing, and the aliasing-free slowness range.

**★2.** For the same array at 12 Hz, state which of the four numbers of ★1 change
and give the new values.

**★3.** Two arrivals differ in slowness by $0.02\ \mathrm{s\,km^{-1}}$. Will the
array of ★1 resolve them at 4 Hz? Justify with a number.

## ★★ Applied

**★★4.** A colleague reports an array gain of $20\ \mathrm{dB}$ from 10
incoherent sensors. Show that this is impossible for the stated conditions, give
the correct value, and name the two most likely errors behind their number.

**★★5.** Derive the $N$-fold array gain from the beamformer definition and
evaluate it for $N = 36$ sensors. State the condition on the noise.

**★★6.** An array with 4 km spacing is used at 5 Hz to search slownesses around
$0.10\ \mathrm{s\,km^{-1}}$. Compute the grating-lobe positions and decide whether
the search range $\pm0.06\ \mathrm{s\,km^{-1}}$ is safe.

## ★★★ Research-oriented

**★★★7.** Design a linear array that resolves slownesses $0.005\ \mathrm{s\,km^{-1}}$
apart at 2 Hz with no grating lobe within $|s| < 0.1\ \mathrm{s\,km^{-1}}$ and no
sensor spacing above 2.5 km. Report the aperture, the number of sensors and the
achieved numbers. A specification that could not be executed is a failed answer.

**★★★8.** The demonstration measures two plane waves separated by
$0.004\ \mathrm{s\,km^{-1}}$ as a single merged peak, and by
$0.015\ \mathrm{s\,km^{-1}}$ as two distinct peaks. Explain, using the array
response, why there is a hard threshold rather than a gradual degradation, and why
no post-processing can recover the merged case.
