# Exercises — 06-06-02 Travel-Time Tomography: Parametrisation and Inversion

Worked answers are in
[02-travel-time-tomography-solutions.md](02-travel-time-tomography-solutions.md).
The lesson is
[02-travel-time-tomography.md](../02-travel-time-tomography.md) and the
demonstration is
[../code/travel_time_tomography_demo.py](../code/travel_time_tomography_demo.py).

## ★ Foundational

1. A $16\times12$ cell grid covers $16\ \mathrm{km}\times5.5\ \mathrm{km}$.
   Compute the cell dimensions and the number of parameters, and state which
   feature sizes the parametrisation forbids.
2. With 140 rays and 192 parameters, compute the data-to-parameter ratio. Does
   that ratio alone tell you whether the problem is over- or underdetermined?
   Justify with the measured rank.
3. A datum misfit of $5.561\times10^{-2}\ \mathrm{s}$ on 140 picks corresponds
   to what per-pick rms residual? Compare it with the stated noise of 5 ms.

## ★★ Applied

4. From the CGLS table, estimate the misfit and the distance from the direct
   solution after 5, 10 and 20 iterations, and state the stopping rule you would
   use for a problem where each matrix-vector product costs 1 hour.
5. The grid sweep gives model errors of $1.6292\times10^{-2}$ ($8\times6$),
   $1.8668\times10^{-2}$ ($16\times12$) and $1.9810\times10^{-2}$
   ($32\times24$), with null fractions 0.519, 0.526 and 0.589. Separate the error
   into a row-space part and a null part for the $8\times6$ grid and check that
   the two add in quadrature to the measured total.
6. A colleague replaces the first-difference operator by a **second**-difference
   (Laplacian) operator. Predict what happens to the null space of the
   regulariser itself, and to the mean level of the model.

## ★★★ Research-oriented

7. The Fermat measurement shows the travel-time penalty of a forced mid-point
   displacement growing as $d^2$ (2.595, 11.315, 45.101 ms for 0.25, 0.50,
   1.00 km). Fit the coefficient, and use it to predict the penalty for a 2 km
   displacement. State the assumption you made.
8. The Newton iteration reduces the data residual from $2.99\times10^{-3}$ to
   $2.13\times10^{-6}$ s in one step, a factor of 1400, while the model error
   against the recoverable part falls only from $7.77\times10^{-4}$ to
   $7.18\times10^{-4}$. Explain both numbers, and say what a third iteration
   would change.
