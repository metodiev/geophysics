# Solutions — 06-12-02 Pore-Pressure Diffusion and Triggering Mechanisms

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [02 Pore-Pressure Diffusion and Triggering](../02-pore-pressure-triggering.md).

---

## ★1 — The front at one year

One year $= 365.2$ days $= 365.2 \times 86400 = 3.1553\times10^{7}\ \mathrm{s}$
(the demonstration's own year length).

$$r_c = \sqrt{4Dx_ct} = \sqrt{4 \times 0.1 \times 1.1977 \times 3.1553\times10^{7}}
= \sqrt{1.51156\times10^{7}} = 3887.0\ \mathrm{m} \approx 3.887\ \mathrm{km}.$$

The demonstration prints $3888.2\ \mathrm{m}$, the small difference being its exact
year length in seconds.

Units: $\mathrm{m^2\,s^{-1}} \times \text{dimensionless} \times \mathrm{s} =
\mathrm{m^2}$, whose square root is m ✔. The whole content of the front law is that
the radius grows as $\sqrt{Dt}$, so a *time* of arrival is converted into a
*distance* only through $D$.

---

## ★2 — Source strength from one pressure measurement

$$p(r,t) = \frac{Q}{4\pi D}E_1\!\left(\frac{r^2}{4Dt}\right)
\;\Longrightarrow\;
Q = \frac{4\pi D\,p}{E_1(r^2/4Dt)} .$$

$$Q = \frac{4\pi (0.1)(5.0\times10^{6})}{7.9500}
= \frac{6.2832\times10^{6}}{7.9500}
= 7.9034\times10^{5}\ \mathrm{Pa\,m^2\,s^{-1}},$$

which is the demonstration's printed value. Units: $[\mathrm{m^2\,s^{-1}}]\times
[\mathrm{Pa}] = \mathrm{Pa\,m^2\,s^{-1}}$ — a pressure change per unit time
integrated over area, which is what a line source strength is.

Note the structure of the result: the *shape* of the pressure field is set by $D$
alone, and the *amplitude* is set by $Q$. One pressure measurement at one place and
time therefore gives $Q$ given $D$, or $D$ given $Q$ — never both.

---

## ★3 — Why $D$ is quadratic in the radius

$$D = \frac{r_c^2}{4x_ct},$$

so a fractional error $\delta$ in $r_c$ produces a fractional error
$(1+\delta)^2 - 1 \approx 2\delta$ in $D$. For $\delta = 0.10$:

$$D \to D(1.10)^2 = 1.21D,$$

i.e. a **+21%** error in $D$. The physical reason is that seismicity locates a
*threshold crossing* of the pressure field, and the pressure falls only
logarithmically with radius in this regime, so a modest error in radius corresponds
to a large error in the diffusivity that would produce that field.

---

## ★4 — Constancy of $r/\sqrt{t}$

The demonstration's values: $r/\sqrt{t} = 0.693$ (30 d), then $0.692$ at each of
60, 120, 240, 365, 500 and 730 days. If $r = a^{1/2}t^{1/2}$, the ratio is exactly
constant, so the fitted exponent must be $1/2$ to within the scatter of those
rounded values.

Quantitatively, the spread of the seven values is $0.693 - 0.692 = 0.001$ by
inspection, and the demonstration reports the spread as
$0.0004\ \mathrm{m\,s^{-0.5}}$ — that is, about $0.06\%$ of the value $0.692$. A
constant of that precision over a factor of 24 in time determines the exponent to
about $0.06\%$ as well: the fitted value $0.499902$ differs from $0.5$ by
$0.02\%$. The exponent is therefore *measured*, not assumed, and the residual is
consistent with the reported spread.

---

## ★5 — Inferred diffusivity, two ways

$$x_c = 0.1298:\quad D_{\text{inferred}} = \frac{0.4792}{4 \times 0.1298}
= \frac{0.4792}{0.5192} = 0.9230\ \mathrm{m^2\,s^{-1}}$$

against the printed $0.9226$ ✔ (0.04% — rounding in the printed $x_c$).

$$x_c = 2.8454:\quad D_{\text{inferred}} = \frac{0.4792}{4 \times 2.8454}
= \frac{0.4792}{11.3816} = 0.04210\ \mathrm{m^2\,s^{-1}}$$

against the printed $0.0421$ ✔.

The two assumed thresholds differ by a factor of 100, and the inferred diffusivities
differ by a factor of $0.9230/0.0421 = 21.9$. Since the *measured* migration rate
$a$ is identical in both cases, this is the degeneracy stated concretely: the front
determines the product $Dx_c$, and every statement about $D$ alone is a statement
about the assumed threshold.

---

## ★6 — Systematic versus random location error

**Systematic bias.** If every hypocentral distance is multiplied by $(1+b)$, then
every measured front radius becomes $r_c(1+b)$, and since $D \propto r_c^2$,

$$D_{\text{fit}} = D_{\text{true}}(1+b)^2 .$$

For $b = 0.10$: $(1.10)^2 = 1.21$, i.e. a **+21%** bias, matching the
demonstration's $1.210$. Crucially the factor $(1+b)^2$ is the *same for every
event*: the bias is a multiplicative constant on each $r_i^2$, so it survives any
averaging and cannot be reduced by more data.

**Random error.** With independent location errors of $\sigma_{\text{loc}}$, each
$r_i$ is perturbed randomly. To first order the perturbation in $r_i^2$ is
$2r_i\delta r_i$, which averages to zero over events; the residual is second order
in $\delta r_i/r_i$, and the *spread* of the estimate falls as $1/\sqrt{N}$. The
demonstration's median fitted $D$ moves only from $0.1049$ (all 150 events) to
$0.0990$ using the single outermost event — a few per cent, with the price that
the $p_{90}/p_{10}$ spread grows from $1.12$ to $2.55$.

**Which reduces with more events:** the random term only. This is the practical
argument for spending effort on velocity-model accuracy (systematic) rather than
only on catalogue size (random).

---

## ★★★7 — Separating $D$ from $x_c$ (specification and impossibility argument)

**What is measured.** Event origin times and hypocentres, from which a migration
rate $a = \langle r^2/t\rangle$ is fitted. This is one number.

**What is inferred.** $D_{\text{inferred}} = a/(4x_c)$ requires $x_c$, and $x_c$ is
the solution of
$E_1(x_c) = (p_c/\Delta p_{\text{ref}})\,E_1(r_{\text{ref}}^2/4Dt)$ — a function of
the *threshold* pressure ratio, which depends on the failure criterion of the rock
and on the absolute pressure level. Seismicity alone gives $a$; it gives nothing
about $p_c$ or $\Delta p_{\text{ref}}$ separately, because the seismicity records
only the *arrival* of the threshold at each location.

**Proof that it cannot be done from seismicity alone.** Any pair
$(D, x_c)$ with the same product $Dx_c$ produces the *same* front arrival times at
every event location, so the two hypotheses are observationally identical in the
catalogue. The degeneracy is exact, not statistical.

**What breaks it.** An independent measurement of either the pressure field or the
threshold:

1. **Downhole pressure monitoring** in an observation well at distance $r$ gives
   $\Delta p(r,t)$ directly, hence $Q$ and therefore $D$ from the shape
   $E_1(r^2/4Dt)$ — a *different* functional dependence on $D$ than the front,
   which is why it breaks the degeneracy.
2. **Focal mechanisms and failure-state predictions**, to estimate $p_c/\Delta
   p_{\text{ref}}$ from the Coulomb criterion, though this substitutes one
   assumption for another.
3. **Tracer or rate tests** that measure permeability independently, since
   $D = k/(\mu S)$ combines permeability $k$, viscosity and storativity.

The honest report of a seismicity-only result is therefore a range of $D$ spanning
the plausible threshold ratios — the demonstration's own range is
$0.0421$ to $11.2411\ \mathrm{m^2\,s^{-1}}$, a factor of 267.

---

## ★★★8 — The $E_1$ solution (worked derivation)

**Start from the diffusion equation** for pressure in a homogeneous medium:

$$\frac{\partial p}{\partial t} = D\nabla^2 p + \frac{Q}{S}\,\delta^2(\mathbf r)\,H(t),$$

where $H(t)$ is the Heaviside step and $S$ the storage coefficient (folded into the
definition of $Q$ in the demonstration's units).

**Green's function.** The impulse response in two dimensions is the Gaussian

$$G(r,t) = \frac{1}{4\pi Dt}\exp\!\left(-\frac{r^2}{4Dt}\right),$$

whose integral over the plane is 1 for every $t$ — the mass-conservation property
the demonstration verifies to $3.45\times10^{-13}$ per cent.

**Convolution with a step source.** For a source switched on at $t = 0$ and held at
constant strength, superpose impulses from $\tau = 0$ to $t$:

$$p(r,t) = \int_0^{t} Q\,\frac{1}{4\pi D(t-\tau)}
\exp\!\left(-\frac{r^2}{4D(t-\tau)}\right)\mathrm{d}\tau .$$

Substitute $u = r^2/[4D(t-\tau)]$; then $\mathrm{d}\tau =
-\dfrac{r^2}{4Du^2}\mathrm{d}u$ and the integral becomes the exponential integral

$$p(r,t) = \frac{Q}{4\pi D}\int_{r^2/(4Dt)}^{\infty}\frac{e^{-u}}{u}\,\mathrm{d}u
= \frac{Q}{4\pi D}E_1\!\left(\frac{r^2}{4Dt}\right).$$

**Assumption about the boundary condition.** The pressure perturbation must vanish
at infinity ($p \to 0$ as $r\to\infty$); with a constant far-field pressure the
diffusion problem has the same Green's function but the perturbation is measured
relative to that constant. Nowhere is the pre-injection pressure gradient assumed
zero — but its *effect* on the perturbation is neglected, which is one of the
model's stated limitations.

**Why this matters for the front.** For small arguments, $E_1(x) \approx
-\gamma - \ln x$ with $\gamma = 0.5772$; a fixed pressure threshold therefore
crosses at $x_c$ roughly constant, giving $r_c^2 \approx 4Dx_ct$ and hence the
$t^{1/2}$ law. The demonstration's fitted exponent $0.499902$ is this approximation
measured, not imposed.

---

## ★★★9 — Anisotropic diffusion

The equation becomes

$$\frac{\partial p}{\partial t} = D_x\frac{\partial^2 p}{\partial x^2}
+ D_y\frac{\partial^2 p}{\partial y^2},$$

and a constant-rate line source gives a front at the *ellipse*
$x^2/(4D_xt) + y^2/(4D_yt) = x_c$, i.e. the front is stretched along the
high-diffusivity direction. For $D_x = 4D_y$ the front's long axis is twice the
short axis.

**What an isotropic fit recovers.** If the analyst fits a single radius to the
front — say by using the mean of the measured distances, or by fitting an
isotropic $\sqrt{t}$ law to the event cloud — the recovered value is a
*geometric-mean-like* quantity. The exact result depends on the estimator, but the
structure is fixed: for the ellipse parameterisation above, equal-area matching
gives

$$D_{\text{apparent}} \approx \sqrt{D_xD_y} = \sqrt{4D_y^2} = 2D_y,$$

so the analyst recovers twice the *smaller* diffusivity when the anisotropy ratio is
4. The estimate is therefore a genuine measurement of the two diffusivities only
through their geometric mean if the front is fully sampled in azimuth; if events
occur preferentially along one axis, the fit recovers a weighted combination and
can differ from $\sqrt{D_xD_y}$ substantially. The honest reporting includes the
azimuthal coverage of the event cloud — a theme the module returns to in
[05 Case Studies](../05-case-studies-induced.md).
