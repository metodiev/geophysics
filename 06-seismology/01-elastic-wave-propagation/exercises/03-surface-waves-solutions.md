# Solutions — 06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [03 Surface Waves](../03-surface-waves.md).

---

## ★1 — The trapping interval and $q$

A Love mode is trapped when the energy turns around in the layer and decays in
the half space, which requires

$$\beta_1 < c < \beta_2 \qquad\Longrightarrow\qquad
3.500 < c < 4.500\ \mathrm{km\,s^{-1}}.$$

The vertical slowness available in the layer is

$$q = \sqrt{\frac{1}{\beta_1^2} - \frac{1}{\beta_2^2}}
= \sqrt{0.0816327 - 0.0493827}
= \sqrt{0.0322500} = 0.179583\ \mathrm{s\,km^{-1}}.$$

The unit is $\mathrm{s\,km^{-1}}$: a reciprocal velocity, which is what a
vertical slowness must be. The demonstration states the same interval and uses
$q$ inside the mode-count formula.

---

## ★2 — Mode counting

At $T = 10\ \mathrm{s}$: $\omega = 2\pi/10 = 0.628319\ \mathrm{rad\,s^{-1}}$,

$$\frac{\omega H q}{\pi} = \frac{0.628319 \times 30 \times 0.179583}{\pi}
= \frac{3.385563}{3.141593} = 1.0777
\;\Longrightarrow\; 1 + \lfloor 1.0777\rfloor = 2 .$$

At $T = 5\ \mathrm{s}$: $\omega = 1.256637\ \mathrm{rad\,s^{-1}}$,
$\omega Hq/\pi = 2.1554$, so $1 + 2 = 3$ modes.

Both match the demonstration's `modes found` column (2 at 10 s, 3 at 5 s) and its
closed form $1 + \lfloor\omega Hq/\pi\rfloor$.

---

## ★3 — Direction of the fundamental's dispersion

As the period shortens, the mode is confined closer to the surface and therefore
samples more of the *slower* layer, so $c$ **decreases** toward $\beta_1$. The
demonstration reports $c(2\ \mathrm{s}) = 3.5056\ \mathrm{km\,s^{-1}}$ and
$c(200\ \mathrm{s}) = 4.4897\ \mathrm{km\,s^{-1}}$, whose limits are
$\beta_1 = 3.5000$ and $\beta_2 = 4.5000\ \mathrm{km\,s^{-1}}$. The fundamental
stays strictly inside the trapping interval, as it must: neither limit is reached
exactly at any finite period.

---

## ★4 — Group velocity by finite difference

Using the printed rows $c(40\ \mathrm{s}) = 4.2519$ and
$c(20\ \mathrm{s}) = 3.8666$ to estimate derivatives over that interval:

$$\frac{\mathrm{d}c}{\mathrm{d}T}
\approx \frac{3.8666 - 4.2519}{20 - 40} = 0.019265\ \mathrm{km\,s^{-1}\,s^{-1}},$$

$$k(40) = \frac{2\pi/40}{4.2519} = 0.036943\ \mathrm{km^{-1}},
\qquad k(20) = \frac{2\pi/20}{3.8666} = 0.081249\ \mathrm{km^{-1}},$$

$$\frac{\mathrm{d}k}{\mathrm{d}T} = \frac{0.081249 - 0.036943}{20 - 40}
= -2.2153\times10^{-3}\ \mathrm{km^{-1}\,s^{-1}},$$

$$\frac{\mathrm{d}c}{\mathrm{d}k}
= \frac{0.019265}{-2.2153\times10^{-3}} = -8.6963\ \mathrm{km^2\,s^{-1}},$$

$$U = c + k\frac{\mathrm{d}c}{\mathrm{d}k} = 4.2519 - 0.3213
= 3.9306\ \mathrm{km\,s^{-1}}.$$

The demonstration's value is $U = 3.8496\ \mathrm{km\,s^{-1}}$, so the two-point
difference over a 20 s interval overshoots by about $0.081\ \mathrm{km\,s^{-1}}$
(2.1%). The point of the exercise is the direction: $U < c$ here, and
$c - U > 0$, which is the **normal-dispersion** signature of a layer over a faster
half space.

---

## ★5 — The size of the $c - U$ difference

$$\frac{0.4023}{4.2519} = 9.46\%.$$

The difference is largest at intermediate periods because that is where the
sensitivity kernel changes most rapidly with depth. At very long periods the mode
samples the fast half space and both $c$ and $U$ approach $\beta_2$ with a small
and slowly varying difference; at very short periods the mode is entirely inside
the layer and both approach $\beta_1$, again with a small difference. The
transition between the two regimes is where $\mathrm{d}c/\mathrm{d}\omega$ is
largest, and $U = c/(1-(\omega/c)\mathrm{d}c/\mathrm{d}\omega)$ amplifies that
derivative.

---

## ★6 — Rayleigh versus Love speeds

$$c_R = 0.91940169\,\beta = 0.91940169 \times 3.5 = 3.217906\
\mathrm{km\,s^{-1}}.$$

The Love fundamental at $T = 5\ \mathrm{s}$ is $3.5327\ \mathrm{km\,s^{-1}}$,
which is *larger*. The comparison is not like-for-like: $c_R$ depends only on the
half-space (or layer) shear speed and Poisson ratio, while the Love value depends
on period and on the layer thickness. To make the comparison meaningful the
Rayleigh speed must be computed for the **same material and the same regime** —
here the layer's $\beta_1 = 3.5\ \mathrm{km\,s^{-1}}$ — and one must state that the
Rayleigh wave is non-dispersive only in a half space, whereas in a layered medium
it disperses like the Love wave.

---

## ★★★7 — Minimum contrast for a trapped mode (specification)

**Procedure.** Fix $\beta_1 = 3.500\ \mathrm{km\,s^{-1}}$, $H = 30\ \mathrm{km}$,
$T = 20\ \mathrm{s}$. Sweep $\beta_2 \in (3.500, 3.700]\ \mathrm{km\,s^{-1}}$ on a
log-spaced grid of at least 200 values. For each, evaluate the Love dispersion
function and detect a sign change on $(\beta_1,\beta_2)$; record the smallest
$\beta_2$ with a sign change.

**Tolerance.** A sign change on a grid is not a root: require additionally that
the secular function be resolvable to $10^{-10}$ relative in double precision and
that a bisection refine the root to $10^{-8}\ \mathrm{km\,s^{-1}}$ in $\beta_2$,
then print the bracketing interval rather than a single value.

**Prediction.** The threshold is **smooth**, not sharp in the contrast, but its
effect is sharp in period: the mode count is
$1 + \lfloor\omega Hq/\pi\rfloor$, and for the fundamental to exist at $T$ one
needs only $q > 0$, i.e. $\beta_2 > \beta_1$, with no smaller threshold. What does
change rapidly is the mode counting: as the contrast shrinks, $q \to 0$ and
$\omega Hq/\pi \to 0$, so the fundamental exists but becomes almost entirely
confined to the half space ($c \to \beta_1^+$) and carries little layer
information. The honest measured quantity is therefore not "existence" but the
contrast at which the mode's layer sensitivity falls below a stated level.

---

## ★★★8 — The two group-velocity forms (worked derivation)

Start from $U = \mathrm{d}\omega/\mathrm{d}k$ and write $k = \omega/c$:

$$\frac{\mathrm{d}k}{\mathrm{d}\omega}
= \frac{1}{c} - \frac{\omega}{c^2}\frac{\mathrm{d}c}{\mathrm{d}\omega}
= \frac{1}{c}\left[1 - \frac{\omega}{c}\frac{\mathrm{d}c}{\mathrm{d}\omega}\right]
\;\Longrightarrow\;
U = \frac{\mathrm{d}\omega}{\mathrm{d}k}
= c\left[1 - \frac{\omega}{c}\frac{\mathrm{d}c}{\mathrm{d}\omega}\right]^{-1}.$$

Also, with $\omega = ck$,

$$U = \frac{\mathrm{d}\omega}{\mathrm{d}k}
= c + k\frac{\mathrm{d}c}{\mathrm{d}k}.$$

These are the same equation rearranged, so any difference between a numerical
evaluation of one and of the other is **finite-difference error**. That is why
the demonstration's $1.52\times10^{-9}$ relative agreement is a check on the
derivative implementation and on the internal consistency of the dispersion
solver — not evidence that the physics is right. A physically meaningful check
would compare $c(T)$ with an independently computed seismogram's envelope peak
time, which is what a real surface-wave study does.

---

## ★★★9 — When does the fundamental sample the layer?

**Reasoning.** The displacement of a trapped mode decays as
$\exp(-\gamma_2 z)$ in the half space with
$\gamma_2 = \sqrt{k^2 - \omega^2/\beta_2^2}$, and varies as $\sin(\nu_1 z)$ in the
layer with $\nu_1 = \sqrt{\omega^2/\beta_1^2 - k^2}$. More than half the energy in
the layer requires $\nu_1 H$ to be of order $\pi/2$, i.e. the fundamental's first
turning point to fall outside the layer.

With the demonstration's numbers, $q = 0.179583\ \mathrm{s\,km^{-1}}$ and
$\nu_1 H = \omega H q$ for a mode near the layer speed. Setting
$\omega H q = \pi/2$ gives $\omega = 1.5708/(30 \times 0.179583) = 0.29156\
\mathrm{rad\,s^{-1}}$, i.e. $T = 2\pi/\omega = 21.5\ \mathrm{s}$.

So for this model the transition from "samples mostly the half space" to "samples
mostly the layer" happens near $T \approx 20\ \mathrm{s}$, which is consistent with
the mode-count change at $T = 10\ \mathrm{s}$ and with the fundamental's value
$c(20\ \mathrm{s}) = 3.8666\ \mathrm{km\,s^{-1}}$ sitting well below $\beta_2$.

**What would make it quantitative.** A mode-count argument is a statement about
eigenvalues, not about energy. The quantitative answer requires the depth
sensitivity kernel $\partial c/\partial\beta(z)$ from a variational or
normal-mode calculation, integrated over the layer; the fraction of energy in the
layer is then that integral normalised by the total. Without the kernel, the
statement above is an estimate of the *period threshold*, not a measurement of the
energy partition.
