# Exercises — 19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom

Attempt these before reading the
[solutions](./01-discretisation-concepts-solutions.md). The lesson is
[01 Discretisation](../01-discretisation-concepts.md). All models are
**SYNTHETIC** teaching values. Numbers printed by
`../code/discretisation_concepts_demo.py` may be quoted directly.

## ★ Foundational

**★1.** A 1-D domain of length $L = 800$ m is discretised with $N = 160$ cells.
State $h$, the number of cell centres, the number of nodes, and the number of
degrees of freedom for one scalar field stored node-centred and cell-centred.

**★2.** A 2-D grid has $N_x = 400$ and $N_y = 250$ cells. Give the number of
unknowns and the float64 storage in MiB for two scalar fields stored
cell-centred.

**★3.** For $g(x) = x^{2}$ on $[0,1]$ with $h = 0.02$, compute the midpoint and
trapezoid estimates of $\int_0^1 g\,\mathrm dx$ and state the exact error of
each.

## ★★ Applied

**★★4.** A three-dimensional acoustic model covers
$12\ \mathrm{km}\times12\ \mathrm{km}\times5\ \mathrm{km}$ with $h = 25$ m and
stores pressure plus a three-component particle velocity. Compute the DOF and the
float64 memory for all fields, and state how many copies of the whole state an
explicit second-order-in-time scheme needs.

**★★5.** A column of length $1.2$ km has $\kappa_1 = 2.0$ and $\kappa_2 = 6.0\
\mathrm{W\,m^{-1}\,K^{-1}}$ with the interface at $0.45$ km. Compute the exact
effective conductivity, then the flux a cell-centred scheme with harmonic face
averaging produces, then the flux a node-centred scheme with arithmetic averaging
produces, for $\Delta T = 80$ K.

**★★6.** In the demonstration the discrete $L^{2}$ norm of $x^{2}$ on $[0,1]$
differs from the continuous norm by $0.1863391\,h^{2}$ at $N = 320$. Derive that
constant from the midpoint-rule error and state which sign the difference has.

## ★★★ Research-oriented

**★★★7.** Design a grid convention for a 1-D problem with three materials in
series ($\kappa = 1, 4, 20\ \mathrm{W\,m^{-1}\,K^{-1}}$, interfaces at
$0.3L$ and $0.7L$) that reproduces the exact steady flux to round-off. State
where the unknowns live, where the properties live, and how you would verify the
claim numerically. Then state what changes when the interfaces do not fall on
cell faces, and estimate the resulting error.

**★★★8.** For the 2-D five-point Laplacian on an $n\times n$ grid the condition
number grows as $O(h^{-2})$ while the truncation error falls as $O(h^{2})$. A
colleague proposes to exploit this: "since refining makes the linear system
worse, the optimum grid is the coarsest one for which the discretisation error is
acceptable." Examine the claim: state where it is right, where it is wrong, and
what additional quantity decides the question. Support the argument with the
measured quantities from the demonstration.
