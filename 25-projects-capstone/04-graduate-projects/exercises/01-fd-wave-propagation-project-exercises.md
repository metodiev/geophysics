# Exercises — 25-04-01 Project: Finite-Difference Wave Propagation and Convergence Testing

Attempt these before reading the
[solutions](./01-fd-wave-propagation-project-solutions.md). The project is
[01 FD Wave Propagation](../01-fd-wave-propagation-project.md). Values printed by
[`code/fd_wave_demo.py`](../code/fd_wave_demo.py):

| Quantity | Value |
|---|---|
| problem | $u_{tt} = c^{2}u_{xx}$, $L = 1.0$ km, $c = 2.5$ km s⁻¹, $T = 0.800$ s |
| integration | $t = 0.55$ s $= 0.688$ periods, CFL $r = 0.5$ |
| errors, naive init | $9.776\times10^{-3}$, $5.018\times10^{-3}$, $2.537\times10^{-3}$, $1.276\times10^{-3}$ |
| orders, naive init | $0.96$, $0.98$, $0.99$ |
| errors, exact init | $3.480\times10^{-4}$, $8.692\times10^{-5}$, $2.174\times10^{-5}$, $5.438\times10^{-6}$ |
| orders, exact init | $2.00$, $2.00$, $2.00$ |
| ppw = 40, 80, 160, 320, 640 | errors $2.161\times10^{-3} \to 8.496\times10^{-6}$ |
| CFL sweep | $0.25 \to 0.37921$; $1.00 \to 0.35352$; $1.01 \to 3.0767$; $1.10 \to 1.1542\times10^{32}$ |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Write the explicit update, define $r$, and state the leading truncation
term. State the value of $r$ at which that term vanishes and the value at which
the scheme becomes unstable.

**★2.** The resolution table gives rms errors $2.161\times10^{-3}$ at 40 points per
wavelength and $5.421\times10^{-4}$ at 80. Fit the order of convergence from that
single pair, and state how many grid pairs are needed for a defensible order.

**★3.** The von Neumann amplification factor satisfies
$|g|^{2} = 1 - r^{2}\sin^{2}\theta$. Derive the stability condition on $r$ and
state the worst-case $\theta$.

## ★★ Applied

**★★4.** Using the exact-initialisation errors at $N = 100, 200, 400$
($8.692\times10^{-5}$, $2.174\times10^{-5}$, $5.438\times10^{-6}$), fit the order
from each successive pair, report the mean, and extrapolate the error at
$N = 800$. State the assumption the extrapolation rests on.

**★★5.** Show that starting the leapfrog with $u^{-1} = u^{0}$ implies an initial
velocity with an error of order $\Delta t$, and use that to explain why the fitted
order falls to $\approx 1$ while the scheme's truncation error remains
$\mathcal O(\Delta x^{2})$.

**★★6.** In the CFL sweep at $N = 100$, the final amplitude is $0.35352$ at
$r = 1.00$ and $3.0767$ at $r = 1.01$. Compute the growth factor over the run and
the per-step growth rate, and state why a per-step rate of this size is dangerous
in a production run of $10^{4}$ steps.

## ★★★ Research-oriented

**★★★7.** Design a verification suite for a heterogeneous, elastic, 2-D
finite-difference code with a free surface and an absorbing boundary, specifying:
the manufactured solutions you would use and what each tests, the quantities you
would fit orders from, how you would separate the boundary error from the interior
error, and the tolerance you would demand before calling the code verified. State
which of your tests could pass while the code is still wrong. That last item is the
point of the exercise.
