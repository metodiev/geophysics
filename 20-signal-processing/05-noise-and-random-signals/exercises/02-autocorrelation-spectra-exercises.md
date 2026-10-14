# Exercises — 20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin

Attempt these before reading the
[solutions](./02-autocorrelation-spectra-solutions.md). The lesson is
[02 Autocorrelation and PSD](../02-autocorrelation-spectra.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A record has $N = 2048$ samples at $f_s = 64\ \mathrm{Hz}$. State the
frequency resolution $\mathrm{d}f$, the Nyquist frequency, and the number of
values in a one-sided PSD array.

**★2.** A record has sample variance $2.50$, and its computed one-sided PSD
integrates to $5.00$. Identify the most likely error and the corrected value.

**★3.** A single periodogram value is reported with an estimated standard error
of $5\%$ of its mean. State the measured ratio you would actually expect for
white noise, and what changes (if anything) when the record length is doubled.

## ★★ Applied

**★★4.** A record has $N = 8192$ samples at $f_s = 100\ \mathrm{Hz}$. A survey
needs a PSD with a $15\%$ standard error and a resolution of $1\ \mathrm{Hz}$.
Find a segment length and overlap, or show the two requirements conflict, and
state the best compromise.

**★★5.** Derive $\operatorname{std}(\hat S)/\mathbb{E}[\hat S] = 1$ for a
Gaussian white record, starting from the distribution of the DFT coefficients.

**★★6.** Two spectral lines are $4\ \mathrm{Hz}$ apart in a record at
$f_s = 200\ \mathrm{Hz}$ analysed with a Hann window whose nominal resolution is
$2f_s/N_{\text{seg}}$. Find the smallest $N_{\text{seg}}$ that resolves them.

## ★★★ Research-oriented

**★★★7.** Specify a Monte Carlo experiment that measures the *bias* (not the
variance) introduced by segmenting a record with a Hann window, as a function of
$N_{\text{seg}}$, on a spectrum with one narrow line. State the metric, the
expected direction of the bias, and how you separate it from variance. A
specification that could not be executed is a failed answer.

**★★★8.** The demonstration verifies the periodogram against the transform of
the biased autocovariance over the whole 8192-sample record and finds a maximum
difference of $9.7\times10^{-17}$. Explain (a) why the two quantities are the
same object, and (b) why the residual is of order $10^{-16}$ and not $10^{-30}$
in double precision, and why the check cannot be extended to a record of
$10^{7}$ samples without rethinking the tolerance.
