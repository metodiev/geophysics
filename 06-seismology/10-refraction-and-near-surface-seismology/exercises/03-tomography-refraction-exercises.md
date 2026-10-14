# Exercises — 06-10-03 Refraction Tomography and First-Arrival Inversion

**All values are SYNTHETIC.** Attempt these before reading the
[solutions](./03-tomography-refraction-solutions.md). The lesson is
[03 Refraction Tomography and First-Arrival Inversion](../03-tomography-refraction.md).
The demonstration geometry is four sources at $0, 25, 50, 75\ \mathrm{m}$,
receivers every $2\ \mathrm{m}$ to $100\ \mathrm{m}$, an inversion grid of
$5\ \mathrm{m}$ cells to $30\ \mathrm{m}$ depth ($20 \times 6 = 120$ unknowns), a
damped LSQR update with $\lambda = 15$ and 12 iterations.

## ★ Foundational

**★1.** A first-arrival ray spends $20\ \mathrm{m}$ in a
$600\ \mathrm{m\,s^{-1}}$ cell, $15\ \mathrm{m}$ in an
$1800\ \mathrm{m\,s^{-1}}$ cell and $20\ \mathrm{m}$ in another
$600\ \mathrm{m\,s^{-1}}$ cell. Compute the travel time in seconds and
milliseconds, and state the units of $\mathbf{A}$, $\mathbf{s}$ and $\mathbf{t}$
in $\mathbf{A}\mathbf{s} = \mathbf{t}$.

**★2.** The demonstration reports that $62.5\%$ of the 120 inversion cells contain
at least one ray. How many cells have zero coverage, and what value does the damped
inversion return for them?

**★3.** The starting model is $400\ \mathrm{m\,s^{-1}} + 60\,z$ with $z$ in metres.
Tabulate its velocity in the six cell rows (centres at
$z = 0, 5, 10, 15, 20, 25\ \mathrm{m}$) and state why a vertical gradient is
necessary at all.

## ★★ Applied

**★★4.** The reference inversion's RMS residual falls from
$15.0693\ \mathrm{ms}$ at iteration 1 to $0.7208\ \mathrm{ms}$ at iteration 12,
while the Gaussian noise level in the data is $0.4473\ \mathrm{ms}$. Compute the
reduction factor and the ratio of the final residual to the noise level, and
explain the second ratio in terms of model error.

**★★5.** Using $h_{\max} = (L/2)\sqrt{(v_2-v_1)/(v_2+v_1)}$, compute the depth of
investigation of a $60\ \mathrm{m}$ spread for $v_1 = 600$,
$v_2 = 1800\ \mathrm{m\,s^{-1}}$, and state the model assumption that makes this an
estimate rather than a theorem.

**★★6.** A target lies $20\ \mathrm{m}$ deep with $v_1 = 1200$ and
$v_2 = 3600\ \mathrm{m\,s^{-1}}$. Compute the crossover and the spread that places
it at one third of the line. Repeat for $v_1 = 1000$ and
$v_2 = 3000\ \mathrm{m\,s^{-1}}$ at the same depth, and state in one sentence
what the agreement of the two answers shows.

## ★★★ Research-oriented

**★★★7.** The demonstration's inversion uses $\lambda = 15$ and a hard box
constraint $150 \le v \le 4000\ \mathrm{m\,s^{-1}}$. Explain what happens if
$\lambda = 0$ is used with the box constraint removed, why the demagnetised
(unconstrained) update drives zero-coverage cells to negative slowness, and what
the box constraint actually communicates about the model.

**★★★8.** Specify an experiment that measures the diagonal of the resolution matrix
$\mathbf{R} = (\mathbf{A}^{\mathsf T}\mathbf{A} +
\lambda\mathbf{I})^{-1}\mathbf{A}^{\mathsf T}\mathbf{A}$ for the demonstration's
grid. State the perturbation, the metric, the control, and the outcome you expect
in a well-covered and in a zero-coverage cell.
