# Exercises — 19-05-02 Boundary Element Methods for Potential Fields

Attempt these before reading the
[solutions](./02-boundary-element-solutions.md). The lesson is
[02 Boundary Element Methods for Potential Fields](../02-boundary-element.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For a circular boundary of radius $a = 10$ km discretised into $N = 32$
constant panels, compute the chord length
$L = 2a\sin(\pi/N)$ and then
$G_{ii} = -\frac{1}{2\pi}L\left(\ln(L/2)-1\right)$.

**★2.** State why $H_{ii} = 0$ for a straight constant panel, in one sentence and
one equation.

**★3.** The demonstration's exterior test reports a relative flux error of
$2.0082$ with the interior free term and $6.8589\times10^{-3}$ with the exterior
one. Explain why the first number is almost exactly $2$.

## ★★ Applied

**★★4.** From the row-sum table ($N = 64$: deviation $7.813\times10^{-3}$;
$N = 256$: $1.953\times10^{-3}$), determine the order of the deviation and
estimate the deviation at $N = 1024$.

**★★5.** The row-sum diagonal correction improves the flux error from
$8.776359\times10^{-3}$ ($N = 128$) to $9.587218\times10^{-4}$. Compute the
improvement factor and estimate the order of the corrected error using the
$N = 64$ and $N = 128$ rows of the same column.

**★★6.** For the volume-grid comparison at $n = 128$: $16\,384$ unknowns,
$79\,888$ nonzeros, error $6.7720\times10^{-7}$. For the boundary method at
$N = 128$: $128$ unknowns, error $5.9824\times10^{-4}$. State which route you
would choose for a 2-D interior problem and which for a 3-D exterior problem, and
give the ratio that decides each.

## ★★★ Research-oriented

**★★★7.** The measured flux order is about $1.1$ and the field order about
$0.97$. Design a refinement study that decides whether the limiting factor is the
flat-panel geometry or the quadrature on the panels, and state the observable.

**★★★8.** The truncation table gives errors $1.2500\times10^{-1}$,
$1.5625\times10^{-2}$, $1.0000\times10^{-3}$ and $1.0000\times10^{-6}$ for
$R/a = 2, 4, 10, 100$. Verify the exponent and state, for the same target
accuracy as the boundary method's $1.733\times10^{-4}$, what $R/a$ a volume solve
would need.
