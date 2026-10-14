# Solutions — 12-03-03 Thermal Evolution of the Earth and Secular Cooling

> Read after attempting the [exercises](./03-thermal-evolution-exercises.md).
> Lesson: [03 Thermal Evolution and Secular Cooling](../03-thermal-evolution.md).
> Numbers computed, not estimated. All models **SYNTHETIC**.

---

## ★1 — Dimensional check of the balance

$\rho c_p d$ is $\mathrm{kg\,m^{-3}}\times\mathrm{J\,kg^{-1}\,K^{-1}}\times
\mathrm{m} = \mathrm{J\,m^{-2}\,K^{-1}}$; multiplying by
$\mathrm{d}T/\mathrm{d}t$ in $\mathrm{K\,s^{-1}}$ gives
$\mathrm{W\,m^{-2}}$. ✔ The right-hand side is $H$ (a volumetric production times
a depth, $\mathrm{W\,m^{-3}\times m}$) plus two fluxes. Every term is a flux in
$\mathrm{W\,m^{-2}}$. Working per unit area — rather than per unit volume — is
what allows the whole mantle to be a single box.

---

## ★2 — Urey ratio and the direction of change

$$Ur = \frac{H}{q_{\text{surf}}} = \frac{30}{50} = 0.60.$$

$H + q_{\text{cmb}} = 30 + 8 = 38\ \mathrm{mW\,m^{-2}} < 50$, so production plus
core heat does **not** cover the loss and the box is **cooling**. A Urey ratio
below 1 is a necessary condition for cooling (in this accounting), but it does
not fix the rate — see ★★4.

---

## ★3 — Instantaneous budget rate

$$\frac{\mathrm{d}T}{\mathrm{d}t} = \frac{(38-50)\times10^{-3}}{1.19\times10^{13}}
\times3.1557\times10^{16} = -31.8\ \mathrm{K\,Gyr^{-1}}.$$

In mixed units: $-31.8\ \mathrm{K\,Gyr^{-1}} = -31.8\
\mathrm{mK\,Ma^{-1}}$. The conversion factor is $\tfrac{1000}{1000} = 1$, which is
worth verifying rather than trusting: $31.8\ \mathrm{K}$ per $10^{9}$ yr is
$31.8\ \mathrm{mK}$ per $10^{6}$ yr.

---

## ★★4 — Quasi-static rate

Put the box on its equilibrium curve, $q_{\text{surf}}(T) = H(t) + q_{\text{cmb}}$,
and differentiate with respect to time. If $q_{\text{cmb}}$ is constant and only
$H$ decays,

$$\frac{\mathrm{d}q}{\mathrm{d}T}\frac{\mathrm{d}T}{\mathrm{d}t} = \frac{\mathrm{d}H}{\mathrm{d}t}
= -\lambda H
\quad\Longrightarrow\quad
\frac{\mathrm{d}T}{\mathrm{d}t}\bigg|_{\text{qs}} = -\frac{\lambda H}{\mathrm{d}q/\mathrm{d}T}.$$

With $\lambda = \ln 2/6.0\ \mathrm{Gyr} = 1.1552\times10^{-10}\ \mathrm{yr^{-1}}$,
$H = 30\ \mathrm{mW\,m^{-2}} = 3.0\times10^{-2}\ \mathrm{W\,m^{-2}}$ and
$\mathrm{d}q/\mathrm{d}T = 2.5\times10^{-4}\ \mathrm{W\,m^{-2}\,K^{-1}}$:

$$\frac{\mathrm{d}T}{\mathrm{d}t}\bigg|_{\text{qs}}
= -\frac{1.1552\times10^{-10}\times3.0\times10^{-2}}{2.5\times10^{-4}}
= -1.386\times10^{-8}\ \mathrm{K\,yr^{-1}} = -13.9\ \mathrm{K\,Gyr^{-1}}.$$

The instantaneous rate from ★3 is $-31.8$: the box is far from equilibrium at
that instant, which is exactly the information the two rates together convey.

---

## ★★5 — Half-life sensitivity

$Ur = H/q$ contains no time derivative and no $\lambda$, so changing the
half-life leaves **Ur unchanged**. The quasi-static rate is proportional to
$\lambda = \ln 2/T_{1/2}$, so it scales as

$$\frac{\lambda_{6}}{\lambda_{4}} = \frac{4.0}{6.0} = 0.667.$$

The rate falls to two-thirds of its 4-Gyr value. The invariance of $Ur$ is not an
accident: $Ur$ is a ratio of two fluxes at one instant, and the decay rate is a
property of how those fluxes change, which a snapshot cannot see.

---

## ★★6 — Temperature implied by a flux difference

$$T(q) \approx T_0 + \frac{q - q_0}{\mathrm{d}q/\mathrm{d}T}
= 1600 + \frac{45 - 55}{0.3137} = 1600 - 31.9 = 1568.1\ \mathrm{K}.$$

A 10 $\mathrm{mW\,m^{-2}}$ difference in heat loss corresponds to a **31.9 K**
potential-temperature difference — about 2% in absolute terms, but a large change
in the thermal state, because a 32 K hotter mantle has a very different melt
budget and seismic signature. The linearisation is legitimate only because the
step is much smaller than $T - T_s \approx 1330\ \mathrm{K}$.

---

## ★★★7 — A growing core flux

A linear ramp from 0 to $20\ \mathrm{mW\,m^{-2}}$ over
$t = 1.42\times10^{17}\ \mathrm{s}$ has mean $10\ \mathrm{mW\,m^{-2}}$, so

$$\int_0^{t} q_{\text{cmb}}\,\mathrm{d}t = \frac{1}{2}\times2.0\times10^{-2}
\times1.42\times10^{17} = 1.42\times10^{15}\ \mathrm{J\,m^{-2}}.$$

Expressed as an equivalent uniform mantle temperature change,

$$\Delta T = \frac{1.42\times10^{15}}{1.19\times10^{13}}
= 119\ \mathrm{K}.$$

The punchline is the comparison: a *constant*
$10\ \mathrm{mW\,m^{-2}}$ delivers exactly the same $1.42\times10^{15}\
\mathrm{J\,m^{-2}}$ over the same interval, because the ramp's mean equals the
constant. So the cumulative energy is unchanged and the *budget* is unbiased. What
changes is the **timing**: the ramped model puts heat into the mantle early, so to
end at the same present state it must have started cooler, and its early
$T(t)$ is different. Ignoring the core's growth therefore does not bias the
present-day cooling rate; it biases the inferred early thermal history, which is
precisely the quantity that is already hardest to constrain.

---

## ★★★8 — Distinguishing two rheologies

**The problem with heat flow.** The model is calibrated so that
$q_{\text{surf}}$ matches at the present temperature; therefore every $E_a$
reproduces the present-day flux by construction. A present-day heat-flow value has
no discriminating power at all.

**A discriminating observable.** The temperature of the mantle in the past. A
defensible synthetic choice is a dated *palaeo-heat-flow* proxy — for example the
depth of a metamorphic assemblage whose formation temperature is known — that
gives $q_{\text{surf}}$ in a specific 100-Myr window, together with an independent
age. The two rheologies differ in how fast they cool: in the demonstration the
quasi-static rate ranges from $-26.8$ to $-15.5\ \mathrm{K\,Gyr^{-1}}$ between
$E_a = 200$ and $400\ \mathrm{kJ\,mol^{-1}}$, so over 1 Gyr they differ by about
11 K in potential temperature, and over 2 Gyr by 22 K. The required precision is
therefore a past-flux constraint of about 5–10%, i.e.
$\pm3$–$6\ \mathrm{mW\,m^{-2}}$ at 2 Gyr, which is comparable to the precision
achievable on a well-characterised borehole or metamorphic transect.

Alternatively, an independent measurement of $\mathrm{d}q/\mathrm{d}T$ from the
mantle's present-day response to a known perturbation (post-glacial rebound,
whose relaxation time depends on viscosity and its temperature sensitivity) gives
the sensitivity directly, bypassing the flux history.

---

## What a good answer looks like

Every part named which rate it computed, which quantity was measured and which was
calibrated, and never reported a Urey ratio as though it determined a cooling
rate.
