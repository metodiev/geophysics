# Exercises — 25-05-01 Project: Local Earthquake Tomography with Resolution Tests

Attempt these before reading the
[solutions](./01-tomography-project-solutions.md). The project is
[01 Tomography](../01-tomography-project.md); all numbers below are **SYNTHETIC**
and printed by [`code/tomography_demo.py`](../code/tomography_demo.py):

| Quantity | Value |
|---|---|
| grid | $10 \times 5$ cells of 3 km, 50 cells, $x \in [0,30]$, $z \in [0,15]$ km |
| background | $6.00$ km/s, $s_0 = 0.166667$ s/km |
| rays | 100 (10 sources $\times$ 10 receivers), 830 segments, 8.3 cells/ray |
| coverage | mean ray 19.14 km; per-cell path 5.9 to 74.4 km; no unlit cell |
| anomaly | peak $+5.0\%$ velocity, rms 1.237%, centred $x = 13.5$, $z = 7.5$ km |
| data | perturbation rms 36.16 ms, peak 62.28 ms; noise 5.0 ms; SNR 7.2 |
| damping table | $\alpha$: 0.001 $\to$ 20, residual 3.18 $\to$ 34.64 ms, model rms 9.979% $\to$ 0.062% |
| selected damping | $\alpha = 1.000$ (largest $\alpha$ with residual $\le$ 5.0 ms) |
| recovery | peak 3.46% of 5.00% (69%), model rms 1.037% of 1.237%, position exact |
| checkerboard | $r = 0.888$, amplitude 54.9% of input, best 3.66%, worst 0.04% |
| PSF | own-cell 62.3 / 63.5 / 63.3%, leak 68.0 / 72.7 / 67.4% at $z$ = 1.5 / 7.5 / 13.5 km |

## ★ Foundational

**★1.** Write the forward relation $t_i = t_i^{(0)} + \sum_j G_{ij} \delta s_j$ and
state the units of $G_{ij}$, $\delta s_j$ and $t_i$. Then compute the travel-time
perturbation for a ray that spends $10.0$ km inside a cell whose slowness is $5\%$
below the background, and the absolute travel time of a $19.14$ km ray in the
background medium.

**★2.** State the discrepancy principle as it is used in the project, and apply it
to the damping table: which $\alpha$ is selected, and what would be selected if the
noise level were 20 ms instead of 5 ms?

**★3.** Compute the signal-to-noise ratio of the synthetic dataset from the printed
numbers, and state the smallest velocity anomaly that this geometry and this noise
level could detect at the 36 ms signal level (assume the anomaly perturbs the
travel time in proportion to its amplitude).

## ★★ Applied

**★★4.** In the damping table, the residual changes from 3.18 ms ($\alpha = 0.001$)
to 4.49 ms ($\alpha = 1.000$), while the model rms changes from 9.979% to 1.037%.
Compute both the residual difference as a fraction of the noise level and the model
norm ratio, and explain in three sentences why the first number cannot be used to
choose between the two models.

**★★5.** The true anomaly has rms 1.237% and the recovered one 1.037%. Compute the
ratio, compare it with the peak amplitude recovery of 69%, and explain why the two
differ (what does the model rms measure that the peak does not?).

**★★6.** The checkerboard amplitude recovery is 54.9% while the smooth anomaly
recovery is 69%. Explain the difference in terms of spatial frequency and the
damping operator, and state the direction of the error: is the checkerboard a
conservative or an optimistic resolution test?

**★★7.** The PSF of a spike in one cell returns 63.5% of the input at the spike
cell, the row of the resolution matrix sums to about unity, and the absolute PSF
gain summed over the grid is 2.327. Compute the number of effective cells over which
the spike is spread, and state the resolution length you would quote for a cell of
3 km at that depth.

## ★★★ Research-oriented

**★★★8.** The dominant limitation of this project is the coupling between source
location and velocity: the hypocentres are unknowns, and a velocity error relocates
them, which then re-interprets the arrival times. Design an experiment or an
inversion scheme that breaks the coupling. Your answer must name the observations
or constraints used, state which of the two fields each one determines, give the
resolution you would claim for each, and specify the synthetic test that would show
the coupling is gone rather than merely hidden. An answer that assumes the
hypocentres are correct is a failed answer.
