# Solutions — 22-01-03 Code Review and Collaborative Development

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [03 Code Review and Collaborative Development](../03-code-review.md).

---

## ★1 — A 50-line change

$$t = \frac{50}{200} = 0.25\ \text{h}, \qquad
p_{\text{det}} = 1 - e^{-0.9 \times 0.25} = 1 - e^{-0.225} = 1 - 0.7985 = 0.201.$$

Escaped defects per kLOC:

$$\rho (1 - p_{\text{det}}) = 8 \times 0.799 = 6.39\ \text{per kLOC}.$$

Both match the demonstration's 50-line row ($p = 0.201$, escapes $6.39$).

## ★2 — One reviewer versus two

Two independent reviewers:

$$p_2 = 1 - (1-p)^2 = 1 - (0.407)^2 = 1 - 0.1656 = 0.834.$$

Escapes per kLOC:

- one reviewer: $8 \times 0.407 = 3.25$;
- two reviewers: $8 \times 0.166 = 1.32$.

Both equal the demonstration's table (3.25 and 1.32), a reduction of
$1 - 1.32/3.25 = 59.3\ \%$, also as printed.

## ★3 — Total found versus density escaped

*Total* defects found is $p_{\text{det}}(L) \times \rho L/1000$: detection
saturates but the number of defects in the change grows linearly, so the total
found keeps rising with $L$. The escaped **density** is $\rho(1-p_{\text{det}})$,
a factor that falls as detection improves, while the *total* escaped count
$\rho L (1-p)/1000$ rises at small $L$ before falling at large $L$ — which is
exactly why large reviews leak fewer defects per line and small reviews leak
almost all of them.

## ★★4 — Size for an escape rate of 2 per kLOC

$$8\,e^{-0.9L/200} = 2
\;\Longrightarrow\;
e^{-0.9L/200} = 0.25
\;\Longrightarrow\;
\frac{0.9L}{200} = \ln 4 = 1.3863.$$

$$L = \frac{200 \times 1.3863}{0.9} = 308.1\ \text{lines}.$$

Check against the table: at 200 lines escapes are 3.25, at 400 lines 1.32. Linear
interpolation in $L$ between those points gives
$200 + 200 \times (3.25-2.0)/(3.25-1.32) = 200 + 129.5 = 329.5$, within 7 % of
the analytic 308. The interpolation is loose because the escape curve is convex,
so the analytic value is the one to report: $L \approx 308$ lines.

## ★★5 — Under-reviewed change

$$t = \frac{40}{60} = 0.667\ \text{h}, \qquad
p_{\text{det}} = 1 - e^{-0.9 \times 0.667} = 1 - e^{-0.60} = 1 - 0.5488 = 0.451.$$

Escape rate $= 8 \times 0.549 = 4.39$ per kLOC, which is
$4.39/0.22 = 20$ times the fully inspected value of 0.22 per kLOC at that size.
The reduction of review effort by a factor of six costs a factor of twenty in
escaped density — the return on inspection time is strongly non-linear, which is
the practical content of the saturating detection law.

## ★★6 — Reviewing `normalise`

| # | Item | Consequence |
|---|---|---|
| 1 | `x * scale` promotes `float32` to `float64` | memory doubles on a large array; the caller's dtype assumption is silently broken |
| 2 | no check that `x` is non-empty | `y.mean()` on an empty array yields `nan` and warns, then the division returns `nan` |
| 3 | `y.std()` is the **population** ($N$) standard deviation | if the caller expects the sample ($N-1$) estimate a single-sample input divides by zero, and small-$n$ results differ by $\sqrt{N/(N-1)}$ |
| 4 | subtracting the whole-array mean | if `x` is a time series with a trend, "normalise" removes a physical mean, not a baseline; if `x` is 2-D, the mean is taken over *all* elements and mixes rows |
| 5 | no docstring stating the normalisation convention | a reader cannot tell whether the output is zero-mean/unit-variance or a min–max scaling |
| 6 | no units | the result of subtracting a mean is in the input's unit; a scaled series' unit must be stated |

**Catchable by a unit test:** the dtype promotion (assert `z.dtype`), the
division-by-zero on a one-element input (assert `nan` or raise), and which
denominator is used (compare against a hand-computed value with $N = 3$).

**Not catchable:** items 4 and 6. Whether removing the mean is *physically* right
depends on what the array represents, which no test of the function alone can
decide; that is a review question about the method, and it is the reason the
review checklist puts units and conventions first.

## ★★★7 — Estimating $p_{\text{det}}(L)$ empirically

**Treatment.** Change size $L$, in bins (e.g. $\le 50$, $51$–$150$,
$151$–$400$, $> 400$ lines).

**Unit of analysis.** One reviewed change, with the number of defects it
contained and the number found during review.

**Defect identification.** Defects must be identified independently of the
review under study, or the measurement is circular. The workable design is a
**two-stage** one: after the review, the merged code is inspected (a) by an
automated reference suite of tests and static checks, and (b) by an inspector who
is not a reviewer of that change and who works from a written checklist and the
original specification. Only defects that those methods find *and* that the
review did not are counted as escapes; a defect found by both is a detection.
Records are timestamped so a later fix is not retro-attributed to the review.

**Sample size.** To distinguish $p = 0.30$ from $p = 0.50$ at 95 % confidence with
80 % power, the standard two-proportion formula gives

$$n \approx \frac{(1.96 + 0.84)^2 \times (0.3 \times 0.7 + 0.5 \times 0.5)}
{(0.5 - 0.3)^2} = \frac{7.84 \times 0.46}{0.04} = 90.2$$

changes **per group**, i.e. at least 90 changes in the small-size bin and 90 in
the large-size bin, and every change must contain at least one defect for the
proportion to be estimable — so the design needs roughly 200 reviewed changes
containing defects, which is years for a small group and is exactly why these
numbers are usually taken from the model instead of measured.

## ★★★8 — Modelling reviewer dependence

Let reviewer A detect a defect with probability $p$ and reviewer B with
probability $p$, and let $\phi \in [0,1]$ be the **shared-miss** parameter: the
probability that B misses a defect is $1-p$ times the chance that B "follows" A's
miss. A standard construction is a mixture:

$$P(\text{both miss}) = (1-p)^2 + \phi\,\bigl[(1-p) - (1-p)^2\bigr]
= (1-p)^2 + \phi\, p(1-p).$$

At $\phi = 0$ the reviewers are independent ($(1-p)^2$, the case in §5); at
$\phi = 1$ the second reviewer adds nothing (only A's miss matters). The
detection probability is $1 - (1-p)^2 - \phi p(1-p)$, which interpolates between
the independent value and $p$.

**Measurable quantity.** From a sample of $n$ defects with a known ground truth
(each defect's detection recorded per reviewer), fit the $2 \times 2$ contingency
table of detections. Under independence the off-diagonal cells are equal
(expected count $(1-p)p\,n$ each); the observable that estimates $\phi$ is the
**imbalance of the table**: $\hat\phi$ is the excess of "A misses, B finds" over
"A finds, B misses" relative to $p(1-p)n$, i.e.

$$\hat\phi = \frac{\hat n_{AB} - \hat n_{BA}}{p(1-p)\,n},$$

with a standard error from the multinomial. Substantial asymmetry (a large
$\hat\phi$) is evidence that one reviewer is doing the work and the other is
confirming it — the qualitative failure of "two reviewers" that the independence
assumption hides.

## ★★★9 — Cost-minimising review effort

Let $e$ be review effort in person-hours per kLOC, so inspection time for $L$
lines is $t = eL/1000$ hours. Write the fractional detection in terms of the
effort per kLOC:

$$p(e) = 1 - e^{-\kappa e}, \qquad \kappa = k/1000 \ \text{per hour per kLOC},$$

taking the effort to be applied uniformly. The expected cost per kLOC is

$$C_{\text{total}}(e) = \underbrace{c_r e}_{\text{review}} +
\underbrace{\rho_{\text{def}}\, C_{\text{fix}}\, e^{-\kappa e}}_{\text{escapes}} ,$$

where $c_r$ is the cost of an hour of review, $\rho_{\text{def}}$ the defect
density and $C_{\text{fix}}$ the cost of fixing one escaped defect. Setting
$\mathrm{d}C_{\text{total}}/\mathrm{d}e = 0$:

$$c_r = \kappa\,\rho_{\text{def}}\,C_{\text{fix}}\,e^{-\kappa e}
\;\Longrightarrow\;
e^{\ast} = \frac{1}{\kappa}\ln\!\left(\frac{\kappa\,\rho_{\text{def}}\,C_{\text{fix}}}{c_r}\right).$$

With the demonstration's $\kappa = k/1000 = 0.0009$ per hour per kLOC
($k = 0.90\ \text{h}^{-1}$ for $L$ in kLOC), $\rho_{\text{def}} = 8$ per kLOC and,
say, $C_{\text{fix}} = 10 \times c_r$:

$$e^{\ast} = \frac{1}{0.0009}\ln\!\left(0.0009 \times 8 \times 10\right)
= 1111 \times \ln(0.072) \;\text{— negative}.$$

The negative value is the model telling you it is in the wrong regime: because
$\kappa e$ is small at plausible efforts, the model claims a defect detected in
review costs more than one fixed later, so it recommends no review at all. That
is an artefact of the linear-in-$e$ detection law and of treating $C_{\text{fix}}$
as independent of when the defect is found.

**Two assumptions that make the answer unreliable.** (i) **Uniform effort at
constant return**: real inspection has a steep initial return and a long tail,
so the exponential-based optimum sits in a region the model was never fitted to.
(ii) **Independent fix costs**: a defect found in review is fixed by the author
with full context; the same defect found after publication is fixed by a
different person, may invalidate a figure, and may require a correction or a
retraction, so $C_{\text{fix}}$ is not a constant but a distribution with a
heavy tail.

**What a laboratory should measure.** The detection curve $p(e)$ at two or three
effort levels, and the distribution of fix costs for defects found after a merge
— at minimum the fraction of post-merge defects that invalidated a delivered
result. Only then is the optimisation about the laboratory rather than about the
model.
