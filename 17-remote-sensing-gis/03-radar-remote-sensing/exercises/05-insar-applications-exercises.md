# Exercises — 17-03-05 InSAR for Earthquakes, Volcanoes, Subsidence and Landslides

Attempt these before reading the
[solutions](./05-insar-applications-solutions.md). The lesson is
[05 InSAR Applications](../05-insar-applications.md). All models are
**SYNTHETIC** teaching values.

Constants: $\lambda = 5.6565\ \mathrm{cm}$, one fringe $= 2.8282\
\mathrm{cm}$ of LOS, $\lambda/4 = 14.141\ \mathrm{mm}$ per pixel.
Look vector at heading $8^\circ$, incidence $35^\circ$:
$\hat{u} = (+0.5680,\ -0.0798,\ +0.8192)$ in (east, north, up).

## ★ Foundational

**★1.** A strike-slip fault has slip $b = 1.5\ \mathrm{m}$ and locking depth
$d = 3\ \mathrm{km}$. Give the far-field offset, the peak surface strain
$\mathrm{d}u/\mathrm{d}x$ at the trace, and the displacement at $x = d$. State the
units of each.

**★2.** A surface point moves $3\ \mathrm{cm}$ east and $2\ \mathrm{cm}$ down. Using
the look vector above, compute its line-of-sight displacement. Comment on the
result in one sentence.

**★3.** A Gaussian uplift has amplitude $A = 4\ \mathrm{cm}$ and radius
$\sigma = 3\ \mathrm{km}$. Compute its volume with the exact Gaussian integral,
and the peak line-of-sight displacement and fringe count at $\theta = 35^\circ$.

## ★★ Applied

**★★4.** For the model $u(x) = (b/\pi)\arctan(x/d)$ with $b = 2.0\ \mathrm{m}$ and
$d = 4\ \mathrm{km}$: **(a)** compute the offset over a $\pm2d$ window as a
percentage of $b$; **(b)** find the distance at which $u = 0.4\,b$; **(c)** state
what physical quantity the answer to (b) is measuring.

**★★5.** Using the gradient budget of Section 3.4: **(a)** compute the largest LOS
change per $20\ \mathrm{m}$ pixel for an east–west strike-slip fault with
$b = 2\ \mathrm{m}$ and $d = 2\ \mathrm{km}$; **(b)** find the locking depth at
which the per-pixel change reaches the $\lambda/4$ aliasing limit for the same
slip; **(c)** interpret the result for the shallowest ruptures.

**★★6.** In the demonstration a $6\ \mathrm{mm}$ seasonal term biased a
$-14\ \mathrm{mm\,yr^{-1}}$ rate by $+0.9367\ \mathrm{mm\,yr^{-1}}$. **(a)** Predict
the bias if the seasonal amplitude were $12\ \mathrm{mm}$ instead, and justify the
prediction in one sentence. **(b)** State two properties of the record sampling
that could change the bias by a factor of two even at fixed seasonal amplitude.

## ★★★ Research-oriented

**★★★7.** A volcano shows a radially symmetric uplift of $4\ \mathrm{cm}$ peak with
a $2\ \mathrm{km}$ Gaussian radius in one interferogram. Design the observations
and the inversion that would determine the source depth separately from its
volume. State which trade-off you are breaking, what data breaks it, the
diagnostic you would compute, and the residual you would accept before claiming a
depth. A specification that could not be executed is a failed answer.

**★★★8.** The lesson shows that a northward motion leaks entirely into the east
estimate of the two-geometry decomposition. **(a)** Show that this perfect
leakage occurs when the two passes share the same value of
$\hat{u}_N/\hat{u}_E$. **(b)** Compute that ratio for the demonstration's
ascending and descending geometries and verify the claim. **(c)** State which
observable configuration would break the degeneracy and what additional
measurement would let a $10\ \mathrm{mm}$ north component be recovered.
