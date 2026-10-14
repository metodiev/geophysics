# Exercises — 03-07-04 Symbolic Tensors and Index Notation

> Solutions are in
> [`04-tensor-symbolic-solutions.md`](./04-tensor-symbolic-solutions.md).

---

## ★ Foundational

**★1.** Compute $\delta_{ii}$ and $\delta_{ij}\delta_{jk}$ in 3-D and state the
result in index-free notation.

**★2.** For $\sigma_{ij}$ symmetric and $A_{ij}$ antisymmetric, show that
$\sigma_{ij}A_{ij} = 0$.

**★3.** Write out $\varepsilon_{xy}$ in terms of $u_x$ and $u_y$ and identify
which part corresponds to a shear and which to a rotation.

**★4.** Evaluate $C_{ijkl}$ for $\lambda = \mu$ and count the non-zero components.

**★5.** State the two Lamé parameters and the two elastic constants a materials
laboratory reports, and the relation between $\nu = 0.25$ and the $v_p/v_s$ ratio.

---

## ★★ Applied

**★★6.** Derive the strain tensor for the displacement field $u = (0, 0, w(z))$
and interpret it physically. Which elastic constant alone relates $\sigma_{zz}$ to
$\varepsilon_{zz}$, and why?

**★★7.** Verify symbolically that the isotropic elasticity tensor is symmetric
under $i \leftrightarrow j$, $k \leftrightarrow l$ and $(ij) \leftrightarrow (kl)$.
Report which of the three SymPy confirms with a zero difference.

**★★8.** For a transversely isotropic medium with five independent constants,
write down $C_{ijkl}$ explicitly and count the non-zero components. Compare with
the 21 of the isotropic case.

**★★9.** Compute $J_2$ for a pure shear stress state $\sigma_{xy} = \tau$ and
compare with $\tau^2$; state the general result.

**★★10.** Reproduce the measured $v_p/v_s = 1.732051$ for $\nu = 0.25$ by deriving
$v_p/v_s$ from $(\lambda, \mu)$ algebraically and evaluating.

---

## ★★★ Research-oriented

**★★★11.** Build a symbolic validation of a $v_p/v_s$ inversion. Derive
$v_p(\lambda,\mu,\rho)$ and $v_s(\mu,\rho)$, solve for $(\lambda,\mu)$ from
$(v_p, v_s, \rho)$, and verify by substitution that both equations hold exactly.
Evaluate for a saturated sandstone ($v_p = 3000$ m/s, $v_s = 1600$ m/s,
$\rho = 2300\ \mathrm{kg\,m^{-3}}$) and report $\lambda$, $\mu$, $K$, $E$ and
$\nu$.

**★★★12.** Assess the abstract tensor module independently. Using only
`sympy.tensor.tensor`, attempt $\varepsilon_{ij}\varepsilon_{ij}$,
$A_{ij}B_{ij}$ and $C_{ijkl}\varepsilon_{kl}$ for symmetric symbolic tensors, and
report for each whether the result is correct against an explicit 3-D component
calculation. State your findings as a recommendation with the evidence.
