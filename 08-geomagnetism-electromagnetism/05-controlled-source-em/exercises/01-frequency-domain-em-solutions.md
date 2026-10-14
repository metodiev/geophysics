# Solutions — 08-05-01 Frequency-Domain EM (FDEM) Systems and Responses

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. Lesson:
> [01 Frequency-Domain EM (FDEM) Systems and Responses](../01-frequency-domain-em.md).

---

## ★1 — Skin depth and induction number

$$\omega = 2\pi f = 1.88496\times10^{4}\ \mathrm{rad\,s^{-1}},$$
$$\omega\mu_0\sigma = 1.88496\times10^{4}\times1.2566\times10^{-6}\times0.1
= 2.3688\times10^{-3}\ \mathrm{m^{-2}},$$
$$\delta=\sqrt{\frac{2}{2.3688\times10^{-3}}}
= \sqrt{8.4431\times10^{2}} = 29.058\ \mathrm{m},$$
$$\theta=\frac{r}{\delta}=\frac{25}{29.058}=0.8604.$$

**LIN usable?** No. The lesson's measured relative bias is $1.5\theta = 1.29$, so
the LIN form is in error by more than $100\%$. For the same model the exact
response is $1.3414\times10^{5}+i\,7.8445\times10^{4}\ \mathrm{ppm}$, against a LIN
quadrature of $3.7011\times10^{5}\ \mathrm{ppm}$: the LIN value is $1.3\times$ too
large.

---

## ★2 — Dimensional analysis

$H_s$ and $H_p$ are both magnetic field strengths ($\mathrm{A\,m^{-1}}$), so their
ratio is dimensionless.

$[\omega\mu_0\sigma r^2] = \mathrm{s^{-1}}\cdot\mathrm{H\,m^{-1}}\cdot
\mathrm{S\,m^{-1}}\cdot\mathrm{m^{2}}$. With
$\mathrm{H\,m^{-1}}=\mathrm{kg\,m\,s^{-2}\,A^{-2}}$ and
$\mathrm{S}=\mathrm{A^{2}\,s^{3}\,kg^{-1}\,m^{-2}}$,
$\mathrm{S\,m^{-1}}=\mathrm{A^{2}\,s^{3}\,kg^{-1}\,m^{-3}}$, the product
$\mathrm{H\,m^{-1}}\cdot\mathrm{S\,m^{-1}} = \mathrm{s^{2}\,m^{-2}}$, so
$\omega\mu_0\sigma$ has units $\mathrm{s^{-1}}\cdot\mathrm{s^{2}\,m^{-2}}
= \mathrm{s\,m^{-2}}$ — which is why the demonstration prints it as
$1.5791\times10^{-4}\ \mathrm{m^{-2}}$ for $f=1\ \mathrm{kHz}$,
$\sigma=0.02\ \mathrm{S\,m^{-1}}$ once the factor $\omega$ is included. Multiplying
by $r^2$ gives $\mathrm{s^{0}}$. ✔ Note
$\theta^2=\omega\mu_0\sigma r^2/2$, so $\theta$ and $\omega\mu_0\sigma r^2$ carry
the same information up to the factor $1/2$.

---

## ★3 — The primary coupling dominates

$$M=-\frac{\mu_0\pi a^2b^2}{4s^3}
=-\frac{(1.2566\times10^{-6})\pi(1)^2(1)^2}{4(25)^3}
=-\frac{3.9478\times10^{-6}}{6.2500\times10^{4}}
=-6.3165\times10^{-11}\ \mathrm{H}.$$

A ground response of $3\times10^{-3}$ of the primary means the primary field is
larger than the secondary field by a factor $1/(3\times10^{-3})=333$, i.e.
$20\log_{10}(333)=50.5\ \mathrm{dB}$. To leave the residual primary below $10\%$
of the secondary, the bucking must be accurate to $0.1\times3\times10^{-3}
=3\times10^{-4}$, that is to $0.03\%$ (about $-70\ \mathrm{dB}$) of a coupling
$6.32\times10^{-11}\ \mathrm{H}$. The point of the exercise is the asymmetry with
the lesson's larger-separation case: the primary falls as $s^{-3}$, but so does
the *solid-angle* part of the signal, so increasing the separation does not by
itself improve the signal-to-bucking ratio; only better bucking or a geometry that
discriminates against the primary does.

*(The lesson's $s=20\ \mathrm{m}$ example has $M=-1.2337\times10^{-10}\ \mathrm{H}$
from the dipole formula, checked against the Neumann integral to $0.57\%$.)*

---

## ★4 — Deriving the LIN term

Start from
$S=-r^3\int_0^\infty\lambda^2R(\lambda)e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda$
and use $R=-k^2/(\lambda+u)^2$ (exact, from $\lambda^2-u^2=-k^2$):

$$S=r^3k^2\int_0^\infty\frac{\lambda^2}{(\lambda+u)^2}
e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda .$$

**The approximation enters here:** let $k\to0$ with $\lambda$ fixed, so
$u\to\lambda$ and $\lambda^2/(\lambda+u)^2\to\lambda^2/(2\lambda)^2=1/4$. Then

$$S_{\text{LIN}}\to r^3k^2\frac{1}{4}\int_0^\infty
e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda
=\frac{k^2r^3}{4\sqrt{r^2+4h^2}}
\xrightarrow[h=0]{}\frac{k^2r^2}{4}.$$

The step is *not* uniform: $u\to\lambda$ fails for $\lambda\lesssim|k|$, and it is
that failure which produces the $1.5\theta$ correction. The same substitution shows
why the LIN quadrature is $i\omega\mu_0\sigma r^2/4$: $k^2=i\omega\mu_0\sigma$.

---

## ★5 — Bucking residual versus LIN bias

Reference model: $S=1.111462\times10^{-3}+i\,7.625809\times10^{-3}$, i.e.
$1111.5\ \mathrm{ppm}$ in-phase and $7625.8\ \mathrm{ppm}$ quadrature.

(a) $20\ \mathrm{ppm}$ is $20/1111.5 = 1.80\%$ of the true in-phase response.
(b) $20\ \mathrm{ppm}$ is $20/7625.8 = 0.26\%$ of the quadrature.

LIN bias at $\theta=0.1$: the LIN quadrature for the same model is
$\omega\mu_0\sigma r^2/4 = 8882.6\ \mathrm{ppm}$, and the relative bias is
$1.5\times0.1=0.15$, i.e. $0.15\times8882.6 = 1332\ \mathrm{ppm}$.

**Conclusion.** The LIN bias ($\sim1332$ ppm) exceeds the bucking residual
($20$ ppm) by a factor of about $67$ in the quadrature error budget. The practical
ranking is therefore: (1) use the exact response or account for the LIN bias;
(2) then worry about bucking, which matters mainly for the in-phase channel where
the true signal is only $1111.5\ \mathrm{ppm}$.

---

## ★6 — Apparent conductivity and the source of the discrepancy

$$\sigma_{\text{app}}=\frac{4\,\mathrm{Im}\,S}{\omega\mu_0 r^2}
=\frac{4\left(1.1229\times10^{-3}\right)}
{1884.96\times1.2566\times10^{-6}\times400}
=\frac{4.4916\times10^{-3}}{9.4745\times10^{-1}}
=4.7407\times10^{-3}\ \mathrm{S\,m^{-1}}.$$

Against the true $5.000\times10^{-3}\ \mathrm{S\,m^{-1}}$ the estimate is
$5.19\%$ **low**. The induction number is $\theta=r/\delta$ with
$\delta=\sqrt{2/(\omega\mu_0\sigma)}=411.0\ \mathrm{m}$ (computed with
$\omega\mu_0\sigma=1.1844\times10^{-5}\ \mathrm{m^{-2}}$), so $\theta=0.0487$.

**Bias, not noise.** The lesson's measured rule is a LIN relative error of
$1.5\theta=1.5\times0.0487=7.3\%$ in the response, which propagates to a
$\sim5\%$ low bias in $\sigma_{\text{app}}$ — the same sign and the same order as
the $5.19\%$ observed. The demonstration's section 7 shows the same drift
explicitly ($0.00499$ at $1\ \mathrm{Hz}$, where $\theta=0.0487/5.48$ and the bias
is negligible, falling to $0.00474$ at $300\ \mathrm{Hz}$). A noise explanation
would need the quadrature to be wrong by $5\%$, i.e. a noise level of order
$56\ \mathrm{ppm}$ against the $2\ \mathrm{ppm}$ synthetic floor — two orders of
magnitude larger, and it would have to be systematic across frequencies, which
noise is not.

---

## ★7 — Scale invariance and what breaks it

Substitute $\lambda=x/r$, so $\mathrm{d}\lambda=\mathrm{d}x/r$ and
$u=\sqrt{\lambda^2+k^2}=\sqrt{x^2+(kr)^2}/r$:

$$S=-r^3\int_0^\infty \frac{x^2}{r^2}R\!\left(\frac{x}{r}\right)
e^{-2xh/r}J_0(x)\frac{\mathrm{d}x}{r}
=-\int_0^\infty x^2 R_x\,e^{-2x(h/r)}J_0(x)\,\mathrm{d}x,$$

with $R_x=(x-U)/(x+U)$, $U=\sqrt{x^2+(kr)^2}$ and $kr=(1+i)\theta$. Hence $S$ is a
function of $kr$ and $h/r$ only. For $h=0$ it is a function of $\theta$ alone.
Therefore $(\sigma,r)\to(\sigma/4,2r)$ at the same frequency is undetectable — the
demonstration confirms it to all printed digits
($S=+8.98089260\times10^{-3}+2.78802350\times10^{-2}i$ for all four pairs).

**What breaks it.** A second layer. For two layers the response depends on
$kr$, $h/r$ **and** the thickness-to-separation ratio $d/r$ (and on the
conductivity contrast $\sigma_2/\sigma_1$), so the invariance in $(\sigma_1,r)$
survives only if $d$ scales with $r$ too. A second **separation** at the same
frequency gives two values of $\theta$ and, for a layered ground, two different
weightings of the layering: it constrains the layer thickness in metres. A second
**frequency** moves $\delta$ while leaving $r$ fixed: it constrains the
conductivity–thickness product. Neither observation constrains a single-halfspace
conductivity better than the pair $(\sigma r^2)$; both constrain layering.

---

## ★8 — Experiment specification

**Targets.** $\sigma$ to $5\%$; a $1\%$ separation error distinguished from a
conductivity error.

**Instrument.** HCP coil pair, two rigid separations $r_1=10\ \mathrm{m}$ and
$r_2=30\ \mathrm{m}$ (any pair works provided $r_2/r_1\ge3$, so that the two
$\theta$ overlap minimally), eight logarithmically spaced frequencies
$100\ \mathrm{Hz}$ to $20\ \mathrm{kHz}$, noise $2\ \mathrm{ppm}$ per component
$1\sigma$ (the lesson's synthetic figure).

**Metric.** Fit both separations simultaneously to the exact halfspace response
with $\sigma$ and a multiplicative separation error $\epsilon$
($r_i\to r_i(1+\epsilon)$) as free parameters, using a weighted least-squares
misfit on in-phase and quadrature. The separating direction in parameter space is
the one that changes $\theta_1$ and $\theta_2$ differently:
$\theta_i=r_i/\delta$ gives
$\partial\ln\theta_i/\partial\ln\sigma = 1/2$ for both, but
$\partial\ln\theta_i/\partial\ln r = 1$; a change in $\sigma$ moves $\theta_1$ and
$\theta_2$ *together*, a change in $r$ moves them apart only through the ratio
$r_2/r_1$, which is what the $r_2$ measurement fixes.

**Prediction.** (i) The LIN bias is $1.5\theta$, so at $r=10\ \mathrm{m}$ and
$\sigma=0.02\ \mathrm{S\,m^{-1}}$ the bias is below $5\%$ only for
$f\lesssim2\ \mathrm{kHz}$; use the exact response, or restrict the band, and the
bias stops being the dominant error. (ii) With $2\ \mathrm{ppm}$ noise the
quadrature at $\theta\approx0.05$ is $\sim5\times10^{3}\ \mathrm{ppm}$, a
signal-to-noise of $\sim10^{3}$ per frequency, so averaging over eight frequencies
supports a $\sigma$ precision far better than $5\%$ if the model is a true
halfspace. (iii) Consequently the achievable precision will be limited not by
noise but by *model error* (layering, magnetic susceptibility, height). **A
specification that claims a $5\%$ conductivity from a single-separation
single-frequency FDEM reading is unfalsifiable; one that measures the second
separation and states the noise floor is.**
