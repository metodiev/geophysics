# Solutions — 13-05-03 Benchmarking Geodynamic Codes

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Benchmarking Geodynamic Codes](../03-benchmarking-geodynamics.md).

---

## ★1 — Verification versus validation

**Verification:** does the code solve the stated equations correctly? Example:
reproduce the analytic critical Rayleigh number $8\pi^4 = 779.27$ by extrapolating
the growth rate of the first mode, and show the error shrinking with refinement.

**Validation:** do the stated equations describe the Earth? Example: predict the
present-day surface heat flux of a specific region from a convection model and
compare with measurements *while* stating which observation discriminates between
two models that fit the data equally well. Note that a validation exercise needs
observations; in this synthetic curriculum only the shape of the argument can be
supplied.

---

## ★2 — Observed order

$$p = \frac{\ln\left|\dfrac{F_1-F_2}{F_2-F_3}\right|}{\ln(h_1/h_2)}
= \frac{\ln\left|\dfrac{5.31066-4.97829}{4.97829-4.90191}\right|}{\ln(0.058824/0.030303)}
= \frac{\ln(4.3399)}{\ln(1.941)} = \frac{1.4678}{0.6634} = 2.212 .$$

It may be noise because (i) $h_1/h_2 \ne h_2/h_3$ (1.941 against 1.485), so the
formula's assumption of a uniform refinement ratio is violated and the value is
only indicative; and (ii) with three solutions any curvature in $F(h)$ enters the
estimate. The formal order is 2, and 2.212 is consistent with it within the
expected scatter.

---

## ★3 — Richardson extrapolation and GCI

$$r = h_2/h_3 = 0.030303/0.020408 = 1.4850 .$$

$$F_0 = F_3 + \frac{F_3-F_2}{r^p-1}
= 4.90191 + \frac{4.90191-4.97829}{1.4850^{2.212}-1}
= 4.90191 + \frac{-0.07638}{2.3983-1}
= 4.90191 - 0.05461 = 4.84730 .$$

$$\mathrm{GCI} = 1.25\frac{|F_3-F_2|/F_3}{r^p-1}
= 1.25\frac{0.07638/4.90191}{1.3983}
= 1.25\frac{0.015582}{1.3983} = 0.013928 \approx 1.39\% .$$

The demonstration reports $F_0 = 4.84745$ and GCI $= 1.389\%$; the small
differences come from using the two finest grids only and from rounding in the
values above.

---

## ★4 — Grid error for a result at $N = 32$

Using the $N=24$ and $N=48$ values with an $O(h^2)$ model:

$$c = \frac{5.0799-4.9015}{0.0400^2-0.020408^2} = 150.7, \qquad
Nu_0 = 4.9015-150.7\times0.020408^2 = 4.8387,$$

so the $N=32$ value 4.9788 is $|4.9788-4.8387|/4.8387 = 2.90\%$ above the
extrapolated value. **Assumptions:** a single smooth $O(h^2)$ error term, and no
advection-scheme or diagnostic-definition error included in the comparison. The
lesson measures the scheme difference as 4.2%, so the second assumption is
significant.

---

## ★5 — Definition difference and comparison with the budget

$$\frac{|4.90191-4.63216|}{4.90191} = \frac{0.26975}{4.90191} = 5.503\% .$$

This exceeds the grid error (1.558% at $N=32$ from $N=48$) and the stopping error
(0.000% between tolerances $10^{-5}$ and $10^{-6}$), and it is comparable with the
8.338% at $N=16$. So the definition of the diagnostic is the largest single
contribution to the uncertainty of a number called "the Nusselt number", which is
why the definition must be quoted with it.

---

## ★6 — A benchmark that tests the interior

A good additional quantity: the horizontally averaged temperature profile
$T(z)$ at, say, 10 equally spaced heights, compared with an independent
computation by a stated norm. The lesson measures the $N=32$ and $N=48$ profiles
differing by 0.938% rms and 4.532% maximum while their $Nu$ values differ by
1.558% — so a "0.5% on $Nu$" claim says nothing about the field.

**Why $Nu$ is weak.** It is a single integral of the bottom flux; errors of
opposite sign cancel in it, and two codes can agree on the integral while
distributing the heat differently inside the domain. The interior field is what a
seismic-velocity conversion, a geoid interpretation or a metamorphic assemblage
reads, so a benchmark that does not constrain it verifies the least informative
part of the model.

---

## ★7 — Errors against the analytic value

$$779.27 \to \begin{cases}
N=24: & (813.65-779.27)/779.27 = +4.41\%,\\
N=40: & (799.39-779.27)/779.27 = +2.58\%,\\
N=64: & (791.69-779.27)/779.27 = +1.59\%.
\end{cases}$$

The sequence is monotone toward zero, which is what a consistent discretisation
must do. A **non-monotonic** sequence — say $+1.6\%$, $+4.4\%$, $+2.6\%$ — would
indicate that the measured quantity is not in its asymptotic regime, that two
competing error terms are of comparable size, or that the refinement is not
actually refining the feature (a boundary layer, or a mode whose wavelength is
set by the box rather than the grid). It would not by itself prove a bug, but it
would remove the sequence's value as verification evidence.

---

## ★8 — Time-dependent or unstable?

**Additional diagnostics.** (i) the kinetic energy and the Nusselt number on a
much finer time sampling, to see whether the variation is periodic, quasi-periodic
or chaotic; (ii) the maximum cell Péclet number and the CFL number actually used;
(iii) a run at a smaller time step with the same spatial grid — a *physical*
oscillation is unchanged by $\Delta t$, while a numerical instability changes,
grows, or disappears; (iv) a run at higher spatial resolution — a physical
oscillation converges, an instability usually grows faster; (v) the mesh-Péclet
diagnostic for the advection scheme: at $Ra = 10^{4}$ with $|u|\sim40$ and
$h = 0.030$, $Pe_h$ for a unit diffusivity is $40\times0.030/1 = 1.2$, close to
the monotonicity threshold of 2, so a scheme-dependent instability is plausible;
and (vi) the run's own error output.

**Decision rule.** If the amplitude of the variation is stable under
$\Delta t \to \Delta t/2$ and converges under refinement, and the spectrum is
narrow-band, call it physical and report a time average with its variability.
If the variation is suppressed by a smaller time step, changes amplitude under
refinement, or is dominated by grid-scale wavenumbers, it is numerical.
The measured upwind series wanders by a factor of three with no discernible
period; the decisive test would be the $\Delta t$ and refinement pair above,
which the demonstration does not run — and saying so is part of the answer.

---

## ★9 — A non-circular two-code comparison

**Quantities.** (i) the solution of a problem with an *analytic* target, so that
both codes are compared to something external (the critical Rayleigh number, or
a manufactured solution); (ii) then the interior fields — mean temperature
profile, boundary-layer thickness, rms velocity — on the *same grid*; (iii) the
integrated $Nu$.

**Tolerance.** Set from the code's own grid error, not chosen as a round number:
run each code at three resolutions and quote the GCI, then require that the
cross-code difference be smaller than the sum of the two GCIs.

**Why it is not circular.** The comparison is anchored to an analytic target
first, so the shared discretisation cannot hide the common error; and the
comparison of *derived* quantities (a boundary-layer thickness) that neither code
computes as a primary variable tests whether the two converge to the same
solution rather than the same discretisation.

---

## ★10 — A publishable uncertainty statement

> We report $Nu = 4.90$ for steady constant-viscosity free-slip convection in a
> unit-aspect box at $Ra = 10^{4}$, evaluated from the bottom heat flux. The
> numerical error is estimated from three grids (16, 32, 48 nodes per side:
> $Nu = 5.31066, 4.97829, 4.90191$), giving an observed order of 2.217, a
> Richardson limit of $Nu = 4.8475$ and a Grid Convergence Index of 1.39% with a
> safety factor of 1.25. The diagnostic definition changes the number by 5.5%
> (volume-average $Nu = 4.63216$), which we therefore quote as the dominant
> uncertainty: $Nu = 4.90 \pm 0.07$ (definition) $\pm 0.07$ (grid). Advection is
> by centred differences; a first-order upwind scheme changes $Nu$ by 4.2% at the
> same grid, so the scheme is a further contribution of that size. The stopping
> tolerance contributes less than 0.001% and is excluded.

**Excluded, with justification:** the model's physical correctness (independent
of the numerics); the choice $\eta = $ constant (a model assumption, tested
separately); time-dependent behaviour (the run's $Nu$ was monitored over
$10^{3}$ steps and varied by less than $10^{-4}$). **Included but not quantified
here:** the box aspect ratio's effect on the planform, which would require a
second geometry and is left to the discussion.
