# Solutions — 06-12-01 Causes of Induced Seismicity: Injection, Extraction, Reservoirs

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [01 Causes of Induced Seismicity](../01-induced-seismicity-causes.md).

---

## ★1 — Dimensions

| Quantity | Symbol | Dimension |
|---|---|---|
| Biot coefficient | $\alpha$ | dimensionless |
| friction coefficient | $\mu_f$ | dimensionless |
| seismic moment | $M_0$ | $\mathrm{N\,m} = \mathrm{kg\,m^2\,s^{-2}}$ |
| Coulomb stress change | $\Delta CFS$ | $\mathrm{Pa} = \mathrm{kg\,m^{-1}\,s^{-2}}$ |

$\mu_f\Delta p$ has dimensions $[\text{dimensionless}]\times\mathrm{Pa} =
\mathrm{Pa}$ ✔, so it can be added to $\Delta\tau$ and $\mu_f\Delta\sigma_n$ in

$$\Delta CFS = \Delta\tau - \mu_f(\Delta\sigma_n - \Delta p).$$

The check is worth doing explicitly because the two "$\mu$"s in this literature —
friction (dimensionless) and shear modulus (Pa) — are different quantities with the
same symbol. Mixing them produces errors of order $10^{10}$.

---

## ★2 — Coulomb function at a point

$$CFS = \tau - \mu_f(\sigma_n - p) = 12 - 0.6(40 - 15)
= 12 - 0.6(25) = 12 - 15 = -3\ \mathrm{MPa}.$$

$CFS = -3\ \mathrm{MPa} < 0$, so the fault is **further** from failure than a
fault with $CFS = 0$: the available shear traction falls short of the frictional
resistance by $3\ \mathrm{MPa}$. Failure is favoured when $CFS \ge 0$.

---

## ★3 — Biot coefficient

$$K = 20,\ K_s = 40\ \mathrm{GPa}: \alpha = 1 - \frac{20}{40} = 0.5,$$
$$K = 4,\ K_s = 40\ \mathrm{GPa}: \alpha = 1 - \frac{4}{40} = 0.9 .$$

A rock with a small drained bulk modulus relative to its grain modulus has a
large $\alpha$: its skeleton is compliant, so the pore fluid carries a larger share
of the confining load and a given pressure change does more to the effective
stress. Setting $\alpha = 1$ (Terzaghi) would overstate the $K = 20$ case by a
factor $2$ and would happen to be nearly right for the $K = 4$ case — which is why
$\alpha$ must be stated, not assumed.

---

## ★4 — Pressure-induced Coulomb change

$$\alpha = 1 - \frac{12}{45} = 1 - 0.26667 = 0.73333 .$$

Pressure-only result ($\Delta\boldsymbol\sigma = 0$, so
$\Delta CFS = \mu_f\Delta p$):

$$\Delta CFS = 0.55 \times 3\ \mathrm{MPa} = 1.65\ \mathrm{MPa}.$$

Pressure change for $\Delta CFS = 0.1\ \mathrm{MPa}$:

$$\Delta p = \frac{0.1}{0.55} = 0.18182\ \mathrm{MPa}.$$

The second number is about $6\%$ of the first — i.e. a pressure change sixteen
times smaller than the $3\ \mathrm{MPa}$ injection is already enough to produce a
$0.1\ \mathrm{MPa}$ Coulomb change, a magnitude commonly quoted as decisive. That
is the honest scale of the pressure term: it is easy to produce, and it is the
only term in $\Delta CFS$ that does not depend on the assumed receiver plane.

---

## ★5 — Tensorial versus pressure term

The demonstration gives, at $r = 3\ \mathrm{km}$ from an $M_w\,4.5$ source,
$\text{peak}\,\lvert\Delta\sigma\rvert = 0.0348\ \mathrm{MPa}$. Since
$\Delta\sigma \propto M_0/r^3$,

$$\lvert\Delta\sigma\rvert(5\ \mathrm{km}) = 0.0348 \times \left(\frac{3}{5}\right)^{3}
= 0.0348 \times 0.216 = 0.00752\ \mathrm{MPa}.$$

Pressure term for $\Delta p = 0.5\ \mathrm{MPa}$, $\mu_f = 0.6$:

$$\mu_f\Delta p = 0.6(0.5) = 0.300\ \mathrm{MPa}.$$

Ratio: $0.300/0.00752 = 39.9$. The pressure term dominates by about a factor of
**40**. Note also that the $-3$ power is brutal: moving from 3 km to 5 km reduces the
static stress change by a factor of $4.6$, while the pressure term depends on the
diffusion geometry rather than on the source distance.

---

## ★6 — Interpolating the flip rate

Data (perturbation $\Delta$ in degrees, flip rate $f$): $(45, 0.1736)$,
$(60, 0.2917)$. Linear interpolation to $f = 0.25$:

$$\Delta_{25\%} = 45 + 15 \times \frac{0.25 - 0.1736}{0.2917 - 0.1736}
= 45 + 15 \times \frac{0.0764}{0.1181} = 45 + 9.7 = 54.7^\circ \approx 55^\circ .$$

So an uncertain receiver plane of about $\pm55^\circ$ flips a quarter of the
predictions. This is not a property of the earthquake but of the *pair*: the
static field of a double couple changes sign between neighbouring quadrant
boundaries, and $\Delta CFS$ depends on the resolved normal and shear tractions on
the assumed receiver plane. The demonstration makes the point twice: over all
orientations, half have $\Delta CFS > 0$ and half $< 0$ at *every* friction
coefficient, and the coplanar azimuth sweep alternates promoted and inhibited
directions in a pattern that repeats every $90^\circ$.

---

## ★★★7 — Pressurised inclusion in the undrained limit (derivation sketch)

Take the inclusion to be a sphere of radius $a$ whose internal pressure is raised
by $\Delta p$. In the undrained limit the fluid cannot escape during the
deformation, so the poroelastic response is described by the **undrained** elastic
constants: the same shear modulus $G$, but a bulk modulus increased by the fluid's
stiffness. The classical Eshelby/Mindlin result is that a spherical inclusion
under uniform pressure behaves as a centre of dilatation with strength proportional
to $\Delta p\,a^3$.

Write the displacement as $\mathbf u = \nabla\phi$ (an isotropic source), so
$\nabla^2\phi = \text{const}\times a^3\Delta p\,\delta(\mathbf r)$. Solving the
Poisson equation gives $\phi \propto a^3\Delta p/r$, hence

$$u_r \propto \frac{a^3\Delta p}{r^2},\qquad
\varepsilon \propto \frac{a^3\Delta p}{r^3},\qquad
\Delta\sigma \propto \frac{a^3\Delta p}{r^3},$$

so the stress change decays as $1/r^3$, the same power as the double-couple field —
a useful coincidence: far-field static stress transfer from volume change and from
faulting share the decay law and differ only in their angular pattern.

The undrained Poisson ratio, in terms of the drained $\nu$, the Biot coefficient
$\alpha$ and the Skempton coefficient $B$, is

$$\nu_u = \frac{3\nu + \alpha B(1-2\nu)}{3 - \alpha B(1-2\nu)} .$$

Check the limits: $B = 0$ (no pore-pressure coupling) returns $\nu_u = \nu$, and
$\alpha B \to 1$ pushes $\nu_u \to 0.5$ (an incompressible undrained response),
which is the correct physical limit for a fluid-saturated rock loaded fast enough
that the fluid cannot move.

---

## ★★★8 — Free surface versus point source

**Free-surface images.** A source at depth $z_s$ near a stress-free surface is
equivalent to the real source plus a reflected (image) source at $-z_s$ chosen to
cancel the tractions on $z = 0$. For a receiver at epicentral distance $r$ the
direct and image contributions have magnitudes $\propto 1/r^3$ and
$\propto 1/d^3$ with $d = \sqrt{r^2 + (2z_s)^2}$, and opposite signs for the
relevant components, so the fractional correction behaves as

$$\frac{\lvert d^{-3} - r^{-3}\rvert}{r^{-3}}
= \left(\frac{r^2}{r^2+4z_s^2}\right)^{3/2} - 1 \;\text{(in magnitude)} .$$

Setting this equal to $0.20$ and solving for $r$ with $z_s = 5\ \mathrm{km}$ gives
$r \lesssim 2z_s \approx 10\ \mathrm{km}$: within about $10\ \mathrm{km}$ the
surface changes the static stress by more than 20%. (The estimate is crude, since
the image amplitude also carries the free-surface reflection coefficients; the
scaling $r \sim 2z_s$ is the robust part.)

**Which limitation binds first.** For $M_w\,5$ the point-source approximation fails
at $r \sim 3\ \mathrm{km}$, which is *smaller* than the $10\ \mathrm{km}$
free-surface scale. So for a source at $5\ \mathrm{km}$ depth the point-source
error binds first, and any stress-transfer calculation closer than a few kilometres
should either use a finite-fault source or state that it does not.

---

## ★★★9 — Four questions before accepting "+0.05 MPa"

1. **What is the receiver focal mechanism, and how well is it constrained?**
   $\Delta CFS$ depends on the assumed normal and slip vectors. The demonstration
   shows the sign flips for about a quarter of cases at $\pm55^\circ$ of
   receiver-plane uncertainty, so a poorly constrained mechanism can change the
   *sign*, not just the magnitude.
2. **What is the shear modulus and Poisson ratio, and is the medium layered?**
   $\Delta\sigma \propto M_0/r^3$ scaled by combinations of $\mu$ and $\nu$; a
   factor-of-two error in $\mu$ changes the magnitude proportionally, and a
   layered or anisotropic structure changes the angular pattern. This alters the
   **magnitude** and, near nodal planes, the sign.
3. **What is the location and depth uncertainty of the hypocentre?**
   Because $\Delta\sigma \propto r^{-3}$, a $1\ \mathrm{km}$ location error near
   $r = 3\ \mathrm{km}$ is a $>60\%$ change in magnitude, and a depth error moves
   the receiver between stress lobes, potentially flipping the sign.
4. **What is the reference state, and is the pressure term included?**
   $+0.05\ \mathrm{MPa}$ relative to what baseline, and does $\Delta CFS$ include
   $\mu_f\Delta p$? If the reported number is the tensorial term only while a large
   pressure change was also present, the reported value can be a minor contributor
   (§4 above: $0.1\ \mathrm{MPa}$ of pressure term needs only
   $0.18\ \mathrm{MPa}$ of pressure change).

A common failure mode is to answer questions 1–3 with "standard values" and then
report a two-significant-figure stress change; the honest output is a range, or a
statement of which questions were not answered.
