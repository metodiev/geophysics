# Solutions — 05-04-07 Electrical Properties, Archie's Law and Clay Effects

> Numbers marked *verified* were computed.

---

## ★1

$S_w^n = aR_w/(\phi^mR_t)$ and $R_t = aR_w/(\phi^mS_w^n)$. Right side:
$(\Omega\cdot\mathrm{m})/(\text{dimensionless})$, i.e. Ω·m, matching $R_t$. Left
side of the first form is dimensionless, matching
$aR_w/(\phi^mR_t)$. ✓

---

## ★2

Resistance along a tortuous path of length $L_e = LL_r$ and effective area
$A_e = L^2\phi/L_r$: $R = R_wL_e/A_e = R_w L_r^2/(L\phi)$; bulk resistivity
$R_t = R(L^2/L) = R_wL_r^2/\phi$. Comparing with $R_t = aR_w/\phi^m$ shows
$m=1$ for straight tubes and $a$ absorbing $L_r^2$; $m>1$ encodes the empirical
observation that tortuosity increases as porosity falls.

---

## ★3

(1) Conduction only through pore water — violated by sulphides, graphite.
(2) No surface conduction — violated by clays and shales. (3) Uniform,
non-patchy saturation — violated by patchy saturation. (4) Connected
intergranular porosity — violated by vuggy or fractured rocks. (5) $a$, $m$, $n$
known — almost always the weakest link. (6) Isotropy — violated by anisotropic
shales.

---

## ★★4 *(verified)*

$R_t = aR_w/(\phi^mS_w^n) = (1)(0.5)/[(0.20)^2(0.5)^2]
= 0.5/[0.04\cdot0.25] = 0.5/0.01 = 50$ Ω·m.

---

## ★★5 *(verified)*

$S_w^n = aR_w/(\phi^mR_t) = 0.5/[0.04\cdot12] = 0.5/0.48 = 1.0417$, so
$S_w = \sqrt{1.0417} = 1.0206$ — **not physically admissible** (saturation
cannot exceed 1). With $R_t = 30$: $S_w^n = 0.5/[0.04\cdot30] = 0.4167$,
$S_w = 0.6455$ — admissible. So $R_t = 12$ Ω·m is too conductive to be explained
by the stated $R_w$, $\phi$ and exponents; something is missing from the model
(clay conduction being the usual candidate).

---

## ★★6 *(verified)*

With $\phi = 0.10$, $m = 2$: $\phi^m = 0.01$. With $S_w = 0.4$, $n = 2$:
$S_w^n = 0.16$.

Archie term: $\phi^mS_w^n/(aR_w) = 0.01\cdot0.16/0.5 = 0.0032$ S/m, so the
Archie-only $R_t = 1/0.0032 = 312.5$ Ω·m.
Clay term: $S_w\cdot0.02 = 0.4\cdot0.02 = 0.008$ S/m.
Total: $0.0032+0.008 = 0.0112$ S/m, so $R_t = 89.3$ Ω·m — a **factor of 3.50
lower** than the Archie-only value.

Cross-check against the demonstration: inverting the Archie model on
$R_t = 89.3$ Ω·m gives
$S_w = \sqrt{aR_w/(\phi^mR_t)} = \sqrt{0.5/(0.01\cdot89.3)} = 0.7483$, which is
exactly the value the demonstration prints for $\phi = 0.10$. The two
calculations agree, which is the point of the cross-check.

The clay path makes the formation look more conductive, and Archie reads extra
conductivity as extra water. At this low porosity the clay term is 2.5 times the
pore-water term, so the bias is severe.

---

## ★★7

Because the clay adds a conduction path that Archie cannot attribute to anything
except pore water. The inversion therefore requires *more* water to explain the
observed conductivity, so the recovered $S_w$ is always biased upward — never
downward.

---

## ★★★8

Expected: for the stated clay term, Archie returns $S_w>1$ at low porosity
(roughly $\phi\lesssim0.07$ for this contrast) and is accurate to 5% only at
high porosity ($\phi\gtrsim0.30$) or when the clay term is small relative to the
pore-water term. A two-term model recovers $S_w$ accurately across the grid
*provided* the clay conductivity is known — which is the practical difficulty,
since it depends on clay type, amount and the cation exchange capacity.

Sensitivity: doubling the assumed clay conductivity roughly doubles the bias
correction at low porosity, so the conclusion "Archie fails here" is robust
while "the correct $S_w$ is X" is strongly model-dependent. Report the failure
region as a finding; report the corrected saturation with its uncertainty.

---

## ★★★9

From $S_w = [aR_w/(\phi^mR_t)]^{1/n}$,
$\mathrm{d}\ln S_w = \frac1n[\mathrm{d}\ln a + \mathrm{d}\ln R_w - m\,\mathrm{d}\ln\phi
- \mathrm{d}\ln R_t] - \frac{\ln(\cdot)}{n^2}\mathrm{d}n - \frac{\ln\phi}{n}\mathrm{d}m$.

At $\phi = 0.15$, with the stated uncertainties: $m$ contributes
$|\ln\phi|\,\delta m/n = 1.897\cdot0.1/2 = 0.0949$ in $\ln S_w$ (9.9%
relative); $n$ contributes $|\ln(\cdot)|\,\delta n/n^2$; $R_w$ contributes
$0.10/2 = 5\%$; $R_t$ contributes $0.02/2 = 1\%$.

Combined (in quadrature) roughly 12% relative uncertainty in $S_w$ — larger than
the 0.05 change being asked about if $S_w$ is around 0.4 (0.05/0.4 = 12.5%).
So at low porosity an observed saturation change of 0.05 is **not resolvable**
without better constraints on $m$ and $n$.

At $\phi = 0.35$: $|\ln\phi| = 1.05$, so the $m$ contribution falls to 5.3%,
$R_w$ still 5%, $R_t$ 1% — combined about 7.5% relative, so a 0.05 change on
$S_w\approx0.4$ (12.5%) **is** resolvable. Conclusion: the exponent
uncertainties dominate at low porosity, and they must be measured on cores from
the interval rather than assumed.
