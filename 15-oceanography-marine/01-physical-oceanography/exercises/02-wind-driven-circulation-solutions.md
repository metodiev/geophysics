# Solutions — 15-01-02 Wind-Driven Circulation, Ekman Transport and Gyres

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed, not estimated by hand.

Lesson: [02 Wind-Driven Circulation](../02-wind-driven-circulation.md).

Constants: $\Omega = 7.292115\times10^{-5}\ \mathrm{s^{-1}}$,
$R = 6.371\times10^{6}\ \mathrm{m}$, $\rho = 1025\ \mathrm{kg\,m^{-3}}$,
$1^\circ = 111.19\ \mathrm{km}$.

---

## ★1 — $f$ and $\beta$ at $25^\circ$S

$$\phi = -25^\circ,\qquad \sin(-25^\circ) = -0.422618,\qquad
f = 2(7.292115\times10^{-5})(-0.422618) = -6.1636\times10^{-5}\ \mathrm{s^{-1}}.$$

$$\beta = \frac{2(7.292115\times10^{-5})(\cos(-25^\circ))}{6.371\times10^{6}}
= \frac{1.458423\times10^{-4}(0.906308)}{6.371\times10^{6}}
= 2.0747\times10^{-11}\ \mathrm{m^{-1}\,s^{-1}}.$$

**Units:** $f$ is an angular frequency, $\mathrm{s^{-1}}$; $\beta = \partial
f/\partial y$ is $\mathrm{s^{-1}\,m^{-1}}$. **Signs:** $f$ is negative in the
southern hemisphere (rotation is clockwise viewed from above); $\beta$ is
positive everywhere, because $\cos\phi > 0$ for $|\phi| < 90^\circ$. Inertial
period: $2\pi/|f| = 2\pi/6.1636\times10^{-5} = 1.0194\times10^{5}\ \mathrm{s}
= 28.32$ h.

---

## ★2 — Ekman transport at $35^\circ$N

$$f = 2\Omega\sin35^\circ = 1.458423\times10^{-4}(0.573576)
= 8.3652\times10^{-5}\ \mathrm{s^{-1}},$$

$$M = \frac{\tau}{\rho f} = \frac{0.15}{1025 \times 8.3652\times10^{-5}}
= \frac{0.15}{0.085743} = 1.7494\ \mathrm{m^{2}\,s^{-1}}.$$

**Direction:** to the right of the wind; the wind is eastward, so the transport
is **southward**. Across $500\ \mathrm{km}$:

$$Q = M \times 5.0\times10^{5}\ \mathrm{m} = 8.747\times10^{5}\
\mathrm{m^{3}\,s^{-1}} = 0.875\ \mathrm{Sv}.$$

An equatorward Ekman transport at a western coast would drive downwelling; on an
eastern boundary it drives upwelling. The number sets the scale of the coastal
signal.

---

## ★3 — Dimensional analysis and meaning

$$\left[\frac{\tau}{\rho f}\right]
= \frac{\mathrm{N\,m^{-2}}}{\mathrm{kg\,m^{-3}}\cdot\mathrm{s^{-1}}}
= \frac{\mathrm{kg\,m^{-1}\,s^{-2}}}{\mathrm{kg\,m^{-3}\,s^{-1}}}
= \mathrm{m^{2}\,s^{-1}}. \ ✔$$

"Depth-integrated" means $\mathbf{M} = \int \mathbf{u}\,\mathrm{d}z$: a velocity
integrated over a vertical extent, so it is a *volume flux per unit horizontal
length* ($\mathrm{m^{3}\,s^{-1}}$ per metre $= \mathrm{m^{2}\,s^{-1}}$). To
obtain a volume transport through a section, multiply by the section length.

---

## ★★4 — Sverdrup transport

**(a)** With $\tau_y = 0$,
$\mathrm{curl}_z\boldsymbol{\tau} = \partial\tau_y/\partial x -
\partial\tau_x/\partial y = -\tau_0(\pi/L)\sin(\pi y/L)$:

$$-\tau_0\frac{\pi}{L} = -0.10 \times \frac{\pi}{3.0\times10^{6}}
= -1.0472\times10^{-7}\ \mathrm{N\,m^{-3}},$$

$$\text{at } y = 750\ \mathrm{km}: \quad \sin\!\left(\frac{\pi \times 750}{3000}\right)
= \sin\!\left(\frac{\pi}{4}\right) = 0.70711,$$

$$\mathrm{curl}_z\boldsymbol{\tau} = -1.0472\times10^{-7}\times0.70711
= -7.4048\times10^{-8}\ \mathrm{N\,m^{-3}}.$$

**(b)** $\beta(30^\circ\mathrm{N}) = 1.98247\times10^{-11}\
\mathrm{m^{-1}\,s^{-1}}$, so

$$V = \frac{\mathrm{curl}_z\tau}{\rho\beta}
= \frac{-7.4048\times10^{-8}}{1025 \times 1.98247\times10^{-11}}
= \frac{-7.4048\times10^{-8}}{2.03193\times10^{-8}}
= -3.6440\ \mathrm{m^{2}\,s^{-1}}.$$

**(c)** Across a $5000\ \mathrm{km}$ basin:

$$-3.6440 \times 5.0\times10^{6} = -1.822\times10^{7}\ \mathrm{m^{3}\,s^{-1}}
= -18.2\ \mathrm{Sv}.$$

Negative means **southward**. (The lesson quotes $4.169\ \mathrm{m^{2}\,s^{-1}}$
at $y = 900\ \mathrm{km}$, where $\sin(0.3\pi) = 0.8090$; note how strongly the
answer depends on where in the gyre you evaluate it.)

**(d)** The interior flow reverses where $\mathrm{curl}_z\tau = 0$, i.e. where
$\sin(\pi y/L) = 0$: at $y = 0$ and $y = 3000\ \mathrm{km}$. The physical reason
is the vorticity budget: $V$ is proportional to the local rate at which the wind
supplies vorticity, so it must change sign wherever that rate does.

---

## ★★5 — Ekman pumping

$$w_E = \frac{\mathrm{curl}_z\boldsymbol{\tau}}{\rho f}
= \frac{-7.4048\times10^{-8}}{1025 \times 7.292\times10^{-5}}
= \frac{-7.4048\times10^{-8}}{0.074744}
= -9.907\times10^{-7}\ \mathrm{m\,s^{-1}}.$$

In metres per year, using $1\ \mathrm{yr} = 3.156\times10^{7}\ \mathrm{s}$:

$$-9.907\times10^{-7} \times 3.156\times10^{7} = -31.27\ \mathrm{m\,yr^{-1}}.$$

**Sign:** negative $w_E$ with $z$ positive upward means **downward** flow at the
base of the Ekman layer, i.e. Ekman pumping, which displaces the thermocline
*downward*. Positive curl would give Ekman suction and an upward displacement.
Note that the sign convention must be stated: it is meaningless to report
"upwelling" without saying which direction is positive.

---

## ★★6 — The effect of $A_v$

**(a)** $D \propto \sqrt{A_v}$ and $V_0 \propto A_v^{-1/2}$, so multiplying
$A_v$ by 4 multiplies $D$ by 2 and divides $V_0$ by 2:

$$D = \sqrt{\frac{2(0.040)}{1.031261\times10^{-4}}} = \sqrt{775.8}
= 27.85\ \mathrm{m},$$

$$V_0 = \frac{0.10}{1025\sqrt{0.040 \times 1.031261\times10^{-4}}}
= \frac{0.10}{1025 \times 2.031\times10^{-3}}
= 0.04804\ \mathrm{m\,s^{-1}},$$

against $D = 13.93\ \mathrm{m}$ and $V_0 = 0.0961\ \mathrm{m\,s^{-1}}$.

**(b)** Both cases give

$$M = \frac{\tau}{\rho f} = \frac{0.10}{1025 \times 1.031261\times10^{-4}}
= 0.9460\ \mathrm{m^{2}\,s^{-1}},$$

to every digit. **The transport is the robust quantity.** It follows from
integrating the balance, so any $A_v$ that satisfies the surface stress and
vanishes at depth gives the same integral. The lesson's Section 3.2 makes the
same point with a $0.00\times10^{0}$ numerical difference. Consequence: a model
calibrated on satellite-derived *surface currents* constrains $A_v$ and says
almost nothing about the transport; a model calibrated on *transports* does the
reverse.

---

## ★★7 — $\beta$-plane error at $\pm2500$ km

At $d = 2500\ \mathrm{km}$, the true latitude is
$\phi = 30^\circ + 2500/111.19 = 30^\circ + 22.48^\circ = 52.48^\circ$, and

$$f_{\text{exact}} = 2\Omega\sin(52.48^\circ) = 1.1567\times10^{-4}\
\mathrm{s^{-1}},$$

$$f_0 + \beta d = 7.292115\times10^{-5} + 1.98247\times10^{-11}(2.5\times10^{6})
= 1.2247\times10^{-4}\ \mathrm{s^{-1}},$$

$$\text{error} = +6.805\times10^{-6}\ \mathrm{s^{-1}}
= 9.33\,\%\ \text{of } f_0$$

— against $3.13\,\%$ at $\pm1500\ \mathrm{km}$. Since $M \propto 1/f$, a
$9.3\,\%$ error in $f$ is a $9.3\,\%$ error in Ekman transport, and (from
Section 4) a $9.3\,\%$ error in the Sverdrup transport through $\beta$, whose own
mislocation compounds the first error. **A $\beta$-plane fitted at $30^\circ$N
should not be trusted $22^\circ$ away from it.**

---

## ★★★8 — Designing a Sverdrup test

A defensible answer has four parts.

**(a) Measured.** Two things. The surface wind-stress field, from scatterometry,
at a resolution fine enough to difference it ($\sim1^\circ$ is the practical
limit), plus a measure of the ocean's interior transport. The transport can be
taken from the depth-integrated geostrophic flow derived from hydrography, from
sea-surface height referenced to a mean, or (in the synthetic setting) directly
from a numerical model's streamfunction.

**(b) Inferred.** $V$ from $\beta V = \mathrm{curl}_z\tau/\rho$, and separately
$V$ from the measured transport. The test is the closure of the two, evaluated
term by term, ideally as a variance budget rather than a point comparison: over
what fraction of the basin does the wind curl explain the observed transport?

**(c) Error budget.** The dominant terms are the wind-stress error (a
$20\,\%$ stress error is a $20\,\%$ curl error), the errors in $f$ and $\beta$
(a $1\,\%$ latitude error near $30^\circ$N is a $\sim3\,\%$ $f$ error), and the
reference-level choice in the geostrophic transport, which can dwarf both.
Nonlinear and inertial terms enter the budget as a residual, not as a correction.

**(d) Where it fails first.** At the eastern margin. The vorticity balance has a
growing solution on the eastern side, so no laminar interior solution can close
there; in practice the balance fails where the boundary-layer scale becomes
comparable to the grid or the observed current width — tens of kilometres,
against a basin of thousands. Equivalently: the term dropped, friction, is
smallest in the interior and largest at the margin, so the interior is where the
balance should hold best and the margin is where it must fail. Quantitatively,
with $\delta_{\text{Munk}} = (\beta/A_H)^{-1/3}$-
scale widths of $\sim60\ \mathrm{km}$ (Section 5 of the lesson), any test
resolved on a $100\ \mathrm{km}$ grid cannot see the failure.

---

## ★★★9 — Why the boundary width is not constrained

**(The argument.)** The interior balance comes from *removing* friction: the
depth-integrated vorticity equation is $\beta V = \mathrm{curl}_z\tau/\rho$
gained by dropping the friction terms, and that step can be made only where those
terms are small. The boundary layer exists precisely where they are not small, so
the interior equation cannot determine its width. All that the interior solution
requires of the boundary layer is that it absorb the difference between the
interior transport and zero at the coast — a statement about an integral.

A different closure therefore gives a different width *and the same interior*:
$\delta \propto r$ for bottom drag, $\delta \propto A_H^{1/3}$ for lateral
viscosity. Both were computed in the lesson under the same wind.

**(One discriminator.)** The *cross-stream structure* of the boundary current:
bottom-drag closure predicts a velocity profile decaying over a fixed length
independent of depth and a strong sensitivity to bottom topography, whereas
lateral-viscosity closure predicts a smooth, depth-independent profile with a
sizeable return flow offshore and no direct topographic sensitivity. Measuring a
velocity section across the current at two depths is therefore a more informative
test than measuring its width.
