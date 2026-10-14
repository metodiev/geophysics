# Exercises — 09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole

Attempt these before reading the
[solutions](./02-electrode-arrays-solutions.md). The lesson is
[02 Electrode Arrays](../02-electrode-arrays.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** Compute $k$ for a Schlumberger array with $L = 40$ m and $l = 4$ m.
Then compute the $\Delta V$ for $\rho_a = 120\ \Omega\,\mathrm{m}$ at
$I = 0.1\ \mathrm{A}$.

**★2.** Compute $k$ for a pole-dipole array with $n = 2$ and $a = 5$ m, and for
a dipole-dipole array with the same $n$ and $a$.

**★3.** Using $\Delta V = \rho I/k$, compute the signal ratio between a Wenner
array with $a = 5$ m and a dipole-dipole array with $n = 6$, $a = 5$ m, on a
$100\ \Omega\,\mathrm{m}$ half-space at $I = 0.1\ \mathrm{A}$.

## ★★ Applied

**★★4.** Explain why $F(0^+) = 1/2$ for every DC array, using the perturbation
argument of the lesson (a uniformly perturbed medium changes $\Delta V$ by
exactly $\varepsilon$ in the relative sense).

**★★5.** From the lesson's DOI table, estimate the spacing that a Wenner array
would need to reach 5 m, and compute the % signal cost relative to $a = 5$ m.

**★★6.** A dipole-dipole array with $n = 3$, $a = 10$ m gives $\rho_a = 80\
\Omega\,\mathrm{m}$ while a Wenner array with $a = 10$ m at the same place gives
$140\ \Omega\,\mathrm{m}$. Give two explanations consistent with the sensitivity
tables, and the measurement that would distinguish them.

## ★★★ Research-oriented

**★★★7.** Verify the kernel constant $1/(8\pi^2)$ analytically by integrating
$S_\rho$ over the whole half-space and using the identity
$\int\nabla(1/r_A)\cdot\nabla(1/r_M)\,\mathrm{d}V = 4\pi/r_{AM}$, then compare
the result with the demonstration's printed normalisation
($1.2268$ raw vs $1.2566$ required).

**★★★8.** Design a survey whose total sensitivity mass is concentrated between
5 and 15 m depth. Specify the array(s), the spacings, the expected signal at
$\rho = 50\ \Omega\,\mathrm{m}$ with $I = 0.2$ A, and argue from the DOI and
footprint numbers that the design meets the specification.
