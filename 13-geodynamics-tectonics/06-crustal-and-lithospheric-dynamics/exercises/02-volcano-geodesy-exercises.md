# Exercises — 13-06-02 Volcano Deformation, Magma Chamber Models and InSAR

Attempt these before reading the
[solutions](./02-volcano-geodesy-solutions.md). The lesson is
[02 Volcano Deformation, Magma Chamber Models and InSAR](../02-volcano-geodesy.md)
and its numbers come from
[`code/volcano_geodesy_demo.py`](../code/volcano_geodesy_demo.py). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute $u_z(0) = 3\Delta V/(4\pi d^2)$ for $d = 2$ km and
$\Delta V = 5.0\times10^{5}$ m³, in centimetres.

**★2.** For the same source, compute $u_r$ and $u_z$ at $r = 4$ km and verify the
identity $u_r/u_z = r/d$.

**★3.** State the two components of the look vector that a descending orbit with
incidence $39°$ and heading $190°$ gives, and explain the sign of the east
component.

## ★★ Applied

**★★4.** A purely vertical displacement of 2 cm is measured by a satellite with
incidence $35°$. Compute the line-of-sight change, and state what fraction of the
vertical motion a single orbit misses.

**★★5.** Using the lesson's 2×2 decomposition matrix, compute the solution for
$u_U$ and $u_E$ from line-of-sight values of $+1.0$ cm (ascending) and
$+1.0$ cm (descending), and check your answer against the measured north-component
leak of 14.06%.

**★★6.** Two initial conditions produce observables differing by
$1.3\times10^{-16}$ relative while differing by 16.7% themselves. Explain what
this implies for the depth uncertainty of a Mogi inversion that has only a
single-orbit dataset.

**★★7.** The best fit for a synthetic dataset gives $d = 2.98$ km,
$\Delta V = 9.53\times10^{5}$ m³ against a truth of $d = 3.00$ km,
$\Delta V = 1.00\times10^{6}$ m³. Compute the relative errors and state whether
they are larger or smaller than the half-width of the admitted depth range.

## ★★★ Research-oriented

**★★★8.** Design an observation campaign that would resolve the vertical extent
of a magma chamber. State the observable, the required precision and the reason
surface geodesy alone is insufficient.

**★★★9.** A Mogi inversion reports $d = 4 \pm 0.2$ km with $\Delta V = 5\times10^{6}$
m³ from one interferogram. List three reasons the error bar is likely too small,
and state the diagnostic that would reveal each.

**★★★10.** The admitted depth range from two orbits is 1.43 km and from one orbit
1.82 km. Explain why the improvement is modest, and compute the condition number
of the two-orbit vertical/east–west system to justify your answer.
