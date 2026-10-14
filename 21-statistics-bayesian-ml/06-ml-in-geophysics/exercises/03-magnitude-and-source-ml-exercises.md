# Exercises — 21-06-03 ML for Magnitude Estimation and Source Characterisation

Attempt these before reading the
[solutions](./03-magnitude-and-source-ml-solutions.md). The lesson is
[03 Magnitude and Source](../03-magnitude-and-source-ml.md). All values are
**SYNTHETIC**, printed by
[`code/magnitude_and_source_ml_demo.py`](../code/magnitude_and_source_ml_demo.py).

Generator and measurements to use:

- $\log_{10}A = M - \log_{10}(R/10\ \mathrm{km}) - 1.0
  + \mathcal{N}(0, 0.15^2)$, $A$ in counts;
- $\log_{10}T = \log_{10}(0.4 + 0.1M) + \mathcal{N}(0, 0.05^2)$, $T$ in s;
- 400 events, $M \sim U(2.0, 5.0)$, $R$ log-uniform on $5.0$–$99.8\ \mathrm{km}$;
- hand-written estimator RMSE $0.141$ (full sample $0.145$), learned regressor
  RMSE $0.137$ on a random split;
- range-restricted split at $M = 3.6$: hand-written $0.145$, learned $0.179$ with
  bias $-0.113$.

## ★ Foundational

**★1.** Compute $\hat M$ by hand for three measurements, giving the answer in
magnitude units to three decimals: (a) $\log_{10}A = 1.20$, $R = 10\ \mathrm{km}$;
(b) $\log_{10}A = 1.20$, $R = 25\ \mathrm{km}$; (c) $\log_{10}A = 1.20$,
$R = 100\ \mathrm{km}$. State the distance correction you applied.

**★2.** Using the amplitude scatter $\sigma_{\log A} = 0.15$ as the magnitude
uncertainty, compute the standard error of the *mean* magnitude residual from
$n$ events. How many events are needed to state the mean bias to $\pm0.02$
magnitude units at one standard error, and how many at three?

**★3.** Compute the relative RMSE improvement of the learned model over the
hand-written estimator on the random split, as a percentage. Then compute the
relative degradation on the extrapolation test. State which of the two numbers a
reviewer should react to.

## ★★ Applied

**★★4.** The generator has $\log_{10}A = M - \log_{10}R' + c + \varepsilon$ with
$\varepsilon \sim \mathcal{N}(0,0.15^2)$ and $R' = R/10\ \mathrm{km}$. Explain
why $\log_{10}A$ is a *noisy regressor* rather than a noisy response, and compute
the first-order errors-in-variables attenuation factor
$\mathrm{Var}(\text{true})/(\mathrm{Var}(\text{true}) + \sigma_\varepsilon^2)$
using $\mathrm{Var}(M)$ for $M\sim U(2,5)$ and $\mathrm{Var}(\log_{10}R)$ for
$\log_{10}R \sim U(0.7,2.0)$. Compare it with the fitted standardised coefficient
$+0.904$ on $\log_{10}A$ and list the two reasons the numbers differ.

**★★5.** Design the per-magnitude-bin residual diagnostic: choose the bins, the
per-bin metric and its uncertainty, and compute the sample size per bin that
resolves a bias of $\pm0.05$ magnitude units at three standard errors. State what
the diagnostic would look like if the model were saturated.

**★★6.** Suppose the catalogue comes from two stations with offsets $+0.1$ and
$-0.1$ magnitude units, both estimated by the hand-written law with the same
$0.15$ scatter. Compute the pooled bias, the per-station bias, and the pooled
RMSE. State the sample size per station needed to detect the offset at three
standard errors, and the modelling change that removes it.

## ★★★ Research-oriented

**★★★7.** Design a study that tests whether a learned magnitude model genuinely
beats the classical formula on a real catalogue. Name the confound that makes
the comparison unfair by default, the split, the metric, the strata, and the
result that would falsify the claim.

**★★★8.** Extend the generator with a saturation corner at $M_c$ and specify the
experiment that measures where RMSE departs from the uncapped value. State the
metric, the sweep, and the inference that the experiment cannot support.

**★★★9.** A moment-tensor predictor is trained on labels produced by a waveform
inversion whose own error variance is $0.3$ times the variance of the true
source parameters. Compute the largest $R^2$ the predictor can possibly achieve
against those labels, and design the synthetic-truth experiment that would
separate "the model is weak" from "the labels are noisy".
