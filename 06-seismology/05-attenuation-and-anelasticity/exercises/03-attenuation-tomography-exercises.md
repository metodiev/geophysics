# Exercises — 06-05-03 Attenuation Tomography and Temperature Interpretation

Attempt these before reading the
[solutions](./03-attenuation-tomography-solutions.md). The lesson is
[03 Attenuation Tomography and Temperature Interpretation](../03-attenuation-tomography.md).
All models are **SYNTHETIC** teaching values. Use
$R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$.

## ★ Foundational

**★1.** A $t^{*}$ is fitted from a spectral decay over $[1, 10]\ \mathrm{Hz}$
with 32 samples and white noise $\sigma = 0.02$ in $\ln A$. Compute
$\sigma_m$, then $\sigma_{t^{*}}/t^{*}$. State which quantity in the problem sets
the precision.

**★2.** A ray with a $40\ \mathrm{s}$ travel time gives $t^{*} = 0.80\
\mathrm{s}$. Compute the path-averaged $Q$ and state the units of $t^{*}$ and of
the ray-kernel element $G = \int \mathrm{d}l/v$ over a cell.

**★3.** Write the Jacobian entries for a joint inversion of $1/Q$ per cell plus
one amplitude term per event, and check the units of each entry against the units
of the data.

## ★★ Applied

**★★4.** A damped inversion is run for five values of $\lambda$ and the
following results are obtained (SYNTHETIC): the rms misfit is 0.0199, 0.0199,
0.0199, 0.0210, 0.0450 and the rms model error is $5.1\times10^{-3}$,
$2.5\times10^{-3}$, $2.4\times10^{-3}$, $2.6\times10^{-3}$, $8.9\times10^{-3}$
for $\lambda = 10^{-8}, 10^{-7}, 10^{-6}, 10^{-5}, 10^{-4}$. The data noise level
is $\sigma = 0.02$. **(a)** Which $\lambda$ does the discrepancy principle
select, and why? **(b)** Why does the misfit rise for $\lambda \ge 10^{-5}$?
**(c)** State in one sentence what the model error would look like if the noise
level were halved.

**★★5.** A joint inversion has 30 model parameters (25 cells plus 5 event
amplitudes) and a numerical rank of 22 at a relative threshold of $10^{-3}$.
**(a)** How many exact null directions exist at that threshold? **(b)** Explain
why none of them can have a non-zero amplitude component. **(c)** The largest
exact null vector changes the rms $1/Q$ field by $1.0\times10^{-3}\
\mathrm{s^{-1}}$ while changing the data by a relative $7\times10^{-17}$; write
one sentence that could go into a paper reporting the $1/Q$ value of a single
cell, and one that could not.

**★★6.** For $H^{*} = 250\ \mathrm{kJ\,mol^{-1}}$ and $T = 1200\ \mathrm{K}$:
**(a)** compute $\mathrm{d}\ln\tau/\mathrm{d}T$; **(b)** compute the temperature
change that corresponds to a factor of 4 in relaxation time; **(c)** compute how
much the answer in (b) changes if $H^{*}$ is uncertain by $\pm 15\%$.

## ★★★ Research-oriented

**★★★7.** Design a synthetic recovery test for an attenuation-tomography
inversion that would expose the null space rather than hide it. Specify: the
input model, the ray geometry, the noise level, the inversion settings, the
diagnostics you will report, and the criterion you will use to decide that a
recovered feature is resolvable. Explain what a *failed* test looks like and how
you would change the design rather than the answer.

**★★★8.** A study wants to hold $1/Q$ within $5\%$ of a target over two decades
of frequency. **(a)** Using the demonstration's flatness-versus-$N$ table
($N = 4$: $19.08\%$ central-decade deviation; $N = 6$: $1.77\%$; $N = 8$:
$0.17\%$), state how many relaxations are needed and why the table itself cannot
answer the question without an interpolation assumption. **(b)** State the
modelling cost per relaxation per grid point per time step and explain why that
cost, not accuracy, is the binding constraint in production viscoacoustic codes.
**(c)** The measured $Q$ at $0.001\ \mathrm{Hz}$ is $521.776$ for a target of
$100$. Convert that band-edge value into an implied temperature error using
$\mathrm{d}\ln\tau/\mathrm{d}T = 3.61\times10^{-2}\ \mathrm{K^{-1}}$ and comment.
