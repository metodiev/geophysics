# Exercises — 17-08-01 Mineral and Alteration Mapping from Space

Attempt these before reading the
[solutions](./01-mineral-mapping-rs-solutions.md). The lesson is
[01 Mineral and Alteration Mapping from Space](../01-mineral-mapping-rs.md). All
models and values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** A spectrum has $R(2.10) = 0.50$, $R(2.40) = 0.55$ and
$R(2.20) = 0.42$ (all $\mu\mathrm{m}$). Compute the linear continuum at
$2.20\ \mu\mathrm{m}$ and the absorption band depth.

**★2.** Define an *endmember* and state the two constraints the abundances of a
linear mixture model must satisfy.

**★3.** State in one sentence what continuum removal does, and one thing it
does *not* do.

## ★★ Applied

**★★4.** The lesson's degeneracy table gives $(a, g)$ pairs that all produce a
band depth of $0.0724$. Estimate, by linear interpolation between the tabulated
rows, the grain factor that reproduces the same depth at $a = 0.20$, and state
what the result means for a map that reports only the depth.

**★★5.** Two libraries have condition numbers $53.6$ and $130.2$ and unmixing
RMSEs on component 1 of $0.0087$ and $0.0229$. Compute the ratios of condition
numbers and of RMSEs, and comment on whether the RMSE growth is consistent with
the conditioning alone.

**★★6.** A curved spectral artefact of amplitude $0.10$ gives a band depth of
$0.0288$ in a scene with no clay. If the calibration maps a depth of $0.30$ to
unit abundance, compute the false apparent abundance and state why the *ratio*
of curvature to reference depth is the controlling quantity.

## ★★★ Research-oriented

**★★★7.** Design a study to break the abundance/grain-size degeneracy using a
second, independent absorption feature. State the data you would need, the model
you would fit, the quantity that separates the two causes, and the failure mode
that would leave them entangled. A specification that could not be executed is a
failed answer.

**★★★8.** The lesson shows that a *linear* spectral error cancels exactly in a
continuum-removed depth while a *curved* one does not. Explain why this is a
statement about the continuum (a straight line), and describe how you would use
the *shape* of the feature (not just its depth) to distinguish a real absorption
from a curved atmospheric artefact.
