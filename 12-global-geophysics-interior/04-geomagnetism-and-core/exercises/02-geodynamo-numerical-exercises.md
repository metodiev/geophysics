# Exercises — 12-04-02 Numerical Geodynamo Models

Attempt before the [solutions](./02-geodynamo-numerical-solutions.md). Lesson:
[02 Numerical Geodynamo Models](../02-geodynamo-numerical.md). All models
**SYNTHETIC**; the parameters are adopted inputs.

## ★ Foundational

**★1.** For $\nu = 10^{-6}\ \mathrm{m^2\,s^{-1}}$,
$\eta = 0.7958\ \mathrm{m^2\,s^{-1}}$, $L = 3.48\times10^6$ m and
$\Omega = 7.292\times10^{-5}\ \mathrm{s^{-1}}$, compute the Ekman number and the
magnetic Prandtl number. State what each of them compares.

**★2.** State which term of the induction equation creates field and which
destroys it, and write the ratio of their magnitudes for a flow of speed $U$ and
scale $L$.

**★3.** A two-mode dynamo has $\kappa = 1$, $\alpha = \omega = 1.5$. Compute the
dynamo number $D$, the linear growth rate, and the saturation amplitude for
$B_{\text{sat}} = 1$.

## ★★ Applied

**★★4.** Starting from
$\mathrm{d}P/\mathrm{d}t = \alpha T - \kappa P$,
$\mathrm{d}T/\mathrm{d}t = \omega P - \kappa T$, derive the growth rates and the
onset condition $D = 1$. Then find the ratio $T/P$ at saturation and explain why
the saturated state is steady rather than oscillatory.

**★★5.** For $Pm = 10^{-4}$, compute $\sqrt{\eta/\nu}$ and the number of grid
points per direction needed to resolve both the viscous and the magnetic
diffusion lengths. Repeat for $Pm = 1$ and state the practical implication.

**★★6.** Compute the Elsasser number for $B = 2\ \mathrm{mT}$ with
$\rho = 1.1\times10^4\ \mathrm{kg\,m^{-3}}$, $\eta = 0.7958\ \mathrm{m^2\,s^{-1}}$
and $\Omega = 7.292\times10^{-5}\ \mathrm{s^{-1}}$. Say whether that field is in
the magnetostrophic regime and what would have to change for it to be
$\Lambda = 0.3$.

## ★★★ Research-oriented

**★★★7.** A scaling study reports $B_{\text{rms}} \propto Pm^{1/2}$ between
$Pm = 0.1$ and $Pm = 10$. Extrapolate to $Pm = 10^{-6}$ and state the result.
Then repeat with the exponent changed by $\pm 0.1$ and report the range. Explain
why the range, not the value, is the honest output.

**★★★8.** Specify a verification suite for a new dynamo code that could detect a
sign error in the Lorentz-force term. State each test, the analytic or independent
reference it uses, and the tolerance you would accept.

## Notes on answers

Answers must state which quantities are inputs, which are outputs and which are
extrapolations, and must not present a simulation's numbers as properties of the
Earth's core.
