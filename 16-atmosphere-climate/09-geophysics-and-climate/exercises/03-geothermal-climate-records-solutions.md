# Solutions — 16-09-03 Borehole Temperature Records of Past Climate

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [03 Borehole Temperature Records of Past Climate](../03-geothermal-climate-records.md).

---


## ★ Foundational

## ★1 — A step signature at depth

$$t = 150\ \mathrm{yr} = 150 \times 3.15576\times10^{7}
= 4.734\times10^{9}\ \mathrm{s},$$
$$\kappa t = 1.0\times10^{-6} \times 4.734\times10^{9}
= 4.734\times10^{3}\ \mathrm{m^{2}}, \qquad
\sqrt{\kappa t} = 68.80\ \mathrm{m},$$
$$u = \frac{z}{2\sqrt{\kappa t}} = \frac{60}{137.6} = 0.4360.$$

$$\operatorname{erfc}(0.4360) = 0.5375, \qquad
\Delta T(60\ \mathrm{m}) = 1.5 \times 0.5375
= \mathbf{0.806\ K}.$$

So a $1.5\ \mathrm{K}$ surface step 150 years old has decayed to
$0.81\ \mathrm{K}$ at $60\ \mathrm{m}$ — a little over half its amplitude. The
Bessel-type decay is why a deep profile integrates many decades together.

---

## ★2 — E-folding depths

$$d = \sqrt{\frac{\kappa P}{\pi}} = \sqrt{\frac{1.0\times10^{-6} \times P \times
3.15576\times10^{7}}{\pi}}.$$

| $P$ (yr) | $d$ (m) |
|---|---|
| 50 | 22.41 |
| 200 | 44.82 |
| 500 | 70.87 |

A $300\ \mathrm{m}$ profile resolves all three, but with very different
efficiencies: the $50$-year oscillation has decayed by
$e^{-300/22.4} = e^{-13.4} \approx 10^{-6}$ at the bottom, effectively
indistinguishable from noise there, whereas the $500$-year oscillation has decayed
by only $e^{-300/70.9} = e^{-4.23} = 0.015$ — still $1.5\%$ of its surface
amplitude at the base of the profile, which is measurable. **The profile is a
long-period instrument: the longest period present is the one best constrained.**

---

## ★3 — A forward-matrix entry

$$\sqrt{\kappa \times 100\ \mathrm{yr}} = 56.176\ \mathrm{m}
\;\Rightarrow\; u(100) = \frac{50}{2 \times 56.176} = 0.4450,$$
$$\sqrt{\kappa \times 50\ \mathrm{yr}} = 39.72\ \mathrm{m}
\;\Rightarrow\; u(50) = \frac{50}{2 \times 39.72} = 0.6293,$$

$$G = \operatorname{erfc}(0.4450) - \operatorname{erfc}(0.6293)
= 0.5291 - 0.3722 = \mathbf{0.1569}.$$

A $1\ \mathrm{K}$ surface temperature over that $50$-year interval raises the
temperature at $50\ \mathrm{m}$ today by $0.157\ \mathrm{K}$. Note the implication
for inversion: the data are a $6$-fold *attenuation* of the signal being sought, so
inverting requires dividing by small numbers — which is the origin of the
instability.

---

## ★★ Applied

## ★★4 — Amplification and the truncation decision

| direction | $\sigma$ | $1/\sigma$ |
|---|---|---|
| 1 | 1.266 | 0.79 |
| 2 | 0.493 | 2.03 |
| 3 | 0.143 | 6.99 |
| 4 | 0.028 | 35.71 |
| 5 | 0.003 | 333.33 |

Retention criterion: a component contributes at most
$(1/\sigma) \times \text{noise}$ to the history error. With a noise of
$0.02\ \mathrm{K}$ and a tolerance of $1\ \mathrm{K}$:

- direction 1: $0.79 \times 0.02 = 0.016\ \mathrm{K}$ — fine;
- direction 2: $2.03 \times 0.02 = 0.041\ \mathrm{K}$ — fine;
- direction 3: $6.99 \times 0.02 = 0.140\ \mathrm{K}$ — fine;
- direction 4: $35.71 \times 0.02 = 0.714\ \mathrm{K}$ — acceptable;
- direction 5: $333.33 \times 0.02 = 6.67\ \mathrm{K}$ — **exceeds the tolerance**.

So retain four directions, i.e. $k = 4$, which is consistent with the
demonstration's measured optimum of $k = 3$ for its own noise draw: the exact
optimum depends on the noise realisation, and the criterion above is the
reproducible way to choose.

---

## ★★5 — Choosing a truncation

**Choice: $k = 3$.**

Justification: at $k = 3$ the rms misfit ($0.0238\ \mathrm{K}$) has already
reached the profile noise level ($0.02\ \mathrm{K}$), so the fit is as good as the
data allow; and the rms bin error is $0.399\ \mathrm{K}$, the smallest of any row.
Going to $k = 5$ or $6$ reduces the misfit by less than $0.005\ \mathrm{K}$ —
i.e. by less than a quarter of the noise — while the bin error rises to $2.845$
and $17.230\ \mathrm{K}$. The extra components are fitting noise, not history, so
$k$ should be the smallest value that reaches the noise-level misfit.

---

## ★★6 — A null direction

$$\delta(\text{profile}) = \sigma \times \delta h = 1.0\times10^{-4}
\times 0.5 = \mathbf{5.0\times10^{-5}\ K\ rms}.$$

That is $5\times10^{-5}\ \mathrm{K}$ against a profile noise of $0.02\ \mathrm{K}$,
a ratio of $2.5\times10^{-3}$. A profile with $0.02\ \mathrm{K}$ noise **cannot
detect it**: the change is $400$ times smaller than the noise. So the data are
consistent with two surface histories differing by $0.5\ \mathrm{K}$ — by half a
kelvin, not by a rounding error. This is the argument for reporting an admitted
family of histories: the non-uniqueness is not a small correction, it is a
first-order ambiguity in the quantity being reported.

---

## ★★★ Research-oriented

## ★★★7 — How much advection breaks a diffusion-only inversion (design)

**Forward model.** Two forward operators on the same surface history:
(i) pure conduction, $\partial_t T = \kappa \partial_z^2 T$;
(ii) conduction plus vertical advection by a Darcy flux,
$\partial_t T = \kappa \partial_z^2 T + v_z \partial_z T$,
with $v_z$ set by a chosen (synthetic) groundwater flux divided by the
volumetric heat capacity.

**Estimator.** Invert the *advective* synthetic profile with the *conductive*
forward model (a deliberate model error), using truncated SVD at a fixed
truncation, and compare the recovered history with the true one.

**Metric.** The rms bin error of the reconstructed history as a function of the
Péclet number $\mathrm{Pe} = v_z L / \kappa$, where $L$ is the profile depth.

**Tolerance.** Report the $\mathrm{Pe}$ at which the history error equals (a) the
reconstruction's own noise-driven error at $\mathrm{Pe} = 0$ and (b) the reported
uncertainty. The result that defines the tolerance is the $\mathrm{Pe}$ at which
the advection-induced error exceeds the quoted uncertainty; below that, a
conductive inversion is adequate *for that reported precision*, and above it, it
is not. A useful extra output is the shape of the misfit: advection biases the
deepest bins first, so the residual pattern, not just its size, identifies the
missed process.

---

## ★★★8 — Sensitivity analysis for a quoted $2.0 \pm 0.3\ \mathrm{K}$ warming

**Three assumptions to propagate, in the order I expect them to matter:**

1. **The thermal diffusivity $\kappa$.** It rescales the depth-to-time mapping, so
   an error in it moves the *timing* of the reconstructed change and hence the
   amplitude assigned to a fixed window. With $\kappa$ uncertain by, say, $20\%$
   (lithology, saturation), the depth corresponding to a given age moves by
   $\sqrt{1.2} \approx 1.10$, i.e. $10\%$, which reorganises which bins carry the
   signal. Expected to dominate, because it acts multiplicatively on the
   independent variable.
2. **The geothermal gradient removed before inversion.** It contributes several
   kelvin across the profile against a sub-kelvin signal ($7.75\ \mathrm{K}$ vs
   $0.60\ \mathrm{K}$ in the demonstration), so an error of a few per cent makes a
   large apparent perturbation. Expected second, and strongly correlated with the
   reconstruction's own deep-end behaviour.
3. **The non-conductive heat transport (advection, latent heat, land-use change).**
   Expected third in magnitude for a typical site but the hardest to bound, and
   the one most likely to produce a *sign* error rather than a magnitude error.

**Procedure.** Re-run the inversion with each assumption perturbed within a stated
prior (or with a stated bound), and report the resulting distribution of the
reconstructed warming: a central estimate plus the fraction of the $0.3\
\mathrm{K}$ budget attributable to each assumption. If the propagated uncertainty
exceeds $0.3\ \mathrm{K}$, the published uncertainty is too small, and the honest
report states which assumption sets the floor.

**Also required:** the truncation $k$, the depth range and the profile noise —
without those the uncertainty cannot be reproduced at all.
