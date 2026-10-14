---
id: 06-08-05
title: "Joint Inversion of Receiver Functions and Surface Waves"
level: research
prereqs: ["06-08-02", "06-08-04"]
tags: [seismology, joint-inversion, receiver-functions, surface-waves, inverse-problems]
---

# Joint Inversion of Receiver Functions and Surface Waves

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why receiver functions and surface-wave dispersion constrain
   *different* combinations of the crustal parameters, and why that difference
   is what makes joint inversion work.
2. **Derive** the fundamental-mode Love-wave dispersion relation for a single
   layer over a half-space and verify its asymptotic limits.
3. **Build** a joint objective of squared, normalised residuals, and show how it
   converts a ridge into a peak.
4. **Quantify** the reduction in the admitted $H$ range achieved by adding an
   independent measurement (from 16 km to 1 km in the demonstration).
5. **State** when joint inversion helps, when it merely re-weights, and where the
   residual non-uniqueness remains.
6. **Recognise** the assumptions of the linearised, grid-searched approach and
   when a fully non-linear Bayesian treatment is required.

## Prerequisites

- [02 H-K Stacking and Crustal Thickness Estimation](02-h-k-stacking.md).
- [04 Anisotropy from Receiver Functions and Shear-Wave Splitting](04-anisotropy-receiver-functions.md).

## 1. Intuition: two measurements, two shadows

Each geophysical measurement is a *shadow* of the Earth: it compresses a
structure into a few numbers, and many structures cast the same shadow. A single
receiver function casts a shadow in which $H$ and $k$ are tangled — the ridge of
lessons 01 and 02. Surface-wave dispersion casts a different shadow: the phase
velocity at each period is controlled mainly by the shear speed over the depth
range the wave samples, with almost no dependence on the sharpness of individual
interfaces.

Two different shadows of the same object, intersected, locate it much better than
either alone. That is the entire content of joint inversion, and the mathematics
is only bookkeeping: define one objective that measures how badly a candidate
model reproduces *both* data sets, and search for the model that minimises it.

The honest caveats are equally important: joint inversion cannot create
information that neither data set contains, the relative weighting is a choice
with consequences, and a model that fits both data sets well is not thereby the
true Earth.

## 2. Precise definitions

### 2.1 The two data sets

- **Receiver functions**, reduced here to the single measured Ps delay
  $\Delta t_{Ps}^{\text{obs}}$ at a stated ray parameter, with uncertainty
  $\sigma_t$. This is a deliberate simplification for a transparent demonstration;
  real practice uses the full waveform.
- **Surface-wave dispersion**: fundamental-mode Love-wave phase velocities
  $c^{\text{obs}}(T_j)$ at periods $T_j$, with uncertainties $\sigma_c$. Love
  waves are used because their dispersion relation is the simplest to write and
  solve, so the demonstration can be verified analytically.

### 2.2 The objective

For a candidate model $m = (H, k)$ with $v_p$ fixed,

$$\chi^2(m) = \underbrace{\frac{\left(\Delta t_{Ps}(m)-
\Delta t_{Ps}^{\text{obs}}\right)^{2}}{\sigma_t^{2}}}_{\text{receiver function}}
+ \underbrace{\sum_{j=1}^{N_T}
\frac{\left(c_j(m)-c_j^{\text{obs}}\right)^{2}}{\sigma_c^{2}}}_{\text{dispersion}}.$$

The normalisation by $\sigma^2$ is what makes the two data sets comparable: a
residual is measured in units of its own uncertainty. Without it, the weighting
would be decided by the accidental units of the two measurements.

### 2.3 Love-wave dispersion relation

For an SH wave in a layer (thickness $H$, shear speed $b_1$, density
$\rho_1$) over a half-space (speed $b_2 > b_1$, density $\rho_2$), the
fundamental mode satisfies

$$\tan\!\left(\omega H\sqrt{\frac{1}{b_1^{2}}-\frac{1}{c^{2}}}\right)
= \frac{\mu_2\sqrt{\dfrac{1}{c^{2}}-\dfrac{1}{b_2^{2}}}}
{\mu_1\sqrt{\dfrac{1}{b_1^{2}}-\dfrac{1}{c^{2}}}}, \qquad \mu = \rho b^{2},$$

with $\omega = 2\pi/T$ and $b_1 < c < b_2$ for the fundamental mode.

## 3. Derivations

### 3.1 Where the dispersion relation comes from

Inside the layer the SH displacement is a sum of a downgoing and an upgoing wave;
in the half-space it must decay (or radiate downward) so that energy leaves the
layer. Matching displacement and traction at the interface, and requiring the
traction to vanish at the free surface, gives two equations in two amplitudes. A
non-trivial solution exists only when the determinant vanishes, and that
condition is the dispersion relation above.

The two physical limits are worth fixing in mind:

- **Short period** ($\omega\to\infty$, shallow sampling): the wave is confined to
  the layer and $c\to b_1$.
- **Long period** ($\omega\to 0$, deep sampling): the wave samples the
  half-space and $c\to b_2$.

*Numerical check (SYNTHETIC).* With $H=30\ \mathrm{km}$, $b_1=3.650\
\mathrm{km\,s^{-1}}$, $b_2=4.50\ \mathrm{km\,s^{-1}}$, solving the relation
numerically gives $c = 3.7337\ \mathrm{km\,s^{-1}}$ at $T = 8\ \mathrm{s}$ and
$c=4.1972\ \mathrm{km\,s^{-1}}$ at $T=30\ \mathrm{s}$. The limits hold:
$c=3.6648$ at $T=1\ \mathrm{s}$ (layer speed $3.6501$, difference
$14.7\ \mathrm{m\,s^{-1}}$) and $c=4.4917$ at $T=200\ \mathrm{s}$ (half-space
speed $4.5000$, difference $8.3\ \mathrm{m\,s^{-1}}$). Independent verification
of the solver against its own asymptotics is the cheapest check available and
should always be done.

### 3.2 Why the two data sets see different things

- The **receiver function** measures $t_{Ps}=H(q_s-q_p)$ at a single $p$: a
  product of thickness and a velocity *difference*. It is insensitive to the
  absolute $v_s$ for a given $k$.
- The **dispersion** measures phase velocities over a period band: these depend
  on $b_1$ and $H$ mostly through the ratio $H/\lambda$ and the absolute $b_1$.
  For a fixed band, the dispersion curve constrains $b_1$ (hence $k$ if $v_p$ is
  known) and $H$ jointly, but with a different trade-off than the receiver
  function.

The two trade-off directions are not parallel, so their intersection is compact.
Formally, the two objectives' null directions differ; the joint Hessian is
better conditioned than either.

### 3.3 From a ridge to a peak — the measurement

The demonstration grids $H\in[24,40]\ \mathrm{km}$ (step $0.5$) and
$k\in[1.55,1.95]$ (step $0.005$), $2673$ cells, and evaluates both objectives
with SYNTHETIC data ($\Delta t^{\text{obs}} = 3.60\ \mathrm{s}$,
$\sigma_t = 0.05\ \mathrm{s}$; eight dispersion periods,
$\sigma_c = 0.02\ \mathrm{km\,s^{-1}}$). Taking the $1\sigma$ set as
$\chi^2 \le \chi^2_{\min}+1$:

| objective | best $(H,k)$ | $H$ admitted | span |
|---|---|---|---|
| receiver function alone | $(25.50, 1.860)$ | $24.00$–$40.00\ \mathrm{km}$ | $16.0\ \mathrm{km}$ |
| dispersion alone | $(29.00, 1.730)$ | $28.00$–$30.00\ \mathrm{km}$ | $2.0\ \mathrm{km}$ |
| **joint** | $(30.00, 1.725)$ | $29.50$–$30.50\ \mathrm{km}$ | $1.0\ \mathrm{km}$ |

The true model is $H = 30.0\ \mathrm{km}$, $k = 1.726$. The receiver function
alone admits the entire grid in $H$ — it is a ridge, exactly as predicted — while
the joint objective recovers the truth to the grid spacing. This is the
quantitative payoff, and it is reproducible from `code/joint_inversion_demo.py`.

**Honest reading.** The dispersion alone already admits only $2\ \mathrm{km}$ of
$H$. The joint inversion helps the receiver function much more than it helps the
dispersion. In a real study the balance depends on the quality and period range
of each data set; the demonstration's balance is a **stated, chosen** one.

### 3.4 Weighting and the meaning of $\sigma$

The objective treats $\sigma_t$ and $\sigma_c$ as known. If they are
underestimated, the corresponding data set dominates and the joint answer is
effectively that data set alone. A defensible practice is to report the solution
for at least two weightings and show that the conclusion is stable. If it is not
stable, the data do not determine the answer and no weighting will fix that.

## 4. Physical interpretation

- **Different physics, different shadows.** The receiver function uses converted
  body waves, sensitive to sharp contrasts. Dispersion uses guided surface
  waves, sensitive to the average speed over their sampling depth. Combining them
  is not redundant averaging; it is complementary illumination.
- **The ridge is real information.** A receiver function that admits 16 km of $H$
  is telling you that it constrains one combination of $H$ and $k$ very well.
  The joint inversion sharpens the answer by adding a second constraint, not by
  discovering that the first was wrong.
- **No method escapes non-uniqueness entirely.** Even the joint objective can be
  fooled by a thin low-velocity layer, by anisotropy, or by a mis-specified
  $v_p$; the improvement is quantitative, not absolute.

### 4.1 When joint inversion does not help

Joint inversion is not a universal cure, and three failure modes are worth
naming.

1. **Correlated null directions.** If the second data set's trade-off happens to
   be nearly parallel to the first's ridge, their intersection stays a ridge. The
   demonstration's two trade-offs are nearly orthogonal — that is *why* it works
   so well — and this is a property that must be checked, not assumed.
2. **Systematic model error.** If the Earth has anisotropy, a dipping interface
   or a low-velocity zone that the single-layer model cannot represent, both data
   sets will be misfit systematically, and the joint peak can be sharp yet wrong.
   A sharp joint minimum is evidence of consistency, not of truth.
3. **Mislabelled uncertainties.** If $\sigma_c$ is understated, the dispersion
   term dominates and the receiver function contributes little; the joint answer
   becomes the dispersion answer with extra steps.

The constructive response is to report the admitted set for several weightings
and to inspect residual patterns rather than only the total $\chi^2$. Structured
residuals are the signature of a missing physical effect.

## 5. Assumptions

1. A single isotropic layer over a half-space, with $v_p$ known independently.
2. Laterally homogeneous structure under the station for both data sets.
3. Errors in the two data sets are independent and Gaussian, with known
   standard deviations.
4. The Love-wave fundamental mode is identified correctly; higher modes are not
   mixed in.
5. The receiver-function delay is measured at a known ray parameter, and the
   same structure applies to both measurements.
6. The grid is fine enough near the optimum; a coarse grid can hide the true
   minimum. The residual bias in the demonstration is pure grid discretisation.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $H$ | km | |
| $b_1, b_2, c$ | $\mathrm{km\,s^{-1}}$ | |
| $T$ | s | $\omega = 2\pi/T$, $\mathrm{s^{-1}}$ |
| $\omega H\sqrt{b_1^{-2}-c^{-2}}$ | dimensionless | $\mathrm{s^{-1}\cdot km\cdot s\,km^{-1}}$ |
| $\Delta t$, $\sigma_t$ | s | ratio dimensionless |
| $\sigma_c$ | $\mathrm{km\,s^{-1}}$ | ratio dimensionless |
| $\chi^2$ | dimensionless | sum of squared standardised residuals |

Both terms of $\chi^2$ are dimensionless only because each residual is divided by
its own uncertainty; a mixed-unit objective is the commonest error in
hand-rolled joint inversions.

## 7. Worked examples

### Example 1 — one term of the objective

Candidate $m_1$ gives $\Delta t = 3.65\ \mathrm{s}$ against
$\Delta t^{\text{obs}} = 3.60\ \mathrm{s}$ with $\sigma_t = 0.05\ \mathrm{s}$:

$$\chi^2_{\text{RF}} = \left(\frac{3.65-3.60}{0.05}\right)^{2} = 1.0.$$

If the same candidate misfits two dispersion points by $0.02$ and
$0.03\ \mathrm{km\,s^{-1}}$ with $\sigma_c = 0.02$:

$$\chi^2_{\text{disp}} = 1^{2} + 1.5^{2} = 3.25, \qquad
\chi^2 = 4.25.$$

A candidate that halves the delay residual but doubles the dispersion residual
would score $\chi^2 = 0.25 + 13 = 13.25$: worse. The weighting decides which
misfit matters, and that is why the uncertainties must be honest.

### Example 2 — the asymptotic check of the dispersion solver

At $T = 1\ \mathrm{s}$ the Love wave is confined to the top of the layer, so
$c \approx b_1 = 3.6501\ \mathrm{km\,s^{-1}}$; the solver returns $3.6648$, a
$0.4\%$ difference from the finite layer thickness. At $T = 200\ \mathrm{s}$ the
wave samples the half-space, so $c \approx b_2 = 4.5000$; the solver returns
$4.4917$, a $0.18\%$ difference. Both differences shrink as the limits are
approached further, which is the expected behaviour of a correct solver. A solver
that failed one limit would be wrong.

### Example 3 — reading the $1\sigma$ set

The joint best fit is at $(30.00, 1.725)$ with $H$ admitted from $29.50$ to
$30.50$. Reporting "$H = 30.0\ \mathrm{km}$" without that range overstates the
precision; reporting "$H = 30.0 \pm 0.5\ \mathrm{km}$ (joint, $1\sigma$, grid
step $0.5\ \mathrm{km}$)" is defensible and states the discretisation.

### Example 4 — two weightings and the stability test

Take the demonstration's data. With $\sigma_t = 0.05\ \mathrm{s}$ and
$\sigma_c = 0.02\ \mathrm{km\,s^{-1}}$, the joint $1\sigma$ $H$ range is
$1.0\ \mathrm{km}$. Now halve $\sigma_c$ to $0.01\ \mathrm{km\,s^{-1}}$: every
dispersion residual is doubled in standardised units, so the dispersion term
dominates the objective. The admitted range is then set almost entirely by the
dispersion curve, and the receiver function contributes little. Doubling
$\sigma_c$ to $0.04$ instead makes the two terms comparable in a different
balance, and the range widens. The *conclusion* — that $H$ is about $30\
\mathrm{km}$ — survives both, but the *quoted uncertainty* changes materially.
Reporting the uncertainty from one arbitrary weighting would overstate the case.

## 8. Python demonstration

`code/joint_inversion_demo.py`:

1. implements the Love-wave dispersion relation and verifies the short- and
   long-period limits numerically;
2. generates a synthetic observed dispersion curve with stated noise;
3. evaluates the receiver-function, dispersion and joint objectives on a
   $51\times81$ grid;
4. reports the best model and the $1\sigma$ admitted $H$ range for each
   objective;
5. prints the truth so the recovery can be judged.

The demonstration uses no real data and no network access.

## 9. Exercises

Full sets are in
[`exercises/05-joint-inversion-rf-exercises.md`](./exercises/05-joint-inversion-rf-exercises.md)
and
[`exercises/05-joint-inversion-rf-solutions.md`](./exercises/05-joint-inversion-rf-solutions.md).

- **★** Evaluate $\chi^2$ for a candidate given three residuals and their
  uncertainties.
- **★★** Show that the short-period limit of the dispersion relation is $b_1$ by
  taking $\omega\to\infty$ in the tangent argument.
- **★★** Explain why normalising each residual by its uncertainty is necessary
  and what happens if one $\sigma$ is wrong by a factor of two.
- **★★★** Repeat the demonstration with $\sigma_c$ halved and doubled and report
  how the admitted $H$ range changes. State the conclusion in one sentence.

## 10. Common mistakes

1. **Summing raw residuals.** Adding a time residual in seconds to a velocity
   residual in km/s gives a meaningless objective; normalise first.
2. **Treating $\sigma$ as a tuning knob.** Choosing it to get the answer you
   prefer is fitting the error model to the conclusion.
3. **Reporting the grid minimum as a point estimate.** The grid step is part of
   the answer.
4. **Assuming more data always helps.** A second data set with a systematic
   inconsistency (for example, anisotropy that the model ignores) can pull the
   joint solution away from the truth.
5. **Forgetting the model space.** Both objectives are computed for the same
   simple model; if the real Earth violates that model, the joint peak may be
   sharp *and* wrong.
6. **Reporting only the joint answer.** The receiver-function-only and
   dispersion-only answers are part of the result: they show which data set
   actually constrains the parameter, and they let a reader check the claim.
7. **Assuming a smaller objective always means a better model.** $\chi^2$ can be
   lowered by adding parameters or by changing the assumed $v_p$; the objective
   measures consistency with the stated model, not fidelity to the Earth.

## 11. Real-world applications

- **Crustal and uppermost-mantle profiles.** Joint receiver-function and
  dispersion inversion is a standard way to build $v_s$ profiles under a station,
  with the joint constraint mitigating the trade-offs of either alone.
- **Array studies.** With many stations, lateral variations can be mapped while
  the joint constraint at each station keeps the vertical profile honest.
- **Planetary seismology.** On bodies with a single station, joint inversion of
  whatever data exist (body-wave travel times, surface-wave dispersion if
  available) is the only route to a profile.
- **Methodological lesson.** This lesson is a template for any joint inversion:
  identify each data set's null directions, verify that they differ, normalise
  by uncertainty, and report the admitted set. The same reasoning appears in
  [06-06-01 Seismic Tomography: Principles](../06-seismic-tomography/01-tomography-principle.md).

## 12. Further reading

- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. Surface-wave dispersion and the
  layer-over-half-space problem.
- **Shearer, P. M. (2019). *Introduction to Seismology* (3rd ed.). Cambridge
  University Press.** Level: intermediate to advanced. Joint constraints on
  crustal structure.
- **Stein, S., & Wysession, M. (2003). *An Introduction to Seismology,
  Earthquakes, and Earth Structure*. Blackwell.** Level: intermediate.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference. Tools for
  reading and processing the data a joint inversion needs.
- **FDSN web services specification.** <https://www.fdsn.org/webservices/> —
  Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [01 Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md).
- [02 H-K Stacking and Crustal Thickness Estimation](02-h-k-stacking.md).
- [04 Anisotropy from Receiver Functions and Shear-Wave Splitting](04-anisotropy-receiver-functions.md).
- [06-06-01 Seismic Tomography: Principles](../06-seismic-tomography/01-tomography-principle.md) —
  the same inverse-problem logic at a larger scale.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of non-uniqueness, regularisation and resolution.

## 14. Self-assessment checklist

- [ ] I can explain why the two data sets constrain different parameter combinations.
- [ ] I can write the dispersion relation and verify both asymptotic limits.
- [ ] I can build a normalised joint objective and say why normalisation is needed.
- [ ] I can extract and report a $1\sigma$ admitted range from a grid search.
- [ ] I can explain why a sharp joint minimum can still be wrong.
- [ ] I can state when joint inversion helps and when it merely re-weights.
