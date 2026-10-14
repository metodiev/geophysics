# Solutions — 12-02-02 High-Pressure Experiments and Diamond Anvil Cells

Worked solutions for
[02-high-pressure-experiments-exercises.md](./02-high-pressure-experiments-exercises.md).
The lesson is
[02 High-Pressure Experiments and Diamond Anvil Cells](../02-high-pressure-experiments.md).
All models are **SYNTHETIC**.

---

## ★ Foundational

### ★1 — Culet size and pressure

$$A = \frac{\pi d_c^{2}}{4} = \frac{\pi\left(80\times10^{-6}\right)^{2}}{4}
= 5.027\times10^{-9}\ \mathrm{m^{2}},$$
$$P = \frac{F}{A} = \frac{350}{5.027\times10^{-9}} = 6.963\times10^{10}\ \mathrm{Pa}
= 69.6\ \mathrm{GPa}.$$

For 150 GPa at the same load:

$$A = \frac{350}{150\times10^{9}} = 2.333\times10^{-9}\ \mathrm{m^{2}},
\qquad
d_c = 2\sqrt{\frac{A}{\pi}} = 2\sqrt{7.427\times10^{-10}}
= 5.45\times10^{-5}\ \mathrm{m} = 54.5\ \mu\mathrm{m}.$$

Cross-check with the $P \propto d_c^{-2}$ scaling: halving the diameter from 80 to
54.5 µm multiplies the area by $(54.5/80)^2 = 0.464$, hence the pressure by 2.16, and
$69.6 \times 2.16 = 150.3$ GPa ✓. **The arithmetic is easy; surviving it is the
experimental problem**, which is why culet size is always quoted with the pressure.

### ★2 — A pressure scale

$$P = \frac{1}{s}\frac{\Delta\lambda}{\lambda_0}
= \frac{2.5\times10^{-2}}{5.26\times10^{-4}} = 47.53\ \mathrm{GPa}.$$

Resolution:

$$\Delta P = \frac{1}{5.26\times10^{-4}} \times \frac{0.05}{694.0}
= 1901.1 \times 7.205\times10^{-5} = 0.1370\ \mathrm{GPa}.$$

Relative error at 47.53 GPa: $0.1370/47.53 = \mathbf{0.29\ \%}$. Note the
structure of the answer: the *absolute* resolution is a constant fixed by the
wavelength resolution and the scale sensitivity, so the relative error is inversely
proportional to the pressure. This is why a low-pressure point in a data set is worth
less than a high-pressure one for determining $K_0$, even though it looks equally
precise on the axis label.

### ★3 — Two compressions

With $x = (V_0/V)^{2/3}$:

**At $V/V_0 = 0.95$:** $x = (1/0.95)^{2/3} = 1.03451$,
$$P = 1.5(160)\left[1.03451^{3.5} - 1.03451^{2.5}\right]
\left[1 + 0.75(4-4)(x-1)\right] = 240\left[1.12638 - 1.08859\right] = 9.07\ \mathrm{GPa}.$$

**At $V/V_0 = 0.80$:** $x = (1.25)^{2/3} = 1.16040$,
$$P = 240\left[1.16040^{3.5} - 1.16040^{2.5}\right] = 240\left[1.68665 - 1.45068\right]
= 56.63\ \mathrm{GPa}.$$

(The precise values from the demonstration's function are 9.094 and 55.84 GPa; the
small differences here are rounding in $x$.)

**Which is closer to linear?** Compare $P/(1-V/V_0)$: at 0.95 it is
$9.094/0.05 = 181.9$ GPa, at 0.80 it is $55.84/0.20 = 279.2$ GPa. The modulus
increases with compression (that is what $K_0' > 0$ means), so the *low*-compression
point is the more nearly linear one, and its effective modulus (181.9 GPa) is closer
to $K_0 = 160$ GPa than the high-compression value is. **This is the same statement
as "$K_0$ is the zero-pressure limit", and it is why a fit to low-pressure data alone
cannot separate $K_0$ from $K_0'$.**

---

## ★★ Applied

### ★★4 — Reading a covariance matrix

$$\sigma_{K_0} = \sqrt{7.0} = 2.646\ \mathrm{GPa}, \qquad
\sigma_{K_0'} = \sqrt{0.010} = 0.100,$$
$$r = \frac{-0.25}{\sqrt{7.0 \times 0.010}} = \frac{-0.25}{0.2646} = -0.9449.$$

For a linear combination $aK_0 + bK_0'$ the variance is
$\mathbf{a}^{T}\mathbf{C}\mathbf{a}$:

$$a = 1,\ b = 4:\quad
V = 7.0 + 16(0.010) + 2(4)(-0.25) = 7.0 + 0.16 - 2.0 = 5.16
\;\Rightarrow\; \sigma = 2.272\ \mathrm{GPa}.$$

(Here $K_0'/1$ is treated as carrying the unit GPa for the purpose of forming the
combination, as is conventional.) So the combination $K_0 + 4K_0'$ is determined to
**2.27 GPa** while $K_0$ alone is determined to **2.65 GPa**: the *sum* is better
determined because the two parameters move in opposite directions when the data are
refitted. The well-determined direction of the covariance ellipse is the one along
which $K_0$ and $K_0'$ move *together*, which is what $K_0 + 4K_0'$ approximates.

**The practical statement:** quoting "$K_0 = 160.0 \pm 2.6$ GPa and
$K_0' = 4.10 \pm 0.10$" as if the errors were independent overstates the constraint,
because a shift of $+0.4$ in $K_0'$ can be compensated by $-1.6$ GPa in $K_0$ with no
change in the fit. Report the correlation.

### ★★5 — Removing the thermal pressure

$$P_\text{th} = \alpha K_T\,\Delta T
= 3.0\times10^{-5} \times 130\times10^{9} \times (1700-300)
= 3.0\times10^{-5} \times 130\times10^{9} \times 1400
= 5.46\ \mathrm{GPa}.$$

The static pressure to use in the isothermal EOS is

$$P_\text{static} = 28.0 - 5.46 = 22.54\ \mathrm{GPa},$$

a correction of $5.46/28.0 = \mathbf{19.5\ \%}$.

**What an analyst who neglects it concludes:** the point $V(P)$ is plotted 5.46 GPa
too far to the right, i.e. the model must compress the sample *more* than it actually
did to reach that volume. The fit compensates by reducing $K_T$ and usually by
tweaking $K_0'$ as well, so the reported bulk modulus comes out systematically **too
low** — and, worse, the bias depends on temperature, so it appears as a
temperature-dependent modulus, which is exactly what a thermal-EOS experiment is
trying to measure. The correction is not independent of the answer either:
$\alpha$ and $K_T$ depend on $P$ and $T$, so removing $P_\text{th}$ is part of the
iterative inversion, not a pre-processing step.

### ★★6 — What 6 points to 30 GPa will give you

From the lesson's truncation table, the entry nearest this geometry is
$P_\text{max} = 30$ GPa (8 points): $K_0 = 157.4 \pm 7.8$ GPa and
$K_0' = 4.58 \pm 0.96$ against true values 160.0 and 4.10. Interpolating, 6 points to
30 GPa would give roughly

$$K_0 \approx 158 \pm 10\ \mathrm{GPa}, \qquad K_0' \approx 4.6 \pm 1.2,$$

i.e. a $K_0$ uncertainty of about **6 %** and a $K_0'$ uncertainty of about **26 %**.
Note that the *bias* in $K_0$ happens to be small here (157 against 160) while the
*bias* in $K_0'$ is large (4.6 against 4.1) — the two are correlated, so the misfit
stays small and the mistake is invisible in a residual plot.

**To beat 2 % on $K_0$** the table suggests a range of at least ~90 GPa: at
$P_\text{max} = 90$ the 1σ is 2.37 GPa, i.e. 1.5 % of 160. The scaling is roughly
$\sigma_{K_0} \propto 1/P_\text{max}$ over the tabulated range: from 13.7 GPa at 20
GPa to 1.7 GPa at 120 GPa is a factor of 8 for a factor of 6 in range, so the trend
is nearly linear in $1/P_\text{max}$. **Reaching a target $K_0$ precision is
therefore a pressure-range requirement, not a point-count requirement.**

### ★★7 — Is the quoted uncertainty meaningful?

Systematic pressure uncertainty at 60 GPa:

$$\delta P = 0.015 \times 60 = 0.90\ \mathrm{GPa}.$$

Since $K_0$ is essentially the slope of $P(V)$ at low compression, a pressure-scale
offset propagates into $K_0$ with a coefficient of order one (the demonstration's
$\mathrm{d}K_0/\mathrm{d}P_\text{scale} \approx 1$ is the natural scale), giving

$$\delta K_0^\text{syst} \approx 0.90\ \mathrm{GPa}.$$

So the formal $\pm 2$ GPa is *larger* than this particular systematic, and the quoted
uncertainty is meaningful **in this case**. But two cautions make the conclusion
narrow:

1. The calibration error is *fully correlated* across all points, whereas the formal
   ±2 GPa comes from random scatter. Adding them in quadrature is therefore wrong;
   the systematic should be treated as a bias, i.e. the true uncertainty on $K_0$ is
   "$\pm 2$ GPa random, plus an unknown offset of order 0.9 GPa".
2. The coefficient $\mathrm{d}K_0/\mathrm{d}P_\text{scale}$ is not always 1: if the
   EOS fit also adjusts $K_0'$, a scale offset is partly absorbed, and the effective
   coefficient can be either larger or smaller depending on the range. The
   demonstration's truncated fits show the coefficient changing as the range shrinks.

**The reporting rule:** a $K_0$ should carry both a random and a systematic
uncertainty, with the systematic traced to the scale calibration. Most published
values carry only the first.

---

## ★★★ Research-oriented

### ★★★8 — Determining $K_0'$ independently of $K_0$

**Why the problem is real.** $K_0$ and $K_0'$ are anticorrelated at −0.93 to −0.95 in
a fit to a conventional $P$–$V$ data set, so a narrow-range experiment determines only
a combination.

**Observables.**

1. **A wide compression range.** $K_0'$ is the curvature of $P(V)$, so it becomes
   visible only when the compression is large: at $V/V_0 = 0.9$ the BM3 curvature
   term contributes $(3/4)(K_0'-4)(x-1)$ with $x-1 = 0.0722$, i.e. a few per cent of
   the pressure; at $V/V_0 = 0.7$ it contributes 20 %. The demonstration quantifies
   this: fitting only to 20 GPa returns $K_0' = 2.21 \pm 2.06$, while fitting to
   120 GPa returns $4.12 \pm 0.08$ — the same model, the same noise, a *700-fold*
   improvement in the variance of $K_0'$ from extending the range.
2. **An independent pressure-scale-less constraint on compression.** Brillouin
   scattering or impulsive stimulated scattering gives the *sound velocity* at each
   pressure, hence $K_S = \rho v_p^2 - \frac43\rho v_s^2$ directly and
   $\mathrm{d}K/\mathrm{d}P$ along the compression path. An acoustic datum constrains
   $K$ at that pressure rather than the *difference* of compressions, which breaks
   the $K_0$–$K_0'$ degeneracy in a way that more X-ray points in the same range
   cannot.
3. **A known $V_0$ to high precision** from a separate ambient measurement, so that
   the fit's $V_0$ does not absorb part of the curvature.

**Sample requirements.** A single-phase, well-annealed sample in a quasi-hydrostatic
medium, with the gasket and culet geometry chosen so that the sample pressure is
uniform to a few per cent; a solid or noble-gas pressure medium; and, for the
acoustic measurement, an optically accessible geometry and an oriented single
crystal.

**Quantitative prediction.** With X-ray data to 150 GPa (compression
$V/V_0 \approx 0.63$) and 0.1 % volume precision, the demonstration's scaling
$\sigma_{K_0'} \propto 1/P_\text{max}$ predicts
$\sigma_{K_0'} \approx 0.08 \times (120/150) = 0.064$ — but the dominant term at that
compression is the *systematic* scale error, which enters $K_0'$ roughly as
$\delta K_0' \approx \delta\ln P/(\text{compression range})$. With a 1 % scale error
and a fractional compression range of 0.37, that is $0.01/0.37 = 0.027$ — smaller
than the formal error, so the wide-range experiment is genuinely limited by its
random noise and *not* by the calibration. **That is the payoff of a wide range: it
changes which error dominates.**

**Why range beats point count.** The information about curvature comes from the
*dynamic range* of the data, not its number: N points inside a compressed interval of
width $\Delta V$ constrain $K_0'$ with a variance that scales as
$1/(N\Delta V^{2})$ for the *best-determined* combination and
$1/\Delta V^{4}$ along the poorly determined direction. Increasing $N$ at fixed
$\Delta V$ helps only as $1/\sqrt{N}$; increasing $\Delta V$ helps quadratically or
better. **A wider range buys more than more points, and the demonstration's table is
the proof.**

### ★★★9 — Deviatoric stress as a hidden bias

**Size of the bias.** A deviatoric stress $t$ (the difference between the maximum and
minimum principal stresses) shifts and splits diffraction lines. In the simplest
model the measured lattice strain at a given pressure has a term linear in $t$, and
the apparent volume derived from a single reflection differs from the hydrostatic
volume by

$$\frac{\delta V}{V} \sim \frac{t}{G},$$

with $G$ the shear modulus of the sample. For $t = 1$ GPa and
$G = 130$ GPa (a plausible oxide), $\delta V/V \sim 0.008$ — **0.8 %**, which is four
times the 0.2 % diffraction precision assumed in the lesson's synthetic data.

**How it biases $K_0$.** The bias is not a constant offset: it grows with pressure as
the sample work-hardens, so it adds a systematic *curvature* to $V(P)$. A fit to BM3
cannot distinguish "the material is stiffer than I thought" from "the stress state is
wrong", so the bias lands in $K_0$ and $K_0'$ jointly, along their trade-off
direction. Scaling the lesson's Example 2 estimate, an 0.8 % volume error over a
compression range of 0.30 gives
$\delta K_0/K_0 \sim 0.008 \times 120/(160 \times 0.30) = 2\ \%$ — about **3 GPa**,
larger than the formal 1σ of 2.6 GPa. In other words, a 1 GPa deviatoric stress is
worth more uncertainty than the entire random error budget of a good experiment.

**Two tests that detect the bias without knowing the stress independently.**

1. **Load/unload hysteresis and cycling.** Collect the data on both branches. A
   hydrostatic compression is reversible; deviatoric stress produces hysteresis and
   path dependence. Fitting the two branches separately and comparing $K_0$ is the
   cheapest test.
2. **Multiple reflections / line-width analysis.** Under hydrostatic conditions all
   reflections move consistently and lines stay narrow. Deviatoric stress splits
   lines in a crystallographically systematic way (the $t$ and $s$ strain
   components), and the line widths grow with pressure. Fitting a single reflection
   hides this; using *all* reflections and requiring a consistent single-crystal
   strain model reveals it.

The practical mitigation is not statistical but procedural: anneal the sample, use a
pressure medium that stays hydrostatic over the range, and report the pressure
gradient across the sample. **An EOS fit cannot detect the problem it is being used
to solve.**

### ★★★10 — Second-order against third-order

Setting $K_0' = 4$ in the BM3 expression removes the curvature correction, giving the
second-order (Birch–Murnaghan) form. With $K_0 = 160$ GPa, the pressures predicted at
two compressions:

| $V/V_0$ | $P_\text{BM2}$ (GPa) | $P_\text{BM3}$ ($K_0' = 4.1$) (GPa) | difference (GPa) | difference (%) |
|---|---|---|---|---|
| 0.90 | 20.816 | 20.930 | 0.114 | 0.55 |
| 0.70 | 116.740 | 119.090 | 2.350 | 2.01 |

**Comparison with a 1 % calibration error.** At 100 GPa a 1 % scale error is 1.0 GPa.
So at $V/V_0 = 0.70$ the *choice of EOS form* (2.35 GPa) is **more than twice the
calibration error**, while at $V/V_0 = 0.90$ it is an order of magnitude smaller
(0.11 GPa).

Two conclusions:

- **At low compression the EOS form is irrelevant**, and a second-order fit is
  adequate — which is why a low-pressure-only study can quote either form and see no
  difference.
- **At high compression the form matters more than the calibration**, so an
  extrapolation of a low-pressure fit to core pressures is dominated by the
  functional form, not by the data quality. This is the quantitative version of the
  warning in the lesson's Section 4: reported $K_0$ and $K_0'$ values are only
  comparable when the *range* and the *form* are quoted, and at large compressions
  the form is the larger of the two uncertainties.

---

## Mastery checkpoint — worked version

> $V_0 = 40.12\ \mathrm{\AA^3}$, $K_0 = 152 \pm 3$ GPa,
> $K_0' = 4.30 \pm 0.10$, $\mathrm{corr} = -0.94$, range 0–40 GPa, $T = 300$ K,
> scale calibration ±1 %.

**(a) Systematic pressure error at 40 GPa.**

$$\delta P = 0.01 \times 40 = 0.40\ \mathrm{GPa}.$$

**(b) Which term dominates?** Propagating the scale offset into $K_0$ with a
coefficient of order one (the natural scale, since $K_0$ is the slope of $P(V)$ at
low compression):

$$\delta K_0^\text{syst} \approx 0.40\ \mathrm{GPa} \quad\text{against}\quad
3\ \mathrm{GPa}\ \text{formal}.$$

So the **formal (random) term dominates** here, and the quoted ±3 GPa is meaningful.
But the range is the reason the formal term is large: from the lesson's truncation
table, a fit restricted to ≤40 GPa has $\sigma_{K_0} \approx 5.4$ GPa at 0.2 %
volume precision, so this study's ±3 GPa implies either better diffraction or fewer
free parameters. And the correct way to report it is as a random part (±3 GPa) plus a
systematic part (~±0.4 GPa from the scale, fully correlated between points), not as a
single number.

**(c) What extending the range to 120 GPa would do.** Two effects, both from the
table and both in the same direction:

1. **The uncertainties would shrink by about a factor of three**: $\sigma_{K_0}$
   from ~3 GPa toward ~1.7 GPa, and $\sigma_{K_0'}$ from 0.10 toward 0.08. The
   variance of $K_0'$ scales roughly as $1/P_\text{max}^{2}$ over the table, so the
   gain is largest at the first extension and flattens afterwards.
2. **The values would move**, because the 0–40 GPa fit is biased: compression alone is
   not large enough to separate $K_0$ from curvature, so $K_0$ absorbs what $K_0'$
   should carry (and the table shows $K_0'$ running high, 4.41, at short range and
   settling to 4.12 at full range). Reporting over a wider range would move
   $K_0$ toward the true value and $K_0'$ down.

The *correlation* would improve (become less negative) but would not vanish: the
trade-off is a property of the model, not of the range.

**(d) Fitted rather than measured.** $V_0$, $K_0$ and $K_0'$ are all **fitted model
parameters** of an assumed EOS form — all three, even though $V_0$ is often treated
as a measurement because it can be obtained at ambient pressure from a separate
experiment. The quantity that looks like a measurement but is not is the **pressure**:
it is inferred through a calibration chain, and its uncertainty is a *traceable
systematic*, not a reading error. The only genuinely direct measurement in this
experiment is the unit-cell volume.
