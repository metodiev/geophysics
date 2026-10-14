# Solutions — 04-02-02 Divergent, Convergent and Transform Boundaries

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — A rupture

**(a)** $A = 3.0\times10^4 \times 1.5\times10^4 = 4.5\times10^8$ m².

**(b)** $M_0 = 3\times10^{10} \times 4.5\times10^8 \times 0.8 = 1.08\times10^{19}$ N·m.

**(c)** $M_w = \frac23(\log_{10}1.08\times10^{19} - 9.1) = \frac23(19.0334-9.1)
= \frac23(9.9334) = 6.62$.

**(d)** Doubling the slip doubles $M_0$, and $M_w$ increases by
$\frac23\log_{10}2 = 0.20$, giving 6.82.

---

## ★2 — A magnitude 7.5

**(a)** $M_0 = 10^{1.5\times7.5+9.1} = 10^{20.35} = 2.239\times10^{20}$ N·m.

**(b)** $A = M_0/(\mu D) = 2.239\times10^{20}/(3\times10^{10}\times2.0)
= 3.73\times10^9$ m².

**(c)** $3730$ km² — for example a rupture 150 km long and 25 km wide, which is a
plausible subduction megathrust segment or a long continental strike-slip
segment.

**(d)** $31.6$, because $M_0 \propto 10^{1.5M_w}$ and $10^{1.5} = 31.6$.

---

## ★3 — Obliquity

**(a)** The boundary-normal azimuth is $20° + 90° = 110°$.

**(b)** $v_\perp = 45\cos(110° - 60°) = 45\cos 50° = 28.9$ mm/a. And
$v_\parallel = 45\cos(20° - 60°) = 45\cos(-40°) = 34.5$ mm/a.

**(c)** The obliquity is $\arccos(|v_\parallel|/v) = \arccos(34.5/45) = 40.0°$.

**(d)** Both components are significant, so the boundary is **oblique**. The
normal component is *positive*, which means the plates are separating, so the
boundary is **oblique divergent**, and the normal component produces normal
faulting rather than thrusting. The parallel component produces strike-slip.

---

## ★★4 — Focal mechanisms

**(a)** A dip of 60° with a rake of −90° is a **normal fault**.

**(b)** The demo's computation gives P plunge 15.0° and T plunge 75.0°.

**(c)** The T axis is steeper. That is the rule of thumb: extension means the
maximum tension is near-vertical, because the crust is being pulled apart
vertically as the hanging wall slides down the dipping plane. The P and T axes
both make 45° with the nodal planes, so a 60° dip puts T at 75° and P at 15°.

**(d)** Strike 90°, dip 45°, rake 90° is a **thrust fault**, with P plunge 90.0°
(vertical) and T plunge 0.0° (horizontal), since a 45° dip puts the axes exactly
at the extremes.

---

## ★★5 — The moment budget

**(a)** With $v$ in m/s and the result converted to N·m/a by multiplying by
$3.15576\times10^7$ s:

| Type | $A$ (m²) | $v$ (m/s) | $\dot M_0$ (N·m/a) |
|---|---|---|---|
| Subduction | $3.2\times10^9$ | $1.584\times10^{-9}$ | $4.80\times10^{18}$ |
| Continental transform | $5.0\times10^8$ | $7.92\times10^{-10}$ | $3.75\times10^{17}$ |
| Spreading ridge | $4.4\times10^8$ | $1.426\times10^{-9}$ | $5.94\times10^{17}$ |

**(b)** Total $5.77\times10^{18}$ N·m/a, so the shares are **83.2 per cent**
subduction, 6.5 per cent transform and 10.3 per cent ridge.

**(c)** The demo uses a 100 km subduction width and a 5 km ridge width, which
favours subduction more strongly. Reducing the subduction width to 80 km and
raising the ridge width to 8 km moves the subduction share from 91 to 83 per
cent.

**(d)** The conclusion is unchanged: subduction dominates the moment budget by
roughly an order of magnitude over each other type, and it does so because of its
seismogenic *width* rather than its length or slip rate. A factor-of-two change
in an illustrative width moves the share by a few per cent.

---

## ★★6 — Aseismic coupling

**(a)** $A = 1.0\times10^6 \times 1.5\times10^5 = 1.5\times10^{11}$ m²;
$v = 60\times10^{-3}/3.15576\times10^7 = 1.901\times10^{-9}$ m/s; so
$\dot M_0 = 3\times10^{10}\times1.5\times10^{11}\times1.901\times10^{-9}
= 8.556\times10^{12}$ N·m/s $= 2.700\times10^{20}$ N·m/a.

**(b)** With 60 per cent coupling, $1.620\times10^{20}$ N·m/a.

**(c)** The recurrence interval of a given magnitude is inversely proportional to
the moment rate, so it lengthens by a factor of $1/0.6 = 1.67$: a magnitude 8
interval of 119 years becomes 198 years.

**(d)** It does not change by the same factor, because the *hazard* also depends
on how the aseismic slip is distributed in time and space. Slow slip that
accumulates smoothly reduces the locked-zone stress at the same rate as it
releases it, so it removes the loading entirely; but a margin that releases
60 per cent aseismically may still accumulate the remaining 40 per cent and
release it in full-size events, in which case the maximum magnitude is unchanged
and only the frequency falls. Deciding which applies requires measuring the
coupling, which is why offshore geodetic observatories exist.

---

## ★★★7 — A smaller margin

**(a)** $A = 6.0\times10^5 \times 1.2\times10^5 = 7.2\times10^{10}$ m²;
$v = 70\times10^{-3}/3.15576\times10^7 = 2.218\times10^{-9}$ m/s;
$\dot M_0 = 3\times10^{10}\times7.2\times10^{10}\times2.218\times10^{-9}
= 4.791\times10^{12}$ N·m/s $= 1.512\times10^{20}$ N·m/a.

**(b)** The moment balance requires
$$10^a = \frac{\dot M_0}{2\cdot10^{9.1}\left(10^{0.5M_\text{max}}
- 10^{0.5M_\text{min}}\right)} .$$
The bracket is $10^{4.75} - 10^{3.0} = 5.6234\times10^4 - 1000 = 5.5234\times10^4$,
so the denominator is $2\times1.2589\times10^9\times5.5234\times10^4
= 1.3906\times10^{14}$, and
$10^a = 1.512\times10^{20}/1.3906\times10^{14} = 1.0873\times10^6$, giving
**$a = 6.036$**.

**(c)** The rate of $M_w \ge 8$ is $10^{6.036-8} = 1.0873\times10^{-2}$ per year,
so the mean interval is **92 years**.

**(d)** With 60 per cent coupling the moment rate is $0.6\times1.512\times10^{20}
= 9.072\times10^{19}$ N·m/a, so $\log_{10}$ of the right-hand side falls by
$\log_{10}(1/0.6) = 0.2218$ and $a = 5.814$. The $M_w\ge8$ interval becomes
**153 years**. The two numbers bracket the range that the unknown coupling
coefficient places on the recurrence: 92 years if every millimetre of
convergence is released seismically, 153 years if only 60 per cent is.

---

## ★★★8 — The demo's output

**(a)**

| Mechanism | P plunge | P azimuth | T plunge | T azimuth |
|---|---|---|---|---|
| normal (0/45/−90) | 0.0 | 90.0 | 90.0 | 225.1 |
| thrust (0/30/90) | 75.0 | 270.0 | 15.0 | 90.0 |
| strike-slip (0/90/0) | 0.0 | 45.0 | 0.0 | 135.0 |
| oblique normal (30/55/−60) | 5.5 | 279.2 | 65.1 | 177.2 |

**(b)** Strike-slip gives `- + + - - + + -` — four alternating quadrants.
Normal gives `- + + + - + + +` and thrust `+ + + + + - - -` at the sampled
take-off angle — two quadrants each.

**(c)** For a strike of 0°: at azimuth 90° the velocity is entirely normal
(`v_normal 50.0, v_parallel 0.0`, "divergent (near-orthogonal)"); at 60°
(`60.6, 35.0`, "oblique divergent"); at 0° (`0.0, 40.0`, "transform
(near-parallel)").

**(d)** 50 km × 20 km with 1.0 m slip gives `M0 = 3.000e+19, Mw = 6.92`;
200 km × 50 km with 2.0 m gives `M0 = 6.000e+20, Mw = 7.79`. The factor is
**20** in moment over 0.87 of magnitude.

**(e)** Subduction 91 per cent, spreading ridge 5 per cent, continental
transform 3 per cent, continental collision 2 per cent.

**(f)** The boundary lengths, seismogenic widths and slip rates are labelled
`ILLUSTRATIVE`, because they are order-of-magnitude values rather than
measurements of specific margins. The conclusion — that subduction dominates —
is robust to changing them by a factor of two, and stating the inputs as
illustrative is what allows a reader to check that claim instead of having to
trust it.

---

## ★★★9 — The P/T sign convention

**(a)–(b)** Reversing the slip vector's sign flips the sign of the moment tensor,
so its largest and smallest eigenvalues exchange and the **P and T axes swap**:
the normal mechanism becomes P plunge 90 / T plunge 0 and the thrust becomes
P plunge 15 / T plunge 75. The plunge and azimuth of each axis are otherwise
unchanged, and the null axis is unchanged.

**(c)** The convention must be checked against the catalogue's own documentation
rather than assumed, because both are in use: some catalogues report the
hanging-wall slip with the upward normal (giving a steep T for normal faulting)
and others use the opposite sign. The check is to take an event with a known
normal-faulting mechanism and observe whether the reported T axis is steep or
shallow — a step that is worth doing once and noting for the catalogue in
question.

**(d)** Because the radiation amplitude is
$A_P \propto (\hat{\mathbf{r}}\cdot\mathbf{n})(\hat{\mathbf{r}}\cdot\mathbf{s})$,
which is unchanged when $\mathbf{s} \to -\mathbf{s}$. The physical
first-motion pattern is a property of the *fault plane and slip direction as
lines*, not of the arbitrary sign attached to them, so the observed quadrant
pattern cannot distinguish the two conventions. Only a convention, or an
independent observation such as the surface rupture, does.
