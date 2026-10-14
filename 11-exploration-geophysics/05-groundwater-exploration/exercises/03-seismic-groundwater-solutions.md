# Solutions — 11-05-03 Seismic Refraction and Surface Waves for Aquifers

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [03 Seismic Refraction and Surface Waves for Aquifers](../03-seismic-groundwater.md).

---

## ★1 — Refractor depth

$$ z = \frac{x_c}{2}\sqrt{\frac{v_2-v_1}{v_2+v_1}}
= 20\sqrt{\frac{2000}{4000}} = 20(0.70711) = 14.14\ \mathrm{m}. $$

---

## ★2 — Critical angle, intercept time and the depth check

$$ \theta_c = \arcsin\!\left(\frac{1000}{3000}\right) = 19.47^\circ, \qquad
\cos\theta_c = 0.94281, $$
$$ t_i = \frac{2z\cos\theta_c}{v_1}
= \frac{2(14.142)(0.94281)}{1000} = 0.026667\ \mathrm{s} = 26.67\ \mathrm{ms}, $$
$$ z = \frac{v_1 t_i}{2\cos\theta_c}
= \frac{1000(0.026667)}{2(0.94281)} = 14.14\ \mathrm{m}. $$

**The agreement is algebraic consistency, not independent confirmation**: both
formulas come from the same two-layer model, so a mismatch indicates a mis-pick
or a violation of the model, not a measurement of the error.

---

## ★3 — Sampling depth

$$ \lambda = v_R/f, \qquad z_{\text{sample}} \approx \lambda/3: $$

| $f$ (Hz) | $\lambda$ (m) | $\lambda/3$ (m) | resolves |
|---|---|---|---|
| 5 | 60.0 | 20.0 | trends to ~20 m |
| 15 | 20.0 | 6.67 | layers a few metres thick near 7 m |
| 45 | 6.67 | 2.22 | layers ~2 m thick near 2 m |

The high frequencies resolve thin layers but only *shallow* ones; the low
frequencies reach deep but average over a wide window. Resolution and depth trade
against each other, exactly as in the EM and ERT methods of
[11-05-02](../02-em-and-ert-groundwater.md).

---

## ★4 — Depth error from a velocity error

Using the lesson's table (a $+5\%$ error in $v_1$ gives $-6.1\%$ at contrast
$1.5$ and $-1.9\%$ at contrast $3$), a $+10\%$ error is approximately double:

| $v_2/v_1$ | $z$ at $+10\%$ $v_1$ | error |
|---|---|---|
| 1.5 | $7.85\ \mathrm{m}$ | $-12.3\%$ |
| 3.0 | $13.62\ \mathrm{m}$ | $-3.7\%$ |

The contrast-3 survey is the one to trust: a $10\%$ velocity error costs less
than $4\%$ of the depth, whereas at contrast $1.5$ it costs more than $12\%$ —
larger than the geological question usually allows.

---

## ★5 — Water-table crossover at a modest contrast

$$ \theta_c = \arcsin(1200/1800) = 41.81^\circ, \qquad
\cos\theta_c = 0.74536, $$
$$ x_c = 2(8)\sqrt{\frac{3000}{600}} = 16(2.2361) = 35.78\ \mathrm{m}. $$

It is harder to pick than the ★1 case for two reasons: the head wave is
generated inefficiently when the contrast is small (conversion amplitude falls
with the velocity contrast), and the head wave is **slower** relative to the
direct wave, so it overtakes the direct arrival further out and at a shallower
angle to the travel-time curve — a smaller intercept and a shallower crossover
slope, which a small picking error turns into a large depth error.

---

## ★6 — Frequency needed to resolve a 3 m layer

The sampling window is $\lambda/3$; to keep it no wider than the layer, require
$\lambda/3 \le 3\ \mathrm{m}$, i.e. $\lambda \le 9\ \mathrm{m}$:

$$ f_{\text{resolve}} = \frac{v_R}{\lambda} = \frac{250}{9} = 27.8\ \mathrm{Hz}. $$

To *centre* the window on the layer the rule is $\lambda/3 = 12\ \mathrm{m}$,
i.e. $\lambda = 36\ \mathrm{m}$:

$$ f_{\text{centre}} = \frac{250}{36} = 6.94\ \mathrm{Hz}. $$

Both are reachable with a modest active-source array (a few tens of hertz is
routine), so the layer can in principle be resolved — *provided* the 27.8 Hz
energy is present and the site is not so attenuating or noisy that the
high-frequency branch of the dispersion curve cannot be picked. If it cannot, the
layer is a target for a borehole, not for the surface-wave survey.

---

## ★7 — Combined survey design (specification)

**(a) Water table at ~15 m.** Refraction: source-receiver offsets from 5 m to at
least $4z = 60\ \mathrm{m}$ so that the head wave is well separated from the
direct arrival; receiver spacing 2 m near the crossover to pick it accurately;
shooting in both directions to test for dip. Use the crossover distance formula
with the *measured* saturated/unsaturated velocity contrast; if the contrast is
below about 1.2, report that refraction cannot resolve the water table rather
than reporting a depth.

**(b) Porosity variations 5-25 m.** MASW: a 24-channel array with 2 m spacing
(46 m spread) giving usable dispersion from roughly 5 to 40 Hz; a sledgehammer
source for the high frequencies and a drop weight for the low ones, to cover the
band continuously. Record the fundamental-mode dispersion curve with its
uncertainty, not a single dispersion value per frequency.

**Numerical test for (a).** Invert the MASW curve for $v_s(z)$; predict $v_p(z)$
from Gassmann for the two candidate interpretations — a saturation front and a
lithological boundary — and forward-model the refraction travel times for each.
Compare with the picks. A saturation front predicts a $v_p$ increase with the
$v_s$ essentially flat; a lithological boundary predicts a change in $v_s$ too.
Whichever model reproduces both data sets with residuals inside the picking
error is preferred, and a borehole with a water-level reading settles it.

---

## ★8 — Ignoring an intermediate refractor

The true section: layer 1 ($v_1 = 800\ \mathrm{m\,s^{-1}}$) to $d_1 = 10\
\mathrm{m}$; layer 2 ($v_2 = 1600\ \mathrm{m\,s^{-1}}$) from $10$ to $26\
\mathrm{m}$, so $h = 16\ \mathrm{m}$; basement $v_3 = 2400\
\mathrm{m\,s^{-1}}$ below $26\ \mathrm{m}$.

The basement head wave travels down and up at the critical angles set by Snell's
law across all three media:

$$ \sin\theta_1 = \frac{v_1}{v_3} = \frac{1}{3} \Rightarrow
\theta_1 = 19.47^\circ,\ \cos\theta_1 = 0.94281, $$
$$ \sin\theta_2 = \frac{v_2}{v_3} = \frac{2}{3} \Rightarrow
\theta_2 = 41.81^\circ,\ \cos\theta_2 = 0.74536. $$

The two-way time through the cover is

$$ t_{\text{cover}} = 2\left[\frac{d_1}{v_1\cos\theta_1}
+ \frac{h}{v_2\cos\theta_2}\right]
= 2\left[\frac{10}{754.25} + \frac{16}{1192.58}\right]
= 2[0.013258 + 0.013416] = 0.053348\ \mathrm{s}. $$

A **two-layer** fit attributes this time to a single layer of velocity $v_1$
above the basement, so its apparent depth is

$$ z_{\text{app}} = \frac{t_{\text{cover}}\,v_1\cos\theta_1}{2}
= \frac{0.053348 \times 754.25}{2} = 20.12\ \mathrm{m}. $$

Writing the same relation in closed form, with $d_1 + h = 26\ \mathrm{m}$,

$$ z_{\text{app}} = d_1 + \frac{v_1\cos\theta_1}{v_2\cos\theta_2}\,h
= 10 + 0.6324(16) = 20.12\ \mathrm{m}. $$

**Bias:** $20.1\ \mathrm{m}$ against a true $26\ \mathrm{m}$, i.e. $-5.9\
\mathrm{m}$ ($-23\%$). The intermediate fast layer *hastens* the descent relative
to the two-layer assumption, so the deeper refractor appears too **shallow**.

**How to reveal it.** The travel-time curve should show a $1600\
\mathrm{m\,s^{-1}}$ branch between the two, even if only over a short offset
range; picking it (or using first-arrival refraction tomography with a fine
receiver spacing) resolves the three-layer structure. A two-layer intercept
method cannot, because its assumption — that velocity increases monotonically
with depth and that every refractor is the first arrival over some range — is
exactly what the intermediate layer violates.

---

## Worked mastery checkpoint

**(a) Refractor depth and intercept time** with $v_1 = 700$,
$v_2 = 2100\ \mathrm{m\,s^{-1}}$, $x_c = 31\ \mathrm{m}$:

$$ z = \frac{31}{2}\sqrt{\frac{2100-700}{2100+700}}
= 15.5\sqrt{0.5} = 15.5(0.70711) = 10.96\ \mathrm{m}, $$

$$ \theta_c = \arcsin(1/3) = 19.47^\circ,\quad \cos\theta_c = 0.9428, $$
$$ t_i = \frac{2z\cos\theta_c}{v_1}
= \frac{2(10.96)(0.9428)}{700} = 0.02952\ \mathrm{s} = 29.5\ \mathrm{ms}. $$

**(b) Depth error for a $10\%$ higher $v_1$** (that is $770\
\mathrm{m\,s^{-1}}$), with the crossover unchanged:

$$ z = 15.5\sqrt{\frac{1330}{2870}} = 15.5(0.68074) = 10.55\ \mathrm{m}, $$

an error of $-0.41\ \mathrm{m}$ ($-3.8\%$), consistent with the lesson's
contrast-3 row.

**(c) Sampling depths.** At $10\ \mathrm{Hz}$ with $v_R = 240\
\mathrm{m\,s^{-1}}$: $\lambda = 24\ \mathrm{m}$, $\lambda/3 = 8.0\ \mathrm{m}$.
At $40\ \mathrm{Hz}$ with $v_R = 180\ \mathrm{m\,s^{-1}}$: $\lambda = 4.5\
\mathrm{m}$, $\lambda/3 = 1.5\ \mathrm{m}$. A 3 m layer lying between those
sampling depths occupies most of the 8.0 m window and is well below the 1.5 m
window, so it is **averaged into the low-frequency part and missed by the
high-frequency part**: it is poorly resolved by this pair of frequencies.

**(d) Why the two methods can disagree without either being wrong.** Refraction
measures the $v_p$ increase produced by saturating the pores, so it tracks the
**saturation front**; surface waves measure $v_s$, which responds to the
framework (porosity, cementation, stress) and barely at all to the pore fluid, so
they track the **lithological or porosity boundary**. Where the two differ, the
shallow soil layer that holds the water table and the weathered-to-competent
transition are at different depths, and both measurements are correct measurements
of different things.
