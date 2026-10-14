# Solutions — 08-01-02 The Geocentric Dipole, IGRF and WMM Models

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [02 The Geocentric Dipole, IGRF and WMM Models](../02-dipole-and-igrf.md).

---

## ★1 — Inclination and latitude

$$\tan I = 2\tan\lambda \quad\Longrightarrow\quad
I = \arctan(2\tan\lambda), \qquad
\lambda = \arctan\!\left(\tfrac{1}{2}\tan I\right).$$

| $\lambda$ (°) | $2\tan\lambda$ | $I$ (°) |
|---|---|---|
| 20 | 0.727940 | 36.0524 |
| 35 | 1.400835 | 54.4785 |
| 70 | 5.494951 | 79.6859 |

For $I = 55.0^{\circ}$: $\tan I = 1.428148$, so
$\tan\lambda = 0.714074$ and $\lambda = 35.5296^{\circ}$.

Note the round trip: the $\lambda = 35^{\circ}$ row gives $I = 54.4785^{\circ}$,
close to but distinct from $55.0^{\circ}$ — the mapping is monotone but not
linear.

---

## ★2 — Components at $\lambda = 60^{\circ}$

$\theta = 90^{\circ}-60^{\circ} = 30^{\circ}$, so
$\sin\theta = \cos\lambda = 0.5$ and $\cos\theta = \sin\lambda = 0.866025$.

$$X = -g_1^0\sin\theta = 30000\times0.5 = 15000.0\ \mathrm{nT},$$
$$Z = -2g_1^0\cos\theta = 2\times30000\times0.866025 = 51961.5\ \mathrm{nT},$$
$$F = \sqrt{X^2+Z^2} = \sqrt{2.25\times10^{8} + 2.7\times10^{9}}
= \sqrt{2.925\times10^{9}} = 54083.25\ \mathrm{nT}.$$

The demonstration's table gives $X = 15000.0\ \mathrm{nT}$,
$Z = 51961.5\ \mathrm{nT}$, $I = 73.8979^{\circ}$. Check the inclination:
$\arctan(51961.5/15000.0) = \arctan(3.46410) = 73.8979^{\circ}$. ✔ And
$I = \arctan(2\tan 60^{\circ}) = \arctan(3.46410)$, the same number. ✔

---

## ★3 — Radial factors

Field radial dependence at degree $n$: $(a/r)^{n+2}$.

$$r = 6371 + 600 = 6971\ \mathrm{km}, \qquad a/r = 0.913928.$$

| degree $n$ | exponent $n+2$ | $(a/r)^{n+2}$ |
|---|---|---|
| 1 | 3 | 0.763374 |
| 4 | 6 | 0.582740 |

So a degree-4 feature retains 58.27% of its surface amplitude at 600 km, against
76.34% for the dipole: the higher degrees die faster, which is exactly why
satellite surveys at altitude are blind to short-wavelength crustal fields.

---

## ★4 — Recovering the dipole coefficient

At the dipole equator $\lambda = 0$, so $X = -g_1^0(a/r)^3$ and $F = |X|$:

$$F = |g_1^0|\left(\frac{a}{r}\right)^3
= |g_1^0|\left(\frac{6371}{6771}\right)^3 = |g_1^0|\times0.833037,$$

$$|g_1^0| = \frac{24991.11}{0.833037} = 30000.0\ \mathrm{nT}.$$

The number assumed is the **reference radius** $a = 6371\ \mathrm{km}$ (and,
implicitly, that the field is purely axial at that instant). A different $a$
gives a different coefficient for the same field: $g_1^0$ and $a$ are not
separately determined by field values alone.

---

## ★5 — Coefficient counts

Degree $n$ contributes $2n+1$ coefficients ($g_n^0$, and $g_n^m, h_n^m$ for
$1\le m\le n$). So

$$\sum_{n=1}^{N}(2n+1) = N(N+2).$$

- $N = 6$: $6\times8 = 48$ coefficients.
- $N = 10$: $10\times12 = 120$ coefficients.
- $N = 13$: $13\times15 = 195$ coefficients.

**Minimum degree for a 3000 km wavelength.** A harmonic of degree $n$ has angular
wavelength $2\pi/n$, so the linear wavelength at radius $r$ is

$$\Lambda = \frac{2\pi r}{n} \quad\Longrightarrow\quad
n = \frac{2\pi r}{\Lambda}
= \frac{2\pi\times6371}{3000} = 13.34.$$

A degree-13 model cannot represent it (it needs $n \ge 13.343$), so **degree 14**
is the minimum — and in practice more, because the wavelength that defines the
Nyquist limit must be sampled at least twice per wavelength.

---

## ★6 — A local fit does bias the coefficients

Least squares on $4 \times 3 = 12$ observations for 3 coefficients, using the
demonstration's synthetic coefficients, returns

| coefficient | true (nT) | fitted (nT) | bias (nT) |
|---|---|---|---|
| $g_1^0$ | −30000.00 | −30274.99 | −274.99 |
| $g_1^1$ | −1800.00 | −2317.47 | −517.47 |
| $h_1^1$ | +4800.00 | +5371.40 | +571.40 |

with an rms residual of $2081.78\ \mathrm{nT}$ against an rms field of
$24391.02\ \mathrm{nT}$ (8.5%). Every coefficient is biased by hundreds of nT —
the same order as the degree-2 coefficients themselves
($g_2^0 = 1200$, $g_2^2 = 1500\ \mathrm{nT}$).

**Why.** Over four scattered points the degree-2 functions are not orthogonal to
the degree-1 functions: the inner product $\sum_i P_1(\theta_i)P_2(\theta_i)$ is
not zero. The fit therefore spends part of the degree-2 signal on the degree-1
coefficient. Over a complete sphere with quadrature weights the same inner
product is exactly zero, which is the result the demonstration prints as
"error $0.00\ \mathrm{nT}$". **The bias is a property of the sampling, not of the
basis.**

---

## ★7 — Separating internal and external amplitudes

Write the degree-$n$ surface value $S_n(\theta,\phi)$. The two candidate
sources give, at radius $r$,

$$V^{\text{int}} = a\left(\frac{a}{r}\right)^{n+1} S_n, \qquad
V^{\text{ext}} = a\left(\frac{r}{a}\right)^{n} S_n.$$

Only the total is measured, so with observations at two radii $r_1 = a$ and
$r_2$ we have

$$\begin{pmatrix} 1 & 1 \\ (a/r_2)^{n+2} & (r_2/a)^{n-1} \end{pmatrix}
\begin{pmatrix} I \\ E \end{pmatrix} = \begin{pmatrix} F(a) \\ F(r_2) \end{pmatrix},$$

where $I$ and $E$ are the internal and external field amplitudes at $r = a$ and
the matrix entries are the radial factors of the *field* (potential factors plus
one power of $1/r$). At $n = 2$, $r_2 = 0.95a$:

$$A = \begin{pmatrix} 1 & 1 \\ 1.22774 & 0.95000 \end{pmatrix},
\qquad \det A = 0.95 - 1.22774 = -0.27774.$$

The inverse has entries of size $1/0.27774 \approx 3.6$, so the separation is
workable but not comfortable at a 5% radius difference. As $r_2\to a$ the two
columns become identical, $\det A \to 0$, and the separation becomes impossible:
**the internal/external ambiguity is exact at a single radius**, and its
removal requires a finite baseline in radius, with conditioning that degrades as
$1/|1 - r_2/a|$.

---

## ★8 — Testing a normalisation convention

**Metric.** Take $M$ field triplets at scattered points from the given
coefficient set. For each of the two hypotheses — Schmidt semi-normalised or
fully normalised — forward-compute the field and form the residual rms at those
points, after re-fitting the coefficients by least squares in each convention.

**Decision rule.** The correct convention leaves a residual at the noise level of
the data; the wrong one leaves a residual of the same order as the field itself,
because the Legendre normalisation factors differ by $\sqrt{(2-\delta_{m0})(n-m)!/(n+m)!}$,
which reaches a factor of several hundred at degree 13.

**Failure mode.** If the test points are all at degrees where the two
conventions coincide ($n\le1$, $m\le1$), both hypotheses fit and the test is
inconclusive. A second failure mode is a coefficient set that is *nearly* right
but was published in a different reference radius: the residual then looks like a
radial-scaling error rather than a normalisation error. The test therefore needs
at least one point with $n\ge2$ and must be repeated with $a$ as a free
parameter.
