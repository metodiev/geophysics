# Exercises — 19-02-03 Boundary Conditions: Dirichlet, Neumann, Absorbing, PML

Attempt these before reading the
[solutions](./03-fd-boundary-conditions-solutions.md). The lesson is
[03 Boundary Conditions](../03-fd-boundary-conditions.md). All models are
**SYNTHETIC**. Numbers printed by
`../code/fd_boundary_conditions_demo.py` may be quoted directly.

## ★ Foundational

**★1.** State the reflection coefficient for a pressure-release surface and for
a rigid (free) surface, and the boundary condition that imposes each.

**★2.** Write the ghost-node value for a Neumann condition
$\partial u/\partial n = q$ on a uniform grid at the left boundary, and the
boundary row it produces for the second-derivative operator.

**★3.** State the measured global order of a solution whose Neumann condition is
implemented with a two-point one-sided difference, and with a ghost node.

## ★★ Applied

**★★4.** A 1-D domain has a first-order one-way condition at one end. Using the
measured residual reflections, predict the reflection at $h = 0.125$ m if the
measured value at $h = 0.25$ m is $8.64\times10^{-8}$, and state the dB level.

**★★5.** A sponge layer of 40 cells has residual reflections $0.8652$,
$0.6494$, $0.6054$, $0.6468$ for $\sigma_{\max} = 0.05, 0.2, 0.5, 1.0$. Identify
the optimum, state the evidence that the behaviour is non-monotonic, and give
the dimensionless group that should set the damping scale.

**★★6.** A two-dimensional model has a free surface at the top and absorbing
edges elsewhere. Explain which conditions are physical, which are numerical, and
what measurement you would make to confirm each.

## ★★★ Research-oriented

**★★★7.** Design a boundary-condition test suite for a 2-D acoustic code that
establishes, independently: (a) the reflection coefficient of a physical free
surface, (b) the residual reflection of an absorbing edge at normal and oblique
incidence, and (c) the absence of leakage from the corners. State the geometry,
the source, the observable and the acceptance criterion for each, and say which
experiment would catch a sign error in the free-surface implementation.

**★★★8.** The lesson measures a graded sponge whose reflection falls roughly as
$1/W$ in layer width and whose optimum damping depends on the pulse bandwidth.
Explain why a PML does better — what makes its reflection fall exponentially
rather than algebraically — and state the two additional failure modes a PML
introduces that a sponge does not have.
