# Exercises — 19-03-01 Weak Formulation and the Galerkin Method

Attempt these before reading the
[solutions](./01-fem-weak-form-solutions.md). The lesson is
[01 Weak Formulation and the Galerkin Method](../01-fem-weak-form.md). All
models are **SYNTHETIC** teaching values; the demonstration
[`code/fem_weak_form_demo.py`](../code/fem_weak_form_demo.py) prints the numbers
that are quoted as measurements.

## ★ Foundational

**★1.** Integrate $-\int_0^1 u''(x)v(x)\,\mathrm{d}x$ by parts for
$v \in H^1_0(0,1)$ and state, with a reason, which boundary terms vanish. Repeat
for $v$ with $v(0) = 0$ but $v(1) \ne 0$, and say what the extra term is.

**★2.** For a P1 element of width $h$ on $[0,h]$, compute
$K_{00} = \int_0^h (\varphi_0')^2\,\mathrm{d}x$ and $M_{01} = \int_0^h\varphi_0
\varphi_1\,\mathrm{d}x$ directly from $\varphi_0 = 1-x/h$,
$\varphi_1 = x/h$ (units: $a$ dimensionless, so $K$ has units of 1/length and $M$
of length).

**★3.** A manufactured solution $u = \sin(\pi x)$ on $(0,1)$ with $u(0) = u(1) = 0$
satisfies $-u'' = f$. Compute $f$ and state the units of $f$ for $x$ in metres.

## ★★ Applied

**★★4.** Assemble the two-element P1 system for $-u'' = 1$, $u(0) = u(1) = 0$
with $h = 1/2$, solve it for the free nodal value $U_1$, and compare with the
exact solution $u(1/2) = 1/8$. Comment on the difference in one sentence.

**★★5.** The demonstration reports, for a $10{:}1$ coefficient contrast with the
interface on a face, an arithmetic-mean error of $7.264\times10^{-2}$ m at
$h = 0.125$ m and $1.188\times10^{-3}$ m at $h = 1.95\times10^{-3}$ m. Confirm
from these two numbers that the scheme is first order, and predict the error at
$h = 9.77\times10^{-4}$ m.

**★★6.** A colleague imposes $u(0) = 0$ and leaves $x = 1$ free, then reports
$u_h(1) = 3.99$ for the source $f = \pi^2\sin(\pi x)$. Show analytically what the
exact solution of that problem is and hence what the colleague should have
expected.

## ★★★ Research-oriented

**★★★7.** Derive the value of
$\left.\mathrm{d}H/\mathrm{d}k\right|_{\Delta t}$-type sensitivity for the
one-dimensional finite-element depth estimate: define
$E(h) = \|u - u_h\|_{L^2}$ for P1 elements on a uniform mesh, and show by
dimensional analysis and by the measured table of the lesson that
$E \approx Ch^2$ where $C$ depends on the fourth derivative of $u$. Estimate $C$
from the measured error at $h = 1/8$ and check it against the error at $h = 1/64$.

**★★★8.** Design a *verification* test that would detect a wrong sign in the
natural boundary term of the weak form (1.3), using only quantities the
demonstration already prints. State the two runs, the metric, the expected
outcome for the correct implementation, and the outcome you would expect for the
sign error. Your design must be executable as stated.
