# Solutions — 01-01-05 Absolute vs Relative Error, Conditioning and Stability

> **Read this after attempting the exercises, not before.**
>
> Every numeric value below was produced by running the stated computation in
> CPython 3.14 on a macOS machine, with the standard library only. Where a result
> is platform-dependent — in particular anything that depends on the accuracy of
> the C library's transcendental functions — that is flagged explicitly. Rarely
> will an answer require a value that cannot be checked in a few lines of code;
> where an answer cannot be verified, that is stated rather than guessed.

---

## ★1 — Absolute versus relative error

**(a)** $1/7 = 0.142857142857\ldots$, so

$$|1/7 - 0.142857| = 1.42857\times10^{-7}.$$

**(b)**

$$\frac{1.42857\times10^{-7}}{1/7} = 1.0\times10^{-6}.$$

(The approximation `0.142857` was evidently built by rounding to exactly six
significant figures of the repeat, so the relative error is exactly $10^{-6}$ to
the precision shown.)

**(c)** Quote the **relative** error. An absolute error of
$1.4\times10^{-7}$ sounds impressive but is meaningless without knowing the size
of the quantity; the same absolute error on a quantity of size $10^{-7}$ would
be a 100% mistake. Relative error is dimensionless and therefore comparable
across quantities, which is exactly what a reader needs.

**(d)** For $6.674\times10^{-11}$ approximated by `6.7e-11`:

$$|6.674\times10^{-11} - 6.7\times10^{-11}| = 2.6\times10^{-13},
\qquad \frac{2.6\times10^{-13}}{6.674\times10^{-11}} = 3.90\times10^{-3}.$$

So the $1/7$ approximation is relatively better ($10^{-6}$ versus
$3.9\times10^{-3}$), even though its absolute error is numerically larger. This
is the whole reason relative error exists.

**Note on the constant.** $6.674\times10^{-11}$ is the modern CODATA-family value
of $G$ quoted to four significant figures; it is used here purely as an
arithmetic example, and its uncertainty is not part of this exercise.

---

## ★2 — Condition numbers from the formula

| $f$ | point | $\kappa_f(x) = \|x f'/f\|$ | assessment |
|---|---|---|---|
| $\sqrt{x}$ | $x = 10^{-8}$ | $1/2$ | well conditioned |
| $\ln x$ | $x = 1.0001$ | $1/\|\ln x\| = 10000.5$ | badly conditioned |
| $\ln x$ | $x = 10^{6}$ | $1/\|\ln x\| = 0.0724$ | well conditioned |
| $e^{x}$ | $x = 20$ | $\|x\| = 20$ | mildly conditioned |

All four match the values the demonstration computes numerically.

**Why `ln x` is a poor route to $(x-1)$ for $x$ near 1.** As $x \to 1$,
$\ln x \to 0$, and the condition number $1/|\ln x|$ diverges. Concretely,
$\ln(1.0001) = 9.9995\times10^{-5}$: an input relative error of $u$ becomes an
output relative error of about $10^{4}u \approx 1.1\times10^{-12}$. The
mathematical identity $\ln x \approx x-1$ holds, but alternating between the two
forms near $x=1$ throws away four digits per evaluation. Use `math.log1p(x - 1)`
instead, which evaluates the small correction directly and stays
well-conditioned — much as `expm1` does for the exponential case in Section 5.3
of the lesson.

---

## ★3 — Forward error, backward error, residual

**Definitions.**

- **Forward error**: how far the computed answer is from the true answer,
  $\|\hat{x} - x\| / \|x\|$.
- **Backward error**: the smallest perturbation of the data for which the
  computed answer is exact, i.e. the smallest $\Delta A,\Delta b$ with
  $(A+\Delta A)\hat{x} = b+\Delta b$.
- **Residual**: the amount by which the computed answer fails to satisfy the
  original equations, $r = b - A\hat{x}$.

**(a)** With $\hat{x} = (1.0000001, 0.9999999)$:

$$A\hat{x} = \bigl(2(1.0000001) + 0.9999999,\; 1.0000001 + 3(0.9999999)\bigr)
= (3.0000001,\ 3.9999998),$$

$$r = (3 - 3.0000001,\; 4 - 3.9999998) = (-1.000\times10^{-7},\ 2.000\times10^{-7}).$$

**(b)** $\hat{x} - x = (1.0\times10^{-7},\ -1.0\times10^{-7})$.

**(c)** $\|\Delta x\|_\infty/\|x\|_\infty = 1.0\times10^{-7}$ and
$\|r\|_\infty/\|b\|_\infty = 2.0\times10^{-7}/4 = 5.0\times10^{-8}$.

**(d)** $\|A\|_\infty = \max(2+1,\ 1+3) = 4$ and

$$A^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2\end{pmatrix},
\qquad \|A^{-1}\|_\infty = \max(4/5,\ 3/5) = 0.8,$$

so $\kappa_\infty(A) = 4 \times 0.8 = 3.2$. The bound then gives

$$\frac{\|\Delta x\|}{\|x\|} \le \kappa(A)\frac{\|r\|}{\|b\|}
= 3.2 \times 5.0\times10^{-8} = 1.6\times10^{-7},$$

and the observed $1.0\times10^{-7}$ satisfies it. Here the bound is only a factor
of 1.6 from the truth, because $A$ is well conditioned and the perturbation is
close to the worst direction.

**The point worth retaining.** The residual ($2\times10^{-7}$) and the forward
error ($1\times10^{-7}$) are of the same order *only because $\kappa$ is about
3*. For the Hilbert matrices in ★★6, a residual at the level of $u$ coexists
with a relative error of $10^{-4}$.

---

## ★4 — Instrument uncertainty versus round-off

**(a)** $\;0.01/979\,812.37 = 1.0206\times10^{-8}$.

**(b)** $\;u = 2^{-53} = 1.1102\times10^{-16}$.

**(c)** Ratio:

$$\frac{1.0206\times10^{-8}}{1.1102\times10^{-16}} = 9.19\times10^{7}.$$

The measurement uncertainty is about **eight orders of magnitude** larger than
the floating-point round-off. Round-off is therefore irrelevant to this
measurement's error budget; the instrument, the station positioning and the
reduction procedure dominate. (The floating-point error only becomes relevant on
the modelling side, or when differences of many large model values are
accumulated.)

---

## ★★5 — The conditioning of the subtraction inside $1-\cos x$

**(a)** At $x = 10^{-4}$, in binary64: $\cos x = 0.9999999950000002$,
$1-\cos x = 4.99999995\times10^{-9}$ approximately, and

$$\mathrm{amp}(x) = \frac{\cos x}{1-\cos x} = 2.000\times10^{8}.$$

**(b)** Predicted relative error of the numerator:

$$u\,\mathrm{amp}(x) = 1.1102\times10^{-16}\times2.000\times10^{8}
= 2.22\times10^{-8}.$$

The lesson's observed relative error of the quotient $(1-\cos x)/x^{2}$ at the
same $x$ is $5.24\times10^{-9}$. The prediction is right to better than a factor
of five — the same order of magnitude, which is all an error model promises.

**(c)** At $x = 10^{-6}$: $\mathrm{amp}(x) = 2.000\times10^{12}$, so

$$u\,\mathrm{amp}(x) = 2.22\times10^{-4},$$

against an observed $8.89\times10^{-5}$ — again the same order of magnitude.

As $x$ decreases further the prediction keeps rising, but reality changes
character: once $x^{2}/2 < u$, i.e. below $x \approx \sqrt{2u} =
1.49\times10^{-8}$, $\cos x$ rounds to exactly $1.0$ and the naive numerator is
computed as exactly $0.0$. The relative error is then $1$ (100%), and no
error model of the form $u\,\mathrm{amp}$ can describe it, because the
information is not "perturbed" but destroyed. This is why the half-angle form
$2\sin^{2}(x/2)$ should be used instead: it has no subtraction of nearly equal
quantities, so **there is nothing to amplify**.

**(d)** The function $f(x) = 1-\cos x$ evaluated at a given $x$ has condition
number $\kappa = |x\sin x/(1-\cos x)|$, which tends to $2$ as $x\to0$ — it is
perfectly well conditioned, and the answer deserves full precision for every
$x$. The *route* `cos` then subtract computes an intermediate $y = \cos x \approx
1$ and then forms $y - 1$, a difference of nearly equal numbers whose own
condition number is $y/(y-1) \approx 1/x$, which diverges. The algorithm inherits
the worst conditioning of its steps.

---

## ★★6 — Hilbert-matrix conditioning

**(a)** Ratios observed$/(\kappa u)$:

| $n$ | observed | $\kappa_\infty u$ | ratio |
|---|---|---|---|
| $3$ | $6.513\times10^{-15}$ | $8.304\times10^{-14}$ | $0.078$ |
| $5$ | $3.668\times10^{-13}$ | $1.048\times10^{-10}$ | $0.0035$ |
| $8$ | $2.423\times10^{-8}$ | $3.761\times10^{-6}$ | $0.0064$ |
| $10$ | $1.927\times10^{-4}$ | $3.925\times10^{-3}$ | $0.049$ |

**(b)** The bound is **not** violated anywhere: every ratio is below 1, and most
are below 0.01. The interpretation is that $\kappa u$ is a *worst-case* estimate
over perturbation directions and rounding patterns; in practice the actual
rounding errors rarely align with the least favourable direction. Ratios between
$0.003$ and $0.08$ mean the bound overestimates the error by roughly one to two
orders of magnitude, while still predicting the growth with $n$ correctly. A
bound that is right about the *scaling* is the useful kind.

**(c)** No correct significant digits remain when the expected relative error
$\kappa_\infty u$ reaches about 1, i.e. $\kappa_\infty \gtrsim 9\times10^{15}$.
Computing $\kappa_\infty$ for the Hilbert matrix directly (float inverse,
solving for each unit vector) gives

| $n$ | $\kappa_\infty(H_n)$ | $\kappa_\infty u$ |
|---|---|---|
| $11$ | $1.231\times10^{15}$ | $0.137$ |
| $12$ | $3.832\times10^{16}$ | $4.25$ |
| $13$ | $4.636\times10^{17}$ | $51.5$ |

so the last correct digit is lost between $n = 11$ and $n = 12$. Beyond that,
the computed "solution" is noise dressed as numbers. This can be estimated
without running the solver by *computing $\kappa(A)$ first* — which is the
practical lesson: estimate the conditioning before trusting an answer, and use
$\kappa u$ as the accuracy you can expect.

**(d)** **Refutation.** "Exact inputs" guarantees only that no error is introduced
*before* the solve; it says nothing about how the problem responds to the
inevitable $\mathcal{O}(u)$ relative perturbation that a backward-stable
algorithm introduces, nor about the perturbation already present in the stored
values of $1/(i+j-1)$ (each is a rounded double). The forward error is bounded by
$\kappa(A)$ times the backward error, so with $\kappa_\infty \approx 3.5\times
10^{13}$ at $n = 10$, a backward error of $10^{-16}$ becomes a forward error of
about $10^{-4}$. The matrix, not the input list, is the problem.

---

## ★★7 — Amplification in the integral recurrence

**(a)** The recurrence is $I_n = 1/n - 10 I_{n-1}$. If $I_{n-1}$ is known with
error $\varepsilon_{n-1}$, the computed value inherits exactly $-10$ times that
error (the term $1/n$ and the factor $10$ are (nearly) exact operations):

$$|\varepsilon_n| = 10\,|\varepsilon_{n-1}| = 10^{n}|\varepsilon_0|.$$

After 8 steps an initial error is 100 million times larger; after 16 steps,
$10^{16}$ times larger.

**(b)** The value itself shrinks: roughly $I_n = \mathcal{O}(1/n)$
(measured $I_8 = 0.010194$, versus $I_0 = 0.095310$). The error exceeds the value
when

$$10^{n}u \gtrsim 1 \;\Longrightarrow\; n \gtrsim \log_{10}(1/u) = 15.95,$$

so about **16 steps**. Consistent with the measurement: the lecture's forward
relative error is $1.31\times10^{1}$ (1310%) at $n=15$.

**(c)** The naive model predicts $10^{8}u = 1.11\times10^{-8}$ at $n=8$; the
measured error is $7.34\times10^{-7}$ — larger by a factor of 66. Two
identifiable causes, and the second is a useful lesson in itself.

*Cause 1: amplification should be applied to the absolute error and compared
against the shrinking value.* If the starting value carries relative error
$\rho_0$, the relative error at step $n$ is

$$\rho_n = \rho_0 \cdot 10^{n} \cdot \frac{I_0}{I_n}.$$

With $I_0/I_8 = 0.095310/0.010194 = 9.35$, the amplification is
$9.35\times10^{8}$, not $10^{8}$: a factor of 9.35 accounted for.

*Cause 2: on this machine, `math.log(1.1)` is not accurate to $u$.* Measured:

$$\mathrm{rel\,error}\big(\texttt{math.log(1.1)}\big) = 7.85\times10^{-16}
= 7.07\,u = 5.4\ \text{ulps},$$

while `math.log1p(0.1)` is accurate to $0.39$ ulp. Using $\rho_0 = 7.07u$ and
the corrected amplification,

$$\rho_8 = 7.07u \times 9.35\times10^{8} = 7.34\times10^{-7},$$

which reproduces the measurement exactly. The lesson: an error budget written in
multiples of $u$ assumes correctly rounded elementary functions. **Actual
library functions are usually good to a fraction of an ulp, but not always**, and
an unstable recurrence multiplies whatever accuracy you actually got. This
particular figure is platform-dependent; check it on your own machine before
citing it.

*Supporting measurement.* Isolating the two error sources by replaying the
recurrence at 60-digit precision (a) starting from the float value of
`log(1.1)` and (b) starting from the exactly rounded value but rounding every
step to binary64:

| $n$ | error from the start value only | error from per-step rounding only |
|---|---|---|
| $4$ | $4.05\times10^{-11}$ | $6.64\times10^{-14}$ |
| $8$ | $7.34\times10^{-7}$ | $1.20\times10^{-9}$ |
| $12$ | $1.06\times10^{-2}$ | $1.74\times10^{-5}$ |

The initial error dominates by about two to three orders of magnitude, confirming
that the forward recurrence's sin is *amplification*, not accumulation.

**(d)** The backward recurrence

$$I_{n-1} = \frac{1}{10}\left(\frac{1}{n} - I_n\right)$$

divides any error in $I_n$ by 10 at each step (the division by 10 and the
subtraction of the exact $1/n$ are as accurate as the arithmetic allows). An
error $\varepsilon$ at $n = 20$ therefore contributes at most
$10^{-20}\varepsilon$ at $n = 0$. The lecture's starting estimate at $n=20$
carried a relative error of $4.15\times10^{-3}$; after 20 contraction steps the
relative error at $n=0$ is $8.87\times10^{-17}$ — full double precision, even
though the starting value was only good to three decimal places. Errors that
*contract* are free accuracy; errors that grow are fatal. Choosing the direction
is the whole design decision.

---

## ★★8 — Ranking measurements by relative uncertainty

| measurement | $\delta$ | $v$ | relative uncertainty |
|---|---|---|---|
| relative gravimeter | $0.01$ mGal | $979\,812.37$ mGal | $1.02\times10^{-8}$ |
| magnetometer | $1$ nT | $500$ nT | $2.0\times10^{-3}$ |
| GNSS baseline | $5$ mm | $10\,000$ m | $5.0\times10^{-7}$ |
| binary64 unit roundoff | — | — | $1.11\times10^{-16}$ |

Ranking, best to worst relative uncertainty:
gravimeter ($10^{-8}$), GNSS ($5\times10^{-7}$), magnetometer ($2\times10^{-3}$),
round-off ($10^{-16}$, irrelevant to all of them).

**Where round-off matters.** Compare each measurement uncertainty with $u$ by
ratio:

| measurement | ratio to $u$ |
|---|---|
| gravimeter | $9.2\times10^{7}$ |
| GNSS baseline | $4.5\times10^{9}$ |
| magnetometer | $1.8\times10^{13}$ |

All three are between 8 and 13 orders of magnitude larger than round-off, so
round-off is irrelevant to the *measurement* itself. It becomes relevant when
the measured quantity is a small difference of large modelled values (potential
fields, travel-time residuals) or when a long accumulation is involved — the
situations of lessons 01-01-04 and 01-01-05, Section 5.3.

---

## ★★★9 — Testing the perturbation bound on the Hilbert matrix

**(a)** Exact solution of $H_5 x = (1,1,1,1,1)$ from `fractions.Fraction`
elimination, converted to float:

$$x = (5,\ -120,\ 630,\ -1120,\ 630).$$

(Verified with `Fraction`: the exact solution of $H_5x = (1,1,1,1,1)$ is
integral. This is a property of this particular right-hand side, not a general
feature of Hilbert systems, and it is useful here because it gives a reference
solution with no rounding at all.)

**(b)–(c)** Perturbing in the alternating direction $v=(1,-1,1,-1,1)$:

| $\rho$ | $\|\Delta x\|_\infty/\|x\|_\infty$ | observed amplification |
|---|---|---|
| $10^{-3}$ | $3.69\times10^{-1}$ | $369$ |
| $10^{-6}$ | $3.69\times10^{-4}$ | $369$ |

The amplification is the *same* to three digits for both perturbations, which is
exactly what linear conditioning predicts: the forward error is proportional to
the data perturbation. A $0.1\%$ error in the right-hand side becomes a **37%**
error in the solution.

**(d)** $\kappa_\infty(A) = 9.437\times10^{5}$, so the bound predicts
$\kappa_\infty\rho = 943.7$ for $\rho = 10^{-3}$ and $9.437\times10^{-4}$ for
$\rho=10^{-6}$. The observed amplification is 369 in both cases, so the bound is
larger than the measurement by a factor of $943.7/0.369 = 2560$.

**(e)** With the constant direction $v = (1,1,1,1,1)$ the perturbed system is
$H(1+\rho)x = (1+\rho)b$, whose exact solution is $(1+\rho)x$ by linearity. The
relative change in the solution is therefore exactly $\rho$, and the
amplification is **1**. Measured: $1.000$ for both $\rho$. No computation is
needed — the observation follows from linearity, and this is a good reminder to
ask "what is this perturbation in the eigenbasis?" before trusting a bound.

**(f) Report.** The exercise shows that $\kappa(A)$ is a *worst-case* measure
over all perturbation directions, and that in the $\infty$-norm it is not
attained by a generic direction; the measured amplification for one direction can
be three orders of magnitude below the bound, and for another direction exactly 1.
What the bound guarantees is the *scaling*: doubling or thousand-folding $\rho$
multiplies the error by the same factor, and the error stays bounded by
$\kappa(A)\rho$. **Limits:** this is one matrix, one norm, two directions, and
the perturbations were applied to $b$ only; perturbing $A$ as well, or using the
2-norm, would give different numbers (for symmetric positive-definite matrices
the 2-norm condition number is the ratio of extreme eigenvalues and *is*
attained, by the corresponding singular vectors). Nothing here says the Hilbert
matrix is "bad" — only that any solver inherits its conditioning.

---

## ★★★10 — Conditioning a differential arrival time

**(a)** $\Delta t = 1.520 - 1.500 = 0.020$ s $= 20$ ms. With each pick carrying
$\pm1$ ms and taking the most pessimistic (same-sign) combination:

$$\frac{\delta(\Delta t)}{\Delta t} = \frac{2\ \mathrm{ms}}{20\ \mathrm{ms}}
= 0.10 = 10\%.$$

**(b)** The amplification of the differencing step:

$$\kappa = \frac{t}{\Delta t} = \frac{1.500}{0.020} = 75.$$

Each pick's relative uncertainty is $\varepsilon = 1\ \mathrm{ms}/1.500\
\mathrm{s} = 6.667\times10^{-4}$, so

$$\kappa\,\varepsilon = 75 \times 6.667\times10^{-4} = 5.0\times10^{-2} = 5\%.$$

**(c)** The two answers differ because they perturb different things.

- (a) perturbs **both** picks in the same direction, so the two errors add in
  $\Delta t$: $2$ ms out of 20 ms, i.e. 10%.
- (b) perturbs **one** pick only, which changes $\Delta t$ by 1 ms out of 20 ms:
  $5\%$.

The quadrature (independent, uncorrelated) combination is
$\sqrt{2}\times1\ \mathrm{ms} = 1.414$ ms, i.e. $7.07\%$ — between the two, as it
must be. Reporting the number that matches the physics matters more than any
convention: are the two picks independent, or are they dominated by a shared
clock offset? In (e) we see that the answer changes by a factor of $\sqrt2$ or
more.

**(d)** Setting $\kappa\varepsilon = 0.01$:

$$\frac{t}{\Delta t}\varepsilon = 0.01
\;\Longrightarrow\;
\Delta t = \frac{t\varepsilon}{0.01} = \frac{1.5 \times 6.667\times10^{-4}}{0.01}
= 0.100\ \mathrm{s} = 100\ \mathrm{ms}.$$

With 1 ms picks, the receiver spacing must give a differential arrival of at
least 100 ms — for a typical upper-crustal P-wave speed of order 5–6 km/s, that
means the receivers must be separated by hundreds of metres — before the
differential travel time is known to 1%. **Survey geometry is a conditioning
design decision**: spreading receivers widens $\Delta t$ and lowers $\kappa$,
which is why refraction spreads are laid out long.

**(e)** Correlated picks — same instrument, same clock offset, same operator
bias — do **not** cancel in $\Delta t$; they add fully, exactly as in (a). Only
the *independent* part of the noise is reduced by differencing, and by
$\sqrt{2}$ at that. So the relative uncertainty of $\Delta t$ is *larger* than
the quadrature estimate when the errors are correlated, which is why shared
timing errors (and, in seismic work, the source-time origin error) must be
characterised separately: no amount of receiver spacing fixes a common-mode
error.

---

## Notes on what these exercises do not settle

- The claim that `math.log(1.1)` carries about 7 u of error is an observation
  about the platform's C library. It is reproducible on the machine where these
  solutions were computed, and should be re-measured (two lines of code) before
  being quoted elsewhere. The *method* of isolating initial-value error from
  per-step rounding by replaying at high precision is portable and is the real
  content of the exercise.
- $\kappa_\infty$ values for the Hilbert matrix were computed by inverting the
  float matrix and taking row-sum norms. They are therefore themselves affected by
  round-off at large $n$; treat the values at $n \ge 12$ as order-of-magnitude
  estimates. The conclusion — that no digits survive past $n \approx 12$ — is
  robust to that uncertainty because it is a statement about an order of
  magnitude.
- No claim is made about the conditioning of any specific published tomographic
  or geodetic system; those numbers depend on the data and must be measured for
  the problem at hand.
