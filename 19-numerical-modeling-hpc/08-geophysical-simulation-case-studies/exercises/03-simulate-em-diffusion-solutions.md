# Solutions — 19-08-03 Simulating EM Diffusion in Conductive Media

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [03 Simulating EM Diffusion in Conductive Media](../03-simulate-em-diffusion.md).

---

## ★1 — Skin depth two ways

$\omega = 2\pi f = 0.31416$ s$^{-1}$, $\omega\mu_0 = 3.9478\times10^{-7}$
$\Omega$ m$^{-1}$:

$$\delta = \sqrt{\frac{2\times50}{3.9478\times10^{-7}}}
= \sqrt{2.5330\times10^{8}} = 15915\ \mathrm{m},$$

$$503.29\sqrt{\frac{50}{0.05}} = 503.29\sqrt{1000} = 503.29\times31.6228
= 15915\ \mathrm{m}.$$

They agree to five figures: the constant $503.29 = 1/\sqrt{\pi\mu_0}$ is derived,
not remembered, and the two expressions are algebraically identical.

---

## ★2 — Conductance

$$S = \frac{h}{\rho} = \frac{200}{40} = 5.0\ \mathrm{S}.$$

Conductance is additive in layers in series, so a stack of thin layers is
characterised at long periods by the sum of their conductances — the reason a
sounding cannot separate the individual layers in that limit.

---

## ★3 — The $45^\circ$ phase

For a uniform half-space $Z = \sqrt{\mathrm{i}\omega\mu_0\rho} =
\sqrt{\omega\mu_0\rho}\,e^{\mathrm{i}\pi/4}$, so the phase is exactly
$\pi/4 = 45^\circ$ regardless of the resistivity, the frequency and the units. The
phase therefore carries **no information about a uniform Earth**; departures from
$45^\circ$ measure the *distribution* of conductivity with depth, which the
amplitude alone cannot resolve because apparent resistivity is a weighted average.
That is the reason every magnetotelluric interpretation plots both.

---

## ★4 — Where conductance equivalence becomes visible

Two points give the scaling: $1.939$ per cent at $0.1$ s and $0.625$ per cent at
$1$ s, a ratio $3.102$ for a factor of $10$ in period, so the difference varies
approximately as $T^{-0.492}$. Setting $0.625(T/1)^{-0.492} = 5$:

$$(T)^{-0.492} = 8 \;\Longrightarrow\; T = 8^{-1/0.492} = 8^{-2.033}
= 0.0147\ \mathrm{s}.$$

**Assumption:** the power law fitted to those two points continues to shorter
periods. It does not have to: below the layer's internal diffusion time the response
becomes sensitive to the individual parameters and the difference saturates rather
than growing without bound. The honest procedure is to compute the response at the
candidate periods rather than to extrapolate a fit.

---

## ★5 — Diffusion length and the remaining fraction

$$D = \frac{\rho}{\mu_0} = \frac{10}{1.2566\times10^{-6}} = 7.9577\times10^{6}\ \mathrm{m^{2}s^{-1}},
\qquad \sqrt{Dt} = \sqrt{7.9577\times10^{3}} = 89.2\ \mathrm{m}.$$

The argument of the error function at $100$ m is $100/(2\times89.2) = 0.5605$, and
$\mathrm{erfc}(0.5605) \approx 0.427$. So **43 per cent** of the surface step
remains at $100$ m after $1$ ms. For reference $\mathrm{erfc}(0.5) = 0.4795$, so
the field is decaying roughly linearly in this range; and note that no wavefront
appears — the field is non-zero at every depth for every positive time.

---

## ★6 — The node-aligned interface defect

**Mechanism.** The scheme approximates $E''$ with a three-point stencil and samples
$\sigma$ at nodes. If a layer boundary lies exactly on a node, then $E''$ jumps at
that node while the stencil assumes a smooth $E$ across it; the local truncation
error there is $O(1)\times\Delta z$ rather than $O(\Delta z^{2})$, and the global
error loses an order. The measured sequence $2.06$ per cent (boundary *between*
nodes, $\Delta z = 200$ m), then $9.43$, $4.86$, $2.47$ per cent at $100$, $50$,
$25$ m shows exactly this: the errors halve with each refinement (order $1$) once
the boundary is node-aligned, and the finest grid is worse by a factor of $5$ than
the unaligned coarse one.

**Fixes.** (i) Place layer boundaries on cell faces, so that each cell lies within
one layer and the stencil never straddles a discontinuity; (ii) solve the
*flux-conservative* form for the field whose flux is continuous, so that the
interface condition is enforced by the discretisation rather than assumed
(the magnetic field in this problem). Either way, the choice must be stated, since
two codes differing in it will disagree by the size of their errors.

---

## ★7 — Separating a thin good conductor from a thick poor one

**Conductances.** Model A: $S = 300/5 = 60$ S. Model B: $S = 150/2.5 = 60$ S: the
same conductance, so the two are equivalent at long periods by construction.

**Periods where they differ.** The relevant internal diffusion time of the layer is
$T_i \sim \mu_0\sigma h^{2}$: for model A,
$4\pi\times10^{-7}\times(1/5)\times300^{2} = 4\pi\times10^{-7}\times1.8\times10^{4}
= 0.0226$ s; for model B,
$4\pi\times10^{-7}\times(1/2.5)\times150^{2} = 0.0113$ s. The two responses separate
at periods *shorter* than about $10\,T_i$, i.e. below roughly $0.2$ s; above about
$1$ s they are equivalent to well under a per cent. So the required period range
extends to $0.01$–$0.05$ s, which is measurable in principle.

**What limits the answer.** Two things. First, the *resolution* of the
above-layer response: the $500$ m of $200$ $\Omega$ m has its own diffusion time
$4\pi\times10^{-7}\times(1/200)\times500^{2} = 1.57$ s, so at $0.02$ s the field
barely penetrates that layer and the sensitivity to the deep layer is tiny in
absolute terms — the signal is a small fraction of a large near-surface response,
which is exactly the regime where galvanic distortion and near-surface
heterogeneity dominate. Second, the *noise*: a $2$ per cent apparent-resistivity
difference at $0.02$ s must exceed the measurement uncertainty, which is a
statement about the instrument, the site and the processing, not about the physics.

---

## ★8 — A defensible depth-of-investigation claim

**Diffusion length.** At $T = 100$ s ($f = 0.01$ Hz) in $\rho = 50$ $\Omega$ m,

$$\delta = 503.29\sqrt{\frac{50}{0.01}} = 503.29\times70.71 = 35588\ \mathrm{m}.$$

So the skin depth is about $36$ km, and the claimed $2$ km is only $0.056$ of it.
Because the field at depth $z$ scales roughly as $\exp(-z/\delta)$, a depth of
$0.056\delta$ corresponds to an amplitude ratio of $e^{-0.056} = 0.946$: the claim
of "penetration to $2$ km" is true but vacuous, since $95$ per cent of the surface
field is present there — no target would be detectable.

**The implicit threshold.** A common convention is that a target is detectable when
it perturbs the response by a few per cent, which corresponds to a depth of roughly
$0.1$–$0.2\delta$. The claim therefore implicitly assumes a threshold far smaller
than any measurement can use, and it does not state the target contrast.

**Rewritten claim.** "At a longest period of $100$ s over a $50$ $\Omega$ m
half-space the skin depth is $36$ km. A layer whose conductance is $S$ will perturb
the apparent resistivity by approximately ... (computed, not asserted) at this
period; for a target of conductance $60$ S the perturbation is $X$ per cent, so a
layer at $2$ km depth is detectable only if its conductance exceeds $S_{\min}$ as
computed here. The depth of investigation is stated with the target conductance,
the threshold and the period range, and no depth is quoted without them."

That is the form the lesson's later exercise on critical reading asks for: a
number, its threshold, and the target it applies to.
