# Exercises — 04-04-03 Fold Geometry, Mechanisms and Interpretation

Attempt these **closed-book** before opening the
[solutions](./03-folds-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/03-folds_demo.py`](../code/03-folds_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** A fold is described by $z(x) = A\cos(2\pi x/\lambda)$ with $A = 200$ m
and $\lambda = 2000$ m.

(a) Compute the maximum limb dip and state where it occurs.
(b) Compute the curvature at the crest.
(c) State where the curvature is zero and what that implies structurally.
(d) State which two parameters determine the shortening, and whether the limb
dips do.

---

**★2.** Ramsay's thickness classification: the orthogonal thickness ratio for
parallel folding is $t' = \cos\alpha$.

(a) Compute $t'$ at limb dips of 10°, 50° and 70°.
(b) State the value of $t'$ for similar folding.
(c) Compute the ratio of the two predictions at 50°.
(d) State why that ratio is measurable in the field and why it is diagnostic.

---

**★3.** State the sign convention and the physical meaning of the shear strain
$\gamma = 2\tan(\alpha/2)$ for flexural slip.

(a) Compute $\gamma$ at limb dips of 30° and 60°.
(b) Compute $\tan\alpha$ for the same dips and compare.
(c) State which mechanism each corresponds to and why the two differ.
(d) State what measurement would distinguish them in the field.

---

## ★★ Applied

**★★4.** Run [`../code/03-folds_demo.py`](../code/03-folds_demo.py).

(a) Report the arc length, chord length and shortening over four wavelengths for
the demo's fold.
(b) Report the maximum limb dip.
(c) Report the recovered amplitude and its error, and the rms residual in
degrees.
(d) State what the fit assumed and what it therefore could not determine.

---

**★★5.** The buckling relation for a single competent layer is
$\lambda_d/d = 2\pi(G/6)^{1/3}$.

(a) Compute $\lambda_d/d$ for $G = 10$, 100 and 1000.
(b) State the exponent and verify it by comparing 10 and 1000.
(c) Compute the viscosity ratio implied by a measured wavelength ratio of 2, and
state why the answer is unusable as a measurement.
(d) State the direction in which the relation is useful.

---

**★★6.** The excess-area method states $h = A/S$. For a sinusoidal fold belt the
demo derives $h = 2\lambda^2/(\pi^2A)$.

(a) Run the demo and report the predicted $h$, the numerical $h$, and the
percentage difference.
(b) State the cause of the difference.
(c) Report the sensitivity of $h$ to a 10 per cent change in amplitude and to a
10 per cent change in wavelength.
(d) State which of the two limits the method, and why.

---

## ★★★ Research-oriented

**★★★7.** Derive the closed form used in ★6.

(a) Show that the excess area of $n$ waves of amplitude $A$ and wavelength
$\lambda$ is $A_{\text{excess}} = n\lambda A/2$.
(b) Show that, to second order in the limb dip, the bed-length shortening is
$S = n\pi^2A^2/(4\lambda)$. State where the factor of 4 comes from.
(c) Hence show that $h = 2\lambda^2/(\pi^2A)$, independent of $n$.
(d) Explain why the independence of $n$ is the content of the result rather than
a coincidence, and state the kinematic assumption that makes it true.

---

**★★★8.** A fold train has limbs at 50° and a measured thickness ratio of 0.75.

(a) State whether the value is consistent with parallel folding, with similar
folding, or with neither, and show the arithmetic.
(b) Propose a mechanism that produces an intermediate value.
(c) Estimate the flattening strain required to reduce the $t'$ of a parallel fold
from $\cos 50^\circ$ to 0.75, stating your model.
(d) State what additional measurement would test your model, and what the model
predicts for it.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
