# Solutions — 10-02-04 3-D GPR Imaging and Time Slices

> Read after attempting. Lesson: [04 3-D Imaging](../04-gpr-3d-imaging.md).

---

## ★1 — Cube geometry

Lines: $\lceil 4/0.20\rceil+1 = 21$. Traces per line:
$\lceil 6/0.05\rceil+1 = 121$. Total traces: $21\times121 = 2541$.

Samples per trace: $2000$. Volume:
$2541\times2000\times2 = 10\,164\,000$ bytes $= 10.2\ \mathrm{MB}$.

---

## ★2 — Time-slice shift rate

$$\frac{\mathrm{d}y}{\mathrm{d}t} = \frac{v}{2\sin\theta}
= \frac{0.075}{2\times0.5000} = 0.075\ \mathrm{m\,ns^{-1}}.$$

So the band moves $0.075\ \mathrm{m}$ per nanosecond — exactly $v/2$ at
$30^\circ$ and *less* than $v/2$ for steeper dips.

---

## ★3 — Maximum unaliased dip

$$\sin\theta_{\max} = \frac{\lambda}{4\Delta y}
= \frac{0.4328}{1.20} = 0.3607 \;\Rightarrow\; \theta_{\max} = 21.15^\circ.$$

A $30^\circ$ dip would alias at this spacing.

---

## ★★4 — Dip from the shift rate

$\mathrm{d}y/\mathrm{d}t = 0.30/2.0 = 0.15\ \mathrm{m\,ns^{-1}}$.

$$\sin\theta = \frac{v}{2\,\mathrm{d}y/\mathrm{d}t}
= \frac{0.09993}{0.30} = 0.3331 \;\Rightarrow\; \theta = 19.46^\circ.$$

Check the plausibility rule of the lesson: the shift rate must be at least
$v/2 = 0.04997\ \mathrm{m\,ns^{-1}}$; $0.15$ satisfies it.

---

## ★★5 — Velocity error on a dipping interface

Recovered dip: $\sin\theta' = 1.08\times\sin15^\circ = 1.08\times0.2588 = 0.2795$,
so $\theta' = 16.23^\circ$ (apparent in the depth-converted section, since the
depth conversion scales the slope by the velocity ratio).

Lateral position: at $2.0\ \mathrm{m}$ depth,
$y_{\text{true}} = (2.0-1.0)/\sin15^\circ = 3.864\ \mathrm{m}$;
with the wrong velocity, $y = (2.0/1.08 - 1.0)/\sin15^\circ = (1.852-1.0)/0.2588 =
3.291\ \mathrm{m}$: an error of $-0.573\ \mathrm{m}$, i.e. about $15\%$ of the
position. A dip error and a velocity error are the same observation.

---

## ★★6 — Reported position

Report $(1.50, 2.00)\ \mathrm{m}$ with an uncertainty of at least $\pm$ one grid
step ($\pm0.10\ \mathrm{m}$) in each direction, plus any positioning error of the
lines themselves. A maximum of a slice on a decimetre grid does not determine a
centimetre position: the slice's localisation precision *is* the grid step, and a
finer statement is fabricated precision unless the anomaly was found by
interpolation of a smooth, well-sampled peak — which should then be stated.

---

## ★★★7 — Mixed wavelength and aliasing

Zone A, $\lambda = 0.30\ \mathrm{m}$:
$\lambda/(2\Delta y) = 0.30/0.80 = 0.375$; the allowed band is
$|\sin\theta_{\text{app}}| \le \lambda/(4\Delta y) = 0.1875$.
$\sin25^\circ = 0.4226$ exceeds it, so wrapping with $m=1$:
$\sin\theta_{\text{app}} = 0.4226-0.375 = 0.0476$, i.e.
$\theta_{\text{app}} = 2.73^\circ$.

Zone B, $\lambda = 0.60\ \mathrm{m}$:
$\lambda/(2\Delta y) = 0.75$, so with $m=1$:
$\sin\theta_{\text{app}} = 0.4226-0.75 = -0.3274$, i.e.
$\theta_{\text{app}} = -19.11^\circ$.

Interpretive consequence: the same geological plane appears as two gently to
steeply *oppositely* dipping panels across the moisture boundary, with a
discontinuity at the change. This is a classic false structure: it looks like a
fault or a fold, and it is an artefact of the wavelength changing within a fixed
grid. The remedy is to design the spacing for the shortest in-situ wavelength
(wet ground), not the dry one.

---

## ★★★8 — Can the cube resolve two targets $0.3\ \mathrm{m}$ apart?

Along the line the spacing is $0.05\ \mathrm{m} = \lambda/10$ for
$\lambda = 0.5\ \mathrm{m}$, so along-line sampling is not the limit: the limit is
the migrated point-spread width, measured at $0.300\ \mathrm{m}$ laterally
($0.600\lambda$) with a $\pm2\ \mathrm{m}$ aperture at $1.20\ \mathrm{m}$ depth.
Two targets $0.3\ \mathrm{m}$ apart are therefore *just at* the measured
resolution limit, and would be marginal or merged depending on their strength
ratio and depth.

Between lines the spacing is $0.25\ \mathrm{m}$; the between-line resolution is
then the line spacing itself ($0.25\ \mathrm{m}$), which is comparable with the
$0.3\ \mathrm{m}$ separation — so in the $y$ direction the two targets are
marginally resolvable at best.

Test: migrate the cube and measure the envelope width of the image of a single
known target at that depth (the point-spread function); if its width is
$\ge0.3\ \mathrm{m}$ the claim fails. That is exactly the measurement made in the
lesson and in [10-01-05 §4](../../01-gpr-principles/05-gpr-resolution.md).
