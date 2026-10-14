# Solutions — 04-07-03 Landslides, Slope Stability and Geotechnical Geophysics

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Infinite slope with cohesion

**(a)** $\gamma z = 76$ kPa. $\cos^2 25^\circ = 0.8214$ and
$\sin25^\circ\cos25^\circ = 0.3830$, so $\sigma_n = 62.4$ kPa and
$\tau = 29.1$ kPa.

**(b)** $\tan\phi' = 0.5317$, so
$FS = (8 + 62.4\times0.5317)/29.1 = (8+33.2)/29.1 = 1.415$.

**(c)** $u = 0.35\times76 = 26.6$ kPa, so
$FS = (8 + (62.4-26.6)\times0.5317)/29.1 = 27.1/29.1 = 0.929$. The slope fails:
a 35 per cent pore-pressure ratio is enough to remove the margin, which is a
modest amount of water.

**(d)** Set the strength equal to the stress:
$u^\mathrm{crit} = \sigma_n - (\tau - c')/\tan\phi'
= 62.4 - (29.1-8)/0.5317 = 22.7$ kPa, so
$r_u^\mathrm{crit} = 22.7/76 = 0.299$. A piezometer reading above 0.299 of
$\gamma z$ is the alarm threshold for this slope.

---

## ★2 — Critical acceleration

**(a)** $FS_0 = \tan30^\circ/\tan25^\circ = 0.5774/0.4663 = 1.238$.

**(b)** Exact:
$k_h = \tan25^\circ(FS_0-1)/(1+FS_0\tan^2 25^\circ)
= 0.4663\times0.238/(1+1.238\times0.2174) = 0.1110/1.2692 = 0.0875$.
Approximation: $(FS_0-1)\tan\beta = 0.238\times0.4663 = 0.1110$. The ratio is
$0.7879$: the approximation is **27 per cent high**.

**(c)** $a_c = 0.0875 \times 9.80665 = 0.858$ m s⁻².

**(d)** Unsafe. An overestimated critical acceleration means the sliding block
starts later and slides less, so a displacement calculated with (6) is too
small — the non-conservative direction for a hazard estimate. For a screening
calculation at gentle slopes the error is small; at 25 degrees it is not.

---

## ★3 — Sliding-block displacement

**(a)** $d = 3\times0.4^2(3-1.5)/(2\times1.5) = 0.48\times0.5 = 0.240$ m.

**(b)** $d = 3\times0.2^2\times1.5/3 = 0.06$ m, a quarter of the previous value,
because $d \propto t_0^2$.

**(c)** At fixed $a_c$, $d \propto (a-a_c)$ linearly but $d \propto t_0^2$
quadratically. At fixed $a$, $d = a t_0^2(a-a_c)/(2a_c)$ is *not* a simple power
of $a_c$: it grows without bound as $a_c \to a$, and falls as $1/a_c$ for
$a_c \ll a$. The sensitivity to $a_c$ therefore depends entirely on how close
the slope is to failure, which is the subject of ★★6(d).

---

## ★4 — Refraction depth

**(a)** $z = t_i v_1v_2/(2\sqrt{v_2^2-v_1^2})
= 0.014\times500\times2400/(2\sqrt{2400^2-500^2}) = 16800/4694.8 = 3.58$ m.

**(b)** $v_1$ and $t_i$. For $v_2 \gg v_1$ the expression approaches
$z \approx t_iv_1/2$, so the refractor velocity enters only weakly: changing
$v_2$ from 2400 to 3000 m s⁻¹ moves the depth from 3.579 m to 3.550 m, a
0.8 per cent change for a 25 per cent change in $v_2$, while a 10 per cent error
in $v_1$ is a 10 per cent error in $z$.

**(c)** A 300 m s⁻¹ layer is *slower* than both its neighbours, so no first
arrival travels through it; the survey would show only the 500 m s⁻¹ direct
branch and a head-wave branch from below 8 m, and the inversion for a two-layer
model would place the "refractor" much deeper than 8 m (quantified in ★★★8).

---

## ★★5 — Running the stability section

**(a)** At $\beta = 32^\circ$ with $c' = 0$ and $u = 0$ the factor of safety is
exactly 1.0000: the general rule is $FS = \tan\phi'/\tan\beta$, so a dry
cohesionless slope fails at $\beta = \phi'$.

**(b)** The fully saturated ratio is $\gamma_w/\gamma = 9.81/18 = 0.5450$. The
critical values are 0.6962, 0.5329 and 0.3687 at 10, 15 and 20 degrees.

**(c)** Compare each critical value with 0.5450: at 15 degrees the critical
value is 0.5329, *below* saturation, so a saturated 15 degree slope fails; at 14
degrees the critical value is 0.5658, above saturation, so it stands. The
steepest whole degree that survives is therefore **14 degrees**, and the exact
threshold angle is 14.6 degrees (computed in §8 of the lesson).

**(d)** With $h = 1.5$ m of head above the slip plane in a 3 m column,
$u = 9.81\times1.5 = 14.7$ kPa and $r_u = 14.7/(18\times3) = 0.2724$. Using
(3a) with $\cos^2 20^\circ = 0.8830$ and $r_u^\mathrm{crit} = 0.3687$:

$$FS = \frac{0.8830-0.2724}{0.8830-0.3687} = 1.187 .$$

The slope is stable with a 19 per cent margin, and the critical head is
$0.3687\times54/9.81 = 2.03$ m: half a metre more water and the margin is gone.
Note that $r_u^\mathrm{crit}/r_u = 1.35$ would be the wrong comparison — the
pore pressure appears on both sides through $r_u^\mathrm{crit}$.

---

## ★★6 — Integrator, and the sensitivity to $a_c$

**(a)** The numerical and closed-form displacements agree to between
$2.86\times10^{-14}$ and $6.50\times10^{-13}$ relative, over four pulse
durations.

**(b)** The closed form (7) contains the *decelerating* phase, in which the
block continues to slide at a constant deceleration $a_c$ after the pulse has
ended. A record that stops at $t_0$ integrates only the first term and returns
exactly half the displacement (the demo shows the halved value when the
post-pulse part is truncated). The physics is in the tail.

**(c)** $d = 5\times0.3^2(5-0.86)/(2\times0.86) = 0.45\times4.14/1.72
= 1.083$ m.

**(d)** With $a_c = 1.03$ m s⁻², $d = 0.45\times3.97/2.06 = 0.865$ m: a
**20 per cent decrease** for a 20 per cent increase in $a_c$, i.e. roughly
proportional. With $a_c = 4.8$ against $a_c = 4.0$: $d$ falls from
$0.45\times1.0/8 = 0.0563$ m to $0.45\times0.2/9.6 = 0.0094$ m, an **83 per
cent decrease** for the same 20 per cent change in $a_c$. The sensitivity is
governed by the ratio $a/a_c$: far from failure the displacement is almost
linear in $a_c$, and near failure it collapses. This is why a displacement map
must carry the $a_c$ uncertainty, and why the mapping variable used in practice
is the ratio $a_c/a_\mathrm{max}$.

---

## ★★7 — Water content from a velocity

**(a)** 0.1362 m ns⁻¹ at $\theta = 0.05$ and 0.0715 m ns⁻¹ at $\theta = 0.30$,
a ratio of 1.905.

**(b)** $\mathrm{d}\theta/\mathrm{d}v = 3.866$ per m ns⁻¹, so 0.001 m ns⁻¹ of
velocity precision corresponds to **0.0039** of volumetric water content — four
parts in a thousand.

**(c)** $v = 0.090$ m ns⁻¹ gives
$\varepsilon_r = (c/v)^2 = (0.29979/0.090)^2 = 11.096$, so
$\sqrt{\varepsilon_r} = 3.331$. Then (8) gives

$$3.331 = 8.967\theta + 0.65\times2.236 + (0.35-\theta) ,$$

so $7.967\theta = 3.331 - 1.453 - 0.35 = 1.528$ and $\theta = 0.192$. Checking
forward: CRIM with $\theta = 0.192$ gives $\varepsilon_r = 11.10$ and
$v = 0.0900$ m ns⁻¹ ✓.

**(d)** Two of the several reasons: (i) the porosity $\phi$ was *assumed*, and
the same velocity with $\phi = 0.30$ gives a different $\theta$ — the model has
two unknowns and the survey measures one number; (ii) CRIM is a model, and a
clay-bearing or organic soil departs from it substantially, so the answer is a
model-dependent water content rather than a measured one. A third is that the
velocity was inverted from a travel time over a path that may not have been
uniformly wet.

---

## ★★★8 — The hidden layer

**(a)** A critically refracted head wave only exists at an interface where the
velocity *increases*. Layer 2 at 300 m s⁻¹ is slower than layer 1 at
500 m s⁻¹, so no ray can be critically refracted along its top, and any ray
entering it is bent towards the normal and cannot return to the surface as a
first arrival. The first arrivals are the direct wave in layer 1 and the head
wave along the top of layer 3.

**(b)** The two critical angles are
$\sin\theta_{13} = v_1/v_3 = 0.25$ and $\sin\theta_{23} = v_2/v_3 = 0.15$. The
intercept time is the vertical travel through both layers at those angles:

$$t_i = \frac{2z_1}{v_1\cos\theta_{13}} + \frac{2(z_3-z_1)}{v_2\cos\theta_{23}}
= \frac{6}{500\times0.9682} + \frac{10}{300\times0.9887}
= 0.01239 + 0.03372 = 0.04611\ \mathrm{s}.$$

**(c)** Inverting that intercept with the two-layer formula (9), as if the
section were layer 1 over layer 3:

$$z_\mathrm{app} = \frac{0.04611\times500\times2000}{2\sqrt{2000^2-500^2}}
= \frac{46110}{3873} = 11.91\ \mathrm{m},$$

against a true 8 m — an **overestimate of 49 per cent**. Worse, the 5 m thick
300 m s⁻¹ layer, which is the weak, water-bearing unit and the one a stability
assessment cares about, has left no trace at all in the data.

**(d)** The survey must detect the low-velocity zone rather than the first
arrival: reflection imaging from within the layer, surface-wave dispersion
(a slow layer shows as a low-velocity zone in the dispersion curve, and MASW
inversions can recover it), or a borehole measurement. All of these are more
expensive than a refraction line because they require either a source and
receiver spread optimised for reflections, a wideband recording of surface
waves and a nonlinear inversion, or drilling.

---

## ★★★9 — A rainfall threshold

**(a)** $r_u^\mathrm{crit} = \cos^2 18^\circ(1-\tan18^\circ/\tan34^\circ)
= 0.9045(1-0.3249/0.6745) = 0.469$. The fully saturated value is
$9.81/20 = 0.491$, which **exceeds** the critical value, so a fully saturated
slope fails: $FS = (0.9045-0.491)/(0.9045-0.469) = 0.95$.

**(b)** A water table 2 m below the surface leaves 4 m of head above a slip
plane at 6 m. Assuming hydrostatic conditions below the water table and no
capillary effects above it, $u = \rho_w g\times4 = 39.24$ kPa and
$r_u = 39.24/(20\times6) = 0.327$, so

$$FS = \frac{0.9045-0.327}{0.9045-0.469} = 1.33 .$$

The assumptions are: hydrostatic below the water table, no flow (so no seepage
force), a planar slip surface parallel to the ground at 6 m, uniform material,
and $c' = 0$.

**(c)** Failure at $u = r_u^\mathrm{crit}\gamma z = 0.469\times120 = 56.3$ kPa,
i.e. a head of $56.3/9.81 = 5.73$ m. With the slip plane 6 m below the surface,
the water table must rise to **0.27 m below the surface**. There is almost no
warning interval: the critical state is a saturated slope.

**(d)** Operationally, the computation gives a trigger threshold in a
measurable variable: a piezometer head (5.73 m above the slip plane) or an
equivalent rainfall accumulation from a simple infiltration model. The real
threshold will differ because (i) the pore pressure response to rainfall is not
hydrostatic and lags it, with the lag set by the permeability and the depth;
(ii) $c'$ was set to zero, and even a small cohesion raises the threshold
appreciably at a gentle 18 degree slope; and (iii) an intense storm can generate
a perched water table above the slip plane that produces a much higher local
pressure than the static profile.
