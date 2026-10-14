# Solutions — 06-06-01 The Tomography Principle: Data as Path Integrals

Exercises: [01-tomography-principle-exercises.md](01-tomography-principle-exercises.md).
All values are **SYNTHETIC**.

## ★ Foundational

**1.** $\delta T = \int \delta u\,\mathrm{d}s = 1.0\times10^{-6}\ \mathrm{s\,m^{-1}}
\times 1.20\times10^{4}\ \mathrm{m} = 1.20\times10^{-2}\ \mathrm{s} = \mathbf{12.0\ ms}$.
Units: $(\mathrm{s\,m^{-1}})(\mathrm{m}) = \mathrm{s}$.

**2.** A vertical ray stays in one column ($x = 2.55$ km is cell $i = 2$ with
$0 \le i \le 9$) and crosses all ten rows, so it spends $0.5\ \mathrm{km}$ in each
of the ten cells of that column. The entry in the cell of the top row is
$\ell/v_0 = 500\ \mathrm{m} / 4000\ \mathrm{m\,s^{-1}} =
\mathbf{1.25\times10^{-1}\ s}$; the ray has ten such non-zero entries, one per
row, and none elsewhere.

**3.** The remainder scales as $p^2$ (it is
$\int(\mathrm{d}s/v_0)\,p^2/(1+p)$). Halving the anomaly quarters it:
$4.07\times10^{-3}/4 = \mathbf{1.02\times10^{-3}\ s}$ rms, i.e. about
1.5 per cent of the datum instead of 6.06 per cent.

## ★★ Applied

**4.** The 30 unlit cells contribute at least 30 to the null-space dimension.
The measured null dimension is $100 - 89 = 11$, which is *smaller* than 30 —
so the two measurements refer to different acquisitions. For the *narrow*
aperture (30 unlit cells) the null dimension is at least 30; for the crossing
acquisition there are no unlit cells and the 11 null directions are entirely
non-local, i.e. smooth combinations of illuminated cells. The comparison is the
lesson: unlit cells are the visible part of a null space that is larger than it
looks.

**5.** $u = 1/(v_0(1+p)) = u_0/(1+p) \approx u_0(1-p)$ for small $p$, so
$\delta u \approx -u_0 p = -p/v_0$. With $p = +0.08$ and
$v_0 = 4000\ \mathrm{m\,s^{-1}}$: $\delta u = -0.08/4000 =
\mathbf{-2.0\times10^{-5}\ s\,m^{-1}}$. Faster rock is slower per metre — the
sign is negative, and forgetting it inverts the image.

**6.** Model-error ratio $= 1.81\times10^{-2}/9.74\times10^{-3} = \mathbf{1.86}$;
misfit ratio $= 2.875\times10^{-4}/2.214\times10^{-4} = \mathbf{1.30}$. Both
misfits are far below any plausible noise level (5 ms here), so they are
numerically "zero" for the purposes of model quality: the misfit measures how
well the model reproduces the 140 numbers in the data, and the model error
measures how close the model is to the truth — a different question with a
different answer, and the answer that matters for interpretation.

## ★★★ Research-oriented

**7.** Rank is limited by the number of independent crossing directions per
cell. A geometry that raises it: put **sources and receivers on all four sides of
the region** — e.g. 6 sources along the left edge and 6 along the top edge,
6 receivers along the right edge and 6 along the bottom edge, giving 144 rays
with four distinct ray families and hence a wide spread of incidence angles at
every interior cell. The directions that improve are the near-vertical ones
(rays entering from the top and leaving at the bottom), which are absent from the
horizontal cross-hole geometry and which are exactly the ones that separate
shallow from deep structure. A corner cell still cannot be fully resolved: it is
crossed by at most two families, so the rank will not reach 144 exactly; the
prediction to test is that the null dimension falls from 11 to the number of
corner and edge cells that remain degenerate.

**8.** If $R$ projects onto a $d$-dimensional null space, then
$R-I$ has $d$ unit eigenvalues and the remaining $n-d$ eigenvalues are zero at
$\lambda\to0$ (damping aside), so
$\lVert R-I\rVert_F/\sqrt{n} \approx \sqrt{d/n}$. With $d = 11$, $n = 100$:
$\sqrt{0.11} = \mathbf{0.332}$, which matches the measured 0.3317 exactly — the
floor is set by the null space, and the inversion is already at it at
$\lambda = 10^{-4}\lambda_{\max}$. It is a lower bound rather than an equality
for general $\lambda$ because damping adds bias to the $n-d$ resolved
directions, so $\lVert R-I\rVert_F/\sqrt{n}$ grows above $\sqrt{d/n}$ as
$\lambda$ rises (0.3467 at $10^{-2}$, 0.9493 at $10^{0}$ here).
