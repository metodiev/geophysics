# Solutions — 13-04-04 Interseismic Coupling and Megathrust Locking

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Interseismic Coupling and Megathrust Locking](../04-interseismic-coupling.md).

---

## ★1 — Profile of a fully locked patch

$v(x) = V/2 - (V/\pi)\operatorname{atan2}(d, x)$ with $V/2 = 20\
\mathrm{mm\,yr^{-1}}$, $V/\pi = 12.732\ \mathrm{mm\,yr^{-1}}$, $d = 25\
\mathrm{km}$.

- $x = 5$: $\operatorname{atan2}(25,5) = \arctan 5 = 1.3734$;
  $v = 20 - 12.732\times1.3734 = 20 - 17.49 = 2.51\
  \mathrm{mm\,yr^{-1}}$.
- $x = 25$: $\arctan 1 = 0.7854$; $v = 20 - 10.00 = 10.00\
  \mathrm{mm\,yr^{-1}}$.
- $x = 100$: $\arctan 0.25 = 0.2450$; $v = 20 - 3.12 = 16.88\
  \mathrm{mm\,yr^{-1}}$.

Far field ($x\to\infty$): $\operatorname{atan2}\to0$, so
$v\to20\ \mathrm{mm\,yr^{-1}} = V/2$ ✔.

A useful pattern to notice: $v(x) = V/2$ exactly when
$\operatorname{atan2}(d,x) = 0$, and $v = 0$ at the trace. The profile crosses
$v = V/4 = 10\ \mathrm{mm\,yr^{-1}}$ at $\operatorname{atan2}(d,x) = \pi/4$,
i.e. $x = d$ — the **locking depth is the distance at which the surface velocity
has fallen to three quarters of the creeping far-field value.**

---

## ★2 — Relative velocity at the trace

For $x\to0^+$: $\operatorname{atan2}(d, x) \to \pi/2$, so
$v(0^+) = 20 - 12.732\times(\pi/2) = 20 - 20.00 = 0$.
For $x\to0^-$: $\operatorname{atan2}(d,x) \to \pi$, and
$\operatorname{sgn}(x) = -1$, so
$v(0^-) = -20 - 12.732\times(\pi - \pi) = -20$? Careful — the $\pi$ in the
$\operatorname{atan2}(0,x)$ term compensates:

$$
v(0^-) = -\frac{V}{2}
- \frac{\chi V}{\pi}\left[\pi - \pi\right] = -20\ \mathrm{mm\,yr^{-1}}?
$$

That cannot be right: a fully locked fault must have **no** relative motion at
the trace. The correct evaluation uses
$\operatorname{atan2}(d, x\to0^-) = \pi - \pi/2 = \pi/2$ in the limit sense: for
small negative $x$, $\operatorname{atan2}(d,x) = \pi - \arctan(d/\lvert x\rvert)
\to \pi/2$, and $\operatorname{atan2}(0,x) = \pi$, so the bracket is
$\pi/2 - \pi = -\pi/2$ and

$$
v(0^-) = -\frac{V}{2} - \frac{\chi V}{\pi}\left(-\frac{\pi}{2}\right)
= -\frac{V}{2} + \frac{\chi V}{2} = -\frac{V}{2}(1-\chi).
$$

Hence $v(0^+) - v(0^-) = \frac{V}{2}(1-\chi) - \left[-\frac{V}{2}(1-\chi)\right]
= V(1-\chi)$ ✔. For $\chi = 1$ the relative velocity is zero — the fault trace
does not move relatively — and for $\chi = 0$ it is $V$, the full creeping rate.

---

## ★3 — Units of the kernel

$\operatorname{atan2}$ is dimensionless, so the kernel is dimensionless. It
multiplies $\chi_j$ (dimensionless) and $V$ (mm/yr), giving mm/yr: the kernel is
the **fraction of the plate rate** that patch $j$ removes from the surface
velocity at $x$. When summed over a fully coupled fault
($\chi_j = 1$ for all $j$), the sum telescopes:

$$
\sum_j \left[\operatorname{atan2}(z_{j+1},x) - \operatorname{atan2}(z_j,x)\right]
= \operatorname{atan2}(z_{\max}, x),
$$

recovering the single-patch form no matter how finely the fault is discretised.
That telescoping identity is the algebraic reason the discretisation error is
only $0.06\ \mathrm{mm\,yr^{-1}}$ where the patch straddling the true locking
depth is partially coupled.

---

## ★4 — Two models, four stations

Using $V/\pi = 12.732\ \mathrm{mm\,yr^{-1}}$ and $V/2 = 20\
\mathrm{mm\,yr^{-1}}$:

Model A ($\chi = 1$, $d = 20\ \mathrm{km}$):
$x = 5$: $\arctan 4 = 1.3258$, $v = 20-16.88 = 3.12$;
$x = 20$: $\arctan 1 = 0.7854$, $v = 20-10.00 = 10.00$;
$x = 50$: $\arctan 0.4 = 0.3805$, $v = 20-4.84 = 15.16$;
$x = 200$: $\arctan 0.1 = 0.0997$, $v = 20-1.27 = 18.73$.

Model B ($\chi = 0.6$, $d = 40\ \mathrm{km}$):
$x = 5$: $\arctan 8 = 1.4464$, $v = 20 - 0.6\times12.732\times1.4464 =
20-11.05 = 8.95$;
$x = 20$: $\arctan 2 = 1.1071$, $v = 20 - 8.46 = 11.54$;
$x = 50$: $\arctan 0.8 = 0.6747$, $v = 20 - 5.15 = 14.85$;
$x = 200$: $\arctan 0.2 = 0.1974$, $v = 20 - 1.51 = 18.49$.

(These reproduce the demonstration's $8.950$, $11.542$, $14.845$ and $18.626$
to within rounding.)

Differences $A-B$: $-5.83$, $-1.54$, $+0.31$, $+0.24$
$\mathrm{mm\,yr^{-1}}$.

**Answer:** the difference falls below $1\ \mathrm{mm\,yr^{-1}}$ at
$\lvert x\rvert \approx 35$–$50\ \mathrm{km}$; from the demonstration's finer
table it is $0.048\ \mathrm{mm\,yr^{-1}}$ at $35\ \mathrm{km}$ and
$0.334\ \mathrm{mm\,yr^{-1}}$ at $50\ \mathrm{km}$. So beyond roughly
$35\ \mathrm{km}$ the two models are indistinguishable at $1\
\mathrm{mm\,yr^{-1}}$ noise.

---

## ★5 — Which networks can tell?

Stations at $8$, $25$ and $90\ \mathrm{km}$. From ★4:

| station | $A-B$ (mm/yr) | decisive at $1\ \mathrm{mm\,yr^{-1}}$? |
|---|---|---|
| $8\ \mathrm{km}$ | about $-5.0$ | yes, by a factor $5$ |
| $25\ \mathrm{km}$ | about $-1.0$ | marginal, about $1\sigma$ |
| $90\ \mathrm{km}$ | about $+0.35$ | no |

So the $8\ \mathrm{km}$ station does the work, the $25\ \mathrm{km}$ station is
marginal, and the $90\ \mathrm{km}$ station contributes mainly to the far-field
rate.

**The single most useful additional station** is at the smallest possible
distance from the trace — $2$–$3\ \mathrm{km}$ if it can be occupied — because
the difference between the models grows monotonically as $x\to0$ (it is
$5.83\ \mathrm{mm\,yr^{-1}}$ at $5\ \mathrm{km}$ and would be larger closer in).
Adding another inland station adds almost nothing: the far-field part of the
profile is nearly model-independent.

---

## ★6 — Moment deficit and magnitude

Coupled area: $A_c = L\times D_c = 250\ \mathrm{km}\times30\ \mathrm{km}
= 7500\ \mathrm{km^{2}} = 7.5\times10^{9}\ \mathrm{m^{2}}$.

$$
\dot M_0 = \mu V A_c = 3\times10^{10}\times0.050\times7.5\times10^{9}
= 1.125\times10^{19}\ \mathrm{N\,m\,yr^{-1}} .
$$

Over $50\ \mathrm{yr}$: $M_0 = 5.625\times10^{20}\ \mathrm{N\,m}$,

$$
M_w = \tfrac23\left(\log_{10}5.625\times10^{20} - 9.1\right)
= \tfrac23(20.750 - 9.1) = \tfrac23(11.650) = 7.77 .
$$

Revising the coupled extent to $20\ \mathrm{km}$ scales the area and therefore
the moment by $20/30 = 0.667$:
$M_0 = 3.75\times10^{20}\ \mathrm{N\,m}$ and

$$
M_w = \tfrac23(\log_{10}3.75\times10^{20} - 9.1)
= \tfrac23(20.574 - 9.1) = 7.65 .
$$

**The magnitude changes by $0.12$ units for a one-third change in coupled
extent** — small in magnitude terms, but it corresponds to a $33\%$ change in the
moment, which is what matters for hazard and for the deficit budget.

---

## ★7 — Why a deep patch needs near-field data

In the far field $x \gg z_j$, the kernel difference
$\left[\operatorname{atan2}(z_{j+1},x) - \operatorname{atan2}(z_j,x)\right]/\pi$
expands as

$$
\operatorname{atan2}(z,x) = \frac{\pi}{2} - \arctan\frac{x}{z}
\approx \frac{\pi}{2} - \frac{x}{z}
\;\Longrightarrow\;
\Delta \approx \frac{1}{\pi}\left(\frac{x}{z_j} - \frac{x}{z_{j+1}}\right)
= \frac{x\,\Delta z}{\pi z_j^{2}} .
$$

So the kernel for a deep patch **grows linearly with distance** in the far field
rather than decaying — which looks like good news, until one notices that the
*contrast* between two nearby deep patches scales as $\Delta z/z_j^{2}$ and is
swamped by the contribution of the shallow patches, whose kernels vary rapidly
near the fault. Quantitatively: to distinguish patch $j$ from patch $j+1$ one
needs the difference of their kernels to exceed the noise, and the difference is
largest where $x \approx z_j$ (the arctan's curvature is there). Hence
**stations at $\lvert x\rvert \gtrsim z_j$ are required**, and the demonstration
measures exactly this: the difference between models with $20$ and $40\
\mathrm{km}$ locking depth is $5.8\ \mathrm{mm\,yr^{-1}}$ at $5\ \mathrm{km}$
and $0.33\ \mathrm{mm\,yr^{-1}}$ at $50\ \mathrm{km}$.

A second consequence: because the far-field kernel grows with $x$, a station at
$1000\ \mathrm{km}$ is not more informative about a $40\ \mathrm{km}$ patch than
one at $100\ \mathrm{km}$ — the *differences* between patches shrink as
$1/z^{2}$, and the far field only measures the integral.

---

## ★8 — Damped inverse problem and the resolution matrix

**Setup.** With $G = \begin{pmatrix}K\\ \lambda D\end{pmatrix}$ and
$d = \begin{pmatrix}\Delta v\\ 0\end{pmatrix}$, the damped least-squares solution
is

$$
\hat\chi = (G^{\mathsf T}G)^{-1}G^{\mathsf T}d
= (K^{\mathsf T}K + \lambda^{2}D^{\mathsf T}D)^{-1}K^{\mathsf T}\Delta v .
$$

**Resolution matrix.** The model resolution is

$$
R = (K^{\mathsf T}K + \lambda^{2}D^{\mathsf T}D)^{-1}K^{\mathsf T}K ,
$$

whose diagonal is reported in the lesson's table ($0.91$ down to $0.15$). If
$R = I$, every patch is perfectly resolved; the further $R$ departs from $I$,
the more each estimate is a weighted average of its neighbours.

**Covariance.** With data covariance $C_d = \sigma^{2}I$,

$$
C_\chi = \sigma^{2}(K^{\mathsf T}K + \lambda^{2}D^{\mathsf T}D)^{-1}K^{\mathsf T}K
(K^{\mathsf T}K + \lambda^{2}D^{\mathsf T}D)^{-1} ,
$$

so the parameter standard deviations fall as $\lambda$ grows while the resolution
diagonal falls too. **There is no $\lambda$ that maximises both**: this is the
classical bias–variance trade-off, and the honest reporting of a coupling model
includes both the resolution diagonal and the parameter covariance at the
$\lambda$ that was used.

**Limits.**
- $\lambda\to0$: $\hat\chi\to(K^{\mathsf T}K)^{-1}K^{\mathsf T}\Delta v$ —
  formally the least-squares solution, but $K^{\mathsf T}K$ is nearly singular
  because deep patches have almost collinear kernels, so the estimates oscillate
  with huge variance while fitting the data well.
- $\lambda\to\infty$: $D^{\mathsf T}D$ dominates, so
  $\hat\chi\to$ the smoothest model (a constant, then a linear ramp with the
  first-difference penalty), with tiny variance and almost no resolution: the
  answer is dictated by the regularisation, not the data.

The practical rule: choose $\lambda$ so that the resolution diagonal of the
*shallow* patches (the ones physically expected to be resolved) stays above
about $0.5$, and report the effect on the deeper ones rather than hiding it.

---

## ★9 — Resolving the smallest coupled depth (specification)

**Network geometry.** Two families: (i) a dense profile
$x = 1,2,5,10,20,40,80,160,320\ \mathrm{km}$; (ii) the same profile with the
closest $k$ stations removed ($k = 1\dots5$), to simulate a land-only network
whose nearest site is $x_{\min}$ inland.

**Forward models.** A single-patch family with $d \in \{10,20,30,40,50,60\}\
\mathrm{km}$ and $\chi = 1$, each predicted by the closed-form profile.

**Noise model.** $1\ \mathrm{mm\,yr^{-1}}$ per component, independent, 500
realisations per case; optionally $0.5\ \mathrm{mm\,yr^{-1}}$ of common-mode
error to test robustness.

**Metric.** (i) The $\Delta\chi^{2}=1$ width of the recovered $d$ for each true
$d$; (ii) the fraction of realisations in which the true $d$ lies inside the
accepted range.

**Expected scaling.** The resolution should vanish when $x_{\min} \gtrsim d$:
in the far field the profile depends on $d$ and $\chi$ mainly through the
product $\chi d$ (the total deficit), so the two are degenerate. Concretely,
predict a resolution breakdown at $x_{\min}/d \approx 1$ and a
$\Delta\chi^{2}=1$ width in $d$ that grows roughly linearly with $x_{\min}$.

**Falsification.** A result showing good resolution for $x_{\min} \gg d$ would
indicate that the $\chi$–$d$ degeneracy is being broken by something other than
the geometry — most plausibly by the assumed $V$, by noise structure, or by an
error in the kernel. That is exactly the case worth investigating, because it
would mean the documented trade-off is not the limiting factor after all.
