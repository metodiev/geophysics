# Solutions — 12-05-03 Rotation Variations, LOD and Core-Mantle Coupling

> Read after attempting the
> [exercises](./03-rotation-and-length-of-day-exercises.md). Lesson:
> [03 Rotation Variations, LOD and Core-Mantle Coupling](../03-rotation-and-length-of-day.md).
> Numbers computed. All models **SYNTHETIC**.

---

## ★1 — The budget

$$H_3 = C\Omega = 8.04\times10^{37}\times7.292115\times10^{-5}
= 5.86286\times10^{33}\ \mathrm{kg\,m^{2}\,s^{-1}}.$$

For a 2-ms change,

$$\frac{\Delta\,\mathrm{LOD}}{\mathrm{LOD}} = \frac{2\times10^{-3}}{86400}
= 2.3148\times10^{-8},$$

$$\Delta L = H_3\times2.3148\times10^{-8} = 1.35716\times10^{26}
\ \mathrm{kg\,m^{2}\,s^{-1}}.$$

Units: kg m² s⁻¹ × dimensionless = kg m² s⁻¹ ✔.

---

## ★2 — The budget and conservation

$$\frac{\Delta\,\mathrm{LOD}}{\mathrm{LOD}} = \frac{\Delta h}{C\Omega},$$

with $h$ the angular momentum carried by motion relative to the solid body. Any
exchange between parts of a closed system leaves the total unchanged, because the
torque between two parts is equal and opposite — which is why an LOD change can
only ever be evidence of an *exchange*, not of a creation or a loss.

---

## ★3 — Winds to milliseconds

$$\Delta\,\mathrm{LOD} = \mathrm{LOD}\times\frac{1.5\times10^{25}}{5.86286\times10^{33}}
= 86400\times2.5584\times10^{-9} = 2.2105\times10^{-4}\ \mathrm{s}
= 0.221\ \mathrm{ms}.$$

---

## ★★4 — The residual and the torque

Residual $= 2.000 - 0.221 = 1.779$ ms, i.e.

$$\Delta L_{\text{resid}} = 1.35716\times10^{26} - 1.5\times10^{25}
= 1.20716\times10^{26}\ \mathrm{kg\,m^{2}\,s^{-1}}.$$

Mean torque over 5 years ($1.578\times10^{8}$ s):

$$\tau = \frac{1.20716\times10^{26}}{1.578\times10^{8}}
= 7.65\times10^{17}\ \mathrm{N\,m}.$$

This is the *requirement*. Note how the relative size of the terms works out: the
winds supply 11% of the change and the residual is 89% of it, so the "core
signal" in this synthetic example is dominant — which is not the case in general
and would have to be established from the data rather than assumed.

---

## ★★5 — Electromagnetic coupling time

$$\tau_{\text{EM}} = \mu_0\sigma\,d\,D
= 1.2566\times10^{-6}\times10^{3}\times10^{5}\times2.187\times10^{7}
= 2.748\times10^{9}\ \mathrm{s} = 87.1\ \mathrm{yr}.$$

That is a *centennial* timescale, an order of magnitude too long for a decadal
signal (and, importantly, it is a timescale for the torque to act rather than a
period of oscillation — so "too long" is a statement about the exchange rate).

For $\tau = 10$ yr $= 3.1557\times10^{8}$ s,

$$\sigma = \frac{\tau}{\mu_0 d D}
= \frac{3.1557\times10^{8}}{1.2566\times10^{-6}\times10^{5}\times2.187\times10^{7}}
= 1.148\times10^{2}\ \mathrm{S\,m^{-1}}.$$

So a decadal timescale requires $\sigma \approx 10^{2}$ S/m in a 100-km layer —
two orders of magnitude less conductive than the value assumed in the question.

---

## ★★6 — Topographic capacity

$$\tau_{\max} = \frac{\pi^{2}}{2}\Delta\rho\,g\,h_0^{2}mR^{2}
= \frac{9.8696}{2}\times4400\times10.7\times(500)^{2}\times2\times
(3.48\times10^{6})^{2}$$

$$= 4.9348\times4400\times10.7\times2.5\times10^{5}\times2\times1.211\times10^{13}
= 1.407\times10^{24}\ \mathrm{N\,m}.$$

Ratio to the requirement:

$$\frac{1.407\times10^{24}}{7.65\times10^{17}} = 1.8\times10^{6}.$$

A 0.5-km CMB topography has six orders of magnitude more torque capacity than the
residual requires. **The capacity is not the issue; whether the topography is
uncompensated and unlocked is.**

---

## ★★★7 — Inner-core differential rotation for the residual

$$\Delta\Omega_{\text{ic}} = \frac{\Delta L_{\text{resid}}}{C_{\text{ic}}}
= \frac{1.20716\times10^{26}}{5.85\times10^{34}} = 2.063\times10^{-9}
\ \mathrm{rad\,s^{-1}}.$$

As a fraction of the rotation rate:

$$\frac{\Delta\Omega_{\text{ic}}}{\Omega} = \frac{2.063\times10^{-9}}
{7.292\times10^{-5}} = 2.83\times10^{-5}.$$

In degrees per year:

$$2.063\times10^{-9}\times3.1557\times10^{7}\times\frac{180}{\pi}
= 3.73\ \mathrm{deg\,yr^{-1}}.$$

**Plausibility.** Three and a half degrees per year is an enormous differential
rotation — the inner core would have to change its rotation rate by that much in
the course of a few years, which exceeds any published claim by orders of
magnitude. **The implication.** A 2-ms residual cannot be attributed to inner-core
rotation; it must be carried by the whole core, whose moment of inertia is 160
times larger (giving $2.3\times10^{-2}$ deg/yr, still large but at least of the
right order for a decadal exchange). This kind of arithmetic is exactly how the
inner core's role is bounded rather than asserted.

---

## ★★★8 — Discriminating the mechanisms

**Observable.** The *phase relation* between the LOD residual and independent
measurements of the other two quantities:

1. **The magnetic field at the CMB.** Electromagnetic coupling requires a strong,
   correctly oriented poloidal field threading the lowermost mantle, and the
   torque depends on the field *and* on the conducting layer's thickness and
   conductivity. A candidate LOD residual should be accompanied by a
   secular-variation signal at the CMB of the right geometry and timescale; the
   field history also has to have been strong enough at that epoch.

2. **The CMB topography.** Topographic coupling requires long-wavelength
   undulations of the CMB that are not compensated by a density anomaly. The
   testable prediction is that the LOD residual's amplitude should scale with the
   *square* of the topography amplitude ($\tau \propto h_0^{2}$), so a region or
   epoch with twice the topographic amplitude should show four times the coupling
   signature.

**Models required.** For the electromagnetic route, a dynamo-based field model at
the CMB for the relevant epoch plus a conductivity profile; for the topographic
route, a model of the CMB topography and of its dynamic compensation, which is
itself derived from the same geoid and seismic observations.

**Separating prediction.** Electromagnetic coupling is limited by the *magnetic
diffusion time* through the conducting layer and should therefore act as a low-pass
filter on the LOD signal, with a cutoff that moves as the layer's conductivity
changes (and hence should differ between the present and an epoch when the layer
was hotter). Topographic coupling is essentially instantaneous and should show no
such frequency-dependent cutoff. **A measured frequency-dependent coupling
strength is therefore the discriminator**, and it is the reason the two mechanisms
can in principle be told apart even though both can supply the required torque.

---

## What a good answer looks like

Every torque was labelled as a requirement or a capacity, every differential
rotation was compared with a plausibility argument, and no mechanism was declared
the source on the strength of a capacity estimate.
