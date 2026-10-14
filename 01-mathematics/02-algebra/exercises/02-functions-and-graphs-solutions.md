# Solutions — 01-02-02 Functions, Graphs and Transformations

> **Read this after attempting the exercises, not before.**
>
> Numeric values were computed with the standard library. Where a function is
> defined only on part of the real line, the domain is stated as part of the
> answer, because a function without its domain is not a function.

---

## ★1 — Domains

| function | natural domain | physical reason |
|---|---|---|
| $GM/d^{2}$ | $d \ne 0$, i.e. $d > 0$ for a depth | the field diverges at the source; a depth is non-negative |
| $\ln(D/D_0)$ | $D/D_0 > 0$, i.e. $D > 0$ and $D_0 > 0$ | the argument of a logarithm must be positive; a ratio of activities or amplitudes is |
| $\sqrt{GM/g}$ | $g > 0$ (and $M \ge 0$) | the quantity under the root must be non-negative; a negative gravity anomaly does not prevent a square root here, but $g = 0$ does |
| $1/(1+x^{2})$ | all of $\mathbb{R}$ | the denominator never vanishes |

**Note on (b).** The logarithm's domain excludes *zero* as well as negatives. In
a decay problem the ratio $D/D_0$ can approach zero but never reach it, so the
logarithm becomes large and negative without bound — which is why ages from
activity ratios become unreliable long before the ratio is exactly zero.

---

## ★2 — Identifying the family

**Table A: linear.** Successive differences are constant: $7-5 = 9-7 = 11-9 = 2$.
So $m = 2$ and $f(0) = 5$:

$$f(x) = 5 + 2x.$$

**Table B: exponential.** Successive *ratios* are constant: $6/3 = 12/6 = 24/12
= 2$. So the base factor is 2 and the initial value is 3:

$$f(x) = 3 \cdot 2^{x} = 3e^{x\ln 2}.$$

**Table C: quadratic.** First differences are $1, 3, 5$ — not constant; second
differences are $2, 2$ — constant, which is the signature of a quadratic. With
second difference $2a = 2$ we have $a = 1$; then $f(0) = 1$ and $f(1) = 2$ give
$b = 0$, $c = 1$:

$$f(x) = x^{2} + 1.$$

**The operational rule.** Test *differences* for a polynomial and *ratios* for an
exponential. This is the discrete version of the statement in Section 3 of the
lesson: a polynomial has constant differences of some order, an exponential has
constant ratios.

---

## ★3 — Transformations of the bump

$f(x) = 1/(1+x^{2})$ has its maximum at $x = 0$, with $f(0) = 1$.

| transformation | peak position | peak height | survey operation |
|---|---|---|---|
| $f(x-3)$ | $x = 3$ | $1.0$ | a body offset by 3 units in position |
| $f(x) + 0.5$ | $x = 0$ | $1.5$ | a uniform baseline added to the anomaly |
| $f(2x)$ | $x = 0$ | $1.0$ | compression of the horizontal scale (finer sampling of the same shape) |
| $-f(x)$ | $x = 0$ (now a minimum) | $-1.0$ | polarity reversal |

All four were confirmed numerically by the demonstration, which prints exactly
these peak heights.

**Why the minus sign acts inside.** $f(x-3)$ has its maximum where its *argument*
is zero, i.e. $x - 3 = 0$. The graph therefore moves to $x = 3$, to the right,
even though the formula contains a minus sign. Reading a shift off the formula
means solving for the argument, not copying the sign.

---

## ★4 — Even, odd, neither

| function | $f(-x)$ | classification |
|---|---|---|
| $x^{3}$ | $-x^{3}$ | **odd** |
| $x^{2}$ | $x^{2}$ | **even** |
| $x^{3} + x$ | $-(x^{3}+x)$ | **odd** |
| $1 + x + x^{3}$ | $1 - x - x^{3}$ | **neither** |
| $e^{x}$ | $e^{-x}$ | **neither** |

A sum of even functions is even, and a sum of odd functions is odd; mixing the two
gives neither.

**Splitting $f(x) = 2 + x + x^{2}$.** With $f(-x) = 2 - x + x^{2}$:

$$f_e(x) = \frac{f(x)+f(-x)}{2} = \frac{(2+x+x^{2}) + (2-x+x^{2})}{2} = 2 + x^{2},$$

$$f_o(x) = \frac{f(x)-f(-x)}{2} = \frac{(2+x+x^{2}) - (2-x+x^{2})}{2} = x.$$

**Check at $x = 3$:** $f(3) = 14$, $f_e(3) = 11$, $f_o(3) = 3$, and
$11 + 3 = 14$. ✓

**Why this is more than an exercise.** If a gravity profile measured across a
suspected body is decomposed this way, the even part is the signature of a
centred body and the odd part indicates a contact, a fault or a dip. The
decomposition is a real interpretation tool, and
[01-10 Fourier Analysis](../../10-fourier-analysis/README.md) generalises it to the
frequency domain.

---

## ★★5 — Inverses

**(a)** $t = 2d/v \Rightarrow d = vt/2$, on the domain $t \ge 0$ with range
$d \ge 0$. The function is strictly increasing in $d$ (for $v>0$), so the inverse
exists and is unique.

**(b)** Isolate the exponential:

$$T - T_\infty = (T_0 - T_\infty)e^{-t/\tau}
\;\Longrightarrow\;
e^{-t/\tau} = \frac{T - T_\infty}{T_0 - T_\infty},$$

$$t = -\tau\ln\!\left(\frac{T - T_\infty}{T_0 - T_\infty}\right).$$

Conditions: $\tau > 0$; $T_0 \ne T_\infty$ (otherwise there is no cooling to
invert); and $0 < T - T_\infty < T_0 - T_\infty$ for a finite positive time. The
strict inequalities matter: $T = T_\infty$ gives infinite time and
$T = T_0$ gives $t=0$, both as limits rather than attained values.

**(c)** With $T_\infty = 10$, $T_0 = 900$, $\tau = 4$ days, $T = 100$:

$$t = -4\ln\!\left(\frac{100-10}{900-10}\right) = -4\ln(0.1011236)
= 9.166\ \text{days}.$$

**Check by substitution:** $T(9.166) = 10 + 890\,e^{-9.166/4} = 100.000$ °C,
which the demonstration confirms to six decimals.

**(d)** Physically, every moment of time after emplacement corresponds to exactly
one temperature of the body (which is monotonically decreasing towards the
ambient temperature), and every temperature between the initial value and ambient
occurs at exactly one time. That one-to-one correspondence *is* invertibility. If
the body were being heated and then cooled, the temperature would be visited
twice and the time would not be recoverable from temperature alone — which is why
the sign of the temperature trend must be known independently.

---

## ★★6 — Asymptotes

**(a)** $\dfrac{3x^{2}+2x}{x^{2}+5}$. Degrees are equal, so divide by $x^{2}$:
$\dfrac{3 + 2/x}{1 + 5/x^{2}} \to 3$. **Horizontal asymptote $y = 3$.** The
denominator never vanishes, so there is no vertical asymptote.

**(b)** $\dfrac{x+1}{x^{2}-4}$. Denominator zero when $x = \pm2$, numerator
nonzero there ($3$ and $-1$), so **vertical asymptotes $x = 2$ and $x = -2$**.
Denominator degree exceeds numerator degree, so the **horizontal asymptote is
$y = 0$**.

**(c)** $\dfrac{z}{1+z} = \dfrac{1}{1 + 1/z} \to 1$. **Horizontal asymptote
$y = 1$**, with a **vertical asymptote at $z = -1$**, which lies outside the
physical domain $z \ge 0$.

**(d)** $1 - \dfrac{z}{1+z} = \dfrac{1}{1+z}$. Requiring
$\dfrac{1}{1+z} < 10^{-4}$ gives

$$1 + z > 10^{4} \quad\Longrightarrow\quad z > 9999,$$

so $z = 10^{4}$ is the first round value that satisfies it. Verified:
$z/(1+z) = 0.9999000100$ at $z = 10^{4}$, so the residual is
$9.999\times10^{-5} < 10^{-4}$. ✓

**Comment.** The residual goes as $1/z$, so each additional decimal digit of
accuracy costs a factor of ten in $z$. This is the practical shape of every
"far-field" approximation: cheap accuracy is not available.

---

## ★★7 — Average rates of change

**(a)** $T(z) = 10 + 25z$:

| interval | average rate (°C/km) |
|---|---|
| $[0, 1]$ | $25.0$ |
| $[1, 2.5]$ | $25.0$ |
| $[2.5, 5]$ | $25.0$ |

The rate is the same on every interval — the defining property of a linear
function. On a temperature log, a straight segment therefore means a constant
gradient, and a change of slope is a change in regime (conductivity contrast, an
advective zone, or a climatic transient), not merely a change of value.

**(b)** For $f(x) = x^{2}$ on $[1, 1+h]$:
$(f(1+h)-f(1))/h = (2h + h^{2})/h = 2 + h$.

| interval | $h$ | average rate |
|---|---|---|
| $[1,2]$ | $1$ | $3.0$ |
| $[1,1.1]$ | $0.1$ | $2.1$ |
| $[1,1.01]$ | $0.01$ | $2.01$ |

(Observed values: $2.100000000000002$ and $2.0100000000000007$, the small excess
being round-off in the subtraction.)

**(c)** The rates approach $2$. That number is the **derivative** $f'(1) = 2$ — the
slope of the tangent, defined as the limit of the secant slopes. Note the structure
of the calculation: $2 + h$ *is* the exact average rate, and the limit is visible
in it without any numerical experiment. This is the subject of
[01-05 Single-Variable Calculus](../../05-single-variable-calculus/README.md).

---

## ★★8 — Composition

**(a)** $f(g(x)) = 2(x+1) = 2x+2$ and $g(f(x)) = 2x + 1$. At $x=3$ the values are
**8** and **7**: composition does not commute.

**(b)** Substituting the depth–time relation into the velocity model:

$$v(t) = v_0 + k\big(z_0 + ut\big) = (v_0 + kz_0) + ku\,t.$$

This is still **linear in $t$**, because a linear function composed with a linear
function is linear. The composite slope is $ku$: the rate of velocity change in
time equals the rate of change with depth times the rate of change of depth with
time — the chain rule, appearing already at this level.

**(c)** In a processing chain the order encodes physics. If a rock-physics law maps
porosity to velocity, and a compaction law maps depth to porosity, then velocity
as a function of depth must be built as "compaction first, then rock physics". The
reverse order asks the rock-physics law to accept a depth as input, which is
meaningless. Changing the order changes the model — and, as (a) shows numerically,
changes the numbers.

---

## ★★★9 — How slowly $\left(1+1/z\right)^{z}$ approaches $e$

**(a)**

| $z$ | $\left(1+1/z\right)^{z}$ | $r(z) = e - (\cdot)$ | $z\,r(z)$ |
|---|---|---|---|
| $10$ | $2.593742460$ | $1.245\times10^{-1}$ | $1.245394$ |
| $10^{2}$ | $2.704813829$ | $1.347\times10^{-2}$ | $1.346800$ |
| $10^{3}$ | $2.716923932$ | $1.358\times10^{-3}$ | $1.357896$ |
| $10^{4}$ | $2.718145927$ | $1.359\times10^{-4}$ | $1.359016$ |
| $10^{5}$ | $2.718268237$ | $1.359\times10^{-5}$ | $1.359127$ |
| $10^{6}$ | $2.718280469$ | $1.359\times10^{-6}$ | $1.359363$ |

**(b)** Yes: $z\,r(z)$ settles at about $1.359$, with $e/2 = 1.359141$. So
$r(z) \approx e/(2z)$: the error decays like $1/z$, not like $1/z^{2}$ and not
exponentially.

**(c)** The standard correction follows from expanding the logarithm:

$$\ln\!\left(1+\frac{1}{z}\right)^{z}
= z\ln\!\left(1+\frac{1}{z}\right)
= z\left(\frac{1}{z} - \frac{1}{2z^{2}} + \frac{1}{3z^{3}} - \cdots\right)
= 1 - \frac{1}{2z} + \frac{1}{3z^{2}} - \cdots,$$

so

$$\left(1+\frac{1}{z}\right)^{z}
= e^{1 - 1/(2z) + O(1/z^{2})}
= e\left(1 - \frac{1}{2z} + O\!\left(\frac{1}{z^{2}}\right)\right),$$

and the residual is $r(z) = e/(2z) + O(1/z^{2})$. The measured values of $z\,r(z)$
are within $0.02\%$ of $e/2$ at $z = 10^{5}$ and converge towards it from below,
exactly as the $+O(1/z^{2})$ term predicts. (The expansion of $\ln(1+\cdot)$ used
here is the standard Mercator series, derived in
[01-05 Single-Variable Calculus](../../05-single-variable-calculus/README.md).)

**(d) Limits of the conclusion.** The fit was made over $z \in [10, 10^{6}]$; the
coefficient $e/2$ was identified by numerical agreement, and the theoretical
formula above is quoted from the standard logarithmic series rather than
re-derived from scratch here. As $z$ grows further, `1 + 1/z` eventually rounds to
exactly `1.0`, at which point the computed value is exactly 1 and the whole
expression is useless. That happens when $1/z < u = 2^{-53}$, i.e.
$z \gtrsim 9\times10^{15}$ — the *computation*, not the mathematics, gives out
first. Verify it on your machine by evaluating
`(1.0 + 1.0/1e17) ** 1e17` and comparing with 1.

---

## ★★★10 — The profile of a buried mass

**(a)** At $x = 0$, $g(0) = GMh/h^{3} = GM/h^{2}$. At $x = h$,

$$g(h) = \frac{GMh}{(2h^{2})^{3/2}} = \frac{GMh}{2^{3/2}h^{3}}
= \frac{GM}{2\sqrt{2}\,h^{2}} = \frac{g(0)}{2\sqrt{2}},$$

so $g(h)/g(0) = 1/(2\sqrt{2}) = 0.353553$. The anomaly has already fallen to 35%
of its peak at an offset equal to the depth.

**(b)** Set $g(x)/g(0) = 1/2$. Since

$$\frac{g(x)}{g(0)} = \left(1 + \frac{x^{2}}{h^{2}}\right)^{-3/2},$$

taking both sides to the $-2/3$ power gives

$$2^{2/3} = 1 + \frac{x_{1/2}^{2}}{h^{2}}
\quad\Longrightarrow\quad
x_{1/2} = h\sqrt{2^{2/3} - 1} = 0.766421\,h,$$

and inverting, $h = x_{1/2}/0.766421 = 1.304766\,x_{1/2}$ — the familiar "depth is
about 1.3 times the half-width" rule for a compact body.

**(c)** With $x/h = u$, $g/g(0) = (1+u^{2})^{-3/2}$:

| $x/h$ | $g/g(0)$ |
|---|---|
| $0$ | $1.000000$ |
| $0.5$ | $0.715542$ |
| $1$ | $0.353553$ |
| $2$ | $0.089443$ |
| $5$ | $0.007543$ |
| $10$ | $0.000985$ |

These are the values printed by `code/polynomials_roots_demo.py` (Section 6) for
$h = 500$ m, $M = 10^{12}$ kg.

**(d)** For $x \gg h$,

$$\frac{g(x)x^{3}}{GMh} = \frac{x^{3}}{(x^{2}+h^{2})^{3/2}}
= \left(1 + \frac{h^{2}}{x^{2}}\right)^{-3/2} \to 1,$$

so $g \sim GMh/x^{3}$ in the far field: the profile decays one power of $x$ faster
than the anomaly directly above the source. Measured values: $0.942866$ at
$x/h = 5$, $0.985185$ at $x/h = 10$. To reach $1 - 3\times10^{-3}$ one needs
$\tfrac{3}{2}(h/x)^{2} \lesssim 3\times10^{-3}$, i.e. $x/h \gtrsim 22$. The
practical reading: the far-field form is a *bad* description inside a few depths
of the body, which is exactly where the target tends to be.

**(e)** For a uniform sphere the external field is exactly that of a point mass at
the centre, so the half-width rule returns the depth **to the centre** — not to the
top, and not to the middle of the *anomalous* mass. For a sphere of radius $R$ whose
top is at depth $z_{\text{top}}$, the rule returns $h = z_{\text{top}} + R$, and
the difference between that and the top depth is the entire radius.

The geometry matters more than that. For an infinite horizontal cylinder of mass
per unit length $\lambda$ with axis at depth $h$, the standard anomaly is
$g(x) \propto h/(x^{2}+h^{2})$, so

$$\frac{g(x)}{g(0)} = \left(1 + \frac{x^{2}}{h^{2}}\right)^{-1}
= \frac{1}{2} \;\Longrightarrow\; x_{1/2} = h.$$

A cylinder's anomaly is **wider** than a sphere's at the same depth
($x_{1/2} = h$ versus $0.766h$). Applying the sphere rule to a cylinder's anomaly
therefore returns $1.3048\,h$ instead of $h$: a **30% overestimate** of the depth.
Conversely, a body more compact than a sphere would be underestimated. The
half-width is a *shape-dependent* depth indicator, and quoting it without stating
the assumed geometry is not a result.

*(Caveat: the cylinder anomaly quoted here is the standard infinite-horizontal-
cylinder result, not derived in this module. It is used only to exhibit the
geometry dependence, which the algebra of the half-width already establishes.)*

**(f) Report.** *Method:* the profile formula $g(x) = GMh/(x^{2}+h^{2})^{3/2}$,
evaluated in binary64 and checked against the closed forms derived in (a), (b) and
(d); the demo's table provides the numbers for $h = 500$ m, $M = 10^{12}$ kg.
*Numbers:* as tabulated in (c) and quoted in (d). *Trend:* the profile is flat only
within $x \lesssim h/2$, falls to 35% at $x = h$, and follows $1/x^{3}$ beyond
$x \approx 20h$. *Limits:* the analysis assumes a point mass or uniform sphere,
a flat surface at the observation level, and no regional field. For an extended
body of any other shape the profile is the *convolution* of shape and depth, and
the half-width alone cannot separate the two; that separation is the classical
non-uniqueness of potential-field interpretation, and it is why the answer must be
reported together with the assumed geometry.

## Notes on what these solutions do not settle

- The "physical" interpretations attached to transformations, curvature and
  asymmetry are conventional reading rules, not deductions: a curved temperature
  log is consistent with several mechanisms, and distinguishing them needs the
  data, not the graph alone.
- The binomial and logarithmic expansions used in ★★★9 and ★★★10 are quoted as
  standard results and verified numerically here; neither is derived from first
  principles in this module.
- The demo and solutions use the synthetic values stated in each problem. Nothing
  here is a measurement of a real Earth property.
