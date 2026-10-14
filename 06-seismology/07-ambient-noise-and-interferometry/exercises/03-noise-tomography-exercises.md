# Exercises — 06-07-03 Ambient-Noise Tomography and Monitoring

Attempt these before reading the
[solutions](./03-noise-tomography-solutions.md). The lesson is
[03 Ambient-Noise Tomography and Monitoring](../03-noise-tomography.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** The demonstration's tomographic grid is $6\times6$ cells of
$20\ \mathrm{km}$ covering a $120\ \mathrm{km}$ box. A straight ray runs from
the corner $(0,0)$ to the opposite corner $(120,120)$. Compute its length and
the length of its segment inside each cell it crosses, then write the row of the
matrix $\mathbf{G}$ that corresponds to it.

**★2.** For a station pair with $d = 60\ \mathrm{km}$, $T = 20\ \mathrm{s}$ and
$c = 2.2500\ \mathrm{km\,s^{-1}}$ (the lesson's table), compute the phase
$2\pi f d/c$ and verify the phase-velocity formula against the table.

**★3.** Compute the largest frequency step that avoids a $2\pi$ phase ambiguity
for $c = 3.00\ \mathrm{km\,s^{-1}}$ and $d = 80\ \mathrm{km}$, and compare with
the demonstration's step of $3.8\times10^{-4}\ \mathrm{Hz}$.

## ★★ Applied

**★★4.** In the damping table, the rms misfit is $7.76\times10^{-4}$ at
$\lambda = 0.003$ and $2.47\times10^{-3}$ at $\lambda = 1.0$, while the input
data noise is $0.1\%$ relative slowness. Compute the misfit-to-noise ratio at
both dampings and state what each value says about the fit and about the bias.

**★★5.** Verify the group velocity of the $T = 30\ \mathrm{s}$ row from
$c = 2.6046\ \mathrm{km\,s^{-1}}$ and $dc/dT = 0.04430\
\mathrm{km\,s^{-1}\,s^{-1}}$, and compute the group-minus-phase difference as a
percentage.

**★★6.** The checkerboard recovery has a norm ratio of $0.935$. A later study of
a region with a true anomaly of $3.0\%$ reports $2.5\%$. Assuming the same
resolution, is the reported amplitude consistent with a $3.0\%$ true anomaly?
Justify numerically.

## ★★★ Research-oriented

**★★★7.** Four cells in the demonstration's grid are crossed by no ray. Specify
a deployment change that would bring them into the resolved part of the model,
quantify the benefit you expect, and state the cost. Include the diagnostic you
would compute before and after.

**★★★8.** A monitoring study uses the inversion of this lesson at monthly
epochs. Specify the error budget item by item, giving for each item whether it
is reduced, amplified or unchanged by the tomographic inversion, and design the
single measurement that would most reduce the total error.
