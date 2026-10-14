# Exercises — 25-04-03 Project: InSAR Deformation Time Series Analysis

Attempt these before reading the
[solutions](./03-insar-deformation-project-solutions.md). The project is
[03 InSAR Time Series](../03-insar-deformation-project.md). Values printed by
[`code/insar_timeseries_demo.py`](../code/insar_timeseries_demo.py):

| Quantity | Value |
|---|---|
| series | 60 epochs, 18-day repeat, span 2.95 yr |
| truth | 12.0 mm/yr, 8.0 mm annual, 10.0 mm step at 1.95 yr, 3.0 mm noise |
| step-free: rate only | $10.3834 \pm 2.6966$ mm/yr, rms 5.9276 mm |
| step-free: rate + season | $12.0207 \pm 1.2355$ mm/yr, rms 2.5760 mm |
| with step: rate + season | $16.7561 \pm 1.6209$ mm/yr, rms 3.3796 mm |
| with step: full model | $13.2905 \pm 2.6921$ mm/yr, rms 2.8863 mm |
| recovered step | $7.1133 \pm 4.7237$ mm (true 10.0) |
| transient windows | $23.0487 \pm 7.8911$; $14.2215 \pm 1.6153$; $14.1207 \pm 4.3579$ mm/yr |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Write the design matrix columns for a rate, an annual season and a step at
$t_s$, and state which fitted coefficient is the deformation rate and which is the
step.

**★2.** The step-free series gives a rate of $10.3834$ mm/yr without a seasonal
term and $12.0207$ mm/yr with one. Compute the bias, its ratio to the correct
model's error bar, and state why the residual rms alone does not identify the
missing term.

**★3.** The step is recovered as $7.1133 \pm 4.7237$ mm against a true 10.0 mm.
Compute the discrepancy in units of the uncertainty, and state the two reasons the
uncertainty is large.

## ★★ Applied

**★★4.** Compute the bias from omitting the step ($16.7561$ against $13.2905$
mm/yr) and express it as a fraction of the true rate. State which of the two
omissions in this project is the more dangerous and why.

**★★5.** The early window (0–1.0 yr) returns $23.0487 \pm 7.8911$ mm/yr against a
true 12.0. Show that this is consistent with a linear-plus-exponential signal whose
transient decays with a 0.3 yr time constant, and compute the mean rate of that
signal over the window analytically to compare with the fitted value.

**★★6.** A colleague reports a rate of $14.2 \pm 0.3$ mm/yr from the transient
series over 0.25–3.0 yr, quoting the formal error. State why the quoted error is
too small and what the honest uncertainty is, using the demonstration's numbers.

## ★★★ Research-oriented

**★★★7.** Design a time-series model for a subsidence study on a coastal aquifer
where the signal may contain a linear trend, a seasonal groundwater cycle, a
coseismic step, and a slowing (decelerating) compaction transient. State the
functional form for each term, the number of parameters, how you would choose
between competing forms objectively, the observation span needed to separate the
terms, and the test that would show your model is over-parameterised rather than
correct. A design without the last item is a failed answer.
