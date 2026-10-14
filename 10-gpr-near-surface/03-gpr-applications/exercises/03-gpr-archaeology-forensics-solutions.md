# Solutions — 10-03-03 GPR in Archaeology, Forensics and Buried Utilities

> **Read after attempting the exercises.** Numbers were computed with the project
> virtual environment. Where a problem has more than one defensible answer, that
> is said.

Lesson: [03 GPR in Archaeology, Forensics and Buried Utilities](../03-gpr-archaeology-forensics.md).
All values are **SYNTHETIC** teaching values except the physical constants
$c = 0.299792458\ \mathrm{m\,ns^{-1}}$,
$Z_0 = 376.730313668\ \Omega$, $\varepsilon_{\mathrm{water}} = 80.1$.

---

## ★1 — Fit of a small hyperbola

$$t^2 = \frac{4}{v^2}x^2 + \frac{4z^2}{v^2}.$$

Two points: $(x^2, t^2) = (0, 576.00\ \mathrm{ns^2})$ and
$(1.0\ \mathrm{m^2}, 1128.96\ \mathrm{ns^2})$.

$$m = \frac{1128.96 - 576.00}{1.0} = 552.96\ \mathrm{ns^2\,m^{-2}},
\qquad c = 576.00\ \mathrm{ns^2}.$$

$$v = \frac{2}{\sqrt{552.96}} = \frac{2}{23.5151} = 0.085052\ \mathrm{m\,ns^{-1}},$$

$$z = \frac{\sqrt{576.00}}{2}(0.085052) = \frac{24.0}{2}(0.085052)
= 1.0206\ \mathrm{m}.$$

$$\varepsilon_r = \left(\frac{c}{v}\right)^{2}
= \left(\frac{0.299792458}{0.085052}\right)^{2} = 3.5248^{2} = 12.42.$$

Units: $m$ in $\mathrm{ns^2\,m^{-2}}$, $c$ in $\mathrm{ns^2}$, $v$ in
$\mathrm{m\,ns^{-1}}$, $z$ in m, $\varepsilon_r$ dimensionless.

Note how thin the evidence is: **two** points determine both parameters, and a
single pick error anywhere propagates directly. Real practice uses $20$–$100$
traces precisely so that the fit is over-determined and the residuals can be
inspected.

---

## ★2 — Air-filled and water-filled voids

$$R_{\mathrm{air}} = \frac{\sqrt{12.0}-1}{\sqrt{12.0}+1}
= \frac{3.46410-1}{3.46410+1} = +0.5520
\;\Rightarrow\; 20\log_{10}(0.5520) = -5.16\ \mathrm{dB},$$

$$R_{\mathrm{water}} = \frac{3.46410-8.95042}{3.46410+8.95042}
= -0.4419 \;\Rightarrow\; 20\log_{10}(0.4419) = -7.09\ \mathrm{dB}.$$

| target | $R$ | relative amplitude |
|---|---|---|
| air-filled void | $+0.5520$ | $-5.16\ \mathrm{dB}$ |
| water-filled void | $-0.4419$ | $-7.09\ \mathrm{dB}$ |

**They differ in sign and in magnitude; they do not differ in the fact that both
are strong.** The magnitudes differ by $1.9\ \mathrm{dB}$, which is inside the
calibration error of most field amplitude work, so the *sign* (i.e. the polarity
of the onset relative to the surface echo) is the usable discriminator, with the
amplitude as a weak confirmation. In practice the two are separated by
understanding the situation — a void under a slab is air; a pipe network carries
water — rather than by the trace alone.

---

## ★3 — Wavelength, $\lambda/4$, Fresnel radius

$$v = \frac{0.299792458}{\sqrt{12.0}} = 0.0865441\ \mathrm{m\,ns^{-1}},
\qquad
\lambda = \frac{v}{f} = \frac{0.0865441}{0.400} = 0.216360\ \mathrm{m}.$$

$$\frac{\lambda}{4} = 0.054090\ \mathrm{m} \approx 54\ \mathrm{mm},$$

$$r_f = \sqrt{\frac{\lambda z}{2}} = \sqrt{\frac{0.216360 \times 1.20}{2}}
= \sqrt{0.129816} = 0.36030\ \mathrm{m} \approx 0.36\ \mathrm{m}.$$

**$\lambda/4$ is a resolution statement** — the closest two interfaces can be and
still be seen as two echoes. **$r_f$ is a detection statement** — the patch of
reflector that contributes to one echo, hence the smallest object that returns a
strong echo on its own. The Fresnel radius here is $6.7\times$ the quarter
wavelength; quoting one for the other understates or overstates the survey by
nearly an order of magnitude.

---

## ★4 — Does the short aperture meet the specification?

From the lesson, the short-aperture fit ($\pm0.50\ \mathrm{m}$, $41$ traces,
$0.20\ \mathrm{ns}$ picks) gives $\sigma_z = 3.3\%$ of the depth. For
$z = 1.50\ \mathrm{m}$:

$$\sigma_z = 0.033 \times 1.50 = 0.0495\ \mathrm{m} \approx 0.050\ \mathrm{m},$$

$$2\sigma_z = 0.099\ \mathrm{m} \approx 0.10\ \mathrm{m}.$$

| claim | depth interval |
|---|---|
| $1\sigma$ ($68\%$) | $1.500 \pm 0.050\ \mathrm{m}$ |
| $2\sigma$ ($95\%$) | $1.500 \pm 0.099\ \mathrm{m}$ |

**Verdict: the specification is met at $1\sigma$ and only just met at $2\sigma$.**
A report of "$\pm0.10\ \mathrm{m}$" from this survey is defensible as a $2\sigma$
bound, but it would be dishonest as a *worst case*: the Gaussian tail extends
beyond it, and the velocity error may be systematic rather than random. The
long-aperture fit ($0.4\%$, $\sigma_z = 0.006\ \mathrm{m}$) meets the
specification by a factor of $8$ at $2\sigma$ — which is the practical reason to
double the profile length.

---

## ★5 — Small targets and the noise floor

The Rayleigh law is $A \propto a^3$ at fixed frequency.

| radius (mm) | $(a/30)^3$ | dB relative to the $30\ \mathrm{mm}$ target | absolute (noise $=0\ \mathrm{dB}$) |
|---|---|---|---|
| $30$ | $1.0000$ | $0.0$ | $+30.0\ \mathrm{dB}$ |
| $15$ | $0.1250$ | $-18.06$ | $+11.94\ \mathrm{dB}$ |
| $8$ | $0.018963$ | $-34.44$ | $-4.44\ \mathrm{dB}$ |

The $8\ \mathrm{mm}$ target is **below the noise floor by $4.4\ \mathrm{dB}$**:
undetectable, even though it is far larger than the $\lambda/4 = 0.054\
\mathrm{m}$... it is not, in fact: $8\ \mathrm{mm}$ is smaller than $\lambda/4$,
which is the point. Resolution and detection are answering different questions.

For a detection threshold of $+6\ \mathrm{dB}$ above the noise, the budget is
$30 - 6 = 24\ \mathrm{dB}$ below the reference target:

$$\left(\frac{a}{30}\right)^{3} = 10^{-24/20} = 0.063096
\;\Rightarrow\; a = 30\,(0.063096)^{1/3} = 30(0.39810) = 11.94\ \mathrm{mm}.$$

**The smallest detectable radius is about $12\ \mathrm{mm}$** — the cube root of
the amplitude budget, which is why the size range that a survey can see is so much
narrower than its dynamic range suggests.

---

## ★6 — Focus loss and reported depth

$$20\log_{10}\!\left(\frac{0.0809}{0.6495}\right) = 20\log_{10}(0.12456)
= -18.09\ \mathrm{dB}.$$

So a migration velocity $20\%$ too low destroys $18\ \mathrm{dB}$ of the focus
amplitude — a factor of $8$ — while the event remains perfectly visible.

Reported depth:

$$z = \frac{v_{\mathrm{mig}}t_0}{2} = \frac{(0.8 \times 0.0999)(30.02)}{2}
= 1.1998\ \mathrm{m} \approx 1.20\ \mathrm{m},$$

against a true $1.50\ \mathrm{m}$: $-0.30\ \mathrm{m}$ ($-20\%$). The demonstration
prints $1.192\ \mathrm{m}$ for $v_{\mathrm{mig}} = 0.0800$ because it uses
$v = 0.0800$ rather than $0.8\times0.0999 = 0.07992$; the difference is
$0.008\ \mathrm{m}$, which is the rounding in the table.

**What focus analysis can and cannot measure.** The *focus* measures the velocity:
it is the only quantity that makes the summation constructive, and the peak
amplitude is a direct functional of it. It **cannot** measure the depth
independently, because the depth is computed from the same velocity and the apex
time. Focus analysis therefore gives one number (velocity) and the depth is a
derived quantity — a self-consistent pair, not two independent measurements. This
is the same structural point as the moisture inversion: the observation constrains
a curve, and a curve plus an assumption gives a point.

---

## ★7 — A utility-mapping procedure

**Objective:** service depth to $\pm0.15\ \mathrm{m}$ in a soil of
$\varepsilon_r = 12$ ($v = 0.0865\ \mathrm{m\,ns^{-1}}$).

1. **Frequency: $400\ \mathrm{MHz}$.** $\lambda = 0.216\ \mathrm{m}$,
   $\lambda/4 = 54\ \mathrm{mm}$, comfortably below the tolerance; $r_f$ at
   $1.2\ \mathrm{m}$ depth is $0.36\ \mathrm{m}$, so a service crossing the line
   perpendicular is well resolved and a service running *along* the line is a
   broad flat event — which is why the procedure requires crossing, not just
   proximity.
2. **Trace spacing: $0.05\ \mathrm{m}$.** Oversampled relative to $r_f$ so the
   hyperbola is sampled smoothly for the fit; this is a fitting requirement, not
   a resolution claim, and the resolution claim stated in the report is
   $r_f \approx 0.36\ \mathrm{m}$.
3. **Velocity, from two independent measurements.** (a) A common-midpoint
   sounding over the same line, giving $v$ with about $4\%$ uncertainty from the
   moveout — the best available because it uses many offsets. (b) A hyperbola fit
   over the full available aperture (at least $\pm2\ \mathrm{m}$, i.e. more than
   the target depth) with a stated pick error, which the lesson's Monte Carlo
   converts into a velocity uncertainty. If the two disagree by more than the
   combined uncertainty, the overburden is layered and a two-layer velocity model
   is required.
4. **Depth and its interval.** $z = vt_0/2$ with the CMP velocity:
   a $4\%$ velocity error is a $4\%$ depth error, i.e. $\pm0.048\ \mathrm{m}$ at
   $1.2\ \mathrm{m}$ — inside the $\pm0.15\ \mathrm{m}$ target with room for the
   $0.5\ \mathrm{ns}$ picking term ($\pm0.02\ \mathrm{m}$). Report
   $1.20 \pm 0.06\ \mathrm{m}$, not $1.20\ \mathrm{m}$.
5. **A service not crossed at its apex.** The minimum-time trace gives the plan
   position directly (no velocity involved); the depth at that trace is
   $v t_{\min}/2$, which is a *lower bound* on the true depth, because at any
   nonzero offset the true depth is larger. The report must therefore carry the
   offset, e.g. "at least $1.15\ \mathrm{m}$ deep, $0.3\ \mathrm{m}$ east of the
   marked line".
6. **The assumption that would invalidate the result.** A laterally variable
   moisture content along the line, which changes $v$ between the CMP location and
   the target location. The test is a second CMP at the far end of the line: if
   the two velocities differ by more than the stated uncertainty, the profile is
   not homogeneous and the depth must be reported per segment.

---

## ★8 — Why the fitted velocity and depth are correlated

With $c$ (the intercept) exact:

$$v = 2m^{-1/2} \;\Rightarrow\;
\frac{\partial v}{\partial m} = -m^{-3/2}
\;\Rightarrow\; \frac{\delta v}{v} = -\frac{1}{2}\frac{\delta m}{m}
= -\frac{\epsilon}{2},$$

$$z = \frac{\sqrt c}{2}v \;\Rightarrow\;
\frac{\delta z}{z} = \frac{\delta v}{v} = -\frac{\epsilon}{2}.$$

Both quantities move by the same relative amount and in the same direction, so a
slope error alone would give a correlation of $+1$: **the two estimates are the
same information expressed twice.**

**Why $+0.999$ rather than exactly $+1$.** The intercept $c$ is *not* exact. Write

$$\frac{\delta z}{z} = \frac{1}{2}\frac{\delta c}{c} - \frac{1}{2}\frac{\delta m}{m},
\qquad
\frac{\delta v}{v} = -\frac{1}{2}\frac{\delta m}{m}.$$

The $\delta c$ term appears only in $z$, so it is an independent contribution. The
observed correlation is therefore
$\rho = \sigma_m^{2}/(\sigma_m\,\sigma_z)$ evaluated with both terms — close to
$+1$ when the slope term dominates, and below $+1$ when the intercept term
contributes a comparable amount.

**Why a longer aperture lowers the correlation (to $+0.948$).** Over a long
baseline the slope is determined much better relative to the intercept
($\sigma_m/m$ falls as $a^{-2}$), so both errors shrink and the *shared* component
becomes a smaller fraction of the total; what remains is increasingly the
independent $\delta c$ contribution to $z$. A correlation of $+0.948$ is still
high, but it is measurably lower than $+0.999$, and the demonstration's numbers
show the whole trade: a factor of $4$ in aperture buys a factor of $10$ in
velocity accuracy and a factor of $8$ in depth accuracy.

---

## ★9 — A forensic target: reflection, shadow or pattern?

**Reflection coefficient of the disturbance.** $\varepsilon_r$ from $9.00$ to
$9.36$:

$$R = \frac{\sqrt{9.00}-\sqrt{9.36}}{\sqrt{9.00}+\sqrt{9.36}}
= \frac{3.00000-3.05941}{6.05941} = -0.00981
\;\Rightarrow\; 20\log_{10}(0.00981) = -40.2\ \mathrm{dB}.$$

Relative to a $0.30$ contrast (a strong utility or wet interface):

$$20\log_{10}\!\left(\frac{0.00981}{0.30}\right) = -29.7\ \mathrm{dB}.$$

So the *reflection* from the grave wall is about $30\ \mathrm{dB}$ below a strong
reflector. It is inside the dynamic range of a good system, but it is at the level
of sedimentological noise, coupling changes and clutter; a reflection-based claim
would need the strongest possible evidence.

**Attenuation shadow.** With $\varepsilon_r = 9$ and $\sigma$ doubling from
$0.005$ to $0.010\ \mathrm{S\,m^{-1}}$, the low-loss attenuation is
$\alpha = \sigma Z_0/(2\sqrt{\varepsilon_r})$:

$$\alpha_{\mathrm{background}} = \frac{0.005(376.73)}{2(3)} = 0.31394\
\mathrm{Np\,m^{-1}} = 2.727\ \mathrm{dB\,m^{-1}},$$

$$\alpha_{\mathrm{grave}} = \frac{0.010(376.73)}{2(3)} = 0.62788\
\mathrm{Np\,m^{-1}} = 5.454\ \mathrm{dB\,m^{-1}}.$$

A reflector at $1.50\ \mathrm{m}$ below a $0.60\ \mathrm{m}$ thick disturbed
volume has a two-way path of $1.2\ \mathrm{m}$ through it:

$$\Delta(\text{loss}) = 1.2\,(5.454-2.727) = 3.27\ \mathrm{dB}.$$

**A $3.3\ \mathrm{dB}$ amplitude deficit** in the reflections below the
disturbance, with a lateral extent equal to its footprint. That is measurable, and
it is spatially coherent.

**Disruption of stratigraphy.** The natural horizon at, say, $0.4\ \mathrm{m}$
depth is truncated over the grave: the observable is the *absence* of an event
over a $1.0\ \mathrm{m}\times0.6\ \mathrm{m}$ area, against an $r_f$ of
$0.3$–$0.4\ \mathrm{m}$ at this depth. The footprint is $1.5$–$3$ Fresnel radii
across, so it is resolvable in extent to about one Fresnel radius.

**Conclusion, with the numbers.** The reflection is the weakest of the three
observables ($-40\ \mathrm{dB}$, $30\ \mathrm{dB}$ below a strong contrast); the
shadow is marginal on its own ($3.3\ \mathrm{dB}$) but coherent; the truncation of
a natural horizon is the most robust, because it is a pattern whose lateral extent
is $1.5$–$3$ Fresnel radii and whose amplitude does not depend on the permittivity
contrast of a single boundary at all. A report that claims detection on the
strength of a $3.3\ \mathrm{dB}$ anomaly alone would be overstating the evidence;
a report that shows the truncated horizon *and* the shadow beneath it is making a
claim the data can support.
