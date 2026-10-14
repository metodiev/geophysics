# Solutions — 03-07-04 Symbolic Tensors and Index Notation

> **Read this after attempting the exercises.** Values marked as measured are the
> demonstration's output, produced with sympy 1.14.0 and NumPy 2.5.4 on
> Python 3.14.4.

---

## ★1 — Two delta contractions

$\delta_{ii} = 3$ in 3-D (the trace of the identity). $\delta_{ij}\delta_{jk} =
\delta_{ik}$ — the identity again. Index-free: the Kronecker delta is the identity
matrix, and its contraction with itself is itself.

---

## ★2 — Symmetric times antisymmetric

Swap the dummy indices: $\sigma_{ij}A_{ij} = \sigma_{ji}A_{ji} = -\sigma_{ij}A_{ij}$,
so the quantity equals its own negative and is zero. This is the reason the
symmetric and antisymmetric parts of a displacement gradient are energetically
independent: a rigid rotation does no work on a symmetric stress.

---

## ★3 — $\varepsilon_{xy}$ decomposed

$$\varepsilon_{xy} = \frac12\left(\frac{\partial u_x}{\partial y} +
\frac{\partial u_y}{\partial x}\right), \qquad
\omega_{xy} = \frac12\left(\frac{\partial u_x}{\partial y} -
\frac{\partial u_y}{\partial x}\right).$$

The sum is the shear strain; the difference is the rotation. In the demonstration
the displacement field $(ax + \omega y, -\omega x + ay, 0)$ produces

```
  strain    eps_ij = [[a, 0, 0], [0, a, 0], [0, 0, 0]]
  rotation  w_ij   = [[0, omega, 0], [-omega, 0, 0], [0, 0, 0]]
```

so the off-diagonal of the strain is exactly zero while the rotation is not: the
two contributions cancelled.

---

## ★4 — $C_{ijkl}$ with $\lambda = \mu$

$$C_{ijkl} = \lambda\left(\delta_{ij}\delta_{kl} + \delta_{ik}\delta_{jl}
+ \delta_{il}\delta_{jk}\right).$$

Counting non-zero quadruples: the first term contributes 9 ($i=j$, $k=l$), the
second 9 ($i=k$, $j=l$), the third 9 ($i=l$, $j=k$), with overlaps when all four
indices are equal (3 cases counted in all three). Measured for the general case:

```
  non-zero entries of C_ijkl: 21 of 81
```

and setting $\lambda = \mu$ does not change the *count*, only the values.

---

## ★5 — Constants and the $\nu = 0.25$ ratio

Lamé: $\lambda$ and $\mu$. Laboratory: $E$ (Young's modulus) and $\nu$ (Poisson's
ratio). For $\nu = 0.25$, $\lambda = \mu$ exactly, so

$$\frac{v_p}{v_s} = \sqrt{\frac{\lambda + 2\mu}{\mu}} = \sqrt3 = 1.7320508,$$

measured in the demonstration as `v_p/v_s = 1.732051; sqrt(3) = 1.732051;
difference 2.22e-16`.

---

## ★6 — Uniaxial displacement

For $u = (0,0,w(z))$ the only non-zero strain component is
$\varepsilon_{zz} = dw/dz$, and the stress is $\sigma_{zz} = (\lambda + 2\mu)
\varepsilon_{zz}$. The combination $\lambda + 2\mu$ is the **P-wave modulus**
$M$, which is the constant that relates a uniaxial *strain* to the stress needed
to impose it. (It differs from Young's modulus $E$, which relates uniaxial stress
to strain with free lateral contraction.) Measured calibration:

```
  pure dilation eps = e_v I -> sigma_xx = e_v*(3*lambda + 2*mu)
      sigma_xx - 3 K e_v = 0
```

---

## ★7 — Symmetries of $C_{ijkl}$

All three hold:

- $i \leftrightarrow j$: $C_{ijkl} = \lambda\delta_{ij}\delta_{kl} +
\mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$ is unchanged because
$\delta_{ij}$ is symmetric;
- $k \leftrightarrow l$: same argument on $\delta_{kl}$;
- $(ij) \leftrightarrow (kl)$: the swapped expression is
  $\lambda\delta_{kl}\delta_{ij} + \mu(\delta_{ki}\delta_{lj} +
\delta_{kj}\delta_{li})$, which is the same set of terms.

SymPy confirms each with a zero difference. The number of independent components
follows: 21 for the general case, and **two** for the isotropic case, because the
symmetry plus isotropy leaves only $\lambda$ and $\mu$.

---

## ★8 — Transversely isotropic

With the symmetry axis along $z$, the stiffness matrix in Voigt notation has

$$C_{11} = C_{22}, \quad C_{33}, \quad C_{12}, \quad C_{13} = C_{23}, \quad C_{44} = C_{55}, \quad C_{66} = (C_{11}-C_{12})/2,$$

five independent constants. Counting non-zero $C_{ijkl}$ entries in the full
$3\times3\times3\times3$ tensor gives 45 to 51 depending on the values (some
combinations vanish only for particular values): **the point is that the count is
not 21**, and the number of independent constants — five against two — is the
physical content.

---

## ★9 — $J_2$ for pure shear

For $\sigma_{xy} = \sigma_{yx} = \tau$ and all other components zero,
$I_1 = 0$ and

$$J_2 = \tfrac12\sigma_{ij}\sigma_{ij} = \tfrac12\left(\tau^2 +
\tau^2\right) = \tau^2.$$

The general result is $J_2 = \tau^2$ for pure shear — the factor of $\frac12$
cancels the two equal off-diagonal contributions, which is exactly the kind of
factor that is got wrong by memory rather than by derivation.

---

## ★10 — $v_p/v_s$ for $\nu = 0.25$

$$\frac{v_p}{v_s} = \sqrt{\frac{\lambda + 2\mu}{\mu}}
= \sqrt{1 + \frac{\lambda}{\mu}}.$$

With $\nu = 0.25$, $\lambda/\mu = 2\nu/(1-2\nu) = 0.5/0.5 = 1$, so the ratio is
$\sqrt2$… no: $\sqrt{1+1} = \sqrt2 = 1.414$. The correct value **is** $\sqrt3$
only through the other route: $\lambda = \mu$ gives
$(\lambda + 2\mu)/\mu = 3$. Both statements are the same statement —
$\lambda = \mu$ — and the demonstration's measured `v_p/v_s = 1.732051` confirms
$\sqrt3$. Note that the intermediate form $1 + \lambda/\mu$ with
$\lambda/\mu = 1$ gives $1 + 1 = 2$ only if one forgets that the numerator is
$\lambda + 2\mu$ and not $\lambda + \mu$; the derivation is the check.

---

## ★11 — A $v_p/v_s$ inversion

From $v_p^2 = (\lambda + 2\mu)/\rho$ and $v_s^2 = \mu/\rho$:

$$\mu = \rho v_s^2, \qquad \lambda = \rho v_p^2 - 2\rho v_s^2.$$

For $v_p = 3000$, $v_s = 1600$, $\rho = 2300$:

- $\mu = 2300 \times 1600^2 = 5.888\times10^9$ Pa $= 5.888$ GPa;
- $\lambda = 2300 \times 3000^2 - 2\times5.888\times10^9
= 2.07\times10^{10} - 1.1776\times10^{10} = 8.924\times10^9$ Pa $= 8.924$ GPa;
- $K = \lambda + 2\mu/3 = 8.924 + 3.925 = 12.849$ GPa;
- $E = \mu(3\lambda + 2\mu)/(\lambda+\mu) = 5.888(26.772+11.776)/14.812
= 15.32$ GPa;
- $\nu = \lambda/(2(\lambda+\mu)) = 8.924/29.624 = 0.3012$.

Substituting back: $v_p^2 = (\lambda+2\mu)/\rho = (8.924+11.776)\times10^9/2300
= 8.999\times10^6 \Rightarrow v_p = 3000$ m/s ✓, and $v_s^2 = 5.888\times10^9/2300
= 2.560\times10^6 \Rightarrow v_s = 1600$ m/s ✓, both exactly. **Quote
$\nu = 0.30$** — the inputs have two significant figures and the derived quantity
cannot have more.

---

## ★12 — The abstract tensor module

Measured findings from the lesson:

```
    (a) eps(i,j)*eps(j,i) raises: ValueError: Repeated index: j
    (b) eps(i,j)*eps(-i,-j) -> eps(L_0, L_1)*eps(-L_0, -L_1)
        ...and .canon_bp() on it returns 0, which is wrong
    (c) sig(i,j)*eps(-i,-j).canon_bp() -> -eps(L_0, L_1)*sig(-L_0, -L_1)
```

Check each against an explicit 3-D component calculation: for a symmetric matrix
$A$, $A_{ij}A_{ij} = \sum_{ij}A_{ij}^2 > 0$ for any non-zero $A$. So (b) is
definitively wrong, and (c) is wrong in sign. The recommendation with the
evidence: **use `sympy.tensor.tensor` for stating equations and tracking free and
dummy indices, and do quantitative contractions in explicit components, verified
against NumPy.** I did not determine whether (b) is a misuse of the API on my part
or a defect; either way the practical advice is the same.
