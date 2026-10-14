# Exercises — 06-12-03 Rate-and-State Friction and Dieterich Seismicity Model

Attempt these before reading the
[solutions](./03-rate-state-triggering-solutions.md). The lesson is
[03 Rate-and-State Friction and the Dieterich Seismicity Model](../03-rate-state-triggering.md);
all numbers are printed by
[`../code/rate_state_omori_demo.py`](../code/rate_state_omori_demo.py). All models
are **SYNTHETIC** teaching values; no real earthquake sequence or catalogue is
used.

## ★ Foundational

**★1.** For $r_0 = 1.00$ event/day, $\gamma = 20.0$ and $t_a = 30.0$ days, compute
$r(t)/r_0$ at $t = 1$, $10$ and $100$ days from
$r(t)/r_0 = \left[1 - (1 - \gamma^{-1})e^{-t/t_a}\right]^{-1}$, and compare with
the demonstration's values $12.324$, $3.132$ and $1.035$.

**★2.** Evaluate the same expression at $t \to 0^+$ and $t \to \infty$, and state
in one sentence why a stress *step* produces a transient rather than a new
elevated seismicity rate.

**★3.** Compute the Omori-equivalent corner time $c = t_a/(\gamma - 1)$ for the
model parameters, with units.

## ★★ Applied

**★★4.** Using the demonstration's table, compute the ratio $r(1\ \mathrm{d})/
r(10\ \mathrm{d}) = 12.324/3.132$ and compare it with $10^{p}$ for the fitted
$p = 0.4186$. Explain the difference in terms of the Omori approximation
$r \propto t^{-p}$ being valid only while $r/r_0 \gg 1$.

**★★5.** The demonstration fixes $c$ and refits $p$, obtaining $p = 0.4102$ at
$c = 0.05\ \mathrm{d}$, $0.4230$ at $c = 0.20\ \mathrm{d}$ and $0.5401$ at
$c = 10\ \mathrm{d}$, with $\Delta\log L$ from the best fit of $-0.14$, $0.00$ and
$-14.18$. Using the rule that a likelihood difference below about 2 is not a
constraint for one parameter, state the range of $c$ the catalogue actually
constrains, and say why $c$ is quoted with the widest uncertainty.

**★★6.** The demonstration reports that cutting the observation window from 365
days to 30 days changes the fit from $(K, c, p) = (9.144, 0.1336\ \mathrm{d},
0.4186)$ to $(47.455, 2.9076\ \mathrm{d}, 0.9967)$. Explain why a *shorter* window
pushes $p$ toward 1 and $c$ upward, and state what must therefore accompany any
published $(c,p)$ pair.

## ★★★ Research-oriented

**★★★7.** The demonstration's bootstrap gives a correlation between $\ln K$ and
$p$ of $+0.9997$. Design a bootstrap experiment that tests whether that
correlation is a property of the Omori-Utsu parameterisation or of the
observation window, stating the resampling scheme, the statistic, and the
predicted outcome under each hypothesis.

**★★★8.** Derive the Dieterich response
$r(t)/r_0 = \left[1 - (1-\gamma^{-1})e^{-t/t_a}\right]^{-1}$ from the
rate-and-state friction law with a state variable evolving toward steady state at
constant slip speed, stating each approximation. Then show that the small-step
limit gives $r/r_0 \approx 1 + (\gamma - 1)e^{-t/t_a}$ and explain why this is a
different functional form from Omori's law.

**★★★9.** The demonstration shows that discarding the first 20 days of a sequence
changes the fitted $p$ from $0.4186$ to $0.1447$. Design a detection model that
would make early-time incompleteness *separable* from the Omori parameters, state
what additional data it requires, and say what would falsify it.
