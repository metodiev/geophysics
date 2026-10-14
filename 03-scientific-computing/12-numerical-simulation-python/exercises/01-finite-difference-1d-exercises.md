# Exercises — 03-12-01 A 1-D Finite-Difference Solver from Scratch

Attempt these **closed-book** before opening the
[solutions](./01-finite-difference-1d-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first:

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/finite_difference_1d_demo.py
```

---

## ★ Foundational

**★1.** Derive $u''(x) = (u_{i+1} - 2u_i + u_{i-1})/\Delta x^2 + O(\Delta x^2)$
by adding the Taylor expansions at $x\pm\Delta x$. State the leading error term
and its coefficient.

**★2.** Show that $r = c\Delta t/\Delta x$ is dimensionless, verify the same for
$r^2(u_{i+1}-2u_i+u_{i-1})$, and state the value of $r$ used in the
demonstration.

**★3.** Write the consistent first step for a standing mode with $u_t = 0$ at
$t = 0$. State what is wrong with using $u^{-1} = 0$.

**★4.** Give the measured order of convergence for (a) the travelling-wave test
and (b) the standing-mode test read at $t = 1.0$ s. State which is the scheme's
true order and why the other is larger.

**★5.** State the discrete energy that the leapfrog scheme conserves, and give
the measured relative drift over 2000 steps.

---

## ★★ Applied

**★★6.** Derive the apparent order 4 of the standing-mode test: show that the
leading error is a phase error of order $\Delta x^2$ and that the amplitude
error at a phase extremum is of order $\delta\phi^2$.

**★★7.** Reconcile these two measured statements: at $r = 1$ the travelling
wave has error $3.1\times10^{-15}$; at $r = 1$ the $2\Delta x$ standing mode
grows as $2n-1$. State which initial condition produces the growth and why it
is a measure-zero case.

**★★8.** From the dispersion table, interpolate the phase-speed deficit at
5 points per wavelength and state the practical resolution rule that follows.

**★★9.** Recompute the energy using the gradient at a single time level and
report the apparent damping you measure. Explain why the naive definition
appears to show damping that the scheme does not have.

**★★10.** The error in the refinement table stops falling at
$\Delta x \approx 8\times10^{-5}$ and then rises. Explain the rise, state the
scaling you expect, and check it against the measured values.

---

## ★★★ Research-oriented

**★★★11.** Push the travelling-wave convergence test to 8, 16 and 32 points per
wavelength and measure the phase speed with the Fourier-phase estimator. Report
the contamination from the counter-propagating root as a function of $k\Delta x$
and state whether the estimator is usable above $k\Delta x = 1$.

**★★★12.** Replace the centred second difference with the fourth-order
five-point stencil and repeat the convergence study. Report the measured order,
the stability limit (it is not 1), and the points per wavelength at which the
two schemes give the same error.

**★★★13.** Choose a geophysical target — say a 1 Hz surface wave crossing a
100 km basin — and specify the grid spacing, time step, number of cells and
number of steps from the $\lambda$-per-wavelength rule and the CFL condition.
State every assumption and compute the resulting memory and operation counts.
