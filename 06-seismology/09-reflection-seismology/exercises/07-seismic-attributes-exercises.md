# Exercises — 06-09-07 Seismic Attributes and Quantitative Interpretation

Attempt these before reading the
[solutions](./07-seismic-attributes-solutions.md). The lesson is
[07 Seismic Attributes](../07-seismic-attributes.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute $\lambda$, $\lambda/4$ and $\lambda/8$ for
$v = 2600\ \mathrm{m\,s^{-1}}$ and $f_0 = 25\ \mathrm{Hz}$, with units.

**★2.** Verify the demonstration's resolution scales for
$v = 3000\ \mathrm{m\,s^{-1}}$, $f_0 = 30\ \mathrm{Hz}$: $\lambda = 100\
\mathrm{m}$, $\lambda/4 = 25\ \mathrm{m}$, $\lambda/8 = 12.5\ \mathrm{m}$.

**★3.** The demonstration's tuning maximum is at a bed thickness of $20.0\
\mathrm{m}$, with a two-way time separation of $13.3\ \mathrm{ms}$. Verify both
numbers from $v = 3000\ \mathrm{m\,s^{-1}}$ and the definition of the two-way
separation for a thin bed.

## ★★ Applied

**★★4.** Derive the zero-offset first Fresnel radius
$r_f \approx \sqrt{\lambda z/2}$ from the half-wavelength path criterion, and
verify it at $z = 500\ \mathrm{m}$ and $z = 4000\ \mathrm{m}$ with
$\lambda = 100\ \mathrm{m}$ (the demonstration's printed values are $158.1$ and
$447.2\ \mathrm{m}$).

**★★5.** Using the demonstration's detection table (noise rms $0.050$, so the
$3\sigma$ threshold for a difference is $0.212$), explain why a $10\ \mathrm{m}$
bed needs a contrast of $0.30$ to be detected while a $20\ \mathrm{m}$ bed is
detected at $0.15$. Then state which of the two has the *better vertical
resolution* and why the two questions are different.

**★★6.** The demonstration measures the amplitude ratio between a bed of
$2\ \mathrm{m}$ and one of $4\ \mathrm{m}$ (equal contrast) as $1.97$, and
between $8\ \mathrm{m}$ and $16\ \mathrm{m}$ as $1.53$. State the regime each
pair is in, and explain the difference in one sentence using $\lambda/8$.

## ★★★ Research-oriented

**★★★7.** Design a workflow to estimate the thickness of a bed thinner than
$\lambda/4$ from seismic data. State how thickness is estimated, list every
assumption it requires, and say which assumption would fail first in a real data
set. Include the quantitative check that would detect that failure.

**★★★8.** The demonstration's instantaneous frequency at the wavelet peak is
$33.81\ \mathrm{Hz}$ for a $30\ \mathrm{Hz}$ Ricker. Explain why an attribute
that is supposed to measure "the frequency" is biased at the peak, and specify
the amplitude threshold rule you would apply before averaging an instantaneous
frequency map.
