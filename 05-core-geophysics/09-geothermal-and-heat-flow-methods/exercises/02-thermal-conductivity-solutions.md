# Solutions — 05-09-02 Thermal Conductivity Measurement and Corrections

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Two quantities

- $k$ (W m⁻¹ K⁻¹): the factor converting a temperature gradient into a heat flux,
  $q = -k\nabla T$. Needed in a heat-flow calculation.
- $\kappa$ (m² s⁻¹): the factor converting a length into a time,
  $\tau \sim L^2/\kappa$. Needed in any time-dependent problem.

$\kappa = k/(\rho c_p)$, with $\rho c_p$ of order $2$–$3\times10^{6}$ J m⁻³ K⁻¹ for
rock. Confusing them is a factor of a few, not a rounding.

---

## ★2 — Equal thicknesses of 1.0 and 4.0

$$k_\parallel = 0.5(4.0) + 0.5(1.0) = 2.5, \qquad
k_\perp = \left(\frac{0.5}{4.0} + \frac{0.5}{1.0}\right)^{-1}
= \left(0.125 + 0.5\right)^{-1} = 1.6,$$

$$A_k = \frac{2.5}{1.6} = 1.5625.$$

Check with equation (7) of the lesson: $(1+4)^2/(4\times4) = 25/16 = 1.5625$ ✓.

---

## ★3 — Which mean is smaller

The **harmonic** mean (series, heat flowing across the layers) is always the
smaller, and the arithmetic mean the larger; they are equal only if all
conductivities are equal. The physical reason: in series, the *least* conductive
layer sets the flux for a given total temperature drop, so it dominates; in
parallel, the *most* conductive layer carries most of the flux. The harmonic mean is
dominated by the smallest values and the arithmetic mean by the largest, which is
exactly the distinction.

---

## ★4 — The three means

**(a)** Demonstration stack (0.30 shale 1.5, 0.50 sandstone 3.5, 0.20 limestone 2.8):
arithmetic 2.7600, harmonic 2.4138, geometric 2.5959 W m⁻¹ K⁻¹; ratio 1.143.

**(b)** For 0.50 shale (1.5), 0.30 sandstone (3.5), 0.20 evaporite (5.0):

- arithmetic $= 0.5(1.5) + 0.3(3.5) + 0.2(5.0) = 0.75 + 1.05 + 1.00
  = 2.8000$ W m⁻¹ K⁻¹;
- harmonic $= (0.5/1.5 + 0.3/3.5 + 0.2/5.0)^{-1}
  = (0.3333 + 0.0857 + 0.0400)^{-1} = (0.4590)^{-1} = 2.1787$ W m⁻¹ K⁻¹;
- geometric $= 1.5^{0.5} \cdot 3.5^{0.3} \cdot 5.0^{0.2}
  = 1.2247 \times 1.4546 \times 1.3797 = 2.4783$ W m⁻¹ K⁻¹.

Ratio arithmetic/harmonic $= 1.285$.

**(c)** The **harmonic** mean belongs in a vertical heat-flow calculation, because a
vertical borehole samples the layers in series. Using the arithmetic value here
would overestimate the heat flow by 28 per cent.

---

## ★5 — Divided bar

**(a)** $k_s = 3.50 \times (40/50) \times (2.00/2.80)
= 3.50 \times 0.8 \times 0.7143 = 2.0000$ W m⁻¹ K⁻¹.

**(b)** Relative uncertainty
$= \sqrt{(0.03/2.00)^2 + (0.03/2.80)^2} = \sqrt{0.000225 + 0.000115}
= \sqrt{0.000340} = 0.0184$, i.e. **1.8 per cent**, or $\pm 0.037$ W m⁻¹ K⁻¹
(assuming no error in the lengths, which at a 0.1 mm precision on 40–50 mm
contributes 0.25 per cent, negligible in comparison).

**(c)** The **sample temperature difference** dominates, because it is both smaller
in absolute terms (2.80 K) and divided into the result. The general rule: in a
divided bar, improve the thermometry before the length measurement.

---

## ★6 — Diffusivity and timescales

$$\kappa = \frac{k}{\rho c_p} = \frac{2.6}{2700 \times 900} = 1.070\times10^{-6}\
\mathrm{m^2\,s^{-1}}.$$

Diffusion time over 1 km: $L^2/\kappa = 10^{6}/1.070\times10^{-6} = 9.35\times10^{11}$
s $= 2.96\times10^{4}$ yr (about **30 ka**).

Diffusion length in 1 Ma: $\sqrt{\kappa t} = \sqrt{1.070\times10^{-6}\times3.156
\times10^{13}} = \sqrt{3.377\times10^{7}} = 5812$ m, i.e. about **5.8 km**.

Both numbers are the standard "kilometre per 30 ka, six kilometres per Ma" rule of
thumb for crustal rock at these properties.

---

## ★7 — A statistical orientation model

A defensible construction: assign each element a random orientation and weight the
two components by $\cos^2\theta$ and $\sin^2\theta$, then average over a stated
orientation distribution (isotropic, or with a preferred alignment |parameter| $p$
from 0 for random to 1 for perfectly aligned). The result lies between the harmonic
and arithmetic bounds by construction, since any such average is a weighted
combination of the two:

$$k_{\text{eff}}(p) \in [k_\perp, k_\parallel], \qquad
p = 0 \Rightarrow \text{closer to geometric}, \qquad
p = 1 \Rightarrow \text{approaching the bounds}.$$

**Geological mapping:** perfectly laminated shale approaches the bounds (series for
vertical flow); a massive sandstone with dispersed grains approaches the geometric
mean and is nearly isotropic; a fractured or mylonitic rock with a strong foliation
lies between, and its anisotropy is a *structural* measurement as much as a
thermal one. The honest report states the parameter $p$ only if a texture
measurement supports it; otherwise report the bounds as an interval.

---

## ★8 — A measurement programme for a 2 km hole

**Design:**

1. **Sampling:** 3–5 samples per major lithological interval, i.e. of order 30–60
   samples for a 2 km hole, biased towards the intervals that carry most of the
   temperature drop (the low-conductivity shales), because the *integral* of
   $1/k$ controls the temperature.
2. **Orientation:** measure both $k_\parallel$ and $k_\perp$ on at least one sample
   per interval, to establish the anisotropy, then $k_\perp$ on the rest.
3. **Conditions:** measure saturated (or correct explicitly), at the *in-situ*
   effective pressure if the apparatus allows, and state the measurement
   temperature.
4. **Borehole method:** run a borehole conductivity tool (optical scanning or a
   divided-bar tool in the hole) at a coarse sampling, to give a continuous
   profile and to catch intervals not cored.

**Combine** core (absolute, need corrections) with the borehole log (continuous,
needs calibration): calibrate the log against the cores and use the log's shape with
the cores' levels.

**Resulting uncertainty:** expect 5–10 per cent on $k_\perp$ for a well-sampled
interval and 15–25 per cent for a poorly sampled one. Since $q = k\,\mathrm{d}T/
\mathrm{d}z$, this is 5–25 per cent on the heat flow — comparable with the usual
temperature-gradient uncertainty, which is why both terms must be in the budget and
neither can be neglected.
