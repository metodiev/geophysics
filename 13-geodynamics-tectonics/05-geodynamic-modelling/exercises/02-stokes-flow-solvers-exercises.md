# Exercises — 13-05-02 Solving the Stokes Equations for Mantle Flow

Attempt these before reading the
[solutions](./02-stokes-flow-solvers-solutions.md). The lesson is
[02 Solving the Stokes Equations for Mantle Flow](../02-stokes-flow-solvers.md)
and its numbers come from
[`code/stokes_flow_solvers_demo.py`](../code/stokes_flow_solvers_demo.py). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the Rayleigh number for $\rho_0 = 3200$ kg/m³,
$g = 9.81$ m/s², $\alpha = 3.0\times10^{-5}$ K$^{-1}$, $\Delta T = 2000$ K,
$d = 1.5\times10^{6}$ m, $\kappa = 1.0\times10^{-6}$ m²/s and
$\eta = 5.0\times10^{20}$ Pa s. State the units of every factor.

**★2.** Evaluate the linear growth rate
$\sigma(k,l) = -(k^2+l^2\pi^2) + Rak^2/(k^2+l^2\pi^2)^2$ for
$k = 2\pi$, $l = 1$, $Ra = 3000$ and state whether the mode grows.

**★3.** Compute $Ra_c(k,l) = (k^2+l^2\pi^2)^3/k^2$ for the same mode, and compare
with the value for the $(k=\pi,l=1)$ mode.

## ★★ Applied

**★★4.** Show that minimising $Ra_c(k,l)$ over $k$ at $l = 1$ gives
$k_c = \pi/\sqrt{2}$ and $Ra_c = 27\pi^4/4$. Explain in one sentence why the
unit-aspect box has a larger $Ra_c$ than the unbounded layer.

**★★5.** Use the measured Nusselt numbers at $N = 24$ and $N = 48$
($5.0799$, $4.9015$) with $h = 1/(N+1)$ to estimate $Nu(h\to0)$ assuming an
$O(h^2)$ error, and state the assumption you made.

**★★6.** At $Ra = 2000$, compute $\sigma$ for the modes $(\pi,1)$,
$(2\pi,1)$ and $(\pi,2)$, and rank them by how fast they grow or decay. Compare
with the measured values in the lesson.

**★★7.** A colleague's solver slows by a factor of 30 between a constant
viscosity and a viscosity of $10^{6}$. Design the diagnostic experiment that
decides whether the contrast or its sharpness is responsible, naming the quantity
measured and the expected outcome in each case.

## ★★★ Research-oriented

**★★★8.** The measured $Ra_c$ is 813.65 at $N=24$, 799.39 at $N=40$ and 791.69
at $N=64$, against the analytic 779.27. Fit $Ra_c(h) = Ra_c^0 + c\,h^p$ to the
three values (by trial values of $p$) and state whether a single power law
describes them.

**★★★9.** Design a numerical experiment to determine whether the Nusselt-number
exponent over $10^{4} \le Ra \le 10^{5}$ is closer to $1/3$ than the fitted
exponent of 0.380 measured over $3\times10^{3}$–$3\times10^{4}$. State the
resolution requirement and the quantity that must be shown to be
grid-independent.

**★★★10.** A model with temperature-dependent viscosity $\eta(T) =
\eta_0\exp[-\gamma(T-T_0)]$ reports $Nu$ at $\gamma = 10$. Specify the additional
diagnostics that must accompany that number for it to be interpretable, and
explain why $\gamma$ changes the effective Rayleigh number and the planform in
opposite directions.
