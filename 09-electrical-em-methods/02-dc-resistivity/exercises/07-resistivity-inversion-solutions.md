# Solutions — 09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints

> **Read after attempting the exercises.** Lesson:
> [07 Resistivity Inversion](../07-resistivity-inversion.md).

---

## ★1 — The normal equations

$$\left(J^{\mathsf{T}}J + \lambda D^{\mathsf{T}}D\right)\delta m
= J^{\mathsf{T}}r,$$

with $J$ the $8\times4$ sensitivity matrix
$J_{ij} = \partial f_i/\partial m_j$ (data $i$, parameter $j$),
$D$ the $3\times4$ first-difference matrix, $\lambda$ a scalar,
$\delta m$ the $4\times1$ model update and $r$ the $8\times1$ vector of
scaled residuals $(d_i-f_i)/\sigma$.

$J^{\mathsf{T}}J$ is $4\times4$; $D^{\mathsf{T}}D$ is $4\times4$ (rank 3, a
Laplacian-like operator with a null space of constant models), which is why the
data term is needed to fix the level.

---

## ★2 — Why log parameters

Because resistivity spans six decades: in linear space one large deep value
dominates the Jacobian and the inversion spends its effort reducing a number that
the data constrain poorly, while relative errors are what the physics actually
controls. Log parameters also make a smoothness penalty on *ratios* rather than
differences, which is the right statement for a quantity defined up to a factor.

---

## ★3 — The discrepancy principle

Choose the **smallest** $\lambda$ whose linearised $\chi^{2}$ per datum still
reaches 0.9 (the lesson's explicit convention). Smaller $\lambda$ overfits the
noise; larger $\lambda$ adds systematic misfit. The direction of the rule — take
the smallest admissible $\lambda$, i.e. the roughest admissible model — is a
*choice*: the equally defensible alternative is the largest $\lambda$ with
$\chi^{2}\le1$, and the two differ in the deep layers by hundreds of per cent in
this example.

---

## ★4 — Convergence

From the table: $\chi^{2}$ first falls below 1.0 between iterations 3 and 4
(1.146 → 0.999), where the roughness is about 2.43. By iteration 14,
$\chi^{2} = 0.926$ (a further $7\%$ improvement over 10 iterations) while the
roughness has risen from 2.43 to 3.09 — a $27\%$ increase in structure bought
with $7\%$ of misfit. That is the classic signature of a converged fit that is
now trading misfit for structure, and it is the reason the trade-off parameter
must be chosen deliberately rather than by running to convergence at a fixed
$\lambda$.

---

## ★5 — A $2\sigma$ range

$2\sigma = 2\times18.4\% = 36.8\%$ in the log (which is the fractional
uncertainty), so

$$\rho_2 = 33.5\ \Omega\,\mathrm{m}\times\mathrm{e}^{\pm0.368}
= 33.5\times[0.692, 1.445] = [23.2,\ 48.4]\ \Omega\,\mathrm{m}.$$

A borehole sample at $30\ \Omega\,\mathrm{m}$ lies inside the range with room to
spare, so the two are **consistent**. Note what the statement does *not* say: it
does not confirm that 33.5 is the right answer — the covariance is a statement
about the family, and a sample at 48 would be equally consistent.

---

## ★6 — The residual of a bad datum

The corrupted datum is $+20\%$ high. In the least-squares solution the inversion
has partly absorbed it into the model, so the residual is smaller than 20%. With
layer 2 at 67.9 $\Omega\,\mathrm{m}$ against a true 30.0, the model itself
carries part of the error; the fitted curve at $a = 6$ m is pulled upward. A
defensible estimate of the residual ratio uses the printed $\chi^{2} = 9.728$
with 8 data: the total squared scaled residual is
$8\times9.728 = 77.8$, of which the corrupted datum contributes the dominant
share. Assuming the other seven data sit near $\chi^{2}\approx1$
(7 contributions of ~1), the corrupted one has

$$r_\text{bad}^{2} \approx 77.8 - 7 = 70.8 \Rightarrow r_\text{bad}
\approx 8.4\ \mathrm{sigma}.$$

So the offending datum is an **8-sigma outlier relative to the assumed 2%
error**. That is the diagnostic: not "the fit is bad" but "*this datum* is
inconsistent with the error model by a factor 8". The correct actions are to
reweight it (as the demonstration does) and to investigate why — a bad electrode
contact, a cable fault, or a genuine geological surprise.

---

## ★7 — The convention's failure mode

**Equivalence.** For a smoothness penaltly, increasing $\lambda$ strictly
increases the penalty term at fixed misfit; the admissible set
$\{\lambda : \chi^{2}(\lambda) \le \chi^{2}_\text{target}\}$ is an interval, and
its smallest element is by construction the model with the largest roughness
$\|Dm\|$ among admissible ones. So "smallest $\lambda$ with
$\chi^{2} \ge 0.9$" = "roughest model that still fits".

**Failure mode.** Suppose the target is a *conductive* body under a resistive
cover with a very small sensitivity (a null direction dominated by $S = h/\rho$).
The roughest admissible model can put the entire conductance into a
vanishingly thin, arbitrarily conductive sheet at the sensitivity maximum,
because thinning the sheet is nearly free in $\chi^{2}$ while the smoothness
penalty is small for a single-jump model. The selected model is then physically
unacceptable (a layer thinner than a pore scale) even though it fits.

**Resolution.** The convention needs an *auxiliary constraint*: bounds on
thickness, a penalty on total variation rather than on squared gradient, or a
prior with a length scale. That is exactly the lesson's point about bounds being
part of the formulation, and about the choice of norm being part of the answer.

---

## ★8 — A monitoring protocol

1. **Fix between epochs.** The discretisation (layer boundaries or mesh), the
   regularisation operator $D$ and its weight $\lambda$, the data error model,
   and the starting model. Differencing inversions that used different
   parameters produces a difference that is mostly the parameters.
2. **Statistics.** Report the changed-model estimate with its covariance,
   computed from the linearised system at the *base* model, plus the
   *difference* covariance $\mathrm{Cov}(\Delta m) \approx 2\mathrm{Cov}(m)$
   for independent errors. A claimed change must exceed $2\sigma$ of the
   difference, not of either model.
3. **Project out the null space.** Compute the SVD of the base Jacobian and
   report the change *after* projecting onto the well-determined subspace,
   together with the fraction of the model norm that the projection removed. A
   change that lives mostly in the null space is not measured.
4. **Falsification test.** (i) Re-invert with a different $\lambda$ and a
   different discretisation: a real change survives; a processing artefact does
   not. (ii) Check a *null* target region where nothing should change: if the
   inversion reports change there, the noise model is wrong and the claimed
   change cannot be trusted. (iii) Repeat the survey with a reversed array
   (reciprocal measurements): the difference gives a direct estimate of the
   repeatability, which must be smaller than the claimed change.
