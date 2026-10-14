# Exercises — 10-05-01 EM Induction (EMI) and Conductivity Meters

Attempt these before reading the
[solutions](./01-electromagnetic-induction-nearsurface-solutions.md). The lesson is
[01 EM Induction](../01-electromagnetic-induction-nearsurface.md). All models are
**SYNTHETIC** teaching values; the layer weights are those printed by
`code/em_induction_demo.py` for $a = 0.25\ \mathrm{m}$.

## ★ Foundational

**★1.** A small-loop conductivity meter with $s = 1.00\ \mathrm{m}$ is used at
$f = 9.8\ \mathrm{kHz}$ over ground of conductivity
$\sigma = 50\ \mathrm{mS\,m^{-1}}$. Compute $\omega$, $\omega\mu_0\sigma$, the skin
depth $\delta$ and the induction number $B$. Repeat $B$ for
$s = 2.50\ \mathrm{m}$ and state whether the linear interpretation is defensible
in each case.

**★2.** By dimensional analysis, show that $\sqrt{2/(\omega\mu_0\sigma)}$ is a
length. Start from the SI units of $\mu_0$ ($\mathrm{H\,m^{-1}}$) and use
$\mathrm{1\ H = 1\ kg\,m^2\,s^{-2}\,A^{-2}}$.

**★3.** A three-layer soil has conductivities $80$, $30$ and
$10\ \mathrm{mS\,m^{-1}}$ in the intervals $0$–$0.5$, $0.5$–$1.5$ and
$1.5\ \mathrm{m}$ to infinity. Using the layer weights printed by the
demonstration at $s = 1.00\ \mathrm{m}$, compute $\sigma_a$ and state which
interval contributes most to the reading.

## ★★ Applied

**★★4.** A reading of $55.0\ \mathrm{mS\,m^{-1}}$ is obtained at
$s = 1.00\ \mathrm{m}$ over a half-space of $20.0\ \mathrm{mS\,m^{-1}}$. Using the
layer weights of the demonstration, build **two** models that both explain the
reading: (a) a $0.50\ \mathrm{m}$ surface layer over the half-space; (b) a
$1.50\ \mathrm{m}$ surface layer over the half-space. Then predict the reading of
each model at $s = 2.50\ \mathrm{m}$ and report the percentage difference. State
in one sentence what this shows about a single-spacing interpretation.

**★★5.** The two-spacing system of Section 3.3 has the weight matrix

$$M = \begin{pmatrix} 0.3501 & 0.6499 \\ 0.0845 & 0.9155 \end{pmatrix}.$$

Compute the determinant, the 2-norm condition number and the inverse. If each
reading carries an independent error of $\pm 0.5\ \mathrm{mS\,m^{-1}}$, bound the
error in the recovered layer conductivities $\sigma_1$ (surface layer) and
$\sigma_2$ (half-space). Which of the two is better determined, and why?

**★★6.** A survey reads $48.0\ \mathrm{mS\,m^{-1}}$ at $s = 1.00\ \mathrm{m}$ and
$26.8\ \mathrm{mS\,m^{-1}}$ at $s = 2.50\ \mathrm{m}$ over the same point, under
which the same instrument reads a uniform nearby field site at
$20.0\ \mathrm{mS\,m^{-1}}$. Sketch the qualitative profile (where must the
conductor be?) and justify your answer with two weight values from the lesson.

## ★★★ Research-oriented

**★★★7.** Design a multi-spacing, multi-frequency survey to distinguish
(1) a wet, clay-rich soil with no salinity, from (2) a drier soil with saline pore
water, both of which read the same apparent conductivity at a single setting.
State the measurements, the quantity you will plot, the confounder you cannot
remove with these two methods alone, and the observables that break it — a
quantitative specification, not a wish list. Note that
$\sigma \propto \sigma_w \theta^{m}$ (an Archie-type relation, teaching form) ties
salinity and water content to one reading.

**★★★8.** The linear interpretation fails when $B$ is not small, but the
direction and size of the bias cannot be established from the LIN model itself.
Specify a numerical experiment that would measure it: the model, the solver, the
metric, and the control case. State explicitly which quantity you would report as
the bias, and what result would falsify the claim that the LIN reading
under-reports a highly conductive layer.
