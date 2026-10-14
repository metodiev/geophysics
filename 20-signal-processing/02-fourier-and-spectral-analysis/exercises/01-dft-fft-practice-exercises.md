# Exercises — 20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls

Attempt these before reading the
[solutions](./01-dft-fft-practice-solutions.md). The lesson is
[01 Practical DFT/FFT](../01-dft-fft-practice.md). **All models and data in this
module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** Write the forward and inverse DFT as `numpy.fft` defines them. State
which one carries $1/N$ and the sign of each exponent.

**★2.** A 2048-sample record sampled at $512\ \mathrm{Hz}$ contains a
$1\ \mathrm{V}$ sine at $64\ \mathrm{Hz}$. Give $\Delta f$, the raw peak bin
value $\lvert X\rvert$, the amplitude-spectrum value and the one-sided PSD value,
with units. Show that the PSD integrates to the sine's power.

**★3.** A 40-sample pulse sits in a 1000-sample record. List five bin indices at
which its DFT is exactly zero, and explain the rule in one sentence.

## ★★ Applied

**★★4.** The tone in ★2 is at $64.1\ \mathrm{Hz}$ instead of $64\ \mathrm{Hz}$.
Compute the bin offset, the expected amplitude-spectrum peak using the Dirichlet
factor, the error in dB, and the amplitude you would report if you naively read
the peak.

**★★5.** A colleague reports a flat noise PSD of $1.0\times10^{-9}$ in units of
"power" for a synthetic channel whose time-domain rms is $1.0\times10^{-4}$ and
whose record is 100 s long at $200\ \mathrm{Hz}$. Test the claim with Parseval
and state the most likely error (state whether the value is a one-sided PSD, a
two-sided PSD or a power in a bin).

**★★6.** For $x[n] = e^{+2\pi i k_0 n/N}$ with $N = 128$ and $k_0 = 3$, compute
the DFT by hand at $k = 3$ and at $k = 4$, and verify your two values against the
identities in the lesson. Then state what happens if the same signal is fed to
`fft` with $k_0 = 131$ and explain why no aliasing has occurred in the DFT.

## ★★★ Research-oriented

**★★★7.** Design a test suite (in pseudocode with stated tolerances) that would
catch: a normalisation error, an off-by-one in the bin indexing, a missing
$2/N$, a doubling of the Nyquist bin, and a leakage assumption. For each bug
state which test fails, why, and the size of the residual you would expect from
rounding alone. Then say which of the five bugs no spectral test can detect and
why.

**★★★8.** A synthetic microseism record is to be searched for a monochromatic
signal at an unknown frequency in $0.05$–$2\ \mathrm{Hz}$ with an amplitude
$100$ times smaller than the broadband noise. Specify the record length, the
window, the estimator and the threshold, and compute the smallest detectable
amplitude relative to the noise level for your choice. State where your
calculation is a bound and where it is an estimate. (You may use the exact
periodogram statistics of lesson 20-02-02 without re-deriving them, but state
which result you use.)
