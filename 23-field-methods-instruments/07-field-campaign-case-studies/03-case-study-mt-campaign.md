---
id: 23-07-03
title: "Case Study: A Magnetotelluric Campaign"
level: research
prereqs: ["23-04-03", "23-07-02", "08-04-02"]
estimated_minutes: 115
tags: [case-study, magnetotellurics, coherence, remote-reference, campaign-planning]
---

# Case Study: A Magnetotelluric Campaign

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the period band a target depth requires, for a range of resistivities.
2. **Compute** the number of independent period estimates a stated impedance accuracy needs
   from the coherence, and the recording time that implies.
3. **Compute** what a remote reference buys, and **state** where the gain is largest.
4. **Plan** a multi-site campaign: site-days, crews, calendar and the contingency factor.
5. **Compute** the data volume and **state** which resource is scarce.
6. **Estimate** the depth resolution a period band supports, and **state** what the dead band
   removes.
7. **Write** the campaign plan so that its resolution claim is checkable.

All numbers here are **SYNTHETIC** teaching values combined with the standard relations quoted
in the text (skin depth, the coherence-to-accuracy relation for an impedance estimate, the
half-decade-per-layer resolution rule, data-rate arithmetic). No real campaign, instrument,
vendor figure or measured dataset is reproduced.

## Prerequisites

- [23-04-03 MT Fieldwork: Sites, Remote Reference and Noise](../04-electrical-em-fieldwork/03-mt-fieldwork.md) —
  the field procedure and the coherence arithmetic this case study scales up.
- [23-07-02 Case Study: An ERT Survey from Design to Report](02-case-study-ert-survey.md) —
  the same design sequence for a survey whose cost is field time.
- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the transfer functions the campaign estimates.

## 1. The requirement

A synthetic campaign must **resolve a conductive body at about 2 km depth** and place it in a
regional resistivity structure, over a 30-site grid. The requirement contains one number that
drives the whole campaign — the depth — and one that drives its *cost* — the accuracy of the
impedance estimate, because accuracy is bought with recording time.

## 2. The period band from the target depth

The skin depth,

$$\delta = 503.3\sqrt{\frac{\rho}{f}} \quad [\mathrm{m},\ \Omega\cdot\mathrm{m},\ \mathrm{Hz}],$$

must be comparable to the target depth for the target to be sensed:

| $\rho$ | Frequency for $\delta = 2$ km | Period |
|---|---|---|
| 1 Ω·m | 0.0633 Hz | 15.791 s |
| **10 Ω·m** | **0.6333 Hz** | **1.579 s** |
| 100 Ω·m | 6.3328 Hz | 0.158 s |
| 1000 Ω·m | 63.3277 Hz | 0.016 s |

so a 10 Ω·m target at 2 km needs periods longer than about **1.58 s**, and the *same depth* in
a 100 Ω·m rock needs a period ten times shorter. The band must therefore be set from the
resistivity the survey expects — and since that is what the survey is trying to measure, the
band is chosen generously:

| Period | $\delta$ at 10 Ω·m | $\delta$ at 100 Ω·m |
|---|---|---|
| 0.001 s | 50.3 m | 159.2 m |
| 0.01 s | 159.2 m | 503.3 m |
| 0.1 s | 503.3 m | 1591.6 m |
| 1 s | 1591.6 m | 5033.0 m |
| 10 s | 5033.0 m | 15 915.7 m |
| 100 s | 15 915.7 m | 50 330.0 m |
| 1000 s | 50 330.0 m | 159 157.4 m |

A band from 0.001 s to 100 s spans 5 decades and covers depths from about 50 m to 50 km in the
conductive case: enough to see the target and to place it in a regional structure, and the
reason the campaign cannot save time by shortening the band at the *long* end — the regional
structure is what makes the target interpretable.

## 3. Recording time: the coherence decides

For a single-station estimate from $N$ independent period estimates with coherence
$\gamma^{2}$, the relative error of the impedance is approximately

$$\sigma_Z \approx \sqrt{\frac{1-\gamma^{2}}{2N\gamma^{2}}} ,$$

so the number of estimates a 1 % accuracy needs is

$$N = \frac{1-\gamma^{2}}{2\sigma_Z^{2}\gamma^{2}} :$$

| $\gamma^{2}$ | $N$ for 1 % | $N$ for 5 % | Time at $T = 10$ s (1 %) |
|---|---|---|---|
| 0.500 | 5000.0 | 200.0 | 833.3 min |
| 0.800 | 1250.0 | 50.0 | 208.3 min |
| 0.900 | 555.6 | 22.2 | 92.6 min |
| 0.950 | 263.2 | 10.5 | 43.9 min |
| 0.990 | 50.5 | 2.0 | 8.4 min |
| 0.998 | 10.0 | 0.4 | 1.7 min |

The table is the campaign's cost model. **A coherence of 0.99 rather than 0.90 is a factor of
10.5 in the recording time**, and the coherence is a property of the *site* — its cultural
noise, its power lines, its wind — far more than of the instrument. The consequences:

1. **Site selection is the largest cost lever in the campaign.** An hour spent finding a quiet
   site can save a day of recording, and the ranking of candidate sites should be done with a
   short broadband noise recording before any long deployment.
2. **Accuracy requirements should be stated per period band**, not globally: the long periods
   (deep, regional structure) usually tolerate a larger error than the target band, and the
   cost of accuracy falls steeply with period (because the time per estimate is the period).
3. **The estimate count is a floor, not a target.** It assumes independent, unbiased
   estimates; correlated noise (a coherent source across the whole band) does not average
   down, and no amount of recording removes it — which is what the next section addresses.

## 4. The remote reference

A remote reference correlates the local magnetic field with a distant station's, removing the
part of the noise that is *coherent at both sites*:

| Local $\gamma^{2}$ | Remote $\gamma^{2}$ | $N$ local | $N$ remote | Time ratio |
|---|---|---|---|---|
| 0.900 | 0.980 | 555.6 | 102.0 | 5.44 |
| 0.800 | 0.950 | 1250.0 | 263.2 | 4.75 |
| 0.990 | 0.998 | 50.5 | 10.0 | 5.04 |

So a remote reference buys a factor of about **5** in the required recording time — and the
gain is largest exactly where the local data are worst, which is the property that makes it
worth the extra station, the extra crew and the extra analysis. Two practical rules:

1. **The remote site must be far enough to be independent and close enough to share the
   source.** If the two sites share the *signal* (the same regional MT field), the remote
   reference estimates it; if they share only *noise* (a common power grid), the reference
   does nothing. Choosing the distance is a design decision with a physical argument.
2. **The remote reference is a permanent asset.** One reference site serving a rotating
   campaign of 30 sites costs one station-day of deployment per site-visit cycle, and the
   arithmetic above says it saves four.

## 5. Campaign arithmetic

With 3.0 days of recording per site (a synthetic figure that already accounts for the
coherence-required periods, the dead band and the reference), 30 sites is 90 site-days:

| Crews | Site-days | Calendar days | With 20 % contingency |
|---|---|---|---|
| 1 | 90 | 90.0 | 108.0 |
| 2 | 90 | 45.0 | 54.0 |
| 3 | 90 | 30.0 | 36.0 |

and the data volume is modest: five channels at 500 Hz and four bytes is 10.0 kB/s, so **2.59 GB
per site** and **77.8 GB for the campaign**. Three points that decide the plan:

1. **The schedule, not the archive, is the scarce resource.** The campaign is 90 site-days of
   *recording*, and the crew count only changes the calendar — the labour is constant, as in
   the array case study.
2. **The 20 % contingency is not padding.** Access, weather, equipment failures and a
   re-deployment at one site are the norm; a plan without contingency is a plan that ends
   early with an incomplete grid.
3. **Site-days and crew-days differ.** A remote reference site and a site with a long
   deployment have a different cost from a quick broadband site, so the plan should be a table
   of site *types*, not an average.

## 6. Depth resolution and the dead band

The standard rule of thumb is **one independent depth layer per half-decade of period**, so a
5-decade band (0.001 s to 100 s) supports about 10 layers:

| Band | Decades | Layers at 0.5 dec |
|---|---|---|
| 0.001–1 s | 3.00 | 6 |
| 0.001–100 s | 5.00 | 10 |
| 0.01–1000 s | 5.00 | 10 |
| 0.1–1000 s | 4.00 | 8 |

The rule's consequence is that **the model's layer count is set by the band, not by the mesh**:
a 30-layer inversion of a 5-decade dataset claims structure the data cannot constrain, exactly
as in the ERT case study. The second consequence is the **dead band**: in the 1–5 s range (the
ambiguous band between the audio-magnetotelluric and magnetotelluric ranges) the coherence
collapses in most environments — the synthetic coherence has a minimum of 0.9302 at 1.701 s,
against more than 0.9848 elsewhere — so the layers that the dead band covers are the
worst-resolved of the model, and the report must say so rather than present them as structure.

## 7. From data to report

The report's sections, and the design question each answers:

1. **Requirement and band** (§1–§2): the target, the resistivity range and the periods
   required.
2. **Sites and their quality** (§3): the coherence at each site per band, the required
   estimate count, and the noise survey that ranked the sites.
3. **Reference strategy** (§4): the remote site, its distance, the coherence improvement
   measured, and the time it saved.
4. **Schedule and logistics** (§5): site types, crew-days, contingency and the data volume.
5. **Processing and inversion** (§6): the band used, the dead band excluded or downweighted,
   the model's layer count justified by the band, and the resolution claim per depth.
6. **Interpretation**, with the regional structure and the target body stated separately,
   because they are constrained by different parts of the band.

## 8. Assumptions and regime of validity

1. **The impedance estimator's error relation applies.** It assumes independent, unbiased
   estimates and a single coherent noise source; robust processing changes the constants, not
   the shape of the trade-off.
2. **The skin depth assumes a uniform half-space.** Layering, anisotropy and a conductive
   overburden change the actual depth sensitivity, so the band is chosen generously.
3. **The remote reference removes *coherent* noise.** Its two requirements — independence of
   the noise, sharing of the signal — are physical claims to be argued, not assumed.
4. **The site ranking from a short survey holds.** The noise environment changes (seasonally,
   with construction, with agriculture), so a site that was quiet in the reconnaissance may
   not remain quiet.
5. **The half-decade-per-layer rule is a rule of thumb.** It is a design guide for the model's
   parameterisation, not a resolution guarantee, and the honest claim comes from a synthetic
   resolution test.
6. **The crews and the access hold through the campaign.** Permissions, landowner relations
   and seasonal access are the terms that most often destroy an MT schedule.

## 9. The honest summary

- A 10 Ω·m target at 2 km needs periods longer than 1.58 s; the same depth at 100 Ω·m needs
  0.158 s, so the band is set from the expected resistivity.
- Coherence, not the instrument, sets the recording time: $N = (1-\gamma^{2})/(2\sigma_Z^{2}
  \gamma^{2})$ is 555.6 estimates at $\gamma^{2} = 0.90$ and 50.5 at $\gamma^{2} = 0.99$ for a
  1 % impedance error — a factor of 10.5, and 92.6 min against 8.4 min at $T = 10$ s.
- A remote reference buys a factor of about 5 (5.44 in the synthetic case), most where the
  local data are worst.
- 30 sites at 3 days is 90 site-days: 90, 45 or 30 calendar days for 1, 2 or 3 crews, plus 20 %
  contingency; the data volume is only 77.8 GB.
- A 5-decade band supports about 10 layers, so a 30-layer model over-reaches; and the dead band
  (coherence 0.9302 at 1.701 s here) is where the model is worst.
- The two levers that matter are site quality and the reference: both are field decisions taken
  before the long deployments.

## 10. Python demonstration

[`code/case_study_mt_campaign_demo.py`](./code/case_study_mt_campaign_demo.py) prints every
number quoted above: the skin-depth band tables, the coherence-to-estimate-count table with
times, the remote-reference gains, the crew schedule and data volume, and the depth-resolution
table with a seeded synthetic coherence showing the dead band.

```bash
cd 23-field-methods-instruments/07-field-campaign-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_mt_campaign_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/03-case-study-mt-campaign-exercises.md`](./exercises/03-case-study-mt-campaign-exercises.md)
and
[`exercises/03-case-study-mt-campaign-solutions.md`](./exercises/03-case-study-mt-campaign-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. Compute the period for $\delta = 5$ km at 50 Ω·m, and the period for $\delta = 5$ km at
   500 Ω·m.
2. With $\gamma^{2} = 0.95$, compute $N$ for a 2 % impedance accuracy.
3. A remote reference raises $\gamma^{2}$ from 0.85 to 0.97. Compute the time ratio at a 1 %
   accuracy.
4. With 20 sites at 4 days each and 2 crews, compute the calendar days with 10 % contingency.
5. Compute the data volume for 20 sites recording 4 channels at 250 Hz and 4 bytes for 4 days.
6. For a band of 0.005–500 s, compute the number of half-decade layers.

## 13. Common pitfalls

1. **Choosing the band from the expected resistivity only.** The band must bracket the
   possible resistivity, not the hoped-for one.
2. **Treating the coherence as an instrument property.** It is a site property.
3. **Skipping the reconnaissance noise survey.** It is the cheapest part of the campaign and
   the most valuable.
4. **A remote reference too close to share nothing or too far to share the signal.** The
   distance is an argument, not a default.
5. **Planning without contingency.** The schedule is where the campaign fails.
6. **Inverting with more layers than the band supports.** The extra structure is the mesh.
7. **Presenting the dead-band layers as structure.** They are the worst-resolved part of the
   model.

## 14. Where this is used

- Crustal and lithospheric studies using MT, where the band is chosen for depth and the sites
  for noise — see
  [23-04-03 MT Fieldwork: Sites, Remote Reference and Noise](../04-electrical-em-fieldwork/03-mt-fieldwork.md).
- Geothermal and mineral exploration, where a conductor at 1–3 km is the target.
- Monitoring for fluid injection, where the time-lapse requirement adds its own coherence
  demands.
- Any campaign whose schedule is set by a physical noise floor rather than by a hardware
  specification.

## 15. Related lessons

- [02 Case Study: An ERT Survey from Design to Report](02-case-study-ert-survey.md) —
  where resolution is bought with electrode spacing and stacking.
- [01 Case Study: Deploying a Temporary Seismic Array](01-case-study-seismic-array.md) —
  where the same site-days and redundancy arithmetic applies.
- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the transfer functions and their uncertainty.
- [23-07-04 Case Study: A Marine Geophysical Cruise](04-case-study-marine-cruise.md) —
  the campaign whose geometry is set by a moving platform.

## 16. Self-assessment checklist

- [ ] I can compute the band a target depth requires.
- [ ] I can compute the estimate count from a coherence and an accuracy.
- [ ] I can compute what a remote reference buys.
- [ ] I can plan crews, site-days, calendar and contingency.
- [ ] I can compute the data volume and name the scarce resource.
- [ ] I can estimate the layer count a band supports and locate the dead band.
- [ ] I can state the resolution claim per depth.
