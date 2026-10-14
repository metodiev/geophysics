# Exercises — 03-12-02 Numerical Stability, CFL Conditions and Convergence Testing

Attempt these **closed-book** before opening the
[solutions](./02-stability-and-cfl-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first:

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/stability_and_cfl_demo.py
```

---

## ★ Foundational

**★1.** Perform the von Neumann analysis of the explicit wave scheme: insert
$u_i^n = G^n\mathrm{e}^{\mathrm{i}ki\Delta x}$, divide through, and derive
$G^2 - 2aG + 1 = 0$ with $a = 1 - 2r^2\sin^2(k\Delta x/2)$.

**★2.** State the stability limit of (a) the explicit wave scheme, (b) explicit
FTCS diffusion, (c) backward Euler diffusion. Give the measured growth-rate
agreement for each in the unstable regime (or state that there is none).

**★3.** Show that $r = \kappa\Delta t/\Delta x^2$ is dimensionless, and state the
limits $r \le 1$ and $r \le 1/2$ in words for a physical grid.

**★4.** The flipped-sign wave scheme grows by 2.618034 per step at $r = 0.5$.
Derive the quadratic it solves and show that the largest root is
$(3+\sqrt5)/2$.

**★5.** At $k\Delta x = \pi$, write $a$ in terms of $r$ for the wave scheme, and
state the value of $r$ at which $\lvert a\rvert$ first exceeds 1.

---

## ★★ Applied

**★★6.** Compute the predicted growth per step at $r = 1.05$ from
$\lvert G\rvert = (2r^2-1)+\sqrt{(2r^2-1)^2-1}$ and compare with the measured
1.877328. Then compute the amplitude after 30 steps from an initial amplitude
of 1 and state whether it overflows a `float64`.

**★★7.** Explain why $r = 1$ appears as "bounded" in the wave table while the
maximum amplitude at 300 steps is 601. Name the property of the amplification
matrix responsible and state the linear growth law.

**★★8.** A simulation uses $c_{\max} = 6$ km/s, $\Delta x = 100$ m and
$\Delta t = 0.02$ s. Compute $r$, state whether it is stable, and compute the
time step that a CFL of 0.9 would require.

**★★9.** For explicit diffusion, explain why $r = 1/2$ is marginally stable
rather than stable, using the value of $G$ at $k\Delta x = \pi$ and the measured
growth of exactly 1.000000.

**★★10.** Solve the wave-scheme quadratic at $r = 0.9$ and $k\Delta x = \pi$ and
show $\lvert G\rvert = 1$. Then explain the measured maximum amplitude of 2.3 at
300 steps for the same parameters.

---

## ★★★ Research-oriented

**★★★11.** Derive the Lax–Wendroff advection stability condition by von Neumann
analysis, then measure the growth rate in the unstable regime at $\nu = 1.05$
and $\nu = 1.2$ and compare with the prediction.

**★★★12.** Measure the growth rate of a staggered-grid acoustic scheme beyond
its CFL limit and compare with the prediction. State whether the diagnostic is as
sharp there as on a collocated grid, and why.

**★★★13.** Construct a scheme with a double root on the unit circle at $r = 1$ at
a wavenumber other than $\pi$. Report the wavenumbers and the growth behaviour,
and state what this implies for the practical advice "use $r \le 0.9$".
