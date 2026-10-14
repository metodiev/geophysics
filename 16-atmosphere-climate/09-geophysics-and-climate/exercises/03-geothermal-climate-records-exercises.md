# Exercises — 16-09-03 Borehole Temperature Records of Past Climate

Attempt these before reading the
[solutions](./03-geothermal-climate-records-solutions.md). The lesson is
[03 Borehole Temperature Records of Past Climate](../03-geothermal-climate-records.md).
All models and numbers are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** With $\kappa = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, a surface step
of $1.5\ \mathrm{K}$ occurred $150$ years ago. Compute the perturbation at
$z = 60\ \mathrm{m}$ today, showing the value of
$u = z/(2\sqrt{\kappa t})$.

**★2.** Compute the e-folding depth for surface oscillations of period $50$,
$200$ and $500$ years, and state which of the three a $300\ \mathrm{m}$ profile
resolves best.

**★3.** Using $\kappa = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, compute the
forward-matrix entry $G$ for a $50$-year bin spanning ages $50$ to $100$ years at
depth $50\ \mathrm{m}$.

## ★★ Applied

**★★4.** A design matrix has singular values $1.266$, $0.493$, $0.143$, $0.028$,
$0.003$. Compute the noise amplification $1/\sigma$ for each direction and state
which components can be retained if the profile noise is $0.02\ \mathrm{K}$ and a
history error of $1\ \mathrm{K}$ is acceptable.

**★★5.** Using the demonstration's misfit/resolution table ($k=1$: misfit
$0.2881$, error $1.653$; $k=3$: $0.0238$, $0.399$; $k=5$: $0.0191$, $2.845$;
$k=6$: $0.0190$, $17.230$), choose a truncation for a profile noise of
$0.02\ \mathrm{K}$ and justify the choice in two sentences.

**★★6.** A null direction has singular value $1.0\times10^{-4}$. Compute the change
in the predicted profile produced by a $0.5\ \mathrm{K}$ change along that
direction, and state whether a profile with $0.02\ \mathrm{K}$ noise could detect
it.

## ★★★ Research-oriented

**★★★7.** Design a synthetic experiment to test how much groundwater advection
would have to add to conduction before a diffusion-only inversion misestimates the
surface history. Specify the forward model, the estimator, the metric and the
result that defines the tolerance.

**★★★8.** A borehole reconstruction reports a $2.0\ \mathrm{K}$ warming over
$200$ years with a stated uncertainty of $\pm0.3\ \mathrm{K}$. Design the
sensitivity analysis you would require, naming the three assumptions whose errors
you would propagate and the order in which you would expect them to matter.
