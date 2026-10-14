# Exercises — 08-04-03 MT Processing: Robust Estimation, Remote Reference, Tipper

Attempt these before reading the
[solutions](./03-mt-processing-solutions.md). The lesson is
[03 MT Processing](../03-mt-processing.md). All models are **SYNTHETIC** and the
noise is generated.

## ★ Foundational

**★1.** A station has magnetic-noise power ratio $\eta_H = 0.25$. Compute the
factor by which the single-station estimate of $\rho_a$ is biased, and the
corrected value if the estimate was $100\ \Omega$m.

**★2.** A station has $\eta_H = 0.5$ and a single-station $\rho_a = 40\ \Omega$m.
Compute the corrected value.

**★3.** State the remote-reference estimator and the two properties of the remote
channel that make it unbiased.

## ★★ Applied

**★★4.** With 20% coherent spikes in $E$, the least-squares mean $\rho_a$ is
109.625 $\Omega$m and the Huber mean is 100.515 $\Omega$m, against a baseline of
100.18 $\Omega$m. Compute the bias of each and state what the robust estimator
recovered.

**★★5.** With a local artificial source, the least-squares median is
51.678 $\Omega$m, the Huber median 51.174 $\Omega$m and the remote-reference
median 100.062 $\Omega$m, against a true 100 $\Omega$m. Compute the errors and
explain in one sentence why robustness fails here.

**★★6.** In the electric-noise table, at $\eta_E = 4$ the mean of $\rho_a$ is
101.525 $\Omega$m and the median is 101.156 $\Omega$m while the scatter (standard
deviation) is 18.108 $\Omega$m. Explain why the mean is not biased by 18% when the
scatter is 18%.

## ★★★ Research-oriented

**★★★7.** Design a processing experiment to determine the smallest remote-site
noise ratio $\eta_R$ for which the remote-reference estimator still removes the
$\eta_H = 1$ bias to within 5%. State the metric, the sample sizes, and the
expected behaviour of the answer as the segment count grows.

**★★★8.** A colleague reports $\rho_a = 45\ \Omega$m from a single-station
estimate with no statement of the noise. List the four items you would require,
and for each say what it would change about your interpretation of the number.
