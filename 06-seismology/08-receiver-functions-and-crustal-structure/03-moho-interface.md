---
id: 06-08-03
title: "Moho Discontinuity Depth and Sharpness"
level: advanced
prereqs: ["06-08-01", "06-08-02"]
tags: [seismology, moho, crustal-structure, receiver-functions, discontinuity]
---

# Moho Discontinuity Depth and Sharpness

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what the Moho is as a *seismological* definition, and why that
   definition differs from the petrological base of the crust.
2. **Derive** the depth error caused by an error in the reference slowness and
   by an error in the assumed velocity ratio, and quantify both.
3. **Derive** the amplitude response of a conversion to a transition zone of
   finite width, and explain why a "sharp" Moho is a statement about bandwidth.
4. **Distinguish** a primary conversion from a multiple using moveout, and
   explain how a multiple can masquerade as real structure.
5. **Report** a Moho depth with its velocity assumption and admitted range,
   rather than as a bare number.
6. **State** which conclusions about crustal evolution require sharpness
   information and which do not.

## Prerequisites

- [01 Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md).
- [02 H-K Stacking and Crustal Thickness Estimation](02-h-k-stacking.md).

## 1. Intuition: the Moho is a definition, not an object you can touch

The Moho (Mohorovičić discontinuity) is defined **seismologically**: the level at
which P-wave speed jumps from crustal to mantle values, with a corresponding
jump in S speed. It is not the same as the petrological crust–mantle boundary.
Underplated magmatic rock, serpentinised mantle, and a broad transition can all
place the two boundaries at different depths, and this mismatch is a real
scientific result rather than a technicality.

The consequence for this lesson is immediate: when a receiver function yields a
"depth to the Moho", it has measured the depth of a *seismic* contrast. Whether
that contrast coincides with the petrological Moho is a separate question, and a
receiver function alone cannot answer it. Throughout, we therefore say
"depth to the seismic Moho".

Two attributes of that contrast are of interest:

- **Depth**, from the Ps delay — but only as well as the assumed velocities
  allow (the H-k trade-off).
- **Sharpness** (or gradational character), from the *amplitude* of the
  conversion relative to the direct P.

All numbers quoted in this lesson are **SYNTHETIC** teaching values.

## 2. Precise definitions

### 2.1 The conversion delay, restated

$$\Delta t_{Ps} = H\left(q_s - q_p\right), \qquad
q_p = \sqrt{v_p^{-2}-p^{2}}, \quad q_s = \sqrt{v_s^{-2}-p^{2}}.$$

### 2.2 Transition width

Define the **transition width** $w_z$ as the thickness over which the velocity
(equivalently the impedance) changes from the crustal to the mantle value. A
width comparable to the shortest wavelength in the band makes the contrast
"gradational"; a width far smaller makes it "sharp". Because wavelength depends
on frequency, sharpness has meaning only relative to a stated frequency band.

### 2.3 Conversion amplitude

The conversion amplitude is the size of the Ps arrival relative to the direct P
on the same receiver function, after the deconvolution has removed the source.
It depends on the velocity contrast, the angle (through $p$), and the transition
width.

## 3. Derivations

### 3.1 Error in depth from an error in the reference slowness

Suppose the analyst removes moveout using a reference ray parameter
$p_{\text{ref}}$ but then converts the remaining delay to depth using
$p_{\text{true}}$. The apparent delay becomes $\Delta t(p_{\text{ref}})$, and
the inferred depth is

$$H_{\text{inf}} = \frac{\Delta t(p_{\text{ref}})}
{q_s(p_{\text{true}})-q_p(p_{\text{true}})}.$$

Differentiating the delay with respect to $p$ at fixed $H$,

$$\frac{\partial \Delta t}{\partial p}
= H\left(\frac{-p}{q_s} + \frac{p}{q_p}\right)
= H\,p\left(\frac{1}{q_p}-\frac{1}{q_s}\right) > 0 .$$

A small error $\delta p = p_{\text{ref}} - p_{\text{true}}$ therefore gives

$$H_{\text{inf}} = H + \frac{\delta p}{q_s-q_p}\,
\frac{\partial \Delta t}{\partial p},
\qquad\text{so}\qquad
\boxed{\;\delta H = \delta p\;\frac{H\,p}{q_s-q_p}
\left(\frac{1}{q_p}-\frac{1}{q_s}\right).}$$

*Numerical check (SYNTHETIC).* $H=32\ \mathrm{km}$, $v_p=6.00$,
$v_s=3.50\ \mathrm{km\,s^{-1}}$, $p=0.060\ \mathrm{s\,km^{-1}}$,
$\Delta t = 3.9632\ \mathrm{s}$, $q_p=0.155492$, $q_s=0.279343$. Then
$1/q_p - 1/q_s = 6.4312 - 3.5798 = 2.8514\ \mathrm{km\,s^{-1}}$, and with
$\delta p = -0.010\ \mathrm{s\,km^{-1}}$:

$$\delta H = (-0.010)\times\frac{32\times0.060}{0.123851}\times 2.8514
= (-0.010)\times 15.501 \times 2.8514 = -0.442\ \mathrm{km}.$$

The demonstration reports $-0.40\ \mathrm{km}$, the difference being that its
grid step is $0.005\ \mathrm{s\,km^{-1}}$ away from the reference ($0.055$ rather
than the exact $0.050$ used here). **A $0.01\ \mathrm{s\,km^{-1}}$ error in the
reference slowness is worth about $0.4\ \mathrm{km}$ of apparent Moho depth** for
this model — small compared with the velocity-ratio error of Section 3.2, but
not negligible. Note that $H$ appears explicitly: the same $\delta p$ hurts a
thick crust more than a thin one.

### 3.2 Error in depth from an error in $k$

This is the dominant error. From Section 3.2 of lesson 01,

$$\frac{\mathrm{d}H}{\mathrm{d}k}\bigg|_{\Delta t}
= -\frac{H^{2}}{\Delta t}\,\frac{k}{v_p^{2}q_s}.$$

*Numerical check.* With the numbers above, $H^2/\Delta t = 258.4\ \mathrm{km}$,
$k/(v_p^{2}q_s) = 0.1704$, giving $-44.0\ \mathrm{km}$ per unit $k$. A $5\%$
error in $k$ (from $1.714$ to $1.800$) therefore moves the depth by about
$-3.8\ \mathrm{km}$, i.e. $-12\%$. The demonstration's exact computation gives
$H_{\text{inf}} = 28.62\ \mathrm{km}$ for $k_{\text{try}} = 1.80$, a
$-3.38\ \mathrm{km}$ ($-10.6\%$) error. Agreement is good; the residual reflects
the curvature neglected by the derivative.

**Conclusion.** Depth to the Moho from a receiver function is only as good as the
assumed $k$. This is why joint inversion with a $k$-sensitive measurement
(lesson 05) is not a luxury.

### 3.3 Amplitude response of a transition zone

Consider a P wave crossing a transition in which the S velocity (and hence the
impedance) varies over a depth $w_z$. In the weak-scattering, single-conversion
approximation the converted amplitude is proportional to the Fourier component
of the vertical gradient of the velocity at the vertical wavenumber of the
wave. Write the vertical slowness of the S leg as $q_s$; the vertical phase
change across the transition is $\omega w_z q_s = 2\pi f\,w_z q_s$. If the
gradient is a boxcar of thickness $w_z$ (a linear ramp in velocity), its
transform is a sinc, and the amplitude factor is

$$\boxed{\;A(f,w_z) = \operatorname{sinc}\!\left(\pi f\,w_z q_s\right)
= \frac{\sin\!\left(\pi f w_z q_s\right)}{\pi f w_z q_s}.}$$

*Derivation of the sinc.* Put $s$ for depth inside the ramp. The gradient
$g(s)$ is constant over $0\le s\le w_z$ and zero elsewhere, so

$$\int_{0}^{w_z} g_0\,e^{\,i\omega q_s s}\,\mathrm{d}s
= g_0\,\frac{e^{\,i\omega q_s w_z}-1}{i\omega q_s}
= g_0 w_z\,e^{\,i\omega q_s w_z/2}\,
\frac{\sin(\omega q_s w_z/2)}{\omega q_s w_z/2}.$$

With $\omega = 2\pi f$ this is $g_0 w_z\,e^{i\pi f w_z q_s}\operatorname{sinc}(\pi f w_z q_s)$:
an amplitude factor that starts at 1 for $w_z=0$ and rolls off as the transition
widens.

*Numerical check.* For $q_s = 0.279343\ \mathrm{s\,km^{-1}}$ and a dominant
frequency $f = 0.30\ \mathrm{Hz}$ (a **CHOSEN** band parameter):

| $w_z$ (km) | $\Delta\tau = w_z q_s$ (s) | $A$ |
|---|---|---|
| 0.5 | 0.140 | 0.997 |
| 2.0 | 0.559 | 0.954 |
| 5.0 | 1.397 | 0.735 |
| 8.0 | 2.235 | 0.408 |

The amplitude falls to $2/\pi = 0.637$ at $\pi f w_z q_s = \pi/2$, i.e.
$w_z = 1/(2f q_s) = 1/(2\times0.30\times0.279343) = 5.97\ \mathrm{km}$. These
are the numbers the demonstration prints. The lesson: **a receiver-function
"sharp Moho" means a contrast thinner than a few kilometres at the frequency
used to measure it** — not a statement about the Earth independent of bandwidth.

### 3.4 Multiples and spurious structure

A conversion at the Moho is followed in time by multiples of the same interface.
Their delays are $t_{PpPs} = H(q_s+q_p)$ and $t_{PpSs} = 2Hq_s$. A naive reading
of a receiver function — "every peak is a discontinuity" — converts these into
spurious interfaces, usually deeper than the true Moho.

The diagnostic is moveout. The demonstration measures
$\mathrm{d}t/\mathrm{d}(p^{2})$:

| phase | slope (s per $(\mathrm{s\,km^{-1}})^{2}$) |
|---|---|
| Ps (primary) | $+45.7$ |
| PpPs (multiple) | $-160.2$ |
| PpSs + PsPs (multiple) | $-114.5$ |

A primary conversion's delay **increases** with $p^{2}$; the multiples'
delays **decrease**. Stacking a candidate arrival with the wrong moveout sign
therefore *destroys* it rather than enhancing it. Amplitude alone cannot make
this distinction; moveout can.

## 4. Physical interpretation

- **Depth is a trade-off.** $H$ and $k$ move together; a depth without a stated
  $k$ (or a stated jointly-inverted $k$) is incomplete.
- **Sharpness is a frequency statement.** A transition that looks sharp at
  $0.3\ \mathrm{Hz}$ looks gradational at $2\ \mathrm{Hz}$ if its width exceeds
  the shorter wavelength.
- **Multiples are not noise.** They are part of the signal, they carry
  information, and they are the main source of spurious "deep interfaces" in
  careless interpretation.
- **The seismic Moho is a definition.** A depth to the seismic Moho is a
  measurement of a velocity contrast, and the claim that it is the petrological
  Moho is an *interpretation* requiring additional evidence.

### 4.1 Detection versus resolution of the Moho

These are different claims and they are routinely confused.

- **Detection** asks: is there a contrast at all? The Ps arrival stands above the
  noise, and its moveout matches a primary. Detection is often robust even when
  the contrast is thin or gradational, because the receiver function is stacked
  over many events. A thin transition merely reduces the amplitude.
- **Resolution** asks: how precisely are depth and sharpness determined? The
  answer is the ridge (in depth) and the sinc roll-off (in width), and it is
  much weaker than detection. A Moho can be *detected* with a handful of good
  events but *resolved* in depth only to a few kilometres.

The demonstration makes the asymmetry concrete. A $5\ \mathrm{km}$ transition
reduces the conversion amplitude to $0.735$ of a sharp interface at
$f=0.30\ \mathrm{Hz}$ — a $26\%$ loss, easily detected above noise — yet the same
interface still produces a clear Ps arrival whose delay fixes the depth to the
ridge width. Detection survives a loss of amplitude that would make a precise
width measurement hopeless. Report which claim you are making.

## 5. Assumptions

1. Single-layer, horizontal, isotropic structure. A two-layer crust with a
   strong mid-crustal contrast adds extra multiples.
2. The transition is thin compared with the layer, so the ramp may be treated as
   a perturbation at a single depth.
3. Weak-contrast, single-scattering for the amplitude derivation; it fails for a
   very large velocity jump.
4. The receiver-function amplitudes are preserved across events.
5. The dominant frequency $f$ used to convert amplitude to width is stated and
   justified; it is not the same as the Nyquist frequency.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $w_z$ | km | |
| $q_s$ | $\mathrm{s\,km^{-1}}$ | |
| $\pi f w_z q_s$ | dimensionless | $\mathrm{s^{-1}\cdot km\cdot s\,km^{-1}}$ |
| $\Delta t$, $\Delta\tau$ | s | |
| $A$ | dimensionless | amplitude ratio |

The argument of the sinc must be dimensionless; if a computation produces units
of seconds, the frequency has been omitted.

## 7. Worked examples

### Example 1 — depth with a stated assumption

A receiver function gives $\Delta t_{Ps} = 3.60\ \mathrm{s}$ at
$p = 0.055\ \mathrm{s\,km^{-1}}$. Assume $v_p = 6.20\ \mathrm{km\,s^{-1}}$ and
$k = 1.75$.

$v_s = 3.543\ \mathrm{km\,s^{-1}}$;
$q_p = \sqrt{0.026017-0.003025} = 0.151632$;
$q_s = \sqrt{0.079680-0.003025} = 0.276854$;
$H = 3.60/0.125222 = 28.75\ \mathrm{km}$.

State the joint assumption explicitly: "28.8 km assuming $v_p = 6.20$ and
$k = 1.75$". With $k = 1.70$ the answer would be $30.8\ \mathrm{km}$.

### Example 2 — width from an amplitude ratio

Suppose the Moho conversion amplitude is measured to be $0.74$ of what a sharp
interface of the same contrast would give, at $f = 0.30\ \mathrm{Hz}$ and
$q_s = 0.28\ \mathrm{s\,km^{-1}}$. Solve
$\operatorname{sinc}(\pi f w_z q_s) = 0.74$. The first root is
$\pi f w_z q_s \approx 1.30$, so

$$w_z = \frac{1.30}{\pi\times0.30\times0.28} = 4.9\ \mathrm{km}.$$

The transition is about $5\ \mathrm{km}$ thick **at this frequency**. At
$f = 1.0\ \mathrm{Hz}$ the same interface would give
$\operatorname{sinc}(\pi\times1.0\times4.9\times0.28) = \operatorname{sinc}(4.31)
= -0.216$ — a small, sign-reversed arrival. Reporting the width without the
frequency is therefore incomplete.

### Example 3 — a multiple misread as a deep interface

Take the demonstration's SYNTHETIC model, $H = 30\ \mathrm{km}$, $k = 1.726$,
$p = 0.055\ \mathrm{s\,km^{-1}}$. The PpPs multiple appears at
$t_{PpPs} = H(q_s+q_p) = 12.5\ \mathrm{s}$. If an analyst interprets that peak as
a Ps conversion at the same $p$,

$$H_{\text{spurious}} = \frac{12.5}{q_s-q_p}
= \frac{12.5}{0.120} \approx 104\ \mathrm{km},$$

a nonsense depth for a Moho but a plausible-looking arrival. Its moveout slope is
$-160\ \mathrm{s}$ per $(\mathrm{s\,km^{-1}})^{2}$, the opposite sign to a
primary, which is how it is identified.

### Example 4 — why stacking many events sharpens the depth but not the ridge

Suppose $N$ independent events each give a Ps delay with uncertainty
$\sigma_0 = 0.10\ \mathrm{s}$. Stacking reduces the delay uncertainty to
$\sigma_0/\sqrt{N}$: with $N=25$, $\sigma = 0.02\ \mathrm{s}$, and the depth
uncertainty from timing alone becomes
$\sigma_H = \sigma/(q_s-q_p) = 0.02/0.123851 = 0.16\ \mathrm{km}$. But the
*ridge* — the trade-off between $H$ and $k$ — does not shrink with $N$, because
it is not a noise effect: every event lies on the same ridge. The demonstration's
noise Monte Carlo gives an $H$ scatter of $0.14\ \mathrm{km}$, consistent with
$\sigma_H=0.16\ \mathrm{km}$, while the 95% set spans $1.50\ \mathrm{km}$. **More
events make a precise answer to the wrong question.** Breaking the ridge requires
a *different* measurement (Section 5.1) or an assumption about $k$.

## 8. Python demonstration

`code/moho_interface_demo.py` prints:

1. the depth inferred from delays computed at five reference slownesses, with
   depth errors from $-0.40$ to $+0.49\ \mathrm{km}$;
2. the two-part moveout study: a wrong reference shifts the stack
   (identical peak amplitude for every $p_{\text{ref}}$), while a wrong velocity
   biases the depth — $k_{\text{try}} = 1.55$ inflates $H$ to $41.41\ \mathrm{km}$
   against a true $32.00\ \mathrm{km}$;
3. the transition-width table of Section 3.3;
4. the moveout slopes of Section 3.4.

Every number is reproducible from the printed inputs; nothing is copied from a
published measurement.

## 9. Exercises

Full sets are in
[`exercises/03-moho-interface-exercises.md`](./exercises/03-moho-interface-exercises.md)
and
[`exercises/03-moho-interface-solutions.md`](./exercises/03-moho-interface-solutions.md).

- **★** Convert a delay of $4.1\ \mathrm{s}$ at $p = 0.06\ \mathrm{s\,km^{-1}}$
  to a depth for $k = 1.72$, $v_p = 6.3\ \mathrm{km\,s^{-1}}$.
- **★★** Derive the sinc response of Section 3.3 from the boxcar gradient.
- **★★** A peak appears at $14\ \mathrm{s}$ with negative moveout. Is it a deep
  converter? Justify with a calculation.
- **★★★** Design a bandwidth study: for a $5\ \mathrm{km}$ transition, compute
  the amplitude at $0.2$, $0.5$, $1.0$ and $2.0\ \mathrm{Hz}$ and state at which
  frequencies the interface would be called sharp.

## 10. Common mistakes

1. **Quoting a Moho depth with no velocity assumption.** The depth is
   conditional; the assumption is part of the result.
2. **Calling a transition "sharp" without a frequency.** Sharpness is
   bandwidth-relative.
3. **Treating every peak as a discontinuity.** Multiples and crustal
   reverberations are common; check the moveout.
4. **Confusing the seismic and petrological Moho.** They can differ, and the
   receiver function measures a velocity contrast.
5. **Using the peak's width as the transition width directly.** Pulse width
   convolves the source, the deconvolution stabiliser and the true gradient; the
   amplitude ratio is the more robust quantity.
6. **Reporting the depth of the seismic Moho as the base of the crust without
   qualification.** The two can differ, and the difference is often the
   interesting result.

## 11. Real-world applications

- **Continental crustal structure and evolution.** Moho depth and character are
  used as constraints on crustal growth, underplating and orogenic history; the
  sharpness question is exactly what distinguishes a magmatic underplate from a
  tectonic boundary.
- **Isostasy and gravity modelling.** A depth to the seismic Moho is an input to
  Airy-type isostatic calculations; an unacknowledged $\pm 5\%$ velocity error in
  $k$ propagates into the density model.
- **Basin and resource studies.** Depth to a strong shallow contrast follows the
  same logic, with poorer separation of multiples.
- **Planetary interiors.** On Mars and the Moon, single-station H-k and
  sharpness arguments constrain crustal structure where no other measurement
  exists — which makes reporting the ridge essential rather than optional.

## 12. Further reading

- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. The reflection/transmission and
  conversion coefficients, and the weak-contrast approximations used in
  Section 3.3.
- **Shearer, P. M. (2019). *Introduction to Seismology* (3rd ed.). Cambridge
  University Press.** Level: intermediate to advanced. Discontinuity imaging and
  the resolution arguments.
- **Stein, S., & Wysession, M. (2003). *An Introduction to Seismology,
  Earthquakes, and Earth Structure*. Blackwell.** Level: intermediate. Crustal
  structure and the seismic definition of the Moho.
- **Zhu, L., & Kanamori, H. (2000).** *Journal of Geophysical Research*, 105(B2),
  2969–2980. Level: research. The stacking method that supplies the depth.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Confirm current editions through
> your library.

## 13. Related lessons

- [01 Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md).
- [02 H-K Stacking and Crustal Thickness Estimation](02-h-k-stacking.md).
- [05 Joint Inversion of Receiver Functions and Surface Waves](05-joint-inversion-rf.md).
- [06-09-05 AVO/AVA Analysis and Its Assumptions](../09-reflection-seismology/05-amplitude-vs-offset.md) —
  the full reflection-coefficient algebra behind conversion amplitudes.
- [02-11-03 Seismic Parameter Relations](../../02-physics/11-physics-of-earths-interior-and-atmosphere/03-seismic-parameter-relations.md) —
  how $v_p$, $v_s$ and $k$ relate in real materials.

## 14. Self-assessment checklist

- [ ] I can state the seismic (not petrological) definition of the Moho.
- [ ] I can compute the depth error from a stated $k$ error.
- [ ] I can derive the sinc amplitude response of a transition zone.
- [ ] I can explain why "sharp" requires a stated frequency.
- [ ] I can identify a multiple from its moveout sign with a calculation.
- [ ] I can write a one-sentence defensible Moho result including its assumptions.
