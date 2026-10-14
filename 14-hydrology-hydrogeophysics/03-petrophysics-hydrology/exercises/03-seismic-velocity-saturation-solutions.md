# Solutions — 14-03-03 Seismic Velocity vs Saturation and Gassmann

> Read after attempting. Lesson:
> [03 Seismic Velocity vs Saturation and Gassmann](../03-seismic-velocity-saturation.md).
> All models **SYNTHETIC**. $K_w = 2.20\ \mathrm{GPa}$,
> $K_g = 1.0\times10^{-4}\ \mathrm{GPa}$.

---

## ★1 — Gassmann at full saturation

Numerator: $\left(1 - K_\text{dry}/K_\text{min}\right)^{2}
= (1 - 9/36)^{2} = 0.75^{2} = 0.5625$.

Denominator with $K_\text{fl} = 2.20\ \mathrm{GPa}$:

$$\frac{\phi}{K_\text{fl}} + \frac{1-\phi}{K_\text{min}}
 - \frac{K_\text{dry}}{K_\text{min}^{2}}
= \frac{0.25}{2.20} + \frac{0.75}{36} - \frac{9}{36^{2}}
= 0.113636 + 0.020833 - 0.006944 = 0.127525 .$$

$$K_\text{sat} = 9.00 + \frac{0.5625}{0.127525} = 9.00 + 4.4109
= 13.4109\ \mathrm{GPa}.$$

$$\rho = 0.75\times2650 + 0.25\times1000 = 1987.5 + 250 = 2237.5\ \mathrm{kg\,m^{-3}}.$$

$$V_p = \sqrt{\frac{(13.4109 + \tfrac43\times8.00)\times10^{9}}{2237.5}}
= \sqrt{\frac{24.0776\times10^{9}}{2237.5}} = 3.2804\ \mathrm{km\,s^{-1}},$$

$$V_s = \sqrt{\frac{8.00\times10^{9}}{2237.5}} = 1.8909\ \mathrm{km\,s^{-1}}.$$

---

## ★2 — Wood fluid modulus

$$\frac{1}{K_\text{fl}} = \frac{S_w}{2.20} + \frac{1-S_w}{1.0\times10^{-4}} .$$

| $S_w$ | $K_\text{fl}$ (GPa) | ratio to $K_w$ |
|---|---|---|
| 0.5 | $1.9999\times10^{-4}$ | $9.1\times10^{-5}$ |
| 0.9 | $9.996\times10^{-4}$ | $4.5\times10^{-4}$ |
| 1.0 | 2.200 | 1.0 |

At $S_w = 0.9$ the fluid modulus is still four orders of magnitude below the
water value. The **harmonic** average is controlled by the softest component: a
tenth of the pore space filled with a modulus $2\times10^{4}$ times smaller than
water dominates the series sum. Only when $1-S_w$ becomes comparable to
$K_g/K_w = 4.5\times10^{-5}$ does water take over — which is why the velocity
minimum sits at $S_w \approx 0.99$ and not at some intuitive midpoint.

---

## ★3 — Shear modulus

Gassmann gives $\mu_\text{sat} = \mu_\text{dry}$, because a fluid at rest cannot
support a shear stress: the pores deform at constant volume under shear, the
pore pressure does not change, and the fluid never enters the stress–strain
relation. Hence $V_s = \sqrt{\mu_\text{dry}/\rho}$ and the fluid acts only through
$\rho$.

For ★1: $\rho(S_w = 0) = 0.75\times2650 + 0.25\times1.2
= 1987.8\ \mathrm{kg\,m^{-3}}$, so
$V_s = \sqrt{8.00\times10^{9}/1987.8} = 2.0064\ \mathrm{km\,s^{-1}}$, against
$V_s(S_w = 1) = 1.8909\ \mathrm{km\,s^{-1}}$. The change is
$\mathbf{115.5\ \mathrm{m\,s^{-1}}}$ — pure density, entirely explained by
$\rho$ rising from $1987.8$ to $2237.5\ \mathrm{kg\,m^{-3}}$.

---

## ★★4 — Patchy $K_\text{sat}$

End members from the demonstration: $K_\text{sat}(S_w = 1) = 12.0428\ \mathrm{GPa}$
and $K_\text{sat}(S_w = 0) = 8.0002\ \mathrm{GPa}$.

$$K_\text{sat}^\text{patchy}(0.5) = 0.5\times12.0428 + 0.5\times8.0002
= 6.0214 + 4.0001 = 10.0215\ \mathrm{GPa}.$$

$\rho(0.5) = 2005.2\ \mathrm{kg\,m^{-3}}$, so

$$V_p = \sqrt{\frac{(10.0215 + \tfrac43\times7.00)\times10^{9}}{2005.2}}
= \sqrt{\frac{19.3548\times10^{9}}{2005.2}} = 3.1068\ \mathrm{km\,s^{-1}}.$$

---

## ★★5 — Uniform versus patchy at $S_w = 0.5$

Uniform: $K_\text{fl} = 2.0\times10^{-4}\ \mathrm{GPa}$, so
$K_\text{sat} = 8.0004\ \mathrm{GPa}$ and (from the demonstration)
$V_p = 2.9401\ \mathrm{km\,s^{-1}}$.

Patchy: $V_p = 3.1068\ \mathrm{km\,s^{-1}}$.

$$\Delta V_p = 3.1068 - 2.9401 = 0.1667\ \mathrm{km\,s^{-1}}
= \mathbf{166.7\ \mathrm{m\,s^{-1}}} .$$

**Safer default.** With no other information, **uniform** mixing is the safer
default, because it corresponds to a well-mixed pore fluid, which is the
expectation in an aquifer that has been recharged and drained slowly. Patchy
saturation requires a mechanism to segregate the fluids on a length scale much
larger than the pore — for example a gas charge displacing water in a
heterogeneous sand. Note that "safer" means "less likely to be wrong by
$300\ \mathrm{m\,s^{-1}}$", not "correct": the honest statement is that the
geometry is unknown and the ambiguity is $\sim2\times10^{2}\ \mathrm{m\,s^{-1}}$.

---

## ★★6 — Where $V_p$ has dropped 100 m/s, and where it recovers

Dry value: $V_p(S_w = 0) = 3.0565\ \mathrm{km\,s^{-1}}$. Target:
$2.9565\ \mathrm{km\,s^{-1}}$. Numerically,

$$V_p = 2.9565\ \mathrm{km\,s^{-1}}\ \text{at}\ S_w = 0.426 .$$

The rising-branch crossing of the dry value occurs only at
$S_w = 0.99998$, i.e. effectively at full saturation.

**Asymmetry.** The falling branch is long — it occupies the first $43\%$ of the
saturation range and more than half of the total velocity drop. The recovery
happens in the last $0.002\%$ of the range. The reason is the same harmonic-average
argument as ★2: $K_\text{fl}$ does not become comparable to $K_w$ until the gas
fraction is at the $10^{-4}$ level. A hydrological interpretation of a
"$100\ \mathrm{m\,s^{-1}}$ velocity drop" is therefore consistent with a very
wide range of saturations, and a "$V_p$ back to dry" reading means the rock is
essentially fully saturated, not half.

---

## ★★7 — The $K_\text{fl} = K_\text{min}$ limit

Substitute $K_\text{fl} = K_\text{min}$ into the denominator:

$$\frac{\phi}{K_\text{min}} + \frac{1-\phi}{K_\text{min}}
 - \frac{K_\text{dry}}{K_\text{min}^{2}}
= \frac{1}{K_\text{min}} - \frac{K_\text{dry}}{K_\text{min}^{2}}
= \frac{K_\text{min} - K_\text{dry}}{K_\text{min}^{2}} .$$

The numerator is $\left(1 - K_\text{dry}/K_\text{min}\right)^{2}
= (K_\text{min} - K_\text{dry})^{2}/K_\text{min}^{2}$. Dividing,

$$K_\text{sat} = K_\text{dry}
+ \frac{(K_\text{min} - K_\text{dry})^{2}/K_\text{min}^{2}}
{(K_\text{min} - K_\text{dry})/K_\text{min}^{2}}
= K_\text{dry} + (K_\text{min} - K_\text{dry}) = K_\text{min} .$$

Independent of $\phi$, $K_\text{dry}$ and $\mu$: the identity must hold for
every model. Checking it is the first thing to do after implementing Gassmann,
because it exercises the algebra of the denominator where sign errors hide.

---

## ★★★8 — The ambiguity at $V_p = 2.90\ \mathrm{km\,s^{-1}}$

**(a)** The patchy curve of the demonstration rises monotonically from
$3.0565\ \mathrm{km\,s^{-1}}$ at $S_w = 0$ to $3.1495\ \mathrm{km\,s^{-1}}$ at
$S_w = 1$. Its minimum over the whole range is therefore $3.0565\ \mathrm{km\,s^{-1}}$
at $S_w = 0$, which is $156\ \mathrm{m\,s^{-1}}$ **above** the reported value.
No saturation reproduces $2.90\ \mathrm{km\,s^{-1}}$ under the patchy assumption.

**(b)** Hold $\mu_\text{dry} = 7.0\ \mathrm{GPa}$ and lower the frame to
$K_\text{dry} = 7.0\ \mathrm{GPa}$. The uniform curve then takes the value
$2.9000\ \mathrm{km\,s^{-1}}$ at $S_w = 0.2897$. So the two admissible
interpretations are

- $K_\text{dry} = 8.0\ \mathrm{GPa}$, $S_w = 0.687$ (uniform), and
- $K_\text{dry} = 7.0\ \mathrm{GPa}$, $S_w = 0.290$ (uniform),

which differ by a factor of $2.4$ in water content.

**(c)** The resolving measurement must constrain the **dry frame independently
of the fluid**. The natural choice is $V_s$ (or a $V_p/V_s$ ratio), because
Gassmann makes $V_s$ fluid-independent, so the measured $V_s$ and $\rho$ fix
$\mu_\text{dry}$ directly. A shear measurement plus density converts the
problem from one equation in two unknowns to two equations in two.

**(d)** A more accurate $V_p$ would not help because the ambiguity is not noise:
each $(K_\text{dry}, S_w)$ pair lies on the *same* forward curve and predicts
the same $V_p$ to the last digit. Reducing the measurement error shrinks the
error bars along the curve, not the curve itself. Only new information about the
frame — a different data type, or an independent porosity — reduces the admitted
set.

---

## ★★★9 — Testing uniform versus patchy mixing (model answer)

**(a)** **Protocols.** Uniform saturation is produced by *increasing* water
saturation on a water-wet sample, either by slow imbibition from a water-wet
membrane or by humidity equilibration, because the wetting phase then advances
frontally and each pore fills with a mixture at a common capillary pressure.
Patchy saturation is produced by *draining* a fully saturated sample with gas:
gas invades the largest pores first and occupies connected pathways, leaving
water in the small pores and in the fine layers, so the two fluids sit in
different patches whose size grows with the saturation contrast. Reporting which
protocol produced the curve is essential, because the same rock tested both ways
gives two curves.

**(b)** **Frequency.** The Gassmann limit requires the pore pressure to equalise
within a half-cycle, i.e. frequencies low compared with
$f_c \sim K_\text{fl}\kappa/(\eta L^{2})$ for the relevant patch length $L$.
For laboratory plugs, that usually means low-frequency (e.g. forced-oscillation
or resonance) techniques rather than the megahertz ultrasonic pulse, whose
wavelength approaches the pore scale and whose velocity is a high-frequency
limit. Measuring patchy saturation at ultrasonic frequency would test a
different physics and would not falsify or confirm the Gassmann branch.

**(c)** **Plot and signature.** Plot $V_p$ (and $V_s/\rho$-derived
$\mu_\text{dry}$) against $S_w$ with the two model curves overlaid. Signature of
uniform mixing: a $V_p$ minimum near $S_w \approx 0.99$, a fall of
$\sim2\times10^{2}\ \mathrm{m\,s^{-1}}$ at mid-saturation, and $V_p$ at
$S_w = 0.5$ well *below* the dry value. Signature of patchy mixing: monotonic
$V_p$ with no interior minimum, and $V_p(0.5)$ close to the arithmetic mean of
the end members. In both cases $V_s$ must vary only through $\rho$; a deviation
in $V_s$ falsifies the dry frame rather than the mixing model.

**(d)** An intermediate answer, with $V_p(0.5)$ between the two predicted curves,
implies that the fluid patches are comparable to the diffusion length at the
measurement frequency — the **dispersive** regime, where Gassmann is not valid
at either limit. The correct response is a mesoscopic-loss model with a patch
length as a parameter, and a second frequency measurement to constrain it. Note
what an intermediate result does *not* justify: quoting a saturation from the
uniform curve and calling the residual "noise".
