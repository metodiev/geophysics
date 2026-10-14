# Exercises — 19-02-04 Explicit vs Implicit Time Stepping and Stability Limits

Attempt these before reading the
[solutions](./04-fd-time-stepping-solutions.md). The lesson is
[04 Time Stepping](../04-fd-time-stepping.md). All models are **SYNTHETIC**.
Numbers printed by `../code/fd_time_stepping_demo.py` may be quoted directly.

## ★ Foundational

**★1.** Write the FTCS update for $u_t = \alpha u_{xx}$, define $r$, and state
the stability limit and the growth factor of the highest mode at $r = 0.5$.

**★2.** State the order of accuracy in time of forward Euler, backward Euler and
Crank–Nicolson for the diffusion equation.

**★3.** Write the leapfrog update for $u_{tt} = c^{2}u_{xx}$, define $C$, and
state the CFL limit.

## ★★ Applied

**★★4.** A 2-D diffusion problem has $\alpha = 2\times10^{-7}\
\mathrm{m^{2}\,s^{-1}}$ and $h = 100$ m. Compute the explicit step limit and the
number of steps to reach $t = 10^{7}$ s. Then state whether the limit or the
physical timescale binds.

**★★5.** A wave run at $C = 1.08$ shows exponential growth. Predict the growth
per step at the Nyquist mode and the number of steps for the amplitude to exceed
$10^{6}$ times its initial value.

**★★6.** The trapezoidal scheme gives an amplitude ratio of $0.99992$ after 1000
steps at $C = 10$ and an $L^{2}$ error of $2.03\times10^{-1}$ against the exact
solution. Explain how both statements can be true and what each measures.

## ★★★ Research-oriented

**★★★7.** A production thermal code currently uses explicit FTCS on a
$400\times400$ grid with $h = 25$ m and $\alpha_{\max} = 10^{-6}\
\mathrm{m^{2}\,s^{-1}}$. Propose a change that reduces the run time by at least
a factor of ten without changing the grid, quantify the change, and state the two
risks the change introduces and how you would test for each.

**★★★8.** Lax equivalence requires stability *and* consistency. Construct a
scenario in which an unconditionally stable implicit scheme produces a visible
artefact at large $dt$ that refinement of $h$ cannot remove, explain the
mechanism, and specify the measurement that distinguishes it from a physical
effect.
