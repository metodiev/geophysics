# Solutions — 08-03-01 Magnetic Anomaly Physics and Remanent vs Induced Magnetisation

> **Read after attempting the exercises.** Several problems have more than one
> defensible answer; where that is so, it is said. All numbers here were computed
> from the stated inputs or taken from the demonstration's printed output.

Lesson: [01 Magnetic Anomaly Physics](../01-magnetic-anomaly-basics.md).

---

## ★1 — Ambient field to H

$$H_0 = \frac{B_0}{\mu_0} = \frac{55\times10^{-6}}{4\pi\times10^{-7}}
= \frac{55\times10^{-6}}{1.256637\times10^{-6}} = 43.77\ \mathrm{A\,m^{-1}}.$$

The step is T $\to$ A m$^{-1}$, and $\mu_0$ carries the units H m$^{-1}$:
$(\mathrm{T})/(\mathrm{H\,m^{-1}}) = (\mathrm{kg\,s^{-2}\,A^{-1}})/(\mathrm{kg\,m\,s^{-2}\,A^{-2}})
= \mathrm{A\,m^{-1}}$. ✔

---

## ★2 — Induced magnetisation and moment

$$M_i = \chi H_0 = 0.020\times43.77 = 0.8753\ \mathrm{A\,m^{-1}},$$
$$m = M_i V = 0.8753\times2.0\times10^{9} = 1.751\times10^{9}\ \mathrm{A\,m^{2}}.$$

The conversion $2.0\ \mathrm{km^{3}} = 2.0\times10^{9}\ \mathrm{m^{3}}$ is where
most errors happen: $1\ \mathrm{km^{3}} = (10^{3})^{3} = 10^{9}\ \mathrm{m^{3}}$.

---

## ★3 — The anomaly

$$\Delta T = \frac{\mu_0}{4\pi}\frac{2m}{z^{3}}
= 1.0\times10^{-7}\times\frac{2\times1.751\times10^{9}}{(2.0\times10^{3})^{3}}
= 1.0\times10^{-7}\times\frac{3.502\times10^{9}}{8.0\times10^{9}}
= 4.377\times10^{-8}\ \mathrm{T} = 43.77\ \mathrm{nT}.$$

---

## ★4 — Why a projection

The instrument records $\left|\mathbf{B}_0+\mathbf{B}_a\right|$, and the leading
correction to $\left|\mathbf{B}_0\right|$ is the component of $\mathbf{B}_a$
along $\mathbf{B}_0$: $\Delta T = \hat f\cdot\mathbf{B}_a$. The quantity measured
is therefore the total-field magnitude (a scalar), and $\Delta T$ is a derived
projection, not a vector component and not $\left|\mathbf{B}_a\right|$. In the
demonstration's model $\left|\mathbf{B}_a\right| = 44.83$ nT while
$\Delta T = 31.08$ nT — a 44% difference for a body in a $60^\circ$ field.

---

## ★5 — Using the invariant $\Delta T z^{3}$

$$\Delta T(5.0\ \mathrm{km}) = \frac{248.7\ \mathrm{nT\,km^{3}}}{(5.0\ \mathrm{km})^{3}}
= \frac{248.7}{125} = 1.99\ \mathrm{nT}.$$

The product is constant because the anomaly of a fixed dipole falls exactly as
$r^{-3}$ and the observer is moving along the axis; equivalently, because the
field is homogeneous of degree $-3$ in the distance from the source. It is *not*
constant for a body of finite size when the observation moves closer than a few
body widths, which is the point of
[04 Forward Modelling](../04-magnetic-forward-modelling.md).

---

## ★6 — The $3\sin^{2}I - 1$ factor

$$\frac{3\sin^{2}45^\circ - 1}{3\sin^{2}90^\circ - 1}
= \frac{3(0.5) - 1}{3 - 1} = \frac{0.5}{2} = 0.25 .$$

At $I = 45^\circ$ the anomaly is one quarter of the pole value. The factor
vanishes when $3\sin^{2}I = 1$, i.e. $\sin I = 0.5774$, i.e.
$I = 35.26^\circ$. Note that a *real* survey at $35^\circ$ does not see zero: the
vanishing applies to a dipole observed over its centre, whereas a finite body has
a distributed anomaly whose peak is displaced.

---

## ★7 — Required moment and volume

$$m = \frac{\Delta T\,4\pi z^{3}}{2\mu_0}
= \frac{25.0\times10^{-9}\times4\pi\times(3.0\times10^{3})^{3}}{2\times4\pi\times10^{-7}}
= \frac{25.0\times10^{-9}\times2.7\times10^{10}}{2\times10^{-7}}
= 3.38\times10^{9}\ \mathrm{A\,m^{2}}.$$

The $4\pi$ cancels between numerator and denominator — a useful simplification:
$m = \Delta T z^{3}/(2\left(\mu_0/4\pi\right))$. Then

$$V = \frac{m}{M} = \frac{3.38\times10^{9}}{2.0} = 1.69\times10^{9}\ \mathrm{m^{3}}
= 1.69\ \mathrm{km^{3}}.$$

---

## ★8 — The quadratic term

The expansion of $\left|\mathbf{B}_0+\mathbf{B}_a\right|$ gives a second term of
order $B_a^{2}/(2B_0)$:

$$\frac{\left(500\times10^{-9}\right)^{2}}{2\times50\times10^{-6}}
= \frac{2.5\times10^{-13}}{1.0\times10^{-4}} = 2.5\times10^{-9}\ \mathrm{T}
= 2.5\ \mathrm{nT},$$

which is $0.5\%$ of the 500 nT anomaly. For the term to reach $1\%$ of the
anomaly, $\Delta T^{2}/(2B_0) = 0.01\,\Delta T$, so
$\Delta T = 0.02\,B_0 = 0.02\times50\ \mu$T $= 1.0\ \mu$T. **A 1 $\mu$T anomaly in
a 50 $\mu$T field is where the linearisation of a total-field measurement starts
to fail**, which is why airborne surveys over magnetite-rich bodies sometimes
need the full non-linear reduction.

---

## ★9 — Experiment design (specification)

**Metric.** $\varepsilon(r) = \left|\Delta T_{\text{cube}}(r) - \Delta T_{\text{dipole}}(r)\right| /
\left|\Delta T_{\text{cube}}(r)\right|$ along a ray fixed in direction (say the
body axis and perpendicular to it, since the error is anisotropic), with $r$
the distance from the body centre.

**Exact reference.** The uniformly magnetised cube by the surface-charge integral
of [04 Forward Modelling](../04-magnetic-forward-modelling.md), which itself must
first be validated against the exact axial field of a charged disk. A dipole
formula is *not* an acceptable reference, since it is the thing being tested.

**Sampling.** $r/a$ from 0.75 to 20 at ten points, with $a$ the cube side; the
first point is inside the near field and the last is deep in the far field.

**Expected shape.** A monotone decay in $r/a$, with the error of order unity at
$r \sim a$, below 10% by $r \sim 3a$ and below 2% by $r \sim 5a$: the
$r^{-2}$-type convergence measured for the prism in
[04 Forward Modelling](../04-magnetic-forward-modelling.md).

---

## ★10 — Three explanations of a negative anomaly

1. **A body magnetised against the field** (remanence-dominated, or a
   reverse-polarity rock). Discriminator: measure the NRM direction on an
   oriented sample.
2. **A body at low magnetic latitude magnetised along the field.** The
   $3\sin^{2}I - 1$ factor is negative below $35.3^\circ$ inclination.
   Discriminator: compute the factor from the known field inclination.
3. **A shape or magnetic-moment effect producing a negative lobe**, e.g. the
   negative ring of a shallow dipole or the negative part of a prism's anomaly.
   Discriminator: forward-model the anomaly shape and compare the peak-to-trough
   ratio.

A fourth, legitimate answer is a **mis-levelled survey** where the "anomaly" is a
processing artefact; the discriminator is a repeat of the line in the opposite
direction.
