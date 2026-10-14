# Exercises — 20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation

Attempt these before reading the
[solutions](./01-deconvolution-concept-solutions.md). The lesson is
[01 Deconvolution: Concept](../01-deconvolution-concept.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the water-level (damped) inverse formula and identify every symbol
with its units.

**★2.** State in two sentences why a band-limited wavelet makes deconvolution
ill-posed, using the words *division* and *noise*.

**★3.** Distinguish band-limit bias from regularisation bias in one sentence each.

## ★★ Applied

**★★4.** Using the lesson's water-level table, choose a water level for a survey
that must resolve a 25 ms pulse while keeping the noise gain below $+12$ dB. State
the numbers you compared.

**★★5.** A wavelet has a usable-band condition number of 500, and the demo's
wavelet has 950.2. Estimate the ratio of their naive-inverse noise amplifications
and the difference in dB.

**★★6.** The oracle sweep gives best $\varepsilon$ values of $2.371\times10^{-4}$
at NSR $=10^{-3}$ and $1.334\times10^{-5}$ at NSR $=1.003\times10^{-4}$. Compute
the ratio $\varepsilon/\text{NSR}$ in each case and comment on the consistency.

## ★★★ Research-oriented

**★★★7.** Derive the optimal $\varepsilon$ for a single-frequency problem by
minimising the expected squared error, and show it equals the noise-to-signal power
ratio. Then explain why the demo's measured ratio is about 0.2 rather than 1.

**★★★8.** The numerical condition number is $3.686\times10^{36}$ while the
usable-band figure is 950.2. Explain which is a property of the physics, which is a
property of floating point, and how you would decide which to quote.