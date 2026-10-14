# Exercises — 03-07-01 Symbolic Variables, Expressions and Assumptions

> Solutions, with the measured outputs, are in
> [`01-symbolic-basics-solutions.md`](./01-symbolic-basics-solutions.md).

---

## ★ Foundational

**★1.** For each expression, say what SymPy returns with the symbol declared
(a) unconstrained, (b) `real=True`, (c) `positive=True`:
(i) $\sqrt[3]{x^3}$ (ii) $|x|$ (iii) $\sqrt{x}\sqrt{x}$ (iv) $e^{\ln x}$.

**★2.** Compute by hand and then with SymPy: $\frac17 \times 7$, $\frac17$ as a
binary64, and the difference between the two as an exact rational.

**★3.** Convert to exact rationals: (a) 0.375, (b) 2.5, (c) 0.1. Which is exactly
representable in binary64, and how can you tell from the denominator?

**★4.** The demonstration prints `mpmath.mp.dps = 15` rather than assuming a
value. Explain why a numeric claim about precision has to be measured in the
session that makes it.

**★5.** Evaluate $0.1 + 0.2 - 0.3$ in binary64 and state the exact rational value
of the discrepancy.

---

## ★★ Applied

**★★6.** Declare symbols for the density, radius and gravitational constant of a
planet and derive the surface gravity of a uniform sphere symbolically. Evaluate
for Mars ($R = 3.390\times10^{6}$ m, $\rho = 3933\ \mathrm{kg\,m^{-3}}$,
$G = 6.67430\times10^{-11}$ m³ kg⁻¹ s⁻²) and compare with the measured surface
gravity $3.71\ \mathrm{m\,s^{-2}}$. Report the discrepancy and two reasons for it.

**★★7.** Derive the depth at which a two-layer model has equal free-air and slab
contributions, symbolically, and evaluate it for $\rho = 2670\ \mathrm{kg\,m^{-3}}$.

**★★8.** Show symbolically that $\sin^2\theta + \cos^2\theta = 1$ only after
`trigsimp`, and report the operation counts before and after. Name the single
function that gives the same result.

**★★9.** Using `nsimplify`, demonstrate one case where it recovers the intended
constant and one where it destroys a genuinely different value. Report both inputs
and outputs.

**★★10.** Compute the mean density of the Earth from surface gravity and radius
symbolically and evaluate it. Report the value, the SI dimensional check, and the
percentage difference from 5514 kg/m³.

---

## ★★★ Research-oriented

**★★★11.** Derive the mean density of a two-layer Earth (crust of density
$\rho_1$ to depth $d$, mantle $\rho_2$ below) symbolically, then solve for the
mantle density given a mean of $5514\ \mathrm{kg\,m^{-3}}$, a crustal density of
$2700\ \mathrm{kg\,m^{-3}}$ and a crustal thickness of 35 km. Report the exact
rational if one arises, the float, and the significant figures the inputs justify.

**★★★12.** Quantify the growth of exact rational arithmetic. Build
$S_n = \sum_{k=1}^{n} \frac1k$ symbolically for $n = 10, 10^2, 10^3$ and report
for each the number of digits in the numerator and denominator of the exact sum,
the value to 20 digits, and `count_ops`. State where you would stop using exact
arithmetic and why.
