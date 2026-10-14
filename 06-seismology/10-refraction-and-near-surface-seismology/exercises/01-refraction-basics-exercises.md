# Exercises — 06-10-01 Refraction Survey Geometry and Travel-Time Interpretation

**All values are SYNTHETIC.** Attempt these before reading the
[solutions](./01-refraction-basics-solutions.md). The lesson is
[01 Refraction Survey Geometry and Travel-Time Interpretation](../01-refraction-basics.md).

## ★ Foundational

**★1.** For $v_1 = 800\ \mathrm{m\,s^{-1}}$ and
$v_2 = 2400\ \mathrm{m\,s^{-1}}$, compute $\sin i_c$, $i_c$ in degrees and
radians, $\cos i_c$, and the ray parameter $p$ of the critically refracted ray.
State the unit of $p$.

**★2.** With the velocities of ★1 and a refractor at $h = 15\ \mathrm{m}$,
compute the intercept time $t_i$ and the crossover distance $x_c$, with units.

**★3.** Verify numerically that
$t_i = 2h\cos i_c/v_1$ and $t_i = 2h\sqrt{v_2^{2}-v_1^{2}}/(v_1 v_2)$ give the same
value for ★2, and explain in one sentence why they must.

## ★★ Applied

**★★4.** A three-layer SYNTHETIC site has $1000\ \mathrm{m\,s^{-1}}$ to $6\
\mathrm{m}$, $400\ \mathrm{m\,s^{-1}}$ from $6$ to $11\ \mathrm{m}$, and
$2500\ \mathrm{m\,s^{-1}}$ below. Compute the exact intercept time of the
first-arrival curve and the depth obtained by interpreting that curve as two
layers ($1000$ over $2500\ \mathrm{m\,s^{-1}}$). State the depth error in metres
and as a percentage of the true depth to the $2500\ \mathrm{m\,s^{-1}}$ layer.

**★★5.** The demonstration's eikonal solver plateaus at a maximum difference of
$0.0275\ \mathrm{ms}$ for both 48 and 96 directions, and falls to
$0.0104\ \mathrm{ms}$ at 144 directions. Explain the plateau and the drop in terms
of which ray directions are available, and state the parameter that must be
refined.

**★★6.** A spread of $20\ \mathrm{m}$ is shot over the demonstration's model
($v_1 = 500$, $v_2 = 1800\ \mathrm{m\,s^{-1}}$, $h = 10\ \mathrm{m}$). Is the
refractor seen? Repeat for $h = 6\ \mathrm{m}$, and state what the far branch of
that second survey constrains.

## ★★★ Research-oriented

**★★★7.** Design a refraction survey for a $25\ \mathrm{m}$ deep target with
$v_1 = 900\ \mathrm{m\,s^{-1}}$ and $v_2 = 2700\ \mathrm{m\,s^{-1}}$. Give the
crossover distance, the spread length with the crossover at one third of the line,
the receiver spacing you would choose, and the two checks you would run on the
result before reporting a depth.

**★★★8.** Specify a synthetic experiment that would demonstrate, with a single
number, that a perfect two-layer fit does not imply a two-layer site. State the
forward model, the metric, the control case, and the outcome you expect.
