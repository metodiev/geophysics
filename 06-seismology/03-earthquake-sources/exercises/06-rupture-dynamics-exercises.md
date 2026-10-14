# Exercises — 06-03-06 Rupture Dynamics, Fracture Energy and Scaling Laws

Attempt these before reading the
[solutions](./06-rupture-dynamics-solutions.md). The lesson is
[06 Rupture Dynamics, Fracture Energy and Scaling Laws](../06-rupture-dynamics.md)
and the demonstration is
[`../code/rupture_dynamics_demo.py`](../code/rupture_dynamics_demo.py). All values
are **SYNTHETIC**. Unless stated otherwise use $\beta = 3500\ \mathrm{m\,s^{-1}}$,
$\mu = 3.0\times10^{10}\ \mathrm{Pa}$, $k = 0.37$,
$W_{\max} = 15\ \mathrm{km}$ and

$$M_0 = \frac{16}{7}\Delta\sigma a^{3},\quad f_c = \frac{k\beta}{a},\quad
\bar D = \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}a,\quad
G_c = \tfrac12(\tau_p-\tau_r)D_c.$$

## ★ Foundational

**★1.** For a circular rupture with $a = 100\ \mathrm{m}$ and
$\Delta\sigma = 3.0\ \mathrm{MPa}$, compute $M_0$, $f_c$ and the mean slip. State
the unit of each.

**★2.** Compute the saturation corner frequency $f_{c,\text{sat}}$ for
$W_{\max} = 15\ \mathrm{km}$, and state in one sentence what physical length sets
it.

**★3.** For $\tau_p = 80\ \mathrm{MPa}$, $\tau_r = 40\ \mathrm{MPa}$ and
$D_c = 2.0\ \mathrm{m}$, compute the fracture energy $G_c$. State its unit and
say what it represents geometrically on the strength-versus-slip curve.

## ★★ Applied

**★★4.** A rupture has $L = 100\ \mathrm{km}$, $W_{\max} = 15\ \mathrm{km}$ and
$\Delta\sigma = 3.0\ \mathrm{MPa}$. Compute $a$, $f_c$, the mean slip, the rupture
area and $M_0$. State whether this event is on the self-similar or the saturated
branch, and compute $M_0$ a second way from $\mu\,\bar D\times(\text{area})$.

**★★5.** Compute the radiation efficiency for two cases:
(a) $G_c = 1.75\times10^{7}\ \mathrm{J\,m^{-2}}$ with
$E_R = 4.1674\times10^{9}\ \mathrm{J\,m^{-2}}$;
(b) $G_c = 5.00\times10^{8}\ \mathrm{J\,m^{-2}}$ with
$E_R = 1.6673\times10^{9}\ \mathrm{J\,m^{-2}}$.
State which event is more efficient and why, in one sentence.

**★★6.** The demo's first energy loop runs at most $2\times10^{6}$ steps of
$\mathrm{d}t = 10^{-5}\ \mathrm{s}$, and the post-weakening approach to arrest is
exponential with time constant $\eta/\kappa$, where $\eta = \mu/(2\beta)$ and
$\kappa = 6.0\times10^{5}\ \mathrm{Pa\,m^{-1}}$. Compute the time constant, predict
the fractional shortfall of the final slip from its arrest value, and compare with
the demo's measured $6.2\%$.

**★★7.** Define the apparent stress as
$\tau_a \equiv \mu E_R^{\text{total}}/M_0$, where $E_R^{\text{total}}$ is the total
radiated energy. Show that for a rupture of area $A$ and mean slip $\bar D$ this
reduces to $\tau_a = E_R/\bar D$ with $E_R$ the radiated energy **per unit area**,
and evaluate it for the demo's $\tau_r = 10\ \mathrm{MPa}$ row using
$E_R = 4.1674\times10^{9}\ \mathrm{J\,m^{-2}}$.

## ★★★ Research-oriented

**★★★8.** Design a study to *detect* the saturated branch in a real catalogue
conceptually — you have no real data, so specify what you would measure and what
you would plot. State the observable, the predicted kink, the size of a population
needed to see it above scatter in $\Delta\sigma$, and the two model assumptions
that must hold for the kink to be interpretable.

**★★★9.** $G_c$ and $D_c$ are inferred, not measured. Design an inversion that
recovers $D_c$ from observations, and state explicitly the trade-off between
$D_c$ and the strength drop $(\tau_p-\tau_r)$ at fixed radiated energy. Explain
why this makes an *absolute* $D_c$ hard to determine but a *relative* comparison
across a population more robust.

**★★★10.** The demo's narrative states that the integrated final slip "matches
$(\tau_0-\tau_r)/\kappa$ to the same accuracy" as the energy residual. Using the
numbers printed by the demo and the reasoning of Section 3.4 of the lesson,
explain in three or four sentences why the printed $D_f$ values cannot support
that claim, and state the single diagnostic that reveals it.
