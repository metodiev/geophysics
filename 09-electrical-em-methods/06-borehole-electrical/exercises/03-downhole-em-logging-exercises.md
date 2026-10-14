# Exercises — 09-06-03 Downhole EM Logging and Induction Tools

Attempt these before reading the
[solutions](./03-downhole-em-logging-solutions.md). The lesson is
[03 Downhole EM Logging and Induction Tools](../03-downhole-em-logging.md).
All models are **SYNTHETIC** teaching values; $\mu_0$ is a standard constant.

## ★ Foundational

**★1.** A two-coil sonde operates at 20 kHz. For a $20\ \Omega\,\mathrm{m}$
formation, compute the skin depth and the induction number for coil spacings of
0.50, 1.00 and 1.50 m. State which (if any) is in the wave regime.

**★2.** Show by dimensional analysis that $\delta = \sqrt{2/(\omega\mu\sigma)}$ is
a length, and that $\delta$ falls as $\sigma^{-1/2}$ while the apparent-conductivity
bias of a linear calibration rises as $\sigma^{1/2}$.

**★3.** Using the small-$p$ result $\sigma_a/\sigma - 1 \approx \tfrac{2}{3}p$,
estimate the bias for the three spacings of ★1 and compare with the exact table
in the lesson ($p = 0.05$: $+3.33\%$; $p = 0.10$: $+6.65\%$; $p = 0.20$:
$+13.22\%$).

## ★★ Applied

**★4.** For the synthetic sonde ($L = 1.00$ m, 20 kHz), find the formation
resistivity at which the skin-effect bias of the quadrature calibration reaches
10%, using both the approximation $\tfrac23p$ and the exact value at that $p$.

**★5.** The lesson measures that the vertical response carries a fraction 0.5034
of the measurement inside $|z|\le L/2$, 0.7579 inside $|z|\le L$ and 0.8840
inside $|z|\le 2L$. Use those numbers to estimate the bed thickness at which the
peak reading comes within 5% of the true bed conductivity, and check your estimate
against the shoulder-effect table (a 1 m bed reads 0.9484 S/m with $L = 0.25$ m).

**★6.** A 1 m bed of $1.00\ \mathrm{S\,m^{-1}}$ in a
$0.10\ \mathrm{S\,m^{-1}}$ formation reads 0.7922 S/m at the peak with $L = 1$ m.
An analyst converts that reading to water saturation with
$\sigma \propto S_w^{2}$. Compute the saturation error, and state one independent
measurement that would settle whether the error is real.

## ★★★ Research-oriented

**★★★7.** Design a two-frequency, two-spacing induction experiment that
separates a salinity change from a clay-content change in a sand-shale sequence.
State the model you would invert, the data you would weight most, and the
degeneracy that remains even after the experiment. A specification that could not
be executed is a failed answer.

**★★★8.** The Doll geometric factor assumes a homogeneous medium, no borehole and
no skin effect. Design a study that measures the error introduced by the borehole
alone, and specify the statistic that would reveal it. State how you would
separate the borehole effect from the skin effect in the same data set.
