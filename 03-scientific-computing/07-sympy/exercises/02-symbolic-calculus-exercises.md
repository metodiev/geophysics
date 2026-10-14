# Exercises — 03-07-02 Symbolic Differentiation, Integration and Limits

> Solutions are in
> [`02-symbolic-calculus-solutions.md`](./02-symbolic-calculus-solutions.md).

---

## ★ Foundational

**★1.** Differentiate with respect to $x$: (a) $3x^4 - 2x$,
(b) $\sin(kx)e^{-ax}$, (c) $\ln(x^2+a^2)$, (d) $\mathrm{erf}(x/2)$.

**★2.** Evaluate: (a) $\int_0^1 x^2\,dx$, (b) $\int_0^\infty x e^{-x}\,dx$,
(c) $\int_0^\pi \sin^2\theta\,d\theta$.

**★3.** Compute $\lim_{x\to0}\sin x/x$ and
$\lim_{x\to0}(e^x - 1 - x)/x^2$ symbolically and by series.

**★4.** State the two error terms in a central difference and which way each
scales with $h$.

**★5.** State the side-lobe amplitude of the Ricker wavelet as a fraction of its
peak, and as a number.

---

## ★★ Applied

**★★6.** Derive symbolically the depth at which the vertical attraction of a
point mass at depth $d$ beneath the surface has its maximum horizontal gradient,
and evaluate it for $d = 1000$ m.

**★★7.** Verify by symbolic differentiation that
$q(z,t) = k\Delta T e^{-z^2/(4\kappa t)}/\sqrt{\pi\kappa t}$ satisfies the heat
equation for the temperature of the lesson's §7. Report the residual.

**★★8.** Compute $\int_0^1 dx/(1+x^2)$ symbolically and by
`scipy.integrate.quad`, and report both values, their difference, and which you
would quote with a tolerance.

**★★9.** Derive the Ricker wavelet's extrema, evaluate the ratio to the peak, and
report it to four significant figures as a fraction and in decibels.

**★★10.** Compute the Laplacian of $V = -GM/r$ in Cartesian coordinates and report
the residual after simplification, stating the domain on which the identity holds.

---

## ★★★ Research-oriented

**★★★11.** Build the gravitational attraction of a vertical cylinder of radius
$a$, depth range $[z_1, z_2]$ and density $\rho$ by integrating the point-mass
kernel over the cross-section symbolically. Verify against a numerical double
integral for three geometries, report the relative differences, and state which
route you would use for a survey of 10 000 stations.

**★★★12.** Quantify the finite-difference optimum for the diffusion gradient of
the lesson's §7. Map the relative error over $h$ from $10^{-1}$ to $10^{-9}$ m,
report the empirical exponent of the truncation regime and the minimum error with
its $h$, and compare with the classical estimate
$h_{\text{opt}} \approx (\epsilon|f|/|f'''|)^{1/3}$. State where the comparison
fails.
