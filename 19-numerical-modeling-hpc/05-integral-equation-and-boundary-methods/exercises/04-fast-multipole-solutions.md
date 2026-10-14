# Solutions — 19-05-04 Fast Multipole and Hierarchical Acceleration

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs. All models are **SYNTHETIC**.

Lesson: [04 Fast Multipole and Hierarchical Acceleration](../04-fast-multipole.md).

---

## ★1 — Monopole potential

$$\phi \approx \frac{M_0}{d} = \frac{404.726574}{2.001436} = 202.218080
\ \mathrm{km^{-1}},$$

since the kernel is $1/r$ with $r$ in km and the strengths carry the units. The
printed value is $202.2180799309$; the exact direct sum is $205.6370151508$, so the
monopole alone is in error by $1.663\times10^{-2}$.

---

## ★2 — Admissibility and $s/d$

Accept a node as far when $|y - c| > \theta s$, with $s$ the node's half-width and
$\theta$ the opening angle. The series expansion of $1/|y - x_j|$ is geometric
with ratio $\delta/d$ and $|\delta|\le s$, so the criterion bounds $s/d \le
1/\theta$. The truncation error after $p$ terms is then bounded by
$(s/d)^{p}$ up to a constant, which is exactly the geometric rate the table
measures: with $s/d = 0.2470$ the error falls by about $0.247$ per added term in
the asymptotic regime.

---

## ★3 — Which side, and does the series alternate?

The node spans $[$centre $- s$, centre $+ s]$, and $|y - c| = 1.998564 > s =
0.494$ (half of $0.988$), so the target is outside the node's span. Since
$c = 0.498564$ km is positive and $y = -1.5$ km, we have $y < c$: the target is
**to the left** of the node.

Therefore $|y - x_j| = (c - y) + \delta_j = D + \delta_j$ with $D > 0$, and

$$\frac{1}{|y-x_j|} = \frac{1}{D}\left(1 - \frac{\delta_j}{D} +
\frac{\delta_j^{2}}{D^{2}} - \cdots\right),$$

so the far-field series $\sum_k (-1)^{k}M_k/D^{k+1}$ **alternates**. Using the
non-alternating form here flips the sign of every odd moment — a reflection error
of order one, not of order $(s/d)^{p}$.

---

## ★4 — The per-term ratio

$$\frac{5.571\times10^{-4}}{1.743\times10^{-6}} = 319.6 \quad\text{over 5 terms}
\;\Rightarrow\; 319.6^{1/5} = 3.17 \text{ per term}.$$

A ratio of $3.17$ per term corresponds to $(s/d)^{-1} = 1/0.2470 = 4.05$ for a
pure geometric law; the measured $3.17$ is lower, which is the effect of the
non-monotone $p = 1,2$ behaviour and of the mixture of moment magnitudes. At
$p = 12$, extrapolating the last four terms:

$$1.743\times10^{-6}\times3.17^{-4} = \eta \approx 1.7\times10^{-8}.$$

The assumption behind the estimate is that the ratio is constant over the next
four terms, which the table supports for $p \ge 4$ but not for $p < 3$.

---

## ★5 — Counts against time

$$\text{direct pairs} / (\text{far nodes} + \text{direct particles})
= \frac{1.024\times10^{7}}{33\,636 + 55\,066} = 115.4 .$$

So the tree does about $115\times$ fewer interactions, and reports a *time*
ratio of $0.16$ — i.e. it is $6\times$ **slower**. The gap is entirely in the
implementation: the direct sum is one vectorised numpy expression whose $10^{7}$
interactions are executed by compiled loops, while the tree performs $88\,702$
interactions through Python-level recursion, with a function call and a node
object attribute lookup per interaction. The count ratio describes the algorithm;
the time ratio describes this implementation, and only a compiled tree code would
express the former.

---

## ★6 — Growth of the direct work with $\theta$

Between $\theta = 1.0$ and $5.0$, $\log\theta$ increases by $\ln 5 = 1.609$, and
the direct-particle count rises from $4699$ to $22054$, a factor of $4.69$:

$$\frac{\ln 4.69}{\ln 5} = 0.963 \;\Rightarrow\; N_{\text{direct}} \propto
\theta^{0.96}.$$

So the direct work grows almost **linearly** in $\theta$ while the accuracy
improves geometrically in $p$ (or rapidly in $\theta$). The consequence for a
tuning strategy: buy accuracy with $p$ first, because each added moment costs one
term in the far-field sum, whereas raising $\theta$ costs direct interactions for
every target. The optimum in a real code is set by the relative constant costs of
a far-field term and a direct pair, which is why the measured table — not a rule
of thumb — is what a code should be tuned with.

---

## ★7 — Why a larger $\theta$ is more accurate

The far test is $|y-c| > \theta s$. Increasing $\theta$ makes the test
**stricter**: fewer nodes qualify as far, so more of the near field is summed
directly (exactly), and the nodes that remain far are further away, with a smaller
$s/d$. The accuracy therefore improves from
$8.973\times10^{-4}$ to $1.975\times10^{-6}$, a factor of $454$.

The cost, measured at $n = 400$: direct particles rise from $9063$ to $22054$,
a factor of $2.43$, and far-field nodes from $2851$ to $4680$. Total interactions
rise from $11\,914$ to $26\,734$, i.e. $2.24\times$ more work for $454\times$ less
error. In this regime $\theta$ is the cheaper knob, and the crossover point where
$p$ becomes cheaper is what a tuning experiment must locate.

---

## ★8 — Sign convention or admissibility?

- **A sign/parity error** affects *only* the targets on one side of a node, and it
  affects them by an $O(1)$ relative error that does **not** shrink with $p$.
  Observable: plot the error against the target's side; errors cluster on one side
  and are flat in $p$.
- **A wrong admissibility test** (too small $\theta$) affects *all* targets, and
  the error **does** shrink as $p$ increases, because the truncation error is
  $(s/d)^{p}$ even for a badly chosen $s/d$.

The experiment: run the same geometry at $p = 2$ and $p = 10$ with $\theta$
unchanged. If the error falls, the expansion is right and the criterion is loose;
if the error is unchanged and concentrated on one side of the nodes, the
convention is wrong. The lesson's own first version failed exactly this way — an
$O(1)$ error with no improvement in $p$ — and the direct-sum comparison caught it
immediately.
