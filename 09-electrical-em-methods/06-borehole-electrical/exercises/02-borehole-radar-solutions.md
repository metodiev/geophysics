# Solutions — 09-06-02 Borehole Radar and Directional Probing

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All models are **SYNTHETIC**.

Lesson: [02 Borehole Radar and Directional Probing](../02-borehole-radar.md).

---

## ★1 — Velocity, wavelength and resolution at 200 MHz

$v = c/\sqrt{\varepsilon_r}$ with $c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$
(exact), $\lambda = v/f$, $f = 2.00\times10^{8}$ Hz.

| $\varepsilon_r$ | $\sqrt{\varepsilon_r}$ | $v$ (m/s) | $v$ (m/ns) | $\lambda$ (m) | $\lambda/2$ (m) |
|---|---|---|---|---|---|
| 4 | 2 | $1.498962\times10^{8}$ | 0.1498962 | 0.749481 | 0.374741 |
| 9 | 3 | $9.993082\times10^{7}$ | 0.0999308 | 0.499654 | 0.249827 |
| 25 | 5 | $5.995849\times10^{7}$ | 0.0599585 | 0.299792 | 0.149896 |

The resolution improves as $\varepsilon_r^{-1/2}$: water-bearing rock slows the
wave and shortens the wavelength, but it also attenuates far more strongly, so
the gain in resolution is usually paid for in penetration.

---

## ★2 — Range from a two-way time

$$R = \frac{v\,t}{2} = \frac{1.2239\times10^{8}\times130.7\times10^{-9}}{2}
= 8.00\ \mathrm{m}\ (8.0\ \mathrm{m\ to\ 3\ significant\ figures}).$$

Two independent quantities that each produce a $10\%$ range error:

1. **The velocity.** $R\propto v$, so a $10\%$ error in $\varepsilon_r$ (a $5\%$
   error in $\varepsilon_r$ changes $v$ by $10\%$) changes every range by $10\%$.
2. **The time origin.** $R$ is proportional to $t$, so an uncorrected
   antenna/cable delay of $13.1$ ns (10% of 130.7 ns) does the same. A third,
   equally real, is the assumption of a straight, monostatic path in a medium
   that may be anisotropic or layered.

---

## ★3 — Velocity and permittivity from a travel time

$$v = \frac{20.0}{168.5\times10^{-9}} = 1.1869\times10^{8}\ \mathrm{m\,s^{-1}},
\qquad
\varepsilon_r = \left(\frac{c}{v}\right)^{2}
= \left(\frac{2.99792458}{1.1869}\right)^{2} = 6.379 .$$

The assumption connecting $\varepsilon_r$ to water content is a **mixing law**
(e.g. a time-average or a complex-refractive-index model) together with a
porosity, and — crucially — the assumption that the wave samples the pore water
volumetrically rather than along grain contacts. The travel time does not test
that assumption.

---

## ★4 — Attenuation in two formations

$\varepsilon = 9\varepsilon_0 = 7.96877\times10^{-11}\ \mathrm{F\,m^{-1}}$,
$\sqrt{\mu_0/\varepsilon} = 125.58\ \Omega$,
$\omega\varepsilon = 2\pi\times2\times10^{8}\times7.96877\times10^{-11}
= 0.1001\ \mathrm{S\,m^{-1}}$.

| $\sigma$ (S/m) | loss tangent $\sigma/\omega\varepsilon$ | $\alpha = \frac{\sigma}{2}\sqrt{\mu/\varepsilon}$ (Np/m) | $\alpha$ (dB/m) | two-way loss over 20 m |
|---|---|---|---|---|
| 0.002 | 0.0200 | 0.1256 | 1.091 | 43.6 dB |
| 0.020 | 0.1997 | 1.256 | 10.91 | 436 dB |

The first is a radar formation: 43.6 dB over a 20 m two-way path is measurable,
and the loss tangent of 0.02 is well inside the low-loss regime (the
approximation is good to better than 1% there). The second is not: 436 dB is
$10^{22}$ in amplitude and the loss tangent of 0.20 is already where the
approximation is about 1% low, so the wave has become diffusive at that range.
**The regime check, not the frequency, decides whether the method applies.**

---

## ★5 — The azimuthal arc at 8 m

Omnidirectional: arc $= 2\pi R = 2\pi\times8.0 = 50.265$ m.
$\pm20^\circ$: arc $= 2R\theta = 2\times8.0\times0.349066 = 5.585$ m.

Criterion for an antenna to be adequate for a siting decision: state the
tolerance of the decision (for example "the target must be intersected by a
borehole whose position uncertainty is under 1 m") and require the arc at the
target range to be smaller than that tolerance. At 8 m the $\pm20^\circ$ antenna
gives a 5.6 m arc, which is *not* adequate for a 1 m siting tolerance; either a
narrower antenna, a lower range, a second hole or a vector (multi-component)
measurement is required. The criterion is what makes the answer defensible; the
arc alone is not a decision.

---

## ★6 — Why the rank is 59 and not 64

The rank of a $64\times80$ matrix cannot exceed 64, so the ceiling is the number
of rays. The measured rank is 59, five short of the ceiling and twenty-one short
of the number of cells: the ray paths in a two-borehole transmission geometry are
drawn from a two-parameter family (source depth, receiver depth), so their path
lengths in the cells satisfy linear dependencies. Adding rays from the same two
holes does not add information once the family is exhausted.

What the missing directions do: they are model perturbations that change the data
by less than the noise, so a reported model can differ from the truth by an
amount comparable to the anomaly — measured in the lesson as $11.8\%$ of velocity
(against a $10\%$ anomaly) for a data change of $6.4\times10^{-14}$ of the picking
error. A reported anomaly amplitude is therefore a lower bound of unknown
tightness, and the honest report includes the singular spectrum or a resolution
estimate.

---

## ★7 — Designing for rank

Model answer. Requirements: (i) cells small enough to resolve the target
($1.0\times1.0$ m for metre-scale features at $\lambda = 1.22$ m in
$\varepsilon_r = 6$); (ii) rank $\ge0.9\,N_{\text{cell}}$. With two boreholes 20 m
apart and a $1.0\times1.0$ m grid the inter-hole volume contains 200–400 cells,
so 200 rays of a *single* family will not reach the rank target — the family has
at most two free indices. The design that works uses several ray *families*: a
fixed source at depth $z_s$ with receivers throughout the other hole (a fan), the
source repeated at many depths, **plus** sources and receivers on the surface
between the holes, and a few shots from a third geometry such as a surface line
offset from the hole pair. Because the question forbids a third borehole, the
surface geometry is the only additional family available, and it must be used.

Expected spectrum: $s_{\max}\sim$ half the longest path length; the rank should
follow the count of independent families times the number of sampling depths, and
the singular spectrum should show no gap beyond a factor $10^{3}$ between
$s_{\max}$ and $s_{\text{rank}+1}$. Defence against the straight-ray assumption:
the cell size (1 m) is comparable to $\lambda/2$ (0.61 m), so the Fresnel zone
spans only a few cells and the straight-ray approximation is marginal; the design
must state that a curved-ray or full-wave check would be needed for the final
interpretation, and that the tomogram's resolution claim is limited accordingly.

---

## ★8 — Making the null direction observable

Model answer. The null direction is invisible because every ray in the geometry
measures a path integral of slowness, and the perturbation has the same effect on
all paths. To observe it, add a measurement whose sensitivity is *not* a path
integral: (a) **reflectivity from a borehole wall** — the single-hole reflection
geometry of §3 of the lesson measures the local dielectric contrast at a point on
the wall, with a sensitivity that is local in range and (with a directional
antenna or a vector receiver) in azimuth; (b) **amplitude/tomography of the
transmitted field** rather than travel time, which samples attenuation and adds a
second, differently-weighted integral; (c) **a third borehole**, which introduces
new path directions (excluded by the question). The physical quantity added is
therefore the *local reflection coefficient* (case a) or the *attenuation
coefficient* along each path (case b). Executable specification: place the
transmitter and receiver at the same depths in a single hole, record the
wall-reflection trace at 250 MHz, and compute the local reflection coefficient as
a function of depth; then check whether the null-direction perturbation of §4.3
predicts a reflection-coefficient change above the system's noise floor.
