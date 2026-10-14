# Solutions — 19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy

> **Read after attempting the exercises.** Arithmetic is shown; demonstration
> values are quoted where they apply.

Lesson: [04 Numerical Dispersion and Dissipation](../04-numerical-dispersion-diffusion.md).

---

## ★1 — Phase speeds

$\omega\,dt = \arcsin(C\sin\theta)$, $\theta = 2\pi/\mathrm{PPW}$,
$v_{\text{num}}/v = \arcsin(C\sin\theta)/(C\theta)$.

$\mathrm{PPW} = 4$: $\theta = \pi/2$, $\sin\theta = 1$,
$\arcsin(0.5) = 0.523599$, $C\theta = 0.785398$ → ratio $= 0.666667$
(a phase error of $-33.33\,\%$, as measured).

$\mathrm{PPW} = 10$: $\theta = 0.628319$, $\sin\theta = 0.587785$,
$C\sin\theta = 0.293893$, $\arcsin = 0.298535$, $C\theta = 0.314159$ → ratio
$= 0.950348$ (measured $0.94950813$; the small difference is the $O(\theta^{4})$
term of the arcsine).

---

## ★2 — Upwind dissipation

$$|G|^{2} = 1 - 2C(1-C)(1-\cos\theta), \qquad
D_{\text{num}} = \frac{ah}{2}(1-C).$$

For $0<C<1$, $|G|<1$: the scheme dissipates, and the modified equation is
advection with an added diffusivity $D_{\text{num}}$.

---

## ★3 — No dissipation

$|G| = 1$ for every mode in the stable range, so the amplitude of every Fourier
component is preserved exactly; all of the scheme's error is phase (dispersion)
error. The measured example is CTCS (leapfrog) for advection, whose
$|G|^{2} = C^{2}\sin^{2}\theta + 1 - C^{2}\sin^{2}\theta = 1$; the demonstration
measures an amplitude ratio of $1.0000000000$ over a full period at four
resolutions.

---

## ★4 — Pulse lag over 5 km

Carrier $\mathrm{PPW} = 8 \Rightarrow \theta = \pi/4$, $C = 0.5$:

$$\frac{v_g}{v} = \frac{\cos\theta}{\sqrt{1-C^{2}\sin^{2}\theta}}
= \frac{0.707107}{\sqrt{1-0.25\times0.5}} = \frac{0.707107}{0.935414}
= 0.755929.$$

Travel time at $v_g$: $5000/(0.755929\times2000) = 3.3072$ s; at $v$:
$5000/2000 = 2.5$ s. Lag $= 0.8072$ s, i.e. $32.3\,\%$ of the ideal travel time
— note this is larger than the $24.4\,\%$ of the demonstration because the
demonstration travelled $400$ m and quoted the lag as a fraction of the travel
time at the *group* speed. In per cent of the true travel time:
$0.8072/2.5 = 32.29\,\%$.

---

## ★5 — Upwind decay over 20 wavelengths

$r = C(1-C)(1-\cos\theta)$; $\theta = 2\pi/12 = 0.523599$,
$\cos\theta = 0.866025$, $1-\cos\theta = 0.133975$,
$C(1-C) = 0.75\times0.25 = 0.1875$.

$|G|^{2} = 1 - 2(0.1875)(0.133975) = 1 - 0.050241 = 0.949759$,
$|G| = 0.974556$ per step.

Steps per wavelength: $\Delta t$ for one wavelength of travel is
$\lambda/(a\,dt)$ with $dt = Ch/a$, so steps per wavelength
$= \lambda/(Ch) = 12/0.75 = 16$; 20 wavelengths gives 320 steps.

Amplitude remaining: $0.974556^{320} = e^{320\ln 0.974556}
= e^{320\times(-0.025774)} = e^{-8.2477} = 2.62\times10^{-4}$.

Equivalent diffusivity: $D_{\text{num}} = ah(1-C)/2 = 1500\times10\times0.25/2
= 1875\ \mathrm{m^{2}\,s^{-1}}$.

**Which is which:** $D_{\text{num}}$ is purely numerical — it has no physical
counterpart in $u_t + au_x = 0$, and it would be indistinguishable from a real
diffusivity if the medium were not known. The amplitude loss is the *consequence*
of that numerical diffusivity acting over the wave's path; the physics of the
teaching equation preserves amplitude exactly.

---

## ★6 — Anisotropy from the table

| PPW | 5-point anisotropy | 9-point anisotropy | reduction factor |
|---|---|---|---|
| 8 | $1.3036\,\%$ | $0.0268\,\%$ | 48.6 |
| 16 | $0.3224\,\%$ | $0.0017\,\%$ | 190 |

Cost: the nine-point operator has nine non-zeros per row against five for the
five-point operator — a factor $1.8$ in bandwidth (and in the work of an
efficient matrix-vector product, from five to nine multiplies per row), for a
reduction in angular error of two orders of magnitude at PPW $= 16$.

---

## ★7 — The 6-PPW policy

Measured table, $C = 0.5$: at $\mathrm{PPW} = 6$ the CTCS phase error would be
about $-17\,\%$ — far outside any target. Using the asymptotic law with the
correct constant from §3.1 of the lesson,

$$\varepsilon \approx \frac{(1-C^{2})2\pi^{2}}{3\,\mathrm{PPW}^{2}}
= \frac{14.804}{\mathrm{PPW}^{2}},$$

a $0.5\,\%$ target needs $\mathrm{PPW} = \sqrt{14.804/0.005} = 54.4$.

**The wrong assumption.** The policy assumes the *order* of the error determines
its size. Order two means the error falls as $h^{2}$, which says nothing about
the constant: at $\mathrm{PPW} = 6$ the constant is large enough that halving
$h$ only reduces the error to $4.3\,\%$. The measured table, not the order,
decides the policy.

---

## ★8 — Separating numerical from physical attenuation

**Observable.** The amplitude decay of a monochromatic wave as a function of
distance, measured on a line of receivers with the *same* carrier wavelength but
different grid spacings (i.e. different PPW).

**Predictions.** Physical attenuation with quality factor $Q$ decays as
$\exp(-\pi f x/(Qv))$: independent of $h$. Numerical dissipation of upwind
differencing decays as $|G|^{n}$ with
$|G|^{2} = 1-2C(1-C)(1-\cos\theta)$: at fixed PPW it is *independent of $h$* too
(because $\theta$ is fixed), so the discrimination needs a second axis: change
$C$ at fixed PPW, or change PPW at fixed physical wavelength. Numerical
dissipation scales as $D_{\text{num}}k^{2} = (ah(1-C)/2)k^{2}$, i.e. as
$(1-C)/\mathrm{PPW}$; physical attenuation has no $C$ dependence.

**Resolution to distinguish them.** Both effects are measurable separately at
$\mathrm{PPW}\ge20$, where the numerical term is $(1-C)/20$ of the physical one
for equal $Q$ — so measure at PPW $=20$ and $40$ and extrapolate to
$1/\mathrm{PPW} = 0$ to remove the numerical part.

**Controls.** (i) Change $C$ at fixed PPW: numerical attenuation must change,
physical must not. (ii) Set $C = 1$: the upwind scheme's numerical dissipation
vanishes exactly, leaving only the physical term — the cleanest control
available. A run at $C = 1$ and one at $C = 0.5$ therefore bracket the answer.
