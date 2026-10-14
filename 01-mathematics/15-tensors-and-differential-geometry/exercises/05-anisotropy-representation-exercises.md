# Exercises — 01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes

Attempt these **closed-book** before opening the
[solutions](./05-anisotropy-representation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $C_{ijkl}$ is the elastic stiffness in the tensor notation,
$C_{\alpha\beta}$ its $6\times6$ Voigt matrix with the index mapping
$(11,22,33,23,13,12)\to(1,\dots,6)$; the **engineering** shear strain
$\varepsilon_\alpha = 2e_{ij}$ for $\alpha = 4,5,6$ sits on the strain side and
nowhere else. Constants are in GPa, densities in kg m$^{-3}$, velocities in
m s$^{-1}$. State your symmetry-axis convention in every answer.

Problems referring to
[`../code/voigt_anisotropy_demo.py`](../code/voigt_anisotropy_demo.py) require you
to run it and report its actual output.

---

## ★ Foundational

**★1.** Convert between tensor and Voigt notation.

(a) Write the $6\times6$ Voigt matrix of a general stiffness with minor and major
symmetry, and state how many independent entries it has.
(b) For a stiffness whose only nonzero components are
$C_{1111} = 40$, $C_{2222} = 30$, $C_{1122} = C_{2211} = 8$,
$C_{1221} = C_{2112} = C_{1212} = C_{2121} = 6$ GPa, write the Voigt matrix.
(c) Convert the diagonal Voigt matrix
$\operatorname{diag}(20, 20, 20, 10, 10, 10)$ GPa back to $C_{ijkl}$ and identify
the two Lamé constants it represents.
(d) State which of the two matrices in (b) and (c) describes an isotropic material,
give the pair of conditions an isotropic Voigt matrix satisfies, and say why the
other matrix fails them.

---

**★2.** The VTI stiffness matrix.

(a) Write the $6\times6$ matrix $\mathbf C_V$ for vertical transverse isotropy with
the symmetry axis along $z$, and state how many independent constants it has.
(b) Write the algebraic constraint on $C_{12}$ and explain why it is part of the
definition of hexagonal symmetry rather than a convention.
(c) For $C_{11} = 30$, $C_{33} = 22$, $C_{44} = 7$, $C_{66} = 10$,
$C_{13} = 12$ GPa, write out the matrix with $C_{12}$ evaluated.
(d) State what happens to $C_{12}$ if $C_{66}$ is changed to 5 GPa, given that
$C_{11}$ is fixed: does the matrix describe hexagonal symmetry?

---

**★3.** Thomsen parameters.

For the model of ★2(c):

(a) Compute $\epsilon$, $\gamma$ and $\delta$ to six decimals.
(b) Compute $v_p(0)$, $v_{sv}(0)$, $v_p(90^\circ)$ and $v_{sh}(90^\circ)$ with
$\rho = 2400\ \mathrm{kg\,m^{-3}}$, and state which constant sets each.
(c) Compute the exact ratio $v_p(90^\circ)/v_p(0)$ and compare it with
$1 + \epsilon$.
(d) State which of $\epsilon$, $\gamma$, $\delta$ would be zero for an isotropic
medium, and why $\delta$ is the awkward one to measure.

---

**★4.** Count independent constants by writing relations.

(a) Write the relations among the $C_{ijkl}$ implied by one mirror plane
(monoclinic) and count the survivors.
(b) Repeat for three orthogonal mirror planes (orthorhombic) and count.
(c) Repeat for a single axis of six-fold symmetry (hexagonal) and count.
(d) State, for each class, the physical cause in a rock that produces it.

---

## ★★ Applied

**★★5.** Verify the factor-of-two rule on a hand-worked pure shear.

(a) Take $C_{1212} = 20$ GPa as the only nonzero stiffness and impose the pure
shear strain $e_{12} = e_{21} = 0.01$, all other components zero.
(b) Compute $\sigma_{12}$ from the tensor contraction, including every term.
(c) Compute it from the Voigt form with $\varepsilon_6 = 2e_{12}$.
(d) Compute it from the Voigt form with $\varepsilon_6 = e_{12}$ and state the
error that the wrong convention produces.

---

**★★6.** Positive definiteness of VTI models.

For each model decide whether the $6\times6$ stiffness is positive definite, by
computing its six eigenvalues:

(a) $C_{11} = 30$, $C_{33} = 22$, $C_{44} = 7$, $C_{66} = 10$, $C_{13} = 12$;
(b) $C_{11} = 30$, $C_{33} = 22$, $C_{44} = 7$, $C_{66} = 5$, $C_{13} = 12$;
(c) $C_{11} = 30$, $C_{33} = 22$, $C_{44} = -1$, $C_{66} = 10$, $C_{13} = 12$;
(d) $C_{11} = 30$, $C_{33} = 22$, $C_{44} = 7$, $C_{66} = 10$, $C_{13} = 25$.

State in each case whether the model is physically admissible, and check the
classical necessary conditions $C_{44}>0$, $C_{11}>|C_{12}|$ and
$C_{33}(C_{11}+C_{12}) > 2C_{13}^{2}$ against your answer.

---

**★★7.** A pattern of zeros is not a symmetry.

Take the VTI matrix of ★2(c) and a modified matrix identical except that
$C_{12} = 20$ GPa.

(a) State what the two matrices have in common and what axial wave speeds they
share.
(b) Explain why the pattern of zeros alone cannot distinguish them.
(c) The demonstration measures the largest change of each tensor under a $60^\circ$
rotation about $z$: $1.907\times10^{-6}$ GPa (relative $6.4\times10^{-17}$) for the
correct matrix and $3.750\times10^{9}$ GPa (relative $1.3\times10^{-1}$) for the
modified one. Interpret both numbers.
(d) State what class the modified matrix belongs to, and what practical error a
seismic survey would incur if it were treated as VTI.

---

**★★8.** Comparing exact velocities with the Thomsen approximations.

(a) Compute $v_p(0)$ and $v_p(90^\circ)$ exactly for the model of ★2(c).
(b) Compute the weak-anisotropy approximation
$v_p(90^\circ) \approx v_p(0)(1 + \epsilon)$ and its error.
(c) Compute the exact ratio and the ratio predicted by $1 + \epsilon$, and state
why the approximation is not merely a Taylor expansion of the exact ratio.
(d) State what the $1.2$ per cent error implies for a survey whose anisotropy
parameter is $0.18$.

---

## ★★★ Research-oriented

**★★★9.** The invariance projector for a monoclinic point group.

Let $G$ be a point group and $R(g)$ the action of $g$ on rank-4 tensors.

(a) Show that $\mathcal P = \frac{1}{|G|}\sum_{g\in G}R(g)$ is a projector
($\mathcal P^{2} = \mathcal P$).
(b) For the monoclinic group with a single mirror plane perpendicular to $z$ (the
group $\{E, m_z\}$ of order 2), write the action of $m_z$ on the index patterns and
identify which of the 21 entries of the Voigt matrix are odd under it.
(c) Deduce that the invariant subspace has dimension $21 - 8 = 13$, and state which
8 entries are forced to zero.
(d) Explain what the rank of $\mathcal P$ has to do with the number of independent
elastic constants, and what goes wrong if the group used is too large.

---

**★★★10.** Backus average of a two-layer medium.

Two isotropic constituents are interleaved in thin horizontal layers with equal
volume fractions: layer A has $\lambda = 30$, $\mu = 20$ GPa; layer B has
$\lambda = 10$, $\mu = 6$ GPa.

(a) Write the Backus averages
$C_{33} = \langle1/(\lambda+2\mu)\rangle^{-1}$,
$C_{44} = \langle1/\mu\rangle^{-1}$, $C_{66} = \langle\mu\rangle$,
$C_{13} = C_{33}\langle\lambda/(\lambda+2\mu)\rangle$ and
$C_{11} = \langle4\mu(\lambda+\mu)/(\lambda+2\mu)\rangle + C_{13}^{2}/C_{33}$.
(b) Evaluate all five constants, and $C_{12}$ from the hexagonal constraint
$C_{12} = C_{11} - 2C_{66}$.
(c) Verify the constraint holds identically for this construction, and state why
that is a derivation rather than an assumption.
(d) Compute the Thomsen parameters of the resulting medium, and state whether the
effective anisotropy is stronger or weaker than either constituent's.

---

## Self-check

Before opening the solutions, state for each problem whether the quantity you
computed is (i) a component that changes under rotation, (ii) an invariant, or
(iii) a velocity. Only (ii) and (iii) may be compared with a paper's numbers
without first checking the paper's axis convention.
