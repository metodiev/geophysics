# Exercises — 01-15-03 Strain and Stress Tensors as Physical Tensors

Attempt these **closed-book** before opening the
[solutions](./03-strain-and-stress-tensors-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: stress is **tension positive**, so the traction on a face with
outward normal $n_j$ is $t_i = \sigma_{ij}n_j$; strain is the **scientific**
(tensorial) strain $e_{ij} = \tfrac12(u_{i,j} + u_{j,i})$, so the engineering shear
strain is $\gamma_{ij} = 2e_{ij}$ for $i\ne j$. State any convention you add. All
stress values are in MPa unless stated.

Problems referring to
[`../code/stress_strain_demo.py`](../code/stress_strain_demo.py) require you to
run it and report its actual output.

---

## ★ Foundational

**★1.** For the stress state

$$\boldsymbol\sigma = \begin{pmatrix}100 & 25 & -10\\ 25 & 60 & 5\\
-10 & 5 & 40\end{pmatrix}\ \text{MPa},$$

(a) give the traction on the three coordinate faces $\hat x_1$, $\hat x_2$,
$\hat x_3$;
(b) compute the traction on the plane with unit normal
$n = (0.6, 0.8, 0)$;
(c) split that traction into its normal and shear parts and check
$|t|^{2} = \sigma_n^{2} + \tau^{2}$;
(d) state how many independent measurements of traction on distinct planes are
needed to determine $\sigma_{ij}$ for an unknown state.

---

**★2.** For the same $\boldsymbol\sigma$:

(a) compute the three principal stresses;
(b) compute $I_1$, $I_2$ and $I_3$ from the components, and verify that they equal
the elementary symmetric functions of the principal stresses;
(c) split $\boldsymbol\sigma$ into isotropic and deviatoric parts and state $p$;
(d) compute $J_2$ and the von Mises equivalent stress $\sqrt{3J_2}$.

---

**★3.** Repeat ★2 for the two-dimensional state
$\boldsymbol\sigma = \begin{pmatrix}8&3\\3&2\end{pmatrix}$ MPa.

(a) Give the principal stresses exactly.
(b) Give the invariants $I_1$, $I_2$.
(c) Give the deviatoric part and $J_2$.
(d) State what the direction of the principal axes is, as an angle from the
$x_1$ axis, both exactly and numerically.

---

**★4.** A displacement field has the gradient

$$u_{i,j} = \begin{pmatrix}0.002 & 0.005 & -0.001\\ -0.005 & -0.004 & 0.001\\
0.001 & 0.003 & 0.002\end{pmatrix}.$$

(a) Compute $e_{ij}$ and $\omega_{ij}$.
(b) Compute the dilatation $e_{ii}$ and state the fractional volume change.
(c) Compute the engineering shear strain $\gamma_{12}$, $\gamma_{13}$,
$\gamma_{23}$.
(d) State which of $e$ and $\omega$ can store elastic energy and why.

---

## ★★ Applied

**★★5.** Derive the symmetry of the Cauchy stress tensor.

(a) Take a small cube of side $\ell$ and write the moment balance about its
centre, keeping the leading terms in $\ell$.
(b) Show that a distributed body couple density $c_k$ would also scale as
$\ell^{3}$, and that with $c_k = 0$ the antisymmetric part of $\sigma$ must
vanish.
(c) State the physical assumption that fails in a Cosserat medium and what
replaces it.
(d) State one geological situation in which the assumption is questionable.

---

**★★6.** A strike-slip stress state has $\sigma_1$ oriented north–south and
$\sigma_3$ east–west, both horizontal, with $\sigma_2$ vertical.

(a) State the orientation of the two planes that maximise the shear stress.
(b) State the resulting fault type and why the principal stresses predict it.
(c) For $\sigma_1 = 120$ MPa, $\sigma_2 = 80$ MPa, $\sigma_3 = 40$ MPa, compute the
maximum shear stress and the normal stress on the maximum-shear plane.
(d) State what a focal mechanism for an earthquake on such a plane would show, in
terms of the P and T axes.

---

**★★7.** Show that pure shear preserves volume, and distinguish it from simple
shear.

(a) From $|d\mathbf{x}'|^{2} - |d\mathbf{x}|^{2} = 2e_{ij}dx_idx_j$, show that a
pure shear $e_{12} = e_{21} = \epsilon$, all other components zero, has
$e_{ii} = 0$.
(b) Write the displacement field that produces it and compute its rotation tensor.
(c) Write the displacement field for simple shear $u_1 = \kappa x_2$,
$u_2 = u_3 = 0$, and compute $e$ and $\omega$ for it.
(d) Explain why the two produce the same stress in an isotropic material but
different microstructures in a rock.

---

**★★8.** Check the compatibility conditions for three strain fields:

(i) $e_{xx} = y^{2}$, $e_{yy} = x^{2}$, all other components zero;
(ii) $e_{xx} = x^{2}$, $e_{yy} = y^{2}$, $e_{xy} = 0$, all other components zero;
(iii) $e_{xx} = x^{2}$, $e_{yy} = y^{2}$, $e_{xy} = xy/2$, all other components
zero.

(a) Compute the residual of
$e_{ij,kl} + e_{kl,ij} - e_{ik,jl} - e_{jl,ik} = 0$ for each.
(b) Identify which fields are impossible, and state the physical state each
describes.
(c) For the compatible field, reconstruct a displacement field that produces it.
(d) State what happens numerically when an incompatible field is imposed on a
displacement-based finite-element model.

---

## ★★★ Research-oriented

**★★★9.** Construct the three-dimensional Mohr circles for the stress state of
★1.

(a) State the three principal stresses and the three circle radii.
(b) Show that the maximum shear stress over *all* plane orientations is
$(\sigma_1 - \sigma_3)/2$, and verify it against the value obtained by maximising
over the three circles.
(c) Explain why the two-dimensional maximum in-plane shear, computed in the plane
containing $\sigma_2$, is *less* than the three-dimensional maximum.
(d) State the formula $\tau_{\max} = (I_1 - 3\sigma_2)/2$ that appears in the
lesson, evaluate it, and comment on whether it equals $(\sigma_1-\sigma_3)/2$ for
this state.

---

**★★★10.** A moment tensor $M$ for a seismic source is symmetric with units of
N m.

(a) Split $M$ into isotropic and deviatoric parts and state what the isotropic part
measures physically.
(b) State how $M_0 = \left(\tfrac12M_{ij}M_{ij}\right)^{1/2}$ relates to the
invariants of the deviatoric part, and compute $M_0$ for
$M = \operatorname{diag}(3,-1,-2)\times10^{18}$ N m.
(c) Compute the principal axes, the principal values and the Lode angle of the
deviator, using equation (11) of the lesson.
(d) State what a seismologist can and cannot infer from the mechanism alone, in
terms of this lesson's invariants.

---

## Self-check

Before opening the solutions, confirm you can state for each problem (a) which
convention you used and (b) whether your answer would change under a global sign
flip of the stress. If a quantity is invariant under that flip, say so — that is
the difference between a physical quantity and a coordinate artefact.
