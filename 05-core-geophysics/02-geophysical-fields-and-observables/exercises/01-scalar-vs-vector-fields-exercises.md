# Exercises — 05-02-01 Scalar and Vector Fields; Potentials and Gradients

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Classify as scalar or vector field: temperature, gravitational
acceleration, magnetic flux density, gravitational potential, magnetic scalar
potential, electric field.

**★2.** Show that $\Phi = -Gm/r$ gives $\mathbf{g} = -Gm(\mathbf{r}-\mathbf{r}')/r^3$,
and check the dimensions.

**★3.** State Laplace's equation and the regions in which it holds for a
gravity survey.

**★4.** Explain in two sentences why gravity decays as $r^{-2}$ and the field of
a dipole as $r^{-3}$, from the potential viewpoint.

---

## ★★ Applied

**★★5.** A point mass of $2\times10^{9}$ kg is at 150 m depth. Compute $\Phi$ and
$g_z$ at the surface directly above, and verify numerically that
$g_z \approx -\Delta\Phi/\Delta z$ for a suitably small $\Delta z$.

**★★6.** For a dipole of moment 5 A·m², compute $|\mathbf{B}|$ at 100 m on the
equatorial axis and on the axial axis. State the ratio.

**★★7.** Draw, or describe precisely, the equipotential surfaces of a point mass
and of a vertically oriented dipole. Explain why the dipole's surfaces are not
spheres.

**★★8.** A magnetometer reads $|\mathbf{B}|$. Show that the total-field anomaly
is $\Delta T \approx \hat{\mathbf{b}}_0\cdot\mathbf{B}_a$ and state the
condition for the approximation to be accurate to 1%.

---

## ★★★ Research-oriented

**★★★9.** Numerically verify Laplace's equation for a synthetic anomaly. Take a
grid of observations above a point mass, compute $\Phi$ on the grid, then
estimate $\nabla^2\Phi$ by finite differences at an interior point. Report the
measured residual and show that it scales with the square of the grid spacing
(second-order convergence). State why the residual does not go to exactly zero,
and confirm that the maximum principle holds for the sampled anomaly.

**★★★10.** Construct the magnetic scalar potential for a uniformly magnetised
sphere and verify by numerical differentiation that it reproduces the dipole
field used in this lesson. Report the measured agreement and state which
approximation (point dipole versus finite body) each model represents.
