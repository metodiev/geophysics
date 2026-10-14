# Solutions — 06-10-02 Delay-Time (Plus-Minus) Methods and Depth Estimation

**Read after attempting the exercises.** Numbers were computed, not estimated.
Lesson: [02 Delay-Time (Plus-Minus) Methods and Depth Estimation](../02-plus-minus-method.md).
All models are SYNTHETIC.

---

## ★1 — Delay time and depth at x = 80 m

$$d(80) = \tfrac12\left[t_f + t_r - T\right]
= \tfrac12\left[47.10808 + 30.44141 - 69.36492\right]\ \mathrm{ms}
= \tfrac12(8.18457) = 4.092285\ \mathrm{ms}.$$

With $\mathrm{d}z/\mathrm{d}d = v_1/\cos i_c = 619.6773\
\mathrm{m\,s^{-1}}$ (because $v_1/\cos i_c = 600/0.968246$),

$$z(80) = 619.6773 \times 4.092285\times10^{-3} = 2.5359\ \mathrm{m}.$$

Check: $z(80) = 6 + 4\sin(2\pi \cdot 80/120) = 6 + 4\sin(240^\circ)
= 6 - 3.4641 = 2.5359\ \mathrm{m}$. ✔

---

## ★2 — The minus term and the refractor velocity

$$\text{slope} = \frac{33.33333 - (-33.33333)}{100 - 20}\ \frac{\mathrm{ms}}{\mathrm{m}}
= \frac{66.66667}{80} = 0.833333\ \mathrm{ms\,m^{-1}},$$

$$v_2 = \frac{2}{\text{slope}} = \frac{2}{0.833333\times10^{-3}}
= 2400.0\ \mathrm{m\,s^{-1}}.$$

The depths cancel because

$$t_f(x) - t_r(x) = \frac{2x - L}{v_2} + d(0) - d(L),$$

which contains $d$ only at the two *shot points*, both constants. Any error in the
assumed depth profile cancels exactly in the difference, which is why the minus
term is the most robust quantity in the method.

---

## ★3 — Reciprocity misfit

Two independent picks of the same arrival, each with standard deviation
$\sigma$, differ by a quantity with variance $\sigma^{2} + \sigma^{2}$:

$$\sigma_{\text{misfit}} = \sqrt{2}\,\sigma = 1.41421 \times 2 = 2.8284\ \mathrm{ms}.$$

The demonstration measures $-0.0115 \pm 2.8269\ \mathrm{ms}$ at $\sigma = 2\
\mathrm{ms}$ and $-0.0713 \pm 1.4187\ \mathrm{ms}$ at $\sigma = 1\ \mathrm{ms}$
(predicted $1.4142$). The measured standard deviations match to within the
sampling error of 2000 realisations, so the reciprocal misfit *is* a
$\sqrt{2}\sigma$ estimate of the pick scatter.

---

## ★★4 — Depth bias from a velocity error

With the exact sensitivities $\partial\ln h/\partial\ln v_1 = 1.0667$ and
$\partial\ln h/\partial\ln v_2 = -0.0667$ for $v_1/v_2 = 0.25$:

$$\delta h (v_1) = 0.05 \times 1.0667 \times 10\ \mathrm{m} = +0.533\ \mathrm{m},$$
$$\delta h (v_2) = 0.05 \times (-0.0667) \times 10\ \mathrm{m} = -0.033\ \mathrm{m}.$$

**Ratio: $0.533/0.033 = 16.0$.** The depth is sixteen times more sensitive to the
overburden velocity than to the refractor velocity, which is the opposite of most
people's intuition. The reason is that $h = d\,v_1/\cos i_c$ and
$\cos i_c = 0.968$ is close to one: the refractor velocity enters only through the
small correction $\cos i_c$, while the overburden velocity multiplies the delay
directly.

The practical consequence: measure $v_2$ from the minus term and *know* $v_1$ from
somewhere else (a borehole, a short-offset direct-wave fit). Spending the survey
budget on a longer line to improve $v_2$ buys almost nothing.

---

## ★★5 — Depth standard deviation for σ = 3 ms

$$\sigma_d = \sqrt{0.625}\,\sigma = 0.790569 \times 3\ \mathrm{ms}
= 2.3717\ \mathrm{ms},$$
$$\sigma_z = 619.6773 \times 2.3717\times10^{-3} = 1.4697\ \mathrm{m}.$$

The demonstration's table extends this to $\sigma = 5\ \mathrm{ms}$ and obtains an
RMS depth error of $2.4103\ \mathrm{m}$ against the analytic $2.4495\ \mathrm{m}$;
the ratio falls below one because the *velocity* errors, which the Monte Carlo also
includes, become important at large $\sigma$ and are correlated between receivers.

---

## ★★6 — Reading the error ellipse

The two intervals are the **projections** of the $95\%$ error ellipse onto the two
parameter axes: $v_1 = 600.0 \pm 34.68\ \mathrm{m\,s^{-1}}$ and
$h = 10.00 \pm 0.665\ \mathrm{m}$.

The ellipse has semi-axes $0.641$ and $3.402$ in units of
$\sigma_{v_1} = 17.162\ \mathrm{m\,s^{-1}}$ and $\sigma_h = 0.3311\ \mathrm{m}$,
and its major axis lies at $+45^\circ$ from the $v_1$ axis. Its area is
$\pi \times 0.641 \times 3.402\ \sigma_{v_1}\sigma_h \approx 6.9\,
\sigma_{v_1}\sigma_h$, whereas the rectangle representing two independent $95\%$
intervals would have area $(2\times1.96)^{2}\sigma_{v_1}\sigma_h = 15.4\,
\sigma_{v_1}\sigma_h$: **more than twice as large.**

So the rectangle is a faithful tabulation of the marginals and a false description of
the joint uncertainty. With $\mathrm{corr}(v_1,h) = 0.932$, the physically
allowed combinations run along a thin ridge in which a larger $v_1$ pairs with a
larger $h$; the corners of the rectangle — high velocity with shallow depth, low
velocity with deep depth — are excluded by the data. Quoting the pair of intervals
without the correlation invites the reader to explore those corners.

---

## ★★★7 — How many picks for ±0.10 m?

**Intercept-only requirement.** For the flat demonstration model, $\mathrm{d}h/\mathrm{d}t_i
= v_1v_2/(2\sqrt{v_2^{2}-v_1^{2}}) = 309.8387\ \mathrm{m\,s^{-1}}$, so the
requirement is

$$\sigma_{t_i} \le \frac{0.10}{309.8387} = 3.2275\times10^{-4}\ \mathrm{s}
= 0.3227\ \mathrm{ms}$$

with $\sigma_t = 1\ \mathrm{ms}$. For $N$ equally spaced far-branch picks between
$x_c = 25.8199\ \mathrm{m}$ and $3x_c = 77.46\ \mathrm{m}$,
$\bar{x} = 51.64\ \mathrm{m}$ and $S_{xx} = N W^{2}/12 = 222.2\,N$, so

$$\sigma_{t_i} = \sigma_t\sqrt{\frac{1}{N} + \frac{\bar{x}^{2}}{S_{xx}}}
= \sigma_t\sqrt{\frac{1}{N} + \frac{12}{N}}
= \sigma_t\sqrt{\frac{13}{N}}.$$

Setting $\sqrt{13/N} \le 0.3227$ gives $N \ge 124.9$, i.e. **$N = 125$ picks**
(about $0.42\ \mathrm{m}$ spacing over the $51.6\ \mathrm{m}$ far branch).

Lengthening the line to $6x_c = 154.9\ \mathrm{m}$ improves the geometry term:
$\bar{x} = 3.5x_c$ and $S_{xx} = 25Nx_c^{2}/12$, so
$\sigma_{t_i} = \sigma_t\sqrt{1/N + 5.88/N} = \sigma_t\sqrt{6.88/N}$ and the same
requirement gives $N \ge 66$ picks — 66 receivers over $129\ \mathrm{m}$ rather
than 125 over $52\ \mathrm{m}$, the same $0.42\ \mathrm{m}$ spacing either way.
The cost of the extra cable is real and the benefit is a factor of $1.9$ in the
pick count.

**But ±0.10 m is not achievable with 1 ms picks.** The full least-squares
covariance of $(v_1, v_2, t_i)$, which is what the demonstration evaluates, gives
$\sigma_h = 0.3311\ \mathrm{m}$ at $\sigma = 1\ \mathrm{ms}$ — three times the
intercept-only term, because the *velocity* uncertainties also propagate into the
depth and those do not shrink when picks are added. Since $\sigma_h$ is linear in
$\sigma_t$, the requirement is met when

$$\sigma_t \le 1\ \mathrm{ms} \times \frac{0.10}{0.3311} = 0.302\ \mathrm{ms}.$$

**Answer.** ~125 far-branch picks over a ~52 m baseline, and the pick standard
deviation reduced to about $0.3\ \mathrm{ms}$ by stacking or a stronger source.
Adding picks alone cannot reach $\pm 0.10\ \mathrm{m}$: the budget is
velocity-limited, not pick-limited. This is the same lesson as Section 6.2 of the
lesson — the depth and the velocity are $93\%$ correlated, so a study that wants a
precise depth must also want a precise $v_1$.

---

## ★★★8 — Forgetting the reciprocal time

Using $\tfrac12(t_f + t_r)$ instead of $\tfrac12(t_f + t_r - T)$ adds $T/2$ to every
delay time, and therefore to every depth, since $z = (v_1/\cos i_c)\,d$.

At $x = 60\ \mathrm{m}$ of the undulating model, $t_f = t_r = 44.36492\ \mathrm{ms}$
and $T = 69.36492\ \mathrm{ms}$, so

$$d_{\text{true}}(60) = \tfrac12(88.72984 - 69.36492) = 9.68246\ \mathrm{ms}
\;\Rightarrow\; z = 6.000\ \mathrm{m},$$
$$d_{\text{wrong}}(60) = \tfrac12(88.72984) = 44.36492\ \mathrm{ms}
\;\Rightarrow\; z = 27.49\ \mathrm{m}.$$

The bias is $T/2 \times 619.6773 = 34.68246\times10^{-3} \times 619.6773
= 21.49\ \mathrm{m}$: the reported refractor would sit at $27.5\ \mathrm{m}$ where
the truth is $6.0\ \mathrm{m}$.

**Diagnostic, without knowing the answer.** Two checks catch it:

1. **Internal consistency with the far-branch intercept.** The same picks,
   inverted as a two-layer model from the intercept time alone, give a depth of
   order $10\ \mathrm{m}$ for this spread. A plus-term profile claiming $27.5\
   \mathrm{m}$ disagrees with the line's own two-layer answer by a factor of
   $2.7$, and both cannot be right.
2. **Reciprocity gives $T$ twice.** $T$ must equal $t_f(L)$ *and* $t_r(0)$, two
   different picks that must agree to within the pick scatter (Section 5 of the
   lesson). If they disagree by something comparable to $T/2$ rather than by
   $0.7\ \mathrm{ms}$, the wrong pick has been used as the reciprocal time — for
   example a receiver one spacing short of the shot. The misfit reports it without
   any knowledge of the answer.
