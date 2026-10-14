# Solutions — 02-11-05 Comparative Planetary Physics and Interiors

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Earth values are **nominal** handbook
> characteristics; the moment-of-inertia factor is **nominal and rounded**. No
> values for other bodies are supplied here — use mission sources for those.

---

## ★1 — The two-layer moment of inertia

**(a)** Homogeneous sphere: $C = \tfrac25MR^2$, so $k = 0.4$. Point mass:
$C = 0$, so $k = 0$. Derivation of the first: with $\rho$ constant,
$C = \tfrac{8\pi}{3}\rho\int_0^R r^4\mathrm{d}r
= \tfrac{8\pi}{3}\rho\tfrac{R^5}{5} = \tfrac{8\pi}{15}\rho R^5$, and
$\rho = M/(\tfrac43\pi R^3)$, so
$C = \tfrac{8\pi}{15}\cdot\tfrac{3M}{4\pi R^3}R^5 = \tfrac25MR^2$ ✓.

**(b)** $f = 0.5$: $f^3 = 0.125$, $f^5 = 0.031\,25$;
$k = 0.4(0.031\,25\times3+0.968\,75)/(0.125\times3+0.875)
= 0.4\times1.0625/1.25 = \mathbf{0.34}$.

**(c)** $k = 0.4$ at $\alpha = 1$, by inspection: both the numerator and the
denominator bracket reduce to 1, and the body is homogeneous however its
"core" is labelled.

**(d)** Because $k = C/(MR^2)$ and, for a fixed $M$ and $R$, $C$ is maximised by
putting all the mass as far from the axis as possible — on the surface. The
homogeneous sphere already does that (given spherical symmetry), so no distribution
can exceed 0.4. Concentrating mass inward can only reduce $C$.

---

## ★2 — The two-layer inversion

**(a)** $f = 0.6$: $f^3 = 0.216$, $f^5 = 0.077\,76$. Solving
$0.33(0.216\alpha+0.784) = 0.4(0.077\,76\alpha+0.922\,24)$ gives
$0.071\,28\alpha+0.258\,72 = 0.031\,104\alpha+0.368\,896$, so
$0.040\,176\alpha = 0.110\,176$ and $\alpha = \mathbf{2.7423}$.

**(b)** $S = f^3\alpha+1-f^3 = 0.216\times2.7423+0.784 = 0.592\,34+0.784
= 1.376\,34$. With $\tfrac43\pi R^3 = 1.083\,21\times10^{21}$ m³,
$\rho_m = 5.972\times10^{24}/(1.083\,21\times10^{21}\times1.376\,34)
= \mathbf{4\,006}$ kg m⁻³.

**(c)** $\rho_c = 2.7423\times4006 = \mathbf{10\,985}$ kg m⁻³.

**(d)** Yes: 10 985 kg m⁻³ lies inside the handbook's span of 9900 (outer core,
top) to 13 100 kg m⁻³ (inner core, centre). So a core occupying 60 per cent of the
radius with a density contrast of 2.74 is admissible, and it is not the geometry
that the seismological core radius implies (0.546). That is the degeneracy: both
are consistent with $M$ and $k$.

---

## ★3 — Dynamo diagnostics

**(a)** $Rm = 1.256\,637\times10^{-6}\times5\times10^5\times2\times10^{-4}
\times1.5\times10^6 = \mathbf{188.5}$.

**(b)** $\tau_\eta = 1.256\,637\times10^{-6}\times5\times10^5\times(1.5\times10^6)^2
= 1.414\times10^{12}$ s $= \mathbf{4.48\times10^4}$ yr.

**(c)** $Rm = 188$ is **above** the threshold, which is of order tens. The margin
is about a factor of 5 to 20 depending on where in "tens" the true critical value
lies, so the conclusion is robust to a factor-of-two error in one input but not to
simultaneous factor-of-two errors in all three; the electrical conductivity is the
most uncertain input.

**(d)** $\tau_\eta$ is the time over which the field would decay by diffusion if
the fluid motion stopped — the field's "memory" in the absence of a dynamo.

---

## ★4 — Jeans escape

**(a)** Escape requires $\tfrac12mv^2 \ge GMm/r$, so the boundary case is
$v^2 = 2GM/r$. Comparing that energy with the thermal energy $k_BT$ defines
$\lambda = \dfrac{GMm}{k_BTr}$: the ratio of gravitational to thermal energy for
one molecule at the exobase.

**(b)** Since $v_{\text{esc}}^2 = 2GM/r$, we have $GM/r = v_{\text{esc}}^2/2$, so
$\lambda = \dfrac{m}{k_BT}\cdot\dfrac{v_{\text{esc}}^2}{2}
= \dfrac{v_{\text{esc}}^2m}{2k_BT}$ ✓.

**(c)** With $r = 6.871\times10^6$ m, $T = 1000$ K and
$m = 28.014\times1.660\,54\times10^{-27} = 4.652\times10^{-26}$ kg:

$$\lambda = \frac{6.6743\times10^{-11}\times5.972\times10^{24}\times4.652\times10^{-26}}
{1.380\,649\times10^{-23}\times1000\times6.871\times10^6}
= \frac{1.854\,6\times10^{-11}}{9.485\,4\times10^{-14}} = \mathbf{195.5}.$$

**(d)** $\lambda = 195.5 \gg 30$, so N₂ is **retained**. The threshold used is
$\lambda\gtrsim30$ for retention over billions of years; between about 10 and 30
the escape is slow but significant, and below about 10 it is fast.

---

## ★★5 — The degeneracy grid

**(a)** $f = 0.4$: $k = \mathbf{0.4000}$ ($\alpha=1$), $\mathbf{0.3798}$
($\alpha=2$), $\mathbf{0.3619}$ ($\alpha=3$), $\mathbf{0.3459}$ ($\alpha=4$).

**(b)** $\alpha = 3$: $k = \mathbf{0.3940}$ ($f=0.2$), $\mathbf{0.3619}$
($f=0.4$), $\mathbf{0.3228}$ ($f=0.6$), $\mathbf{0.3271}$ ($f=0.8$).

**(c)** Two pairs consistent with $k = 0.36$: $(f,\alpha) = (0.4, 3.11)$ and
$(0.5, 2.23)$. (Both give $k = 0.360$ to three decimals.) Distinguishing them
requires a measurement that fixes $f$ or $\alpha$ independently: the core radius
from seismology or geodesy, an equation of state that fixes $\alpha$ from
composition, or a higher-order gravity coefficient that constrains the radial
distribution more tightly than a single scalar.

**(d)** Because self-compression lowers $k$ with no compositional change at all: a
larger body of the *same* composition compresses more, has a higher central
density and a lower $k$. So a low $k$ establishes only that there is dense
material toward the centre; separating "dense because compressed" from "dense
because it is iron" requires an equation of state, which requires a composition
assumption — a circularity that is broken only by additional measurements.

---

## ★★6 — Diffusion timescales compared

**(a)** $\tau_\kappa = (1.5\times10^6)^2/10^{-5} = 2.25\times10^{17}$ s
$= \mathbf{7.13\times10^9}$ yr.

**(b)** $\tau_\kappa/\tau_\eta = 2.25\times10^{17}/1.414\times10^{12}
= \mathbf{1.59\times10^5}$. The magnetic field's diffusion time is five orders of
magnitude shorter than the thermal one.

**(c)** $7.13\times10^9$ yr is **1.6 times** the age of the Earth
($4.5\times10^9$ yr). A core that could remove its heat only by conduction would
still be nearly isothermal after 4.5 Gyr, i.e. its heat would effectively be
trapped. The conclusion is that the core **must convect** — conduction cannot
carry the heat out on the available time.

**(d)** Because the same convection that transports the heat also provides the
flow with $Rm\gg1$ that the dynamo needs. The thermal requirement and the magnetic
requirement are satisfied by one mechanism, which is why the geodynamo is robust:
it does not depend on a coincidence, only on the core not being able to conduct
its heat away fast enough.

---

## ★★7 — Selectivity of escape

**(a)** From $\lambda = GMm/(k_BTr)$, mass enters only through $m$ in the
numerator, so at fixed $M$, $r$ and $T$ the parameter is **linear in $m$**.

**(b)** $\lambda(\text{H}_2) = 195.5\times2.016/28.014 = \mathbf{14.1}$;
$\lambda(\text{He}) = 195.5\times4.003/28.014 = \mathbf{27.9}$. H₂ is at the
margin of escape and He is at the low end of "slowly lost"; both agree with the
demo's table.

**(c)** With $M\to M/10$ and $r\to r/2$, the factor is
$(1/10)/(1/2) = 0.2$:
$\lambda(\text{H}_2) = 14.1\times0.2 = \mathbf{2.82}$;
$\lambda(\text{N}_2) = 195.5\times0.2 = \mathbf{39.1}$;
$\lambda(\text{CO}_2) = 307.1\times0.2 = \mathbf{61.4}$.

**(d)** The body loses H₂ quickly ($\lambda = 2.8 \ll 10$) and retains N₂ and CO₂
($\lambda = 39$ and 61, both above about 30). The selection rule is simply
$\lambda\propto m$: the lightest species have the smallest gravitational binding
relative to their thermal energy, so they escape first, and the residual atmosphere
is enriched in heavy molecules. This is the mechanism that produced the
terrestrial planets' secondary atmospheres.

---

## ★★8 — Scale height and escape together

**(a)** $H = k_BT/(mg)$ is **inversely** proportional to $m$;
$\lambda = GMm/(k_BTr)$ is proportional to $m$. The two have opposite
dependencies on the molecular mass.

**(b)** A heavy species has a small $H$, so its density falls off rapidly with
height and only a thin layer is exposed to escape — and simultaneously a large
$\lambda$, so the exposed molecules cannot escape anyway. A light species has a
large $H$, so it extends far out where escape is possible, and a small $\lambda$,
so escape is energetically easy. Both effects point the same way, which is why
selective escape is such a sharp filter.

**(c)** The error is the sign of the argument. A large $H$ means the species
extends to great heights where the gravitational binding is weakest, and it
corresponds to a *small* $\lambda$. A thick, puffy atmosphere is precisely the
vulnerable one; the Earth's heavy, thin N₂/O₂ atmosphere is the retained one, and
its species have the *smallest* scale heights.

**(d)** Two properties: the molecular mass $m$, which enters both $H$ and
$\lambda$, and the exobase temperature $T$, which also enters both (and inversely
in $\lambda$). $T$ is set by radiation and is not a property of the molecule, which
is why escape rates change with stellar activity.

---

## ★★★9 — The inference loop without seismology

**(a)** *Measured*: mass, radius, the moment-of-inertia factor, the rotation rate
and the gravity field (and, where available, a Love number or a libration
amplitude). *Assumed*: a composition and a thermal state, hence an equation of
state. *Computed*: the hydrostatic structure and the implied $M$, $R$, $k$.
*Compared*: the computed values with the measured ones, over a grid of assumed
compositions and thermal states.

**(b)** Because the number of unknowns exceeds the number of constraints. Even in
the simplest parameterisation, a two-layer model has three unknowns ($f$, $\alpha$
and the absolute density scale) and only two hard constraints ($M$ and $k$),
giving a one-parameter family. Add a third layer, a temperature gradient and a
distribution of light elements and the family becomes a high-dimensional region.
A single answer would require as many independent constraints as unknowns.

**(c)** Three examples, each supplying one constraint: (i) a **moment of inertia**
from the degree-2 gravity field and the rotation, constraining the radial
distribution of mass; (ii) a **tidal Love number $k_2$** from a flyby or an
orbiter, constraining the response of the body to a known forcing and hence its
rigidity and internal layering; (iii) a **libration amplitude** of a body locked in
a spin–orbit resonance, constraining whether a decoupled liquid layer exists, since
a floating shell librates differently from a solid one.

**(d)** The Earth is the only body whose interior is known in detail, so it is the
only place where a given set of $M$, $R$, $k$ can be compared against a
seismologically determined structure. Every prior used to interpret another body —
core density contrasts, mantle mineralogies, equations of state — is calibrated
there. The extrapolation difficulty is therefore not in gravity, which is exact,
but in the **equation of state at conditions** (pressure, temperature,
composition) that have never been sampled, which is the difficulty identified in
lesson [02](../02-equations-of-state.md) §6.

---

## ★★★10 — Dynamo criteria and the observed pattern

**(a)** (i) A **conducting fluid region**, because the induction term
$\nabla\times(\mathbf u\times\mathbf B)$ requires free charges that can move with
the flow; a solid or an insulator cannot support it. (ii) An **energy source**
driving convection in that region, because the field's Ohmic dissipation must be
continuously replaced; a stably stratified, motionless core produces no dynamo.
(iii) **Rotation**, because the organising effect of the Coriolis force is what
makes the flow coherent and large-scale rather than small-scale and tangled; a
non-rotating dynamo is possible in principle but is not what the planets show.

**(b)** Two candidate explanations: (i) Venus has a **stagnant lid** — a single
plate with no subduction — so its core heat has no efficient escape route and the
core may be stably stratified or not convecting vigorously; (ii) Venus rotates
extremely slowly, so the organising effect of point (a)(iii) is weak. These are
distinguishable in several ways: a measurement of the present-day surface heat
flow (or the elastic lithosphere thickness) tests the stagnant-lid argument
directly; a determination of the core size and state from future seismology or
gravity would test whether the core is convecting; and the absence of a field is
*not* by itself discriminating, since both explanations predict it.

**(c)** Because Mars retains strong **crustal remanent magnetization**, which is
fossil evidence of an ancient field: the dynamo operated early and then shut down.
So the complete statement is "Mars has no present-day global dynamo field, but had
one early in its history, and the shutdown is the phenomenon to be explained" —
the small size of the body, rapid cooling and eventual stable stratification of the
core being the leading candidates. The distinction matters because a body that
never had a dynamo and a body that stopped having one are different problems.

**(d)** A dynamo acting in a thin outer shell with the geometry of the Earth's
would produce a field dominated by an axial dipole, because the flow's geometry is
constrained by the spherical shell. Uranus and Neptune instead have strongly
tilted and strongly **offset** dipoles, which requires the dynamo region to be a
thick shell whose geometry permits a non-axisymmetric, off-centre field. So the
statement is not merely "they have dynamos" but "their dynamos act in a geometry
different from the Earth's", which constrains the depth and thickness of their
conducting regions — a much stronger inference.

---

## ★★★11 — Sensitivity and honest reporting

**(a)** Numerically at $(f,\alpha) = (0.5462, 3.039)$:
$\partial k/\partial f = \mathbf{-0.1796}$ and
$\partial k/\partial\alpha = \mathbf{-0.02577}$ per unit of the respective
variable. The ratio is **6.97**, so $k$ is about seven times more sensitive to the
core radius fraction than to the density contrast.

**(b)** Holding $f = 0.5462$ fixed: $k = 0.33$ gives $\alpha = 3.0391$ and
$\rho_c = 12\,577$ kg m⁻³; $k = 0.3308$ gives $\alpha = 3.0082$ and
$\rho_c = 12\,496$ kg m⁻³. So $\Delta\alpha = -0.031$ and
$\Delta\rho_c = \mathbf{-81}$ kg m⁻³, i.e. $-0.64$ per cent.

**(c)** The core **radius fraction $f$**. Because $k$ responds to $f$ seven times
more strongly than to $\alpha$, a given uncertainty in $k$ translates into a
seven-times-larger relative uncertainty in $f$ than in $\alpha$ — equivalently, a
small error in $f$ masquerades as a large error in $\alpha$ when (a) is inverted.
So it is the *length* that limits the density, which is why seismic core radii
matter so much.

**(d)** Three defensible sentences, using only computed numbers:

> A two-layer model of the Earth, with the core radius fraction fixed at the
> seismological value 0.546, reproduces the nominal moment-of-inertia factor
> $C/(MR^2) = 0.33$ with a core/mantle density contrast of 3.04 and a mean core
> density of $1.26\times10^4$ kg m⁻³. Because $k$ is roughly seven times more
> sensitive to the core radius fraction than to the density contrast, that density
> is meaningful only to the extent that the core radius is known independently.
> The dominant systematic is therefore the two-layer assumption itself rather than
> the numerical value of $k$: a continuous core with a density gradient would
> displace this result by a comparable amount.

Note what the report does not do: it does not call $1.26\times10^4$ kg m⁻³ a
measurement, and it names the assumption that limits the answer.

---

## ★★★12 — What would falsify the claims

**(a)** *Claim*: a low $k$ requires a metallic core. *Falsified by*: a body whose
$k$ is low but which is measurably homogeneous in the relevant elements — for
instance a large icy body whose low $k$ is entirely produced by self-compression
of a single material. *Currently available?* Partly: the necessary measurements
(moment of inertia plus an independent constraint on composition) exist for a few
bodies, and the general statement is already known to be false as written, because
self-compression lowers $k$ with no core at all.

**(b)** *Claim*: crustal remanence implies a past dynamo. *Falsified by*: a
demonstration that the magnetization could have been imparted by an externally
imposed field — from a nearby star, a companion, or the interplanetary field during
a period of high plasma flux. *Currently available?* Not decisively; this is an
active question, and it is one of the standard caveats attached to the Mars
result.

**(c)** *Claim*: no present-day field implies a failed dynamo requirement.
*Falsified by*: a body with no field whose core is demonstrably convecting, rotating
and conducting. *Currently available?* No — such a body would be a serious puzzle
and none is established, which is why the three-requirement framework survives.

**(d)** *Claim*: Jeans escape alone explains a terrestrial atmosphere's
composition. *Falsified by*: evidence that a substantial fraction of the inventory
was lost by a non-thermal mechanism or by a giant impact. *Currently available?*
Partly. For the Earth, the loss of hydrogen is largely limited by the upward
transport of water rather than by Jeans escape itself, and hydrodynamic escape
matters for early, hot atmospheres; so the claim is known to be too strong even
though Jeans escape is a useful first framework.
