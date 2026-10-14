# Solutions — 01-01-01 Number Systems, Precision and Scientific Notation

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Where a numeric answer is given, it was computed
> and verified rather than estimated by hand. Several problems have more than one
> defensible answer; where that is true, it is stated explicitly.

---

## ★1 — Scientific notation to 3 significant figures

| | Value | Answer | Note |
|---|---|---|---|
| (a) | 0.000482 | $4.82\times10^{-4}$ | leading zeros are placeholders only |
| (b) | 91 300 | $9.13\times10^{4}$ | trailing zeros dropped in favour of explicit power |
| (c) | 0.6071 | $6.07\times10^{-1}$ | rounded from 0.6071 to 3 s.f. |
| (d) | 4 500 000 | $4.50\times10^{6}$ | the trailing zero **is** significant, so it stays |

**Key point.** In (d), writing $4.50\times10^{6}$ states that the value is
4 500 000 ± 5 000. Writing $4.5\times10^{6}$ would state ±50 000. The extra digit
is information, not decoration.

---

## ★2 — Gravity unit conversions

Conversion chain: multiply by the exact ratio
$\dfrac{10^{-5}\ \mathrm{m\,s^{-2}}}{1\ \mathrm{mGal}}$,
then multiply by $\dfrac{10^{6}\ \mu\mathrm{m}}{1\ \mathrm{m}}$.

| | Given | In SI (m/s²) | In µm/s² |
|---|---|---|---|
| (a) | 15.2 mGal | $1.52\times10^{-4}$ | 152 |
| (b) | −3.7 mGal | $-3.70\times10^{-5}$ | −37.0 |
| (c) | 1.05 Gal | $1.05\times10^{-2}$ | $1.05\times10^{4}$ |

**Reasoning check (the step students skip).** mGal is a *small* unit, so the
same physical acceleration is a *larger* number when expressed in mGal than in
m/s². Check (a): 15.2 (mGal) → 0.000152 (m/s²). The number got smaller, and the
unit got bigger. Consistent. Check (a) → (µm/s²): the unit got smaller
again, so the number got bigger again: 152. Consistent.

**Significant figures.** All conversions use exact factors, so 15.2 keeps 3
significant figures throughout: $1.52\times10^{-4}$.

---

## ★3 — Counting significant figures

| | Value | s.f. | Ambiguous? |
|---|---|---|---|
| (a) | `0.00340` | **3** | no — non-zero digits plus the trailing zero |
| (b) | `1.20×10⁴` | **3** | no — scientific notation is unambiguous |
| (c) | `700` | **1, 2, or 3** | **yes** — trailing zeros with no decimal point |
| (d) | `7.00×10²` | **3** | no |

**Why (c) matters.** `700` could mean $7\times10^{2}$ (1 s.f., meaning anywhere
from 650 to 750), or $7.00\times10^{2}$ (3 s.f., meaning 699.5 to 700.5). A
reader cannot tell. This is the practical reason scientific notation is not
optional in scientific writing.

**Note on (a).** `0.00340` has 3 s.f., not 5. The three leading zeros
(`0.00`) exist only to position the decimal point and are never significant. The
trailing zero in `340` **is** significant.

---

## ★4 — Arithmetic with correct significant figures

### (a) $4.56 \times 2.1 = 9.576$

**Rule applied:** multiplication → fewest significant figures. $4.56$ has 3 s.f.,
$2.1$ has 2 s.f. → **2 s.f.**

$$\boxed{9.6}$$

Note that 9.576 rounds to 9.6, not 9.58. The calculator's extra digits are
intermediate values, not results.

### (b) $12.5 \div 0.25 = 50$

**Rule applied:** division → fewest significant figures. $0.25$ has 2 s.f.,
$12.5$ has 3 s.f. → **2 s.f.**

$$\boxed{5.0\times10^{1}}$$

**The trap.** Writing `50` is ambiguous — a reader cannot tell whether you mean
2 s.f. (50 ± 0.5) or 1 s.f. (50 ± 5). Write $5.0\times10^{1}$. This is exactly
the ambiguity identified in ★3(c).

### (c) $101.3 + 0.44 = 101.74$

**Rule applied:** addition → least precise *decimal place*. $101.3$ is known to
the tenths place; $0.44$ to the hundredths place. The result is limited to the
tenths place.

$$\boxed{101.7}$$

**Observation worth dwelling on.** We started with 4 and 2 significant figures
and ended with 4 — yet information was still lost. The hundredths digit of the
answer (0.04) is not meaningful because we do not know the tenths digit of
$101.3$ precisely. Addition and subtraction limit by *position*, not by *count*.

---

## ★★5 — Magnetic anomaly

**(a)** $1250\ \mathrm{nT} = 1250 \times 10^{-9}\ \mathrm{T}
= 1.250\times10^{-6}\ \mathrm{T}$, so the anomaly is
$\boxed{-1.250\times10^{-6}\ \mathrm{T}}$.

**(b)** Since $1\ \gamma = 1\ \mathrm{nT}$ by definition, the magnitude is
$\boxed{1250\ \gamma}$. The gamma was introduced precisely because the tesla is
an inconveniently large unit for geomagnetic work; it is now deprecated in
favour of nT, but still appears in older literature.

**(c)** With 1 nT resolution the value is known to the ones place:
$-1250 \pm 1$ nT. Every digit is therefore meaningful, including the trailing
zero. **4 significant figures** may be quoted.

**Important subtlety.** This is a case where the trailing zero *is* significant,
because we know the value to the nT. Compare with ★3(c), where `700` was
ambiguous. Here the resolution is stated, which removes the ambiguity. **Always
state the resolution when you quote a precise number.** In practice you would
write $1.250\times10^{3}$ nT or $-1250$ nT (resolution 1 nT).

---

## ★★6 — Seismic velocity

**(a)** Using verified arithmetic:

$$v = \frac{412\ \mathrm{km}}{68.4\ \mathrm{s}} = 6.023391\ldots\ \mathrm{km/s}
\qquad\text{and}\qquad 6.023391\ldots\times10^{3}\ \mathrm{m/s}.$$

**(b)** The distance 412 km has 3 s.f.; the time 68.4 s has 3 s.f. Division →
fewest s.f. → **3 significant figures**:

$$\boxed{v = 6.02\ \mathrm{km/s} = 6.02\times10^{3}\ \mathrm{m/s}}$$

**(c) Why `6.02339 km/s` is physically wrong, not merely untidy.**

The time is quoted to 0.1 s, so the *relative* uncertainty in the time is at
least

$$\frac{0.05\ \mathrm{s}}{68.4\ \mathrm{s}} \approx 7.3\times10^{-4}
\quad (\text{about } 0.07\%).$$

The distance, quoted to 1 km, contributes

$$\frac{0.5\ \mathrm{km}}{412\ \mathrm{km}} \approx 1.2\times10^{-3}
\quad (\text{about } 0.12\%).$$

Combining in quadrature:

$$\frac{\sigma_v}{v} \approx \sqrt{(7.3\times10^{-4})^{2} + (1.2\times10^{-3})^{2}}
\approx 1.4\times10^{-3}\quad (\text{about } 0.14\%).$$

Applied to $v = 6.0234$ km/s, that gives

$$v = 6.023 \pm 0.009\ \mathrm{km/s}.$$

Reporting `6.02339` km/s claims a precision of ±0.00001 km/s, which is **about
140 times finer than the data support**. The extra digits would imply that this
measurement could distinguish a 6.02339 km/s medium from a 6.02340 km/s
medium — one centimetre per second. No seismic survey resolves that, and
real geological variation in a rock unit is orders of magnitude larger.

**The general principle.** Digits beyond the information content are not
"extra precision available if needed". They are fabricated precision, and a
competent reader will discount your entire result because of them.

---

## ★★7 — Depth of a buried mass

**(a) Order of magnitude.**

$$g_z = \frac{GM}{d^{2}} \;\Longrightarrow\; d = \sqrt{\frac{GM}{g_z}}.$$

With $GM \sim (7\times10^{-11})(10^{10}) \sim 0.7\ \mathrm{m^{3}\,s^{-2}}$ and
$g_z = 5\times10^{-7}\ \mathrm{m\,s^{-2}}$:

$$d^{2} \sim \frac{0.7}{5\times10^{-7}} \sim 1.4\times10^{6}\ \mathrm{m^{2}}
\;\Longrightarrow\; d \sim 10^{3}\ \mathrm{m} = 1\ \mathrm{km}.$$

**(b) Exact computation.** Converting first:
$0.05\ \mathrm{mGal} = 0.05\times10^{-5} = 5.0\times10^{-7}\ \mathrm{m\,s^{-2}}$.

$$d = \sqrt{\frac{(6.674\times10^{-11})(10^{10})}{5.0\times10^{-7}}}
= \sqrt{\frac{6.674\times10^{-1}}{5.0\times10^{-7}}}
= \sqrt{1.3348\times10^{6}}
\approx 1155\ \mathrm{m}.$$

$$\boxed{d \approx 1.16\ \mathrm{km}}$$

Agreement with the order-of-magnitude estimate (1 km) confirms no arithmetic
blunder. **This is the value of the two-step method: the estimate validates the
precise answer.**

**(c) Is the point-mass approximation justified?**

Volume $V = M/\rho = 10^{10}/3000 = 3.33\times10^{6}\ \mathrm{m^{3}}$.
For a sphere, $R = \left(\frac{3V}{4\pi}\right)^{1/3}$:

$$R = \left(\frac{3\times3.33\times10^{6}}{4\pi}\right)^{1/3}
= \left(7.96\times10^{5}\right)^{1/3} \approx 92.7\ \mathrm{m}.$$

The ratio of observation distance to body radius is

$$\frac{d}{R} = \frac{1155}{92.7} \approx 12.5.$$

The leading correction to the point-mass field is of relative order
$(R/d)^{2} \approx (1/12.5)^{2} \approx 6.4\times10^{-3}$, i.e. **below 1%**.

**Verdict.** The approximation is justified. Quoting $d$ to two significant
figures (1.2 km) is appropriate, since the shape error alone is ~0.6% and the
instrumental resolution contributes more than that.

**The general rule.** The point-mass (monopole) approximation is adequate when
$d \gtrsim 5R$; the error falls off as $(R/d)^2$. Below that, higher multipoles
matter and you need the full forward model developed in
[07-gravity-geodesy](../../../07-gravity-geodesy/README.md).

**(d) Sphere or cube?**

At $d/R \approx 12.5$ the answer is **essentially independent of shape.** The
difference between a sphere and a cube of equal mass appears only in the
quadrupole and higher terms, which are suppressed by $(R/d)^{2}$ and
$(R/d)^{4}$.

This is a **profound and general result in potential-field methods**:

> At sufficient depth, shape is invisible and only total mass is recoverable
> from the anomaly amplitude.

It is also why potential-field inversion is so non-unique. If you measure only
$g_z$ (and not its gradients), a buried sphere and a buried cube of equal mass
at the same depth produce indistinguishable anomalies. Recovering shape requires
either the anomaly *shape* (which constrains depth) or additional data —
gravity gradients, or a second method. This theme is central to
[18-inverse-problems](../../../18-inverse-problems/README.md).

---

## ★★8 — Survey area and honest uncertainty

**(a)** Exact product of the given numbers:
$1.25 \times 0.80 = 1.0000\ \mathrm{km^{2}}$. (Both are exact decimals as
written, so this is the *exact* arithmetic result.)

**(b)** Significant-figures rule: each dimension has 2 s.f., so the area has
**2 s.f.**:

$$\boxed{A = 1.0\ \mathrm{km^{2}} = 1.0\times10^{6}\ \mathrm{m^{2}}}$$

But note the granularity problem: 2 s.f. forces the answer to be either 1.0 or
1.1 — a 5% step. That is coarse relative to the real uncertainty.

**(c) Proper propagation.** Each dimension carries ±0.005 km (half the last
quoted digit):

$$\frac{\sigma_a}{a} = \frac{0.005}{1.25} = 4.0\times10^{-3}\ (0.40\%), \qquad
\frac{\sigma_b}{b} = \frac{0.005}{0.80} = 6.25\times10^{-3}\ (0.63\%).$$

For a product, relative uncertainties combine in quadrature:

$$\frac{\sigma_A}{A} = \sqrt{(4.0\times10^{-3})^{2} + (6.25\times10^{-3})^{2}}
= \sqrt{1.6\times10^{-5} + 3.9\times10^{-5}}
\approx 7.4\times10^{-3}\ (0.74\%).$$

$$\sigma_A = 0.0074\ \mathrm{km^{2}} \approx 7.4\times10^{3}\ \mathrm{m^{2}}.$$

$$\boxed{A = 1.000 \pm 0.007\ \mathrm{km^{2}} = (1.000 \pm 0.007)\times10^{6}\ \mathrm{m^{2}}}$$

**(d) Comparison — an important lesson.**

| Method | Result | Information lost |
|---|---|---|
| s.f. rule | $1.0\ \mathrm{km^{2}}$ | Rounds a ±0.7% uncertainty up to a ±5% granularity — **hides** the real precision |
| Propagation | $1.000 \pm 0.007\ \mathrm{km^{2}}$ | States the uncertainty explicitly |

**The propagation result is more informative**, because it distinguishes the
*uncertainty* (±0.7%) from the *rounding granularity* (5%).

**The general lesson.** Significant-figure rules are a **crude shortcut**, useful
for quick mental checks but not a substitute for propagation. They can both
over-state and under-state uncertainty. The rigorous approach — combining
relative uncertainties in quadrature — is developed in
[01-13 Probability and Statistics Foundations](../../13-probability-and-statistics-foundations/README.md),
and it is what you should use in any reported result.

---

## ★★★9 — Growth of naive summation error

This is a research-style exercise, so the *method* and the *limitations* matter
as much as the number.

### Observed reference value

The supplied demonstration, at $n = 10^{5}$, gives:

```text
naive sum       = 10000.000000018848
exact           = 10000
naive error     = 1.885e-08
compensated err = 0.000e+00
```

So at $n = 10^{5}$ the naive error is $\approx 1.9\times10^{-8}$, while
Kahan-compensated summation is **exact to the precision reported**.

### Expected behaviour and mechanism

At step $k$ of naive summation, the running partial sum is $\approx 0.1k$. The
addition of the next 0.1 incurs a rounding error of magnitude at most
$\varepsilon \cdot 0.1k$, where $\varepsilon \approx 2.2\times10^{-16}$.

- **If all these errors had the same sign**, the accumulated error would be
  $\sum_{k=1}^{n} \varepsilon \cdot 0.1k \sim \varepsilon \cdot 0.05\,n^{2}$ —
  growth as $n^{2}$.
- At $n = 10^{5}$ that bound gives
  $2.2\times10^{-16} \times 0.05 \times 10^{10} \approx 1.1\times10^{-7}$,
  **the same order of magnitude as the observed $1.9\times10^{-8}$.** So the
  worst-case model is consistent with the data at this $n$.

### What you should find when you extend $n$

Whether the empirical exponent is closer to 2 or closer to 1 is the interesting
question, and the answer depends on how the individual rounding errors cancel:

- If rounding errors were **systematically biased** (all the same sign), you
  would see the $n^{2}$ law across the full range.
- If they are effectively **random and centred on zero**, the partial sums
  undergo a random walk, and the accumulated error grows closer to
  $n^{1.5}$ — or, if the errors anti-correlate, $n$ or slower.

**Report what you measure, not what theory suggests.** A defensible write-up
states: the fitted exponent; the fit quality; whether $n^{2}$ lies within the
confidence interval of the fit; and the range of $n$ over which the fit holds.

### Limits of the conclusion

A careful report must state:

1. **Dependence on the value summed.** The result is specific to summing 0.1.
   Values that are exactly representable in binary (e.g. 0.5, 0.25) sum
   exactly and show **zero** error at every $n$. Choosing 0.1 is what makes the
   experiment work.
2. **Dependence on summation order.** Summing the same values in a different
   order gives a different error, because the partial sums differ at each step.
   This is a genuine property of floating-point addition: it is **not
   associative**.
3. **Dependence on platform and compiler.** IEEE 754 binary64 is standardised,
   so results should agree across platforms *if* extended precision
   (x87 80-bit registers, fused multiply-add contraction) is not used
   silently. Python's `float` maps to C `double`, and CPython does not retain
   extra precision in registers, so results are stable — but that is a property
   of the implementation, not a law.
4. **The exponent is not a universal constant.** It characterises this
   experiment, not "floating point in general".

### The practical takeaway

Kahan compensated summation returned the **exact** result here at negligible
cost. For any long accumulation — integrating a time series, summing a
wavefield, computing a mean over millions of samples — this is the difference
between a trustworthy number and a plausible-looking one. The full theory is in
[01-05 Absolute vs Relative Error, Conditioning and Stability](../05-error-and-conditioning.md).

---

## ★★★10 — Reporting a mass with honest uncertainty

**(a) Contribution from $G$ alone.**

$$M = \frac{g_z d^{2}}{G}.$$

Since $G$ appears as $1/G$, its relative uncertainty passes through unchanged:

$$\frac{\sigma_M}{M}\bigg|_{G} = \frac{\sigma_G}{G} = 2.2\times10^{-5}
\quad (0.0022\%).$$

So $G$ alone forces a **0.0022%** uncertainty — small, but not zero.

**(b) Contribution from $g_z$ and $d$, each at 1%.**

$g_z$ enters linearly: relative uncertainty 1%.
$d$ enters **squared**, so its relative uncertainty is **doubled**: $2 \times 1\% = 2\%$.

Combining all independent contributions in quadrature:

$$\frac{\sigma_M}{M}
= \sqrt{(2.2\times10^{-5})^{2} + (0.01)^{2} + (0.02)^{2}}
= \sqrt{(0.00022)^{2} + 10^{-4} + 4\times10^{-4}}
\approx \sqrt{5.0005\times10^{-4}}
\approx 2.24\times10^{-2}.$$

$$\boxed{\frac{\sigma_M}{M} \approx 2.2\%}$$

Note that $G$'s contribution (0.0022%) is utterly negligible here — **almost
600 times smaller** than the combined measurement contributions.

**(c) How many significant figures are justified?**

A 2.2% relative uncertainty means we know the mass only to about 1 part in 45.
Therefore only **2 significant figures** are defensible:

$$\boxed{M = 3.4\times10^{9}\ \mathrm{kg}\ \text{(2 s.f.)}}$$

If the uncertainty were instead around 0.1%, then 3 s.f. would be appropriate.
**The rule is: report digits to the point where the uncertainty becomes
significant — usually one or two digits of the uncertainty.**

**(d) Feedback to the student.**

> "Your computation is correct, but reporting eight significant figures implies
> you know the mass to within 0.00001%. Your stated input uncertainties —
> 1% on $g_z$ and $d$, plus the uncertainty in $G$ — limit you to about 2.2%,
> which is roughly two significant figures. I'd suggest reporting
> $M = 3.4 \times 10^{9}$ kg, with an explicit uncertainty such as
> $\pm 0.07 \times 10^{9}$ kg. Two further notes: because $d$ is squared, its
> 1% uncertainty becomes 2% in $M$ — that dominates your error budget. And $G$'s
> contribution (0.0022%) is negligible by comparison, so it need not be quoted
> as a limiting factor. Reporting the error budget explicitly will make your
> result far more convincing."

**The deeper point.** This problem teaches a habit that separates competent from
careless quantitative work: **compute the error budget before deciding how many
digits to report.** Note also the asymmetry — the term you might expect to
dominate ($G$, a fundamental constant) is irrelevant here, while a squared
geometric quantity ($d$) dominates. Error budgets are frequently
counter-intuitive, which is precisely why they must be computed rather than
assumed.

A systematic treatment of error propagation, including correlated
uncertainties, is in
[01-13 Probability and Statistics Foundations](../../13-probability-and-statistics-foundations/README.md),
and its role in inverse problems in
[18-inverse-problems](../../../18-inverse-problems/README.md).

---

## Self-assessment: have you actually learned this?

Mark yourself honestly. If you cannot do these from memory, revisit the lesson
before proceeding to [02 Orders of Magnitude](../02-orders-of-magnitude.md).

- [ ] I can convert between mGal, Gal, and m/s² without looking up the factors.
- [ ] I can state the significant-figures rules for ×, ÷, +, − and explain *why*
      addition behaves differently.
- [ ] I can explain why `2500` is ambiguous and fix it.
- [ ] I can propagate two independent 1% uncertainties through a product.
- [ ] I can explain why a squared quantity doubles its relative uncertainty.
- [ ] I can describe what catastrophic cancellation is and give a geophysical
      example.
- [ ] I can name the machine epsilon for binary64 and say what it means.
