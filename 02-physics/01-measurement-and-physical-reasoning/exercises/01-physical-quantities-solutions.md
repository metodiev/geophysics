# Solutions — 02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity

> **Read this after attempting the exercises, not before.**
>
> These are worked solutions: one valid route each, with arithmetic that was
> computed and checked rather than estimated. Where a problem admits more than
> one defensible answer, that is stated. Exact conversion factors are marked;
> every other number is derived here from the constants listed at the top of the
> exercise sheet.

---

## ★1 — Unit conversions

| | Given | Conversion used (exact) | In SI |
|---|---|---|---|
| (a) | 3.2 mGal | $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ | $3.2\times10^{-5}\ \mathrm{m\,s^{-2}}$ |
| (b) | 250 nT | $1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}$ | $2.5\times10^{-7}\ \mathrm{T}$ |
| (c) | 3.5 km/s | $1\ \mathrm{km\,s^{-1}} = 3600\ \mathrm{km\,h^{-1}}$ | $1.26\times10^{4}\ \mathrm{km\,h^{-1}}$ |
| (d) | $45\ \mu\mathrm{W\,m^{-3}}$ | $1\ \mu = 10^{-6}$ | $4.5\times10^{-5}\ \mathrm{W\,m^{-3}}$ |
| (e) | 0.15 m/s | $10^{3}\ \mathrm{mm\,m^{-1}}$, $3.1557\times10^{7}\ \mathrm{s\,yr^{-1}}$ | $4.7336\times10^{9}\ \mathrm{mm\,yr^{-1}}$ |

**Sanity check on (e).** 0.15 m/s is fast for a geological process
(≈ 4.7 × 10⁹ mm/yr); the unit change explains why geologists never write plate
velocities in m/s. **Sanity check on (c).** 3.5 km/s is a modest P-wave speed,
and 1.26 × 10⁴ km/h is about ten times the speed of a passenger aircraft — a
useful way to feel the number.

---

## ★2 — Significant figures and status

| | Value | s.f. | Status | Why |
|---|---|---|---|---|
| (a) | `6371 km` | 4 (as written) | **nominal** | the Earth is not a sphere; the value is a mean radius, and writing `6.371 × 10³ km` removes the ambiguity |
| (b) | `6.674 30 × 10⁻¹¹` | 6 | **measured** | CODATA value of $G$, relative uncertainty $2.2\times10^{-5}$; the last digit is meaningful only with the uncertainty quoted |
| (c) | `1 mGal = 10⁻⁵ m s⁻²` | exact | **exact (defining)** | the Gal is defined as $10^{-2}$ m s⁻²; no measurement is involved |
| (d) | `9.806 65 m/s²` | 6 | **exact (defining)** | standard gravity, fixed by convention |
| (e) | `3300 kg/m³` | 2–4 (ambiguous) | **nominal** | a representative mantle density spanning thousands of kg m⁻³ |

**Key point.** (b) and (d) look alike and are not: $G$ is measured, $g_n$ is
defined. Quoting $G$ to 6 figures *without* its uncertainty is a provenance
error, while quoting $g_n$ with an uncertainty is a misunderstanding of the SI.

---

## ★3 — Homogeneity checks

Using $(M,L,T)$ for the dimension vectors.

| | Left side | Right side | Verdict |
|---|---|---|---|
| (a) | $[v^{2}] = L^{2}T^{-2}$ | $[2gh] = (LT^{-2})(L) = L^{2}T^{-2}$ | homogeneous |
| (b) | $[p] = ML^{-1}T^{-2}$ | $[(ML^{-3})(LT^{-2})(L)] = ML^{-1}T^{-2}$ | homogeneous |
| (c) | $[q] = MT^{-3}$ | $[(W\,m^{-1}K^{-1})(K\,m^{-1})] = (MLT^{-3}K^{-1})(K\,L^{-1}) = MT^{-3}$ | homogeneous |
| (d) | $[E] = ML^{2}T^{-2}$ | $[(M)(L^{2}T^{-2})] = ML^{2}T^{-2}$ | homogeneous |
| (e) | $[\omega] = T^{-1}$ | $[\sqrt{g/L}] = \sqrt{LT^{-2}/L} = T^{-1}$ | homogeneous |
| (f) | $[v_p] = LT^{-1}$ | $[\sqrt{\mu/\rho}] = \sqrt{ML^{-1}T^{-2}/(ML^{-3})} = LT^{-1}$ | homogeneous |

Note that (c) is the one students most often get wrong: the conductivity $k$ has
a length in its denominator, and the temperature *gradient* has one in its own
denominator, so the two lengths cancel and no length survives in a heat flux.
That cancellation is the physics: a flux density does not depend on the size of
the sample.

---

## ★4 — Dimensions from defining equations

**(a) Seismic moment.** $[M_0] = [\mu][A][D]
= (ML^{-1}T^{-2})(L^{2})(L) = ML^{2}T^{-2}$ — the dimension of energy.

**(b) Hydraulic conductivity.** From $\mathbf{v} = -K\nabla h$, where $h$ is a
head (length) so $[\nabla h] = 1$ (dimensionless):
$[K] = [\mathbf{v}]/[\nabla h] = LT^{-1}$. **$K$ has the dimension of a
velocity**, which is why it is called "hydraulic conductivity" and reported in
m/s while the intrinsic permeability $k$ is reported in m². The ratio is
$K = k\rho g/\mu$, a velocity by construction.

**(c) Eötvös.** $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$, the dimension of a
gravity gradient; numerically $1\ \mathrm{E} = 10^{-4}$ mGal/m because
$10^{-9}\ \mathrm{s^{-2}} = 10^{-9}/10^{-5}$ mGal/m, where the division by 1 m is
implicit in "per metre".

**(d) Surface heat flow.** $\mathrm{W\,m^{-2}} = ML^{2}T^{-3}/L^{2} = MT^{-3}$.

**(e) Magnetic dipole moment.** From $B = \mu_0 m/(4\pi r^{3})$, with
$[B] = MT^{-2}I^{-1}$ and $[\mu_0] = MLT^{-2}I^{-2}$:
$[m] = [B][r^{3}]/[\mu_0] = (MT^{-2}I^{-1})(L^{3})/(MLT^{-2}I^{-2}) = L^{2}I$.
So the SI unit is A m², as stated in §2.3 of the lesson.

---

## ★★5 — Surface gravity at two radii

**(a)**
$$g(6371\ \mathrm{km}) = \frac{3.986\,004\,418\times10^{14}}{(6.371\times10^{6})^{2}}
= 9.820\,250\ \mathrm{m\,s^{-2}},$$
$$g(6375\ \mathrm{km}) = \frac{3.986\,004\,418\times10^{14}}{(6.375\times10^{6})^{2}}
= 9.807\,931\ \mathrm{m\,s^{-2}}.$$

**(b)** The difference is $9.820\,250 - 9.807\,931 = 0.012\,3195\ \mathrm{m\,s^{-2}}$.
By comparison,
$$\frac{2GM}{R^{3}}\,\Delta R = (3.0828\times10^{-6})(4000)
= 1.2331\times10^{-2}\ \mathrm{m\,s^{-2}},$$
i.e. $0.012\,331$ — agreeing with the exact difference to 4 parts in 10⁴.

**(c)** They agree only approximately because the gradient used is $dg/dR$ at the
*single* radius 6371 km, whereas the true difference is the integral of
$dg/dR$ over the interval; the agreement improves as $\Delta R \to 0$, and the
residual here is the curvature term $\tfrac12g''\,\Delta R^{2}$, of order
(0.0123)(4/6371) ≈ 8 × 10⁻⁶.

---

## ★★6 — Gravity gradient and levelling

**(a)** $\dfrac{2GM}{R^{3}} = \dfrac{2(3.986\,004\,418\times10^{14})}{2.586\times10^{20}}
= 3.0828\times10^{-6}\ \mathrm{s^{-2}} = 0.308\,280\ \mathrm{mGal\,m^{-1}}$.

**(b)** $\Delta z = \dfrac{0.01\ \mathrm{mGal}}{0.308\,280\ \mathrm{mGal\,m^{-1}}}
= 3.244\times10^{-2}\ \mathrm{m}$ — about **3.2 cm**.

**(c)** A 3 cm levelling error gives $0.03 \times 0.308\,280
= 9.248\times10^{-3}$ mGal ≈ **0.0092 mGal**.

**(d)** Any other term: the Bouguer/terrain density uncertainty (typically
0.4 mGal for 100 m of relief and 100 kg m⁻³ density error), tidal-correction
residual, latitude-model residual, network adjustment. The point of the question
is that no survey is limited by its instrument until the budget says so — see
[02-01-02](../02-measurement-uncertainty.md) §7.

---

## ★★7 — The Bouguer slab

**(a)** $2\pi G = 4.1936\times10^{-10}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}\cdot
\mathrm{kg\,m^{-3}}\cdot\mathrm{m} = 4.1936\times10^{-10}\ \mathrm{m\,s^{-2}}$ per
(kg m⁻³)(m). For $\rho = 2670\ \mathrm{kg\,m^{-3}}$,
$$\frac{2\pi G\rho}{10^{-5}} = \frac{4.1936\times10^{-10}\times2670}{10^{-5}}
= 0.111\,969\ \mathrm{mGal\,m^{-1}}.$$

**(b)** With $\rho = 2.670\ \mathrm{g\,cm^{-3}}$,
$0.04193 \times 2.670 = 0.111\,953\ \mathrm{mGal\,m^{-1}}$, matching (a) to 1 part
in 7 000. The coefficient 0.04193 is just $2\pi G \times 10^{3}/10^{-5}$ in the
mixed units.

**(c)** $0.111\,969 \times 500 = \mathbf{55.98\ mGal}$.

**(d)** With $u(\rho) = 50\ \mathrm{kg\,m^{-3}}$,
$$u(\Delta g) = \frac{2\pi G\,t\,u(\rho)}{10^{-5}} = 1.048\ \mathrm{mGal},$$
i.e. ±1.05 mGal on a 56 mGal correction — a 1.9% relative error, which is
usually the dominant term in a regional gravity budget.

---

## ★★8 — Relative uncertainty of $g = GM/R^{2}$

**(a)** By the exponent rule with $p_{GM} = 1$, $p_R = -2$:
$$\frac{u(g)}{g} = \sqrt{\left(10^{-9}\right)^{2} + \left(2\times\frac{0.1}{6.371\times10^{6}}\right)^{2}}
= \sqrt{10^{-18} + (3.139\times10^{-8})^{2}} = 3.141\times10^{-8}.$$

**(b)** The radius term dominates by more than seven orders of magnitude:
$2\times0.1/6.371\times10^{6} = 3.14\times10^{-8}$ against $10^{-9}$.

**(c)** 12 significant figures implies a relative precision of $10^{-12}$, which
is 30 000 times better than the inputs support. A defensible report gives
$g$ to about 8 significant figures here, and states what the uncertainty is:
$u(g) = 3.14\times10^{-8}\times9.820\,250 = 3.08\times10^{-7}\ \mathrm{m\,s^{-2}}$.
The deeper point from the constant handbook applies: any quantity obtained by
*dividing* by $G$ is limited to about 5 significant figures, but dividing $GM$
by $R^{2}$ is limited only by the radius — which is why geodesy works in $GM$,
never in $M$.

---

## ★★★9 — Dimensionless groups by rank argument

**(a) Pendulum $T(l,g,m,\theta_0)$.** Excluding $\theta_0$ (already
dimensionless), the exponent matrix for $(l,g,T,m)$ in $(M,L,T)$ is
$$\begin{pmatrix}0&0&0&1\\1&1&0&0\\0&-2&1&0\end{pmatrix},\quad \mathrm{rank}=3,$$
so $4-3 = 1$ group: $\Pi = T\sqrt{g/l}$. **The mass drops out** because it is the
only variable carrying $M$, so no non-trivial combination containing it can be
dimensionless. Physically: the equation $m\ddot{x} = -mg\sin(x/l)$ has $m$ on
both sides.

**(b) Skin depth $\delta(\sigma,\mu_0,\omega)$.** With four variables
$(\delta,\sigma,\mu_0,\omega)$ and dimension vectors
$\delta = (0,1,0,0)$, $\sigma = (-1,-3,3,2)$,
$\mu_0 = (1,1,-2,-2)$, $\omega = (0,0,-1,0)$ in $(M,L,T,I)$, the exponent matrix
has rank **3**, not 4: the combination $\mu_0\sigma\omega$ has dimension
$(0,-2,1,0)$, so the four vectors are linearly dependent. With $n = 4$ and
$r = 3$ there is **one** group,
$$\Pi = \delta\sqrt{\mu_0\sigma\omega},
\qquad \text{so}\qquad \delta \propto \frac{1}{\sqrt{\mu_0\sigma\omega}}.$$
Check it: $[\mu_0\sigma\omega] = (M L T^{-2}I^{-2})(M^{-1}L^{-3}T^{3}I^{2})(T^{-1})
= L^{-2}$, so $\delta^{2}\mu_0\sigma\omega$ is dimensionless. The rank
argument supplies the *group*; the coefficient $\sqrt{2}$ (for the
1/e amplitude convention) comes only from the diffusion equation. That division
of labour — dimensions give the group, the equation gives the coefficient — is
the general rule.

**(c) Escape velocity $v_e(G,M,R)$.** Seven-dimensional vectors with
$\dim G = M^{-1}L^{3}T^{-2}$, $\dim M = M$, $\dim R = L$, $\dim v_e = LT^{-1}$:
rank 3 (all three of $M$, $L$, $T$ are represented), so $4-3 = 1$ group:
$\Pi = v_e\sqrt{R/(GM)}$, i.e. $v_e \propto \sqrt{GM/R}$. The coefficient
$\sqrt{2}$ requires the energy argument. Evaluating for $R = 6371$ km:
$v_e = \sqrt{2GM/R} = 11\,186\ \mathrm{m\,s^{-1}} = 11.19$ km/s.

---

## ★★★10 — Seismic moment versus energy

**(a)** $[M_0] = [\mu][A][D] = (ML^{-1}T^{-2})(L^{2})(L) = ML^{2}T^{-2} = [E]$.
Verified.

**(b)** $A = 10^{4} \times 5\times10^{3} = 5\times10^{7}\ \mathrm{m^{2}}$,
$D = 1$ m, $\mu = 3\times10^{10}$ Pa:
$$M_0 = 3\times10^{10}\times5\times10^{7}\times1 = 1.5\times10^{18}\ \mathrm{N\,m}.$$

**(c)** With $\Delta\sigma = 3\times10^{6}$ Pa and $\mu = 3\times10^{10}$ Pa:
$$\frac{E_s}{M_0} = \frac{\Delta\sigma}{2\mu} = \frac{3\times10^{6}}{6\times10^{10}}
= 5\times10^{-5}.$$

**(d)** $M_0$ is a source-strength scale: it is the product of an elastic modulus,
an area and a slip, and it controls the *amplitude* and long-period shape of the
radiated field, not its energy. Energy is a scalar that is conserved, dissipated
and converted; $M_0$ is a tensor component (in general $M_{ij}$) with sign
structure that encodes the fault geometry. A measurement that distinguishes them
is the radiated seismic energy: the far-field ground velocity record, integrated
(flux of $\rho v\dot{u}^{2}$) over the focal sphere, gives $E_s$ and yields the
ratio $E_s/M_0$ — while $M_0$ itself is obtained independently from the
low-frequency plateau of the displacement spectrum. The two numbers have the
same dimension and differ by five orders of magnitude, which is itself the
physical statement (the stress drop is a tiny fraction of the shear modulus).

---

## Self-assessment: have you actually learned this?

- [ ] I can convert between mGal, Gal and m s⁻² and between nT and T without a
      table, and say which conversions are exact.
- [ ] I can classify a constant as exact, measured or nominal and adjust my
      reporting accordingly.
- [ ] I can check a formula's homogeneity in under a minute, including the
      temperature-dimension case (★3c).
- [ ] I can derive the dimension of a quantity I have never seen from its
      defining equation (permeability, hydraulic conductivity, dipole moment).
- [ ] I know when the rank argument gives a definite number of π groups and when
      it gives none (★★★9b).
- [ ] I can compute the gravity gradient, the levelling requirement and the
      Bouguer slab correction from memory of the method, not the numbers.
