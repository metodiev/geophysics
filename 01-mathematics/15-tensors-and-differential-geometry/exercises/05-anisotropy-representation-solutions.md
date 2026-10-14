# Solutions — 01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes

> **Read this after attempting the exercises, not before.** Every component count
> and eigenvalue below was computed (six-by-six eigenvalues by a Jacobi iteration
> on the symmetric Voigt matrix); values attributed to the demonstration are its
> output.

---

## ★1 — Tensor to Voigt and back

**(a)** With the ordering $(11,22,33,23,13,12)\to(1,\dots,6)$ and both minor and
major symmetry, the Voigt matrix is symmetric, so it has
$6\cdot7/2 = 21$ independent entries.

**(b)** $C_{1111} = 40 \to C_{11}$; $C_{2222} = 30 \to C_{22}$;
$C_{1122} = 8 \to C_{12} = C_{21}$; $C_{1212} = 6 \to C_{66}$. Every other entry is
zero (the given list contains no $C_{3333}$, no $C_{2323}$ and no $C_{1313}$):

$$\mathbf C = \begin{pmatrix}
40 & 8 & 0 & 0 & 0 & 0\\
8 & 30 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 6
\end{pmatrix}\ \text{GPa}.$$

The matrix is a valid *conversion* but not a valid *material*: with $C_{33} = 0$ it
is not positive definite, so no strain energy is stored under axial strain along
$z$. Situations like this arise when a table is transcribed partially, and the
positive-definiteness check of ★★6 is what catches them.

**(c)** $\operatorname{diag}(20,20,20,10,10,10)$ means
$C_{1111} = C_{2222} = C_{3333} = 20$,
$C_{2323} = C_{1313} = C_{1212} = 10$, and every mixed component
$C_{iijj} = 0$ for $i\ne j$. That is exactly

$$C_{ijkl} = \mu\left(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}\right)
+ \lambda\,\delta_{ij}\delta_{kl} \qquad\text{with}\quad \mu = 10,\ \lambda = 0\ \text{GPa}.$$

A medium with $\lambda = 0$ has Poisson ratio $\nu = \lambda/(2(\lambda+\mu)) = 0$:
it stretches without contracting laterally.

**(d)** Only (c) is isotropic. An isotropic Voigt matrix satisfies

$$C_{12} = C_{11} - 2C_{66}, \qquad C_{44} = C_{55} = C_{66},$$

i.e. the axial shear moduli must all be equal and the off-diagonal entry must equal
$\lambda = C_{11} - 2C_{66} = 20 - 20 = 0$ ✓. Matrix (b) fails the first condition:
$C_{11} - 2C_{66} = 40 - 12 = 28 \ne C_{12} = 8$, and it also fails
$C_{44} = C_{66}$ ($0 \ne 6$). The condition is not a convention but a consequence
of the isotropic fourth-rank basis having exactly two independent tensors, which is
the derivation of [01-15-02](../02-tensor-algebra.md) §3.5.

---

## ★2 — The VTI matrix

**(a)** With the symmetry axis along $z$,

$$\mathbf C_V = \begin{pmatrix}
C_{11} & C_{12} & C_{13} & 0 & 0 & 0\\
C_{12} & C_{11} & C_{13} & 0 & 0 & 0\\
C_{13} & C_{13} & C_{33} & 0 & 0 & 0\\
0 & 0 & 0 & C_{44} & 0 & 0\\
0 & 0 & 0 & 0 & C_{44} & 0\\
0 & 0 & 0 & 0 & 0 & C_{66}
\end{pmatrix}, \qquad C_{12} = C_{11} - 2C_{66},$$

so the independent constants are $C_{11}$, $C_{33}$, $C_{44}$, $C_{66}$ and
$C_{13}$ — **five**.

**(b)** The constraint $C_{12} = C_{11} - 2C_{66}$ is the statement
$C_{1212} = \tfrac12(C_{1111} - C_{1122})$, which follows from the in-plane part of
the tensor being isotropic: a rotation by a generic angle kills every in-plane
angular weight $m\ne0$, leaving two in-plane constants with the third determined.
A matrix with the VTI *pattern* of zeros but a $C_{12}$ violating this relation is
invariant under a *four*-fold rotation, not a six-fold one — it is **tetragonal**,
and a seismic survey using it as VTI would predict azimuthally independent
velocities for a medium that has azimuthal dependence. That is why the constraint
is part of the definition rather than a notational choice.

**(c)** $C_{12} = 30 - 2(10) = 10$ GPa, so

$$\mathbf C_V = \begin{pmatrix}
30 & 10 & 12 & 0 & 0 & 0\\
10 & 30 & 12 & 0 & 0 & 0\\
12 & 12 & 22 & 0 & 0 & 0\\
0 & 0 & 0 & 7 & 0 & 0\\
0 & 0 & 0 & 0 & 7 & 0\\
0 & 0 & 0 & 0 & 0 & 10
\end{pmatrix}\ \text{GPa}.$$

**(d)** With $C_{66} = 5$ and $C_{11} = 30$ fixed, the constraint forces
$C_{12} = 30 - 10 = 20$ GPa. The matrix is then hexagonal-compatible only if it is
written with that $C_{12}$ — the value is *not* free. Keeping $C_{12} = 10$ while
changing $C_{66}$ to $5$ would break the relation and produce a tetragonal medium.

---

## ★3 — Thomsen parameters

**(a)**

$$\epsilon = \frac{C_{11} - C_{33}}{2C_{33}} = \frac{30 - 22}{44} = 0.181818,$$

$$\gamma = \frac{C_{66} - C_{44}}{2C_{44}} = \frac{10 - 7}{14} = 0.214286,$$

$$\delta = \frac{(C_{13}+C_{44})^{2} - (C_{33}-C_{44})^{2}}
{2C_{33}(C_{33}-C_{44})} = \frac{19^{2} - 15^{2}}{2(22)(15)}
= \frac{361 - 225}{660} = 0.206061 .$$

**(b)** With $\rho = 2400\ \mathrm{kg\,m^{-3}}$ (and $C$ in Pa, i.e.
multiplied by $10^{9}$):

| velocity | formula | value (m s$^{-1}$) | set by |
|---|---|---|---|
| $v_p(0)$ | $\sqrt{C_{33}/\rho}$ | 3027.6504 | $C_{33}$ |
| $v_{sv}(0)$ | $\sqrt{C_{44}/\rho}$ | 1707.8251 | $C_{44}$ |
| $v_p(90^\circ)$ | $\sqrt{C_{11}/\rho}$ | 3535.5339 | $C_{11}$ |
| $v_{sh}(90^\circ)$ | $\sqrt{C_{66}/\rho}$ | 2041.2415 | $C_{66}$ |

Note that $C_{13}$ appears in *none* of the four — which is exactly why it is the
constant that no single-direction experiment determines.

**(c)** The exact ratio is

$$\frac{v_p(90^\circ)}{v_p(0)} = \sqrt{\frac{C_{11}}{C_{33}}}
= \sqrt{1.363636} = 1.167748,$$

against $1 + \epsilon = 1.181818$: the approximation overestimates the ratio by
$0.014070$, i.e. **1.20 per cent**. The exact ratio is the square root of a ratio of
stiffnesses; $1+\epsilon$ is the first-order expansion of that square root in
$(C_{11}-C_{33})/C_{33} = 0.363636$, whose next term
$-\tfrac18(\cdot)^{2}$ would cost $1.65$ per cent. So the approximation is a
truncated series, and at $\epsilon = 0.18$ the neglected term is comparable to the
effect being measured — the weak-anisotropy approximation is *not* valid at this
level of anisotropy.

**(d)** For an isotropic medium $\epsilon = \gamma = \delta = 0$: all three are
measures of departure from isotropy, and each reduces to a difference of stiffnesses
relative to a reference. $\delta$ is the awkward one because it involves $C_{13}$,
which as (b) showed enters no axial velocity; $\delta$ is defined precisely so that
the combination $(C_{13}+C_{44})^{2}/(C_{33}(C_{33}-C_{44}))$ — which *does* control
the near-vertical $P$ and $SV$ behaviour — is isolated. It is measured only by
off-axis observations (a walkaway VSP or a range of source–receiver offsets), and
it is the parameter most often wrong in published models, because its effect is
weakest in the geometry most surveys use.

---

## ★4 — Counting by relations

**(a)** A single mirror plane (say $z\to-z$) makes the odd-index patterns vanish:
the surviving entries are $C_{11}, C_{12}, C_{13}, C_{22}, C_{23}, C_{33}, C_{44},
C_{55}, C_{66}$ together with $C_{16}, C_{26}, C_{36}, C_{45}$ — **13**
independent constants.

**(b)** Three orthogonal mirror planes (the orthorhombic group of order 4 in the
$mmm$ setting) kill the $C_{16}, C_{26}, C_{36}, C_{45}$ entries as well, leaving
the nine entries $C_{11}, C_{12}, C_{13}, C_{22}, C_{23}, C_{33}, C_{44}, C_{55},
C_{66}$ — **9** constants.

**(c)** A six-fold axis along $z$ additionally makes the in-plane part isotropic,
which imposes $C_{66} = \tfrac12(C_{11}-C_{12})$ and $C_{55} = C_{44}$, leaving
$C_{11}, C_{33}, C_{44}, C_{66}, C_{13}$ — **5** constants.

**(d)** In rocks: a set of parallel aligned fractures plus layering gives
orthorhombic (9) — the realistic default for a fractured reservoir; fine horizontal
layering at long wavelength gives transverse isotropy (5), because the layering is a
property of geometry rather than of any mineral; a single crystal with a
crystallographic preferred orientation gives the crystal's own class (olivine and
garnet are cubic, 3, calcite and quartz trigonal, 6); and a rock with no preferred
orientation at all gives isotropy (2). Triclinic (21) and monoclinic (13) arise in
rocks that have been sheared into a single foliation, where one mirror plane
survives.

---

## ★★5 — The factor of two

**(a)** With only $C_{1212}$ nonzero and
$e_{12} = e_{21} = 0.01$, all other $e_{kl} = 0$.

**(b)** Expanding over the nine ordered index pairs $(k,l)$:

$$\sigma_{12} = \sum_{k,l}C_{12kl}e_{kl} = C_{1212}e_{12} + C_{1221}e_{21}
= 20(0.01) + 20(0.01) = 0.4\ \text{GPa} = 400\ \text{MPa},$$

where the second term appears because $C_{1221} = C_{1212}$ by minor symmetry. The
factor of two is visible in the tensor contraction itself: the two ordered pairs
$(1,2)$ and $(2,1)$ each contribute.

**(c)** In Voigt notation with $\varepsilon_6 = 2e_{12} = 0.02$:

$$\sigma_6 = C_{66}\varepsilon_6 = 20(0.02) = 0.4\ \text{GPa} = 400\ \text{MPa}.$$

✓ Agreement is exact, not approximate.

**(d)** With the wrong convention $\varepsilon_6 = e_{12} = 0.01$:

$$\sigma_6 = 20(0.01) = 0.2\ \text{GPa} = 200\ \text{MPa},$$

a **factor of two too small** — the shear stress halved, silently. This is the
single most common error in implementing an anisotropic constitutive relation, and
it is invisible in any check that uses only axial strains. The demonstration prints
exactly this comparison (`400.0000` both ways with the correct convention, and
`200.0000` with the wrong one).

---

## ★★6 — Positive definiteness

Eigenvalues of the $6\times6$ Voigt matrix, in GPa:

| model | parameters | eigenvalues | positive definite? |
|---|---|---|---|
| (a) | $C_{66}=10$, $C_{13}=12$ | 7, 7, 10, 11.790627, 20, 50.209373 | **yes** |
| (b) | $C_{66}=5$, $C_{13}=12$ | 5, 7, 7, 10, 14, 58 | **yes** |
| (c) | $C_{44}=-1$ | $-1$, $-1$, 10, 11.790627, 20, 50.209373 | **no** |
| (d) | $C_{13}=25$ | $-5.482873$, 7, 7, 10, 20, 67.482873 | **no** |

The three eigenvalues $7, 7, 10$ in model (a) are the shear block
($C_{44}, C_{44}, C_{66}$); the other three come from the coupled $3\times3$
axial block, whose eigenvalues are
$\{20,\ 11.790627,\ 50.209373\}$ — the $20$ being the decoupled in-plane
combination $C_{11}-C_{12}$, and the remaining two solving
$\lambda^{2} - (C_{11}+C_{12}+C_{33})\lambda + \ldots$.

The classical necessary conditions:

| model | $C_{44}>0$ | $C_{11}>\lvert C_{12}\rvert$ | $C_{33}(C_{11}+C_{12}) > 2C_{13}^{2}$ | verdict matches? |
|---|---|---|---|---|
| (a) | $7>0$ ✓ | $30>10$ ✓ | $22(40) = 880 > 288$ ✓ | yes |
| (b) | $7>0$ ✓ | $30>20$ ✓ | $22(50) = 1100 > 288$ ✓ | yes |
| (c) | $-1>0$ ✗ | ✓ | ✓ | yes (caught by $C_{44}$) |
| (d) | ✓ | ✓ | $880 > 2(625) = 1250$ ✗ | yes |

Model (c) fails the most elementary condition — a negative shear modulus — and
model (d) fails the axial inequality, which is the one that catches an
over-large $C_{13}$. Model (b) is admissible but strongly anisotropic: its
$\epsilon = (30-22)/44 = 0.1818$ and
$\gamma = (5-7)/14 = -0.142857$, so the medium is slower in shear within the
isotropy plane than perpendicular to it — unusual, and worth checking against the
rock physics before believing it. The lesson's point stands: symmetries do not imply
stability, and the eigenvalues are the only complete check.

---

## ★★7 — A pattern of zeros is not a symmetry

**(a)** The two matrices have identical nonzero *positions*. Their axial velocities
are identical, because $v_p(0) = \sqrt{C_{33}/\rho}$,
$v_{sv}(0) = \sqrt{C_{44}/\rho}$, $v_p(90^\circ) = \sqrt{C_{11}/\rho}$ and
$v_{sh}(90^\circ) = \sqrt{C_{66}/\rho}$ involve only $C_{33}, C_{44}, C_{11},
C_{66}$ — and $C_{12}$ appears in none of them. So a survey that shoots only
vertically and horizontally cannot tell the two apart.

**(b)** Because the pattern of zeros is *necessary* but not *sufficient*: it says
which components are allowed to be nonzero, not what values the symmetry forces the
survivors to take. The missing information is the algebraic relation
$C_{12} = C_{11} - 2C_{66}$, and nothing in the array's structure records it.

**(c)** Both numbers are the largest change of the assembled tensor under a $60^\circ$
rotation about $z$, i.e. they test invariance directly. For the correct matrix the
change is $1.907\times10^{-6}$ GPa, which relative to the tensor's scale
($\sim3\times10^{10}$ GPa of accumulated component magnitude, or $\sim30$ GPa of
component value) is $6.4\times10^{-17}$ — round-off, i.e. **invariant**. For the
modified matrix the change is $3.750\times10^{9}$ — relative $1.3\times10^{-1}$,
13 per cent of the tensor's own magnitude: it is not invariant under the six-fold
rotation at all.

**(d)** The modified matrix is **tetragonal**: it is invariant under a four-fold
rotation but not a six-fold one, because the in-plane weight-4 combination survives
a $90^\circ$ rotation ($e^{\mathrm{i}4\phi} = 1$) but not a $60^\circ$ one. A
survey processing the data as VTI would fit a single $C_{12}$ (or $\delta$) to
observations that vary with azimuth, and would report a misfit that depends on
azimuth — the classic signature of mis-assigned symmetry. The practical cost is
that the azimuthal variation is either absorbed into noise or, worse, fitted by
anisotropy parameters that then mispredict the $\delta$ needed for depth imaging.

---

## ★★8 — Exact versus approximate velocities

**(a)** $v_p(0) = \sqrt{22\times10^{9}/2400} = 3027.6504$ m s$^{-1}$ and
$v_p(90^\circ) = \sqrt{30\times10^{9}/2400} = 3535.5339$ m s$^{-1}$.

**(b)** $v_p(0)(1+\epsilon) = 3027.6504(1.181818) = 3578.13$ m s$^{-1}$, which
exceeds the exact value by $42.60$ m s$^{-1}$, i.e. **1.20 per cent**.

**(c)** The exact horizontal-to-vertical ratio is
$\sqrt{C_{11}/C_{33}} = 1.167748$; the approximation predicts
$1 + \epsilon = 1 + (C_{11}-C_{33})/(2C_{33}) = 1.181818$. Writing
$C_{11}/C_{33} = 1 + 2\epsilon$, the exact ratio is $\sqrt{1+2\epsilon}$ whose
expansion is $1 + \epsilon - \epsilon^{2}/2 + \dots$; so the approximation is the
first-order term of a square root, and the quadratic term
$-\epsilon^{2}/2 = -0.016529$ accounts for 1.65 per cent, of which the observed
1.20 per cent is the net after the next term. It is a truncated series with a
*known* next term, which is why Thomsen's parameterisation is used with a stated
maximum $|\epsilon|$ rather than as an identity.

**(d)** An error of 1.2 per cent in a velocity is an error of 0.012 s per second of
travel time: for a 2 s two-way reflection that is 24 ms, comparable to the wavelet
period of a 40 Hz survey — enough to degrade a depth conversion and to bias
moveout-derived anisotropy estimates. The practical rule is that the weak-anisotropy
formulas are adequate for interpreting *trends* in $\epsilon$ and $\gamma$ but not
for converting a measured velocity ratio into a stiffness, which must be done
exactly.

---

## ★★9 and ★★★9 — The invariance projector

**(a)** Since each $R(g)$ is a linear map and $G$ is a group,
$R(g)R(h) = R(gh)$. Then

$$\mathcal P^{2} = \frac{1}{|G|^{2}}\sum_{g,h}R(g)R(h)
= \frac{1}{|G|^{2}}\sum_{g,h}R(gh)
= \frac{1}{|G|^{2}}\sum_{g}|G|R(g)
= \frac{1}{|G|}\sum_gR(g) = \mathcal P,$$

where the third step uses that for fixed $g$ the map $h\mapsto gh$ is a bijection of
$G$. So $\mathcal P$ is a projection onto the invariant subspace. $\square$

**(b)** For the group $\{E, m_z\}$ with $m_z = \operatorname{diag}(1,1,-1)$ acting as
$C'_{ijkl} = m_{ip}m_{jq}m_{kr}m_{ls}C_{pqrs}$, each index contributes a factor
$(-1)$ if it is $3$. A tensor component with an **odd** number of $3$-indices is
therefore negated by $m_z$ and forced to zero by the projector (an invariant must
satisfy $C' = C$, so $C = -C \Rightarrow C = 0$). Counting the entries of the
$21$-component Voigt basis with an odd number of $3$-indices:

$$C_{14},\ C_{15},\ C_{24},\ C_{25},\ C_{34},\ C_{35},\ C_{46},\ C_{56}
\quad\text{--- 8 entries,}$$

each being of the form $C_{a3}$- or $C_{33}$-type $3$-index-odd patterns
(explicitly: $(11,23), (11,13), (22,23), (22,13), (33,23), (33,13), (23,12),
(13,12)$ in index pairs, each containing exactly one $3$).

**(c)** The invariant subspace is the space of $21$-component tensors satisfying
$C' = C$, which is the image of $\mathcal P$; the eight odd entries are killed, so
its dimension is

$$21 - 8 = \boxed{13},$$

the monoclinic count, with the surviving entries
$C_{11}, C_{12}, C_{13}, C_{22}, C_{23}, C_{33}, C_{44}, C_{55}, C_{66}, C_{16},
C_{26}, C_{36}, C_{45}$ — the last four being the ones a single foliation allows to
be nonzero. $\square$

**(d)** The rank of $\mathcal P$ *is* the number of independent elastic constants of
the class, because $\mathcal P$ projects the 21-dimensional space of
minor-and-major-symmetric tensors onto the subspace that the point group leaves
fixed, and a basis of that subspace is a basis of independent constants. If the
group used is **too large**, $\mathcal P$ projects onto a smaller subspace and the
computed count is *lower* than the true one — the medium is then assumed to have
symmetry it does not have, which is exactly the failure measured in ★★7 (using a
six-fold group on a tetragonal matrix leaves a residual of 13 per cent). If the
group is too small, extra constants are admitted and the count is too high, which
is harmless for a forward model but loses the interpretive content of the class.

---

## ★★★10 — Backus average of two layers

**(a)** With $\langle\cdot\rangle$ the volume average over the two layers, the
Backus (long-wavelength) averages for a stack of isotropic layers are

$$C_{33} = \left\langle\frac{1}{\lambda+2\mu}\right\rangle^{-1}, \quad
C_{44} = \left\langle\frac{1}{\mu}\right\rangle^{-1}, \quad
C_{66} = \langle\mu\rangle, \quad
C_{13} = C_{33}\left\langle\frac{\lambda}{\lambda+2\mu}\right\rangle, \quad
C_{11} = \left\langle\frac{4\mu(\lambda+\mu)}{\lambda+2\mu}\right\rangle
+ \frac{C_{13}^{2}}{C_{33}} .$$

**(b)** With equal fractions of $(\lambda,\mu) = (30,20)$ and $(10,6)$ GPa — so
$\lambda+2\mu = 70$ and $22$, and $\lambda+\mu = 50$ and $16$ — the five averages
evaluate to:

| average | arithmetic | value (GPa) |
|---|---|---|
| $\langle1/(\lambda+2\mu)\rangle^{-1}$ | $\left(\tfrac12\tfrac1{70} + \tfrac12\tfrac1{22}\right)^{-1}$ | $C_{33} = 33.478261$ |
| $\langle1/\mu\rangle^{-1}$ | $\left(\tfrac12\tfrac1{20} + \tfrac12\tfrac16\right)^{-1}$ | $C_{44} = 9.230769$ |
| $\langle\mu\rangle$ | $\tfrac12(20) + \tfrac12(6)$ | $C_{66} = 13.000000$ |
| $\langle\lambda/(\lambda+2\mu)\rangle$ | $\tfrac12\tfrac{30}{70} + \tfrac12\tfrac{10}{22}$ | $0.4415584$ |
| $\langle4\mu(\lambda+\mu)/(\lambda+2\mu)\rangle$ | $\tfrac12\tfrac{4(20)(50)}{70} + \tfrac12\tfrac{4(6)(16)}{22}$ | $37.298701$ |

so

$$C_{13} = 33.478261(0.4415584) = 14.782609\ \text{GPa},$$

$$C_{11} = 37.298701 + \frac{14.782609^{2}}{33.478261}
= 37.298701 + 6.527386 = 43.826087\ \text{GPa},$$

$$C_{12} = C_{11} - 2C_{66} = 43.826087 - 26.000000 = 17.826087\ \text{GPa}.$$

**(c)** The constraint holds **identically** for this construction: the difference
$C_{11} - 2C_{66} - C_{12}$ evaluates to exactly $0$ in floating point, not because
it was imposed but because Backus averaging is itself a projection onto the
hexagonal subspace — a stack of isotropic layers is transversely isotropic by
*construction*, and the relation is a consequence. That is a useful diagnostic when
implementing the formulas: if the constraint fails, the averages have been mistyped.

**(d)** Thomsen parameters of the effective medium:

$$\epsilon = \frac{43.826087 - 33.478261}{2(33.478261)} = 0.154545, \qquad
\gamma = \frac{13.000000 - 9.230769}{2(9.230769)} = 0.204167,$$

$$\delta = \frac{(14.782609 + 9.230769)^{2} - (33.478261 - 9.230769)^{2}}
{2(33.478261)(33.478261 - 9.230769)} = -0.006959 .$$

The effective anisotropy ($\epsilon = 0.155$, $\gamma = 0.204$) is created purely by
geometry — each constituent is isotropic — and it is **stronger in shear than in
compression**: $\gamma > \epsilon$ is the signature of a stack whose contrast lies
in the shear moduli, and it is the opposite of the usual shale end member where
$\epsilon \gtrsim \gamma$. $\delta$ is small and **negative** ($-0.0070$); a
negative $\delta$ is physically admissible and common for layered media, and its
practical meaning is that the $P$-wave slowness surface is very nearly elliptical.
The general lesson is that "isotropic layers" is not a licence to assume an
isotropic overburden: a 50/50 stack with a $3\times$ stiffness contrast produces a
medium with 15-20 per cent anisotropy.
