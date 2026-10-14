# Solutions — 06-09-05 AVO/AVA Analysis and Its Assumptions

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [05 Amplitude vs Offset](../05-amplitude-vs-offset.md).

---

## ★1 — Intercept and gradient

$$A = \tfrac12\left(\frac{\Delta v_p}{\bar v_p}
+ \frac{\Delta \rho}{\bar \rho}\right)
= \tfrac12(0.10 + 0.05) = 0.0750,$$
$$B = \tfrac12\frac{\Delta v_p}{\bar v_p}
- 2\left(\frac{\bar v_s}{\bar v_p}\right)^{2}
\left(\frac{\Delta \rho}{\bar \rho}
+ 2\frac{\Delta v_s}{\bar v_s}\right)
= 0.0500 - 2(0.55)^{2}(0.05 + 0.30)$$
$$= 0.0500 - 0.605 \times 0.350 = 0.0500 - 0.21175 = -0.16175 .$$

**What they measure.** $A = R(\theta=0)$ is the *impedance* contrast at normal
incidence: it depends on $v_p$ and $\rho$ only through their sum. $B$ is the
angular *gradient*, and it is the part of the reflection coefficient that
contains $v_s$ — the quantity normal-incidence data cannot see. A negative $B$
means the reflection amplitude falls with angle.

---

## ★2 — Why $A$ is not the reflection coefficient

$$\text{difference} = 0.094079 - 0.093894 = +1.85\times10^{-4}.$$

The Aki–Richards formulas are **first-order in the contrasts**: they replace
ratios such as $v_2/(v_1+v_2)$ by average-parameter forms, and the neglected
terms are of second order in $\Delta v/v$ and $\Delta\rho/\rho$. For this
interface the contrasts are about $13\%$ in $v_p$, and the *net* residual after
the cancellation of the leading second-order terms is the measured
$1.85\times10^{-4}$, i.e. $0.2\%$ of $R$. **The honest statement is that an AVO
"intercept" is a first-order impedance contrast, and quoting it as the
normal-incidence reflection coefficient is a small but real error** — small
compared with real-data noise, and not small compared with the precision of a
well-calibrated inversion.

---

## ★3 — The demonstration's interface

$$\bar v_p = \frac{3000+3400}{2} = 3200, \qquad
\bar v_s = \frac{1600+1900}{2} = 1750, \qquad
\bar \rho = \frac{2300+2450}{2} = 2375,$$
$$\frac{\bar v_s}{\bar v_p} = \frac{1750}{3200} = 0.546875,$$
$$\frac{\Delta v_p}{\bar v_p} = \frac{400}{3200} = 0.125, \qquad
\frac{\Delta v_s}{\bar v_s} = \frac{300}{1750} = 0.171429, \qquad
\frac{\Delta\rho}{\bar\rho} = \frac{150}{2375} = 0.063158,$$
$$A = \tfrac12(0.125 + 0.063158) = 0.094079 \quad\text{(printed } 0.09408\text{)},$$
$$B = \tfrac12(0.125) - 2(0.546875)^{2}(0.063158 + 2\times0.171429)
= 0.0625 - 0.598145\times0.406016 = -0.180356
\quad\text{(printed } -0.18036\text{)}. \quad\checkmark$$

Both match the demonstration.

---

## ★4 — Reduction to the normal-incidence coefficient

Write $Z_1 = \rho_1v_{p1}$, $Z_2 = \rho_2v_{p2}$ and expand to first order in the
contrasts, using $\bar Z = (Z_1+Z_2)/2$:

$$R = \frac{Z_2-Z_1}{Z_2+Z_1} = \frac{\Delta Z}{2\bar Z}
= \frac12\frac{\Delta(\rho v_p)}{\bar\rho\bar v_p}
= \frac12\left(\frac{\Delta\rho}{\bar\rho}
+ \frac{\Delta v_p}{\bar v_p}\right) + \mathcal{O}(\text{contrast}^{2}) = A.$$

The neglected terms are the second-order products
$\tfrac12(\Delta\rho/\bar\rho)(\Delta v_p/\bar v_p)$, plus the third-order terms
from expanding $1/(2\bar Z)$. For a $13\%$ contrast the leading neglected term is
$0.5\times0.063\times0.125 = 3.9\times10^{-3}$, and it largely cancels against the
other second-order terms, leaving the measured $1.85\times10^{-4}$.

**Note the structural point:** $A$ is symmetric in $\rho$ and $v_p$. No
rearrangement of first-order theory can separate them, which is why the
separation requires either non-normal incidence ($B$, which contains $v_s$) or an
independent measurement.

---

## ★5 — Fluid substitution as the demonstration shows it

| saturation | $\rho$ (kg/m³) | $v_p$ (m/s) | $v_s$ (m/s) | $R(0)$ | $R(30^\circ)$ |
|---|---|---|---|---|---|
| brine | 2238 | 3233 | 1891 | $+0.0236$ | $-0.0120$ |
| oil | 2188 | 3062 | 1912 | $-0.0148$ | $-0.0626$ |
| gas | 2025 | 3046 | 1988 | $-0.0560$ | $-0.1072$ |

As the pore fluid becomes lighter (brine → oil → gas):

- **Density falls** (2238 → 2025 kg/m³): the fluid is simply lighter.
- **$v_p$ falls** because the bulk modulus of the *saturated* rock falls: the
  fluid's own bulk modulus drops from that of brine toward that of gas, and
  Gassmann's relation transfers that loss to the saturated frame.
- **$v_s$ rises** because $v_s = \sqrt{\mu/\rho}$ and the shear modulus $\mu$ is
  **unchanged** by the fluid (a fluid cannot support shear): only the density in
  the denominator moves, so $v_s$ must increase as $\rho$ decreases.

The reflection coefficient changes **sign** across the fluid sequence, and the
gradient $B$ becomes more negative. That sign change is the physical basis of
AVO hydrocarbon detection — and the reason a gas sand can be "soft" even though
its shear velocity is high.

---

## ★★★7 — Verifying the equivalence with the printed values

Applying the definitions of ★3 to the printed (rounded) parameters:

| model | $v_p$ | $v_s$ | $\rho$ | $A$ | $B$ |
|---|---|---|---|---|---|
| A | 3400 | 1900 | 2450 | $+0.094079$ | $-0.180356$ |
| B | 3026 | 1705 | 2754 | $+0.094144$ | $-0.180223$ |

Differences: $\Delta A = 6.6\times10^{-5}$, $\Delta B = 1.3\times10^{-4}$. The
two-term reflection coefficients then differ by at most

$$\max_{0^\circ\le\theta\le40^\circ}|R_A-R_B| = 1.2\times10^{-4},$$

reached at $40^\circ$. **The demonstration reports exactly $0.00000$ because it
solved for model B from the unrounded equations; the residual here is the
rounding of the four printed numbers.** That is itself the lesson: the family is
a *ridge*, and a change of $-374\ \mathrm{m\,s^{-1}}$ in $v_p$ (and
$-195\ \mathrm{m\,s^{-1}}$ in $v_s$) is invisible in near-angle data to within
$10^{-4}$.

---

## ★★★8 — A third family member (specification)

**Constraint to impose:** keep the intercept $A$ fixed by requiring

$$\frac{\Delta\rho}{\bar\rho} + \frac{\Delta v_p}{\bar v_p} = 2A = 0.188158,$$

and keep the gradient $B$ fixed through the relation of ★3. One convenient
parametrisation is to choose a value of $\bar v_s/\bar v_p$ and then solve for the
two contrast ratios, which yields a one-parameter family
$\big(v_p(\lambda), v_s(\lambda), \rho(\lambda)\big)$ that reproduces the same
two-term curve. Any member can be constructed by fixing, say, $\rho$ and solving
the two equations for $\Delta v_p/\bar v_p$ and $\Delta v_s/\bar v_s$.

**Two independent measurements that break the degeneracy.**

1. **Far-angle data ($\theta \gtrsim 35^\circ$)** constrains the third
   (density-weighted) term of the Aki–Richards expansion, which is independent of
   the first two *as a function of angle*. The demonstration measures this: over
   $0$-$40^\circ$ the third term separates the two models at $3.39\sigma$.
2. **An independent $v_s$ or density measurement** (dipole sonic log, or a
   density log; or a converted-wave survey). This is independent of the AVO
   curve because it is a *different* physical observable, not a different
   angular sample of the same one.

A third, weaker constraint is a **Gassmann-consistent rock-physics prior**: it
links $v_p$, $v_s$ and $\rho$ through the fluid content, at the cost of assuming
the frame and fluid properties — which is precisely the assumption the AVO
inversion is often used to test.

---

## ★★★9 — Acquisition for a routine three-term separation (specification)

**Requirement.** Data at angles up to $\approx40^\circ$ with an angular
sampling fine enough to fit three terms, and a signal-to-noise ratio sufficient
for the third term's contribution (measured at $3.39\sigma$ in the
demonstration over $0$-$40^\circ$).

**Maximum offset.** For a target at $t_0 = 2.0\ \mathrm{s}$,
$v_{\text{rms}} = 2800\ \mathrm{m\,s^{-1}}$ and a target depth
$z = v_{\text{rms}}t_0/2 = 2800\ \mathrm{m}$, the offset needed for
$\theta = 40^\circ$ follows from $\tan\theta = x/(2z)$ (source–receiver geometry,
image point at half the offset):

$$x = 2z\tan\theta = 2\times2800\times\tan40^\circ
= 5600\times0.8391 = 4699\ \mathrm{m}.$$

So a maximum offset of about $4.7\ \mathrm{km}$, against $\approx2.0\ \mathrm{km}$
for a $20^\circ$ (two-term) analysis. The cost is therefore roughly a
$2.4\times$ longer streamer or a larger source–receiver spread — plus the
processing cost of the longer-offset data (refraction, anellipticity and
multiple contamination all grow with offset, which is why the demonstration's
third-term test is described as *heavily weighted by density* and fragile).
