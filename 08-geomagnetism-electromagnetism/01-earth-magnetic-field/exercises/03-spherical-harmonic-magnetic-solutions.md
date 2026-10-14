# Solutions — 08-01-03 Spherical Harmonic Analysis of the Magnetic Field

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [03 Spherical Harmonic Analysis](../03-spherical-harmonic-magnetic.md).

---

## ★1 — Two Legendre values at $45^{\circ}$

Definition used here:
$P_n^m(x) = \sqrt{(2-\delta_{m0})(n-m)!/(n+m)!}\;(1-x^2)^{m/2}
\,\mathrm{d}^mP_n/\mathrm{d}x^m$, $x = \cos\theta$.

**$(n,m) = (2,2)$.** Normalisation:
$\sqrt{(2)(0!)/(4!)} = \sqrt{2/24} = 0.288675$. With $P_2(x) = (3x^2-1)/2$,
$\mathrm{d}^2P_2/\mathrm{d}x^2 = 3$, and $(1-x^2) = \sin^2\theta$, so

$$P_2^2 = 0.288675\times3\sin^2\theta = 0.866025\sin^2\theta.$$

At $\theta = 45^{\circ}$: $\sin^2 45^{\circ} = 0.5$, so
$P_2^2 = 0.433013$.

**$(n,m) = (3,1)$.** Normalisation:
$\sqrt{(2)(2!)/(4!)} = \sqrt{4/24} = 0.408248$. With $P_3(x) = (5x^3-3x)/2$,
$\mathrm{d}P_3/\mathrm{d}x = (15x^2-3)/2$, and $\sin\theta$ from
$(1-x^2)^{1/2}$:

$$P_3^1 = 0.408248\,\sin\theta\;\frac{15\cos^2\theta-3}{2}.$$

At $\theta = 45^{\circ}$: $\cos^2 = 0.5$, so $15(0.5)-3 = 4.5$,
$(4.5)/2 = 2.25$, and $0.408248\times0.707107\times2.25 = 0.649519$.

$P_3^1(45^{\circ}) = 0.649519$.

---

## ★2 — Orthogonality for $(n,m) = (2,2)$

$$\int_0^{\pi}\left[P_2^2(\cos\theta)\right]^2\sin\theta\,\mathrm{d}\theta
= \frac{2(2-\delta_{20})}{2(2)+1} = \frac{4}{5} = 0.800000.$$

The demonstration's 40-point Gauss–Legendre quadrature returns $0.800000$. ✔

Sanity check by direct integration with $P_2^2 = 0.866025\sin^2\theta$:

$$0.75\int_0^{\pi}\sin^5\theta\,\mathrm{d}\theta
= 0.75\times\frac{16}{15} = 0.8,$$

using $\int_0^{\pi}\sin^5\theta\,\mathrm{d}\theta = 16/15$. ✔

---

## ★3 — Degree-1 power

$$R_1 = 2\left[(g_1^0)^2+(g_1^1)^2+(h_1^1)^2\right]
= 2\left[(-30000)^2+(-1800)^2+(4800)^2\right]$$
$$= 2\left[9.0\times10^{8} + 3.24\times10^{6} + 2.304\times10^{7}\right]
= 2\times9.26280\times10^{8} = 1.852560\times10^{9}\ \mathrm{nT^2}.$$

The demonstration prints $1.85256\times10^{9}\ \mathrm{nT^2}$; the arithmetic
above agrees exactly.

---

## ★4 — The equatorial quadrupole term

At $\theta = 90^{\circ}$: $P_1^0 = 0$, $P_1^1 = 1$, $P_2^0 = -0.5$,
$P_2^1 = 0$ (since $P_2^1 \propto \sin\theta\cos\theta$).

**Dipole only.** $S_1 = g_1^0\cos 90^{\circ} = 0$, so $B_r = 2S_1 = 0$ and
$Z = -B_r = 0$. Also
$\mathrm{d}S_1/\mathrm{d}\theta = -g_1^0\sin\theta = 30000$, and
$X = -\left[-(a/r)^3\,\mathrm{d}S_1/\mathrm{d}\theta\right] = 30000$.

$$X = 30000.0000\ \mathrm{nT}, \quad Z = -0.0000\ \mathrm{nT}, \quad
I = -0.0000^{\circ}.$$

**Adding $g_2^0 = +1200\ \mathrm{nT}$.** $S_2 = 1200\times(-0.5) = -600\
\mathrm{nT}$, so $B_r = 3S_2 = -1800$ and $Z = +1800\ \mathrm{nT}$.

$$X = 30000.0000\ \mathrm{nT}, \quad Z = 1800.0000\ \mathrm{nT}, \quad
I = \arctan(1800/30000) = 3.4336^{\circ}, \quad F = 30053.94\ \mathrm{nT}.$$

All four numbers match the demonstration's section 2b.

**Why $X$ is unchanged.** $X \propto \mathrm{d}S/\mathrm{d}\theta$, and for the
zonal quadrupole $\mathrm{d}P_2^0/\mathrm{d}\theta = -3\sin\theta\cos\theta$,
which vanishes at the equator. The dipole's own $X$ term is
$|g_1^0|\sin 90^{\circ}$ and also unaffected by the added degree.

**Why $Z$ is three times the Legendre value.** $B_r = (n+1)(a/r)^{n+2}S_n$, and
at the surface $(a/r)^{n+2} = 1$; for $n = 2$ the factor is $3$, so
$Z = -3S_2 = -3\times(-600) = +1800\ \mathrm{nT}$. The prefactor $n+1$ is the
radial derivative of $r^{-(n+1)}$, not an arbitrary coefficient convention.

---

## ★5 — Maximum degree for a 2000 km wavelength

$$\Lambda = \frac{2\pi r}{n} \quad\Longrightarrow\quad
n = \frac{2\pi r}{\Lambda}.$$

At the surface, $r = 6371\ \mathrm{km}$:

$$n = \frac{2\pi\times6371}{2000} = 20.02 \quad\Longrightarrow\quad
N \ge 21.$$

At 400 km altitude, $r = 6771\ \mathrm{km}$:

$$n = \frac{2\pi\times6771}{2000} = 21.272 \quad\Longrightarrow\quad
N \ge 22.$$

The altitude raises the required degree slightly, but the deeper problem is that
the *amplitude* of degree 21 at 400 km is only
$(6371/6771)^{23} = 0.2465$ of its surface value — a quarter. Representing the
wavelength is not the same as detecting it.

---

## ★6 — Continuation amplitudes

Factor: $(a/r)^{n+2}$ with $n = 5$, so exponent 7.

- 400 km altitude, $r = 6771\ \mathrm{km}$: $(6371/6771)^7 = 0.652955$.
  A 20 nT measurement at altitude corresponds to

  $$F_{\text{surf}} = \frac{20}{0.652955} = 30.63\ \mathrm{nT}.$$

- 100 km altitude, $r = 6471\ \mathrm{km}$: $(6371/6471)^7 = 0.896713$.

  $$F_{100} = 0.896713\times30.63 = 27.47\ \mathrm{nT}.$$

**Noise.** At degree 13 the downward-continuation factor from 400 km to the
surface is $\left(6771/6371\right)^{15} = 2.4927$, so $1\ \mathrm{nT}$ rms of
noise becomes $2.49\ \mathrm{nT}$ rms. The signal-to-noise ratio of degree 13
therefore *falls* by a factor 2.49 while the degree-1 signal-to-noise ratio
falls by 1.20. Naive continuation to the surface is only defensible while the
amplified noise stays below the level you are willing to interpret; beyond that,
degrees must be dropped or damped, which is a statement about the model, not a
statement about the Earth.

---

## ★7 — Conditioning of the internal/external separation

The matrix with observations at $r = a$ and $r = a(1-\varepsilon)$ is

$$A = \begin{pmatrix}1 & 1\\ (1-\varepsilon)^{-(n+2)} & (1-\varepsilon)^{n-1}\end{pmatrix}.$$

Expand to first order:

$$(1-\varepsilon)^{-(n+2)} \approx 1+(n+2)\varepsilon, \qquad
(1-\varepsilon)^{n-1} \approx 1-(n-1)\varepsilon,$$

$$\det A \approx \left[1+(n+2)\varepsilon\right]\times1 - 1\times\left[1-(n-1)\varepsilon\right]
= (2n+1)\varepsilon.$$

At $n = 2$, $\varepsilon = 0.05$: $\det \approx 5\times0.05 = 0.250$. The exact
value is $-0.27774$: the first-order estimate is right to 10%, and the sign in
the exact case is negative because the two columns are ordered
internal-then-external. The magnitude is what matters.

**Scaling.** The inverse matrix has entries of order $1/[(2n+1)\varepsilon]$, so
the error in the separated amplitudes for a field error $\sigma_B$ is

$$\sigma_{I} \approx \sigma_{E} \approx \frac{\sigma_B}{(2n+1)\varepsilon}.$$

The separation is therefore *linearly* ill-conditioned in the radial baseline and
*worse* for high degree: doubling the baseline halves the error, doubling the
degree roughly halves it again. Two radii that are 5% apart in radius can
separate low degrees at a cost of about 3–10× amplification of the field error;
two radii 0.5% apart cannot separate anything.

---

## ★8 — A downward-continuation scheme (specification)

**Objective.** Fit coefficients $\{g,h\}$ up to degree $N$ by weighted least
squares to the satellite data at altitude, with a degree-dependent penalty

$$\Phi = \sum_i \frac{\left[(\mathbf{B}_{\text{obs}})_i - (\mathbf{B}_{\text{model}})_i\right]^2}{\sigma_i^2}
+ \lambda\sum_{n=1}^{N} w_n \sum_m\left[(g_n^m)^2+(h_n^m)^2\right],$$

with $w_n = \left[(a+h_{\text{obs}})/a\right]^{2(n+2)}$ so that the penalty is
applied to the field energy **at the continuation radius** and grows with degree.

**Choosing $N$.** Set $N$ by the wavelength requirement of the target region
(§5), then check that the data coverage supports every degree up to $N$: if the
spatial sampling cannot resolve degree $N$, lower it. $N$ is a data-coverage
statement, not a tuning knob.

**Choosing $\lambda$.** Sweep $\lambda$ and plot the data residual against the
continued-field energy. The corner in the L-curve is the standard choice; a
physical bound (the continued field cannot exceed the observed surface field by
more than a stated factor) is a better tie-breaker than the corner itself.

**Stopping rule.** Stop when the residual reaches the stated noise level of the
data. Continuing further fits noise, and the noise is amplified by
$(r_2/r_1)^{n+2}$ at the target radius.

**Validation test.** Split the data into two halves by longitude band, fit on
one, and predict the other. An over-continued model has a low fit residual and a
*high* prediction error on the held-out half — the signature of a model that has
absorbed noise. A second test is to continue to two nearby depths and check that
the difference field is smooth rather than dominated by the highest degrees.
