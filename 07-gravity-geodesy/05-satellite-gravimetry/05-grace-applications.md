---
id: 07-05-05
title: "Applications: Groundwater Depletion, Ice Loss, Sea Level"
level: doctoral
prereqs: ["07-05-01", "07-05-04", "07-04-02"]
tags: [gravity, geodesy, satellite-gravimetry, hydrology, sea-level]
---

# Applications: Groundwater Depletion, Ice Loss, Sea Level

## Learning objectives

By the end of this lesson you will be able to:

1. **Fit** a trend to a monthly equivalent-water-height record, with seasonal
   terms, and **report** a standard error rather than a bare slope.
2. **Demonstrate** the bias introduced by omitting a real seasonal term, and
   **explain** why adding spurious terms is neither rewarded nor punished by the
   fit.
3. **Derive** the scaling of trend uncertainty with record length and **state**
   what record length a target precision requires.
4. **Quantify** how a solid-Earth (GIA) correction propagates into a reported
   depletion rate, and **state** the correction with its uncertainty.
5. **Correct** a basin trend for a stated leakage fraction and **compare** the
   correction with the standard error to decide whether it matters.
6. **Convert** a mass trend into a sea-level equivalent and **explain** why a
   budget that "closes" inside its error bars has not been tested.
7. **Write** a defensible application claim that labels each number as measured,
   converted, corrected or assumed.

## Prerequisites

- [01 GRACE and GRACE-FO: Mission Concept and Data Products](01-grace-gracefo.md) —
  the coefficients, the noise and the equivalent-water-height conversion.
- [04 Mass Concentration Solutions, Leakage and Filtering](04-mascons-and-leakage.md) —
  the filter, the leakage and the region-size criterion used here.
- [07-04-02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](../04-geodesy-reference-frames/02-height-systems.md) —
  the vertical reference against which water storage and sea level are measured.

> **All models and data in this module are SYNTHETIC.** The basins, trends,
> noise, GIA signal and leakage fractions below are teaching values chosen so
> that the arithmetic can be followed. No measured mass change, real basin or
> published trend is used anywhere in this module.

## 1. What an application actually claims

A published-looking sentence such as

> "the basin lost $1.0\ \mathrm{cm\,yr^{-1}}$ of water equivalent over the last
> decade"

is a composite of at least six statements:

| Layer | Status | Example value used here |
|---|---|---|
| coefficients with covariance, degrees 2–$L$ | measured | noise $1.20\ \mathrm{cm}$ per monthly solution |
| spatial filter / mascon kernel | chosen | $\sigma = 400\ \mathrm{km}$ in [04](04-mascons-and-leakage.md) |
| conversion to water equivalent | converted, uses $k_l$ | $k_2 = -0.30$ |
| solid-Earth response removed | corrected, modelled | $+0.40\ \mathrm{cm\,yr^{-1}}$ |
| neighbour contribution removed | corrected, modelled | $0.4\%$ of $+0.50\ \mathrm{cm\,yr^{-1}}$ |
| temporal model | chosen | trend + annual + semiannual |

Every one of the last four rows is a number that a reader cannot check from the
report unless the report includes it. The purpose of this lesson is to make each
one of them *measurable in a synthetic experiment*, so that the size of the
correction can be compared with the size of the error bar.

## 2. Trend estimation, and the seasonal trap

Take a synthetic monthly record of equivalent water height,
$y(t) = a + bt + A_1\sin(2\pi t/12 + \phi_1) + A_2\sin(4\pi t/12 + \phi_2) +
\varepsilon(t)$, with $b = -1.00\ \mathrm{cm\,yr^{-1}}$, $A_1 = 2.00\
\mathrm{cm}$, $A_2 = 0.80\ \mathrm{cm}$ and
$\varepsilon \sim \mathcal{N}(0, 1.20^2\ \mathrm{cm^2})$ over ten years. Fit

$$y(t) = a + bt + \sum_{k=1}^{K}\left[c_k\cos\frac{2\pi kt}{12} +
d_k\sin\frac{2\pi kt}{12}\right]$$

by least squares and read $b$ and its standard error from the covariance matrix
$\hat\sigma^{2}(A^{\mathsf T}A)^{-1}$, where $\hat\sigma^{2}$ is the residual
variance and the dof are $N - (2 + 2K)$.

| model | trend (cm/yr) | standard error | residual rms (cm) |
|---|---|---|---|
| constant + linear | $-1.072$ | 0.063 | 1.998 |
| $+$ annual | $-1.030$ | 0.038 | 1.189 |
| $+$ annual $+$ semiannual | $-1.025$ | 0.035 | 1.109 |
| $+$ 3rd and 4th harmonics (spurious) | $-1.024$ | 0.035 | 1.090 |

Three measured facts, all of which contradict a common shorthand:

1. **Omitting a real seasonal term biases the trend.** The plain linear fit gives
   $-1.072$ against a truth of $-1.000$, a bias of $0.072\ \mathrm{cm\,yr^{-1}}$,
   larger than its own standard error of $0.063$. The bias is not random: it is
   the projection of the annual sinusoid onto the linear basis over the specific
   record length, and it changes sign with the phase $\phi_1$.
2. **Adding the real terms reduces the error, not just the bias.** The standard
   error falls from $0.063$ to $0.035$ because the residual rms falls from
   $1.998$ to $1.109\ \mathrm{cm}$, far more than the four extra degrees of
   freedom cost.
3. **Adding spurious terms changes nothing measurable.** The 3rd and 4th
   harmonics move the trend by $0.001\ \mathrm{cm\,yr^{-1}}$, leave the standard
   error unchanged and improve the residual rms from $1.109$ to $1.090\ \mathrm{cm}$.
   Parsimony is therefore a *judgement* supported by physics, not a diagnostic
   supplied by the fit.

*Worked example 1 (record length).* The standard error of a linear slope scales
as $\sigma_b = \sigma_\varepsilon/\sqrt{\sum_i(t_i-\bar t)^{2}}$. For $N$ monthly
samples over $T$ years, $\sum(t_i-\bar t)^{2} \approx N T^{2}/12$ (in years),
so

$$\sigma_b \propto \frac{\sigma_\varepsilon}{T^{3/2}} .$$

Measured in the demonstration: $2$ years give $0.563\ \mathrm{cm\,yr^{-1}}$,
$10$ years give $0.035$ — a factor $16$ for five times the record, consistent
with $5^{3/2} = 11.2$ up to the different noise realisations in the partial
records. **A trend from two or three years of monthly solutions is usually a
statement about the noise**, and the honest way to say so is to quote the error.

## 3. Corrections that exceed the signal

### 3.1 Solid-Earth response

The measured coefficient change contains the Earth's response to past ice
loading (post-glacial rebound, see
[06-04](../06-earth-tides-and-rotation/04-post-glacial-rebound.md)). In the
synthetic experiment a trend of $+0.40\ \mathrm{cm\,yr^{-1}}$ of apparent
equivalent water is added to every basin:

| quantity | value |
|---|---|
| fitted trend without correction | $-0.625\ \mathrm{cm\,yr^{-1}}$ |
| solid-Earth correction | $-0.400\ \mathrm{cm\,yr^{-1}}$ |
| corrected trend | $-1.025\ \mathrm{cm\,yr^{-1}}$ |

**The correction is $40\%$ of the answer.** A quoted depletion rate without the
correction *and its uncertainty* is therefore uninterpretable: if the correction
is uncertain by $50\%$, the answer inherits a $20\%$ systematic error, which no
amount of averaging will remove.

### 3.2 Leakage

Take the leakage measured in [04](04-mascons-and-leakage.md): the contamination
of a basin by a neighbour $1443\ \mathrm{km}$ away was $+0.121\ \mathrm{cm}$ in
$32\ \mathrm{cm}$, i.e. a fraction $0.004$. If the neighbour is gaining at
$+0.50\ \mathrm{cm\,yr^{-1}}$, the basin's apparent trend is shifted by
$0.004\times0.50 = 0.002\ \mathrm{cm\,yr^{-1}}$:

| quantity | value |
|---|---|
| trend as measured | $-1.023\ \mathrm{cm\,yr^{-1}}$ |
| leakage correction | $-0.002\ \mathrm{cm\,yr^{-1}}$ |
| trend corrected | $-1.025\ \mathrm{cm\,yr^{-1}}$ |
| bias / standard error | $0.06\sigma$ |

Here the correction is negligible *relative to the error bar*, and that is the
only defensible criterion: a bias is worth correcting when it is comparable to or
larger than the uncertainty, and worth reporting either way. The same leakage
fraction would be decisive for a basin with a small trend and a long record.

## 4. From mass to sea level

A mass change $\Delta M$ spread into the ocean of area $A_{\text{ocean}}$ raises
global mean sea level by

$$\Delta \mathrm{SL} = \frac{\Delta M}{\rho_w A_{\text{ocean}}} .$$

With $R = 6371\ \mathrm{km}$ and a stated ocean fraction $0.708$,
$A_{\text{ocean}} = 0.708\times4\pi R^{2} = 3.6113\times10^{14}\ \mathrm{m^{2}}$.

*Worked example 2.* The synthetic basin is $10^{6}\ \mathrm{km^{2}} =
10^{12}\ \mathrm{m^{2}}$. A loss of $1.00\ \mathrm{cm\,yr^{-1}}$ of water
equivalent is a mass loss of

$$\Delta M = \rho_w \times 0.010 \times 10^{12} = 1.0000\times10^{13}\
\mathrm{kg\,yr^{-1}},$$

and the sea-level equivalent is

$$\Delta \mathrm{SL} = \frac{1.0000\times10^{13}}{(1000)(3.6113\times10^{14})}
= 2.769\times10^{-5}\ \mathrm{m\,yr^{-1}} = 0.0277\ \mathrm{mm\,yr^{-1}} .$$

The demonstration tabulates $1$, $5$ and $10\ \mathrm{cm\,yr^{-1}}$ giving
$0.0277$, $0.1385$ and $0.2769\ \mathrm{mm\,yr^{-1}}$: the conversion is exactly
linear, and the whole of the uncertainty therefore resides in the mass trend, not
in the conversion.

## 5. Why a "closed" budget can be empty

Suppose the ice sheets, glaciers, groundwater and terrestrial storage trends are
each estimated to $20\%$. Their sum then has an uncertainty of about $20\%$ of
the sum of their absolute values. Comparing that sum with an independently
observed sea-level rate and finding agreement to within the combined error bars
is **not** a test of the budget: with errors of that size, agreement is expected
for a wide range of true partitions. A budget closes because the errors are
large, and saying so is the honest version of the claim.

The test that *does* have power is a **spatial** one: the pattern of mass change
predicted by a model (glacier inventory, hydrological model, GIA model) can be
compared with the observed *pattern* coefficient by coefficient, which uses
thousands of independent constraints instead of one sum. That is the difference
between the budget arithmetic of this lesson and the model-evaluation argument of
[04](04-mascons-and-leakage.md).

## 6. Assumptions and regime of validity

1. **Linear trend + deterministic seasonals.** Real records contain
   interannual variability (droughts, floods) that is neither; the trend error
   from such variability is *not* captured by the least-squares error bar, and
   must be estimated from the residual autocorrelation.
2. **Independent monthly errors.** Real solutions have correlated errors,
   especially at low degree, so the formal error bars are optimistic. All the
   numbers here use an independently drawn noise, which is the *optimistic*
   case.
3. **The basin is the region reported.** A trend is a property of a filtered
   region of a stated size, not of a place.
4. **The corrections are known.** Solid-Earth response, atmosphere, ocean and
   terrestrial water are removed with models whose errors are systematic.
5. **The mass change is surface mass.** Deep mass change is misattributed.
6. **Sea level responds uniformly.** The conversion ignores ocean circulation,
   self-attraction and loading, and the fact that the ocean basin changes shape —
   each of which is a model in its own right.

## 7. Python demonstration

`code/grace_applications_demo.py` prints, with units:

1. **A synthetic ten-year monthly record** with a trend of $-1.00\
   \mathrm{cm\,yr^{-1}}$, seasonals and $1.20\ \mathrm{cm}$ of noise, plus the
   naive end-point slope ($-1.166\ \mathrm{cm\,yr^{-1}}$) for contrast.
2. **Four temporal models**: the bias from omitting seasonals ($-1.072$ against
   $-1.000$), the error reduction from adding them ($0.063 \to 0.035\
   \mathrm{cm\,yr^{-1}}$) and the neutrality of spurious terms.
3. **Record-length scaling**: $0.563\ \mathrm{cm\,yr^{-1}}$ at two years,
   $0.035$ at ten.
4. **The solid-Earth correction**: $40\%$ of the signal.
5. **The leakage correction**: a $0.06\sigma$ effect, and the criterion for
   when it matters.
6. **Mass to sea level**: $0.0277\ \mathrm{mm\,yr^{-1}}$ per
   $\mathrm{cm\,yr^{-1}}$ over $10^{6}\ \mathrm{km^{2}}$, exactly linear.

Print-only, fixed seed, no network, exits 0.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/05-grace-applications-exercises.md`](./exercises/05-grace-applications-exercises.md)
and
[`exercises/05-grace-applications-solutions.md`](./exercises/05-grace-applications-solutions.md).

- **★** Convert a $\mathrm{cm\,yr^{-1}}$ trend over $2\times10^{5}\
  \mathrm{km^{2}}$ into a mass rate and a sea-level rate.
- **★** Explain, with the demonstration's numbers, why the plain linear fit
  returns $-1.072$ rather than $-1.000$.
- **★★** A record gives $b = -1.20 \pm 0.30\ \mathrm{cm\,yr^{-1}}$ before the
  solid-Earth correction and the correction is $+0.40 \pm 0.20\
  \mathrm{cm\,yr^{-1}}$. Report the corrected rate with its uncertainty and state
  whether the result is significant.
- **★★★** Design a study that would test a water-budget partition using the
  *spatial pattern* of mass change rather than the total, specifying the
  forward model, the observation operator and the diagnostic.

## 9. Common mistakes

1. **Quoting a trend with no error and no corrections.**
2. **Fitting only a line to a ten-year monthly record** and calling the
   difference from a nearby basin a real difference.
3. **Treating the formal least-squares error as the total uncertainty**, when
   the dominant terms are systematic (filter, Love numbers, GIA).
4. **Comparing a filtered observation with an unfiltered model.** Apply the
   same filter to both, always.
5. **Reporting a budget closure as a validation.** With $20\%$ errors on the
   terms, closure is expected.
6. **Forgetting the sign conventions** of the solid-Earth correction, which can
   be comparable to the signal and is different in different regions.

## 10. Real-world applications

- **Groundwater.** The rate of storage loss in a defined aquifer system, with
  the well records as the independent check.
- **Ice sheets and glaciers.** Mass balance from gravity, cross-checked against
  altimetry and input–output methods.
- **Sea level.** The mass component of sea-level change, separated from the
  steric (thermal) component by combining gravity with altimetry.
- **Droughts and floods.** Total water storage as a *state variable* for
  hydrological models, which is where time-variable gravity is most useful as a
  constraint rather than as an answer.

## 11. Mastery checkpoint

Do this without notes:

> A synthetic basin of $5\times10^{5}\ \mathrm{km^{2}}$ is observed for eight
> years of monthly solutions with a per-solution noise of $1.0\ \mathrm{cm}$ EWH
> and a real annual cycle of $2.0\ \mathrm{cm}$ amplitude. The fitted trend,
> with seasonals, is $-1.50 \pm 0.10\ \mathrm{cm\,yr^{-1}}$; a stated
> solid-Earth correction is $+0.30 \pm 0.15\ \mathrm{cm\,yr^{-1}}$; a neighbour
> gaining at $+0.60\ \mathrm{cm\,yr^{-1}}$ leaks into the basin with a measured
> fraction $0.004$. **(a)** Report the corrected trend with its uncertainty,
> combining the two corrections in quadrature. **(b)** Is the result significant
> at $3\sigma$? **(c)** Convert it to a mass rate and a sea-level rate.
> **(d)** State which parts of your answer are measured, converted, corrected and
> assumed. **(e)** Estimate how much longer the record would have to be to halve
> the statistical error.

*Answers.* **(a)** Corrections: solid-Earth $-0.30\ \mathrm{cm\,yr^{-1}}$,
leakage $-0.004\times0.60 = -0.0024\ \mathrm{cm\,yr^{-1}}$. Corrected trend:

$$b = -1.50 - 0.30 - 0.0024 = -1.802\ \mathrm{cm\,yr^{-1}},$$
$$\sigma_b = \sqrt{0.10^{2} + 0.15^{2} + 0^{2}} = 0.180\ \mathrm{cm\,yr^{-1}} .$$

**(b)** $|b|/\sigma_b = 1.80/0.18 = 10.0$, so yes, significant at $10\sigma$
(the uncertainty is dominated by the correction, not by the record).
**(c)** $A = 5\times10^{11}\ \mathrm{m^{2}}$;
$\Delta M = \rho_w(0.01802)(5\times10^{11}) = 9.01\times10^{12}\
\mathrm{kg\,yr^{-1}}$ mass loss; sea level
$\Delta\mathrm{SL} = 9.01\times10^{12}/(1000\times3.6113\times10^{14})
= 2.50\times10^{-5}\ \mathrm{m\,yr^{-1}} = 0.0250\ \mathrm{mm\,yr^{-1}}$.
**(d)** *Measured*: the trend and its formal error. *Converted*: water equivalent
via the load Love numbers, and the sea-level division. *Corrected*: solid-Earth
response and leakage, each with stated uncertainty. *Assumed*: that the mass
change is a surface layer, that the corrections are additive, and that the
network of solutions is internally consistent. **(e)** The statistical error
scales as $T^{-3/2}$, so halving it needs $T \to 2^{2/3}T = 1.59T$, i.e. about
$4.7$ more years — but the *total* uncertainty is dominated by the
$0.15\ \mathrm{cm\,yr^{-1}}$ correction, so a longer record would barely improve
the answer. **Reducing the correction uncertainty is worth more than more data
here**, and that is the real lesson.

## 12. Further reading

- **Torge, W. & Müller, J., *Geodesy*** — time-variable gravity in the wider
  context of geodetic monitoring.
- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the layer formula and
  its normalisation.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — the boundary-value
  framework behind the coefficients.
- **Turcotte, D. L. & Schubert, G., *Geodynamics*** — the solid-Earth response
  that must be removed from a surface-mass signal.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 13. Related lessons

- [01 GRACE and GRACE-FO: Mission Concept and Data Products](01-grace-gracefo.md) —
  where the coefficients and the noise come from.
- [04 Mass Concentration Solutions, Leakage and Filtering](04-mascons-and-leakage.md) —
  the leakage fraction used in Section 3.2, measured.
- [07-04-04 GNSS for Tectonics, Subsidence and Sea Level](../04-geodesy-reference-frames/04-gnss-geodesy-applications.md) —
  the independent measurement of vertical motion and sea level.
- [06-04 Post-Glacial Rebound: Viscosity and Ice History Inference](../06-earth-tides-and-rotation/04-post-glacial-rebound.md) —
  the correction that dominates several real basins.

## 14. Common pitfalls

1. **A trend without its error is not a measurement.** It is a slope.
2. **A correction without its uncertainty is a second slope.** The demonstration's
   correction is $40\%$ of the signal.
3. **Extrapolating a ten-year trend over a century.** Ice-sheet and aquifer
   behaviour is not linear over that range; the trend is a local description.
4. **Assuming the error bar includes the systematic terms.** Least-squares
   errors do not know about filter width, Love numbers or GIA.
5. **Comparing filtered observations with raw model output.**
6. **Reporting a budget that closes:** with large errors, closure is not evidence.

## 15. Related modules

- [Satellite Gravimetry](./README.md) — this module's index.
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  the frames, heights and GNSS measurements that provide the independent checks.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the science the groundwater trends inform.
- [15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md) —
  where the sea-level component is used.
- [26-reference-library](../../26-reference-library/README.md) — symbols, units
  and constants used without re-derivation.

## 16. Self-assessment checklist

- [ ] I can fit a trend with seasonals and quote its standard error.
- [ ] I can explain the sign and size of the seasonal-omission bias.
- [ ] I can scale a trend uncertainty with record length.
- [ ] I can propagate a correction uncertainty into a reported rate.
- [ ] I can convert a mass trend into a sea-level rate.
- [ ] I can decide whether a correction matters by comparing it with the error.
- [ ] I can label every number in an application claim by its status.
