# Solutions — 01-13-03 Expectation, Variance and Moments

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed, not estimated. Independence assumptions are named wherever
> they are used, because almost every error in this subject comes from a silently
> assumed one.

---

## ★1 — Discrete moments

Using $E[X] = \sum_x x\,p(x)$:

$$E[X] = 0(0.5) + 1(0.3) + 2(0.2) = 0.7,$$

$$E[X^{2}] = 0(0.5) + 1(0.3) + 4(0.2) = 1.1,$$

$$\operatorname{Var}(X) = E[X^{2}] - (E[X])^{2} = 1.1 - 0.49 = \boxed{0.61}.$$

**Check by the definition.** Deviations from the mean are $-0.7, 0.3, 1.3$, with
squares $0.49, 0.09, 1.69$; weighting by the probabilities:

$$0.5(0.49) + 0.3(0.09) + 0.2(1.69) = 0.245 + 0.027 + 0.338 = 0.610. \ \checkmark$$

Both routes agree, which is the point of computing the second moment both ways when
the arithmetic is unfamiliar.

---

## ★2 — Exponential moments

For $X \sim \text{Exp}(\lambda)$ with $f(x) = \lambda e^{-\lambda x}$ on $x \ge 0$:

$$E[X] = \frac{1}{\lambda}, \qquad \operatorname{Var}(X) = \frac{1}{\lambda^{2}},
\qquad E[X^{2}] = \operatorname{Var}(X) + (E[X])^{2} = \frac{1}{\lambda^{2}} +
\frac{1}{\lambda^{2}} = \frac{2}{\lambda^{2}}.$$

**Verification by direct integration.**

$$E[X^{2}] = \int_0^{\infty} x^{2}\lambda e^{-\lambda x}\,dx.$$

Substituting $u = \lambda x$ gives $\int_0^{\infty} u^{2}e^{-u}\,du/\lambda^{2}
= \Gamma(3)/\lambda^{2} = 2/\lambda^{2}$, matching the moment identity. Then
$E[X^{2}] - (E[X])^{2} = 2/\lambda^{2} - 1/\lambda^{2} = 1/\lambda^{2} =
\operatorname{Var}(X)$. $\checkmark$

**A consistency remark.** $E[X^{2}] = 2/\lambda^{2}$ while $(E[X])^{2} =
1/\lambda^{2}$: the raw second moment is twice the square of the mean. That factor
of two is why the variance of an exponential equals the square of its mean, and it
is the origin of the high coefficient of variation (equal to $1$) that makes
averaging exponentially distributed waiting times relatively inefficient.

---

## ★3 — Scaling and shifting

For constants $a$ and $b$, $\operatorname{Var}(aX + b) = a^{2}\operatorname{Var}(X)$.
The shift $b$ has no effect because it moves every value and the mean together, so
deviations are unchanged. Hence

$$\operatorname{Var}(3X - 2) = 9 \times 4 = \boxed{36}, \qquad
\operatorname{sd}(3X - 2) = \sqrt{36} = \boxed{6}.$$

**Units worth noticing.** If $X$ were in mGal, then $3X - 2$ is in mGal only if the
constant $2$ is also in mGal; the variance is in mGal², and the standard deviation
returns to mGal. A variance of 36 is not interpretable until the unit is stated.

---

## ★4 — Linear combination of independent variables

For independent variables, $\operatorname{Var}(\sum_i a_iX_i) = \sum_i
a_i^{2}\sigma_i^{2}$, so

$$\operatorname{Var}(Y) = 4(0.01) + 9(0.04) = 0.04 + 0.36 = 0.40, \qquad
\sigma_Y = \boxed{0.632456}.$$

**Two things to notice.** First, the coefficients are squared, so the factor of $3$
on the noisier input contributes nine times its variance, and $X_2$ dominates the
result even though the coefficients $2$ and $3$ look comparable. Second, the answer
is *not* $2(0.1) + 3(0.2) = 0.8$: standard deviations add in quadrature, not
linearly. Adding them linearly would overstate the uncertainty by $26\%$.

---

## ★5 — Covariance and correlation from a joint table

Marginals: $P(X = 1) = 0.2 + 0.3 = 0.5$ so $E[X] = 0.5$; $P(Y = 1) = 0.1 + 0.3 =
0.4$ so $E[Y] = 0.4$.

$$E[XY] = 1 \cdot 1 \cdot P(X{=}1, Y{=}1) = 0.3,$$

$$\operatorname{Cov}(X,Y) = E[XY] - E[X]E[Y] = 0.3 - 0.2 = \boxed{0.1}.$$

Variances: $\operatorname{Var}(X) = E[X^{2}] - (E[X])^{2} = 0.5 - 0.25 = 0.25$ and
similarly $\operatorname{Var}(Y) = 0.4 - 0.16 = 0.24$. Hence

$$\rho = \frac{0.1}{\sqrt{0.25 \times 0.24}} = \frac{0.1}{0.244949} =
\boxed{0.408248}.$$

**Direct check of $\operatorname{Var}(X+Y)$.** The variable $X + Y$ takes values
$0, 1, 2$ with probabilities $0.4$, $0.3$, $0.3$ (using $0.1 + 0.2$ for the value
$1$). Therefore $E[X+Y] = 0.9$ and $E[(X+Y)^{2}] = 0.3 + 4(0.3) = 1.5$, so

$$\operatorname{Var}(X + Y) = 1.5 - 0.81 = 0.69.$$

By the formula,

$$\operatorname{Var}X + \operatorname{Var}Y + 2\operatorname{Cov}(X,Y)
= 0.25 + 0.24 + 0.2 = 0.69. \ \checkmark$$

The cross term contributes $0.2$ of the $0.69$ — nearly a third of the total. Ignoring
it would understate the spread of the sum by $20\%$ in variance terms.

---

## ★6 — Averaging, and the ceiling

**(a)** The standard error is $\sigma/\sqrt n$, so

$$\frac{0.5}{\sqrt n} = 0.02 \ \Longrightarrow\ \sqrt n = 25
\ \Longrightarrow\ n = \boxed{625}.$$

**(b)** With a shared calibration error of standard deviation $0.08$ mGal the mean of
any number of readings has variance at least $0.08^{2} = 0.0064\ \mathrm{mGal^{2}}$,
because the bias appears in every reading and does not average away. The smallest
achievable standard error is therefore $0.08$ mGal.

The noise contribution equals the calibration contribution when

$$\frac{0.5}{\sqrt n} = 0.08 \ \Longrightarrow\ \sqrt n = 6.25
\ \Longrightarrow\ n \approx \boxed{40}.$$

At $n = 40$ the total standard error is $\sqrt{0.0064 + 0.00625} = 0.1125$ mGal; at
$n = 4000$ it is $\sqrt{0.0064 + 0.0000625} = 0.08039$ mGal. A hundredfold increase
in effort reduced the standard error by $29\%$. Further readings buy progressively
less: the total approaches $0.08$ from above and never reaches it. The productive
investment at this point is a calibration experiment that reduces $\sigma_B$, not a
larger $n$.

---

## ★7 — Shared bias versus noise

The variance of the mean is

$$\operatorname{Var}(\bar X) = \sigma_B^{2} + \frac{\sigma_\varepsilon^{2}}{n}
= 0.04 + \frac{0.64}{64} = 0.04 + 0.01 = 0.05,$$

so

$$\operatorname{se}(\bar X) = \sqrt{0.05} = \boxed{0.223607}\ \mathrm{mGal}.$$

The careless analyst reports $\sigma_\varepsilon/\sqrt n = 0.8/8 = 0.1$ mGal — less
than half the correct value. The understatement factor is
$0.2236/0.1 = 2.236$, which is exactly $\sqrt{5}$: the correct variance is five
times the quoted one because the shared bias contributes four times as much as the
noise term at this sample size.

**The structural point.** Increasing $n$ cannot fix this. As $n \to \infty$ the
correct standard error tends to $0.2$ mGal while the careless formula tends to zero.
A survey that reports the careless number will appear arbitrarily precise and will be
systematically wrong by up to $0.2$ mGal.

---

## ★8 — Difference of correlated quantities

$$\operatorname{Var}(X - Y) = \sigma_X^{2} + \sigma_Y^{2} - 2\rho\sigma_X\sigma_Y
= 4 + 4 - 2(0.7)(2)(2) = 8 - 5.6 = 2.4,$$

so

$$\operatorname{sd}(X - Y) = \sqrt{2.4} = \boxed{1.549193}.$$

The value is smaller than $\sqrt{8} = 2.828427$ because the shared component of the
two quantities cancels in the subtraction — the same mechanism that makes relative
gravity, differential GNSS and differential InSAR accurate, as the lesson's Section 4
makes quantitative.

**A caution.** The formula is symmetric: if $\rho$ had been $-0.7$ the standard
deviation would have been $\sqrt{8 + 5.6} = 3.687818$, larger than the independent
value. Correlation can either help or hurt, and the direction is a physical question
about whether the two error sources add or subtract.

---

## ★9 — The variance of an average under correlation

**(a) Derivation.** Write $S = \sum_{i=1}^{n}X_i$ so that $\bar X = S/n$. Then

$$\operatorname{Var}(S) = \sum_{i=1}^{n}\sum_{j=1}^{n}\operatorname{Cov}(X_i, X_j)
= \sum_{i=1}^{n}\operatorname{Var}(X_i) + \sum_{i \ne j}\operatorname{Cov}(X_i, X_j).$$

The first sum is $n\sigma^{2}$. The second has $n(n-1)$ terms, each equal to
$\rho\sigma^{2}$ by the constant-correlation assumption. Hence

$$\operatorname{Var}(S) = n\sigma^{2} + n(n-1)\rho\sigma^{2}
= n\sigma^{2}\left[1 + (n-1)\rho\right],$$

and dividing by $n^{2}$,

$$\operatorname{Var}(\bar X) = \frac{\sigma^{2}}{n}\left[1 + (n-1)\rho\right].
\qquad \blacksquare$$

**(b) Limit.** As $n \to \infty$ with $\rho > 0$ fixed,

$$\operatorname{Var}(\bar X) \to \rho\sigma^{2} + \frac{\sigma^{2}}{n}(1-\rho) \to
\rho\sigma^{2}.$$

The variance of the mean does not vanish; it stops at $\rho\sigma^{2}$. Averaging
many correlated observations does not recover the mean more precisely than the
shared component allows, no matter how many are taken. This is the general form of
the shared-bias floor of Section 8 of the lesson, with the bias replaced by a
correlation.

**(c)** For $n = 100$, $\rho = 0.05$, $\sigma = 0.2$:

$$\operatorname{Var}(\bar X) = \frac{0.04}{100}\left[1 + 99(0.05)\right]
= 0.0004 \times 5.95 = 0.00238, \qquad
\operatorname{sd}(\bar X) = 0.048785.$$

The effective sample size is the $n_{\text{eff}}$ for which $\sigma^{2}/n_{\text{eff}}
= 0.00238$:

$$n_{\text{eff}} = \frac{0.04}{0.00238} = \boxed{16.807},$$

which matches the equivalent form $n/[1 + (n-1)\rho] = 100/5.95 = 16.807$. One
hundred correlated observations carry the information of about seventeen
independent ones.

**(d)** If stations are correlated over a length of about ten stations, then the
effective sample size of a line of $n$ stations is about $n/10$, and the achievable
standard error is roughly $\sigma\sqrt{10/n}$ rather than $\sigma/\sqrt n$ — a factor
of $\sqrt{10} = 3.16$ worse. A survey designed from $n^{-1/2}$ alone will overstate
its precision by that factor, and no amount of additional stations along the same
line fixes it, because the new stations are correlated with the old ones in the same
way. The remedy is to spread the stations more widely, or to accept the precision the
correlation length permits.

---

## ★10 — Jensen's inequality for the reciprocal

**(a)** For $X \sim \text{Uniform}(a,b)$ the density is $1/(b-a)$ on $(a,b)$, so

$$E\left[\frac{1}{X}\right] = \frac{1}{b-a}\int_a^{b}\frac{dx}{x}
= \frac{\ln b - \ln a}{b - a} = \frac{\ln(b/a)}{b-a}.$$

**(b)**

$$\frac{1}{E[X]} = \frac{1}{(a+b)/2} = \frac{2}{a+b}.$$

**(c)** The function $g(x) = 1/x$ is strictly convex on $(0,\infty)$, since
$g''(x) = 2/x^{3} > 0$. Jensen's inequality for a convex function states
$E[g(X)] \ge g(E[X])$, so

$$E\left[\frac{1}{X}\right] = \frac{\ln(b/a)}{b-a} > \frac{2}{a+b} =
\frac{1}{E[X]}. \qquad \blacksquare$$

Geometrically, the mean of the reciprocals exceeds the reciprocal of the mean because
small values of $X$ produce disproportionately large reciprocals, and the average is
dragged upward by them.

**(d)** For $a = 1$, $b = 3$:

$$E\left[\frac{1}{X}\right] = \frac{\ln 3}{2} = 0.549306, \qquad
\frac{1}{E[X]} = \frac{1}{2} = 0.500000.$$

The Jensen gap is $0.049306$, that is $+9.9\%$ relative to $1/E[X]$.

**The practical form of this result.** The reciprocal of an unbiased estimator is not an
unbiased estimator of the reciprocal. If a velocity is unbiased, the slowness
computed as its reciprocal is biased upward; if a mass and a volume are both
unbiased, the density computed as their ratio is biased, by approximately the
relative variance of the volume. The bias grows approximately as the square of the
relative uncertainty, which is why it is negligible for a $1\%$ measurement and
dominant for a $30\%$ one — the effect measured numerically in
[01-13-09](../09-error-propagation.md) Section 6.
