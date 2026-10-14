# Solutions — 09-03-03 IP Acquisition, Chargeability and Phase Units

> **Read after attempting the exercises.** Lesson:
> [03 IP Acquisition](../03-ip-acquisition.md). All models **SYNTHETIC**.

---

## ★1 — Sample count and time for a phase target

$$M = 2\left(\frac{\sigma_n}{A\,\sigma_{\varphi}}\right)^{2}
= 2\left(\frac{0.1}{2\times10^{-3}}\right)^{2}
= 2 \times 50^{2} = 5000\ \text{samples}.$$

At $16$ samples per cycle and a $2$ Hz fundamental, one cycle lasts $0.5$ s:

$$\text{cycles} = \frac{5000}{16} = 312.5, \qquad
t_{\text{acq}} = 312.5 \times 0.5\ \mathrm{s} = 156.25\ \mathrm{s}.$$

Note that the result is independent of the absolute signal amplitude: only the
ratio $\sigma_n/A$ enters.

---

## ★2 — Drift bias

$$\Delta M_{\text{int}} = \frac{\frac{1}{2}sT}{V_p}
= \frac{0.5 \times 5.0\times10^{-3} \times 2.0}{20.0}
= 2.5\times10^{-4}\ \mathrm{s} = 0.250\ \mathrm{ms}.$$

The bias is additive to the true chargeability, and it grows linearly with both
the drift rate and the window length, so a longer window makes this error worse
even though it improves the random-noise average.

---

## ★3 — The three quantities

| quantity | unit | window-dependent? |
|---|---|---|
| window-integral chargeability | ms (mV/V per second) | yes, via $T$ and via the charging time |
| window-average chargeability | mV/V | yes, as $M_{\text{int}}/T$ |
| percent frequency effect | % | no window; depends on the two frequencies |
| phase | mrad or degrees | no window; depends on the frequency |

The first two are the same measurement reported with different conventions; they
coincide numerically only for a one-second window. PFE and phase are frequency
domain quantities and have no window at all — but they do depend on which
frequencies were chosen, which is the same kind of choice.

---

## ★4 — Deriving and evaluating the noise law

With $y_k = A\sin\left(\theta_k + \varphi\right) + n_k$ and the projections
$\hat a = \frac{2}{M}\sum_k y_k\cos\theta_k$,
$\hat b = \frac{2}{M}\sum_k y_k\sin\theta_k$, orthogonality over whole cycles
gives $X^{\mathsf{T}}X = (M/2)I$, hence
$\operatorname{var}(\hat a) = \operatorname{var}(\hat b) = 2\sigma_n^{2}/M$.

Since $\varphi = \arctan(a/b)$ with $a = A\sin\varphi$, $b = A\cos\varphi$,

$$\sigma_{\varphi}^{2} =
\frac{\cos^{2}\varphi}{A^{2}}\operatorname{var}(\hat a) +
\frac{\sin^{2}\varphi}{A^{2}}\operatorname{var}(\hat b)
= \frac{2\sigma_n^{2}}{MA^{2}}
\;\Longrightarrow\;
\sigma_{\varphi} = \frac{\sigma_n}{A\sqrt{M/2}} .$$

**(a)** $A/\sigma_n = 50$, $M = 2000$:
$\sigma_{\varphi} = \frac{1}{50\sqrt{1000}} = 6.3246\times10^{-4}$ rad
$= 0.632$ mrad.

**(b)** $A/\sigma_n = 20$, $M = 32$:
$\sigma_{\varphi} = \frac{1}{20\sqrt{16}} = \frac{1}{80} = 1.25\times10^{-2}$ rad
$= 12.5$ mrad, against the measured $13.171$ mrad — the law is $5\%$ low at
this small sample count, which is the expected behaviour as the $\arctan$
linearisation and the orthogonality argument degrade.

---

## ★5 — Bounding the phase from chargeability

$$\varphi_{\min} = \frac{M}{(M/\varphi)_{\max}} = \frac{12.0}{6.612}
= 1.81\ \mathrm{mrad}, \qquad
\varphi_{\max} = \frac{M}{(M/\varphi)_{\min}} = \frac{12.0}{0.540}
= 22.2\ \mathrm{mrad}.$$

So $12.0$ ms is consistent with any phase between $1.8$ and $22.2$ mrad under the
measured spread of models. The measurement that narrows it is a *direct* phase
(or PFE) measurement on the same ground, which removes the need for a conversion
factor altogether; a fit of a model to the full decay curve is the second-best
option.

---

## ★6 — Charging bias

$$\text{bias} = \frac{20.690}{72.987} - 1 = 0.28348 - 1 = -71.65\%.$$

Check: $\left(1 - e^{-t_{\text{on}}/\tau}\right)$ with
$t_{\text{on}}/\tau = 0.50/1.5 = 0.3333$ gives
$1 - e^{-0.3333} = 0.28347$ — identical, as it must be, since the window factor
$\left(1 - e^{-T/\tau}\right)$ is common to both the measured and the reference
value and cancels in the ratio.

---

## ★7 — One-hour acquisition (specification and arithmetic)

**Constraint set.** $\tau \in \left[0.5, 5\right]$ s; $m \approx 0.05$; target
$\pm20\%$ on $m$; budget $3600$ s per sounding.

**Step 1 — on-time.** To charge the slowest $\tau = 5$ s to within $5\%$,
$t_{\text{on}} \ge 3\tau = 15$ s. Choose $t_{\text{on}} = 20$ s
($\left(1 - e^{-4}\right) = 0.9817$).

**Step 2 — decay traces per stack.** A window set that resolves
$\tau \in \left[0.5, 5\right]$ needs $T$ out to about $5\tau_{\max} = 25$ s.
With $t_{\text{on}} = 20$ s and $T = 25$ s the cycle is $45$ s.

**Step 3 — cycles.** Budget $3600$ s allows
$3600/45 = 80$ complete cycles. Splitting them $40$ for a short window
($T_1 = 4$ s) and $40$ for a long window ($T_2 = 25$ s) keeps the cycle shorter
for the first set: two sub-surveys of $40 \times 24 = 960$ s and
$40 \times 45 = 1800$ s, total $2760$ s, inside budget.

**Step 4 — uncertainty.** With per-decay noise $\sigma_n$ and $N = 40$ stacks,
the stacked noise is $\sigma_n/\sqrt{40} = 0.158\,\sigma_n$. The chargeability
uncertainty is
$\frac{1}{V_p}\sqrt{\sum \left(\sigma_n/\sqrt{N}\right)^{2}\Delta t^{2}}$ per
sample; with the demonstration's drift-free numbers as a scale, a
$72.987$ ms chargeability measured with $40$ stacks and a $1\%$ per-sample noise
level gives a relative uncertainty of order
$0.01/\sqrt{40} = 0.0016$, i.e. $0.16\%$ — far better than the $\pm20\%$ target.
The binding constraint is therefore *systematic*, not random: the charging
correction at $t_{\text{on}} = 20$ s ($1.8\%$ error for $\tau = 5$ s) and drift
removal dominate the error budget, and both must be reported.

**Step 5 — frequency-domain cross-check.** One 1 mrad phase measurement at
$0.1$-$1$ Hz with $A/\sigma_n = 20$ needs $2\left(20/10^{-3}\right)^{2} =
8.0\times10^{5}$ samples; at $1$ Hz and $32$ samples per cycle that is
$25000$ s and does not fit the budget. The honest design is therefore
time-domain within the hour, with the phase measurement used on a subset of
sites rather than everywhere.

---

## ★8 — Model failure versus noise failure

The two window sets give $\left(0.111, 1.266\ \mathrm{s}\right)$ and
$\left(0.090, 3.960\ \mathrm{s}\right)$ — a shift of $-18.9\%$ in $m$ and a
factor $3.13$ in $\tau$ from the window alone. If the effect were noise, adding
data (more windows) would move the estimate *towards* the truth and shrink the
range. Instead the estimates move *away* from the truth
($m_{\text{true}} = 0.12$, $\tau_{\text{true}} = 0.30$ and $6.00$ s) and the
admitted ranges stay narrow — they are narrow around two different wrong
answers.

The zero-noise residuals of the long-window fit settle the matter: $-13.89\%$,
$-5.64\%$, $+4.08\%$, $+10.04\%$, $+8.49\%$, $+0.44\%$, $-8.97\%$ at
$T = 0.25, 0.5, 1, 2, 4, 8, 16$ s. With *no noise at all* the fit is off by up
to $14\%$, and the residual changes sign — the signature of a model that cannot
represent the data (a single relaxation against two). A noise-limited fit
produces residuals that scatter around zero without systematic curvature; this
one does not.

**Implication for reporting.** Every fitted $(m, \tau)$ must be accompanied by
(a) the window set, (b) the model family, and (c) the residual pattern, not only
its rms. A reader who is given a single $(m, \tau)$ pair cannot tell an adequate
model from an inadequate one, and the window-dependence above means they cannot
even reproduce the pair.
