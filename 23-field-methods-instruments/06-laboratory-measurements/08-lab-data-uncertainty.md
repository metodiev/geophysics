---
id: 23-06-08
title: "Laboratory Uncertainty Budgets and Reporting"
level: research
prereqs: ["23-05-04", "23-06-03"]
estimated_minutes: 105
tags: [laboratory, uncertainty, reporting, metrology, reproducibility, interlaboratory]
---

# Laboratory Uncertainty Budgets and Reporting

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** an uncertainty budget from Type A and Type B terms and **combine** them in
   quadrature.
2. **Convert** a certificate's expanded uncertainty, a resolution and a drift estimate into
   standard uncertainties.
3. **Compute** an effective degrees of freedom and **state** when the coverage factor is not
   2.
4. **Propagate** the budget of a derived property and **identify** the dominant term.
5. **Report** a value and its uncertainty with defensible significant digits.
6. **Compare** a result with another laboratory using the $E_n$ score, and **interpret** both
   outcomes.
7. **Separate** repeatability from reproducibility and **state** which one more measurements
   improve.

All values, uncertainties, coefficients and scores here are **SYNTHETIC** teaching values
combined with the standard relations quoted in the text (the GUM-style combination of
standard uncertainties, the rectangular and certificate conversions, the
Welch-Satterthwaite formula, the $E_n$ score, a variance-components model). No certificate,
laboratory standard or measured value is reproduced.

## Prerequisites

- [04 Calibration, Testing and Traceability](../05-instrumentation-and-electronics/04-calibration-and-testing.md) —
  the calibration budget and re-calibration interval that feed this lesson's first term.
- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the derived-property example used throughout.

## 1. Intuition: an uncertainty is a statement about what would change the answer

An uncertainty budget answers one question: **which of the things I did differently from
someone else, or from last time, could move this number?** That framing is what makes the
budget useful, and it is why a budget is built from *sources*, not from instrument
specifications:

- a **Type A** term is one measured by repeating something (a scatter, with degrees of
  freedom);
- a **Type B** term is one taken from documentation or judgement (a certificate, a
  resolution, a temperature coefficient, a drift), and it is converted to a standard
  uncertainty by dividing by a divisor that depends on the assumed distribution;
- the terms are combined in quadrature, which assumes independence — and correlated terms
  must be added linearly instead.

The two mistakes that recur in laboratory reports are (i) quoting only the repeatability,
which is usually the *smallest* term, and (ii) quoting a budget whose dominant term was never
identified, so the improvement effort goes to the wrong measurement.

## 2. Building and combining a budget

Synthetic budget for a mass-based measurement:

| Term | Type | Standard $u$ | Variance share |
|---|---|---|---|
| repeatability ($s = 0.45$, $n = 6$) | A | 0.18371 | 26.46 % |
| calibration certificate ($U = 0.60$, $k = 2$) | B | 0.30000 | 70.56 % |
| resolution 0.1 (rectangular) | B | 0.02887 | 0.65 % |
| temperature ±0.05 (rectangular) | B | 0.02887 | 0.65 % |
| drift since calibration 0.08 (rectangular) | B | 0.04619 | 1.67 % |

with the three conversions that must be applied:

$$u_A = \frac{s}{\sqrt{n}}, \qquad
u_B(\text{rectangular}) = \frac{a}{\sqrt{3}}, \qquad
u_B(\text{certificate}) = \frac{U}{k} ,$$

$$u_c = \sqrt{\sum u_i^{2}} = \sqrt{0.18371^{2} + 0.30000^{2} + 0.02887^{2}
+ 0.02887^{2} + 0.04619^{2}} = 0.35714 .$$

Three points that matter:

1. **The certificate dominates at 70.56 %.** The instrument's own repeatability (26.46 %) is
   *not* the limit, so more repeats would barely help — the lever is a better-calibrated
   reference, or a measurement whose calibration is common-mode across the comparison.
2. **The resolution term is negligible** (0.65 %) whenever the scatter or the certificate
   exceeds it; quoting a budget dominated by resolution is a sign that the repeats were not
   taken.
3. **A rectangular assumption is generous.** Using $a/\sqrt{3}$ rather than $a/2$ (a
   triangular assumption would give $a/\sqrt{6}$) is a judgement that must be stated; the
   divisor is a modelling choice, not a measurement.

## 3. Coverage factors and degrees of freedom

The expanded uncertainty is $U = k u_c$, with $k$ from the Student distribution at the
effective degrees of freedom

$$\nu_{\text{eff}} = \frac{u_c^{4}}{\sum \dfrac{u_i^{4}}{\nu_i}} .$$

Here only the Type A term has finite degrees of freedom ($\nu = 5$), giving
$\nu_{\text{eff}} = 71.4$, so $k = 1.99$ for 95 % and $U = 0.71071$ against the familiar
$k = 2$ value of 0.71428 — the small-sample correction is 0.5 %. **But that is a consequence
of a well-measured Type A term**:

| Repeats $n$ | Degrees of freedom | $t$(95 %) |
|---|---|---|
| 2 | 1 | 12.710 |
| 3 | 2 | 4.303 |
| 4 | 3 | 3.182 |
| 6 | 5 | 2.571 |
| 10 | 9 | 2.262 |
| 20 | 19 | 2.093 |

So an uncertainty quoted as "$k = 2$" from **three repeats** understates a 95 % interval by a
factor of 2.2. The rule that follows: state $k$, or state the coverage probability *and* the
degrees of freedom; a bare "±" with no basis is not a statement about anything.

## 4. Propagating a derived quantity

For porosity from a mass difference and a bulk volume,

$$\phi = \frac{\Delta m}{\rho_w V_{\text{bulk}}} ,$$

and the relative uncertainties combine in quadrature:

| Term | Value | Relative $u$ | Variance share |
|---|---|---|---|
| mass difference | $6.90 \pm 0.020$ g | 0.2899 % | 76.34 % |
| bulk volume | $32.60 \pm 0.050$ cm³ | 0.1534 % | 21.38 % |
| fluid density | $0.998 \pm 0.0005$ g/cm³ | 0.0501 % | 2.28 % |
| **combined** | $\phi = 21.2081$ % | **0.3317 %** | 100 % |

giving $u(\phi) = 0.0704$ porosity points and $U = 0.1407$ points at $k = 2$.

The dominant term is the **mass difference**, at 76.34 % — which is a *difference*, so its
relative uncertainty is that of a small number: a 0.020 g uncertainty on a 6.90 g difference
is 0.29 %, whereas the same balance uncertainty on the 200 g dry mass would be 0.01 %. This
is the single most useful pattern in laboratory uncertainty work: **derived properties
usually hinge on differences, and differences amplify relative errors**. The remedies are a
larger signal (a bigger specimen), a common-mode cancellation, or a better balance — in that
order of cost-effectiveness.

## 5. Reporting

The rules, applied to $\phi = 21.2081$ % with $u = 0.3571$ %:

| Practice | Example | Verdict |
|---|---|---|
| two significant digits for $U$, value to the same place | $21.21 \pm 0.71$ % ($k = 2$) | correct |
| interval too coarse | $21.2081 \pm 0.7$ % | over-rounded |
| false precision | $21.208100 \pm 0.71428$ % | under-rounded |
| no basis given | $21.21 \pm 0.71$ % | incomplete: state $k$ (or 95 %) |

Four more statements that belong with a laboratory value:

1. **The measurement conditions**: temperature, saturation, fluid, stress state, frequency —
   whichever of them the property depends on.
2. **The specimen count and the variability**: "$n = 12$, between-specimen sd 0.45" is part
   of the result, not part of the metadata.
3. **Which uncertainties are systematic**: a calibration offset, a protocol difference and a
   temperature coefficient are one-signed, and they are the terms that survive a comparison
   with another laboratory.
4. **The traceability statement**, with the calibration chain's uncertainty included (see
   [04 Calibration, Testing and Traceability](../05-instrumentation-and-electronics/04-calibration-and-testing.md)).

## 6. Comparing with another laboratory: the $E_n$ score

Inter-laboratory comparison is where a budget is tested. The $E_n$ score compares a
difference with the combined uncertainty:

$$E_n = \frac{\lvert x - x_{\text{ref}}\rvert}
{\sqrt{u^{2} + u_{\text{ref}}^{2}}} ,$$

and a result is consistent when $E_n < 1$:

| Case | Difference | Combined $u$ | $E_n$ | Verdict |
|---|---|---|---|---|
| consistent, tight budgets | 0.10 | 0.1221 | 0.819 | consistent |
| the case above | 0.25 | 0.1221 | **2.048** | **inconsistent** |
| large difference, large budgets | 0.25 | 0.3606 | 0.693 | consistent |
| small difference, tiny budgets | 0.05 | 0.0224 | 2.236 | inconsistent |

The last two rows are the point: **the score is a ratio, so it tests the budgets as much as
the values**. A difference of 0.25 porosity points is inconsistent with tight budgets and
perfectly consistent with loose ones; a trivially small difference of 0.05 is *inconsistent*
if both laboratories claim 0.02. Two consequences:

1. **A failed $E_n$ is a statement about the budgets**, and the productive response is to find
   which term was underestimated — usually a systematic one (a protocol difference, a
   calibration, a sample-preparation difference) rather than the repeatability.
2. **An $E_n$ that is always far below 1 is not a success**: it usually means the budgets are
   overstated, which is itself a reporting error, because an inflated uncertainty makes every
   comparison pass and hides real disagreement.

## 7. Repeatability, reproducibility, and where the variance lives

The total variance of a reported property has two components: the **repeatability** (the
scatter of repeated measurements on one specimen in one laboratory) and the components that
do not change with repeats — between specimens, between sessions, between laboratories:

$$s_{\text{repro}} = \sqrt{s_r^{2} + s_L^{2}} .$$

With a synthetic $s_r = 0.08$ and $s_L = 0.35$ porosity points:

| Component | Value | Variance share |
|---|---|---|
| within-laboratory repeatability | 0.08 | 4.97 % |
| between-specimen / between-laboratory | 0.35 | 95.03 % |
| reproducibility sd | 0.3590 | 100 % |

| Repeats | Standard error | 95 % half-width |
|---|---|---|
| 1 | 0.3590 | 0.7037 |
| 2 | 0.2539 | 0.4976 |
| 3 | 0.2073 | 0.4063 |
| 6 | 0.1466 | 0.2873 |
| 12 | 0.1036 | 0.2031 |

and to reach a 0.10-point half-width takes $n = (1.96 \times 0.3590/0.10)^{2} = 50$
specimens. **The between-specimen term is 95 % of the variance, so repeating one specimen
buys almost nothing**: the count that matters is the number of *specimens*, and the
improvement that matters is a protocol that reduces the between-specimen differences
(preparation, saturation, measurement conditions) — see
[01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md).

## 8. Assumptions and regime of validity

1. **The terms are independent.** Correlated terms (the same calibration used twice, a
   common temperature) must be combined linearly, and the quadrature sum then understates the
   total.
2. **The distribution assumptions are stated.** Rectangular, triangular and normal divisors
   differ by up to a factor of 1.7 on a single term.
3. **The model of the measurement is correct.** An uncertainty budget for the wrong equation
   is precise and wrong; the sensitivity coefficients $\partial\phi/\partial x_i$ are part of
   the budget.
4. **The scatter reflects the process, not the operator.** A repeatability measured by one
   person on one day is a lower bound on the reproducibility.
5. **The dominant term was actually measured.** A budget whose largest term is a judgement
   (an estimated drift, a manufacturer's coefficient) is a hypothesis until it is verified.
6. **The reference value is itself uncertain.** An inter-laboratory comparison with an
   assumed-exact reference is a comparison with that assumption.

## 9. The honest summary

- A budget is built from sources, not from specifications: Type A scatter and Type B
  certificates, resolutions, coefficients and drifts.
- Here the certificate dominated at 70.56 % and the repeatability was 26.46 %: more repeats
  would not have helped.
- $\nu_{\text{eff}} = 71.4$ made $k = 2$ adequate, but three repeats justify
  $k = 4.303$ — an "$k = 2$" claim from three repeats understates the interval by half.
- Again the dominant source was a **difference** (mass difference, 76.34 % of the variance),
  because a small difference amplifies relative errors.
- Report two significant digits for $U$ and the value to the same place; always state $k$ or
  the coverage.
- $E_n$ tests the budgets as much as the values, and an $E_n$ far below 1 is a sign the
  budgets are overstated.
- With $s_L$ at 95 % of the variance, the lever is specimens and protocol, not repeats.

## 10. Python demonstration

[`code/lab_uncertainty_demo.py`](./code/lab_uncertainty_demo.py) prints every number quoted
above: the five-term budget with its variance shares and effective degrees of freedom, the
$t$-factor table, the propagated porosity budget, the reporting examples, four $E_n$ cases
and the repeatability/reproducibility decomposition with the specimen count a target needs.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lab_uncertainty_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/08-lab-data-uncertainty-exercises.md`](./exercises/08-lab-data-uncertainty-exercises.md)
and
[`exercises/08-lab-data-uncertainty-solutions.md`](./exercises/08-lab-data-uncertainty-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. Convert to standard uncertainties: a repeatability $s = 0.30$ from $n = 9$; a certificate
   $U = 0.80$ at $k = 2$; a resolution of 0.02 (rectangular).
2. Combine those three and compute $U$ at $k = 2$ and each term's variance share.
3. Give an effective degrees of freedom for the combination of (1) and state the coverage
   factor you would use.
4. A porosity is $\Delta m = 4.20 \pm 0.015$ g over $\rho_w V = 18.40$ cm³ (no volume
   uncertainty). Compute $\phi$ and its relative uncertainty.
5. A laboratory reports $12.40 \pm 0.05$ and a reference $12.30 \pm 0.04$. Compute $E_n$ and
   state the verdict.

## 13. Common pitfalls

1. **Quoting the repeatability as the uncertainty.** It is usually the smallest term.
2. **"$k = 2$" with three repeats.** The correct factor is 4.3.
3. **Forgetting the divisor basis.** Rectangular and triangular differ by 1.7 on a term.
4. **Correlated terms in quadrature.** It understates the total.
5. **Over-rounding the uncertainty or under-rounding the value.** Both destroy information.
6. **Reporting a difference-dominated property without noticing.** The dominant term is a
   small difference.
7. **Treating a passed $E_n$ as validation and an $E_n$ far below 1 as excellence.** It may
   mean the budgets are too loose.
8. **Repeating one specimen to improve a between-specimen-limited result.** It cannot.

## 14. Where this is used

- Every laboratory value published in rock physics, petrophysics and geochemistry: the
  budget is the difference between a number and a result.
- Inter-laboratory comparisons and proficiency tests, where $E_n$ is the standard metric.
- Calibration records and traceability statements, which this lesson's first term comes from
  — see
  [04 Calibration, Testing and Traceability](../05-instrumentation-and-electronics/04-calibration-and-testing.md).
- Any dataset reused by someone else, where the uncertainty determines what the data can be
  used for — see [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md).

## 15. Related lessons

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the largest component of most laboratory variance.
- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the derived-property example worked here.
- [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md) —
  a budget whose dominant term is a timing difference.
- [04 Calibration, Testing and Traceability](../05-instrumentation-and-electronics/04-calibration-and-testing.md) —
  the calibration budget this lesson's Type B terms come from.

## 16. Self-assessment checklist

- [ ] I can build a Type A + Type B budget and combine it in quadrature.
- [ ] I can convert certificates, resolutions and drifts into standard uncertainties.
- [ ] I can compute an effective degrees of freedom and choose a coverage factor.
- [ ] I can propagate a derived quantity's budget and name the dominant term.
- [ ] I can report a value with defensible significant digits.
- [ ] I can compute and interpret an $E_n$ score.
- [ ] I can separate repeatability from reproducibility and say what more measurements buy.
