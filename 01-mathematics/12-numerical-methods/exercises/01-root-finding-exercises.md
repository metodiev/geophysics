# Exercises — 01-12-01 Root Finding: Bisection, Newton, Secant and Robust Hybrids

Attempt these **closed-book** before opening the
[solutions](./01-root-finding-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the order of convergence is defined by $|e_{k+1}|\le C|e_k|^p$; the
order estimator is $p\approx\log(e_{k+1}/e_k)/\log(e_k/e_{k-1})$; the Murnaghan
equation of state is $P(V)=\frac{K_0}{K_0'}\left[(V_0/V)^{K_0'}-1\right]$ with
$K_0=130$ GPa, $K_0'=4$, $V_0=1$ unless stated; GPa $=10^{9}$ Pa. State any
convention you add.

---

## ★ Foundational

**★1.** How many bisection steps reduce an initial bracket of width 2 to a width
below $10^{-6}$? And below the double-precision unit roundoff
$u = 2.2\times10^{-16}$?

---

**★2.** Derive the Newton iteration for $f(x)=x^2-c$ and show that it is the
Babylonian square-root algorithm. Give the error recursion and the order of
convergence.

---

**★3.** Apply one Newton step to $f(x)=x^3-2x+2$ from $x_0=0$, and then from the
resulting point. Show that the orbit is a 2-cycle, and give the true root of the
cubic.

---

**★4.** Using the Murnaghan equation of state with the stated constants, estimate
the volume at $P=5$ GPa by two bisection steps starting from the bracket
$[0.95,1.0]$. Report the bracket after each step and compare the final midpoint
with the closed-form value.

---

## ★★ Applied

**★★5.** Show that Newton's method at a root of multiplicity $m$ has the linear
constant $(m-1)/m$ and compute it for $m=2,3,4$. At what rate does the *residual*
fall in each case?

---

**★★6.** Derive the secant order equation $p^2=p+1$ from the recursion
$e_{k+1}=Ce_ke_{k-1}$, stating clearly where the assumption $e_k\ll1$ is used.

---

**★★7.** A four-station array with $v = 5.8$ km/s records arrivals of 1.85, 2.61,
2.81 and 2.15 s from stations at the corners of a 20 km square (in the order
$(0,0)$, $(20,0)$, $(20,20)$, $(0,20)$, in km). Set up the residual vector and its
Jacobian at the trial hypocentre $(5,5,0.0)$ and take one Newton step by hand
using the normal equations. State what the step does and what the residual norm
does.

---

**★★8.** The equation of state is replaced by a tabulated $P(V)$ available only
at 25 evenly spaced volumes. Describe how you would bracket the root of
$P(V)-P_{\text{target}}$, and what order you would expect from the secant method
applied to the table. What breaks first — the order, the convergence, or the
monotonicity of the bracket?

---

## ★★★ Research-oriented

**★★★9.** Design and run an experiment that measures the order of convergence of
a safeguarded hybrid on a function where Newton and bisection steps alternate for
many steps. Report the measured order, explain why it lies between 1 and 2, and
state how the answer depends on the function. Justify the bracket you use and
show the step-type sequence.

---

**★★★10.** A colleague reports a hypocentre located 40 km from every station of a
regional network, with a residual that "converged". Using only the structure of
the residual system, list the three most likely explanations, and give the
diagnostic that would distinguish them using data you already have. State which
of the three a bracketing safeguard would and would not repair.
