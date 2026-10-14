# Exercises — 12-06-01 Moment of Inertia, Figure and Interior Constraints

Attempt these before reading the
[solutions](./01-moment-of-inertia-solutions.md). The lesson is
[01 Moment of Inertia, Figure and Interior Constraints](../01-moment-of-inertia.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A two-layer body has a core of radius $r_{c} = 0.25R$ with density
$\alpha = 1.5$ times the mantle density. Compute $C/MR^{2}$ with the shell
factor $(1-x^{5})/(1-x^{3})$, showing each term, and state which term dominates.

**★2.** Derive $C/MR^{2} = 2/5$ for a uniform sphere by integrating
$\tfrac{2}{3}r^{2}\,\mathrm{d}m$ over the radius. Show the two integrals and the
units of each.

**★3.** Evaluate the shell factor $(1-x^{5})/(1-x^{3})$ at $x = 0.5$ and
$x = 0.9$. Show that it tends to $5/3$ as $x\to1$ and explain what that limit
means physically.

## ★★ Applied

**★★4.** For the adopted constraint $C/MR^{2} = 0.3350$ the lesson's ridge table
gives $\alpha = 3.8083$ at $x_{\text{core}} = 0.45$. For
$M = 4.0\times10^{24}$ kg and $R = 3.0\times10^{6}$ m, compute the mean density,
the mantle density and the core density. Comment on whether the core density is
plausible.

**★★5.** A body has $J_{2} = 0.005$ and $C/MR^{2} = 0.335$. Compute the
dynamical ellipticity $H$, the rigid-body free-wobble period in sidereal days,
and the same period if the inertia factor were 2% larger. State which quantity
the period is most sensitive to.

**★★6.** The exact Maclaurin spheroid gives $f/q = 1.2451$ at $q = 4\times10^{-3}$,
while the first-order result is $f/q = 1.2500$. Compute the percentage error of
the first-order formula at that $q$, and at $q = 3\times10^{-2}$ (where the exact
value is $1.2144$). Comment on the trend.

## ★★★ Research-oriented

**★★★7.** A colleague proposes to determine the core radius of a body by
measuring $C/MR^{2}$ to 0.5%. Using the ridge of the lesson's §4, state exactly
what the measurement does and does not determine, and specify the additional
observable (with the precision it would need) that would close the inference.
Your specification must be executable: name the observable, the precision, and
the assumption that would remain.

**★★★8.** Starting from the definitions $J_{2} = (C-A)/(MR^{2})$ and
$H = (C-A)/C$, derive $H = J_{2}/(C/MR^{2})$ exactly. Then propagate the
independent fractional errors $\sigma_{J}/J_{2} = 1\%$ and
$\sigma_{C}/(C/MR^{2}) = 2\%$ into $\sigma_{H}/H$, and state what an observed $H$
at the 0.1% level would constrain if $J_{2}$ were known to 0.01%.
