# Solutions — 05-07-03 Integrating Multiple Methods and Constraints

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; grid searches repeated here state their grid
> size. All resistivities, thicknesses and tolerances are SYNTHETIC.

Constants: $\mu_0 = 4\pi\times10^{-7}$ H m⁻¹. Model throughout:
$\rho_1 = 100$ Ω m, $h_1 = 100$ m, target layer $\rho_2$ and $h_2$, basement
$\rho_3 = 500$ Ω m, periods 0.01–1000 s (21 log-spaced).

---

## ★1 — Half-space validation

**(a)** With $k = \sqrt{\mathrm{i}\omega\mu_0/\rho}$ and
$Z = \mathrm{i}\omega\mu_0/k$,

$$|Z|^2 = \frac{(\omega\mu_0)^2}{|k|^2} = \frac{(\omega\mu_0)^2}{\omega\mu_0/\rho}
= \omega\mu_0\rho
\;\Longrightarrow\;
\rho_a = \frac{|Z|^2}{\omega\mu_0} = \rho .$$

(The measured maximum relative error is $4.44\times10^{-16}$, i.e. floating-point
round-off.)

**(b)** It is an identity of the definitions, so it tests the *implementation* —
sign conventions, branch of the square root, unit consistency — and says nothing
about whether the Earth is a half-space. Any inversion built on an operator that
fails this test is worthless, which is why it is the first section of the
demonstration.

---

## ★2 — Conductances

**(a)** $S = 50/1 = 50$ m Ω⁻¹.
**(b)** $S = 100/2 = 50$ m Ω⁻¹.
**(c)** $S = 500/5 = 100$ m Ω⁻¹.
**(d)** $S = 1000/20 = 50$ m Ω⁻¹.

(a), (b) and (d) have equal conductance; (c) does not and is distinguishable on
that ground alone. But (d) is only equivalent in the thin-layer regime: the
demonstration measures its log₁₀ deviation from the $(50, 1)$ model as 0.0109,
against 0.0000, 0.0006 and 0.0017 for the first three. At $h = 1000$ m the layer
is no longer thin compared with the skin depth, so the first-order argument of
equation (2) of the lesson fails.

---

## ★3 — Ambiguous versus insensitive

**Ambiguous:** the data depend on the parameter, and a one-parameter family of
values fits within the tolerance. *Example:* $h_2$ versus $\rho_2$ in the target
layer — a curve of pairs fits the MT sounding.

**Insensitive:** the data barely depend on the parameter, so it is barely
determined at all. *Example:* the *sharpness* of the boundary, for any transition
thinner than about 50 m, which no tolerance in the sounding can resolve.

The demonstration shows the distinction directly: the basement resistivity
$\rho_3$ is *not* insensitive (a factor of two changes the response by 92.8 per
cent), while $h_2$ and $\rho_2$ *are* ambiguous.

---

## ★4 — Feasible set at two tolerances

Computed on a 400 × 400 grid (400 thicknesses, 400 resistivities):

| Tolerance | Models | $h_2$ range (m) | $\rho_2$ range (Ω m) | $S$ range (m Ω⁻¹) | Spread $h_2$ | Spread $S$ |
|---|---|---|---|---|---|---|
| 1 per cent | 75 | 275–327 | 9.28–10.66 | 29.3–30.8 | 17.1 % | 5.0 % |
| 3 per cent | 698 | 226–386 | 7.86–12.42 | 27.5–32.8 | 52.6 % | 17.6 % |

**(a)** At 1 per cent: 75 models, $h_2$ 275–327 m, $S$ 29.3–30.8 m Ω⁻¹.

**(b)** At 3 per cent: 698 models, $h_2$ 226–386 m, $S$ 27.5–32.8 m Ω⁻¹.

**(c)** Thickness/conductance spread ratio: $17.1/5.0 = 3.4$ at 1 per cent and
$52.6/17.6 = 3.0$ at 3 per cent. **The conductance is constrained about three
times better than either factor, at both tolerances** — the trade-off direction is
set by physics (equation 2 of the lesson), not by the tolerance. The tolerance sets
how far along the curve you are willing to go; it does not change the direction.

---

## ★5 — What the seismic constraint buys

**(a)** Before: $h_2$ 278–327 m, $\rho_2$ 9.44–10.72 Ω m (the demo's 200 × 200
grid). After the 300 ± 15 m seismic pick: 15 of 21 models survive,
$h_2$ 286–315 m, $\rho_2$ 9.44–10.45 Ω m.

**(b)** $(10.72-9.44)/(10.45-9.44) = 1.28/1.01 = 1.3$.

**(c)** The seismic datum is sensitive to *thickness* and essentially insensitive
to resistivity. The MT feasible set is a curve of near-constant conductance; a
thickness constraint cuts the curve at one point *along* its length, removing the
ends but leaving the local direction (the conductance trade-off) untouched. Only a
constraint whose sensitivity has a component *across* the curve — an independent
conductivity measurement — can shorten the curve's width, and even then only by
the amount that the two constraint directions are non-parallel.

Reference: [18-07-01 Why Joint Inversion: Complementary
Sensitivities](../../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md).

---

## ★6 — The conflict, quantified

Computed on the same 400-value resistivity grid:

| Seismic pick $h_2$ (m) | Best MT log-misfit | Ratio to the 1 per cent tolerance |
|---|---|---|
| 150 | 0.0658 | 6.6 |
| 200 | 0.0415 | 4.2 |
| 400 | 0.0337 | 3.4 |

**(a)** 0.0658, ratio 6.6.

**(b)** 4.2 and 3.4 respectively.

**(c)** The misfit falls inside the 1 per cent tolerance only for
$h_2 \approx 275$–327 m, the feasible set itself. Both a *too-thin* and a
*too-thick* pick are rejected, and by comparable factors (6.6 and 3.4). The
inconsistency is therefore not a simple bias in one direction — it is a failure of
one of the two models. The likely candidates, in order of frequency in practice:
a mis-picked multiple on the seismic section, a static shift or 3-D effect in the
MT, and a genuinely laterally varying layer that neither 1-D model represents.

---

## ★7 — Boundary sharpness

**(a)** With the boundary at 400 m and the target layer subdivided into a sharp
part plus a 20-sub-layer logarithmic ramp:

| Ramp thickness | log-RMS vs sharp boundary |
|---|---|
| 25 m | 0.0076 |
| 100 m | 0.0314 |
| 200 m | 0.0659 |

A 25 m ramp is inside the 1 per cent tolerance and indistinguishable from sharp; a
100 m ramp already requires 3.1 per cent misfit and is rejected. Interpolating, the
transition becomes distinguishable at roughly **50 m**.

**(b)** A 50 m bound distinguishes a sharp fault from a several-hundred-metre
gradational contact, which is often the geological question. It does *not*
distinguish a 10 m transition from a 0 m one, so "sharp" must be reported as
"thinner than about 50 m", not as "sharp". Where the question is whether a
transition zone is a permeability barrier or a gradual seal, 50 m may or may not
be adequate — and only the geologist can say.

**(c)** A tighter bound requires a measurement with shorter spatial sensitivity:
a borehole log across the boundary, a core, or a higher-frequency method
(GPR or a shallow seismic reflection) whose wavelength is comparable with the
transition thickness. This is the transverse-sensitivity criterion again, applied
in the *length-scale* direction rather than in parameter space.

---

## ★8 — A resolution study (worked outline)

A worked answer is a template; the numbers depend on the chosen target. The
structure that earns full marks:

**(a)** Primary method with its kernel. For a gravity survey:
$K_g(\mathbf{r}, \mathbf{r}') \propto z'/|\mathbf{r}-\mathbf{r}'|^3$, decaying as
$z^{-2}$ in amplitude at fixed mass, with a null space consisting of all harmonic
source distributions with zero moment.

**(b)** Null-space direction: the equivalent stratum — mass can be moved along
$z$ with the density rescaled to preserve the field. Formally the annihilator is
the set of harmonic $\Delta\rho$ with zero moments.

**(c)** A transverse second method: seismic reflection travel times (sensitive to
depth of interfaces, not to density), or gravity gradiometry (different $z$
weighting of the same density). Seismic gives interface depths, which restrict
the *supported* part of the gravity model to the depth range between reflectors;
the feasible-set reduction is then the ratio of the allowed depth range to the
original, raised to the power set by the falloff — a factor of order $(z_1/z_2)^3$
per unit mass for a factor-$z$ depth reduction.

**(d)** Assumptions: the reflectors bound the density contrasts; the seismic is
correctly depth-converted (a 5 per cent velocity error is a 5 per cent depth
error, §3.2 of the ground-truthing lesson); densities are constant between
reflectors. Falsification: a borehole that finds a density contrast at a depth
with no corresponding reflector, which invalidates the depth-bounding assumption
and reopens the null space. Report the ratio and the assumptions together; a
reduction factor without its assumptions is a number, not a result.
