# Exercises — 19-04-01 Spectral Methods: Basis Choice and Exponential Convergence

Attempt these before reading the
[solutions](./01-spectral-methods-solutions.md). The lesson is
[01 Spectral Methods: Basis Choice and Exponential Convergence](../01-spectral-methods.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For $u(x) = e^{\mathrm{i}2\pi m x}$ sampled on $N = 64$ points over one
period, state the exact Fourier derivative and the largest $m$ for which the
derivative is exact.

**★2.** State the error model for exponential (spectral) convergence and for
$p$-th order convergence, and identify which is a power law and which is not.

**★3.** State the two quantities whose product sets the round-off floor of a
spectral derivative, and say what happens to a convergence table that continues
past that floor.

## ★★ Applied

**★★4.** The measured second-order finite-difference constant for
$e^{\sin(2\pi x)}$ is $\text{error}_2 \approx 167.6/N^2$ and the fourth-order one
is $\text{error}_4 \approx 8.00\times10^{3}/N^4$. Compute the $N$ needed by each
to reach a relative derivative error of $10^{-10}$, and compare with the
19 modes the spectral method needed for $10^{-6}$.

**★★5.** The kinked function $|\sin(\pi x)|$ has Fourier coefficients decaying
like $k^{-2}$. Using $\|u' - u'_N\|_{L^2}^2 \sim \sum_{k>N}k^{-2}$, predict the
rms convergence order of the derivative and compare with the measured sequence
0.401, 0.452, 0.476, 0.488, 0.494.

**★★6.** A colleague reports a maximum derivative error of $1.21$ rad/m for a
periodic function with a kink, and refines from 16 to 512 points with no
improvement. State what is wrong with their conclusion that "the code is
converging to the wrong answer", and state the norm they should have used.

## ★★★ Research-oriented

**★★★7.** Design an experiment that distinguishes "the function has a kink" from
"the grid is too coarse" as the cause of a stagnating maximum error. State the
two runs, the metric, and the predicted outcome for each cause.

**★★★8.** A global field has a spectrum known to decay like $\rho^{-m}$ with
$\rho = 2$. Derive the number of modes needed for a relative error of $10^{-8}$,
compute the corresponding grid size for a real function, and state how the answer
changes if the target is $10^{-12}$.
