# Exercises — 20-04-03 Wiener Filtering and Least-Squares Inverse Filters

Attempt these before reading the
[solutions](./03-wiener-filtering-solutions.md). The lesson is
[03 Wiener Filtering](../03-wiener-filtering.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** Write the mean squared error that the Wiener filter minimises, and state
what the "desired signal" is in the deconvolution case.

**★2.** Write the Wiener-Hopf normal equations for a filter of length $L = 2$,
identifying each correlation term.

**★3.** State the orthogonality condition and explain in one sentence why it is a
*checkable* optimality criterion.

## ★★ Applied

**★★4.** The demo's orthogonality residuals are $4.11\times10^{-4}$ for lags
$0$–$60$ and $1.29\times10^{-2}$ for lags $-60$–$0$. Explain why the second is
larger, and which one is the meaningful test.

**★★5.** Using the record-SNR table, state where you would and would not bother
with a Wiener filter rather than a naive inverse, with numbers.

**★★6.** The demo's filter-length sweep gains only 0.55 dB going from length 5 to
length 161. Explain what the extra coefficients are doing and connect it to the
notion of regularisation.

## ★★★ Research-oriented

**★★★7.** Derive the excess mean squared error of a length-$L$ Wiener filter
relative to the infinite-length filter, and compare its predicted size with the
measured 0.55 dB.

**★★★8.** Show that the matched filter maximises the peak signal-to-noise ratio but
does not minimise mean squared error, and construct a numeric example where a
Wiener filter and a matched filter rank the same two candidate desirable signals
differently.