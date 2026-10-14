# Exercises — 19-08-02 Simulating Gravity and Magnetic Responses

Attempt these before reading the
[solutions](./02-simulate-gravity-response-solutions.md). The lesson is
[02 Simulating Gravity and Magnetic Responses](../02-simulate-gravity-response.md).
All bodies are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the exact infinite-slab gravity for $\Delta\rho = 500$ kg m$^{-3}$
and $t = 100$ m, in mGal. State why the answer does not depend on the slab's depth.

**★2.** A point mass of $2.0\times10^{9}$ kg sits at $250$ m depth. Compute the
vertical gravity directly above it and at $500$ m horizontal offset, in mGal, and
give the ratio.

**★3.** A uniformly magnetised sphere of radius $150$ m and magnetisation
$2.0$ A m$^{-1}$ is centred at $400$ m depth. Compute its dipole moment and the
field directly above the centre, in nT.

## ★★ Applied

**★★4.** Using the demonstration's cube-versus-point-mass table, state the smallest
offset beyond which the point-mass error is below $0.5$ per cent, and explain why
the error is *not* monotonic in offset.

**★★5.** Three bodies have the same mass and centroid: a $200$ m cube, an
equivalent sphere and a $4\times4$ km sheet $200$ m thick. Using the demonstration's
numbers, state which pair of offsets would discriminate all three, and what the
discriminating signal is.

**★★6.** A cube of side $200$ m has a uniform magnetisation of $0.5$ A m$^{-1}$.
Compute the field of its equivalent dipole at $300$ m depth, in nT, and state the
two reasons why the real body's anomaly differs from this.

## ★★★ Research-oriented

**★★★7.** Design a survey that could distinguish a compact body from an
equal-mass sheet, stating the station spacing, the offsets, and the model-form
signature you would plot. Include the noise level you assume and justify it.

**★★★8.** The demonstration verifies its quadrature to $1.3\times10^{-14}$ at
20 nodes per axis. For a body with a $10{:}1$ aspect ratio and a target accuracy of
$10^{-6}$, state the convergence test you would run, why the node count cannot be
chosen from the sphere's table alone, and what you would report if the test failed
to converge.
