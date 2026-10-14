# Exercises — 10-05-05 Integrating Near-Surface Methods

Attempt these before reading the
[solutions](./05-multi-method-nearsurface-solutions.md). The lesson is
[05 Integrating Near-Surface Methods](../05-multi-method-nearsurface.md). All
models are **SYNTHETIC** teaching values; reference numbers come from
`code/multi_method_demo.py`. Constants: $k_s = 3.00$, $k_w = 0.60$,
$k_a = 0.025\ \mathrm{W\,m^{-1}\,K^{-1}}$; the mixing model is the geometric mean
$k = k_s^{1-\phi}k_w^{\theta}k_a^{\phi-\theta}$ and the electrical relation is
$\sigma = \sigma_w\theta^{m}$.

## ★ Foundational

**★1.** Differentiate $\sigma = \sigma_w\theta^{m}$ logarithmically and state, in
words, how a 10% uncertainty in the pore-water conductivity propagates into the
inferred water content for $m = 2$.

**★2.** Compute the thermal conductivity of a soil with $\phi = 0.40$ and
$\theta = 0.15$ using the teaching constants. State the units of every factor.

**★3.** Explain in three sentences why two different methods that are both
sensitive to water content can together determine it, even though neither can
alone.

## ★★ Applied

**★★4.** The measured pair is $\sigma = 21.83\ \mathrm{mS\,m^{-1}}$ and
$k = 0.6661\ \mathrm{W\,m^{-1}\,K^{-1}}$. Suppose an independent water sample
shows $\sigma_w = 0.100 \pm 0.010\ \mathrm{S\,m^{-1}}$. Compute the admissible
water content from the electrical reading alone, compare it with the interval
obtained from the thermal reading, and state in one sentence what the disagreement
means for the assumed $\sigma_w$.

**★★5.** A colleague assumes $\phi = 0.40$ instead of the true $0.45$ and inverts
the same thermal reading. Compute the water content obtained, compare with the
value for $\phi = 0.45$, and state the direction and size of the error. Explain
the sign physically.

**★★6.** Using the Monte Carlo result of the lesson ($\theta = 0.2042 \pm 0.0093$,
$\sigma_w = 0.2373 \pm 0.0203$, correlation $-0.808$), state whether the pair
$(\theta, \sigma_w) = (0.19, 0.30)$ is within the joint one-sigma region, and
justify your answer with a number.

## ★★★ Research-oriented

**★★★7.** Design a survey for a clay-rich agricultural soil that must report
volumetric water content to 5% relative at 1 m depth. Specify the methods, the
calibration measurements, the assumed constants with their sources, the metric,
and the falsification test. State explicitly which of the assumptions your design
cannot test.

**★★★8.** A third measurement — seismic $v_s$ — is added to the pair of the
lesson. Construct the sensitivity vector of each method with respect to
$(\theta, \phi)$ using plausible functional forms, and show whether the third
method reduces the residual degeneracy of Section 3.5. A qualitative answer
without the vectors is a failed answer.
