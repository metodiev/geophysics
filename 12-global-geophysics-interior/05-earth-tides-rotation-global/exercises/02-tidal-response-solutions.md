# Solutions — 12-05-02 Tidal Response and the Quality Factor of the Whole Earth

> Read after attempting the
> [exercises](./02-tidal-response-exercises.md). Lesson:
> [02 Tidal Response and the Quality Factor of the Whole Earth](../02-tidal-response.md).
> Numbers computed. All models **SYNTHETIC**.

---

## ★1 — Phase lag for $Q = 250$

$$\delta = \arctan\frac{1}{250} = \arctan(0.004) = 0.22918190°,$$

$$\delta \approx \frac{180}{\pi Q} = \frac{57.29578}{250} = 0.22918312°.$$

Difference: $1.2\times10^{-6}$ degrees, i.e. $5\times10^{-6}$ relative. The
small-angle replacement is exact to better than a part in $10^{5}$ at this $Q$,
which is far below any measurement precision — and that is the point: the
approximation is never the limiting error.

---

## ★2 — Dissipation rate

$$P = \omega E\tan\delta = \omega E/Q .$$

For $Q = 80$:

$$P = 1.4\times10^{-4}\times8.0\times10^{16}/80
= 1.40\times10^{11}\ \mathrm{W} = 0.140\ \mathrm{TW}.$$

For $Q = 160$: **0.070 TW**, exactly half, because $P \propto 1/Q$.

---

## ★3 — Why a real Love number cannot drive recession

If $k_2$ were real, the deformation would be *in phase* with the forcing; there
would be no torque, no dissipation, and the Earth's rotation and the Moon's orbit
would exchange no angular momentum. The secular recession exists only because the
imaginary part of the response creates a phase lag, so the bulge leads the Moon
and pulls it forward.

---

## ★★4 — The hysteresis identity

With $x = x_0\cos\omega t$ and $\dot{x} = -x_0\omega\sin\omega t$,

$$W = \oint F\,\mathrm{d}x
= \oint k x\,\mathrm{d}x - \frac{k\tan\delta}{\omega}\oint\dot{x}^{2}\,\mathrm{d}t
= 0 - \frac{k\tan\delta}{\omega}\,\pi x_0^{2}\omega
= -\pi k\tan\delta\,x_0^{2}.$$

The average power over a cycle is $|W|/(2\pi/\omega)$:

$$P = \frac{\omega}{2\pi}\pi k\tan\delta\,x_0^{2}
= \frac{\omega}{2}kx_0^{2}\tan\delta
= \omega E\tan\delta,\qquad E = \tfrac12 kx_0^{2}.$$

Numerically: $E = \tfrac12\times4\times10^{20}\times0.04 = 8.0\times10^{18}$ J,
and

$$P = 1.4\times10^{-4}\times8.0\times10^{18}\times0.01
= 1.12\times10^{13}\ \mathrm{W} = 11.2\ \mathrm{TW}.$$

Note how much larger this synthetic spring is than the Earth's tide: the tide's
stored energy in the demonstration is $7.6\times10^{16}$ J, two orders of
magnitude smaller, which is why its dissipation is measured in tenths of a
terawatt.

---

## ★★5 — The single relaxation at 0.1 Hz

From the demonstration's fit, $\Delta = 0.010$ and $\tau = 7116$ s. At
$f = 0.1$ Hz, $\omega = 0.6283$ rad/s and $\omega\tau = 4471.4$:

$$Q^{-1} = \frac{\Delta\,\omega\tau}{1 + (\omega\tau)^{2}}
= \frac{0.01\times4471.4}{1 + 1.999\times10^{7}} = 2.24\times10^{-6},$$

$$Q = 4.47\times10^{5}.$$

A factor $4.47\times10^{5}/400 = 1.1\times10^{3}$ above the adopted comparison
value. The single relaxation over-predicts $Q$ by three orders of magnitude only
five decades above the tidal frequency — and by four orders at 1 Hz.

---

## ★★6 — The required absorption-band exponent

$$\alpha = \frac{\log_{10}(Q_2/Q_1)}{\log_{10}(\omega_2/\omega_1)}
= \frac{\log_{10}2}{\log_{10}(0.6283/1.4052\times10^{-4})}
= \frac{0.30103}{3.65076} = 0.0825 .$$

(The lesson's value of 0.0647 uses 1 Hz instead of 0.1 Hz; the exponent is
$\log_{10}2$ divided by the number of decades, so shortening the frequency range
increases the required exponent.)

The smallness of $\alpha$ is the result: over five decades $Q$ changes by less
than a factor of three, which is why a single "whole-Earth $Q$" is a defensible
shorthand — and why measuring its frequency dependence is hard.

---

## ★★★7 — Separating the ocean tide from the solid Earth

**Observables.**

1. **Satellite altimetry of the open-ocean tide**, which measures the ocean's
   response directly, away from coasts and away from the load of the solid tide.
2. **Gravimetric or strain tidal analysis at a low-ocean-load site**, which
   measures the solid body's response where the ocean load is small.
3. **Space-geodetic measurement of the secular $J_2$ and of the lunar
   recession**, which measure the *total* dissipation without separating its
   sources.

**Models required.** A satellite-altimetry tide model (a hydrodynamic or
assimilative solution, not a measurement), an ocean-load Green's function set,
and a solid-Earth tide model with frequency-dependent Love numbers.

**Dominant systematic in each case.** For the altimetry route, the internal-tide
and barotropic-model error in shallow water, which aliases into the diurnal and
semidiurnal bands. For the ground route, the ocean-load correction itself —
the correction is a model, and its error can exceed the signal in the phase lag.
For the geodetic route, the partition between the semidiurnal tide and
other secular effects (post-glacial rebound, in particular).

The key methodological point: the *total* dissipation is what the geodetic
observables constrain, and the solid-Earth contribution can only be isolated by
subtracting a model of the ocean's, i.e. by assuming the answer to the question.

---

## ★★★8 — Referee report on "$Q = 100 \pm 30$"

**Paragraph 1 (what the error bar should contain).** The quoted $\pm 30$ appears
to be a statistical error from the harmonic fit. It should instead be stated as
a budget: the statistical part (the fit uncertainty on the phase lag, which *does*
fall as more cycles are added), the calibration part (the instrument response,
whose phase error enters the lag directly), and the model part (the removal of
the ocean load, the atmospheric tide and the local site effects). For a
solid-Earth $Q$ derived from a phase lag, the last two terms usually dominate and
are typically larger than the statistical term by a factor of several. The
report should also state whether the quoted $Q$ is a whole-Earth or a
mantle-only value, since the ocean is inside the former.

**Paragraph 2 (what cannot be reduced by more data).** The non-reducible
contribution is the systematic one: more cycles of the same station reduce the
statistical error but leave the ocean-load model error untouched, because it is
a modelling error rather than a random one. To reduce it requires an independent
constraint on the load — a nearby station pair with different load geometry, or a
direct ocean-tide measurement at the relevant wavelengths. The referee should
therefore ask for the error budget to be split into reducible and non-reducible
components, and should be sceptical of any $\pm$ that shrinks with record length
alone.

---

## What a good answer looks like

Every dissipation number came with the Love number and the frequency it assumed,
and every error bar was split into statistical and systematic parts.
