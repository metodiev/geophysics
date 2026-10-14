# Exercises — 12-01-02 Crustal Structure and Continental vs Oceanic Crust

Attempt these before reading the
[solutions](./02-crustal-structure-solutions.md). The lesson is
[02 Crustal Structure and Continental vs Oceanic Crust](../02-crustal-structure.md).
All models and data are **SYNTHETIC** teaching values.

Useful relations: $T_\text{head} = x/v_2 + 2H\sqrt{v_2^2-v_1^2}/(v_1v_2)$,
$H = t_i v_1 v_2/(2\sqrt{v_2^2-v_1^2})$,
$x_c = 2Hv_1/\sqrt{v_2^2-v_1^2}$, $x_\times = t_i/(1/v_1-1/v_2)$,
$\nu = (k^2-2)/[2(k^2-1)]$ with $k=v_p/v_s$,
$r = h\rho_c/(\rho_m-\rho_c)$,
$g = \frac{4}{3}\pi G \Delta\rho\, a^3/d^2$ with
$G = 6.674\times10^{-11}$ SI, and
$\Delta t_{Ps} = H\left(\sqrt{v_s^{-2}-p^2} - \sqrt{v_p^{-2}-p^2}\right)$.

## ★ Foundational

**★1.** A SYNTHETIC two-layer crust has $v_1 = 6.20\ \mathrm{km\,s^{-1}}$,
$v_2 = 8.10\ \mathrm{km\,s^{-1}}$, $H = 32.0\ \mathrm{km}$. Compute (a) the
intercept time $t_i$, (b) the critical distance $x_c$, (c) the crossover distance
$x_\times$, and (d) the thickness you would report if the picked intercept were
6.90 s while the velocities were correct.

**★2.** Compute Poisson's ratio for $k = v_p/v_s = 1.70$, 1.73 and 1.80. Then
evaluate $\Delta\nu$ produced by a 1 % error in $k$ at $k = 1.73$, and state
whether $\nu$ is a sensitive or a blunt discriminator.

**★3.** A SYNTHETIC three-layer column is 1.5 km of sediment
($v_p = 2.50$), 14.0 km of upper crust ($v_p = 6.00$) and 16.0 km of lower crust
($v_p = 6.70\ \mathrm{km\,s^{-1}}$). Compute the total vertical travel time, the
harmonic-mean velocity, and the depth you would report by converting the time
with $v_p = 6.00\ \mathrm{km\,s^{-1}}$. Report the depth error.

## ★★ Applied

**★★4.** A refraction experiment yields an intercept time with a standard error
of 30 ms at fixed velocities $v_1 = 6.20$ and $v_2 = 8.10\ \mathrm{km\,s^{-1}}$.
Propagate that to a depth uncertainty by hand. Compare your answer with the
$0.201\ \mathrm{km}$ scatter of the lesson's 300-survey Monte Carlo and explain
the difference.

**★★5.** Using $\rho_c = 2.85$, $\rho_m = 3.32\ \mathrm{g\,cm^{-3}}$ and a
reference crustal thickness of 30 km, compute (a) the root beneath a 2 km high
plateau and the total crustal thickness there, and (b) the crustal thickness
beneath an ocean basin of depth 3.5 km (water density
$1.03\ \mathrm{g\,cm^{-3}}$).

**★★6.** A residual gravity anomaly of 20 mGal is fitted by a buried sphere of
radius 4 km at 8 km depth. (a) Compute the required density contrast. (b) What
density contrast would the *same-size* sphere need at 16 km depth? (c) Now keep
instead the ratio $a/d$ fixed (so the body grows with depth) and recompute.
Explain in one sentence why the gravity data alone cannot choose between (a) and
its part-(c) counterpart, and say which of the two is physically admissible.

**★★7.** A receiver function gives a Ps delay of 3.888 s at
$p = 0.060\ \mathrm{s\,km^{-1}}$ for a structure with
$v_p = 6.20\ \mathrm{km\,s^{-1}}$ and $v_s = 3.60\ \mathrm{km\,s^{-1}}$. Invert
for $H$, then repeat with $k$ assumed to be 1.65 and 1.78 and report both depths.
Which of the two assumptions biases the depth in the same direction as the
refraction bias produced by a velocity that is too fast?

## ★★★ Research-oriented

**★★★8.** Show analytically that the head-wave travel-time curve cannot separate
$H$ from $v_1$: derive $\delta H/\delta v_1$ at fixed $t_i$ and evaluate it for
the ★1 model. Then state, with a number, how much of the depth ambiguity remains
after adding a 5 km deep borehole that measures $v_1$ directly.

**★★★9.** Design a field survey that would measure a Moho depth to better than
2 % *without* assuming a velocity. State the acquisition geometry, the
forward model you would fit, the parameter you expect to be well determined, and
the parameter you expect to trade off, with a quantitative prediction.

**★★★10.** A gravity profile is measured over a buried body and is fit equally
well by a sphere at 5 km and a sphere at 15 km. Propose the measurement that
would resolve the ambiguity, derive how the discriminating signal scales with
depth (state the power of $d$), and estimate the factor by which that signal is
smaller at 15 km than at 5 km.
