# Exercises — 20-05-03 Colour of Noise: White, Pink, Red and Geophysical Examples

Attempt these before reading the
[solutions](./03-noise-colour-solutions.md). The lesson is
[03 Colour of Noise](../03-noise-colour.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** Three records have successive octave-band power ratios of $2.0$, $1.0$
and $0.5$. For each, state the spectral index $\alpha$, the Hurst exponent $H$,
and the conventional colour name.

**★2.** A structure function is measured to grow as $D(T) \propto T^{0.6}$ over
two decades. State $H$, $\alpha$, and the slope of the log–log PSD.

**★3.** A mean is estimated from a record of $n = 4000$ samples with a naive
standard error of $0.02$. The measured integrated correlation time is 400
samples. Give the corrected standard error and the factor by which the naive
value was wrong.

## ★★ Applied

**★★4.** For a band-limited $f^{-1}$ spectrum between $f_{\min} = 1/T$ and the
Nyquist frequency, derive the scaling of $\operatorname{Var}(\bar x_T)$ with
$T$, and state why the result is between the white and the red cases.

**★★5.** Design a procedure that classifies a record as white, pink or red using
**only** octave-band powers. State the minimum number of bands, the minimum
dynamic range over which it works, and the failure mode.

**★★6.** A monitoring study claims a noise reduction by averaging 100 records,
each of which has an $f^{-2}$ spectrum. Quantify what part of the error is
reduced by the average and what part survives, using the structure-function
scaling of the lesson.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures how the *fitted* spectral exponent
of a pink-noise record depends on the band over which the fit is made. State the
prediction, the metric, and why a single fitted number without its band is not a
measurement. A specification that could not be executed is a failed answer.

**★★★8.** A colleague reports $H = 0.8$ for a geophysical series and concludes
that the process is "persistent". State two independent checks that would have to
be passed before that conclusion is defensible, and describe what measurement
would falsify it.
