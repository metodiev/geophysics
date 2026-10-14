# Exercises — 19-05-01 Volume and Surface Integral Equations

Attempt these before reading the
[solutions](./01-integral-equations-solutions.md). The lesson is
[01 Volume and Surface Integral Equations](../01-integral-equations.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A uniform 2-D body has area $A = 72.0\ \mathrm{km^{2}}$ and density
$\rho = 2600\ \mathrm{kg\,m^{-3}}$. Compute $2G\rho A$ with
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and state its units.

**★2.** Using the printed monopole estimate $2G\rho A/R$ for $R = 30$ km, and the
printed boundary-quadrature value $g_{x} = 8.413406\times10^{-4}\ \mathrm{m\,s^{-2}}$,
compute the ratio and state what the $1\%$ residual represents.

**★3.** State the units of the area-quadrature error in the table of Section 3.2
and explain why a *potential* error and a *field* error cannot be compared
directly.

## ★★ Applied

**★★4.** Use three successive rows of the midpoint table
($n = 48, 96, 192$) to estimate the constant $C$ in the error law
$E = Ch^{2}$, where $h = 12\,000/n$ m is the cell width. Report $C$ in
$\mathrm{m^{4}\,s^{-2}}$.

**★★5.** The first-kind table reports $\mathrm{cond}(A) = 6.542\times10^{16}$ at
$n = 32$ and $2.510\times10^{19}$ at $n = 64$. Estimate the condition number at
$n = 128$ by log-linear extrapolation and state why the estimate is an
over-estimate.

**★★6.** For the second-kind problem the contraction factor is $0.8000$ and the
measured Neumann iteration count to a $10^{-12}$ residual is $106$ against
$\ln(10^{-12})/\ln(0.8) = 124$ predicted. Explain the direction of the
discrepancy.

## ★★★ Research-oriented

**★★★7.** The Poisson check reports the inside ratio $1.00004$ at $h = 100$ m and
$1.00060$ at $h = 400$ m, with an observed order of $2.00$. Design a refinement
study that separates the truncation error of the difference operator from the
quadrature error of the representation, and state the observable that
distinguishes them.

**★★★8.** The far-field residual $|R g_{R} - 2G\rho A|$ falls with a fitted slope
of $-2.003$. Predict the residual at $R = 480$ km from the printed values at
$120$ and $240$ km, and state the assumption that makes the prediction valid.
