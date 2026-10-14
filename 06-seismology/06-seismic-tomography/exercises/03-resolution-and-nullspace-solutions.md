# Solutions — 06-06-03 Resolution, Null Space and Model Covariance

Exercises:
[03-resolution-and-nullspace-exercises.md](03-resolution-and-nullspace-exercises.md).

## ★ Foundational

**1.** $192 - 141 = \mathbf{51}$ null directions, i.e. $51/192 = \mathbf{26.6}$
per cent of the model space is invisible to the data.

**2.** A single-cell spike is smeared: only 61.8 per cent of the estimate in that
cell is the spike itself, and the remaining 38.2 per cent comes from other cells
(measured as a weighted spread of about 2.4 km in $x$ and 1.4 km in $z$).

**3.** $8.9\times10^{-3}\times3000 =
\mathbf{26.7\ m\,s^{-1}}$, i.e. $\mathbf{0.89}$ per cent of $v_0$. (Velocity and
slowness perturbations are related by $\delta v/v_0 = -\delta u/u_0$ to first
order.)

## ★★ Applied

**4.** The effective count is $\operatorname{tr}R = \mathbf{109.3}$ parameters
out of 192. If errors were computed as if all 192 were independent, each would be
too small by roughly $\sqrt{192/109.3} = \mathbf{1.33}$ — before any allowance
for correlated cells, which errs in the same direction.

**5.** Adding in quadrature gives
$\sqrt{0.9^2+0.9^2} = \mathbf{1.27}$ per cent. The measured correlation of
$-0.098$ means the errors are (weakly) anti-correlated, so the true standard
deviation of the mean is
$0.9\sqrt{(1 + (-0.098))/2} = 0.9\times0.672 = \mathbf{0.60}$ per cent: the
quadrature formula overstates the uncertainty by a factor of about 2.1. For
adjacent cells, where the correlation approaches 1.000, the quadrature formula
would overstate it by a much larger factor.

**6.** $R^2$ measures the fraction of the *input model*'s energy recovered, not
the size of its data signature. The 4 km checkerboard is closer in scale to the
ray spacing and to the point-spread width (median 4.73 km in $x$), so the
inversion cannot disentangle its cells and destroys more of its energy even
though it predicts more datum (51.4 ms against 24.8 ms). Data amplitude and
recoverability are different things: what matters is whether a pattern projects
onto the geometry's near-null directions.

## ★★★ Research-oriented

**7.** The $x$ point spread is long because the rays run predominantly in $x$.
A second acquisition with the same number of rays but a **subsurface source or a
second borehole at 90 degrees** — for example sources in the left borehole and
receivers along the *bottom* of the region, so that rays cross the interior
diagonally — adds a second angular family. Prediction: the $x$ point spread falls
towards the $z$ value (1.3-2.0 km), the rank rises towards the number of
independent rays, and $\operatorname{tr}R$ rises. The honest test is a
known-model (checkerboard) inversion of the combined ray set, because the
predicted improvement is a statement about the resolution matrix, not about the
data misfit.

**8.** A feature is likely to be an image of the null space if it is
reproducible by a model perturbation with (i) $\lVert G\mathbf{v}\rVert$ below
the noise, (ii) amplitude concentrated where the ray count is low, and (iii) a
shape equal to a leading null vector of the published parametrisation. The
diagnostic to request from the authors is therefore the **first few right
singular vectors of their $G$** together with their singular values and the
data covariance; failing that, the resolution matrix's columns at the disputed
cells. What you cannot do is decide from the figure alone: a null-space feature
and a true feature look identical in the image, which is the point of the
lesson.
