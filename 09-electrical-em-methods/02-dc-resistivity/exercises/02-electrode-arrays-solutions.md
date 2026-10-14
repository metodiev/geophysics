# Solutions — 09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole

> **Read after attempting the exercises.** Lesson:
> [02 Electrode Arrays](../02-electrode-arrays.md).

---

## ★1 — Schlumberger

$$k = \frac{\pi(L^{2}-l^{2})}{4l}
= \frac{\pi(1600-16)}{16} = \frac{\pi\times1584}{16} = 311.02\ \mathrm{m}.$$

$$\Delta V = \frac{\rho_a I}{k} = \frac{120\times0.1}{311.02}
= 0.03858\ \mathrm{V} = 38.6\ \mathrm{mV}.$$

---

## ★2 — Pole-dipole and dipole-dipole

Pole-dipole, $n = 2$, $a = 5$: $k = 2\pi(n+1)(n+2)a = 2\pi\times3\times4\times5
= 376.99\ \mathrm{m}$.

Dipole-dipole, $n = 2$, $a = 5$: $k = \pi n(n+1)(n+2)a
= \pi\times2\times3\times4\times5 = 376.99\ \mathrm{m}$.

They are equal here because $2\pi(n+1)(n+2) = \pi n(n+1)(n+2)$ only if $n = 2$ —
a coincidence of this exercise that is worth noticing: the pole-dipole array is
*not* generally equal to the dipole-dipole one, and the general relation is
$k_\text{PD}/k_\text{DD} = 2(n+1)(n+2)/[n(n+1)(n+2)] \times\ldots$ — check by
substituting: $k_\text{PD} = 2\pi(n+1)(n+2)a$ against
$k_\text{DD} = \pi n(n+1)(n+2)a$, ratio $2/n$. So for $n = 2$ the ratio is 1 (as
computed), for $n = 5$ it is 0.4. **The two arrays coincide numerically only at
$n = 2$.**

---

## ★3 — Signal ratio

Wenner $a = 5$: $k = 31.4159$ m, $\Delta V = 100\times0.1/31.4159
= 0.318310\ \mathrm{V}$.

Dipole-dipole $n = 6$, $a = 5$: $k = 5277.88$ m,
$\Delta V = 100\times0.1/5277.88 = 1.8947\times10^{-3}\ \mathrm{V}$.

Ratio: $168.0$. The dipole-dipole array delivers $1/168$ of the Wenner signal
for the same current, in exchange for a DOI of 8.62 m against 2.60 m.

---

## ★4 — Why $F(0^+) = 1/2$

Let the resistivity of a thin surface layer of thickness $t$ be increased by a
fraction $\varepsilon$. For a point source on a half-space the potential at
distance $r$ can be written (as in the image series of
[06](../06-resistivity-forward-modelling.md)) as

$$V(r) \propto \rho_1\left[\frac{1}{r} + \text{images}\right].$$

The first-layer resistivity $\rho_1$ multiplies the *whole* expression, and the
image terms carry the reflection coefficient of the interface at depth $t$,
$k = -\varepsilon/(2+\varepsilon)$. To first order in $\varepsilon$:

$$V(r) \propto (1+\varepsilon)\left[1 - \frac{\varepsilon}{2}\cdot
\text{(image factor)}\right].$$

As $t \to 0$ the image factor $\to 1$ for every finite $r$ (the images collapse
onto the surface), so the bracket becomes $1-\varepsilon/2$ and the leading
$\varepsilon$ from $\rho_1$ leaves

$$\frac{\delta V}{V} \to \varepsilon - \frac{\varepsilon}{2}
= \frac{\varepsilon}{2}.$$

Because this limit is independent of $r$, the same ${1}/{2}$ applies to the
*combination* of four potentials that makes up $\Delta V$ of any array.
Physically: half of the total sensitivity of a DC array is spent on the medium
immediately beneath the electrodes, which no array can resolve. Hence the
cumulative response starts at $F(0^+) = 1/2$ and the *buried* density must be
normalised as $s = 2\,\mathrm{d}F/\mathrm{d}z$.

---

## ★5 — Reaching 5 m with Wenner

From the DOI table, $a = 5$ m gives DOI $= 2.60$ m. The demonstration of
[05](../05-ert-tomography.md) shows the DOI is proportional to the spacing, so
the required spacing is

$$a = 5\times\frac{5.00}{2.60} = 9.62\ \mathrm{m}\ \text{(use }a \approx 10\
\mathrm{m)}.$$

Signal cost: $k \propto a$, so $\Delta V \propto 1/a$:
$\Delta V(10)/\Delta V(5) = 0.5$, i.e. **a 50% loss of signal** for the extra
depth. With $I = 0.1$ A and $\rho = 100\ \Omega\,\mathrm{m}$,
$\Delta V = 100\times0.1/62.83 = 0.159\ \mathrm{V}$ — still far above any
plausible noise floor, so the trade is cheap in this ground.

---

## ★6 — Two arrays, two answers

The dipole-dipole reading (80 $\Omega\,\mathrm{m}$) is lower than the Wenner
reading (140 $\Omega\,\mathrm{m}$) at similar depths. Two explanations
consistent with the sensitivity tables:

1. **Sign reversal.** The dipole-dipole array has negative sensitivity at depth
   (the $\int s\,\mathrm{d}z = 1.0195$ overshoot in the lesson's table). If a
   resistive layer lies beneath the array, it lowers the dipole-dipole reading
   while raising the Wenner reading: both observations follow from one model.
2. **Depth weighting.** The two arrays sample different volumes (DOI 4.81 m
   against 2.60 m at $a = 5$ m; the dipole-dipole at $a = 10$ m reaches further
   still). If a conductive layer sits between 5 and 10 m, the dipole-dipole sees
   it and the Wenner does not.

Distinguishing measurement: **repeat both arrays at two or three spacings.** A
model with a resistive layer below a conductive one makes the dipole-dipole
$\rho_a$ pass through a minimum then *increase* with $n$ (the sign reversal),
whereas a simple two-layer model makes it decrease monotonically. Equivalently,
invert both data sets jointly with the same layer boundaries and compare
$\chi^{2}$.

---

## ★7 — The kernel constant

For a homogeneous half-space the sensitivity kernel is

$$S_\rho = \frac{I}{8\pi^{2}}\nabla\!\left(\frac{1}{r_A}-\frac{1}{r_B}\right)
\cdot\nabla\!\left(\frac{1}{r_M}-\frac{1}{r_N}\right).$$

Integrating over the half-space and using
$\int\nabla(1/r_A)\cdot\nabla(1/r_M)\mathrm{d}V = 4\pi/r_{AM}$ (the sources lie
in the plane, so the boundary terms vanish):

$$\int S_\rho\,\mathrm{d}V = \frac{I}{8\pi^{2}}\times4\pi\left[\frac{1}{r_{AM}}
-\frac{1}{r_{AN}}-\frac{1}{r_{BM}}+\frac{1}{r_{BN}}\right]
= \frac{I}{2\pi}\left[\cdots\right] = \frac{V}{\rho},$$

since for unit current $V = (\rho/2\pi)[\cdots]$. Now impose the *uniform
scaling* consistency condition: scaling the whole half-space by
$\rho\to\rho(1+\varepsilon)$ changes $\Delta V$ by exactly $\varepsilon\Delta V$,
so $\int S_\rho\,\mathrm{d}V$ must equal $\Delta V/\rho$. But the direct
integration gives $V/(2\rho)$; the missing factor 2 is the **surface step**
$F(0^+) = 1/2$ established in ★4. Both statements are therefore correct, and
their consistency *is* the check: the volume integral of the kernel gives the
buried half ($0.5$ of the total), and the surface step supplies the other half.

The demonstration's printed numbers confirm the arithmetic: the raw integral of
the kernel over $x$ (after integrating over $y$ and $z$) is $1.2268$ against the
required $V/(2\rho)\times8\pi^{2}/I = 1.2566$, i.e. agreement to 2.4% limited by
the finite integration ranges.

---

## ★8 — A 5–15 m design

Specification: sensitivity mass concentrated between 5 and 15 m.

1. **Target DOI ≈ 12 m.** Using the scaling DOI $= a(\text{DOI}/a)$: for
   dipole-dipole $n = 6$, $\text{DOI}/a = 1.787$, so $a = 12/1.787 = 6.7$ m.
2. **Shallow control.** Add $n = 1$ and $n = 2$ at the same spacing to cover
   0–4 m, so the shallow structure is not aliased into the deep image.
3. **Signal.** $|k| = 1055.58\,a = 7072$ m at $a = 6.7$ m, so
   $\Delta V = 50\times0.2/7072 = 1.41\ \mathrm{mV}$ for the deepest
   measurement — and $50\times0.2/94.25\times(6.7/6.7)^{-1}$: for $n = 1$,
   $|k| = 18.85a = 126.3$ m giving $\Delta V = 79.2\ \mathrm{mV}$. So the deep
   data are about 1.4 mV and need stacking (16 stacks give a factor 4) while the
   shallow data are comfortable.
4. **Footprint.** At 12 m depth the footprint is
   $a\times(15.03/6.0) = 6.7\times2.51 = 16.8$ m wide (10–90%). Any target
   smaller than ~17 m will be smeared; state that as part of the design.
5. **Electrodes.** A 100 m line needs $\lceil100/6.7\rceil + 1 + 8 \approx 25$
   electrodes.

The design meets the specification in the sense that the sensitivity is
concentrated where it is wanted; it does *not* promise resolution better than
its 17 m footprint, and the report must say so.
