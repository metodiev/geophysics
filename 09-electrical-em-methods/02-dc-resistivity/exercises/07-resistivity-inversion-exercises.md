# Exercises — 09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints

Attempt these before reading the
[solutions](./07-resistivity-inversion-solutions.md). The lesson is
[07 Resistivity Inversion](../07-resistivity-inversion.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the damped normal equations for the inversion, naming each
matrix and its dimensions for 8 data and a 4-layer model.

**★2.** Explain in two sentences why the model parameters are log-resistivities
rather than resistivities.

**★3.** State the discrepancy principle as used in the lesson, with its
threshold and the direction of the selection rule.

## ★★ Applied

**★★4.** From the lesson's iteration table, at which iteration does
$\chi^{2}$ per datum first fall below 1.0, and what is the roughness then? What
has happened to the model by iteration 14?

**★★5.** The lesson's covariance table gives $1\sigma$ of 1.6%, 18.4%, 14.9%
and (bounded) for the four layers. Compute the $2\sigma$ *resistivity* range for
layer 2 around 33.5 $\Omega\,\mathrm{m}$ and state whether a borehole sample at
$30\ \Omega\,\mathrm{m}$ is consistent with it.

**★★6.** A single datum is corrupted by $+20\%$; the least-squares inversion
gives layer 2 as 67.9 $\Omega\,\mathrm{m}$ and three reweighting sweeps give 48.7
$\Omega\,\mathrm{m}$, against a true 30.0. Compute the residual of the corrupted
datum in units of the assumed 2% error for the least-squares solution, and state
what it tells you.

## ★★★ Research-oriented

**★★★7.** The lesson chooses $\lambda$ by the smallest value whose linearised
$\chi^{2}$ still reaches 0.9. Show that this convention is equivalent to
"the roughest model consistent with the data" and then construct a data set
where it selects a model that is physically unacceptable, explaining why the
convention needs an auxiliary constraint.

**★★★8.** Design an inversion protocol for a monitoring survey that must
distinguish a real 5% change from processing artefacts, specifying: the
inversion parameters held fixed between epochs, the statistics you would
compute, the null-space direction you would project out, and the falsification
test for a claimed change.
