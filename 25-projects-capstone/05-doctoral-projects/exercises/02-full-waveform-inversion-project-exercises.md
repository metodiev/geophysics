# Exercises — 25-05-02 Project: A Small-Scale Full-Waveform Inversion

Attempt these before reading the
[solutions](./02-full-waveform-inversion-project-solutions.md). The project is
[02 Full-Waveform Inversion](../02-full-waveform-inversion-project.md); all numbers
below are **SYNTHETIC** and printed by
[`code/full_waveform_inversion_demo.py`](../code/full_waveform_inversion_demo.py):

| Quantity | Value |
|---|---|
| grid and time step | $\Delta z = 10$ m, 100 cells (1.00 km), $\Delta t = 1$ ms, 700 steps (0.70 s) |
| CFL number | $c_{\max}\Delta t/\Delta z = 0.21$ |
| source | 12 Hz Ricker, receiver co-located at 10 m depth |
| wavelength | 175 m at 2100 m/s = 17.5 cells; resolution limit $\approx 88$ m |
| true model | 1800 / 2000 / 1700 / 2100 m/s at 0–200 / 200–400 / 400–600 / 600–1000 m |
| data | peak 3.086, rms 0.585; noise 0.0309 (1% of peak); SNR 18.9 |
| two-way times | 0.222 s (200 m), 0.422 s (400 m), 0.658 s (600 m) |
| adjoint test | $\lVert g\rVert$ both $8.3310\times10^{7}$; cosine $1.0000000000$; ratio $1.0000009$ |
| true-model misfit | $J = 0.3301$, rms 0.0307 against noise 0.0309 |
| start 1900 | $2.6834 \to 0.3228$, rms 0.0303, 121 iterations, recovered 1798 / 1995 / 1682 / 1898 |
| start 1650 | $5.8857 \to 0.8048$, rms 0.0479, 122 iterations, recovered 1798 / 1606 / 1288 / 1650 |
| start 2300 | $20.0516 \to 0.6067$, rms 0.0416, 400 iterations, recovered 1800 / 2459 / 2350 / 2304 |
| parameters / data | 20 / 701 |

## ★ Foundational

**★1.** Write the discrete forward update. Then show that the coefficient
$A_j = \Delta t^2/(m_j\Delta z^2)$ equals the square of the CFL number at cell $j$,
and evaluate $A_j$, $m_j$ and the gradient factor $-A_j/m_j$ for
$c_j = 1900\ \mathrm{m\,s^{-1}}$, $\Delta z = 10$ m, $\Delta t = 1$ ms.

**★2.** State the finite-difference gradient test, and state two things it does
*not* verify. Give the stability limit on $\Delta t$ for this grid and this maximum
velocity, and compare it with the $\Delta t$ actually used.

**★3.** Compute the dominant period of the 12 Hz source and the half-period limit
$T/2$. Then compute the two-way time to the 400 m reflector for constant starting
models of 1900, 1750, 1700 and 2300 m/s, and decide which of them satisfy the
criterion.

## ★★ Applied

**★★4.** The successful inversion reaches $J = 0.3228$ while the true model gives
$J = 0.3301$; the noise variance is $\sigma^2 = 0.0309^2$. Using $\chi^2$ counting
for $N = 701$ data and $p = 20$ parameters, compute the expected misfit of the true
model and of the best-fitting model, compare both with the observed values, and state
whether the difference between the two is evidence of overfitting.

**★★5.** The deepest layer is recovered as 1898 m/s against a true 2100 m/s.
Compute the relative error. Compute how much of a 12 Hz Ricker wavelet (whose
half-width is about $T/2$) falls inside the 0.70 s record for the 600 m reflector at
0.658 s, and explain the connection.

**★★6.** The resolution limit is about half the dominant wavelength. Compute it in
metres and express it in terms of the 50 m layer thickness used in the inversion
parameterisation. What does the answer say about using 20 parameters of 50 m for
this dataset?

**★★7.** For the 2300 m/s starting model the largest travel-time error is 136 ms at
the 600 m reflector. Compute the highest frequency at which the half-period
criterion would still be satisfied, and compare it with the 12 Hz of the data.

## ★★★ Research-oriented

**★★★8.** Design a multiscale full-waveform inversion workflow for this dataset that
would make the 2300 m/s starting model converge. Your answer must state: the
frequency schedule and the criterion that fixes it, how the starting model is
obtained and why that removes the long-wavelength error, what objective function is
used at each stage, the resolution you claim from each stage, and at least three
tests that would demonstrate the multiscale run reached the global rather than a
different local minimum. An answer that only lists lower frequencies without the
per-frequency criterion and the starting-model construction is incomplete.
