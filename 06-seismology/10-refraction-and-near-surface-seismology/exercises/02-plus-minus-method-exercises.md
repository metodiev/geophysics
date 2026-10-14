# Exercises — 06-10-02 Delay-Time (Plus-Minus) Methods and Depth Estimation

**All values are SYNTHETIC.** Attempt these before reading the
[solutions](./02-plus-minus-method-solutions.md). The lesson is
[02 Delay-Time (Plus-Minus) Methods and Depth Estimation](../02-plus-minus-method.md).
The demonstration model is $v_1 = 600\ \mathrm{m\,s^{-1}}$,
$v_2 = 2400\ \mathrm{m\,s^{-1}}$, $L = 120\ \mathrm{m}$,
$z(x) = 6 + 4\sin(2\pi x/120)\ \mathrm{m}$.

## ★ Foundational

**★1.** For the receiver at $x = 80\ \mathrm{m}$, $t_f = 47.10808\ \mathrm{ms}$,
$t_r = 30.44141\ \mathrm{ms}$ and the reciprocal time
$T = 69.36492\ \mathrm{ms}$. Compute the delay time and the depth. Compare with
$z(80) = 6 + 4\sin(2\pi\cdot80/120)$.

**★2.** The minus term is $-33.33333\ \mathrm{ms}$ at $x = 20\ \mathrm{m}$ and
$+33.33333\ \mathrm{ms}$ at $x = 100\ \mathrm{m}$. Compute its slope, the
refractor velocity, and state why the depths cancelled.

**★3.** The exact model satisfies reciprocity identically. Two independent picks
of the same arrival have a standard deviation of $2\ \mathrm{ms}$; what is the
predicted standard deviation of their difference, and what does the demonstration
measure?

## ★★ Applied

**★★4.** For the demonstration model, the logarithmic sensitivity of the depth to
the overburden velocity is $+1.0667$. Compute the depth bias at $h = 10\
\mathrm{m}$ produced by a $5\%$ error in $v_1$, and the bias produced by a $5\%$
error in $v_2$ (sensitivity $-0.0667$). State the ratio.

**★★5.** The delay time has $\sigma_d^{2} = 0.625\sigma^{2}$ because the
reciprocal time is itself the mean of two picks. For $\sigma = 3\ \mathrm{ms}$,
compute $\sigma_d$ and the depth standard deviation using
$\mathrm{d}z/\mathrm{d}d = 619.6773\ \mathrm{m\,s^{-1}}$.

**★★6.** The $95\%$ error ellipse of the flat-model fit at $\sigma = 1\
\mathrm{ms}$ has semi-axes $0.641$ and $3.402$ in units of $\sigma_{v_1}$ and
$\sigma_h$, with its major axis at $+45^\circ$ from the $v_1$ axis; the quoted
$95\%$ values are $v_1 = 600.0 \pm 34.68\ \mathrm{m\,s^{-1}}$ and
$h = 10.00 \pm 0.665\ \mathrm{m}$. Explain what those two intervals describe and
why the rectangle they form is not the $95\%$ region.

## ★★★ Research-oriented

**★★★7.** A study must deliver a depth accurate to $\pm 0.10\ \mathrm{m}$ from
$1\ \mathrm{ms}$ picks at the demonstration's site ($v_1 = 988.4$,
$v_2 = 3500\ \mathrm{m\,s^{-1}}$ for the bedrock refractor at $18\ \mathrm{m}$ —
or use the lesson-02 model's $515.191\ \mathrm{m\,s^{-1}}$ $h$–$t_i$ factor).
How many far-branch picks are needed, over what baseline, and is the requirement
achievable at all? Show the arithmetic.

**★★★8.** Show what happens if the analyst forgets to subtract the reciprocal
time and uses $\tfrac12(t_f + t_r)$ as the delay time. Compute the resulting depth
error for the demonstration model at $x = 60\ \mathrm{m}$, and state the diagnostic
that would reveal the mistake without any knowledge of the true answer.
