# Solutions — 06-09-02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [02 Processing Flow](../02-processing-flow.md).

---

## ★1 — Moveout at 1500 m

$$t(x) = \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}}
= \sqrt{1.0^{2} + \left(\frac{1500}{2500}\right)^{2}}
= \sqrt{1.0 + 0.36} = \sqrt{1.36} = 1.166190\ \mathrm{s},$$
$$\Delta t = t(x) - t_0 = 0.166190\ \mathrm{s} = 166.2\ \mathrm{ms}.$$

The moveout is $17\%$ of $t_0$ at this offset: it is a *large* number compared
with the timing precision needed for velocity analysis, which is the point of
lesson 03.

---

## ★2 — Hyperbolic time and residual at long offset

$$t_{\text{hyp}} = \sqrt{1.4251^{2} + \left(\frac{3002}{2848.1}\right)^{2}}
= \sqrt{2.030910 + 1.110905} = \sqrt{3.141815} = 1.772542\ \mathrm{s}.$$

The demonstration prints $1.7725\ \mathrm{s}$ — agreement to $4\times10^{-5}\
\mathrm{s}$. The exact (ray-traced) time at that offset is $1.7679\ \mathrm{s}$,
so the residual is

$$\text{exact} - \text{hyperbolic} = 1.7679 - 1.7725 = -4.6\ \mathrm{ms},$$

printed as $+4.565\ \mathrm{ms}$ in magnitude. The sign matters: the hyperbola is
*late* at long offset, and the residual grows from $0.005\ \mathrm{ms}$ at
$500\ \mathrm{m}$ to $12.2\ \mathrm{ms}$ at $3992\ \mathrm{m}$. The maximum
residual over the whole spread is $79.06\ \mathrm{ms}$ for this three-layer
model, i.e. the hyperbolic approximation breaks down at large offsets — which is
exactly what anellipticity corrections exist for.

---

## ★3 — Derivation from the mirror-image geometry

Place the source at the surface at $x = 0$, the receiver at $x$, and the
interface at depth $h$ with constant velocity $v$ above it. Reflect the source
in the interface; the reflected image sits at depth $h$ *below* the interface,
i.e. at distance $2h$ below the surface. The reflected ray from the source to
the interface and up to the receiver is a straight line from the image to the
receiver. Its length is the hypotenuse of a right triangle with legs $x$ and
$2h$:

$$\ell = \sqrt{x^{2} + (2h)^{2}}.$$

Since the whole path is travelled at the single speed $v$,

$$t(x) = \frac{\ell}{v} = \frac{\sqrt{x^{2}+4h^{2}}}{v}.$$

Now use $t_0 = 2h/v$, so $4h^{2} = v^{2}t_0^{2}$:

$$t(x) = \frac{\sqrt{x^{2}+v^{2}t_0^{2}}}{v}
= \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}}.
\quad\checkmark$$

**Where constant velocity is assumed.** Twice: (i) the image construction puts
the virtual source at $2h$ below the surface, which is only valid if the ray is
straight, i.e. if the velocity above the interface is constant; and (ii) the
travel time is the path length divided by a *single* $v$. For a layered
overburden neither holds, and one uses $v_{\text{rms}}$ — an approximation whose
residual is the anellipticity term measured in ★2.

---

## ★4 — Stacking improvement against the $\sqrt{N}$ law

| fold $N$ | predicted $\sqrt{N}$ | measured | measured/predicted |
|---|---|---|---|
| 4 | 2.00 | 2.04 | 1.020 |
| 8 | 2.83 | 2.98 | 1.053 |
| 16 | 4.00 | 4.48 | 1.120 |

The measured improvement is **better** than $\sqrt{N}$ in every case, and the
excess grows with fold. Two benign explanations, both worth checking before
quoting it as a property of the data: the metric is a ratio of rms values outside
the arrival window, and with a single finite realisation its sampling error is
of the order of $1/\sqrt{(\text{number of independent samples})}$; and the
noise realisation may be slightly correlated *within* each trace, which inflates
the single-trace rms that appears in the denominator. The defensible statement is
that the improvement **tracks** $\sqrt{N}$ to within about $12\%$ at 16-fold,
which is the claim the lesson makes.

---

## ★5 — What a coherent event would do

If the coherent event averaged down like random noise, at $N = 16$ the ratio
would be improved by $\sqrt{16} = 4$:

$$\text{ratio}_{\text{random}} = \frac{1.000}{4} = 0.250 .$$

The measured ratio is $0.916$ — i.e. the coherent event was attenuated by only
$8.4\%$ instead of $75\%$. A coherent event with a *different moveout* is
summed with a varying phase, but it does not cancel: it **stacks
constructively wherever its own moveout is stationary**. Since the standard
stack is tuned to the primary's moveout, the coherent event is smeared rather
than removed, and its residual amplitude is roughly the fraction of the spread
over which its moveout is close to the primary's.

**That is why SRME and Radon methods exist:** they model or transform the
multiple using its *moveout* (or its generation mechanism), instead of relying
on the stacking average to suppress it. Stacking alone cannot do the job, and
the measured $0.916$ is the demonstration.

---

## ★★★7 — Processing sequence for a water-bottom multiple (specification)

| # | step | why here | QC that would show failure |
|---|---|---|---|
| 1 | Geometry, amplitude recovery, brute stack | needs a section to see the multiple at all | stacking chart consistency; flat water bottom on the brute stack |
| 2 | Deterministic deconvolution (source signature, or a gap/designature) | shortens the wavelet so later steps see separated events | autocorrelation of the output shows the shortening; primary/multiple ratio improves |
| 3 | Velocity analysis (semblance + DMO) | NMO needs a velocity, and the multiple has its own, lower velocity | semblance peaks are stable across the offset ranges; a multiple pick is not mixed with the primary |
| 4 | NMO + mute | removes the multiple's long-offset tail before stacking | muted energy map; multiple event amplitude after mute |
| 5 | Radon (parabolic) demultiple + inverse transform | attacks the multiple's residual curvature using a *moveout* criterion | round-trip residual of the transform; primary preservation and multiple attenuation, both quoted as numbers |
| 6 | SRME (surface-related multiple elimination) | predicts the multiple from the data itself, for multiples the Radon cannot separate | predicted-multiple adaptive-subtraction residual; not-blowing-up check on the primary |
| 7 | Predictive deconvolution | removes short-period multiples with a constant lag | the multiple's amplitude, but check the wavelet length it also changes |
| 8 | Migration (Kirchhoff or RTM) | positions energy; must come after demultiple or the multiples migrate to false structure | image focus versus migration velocity (lesson 04) |

The order is forced by dependencies, not taste: a demultiple step **must**
precede migration (otherwise the multiple is imaged as coherent structure), and
velocity analysis **must** precede the Radon transform (the transform is
parametrised by curvature, which needs a velocity). The failure mode of any
cascade is over-processing, so each step's QC has to be a *number* printed
alongside the result.

---

## ★★★8 — NMO stretch bias versus stacking-time quantisation

**Which number limits a stacked pick.** The demonstration's stacked peak sits at
$1.428\ \mathrm{s}$ against an expected $1.4251\ \mathrm{s}$: a difference of

$$1.428 - 1.4251 = 0.0029\ \mathrm{s} = 2.9\ \mathrm{ms}.$$

The hyperbolic-versus-exact residual is $12.2\ \mathrm{ms}$ at the longest
offset tabulated and up to $79.06\ \mathrm{ms}$ over the whole spread. So the
**approximation**, not the stacking quantisation, is the larger term — but the
two act in *opposite* senses: NMO stretch (applying a single hyperbolic moveout
to a wavelet) shifts the stacked event to *earlier* time at far offset, and the
higher-order residual leaves the far-offset train *late*. The net $2.9\
\mathrm{ms}$ is the difference between two effects of the same order, which is
why a stacked pick cannot be improved by simply averaging more traces.

**Measurement that separates them.**

1. Build the same synthetic gather twice: once by ray tracing (exact) and once
   by the hyperbolic NMO operator, with *identical* noise and fold.
2. Stack both, and compute the pick difference as a function of (i) the
   maximum offset and (ii) the number of traces muting the stretched
   far-offset samples. Extrapolate the curve to zero offset: the intercept is the
   quantisation + picking contribution, and the slope with offset is the
   residual term.
3. Repeat with a mute that discards the samples whose NMO stretch exceeds a
   stated fraction (the standard "stretch mute"): the difference between the
   muted and unmuted stacked times isolates the stretch contribution
   quantitatively.

The deliverable is a number with units for each term — e.g. "residual
$X\ \mathrm{ms}$ at $3\ \mathrm{km}$ offset, stretch $Y\ \mathrm{ms}$,
picking/quantisation $Z\ \mathrm{ms}$" — not a statement that stacking is
"accurate".
