# Exercises — 16-08-02 Reanalysis: ERA5, MERRA, JRA and Their Caveats

Attempt these before reading the
[solutions](./02-reanalysis-products-solutions.md). The lesson is
[02 Reanalysis: ERA5, MERRA, JRA and Their Caveats](../02-reanalysis-products.md).
All models and numbers are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A scalar analysis has background variance $B = 0.04\ \mathrm{K^{2}}$ and
observation error variance $R = 0.01\ \mathrm{K^{2}}$. With background
$x^{b} = 1.0\ \mathrm{K}$ and observation $y = 1.5\ \mathrm{K}$, compute the gain
$K$, the analysis $x^{a}$ and the analysis variance $B^{a}$.

**★2.** State what the analysis reduces to in the two limits $R \to \infty$ and
$B \to 0$, and explain why the two limits are the same failure.

**★3.** For $\varphi = 0.70$ and process-noise variance $Q = 0.05^{2}\
\mathrm{K^{2}}$, compute the steady-state background variance and its standard
deviation when no observations are assimilated.

## ★★ Applied

**★★4.** Using the steady-state bias relation
$\text{bias} = \dfrac{(1-K)(c_{\text{model}}-c_{\text{truth}})}{1-\varphi(1-K)}$
with $K = 0.5$, $c_{\text{model}} = -0.10\ \mathrm{K\,step^{-1}}$ and
$c_{\text{truth}} = +0.05\ \mathrm{K\,step^{-1}}$, compute the analysis bias and
state its sign.

**★★5.** A product has a level discontinuity of $0.40\ \mathrm{K}$ at year 30 of a
60-year record. Using $\sum_t(t-\bar t)^{2} = 17{,}995$ and
$\sum_{t\ge30}(t-\bar t) = 450$, compute the apparent trend the discontinuity
produces.

**★★6.** A reanalysis ensemble spread in a data-sparse era is
$0.10\ \mathrm{K}$ and the actual rms error against an independent truth is
$0.40\ \mathrm{K}$. Compute the ratio and state, in one sentence, which component
of the error is missing from the spread.

## ★★★ Research-oriented

**★★★7.** Design a validation that would distinguish a reanalysis trend caused by
a change in the observing system from a genuine climate trend. Specify the
diagnostic, the null hypothesis, and the result that would leave the two
indistinguishable.

**★★★8.** Two reanalysis families agree on a regional warming trend while a
homogenised station product gives a smaller trend. A colleague concludes that the
two reanalyses confirm each other. Write the response, and design a synthetic
experiment that would measure how much of the agreement is due to shared
observations rather than to truth.
