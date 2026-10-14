# Solutions — 10-02-05 GPR Modelling and Full-Waveform Inversion

> Read after attempting. Lesson:
> [05 Modelling and Inversion](../05-gpr-modelling-and-inversion.md).

---

## ★1 — CFL condition

$$\Delta t \le \frac{h}{v_{\max}\sqrt{2}}
= \frac{0.015}{0.11\times1.41421} = 0.0964\ \mathrm{ns}.$$

$\Delta t = 0.045\ \mathrm{ns}$ is $47\%$ of the limit: **stable**.

---

## ★2 — Convolutional model

$$d(t) = 0.2\,w\!\left(t - \frac{2\times1.0}{0.1}\right)
- 0.15\,w\!\left(t - \frac{2\times2.5}{0.1}\right),$$

with two-way times $20.0\ \mathrm{ns}$ and $50.0\ \mathrm{ns}$. Note the sign of
the second coefficient: a reflection from a decrease in permittivity is
opposite-polarity to one from an increase, and the convolutional model retains
that polarity.

---

## ★3 — Misfit reduction in dB

$$10\log_{10}\left(\frac{7.4751}{9.8166}\right)
= 10\log_{10}(0.7615) = -1.18\ \mathrm{dB},$$

the four-iteration figure of the lesson's table.

---

## ★★4 — Grid convergence

If the error scales as $h^{1.6}$, halving $h$ multiplies it by
$2^{-1.6} = 0.3299$: from $0.25\ \mathrm{ns}$ to $0.082\ \mathrm{ns}$.

Test: run the same model at three (or more) grid spacings with the source and
geometry unchanged, pick the same event by the same criterion (envelope maximum
within a fixed window), and fit $\log(\text{error})$ against $\log h$. The
observed demonstration values ($+0.884$, $+0.334$, $+0.209\ \mathrm{ns}$ at
$h = 0.040$, $0.020$, $0.010\ \mathrm{m}$) give successive ratios $0.378$ and
$0.626$, i.e. apparent orders $1.40$ and $0.68$: the trend is *not* a clean power
law at these resolutions, which is itself information — the pick, the source
discretisation and the reflection coefficient at a sampled interface all
contribute. Report the three numbers, not a single order.

---

## ★★5 — The adjoint equation

For the recursion
$u^{m}_{i,j} = 2u^{m-1}_{i,j} - u^{m-2}_{i,j} + a_{i,j}(Lu^{m-1})_{i,j} + s^{m}_{i,j}$
with $a = (v\Delta t/h)^{2}$, the transpose system $M^{T}\lambda = R^{T}r$ reads

$$\lambda^{m-1}_{i,j} = 2\lambda^{m}_{i,j} - \lambda^{m+1}_{i,j}
+ a_{i,j}\left(L\lambda^{m}\right)_{i,j} + r^{m-1}_{i,j},$$

i.e. the same recursion with the time index running backwards, the residual
injected at the receivers, and the terminal conditions
$\lambda^{N} = \lambda^{N+1} = 0$.

Why backwards: the forward operator is a two-step (in time) recurrence whose
spatial part is self-adjoint, so its transpose reverses the time order and
re-uses the same Laplacian. That is why the adjoint costs one extra simulation
regardless of how many model parameters there are — the property that makes FWI
computationally possible at all.

---

## ★★6 — Cycle skipping

Period $T = 1/f_0 = 5.00\ \mathrm{ns}$; the modelled error is $8\ \mathrm{ns} =
1.60\,T$, which is beyond the first spurious minimum measured at
$0.91\,T = 4.55\ \mathrm{ns}$.

Verdict: cycle skipping is a **serious risk**. The misfit at that shift is
already in the neighbouring basin, and the gradient can push the model further
away. Remedies: obtain a better starting model (a CMP sounding, a wide-offset
sounding or a refraction-style estimate), invert a low-pass-filtered version of
the data first, or use a misfit that is less phase-sensitive (but then state what
it measures).

---

## ★★★7 — A verification suite

| test | quantity measured | pass criterion |
|---|---|---|
| CFL / stability | field growth over long runs | no growth for $\Delta t \le h/(v_{\max}\sqrt{2})$ |
| analytic travel time | modelled minus analytic reflection time | error falls with $h$ and is under one time sample at the production grid |
| grid convergence | error versus $h$ at three spacings | monotone decrease; residual under the stated tolerance |
| adjoint gradient | adjoint gradient versus finite differences | agreement to the finite-difference accuracy (demonstration: $5.5\times10^{-4}$ maximum, $7.4\times10^{-6}$ median) |
| reciprocity | trace at (source A, receiver B) versus (B, A) | identical to machine precision |

Two more that are worth adding for a GPR code specifically: a homogeneous-medium
test (no reflections beyond the boundary reflection, whose arrival time is
predicted from the geometry) and a half-space reflection-coefficient test
(amplitude ratio against the analytic normal-incidence value).

---

## ★★★8 — Reporting four noisy runs

Values at the fixed location: $0.1010$, $0.0999$, $0.0972$, $0.1009\
\mathrm{m\,ns^{-1}}$ on a background of $0.1000$.

Mean $= (0.1010+0.0999+0.0972+0.1009)/4 = 0.09975\ \mathrm{m\,ns^{-1}}$.

Standard deviation (sample, $N-1 = 3$): deviations from the mean are
$+0.00125$, $+0.00015$, $-0.00255$, $+0.00115$; squares $1.5625\times10^{-6}$,
$2.25\times10^{-8}$, $6.5025\times10^{-6}$, $1.3225\times10^{-6}$, sum
$9.41\times10^{-6}$, variance $3.137\times10^{-6}$, so
$\sigma = 0.00177\ \mathrm{m\,ns^{-1}}$ — about $4.4\%$ of the true contrast
($0.040\ \mathrm{m\,ns^{-1}}$), consistent with the demonstration's quoted spread
of $0.0014\ \mathrm{m\,ns^{-1}}$ between the extremes ($3\%$ of the contrast).

Report: the mean value at a **named location**, its standard deviation over runs
that differ in noise realisation *and* starting model, the misfit reduction, and
the statement that one gradient iteration recovers a few per cent of the true
contrast. Never report a single run's global maximum as "the anomaly".
