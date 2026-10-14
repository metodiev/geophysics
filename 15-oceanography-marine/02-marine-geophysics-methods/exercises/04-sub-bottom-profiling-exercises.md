# Exercises — 15-02-04 Sub-Bottom Profiling and Chirp Systems

Attempt these before reading the
[solutions](./04-sub-bottom-profiling-solutions.md). The lesson is
[04 Sub-Bottom Profiling](../04-sub-bottom-profiling.md). All parameters are
**SYNTHETIC** teaching values.

Use $c_{\text{sed}} = 1600\ \mathrm{m\,s^{-1}}$ unless told otherwise, and the
attenuation law $\alpha(f) = 0.10\,(f/\mathrm{kHz})^{1.0}\ \mathrm{dB\,m^{-1}}$
one-way.

## ★ Foundational

**★1.** A chirp sweeps $1.0\ \mathrm{kHz}$ to $8.0\ \mathrm{kHz}$ over
$15\ \mathrm{ms}$ in a sediment of $1700\ \mathrm{m\,s^{-1}}$. Compute $B$, the
sweep rate, $BT$, and the resolution $c/(2B)$.

**★2.** For the same chirp, compute the number of samples $N$ at
$F_s = 100\ \mathrm{kHz}$ and the matched filter's gain in dB under the lesson's
definitions.

**★3.** State which of the three contributions to that gain is specific to a
chirp, and why the other two are not.

## ★★ Applied

**★★4.** Derive $G = \sqrt{N}$ in amplitude from the correlator's definitions:
the peak of the compressed signal is $\sum_k s_k^{2}$, and the standard deviation
of the compressed noise is $\sigma\sqrt{\sum_k s_k^{2}}$.

**★★5.** Compute the two-way attenuation loss for $60\ \mathrm{dB}$ of dynamic
range at $3\ \mathrm{kHz}$ and at $6\ \mathrm{kHz}$, and give the penetration
depth at each. State the trade in one sentence.

**★★6.** A rectangular chirp of the lesson's parameters has a compressed FWHM of
$0.2900\ \mathrm{ms}$ and a peak side lobe of $-13.57\ \mathrm{dB}$; a Hann taper
gives $0.5500\ \mathrm{ms}$ and $-26.10\ \mathrm{dB}$. (a) Convert both FWHMs to
resolution in a sediment of $1600\ \mathrm{m\,s^{-1}}$. (b) State which taper you
would choose to resolve reflectors $0.35\ \mathrm{m}$ apart and why.

**★★7.** A reflection coefficient of $-22\ \mathrm{dB}$ and a target
$35\ \mathrm{m}$ below the seabed must be detected with $8\ \mathrm{dB}$ of
margin at $5\ \mathrm{kHz}$. Using $\alpha = 0.5\ \mathrm{dB\,m^{-1}}$ and a
matched filter with $33\ \mathrm{dB}$ of gain, state whether the target is
detectable if the system's unprocessed echo level is $45\ \mathrm{dB}$.

## ★★★ Research-oriented

**★★★8.** Design a survey that resolves a $0.3\ \mathrm{m}$ layer at
$25\ \mathrm{m}$ below the seabed in a sediment of $1700\ \mathrm{m\,s^{-1}}$,
stating the required bandwidth, the required frequency band, the implied
penetration requirement at the required dynamic range, and which of the four
constraints (bandwidth, attenuation, energy, side lobes) binds. A specification
that could not be executed is a failed answer.

**★★★9.** The lesson measures the compressed FWHM directly and finds a
factor-1.6 degradation at $30\ \mathrm{m}$ of path, where the half-power bandwidth
predicts a factor 8. Explain the discrepancy in terms of the shape of the
surviving spectrum, and state which quantity a practising processor should quote.
