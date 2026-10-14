# Exercises — 01-12-04 Numerical Integration: Trapezoid, Simpson, Gauss Quadrature

Attempt these **closed-book** before opening the
[solutions](./04-numerical-integration-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $h=(b-a)/n$; the composite trapezoid rule is $T_n$; the composite
Simpson rule $S_n$; an $n$-point Gauss–Legendre rule has degree of exactness
$2n-1$; $G = 6.674\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$ and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$. State any convention you add.

---

## ★ Foundational

**★1.** Compute the composite trapezoid and Simpson estimates of
$\int_0^1\mathrm e^x\,dx$ with $n=4$ panels, and compare each with the exact
value.

---

**★2.** State the degree of exactness of the 3-point Gauss rule. Verify it by
integrating $x^4$ and $x^6$ on $[-1,1]$.

---

**★3.** Derive the one-panel Simpson rule from the requirement of exactness on
cubics and show that its error term is $-h^4f''''(\xi)/180$.

---

**★4.** A sediment layer of density $2670\ \mathrm{kg\,m^{-3}}$ and thickness
200 m extends to infinity laterally. Compute the Bouguer slab gravity anomaly in
mGal, and state which limit of a quadrature it represents.

---

## ★★ Applied

**★★5.** Show that the trapezoid error series contains only even powers of $h$ by
writing $f$ as a Taylor series and summing the panel errors.

---

**★★6.** Use the Romberg table in the lesson to estimate $\int_0^1\mathrm e^x\,dx$
to eight digits. State which table entry you used and why the next refinement
level does not help.

---

**★★7.** The integral $\int_0^1x^{-1/2}\,dx$ is improper. Compute it by (a) a
composite trapezoid rule with the endpoint value omitted, (b) the substitution
$x=t^2$ followed by Simpson with 8 panels, and (c) a 4-point Gauss rule. Compare
the three errors and explain the ranking.

---

**★★8.** A gravity anomaly is computed by quadrature with $n_r=n_\mu=4$ and comes
out 1% low. Using the error table in the lesson, estimate the node counts needed
for 0.01% accuracy, and state the assumption you are making about the integrand.

---

## ★★★ Research-oriented

**★★★9.** Implement the finite-plate Bouguer quadrature: a square plate of
half-width $L$ and thickness $t$, with the observation point at the centre of the
top surface. Measure $g_z/(2\pi G\rho t)$ for $L/t = 1$, 10 and 100, report the
approach to the infinite-slab limit, and explain how the corner singularity at the
observation point affects the Gauss convergence.

---

**★★★10.** A colleague integrates a magnetic anomaly over a dipping dyke by
Gauss–Legendre quadrature with 20 nodes and reports four-figure accuracy, verified
by repeating the calculation with 24 nodes. Critique the verification, and state
the two independent checks you would require instead.
