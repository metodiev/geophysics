# Exercises — 06-06-01 The Tomography Principle: Data as Path Integrals

Worked answers are in
[01-tomography-principle-solutions.md](01-tomography-principle-solutions.md).
The lesson is [01-tomography-principle.md](../01-tomography-principle.md) and the
demonstration is
[../code/tomography_demo.py](../code/tomography_demo.py). All numbers below are
**SYNTHETIC**.

## ★ Foundational

1. A ray of length $L = 12.0\ \mathrm{km}$ crosses a cell whose slowness is
   perturbed by $\delta u = +1.0\times10^{-6}\ \mathrm{s\,m^{-1}}$. Compute the
   travel-time perturbation in milliseconds and state the units of every factor.
2. Using the demonstration's grid ($\mathrm{d}x = 1.0\ \mathrm{km}$,
   $\mathrm{d}z = 0.5\ \mathrm{km}$, 10 by 10 cells, $v_0 = 4000\ \mathrm{m\,s^{-1}}$),
   compute the $G$ entry for a vertical ray from $(x = 2.55\ \mathrm{km},
   z = 0.25\ \mathrm{km})$ to $(x = 2.55\ \mathrm{km},
   z = 5.25\ \mathrm{km})$.
3. A datum of $0.067\ \mathrm{s}$ rms with 8 per cent anomalies gave a
   second-order remainder of $4.07\times10^{-3}\ \mathrm{s}$ rms. Estimate the
   remainder for 4 per cent anomalies and justify the scaling in one sentence.

## ★★ Applied

4. In the demonstration the wide-aperture acquisition has rank 89 on 100 cells
   and the narrow one has 30 cells with no ray. Estimate the null-space
   dimension contributed by the unlit cells alone, and compare it with the
   measured total.
5. A $+8$ per cent velocity perturbation is applied to a cell. Convert it to a
   slowness perturbation and state the sign, using
   $u = 1/(v_0(1+p))$.
6. The two acquisitions in the demonstration have data misfits of
   $2.214\times10^{-4}$ s and $2.875\times10^{-4}$ s and model errors of
   $9.74\times10^{-3}$ and $1.81\times10^{-2}$ in $v/v_0$. Compute the ratio of
   model errors and explain why the misfit ratio gives the opposite impression.

## ★★★ Research-oriented

7. Design an acquisition for the same 10 by 10 cell region that would raise the
   rank from 89 to 144 with 144 rays. State the geometry, and predict which
   singular-value directions improve. (Hint: rank is limited by the angular
   range of rays crossing each cell.)
8. The demonstration reports $\lVert R-I\rVert_F/\sqrt{n} = 0.3317$ at
   $\lambda/\lambda_{\max} = 10^{-4}$. Show that a null space of dimension $d$
   out of $n$ parameters alone implies a floor of about $\sqrt{d/n}$, evaluate
   it, and explain why your answer is a lower bound rather than an equality.
