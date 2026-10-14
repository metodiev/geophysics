---
id: 26-04-01
title: "Annotated Bibliography: Mathematics and Numerical Methods"
level: intermediate
prereqs: []
estimated_minutes: 25
tags: [reference, bibliography, mathematics, numerics]
---

# Annotated Bibliography: Mathematics and Numerical Methods

An annotated list of the mathematics and numerical-analysis books this
curriculum assumes you can reach. Each entry says what the book is for, at what
level it is written, and what it does *not* cover.

## How to use this page

Entries are grouped by purpose, not alphabetically: general methods, linear
algebra, numerical analysis, differential equations, optimisation, and tables.
Read the "use it for" column before ordering anything.

**Honesty statement about citations.** The author–title pairs below are real,
widely held works; they are not invented, and no DOI or URL is fabricated. Years
and edition numbers change between printings and reissues, so treat the edition
given here as indicative and **verify the edition and year in a library
catalogue before citing**. Where the edition is uncertain, the entry says so
explicitly.

*Provenance:* bibliographic reference only. This repository hosts no copyrighted
text.

## General mathematical methods

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Arfken, Weber & Harris**, *Mathematical Methods for Physicists* (Academic Press/Elsevier; 7th ed. 2013) | advanced | The standard broad reference: complex analysis, special functions, integral transforms, tensors, Sturm–Liouville problems | Numerical method design; it is analytic in emphasis |
| **Boas**, *Mathematical Methods in the Physical Sciences* (Wiley; 3rd ed. 2005) | intermediate | A gentler route to the same material; good for self-study of series, Fourier methods and vector calculus | Deep or rigorous proofs |
| **Abramowitz & Stegun**, *Handbook of Mathematical Functions* (National Bureau of Standards; 1964, reprinted by Dover) | reference | Numerical tables, identities and asymptotic forms for special functions. Now effectively superseded by the NIST Digital Library of Mathematical Functions | Derivations; it is a handbook |
| **Gradshteyn & Ryzhik**, *Table of Integrals, Series and Products* (Academic Press; 8th ed. 2014) | reference | Looking up a definite integral you cannot do and do not need to derive | Learning technique; a table is a lookup tool |

## Linear algebra and matrix computation

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Strang**, *Linear Algebra and Its Applications* (Cengage; edition varies) | intermediate | First exposure to the four subspaces, least squares and the geometry of the SVD | Numerical stability guidance |
| **Golub & Van Loan**, *Matrix Computations* (Johns Hopkins University Press; 4th ed. 2013) | advanced | The authoritative account of QR, SVD, eigenproblems and least-squares algorithms, with error analysis | A first course; the density is high |
| **Trefethen & Bau**, *Numerical Linear Algebra* (SIAM; 1997) | advanced | *Why* the algorithms work: conditioning, stability, SVD geometry, iterative methods, written with unusual clarity | Complete analysis of huge sparse systems |
| **Trefethen & Embree**, *Spectra and Pseudospectra* (Princeton University Press; 2005) | research | Why non-normal matrices behave nothing like their eigenvalues suggest — directly relevant to inverse problems and to iterative solver behaviour | Practical recipes |
| **Hansen**, *Rank-Deficient and Discrete Ill-Posed Problems* (SIAM; 1998) | research | The definitive numerical treatment of regularisation: SVD, generalised cross-validation, the L-curve | Geophysical interpretation |

## Numerical analysis and partial differential equations

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Burden & Faires**, *Numerical Analysis* (Cengage; edition varies) | intermediate | A conventional first course: root finding, interpolation, quadrature, initial-value problems, error analysis | Modern large-scale methods |
| **LeVeque**, *Finite Difference Methods for Ordinary and Partial Differential Equations* (SIAM; 2007) | advanced | Stability, consistency and convergence of finite-difference schemes for the diffusion, advection and wave equations | Unstructured meshes |
| **Hairer, Nørsett & Wanner**, *Solving Ordinary Differential Equations I* (Springer; 2nd ed. 1993) | advanced | Stiff and non-stiff ODE problems, order and stability theory, with a companion volume on stiff problems | PDE boundary-value problems |
| **Trefethen**, *Spectral Methods in MATLAB* (SIAM; 2000) | advanced | Spectral differentiation and the exponential accuracy that makes it worth the boundary-condition care | Problems with discontinuities |
| **Press, Teukolsky, Vetterling & Flannery**, *Numerical Recipes* (Cambridge University Press; 3rd ed. 2007) | intermediate | Practical descriptions and code for a very wide range of methods, useful for orientation | Citation-grade error analysis; always check the primary literature |

## Optimisation and inverse problems

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Nocedal & Wright**, *Numerical Optimization* (Springer; 2nd ed. 2006) | advanced | Line search, trust region, quasi-Newton methods, and their convergence theory | Stochastic or global optimisation |
| **Boyd & Vandenberghe**, *Convex Optimization* (Cambridge University Press; 2004) | advanced | Why convex problems are the ones you can actually solve reliably; duality; modern regularised formulations | Non-convex (most geophysical) misfits |

## Which one to read, by need

| If you need to… | Start with |
|---|---|
| Refresh series, transforms and vector calculus | Boas |
| Look up a special-function identity | Abramowitz & Stegun (or its NIST successor) |
| Understand why an inversion is ill-conditioned | Trefethen & Bau, then Golub & Van Loan |
| Choose a damping parameter defensibly | Hansen |
| Understand a finite-difference stability condition | LeVeque |
| Implement an optimiser | Nocedal & Wright, with Press et al. for orientation |

## How to cite these works

Give author, title, edition, publisher and year, exactly as printed on the
title page of the edition you actually used. Because editions of textbooks are
reissued with revisions, a citation that omits the edition is not reproducible:
a page reference in the 3rd edition may point at different material in the 4th.

## Assumptions and regime of validity

- These annotations are this repository's opinion about level and usefulness;
  they are not claims about quality or about which book is "best".
- Copyrighted books are cited, never reproduced. Confirm availability through
  your library or a legitimate vendor.
- Publication years and editions are indicative. **Verify before citing.**

## Related pages

- [Annotated Bibliography: Physics, Elasticity and Continuum Mechanics](./02-bibliography-physics.md)
- [Annotated Bibliography: Inverse Theory, Statistics and ML](./05-bibliography-inverse-stats.md)
- [Formula Sheet: Linear Algebra, SVD and Numerics](../03-formula-handbook/02-formulas-linear-algebra-numerics.md)
- [01-mathematics folder overview](../../01-mathematics/README.md)
- [19-numerical-modeling-hpc folder overview](../../19-numerical-modeling-hpc/README.md)
