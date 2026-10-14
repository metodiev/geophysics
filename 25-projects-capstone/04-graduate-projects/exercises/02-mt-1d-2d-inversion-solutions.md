# Solutions — 25-04-02 Project: 1-D and 2-D Magnetotelluric Inversion

> Read after attempting. Lesson:
> [02 MT Inversion](../02-mt-1d-2d-inversion.md). All values are **SYNTHETIC**
> teaching numbers printed by
> [`code/mt_inversion_demo.py`](../code/mt_inversion_demo.py).

---

## ★1 — Skin depth

$$\delta = \sqrt{\frac{2\rho}{\omega\mu_0}}
= 503.3\sqrt{\frac{\rho}{f}}\ \mathrm{m}
= 5.03\sqrt{\frac{\rho}{100}}\sqrt{\frac{1}{f}}\ \mathrm{km},$$

so in $100\ \Omega\,\mathrm{m}$ rock:

| $f$ (Hz) | $\delta$ |
|---|---|
| 0.01 | $50.3\ \mathrm{km}$ |
| 0.1 | $15.9\ \mathrm{km}$ |
| 1 | $5.03\ \mathrm{km}$ |
| 10 | $1.59\ \mathrm{km}$ |

Both agree with the demonstration's $5.0\ \mathrm{km}$ at 1 Hz. The band
$0.01$–$10\ \mathrm{Hz}$ samples roughly 1.6 to 50 km in this resistivity —
a factor of 31 in depth for a factor of $10^{3}$ in frequency, because
$\delta \propto f^{-1/2}$. This square-root scaling is the reason MT needs three
decades of frequency to cover one and a half decades of depth.

---

## ★2 — The half-space limit

For a layer of resistivity $\rho$ over a half-space of the same resistivity, the
reflection term vanishes because
$Z_{k+1} = Z_k^{\text{layer}}$, and

$$Z_k = Z_k^{\text{layer}}\frac{Z_k^{\text{layer}} + Z_k^{\text{layer}}\tanh x}
{Z_k^{\text{layer}} + Z_k^{\text{layer}}\tanh x} = Z_k^{\text{layer}},$$

independent of thickness — a uniform half-space is indistinguishable from a
layered model whose layers all have the same resistivity, which is the simplest
statement of the method's non-uniqueness. Then

$$\rho_a = \frac{|Z|^{2}}{\omega\mu_0} = \frac{\omega\mu_0\rho}{\omega\mu_0} = \rho,
\qquad
\phi = \arctan\frac{\operatorname{Im}Z}{\operatorname{Re}Z} = 45° .$$

The $45°$ phase is the signature of induction in a uniform half-space and is the
first sanity check on any MT processing chain: a phase that is not near $45°$ over
some band means the section is layered there.

---

## ★3 — The distortion's amplitude bias

$$|D|^{2} = 1.25^{2} = 1.5625,
\qquad
\Delta\log_{10}\rho_a = \log_{10}1.5625 = +0.194\ \text{decade}
= +56.3\%,$$

matching the demonstration.

**Why the phase cannot be absorbed.** A layered model's phase is a *function of
frequency*, determined by the depth distribution of conductivity: it passes through
$45°$ in a uniform half-space, rises above it where resistivity decreases with
depth, and falls below it where resistivity increases. A constant $+8°$ offset
across the whole band — the signature of a galvanic distortion — is not any
function of frequency that a layered model can produce, so the inversion cannot fit
it and the misfit climbs to $916$ instead of $1$. The amplitude factor, by contrast,
looks exactly like a slightly more resistive section and *can* be absorbed, which is
why the correct diagnosis comes from the phase and misfit, not from the amplitude.

---

## ★★4 — The penalty and the misfit

$$\frac{\chi^{2}(\alpha = 2.0)}{\chi^{2}(\alpha = 0.02)}
= \frac{0.8033}{0.7150} = 1.12.$$

A $12\%$ difference in per-datum misfit, both comfortably below the noise level of
$1$, buys a model with the roughness reduced from $19.80$ to $2.67$ and a change of
up to $1.259$ in $\log_{10}\rho$ — a factor of $18.2$ in resistivity. Since the
$\chi^{2}$ surface is nearly flat there, **the data have not chosen between these
models; the analyst has.** The smoothest model is therefore not "the answer": it is
the model preferred by the strongest prior, and choosing it because its misfit is
not measurably worse is exactly the choice that must be reported. The defensible
practice is to report all three (or the $\chi^{2}$-versus-roughness curve) and to
show that the geological conclusion is stable across them — or to say that it is
not.

---

## ★5 — Fixed conductance and why only one thickness fits

$$t = 600\ \mathrm{m}:\ \rho = \frac{600}{540} = 1.11\ \Omega\,\mathrm{m},$$

$$t = 2700\ \mathrm{m}:\ \rho = 5.00\ \Omega\,\mathrm{m},
\qquad
t = 10800\ \mathrm{m}:\ \rho = 20.00\ \Omega\,\mathrm{m},$$

with reported misfits $106.6$, $1.121$ and $179.0$ per datum.

**Why only 2700 m is accepted.** The S-equivalence argument treats the conductor as
a *thin* layer whose only electromagnetic signature is its conductance,
$h/\rho$. That holds while the layer is thin compared with the skin depth at the
frequencies that sense it. Here the skin depth in the conductor at 0.3 Hz is
$2.05\ \mathrm{km}$, and the conductor is $2700\ \mathrm{m}$ thick — thicker than
the skin depth. The field therefore does not traverse it as a thin sheet: the
depth to its base is sensed, the phase and amplitude constrain the *depth extent*
independently of the conductance, and the trade-off collapses. A thinner conductor
(a few hundred metres, as in a sedimentary or shear-zone target) would show a broad
equivalence; a thick one does not.

**The general lesson.** Whether a degeneracy applies is a property of the *model
and band*, not of the method's reputation. The demonstration's $1.05$ scan step is
the resolution of its own test: the class along this direction is narrower than one
grid step.

---

## ★★6 — A field inversion that will not fit

**Diagnosis.** A misfit of $916$ per datum with a reasonable-looking model is not a
resolution problem; it is a **model-error** problem: the data contain a component
that no 1-D model can represent. The two most likely such components are
(a) galvanic distortion from nearby lateral conductivity contrast, producing a
frequency-independent complex factor, and (b) genuine 2-D or 3-D structure, which
also splits the response into TE and TM modes with different sensitivities.

**Indicators to check.**

1. **The TE–TM mode split**, computed as the difference between the two apparent
   resistivities and phases as a function of frequency. A split that grows with
   period indicates lateral structure whose influence deepens with skin depth; a
   frequency-independent, mode-*independent* offset is more likely distortion.
2. **The tipper** (the vertical-magnetic transfer function) and its magnitude and
   induction arrows. A non-zero tipper with a consistent direction is direct
   evidence of lateral gradients; its magnitude and orientation locate the boundary
   relative to the site.

Two further checks are cheap and belong in the same pass: the **phase tensor**
skew and ellipticity, which are distortion-free by construction, and a consistency
test between neighbouring sites, since distortion is site-specific while regional
structure is coherent.

**The next inversion.** A 2-D inversion jointly fitting TE and TM (with the
distortion parameters moved into the inversion as unknowns, or with a distortion
decomposition applied first if the site spacing is dense enough to estimate a
regional impedance). If the tipper and the mode split are directionally consistent
across the array, let the 2-D model's strike direction be that direction; if they
are not, the dataset is three-dimensional and a 2-D result will be an average of
unknown meaning.

---

## ★★★7 — A dimensionality test before model selection

**Quantities to compute.**

| quantity | what it is | what it indicates |
|---|---|---|
| TE–TM apparent-resistivity and phase split | difference between the two modes versus period | lateral structure whose influence deepens with period |
| tipper magnitude and induction arrows | vertical-magnetic transfer function | presence, direction and side of a lateral contrast |
| **phase tensor** skew $\beta$ and ellipticity | derived from the impedance, invariant to distortion | dimensionality independent of a galvanic factor |
| skew of the impedance tensor | $\lvert Z_{xy}+Z_{yx}\rvert/\lvert Z_{xy}-Z_{yx}\rvert$ | 3-D versus 2-D structure |

**Thresholds.** The standard first pass is: phase-tensor skew small (a few degrees)
and ellipticity near unit over most periods indicates 1-D; a large skew
($\gtrsim 5°$–$10°$) indicates 3-D; a 2-D interpretation is defensible when the
skew is small *after* rotating to the strike that minimises it, the TE–TM split is
stable in direction, and the tipper is consistent between neighbouring sites.

**Acquisition choices that make the test possible.** A **remote reference** to
suppress correlated noise (which otherwise mimics small skew), **multiple sites**
because distortion is site-specific while regional structure is coherent, wide
**period range** because the split's growth with period is the diagnostic rather
than the split's existence, and **broadband horizontal magnetic data** without which
the tipper cannot be computed.

**Parameterisation implied.** 1-D where skew and ellipticity are flat; 2-D with a
stated strike where the skew is small in the rotated frame and the tipper is
coherent; 3-D where the skew is large or the tipper direction rotates with period.

**What the test cannot detect.** A **thin, deep conductor whose distortion is
nearly isotropic**: a small, isotropic, frequency-independent factor leaves no
skew and no split, yet biases the apparent resistivity (§★3). Nor can it separate
a genuine 1-D earth from a 1-D earth under an isotropic static shift — the shift is
*by construction* invisible to every rotationally invariant quantity. That is why
the amplitude-bias correction of §★3 requires either a distortion decomposition
with the regional impedance assumed from a distance, or an independent constraint
such as a borehole resistivity log.
