# Solutions — 01-02-03 Exponentials, Logarithms and Decay Laws in Earth Science

> **Read this after attempting the exercises, not before.**
>
> Numeric values were computed with the standard library. Half-lives used are the
> conventionally quoted ones and are labelled as such; where a value is a
> convention rather than a measurement, that is stated.

---

## ★1 — Conversions between the three parameters

The bridge identity is $\lambda T_{1/2} = \ln 2$, equivalently
$T_{1/2} = \ln 2/\lambda$ and $\tau = 1/\lambda = T_{1/2}/\ln 2$.

**(a)** $\lambda = \dfrac{\ln 2}{5730} = \dfrac{0.693147}{5730}
= 1.209681\times10^{-4}\ \mathrm{yr^{-1}}$.

**(b)** $T_{1/2} = \dfrac{\ln 2}{0.05} = 13.8629$ **days**.

**(c)** With $\lambda = 0.3\ \mathrm{day^{-1}}$, $T_{1/2} = \ln 2/0.3
= 2.310491$ days, so

$$N(t) = 100 \cdot 2^{-t/2.310491}.$$

**Check:** at $t = 2.310491$ the exponent is $-1$ and $N = 50$; the original form
gives $100e^{-0.3\times2.310491} = 100e^{-0.693147} = 50.000$. ✓

**(d)** $T_{1/2} = \tau\ln 2 = 8266.6 \times 0.693147 = 5729.9$ **yr**, which is
the $5730$ yr half-life to three significant figures. This is a useful internal
consistency check: the mean life and the half-life of $^{14}$C printed in the
demonstration are two views of the same constant, and $\tau/T_{1/2} = 1/\ln 2 =
1.4427$.

---

## ★2 — Down to 0.1% remaining

**(a)** Requiring $N/N_0 = 10^{-3} = 2^{-n}$:

$$n = \frac{\ln 10^{3}}{\ln 2} = \frac{6.907755}{0.693147} = 9.9658
\ \text{half-lives}.$$

**(b)** $t = 9.9658 \times 5730 = 57103.9$ **yr**. Equivalently
$t = \ln(10^{3})/\lambda = 6.907755/1.209681\times10^{-4} = 57104$ yr.

**(c)** The arithmetic is happy at 0.1%, but the *measurement* is not. With 0.1%
of the original activity left, the count rate is near the detection limit, the
blank correction and modern carbon contamination dominate, and the uncertainty on
the ratio grows as the ratio shrinks. In practice, radiocarbon dating is limited
to roughly $5\times10^{4}$ yr — close to ten half-lives — for exactly this
reason, and the precise limit depends on the laboratory and the sample. The
exercise shows where the *mathematics* permits a number and the *measurement*
does not.

---

## ★3 — Logarithm laws

| expression | value | law used |
|---|---|---|
| $\ln e^{3}$ | $3$ | $\ln$ and $e^{\cdot}$ are inverses |
| $\ln 1$ | $0$ | $e^{0} = 1$ |
| $\ln(1/e)$ | $-1$ | $\ln a^{-1} = -\ln a$ |
| $\log_{10}1000$ | $3$ | $10^{3} = 1000$ |
| $\ln(a^{2}b/c)$ | $2\ln a + \ln b - \ln c$ | product, quotient and power rules |

**Remark on the fourth row.** $\log_{10}$ and $\ln$ differ only by the constant
$1/\ln 10 = 0.434294$: $\log_{10}x = \ln x/\ln 10$. Choosing base 10 for reporting
is a convention (and the reason the decibel exists); choosing base $e$ for
calculus is not.

---

## ★4 — Evaluating and characterising an exponential

For $N(t) = 100e^{-0.3t}$:

| $t$ | $N$ |
|---|---|
| $0$ | $100.0000$ |
| $1$ | $74.0818$ |
| $2$ | $54.8812$ |
| $5$ | $22.3130$ |

Successive ratios at unit steps:

$$\frac{74.0818}{100} = \frac{54.8812}{74.0818} = 0.740818 = e^{-0.3}.$$

The series has a **constant ratio**, not a constant difference (the differences
are $-25.918$, $-19.201$, $-32.568$ — no pattern). Constant ratio is the signature
of an exponential, exactly as constant difference is the signature of a linear
function. This test — divide successive values — is the quickest way to recognise
exponential behaviour in a table.

---

## ★★5 — Age from an activity ratio

**(a)** $N/N_0 = e^{-\lambda t}$ with $\lambda = 1.209681\times10^{-4}$:

$$t = -\frac{\ln(0.25)}{1.209681\times10^{-4}} = \frac{1.386294}{1.209681\times10^{-4}}
= 11460.0\ \mathrm{yr}.$$

**(b)** $0.25 = 1/4 = 2^{-2}$, so two half-lives have elapsed, giving exactly
$2\times5730 = 11460$ yr. The general statement: any ratio of the form $2^{-n}$
gives an age of exactly $n$ half-lives, because the $\ln 2$ in the numerator and
in $\lambda$ cancel. This is why half-lives, rather than years, are the natural
unit for thinking about decay.

**(c)** A laboratory would apply at least:

1. **Isotopic fractionation normalisation** (the $\delta^{13}$C correction), which
   accounts for the fact that biological and physical processes fractionate carbon
   isotopes, so a sample's $^{14}$C/$^{12}$C ratio is not identical to the
   atmosphere's.
2. **Calibration** using a measured calibration curve, which converts the
   "conventional radiocarbon age" into a calendar age. The curve exists because
   atmospheric $^{14}$C production has varied with time (geomagnetic field,
   solar activity, the industrial and bomb effects).
3. Where relevant, a **reservoir or marine correction**, which can shift marine and
   lacustrine ages by centuries to millennia.

None of these is an arithmetic step: they are model corrections, and they are why
a reported radiocarbon date comes with a laboratory code and a calibration curve
version.

**Scope note.** The number in (a) is a *conventional* age from a simple
exponential model, and it assumes a constant atmospheric $^{14}$C level. It is a
legitimate intermediate quantity, not a date.

---

## ★★6 — The isochron derivation

**(a)** $P(t) = P_0e^{-\lambda t}$, and with no initial daughter,
$D^{*}(t) = P_0 - P(t) = P_0\left(1 - e^{-\lambda t}\right)$.

**(b)** Dividing,

$$\frac{D^{*}}{P} = \frac{P_0(1-e^{-\lambda t})}{P_0e^{-\lambda t}}
= \frac{1-e^{-\lambda t}}{e^{-\lambda t}} = e^{\lambda t} - 1.$$

The unknown $P_0$ cancels, which is the whole point: we cannot weigh the original
amount of parent, but we can measure the present ratio.

**(c)** $e^{\lambda t} = 1 + D^{*}/P$, hence

$$t = \frac{1}{\lambda}\ln\!\left(1 + \frac{D^{*}}{P}\right).$$

**(d)** For $^{238}$U, $T_{1/2} = 4.468\times10^{9}$ yr gives

$$\lambda = \frac{\ln 2}{4.468\times10^{9}} = 1.551359\times10^{-10}\ \mathrm{yr^{-1}},$$

$$t = \frac{\ln(1.5)}{1.551359\times10^{-10}} = \frac{0.405465}{1.551359\times10^{-10}}
= 2.6136\times10^{9}\ \mathrm{yr} = 2613.6\ \mathrm{Ma}.$$

**Sanity check.** $D^{*}/P = 1$ gives $t = \ln 2/\lambda = T_{1/2} = 4468.0$ Ma,
and indeed half the parent has decayed when the daughter/parent ratio reaches one.
The demonstration's table prints exactly this value.

**(e)** The linear form is obtained by taking logarithms of the isochron equation:

$$1 + \frac{D^{*}}{P} = e^{\lambda t}
\qquad\Longrightarrow\qquad
\ln\!\left(1 + \frac{D^{*}}{P}\right) = \lambda t.$$

Plotting $\ln(1 + D^{*}/P)$ against $t$ gives a straight line through the origin
with slope $\lambda$ — and, crucially, this is the form that can be fitted to many
samples at once. In practice, several minerals from the same rock are analysed and
plotted together, and the slope of the best-fit line gives the age while the
intercept tests the "no initial daughter" assumption. That is why the method is
called an *isochron*: same age, hence iso-chron.

**(f)** Assumptions and the direction of bias if each is violated:

| assumption | if violated | effect on the age |
|---|---|---|
| no initial daughter | some daughter was present at $t=0$ | measured ratio too high → age **too old** |
| closed system for the parent | parent was lost or gained | parent lost → ratio too high → **too old**; parent gained → **too young** |
| closed system for the daughter | daughter was lost or gained | daughter lost → ratio too low → **too young** |
| the measured daughter is all radiogenic | a non-radiogenic contribution | ratio too high → **too old** |
| $\lambda$ constant | exotic variation | no practical effect for these nuclides; a change in $\lambda$ rescales the age directly |

The practical value of a multi-mineral isochron is that a non-zero intercept
*detects* initial daughter directly, rather than assuming its absence. That is a
model check, available because more than one measurement was made — the same logic
as an over-determined fit in
[01-13 Probability and Statistics Foundations](../../13-probability-and-statistics-foundations/README.md).

---

## ★★7 — Attenuation and $Q$

**(a)** With $f = 20$ Hz, $v = 3500$ m/s, $Q = 100$:

$$\alpha = \frac{\pi f}{Qv} = \frac{\pi \times 20}{100 \times 3500}
= 1.795196\times10^{-4}\ \mathrm{m^{-1}}, \qquad
\frac{1}{\alpha} = 5570.4\ \mathrm{m}.$$

**(b)**

| $x$ (m) | $A/A_0 = e^{-\alpha x}$ |
|---|---|
| $100$ | $0.982208$ |
| $500$ | $0.914151$ |
| $1000$ | $0.835672$ |

**(c)** With $A(500)/A(100) = 0.930710$:

$$Q = -\frac{\pi f (x_2 - x_1)}{v\ln\!\big(A(x_2)/A(x_1)\big)}
= -\frac{\pi\times20\times400}{3500 \times \ln(0.930710)}
= \frac{25132.7}{3500\times0.071817} = 100.000.$$

The recovery is exact because the synthetic ratio was generated from $Q = 100$ and
no noise was added. With real amplitudes the logarithm of a ratio near 1 is
sensitive to small errors, which is the practical reason $Q$ estimates from
spectral ratios have large uncertainties.

**(d)** The factor of 2 comes from the fact that **energy** decays as the square of
the amplitude: the standard statement is that the fractional energy loss per cycle
is $2\pi/Q$, so the amplitude decays at half that rate, giving $\alpha = \pi
f/(Qv)$.

---

## ★★8 — Newton cooling

**(a)** $T(t) = 10 + 890\,e^{-t/4}$ with $t$ in days:

| $t$ (days) | $T$ (°C) |
|---|---|
| $0$ | $900.0000$ |
| $4$ | $337.4127$ |
| $8$ | $130.4484$ |

The *excess* over ambient decays by a factor $e$ every 4 days: $890$, $327.41$,
$120.45$ °C.

**(b)**

$$t = -4\ln\!\left(\frac{200 - 10}{900 - 10}\right)
= -4\ln(0.213483) = 6.1768\ \text{days}.$$

**Check:** $T(6.1768) = 10 + 890e^{-1.54420} = 200.0000\,^\circ$C. ✓

**(c)** $\tau = 4$ days is the **e-folding time**: the time for the temperature
*excess* to fall by a factor $e$. It is not the half-life, which is the time for
the excess to fall by a factor 2:

$$T_{1/2} = \tau\ln 2 = 2.7726\ \text{days}.$$

The two differ by the factor $\ln 2 = 0.693$: a common and avoidable confusion,
and one worth checking in any code that mixes the two vocabularies.

**(d)** The lumped-parameter model assumes the body has a **uniform internal
temperature** and exchanges heat at a rate proportional to the excess. A real
intrusion has a temperature *gradient* inside it and loses heat by conduction into
the country rock, so the cooling is a diffusion problem, not a single exponential.
The correct treatment solves the heat equation (with the appropriate geometry:
half-space, sheet, or sphere), giving solutions built from error functions or
series; the single exponential is the correct limit only once the internal
gradients have been erased, and it is an approximation everywhere else. It is still
useful — but it is a model, and the time constant obtained from it is a
lumped-parameter time constant, not a diffusion time.

---

## ★★★9 — A single exponential fitted to a mixture

**(a)** $\lambda_1 = \ln2/5 = 0.138629\ \mathrm{day^{-1}}$ (half-life 5 days) and
$\lambda_2 = \ln2/100 = 0.006931\ \mathrm{day^{-1}}$ (half-life 100 days). The
**slow** component (half-life 100 days) dominates at $t\to\infty$, because the fast
component decays away first.

**(b)** Single-exponential least-squares fits of $\ln N$ against $t$:

| window (days) | apparent $\lambda$ (day⁻¹) | implied $T_{1/2}$ (days) | $R^{2}$ |
|---|---|---|---|
| $[1, 20]$ | $0.052453$ | $13.21$ | $0.96796$ |
| $[1, 50]$ | $0.023154$ | $29.94$ | $0.84568$ |
| $[1, 200]$ | $0.008350$ | $83.01$ | $0.92038$ |
| $[1, 1000]$ | $0.006993$ | $99.13$ | $0.99866$ |

**(c)** The apparent decay constant approaches $\lambda_2 = 0.006931$ (half-life
100 days) as the window lengthens, and never approaches $\lambda_1$. This is the
expected behaviour: a single exponential fitted to a sum is dominated by the
slowest component at long times, and by whichever component contributes most
*within the fitted window* at short times.

**(d)** The window length dominates because it decides which component is still
present. In the 20-day window the fast component contributes most of the signal,
and the fitted slope reflects a mixture heavily weighted towards it, giving an
apparent half-life of 13 days — which is **neither** of the true half-lives, and
which would be reported as a physical property of the sample if the mixture were
not suspected. Note also that $R^{2}$ is *highest* for the longest window
(0.99866), even though the log-linear model is formally wrong there: a mixture of
two similar decays looks very nearly straight over a few decades, and $R^{2}$ does
not detect the model error. For real data this means: a decay constant is only
interpretable alongside the fitted window, and a "linear" semilog plot is not
evidence that a single process is at work.

**(e) Limits.** The result depends on the *ratio* $A/B$ and on the separation of
the two constants. Reversing the ratio to $A/B = 0.5$ would put the slow component
in the majority from the start and the apparent constant would sit closer to
$\lambda_2$ in every window. Separating the components by only a factor of two in
half-life would make the sum barely distinguishable from a single exponential over
any practical window, and the fitted constant would then be near the weighted mean
of the two. Nothing here establishes a general formula for the bias; it
demonstrates that the bias exists, that it is a *method* error rather than a noise
error (the data are exact), and that it is controlled by the window.

---

## ★★★10 — Telling an exponential from a power law

**(a)** Two synthetic series on $t = 1, \dots, 100$:
$y_{\exp} = 100e^{-0.02t}$ and $y_{\text{pow}} = 1000(t+1)^{-1.5}$.

**(b)** Straight-line fits in the two coordinate systems (with $R^{2}$ of the fit
to $\ln y$):

| data set | $R^{2}$ of $\ln y$ vs $t$ (semilog) | $R^{2}$ of $\ln y$ vs $\ln t$ (log–log) |
|---|---|---|
| $y_{\exp}$ | $1.00000$ | $0.80256$ |
| $y_{\text{pow}}$ | $0.83674$ | $0.99670$ |

**(c)** Yes: the larger $R^{2}$ identifies the correct family in both cases, and the
contrast is decisive — the correct coordinate system gives $R^{2}$ above 0.996
while the wrong one gives below 0.84. But note the second part of the question:
the exponential data are *poorly* fit by the log–log line ($R^{2} = 0.80$) while
the power-law data are *moderately* well fit by the semilog line
($R^{2} = 0.84$). So the discrimination is asymmetric: "straight on a semilog plot"
is much weaker evidence against a power law than the converse.

**(d)** $R^{2}$ alone is dangerous because it measures how well a line fits the
*transformed* data, not which model is physically right, and because a shifted or
truncated data range can make either family look acceptable. A better procedure is
to (i) fit both candidate models and compare **residuals as a function of $t$** — a
systematic curvature in the residuals betrays the wrong family — and (ii) test the
two models against each other with an information criterion on the *untransformed*
data, so that both are judged on the same scale. On real data, also check whether
the data range covers more than one or two decades: over a narrow range almost
anything looks straight.

**(e) Report.** *Method:* two synthetic series, one from each family, fitted by
ordinary least squares in both coordinate systems, with $R^{2}$ computed on the
log-independent variable. *Results:* as tabulated; the correct family wins in both
cases by a wide margin. *Limits:* the outcome depends on the amplitudes chosen
(over this range the power law spans about 2.5 decades — from $353.6$ at $t=1$ to
$0.985$ at $t=100$ — while the exponential spans under one, from $98.0$ to
$13.5$), on the fitted range $t \in [1,100]$, and on the absence of noise. Adding
multiplicative noise of even a few per cent would reduce the semilog $R^{2}$ of the
exponential data by a visible amount while leaving the *ordering* of the four
values intact — but the margins, not the ordering, are what a real decision would
depend on.

---

## Notes on what these solutions do not settle

- The half-lives used ($^{14}$C: 5730 yr; $^{238}$U: $4.468\times10^{9}$ yr) are
  the values commonly quoted in the literature. They are quoted here as
  conventional constants for arithmetic, and a dating laboratory would use its own
  evaluated values and uncertainties; the difference is small but it is real, and
  an age should always be reported with the constants used.
- Nothing here treats the *measurement* uncertainty of a ratio or an amplitude.
  Every age and every $Q$ computed above is an error-free calculation from an
  assumed input; propagating real uncertainties is a separate skill, developed in
  [01-13 Probability and Statistics Foundations](../../13-probability-and-statistics-foundations/README.md).
- The constant-$Q$ attenuation model is the standard one and is used with its
  derivation sketched, not proven, in Section 5.2 of the lesson; the full
  treatment requires the theory of anelasticity.
- The statement that radiocarbon dating is limited to roughly $5\times10^{4}$ yr is
  a commonly used rule of thumb that depends on sample size, laboratory, and
  contamination; it is given as orientation, not as a specification.
