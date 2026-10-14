# Exercises — 02-02-01 Kinematics in One and Two Dimensions

Attempt these **closed-book** before opening the
[solutions](01-kinematics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Unless stated otherwise use $g = GM_\oplus/R^{2}$ with $R = 6\,371$ km and the
defining $GM_\oplus = 3.986\,004\,418\times10^{14}\ \mathrm{m^3\,s^{-2}}$, so
$g = 9.82025\ \mathrm{m\,s^{-2}}$. Take
$1\ \mathrm{yr} = 3.1557\times10^{7}$ s. State a regime of validity with every
numerical answer in ★★ and ★★★.

---

## ★ Foundational

**★1.** Differentiate and integrate: given $a(t) = a_0$ (constant) and
$x(0) = x_0$, $v(0) = v_0$, derive $v(t)$ and $x(t)$, then eliminate $t$ to obtain
$v^{2} = v_0^{2}+2a(x-x_0)$. State which step requires constant $a$.

---

**★2.** A body is dropped from rest from $h = 10$, 100, 400 and 1000 m.
Compute the fall time and the impact speed for each, and say at which height the
constant-$g$ assumption has an error above 0.01%, using the vertical gradient
$2GM/R^{3}$.

---

**★3.** A projectile is launched at 25 m/s at 30°, 45° and 60° on level ground.
Compute the range and apex height for each. Why do 30° and 60° give the same
range, and which angle gives the higher apex?

---

**★4.** Convert: (a) 7 cm/yr to mm/yr and to m/s; (b) 5 km/s to mm/yr;
(c) 1 mGal to m/s². Which of these numbers is a *rate of motion of ground* and
which is a *property of rock*?

---

## ★★ Applied

**★★5.** A projectile is fired horizontally at 1000 m/s from a 100 m tower.
(a) How long is it in the air, and how far does it travel? (b) By how much has
the Earth's surface curved away at that range (use $x^{2}/2R$)? (c) Is the
flat-Earth answer acceptable at that range? State the criterion you use.

---

**★★6.** For quadratic drag with $\dot v = -g - cv^{2}$, compute the speed at
which drag equals gravity for $c = 10^{-3}$ and $2\times10^{-3}\ \mathrm{m^{-1}}$,
and state the *speed regime* in which a vacuum ballistic calculation is adequate
for each.

---

**★★7.** A GNSS station is observed daily for 365 days with white position noise
of $\sigma = 1$ cm. (a) Compute the uncertainty of a fitted linear rate using
$\sigma_v = \sigma\sqrt{12/[n(n^{2}-1)\Delta t^{2}]}$ with
$\Delta t = 1$ day. (b) Repeat for 2 and 3 years. (c) A tectonic signal of
2 mm/yr: how many years of data are needed for a 2σ detection? (d) State the
assumption that makes this formula this simple, and what a real network does to
it.

---

**★★8.** A 50 kg instrument is dropped down a 400 m borehole. (a) Compute the
vacuum fall time and the impact speed. (b) With quadratic drag
$c = 2\times10^{-3}\ \mathrm{m^{-1}}$, by how much does the fall time increase?
(You may quote the module's demonstration value if you state that you are doing
so.) (c) Which of the two answers should the field crew use for the logging
speed, and why?

---

## ★★★ Research-oriented

**★★★9.** Design a drop-calibration experiment to measure the drag coefficient
$c$ of a falling probe, given a 400 m borehole, a timing precision of 1 ms, and
the ability to vary the probe's mass and cross-section.

(a) Write the equation of motion and identify the two dimensionless groups
(specific gravity and a drag parameter).
(b) State what must be measured to determine $c$, and the expected precision.
(c) Explain how the *sign* of the timing difference relative to the vacuum time
distinguishes $c$ from a systematic timing offset.

---

**★★★10.** A noisy position series $x(t)$ with white noise of standard deviation
$\sigma$ sampled at interval $\Delta t$ is differentiated by a simple two-point
difference, $\dot x \approx (x_{i+1}-x_i)/\Delta t$.

(a) Show that the noise in the derivative has standard deviation
$\sqrt2\,\sigma/\Delta t$.
(b) Compute that for $\sigma = 1$ cm and $\Delta t = 1$ day and for
$\Delta t = 30$ days, in mm/yr.
(c) Explain why this is worse than the fitted-slope estimator of ★★7 by a large
factor, and what that factor is.
(d) State one geophysical situation in which the two-point difference is
nevertheless the right tool.
