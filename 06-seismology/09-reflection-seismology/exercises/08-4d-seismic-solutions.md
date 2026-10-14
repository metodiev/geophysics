# Solutions — 06-09-08 Time-Lapse (4-D) Seismic and Reservoir Monitoring

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [08 4-D Seismic](../08-4d-seismic.md).

---

## ★1 — NRMS

$$\text{NRMS} = \frac{\text{rms}(\text{monitor}-\text{baseline})}
{\tfrac12\left[\text{rms}(\text{monitor})+\text{rms}(\text{baseline})\right]}
= \frac{0.05}{0.40} = 0.125 = 12.5\%.$$

The symmetric denominator is used because it is the only normalisation that is
invariant to the order in which the two surveys are named.

---

## ★2 — The 3-sigma difference floor

For independent noise of rms $\sigma$ in each survey, the difference has rms
$\sigma_{\text{diff}} = \sqrt{2}\,\sigma$, so the 3-sigma floor is
$3\sqrt{2}\sigma$:

$$\sigma = 0.001:\quad 3\sqrt{2}\times0.001 = 4.243\times10^{-3}
\quad\text{(printed } 0.00424\text{)},$$
$$\sigma = 0.010:\quad 3\sqrt{2}\times0.010 = 4.243\times10^{-2}
\quad\text{(printed } 0.04243\text{)}. \quad\checkmark$$

$$\frac{\text{difference noise}}{\text{individual-survey noise}} = \sqrt{2}
= 1.4142 .$$

The factor is larger than one, which is the quantitative statement that a 4-D
survey is *harder* than a single survey: the difference of two noisy images has
more noise than either.

---

## ★3 — Interface times and the direction of the change

The top reservoir interface is at a two-way time
$t = 0.5385\ \mathrm{s}$ in the baseline, which for
$v = 3000\ \mathrm{m\,s^{-1}}$ implies a depth

$$h = \frac{v t}{2} = \frac{3000\times0.5385}{2} = 807.75\ \mathrm{m}.$$

With the monitor's faster reservoir velocity ($3180\ \mathrm{m\,s^{-1}}$,
$+6.0\%$), the same depth is reached in

$$t' = \frac{2h}{v'} = \frac{2\times807.75}{3180} = 0.50802\ \mathrm{s},$$

i.e. $30.5\ \mathrm{ms}$ **earlier** than the baseline. (Note: this simplified
conversion assumes the whole overburden changes, which is not what the
demonstration models — the demonstration changes only the reservoir and reports
the reflection coefficients at the reservoir interfaces. The arithmetic here is
the correct statement for a *single-layer* velocity change and is the standard
back-of-envelope.)

**Check of the reflection coefficients.** The top interface has
$R = +0.0386$ in the baseline becoming $+0.0676$ in the monitor; the base
$R = +0.1356 \to +0.1069$. A harder floor (higher velocity at constant density)
increases the contrast above the reservoir and *reduces* it below it — the
**opposite signs** of the two changes are a diagnostic that the change is
internal to the reservoir, not a global velocity shift.

---

## ★4 — Deriving the $\sqrt{2}$

Let the difference be $d = m - b$ with $m$ and $b$ the monitor and baseline
traces. For zero-mean noise,

$$\sigma_d^{2} = \mathbb{E}[(m-b)^{2}] = \mathbb{E}[m^{2}] - 2\mathbb{E}[mb]
+ \mathbb{E}[b^{2}] = \sigma_m^{2} + \sigma_b^{2} - 2\,\mathrm{Cov}(m,b).$$

**Assumption:** the noise is *uncorrelated* between surveys,
$\mathrm{Cov}(m,b)=0$, and has equal variance $\sigma_m = \sigma_b = \sigma$:

$$\sigma_d = \sqrt{2}\,\sigma .$$

**If the noise is correlated** (a repeatable acquisition signature — the same
source, receiver, statics and coupling artefacts), write
$\rho = \mathrm{Cov}(m,b)/\sigma^{2}$. Then

$$\sigma_d = \sigma\sqrt{2(1-\rho)} .$$

At $\rho = 0$ this is $\sqrt{2}\sigma$; at $\rho = 1$ (identical noise, which
cancels) it is **zero**; at $\rho = 0.5$ it is $\sigma$. This formula is the
theoretical basis of the entire repeatability-engineering industry: the way to
lower the difference noise is not to lower $\sigma$ but to **raise $\rho$** —
repeating the source and receiver positions, the acquisition timing, the
processing sequence.

---

## ★5 — Is the survey feasible?

$$\text{threshold} = 3\sigma_{\text{diff}} = 3\sqrt{2}\times0.015
= 0.063640, \qquad \text{signal} = 0.060 .$$

$$\text{margin} = \frac{0.060}{0.063640} = 0.943 < 1 .$$

**Not feasible at $3\sigma$**. The 4-D signal is $6\%$ short of the detection
threshold, i.e. it would be detected at about $2.8\sigma$ — a marginal result that
would be reported as "possible" and that a small improvement in repeatability
($\rho$ raised from $0$ to $0.1$ lowers the floor by
$\sqrt{(1-0.1)} = 0.95$, i.e. $5\%$) would convert to a detection. The quantitative
statement of infeasibility is the ratio $0.943$, not the word "marginal".

---

## ★6 — The inside/outside ratio

$$\frac{0.02543}{0.00422} = 6.02 .$$

**What it measures.** The *spatial localisation* of the difference: how much
larger the difference is where we expect the change than where we do not.

**For a purely random difference** the noise is spread evenly, so the localisation
ratio would be $1.0$ — the measured $6.02$ says that most of the difference
energy is concentrated at the reservoir.

**Why the pattern and not the amplitude.** An amplitude threshold can always be
met by noise in a large survey (with many samples, some window will exceed any
fixed threshold); a *spatially coherent, correctly located, geologically
plausible* difference cannot be produced by random noise with that probability.
This is exactly the same logic as the detection-versus-resolution distinction in
lesson 07: an amplitude says "something is here", a pattern says "*the* something
is here".

**Caveat.** NRMS computed in a window where the seismic amplitude is near zero
divides by a tiny denominator and becomes meaningless; the difference rms (or
NRMS with a stated reference amplitude) is the defensible metric.

---

## ★7 — 4-D QC plan (specification)

| metric | window | decision it supports | halt threshold |
|---|---|---|---|
| NRMS (or difference rms with a stated reference) | whole survey, far from the reservoir | acquisition repeatability | NRMS outside the reservoir above the pre-survey feasibility estimate |
| Localisation ratio (inside/outside difference rms) | reservoir window versus a control window | whether the difference is a 4-D signal or noise | ratio below the feasibility target (the demonstration measures $6.02$ for a genuine change) |
| Time-shift map between surveys (cross-correlation per trace) | whole survey | positioning and statics repeatability | coherent shifts exceeding the reservoir's expected $\delta t$ |
| Amplitude-versus-offset difference | near-to-mid angles over the reservoir | whether the change is fluid (amplitude) or pressure (time) | absence of the predicted angular signature |
| 3-sigma floor from the difference noise | whole survey | whether *any* detection is possible | expected signal below the floor (the ★5 test) |
| Well-log or pressure data at a monitor well | reservoir | independent calibration of the expected signal | mismatch between predicted and observed 4-D amplitude |

**Two required properties of the list.** At least one metric must test
*repeatability* (NRMS, time shifts) and one must test *spatial plausibility*
(localisation, AVO signature); and each metric must be computable before the
interpretation begins, so that a halt decision does not require the answer it is
meant to validate.

---

## ★8 — Separating a velocity change from a density change (specification)

**The degeneracy.** At a single incidence angle the 4-D amplitude is one number
determined by a combination of $\Delta v_p$, $\Delta v_s$ and $\Delta\rho$. By
the same argument as lesson 05, one number cannot fix three changes.

**The measurement that separates them.** The **angular dependence** of the 4-D
difference (4-D AVO): a saturation change (fluid substitution) alters
$v_p$, $v_s$ and $\rho$ together and produces a characteristic *gradient* change,
whereas a pressure change alters mainly $v_p$ through the frame stiffness. So
compute the difference amplitude as a function of incidence angle and fit the
same two-term (or three-term) expansion to the *difference*, not to the monitor
alone.

**Independent constraint.** Where available, time shifts between surveys add a
second, physically different observable: a pressure change alters the velocity
and hence the *travel time* (a time shift), while a fluid substitution alters the
*reflectivity* (an amplitude change). Combining the time-shift map with the
amplitude-versus-angle map breaks the degeneracy for the two most common
reservoir changes.

**What it costs.** (i) Far-angle data, which means a longer cable or a different
geometry (lesson 05 ★8 computes $4.7\ \mathrm{km}$ versus $2.0\ \mathrm{km}$ for
a $2.0\ \mathrm{s}$, $2800\ \mathrm{m\,s^{-1}}$ target); (ii) a repeatable
acquisition at those angles, which is harder than at near angles (the
illumination pattern at far offset is more sensitive to the source and the
overburden); and (iii) a rock-physics model to convert the fitted coefficients
into saturation and pressure changes — which is itself an assumption that must be
stated.
