# Solutions — 07-03-04 Gravity Inversion and Its Severe Non-Uniqueness

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [04 Gravity Inversion](../04-inversion-gravity.md).

---

## ★1 — The discrete forward problem

With three stations at offsets $x_1 < x_2 < x_3$ and two rectangular cells
($j = 1,2$) of known geometry,

$$\begin{pmatrix} d_1 \\ d_2 \\ d_3 \end{pmatrix}
= \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \\ A_{31} & A_{32}
\end{pmatrix}
\begin{pmatrix} m_1 \\ m_2 \end{pmatrix}.$$

Units: $d_i$ in $\mathrm{m\,s^{-2}}$; $m_j$ in $\mathrm{kg\,m^{-3}}$;
$A_{ij}$ in $\mathrm{m\,s^{-2}}$ per $\mathrm{kg\,m^{-3}}$, obtained by evaluating
the 2-D rectangle kernel with unit density. With $n = 3$ and $p = 2$ the problem is
formally overdetermined, and the least-squares solution is unique *as a
parameter-vector problem* — but "unique densities on this particular two-cell
grid" is not "unique Earth", which is exactly the point of the lesson.

---

## ★2 — Resolution matrix and the trace bound

$$\mathbf{R} = \left(\mathbf{A}^{\mathsf{T}}\mathbf{A}
+ \alpha\mathbf{D}^{\mathsf{T}}\mathbf{D}\right)^{-1}\mathbf{A}^{\mathsf{T}}\mathbf{A},
\qquad
\mathrm{trace}(\mathbf{R}) =
\sum_i \frac{\lambda_i}{\lambda_i+\alpha\mu_i},$$

where $\lambda_i$ are the eigenvalues of $\mathbf{A}^{\mathsf{T}}\mathbf{A}$ and
$\mu_i$ those of $\mathbf{D}^{\mathsf{T}}\mathbf{D}$ in the same basis. Each term
is between 0 and 1, so $\mathrm{trace}(\mathbf{R}) \le p$; and because each term
also counts the number of data-supported directions, in practice
$\mathrm{trace}(\mathbf{R}) \le n$ as well — a direction with no data cannot be
resolved no matter what the penalty does. The demonstration measures
$45.9$ for $p = 246$ and $n = 61$: the data support fewer than $61$ parameters
because the kernels are highly correlated.

---

## ★3 — Two indistinguishable distributions

1. **Sheets inside the observation surface.** Two thin sheets at depths $h_1$,
   $h_2$ with sinusoidal densities in the ratio
   $\sigma_2 = -\sigma_1e^{k(h_2-h_1)}$ produce zero net field at the surface for
   the single wavenumber $k$ (derived in ★7).
2. **Any mass distribution entirely outside the observation domain.** By
   Gauss's law a spherically symmetric shell of mass outside a measurement sphere
   exerts no field inside it; more generally, a mass distribution whose potential
   is a solution of Laplace's equation inside the observation surface contributes
   nothing to the measured field. The classic construction is to extend the mass
   beyond the survey boundary: the field inside is unchanged, the mass is not.

Both are exact (not approximate) statements, and they are the reason the admitted
set in the lesson's aperture table is non-empty.

---

## ★4 — Choosing the regularisation

Requirements: the misfit should not fall well below the stated noise, because that
is fitting noise; and the model should not be so smooth that real structure is
invisible.

From the table:

| $\alpha$ | rms misfit (mGal) | comment |
|---|---|---|
| $10^{-6}$ | 0.0109 | below the $0.02\ \mathrm{mGal}$ noise — over-fitting |
| $10^{-5}$ | 0.0115 | still below the noise |
| $10^{-4}$ | 0.0139 | below the noise |
| $10^{-3}$ | 0.0277 | **just above the noise** |
| $10^{-2}$ | 0.3857 | 19$\times$ the noise — under-fitting |

**Choice: $\alpha = 10^{-3}$**, the smallest value whose misfit is *not* smaller
than the stated noise. The demonstration shows that this choice also brings the
mass centre down to $736.7\ \mathrm{m}$, close to the true $700.0\ \mathrm{m}$,
while smaller $\alpha$ places it at $230$–$300\ \mathrm{m}$ — a concrete instance
of the general rule that the discrepancy principle selects a more truthful model
than the minimum-misfit solution. Note that the criterion, not the number, is the
defensible part of the answer.

---

## ★5 — Mass and the admitted set

Point-mass mass at $1000\ \mathrm{m}$ for $0.30\ \mathrm{mGal}$:

$$M = \frac{g z^{2}}{G}
= \frac{3.0\times10^{-6}\times10^{6}}{6.67430\times10^{-11}}
= 4.495\times10^{10}\ \mathrm{kg}.$$

With a $1\ \mathrm{km}$ aperture and $0.02\ \mathrm{mGal}$ noise the lesson's
table gives depth $919$–$1099\ \mathrm{m}$ and mass
$1.72$–$2.38\times10^{11}\ \mathrm{kg}$ **for a $2.0\times10^{11}\ \mathrm{kg}$
source**. Rescaling to the $4.495\times10^{10}\ \mathrm{kg}$ source at the same
depth, the ranges scale linearly with mass:

- depth $919$–$1099\ \mathrm{m}$ (independently of the mass scale, because it is
  set by the profile shape);
- mass $3.9$–$5.3\times10^{10}\ \mathrm{kg}$, a factor $1.38$ — the same factor as
  the table's $1.38$, as expected.

---

## ★6 — Where resolution falls below 0.1

| layer (m) | mean $\mathrm{diag}(\mathbf{R})$ |
|---|---|
| 100–200 | 0.5446 |
| 200–400 | 0.3812 |
| 400–800 | 0.1090 |
| 800–1600 | 0.0423 |

The threshold $0.1$ is crossed between the $400$–$800\ \mathrm{m}$ layer
($0.1090$) and the $800$–$1600\ \mathrm{m}$ layer ($0.0423$), i.e. at roughly
$800\ \mathrm{m}$ — essentially the depth of the true body's centre ($700\
\mathrm{m}$).

**Physical reason.** The unit-density kernel of a cell at depth $z$ has amplitude
$\propto z^{-2}$ and width $\propto z$, so its contribution to the data falls
roughly as $z^{-2}$ while its overlap with neighbouring cell kernels grows. Put
differently, the data can distinguish two nearby shallow cells but not two nearby
deep ones: the deep cells are nearly linearly dependent columns of
$\mathbf{A}$, and the regularisation resolves the ambiguity by suppressing them.

---

## ★7 — The annihilator condition, and a $500\ \mathrm{m}$ wavelength

For a thin sheet at depth $h$ with $\sigma(x) = \sigma_0\cos kx$:

$$g_z(x) = 2\pi G\sigma_0\cos(kx)e^{-kh}.$$

Two sheets cancel when

$$\sigma_1e^{-kh_1} + \sigma_2e^{-kh_2} = 0
\;\Longrightarrow\;
\frac{\sigma_2}{\sigma_1} = -e^{k(h_2-h_1)} .$$

The required amplitude ratio is $e^{k\Delta h}$, which grows **exponentially** in
the depth separation and in $k$: deeper and shorter-wavelength annihilators demand
increasingly extreme amplitudes.

**Numbers:** $k = 2\pi/500 = 1.2566\times10^{-2}\ \mathrm{m^{-1}}$,
$\Delta h = 2000\ \mathrm{m}$, so

$$e^{k\Delta h} = e^{25.13} = 8.2\times10^{10}.$$

A $2\ \mathrm{km}$-deeper sheet would need to carry $8.2\times10^{10}$ times the
surface density of the first to cancel it at that wavelength. The lesson's
$500\ \mathrm{m}$ wavelength and $800\ \mathrm{m}$ separation gives
$e^{5.03} = 152.4$, which is large but physically imaginable; the $2\ \mathrm{km}$
version is a mathematical statement more than a geological one. **This is the
practical content of "the null space has structure": shallow annihilators are
mild, deep ones are enormous, and that is why depth weighting works at all.**

---

## ★8 — Reducing the admitted mass range to below $1.3$

The lesson's table bounds what geometry alone can buy:

| aperture (m) | mass factor |
|---|---|
| 500 | 3.19 |
| 1000 | 1.38 |
| 2000 | 1.16 |
| 8000 | 1.22 |

Even an $8\ \mathrm{km}$ aperture leaves $1.22$, so **geometry alone cannot reach
$1.3$ everywhere but can beat it beyond about $1.5\ \mathrm{km}$ aperture at
$0.02\ \mathrm{mGal}$ noise** — the $2000\ \mathrm{m}$ row already gives $1.16$.
The scheme:

1. **Aperture $\ge 2\ \mathrm{km}$** on both sides of the source (about twice the
   source depth), stations at $25$–$50\ \mathrm{m}$ spacing on the flanks where
   the curvature lives.
2. **Noise $\le 0.02\ \mathrm{mGal}$ rms**, achieved by repeat readings at each
   station and a drift protocol; the mass factor scales roughly linearly with
   noise, so doubling the noise doubles the admitted range.
3. **Model shape fixed to a compact body** for the admitted-set calculation;
   allowing a dyke re-opens the shape ambiguity of
   [01](../01-anomaly-interpretation.md) ($\sim30\%$ in depth).
4. **Additional assumption forced:** if a factor below $1.3$ is required at a
   smaller aperture, the only remaining lever is a prior — a density contrast
   range from petrophysics, a drilling constraint, or an independent
   measurement — because the data themselves cannot exclude the family. Stating
   which prior and how much it binds is the honest form of the answer.
