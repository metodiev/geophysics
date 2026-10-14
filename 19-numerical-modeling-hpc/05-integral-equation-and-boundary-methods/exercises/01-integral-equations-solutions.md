# Solutions — 19-05-01 Volume and Surface Integral Equations

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs, not estimated by hand. All models are **SYNTHETIC**.

Lesson: [01 Volume and Surface Integral Equations](../01-integral-equations.md).

---

## ★1 — Monopole strength

$$2G\rho A = 2(6.67430\times10^{-11})(2600)(7.2\times10^{7}) = 2.498858\times10^{1}.$$

Units: $\mathrm{m^{3}\,kg^{-1}\,s^{-2}} \cdot \mathrm{kg\,m^{-3}}\cdot
\mathrm{m^{2}} = \mathrm{m^{2}\,s^{-2}}$ — a potential, consistent with
$\Phi = 2G\rho\int\ln\cdot\,\mathrm{d}A$ because the logarithm is dimensionless.

---

## ★2 — Far-field ratio

$$\frac{g_{x}}{2G\rho A/R} = \frac{8.413406\times10^{-4}}{8.329526\times10^{-4}}
= 1.010070 .$$

The $1.007\%$ residual is the non-monopole part of the body's field — the
quadrupole and higher moments of a $12\ \mathrm{km}\times6\ \mathrm{km}$ rectangle
seen from $30$ km. It is structure, not error: the same code refined does not
change it, and the residual's $R^{-2}$ decay measures its multipole order.

---

## ★3 — Units

The area-quadrature table's error is in $\mathrm{m^{2}\,s^{-2}}$: the quantity
being refined is $\Phi$, a potential. A field error is
$(\text{potential error})/\mathrm{m}$, i.e. $\mathrm{m\,s^{-2}}$. Since an error
of $10^{-5}\ \mathrm{m^{2}\,s^{-2}}$ corresponds to about
$10^{-9}\ \mathrm{m\,s^{-2}}$ when divided by a $10$ km scale, quoting the two
interchangeably understates or overstates the accuracy by three orders of
magnitude.

---

## ★4 — The constant in the error law

Cell widths: $h = 12\,000/n$ m, so $h_{48} = 250$ m, $h_{96} = 125$ m,
$h_{192} = 62.5$ m.

Using $E_{96} = 6.753538\times10^{-5}$ and $h_{96} = 125$:

$$C = \frac{E}{h^{2}} = \frac{6.753538\times10^{-5}}{125^{2}}
= 4.32\times10^{-9}\ \mathrm{m^{4}\,s^{-2}} .$$

Check with $n = 192$: $E/h^{2} = 1.688386\times10^{-5}/62.5^{2}
= 4.32\times10^{-9}$ ✔, and with $n = 48$:
$2.701405\times10^{-4}/250^{2} = 4.32\times10^{-9}$ ✔. The constant is stable, so
the error law is a single power over this range — which is exactly the assumption
Richardson extrapolation makes, and the reason the two extrapolations agreed to
$2.04\times10^{-11}$.

---

## ★5 — Extrapolating a condition number

Log-linear fit through $(n,\log_{10}\mathrm{cond})$ at $n = 32$
($16.82$) and $n = 64$ ($19.40$): slope
$(19.40 - 16.82)/\log_{2}(64/32) = 2.58$ decades per doubling. At $n = 128$ the
extrapolation gives $10^{21.98} \approx 9.5\times10^{21}$.

This is an **over-estimate of the difficulty and an under-estimate of the true
condition number's futility**, because double precision cannot represent a matrix
whose condition number exceeds $1/\epsilon \approx 4.5\times10^{15}$ in a
meaningful way: measured $\mathrm{cond}$ is already pinned at
$2.545\times10^{19}$ at $n = 128$, and the growth stops. The extrapolation
describes the *continuous* operator; the discretisation saturates at the
roundoff floor, where the computed singular values are noise.

---

## ★6 — Neumann iterations: $106$ against $124$

The prediction $\ln(10^{-12})/\ln(0.8) = 124$ assumes the error falls by the
contraction factor in a *norm* at every iteration. The measured $106$ is a
*pointwise* criterion on an already-converged iterate whose error is
concentrated where the solution is large; the residual drops below the tolerance
before the worst-case norm bound needs the extra $18$ iterations.

The direction of the gap is the informative part: a normwise bound is a
worst-case envelope, and a measured pointwise count will usually beat it. A count
*larger* than the bound would indicate a bug, since the bound is a contraction
guarantee.

---

## ★7 — Separating difference error from quadrature error

Two candidate explanations for the Poisson-check residual, and the observable
that separates them:

- **Difference-operator truncation error** scales as $h^{2}$ for fixed
  quadrature resolution. Observable: halve $h$ at fixed $n$, and the residual
  falls by $4$.
- **Representation/quadrature error** is fixed once $n$ is fixed (it does not
  depend on the difference step). Observable: refine $n$ at fixed $h$ and the
  residual falls until it hits the difference-error floor.

The experiment: a $2\times2$ grid of runs over $(h, n)$. If the residual depends
only on $h$, it is the difference; if it depends on $n$ and flattens once
$n$ is large, it is the quadrature; if the two effects are comparable, the
residual shows a minimum where the two curves cross. The measured $4\times$
reduction per halving of $h$ (order $2.00$) identifies the difference operator,
because the quadrature resolution was held fixed throughout.

---

## ★8 — Predicting the residual at $480$ km

With $E \propto R^{-2.003}$ and $E(240) = 3.904913\times10^{-3}$:

$$E(480) = 3.904913\times10^{-3}\left(\frac{240}{480}\right)^{2.003}
= 9.74\times10^{-4}\ \mathrm{m^{2}\,s^{-2}} .$$

For reference, $3.904913\times10^{-3}/4 = 9.76\times10^{-4}$; the $2.003$ exponent
moves the answer by $0.2\%$.

**Assumption:** the asymptotic regime has been reached, i.e. the next term in the
multipole expansion dominates the residual at both radii. The fitted $2.003$
versus the integer $2$ is the evidence for that, and the residual at $30$ km
being $2.5\times10^{-1}$ (not four times the $60$ km value) is evidence that the
asymptotic regime starts somewhere between $30$ and $60$ km.
