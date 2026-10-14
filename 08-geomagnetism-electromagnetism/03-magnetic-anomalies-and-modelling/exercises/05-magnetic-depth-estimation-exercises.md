# Exercises — 08-03-05 Depth Estimation

Attempt these before reading the
[solutions](./05-magnetic-depth-estimation-solutions.md). The lesson is
[05 Depth Estimation](../05-magnetic-depth-estimation.md). All models are
**SYNTHETIC**.

## ★ Foundational

**★1.** Write Euler's equation and state the structural index for a dipole, a
vertical cylinder, a thin sheet and a contact.

**★2.** In the demonstration, Euler with $N = 3$ returns a median depth of
3.018 km and with $N = 2$ a median of 2.424 km, for a true depth of 3.000 km.
Compute each ratio and state which is acceptable.

**★3.** State the half-width rule for a 2-D line source and compute the depth it
gives for a measured FWHM of 3.0 km.

## ★★ Applied

**★★4.** The same rule applied to a dipole profile in the demonstration gives
FWHM $= 2.000$ km and hence $z = 1.000$ km, against a true depth of 2.00 km.
Compute the error and state in one sentence why the rule is not slightly wrong
but wrong by a factor.

**★★5.** The spectral method fits $\ln P - 2\ln k = \text{const} - 2kz_0$. A fit
returns a slope of $-8000$ m per (rad m$^{-1}$). Compute the depth it implies.

**★★6.** In the noise table, the median Euler depth rises from 4.052 km at zero
noise to 6.160 km at 10 nT rms. Compute the change and state, in one sentence,
which of the two contributing effects dominates.

## ★★★ Research-oriented

**★★★7.** The spectral fit on an ensemble of 160 equal-moment dipoles half at
2 km and half at 6 km returns 2.951 km, and the moment-squared weighted mean at
the band centre is 2.022 km. Explain, in terms of the assumptions of the
Spector–Grant derivation, why the two differ, and state what experimental change
would make the method succeed.

**★★★8.** Design a test that would determine whether a Werner depth from a noisy
profile is meaningful. State the diagnostic you would compute, the threshold you
would set, and what you would report if the diagnostic fails.

**★★★9.** A colleague reports an Euler depth of $4.2$ km from data smoothed with
a 1 km Gaussian and a window of 8 km. State three corrections or caveats you
would require before accepting the number, and justify each with a number from
the lesson.
