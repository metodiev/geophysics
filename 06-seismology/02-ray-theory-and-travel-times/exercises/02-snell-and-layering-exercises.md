# Exercises — 06-02-02 Snell's Law, Layered Media and the Travel-Time Curve

Attempt these before reading the
[solutions](./02-snell-and-layering-solutions.md). The lesson is
[02 Snell's Law, Layered Media and the Travel-Time Curve](../02-snell-and-layering.md).
All models are **SYNTHETIC** teaching values. Numbers marked "from the demo" are
printed by `code/snell_and_layering_demo.py`.

## ★ Foundational

**★1.** A layer of $v_1 = 5.60\ \mathrm{km\,s^{-1}}$ overlies a half space of
$v_2 = 6.20\ \mathrm{km\,s^{-1}}$. Compute the critical angle, and state whether
a head wave exists.

**★2.** With the same velocities and $h_1 = 2.00$ km, compute the intercept time
of the head-wave branch. Show each factor with its unit.

**★3.** For the same model, compute the crossover distance at which the head wave
becomes the first arrival, using both
$X = \tau_1/(v_1^{-1} - v_2^{-1})$ and
$X = 2h_1\sqrt{(v_2+v_1)/(v_2-v_1)}$, and confirm they agree.

## ★★ Applied

**★★4.** For the demonstration's stack ($h = 5, 10, 10$ km;
$v = 6.00, 6.50, 7.00\ \mathrm{km\,s^{-1}}$; half space
$8.00\ \mathrm{km\,s^{-1}}$), reconstruct interface 3 from scratch: the ray
parameter, the three ray angles, the three one-way horizontal legs, the critical
offset, and the intercept time. Compare with the demo's
$X_c = 75.3617$ km and $\tau = 4.279331$ s.

**★★5.** A synthetic stack has $v = 6.20$, then $5.80$, then
$6.80\ \mathrm{km\,s^{-1}}$, with the first two layers 4.0 km thick over a half
space. State which interfaces can produce head waves and which cannot, with the
criterion you used. For the interface that does, compute its intercept time and
critical offset.

**★★6.** A refraction branch is fitted as $T = X/6.95 + 1.55$ (with $X$ in
kilometres and $T$ in seconds). State the velocity the slope measures, and
explain why the intercept alone cannot give the thickness of the layer above.
Say what additional information you would need and why the requirement is
one-directional (each branch is inverted using velocities from shallower
branches).

## ★★★ Research-oriented

**★★★7.** The demonstration puts $\sigma_h = 0.25$ km and
$\sigma_v = 0.10\ \mathrm{km\,s^{-1}}$ on the first interface and finds a
recovered depth of $4.9869 \pm 0.6189$ km. Treat the velocity sensitivity as
$5.84$ km of depth per $\mathrm{km\,s^{-1}}$ of velocity error (measured from the
run). What velocity uncertainty and what thickness uncertainty would be needed
for a total depth error of 0.10 km? Is the thickness term or the velocity term
the binding constraint, and what does that imply for survey design?

**★★★8.** Design a refraction survey that can detect an interface at 8.0 km
depth beneath $v_1 = 5.60\ \mathrm{km\,s^{-1}}$ material, given that the
refractor has $v_2 = 6.20\ \mathrm{km\,s^{-1}}$. Specify the shortest offset at
which the interface's head wave is the first arrival, the longest offset at which
it can still be correlated across the array, and the observable that would
*contradict* its existence. State one way the design fails if the refractor is
only 1.5 km thick.
