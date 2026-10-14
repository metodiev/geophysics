# Solutions — 11-06-02 Geophysics for Tunnels, Dams and Foundations

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [02 Geophysics for Tunnels, Dams and Foundations](../02-tunnelling-and-dams.md).

---

## ★1 — Refraction depth sensitivity

$$ \theta_c = \arcsin(1200/3500) = 20.05^\circ, \qquad
\cos\theta_c = 0.93939, $$
$$ \frac{\partial z}{\partial t_i} = \frac{v_1}{2\cos\theta_c}
= \frac{1200}{1.8788} = 638.7\ \mathrm{m\,s^{-1}}. $$

A $2\ \mathrm{ms}$ pick error is therefore a
$638.7 \times 2\times10^{-3} = 1.28\ \mathrm{m}$ depth error. On this geometry
the depth is only as good as the picking, before any velocity uncertainty.

---

## ★2 — Thin low-velocity zone

$$ \Delta t = 2h\left(\frac{1}{v_{\text{slow}}}
- \frac{1}{v_{\text{fast}}}\right)
= 8\left(\frac{1}{1800}-\frac{1}{3500}\right)
= 8(5.556\times10^{-4}-2.857\times10^{-4}) = 8(2.699\times10^{-4}), $$
$$ \Delta t = 2.16\times10^{-3}\ \mathrm{s} = 2.16\ \mathrm{ms}. $$

This exceeds a $1\ \mathrm{ms}$ picking error, so the zone is **detectable**. But
the delay fixes only the product $h(1/v_{\text{slow}} - 1/v_{\text{fast}})$: a
$1.5\ \mathrm{m}$ zone at $1500\ \mathrm{m\,s^{-1}}$ gives the same delay, and the
two cannot be separated from first arrivals alone. Detection, not resolution.

---

## ★3 — Self-potential directly above a current pair

$$ V(0) = \frac{I\rho}{2\pi}\left(\frac{1}{d_1}-\frac{1}{d_2}\right)
= \frac{(20\times10^{-3})(150)}{2\pi}\left(\frac{1}{8}-\frac{1}{24}\right), $$
$$ = 0.4775 \times 0.08333 = 0.03979\ \mathrm{V} = 39.8\ \mathrm{mV}. $$

Units: $[I\rho] = \mathrm{A}\,\Omega\,\mathrm{m} = \mathrm{V\,m}$, divided by a
length gives volts. ✔

---

## ★4 — Temperature profile

$$ T(z) = 9 + 12\,\frac{e^{\mathrm{Pe}\,z/12}-1}{e^{\mathrm{Pe}}-1},
\qquad z = 4\ \mathrm{m}, $$

| $\mathrm{Pe}$ | $T(4\ \mathrm{m})$ (°C) | departure from 13.0 °C |
|---|---|---|
| 0 | 13.00 | 0.00 |
| 2 | 10.78 | $-2.22$ |
| 10 | 9.01 | $-3.99$ |

**(Note for ★4.** For $\mathrm{Pe} = 0$ the exponential form is indeterminate;
evaluate the limit, which is the linear conductive profile
$T = T_{\text{top}} + (T_{\text{bot}}-T_{\text{top}})z/L$.) The departure grows
with the Péclet number and saturates near the top temperature as
$\mathrm{Pe} \to \infty$: advection pins the logged interval to the boundary
temperature.

---

## ★5 — Look-ahead range and its scaling

$$ A(d) > 3\sigma \;\Longrightarrow\;
\frac{1}{1+(d/d_0)^{2}} > 3\sigma/A_0
\;\Longrightarrow\;
d = d_0\sqrt{\frac{A_0}{3\sigma}-1}. $$

With $d_0 = 20\ \mathrm{m}$:

| $\sigma/A_0$ | range |
|---|---|
| 0.04 | $20\sqrt{8.333-1} = 20(2.708) = 54.2\ \mathrm{m}$ |
| 0.12 | $20\sqrt{2.778-1} = 20(1.333) = 26.7\ \mathrm{m}$ |

A threefold lower noise gives about twice the range, not three times: the range
scales as $\sqrt{A_0/\sigma}$ (with the $-1$ offset). Improving the signal by
better coupling is usually cheaper than improving the noise floor by the same
factor.

---

## ★6 — SP geometry and current

The half-width scales with the source depth: from the lesson's calibration
(23.8 m half-width for sources at 10 and 30 m), a 15 m half-width corresponds to
sources roughly $15/2.4 \approx 6.3\ \mathrm{m}$ and $19\ \mathrm{m}$ deep (same
20 m separation).

For the current, the amplitude scales linearly with $I$ and with $\rho$. Using
the lesson's $10\ \mathrm{mA}$ giving $10.61\ \mathrm{mV}$ at
$\rho = 100\ \Omega\,\mathrm{m}$:

$$ I = 10\ \mathrm{mA}
\times \frac{18\ \mathrm{mV}}{10.61\ \mathrm{mV}}
\times \frac{100\ \Omega\,\mathrm{m}}{80\ \Omega\,\mathrm{m}} = 21.2\
\mathrm{mA}. $$

**Caveat.** The half-width-to-depth calibration is a stated teaching
relationship, not a physical law; a real interpretation must fit the whole
profile (both lobes, if horizontal) to the source geometry, and the coupling
coefficient must be measured if the current is to be converted into a flow rate.

---

## ★7 — Internal-erosion monitoring plan (specification)

| Observable | What it measures | Resolution / detection limit | False-negative mode |
|---|---|---|---|
| Self-potential | Electrokinetic current from seepage | $\sim1$ mV with non-polarising electrodes | Low coupling coefficient; masking by telluric noise; the sign of the anomaly can reverse with the reservoir cycle |
| Temperature (fibre-optic or log) | Advective heat transport | $\sim0.5$ K departure from the conductive profile | Slow seepage below $\mathrm{Pe}\sim1$; seasonal transients; a single log cannot distinguish steady from transient |
| Resistivity (ERT/cross-borehole) | Salinity and porosity change | A few per cent change in $\rho_a$ with time-lapse differencing | A localised leak across a short interval is averaged into a large cell; electrode drift mimics change |
| Time-lapse microgravity (chosen addition) | Mass change from internal erosion or void growth | A few $\mu$Gal over months-to-years | Slow, diffuse mass loss below the noise; regional hydrology and groundwater abstraction must be modelled out |

**Distinguishing real change from seasonal and operational noise.** Repeat each
measurement on a fixed schedule including the same season in consecutive years,
and difference *against the reservoir level*: a real seepage signature scales with
the head, a seasonal artefact scales with temperature and rainfall. Any observable
that does not co-vary with head should be treated as suspect.

**False-negative mode.** All four measure *fluid or mass*, and all four are weak
for a diffuse, low-gradient leak in low-coupling rock. The plan therefore pairs
them with periodic **direct** observation — piezometers and turbidity — because
the geophysics reduces the search space rather than certifying the dam.

---

## ★8 — Decision rule after a look-ahead detection

**What the survey has established.** A low-velocity zone about 2 m thick exists
roughly 20 m ahead of the face (with the depth uncertainty of Section 3.2).

**What it has not established.** Whether the zone is water-bearing; its
permeability; its orientation; whether it intersects the tunnel axis as a
thin band or a wide, dilated fault zone.

**Decision model.** Let $p$ be the probability that the zone would produce an
inflow severe enough to endanger the face (say a cost $C_{\text{inflow}}$),
$C_{\text{probe}}$ the cost of a probe hole (with its own small risk of
triggering the inflow it is trying to find), and $C_{\text{grout}}$ the cost of
pre-grouting. Two actions:

- **Probe first.** Cost $= C_{\text{probe}} + p\,C_{\text{inflow}}$.
- **Continue without probing.** Cost $= p\,C_{\text{inflow}}$ — but with the
  additional *unhedged* risk that if the inflow occurs, the mitigating action
  cannot be staged in advance, so the effective cost is $k\,C_{\text{inflow}}$
  with $k > 1$.

Probing is justified when

$$ C_{\text{probe}} < p(k-1)C_{\text{inflow}}. $$

For example, with $C_{\text{probe}} = 0.05\,C_{\text{inflow}}$ and
$k = 3$: probing pays when $p > 0.05/2 = 0.025$, i.e. above a 2.5% chance of a
serious inflow. A 2.5% threshold is far below any reasonable prior for a
water-bearing low-velocity zone 20 m ahead of a face, which is why a detection
triggers probing essentially always.

**The rule, written before the survey.** "Any velocity or resistivity anomaly
within 25 m of the face, exceeding the detection threshold by $3\sigma$, triggers
probe drilling before the next advance." Stating it in advance is what prevents a
detection from being rationalised away on the day.

---

## Worked mastery checkpoint

**(a) Refraction sensitivity** with $v_1 = 1800$, $v_2 = 4000\
\mathrm{m\,s^{-1}}$:

$$ \theta_c = \arcsin(0.45) = 26.74^\circ, \qquad \cos\theta_c = 0.8930, $$
$$ \frac{\partial z}{\partial t_i} = \frac{1800}{2(0.8930)}
= 1007.9\ \mathrm{m\,s^{-1}} \;\Longrightarrow\; 1.01\ \mathrm{m\ per\ ms}. $$

**(b) A 3 m zone at $2200\ \mathrm{m\,s^{-1}}$:**

$$ \Delta t = 2(3)\left(\frac{1}{2200}-\frac{1}{4000}\right)
= 6(4.545\times10^{-4}-2.500\times10^{-4}) = 6(2.045\times10^{-4}) $$
$$ = 1.23\times10^{-3}\ \mathrm{s} = 1.23\ \mathrm{ms}. $$

At a $1\ \mathrm{ms}$ picking error this is **marginally detectable** — the delay
exceeds the error by only 23%, so a favourable pick is needed. The thickness and
the contrast still trade: a 2 m zone at $1600\ \mathrm{m\,s^{-1}}$ gives the same
delay.

**(c) Darcy velocity from a $3.0\ \mathrm{K}$ departure.** For
$T_{\text{top}} = 10\ ^\circ$C, $T_{\text{bot}} = 20\ ^\circ$C and $L = 10\
\mathrm{m}$, the conductive value at $4\ \mathrm{m}$ is $14\ ^\circ$C, so
$T(4) = 11\ ^\circ$C:

$$ \frac{e^{0.4\,\mathrm{Pe}}-1}{e^{\mathrm{Pe}}-1} = \frac{1}{12}
\;\Longrightarrow\; \mathrm{Pe} \approx 3.8, $$

so

$$ v = \frac{\mathrm{Pe}\,\kappa}{L} = \frac{3.8\times10^{-6}}{10}
= 3.8\times10^{-7}\ \mathrm{m\,s^{-1}}. $$

Order of magnitude: a few times $10^{-7}\ \mathrm{m\,s^{-1}}$. Converting to a
permeability needs the hydraulic gradient (an assumption), and to a leak rate
needs the flow area (unknown).

**(d) Distinguishing a reservoir leak from natural discharge.** The
**pressure head**: log the water level in the same borehole (or a nearby
piezometer) and repeat the temperature log while the reservoir level changes. A
leak's advective signal scales with the reservoir head; natural discharge does
not. A tracer test or a second borehole between the reservoir and the log does
the same job more expensively and more convincingly.
