# Solutions — 17-03-06 SAR Polarimetry and Polarimetric Decomposition

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [06 Polarimetry](../06-polarimetry.md).

---

## ★1 — Canonical matrices and their Pauli vectors

**(a) Trihedral:**
$$S = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
\qquad
\mathbf{k} = \frac{1}{\sqrt{2}}(2,\ 0,\ 0) = (1.4142,\ 0,\ 0).$$
Pure $k_1$: **odd-bounce / surface mechanism**, $\alpha = 0^\circ$.

**(b) Dihedral:**
$$S = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
\qquad
\mathbf{k} = \frac{1}{\sqrt{2}}(0,\ 2,\ 0) = (0,\ 1.4142,\ 0).$$
Pure $k_2$: **double bounce**, $\alpha = 90^\circ$. The name comes from the two
reflections: a wave bouncing from the ground to a vertical wall and back acquires
$S_{HH}$ and $S_{VV}$ with opposite signs, which is exactly $\mathrm{diag}(1,-1)$.

**(c) Dipole at $30^\circ$:** with $\cos^2 30^\circ = 0.75$,
$\sin 30^\circ\cos 30^\circ = 0.4330$, $\sin^2 30^\circ = 0.25$,
$$S = \begin{pmatrix} 0.75 & 0.4330 \\ 0.4330 & 0.25 \end{pmatrix},
\qquad
\mathbf{k} = \frac{1}{\sqrt{2}}(1.00,\ 0.50,\ 0.8660)
= (0.7071,\ 0.3536,\ 0.6124).$$

The first component is $1/\sqrt{2}$ of the norm for **every** dipole orientation,
so $\alpha = \arccos(1/\sqrt{2}) = 45^\circ$ regardless of how the dipole is
turned — which is exactly why the lesson warns that $\alpha$ alone does not
identify volume scattering.

---

## ★2 — The Pauli norm identity

$$\mathbf{k} = \frac{1}{\sqrt{2}}(3,\ 1,\ 1) = (2.1213,\ 0.7071,\ 0.7071).$$
$$\left|\mathbf{k}\right|^{2} = 4.5 + 0.5 + 0.5 = 5.5.$$

Directly from the matrix:
$$\left|S_{HH}\right|^{2} + \left|S_{VV}\right|^{2} + 2\left|S_{HV}\right|^{2}
= 4 + 1 + 2(0.25) = 5.5. \;\checkmark$$

The factor 2 on the cross-polarised term is reciprocity: one measured channel
stands for the two that would exist if the matrix were not symmetric.

---

## ★3 — Bragg resonant wavelengths

$$\Lambda_B = \frac{\lambda}{2\sin\theta} = \frac{5.6565\ \mathrm{cm}}{2\sin\theta}.$$

| $\theta$ | $\sin\theta$ | $\Lambda_B$ | physical scale |
|---|---|---|---|
| $20^\circ$ | 0.3420 | 8.269 cm | clods and furrows of tilled soil |
| $35^\circ$ | 0.5736 | 4.931 cm | gravel, small-scale soil roughness, capillary waves |
| $50^\circ$ | 0.7660 | 3.692 cm | fine gravel and wind ripples |

The radar does not see the whole roughness spectrum, only the component that
happens to satisfy the resonance condition at that geometry. That is why the same
field has a different $\sigma^{0}$ at two incidence angles.

---

## ★4 — Reading a coherency matrix

**(a)** $\sum\lambda = 1.60+0.30+0.10 = 2.00$, so
$$p = (0.8000,\ 0.1500,\ 0.0500).$$
$$H = -\frac{0.8\ln 0.8 + 0.15\ln 0.15 + 0.05\ln 0.05}{\ln 3}
= \frac{0.17851 + 0.28457 + 0.14979}{1.09861} = 0.5578.$$
$$A = \frac{0.30-0.10}{0.30+0.10} = 0.5000.$$

**(b)** $\alpha_i = \arccos(0.95,\ 0.45,\ 0.20)
= (18.19^\circ,\ 63.26^\circ,\ 78.46^\circ)$, so
$$\alpha = 0.8(18.19) + 0.15(63.26) + 0.05(78.46)
= 14.55 + 9.49 + 3.92 = 27.96^\circ.$$

**Interpretation:** $H = 0.56$ is moderate and $A = 0.5$ shows the two weaker
eigenvalues differ, so there is a definite second mechanism; the dominant
eigenvector is surface-like ($18^\circ$). The honest description is "dominant
surface scattering with an ordered secondary contribution" — not volume
scattering, which would need comparable weights and all angles near $45^\circ$.

**(c)** The degeneracy caution applies **weakly**: the eigenvalues are well
separated ($A = 0.5$, $\lambda_2/\lambda_3$ ratio 3), so the eigenvectors of the
non-degenerate pair are unique and the mean $\alpha$ is stable. Compare the
lesson's example where $\lambda_2 = \lambda_3$ exactly and the ambiguity was
$3.50^\circ$.

---

## ★5 — One ratio, two explanations

Linear ratios:
$$10^{-3.0/20} = 0.7079, \qquad 10^{-4.8/20} = 0.5754.$$

From the demonstration's table at $\epsilon = 6.0$:
$HH/VV(35^\circ) = 0.679805$ ($-3.352$ dB) and
$HH/VV(45^\circ) = 0.548037$ ($-5.224$ dB).

Compare the *changes*: measurement $-4.8 - (-3.0) = -1.8$ dB; model
$-5.224 - (-3.352) = -1.872$ dB. The two agree to $0.07$ dB, so the pair is
**consistent with the same dielectric constant** and with the incidence angle
doing all the work.

**Correct interpretation:** the pair of measurements does not determine
$\epsilon$; it determines a *combination* of $\epsilon$ and the two incidence
angles. If the two angles are known independently (from a DEM and the orbit), the
pair constrains $\epsilon$ with the residual 0.07 dB of model error. If they are
not, the same data could be explained by a wetter surface at a smaller angle or a
drier one at a larger angle. This is the polarimetric form of the
$\sigma^{0}$-as-material-constant fallacy: two observables, two unknowns, and one
of the unknowns is geometric.

---

## ★6 — The convergence of entropy and the safety of a threshold

Fit $H(N) = H_\infty\left(1 - a/N\right)$ using $N = 16$ and $N = 64$, where the
$1/N$ form implies $(H_\infty - H_{16})/(H_\infty - H_{64}) = 64/16 = 4$:
$$H_\infty - 0.1743 = 4\left(H_\infty - 0.1831\right)
\;\Longrightarrow\;
3H_\infty = 0.7324 - 0.1743 = 0.5581
\;\Longrightarrow\; H_\infty = 0.1860.$$

Then $H_\infty(1-a/16) = 0.1743$ gives $a/16 = 0.0631$, $a = 1.010$, so
$$H(N) \approx 0.186\left(1 - \frac{1.01}{N}\right).$$

**Implication for a threshold at $H > 0.20$:** the converged entropy of this
*deterministic surface target* under 15% noise is $0.186$, which is $7\%$ below
the threshold. So the threshold would not misclassify it — but the margin is
$0.014$, less than the standard deviation of $H$ at 16 looks (0.013 observed
between the 10% and 90% points around $0.174$). **The classification is not
safe**: at a slightly higher noise level $H_\infty$ would exceed 0.20 and every
surface pixel would be labelled volume scattering.

The practical rule: a threshold must exceed the *measured, converged* entropy of
the null population by more than its scatter at the actual look count, and both
numbers have to be reported. A threshold chosen by eye from a false-colour map
has no such guarantee.

---

## ★7 — Flooded versus dry forest (specification)

**Geometry and channels.** Quad-polarimetric (HH, HV, VV, VH) at one incidence
angle near $35^\circ$, single-look complex, so that the coherency matrix can be
built. A *single* polarimetric acquisition per date is enough for the mechanism
map; repeat passes are needed only if the flood state is transient.

**Parameters and expected values.** Compute $H$, $\alpha$, $A$ and the eigenvalues
for each pixel.

| mechanism | $H$ | $\alpha$ | $A$ | dominant eigenvalue |
|---|---|---|---|---|
| dry canopy (volume over ground) | 0.8–0.9 | 40–50 | low | spread |
| flooded forest (double bounce trunk–water) | low–moderate | 70–90 | higher | strong |
| open water / smooth surface | very low | $<20$ | low | dominant |

The discriminator is **$\alpha$ together with the second eigenvalue**: flooding
turns the trunk–ground path into a trunk–water specular path, raising
$\alpha$ toward $90^\circ$ and concentrating power in a single eigenvalue. The
lesson's canonical table gives the endpoints: dihedral $89.25^\circ$ with
$H = 0.0715$, versus random volume $42.35^\circ$ with $H = 0.9119$.

**Look count.** The demonstration shows $H = 0$ at one look and convergence within
about $10\%$ by 16 looks at 15% noise. Require at least 16 independent looks
(equivalently, a multilook window that averages $\ge 16$ single-look samples),
and *measure* the converged entropy of a known dry-forest control area rather than
assuming it.

**Unavoidable confounder.** Vegetation structure and biomass also move $\alpha$
and the eigenvalues, and they vary within a stand. A second date with the same
geometry but a known water state cannot be obtained for a transient flood, so the
method relies on the *contrast* within one scene (flooded versus dry stands)
rather than on an absolute threshold. That contrast must be stated as the
assumption, and the classification reported with the two populations' statistics.

---

## ★8 — Invariance, and how large the alpha ambiguity can be

**(a)** From the definitions, $p_i = \lambda_i/\sum\lambda$ and
$A = (\lambda_2-\lambda_3)/(\lambda_2+\lambda_3)$ depend only on the **eigenvalues**,
which are unique for a given $T$. Entropy likewise. Mean alpha,
$\alpha = \sum p_i\arccos|u_{i,1}|$, depends on the **eigenvectors**, which are
unique only when the eigenvalues are distinct: inside a degenerate subspace any
orthonormal basis is a valid eigenbasis, and $T$ is unchanged.

**(b)** The eigenvectors form an orthonormal basis, so their first components
satisfy the completeness relation
$$\left|u_{1,1}\right|^{2} + \left|u_{2,1}\right|^{2} + \left|u_{3,1}\right|^{2} = 1
\qquad\Longrightarrow\qquad
\sum_i \cos^{2}\alpha_i = 1 .$$
For the extreme case $T = I$ (all three eigenvalues equal, so *any* orthonormal
basis is an eigenbasis) this constrains the mean alpha to a band. A random search
over orthonormal bases gives

$$\alpha_{\text{mean}} \in [54.7356^\circ,\ 59.9177^\circ],$$

a range of $5.18^\circ$. The lower endpoint is the symmetric configuration
$\cos\alpha_i = 1/\sqrt{3}$ for all three, i.e.
$\arccos(1/\sqrt{3}) = 54.7356^\circ$; the upper endpoint is approached by a basis
like $(1,0,0),(0,1,0),(0,0,1)$ with $\alpha = (0^\circ,90^\circ,90^\circ)$ and
mean $60^\circ$. So the ambiguity is **bounded**, not unbounded, and its maximum
for a fully degenerate matrix is about $5.2^\circ$. The lesson's partially
degenerate example gave $3.50^\circ$, which sits inside that bound — as it must.

**(c) Reporting rule.** Report $H$ and $A$ as measured (they need no convention),
and report $\alpha$ together with:
1. the eigenvector convention used (in practice, the ordering that maximises
   $\alpha$ among degenerate eigenvectors);
2. the anisotropy, since a near-zero $A$ is the warning sign that a degeneracy
   exists;
3. the alternative decomposition and its residual, so a reader can see how much
   freedom the data actually leave.

That converts a number with an invisible convention into a measurement with a
stated model.
