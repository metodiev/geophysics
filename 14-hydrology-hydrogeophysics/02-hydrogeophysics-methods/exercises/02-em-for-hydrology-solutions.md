# Solutions — 14-02-02 EM and TDEM for Groundwater Exploration

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All targets are **SYNTHETIC**.

Lesson: [02 EM and TDEM for Groundwater Exploration](../02-em-for-hydrology.md).

---

## ★1 — Skin depth, exact and approximate

Exact:
$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}
= \sqrt{\frac{2}{2\pi(50)(4\pi \times 10^{-7})(0.05)}}
= \sqrt{\frac{2}{1.9739 \times 10^{-5}}} = 318.31\ \mathrm{m}.$$

Approximate:
$$\delta \approx \frac{503}{\sqrt{f\sigma}} = \frac{503}{\sqrt{50 \times 0.05}}
= \frac{503}{1.5811} = 318.13\ \mathrm{m}.$$

Difference: $0.18$ m, i.e. **0.06%**. The $503$ constant is
$\sqrt{2/(2\pi \times 4\pi \times 10^{-7})}$ rounded; it is exact to the digits
shown, and the small residual here comes from rounding $503$ from
$503.29$. Use it freely, but know where it comes from — it is not a measured
constant.

---

## ★2 — Diffusion depth

$$z = \sqrt{\frac{2\rho t}{\mu_0}}
= \sqrt{\frac{2(25)(1 \times 10^{-3})}{4\pi \times 10^{-7}}}
= \sqrt{\frac{0.05}{1.2566 \times 10^{-6}}} = \sqrt{3.979 \times 10^{4}}
= 199.5\ \mathrm{m}.$$

**Interpretation.** After 1 ms a $25\ \Omega$ m ground has been sampled to about
200 m. Note what this number is *not*: it is the depth the diffusion front has
reached, not the depth of reliable resolution. In practice an inversion puts its
best-resolved boundary at perhaps half this depth, and every report should say
which convention it used.

---

## ★3 — Time to a depth

$$t = \frac{\mu_0 z^{2}}{2\rho}
= \frac{(4\pi \times 10^{-7})(150)^{2}}{2(20)}
= \frac{1.2566 \times 10^{-6} \times 22500}{40}
= 7.069 \times 10^{-4}\ \mathrm{s} = \mathbf{0.707\ ms}.$$

Check the scaling: reaching 150 m in $20\ \Omega$ m takes 0.707 ms; reaching
100 m in the same ground would take $0.707 \times (100/150)^{2} = 0.314$ ms — the
quadratic dependence on depth, once more.

---

## ★★4 — Apparent conductivity and its noise

$$\sigma_a = \frac{\pi t\,g^{2}}{\mu_0}
= \frac{\pi (3 \times 10^{-4})(0.012)^{2}}{1.2566 \times 10^{-6}}
= \frac{9.4248 \times 10^{-4} \times 1.44 \times 10^{-4}}
{1.2566 \times 10^{-6}}
= \frac{1.3572 \times 10^{-7}}{1.2566 \times 10^{-6}}
= 0.1080\ \mathrm{S\,m^{-1}},$$

$$\rho_a = \frac{1}{\sigma_a} = 9.26\ \Omega\,\mathrm{m}.$$

**Noise.** Because $\sigma_a \propto g^{2}$,
$$\frac{\delta\sigma_a}{\sigma_a} = 2\frac{\delta g}{g}
= 2(0.04) = 0.08 = 8\%.$$

The rule: **relative errors double under the square**, so a conductivity target
stated to 10% requires amplitude data good to 5%. This is why TDEM surveys average
so heavily in the late-time window, where the signal is faintest: that is exactly
where the depth information lives.

---

## ★★5 — Aquifer conductance versus cover conductance

**Aquifer conductance:**
$$S_{\text{aq}} = \frac{b}{\rho} = \frac{10}{5} = 2.0\ \mathrm{S}.$$

**Cover conductance:**
$$S_{\text{cover}} = \frac{50}{50} = 1.0\ \mathrm{S}.$$

**Diffusion time to the top of the aquifer**, computed in the cover's resistivity
(the diffusion has to traverse the cover first):
$$t = \frac{\mu_0 z^{2}}{2\rho} = \frac{(1.2566 \times 10^{-6})(60)^{2}}{2(50)}
= \frac{4.5239 \times 10^{-3}}{100} = 4.524 \times 10^{-5}\ \mathrm{s}
= \mathbf{0.0452\ ms}.$$

**Is the aquifer a distinctive anomaly?** Its conductance is twice the cover's, so
it doubles the column's total conductance — a factor-of-two change in a quantity the
data measure well, unlike the marginal case in
[14-02-01 ★★★7](01-ert-for-hydrology-solutions.md) where the two were equal. **So
the aquifer is detectable in principle**, provided the cover conductance is known
to better than a factor of two (which a well-spread multi-time sounding provides,
since the early times constrain the cover before the aquifer's influence arrives).
The time window needed starts at about 0.045 ms and must extend well beyond it: by
the square-root law, sampling to twice the aquifer's depth (120 m) needs
$4.524 \times 4 = 0.181$ ms, so a window of 0.05–0.5 ms covers the target and
gives the inversion something to work with on both sides of it.

---

## ★★6 — Three indistinguishable models, and where equivalence fails

Fixed conductance $S = 0.25$ S, so $\rho = b/0.25 = 4b$:

| $b$ (m) | $\rho$ ($\Omega$ m) |
|---|---|
| 2.5 | 10 |
| 5.0 | 20 |
| 10.0 | 40 |

All three satisfy $S = b/\rho = 0.25$ S, and in the thin-sheet limit they produce
the same TDEM response (the lesson measured deviations of 0%, 1.2%, 3.8%, 9.9% and
25.9% for $b$ from 2 to 32 m against a diffusion depth of 70.7 m — i.e. deviations
below 1–2% while $b \lesssim 0.05$–$0.1\,z_{\text{diff}}$).

**Where it fails.** With a diffusion depth of 150 m at the latest usable time,
equivalence should begin to fail when $b$ approaches something like
$0.1\,z_{\text{diff}} = 15$ m, and be clearly broken by
$b \sim 0.5\,z_{\text{diff}} = 75$ m. Within the table above, $b = 10$ m against
$z = 150$ m is $b/z = 0.067$ — comfortably in the equivalent regime, so **the three
models would be indistinguishable**, and a report claiming "10 m of
$40\ \Omega$ m" rather than "0.25 S of conductance" would be over-claiming.

**How to break the equivalence.** Borehole control (a log through the layer measures
$b$ directly and hence $\rho = b/S$), or a target whose thickness is comparable to
the diffusion depth so that the intermediate-time data carry shape information
rather than just amplitude.

---

## ★★★7 — Survey design for a 15 m aquifer at 60 m

**Target.** $20\ \Omega$ m, $b = 15$ m, top at 60 m, under $150\ \Omega$ m of cover,
$\sigma_{\text{cover}} = 1/150 = 6.667 \times 10^{-3}\ \mathrm{S\,m^{-1}}$.

**Step 1 — time window.** The diffusion must traverse the cover to the target and
then the target:

$$t_{\text{start}} \approx \frac{\mu_0 (60)^{2}}{2(150)}
= \frac{1.2566 \times 10^{-6} \times 3600}{300} = 1.508 \times 10^{-5}\ \mathrm{s}
= 0.0151\ \mathrm{ms}.$$

To see through the target (to 75 m) and beyond, in the *target's* resistivity:
$$t_{\text{through}} \approx \frac{\mu_0 (75)^{2}}{2(20)}
= \frac{1.2566 \times 10^{-6} \times 5625}{40} = 1.767 \times 10^{-4}\ \mathrm{s}
= 0.177\ \mathrm{ms}.$$

A practical window is therefore roughly **0.02 ms to 5 ms** (about 2.5 decades),
which brackets the target with usable data on both sides. The factor between the
earliest useful time and the target's arrival time is small, so the cover's
resistivity is constrained by only a few early channels: **the cover is the weak
link, and a co-located 1-D sounding with a smaller loop, or a shallow ERT line,
would strengthen it.**

**Step 2 — transmitter moment.** The measurable signal scales with the transmitter
moment $M = N I A$ (turns × current × area). The noise floor $V_n$ and the
half-space response imply, for the late-time 3-D regime, a signal proportional to
$M$ and a sensitivity to $\rho$ through $\rho^{-3/2}$; the practical scaling is that
**increasing $M$ by a factor of 10 extends the usable window by roughly a factor of
$(10)^{2/5} = 2.5$** for a fixed signal-to-noise ratio (from $V \propto M\rho^{-3/2}t^{-5/2}$,
setting $V = V_n$ gives $t \propto (M/\rho^{3/2})^{2/5}$). For a 60–75 m target this
is comfortable with a modest $100\ \mathrm{m} \times 100\ \mathrm{m}$ loop in a
30 $\Omega$ m ground; the number is given as a *scaling*, and the absolute design
must use the instrument's own specification.

**Step 3 — noise requirement from the factor of two.** To state the aquifer's
conductance to 10%, the amplitude data must be good to 5% (Section 4.1). The
aquifer's conductance is $S = 15/20 = 0.75$ S against a cover conductance of
$60/150 = 0.40$ S, so the aquifer contributes 65% of the column's conductance and
a 10% error on the aquifer's conductance is an error of
$0.075/(0.75+0.40) = 6.5\%$ in the total — comfortably above a 2–3% achievable
late-time repeatability. So the design closes, with margin.

**Step 4 — what to report.** The data determine the aquifer's **conductance**.
Given $b = 15$ m fixed by borehole control, $\rho = b/S = 20\ \Omega$ m to the
accuracy of $S$ (10%), i.e. $20 \pm 2\ \Omega$ m. **Without borehole control the
deliverable is a conductance and an admitted family**: for example $S = 0.75$ S,
with $(b, \rho) = (10, 13.3)$, $(15, 20)$, $(25, 33.3)$ all consistent — a range of
thicknesses from 10 to 25 m and resistivities from 13 to 33 $\Omega$ m that the
sounding cannot separate. Reporting "15 m of $20\ \Omega$ m" without that caveat is
the most common over-claim in TDEM hydrogeophysics, and the lesson's measured
equivalence table (deviations up to 26% at constant conductance) is the quantitative
justification for the caveat.

---

## ★★★8 — Verification and validation plan

**1. Analytic check — the half-space step-off.** The solution of
$\partial_t B = D\partial_z^{2}B$ with $B(z,0) = B_0$, $B(0,t) = 0$,
$B(\infty,t) = B_0$ is $B = B_0\mathrm{erf}(z/2\sqrt{Dt})$, giving a surface
response $g = 1/\sqrt{\pi Dt}$ and hence $\sigma_a = \pi t g^{2}/\mu_0 = \sigma$
identically. The test: run the code on a uniform half-space and require
$\lvert\sigma_a/\sigma - 1\rvert < 10^{-3}$ over the usable window. **Catches:** a
wrong $\mu_0$, a boundary-condition error at the surface, a unit error in $D$.
**Misses:** everything layered.

**2. Independent-limit check — the thin sheet.** For a layer of conductance $S$
thin compared with the diffusion depth, the response must depend on $S = b/\rho$
and not on $b$ and $\rho$ separately. The test: run $(b, \rho) = (2, 10)$, $(4, 20)$,
$(8, 40)$ and require the responses to agree to within 1% while
$b \ll z_{\text{diff}}$. **Catches:** an error in how layer thickness and
conductivity are discretised onto the grid (a sub-grid layer, an incorrect
interface average). **Misses:** an error that is common to all three models, for
example a wrong transmitter waveform.

**3. Reciprocity / conservation check.** In a 1-D model, exchanging transmitter and
receiver must reproduce the same response (reciprocity), and in a multi-layer model
the total induced current integrated over depth must equal the driver's effect at
$t \to 0$. The test: verify reciprocity to $10^{-8}$, and verify that the total
early-time field equals the imposed step within the discretisation error.
**Catches:** an asymmetric or non-conservative discretisation — the failure mode
that leaves a small, systematic, physically impossible drift in long time series.
**Misses:** a wrong layer model that happens to be conservative.

**4. Convergence with an observed order.** Refine $\Delta z \to \Delta z/2$ while
refining $\Delta t$ proportionally to $\Delta z^{2}$ (to keep the explicit time step
in the same regime), and measure
$p = \log_2\lVert E(\Delta z)\rVert/\lVert E(\Delta z/2)\rVert$ against the
analytic or a fine-grid reference. For a second-order-in-space, first-order-in-time
scheme, expect $p \to 1$ if $\Delta t$ dominates and $p \to 2$ if $\Delta z$ does;
report the exponent **and** the refinement rule, or the number is not reproducible.
**Catches:** an implementation error whose leading truncation term is wrong (for
example an off-centre stencil that is formally first-order). **Misses:** a
consistent-but-wrong model, since it compares the code with itself.

**5. Validation against field data.** Verification answers "am I solving the
equation right?"; validation answers "is this the right equation, with the right
parameters, for this ground?" The validation step is to invert a real sounding with
a known borehole log beside it and ask whether the observed data are reproduced
**within their stated uncertainty**, including the systematic parts: the
transmitter waveform's finite switch-off (which the idealised step ignores), the
loop geometry, the instrument's bandwidth, and 3-D effects. **Catches:** a
mis-specified source waveform, an incorrect system gain, an over-simplified 1-D
assumption. If the residuals are structured, the model — not the code — is wrong,
which is why the two tests must be reported separately.

**What none of them can establish.** That the inverted model is *the* subsurface
model. Conductance equivalence (Section 5) is physical non-uniqueness, not a code
defect: no amount of verification will separate $b$ from $\rho$ for a thin layer
without an independent measurement. The honest deliverable is the admitted family.
