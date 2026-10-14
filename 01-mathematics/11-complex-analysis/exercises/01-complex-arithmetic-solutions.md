# Solutions — 01-11-01 Complex Numbers, Polar Form and Argand Diagrams

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Where a numeric answer is given, it was computed
> and verified rather than estimated by hand.

Throughout, the principal argument is taken in $(-180^{\circ}, 180^{\circ}]$;
every phase quoted is in that interval unless stated otherwise.

---

## ★1 — Rectangular to polar

Formula: $r = \sqrt{x^{2}+y^{2}}$, $\theta = \operatorname{atan2}(y,x)$.

| | $z$ | $r$ | $\theta$ |
|---|---|---|---|
| (a) | $2 - 2i$ | $\sqrt{8} = 2.828427$ | $-45.000^{\circ}$ |
| (b) | $-3 + 4i$ | $5$ | $126.870^{\circ}$ |
| (c) | $-1 - i\sqrt3$ | $2$ | $-120.000^{\circ}$ |
| (d) | $5i$ | $5$ | $90.000^{\circ}$ |

**Reasoning checks.**

- (a) The point is in the fourth quadrant, so the argument must be negative; the
  reference angle is $\arctan(2/2) = 45^{\circ}$.
- (b) $\sqrt{9+16} = 5$ exactly: this is the 3–4–5 triangle, which is why $5$ is
  worth recognising. Second quadrant, so $\theta = 180^{\circ} -
  \arctan(4/3) = 180^{\circ} - 53.130^{\circ} = 126.870^{\circ}$.
- (c) $r = \sqrt{1+3} = 2$ exactly. Third quadrant, reference angle
  $\arctan(\sqrt3) = 60^{\circ}$, so $\theta = -180^{\circ}+60^{\circ} =
  -120^{\circ}$. Note that $240^{\circ}$ is the same angle but is **not** the
  principal value.
- (d) Purely imaginary positive: $\theta = 90^{\circ}$.

**The trap.** For (c), writing $60^{\circ}$ because $\arctan(\sqrt3) = 60^{\circ}$
is the commonest error. The four-quadrant arctangent is required, and the sign of
the imaginary part is what distinguishes $-120^{\circ}$ from $+120^{\circ}$.

---

## ★2 — Multiplication as rotation and scaling

Polar route:

$$\bigl(3e^{i40^{\circ}}\bigr)\bigl(2e^{-i25^{\circ}}\bigr)
= 6\,e^{i(40^{\circ}-25^{\circ})} = 6e^{i15^{\circ}}.$$

Rectangular check:

$$6(\cos 15^{\circ} + i\sin15^{\circ}) = 5.795555 + 1.552914i,$$

and multiplying the two rectangular forms directly gives the same
$5.795555+1.552914i$.

**Which is faster.** The polar route: two multiplications (moduli) and one
addition (arguments). The rectangular route needs four products, two sums and the
identity $i^{2} = -1$. The polar form wins whenever the inputs are already in
polar form — which is the normal case for measured amplitudes and phases.

---

## ★3 — Division by rationalising

$$\frac{4+3i}{1-2i} = \frac{(4+3i)(1+2i)}{1^{2}+2^{2}}
= \frac{4 + 8i + 3i + 6i^{2}}{5}
= \frac{4 + 11i - 6}{5} = \frac{-2 + 11i}{5}
= -0.4 + 2.2i .$$

Modulus check:

$$\left|\frac{z_{1}}{z_{2}}\right| = \frac{|z_{1}|}{|z_{2}|}
= \frac{5}{\sqrt5} = \sqrt5 = 2.236068,$$

and $|-0.4+2.2i| = \sqrt{0.16+4.84} = \sqrt5$. ✓

**Why the conjugate works.** Multiplying by $\bar z_{2}/z_{2}$ replaces the
denominator by the *real* number $z_{2}\bar z_{2} = |z_{2}|^{2}$, so the division
becomes a real division.

---

## ★4 — Powers and roots

**Power.** $|1+i| = \sqrt2$ and $\arg(1+i) = 45^{\circ}$, so

$$(1+i)^{8} = (\sqrt2)^{8}e^{i(8\times45^{\circ})}
= 2^{4}e^{i360^{\circ}} = 16 .$$

Direct expansion gives the same $16 + 0i$.

**Roots of $8i$.** Write $8i = 8e^{i(\pi/2+2\pi k)}$, so

$$z_{k} = 2\exp\!\left[i\left(\frac{\pi/2+2\pi k}{3}\right)\right],
\qquad k = 0,1,2,$$

giving

| $k$ | $z_{k}$ | in rectangular form |
|---|---|---|
| 0 | $2e^{i30^{\circ}}$ | $\sqrt3 + i = 1.732051+1.000000i$ |
| 1 | $2e^{i150^{\circ}}$ | $-\sqrt3 + i = -1.732051+1.000000i$ |
| 2 | $2e^{i270^{\circ}}$ | $-2i$ |

**Sum.** $(\sqrt3 - \sqrt3 + 0) + (1+1-2)i = 0$. ✓ The three roots form an
equilateral triangle on the circle of radius $2$, and their vector sum is zero.

**A remark on care.** The roots are the vertices of the regular $n$-gon inscribed
in the circle $|z| = r^{1/n}$; the angles differ by $2\pi/3 = 120^{\circ}$, not
by $90^{\circ}$ or $60^{\circ}$. Drawing the triangle first prevents most errors
of this kind.

---

## ★5 — Adding three phasors

**(a)** Write each oscillation as $a\cos(\omega t - \phi) =
\operatorname{Re}[Ae^{-i\omega t}]$ with $A = ae^{-i\phi}$:

| component | amplitude | lag $\phi$ | phasor $A$ |
|---|---|---|---|
| $v_{1}$ | 3 | $0^{\circ}$ | $3.000000 + 0.000000i$ |
| $v_{2}$ | 4 | $60^{\circ}$ | $2.000000 - 3.464102i$ |
| $v_{3}$ | 2 | $-45^{\circ}$ | $1.414214 + 1.414214i$ |
| **sum** | — | — | $6.414214 - 2.049888i$ |

**(b)** Amplitude $= |6.414214 - 2.049888i| = 6.733808$; phase
$= \arg = -17.723113^{\circ}$, so the lag is
$\phi = +17.723^{\circ}$ and

$$v_{1}+v_{2}+v_{3} = 6.733808\cos(\omega t + 17.723^{\circ}).$$

**(c)** Because the common factor $e^{-i\omega t}$ cancels in the sum: the
result is the same superposition whatever the frequency, and only the amplitude
and phase depend on the phasors.

**Sign check.** With $a\cos\omega t = \operatorname{Re}[Ae^{-i\omega t}]$ and
$A = ae^{-i\phi}$, a *lag* of $\phi$ gives $\arg A = -\phi$. The sum's argument
is $-17.723^{\circ}$, i.e. a *lead* of $17.7^{\circ}$; equivalently a lag of
$-17.7^{\circ}$. Writing the answer as $\cos(\omega t - \phi)$ with
$\phi = +17.7^{\circ}$ and calling it a lag is a sign error. State the form of
the sinusoid and the sign convention together.

---

## ★6 — A series $R$–$C$ network

**(a)** $Z(\omega) = R + 1/(i\omega C) = R - i/(\omega C)$. At
$f = 1000$ Hz, $\omega = 6283.185307$ rad s⁻¹ and
$1/(\omega C) = 1591.549431\ \Omega$, so

$$Z = 1000.000000 - 1591.549431i\ \Omega, \qquad
|Z| = 1879.635494\ \Omega, \qquad \arg Z = -57.858092^{\circ}.$$

**(b)** The corner frequency is
$f_{c} = 1/(2\pi RC) = 1/(2\pi\times10^{3}\times10^{-7}) = 1591.549431$ Hz, where
$\omega_{c} = 1/(RC)$ and $|Z| = \sqrt{R^{2}+R^{2}} = \sqrt2R = 1414.213562\
\Omega$ with $\arg Z = -45^{\circ}$ exactly. The three facts
($\sqrt2R$, $-45^{\circ}$, equal resistive and reactive parts) are one fact.

**(c)** $|Z| = 1500\ \Omega$ requires
$\sqrt{R^{2}+X^{2}} = 1500$ with $X = 1/(\omega C)$, so
$X = \sqrt{1500^{2}-1000^{2}} = 1118.033989\ \Omega$ and

$$f = \frac{1}{2\pi X C} = 1423.525087\ \mathrm{Hz}, \qquad
\arg Z = -\arctan\!\left(\frac{1118.033989}{1000}\right) = -48.189685^{\circ}.$$

**(d)** The error is dropping the reactive term. $i = v/R$ holds only for a
purely resistive circuit. The correct statement is that the *current* leads the
voltage by $\arctan(X_{C}/R)$, which is $57.9^{\circ}$ at 1 kHz and tends to
$90^{\circ}$ at low frequency — the circuit behaves as a capacitor there. In
phasor language, $I = V/Z$ and the phase of $I$ is the negative of the phase of
$Z$.

---

## ★7 — The driven oscillator

**(a)** With $m=1$, $c=2$, $k=100$:

$$Z(\omega) = m(\omega_{0}^{2}-\omega^{2}) + ic\omega = (100-\omega^{2}) + 2i\omega,
\qquad \omega_{0} = 10 .$$

| $\omega$ | $Z$ | $|Z|$ | amplitude $F_{0}/|Z|$ with $F_{0}=1$ |
|---|---|---|---|
| 8 | $36 + 16i$ | $39.395431$ | $0.025384$ |
| 10 | $0 + 20i$ | $20$ | $0.050000$ |
| 12 | $-44 + 24i$ | $50.119856$ | $0.019952$ |

**(b)** The amplitude is stationary where the phase is $-90^{\circ}$, i.e. where
the real part of $Z$ vanishes — which is exactly $\omega = \omega_{0} = 10$ here.
More generally the *amplitude* peak occurs where
$\mathrm{d}|Z|^{2}/\mathrm{d}\omega = 0$, which gives
$\omega_{\text{peak}}^{2} = \omega_{0}^{2} - c^{2}/(2m^{2})$, so

$$\omega_{\text{peak}} = \sqrt{100 - 4/2} = \sqrt{98} = 9.899495\ \mathrm{rad\,s^{-1}} .$$

At $\omega = \omega_{0}$ the phase is exactly $-90^{\circ}$ but the amplitude is
not quite maximal. The two criteria differ whenever the damping is non-zero, and
they coincide only in the limit $c\to0$.

**(c)** The response lags the force by $\arg Z$:

- $\omega \ll \omega_{0}$: $Z \approx k = 100$, real and positive, so the response
  is **in phase** with the force (stiffness-controlled).
- $\omega = \omega_{0}$: $Z = 2i\omega_{0}$, purely imaginary, so the response
  **lags by exactly $90^{\circ}$**.
- $\omega \gg \omega_{0}$: $Z \approx -m\omega^{2}$, real and negative, so the
  response **lags by $180^{\circ}$** — the mass cannot follow the force and
  responds in the opposite direction (inertia-controlled).

---

## ★8 — Sets in the Argand diagram

**(a)** $|z-(3-2i)| = 4$: a **circle**, centre $3-2i$, radius $4$.

**(b)** $|z-1| = |z+i|$: the locus of points equidistant from $1$ and $-i$, i.e.
the **perpendicular bisector** of the segment joining them — a straight line.
Explicitly, squaring gives $(x-1)^{2}+y^{2} = x^{2}+(y+1)^{2}$, hence
$-2x+1 = 2y+1$ and $y = -x$.

**(c)** $\operatorname{Re}z > 2$: a **half plane**, not a line; the boundary is
the vertical line $x = 2$, excluded.

**(d)** $|z|^{2} = z+\bar z$. Since $z + \bar z = 2x$ and $|z|^{2} = x^{2}+y^{2}$,
the equation is $x^{2}+y^{2} = 2x$, i.e. $(x-1)^{2}+y^{2} = 1$: a **circle**,
centre $1$, radius $1$. This is the standard way a circle through the origin is
written in complex form, and it is worth recognising: $|z|^{2} = 2\operatorname{Re} z$
and $|z-a| = r$ are the same kind of object.

---

## ★★9 — Beats, and why one phasor is not enough

**(a)** A phasor is the coefficient of a *single* $e^{-i\omega t}$. With two
frequencies the sum is

$$\operatorname{Re}\bigl[A_{1}e^{-i\omega_{1}t}\bigr] +
\operatorname{Re}\bigl[A_{2}e^{-i\omega_{2}t}\bigr],$$

and no single factor $e^{-i\omega t}$ can be extracted: there is no common time
dependence to cancel. A phasor describes a steady state at one frequency; a sum
of two frequencies is not a steady state in that sense — its amplitude varies in
time.

**(b)** With the identity $\cos A + \cos B = 2\cos\frac{A-B}{2}
\cos\frac{A+B}{2}$:

$$\cos\omega_{1}t + \cos\omega_{2}t
= 2\cos\left(\frac{\Delta\omega}{2}t\right)
\cos\left(\bar\omega t\right), \qquad
\bar\omega = \frac{\omega_{1}+\omega_{2}}{2}, \quad
\Delta\omega = \omega_{2}-\omega_{1}.$$

The **envelope** is $2|\cos(\Delta\omega\,t/2)|$, with period
$T_{\text{env}} = 2\pi/|\Delta\omega|$; the **carrier** is at the mean frequency
$\bar\omega$. The sum is a single tone at $\bar\omega$ whose amplitude is
modulated.

**(c)** Two arrivals of the *same* wavelet separated by $\Delta t = 20$ ms add in
the frequency domain as $W(f)\bigl(1 + e^{-2\pi i f\Delta t}\bigr)$, whose
magnitude $2|W(f)||\cos(\pi f\Delta t)|$ has **nulls** wherever
$f\Delta t = k + \tfrac12$:

$$f = \frac{k+\tfrac12}{\Delta t} = 25,\ 75,\ 125,\ \dots\ \mathrm{Hz}.$$

The modulation period in the frequency domain is therefore
$1/\Delta t = 50\ \mathrm{Hz}$, and the first null sits at
$1/(2\Delta t) = 25$ Hz, coinciding with the dominant frequency $25$ Hz. That
coincidence is exactly why the delay is *detectable*: the reverberation removes
the very frequency the wavelet is strongest at. This is the standard argument
for detecting a peg-leg multiple from a periodic comb in the amplitude spectrum,
and the estimator is $\Delta t = 1/(\text{null spacing})$. Note what the time
domain shows: **two** arrivals 20 ms apart. The bell-shaped "beat" picture of
part (b) belongs to two tones of different frequencies; here the frequencies are
the same and it is the *phase* that differs with frequency.

**(d)** A phasor description of the **filter** still applies, because a linear
time-invariant filter is characterised by $H(\omega)$ at every frequency, and it
acts on each frequency independently: the output is
$\operatorname{Re}[A_{1}H(\omega_{1})e^{-i\omega_{1}t}] +
\operatorname{Re}[A_{2}H(\omega_{2})e^{-i\omega_{2}t}]$. What fails is
representing the *sum* by one phasor, not representing the *filter* by one
transfer function. This distinction is exactly the difference between a signal
and a system.

---

## ★★★10 — A magnetotelluric impedance

**(a)** With $\omega = 2\pi/100 = 0.062832\ \mathrm{rad\,s^{-1}}$ and
$\mu_{0} = 4\pi\times10^{-7}$:

$$|Z| = \sqrt{2.80^{2}+1.20^{2}}\times10^{-3} = 3.046309\times10^{-3},$$

$$\rho_{a} = \frac{|Z|^{2}}{\mu_{0}\omega}
= \frac{9.279999\times10^{-6}}{7.895683\times10^{-8}}
= 117.533\ \Omega\,\mathrm{m},$$

$$\phi = \arctan\!\left(\frac{1.20}{2.80}\right) = 23.198591^{\circ} .$$

The answer is consistent with the half-space relation
$|Z| = \sqrt{\mu_{0}\omega\rho}$, which inverts to $\rho = 117.5\ \Omega$ m — a
plausible crustal value, which is the check that the units have been handled
correctly. **This unit check is not optional in magnetotellurics**: impedances are
often quoted with $E$ in mV km⁻¹ and $H$ in nT, which differ from SI by
$10^{-6}$ and $10^{-9}$ respectively, so a "117 Ω m" from one route and "1.2 Ω m"
from another are frequently the same data.

**(b)** The phase is $+23.2^{\circ}$, inside $(0^{\circ},90^{\circ})$, which is
what a resistive (or at least non-inductive) half-space gives: the electric field
leads the magnetic field by between $0^{\circ}$ and $45^{\circ}$ for a
conducting earth, approaching $45^{\circ}$ for an infinite half-space and
decreasing towards $0^{\circ}$ when a resistive layer dominates the response.

**A negative impedance phase** means the magnetic field lags the electric field —
physically, a strongly *inductive* response, which occurs over a very good
conductor where the induction of the conductor dominates, or as a sign of
noise/static distortion. It is diagnostic, and it is the reason the phase is
quoted as a signed quantity rather than an absolute value.

**(c)** A $180^{\circ}$ rotation of the measurement axes multiplies the impedance
by $-1$ (the field components reverse), which adds $\pm180^{\circ}$ to the
argument. In the principal-axis convention the phase is reported in
$(0^{\circ},90^{\circ})$ by choosing the axis signs so that
$\operatorname{Re}Z > 0$; the value $23.2^{\circ}$ is then identical, not merely
related. If two authors report $\phi$ and $\phi+180^{\circ}$, one of them is
working in the "unrotated" convention, and the physical interpretation of the
sign must be stated with the number or the number is not interpretable.

**(d)** Two independent checks:

1. **Continuity in frequency.** The impedance phase is a smooth function of
   period for a layered earth, changing by tens of degrees over a decade of
   period, never by $360^{\circ}$. Choose the branch that makes it continuous.
2. **The apparent-resistivity consistency.** $\rho_{a}$ depends only on $|Z|$,
   which is insensitive to the branch of the phase; but the *response function*
   (the impedance as a complex number) must reproduce the measured fields, so
   recompute $E$ from $Z$ and $H$ at every period and check the residual. A
   $2\pi$ error in a reported phase is invisible in $\rho_{a}$ and fatal in an
   inversion, which is why the phase is usually reported modulo $360^{\circ}$
   together with the amplitudes.

---

## Self-assessment: have you actually learned this?

You have if you can, without notes:

- convert between rectangular and polar form, including the correct quadrant;
- explain in one sentence why polar form makes multiplication easy and why
  rectangular form is still needed for addition;
- write an oscillation as a phasor and give the amplitude and phase of a sum of
  phasors, keeping the lag/lead sign consistent;
- write the impedance of an $R$–$C$ network and say which of the modulus and the
  argument carries the amplitude response and which carries the phase;
- state the resonance condition of a damped driven oscillator and say whether it
  is the amplitude peak or the $90^{\circ}$ phase point;
- name one physical quantity whose interpretation depends on the branch of a
  square root or a logarithm.

If any of those is not automatic, re-read Sections 2 to 5 of
[the lesson](../01-complex-arithmetic.md) and redo ★5 and ★6.
