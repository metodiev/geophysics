# Exercises — 10-05-02 Surface-Wave Methods for Shallow Layers

Attempt these before reading the
[solutions](./02-seismic-surface-wave-nearsurface-solutions.md). The lesson is
[02 Surface-Wave Methods](../02-seismic-surface-wave-nearsurface.md). All models
are **SYNTHETIC** teaching values, and every reference number below is printed by
`code/surface_wave_demo.py`.

## ★ Foundational

**★1.** For Poisson's ratio $\nu = 1/3$ and $\beta = 250\ \mathrm{m\,s^{-1}}$,
compute $\alpha/\beta$ and the Rayleigh-wave speed $c_R$. State the ratio
$c_R/\beta$.

**★2.** A layer has $h = 3\ \mathrm{m}$, $\beta_1 = 150\ \mathrm{m\,s^{-1}}$,
$\rho_1 = 1800\ \mathrm{kg\,m^{-3}}$, over a half-space with
$\beta_2 = 350\ \mathrm{m\,s^{-1}}$, $\rho_2 = 2000\ \mathrm{kg\,m^{-3}}$. Compute
the first three Love-mode cut-off frequencies and state how many modes propagate
at $200\ \mathrm{Hz}$ and at $400\ \mathrm{Hz}$.

**★3.** Explain in two sentences why a Rayleigh wave exists in a uniform
half-space but a Love wave does not.

## ★★ Applied

**★★4.** Verify by hand that $c = 186.991\ \mathrm{m\,s^{-1}}$ is a solution of
the Love dispersion equation at $32\ \mathrm{Hz}$ for the teaching model
($h = 5\ \mathrm{m}$, $\beta_1 = 180$, $\rho_1 = 1800$ over $\beta_2 = 400$,
$\rho_2 = 2000$). Compute $k_1$, $k_1h$, $k_2$, $B$ and $\tan(k_1h)$, and state
the branch index $n$.

**★★5.** Using the measured kernel table, convert a **2% increase of $\beta$ in
the top 1 m** into a phase-velocity change at $16$ and at $64\ \mathrm{Hz}$.
Explain why the two answers differ by less than a factor of two even though the
frequencies differ by a factor of four.

**★★6.** A borehole gives $\beta_1$ with a 5% error. Using the measured
thickness–velocity table, state the thickness error implied at
$4$–$16\ \mathrm{Hz}$ and at $4$–$128\ \mathrm{Hz}$, and say in one sentence what
that implies for the value of acquiring a wider band.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that would test whether the thickness–velocity
ridge of Section 3.4 is *as wide as the model predicts* for a given data set.
State the data, the inversion, the metric, the control case, and the result that
would falsify the prediction. A specification that could not be executed is a
failed answer.

**★★★8.** A $0.5\ \mathrm{m}$ thick zone of $\beta = 80\ \mathrm{m\,s^{-1}}$
(e.g. a saturated soft pocket) is suspected at $2\ \mathrm{m}$ depth in ground
otherwise described by the teaching model. Using the kernel formalism, estimate
the phase-velocity perturbation at $32$ and $64\ \mathrm{Hz}$, state whether a 1%
measurement could detect it, and name the practical problem that would limit the
detection before the physics does.
