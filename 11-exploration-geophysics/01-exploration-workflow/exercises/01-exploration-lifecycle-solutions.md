# Solutions — 11-01-01 Exploration Lifecycle: Reconnaissance to Reserve Definition

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All parameters are **SYNTHETIC** teaching values.

Lesson: [01 Exploration Lifecycle](../01-exploration-lifecycle.md).

---

## ★1 — Funnel arithmetic

(a) $P_{\text{success}} = 0.40 \times 0.25 \times 0.50 = 0.0500$, i.e. 1 in 20.

(b) Survival factors: $S_0 = 1$, $S_1 = 0.40$, $S_2 = 0.40\times0.25 = 0.10$.

$$\mathbb{E}[\text{spend}] = 1(1.00) + 0.40(5.00) + 0.10(30.0)
= 1.00 + 2.00 + 3.00 = 6.00\ \mathrm{MUSD}.$$

(c) The unconditional sum $1.0+5.0+30.0 = 36.0$ MUSD is paid only if every stage
runs on every attempt. A staged program enters stage 2 on 40% of attempts and
stage 3 on 10%, so the later budgets are multiplied by the survival fraction.

---

## ★2 — Lognormal moments

Median $= e^{\mu} = 25\ \mathrm{Mt}$.

$$\mathbb{E}[T] = 25\,e^{0.90^{2}/2} = 25\,e^{0.405} = 25 \times 1.49930
= 37.5\ \mathrm{Mt}.$$

$$z = \frac{\ln 150 - \ln 25}{0.90} = \frac{5.01064 - 3.21888}{0.90}
= 1.99084, \qquad \mathbb{P}(T>150) = \Phi(-1.99084) = 0.02325.$$

**Why the mean exceeds the median:** the lognormal is multiplicative, so its
distribution is right-skewed; the mean is pulled up by the upper tail while the
median sits at $e^{\mu}$ and ignores the tail's size.

---

## ★3 — Margin per tonne

Revenue $= rPg = 0.90 \times 8500 \times 0.0035 = 26.775\ \mathrm{USD/t}$.

Margin $= 26.775 - 16.0 = +10.78\ \mathrm{USD}$ per tonne of ore.

**Unit:** $r$ dimensionless, $P$ in $\mathrm{USD/t}$ of metal times a
dimensionless grade gives $\mathrm{USD/t}$ of ore, so subtracting
$\mathrm{USD/t}$ of ore is consistent.

---

## ★4 — Tonnage and head grade above a cut-off

Model: $\ln G \sim \mathcal{N}(\mu_g,\sigma_g^{2})$ with $e^{\mu_g} = 0.0028$
(mass fraction, so $\mu_g = -5.878136$) and $\sigma_g = 0.55$. Then
$e^{\mu_g+\sigma_g^{2}/2} = 0.0028\,e^{0.15125} = 0.00325720$, i.e. a mean grade of
$0.325720\%$ Cu.

Use $z = (\ln c - \mu_g)/\sigma_g$, $\mathbb{P}(G>c) = \Phi(-z)$ and
$\mathbb{E}[G|G>c] = e^{\mu_g+\sigma_g^{2}/2}\,\Phi(\sigma_g-z)/\Phi(-z)$.

**Cut-off $0.10\%$** ($c = 0.0010$):
$\ln c = -6.907755$, so $z = (-6.907755+5.878136)/0.55 = -1.872035$ and
$\Phi(-z) = \Phi(1.872035) = 0.969399$.
$T = 80 \times 0.969399 = 77.55\ \mathrm{Mt}$.
$\Phi(\sigma_g - z) = \Phi(2.422035) = 0.992283$.
$\bar g = 0.00325720 \times 0.992283/0.969399 = 0.00333410 = 0.333410\%$.
$Q = 77.55\times10^{6}\times0.00333410 = 258.57\ \mathrm{kt}$ Cu.

**Cut-off $0.30\%$** ($c = 0.0030$):
$z = (-5.809143+5.878136)/0.55 = +0.125442$; $\Phi(-0.125442) = 0.450087$.
$T = 80 \times 0.450087 = 36.01\ \mathrm{Mt}$.
$\Phi(\sigma_g - z) = \Phi(0.424558) = 0.664421$.
$\bar g = 0.00325720 \times 0.664421/0.450087 = 0.00480830 = 0.480830\%$.
$Q = 36.01\times10^{6}\times0.00480830 = 173.13\ \mathrm{kt}$ Cu.

**Contained metal fell** from $258.57$ to $173.13\ \mathrm{kt}$ ($-33.0\%$) while
the head grade rose from $0.3334\%$ to $0.4808\%$. Because
$Q(c) = T_{\text{tot}}\int_c^\infty g f(g)\,\mathrm{d}g$, raising $c$ removes
grades from the integral that were strictly positive; the integrand is
non-negative, so the integral can only fall. Grade does not conserve metal.

---

## ★5 — Break-even cut-off and its independence from $f(g)$

$$c_{\text{be}} = \frac{C}{rP} = \frac{14}{0.87 \times 7500} = \frac{14}{6525}
= 0.002146 = 0.2146\%\ \mathrm{Cu}.$$

Profit is $\Pi(c) = T_{\text{tot}}\int_c^\infty (rPg - C) f(g)\,\mathrm{d}g$.
Leibniz's rule gives
$\mathrm{d}\Pi/\mathrm{d}c = -T_{\text{tot}}(rPc - C)f(c)$. The stationarity
condition $rPc - C = 0$ therefore involves only $r$, $P$ and $C$: the grade
density $f(c)$ multiplies the whole expression and cancels. $f$ sets *how much*
metal and tonnage exist at that cut-off, not *where* the cut-off should be. (If
$f(c) = 0$ at the stationary point the second-order behaviour has to be examined
separately — a degenerate case that does not arise for a lognormal with
$\sigma_g>0$.)

---

## ★6 — Portfolio arithmetic

$$Np = 20 \times 0.04 = 0.80\ \text{expected discoveries},$$
$$\mathbb{P}(\ge 1) = 1 - 0.96^{20} = 1 - 0.44200 = 0.5580,\qquad
\mathbb{P}(\text{none}) = 0.4420.$$

Smallest $p$ for $\mathbb{P}(\ge1)\ge 0.50$: solve $1-(1-p)^{20} = 0.50$, so
$(1-p)^{20} = 0.50$, $1-p = 0.50^{1/20} = e^{-0.693147/20} = e^{-0.034657}
= 0.96594$, giving $p = 0.03406$.

So a fall in per-target success probability from $0.0400$ to $0.0341$ — a **15%
relative change** — takes the portfolio from "more likely than not to find
something" to "more likely to find nothing". The portfolio is *very* sensitive to
$p$ near this threshold, because $\mathbb{P}(\ge1)$ is linear in $p$ only for
small $Np$.

---

## ★7 — Price sensitivity of the reserve

$$\frac{53.62 - 77.83}{77.83} = -0.3111 = -31.1\%.$$

Price change: $(6000-9000)/9000 = -33.3\%$. Implied elasticity

$$\varepsilon = \frac{-31.1\%}{-33.3\%} = 0.93 .$$

A near-unit elasticity over this interval: **a 1% fall in metal price removes
about 1% of the reserve tonnage** for these SYNTHETIC parameters. The elasticity
is not a universal constant — it depends on $\sigma_g$, the cut-off and the cost
structure — but its order of magnitude is the reason a reserve statement must be
read with its price deck attached.

---

## ★8 — Program design

**Objective:** maximise $\mathbb{E}[\text{discoveries}]$ per MUSD, subject to the
budget.

Let $n$ targets be attempted. Cost per target $= G + p_g D$ (drilling is entered
only with probability $p_g$). Expected discoveries per target $= p_g p_d$. Then

$$\text{efficiency} = \frac{n\,p_g p_d}{n\,(G + p_g D)} = \frac{p_g p_d}{G + p_g D},$$

which is **independent of $n$**: with a linear objective and a linear budget, the
optimum is to spend the whole budget on the single most efficient option. The
constraint is $n(G + p_g D) \le 20$ MUSD, so
$n^{*} = \lfloor 20/(G+p_g D)\rfloor$ and the decision reduces to comparing
candidate $(G,p_g)$ pairs by the ratio above — e.g. cheap regional geophysics
raising $p_g$ from $0.10$ to $0.20$ at $G = 0.5$ MUSD beats expensive
target-scale geophysics raising it from $0.30$ to $0.40$ at $G = 4$ MUSD because
it leaves more money for drilling.

**Assumption that must be made:** targets are independent and identically
distributed, and $p_d$ does not depend on how many are drilled.

**Assumption whose failure inverts the ranking:** that $p_g$ and $p_d$ are
*independent conditional on the method*. If the cheap method's targets are
drillable but geologically poor (anti-correlated $p_g$ and $p_d$), the ratio
$p_gp_d$ falls while $p_g$ alone rises, and the ranking reverses. A design should
therefore report the product $p_gp_d$, not $p_g$.

---

## ★9 — Same mean grade, different reserve tonnage

Two SKEPTICAL-but-defensible constructions:

1. **Different dispersion.** Deposit A has $\sigma_g = 0.30$, B has
   $\sigma_g = 0.80$, both with median grade chosen so that the means coincide at
   $0.35\%$ Cu. With a common cut-off $c = 0.20\%$ Cu the ore fractions are
   $\mathbb{P}(G>c) = 0.957$ for A and $0.618$ for B — a **34-percentage-point**
   difference in ore fraction at identical mean grade, computed from the
   lognormal survival functions. B is more "nuggety": a third of its rock sits
   below the cut-off, so its reserve tonnage is far smaller even though the mean
   grade is the same. A also has the higher head grade above the cut-off.
2. **Different cut-off, same price.** If the two deposits differ in
   mining-plus-processing cost $C$ (hardness, grind size, sulphide content), then
   $c_{\text{be}}$ differs even at the same price, and the reserve tonnages
   diverge for that reason alone.

**Legitimate conclusion from two reserve tonnages at the same mean grade:** that
the two *plans* differ. It is not legitimate to conclude that one deposit
"contains more metal" or is "better" without the cut-off, the cost structure, the
price deck and the confidence class. A reader who is told only "77.8 Mt at 0.42%
Cu" cannot reconstruct any of those.

---

## ★10 — Separating classification from economics (specification)

**Quantity to report:** the *fraction of reserve tonnage variance* attributable to
the confidence classification. Practically, run a two-factor sweep and report the
elasticity pair

$$E_{\text{class}} = \frac{\Delta T_{\text{res}}/T_{\text{res}}}{\Delta s/s},
\qquad
E_{\text{price}} = \frac{\Delta T_{\text{res}}/T_{\text{res}}}{\Delta P/P},$$

and compare their magnitudes on the same relative-perturbation basis.

**Synthetic deposit with known truth:** generate a 3-D grade field on a fine grid
(the truth) with a stated variogram, then subsample it on grids of 400, 200, 100
and 50 m, and for each grid estimate tonnage and grade by ordinary kriging. Take
the *estimated* tonnage at a fixed cut-off as the resource, apply the economic
filter to get the reserve, and repeat for three price decks (e.g. 0.8, 1.0, 1.2
times a base price).

**Decision rule:** report $|E_{\text{class}}|$ and $|E_{\text{price}}|$ with their
sampling distributions from ~100 realisations (block bootstrap over the truth
fields, not over the samples, to preserve spatial structure). Conclude that the
classification effect dominates if the 10th–90th percentile band of
$E_{\text{class}}$ for a 400 m$\to$100 m refinement lies entirely outside the
band produced by a $\pm20\%$ price move; otherwise state that the two effects are
of comparable size and that the reserve tonnage cannot be attributed to either
alone. The failure mode to guard against is estimating the truth from the same
data used to fit the variogram, which biases the classification effect downward.
