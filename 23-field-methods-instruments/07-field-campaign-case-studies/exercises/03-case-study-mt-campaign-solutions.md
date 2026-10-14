# Solutions — 23-07-03 Case Study: A Magnetotelluric Campaign

The lesson is [03 Case Study: A Magnetotelluric Campaign](../03-case-study-mt-campaign.md). All
values are **SYNTHETIC**.

## ★1

$$\delta = 503.3\sqrt{\frac{\rho}{f}} = 5000
\;\Rightarrow\; f = \rho\left(\frac{503.3}{5000}\right)^{2} = \rho \times 0.010132 ,$$

| $\rho$ | $f$ | $T$ |
|---|---|---|
| 50 Ω·m | 0.5066 Hz | 1.974 s |
| 500 Ω·m | 5.0662 Hz | 0.1974 s |

So the *same depth* requires a period **ten times shorter** in the more resistive rock, and the
band must be set from the range of resistivities the survey might encounter: a band designed for
50 Ω·m only would be useless if the cover turns out to be 500 Ω·m, and the cost of extending the
band to shorter periods is small (short periods are cheap to record — the time per estimate is
the period), while extending it to *longer* periods is the expensive direction.

## ★2

$$N = \frac{1-\gamma^{2}}{2\sigma_Z^{2}\gamma^{2}}
= \frac{0.05}{2(0.02)^{2}(0.95)} = \frac{0.05}{7.6\times10^{-4}} = 65.8
\;\Rightarrow\; 66 \text{ estimates},$$

$$\text{time} = 66 \times 20\ \mathrm{s} = 1320\ \mathrm{s} = 22.0\ \mathrm{min} .$$

Note the quadratic sensitivity to the accuracy target: halving the required error from 2 % to
1 % multiplies the count by four, and the *time per estimate* grows linearly with the period, so
the deep bands are where accuracy is expensive in both dimensions. This is why accuracy targets
are stated per band.

## ★3

$$N_{0.85} = \frac{0.15}{2(0.01)^{2}(0.85)} = \frac{0.15}{1.7\times10^{-4}} = 882.4,$$

$$N_{0.97} = \frac{0.03}{2(0.01)^{2}(0.97)} = \frac{0.03}{1.94\times10^{-4}} = 154.6,$$

$$\text{time ratio} = \frac{882.4}{154.6} = \mathbf{5.71} .$$

So the remote reference buys a factor of **5.71** in the required recording time at the
long-period end — where the local coherence is worst. The gain is therefore largest exactly
where the campaign's cost lies: long periods take the longest to record (the time per estimate
is the period), so the coherence improvement at the long periods has the biggest payoff and the
improvement at the short periods almost none.

## ★4

$$\text{site-days} = 20 \times 4.0 = 80, \qquad
\text{calendar days (2 crews)} = \frac{80}{2} = 40.0,$$

$$\text{with 10 % contingency} = 44.0\ \text{days}, \qquad
\text{crew-days} = 80 \text{ crew-days of recording} .$$

Adding a remote reference site running for the whole campaign adds 44 crew-days of *supervision*
(or a separate autonomous reference station that needs only visits), and it does **not** add
site-days of the same kind: the reference runs unattended (no operator, no magnetic disturbance
from a camp) while the crews move between sites. The correct arithmetic is therefore per *site
type*:

| Site type | Days | Crew on site | Site-days | Crew-days |
|---|---|---|---|---|
| sounding site | 4.0 each × 20 | yes | 80 | 80 |
| remote reference | 44 (whole campaign) | visits only | 44 | ~6 (visits) |

Reporting a single "site-days" figure hides this distinction, and it is the distinction that
decides whether the reference is affordable: the reference costs **one extra station and a
handful of visits**, and buys back 5.71× the recording time at the sites that matter.

## ★5

$$\text{rate} = 4 \times 250 \times 4 = 4000\ \mathrm{B/s} = 4.0\ \mathrm{kB/s},$$

$$\text{per site} = 4000 \times 86\,400 \times 4 = 1.3824\times10^{9}\ \mathrm{B}
= 1.3824\ \mathrm{GB},$$

$$\text{campaign} = 20 \times 1.3824 = 27.65\ \mathrm{GB} .$$

So 27.65 GB — a few hours of a modern disk. The scarce resource is **recording time**: the
campaign is 80 site-days, i.e. 40 calendar days with two crews, and every day of recording is a
crew day. The archive can be bought, the crew time cannot, and the recording time is fixed by
the coherence of the sites and the accuracy requirement. The design consequence is the same as
in the two previous case studies: **the physics (coherence, band) sets the schedule, and the
schedule sets the budget.**

## ★6

A model answer.

**Band, cover and target.** The 200 m conductive cover must be *seen* (to bound its effect) and
the 1 km conductor resolved below it. For a synthetic cover of 5 Ω·m:

$$\delta = 200\ \mathrm{m} \Rightarrow f = 5\left(\frac{503.3}{200}\right)^{2}
= 31.7\ \mathrm{Hz}, \quad T = 0.032\ \mathrm{s},$$

and for the target at 1 km in, say, 50 Ω·m:

$$\delta = 1000\ \mathrm{m} \Rightarrow f = 50\left(\frac{503.3}{1000}\right)^{2}
= 12.7\ \mathrm{Hz}, \quad T = 0.079\ \mathrm{s},$$

so the *target band is 0.03–1 s* (about 1.5 decades) — and because the cover is conductive, the
same physical depth needs periods that must be computed **with the cover's resistivity**, which
is the first reason to model the cover rather than guess it. Add 0.001–0.01 s for the cover and
1–100 s for the regional structure, and the full band is 0.001–100 s (5 decades). The **dead
band** (1–5 s typically) falls in the middle of the regional part, not in the target band, so it
degrades the regional placement rather than the target — a favourable geometry that should be
stated.

**Recording time per site.** With $\gamma^{2} = 0.85$ at long periods and a 5 % accuracy target:

$$N = \frac{1-\gamma^{2}}{2\sigma_Z^{2}\gamma^{2}} = \frac{0.15}{2(0.05)^{2}(0.85)}
= \frac{0.15}{0.00425} = 35.3 \text{ estimates per long period},$$

so at $T = 100$ s the long-period data need about $35 \times 100$ s = 58 min of *coherent*
data — but the same period must be estimated in several bands, and the coherence is worse at the
longest periods, so a realistic per-site duration is 3–5 days. With a remote reference
($\gamma^{2} \rightarrow 0.97$) the count falls to
$0.03/(2 \times 0.0025 \times 0.97) = 6.2$ estimates, a factor 5.7 less time: **the remote
reference changes a 5-day site into a 1-day site at the long periods and is therefore the
single most valuable element of this plan.**

**Site ranking.** Before any long deployment, a **short broadband noise survey** (30–60 min per
candidate site, at the target periods) recording all five components, ranked by the coherence
at the long periods and the absence of a single coherent source. Cost: half a day per site; value:
the difference between 1 and 5 days of recording per site. Also verify the *independence* of the
remote reference's noise by comparing the two sites' coherent noise at the deployment epochs.

**Crew and calendar.** 25 sites at a realistic 2 days each with the reference (because the
reference cuts the long-period time): 50 site-days → 25 calendar days with two crews, plus 20 %
contingency → **30 days**, plus 3–4 days of reconnaissance and mobilisation and 3 days of
demobilisation: about 5–6 weeks.

**Model parameterisation.** The band (0.001–100 s, 5 decades) supports about 10 independent
layers at half a decade each — but the target band is only 1.5 decades, so the *target* is
constrained by about 3 layers. The parameterisation should therefore be a coarse layered model
(nominally 10–15 layers, with a fixed shallow layer for the known 200 m cover) or a
smoothness-regularised 2-D section; a 40-layer 3-D model is not supportable.

**Resolution claim and its test.** The defensible claim is "a conductive body with a resistivity
contrast of at least 3× its host can be located within ±200 m vertically at 1 km depth". The test
that supports it: build a synthetic model of the cover and the target with the *actual* site
geometry, forward-model it, add noise consistent with the achieved coherence, invert with the
same mesh and regularisation, and report the recovered contrast and the depth misfit. That
synthetic test — not the field picture — is the resolution claim, and it should also be run for
the *absence* case (no target) to state the detection threshold.

**What the campaign cannot establish.**

1. **The absolute resistivity of a thin target under a conductive cover**: the cover dominates
   the response and suppresses the sensitivity to the target's value; the campaign can bound the
   conductor's depth and conductance but not its resistivity, because the inductive response of a
   thin sheet depends on the product of conductivity and thickness.
2. **Anisotropy or 3-D structure at the scale of the target**: with a 25-site grid and a 1.5-decade
   target band, the tensor's off-diagonal structure is resolved coarsely at best; a 3-D
   interpretation would be a modelling choice presented as a result, and the honest report says
   the data support a 2-D or 1-D-with-cover interpretation.
