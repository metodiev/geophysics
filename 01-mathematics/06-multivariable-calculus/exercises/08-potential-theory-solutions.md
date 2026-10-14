# Solutions — 01-06-08 Potential Fields, Laplace and Poisson Equations

> **Read this after attempting the exercises, not before.**
>
> **Convention.** Throughout, $V = G\int\rho/D\,dV'$ is positive,
> $\mathbf{g} = \nabla V$, and $\nabla^2V = -4\pi G\rho$. Every sign below is tied
> to that choice.
>
> $G = 6.674\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}}$ and
> $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

---

## ★1 — A point mass

**(a)** With $M = 5.0\times10^{11}$ kg at the origin and
$\mathbf{r} = (2000,-1500,3000)$ m:

$$r = \sqrt{2000^2+1500^2+3000^2} = \sqrt{1.525\times10^{7}} = 3905.12\ \mathrm{m},
\qquad r^3 = 5.9550\times10^{10}\ \mathrm{m^3},$$

$$GM = 6.674\times10^{-11}\times5.0\times10^{11} = 33.37,$$

$$\mathbf{g} = \nabla V = -\frac{GM}{r^3}\mathbf{r}
= \left(-1.1207\times10^{-6},\ 8.4056\times10^{-7},\
-1.6811\times10^{-6}\right)\ \mathrm{m\,s^{-2}} .$$

**(b)**

$$\lvert\mathbf{g}\rvert = \frac{GM}{r^2} = \frac{33.37}{1.525\times10^{7}}
= 2.1882\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.21882\ \mathrm{mGal}.$$

**Check:** the norm of the vector in (a) is
$\sqrt{1.1207^2+8.4056^2+1.6811^2}\times10^{-6} = 2.1882\times10^{-6}$ ✓.

**(c)** Analytically, $V = GM/r$ is harmonic for $r > 0$, so $\nabla^2 V = 0$ at
that point (Section ★4 of [01-06-07](./07-vector-identities-solutions.md)). A
seven-point central-difference estimate must therefore *converge to zero*, and the
lesson's demonstration measured exactly this behaviour for the same function: the
residual fell from $7.78\times10^{-14}$ at $h = 10$ m to $7.77\times10^{-16}$ at
$h = 1$ m, a factor of 100 per decade, then hit the round-off floor near
$10^{-15}$.

---

## ★2 — The mean value property

**Statement.** For a function $u$ harmonic on a ball of radius $R$ about
$\mathbf{p}$,

$$u(\mathbf{p}) = \frac{1}{4\pi R^2}\oint_{\lvert\mathbf{r}-\mathbf{p}\rvert=R}
u\,dA .$$

**Evaluation.** Take the mass $M = 10^{12}$ kg at the origin, the test sphere
centred at $\mathbf{c} = (5000,0,0)$ m with $R = 1000$ m. Since
$\lvert\mathbf{c}\rvert - R = 4000\ \mathrm{m} > 0$, the source lies outside the
sphere, so $V = GM/D$ is harmonic on and inside it.

$$V(\mathbf{c}) = \frac{GM}{5000} = \frac{66.74}{5000} = 1.33480\times10^{-2}
\ \mathrm{m^2\,s^{-2}} .$$

The numerical sphere average (midpoint rule in $(\theta,\phi)$,
[`../code/integral_theorems_demo.py`](../code/integral_theorems_demo.py))
converged to it:

| $n$ (per angle) | sphere average | relative difference |
|---|---|---|
| 100 | $1.334853827\times10^{-2}$ | $4.03\times10^{-5}$ |
| 400 | $1.334803364\times10^{-2}$ | $2.52\times10^{-6}$ |

The residual falls by a factor of 16 for a factor of 4 in $n$ — second order, as a
two-dimensional midpoint rule on a smooth integrand should be. **The mean value
property holds, and the demonstration also shows that it fails for
$f = x^2+y^2+z^2$ (whose Laplacian is 6): the average over a unit sphere is
$R^2 = 1$ while the centre value is 0.** So it is a test of harmonicity, not a
general property of averages.

**Why this is the engine of uniqueness.** The property says a harmonic function
cannot have a local extremum in the interior: at any interior point the value is
the average of its neighbours, so it cannot exceed all of them. Hence the maximum
principle, and hence uniqueness of the Dirichlet problem (★★5).

---

## ★3 — A uniform ball

**(a)**

$$M = \frac{4}{3}\pi\rho a^3 = \frac{4}{3}\pi(2800)(400)^3
= 7.5063\times10^{11}\ \mathrm{kg}.$$

**(b)**

$$g_{\text{surface}} = \frac{GM}{a^2} = \frac{(6.674\times10^{-11})
(7.5063\times10^{11})}{1.6\times10^5}
= 3.1311\times10^{-4}\ \mathrm{m\,s^{-2}} = 31.311\ \mathrm{mGal}.$$

Alternatively, and more directly, $g_{\text{surface}} = \tfrac{4}{3}\pi G\rho a =
\tfrac{4}{3}\pi(6.674\times10^{-11})(2800)(400)$ — the same expression with $M$
substituted, which is a useful check that no factor has been lost.

**(c)** Inside a uniform ball, Gauss's law with the sphere of radius $r$ gives
$g(r) = \tfrac{4}{3}\pi G\rho r = 7.8289\times10^{-7}\,r\ \mathrm{s^{-2}}$:

| $r$ (m) | $g$ (m/s²) | $g$ (mGal) |
|---|---|---|
| 200 | $1.56554\times10^{-4}$ | 15.655 |
| 100 | $7.82768\times10^{-5}$ | 7.828 |

The field is exactly linear in $r$, halving when $r$ halves ✓.

**(d)**

$$V(0) - V(a) = \frac{2}{3}\pi G\rho a^2
= \frac{2}{3}\pi(6.674\times10^{-11})(2800)(400)^2
= 6.2621\times10^{-2}\ \mathrm{m^2\,s^{-2}} .$$

The potential is *larger* at the centre than at the surface (the centre is deeper
in the well). As a check, $V(a) = GM/a = 1.2527\times10^{-1}$ m²/s² and
$V(a) - [V(0)-V(a)] = 0.125243 - 0.062621 = 6.2622\times10^{-2}$ m²/s², which should equal $\tfrac{4}{3}\pi G\rho a^2 - \tfrac{2}{3}\pi G\rho a^2 = \tfrac{2}{3}\pi G\rho a^2 = 6.2622\times10^{-2}$ m²/s² ✓ consistent, and $V(0)/V(a) = 1.5$ as required for a uniform sphere.

**(e)** Surface gravity is proportional to $\rho a$ (from $g = \tfrac{4}{3}\pi G\rho a$),
so the relative uncertainty is

$$\frac{\sigma_g}{g} = \sqrt{\left(\frac{\sigma_\rho}{\rho}\right)^2
+ \left(\frac{\sigma_a}{a}\right)^2}
= \sqrt{(0.01)^2 + \left(\frac{5}{400}\right)^2}
= \sqrt{10^{-4} + 1.5625\times10^{-4}} = 1.6\% .$$

So $\sigma_g = 0.016 \times 31.311 = 0.50$ mGal, and the answer should be reported
as

$$g_{\text{surface}} = 31.3 \pm 0.5\ \mathrm{mGal},$$

that is **three significant figures with the last digit uncertain**. Reporting
`31.31 mGal` implies a precision the inputs do not support; reporting `31 mGal`
discards real information. The radius uncertainty (1.25 %) dominates the density
uncertainty (1 %), which is worth noticing: for a compact body it is usually the
*geometry* that limits the answer.

---

## ★4 — The Bouguer slab

Start from the infinite sheet result $g_z = 2\pi G\sigma$ for an areal density
$\sigma$. A slab of thickness $t$ and volume density $\rho$ is a stack of sheets,
each of thickness $dz$ with $\sigma = \rho\,dz$, and because the sheet result is
independent of height, the contributions add without any geometric factor:

$$g_z = \int_0^t 2\pi G\rho\,dz = 2\pi G\rho t .$$

Numerically, with $\rho = 2500\ \mathrm{kg\,m^{-3}}$ and $t = 200$ m:

$$g_z = 2\pi(6.674\times10^{-11})(2500)(200) = 2.0967\times10^{-4}\ \mathrm{m\,s^{-2}}
= 20.967\ \mathrm{mGal}.$$

**Why it is independent of the observation height** is the physical content of the
infinite-sheet result: raising the station reduces the attraction from each small
element (as $1/D^2$) but brings more of the sheet into a given solid angle, and in
the limit the two effects cancel exactly. For a *finite* sheet they do not cancel,
which is the quantitative content of the exercise
[01-06-05](./05-line-surface-integrals-solutions.md), ★★6: a disk must be about
100 times wider than the height to be within 1 % of the infinite-sheet value.

---

## ★★5 — Uniqueness of the Dirichlet problem

**Claim.** $\nabla^2u = 0$ in $\Omega$, $u = f$ on $\partial\Omega$ has at most
one solution.

**Proof.**

1. Suppose $u_1$ and $u_2$ are two solutions, and set $w = u_1 - u_2$. By
   linearity $\nabla^2w = 0$ in $\Omega$, and $w = f - f = 0$ on
   $\partial\Omega$.
2. Apply **Green's first identity** (derived from the divergence theorem in
   [01-06-06](./06-integral-theorems-solutions.md), ★★6) with
   $\phi = \psi = w$:

$$\iiint_\Omega\left(\lvert\nabla w\rvert^2 + w\,\nabla^2w\right)dV
= \oint_{\partial\Omega}w\,\frac{\partial w}{\partial n}\,dA .$$

3. The $\nabla^2w$ term vanishes by harmonicity, and the boundary term vanishes
   because $w = 0$ on $\partial\Omega$. Hence
   $\iiint_\Omega\lvert\nabla w\rvert^2\,dV = 0$.
4. The integrand $\lvert\nabla w\rvert^2$ is non-negative everywhere, so its
   integral can vanish only if $\nabla w = \mathbf{0}$ at every point of $\Omega$.
5. Therefore $w$ is constant on $\Omega$ (which is connected), and the boundary
   condition forces that constant to be 0. So $u_1 = u_2$. $\square$

**The two ingredients** are (i) the divergence theorem expressed as Green's first
identity, which converts the differential equation into a boundary statement, and
(ii) the **positivity** of a squared gradient, which is what makes a vanishing
integral imply a vanishing integrand. Nothing about the shape of $\Omega$, the
smoothness of $f$, or the size of the domain is used. The only regularity needed
is that $u \in C^2(\Omega)\cap C^1(\bar\Omega)$.

**What the theorem does not say.** It says the *harmonic function in the region* is
unique given boundary data. It says nothing about the mass distribution that
produced those boundary values, because:

- the sources lie **outside** the harmonic region (below the surface), so they are
  not constrained by a theorem about the interior;
- the boundary data are the sum of the effects of all the sources, and many
  different distributions produce the same sum;
- an entire infinite-dimensional family of source distributions — the null space
  of the forward operator — produces exactly the same boundary values.

Concretely: the theorem guarantees that the gravity field *above* a survey is
determined by the surface data, and it guarantees that this field was produced by
*some* density distribution. It is silent on which one. ★★★9 exhibits two.

---

## ★★6 — Equivalent strata

**(a)** Let the data be $g_z(x,y)$ on the plane $z=0$ and let the model be an areal
density $\sigma(x,y)$ on the plane at depth $h$. The vertical attraction of a sheet
is a convolution with the kernel $K_h(x,y) = h/2\pi(x^2+y^2+h^2)^{3/2}$ times
$2\pi G$ — equivalently, in the two-dimensional wavenumber domain,

$$\tilde{g}(k_x,k_y) = 2\pi G\,e^{-\lvert k\rvert h}\,\tilde{\sigma}(k_x,k_y),
\qquad \lvert k\rvert = \sqrt{k_x^2+k_y^2},$$

so

$$\tilde{\sigma}(k_x,k_y) = \frac{\tilde{g}(k_x,k_y)}{2\pi G\,
e^{-\lvert k\rvert h}} = \frac{\tilde{g}(k_x,k_y)}{2\pi G}\,e^{\lvert k\rvert h}.$$

**(b)** The exponential $e^{-\lvert k\rvert h}$ is **never zero** for any finite $h$
and any real $k$, so the division is always possible and a solution exists for
every $h > 0$. There is no depth at which the data "cannot" be explained by a
surface density. The exponential *does* tend to zero as $\lvert k\rvert\to\infty$,
which is why the required $\tilde\sigma$ grows at high wavenumber for large $h$ —
the rough edge of the statement, and the reason the family is not a practical
family of models but a mathematical one.

**(c)** For two depths $h_1 < h_2$, the required densities satisfy

$$\frac{\tilde\sigma_{h_1}(k)}{\tilde\sigma_{h_2}(k)}
= e^{\lvert k\rvert(h_1 - h_2)} \le 1,$$

with equality only at $k=0$. So $\tilde\sigma_{h_1} \le \tilde\sigma_{h_2}$ at
every nonzero wavenumber with strict inequality, and the ratio falls off
exponentially in $\lvert k\rvert$. **The shallower stratum ($h_1$) requires the
smoother density**; the deeper one requires a density with more high-wavenumber
content, which is the same amplification that makes downward continuation
unstable. A concrete instance is verified numerically in Section 5.7 of the
lesson: a smooth sheet at 500 m reproduces the field of a point mass at 2000 m to
a relative accuracy of about $10^{-6}$.

**(d)** **No physical information distinguishes them, from gravity data alone.** By
construction, both strata produce the *same* field everywhere above the shallower
plane, so no measurement there — of any precision, at any wavelength — can
separate them. Their difference is a nonzero source distribution whose external
field vanishes identically above the survey: an annihilator of the forward
operator.

What breaks it is information *not* in the gravity data: a measured or assumed
density, an independent geometry from seismic or drilling, a physical bound on
what is geologically possible, or a joint inversion with a method that responds to
something other than mass. **Reporting a single model without stating which
constraint selected it presents a choice as a result.**

---

## ★★7 — An Airy isostatic root

**(a)** Airy isostasy balances the mass of the mountain against the mass of the
root: the mountain replaces air with crust over height $H$, and the root replaces
mantle with crust over thickness $t$. Per unit area,

$$H\rho_c = t\left(\rho_m - \rho_c\right)
\qquad\Longrightarrow\qquad
t = \frac{H\rho_c}{\rho_m - \rho_c}.$$

**(b)** With $H = 2000$ m, $\rho_c = 2800$, $\rho_m = 3300$:

$$t = \frac{(2000)(2800)}{500} = 11200\ \mathrm{m} = 11.2\ \mathrm{km}.$$

Each metre of mountain requires 5.6 m of root, so the root is 5.6 times the
topography — the standard "root thickening ratio" for these densities.

**(c)** The mass deficit per unit area of the root is

$$t\left(\rho_m-\rho_c\right) = 11200 \times 500 = 5.6\times10^{6}\ \mathrm{kg\,m^{-2}},$$

which equals the mountain's excess $H\rho_c = 2000\times2800 =
5.6\times10^{6}\ \mathrm{kg\,m^{-2}}$ ✓ — the balance condition, verified
numerically. Expressed as an equivalent thickness of displaced mantle,

$$\frac{5.6\times10^{6}}{3300} = 1697\ \mathrm{m}.$$

**(d)** The gravity anomaly over a perfectly compensated mountain is small because
**the attraction of the mountain is almost exactly cancelled by the attraction of
the mass deficit in its root**: the two are equal in mass per unit area and
differ only in their vertical distribution. What survives is the second-order
difference in how that mass is distributed with depth, which is why isostatic
residual anomalies are small and require careful reduction before they can be
interpreted. **The compensation is the geological statement; the small residual
is the geophysical one.**

---

## ★★8 — An interior maximum of a residual anomaly

**(a)** The result is the **maximum principle**: a non-constant harmonic function on
a bounded region attains its maximum and minimum on the boundary, never in the
interior. Its hypothesis is that the function is harmonic — $\nabla^2u = 0$ — on
the whole region interior being considered, and continuous up to the boundary.

**(b)** The hypothesis is satisfied in the **measurement region** above the
surface, because that region contains no mass and the gravitational potential is
therefore harmonic there. It is *not* satisfied in the region containing the
sources, because $\nabla^2V = -4\pi G\rho \neq 0$ inside and near a density
contrast. **The distinction matters because the maximum principle applies to the
source-free region only.** Applying it to the region containing the sources — or
to the measured field considered in the absence of any source model — is applying
a theorem whose hypothesis fails, and the conclusion is not merely unproved but
false.

**(c)** An interior maximum is *expected* over a dense body, and there is no
contradiction: the maximum principle constrains the **potential** in the
source-free region, whereas an anomaly map shows a **residual** of the measured
field, which is not a harmonic quantity in that sense. More precisely, the
potential above the surface has no interior maximum, but the *anomaly*
$g_z$ over a dense 3-D body does — because the body lies below the surface and the
surface itself is the boundary of the harmonic region. The maximum of a harmonic
function on the region outside the Earth occurs on the boundary of that region,
which includes the parts of the surface above the body; an interior maximum *of the
map* is a maximum of the boundary values, not an interior maximum of the harmonic
function. **Getting this straight is the difference between using the maximum
principle as a consistency check and misusing it as a prohibition.**

As an aside, the correct statement about an anomaly map is that a harmonic field
in a source-free half-space cannot have a local maximum *anywhere* that is sharper
than its behaviour at infinity — which is why every anomaly must vanish at great
distance. The apparent interior maximum over a body is a consequence of the body
lying in the other half-space.

**(d)** Measurements that discriminate shallow compact from deep broad sources:
**gravity gradients** (second derivatives decay as $r^{-3}$ against the field's
$r^{-2}$, so the tensor weights near-surface mass more heavily by the factor
computed in [01-01](./01-partial-derivatives-solutions.md) ★★★10); **the
amplitude-to-wavelength ratio**, since a compact body produces a narrower anomaly
than a deep one of the same mass; **the half-width**, which scales with depth for
a family of similar shapes; and **an independent depth constraint** from seismic
travel times, drill hole intersections, or the power spectrum of the anomaly
(which has a characteristic slope set by source depth). The textbook scaling rules
for spheres, cylinders and dykes are in
[07-03-01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](../../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md).

---

## ★★★9 — Reproducing the non-uniqueness numerically

**Method.** Direct three-dimensional volume quadrature of
$V = G\int\rho/D\,dV'$ and $g_z = -G\int\rho\,(z - z')/D^3\,dV'$ on an
$n\times n\times n$ spherical grid, for four bodies of total mass
$M = 1.570796\times10^{12}$ kg, observed at $(1200,800,1400)$ m
($\lvert\mathbf{r}\rvert = 2009.975$ m). The shell used
$400\ \mathrm{m} < r < 500$ m. No step of the quadrature uses Newton's shell
theorem.

**(a)–(b)** Measured at $n = 160$:

| model | $\rho$ (kg/m³) | $V$ (m²/s²) | $g_z$ (m/s²) | $\Delta V/V$ vs point mass | $\Delta g_z/g_z$ |
|---|---|---|---|---|---|
| point mass at origin | — | $5.2157335475\times10^{-2}$ | $-1.8074324174\times10^{-5}$ | — | — |
| uniform ball, $a = 500$ m | 3000.0 | $5.2157670481\times10^{-2}$ | $-1.8074427534\times10^{-5}$ | $+6.4\times10^{-6}$ | $+5.7\times10^{-6}$ |
| uniform ball, $a = 300$ m | 13888.9 | $5.2157666449\times10^{-2}$ | $-1.8074434509\times10^{-5}$ | $+6.3\times10^{-6}$ | $+6.1\times10^{-6}$ |
| shell, $400 < r < 500$ m | 6147.5 | $5.2158173806\times10^{-2}$ | $-1.8074596912\times10^{-5}$ | $+1.6\times10^{-5}$ | $+1.5\times10^{-5}$ |

All four agree to a relative $10^{-5}$ or better.

**(c)** Refining the spherical grid, the point-mass value converges as:

| $n$ | $V$ | relative error vs $GM/r$ | $g_z$ | relative error |
|---|---|---|---|---|
| 60 | $5.2159717809\times10^{-2}$ | $4.57\times10^{-5}$ | $-1.8075059147\times10^{-5}$ | $4.07\times10^{-5}$ |
| 120 | $5.2157931043\times10^{-2}$ | $1.14\times10^{-5}$ | $-1.8074507924\times10^{-5}$ | $1.02\times10^{-5}$ |
| 200 | $5.2157549878\times10^{-2}$ | $4.11\times10^{-6}$ | $-1.8074390325\times10^{-5}$ | $3.66\times10^{-6}$ |

The error falls by a factor of about 4 whenever the resolution doubles — second
order — and the difference between the models is *smaller than or comparable to
the quadrature error* at every resolution tried. **This is itself the finding: the
discrepancy between physically different source distributions is at or below the
level of the numerical error, so the models are indistinguishable at the accuracy
achieved.** To make the ambiguity sharper, more resolution or a purpose-built
annihilator (as in Section 5.7 of the lesson) is needed.

**(d)** No improvement in instrument precision can separate (i) from (iv), because
they are not merely similar: their external fields are **identical**, to the
accuracy of the computation, by Newton's shell theorem — any spherically symmetric
body produces exactly the point-mass field outside itself. The residual
differences in the table ($10^{-5}$) are quadrature error and shrink with
resolution; the true difference is zero.

An instrument with infinite precision measures the same number for both. To
separate them requires information that is not the external field: a density
measurement within the body, a gradient measurement (which is still generated by
the same potential, so it too is identical — no help here), or an independent
geometric or geological constraint. **Precision is not the limiting factor;
information is.**

---

## ★★★10 — Continuation, stability and non-uniqueness

**(a)** Upward continuation by a height $h$ multiplies the wavenumber spectrum by
$e^{-\lvert k\rvert h}$, which is $\le1$ and decreases with $\lvert k\rvert$:

- **smoothing:** the amplitude of every wavelength is reduced, and the shortest
  wavelengths are reduced most;
- **stable:** the multiplicative factor is bounded by 1, so the operator's norm is
  at most 1 and no noise is amplified. The continuation of two datasets differing
  by $\delta$ differ by at most $\delta$.

Physically, upward continuation is the same operation as observing the field from
further away, and the field of a source is smoother at greater distance.

**(b)** Downward continuation by a depth $d$ multiplies by $e^{+\lvert k\rvert d}$:

- **growth:** the factor is unbounded as $\lvert k\rvert\to\infty$, so the operator
  is not bounded and the problem is ill-posed;
- the **amplification factor** at wavenumber $k$ is $e^{\lvert k\rvert d}$;
- in terms of wavelength $\lambda$, $\lvert k\rvert d = 2\pi d/\lambda$, so short
  wavelengths are amplified as $e^{2\pi d/\lambda}$.

**(c)** Setting the amplification at the shortest resolved wavelength
$\lambda_{\min}$ equal to $10^{3}$:

$$e^{2\pi d/\lambda_{\min}} = 10^{3}
\qquad\Longrightarrow\qquad
d = \frac{\lambda_{\min}\ln 1000}{2\pi} = 1.099\,\lambda_{\min}.$$

So **continuation downward by about 1.1 times the shortest wavelength amplifies
that wavelength by a factor of $10^{3}$.** For a survey resolving 10 km
wavelengths, that is a depth of 11.0 km; for 20 km wavelengths, 22.0 km.

If the noise at $\lambda_{\min}$ is $10^{-3}$ of the signal, it becomes comparable
to the signal after an amplification of $10^{3}$ — which is **the same depth**,
$d = 1.099\lambda_{\min}$, since the two conditions are the same equation with the
same right-hand side. Beyond that depth the continuation is noise.

**Note the structure of the result:** the usable continuation depth is proportional
to the shortest *resolved* wavelength, not to the data precision. Improving
precision from $10^{-3}$ to $10^{-6}$ raises the achievable factor from $10^{3}$ to
$10^{6}$ but only increases the depth by $\ln(10^{3})/2\pi \approx 1.1$
wavelengths — a *logarithmic* improvement. **This is the standard signature of an
ill-posed problem: accuracy buys you very little depth.**

**(d)** The relation to the equivalent stratum of ★★6 is direct, and it is worth
stating as one sentence:

> **A source placed deeper must contain higher wavenumbers to produce the same
> short-wavelength surface signal, and the factor by which those wavenumbers must
> be amplified is exactly $e^{\lvert k\rvert d}$.**

The equivalent-stratum formula gave $\tilde\sigma_h = (\tilde g/2\pi G)
e^{\lvert k\rvert h}$ — the same exponential with the same role. So:

- **Non-uniqueness:** a density at depth $h$ can always be constructed to
  reproduce the data, so the data do not determine the depth.
- **Instability:** constructing that density requires amplifying its
  high-wavenumber content, so a small high-wavenumber error in the data becomes a
  large error in the model.

These are two readings of one equation. The non-uniqueness says the *exact* problem
has infinitely many solutions; the instability says that among those solutions,
only some are reachable from *noisy* data — and the unreachable ones are exactly the
deep, high-wavenumber ones. **If both statements are true, then no algorithm and no
instrument can resolve the difference: the ambiguity is a property of the forward
operator.** That is why regularisation does not *remove* the null space but
*selects* a representative from it, and why reporting the selection criterion is
part of the result. See
[18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)
and
[18-03-01 Why Regularisation Is Physically and Statistically Justified](../../../18-inverse-problems/03-regularization/01-why-regularize.md).
