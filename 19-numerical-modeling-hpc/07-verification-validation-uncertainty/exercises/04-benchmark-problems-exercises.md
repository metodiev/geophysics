# Exercises — 19-07-04 Standard Benchmark Problems and Community Comparisons

Attempt these before reading the
[solutions](./04-benchmark-problems-solutions.md). The lesson is
[04 Benchmark Problems](../04-benchmark-problems.md). All problems are
**SYNTHETIC** and defined here.

## ★ Foundational

**★1.** Apply the fourth-order stencil
$\big(-u_{i-2} + 16u_{i-1} - 30u_i + 16u_{i+1} - u_{i+2}\big)/(12h^{2})$ by hand to
$u = x^{4}$ at $x = 1$ with $h = 1$, and compare the result with the exact
$u''(1)$. Explain why the agreement is exact, and state what this implies about
the usefulness of such a test.

**★2.** A benchmark table reports RMS errors $1.20\times10^{-2}$,
$3.00\times10^{-3}$, $7.50\times10^{-4}$ for grids with $N$, $2N$, $4N$. Compute
the observed order and state whether the method is second or fourth order.

**★3.** Explain why the discrete error norm must carry an $h$ weight, and what a
comparison between two methods of different $N$ would show if the weight were
dropped.

## ★★ Applied

**★★4.** The periodic problem $-u'' = f$ on $[0,1)$ is posed with
$f(x) = 1 + \sin(2\pi x)$. Compute $\sum_i f_i$ and state why the discrete problem
has no periodic solution. Then state the two changes that make it well posed.

**★★5.** Two codes solve the periodic benchmark of Section 5.1 of the lesson and
differ by a constant $c = 0.5$. Compute the reported $L^{2}$ error of each code
against the stated exact solution, and state what the benchmark specification is
missing.

**★★6.** Write a complete benchmark specification for a 1-D steady diffusion
problem with a spatially varying coefficient that is piecewise constant, including
the interface condition, and state which discretisation choice a competing code is
most likely to make differently.

## ★★★ Research-oriented

**★★★7.** Design a benchmark that detects a code whose periodic boundary
implementation is correct to second order but whose interior stencil is fourth
order. State the observed order you expect, the grid sequence, and the diagnostic
that distinguishes this defect from a genuinely fourth-order code on a coarse grid.

**★★★8.** You are reviewing this comparison table. Identify every unstated
assumption that makes it unusable, and rewrite it in a form that would support the
conclusion "method B is preferable for this problem".

| method | resolution | error | run time |
|---|---|---|---|
| A: finite difference | 200 cells | $3\times10^{-3}$ | 1.2 s |
| B: spectral | 32$^{2}$ modes | $2\times10^{-4}$ | 1.1 s |
| C: finite difference | 400 cells | $4\times10^{-3}$ | 2.6 s |
