# Exercises — 19-03-04 Finite Volume Methods and Conservative Discretisation

Attempt these before reading the
[solutions](./04-finite-volume-solutions.md). The lesson is
[04 Finite Volume Methods and Conservative Discretisation](../04-finite-volume.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the cell update (1.3) for cell $i$ and show by summing over a
periodic domain that $\sum_i u_i\Delta x_i$ is unchanged. State in one sentence
which single design decision makes the proof work.

**★2.** For $a = 2$ m/s, $\Delta x = 0.02$ m and CFL 0.6, compute the timestep,
the numerical diffusion coefficient $D_{\rm num} = a\Delta x(1-C)/2$, and the
diffusion length $\sqrt{2D_{\rm num}t}$ after $t = 0.5$ s.

**★3.** State the three faces of a cell in a one-dimensional periodic mesh and
say how many of them are shared with another cell.

## ★★ Applied

**★★4.** With cell values $u_{i-1} = 1.0$, $u_i = 0.7$, $u_{i+1} = 0.2$ and
$a = 1$ m/s, $\Delta x = 0.01$ m, CFL 0.7, compute one upwind step for cells
$i$ and $i+1$ and verify that the change over the two cells equals the net
boundary flux.

**★★5.** The demonstration reports measured $2D_{\rm num}$ values of
$0.00199987$, $0.00099986$ and $0.00049986$ m²/s at $\Delta x = 0.01,\ 0.005,
0.0025$ m with CFL 0.8. Confirm the first-order scaling and predict the value at
$\Delta x = 0.00125$ m.

**★★6.** Lax–Wendroff overshoots a jump to $\max u = 1.174417$ while upwind
stays at $0.999995$. State the theorem that forbids a linear scheme from being
both second-order and monotone, and give the measured total-variation numbers for
each scheme.

## ★★★ Research-oriented

**★★★7.** Derive the harmonic face transmissibility $2a_La_R/(a_L+a_R)$ by
writing the series resistance of two half-cells of width $\Delta x/2$, and
verify that it reduces to $a$ when $a_L = a_R = a$. Then compute the arithmetic
mean and both ratios for $a_R/a_L = 1000$.

**★★★8.** Design a numerical experiment that decides whether the first-order
error of the upwind scheme on a *graded* mesh is dominated by the numerical
diffusion of Section 2 or by the face-coefficient error of Section 4. State the
two configurations, the metric, and the predicted outcome for each.
