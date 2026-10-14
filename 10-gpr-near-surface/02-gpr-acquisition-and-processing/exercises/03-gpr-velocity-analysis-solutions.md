# Solutions — 10-02-03 Velocity Analysis and CMP Sounding

> Read after attempting. Lesson:
> [03 Velocity Analysis](../03-gpr-velocity-analysis.md).

---

## ★1 — Semblance values

Identical traces: the numerator is $\sum_\tau (2y)^2 = 4\sum y^2$ and the
denominator is $N\sum_\tau (y^2+y^2) = 2\times2\sum y^2 = 4\sum y^2$, so
$S = 1$.

Negative of each other ($y_2 = -y_1$): the numerator is
$\sum_\tau (y_1-y_1)^2 = 0$, so $S = 0$. Semblance measures *similarity*, not
amplitude, and inverts polarity.

---

## ★2 — Velocity from moveout

$$v = \frac{x}{\sqrt{t^{2}-t_0^{2}}}
= \frac{3.0}{\sqrt{58.0^{2}-50.0^{2}}}
= \frac{3.0}{\sqrt{3364-2500}} = \frac{3.0}{29.39}
= 0.1021\ \mathrm{m\,ns^{-1}}.$$

---

## ★3 — Ray parameter

$p = 1/v = 1/0.075 = 13.33\ \mathrm{ns\,m^{-1}}$.

The unit follows from the GPR time unit: with $v$ in $\mathrm{m\,ns^{-1}}$, $p$ is
in $\mathrm{ns\,m^{-1}}$, not $\mathrm{s\,m^{-1}}$ (a factor $10^{9}$ apart).

---

## ★★4 — Analytic versus measured velocity resolution

$t = \sqrt{66.7^{2} + 4.0^{2}/0.0740^{2}} = \sqrt{4448.9 + 2921.8}
= 85.99\ \mathrm{ns}$.

$$\delta v = \frac{v^{3}t\,\delta t}{x^{2}}
= \frac{4.053\times10^{-4}\times85.99\times0.25}{16}
= 5.45\times10^{-4}\ \mathrm{m\,ns^{-1}} = 0.74\%.$$

The measured $0.9$-of-peak width is $0.0020\ \mathrm{m\,ns^{-1}}$ ($2.70\%$),
about $3.7\times$ larger. The excess is not noise (the data have only $0.02$ rms
noise): it is **model error**, because the two-layer moveout is not exactly
hyperbolic and the residual after NMO reaches $0.675\ \mathrm{ns}$ at the far
offset. Report both: the analytic value as the noise-limited precision, and the
semblance width as the model-limited resolution.

---

## ★★5 — Short aperture

At $x_{\max} = 1.0\ \mathrm{m}$, $t = \sqrt{4448.9+182.6} = 68.06\ \mathrm{ns}$:

$$\delta v = \frac{4.053\times10^{-4}\times68.06\times0.25}{1.0}
= 6.90\times10^{-3}\ \mathrm{m\,ns^{-1}} = 9.3\%.$$

Compare the demonstration's measured width at $0.8\ \mathrm{m}$ maximum offset:
$0.0750\ \mathrm{m\,ns^{-1}}$, larger than the entire plausible velocity range of
the medium. The design consequence: a monostatic (zero-offset) profile cannot
measure a velocity at all, and a CMP sounding (or a calibration target at known
depth) is the only way to make an absolute depth measurement.

---

## ★★6 — Dix inversion and its sensitivity

$$v_2 = \sqrt{\frac{0.0740^{2}\times67.3 - 0.0600^{2}\times40.0}{27.3}}
= \sqrt{\frac{0.3686-0.1440}{27.3}} = \sqrt{8.227\times10^{-3}}
= 0.0907\ \mathrm{m\,ns^{-1}}.$$

Perturbations of $+5\%$:

- $v_{\text{nmo},2} \to 0.0777$: numerator $0.4064-0.1440 = 0.2624$,
  $v_2 = \sqrt{9.612\times10^{-3}} = 0.0980$ ($+8.09\%$);
- $v_{\text{nmo},1} \to 0.0630$: numerator $0.3686-0.1588 = 0.2098$,
  $v_2 = 0.0877$ ($-3.35\%$);
- $t_{0,2} \to 70.7$ and denominator $30.7$:
  $v_2 = \sqrt{(0.3867-0.1440)/30.7} = 0.0889$ ($-1.97\%$);
- $t_{0,1} \to 42.0$ and denominator $25.3$:
  $v_2 = \sqrt{(0.3686-0.1512)/25.3} = 0.0927$ ($+2.20\%$).

The deeper event's NMO velocity dominates: the interval velocity is the least
well-determined quantity in the model.

---

## ★★★7 — High semblance, biased velocity

Semblance measures **coherency along a hyperbolic path**, and the two-layer
moveout is *almost* hyperbolic. A single hyperbolic path therefore still aligns the
traces well (hence $S = 0.9956$) while the best-fitting velocity differs from the
model's $\overline{v^2}$ definition by $0.70\%$. The misfit is spread thinly over
the far offsets (residual $0.675\ \mathrm{ns}$), so the semblance value barely
notices.

Report: the peak $(v, t_0)$, the $0.9$-of-peak width as the resolution, the
analytic noise-limited error, the residual moveout after correction (as the
evidence for model error), and a statement that a single hyperbolic velocity fits
this event to $0.68\ \mathrm{ns}$ at the far offset. The demonstration prints
exactly these.

---

## ★★★8 — A velocity programme

Requirements: interval velocity for the $1.5$–$3.0\ \mathrm{m}$ layer to $5\%$.

- Second-reflector time: $t_{0,1} = 2\times1.5/0.06 = 50.0\ \mathrm{ns}$;
  $t_{0,2} = 50.0 + 2\times1.5/0.09 = 83.3\ \mathrm{ns}$.
- Offsets: from the aperture rule, $x_{\max} \approx 1.5\times$ the deeper target
  depth $= 4.5\ \mathrm{m}$, with at least 20 offsets at $0.2\ \mathrm{m}$ steps.
- Resolution: from the demonstration's scaling, a maximum offset of
  $4.0\ \mathrm{m}$ gave a $0.9$-of-peak width of $0.0020\ \mathrm{m\,ns^{-1}}$
  for a comparable two-layer event; scaling by $(4.0/4.5)^{2}$ gives about
  $0.0016$, i.e. $\sim2\%$ of $0.09$ — inside the $5\%$ target.
- Independent cross-check: a slant stack of the direct ground wave gives the
  top-layer velocity ($0.0600$, recovered to $+0.10\%$ in the demonstration), and
  it uses linear moveout only, so it cannot inherit the hyperbolic model error.
  A second check is a target of known depth (a buried marker or a borehole
  intersection) used to calibrate the depth conversion.
