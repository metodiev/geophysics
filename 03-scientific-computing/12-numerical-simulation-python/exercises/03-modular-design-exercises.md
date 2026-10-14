# Exercises — 03-12-03 Designing Reusable Model Code: Grids, Operators, Boundaries

Attempt these **closed-book** before opening the
[solutions](./03-modular-design-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first:

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/modular_design_demo.py
```

---

## ★ Foundational

**★1.** Name the four interfaces and the single question each answers.

**★2.** Give the measured orders of the four operators (centred and five-point
second derivatives, centred and forward first derivatives), and state which one
collapses at the finest grid and why.

**★3.** State the measured reflection coefficient of the rigid, naive-shift and
Reynolds boundary treatments at Courant number 0.5.

**★4.** Explain why `Grid` is declared frozen, and give the measured errors for
`dx = 0.0` and `nx = 2`.

**★5.** State the units of the Reynolds coefficient $b = (r-1)/(r+1)$ and
verify that every term of the boundary update has the units of displacement.

---

## ★★ Applied

**★★6.** Write a test that measures an operator's order against the correct
analytic derivative. Report the measured order and the grid spacing at which the
round-off floor appears.

**★★7.** Swap the flux indices in the centred second-derivative stencil and
measure (a) the error against the analytic derivative and (b) the growth rate
per step in a time-stepping run at $r = 0.5$. Compare with the predicted
$(3+\sqrt5)/2$.

**★★8.** Explain the off-by-one-in-time bug in the boundary condition: state
which two time levels a one-way condition needs, which two the buggy version
passed, and the measured reflection coefficient of each.

**★★9.** The five-point and centred operators give RMS errors of 5.44e−01 and
5.52e−01 at 8 points per wavelength, and 8.11e−01 and 8.65e−01 at 4. Explain why
the *operator's* error differs by a factor of 12 at 8 points while the
*solution's* error barely differs.

**★★10.** Recommend a change to the `Boundary.apply` signature that would have
prevented the time-level bug, and state whether you would also change the
`Operator.apply` signature for the same reason.

---

## ★★★ Research-oriented

**★★★11.** Implement a sponge (damping) boundary layer as a `Boundary` subclass
and measure its reflection coefficient as a function of layer width (10, 20, 40
cells) and damping strength. Report the width needed to beat the Reynolds
condition's 0.0012, and state the cost in extra cells.

**★★★12.** Implement a second-order absorbing condition and measure its
reflection at $r = 0.5$. Report the improvement over first order and state the
criterion you used to decide whether the extra complexity is justified.

**★★★13.** Refactor the demonstration so that the same `WaveModel1D` runs a
*heterogeneous* medium with a measured reflection coefficient against the
analytic $R = (Z_1-Z_2)/(Z_1+Z_2)$, and report the agreement. State which of the
four interfaces had to change and which did not.
