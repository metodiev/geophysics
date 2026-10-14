# Solutions — 02-08-03 Spherical Harmonics and Multipole Expansions

> **Read this after attempting the exercises, not before.** Conventions: complex
> $Y_{lm}$ with the Condon–Shortley phase,
> $Y_{lm} = \sqrt{\tfrac{2l+1}{4\pi}\tfrac{(l-m)!}{(l+m)!}}P_l^m(\cos\theta)e^{im\phi}$,
> $C_{lm} = \tfrac{4\pi}{2l+1}q_{lm}/(Ma^l)$ and, for an axisymmetric body,
> $J_l = -\tfrac{1}{Ma^l}\int r'^lP_l(\cos\theta')\rho\,dV'$. Values attributed to
> the demonstration are its actual output.

---

## ★1 — Legendre polynomials

**(a)** From $(l+1)P_{l+1} = (2l+1)xP_l - lP_{l-1}$ with $P_0 = 1$, $P_1 = x$:

$$P_0 = 1,\quad P_1 = x,\quad P_2 = \tfrac12(3x^2-1),\quad
P_3 = \tfrac12(5x^3-3x),\quad P_4 = \tfrac18(35x^4-30x^2+3).$$

**(b)** $P_4(1) = \tfrac18(35-30+3) = 1 = (+1)^4$; $P_4(0) = \tfrac{3}{8} = 0.375$ (the
demonstration prints $0.375$); $P_4(-1) = \tfrac18(35-30+3) = 1 = (-1)^4$. ✓

**(c)** $P_3(0.5) = \tfrac12(5\times0.125 - 3\times0.5) = \tfrac12(0.625-1.5) = -0.4375$,
matching the demonstration's Bonnet-recurrence value $-0.4375$ to all printed digits.

**(d)** $\int_{-1}^1P_2P_4dx = 0$ by orthogonality ($2\neq4$; the integral
$2/(2l+1)\delta_{lm}$ vanishes for unequal indices). Numerically the demonstration's
Gauss–Legendre quadrature over $l,m\le5$ gives a worst deviation from
$2/(2l+1)\delta_{lm}$ of $1.79\times10^{-16}$ — round-off.

---

## ★2 — Spherical harmonics at a point

At $\theta = \pi/3$ ($\cos\theta = 0.5$, $\sin\theta = 0.866025$) and
$\phi = \pi/4$ ($e^{i\phi} = 0.707107+0.707107i$):

**(a)**

$$Y_{00} = \frac{1}{\sqrt{4\pi}} = 0.282\,094\,792,$$
$$Y_{10} = \sqrt{\frac{3}{4\pi}}\times0.5 = 0.244\,301\,256,$$
$$Y_{11} = -\sqrt{\frac{3}{8\pi}}\times0.866\,025\times(0.707\,107+0.707\,107i)
= -0.211\,571\,094 - 0.211\,571\,094i.$$

**(b)** $\lvert Y_{00}\rvert^2 = 0.079\,577\,471$;
$\lvert Y_{10}\rvert^2 = 0.059\,683\,027$;
$\lvert Y_{11}\rvert^2 = 0.089\,524\,542$.

**(c)** The sum over $m = -1, 0, +1$ **including $m=-1$** is

$$\sum_{m=-1}^{1}\lvert Y_{1m}\rvert^2 = 0.059\,683\,027 + 2\times0.089\,524\,542
= 0.238\,732\,415 = \frac{3}{4\pi},$$

which is the addition theorem for $l=1$: the sum equals $(2l+1)/4\pi$, a constant.
Proof: with $\lvert Y_{10}\rvert^2 = \tfrac{3}{4\pi}\cos^2\theta$ and
$\lvert Y_{1,\pm1}\rvert^2 = \tfrac{3}{8\pi}\sin^2\theta$, the sum is
$\tfrac{3}{4\pi}(\cos^2\theta+\sin^2\theta) = \tfrac{3}{4\pi}$. The demonstration's
orthonormality test over $l,l'\le3$ confirms the underlying normalisation with a
worst deviation of $1.22\times10^{-14}$.

**(d)** $q_{11} = Mr'\,Y_{11}^{*}(\pi/4, 0) = 10^{11}\times500\times(-0.244\,301)
= -1.221\,51\times10^{13}$ kg m. (Note the sign: $Y_{11}$ carries the
Condon–Shortley minus, and $Y_{11}(\pi/4,0)$ is real. In this lesson's convention,
$C_{11} = \tfrac{4\pi}{3}q_{11}/(Ma) = \tfrac{4\pi}{3}\times(-0.244\,301)
= -1.0233$.)

---

## ★3 — Spherically symmetric densities leave only $l=0$

**(a)** $q_{lm} = \left(\int_0^a\rho(r')r'^{l+2}dr'\right)
\left(\oint\overline{Y}_{lm}\,d\Omega'\right)$ for $l>0$.

**(b)** $\oint_{S^2}\overline{Y}_{lm}d\Omega = 0$ for every $(l,m)\neq(0,0)$: the
average of a non-constant harmonic over the sphere vanishes, which is the mean value
property evaluated at the centre of the sphere. Equivalently, $Y_{00}$ is the only
harmonic that is constant on the sphere.

**(c)** For $l=m=0$, $\oint\overline{Y}_{00}d\Omega = \tfrac{1}{\sqrt{4\pi}}\times4\pi
= \sqrt{4\pi}$. So $q_{00} = M/\sqrt{4\pi}$ and

$$C_{00} = \frac{4\pi}{1}\frac{q_{00}}{M} = 4\pi\times\frac{1}{\sqrt{4\pi}}
= \sqrt{4\pi} = 3.544\,907\,702 .$$

**(d)** It is a statement about symmetry: a spherically symmetric body has *no*
$l\ge1$ content, exactly, for any radial profile. It is not that the higher
coefficients are small; they are zero. The demonstration's computed values for a
uniform ball of radius $1000$ m and density $3000$ kg m$^{-3}$ are
$\lvert C_{10}/C_{00}\rvert = 2.8\times10^{-19}$,
$\lvert C_{20}/C_{00}\rvert = 3.9\times10^{-22}$ and
$\lvert C_{60}/C_{00}\rvert = 1.8\times10^{-35}$ — decreasing as the quadrature's
round-off, not as physics.

---

## ★4 — A dumbbell

**(a)** $C_{00} = \sqrt{4\pi}$ for any body, by ★3(c). The claim here is not that
the *dumbbell* has only a monopole — it does not — but that the $l=0$ term is fixed
by the total mass alone.

**(b)** $I_2 = \int r'^2P_2(\cos\theta')\rho\,dV' = md^2P_2(1) + md^2P_2(-1)
= md^2 + md^2 = 2md^2 = Md^2 = 10^{11}\times10^6 = 10^{17}$ kg m$^2$. And
$q_{20} = \sqrt{\tfrac{5}{4\pi}}I_2 = 0.630\,784\times10^{17}
= 6.3078\times10^{16}$ kg m$^2$. With $a = d$,

$$J_2 = -\frac{I_2}{Ma^2} = -\frac{Md^2}{Md^2} = -1 \quad\text{exactly.}$$

**(c)** The body is **prolate** (elongated along the polar axis, mass concentrated
near the poles, deficit at the equator). A prolate body has negative $J_2$ — the
opposite sign to the Earth's oblate $+1.08\times10^{-3}$ — so the sign is as
expected. The value $-1$ is the maximum magnitude possible for a body confined within
radius $a$, because $P_2(\cos\theta')\ge-1/2$ and $r'\le a$ bound the moment.

**(d)** Along the axis at $z = 5000$ m: the distances to the two masses are
$\lvert5000-1000\rvert = 4000$ m and $\lvert5000+1000\rvert = 6000$ m, so

$$V_{\text{exact}} = Gm\left(\frac{1}{4000}+\frac{1}{6000}\right)
= 3.337\,15\times10^{-4}\times\left(2.5\times10^{-4}+1.6\overline{6}\times10^{-4}\right)
= 1.390\,479\times10^{-3}\ \text{m}^2\text{s}^{-2}.$$

The multipole series along the axis is
$V = (GM/z)[1 - J_2(a/z)^2P_2(1) + \ldots] = (GM/z)[1+(d/z)^2+\ldots]$, so

| truncation | $V$ (m$^2$ s$^{-2}$) | relative error |
|---|---|---|
| monopole only | $1.334\,860\times10^{-3}$ | $4.00$ per cent |
| monopole + quadrupole | $1.388\,254\times10^{-3}$ | $0.16$ per cent |

The quadrupole term is $G\times2md^2/z^3 = 5.3394\times10^{-5}$ m$^2$ s$^{-2}$, and
adding it reduces the error by a factor $25$ — the series converges as $(d/z)^2 = 0.04$
per degree, as expected.

---

## ★5 — Reading the demonstration

**(a)** Worst deviation from orthonormality: $1.22\times10^{-14}$, at
$(l,m,l',m') = (0,0,0,0)$ — that is, the (0,0) normalisation integral, whose exact
value is $1$.

**(b)** Truncated potential at $L = 0$: $3.337\,150\times10^{-3}$ m$^2$ s$^{-2}$
(relative error $3.486\times10^{-2}$); at $L = 2$: $3.472\,926\times10^{-3}$
($4.410\times10^{-3}$); at $L = 8$: $3.457\,676\times10^{-3}$
($7.606\times10^{-7}$). The reference is the direct
$GM/\lvert\mathbf{r}-\mathbf{r}'\rvert = 3.457\,678\times10^{-3}$.

**(c)** Centred origin: $\lvert q_1\rvert = 0$. Shifted to $x = +200$ m:
$\lvert q_1\rvert = 9.772\,050\times10^{12}$ kg m.

**(d)** $\lvert C_{20}/C_{00}\rvert = 3.895\times10^{-22}$;
$\lvert C_{60}/C_{00}\rvert = 1.784\times10^{-35}$.

**(e)** At $f = 0.0033528107$: quadrature $J_2 = 1.338\,875\,9980\times10^{-3}$,
formula $(2f-f^2)/5 = 1.338\,875\,9980\times10^{-3}$ — identical to the displayed
digits, and the demonstration's worst relative difference over all four
flattenings is $3.0\times10^{-13}$. The measured Earth value $1.08\times10^{-3}$ divided by the homogeneous value
gives $0.8066$ (the lesson quotes $0.8077$ against the Darwin–Radau value
$1.0814\times10^{-3}$: the two comparisons differ because they use two different
"Earth" values, and both are correct as stated).

---

## ★6 — Deriving $C_{00}$

**(a)** $q_{00} = \int\rho Y_{00}^{*}\,dV' = \tfrac{1}{\sqrt{4\pi}}\int\rho\,dV'
= \tfrac{M}{\sqrt{4\pi}}$.

**(b)** $C_{00} = \tfrac{4\pi}{1}\cdot\tfrac{M/\sqrt{4\pi}}{M\cdot a^0}
= \tfrac{4\pi}{\sqrt{4\pi}} = \sqrt{4\pi} = 3.544\,907\,702$.

**(c)** The $l=0$ term of the expansion is
$(GM/r)C_{00}Y_{00} = (GM/r)\sqrt{4\pi}\cdot\tfrac{1}{\sqrt{4\pi}} = GM/r$ — the
point-mass potential, as it must be, since the monopole term is the only one that
survives symmetrisation.

**(d)** Because $q_{00}$ is proportional to the total mass and the normalisation
$Y_{00} = 1/\sqrt{4\pi}$ is universal. The content of the statement is that the
*largest* term in the expansion is a property of the body's mass alone and contains
no information about its shape.

---

## ★7 — $J_2$ of a homogeneous spheroid

**(a)** $J_2 = (2\times0.001 - 10^{-6})/5 = (0.002-0.000001)/5 = 3.998\times10^{-4}$.

**(b)** With $a = 1$, $c = 0.999$: $C = \tfrac25 = 0.4$,
$A = \tfrac15(1+0.998001) = 0.399\,6002$. So $J_2 = (C-A)/a^2 = 3.998\times10^{-4}$ ✓
— agreement to the displayed digits, and the demonstration prints
$3.9980000000\times10^{-4}$ for both routes.

**(c)** For $f = 0.05$: $(2f-f^2)/5 = (0.1-0.0025)/5 = 1.95\times10^{-2}$. From the
moments: $c = 0.95$, $A = \tfrac15(1+0.9025) = 0.3805$, $C = 0.4$, giving
$J_2 = 1.95\times10^{-2}$ ✓. The agreement is exact at every $f$, not merely
first-order — the demonstration prints $1.9500000000\times10^{-2}$ for both.

**(d)** For a homogeneous body the quadrupole moment is a fixed function of the
shape, so $f$ determines $J_2$. For a body with an arbitrary radial density profile,
the same shape can carry very different quadrupole moments: $J_2$ is a *mass* moment,
and a body can be flattened with its mass concentrated at the centre (small $J_2$) or
spread to the surface (large $J_2$). The Earth is the first case: it has the shape of
a spheroid with $f = 1/298.257$ but $J_2$ about $19$ per cent smaller than the
homogeneous spheroid with that shape.

---

## ★8 — $q$ and $J_2$ from the defining data

**(a)** $q = \omega^2a^3/GM = (7.292\,115\times10^{-5})^2(6\,378\,137)^3
/3.986\,004\,418\times10^{14} = 3.461\,391\,8985\times10^{-3}$.

**(b)** $f = 1/298.257\,223\,563 = 3.352\,810\,6647\times10^{-3}$, so
$J_2 = (2f-q)/3 = (6.705\,621\,3294\times10^{-3} - 3.461\,391\,8985\times10^{-3})/3
= 1.081\,409\,8103\times10^{-3}$.

**(c)** $(2f-f^2)/5 = (6.705\,621\,3294\times10^{-3} - 1.124\,133\times10^{-5})/5
= 1.338\,875\,9980\times10^{-3}$.

**(d)** Ratio $= 1.0814/1.3389 = 0.8077$. The Earth carries only about $81$ per cent
of the quadrupole that a homogeneous body of the same shape and rotation would
carry, which says that its mass is concentrated toward the centre — the same
conclusion the seismic density profile reaches, obtained here from the definining
flattening and rotation rate alone. Note the provenance carefully: $a$, $1/f$,
$\omega$ and $GM$ are exact *defining* parameters of WGS 84, but their combination
through the hydrostatic relation predicts $J_2$ only if the Earth is in hydrostatic
equilibrium. The measured $J_2$ is $1.08\times10^{-3}$; authoritative digits and
uncertainty come from ICGEM.

---

## ★★★9 — The addition theorem for $l = 1$

**(a)** $\cos\gamma = \hat{\mathbf{r}}\cdot\hat{\mathbf{r}}'
= \cos\theta\cos\theta' + \sin\theta\sin\theta'\cos(\phi-\phi')$.

**(b)** With $Y_{10} = \sqrt{3/4\pi}\cos\theta$,
$Y_{11} = -\sqrt{3/8\pi}\sin\theta e^{i\phi}$ and
$Y_{1,-1} = -Y_{11}^{*} = +\sqrt{3/8\pi}\sin\theta e^{-i\phi}$:

$$\frac{4\pi}{3}\sum_{m=-1}^{1}Y_{1m}(\theta,\phi)\overline{Y}_{1m}(\theta',\phi')
= \frac{4\pi}{3}\left[\frac{3}{4\pi}\cos\theta\cos\theta'
+ \frac{3}{8\pi}\sin\theta\sin\theta'e^{i(\phi-\phi')}
+ \frac{3}{8\pi}\sin\theta\sin\theta'e^{-i(\phi-\phi')}\right]$$
$$= \cos\theta\cos\theta' + \frac{4\pi}{3}\cdot\frac{3}{8\pi}
\cdot2\sin\theta\sin\theta'\cos(\phi-\phi')
= \cos\theta\cos\theta' + \sin\theta\sin\theta'\cos(\phi-\phi') = \cos\gamma .$$

**(c)** At the demonstration's direction, $(\theta,\phi) = (70^\circ, 110^\circ)$
and $(\theta',\phi') = (40^\circ, 20^\circ)$: the left side gives
$\cos\gamma = 0.262\,002\,6302$ and the right side gives $0.262\,002\,6302$, agreeing
to $0.0\times10^{0}$ (with zero imaginary part). Two further pairs confirm the
identity: $(30^\circ,0^\circ)$–$(60^\circ,45^\circ)$ gives
$0.739\,198\,9197$ on both sides, and $(10^\circ,300^\circ)$–$(80^\circ,120^\circ)$
gives $0$ on both sides to $2.9\times10^{-16}$. ✓

**(d)** The theorem replaces a *coupling* between two directions, $P_l(\cos\gamma)$,
by a *separable* sum of functions of each direction. In the forward problem — the
potential of a body, which is an integral over source directions weighted by
$1/\lvert\mathbf{r}-\mathbf{r}'\rvert$ — separability is what turns an
apparently two-direction problem into the product of a source integral and a
field-direction evaluation. That is why the coefficient $q_{lm}$ can be computed by
a single integral over the source, with the observation direction appearing only as
$Y_{lm}(\theta,\phi)$.

---

## ★★★10 — A triaxial ellipsoid

**(a)** $l=1$ coefficients are linear moments $\int r'\overline{Y}_{1m}\rho\,dV'$,
i.e. proportional to $\int\mathbf{r}'\rho\,dV'$, which vanishes when the origin is at
the centre of mass (as it is for an ellipsoid). For $l=2$, the quadrupole is a
traceless symmetric second-rank tensor with **five** independent components, and
those correspond to $C_{20}$, $\mathrm{Re}\,C_{21}$, $\mathrm{Im}\,C_{21}$,
$\mathrm{Re}\,C_{22}$, $\mathrm{Im}\,C_{22}$: five real coefficients. A triaxial body
with all three semi-axes distinct has no symmetry that kills any of them in general.

**(b)** Reflection symmetry $x\to-x$ and $y\to-y$ (with $z$ fixed) is a rotation by
$\pi$ about $z$, under which $Y_{lm}\to(-1)^mY_{lm}$. A body invariant under that
rotation has $\int\rho r'^lY_{lm}^{*}dV' = 0$ for odd $m$. Reflection $z\to-z$
(which leaves an axis-aligned ellipsoid invariant) changes $Y_{lm}$ by
$(-1)^{l+m}$ up to a phase, killing coefficients with odd $l+m$, and with the
previous result that leaves only even $l$ and even $m$. So for an axis-aligned
ellipsoid only $l$ even and $m$ even survive: $l=2$ gives $C_{20}$ and $C_{22}$ only.

**(c)** With $A_{ij} = \int x_ix_j\rho\,dV'$ the second-moment tensor, the $l=2$
content is the traceless part
$Q_{ij} = A_{ij} - \tfrac13\delta_{ij}\mathrm{tr}A$:

$$C_{20}\propto\left(2A_{zz}-A_{xx}-A_{yy}\right), \qquad
C_{2,\pm1}\propto A_{xz},\,A_{yz}, \qquad
C_{2,\pm2}\propto\left(A_{xx}-A_{yy}\right),\,A_{xy} ,$$

with proportionality constants fixed by the normalisation. The trace
$\mathrm{tr}A = \int r'^2\rho\,dV'$ is fixed by the body's radial mass distribution
and the reference radius, so only the **five** independent components of the
traceless $Q$ are free — matching the five real degrees of freedom at $l=2$.

**(d)** For a homogeneous ellipsoid with semi-axes $a,b,c$:
$A_{xx} = Ma^2/5$, $A_{yy} = Mb^2/5$, $A_{zz} = Mc^2/5$, and the off-diagonal
$A_{ij} = 0$. So

$$\frac{A_{xx}-A_{yy}}{Ma^2} = \frac{1}{5}\left(1-\frac{b^2}{a^2}\right),
\qquad
\frac{2A_{zz}-A_{xx}-A_{yy}}{Ma^2} = \frac{1}{5}\left(\frac{2c^2-a^2-b^2}{a^2}\right).$$

With $a=b$ the first is zero, so $C_{22} = 0$: an oblate spheroid has no
east–west quadrupole, which is the symmetry statement that an axisymmetric body has
$m=0$ only. The second becomes $\tfrac15(2c^2-2a^2)/a^2 = -\tfrac25(1-(c/a)^2)$, and
using $J_2 = -\sqrt{4\pi/5}\,C_{20}$ in this lesson's convention recovers
$J_2 = \tfrac15(1-(1-f)^2)$ from ★7. ✓
