# Exercises — 15-01-03 Thermohaline Circulation and Deep Water Formation

Attempt these before reading the
[solutions](./03-thermohaline-circulation-solutions.md). The lesson is
[03 Thermohaline Circulation](../03-thermohaline-circulation.md). All models are
**SYNTHETIC** teaching values.

Model: $\dot T = C_T(T_a - T) - |q|T$,
$\dot S = F_S - |q|S$, $q = K_Q(\alpha T - \beta S)$, with
$C_T = 1/25\ \mathrm{yr^{-1}}$, $T_a = 25\ ^\circ$C,
$\alpha = 1.70\times10^{-4}\ {}^\circ\mathrm{C}^{-1}$,
$\beta = 7.60\times10^{-4}\ \mathrm{(g\,kg^{-1})^{-1}}$,
$K_Q = 30\ \mathrm{yr^{-1}}$. Use $\rho = 1025\ \mathrm{kg\,m^{-3}}$,
$c_p = 3994\ \mathrm{J\,kg^{-1}\,K^{-1}}$, $1\ \mathrm{Sv} = 10^{6}\
\mathrm{m^{3}\,s^{-1}}$, $1\ \mathrm{PW} = 10^{15}\ \mathrm{W}$,
$1\ \mathrm{yr} = 3.156\times10^{7}\ \mathrm{s}$.

## ★ Foundational

**★1.** At $F_S = 0.020\ \mathrm{(g\,kg^{-1})\,yr^{-1}}$ and a trial
$q = 0.030\ \mathrm{yr^{-1}}$, compute $T$, $S$ and $K_Q(\alpha T - \beta S)$.
State whether $q$ must increase or decrease to reach a steady state, and which of
the two steady states of the lesson it is nearer.

**★2.** State what each of the four terms in the model means physically, and name
which one is responsible for the existence of more than one equilibrium.

**★3.** Show that $S = F_S/|q|$ has units of $\mathrm{g\,kg^{-1}}$ given that
$F_S$ has units of $\mathrm{(g\,kg^{-1})\,yr^{-1}}$ and $q$ of
$\mathrm{yr^{-1}}$. Explain in one sentence why this expression diverges as
$q\to0$ and why that is not a numerical artefact.

## ★★ Applied

**★★4.** Derive $\operatorname{tr}J = -C_T - 3|q|$ from the Jacobian of the
lesson. (a) State what the result forbids. (b) Evaluate the trace at the two
steady states for $F_S = 0.020$ and check it against the printed eigenvalues
$(-0.09648, +0.04423)$ and $(-0.14071, -0.04423)$.

**★★5.** For $w = 2.0\ \mathrm{m\,yr^{-1}}$ and
$\kappa = 1.0\times10^{-4}\ \mathrm{m^{2}\,s^{-1}}$, compute $\delta = \kappa/w$
in metres. Then (a) state the depth at which $T$ has fallen to $1/e$ of the way
from $T_0$ to $T_d$; (b) compute the Péclet number $wH/\kappa$ for $H = 4000$ m;
(c) state what a Péclet number much greater than 1 implies about the balance.

**★★6.** Verify the fixed-point solution for $F_S = 0.010\
\mathrm{(g\,kg^{-1})\,yr^{-1}}$ by two iterations: start from $q_0 = 0.050$, use
$T = C_T T_a/(C_T+|q|)$ and $S = F_S/|q|$, compute a new $q$, and iterate. Report
the values after two iterations and say whether the iteration is converging
towards the strong or the weak branch.

**★★7.** Compute the ocean heat transport for $\Psi = 18\ \mathrm{Sv}$ and
$\Delta T = 12\ ^\circ$C, in W and PW. Then invert the calculation: what
$\Psi$ would give the same transport with $\Delta T = 18\ ^\circ$C?

## ★★★ Research-oriented

**★★★8.** Design a measurement that would distinguish the two stable states of
the two-box model. State (a) what you would measure, (b) over what duration,
(c) the size of the signal you must resolve, and (d) which of the two boxes'
assumptions your design does *not* test. A specification that could not be
executed is a failed answer.

**★★★9.** The lesson claims that the *existence* of a fold is robust to the
coefficients while the *threshold value* is not. Support or refute this by
re-solving the fold position for $K_Q = 15\ \mathrm{yr^{-1}}$ and for
$K_Q = 60\ \mathrm{yr^{-1}}$ (a hand estimate with two or three trials at each
value is sufficient), and state what the comparison shows.
