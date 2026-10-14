# Solutions — 15-01-03 Thermohaline Circulation and Deep Water Formation

> **Read after attempting the exercises.** Several problems ask for a judgement
> as well as a number; where more than one answer is defensible it is said so.
> All arithmetic was computed.

Lesson: [03 Thermohaline Circulation](../03-thermohaline-circulation.md).

---

## ★1 — Trial value $q = 0.030$ at $F_S = 0.020$

$$T = \frac{C_T T_a}{C_T + |q|} = \frac{(1/25)(25)}{1/25 + 0.030}
= \frac{1.000}{0.070} = 14.286\ ^\circ\mathrm{C},$$

$$S = \frac{F_S}{|q|} = \frac{0.020}{0.030} = 0.6667\
\mathrm{g\,kg^{-1}},$$

$$K_Q(\alpha T - \beta S) = 30\left[1.70\times10^{-4}(14.286)
- 7.60\times10^{-4}(0.6667)\right]$$
$$= 30\left[2.4286\times10^{-3} - 5.0667\times10^{-4}\right]
= 30\left(1.9219\times10^{-3}\right) = 0.05766\ \mathrm{yr^{-1}}.$$

The right-hand side ($0.05766$) exceeds the trial $q$ ($0.030$), so
$F(q) = q - \mathrm{RHS} = -0.0277 < 0$ and **$q$ must increase** to reach a
steady state. It is nearest the **strong** branch: the two roots at this forcing
are $0.004086$ and $0.048311$, and $0.030$ lies between the saddle and the strong
node. Physically, the trial circulation is too weak to carry the freshwater away,
so $S$ has built up to $0.667\ \mathrm{g\,kg^{-1}}$ and the buoyancy difference is
suppressed ($\alpha T = 2.43\times10^{-3}$ against $\beta S = 5.07\times10^{-4}$).

---

## ★2 — The four terms

| term | meaning |
|---|---|
| $C_T(T_a - T)$ | the atmosphere relaxes the thermal contrast toward $T_a$; destroys contrast at rate $C_T$ |
| $|q|T$ | advection destroys the thermal contrast at a rate proportional to the circulation |
| $F_S$ | the *imposed* freshwater flux increases the salinity contrast |
| $|q|S$ | advection destroys the salinity contrast |
| $q = K_Q(\alpha T - \beta S)$ | the buoyancy difference drives the overturning |

The **imposed freshwater flux** $F_S$ (together with the modulus $|q|$, and the
fact that $S$ is not relaxed toward a prescribed value) is what makes more than
one equilibrium possible. If both tendencies were relaxations, the map from $q$
to the right-hand side would be monotonically decreasing and only one
intersection with the line $q$ would exist.

---

## ★3 — Units, and why $S = F_S/|q|$ diverges

$$\left[\frac{F_S}{|q|}\right]
= \frac{\mathrm{(g\,kg^{-1})\,yr^{-1}}}{\mathrm{yr^{-1}}}
= \mathrm{g\,kg^{-1}}. \ ✔$$

As $q\to0$ the circulation carries the freshwater away ever more slowly, so the
salinity difference must grow without limit to balance the same flux. The
divergence is the model's honest statement of its own limitation: a real ocean
cannot build an unbounded salinity contrast, because other processes — gyre
transport, eddy fluxes, and the flux's own dependence on the circulation — take
over. The divergence is therefore **physical within the model**, and a warning
about the model, not a numerical artefact.

---

## ★★4 — The trace identity

With $A = |q|$, $s = \operatorname{sign}(q)$, $T = C_T T_a/(C_T+A)$ and
$S = F_S/A$, the partial derivatives are

$$\frac{\partial \dot T}{\partial T} = -C_T - A - TsK_Q\alpha, \qquad
\frac{\partial \dot T}{\partial S} = +TsK_Q\beta,$$
$$\frac{\partial \dot S}{\partial T} = -SsK_Q\alpha, \qquad
\frac{\partial \dot S}{\partial S} = -A + SsK_Q\beta.$$

The trace is

$$\operatorname{tr}J = -C_T - 2A + sK_Q(\beta S - \alpha T).$$

At a steady state, $q = K_Q(\alpha T - \beta S)$, so
$\beta S - \alpha T = -q/K_Q$ and $sK_Q(\beta S - \alpha T) = -s\,q = -A$. Hence

$$\boxed{\operatorname{tr}J = -C_T - 2A - A = -C_T - 3|q| < 0 .}$$

**(a) What it forbids.** Since the trace equals the sum of the eigenvalues and is
strictly negative, there is no Hopf bifurcation: a state cannot lose stability by
a pair of eigenvalues crossing the imaginary axis with positive real part. A
state is unstable **only** if $\det J < 0$, i.e. if one eigenvalue is positive
and one negative — a saddle. The model therefore has no internal oscillation on
its way to or from equilibrium.

**(b) Numerical check.** Strong state, $q = 0.048311$:

$$-C_T - 3|q| = -0.04000 - 3(0.048311) = -0.184933,$$

against the printed eigenvalues summing to $-0.14071 - 0.04423 = -0.18494$. ✔
Weak state, $q = 0.004086$:

$$-0.04000 - 3(0.004086) = -0.052258,$$

against $-0.09648 + 0.04423 = -0.05225$. ✔ Agreement in both cases is at the
level of the printed digits, which is what a consistency identity should give.

---

## ★★5 — Thermocline scale for $w = 2\ \mathrm{m\,yr^{-1}}$

Convert the velocity: $w = 2.0/3.156\times10^{7} = 6.337\times10^{-8}\
\mathrm{m\,s^{-1}}$.

$$\delta = \frac{\kappa}{w} = \frac{1.0\times10^{-4}}{6.337\times10^{-8}}
= 1578\ \mathrm{m}.$$

**(a)** The solution is $T - T_d = (T_0-T_d)e^{-z/\delta}$, so the $1/e$ depth is
$z = \delta = 1578\ \mathrm{m}$. (Note: the *value* at that depth is
$T_d + (T_0-T_d)/e$, i.e. $36.8\,\%$ of the way from $T_0$ down to $T_d$, or
$63.2\,\%$ of the total drop completed.)

**(b)** $\mathrm{Pe} = wH/\kappa = 6.337\times10^{-8}\times4000/1.0\times10^{-4}
= 2.535$.

**(c)** A Péclet number well above 1 means advection dominates diffusion: the
thermocline is thin and the temperature is carried downward faster than it can
diffuse away, so the exponential decay length is short compared with the depth of
the basin. ($\mathrm{Pe} = H/\delta$ exactly, so with $H = 4000$ m and
$\delta = 1578$ m, $\mathrm{Pe} = 2.53$ by construction — a useful identity to
note.)

---

## ★★6 — Fixed-point iteration at $F_S = 0.010$

| iteration | $T$ ($^\circ$C) | $S$ (g kg$^{-1}$) | new $q$ (yr$^{-1}$) |
|---|---|---|---|
| 0 (guess) | – | – | 0.050000 |
| 1 | 11.111 | 0.2000 | 0.052107 |
| 2 | 10.857 | 0.1919 | 0.050995 |
| 3 | 10.990 | 0.1961 | 0.051576 |
| 4 | 10.920 | 0.1939 | 0.051271 |
| 5 | 10.956 | 0.1950 | 0.051431 |
| 6 | 10.937 | 0.1944 | 0.051347 |

The true roots at this forcing are $0.00190307$ and $0.05137565$; the iteration is
**converging to the strong branch, $0.05138$**, but slowly and with an
oscillating (overshooting) approach. The contraction factor here is close to 1 —
the derivatives of the map are almost exactly $-1$ in magnitude — so the
iteration takes many tens of steps. A dichotomy or a Newton method with a bracket
is the practical choice; the point of this exercise is that the *fast* iteration
converges to a *stable* state, which is the numerical reflection of Section 5.

---

## ★★7 — Heat transport and its inversion

$$\Psi = 18\ \mathrm{Sv} = 1.8\times10^{7}\ \mathrm{m^{3}\,s^{-1}}, \qquad
\Delta T = 12\ \mathrm{K},$$

$$Q = \rho c_p \Psi \Delta T = 1025 \times 3994 \times 1.8\times10^{7}
\times 12 = 8.843\times10^{14}\ \mathrm{W} = 0.884\ \mathrm{PW}.$$

Inverting for $\Psi$ at $\Delta T = 18$ K:

$$\Psi = \frac{Q}{\rho c_p \Delta T}
= \frac{8.843\times10^{14}}{1025 \times 3994 \times 18}
= \frac{8.843\times10^{14}}{7.369\times10^{7}}
= 1.20\times10^{7}\ \mathrm{m^{3}\,s^{-1}} = 12.0\ \mathrm{Sv}.$$

**The answer is exactly $18 \times (12/18) = 12$ Sv**, because $Q$ is held fixed
and $\Psi \propto 1/\Delta T$. That proportionality is the whole difficulty: the
data constrain the product, so a $50\,\%$ change in the assumed $\Delta T$ moves
the reported circulation by $33\,\%$ with no change in the measurement.

---

## ★★★8 — Distinguishing the two stable states

**(a) What to measure.** The two states differ most cleanly in the salinity
contrast ($4.895$ against $0.414\ \mathrm{g\,kg^{-1}}$) and in the overturning
rate ($0.004086$ against $0.048311\ \mathrm{yr^{-1}}$). Salinity is the better
target: it differs by a factor 12, it is a *state variable* rather than a rate,
and it is measurable from hydrography or from a deliberate tracer release.
Overturning is measurable by mooring arrays across a boundary or by geostrophic
shear referenced to the surface.

**(b) Duration.** One overturning period of the slow state is
$1/0.004086 = 245$ years — longer than any observing programme. The design must
therefore measure the *contrast* (a state) rather than the *transport* (a rate),
or use a transient tracer whose inventory integrates the circulation over decades.
A tracer with a half-life of tens of years (or an anthropogenic transient with a
known input history) is the only route to a rate on that timescale.

**(c) Signal to resolve.** The salinity contrast difference is
$4.895 - 0.414 = 4.48\ \mathrm{g\,kg^{-1}}$, i.e. $\sim13\,\%$ of a typical
salinity. Against modern conductivity-sensor precision this is a large signal;
the difficulty is not precision but **spatial representativeness and drift** —
two boxes' worth of difference has to be inferred from finite station coverage,
and any single sensor's calibration drift of a few thousandths of a unit over a
decade must be removed.

**(d) What the design does not test.** It does not test the size of the
freshwater forcing, the constancy of $\alpha$ and $\beta$, the two-box
idealisation of an actual basin, or the modulus assumption $|q|$. It can confirm
that two states exist; it cannot confirm that the model's threshold is the
ocean's.

---

## ★★★9 — Is the fold robust?

Re-solving the fold numerically for three values of the coupling:

| $K_Q$ (yr$^{-1}$) | fold $F_S$ ((g kg$^{-1}$) yr$^{-1}$) | $q$ at the fold (yr$^{-1}$) |
|---|---|---|
| 15 | 0.04146 | 0.016166 |
| 30 | 0.05864 | 0.024510 |
| 60 | 0.07754 | 0.035648 |

The fold **exists for all three couplings** — two steady states at weak forcing,
none beyond a finite threshold — and its position moves monotonically with
$K_Q$: the threshold grows from $0.0415$ to $0.0775$, an increase of $87\,\%$
while $K_Q$ changes by a factor 4. So the claim is supported in the sense the
lesson states it:

- the **existence** of a saddle-node and of the hysteresis that goes with it is
  structural — it follows from the shape of the map $q\mapsto$ RHS, which is
  non-monotonic for any $K_Q > 0$ with a prescribed flux;
- the **threshold value** is a function of the coefficients, moving by tens of
  per cent for a factor-4 change in one of them.

A stronger statement is also available from the table: the *ratio* $F_{S,\text{fold}}/K_Q$
is $2.76\times10^{-3}$, $1.95\times10^{-3}$ and $1.29\times10^{-3}$ — not
constant, so no simple rescaling collapses the three cases. Even the
dimensionless form of the threshold is model-dependent, which is the sharpest way
to say that this number cannot be exported to the ocean.
