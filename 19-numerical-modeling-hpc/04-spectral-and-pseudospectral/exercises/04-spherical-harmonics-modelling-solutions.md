# Solutions — 19-04-04 Spherical Harmonic Modelling of Global Fields

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Spherical Harmonic Modelling of Global Fields](../04-spherical-harmonics-modelling.md).

---

## ★1 — Sampling a degree-30 field

- **Latitude:** at least $L + 1 = 31$ Gauss-Legendre nodes.
- **Longitude:** at least $2L + 1 = 61$ uniform samples, since the highest
  longitudinal wavenumber present is $m = L = 30$.

**The requirement is exact, not approximate.** The product of two degree-$L$
harmonics has degree $2L$, and a Gauss rule with $L+1$ nodes integrates a
degree-$2L$ polynomial exactly because $2(L+1) - 1 = 2L+1 \ge 2L$. With $L$ nodes
the rule is exact only to $2L-1$ and the products fold between degrees. The
lesson's measured table is the evidence: at 8 nodes for a degree-8 field the
coefficient error is $1.104\times10^{-1}$; at 9 nodes it is $6.1\times10^{-15}$.

---

## ★2 — Coefficient count

A real expansion truncated at degree $L$ contains $\sum_{l=0}^{L}(2l+1)$
coefficients, which sums to $(L+1)^2$. For $L = 30$:

$$(31)^2 = 961 .$$

Each degree contributes $2l+1$ coefficients, so the count grows quadratically in
the band limit — a $L = 100$ model has $101^2 = 10201$ coefficients, ten times
those of a $L=30$ model for a factor 3.3 in resolution.

---

## ★3 — Parseval in the fully normalised convention

With the $1/(4\pi)$ inner product of the lesson,

$$\frac{1}{4\pi}\int_{\Omega}f^2\,\mathrm{d}\Omega
= \sum_{l=0}^{L}\sum_{m=-l}^{l} f_{lm}^2 .$$

The lesson measures both sides as $31.421635044902$ from a random degree-4 set,
differing by $+1.1\times10^{-14}$.

**A non-zero residual indicates a sampling or normalisation error.** The identity
is exact when the quadrature is exact for the band, so a discrepancy of
$10^{-2}$ is not "numerical noise to be averaged away" — it means the analysis
grid is inadequate or the basis functions do not satisfy the orthonormality the
identity assumes. The first test to run is the Gram-matrix residual of the
lesson's Section 1, measured at $4.2\times10^{-15}$.

---

## ★4 — The 8-to-9 node jump

The improvement is a jump because the quadrature either integrates the relevant
product exactly or it does not. For a field of band $L = 8$, the product
integrands have degree $2L = 16$. A Gauss rule with $n$ nodes is exact to
$2n - 1$:

- $n = 8$: exact to degree 15 — one degree short of 16. The highest-degree
  products are integrated with an error that couples adjacent degrees, giving
  $1.104\times10^{-1}$.
- $n = 9$: exact to degree 17 — above 16, so everything in the band is exact, and
  the residual is round-off ($6.1\times10^{-15}$).

There is no gradual decay because there is no asymptotic regime: below the
threshold the error is a mis-integrated projection (of order the signal), above it
the error is double-precision round-off.

**Prediction for 10 nodes:** round-off, at the same level as 9 nodes —
$O(10^{-15})$, and if anything slightly larger because more nodes mean more
accumulated round-off (the lesson's measured values at 12 and 16 nodes are
$6.2\times10^{-15}$ and $2.1\times10^{-15}$, i.e. flat within a factor 3). Using
more nodes than required buys nothing but costs arithmetic; this is the practical
form of an exact band limit.

---

## ★5 — Downward continuation at $r/R = 1.03$

| $l$ | $(1.03)^l$ |
|---|---|
| 50 | 4.3839 |
| 100 | 19.2186 |
| 150 | 84.2527 |

An $O(1)$ amplification is reached already at $l \approx 0$–$50$; by $l = 150$ a
coefficient error is magnified by 84.

**Maximum usable degree** for $\eta = 10^{-2}$ and $\epsilon = 10^{-5}$:

$$l_{\max} = \frac{\log(10^{-2}/10^{-5})}{\log 1.03}
= \frac{6.9078}{0.029559} = 233.7 .$$

So the model supports degrees up to about 234 under that tolerance and error
level. Note the sensitivity to the geometry: at $r/R = 1.05$ the same tolerance
and error give $l_{\max} = 141.6$, and at $r/R = 1.10$ about $72.5$. The geometry,
not the instrument, becomes the binding constraint as the continuation distance
grows, which is why the useful way to quote a continuation is *with its
$l_{\max}$* rather than with the measured band alone.

---

## ★6 — What a map's smoothness demonstrates

**It demonstrates** that the field has been represented by a finite sum of
$C^\infty$ basis functions. Truncation at $L = 50$ removes all structure below
about $180^\circ/50 = 3.6^\circ$ of angular scale, and what remains cannot have
sharp features, by construction.

**It does not demonstrate** that the Earth is smooth, that the data support the
50-degree model, or that structure finer than the truncation is absent. The
coefficients above $L = 50$ are *zero by assumption*, not measured, and half the
information in a map — the resolution — is contained in the number 50 rather than
in the picture. A map presented without its degree limit and its coefficient
errors is missing precisely the quantities that would let a reader judge it.

---

## ★7 — Which degrees survive at $r/R = 1.05$

Target: a relative error $\eta = 10^{-2}$ in the continued field, from a
coefficient error $\epsilon = 10^{-6}$ at $r = 1.05R$:

$$l_{\max} = \frac{\log(10^{-2}/10^{-6})}{\log 1.05}
= \frac{9.2103}{0.048790} = 188.8 .$$

So degrees up to about **189 survive** and above that the amplified error exceeds
the tolerance. The measured factor at $l = 200$, $r/R = 1.10$ was
$1.899\times10^{8}$; at $r/R=1.05$ the factor at the same degree is
$1.729\times10^{4}$, and multiplying by the $10^{-6}$ coefficient error gives
$1.7\times10^{-2}$ — indeed above the $10^{-2}$ tolerance, consistent with
$l_{\max} = 188.8$.

**How much of the band is lost:** the original model carried degrees to 200, so
about $11.2$ degrees — roughly 6% of the band — are unusable. That is a much
milder loss than the 1.10 case, where the tolerance would cut $l_{\max}$ to about
72.5 and half the band would be lost.

**The honest presentation** of such a model therefore contains three numbers: the
band measured (200), the tolerance and coefficient error assumed, and the degree
that survives (189). Quoting only the measured band suggests the continued model
is as good as the measured one, and it is not.

---

## ★8 — Verifying a synthesis/analysis pair

**Test 1 — normalisation.**

- *Metric:* the Gram matrix
  $G_{ab} = \frac{1}{4\pi}\int Y_aY_b\,\mathrm{d}\Omega$ evaluated by the same
  quadrature the code uses for analysis, reported as $\max|G - I|$.
- *Expected with the correct convention:* round-off — measured
  $4.2\times10^{-15}$ for $l\le6$.
- *Expected with a wrong convention:* a diagonal that is not 1 but a smooth
  function of $l$ (a missing $\sqrt{2l+1}$ gives $G_{ll} = 2l+1$, so
  $\max|G-I| = 2L$). The test is decisive because the offending factor grows with
  degree and cannot hide.

**Test 2 — latitude nodes.**

- *Metric:* the maximum coefficient error of a *band-limited synthetic* field
  analysed on $n_{\rm lat}$ nodes, sweeping $n_{\rm lat}$ upward.
- *Expected with adequate sampling:* round-off from $n_{\rm lat} = L+1$ onward —
  measured $6.1\times10^{-15}$ at 9 nodes for $L = 8$, and flat thereafter.
- *Expected with too few nodes:* an error of order the signal
  ($1.1\times10^{-1}$ at 8 nodes) that does not shrink as $n_{\rm lat}\to L$ from
  below, then collapses at $L+1$. The signature is the *step*, and the test
  locates it, which is how the required band is confirmed rather than assumed.

**Why a synthetic field is the right reference.** Its coefficients are known
exactly, so the test measures the analysis operator and not the field's
regularity. Using a measured field would confound the two — the same reason every
number in this module is synthetic.
